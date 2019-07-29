## English
### Install dependencies
`pip install -r requirements.txt`

### How to run
`python web-app.py`

### How it works
App starts web server (Flask) and web cam<br>
When you press button `Json` webcam takes a picture, detects faces on picture and forms json with params (start x point, start y point, width, height) like this <br>
`[{"x": 50,"y": 48,"width": 104,"height": 126},{"x": 200,"y": 75,"width": 216,"height": 231}]` 

When you press button `Image` webcam takes a picture, detects faces on picture and transfer image to server<br>
After all, results are displayed on the web page.

Image showing is hardcoded (save cv2 image to file and read its path for showing html img)

## Русский
### Установка зависимостей проекта
`pip install -r requirements.txt`

### Как запускать
`python web-app.py`

### Как работает приложение
Приложение запускает веб сервер (Flask) и веб камеру<br>
При нажатии кнопки `Json` делается снимок с веб камеры, обнаруживает лица на снимке и формирует json с параметрами (начальная координата по горизонтали, начальная координата по вертикали, ширина, высота). Пример:<br>
`[{"x": 50,"y": 48,"width": 104,"height": 126},{"x": 200,"y": 75,"width": 216,"height": 231}]` 

При нажатии кнопки `Image` делается снимок с веб камеры, обнаруживает лица на снимке и передает изображение на сервер<br>
После всего этого результаты отображаются на веб страницу

Показ изображения закостылен (сохраняет полученное с веб камеры изображение как файл и для показа как html изображение считывается путь до файла)