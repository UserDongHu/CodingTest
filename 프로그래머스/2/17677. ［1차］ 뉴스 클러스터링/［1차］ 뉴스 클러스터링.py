import re
def solution(str1, str2):
    mystr1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    mystr2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(mystr1) == 0 and len(mystr2) == 0:
        return 65536
    else: 
        str1_2 = mystr1[:]
        str1_2_2 = mystr1[:]
        for i in mystr2:
            str1_2_2.append(i) if i not in str1_2 else str1_2.remove(i)
        hap = len(str1_2_2)
        print(str1_2_2)
        
        temp = []
        for i in mystr2:
            if i in mystr1:
                mystr1.remove(i)
                temp.append(i)
        gyo = len(temp)
        print(temp)
        
        return int(gyo / hap * 65536)