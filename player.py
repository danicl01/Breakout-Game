import pygame

class Player:

    def __init__(self, position_x, position_y, width, height, colour, score):
        self.position = pygame.Vector2(position_x, position_y)
        self.width = width
        self.height = height
        self.colour = colour
        self.score = score

    def update(self, dt):
        self.position += self.speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.width, self.height))

    def score_increment(self):
        self.score += 1

    def move_left(self, dt):
        if self.position.x > 0:
            self.position.x -= 300 * dt

    def move_right(self, dt):
        if self.position.x < 500:
            self.position.x += 300 * dt