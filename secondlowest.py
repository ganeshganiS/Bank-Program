marksheet=[]
scoresheet=[]
n=int(input("Enter a number"))
if __name__ == '__main__':
    for i in range(n):
        name = input("ENter a name")
        marks = int(input("Enter the marks"))
        score = float(marks)
        marksheet+=[[name,score]]
        scoresheet+=[score]
    x=sorted(set(scoresheet))[1]
    print(x)
    for n,s in sorted(marksheet):
        if s==x:
            print(n)
