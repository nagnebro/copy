
from ursina import *


from prec.my_test.chapter6_test import RenScene
# from ui.scene.renscene import RenScene
# from conversation import Conversation
from ui.component.renconversation import RenConversation


# from ui.scene.renscene import RenScene





app = Ursina()

window.borderless = False

# texture를 못 일겅온다. main에서부터 시작된 파일이 아니끼 때문에 상대경로로 파일찾음.
# class Test1:
#     def __init__(self):
#         Entity(model='quad',  color=color.black, parent=camera.ui, scale =(camera.aspect_ratio,1))
#         Test2()
#
# class Test2:
#     def __init__(self):
#         print('hi')
#
#         Entity(model='quad',  color=color.red, parent=camera.ui, scale =1)







# Test2()



app.run()