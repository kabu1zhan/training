import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def len(self):
        """РІРѕР·РІСЂР°С‰Р°РµС‚ РґР»РёРЅСѓ РІРµРєС‚РѕСЂР°"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def int_pair(self):
        """РІРѕР·РІСЂР°С‰Р°РµС‚ РєРѕСЂС‚РµР¶ РёР· РґРІСѓС… С†РµР»С‹С… С‡РёСЃРµР» (С‚РµРєСѓС‰РёРµ РєРѕРѕСЂРґРёРЅР°С‚С‹ РІРµРєС‚РѕСЂР°)"""
        return int(self.x), int(self.y)

    def __add__(self, other):
        """РІРѕР·РІСЂР°С‰Р°РµС‚ СЃСѓРјРјСѓ РґРІСѓС… РІРµРєС‚РѕСЂРѕРІ"""
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vec2d(new_x, new_y)

    def __sub__(self, other):
        """"РІРѕР·РІСЂР°С‰Р°РµС‚ СЂР°Р·РЅРѕСЃС‚СЊ РґРІСѓС… РІРµРєС‚РѕСЂРѕРІ"""
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vec2d(new_x, new_y)

    def __mul__(self, number):
        """РІРѕР·РІСЂР°С‰Р°РµС‚ РїСЂРѕРёР·РІРµРґРµРЅРёРµ РІРµРєС‚РѕСЂР° РЅР° С‡РёСЃР»Рѕ"""
        new_x = self.x * number
        new_y = self.y * number
        return Vec2d(new_x, new_y)


class Polyline:

    def __init__(self, points=None, speeds=None):
        if points:
            self.points = points
        else:
            self.points = []

        if speeds:
            self.speeds = speeds
        else:
            self.speeds = []

    def append_point(self, point, speed):
        """С„СѓРЅРєС†РёСЏ РґРѕР±Р°РІР»РµРЅРёСЏ С‚РѕС‡РєРё (Vec2d) c РµС‘ СЃРєРѕСЂРѕСЃС‚СЊСЋ"""
        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self):
        """С„СѓРЅРєС†РёСЏ РїРµСЂРµСЂР°СЃС‡РµС‚Р° РєРѕРѕСЂРґРёРЅР°С‚ РѕРїРѕСЂРЅС‹С… С‚РѕС‡РµРє"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p].x = - self.speeds[p].x
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p].y = - self.speeds[p].y

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """С„СѓРЅРєС†РёСЏ РѕС‚СЂРёСЃРѕРІРєРё С‚РѕС‡РµРє РЅР° СЌРєСЂР°РЅРµ"""
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.points[p_n].x), int(self.points[p_n].y)),
                                 (int(self.points[p_n + 1].x), int(self.points[p_n + 1].y)), width)
        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.x), int(p.y)), width)


class Knot(Polyline):
    def __init__(self, points, count):
        super().__init__()
        self.points = points
        self.count = count

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self.get_points(ptn, self.count))
        return res


def draw_help():
    """С„СѓРЅРєС†РёСЏ РѕС‚СЂРёСЃРѕРІРєРё СЌРєСЂР°РЅР° СЃРїСЂР°РІРєРё РїСЂРѕРіСЂР°РјРјС‹"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# РћСЃРЅРѕРІРЅР°СЏ РїСЂРѕРіСЂР°РјРјР°
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    polyline = Polyline()
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polyline = Polyline()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.append_point(Vec2d(event.pos[0], event.pos[1]),
                                      Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline.draw_points()
        knot = Knot(polyline.points, steps)
        curve = Polyline(knot.get_knot())
        curve.draw_points("line", 3, color)
        if not pause:
            polyline.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)