""" 
@File    : main.py
@Time    : 2024年11月26日13:46:44
@Author  : sinvon
@Desc    : 启动主程序
"""
import os
import sys
import webview

def get_resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def start_webview():
    vue_dist_path = get_resource_path('dist')
    vue_dist_path = vue_dist_path.replace("\\", "/")
    print(f"Vue dist path: {vue_dist_path}")  # 添加调试信息
    # webview.create_window('Pvideo-demo', f'file://{vue_dist_path}/index.html',text_select=True,width=900,height=600)
    webview.create_window('Pvideo-demo','http://localhost:8080',text_select=True,width=900,height=600)
    webview.start()

if __name__ == '__main__':
    start_webview()  # 启动 WebView