import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup

data = []


async def get_page_data(session, page):
    """
    The function collects data from a web page.

    """
    # url - сайта по продаже авто (renault - talisman)
    url = f"https://cars.av.by/filter?brands[0][brand]=1039&brands[0][model]=5346&page={page}"

    async with session.get(url=url) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, 'lxml')

        # Получаем все объявления со страницы и помещаем их в список
        cars = soup.find_all('div', class_='listing-item')

        for car in cars:
            link = 'https://cars.av.by' + car.find('a', class_='listing-item__link').get('href')

            # берем цену в byn
            price_byn = car.find('div', class_='listing-item__price').text.encode('ascii', errors='ignore')\
                .decode('UTF-8').replace('.', '')

            # берем цену в usd
            price_usd = car.find('div', class_='listing-item__priceusd').text.encode('ascii', errors='ignore')\
                .decode('UTF-8').replace('$', '')

            # берем параметры
            info = car.find('div', class_='listing-item__params').text.replace('\xa0', '')
            new_info = info.replace('\u2009', '')

            # Формируем список из данных по авто и добавляем его в список data
            data.append([price_usd, price_byn, new_info, link])
        print(data)


async def gather_data():
    """The function creates a list of tasks."""

    async with aiohttp.ClientSession() as session:
        # С помощью контекстного менеджера создаем клиент-сессию для повторного использования соединения
        tasks = []
        # Перебераем циклом страницы
        for page in range(1, 7):
            # Создаем таски с помощью asyncio.create_task
            task = asyncio.create_task(get_page_data(session, page))
            # Добавляем таски в список tasks
            tasks.append(task)

        await asyncio.gather(*tasks)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_data())
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


if __name__ == "__main__":
    main()
