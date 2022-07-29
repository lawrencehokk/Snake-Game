import pygame
import time
from snake import Snake
from fruit import Fruit

screen_width = 720
screen_height = 480
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.init()

snake = Snake()
fruit = Fruit(screen_width, screen_height)

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
blue = pygame.Color(0,0,255)
yellow = pygame.Color(255,255,0)
green = pygame.Color(0,255,0)
orange = pygame.Color(255,100,10)
purple = pygame.Color(240,0,255)
pink = pygame.Color(255,100,180)

score = 0

clock = pygame.time.Clock()

def show_score(self, color, font, size):
    score_font = pygame.font.SysFont(font,size) # Choose the font
    score_surface = score_font.render(f"Score: {score}", True, color) # Creates a surface for our score to go on
    score_rect = score_surface.get_rect() # Creates a rectangular object for our score
    screen.blit(score_surface,score_rect) # Displays the score on our screen

def collided():
    if snake.head[0] == fruit.location[0] and snake.head[1] == fruit.location[1]:
        global score
        score += 1
        return True
    else:
        return False

def win():
    win_font = pygame.font.SysFont("arial",50) # Choose the font
    win_surface = win_font.render(f"CONGRATULATIONS YOU WON! Your score: {score}",True, green) # Creates a surface for our game_over message
    win_rect = win_surface.get_rect() # Creates a rectangular object for our message
    win_rect.midtop = (screen_width / 2, screen_height / 4) # Displays the message in the middle of our screen
    screen.blit(win_surface, win_rect) # Displays the message on our screen
    pygame.display.flip() # Method to update our whole display
    time.sleep(5) # Add in time delay of 5 seconds before our game quits automatically
    pygame.quit() # Quits the Pygame modules
    quit() # Quits the screen

def game_over():
    gameover_font = pygame.font.SysFont("arial",50) # Choose the font
    gameover_surface = gameover_font.render(f"Your score: {score}",True, red) # Creates a surface for our game_over message
    gameover_rect = gameover_surface.get_rect() # Creates a rectangular object for our message
    gameover_rect.midtop = (screen_width / 2, screen_height / 4) # Displays the message in the middle of our screen
    screen.blit(gameover_surface, gameover_rect) # Displays the message on our screen
    pygame.display.flip() # Method to update our whole display
    time.sleep(5) # Add in time delay of 5 seconds before our game quits automatically
    pygame.quit() # Quits the Pygame modules
    quit() # Quits the screen

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                snake.change_direction = 'LEFT'
            elif event.key == pygame.K_UP:
                snake.change_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                snake.change_direction = 'DOWN'
    snake.move()

    for block in snake.body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], 10, 10))

    if snake.hit_body() == True or snake.hit_wall(screen_width, screen_height) == True:
        game_over()

    if collided():
        fruit.randomize_location(screen_width, screen_height)
        snake.add_length(True)
    else:
        snake.add_length(False)

    if score == 35:
        win()

    pygame.draw.rect(screen, pink, pygame.Rect(fruit.location[0], fruit.location[1], 10, 10))

    show_score(1, white, "arial", 25)
    pygame.display.update()
    clock.tick(10)