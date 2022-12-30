class Training:
    def __init__(self, title):
        self.title = title
        self.projects = []

    def __str__(self):
        return self.title

    def load_projects(self, file):
        pass