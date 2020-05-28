visitingNPC = False # Keep track of whether the player is visiting the npc (going to the same square as the npc)

# Basic classes - could probably be added to another file and used as a proper python library
class player:
    def __init__(self, posX, posY, inventory):
        self.posX = posX
        self.posY = posY
        self.inventory = inventory # Items in the inventory will look like: [["Axe", ["Weapon", "Tool"]], ["Fish", ["Food"]]]

    def moveForward(self, amount):
        self.posY -= amount

    def moveBackward(self, amount):
        self.posY += amount

    def moveLeft(self, amount):
        self.posX += amount

    def moveRight(self, amount):
        self.posX -= amount

class canvas:
    def __init__(self, width, height, playerPosX, playerPosY, playerInventory):
        self.width = width
        self.height = height
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.playerInventory = playerInventory # For an inventory at the bottom of the screen

    def resetPlayer(self, playerPosX, playerPosY, playerInventory): # To reset the positions of the character, etc
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.playerInventory = playerInventory

    def printCanvas(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if x == self.playerPosX and y == self.playerPosY:
                    print("#", end="")

                elif x == 15 and y == 5:
                    print("@", end="")

                else:
                    print("`", end="")

                # If you go to the NPC:
                if self.playerPosX == 15 and self.playerPosY == 5:
                   visitingNPC = True

                else:
                    visitingNPC = False

            print()

        print()

        # Display the items in the players inventory:
        print("Inventory: ", end="")
        for i in range(0, len(self.playerInventory)):
            print(self.playerInventory[i][0])
    
        print()

        if visitingNPC == True:
            fishInInventory = False
            for i in range(0, len(self.playerInventory)):
                if "Fish" in self.playerInventory[i]: # The NPC has already given you a fish.
                    print("Hello again!")
                    fishInInventory = True
			
            if fishInInventory == False: # The NPC hasn't given you a fish yet.
                print("NPC: Hello - I would like to give you a gift to help you in your journey.")
                print("(The NPC gives you a Fish.)")
                inventoryItem = ["Fish", ["Food"]]
                self.playerInventory.append(inventoryItem)

# Game Logic
mainPlayer = player(10, 0, [])
mainCanvas = canvas(40, 10, mainPlayer.posX, mainPlayer.posY, mainPlayer.inventory)
mainCanvas.printCanvas()

while True:
    command = input("Please enter either W, S, A, D: ")

    if command == "w" or command == "W":
        mainPlayer.moveForward(1)
        mainCanvas.resetPlayer(mainPlayer.posX, mainPlayer.posY, mainPlayer.inventory)
        mainCanvas.printCanvas()

    elif command == "s" or command == "S":
        mainPlayer.moveBackward(1)
        mainCanvas.resetPlayer(mainPlayer.posX, mainPlayer.posY, mainPlayer.inventory)
        mainCanvas.printCanvas()

    
    elif command == "a" or command == "A":
        mainPlayer.moveRight(1)
        mainCanvas.resetPlayer(mainPlayer.posX, mainPlayer.posY, mainPlayer.inventory)
        mainCanvas.printCanvas()

    
    elif command == "d" or command == "D":
        mainPlayer.moveLeft(1)
        mainCanvas.resetPlayer(mainPlayer.posX, mainPlayer.posY, mainPlayer.inventory)
        mainCanvas.printCanvas()

    else:
        print("Unknown input.")
