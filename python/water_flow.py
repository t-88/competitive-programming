#https://github.com/AlphaBitClub/alphabit-coding-challenge/blob/master/alphabit-coding-challenge-02/03_water_flow/water_flow.pdf


def calcTime(flow,bandwidth,delay):
    while(flow > 0):
        flow -= bandwidth
        delay += 1
    return delay     

flow = int(input("flow: "))
count = int(input("count: "))
bandWidths = input("bandWidths: ").split(" ")

delays = [0] 
delays.extend(input("delays: ").split(" "))

times = []
for i in range(count):
    times.append(calcTime(flow,int(bandWidths[i]),int(delays[i])))

print(times.index(min(times)))
