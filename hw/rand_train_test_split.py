import random
import numpy as np

def train_test_split(x, y, test_size=0.2, random_state=42):
    random.seed(random_state)
    x = np.array(x)
    y = np.array(y)
    n = x.shape[0]
    split = int(n*(1-test_size))

    idxs = np.random.permutation(n)   
    
    test_indices = idxs[split:]
    train_indices = idxs[:split]
    
    x_train, x_test = x[train_indices], x[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    
    return x_train, x_test, y_train, y_test

# x = list(range(10))
# y = list(range(10))

# print(train_test_split(x,y))
