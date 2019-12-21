if __name__=='__main__':
    n,m=input().split()
    set_x = input().split()
    set_a = set(input().split())
    set_b = set(input().split())
    print(sum([(i in set_a) - (i in set_b) for i in set_x]))
