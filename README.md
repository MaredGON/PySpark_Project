
## Установка

### Требования

- Python 3.7+
- PySpark 3.0+
- Java 8+
- Hadoop (winutils.exe для Windows)

### Установка зависимостей

1. Установите зависимости из файла `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Скачайте `winutils.exe` для вашей версии Hadoop и установите переменные среды (только для Windows):

    - Создайте папку, например `C:\hadoop`.
    - Скачайте `winutils.exe` и поместите его в папку `C:\hadoop\bin`.
    - Установите переменную среды `HADOOP_HOME` на `C:\hadoop`.
    - Добавьте `C:\hadoop\bin` в системную переменную `PATH`.

## Использование

1. Убедитесь, что файлы данных (`products.csv`, `categories.csv`, `product_category_rel.csv`) находятся в папке `data` в корне проекта.
2. Запустите основной скрипт:

    ```bash
    python src/main.py
    ```

## Структура файлов

### `data/`

- **products.csv**: Содержит информацию о продуктах.
- **categories.csv**: Содержит информацию о категориях.
- **product_category_rel.csv**: Содержит связи между продуктами и категориями.

### `src/`

- **`__init__.py`**: Указывает, что каталог является пакетом Python.
- **`main.py`**: Основной скрипт для запуска приложения.
- **`config.py`**: Конфигурационный файл для настройки параметров.
- **`data_loader.py`**: Модуль для загрузки данных.
- **`process.py`**: Модуль для обработки данных и выполнения основной логики.

### `notebooks/`

- **exploration.ipynb**: Пример ноутбука для исследования данных.

### `tests/`

- **`__init__.py`**: Указывает, что каталог является пакетом Python.
- **`test_data_loader.py`**: Тесты для модуля загрузки данных.
- **`test_process.py`**: Тесты для модуля обработки данных.

## Запуск тестов

Для запуска тестов используйте следующую команду:

```bash
python -m unittest discover -s tests
