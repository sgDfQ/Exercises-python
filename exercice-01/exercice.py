# Variables
produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

# Calculs
total_ht = prix_ht * quantite
total_ttc = total_ht + (total_ht * taux_tva)

# Affichage avec f-string plus total en 2 decimales
print(f"Le total pour le {produit} est de {total_ttc:.2f} €.")

# Nouveau prix sous forme de texte
prix_texte = "19.90"

# Conversion en float et nouveau calcul
prix_ht = float(prix_texte)
total_ht = prix_ht * quantite
total_ttc = total_ht + (total_ht * taux_tva)

print(f"Le nouveau total est de {total_ttc:.2f} €.")