# step4!
ここでは、step3までに構築したdokcer-composeにnginxをリバースプロキシとして導入し、通信を中継させます。

## ファイルの簡単な解説
### docker-compose.yml
今回登場するnginxの記述を加えています。また、nginxを導入することでホストの8080番ポートと接続されるのは、このnginxの80番ポートになるので、いままでbottle-appの80番につないでいたものを繋ぎ変えています。

### nginx.conf (./volumes/nginx-proxy/nginx.conf)
今回は、リバースプロキシとして導入するのでそのためのコンフィグファイルです。80番ポートにhttpリクエストがあると、それをbottle-appの80番ポートに投げてくれるようにしています。

## 使い方
### docker-compose のビルド
docker-compose.ymlが配置されているディレクトリ内で以下のコマンドを打ちます。
```
docker-compose build
```

### docker-compose の起動
```
docker-compose up -d
```
-d オプションにより、バックグラウンドで立ち上がります。-dをつけずに起動すると、実行したシェルにログが出力されます。

### docker-compose の停止
```
docker-compose down
```
起動しているコンテナを停止できます。

## 立ち上がりの確認
ここの動作は、クライアント目線だとstep4と変わりません。ビルドしたdokcerイメージを起動したあと、1分ほどbottle-app-containerとmysql-dbが立ち上がるのを待ったあと、ブラウザやcurlなどで、http://localhost:8080/ にアクセスするとHelloWorldが返ってきます。また、http://localhost:8080/show/hachan にアクセスるとパスワード表示されます。