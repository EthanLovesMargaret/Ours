import os

def add_suffix_to_images(folder_path, suffix):
    # 获取images文件夹下所有文件
    for filename in os.listdir(folder_path):
        # 分离文件名和扩展名
        name, ext = os.path.splitext(filename)
        
        # 只处理图片文件（可根据需要添加更多图片格式）
        if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            # 构造新文件名
            new_name = f"{name}100{ext}"
            
            # 重命名文件
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    images_folder = "images"  # 图片文件夹路径
    suffix_to_add = "100"     # 要添加的后缀
    
    # 检查文件夹是否存在
    if os.path.exists(images_folder):
        add_suffix_to_images(images_folder, suffix_to_add)
    else:
        print(f"Error: Folder '{images_folder}' not found!")