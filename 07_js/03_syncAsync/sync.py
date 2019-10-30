# Python: Blocking

from time import sleep

# print('hi')
# sleep(3)
# print('bye')


def sleep_3s():
    sleep(3)
    print('Wake Up!')


print('Start sleeping')
sleep_3s()
print('End of program')