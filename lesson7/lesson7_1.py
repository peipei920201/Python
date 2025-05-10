import tools

def main():
    hight:float = float(input("請輸入身高(公分):"))
    weight:float = float(input("請輸入體重:"))

    BMI = tools.get_bmi(weight,hight) #tools裡的函式
    a_message = tools.aa_bmi(BMI)
    print(a_message)

if __name__ == '__main__':   #文件(.py檔)敘述
    main()