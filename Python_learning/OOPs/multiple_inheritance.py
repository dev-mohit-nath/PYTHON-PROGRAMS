class A:
    varA =  "This is class A variable"
class B:
    varB = "This is class B variable"
class C(A, B):
    varC = "This is class C variable"
c_instance = C()
print(c_instance.varA)  # Accessing variable from class A
print(c_instance.varB)  # Accessing variable from class B
print(c_instance.varC)  # Accessing variable from class C