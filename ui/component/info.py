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
    def __init__(self):
        super().__init__(parent=camera.ui)

        gradient_v = Entity(model='quad', texture='vertical_gradient', parent=self,
                          rotation_z=180,
                          scale=(2, 1),
                          color=color.rgba(0, 0, 0, 180), z=8)

        guide = Text(parent=self, font="NanumSquareRoundB.ttf", text="'Q' 조합      'W,A,S,D' 이동      'E' 상호작용:     M : 배경음악 On/Off",
                     origin=(-.5, .5), scale=(1, 1), x=-.2, y=-.45, z=8)

        guide = Text(parent=self, font="NanumSquareRoundB.ttf", text="'space' 시험버전: 갈려나간 개발자의 끔찍한 비명",
                     color=color.black66, origin=(-.5, .5), scale=(.8, .8), x=.4, y=-.48, z=8)

        title = Entity(parent=self, model='quad', texture='chapter_info', name='paper', color=color.white,
                       scale=(.4, .2), x=-.65, y=.36, z=8)

        clock = Entity(parent=self, model='quad', texture='clock', name='paper', color=color.white, origin=(-.5, .5),
                       scale=(.2, .14), x=.6, y=.45, z=8)

        tab = Entity(parent=self, model='quad', texture='tab_menu', name='paper', color=color.white,
                     origin=(0, .5), scale=(.5, .6), x=1.05, y=.25, z=8)

        item = Entity(parent=self, model='quad', texture='paper', name='paper', color=color.white, origin=(-.5, -.5),
                      scale=(.12, .12), x=-.8, y=-.45, z=8)