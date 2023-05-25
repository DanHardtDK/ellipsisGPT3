import sys


exampleFileList = sys.argv[1]
f = open(exampleFileList)
resultFiles = f.readlines()
tot=[]
for fName in resultFiles:
    fName = fName.strip()
    rFile = open(fName)
    results = rFile.readlines()

    r=results[1]
    current=[]
    vals = r.split()
    current.append(vals)

    for r in results[2:]:
        vals = r.split()
        current.append(vals)

    tot.append(current)

print("Pattern \t Total VPEcorrect    NoVPEcorrect")
out = list(zip(*tot))
avg1tot = avg2tot = cnt = 0
for o in out:
    print(o[0][0],end="\t ") #pattern
    tot=[0,0,0]
    for vals in o:
        tot[0] += int(vals[1])
        tot[1] += int(vals[2])
        tot[2] += int(vals[3])
    avg1=tot[1]/tot[0]
    avg2=tot[2]/tot[0]
    avg1tot += avg1
    avg2tot += avg2
    cnt+=1
    print(tot[0],tot[1],"(",avg1,"%)",tot[2],"(",avg2,"%)")


print(avg1tot/cnt, avg2tot/cnt)
    
        
            


    
        

