queue = ['A', 'B', 'C']
queue.append('D')
queue.append('E')
print(queue) #Output ['A', 'B', 'C', 'D', 'E']

print(queue.pop(0)) #Output A
print(queue) #Output ['B', 'C', 'D', 'E']

print(queue.pop(0)) #Output B
print(queue) #Output ['C', 'D', 'E']