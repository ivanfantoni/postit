class Postit:

    def __init__(self, id=None, text=None, priority=None):
        
        self.id = id if id is not None else None
        self.text = text
        self.priority = priority if priority is not None else None

    def __repr__(self):
        return f'({self.id},{self.text},{self.priority})'