# Queue
# back/rear/tail  Front/Head
# First In First Out(FIFO)
# Last In Last Out(LILO)

# enqueue 
# dequeue

# isFull
# isEmpty

# Queue Implementation using list
queue = []
def enqueue():
    element = input("Enter the Element: ")
    queue.append(element)
    print(queue)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        removed_element = queue.pop(0)
        print("Removed Element", removed_element)

def display_queue():
    print("Queue: ", queue)

while True:
    print("Select the operation: 1. Add 2. Remove 3. Show 4. Quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display_queue()
    else:
        break