from ursina import *
# from ui.scene.renscene import RenScene
# from conversation import Conversation
from ui.component.renconversation import RenConversation
# from ui.scene.renscene import RenScene




app = Ursina()

window.borderless = False




class RenScene(Entity):

    def __init__(self, image, background,
                 variables_object=None):  # variables_object = None이라는 것은 매개변수값으로 아무것도 들어오지 않을시
        # default값으로 none을 집어넣겠다는 것. 키워드 인자이다.
        super().__init__(parent=camera.ui)


        self.conversation = RenConversation(variables_object=variables_object, parent=self)

        with open('script/test.txt', 'r', encoding='UTF8') as file:

            # open(파일 경로, r/w, 인코딩)
#'_resources/script/'+variables_object

            data = file.read()

            convo = dedent(data)

            self.conversation.start_conversation(convo)


        background = Entity(parent=self.conversation, model='quad', texture=background,
                            scale=(camera.aspect_ratio, 1),
                            color=color.black, z=4, world_y=0)

# npc = Entity(parent=self.conversation, model='quad', texture=image, position=(0, .1),
#              scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 3), z=3)
#

background  = Entity(
    color = color.black,
    model = 'quad',
    parent = camera.ui,
    scale = (camera.aspect_ratio,1),
    z= -3
)




#
# result = RenScene(
#     image = None,
#     background= None,
#     parent = background
#
#
#     # variables_object="script/test.txt" # .txt까지 붙여야함
#
# )
#





app.run()