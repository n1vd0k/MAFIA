from player import Player

mafia_kill = []  # list куда записываются выстрелы мафии

class Mafiozi(Player):
    def __init__(self, user_name, user_box, user_status, model, canvas):
        super(Mafiozi, self).__init__(user_name, user_box, user_status, model, canvas)


    def user_roll_mafia_shot(self,btn):
        """Выстрел мафии"""
        if self.user_status == 1:
            mafia_kill.append(btn)


