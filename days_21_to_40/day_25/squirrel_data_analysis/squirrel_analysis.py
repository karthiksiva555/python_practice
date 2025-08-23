import pandas

DATA_FILE_PATH = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pandas.read_csv(DATA_FILE_PATH)
gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
squirrel_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
}
print(squirrel_data_dict)
squirrel_data_by_fur_color = pandas.DataFrame(squirrel_data_dict)
squirrel_data_by_fur_color.to_csv("squirrel_count.csv")

# use group by
# squirrel_grouped_by_fur = squirrel_data.groupby("Primary Fur Color")
# print(squirrel_grouped_by_fur.count())