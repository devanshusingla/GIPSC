.data



.text
.globl main
_inc:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -4
	li $t9, 6
<<<<<<< HEAD
	sw $t8, 8($fp)
	add $t8, $t8, $t9
	add $t7, $t8, $0
	sw $t6, 8($fp)
	li $t5, 5
<<<<<<< HEAD
	sw	$t4,-24($fp)

	sw $t4, 0($fp)
	sw	$t3,-28($fp)

	lw $t7, 8($fp)
	add $t8, $t7, $t9
	add $t6, $t8, $0
	sw $t5, 8($fp)
	li $t4, 5
	sw $t4, -4($fp)

	li $t3, 3
	lw $t1, 8($fp)
	add $t2, $t1, $t3
	add $t0, $t2, $0
	li $a0 8
	li $v0 9
	syscall
	sw $t0, 0($v0)
	# Swapping out reg $t8 for variable 2_z
	lw	$t8,-4($fp)
	sw $t8, 4($v0)
	addi $v1, $0, 8
	jr $ra
	_return_inc:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
main:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -44
	li $t7, 5
	add $a0, $t7, $0
	jal _inc
	sw	$t9,0($sp)

	lw $t9, 0($v0)
	lw $t9, -4($fp)
	sw	$t6,0($sp)

	lw $t6, 4($v0)
	lw $t6, -8($fp)
	sw	$t5,0($sp)

	li $t5, 6
	sw $t5, -12($fp)
	sw	$t4,0($sp)

	la $t4, -12($fp)
	sw $t4, -16($fp)
	li $t2, 2
	sw $t2, -12($fp)
	la $t1, -12($fp)
	sw	$t3,0($sp)

	lw $t3, 0($t1)
	sw	$t0,0($sp)

	li $t0, 4
	sw	$t8,0($sp)

	la $t8, -12($fp)
	sw $t8, -20($fp)
	sw	$t7,0($sp)

	# Swapping out reg $t9 for variable 4_g
	lw	$t9,-20($fp)
	lw $t7, 0($t9)
	add $t6, $t7, $0
	lw $s7, 0($t6)
	li $s6, 7
	li $s5, 2
	sw $s5, -24($fp)
	li $s4, 5
	sw $s4, -28($fp)
	la $s3, -28($fp)
	sw $s3, -32($fp)
	la $s2, -32($fp)
	sw $s2, -36($fp)
	la $s1, -36($fp)
	sw $s1, -40($fp)
	la $s0, -40($fp)
	sw $s0, -44($fp)
	sw	$s7,0($sp)

	sw	$s6,0($sp)

	# Swapping out reg $s6 for variable 4_r
	lw	$s6,-44($fp)
	lw $s7, 0($s6)
	sw	$s5,0($sp)

	lw $s5, 0($s7)
	sw	$s4,0($sp)

	lw $s4, 0($s5)
	sw	$s3,0($sp)

	la $s3, -24($fp)
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
