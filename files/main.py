import tkinter as tk
from tkinter import ttk
from pypresence import Presence
import time
import threading

# Variable pour stocker l'heure de début
start_time = None
RPC = None  # Initialisation vide

# Fonction pour démarrer la connexion à Discord et enregistrer l'heure de début
def start_rpc():
    global start_time, RPC

    client_id = client_id_entry.get().strip()  # Récupère l'ID entré
    if not client_id:
        status_label.config(text="⚠ Erreur : Entre un Client ID !", foreground="red")
        return
    
    try:
        RPC = Presence(client_id)
        RPC.connect()
        start_time = int(time.time())  # Enregistre l'heure actuelle UNE FOIS au démarrage
        status_label.config(text="✅ Connecté à Discord", foreground="green")
    except Exception as e:
        status_label.config(text=f"❌ Erreur : {str(e)}", foreground="red")

# Fonction pour mettre à jour le Rich Presence (sans changer l'heure de début)
def update_presence():
    global start_time, RPC
    if start_time is None or RPC is None:
        status_label.config(text="⚠ Erreur : Lance le RPC d'abord !", foreground="red")
        return
    
    state = state_entry.get()
    details = details_entry.get()

    try:
        RPC.update(state=state, details=details, start=start_time)  # Utilise toujours le même temps
        status_label.config(text="✅ Statut mis à jour !", foreground="green")
    except Exception as e:
        status_label.config(text=f"❌ Erreur : {str(e)}", foreground="red")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Discord Rich Presence")

# Taille et style
window.geometry("450x400")
window.configure(bg="#2C2F33")

# Style général
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 11), background="#2C2F33", foreground="white")

# Titre
title_label = ttk.Label(window, text="🎮 Discord Rich Presence", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Champ pour entrer le Client ID
ttk.Label(window, text="🆔 Client ID :").pack(pady=5)
client_id_entry = ttk.Entry(window, width=40)
client_id_entry.pack(pady=5)

# Détails de l'activité
ttk.Label(window, text="📝 Détails de l'activité :").pack(pady=5)
details_entry = ttk.Entry(window, width=40)
details_entry.pack(pady=5)

# État de l'activité
ttk.Label(window, text="🎭 État de l'activité :").pack(pady=5)
state_entry = ttk.Entry(window, width=40)
state_entry.pack(pady=5)

# Bouton pour démarrer la connexion RPC
start_button = ttk.Button(window, text="🚀 Démarrer RPC", command=lambda: threading.Thread(target=start_rpc).start())
start_button.pack(pady=10)

# Bouton pour mettre à jour le Rich Presence
update_button = ttk.Button(window, text="🔄 Mettre à jour", command=update_presence)
update_button.pack(pady=5)

# Label de statut
status_label = ttk.Label(window, text="🔴 Non connecté", foreground="red")
status_label.pack(pady=10)

# Démarrer l'interface graphique
window.mainloop()
