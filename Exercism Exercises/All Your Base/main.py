'''
This function is designed to take take a number in any base between 2 and 36, and return the number
in any other base between 2 and 36.
'''

def convert_base(input_num, input_base: int, output_base: int):
    conversion = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I',
                  19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R',
                  28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}

    try:
        num = int(str(input_num), input_base)
        if input_base < 2:
            raise ValueError("Input base must be greater than 2.")
        if output_base < 2:
            raise ValueError("Output base must be greater than 2.")
        if input_base > 36 or output_base > 36:
            raise valueError("Please use a base between 2 and 36.")
    except ValueError as error:
        print(error)
        print('The input number does not exist in the input base.')
        return None
    else:
        out = ''
        while num > 0:
            if num < output_base:
                out = conversion[num] + out
                num = 0
            else:
                i = num % output_base
                num = num // output_base
                out = conversion[i] + out
        return out
