from ursina import *

from game.char.npc import Npc
from game.char.player import Player
from game.map.map_inha import MapInha
from ui.scene.boardscene import BoardScene

app = Ursina()
window.borderless = False  # window 상단 바 제거 여부

player = Player()

editor_camera = EditorCamera(enabled=False, ignore_paused=True)

board = BoardScene(parent=camera.ui)
board.disable()


def init_map():
    # 기본 땅, 하늘
    inha_map = MapInha()

    sun = DirectionalLight(parent=inha_map, color=color.rgba(255, 255, 220, 255), shadows=True)
    sun.look_at(Vec3(0.5, 1, 1))
    sun_sub = DirectionalLight(color=color.rgba(110, 110, 110, 255), shadows=False)
    sun_sub.look_at(Vec3(-0.5, 1, 1))
    Sky()

    inha_map.place_npc(player)

    return inha_map

# def other_map():
#     ground = Entity(model='plane', collider='box', scale=8, color=color.white)
#     ground.rotation_x = -90
#
#     Sky(color=color.hex("2b1e15"))


def update():
    camera.position = (player.x, player.y - 18, -6)
    camera.rotation_x = -75


def input(key):
    if key == 'q':
        board.enable()


init_map()
app.run()
