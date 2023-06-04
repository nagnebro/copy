from ursina import *
# from ui.scene.renscene import RenScene
# from conversation import Conversation
from ui.component.renconversation import RenConversation
from ui.scene.renscene import RenScene



app = Ursina()




# class RenScene(Entity):
#
#     def __init__(self, image, background,
#                  variables_object=None):  # variables_object = None이라는 것은 매개변수값으로 아무것도 들어오지 않을시
#         # default값으로 none을 집어넣겠다는 것. 키워드 인자이다.
#         super().__init__(parent=camera.ui)
#
#
#         self.conversation = RenConversation(variables_object=variables_object, parent=self)
#
#         with open('test.txt', 'r', encoding='UTF8') as file:
#
#
#
#             data = file.read()
#
#             convo = dedent(data)
#
#             self.conversation.start_conversation(convo)
#
#             background = Entity(parent=self.conversation, model='quad', texture=background,
#                                 scale=(camera.aspect_ratio, 1),
#                                 color=color.gray, position=(0, 0, -0))
#
#

RenScene(background = None, )

RenScene( background=None, script = "",font = "NanumSquareRoundB.ttf")

app.run()
