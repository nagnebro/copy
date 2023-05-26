from ursina import *

from game.char.npc import Npc
from game.portal import Portal


class MapChapter(Entity):
    def __init__(self, target, chapter, **kwargs):
        super().__init__(**kwargs)
        ground = Entity(parent=self, model='plane', texture='brick', scale=(36, 0, 8),
                        texture_scale=(8, 8), color=color.white)
        ground.rotation_x = -90

        target.position = (0, 0, 0)

        self.portal = Portal(parent=self, position=(12, 0, 0))
        self.target = target
        self.passed = False

        if chapter == 1:
            self.npc = Npc(parent=self, name='학생회장', image='crimer1', background='inha_ware6_hall',
                script='chapter1/chapter1.txt',
                target=target, position=(1, 4))
            self.portal.set_next_chapter(2)
            b1 = Entity(parent=self, name='화장실', model='cube', scale=2, position=(-3, 1, -1), collider='box',
                        color=color.orange)

        elif chapter == 2:
            self.npc = Npc(parent=self, name='졸업생', image='crimer1', background='inha_ware6_hall',
                script='chapter2/chapter2.txt',
                target=target, position=(1, 1))
            self.portal.set_next_chapter(3)
            b2 = Entity(parent=self, name='복도', model='cube', scale=(2, 4, 1), position=(3, 1, -0.5),
                        collider='box', color=color.azure)

        elif chapter == 3:
            self.npc = Npc(parent=self, name='동아리 선배', image='crimer1', background='inha_ware6_hall',
                      script='chapter3/chapter3.txt',
                      target=target, position=(1, 4))
            self.npc.play_animation('idle_left')
            self.portal.set_next_chapter(4)
            # b3 = Entity(parent=inha_map, name='동아리실', model='cube', scale=(2, 4, 1), position=(2, 4, -0.5),
            # collider='box', color=color.black)

        elif chapter == 4:
            self.npc = Npc(parent=self, name='남교수', image='crimer1', background='inha_ware6_hall',
                      script='chapter4/chapter4.txt',
                      target=target, position=(1, 4))
            self.npc.play_animation('idle_left')
            self.portal.set_next_chapter(5)
            # b4 = Entity(parent=inha_map, name='주차장', model='cube', scale=4, position=(6, 4, -2), collider='box',
            #             color=color.white)
        elif chapter == 5:
            self.npc = Npc(parent=self, name='전 애인', image='crimer1', background='inha_ware6_hall',
                script='chapter5/chapter5.txt',
                target=target, position=(1, 4))
            self.npc.play_animation('idle_right')
            self.portal.set_next_chapter(1)
            # b5 = Entity(parent=inha_map, name='자취방', model='cube', scale=(4, 2, 1), position=(0, -4, -0.5),
            #             collider='box', color=color.dark_gray)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        if self.portal.intersects(self.target) and not self.passed:
            self.passed = True
            self.npc.disable()
            self.disable()

            MapChapter(target=self.target, chapter=self.portal.next_index)
