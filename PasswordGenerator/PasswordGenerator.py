import random

def generate(usrLength = 8):
    randint = random.randint(33,126)

    pw = ""
    gb = False;
    kb = False;
    zi = False;
    so = False;

    length = usrLength + 1
    
    while gb == False or kb == False or zi == False or so == False:
          
        pw = ""
        gb = False;
        kb = False;
        zi = False;
        so = False; 
        
        for i in range(1,length):
            randint = random.randint(33,126)
            pw += chr(randint)

            if randint >= 65 and randint <= 90:
                gb = True
            elif randint >= 97 and randint <= 122:
                kb = True
            elif randint >= 48 and randint <= 57:
                zi = True
            else:
                so = True

    return pw

#print(pw)
