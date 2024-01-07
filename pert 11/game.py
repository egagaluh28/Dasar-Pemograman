import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Lebar dan tinggi jendela
WIDTH, HEIGHT = 800, 400

# Warna
WHITE = (255, 255, 255)

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animasi Berjalan")

# Inisialisasi karakter
character = pygame.image.load("character.png")
character_rect = character.get_rect()
character_speed = 5
character_x = 0
character_y = HEIGHT // 2 - character.get_height() // 2

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # Menggerakkan karakter dari kiri ke kanan
    character_x += character_speed

    # Menggambar latar belakang
    screen.fill(WHITE)

    # Menggambar karakter
    screen.blit(character, (character_x, character_y))

    # Update tampilan
    pygame.display.flip()

    # Batasi kecepatan frame
    pygame.time.delay(30)

    # Menghentikan animasi jika karakter mencapai batas layar
    if character_x > WIDTH:
        running = False

# Keluar dari Pygame
pygame.quit()
sys.exit()
