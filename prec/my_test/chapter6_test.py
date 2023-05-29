from ursina import *
# from ui.scene.renscene import RenScene
# from conversation import Conversation
from ui.component.renconversation import RenConversation
# from ui.scene.renscene import RenScene


# import os

# # 현재 스크립트의 절대 경로
# script_dir = os.path.dirname(os.path.abspath(__file__))
#

# file open할떄 절대경로로 할지 상대경로로 할지 정해야 하는데
# 상대경로가 안전할 듯 하다.
# 다만 상대경로로 할 경우 현재 파일의 위치가 바뀔 경우 계속해서 수정해줘야 한다.

# # 파일의 절대 경로
# file_path = os.path.join(script_dir, 'projectI/_resources/test.txt')


# 만들어야 할 것. renconveersation 을 우리가 구현해야 할 게임 스타일에 맞게 바꿀 것.
# 1.우선 선택지로 나타나는 버튼의 객체를 늘릴 것.
# 2. 버튼의 객체가 가지고 있는 값이나 버튼 리스트의 인덱스를 이용해서 선택한 것이 무엇인지 저장할 수 있어야 함.
# 용의자에 대한 정리를 하기 위해서는.. 현재 출력되고 있는 텍스트가 몇번째인지 알아야 한다.


# 3. 비단 용의자 선택뿐만 아니라 대화를 통해 얻게 된 키워드 따위를 사전이나, 보드에 추가할 수 있어야함.
# 3번 부분은 사용자가 그냥 텕스트 입력하면 입력하게끔 만들어도 되기는 함.


app = Ursina()

window.borderless = False

btn_list = []


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
                            color=color.white, z=4, world_y=0)
        npc = Entity(parent=self.conversation, model='quad', texture=image, position=(0, .1),
                     scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 3), z=3)



result = RenScene(
    image = None,
    background= None,
    variables_object="test.txt" # .txt까지 붙여야함

)

# def success():
#     Entity( parent = camera.ui,  scale=(camera.aspect_ratio, 1), color = color.green )
#     Entity(parent = camera.ui,  scale= .4, color = color.blue, text = "success")
#
# def gameOver():
#     Entity( parent = camera.ui,  scale=(camera.aspect_ratio, 1), color = color.green )
#     Entity(parent = camera.ui,  scale= .4, color = color.blue, text = "Game Over")
#
#
# def result2():
#     answer = result.conversation.list
#     if answer != '학생회장' :
#         success()
#         return
#     gameOver()


def success(self):
    Entity(parent=camera.ui, scale=(camera.aspect_ratio, 1), model='quad', color=color.red)
    Entity(parent=camera.ui, scale=.4, color=color.blue, model='quad', text="success")
    print('success')


def gameOver(self):
    Entity(parent=camera.ui, scale=(camera.aspect_ratio, 1), model='quad', color=color.green)
    Entity(parent=camera.ui, scale=.4, color=color.blue, model='quad', text="Game Over")
    print('gameOver')


def result2(self):
    print('hi')


mm = Button(scale = .3, color = color.red, z=-1)




app.run()