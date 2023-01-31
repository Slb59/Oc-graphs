import csv
from training.project import Project
from logs import LOGGER

class Training:

    """ manage a training """
    def __init__(self, title):
        self.title = title
        self.path = ''
        self.file = ''

        self.projects = []

    def __str__(self):
        return self.title

    def __repr__(self):
        infos = self.title + '\n'
        infos += 'Liste des projets\n'
        for p in self.projects:
            infos += p.subject + ': ' + p.title + '\n'
        return infos

    def load_projects(self):

        LOGGER.debug('Chargement du fichier principal de formation')

        with open(self.path + self.file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for line in reader:
                p = Project(line['Sujet'])

                p.title = line['Titre']
                p.description = line['Description']

                p.estimate_time = line['Temps estimé']
                p.pct_total_time = line['% temps / total']
                p.nb_days_affected = line['Nombre de jours affectés']
                p.nb_hours_on_project = line['Nombre heures sur le projet']
                p.nb_hours_affected = line["Nombre d'heures affectées"]
                p.estimate_start_date = line['Date de démarrage estimée']
                p.estimate_end_date = line['Date de fin estimée']
                p.real_start_date = line['Date de damarrage effectif']
                p.real_end_date = line['Date de fin effectif']
                p.real_time = line['Temps effectif']
                p.real_time_on_project = line['Temps consacré au projet']
                p.evaluate_date = line['Date de soutenance']

                self.projects.append(p)



