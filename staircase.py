def staircase(n):
    # The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of n=6.
    symbols=0
    image="#"
    for i in range(n):
        symbols=i+1
        spaces=symbols*image
        print(spaces.rjust(n))


or

def staircase(n):
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)