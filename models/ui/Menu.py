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


# from models.SpriteModel import SpriteModel
from pygame_menu import Menu as PygameMenu


class Menu(PygameMenu):
    def __init__(self, type:str='default', **kwargs):
        super(Menu, self).__init__(**kwargs)
        # super(Menu, self).__init__(**{k: v for k, v in kwargs.items() if k in list(inspect.signature(PygameMenu.__init__).parameters.keys())})
        self.type = type



# class Menu(SpriteModel):
#     def __init__(self, **kwargs):
#         super(Menu, self).__init__(**kwargs)

