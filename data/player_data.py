

class PlayerData:
    def __init__(self, name, chapter=1):
        self.name = name

        self.inventory = []
        self.record_titles = set()
        self.chapter = chapter
        self.sample_data = 0
