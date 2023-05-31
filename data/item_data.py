

class ItemData:
    def __init__(self, name, desc, chapter_no, texture):
        self.name = name
        self.desc = desc
        self.chapter_no = chapter_no
        self.texture = texture


class GameItemData:
    def __init__(self):
        self.item = {
            "떨어진 영수증": ItemData("떨어진 영수증", "샌드위치를 구매한 영수증이다.", 1, 'paper'),
            "내려치기 딱 좋은 망치": ItemData("내려치기 딱 좋은 망치", "낡고 오래 방치된 듯한 외관이다.", 1, 'glass'),
            "동아리실 마스터 키": ItemData("동아리실 마스터 키", "학생회장의 마스터 키.", 1, 'paper'),
            "테스트 아이템1": ItemData("테스트 아이템1", "테스트 아이템 이다", 1, 'glass'),
            "테스트 아이템2": ItemData("테스트 아이템2", "테스트 하려고 만든 아이템이다2", 1, 'glass'),
        }
