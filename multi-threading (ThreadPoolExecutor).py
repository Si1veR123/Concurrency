from concurrent.futures import ThreadPoolExecutor

def user_input():
    input('Input: ')

def complex_calc():
    var = [x ** 2 for x in range(20000000)]

# using a pool means that threads are not allocated a function when created
with ThreadPoolExecutor(max_workers = 2) as pool:
    pool.submit(complex_calc)
    pool.submit(user_input)
    pool.submit(complex_calc)
    print('done')