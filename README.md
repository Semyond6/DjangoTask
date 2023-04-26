# DjangoTask

В settings.py прописать ключ к Django: SECRET_KEY=''.

Для работы в docker использовался docker-compose. Для сборки образа необходимо наличие запущенной программы docker на машине. 
Чтобы собрать образ в терминале неообходимо ввести команду:

        "docker-compose up -d --build"
        
Дождаться сборки и запуска контейнеров.
Выполнить команду в терминале: 

        "docker-compose exec web /usr/local/bin/python manage.py migrate"

Для локального запуска программы в settings.py заменить HOST на:
    "DATABASES = {
    'default': {
        'HOST': 'localhost',
    }
}"
Иметь на машине mysql с портом: "3306"
