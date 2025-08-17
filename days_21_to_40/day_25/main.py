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
    weather_data_pandas = pandas.read_csv(WEATHER_DATA_FILE)
    print(weather_data_pandas["temp"])

def get_weather_data_with_pandas():
    return pandas.read_csv(WEATHER_DATA_FILE)

show_weather_data_with_file()

show_weather_data_with_csv()
show_temperatures_with_csv()

show_weather_data_with_pandas()
show_temperatures_with_pandas()

weather_data = get_weather_data_with_pandas()
weather_data_dict = weather_data.to_dict()
print(weather_data_dict)

temperatures = weather_data["temp"]
temperature_list = temperatures.to_list()
print(temperature_list)

# Average temperature
average_temp = sum(temperature_list) / len(temperature_list)
print(f"Average temperature: {round(average_temp, 2)}")

average_temp_pandas = weather_data["temp"].mean()
print(f"Average temperature using pandas.Series.mean(): {round(average_temp_pandas, 2)}")

highest_temperature = weather_data["temp"].max()
print(f"Highest temperature for the week is: {highest_temperature}")

# object notation
print(weather_data.temp)

# accessing rows
monday = weather_data[weather_data.day == "Monday"]
print(f"The weather data for Monday:\n{monday}")

# day with max temperature
day_data = weather_data[weather_data.temp == weather_data.temp.max()]
print(day_data.day)

# create a DataFrame from scratch
student_dict = {
    "students": ["David", "Ralph", "Manos"],
    "scores": [35, 86, 56]
}

student_data = pandas.DataFrame(student_dict)
print(student_data)

# save the data in a new csv file
student_data.to_csv("student_data.csv")

