import pygame
import sys
from button import Button
from pacman import run_game

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BG = pygame.transform.scale(BG, (1280, 720))  # Căn chỉnh kích thước hình nền

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    # Tạo cửa sổ game với kích thước phù hợp
    original_screen = pygame.display.get_surface()
    run_game()
    # Sau khi game kết thúc, khôi phục lại cửa sổ menu
    pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Huong dan choi Pacman", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Thêm hướng dẫn chơi
        INSTRUCTION1 = get_font(30).render("Su dung cac phim mui ten de di chuyen", True, "Black")
        INSTRUCTION1_RECT = INSTRUCTION1.get_rect(center=(640, 320))
        SCREEN.blit(INSTRUCTION1, INSTRUCTION1_RECT)
        
        INSTRUCTION2 = get_font(30).render("An cac cham trang de ghi diem", True, "Black")
        INSTRUCTION2_RECT = INSTRUCTION2.get_rect(center=(640, 360))
        SCREEN.blit(INSTRUCTION2, INSTRUCTION2_RECT)
        
        INSTRUCTION3 = get_font(30).render("An cham lon de co the an ma", True, "Black")
        INSTRUCTION3_RECT = INSTRUCTION3.get_rect(center=(640, 400))
        SCREEN.blit(INSTRUCTION3, INSTRUCTION3_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75),
                              base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))  # Vẽ hình nền
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Căn giữa văn bản
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Tạo các nút
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75),
                                base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()  # Gọi hàm play
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()