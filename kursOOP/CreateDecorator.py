from abc import abstractmethod, ABC
class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base


    def get_positive_effects(self):
        pass


    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass

class AbstractPositive(AbstractEffect):

    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        if type(self).__name__ in ["Berserk", "Blessing"]:
            positive_effects.append(type(self).__name__)
        return positive_effects

    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        if type(self).__name__ in ["Weakness", "EvilEye", "Curse"]:
            negative_effects.append(type(self).__name__)

        return negative_effects

class AbstractNegative(AbstractEffect):

    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        if type(self).__name__ in ["Weakness", "EvilEye", "Curse"]:
            negative_effects.append(type(self).__name__)

    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        if type(self).__name__ in ["Berserk", "Blessing"]:
            positive_effects.append(type(self).__name__)

        return positive_effects

class Berserk(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()

        params = ["Strength", "Endurance", "Agility", "Luck"]
        for param in params:
            stats[param] += 7

        params = ["Perception", "Charisma", "Intelligence"]
        for param in params:
            stats[param] -= 3

        stats['HP'] += 50

        return stats

class Blessing(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        params = ["Strength", "Endurance", "Agility", "Luck", "Perception", "Charisma", "Intelligence"]
        for param in params:
            stats[param] += 2

        return stats

class Weakness(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        params = ["Strength", "Endurance", "Agility"]
        for param in params:
            stats[param] -= 4
        return stats

class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        params = ["Strength", "Endurance", "Agility", "Luck", "Perception", "Charisma", "Intelligence"]
        for param in params:
            stats[param] -= 2
        return stats

hero = Hero()
hero.get_stats()
hero.stats
hero.get_negative_effects()
hero.get_positive_effects()

brs1 = Berserk(hero)
brs1.get_stats()
brs1.get_negative_effects()
brs1.get_positive_effects()

brs2 = Berserk(brs1)
cur1 = Curse(brs2)
cur1.get_stats()
cur1.get_positive_effects()
cur1.get_negative_effects()

cur1.base = brs1
cur1.get_stats()
cur1.get_positive_effects()
cur1.get_negative_effects()