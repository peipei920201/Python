#猜數字遊戲
import tools

def main():
    while(True):
        tools.play()
        play = input("繼續?(y,n)")
        if play == 'n':
            break 
       

print("遊戲結束")

if __name__ == "__main__":
    main()