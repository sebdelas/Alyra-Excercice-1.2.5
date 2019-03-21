#!/usr/bin/env python3

class Noeud:
    def __init__(self, v):
        self.gauche = None
        self.droit = None
        self.valeur = v

class Arbre:
    def __init__(self):
        self.racine = None

    def ajouter(self, val):
        if(self.racine == None):
            self.racine = Noeud(val)
        else:
            self._ajouter(val, self.racine)

    def _ajouter(self, val, nd):
        if(val < nd.valeur  ):
            if(nd.gauche is not None):
                self._ajouter(val, nd.gauche)
            else:
                nd.gauche = Noeud(val)
        else:
            if(nd.droit is not None):
                self._ajouter(val, nd.droit)
            else:
                nd.droit = Noeud(val)

    def rechercher(self, val):
        if (self.racine.valeur is not None):
            return self._rechercher(self.racine, val)

    def _rechercher(self, nd, val):
        ret = None
        if (nd.gauche is not None):
            ret = self._rechercher(nd.gauche, val)
        if (nd.droit is not None and ret is None):
            ret = self._rechercher(nd.droit, val)        
        if (val == nd.valeur):
            ret = nd
        return ret

    def afficher(self):
        if (self.racine.valeur is not None):
            self._afficher(self.racine)        

    def _afficher(self, nd):
        if (nd.gauche is not None):
            self._afficher(nd.gauche)
        print (nd.valeur)            
        if (nd.droit is not None):
            self._afficher(nd.droit)

    def supprimer(self, nd):
        if (self.racine == nd):
            self.racine = None
        else:
            self._supprimer(self.racine, nd)  

    def _supprimer(self, nd, ndtodel):
        trouve = False
        if (nd.gauche is not None):
            trouve = self._supprimer(nd.gauche, ndtodel)
            if (trouve == False and nd.gauche.valeur == ndtodel.valeur):                
                if (nd.gauche.gauche is None and nd.gauche.droit is None):
                    nd.gauche = None                
                elif (nd.gauche.gauche is None or nd.gauche.droit is None):
                    if (nd.gauche.gauche is None):
                        nd.gauche = nd.gauche.droit
                    else:
                        nd.gauche = nd.gauche.gauche
                else:
                    ndrempl = nd.gauche.gauche
                    while (ndrempl.droit is not None):
                        ndrempl = ndrempl.droit
                    ndrempl.droit = nd.gauche.droit
                    nd.gauche = ndrempl
                trouve = True            
        if (nd.droit is not None and trouve == False):
            trouve = self._supprimer(nd.droit, ndtodel)        
            if (trouve == False and nd.droit.valeur == ndtodel.valeur):
                if (nd.droit.gauche is None and nd.droit.droit is None):
                    nd.droit = None                
                elif (nd.droit.gauche is None or nd.droit.droit is None):
                    if (nd.droit.gauche is None):
                        nd.droit = nd.droit.droit
                    else:
                        nd.droit = nd.droit.gauche
                else:
                    ndrempl = nd.droit.droit
                    while (ndrempl.gauche is not None):
                        ndrempl = ndrempl.gauche
                    ndrempl.gauche = nd.droit.gauche
                    nd.droit = ndrempl
                trouve = True
        return trouve
       
arbre = Arbre()
arbre.ajouter('A')
arbre.ajouter('2')
arbre.ajouter('B')
arbre.ajouter('1')
arbre.ajouter('3')
arbre.ajouter('C')
print ('Arbre complet')
arbre.afficher()
print ('Arbre après suppression du noeud 2 (deux enfants)')
nd = arbre.rechercher('2')
arbre.supprimer(nd)
arbre.afficher()
print ('Arbre après suppression de la feuille 1')
nd = arbre.rechercher('1')
arbre.supprimer(nd)
arbre.afficher()
print ('Arbre après suppression du noeud B (un enfant)')
nd = arbre.rechercher('B')
arbre.supprimer(nd)
arbre.afficher()

