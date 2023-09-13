import pygame
import random

x = (random.sample(range(1,100),9))


def bubble(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                swapped = True
                return j
        if not swapped: break
                
def update(arr, green):
    y = 100
    for i in range(len(arr)):
        block_rect = pygame.rect.Rect(y, 0, 50, arr[i] * 10)
        y += 60
        if i != green:
            pygame.draw.rect(screen, "white", block_rect)
        else:
            pygame.draw.rect(screen, "green", block_rect)

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

def main():
    while True:
        screen.fill("Black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        update(x, bubble(x))
        pygame.display.update()
        clock.tick(1)

        
main()
