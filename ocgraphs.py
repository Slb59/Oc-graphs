from training import *

def main():

    t1 = Training('Formation développement python')
    t1.path = "C:\\Users\\brico\Documents\\8_Informatique\\1_Formation python\\0-Administratif\\"
    t1.file = 'planning.csv'
    t1.load_projects()
    print(repr(t1))

    p1 = Project('Projet 1')
    p1.description = "Démarrer votre formation de développeur d'application Python"
    p1.path = "C:\\Users\\brico\\Documents\\8_Informatique\\1_Formation python\\Projet 1\\"
    p1.project_file = 'suivi-projet 1.csv'
    print(p1)
    p1_loader = ProjectLoader(p1)
    p1_loader.load_csv()
    p1.task_pivot_to_table()
    p1.task_pivot_to_pie()
    p1.task_pivot_to_bar()

    p2 = Project('Projet 2')
    p2.description = "Utilisez les bases de Python pour l'analyse de marché"
    p2.path = "C:\\Users\\brico\\Documents\\8_Informatique\\1_Formation python\\Projet 2\\"
    p2.project_file = 'suivi-projet2.csv'
    print(p2)
    p2_loader = ProjectLoader(p2)
    p2_loader.load_csv()
    p2.task_pivot_to_table()
    p2.task_pivot_to_pie()
    p2.task_pivot_to_bar()

if __name__ == '__main__':
    main()
