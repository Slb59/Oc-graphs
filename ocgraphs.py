from training import *

def load_training():
    t1 = Training('Formation développement python')
    t1.path = "C:\\Users\\brico\Documents\\8_Informatique\\1_Formation python\\0-Administratif\\"
    t1.file = 'planning.csv'
    t1.load_projects()
    print(repr(t1))

def load_p1():
    p1 = Project('Projet 1')
    p1.description = "Démarrer votre formation de développeur d'application Python"
    p1.path = "C:\\Users\\brico\\Documents\\8_Informatique\\1_Formation python\\Projet 1\\"
    p1.project_file = 'suivi-projet 1.csv'
    print(p1)
    analyse_projet(p1)

def load_p2():
    p2 = Project('Projet 2')
    p2.description = "Utilisez les bases de Python pour l'analyse de marché"
    p2.path = "C:\\Users\\brico\\Documents\\8_Informatique\\1_Formation python\\Projet 2\\"
    p2.project_file = 'suivi-projet2.csv'
    print(p2)
    analyse_projet(p2)

def load_p3():
    p = Project('Projet 3')
    p.description = "Designez une application adaptée aux besoins d'un client"
    p.path = "C:\\Users\\brico\\Documents\\8_Informatique\\1_Formation python\\Projet 3\\"
    p.project_file = 'suivi-projet3.csv'
    print(p)
    analyse_projet(p)

def analyse_projet(projet):
    p1_loader = ProjectLoader(projet)
    p1_loader.load_csv()
    projet.task_pivot_to_table()
    projet.task_pivot_to_pie()
    projet.task_pivot_to_bar()


def main():

    load_training()
    load_p1()
    load_p2()
    load_p3()


if __name__ == '__main__':
    main()
