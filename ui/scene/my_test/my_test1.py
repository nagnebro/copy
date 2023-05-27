from ursina import *



app = Ursina()
window.borderless = False # 창 사이즈
window.color = color._16 # 창 칼라?
background = Entity(parernt = camera.ui, model ="quad", color = color.white,   scale=(100, 100),z=4,world_y=0) # 배경 지정

cursor = Entity(parent=camera.ui, model="quad", texture="brain.png", color=color.white , scale=.2, y=0) # 텍스쳐 지정
#여기서 텍스쳐란 Entity 클래스를 통해 생성할 수 있는 사물같은 것을 뜻한다.?



window.size = window.fullscreen_size * 0.7

app.run()