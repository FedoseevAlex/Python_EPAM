def get_data() -> list:
    return [
        {'name': 'Alexey', 'rate': 2, 'course': 'Python'},
        {'name': 'Boris', 'rate': 2, 'course': 'Math'},
        {'name': 'Jean', 'rate': 2, 'course': 'Karate'},
        {'name': 'Elena', 'rate': 1, 'course': 'Python'},
        {'name': 'Chuck', 'rate': 1, 'course': 'Karate'},
        {'name': 'Nikolay', 'rate': 3, 'course': 'Math'},
        {'name': 'Bolo', 'rate': 3, 'course': 'Karate'},
        {'name': 'Vasily', 'rate': 3, 'course': 'Python'},
        {'name': 'Gennadiy', 'rate': 1, 'course': 'Math'},
        {'name': 'Steven', 'rate': 4, 'course': 'Karate'},
        {'name': 'Paul', 'rate': 4, 'course': 'Python'}
    ]


def get_courses(data) -> list:
    return sorted(list({item['course'] for item in data}))


def get_rating(data, course) -> list:
    return ["{} - {}".format(item['rate'], item['name'])
            for item in sorted(data, key=lambda i: i['rate']) if item['course'] == course]


def get_output(course):
    return course + '\n' + '\n'.join(get_rating(get_data(), course))
    

print('\n'.join(map(get_output, get_courses(get_data()))))