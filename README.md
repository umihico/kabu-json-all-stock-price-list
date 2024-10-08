# 【株JSON】全銘柄終値JSON取得プログラム

日本株の全銘柄の終値一覧を毎日取得してJSONにするプログラムを公開しています。フォークして自由に利用してください。

[![badge](https://github.com/umihico/kabu-json-all-stock-price-list/actions/workflows/auto-update.yml/badge.svg)](https://github.com/umihico/kabu-json-all-stock-price-list/actions/workflows/auto-update.yml)

## 注意事項

[株価検索 | 日本取引所グループ](https://quote.jpx.co.jp/jpx/template/quote.cgi?F=tmp/stock_search)には以下の通り注意事項がありますので、取得した情報の利用にはご注意ください。

> 「株価検索サイト」に掲載される内容の著作権は、JPXおよびその情報提供元にあります。情報は、利用者ご自身のためにのみ利用するものとし、第三者または情報を閲覧している端末機以外の媒体への提供目的で加工、再利用および再配信することを固く禁じます。また、情報の蓄積、編集および加工等を禁じます。

## 使い方

1. このリポジトリをフォークします。
2. フォークしたリポジトリをローカルにクローンします。
3. `get_stock_prices.py`を実行します。以下のファイルが生成されます。
    - `stock_prices.json`: 全銘柄の終値一覧
4. または、GitHub Actionsを使って定期的に実行します。同じくCI上で`stock_prices.json`が生成されます。

## 記事

- [日本株の全銘柄一覧をJSON形式で毎日更新・配信する「株JSON」をリリース](https://umihi.co/blog/20240908-kabu-json-release)
- [日本株の全銘柄の終値一覧を毎日取得してJSONにするプログラムを公開しました](https://umihi.co/blog/20240909-kabu-json-all-close-prices-release)
