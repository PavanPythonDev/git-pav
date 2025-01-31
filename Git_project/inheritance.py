class vechicle:
    def __init__(self,brand):
        self.brand

class Car(vechicle):
    def __init__(self,brand,model):
        vechicle.__init__(self,brand)
        self.model

    def info(self):
        return f'{self.brand,self.model}'

