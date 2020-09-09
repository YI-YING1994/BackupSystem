#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time

welecomeMSG = "歡迎使用 Tar Backup 系統!"
exitMSG = "Thank you for your using"

def recoverSingleFile():
    while True:
        fileName = input("請輸入您想還原的檔案名稱，或是輸入「exit」返回上層選擇清單:")
        baseVersionLog = "backup/logs/"
        
        if fileName == "exit":
            os.system("clear")
            break
        elif os.path.exists(baseVersionLog + fileName):
            os.system("clear")
            print("「%s」有這些版本:\n"% fileName)

            versionLog = baseVersionLog + fileName
            f = open(versionLog, "r")
            versions = f.readlines()
            i = 1
            for version in versions:
                print("%d.%s"% (i, version.strip()))
                i += 1            
            
            print("%d.返回"% i)

            userChoice = input("\n請輸入您想取得的版本:")
            os.system("clear")

            if userChoice == "%d"%i:
                pass
            else:
                break


        else:
            print("檔案「%s」不存在任何備份，請再次輸入檔名。"% fileName)
            print()

def showBackupContent(name, path):
    bFinished = False
    while not bFinished:
        os.system("clear")
        print("備份「%s」包含了這些檔案及資料夾:\n"% name)
        content = os.listdir(path)
        for file in content:
            print(file)

        print("\n1.找到要還原的檔案了，請幫我還原")
        print("2.未看到要還原的檔案，查看此資料夾不同時間點的備份")
        print("3.返回上層資料夾")
        print("4.進入下層資料夾")
        print("5.返回備份選擇清單")

        userChoice = input("\n請輸入您的選擇:")
        if userChoice == "5":
            os.system("clear")
            bFinished = True
            return bFinished
        if userChoice == "1":
            os.system("clear")
            print("請選擇您想還原的檔案\n")
            i = 1
            for file in content:
                if os.path.isfile(path + "/" + file):
                    print("%d.%s"% (i, file))
                    i += 1
            print("%d.%s"%(i, "返回"))
            
            recoverChoice = input("\n您的選擇:")
            if recoverChoice == "%d"% i:
                pass
            else:
                os.system("clear")
                input("還原完成，請按下 Enter 鍵，以離開程式")
                os.sys.exit()
        elif userChoice == "2":
            pass
        elif userChoice == "3":
            os.system("clear")
            if os.path.dirname(path) != "backup/database":
                break
            else:
                input("此資料夾為最上層目錄，請按 Enter 以重新選擇")
        elif userChoice == "4":
            os.system("clear")
            print("請選擇您想進入的下層資料夾\n")
            i = 1
            for file in content:
                if os.path.isdir(path + "/" + file):
                    print("%d.%s"% (i, file))
                    i += 1
            print("%d.%s"%(i, "返回"))
            
            folderChoice = input("\n您的選擇:")
            if folderChoice == "%d"% i:
                pass
            else:
                bFinished = showBackupContent(content[int(folderChoice)-1], path + "/" + content[int(folderChoice)-1])
                print("return")

def viewBackup():
    while True:
        databasePath = "backup/database/"
        
        if not os.path.exists(databasePath) or len(os.listdir(databasePath)) == 0:
            input("尚未進行過備份，按下 Enter 鍵，以返回主選單")
            os.system("clear")
            return
        
        backups = os.listdir(databasePath)
        backups.sort()
        print("目前備份有\n")
        i = 1
        for backup in backups:
            print("%d.%s"% (i, backup))
            i += 1
        print("%d.返回"% i)
        
        userChoice = input("\n請輸入欲查看的備份代號:")
        os.system("clear")
        if userChoice == "%d"%i:
            break
        else:
            showBackupContent(backups[int(userChoice)-1], databasePath + backups[int(userChoice)-1])

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
            recoverSingleFile()
        elif userChoice == "2":
            
            progress = 50
            for i in range(progress):
                os.system("clear")
                print("正在進行備份作業，請您耐心等候%s"% ("." * (i%4)))
                print("[%s%s]"% ("#" * i, "=" * (progress -i)))
                time.sleep(0.25)
            
            os.system("clear")

        elif userChoice == "3":
            viewBackup()
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
