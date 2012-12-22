###Prime Number Game###
#All age
#2~1000 players
#Playing prime number range 2~100000

##System Recommendations
#Python 2.7.1

from collections import defaultdict
##############Players##############
def numbers():
    while True:
        try:
            num = int(raw_input("Enter number of players:"))
            if num < 2 or num > 1000:
                raise ValueError
            print "OK! " + str(num) + " players."
            break
        except ValueError:
            print "Oops!  That was no valid input.Try again... Only number is acceptable(between 2 and 1000)."
        
    return num


def name(num):
    nlist = []
    checker = 0
    while checker < num:
        while True:
            try:
                name = raw_input("Enter name of player No." + str(checker+1) + ":")
                
                if name in nlist or name =="" or len(name) > 24:
                    raise ValueError
                print name
                break
            except ValueError:
                print "Oops! It is not possible to use same name,blank and over 24 characters. Try again..."
                
        nlist.append(name)
        checker += 1
        
    return nlist
##############Players##############

##############Prime_numbers##############
def eratosthenes(minimum, upper):
    tlist = [2]
    slist = range(3, upper+1,2)
    t = 0
    while t*t < upper:
        prime = slist[0]
        tlist.append(prime)
        for s in slist:
            if s%prime == 0:
                slist.remove(s)
            else:
                pass  
        t = tlist[-1]
    else:
        elist = tlist + slist
        plist = [e for e in elist if e > minimum-1] 
        
    return plist


def minimum():
    while True:
        try:
            num = int(raw_input("Enter minimum range:"))
            if num < 2 or num >99990:
                raise ValueError
            print num
            break
        except ValueError:
            print "Oops!  That was no valid input.Try again... Only number is acceptable (between 2 and 99,990)."
    
    return num


def prime_numbers(minimum):
    while True:
        try:
            upper = int(raw_input("Enter upper range:"))
            if upper <= minimum or upper >100000:
                raise ValueError
            #call eratosthenes
            plist = eratosthenes(minimum, upper)
            if not plist:
                raise IndexError
            print upper
            break
        except ValueError:
            print "Oops!  That was no valid input.Try again... Only number is acceptable (more than " + str(minimum) +", max is 100,000)."
        except IndexError:
            print "Oops! There is no prime number (between " + str(minimum) +" and " +str(upper) +").Try again... "
        except OverflowError:
            print "Oops! It seems lots of calculation. Enter smaller number."
        
    return plist, minimum, upper
##############Prime_numbers##############

##############Main##############
def primes(minimum, upper):
    while True:
        try:
            num = int(raw_input("Enter prime number:"))
            if num < minimum or num > upper:
                raise ValueError
            print num
            break
        except ValueError:
            print "Oops!  That was no valid input.Try again... Only number is acceptable (between " + str(minimum) +" and " +str(upper) +")."
    
    return num


def result(pdict):
    result = sorted(pdict.items(), key=lambda x:(len(x[1]),x[1]), reverse=True) 
    winner = result[0][0]
    print ""
    raw_input("Congratulation! You guys got all prime numbers! Winner is...")
    print winner
    print ""
    raw_input("All results below. Press enter.")
    print "name--prime numbers" 
    for n, l in result:
        print  str(n) +"--" +str(l)
            
            
def noresult(pdict,nlist):
    nolist = []
    for n in nlist:
        checker = pdict.has_key(n)
        if checker != True:
            nolist.append(n)
            
    for n2 in nolist:
        print str(n2) + "--" + "[Nothing]"
            
            
def main(nlist, p):
    plist = p[0]
    minimum = p[1]
    upper = p[2]
    pdict = defaultdict(list)
    clist = []
    while plist:
        for n in nlist:           
            rest_primes = len(plist)
            print n + ", your turn!"
            print "We have " + str(rest_primes) + " more left."
            # Call primes
            prime = primes(minimum, upper)       
            if prime in plist:
                pdict[n].append(prime)
                pdict[n].sort(reverse=True)
                clist.append(prime)
                plist.remove(prime)
                print "Nice!(^ ^)"
                if not plist:
                    break
            elif prime in clist:
                print "Already taken(- -)."    
            else:
                print "No(> <)."
            print ""
              
    else:
        #Call result
        result(pdict)
        #Call noresult
        noresult(pdict,nlist)
##############Main##############

print "---Prime Number Game---"
print "All age"
print "2~1000 players"
print "Playing prime number range 2~100000"

print ""
print "--Rule--"
print "1.Take prime number from designated range by rotation."
print "2.The player who gets the most prime numbers becomes the winner."
print "(If two more players get the most, the player who gets highest prime number becomes the winner.)"

print ""
print "--Settings--"
nlist = name(numbers())
print "Designate playing range."
p = prime_numbers(minimum())

raw_input("Now we have done settings. Let's start! Press Enter.")
main(nlist, p)
    
