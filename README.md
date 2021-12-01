# Introduction

optimization demands a lot of research, not only from the professionals
responsible for developing the hardware but also from physicists and
chemists who can find ways or elements that improve the functioning of
the hardware.

Regardless of the application, every hardware project is complex,
demanding a great intellectual effort and, consequently, monetary. The
process of design and development of a hardware component has several
steps. In this work, the focus is on the optimization of Finite State
Machines (FSM).

FSMs are abstractions of the behavior of a given circuit, whether it is
a part of the whole of an Application-Specific Integrated Circuit (ASIC)
or a conventional processor. When thinking in terms of algorithm, it is
referred to the sequence of commands, or steps, that in a certain order
performs a task.

This algorithm can be abstracted in the form of a machine where each
step is represented by a state. Conventional computers allow us to
perform only one step at a time and the transition between states is
made through external or internal stimulus (inputs).

From this representation, it is possible to provide a physical model,
where this FSM model can be synchronous about to with concerning the
internal or external behavior, as well as it can be asynchronous,
varying according to the application.

The optimization of an FSM can lead to a reduction in the physical size
of the final circuit, resulting in savings in the critical path, area,
and power. For the optimization of the FSM, the goal is composed of
finding the best allocation of states and minimizing the size of the
Boolean expressions that represent the machine behavior.

This is not a recent research topic , however, due to its importance and
being an NP-Complete problem, is still an open topic because of breaking
down of Dennard’s law , which states that as the dimensions of a device
go down, so does the power consumption. And many complex metaheuristic
algorithms have been tested for this problem, such as Evolutionary
Algorithms , Tabu Seach , and Simulated Annealing .

As far as it is known, Ahmad et al have proposed a complex hybrid method
combining Genetic Algorithms with Simulated Annealing, to find optimal
state-machine allocations. Thus, arises the question **how distant is
the result with a much simpler and faster metaheuristic, which uses less
computational resources (without a population of solutions)?**
Therefore, the objective of this investigation is to provide an answer
to this question. Furthermore, the main contribution of this paper is
**the evaluation of the state assignment in a finite state machine
solution produced by a simulated annealing algorithm**.

# Definitions

## Finite State Machine <span id="sec:FSM" label="sec:FSM">\[sec:FSM\]</span>

Sequential circuits can be defined as circuits with a section made of
combinational logic and another section of memory which are normally
flip-flops. Where each stage that the sequential circuit advances are
called a state. In each state, the circuit stores the inputs passed to
define its output, and the state transition only occurs with the clock
variation .

An FSM has a finite number of inputs, constituting the set of
*N* = {*N*<sub>1</sub>, *N*<sub>2</sub>, ..., *N*<sub>*n*</sub>}. Thus,
the circuit has a finite number of outputs, determined by the set of
*M* = {*M*<sub>1</sub>, *M*<sub>2</sub>, ..., *M*<sub>*m*</sub>}. The
value contained in each memory element is called state variables,
forming the set of
*K* = {*K*<sub>1</sub>, *K*<sub>2</sub>, ..., *K*<sub>*k*</sub>}. The
values contained in the *K* memory elements define the current state of
the machine. The internal transition functions generate the next state
set *S* = {*S*<sub>1</sub>, *S*<sub>2</sub>, ..., *S*<sub>*s*</sub>},
which depend on the inputs *N* and the current states *K* of the machine
and are defined through combinational circuits . The values of S, which
appear in the state machine transition function at time *t*, determine
the values of the state variables at time *t* + 1, and therefore define
the next state of the machine.

The behavior of an FSM can be described through a state transition
diagram or a state transition table. A state transition diagram or state
transition table lists the current state, next state, input, and output.
A state transition table has 2<sup>*N*</sup> columns, one for each
occurrence of the input set and 2<sup>*K*</sup> rows, one for each
occurrence of the state set.

The transition diagram is an oriented graph, where each node represents
a state, and from each node emanate *p* oriented edges corresponding to
the state transitions. Each oriented edge is labeled with the input that
determines the transition and the output generated. FSM determine the
next state *K*(*t*+1), based only on the current state *K*(*t*) and the
current input *N*(*t*). FSM can be represented by,

$$\\begin{aligned}
K(t+1) = f \[K(t), N(t)\]
\\label{nextstate}\\end{aligned}$$

where *f* is a state transition function. The output value *M*(*t*) is
obtained by,

$$\\begin{aligned}
M(t+1) = g \[K(t)\]
\\label{out1}\\end{aligned}$$

$$\\begin{aligned}
M(t+1) = g \[K(t), N(t)\]
\\label{out2}\\end{aligned}$$

where *g* is an output function.

An FSM with properties described in the Eqs. ([\[nextstate\]][1]) and
([\[out1\]][2]) is called a *Moore* Machine and a machine described
through the Eqs. ([\[nextstate\]][1]) and ([\[out2\]][3]) is called the
*Mealy* Machine.

The operation of computers is based on the operation of transistors,
which depending on the amount of stored charge, the signal can be
interpreted as high (1) or low (0), and off (no stored energy).

As the computer works on the interpretation of two electrical impulses
can be observed that it is a binary system, therefore, being governed by
Boolean algebra.

Boolean algebra is an algebraic structure that defines the arithmetic of
logical operators that, being composed of the symbols *S* = {0, 1},
constitute a binary system. The concepts of Boolean algebra are also
used in electronics since physical circuits are rather designed in
abstractions, called logic circuits.

Given a Boolean space, a *variable* is a symbol representing a
coordinate in that space. A variable or its negation is called
*literal*. The term product is defined as the Boolean product of one or
more literals. A minimal term, or *minterm*, is a term product that
outputs a value ‘1’. A circuit with all variables in certain cases can
be simplified, eliminating redundancies and having its size reduced. A
Boolean function that implies a combination of minterms is called the
*implicant* of a function, and an implicant that cannot be reduced, that
is, does not imply another function, is called a *prime implicant*. The
sum of all implicants and prime implicants of a function is the set of
minterms for which the function’s result is ‘1’.

When representing an FSM, usually are used words or letters to refer to
states, since the number of flip-flops needed to represent an FSM is
calculated similarly to the number of rows in the truth table. When
assigning a value to a state, each literal symbolizes the value that
will be delivered to a respective flip-flop at a given time. *The
joining of the values of each flip-flop is equivalent to the value
assigned to a given state of the FSM*.

The values present in the memory element, when combined, represent the
current state. The flip-flops are then connected in combinational
circuits that change the value contained in the flip-flop at each clock
pulse, making the flip-flops start to represent the value assigned to
the next state of the machine, going from the current state to the next
state.

The combinational circuit responsible for this change of states is the
result of simplifying the expressions obtained from the inputs of a
given flip-flop and the stimulus that will be given. The circuit
receives the flip-flop output value and the machine state stimulus
value. The set of output values represent the next state that the state
machine will assume.

The state assignment is fundamental when there is the intention to
optimize, as it is directly linked to the size of the expression that
will make the change between the current state and the next state.
Changing the distribution of values drastically affects the size of the
expression, which consequently increases the size of the circuit.

For instance, a 7-state FSM, where the assignment of values to the
states is done sequentially, from 0 to 6 with numbers on a binary basis.
Table [\[tab:estados1\]][1] shows the arrangement of assigning values to
states. The state transition diagram is depicted in Fig.
[\[fig:ex1\]][2].

<div id="tab:estados1">

|     |     |
|:---:|:---:|
|  0  | 000 |
|  1  | 001 |
|  2  | 010 |
|  3  | 011 |
|  4  | 100 |
|  5  | 101 |
|  6  | 110 |

First Assignment.

</div>
