def egcd(a, b):

    if a == 0:
        return
    if b == 0:
        return
        
    quotient = a//b
    remainder = a%b

    print(f"{a} = {quotient}*{b} + {remainder}")
    egcd(b, remainder)

if __name__=="__main__":
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    egcd(a, b)
