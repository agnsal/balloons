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
from pygame import Vector2

from utils.files import getAssets


class SpriteModel(pygame.sprite.Sprite):

    def __init__(self, type:str='standard', **kwargs):
        super().__init__()
        self.type = type
        self.screen = pygame.display.get_surface()
        self.speed = kwargs['speed'] if 'speed' in kwargs else 10
        self.images = {k: pygame.image.load(a).convert_alpha() for k, a in getAssets(kwargs['images']).items()}
        self.pDims = Vector2(*kwargs['dimensions'])
        self.dCenter = pygame.Vector2(tuple(kwargs['position']) if 'position' in kwargs else (0, 0))
        self.currImg = 'default'
        self.changeImage(self.currImg)
        # self.rect = self.image.get_rect()
        # self.rect.center = pygame.Vector2(tuple(kwargs['position']) if 'position' in kwargs else (0, 0))

    def move(self, vect):
        self.rect.move_ip(vect)
        return self

    def changeImage(self, imgName:str):
        wsize = self.screen.get_size()[0]
        # self.image = pygame.transform.scale(self.images[imgName], (wsize * self.pDims[0] / 100, wsize * self.pDims[1] / 100))
        c = self.rect.center if hasattr(self, 'rect') else self.dCenter
        self.image = pygame.transform.scale(self.images[imgName], self.pDims * wsize / 100)
        self.rect = self.image.get_rect()
        self.rect.center = c
        self.currImg = imgName
        return self



    # def __scanArgs(self, args, sep:str='.'):
    #     for k, v in args.items() if isinstance(args, dict) else enumerate(args):
    #         if isinstance(v, str):
    #             s = v.split(sep)
    #             print('S:', v, s, s[0], s[0] in calculusMap)
    #             if s[0] in calculusMap:
    #                 args[k] = calculusMap[s[0]](*s[1:len(s)])
    #         elif isinstance(v, Iterable):
    #             self.__scanArgs(v, sep=sep)
    #     return args


