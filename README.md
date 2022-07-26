#Шаги установки: 

####1 - Подключить venv командой: 
`python -m venv venv`

####2 - Активировать его, командой:
- `cd venv`
- `cd Scripts`
- `activate`

####3 - В Консоле прейти в папку рут, командой:
`cd Yellow-News-Site--master`

####4 - Установить библиотеки командой:
`pip install -r requirements.txt`

####5 - Выполнить мигрцию, командой:
`python manage.py migrate`

####6 - Запустить сервер, командой:
`python manage.py runserver`