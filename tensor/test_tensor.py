import torch

# unsqueeze 函数的作用是在指定的维度位置插入一个大小为1的新维度。
# 如果要在原地修改张量的维度，可以使用 unsqueeze_ 方法（注意下划线），这将会改变原始张量。
x = torch.tensor([1, 2, 3])
x_new = x.unsqueeze(0)

y = torch.tensor([4, 5, 6])  # torch.Size([1, 3])
y_new = y.unsqueeze(1) # torch.Size([3, 1])
y_new_new = y_new.squeeze(0)


print(y_new_new.shape)