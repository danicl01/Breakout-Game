import pygame

class Ball:
    
    def __init__(self, position_x, position_y, speed_x, speed_y, radius, colour):
        self.position = pygame.Vector2(position_x, position_y)
        self.speed = pygame.Vector2(speed_x, speed_y)
        self.radius = radius
        self.colour = colour

    def update(self, dt):
        self.position += self.speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.position.x), int(self.position.y)), self.radius)

    def check_screen_collision(self, screen_width, screen_height):
        # Checking horizontal collision
        if self.position.x <= 0:
            self.speed.x *= -1
            self.position.x = 0   # updating position for possible errors
        elif self.position.x >= screen_width-self.radius:
            self.speed.x *= -1
            self.position.x = screen_width-self.radius
        # Checking vertical collision
        if self.position.y <= 0:
            self.speed.y *= -1
            self.position.y = 0   # updating position for possible errors

    def check_player_collision(self, player_pos_x, player_pos_y):
        if self.position.x < player_pos_x+100 and self.position.x > player_pos_x:    # 100 is the value for the platform width. Will be modified in future updates
            if self.position.y >= player_pos_y-10 and self.speed.y > 0:
                self.speed.y *= -1
                return True

    def incremental(self):
        self.speed.x *= 1.1   # testing increment of speed
        self.speed.y *= 1.1

    # This function will be removed when Game class developed
    def check_lost(self, screen_height):
        if self.position.y >= screen_height - self.radius:
            self.speed = pygame.Vector2(0, 0)
            return True
        return False

            

    
    
    
    
    