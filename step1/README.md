# Step1!
このディレクトリでは、dockerfileを使って、コンテナを一つ立ち上げます。

## ファイルの簡単な解説

### app.py
これは、80番ポートの"/"に対して、httpリクエストが来ると、
```
  <h1>Hello,World!</h1> 
```
を返すだけサーバーを開くものです。

### dockerfile
ここでは、コンテナのイメージについて、記述しています。
ベースとなるイメージはubuntuの22.04としています。また、app.pyを走らせるために必要なライブラリ群をインストールしています。
RUN はその後の、コマンドを実行してそれをイメージに反映してくれる感じです。RUNをたくさん使ってもいいのですが、dockerの仕様上RUNを一回使うと、レイヤーが一つ増える形になるので、RUNを複数回使うよりも RUN command && command 〜　という感じに一つに連ねたほうがいい場合が多いです。

## 使い方

### dockerイメージのビルド
dockerfileを配置したディレクトリに移動して以下のコマンドを打ちます。
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

## 立ち上がりの確認
ビルドしたdokcerイメージを起動したあと、ブラウザやcurlなどで、http://localhost:8080/ にアクセスするとHelloWorldが返ってきます。