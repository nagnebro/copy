from ursina import *


app =Ursina()


# mm = Button(text= 'ss' ,color = color.red, scale= .2)

# Entity(parent=camera.ui, scale=(camera.aspect_ratio, 1), model = 'quad', color=color.green)
Entity(parent=camera.ui, scale=.4, color=color.blue, text="Game Over")

e = Entity(name='동아리 선배', scale=5, model='quad', texture="paper", image='club_leader_0', z=-10)



app.run()