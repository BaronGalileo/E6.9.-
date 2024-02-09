"# E6.9.-" 
1.После установки проекта необходимо подключить Redis с портом 6379
![Alt text](image.png)
Запустить проект py manage.py runserver и перейти по ссылке http://127.0.0.1:8000/
В браузере, в котором будем работать, необходимо в закладке Application далее Local storage / http://127.0.0.1:8000/ ![alt text](image-1.png) в Token вести данные токена.
Токен мы получаем по пути **messanger/messanger_chat** открываем файл [text](../../Desktop/pythonProject25/messanger/messanger_chat/tokenizator.py) **tokenizator.py**  клавишамиShift+F10(запустить этот файл)create_toke(1),
где передаем  id пользователя ![alt text](image-2.png)
Копируем и вставляем токе![alt text](image-3.png).
Токен работает 2 часа, затем необходимо обновить.![alt text](image-4.png).
Пример токена для пользователя с user_profile_id=2 ![alt text](image-5.png)![alt text](image-6.png)![alt text](image-7.png)
Все необходивые библиотеки перечислены в файле [text](../../Desktop/pythonProject25/messanger/requirements.txt)