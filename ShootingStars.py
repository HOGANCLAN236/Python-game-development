import pgzrun
import random

WIDTH = 800
HEIGHT = 600

FONT_COLOR = (255, 255, 255)
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 10
COLORS = ["blue", "green", "orange", "purple", "yellow"]

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []
Color = ""


def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))
    if game_over:
        display_message("GAME OVER", "Try again :)")
    elif game_complete:
        display_message("YOU WON :)", "Well done :D")
    else:
        for star in stars:
            star.draw()

def update():
    global stars, count
    if len(stars) == 0:
        stars = make_stars(current_level)

def make_stars(number_Of_Extra_Stars):
    colors_to_create = get_color_to_create(number_Of_Extra_Stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars


def get_color_to_create(number_Of_Extra_Stars):
    colors_to_create = ["red"]
    for i in range(0, number_Of_Extra_Stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars(colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    #Space_between_stars = WIDTH / len(new_stars)  + 1
    #Index = 0
    #for star in stars:
        #if(Index != 0):
            #stars[Index].pos = stars[Index - 1].pos + Space_between_stars
        #else:
            #stars[Index].pos += Space_between_stars

    num_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / num_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index+1) * gap_size
        star.x = new_x_pos

def animate_stars(Stars_to_animate):
    global animations
    for star in Stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        animation = animate(star,
                            duration=duration,
                            on_finished=handle_game_over,
                            y=HEIGHT)
        animations.append(animation)
        

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global stars, current_level, game_complete
    if game_complete == False:
        for star in stars:
            if star.collidepoint(pos):
                if "red" in star.image:
                    red_star_click()
                else:
                    handle_game_over()

def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        stars = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop
    
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text,
                     fontsize=60,
                     center=CENTRE,
                     color=FONT_COLOR)
    screen.draw.text(sub_heading_text,
                     fontsize=30,
                     center=(CENTRE_X, CENTRE_Y + 30),
                     color=FONT_COLOR)

pgzrun.go()





