import z3
def relu(v):
   return z3.If(0.0 >= v, 0.0, v)

def my_symbolic_execution(dnn):
    ii0=z3.Real("ii0")
    ii1=z3.Real("ii1")
    i0=4
    i1=7/2
    res=[i0,i1]
    prev_layer=len(res)
    len_layer=0
    for layer in dnn: #loop over all the layers
        print("nodes: "+ str(layer))
        print("length: "+ str(len_layer))
        for i in range(0,len(layer)): #loops over neurons in a specific layer
            print(layer[i])
            print("bias " +str(layer[i][1]))
            temp=0.0
            for j in range(len(layer[i][0])): #loops over all the weigth connected by the previous neurons to the current neuron
                weight=(layer[i][0][j])
                weightNum=z3.Real()
                print("weigth: "+str(weight))
                print("IM GOING INSANE   "+str(j))
                print(len_layer)
                input=res[j+len_layer]
                inputNum=z3.Real("")
                print("input: "+str(input))
                temp+= weight*input
            bias=layer[i][1]
            biasNum=z3.Real()
            temp-=bias
            if layer[i][2]==True:
                if temp<=0:
                    res.append(0)
                else:
                    res.append(temp)
            else:
                res.append(temp)
        len_layer+=prev_layer
        prev_layer=len(layer)
        print(res)

n00 = ([1.0, -1.0], 0.0, True)
n01 = ([1.0, 1.0], 0.0, True)
hidden_layer0 = [n00,n01]

n10 = ([0.5, -0.2], 0.0, True)
n11 = ([-0.5, 0.1], 0.0, True)
n12 = ([-0.5, 0.1], 0.0, True)
hidden_layer1 = [n10, n11,n12]

# don't use relu for outputs
o0 = ([1.0, -1.0,0.0], 0.0, False)  
o1 = ([-1.0, 1.0,0.0], 0.0, False)
output_layer = [o0, o1]

dnn = [hidden_layer0, hidden_layer1, output_layer]
symbolic_states = my_symbolic_execution(dnn)

