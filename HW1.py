#HW2 _ Part 1

import queue
import time
import random
import sys


request_queue = queue.Queue()
request_number = 0

def generate_request():
    global request_number
    request_number += 1
    request_queue.put(request_number)
    print(f'Нова заявка створена: {request_number}')


def process_request():
    if not request_queue.empty():
        request_number = request_queue.get()
        print(f'Заявка {request_number} обробляється...')
        time.sleep(2)
        print(f'Заявка {request_number} успішно оброблена')
    else:
        print('Черга порожня')

try:
    while request_number < 20:
        generate_request() 
        process_request()
        time.sleep(random.randint(1, 3))
except KeyboardInterrupt:
    print("Програма припинена користувачем.") # Комбінація ctrl + c зупиняє программу
    sys.exit(0)
    
    



#HW2 _ Part 2

# from collections import deque

# def is_palindrome(input_string):
#     input_string = input_string.lower().replace(" ", "")
    
#     symbols = (',', '.', '!', '?', '-')

#     char_queue = deque()
#     for char in input_string:
#         char_queue.append(char)
#         for s in symbols:
#             if char == s:
#                 char_queue.pop()
#     print(char_queue)
    
#     while len(char_queue) > 1:
#         if char_queue.popleft() != char_queue.pop():
#             return False
    
#     return True

# input_str1 = "Cigar? Toss it in a can. It is ragic"     #False
# input_str2 = "Sit on a potato pan, Otis!"               #True
# print(is_palindrome(input_str1))
# print(is_palindrome(input_str2))
    
    