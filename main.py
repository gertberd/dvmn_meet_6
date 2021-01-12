import os
from random import randint, sample, choice

from faker import Faker

from file_operations import render_template, read_file


def generate_male_char(fake):
    return {
        'first_name': fake.first_name_male(),
        'last_name': fake.last_name_male(),
    }


def generate_female_char(fake):
    return {
        'first_name': fake.first_name_female(),
        'last_name': fake.last_name_female(),
    }


def make_runic(word):
    letter_mapping = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }
    runic_word = ''.join([letter_mapping[letter] for letter in word])
    return runic_word


def main():
    charsheet_foldername = 'charsheets'
    charsheets_num = 10
    min_skill_value = 8
    max_skill_value = 14
    template_filepath = 'charsheet.svg'
    skills = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Кислотный взгляд',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд'
    ]
    runic_skills = [make_runic(skill) for skill in skills]
    fake = Faker("ru_RU")
    for num in range(1, charsheets_num + 1):
        skill_1, skill_2, skill_3 = sample(runic_skills, k=3)
        character = choice([generate_male_char(fake), generate_female_char(fake)])
        character.update(
            {
                'town': fake.city(),
                'job': fake.job(),
                'strength': randint(min_skill_value, max_skill_value),
                'agility': randint(min_skill_value, max_skill_value),
                'endurance': randint(min_skill_value, max_skill_value),
                'intelligence': randint(min_skill_value, max_skill_value),
                'luck': randint(min_skill_value, max_skill_value),
                'skill_1': skill_1,
                'skill_2': skill_2,
                'skill_3': skill_3
            }
        )
        charsheet_filename = os.path.join(charsheet_foldername, f'charsheet_{num}.svg')
        render_template(template_filepath, charsheet_filename, character)


if __name__ == '__main__':
    main()
