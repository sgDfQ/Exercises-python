#Liste de ventes
ventes = [
    {"produit": "café", "prix_ht": 2.5, "quantite": 120},
    {"produit": "thé", "prix_ht": 2.0, "quantite": 80},
    {"produit": "jus", "prix_ht": 3.5, "quantite": 45}
]

#1. Construire un dictionnaire ca_par_produit : produit vers prix + quantite
ca_par_produit = {}
for vente in ventes:
    produit = vente["produit"]
    prix_ht = vente["prix_ht"]
    quantite = vente["quantite"]
    ca_par_produit[produit] = prix_ht * quantite
print("CA par produit:", ca_par_produit)

#2. Calculer le chiffre d'affaires total
ca_total = sum(ca_par_produit.values())
print("Chiffre d'affaires total:", ca_total)

#3. Trouver le produit qui rapporte le plus

meilleur_produit = None
gain_max = 0

for produit, ca in ca_par_produit.items():
    if ca > gain_max:
        gain_max = ca
        meilleur_produit = produit

print(f"Produit : {meilleur_produit} ({gain_max} €)")