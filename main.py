class ColorRGB:
    def __init__(self, red, green, blue):
        if red < 0 or red > 255:
            raise ValueError("red повинен бути від 0 до 255")
        if green < 0 or green > 255:
            raise ValueError("green повинен бути від 0 до 255")
        if blue < 0 or blue > 255:
            raise ValueError("blue повинен бути від 0 до 255")
        self.red = red
        self.green = green
        self.blue = blue

        def show(self):
            print(f"Колір: ({self.red}, {self.green}, {self.blue})")

        def to_hex(self):
            return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)

        def grayscale(self):
            avg = (self.red + self.green + self.blue) // 3
            return ColorRGB(avg, avg, avg)

        if __name__ == "__main__":
            try:
                color1 = ColorRGB(100, 150, 200)
                color1.show()
                print("HEX:", color1.to_hex())

                gray = color1.grayscale()
                gray.show()
                bad_color = ColorRGB(300, -10, 50)
            except Exception as e:
                print("сталася помилка:", e)