import numpy as np

# 定义初始四元数 (0, 0, 0, 1)
quaternion_initial = np.array([0, 0, 0, 1])

# 定义目标四元数 (-0.5, 0.5, -0.5, 0.5)
quaternion_target = np.array([-0.5, 0.5, -0.5, 0.5])

# 将四元数转换为旋转矩阵
def quaternion_to_rotation_matrix(quaternion):
    x, y, z, w = quaternion
    rotation_matrix = np.array([
        [1 - 2*y*y - 2*z*z, 2*x*y - 2*w*z, 2*x*z + 2*w*y],
        [2*x*y + 2*w*z, 1 - 2*x*x - 2*z*z, 2*y*z - 2*w*x],
        [2*x*z - 2*w*y, 2*y*z + 2*w*x, 1 - 2*x*x - 2*y*y]
    ])
    return rotation_matrix

# 计算初始四元数对应的旋转矩阵
rotation_matrix_initial = quaternion_to_rotation_matrix(quaternion_initial)

# 计算目标四元数对应的旋转矩阵
rotation_matrix_target = quaternion_to_rotation_matrix(quaternion_target)

print("初始旋转矩阵：")
print(rotation_matrix_initial)
print("目标旋转矩阵：")
print(rotation_matrix_target)
