def on_button_pressed_a():
    SHIP.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global BULLET
    BULLET = game.create_sprite(SHIP.get(LedSpriteProperty.X), SHIP.get(LedSpriteProperty.Y))
    for index in range(4):
        BULLET.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if ENEMY.is_touching(BULLET):
            ENEMY.delete()
            BULLET.delete()
            game.add_score(1)
    BULLET.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    SHIP.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

ENEMY: game.LedSprite = None
BULLET: game.LedSprite = None
SHIP: game.LedSprite = None
SHIP = game.create_sprite(2, 4)
game.set_score(0)

def on_forever():
    global ENEMY
    ENEMY = game.create_sprite(randint(0, 4), 0)
    ENEMY.set(LedSpriteProperty.BRIGHTNESS, 1000)
    basic.pause(100)
    ENEMY.turn(Direction.RIGHT, 90)
    for index2 in range(4):
        ENEMY.move(1)
        if ENEMY.is_touching(BULLET):
            ENEMY.delete()
            BULLET.delete()
            game.add_score(1)
        basic.pause(500)
    if SHIP.is_touching(ENEMY):
        game.game_over()
    else:
        if ENEMY.is_touching_edge():
            ENEMY.delete()
basic.forever(on_forever)
