#!/usr/bin/python
import os
import stat

"""
r:4
w:2
x:1

stat.S_IRUSR : 拥有者 - 读权限   - 0o400 - 256
stat.S_IWUSR : 拥有者 - 写权限   - 0o200 - 128
stat.S_IXUSR : 拥有者 - 执行权限 - 0o100 - 64

stat.S_IRGRP : 组用户 - 读权限   - 0o040 - 32
stat.S_IWGRP : 组用户 - 写权限   - 0o020 - 16
stat.S_IXGRP : 组用户 - 执行权限 - 0o010 - 8

stat.S_IROTH : 其他用户 - 读权限 - 0o004 - 4
stat.S_IWOTH : 其他用户 - 写权限 - 0o002 - 2
stat.S_IXOTH : 其他用户 - 执行权 - 0o001 - 1
"""

RD, WD, XD = 4, 2, 1
BNS = [RD, WD, XD]
MDS = [
    [stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR],
    [stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP],
    [stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH],
]


def chmodPermiss(path, mode):
    if not os.path.exists(path):
        os.mkdir(path, 766)

    mode = int(mode) if not isinstance(mode, int) else mode
    if oct(os.stat(path).st_mode)[-3:] == str(mode):
        return 0

    modeNum = 0
    for mode_index, mode_slice in enumerate(str(mode)):
        for permiss_index, permiss_slice in enumerate(BNS):
            if (int(mode_slice) & permiss_slice) > 0:
                modeNum += MDS[mode_index][permiss_index]

    os.chmod(path, modeNum)
    return oct(os.stat(path).st_mode)[-3:]

