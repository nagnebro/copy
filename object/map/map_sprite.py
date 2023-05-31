from ursina import *

from ui.scene.renscene import RenScene
from object.char.npc import Npc
from object.char.player import Player
from object.portal import Portal
from object.proviso import Proviso


class MapSprite(Entity):
    def __init__(self, player_data, chapter, **kwargs):
        super().__init__(**kwargs)
        self.player_data = player_data
        self.proviso = Entity()
        self.portal = Portal(parent=self, position=(12, 0, 0))
        self.player = Player(player_data)
        self.passed = False
        self.pro_passed = False


        # 맵 초기화
        camera.orthographic = True
        camera.position = (0, 0)
        camera.fov = 12
        Sky(color=color.hex('4A4C50'))

        wall = Sprite(parent=self, model='quad', texture='test_hall', texture_scale=(1, 1))
        wall.scale *= 2

    def update(self):
        camera.position = (self.player.x, self.player.y)