"""
    아이템과 아이템의 좌표가 겹쳐진 경우:
        조합이 가능한 경우:
            조합식에 맞게 새 아이템 생성
            조합에 사용된 아이템 삭제
            새 아이템 출력
            (결과 아이템 정보 출력)
        조합이 불가능한 경우:
            (조합불가 메세지 출력)
            이전 위치로 이동
"""

from ursina import *


class Combine(Entity):

    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            scale=(.5, .8),
            origin=(.5, .5),
            position=(.8, .4, -1),
            color=color.color(0, 0, .1, .9),
        )

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.items = []

        item0 = Entity(parent=self, model='quad', color=color.rgba(255, 255, 255, 100), origin=(0, .5),
                       scale=(.2, .125), x=-.8, y=-.2, z=-1)
        item1 = Entity(parent=self, model='quad', color=color.rgba(255, 255, 255, 100), origin=(0, .5),
                       scale=(.2, .125), x=-.5, y=-.2, z=-1)
        item2 = Entity(parent=self, model='quad', color=color.rgba(255, 255, 255, 100), origin=(0, .5),
                       scale=(.2, .125), x=-.2, y=-.2, z=-1)

        result = Entity(parent=self, model='quad', color=color.rgba(255, 255, 255, 100), origin=(0, .5),
                        scale=(.2, .125), x=-.5, y=-.6, z=-1)

        guide = Text(parent=self, font="NanumSquareRoundB.ttf", text="'V' 길게 눌러서 조합",
                     origin=(1.2, .5), position=(0, -.9, -1), scale=(2, 1.25))

    def append(self, item_name):
        print('add item:', item_name)

        item = Draggable(
            parent=self,
            model='quad',
            texture=item_name,
            name=item_name,
            color=color.white,
            scale_x=.2,
            scale_y=.125,
            origin=(0, .5),
            x=-.8 + (len(self.items) * 0.3),
            y=-.2,
            z=-.5,
        )
        self.items.append(item)
        item.drop = Func(self.drop, item)

    def drop(self, item):
        if item.x < 0 or item.x >= 1 or item.y > 0 or item.y <= -1:
            self.parent.append(item.name)
            if item in self.items:
                self.items.remove(item)
            item.disable()
            return

    def input(self, key):
        if key == 'v':
            for item in self.items:
                item.disable()
            self.items.clear()
            result_item = Draggable(
                parent=self,
                model='quad',
                texture='blueprint',
                name='blueprint',
                color=color.white,
                scale_x=.2,
                scale_y=.125,
                origin=(0, .5),
                x=-.5,
                y=-.6,
                z=-.5,
            )
            result_item.drop = Func(self.drop, result_item)
