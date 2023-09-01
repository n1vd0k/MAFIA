
class Player:
    def __init__(self, user_name, user_box, user_status, model, canvas):
        self.user_name = user_name
        # self.user_rol = user_rol
        self.user_box = user_box
        self.user_status = user_status
        self.user_foll = 0
        self.model = model
        self.canvas = canvas

    def __str__(self):
        return self.user_name

    def get_box(self, num_box):
        self.user_box = num_box

    def change(self,x1,y1,x2,y2,b):
        if self.user_status == 1:
            self.model = self.canvas.create_oval(x1,y1,x2,y2, outline='white',fill=b)

    def dead(self):
        self.user_status = 0

    def killed(self):
        return self.model

    @property
    def list_user_name(self):
        """Получить имя игрока"""
        return self.user_name

    @property
    def list_user_box(self):
        """Получить место на котором сидит игрок"""
        return self.user_box

    @property
    def list_user_status(self):
        """Получить статус жизни игрока"""
        return self.user_status
