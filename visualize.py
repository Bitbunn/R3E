# visualize.py
from shared_memory_reader import SharedMemoryReader
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Initialisation du lecteur de mémoire partagée
reader = SharedMemoryReader()

# Listes pour stocker les données à tracer
times = []
speeds = []

# Création d'une figure et d'un axe pour le graphique
fig, ax = plt.subplots(figsize=(10, 6))

# Initialisation de la ligne pour la vitesse
line, = ax.plot([], [], label="Vitesse (m/s)")

# Configuration du graphique pour la vitesse
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)  # Ajuster selon la plage de vitesse attendue
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Vitesse (m/s)")
ax.legend()

# Fonction pour initialiser le graphique
def init():
    line.set_data([], [])
    return line,

# Fonction pour mettre à jour le graphique
def update(frame):
    data = reader.get_player_data()

    if data:
        current_time = time.time() - start_time
        try:

            speed = data['Velocity']['X']  # Remplacer par la clé réelle pour la vitesse
        except KeyError:
            print("Clé 'Velocity' ou 'X' non trouvée dans les données. Clés disponibles :", data.keys())
            return line,

        times.append(current_time)
        speeds.append(speed)

        #les 100 derniers points pour un graphique en temps réel fluide
        times_trimmed = times[-100:]
        speeds_trimmed = speeds[-100:]

        line.set_data(times_trimmed, speeds_trimmed)

        ax.set_xlim(times_trimmed[0], times_trimmed[-1])
        ax.set_ylim(0, max(speeds_trimmed) + 5)  # S'assurer que l'axe Y commence à 0
    return line,

# Capture du temps de départ
start_time = time.time()

# Création d'une animation qui met à jour le graphique
ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=100)  # Intervalle en millisecondes

plt.tight_layout()
plt.show()
