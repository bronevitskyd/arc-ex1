# importation de la librairie arcade et random
import arcade
import random
#definir les parametres pour la fenetre
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MAX_RADIUS = 50

# creation de la classe cercle
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
#methode pour dessiner le cercle
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

# en cree une classe mygame
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
#liste de coulurs possibles
        self.colors = [
            arcade.color.RED,
            arcade.color.ORANGE,
            arcade.color.YELLOW,
            arcade.color.GREEN,
            arcade.color.BLUE,
            arcade.color.PURPLE,
            arcade.color.PINK,
            arcade.color.WHITE,
            arcade.color.FRENCH_BEIGE,
            arcade.color.GRAY,
            arcade.color.LIGHT_BLUE,
            arcade.color.VIOLET,
            arcade.color.WHEAT,
            arcade.color.TEAL,
            arcade.color.AZURE,
            arcade.color.SALMON,
            arcade.color.PEACH,
            arcade.color.OLIVE,
            arcade.color.TAN,
            arcade.color.GOLD,
            arcade.color.MAROON,
        ]
#initialisation de cette liste
        self.circle_list = []

    def setup(self):
        for i in range(20):
            color = random.choice(self.colors)
            x = random.randint(MAX_RADIUS, SCREEN_WIDTH - MAX_RADIUS)
            y = random.randint(MAX_RADIUS, SCREEN_HEIGHT - MAX_RADIUS)
            radius = random.randint(10, MAX_RADIUS)
            circle = Circle(x, y, radius, color)
            self.circle_list.append(circle)

    def on_draw(self):
        arcade.start_render()
        for circle in self.circle_list:
            circle.draw()
#pour le bouton gauche
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for circle in self.circle_list:
                if (x - circle.x) ** 2 + (y - circle.y) ** 2 <= circle.radius ** 2:
                    self.circle_list.remove(circle)
   #pour le bouton droit
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            for circle in self.circle_list:
                if (x - circle.x) ** 2 + (y - circle.y) ** 2 <= circle.radius ** 2:
                    circle.color = random.choice(self.colors)
                    break


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "20 cercles interactifs")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
