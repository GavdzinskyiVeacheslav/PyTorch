import torch
import matplotlib.pyplot as plt
tensor1 = torch.randn([2, 3])
print(tensor1)
# tensor([[-0.7306, -0.8061, 0.9215],
# [-0.1901, -1.0961, -0.4659]])
plt.imshow(torch.randn([224, 224, 3]))
# Картинка шума
tensor1.shape
# #torch.Size([2, 3])
tensor1
# tensor([[-0.7306, -0.8061, 0.9215],
#[-0.1901, -1.0961, -0.4659]])
tensor1[0, 0]
#tensor(-0.7306)
tensor1[0, 0]
#tensor(-0.1901)
tensor1[:, 1]
#tensor([-0.8061, -1.0961])
tensor1[:, 0]
#tensor([-0.7306, -0.1901])
tensor1[0, :]
#tensor([-0.7306, -0.8061, 0.9215])
torch.pow(tensor1, 2)
# tensor([[0.5337, 0.6498, 0.8492],
#[0.0361, 1.2014, 0.2171]])
torch.pow(torch.tensor(-0.7306), 2)
#tensor(0.5337)
torch.dot
torch.matmul
torch.mm
torch2 = torch.randn([3, 2])
tensor1.shape
#torch.Size([2, 3])
torch.mm(tensor1, tensor2)
#tensor([[1.0258, 0.7563],
#        [-0.4150, 2.1277])
torch.mm(tensor1, tensor2).shape
#torch.Size([2, 2])
tensor1
#tensor([[-0.7306, -0.8061, 0.9215],
#[-0.1901, -1.0961, -0.4659]])
tensor2
#tensor([[ -1.4045, -0.8648],
#       [0.4536, -1.3475],
#       [0.3965, -1.0437]])

tensor1[0, :]
#tensor([-0.7306, -0.8061, 0.9215])
tensor2[:, 0]
#tensor([-1.4045, 0.4536, 0.3965])

torch.sum(tensor1[0, :] * tensor[:, 0])
#tensor(1.0258)
