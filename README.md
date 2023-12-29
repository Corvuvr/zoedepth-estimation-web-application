# zoedepth-estimation-web-application
This web-application will let you get depth map from single image.

![alt text](https://github.com/Corvuvr/zoedepth-estimation-web-application/blob/main/src/uploads/hat.png?raw=true)

## Usage
1. Launch Docker.
2. Run `run.bat`.
3. After installation completes, open browser and paste `localhost:4000/` in address bar (don't miss slash).
4. Upload image you want (_english filenames only_).
5. Wait (photo processing may take about one minute or more).
6. Get the result.
7. You can complete the work using the keyboard shortcut `ctrl+c` in the terminal.

P.s.: to restart, run `run.bat` again.
## REST API methods
1. POST `http://localhost:4000/`
   - Uploads an inage to the server for depth estimation.
   - Image is transferred as binary in the body of the request.
   - Postman collection link (import collection via 'Import' button): `https://api.postman.com/collections/30844064-f970a9df-6db6-4196-be21-8cf07a4236d5?access_key=PMAT-01HJVB6RHZKPXYGWVNARNWDRXK`.
# На русском
## Использование 
1. Запустить Docker.
2. Запустить `run.bat`.
3. После установки, открыть браузер и вбить в адресную строку: `localhost:4000/` (не забудьте про слэш).
4. Загрузите желаемое изображение (_только английские названия файлов_).
5. Подождать (обработка фото может занять около одной минуты или больше).
6. Получить результат.
7. Завершить работу можно с помощью сочетания клавиш `ctrl+c` в терминале.

P.s.: для повторного запуска ещё раз запустите `run.bat`.
## Методы REST API 
1. POST `http://localhost:4000/`
   - Загружает изображение на сервер для обработки.
   - Изображение передаётся в бинарном виде в теле запроса.
   - Ссылка на коллекцию Postman (добавить коллекцию с помощью кнопки `Import`): `https://api.postman.com/collections/30844064-f970a9df-6db6-4196-be21-8cf07a4236d5?access_key=PMAT-01HJVB6RHZKPXYGWVNARNWDRXK`.
