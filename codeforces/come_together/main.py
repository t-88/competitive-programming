import sys

cases_count = int(sys.stdin.readline())
cases = []

for _ in range(cases_count):
    test_case = []
    for _ in range(3):
        test_case.append(tuple(map(int,sys.stdin.readline().split(" "))))
    cases.append(test_case)

def count_shared_cells(cells):
    A , B , C = cells[0] , cells[1] , cells[2]
    if A[0] <= max(B[0],C[0]) and A[0] >= min(B[0],C[0]) and  A[1] <= max(B[1],C[1]) and A[1] >= min(B[1],C[1]):
        return 1

    AB = abs(A[0] - B[0]) +  abs(A[1] - B[1]) + 1
    AC = abs(A[0] - C[0]) +  abs(A[1] - C[1]) + 1
    BC = abs(B[0] - C[0]) +  abs(B[1] - C[1]) + 1
    

    return int((AB + AC - BC - 1) / 2) + 1  
    
    
for _case in cases:
    print(count_shared_cells(_case))


