def print_list(list ,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print_list(fruits)  # Recursive call to print the next element