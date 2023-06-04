from ursina import *

from data.player_data import PlayerData
from ui.scene.mainmenu import MainMenu
from game import Game

app = Ursina()
# 상단 바 설정
window.borderless = False
# 해상도 고정
window.size = (1280, 720)

#프롤로그 영상 입니다.

# video = Entity(parent=camera.ui, model='quad', texture='zelda_trailer.mp4',
#                     scale=(camera.aspect_ratio, 1),
#                     color=color.white, z=4, world_y=0)
#
# # 싱크가 맞는진 모르겠으나. .. audio 재생이 됩니다.
# sound = Audio("_resources/video/zelda_trailer.mp4", loop=True)

# RenScene test 코드
# menu = RenScene(variables_object=variables)
# 타이틀 화면
menu = MainMenu

# video = 'zelda_trailer.mp4'
# video_player = Entity(model='quad', parent=camera.ui, scale=(1.5, 1), texture=video)

# 게임 초기화
game = Game('김이조', menu)
# MapSprite(PlayerData(name='김이조', chapter=1), 1)

# 게임 시작
app.run()

