# NetworkError has base RuntimeError
# and not Exception
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Error")

except Networkerror as e:
    print(e.args)


# class Error is derived from super class Exception
class Error(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass


class TransitionError(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex

        # Error message thrown is saved in msg
        self.msg = msg


try:
    raise (TransitionError(2, 3 * 2, "Not Allowed"))

# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occurred: ', error.msg)


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class zerodivision(Error):
    """Raised when the input value is zero"""
    pass


try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise zerodivision
except zerodivision:
    print("Input value is zero, try again!")
    print()