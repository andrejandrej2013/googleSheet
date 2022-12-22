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
                if personAnswers[i]<3:
                    personAnswers[i]+=1
                    points-=1
    elif points<0:
        print("Some problems with userPoints calculations")
        return None
    random.shuffle(personAnswers) 
    return personAnswers

# SelfEsteem
def getSelfEsteemResults(userSelfEsteemLevel=random.randint(0,2)):
    
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
# change functions +1 and middlePoints
def highNumberPoints(x,pointsMax,sampleSize):
    return int((-(pointsMax/(sampleSize**2))*(x**2))+(((2*pointsMax)/sampleSize)*x)+1)
def lowNumberPoints(x,pointsMax,sampleSize):
    return int(pointsMax/(sampleSize**2)*(x**2)+1)
def middlePoints(x,pointsMax,sampleSize):
    return None

def getCommonMotivationsPoints(SELevel=random.randint(0,2)):
    sample = 1000
    extrinsicMaxPoints=100
    intrinsicMaxPoints=50

    if SELevel==0:
        personExtrinsic=highNumberPoints(random.randint(1,sample),extrinsicMaxPoints)
        personIntrinsic=lowNumberPoints(random.randint(1,sample),intrinsicMaxPoints)
    elif SELevel==1:
        personExtrinsic=personIntrinsic=middlePoints(random.randint(1,sample),extrinsicMaxPoints)
    elif SELevel==2:
        personExtrinsic=lowNumberPoints(random.randint(1,sample),extrinsicMaxPoints)
        personIntrinsic=highNumberPoints(random.randint(1,sample),intrinsicMaxPoints)
    else:
        print("err: self-esteem should be 0,1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)")
        return "err"
    return {"personExtrinsic":personExtrinsic,"personIntrinsic":personIntrinsic}

class TUSMSQ2ResualtGenerator:
    extrinsicMaxPoints=100
    intrinsicMaxPoints=50
    sample=0
    SELevel=0

    def highNumberPoints(x,pointsMax,sampleSize=sample):
        return int((-(pointsMax/(sampleSize**2))*(x**2))+(((2*pointsMax)/sampleSize)*x)+1)
    def lowNumberPoints(x,pointsMax,sampleSize=sample):
        return int(pointsMax/(sampleSize**2)*(x**2)+1)
    def middlePoints(x,pointsMax,sampleSize=sample):
        return
    def __init__(self,SELevel,sample):
        self.sample=sample
        self.SELevel=SELevel
        if SELevel==0:
            personExtrinsic=self.highNumberPoints(random.randint(1,self.sample),self.extrinsicMaxPoints)
            personIntrinsic=self.lowNumberPoints(random.randint(1,self.sample),self.intrinsicMaxPoints)
        elif SELevel==1:
            personExtrinsic=personIntrinsic=self.middlePoints(random.randint(1,self.sample),self.extrinsicMaxPoints)
        elif SELevel==2:
            personExtrinsic=self.lowNumberPoints(random.randint(1,self.sample),self.extrinsicMaxPoints)
            personIntrinsic=self.highNumberPoints(random.randint(1,self.sample),self.intrinsicMaxPoints)
        else:
            print("err: self-esteem should be 0,1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)")
            return "err: self-esteem should be 0,1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)"
        

SELevel=0
print(getSelfEsteemResults(SELevel))

