.data


	_0_pre: .word 0



.text
.globl main
_Println:
	jr $ra
_f:
	jr $ra
main:
	addi $sp, $sp, -4
	sw $t9 ($sp)
	li $v0 10
	syscall
