""" 
@File    : build_exe.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 构建 .exe 文件 - Windows
"""
import subprocess
import os

# 设置工作目录
work_dir = os.path.abspath('.')
output_dir = os.path.join(work_dir, 'output')  # 修改输出目录名称
main_file = os.path.join(work_dir, 'src', 'main.py')
dist_dir = os.path.join(work_dir, 'dist')  # 前端项目 dist 目录

command = [
    'pyinstaller',
    '--onefile', 
    '--noconsole',
    f'--add-data={dist_dir};dist',  # 添加 dist 目录及其内容
    '--name', 'Pvideo-demo',  # 可执行文件名称
    '--workpath', os.path.join(work_dir, 'build'),  # 指定临时文件目录
    '--distpath', output_dir,  # 指定输出目录
    main_file  # 主入口文件
]

# 执行 PyInstaller 命令
subprocess.run(command)

print(f"Successfully created {os.path.join(output_dir, 'Pvideo-demo.exe')}")
