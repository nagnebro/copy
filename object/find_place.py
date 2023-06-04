from ursina import *

from ui.scene.find_proviso import Find_Proviso


class FindPlace(Entity):
    def __init__(self, player, game, number, **kwargs):
        super().__init__(**kwargs)
        self.player = player
        self.pro_passed = False

        self.proviso = Find_Proviso(self.player.data, game.item_data, number)
        self.proviso.disable()

    def input(self, key):
        # 단서수집 포탈 근처에 갔을 떄 키를 눌러야 동작하게끔(Npc와 말거는 거처럼)
        if self.intersects(self.player) and key == 'e':
            if not self.proviso.enabled:
                self.proviso.enable()
