from ursina import *


class Player(SpriteSheetAnimation):
    def __init__(self, data, **kwargs): # 여기서 data는 player_data클래스의 player_data 객체를 뜻한다.
        super().__init__('Tressa', tileset_size=(6, 5), fps=8, collider='box', animations={
            'idle_left': ((1, 4), (1, 4)),
            'idle_right': ((0, 4), (0, 4)),

            'walk_down': ((0, 3), (4, 3)),
            'walk_up': ((0, 2), (4, 2)),
            'walk_left': ((0, 1), (4, 1)),
            'walk_right': ((0, 0), (4, 0)),
        })
        self.data = data
        self.position = (1, 0)
        self.origin = (0, 0, 1)
        self.play_animation('idle_right')
        self.scale_y = 1.5
        self.scale_x = 0.9

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'w up':
            self.play_animation('idle_right')
        elif key == 's up':
            self.play_animation('idle_right')
        elif key == 'a up':
            self.play_animation('idle_left')
        elif key == 'd up':
            self.play_animation('idle_right')
        elif key == 'd':
            self.play_animation('walk_right')
        elif key == 'a':
            self.play_animation('walk_left')
        elif key == 'w':
            self.play_animation('walk_up')
        elif key == 's':
            self.play_animation('walk_down')

    def update(self):
        self.y += held_keys['w'] * time.dt * 8
        self.y -= held_keys['s'] * time.dt * 8
        self.x += held_keys['d'] * time.dt * 8
        self.x -= held_keys['a'] * time.dt * 8
