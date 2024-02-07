# Step3!
step2で作成たdocker-composeにmysqlのデータベースサーバーを配置して、そのmysqlとbottle-app-containerを通信させます。

## docker-compose内での通信について
docker-compose内でコンテナ同士を通信させるには、docker-compose.ymlでserviceの一つ下位に設定した名前をホスト名として通信させることができます。今回の場合、bottle-appから、mysql-dbのデータベースへアクセスするためには、ホスト名をmysql-dbとしてポート番号をmysqlのデフォルトのポート番号である3306に指定することでできます。

## ファイルの簡単な解説
### docker-compose.yml (./docker-compose.yml)
step2のものをベースにmysqlを追加しています。./mysql-dbのdockerfileをもとにイメージを作成して、mysql-db-containerとしてコンテナを実行しています。また、mysqlのスキーマの初期設定のファイルをコンテナ内の/docker-entrypoint-initdb.d/に配置しています。今回はまだアカウントまわりは触らずにroot権限のままやるので、mysqlのroot権限のパスワードだけ環境変数から設定しています。

### app.py (./volumes/bottle-app/app.py)
step2のものをベースにmysqlと通信させるように変更しています。まず、idとusername、passwordを持つUserテーブルを作成して、一つレコードを登録しています。/show/username にhttpリクエストがあると、mysql-dbと通信して、usernameと同じユーザーを探して、そのユーザーのpasswordを返すようにしています。途中で60秒sleepしているのは、mysql-dbが立ち上がるまで少し時間がかかるため立ち上がる前にアクセスしに行っていしまうとエラーを吐いてプログラムが落ちてしまうためです。

### init.sql (./volumes/mysql-db/initdb.d/init.sql)
このファイルはコンテナ内の/docker-entrypoint-initdb.d/に配置され、コンテナが起動するときに実行されます。内容は、sampleという名前のスキーマを作るだけです。

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
ビルドしたdokcerイメージを起動したあと、1分ほどbottle-app-containerとmysql-dbが立ち上がるのを待ったあと、ブラウザやcurlなどで、http://localhost:8080/ にアクセスするとHelloWorldが返ってきます。また、http://localhost:8080/show/hachan にアクセスるとパスワード表示されます。