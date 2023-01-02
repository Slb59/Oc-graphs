import csv
from training.project import Project

class Training:
    def __init__(self, title):
        self.title = title
        self.path = ''
        self.file = ''

        self.projects = []

    def __str__(self):
        return self.title

    def load_projects(self):
        with open(self.path + self.file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for line in reader:
                task = Project(line['Sujet'], line['Titre'], line['Description'], line['Description'],
                               line['Temps estimé'], line['% temps / total'],
                               line['Nombre de jours affectés'],
                               line['Nombre heures sur le projet'],
                               line["Nombre d'heures affectées"],
                               line['Date de démarrage estimée'], line['Date de fin estimée'],
                               line['Date de damarrage effectif'], line['Date de fin effectif'],
                               line['Temps effectif'], line['Temps consacré au projet'],
                               line['Date de soutenance'])


