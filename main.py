from ursina import *

from char.npc import Npc
from char.player import Player
from scene.findscene import FindScene
from ui.inventory import Inventory
from scene.chapter1_test import Chapter1_test
from scene.chapter2_test import Chapter2_test
from scene.chapter3_test import Chapter3_test
from scene.chapter4_test import Chapter4_test
from scene.chapter5_test import Chapter5_test

app = Ursina()
window.borderless = False  # window 상단 바 제거 여부

player = Player()

editor_camera = EditorCamera(enabled=False, ignore_paused=True)

inventory = Inventory(parent=camera.ui)


def initMap():
    ground = Entity(model='plane', collider='box', scale=64, texture='brick', texture_scale=(4, 4))
    ground.rotation_x = -90

    b1 = Entity(model='cube', scale=2, position=(-3, 1, -1), collider='box', color=color.orange)
    b2 = Entity(model='cube', scale=(2, 4, 1), position=(0, 4, -0.5), collider='box')
    b3 = Entity(model='cube', scale=(2, 4, 1), position=(2, 4, -0.5), collider='box')
    b4 = Entity(model='cube', scale=4, position=(6, 4, -2), collider='box')
    b5 = Entity(model='cube', scale=(4, 2, 1), position=(0, -4, -0.5), collider='box')

    npc = Npc(target=player)

    sun = DirectionalLight(color=color.rgba(255, 255, 220, 255), shadows=True)
    sun.look_at(Vec3(0.5, 1, 1))

    sun_sub = DirectionalLight(color=color.rgba(110, 110, 110, 255), shadows=False)
    sun_sub.look_at(Vec3(-0.5, 1, 1))

    Sky()


def input(key):
    if key == 'q':
        FindScene(inventory, Empty(
            evil=0,
            chaos=0,
            bar_mission_solved=False,
        ))
    elif key == '1':
        Chapter1_test(Empty(
            evil=0,
            chaos=0,
            bar_mission_solved=False,
        ))

    elif key == '2':
        Chapter2_test(Empty(
            evil=0,
            chaos=0,
            bar_mission_solved=False,
        ))
    elif key == '3':
        Chapter3_test(Empty(
            evil=0,
            chaos=0,
            bar_mission_solved=False,
        ))

    elif key == '4':
        Chapter4_test(Empty(
            evil=0,
            chaos=0,
            bar_mission_solved=False,
        ))

    elif key == '5':
        Chapter5_test(Empty(
            evil=0,
            chaos=0,
            bar_mission_solved=False,
        ))


def update():
    camera.position = (player.x, player.y - 18, -6)
    camera.rotation_x = -75


initMap()
app.run()
