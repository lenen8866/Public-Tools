import os


def remove_string_from_files(directory, target_string):
    """
    批量删除文本文件中的指定字符串
    :param directory: 要扫描的目录路径
    :param target_string: 要删除的目标字符串
    """
    # 遍历指定目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理 .txt 文件
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                print(f"正在处理文件: {file_path}")

                # 读取文件内容并删除目标字符串
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # 删除目标字符串
                new_content = content.replace(target_string, "")

                # 将修改后的内容写回文件
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"已删除 '{target_string}' 并更新文件: {file_path}")


if __name__ == "__main__":
    # 直接指定文件夹路径和要删除的字符串
    directory = r"story/纯文本文件"  # 替换为你的文件夹路径
    target_string = "@@@"  # 要删除的目标字符串

    # 执行字符串删除操作
    remove_string_from_files(directory, target_string)
    print("\n所有文件已处理完毕！")