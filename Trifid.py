import numpy as np # type: ignore

encdec = input("Decrypt or Encrypt:")

def multilineinput():
    fullinput=""
    print("To exit multiline loop, enter the value ഗ")
    while True:
        line = input("Another: ")
        #print(line)
        if line == "ഗ":
            return list(fullinput)
        if fullinput == "":
            fullinput+=line
        else:
            fullinput+="\n"+line
        #print(fullinput)



if encdec == "E":
    plainlist=multilineinput()
    print(plainlist)
    ciphertext=""
    cipherlist=[]
elif encdec == "D":
    cipherlist=multilineinput()
    plaintext=""
    plainlist=[]
else:
    print("you mongrel")



xcoord = []
ycoord = []
zcoord = []

'''cipherkey = [
    [["A","B","C"],["D","E","F"],["G","H","I"]],
    [["J","K","L"],["M","_","N"],["O","P","Q"]],
    [["R","S","T"],["U","V","W"],["X","Y","Z"]]
    ] #[x][y][z]
mufucker=""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ♥"""
# !"#45·œ¹º»6789:;<=>?@ABCDE¶¼ʧȽ♥WXYZ[\]^_`abcg$%&'(HIJK½¿LMNS)*+,-./0123hijkpqrsOPQRtuvwxyz{|}~¡¢£¤lmno¥¦§¨def©ª«FGTUV¬¯°±²Þµ
mufuckerlist=list(mufucker) #♥♥♥♥
print(mufuckerlist)
print(len(mufucker))
'''
'''
[[[' ' '!' '"' '#' '$']
  ['%' '&' "'" '(' ')']
  ['*' '+' ',' '-' '.']
  ['/' '0' '1' '2' '3']
  ['4' '5' '6' '7' '8']]

 [['9' ':' ';' '<' '=']
  ['>' '?' '@' 'A' 'B']
  ['C' 'D' 'E' 'F' 'G']
  ['H' 'I' 'J' 'K' 'L']
  ['M' 'N' 'O' 'P' 'Q']]

 [['R' 'S' 'T' 'U' 'V']
  ['W' 'X' 'Y' 'Z' '[']
  ['\\' ']' '^' '_' '`']
  ['a' 'b' 'c' 'd' 'e']
  ['f' 'g' 'h' 'i' 'j']]

 [['k' 'l' 'm' 'n' 'o']
  ['p' 'q' 'r' 's' 't']
  ['u' 'v' 'w' 'x' 'y']
  ['z' '{' '|' '}' '~']
  ['¡' '¢' '£' '¤' '¥']]

 [['¦' '§' '¨' '©' 'ª']
  ['«' '¬' '¯' '°' '±']
  ['²' 'Þ' 'µ' '¶' '·']
  ['œ' '¹' 'º' '»' '¼']
  ['ʧ' '½' '¿' 'Ƚ' '\n']]]
'''
keytext=input("Keytext:\n")
keylist=list(keytext.replace("♥","\n"))


np.insert(keylist, 1, 125, axis=0)
cipherkey=np.reshape(keylist,(5,5,5))
#print(cipherkey)

def coordlocate(letter):
    for x in range(5):
        for y in range(5):
            for z in range(5):
                if cipherkey[x][y][z] == letter:
                    xcoord.append(x)
                    ycoord.append(y)
                    zcoord.append(z)

if encdec == "E":
    for i in plainlist:
        coordlocate(i)
    for i in range(len(plainlist)):
        cipherlist.append(cipherkey[xcoord[i]][ycoord[i-1]][zcoord[i-2]])
    ciphertext="".join(cipherlist)
    print(ciphertext)
elif encdec == "D":
    for i in cipherlist:
        coordlocate(i)
    for i in range(len(cipherlist)):
        plainlist.append(cipherkey[xcoord[i]][ycoord[ (i+1) % len(cipherlist)]][zcoord[ (i+2) % len(cipherlist)]])
    plaintext="".join(plainlist)
    print(plaintext)
else:
    print("you mongrel")
