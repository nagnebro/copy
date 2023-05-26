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


class Info(Entity):
    def __init__(self, variables_object=None, **kwargs):
        super().__init__(parent=camera.ui, )

        guide = Text(parent=self, font="NanumSquareRoundB.ttf", text="조합 q        이동 w,a,s,d        상호작용 e",
                         origin=(-.5, .5), scale=(1, 1), x=-.2, y=-.45, z=8)

        title = Entity(parent=self, model='quad', name='paper', color=color.white, origin=(.5, .5),
                         scale=(.8, .2), x=-.4, y=.45, z=8)

        clock = Entity(parent=self, model='quad', texture='clock', name='paper', color=color.white, origin=(-.5, .5),
                       scale=(.2, .14), x=.6, y=.45, z=8)

        tab = Entity(parent=self, model='quad', name='paper', color=color.white, origin=(.5, .5),
                     scale=(.15, .15), x=.9, y=.25, z=8)

        minimap = Entity(parent=self, model='quad', name='paper', color=color.white, origin=(-.5, -.5),
                         scale=(.3, .2), x=.5, y=-.45, z=8)

        item = Entity(parent=self, model='quad', texture='paper', name='paper', color=color.white, origin=(-.5, -.5),
                      scale=(.12, .12), x=-.8, y=-.45, z=8)
