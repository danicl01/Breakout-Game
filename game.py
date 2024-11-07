import pygame
from ball import Ball
from player import Player

class Game:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score = 0

        #self.background = pygame.image.load("assets/images/Ruined City Background Preview.png")

        self.player = Player(position_x=self.screen_width/2, position_y=700, width=100, height=20, colour="white")
        self.ball = Ball(position_x=self.screen_width / 2, position_y=self.screen_height / 2, speed_x=-300, speed_y=-300, radius=10, colour="white")
        self.colours = ["#000000", "#0D1B2A", "#1B263B", "#2A3C56", "#3E5C76", "#4F6D87", 
          "#607D9B", "#788CAF", "#97A9C6", "#B8C8E6", "#DDE6F6", "#A9D6E5", 
          "#80CED6", "#60B0D4", "#5D9CBE", "#2B6C9E", "#1E4F7A", "#1A4F77", 
          "#1A6A99", "#2D7AAB", "#3298B9", "#3BB3CC", "#40C3DB", "#5ED4E8", 
          "#79E1EB", "#A2E7F5", "#D0F1F9", "#D9EAF5"]
        self.colour_index = 0
        self.game_over = False
        self.font = pygame.font.SysFont('Arial', 40)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            # Player move Logic
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.player.move_left(self.dt)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.player.move_right(self.dt)
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

    def update(self):
        if not self.game_over:
            self.ball.check_screen_collision(screen_width=self.screen_width, screen_height=self.screen_height)
            if self.ball.check_player_collision(self.player.position.x, self.player.position.y):
                self.ball.incremental()
                self.score_increment()
                if self.colour_index < len(self.colours):
                    self.colour_index += 1
            self.ball.update(self.dt)
        if self.ball.check_lost(screen_height=self.screen_height):
            self.game_over = True

    def draw(self):
        self.screen.fill(self.colours[self.colour_index])
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        if self.game_over:
            game_over_text = self.font.render(f"Game Over, CLick To Restart", True, (255, 0, 0))
            self.screen.blit(game_over_text, (100, 400))

    def score_increment(self):
        self.score += 1

