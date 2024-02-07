# Step2!
step1で作成したコンテナをdocker-composeを使って立ち上げます。
ディレクトリの構成に関しては、今後コンテナを増やしていきたいので、拡張性がありそうなディレクトリ構成にしています。

## ファイルの簡単な解説
### docker-compose.yml
ここでは、docker-composeの設定を記述しています。
./bottle-app にある dockerfile を使って bottle-app という docker のイメージを作成し、それを使って、bottle-app-container という名前のコンテナを作成するようにしています。
そして、そのコンテナの80番ポートとローカルの8080番ポートを接続しています。
また、./volumes/bottle-app をコンテナ内の /opt/bottle-app/ に配置しています。

### app.py
step1のものをそのまま使用しています。

### dockerfile
基本的にはstep1のもので、step1のときと異なりディレクトリの配置をdocker-composeの方でやっているので、COPYのくだりを削除しています。

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
ビルドしたdokcerイメージを起動したあと、ブラウザやcurlなどで、http://localhost:8080/ にアクセスするとHelloWorldが返ってきます。