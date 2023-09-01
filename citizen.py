from player import Player

list_vote = []

class Citizen(Player):
    def __init__(self, user_name, user_box, user_status, model, canvas):
        super(Citizen, self).__init__(user_name, user_box, user_status, model, canvas)

    def want_vote(self, use_vote):
        """Выставить на голосование"""
        if self.user_status == 1:
            if use_vote == 1:
                return True

    def vote(self):
        if self.user_status == 1:
            bad_guy = int(input('who is a bad guy'))
            list_vote.append(bad_guy)

