import pygame as pg
import time


pg.init()

screen = pg.display.set_mode((800, 768))
pg.display.set_caption("STATERA")
ImgBackground = pg.image.load('images/You Lose.PNG')
ImgBackground = pg.transform.scale(ImgBackground, (865, 555))
Opening = pg.image.load('images/STATERA.PNG')
leave_it = pg.image.load('images/nextscreen.png')
Ending = pg.image.load('images/you won.png')
Ending = pg.transform.scale(Ending, (868, 487))
imgBackground = pg.image.load('images/bg2.png')
how_to_play = pg.image.load('images/about the game.PNG')
parents = pg.image.load('images/parents.png')
parents = pg.transform.scale(parents, (75, 71))
villagers = pg.image.load('images/villagers.png')
villagers = pg.transform.scale(villagers, (100, 95))

run = True
screen_show1 = "hide"
screen_show2 = "hide"
screen_show3 = "hide"

loseSound = pg.mixer.Sound('sound/lose.wav')
winSound = pg.mixer.Sound('sound/clap.wav')
blockSound = pg.mixer.Sound('sound/drop.wav')

imgBlock1 = pg.image.load('images/Lego1.png')
block1X = 285
block1Y = 638

imgBlock2 = pg.image.load('images/Lego2.png')
block2X = -172
block2Y = 568
block2X_change = 0
block2Y_change = 0
block2_state = "stable"

imgBlock3 = pg.image.load('images/Lego3.png')
block3X = 900
block3Y = 568
block3X_change = 0
block3Y_change = 0
block3_state = "stable"

imgBlock4 = pg.image.load('images/Lego4.png')
block4X = -172
block4Y = 498
block4X_change = 0
block4Y_change = 0
block4_state = "stable"

ang = 0
num_blocks = 10
imgBlock = []
blockX = []
blockY = []
blockX_change = []
blockY_change = []
block_state = []
y = []
music_play = []
for i in range(num_blocks):
    if i == 0:
        imgBlock.append(imgBlock1)
        blockX.append(block1X)
        blockY.append(block1Y)
    if i == 1:
        imgBlock.append(imgBlock2)
        blockX.append(block2X)
        blockY.append(block2Y)
    if i == 2:
        imgBlock.append(imgBlock3)
        blockX.append(block3X)
        blockY.append(block3Y)
    if i == 3:
        imgBlock.append(imgBlock4)
        blockX.append(block4X)
        blockY.append(block4Y)
    if i > 3:
        if i % 4 == 0:
            imgBlock.append(pg.image.load('images/Lego1.png'))
        if i % 4 == 1:
            imgBlock.append(pg.image.load('images/Lego2.png'))
        if i % 4 == 2:
            imgBlock.append(pg.image.load('images/Lego3.png'))
        if i % 4 == 3:
            imgBlock.append(pg.image.load('images/Lego4.png'))
        if i % 2 == 0:
            blockX.append(900)
        if i % 2 == 1:
            blockX.append(-172)
        if i % 3 == 1 or i % 3 == 0:
            blockY.append(blockY[i - 1] - 70)
        if i % 3 == 2:
            blockY.append(blockY[i - 1])
    y.append((653 - blockY[i]) // (4 + 2 * i))
    music_play.append(blockY[i] + (4 + 2 * i) * y[i])
    blockX_change.append(0)
    blockY_change.append(0)
    block_state.append("stable")

def reset():
    global blockY, blockX
    for i in range(num_blocks):
        if i > 3:
            if i % 4 == 0:
                imgBlock[i] = pg.image.load('images/Lego1.png')
            if i % 4 == 1:
                imgBlock[i] = pg.image.load('images/Lego2.png')
            if i % 4 == 2:
                imgBlock[i] = pg.image.load('images/Lego3.png')
            if i % 4 == 3:
                imgBlock[i] = pg.image.load('images/Lego4.png')
            if i % 2 == 0:
                blockX[i] = 900
            if i % 2 == 1:
                blockX[i] = -172
            if i % 3 == 1 or i % 3 == 0:
                blockY[i] = blockY[i - 1] - 70
            if i % 3 == 2:
                blockY[i] = blockY[i - 1]
        blockX_change[i] = 0
        blockY_change[i] = 0
        block_state[i] = "stable"
    blockY = [638, 568, 568, 498, 428, 428, 358, 288, 288, 218]
    blockX = [287, -172, 900, -172, 900, -172, 900, -172, 900, -172]


boy = pg.image.load("images/standing boy.png")
boy = pg.transform.scale(boy, (151, 210))
boy1 = pg.image.load("images/standing boy.png")
boy1 = pg.transform.scale(boy1, (151, 210))
boyX = 900
boyY = 0
boyX_change = 0
boyY_change = 0
boy_state = "stable"


def boy_show(x, y):
    screen.blit(boy, (x, y))


font = pg.font.Font('freesansbold.ttf', 35)
fontv2 = pg.font.Font('freesansbold.ttf', 30)
font3 = pg.font.Font('freesansbold.ttf', 25)
msg_time = False
restart = False
game_lost = False
continue_button = True
score_value = 0


def next_page():
    msg = font.render("Press Tab to Continue", True, (255, 255, 255))
    screen.blit(msg, (225, 700))


'''
def start_game():
    msg = font.render("Press Enter to start", True, (0, 0, 0))
    msg2 = font.render("  Press X to restart", True, (0, 0, 0))
    msg3 = fontv2.render("Press Space to place the moving block", True, (0, 0, 0))
    screen.blit(msg, (230, 300))
    screen.blit(msg2, (230, 400))
    screen.blit(msg3, (125, 350))
'''


def start_gamev2():
    global restart
    if restart:
        msg4 = font.render("Press Enter to start", True, (255, 0, 0))
        screen.blit(msg4, (230, 250))


def block2(x, y):
    screen.blit(imgBlock2, (x, y))


def block1(x, y):
    screen.blit(imgBlock1, (x, y))


def block3(x, y):
    screen.blit(imgBlock3, (x, y))


def block4(x, y):
    screen.blit(imgBlock4, (x, y))


def game_over():
    global game_lost
    screen.blit(ImgBackground, (-55, 215))
    msg_5 = fontv2.render("Wanna Play Again ? Press X", True, (0, 0, 0))
    screen.blit(msg_5, (185, 165))


def score_display1():
    global score_value
    msg7 = fontv2.render("Score:" + str(score_value), True, (0, 0, 0))
    screen.blit(msg7, (10, 20))


def block_movement():
    for k in range(num_blocks):
        blockX[k] += blockX_change[k]
        blockY[k] += blockY_change[k]
    # If it causes error like 'int' object not ..... then you missed [k] somewhere....


def block_blit():
    for i in range(num_blocks):
        if i > 3:
            screen.blit(imgBlock[i], (blockX[i], blockY[i]))


score = False
'''
def show_block(i):
    screen.blit(imgBlock[i], (blockX[i], blockY[i]))
'''


def fall(i):
    if i % 2 == 0:
        if blockX[i] != 900 and blockX[i + 1] == -172:
            if blockX[i - 1] != -172:
                block_state[i] = "fall"
                imgBlock[i] = pg.transform.rotate(imgBlock[i], -90)
    if i % 2 == 1 and blockX[i + 1] == 900:
        if blockX[i] != -172:
            if blockX[i - 1] != 900 and blockX[i + 1] == 900:
                block_state[i] = "fall"
                imgBlock[i] = pg.transform.rotate(imgBlock[i], -90)


you_win_window = False

while run:
    screen.fill((0, 0, 0))
    screen.blit(Opening, (-100, 110))
    blockX_change[3] = block4X_change
    blockY_change[3] = block4Y_change
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_TAB:
                if screen_show3 == "hide" and screen_show2 == "show_stage1":
                    screen_show3 = "show_stage2"
                    continue_button = False
                if screen_show2 == "hide" and screen_show1 == "show_howtoplay":
                    screen_show2 = "show_stage1"
                if screen_show2 == "hide" and screen_show1 == "hide":
                    screen_show1 = "show_howtoplay"

            if event.key == pg.K_RETURN and block2Y == 568 and screen_show3 == "show_stage2":
                block3X_change = 0
                if block2X < 0:
                    block2X_change = 10
                    block2_state = "move"
                    msg_time = False
                    restart = False
            if event.key == pg.K_SPACE:
                blockSound.play()
                if (0 < block2X + 172 < 337) and block2X != 164 and block2Y == 568 and block3X == 900:
                    block2_state = "fall"
                    imgBlock2 = pg.transform.rotate(imgBlock2, -90)

                if 900 > block3X > 409 and block3Y == 568:
                    block3_state = "fall"
                    imgBlock3 = pg.transform.rotate(imgBlock3, -90)

                if block4Y == 498 and not (block3X + 52 < block4X + 172 and block2X + 120 > block4X):
                    if block4X != -172:
                        block4_state = "fall"
                        imgBlock4 = pg.transform.rotate(imgBlock4, -90)

                if block2X >= 167 and block3X == 900:
                    block2_state = "stable"
                    block3_state = "move"
                    score_value += 10

                if block3X <= 407 and block4X == -172:
                    block3_state = "stable"
                    block4_state = "move"
                    score_value += 10

                if blockX[4] == 900 and block3X - 34 < block4X + 86 and block2X + 34 > block4X - 86:
                    block_state[4] = "move"
                    score_value += 10
                    block4_state = "stable"

                # Stop
                for i in range(num_blocks):
                    if i > 3:
                        if i % 3 == 1 and i % 2 == 0:
                            if blockX[i] < blockX[i - 1] + 34 + 86:
                                block_state[i] = "stable"
                                if block_state[i + 1] == "stable" and blockX[i + 1] == -172:
                                    block_state[i + 1] = "move"
                                    score_value += 10
                                if block_state[i + 1] == "move":
                                    block_state[i] = "stable"
                            else:
                                fall(i)
                        if i % 3 == 2 and i % 2 == 1:
                            if blockX[i - 2] + 52 < blockX[i] + 172 < blockX[i - 2] + 87:
                                block_state[i] = "stable"
                                if block_state[i + 1] == "stable" and blockX[i + 1] == 900:
                                    block_state[i + 1] = "move"
                                    score_value += 10
                            if blockX[i + 1] != 900:
                                block_state[i] = "stable"
                            if not (blockX[i - 2] + 52 < blockX[i] + 172 < blockX[i - 2] + 87) and blockY[i] == blockY[
                                i - 2] - 70:
                                if blockX[i] != -172 and blockX[i + 1] == 900:
                                    block_state[i] = "fall"
                                    block_state[i - 1] = "stable"
                                    imgBlock[i] = pg.transform.rotate(imgBlock[i], -90)
                        if i % 3 == 0 and i % 2 == 0:
                            if blockX[i] <= blockX[i - 1] + 120 and blockX[i - 2] + 51 <= blockX[i] + 172:
                                if blockX[i] != 900:
                                    block_state[i] = "stable"
                                    blockX_change[i] = 0
                                if block_state[i + 1] == "stable" and blockX[i + 1] == -172:
                                    block_state[i + 1] = "move"
                                    score_value += 10
                            else:
                                fall(i)
                        if i % 3 == 1 and i % 2 == 1:
                            if blockX[i - 1] + 52 < blockX[i] + 172 < blockX[i - 1] + 87:
                                block_state[i] = "stable"
                                if block_state[i + 1] == "stable" and blockX[i + 1] == 900:
                                    block_state[i + 1] = "move"
                                    score_value += 10
                            else:
                                if blockX[i] != -172:
                                    if blockX[i - 1] != 900:
                                        block_state[i] = "fall"
                                        block_state[i - 1] = "stable"
                                        imgBlock[i] = pg.transform.rotate(imgBlock[i], -90)

                        if i % 3 == 2 and i % 2 == 0:
                            if blockX[i] <= blockX[i - 2] + 86 + 34 and blockX[i] != 900:
                                block_state[i] = "stable"
                                if block_state[i + 1] == "stable" and blockX[i + 1] == -172:
                                    block_state[i + 1] = "move"
                                    score_value += 10
                            else:
                                fall(i)
                        if i % 3 == 0 and i % 2 == 1:
                            if blockX[i] + 172 > blockX[i - 1] + 51 and blockX[i] < blockX[i - 2] + 86 + 34:
                                if blockX[i] != 900:
                                    block_state[i] = "stable"
                                    blockX_change[i] = 0
                                if boy_state == "stable" and boyX == 900 and blockX[i] != -172:
                                    boy_state = "move"
                                    score_value += 10
                            else:
                                if blockX[i] != -172:
                                    if blockX[i - 1] != 900:
                                        block_state[i] = "fall"
                                        imgBlock[i] = pg.transform.rotate(imgBlock[i], -90)

                if blockX[9] + 51 <= boyX + 45 and boyX + 151 - 52 <= blockX[9] + 120:
                    boy_state = "stable"
                    score_value = 100
                    play_sound = True

                if not (blockX[9] + 51 <= boyX + 45 and boyX + 151 - 52 <= blockX[9] + 120) and boy_state != "stable":
                    if boyX != 900:
                        boy_state = "fall"
                        boy = pg.transform.rotate(boy, 180)

            if event.key == pg.K_x:  # This loop was between those two comments below
                block2X = -172
                block2Y = 568
                block3Y = 568
                block3X = 900
                block4X = -172
                block4Y = 498
                boyX = 900
                boyY = 0
                boyX_change = 0
                boyY_change = 0
                block4X_change = 0
                block4Y_change = 0
                block2X_change = 0
                block3X_change = 0
                block3Y_change = 0
                block2Y_change = 0
                score_value = 0
                imgBlock2 = pg.image.load('images/Lego2.png')
                imgBlock3 = pg.image.load('images/Lego3.png')
                imgBlock4 = pg.image.load('images/Lego4.png')
                boy = boy1
                block2_state = "stable"
                block3_state = "stable"
                block4_state = "stable"
                boy_state = "stable"
                reset()
                restart = True
                game_lost = False
    if restart:
        screen.blit(imgBackground, (0, 0))
        score_display1()
        restart = False

    if continue_button:
        next_page()
    block2X += block2X_change
    block2Y += block2Y_change
    if block2X < 0 and block2X_change < 0:  # between last two comments
        block2X_change = -block2X_change
    if block2X > 185 and block2X_change > 0:
        block2X_change = -block2X_change

    if block2_state == "fall" and block2Y >= 568:
        block2Y_change = 5
        block2X_change = 0
    if block3_state == "fall":
        block3X_change = 0
        block3Y_change = 5
    if block4_state == "fall":
        block4Y_change = 7
        block4X_change = 0
    if boy_state == "fall":
        boyY_change = 20
        boyX_change = 0

    if block2_state == "stable":
        block2X_change = 0
        imgBlock2 = pg.image.load("images/Lego2.png")
    if block3_state == "stable":
        block3X_change = 0
    if block4_state == "stable":
        block4X_change = 0
    if boy_state == "stable":
        boyX_change = 0

    if block3X < 389 and block3_state == "move":
        block3_state = "opp_move"
    if block3X > 628 and block3X_change > 0:
        block3_state = "move"

    if boyX <= 0 and boy_state == "move":
        boy_state = "opp_move"
    if boyX + 151 >= 800 and boy_state == "opp_move":
        boy_state = "move"

    if block4_state == "move":
        block4X_change = 12
    if block4_state == "opp_move":
        block4X_change = -12

    if block3_state == "move":
        block3X_change = -10
    if block3_state == "opp_move":
        block3X_change = 10

    block_movement()

    if boy_state == "move":
        boyX_change = -15
    if boy_state == "opp_move":
        boyX_change = 15
    if boy_state == "stable":
        boyX_change = 0

    for i in range(num_blocks):
        if i > 3:
            if i % 2 == 0 and i % 3 == 1:
                if blockX[i] - 86 <= blockX[i - 1] + 17 and block_state[i] != "stable":
                    block_state[i] = "opp_move"
                if blockX[i] + 86 >= 800 - 86 and blockX_change[i] > 0 and block_state[i] != "stable":
                    block_state[i] = "move"
            if i % 2 == 1 and i % 3 == 2:
                if blockX[i] + 172 >= blockX[i - 2] + 71 and block_state[i] == "move":
                    block_state[i] = "opp_move"
                if blockX[i] <= 0 and block_state[i] == "opp_move":
                    block_state[i] = "move"
            if i % 2 == 0 and i % 3 == 0:
                if 0 >= blockX[i] and block_state[i] == "move":
                    block_state[i] = "opp_move"
                if blockX[i] + 172 >= 800 and block_state[i] == "opp_move":
                    block_state[i] = "move"
            if i % 2 == 1 and i % 3 == 1:
                if blockX[i] + 172 >= blockX[i - 1] + 71 and block_state[i] == "move":
                    block_state[i] = "opp_move"
                if blockX[i] <= 0 and block_state[i] == "opp_move":
                    block_state[i] = "move"
            if i % 2 == 0 and i % 3 == 2:
                if blockX[i] - 86 <= blockX[i - 2] + 17 and block_state[i] != "stable":
                    block_state[i] = "opp_move"
                if blockX[i] + 86 >= 800 - 86 and blockX_change[i] > 0 and block_state[i] != "stable":
                    block_state[i] = "move"
            if i % 3 == 0 and i % 2 == 1:
                if 0 >= blockX[i] and block_state[i] == "opp_move":
                    block_state[i] = "move"
                if blockX[i] + 172 >= 800 and block_state[i] == "move":
                    block_state[i] = "opp_move"

    for k in range(num_blocks):
        if block_state[k] == "stable" and k > 3:
            blockX_change[k] = 0
            blockY_change[k] = 0
            if k % 4 == 0:
                imgBlock[k] = pg.image.load('images/Lego1.png')
            if k % 4 == 1:
                imgBlock[k] = pg.image.load('images/Lego2.png')
            if k % 4 == 2:
                imgBlock[k] = pg.image.load('images/Lego3.png')
            if k % 4 == 3:
                imgBlock[k] = pg.image.load('images/Lego4.png')
        if block_state[k] == "move" and 10 > i > 3:
            if k == 4:
                blockX_change[4] = -14

            if k == 5:
                blockX_change[5] = 14
            if k % 2 == 0 and k != 4:
                blockX_change[k] = - 14 - 5 * (k - 4) / 4
            if k % 2 == 1 and i != 5:
                blockX_change[k] = 14 + 5 * (k - 5) / 4
        if block_state[k] == "opp_move" and k > 3:
            if k == 4:
                blockX_change[4] = 14
            if k == 5:
                blockX_change[5] = -14
            if k % 2 == 0 and k != 4:
                blockX_change[k] = 14 + 5 * (k - 4) / 4
            if k % 2 == 1 and i != 5:
                blockX_change[k] = - 14 - 5 * (k - 5) / 4
        if block_state[k] == "fall" and k > 3:
            blockX_change[k] = 0
            blockY_change[k] = 4 + 2 * k

    if block4X + 172 >= 800 and block4X_change > 0:
        block4_state = "opp_move"
    if block4X < 0 and block4X_change < 0:
        block4_state = "move"

    if block2Y >= 653:
        block2Y = 653
        game_lost = True
    if block3Y >= 653:
        block3Y = 653
        game_lost = True
    if block4Y >= 653:
        block4Y = 653
        game_lost = True

    for i in range(num_blocks):
        if i > 3:
            if blockY[i] >= 653:
                blockY[i] = 653
                blockY_change[i] = 0
                game_lost = True

    if boyY >= 653:
        boyY = 653
        game_lost = True

    if block2Y == 652:
        loseSound.play()

    if block3Y == 652:
        loseSound.play()

    if block4Y == 650:
        loseSound.play()

    for i in range(num_blocks):
        if blockY[i] == music_play[i]:
            loseSound.play()

    if boyY == 640:
        loseSound.play()

    block3X += block3X_change
    block3Y += block3Y_change
    block4Y += block4Y_change
    block4X += block4X_change
    boyX += boyX_change
    boyY += boyY_change
    if screen_show1 == "show_howtoplay" and screen_show2 != "show_stage1":
        screen.fill((0, 0, 0))
        next_page()
        screen.blit(how_to_play, (-55, 139.5))

    if screen_show2 == "show_stage1":
        screen.fill((0, 0, 0))
        next_page()
        screen.blit(leave_it, (-120, 110))

    if screen_show3 == "show_stage2":
        screen.fill((0, 0, 0))
        screen.blit(imgBackground, (0, 0))
        screen.blit(parents, (100, 650))
        screen.blit(villagers, (650, 525))
        score_display1()
        block2(block2X, block2Y)
        block1(block1X, block1Y)
        block3(block3X, block3Y)
        block4(block4X, block4Y)
        block_blit()
        boy_show(boyX, boyY)
    if game_lost:
        game_over()
    if score_value == 100 and play_sound and not you_win_window:
        winSound.play()

    if score_value == 100:
        time.sleep(1)
        screen.blit(Ending, (-30, 200))
        play_sound = False
        you_win_window = True

    pg.display.update()