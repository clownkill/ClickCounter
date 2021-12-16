import argparse
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {
        "long_url": f"{normalize_url(url)}",
        "domain": "bit.ly"
    }
    response = requests.post(api_url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, bitlink):
    parsed_url = urlparse(bitlink)
    url_for_count = f'{parsed_url.netloc}{parsed_url.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_count} \
          /clicks/summary'
    headers = {
              'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def normalize_url(url):
    parsed_url = urlparse(url, scheme='https')
    if parsed_url.netloc:
        return f'{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}'
    return f'{parsed_url.scheme}://{parsed_url.path}'


def is_bitlink(url, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url_for_check = normalize_url(url).replace('https://', '')
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_check}',
        headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(description='Сокращает ссылку, либо выводит количество кликов по ссылке')
    parser.add_argument('url_link', help='Ссылка для обработки')
    url = parser.parse_args().url_link
    if is_bitlink(url, token):
        try:
            count = count_clicks(token, url)
            print('Количество переходов:', count)
        except requests.exceptions.HTTPError:
            print('Ошибка при получении количества переходов')
    else:
        try:
            bitlink = shorten_link(token, url)
            print('Битлинк: ', bitlink)
        except requests.exceptions.HTTPError:
            print('Вы не правильно ввели ссылку для сокращения!')


if __name__ == "__main__":
    main()
