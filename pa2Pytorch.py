import random
import z3
from pa1Pytorch import my_symbolic_execution
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


def my_interval_execution(dnn,pre):
    res = {}
    neuronsList=[]
    prev_layer=len(res)
    len_layer=0
    for interval in pre:
        res[interval]=pre[interval]
        neuronsList.append(interval)
    for layer_index, (name, param) in enumerate(dnn.named_parameters()):
        if param.requires_grad:
            if "bias" in name:
                biases = param.data.tolist() 
                for index,bias in enumerate(biases):
                    
                    neuron=neuronsList[len_layer+index]
                    temp=res[neuron]
                    for bound,val in enumerate(temp):
                        temp[bound]-=bias
                        if not "o" in neuron:
                            res[neuron][bound]=relu_activation(temp[bound])
                        temp[bound]=round(temp[bound],4)

            if "weight" in name:
                neurons = param.data.tolist()
                # For the first layer

                for neuron_index, neuron in enumerate(param): #loops over neurons in a specific layer
                    if  "output_layer" in name:
                        neuron_name = f'o{neuron_index}'
                    else:
                        neuron_name = f'n{int(layer_index/2)}_{neuron_index}'
                    neuronsList.append(neuron_name)
                    temp=[0,0]
                    for weight_index, weight in enumerate(neuron): #loops over all the weigth connected by the previous neurons to the current neuron
                        weight=(float(neuron[weight_index].item()))
                        input=neuronsList[weight_index+len_layer]
                        if weight<0:
                            temp[0]+=res[input][1]*weight
                            temp[1]+=res[input][0]*weight
                        else:
                            temp[0]+=res[input][0]*weight
                            temp[1]+=res[input][1]*weight
                    res[neuron_name]=temp
                if len_layer==0:
                    len_layer+=len(pre)
                len_layer+=prev_layer
                prev_layer=len(param)
    return res

def test1():
    print("\n\nTest1:\n\n")

    dnn= CustomModel1()

    print(" finding outputs when inputs are fixed [i0 == 1, i1 == -1]")
    states = my_interval_execution(dnn, pre={'i0':[1,1], 'i1':[-1,-1]})
    print(states)

    print("\nexecuting using precondition 0.1 <= i0 <= 0.3, -0.7 <= i1 <= 0.0") 
    states = my_interval_execution(dnn, pre={'i0':[0.1, 0.3], 'i1':[-0.7, 0.]})
    print(states)

def test2():
    print("\n\nTest2:\n\n")

    dnn= CustomModel2()

    print(" finding outputs when inputs are fixed [i0 == 1, i1 == -1]")
    states = my_interval_execution(dnn, pre={'i0':[1,1], 'i1':[-1,-1]})
    print(states)

    print("\nexecuting using precondition 0.1 <= i0 <= 0.3, -0.7 <= i1 <= 0.0") 
    states = my_interval_execution(dnn, pre={'i0':[0.1, 0.3], 'i1':[-0.7, 0.]})
    print(states)

class CustomModel1(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer0 = nn.Linear(2, 2)
        self.layer1 = nn.Linear(2, 2)
        self.output_layer = nn.Linear(2, 2)

        with torch.no_grad():
            self.layer0.weight = nn.Parameter(torch.tensor([[1.0, -1.0], [1.0, 1.0]], dtype=torch.float64))
            self.layer0.bias = nn.Parameter(torch.tensor([0.0, 0.0], dtype=torch.float64))
            self.layer1.weight = nn.Parameter(torch.tensor([[0.5, -0.2], [-0.5, 0.1]], dtype=torch.float64))
            self.layer1.bias = nn.Parameter(torch.tensor([0.0, 0.0], dtype=torch.float64))
            self.output_layer.weight = nn.Parameter(torch.tensor([[1.0, -1.0], [-1.0, 1.0]], dtype=torch.float64))
            self.output_layer.bias = nn.Parameter(torch.tensor([0.0, 0.0], dtype=torch.float64))
        self.linear_relu_stack = nn.Sequential(
            self.layer0,
            nn.ReLU(),
            self.layer1 ,
            nn.ReLU(),
            self.output_layer
            )
            
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
    
class CustomModel2(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer0 = nn.Linear(2, 4)
        self.layer1 = nn.Linear(4, 4)
        self.layer2 = nn.Linear(4, 4)
        self.output_layer = nn.Linear(4, 2)

        with torch.no_grad():
            self.layer0.weight = nn.Parameter(torch.tensor([[1.0,-0.1], [1, -0.5],[0.7, 1.0],[0.5, 1.0]], dtype=torch.float64))
            self.layer0.bias = nn.Parameter(torch.tensor([0, 0,0,0], dtype=torch.float64))
            self.layer1.weight = nn.Parameter(torch.tensor([[0.9, 0.2,0.5, 0.1], [0.5, 0.1,-0.5, 0.1],[0.5, 0.1,-0.5, 0.1],[-0.5, 0.1,-0.5, 0.1]], dtype=torch.float64))
            self.layer1.bias = nn.Parameter(torch.tensor([0.0, 0.0,0.0,1.0], dtype=torch.float64))
            self.layer2.weight = nn.Parameter(torch.tensor([[1, -0.2,1, -0.2], [-0.5, 0.1,-0.5, 0.1],[-0.5, 0.1,-0.3, 0.1],[-0.5, 0.1,-0.3, 0.1]], dtype=torch.float64))
            self.layer2.bias = nn.Parameter(torch.tensor([0.0, 0.0,0.0,1.0], dtype=torch.float64))
            self.output_layer.weight = nn.Parameter(torch.tensor([[1.0, -1.0,1.0, -1.0], [-0.5, 1.0,1.0, 1.0]], dtype=torch.float64))
            self.output_layer.bias = nn.Parameter(torch.tensor([2.0, 2.0], dtype=torch.float64))
        self.linear_relu_stack = nn.Sequential(
            self.layer0,
            nn.ReLU(),
            self.layer1,
            nn.ReLU(),
            self.layer2,
            nn.ReLU(),
            self.output_layer
            )
            
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

def main():
    test1()
    test2()

if __name__=="__main__":
    main()