import pygame
from PIL import Image

gif_path1 = "nerd-emoji.gif"
gif_path2 = "nerd-emoji.gif"
gif1 = Image.open(gif_path1)
gif2 = Image.open(gif_path2)
gif1.seek(0)
gif2.seek(0)
photo1 = gif1.copy()
photo2 = gif2.copy()

photo1.save("nerd-emoji1.png")
photo2.save("nerd-emoji2.png")

pygame.init()

# Set up the display
screen = pygame.display.set_mode((photo1.width + photo2.width, max(photo1.height, photo2.height)))
pygame.display.set_caption("GIF Merger")

# Load images
image1 = pygame.image.load("nerd-emoji1.png")
image2 = pygame.image.load("nerd-emoji2.png")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                print("The 'n' key was pressed")
        if event.type == pygame.QUIT:
            running = False

    # Blit images to the screen
    screen.blit(image1, (0, 0))
    screen.blit(image2, (photo1.width, 0))

    pygame.display.flip()

pygame.quit()