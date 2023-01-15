import pytest

from homeassistant.components.homematic import _create_ha_id


def test_create_ha_id():
    # Casos de teste com entradas válidas
    assert _create_ha_id("Device1", "channel1", None, 1) == "Device1"
    assert _create_ha_id("Device1", "channel1", None, 2) == "Device1 channel1"
    assert _create_ha_id("Device1", "channel1", "param1", 1) == "Device1 param1"
    assert (
        _create_ha_id("Device1", "channel1", "param1", 2) == "Device1 channel1 param1"
    )

    # Casos de teste com entradas inválidas
    assert _create_ha_id(None, "channel1", "param1", 1) == None
    assert _create_ha_id("Device1", None, "param1", 2) == None
    assert _create_ha_id("Device1", "channel1", None, -1) == None
    assert _create_ha_id(None, "channel1", "param1", 2) == None

