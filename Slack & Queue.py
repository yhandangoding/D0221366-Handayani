#Stack
def bikin_stack () :
		stack = [38,39,40]
		return stack
		
def periksa_empty ( stack ) :
		return len (stack) == 0
		
def push ( stack,item ):
		stack.append (item)
		print ("ukuran sepatu yang dikembalikan:",item)
		
def pop (stack) :
		if (periksa_empty (stack)) :
			return print ("ukuran sepatu pada rak kosong")
		print ("ukuran sepatu yang diambil:",stack.pop())
		
def size (stack) :
		print ("jumlah sepatu pada rak:" ,len(stack))
		
def top (stack):
		top = len (stack) -1
		if top < 0 :
			print (" tidak terdefenisi")
		else :
			print ("ukuran sepatu yang teratas:" , stack [top])
			
def tampilkan (stack) :
		print (stack)
		
			
s = bikin_stack ()
print (" tumpukan ukuran sepatu pada rak ")


#Data awal stack
print ("ukuran sepatu yang yang berada pada tumpukan saat ini:  ",s) 

size (s)
top (s)
print ()

#Meminjam ukuran sepatu
pop (s)
pop (s)
pop (s)
print ("ukuran sepatu yang yang berada pada tumpukan saat ini:  ",s) 
top (s)
size (s)
print ()

#Mengembalikan ukuran sepatu
push (s,input())
push (s,input())
push (s,input ())
print ("ukuran sepatu yang yang berada pada tumpukan saat ini:  ",s)

#Queue
queue = []
max_size = int(input("Masukkan Ukuran Maksimal Queue: "))

def isEmpty():
	if len(queue) == 0:
		print("Queue Kosong.")
		return True
	return False
	
def isFull():
	if len(queue) == max_size:
		print("Queue Penuh.")
		return True
	return False
		
def dequeue():
	if isEmpty() == False:
		print(queue.pop(0), "terhapus dari queue.")

def enqueue():
	if isFull() == False:
		x = input("Masukkan Antrian Baru: ")
		queue.append(x)
		print(x, "ditambahkan ke queue.")

p = 0
while p != '6':
    print('''\n1. Enqueue => Menambah Antrian
2. Dequeue => Menghapus dari Antrian
3. Full => Memeriksa Apakah Queue Penuh
4. Size => Melihat Ukuran Queue''')
    p = input("Ketik 6 untuk berhenti\nMasukkan Perintah: ")
    print()
    
    if p == '1':
    	enqueue()
    elif p == '2':
    	dequeue()
    elif p == '3':
    	if isFull() == False:
    		print("Queue belum penuh.")
    elif p == '4':
    	print("Ukuran queue saat ini: ", len(queue), "\nUkuran maksimal queue: ", max_size)