#Week 11
#Warm up
#FizzBuzz Plus
#Write fizzbuzz_plus(n) that returns a list of strings for the numbers 1 to n

def fizzbuzz_plus(n):
    res = []
    for i in range(1, n+1):
        temp = ""
        if i % 3 == 0: 
            temp += "Fizz"
        if i % 5 == 0: 
            temp += "Buzz"
        if i % 7 == 0: 
            temp += "Bazz"
        if len(temp)== 0:
            temp = str(i)
        res.append(temp)
            
    return res

print(fizzbuzz_plus(105))
