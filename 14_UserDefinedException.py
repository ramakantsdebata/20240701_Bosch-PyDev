class InvalidAgeDataType(TypeError):
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
        super().__init__(msg, code)

class InvalidAgeValueError(ValueError):
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
        super().__init__(msg, code)


def CheckAge(age):
    if isinstance(age, int) == False:
        raise InvalidAgeDataType("Age can't be non-integer", 1001)
    elif age < 0:
        raise InvalidAgeValueError("Age can't be Negative", 1002)
    elif age < 18:
        raise InvalidAgeValueError("Still can't vote", 1003)
    else:
        print("Age is Valid")



#######################################################################################

def Main():
    age = "Five"

    try:
        CheckAge(age)
    except InvalidAgeDataType as ex:
        print(f"Exception : {ex!r}")
    except InvalidAgeValueError as ex:
        print(f"Exception : {ex!r}")
    except Exception as ex:
        print(f"Exception : {ex!r}")

if __name__ == '__main__':
    Main()