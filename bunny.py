s = 'bcdbcdbcdbcd'
t = 'bcdbcd'

def findSmallestDivisor(s, t):
    # Write your code here
    fits = False
    concat = t
    i=1
    while len(concat)<=len(s):
        if concat!=s:
            i+=1
            concat = t * i
            print(concat)
            print(len(concat))
        else:
            print(concat)
            print(len(concat))
            fits = True
            break
    if not fits:
        return -1
    for i in range(1,len(t)+1):
        if (t[:i]*(len(t)//i)) == t:
            return i
