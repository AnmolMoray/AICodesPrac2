from collections import defaultdict

jug1, jug2, aim = 2, 8, 6

visited = defaultdict(lambda: False)

def WaterJugProblem(amt1, amt2):
	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print(amt1, amt2)
		return True

	if visited[(amt1, amt2)] == False:
		print(amt1, amt2)
		visited[(amt1, amt2)] = True
		return (WaterJugProblem(0, amt2) or
				WaterJugProblem(amt1, 0) or
				WaterJugProblem(jug1, amt2) or
				WaterJugProblem(amt1, jug2) or
				WaterJugProblem(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				WaterJugProblem(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	else:
		return False
print("Steps: ")
if (jug1%2==0 and jug2%2==0):
	print("Solution could not found")
elif (aim>jug1 and aim>jug2):
	print("Solutio could not found")
else:
	a=WaterJugProblem(0, 0)
	if a==False:
		print("Solution not found")
