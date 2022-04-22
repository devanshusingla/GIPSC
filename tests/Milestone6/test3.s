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
	sw $t8, 8($fp)
	add $t8, $t8, $t9
	add $t7, $t8, $0
	sw $t6, 8($fp)
	li $t5, 5
<<<<<<< HEAD
	sw	$t4,-24($fp)

	sw $t4, 0($fp)
	sw	$t3,-28($fp)

=======
	# Swapping out reg $t4 for variable 2_z
	lw	$t4,$t4($fp)
	add $t5, $t4, $0
>>>>>>> b6b042c40de065c79f434eff744981824e3e7632
	li $t3, 3
	sw $t8, 8($fp)
	add $t8, $t8, $t3
	add $t2, $t8, $0
	li $a0 8
	li $v0 9
	syscall
	sw $t2, 0($v0)
	sw $t4, 4($v0)
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
	li $t1, 5
	add $a0, $t1, $0
	jal _inc
	lw $t8, 0($v0)
	add {ret_reg}, {loc}, $0
	lw $t8, 4($v0)
	add {ret_reg}, {loc}, $0
	sw	$t7,0($sp)

	li $t7, 6
	sw	$t6,0($sp)

	# Swapping out reg $t6 for variable 4_y
	lw	$t6,$t6($fp)
	add $t7, $t6, $0
	sw	$t5,0($sp)

	add $t5, $t6, $0
	sw	$t3,0($sp)

	# Swapping out reg $t3 for variable 4_x
	lw	$t3,$t3($fp)
	add $t5, $t3, $0
	sw	$t2,0($sp)

	li $t2, 2
	add $t2, $t6, $0
	sw	$t4,0($sp)

	add $t4, $t6, $0
	sw	$t1,0($sp)

	lw $t1, 0($t4)
	sw	$t0,0($sp)

	li $t0, 4
	add $t8, $t6, $0
	# Swapping out reg $s7 for variable 4_g
	lw	$s7,$s7($fp)
	add $t8, $s7, $0
	lw $s6, 0($s7)
	add $s5, $s6, $0
	lw $s4, 0($s5)
	li $s3, 7
	li $s2, 2
	# Swapping out reg $s1 for variable 4_p
	lw	$s1,$s1($fp)
	add $s2, $s1, $0
	li $s0, 5
	sw	$t9,0($sp)

	# Swapping out reg $t9 for variable 4_a1
	lw	$t9,$t9($fp)
	add $s0, $t9, $0
	sw	$t7,0($sp)

	add $t7, $t9, $0
	sw	$t3,0($sp)

	# Swapping out reg $t3 for variable 4_a2
	lw	$t3,$t3($fp)
	add $t7, $t3, $0
	sw	$t5,0($sp)

	add $t5, $t3, $0
	sw	$t2,0($sp)

	# Swapping out reg $t2 for variable 4_a3
	lw	$t2,$t2($fp)
	add $t5, $t2, $0
	sw	$t1,0($sp)

	add $t1, $t2, $0
	sw	$t4,0($sp)

	# Swapping out reg $t4 for variable 4_a4
	lw	$t4,$t4($fp)
	add $t1, $t4, $0
	sw	$t0,0($sp)

	add $t0, $t4, $0
	sw	$t6,0($sp)

	# Swapping out reg $t6 for variable 4_r
	lw	$t6,$t6($fp)
	add $t0, $t6, $0
	sw	$t8,0($sp)

	lw $t8, 0($t6)
	sw	$s7,0($sp)

	lw $s7, 0($t8)
	sw	$s6,0($sp)

	lw $s6, 0($s7)
	sw	$s4,0($sp)

	add $s4, $s1, $0
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
