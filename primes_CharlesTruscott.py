# -*- coding: utf-8 -*-
"""
HOW MANY PRIMES ARE IN EACH 1000 NUMBERS UP TO A MILLION?
Charles Thomas Wallace Truscott

"""

def return_primes():
    primes = []
    primesCount = []
    count = 0
    low = 2
    for q in range(0, 1000000, 1000):
        high = q
        print("q: {} ".format(q))
        for n in range(high, low, -1):
            for x in range(2, n, 1):
                if n % x == 0:
                    continue
                elif (n % x != 0) and (n in primes) == False:
                    count += 1
                    primes.append(n)
            if high > 1000:
                low = high - 1000
        primesCount.append((count, high))
        print(primesCount)
#wrong: print("There are {} number of primes in the first {} natural numbers".format(primesCount[0], primesCount[1]))
        count = 0

                
    print(primesCount)

def main():
    return_primes()
    
if __name__ == "__main__": main()


"""
Almost surely a doubly exponentially costly time scale to this algorithm
Works better to simply have a True False value for the prime check instead of adding to a list and complex logical operators and operands
"""
"""
runfile('C:/Users/17/Downloads/primes_CharlesTruscott.py', wdir='C:/Users/17/Downloads')
q: 0 
[(0, 0)]
q: 1000 
[(0, 0), (998, 1000)]
q: 2000 
[(0, 0), (998, 1000), (1000, 2000)]
q: 3000 

Are there 998 primes in the first 1000 numbers and 1000 primes between 1000 and 2000?

Minutes later and microprocessor overheating with fans running ... 3.0Ghz Quad Core Alienware 17 R2 32GB RAM DDR3 

runcell(0, 'C:/Users/17/Downloads/primes_CharlesTruscott.py')
q: 0 
[(0, 0)]
q: 1000 
[(0, 0), (998, 1000)]
q: 2000 
[(0, 0), (998, 1000), (1000, 2000)]
q: 3000 
[(0, 0), (998, 1000), (1000, 2000), (1000, 3000)]
q: 4000 



"""