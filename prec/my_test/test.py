from ursina import *


# app = Ursina()
#
# window.borderless = False
#
# m1 = Draggable(parent = camera.ui , scale =.5 , color = color.blue, model = 'quad')
# m2 = Entity(parent = camera.ui , scale =.3 , color = color.red ,model = 'quad' , position = Vec3(0.1,0.1,-0.1))
#
#
# app.run()

from ursina import *

app = Ursina()

# 부모 객체 생성
parent_obj = Entity(model='cube', color=color.red, scale=(1, 1, 1))

# 자식 객체 생성
child_obj = Entity(model='cube', color=color.blue, scale=(0.5, 0.5, 0.5), z= -3)

# 자식 객체를 부모 객체의 자식으로 설정
child_obj.parent = parent_obj

# 부모 객체의 위치 변경
child_obj.position = (0.1, 0, -1)

app.run()