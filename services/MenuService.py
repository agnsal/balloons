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


from models.ui.Menu import Menu
from pygame_menu import Menu as PygameMenu, events, themes

from utils.confManager import scanConfig
from utils.kwargy import seedFunc
from controllers.Game import Game

class MenuService:

    quit = events.EXIT

    def __init__(self, type:str='default_menu', **kwargs):
        self.screen = kwargs['screen']
        self.clock = kwargs['clock']
        self.conf = kwargs['config']
        self.audio = kwargs['audio']
        self.logging = kwargs['logging']
        self.__makeMenu(type=type)
        self.state = {
            'level': list(self.conf['levels'].keys())[0]
        }
        self.history = {
            'victories': kwargs['victories'] if 'victories' in kwargs else {}
        }

    def __makeMenu(self, type:str):
        self.__menu = Menu(type=type, **seedFunc(PygameMenu.__init__, self.conf) |
                          {'theme': getattr(themes, self.conf['theme']) if 'theme' in self.conf else None,
                           'width': self.conf['dimensions'][0], 'height': self.conf['dimensions'][1]})
        scanConfig(self.conf, self)
        for k, item in self.conf['items'].items():
            c = getattr(self.__menu.add, item['typology'])
            c(**seedFunc(c, item))
            # self.__menu.add.button()
            # self.__menu.add.selector()
        return self

    def getMenu(self):
        return self.__menu

    def getLevels(self):
        return [(str(i), k) for i, k in enumerate(self.conf['levels'])]

    def getDefaultLevel(self):
        return 0

    def setLevel(self, item, k):
        self.state['level'] = k
        return self

    def play(self):
        g = Game(level=self.state['level'], screen=self.screen, clock=self.clock,
             config={'app': self.conf['app']} | self.conf['levels'][self.state['level']],
             audio=self.audio, logging=self.logging).run()
        if g.player.state['winner']: self.history['victories'][g.level] = g.player.state
        self.logging.info(f"Game Over: {self.state['level']} - {self.history}")
        return self




