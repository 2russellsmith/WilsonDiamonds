import os
import pymysql

clear = lambda: os.system('clear')

clear()

def mainMenu():
    clear()
    print("1) Print a diamond")
    print("2) Sub Menu")
    print("3) Quit")
    selection = input("Select: ")
    valid = 1
    while valid != 0:
        if selection == '1':
            printDiamond()
            valid = 0
        elif selection == '2':
            subMenu()
            valid = 0
        elif selection == '3':
            valid = 0
        else:
            selection = input("Invalid selection. Select: ")

def selectall():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='WilsonDiamonds')
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    for r in cur:
        print(r)
    cur.close()
    conn.close()
    input("Found...")
    mainMenu()

def addRing():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='WilsonDiamonds')
    cur = conn.cursor()
    name = input("Ring name: ")
    cur.execute("INSERT INTO inventory (name) VALUES ('%s')" % name)
    cur.close()
    conn.commit()
    conn.close()
    input("Added...")
    mainMenu()



def subMenu():
    clear()
    print("1) Print a diamond")
    print("2) Select All Rings")
    print("3) Add A Ring")
    print("m) Main menu")
    selection = input("Select: ")
    valid = 1
    while (valid != 0):
        if (selection == '1' or selection == '2' or selection == '3' or selection == 'm'):
            valid = 0
        else:
            selection = input("Invalid selection. Select: ")

    if (selection == '1'):
        printDiamond()
    elif selection == '2':
        selectall()
        valid = 0
    elif selection == '3':
        addRing()
        valid = 0
    elif selection == 'm':
        mainMenu()
        valid = 0

def printDiamond():
    clear()
    f = open('diamond.txt', 'r')
    diamond = f.read()
    print(diamond)
    input("Done...")
    mainMenu()

mainMenu()