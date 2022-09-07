     goto main 
     wb 0        

k    ww 0
n    ww 100
r    ww 2
d    ww 100 
a    ww 1
j    ww 2

main x, n
     jz x, final 
     x, j
     sub x, r
     jz x, final2
     h, r
     x, j 
     div 
     jz x, final3
     x, r
     add x, a 
     mov x, r 
     goto main

final  x, j
       mov x, k
       halt 

final2 x, n 
       sub x, a 
       mov x, n
       jz x, final
       x, j 
       add x, a
       mov x, j
       x, a
       add x, a
       mov x, r
       goto main

final3 x, a
       add x, a 
       mov x, r
       x, j 
       add x, a
       mov x, j
       goto main