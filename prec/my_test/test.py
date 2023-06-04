
from ursina import *


# from prec.my_test.chapter6_test import RenScene
# from ui.scene.renscene import RenScene
# from conversation import Conversation
from ui.component.renconversation import RenConversation


# from ui.scene.renscene import RenScene





app = Ursina()

window.borderless = False


Entity(model = 'quad', color = color.red, scale  = 0.3, x=.2, y=1)
Entity(model = 'quad', color = color.blue, scale  = 0.5, position = (3,0,0))



app.run()