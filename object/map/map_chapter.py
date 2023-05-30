from ursina import *

from object.char.npc import Npc
from object.char.player import Player
from object.portal import Portal
from object.proviso import Proviso


class MapChapter(Entity):
    def __init__(self, player_data, chapter, **kwargs):
        super().__init__(**kwargs)
        self.player_data = player_data
        self.proviso = Entity()
        self.portal = Portal(parent=self, position=(12, 0, 0))
        self.player = Player(player_data)  # 여기서 player 객체를 생성, mapchapter는 새게임이나 계속하기 선택시 실행되는 파일임. game.py 파일에서 계속 data를 저장하고 있는 상태.
        self.passed = False
        self.pro_passed = False


        # 맵 초기화
        EditorCamera(enabled=False, ignore_paused=True)
        Sky(color=color.black)
        ground = Entity(parent=self, model='plane', texture='brick', scale=(36, 0, 8),
                        texture_scale=(8, 8), color=color.white)
        ground.rotation_x = -90
        wall = Entity(parent=self, model='plane', texture='hall', scale=(36, 0, 8),
                      position=(0, 5, -.2), texture_scale=(1, 1), color=color.white)
        wall.rotation_x = -180
        self.player.position = (0, 0, 0)


        # 챕터 별 배치
        if chapter == 1:
            self.npc = Npc(parent=self, name='학생회장', image='stu_pr_0', background='inha_ware6_hall',
                           script='chapter1/chapter1.txt',
                           target=self.player, position=(1, 4))
            self.portal.set_next_chapter(2)
            self.proviso = Entity(parent=self, name='화장실', model='cube', scale=2, position=(-3, 1, -1),
                                  collider='box', color=color.orange)

        elif chapter == 2:
            self.npc = Npc(parent=self, name='졸업생', image='gradu_0', background='inha_ware6_hall',
                           script='chapter2/chapter2.txt',
                           target=self.player, position=(1, 1))
            self.portal.set_next_chapter(3)
            self.proviso = Entity(parent=self, name='복도', model='cube', scale=(2, 4, 1), position=(3, 1, -0.5),
                        collider='box', color=color.azure)

        elif chapter == 3:
            self.npc = Npc(parent=self, name='동아리 선배', image='club_leader_0', background='inha_ware6_hall',
                           script='chapter3/chapter3.txt',
                           target=self.player, position=(1, 4))
            self.npc.play_animation('idle_left')
            self.portal.set_next_chapter(4)
            # b3 = Entity(parent=inha_map, name='동아리실', model='cube', scale=(2, 4, 1), position=(2, 4, -0.5),
            # collider='box', color=color.black)

        elif chapter == 4:
            self.npc = Npc(parent=self, name='남교수', image='prof_nam_0', background='inha_ware6_hall',
                           script='chapter4/chapter4.txt',
                           target=self.player, position=(1, 4))
            self.npc.play_animation('idle_left')
            self.portal.set_next_chapter(5)
            # b4 = Entity(parent=inha_map, name='주차장', model='cube', scale=4, position=(6, 4, -2), collider='box',
            #             color=color.white)
        elif chapter == 5:
            self.npc = Npc(parent=self, name='전 애인', image='ex_gf_0', background='inha_ware6_hall',
                           script='chapter5/chapter5.txt',
                           target=self.player, position=(1, 4))
            self.npc.play_animation('idle_right')
            self.portal.set_next_chapter(1)
            # b5 = Entity(parent=inha_map, name='자취방', model='cube', scale=(4, 2, 1), position=(0, -4, -0.5),
            #             collider='box', color=color.dark_gray)

        for key, value in kwargs.items():
            setattr(self, key, value)



    def check(self):
        input()
        return True

    def input(self,key=None):
        if key == "x":
            print(key)
            return True


    def update(self):
        camera.rotation_x = -45
        camera.position = (camera.position.x, self.player.y - 18, -18)
        if self.player.x < 12:
            camera.position = (self.player.x, self.player.y - 18, -18)


        # print(self.portal.intersects(self.player),self.passed)
        if  self.portal.intersects(self.player) and not self.passed:

            self.passed = True
            self.npc.disable()
            self.player.disable()
            self.proviso.disable()
            self.disable()

            self.player.data.chapter = self.portal.next_index
            # print(self.player.data.chapter)
            MapChapter(player_data=self.player.data, chapter=self.portal.next_index)



    def input(self,key): # 단서수집 포탈 근처에 갔을 떄 키를 눌러야 동작하게끔(Npc와 말거는 거처럼)

        if self.proviso.intersects(self.player) and key == 'e':

            self.pro_passed = True
            Proviso(self.player_data)
