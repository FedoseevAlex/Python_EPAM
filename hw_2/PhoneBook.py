# Create phonebook dict key -- name: value -- list of numbers
pbook = dict()


def pbook_add() -> None:
    """Adds a new entry in phone book.\
    Asks user to type name and number, then adds it to the phone book.
    """
    print('New entry addition')

    name = pbook_ask_name()

    # Checking phone number is numeric only
    while True:
        pnumber = str(input('Enter number for {}: '.format(name)))
        # Remove whitespaces to allow type number like: 1 234 567 89 01
        if not pnumber.replace(' ', '').isdigit():
            print('It seems that "{}" is not number. Try again.'.format(pnumber))
            continue
        else:
            break

    # Check key presence in pbook
    if name not in pbook.keys():
        # If there is not such name, then create a new key and add phone number
        pbook[name] = list()
        pbook[name].append(pnumber)
    else:
        # If key is present, then just add new number
        pbook[name].append(pnumber)

    print('Addition successful! "{} - {}"'.format(name, pnumber))


def pbook_delete() -> None:
    """Removes name from phone book.
    :return: None
    """
    # If phone book is empty - exit
    if not pbook:
        print('Phone book is empty')
        return

    print('Delete entry')
    # Print names in phone book
    pbook_print()

    name = pbook_ask_name()

    # Check key presence in pbook
    if name not in pbook.keys():
        # If there is not such name, then print error
        print('Name - "{}" is not in the phone book')
    else:
        # If key is present, delete it
        pbook.pop(name)
        print('Name "{}" deleted successfully! '.format(name))


def pbook_print(*args) -> None:
    """Prints name and all known numbers.
    If function called without arguments then it prints all names in phone book.
    :param args: names to print their numbers
    :type args: str
    :return: None
    """
    # Check if args is empty or not
    if args:
        # If not empty then print number for all names in args
        for name in args:
            if name in pbook.keys():
                print('Name\tnumber')
                for number in pbook[name]:
                    print('{}\t{}'.format(name, number))
            else:
                print('There is no such name!')
    else:
        # If args is empty print all available names
        print('Available names:')
        for name in pbook.keys():
            print('{}'.format(name))


def pbook_search() -> None:
    """Handles search in phone book.
    :return: None
    """
    if pbook:
        name = pbook_ask_name()
        pbook_print(name)
    else:
        print('Phone book is empty')


def pbook_ask_name() -> str:
    """Handles input from user. Will ask normal name until user give up.\
    Accepts normal human names like: "John", "Peter" or even "Abdulla ibn Hattab".\
    Refuses names like: "killer2005", "DesTR()Y3R" and so on.\
    :return: string with name\
    """
    # Checking whether the name string contains only alphabetic characters
    while True:
        name = str(input('Enter name: '))
        # Remove all spaces
        if not name.replace(' ', '').isalpha():
            print('"{}" is not normal human name. Try again.'.format(name))
            continue
        else:
            return name


# Create main menu actions dict
menu = dict().fromkeys(range(1, 4))
menu[1] = pbook_add
menu[2] = pbook_search
menu[3] = pbook_delete


def pbook_process() -> None:
    """Function that handles logic of the phone book.
    :return: None
    """
    print('Homework 2.1 Phone Book')

    menu_print = ['Choose menu', '1. Add', '2. Search', '3. Delete', '4. Exit']

    while True:
        # Ask user to choose valid menu item
        while True:
            print(*menu_print, sep='\n')
            user_choise = str(input('>> '))

            if user_choise.isdigit():
                user_choise = int(user_choise)
                break
            else:
                print('Wrong input! Type number like 1, 2, 3 ...')
                continue
        # Do corresponding job
        if 0 < user_choise <= 3:
            menu[user_choise]()
        elif user_choise == 4:
            break
        else:
            continue
        input('Press Enter ...')

pbook_process()
