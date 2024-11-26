"""
@File    : build_dmg.py
@Time    : 2024年11月26日15:24:38
@Author  : sinvon
@Desc    : 构建 .dmg 文件
"""
import subprocess
import os

# 设置工作目录
work_dir = os.path.abspath('.')
output_dir = os.path.join(work_dir, 'output')  # 修改输出目录名称
app_name = 'Pvideo-demo'
app_path = os.path.join(output_dir, f'{app_name}.app')
dmg_path = os.path.join(output_dir, f'{app_name}.dmg')

# 使用 hdiutil 创建 .dmg 文件
dmg_command = [
    'hdiutil', 'create',
    '-volname', app_name,
    '-fs', 'HFS+',
    '-srcfolder', app_path,
    '-format', 'UDBZ',
    dmg_path
]

# 执行 hdiutil 命令
subprocess.run(dmg_command, check=True)

print(f"Successfully created {dmg_path}")