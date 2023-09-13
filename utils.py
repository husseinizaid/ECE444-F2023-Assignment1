class utils:

    def reversed(number):
        if (isinstance(number, int)):
            number = int(number)
            reversed = 0
            while number > 0:
                lastDigit = number % 10
                reversed = reversed * 10 + lastDigit
                number = number // 10
            return reversed
        else:
            return "Please type an integer as your input!"
        

    def formatter(number):
        if (isinstance(number, int)):
            number = int(number)
            return (bin(number), oct(number))
        else:
            return "Please type an integer as your input!"


