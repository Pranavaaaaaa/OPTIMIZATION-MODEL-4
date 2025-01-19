from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Step 1: Define the problem
problem = LpProblem("Logistics_Optimization", LpMinimize)

# Step 2: Define decision variables
# Variables represent units shipped from each warehouse to each customer
x11 = LpVariable("Ship_W1_to_A", lowBound=0, cat="Continuous")
x12 = LpVariable("Ship_W1_to_B", lowBound=0, cat="Continuous")
x13 = LpVariable("Ship_W1_to_C", lowBound=0, cat="Continuous")
x21 = LpVariable("Ship_W2_to_A", lowBound=0, cat="Continuous")
x22 = LpVariable("Ship_W2_to_B", lowBound=0, cat="Continuous")
x23 = LpVariable("Ship_W2_to_C", lowBound=0, cat="Continuous")

# Step 3: Define the objective function (Minimize transportation costs)
costs = {
    (1, "A"): 4, (1, "B"): 3, (1, "C"): 6,
    (2, "A"): 5, (2, "B"): 7, (2, "C"): 4
}
problem += (
    costs[(1, "A")] * x11 + costs[(1, "B")] * x12 + costs[(1, "C")] * x13 +
    costs[(2, "A")] * x21 + costs[(2, "B")] * x22 + costs[(2, "C")] * x23
), "Total_Transportation_Cost"

# Step 4: Define constraints
# Supply constraints
problem += x11 + x12 + x13 <= 200, "Supply_Warehouse_1"
problem += x21 + x22 + x23 <= 300, "Supply_Warehouse_2"

# Demand constraints
problem += x11 + x21 >= 180, "Demand_Customer_A"
problem += x12 + x22 >= 120, "Demand_Customer_B"
problem += x13 + x23 >= 150, "Demand_Customer_C"

# Step 5: Solve the problem
status = problem.solve()

# Step 6: Display results
print(f"Status: {problem.status}")
print(f"Units shipped from Warehouse 1 to Customer A: {x11.varValue}")
print(f"Units shipped from Warehouse 1 to Customer B: {x12.varValue}")
print(f"Units shipped from Warehouse 1 to Customer C: {x13.varValue}")
print(f"Units shipped from Warehouse 2 to Customer A: {x21.varValue}")
print(f"Units shipped from Warehouse 2 to Customer B: {x22.varValue}")
print(f"Units shipped from Warehouse 2 to Customer C: {x23.varValue}")
print(f"Total Transportation Cost: ${problem.objective.value()}")

import matplotlib.pyplot as plt
import numpy as np

# Data for visualization
warehouses = ["Warehouse 1", "Warehouse 2"]
customers = ["Customer A", "Customer B", "Customer C"]
shipments = [
    [80.0, 120.0, 0.0],  # Shipments from Warehouse 1
    [100.0, 0.0, 150.0],  # Shipments from Warehouse 2
]

# Plot a bar chart
x = np.arange(len(customers))  # Label positions for customers
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(8, 6))

# Bar plots for each warehouse
bar1 = ax.bar(x - width / 2, shipments[0], width, label=warehouses[0], color='blue')
bar2 = ax.bar(x + width / 2, shipments[1], width, label=warehouses[1], color='green')

# Add labels, title, and legend
ax.set_xlabel('Customers', fontsize=12)
ax.set_ylabel('Units Shipped', fontsize=12)
ax.set_title('Optimized Shipments from Warehouses to Customers', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(customers)
ax.legend()

# Annotate bars with values
for bar in bar1 + bar2:
    ax.annotate(f'{bar.get_height():.1f}',  # Annotate value
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position
                xytext=(0, 3),  # Offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

import seaborn as sns

# Transportation cost matrix
cost_matrix = [
    [4, 3, 6],  # Costs from Warehouse 1
    [5, 7, 4],  # Costs from Warehouse 2
]

# Create a heatmap
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(cost_matrix, annot=True, fmt=".0f", cmap="YlGnBu",
            xticklabels=customers, yticklabels=warehouses, ax=ax)

# Add labels and title
ax.set_title('Transportation Costs per Unit', fontsize=14)
ax.set_xlabel('Customers', fontsize=12)
ax.set_ylabel('Warehouses', fontsize=12)
plt.tight_layout()
plt.show()
