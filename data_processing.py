import csv

def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]

def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)

cities = []
with open('Cities.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['latitude'] = float(row['latitude'])
        row['longitude'] = float(row['longitude'])
        row['temperature'] = float(row['temperature'])
        cities.append(row)

avg_temp = aggregate('temperature', lambda scores: sum(scores) / len(scores), cities)
print("Average temperature of all cities:", avg_temp)
