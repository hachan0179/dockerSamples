# はじめに 
これはDocker Composeを使ったものを作るにあたってステップに分けて使い方を学ぶためのディレクトリです。
- step0.環境構築やdockerの基礎コマンド、また参考文献となるサイトなどのURL
- step1.単一のdockerfileを使って作ったコンテナを立ち上げる
- step2.step1で作成したコンテナをdocker-composeを使って立ち上げる
- step3.step2で作成したdocker-composeにmysqlのコンテナを追加して、コンテナ間で通信をさせる

# 使用ライブラリなど
- bottle (pythonのwebフレームワーク)
- peewee (mysqlをpythonで操作するためのもの)
