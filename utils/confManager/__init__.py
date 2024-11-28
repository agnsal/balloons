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


import config

from utils.files import getPath

def loadConfig(path:str='', logging=None):
    try:
        return config.Config(getPath(path)).as_dict()
    except Exception as e:
        if logging:
            logging.error(e)


def scanConfig(conf, cbOwner, sep:str=',', delKeys:list=[]):
    for k, v in conf.items() if isinstance(conf, dict) else enumerate(conf):
        if k in delKeys:
            del conf[k]
        else:
            if isinstance(v, str):
                s = v.split(sep)
                conf[k] = getattr(cbOwner, s[0][3:])(*s[1:len(s)]) if s[0].startswith('cn_') and hasattr(cbOwner, s[0][3:]) else getattr(cbOwner, s[0][3:]) if s[0].startswith('cb_') and hasattr(cbOwner, s[0][3:]) else v
            elif isinstance(v, dict) or isinstance(v, list):
                scanConfig(v, cbOwner, sep=sep)
    return conf

# def loadConfig(path:str='', logging=None):
#     res = {}
#     try:
#         # files = glob.glob(path + '**\\*.yml', recursive=True)
#         files = getFolderFiles(path, exts=['.yaml', '.yml'])
#         print('f', files)
#         for f in files:
#             with open(f) as cf:
#                 for k, v in {'.yml': '', '.yaml': ''}.items(): f = f.replace(k, v)
#                 print(f)
#                 res[f.split(sep)[-1]] = yaml.safe_load(cf)
#         print('res', res)
#     except Exception as e:
#         if logging:
#             logging.error(e)
#     return res




