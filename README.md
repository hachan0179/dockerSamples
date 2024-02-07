# はじめに 
これはDocker Composeを使ったものを作るにあたってステップに分けて使い方を学ぶためのディレクトリです。
- step0.環境構築やdockerの基礎コマンド、また参考文献となるサイトなどのURL
- step1.単一のdockerfileを使って作ったコンテナを立ち上げる
- step2.docker-composeを使って立ち上げる
- step3.mysqlのコンテナを追加して、コンテナ間で通信をさせる
- step4.nginxをリバースプロキシとして導入し、通信を中継させる。
- step5.さらにTCP通信を行うサーバーを一つ追加し、サブドメインによる管理を行う。

# 使用ライブラリなど
- bottle (pythonのwebフレームワーク)
- peewee (mysqlをpythonで操作するためのもの)
