"""
@File    : build_app.py
@Time    : 2024年11月26日15:24:48
@Author  : sinvon
@Desc    : 构建 .app 文件 - macOS
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
    '--windowed',  # 生成 macOS 应用程序包
    '--noconsole',
    f'--add-data={dist_dir}:dist',  # 添加 dist 目录及其内容，注意中间没有空格
    '--name', 'Pvideo-demo',  # 可执行文件名称
    '--workpath', os.path.join(work_dir, 'build'),  # 指定临时文件目录
    '--distpath', output_dir,  # 指定输出目录
    main_file  # 主入口文件
]

# 执行 PyInstaller 命令
subprocess.run(command, check=True)

print(f"Successfully created {os.path.join(output_dir, 'Pvideo-demo.app')}")