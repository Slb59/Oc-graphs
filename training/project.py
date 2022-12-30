class Project:
    def __init__(self, title):
        self.title = title
        self.description = ''

    """
    - Sujet
    - Titre
    - Description
    - Temps estimé
    - % temps / total
    - Nombre de jours affectés
    - Nombre heures sur le projet
    - Nombre d'heures affectées
    - Date de démarrage estimée
    - Date de fin estimée
    - Date de damarrage effectif
    - Date de fin effectif
    - Temps effectif
    - Temps consacré au projet
    - Date de soutenance
    """

    def __str__(self):
        return self.title + ': ' + self.description