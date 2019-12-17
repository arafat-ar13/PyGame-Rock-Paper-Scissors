import pygame
import random
import time

from winner_decider import decide_winner
from button import Button

pygame.init()

# Setting up the game display resolution
screen_res = (420, 420)
win = pygame.display.set_mode(screen_res)

# Setting up the hands
hand_x = 170
hand_y = 260
hand_width = 80
hand_height = 150

computer_x = 175
computer_y = 0


class StartPage():
    def __init__(self, player_hand_coords, computer_hand_coords, hands_res, win):
        self.hand_x, self.hand_y = player_hand_coords
        self.computer_x, self.computer_y = computer_hand_coords
        self.hand_width, self.hand_height = hands_res
        self.win = win

        quit_game = False
        while not quit_game:
            start_button = Button((0, 255, 0), 90, 160, 250, 50, "Start game")
            start_button.draw(self.win, (0, 0, 255))

            instructions_button = Button(
                (255, 0, 255), 90, 210, 250, 50, "How to play")
            instructions_button.draw(self.win, (0, 0, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.isOver(pygame.mouse.get_pos()):
                        self.start_game()
                    if instructions_button.isOver(pygame.mouse.get_pos()):
                        self.go_to_inst_page()

            pygame.display.update()

    def start_game(self):
        return GamePage((self.hand_x, self.hand_y), (self.computer_x, self.computer_y), (self.hand_width, self.hand_height), self.win).start_game()

    def go_to_inst_page(self):
        return HowToPlay(self.win, (self.hand_width, self.hand_height))


class HowToPlay():
    def __init__(self, win, hands_res):
        self.win = win
        self.res = (hands_res[0]-20, hands_res[1]-20)

        self.on_this_page = True
        while self.on_this_page:
            self.win.fill((0, 0, 0))

            self.hand = pygame.image.load("Game Pictures/hand.png")
            self.hand = pygame.transform.scale(self.hand, self.res)
            self.rock = pygame.image.load("Game Pictures/rock.png")
            self.rock = pygame.transform.scale(self.rock, self.res)
            self.scissors = pygame.image.load("Game Pictures/scissors.png")
            self.scissors = pygame.transform.scale(self.scissors, self.res)

            self.win.blit(self.scissors, (50, 50))
            self.win.blit(self.rock, (180, 50))
            self.win.blit(self.hand, (300, 50))

            self.left_click = pygame.image.load("Game Pictures/left_click.png")
            self.left_click = pygame.transform.scale(
                self.left_click, (self.res[0]+35, self.res[1]))
            self.middle_click = pygame.image.load("Game Pictures/middle_click.png")
            self.middle_click = pygame.transform.scale(
                self.middle_click, (self.res[0]+20, self.res[1]))
            self.right_click = pygame.image.load("Game Pictures/right_click.png")
            self.right_click = pygame.transform.scale(
                self.right_click, (self.res[0]+30, self.res[1]))

            self.win.blit(self.left_click, (40, 220))
            self.win.blit(self.middle_click, (165, 220))
            self.win.blit(self.right_click, (285, 220))

            self.back_button = Button(
                (230, 185, 200), 80, 365, 250, 50, "Go back")
            self.back_button.draw(self.win, (0, 0, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.isOver(pygame.mouse.get_pos()):
                        self.win.fill((0, 0, 0))
                        self.on_this_page = False

            pygame.display.update()


class GamePage():
    def __init__(self, player_hand_coords, computer_hand_coords, hands_res, window):
        self.hand_x, self.hand_y = player_hand_coords
        self.computer_x, self.computer_y = computer_hand_coords
        self.hand_width, self.hand_height = hands_res
        self.win = window

    def start_game(self):

        my_hand = pygame.image.load("Game Pictures/rock.png")
        my_hand = pygame.transform.scale(
            my_hand, (self.hand_width, self.hand_height))

        computer_hand = pygame.image.load("Game Pictures/rock.png")
        computer_hand = pygame.transform.scale(
            my_hand, (self.hand_width, self.hand_height))
        computer_hand = pygame.transform.rotate(computer_hand, 180)

        rock_hand = pygame.image.load("Game Pictures/rock.png")
        rock_hand = pygame.transform.scale(
            rock_hand, (self.hand_width, self.hand_height))
        scissors_hand = pygame.image.load("Game Pictures/scissors.png")
        scissors_hand = pygame.transform.scale(
            scissors_hand, (self.hand_width, self.hand_height))
        hand_hand = pygame.image.load("Game Pictures/hand.png")
        hand_hand = pygame.transform.scale(
            hand_hand, (self.hand_width, self.hand_height))

        options = [rock_hand, scissors_hand, hand_hand]

        game = True
        while game:
            start_game = False
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # Getting mouse button states
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start_game = True
                    if pygame.mouse.get_pressed()[0]:
                        my_hand = scissors_hand
                        my_hand_name = "scissors"
                    elif pygame.mouse.get_pressed()[1]:
                        my_hand = rock_hand
                        my_hand_name = "rock"
                    elif pygame.mouse.get_pressed()[2]:
                        my_hand = hand_hand
                        my_hand_name = "hand"
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    game = False

            # Giving the ability to move the mouse
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and self.hand_x < 340:
                self.hand_x += 15
                self.computer_x += 15
            elif keys[pygame.K_LEFT] and self.hand_x > 0:
                self.hand_x -= 15
                self.computer_x -= 15
            elif keys[pygame.K_UP] and self.hand_y > 209:
                self.hand_y -= 15
                self.computer_y += 15
            elif keys[pygame.K_DOWN] and self.hand_y < 270:
                self.hand_y += 15
                self.computer_y -= 15

            # Filling the background with black to avoid error
            self.win.fill((0, 0, 0))

            # Displaying the hand on the screen
            self.win.blit(my_hand, (self.hand_x, self.hand_y))

            # Displaying the computer hand
            self.win.blit(computer_hand, (self.computer_x, self.computer_y))

            # A mouse press starts the game
            if start_game:
                self.hand_x = 170
                self.hand_y = 260

                computer_hand = random.choice(options)
                if computer_hand == rock_hand:
                    computer_hand_name = "rock"
                elif computer_hand == scissors_hand:
                    computer_hand_name = "scissors"
                else:
                    computer_hand_name = "hand"
                computer_hand = pygame.transform.rotate(computer_hand, 180)

                self.win.blit(
                    computer_hand, (self.computer_x, self.computer_y))

                self.computer_x = 175
                self.computer_y = 0

                winner, color = decide_winner(my_hand_name, computer_hand_name)
                if color != (0, 0, 255):
                    winner_text = f"The winner is {winner}"
                else:
                    winner_text = "It is a freakin' DRAW!!!!!"

                # Showing up a message to display the winner
                font = pygame.font.Font("freesansbold.ttf", 35)
                text = font.render(winner_text, True, color, (0, 0, 128))
                textRect = text.get_rect()

                self.win.blit(text, (-2, 180))
                pygame.display.update()
                time.sleep(1)

            pygame.display.update()

        self.win.fill((0, 0, 0))


class MyGame():
    def run(self):
        return StartPage((hand_x, hand_y), (computer_x, computer_y), (hand_width, hand_height), win)


if __name__ == "__main__":
    MyGame().run()
    pygame.quit()
