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


from pygame import event, display, QUIT, KEYDOWN, K_ESCAPE, VIDEORESIZE

from controllers.BaseController import BaseController
from services.MenuService import MenuService


class MenuController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._menuS = MenuService(type='mainMenu', **kwargs)
        self.__initAudio().__initSprites()

    def __initAudio(self):
        self.audio['channels']['soundtracks']['soundtrack'].play(self.audio['items']['soundtracks']['menu'], -1, fade_ms=1000)
        return self

    def __initSprites(self, **kwargs):
        self.menu = self._menuS.getMenu()
        return self

    def initFrame(self):
        return self

    def processEvents(self):
        for e in event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                self.menu.close()
            elif e.type == VIDEORESIZE:
                self.menu.resize(display.get_surface().get_size())
        return self

    def update(self):
        return self

    def render(self):
        self.menu.mainloop(self.screen, disable_loop=True)
        # self.screen.blit(self.menu.image, self.menu.rect)
        # pygame.display.update()
        return self

    def getPlayer(self):
        return self._menuS.player

