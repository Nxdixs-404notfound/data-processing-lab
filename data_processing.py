import csv

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


# Load data from CSV
cities = []
with open('Cities.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['latitude'] = float(row['latitude'])
        row['longitude'] = float(row['longitude'])
        row['temperature'] = float(row['temperature'])
        cities.append(row)


# Print the average temperature of all the cities
avg_temp = aggregate('temperature', lambda scores: sum(scores) / len(scores), cities)
print(avg_temp)

# Print all cities in Germany
germany_cities = filter_items(lambda item: item['country'] == 'Germany', cities)
for c in germany_cities:
    print(c['city'])

# Print all cities in Spain with a temperature above 12°C
spain_cities = filter_items(lambda item: item['country'] == 'Spain' and item['temperature'] > 12, cities)
for c in spain_cities:
    print(c['city'])

# Count the number of unique countries
all_countries = aggregate('country', list, cities)
unique_countries = len(set(all_countries))
print(unique_countries)

# Print the average temperature for all the cities in Germany
avg_germany = aggregate('temperature', lambda scores: sum(scores) / len(scores), germany_cities)
print(avg_germany)

# Print the max temperature for all the cities in Italy
italy_cities = filter_items(lambda item: item['country'] == 'Italy', cities)
max_italy = aggregate('temperature', max, italy_cities)
print(max_italy)
