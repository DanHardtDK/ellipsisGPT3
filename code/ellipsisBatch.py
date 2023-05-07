import openai
import json
import sys
import random
import pdb

# sample invocation: python3 ellipsisBatch.py examples1 text-davinci-002 100
# examples1 containing
# 2Sent.json
# 1Sent.json
# 1SentAfter.json
# 1SentSubord.json
# 1SentSubordBackwards.json
# 2Actions.json

# exampleFileList: files containing ellipsis patterns
exampleFileList = sys.argv[1]
if not "json" in exampleFileList:
    exit
f = open(exampleFileList)
exampleFiles = f.readlines()
if len(exampleFiles) == 0:
    exit

# GPT3 model
model = sys.argv[2]
if model not in ["gpt-3.5-turbo", "text-davinci-003","text-davinci-002", "text-ada-001", "text-curie-001", "text-babbage-001"]:
    exit

    # sample size
sampleSize = int(sys.argv[3])
if sampleSize not in [10,50,100, 500]:
    exit

# results File: runID
from datetime import datetime
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%Y_%H%M%S")
print("date and time =", dt_string)
runID =  exampleFileList+"_" + str(sampleSize)+"_"+ model+"_" +"_"+dt_string
print("Running ", runID)
resFile = open(runID,"w")
# Headings
print("File","Total", "VPE Correct","NO VPE Correct", file=resFile)

for eFile in exampleFiles:
    eFile = eFile.strip()
    d = open(eFile)
    examples = json.load(d)
    print("len", len(examples))
       
    examples = random.sample(examples, sampleSize)
    Instructions = "Please give a Yes or No answer:\n\n"

    openai.api_key ="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"

    def completePrompt(p):
        response = openai.Completion.create(
            model=model,
            prompt = Instructions + p + "\n\n",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return(response.choices[0].text)

    def doQuery(p,ans):
        sysout = completePrompt(p)
        sysout = sysout.strip()
        print(p, "System:", sysout)
        sysout = sysout[:len(ans)]
        return(sysout == ans)

    cntVPE = cntNOVPE = cntVPECorrect = cntNOVPECorrect = 0
    for e in examples:
        print("============================================")
        prompt = "C: " +  e['V1a'] +  "\n" + "Q: " + e['Q'] + "\n\n"
        answer = e['A']
        res = doQuery(prompt,answer)
        cntVPE = cntVPE + 1
        if res:
            VPECorrect = True
            cntVPECorrect = cntVPECorrect + 1
        else:
            VPECorrect = False

        print("Yes Ellipsis: Res",res, "Correct is", answer) # 
    
        prompt = "C: " +  e['V1b'] +  "\n" + "Q: " + e['Q'] + "\n\n" # 
        answer = e['A']
        res = doQuery(prompt,answer)


        cntNOVPE = cntNOVPE + 1
        if res:
            NOVPECorrect = True
            cntNOVPECorrect = cntNOVPECorrect + 1
        else:
            NOVPECorrect = False

        print("No Ellipsis: Res",res, "Correct is", answer)         
    
       
    print(eFile,cntVPE, cntVPECorrect,cntNOVPECorrect)
    print(eFile,cntVPE, cntVPECorrect,cntNOVPECorrect, file=resFile)



    
    


    




