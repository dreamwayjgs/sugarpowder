import sys
import os


def add_path():
    # 현재 스크립트의 경로를 가져옵니다.
    # 상위 디렉토리의 경로를 가져옵니다.
    # 상위 디렉토리를 sys.path에 추가합니다.
    current_path = os.path.dirname(os.path.abspath("__file__"))
    root_path = os.path.join(current_path, "..")
    sys.path.append(root_path)
