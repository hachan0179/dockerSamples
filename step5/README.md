# step5
step4に加え、さらにTCP通信を行うコンテナを一つ追加し、サブドメインによる管理を行います。

## ファイルの簡単な解説
### docker-compose.yml (./docker-compose.yml)
新しくTCP通信を行うコンテナであるc-apiコンテナを追加しています。また、capi.localhostの4000番ポートにアクセスするとc-apiコンテナにつながるようにしたいので、新しくホストの4000番ポートとnginxの4000番ポートをつないでいます。

### dockerfile (./c-api/dockerfile)
ここでは、TCP通信を行うコンテナに必要なものを記述しています。具体的には、c言語で書かれたプログラムをコンパイルするために必要なbuild-essentialとTCP通信をするためのsocatコマンドを追加しています。docker-compose.ymlでhello.cをコンテナ内の/optに配置しているので、コンテナが起動すると/optの中で、hello.cをコンパイルしTCPの4000番ポートに接続することで、アクセスが来るとHello,c-api-container!と返すようにしています。

### hello.c (./volumes/c-api/hello.c)
単に、標準出力にHello,c-api-container!を表示するだけのものです。

### nginx.conf (./volumes/nginx-proxy/nginx.conf)
capi.localhostの4000番ポートにTCP通信が来ると、c-apiコンテナに中継するように設定を追加しています。

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
基本的な動作はstep4と同じになりますが、capi.localhostの4000番ポートにncなどするとHello,c-api-container!が返ってきます。