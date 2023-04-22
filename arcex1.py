#je importe 2 librairies python, arcade et random
import arcade
import random

# Je definis les dimensions pour le cadre/ la fenetre
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Je definis le rayon maximum pour les cercles
MAX_RADIUS = 50

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        #je cree une liste de coulurs possibles pour les cercles
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

        # Initialisation de la liste de cercles
        self.circle_list = []

        # Ajout de 20 cercles a la liste
        for i in range(20):
            # je choisis une couleur aleatoire
            color = random.choice(self.colors)

            # je choisi une position aleatoire
            x = random.randint(MAX_RADIUS, SCREEN_WIDTH - MAX_RADIUS)
            y = random.randint(MAX_RADIUS, SCREEN_HEIGHT - MAX_RADIUS)

            # je choisis un rayon aleatoire
            radius = random.randint(10, MAX_RADIUS)

            # j'ajoute le cercle a la liste
            self.circle_list.append((x, y, radius, color))

    def on_draw(self):
        arcade.start_render()

        # pour dessiner chaque cercle dans la liste
        for x, y, radius, color in self.circle_list:
            arcade.draw_circle_filled(x, y, radius, color)

    def run(self):
        arcade.run()

# Créer une instance de la classe de jeu et commencer la boucle #1

MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "20 cercles de couleurs différentes").run()
