import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position,genero,complexion,color,level_number):
        self.canJump=False
        self.isJumping=False
        self.jump_count = 10
        self.speed=5
        self.sheet = pygame.image.load(f'img/{genero}/{complexion}/sprite{color}.png').convert_alpha()
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        self.up_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
        self.level_number=level_number
        
        if self.level_number==3:
            self.canJump=True
        else:
            self.canJump=False
    def reiniciar(self,position,genero,complexion,color):
        self.sheet = pygame.image.load(f'img/{genero}/{complexion}/sprite{color}.png').convert_alpha()
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        self.up_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
        self.speed=5
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    def changeSprite(self,genero,complexion,color,is_slow=False,tiene_alcanzame=False):
        self.sheet = pygame.image.load(f'img/{genero}/{complexion}/sprite{color}.png').convert_alpha()
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
        if complexion=="gordo":
            self.speed=3
        else:
            self.speed=5
        if is_slow:
            self.speed=2
        if tiene_alcanzame:
            self.speed=7
        # self.rect = self.image.get_rect()
    
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= self.speed
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += self.speed
        if direction == 'up':
            if not self.isJumping and self.canJump:
                self.isJumping = True
                self.jump_count = 10
                self.clip(self.up_states[0])

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_none':
            self.clip(self.up_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
    def updateEndgame(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
        if direction == 'right':
            self.clip(self.right_states)
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_none':
            self.clip(self.up_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
            
    def handle_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.update('up')
        if keys[pygame.K_LEFT]:
            self.update('left')
        if keys[pygame.K_RIGHT]:
            self.update('right')
        if hasattr(event, 'type'):
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.update('stand_none')
                if event.key == pygame.K_RIGHT:
                    self.update('stand_none')
        if self.isJumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.isJumping = False
                self.jump_count = 10
        if not self.isJumping and self.rect.y < 750 - 100:
            self.rect.y += 50
        if (self.rect.y>650):
            self.rect.y=650