# Homework, задача “минимум”


1. Реализовать TCP-server (или UDP-server)

– Принимает данные от клиента

– Сохраняет в файл


2. Реализовать TCP-client (или UDP-client):

– Раз в минуту отправляет данные (эмуляция датчика - random) на сервер

– Формат данных: текущее время, значение


# Homework, задача “хорошо”

1. Реализовать TCP-server (или UDP-server)

– Принимает данные от клиента

– Сохраняет в файл


2. Реализовать TCP-client (или UDP-client):

– Раз в минуту отправляет данные на сервер, данные на выбор:

 • Данные CPU, температуры

 • Количество секунд использования мышки

 • Количество нажатий hot keys (ctrl+c, code inspect, ...)

 • Свой вариант

 – Формат данных: текущее время, название метрики, значение


# Homework, задача “максимум”

1. Реализовать TCP-server (или UDP-server)

– Принимает данные от клиента

– Сохраняет в файл


2. Реализовать класс для сборки данных,
– Данные на выбор из пункта (“хорошо”) или свой вариант

– Реализовать методы для метрики:

• start_collect() – начинает сборку метрики

• get_current_state() – получить название метрики, значение

• cleanup() – сброс значения

• stop_collect() – остановка сборщика

– Использование thread для запуска сборщика метрики


3. Реализовать TCP-client (или UDP-client):

– Отправка данных на сервер раз в минуту, с результатами работы сборщика

– Формат данных: текущее время, название метрики, значение
