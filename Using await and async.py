from collections import deque
from types import coroutine

friends = deque(('Rolf', 'George', 'Charlie', 'Jen', 'Anna'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        # priming stops here
        greeting = yield  # this yield is received from greet()
        print(f'{greeting} {friend}')


async def greet(g):
    await g # this doesn't finish until the co-routine 'g' has finished


greeter = greet(friend_upper())
greeter.send(None)  # primes generator
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')