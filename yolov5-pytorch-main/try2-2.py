import torch
from tqdm import tqdm
import time

a = torch.tensor([1, 2, 2, 3.], requires_grad=True)
b = torch.tensor([4, 5, 6.])
c = torch.ones_like(b)*2
print(c)


# b = out.detach()
# print(b)
#
# c = torch.where(a[1]==2, b, torch.zeros_like(a))
# print(c)





# x = torch.randint(10, (3, 3, 3, 3)).numpy()

# print("==="*30)
# print(x, x.shape)
# print("==="*30)
# a = x[..., 4]
# print("ss", a, a.shape)
# print("==="*30)
# b = x[a == 7]
# print("ssss", b, b.shape)
# print("==="*30)
#
# y = torch.randint(10, (3, 3, 3, 3)).numpy()
#
# print(y)
# print("==="*30)
# print(x[y == 4])
#

# mask = x.ge(0.5)  # 大于0.5为true
#
# print(mask)
# print(torch.masked_select(x, mask))
#
# print(x[x[..., 0]==1])
