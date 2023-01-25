import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class ProjectGraph:
    def __init__(self, project):
        self.project = project

    def draw(self):

        # define Seaborn color palette to use
        colors = sns.color_palette('pastel')[0:5]
        # create pie chart
        table = self.project.df.pivot_table(index='category', values='real_time', aggfunc=np.sum, dropna=True)
        print(table['real_time'])
        plt.pie(table['real_time'], labels=table['category'], colors=colors, autopct='%.0f%%')
        plt.show()
