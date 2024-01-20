thisdict =	{
  "04": "-34",
  "03": "3455",
  "02": "+742687536",
  "01": "-7832649",
}
print(thisdict) 

print("Transaktionen gestern: ", len(thisdict))

numeric_values = [int(value) for value in thisdict.values()]

# Finde den Min- und Max-Wert
min_value = min(numeric_values)
max_value = max(numeric_values)

print("Min-Wert:", min_value)
print("Max-Wert:", max_value)