# hydrocarbon-volumetrics
Калькулятор запасов углеводородов

## Возможности  
- Расчёт STOIIP/GIIP объёмным методом
- Интеграция с LAS-файлами
- Визуализация кривых ГИС
- Экспорт результатов


## Структура проекта:
hydrocarbon-calculator/
├── src/
│   ├── cli.py            # Точка входа (командная строка)
│   ├── calculator.py     # Логика расчётов
│   └── config_loader.py  # Загрузка настроек
├── config/
│   └── default.yaml      # Параметры по умолчанию
├── data/
│   ├── input/            # Папка для LAS-файлов
│   └── output/           # Результаты расчётов
├── docs/
│   └── user_guide.md     # Инструкция
└── README.md


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