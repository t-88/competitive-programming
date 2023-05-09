#heap algorithm

def generate_all_permutations(k,arr):
    if k == 1: 
        print(arr)
        return arr
    else:
        generate_all_permutations(k - 1,arr)
        for i in range(0,k):
            if k % 2 == 0:
                arr[i] , arr[k - 1] =  arr[k - 1] , arr[i] 
            else:
                arr[0] , arr[k - 1] =  arr[k - 1] , arr[0] 
            generate_all_permutations(k - 1,arr)

arr = ['a','b','c']
generate_all_permutations(3,arr)

