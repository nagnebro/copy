from ursina import *

from object.find_place import FindPlace
from object.sprite_map import SpriteMap
from object.npc import Npc
from object.player import Player
from ui.scene.find_proviso import Find_Proviso


class MapChapter(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.proviso = Entity()
        self.player = Player(game.player_data)
        # 여기서 player 객체를 생성, mapchapter는 새게임이나 계속하기 선택시 실행되는 파일임. game.py 파일에서 계속 data를 저장하고 있는 상태.
        self.passed = False
        self.pro_passed = False

        # 맵 초기화
        camera.orthographic = True
        camera.position = (0, 0)
        camera.fov = 12
        Sky(color=color.hex('4A4C50'))

        # 프롤로그
        # RenScene(
        #     background='',
        #     script='prologue.txt',
        #     font="NanumSquareRoundR.ttf"
        # )

        SpriteMap(parent=self, texture='map_hall1', player=self.player)
        Npc(parent=self, name='학생회장', image='stu_pr_0', background='entrance1',
            script='chapter1/chapter1.txt', target=self.player, position=(-7.2, 1)).play_animation('idle_right')
        Npc(parent=self, name='졸업생', image='gradu_0', background='third_floor',
            script='chapter2/chapter2.txt', target=self.player, position=(-3, -1.1)).play_animation('idle_right')
        Npc(parent=self, name='동아리 선배', image='club_leader_0', background='second_floor1',
            script='chapter3/chapter3.txt', target=self.player, position=(3, 1)).play_animation('idle_left')
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=2,
                                 name='복도', model='quad', position=(-6, -1),
                                 collider='box', color=color.azure)

        SpriteMap(parent=self, texture='map_restroom', player=self.player, position=(-14.1, 7.15))
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=1,
                                 name='화장실', model='quad', position=(-14, 8),
                                 collider='box', color=color.gray)

        SpriteMap(parent=self, texture='map_club_room', player=self.player, position=(1.5, 9.85))
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=3,
                                 name='동아리실', model='quad', position=(1.5, 12),
                                 collider='box', color=color.gray)

        hall2 = SpriteMap(parent=self, texture='map_hall2', player=self.player, position=(18.42, 5.35))
        Npc(parent=self, name='전 애인', image='ex_gf_0', background='gf1',
            script='chapter5/chapter5.txt', target=self.player, position=(18, 6)).play_animation('idle_left')

        SpriteMap(parent=self, texture='map_dorm_room', player=self.player, position=(24, 13.65))
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=5,
                                 name='자취방', model='quad', position=(24, 15),
                                 collider='box', color=color.gray)

        Npc(parent=self, name='남교수', image='prof_nam_0', background='garage',
            script='chapter4/chapter4.txt', target=self.player, position=(12, -4)).play_animation('idle_left')
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=4,
                                 name='주차장', model='quad', position=(14, -4),
                                 collider='box', color=color.gray)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        camera.position = (self.player.x, self.player.y)
