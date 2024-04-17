import z3
import os
import torch
from torch import nn

def my_symbolic_execution(dnn):
    res = {}
    neuronsList=[]
    prev_layer=len(res)
    len_layer=0
    for layer_index, (name, param) in enumerate(dnn.named_parameters()):
        if param.requires_grad:
            if "bias" in name:
                biases = param.data.tolist() 
                # print(biases)
                for index,bias in enumerate(biases):
                    neuron=neuronsList[len_layer+index]
                    temp=res[neuron]-bias
                    # print(neuron)
                    if not "o" in neuron:
                        res[neuron]=z3.If(temp <= 0, 0.0, temp)

            if "weight" in name:
                neurons = param.data.tolist()
                # For the first layer
                if layer_index == 0:
                    for i in range(len(neurons[0])):
                        neuron_name = f'i{i}'
                        neuronsList.append(neuron_name)
                        res[neuron_name] = z3.Real(neuron_name)
                    
                    len_layer+=prev_layer
                    prev_layer=len(param[0])
                    # print(res)
                for neuron_index, neuron in enumerate(param): #loops over neurons in a specific layer
                    if  "output_layer" in name:
                        neuron_name = f'o{neuron_index}'
                    else:
                        neuron_name = f'n{int(layer_index/2)}_{neuron_index}'
                    neuronsList.append(neuron_name)
                    temp=0
                    for weight_index, weight in enumerate(neuron): #loops over all the weigth connected by the previous neurons to the current neuron
                        weight=(float(neuron[weight_index].item()))

                        input=neuronsList[weight_index+len_layer]
                        temp+= weight*z3.Real(input)
                    res[neuron_name]=temp
                len_layer+=prev_layer
                prev_layer=len(param)

        # Construct the output as a PyTorch tensor
    ans=[]
    # print(res)
    for key in res:
        ans.append((z3.Real(key)==res[key]))
    # print(ans)
    return z3.And(ans)

def test():
    print("\n\nTest1:\n\n")

    dnn=CustomModel1()
    symbolic_states = my_symbolic_execution(dnn)
    assert z3.is_expr(symbolic_states) 
    print("\n\nSymbolic States:\n")
    print(symbolic_states)
    print("\n\nSolving symbolic states:\n")
    z3.solve(symbolic_states)
    print("\n\nfinding outputs when inputs are fixed [i0 == 1, i1 == -1]\n")
    i0, i1, n0_0, n0_1, o0, o1 = z3.Reals("i0 i1 n0_0 n0_1 o0 o1")
    g = z3.And([i0 == 1.0, i1 == -1.0])
    z3.solve(z3.And(symbolic_states, g))
    print("\n\nProve that if (n0_0 > 0.0 and n0_1 <= 0.0) then o0 > o1\n")
    g = z3.Implies(z3.And([n0_0 > 0.0, n0_1 <= 0.0]), o0 > o1)
    print(g)  #  Implies (And(n0_0 > 0, n0_1 <= 0), o0 > o1)
    z3.prove(z3.Implies(symbolic_states, g)) 
    print("\n\nProve that when (i0 - i1 > 0 and i0 + i1 <= 0), then o0 > o1\n")
    g = z3.Implies(z3.And([i0 - i1 > 0.0, i0 + i1 <= 0.0]), o0 > o1)
    print(g)  # Implies(And(i0 - i1 > 0, i0 + i1 <= 0), o0 > o1)
    z3.prove(z3.Implies(symbolic_states, g))
    print("\n\nDisprove that when i0 - i1 >0, then o0 > o1\n")
    g = z3.Implies(i0 - i1 > 0.0, o0 > o1)
    print(g)  # Implies(And(i0 - i1 > 0, i0 + i1 <= 0), o0 > o1)
    z3.prove(z3.Implies(symbolic_states, g))

def test2():
    print("\n\nTest2:\n\n")

    dnn=CustomModel2()
    symbolic_states = my_symbolic_execution(dnn)

    assert z3.is_expr(symbolic_states) 
    print("\n\nSymbolic States:\n")
    print(symbolic_states)
    print("\n\nSolving symbolic states:\n")
    z3.solve(symbolic_states)
    print("\n\nfinding outputs when inputs are fixed [i0 == 1, i1 == -1]\n")
    i0, i1, n0_0, n0_1, o0, o1 = z3.Reals("i0 i1 n0_0 n0_1 o0 o1")
    g = z3.And([i0 == 1.0, i1 == -1.0])
    z3.solve(z3.And(symbolic_states, g))
    print("\n\nProve that if (n0_0 > 0.0 and n0_1 <= 0.0) then o0 > o1\n")
    g = z3.Implies(z3.And([n0_0 > 0.0, n0_1 <= 0.0]), o0 > o1)
    print(g)  #  Implies (And(n0_0 > 0, n0_1 <= 0), o0 > o1)
    z3.prove(z3.Implies(symbolic_states, g)) 
    print("\n\nProve that when (i0 - i1 > 0 and i0 + i1 <= 0), then o0 > o1\n")
    g = z3.Implies(z3.And([i0 - i1 > 0.0, i0 + i1 <= 0.0]), o0 > o1)
    print(g)  # Implies(And(i0 - i1 > 0, i0 + i1 <= 0), o0 > o1)
    z3.prove(z3.Implies(symbolic_states, g))
    print("\n\nDisprove that when i0 - i1 >0, then o0 > o1\n")
    g = z3.Implies(i0 - i1 > 0.0, o0 > o1)
    print(g)  # Implies(And(i0 - i1 > 0, i0 + i1 <= 0), o0 > o1)
    z3.prove(z3.Implies(symbolic_states, g))
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
            self.layer0.weight = nn.Parameter(torch.tensor([[1,-1], [1, 1],[1, 1],[1, 1.0]], dtype=torch.float64))
            self.layer0.bias = nn.Parameter(torch.tensor([0, 0,0,0], dtype=torch.float64))
            self.layer1.weight = nn.Parameter(torch.tensor([[0.5, -0.2,-0.5, 0.1], [-0.5, 0.1,-0.5, 0.1],[-0.5, 0.1,-0.5, 0.1],[-0.5, 0.1,-0.5, 0.1]], dtype=torch.float64))
            self.layer1.bias = nn.Parameter(torch.tensor([0.0, 0.0,0.0,1.0], dtype=torch.float64))
            self.layer2.weight = nn.Parameter(torch.tensor([[1, -0.2,1, -0.2], [-0.5, 0.1,-0.5, 0.1],[-0.5, 0.1,-0.5, 0.1],[-0.5, 0.1,-0.5, 0.1]], dtype=torch.float64))
            self.layer2.bias = nn.Parameter(torch.tensor([0, 0,0,1.0], dtype=torch.float64))
            self.output_layer.weight = nn.Parameter(torch.tensor([[1, -1,1, -1.0], [-1, 1,-1, 1]], dtype=torch.float64))
            self.output_layer.bias = nn.Parameter(torch.tensor([0, 0], dtype=torch.float64))
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
    test()  
    test2()


if __name__ == "__main__":
    main()