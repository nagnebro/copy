"""
*아이템과 아이템을 잇는 붉은 선 출력?
    인벤토리 -> 아이템:
        핀으로 꽂는다
    핀을 클릭, 다른 핀을 다시 클릭하면, 연결됨
    핀을 다시 클릭하면 X표시
    삭제하는 곳도 만듦

    그대로 저장
"""
from ursina import Entity, camera, color, Draggable, Text, Mesh, destroy

from ui.component.combine import Combine
from ui.component.inventory import Inventory


class BoardMenu(Entity):

    def __init__(self, player_data=None, resume=None):
        super().__init__(parent=camera.ui)

        self.player_data = player_data
        self.inventory = None
        self.combine = None
        self.line=None

        self.resume = resume

        background = Entity(parent=self, model='quad', texture='board',
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=4, world_y=0)

        item1 = Draggable(parent=self, model='quad', texture='paper', name='paper', color=color.white,
                          scale=(.1, .1), z=-1)
        item2 = Draggable(parent=self, model='quad', texture='glass', name='glass', color=color.white,
                          scale=(.1, .1), position=(-.2, .1, 0), z=-1)

        def drop():
            destroy(self.line)
            if self.combine and (self.combine.x - item1.x) / self.combine.scale_x < 1:
                self.combine.append(item1.name, 0)
                item1.disable()
            if self.combine and (self.combine.x - item2.x) / self.combine.scale_x < 1:
                self.combine.append(item2.name, 1)
                item2.disable()
            if item1.enabled and item2.enabled:
                points = [item1.position, item2.position]
                self.line = Entity(parent=self, model=Mesh(points, mode='line', thickness=2), z=1, color=color.red)

        item1.drop = drop
        item2.drop = drop

        points = [item1.position, item2.position]
        self.line = Entity(parent=self, model=Mesh(points, mode='line', thickness=2), z=1, color=color.red)

        guide = Text(parent=self, font="NanumSquareRoundB.ttf", text="'Z' 가방\t'X' 닫기\t'C' 조합",
                         position = (-.2, -.45, -1))

    def disable(self):
        self.resume()
        super().disable()

    def input(self, key):
        if key == 'z':
            if self.inventory:
                print(self.player_data.name)
                self.inventory.disable()
                self.inventory = None
            else:
                self.inventory = Inventory(parent=self)
        if key == 'x':
            self.disable()
            if self.combine:
                self.combine.disable()
        if key == 'c':
            if self.combine:
                self.combine.disable()
                self.combine = None
            else:
                self.combine = Combine(parent=self)
