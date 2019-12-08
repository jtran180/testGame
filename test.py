
from tkinter import *
import random

#--------------------------------------Player-Stats-------------------------------------------------
playerChoice = ""
playerMagicChoice = ""
playerSkillChoice = ""
playerAttack = ""
player = []
playerManaCost = 0
playerDead = "Dead" in player
playerPriority = 0
playerSpellList = ["Frostbite", "Heal", "Light", "Blizzard", "Shine", "Permafrost"]
playerSkillList = ["Frigid Jab", "Wide Sweep", "Light Lance", "Triple Thrust", "Icicle Spear", "Sub-Zero Stab"]
playerDamage = 0
playerHealing = 0

playerHP = 100
playerMaxHP = 100

playerMP = 75
playerMaxMP = 75

playerSP = 80
playerMaxSP = 80

playerSTR = 20
playerBaseSTR = 20

playerDEF = 5
playerBaseDEF = 5

playerSKL = 15
playerBaseSKL = 15

playerMAG = 15
playerBaseMAG = 15

playerRES = 5
playerBaseRES = 5

playerSPD = 15
playerBaseSPD = 15

#----------------------------------------Computer-Stats---------------------------------------------
cpuChoice = random.randint(1,2)
cpuAttack = ""
cpu = []
cpuOneName = "Bandit"
cpuDead = "Dead" in cpu
cpuPriority = 0
cpuDamage = 0
cpuHealing = 0
cpuHP = 120
cpuMaxHP = 120

cpuMP = 0
cpuMaxMP = 0

cpuSP = 75
cpuMaxSP = 75

cpuSTR = 15
cpuBaseSTR = 15

cpuDEF = 10
cpuBaseDEF = 10

cpuSKL = 15
cpuBaseSKL = 15

cpuMAG = 5
cpuBaseMAG = 5

cpuRES = 5
cpuBaseRES = 5

cpuSPD = 20
cpuBaseSPD = 20
#-------------------------------------Misc-Stats----------------------------------------------------
speedOrder = [playerPriority, cpuPriority]
placeHolderInt = 0
placeHolderStr = ""
manaCost = 0
staminaCost = 0
userSTR = 0
userMAG = 0
userSKL = 0
userACC = 90
targetDEF = 0
targetRES = 0
targetSPD = 0
freezeCounter = 0
bleedCounterCPU = 0
bleedCounterPlayer = 0
blindCounter = 0
extraDamage = 0
#=========================================Functions=================================

def nameEntered():
    player1 =  txt.get()
 
    res = "You've come face to face with bandit. " + player1 + " must battle"

    menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)

    lbl2.configure(text= res)    

def Bash():

    global cpuHP

    damage = random.randint(1, 10)

    banditBash()

    cpuHP = cpuHP -  damage

    if(cpuHP <= 0):
        res = "You  have won!"
    else:
        res = "Bandit took " + str(damage) + " damage."
        menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)

    lbl2.configure(text = res)
    


def Magic():

    frostbiteBtn = Button(window, text="Frostbite", command=Frostbite)
    healBtn = Button(window, text="Heal", command=Heal)
    lightBtn = Button(window, text="Light", command=Light)
    blizzBtn = Button(window, text="Blizzard", command=Blizzard)
    shineBtn = Button(window, text="Shine", command=Shine)
    permaBtn = Button(window, text="Permafrost", command=Permafrost)

    frostbiteBtn.grid(column=1, row=5)
    healBtn.grid(column=2, row=5)
    lightBtn.grid(column=3, row=5)
    blizzBtn.grid(column=4, row=5)
    shineBtn.grid(column=5, row=5)
    permaBtn.grid(column=6, row=5)

def Frostbite():
    global cpuHP
    global playerMP

    if(playerMP < 5):
        res =  "Not enough mana!"
    else:
        banditBash()
        damage = random.randint(8, 20)
        playerMP -= playerMP -5
        cpuHP = cpuHP - damage

        if(cpuHP <= 0):
            res = "You  have won!"
        else:
            res = "Bandit took " + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text = res)

def Heal():

    res = "Hi"

    lbl.configure(text = res)

def Light():

    res = "Hi"

    lbl.configure(text = res)

def Blizzard():

    res = "Hi"

    lbl.configure(text = res)

def Shine():

    res = "Hi"

    lbl.configure(text = res)

def Permafrost():

    res = "Hi"

    lbl.configure(text = res)

def Skills():

    res = "Hi"

    lbl.configure(text = res)

def banditBash():
    global playerHP

    damage = random.randint(1,10)

    playerHP -= damage

    if(playerHP <= 0):
        res = "You have died"
    else:
        res = "You took " + str(damage) + " damage."
    
    lbl.configure(text = res)

def menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice):
    res = "You: HP:" + str(playerHP) + " MP: " + str(playerMP) + " SP: " + str(playerSP) 
    res2 = "Bandit: HP:" + str(cpuHP) + " MP: " + str(cpuMP) + " SP: " + str(cpuSP)

    lbl3.configure(text=res)
    lbl4.configure(text=res2)

    menuChoice()

    
def menuChoice():
    atkBtn = Button(window, text="Attack", command=Bash)
    mgcBtn = Button(window, text="Magic", command=Magic)
    

    atkBtn.grid(column=1, row=4)
    mgcBtn.grid(column=2, row=4)

def battle():
    menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
#==================Gui==============================#
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('500x500')
 
lbl = Label(window, text="Enter your name: ")

lbl2 = Label(window, text="")

lbl3 = Label(window, text="")

lbl4 = Label(window, text="")
 
lbl.grid(column=0, row=0)

lbl2.grid(column=0, row=1)

lbl3.grid(column=0, row=2)

lbl4.grid(column=0, row=3)

txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)
 
nameBtn = Button(window, text="Enter", command=nameEntered)
 
nameBtn.grid(column=2, row=0)
 
window.mainloop()
