f_obj = open("en_climate_hourly_AB_3060330_10-2023_P1H.csv")
list_of_temps = []
header = f_obj.readline()
for line in f_obj:
    columns = line.split(",")
    if len(columns)>=10:
        list_of_temps.append(columns[9])
print(list_of_temps)
list_of_number = []
for temp in list_of_temps:
    number = float(temp.replace('"', ""))
    list_of_number.append(number)
print(list_of_number) 
print(max(list_of_number))