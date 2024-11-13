import pygame
from PIL import Image

def load_gif_frames(filename):
    gif = Image.open(filename)
    frames = []
    i = 0
    while True:
        frames.append(gif.copy())
        try:
            i += 1
            gif.seek(i)
        except EOFError:
            break
    return frames

gif1_frames = load_gif_frames('nerd-emoji.gif')
pygame.init()
screen = pygame.display.set_mode((gif1_frames[0].get_width(), gif1_frames[0].get_height()))
clock = pygame.time.Clock()

frame_index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(gif1_frames[frame_index], (0, 0))
    pygame.display.flip()
    
    frame_index = (frame_index + 1) % len(gif1_frames)
    clock.tick(10)  # Adjust the frame rate as needed

pygame.quit()