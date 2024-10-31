import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("31 Gateway Galaxy.mp3") 
pygame.mixer.music.play(-1) 

screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
dt = 0 

player_pos = pygame.Vector2(screen.get_width() / 2, 700)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)

ball_speed_x = -300
ball_speed_y = -300

lost = False

counter = 0
flag = 0

colors = [
    "#000000",  # Negro
    "#0D1B2A",  # Azul muy oscuro
    "#1B263B",  # Azul marino oscuro
    "#2A3C56",  # Azul profundo
    "#3E5C76",  # Azul acero
    "#4F6D87",  # Azul grisáceo
    "#607D9B",  # Azul medio
    "#788CAF",  # Azul suave
    "#97A9C6",  # Azul claro
    "#B8C8E6",  # Azul muy claro
    "#DDE6F6",  # Azul casi blanco
    "#A9D6E5",  # Azul suave claro
    "#80CED6",  # Aqua suave
    "#60B0D4",  # Azul claro
    "#5D9CBE",  # Azul pálido
    "#2B6C9E",  # Azul oscuro suave
    "#1E4F7A",  # Azul medianoche
    "#1A4F77",  # Azul oscuro
    "#1A6A99",  # Azul pálido suave
    "#2D7AAB",  # Azul cielo
    "#3298B9",  # Cian oscuro
    "#3BB3CC",  # Cian
    "#40C3DB",  # Aqua
    "#5ED4E8",  # Cian claro
    "#79E1EB",  # Cian muy claro
    "#A2E7F5",  # Cian suave
    "#D0F1F9",  # Cian casi blanco
    "#D9EAF5"   # Cian suave pálido
]

color_index = 0

font = pygame.font.Font(None, 36) 

hit_sound = pygame.mixer.Sound("arcade-8bit-fx-159064.mp3")  

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(colors[color_index])
    if ball_pos.x <= 0:  
        ball_speed_x *= -1
        ball_pos.x = 0  
    elif ball_pos.x >= 590:  
        ball_speed_x *= -1
        ball_pos.x = 590  

    if ball_pos.y <= 0: 
        ball_speed_y *= -1
        ball_pos.y = 0  
    elif ball_pos.y >= 790: 
        lost = True 
        ball_speed_y = 0
        ball_speed_x = 0
        ball_pos.y = 790 
 

        #lost = True
    if ball_pos.x < player_pos.x+100 and ball_pos.x > player_pos.x:
        if ball_pos.y >= player_pos.y and ball_speed_y > 0:
            ball_speed_y *= -1
            #hit_sound.play()
            counter += 1
            flag += 1

    if flag == 2:
        if color_index < len(colors):
            color_index += 1
        flag = 0
        ball_speed_x *= 1.1
        ball_speed_y *= 1.1
        

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
