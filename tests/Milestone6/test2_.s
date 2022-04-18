.data


	_0_pre: .word 0

	_0_a: .word 0
	_0_arr: .word 0, 0, 0


.text

.globl main

__GLOBAL__:
	li $t0, 7
	addi $t1, $t0, 3
	add $a0, $t1, $0
	li $v0, 1
	syscall 
	jr $ra

main:
	jal __GLOBAL__
	li $a0, 1
	jal __0_pre
	j __exit

__0_pre:
	li $v0, 1
    syscall 
	jr $ra

__exit:
	li $v0, 10
    syscall 


	


