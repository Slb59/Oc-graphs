from training.training import Training
from training.project import Project

def main():
    training = Training('Formation développement python')
    training.path = "C:\\Users\\brico\Documents\\8_Informatique\\1_Formation python\\0-Administratif\\"
    training.file = 'planning.csv'
    training.load_projects()


    p1 = Project('Projet 1')
    p1.description = "Démarrer votre formation de développeur d'application Python"
    p1.path = "C:\\Users\\brico\\Documents\\8_Informatique\\1_Formation python\\Projet 1\\"
    p1.project_file = 'suivi-projet 1.csv'
    print(p1)
    p1.load_suivi_csv()
    p1.task_pivot_to_table()

if __name__ == '__main__':
    main()
