from ursina import Entity

from object.map.map_chapter import MapChapter
from ui.scene.boardmenu import BoardMenu
from ui.scene.escapemenu import EscapeMenu
from ui.scene.mainmenu import MainMenu
from ui.component.info import Info


class Game(Entity):

    def __init__(self, player=None, menu=MainMenu):
        super().__init__()
        self.player = player
        self.menu = menu(game=self)
        print(self.menu)

        self.ui = None
        self.chapter = None

    def start_chapter(self, num=1):
        print(self.menu)
        self.menu.disable()
        # print(self.menu)
        # self.menu.disable()
        self.ui = Info(num)
        self.chapter = MapChapter(self.player, num)

    def open_board(self):
        self.ui.disable()
        self.menu = BoardMenu(self.player, self.ui.enable)

    def open_escape(self):
        self.ui.disable()
        self.menu = EscapeMenu(self.ui.enable, self.save_exit)

    def save_exit(self):
        # TODO: 저장 후 종료 기능 구현 필요
        print('save and exit')
        self.ui.enable()

    def input(self, key):
        if key == 'q':
            self.open_board()
        elif key == 'escape':
            self.open_escape()
