import pygame
import time

def arrayChoice():
    print("4x4 or 9x9?")
    choice = input()
    if choice == "4x4":
        Sodoku4()
    if choice == "9x9":
        Sodoku9()
def Sodoku9():
    #Instead of using the same line based solution like in the 4x4 I will be using a 3x3 solution. (ie: Q1, Q2, Q3, Q4, etc..)
    pygame.init()
    surface = pygame.display.set_mode((700,700))
    color = (255,255,255)
    widthL = [30, 90, 150, 210, 270, 330, 390, 450, 510]
    heightL = [30, 90, 150, 210, 270, 330, 390, 450, 510]
    y = 0
    xy = 0
    Quad1 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad2 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad3 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad4 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad5 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad6 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad7 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad8 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    Quad9 = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
    for x in range(9):
        for x in range(9):
            pygame.draw.rect(surface, color, pygame.Rect(widthL[y], heightL[xy], 60, 60),  2)
            pygame.display.flip()
            y = y + 1
            if y == 9:
                y = 0
                xy = xy + 1
    L1completed = 0
    L2completed = 0
    L3completed = 0
    L4completed = 0
    L5completed = 0
    L6completed = 0
    L7completed = 0
    L8completed = 0
    L9completed = 0
    while L1completed == 0:
        print("Please type nine lines of numbers with the letter b representing blank spaces.")
        L1 = input()
        if len(str(L1)) == 9:
            L1completed = 1
        else:
            print("Line 1 is not valid. Please try again.")
    while L2completed == 0:
        L2 = input()
        if len(str(L2)) == 9:
            L2completed = 1
        else:
            print("Line 2 is not valid. Please try again.")
    while L3completed == 0:
        L3 = input()
        if len(str(L3)) == 9:
            L3completed = 1
        else:
            print("Line 3 is not valid. Please try again.")
    while L4completed == 0:
        L4 = input()
        if len(str(L4)) == 9:
            L4completed = 1
        else:
            print("Line 4 is not valid. Please try again.")
    while L5completed == 0:
        L5 = input()
        if len(str(L5)) == 9:
            L5ompleted = 1
        else:
            print("Line 5 is not valid. Please try again.")
    while L6completed == 0:
        L6 = input()
        if len(str(L6)) == 9:
            L6ompleted = 1
        else:
            print("Line 6 is not valid. Please try again.")
    while L7completed == 0:
        L7 = input()
        if len(str(L7)) == 9:
            L7completed = 1
        else:
            print("Line 7 is not valid. Please try again.")
    while L8completed == 0:
        L8 = input()
        if len(str(L8)) == 9:
            L8ompleted = 1
        else:
            print("Line 8 is not valid. Please try again.")
    while L9completed == 0:
        L9 = input()
        if len(str(L9)) == 9:
            L9ompleted = 1
        else:
            print("Line 9 is not valid. Please try again.")
    Quad1 = [L1[0], L1[1], L1[2], L2[0], L2[1], L2[2], L3[0], L3[1], L3[2]]
    #assign all quadrant values
    
def initialLines4(line1, line2, line3, line4, surface, L1, L2, L3, L4):
    widthL = [30, 90, 150, 210]
    textWidthL = [60, 120, 180, 240]
    textHeightL = [60, 120, 180, 240]
    heightL = [30, 90, 150, 210]
    font = pygame.font.SysFont('Arial', 36, bold=True)
    color = (255,255,255)
    black = (0,0,0)
    red = (136,8,8)
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L1[0]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L1[1]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L1[2]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L1[3]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[0]) - img.get_height()/2)))
                    pygame.display.flip()
                    L1[x] = "1"
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[0]) - img.get_height()/2)))
                    pygame.display.flip()
                    L1[x] = "2"
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[0]) - img.get_height()/2)))
                    pygame.display.flip()
                    L1[x] = "3"
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[0]) - img.get_height()/2)))
                    pygame.display.flip()
                    L1[x] = "4"
            x = x + 1
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L2[0]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L2[1]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L2[2]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L2[3]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[1]) - img.get_height()/2)))
                    pygame.display.flip()
                    L2[x] = 1
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[1]) - img.get_height()/2)))
                    pygame.display.flip()
                    L2[x] = 2
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[1]) - img.get_height()/2)))
                    pygame.display.flip()
                    L2[x] = 3
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[1]) - img.get_height()/2)))
                    pygame.display.flip()
                    L2[x] = 4
            x = x + 1
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L3[0]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L3[1]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L3[2]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L3[3]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[2]) - img.get_height()/2)))
                    pygame.display.flip()
                    L3[x] = 1
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[2]) - img.get_height()/2)))
                    pygame.display.flip()
                    L3[x] = 2
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[2]) - img.get_height()/2)))
                    pygame.display.flip()
                    L3[x] = 3
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[2]) - img.get_height()/2)))
                    pygame.display.flip()
                    L3[x] = 4
            x = x + 1
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L4[0]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L4[1]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L4[2]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L4[3]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[3]) - img.get_height()/2)))
                    pygame.display.flip()
                    L4[x] = 1
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[3]) - img.get_height()/2)))
                    pygame.display.flip()
                    L4[x] = 2
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[3]) - img.get_height()/2)))
                    pygame.display.flip()
                    L4[x] = 3
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[x] - img.get_width()/2), ((textHeightL[3]) - img.get_height()/2)))
                    pygame.display.flip()
                    L4[x] = 4
            x = x + 1
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L1[0]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L2[0]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L3[0]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L4[0]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[0] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[0] = "1"
                    if int(x) == int("1"):
                        L2[0] = "1"
                    if int(x) == int("2"):
                        L3[0] = "1"
                    if int(x) == int("3"):
                        L4[0] = "1"
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[0] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[0] = "2"
                    if int(x) == int("1"):
                        L2[0] = "2"
                    if int(x) == int("2"):
                        L3[0] = "2"
                    if int(x) == int("3"):
                        L4[0] = "2"
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[0] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[0] = "3"
                    if int(x) == int("1"):
                        L2[0] = "3"
                    if int(x) == int("2"):
                        L3[0] = "3"
                    if int(x) == int("3"):
                        L4[0] = "3"
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[0] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[0] = "4"
                    if int(x) == int("1"):
                        L2[0] = "4"
                    if int(x) == int("2"):
                        L3[0] = "4"
                    if int(x) == int("3"):
                        L4[0] = "4"
            x = x + 1
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L1[1]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L2[1]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L3[1]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L4[1]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[1] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[1] = "1"
                    if int(x) == int("1"):
                        L2[1] = "1"
                    if int(x) == int("2"):
                        L3[1] = "1"
                    if int(x) == int("3"):
                        L4[1] = "1"
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[1] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[1] = "2"
                    if int(x) == int("1"):
                        L2[1] = "2"
                    if int(x) == int("2"):
                        L3[1] = "2"
                    if int(x) == int("3"):
                        L4[1] = "2"
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[1] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[1] = "3"
                    if int(x) == int("1"):
                        L2[1] = "3"
                    if int(x) == int("2"):
                        L3[1] = "3"
                    if int(x) == int("3"):
                        L4[1] = "3"
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[1] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[1] = "4"
                    if int(x) == int("1"):
                        L2[1] = "4"
                    if int(x) == int("2"):
                        L3[1] = "4"
                    if int(x) == int("3"):
                        L4[1] = "4"
            x = x + 1
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L1[2]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L2[2]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L3[2]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L4[2]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[2] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[2] = "1"
                    if int(x) == int("1"):
                        L2[2] = "1"
                    if int(x) == int("2"):
                        L3[2] = "1"
                    if int(x) == int("3"):
                        L4[2] = "1"
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[2] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[2] = "2"
                    if int(x) == int("1"):
                        L2[2] = "2"
                    if int(x) == int("2"):
                        L3[2] = "2"
                    if int(x) == int("3"):
                        L4[2] = "2"
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[2] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[2] = "3"
                    if int(x) == int("1"):
                        L2[2] = "3"
                    if int(x) == int("2"):
                        L3[2] = "3"
                    if int(x) == int("3"):
                        L4[2] = "3"
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[2] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[2] = "4"
                    if int(x) == int("1"):
                        L2[2] = "4"
                    if int(x) == int("2"):
                        L3[2] = "4"
                    if int(x) == int("3"):
                        L4[2] = "4"
            x = x + 1
    x = 0
    adder = 0
    cor0 = 0
    cor1 = 0
    cor2 = 0
    cor3 = 0
    values = [0, 0, 0, 0]
    for x in range(5):
        if str(L1[3]).__contains__(str(x)):
            adder = adder + 1
            values[0] = x
        if str(L2[3]).__contains__(str(x)):
            adder = adder + 1
            values[1] = x
        if str(L3[3]).__contains__(str(x)):
            adder = adder + 1
            values[2] = x
        if str(L4[3]).__contains__(str(x)):
            adder = adder + 1
            values[3] = x
        x = x + 1
    x = 0
    print(adder)
    print(values)
    if adder == 3:
        for y in range(4):
            if str(values[x]).__contains__("0"):
                if "1" not in str(values[0]) and "1" not in str(values[1]) and "1" not in str(values[2]) and "1" not in str(values[3]):
                    img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[3] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[3] = "1"
                    if int(x) == int("1"):
                        L2[3] = "1"
                    if int(x) == int("2"):
                        L3[3] = "1"
                    if int(x) == int("3"):
                        L4[3] = "1"
                if "2" not in str(values[0]) and "2" not in str(values[1]) and "2" not in str(values[2]) and "2" not in str(values[3]):
                    img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[3] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[3] = "2"
                    if int(x) == int("1"):
                        L2[3] = "2"
                    if int(x) == int("2"):
                        L3[3] = "2"
                    if int(x) == int("3"):
                        L4[3] = "2"
                if "3" not in str(values[0]) and "3" not in str(values[1]) and "3" not in str(values[2]) and "3" not in str(values[3]):
                    img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[3] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[3] = "3"
                    if int(x) == int("1"):
                        L2[3] = "3"
                    if int(x) == int("2"):
                        L3[3] = "3"
                    if int(x) == int("3"):
                        L4[3] = "3"
                if "4" not in str(values[0]) and "4" not in str(values[1]) and "4" not in str(values[2]) and "4" not in str(values[3]):
                    img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                    surface.blit(img, ((textWidthL[3] - img.get_width()/2), ((textHeightL[x]) - img.get_height()/2)))
                    pygame.display.flip()
                    if int(x) == int("0"):
                        L1[3] = "4"
                    if int(x) == int("1"):
                        L2[3] = "4"
                    if int(x) == int("2"):
                        L3[3] = "4"
                    if int(x) == int("3"):
                        L4[3] = "4"
            x = x + 1
    print(L1)
    print(L2)
    print(L3)
    print(L4)
    print("Initial lines complete")
def brute4(surface, L1, L2, L3, L4, red, widthL, heightL, font, color, black, textWidthL, textHeightL):
    L1blanks = [0, 0, 0, 0]
    L2blanks = [0, 0, 0, 0]
    L3blanks = [0, 0, 0, 0]
    L4blanks = [0, 0, 0, 0]
    for x in range(4):
        if L1[x] == "b":
            print("(1, " + str(x) + ") is blank.")
            pygame.draw.rect(surface, red, pygame.Rect(widthL[x], heightL[0], 60, 60),  2)
            L1blanks[x] = 1
        if L2[x] == "b":
            print("(2, " + str(x) + ") is blank.")
            pygame.draw.rect(surface, red, pygame.Rect(widthL[x], heightL[1], 60, 60),  2)
            L2blanks[x] = 1
        if L3[x] == "b":
            print("(3, " + str(x) + ") is blank.")
            pygame.draw.rect(surface, red, pygame.Rect(widthL[x], heightL[2], 60, 60),  2)
            L3blanks[x] = 1
        if L4[x] == "b":
            print("(4, " + str(x) + ") is blank.")
            pygame.draw.rect(surface, red, pygame.Rect(widthL[x], heightL[3], 60, 60),  2)
            L4blanks[x] = 1
        pygame.display.flip()
        print("\n" + "blanks" + "\n")
        print(L1blanks)
        print(L2blanks)
        print(L3blanks)
        print(L4blanks)
        print("\n" + "fulls" + "\n")
        print(L1)
        print(L2)
        print(L3)
        print(L4)
        print()
        Q1 = [L1[0], L1[1], L2[0], L2[1]]
        print("Q1" + str(Q1))
        Q2 = [L1[2], L1[3], L2[2], L2[3]]
        print("Q2" + str(Q2))
        Q3 = [L3[0], L3[1], L4[0], L4[1]]
        print("Q3" + str(Q3))
        Q4 = [L3[2], L3[3], L4[2], L4[3]]
        print("Q4" + str(Q4))
        x = 0
        for x in range(4):
            if str(L1blanks[x]) == "1":
                if str(x) > "1":
                    print("(1, " + str(x) + ") is in quadrant 2")
                else:
                    print("(1, " + str(x) + ") is in quadrant 1")
            if str(L2blanks[x]) == "1":
                if str(x) > "1":
                    print("(2, " + str(x) + ") is in quadrant 2")
                else:
                    print("(2, " + str(x) + ") is in quadrant 1")
            if str(L3blanks[x]) == "1":
                if str(x) > "1":
                    print("(3, " + str(x) + ") is in quadrant 2")
                else:
                    print("(3, " + str(x) + ") is in quadrant 1")
            if str(L4blanks[x]) == "1":
                if str(x) > "1":
                    print("(4, " + str(x) + ") is in quadrant 2")
                else:
                    print("(4, " + str(x) + ") is in quadrant 1")
        if str(Q1).__contains__("b"):
            if str(Q1).__contains__("1") and str(Q1).__contains__("2") and str(Q1).__contains__("3"):
                for x in range(4):
                    if str(Q1[x]).__contains__("b"):
                        Q1[x] = "4"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 1
                            L2[width] = "4"
                        else:
                            height = 0
                            L1[width] = "4"
                        img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q1).__contains__("1") and str(Q1).__contains__("2") and str(Q1).__contains__("4"):
                for x in range(4):
                    if str(Q1[x]).__contains__("b"):
                        Q1[x] = "3"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 1
                            L2[width] = "3"
                        else:
                            height = 0
                            L1[width] = "3"
                        img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q1).__contains__("1") and str(Q1).__contains__("3") and str(Q1).__contains__("4"):
                for x in range(4):
                    if str(Q1[x]).__contains__("b"):
                        Q1[x] = "2"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 1
                            L2[width] = "2"
                        else:
                            height = 0
                            L1[width] = "2"
                        img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q1).__contains__("2") and str(Q1).__contains__("3") and str(Q1).__contains__("4"):
                for x in range(4):
                    if str(Q1[x]).__contains__("b"):
                        Q1[x] = "1"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 1
                            L2[width] = "1"
                        else:
                            height = 0
                            L1[width] = "1"
                        img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
        if str(Q2).__contains__("b"):
            if str(Q2).__contains__("1") and str(Q2).__contains__("2") and str(Q2).__contains__("3"):
                for x in range(4):
                    if str(Q2[x]).__contains__("b"):
                        Q2[x] = "4"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 1
                            L2[width] = "4"
                        else:
                            height = 0
                            L1[width] = "4"
                        img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q2).__contains__("1") and str(Q2).__contains__("2") and str(Q2).__contains__("4"):
                for x in range(4):
                    if str(Q2[x]).__contains__("b"):
                        Q2[x] = "3"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 1
                            L2[width] = "3"
                        else:
                            height = 0
                            L1[width] = "3"
                        img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q2).__contains__("1") and str(Q2).__contains__("3") and str(Q2).__contains__("4"):
                for x in range(4):
                    if str(Q2[x]).__contains__("b"):
                        Q2[x] = "2"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 1
                            L2[width] = "2"
                        else:
                            height = 0
                            L1[width] = "2"
                        img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q2).__contains__("2") and str(Q2).__contains__("3") and str(Q2).__contains__("4"):
                for x in range(4):
                    if str(Q2[x]).__contains__("b"):
                        Q2[x] = "1"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 1
                            L2[width] = "1"
                        else:
                            height = 0
                            L1[width] = "1"
                        img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
        if str(Q3).__contains__("b"):
            if str(Q3).__contains__("1") and str(Q3).__contains__("2") and str(Q3).__contains__("3"):
                for x in range(4):
                    if str(Q3[x]).__contains__("b"):
                        Q3[x] = "4"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 3
                            L4[width] = "4"
                        else:
                            height = 2
                            L3[width] = "4"
                        img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q3).__contains__("1") and str(Q3).__contains__("2") and str(Q3).__contains__("4"):
                for x in range(4):
                    if str(Q3[x]).__contains__("b"):
                        Q3[x] = "3"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 3
                            L4[width] = "3"
                        else:
                            height = 2
                            L3[width] = "3"
                        img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q3).__contains__("1") and str(Q3).__contains__("3") and str(Q3).__contains__("4"):
                for x in range(4):
                    if str(Q3[x]).__contains__("b"):
                        Q3[x] = "2"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 3
                            L4[width] = "2"
                        else:
                            height = 2
                            L3[width] = "2"
                        img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q3).__contains__("2") and str(Q3).__contains__("3") and str(Q3).__contains__("4"):
                for x in range(4):
                    if str(Q3[x]).__contains__("b"):
                        Q3[x] = "1"
                        if str(x) == "0" or str(x) == "2":
                            width = 0
                        if str(x) == "1" or str(x) == "3":
                            width = 1
                        if str(x) > "1":
                            height = 3
                            L4[width] = "1"
                        else:
                            height = 2
                            L3[width] = "1"
                        img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
        if str(Q4).__contains__("b"):
            if str(Q4).__contains__("1") and str(Q4).__contains__("2") and str(Q4).__contains__("3"):
                for x in range(4):
                    if str(Q4[x]).__contains__("b"):
                        Q4[x] = "4"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 3
                            L4[width] = "4"
                        else:
                            height = 2
                            L3[width] = "4"
                        img = font.render("4", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q4).__contains__("1") and str(Q4).__contains__("2") and str(Q4).__contains__("4"):
                for x in range(4):
                    if str(Q4[x]).__contains__("b"):
                        Q4[x] = "3"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 3
                            L4[width] = "3"
                        else:
                            height = 2
                            L3[width] = "3"
                        img = font.render("3", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q4).__contains__("1") and str(Q4).__contains__("3") and str(Q4).__contains__("4"):
                for x in range(4):
                    if str(Q4[x]).__contains__("b"):
                        Q4[x] = "2"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 3
                            L4[width] = "2"
                        else:
                            height = 2
                            L3[width] = "2"
                        img = font.render("2", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            if str(Q4).__contains__("2") and str(Q4).__contains__("3") and str(Q4).__contains__("4"):
                for x in range(4):
                    if str(Q4[x]).__contains__("b"):
                        Q4[x] = "1"
                        if str(x) == "0" or str(x) == "2":
                            width = 2
                        if str(x) == "1" or str(x) == "3":
                            width = 3
                        if str(x) > "1":
                            height = 3
                            L4[width] = "1"
                        else:
                            height = 2
                            L3[width] = "1"
                        img = font.render("1", True, pygame.Color(red), pygame.Color(black))
                        surface.blit(img, ((textWidthL[width] - img.get_width()/2), ((textHeightL[height]) - img.get_height()/2)))
            print(L1, L2, L3, L4)
def Sodoku4():
    false = ""
    lineF = 0
    confirmed = 0
    while confirmed == 0:
        print("Please enter the each line of the sodoku. Enter 'b' if the space is blank. After you are done with a specific line press enter.")
        line1 = "0"
        line2 = "0"
        line3 = "0"
        line4 = "0"
        while lineF != 1:
            line1 = input()
            if len(str(line1)) != 4:
                print("This line is not valid due to the number of characters, please try again.")
            else:
                lineF = 1
        lineF = 0
        while lineF != 1:
            line2 = input()
            if len(str(line2)) != 4:
                print("This line is not valid due to the number of characters, please try again.")
            else:
                lineF = 1
        lineF = 0
        while lineF != 1:
            line3 = input()
            if len(str(line3)) != 4:
                print("This line is not valid due to the number of characters, please try again.")
            else:
                lineF = 1
        lineF = 0
        while lineF != 1:
            line4 = input()
            if len(str(line4)) != 4:
                print("This line is not valid due to the number of characters, please try again.")
            else:
                lineF = 1
        print("Is this the sodoku you wanted to enter? Please enter 'Yes' or 'No'\n")
        confirm = input()
        if confirm == "Yes" or confirm == "yes":
            confirmed = 1
        if confirm == "No" or confirm == "no":
            confirmed = 0
    L1 = [line1[0], line1[1], line1[2], line1[3]]
    L2 = [line2[0], line2[1], line2[2], line2[3]]
    L3 = [line3[0], line3[1], line3[2], line3[3]]
    L4 = [line4[0], line4[1], line4[2], line4[3]]
    columnComplete = [0, 0, 0, 0]
    pygame.init()
    pygame.font.init()
    surface = pygame.display.set_mode((700,700))
    color = (255,255,255)
    black = (0,0,0)
    red = (136,8,8)
    font = pygame.font.SysFont('Arial', 36, bold=True)
    widthL = [30, 90, 150, 210]
    textWidthL = [60, 120, 180, 240]
    textHeightL = [60, 120, 180, 240]
    heightL = [30, 90, 150, 210]
    y = 0
    xy = 0
    finished = 0
    while finished == 0:
        if L1[y] != "b":
            img = font.render(L1[y], True, pygame.Color(color), pygame.Color(black))
            surface.blit(img, ((textWidthL[y] - img.get_width()/2), ((textHeightL[0]) - img.get_height()/2)))
        if L2[y] != "b":
            img = font.render(L2[y], True, pygame.Color(color), pygame.Color(black))
            surface.blit(img, ((textWidthL[y] - img.get_width()/2), ((textHeightL[1]) - img.get_height()/2)))
        if L3[y] != "b":
            img = font.render(L3[y], True, pygame.Color(color), pygame.Color(black))
            surface.blit(img, ((textWidthL[y] - img.get_width()/2), ((textHeightL[2]) - img.get_height()/2)))
        if L4[y] != "b":
            img = font.render(L4[y], True, pygame.Color(color), pygame.Color(black))
            surface.blit(img, ((textWidthL[y] - img.get_width()/2), ((textHeightL[3]) - img.get_height()/2)))
        y = y + 1
        if y == 4:
            y = 0
            xy = xy +1
        if xy == 4:
            finished = 1
    y = 0
    xy = 0
    for x in range(4):
        for x in range(4):
            pygame.draw.rect(surface, color, pygame.Rect(widthL[y], heightL[xy], 60, 60),  2)
            pygame.display.flip()
            y = y + 1
            if y == 4:
                y = 0
                xy = xy + 1
    for x in range(5):
        initialLines4(line1, line2, line3, line4, surface, L1, L2, L3, L4)
        initialLines4(line1, line2, line3, line4, surface, L1, L2, L3, L4)
        brute4(surface, L1, L2, L3, L4, red, widthL, heightL, font, color, black, textWidthL, textHeightL)
        y = 0
    xy = 0
    for x in range(4):
        for x in range(4):
            pygame.draw.rect(surface, color, pygame.Rect(widthL[y], heightL[xy], 60, 60),  2)
            pygame.display.flip()
            y = y + 1
            if y == 4:
                y = 0
                xy = xy + 1
    for x in range(4):
        if L1[x] != "b" and L2[x] != "b" and L3[x] != "b" and L4[x] != "b":
            columnComplete[x] = 1
    if columnComplete[0] == 1 and columnComplete[1] == 1 and columnComplete[2] == 1 and columnComplete[3] == 1:
        print("\n" + "The puzzle has been completed.")
    else:
        print("\n" + "The puzzle was not able to be completed")
arrayChoice()
