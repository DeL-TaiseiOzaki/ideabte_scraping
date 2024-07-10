# ideabte_scraping

## 概要

`ideabte_scraping`は、Idebateサイトからデータを収集するためのWebスクレイピングツールです。このツールは、Pythonスクリプトとシェルスクリプトを使用して、Idebateサイトからデータを効率的に収集します。

## 使用方法

### 1. URLリストの取得

まず、Idebateサイトからデータを収集するためのURLリストを取得します。

```bash
python Get_URL_list/get_url_list.py
```

このコマンドを実行すると、`Get_URL_list/URL_json_output`ディレクトリに`debate_urls.json`というファイルが生成されます。

### 2. データのスクレイピング

次に、収集したURLリストを使ってデータをスクレイピングします。

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
