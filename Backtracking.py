#PYTHON 
n,car_number = list(map(int,input().split()))
cost = []
for i in range(n+1):
    cost.append(list(map(int, input().split())))
global_cost_min = cost[0][1]
for i in range(len(cost)):
    for j in range(i):
        if i != j:
            if cost[i][j] < global_cost_min:
                global_cost_min = cost[i][j]

f = [0] * car_number
f_min = 999
global_min = 999
global_min_result = [None] * car_number
A=[i for i in range(1,n+1)]
visited = [False] * n                               #Check if the city was visited
picked = [list() for i in range(car_number)]        #The chosen paths of each car
for i in range(car_number):
    picked[i].append(0)


k_pick = list()

def solution(x,):
    global f_min
    global global_min_result
    path_list = list(f[i]  for i in range(car_number))
    if max(path_list)<f_min:
        f_min = max(path_list)
        global_min_result = [list(p) for p in x]
def Cluster(i,j, ):
    global f
    global f_min
    for s in A:
        if visited[s-1] == False:
            picked[i].append(s)
            f[i] += cost[picked[i][-2]][picked[i][-1]]
            visited[s-1] = True
            if len(picked[i])==k_pick[i]+1 and i < car_number-1:
                Cluster(i+1,0)
            elif len(picked[car_number-1]) == k_pick[car_number-1]+1 and i == car_number-1:
                solution(picked)
            else:
                g = f[i] + global_cost_min*(len(picked[i])-s)
                if g<f_min:
                    Cluster(i,j+1)
            visited[s-1] = False
            f[i] -= cost[picked[i][-2]][picked[i][-1]]
            picked[i].pop()
def Try(i):
    if  i == car_number-1:
        min = n - sum(k_pick)
        max = n - sum(k_pick)
    else:
        min = 1
        max = n - sum(k_pick) - (car_number-1-i)
    for v in range(min,max+1):
        k_pick.append(v)
        if i == car_number - 1:
            Cluster(0,0)
        else: 
            Try(i+1)
        k_pick.pop()
        
Try(0)
print(car_number)
for i in range(len(global_min_result)):
    print(len(global_min_result[i]))
    for j in global_min_result[i]:
        print(j, end = ' ')
    print()
