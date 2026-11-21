# Cyclomatic complexity for one connected flow graph: M = E - N + 2
E = int(input("Edges (E): "))
N = int(input("Nodes (N): "))
P = int(input("Connected components (P, usually 1): "))
print("Cyclomatic complexity =", E - N + 2 * P)
