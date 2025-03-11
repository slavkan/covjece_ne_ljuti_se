import os
import pygame
import random
import sys


def mainMenu(screen, clock, fontPick):
    pickedOption = 0
    textsToPrint = ["Igraj", "Pravila", "Izlaz"]
    colorBackground = [253, 255, 252]
    colorPicked = [227, 23, 10]
    colorNotPicked = [18, 22, 25]
    binds = pygame.image.load(os.path.join("images", "bindsMainMenu.png")).convert()
    while True:
        clock.tick(30)
        screen.fill(colorBackground)
        optionText = []
        for i in range(3):
            if i != pickedOption:
                optionText.append(fontPick.render(textsToPrint[i], True, colorNotPicked))
            else:
                optionText.append(fontPick.render(textsToPrint[i], True, colorPicked))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pickedOption += 1
                    if pickedOption > 2:
                        pickedOption = 0
                if event.key == pygame.K_UP:
                    pickedOption -= 1
                    if pickedOption < 0:
                        pickedOption = 2
                if event.key == pygame.K_RETURN:
                    if pickedOption == 0:
                        preGameLoop(screen, clock, fontPick)
                    if pickedOption == 1:
                        rules(screen, clock)
                    if pickedOption == 2:
                        sys.exit()
        screen.blit(binds, (0, 804))
        for i in range(3):
            screen.blit(optionText[i], (0, i * 100))
        pygame.display.update()


def rules(screen, clock):
    background = pygame.image.load(os.path.join("images", "rulesBackground.png")).convert()
    waiting = True
    while waiting:
        screen.blit(background, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainMenu(screen, clock, pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 90))


def preGameLoop(screen, clock, fontPick):
    fontSmall = pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 30)
    pickedOption = 0
    colorNotPicked = [18, 22, 25]
    colorPicked = [227, 23, 10]
    imagePawn = []
    playerControl = [[1, "Crveni"], [1, "Plavi"], [0, "Zeleni"], [0, "Žuti"]]
    strTemp = ""
    binds = pygame.image.load(os.path.join("images", "bindsPreGameLoop.png")).convert()

    imagePawn.append(pygame.image.load(os.path.join("images", "pawnRed.png")).convert())
    imagePawn[0].set_colorkey((0, 0, 0))
    imagePawn.append(pygame.image.load(os.path.join("images", "pawnBlue.png")).convert())
    imagePawn[1].set_colorkey((0, 0, 0))
    imagePawn.append(pygame.image.load(os.path.join("images", "pawnGreen.png")).convert())
    imagePawn[2].set_colorkey((0, 0, 0))
    imagePawn.append(pygame.image.load(os.path.join("images", "pawnYellow.png")).convert())
    imagePawn[3].set_colorkey((0, 0, 0))
    while True:
        optionText = []
        playerControlDisplayText = []
        colorBackground = [253, 255, 252]
        clock.tick(30)
        screen.fill(colorBackground)
        for i in range(5):
            if i < 4:
                if playerControl[i][0] == 0:
                    strTemp = "Tip igrača: Prazno"
                elif playerControl[i][0] == 1:
                    strTemp = "Tip igrača: Igrač"
                if i != pickedOption:
                    optionText.append(pygame.draw.rect(screen, colorNotPicked, pygame.Rect(50, 50 + (i * 100), 500, 80), 2))
                    screen.blit(imagePawn[i], (60, 60 + (i * 100)))
                    playerControlDisplayText.append(fontSmall.render(strTemp, True, colorNotPicked))
                    screen.blit(playerControlDisplayText[i], (125, 70 + (i * 100)))
                else:
                    optionText.append(pygame.draw.rect(screen, colorPicked, pygame.Rect(50, 50 + (i * 100), 500, 80), 2))
                    screen.blit(imagePawn[i], (60, 60 + (i * 100)))
                    playerControlDisplayText.append(fontSmall.render(strTemp, True, colorPicked))
                    screen.blit(playerControlDisplayText[i], (125, 70 + (i * 100)))
            if i == 4:
                if i != pickedOption:
                    optionText.append(fontPick.render("Pokreni igru", True, colorNotPicked))
                else:
                    optionText.append(fontPick.render("Pokreni igru", True, colorPicked))
        screen.blit(optionText[4], (45, 440))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    mainMenu(screen, clock, fontPick)
                if event.key == pygame.K_RETURN and pickedOption == 4:
                    anyonePlaying = False
                    for i in range(4):
                        if playerControl[i][0] > 0:
                            anyonePlaying = True
                    if anyonePlaying:
                        for i in range(4):
                            if playerControl[i][0] == 1:
                                playerControl[i][1] += " Igrač"
                        gameLoop(screen, clock, playerControl)
                if event.key == pygame.K_DOWN:
                    pickedOption += 1
                    if pickedOption > 4:
                        pickedOption = 0
                if event.key == pygame.K_UP:
                    pickedOption -= 1
                    if pickedOption < 0:
                        pickedOption = 4
                if event.key == pygame.K_RIGHT and pickedOption != 4:
                    playerControl[pickedOption][0] += 1
                    if playerControl[pickedOption][0] > 1:
                        playerControl[pickedOption][0] = 0
                if event.key == pygame.K_LEFT and pickedOption != 4:
                    playerControl[pickedOption][0] -= 1
                    if playerControl[pickedOption][0] < 0:
                        playerControl[pickedOption][0] = 1
                if event.key == pygame.K_ESCAPE:
                    mainMenu(screen, clock, fontPick)
        screen.blit(binds, (0, 804))
        pygame.display.update()


def gameLoop(screen, clock, playerControl):
    roll = 0
    colorNotPicked = [18, 22, 25]  # CRNA
    colorWhite = [253, 255, 252]
    colorPlayer = [[219, 34, 42], [0, 78, 152], [76, 185, 68], [240, 200, 8]]
    colorName = ["Crveni", "Plavi", "Zeleni", "Zuti"]
    fontSmall = pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 30)
    msgDiceWait = fontSmall.render("Bacite kocku:", True, colorNotPicked)
    msgMovesLeft = []
    msgMovesLeft.append(fontSmall.render("Broj pokušaja: 1", True, colorNotPicked))
    msgMovesLeft.append(fontSmall.render("Broj pokušaja: 2", True, colorNotPicked))
    msgMovesLeft.append(fontSmall.render("Broj pokušaja: 3", True, colorNotPicked))
    imagePawn = []
    imagePawn.append(pygame.image.load(os.path.join("images", "pawnRed.png")).convert())
    imagePawn[0].set_colorkey((0, 0, 0))
    imagePawn.append(pygame.image.load(os.path.join("images", "pawnBlue.png")).convert())
    imagePawn[1].set_colorkey((0, 0, 0))
    imagePawn.append(pygame.image.load(os.path.join("images", "pawnGreen.png")).convert())
    imagePawn[2].set_colorkey((0, 0, 0))
    imagePawn.append(pygame.image.load(os.path.join("images", "pawnYellow.png")).convert())
    imagePawn[3].set_colorkey((0, 0, 0))
    background = pygame.image.load(os.path.join("images", "background.png")).convert()
    binds = pygame.image.load(os.path.join("images", "bindsGameLoop.png")).convert()
    screen.blit(background, (0, 0))
    screen.blit(binds, (0, 804))
    playerVars = [[playerControl[0][0], [0, 0, 0, 0], [-1, -1, -1, -1], [1, 1, 1, 1], False],
                  [playerControl[1][0], [0, 0, 0, 0], [-1, -1, -1, -1], [0, 0, 0, 0], False],
                  [playerControl[2][0], [0, 0, 0, 0], [-1, -1, -1, -1], [0, 0, 0, 0], False],
                  [playerControl[3][0], [0, 0, 0, 0], [-1, -1, -1, -1], [0, 0, 0, 0], False]]
    locationBase = [[[12, 12], [84, 12], [12, 84], [84, 84]],
                    [[660, 12], [732, 12], [660, 84], [732, 84]],
                    [[660, 660], [732, 660], [660, 732], [732, 732]],
                    [[12, 660], [84, 660], [12, 732], [84, 732]]]
    locationField = [[12, 300], [84, 300], [156, 300], [228, 300], [300, 300], [300, 228], [300, 156], [300, 84], [300, 12], [372, 12],
                     [444, 12], [444, 84], [444, 156], [444, 228], [444, 300], [516, 300], [588, 300], [660, 300], [732, 300], [732, 372],
                     [732, 444], [660, 444], [588, 444], [516, 444], [444, 444], [444, 516], [444, 588], [444, 660], [444, 732], [372, 732],
                     [300, 732], [300, 660], [300, 588], [300, 516], [300, 444], [228, 444], [156, 444], [84, 444], [12, 444], [12, 372]]
    locationHome = []
    locationHome = addLocHome(locationHome)
    msgPlayer = []
    for i in range(4):
        screen.blit(binds, (0, 804))
        # ISPISIVANJE FIGURICA NA PRAVIM POZICIJAMA i PRAVLJENJE PORUKA "IGRAC JE NA POTEZU"
        if playerVars[i][0] == 1 or playerVars[i][0] == 2:
            for j in range(4):
                if playerVars[i][1][j] == 0:
                    screen.blit(imagePawn[i], (locationBase[i][j][0], locationBase[i][j][1]))
        if playerVars[i][0] == 1:
            msgPlayer.append(fontSmall.render(str(colorName[i]) + " igrač je na potezu:", True, colorPlayer[i]))
        else:
            msgPlayer.append(fontSmall.render(str(colorName[i]) + " CPU je na potezu:", True, colorPlayer[i]))
    i = whoGoesFirst(screen, clock, playerVars, fontSmall)
    # Kod Igre
    while True:
        # POCETAK POTEZA, VARIJABLA i JE INDEX IGRACA, VRIJEDNOSTI CE MU BIT (0, 1, 2, 3, 0, 1, 2, 3, ...)
        while i < 10:
            movedWithSix = False
            # AKO JE IGRAC ILI CPU UDJI U POTEZ
            if playerVars[i][0] == 1 or playerVars[i][0] == 2:
                # ISPISIVANJE FIGURICA NA KRUGOVIMA
                for igrac in range(4):
                    if playerVars[igrac][0] == 1 or playerVars[igrac][0] == 2 or playerVars[igrac][4]:
                        for j in range(4):
                            if playerVars[igrac][1][j] == 0:
                                screen.blit(imagePawn[igrac], (locationBase[igrac][j][0], locationBase[igrac][j][1]))
                            elif playerVars[igrac][1][j] == 1:
                                screen.blit(imagePawn[igrac], (locationField[playerVars[igrac][2][j]], locationField[playerVars[igrac][2][j]]))
                            elif playerVars[igrac][1][j] == 2 or playerVars[igrac][4]:
                                screen.blit(imagePawn[igrac], (locationHome[playerVars[igrac][2][j]][0], locationHome[playerVars[igrac][2][j]][1]))

                # BACANJE KOCKE
                waitingForDice = 0
                roll = 0
                pawnsOnField = False
                for j in range(4):
                    if playerVars[i][1][j] == 1:
                        pawnsOnField = True
                if pawnsOnField:
                    waitingForDice = 1
                else:
                    waitingForDice = 3
                while waitingForDice > 0:
                    clock.tick(30)
                    pygame.draw.rect(screen, colorWhite, pygame.Rect(804, 0, 626, 804))
                    screen.blit(msgPlayer[i], (820, 20))
                    screen.blit(msgDiceWait, (820, 80))
                    screen.blit(msgMovesLeft[waitingForDice - 1], (820, 210))
                    if waitingForDice == 2 or waitingForDice == 1 and roll != 0:
                        msgYouGot = fontSmall.render("Dobili ste: " + str(roll), True, colorNotPicked)
                        pygame.draw.rect(screen, colorWhite, pygame.Rect(804, 0, 626, 804))
                        screen.blit(msgPlayer[i], (820, 20))
                        screen.blit(msgDiceWait, (820, 80))
                        screen.blit(msgYouGot, (820, 110))
                        screen.blit(msgMovesLeft[waitingForDice - 1], (820, 210))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.KEYDOWN and playerVars[i][0] == 1:
                            # Programian SPACE za random i (NUMPAD_12456) na (123456)
                            if event.key == pygame.K_SPACE:
                                roll = random.randint(1, 6)
                                waitingForDice -= 1
                                if roll == 6:
                                    waitingForDice = 0
                            if event.key == pygame.K_KP_1:
                                roll = 1
                                waitingForDice -= 1
                            if event.key == pygame.K_KP_2:
                                roll = 2
                                waitingForDice -= 1
                            if event.key == pygame.K_KP_3:
                                roll = 3
                                waitingForDice -= 1
                            if event.key == pygame.K_KP_4:
                                roll = 4
                                waitingForDice -= 1
                            if event.key == pygame.K_KP_5:
                                roll = 5
                                waitingForDice -= 1
                            if event.key == pygame.K_KP_6:
                                roll = 6
                                waitingForDice = 0
                            if event.key == pygame.K_ESCAPE:
                                mainMenu(screen, clock, pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 90))
                    pygame.display.update()
                # RACUNANJE LEGALNIH POTEZA
                legalMovesBase = [False, False, False, False]
                legalMovesField = [False, False, False, False]
                legalMovesList = [False, False, False, False]
                legalMovesAny = False
                baseFree = True
                # Koje figurice se mogu izvaditi iz baze (za sve)
                if roll == 6:
                    for j in range(4):
                        if playerVars[i][2][j] == 10 * i and playerVars[i][1][j] == 1:
                            baseFree = False
                    if baseFree:
                        for j in range(4):
                            if playerVars[i][1][j] == 0:
                                legalMovesBase[j] = True
                # Koje izvadjenje figurice se mogu pomaknuti (crveni)
                if i == 0:
                    for j in range(4):
                        if playerVars[i][1][j] == 1:
                            legalMovesField[j] = True
                            for k in range(4):
                                if playerVars[i][2][j] + roll == playerVars[i][2][k] or playerVars[i][2][j] + roll > 43:
                                    legalMovesField[j] = False
                # Koje izvadjenje figurice se mogu pomaknuti (ostali)
                else:
                    for j in range(4):
                        if playerVars[i][1][j] == 1:
                            legalMovesField[j] = True
                            if playerVars[i][2][j] + roll > (i * 10) + 3 and playerVars[i][3][j] == 1:
                                legalMovesField[j] = False
                            for k in range(4):
                                if playerVars[i][2][j] + roll == playerVars[i][2][k] and playerVars[i][3][j] == playerVars[i][3][k]:
                                    legalMovesField[j] = False
                                if playerVars[i][2][j] + roll == playerVars[i][2][k] + 40 and playerVars[i][3][j] == 0 and playerVars[i][3][k] == 1:
                                    legalMovesField[j] = False
                # Stavljanje svih figurica koje se mogu pomaknuti u jednu varijablu legalMovesList
                for index in range(4):
                    if legalMovesBase[index] or legalMovesField[index]:
                        legalMovesList[index] = True
                        legalMovesAny = True
                # ISPIS LEGALNIH I CEKANJE NA POTEZ
                msgMove = []
                for j in range(4):
                    msgMove.append(fontSmall.render(str(j + 1), True, colorWhite))
                msgYouGot = fontSmall.render("Dobili ste: " + str(roll), True, colorNotPicked)
                waitingForMove = True
                if legalMovesAny:
                    msgYouCanPlay1 = fontSmall.render("Pomaknite figuricu", True, colorNotPicked)
                    # msgYouCanPlay2 = fontSmall.render("se nalazi pored figurice", True, colorNotPicked)
                    while waitingForMove:
                        clock.tick(30)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1 and legalMovesList[0]:
                                    playerVars, movedWithSix = pawnMove(i, 0, playerVars, roll)
                                    waitingForMove = False
                                if event.key == pygame.K_2 and legalMovesList[1]:
                                    playerVars, movedWithSix = pawnMove(i, 1, playerVars, roll)
                                    waitingForMove = False
                                if event.key == pygame.K_3 and legalMovesList[2]:
                                    playerVars, movedWithSix = pawnMove(i, 2, playerVars, roll)
                                    waitingForMove = False
                                if event.key == pygame.K_4 and legalMovesList[3]:
                                    playerVars, movedWithSix = pawnMove(i, 3, playerVars, roll)
                                    waitingForMove = False
                                if event.key == pygame.K_ESCAPE:
                                    mainMenu(screen, clock, pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 90))
                            if event.type == pygame.QUIT:
                                sys.exit()
                        for j in range(4):
                            if legalMovesList[j]:
                                if playerVars[i][1][j] == 0:
                                    screen.blit(msgMove[j], (locationBase[i][j][0] + 22, locationBase[i][j][1] + 12))
                                elif playerVars[i][1][j] == 1:
                                    screen.blit(msgMove[j], (locationField[playerVars[i][2][j]][0] + 22, locationField[playerVars[i][2][j]][1] + 12))
                        pygame.draw.rect(screen, colorWhite, pygame.Rect(804, 0, 626, 804))
                        screen.blit(msgPlayer[i], (820, 20))
                        screen.blit(msgYouGot, (820, 110))
                        screen.blit(msgYouCanPlay1, (820, 210))
                        # screen.blit(msgYouCanPlay2, (820, 200))
                        pygame.display.update()
                else:
                    msgNotLegal1 = fontSmall.render("Nemate legalnih poteza za odigrati", True, colorNotPicked)
                    # msgNotLegal2 = fontSmall.render("pritisnite SPACE da zavrsite svoj potez", True, colorNotPicked)
                    while waitingForMove:
                        clock.tick(30)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    waitingForMove = False
                                if event.key == pygame.K_ESCAPE:
                                    mainMenu(screen, clock,
                                             pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 90))
                            if event.type == pygame.QUIT:
                                sys.exit()
                        pygame.draw.rect(screen, colorWhite, pygame.Rect(804, 0, 626, 804))
                        screen.blit(msgPlayer[i], (820, 20))
                        screen.blit(msgYouGot, (820, 110))
                        screen.blit(msgNotLegal1, (820, 210))
                        # screen.blit(msgNotLegal2, (820, 200))
                        pygame.display.update()

            # ZAVRSETAK POTEZA, POSTAVLJANJE i VARIJABLE ZA SLJEDECEG IGRACA
            playersNotPlaying = 0
            allFourDone = True
            for j in range(4):
                if playerVars[i][1][j] != 2:
                    allFourDone = False
            for j in range(4):
                if playerVars[j][0] == 0 or playerVars[j][4]:
                    playersNotPlaying += 1
            if allFourDone:
                playerVars[i][0] = 0
                playerVars[i][4] = True
            i += 1
            if movedWithSix:
                i -= 1
            if i >= 4:
                i = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.blit(background, (0, 0))
            pygame.display.update()
            while playersNotPlaying >= 4:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            mainMenu(screen, clock, pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 90))
                screen.blit(background, (0, 0))
                screen.blit(binds, (0, 804))
                for igrac in range(4):
                    for j in range(4):
                        if playerVars[igrac][1][j] == 2 or playerVars[igrac][4] == True:
                            screen.blit(imagePawn[igrac], (
                                locationHome[playerVars[igrac][2][j]][0], locationHome[playerVars[igrac][2][j]][1]))
                pygame.display.update()
            pygame.display.update()


def pawnMove(playerIndex, pawnIndex, playerVars, roll):
    movedWithSix = False
    # Pomicanje figurica (crvenih)
    if playerIndex == 0:
        if playerVars[playerIndex][1][pawnIndex] == 0:
            playerVars[playerIndex][1][pawnIndex] = 1
            playerVars[playerIndex][2][pawnIndex] = playerIndex * 10
            # Provjeri jel crveni jede koga
            for playerToEat in range(4):
                if playerToEat != playerIndex:
                    for pawnToEat in range(4):
                        if playerVars[playerToEat][1][pawnToEat] == 1:
                            if playerVars[playerToEat][2][pawnToEat] == playerVars[playerIndex][2][pawnIndex]:
                                playerVars[playerToEat][1][pawnToEat] = 0
                                playerVars[playerToEat][2][pawnToEat] = -1
                                playerVars[playerToEat][3][pawnToEat] = 0
        else:
            if playerIndex == 0:
                if playerVars[playerIndex][2][pawnIndex] + roll <= 39:
                    playerVars[playerIndex][2][pawnIndex] += roll
                    # Provjeri jel crveni jede koga
                    for playerToEat in range(4):
                        if playerToEat != playerIndex:
                            for pawnToEat in range(4):
                                if playerVars[playerToEat][1][pawnToEat] == 1:
                                    if playerVars[playerToEat][2][pawnToEat] == playerVars[playerIndex][2][pawnIndex]:
                                        playerVars[playerToEat][1][pawnToEat] = 0
                                        playerVars[playerToEat][2][pawnToEat] = -1
                                        playerVars[playerToEat][3][pawnToEat] = 0
                elif playerVars[playerIndex][2][pawnIndex] + roll >= 40:
                    playerVars[playerIndex][2][pawnIndex] += roll
                    playerVars[playerIndex][1][pawnIndex] = 2
                if roll == 6:
                    movedWithSix = True
    # Pomicanje figurica (ostalih)
    else:
        if playerVars[playerIndex][1][pawnIndex] == 0:
            playerVars[playerIndex][1][pawnIndex] = 1
            playerVars[playerIndex][2][pawnIndex] = playerIndex * 10
            playerVars = checkEat(playerIndex, pawnIndex, playerVars, roll)
        elif playerVars[playerIndex][1][pawnIndex] == 1:
            if playerVars[playerIndex][2][pawnIndex] + roll <= 39 and playerVars[playerIndex][3][pawnIndex] == 0:
                playerVars[playerIndex][2][pawnIndex] += roll
                playerVars = checkEat(playerIndex, pawnIndex, playerVars, roll)
                if roll == 6:
                    movedWithSix = True
            elif playerVars[playerIndex][2][pawnIndex] + roll > 39 and playerVars[playerIndex][3][pawnIndex] == 0:
                playerVars[playerIndex][2][pawnIndex] += roll
                playerVars[playerIndex][2][pawnIndex] -= 40
                playerVars[playerIndex][3][pawnIndex] += 1
                playerVars = checkEat(playerIndex, pawnIndex, playerVars, roll)
                if roll == 6:
                    movedWithSix = True
            elif playerVars[playerIndex][3][pawnIndex] == 1 and playerVars[playerIndex][2][pawnIndex] + roll < playerIndex * 10:
                playerVars[playerIndex][2][pawnIndex] += roll
                playerVars = checkEat(playerIndex, pawnIndex, playerVars, roll)
                if roll == 6:
                    movedWithSix = True
            else:
                playerVars[playerIndex][2][pawnIndex] += roll
                playerVars[playerIndex][1][pawnIndex] = 2
                if roll == 6:
                    movedWithSix = True
    return playerVars, movedWithSix


def checkEat(playerIndex, pawnIndex, playerVars, roll):
    for playerToEat in range(4):
        if playerToEat != playerIndex:
            for pawnToEat in range(4):
                if playerVars[playerToEat][1][pawnToEat] == 1:
                    if playerVars[playerToEat][2][pawnToEat] == playerVars[playerIndex][2][pawnIndex]:
                        playerVars[playerToEat][1][pawnToEat] = 0
                        playerVars[playerToEat][2][pawnToEat] = -1
                        if playerToEat > 0:
                            playerVars[playerToEat][3][pawnToEat] = 0
                        else:
                            playerVars[playerToEat][3][pawnToEat] = 1
    return playerVars


def whoGoesFirst(screen, clock, playerVars, fontSmall):
    howManyPlaying = 0
    indexForOnePlayer = 0
    for i in range(4):
        if playerVars[i][0] > 0:
            howManyPlaying += 1
            indexForOnePlayer = i
    if howManyPlaying == 1:
        return indexForOnePlayer
    colorNotPicked = [18, 22, 25]  # CRNA
    colorWhite = [253, 255, 252]
    colorPlayer = [[219, 34, 42], [0, 78, 152], [76, 185, 68], [240, 200, 8]]
    colorName = ["Crveni", "Plavi", "Zeleni", "Zuti"]
    msgWhoGoesFirst = fontSmall.render("Igrač sa najvecim brojem igra prvi:", True, colorNotPicked)
    msgPlayer = []
    for j in range(4):
        if playerVars[j][0] < 2:
            msgPlayer.append(fontSmall.render(str(colorName[j]) + " igrač: ", True, colorNotPicked))
        #else:
        #    msgPlayer.append(fontSmall.render(str(colorName[j]) + " CPU: ", True, colorNotPicked))
    diceRoll = []
    diceRoll.append(fontSmall.render("1", True, colorNotPicked))
    diceRoll.append(fontSmall.render("2", True, colorNotPicked))
    diceRoll.append(fontSmall.render("3", True, colorNotPicked))
    diceRoll.append(fontSmall.render("4", True, colorNotPicked))
    diceRoll.append(fontSmall.render("5", True, colorNotPicked))
    diceRoll.append(fontSmall.render("6", True, colorNotPicked))
    inGame = [True, True, True, True]
    multipleInGame = True
    for i in range(4):
        if playerVars[i][0] == 0:
            inGame[i] = False
    while multipleInGame:
        roll = [0, 0, 0, 0]
        i = 0
        while i < 4:
            if inGame[i]:
                waitingForDice = True
                while waitingForDice:
                    # print(i)
                    clock.tick(30)
                    #
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.KEYDOWN and playerVars[i][0] == 1:
                            # Programian SPACE za random i (NUMPAD_12456) na (123456)
                            if event.key == pygame.K_SPACE:
                                roll[i] = random.randint(1, 6)
                                waitingForDice = False
                            if event.key == pygame.K_KP_1:
                                roll[i] = 1
                                waitingForDice = False
                            if event.key == pygame.K_KP_2:
                                roll[i] = 2
                                waitingForDice = False
                            if event.key == pygame.K_KP_3:
                                roll[i] = 3
                                waitingForDice = False
                            if event.key == pygame.K_KP_4:
                                roll[i] = 4
                                waitingForDice = False
                            if event.key == pygame.K_KP_5:
                                roll[i] = 5
                                waitingForDice = False
                            if event.key == pygame.K_KP_6:
                                roll[i] = 6
                                waitingForDice = False
                            if event.key == pygame.K_ESCAPE:
                                mainMenu(screen, clock, pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 90))
                    pygame.draw.rect(screen, colorWhite, pygame.Rect(804, 0, 626, 804))
                    screen.blit(msgWhoGoesFirst, (820, 20))
                    printMultiplier = 80
                    for j in range(4):
                        if inGame[j]:
                            screen.blit(msgPlayer[j], (820, printMultiplier))
                            if roll[j] > 0:
                                screen.blit(diceRoll[roll[j] - 1], (1000, printMultiplier))
                            printMultiplier += 30
                    pygame.display.update()
            i += 1
        maximum = roll[0]
        for j in range(4):
            if maximum < roll[j]:
                maximum = roll[j]
        for j in range(4):
            if roll[j] != maximum:
                inGame[j] = False
        howManyLeft = 0
        for j in range(4):
            if inGame[j]:
                howManyLeft += 1
        if howManyLeft == 1:
            multipleInGame = False
        waitingForNext = True
        while waitingForNext:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waitingForNext = False
    startingIndex = 0
    while inGame[startingIndex] != True:
        startingIndex += 1
    return startingIndex


def addLocHome(locationHome):
    for i in range(44):
        locationHome.append(0)
    # LOKCAIJE CRVENIH KUCA
    locationHome[40] = [84, 372]
    locationHome[41] = [156, 372]
    locationHome[42] = [228, 372]
    locationHome[43] = [300, 372]
    # LOKCAIJE PLAVIH KUCA
    locationHome[10] = [372, 84]
    locationHome[11] = [372, 156]
    locationHome[12] = [372, 228]
    locationHome[13] = [372, 300]
    # LOKCAIJE ZELENIH KUCA
    locationHome[20] = [660, 372]
    locationHome[21] = [588, 372]
    locationHome[22] = [516, 372]
    locationHome[23] = [444, 372]
    # LOKCAIJE ZUTIH KUCA
    locationHome[30] = [372, 660]
    locationHome[31] = [372, 588]
    locationHome[32] = [372, 516]
    locationHome[33] = [372, 444]
    return locationHome


def main():
    pygame.init()
    pygame.font.init()
    resWidth = 1430
    resHeight = 864
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((resWidth, resHeight))
    pygame.display.set_caption("Čovjece ne ljuti se")
    fontPick = pygame.font.Font(os.path.join("fonts", "Roboto-Regular.ttf"), 90)
    while True:
        mainMenu(screen, clock, fontPick)


if __name__ == "__main__":
    main()
