import random
import z3
from pa1 import my_symbolic_execution
import matplotlib.pyplot as plt

def create_random_nn(list):
    res=[]
    for index,num in enumerate(list):
        if index==0:
            input_layer=[]
            for i in range(0,num):
                neuron_name = f'i{i}'
                input_layer.append(z3.Real(neuron_name))
            res.append(input_layer)
        elif index==len(list)-1:
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
def main():
    lists=[[2,2,2,2],[2,3,4,3,2],[5, 8, 6, 8, 5, 8],[8,8,7,7,7,9],[2,4,5,5,4,5],[3,1,4,7,4,9],[8,8,5,5,5,6,8],[8,8,2,5,3,6,8],[8,8,9,9,9,6,8],[8,8,8,8,8,8,8]]
    plot=[]
    for list in lists:
        print(list)
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
if __name__=="__main__":
    main()