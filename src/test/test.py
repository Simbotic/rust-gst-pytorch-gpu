from __future__ import print_function
import torch
x = torch.rand(5, 3)
print(x)

print("=============>")
print("Is cuda enable? {0}".format(torch.cuda.is_available()))