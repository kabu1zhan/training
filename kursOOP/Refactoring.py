#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)

class  Vec2d():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return type(self)(self.x * k, self.y * k)

    def int_pair(self):
        return (self.x, self.y)

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __str__(self):
        return str(self.int_pair())

    def __repr__(self):
        return str(self.int_pair())

class Polyline():
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, point):
        self.points.append(Vec2d(point[0], point[1]))
        self.speeds.append(Vec2d(
            random.random() * 2,
            random.random() * 2
        ))

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)

    def get_points(self, points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(points, i * alpha))
        return res

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > self.dim[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > self.dim[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, game, display, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            points = self.get_knot()

            for p_n in range(-1, len(points) - 1):
                game.draw.line(display, color,
                               (int(points[p_n].x), int(points[p_n].y)),
                               (int(points[p_n + 1].x), int(points[p_n + 1].y)), width)

        elif style == "points":
            for p in self.points:
                game.draw.circle(display, color,
                                 (int(p.x), int(p.y)), width)

    def draw_help(game, display, steps):
        """функция отрисовки экрана справки программы"""
        display.fill((50, 50, 50))
        font1 = game.font.SysFont("courier", 24)
        font2 = game.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(steps), "Current points"])

        game.draw.lines(display, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            display.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            display.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


class Knot(Polyline):
    def __init__(self, count, dim):
        super().__init__()
        self.count = count
        self.dim = dim

    def get_count(self):
        return self.count

    def set_count(self, count):
        if count > 0:
            self.count = count

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points)-2):
            ptn = []
            ptn.append((self.points[i] + self.points[i+1])*0.5)
            ptn.append(self.points[i+1])
            ptn.append((self.points[i+1] + self.points[i+2])*0.5)
            res.extend(self.get_points(ptn))
        return res

if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    show_help = False
    pause = True
    knot = Knot(steps, SCREEN_DIM)

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
                    knot = Knot(steps)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    knot.set_count(knot.get_count()+1)
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps = knot.get_count()
                    knot.set_count(steps-1 if steps > 1 else 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                knot.add_point(event.pos)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        knot.draw_points(pygame, gameDisplay)
        knot.draw_points(pygame, gameDisplay, style="line", width=3, color=color)
        if not pause:
            knot.set_points()
        if show_help:
            Knot.draw_help(pygame, gameDisplay, knot.get_count())

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
