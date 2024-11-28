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


from os import sep
from random import choice
from pathlib import Path


def getPath(path:str):
    return path.replace('/', sep).replace('\\', sep)

def getFolderFiles(path:str, pattern:str='*.*', exts:list=[]):
    return [str(item) for item in Path(getPath(path)).rglob(pattern) if len(exts) == 0 or item.suffix in exts]
    # return list(map(lambda item: str(item), Path(getPath(path)).rglob(pattern)))

def getAssets(*args):
    return {k: getPath(f) for k, f in args[0].items()}

def getRandomAsset(*args):
    return choice(getFolderFiles(getPath(args[0]), args[1] if len(args) > 1 else '*.*'))
