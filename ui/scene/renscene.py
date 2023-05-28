from ursina import Entity, dedent, camera, color

from ui.component.renconversation import RenConversation


class RenScene(Entity):

    def __init__(self, image, background, script, font, variables_object=None):   # variables_object = None이라는 것은 매개변수값으로 아무것도 들어오지 않을시
                                                                    # default값으로 none을 집어넣겠다는 것.
        super().__init__(parent=camera.ui)

        conversation = RenConversation(parent=self, font=font, variables_object=variables_object)
        with open('_resources/script/' + script, 'r', encoding='UTF8') as file:
            # open(파일 경로, r/w, 인코딩)

            data = file.read()
            convo = dedent(data)
            conversation.start_conversation(convo)

        background = Entity(parent=conversation, model='quad', texture=background,
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=4, world_y=0)
        npc = Entity(parent=conversation, model='quad', texture=image, position=(0, .1),
                     scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 3), z=3)
