from training import Training, Project, ProjectLoader

MAIN_DIR = "C:\\Users\\brico\Documents\\8_Informatique\\"


def load_training():
    t1 = Training("Formation développement python")
    t1.path = MAIN_DIR + "1_Formation python\\0-Administratif\\"
    t1.file = "planning.csv"
    t1.load_projects()
    print(repr(t1))


def load_p1():
    p1 = Project("Projet 1")
    p1.description = "Démarrer votre formation de développeur"
    +" d'application Python"
    p1.path = MAIN_DIR + "1_Formation python\\Projet 1\\"
    p1.project_file = "suivi-projet 1.csv"
    print(p1)
    analyse_projet(p1)


def load_p2():
    p2 = Project("Projet 2")
    p2.description = "Utilisez les bases de Python pour l'analyse de marché"
    p2.path = MAIN_DIR + "1_Formation python\\Projet 2\\"
    p2.project_file = "suivi-projet2.csv"
    print(p2)
    analyse_projet(p2)


def load_p3():
    p = Project("Projet 3")
    p.description = "Designez une application adaptée aux besoins d'un client"
    p.path = MAIN_DIR + "1_Formation python\\Projet 3\\"
    p.project_file = "suivi-projet3.csv"
    print(p)
    analyse_projet(p)


def load_p4():
    p = Project("Projet 4")
    p.description = "Développez un programme logiciel en Python"
    p.path = MAIN_DIR + "1_Formation python\\Projet 4\\"
    p.project_file = "suivi-projet4.csv"
    print(p)
    analyse_projet(p)


def load_p5():
    p = Project("Projet 5")
    p.description = "Testez votre maîtrise du langage Python"
    p.path = MAIN_DIR + "1_Formation python\\Projet 5\\"
    p.project_file = "suivi-projet5.csv"
    print(p)
    analyse_projet(p)


def load_p6():
    p = Project("Projet 6")
    p.description = "Développez une interface utilisateur "
    +"pour une application web Python"
    p.path = MAIN_DIR + "1_Formation python\\Projet 6\\"
    p.project_file = "suivi-projet6.csv"
    print(p)
    analyse_projet(p)


def load_p7():
    p = Project("Projet 7")
    p.description = ""
    p.path = MAIN_DIR + "1_Formation python\\Projet 7\\"
    p.project_file = "suivi-projet7.csv"
    print(p)
    analyse_projet(p)


def load_p8():
    p = Project("Projet 8")
    p.description = ""
    p.path = MAIN_DIR + "1_Formation python\\Projet 8\\"
    p.project_file = "suivi-projet8.csv"
    print(p)
    analyse_projet(p)


def load_p9():
    p = Project("Projet 9")
    p.description = "Développez une application Web en utilisant Django"
    p.path = MAIN_DIR + "1_Formation python\\Projet 9\\"
    p.project_file = "suivi-projet9.csv"
    print(p)
    analyse_projet(p)


def analyse_projet(projet):
    p_loader = ProjectLoader(projet)
    p_loader.load_csv()
    print(repr(projet))
    projet.task_pivot_to_table_r()
    projet.task_pivot_to_pie()
    projet.task_pivot_to_bar()


def main():
    load_training()
    load_p7()


if __name__ == "__main__":
    main()
