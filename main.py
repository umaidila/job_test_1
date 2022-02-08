import fileinput
import sys
import threading
import time
import random
from hashlib import sha256

messages = ['Аксеныч Семен Русланович', 'Стажёр-программист Python', '50-70 тыс руб']


def showMsg(n):
    sleep = random.randrange(1, 5)
    time.sleep(sleep)
    print(messages[n], sleep)

threads = []
for i in range(3):
    thread = threading.Thread(target=showMsg,args=(i,))
    threads.append(thread)

s = input("Enter string: ")

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print(sha256(s.encode('utf-8')).hexdigest())
