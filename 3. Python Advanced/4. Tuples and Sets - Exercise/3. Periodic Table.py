input_lines = int(input())


elements = set()
for _ in range(input_lines):
    elements.update(input().split())  # Simplified loop

print("\n".join(elements))