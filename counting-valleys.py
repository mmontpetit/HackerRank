def countingValleys(n, s):
    sealevel = 0
    valleys = 0
    for i in list(s):
        if(i=="U"):
            sealevel+=1
            print(sealevel, valleys)
        elif(i=="D"):
            sealevel-=1
            
            if(sealevel==-1):
                valleys+=1
    
    return valleys


or

def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
    
    return valley