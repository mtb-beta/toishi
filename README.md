# toishi

日本語テキストのフォーマッター。
名称は、日本の伝統的な刃物の研ぎに使用される砥石(toishi)をモチーフにしています。

## 開発背景

- 日本語テキストをテキストエディタで修正しつつ、リポジトリでバージョン管理することがありました。
- バージョン管理にあたり、行ごとに改行が入っている方が履歴が追跡しやすくなります。
- 日本語を書くのに夢中になり、不必要な改行が入ることもあります。しかし、それを手作業でチェックするのは煩雑です。
- コードフォーマッターのように自動で修正してほしい、という想いから作りました。

## 機能(開発中)

現在、開発中です。以下は追加予定の機能です。

- [x]  「。」の後に改行を自動で入れる。
- [ ] 空行は連続しない。1行のみ。 複数行ある場合は、1行にする。
- [ ] ファイルの先頭の空行、最後の空行は削除する。
- [ ] チェックのみで修正を入れないオプション（CI用）
- [ ] ディレクトリを指定し、一括で処理する機能
