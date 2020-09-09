#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time

welecomeMSG = "Welcome to use Tar Backup system!"
exitMSG = "Thank you for your using"

def recoverSingleFile():
    while True:
        fileName = input("Please input the file name which you want to recover, or input \"exit\" to go back to the selection list:")
        baseVersionLog = "backup/logs/"
        
        if fileName == "exit":
            os.system("clear")
            break
        elif os.path.exists(baseVersionLog + fileName):
            os.system("clear")
            print("\"%s\"has these versions:\n"% fileName)

            versionLog = baseVersionLog + fileName
            f = open(versionLog, "r")
            versions = f.readlines()
            i = 1
            for version in versions:
                print("%d.%s"% (i, version.strip()))
                i += 1            
            
            print("%d.Go back"% i)

            userChoice = input("\nPlease select the version which you want to get:")
            os.system("clear")

            if userChoice == "%d"%i:
                pass
            else:
                break


        else:
            print("There is no any backup of \"%s\", please input a new file name."% fileName)
            print()

def showBackupContent(name, path):
    bFinished = False
    while not bFinished:
        os.system("clear")
        print("\"%s\"has these files and directories:\n"% name)
        content = os.listdir(path)
        for file in content:
            print(file)

        print("\n1.Found the file, please recover it for me")
        print("2.Not seen the file which I want, check different backup of this directory")
        print("3.Go back to the previous directory")
        print("4.Go forward to the next directory")
        print("5.Go back to the backup selection list")

        userChoice = input("\nPlease input your choice:")
        if userChoice == "5":
            os.system("clear")
            bFinished = True
            return bFinished
        if userChoice == "1":
            os.system("clear")
            print("Please select the file which you want to recover\n")
            i = 1
            for file in content:
                if os.path.isfile(path + "/" + file):
                    print("%d.%s"% (i, file))
                    i += 1
            print("%d.%s"%(i, "Go back"))
            
            recoverChoice = input("\nYour choice:")
            if recoverChoice == "%d"% i:
                pass
            else:
                os.system("clear")
                input("Recovery finished, Please press enter to leave the program")
                os.sys.exit()
        elif userChoice == "2":
            pass
        elif userChoice == "3":
            os.system("clear")
            if os.path.dirname(path) != "backup/database":
                break
            else:
                input("There is no previous directory, please press enter to go back to the selection list")
        elif userChoice == "4":
            os.system("clear")
            print("Please select the directory which you want to go forward\n")
            i = 1
            for file in content:
                if os.path.isdir(path + "/" + file):
                    print("%d.%s"% (i, file))
                    i += 1
            print("%d.%s"%(i, "Go back"))
            
            folderChoice = input("\nYour choice:")
            if folderChoice == "%d"% i:
                pass
            else:
                bFinished = showBackupContent(content[int(folderChoice)-1], path + "/" + content[int(folderChoice)-1])
                print("return")

def viewBackup():
    while True:
        databasePath = "backup/database/"
        
        if not os.path.exists(databasePath) or len(os.listdir(databasePath)) == 0:
            input("There is no any backup, press enter to go back to the main menu")
            os.system("clear")
            return
        
        backups = os.listdir(databasePath)
        backups.sort()
        print("We have these backups\n")
        i = 1
        for backup in backups:
            print("%d.%s"% (i, backup))
            i += 1
        print("%d.Go back"% i)
        
        userChoice = input("\nPlease select the backup which you want to look inside:")
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
        print("Please tell us what you want to do？")
        print("1.Recover single file")
        print("2.Backup immediately")
        print("3.View the backups")
        print("4.Leave the program")
        print()
        userChoice = input("Please input your choice(1/2/3/4):")
        os.system("clear")

        if userChoice == "1":
            recoverSingleFile()
        elif userChoice == "2":
            
            progress = 50
            for i in range(progress):
                os.system("clear")
                print("It takes time to complete backup, please be patient%s"% ("." * (i%4)))
                print("[%s%s]"% ("#" * i, "=" * (progress -i)))
                time.sleep(0.25)
            
            os.system("clear")

        elif userChoice == "3":
            viewBackup()
        elif userChoice == "4":
            break
        else:
            print("Sorry, we could not understand what your choice \"%s\" is. Please input number 1, 2, 3 or 4"% userChoice)
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
