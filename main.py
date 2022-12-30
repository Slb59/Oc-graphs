from training.training import Training
from training.project import Project

def main():
    training = Training('Formation développement python')
    training.load_projects('C:\Users\brico\Documents\8_Informatique\1_Formation python\0-Administratif\planning.ods')
    p1 = Project('Projet 1')
    p1.description = "Démarrer votre formation de développeur d'application Python"
    print(p1)

if __name__ == '__main__':
    main()
