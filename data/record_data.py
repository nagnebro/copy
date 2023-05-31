class RecordData:
    def __init__(self, name, npc_name, desc):
        self.name = name
        self.npc_name = npc_name
        self.desc = desc


class GameRecordData:
    def __init__(self):
        self.record = {"졸업생의 방문 목적": RecordData(name="졸업생의 방문 목적", npc_name="졸업생",
                                                                     desc="졸업생은 보조 배터리를 찾기 위해 학교에 방문했다고 주장한다.")}
