# a = input().split(' ')
a = ["19B","2Tb","18Kb","10GB"  ]


mapped = {
    "b" : 1/8, 
    "B" :1 , 
    "KB": 2**10, 
    "MB": 2**20, 
    "GB": 2**30,
    "TB": 2**40, 
    "kB": 2**10, 
    "mB": 2**20, 
    "gB": 2**30,
    "tB": 2**40, 
    "Kb":  134217728/2**20,  
    "Mb": 134217728/2**10, 
    "Gb": 134217728,
    "Tb": 137438953472,
    "kb": 134217728/2**20,  
    "mb": 134217728/2**10, 
    "gb": 134217728,
    "tb": 137438953472

}


def function():
    k = [str(i) for i in range(10)]
    d = []
    for val in a:
        unit = val[-2:]
        if  unit[0] in k:
            unit = unit[1:]
        p  = int(val.replace(unit,''))
        if int(p * mapped[unit]) == p * mapped[unit]:
            d.append(int(p * mapped[unit]))
        else:
            d.append(p * mapped[unit])

    for i in range(len(d)):
        print(str(d[i]),end='')
        if i != len(d) - 1:
            print(', ',end='')

function()