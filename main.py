import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

BASE_URL = "https://api-ssl.bitly.com/v4/"


def get_short_link(user_input, headers):
    """ Сокращение длинных ссылок. Возвращает битлинк """
    response = requests.post(url=f"{BASE_URL}bitlinks",
                             headers=headers,
                             json=user_input)
    response.raise_for_status()
    return response.json()['link']


def get_count_clicks(bitlink, headers):
    """ Подсчёт количества переходов по битлинку """
    link = urlparse(bitlink)
    url = f"{BASE_URL}bitlinks/{link.netloc}{link.path}/clicks/summary"
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    return response.json().get("total_clicks")


def is_bitlink(user_input, headers):
    """ Проверка введённых данных на bitlink """
    link = urlparse(user_input)
    url = f"{BASE_URL}bitlinks/{link.netloc}{link.path}"
    response = requests.get(url=url, headers=headers)
    return response.ok


if __name__ == "__main__":
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    bitly_api_token = os.environ.get("BITLY_API_TOKEN")
    headers = {"Authorization": f"Bearer {bitly_api_token}"}

    parser = argparse.ArgumentParser(description="Сокращение длинных ссылок через сервис Bitly")
    parser.add_argument('link', help='ссылка формата https://mozilla.org')
    args = parser.parse_args()

    try:
        if is_bitlink(args.link, headers):
            print("Количество переходов по битлинку --", get_count_clicks(args.link, headers))
        else:
            print("Битлинк --", get_short_link({"long_url": args.link}, headers))
    except requests.exceptions.HTTPError as error:
        print(f"\nЧто то пошло не так. Проверьте корректность входных данных:\n\n{error}")
