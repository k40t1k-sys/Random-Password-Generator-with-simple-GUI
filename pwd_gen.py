import time

MAX_LEN = 32
MIN_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '&']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

def random():
    x = time.thread_time_ns()
    a = 8974556217
    c = 524556445
    m = 2**32
    x = (a*x + c) % m
    return x

def choice(seq):
    return seq[(random() % len(seq))]

def shuffle(arr, n):
    for i in range(n-1,0,-1): 

        j = random() % (i+1) 
   
        arr[i],arr[j] = arr[j],arr[i] 
    return arr

def gen_pwd():
    password = ''

    LIMIT = (random() % (MAX_LEN - MIN_LEN + 1)) + MIN_LEN

    temp_pass = choice(DIGITS) + choice(UPCASE_CHARACTERS) + choice(LOCASE_CHARACTERS) + choice(SYMBOLS)

    for i in range(LIMIT - 4):
        temp_pass = temp_pass + choice(COMBINED_LIST)

    array_pass = shuffle(list(temp_pass), len(temp_pass))

    for i in array_pass:
        password += i

    password = LOCASE_CHARACTERS[random() % len(LOCASE_CHARACTERS)] + password + UPCASE_CHARACTERS[random() % len(UPCASE_CHARACTERS)]

    return password