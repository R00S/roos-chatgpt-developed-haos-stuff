from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([HaosForecastSensor()])

class HaosForecastSensor(Entity):
    @property
    def name(self):
        return "HAOS Feature Forecast"

    @property
    def state(self):
        return "Initialized"
