# A piece of data to process
friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
    {'name': 'Джон', 'gender': 'Мужской', 'sport': 'Борьба', 'email': 'email1@email2.com'},
    {'name': 'Рональд', 'gender': 'Мужской', 'sport': 'Футбол', 'email': 'email1@email3.com'},
    {'name': 'Джилл', 'gender': 'Женский', 'sport': 'Теннис', 'email': 'email1@email4.com'},
    {'name': 'Софи', 'gender': 'Женский', 'sport': 'Шахматы', 'email': 'email2@email4.com'},
    {'name': 'Айзек', 'gender': 'Мужской', 'sport': 'Шахматы', 'email': 'email3@email4.com'},
    {'name': 'Брайан', 'gender': 'Мужской', 'sport': 'Теннис', 'email': 'email4@email4.com'},
    {'name': 'Марта', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email5@email4.com'},
]

# List of fields to show in output
select_res = []
# Dict key - fields: value - list of fields values to filter
filter_res = {}


def select(*field_name: str) -> None:
    """Specify fields to show in output
    :param field_name: arbitrary number of fields
    :type field_name: str
    :return: None
    """
    global select_res
    # Add fields to be shown
    select_res.extend([name for name in field_name if name not in select_res])


def field_filter(field_name: str, *collection: list) -> None:
    """Specify field name and possible values to sort data
    :param field_name: name of field to be filtrated
    :type field_name: str
    :param collection: possible field values
    :type collection: list
    :return: None
    """
    # We'll modify global variable
    global filter_res
    filter_res.update({field_name: list(*collection)})


def query(collection: list, *args) -> list:
    """Perform data filtrating based on fields specified in field_filter and shows output fields\
    assigned in select
    :param collection: data container to process
    :type collection: list of dicts
    :param args: add select and filters here
    :return: list with requested data
    """
    global select_res, filter_res
    to_return = []
    # If select was not called then empty list
    #if select_res:
    if args:
        for item in collection:
            # Compare each field that are to be filtered
            for field in filter_res:
                if field in item.keys() and item[field] in filter_res[field]:
                    continue
                else:
                    break
            else:
                # Return only selected fields
                to_return.append({key: value for key, value in item.items() if key in select_res})
    # Clean select and filter options before return
    select_res = []
    filter_res = {}
    return to_return


# Tests

result = query(
friends,
select('name', 'gender', 'sport'),
field_filter('sport', ['Баскетбол', 'Волейбол']),
field_filter('gender', ['Мужской']))

print(result) # [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'}, ​​​​]

"""
result = query(
friends,
select('name', 'gender', 'sport'))


print(result)


result = query(
friends,
select('name', 'sport'),
field_filter('gender', ['Женский']))

print(result)


result = query(
friends,
field_filter('gender', ['Мужской']))

print(result)


result = query(
friends,
select('name', 'email'),
field_filter('gender', ['Мужской', 'Женский', 'Нет']))

print(result)


result = query(
friends,
select('name', 'sport'),
field_filter('name', ['Джон', 'Рональд']),
field_filter('sport', ['Борьба']),
select('email'))

print(result)
"""
