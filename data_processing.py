import csv

class Table:
    """
    A class representing a table of data with filtering and aggregation capabilities.
    """
    def __init__(self, data):
        self.data = data

    def filter_items(self, condition):
        """Return a new Table containing only items that satisfy the condition."""
        filtered_data = [item for item in self.data if condition(item)]
        return Table(filtered_data)

    def aggregate(self, aggregation_key, aggregation_function):
        """Aggregate values associated with aggregation_key using the provided function."""
        values = [item[aggregation_key] for item in self.data]
        return aggregation_function(values)

    def get_data(self):
        """Return the raw list of dictionaries."""
        return self.data


class DataLoader:
    """
    A class responsible for loading CSV data into a Table object.
    """
    @staticmethod
    def load_csv(filename):
        cities = []
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['latitude'] = float(row['latitude'])
                row['longitude'] = float(row['longitude'])
                row['temperature'] = float(row['temperature'])
                cities.append(row)
        return Table(cities)


# --- Load data using DataLoader ---
table = DataLoader.load_csv('Cities.csv')

# 1. Print the average temperature of all the cities
avg_temp = table.aggregate('temperature', lambda scores: sum(scores) / len(scores))
print(avg_temp)

# 2. Print all cities in Germany
germany_table = table.filter_items(lambda item: item['country'] == 'Germany')
for c in germany_table.get_data():
    print(c['city'])

# 3. Print all cities in Spain with a temperature above 12°C
spain_table = table.filter_items(lambda item: item['country'] == 'Spain' and item['temperature'] > 12)
for c in spain_table.get_data():
    print(c['city'])

# 4. Count the number of unique countries
all_countries = table.aggregate('country', list)
unique_countries = len(set(all_countries))
print(unique_countries)

# 5. Print the average temperature for all the cities in Germany
avg_germany = germany_table.aggregate('temperature', lambda scores: sum(scores) / len(scores))
print(avg_germany)

# 6. Print the max temperature for all the cities in Italy
italy_table = table.filter_items(lambda item: item['country'] == 'Italy')
max_italy = italy_table.aggregate('temperature', max)
print(max_italy)
