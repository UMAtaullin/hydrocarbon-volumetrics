import numpy as np
import lasio


class HydrocarbonCalculator:
    """
    Калькулятор запасов нефти (STOIIP) и газа (GIIP) по объёмному методу.
    Поддерживает загрузку данных из LAS-файлов.
    """

    def __init__(self, area_m2, bo=1.2, bg=0.0035, oil_density=0.85, gas_density=0.75):
        self.area = area_m2
        self.bo = bo
        self.bg = bg
        self.oil_density = oil_density
        self.gas_density = gas_density


    def from_las(self, las_path, vsh_cutoff=0.3):
        """Адаптированная версия для новых lasio и вашего формата данных"""
        las = lasio.read(las_path)
        df = las.df()

        # 1. Определяем шаг дискретизации
        if len(df.index) > 1:
            step = abs(df.index[1] - df.index[0])  # Автоматическое определение шага
        else:
            step = 0.1  # Значение по умолчанию

        # 2. Расчёт глинистости через GR (нормализованный)
        df["VSH"] = 1 - (df["GR"] / df["GR"].max())

        # 3. Расчёт пористости через DFAR (формула для песчаников)
        df["PHIT"] = (2.65 - df["DFAR"]) / (2.65 - 1.0)
        df["PHIT"] = df["PHIT"].clip(0, 0.4)  # Ограничиваем реалистичные значения

        # 4. Фильтрация по глинистости
        clean_zone = df[df["VSH"] < vsh_cutoff]

        return {
            "thickness": len(clean_zone) * step,
            "porosity": clean_zone["PHIT"].mean(),
            "oil_saturation": 0.65,  # По умолчанию
        }
