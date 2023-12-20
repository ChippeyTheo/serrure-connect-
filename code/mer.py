from machine import Pin, PWM
from time import sleep_ms

# Définir les fréquences pour chaque note
f4 = 349
g4 = 392
a4 = 440
b4 = 493
c5 = 523
d5 = 587
e5 = 659
f5 = 698
g5 = 784
a5 = 880
rest = -1

# Connectez votre buzzer à ce pin ou changez-le pour correspondre à votre circuit!
pin = Pin(25, mode=Pin.OUT)
pin_with_pwm = PWM(pin)

# Définir la mélodie
melody = [f4, f4, f4, a4, f5, e5, d5, c5, a4, g4, f4, g4, a4]

# Définir le rythme
rhythm = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

# Jouer la mélodie
for i in range(len(melody)):
    if melody[i] > 0:
        pin_with_pwm.freq(melody[i])  # Définir la fréquence
        pin_with_pwm.duty_u16(512)  # Activer le buzzer
    else:
        pin_with_pwm.duty_u16(0)  # Désactiver le buzzer si la note est un repos
    sleep_ms(int(rhythm[i] * 100 * 1.25))  # Attendre pour la durée de la note

pin_with_pwm.deinit()  # Désactiver le PWM
