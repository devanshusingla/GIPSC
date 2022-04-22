.data



.text
.globl main

_add:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -0
	add $t9, $a0, $a1
	add $t8, $t9, $0
	sub $t7, $a0, $a1
	add $t6, $t7, $0
	li $a0 8
	li $v0 9
	syscall
	sw $t6, 0($v0)
	sw $t8, 4($v0)
	addi $v1, $0, 8
	jr $ra
	_return_add:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
main:
	addi $sp, $sp, -128
	add $fp, $sp, $0
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -16
	li $t5, 6
	sw $t5, -4($fp)
	la $t4, -4($fp)
	sw $t4, -8($fp)
	li $t3, 2
	sw $t3, -4($fp)
	li $t2, 7
	li $t1, 11
	add $a0, $t2, $0
	add $a1, $t1, $0
	jal _add
	lw $t0, 0($v0)
	lw $t0, -12($fp)
	lw $t9, 4($v0)
	lw $t9, -16($fp)
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	li $v0 10
	syscall
