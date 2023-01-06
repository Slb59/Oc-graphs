from training import *
from exercises import *

def main():

    t1 = Training('Formation développement python')
    t1.path = "C:\\Users\\brico\Documents\\8_Informatique\\1_Formation python\\0-Administratif\\"
    t1.file = 'planning.csv'
    t1.load_projects()

    p1 = Project('Projet 1')
    p1.description = "Démarrer votre formation de développeur d'application Python"
    p1.path = "C:\\Users\\brico\\Documents\\8_Informatique\\1_Formation python\\Projet 1\\"
    p1.project_file = 'suivi-projet 1.csv'
    print(p1)
    p1l = ProjectLoader(p1)
    p1l.load_csv()
    p1.task_pivot_to_table()


if __name__ == '__main__':
    tests_data_science = DataScience()
    tests_data_science.tests_np3()
