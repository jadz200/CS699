1)
#Run program
python pa1.py

#Output

Test1:




Symbolic States:

And(i0 == i0,
    i1 == i1,
    n0_0 == If(0 + 1*i0 + -1*i1 <= 0, 0, 0 + 1*i0 + -1*i1),
    n0_1 == If(0 + 1*i0 + 1*i1 <= 0, 0, 0 + 1*i0 + 1*i1),
    n1_0 ==
    If(0 + 1/2*n0_0 + -1/5*n0_1 <= 0,
       0,
       0 + 1/2*n0_0 + -1/5*n0_1),
    n1_1 ==
    If(0 + -1/2*n0_0 + 1/10*n0_1 <= 0,
       0,
       0 + -1/2*n0_0 + 1/10*n0_1),
    o0 == 0 + 1*n1_0 + -1*n1_1,
    o1 == 0 + -1*n1_0 + 1*n1_1)


Solving symbolic states:

[i1 = 7/2,
 n0_0 = 1/2,
 n1_1 = 1/2,
 i0 = 4,
 n0_1 = 15/2,
 o1 = 1/2,
 n1_0 = 0,
 o0 = -1/2]


finding outputs when inputs are fixed [i0 == 1, i1 == -1]

[n1_1 = 0,
 i0 = 1,
 n0_1 = 0,
 o1 = -1,
 o0 = 1,
 n0_0 = 2,
 i1 = -1,
 n1_0 = 1]


Prove that if (n0_0 > 0.0 and n0_1 <= 0.0) then o0 > o1

Implies(And(n0_0 > 0, n0_1 <= 0), o0 > o1)
proved


Prove that when (i0 - i1 > 0 and i0 + i1 <= 0), then o0 > o1

Implies(And(i0 - i1 > 0, i0 + i1 <= 0), o0 > o1)
proved


Disprove that when i0 - i1 >0, then o0 > o1

Implies(i0 - i1 > 0, o0 > o1)
counterexample
[n1_1 = 1/2,
 i0 = 4,
 n0_1 = 15/2,
 o1 = 1/2,
 o0 = -1/2,
 i1 = 7/2,
 n1_0 = 0,
 n0_0 = 1/2]


Test2:




Symbolic States:

And(i0 == i0,
    i1 == i1,
    n0_0 == If(0 + 1*i0 + -1*i1 <= 0, 0, 0 + 1*i0 + -1*i1),
    n0_1 == If(0 + 1*i0 + 1*i1 <= 0, 0, 0 + 1*i0 + 1*i1),
    n0_2 == If(0 + 1*i0 + 1*i1 <= 0, 0, 0 + 1*i0 + 1*i1),
    n0_3 == If(0 + 1*i0 + 1*i1 <= 0, 0, 0 + 1*i0 + 1*i1),
    n1_0 ==
    If(0 + 1/2*n0_0 + -1/5*n0_1 + -1/2*n0_2 + 1/10*n0_3 <= 0,
       0,
       0 + 1/2*n0_0 + -1/5*n0_1 + -1/2*n0_2 + 1/10*n0_3),
    n1_1 ==
    If(0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 <=
       0,
       0,
       0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3),
    n1_2 ==
    If(0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 <=
       0,
       0,
       0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3),
    n1_3 ==
    If(-1 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 <=
       0,
       0,
       -1 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3),
    n2_0 ==
    If(0 + 1*n1_0 + -1/5*n1_1 + 1*n1_2 + -1/5*n1_3 <= 0,
       0,
       0 + 1*n1_0 + -1/5*n1_1 + 1*n1_2 + -1/5*n1_3),
    n2_1 ==
    If(0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 <=
       0,
       0,
       0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3),
    n2_2 ==
    If(0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 <=
       0,
       0,
       0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3),
    n2_3 ==
    If(-1 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 <=
       0,
       0,
       -1 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3),
    o0 == 0 + 1*n2_0 + -1*n2_1 + 1*n2_2 + -1*n2_3,
    o1 == 0 + -1*n2_0 + 1*n2_1 + -1*n2_2 + 1*n2_3)


Solving symbolic states:

[n1_0 = 0,
 o1 = 0,
 o0 = 0,
 n1_3 = 0,
 i0 = 7/12,
 n0_1 = 5/3,
 n2_0 = 0,
 n1_2 = 0,
 n1_1 = 0,
 n2_2 = 0,
 n0_0 = 0,
 n2_3 = 0,
 n0_2 = 5/3,
 i1 = 13/12,
 n2_1 = 0,
 n0_3 = 5/3]


finding outputs when inputs are fixed [i0 == 1, i1 == -1]

[i0 = 1,
 o1 = -1,
 n2_2 = 0,
 n1_2 = 0,
 n2_3 = 0,
 n0_0 = 2,
 i1 = -1,
 n0_2 = 0,
 n2_1 = 0,
 n0_3 = 0,
 n2_0 = 1,
 n1_1 = 0,
 n1_0 = 1,
 n0_1 = 0,
 o0 = 1,
 n1_3 = 0]


Prove that if (n0_0 > 0.0 and n0_1 <= 0.0) then o0 > o1

Implies(And(n0_0 > 0, n0_1 <= 0), o0 > o1)
proved


Prove that when (i0 - i1 > 0 and i0 + i1 <= 0), then o0 > o1

Implies(And(i0 - i1 > 0, i0 + i1 <= 0), o0 > o1)
proved


Disprove that when i0 - i1 >0, then o0 > o1

Implies(i0 - i1 > 0, o0 > o1)
counterexample
[n1_0 = 0,
 n1_3 = 0,
 o1 = 0,
 i0 = 7/8,
 n2_2 = 0,
 n1_2 = 0,
 o0 = 0,
 n2_1 = 0,
 n2_3 = 0,
 n0_0 = 1/2,
 i1 = 3/8,
 n0_2 = 5/4,
 n0_1 = 5/4,
 n0_3 = 5/4,
 n1_1 = 0,
 n2_0 = 0]


2)i)
    Begin by intializing an array that has the nodes as strings and a dictionary (res) that will hold the answer, also keep the length of the current and previous layer so you can iterate correctly and not have any OutOfBounds exceptions.
    we start by iterating over the layers of the DNN,then the neurons in each layer, we intialze the whole function with the bias then assign a name to the current neuron and add it to the neurons arrays (only holds the position).
    then we iterate over all the weights that this neuron has and add them to the bias.
    After that we use the relu function and add the answer into the dictionary (res), and we change the layer legnths
    Once done we just convert the dictionary to an z3.And SE and return that

ii)
    Converting to SE using Z3. I am unfamilliar with Z3 so I did not know how to correctly make assignements while not getting a boolean value from the expression
iii)
    Make Sure to understand what a DNN is, Solve it by hand first and try to write a program that compute those values then transform it to SE