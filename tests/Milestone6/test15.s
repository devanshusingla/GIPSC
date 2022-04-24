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
	add $fp, $sp, $0
	addi $sp, $sp, -12
	li $a0, 12
	li $v0, 9
	syscall
	sw $v0, -12($fp)
	li $a0, 8
	sw $a0, 4($v0)
	sw $a0, 8($v0)
	li $t9, 0
	# $t9, temp_1
	li $t7, 4
	mult $t9, $t7
	mflo $t8
	add $t6, $t8, $0
	# Swapping out reg $t4 for variable 2_a
	# Changed 2_a
	lw	$t4,-12($fp)
	lw $t4, 0($t4)
	# $t6, temp_2
	add $t5, $t4, $t6
	add $t3, $t5, $0
	li $t2, 1
	# $t3, temp_3
	sw $t2, 0($t3)
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
