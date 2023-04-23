import os

def analyze_folder(folder_path):
    # 初始化总大小和已用空间大小
    total_size = 0
    used_space = 0
    folder_sizes = {}
    
    # 获取顶层文件夹下所有的文件夹
    subfolders = [os.path.join(folder_path, name) for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
    
    # 过滤出特定规则的子文件夹
    subfolders = [subfolder for subfolder in subfolders if subfolder.endswith(('apps', 'data'))]
    
    # 遍历特定规则的子文件夹中的所有文件和文件夹
    for subfolder in subfolders:
        for root, dirs, files in os.walk(subfolder):
            # 计算当前文件夹中的文件大小
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
            
            # 计算当前文件夹中已用空间的大小
            used_space += sum(os.stat(os.path.join(root, file)).st_blocks * 512 for file in files)
            folder_sizes[subfolder] = used_space
    
    # 对文件夹按照已用空间的大小进行排序
    sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
    
    # 计算百分比
    percent_used = (used_space / total_size) * 100
    
    # 输出结果
    print(f"Total Size: {total_size} bytes")
    print(f"Used Space: {used_space} bytes")
    print(f"Percent Used: {percent_used}%")
    print("Folder Sizes (in descending order):")
    for folder, size in sorted_folders:
        print(f"{folder}: {size} bytes")
