import pygame
import os

class UI:
    def __init__(self):
        self.assets = {}

    def load_assets(self):
        king_path = os.path.join("assets", "images", "white_king.svg")
        self.assets["king_white"] = pygame.image.load(king_path).convert_alpha()
    
    def draw_board(self, screen, board):
        pass