import requests
from bs4 import BeautifulSoup
from time import sleep


def page_formation(url):
    """
    The function takes an url.
    Returns the rendered html page.

    """
    response = requests.get(url)
    # формируем обработанную html страницу:
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def get_url():
    """
    The function accepts a rendered html page.
    Links to ads is returned.

    """
    for count in range(1, 6):
        # url - адрес сайта присваиваем переменной
        url = f"https://cars.av.by/filter?brands[0][brand]=1039&brands[0][model]=5346&page={count}"
        soup = page_formation(url)
        # дергаем все объявления со страницы и помещаем их в список
        data = soup.find_all("div", class_="listing-item")

        for i in data:
            # берем из списка ссылки на объявления
            card_url = "https://cars.av.by" + i.find("a").get("href")
            yield card_url


def array_():
    """
    The function takes a link to a declaration.
    Returns url, price in dollars, price in rubles and description.

    """
    for card_url in get_url():
        sleep(2)
        soup = page_formation(card_url)
        data = soup.find("div", class_="card")
        # берем цену в usd
        price_usd = data.find("div", class_="card__price-secondary").text.replace("\n", "")
        # берем цену в byn
        price_byn = data.find("div", class_="card__price-primary").text.replace("\n", "")
        # берем параметры
        text = data.find("div", class_="card__params").text.replace("\n", "")
        yield card_url, price_usd, price_byn, text


if __name__ == "__main__":
    print("Вы запустили этот файл напрямую. Его нужно импортировать!")

