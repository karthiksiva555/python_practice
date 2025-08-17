import csv
import pandas

WEATHER_DATA_FILE = "weather_data.csv"

def show_weather_data_with_file():
    with open(WEATHER_DATA_FILE) as file:
        table_as_csv = file.read().splitlines()
        print(table_as_csv)

def show_weather_data_with_csv():
    with open(WEATHER_DATA_FILE) as file:
        data = csv.reader(file)
        for row in data:
            print(row)

def show_temperatures_with_csv():
    with open(WEATHER_DATA_FILE) as file:
        data = csv.reader(file)
        temperatures = []
        for row in data:
            if row[1] != "temp":
                temperatures.append(int(row[1]))
        print(temperatures)

def show_weather_data_with_pandas():
    weather_data = pandas.read_csv(WEATHER_DATA_FILE)
    print(type(weather_data))
    print(type(weather_data["temp"]))
    print(weather_data)

def show_temperatures_with_pandas():
    weather_data = pandas.read_csv(WEATHER_DATA_FILE)
    temperatures = weather_data["temp"]
    print(temperatures)

show_weather_data_with_file()

show_weather_data_with_csv()
show_temperatures_with_csv()

show_weather_data_with_pandas()
show_temperatures_with_pandas()





