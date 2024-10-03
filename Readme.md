## アプリの概要

- Producer
  - RDS for postgresのDBに開始ログを設定(uuid生成、プロセスID生成して登録)
  - SQSにキューを登録
  - RDS for postgresのDBに終了ログを設定(uuid生成、開始時のプロセスIDと同じIDで登録)
- Consumer
  - RDS for postgresのDBに開始ログを設定(uuid生成、SQSから受け取ったプロセスIDを登録)
  - SQSから受け取ったメッセージを参照してDBに登録(ログ用とは別のテーブル)
  - RDS for postgresのDBに終了ログを設定(uuid生成、SQSから受け取ったプロセスIDと同じIDで登録)

## DB
- ログ用 : sample_log
- メッセージ用 : sample_message