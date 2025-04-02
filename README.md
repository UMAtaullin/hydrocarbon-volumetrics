# hydrocarbon-volumetrics
Калькулятор запасов углеводородов

## Возможности  
- Расчёт STOIIP/GIIP объёмным методом
- Интеграция с LAS-файлами
- Визуализация кривых ГИС
- Экспорт результатов


## Структура проекта:
hydrocarbon-volumetrics/
├── src/
│   ├── calculator.py       # Основной расчётный модуль
│   └── visualization.py    # Построение графиков
├── data/
│   └── example_well.las    # Пример LAS-файла
├── tests/
│   └── test_calculator.py  # Тесты
├── docs/
│   └── tutorial.ipynb     # Jupyter-ноутбук с примерами
├── README.md               # Описание проекта
├── requirements.txt        # Зависимости
└── LICENSE                 # Лицензия MIT


## Установка:
```bash
git clone git@github.com:UMAtaullin/hydrocarbon-volumetrics.git
python3 -m venv .env
. .env/bin/activate
pip install -r requirements.txt
```

## Что еще можно сделать:
1. Обработка нескольких горизонтов 
2. Построить карты распределения параметров (например, через matplotlib) 
3. Реализовать вероятностный расчёт (P10/P50/P90) через Монте-Карло