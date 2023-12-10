input.onButtonPressed(Button.A, function () {
    SHIP.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    BULLET = game.createSprite(SHIP.get(LedSpriteProperty.X), SHIP.get(LedSpriteProperty.Y))
    for (let index = 0; index < 4; index++) {
        BULLET.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if (ENEMY.isTouching(BULLET)) {
            ENEMY.delete()
            BULLET.delete()
            game.addScore(1)
        }
    }
    BULLET.delete()
})
input.onButtonPressed(Button.B, function () {
    SHIP.move(1)
})
let ENEMY: game.LedSprite = null
let BULLET: game.LedSprite = null
let SHIP: game.LedSprite = null
SHIP = game.createSprite(2, 4)
game.setScore(0)
basic.forever(function () {
    ENEMY = game.createSprite(randint(0, 4), 0)
    ENEMY.set(LedSpriteProperty.Brightness, 80)
    basic.pause(100)
    ENEMY.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        ENEMY.move(1)
        basic.pause(1000)
    }
    if (SHIP.isTouching(ENEMY)) {
        game.gameOver()
    } else {
        if (ENEMY.isTouchingEdge()) {
            game.gameOver()
        }
    }
})
