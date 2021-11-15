Petit script python pour résoudre un circuit de 2e ordre rapidement.

Pour faire rouler le script, modifier les variables avec un commentaire
"===VARIABLE À MODIFIER===" juste au dessus en suivant les indications et l'exemple.

Le script sortir l'ED, la solution particulière, les racines, la solution
homogène et finalement la solution complète.

Utilisez la variable `I` pour définir un nombre imaginaire si nécessaire.

L'exemple déjà présent dans le fichier est pour un circuit comme celui-ci. Pour
l'exemple la méthode utilisé est la méthode des courants circulatoire et on
veut trouver j_2:

  L2=.25H   L1=0.2H
+---nnn---+---nnn---+
| j1 ->   | j2 ->   |
O V=100  | | R2=100| |
|   R1=50| |       | |
|         |         |
+---------+---------+

On va donc avoir la matrice suivante:
+-                      -++-  -+   +-  -+
| R1 + L1s     -R1       || j1 | = | Vs |
|   -R1    R1 + R2 + L2s || j2 |   | 0  |
+-                      -++-  -+   +-  -+

En entrant les valeurs de la matrice directement dans le script on peut
facilement obtenir la solution.
