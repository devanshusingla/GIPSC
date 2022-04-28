.data

	_nl: .asciiz "\n"


.text
.globl main

_inc:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	add $fp, $sp, $0
	addi $sp, $sp, -4
	### Saving $s registers
	add $sp, $sp, -4
	sw $s0, 0($sp)
	add $sp, $sp, -4
	sw $s1, 0($sp)
	add $sp, $sp, -4
	sw $s2, 0($sp)
	add $sp, $sp, -4
	sw $s3, 0($sp)
	add $sp, $sp, -4
	sw $s4, 0($sp)
	add $sp, $sp, -4
	sw $s5, 0($sp)
	add $sp, $sp, -4
	sw $s6, 0($sp)
	add $sp, $sp, -4
	sw $s7, 0($sp)
	li $t9, 6
	# $t9, temp_0
	add $t8, $a0, $t9
	add $t7, $t8, $0
	add $t6, $t7, $0
	# $t6, temp_2
	add $a0, $t6, $0
	li $t5, 5
	# $t5, temp_3
	sw $t5, -36($fp)
	li $t4, 3
	# $t4, temp_4
	add $t3, $a0, $t4
	add $t2, $t3, $0
	lw $t1, -36($fp)
	li $a0 8
	li $v0 9
	syscall
	lw $t0, -36($fp)
	sw $t0, 0($v0)
	# $t2, temp_5
	sw $t2, 4($v0)
	addi $v1, $0, 8
	j _return_inc
	_return_inc:
	### Restoring $s registers
	lw $s7, 0($sp)
	add $sp, $sp, 4
	lw $s6, 0($sp)
	add $sp, $sp, 4
	lw $s5, 0($sp)
	add $sp, $sp, 4
	lw $s4, 0($sp)
	add $sp, $sp, 4
	lw $s3, 0($sp)
	add $sp, $sp, 4
	lw $s2, 0($sp)
	add $sp, $sp, 4
	lw $s1, 0($sp)
	add $sp, $sp, 4
	lw $s0, 0($sp)
	add $sp, $sp, 4
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	jr $ra
main:
	addi $sp, $sp, -128
	add $fp, $sp, $0
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	add $fp, $sp, $0
	addi $sp, $sp, -44
	### Saving $s registers
	add $sp, $sp, -4
	sw $s0, 0($sp)
	add $sp, $sp, -4
	sw $s1, 0($sp)
	add $sp, $sp, -4
	sw $s2, 0($sp)
	add $sp, $sp, -4
	sw $s3, 0($sp)
	add $sp, $sp, -4
	sw $s4, 0($sp)
	add $sp, $sp, -4
	sw $s5, 0($sp)
	add $sp, $sp, -4
	sw $s6, 0($sp)
	add $sp, $sp, -4
	sw $s7, 0($sp)
	li $t8, 5
	#### Saving temporary registers
	add $sp, $sp, -4
	sw $t0, 0($sp)
	add $sp, $sp, -4
	sw $t1, 0($sp)
	add $sp, $sp, -4
	sw $t2, 0($sp)
	add $sp, $sp, -4
	sw $t3, 0($sp)
	add $sp, $sp, -4
	sw $t4, 0($sp)
	add $sp, $sp, -4
	sw $t5, 0($sp)
	add $sp, $sp, -4
	sw $t6, 0($sp)
	add $sp, $sp, -4
	sw $t7, 0($sp)
	add $sp, $sp, -4
	sw $t8, 0($sp)
	add $sp, $sp, -4
	sw $t9, 0($sp)
	#### Done saving temporary registers
	#### Saving argument registers
	add $sp, $sp, -4
	sw $a0, 0($sp)
	add $sp, $sp, -4
	sw $a1, 0($sp)
	add $sp, $sp, -4
	sw $a2, 0($sp)
	add $sp, $sp, -4
	sw $a3, 0($sp)
	#### Done saving argument registers
	#### YAYYY temp_6
	### offset: [0, '$t8'], temp_6
	add $a0, $t8, $0
	jal _inc
	### Restoring argument registers
	lw $a3, 0($sp)
	add $sp, $sp, 4
	lw $a2, 0($sp)
	add $sp, $sp, 4
	lw $a1, 0($sp)
	add $sp, $sp, 4
	lw $a0, 0($sp)
	add $sp, $sp, 4
	### Done restoring argument registers
	lw $t9, 0($sp)
	add $sp, $sp, 4
	lw $t8, 0($sp)
	add $sp, $sp, 4
	lw $t7, 0($sp)
	add $sp, $sp, 4
	lw $t6, 0($sp)
	add $sp, $sp, 4
	lw $t5, 0($sp)
	add $sp, $sp, 4
	lw $t4, 0($sp)
	add $sp, $sp, 4
	lw $t3, 0($sp)
	add $sp, $sp, 4
	lw $t2, 0($sp)
	add $sp, $sp, 4
	lw $t1, 0($sp)
	add $sp, $sp, 4
	lw $t0, 0($sp)
	add $sp, $sp, 4
	add $sp, $sp, -4
	sw	$t9,-112($fp)

	lw $t9, 0($v0)
	add $sp, $sp, -4
	sw	$t7,-116($fp)

	addi $t7, $t9, 0
	add $sp, $sp, -4
	sw	$t6,-120($fp)

	lw $t6, 4($v0)
	add $sp, $sp, -4
	sw	$t5,-124($fp)

	addi $t5, $t6, 0
	# $t7, temp_7
	sw $t7, -36($fp)
	# $t5, temp_8
	sw $t5, -40($fp)
	li $t3, 6
	# $t3, temp_9
	sw $t3, -44($fp)
	add $sp, $sp, -4
	sw	$t4,-128($fp)

	addi $t4, $fp, -44
	# $t4, temp_10
	sw $t4, -48($fp)
	li $t1, 2
	add $t0, $t1, $0
	# $t0, temp_12
	sw $t0, -44($fp)
	add $sp, $sp, -4
	sw	$t2,-132($fp)

	addi $t2, $fp, -44
	add $sp, $sp, -4
	sw	$t8,-136($fp)

	# $t2, temp_13
	lw $t8, 0($t2)
	li $t9, 4
	add $t6, $t9, $0
	# $t2, temp_13
	sw $t6, 0($t2)
	addi $s7, $fp, -44
	# $s7, temp_17
	sw $s7, -52($fp)
	lw $s5, -52($fp)
	lw $s6, 0($s5)
	# $s6, temp_18
	add $s4, $s6, $0
	# $s4, temp_19
	lw $s3, 0($s4)
	li $s2, 7
	add $s1, $s2, $0
	# $s4, temp_19
	sw $s1, 0($s4)
	li $s0, 2
	# $s0, temp_23
	sw $s0, -56($fp)
	add $sp, $sp, -4
	sw	$t7,-140($fp)

	li $t7, 5
	# $t7, temp_24
	sw $t7, -60($fp)
	add $sp, $sp, -4
	sw	$t5,-144($fp)

	addi $t5, $fp, -60
	# $t5, temp_25
	sw $t5, -64($fp)
	add $sp, $sp, -4
	sw	$t3,-148($fp)

	addi $t3, $fp, -64
	# $t3, temp_26
	sw $t3, -68($fp)
	add $sp, $sp, -4
	sw	$t4,-152($fp)

	addi $t4, $fp, -68
	# $t4, temp_27
	sw $t4, -72($fp)
	add $sp, $sp, -4
	sw	$t1,-156($fp)

	addi $t1, $fp, -72
	# $t1, temp_28
	sw $t1, -76($fp)
	add $sp, $sp, -4
	sw	$t0,-160($fp)

	add $sp, $sp, -4
	sw	$t8,-164($fp)

	lw $t8, -76($fp)
	lw $t0, 0($t8)
	add $sp, $sp, -4
	sw	$t9,-168($fp)

	# $t0, temp_29
	lw $t9, 0($t0)
	add $sp, $sp, -4
	sw	$t2,-172($fp)

	# $t9, temp_30
	lw $t2, 0($t9)
	add $sp, $sp, -4
	sw	$t6,-176($fp)

	addi $t6, $fp, -56
	add $sp, $sp, -4
	sw	$t7,-180($fp)

	add $t7, $t6, $0
	# $t9, temp_30
	sw $t7, 0($t9)
	_return_main:
	### Restoring $s registers
	lw $s7, 0($sp)
	add $sp, $sp, 4
	lw $s6, 0($sp)
	add $sp, $sp, 4
	lw $s5, 0($sp)
	add $sp, $sp, 4
	lw $s4, 0($sp)
	add $sp, $sp, 4
	lw $s3, 0($sp)
	add $sp, $sp, 4
	lw $s2, 0($sp)
	add $sp, $sp, 4
	lw $s1, 0($sp)
	add $sp, $sp, 4
	lw $s0, 0($sp)
	add $sp, $sp, 4
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
