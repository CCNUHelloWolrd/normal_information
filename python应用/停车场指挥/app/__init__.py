# -*- coding: utf-8 -*-
# __init__.py
# date: 2025.6.25

"""本文件为库说明文件

实现小游戏：挪车
游玩规则：双击小车，小车会前进直到遇到障碍物或者走出停车场，
        单击道具，再次单击小车，小车的前进方向会发生变化
        当所有小车移出界面后，游戏胜利
使用方式：导入本库, 使用函数start()
其他说明：如需修改游戏或素材，请修改对应代码

所有SAVE_DATA相关内容为游戏备份接口
"""

__version__ = "1.0.0"
__author__ = 'zrk'
__all__ = ["start"]

from .main import start
import os

WORK_PATH = os.getcwd() + "/app"
print(f"当前地址为：{WORK_PATH}")
