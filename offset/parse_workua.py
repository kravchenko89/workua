import requests

from bs4 import BeautifulSoup
from user_agent import generate_user_agent

from table_db import save_db, create_db
from utils import save_info, random_sleep, json_save
from path import HOST, ROOT_PATH


def main():
    page = 0

    while True:
        page += 1

        payload = {
            'ss': 1,
            'page': 1,
        }
        user_agent = generate_user_agent()
        headers = {
            'User-Agent': user_agent,
        }

        print(f'PAGE: {page}')
        response = requests.get(HOST + ROOT_PATH, params=payload, headers=headers)
        response.raise_for_status()
        random_sleep()

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        cards = soup.find_all('div', class_='job-link')

        json_db = []
        result = []
        if not cards:
            break

        for card in cards:
            tag_a = card.find('h2').find('a')
            vacancy = tag_a.text
            href = tag_a['href']
            path = requests.get(HOST + href, headers=headers)
            text = path.text
            work_path = HOST + href
            soup = BeautifulSoup(text, 'html.parser')
            company = soup.find(class_='glyphicon-company').findNext('a').find('b').text
            address = soup.find(class_='glyphicon-map-marker').findParent('p').text
            description = soup.find(id='job-description').text

            try:

                wage = soup.find(class_='glyphicon-hryvnia').findNext('b').text
            except AttributeError:

                wage = 'Информация не предоставлена'

            result.append(
                [
                    f'Ссылка: {work_path},\n'
                    f'Вакансия: {vacancy},\n'
                    f'Зарплата: {wage},\n'
                    f'Компания: {company},\n'
                    f'Город: {address},\n'
                    f'Описание: {description}\n'
                ]
            )
            save_db(work_path, vacancy, wage, company, address, description)
            # create_db(work_path, vacancy, wage, company, address, description)

            json_db.append({'job vacancy':
                {
                    'Ссылка': work_path,
                    'Вакансия': vacancy,
                    'Зарплата': wage,
                    'Компания': company,
                    'Город': address.replace('\n', ''),
                    'Описание': description.replace('\n', ''),
                }
            })
            json_save(json_db)

        save_info(result)


if __name__ == "__main__":
    main()
