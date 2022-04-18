.data




.text
.globl main
_inc:
	jr $ra
_main:
	li $v0 10
	syscall
