from machine import Pin, PWM
from time import sleep_ms

# Définir les fréquences pour chaque note
a3f = 208
b3f = 233
b3 = 247
c4 = 261
c4s = 277
e4f = 311
f4 = 349
a4f = 415
b4f = 466
b4 = 493
c5 = 523
c5s = 554
e5f = 622
f5 = 698
f5s = 740
a5f = 831
rest = -1

# Connectez votre buzzer à ce pin ou changez-le pour correspondre à votre circuit!
pin = Pin(25, mode=Pin.OUT)
pin_with_pwm = PWM(pin)

# Définir la mélodie
melody = [c5s, e5f, e5f, f5, a5f, f5s, f5, e5f, c5s, e5f, rest, a4f, a4f]

# Définir le rythme
rhythm = [6, 10, 6, 6, 1, 1, 1, 1, 6, 10, 4, 2, 10]

# Jouer la mélodie
for i in range(len(melody)):
    if melody[i] > 0:
        pin_with_pwm.freq(melody[i])  # Définir la fréquence
        pin_with_pwm.duty_u16(512)  # Activer le buzzer
    else:
        pin_with_pwm.duty_u16(0)  # Désactiver le buzzer si la note est un repos
    sleep_ms(int(rhythm[i] * 100 * 1.25))  # Attendre pour la durée de la note

pin_with_pwm.deinit()  # Désactiver le PWM
