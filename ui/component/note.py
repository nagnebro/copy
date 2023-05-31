from ursina import *

from data.record_data import GameRecordData


class Note(Entity):
    def __init__(self, player_data, resume=None):
        super().__init__(
            parent=camera.ui,
            model=Quad(),
            scale=(1.5, 1),
            texture='note',
            color=color.white,
        )
        self.index = 0

        self.text_title = Text(parent=self, font="NanumSquareRoundB.ttf", text='', position=(0, .2, -1), scale=(2, 1.25))
        self.text_desc = Text(parent=self, font="NanumSquareRoundB.ttf", text='', position=(0, .1, -1), scale=(2, 1.25))

        self.resume = resume
        print(player_data.record_titles)

        self.recordData = GameRecordData()
        self.playerRecordData = []
        for record_title in player_data.record_titles:
            self.playerRecordData.append(self.recordData.record[record_title])
        if len(self.playerRecordData) != 0:
            self.print_record(0)

    def print_record(self, index):
        self.text_title.text = self.playerRecordData[index].name
        self.text_desc.text = self.playerRecordData[index].desc

    def next_page(self):
        # 인덱스가 전체 기록 수 보다 클 경우, 다음 페이지 없음
        if self.index >= len(self.playerRecordData):
            return
        else:
            self.print_record(self.index)

    def prev_page(self):
        # 인덱스가 0 보다 작을 경우, 이전 페이지 없음
        if self.index >= 0:
            return
        else:
            self.print_record(self.index)

    def disable(self):
        self.resume()
        super().disable()

    def input(self, key):
        if key == 'x':
            self.disable()
        if key == 'z':
            self.next_page()
        if key == 'c':
            self.prev_page()