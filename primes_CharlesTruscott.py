# -*- coding: utf-8 -*-
"""
HOW MANY PRIMES ARE IN EACH 1000 NUMBERS UP TO A MILLION?
Charles Thomas Wallace Truscott

"""

def return_primes():
    primes = []
    counts = []
    divisorFound = False
    count = 0
    for q in range(2, 1000000, 1000):
        high = q
        if q == 1000:
            low = 2
        else:
            low = high - 1000
        for n in range(low, high, 1):
            for x in range(2, n, 1):
                if n % x == 0:
                    divisorFound = True
            if divisorFound == False:
                count += 1
            divisorFound = False
        print("There are {} prime numbers between {} and {}".format(count, high, high - 1000))
        counts.append((high, count))
        count = 0
    print(counts)
def main():
    return_primes()
    
if __name__ == "__main__": main()

"""
runfile('C:/Users/17/Downloads/primes_CharlesTruscott.py', wdir='C:/Users/17/Downloads')
There are 1000 prime numbers between 2 and -998
There are 168 prime numbers between 1002 and 2
There are 135 prime numbers between 2002 and 1002
There are 128 prime numbers between 3002 and 2002
There are 120 prime numbers between 4002 and 3002
There are 118 prime numbers between 5002 and 4002
There are 114 prime numbers between 6002 and 5002
There are 118 prime numbers between 7002 and 6002
There are 106 prime numbers between 8002 and 7002
There are 111 prime numbers between 9002 and 8002
There are 111 prime numbers between 10002 and 9002
There are 106 prime numbers between 11002 and 10002
There are 103 prime numbers between 12002 and 11002
There are 110 prime numbers between 13002 and 12002
There are 104 prime numbers between 14002 and 13002
There are 102 prime numbers between 15002 and 14002
There are 109 prime numbers between 16002 and 15002
There are 97 prime numbers between 17002 and 16002
There are 104 prime numbers between 18002 and 17002
There are 95 prime numbers between 19002 and 18002
There are 103 prime numbers between 20002 and 19002
There are 99 prime numbers between 21002 and 20002
There are 103 prime numbers between 22002 and 21002
There are 100 prime numbers between 23002 and 22002
There are 105 prime numbers between 24002 and 23002
There are 93 prime numbers between 25002 and 24002
There are 98 prime numbers between 26002 and 25002
There are 101 prime numbers between 27002 and 26002
There are 95 prime numbers between 28002 and 27002
There are 97 prime numbers between 29002 and 28002
There are 92 prime numbers between 30002 and 29002
There are 95 prime numbers between 31002 and 30002
There are 92 prime numbers between 32002 and 31002
There are 106 prime numbers between 33002 and 32002
There are 100 prime numbers between 34002 and 33002
There are 94 prime numbers between 35002 and 34002
There are 92 prime numbers between 36002 and 35002
There are 99 prime numbers between 37002 and 36002
There are 94 prime numbers between 38002 and 37002
There are 90 prime numbers between 39002 and 38002
There are 96 prime numbers between 40002 and 39002
There are 88 prime numbers between 41002 and 40002
There are 101 prime numbers between 42002 and 41002
There are 102 prime numbers between 43002 and 42002
There are 85 prime numbers between 44002 and 43002
There are 96 prime numbers between 45002 and 44002
There are 86 prime numbers between 46002 and 45002
There are 90 prime numbers between 47002 and 46002
There are 95 prime numbers between 48002 and 47002
There are 89 prime numbers between 49002 and 48002
There are 98 prime numbers between 50002 and 49002
"""

"""
runfile('C:/Users/17/Downloads/primes_CharlesTruscott.py', wdir='C:/Users/17/Downloads')
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997] 168
"""

"""


runfile('C:/Users/17/Downloads/primes_CharlesTruscott.py', wdir='C:/Users/17/Downloads')
high: 2 count: 1000
high: 1002 count: 168
high: 2002 count: 135
high: 3002 count: 128
high: 4002 count: 120
high: 5002 count: 118
high: 6002 count: 114
high: 7002 count: 118
high: 8002 count: 106
high: 9002 count: 111
high: 10002 count: 111
high: 11002 count: 106
high: 12002 count: 103
high: 13002 count: 110
high: 14002 count: 104
high: 15002 count: 102
high: 16002 count: 109
high: 17002 count: 97
high: 18002 count: 104
high: 19002 count: 95
high: 20002 count: 103
high: 21002 count: 99
high: 22002 count: 103
high: 23002 count: 100
high: 24002 count: 105

There are 1000 prime numbers between 2 and -998
There are 168 prime numbers between 1002 and 2
There are 135 prime numbers between 2002 and 1002
There are 128 prime numbers between 3002 and 2002
There are 120 prime numbers between 4002 and 3002
There are 118 prime numbers between 5002 and 4002
There are 114 prime numbers between 6002 and 5002
There are 118 prime numbers between 7002 and 6002
There are 106 prime numbers between 8002 and 7002
There are 111 prime numbers between 9002 and 8002
There are 111 prime numbers between 10002 and 9002
There are 106 prime numbers between 11002 and 10002
There are 103 prime numbers between 12002 and 11002
There are 110 prime numbers between 13002 and 12002
There are 104 prime numbers between 14002 and 13002
There are 102 prime numbers between 15002 and 14002
There are 109 prime numbers between 16002 and 15002
There are 97 prime numbers between 17002 and 16002



"""

