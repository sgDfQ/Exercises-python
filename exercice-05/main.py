from outils import convertir_note, mention, moyenne

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes_valides = []
notes_invalides = 0

for note_brute in notes_brutes:
    note = convertir_note(note_brute)
    if note is None:
        notes_invalides += 1
    else:
        notes_valides.append(note)

moyenne_generale = moyenne(notes_valides)
mention_finale = mention(moyenne_generale)

print(f"Notes ignorées : {notes_invalides}")
print(f"Moyenne : {moyenne_generale:.2f}")
print(f"Mention : {mention_finale}")