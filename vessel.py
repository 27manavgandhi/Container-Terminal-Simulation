class Vessel:
    def __init__(self, id):
        self.id = id
        self.containers = 150

    def __str__(self):
        return f"Vessel-{self.id}"