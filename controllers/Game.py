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


import pygame
from pygame.sprite import Group
from time import time

from controllers.BaseController import BaseController
from models.Player import Player
from services.BalloonService import BalloonService
from services.GunService import GunService
from services.PlayerService import PlayerService
from utils import calculus


class Game(BaseController):
    def __init__(self, level:str, **kwargs):
        self.level = level
        self.state = kwargs['state'] if 'state' in kwargs else {'last_shoot': None}
        super().__init__(**kwargs)
        self.__initAudio()
        self.__initSprites()
        self.logging.info(f"Game {id(self)} - level {self.level} created.")

    def __initSprites(self):
        self.player = Player(**self.conf['sprites']['player'] | {'app': self.conf['app']} )
        self.balloons = Group()
        self.sprites.add(self.player)

    def __initAudio(self):
        self.audio['channels']['soundtracks']['soundtrack'].play(self.audio['items']['soundtracks']['balloons_flow'], -1, fade_ms=1000)
        self.audio['channels']['soundtracks']['ambience'].play(self.audio['items']['soundtracks']['chirping_birds'], -1)

    def initFrame(self):
        self.commands = {'movements': set(), 'shoot': False}
        if calculus.pickOne([False, True], [100 - self.conf['sprites']['balloon']['instances']['prob_x_frame'], self.conf['sprites']['balloon']['instances']['prob_x_frame']]):
            b = BalloonService.makeRandomBalloon(self.conf)
            self.balloons.add(b)
            self.sprites.add(b)
        return self

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                self.logging.info('Quitting Game...')
                break
            elif event.type == pygame.KEYDOWN:
                self.commands['shoot'] = event.key in [getattr(pygame, k) for k in self.conf['app']['keys']['shoot']]
                self.pause = not self.pause if event.key in [getattr(pygame, k) for k in self.conf['app']['keys']['pause']] else self.pause
            else: self.checkResize(event)
        keys = pygame.key.get_pressed()
        self.commands['movements'] = set([d for d, vals in self.conf['app']['keys']['movements'].items() if len(list(filter(lambda v: keys[getattr(pygame, v)], vals))) > 0])
        self.logging.debug(f"commands: {self.commands}")
        self.logging.debug(f"state: {self.state}")
        self.logging.debug(f"player state: {self.player.state}")
        return self

    def update(self):
        BalloonService.randomMoveBalloons(balloons=self.balloons)
        PlayerService.movePlayer(screen=self.screen, player=self.player, movements=self.commands['movements'])
        now = time()
        if GunService.reChargeOrStandBy(self.player, now, self.audio) and self.commands['shoot']: GunService.shoot(self.player, self.balloons, now, self.audio, self.conf['rewards'])
        self.logging.debug(f'gun magazine:{self.player.gun.magazine}')
        if PlayerService.checkGoal(self.player): self.gameOver()
        BalloonService.killUpperBalloons(self.balloons)
        return self

    def render(self):
        [self.screen.blit(s.image, s.rect) for s in self.balloons]
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.update()
        return self

    def gameOver(self):
        self.running = False
