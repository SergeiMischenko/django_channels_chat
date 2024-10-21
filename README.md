<h1 align="center">Django_Channels_Chat</h1>

В рамках данного проекта было создано простое CRUD-приложение на Django с использованием Django-channels и Websocket. Приложение это чат, который работает через Группы(Вход/Выход из группы) далее подключаемся к группе и входим в чат между участниками, Стоило добавить ещё Redis для хранения сообщений и слоёв, сейчас используется обычный бекенд на sqlite.

Цель проекта — изучить базовые возможности работы Django-channels и Websocket.
___

<h2 align="center">Установка</h2>

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/SergeiMischenko/django_channels_chat.git
    ```

2. **Перейдите в папку проекта:**
    ```bash
    cd django_channels_chat
    ```

3. **Установите виртуальное окружение и активируйте его:**
    ```bash
    python -m venv env
    source env/bin/activate   # Для Linux и macOS
    env\Scripts\activate      # Для Windows
    ```

4. **Установите необходимые зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Откройте файл .env и заполнить его своими данными**
    ```env
    SECRET_KEY = 'your-secret-key'
    ```

6. **Выполните миграции базы данных:**
    ```bash
    python manage.py migrate
    ```

7. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    ```

8. **Доступ к тестам:**
   
    После завершения всех вышеуказанных шагов, приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
