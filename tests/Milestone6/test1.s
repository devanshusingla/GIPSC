.data



.text
.globl main
_add:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -0
	sw $t9, 8($fp)
	sw $t9, 12($fp)
	add $t9, $t9, $t9
	add $t8, $t9, $0
	sw $t9, 8($fp)
	sw $t9, 12($fp)
	sub $t9, $t9, $t9
	add $t7, $t9, $0
	li $a0 8
	li $v0 9
	syscall
	sw $t7, 0($v0)
	sw $t8, 4($v0)
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
	addi $sp, $sp, -8
	li $t6, 6
	# Swapping out reg $t5 for variable 4_y
	lw	$t5,-4($fp)
	add $t6, $t5, $0
	add $t4, $t5, $0
	# Swapping out reg $t3 for variable 4_x
	lw	$t3,-8($fp)
	add $t4, $t3, $0
	li $t2, 2
	add $t2, $t5, $0
	lw $t1, 0($t3)
	li $t0, 7
	li $t9, 11
	add $a0, $t0, $0
	add $a1, $t9, $0
	jal _add
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
