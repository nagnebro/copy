from ursina import Entity, camera, color, Draggable, Text, Mesh, destroy, Button, Func


class MainMenu(Entity):

    def __init__(self, game):
        super().__init__(parent=camera.ui)

        background = Entity(parent=self, model='quad', texture='inha_ware6_entry',
                            scale=(camera.aspect_ratio, 1), z=4)
        title = Entity(parent=self, model='quad', texture='title', position=(-.35, -.1),
                       scale=(camera.aspect_ratio / 2.5, camera.aspect_ratio / 2.5), z=3)

        gradient = Entity(model='quad', texture='horizontal_gradient', parent=self,
                          rotation_z=180,
                          scale=(camera.aspect_ratio / 2, 1),
                          origin=(.5, 0),
                          color=color.rgba(0, 0, 0, 180), z=2)

        title_name = Entity(parent=self, model='quad', texture='title_name', position=(.45, .1),
                            scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 6), z=1)

        version = Text(parent=self, text="0.5.28.1. Early Access", color=color.light_gray,
                       scale=.8, origin=(-1, 0), x=-.98, y=-.48, z=1)

        btn_new_game = Button(parent=self, font="NanumSquareRoundB.ttf", text="새 게임",
                              scale=(.2, .05), x=.6, y=-.1, z=1)

        btn_continue = Button(parent=self, font="NanumSquareRoundB.ttf", text="계속하기",
                              scale=(.2, .05), x=.6, y=-.2, z=1)

        btn_exit = Button(parent=self, font="NanumSquareRoundB.ttf", text="종료",
                          scale=(.2, .05), x=.6, y=-.3, z=1)

        self.buttons = (btn_new_game, btn_continue, btn_exit)
        for b in self.buttons:
            b.text_entity.font = "NanumSquareRoundB.ttf"
            b.text_entity.line_height = 1.15

        btn_new_game.on_click = Func(game.start_chapter, 1)
        btn_continue.on_click = Func(game.start_chapter, game.player.chapter)
        btn_exit.on_click = exit

    def start_new_game(self):
        self.disable()