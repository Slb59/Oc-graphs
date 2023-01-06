import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Project:
    def __init__(self, name):

        self.subject = name
        self.title = name
        self.description = ''
        self.estimate_time = 0
        self.pct_total_time = 0
        self.nb_days_affected = 0
        self.nb_hours_on_project = 0
        self.nb_hours_affected = 0
        self.estimate_start_date = ''
        self.estimate_end_date = ''
        self.real_start_date = ''
        self.real_end_date = ''
        self.real_time = 0
        self.real_time_on_project = 0
        self.evaluate_date = ''

        self.path = ''
        self.project_file = ''

        self.tasks = []

    def __str__(self):
        return self.title + ': ' + self.description

    def __repr__(self):
        return ''

    def task_pivot_to_table(self):
        df = pd.DataFrame([task.__dict__ for task in self.tasks])
        table = df[['category', 'real_time']].pivot_table(index='category', values='real_time', aggfunc=np.sum)
        table['(HH:MM)'] = table['real_time'].apply(lambda x: f'{int(x // 3600):02d}:{int((x % 3600) // 60):02d}')
        print(table)

    def task_pivot_to_pie(self):
        df = pd.DataFrame([task.__dict__ for task in self.tasks])
        table = df[['category', 'real_time']].pivot_table(index='category', values='real_time', aggfunc=np.sum)

        realise = table['real_time'].tolist()
        categories = table.index.tolist()

        plt.pie(realise, labels=categories, autopct='%1.0f%%')
        plt.title("Réalisé par catégorie")

        plt.savefig(self.path + 'realisé.png')

    def print_tasks(self):
        for t in self.tasks:
            print(t)


