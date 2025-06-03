class ColorRGB:
    def __init__(self, red, green, blue):
        #R, G, B 
        self.red = min(255, max(0, red))
        self.green = min(255, max(0, green))
        self.blue = min(255, max(0, blue))

    def show(self):
        """Показывает цвет в консоли"""
        print(f"RGB({self.red}, {self.green}, {self.blue})")
    
    def get_hex(self):
        #HEX-цвет
        return "#{:02X}{:02X}{:02X}".format(self.red, self.green, self.blue)

    def create_from_hex(hex_code):
        #HEX
        hex_code = hex_code.lstrip('#')
        if len(hex_code) != 6:
            raise ValueError("HEX код должен содержать 6 символов")
        return ColorRGB(
            int(hex_code[0:2], 16),
            int(hex_code[2:4], 16),
            int(hex_code[4:6], 16)
        )

    def grayscale(self):
        #серый вариант цвета
        gray = (self.red + self.green + self.blue) // 3
        return ColorRGB(gray, gray, gray)

    def brightness(self):
        # яркость цвета
        return (self.red + self.green + self.blue) / 3

    def invert(self):
        return ColorRGB(255-self.red, 255-self.green, 255-self.blue)

    def mix(self, other, ratio=0.5):
        #смешиваем
        r = int(self.red*(1-ratio) + other.red*ratio)
        g = int(self.green*(1-ratio) + other.green*ratio)
        b = int(self.blue*(1-ratio) + other.blue*ratio)
        return ColorRGB(r, g, b)

    def __eq__(self, other):
        #равенство цветов
        return (self.red, self.green, self.blue) == (other.red, other.green, other.blue)


if __name__ == "__main__":
    color1 = ColorRGB(100, 150, 200)
    color2 = ColorRGB.create_from_hex("#FFA500")  # оранжевый
    
    print("Основной цвет:")
    color1.show()
    print("HEX:", color1.get_hex())
    
    print("\nЦвет из HEX-кода:")
    color2.show()
    print("HEX:", color2.get_hex())
    
    print("\nСерый вариант:")
    color2.grayscale().show()
    
    print("\nИнвертированный:")
    color2.invert().show()
