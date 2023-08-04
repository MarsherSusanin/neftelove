# neftelove

## Функционал
- Алгоритм поиска по спутниковым снимкам нефтеразливов на:
  - Суше
  - Пресном водоеме
  - Море
- Пользовательский интерфейс веб-приложения с функциями:
  - Работа с картой страны и конкретным региона в частности
  - Ведение, дополнение и удаление обнаруженных потенциальных угроз экологии
  - Выгрузка отчетности по происшествию
  - Составление маршрута облета интересующего участка БПЛА, выгрузка и автоматическая отправка запроса в ЗЦ

## Особенности
- Дополнительные слои с важной для анализа информацией
- Алгоритм обнаружения следов нефтеразливов на суше и на воде
- Расчет уровня угрозы для экологии
- Оптимизация работы с БПЛА
- Работа с несколькими спутниками
- Поиск виновного в происшествии на воде по АИС данным

## Стек
- Микросервисная архитектура
- Алгоритм поиска по спутниковым снимкам: python, numpy, scipy, openCV
- API middleware: flask
- Бэкенд веб-прилоежния: Laravel
- Фронтенд веб-приложения: Vue.js
- Контейнеризация: Docker

## Инструкция по развертыванию приложения

```git https://github.com/MarsherSusanin/neftelove.git```

### Сервер алгоритма

```
cd ./neftelove/ComputerVision-Server/
pip3 install -r requirements.txt
```
### Сервер веб-приложения

cd neftelove/proxy
docker-compose up
cd ../api
docker-compose up
cd html
composer install
php artisan migrate
cd ../../front/app
npm run build
cd ..
docker-compose up

## Работа алгоритма

### HighLight для выделения нефтяных разливов:
```
cd "./neftelove/HighLight - function (example)"
python3 HighLight.py
```

### Алгоритм, проверенный и работающий на файлах локально:
```cd "./neftelove/Html_test/From_files"```

### Алгоритм, проверенный и работающий с подтягиванием данных с sentinel-hub:
```cd "./neftelove/Html_test/From_sentinel-hub"```

## Демо
[Доступно по ссылке](http://neftelove.pena.marketing)
[Notebook с алгоритмом обнаружения нефтреразлива у нефтепровода](https://github.com/MarsherSusanin/neftelove/blob/main/ComputerVision-Server%20(Description%20Notebook)/sentinel-2.ipynb)

## Команда
- [Радаев Иван](https://t.me/MarsherSus), project lead, старший инженер ТОИ ДВО РАН, опыт ведения разработки стартапов и IT решений
- [Любавский Глеб](https://t.me/Liubavskii_Gleb), senior designer, UI/UX, продуктовый дизайн, международные и федеральные бренды
- [Гриценко Владимир](https://t.me/Amiwriter), senior architector, back-end, мнс ТОИ ДВО РАН, 15 лет стажа разработки промышленного ПО
- [Деев Максим](https://t.me/MaksDeev), senior fullstack, преподаватель нескольких онлайн школ программирования, 7 лет боевой разработки
- [Вилков Виктор](https://t.me/moskoviy), junior front-end, молодой и амбициозный
-  [Сизов Данил](https://t.me/sizov_da), junior back-end, студент ДВФУ 
