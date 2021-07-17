import random
import pygame
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


# Inheritance
class BlueBlob(Blob):
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(
            color, x_boundary, y_boundary
        )  #Even though the parent class sets the user inputed color as self.color we can change it in child class
        self.color = BLUE


def draw_environment(blobs_list):
    game_display.fill(WHITE)
    for blob_dict in blobs_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y],
                               blob.size)
            blob.move()
    pygame.display.update()


def main():
    blue_blobs = dict(
        enumerate([
            BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)
        ]))
    red_blobs = dict(
        enumerate(
            [BlueBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)


if __name__ == "__main__":
    main()
