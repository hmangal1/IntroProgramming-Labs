n=int(input("Enter a number after 0."))

def main():
    prevNum=1
    dubPrevNum=1
    currentNum=prevNum+dubPrevNum
    if (n==1):
        print("The",n,"term of the fibonacci sequence is",dubPrevNum)
    if (n==2):
        print("The",n,"term of the fibonacci sequence is",prevNum)
    if (n==3):
        print("The",n,"term of the fibonacci sequence is",currentNum)
    for i in range(n-3):
        if(n>3):
            dubPrevNum=prevNum
            prevNum=currentNum
            currentNum=dubPrevNum+prevNum
    print("The",n,"term of the fibonacci sequence is",currentNum)
    
main()
        
        
    
        
        
    
