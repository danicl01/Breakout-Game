import pygame
from ball import Ball
from player import Player
from game import Game

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("31 Gateway Galaxy.mp3") 
pygame.mixer.music.play(-1) 

if __name__ == "__main__":
    game = Game()
    game.run()
