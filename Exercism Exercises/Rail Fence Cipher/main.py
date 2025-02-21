import re

def encode(message: str, rails: int):
    '''
    Take a message and a number of rails, and return an encoded message.
    Example:
    "Ride at dawn", 3
    R . . . A . . . W .
    . I . E . T . A . N
    . . D . . . D . . .
    Return "RAWIERANDD"
    '''
    if rails < 2:
        return 'Please use at least two rails.'
    #Remove punctuation and spacing, and get length.
    message = re.sub(r'[^A-Za-z0-9]', '', message).upper()

    encoded_array = ['' for rail in range(rails)]
    j = 0
    down = True
    for i in range(len(message)):
        encoded_array[j] += message[i]
        if j == rails - 1 and down == True:
            down = False
        if j == 0 and down == False:
            down = True
        if down:
            j += 1
        else:
            j -= 1
    encoded_message = ''.join(encoded_array)
    print(encoded_array)
    return encoded_message


def decode(encoded_message, rails):
    '''
    Take an encoded message and the number of rails used and decode it.
    '''
    #Recreate array(rails)
    decoded_array = ['' for rail in range(rails)]
    spacing = [rails * 2 - 2, 0]
    j, k, l = 0, 0, 0
    for i in range(len(encoded_message)):
        print('index: ', i, '  array:', j, '  spacing0: ', spacing[0], '  spacing1: ', spacing[1], '  place: ', k)
        decoded_array[j] += encoded_message[i]
        if spacing[l] != 0:
            k += spacing[l]
        else:
            k += spacing[0]
        if l == 0:
            l = 1
        else:
            l = 0
        if k > len(encoded_message) - 1:
            j += 1
            k = j
            l =0
            if j > rails / 2:
                spacing[0] += 2
                spacing[1] -= 2
            else:
                spacing[0] -= 2
                spacing[1] += 2

    #Iterate through rails, recreate message
    decoded_message = ''
    j = 0
    down = True
    for i in range(len(encoded_message)):
        letter = decoded_array[j][:1]
        decoded_array[j] = decoded_array[j][1:]
        decoded_message += letter
        if j == rails - 1 and down == True:
            down = False
        if j == 0 and down == False:
            down = True
        if down:
            j += 1
        else:
            j -= 1

    return decoded_message
