import random
# import gspread
# # import pandas as pd
# # from oauth2client.service_account import ServiceAccountCredentials

# sa = gspread.service_account(filename="indigo-charge-372214-89932d23d246.json")
# sh = sa.open("Test")

# list1 = sh.worksheet("list1")
# list2 = sh.worksheet("list2")

# print(list1.acell('D6').value)
# print("\n")


def spreadPoints(points,arraySize,oneSlotSizeMax,oneSlotSizeMin=0):
    points-=oneSlotSizeMin*arraySize
    if points<0:
        print("Not correct parameters:","not enouth points for oneSlotSizeMin")
        return None
    personAnswers = [oneSlotSizeMin]*arraySize 
    for i in range(len(personAnswers)):
        if points == 0:
            break
        generatQuestionPoint=random.randint(oneSlotSizeMin,oneSlotSizeMax)
        if points-generatQuestionPoint<0:
            personAnswers[i]=points
            break
        personAnswers[i]=generatQuestionPoint
        points-=generatQuestionPoint
    if points>0:
        while(points!=0):
            for i in range(len(personAnswers)):
                if points==0:
                    break
                if personAnswers[i]<oneSlotSizeMax:
                    personAnswers[i]+=1
                    points-=1
    elif points<0:
        print("Some problems with userPoints calculations")
        return None
    random.shuffle(personAnswers) 
    return personAnswers

# SelfEsteem
def getSelfEsteemAnswersList(userSelfEsteemLevel=random.randint(0,2)):
    
    if userSelfEsteemLevel<0 or userSelfEsteemLevel>2:
        print("err: self-esteem should be 0,1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)")
        return "err: self-esteem should be 0,1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)"
    
    maxPoints=30
    arraySize=10
    normalSelfEsteemRange=[15,25]
    oneSlotSizeMax=3
    
    userPoints = 0
    if userSelfEsteemLevel == 0:
        userPoints = random.randint(0,normalSelfEsteemRange[0]-1)
    elif userSelfEsteemLevel == 1:
        userPoints = random.randint(normalSelfEsteemRange[0],normalSelfEsteemRange[1])
    else:
        userPoints = random.randint(normalSelfEsteemRange[1]+1,maxPoints)
    

    # return userPoints
    return spreadPoints(userPoints,arraySize,oneSlotSizeMax)

# Motivation
# add middlePoints
def highNumberPoints(x,sampleSize,minPoints,maxPoints):
    return int(((minPoints-maxPoints)/(sampleSize**2))*(x**2)+(2*(maxPoints-minPoints)/sampleSize)*x+(minPoints))
def lowNumberPoints(x,sampleSize,minPoints,maxPoints):
    return int((((maxPoints-minPoints)/(sampleSize**2))*(x**2))+minPoints)
def middlePoints(x,sampleSize,minPoints,maxPoints):
    tmpMaxPoints=(maxPoints-minPoints)/2
    oneSidePoints=highNumberPoints(x,sampleSize,minPoints,tmpMaxPoints)
    if random.randint(0,1):
        oneSidePoints+=tmpMaxPoints-oneSidePoints
    return oneSidePoints
    
def getMotivationAnswersList(SELevel=random.randint(0,2)):
    sample = 1000
    maxExtrinsicPoints=100
    maxIntrinsicPoints=50
    extrinsicArraySize=20
    intrinsicArraySize=10
    oneSlotSizeMax=5
    oneSlotSizeMin=1
    # x,sampleSize,minPoints,maxPoints

    # while True:
    if SELevel==0:
        personExtrinsic=highNumberPoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
        personIntrinsic=lowNumberPoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
        # if personExtrinsic<personIntrinsic and random.randint(0,1):
        #     continue
        # else:
        #     break
    elif SELevel==1:
        personIntrinsic=middlePoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
        personExtrinsic=middlePoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
    elif SELevel==2:
        personExtrinsic=lowNumberPoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
        personIntrinsic=highNumberPoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
        # if personExtrinsic>personIntrinsic and random.randint(0,1):
        #     continue
        # else:
        #     break
    else:
        print("err: self-esteem should be 0,1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)")
        return None
    
    
    return {"personExtrinsic":spreadPoints(personExtrinsic,extrinsicArraySize,oneSlotSizeMax,oneSlotSizeMin),"personIntrinsic":spreadPoints(personIntrinsic,intrinsicArraySize,oneSlotSizeMax,oneSlotSizeMin),"sum":[personExtrinsic,personIntrinsic]}
     



SE=1

for i in range(10):
    print(getMotivationAnswersList(SE),"\n")



