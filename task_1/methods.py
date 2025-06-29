from enum import Enum, auto


class TemperatureUnit(Enum):
    CELSIUS = auto()
    FAHRENHEIT = auto()


class Temperature:
    def __init__(self, temperature, *, unit=TemperatureUnit.CELSIUS):
        self.temperature = temperature
        self.unit = unit

    @classmethod
    def from_celsius_to_fahrenheit(cls, temperature_in_celsius):
        temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
        return cls(temperature_in_fahrenheit, unit=TemperatureUnit.FAHRENHEIT)
    
    @property
    def in_kelvins(self):
        if self.unit == TemperatureUnit.CELSIUS:
            return self.temperature + 273.15
        return (self.temperature - 32) * 5/9 + 273.15
    
    @staticmethod
    def is_water_freezing_point_at(temperature, *, unit=TemperatureUnit.CELSIUS):
        if unit == TemperatureUnit.CELSIUS:
            return temperature <= 0
        return temperature <= 32


def test_temperature_initialization():
    # Проверка создания с Цельсиями
    temp_c = Temperature(25, unit=TemperatureUnit.CELSIUS)
    assert temp_c.temperature == 25
    assert temp_c.unit == TemperatureUnit.CELSIUS
    
    # Проверка создания с Фаренгейтами
    temp_f = Temperature(77, unit=TemperatureUnit.FAHRENHEIT)
    assert temp_f.temperature == 77
    assert temp_f.unit == TemperatureUnit.FAHRENHEIT


def test_from_celsius_to_fahrenheit():
    # Конвертация 25°C → 77°F
    temp = Temperature.from_celsius_to_fahrenheit(25)
    assert temp.temperature == 77
    assert temp.unit == TemperatureUnit.FAHRENHEIT


def test_in_kelvins():
    # Проверка для Цельсиев (25°C → 298.15K)
    temp_c = Temperature(25, unit=TemperatureUnit.CELSIUS)
    assert temp_c.in_kelvins == 298.15
    
    # Проверка для Фаренгейтов (77°F → 298.15K)
    temp_f = Temperature(77, unit=TemperatureUnit.FAHRENHEIT)
    assert temp_f.in_kelvins == 298.15


def test_is_water_freezing_point_at():
    # Проверка для Цельсиев
    assert Temperature.is_water_freezing_point_at(0) is True
    assert Temperature.is_water_freezing_point_at(1) is False
    
    # Проверка для Фаренгейтов
    assert Temperature.is_water_freezing_point_at(32, unit=TemperatureUnit.FAHRENHEIT) is True
    assert Temperature.is_water_freezing_point_at(33, unit=TemperatureUnit.FAHRENHEIT) is False

test_from_celsius_to_fahrenheit()
test_in_kelvins()
test_is_water_freezing_point_at()
test_temperature_initialization()