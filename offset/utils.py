import json
import random

from time import sleep


def save_info(array: list) -> None:
    with open('workua.txt', 'a') as file:
        for line in array:
            file.write(' | '.join(line) + '\n'*3)


def random_sleep():
    sleep(random.randint(5, 12))


def json_save(json_db):
    with open('data.json', mode='w', encoding='utf-8') as db:
        json.dump(json_db, db, ensure_ascii=False, indent=2)
