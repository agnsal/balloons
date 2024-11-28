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


from abc import abstractmethod

from pygame import display, VIDEORESIZE, RESIZABLE, HWSURFACE, HWACCEL, DOUBLEBUF
from pygame.sprite import Group


class BaseController:
    def __init__(self, **kwargs):
        self.running = True
        self.pause = False
        self.conf = kwargs['config']
        self.logging = kwargs['logging']
        self.screen = kwargs['screen']
        self.clock = kwargs['clock']
        self.audio = kwargs['audio']
        self.fps = self.conf['app']['frames_per_second']
        self.sprites = Group()

    @abstractmethod
    def __initSprites(self):
        pass

    @abstractmethod
    def __initAudio(self):
        pass

    @abstractmethod
    def initFrame(self):
        pass

    @abstractmethod
    def processEvents(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    def run(self):
        self.logging.debug('Running...')
        while self.running:
            while self.pause:
                self.processEvents()
            if 'screen' in self.conf and 'colour' in self.conf['screen']: self.screen.fill(self.conf['screen']['colour'])
            self.initFrame().processEvents().update().render()
            self.clock.tick(self.fps)
        return self

    def checkResize(self, event):
        if event.type == VIDEORESIZE:
            for s in self.sprites: s.changeImage(s.currImg)
            self.screen = display.set_mode((event.w, event.h), HWACCEL|HWSURFACE|DOUBLEBUF|RESIZABLE)
        return self

