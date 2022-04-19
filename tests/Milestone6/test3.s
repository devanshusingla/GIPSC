.data




.text
.globl main
_inc:
	jr $ra
	li $a0 8
	li $v0 9
	syscall
	sw $t9, 0($v0)
	sw $t8, 4($v0)
	addi $v1, $0, 8
	jr $ra
	addi $sp, $sp, -4
	sw $t7 ($sp)
	jr $ra
main:
	addi $sp, $sp, -4
	sw $t7 ($sp)
	li $v0 10
	syscall
