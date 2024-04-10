import pygame
import sys
from prev_arkanoid import run_game  # Importing the run_game function from lab #8 arkanoid

# Initialize
pygame.init()

# Set screen dimensions
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ARKANOID")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 255, 255)

# Menu class
class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 52)
        self.title_font = pygame.font.Font(None, 80)
        self.menu_options = ["Start Game", "Settings", "Quit"]
        self.selected_option = 0

    def draw_menu(self):
        # Render and blit the game title
        title_text = self.title_font.render("ARKANOID", True, white)
        title_rect = title_text.get_rect(center=(screen_width // 2, 100))
        screen.blit(title_text, title_rect)

        # Render and blit menu options
        for i, option in enumerate(self.menu_options):
            text = self.font.render(option, True, cyan if i == self.selected_option else white)
            text_rect = text.get_rect(center=(screen_width // 2, 300 + i * 100))
            screen.blit(text, text_rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                elif event.key == pygame.K_RETURN:
                    if self.selected_option == 0:  # Start Game
                        run_game()  # Call the run_game function from prev_arkanoid.py
                    elif self.selected_option == 1:  # Settings
                        print("Showing Settings...")
                    elif self.selected_option == 2:  # Quit
                        pygame.quit()
                        sys.exit()

# Main function
def main():
    menu = MainMenu()

    while True:
        screen.fill(black)
        menu.draw_menu()
        menu.handle_input()
        pygame.display.flip()

main()
