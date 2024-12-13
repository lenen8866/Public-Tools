import os
import shutil


# 清空指定的目录
def clear_directory(dir_path):
    try:
        # 如果目录存在
        if os.path.exists(dir_path):
            # 遍历目录中的所有文件和子目录
            for filename in os.listdir(dir_path):
                file_path = os.path.join(dir_path, filename)
                if os.path.isdir(file_path):
                    # 如果是文件夹，递归调用删除子目录
                    shutil.rmtree(file_path)
                else:
                    # 如果是文件，直接删除
                    os.remove(file_path)
            print(f"目录 '{dir_path}' 已成功清空。")
        else:
            print(f"目录 '{dir_path}' 不存在。")
    except Exception as e:
        print(f"清空目录 '{dir_path}' 时出错: {e}")


# 清空多个指定目录
def clear_multiple_directories(directories):
    for dir_path in directories:
        clear_directory(dir_path)


# 示例：你可以添加多个目录路径
directories_to_clear = [
    "story/json",#清空json
    "story/srt",#清空字幕文件


]

# 执行清空操作
clear_multiple_directories(directories_to_clear)
