import requests
from prometheus_client import CollectorRegistry, Gauge

HOURLY_RED_HAT = "https://api.weather.gov/gridpoints/RAH/73,57/forecast/hourly"
def get_temperature():
    result = requests.get(HOURLY_RED_HAT)
    return result.json()["properties"]["periods"][0]["temperature"]





def prometheus_temperature(num):
    registry = CollectorRegistry()
    g = Gauge("red_hat_temp", "Temperature at Red Hat HQ", registry=registry)
    g.set(num)
    return registry


def main():
    #print(get_temperature())
    prometheus_temperature(10)


main()
