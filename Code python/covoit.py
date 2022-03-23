'''
File: covoit.py
Project: Code python
Created Date: Su Jan 2022
Author: Julien Dagnelie
-----
Last Modified: Wed Mar 02 2022
Modified By: Julien Dagnelie & Loïc Tumelaire
-----
Copyright (c) 2022 Universite catholique de Louvain
-----
HISTORY:
Date   Sun Jan 16 2022   	By Julien Dagnelie	Comments
----------	---	---------------------------------------------------------
'''
def prix(historique, Conducteur, Passagers, prix_plein= 16 ):
    with open("historique_trajets.txt") as historique:             #Enregistrer le trajet (km + conducteur + passagers)

        try:
            list_passager = passagers
            km_perso = float(input("Quel est ton kilometrage personel ? : "))
            km_tot = km_perso

            for i in range(len(passagers)):
                x = i+1
                passager = float(input("Entrez le nombre de kilomètre du passager n°{} : ".format(x)))
                list_passager.append(passager)
                km_tot += passager
                
            for k in range(4):
                z = k + 1
                prix  = (list_passager[k]/km_tot)*prix_plein
                print("Le passager {} doit payer ".format(z), round(prix, 2), "€", sep="")
        except ValueError:
            print("Un plein ou des kilomètres ne se fait pas avec des lettres mais bien des chiffres")
        finally:
            print("C'est ici que se termine mon beau calcul")