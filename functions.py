def hello_world():
    """Prints 'Hello World' to the screen"""

    print "Hello World"


def hi_name(name):
    """Prints 'Hi [string]' to screen"""

    print "Hi", name


def product(num1, num2):
    """Prints the product of two integers"""

    print num1 * num2


def repeat(text, times):
    """Prints the given text [times] number of times, with no spaces or line breaks"""

    print text * times


def find_zero(num):
    """Tells the user if the given number is higher, lower, or equal to 0"""

    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"


def mult_of_3(num):
    """Determines if the given integer is evenly divisible by 3"""

    if num % 3 == 0:
        return True
    else:
        return False


def num_spaces(sentence):
    """Determines the number of spaces in a given sentence"""

    spaces = 0

    for char in sentence:
        if char == " ":
            spaces += 1

    return spaces


def add_tip(meal, tip=.15):
    """Determines the total cost (meal and tip) of a restaurant meal"""

    return meal + meal * tip


def sign_parity(num):
    """Determines whether a given integer is positve or negative, and whether integer
    is even or odd. Function returns this data as a tuple.
    """

    # Determine sign
    if num >= 0:
        sign = 'Positive'
    else:
        sign = 'Negative'

    # Determine parity
    if num % 2 == 0:
        parity = 'Even'
    else:
        parity = 'Odd'

    return (sign, parity)
    # test located in line 117, since code generally comes after all functions are defined.


def add_tax(price, state, tax=.05):
    """Determines the total price, tax included, of an item given its list price.
    If the item is from California, the tax is updated to the higher, CA amount
    """

    if state == "CA":
        tax = .07

    return price + price * tax


def title_name(name, title="Engineer"):
    """Prints the name and job title of a given person"""

    return title + ' ' + name


def print_letter(addressee, a_title, sender):
    """Prints a flattering letter to the adressee"""

    reciever = title_name(addressee, a_title)

    print "Dear {r}, I think you are amazing!\nSincerely, {s}".format(r=reciever, s=sender)


def append_nums(numbers, num):
    """Appends the given number to the given string"""

    numbers.append(num)

    print numbers


# Unpack the results of sign_parity(int), print both.
num_sign, num_parity = sign_parity(-6)
print num_sign
print num_parity
