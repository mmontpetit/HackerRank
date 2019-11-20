def jumpingOnClouds(c):
    i=0
    count=0
    while(i!=len(c)-1):
        
        if(i+2<=len(c)-1) and (c[i+2]!=1):
            i+=2
            count+=1
        elif(i+1<=len(c)-1) and (c[i+1]!=1):
            i+=1
            count+=1

    return count