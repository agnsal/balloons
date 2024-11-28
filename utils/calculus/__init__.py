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


import random


def randomBtw(*args):
    return random.randint(int(args[0]), int(args[1]) + 1)

def pickOne(*args):
    return random.choices(args[0], weights=args[1], k=args[2] if len(args) > 2 else 1)[0]

# calculusMap = {
#     'randomBtw': lambda *args: random.randint(int(args[0]), int(args[1])+1),
#     'pickOne': lambda *args: random.choices(args[0], weights=args[1], k=args[2] if len(args) > 2 else 1)[0],
#     'getAsset': lambda *args: __getPath(args[0]),
#     'getRandomAsset': lambda *args: random.choice(__getFolderFiles(__getPath(args[0]), '.*\.png|.*\.jpeg')),
# }

