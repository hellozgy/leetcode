import torch
import numpy as np

def dropout(src, p=0, training=False):
    assert 0<=p<=1
    if training:
        shape = src.shape
        print(shape)
        a=1
        for d in shape:
            a *= d
        print(a)
        mask = np.random.choice(a, int(a*p))
        mask = [0 if i in mask else 1 for i in range(a)]
        src = src*torch.Tensor(mask).view(shape)
    else:
        if p>0:
            src = src / p
    return src

t = torch.randn(2,3)
print(t)
print(dropout(t, 0.5, True))
print(dropout(t, 0.5, False))