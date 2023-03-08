# class CustomError(Exception):
#     pass
#
#
# raise CustomError("TEST")
# print("test")

class MyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(3 * 2)
except MyError as er:
    print("Error", er.value)
    print("Error", er)
