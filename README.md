### Обучаемые Боты для службы поддержки  в Telegram  и VK с использованием нейросети  

#### Перед первым запуском необходимо выполнить ряд обязательных условий :

<b>1) Зарегистрируетесь на Heroku и создайте приложение (app) </b>

https://id.heroku.com/login


Привяжите GitHub и залейте код.
Это  можно осуществить на вкладке Deploy. После подключения выполните Deploy Branch.

В разделе Settings приложения необходимо создать переменные с названиями:
CHAT_ID_FOR_LOGBOT,GOOGLE_APLICATION_CREDENTIALS,GOOGLE_CREDENTIALS,PROJECT_ID,TELEGRAM_BOT_TOKEN,TELEGRAM_LOGBOT_TOKEN,VK_TOKEN .Значения для них получим на следующих шагах. 

<b>2) Зарегистрировать двух ботов Telegram  и получить их API ключи (бот для диалогов и бот для сервисных сообщений) </b>

Написать Отцу ботов
/start
/newbot

Передать значение токенов TELEGRAM_BOT_TOKEN и TELEGRAM_LOGBOT_TOKEN соответсвенно, в разделе Settings приложения на Heroku

Получить свой chat_id, возможно написав в Telegram специальному боту: @userinfobot после необходимо
передать значение переменной CHAT_ID_FOR_LOGBOT приложенния в разделе Settings приложения на Heroku


<b>3) Создайте группу VK</b>

Создать группу ВК,перейти в настройки группы ,в меню "Работа с API " создать ключ с правами  доступа: управление сообществом, сообщения сообщества
передать значение ключа переменной VK_TOKEN





<b>4) Создайте проект в DialogFlow  и обучите ботов</b>

Создать проект в DialogFlow

https://dialogflow.com/docs/getting-started/first-agent

в настройках проекта в разделе GOOGLE PROJECT скопируйте значение Project ID и передайте его переменной PROJECT_ID


Получите Dev Token :

https://dialogflow.com/docs/reference/agent#obtaining_access_tokens

содержимое файла -токена google-credentials.json  скопируйте переменной GOOGLE_CREDENTIALS

в файле questions.json находятся тестовые фразы для обучения проекта в DialogFlow

Запустите скрипт add_intense.py




#### Установка  и запуск на локальной машине
Запуск бота также возможен  на локальной машине ,для этого в каталоге с модулем необходимо создать файл .env  в нем объявить переменные CHAT_ID_FOR_LOGBOT,GOOGLE_APLICATION_CREDENTIALS,GOOGLE_CREDENTIALS,PROJECT_ID,TELEGRAM_BOT_TOKEN,TELEGRAM_LOGBOT_TOKEN,VK_TOKEN и передать им  значения полученные в предыдущих шагах.файл токен переименовать на google-credentials.json и сохранить в каталоге с программой

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 

```
pip3 install -r requirements.txt

```


```
$python3 vk_bot.py
$python3 telegram_bot.py

```




#### Запуск
После получения Токенов и  CHAT_ID  необходжимо перейти в раздел Resources и передвинув ползунки ботов вправо (через редактирование) разрешить запуск приложений.




### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

2019 Dark_Dmake