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
import logging

from controllers.MenuController import MenuController
from utils import confManager
from utils.files import getPath


def initPygame(conf:dict):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(tuple(conf['app']['screen']['size'].values()), flags=pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.HWACCEL|pygame.RESIZABLE if conf['app']['screen']['resizable'] else None)
    pygame.display.set_caption(conf['app']['title'])
    screen.fill(conf['app']['screen']['colour'])
    logging.info('Pygame initialized.')

    pygame.mixer.init()
    audio = {
        'items': {item: conf['app']['audio'][item] | {k: pygame.mixer.Sound(getPath(p)) for k, p in conf['app']['audio'][item]['elements'].items()} for item in ['soundtracks', 'sounds']},
        'channels': {}
    }
    x = 0
    for k, v in conf['app']['audio'].items():
        audio['channels'][k] = {}
        for cn in v['channels']:
            audio['channels'][k][cn] = pygame.mixer.Channel(x)
            audio['channels'][k][cn].set_volume(conf['app']['audio'][k]['volume'])
            x += 1
    logging.debug(f"Audio initialized: {audio}")
    return screen, clock, audio

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # filename='baloon.log', filemode='a'
    conf = confManager.loadConfig(path='config/main.cfg', logging=logging)
    logging.info(f'Config loaded: {conf}')
    screen, clock, audio = initPygame(conf)
    MenuController(screen=screen, clock=clock,
                   config= {'app': conf['app'], 'levels': conf['levels']} | conf['menus']['main_menu'],
                   audio=audio, logging=logging).run()
    pygame.quit()

