#break

i = 1
while i <= 10:
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    i += 1
    
print("end of loop")  # This will not be printed when the loop breaks

#continue
i = 1
while i <= 10:
    if  i == 5: # Skip the rest of the loop when i is 5
        i += 1 
        continue # Continue to the next iteration
    print(i)
    i += 1
print("end of loop")  # This will be printed after the loop completes   
i = 1
while i <= 20:
    if i%2 != 0: # Skip odd numbers
        i += 1  # Increment i to avoid infinite loop
        continue  # Skip the rest of the loop when i is 5
    print(i)
    i += 1