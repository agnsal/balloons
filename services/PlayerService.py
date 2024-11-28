'''
Copyright 2024 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''


from sympy import sympify

from models.Player import Player
import pygame


class PlayerService:
    @classmethod
    def movePlayer(cls, screen, player:Player, movements:list=[]):
        dx, dy = 0, 0
        if 'right' in movements:
            dx += player.speed
        elif 'left' in movements:
            dx -= player.speed
        elif 'down' in movements:
            dy += player.speed
        elif 'up' in movements:
            dy -= player.speed
        player.move(pygame.Vector2(dx, dy))
        player.rect.clamp_ip(screen.get_rect())
        return cls

    @classmethod
    def checkGoal(cls, player:Player) -> bool:
        for row in player.goal:
            for c in row:
                x = c.split(',')
                if not sympify(f"{player.state[x[0]]}{x[1]}"):
                    return False
        player.state['winner'] = True
        return True


