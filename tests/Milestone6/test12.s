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
	addi $sp, $sp, -4
	### Need new register for $t9
	### Going to free register $t9
	###STACK: 0
	li $t9, 5
	# $t9, temp_0
	sw $t9, -4($fp)
	### Need new register for $t8
	### Going to free register $t8
	###STACK: 0
	li $t8, 5
	### Need new register for $t7
	### Going to free register $t7
	###STACK: 0
	### Need new register for $t6
	### Going to free register $t6
	###STACK: 0
	lw $t6, -4($fp)
	# $t8, temp_1
	### Need new register for $t5
	### Going to free register $t5
	###STACK: 0
	slt $t7, $t6, $t8
	xori $t7, $t7, 1
	slt $t5, $t8, $t6
	xori $t5, $t5, 1
	and $t7, $t7, $t5
	### Need new register for $t4
	### Going to free register $t4
	###STACK: 0
	add $t4, $t7, $0
	beqz $t4, else_20
	### Need new register for $t3
	### Going to free register $t3
	###STACK: 0
	li $t3, 1
	### Need new register for $t2
	### Going to free register $t2
	###STACK: 0
	li $t2, 10
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
	### offset: [0, '$t2'], temp_4
	add $a0, $t2, $0
	### STACK: -56
	li $v0, 1
	syscall
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
	### Need new register for $t1
	### Going to free register $t1
	###STACK: 0
	li $t1, 7
	# $t1, temp_5
	sw $t1, -4($fp)
	### Need new register for $t0
	### Going to free register $t0
	###STACK: 0
	li $t0, 3
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,0($sp)

	###STACK: -4
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -4
	lw $t7, -4($fp)
	# $t0, temp_6
	div $t7, $t0
	mflo $t9
	### Need new register for $t6
	### Going to free register $t6
	###STACK: -4
	add $t6, $t9, $0
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,0($sp)

	###STACK: -8
	li $t8, 9
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -8
	# $t6, temp_7
	# $t8, temp_8
	slt $t5, $t6, $t8
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,0($sp)

	###STACK: -12
	add $t4, $t5, $0
	beqz $t4, else_19
	### Need new register for $t3
	### Going to free register $t3
	add $sp, $sp, -4
	sw	$t3,0($sp)

	###STACK: -16
	li $t3, 0
	add $sp, $sp, -4
	### LOCATION 6_i : 16
	# $t3, temp_10
	sw $t3, 16($fp)
begin_for_10:
poststmt_for_10:
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,0($sp)

	###STACK: -24
	li $t2, 10
	### Need new register for $t1
	### Going to free register $t1
	add $sp, $sp, -4
	sw	$t1,0($sp)

	###STACK: -28
	### Need new register for $t9
	### Going to free register $t9
	###STACK: -28
	lw $t9, 16($fp)
	# $t2, temp_11
	slt $t1, $t9, $t2
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -28
	add $t7, $t1, $0
	beqz $t7, end_for_10
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,0($sp)

	###STACK: -32
	li $t0, 1
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
	### offset: [1, 20], 6_i
	lw $a0, 16($fp)
	### STACK: -88
	li $v0, 1
	syscall
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
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -32
	li $t5, 1
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,0($sp)

	###STACK: -36
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,0($sp)

	###STACK: -40
	lw $t8, 16($fp)
	# $t5, temp_14
	add $t6, $t8, $t5
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,0($sp)

	###STACK: -44
	add $t4, $t6, $0
	### LOCATION 6_i : 16
	sw $t4, 16($fp)
	j begin_for_10
end_for_10:
	j end_19
else_19:
	### Need new register for $t3
	### Going to free register $t3
	add $sp, $sp, -4
	sw	$t3,0($sp)

	###STACK: -48
	li $t3, 1
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -48
	### Need new register for $t9
	### Going to free register $t9
	###STACK: -48
	lw $t9, -4($fp)
	# $t3, temp_15
	slt $t1, $t3, $t9
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,0($sp)

	###STACK: -52
	add $t2, $t1, $0
	beqz $t2, else_18
	### Need new register for $t7
	### Going to free register $t7
	add $sp, $sp, -4
	sw	$t7,0($sp)

	###STACK: -56
	li $t7, 1
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,0($sp)

	###STACK: -60
	li $t0, 100
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
	### offset: [0, '$t0'], temp_18
	add $a0, $t0, $0
	### STACK: -116
	li $v0, 1
	syscall
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
	j end_18
else_18:
end_18:
end_19:
	j end_20
else_20:
end_20:
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
