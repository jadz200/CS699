1)python se.py

#Output

Test1:


 finding outputs when inputs are fixed [i0 == 1, i1 == -1]
{'i0': [1, 1], 'i1': [-1, -1], 'n0_0': [2.0, 2.0], 'n0_1': [0, 0], 'n1_0': [1.0, 1.0], 'n1_1': [0, 0], 'o0': [1.0, 1.0], 'o1': [-1.0, -1.0]}

executing using precondition 0.1 <= i0 <= 0.3, -0.7 <= i1 <= 0.0
{'i0': [0.1, 0.3], 'i1': [-0.7, 0.0], 'n0_0': [0.1, 1.0], 'n0_1': [0, 0.3], 'n1_0': [0, 0.5], 'n1_1': [0, 0], 'o0': [0.0, 0.5], 'o1': [-0.5, 0.0]}


Test2:


 finding outputs when inputs are fixed [i0 == 1, i1 == -1]
{'i0': [1, 1], 'i1': [-1, -1], 'n0_0': [1.1, 1.1], 'n0_1': [1.5, 1.5], 'n0_2': [0, 0], 'n0_3': [0, 0], 'n1_0': [1.29, 1.29], 'n1_1': [0.7, 0.7], 'n1_2': [0.7, 0.7], 'n1_3': [0, 0], 'n2_0': [1.85, 1.85], 'n2_1': [0, 0], 'n2_2': [0, 0], 'n2_3': [0, 0], 'o0': [-0.15, -0.15], 'o1': [-2.925, -2.925]}

executing using precondition 0.1 <= i0 <= 0.3, -0.7 <= i1 <= 0.0
{'i0': [0.1, 0.3], 'i1': [-0.7, 0.0], 'n0_0': [0.1, 0.37], 'n0_1': [0.1, 0.65], 'n0_2': [0, 0.21], 'n0_3': [0, 0.15], 'n1_0': [0.11, 0.583], 'n1_1': [0, 0.265], 'n1_2': [0, 0.265], 'n1_3': [0, 0], 'n2_0': [0.057, 0.848], 'n2_1': [0, 0], 'n2_2': [0, 0], 'n2_3': [0, 0], 'o0': [-1.943, -1.152], 'o1': [-2.424, -2.0285]}





2) 

i)In part 1 We just loop over the list of sizes and generate  the layers with their neurons with random weights and biases and return 
  it as a Pytorch Object
  In part 2 it's very similar as the symbolic execution function we've written for part 1 but we have accurate values for the lower and upper bound of the input neurons, we just have make sure to check whether the weight is negative or positive to correctly compute the bounds of the next neurons, unlike symbolic execution we are directly returning the dictioary res with it's appropriate values


ii)
![alt text](https://i.imgur.com/Fh9GKef.png)

 Looking at the plots we can clearly see that interval execution is way faster at executing than symbolic execution and that its way more scalable.

iii) hardest part was understanding how to compute teh lower and upper bounds in case we have a negative weight

iv) Follow the PA instructions it's already pretty clear, also search more outside of the website concerning how to calculate weight. 