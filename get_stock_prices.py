

import requests
# import requests_cache
from lxml import html
import json
# from pprint import pprint

index = 0

request_headers = {
    'referer': "https://quote.jpx.co.jp/jpx/template/quote.cgi?F=tmp/stock_search"}

# session = requests_cache.CachedSession('stock_prices', expire_after=3600)
session = requests.Session()

index = 0
prices = []
for i in range(9999):
    print("Page:", i)
    url = "https://quote.jpx.co.jp/jpx/template/qsearch.exe?F=tmp%2Fstock_list&KEY1=&KEY5=&shijyo12=%EF%BE%8C%EF%BE%9F%EF%BE%97%EF%BD%B2%EF%BE%91&shijyo13=%EF%BD%BD%EF%BE%80%EF%BE%9D%EF%BE%80%EF%BE%9E%EF%BD%B0%EF%BE%84%EF%BE%9E&shijyo14=%EF%BD%B8%EF%BE%9E%EF%BE%9B%EF%BD%B0%EF%BD%BD&shijyo15=%EF%BE%8C%EF%BE%9F%EF%BE%97%EF%BD%B2%EF%BE%91F&shijyo16=%EF%BD%BD%EF%BE%80%EF%BE%9D%EF%BE%80%EF%BE%9E%EF%BD%B0%EF%BE%84%EF%BE%9EF&shijyo17=%EF%BD%B8%EF%BE%9E%EF%BE%9B%EF%BD%B0%EF%BD%BDF&shijyo6=E%2CFE%2CCE%2CO%2CA&shijyo9=EN&shijyo7=R&shijyo10=TPM%2CTPMF&shijyo11=IJ%2CIF%2CIE&KEY3=&kind=TTCODE&sort=%2B&MAXDISP=100&submit=%E6%A4%9C%E7%B4%A2%E9%96%8B%E5%A7%8B&KEY2=E%2CFE%2CCE%2CO%2CA%2CR%2CEN%2CTPM%2CTPMF%2CIJ%2CIF%2CIE%2C%EF%BE%8C%EF%BE%9F%EF%BE%97%EF%BD%B2%EF%BE%91%2C%EF%BD%BD%EF%BE%80%EF%BE%9D%EF%BE%80%EF%BE%9E%EF%BD%B0%EF%BE%84%EF%BE%9E%2C%EF%BD%B8%EF%BE%9E%EF%BE%9B%EF%BD%B0%EF%BD%BD%2C%EF%BE%8C%EF%BE%9F%EF%BE%97%EF%BD%B2%EF%BE%91F%2C%EF%BD%BD%EF%BE%80%EF%BE%9D%EF%BE%80%EF%BE%9E%EF%BD%B0%EF%BE%84%EF%BE%9EF%2C%EF%BD%B8%EF%BE%9E%EF%BE%9B%EF%BD%B0%EF%BD%BDF&KEY6=&REFINDEX=%2BTTCODE&GO_BEFORE=&BEFORE=" + \
        str(index)
    response = session.get(url, headers=request_headers)
    body = response.content.decode('utf-8')
    xpath = html.fromstring(body)
    table = xpath.xpath('//table[@width="545"]')[0]
    table_attrib = table.attrib
    outer_html = html.tostring(table)
    rows = table.xpath('.//tr')
    header = rows[0].xpath('.//td')
    if len(header) != 11:
        raise ValueError("Expected 11 columns, got %d" % len(header))
    # headers = [td.text_content().strip() for td in header] \r\nが邪魔、前日比がcolspan=2なので不採用にしてハードコードする
    csv_headers = ['コード', '銘柄名', '所属部', '業種', '現在値', '時刻', '前日比',
                   '前日比率', '売買高(千株)', 'ROE(%)', 'PER(倍)', 'PBR(倍)']
    for row in rows[1:]:
        price = {}
        tds = row.xpath('.//td')
        if len(tds) != 12:
            raise ValueError("Expected 12 columns, got %d" % len(tds))
        for i, td in enumerate(tds):
            price[csv_headers[i]] = td.text_content().strip()
        prices.append(price)
    index += 100
    if f"GO_NEXT=&NEXT={index}" not in body:
        break

with open("all_stock_prices.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(prices, ensure_ascii=False, indent=4))

# print(prices)
print("銘柄数:", len(prices))
