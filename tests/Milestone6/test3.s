.data




.text
.globl main
_inc:
	add $t9, $t8, $t7
	add $t6, $t9, $0
	add $t9, $t8, $t5
	add $t4, $t9, $0
	jr $ra
	li $a0 8
	li $v0 9
	syscall
	sw $, 0($v0)
	sw $, 4($v0)
	addi $v1, $0, 8
	jr $ra
	addi $sp, $sp, -4
	sw $t2 ($sp)
	jr $ra
main:
	addi $sp, $sp, -4
	sw $t2 ($sp)
	li $v0 10
	syscall
