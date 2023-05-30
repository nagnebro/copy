
from ursina import *

app = Ursina()


mm = Button(model = 'quad', color = color.red ,scale = 0.3 , enabled= False)


def hi():
    print('hi')
mm.on_click = hi


app.run()

class parent1:
    def parent1_method(self):
        print('hi')

class parent2:
    def parent2_method(self):
        print('bye')


class child(parent1,parent2):

    def __init__(self):
        pass

c = child()
