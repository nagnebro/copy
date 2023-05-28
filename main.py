from ursina import *

from data.player_data import PlayerData
from game.char.player import Player
from game.map.map_chapter import MapChapter
from ui.component.info import Info
from ui.scene.boardscene import BoardScene
from ui.scene.mainmenu import MainMenu

app = Ursina()
window.borderless = False  # window 상단 바 제거 여부

player = Player(data=(PlayerData(name='이름')))

editor_camera = EditorCamera(enabled=False, ignore_paused=True)

info = Info(parent=camera.ui)
board = BoardScene(parent=camera.ui, player_data=player.data)
board.disable()


def init_map():
    # 기본 땅, 하늘
    start = MapChapter(player, 1)
    # sun = DirectionalLight(parent=inha_map, color=color.rgba(255, 255, 220, 255), shadows=True)
    # sun.look_at(Vec3(0.5, 1, 1))
    # sun_sub = DirectionalLight(color=color.rgba(110, 110, 110, 255), shadows=False)
    # sun_sub.look_at(Vec3(-0.5, 1, 1))
    Sky(color=color.black)
    return start


def update():
    camera.rotation_x = -45
    camera.position = (camera.position.x, player.y - 18, -18)
    if player.x < 12:
        camera.position = (player.x, player.y - 18, -18)


def input(key):
    if key == 'q':
        board.enable()


MainMenu()
init_map()
# RenScene test해보려고 추가한 코드.
# variables = Empty(
#     evil=0,
#     chaos=0,
#     bar_mission_solved=False,
# )
#
#
# RenScene(variables_object=variables)
app.run()
