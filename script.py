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

def rosenbergResualtGenerator(userSelfEsteemLevel=random.randint(0,2)):
    
    if userSelfEsteemLevel<0 or userSelfEsteemLevel>2:
        return "err: self-esteem should be 0,1 or 2, the test reveals three levels of self-esteem (0:low, 1:normal, 2:high)"
    
    maxPoints=30
    normalSelfEsteemRange=[15,25]
    
    userPoints = 0
    if userSelfEsteemLevel == 0:
        userPoints = random.randint(0,normalSelfEsteemRange[0]-1)
    elif userSelfEsteemLevel == 1:
        userPoints = random.randint(normalSelfEsteemRange[0],normalSelfEsteemRange[1])
    else:
        userPoints = random.randint(normalSelfEsteemRange[1]+1,maxPoints)

    userAnswers = [0]*10
    for i in range(len(userAnswers)):
        generatQuestionPoint=random.randint(0,3)
        if userPoints-generatQuestionPoint<0:
            userAnswers[i]=userPoints
            break
        userAnswers[i]=generatQuestionPoint
        userPoints-=generatQuestionPoint
    if userPoints>0:
        while(userPoints!=0):
            for i in range(len(userAnswers)):
                if userPoints==0:
                    break
                if userAnswers[i]<3:
                    userAnswers[i]+=1
                    userPoints-=1
    elif userPoints<0:
        print("Some problems with userPoints calculations")
    random.shuffle(userAnswers)
    return userAnswers
class TUSMSQ2ResualtGenerator:
    def __init__():
        x=2
    def TUSMSQ2ResualtGenerator(maxAmountOfPoints,angle=3,userSelfEsteemLevel=random.randint(0,2)):
        points=[0,maxAmountOfPoints/2,maxAmountOfPoints]


print(rosenbergResualtGenerator(3))
print(TUSMSQ2ResualtGenerator(3))