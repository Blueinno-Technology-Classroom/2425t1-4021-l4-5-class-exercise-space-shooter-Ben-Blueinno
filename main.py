import random

import pgzrun

WIDTH = 1024
HEIGHT = 768

player = Actor("playership1_red")
player.x = WIDTH/2
player.bottom = HEIGHT
enemies = []
player_lasers = []
enemy_lasers = []

player.hp = 100


def update():
    if player.hp > 0:
        if keyboard.up:
            player.y -= 5
        if keyboard.down:
            player.y += 5
        if keyboard.left:
            player.x -= 5
        if keyboard.right:
            player.x += 5

        player.top = max(0, player.top)
        player.left = max(0, player.left)
        player.bottom = min(HEIGHT, player.bottom)
        player.right = min(WIDTH, player.right)

        if random.randint(0, 100) < 5:
            enemy = Actor("ufoblue")
            enemy.top = 25
            enemy.x = random.randint(0, WIDTH)
            enemies.append(enemy)

        if keyboard.SPACE:
            player_laser = Actor("laserred10")
            player_laser.pos = player.pos
            player_lasers.append(player_laser)

        for l in player_lasers:
            l.y -= 7
            if l.bottom < 0:
                player_lasers.remove(l)
            else:
                for e in enemies:
                    if l.colliderect(e):
                        enemies.remove(e)
                        player_lasers.remove(l)
                        break

        for e in enemies:
            if random.randint(0, 1000) < 3:
                enemy_laser = Actor("laserblue09")
                enemy_laser.pos = e.pos
                enemy_lasers.append(enemy_laser)

        for l in enemy_lasers:
            l.y += 7
            if l.top > HEIGHT:
                enemy_lasers.remove(l)
            else:
                if l.colliderect(player):
                    enemy_lasers.remove(l)
                    player.hp -= 1

        # print(len(player_lasers))


def draw():
    screen.clear()
    player.draw()
    for e in enemies:
        e.draw()
    for l in player_lasers:
        l.draw()
    for l in enemy_lasers:
        l.draw()
    screen.draw.filled_rect(Rect(0, 0, WIDTH, 20), "red")
    screen.draw.filled_rect(Rect(0, 0, WIDTH * player.hp/100, 20), "green")
    screen.draw.text(f"{player.hp} / 100", center=(WIDTH/2, 10), color='black')


pgzrun.go()
