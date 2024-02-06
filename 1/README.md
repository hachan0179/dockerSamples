# 第一ステップ
このディレクトリでは、dockerfileを使って、コンテナを一つ立ち上げます。

### dockerイメージのビルド
```
docker build -t bottle-app .
```

### ビルドしたdockerイメージでコンテナを起動
```
docker run -it -d --rm -p 8080:8080 --name bottle-container bottle-app
```

### 起動したdockerコンテナの停止
```
docker stop bottle-container
```

### ビルドしたdockerイメージの削除
```
docker image rm bottle-app
```

### まとめたもの
上のコマンドをrun.shにまとめてあります。
```
chmod u+x run.sh
```
のあと、
```
./run.sh [option]
```
で利用できます。
```
Usage : ./run.sh [AN OPTION]
Options:
  -b  --build     Build the docker image
  -r  --run       Run the docker image
  -s  --stop      Stop the docker container
  -e  --exec      Execute bash in runnig contaicer
  -c  --clear     Delete the docker image
```