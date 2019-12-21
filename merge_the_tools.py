def del_char(t,index):
    s1=index>0 and t[:index] or ""
    s2=index<len(t)-1 and t[index+1:] or ""
    return s1+s2

def get_u_from_t(t):
    res=t
    for i in reversed(range(1,len(t))):
        if t[i] in t[:i]:
            t=del_char(t,i)
    return t

def get_subsequences(string,k):
    subseq_count=int(len(string) / k)
    l=[]
    for i in range(0,len(string),k):
       l.append(string[i:i+k])
    return l
def merge_the_tools(string, k):
    l=get_subsequences(string,k)
    for i in range(len(l)):
       print(get_u_from_t(l[i]))

if __name__=='__main__':
    string,k=input(),int(input())
    merge_the_tools(string,k)