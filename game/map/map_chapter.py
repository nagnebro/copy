from ursina import *

from game.char.npc import Npc


class MapChapter(Entity):
    def __init__(self, target, chapter, **kwargs):
        super().__init__(**kwargs)
        ground = Entity(parent=self, model='plane', texture='brick', collider='box', scale=(36, 0, 8),
                        texture_scale=(8, 8), color=color.white)
        ground.rotation_x = -90

        if chapter == 1:
            npc1 = Npc(name='학생회장', image='crimer1', background='inha_ware6_hall', script='chapter1/chapter1.txt',
                       target=target, position=(1, 4))
            npc1.play_animation('idle_right')
            # b1 = Entity(parent=inha_map, name='화장실', model='cube', scale=2, position=(-3, 1, -1), collider='box',
            #             color=color.orange)

        elif chapter == 2:
            npc2 = Npc(name='졸업생', image='crimer1', background='inha_ware6_hall', script='chapter2/chapter2.txt',
                       target=target, position=(1, 4))
            npc2.play_animation('idle_right')
            # b2 = Entity(parent=inha_map, name='복도', model='cube', scale=(2, 4, 1), position=(0, 4, -0.5),
            # collider='box', color=color.azure)

        elif chapter == 3:
            npc3 = Npc(name='동아리 선배', image='crimer1', background='inha_ware6_hall', script='chapter3/chapter3.txt',
                       target=target, position=(1, 4))
            npc3.play_animation('idle_left')
            # b3 = Entity(parent=inha_map, name='동아리실', model='cube', scale=(2, 4, 1), position=(2, 4, -0.5),
            # collider='box', color=color.black)

        elif chapter == 4:
            npc4 = Npc(name='남교수', image='crimer1', background='inha_ware6_hall', script='chapter4/chapter4.txt',
                       target=target, position=(1, 4))
            npc4.play_animation('idle_left')
            # b4 = Entity(parent=inha_map, name='주차장', model='cube', scale=4, position=(6, 4, -2), collider='box',
            #             color=color.white)
        elif chapter == 5:
            npc5 = Npc(name='전 애인', image='crimer1', background='inha_ware6_hall', script='chapter5/chapter5.txt',
                       target=target, position=(1, 4))
            npc5.play_animation('idle_right')
            # b5 = Entity(parent=inha_map, name='자취방', model='cube', scale=(4, 2, 1), position=(0, -4, -0.5),
            #             collider='box', color=color.dark_gray)
