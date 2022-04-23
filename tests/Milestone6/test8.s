.data



.text
.globl main

_f:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	add $fp, $sp, $0
	addi $sp, $sp, -4
	### Need new register for $t9
	### Going to free register $t9
	###STACK: 0
	li $t9, 4
	### GLOBAL VAR 2_x
	### $t9, temp_0
	sw $t9, -4($fp)
	### Need new register for $t8
	### Going to free register $t8
	###STACK: 0
	li $t8, 1
	### Need new register for $t7
	### Going to free register $t7
	###STACK: 0
	add $t7, $a0, $t8
	### Need new register for $t6
	### Going to free register $t6
	###STACK: 0
	add $t6, $t7, $0
	addi $v0, $t6, 0
	j _return_f
	_return_f:
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
	addi $sp, $sp, -8
	### Need new register for $t5
	### Going to free register $t5
	###STACK: 0
	li $t5, 5
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
	li $v0, 5
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
	### GLOBAL VAR 4_a
	sw $v0, -4($fp)
	### Need new register for $t4
	### Going to free register $t4
	###STACK: 0
	li $t4, 1
	### Need new register for $t3
	### Going to free register $t3
	###STACK: 0
	### Need new register for $t2
	### Going to free register $t2
	###STACK: 0
	# Swapping out reg $t2 for variable 4_a
	# Changed 4_a
	lw	$t2,4($sp)
	add $t3, $t2, $t4
	### Need new register for $t1
	### Going to free register $t1
	###STACK: 0
	add $t1, $t3, $0
	### GLOBAL VAR 4_c
	### $t1, temp_5
	sw $t1, -8($fp)
	### Need new register for $t0
	### Going to free register $t0
	###STACK: 0
	li $t0, 0
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,-4($sp)

	###STACK: -4
	### $t0, temp_6
	add $t9, $t0, $0
begin_for_11:
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -4
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-4($sp)

	###STACK: -8
	# Swapping out reg $t8 for variable 4_c
	# Changed 4_c
	lw	$t8,8($sp)
	slt $t7, $t8, $t9
	xori $t7, $t7, 1
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,-4($sp)

	###STACK: -12
	add $t6, $t7, $0
	beqz $t6, end_for_11
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
	add $a0, $t9, $0
	### STACK: -68
	jal _f
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
	### STACK1: -12, temp_8
	### False
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,-4($sp)

	###STACK: -16
	### STACK2: -16
	addi $t5, $v0, 0
	### Need new register for $t3
	### Going to free register $t3
	###STACK: -16
	### $t5, temp_8
	add $t3, $t5, $0
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,-4($sp)

	###STACK: -20
	li $t2, 5
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,-4($sp)

	###STACK: -24
	### Need new register for $t1
	### Going to free register $t1
	add $sp, $sp, -4
	sw	$t1,-4($sp)

	###STACK: -28
	slt $t4, $t3, $t2
	xori $t4, $t4, 1
	slt $t1, $t2, $t3
	xori $t1, $t1, 1
	and $t4, $t4, $t1
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,-4($sp)

	###STACK: -32
	add $t0, $t4, $0
	beqz $t0, else_15
	j poststmt_for_11
	j end_15
else_15:
end_15:
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -32
	li $t7, 7
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,-4($sp)

	###STACK: -36
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-4($sp)

	###STACK: -40
	slt $t9, $t3, $t7
	xori $t9, $t9, 1
	slt $t8, $t7, $t3
	xori $t8, $t8, 1
	and $t9, $t9, $t8
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,-4($sp)

	###STACK: -44
	add $t6, $t9, $0
	beqz $t6, else_19
	j poststmt_for_11
	j end_19
else_19:
end_19:
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,-4($sp)

	###STACK: -48
	li $t5, 1
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
	add $a0, $t3, $0
	### STACK: -104
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
poststmt_for_11:
	### Need new register for $t4
	### Going to free register $t4
	###STACK: -48
	# Swapping out reg $t4 for variable 5_i
	# Changed 5_i
	lw	$t4,16($sp)
	### $t4, 5_i
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,-4($sp)

	###STACK: -52
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -52
	li $t1, 1
	add $t2, $t4, $t1
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,-4($sp)

	###STACK: -56
	add $t0, $t2, $0
	add $t4, $t0, $0
	j begin_for_11
end_for_11:
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
