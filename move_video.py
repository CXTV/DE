import os
import shutil

###找出A文件夹和B文件夹同名的子文件，并且将B文件夹下的子文件，移动到A文件的子文件夹下

# 指定视频文件夹和字幕文件夹的路径
folder_A = 'F:/Downloads/Azure Data Factory For Data Engineers - Project on Covid19'
folder_B = 'F:/Downloads/Azure Data Factory For Data Engineers - Project on Covid19/Resource/Subtitle'

# 遍历文件夹A中的所有子文件夹
for dirpath_A, dirnames_A, filenames_A in os.walk(folder_A):
    # 遍历文件夹B中的所有子文件夹
    for dirpath_B, dirnames_B, filenames_B in os.walk(folder_B):
        # 如果A和B的子文件夹同名，则将B的子文件移动到A的子文件夹下
        if os.path.basename(dirpath_A) == os.path.basename(dirpath_B):
            for filename_B in filenames_B:
                # 构造B中文件的完整路径
                path_B = os.path.join(dirpath_B, filename_B)
                # 构造A中相应文件的路径
                path_A = os.path.join(dirpath_A, filename_B)
                # 如果A中的文件不存在，则将B中的文件移动到A中
                if not os.path.isfile(path_A):
                    shutil.move(path_B, path_A)








