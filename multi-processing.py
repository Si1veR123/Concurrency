from multiprocessing import Process

def user_input():
    input('Input: ')

def complex_calc():
    var = [x ** 2 for x in range(20000000)]

process = Process(target=complex_calc)
process2 = Process(target=user_input)

process.start()
process2.start()

process.join()
process2.join()

"""
This may cause errors as the processes are on different cpu cores and one may not have access for the terminal for input
"""