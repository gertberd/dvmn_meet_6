# Утилита для генерации карточек персонажей настольной игры Метро&Монстры

Шаблон: `charsheet.svg`
Для генерации карточек используются:
- библиотека `faker`
- `random.randint()` и `random.sample()`

## Как установить

Создать в директории проекта папку `charsheets`, в неё будут сохраянться сгенерированные карточки.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Использование
```
python main.py
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
