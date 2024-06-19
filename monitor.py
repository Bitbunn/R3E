# monitor.py
from shared_memory_reader import SharedMemoryReader
import time

def monitor_values():
    reader = SharedMemoryReader()
    prev_suspension_deflection = None
    prev_velocity = None

    while True:
        data = reader.get_player_data()
        if data:
            # Surveillance de la Position
            position = data.get('Position', {})
            print("Position:", position)

            # Surveillance de la Vélocité
            velocity = data.get('Velocity', {})
            print("Velocity:", velocity)

            # Surveillance de la Déflexion de la Suspension
            suspension_deflection = data.get('SuspensionDeflection', {})
            print("SuspensionDeflection:", suspension_deflection)

            # Surveillance de la Vitesse de la Suspension
            suspension_velocity = data.get('SuspensionVelocity', {})
            print("SuspensionVelocity:", suspension_velocity)

            # Surveillance de la Charge des Pneus
            tire_load = data.get('TireLoad', {})
            print("TireLoad:", tire_load)

            # Surveillance du Glissement des Roues
            wheel_slip = data.get('WheelSlip', {})
            print("WheelSlip:", wheel_slip)

            # Surveillance des Accélérations
            acceleration = data.get('Acceleration', {})
            print("Acceleration:", acceleration)

            # Détection de collision basée sur la déflexion de la suspension
            if prev_suspension_deflection:
                for key in suspension_deflection:
                    if abs(suspension_deflection[key] - prev_suspension_deflection[key]) > 0.05:  # Seuil à ajuster
                        print("Collision détectée!")
                        break
            prev_suspension_deflection = suspension_deflection

            # Détection de sortie de route basée sur le glissement des roues
            for key in wheel_slip:
                if wheel_slip[key] > 0.5:  # Seuil à ajuster
                    print("Sortie de route détectée!")
                    break
            
            # Détection de collision basée sur la vélocité
            if prev_velocity:
                if abs(velocity['X'] - prev_velocity['X']) > 5 or abs(velocity['Y'] - prev_velocity['Y']) > 5 or abs(velocity['Z'] - prev_velocity['Z']) > 5:  # Seuils à ajuster
                    print("Collision détectée!")
            prev_velocity = velocity

        else:
            print("Failed to retrieve data. Data is None.")
        time.sleep(0.1)  # Ajuster l'intervalle à 0.1 seconde

if __name__ == "__main__":
    monitor_values()
