

class Characters:
    images = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.animation_count = 0

        self.img = None
        self.rectangle = None

    def draw_sprite(self, screen, images, speed):
        """Creating rect for sprite"""
        self.animation_count += speed
        if self.animation_count >= len(images):
            self.animation_count = 0
        self.img = images[int(self.animation_count)]

        self.rectangle = self.get_rect((self.x, self.y))
        screen.blit(self.img, (self.x, self.y))

    def get_rect(self, pos):
        return self.img.get_rect(topleft=pos)
