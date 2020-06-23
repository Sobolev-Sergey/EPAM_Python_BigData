"""
Есть список словарей: ​

friends = [​​​
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'}, ​​
    {'name': 'Эмили', 'gender': 'Женский' 'sport': 'Волейбол'}, ​​​
    …​​​
]​
​
Напишите функции для работы с массивами данных (стабы уже написаны).
​
Пример работы программы:​

result = query(​​​
    friends,​​​
    select('name', 'gender', 'sport'),​​​
    field_filter('sport', ['Баскетбол', 'Волейбол']),​​​
    field_filter('gender', ['Мужской']),​​​
)

Требуется возможность из списка диктов выбрать интересуюшие нас колонки и фильтрануть данные по ним.

Не забываем документацию!
"""

"""
EPAM Training Python & Big Data 2020. Author: Sergey Sobolev

Select from the list according to the specified criteria.
A list of keys and a filter are passed as criteria.
The filter contains keys and valid values.
"""


from typing import List, Dict, Any

# SECOND SOLUTION


def select(*field_names: str) -> List[Dict[str, Any]]:
    def selection(copy_input_data):
        result_select = []
        for field in copy_input_data:
            field_result = {}
            for field_name in field_names:
                if field[field_name]:
                    field_result[field_name] = field[field_name]
            result_select.append(field_result)

        return result_select

    return selection


def field_filter(field_name: str, *values) -> List[Dict[str, Any]]:
    def filtering(data_after_selection):
        result_filtering = []
        for field in data_after_selection:
            if field[field_name] in str(values):
                result_filtering.append(field)

        return result_filtering

    return filtering


def query(
    data: List[Dict[str, Any]], selection, *filters: callable
) -> List[Dict[str, Any]]:
    copy_input_data = data.copy()
    select_field = selection
    data_after_selection = select_field(copy_input_data)

    for data_filter in filters:
        filter_data = data_filter
        data_after_selection = filter_data(data_after_selection)

    return data_after_selection


# FIRST SOLUTION

# def select(*field_names: str) -> List[str]:
#     """
#     Valid search field or key names

#     :param field_names: The field names
#     :return: List field names
#     """
#     names = []
#     for field_name in field_names:
#         names.append(field_name)

#     return names


# def field_filter(field_name: str, *values) -> Dict[str, Any]:
#     """
#     Converts input parameters to a parameter dictionary for filtering

#     :param field_name: Field names where to search
#     :param values: Values to search
#     :return: Dictionary of parameters for filtering
#     """
#     filters = {}
#     for val in values:
#         filters[field_name] = val

#     return filters


# def query(
#     data: List[Dict[str, Any]], selection, *filters: callable
# ) -> List[Dict[str, Any]]:
#     """
#     Select from the data according to the specified criteria.

#     :param data: List of dictionaries from which to select the appropriate values
#     :param selection: List field names
#     :param filters: Dictionary of parameters for filtering
#     :return: Return list result if successful or empty list otherwise
#     """

#     all_filters = {}
#     for current_filter in filters:
#         for key, value in current_filter.items():
#             if key in selection:
#                 all_filters[key] = value

#     full_result = []
#     number_of_filters = len(all_filters)

#     for field in data:
#         concurrency = 0
#         field_result = {}
#         for key, value in field.items():
#             if key in selection:
#                 field_result[key] = value
#                 for key_filter, value_filter in all_filters.items():
#                     if key == key_filter and value in value_filter:
#                         concurrency += 1
#         if concurrency == number_of_filters:
#             full_result.append(field_result)

#     return full_result


# friends = [
#     {"name": "Sam", "gender": "Man", "sport": "Basketball", "age": 23},
#     {"name": "Emili", "gender": "Girl", "sport": "Volleyball", "age": 33},
#     {"name": "Cray", "gender": "Man", "sport": "Football", "age": 43},
#     {"name": "Lou", "gender": "Girl", "sport": "Hockey", "age": 35},
#     {"name": "John", "gender": "Man", "sport": "Volleyball", "age": 21},
# ]

# result = query(
#     friends,
#     select("name", "gender", "sport"),
#     field_filter("sport", ["Basketball", "Volleyball"]),
#     field_filter("gender", ["Man"]),
# )

# print(result)
# [{'name': 'Sam', 'gender': 'Man', 'sport': 'Basketball'}, {'name': 'John', 'gender': 'Man', 'sport': 'Volleyball'}]

"""
from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc, *filters: ModifierFunc) -> DataType:
    
    # Query data with column selection and filters
    #
    # :param data: List of dictionaries with columns and values
    # :param selector: result of `select` function call
    # :param filters: Any number of results of `field_filter` function calls
    # :return: Filtered data
    
    modifiers = [selector, *filters]
    for modifier in modifiers:
        data = modifier(data)
    return list(data)


def select(*columns: str) -> ModifierFunc:
    
    #Return function that selects only specific columns from dataset
    
    def modifier(data: DataType) -> DataType:
        for row in data:
            yield {col: row[col] for col in columns}
    return modifier


def field_filter(column: str, *values: Any) -> ModifierFunc:
    
    #Return function that filters specific column to be one of `values`
    
    def modifier(data: DataType) -> DataType:
        for row in data:
            if row[column] in values:
                yield row
    return modifier
"""
