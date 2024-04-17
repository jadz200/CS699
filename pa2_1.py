import random
import z3
from pa1Pytorch import my_symbolic_execution
from pa2Pytorch import my_interval_execution
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
def relu_activation(temp): return temp if temp > 0 else 0

def create_random(size):
    class RandomModel(nn.Module):
        def __init__(self):
            super().__init__()
            for i in range(len(size) - 1):
                if i!=len(size)-2:
                    setattr(self, f"layer{i}", nn.Linear(size[i], size[i+1]))
                else:
                    setattr(self, f"output_layer", nn.Linear(size[i], size[i+1]))
            with torch.no_grad():
                for i in range(len(size) - 1):
                    if i != len(size) - 2:
                        layer = getattr(self, f"layer{i}")
                        # Random weight initialization for hidden layers
                        weights = torch.randn(size[i+1], size[i], dtype=torch.float64)
                        layer.weight = nn.Parameter(weights)
                        biases= 10 * torch.rand(size[i+1], dtype=torch.float64) - 5
                        layer.bias= nn.Parameter(biases)
                    else:
                        layer = getattr(self, f"output_layer")
                        # Random weight initialization for output layer
                        weights = torch.randn(size[i+1], size[i], dtype=torch.float64)
                        layer.weight = nn.Parameter(weights)
                        biases= 10 * torch.rand(size[i+1], dtype=torch.float64) - 5
                        layer.bias= nn.Parameter(biases)
            layers=[]
            for i in range(len(size)-2):
                layers.append(getattr(self, f"layer{i}"))
                layers.append(nn.ReLU())

            # layers = [getattr(self, f"layer{i}") for i in range(len(size) - 2)]
            # layers.append(nn.ReLU())
            layers.append(getattr(self, "output_layer"))
            self.linear_relu_stack = nn.Sequential(*layers)

        def forward(self, x):
            x = self.flatten(x)
            logits = self.linear_relu_stack(x)
            return logits
    return RandomModel()



def test1():
    #300 neuron each layer has 50
    #1k 
    lists=[[2,2,2,2],[2,4,4,4,2],[3,7,7,7,7,5],[5,8,8,8,8],[5,7,4,8,8,5],[4,10,9,10,4]]
    list_pre=[{'i0':[0.1, 0.3], 'i1':[-0.7, 0.]},{'i0':[0.1, 0.3], 'i1':[-0.7, 0.]},{'i0':[0.1, 0.3], 'i1':[-0.7, 0.],'i2':[0, 0.4]},{'i0':[0.1, 0.3], 'i1':[-0.7, 0.],'i2':[0, 0.4],'i3':[-0.4, 0.1],'i4':[0, 0]},{'i0':[0.1, 0.3], 'i1':[-0.7, 0.],'i2':[0, 0.4],'i3':[-0.4, 0.1],'i4':[-0.9, 0.5],'i5':[0.25, 0.45]},{'i0':[0.1, 0.3], 'i1':[-0.7, 0.],'i2':[0, 0.4],'i3':[-0.4, 0.1],'i4':[0.3, 0.4]}]
    plot=[]
    symbolic_execution_list=[]
    interval_execution_list=[]
    for i,list in enumerate(lists):
        product = 1
        for value in list:
            product *= value
        dnn = create_random(list)
        symbolic_state = my_symbolic_execution(dnn)
    #     # time the execution
        import time
        st = time.time()
        _ = z3.solve(symbolic_state)
        duration=time.time() - st
        print('time to solve symbolic execution: ', duration)
        symbolic_execution_list.append((product,duration))
        print(product)
        st = time.time()
        _ = my_interval_execution(dnn,list_pre[i])
        duration=time.time() - st
        print('time to solve interval execution: ', duration)
        interval_execution_list.append((product,duration))
    #     print(product)

    print(symbolic_execution_list)
    print(interval_execution_list)
    symbolic_values_x, symbolic_values_x_y = zip(*symbolic_execution_list)
    interval_values_x, interval_values_x_y = zip(*interval_execution_list)
    plt.scatter(symbolic_values_x, symbolic_values_x_y,color="red")
    # plt.scatter(interval_values_x, interval_values_x_y,color="blue")

    plt.xlabel('Product of values in the list')
    plt.ylabel('Time to solve (seconds)')
    plt.title('Scatter plot of Product vs Time to solve')
    plt.show()

    plt.scatter(interval_values_x, interval_values_x_y,color="blue")
    plt.show()





test1()