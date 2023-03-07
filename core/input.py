"""Input management"""
import pygame


class Input(object):
    """Manages the users commands"""
    def __init__(self) -> None:
        """User terminated?"""
        self.quit = False
        # lists to store key states
        # down, up: discrete event; lasts for one iteration
        # pressed: continuous event, between down and up events
        self.key_down_list = []
        self.key_pressed_list = []
        self.key_up_list = []
        self.is_pressed = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        self.mouse_pos = (0, 0)
        self.mouse_pressed = False

    # functions to check key states
    def isKeyDown(self, keyCode):
        return keyCode in self.key_down_list
    def isKeyPressed(self, keyCode):
        return keyCode in self.key_pressed_list
    def isKeyUp(self, keyCode):
        return keyCode in self.key_up_list
    def getMousePosition(self):
        return self.mouse_pos    
    def isMousePressed(self, keyCode):
        return pygame.mouse.get_pressed()[0]

    def update(self):
        """Manage user input events"""
        # Reset discrete key states
        self.key_down_list = []
        self.key_up_list = []
        # Iterate to detect changes since last check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            # Check for key-down and key-up events;
            # get name of key from event and append to or remove from corresponding lists
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                self.key_down_list.append(key_name)
                self.key_pressed_list.append(key_name)
            if event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                self.key_pressed_list.remove(key_name)
                self.key_up_list.append(key_name)
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:
                    self.mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:
                    self.mouse_pressed = False
