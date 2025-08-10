import json
import os
import tkinter as tk
from tkinter import filedialog

def update_paths(file_path, new_base_path):
    """
    Aggiorna i percorsi dei file all'interno del file .escore.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Estrai la directory del file .escore
    escore_dir = os.path.dirname(file_path)

    # Aggiorna i percorsi dei file
    for sound_object in data['sound_objects']:
        old_path = sound_object['filename']
        # Trova il nome del file relativo al file .escore
        relative_path = os.path.relpath(old_path, escore_dir)
        # Crea il nuovo percorso completo
        new_path = os.path.join(new_base_path, relative_path)
        sound_object['filename'] = new_path

    # Salva il file modificato
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def select_escore_file():
    """
    Seleziona il file .escore da modificare.
    """
    escore_path = filedialog.askopenfilename(
        title="Seleziona il file .escore",
        filetypes=[("EScore files", "*.escore")]
    )
    if escore_path:
        select_new_base_path(escore_path)

def select_new_base_path(escore_path):
    """
    Seleziona il nuovo percorso base per i file.
    """
    new_base_path = filedialog.askdirectory(
        title="Seleziona la nuova directory per i file"
    )
    if new_base_path:
        update_paths(escore_path, new_base_path)
        tk.messagebox.showinfo("Successo", "I percorsi dei file sono stati aggiornati correttamente.")

# Creazione dell'interfaccia utente
root = tk.Tk()
root.title("Aggiorna Percorsi .escore")

# Bottone per selezionare il file .escore
select_escore_button = tk.Button(root, text="Seleziona file .escore", command=select_escore_file)
select_escore_button.pack(pady=20)

# Avvia l'interfaccia utente
root.mainloop()