from queue import Queue

my_queue = Queue()

print(f'Queue top = {my_queue.front()}')
print(f'Queue size = {my_queue.size()}')
print(f'If queue is empty = {my_queue.empty()}\n')

n = int(input("How many countries you are going to enter: "))
for i in range(1,n+1):
    my_queue.push_back(input(f"{i}: "))

print(f'Queue top = {my_queue.front()}')
print(f'Queue size = {my_queue.size()}')
print(f'If queue is empty = {my_queue.empty()}\n')

print('\nQueue elements\n')

for student in my_queue.iter():
    print(student)

print('\nPop an element\n')
print(my_queue.pop())

print('\nQueue elements\n')

for student in my_queue.iter():
    print(student)