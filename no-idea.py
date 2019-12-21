if __name__=='__main__':
    n,m=(map(int,input().split()))
    set_x = list(map(int, input().split()))
    set_a = list(map(int, input().split()))
    set_b = list(map(int, input().split()))
    set_x_a = (i  for i in set_x if i in set_a)
    set_x_b = (i for i in set_x if i in set_b)
    hp,up=0,0
    for i in set_x_a:
        hp+=1
    for i in set_x_b:
        up+=1
    print(hp- up)
