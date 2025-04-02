import yaml
from pathlib import Path


def load_config(config_path):
    """
    Загрузка YAML-конфигурации
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config


def validate_config(config):
    """
    Проверка обязательных полей конфига
    """
    required = ["calculator"]
    for field in required:
        if field not in config:
            raise ValueError(f"В конфиге отсутствует обязательное поле: {field}")
