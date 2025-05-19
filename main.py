class ColorRGB:
    def __init__(self, red, green, blue):
        if red < 0 or red > 255:
            raise ValueError("red повинен бути вiд 0 до 255")
        if green < 0 or green > 255:
            raise ValueError("green повинен бути вiд 0 до 255")
        if blue < 0 or blue > 255:
            raise ValueError("blue повинен бути вiд 0 до 255")
        self.red = red
        self.green = green
        self.blue = blue

    def show(self):
        print(f"колiр: ({self.red}, {self.green}, {self.blue})")

    def to_hex(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)

    def grayscale(self):
        avg = (self.red + self.green + self.blue) // 3
        return ColorRGB(avg, avg, avg)

    def brightness(self):
        return (self.red + self.green + self.blue) / 3

    def __eq__(self, other):
        return (self.red, self.green, self.blue) == (other.red, other.green, other.blue)

if __name__ == "__main__":
    try:
        print(" створюємо основний колiр:")
        color1 = ColorRGB(100, 150, 200)
        color1.show()

        print("\n hex формат:")
        print(color1.to_hex())

        print("\n вiдтiнок сiрого:")
        gray = color1.grayscale()
        gray.show()

        print("\n яскравiсть:")
        print(color1.brightness())

        print("\n перевiрка рiвностi:")
        same = ColorRGB(100, 150, 200)
        print("color1 == same:", color1 == same)

        print("\n спроба створити неправильний колiр:")
        bad = ColorRGB(300, -10, "50")

    except Exception as e:
        print(" сталася помилка:", e)
