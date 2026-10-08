# Conditions de temperature
temperature = float(input("Entrez la température en degrés Celsius : "))

if temperature < 0:
    print("Gel")
elif temperature < 15:
    print("Froid")
elif temperature < 25:
    print("Doux")
else:
    print("Chaud")

#Test avec -3, 0, 15 et 31; Verifier les cas limites


# Une année bissextile si elle est divisible par 4 mais pas par 100,
# ou si elle est divisible par 400.
annee = int(input("Entrez une année : "))

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")

# Test avec 2020, 1900, 2000 et 2023 ; vérifier les cas limites

