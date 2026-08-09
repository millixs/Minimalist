import os
from math import cos, sin
import pygame
import colorsys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 400, 400  
FPS = 60

pixel_width = 10
pixel_height = 10

screen_width = WIDTH // pixel_width
screen_height = HEIGHT // pixel_height
screen_size = screen_width * screen_height

A, B = 0, 0

theta_spacing = 10
phi_spacing = 3

chars = ".,-~:;=!*#$@"

R1 = 6
R2 = 12
K2 = 100
K1 = screen_height * K2 * 3 / (8 * (R1 + R2))

pygame.init()

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 16, bold=True)

def hsv2rgb(h, s, v):
    """Convert HSV color to RGB format for Pygame."""
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def text_display(char, x, y, color):
    """Render the text character with the given color."""
    text = font.render(str(char), True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

k = 0
paused = False
running = True
hue = 0  # Start hue for smooth color transition

while running:
    clock.tick(FPS)
    pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
    screen.fill(BLACK)

    output = [' '] * screen_size
    zbuffer = [0] * screen_size

    for theta in range(0, 628, theta_spacing):
        for phi in range(0, 628, phi_spacing):

            cosA, sinA = cos(A), sin(A)
            cosB, sinB = cos(B), sin(B)
            costheta, sintheta = cos(theta), sin(theta)
            cosphi, sinphi = cos(phi), sin(phi)

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z

            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            position = xp + screen_width * yp

            L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (
                        cosA * sintheta - costheta * sinA * sinphi)

            if 0 <= position < screen_size and ooz > zbuffer[position]:
                zbuffer[position] = ooz
                luminance_index = int(L * 8)
                output[position] = chars[luminance_index if luminance_index > 0 else 0]

    x_pixel, y_pixel, k = 0, 0, 0
    hue = (hue + 0.005) % 1  # Increment hue gradually to cycle colors smoothly

    for i in range(screen_height):
        y_pixel += pixel_height
        for j in range(screen_width):
            x_pixel += pixel_width
            text_display(output[k], x_pixel, y_pixel, hsv2rgb(hue, 1, 1))  # Color changes dynamically
            k += 1
        x_pixel = 0

    A += 0.06
    B += 0.03

    if not paused:
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                paused = not paused
