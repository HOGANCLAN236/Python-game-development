import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

ship = Actor('galaga')
bug = Actor('bug')

ship.pos = (
  WIDTH // 2, HEIGHT - 60
)  #// gives an integer value, instead of / that gives a float value -> ex. 600.0
speed = 5

Game_over = False

#define list of bullets and enemies
bullets = []
enemies = []
#enemies.append(Actor('bug'))

#enemies[-1].x = 10
#enemies[-1].y = -100

score = 0

direction = 1
ship.countdown = 90

for x in range(8):
  for y in range(4):
    enemies.append(Actor('bug'))
    enemies[-1].x = 100 + 50 * x
    enemies[-1].y = 80 + 50 * y


def display_Score():
  screen.draw.text(str(score), (50, 30))


def on_key_down(key):
  if key == keys.SPACE:
    bullets.append(Actor('bullet'))
    bullets[-1].x = ship.x
    bullets[-1].y = ship.y - 50


def update():
  global score, Game_over, direction
  moveDown = False
  if keyboard.a:
    ship.x -= speed
    if ship.x <= 0:
      ship.x = 0
  elif keyboard.d:
    ship.x += speed
    if ship.x >= WIDTH:
      ship.x = WIDTH

  #if Game_over == False and enemies == []:
  #        enemies.append(bug)
  #        bug.move_ip(random.randint(50, WIDTH-50), -100)

  for bullet in bullets:
    if bullet.y <= 0:
      bullets.remove(bullet)
    else:
      bullet.y -= 10

  #if len(enemies) == 0:
  #    handle_game_over()

  if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 80):
    moveDown = True
    direction = direction * -1

  for enemy in enemies:
    enemy.x += 4 * direction
    if moveDown == True:
      enemy.y += 100
    if enemy.y > HEIGHT:
      enemies.remove(enemy)

    if enemy.colliderect(ship):
      #handle_game_over()
      for enemy in enemies:
        enemies.remove(enemy)
    if enemy.y >= HEIGHT:
      enemy.y = -100
      enemy.x = random.randint(50, WIDTH - 50)
    for bullet in bullets:
      if enemy.colliderect(bullet):
        score += 100
        enemies.remove(enemy)
        bullets.remove(bullet)
        if len(enemies) == 0:
          handle_game_over()


def draw():
  global score
  screen.clear()
  screen.fill(BLUE)
  for bullet in bullets:
    bullet.draw()
  for enemy in enemies:
    enemy.draw()
  ship.draw()
  if Game_over:
    screen.fill('black')
    screen.draw.text('Game Over', (500, 300), fontsize=60)
    screen.draw.text('Final Score: {}'.format(score), (550, 350), fontsize=30)

  if Game_over == False:
    display_Score()


def handle_game_over():
  global Game_over
  Game_over = True


pgzrun.go()