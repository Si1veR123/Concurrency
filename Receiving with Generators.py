from collections import deque

friends = deque(('Rolf', 'George', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        # priming stops here
        greeting = yield # this yield is received from greet()
        print(f'{greeting} {friend}')


def greet(g):
    yield from g # whatever is sent to this generator, gets passed to friend_upper()

    """
    SAME AS
    
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)
    """


greeter = greet(friend_upper())
greeter.send(None) # primes generator
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')