import numpy as np
import pandas as pd


class DataScience:
    """ Exercices issus de la formation OCR
    https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science
    """

    def __init__(self):
        pass

    def tests_np3(self):
        prets = pd.read_csv('https://raw.githubusercontent.com/benjaminmrl/data-4452741/main/prets.csv')

        prets.rename(columns={'taux': 'taux_interet'}, inplace=True)
        print(prets.keys())

        prets['taux_endettement'] = round(prets['remboursement'] / (prets['revenu']) * 100, 2)

        prets['cout_total'] = prets['remboursement'] * prets['duree']

        prets['benefices'] = round(prets['cout_total'] * prets['taux_interet'] / 24 / 100, 2)

        prets = prets.sort_values('benefices', ascending=False)

        print(prets.head())

        print(prets.loc[0:10, :])
        print(prets.iloc[0:10, :])

    def tests_np2(self):
        data = np.arange(7)
        print(data)

        a = np.linspace(5, 10, 11)
        print(a)
        print(a[-3:-1])

        b = np.array([
            [[1, 2], [4, 5]],
            [[6, 7], [8, 9]],
            [[10, 11], [12, 13]]])
        print(b)

    def tests_np(self):
        hugo = [1800, 21, 0]
        richard = [1500, 54, 2]
        emilie = [2200, 28, 3]
        pierre = [3000, 37, 1]
        paul = [2172, 37, 2]
        deborah = [5000, 32, 0]
        yohann = [1400, 23, 0]
        anne = [1200, 25, 1]
        thibault = [1100, 19, 0]
        emmanuel = [1300, 31, 2]

        tableau = [hugo, richard, emilie, pierre, paul, deborah,
                   yohann, anne, thibault, emmanuel]

        print(tableau)
        data = np.array(tableau)
        print(data[4, :])
        m = data[4, 0] * 35 / 100
        print(m)

        louise = [1900, 31, 1]
        data = np.vstack((data, louise))
        print(data)

        revenus = data[:, 0]
        print(revenus)