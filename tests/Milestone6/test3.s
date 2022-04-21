.data



.text
.globl main
_inc:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -4
	sw	$t9,-4($fp)

	li $t9, 6
	sw	$t8,-8($fp)

	sw $t8 8($fp)
	add $t8, $t8, $t9
	sw	$t7,-12($fp)

	add $t7, $t8, $0
	sw	$t6,-16($fp)

	sw $t6, 8($fp)
	sw	$t5,-20($fp)

	li $t5, 5
	sw	$t4,-24($fp)

	sw $t4, 0($fp)($fp)
	sw	$t3,-28($fp)

	li $t3, 3
	sw $t8 8($fp)
	add $t8, $t8, $t3
	sw	$t2,-32($fp)

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
	sw	$t1,-36($fp)

	li $t1, 5
	addi $sp, $sp, -4
	sw $t1 ($sp)
	lw $t8, 0($v0)
//: 0($fp)
	lw $t8, 0($fp)($fp)
	lw $t8, 4($v0)
//: 4($fp)
	lw $t8, 4($fp)($fp)
	sw	$t0,-40($fp)

	li $t0, 6
	sw	$t9,-44($fp)

	sw $t9, 8($fp)($fp)
	sw	$t7,-48($fp)

	la $t7, $t9
	sw	$t6,-52($fp)

	sw $t6, 12($fp)($fp)
	sw	$t5,-56($fp)

	li $t5, 2
	sw $t9, []($fp)
	sw	$t3,-60($fp)

	la $t3, $t9
	sw	$t2,-64($fp)

	lw $t2 $t3
	sw	$t4,-68($fp)

	li $t4, 4
	sw	$t1,-72($fp)

	la $t1, $t9
	sw	$t8,-76($fp)

	sw $t8, 16($fp)($fp)
	sw	$s7,-80($fp)

	lw $s7 $t8
	sw	$s6,-84($fp)

	la $s6, $s7
	sw	$s5,-88($fp)

	lw $s5 $s6
	sw	$s4,-92($fp)

	li $s4, 7
	sw	$s3,-96($fp)

	li $s3, 2
	sw	$s2,-100($fp)

	sw $s2, 20($fp)($fp)
	sw	$s1,-104($fp)

	li $s1, 5
	sw	$s0,-108($fp)

	sw $s0, 24($fp)($fp)
	sw	$t0,-112($fp)

	la $t0, $s0
	sw	$t7,-116($fp)

	sw $t7, 28($fp)($fp)
	sw	$t6,-120($fp)

	la $t6, $t7
	sw	$t5,-124($fp)

	sw $t5, 32($fp)($fp)
	sw	$t2,-128($fp)

	la $t2, $t5
	sw	$t3,-132($fp)

	sw $t3, 36($fp)($fp)
	sw	$t4,-136($fp)

	la $t4, $t3
	sw	$t1,-140($fp)

	sw $t1, 40($fp)($fp)
	sw	$t9,-144($fp)

	lw $t9 $t1
	sw	$t8,-148($fp)

	lw $t8 $t9
	sw	$s7,-152($fp)

	lw $s7 $t8
	sw	$s5,-156($fp)

	la $s5, $s2
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
