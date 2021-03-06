"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and returns
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.


def is_my_hometown(town_name):
    """Check if a town is your hometown.

    Compares town_name and hometown, if they are equivalent it returns True
    otherwise it returns False.
    """

    # Assigned hometown to 'Morgan Hill', checked if town_name is equivalent.
    # Returns True if they are ==, False if they are not ==.
    hometown = "Morgan Hill"
    if town_name == hometown:
        return True
    else:
        return False


def combine_names(first_name, last_name):
    """Combines first and last names into single string.

    Takes first_name and last_name as arguments, string concatenates using
    format and returns the full name as a string.
    """

    # Returns formatted string containing the first_name and last_name.
    return "{} {}".format(first_name, last_name)


def greeting(town_name, first_name, last_name):
    """Greets combined first and last name and references hometown.

    Uses combine_names() to greet first_name + last_name.  If they have
    the same hometown, it says this.  If not, a different greeting is given.
    """

    # Using is_my_hometown checks to see if their hometown
    # and my hometown are equivalent.  If they are, they are greeted by name
    # and told they are from same place.  If not, they are greeting by name
    # and told that I want to visit their hometown.

    if is_my_hometown(town_name):
        print "Hi, {}, we're from the same place!".format(
            combine_names(first_name, last_name))
    else:
        print "Hi {}, I'd like to visit {}!".format(
            combine_names(first_name, last_name), town_name)


###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry",
#        "blackberry", or "currant."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a fruit name and a list of fruits. It should
#        return a new list containing the elements of the input list, along with
#        given fruit, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price of $100 or less and $3 for items over $100. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry.

    If fruit is "strawberry", "raspberry", "blackberry", or "currant" return
    True, otherwise return False.
    """

    # Makes a list of acceptable fruits.  Checks to see if fruit is in fruits
    # and returns boolean.
    fruits = ["strawberry", "raspberry", "blackberry", "currant"]
    if fruit in fruits:
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit.

    If the argument 'fruit' is a berry, determined by is_berry(), then the
    shipping cost is 0.  If the fruit is not a berry then the cost is 5.
    """

    # Checks to see if the fruit is a berry.  If it is return 0, else return 5.
    if is_berry(fruit):
        return 0
    else:
        return 5


def append_to_list(lst, fruit):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    Takes in two arguments lst (a list) and fruit (a string).
    """

    # I'm assuming I can use append() since it was not explicitly stated not to.
    # Used the list method append() to add the fruit onto the end of lst in place.
    lst.append(fruit)
    return lst


def calculate_price(item_base_price, state, tax=.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    Takes arguments item_base_price as a float, state as a two letter
    abbreviated string, and tax as a 2 decimal place float.  The function
    returns the total cost of the item as a float.
    """

    # Standardize the arguments by making the state all caps, item_base_price
    # a float, and setting a base fee of zero.
    state = state.upper()
    item_base_price = float(item_base_price)
    fees = 0

    # Calculate tax and after tax state fees.
    with_tax = item_base_price * tax + item_base_price
    if state == 'CA':
        fees = with_tax * .03
    elif state == 'PA':
        fees = 2.00
    elif state == 'MA':
        if item_base_price <= 100.00:
            fees = 1.00
        else:
            fees = 3.00

    # Return the total cost of the item with taxes and fees included.
    total_cost = with_tax + fees
    return total_cost


###############################################################################

# PART THREE

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


def unpack_and_append(*args):
    """Appends arguments to the end of a new list.

    Takes any number of arguments and appends them to an empty list and then
    returns the list.
    """

    # So this is cool! I actually looked up how to do this on Friday during
    # lab.  I couldn't find my original source, but here is another that is
    # doing the same thing...
    # https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

    # Creats a new list and through a for loop appends all the arguments into
    # this new_list.
    new_list = []
    for arg in args:
        new_list.append(arg)
    return new_list


def multiply_word(word):
    """Multiplies an argument by three.

    Argument taken can be any type, it will be treated and returned as a string.
    """

    # Used format() method to take any argument type and create a string which
    # repeats the argument three times. Using word * 3 creats unintended results
    # for non-string types.
    return '{}{}{}'.format(word, word, word)


def multiply_word_tuple(word):
    """Prints a tuple with index 1 being a word and index 2 being the word *3.

    Takes two arguments, the first a string and the second the result of the
    function multiply_word() for that same string. Returns these arguments as
    a tuple.
    """

    # Print a tuple with two indeces the first the word, and the second word*3
    print (word, multiply_word(word))


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
