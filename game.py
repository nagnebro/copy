from ursina import Entity, Audio, camera, color
import pickle

from data.item_data import GameItemData
from object.map_chapter import MapChapter
from ui.component.note import Note
from ui.scene.boardmenu import BoardMenu
from ui.scene.escapemenu import EscapeMenu
from ui.scene.mainmenu import MainMenu
from ui.component.info import Info


class Game(Entity):
    def __init__(self, player_name, menu=MainMenu):
        super().__init__()
        self.player_data = None
        self.item_data = GameItemData()

        self.load_player_data(player_name)
        self.menu = menu(game=self)

        self.ui = None
        self.chapter = None

        self.video = Entity(parent=camera.ui, model='quad', texture='zelda_trailer.mp4',
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=4, world_y=0)

        # 싱크가 맞는진 모르겠으나. .. audio 재생이 됩니다.
        self.sound = Audio("_resources/video/zelda_trailer.mp4", loop=True)

        # soundtrack = Audio("_resources/sound/prologue.wav", loop=True) # 배경음악 삽입.
        # soundtrack.play() #들으면서 하면 음침해서 꺼놨음. 정상작동함.

    def load_player_data(self, player_name):
        try:
            with open(player_name + '.pickle', 'rb') as file:
                self.player_data = pickle.load(file)
        except FileNotFoundError:
            return None

    def save_player_data(self, player_data):
        with open(player_data.name + '.pickle', 'wb') as file:
            pickle.dump(player_data, file)
        self.load_player_data(player_data.name)

    def start_chapter(self):
        print(self.menu)
        self.menu.disable()
        # print(self.menu)
        # self.menu.disable()
        self.ui = Info()
        self.chapter = MapChapter(self)

    def open_board(self):
        self.ui.disable()
        self.menu = BoardMenu(self.player_data, self.ui.enable)

    def open_note(self):
        self.ui.disable()
        self.menu = Note(self.player_data, self.ui.enable)

    def open_escape(self):
        self.ui.disable()
        self.menu = EscapeMenu(self.ui.enable, self.save_exit)

    def save_exit(self):
        self.save_player_data(player_data=self.player_data)
        print('save and exit')
        exit()

    def input(self, key):
        if key == 'q':
            self.open_board()
        elif key == 't':
            self.open_note()
        elif key == 'escape':
            self.open_escape()

        elif key == 'm':  # 배경음악끄기 mute
            if (self.sound.loop):
                print('hi')
                self.sound.loop = False
                self.video.disable()
                self.sound.stop()
                # self.video.disable()
                return
            self.sound.loop = True
            self.sound.play()
        elif key == 'space':
            import random
            a = Audio('aa', pitch=random.uniform(.5, .7), loop=True, autoplay=True)
