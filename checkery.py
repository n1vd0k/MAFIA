from player import Player
from citizen import Citizen
from mafiozi import Mafiozi




class Sherif(Player):
    def __init__(self, user_name, user_box, user_status, model, canvas):
        super(Sherif, self).__init__(user_name, user_box, user_status, model, canvas)




    def user_roll_sherif_check(self, p_list,btn):
        """Проверка шерифа"""
        if self.user_status == 1:
            btn -= 1
            if isinstance(p_list[btn], Sherif):
                print('PASS')
                pass
            elif isinstance(p_list[btn], Don) or isinstance(p_list[btn], Mafiozi):
                self.canvas.delete(p_list[btn].killed())
                if p_list[btn].user_box == 0:
                    p_list[btn].change(350, 100, 450, 200, 'red')
                elif p_list[btn].user_box == 1:
                    p_list[btn].change(485, 140, 585, 240, 'red')
                elif p_list[btn].user_box == 2:
                    p_list[btn].change(575, 250, 675, 350, 'red')
                elif p_list[btn].user_box == 3:
                    p_list[btn].change(575, 450, 675, 550, 'red')
                elif p_list[btn].user_box == 4:
                    p_list[btn].change(485, 560, 585, 660, 'red')
                elif p_list[btn].user_box == 5:
                    p_list[btn].change(350, 600, 450, 700, 'red')
                elif p_list[btn].user_box == 6:
                    p_list[btn].change(215, 560, 315, 660, 'red')
                elif p_list[btn].user_box == 7:
                    p_list[btn].change(125, 450, 225, 550, 'red')
                elif p_list[btn].user_box == 8:
                    p_list[btn].change(125, 250, 225, 350, 'red')
                elif p_list[btn].user_box == 9:
                    p_list[btn].change(215, 140, 315, 240, 'red')
            elif isinstance(p_list[btn], Citizen):
                self.canvas.delete(p_list[btn].killed())
                if p_list[btn].user_box == 0:
                    p_list[btn].change(350, 100, 450, 200, 'white')
                elif p_list[btn].user_box == 1:
                    p_list[btn].change(485, 140, 585, 240, 'white')
                elif p_list[btn].user_box == 2:
                    p_list[btn].change(575, 250, 675, 350, 'white')
                elif p_list[btn].user_box == 3:
                    p_list[btn].change(575, 450, 675, 550, 'white')
                elif p_list[btn].user_box == 4:
                    p_list[btn].change(485, 560, 585, 660, 'white')
                elif p_list[btn].user_box == 5:
                    p_list[btn].change(350, 600, 450, 700, 'white')
                elif p_list[btn].user_box == 6:
                    p_list[btn].change(215, 560, 315, 660, 'white')
                elif p_list[btn].user_box == 7:
                    p_list[btn].change(125, 450, 225, 550, 'white')
                elif p_list[btn].user_box == 8:
                    p_list[btn].change(125, 250, 225, 350, 'white')
                elif p_list[btn].user_box == 9:
                    p_list[btn].change(215, 140, 315, 240, 'white')

class Don(Mafiozi):
    def __init__(self, user_name, user_box, user_status, model, canvas):
        super(Don, self).__init__(user_name, user_box, user_status,model, canvas)

    def user_roll_don_check(self, p_list,btn):
        if self.user_status == 1:
            btn -= 1
            if isinstance(p_list[btn], Don) or isinstance(p_list[btn], Mafiozi):
                print('PASS')
                pass
            elif isinstance(p_list[btn], Citizen):
                self.canvas.delete(p_list[btn].killed())
                if p_list[btn].user_box == 0:
                    p_list[btn].change(350, 100, 450, 200, 'white')
                elif p_list[btn].user_box == 1:
                    p_list[btn].change(485, 140, 585, 240, 'white')
                elif p_list[btn].user_box == 2:
                    p_list[btn].change(575, 250, 675, 350, 'white')
                elif p_list[btn].user_box == 3:
                    p_list[btn].change(575, 450, 675, 550, 'white')
                elif p_list[btn].user_box == 4:
                    p_list[btn].change(485, 560, 585, 660, 'white')
                elif p_list[btn].user_box == 5:
                    p_list[btn].change(350, 600, 450, 700, 'white')
                elif p_list[btn].user_box == 6:
                    p_list[btn].change(215, 560, 315, 660, 'white')
                elif p_list[btn].user_box == 7:
                    p_list[btn].change(125, 450, 225, 550, 'white')
                elif p_list[btn].user_box == 8:
                    p_list[btn].change(125, 250, 225, 350, 'white')
                elif p_list[btn].user_box == 9:
                    p_list[btn].change(215, 140, 315, 240, 'white')
            elif isinstance(p_list[btn], Sherif):
                self.canvas.delete(p_list[btn].killed())
                if p_list[btn].user_box == 0:
                    p_list[btn].change(350, 100, 450, 200, 'blue')
                elif p_list[btn].user_box == 1:
                    p_list[btn].change(485, 140, 585, 240, 'blue')
                elif p_list[btn].user_box == 2:
                    p_list[btn].change(575, 250, 675, 350, 'blue')
                elif p_list[btn].user_box == 3:
                    p_list[btn].change(575, 450, 675, 550, 'blue')
                elif p_list[btn].user_box == 4:
                    p_list[btn].change(485, 560, 585, 660, 'blue')
                elif p_list[btn].user_box == 5:
                    p_list[btn].change(350, 600, 450, 700, 'blue')
                elif p_list[btn].user_box == 6:
                    p_list[btn].change(215, 560, 315, 660, 'blue')
                elif p_list[btn].user_box == 7:
                    p_list[btn].change(125, 450, 225, 550, 'blue')
                elif p_list[btn].user_box == 8:
                    p_list[btn].change(125, 250, 225, 350, 'blue')
                elif p_list[btn].user_box == 9:
                    p_list[btn].change(215, 140, 315, 240, 'blue')
