# 第一ステップ
このディレクトリでは、dockerfileを使って、コンテナを一つ立ち上げます。

### dockerイメージのビルド
```
docker build -t bottle-app .
```
カレントディレクトリにあるdockerfileを使って、dockerイメージをビルドしています。
作られるイメージの名前は -t オプションで bottle-app に指定しています。

### ビルドしたdokcerイメージを起動
```
docker run -it -d --rm -p 8080:80 --name bottle-container bottle-app
```
上でビルドしたイメージを、起動しています。
-p オプションで、ローカルの8080番ポートとコンテナ内の80番ポートをつなげています。これにより、localhost:8080 にアクセスすると、コンテナ内の80番ポートに立っているサーバーにアクセスできます。
--rm オプションでコンテナを停止した際に自動的にコンテナが削除られるようになっています。

### 起動したコンテナの停止
```
docker stop bottle-container
```
イメージの起動の際 --rm オプションをつけているため、コンテナを停止すると自動的にコンテナが削除されます。
--rm オプションをつけない場合は
```
docker rm bottle-container
```
でコンテナを消去する必要があります。

### ビルドしたdockerイメージの削除
```
docker image rm bottle-app
```

### まとめたもの
打つのが面倒なので、上のコマンドをrun.shにまとめてあります。
```
chmod u+x run.sh
```
のあと、
```
./run.sh [option]
```
で利用できます。以下使用方法です。
```
Usage : ./run.sh [AN OPTION]
Options:
  -b  --build     Build the docker image
  -r  --run       Run the docker image
  -s  --stop      Stop the docker container
  -e  --exec      Execute bash in runnig contaicer
  -c  --clear     Delete the docker image
```