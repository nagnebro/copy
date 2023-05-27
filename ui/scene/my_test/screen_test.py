from ursina import *

# from ursina.prefabs.conversation import Conversation

# from ui.component.renconversation import RenConversation

# 우선 내가 수정한 대화 방식으로 만들어보기. -> 선택지 없는 대화창.
from conversation_test import RenConversation


app = Ursina()
window.borderless = False;

class MyButton(Button):
    def __init__(self, entity, parent=None):
        super().__init__(model='cube', color=color.red, scale=(1, 1, 1), parent=parent)
        self.entity = entity

    def on_click(self, **kwargs):
        print("Entity clicked:", self.entity)




background = Entity(parent=camera.ui, model="quad", texture="restroom.png",
                    scale=(camera.aspect_ratio, 1),
                    color=color.white, z=4, world_y=0)  # 배경 지정

paper = Entity(parent=camera.ui, model="quad", texture="paper", color=color.white, z=4, world_y=0, scale=.2,
               x=0.1, y=0.1, )

paper2 = Entity(parent=camera.ui, model="quad", texture="paper", color=color.white, z=4, world_y=0, scale=.2
                )

button = Button(parent=camera.ui, model="quad", texture='glass', color=color.white, z=4, world_y=0, scale=.2,
                text='glass',
                x=-0.4, y=-0.4, tooltip=Tooltip('this is btn.'))


# Button


# tooltip = Tooltip('this is btn')
# tooltip은 버튼이나 draggable과 같은 클래스에만 먹는다. 상속구조 확인해봐야 할듯

isscreen = True

def open_screen():
    # 창을 생성한다.

    if isscreen :
        print(button.hovered)
        Draggable(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            scale=(.7, .4),
            z=4, world_y=0,
            color=color.color(0, 0, .1, .9),
            disabled=True,
            text='it is common glass i can\'t type korean..')



        print('창이 띄워져있음')

        return False # 창이 띄워져있으면 종료한다.

    # origin = (.5, .5), 얘는 왜 있는지 모르겠네, 얘도 아무튼 위치잡는 속성

button.on_click = open_screen


# if button.hovered_entity == None:
#     print('hi')


# mouse.hovered_entity in self.buttons -> bool type의 결과값을 반환.


# variables = Empty(
#     evil=0,
#     chaos=0,
#     bar_mission_solved=False,
# )
#
# conversation = RenConversation(variables_object=variables, parent=camera.ui)
#
# with open('./test.txt' , 'r', encoding='UTF8') as file:
#
#     data = file.read()
#     # open(파일 경로, r/w, 인코딩)
#     # 인코딩이 안되네. 일단 넘기자.
#
#     print(data)
#
# convo = dedent(data)
# print(convo)
# dedent함수는 문자열(텍스트)을 읽어서 뭐 어떤 변환? 과정을 거쳐서 text를 반환해준다.
# conversation.start_conversation(convo)


# 마우스 호버 조건에 해당하는 조건문.


app.run()
