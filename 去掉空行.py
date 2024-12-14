import os

def remove_empty_lines_in_file(file_path: str) -> None:
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # 过滤空行（strip后仍为空的行）
    filtered_lines = [line for line in lines if line.strip() != '']
    # 将过滤后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

def remove_empty_lines_in_dir(directory: str) -> None:
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                remove_empty_lines_in_file(file_path)
                print(f"已处理文件：{file_path}")

if __name__ == "__main__":
    # 将 'path_to_directory' 替换为实际的目标目录路径
    target_directory = 'story'
    remove_empty_lines_in_dir(target_directory)