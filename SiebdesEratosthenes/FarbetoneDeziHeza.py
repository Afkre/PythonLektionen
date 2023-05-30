import re

#   #09A8C5
#   rgb(09,168,197)

#hexInput =input ("Bitte Hex-Wert eingeben: ")

hexInput = " #09A 8c5    "

def sanitizeHex(usrInput):
    hex= usrInput
    hex = hex.replace(' ','')
    if hex.startswith("#"):
       hex = hex[1:]
    hex = hex.upper()
       
    return hex

hex = sanitizeHex(hexInput)

print(hex)

def validateHex(hex):
    if len(hex) != 6 :
        return False
    
    if re.search(r'[^0-9A-F]', hex) != None :
        return False
    
    return True

def calcRGBValues(hex):
    
    hexTab = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')     
    hexList = [hex[:2], hex[2:4], hex[4:]]
    rgbList = []
    
    for i in range(3):
        rgbList.append(hexTab.index(hexList[i][0]) * 16 + hexTab.index(hexList[i][1]))
        
    return rgbList

def formatOutput(rgb):
    output = "rgb({0}, {1}, {2})".format(rgb[0], rgb[1], rgb[2])
    
if validateHex(hex):
    
    rgb = calcRGBValues(hex)
    
    output = "rgb({0}, {1}, {2})".format(rgb[0], rgb[1], rgb[2])
    
    print(output)
    
    
    
    #hexTab = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    
    #r = hex[:2]
    #g = hex[2:4]
    #b = hex[4:]
    
    #hexList = [hex[:2], hex[2:4], hex[4:]]
    #rgbList = []
    
    #for i in range(3):
    #    rgbList.append(hexTab.index(hexList[i][0]) * 16 + hexTab.index(hexList[i][1]))
        
    
    
    #rD = hexTab.index(hexList[0][0]) * 16 + hexTab.index(hexList[1][0]) * 1
    #gD = hexTab.index(hexList[1][0]) * 16 + hexTab.index(hexList[1][1]) * 1
    #bD = hexTab.index(hexList[2][0]) * 16 + hexTab.index(hexList[2][1]) * 1
    
    #print(rD)
    #print(gD)
    #print(bD)
    
    #print(rgbList)

