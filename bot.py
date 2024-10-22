import discord
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Discordのボットトークンを取得
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

# トークンとチャットチャンネルを管理する辞書
token_channels = {}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

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
        await message.channel.send(f"このチャンネルはトークン '{token}' にリンクされました。")

    # メッセージを転送する処理（テキスト、画像、動画に対応）
    else:
        # 送信元チャンネルがどのトークンに関連しているか確認
        for token, channels in token_channels.items():
            if message.channel in channels:
                # 転送するメッセージのフォーマットを作成
                forward_message = (
                    f"[{message.guild.name}]\n"  # サーバー名の後に改行を追加
                    f"{message.author}: {message.content}"
                )

                # 同じトークンに関連する他のチャンネルにメッセージを送信
                for channel in channels:
                    if channel != message.channel:  # 自分のチャンネルには送らない
                        await channel.send(forward_message)

                        # 添付ファイルがある場合、それも転送（画像、動画）
                        if message.attachments:
                            for attachment in message.attachments:
                                await channel.send(file=await attachment.to_file())

client.run(TOKEN)