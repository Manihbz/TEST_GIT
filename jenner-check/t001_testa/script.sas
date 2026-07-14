/*------------------------------------------------------------*/
/* Script SAS simple utilisant la bibliothèque WORK bfff jhg         */
/*------------------------------------------------------------*/

/* Création d'un jeu de données dans WORK */
data test;
   input id name $ age;
   datalines;
1 Alice 25
2 Bob 30
3 Charlie 35
4 mani 23
5 aziz 69466666
;
run;

/* Affichage du jeu de données */
proc print data=test;
   title "Liste des individus";
run;

/* Calcul de statistiques descriptives sur l'âge */
proc means data=test;
   var age;
   title "Statistiques sur l'âge";
run;
