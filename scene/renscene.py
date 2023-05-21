from ursina import Empty, Entity, dedent, camera, color

from ui.renconversation import RenConversation


class RenScene(Entity):

    def __init__(self, variables_object=None, **kwargs):
        super().__init__(**kwargs)
        conversation = RenConversation(variables_object=variables_object)
        with open('_resources/script/chunsong/chunsong_0.txt', 'r', encoding='UTF8') as file:
            # open(파일경로, read로 불러올건지 wrtie로 불러온건지(아마도), 인코딩)


            data = file.read()
            convo = dedent(data)
            conversation.start_conversation(convo)

        background = Entity(parent=conversation, model='quad', texture='inha_ware6_hall',
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=4, world_y=0)
        npc = Entity(parent=conversation, model='quad', texture='chunsong', position=(0, .1),
                     scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 3), z=3)
