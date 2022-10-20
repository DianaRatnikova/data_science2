import pandas as pd

stations = pd.read_csv(
    open('bus_stops.csv', 'r', encoding='cp1251'),
    sep=';'
)

if __name__ == "__main__":
    # 5 строк по усолчанию, но можно в скобках назвать количество
    print(stations.head())
    # сгруппировать данные по Station и посчитать количество сгруппированных элементов:
    stations_count = stations.groupby(['District']).size()
    print(stations_count)
    print(f"{type(stations_count) = }")
    # Отсортируем результат по значению
    stations_count.sort_values()
    print(stations_count)