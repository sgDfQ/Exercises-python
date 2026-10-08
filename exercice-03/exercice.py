#Liste de temperatures
temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

#1.1 Calcul de la moyenne
moyenne = sum(temperatures) / len(temperatures)
print("Moyenne:", round(moyenne, 2))

#1.2 Calcul du minimum et du maximum
min_temperature = min(temperatures)
max_temperature = max(temperatures)
print("Mini:", min_temperature, "°", "Max:", max_temperature, "°")

#2. Compter avec une boucle les jours au-dessus de 15°C
jours_au_dessus_de_15 = 0
for temperature in temperatures:
    if temperature > 15:
        jours_au_dessus_de_15 += 1

print("Jours > 15°C:", jours_au_dessus_de_15)  

#3. Contruire une liste Farenheit: F = c x 9/5 + 32
temperatures_farenheit = []
for temperature in temperatures:
    temperature_f = temperature * 9/5 + 32
    temperatures_farenheit.append(round(temperature_f, 2))
print("Farenheit:", temperatures_farenheit)

#4. Afficher chaque jour avec enumerate : <jour 1 : 12.5°C>
for index, temperature in enumerate(temperatures, start=1):
    print(f"Jour {index} : {temperature}°C")    