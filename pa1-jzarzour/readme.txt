1)
#Run program
python se.py

#Output

Test1:




Symbolic States:

And(i0 == i0,
    i1 == i1,
    n0_0 ==
    If(0 + 1*i0 + -1*i1 - 0 <= 0, 0, 0 + 1*i0 + -1*i1 - 0),
    n0_1 ==
    If(0 + 1*i0 + 1*i1 - 0 <= 0, 0, 0 + 1*i0 + 1*i1 - 0),
    n1_0 ==
    If(0 + 1/2*n0_0 + -1/5*n0_1 - 0 <= 0,
       0,
       0 + 1/2*n0_0 + -1/5*n0_1 - 0),
    n1_1 ==
    If(0 + -1/2*n0_0 + 1/10*n0_1 - 0 <= 0,
       0,
       0 + -1/2*n0_0 + 1/10*n0_1 - 0),
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
    n0_0 ==
    If(0 + 1*i0 + -1*i1 - 0 <= 0, 0, 0 + 1*i0 + -1*i1 - 0),
    n0_1 ==
    If(0 + 1*i0 + 1*i1 - 0 <= 0, 0, 0 + 1*i0 + 1*i1 - 0),
    n0_2 ==
    If(0 + 1*i0 + 1*i1 - 0 <= 0, 0, 0 + 1*i0 + 1*i1 - 0),
    n0_3 ==
    If(0 + 1*i0 + 1*i1 - 0 <= 0, 0, 0 + 1*i0 + 1*i1 - 0),
    n1_0 ==
    If(0 + 1/2*n0_0 + -1/5*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 0 <=
       0,
       0,
       0 + 1/2*n0_0 + -1/5*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 0),
    n1_1 ==
    If(0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 0 <=
       0,
       0,
       0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 0),
    n1_2 ==
    If(0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 0 <=
       0,
       0,
       0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 0),
    n1_3 ==
    If(0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 1 <=
       0,
       0,
       0 + -1/2*n0_0 + 1/10*n0_1 + -1/2*n0_2 + 1/10*n0_3 - 1),
    n2_0 ==
    If(0 + 1*n1_0 + -1/5*n1_1 + 1*n1_2 + -1/5*n1_3 - 0 <= 0,
       0,
       0 + 1*n1_0 + -1/5*n1_1 + 1*n1_2 + -1/5*n1_3 - 0),
    n2_1 ==
    If(0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 - 0 <=
       0,
       0,
       0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 - 0),
    n2_2 ==
    If(0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 - 0 <=
       0,
       0,
       0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 - 0),
    n2_3 ==
    If(0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 - 1 <=
       0,
       0,
       0 + -1/2*n1_0 + 1/10*n1_1 + -1/2*n1_2 + 1/10*n1_3 - 1),
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
    intialize an empty dictionary and an empty list to know both the symbolic value and the position of the variables in the dnn,
    then loop over all of the layers and check if its a weight and a bias layer. in the case where it's a weight layer we loop throught
    all the neurons and generate their correct names, after that we loop over the weights of these neurons and retrieve the correct real
    element from the dictionary and after computing the symbolic execution we store it in the dictionary. The next layer would be a bias
    layer, when retrieving the symbolic execution we substract the bias numbers and add the relu function.
    In the end we just loop over teh dictionary to add the And logic to connect all the variables to make good symbolic execution

ii)
    Converting to SE using Z3. I am unfamilliar with Z3 so I did not know how to correctly make assignements while not getting a boolean value from the expression
iii)
    Make Sure to understand what a DNN is, Solve it by hand first and try to write a program that compute those values then transform it to SE, just as described in the TIPS section pf the assignement