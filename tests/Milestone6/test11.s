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
	### $t9, temp_0
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
	### $t8, temp_1
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
	beqz $t4, else_8
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
	### $t1, temp_5
	sw $t1, -4($fp)
	j end_8
else_8:
end_8:
	### Need new register for $t0
	### Going to free register $t0
	###STACK: 0
	li $t0, 7
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,-4($sp)

	###STACK: -4
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -4
	lw $t7, -4($fp)
	### $t0, temp_6
	### Need new register for $t6
	### Going to free register $t6
	###STACK: -4
	slt $t9, $t7, $t0
	xori $t9, $t9, 1
	slt $t6, $t0, $t7
	xori $t6, $t6, 1
	and $t9, $t9, $t6
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-4($sp)

	###STACK: -8
	add $t8, $t9, $0
	beqz $t8, else_13
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -8
	li $t5, 1
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,-4($sp)

	###STACK: -12
	li $t4, 14
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
	add $a0, $t4, $0
	### STACK: -68
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
	### Need new register for $t3
	### Going to free register $t3
	add $sp, $sp, -4
	sw	$t3,-4($sp)

	###STACK: -16
	li $t3, 9
	### $t3, temp_10
	sw $t3, -4($fp)
	j end_13
else_13:
end_13:
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,-4($sp)

	###STACK: -20
	li $t2, 3
	### Need new register for $t1
	### Going to free register $t1
	add $sp, $sp, -4
	sw	$t1,-4($sp)

	###STACK: -24
	### Need new register for $t9
	### Going to free register $t9
	###STACK: -24
	lw $t9, -4($fp)
	### $t2, temp_11
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -24
	slt $t1, $t9, $t2
	xori $t1, $t1, 1
	slt $t7, $t2, $t9
	xori $t7, $t7, 1
	and $t1, $t1, $t7
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,-4($sp)

	###STACK: -28
	add $t0, $t1, $0
	### Need new register for $t6
	### Going to free register $t6
	###STACK: -28
	li $t6, 3
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-4($sp)

	###STACK: -32
	li $t8, 3
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,-4($sp)

	###STACK: -36
	### $t6, temp_13
	### $t8, temp_14
	mult $t6, $t8
	mflo $t5
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,-4($sp)

	###STACK: -40
	add $t4, $t5, $0
	### Need new register for $t3
	### Going to free register $t3
	add $sp, $sp, -4
	sw	$t3,-4($sp)

	###STACK: -44
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -44
	lw $t1, -4($fp)
	### $t4, temp_15
	### Need new register for $t9
	### Going to free register $t9
	###STACK: -44
	slt $t3, $t1, $t4
	xori $t3, $t3, 1
	slt $t9, $t4, $t1
	xori $t9, $t9, 1
	and $t3, $t3, $t9
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,-4($sp)

	###STACK: -48
	add $t2, $t3, $0
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -48
	### $t0, temp_12
	### $t2, temp_16
	or $t7, $t0, $t2
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -48
	add $t5, $t7, $0
	beqz $t5, else_18
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,-4($sp)

	###STACK: -52
	li $t6, 1
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-4($sp)

	###STACK: -56
	li $t8, 90
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
	add $a0, $t8, $0
	### STACK: -112
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
	### Need new register for $t3
	### Going to free register $t3
	###STACK: -56
	li $t3, 40
	### $t3, temp_20
	sw $t3, -4($fp)
	j end_18
else_18:
end_18:
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -56
	li $t1, 40
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,-4($sp)

	###STACK: -60
	### Need new register for $t9
	### Going to free register $t9
	###STACK: -60
	lw $t9, -4($fp)
	### $t1, temp_21
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -60
	slt $t4, $t9, $t1
	xori $t4, $t4, 1
	slt $t7, $t1, $t9
	xori $t7, $t7, 1
	and $t4, $t4, $t7
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,-4($sp)

	###STACK: -64
	add $t0, $t4, $0
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,-4($sp)

	###STACK: -68
	li $t2, 90
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,-4($sp)

	###STACK: -72
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,-4($sp)

	###STACK: -76
	lw $t6, -4($fp)
	### $t2, temp_23
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-4($sp)

	###STACK: -80
	slt $t5, $t6, $t2
	xori $t5, $t5, 1
	slt $t8, $t2, $t6
	xori $t8, $t8, 1
	and $t5, $t5, $t8
	### Need new register for $t3
	### Going to free register $t3
	add $sp, $sp, -4
	sw	$t3,-4($sp)

	###STACK: -84
	add $t3, $t5, $0
	### Need new register for $t4
	### Going to free register $t4
	###STACK: -84
	### $t0, temp_22
	### $t3, temp_24
	and $t4, $t0, $t3
	### Need new register for $t9
	### Going to free register $t9
	###STACK: -84
	add $t9, $t4, $0
	beqz $t9, else_24
	### Need new register for $t1
	### Going to free register $t1
	add $sp, $sp, -4
	sw	$t1,-4($sp)

	###STACK: -88
	li $t1, 1
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -88
	li $t7, 45
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
	add $a0, $t7, $0
	### STACK: -144
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
	j end_24
else_24:
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -88
	li $t5, 1
	### Need new register for $t6
	### Going to free register $t6
	###STACK: -88
	li $t6, 100
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
	add $a0, $t6, $0
	### STACK: -144
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
end_24:
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
