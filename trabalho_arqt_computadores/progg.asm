     goto main 
     wb 0        
    
a    ww 0      
b    ww 100      
c    ww 500
d    ww 4     
e    ww 400
f    ww 1
j    ww 0 

main x, c
     h, d
     div
     jz x, veri
     goto final2

veri x, c
     h, b
     div
     jz x, veri2
     goto final

veri2 x, c
      h, e
      div
      jz x, final
      goto final2
      
final x, f
      mov x, a
      halt

final2 x, j
       mov x, a
       halt