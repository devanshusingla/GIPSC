.data



.text
.globl main

main:
	addi $sp, $sp, -128
	add $fp, $sp, $0
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -4
	li $t9, 6
	sw $t9, -4($fp)
	li $t8, 11
	li $t7, 97
	add $a0, $t7, $0
	li $v0, 11
	syscall
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	li $v0 10
	syscall
