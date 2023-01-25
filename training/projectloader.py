import csv
from datetime import datetime
from training import *


class ProjectLoader:
    """ load a csv projet in a Project object """

    def __init__(self, project):
        self.project = project

    def load_csv(self):

        with open(self.project.path + self.project.project_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            # save the prec subject to manage the case of a merged field
            prec_subject = ''

            for line in reader:
                task = Task(line['Date'], line['Sujet'], line['Catégorie'], line['Description'],
                              line['Durée estimée'], line['Réalisé'])

                if task.subject == '':
                    task.subject = prec_subject

                if task.real_time == '':
                    task.real_time = datetime.datetime.strptime("00:00", "%H:%M")
                else:
                    task.real_time = datetime.datetime.strptime(task.real_time, "%H:%M:%S")

                task.real_time = task.real_time.hour * 3600 + task.real_time.minute * 60 + task.real_time.second

                # if the task is on the project (same subject)
                if task.subject.lower() == self.project.subject.lower():
                    self.project.tasks.append(task)
                prec_subject = task.subject

        self.project.df = pd.DataFrame([task.__dict__ for task in self.project.tasks])