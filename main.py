print("---------- numero de discos ----------")


def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        print(source, helper, target)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
            print(source, helper, target)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        print(source, helper, target)


source = [5, 4, 3, 2, 1]
target = []
helper = []
hanoi(len(source), source, helper, target)

print(source, helper, target)
