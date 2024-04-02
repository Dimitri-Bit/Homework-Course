class Color:

    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def get_red(self):
        return self.__red
    
    def set_red(self, red):
        if red >= 0 and red <= 255:
            self.__red = red
        else:
            print(f"Invalid value for color \"{red}\"")
    
    def get_green(self):
        return self.__green

    def set_green(self, green):
        if green >= 0 and green <= 255:
            self.__green = green
        else:
            print(f"Invalid value for color \"{green}\"")

    def get_blue(self):
        return self.__blue

    def set_blue(self, blue):
        if blue >= 0 and blue <= 255:
            self.__blue = blue
        else:
            print(f"Invalid value for color \"{blue}\"")

    def add_red(self, amount):
        temp = self.__red + amount
        if temp >= 0 and temp <= 255:
            self.__red += amount
        else:
            print("Invalid change for the color red (out of range)")

    def add_green(self, amount):
        temp = self.__green + amount
        if temp >= 0 and temp <= 255:
            self.__green += amount
        else:
            print("Invalid change for the color green (out of range)")

    def add_blue(self, amount):
        temp = self.__blue + amount
        if temp >= 0 and temp <= 255:
            self.__blue += amount
        else:
            print("Invalid change for the color blue (out of range)")

    def __lt__(self, color1, color2):
        if color1.get_red() < color2.get_red() and color1.get_green() < color2.get_green() and color1.get_blue() < color2.get_blue():
            return True
        else:
            return False

    def __str__(self):
        print(f"red: {self.__red}, green: {self.__green}, blue: {self.__blue}")

class AlphaColor(Color):

    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self.__alpha = alpha

    def set_alpha(self, alpha):
        if alpha >= 0 and alpha <= 1:
            self.__alpha = alpha
        else:
            print("Invalid alpha value")

    def set_color_by_alpha(self):
        red_alpha = self.get_red() * self.__alpha
        green_alpha = self.get_green() * self.__alpha
        blue_alpha = self.get_blue() * self.__alpha

        self.set_red(red_alpha)
        self.set_green(green_alpha)
        self.set_blue(blue_alpha)


color1 = Color(12, 12, 12)
color2 = Color(56, 252, 20)

# print(color1.__lt__(color1, color2))
# color1.__str__()

alphaColor = AlphaColor(29, 125, 221, 0.3)
alphaColor.__str__()
alphaColor.set_alpha(0.5)
alphaColor.set_color_by_alpha()
alphaColor.__str__()
