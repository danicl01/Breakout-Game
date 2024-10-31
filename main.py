import pygame

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
dt = 0 

player_pos = pygame.Vector2(screen.get_width() / 2, 700)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)

ball_speed_x = 300
ball_speed_y = 300

lost = False

counter = 0

font = pygame.font.Font(None, 36) 

hit_sound = pygame.mixer.Sound("arcade-8bit-fx-159064.mp3")  

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("black")
    if ball_pos.x <= 0 or ball_pos.x >= 590:
        ball_speed_x *= -1
    if ball_pos.y <= 0 or ball_pos.y >= 790:
        ball_speed_y *= -1
        #lost = True
    if ball_pos.x < player_pos.x+100 and ball_pos.x > player_pos.x:
        if ball_pos.y >= player_pos.y and ball_speed_y > 0:
            ball_speed_y *= -1
            #hit_sound.play()
            counter += 1

    if lost == False:
        ball_pos.x += ball_speed_x * dt
        ball_pos.y += ball_speed_y * dt

    pygame.draw.circle(screen, "white", (ball_pos.x, ball_pos.y), 10)
    pygame.draw.rect(screen, "white", (player_pos.x, player_pos.y, 100, 20))

    

    keys = pygame.key.get_pressed()
  
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player_pos.x > 0:
            player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player_pos.x < 500:
            player_pos.x += 300 * dt


    score_text = font.render(f"Puntuación: {counter}", True, (255, 255, 255))  # Texto en blanco
    screen.blit(score_text, (10, 10))  # Coordenadas para colocar el texto
    pygame.display.flip()

    dt = clock.tick(60) / 1000
