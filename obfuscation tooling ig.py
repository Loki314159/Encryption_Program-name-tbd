import random

trifidlist=list(""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼—½¿Ƚ
""")
print(trifidlist)
random.shuffle(trifidlist)#shuffle because I am too lazy to get a key
print(trifidlist)
obfuscatedkey=""
e=1
for i in trifidlist:
    if e==1:
        obfuscatedkey+=f"chr({ord(i)})" # just putting this like this because I want to not need to do formatting after copying this from terminal
        e=0
    else:
        obfuscatedkey+=f" + chr({ord(i)})"
print(obfuscatedkey)


print(chr(95) + chr(104) + chr(50) + chr(65) + chr(113) + chr(114) + chr(102) + chr(74) + chr(35) + chr(48) + chr(103) + chr(59) + chr(82) + chr(81) + chr(42) + chr(77) + chr(93) + chr(182) + chr(99) + chr(78) + chr(75) + chr(126) + chr(186) + chr(70) + chr(175) + chr(162) + chr(172) + chr(185) + chr(573) + chr(191) + chr(54) + chr(183) + chr(165) + chr(96) + chr(10) + chr(161) + chr(339) + chr(44) + chr(125) + chr(169) + chr(189) + chr(8212) + chr(53) + chr(116) + chr(64) + chr(92) + chr(51) + chr(47) + chr(115) + chr(39) + chr(90) + chr(176) + chr(168) + chr(69) + chr(61) + chr(91) + chr(118) + chr(89) + chr(124) + chr(55) + chr(56) + chr(117) + chr(187) + chr(45) + chr(123) + chr(41) + chr(171) + chr(111) + chr(164) + chr(63) + chr(98) + chr(86) + chr(32) + chr(85) + chr(79) + chr(107) + chr(33) + chr(46) + chr(66) + chr(109) + chr(71) + chr(108) + chr(110) + chr(122) + chr(37) + chr(34) + chr(72) + chr(106) + chr(222) + chr(60) + chr(73) + chr(100) + chr(120) + chr(49) + chr(58) + chr(177) + chr(52) + chr(181) + chr(62) + chr(101) + chr(167) + chr(57) + chr(67) + chr(112) + chr(97) + chr(170) + chr(80) + chr(188) + chr(105) + chr(83) + chr(68) + chr(87) + chr(84) + chr(163) + chr(43) + chr(40) + chr(119) + chr(76) + chr(38) + chr(121) + chr(178) + chr(88) + chr(94) + chr(166) + chr(36))
#shuffled and obfuscated key