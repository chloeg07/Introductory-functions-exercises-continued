def Add_Two  (a,b):
    total = a + b
    return total

def Un_Adder (a):
    wordnew = "un" + a
    return wordnew

def Palidndrome(a):
    F = list(a)
    
    G = list(a)
    F.reverse()
    if G == F:
            return "This word is a Palidndrome."
    else:
            return "This word is not a Palidndrome."
        
def rah:
    A = [1,2,3,4,8,10,12,13,15,17]
    Oddlist = []
    Evenlist = []
    
for i in A:
    if i%2 == 0:
    