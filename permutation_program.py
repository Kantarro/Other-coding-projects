import random

def main():
    L = ["a","b","c"]

    #to find the factorial 
    x = 1
    for i in range(1,len(L)+1):
        x*=i
    Perm = []
    while len(Perm) != x:               # x now equals len(L) factorial
        Q = random.sample(L,len(L))     # a list of one permutation
        if Q not in Perm:   
            Perm.append(Q)              # keep appending until len(Perm) = x
            
    for element in Perm:
        print("-".join(element))

    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    re_ask = True
    while re_ask:
        if lower_bound > upper_bound:
            upper_bound = int(input("Enter the upper bound: "))
        else:
            re_ask = False
    print(random.randint(lower_bound, upper_bound))


main()
