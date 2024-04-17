import random
import z3
from pa1Encoded import my_symbolic_execution
import matplotlib.pyplot as plt
def relu_activation(temp): return temp if temp > 0 else 0

def create_random_nn(list):
    res=[]
    for index,num in enumerate(list):
        if index==len(list)-1:
            output_layer=[]
            prev_layer_nodes=list[len(list)-2]
            for i in range(0,num):
                neuron_name = f'o{i}'
                weights=[]
                for j in range(0,prev_layer_nodes):
                    weights.append(round(random.uniform(-1.0, 1.0),2))
                bias=round(random.uniform(-5.0, 5.0),2)
                output_layer.append((weights,bias,False))
            res.append(output_layer)
        else:
            hidden_layer=[]
            prev_layer_nodes=list[index-1]
            for neuron_index in range(0,num):
                neuron_name = f'n{index-1}_{neuron_index}'
                weights=[]
                for j in range(0,prev_layer_nodes):
                    weights.append(round(random.uniform(-1.0, 1.0),2))
                bias=round(random.uniform(-5.0, 5.0),2)
                hidden_layer.append((weights,bias,True))
            res.append(hidden_layer)

    return res

def my_interval_execution(dnn,pre):
    res = {}
    neuronsList=[]
    prev_layer=len(res)
    len_layer=0
    for interval in pre:
        res[interval]=pre[interval]
        neuronsList.append(interval)
    for layer_index, layer in enumerate(dnn): #loop over all the layers
        for neuron_index, neuron in enumerate(layer): #loops over neurons in a specific layer
            if layer_index == len(dnn) - 1:
                neuron_name = f'o{neuron_index}'
            else:
                neuron_name = f'n{layer_index}_{neuron_index}'
            temp=[0,0]
            bias=layer[neuron_index][1]
            neuronsList.append(neuron_name)
            for weight_index, weight in enumerate(neuron[0]): #loops over all the weigth connected by the previous neurons to the current neuron
                weight=(layer[neuron_index][0][weight_index])
                input=neuronsList[weight_index+len_layer]
                if weight<0:
                    temp[0]+=res[input][1]*weight
                    temp[1]+=res[input][0]*weight
                else:
                    temp[0]+=res[input][0]*weight
                    temp[1]+=res[input][1]*weight
            for bound,val in enumerate(temp):
                temp[bound]-=bias
                if neuron[2]:  # Apply relu if specified
                    temp[bound] = round(relu_activation(val),4)
            res[neuron_name]=temp
        if len_layer==0:
                len_layer+=len(pre)
        len_layer+=prev_layer
        prev_layer=len(layer)
        

    return res

def test1():
    #300 neuron each layer has 50
    #1k 
    lists=[[8,8,8,5,4,3]]
    plot=[]
    for list in lists:
        product = 1
        for value in list:
            product *= value
        dnn = create_random_nn(list)
        symbolic_state = my_symbolic_execution(dnn)
        # time the execution
        import time
        st = time.time()
        _ = z3.solve(symbolic_state)
        duration=time.time() - st
        print('time to solve: ', duration)
        plot.append((product,duration))
        print(product)
    x_values, y_values = zip(*plot)
    plt.scatter(x_values, y_values)
    plt.xlabel('Product of values in the list')
    plt.ylabel('Time to solve (seconds)')
    plt.title('Scatter plot of Product vs Time to solve')
    plt.show()

def test2():
    n00 = ([1.0, -1.0], 0.0, True)
    n01 = ([1.0, 1.0], 0.0, True)

    hidden_layer0 = [n00,n01]
    n10 = ([0.5, -0.2], 0.0, True)
    n11 = ([-0.5, 0.1], 0.0, True)
    hidden_layer1 = [n10, n11]


    # don't use relu for outputs
    o0 = ([1.0, -1.0], 0.0, False)  
    o1 = ([-1.0, 1.0], 0.0, False)
    output_layer = [o0, o1]

    dnn = [hidden_layer0, hidden_layer1, output_layer]
    
    print(" finding outputs when inputs are fixed [i0 == 1, i1 == -1]")
    states = my_interval_execution(dnn, pre={'i0':[1,1], 'i1':[-1,-1]})
    print(states)

    print("executing using precondition 0.1 <= i0 <= 0.3, -0.7 <= i1 <= 0.0") 
    states = my_interval_execution(dnn, pre={'i0':[0.1, 0.3], 'i1':[-0.7, 0.]})
    print(states)

def main():
    # test1()
    test2()

if __name__=="__main__":
    main()