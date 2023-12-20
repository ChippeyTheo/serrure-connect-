import machine
import time

# Configuration du broche PWM
pin_pwm = machine.Pin(5)  # Remplacez le numéro de broche selon votre configuration
pwm = machine.PWM(pin_pwm)
pwm.freq(440)  # Réglez la fréquence du buzzer

# Notes de la mélodie du coffre de Zelda
notes = [440, 0, 523, 0, 659, 0, 880, 0, 659, 0, 523, 0, 440, 0, 523, 0, 659, 0, 783, 0, 659, 0, 523, 0, 440, 0]

# Durée de chaque note en secondes
duree_notes = [0.3, 0.1, 0.3, 0.1, 0.3, 0.1, 0.6, 0.1, 0.3, 0.1, 0.3, 0.1, 0.6, 0.1, 0.3, 0.1, 0.3, 0.1, 0.6, 0.1, 0.3,
               0.1, 0.3, 0.1, 0.6, 0.1]

# Jouer la mélodie
for i in range(len(notes)):
    if notes[i] != 0:
        pwm.freq(notes[i])  # Définir la fréquence pour jouer la note
        pwm.duty_u16(512)  # Réglez le rapport cyclique du PWM pour générer du son
        time.sleep(duree_notes[i])  # Attendre la durée de la note
    else:
        pwm.duty_u16(0)  # Arrêter le son pour les notes avec une fréquence de 0
        time.sleep(duree_notes[i])  # Attendre la durée de la pause entre les notes

# Arrêter le son à la fin de la mélodie
pwm.duty_u16(0)
