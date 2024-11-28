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

class GunService:
    @classmethod
    def recharge(cls, player):
        player.gun.magazine = player.gun.magazineTot
        player.changeImage('default')
        return cls

    @classmethod
    def standby(cls, player):
        player.changeImage('recharging')
        return cls

    @classmethod
    def reChargeOrStandBy(cls, player, timestamp, audio) -> bool:
        canShoot = True
        if player.gun.magazine == 0:
            if player.gun.lastShoot is None or timestamp - player.gun.lastShoot > player.gun.rechargeT:
                cls.recharge(player)
                audio['channels']['sounds']['gun'].play(audio['items']['sounds']['pack'])
            else:
                cls.standby(player)
                canShoot = False
        return canShoot

    @classmethod
    def shoot(cls, player, balloons, timestamp, audio, rewards:dict={}):
        player.gun.magazine -= 1
        audio['channels']['sounds']['shoot'].play(audio['items']['sounds']['shoot'])
        collidables = pygame.sprite.spritecollide(player, balloons, False)
        for b in collidables:
            if b.rect.collidepoint(player.rect.center):
                audio['channels']['sounds']['balloons'].play(audio['items']['sounds']['balloon_pop'])
                for item in rewards['balloon'][b.type]: player.state[item[0]] += item[1]
                b.kill()
        # self.state['last_shoot'] = now if self.commands['shoot'] else self.state['last_shoot']
        if player.gun.magazine == 0:
            audio['channels']['sounds']['gun'].play(audio['items']['sounds']['unpack'])
        player.gun.lastShoot = timestamp
        # self.player.changeImage('recharging')
        return cls