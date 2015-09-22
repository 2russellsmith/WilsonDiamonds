import os
import pymysql

clear = lambda: os.system('clear')

clear()

def mainMenu():
    broken = 0
    quitting = 0
    while quitting == 0:
        clear()
        print("1) Print a diamond")
        print("2) Sub Menu")
        print("3) Quit")
        if broken:
            selection = input("Invalid selection. Select: ")
        else:
            selection = input("Select: ")

        if selection == '1':
            printDiamond()
            broken = 0
        elif selection == '2':
            subMenu()
            broken = 0
        elif selection == '3':
            quitting = 1
        else:
            broken = 1

def selectall():
    clear()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='WilsonDiamonds')
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    for r in cur:
        print(r)
    cur.close()
    conn.close()
    input("Found...")

def addRing():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='WilsonDiamonds')
    cur = conn.cursor()
    name = input("Ring name: ")
    cur.execute("INSERT INTO inventory (name) VALUES ('%s')" % name)
    cur.close()
    conn.commit()
    conn.close()
    input("Added...")



def subMenu():
    broken = 0
    while 1:
        clear()
        print("1) Print a diamond")
        print("2) Select All Rings")
        print("3) Add A Ring")
        print("m) Main menu")
        if broken:
            selection = input("Invalid selection. Select: ")
        else:
            selection = input("Select: ")

        if (selection == '1'):
            printDiamond()
            broken = 0
        elif selection == '2':
            selectall()
            broken = 0
        elif selection == '3':
            addRing()
            broken = 0
        elif selection == 'm':
            break
        else:
            broken = 1

def printDiamond():
    clear()
    f = open('diamond.txt', 'r')
    diamond = f.read()
    print(diamond)
    input("Done...")

mainMenu()
