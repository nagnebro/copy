from ursina import *

from object.npc import Npc
from object.player import Player
from object.proviso import Proviso
from object.sprite_map import SpriteMap


class MapChapter(Entity):
    def __init__(self, player_data, item_data, chapter, **kwargs):
        super().__init__(**kwargs)
        self.player_data = player_data
        self.item_data = item_data
        self.proviso = Entity()
        self.player = Player(player_data)
        # 여기서 player 객체를 생성, mapchapter는 새게임이나 계속하기 선택시 실행되는 파일임. game.py 파일에서 계속 data를 저장하고 있는 상태.
        self.passed = False
        self.pro_passed = False

        # 맵 초기화
        camera.orthographic = True
        camera.position = (0, 0)
        camera.fov = 12
        Sky(color=color.hex('4A4C50'))

        SpriteMap(parent=self, texture='map_hall1', player=self.player)
        SpriteMap(parent=self, texture='map_restroom', player=self.player, position=(-14.1, 7.15))
        SpriteMap(parent=self, texture='map_club_room', player=self.player, position=(1.5, 9.85))

        SpriteMap(parent=self, texture='map_hall2', player=self.player, position=(18.42, 5.35))
        SpriteMap(parent=self, texture='map_dorm_room', player=self.player, position=(24, 13.65))

        # 프롤로그
        # RenScene(
        #     background='',
        #     script='prologue.txt',
        #     font="NanumSquareRoundR.ttf"
        # )
        Npc(parent=self, name='학생회장', image='stu_pr_0', background='inha_ware6_hall',
            script='chapter1/chapter1.txt', target=self.player, position=(-7.2, 1)).play_animation('idle_right')
        Npc(parent=self, name='졸업생', image='gradu_0', background='inha_ware6_hall',
            script='chapter2/chapter2.txt', target=self.player, position=(-3, -1.1)).play_animation('idle_right')
        Npc(parent=self, name='동아리 선배', image='club_leader_0', background='inha_ware6_hall',
            script='chapter3/chapter3.txt', target=self.player, position=(3, 1)).play_animation('idle_left')

        self.proviso = Entity(parent=self, name='화장실', model='quad', scale=3, position=(-5, 1),
                              collider='box', color=color.gray)
        self.proviso = Entity(parent=self, name='복도', model='quad', scale=(2, 4), position=(-5, 1),
                            collider='box', color=color.azure)

        # b3 = Entity(parent=inha_map, name='동아리실', model='quad', scale=(2, 4, 1), position=(2, 4, -0.5),
        # collider='box', color=color.black)
        self.npc = Npc(parent=self, name='전 애인', image='ex_gf_0', background='inha_ware6_hall',
                       script='chapter5/chapter5.txt',
                       target=self.player, position=(4, 1))
        self.npc.play_animation('idle_right')
        # b5 = Entity(parent=inha_map, name='자취방', model='cube', scale=(4, 2, 1), position=(0, -4, -0.5),
        #             collider='box', color=color.dark_gray)

        self.npc = Npc(parent=self, name='남교수', image='prof_nam_0', background='inha_ware6_hall',
                       script='chapter4/chapter4.txt',
                       target=self.player, position=(4, 1))
        self.npc.play_animation('idle_left')
        # b4 = Entity(parent=inha_map, name='주차장', model='cube', scale=4, position=(6, 4, -2), collider='box',
        #             color=color.white)

    def update(self):
        camera.position = (self.player.x, self.player.y)

    def input(self, key): # 단서수집 포탈 근처에 갔을 떄 키를 눌러야 동작하게끔(Npc와 말거는 거처럼)
        if self.proviso.intersects(self.player) and key == 'e':
            self.pro_passed = True
            Proviso(self.player_data, self.item_data)
