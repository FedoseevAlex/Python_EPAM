#!/usr/bin/env/ python3.6
# Task #L5.1 Wine class


class Wine:
    """
    Class to characterise wine.
    """
    from datetime import date
    
    def __init__(self, name: str, trademark: str, location: str, year, month, day):
        self.name = name
        self.trademark = trademark
        self.location = location
        self._annotation = list()
        self.bottling_date = self.date(year, month, day)

    def set_name(self, name: str) -> None:
        """
        Sets a name of wine object.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.get_name()
        'Wine name'
        >>> w.set_name('Another wine name')
        >>> w.get_name()
        'Another wine name'
        :param name: desired wine name.
        :type name: str.
        :return: None.
        """
        if type(name) == str:
            self.name = name
        else:
            print('Wrong type error! Got "{}", must be str'.format(type(name)))
    
    def get_name(self) -> str:
        """
        Get a wine name as string.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.get_name()
        'Wine name'
        :return: str
        """
        return self.name
    
    def set_trademark(self, trademark: str) -> None:
        """
        Sets new trademark for wine object.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15
        >>> w.get_trademark()
        'Wine trademark'
        >>> w.set_trademark('Another wine trademark')
        >>> w.get_trademark()
        >>> 'Another wine trademark'
        :param trademark: Desired trademark.
        :type trademark: str.
        :return: None.
        """
        self.trademark = trademark
        
    def get_trademark(self) -> str:
        """
        Get a wine trademark as string.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.get_trademark()
        'Wine trademark'
        :return: str
        """
        return self.trademark
    
    def set_location(self, location: str) -> None:
        """
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15
        >>> w.get_location()
        'Wine location'
        >>> w.set_location('Another wine location')
        >>> w.get_location()
        >>> 'Another wine location'
        :param location: Desired location.
        :type location: str.
        :return: None.
        """
        self.location = location
        
    def get_location(self) -> str:
        """
        Get a wine location as string.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.get_location()
        'Wine location'
        :return: str
        """
        return self.location
        
    def add_annotation(self, *args) -> None:
        """
        Add test to wine annotation.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.add_annotation('string 1', 'string 2', ... , 'string n')
        >>> w.get_annotation()
        [string 1, string 2, ..., string 3]
        >>> w.add_annotation()
        Enter annotation:
        > (awaits user to input something)
        :param args: Strings to add in annotation. If no arguments provided then user input.
        :type args: str
        :return: None.
        """
        if args:
            self._annotation.extend(args)
        else:
            print('Enter annotation: \n')
            while True:
                input_line = input('> ')
                self._annotation.append(input_line)
                if len(input_line) == 0:
                    break
                    
    def clear_annotation(self) -> None:
        """
        Clear annotation container.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.add_annotation('string 1', 'string 2', ... , 'string n')
        >>> w.get_annotation()
        [string 1, string 2]
        >>> w.clear_annotation()
        >>> w.get_annotation()
        'Annotation is empty!'
        :return: None
        """
        self._annotation.clear()
        
    def get_annotation(self) -> list:
        """
        Get annotation as list of strings.
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.add_annotation('string 1', 'string 2', ... , 'string n')
        >>> w.get_annotation()
        [string 1, string 2]
        :return: list
        """
        if len(self._annotation) == 0:
            print('Annotation is empty!')
        else:
            # print(*self._annotation, sep='\n')
            return self._annotation
    
    def age(self, date, month, year) -> list:
        """
        Calculate wine age and return it as a list [years, months, days].
        >>> w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
        >>> w.get_age(2018, 7, 15)
        [28, 0, 7]
        :param date:
        :param month:
        :param year:
        :return:
        """
        current_date = self.date(date, month, year)
        age = current_date - self.bottling_date
        years, days = divmod(age.days, 365)
        months, days = divmod(days, 30)
        # print('Age is: {} years, {} months'.format(years, months, days))
        return [years, months, days]


w = Wine('Wine name', 'Wine trademark', 'Wine location', 1990, 7, 15)
print(w.age(2018, 7, 15))
