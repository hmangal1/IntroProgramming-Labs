def main():
    numerator=4
    denominator=1
    n=int(input("Enter the number of terms to sum. "))
    pi=float(0)
    for i in range(n):
        pi = ( float(numerator/denominator) ) -( float(numerator/(denominator+2))) + ( float(numerator/(denominator+4)) )
        denominator=denominator+4
    print("Output is",pi)
main()                                                                           
                                                                          
