import random
import gspread
from datetime import datetime, timedelta
from colorama import Fore, Back, Style

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
    personExtrinsic=personIntrinsic=0

    if userSelfEsteemLevel==0:
        while True:
            personExtrinsic=highNumberPoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
            personIntrinsic=lowNumberPoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
            if personExtrinsic/maxExtrinsicPoints<personIntrinsic/maxIntrinsicPoints and random.randint(0,1):
                continue
            break
    elif userSelfEsteemLevel==1:
        personIntrinsic=middlePoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
        personExtrinsic=middlePoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
        
    elif userSelfEsteemLevel==2:
        while True:
            personExtrinsic=lowNumberPoints(random.randint(0,sample),sample,extrinsicArraySize,maxExtrinsicPoints)
            personIntrinsic=highNumberPoints(random.randint(0,sample),sample,intrinsicArraySize,maxIntrinsicPoints)
            if personExtrinsic/maxExtrinsicPoints>personIntrinsic/maxIntrinsicPoints and random.randint(0,1):
                continue
            break
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
    nextDateTime=nextDateTime.strftime("%d.%m.%Y %H:%M:%S")
    print(str(nextDateTime))
    return nextDateTime

def getNextId(worksheet,emptyRow):
    val = worksheet.cell(emptyRow-1, worksheet.find("ID").col).value
    return val
def writeResualts(number,worksheet):
    POSITIONS=[0,1,2,4,35]
    emptyRow=int(next_available_row(worksheet))
    for i in range(number):
        answerList=  [None] * 50
        selfEsteemLevel=random.randint(0,2)
        print(Back.GREEN + "selfEsteemLevel : "+str(selfEsteemLevel)+Style.RESET_ALL)
        # print(Style.RESET_ALL)
        answerList[POSITIONS[0]] = int(getNextId(worksheet,emptyRow))+1
        print(answerList[POSITIONS[0]])
        answerList[POSITIONS[1]] = str(getNextDateTime(worksheet.cell(emptyRow-1, worksheet.find("DateTime").col).value))
        answerList[POSITIONS[2]] = random.randint(17,23)
        # worksheet.update_cell(emptyRow,POSITIONS[0], str(getNextDateTime(worksheet.cell(emptyRow-1, 1).value)))
        # worksheet.update_cell(emptyRow,POSITIONS[1], random.randint(17,23))
        motivationAnswersList=getMotivationAnswersList(selfEsteemLevel)
        selfEsteemAnswersList=getSelfEsteemAnswersList(selfEsteemLevel)
        
        for j in range(len(motivationAnswersList)):
            answerList[POSITIONS[3]+j] = motivationAnswersList[j]
            # worksheet.update_cell(emptyRow,POSITIONS[2]+j, motivationAnswersList[j])
        for j in range(len(selfEsteemAnswersList)):
            answerList[POSITIONS[4]+j] = selfEsteemAnswersList[j]
            # worksheet.update_cell(emptyRow,POSITIONS[3]+j, selfEsteemAnswersList[j])    
        
        worksheet.insert_row(answerList,emptyRow)
        emptyRow+=1
        

writeResualts(1,list1)


