import os
import numpy as np
import pickle

root_dir = '/home/u2022141214/mtrcnet_20240918/MTRCNet-CL/cholec'   # TODO 20240710 改为实际路径
img_dir = os.path.join(root_dir, 'data_resize')    # 图片数据
tool_dir = os.path.join(root_dir, 'tool_annotations')  # 每个图片上使用到的手术工具标注
phase_dir = os.path.join(root_dir, 'phase_annotations')  # 每个图片对应手术动作的标注

print(root_dir)
print(img_dir)
print(tool_dir)
print(phase_dir)


def get_dirs(root_dir):
    file_paths = []
    file_names = []
    for lists in os.listdir(root_dir):
        path = os.path.join(root_dir, lists)
        if os.path.isdir(path):
            file_paths.append(path)
            file_names.append(os.path.basename(path))
    file_names.sort()
    file_paths.sort()
    return file_names, file_paths

def get_files(root_dir):
    file_paths = []
    file_names = []
    for lists in os.listdir(root_dir):
        path = os.path.join(root_dir, lists)
        if not os.path.isdir(path):
            file_paths.append(path)
            file_names.append(os.path.basename(path))
    file_names.sort()
    file_paths.sort()
    return file_names, file_paths


img_dir_names, img_dir_paths = get_dirs(img_dir)
tool_file_names, tool_file_paths = get_files(tool_dir)
phase_file_names, phase_file_paths = get_files(phase_dir)

phase_dict = {}
phase_dict_key = ['Preparation', 'CalotTriangleDissection', 'ClippingCutting', 'GallbladderDissection',
                  'GallbladderPackaging', 'CleaningCoagulation', 'GallbladderRetraction']
# 7个手术阶段构建了一个字典, value为0到6
for i in range(len(phase_dict_key)):
    phase_dict[phase_dict_key[i]] = i
print(phase_dict)

# for i in range(1):
#     img_file_names, img_file_paths = get_files(img_dir_paths[i])
#     print(len(img_file_names))
#     print(len(img_file_paths))
#     # print(img_file_names[:10])
#     # print(img_file_paths[:10])

all_info_all = [] # 长度等于视频数, [img_file_each_path, 手术工具1,..手术工具l], [img_file_each_path, 手术工具1,..手术工具l, 手术动作]

for j in range(len(tool_file_names)):
    last_tool_index = ''
    last_phase_index = ''
    tool_file = open(tool_file_paths[j])
    phase_file = open(phase_file_paths[j])
    tool_count = 0
    phase_count = 0
    info_all = []
    for tool_line in tool_file:
        tool_count += 1
        if tool_count > 1:
            tool_split = tool_line.split()
            info_each = []
            img_file_each_path = os.path.join(img_dir_paths[j], img_dir_names[j] + '-' + str(tool_count - 1) + '.png') # TODO 原模型用的jpg格式, 测试数据时png, 这里需要结合实际使用情况来看
            info_each.append(img_file_each_path)
            for l in range(1, len(tool_split)):
                info_each.append(int(tool_split[l]))
                last_tool_index = tool_split[0]
            info_all.append(info_each)
    for phase_line in phase_file:
        phase_count += 1    # 手术动作的行数
        # TODO 20240710 原数据是每秒25张, 每秒肯定是一个手术动作, 所以对应的phase都是一个, 但测试数据连续的只有3张图, 所以这里25要改成3, 当跑原数据时需要改回来.
        if phase_count % 25 == 2 and (phase_count // 25) < len(info_all):  # 每秒25张, 每秒肯定是一个手术动作, 
        # if phase_count % 3 == 2 and (phase_count // 3) < len(info_all):  # 每秒25张, 每秒肯定是一个手术动作, 
            phase_split = phase_line.split()
            # for m in range(len(phase_split)):
            # TODO 20240710 同上面25改3
            info_all[phase_count // 25].append(phase_dict[phase_split[1]])  #  添加手术动作
            # info_all[phase_count // 3].append(phase_dict[phase_split[1]])  #  添加手术动作
            last_phase_index = phase_split[0]   # frame标识
    print('the{:4d}th tool: {:6d} index_error{:2d}'.format(j, tool_count - 1,
                                                           int(last_tool_index) - int(last_phase_index)))

    # print(len(info_all))
    all_info_all.append(info_all)

# for k in range(10):
# print(all_info_all[0][k])
with open('cholec80.pkl', 'wb') as f:
    pickle.dump(all_info_all, f)

import pickle

with open('cholec80.pkl', 'rb') as f:
    all_info = pickle.load(f)

train_file_paths = []
test_file_paths = []
val_file_paths = []
val_labels = []
train_labels = []
test_labels = []

train_num_each = []
val_num_each = []
test_num_each = []

for i in range(0, 6):   # TODO 20240710 只有5个文件, 仅跑通把5个文件都用了
# for i in range(32):   # 前32个视频图像做训练集
    train_num_each.append(len(all_info[i]))
    for j in range(len(all_info[i])):
        train_file_paths.append(all_info[i][j][0])
        train_labels.append(all_info[i][j][1:])

print(len(train_file_paths))
print(len(train_labels))

for i in range(6, 8):   # TODO 20240710 只有5个文件, 仅跑通把5个文件都用了
# for i in range(32, 40):   # 中间8个视频图像做验证集
    val_num_each.append(len(all_info[i]))
    for j in range(len(all_info[i])):
        val_file_paths.append(all_info[i][j][0])
        val_labels.append(all_info[i][j][1:])

print(len(val_file_paths))
print(len(val_labels))

for i in range(8, 10):   # TODO 20240710 只有5个文件, 仅跑通把5个文件都用了
# for i in range(40, 80):  # 后40个视频图像做测试集
    test_num_each.append(len(all_info[i]))
    for j in range(len(all_info[i])):
        test_file_paths.append(all_info[i][j][0])
        test_labels.append(all_info[i][j][1:])

print(len(test_file_paths))
print(len(test_labels))

# for i in range(10):
#     print(train_file_paths[i], train_labels[i])
#     print(test_file_paths[i], test_labels[i])

train_val_test_paths_labels = []
train_val_test_paths_labels.append(train_file_paths)
train_val_test_paths_labels.append(val_file_paths)
train_val_test_paths_labels.append(test_file_paths)

train_val_test_paths_labels.append(train_labels)
train_val_test_paths_labels.append(val_labels)
train_val_test_paths_labels.append(test_labels)

train_val_test_paths_labels.append(train_num_each)
train_val_test_paths_labels.append(val_num_each)
train_val_test_paths_labels.append(test_num_each)

with open('train_val_test_paths_labels.pkl', 'wb') as f:
    pickle.dump(train_val_test_paths_labels, f)


print('Done')
print()

