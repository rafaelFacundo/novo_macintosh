import memory
import clock
import ufc2x as cpu

#memory[50] = 21
#memory[100] = 3
#memory[130] = 10
""" memory.write_word(50, 21)
memory.write_word(100, 3)
memory.write_word(130, 10) """
memory.write_word(50,99999)
memory.write_word(60,32768)

memory.write_byte(1,78)
memory.write_byte(2,50)
memory.write_byte(3,48)

memory.write_byte(6,255)


""" #X <- X + memory[100]
memory.write_byte(1, 2)  #X <- X + memory
memory.write_byte(2, 100) #[100]

#IF X = 0 GOTO 7
memory.write_byte(3, 11) #IF X = 0 GOTO
memory.write_byte(4, 7) #7

#X <- X + memory[130]
memory.write_byte(5, 2)   #X <- X + memory
memory.write_byte(6, 130) #[130]

#X <- X + memory[50]
memory.write_byte(7, 2)   #X <- X + memory
memory.write_byte(8, 50) #[50]

#memory[150] <- X
memory.write_byte(9, 6)    #memory[?] <- X
memory.write_byte(10, 150) #? = 150 

#halt
memory.write_byte(11, 255) #halt """



clock.start([cpu])

print(memory.read_word(145))
