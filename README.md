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
