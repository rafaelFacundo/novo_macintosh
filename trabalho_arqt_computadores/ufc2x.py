from mailcap import findmatch
from wsgiref.validate import validator
import memory
from array import array

MPC = 0
MIR = 0

MAR = 0
MDR = 0
PC = 0
MBR = 0
X = 0
Y = 0
H = 0

N = 0
Z = 1
M = 0

BUS_A = 0
BUS_B = 0
BUS_C = 0

firmware = array('L', [0]) * 512

#main: PC <- PC + 1; MBR <- read_byte(PC); GOTO MBR
firmware[0] = 0b00000000010000110101001000001001
#b000000101
#X = X + mem[address]
##2: PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[2] = 0b00000001100000110101001000001001
##3: MAR <- MBR; read_word; GOTO 4
firmware[3] = 0b00000010000000010100100000010010
##4: H <- MDR; GOTO 5
firmware[4] = 0b00000010100000010100000001000000
##5: X <- H + X; GOTO 0
firmware[5] = 0b00000000000000111100000100000011  

#mem[address] = X
##6: PC <- PC + 1; fetch; GOTO 7
firmware[6] = 0b00000011100000110101001000001001
##7: MAR <- MBR; GOTO 8
firmware[7] = 0b00000100000000010100100000000010
##8: MDR <- X; write; GOTO 0
firmware[8] = 0b00000000000000010100010000100011

#goto address
##9: PC <- PC + 1; fetch; GOTO 10
firmware[9] =  0b00000101000000110101001000001001
##10: PC <- MBR; fetch; GOTO MBR
firmware[10] = 0b00000000010000010100001000001010

#if X = 0 then goto address
## 11: X <- X; IF ALU = 0 GOTO 268 (100001100) ELSE GOTO 12(000001100)
firmware[11] =  0b00000110000100010100000100000011
## 12: PC <- PC + 1; GOTO 0
firmware[12] =  0b00000000000000110101001000000001
## 268: GOTO 9
firmware[268] = 0b00000100100000000000000000000000

#X = X - mem[address]
##13: PC <- PC + 1; fetch; goto 14
firmware[13] = 0b00000111000000110101001000001001
##14: MAR <- MBR; read; goto 15
firmware[14] = 0b00000111100000010100100000010010
##15: H <- MDR; goto 16
firmware[15] = 0b00001000000000010100000001000000
##16: X <- X - H; goto 0
firmware[16] = 0b00000000000000111111000100000011

#halt:
firmware[255] = 0b00000000000000000000000000000000

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
 

#operação de multiplicação 
##2: PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[17] = 0b00001001000000110101001000001001
##3: MAR <- MBR; read_word; GOTO 4
firmware[18] = 0b00001001100000010100100000010010
##4: x <- MDR; GOTO 5
firmware[19] = 0b00001010000000010100000100000000

#pegando a proximo endereço de memoria
#PC <- PC + 1 ...
firmware[20] = 0b00001010100000110101001000001001

#pegando o endereço lido na instrução anterior e 
#colocando no MAR para ler a palavra nesse endereço
firmware[21] = 0b00001011000000010100100000010010

#pegando o valor do MRD e jogando no Y
firmware[22] = 0b00001011100000010100000010000000

#jogando x no H
firmware[23] = 0b00001100000000010100000001000011

#fazendo a multiplicação
firmware[24] = 0b00000000000000110010000100000011

firmware[25] = 0b00001101000000110101100000000010

firmware[26] = 0b00000000000000000000000000100000  

 


#operação de divisão 
#pc + 1 para pegar o endereço 
#firmware[27] = 0b00001110000000110101001000001001

#chamar a partir daqui

#zerando o valor de y 
firmware[28] = 0b00001110100000010000000010000000

#colocando 1 no mdr
firmware[29] = 0b00001111000000110001010000000000

#fazendo o shift de bits
firmware[30] = 0b00001111100011010100010000000000

firmware[31] = 0b00010000000010010100010000000000

firmware[32] = 0b00010000100011010100010000000000

firmware[33] = 0b00010001000011010100010000000000

#aqui o mdr tem 1 um e 31 zeros
firmware[34] = 0b00010001100011010100010000000000

#começo a verificação
firmware[35] = 0b00010010000000000000000000000000

#fazer um "e" com o valor do x para saber se ele é negativo
# primeiro pegar o H e colcoar no y  
firmware[36] = 0b00010010100000011000000010000000

 #colocando X no H 
firmware[37] = 0b00010011000000010100000001000011 


#fazendo o OR e colocando no MDR 
firmware[38] = 0b00010011100100001100000000000000

#após o OR vou subtrair o MDR menos o H para ver se o resultado 
# é zero
#firmware[37] = 0b000100110 01000111111010000000000 

#aqui eu faço a subtração de fato 
# primeiro eu vou colocar o divisor de volta no H 
#colocando o Y no H 
firmware[295] = 0b10010100000000010100000001000100

# agora vou fazer a subtração X - H (b - a)
firmware[296] = 0b10010100100000111111000100000011

#000100001
#incrementar o valor de Y(X), que é o contador
#mandao o microprograma de volta para a posição 35 para 
# verificar mais uma vez 
firmware[297] = 0b00010001100000110101000010000100

firmware[39] = 0b00010100000000010100000001000011 

firmware[40] = 0b00000000000000111100000100000100



# H <- mem
##2: PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[42] = 0b00010101100000110101001000001001
##3: MAR <- MBR; read_word; GOTO 4
firmware[43] = 0b00010110000000010100100000010010
##4: H <- MDR; GOTO 5
firmware[44] = 0b00000000000000010100000001000000  

# x <- mem
##2: PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[45] = 0b00010111000000110101001000001001		
##3: MAR <- MBR; read_word; GOTO 4
firmware[46] = 0b00010111100000010100100000010010
##4: X <- MDR; GOTO 5
firmware[47] = 0b00000000000000010100000100000000  

#operação raiz
#fazendo shift no mdr 
firmware[48] = 0b00011000100000110001010000000000 

firmware[49] = 0b00011001000011010100010000000000

firmware[50] = 0b00011001100010010100010000000000

firmware[51] = 0b00011010000011010100010000000000

firmware[52] = 0b00011010100011010100010000000000

firmware[53] = 0b00011011000011010100010000000000


#colocando h no y
firmware[54] = 0b00011011100000011000000010000000

#zerando o x 
firmware[55] = 0b00011100000000010000000100000011

#somando um ao x
firmware[56] = 0b00011100100000110101000100000011

#colocando x no h 
firmware[57] = 0b00011101000000010100000001000011

#fazendo H <- H * X (x * x)
firmware[58] = 0b00011101100000110010000001000011

#fazendo h <- y - h 
firmware[59] = 0b00011110000000111111000001000100

firmware[60] = 0b00011100001000001100000000000000 
#000110110
#100111011

firmware[312] = 0b00000000000000110110000100000011

#operação de menor que 
#chamar apartir daqui
#fazendo shift no mdr 
firmware[61] = 0b00011111000000110001010000000000

firmware[62] = 0b00011111100011010100010000000000

firmware[63] = 0b00100000000010010100010000000000

firmware[64] = 0b00100000100011010100010000000000

firmware[65] = 0b00100001000011010100010000000000

firmware[66] = 0b00100001100011010100010000000000

#verificando se o número é negativo
#colocando H no Y 
firmware[67] = 0b00100010000000011000000010000000

#coloando x no H
firmware[68] = 0b00100010100000010100000001000011 

#fazendo H(x) - y e colocando no H
firmware[69] = 0b00100011000000111111000001000100

#fazendo MDR & H pra ver se o número é negativo 
firmware[70] = 0b00100011101000001100000000000000 

# se for  positivo o H(x) é menor, vou colocar ele no x para pegar o 
# resultado 
firmware[71] = 0b00000000000000010100000100000011


firmware[327] = 0b00000000000000010100000100000100 



#operação de salvar em um endereço especifico
firmware[72] = 0b00100100100000010100010000000011

firmware[73] = 0b00000000000000011000100000100000






#halt:
firmware[255] = 0b00000000000000000000000000000000


def read_regs(reg_num):
	global MDR, PC, MBR, X, Y, H, BUS_A, BUS_B
	
	BUS_A = H
	
	if reg_num == 0:
		BUS_B = MDR
	elif reg_num == 1:
		BUS_B = PC
	elif reg_num == 2:
		BUS_B = MBR
	elif reg_num == 3:
		BUS_B = X
	elif reg_num == 4:
		BUS_B = Y
	else:
		BUS_B = 0
		
def write_regs(reg_bits):
	global MAR, MDR, PC, X, Y, H, BUS_C

	if reg_bits & 0b100000:
		MAR = BUS_C
		
	if reg_bits & 0b010000:
		MDR = BUS_C
		
	if reg_bits & 0b001000:
		PC = BUS_C
		
	if reg_bits & 0b000100:
		X = BUS_C
		
	if reg_bits & 0b000010:
		Y = BUS_C
		
	if reg_bits & 0b000001:
		H = BUS_C
		

def alu(control_bits):
	global N, Z, BUS_A, BUS_B, BUS_C
	
	a = BUS_A 
	b = BUS_B 
	o = 0
	
	shift_bits = control_bits & 0b11000000
	shift_bits = shift_bits >> 6
	
	control_bits = control_bits & 0b00111111
	
	if control_bits == 0b011000:
		o = a
	elif control_bits == 0b010100:
		o = b
	elif control_bits == 0b011010:
		o = ~a
	elif control_bits == 0b101100:
		o = ~b
	elif control_bits == 0b111100:
		o = a + b
	elif control_bits == 0b111101:
		o = a + b + 1
	elif control_bits == 0b111001:
		o = a + 1
	elif control_bits == 0b110101:
		o = b + 1
	elif control_bits == 0b111111:
		o = b - a
	elif control_bits == 0b110110:
		o = b - 1
	elif control_bits == 0b111011:
		o = -a
	elif control_bits == 0b001100:
		o = a & b
	elif control_bits == 0b011100:
		o = a | b
	elif control_bits == 0b010000:
		o = 0
	elif control_bits == 0b110001:
		o = 1
	elif control_bits == 0b110010:
		#o = -1
		o = a * b 
	
		
	if o == 0:
		N = 0
		Z = 1
	else:
		N = 1
		Z = 0
	
	if shift_bits == 0b01:
		o = o << 1
	elif shift_bits == 0b10:
		
		o = (o & 0b11111111111111111111111111111111) 
		o = o >> 1
	elif shift_bits == 0b11:
		o = o << 8
		
	BUS_C = o 
	
def next_instruction(next, jam):
	global MPC, MBR, N, Z
	
	if jam == 0b000:
		MPC = next 
		return
		
	if jam & 0b001:
		next = next | (Z << 8)
	
	if jam & 0b010:
		
		next = next | (N << 8)
		
	if jam & 0b100:
		next = next | MBR
		
	MPC = next
	
def memory_io(mem_bits):
	global PC, MBR, MDR, MAR
	
	if mem_bits & 0b001:
		MBR = memory.read_byte(PC)

	if mem_bits & 0b010:
		MDR = memory.read_word(MAR)
		
	if mem_bits & 0b100:
		memory.write_word(MAR, MDR)
		
def step():
	global MIR, MPC
	
	MIR = firmware[MPC]
	
	if MIR == 0:
		return False
		
	read_regs       ( MIR & 0b00000000000000000000000000000111)
	alu             ((MIR & 0b00000000000011111111000000000000) >> 12)
	write_regs      ((MIR & 0b00000000000000000000111111000000) >> 6)
	memory_io       ((MIR & 0b00000000000000000000000000111000) >> 3)
	next_instruction((MIR & 0b11111111100000000000000000000000) >> 23, (MIR & 0b00000000011100000000000000000000) >> 20)
	
	return True
