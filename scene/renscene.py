from ursina import Empty, Entity, dedent, camera, color, destroy

from ui.renconversation import RenConversation


class RenScene(RenConversation):

    def __init__(self, variables_object=None):
        super().__init__(variables_object=variables_object)
        with open('_resources/script/' + variables_object.script, 'r', encoding='UTF8') as file:
            # open(파일 경로, r/w, 인코딩)

            data = file.read()
            convo = dedent(data)
            self.start_conversation(convo)

        background = Entity(parent=self, model='quad', texture='inha_ware6_hall',
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=4, world_y=0)
        npc = Entity(parent=self, model='quad', texture='chunsong', position=(0, .1),
                     scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 3), z=3)