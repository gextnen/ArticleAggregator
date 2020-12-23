# ArticleAggregator
Restful приложение, которое является агрегатором лучший статей на habr.com

# Вам понадобиться
Erlang/OTP, RabbitMQ  

Необходимо скачать Erlang: https://www.erlang.org/downloads

Если у вас Windows:

Необходимо  установить RabbitMQ в папку: ..\erl-23.2\lib : https://www.rabbitmq.com/download.html

Если у вас другая ОС, инструкцию по установке можете посмотреть по вышеуказанным ссылкам.

# Настройка
Запустите RabbitMQ Service start.

Запустите проект. После запуска, необходимо в терминале программы в трех разных сессиях ввести следующие команды:
1. python manage.py runserver 
2. celery -A ArticleAggregator worker  -l info
3. celery -A ArticleAggregator beat  -l info

Также вам понадобиться некоторые библиотеки:
1. pip install djangorestframework
2. pip install bs4
3. pip install requests
4. pip install celery
5. pip install Django

Убедитесь, что вы находитесь в нужной дирректории, а также проверьте наличие необходимых библиотек.

# Проверка работы
После запуска сервера перейдите по адресу: http://127.0.0.1:8000/articles/

Вы можете просматривать отдельно взятый ресурс, если в конце данного адреса укажите число номера ресурса. 
