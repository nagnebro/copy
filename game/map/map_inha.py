from ursina import *

from game.char.npc import Npc


class MapInha(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ground = Entity(parent=self, model='plane', scale=(32, 0, 64), texture='brick', texture_scale=(2, 4),
                        position=(4, 24))
        ground.rotation_x = -90

        inha_ware_69 = Entity(parent=self, model='cube', collider='box', origin=(-.5, -.5, .5), scale=(12, 27, 0),
                              position=(9, 15))
        inha_ware_6 = Entity(parent=self, model='cube', collider='box', origin=(-.5, -.5, .5), scale=(12, 7, 3),
                             position=(9, 35), color=color.green)
        inha_ware_9 = Entity(parent=self, model='cube', collider='box', origin=(-.5, -.5, .5), scale=(12, 7, 3),
                             position=(9, 15), color=color.azure)

        inha_ware_f = Entity(parent=self, model='cube', collider='box', origin=(-.5, -.5, .5), scale=(16, 5, 2),
                             position=(-16, 0), color=color.white)

        inha_entry = Entity(parent=self, model='cube', collider='cube', origin=(-.5, -.5, .5), scale=(1.2, 1.7, 1),
                            position=(2.2, -1.7), color=color.white)

        # road = Entity(parent=self, model='cube', scale=(1.5, 128, 0.1), origin=(-.5, -.5, .5), color=color.black,
        #               position=(3.4, -64))

        inha_wall = Entity(parent=self, model='cube', collider='cube', origin=(-.5, -.5, .5), texture='grass',
                           scale=(16, .5, 1),
                           position=(-16, -2), color=color.white)

    @staticmethod
    def place_npc(target):
        # 이벤트 npc
        npc1 = Npc(name='학생회장', script='chapter1/chapter1.txt', target=target, position=(1, 4))
        npc1.play_animation('idle_right')
        # b1 = Entity(parent=inha_map, name='화장실', model='cube', scale=2, position=(-3, 1, -1), collider='box',
        #             color=color.orange)

        npc2 = Npc(name='졸업생', script='chapter2/chapter2.txt', target=target, position=(1, 8))
        npc2.play_animation('idle_right')
        # b2 = Entity(parent=inha_map, name='복도', model='cube', scale=(2, 4, 1), position=(0, 4, -0.5),
        # collider='box', color=color.azure)

        npc3 = Npc(name='동아리 선배', script='chapter3/chapter3.txt', target=target, position=(9, 14))
        npc3.play_animation('idle_left')
        # b3 = Entity(parent=inha_map, name='동아리실', model='cube', scale=(2, 4, 1), position=(2, 4, -0.5),
        # collider='box', color=color.black)

        npc4 = Npc(name='남교수', script='chapter4/chapter4.txt', target=target, position=(9, 7))
        npc4.play_animation('idle_left')
        # b4 = Entity(parent=inha_map, name='주차장', model='cube', scale=4, position=(6, 4, -2), collider='box',
        #             color=color.white)

        npc5 = Npc(name='전 애인', script='chapter5/chapter5.txt', target=target, position=(2.2, -2))
        npc5.play_animation('idle_right')
        # b5 = Entity(parent=inha_map, name='자취방', model='cube', scale=(4, 2, 1), position=(0, -4, -0.5),
        #             collider='box', color=color.dark_gray)
