from ursina import *

from char.npc import Npc
from char.player import Player
from scene.boardscene import BoardScene

app = Ursina()
window.borderless = False  # window 상단 바 제거 여부

player = Player()

editor_camera = EditorCamera(enabled=False, ignore_paused=True)

board = BoardScene(parent=camera.ui)
board.disable()


def init_map():
    # 기본 땅, 하늘
    ground = Entity(model='plane', collider='box', scale=64, texture='brick', texture_scale=(4, 4))
    ground.rotation_x = -90
    sun = DirectionalLight(color=color.rgba(255, 255, 220, 255), shadows=True)
    sun.look_at(Vec3(0.5, 1, 1))
    sun_sub = DirectionalLight(color=color.rgba(110, 110, 110, 255), shadows=False)
    sun_sub.look_at(Vec3(-0.5, 1, 1))
    Sky()

    # 이벤트 npc, 건물
    npc1 = Npc(name='학생회장', script='chapter1/chapter1.txt', target=player, position=(-3, -1))
    npc1.play_animation('idle_right')
    b1 = Entity(name='화장실', model='cube', scale=2, position=(-3, 1, -1), collider='box', color=color.orange)

    npc2 = Npc(name='졸업생', script='chapter2/chapter2.txt', target=player, position=(0, 1))
    npc2.play_animation('idle_right')
    b2 = Entity(name='복도', model='cube', scale=(2, 4, 1), position=(0, 4, -0.5), collider='box', color=color.azure)

    npc3 = Npc(name='동아리 선배', script='chapter3/chapter3.txt', target=player, position=(2, 1))
    npc3.play_animation('idle_left')
    b3 = Entity(name='동아리실', model='cube', scale=(2, 4, 1), position=(2, 4, -0.5), collider='box', color=color.black)

    npc4 = Npc(name='남교수', script='chapter4/chapter4.txt', target=player, position=(6, 0))
    npc4.play_animation('idle_left')
    b4 = Entity(name='주차장', model='cube', scale=4, position=(6, 4, -2), collider='box', color=color.white)

    npc5 = Npc(name='전 애인', script='chapter5/chapter5.txt', target=player, position=(0, -2))
    npc5.play_animation('idle_right')
    b5 = Entity(name='자취방', model='cube', scale=(4, 2, 1), position=(0, -4, -0.5),
                collider='box', color=color.dark_gray)


def update():
    camera.position = (player.x, player.y - 18, -6)
    camera.rotation_x = -75


def input(key):
    if key == 'q':
        board.enable()


init_map()
app.run()
