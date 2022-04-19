.data


	_0_pre: .word 0

	_0_a: .word 0
	_0_arr: .word 0, 0, 0


.text
.globl main
_Println:
	jr $ra
	jr $ra
main:
	li $v0 10
	syscall
