# iconResize
### iOS開発者向けツールです。
Icon resizing tool for iOS developers.

アプリアイコン画像（1024px）を１つ作るだけで残りは　iconResize.pyでリサイズし出力してくれます。

### ツールの内容

.png画像を以下のpxへリサイズして出力します。

20px,29px,40px,58px,60px,76px,80px,87px,120px,152px,167px,180px

### 前提条件
・pythonプログラム実行可能な環境であること。

・Python画像処理ライブラリ『Pillow』が利用可能な環境であること/n

### 使い方

リサイズしたい.png画像の名前をicon.pngにリネーム

iconResize.pyと同じフォルダ内にicon.pngを配置

iconResize.py実行すると、リサイズされた.pngが同じフォルダ内に出力
