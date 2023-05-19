from ursina import Empty, Entity, dedent, camera, color, Cursor, mouse, Func
from ursina.prefabs.draggable import Draggable
from ui.inventory import Inventory


class FindScene(Entity):

    def __init__(self, inven, variables_object=None, **kwargs):
        super().__init__(**kwargs)
        # conversation = RenConversation(variables_object=variables_object)
        # with open('_resources/script/chunsong/chunsong_0.txt', 'r', encoding='UTF8') as file:
        #     data = file.read()
        #     convo = dedent(data)
        #     conversation.start_conversation(convo)
        # Cursor(texture='cursor', scale=.1)

        self.parent = camera.ui

        background = Entity(parent=self, model='quad', texture='inha_ware6_hall',
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=8, world_y=0)

        item1 = Draggable(model='quad', texture='paper', name='paper', color=color.white, origin=(-.5, .5),
                          scale=(.2, 1), x=.4, y=3, z=-1)
        item2 = Draggable(model='quad', texture='glass', name='glass', color=color.white, origin=(-.5, .5),
                          scale=(.2, 1), x=.6, y=5, z=-1)

        item1.parent = inven
        item2.parent = inven
        inven.append(item1)
        inven.append(item2)

    def input(self, key):
        if key == 'b':
            print('wtf?')
            self.disable()
            Func(setattr, self, 'enabled', False)
