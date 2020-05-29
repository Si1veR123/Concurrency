from threading import Thread
from queue import Queue

q = Queue()
q_print = Queue()


def increment(): # this function gets a list of nums from 'q', adds 1 to each and put new list in q_print
    while True:
        prev_num = q.get()
        new_nums = []
        for num in prev_num:
            new_nums.append(num+1)
        q_print.put(new_nums)
        q.task_done()


def print_num(): # this function gets a list of nums from q_print and prints it
    while True:
        num = q_print.get()
        print(num)
        q_print.task_done()

# daemon means that when the main thread is finished, these threads quit too.
# if this isn't added, program will not stop automatically as both functions are infinite loops
increment_thread = Thread(target=increment, daemon=True)
print_thread = Thread(target=print_num, daemon=True)

q.put([1, 2, 3, 4, 5, 6, 7, 8, 9])

increment_thread.start()
print_thread.start()

q.join()
q_print.join()