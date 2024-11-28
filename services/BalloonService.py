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


from collections.abc import Iterable
import pygame

from models.Balloon import Balloon
from utils import calculus, files


class BalloonService:
    @classmethod
    def makeRandomBalloon(cls, conf:dict) -> Balloon:
        ssize = pygame.display.get_surface().get_size()
        return Balloon(**conf['sprites']['balloon'] | {'app': conf['app']} |
                            {'images': {'default': files.getRandomAsset(conf['sprites']['balloon']['images']['default'])}} |
                         {'position': (calculus.randomBtw(conf['sprites']['balloon']['dimensions'][0] * 3, ssize[0] - conf['sprites']['balloon']['dimensions'][0] * 3),
                                       ssize[1] + conf['sprites']['balloon']['dimensions'][1])
                          })

    @classmethod
    def killUpperBalloons(cls, balloons:Iterable[Balloon]={}):
        [b.kill() for b in balloons if b.rect.bottomleft[1] < 0]
        return cls

    @classmethod
    def randomMoveBalloons(cls, balloons:Iterable[Balloon]={}):
        for b in balloons: b.move(pygame.Vector2(calculus.randomBtw(-b.speed, b.speed), calculus.randomBtw(-b.speed, 0)))
        return cls
