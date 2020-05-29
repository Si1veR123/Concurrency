from threading import Thread

def user_input():
    input('Input: ')

def complex_calc():
    [x**2 for x in range(20000000)]


thread1 = Thread(target=user_input)
thread2 = Thread(target=complex_calc)

thread1.start()
thread2.start()

thread1.join()
thread2.join() # tells main thread to wait until these have finished
