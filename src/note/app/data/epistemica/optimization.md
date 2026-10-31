# Optimization

> **Optimization models** are mathematical frameworks used to systematically find the best solution from a set of possible options, given specific constraints and objectives.
> 

> New Geometry → New Theory of Optimization !!!
> 

![image.png](../assets/note/epistemica/optimization/image.png)

## Catalog of Optimization Problems

> Here’s an updated table of **combinatorial optimization problems**, including **coin exchange problems** and similar ones, alongside their relations to other problems:
> 

| **Problem** | **Type** | **Description** | **Related Problems** | **Relation** |
| --- | --- | --- | --- | --- |
| **Traveling Salesman Problem (TSP)** | Routing | Find the shortest possible route visiting a set of cities and returning to the start. | Hamiltonian Cycle, Vehicle Routing Problem (VRP) | TSP is a generalization of the Hamiltonian Cycle problem. VRP extends TSP by adding constraints. |
| **Knapsack Problem** | Selection | Select a subset of items to maximize value without exceeding weight capacity. | Subset Sum, Bin Packing | Knapsack generalizes the subset sum problem. Bin Packing shares similar space allocation ideas. |
| **Subset Sum Problem** | Selection | Determine if a subset of a set of numbers sums up to a specific target value. | Knapsack Problem, Partition Problem | A special case of the knapsack problem. Related to partitioning sets into equal sums. |
| **Bin Packing Problem** | Packing | Pack objects of different sizes into a finite number of bins with minimum space. | Knapsack Problem, Subset Sum | Shares the selection and capacity ideas with knapsack; can be reduced to knapsack. |
| **Job Scheduling Problem** | Scheduling | Schedule tasks on machines to minimize completion time or delays. | Flow Shop Scheduling, TSP | Often relates to TSP for minimizing task completion sequence or routing. |
| **Vehicle Routing Problem (VRP)** | Routing | Determine optimal routes for multiple vehicles to service customers. | TSP, Bin Packing | Extends TSP with multiple routes and vehicles; similar packing ideas with constraints. |
| **Minimum Spanning Tree (MST)** | Graph-based | Find the tree that connects all vertices of a graph with the minimum edge sum. | Shortest Path, Steiner Tree | MST relates to Steiner Tree as a constrained version; a subproblem in shortest path algorithms. |
| **Maximum Flow Problem** | Flow Network | Maximize the flow of material through a network without exceeding capacities. | Minimum Cut, Assignment Problem | Dual to minimum cut problems; related to assignment problems in bipartite graphs. |
| **Assignment Problem** | Matching/Flow | Assign agents to tasks such that the total cost is minimized. | Maximum Flow, Linear Assignment | Can be formulated as a flow network problem; similar to matching in bipartite graphs. |
| **Hamiltonian Cycle Problem** | Graph-based | Find a cycle in a graph that visits every vertex exactly once. | TSP, Eulerian Path | A special case of TSP; differs from Eulerian path which traverses each edge once. |
| **Graph Coloring Problem** | Graph-based | Assign colors to vertices of a graph such that no two adjacent vertices share the same color. | Clique Problem, Scheduling | Closely related to the clique problem; also used in scheduling problems. |
| **Clique Problem** | Graph-based | Find the largest subset of vertices such that every two vertices are connected. | Graph Coloring, Independent Set | Dual to independent set; used in graph coloring problems. |
| **Steiner Tree Problem** | Graph-based | Find the shortest network of edges connecting a subset of nodes in a graph. | MST, TSP | Generalizes MST, with additional non-terminal nodes to be included for shorter connections. |
| **Set Cover Problem** | Covering | Find the smallest subset of sets that covers all elements of a universal set. | Vertex Cover, Hitting Set | Vertex cover is a special case; can be reduced to a hitting set problem. |
| **Vertex Cover Problem** | Covering | Find the smallest subset of vertices such that each edge in the graph has at least one endpoint in the subset. | Set Cover, Independent Set | A special case of set cover; complementary to the independent set problem. |
| **Independent Set Problem** | Graph-based | Find the largest subset of vertices where no two vertices are adjacent. | Clique Problem, Vertex Cover | Dual to the clique problem; complementary to the vertex cover problem. |
| **Partition Problem** | Partitioning | Partition a set of numbers into two subsets with equal sum. | Subset Sum, Knapsack | Related to subset sum and a variant of the knapsack problem. |
| **Facility Location Problem** | Location | Choose facility locations to minimize the cost of serving a set of clients. | K-Median, Set Cover | Closely related to the k-median problem; can be approached similarly to set cover problems. |
| **K-Median Problem** | Clustering/Location | Find k centers such that the sum of distances from each point to its nearest center is minimized. | Facility Location, K-Means Clustering | Related to facility location problems, clustering, and k-means. |
| **K-Means Clustering** | Clustering | Partition a set of points into k clusters, minimizing intra-cluster variance. | K-Median, Facility Location | Similar to k-median, but focuses on minimizing variance within clusters. |
| **Coin Change Problem** | Change-making | Determine the minimum number of coins required to make a specific sum from given denominations. | Knapsack, Subset Sum, Partition Problem | Related to knapsack; finding the minimum set of denominations is like a subset sum with repetition. |
| **Unbounded Knapsack Problem** | Selection | Select items to maximize value without exceeding a capacity, where items can be chosen infinitely. | Coin Change, Knapsack | Similar to knapsack but allows infinite items; coin change is an application of this. |
| **Change-making with Limited Coins** | Change-making | Determine if a specific sum can be made from a set of coin denominations with limited quantities. | Subset Sum, Partition Problem | Generalized version of coin change with limited quantities; similar to knapsack with constraints. |
| **Weighted Set Cover Problem** | Covering | Minimize the weight of sets used to cover a universal set. | Set Cover, Knapsack | Weighted version of set cover; shares optimization principles with knapsack. |
| **Hitting Set Problem** | Covering | Find the smallest subset that intersects all sets in a collection. | Set Cover, Vertex Cover | Hitting set is closely related to set cover; both cover elements, but hitting set focuses on intersecting. |
| **Rod Cutting Problem** | Optimization | Maximize the value obtained by cutting a rod into pieces, considering price per length. | Knapsack, Unbounded Knapsack | Related to knapsack since it involves optimizing value with infinite cuts; unbounded knapsack variant. |
| **Weighted Bipartite Matching** | Matching/Flow | Find the matching in a bipartite graph that maximizes (or minimizes) a weighted sum. | Assignment Problem, Maximum Flow | Closely related to assignment problems and max flow in bipartite graphs. |
| … | .. | … | … | .. |

## Frameworks

> Here is a table summarizing various mathematical optimization models, their descriptions, and applications, including the general concept of mathematical optimization:
> 

| **Optimization Model** | **Description** | **Applications** |
| --- | --- | --- |
| **Mathematical Optimization** | Finding the best solution from a set of feasible solutions, given constraints, and an objective function. | Engineering, economics, logistics, machine learning |
| **Linear Programming (LP)** | Optimizes a linear objective function subject to linear equality and inequality constraints. | Operations research, supply chain management, finance |
| **Integer Programming (IP)** | Similar to linear programming, but with the added constraint, decision variables must be integer values. | Scheduling, facility location, resource allocation |
| **Mixed-Integer Linear Programming (MILP)** | Combines linear and integer programming, allowing some variables to be continuous and others to be integer. | Manufacturing, transportation, energy management |
| **Nonlinear Programming (NLP)** | Optimizes nonlinear objective functions subject to constraints, often requiring iterative methods. | Engineering design, economics, energy systems |
| **Quadratic Programming (QP)** | Optimizes quadratic objective functions subject to linear constraints. | Portfolio optimization, machine learning, control systems |
| **Convex Optimization** | Focuses on optimizing convex objective functions over convex domains. | Machine learning, signal processing, engineering design |
| **Network Optimization** | I find optimal flows through a network, such as transportation or communication networks. | Traffic management, telecommunications, logistics |
| **Multi-Objective Optimization (MOO)** | Considers multiple conflicting objectives to find a set of Pareto-optimal solutions. | Environmental management, finance, engineering |
| **Stochastic Programming** | Incorporates uncertainty into optimization models using probability distributions to model uncertain parameters. | Financial planning, energy planning, supply chain management |
| **Dynamic Programming** | Solves problems by breaking them into smaller subproblems and finding an optimal sequence of decisions. | Inventory control, finance, operations research |
| **Combinatorial Optimization** | Deals with discrete decision variables, seeking optimal solutions in problems like traveling salesman and knapsack. | Logistics, network design, resource allocation |
| **Robust Optimization** | Focuses on finding solutions that perform well under various uncertain scenarios. | Supply chain management, finance, engineering |
| **Goal Programming** | Handles multiple objectives by minimizing the deviations from specified goal levels. | Corporate planning, resource allocation, finance |
| **Constraint Programming** | Solves optimization problems by modeling them as a set of constraints that must be satisfied. | Scheduling, planning, resource allocation |
| **Game Theory** | Studies decision-making in competitive or cooperative situations, aiming to find optimal strategies. | Economics, political science, evolutionary biology |
| **Simulated Annealing** | A stochastic optimization technique inspired by the annealing process in metallurgy. | Global optimization, scheduling, circuit design |
| **Genetic Algorithms** | Evolutionary algorithms are inspired by natural selection to evolve potential solutions over generations. | Optimization in engineering, biology, artificial intelligence |
| **Particle Swarm Optimization** | Simulates the social behavior of birds or fish to optimize objective functions by iteratively adjusting a population of solutions. | Optimization in robotics, neural network training, control systems |
| **Ant Colony Optimization** | The foraging behavior of ants inspired me to find optimal paths through graphs or networks. | Network routing, logistics, and vehicle routing problems |
| **Firefly Algorithm** | It uses the flashing behavior of fireflies to optimize solutions by adjusting the brightness of fireflies based on attractiveness and distance. | Optimization in engineering, clustering, image processing |

## Methods

- https://en.wikipedia.org/wiki/Hill_climbing
- https://en.wikipedia.org/wiki/Minimax
- https://en.wikipedia.org/wiki/Gradient_descent
- https://en.wikipedia.org/wiki/Simulated_annealing
- https://en.wikipedia.org/wiki/Differential_evolution
- https://en.wikipedia.org/wiki/Pattern_search_(optimization)
- https://en.wikipedia.org/wiki/Particle_swarm_optimization
- https://en.wikipedia.org/wiki/Tabu_search
- https://en.wikipedia.org/wiki/Newton's_method
- https://en.wikiversity.org/wiki/Whale_Optimization_Algorithm
- https://en.wikipedia.org/wiki/Beam_search
- https://en.wikipedia.org/wiki/Artificial_bee_colony_algorithm
- https://en.wikipedia.org/wiki/Particle_swarm_optimization
- https://en.wikipedia.org/wiki/Multi-objective_optimization
- https://en.wikipedia.org/wiki/Bat_algorithm
- https://en.wikipedia.org/wiki/Conjugate_gradient_method
- https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms

## Conceptual Model

Conceptual Model: Optimization

## References

- [Satisficing](https://en.wikipedia.org/wiki/Satisficing)
- [Pareto Front](https://en.wikipedia.org/wiki/Pareto_front)
- [Decision Making](https://en.wikipedia.org/wiki/Decision-making)
- [Optimality model](https://en.wikipedia.org/wiki/Optimality_model)
- [Decision Analysis](https://en.wikipedia.org/wiki/Decision_analysis)
- [Optimization Problem](https://en.wikipedia.org/wiki/Optimization_problem)
- [Cost-Benefit Analysis](ttps://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis)
- [Optimal Foraging Theory](https://en.wikipedia.org/wiki/Optimal_foraging_theory)
- [Mathematical Optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Multi-Objective Optimization](https://en.wikipedia.org/wiki/Multi-objective_optimization)
- https://en.wikipedia.org/wiki/Dynamic_programming
- https://en.wikipedia.org/wiki/Change-making_problem
- https://en.wikipedia.org/wiki/Combinatorial_optimization
- https://en.wikipedia.org/wiki/Category:Combinatorial_optimization
- https://en.wikipedia.org/wiki/List_of_metaphor-based_metaheuristics
- Du, D., Pardalos, P. M., Hu, X., & Wu, W. (2022). Introduction to combinatorial optimization. Cham, Switzerland: Springer.
- Schrijver, A. (2005). On the History of Combinatorial Optimization (till 1960). *Handbook of Discrete Optimization/Elsevier*.
- Khuri, S., Bäck, T., & Heitkötter, J. (1994, March). An Evolutionary Approach to Combinatorial Optimization Problems. In ACM Conference on Computer Science (pp. 66-73).
- Wiley Encyclopedia in Operations Research and Management Science, Wiley, 2011.
- Combinatorial Optimization: Theory and Algorithms. B. Korte and J. Vygen. 5th edition. Springer (2012).
- Combinatorial Optimization. W. Cook, W.H. Cunningham, W.R. Pulleyblank, A. Schrijver. Wiley (1998).
- Integer and Combinatorial Optimization. G.L. Nemhauser and L.A. Wolsey. Wiley (1988).
- Integer Programming. L.A. Wolsey. Wiley (1998).
- Ren, Y., Lu, X., Guo, H., Xie, Z., Zhang, H., & Zhang, C. (2023). A review of combinatorial optimization problems in reverse logistics and remanufacturing for end-of-life products. Mathematics, 11(2), 298.
- http://titan.princeton.edu/TestProblems/index.html
- [Geometry](note.html?n=epistemica/mathematical/geometry/geometry.md)
- https://en.wikipedia.org/wiki/Change-making_problem
- [**M**AT 168 Optimization] [https://video.ucdavis.edu/channel/MAT+168+Optimization+(Matthias+Köppe%3B+Winter+2024)/329241352](https://video.ucdavis.edu/channel/MAT+168+Optimization+%28Matthias+K%C3%B6ppe%3B+Winter+2024%29/329241352)
