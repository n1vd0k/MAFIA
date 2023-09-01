import time
from tkinter import *
import random
from citizen import Citizen,list_vote
from mafiozi import Mafiozi, mafia_kill
from checkery import Sherif, Don


root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()

lobby = ["Name1", "Name2", "Name3", "Name4", "Name5", "Name6", "Name7", "Name8", "Name9", "Name10"]
random.shuffle(lobby)
rols = [Citizen(lobby[0], 0, 1, 0, c),
        Citizen(lobby[1], 0, 1, 0, c),
        Citizen(lobby[2], 0, 1, 0, c),
        Citizen(lobby[3], 0, 1, 0, c),
        Citizen(lobby[4], 0, 1, 0, c),
        Citizen(lobby[5], 0, 1, 0, c),
        Mafiozi(lobby[6], 0, 1, 0, c),
        Mafiozi(lobby[7], 0, 1, 0, c),
        Don(lobby[8], 0, 1, 0, c),
        Sherif(lobby[9], 0, 1, 0, c)]
random.shuffle(rols)


players = []
for i in range(len(lobby)):
    rols[i].get_box(i)
    players.append(rols[i])


c.create_oval(350, 100, 450, 200, outline='white')
c.create_oval(350, 600, 450, 700, outline='white')

c.create_oval(575, 450, 675, 550, outline='white')
c.create_oval(575, 250, 675, 350, outline='white')

c.create_oval(125, 450, 225, 550, outline='white')
c.create_oval(125, 250, 225, 350, outline='white')

c.create_oval(215, 140, 315, 240, outline='white')
c.create_oval(215, 560, 315, 660, outline='white')

c.create_oval(485, 140, 585, 240, outline='white')
c.create_oval(485, 560, 585, 660, outline='white')

c.create_oval(200, 200, 600, 600, outline='red', fill='brown')


for i in players:
    if i.user_box == 0:
        i.change(350, 100, 450, 200, 'gray')
    elif i.user_box == 1:
        i.change(485, 140, 585, 240, 'gray')
    elif i.user_box == 2:
        i.change(575, 250, 675, 350, 'gray')
    elif i.user_box == 3:
        i.change(575, 450, 675, 550, 'gray')
    elif i.user_box == 4:
        i.change(485, 560, 585, 660, 'gray')
    elif i.user_box == 5:
        i.change(350, 600, 450, 700, 'gray')
    elif i.user_box == 6:
        i.change(215, 560, 315, 660, 'gray')
    elif i.user_box == 7:
        i.change(125, 450, 225, 550, 'gray')
    elif i.user_box == 8:
        i.change(125, 250, 225, 350, 'gray')
    elif i.user_box == 9:
        i.change(215, 140, 315, 240, 'gray')


def check_game_over():
    count_mafia = 0
    count_citizen = 0
    for i in players:
        if i.list_user_status == 1:
            if isinstance(i, Mafiozi) or isinstance(i, Don):
                count_mafia += 1
            if isinstance(i, Citizen) or isinstance(i, Sherif):
                count_citizen += 1
    if count_mafia == count_citizen:
        return False
    else:
        return True
nums = [1,2,3,4,5,6,7,8,9,10]


def game():
    while True:
        for i in players:
            if i.list_user_status == 1:
                root.update()
        if check_game_over():
            print('','Night start','',sep='\n')
            root.update()
            btn = random.choice(nums)
            time.sleep(1)

            for i in players:
                if isinstance(i, Mafiozi) or isinstance(i, Don) and i.list_user_status == 1:
                    i.user_roll_mafia_shot(btn)
                    root.update()
            btn = random.choice(nums)
            time.sleep(1)
            for i in players:
                if isinstance(i, Don) and i.list_user_status == 1:  # Проверка дона
                    i.user_roll_don_check(players, btn)
                    root.update()
            btn = random.choice(nums)
            time.sleep(1)
            for i in players:
                if isinstance(i, Sherif) and i.list_user_status == 1:  # Проверка шерифа
                    i.user_roll_sherif_check(players,btn)
                    root.update()
            count_yes = 0
            for i in players:
                if isinstance(i, Citizen):
                    if i.want_vote(random.randint(0, 1)):
                        count_yes += 1
                    if count_yes > 3:
                        i.vote()
                        break
                root.update()

            if not(isinstance(players[mafia_kill[0]-1], Mafiozi)) == 1:
                if players[mafia_kill[0]-1].user_status == 1:
                    players[mafia_kill[0] - 1].dead()
                    c.delete(players[mafia_kill[0] - 1].killed())
                    mafia_kill.clear()
                    root.update()
                else:
                    print('Mafia cann`t kill dead person')
                    mafia_kill.clear()
                    root.update()
            else:
                mafia_kill.clear()
            if count_yes > 3:
                if players[list_vote[0]-1].user_status == 1:

                    players[list_vote[0]-1].dead()
                    c.delete(players[list_vote[0] - 1].killed())
                    if players[list_vote[0] - 1].user_box == 0:
                        players[list_vote[0] - 1].change(350, 100, 450, 200, 'pink')
                    elif players[list_vote[0] - 1].user_box == 1:
                        players[list_vote[0] - 1].change(485, 140, 585, 240, 'pink')
                    elif players[list_vote[0] - 1].user_box == 2:
                        players[list_vote[0] - 1].change(575, 250, 675, 350, 'pink')
                    elif players[list_vote[0] - 1].user_box == 3:
                        players[list_vote[0] - 1].change(575, 450, 675, 550, 'pink')
                    elif players[list_vote[0] - 1].user_box == 4:
                        players[list_vote[0] - 1].change(485, 560, 585, 660, 'pink')
                    elif players[list_vote[0] - 1].user_box == 5:
                        players[list_vote[0] - 1].change(350, 600, 450, 700, 'pink')
                    elif players[list_vote[0] - 1].user_box == 6:
                        players[list_vote[0] - 1].change(215, 560, 315, 660, 'pink')
                    elif players[list_vote[0] - 1].user_box == 7:
                        players[list_vote[0] - 1].change(125, 450, 225, 550, 'pink')
                    elif players[list_vote[0] - 1].user_box == 8:
                        players[list_vote[0] - 1].change(125, 250, 225, 350, 'pink')
                    elif players[list_vote[0] - 1].user_box == 9:
                        players[list_vote[0] - 1].change(215, 140, 315, 240, 'pink')
                    list_vote.clear()
                    root.update()
                else:
                    print('People cann`t kill dead person')
                    list_vote.clear()
                    root.update()
        else:
            print('Game over')
            print('Mafia loses')
            exit()

        root.update()
game()
root.mainloop()
