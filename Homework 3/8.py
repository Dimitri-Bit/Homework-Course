class Player:
    
    def __init__(self, x, y, widht, height, health):
        self.__x = x
        self.__y = y
        self.__width = widht
        self.__height = height
        self.__health = health

    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__x = y

    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        self.__height = height

    def get_health(self):
        return self.__health
    
    def set_damage(self, health):
        if health >= 0 and health <= 100:
            self.__health = health

class Enemy:
    
    def __init__(self, x, y, widht, height, damage):
        self.__x = x
        self.__y = y
        self.__width = widht
        self.__height = height
        self.__damage = damage

    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__x = y

    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        self.__height = height

    def get_damage(self):
        return self.__damage
    
    def set_damage(self, damage):
        if damage >= 0 and damage <= 100:
            self.__damage = damage

def check_collision(player, enemy):
    if player.get_x() == enemy.get_x() and player.get_y() == enemy.get_y():
        return True
    
    return False

def decreate_health(player, enemy):
    if check_collision(player, enemy):
        player.set_health(player.get_health() - enemy.get_damage())
        player.health = player.health - enemy.damage


player1 = Player(5, 2, 2, 6, 100)

enemy1 = Enemy(5, 2, 2, 6, 25)
enemy2 = Enemy(3, 15, 2, 5, 15)

print(check_collision(player1, enemy1))