from ursina import *

from data.player_data import PlayerData
from ui.scene.mainmenu import MainMenu
from game import Game

app = Ursina()
# 상단 바 설정
window.borderless = False

# soundtrack = Audio("_resources/sound/background_music.wav", loop=True) # 배경음악 삽입.
# soundtrack.play() 들으면서 하면 음침해서 꺼놨음. 정상작동함.

# RenScene test 코드
# menu = RenScene(variables_object=variables)
# 타이틀 화면
menu = MainMenu

# video = 'zelda_trailer.mp4'
# video_player = Entity(model='quad', parent=camera.ui, scale=(1.5, 1), texture=video)

# 게임 초기화
game = Game('김이조', menu)

# 게임 시작
app.run()
