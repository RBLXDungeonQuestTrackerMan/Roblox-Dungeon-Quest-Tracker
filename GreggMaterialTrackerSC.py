from tkinter import *
import json
def UpdateFile(data):
    with open('greggfarmingmats.json', 'w') as f:
        json.dump(data, f, indent=4)
def addMats(material, amount, weapon):
    data["TotalMats"][material]+=amount
    entryAddCustomMetal.delete(0, END)
    entryAddCustomObsidian.delete(0, END)
    entryAddCustomGold.delete(0, END)
    entryAddCustomAmethyst.delete(0, END)
    entrySetCustomMetal.delete(0, END)
    entrySetCustomObsidian.delete(0, END)
    entrySetCustomGold.delete(0, END)
    entrySetCustomAmethyst.delete(0, END)
    Generate(weapon, data)
    UpdateFile(data)
def setMats(material, amount, weapon):
    data["TotalMats"][material]=amount
    entryAddCustomMetal.delete(0, END)
    entryAddCustomObsidian.delete(0, END)
    entryAddCustomGold.delete(0, END)
    entryAddCustomAmethyst.delete(0, END)
    entrySetCustomMetal.delete(0, END)
    entrySetCustomObsidian.delete(0, END)
    entrySetCustomGold.delete(0, END)
    entrySetCustomAmethyst.delete(0, END)
    Generate(weapon, data)
    UpdateFile(data)
    pass
def updateCrafted(weapon, level):
    global chk80
    global chk120
    global chk160
    global chk200
    match level:
        case 80:
            if chk80.get():
                data["Legendaries"][weapon][str(level)]["Crafted"] = True
            else:
                data["Legendaries"][weapon][str(level)]["Crafted"] = False
                chk120.set(0)
                data["Legendaries"][weapon]["120"]["Crafted"] = False
                chk160.set(0)
                data["Legendaries"][weapon]["160"]["Crafted"] = False
                chk200.set(0)
                data["Legendaries"][weapon]["200"]["Crafted"] = False
            #print(f"chk80={chk80.get()}, {data["Legendaries"][weapon][str(level)]["Crafted"]}")
        case 120:
            if chk120.get():
                data["Legendaries"][weapon][str(level)]["Crafted"] = True
                chk80.set(1)
                data["Legendaries"][weapon]["80"]["Crafted"] = True
            else:
                data["Legendaries"][weapon][str(level)]["Crafted"] = False
                chk160.set(0)
                data["Legendaries"][weapon]["160"]["Crafted"] = False
                chk200.set(0)
                data["Legendaries"][weapon]["200"]["Crafted"] = False
            #print(f"chk120={chk120.get()}, {data["Legendaries"][weapon][str(level)]["Crafted"]}")
        case 160:
            if chk160.get():
                data["Legendaries"][weapon][str(level)]["Crafted"] = True
                chk80.set(1)
                data["Legendaries"][weapon]["80"]["Crafted"] = True
                chk120.set(1)
                data["Legendaries"][weapon]["120"]["Crafted"] = True
            else:
                data["Legendaries"][weapon][str(level)]["Crafted"] = False
                chk200.set(0)
                data["Legendaries"][weapon]["200"]["Crafted"] = False
            #print(f"chk160={chk160.get()}, {data["Legendaries"][weapon][str(level)]["Crafted"]}")
        case 200:
            if chk200.get():
                data["Legendaries"][weapon][str(level)]["Crafted"] = True
                chk80.set(1)
                data["Legendaries"][weapon]["80"]["Crafted"] = True
                chk120.set(1)
                data["Legendaries"][weapon]["120"]["Crafted"] = True
                chk160.set(1)
                data["Legendaries"][weapon]["160"]["Crafted"] = True
            else:
                data["Legendaries"][weapon][str(level)]["Crafted"] = False
            #print(f"chk80={chk200.get()}, {data["Legendaries"][weapon][str(level)]["Crafted"]}")
    
    Generate(weapon, data)
    UpdateFile(data)
def AmountCheck(level, weapon, material):

    CraftedMetal = 0
    CraftedObsidian = 0
    CraftedGold = 0
    CraftedAmethyst = 0
    
    if data["Legendaries"][weapon]["200"]["Crafted"] == True:
        c200 = True
        c160 = True
        c120 = True
        c80 = True

        CraftedMetal = data["Legendaries"][weapon]["80"]["Metal"]+data["Legendaries"][weapon]["120"]["Metal"]+data["Legendaries"][weapon]["160"]["Metal"]+data["Legendaries"][weapon]["80"]["Metal"]
        CraftedObsidian = data["Legendaries"][weapon]["80"]["Obsidian"]+data["Legendaries"][weapon]["120"]["Obsidian"]+data["Legendaries"][weapon]["160"]["Obsidian"]+data["Legendaries"][weapon]["200"]["Obsidian"]
        CraftedGold = data["Legendaries"][weapon]["80"]["Gold"]+data["Legendaries"][weapon]["120"]["Gold"]+data["Legendaries"][weapon]["160"]["Gold"]+data["Legendaries"][weapon]["200"]["Gold"]
        CraftedAmethyst = data["Legendaries"][weapon]["80"]["Amethyst"]+data["Legendaries"][weapon]["120"]["Amethyst"]+data["Legendaries"][weapon]["160"]["Amethyst"]+data["Legendaries"][weapon]["200"]["Amethyst"]

    elif data["Legendaries"][weapon]["160"]["Crafted"] == True:
        c200 = False
        c160 = True
        c120 = True
        c80 = True

        CraftedMetal = data["Legendaries"][weapon]["80"]["Metal"]+data["Legendaries"][weapon]["120"]["Metal"]+data["Legendaries"][weapon]["160"]["Metal"]
        CraftedObsidian = data["Legendaries"][weapon]["80"]["Obsidian"]+data["Legendaries"][weapon]["120"]["Obsidian"]+data["Legendaries"][weapon]["160"]["Obsidian"]
        CraftedGold = data["Legendaries"][weapon]["80"]["Gold"]+data["Legendaries"][weapon]["120"]["Gold"]+data["Legendaries"][weapon]["160"]["Gold"]
        CraftedAmethyst = data["Legendaries"][weapon]["80"]["Amethyst"]+data["Legendaries"][weapon]["120"]["Amethyst"]+data["Legendaries"][weapon]["160"]["Amethyst"]

    elif data["Legendaries"][weapon]["120"]["Crafted"] == True:
        c200 = False
        c160 = False
        c120 = True
        c80 = True

        CraftedMetal = data["Legendaries"][weapon]["80"]["Metal"]+data["Legendaries"][weapon]["120"]["Metal"]
        CraftedObsidian = data["Legendaries"][weapon]["80"]["Obsidian"]+data["Legendaries"][weapon]["120"]["Obsidian"]
        CraftedGold = data["Legendaries"][weapon]["80"]["Gold"]+data["Legendaries"][weapon]["120"]["Gold"]
        CraftedAmethyst = data["Legendaries"][weapon]["80"]["Amethyst"]+data["Legendaries"][weapon]["120"]["Amethyst"]

    elif data["Legendaries"][weapon]["80"]["Crafted"] == True:
        c200 = False
        c160 = False
        c120 = False
        c80 = True

        CraftedMetal = data["Legendaries"][weapon]["80"]["Metal"]
        CraftedObsidian = data["Legendaries"][weapon]["80"]["Obsidian"]
        CraftedGold = data["Legendaries"][weapon]["80"]["Gold"]
        CraftedAmethyst = data["Legendaries"][weapon]["80"]["Amethyst"]
        
    else:
        c200 = False
        c160 = False
        c120 = False
        c80 = False


    #print(locals()["Crafted" + material])
    match level:
        case 200:
            if c200 == False:
                if data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material] <= 0:
                    label = Label(text=f"{data["Legendaries"][weapon]["200"][material]} Held: 0 ({'{0:.2f}'.format(0)}%)", bg="firebrick1")
                elif data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material] < data["Legendaries"][weapon]["200"][material]/4:
                    label = Label(text=f"{data["Legendaries"][weapon]["200"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material]} ({'{0:.2f}'.format(((data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material])/data["Legendaries"][weapon]["200"][material])*100)}%)", bg="firebrick1")
                elif data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material] >= data["Legendaries"][weapon]["200"][material]/4 and not (data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material] >= data["Legendaries"][weapon]["200"][material]):
                    label = Label(text=f"{data["Legendaries"][weapon]["200"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material]} ({'{0:.2f}'.format(((data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material])/data["Legendaries"][weapon]["200"][material])*100)}%)", bg="orange")
                else:
                    label = Label(text=f"{data["Legendaries"][weapon]["200"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]-data["Legendaries"][weapon]["160"][material]+locals()["Crafted" + material]} (100%)", bg="lightgreen")
            else:
                label = Label(text="Already Crafted", bg="cyan2")
        case 160:
            if c160 == False:
                if data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material] <= 0:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["160"][material]} Held: 0 ({'{0:.2f}'.format(0)}%)", bg="firebrick1")
                elif data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material] < data["Legendaries"][weapon]["160"][material]/4:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["160"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material]} ({'{0:.2f}'.format(((data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material])/data["Legendaries"][weapon]["160"][material])*100)}%)", bg="firebrick1")
                elif data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material] >= data["Legendaries"][weapon]["160"][material]/4 and not (data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material] >= data["Legendaries"][weapon]["160"][material]):
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["160"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material]} ({'{0:.2f}'.format(((data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material])/data["Legendaries"][weapon]["160"][material])*100)}%)", bg="orange")
                else:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["160"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]-data["Legendaries"][weapon]["120"][material]+locals()["Crafted" + material]} (100%)", bg="lightgreen")
            else: 
                label = Label(text="Already Crafted", bg="cyan2")
        case 120:
            if c120 == False:
                if data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material] <= 0:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["120"][material]} Held: 0 ({'{0:.2f}'.format(0)}%)", bg="firebrick1")
                elif data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material] < data["Legendaries"][weapon]["120"][material]/4:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["120"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material]} ({'{0:.2f}'.format(((data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material])/data["Legendaries"][weapon]["120"][material])*100)}%)", bg="firebrick1")
                elif data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material] >= data["Legendaries"][weapon]["120"][material]/4 and not (data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material] >= data["Legendaries"][weapon]["120"][material]):
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["120"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material]} ({'{0:.2f}'.format(((data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material])/data["Legendaries"][weapon]["120"][material])*100)}%)", bg="orange")
                else:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["120"][material]} Held: {data["TotalMats"][material]-data["Legendaries"][weapon]["80"][material]+locals()["Crafted" + material]} (100%)", bg="lightgreen")
            else:
                label = Label(text="Already Crafted", bg="cyan2")
        case 80:
            if c80 == False:
                if data["TotalMats"][material] <= 0:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["80"][material]} Held: 0 ({'{0:.2f}'.format(0)}%)", bg="firebrick1")
                elif data["TotalMats"][material] < data["Legendaries"][weapon]["80"][material]/4:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["80"][material]} Held: {data["TotalMats"][material]} ({'{0:.2f}'.format(((data["TotalMats"][material])/data["Legendaries"][weapon]["80"][material])*100)}%)", bg="firebrick1")
                elif data["TotalMats"][material] >= data["Legendaries"][weapon]["80"][material]/4 and not (data["TotalMats"][material] >= data["Legendaries"][weapon]["80"][material]):
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["80"][material]} Held: {data["TotalMats"][material]} ({'{0:.2f}'.format(((data["TotalMats"][material])/data["Legendaries"][weapon]["80"][material])*100)}%)", bg="orange")
                else:
                    label = Label(text=f"Needed: {data["Legendaries"][weapon]["80"][material]} Held: {data["TotalMats"][material]} (100%)", bg="lightgreen")
            else:
                label = Label(text="Already Crafted", bg="cyan2")
        case _:
            label = Label(text="Already Crafted", bg="cyan2")
    return label
def Checkbox(level, weapon):
    box = Checkbutton(text="Crafted?", variable=globals()["chk"+str(level)])
    generate = lambda: updateCrafted(weapon, level)
    box.config(command=generate)
    if data["Legendaries"][weapon][str(level)]["Crafted"]:
        box.select()
    else:
        box.deselect()
    return box
def Generate(weapon, data):
    data["SelectedWeapon"] = weapon
    if data["SelectedWeapon"]=="Sword":
        buttonStaff.config(bg="white", relief=RAISED)
        buttonSword.config(bg="skyblue", relief=SUNKEN)
    elif data["SelectedWeapon"]=="Staff":
        buttonStaff.config(bg="skyblue", relief=SUNKEN)
        buttonSword.config(bg="white", relief=RAISED)
    #Level 80
    label80Mats = Label(text="lvl 80 Materials:")
    label80Mats.grid(row=0, column=1)

    label80Metal = AmountCheck(80, weapon, "Metal")
    label80Obsidian = AmountCheck(80, weapon, "Obsidian")
    label80Gold = AmountCheck(80, weapon, "Gold")
    label80Amethyst = AmountCheck(80, weapon, "Amethyst")

    #Level 120
    label120Mats = Label(text="lvl 120 Materials:")
    label120Mats.grid(row=0, column=2)

    label120Metal = AmountCheck(120, weapon, "Metal")
    label120Obsidian = AmountCheck(120, weapon, "Obsidian")
    label120Gold = AmountCheck(120, weapon, "Gold")
    label120Amethyst = AmountCheck(120, weapon, "Amethyst")

    #Level 160
    label160Mats = Label(text="lvl 160 Materials:")
    label160Mats.grid(row=0, column=3)

    label160Metal = AmountCheck(160, weapon, "Metal")
    label160Obsidian = AmountCheck(160, weapon, "Obsidian")
    label160Gold = AmountCheck(160, weapon, "Gold")
    label160Amethyst = AmountCheck(160, weapon, "Amethyst")

    #Level 200
    label200Mats = Label(text="lvl 200 Materials:")
    label200Mats.grid(row=0, column=4)

    label200Metal = AmountCheck(200, weapon, "Metal")
    label200Obsidian = AmountCheck(200, weapon, "Obsidian")
    label200Gold = AmountCheck(200, weapon, "Gold")
    label200Amethyst = AmountCheck(200, weapon, "Amethyst")

    #Crafted Checkboxes
    checkboxLvl80 = Checkbox(80, weapon)
    checkboxLvl120 = Checkbox(120, weapon)
    checkboxLvl160 = Checkbox(160, weapon)
    checkboxLvl200 = Checkbox(200, weapon)

    label80Metal.grid(row=1, column=1, sticky="nsew")
    label80Obsidian.grid(row=2, column=1, sticky="nsew")
    label80Gold.grid(row=3, column=1, sticky="nsew")
    label80Amethyst.grid(row=4, column=1, sticky="nsew")

    label120Metal.grid(row=1, column=2, sticky="nsew")
    label120Obsidian.grid(row=2, column=2, sticky="nsew")
    label120Gold.grid(row=3, column=2, sticky="nsew")
    label120Amethyst.grid(row=4, column=2, sticky="nsew")

    label160Metal.grid(row=1, column=3, sticky="nsew")
    label160Obsidian.grid(row=2, column=3, sticky="nsew")
    label160Gold.grid(row=3, column=3, sticky="nsew")
    label160Amethyst.grid(row=4, column=3, sticky="nsew")

    label200Metal.grid(row=1, column=4, sticky="nsew")
    label200Obsidian.grid(row=2, column=4, sticky="nsew")
    label200Gold.grid(row=3, column=4, sticky="nsew")
    label200Amethyst.grid(row=4, column=4, sticky="nsew")

    checkboxLvl80.grid(row=5, column=1)
    checkboxLvl120.grid(row=5, column=2)
    checkboxLvl160.grid(row=5, column=3)
    checkboxLvl200.grid(row=5, column=4)

    UpdateFile(data)
def callback(input):
    if input.isdigit():
        return True
                        
    elif input is "":
        return True

    else:
        return False

window = Tk()
chk80 = IntVar()
chk120 = IntVar()
chk160 = IntVar()
chk200 = IntVar()

with open('greggfarmingmats.json', 'r') as f:
    data = json.load(f)

labelMetal = Label(text="Metal:")
labelObsidian = Label(text="Obsidian:")
labelGold = Label(text="Gold:")
labelAmethyst = Label(text="Amethyst:")

labelMetal.grid(row=1, column=0)
labelObsidian.grid(row=2, column=0)
labelGold.grid(row=3, column=0)
labelAmethyst.grid(row=4, column=0)

generateStaff = lambda: Generate("Staff", data)
buttonStaff= Button(text="Staff", command=generateStaff)
buttonStaff.grid(row=6, column=0, columnspan=2)

generateSword = lambda: Generate("Sword", data)
buttonSword = Button(text="Sword", command=generateSword)
buttonSword.grid(row=6, column=2, columnspan=2)

labelAddMats = Label(text="Add Materials:")
labelAddMats.grid(row=0, column=5, columnspan=7)

vcmd = window.register(callback)

entryAddCustomMetal = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))
entryAddCustomObsidian = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))
entryAddCustomGold = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))
entryAddCustomAmethyst = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))

entryAddCustomMetal.grid(row=1, column=10)
entryAddCustomObsidian.grid(row=2, column=10)
entryAddCustomGold.grid(row=3, column=10)
entryAddCustomAmethyst.grid(row=4, column=10)

entrySetCustomMetal = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))
entrySetCustomObsidian = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))
entrySetCustomGold = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))
entrySetCustomAmethyst = Entry(width=3, font=("arial", 20), validate = "all", validatecommand=(vcmd, "%P"))

entrySetCustomMetal.grid(row=1, column=12)
entrySetCustomObsidian.grid(row=2, column=12)
entrySetCustomGold.grid(row=3, column=12)
entrySetCustomAmethyst.grid(row=4, column=12)


#Add Metal
add1metal= lambda: addMats("Metal", 1, data["SelectedWeapon"])
buttonAdd1Metal = Button(text="+1", command=add1metal, padx=5, pady=5)
buttonAdd1Metal.grid(row=1, column=5)

add2metal= lambda: addMats("Metal", 2, data["SelectedWeapon"])
buttonAdd2Metal = Button(text="+2", command=add2metal, padx=5, pady=5)
buttonAdd2Metal.grid(row=1, column=6)

add3metal= lambda: addMats("Metal", 3, data["SelectedWeapon"])
buttonAdd3Metal = Button(text="+3", command=add3metal, padx=5, pady=5)
buttonAdd3Metal.grid(row=1, column=7)

add4metal= lambda: addMats("Metal", 4, data["SelectedWeapon"])
buttonAdd4Metal = Button(text="+4", command=add4metal, padx=5, pady=5)
buttonAdd4Metal.grid(row=1, column=8)

add6metal= lambda: addMats("Metal", 6, data["SelectedWeapon"])
buttonAdd6Metal = Button(text="+6", command=add6metal, padx=5, pady=5)
buttonAdd6Metal.grid(row=1, column=9)


#Add Obsidian
add1Obsidian= lambda: addMats("Obsidian", 1, data["SelectedWeapon"])
buttonAdd1Obsidian = Button(text="+1", command=add1Obsidian, padx=5, pady=5)
buttonAdd1Obsidian.grid(row=2, column=5)

add2Obsidian= lambda: addMats("Obsidian", 2, data["SelectedWeapon"])
buttonAdd2Obsidian = Button(text="+2", command=add2Obsidian, padx=5, pady=5)
buttonAdd2Obsidian.grid(row=2, column=6)

add3Obsidian= lambda: addMats("Obsidian", 3, data["SelectedWeapon"])
buttonAdd3Obsidian = Button(text="+3", command=add3Obsidian, padx=5, pady=5)
buttonAdd3Obsidian.grid(row=2, column=7)

add4Obsidian= lambda: addMats("Obsidian", 4, data["SelectedWeapon"])
buttonAdd4Obsidian = Button(text="+4", command=add4Obsidian, padx=5, pady=5)
buttonAdd4Obsidian.grid(row=2, column=8)

add6Obsidian= lambda: addMats("Obsidian", 6, data["SelectedWeapon"])
buttonAdd6Obsidian = Button(text="+6", command=add6Obsidian, padx=5, pady=5)
buttonAdd6Obsidian.grid(row=2, column=9)

#Gold
add1Gold= lambda: addMats("Gold", 1, data["SelectedWeapon"])
buttonAdd1Gold = Button(text="+1", command=add1Gold, padx=5, pady=5)
buttonAdd1Gold.grid(row=3, column=5)

add2Gold= lambda: addMats("Gold", 2, data["SelectedWeapon"])
buttonAdd2Gold = Button(text="+2", command=add2Gold, padx=5, pady=5)
buttonAdd2Gold.grid(row=3, column=6)

add3Gold= lambda: addMats("Gold", 3, data["SelectedWeapon"])
buttonAdd3Gold = Button(text="+3", command=add3Gold, padx=5, pady=5)
buttonAdd3Gold.grid(row=3, column=7)

add4Gold= lambda: addMats("Gold", 4, data["SelectedWeapon"])
buttonAdd4Gold = Button(text="+4", command=add4Gold, padx=5, pady=5)
buttonAdd4Gold.grid(row=3, column=8)

add6Gold= lambda: addMats("Gold", 6, data["SelectedWeapon"])
buttonAdd6Gold = Button(text="+6", command=add6Gold, padx=5, pady=5)
buttonAdd6Gold.grid(row=3, column=9)

#Amethyst
add1Amethyst= lambda: addMats("Amethyst", 1, data["SelectedWeapon"])
buttonAdd1Amethyst = Button(text="+1", command=add1Amethyst, padx=5, pady=5)
buttonAdd1Amethyst.grid(row=4, column=5)

add2Amethyst= lambda: addMats("Amethyst", 2, data["SelectedWeapon"])
buttonAdd2Amethyst = Button(text="+2", command=add2Amethyst, padx=5, pady=5)
buttonAdd2Amethyst.grid(row=4, column=6)

add3Amethyst= lambda: addMats("Amethyst", 3, data["SelectedWeapon"])
buttonAdd3Amethyst = Button(text="+3", command=add3Amethyst, padx=5, pady=5)
buttonAdd3Amethyst.grid(row=4, column=7)

add4Amethyst= lambda: addMats("Amethyst", 4, data["SelectedWeapon"])
buttonAdd4Amethyst = Button(text="+4", command=add4Amethyst, padx=5, pady=5)
buttonAdd4Amethyst.grid(row=4, column=8)

add6Amethyst= lambda: addMats("Amethyst", 6, data["SelectedWeapon"])
buttonAdd6Amethyst = Button(text="+6", command=add6Amethyst, padx=5, pady=5)
buttonAdd6Amethyst.grid(row=4, column=9)

addCustomMetal = lambda: addMats("Metal", int(entryAddCustomMetal.get()), data["SelectedWeapon"])
buttonAddCustomMetal = Button(text="<Add Custom", command=addCustomMetal, padx=5, pady=5)
buttonAddCustomMetal.grid(row=1, column=11)

addCustomObsidian = lambda: addMats("Obsidian", int(entryAddCustomObsidian.get()), data["SelectedWeapon"])
buttonAddCustomObsidian = Button(text="<Add Custom", command=addCustomObsidian, padx=5, pady=5)
buttonAddCustomObsidian.grid(row=2, column=11)

addCustomGold = lambda: addMats("Gold", int(entryAddCustomGold.get()), data["SelectedWeapon"])
buttonAddCustomGold = Button(text="<Add Custom", command=addCustomGold, padx=5, pady=5)
buttonAddCustomGold.grid(row=3, column=11)

addCustomAmethyst = lambda: addMats("Amethyst", int(entryAddCustomAmethyst.get()), data["SelectedWeapon"])
buttonAddCustomAmethyst = Button(text="<Add Custom", command=addCustomAmethyst, padx=5, pady=5)
buttonAddCustomAmethyst.grid(row=4, column=11)

setCustomMetal = lambda: setMats("Metal", int(entrySetCustomMetal.get()), data["SelectedWeapon"])
buttonSetCustomMetal = Button(text="<Set Custom", command=setCustomMetal, padx=5, pady=5)
buttonSetCustomMetal.grid(row=1, column=13)

setCustomObsidian = lambda: setMats("Obsidian", int(entrySetCustomObsidian.get()), data["SelectedWeapon"])
buttonSetCustomObsidian = Button(text="<Set Custom", command=setCustomObsidian, padx=5, pady=5)
buttonSetCustomObsidian.grid(row=2, column=13)

setCustomGold = lambda: setMats("Gold", int(entrySetCustomGold.get()), data["SelectedWeapon"])
buttonSetCustomGold = Button(text="<Set Custom", command=setCustomGold, padx=5, pady=5)
buttonSetCustomGold.grid(row=3, column=13)

setCustomAmethyst = lambda: setMats("Amethyst", int(entrySetCustomAmethyst.get()), data["SelectedWeapon"])
buttonSetCustomAmethyst = Button(text="<Set Custom", command=setCustomAmethyst, padx=5, pady=5)
buttonSetCustomAmethyst.grid(row=4, column=13)
Generate(data["SelectedWeapon"], data)
window.mainloop()