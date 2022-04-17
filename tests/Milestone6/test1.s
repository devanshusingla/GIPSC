.data
        message1: .asciiz "Enter the value of n: "
        message2: .asciiz ", "

        y: .word 0
           .byte 53 
           .word 1 
.text 
.globl main

        main: 
            li $t0, 5 
            la $t1, y
            sw $t0, 5($t1)

            # Displaying the message on console
            li $v0, 4 
            la $a0, message1
            syscall

            # Reading the value of n
            li $v0, 5
            syscall 
            addi $sp, $sp, -8
            sw $ra, 4($sp)
            sw $v0, 0($sp)

            # Setting up counter for loop
            li $s0, 0

        loop:
            # Checking for breaking the loop
            lw $v0, 0($sp)
            ble $v0, $s0 exit
            addi $s0, $s0, 1

            # Calling fib function in a loop
            xor $a0, $a0, $a0
            add $a0, $s0, $0
            jal fib  

            # Setting up for printing the numbers
            add $a0, $v0, $0
            li $v0, 1
            syscall 

            # Escaping from printing the last ','
            lw $v0, 0($sp)
            ble $v0, $s0 exit

            # Printing message 2 and starting the next iteration
            li $v0, 4
            la $a0, message2 
            syscall 
        
            j loop

        exit:    
            # Terminate the program
            lw $ra, 4($sp)
            add $sp, $sp, 8
            jr $ra 

        fib: 
            # Returning if the argument is 1 with value 1
            addi $t0, $0, 1
            bne $a0, $t0, Label1
            addi $v0, $0, 1
            jr $ra

        Label1:
            # Returning if argument is 2 with value 1 
            xor $t0, $t0, $t0
            addi $t0, $0, 2
            bne $a0, $t0, Label2
            addi $v0, $0, 1
            jr $ra 


        Label2:
            # Save the current values of registers in stack
            addi $sp, $sp, -12
            sw $ra, 8($sp)
            sw $a0, 4($sp)

            # Calculation of fib(n-1)
            addi $a0, $a0, -1
            jal fib

            # Saving the value in stack
            sw $v0, 0($sp)
            lw $a0, 4($sp)

            # Calculation of fib(n-2)
            addi $a0, $a0, -2
            jal fib

            # Adding the results and returning
            lw $t1, 0($sp)
            add $v0, $t1, $v0
            lw $ra, 8($sp)
            addi $sp, $sp, 12
            jr $ra 