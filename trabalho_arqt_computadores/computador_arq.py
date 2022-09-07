import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

disk.read(str('prog6.bin'))

print("Antes: ", mem.read_word(1))

clk.start([cpu])

print("Depois: ", mem.read_word(1))

""" print("Depois: ", mem.read_word(101))
print("Depois: ", mem.read_word(102))
print("Depois: ", mem.read_word(103))
print("Depois: ", mem.read_word(104))
print("Depois: ", mem.read_word(105))
print("Depois: ", mem.read_word(106))
print("Depois: ", mem.read_word(107)) 
print("Depois: ", mem.read_word(108))
print("Depois: ", mem.read_word(109))
print("Depois: ", mem.read_word(110))
print("Depois: ", mem.read_word(111))
print("Depois: ", mem.read_word(112))
print("Depois: ", mem.read_word(113))
print("Depois: ", mem.read_word(114)) 
print("Depois: ", mem.read_word(115))
print("Depois: ", mem.read_word(116))
print("Depois: ", mem.read_word(117))
print("Depois: ", mem.read_word(118))
print("Depois: ", mem.read_word(119))
print("Depois: ", mem.read_word(120))
print("Depois: ", mem.read_word(121)) 
print("Depois: ", mem.read_word(122))
print("Depois: ", mem.read_word(123))
print("Depois: ", mem.read_word(124))
print("Depois: ", mem.read_word(125))  """



