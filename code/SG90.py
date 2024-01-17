from machine import Pin, PWM


class SG90:
    def __init__(self, pin: int = 17):
        self.__pwm = PWM(Pin(pin, Pin.OUT), freq=50, duty=0)
        self.__pwm.duty_u16(0)
        self.__pwm.freq(50)
        self.__state = False
        self.__min_duty_cycle = 20.0
        self.__max_duty_cycle = 130.0

    def __degree_to_duty_cycle(self, degree: float):
        """
        SG90 plage : 0 à 203 degrés
        et un rapport cyclique de 20 à 130.
        """
        if degree < 0:
            degree = 0
        elif degree > 203:
            degree = 203
        return int(((degree / 203.0) * (self.__max_duty_cycle - self.__min_duty_cycle)) + self.__min_duty_cycle)

    def open(self):
        self.__pwm.duty_u16(self.__degree_to_duty_cycle(90))
        self.__state = True

    def close(self):
        self.__pwm.duty_u16(self.__degree_to_duty_cycle(0))
        self.__state = False
