# AiAcademy_Flask_ToDo
AiAcademyの「FlaskとMySQLでToDoアプリを実装しよう」をカスタマイズ。

## 変更点
- 使用するDBをSQLiteに変更
- DBへのアクセス方法をflask.gを使った方法に変更
- 共通テンプレート base.html を使用


## 使い方
ローカルへダウンロードしAiAcademy_Flask_ToDoディレクトリで下記のコマンドを実行
- $ export FLASK_APP=todo
- $ export FLASK_ENV=development
- $ flask init-db
- $ flask run
