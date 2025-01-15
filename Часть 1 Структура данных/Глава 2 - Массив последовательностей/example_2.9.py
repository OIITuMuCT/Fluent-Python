# Пример 2.9. Метод из гипотетического класса Robot

def handle_command(self, message):
    match message:
        case [ 'BEEPER', frequency, times]:
            self.beep(times, frequency)

if __name__ == "__main__":
    main()
