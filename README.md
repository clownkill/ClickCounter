# Сокращение ссылок с помощью Bitly

Скрипт для создания коротких ссылок или получения информации о кликах по коротким ссылкам.

### Как установить
Python3 должен быть уже установлен. Затем используйте 'pip' (или 'pip3', если есть конфликт с Python2) для 
установки зависимостей.
```
pip install -r requirements.txt
```

### Объявление переменных окружения
Перед запуском скрипта в одном каталоге с файлом `main.py` необходимо создать файл для хранения переменных окружения 
с именем .env со следующим содержимым:
```
BITLY_TOKEN=[TOKEN]
```
В переменной `BITLY_TOKEN` хранится API-токен полученный на сервисе [bitly.com](https://bitly.com/).

### Инструкция
Для получения справки используйте python main.py -h или python main.py --help

### Пример использования

```
python main.py https://dvmn.org/modules
---
Битлинк:  https://bit.ly/3pRJBQc
```

```
python main.py https://bit.ly/3pRJBQc
---
Количество переходов: 1
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
