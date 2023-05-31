

class NpcData:
    def __init__(self, name, chapter_no, texture, reason):
        self.name = name
        self.chapter_no = chapter_no
        self.texture = texture
        self.reason = reason


class GameNpcData:
    def __init__(self):
        self.item = {
            "stu_pr": NpcData("떨어진 영수증", "샌드위치를 구매한 영수증이다.", 1, 'paper'),
            "내려치기 딱 좋은 망치": NpcData("내려치기 딱 좋은 망치", "낡고 오래 방치된 듯한 외관이다.", 1, 'glass'),
            "동아리실 마스터 키": NpcData("동아리실 마스터 키", "학생회장의 마스터 키.", 1, 'paper'),
            "테스트 아이템1": NpcData("테스트 아이템1", "테스트 아이템 이다", 1, 'glass'),
            "테스트 아이템2": NpcData("테스트 아이템2", "테스트 하려고 만든 아이템이다2", 1, 'glass'),
        }
