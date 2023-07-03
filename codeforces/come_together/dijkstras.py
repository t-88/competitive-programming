area = {
            "A" : [["B",2],["D",8]], 
            "B" : [["A",2],["E",6],["D",5]], 
            "D" : [["A",8],["F",2],["E",3]], 
            "E" : [["B",6],["F",1],["D",3],["C",9]], 
            "C" : [["F",3],["E",9]], 
            "F" : [["D",2],["E",1],["C",3]], 

       }

visted = []
unvisted = ["A","B","C","D","E","F"]
path = {
            "A" : ["",0],
            "B" : ["",float("inf")],
            "C" : ["",float("inf")],
            "D" : ["",float("inf")],
            "E" : ["",float("inf")],
            "F" : ["",float("inf")],
       }
curr_node = "A"
dis = 0
while len(unvisted):
    nodes = area[curr_node]
    for node in nodes:
        if path[node[0]][1] > node[1] + dis:
            path[node[0]][0] = curr_node
            path[node[0]][1] = node[1] + dis
    
    unvisted.pop(unvisted.index(curr_node))
    curr_min = float("inf")
    for node in unvisted:
        if curr_min > path[node][1]:
            curr_node = node
            curr_min = path[node][1]

    dis = path[curr_node][1]

print(path)
