import torch
import numpy as np

data = [[1,2], [1,3]]

print(data)
print(type(data))

torch_tensor = torch.tensor(data=data)
print(f'Tensor: {torch_tensor}')
print(f'Type: {type(torch_tensor)}')

np_array = np.array(data)
print(f'Numpy: {np_array}')
tensor_numpy = torch.from_numpy(np_array)

tensor_random = torch.rand((100,100), dtype=float)
print(tensor_random)