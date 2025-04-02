import argparse
from src.calculator import HydrocarbonCalculator


def format_number(num):
    return f"{num:,.0f}".replace(",", " ")


def main():
    parser = argparse.ArgumentParser(description="Калькулятор запасов нефти (STOIIP)")
    parser.add_argument("--las", required=True, help="Путь к LAS-файлу")
    parser.add_argument(
        "--area", type=float, required=True, help="Площадь месторождения (м²)"
    )
    args = parser.parse_args()

    calc = HydrocarbonCalculator(area_m2=args.area)
    params = calc.from_las(args.las)
    reserves = calc.calculate_stoiip(**params)

    print("\n=== РЕЗУЛЬТАТЫ ===")
    print(f"Параметры пласта:")
    print(f"- Толщина: {params['thickness']:.2f} м")
    print(f"- Пористость: {params['porosity']:.3f}")
    print(f"- Насыщенность: {params['oil_saturation']:.1%}")

    print("\nЗапасы нефти (STOIIP):")
    print(f"- {format_number(reserves['m3'])} м³")
    print(f"- {format_number(reserves['tons'])} тонн")
    print(f"- {format_number(reserves['bbl'])} баррелей")


if __name__ == "__main__":
    main()
