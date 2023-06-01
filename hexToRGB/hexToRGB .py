import re

# #09A8C5
# rgb(09,168,197)

#hexInput = input("Bitte Hex-Wert eingeben: ")
hexInput = " #09A 8c5    "

def hexToRGB():
    
    #hexInput = input("Bitte Hex-Wert eingeben: ")
    hexInput = " #09A 8c5    "

    hex = sanitizeHex(hexInput)

    if validateHex(hex):

        rgb = calcRGBValues(hex)
        output = formatOutput(rgb)
        print(output)
        

def sanitizeHex(usrInput):
    hex = usrInput
    hex = hex.replace(' ', '')    
    if hex.startswith("#"):
        hex = hex[1:]
    hex = hex.upper()

    return hex

def validateHex(hex):

    if len(hex) != 6:
        return False

    if re.search(r'[^0-9A-F]', hex) != None:
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
    return "rgb({0},{1},{2})".format(rgb[0],rgb[1],rgb[2])


hexToRGB()

    
