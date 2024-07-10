import requests
from bs4 import BeautifulSoup

url = "https://idebate.net/this-house-would-make-all-museums-free-of-charge~b641/"

# ウェブページを取得
response = requests.get(url)
response.raise_for_status()  # エラーチェック

# HTMLを解析
soup = BeautifulSoup(response.content, 'html.parser')

# Points Forのdiv要素を取得
points_for_section = soup.find('div', class_='points-vote points-vote--for')

# ポイントを含むアコーディオン要素を取得
accordion_items = points_for_section.find_next_sibling('div', class_='accordion').find_all('div', class_='accordion__item')

# 各ポイントのテキストを抽出
points = []
for item in accordion_items:
    point_subtitle = item.find('h4', class_='accordion__subtitle').get_text().strip()
    point_body = item.find('div', class_='accordion__body').find('p').get_text().strip()
    points.append(f"**{point_subtitle}**\n{point_body}")

# 抽出したポイントを出力
for point in points:
    print(point)
    print("-" * 20)  # 区切り線
