import numpy as np
import lasio


class HydrocarbonCalculator:
    def __init__(self, area_m2, bo=1.2, bg=0.0035, oil_density=0.85, gas_density=0.75):
        self.area = area_m2
        self.bo = bo
        self.bg = bg
        self.oil_density = oil_density
        self.gas_density = gas_density

    def calculate_stoiip(self, thickness, porosity, oil_saturation):
        """Расчёт запасов нефти (STOIIP)"""
        stoiip_m3 = self.area * thickness * porosity * oil_saturation / self.bo
        return {
            "m3": stoiip_m3,
            "tons": stoiip_m3 * self.oil_density,
            "bbl": stoiip_m3 * 6.2898,  # Конвертация в баррели
        }

    def from_las(self, las_path, vsh_cutoff=0.3):
        las = lasio.read(las_path)
        df = las.df()

        # Автоматическое определение шага дискретизации
        step = abs(df.index[1] - df.index[0]) if len(df.index) > 1 else 0.1

        # Расчёт параметров
        df["VSH"] = 1 - (df["GR"] / df["GR"].max())
        df["PHIT"] = (2.65 - df["DFAR"]) / (2.65 - 1.0)
        df["PHIT"] = df["PHIT"].clip(0, 0.4)

        clean_zone = df[df["VSH"] < vsh_cutoff]

        return {
            "thickness": len(clean_zone) * step,
            "porosity": clean_zone["PHIT"].mean(),
            "oil_saturation": 0.65,  # По умолчанию
        }
