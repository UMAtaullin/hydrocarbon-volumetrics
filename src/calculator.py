import numpy as np
from lasio import LASReader


class HydrocarbonCalculator:
    """
    Калькулятор запасов нефти (STOIIP) и газа (GIIP) по объёмному методу.
    Поддерживает загрузку данных из LAS-файлов.
    """

    def __init__(self, area_m2, bo=1.2, bg=0.0035, oil_density=0.85, gas_density=0.75):
        """
        :param area_m2: Площадь месторождения (м²)
        :param bo: Объёмный коэффициент нефти (д.ед.)
        :param bg: Объёмный коэффициент газа (д.ед.)
        :param oil_density: Плотность нефти (т/м³)
        :param gas_density: Плотность газа (т/м³)
        """
        self.area = area_m2
        self.bo = bo
        self.bg = bg
        self.oil_density = oil_density
        self.gas_density = gas_density

    def calculate_stoiip(self, thickness, porosity, oil_saturation):
        """Расчёт запасов нефти (м³ и тонны)"""
        stoiip_m3 = self.area * thickness * porosity * oil_saturation / self.bo
        stoiip_ton = stoiip_m3 * self.oil_density
        return {"m3": stoiip_m3, "tons": stoiip_ton}

    def calculate_giip(self, thickness, porosity, gas_saturation):
        """Расчёт запасов газа (м³ и тонны)"""
        giip_m3 = self.area * thickness * porosity * gas_saturation / self.bg
        giip_ton = giip_m3 * self.gas_density
        return {"m3": giip_m3, "tons": giip_ton}

    def from_las(self, las_path, vsh_cutoff=0.3):
        """Загрузка данных из LAS-файла"""
        las = LASReader(las_path)
        df = las.df()
        df["VSH"] = 1 - df["GR"] / 100  # Пример расчёта глинистости

        clean_zone = df[df["VSH"] < vsh_cutoff]
        return {
            "thickness": len(clean_zone) * 0.1,  # Предполагаем шаг дискретизации 0.1 м
            "porosity": clean_zone["PHIT"].mean(),
            "oil_saturation": 1 - clean_zone["SW"].mean(),
        }
