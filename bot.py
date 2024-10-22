import os
from dotenv import load_dotenv
from supabase import create_client
import discord

# .envファイルから環境変数を読み込む
load_dotenv()

# Discordのボットトークンを取得
TOKEN = os.getenv('DISCORD_TOKEN')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Supabaseクライアントの作成
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

client = discord.Client(intents=discord.Intents.all())

# トークンとチャットチャンネルを管理する辞書
token_channels = {}

async def load_token_channels():
    """Supabaseからトークンとチャンネルのマッピングを読み込む"""
    response = supabase.table('token_channels').select('*').execute()

    # Supabaseからのレスポンスにデータがない場合
    if response.data:
        # データが存在する場合
        for row in response.data:
            token = row['token']
            channel_id = row['channel_id']
            if token in token_channels:
                token_channels[token].append(discord.Object(id=channel_id))
            else:
                token_channels[token] = [discord.Object(id=channel_id)]
        print("Loaded token channels:", token_channels)  # 読み込んだチャンネルを表示
    else:
        print("No data found or error retrieving data.")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await load_token_channels()  # ボット起動時にトークンとチャンネルを読み込む

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # トークン設定コマンド "/token <トークン名>"
    if message.content.startswith('/token '):
        token = message.content.split()[1]  # トークンを取得
        if token in token_channels:
            token_channels[token].append(message.channel)
        else:
            token_channels[token] = [message.channel]

        # Supabaseにトークンとチャンネルを保存
        supabase.table('token_channels').insert({'token': token, 'channel_id': str(message.channel.id)}).execute()

        await message.channel.send(f"このチャンネルはトークン '{token}' にリンクされました。")
        return

    # メッセージを転送する処理
    for token, channels in token_channels.items():
        print(f"トークン '{token}' に関連するチャンネルをチェックしています: {[channel.id for channel in channels]}")

        if message.channel.id in [channel.id for channel in channels]:
            forward_message = (
                f"[{message.guild.name}]\n"  # サーバー名の後に改行を追加
                f"{message.author}: {message.content}"
            )

            for channel in channels:
                if channel != message.channel:  # 自分のチャンネルには送らない
                    try:
                        channel_to_send = await client.fetch_channel(channel.id)
                        await channel_to_send.send(forward_message)
                        print(f"メッセージをチャンネル {channel.id} に転送しました。")

                        # 添付ファイルがある場合、それも転送（画像、動画）
                        if message.attachments:
                            for attachment in message.attachments:
                                await channel_to_send.send(file=await attachment.to_file())
                                print(f"添付ファイルをチャンネル {channel.id} に送信しました。")

                    except discord.NotFound:
                        print(f"チャンネル {channel.id} が見つかりません。")
                    except discord.Forbidden:
                        print(f"ボットがチャンネル {channel.id} にメッセージを送信する権限を持っていません。")
                    except Exception as e:
                        print(f"チャンネル {channel.id} にメッセージを送信中にエラーが発生しました: {e}")

    # デバッグ用に、受信したチャンネルIDを表示
    print(f"チャンネル {message.channel.id} でメッセージを受信しました。")

# ボットの実行
client.run(TOKEN)