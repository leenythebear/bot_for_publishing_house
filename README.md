# Telegram и VK бот для технической поддержки на основе DialogFlow

## Как установить

1. Скачайте код
2. Для работы скрипта нужен Python версии не ниже 3.7
3. Установите зависимости, указанные в файле ``requirements.txt`` командой:

   ```pip install -r requirements.txt```
5. Создайте бота для работы в Telegram и получите его токен
6. Создайте  группу для работы в VK и получите токен группы
7. Узнайте chat id для получения сообщений-логов
8. Создайте проект и агента в Google Cloud
9. В Google Cloud разделe [IAM&Admin>Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) получите файл в формате json с ключами доступа и разместите его в корне проекта
8. Создайте в корне проекта файл ``.env`` и укажите в нем все вышеуказанные данные, по образцу:

```
TG_TOKEN=токен, полученный в п.5
VK_TOKEN=токен, полученный в п.6
TG_CHAT_ID=ID чата из п. 7 
PROJECT_ID=ID проекта, созданного в п.8
GOOGLE_APPLICATION_CREDENTIALS=путь до файла, полученного в п.9
```

## Как запустить

- Скрипт ``create_intent.py`` осуществляет создание Intents и заполняет их тренировочными фразами из файла ``phrases.json`` в DialogFlow (достаточно запустить его один раз)

Запускается командой:

   ```python3 create_intent.py```

- Скрипт ``google_api.py`` является вспомогательным скриптом, отдельный запуск не требуется

- Скрипты ``tg_bot.py`` и ``vk_bot.py`` запускают ботов в Telegram и VK

Запускаются командой:

```python3 tg_bot.py```

и 

```python3 tg_bot.py```


## Результат работы 

При запуске ботов вы получите сообщения:

```
Telegram  бот запущен
VK бот запущен
```
Примеры работы ботов:

- Vk-бот:
![Vk-бот](https://dvmn.org/filer/canonical/1569214089/322/)
___
- Telegram-бот:
![Telegram-бот](https://dvmn.org/filer/canonical/1569214094/323/)

Попробовать ботов в действии можно по следующим ссылкам:

[Telegram-бот](https://t.me/Leeny_the_bear_bot), [Vk-бот](https://vk.com/im?sel=-215364307)

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Автор проекта

Елена Иванова [Leeny_the_bear](https://github.com/leenythebear)


