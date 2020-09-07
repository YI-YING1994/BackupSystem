#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time

welecomeMSG = """歡迎使用 Tar Backup 系統!
此系統使用 tar 指令建置而成，這也是此系統命名為 Tarback 的原因"""
exitMSG = "Thank you for your using"

def exit(msg, countDown):
    print("")
    print(msg)

    for i in range(countDown, 0, -1):
        sys.stdout.write("\rSystem will be closed in %d second"% i)
        time.sleep(1)

def main():
    while True:
        print("請告訴我們您想做什麼？")
        print("1.還原檔案")
        print("2.立即備份")
        print("3.檢視過去備份")
        print("4.離開")
        print()
        userChoice = input("請輸入您的選擇(1/2/3/4):")
        os.system("clear")

        if userChoice == "1":
            pass
        elif userChoice == "2":
            pass
        elif userChoice == "3":
            pass
        elif userChoice == "4":
            break
        else:
            print("很抱歉，我們無法理解您的選擇「%s」是什麼。請輸入數字(1/2/3/4)"% userChoice)
        print()

try:
    os.system(r"printf \\e\[\?1049h")
    os.system("clear")
    print(welecomeMSG)
    print()
    main()
except KeyboardInterrupt as e:
    exit(e, 0)
else:
    exit(exitMSG, 0)
finally:
    os.system(r"printf \\e\[\?1049l")
