from ursina import *


app =Ursina()


mm = Button(text= 'ss' ,color = color.red, scale= .2)

Entity(parent=camera.ui, scale=(camera.aspect_ratio, 1), model = 'quad', color=color.green)
Entity(parent=camera.ui, scale=.4, color=color.blue, text="Game Over")

mm.on_click()

app.run()