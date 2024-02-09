# 環境構築.etc
ここでは、dockerを始めるにあっての環境構築についてなどをまとめています。

## docker、docker-composeのインストール
dockerの環境構築に関しては、以下のサイトがとてもわかり易くまとめてあります。<br>
<https://kinsta.com/jp/blog/install-docker-ubuntu/><br>
dockerとdocker-composeのインストールと、dockerのコマンドはOSユーザーグループのdockerグループに所属しないと実行できないので、dockerグループへのユーザー追加をしてください。

## dockerの基本的なつかいかた
dockerはコンテナのイメージを使用してコンテナを実行します。
### dockerイメージのダウンロード
dockerイメージをダウンロードする場合は以下のコマンドを使用します。
```
docker image pull <image>:<version>
```
でイメージをpullすることができます。versionにlatestを使用することで最新版をダウンロードすることが可能です。

### コンテナの実行
コンテナの実行は以下のコマンドを使用します。
```
docker run <options> <image> <command> <arg>
```
以下は使用例です。
```
docker run -it -d --rm -p 8080:80 --name ubuntu-container ubuntu:20.04
```
これは、ubuntuのイメージを元にubuntu-containerという名前のコンテナを実行しています。以下オプションについての簡単な解説です。
- -dオプションにより、バックグラウンドでの実行をさせています。
- -pオプションにより、ホスト側の8080番ポートとコンテナ内の80番ポートをつないでいます。これにより、localhost:8080にアクセスすると、コンテナ内80番ポートに開いたサービスにアクセスすることができます。
- -itオプションはざっくりとした話、コンテナとインタラクティブなシェルを開くものです。使用例に、-dオプションをつけないで実行すると、コンテナ起動後、コマンドを実行したシェルとコンテナのシェルが接続されます。基本的にdockerはコンテナ内のプロセスがすべて終了するとコンテナ自体が終了するようになっているので、シェルを開いておくことでコンテナを勝手に終了させないようにしてあったりもします。
- --rm オプションは、コンテナを停止するとコンテナを自動削除するようにしています。このオプションをつけない場合コンテナを削除する場合はコンテナを停止した後、削除のコマンドを打つ必要があります。

### コンテナの確認
立ち上げたコンテナは以下のコマンドで確認できます。ここで、コンテナのIDや、コンテナの名前など確認できます。
また、停止中のコンテナも含めて確認する場合は -aオプションをつけます。
```
docker ps
docker ps -a
```

### コンテナのログの確認
コンテナのログを確認する際は以下のコマンドで確認できます。
```
docker logs <container id> OR <container name>
```

### シェルの起動
バックグラウンド実行しているコンテナのシェルを起動する際は以下のコマンドでシェルに入れます。
```
docker exec -it <container id> OR <container name> sh
```

### コンテナの停止
立ち上げたコンテナを停止するには、コンテナの確認をしたときに表示されるコンテナのIDを使って停止できます。
```
docker stop <container id> OR <container name>
```
この指定する際、IDが手打ちするにはながいのもありtabで補完してもいいですが、コンテナが一意に指定できるところまでコンテナIDを入力すればコマンドが実行できます。コンテナIDがb93dd33fd07cの場合、コマンドは以下でも動きます。
```
docker stop b
```

### コンテナの削除
コンテナを削除するためには以下のコマンドになります。
```
docker rm <container id> OR <container name>
```
idに関しては、コンテナの停止のときと同様です。

###

## 参考記事
<https://kinsta.com/jp/blog/install-docker-ubuntu/#ubuntudocker>
<https://www-creators.com/archives/241>
<https://qiita.com/DQNEO/items/da5df074c48b012152ee>
<https://qiita.com/zembutsu/items/24558f9d0d254e33088f>