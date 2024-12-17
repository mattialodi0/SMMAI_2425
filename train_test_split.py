import random

def train_test_split(x, split_rate=0.8):
    n = len(x)
    random.shuffle(x)
    split = int(split_rate*n)
    y = x[split:]
    x = x[:split]

    return x, y

x = list(range(10))
x, y = train_test_split(x)
print(x)
print(y)
