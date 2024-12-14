import os
import json
import datetime

def replace_string_in_files(directory, extensions, target_string, replacement_string):
    """
    批量替换文件中的指定字符串，并在控制台显示每次替换的具体内容
    :param directory: 要扫描的目录路径
    :param extensions: 要处理的文件扩展名（列表或元组）
    :param target_string: 要替换的目标字符串
    :param replacement_string: 替换后的字符串
    """
    print(f"=== 处理开始: {datetime.datetime.now()} ===\n")

    # 遍历指定目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理指定扩展名的文件
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                print(f"正在处理文件: {file_path}")

                try:
                    # 判断是否为 JSON 文件
                    if file.endswith(".json"):
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = json.load(f)
                        changes_made = replace_string_in_json(content, target_string, replacement_string)

                        if changes_made:
                            with open(file_path, "w", encoding="utf-8") as f:
                                json.dump(content, f, ensure_ascii=False, indent=2)
                            print(f"✅ 已更新文件: {file_path}\n")
                        else:
                            print(f"⚠️ 未找到目标字符串 '{target_string}'\n")
                    else:
                        # 处理普通文本文件
                        with open(file_path, "r", encoding="utf-8") as f:
                            lines = f.readlines()

                        changes_made, updated_lines = replace_string_in_text(lines, target_string, replacement_string)

                        if changes_made:
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.writelines(updated_lines)
                            print(f"✅ 已更新文件: {file_path}\n")
                        else:
                            print(f"⚠️ 未找到目标字符串 '{target_string}'\n")

                except Exception as e:
                    print(f"❌ 处理文件时出错: {file_path}, 错误信息: {e}")

    print(f"=== 处理结束: {datetime.datetime.now()} ===\n")

def replace_string_in_text(lines, target_string, replacement_string):
    """
    替换文本文件中的指定字符串
    :param lines: 文本文件的行列表
    :param target_string: 要替换的目标字符串
    :param replacement_string: 替换后的字符串
    :return: (是否进行了替换, 替换后的行列表)
    """
    changes_made = False
    updated_lines = []

    for line in lines:
        if target_string in line:
            updated_line = line.replace(target_string, replacement_string)
            print(f"🔄 替换内容: \n  原文: {line.strip()}\n  修改: {updated_line.strip()}")
            updated_lines.append(updated_line)
            changes_made = True
        else:
            updated_lines.append(line)

    return changes_made, updated_lines

def replace_string_in_json(obj, target_string, replacement_string):
    """
    递归替换 JSON 对象中的指定字符串
    :param obj: JSON 对象（字典或列表）
    :param target_string: 要替换的目标字符串
    :param replacement_string: 替换后的字符串
    :return: 是否进行了替换操作
    """
    changes_made = False

    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str) and target_string in value:
                old_value = value
                obj[key] = value.replace(target_string, replacement_string)
                print(f"🔄 替换内容: \n  原文: {old_value}\n  修改: {obj[key]}")
                changes_made = True
            elif isinstance(value, (dict, list)):
                if replace_string_in_json(value, target_string, replacement_string):
                    changes_made = True

    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            if isinstance(item, str) and target_string in item:
                old_value = item
                obj[index] = item.replace(target_string, replacement_string)
                print(f"🔄 替换内容: \n  原文: {old_value}\n  修改: {obj[index]}")
                changes_made = True
            elif isinstance(item, (dict, list)):
                if replace_string_in_json(item, target_string, replacement_string):
                    changes_made = True

    return changes_made

if __name__ == "__main__":
    # 固定参数
    directory = r"story/TxTtoJson"  # 指定目录路径
    extensions = (".txt", ".json")  # 要处理的文件扩展名
    target_string = "Story_"  # 要替换的目标字符串
    replacement_string = "Story "  # 替换后的字符串

    # 执行字符串替换操作
    replace_string_in_files(directory, extensions, target_string, replacement_string)
    print("所有文件已处理完毕！")