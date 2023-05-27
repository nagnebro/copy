from ursina import *

from game.char.player import Player
from game.map.map_inha import MapInha
from ui.component.info import Info
from ui.scene.boardscene import BoardScene
from ui.scene.renscene import RenScene

app = Ursina()
window.borderless = False  # window 상단 바 제거 여부

player = Player()

editor_camera = EditorCamera(enabled=False, ignore_paused=True)

info = Info(parent=camera.ui)
board = BoardScene(parent=camera.ui)
board.disable()


def init_map():
    # 기본 땅, 하늘
    inha_map = MapInha()

    # sun = DirectionalLight(parent=inha_map, color=color.rgba(255, 255, 220, 255), shadows=True)
    # sun.look_at(Vec3(0.5, 1, 1))
    # sun_sub = DirectionalLight(color=color.rgba(110, 110, 110, 255), shadows=False)
    # sun_sub.look_at(Vec3(-0.5, 1, 1))
    # Sky()
    #
    # inha_map.place_npc(player)

    return inha_map


def other_map():
    other = Entity()
    # cube = Entity(parent=other, model='plane', texture='inha_ware6_hall', scale=(36, 0, 8), position=(0, 4, -2))
    # cube.rotation_x = -180
    ground = Entity(parent=other, model='plane', texture='brick', collider='box', scale=(36, 0, 8), texture_scale=(8,8), color=color.white)
    ground.rotation_x = -90
    Sky(color=color.black)
    return other


def update():
    camera.rotation_x = -45
    camera.position = (camera.position.x, player.y - 18, -18)
    if player.x < 12:
        camera.position = (player.x, player.y - 18, -18)


def input(key):
    if key == 'q':
        board.enable()
    # if key == 'g':
    #     if other.enabled:
    #         other.disable()
    #         main_map.enable()
    #     else:
    #         other.enable()
    #         main_map.disable()


# FindScene(parent=camera.ui)
# main_map = init_map()


# RenScene test해보려고 추가한 코드.
# variables = Empty(
#     evil=0,
#     chaos=0,
#     bar_mission_solved=False,
# )
#
#
# RenScene(variables_object=variables)


other = other_map()



# other.disable()

app.run()
