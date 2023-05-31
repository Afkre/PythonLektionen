import re

# rgb(09,168,197)
# #09A8C5

def RGBToHex(usrInput):
    rgb = sanitizeRGB(usrInput)
    #print(rgb)
    if validateRGB(rgb):
        hex = calcHexValues(rgb)
        print(hex)
    else:
        print("Fehler")
        

def sanitizeRGB(usrInput):

    rgb = usrInput
    rgb.replace(' ', '')

    if rgb.startswith("rgb("):
       rgb = rgb[4:]

    if rgb.endswith(")"):
       rgb = rgb[0:-1]

    rgbList = rgb.split(',')
    
    return rgbList

def validateRGB(rgb):

    if len(rgb) < 3:
        return False

    for c in rgb:

        if re.search(r'[^0-9]', c) != None:
            return False
        
        if(int(c) < 0 or int(c) > 255):
            return False

    return True

def calcHexValues(rgb):

    hexTab = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    hex = "#"
    for i in range(3):
        value = int(rgb[i])
        hex += hexTab[value // 16]
        hex += hexTab[value % 16]

    return hex


RGBToHex("rgb(09,168,197)")



