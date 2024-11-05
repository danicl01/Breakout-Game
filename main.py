import pygame
from ball import Ball
from player import Player

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("31 Gateway Galaxy.mp3") 
#pygame.mixer.music.play(-1) 

# Default config of the game
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
dt = 0 
font = pygame.font.SysFont('Arial', 40) 
#hit_sound = pygame.mixer.Sound("arcade-8bit-fx-159064.mp3")  

# Player and ball initialization
player =  Player(position_x=screen_width/2, position_y=700, width=100, height=20, colour="white", score= 0)
ball = Ball(position_x=screen_width / 2, position_y=screen_height / 2, speed_x=-300, speed_y=-300, radius=10, colour="white")

# Global variables (will be removed in the future)
lost = False

colours = ["#000000", "#0D1B2A", "#1B263B", "#2A3C56", "#3E5C76", "#4F6D87", 
          "#607D9B", "#788CAF", "#97A9C6", "#B8C8E6", "#DDE6F6", "#A9D6E5", 
          "#80CED6", "#60B0D4", "#5D9CBE", "#2B6C9E", "#1E4F7A", "#1A4F77", 
          "#1A6A99", "#2D7AAB", "#3298B9", "#3BB3CC", "#40C3DB", "#5ED4E8", 
          "#79E1EB", "#A2E7F5", "#D0F1F9", "#D9EAF5"]

colour_index = 0

# GAME LOPP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(colours[colour_index])

    # Ball Logic
    if lost == False:
        ball.check_screen_collision(screen_width=screen_width, screen_height=screen_height)
        if ball.check_player_collision(player_pos_x=player.position.x, player_pos_y=player.position.y):
            ball.incremental()
            player.score_increment()
            if colour_index < len(colours):
                colour_index += 1
            
        ball.update(dt=dt)
    if ball.check_lost(screen_height=screen_height):
        lost = True
    
    # Player move Logic
    keys = pygame.key.get_pressed()
  
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_left(dt)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_right(dt)
        
    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))  

    ball.draw(screen=screen)
    player.draw(screen=screen)
    screen.blit(score_text, (10, 10)) 
    pygame.display.flip()

    dt = clock.tick(60) / 1000
