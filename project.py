import random
import time

def bubbleSort(array1,n1):
	for i in range(n1-1):
		for j in range(i+1,n1):
			if array1[i]>array1[j]:
				temp = array1[i]
				array1[i] = array1[j]
				array1[j] = temp
	return array1

def selectionSort(array2,n2):
	for i in range(n2-1):
		index= i
		for j in range(i+1,n2):
			if array2[index] > array2[j]:
				index = j

		temp = array2[i]
		array2[i] = array2[index]
		array2[index] = temp
	return array2

n1 = int(input("Number to sort using bubble sort: "))
array1 = []
for i in range(n1):
	array1.append(int(random.random()*1000))
print("Unsorted array: ", array1)
array1 = bubbleSort(array1,n1)
print("Sorted Array: ", array1)

n2= int(input('Enter number to sort using selection sort: '))
array2=[]
for i in range(n2):
	array2.append(int(random.random()*1000))

print("Unsorted array:", array2)
array2 = selectionSort(array2,n2)
print("Sorted Array: ",array2)

#Bubble sort
n3 = int(input("Number n for the number of items in array to sort using bubble sort: "))
running_time = 0
for i in range(1000):
	array3 = []
	for j in range(n3):
		array3.append(int(random.random()*1000))
	end_time = time.time()
	bubbleSort(array3,n3)
	running_time += time.time() - end_time
print("Number of items: ", n3*1000)
print("Average running time: ", running_time/1000)

n4 = int(input("Number n for the number of items in array to sort using bubble sort: "))
running_time = 0
for i in range(500):
	array4 = []
	for j in range(n4):
		array4.append(int(random.random()*1000))
	r_time = time.time()
	bubbleSort(array4,n4)
	running_time += time.time() - r_time
print("Number of items: ", n4*500)
print("Average running time: ", running_time/500)

n5 = int(input("Number n for the number of items in array to sort using bubble sort: "))
running_time = 0
for i in range(2500):
	array5 = []
	for j in range(n5):
		array5.append(int(random.random()*1000))
	r_time = time.time()
	bubbleSort(array5,n5)
	running_time += time.time() - r_time
print("Number of items: ", n5*2500)
print("Average running time: ", running_time/2500)

n6 = int(input("Number n for the number of items in array to sort using bubble sort: "))
running_time = 0
for i in range(5000):
	array6 = []
	for j in range(n6):
		array6.append(int(random.random()*1000))
	r_time = time.time()
	bubbleSort(array6,n6)
	running_time += time.time() - r_time
print("Number of items: ", n6*5000)
print("Average running time: ", running_time/5000)

#Selection sort
n3 = int(input("Number n for the number of items in array to sort using selection sort: "))
running_time = 0
for i in range(1000):
	array3 = []
	for j in range(n3):
		array3.append(int(random.random()*1000))
	r_time = time.time()
	selectionSort(array3,n3)
	running_time += time.time() - r_time
print("Number of items: ", n3*1000)
print("Average running time: ", running_time/1000)

n4 = int(input("Number n for the number of items in array to sort using selection sort: "))
running_time = 0
for i in range(500):
	array4 = []
	for j in range(n4):
		array4.append(int(random.random()*1000))
	r_time = time.time()
	selectionSort(array4,n4)
	running_time += time.time() - r_time
print("Number of items: ", n4*500)
print("Average running time: ", running_time/500)

n5 = int(input("Number n for the number of items in array to sort using selection sort: "))
running_time = 0
for i in range(2500):
	array5 = []
	for j in range(n5):
		array5.append(int(random.random()*1000))
	r_time = time.time()
	selectionSort(array5,n5)
	running_time += time.time() - r_time
print("Number of items: ", n5*2500)
print("Average running time: ", running_time/2500)

n6 = int(input("Number n for the number of items in array to sort using selection sort: "))
running_time = 0
for i in range(5000):
	array6 = []
	for j in range(n6):
		array6.append(int(random.random()*1000))
	r_time = time.time()
	selectionSort(array6,n6)
	running_time += time.time() - r_time
print("Number of items: ", n6*5000)
print("Average running time: ", running_time/5000)
