
#12 => 21
#123 => 132; #2555 => 5255


def convIntArr(number):
    return [i for i in str(number)]
def convArrInt(number):
    if number:
        return int(''.join(number))
    else:
        return 0

def bigger_closest_number(number):
    number = convIntArr(number)    
    curr = 0
    while curr < len(number) - 1:
        a = number[len(number) - curr - 1]
        b = number[len(number) - curr - 2]
        # if a > b:


        # print(b,a)

        curr += 1


n = "255"
bigger_closest_number(n)