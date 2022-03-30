import branchandbound as bnb
from branchandbound import pq, done
from priorityQueue import Node
from time import time

fileName = input("Masukkan nama file : ")

start_time = time()
initial_matrix = bnb.readFile(fileName)
for i in range (4) :
    for j in range (4) :
        if(initial_matrix[i][j] == 16) :
            initial_block_pos = [i, j]
            break
root = Node(None, id, initial_matrix, 0, initial_block_pos, 0)
bnb.cost(root)
pq.push(root)
if(bnb.totalKurang(root) % 2 == 0):
    while(not pq.empty() and not done):
        node = pq.pop()
        if bnb.isSolution(node):
            print("Solusi ditemukan")
            break
        bnb.nextNode(node)
else :
    print("Tidak ada solusi yang mungkin")

end_time = time()
print("Waktu Eksekusi : " + str(end_time - start_time)+ " detik")
