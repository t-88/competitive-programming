import sys

cases_count = int(sys.stdin.readline())
cases = []
for _ in range(cases_count):
    c = []
    for _ in range(4):
        c.append(sys.stdin.readline().strip())
    cases.append(c)

def check_password(s,l,u):
    if len(l) > 0:
        for x in range(int(l[0]),int(u[0]) + 1):
            find_once = s.find(str(x))
            if find_once == -1:
                return "YES"
            if check_password(s[find_once+1:],l[1:],u[1:]) == "YES":
                return "YES"
        

    return "NO" 

for c in cases:
    print(check_password(c[0],c[2],c[3]))
