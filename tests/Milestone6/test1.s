.data



.text
.globl main
_add:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -0
	sw $t8, 8($fp)
	sw $t7, 12($fp)
	add $t9, $t8, $t7
	add $t6, $t9, $0
	sw $t4, 8($fp)
	sw $t3, 12($fp)
	sub $t5, $t4, $t3
	add $t2, $t5, $0
	li $a0 8
	li $v0 9
	syscall
	sw $t2, 0($v0)
	sw $t6, 4($v0)
	addi $v1, $0, 8
	jr $ra
	_return_add:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
main:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -16
	li $t1, 6
	sw $t1, -4($fp)
	la $t0, -4($fp)
	sw $t0, -8($fp)
	li $t9, 2
	sw $t9, -4($fp)
	li $t8, 7
	li $t7, 11
	add $a0, $t8, $0
	add $a1, $t7, $0
	jal _add
	lw $t5, 0($v0)
	lw $t5, -12($fp)
	lw $t4, 4($v0)
	lw $t4, -16($fp)
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
