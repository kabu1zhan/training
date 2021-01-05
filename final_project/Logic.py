import Service


class GameEngine:
    """
    Описание механики игры
    """
    objects = []
    map = None
    hero = None
    level = -1
    working = True
    subscribers = set()
    score = 0.
    game_process = True
    show_help = False

    def subscribe(self, obj):
        self.subscribers.add(obj)

    def unsubscribe(self, obj):
        if obj in self.subscribers:
            self.subscribers.remove(obj)

    def notify(self, message):
        for i in self.subscribers:
            i.update(message)

    # HERO
    def add_hero(self, hero):
        self.hero = hero

    def interact(self):
        """
        Взаимодействие объектов между собой
        """
        for obj in self.objects:
            if list(obj.position) == self.hero.position:
                self.delete_object(obj)
                obj.interact(self, self.hero)

    # MOVEMENT
    def move_up(self):
        if self.map[self.hero.position[1] - 1][self.hero.position[0]] == Service.wall:
            return
        self.score -= 0.02
        self.hero.position[1] -= 1
        self.interact()

    def move_down(self):
        if self.map[self.hero.position[1] + 1][self.hero.position[0]] == Service.wall:
            return
        self.score -= 0.02
        self.hero.position[1] += 1
        self.interact()

    def move_left(self):
        if self.map[self.hero.position[1]][self.hero.position[0] - 1] == Service.wall:
            return
        self.score -= 0.02
        self.hero.position[0] -= 1
        self.interact()

    def move_right(self):
        if self.map[self.hero.position[1]][self.hero.position[0] + 1] == Service.wall:
            return
        self.score -= 0.02
        self.hero.position[0] += 1
        self.interact()

    # MAP
    def load_map(self, game_map):
        self.map = game_map

    # OBJECTS
    def add_object(self, obj):
        self.objects.append(obj)

    def add_objects(self, objects):
        self.objects.extend(objects)

    def delete_object(self, obj):
        self.objects.remove(obj)
