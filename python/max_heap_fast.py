#https://www.youtube.com/watch?v=kQDxmjfkIKY&ab_channel=CodDevX

max_heap = [0,17,5,13,1,4,2,6]

#i = 4      => get 5
#i / 2      => parent(i) 
#i * 2      => left(i)
#i * 2 + 1  => right(i)

#push for insert
#peek get max
#pop  remove max

def float_up(heap,index):
    parent = index // 2
    if heap[parent] < heap[index] and index > 1:
        heap[index] , heap[parent] = heap[parent] , heap[index]
        float_up(heap,parent)


def bubble_down(heap,index):
    left = 2 * index
    right = left + 1
    i = index


    if left < len(heap) and heap[i] < heap[left]:
        i  = left
    if right < len(heap) and heap[i] < heap[right]:
        i  = right

    if index != i:
        heap[index] , heap[i] = heap[i] , heap[index]
        bubble_down(heap,i)

def peek(heap):
    if heap[1]:
        return heap[1]
    else:
        return False


def pop(heap):
    if len(heap) == 2: 
        max_value = heap.pop()
    elif len(heap) > 2:
        #swap 
        heap[1] , heap[len(heap) - 1] = heap[len(heap) - 1] , heap[1] 
        max_value = heap.pop()
        bubble_down(heap,1)
    else:
        max_value = False
    
    return max_value
       
print(pop(max_heap))
print(pop(max_heap))
print(pop(max_heap))
print(pop(max_heap))
print(pop(max_heap))
print(pop(max_heap))
print(pop(max_heap))
print(pop(max_heap))



