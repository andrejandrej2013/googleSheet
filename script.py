import random
import gspread
from datetime import datetime, timedelta

sa = gspread.service_account(filename="indigo-charge-372214-89932d23d246.json")
sh = sa.open("Test")

list1 = sh.worksheet("list1")
list2 = sh.worksheet("list2")

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

def highNumberPoints(x,sampleSize,minPoints,maxPoints):
    return int(((minPoints-maxPoints)/(sampleSize**2))*(x**2)+(2*(maxPoints-minPoints)/sampleSize)*x+(minPoints))
def lowNumberPoints(x,sampleSize,minPoints,maxPoints):
    return int((((maxPoints-minPoints)/(sampleSize**2))*(x**2))+minPoints)
def middlePoints(x,sampleSize,minPoints,maxPoints):
    tmpMaxPoints=maxPoints/2
    oneSidePoints=highNumberPoints(x,sampleSize,minPoints,tmpMaxPoints)
    if random.randint(0,1):
        oneSidePoints+=tmpMaxPoints-oneSidePoints
    return oneSidePoints
def deviation(points,deviation=1):
    if random.randint(0,1):
        if random.randint(0,1):
            points+=deviation
        else:
            points-=deviation
    return points
    
def getMotivationAnswersList(userSelfEsteemLevel=random.randint(0,2)):
    sample = 1000
    maxExtrinsicPoints=100
    maxIntrinsicPoints=50
    extrinsicArraySize=20
    intrinsicArraySize=10
    oneSlotSizeMax=5
    oneSlotSizeMin=1
    motivationList=['e', 'i', 'e', 'e', 'e', 'i', 'e', 'i', 'e', 'e', 'e', 'i', 'e', 'i', 'e', 'e', 'e', 'i', 'e', 'i', 'e', 'e', 'e', 'i', 'e', 'i', 'e', 'e', 'e', 'i']

    if userSelfEsteemLevel==0:
        personExtrinsic=highNumberPoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
        personIntrinsic=lowNumberPoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
    elif userSelfEsteemLevel==1:
        personIntrinsic=middlePoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
        personExtrinsic=middlePoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
    elif userSelfEsteemLevel==2:
        personExtrinsic=lowNumberPoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
        personIntrinsic=highNumberPoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
    else:
        print("err: self-esteem should be 0, 1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)")
        return None
    # print(personExtrinsic,personIntrinsic)
    while True:
        personExtrinsic=deviation(personExtrinsic)
        personIntrinsic=deviation(personIntrinsic)
        if personExtrinsic>=extrinsicArraySize and personExtrinsic<=maxExtrinsicPoints and personIntrinsic>=intrinsicArraySize and personIntrinsic<=maxIntrinsicPoints:
            break
    print("Extrinsic : ",personExtrinsic/maxExtrinsicPoints,"Intrinsic : ",personIntrinsic/maxIntrinsicPoints)
    personExtrinsicAnswers=spreadPoints(personExtrinsic,extrinsicArraySize,oneSlotSizeMax,oneSlotSizeMin)
    personIntrinsicAnswers=spreadPoints(personIntrinsic,intrinsicArraySize,oneSlotSizeMax,oneSlotSizeMin)
    for i in range(len(motivationList)):
        if motivationList[i]=="e":
            motivationList[i]=personExtrinsicAnswers.pop(0)
        else:
            motivationList[i]=personIntrinsicAnswers.pop(0)
    return motivationList
     
# do not need
def getMotivationList():
    list = [None] * 30
    extrinsicQuestions=[1,7,13,19,25,3,9,15,21,27,4,10,16,22,28,5,11,17,23,29]
    intrinsicQuestions=[2,8,14,20,26,6,12,18,24,30]
    for i in range(len(extrinsicQuestions)):
        list[extrinsicQuestions[i]-1]="e"
    for i in range(len(intrinsicQuestions)):
        list[intrinsicQuestions[i]-1]="i"
    print(list)

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def getNextDateTime(previousDateTime):
    format = "%d.%m.%Y %H:%M:%S"
    previousDateTime=datetime.strptime(previousDateTime,format)
    nextDateTime = previousDateTime + timedelta(minutes=random.randint(0,23),hours=random.randint(1,3),seconds=random.randint(1,31))
    now = datetime.now()
    if nextDateTime>now:
        print("err: cant be bigger than current datetime")
        return None
    return nextDateTime

def writeResualts(number,worksheet):
    POSITIONS=[1,2,4,35]
    emptyRow=int(next_available_row(worksheet))
    for i in range(number):
        selfEsteemLevel=random.randint(0,2)
        print(getNextDateTime(worksheet.cell(emptyRow-1, 1).value))
        print(type(getNextDateTime(worksheet.cell(emptyRow-1, 1).value)))
        worksheet.update_cell(emptyRow,POSITIONS[0], str(getNextDateTime(worksheet.cell(emptyRow-1, 1).value)))
        worksheet.update_cell(emptyRow,POSITIONS[1], random.randint(17,23))
        motivationAnswersList=getMotivationAnswersList(selfEsteemLevel)
        for i in range(len(motivationAnswersList)):
            worksheet.update_cell(emptyRow,POSITIONS[2+i], motivationAnswersList[i])
        selfEsteemAnswersList=getSelfEsteemAnswersList(selfEsteemLevel)
        for i in range(len(selfEsteemAnswersList)):
            worksheet.update_cell(emptyRow,POSITIONS[3+i], selfEsteemAnswersList[i])    
        emptyRow+=1

writeResualts(1,list2)
# list2.update_cell(17,1,"hi")


