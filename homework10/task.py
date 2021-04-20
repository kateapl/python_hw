# Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта: <br>
# https://markets.businessinsider.com/index/components/s&p_500
#
# Для каждой компании собрать следующую информацию:
# * Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта [центробанка РФ](http://www.cbr.ru/development/sxml/))
# * Код компании (справа от названия компании на странице компании)
# * P/E компании (информация находится справа от графика на странице компании)
# * Годовой рост/падение компании в процентах (основная таблица)
# * Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)
#
# Сохранить итоговую информацию в 4 JSON файла:
# 1. Топ 10 компаний с самими дорогими акциями в рублях.
# 2. Топ 10 компаний с самым низким показателем P/E.
# 3. Топ 10 компаний, которые показали самый высокий рост за последний год
# 4. Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
# <br>Пример формата:
# ```
# [
# {
#     "code": "MMM",
#     "name": "3M CO.",
#     "price" | "P/E" | "growth" | "potential profit" : value,
# },
# ...
# ]
# ```
# For scrapping you cans use `beautifulsoup4`
# For requesting `aiohttp`
import asyncio
import datetime
import json

import aiohttp
import requests
from bs4 import BeautifulSoup


async def fetch_response(url) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def find_PE(bs: BeautifulSoup) -> str:
    divs = bs.findAll("div", class_="snapshot__data-item")
    tag = "P/E Ratio"
    for div in divs:
        if str(div).find(tag):
            return (
                str(div)
                .replace('<div class="snapshot__data-item">\r\n\t\t\t\t', "")
                .split("\r")[0]
            )


def get_latest_price(soup, dollar_cource) -> list:
    rows = soup.findAll("tr")
    price_list = []
    for row in rows:
        elem = (
            str(row.find("td", class_="text-right"))
            .replace('<td class="text-right">', "")
            .split("<br/>")[0]
        )
        if elem != "None":
            price_list.append(
                float(elem.replace("\r\n", "").replace(",", "")) * dollar_cource
            )
    return price_list


def get_growth(soup) -> list:
    rows = soup.findAll("span")
    growth = []
    count = 0
    for row in rows:
        count += 1
        if count == 10:
            if row["class"] == ["colorGreen"]:
                growth.append(
                    str(row)
                    .split("</span>")[0]
                    .replace('<span class="colorGreen">', "")
                )
            else:
                growth.append(
                    str(row)
                    .split("</span>")[0]
                    .replace('<span class="colorRed">', "")
                    .split("</span>")[0]
                )
            count = 0
    return growth


def count_stonks(bs: BeautifulSoup) -> float:
    div = bs.findAll("div", class_="snapshot__highlow")
    res = 0

    if len(div) > 1:
        hl = str(div[1]).split("div")
        low = (
            str(hl[2])
            .replace(
                ' class="snapshot__data-item snapshot__data-item--small">\r\n\t\t\t\t\t\t',
                "",
            )
            .split("\r")[0]
        )
        high = (
            str(hl[6])
            .replace(
                ' class="snapshot__data-item snapshot__data-item--small snapshot__data-item--right">\r\n\t\t\t\t\t\t',
                "",
            )
            .split("\r")[0]
        )
        result = float(high.replace(",", "")) - float(low.replace(",", ""))
        res = result * 100 / float(high.replace(",", ""))
    return res


async def main() -> None:
    stocks = "https://markets.businessinsider.com/index/components/s&p_500"
    page = requests.get(stocks)

    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    dollar = f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={yesterday.strftime('%d/%m/%Y')}&date_req2={now.strftime('%d/%m/%Y')}&VAL_NM_RQ=R01235"
    dollar_page = requests.get(dollar)
    cource = dollar_page.text.split("<Value>")[1]
    dollar_cource = float(cource.split("</Value>")[0].replace(",", "."))
    print(dollar_cource)

    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find("table", class_="table table-small")
    companies = table.findAll("a")
    references = []
    company_name = []
    growth = get_growth(table)
    latest_prices = get_latest_price(soup, dollar_cource)

    ref = "https://markets.businessinsider.com"
    for company in companies:
        references.append(ref + str(company["href"]))
        company_name.append(company["title"])

    tasks = [asyncio.create_task(fetch_response(url)) for url in references]
    await asyncio.gather(*tasks)
    codes = []
    PE = []
    stonks = []
    for task in tasks:
        tasksoup = BeautifulSoup(task.result(), "html.parser")
        PE.append(find_PE(tasksoup))
        codes.append(
            str(tasksoup.find("title"))
            .split(sep=" ", maxsplit=1)[0]
            .replace("<title>", "")
        )
        stonks.append(count_stonks(tasksoup))

    company_list = []
    for i, company in enumerate(company_name):
        company_struct = {}
        company_struct["name"] = company
        company_struct["code"] = codes[i]
        company_struct["P/E"] = PE[i]
        company_struct["growth"] = growth[i]
        company_struct["profit"] = stonks[i]
        company_struct["price"] = latest_prices[i]
        company_list.append(company_struct)
    sort_list = sorted(company_list, key=lambda elem: elem["price"], reverse=True)
    with open("high_price.json", "w") as file:
        json.dump(sort_list[:10], file)
    sort_list = sorted(
        company_list, key=lambda elem: float(elem["P/E"].replace(",", ""))
    )
    with open("low_PE.json", "w") as file:
        json.dump(sort_list[:10], file)
    sort_list = sorted(
        company_list,
        key=lambda elem: float(elem["growth"].replace("%", "")),
        reverse=True,
    )
    with open("high_growth.json", "w") as file:
        json.dump(sort_list[:10], file)
    sort_list = sorted(company_list, key=lambda elem: elem["profit"], reverse=True)
    with open("high_profit.json", "w") as file:
        json.dump(sort_list[:10], file)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
