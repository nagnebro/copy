from ursina import *

app = Ursina()
window.borderless = False  # 창 사이즈
# window.color = color._16  # 창 칼라?

# Entity로 생성한 사물들을 크기를 조절해서 화면위에 엊는 것 뿐

# item0 = Entity(parent=self, model='quad', color=color.rgba(255, 255, 255, 100), origin=(0, .5),
#              scale=(.2, .125), x=-.8, y=-.2, z=-1)
# 지수가 만든 아이템 코드
# 창을 띄운다.



# background = Entity(parent=camera.ui, model="quad", texture="restroom.png",
#                     scale=(camera.aspect_ratio, 1),
#                     color=color.white, z=4, world_y=0)  # 배경 지정

# background1 =Entity(parent = camera.ui, model = "quad", texture = 'restroom',
#                      scale = (camera.aspect_ratio,1),color = color.white, z=4, world_y=0)
icon = Button(parent=camera.ui, model="quad", texture="paper.png", color=color.white, scale=.1,  x=.0, y=.0, z=.0,
               tooltip = 'this is paper' )  # 텍스쳐 지정
# 여기서 텍스쳐란 Entity 클래스를 통해 생성할 수 있는 사물같은 것을 뜻한다.?

guide = Text(parent=camera.ui, font="NanumSquareRoundB.ttf", text="조합 q        이동 w,a,s,d        상호작용 e",
             origin=(-.5, .5), scale=(1, 1), x=-.2, y=-.45, z=8)

title = Entity(parent=camera.ui, model='quad', name='paper', color=color.white, origin=(.5, .5),
               scale=(.8, .2), x=-.4, y=.45, z=8)

b = Button(text='assa', radius=.1, parent=camera.ui, color=color.red, scale=.2, x=.5, y=.5, z=.3,
           tooltip = Tooltip('sss'))
b.on_click = application.quit  # 버튼을 클릭시 어플리케이션을 종료, 이 버튼을 창을 닫는 버튼으로 만들어야 함.
# 매개변수 없이 on_click 실행 자체만으로 self생성자에 의해 action을 실행하게되며 우측이 이벤트 발생시의 action값.


# 드래그 가능한 아이콘의 툴팁을 설정

# icon.tooltip = Tooltip('asdsad')
# icon.tooltip.background.color = color.color(0, 0, 0, .8)

# Entity(
#     parent=camera.ui,
#     model=Quad(radius=.015),
#     texture='white_cube',
#     scale=(.5, .8),
#     origin=(.5, .5),
#     position=(.3, .2, -1),
#     color=color.color(0, 0, .1, .9),
# )

window.size = window.fullscreen_size * 0.8

app.run()
