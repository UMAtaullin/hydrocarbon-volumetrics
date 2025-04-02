import argparse
from src.calculator import HydrocarbonCalculator
from src.config_loader import load_config, validate_config


def main():
    parser = argparse.ArgumentParser(description="Калькулятор запасов углеводородов")
    parser.add_argument(
        "--config", default="config/default.yaml", help="Путь к конфиг-файлу"
    )
    parser.add_argument("--las", help="Путь к LAS-файлу")
    args = parser.parse_args()

    config = load_config(args.config)
    validate_config(config)

    calc = HydrocarbonCalculator(**config["calculator"])

    if args.las:
        results = calc.from_las(args.las)
        print(f"Результаты:\n{results}")


if __name__ == "__main__":
    main()
