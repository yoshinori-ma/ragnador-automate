# ragnador

ソシャゲの自動周回スクリプト
Androidのシミュでアプリを立ち上げて使用する想定
- 起動やフォアグラウンド処理も自動でやりたかったが諦めた
- ウィンドウの位置の割り出しなども本来自動でやるべきだが、手動で特定位置にウィンドウを配置して動くようにした覚えがある
- win, mac それぞれで試して最終的にmacでやった
- wsl2からwin側の画面にアクセスするのが難しかった（無理だった？
- macはmacでretinaの画素数の違いとかがあった

自動周回は現状必要がないので全く保守はしていない
pyautoguiを使ってみたかった、実際簡単に画面の動きを検知して操作が自動化できて楽しかった
