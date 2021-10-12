top_dfs=[]
vis=[]
graph=[]


def bfs(V):
    values = [0]*(V)
    
    for i in range(len(graph)):
        for j in graph[i]:
            values[j] += 1

    queue = []
    for i in range(V):
        if values[i] == 0:
            queue.append(i)

    cnt = 0
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for i in graph[u]:
            values[i] -= 1
            if values[i] == 0:
                queue.append(i)
        cnt += 1
    if cnt != V:
        print("They cannot be studied because of interdependancy")
        return []
    else :
        return order

def dfs(p):
    vis[p] = True
    for i in graph[p]:
        if vis[i] == True:
            return False
        if not dfs(i):
            return False
    top_dfs.append(p)
    return True

def main():
    x = int(input("Enter the number of subects in your course: "))
    y = dict()
    mapp=[]
    for i in range(x):
        z = input("Enter the name of your course: ")
        y[z] = i;
        vis.append(False)
        graph.append([])
        mapp.append(z)
    num = int(input("Enter the number of prerequisites pair: "))
    print("Enter the prerequisite in the form a is a prerequisite to b")
    for i in range(num):
        a = input("subject1: ")
        b = input("subject2: ")
        c = y[a]
        d = y[b]
        graph[c].append(d)
        
        
    ans = bfs(x)
    for i in ans:
        print(mapp[i],end=" ")
    print("\n")
    
    
    for i in  range(x):
        if not vis[i]:
            #print(i)
            result = dfs(i)

            if not result:
                print("They cannot be studied because of interdependancy")
                return
                
    top_dfs.reverse()
    for i in top_dfs:
        print(mapp[i],end=" ")
    print("\n")
# if _name_ == '_main_' :
main()