import z3

def my_symbolic_execution(dnn):
    res = {}
    neurons=[]
    prev_layer=len(res)
    len_layer=0
    for layer_index, layer in enumerate(dnn): #loop over all the layers
        for neuron_index, neuron in enumerate(layer): #loops over neurons in a specific layer
            if layer_index==0:
                neuron_name = f'i{neuron_index}'
                neurons.append(neuron_name)
                res[neuron_name]=z3.Real(neuron_name)
                continue
            bias=layer[neuron_index][1]

            temp=-bias
            if layer_index == len(dnn) - 1:
                neuron_name = f'o{neuron_index}'
            else:
                neuron_name = f'n{layer_index}_{neuron_index}'
            neurons.append(neuron_name)
            for weight_index, weight in enumerate(neuron[0]): #loops over all the weigth connected by the previous neurons to the current neuron
                weight=(layer[neuron_index][0][weight_index])
                input=neurons[weight_index+len_layer]
                temp+= weight*z3.Real(input)

            if neuron[2]:  # Apply relu if specified
                temp = z3.If(temp <= 0, 0.0, temp)
            res[neuron_name]=temp
        len_layer+=prev_layer
        prev_layer=len(layer)
        
    ans=[]
    for key in res:
        ans.append((z3.Real(key)==res[key]))
    return z3.And(ans)

def test():
    print("\n\nTest1:\n\n")
    input_layer=["i0","i1"]

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

    dnn = [input_layer,hidden_layer0, hidden_layer1, output_layer]
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
    input_layer=["i0","i1"]

    n00 = ([1.0, -1.0], -2, True)
    n01 = ([1.0, -0.5], -1, True)
    n02 = ([0.7, 1.0], 0.0, True)
    n03 = ([0.5, 1.0], 0.0, True)

    hidden_layer0 = [n00,n01,n02,n03]

    n10 = ([0.9, 0.2,0.5, 0.1], 0.0, True)
    n11 = ([0.5, 0.1,-0.5, 0.1], 0.0, True)
    n12 = ([0.5, 0.1,-0.5, 0.1], 0.0, True)
    n13 = ([-0.5, 0.1,-0.5, 0.1], 1.0, True)
    hidden_layer1 = [n10, n11,n12,n13]


    n20 = ([1, -0.2,1, -0.2], 0.0, True)
    n21 = ([-0.5, 0.1,-0.5, 0.1], 0.0, True)
    n22 = ([-0.5, 0.1,-0.2, 0.1], 0.0, True)
    n23 = ([-0.5, 0.1,-0.3, 0.1], 1.0, True)

    hidden_layer2 = [n20, n21,n22,n23]

    # don't use relu for outputs
    o0 = ([1.0, -1.0,1.0, -1.0], 0.0, False)  
    o1 = ([-1.0, 1.0,-1.0, 1.0], 0.0, False)
    output_layer = [o0, o1]
    dnn = [input_layer,hidden_layer0, hidden_layer1,hidden_layer2, output_layer]
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

def main():
    test()  
    test2() 

if __name__ == "__main__":
    main()