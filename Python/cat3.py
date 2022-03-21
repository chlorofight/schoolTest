import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
SPRITE_SCALING_COIN = 0.2

coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
def setup(self):
    """ Set up the game and initialize the variables. """

    # Create the sprite lists
    self.player_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()

    # Score
    self.score = 0

    # Set up the player
    # Character image from kenney.nl
    self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50 # Starting position
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    # Create the coins
    for i in range(COIN_COUNT):

        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING_COIN)

        # Position the coin
        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(SCREEN_HEIGHT)

        # Add the coin to the lists
        self.coin_list.append(coin)
def on_draw(self):
    """ Draw everything """
    arcade.start_render()
    self.coin_list.draw()
    self.player_list.draw()
def update(self, delta_time):
    # Generate a list of all coin sprites that collided with the player.
    coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

    # Loop through each colliding sprite, remove it, and add to the score.
    for coin in coins_hit_list:
        coin.kill()
        self.score += 1

