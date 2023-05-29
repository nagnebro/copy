from ursina import *

from data.player_data import PlayerData
from ui.scene.mainmenu import MainMenu
from game import Game

app = Ursina()
# 상단 바 설정
window.borderless = False

# 사용자
player = PlayerData(name='이름', chapter=2)

# RenScene test 코드
# menu = RenScene(variables_object=variables)
# 타이틀 화면
menu = MainMenu

# 게임 초기화
game = Game(player, menu)

# 게임 시작
app.run()
