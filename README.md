<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Linkify README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #ecf0f1;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 4px;
            overflow: auto;
        }
        ul {
            margin: 10px 0;
            padding: 0 20px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<h1>Linkify</h1>

<h2>概要</h2>
<p>Linkifyは、Discordサーバー間でメッセージやメディア（テキスト、画像、動画）を簡単に共有できるボットです。特定のコマンドを使って、ユーザーはメッセージを異なるサーバーに転送することができます。このボットは、コミュニティ間の情報共有を促進し、より良いコミュニケーションを実現します。</p>

<h2>主な機能</h2>
<ul>
    <li><strong>メッセージ転送</strong>: 異なるDiscordサーバー間でテキストメッセージを転送。</li>
    <li><strong>メディアサポート</strong>: 画像や動画も一緒に転送可能。</li>
    <li><strong>トークンによるリンク設定</strong>: 各サーバーで特定のトークンを使って、メッセージの転送先を設定。</li>
    <li><strong>見やすいメッセージフォーマット</strong>: サーバー名とユーザー名を強調表示し、メッセージを読みやすく。</li>
</ul>

<h2>インストール手順</h2>
<ol>
    <li><strong>Pythonのインストール</strong>: LinkifyはPythonで作成されていますので、Pythonがインストールされている必要があります。 <a href="https://www.python.org/downloads/">Pythonのダウンロードページ</a>から最新のバージョンをインストールしてください。</li>
    
    <li><strong>必要なライブラリのインストール</strong>: ターミナルまたはコマンドプロンプトを開き、以下のコマンドを実行して必要なライブラリをインストールします。
        <pre><code>pip install discord.py python-dotenv</code></pre>
    </li>
    
    <li><strong>ボットの作成</strong>: 
        <ul>
            <li><a href="https://discord.com/developers/applications">Discord Developer Portal</a>にアクセスし、新しいアプリケーションを作成します。</li>
            <li>「Bot」タブに移動し、「Add Bot」ボタンをクリックしてボットを作成します。</li>
            <li>トークンをコピーし、後で使用するために保存します。</li>
        </ul>
    </li>
    
    <li><strong>環境変数の設定</strong>: プロジェクトフォルダに <code>.env</code> ファイルを作成し、以下の内容を追加します。
        <pre><code>DISCORD_TOKEN=あなたのボットトークン</code></pre>
    </li>
    
    <li><strong>ボットの実行</strong>: <code>bot.py</code> ファイルを作成し、提供されたボットのコードをコピー＆ペーストします。その後、ターミナルで以下のコマンドを実行してボットを起動します。
        <pre><code>python bot.py</code></pre>
    </li>
</ol>

<h2>使用方法</h2>
<ol>
    <li>Discordサーバーで、ボットがいることを確認します。</li>
    <li>メッセージを転送したいサーバーのチャットで <code>/token &lt;トークン名&gt;</code> と入力してトークンを設定します。</li>
    <li>他のサーバーでも同様に <code>/token &lt;トークン名&gt;</code> を入力します（同じトークンを使用）。</li>
    <li>その後、メッセージや画像、動画を送信すると、それが設定された他のサーバーに転送されます。</li>
</ol>

<h3>メッセージフォーマット</h3>
<p>転送されるメッセージは以下のような形式で表示されます：</p>
<pre><code>**【サーバー名】**
**<ユーザー名>**: <メッセージ内容></code></pre>

<h2>注意事項</h2>
<ul>
    <li>ボットがメッセージを転送するためには、必要な権限を持っている必要があります。サーバー管理者がボットに適切な権限を与えることを確認してください。</li>
    <li>ボットは、トークンに関連付けられたチャンネル間でのみメッセージを転送します。他のサーバーやチャンネルには送信されません。</li>
</ul>

<h2>コントリビュート</h2>
<p>このプロジェクトへの貢献は大歓迎です！バグの報告や機能の提案を行っていただければ、プロジェクトを改善する手助けとなります。</p>

<h2>ライセンス</h2>
<p>このプロジェクトは <a href="LICENSE">MIT License</a> の下で提供されています。</p>

</body>
</html>