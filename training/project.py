import datetime

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
        self.df = pd.DataFrame([task.__dict__ for task in self.tasks])

    def __str__(self):
        return self.title + ': ' + self.description

    def __repr__(self):
        line = self.title + ': ' + self.description + '\n'
        line += f'Estimations : {str(self.estimate_time)} soit {str(self.pct_total_time)}% du total\n'
        line += f'{str(self.nb_days_affected)} jours affectés '
        line += f'soit {str(self.nb_hours_on_project)} heures sur le projet '
        line += f'et {str(self.nb_hours_affected)} heures au total\n'
        line += f'Le projet est prévu de : {self.estimate_start_date} au {self.estimate_end_date}'
        if self.real_start_date:
            line += f"Il s'est effectivement déroulé du {self.real_start_date} au {self.real_end_date}\n"
            line += f"pour une durée de {self.real_time} heure soit {self.real_time_on_project} "
            line += f"{self.real_time_on_project} sur le projet"
        now = datetime.date
        if now < self.evaluate_date:
            line += f"La soutenance aura lieu le {self.evaluate_date}"
        else:
            line += f"La soutenance a eu lieu le {self.evaluate_date}"
        """
    self.tasks = []
"""

    def task_pivot_to_table(self):
        table = self.df.pivot_table(index='category', values='real_time', aggfunc=np.sum)
        table['(HH:MM)'] = table['real_time'].apply(lambda x: f'{int(x):02d}:{int(x % 1 * 60):02d}')
        print('------> Total par catégorie')
        print(table)
        print('------> Total général')
        print(table.sum(axis = 0, skipna = True))

    def task_pivot_to_pie(self):
        df = pd.DataFrame([task.__dict__ for task in self.tasks])
        table = df[['category', 'real_time']].pivot_table(index='category', values='real_time', aggfunc=np.sum)

        realise = table['real_time'].tolist()
        categories = table.index.tolist()

        plt.pie(realise, labels=categories, autopct='%1.0f%%')
        plt.title("Réalisé par catégorie")

        plt.savefig(self.path + 'realisé-pie.png')

    def task_pivot_to_bar(self):
        df = pd.DataFrame([task.__dict__ for task in self.tasks])
        table1 = df[['category', 'real_time']].pivot_table(index='category', values='real_time', aggfunc=np.sum)
        table2 = df[['category', 'estimate_time']].pivot_table(index='category', values='estimate_time', aggfunc=np.sum)
        fig = plt.figure(figsize=(10, 5))
        categories = table1.index.tolist()
        realise = table1['real_time'].tolist()
        estimate = table2['estimate_time'].tolist()

        # Set position of bar on X axis
        barWidth = 0.40
        br1 = np.arange(len(categories))
        br2 = [x + barWidth for x in br1]

        print(br1)
        print(br2)

        plt.bar(br2, realise, color='maroon',
                width=barWidth, label='realisé', edgecolor='grey')
        plt.bar(br1, estimate, color='green',
                width=barWidth, label='estimé', edgecolor='grey')

        plt.xlabel("Catégories")
        plt.ylabel("Temps")
        plt.title("Temps passé par catégorie")
        plt.xticks([r + barWidth for r in range(len(categories))],
                   categories)
        plt.legend()
        plt.savefig(self.path + 'realisé-bar.png')

    def print_tasks(self):
        for t in self.tasks:
            print(t)


