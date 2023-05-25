from ursina import Empty, Entity, dedent, camera, color

from ui.renconversation import RenConversation


class Chapter3_test(Entity):

    def __init__(self, variables_object=None, **kwargs):
        super().__init__(**kwargs)
        conversation = RenConversation(variables_object=variables_object)

        with open('_resources/script/chapter3/chapter3.txt', encoding='UTF8') as file:
            data = file.read()
            convo = dedent(data)
            conversation.start_conversation(convo)

        background = Entity(parent=conversation, model='quad', texture='inha_background.jpg',
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=4, world_y=0)
        npc = Entity(parent=conversation, model='quad', texture='crimer1', position=(0, .1),
                     scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 3), z=3)
        # background 와 npc 변수에 저장되는 값은? Entity 클래스의 생성자에 return값이 없는 것 같은데 어쨋든 인스턴스
        # 생성만으로 screen에 실행됨.
