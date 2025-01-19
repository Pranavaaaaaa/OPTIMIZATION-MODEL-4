# OPTIMIZATION-MODEL-4

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: PRANAV A

**INTERN ID**: CT08JDC

**DOMIAN**: DATA SCIENCE

**BATCH DURATION**: JANUARY 5TH,2025 to FEBRUARY 5TH,2025

**MENTOR NAME**: NEELA SANTHOSH KUMAR

#DESCRIPTION ON THE PROJECT

Overview
This project focuses on optimizing logistics and supply chain operations using linear programming techniques implemented in Python. The problem addresses how a company can minimize transportation costs while meeting customer demands and adhering to supply constraints from multiple warehouses. The solution uses the PuLP library, a popular optimization library in Python, to formulate and solve the optimization problem.

Problem Statement
The company operates two warehouses that supply products to three customers. Each warehouse has a fixed supply limit, and each customer has specific demand requirements. The objective is to determine the optimal number of units to ship from each warehouse to each customer such that:

Customer demands are met.
Warehouse supply limits are not exceeded.
The total transportation cost is minimized.
Data
The input data for the project includes:

Transportation Costs: Cost per unit to ship from each warehouse to each customer.
Supply: Maximum number of units available at each warehouse.
Demand: Number of units required by each customer.
Example data:

Warehouse/Customer	Customer A	Customer B	Customer C	Supply
Warehouse 1	$4/unit$	$3/unit$	$6/unit$	$200$
Warehouse 2	$5/unit$	$7/unit$	$4/unit$	$300$
Demand	$180$	$120$	$150$	
Approach
The problem is modeled as a linear programming (LP) problem:

Decision Variables: Represent the number of units shipped from each warehouse to each customer.
Objective Function: Minimize the total transportation cost.
Constraints:
Supply constraints ensure that shipments from a warehouse do not exceed its capacity.
Demand constraints ensure that customer demands are fully met.
The PuLP library is used to define the LP problem, specify constraints and objectives, and solve it using the CBC solver.

Implementation
Problem Formulation: The optimization problem is defined using mathematical equations. Decision variables represent the shipments, while constraints and costs are encoded into the model.
Solution: The solver determines the optimal shipments from each warehouse to each customer, minimizing costs.
Visualization: Results are visualized using Matplotlib and Seaborn. A bar chart represents the shipments, and a heatmap illustrates transportation costs.
Results
The solver provided the following optimal solution:

Warehouse 1 ships:
80 units to Customer A.
120 units to Customer B.
0 units to Customer C.
Warehouse 2 ships:
100 units to Customer A.
0 units to Customer B.
150 units to Customer C.
Total Transportation Cost: $1780.00.
Insights
The optimization reduced costs by leveraging low-cost routes while ensuring all constraints were satisfied.
Warehouses efficiently distributed their supplies to meet demands.
Visualization aids in understanding shipment patterns and cost structures.
Conclusion
This project demonstrates the power of linear programming in solving real-world logistics challenges. By automating the decision-making process, companies can achieve cost-effective operations and meet customer demands efficiently. The methodology can be extended to more complex scenarios involving additional warehouses, customers, and constraints.
