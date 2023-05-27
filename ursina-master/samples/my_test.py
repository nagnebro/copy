from ursina import *

app = Ursina()

class Ball(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            color=color.orange,
            scale=1,
            collider='sphere'
        )

    def update(self):
        self.x += held_keys['d'] * time.dt
        self.x -= held_keys['a'] * time.dt
        self.y += held_keys['w'] * time.dt
        self.y -= held_keys['s'] * time.dt

ball = Ball()

app.run()