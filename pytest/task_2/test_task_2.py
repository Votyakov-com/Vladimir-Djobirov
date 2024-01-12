import pytest

from task_2 import WateringSystem


@pytest.fixture
def watering_system():
    return WateringSystem()


def test_initial_soil_moisture(watering_system):
    watering_system.add_area("Garden", 30)
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


def test_add_water(watering_system):
    watering_system.add_water(500)
    assert watering_system.water_level == 2500


def test_add_existing_area(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.add_area("Garden", 50)
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


def test_add_new_area(watering_system):
    watering_system.add_area("Lawn", 40)
    assert "Lawn" in watering_system.areas


def test_water_spray_supply(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.water_spray_supply("Garden", 15)
    assert watering_system.areas["Garden"]["spray_water"] == 15


@pytest.mark.parametrize(
    "area, duration, expected_moisture",
    [
        ("Garden", 30, 100),
        ("Flowerbed", 20, 100),
    ],
)
def test_water_area(watering_system, area, duration, expected_moisture):
    watering_system.add_area("Garden", 0)
    watering_system.add_area("Flowerbed", 0)
    watering_system.water_area(area, duration)
    assert watering_system.areas[area]["soil_moisture"] == expected_moisture


def test_water_area_not_enough_water(watering_system):
    watering_system.water_level = 0
    watering_system.add_area("Garden", 30)
    assert watering_system.water_area("Garden", 30) is None


def test_max_soil_moisture(watering_system):
    watering_system.add_area("Garden", 100)
    result = watering_system.water_area("Garden", 30)
    assert result is None


def test_soil_moisture_after_long_watering(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.water_area("Garden", 60)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100


def test_soil_moisture_after_watering(watering_system):
    watering_system.add_area("Garden", 30)
    watering_system.water_area("Garden", 30)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100
