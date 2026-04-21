```python

def calculer\_valeur\_stock(inventaire, prix\_unitaires):

&#x20;   total = 0

&#x20;   indices = 0



&#x20;   while indices < len(inventaire):

&#x20;       produit = inventaire\[indices]

&#x20;       prix = prix\_unitaires\[produit.lower()]

&#x20;       total += prix

&#x20;       indices += 1



&#x20;   return total



def main():

&#x20;   mon\_stock = \["Console", "Manette", "Jeu"]

&#x20;   catalogue = {

&#x20;       "console": 300,

&#x20;       "manette": 50,

&#x20;       "jeu": 60

&#x20;   }

&#x20;   print("Analyse du stock en cours...")

&#x20;   resultat = calculer\_valeur\_stock(mon\_stock, catalogue)

&#x20;   print(f"Valeur totale du stock : {resultat}€")



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   main()

```



