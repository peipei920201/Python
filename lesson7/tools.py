import random

def aa_bmi(bmi:float)->str  :
    if bmi < 18.5:
        message:str = "體重過輕"
    elif bmi < 24:
        message:str = "體重適中"
    else:
        if bmi < 27:
            message:str = "體重過重"
        elif bmi < 30:
            message:str = "輕度肥胖"
        elif bmi < 35:
            message:str = "中度肥胖"
        else:
            message:str = "重度肥胖"
    
    return message

def get_bmi(w:int,h:int)->float:
    return round((w/(h/100)**2),ndigits=1)

def play():
    min = 1
    max = 99
    num = 0
    target = random.randint(min,max)
    print("=======猜數字遊戲=======\n\n")
    print(target)
    while(True):
        keyin = input(f"數字範圍{min}~{max}，猜數字:")
        num+=1

        try:
            keyin = int(keyin)
        except:
            print("輸入錯誤，請重新輸入")
            continue

        keyin = int(keyin)
        if keyin == target:
            print(f"猜對了!答案是{target}，總共猜了{num}次")
            break

        elif keyin>max or keyin > target:
            print("太大了，猜小點")
            max = keyin
        else:
            print("太小了，猜大點")
            min = keyin