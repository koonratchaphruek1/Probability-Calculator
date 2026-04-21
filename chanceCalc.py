def OutputResult(roll, dicton, chance):
    lineSeparate = "=====================================" # 37=

    itemPrint = ""
    for i in range(len(dicton)):
        if i > 0:
            itemPrint+= ", "
            lineSeparate += "=="

        itemPrint += list(dicton.keys())[i]
        for i in range(len(list(dicton.keys())[i])):
            lineSeparate += "="

    print("\n"+lineSeparate)
    print(f'The chance of getting {itemPrint} in {roll} rolls is\n = 1 in {chance}')
    print(lineSeparate+"\n")

# calculate chance
def CalcChance(roll, dicton):
    numItem = len(dicton)
    chance = 0
    for i in range(numItem):
        chance += 100/list(dicton.values())[i]
    chance *= (.5/numItem) * roll
        
    OutputResult(roll, dicton, chance)

# get inputs for tries & chances
def GetInput(items):
    roll = int(input("🌹Input amount of rolls: "))
    """
        chance format as : 1 in x
        ‼️emojis added to print for testing purpose only (I don't wanna read)
    """
    dicton = {}
    i=0
    while i < items:
        i+=1
        try:
            item, chance = input("🛞 Input item name & chance: ").split()
            dicton.update({str(item): int(chance)})

        except:
            print("❌invalid inputs, try again")
            i -= 1
    
    CalcChance(roll, dicton)

GetInput(int(input("🔢Input num of items: ")))