# A piece of data to process
friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
    {'name': 'Джон', 'gender': 'Мужской', 'sport': 'Борьба', 'email': 'email1@email2.com'},
    {'name': 'Рональд', 'gender': 'Мужской', 'sport': 'Футбол', 'email': 'email1@email3.com'},
    {'name': 'Джилл', 'gender': 'Женский', 'sport': 'Теннис', 'email': 'email1@email4.com'},
]

# A dict that acts as mask for data
res_fields = {}


def select(*field_name: str) -> None:
    """Specify fields to show in output
    :param field_name: arbitrary number of fields
    :type field_name: str
    :return: None
    """
    global res_fields
    # Add fields to resulting data
    res_fields.update({name: [] for name in field_name if name not in res_fields})


def field_filter(field_name: str, *collection: list) -> None:
    """Specify field name and possible values to sort data
    :param field_name: name of field to be filtrated
    :type field_name: str
    :param collection: possible field values
    :type collection: list
    :return: None
    """
    # We'll modify global variable
    global res_fields
    if field_name in res_fields.keys():
        res_fields[field_name].extend(*collection)


def query(collection: list, *args) -> list:
    """Perform data filtrating based on fields specified in field_filter and shows output fields\
    assigned in select
    :param collection: data container to process
    :type collection: list of dicts
    :param args: add select and filters here
    :return: list with requested data
    """
    to_return = []
    if res_fields:
        for item in collection:
            for field in res_fields:
                # If fields match and value list is empty  -> True
                # If fields match and value in data is in mask value list -> True
                # If fields match and value in data is not in mask value list -> False
                # If fields not match -> False
                if field in item.keys() and (item[field] in res_fields[field] or not res_fields[field]):
                    continue
                else:
                    break
            else:
                to_return.append({key: value for key, value in item.items() if key in res_fields.keys()})
    return to_return


# Test data
"""
result = query(
friends,
select('name', 'gender', 'sport'),
field_filter('sport', ['Баскетбол', 'Волейбол']),
field_filter('gender', ['Мужской']))

print(result) # [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'}, ​​​​]
res_fields = {}

result = query(
friends,
select('name', 'gender', 'sport'),
field_filter('gender', ['Мужской']))

print(result)
res_fields = {}

result = query(
friends,
select('name', 'sport'),
field_filter('gender', ['Мужской']))

print(result)
res_fields = {}

result = query(
friends,
field_filter('gender', ['Мужской']))

print(result)
res_fields = {}
"""
result = query(
friends,
select('name', 'email'),
field_filter('gender', ['Мужской']))

print(result)
res_fields = {}
"""
result = query(
friends,
select('email'),
field_filter('name', ['Джон', 'Рональд']),
select('gender'))

print(result)
res_fields = {}
"""
"""Если в фильтре есть поле, которого нет в селект, то игнорим его и выводим все, но с учетом селекта"""
