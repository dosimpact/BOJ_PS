def getCount(M,data):
    count=0
    for y in range(len(data)):
        if sum(data[y])==M:
            count+=1
    return count

def find(N,M,K,data):
    count=0
    if(K==0):
        return getCount(M,data)
    for x in range(len(data[0])):
        for y in range(len(data)):
            if(data[y][x]==1): data[y][x]=0
            else: data[y][x]=1
        count=max(count,find(N,M,K-1,data))
        for y in range(len(data)):
            if(data[y][x]==1): data[y][x]=0
            else: data[y][x]=1

    return count

def main0():
    N,M=map(int,input().split())
    data=[]
    for _ in range(N):
        data.append(list(map(int,list(input()))))
    K=int(input())

    print(find(N,M,K,data))

if __name__ == "__main__":
main0()