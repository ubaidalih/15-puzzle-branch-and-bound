from sympy import false, true
from priorityQueue import PriorityQueue, Node
from copy import deepcopy
import sys

def lokasi(matriks, x) :
    for i in range (4) :
        for j in range (4) :
            if matriks[i][j] == x :
                return 4*i+j

def kurang(matriks, i) :
    count = 0
    for j in range (1, i):
        if lokasi(matriks, i) < lokasi(matriks, j):
            count += 1
    return count

def totalKurang(node) :
    sum = 0
    for i in range (1, 17):
        sum += kurang(node.matrix, i)
    if (node.block_pos[0] - node.block_pos[1]) % 2 != 0 :
        sum += 1
    return sum

def cost(node):
    count=0
    for i in range (4):
        for j in range (4):
            if node.matrix[i][j] != 4*i + j + 1 and node.matrix[i][j] != 0:
                count+=1
    node.cost = count + node.level

def isSolution(node):
    solution = true
    for i in range (4) :
        for j in range (4) :
            if(node.matrix[i][j] != 4*i+j+1) :
                solution = false
    return solution

def printNode(node):
    print("Urutan Pencarian : " + str(node.id))
    print("Cost : " + str(node.cost))
    print("Level : " + str(node.level))
    for i in range (21) :
        print("-", end="")
    print("")
    for i in range (4) :
        for j in range (4) :
            print("|", end="")
            if(node.matrix[i][j] >= 10):
                if node.matrix[i][j] == 16 :
                    print("  -", end=" ")  
                else :
                    print(" " + str(node.matrix[i][j]), end=" ")
            else :
                print("  " + str(node.matrix[i][j]), end=" ")        
        print("|", end="\n")
        for i in range (21) :
            print("-", end="")
        print("")
    print("")

def printSolution(node):
    listNode = []
    while node.parent != None :
        listNode.append(node)
        node = node.parent
    listNode.append(node)
    for i in range (len(listNode)-1, -1, -1):
        printNode(listNode[i])
    sys.exit()

def nextNode(node):
    global id
    global pq
    if node.block_pos[0] != 0 and (node.parent == None or (node.parent).block_pos != [node.block_pos[0]-1, node.block_pos[1]]):
        id+=1
        newNodeMatrix1 = deepcopy(node.matrix)
        newNodeMatrix1[node.block_pos[0]][node.block_pos[1]] = node.matrix[node.block_pos[0]-1][node.block_pos[1]]
        newNodeMatrix1[node.block_pos[0]-1][node.block_pos[1]] = 16
        newNode = Node(node, id, newNodeMatrix1, 0, [node.block_pos[0] - 1, node.block_pos[1]], node.level + 1)
        cost(newNode)
        if isSolution(newNode):
            print("Solusi ditemukan")
            printSolution(newNode)
        pq.push(newNode)
    if node.block_pos[1] != 3 and (node.parent == None or (node.parent).block_pos != [node.block_pos[0], node.block_pos[1]+1]):
        id+=1
        newNodeMatrix2 = deepcopy(node.matrix)
        newNodeMatrix2[node.block_pos[0]][node.block_pos[1]] = node.matrix[node.block_pos[0]][node.block_pos[1]+1]
        newNodeMatrix2[node.block_pos[0]][node.block_pos[1]+1] = 16
        newNode = Node(node, id, newNodeMatrix2, 0, [node.block_pos[0], node.block_pos[1]+1], node.level + 1)
        cost(newNode)
        if isSolution(newNode):
            print("Solusi ditemukan")
            printSolution(newNode)
        pq.push(newNode)
    if node.block_pos[0] != 3 and (node.parent == None or (node.parent).block_pos != [node.block_pos[0]+1, node.block_pos[1]]):
        id+=1
        newNodeMatrix3 = deepcopy(node.matrix)
        newNodeMatrix3[node.block_pos[0]][node.block_pos[1]] = node.matrix[node.block_pos[0]+1][node.block_pos[1]]
        newNodeMatrix3[node.block_pos[0]+1][node.block_pos[1]] = 16
        newNode = Node(node, id, newNodeMatrix3, 0, [node.block_pos[0] + 1, node.block_pos[1]], node.level + 1)
        cost(newNode)
        if isSolution(newNode):
            print("Solusi ditemukan")
            printSolution(newNode)
        pq.push(newNode)
    if node.block_pos[1] != 0 and (node.parent == None or (node.parent).block_pos != [node.block_pos[0], node.block_pos[1]-1]):
        id+=1
        newNodeMatrix4 = deepcopy(node.matrix)
        newNodeMatrix4[node.block_pos[0]][node.block_pos[1]] = node.matrix[node.block_pos[0]][node.block_pos[1]-1]
        newNodeMatrix4[node.block_pos[0]][node.block_pos[1]-1] = 16
        newNode = Node(node, id, newNodeMatrix4, 0, [node.block_pos[0], node.block_pos[1]-1], node.level + 1)
        cost(newNode)
        if isSolution(newNode):
            print("Solusi ditemukan")
            printSolution(newNode)
        pq.push(newNode)

pq = PriorityQueue()
id = 1
initial_matrix = [[1,2,3,4],[5,6,16,8],[9,10,7,11],[13,14,15,12]]
root = Node(None, id, initial_matrix, 0, [1,2], 0)
cost(root)
pq.push(root)
if(totalKurang(root) % 2 == 0):
    while(not pq.empty()):
        node = pq.pop()
        if isSolution(node):
            print("Solusi ditemukan")
            break
        nextNode(node)
else :
    print("Tidak ada solusi yang mungkin")


