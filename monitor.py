# monitor.py
from shared_memory_reader import SharedMemoryReader
import time

def monitor_values():
    reader = SharedMemoryReader()
    while True:
        data = reader.get_player_data()
        if data:
            # Afficher les données de position
            position = data.get('Position', {})
            print("Position:", position)
            
            # Afficher les données de vitesse
            velocity = data.get('Velocity', {})
            print("Velocity:", velocity)
            
            # Afficher les données de déflexion de la suspension
            suspension_deflection = data.get('SuspensionDeflection', {})
            print("SuspensionDeflection:", suspension_deflection)
            
            # Afficher les données de vitesse de la suspension
            suspension_velocity = data.get('SuspensionVelocity', {})
            print("SuspensionVelocity:", suspension_velocity)
            
            # Afficher les autres données pertinentes
            engine_rpm = data.get('EngineRPM', 'N/A')
            print("EngineRPM:", engine_rpm)
            
        else:
            print("Failed to retrieve data. Data is None.")
        time.sleep(0.1)  # Ajuster l'intervalle à 0.1 seconde

if __name__ == "__main__":
    monitor_values()
