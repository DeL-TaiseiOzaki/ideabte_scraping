# idebate_scraping

## 概要

`ideabte_scraping`は、Idebateサイトからデータを収集するためのWebスクレイピングツールです。このツールは、Pythonスクリプトとシェルスクリプトを使用して、Idebateサイトからデータを効率的に収集します。

## 使用方法


###  データのスクレイピング

収集したURLリストを使ってデータをスクレイピングします。

```bash
sh scraping_idebate/run_main.sh
```

このコマンドを実行すると、指定されたURLからデータが収集され、`scraping_idebate`ディレクトリ内に保存されます。

## 必要条件

このツールを使用するためには、以下のPythonパッケージが必要です。

- requests
- beautifulsoup4

必要なパッケージをインストールするには、以下のコマンドを実行してください。

```bash
pip install -r requirements.txt
```
