INCH = 2.546

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum+=num
    return sum

print("util", __name__)

if __name__ == "__main__":
    print("Hello util")
    print("~10 = ",calcsum(10))



