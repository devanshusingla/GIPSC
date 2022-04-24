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
	### $t9, temp_0
	sw $t9, -4($fp)
	### Need new register for $t8
	### Going to free register $t8
	###STACK: 0
	li $t8, 1
	### Need new register for $t7
	### Going to free register $t7
	###STACK: 0
	### $t8, temp_1
	add $t7, $a0, $t8
	### Need new register for $t6
	### Going to free register $t6
	###STACK: 0
	add $t6, $t7, $0
	### $t6, temp_2
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
	addi $sp, $sp, -4
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
	sw $v0, -4($fp)
	### Need new register for $t4
	### Going to free register $t4
	###STACK: 0
	li $t4, 0
	add $sp, $sp, -4
	### LOCATION 5_i : 8
	### $t4, temp_4
	sw $t4, -8($fp)
begin_for_11:
	### Need new register for $t3
	### Going to free register $t3
	###STACK: -4
	### Need new register for $t2
	### Going to free register $t2
	###STACK: -4
	lw $t2, -8($fp)
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -4
	lw $t1, -4($fp)
	slt $t3, $t1, $t2
	xori $t3, $t3, 1
	### Need new register for $t0
	### Going to free register $t0
	###STACK: -4
	add $t0, $t3, $0
	beqz $t0, end_for_11
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
	lw $a0, -8($fp)
	### STACK: -60
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
	### STACK1: -4, temp_6
	### False
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,0($sp)

	###STACK: -8
	### STACK2: -8
	addi $t9, $v0, 0
	add $sp, $sp, -4
	### LOCATION 6_x : 16
	### $t9, temp_6
	sw $t9, -16($fp)
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -12
	li $t7, 5
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,0($sp)

	###STACK: -16
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,0($sp)

	###STACK: -20
	lw $t6, -16($fp)
	### $t7, temp_7
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,0($sp)

	###STACK: -24
	slt $t8, $t6, $t7
	xori $t8, $t8, 1
	slt $t5, $t7, $t6
	xori $t5, $t5, 1
	and $t8, $t8, $t5
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,0($sp)

	###STACK: -28
	add $t4, $t8, $0
	beqz $t4, else_15
	j poststmt_for_11
	j end_15
else_15:
end_15:
	### Need new register for $t3
	### Going to free register $t3
	###STACK: -28
	li $t3, 7
	### Need new register for $t2
	### Going to free register $t2
	###STACK: -28
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -28
	lw $t1, -16($fp)
	### $t3, temp_9
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,0($sp)

	###STACK: -32
	slt $t2, $t1, $t3
	xori $t2, $t2, 1
	slt $t0, $t3, $t1
	xori $t0, $t0, 1
	and $t2, $t2, $t0
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,0($sp)

	###STACK: -36
	add $t9, $t2, $0
	beqz $t9, else_19
	j poststmt_for_11
	j end_19
else_19:
end_19:
	### Need new register for $t8
	### Going to free register $t8
	###STACK: -36
	li $t8, 1
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
	lw $a0, -16($fp)
	### STACK: -92
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
	### Need new register for $t6
	### Going to free register $t6
	###STACK: -36
	### Need new register for $t7
	### Going to free register $t7
	add $sp, $sp, -4
	sw	$t7,0($sp)

	###STACK: -40
	lw $t7, -8($fp)
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -40
	li $t5, 1
	add $t6, $t7, $t5
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,0($sp)

	###STACK: -44
	add $t4, $t6, $0
	### LOCATION 5_i : 8
	sw $t4, -8($fp)
	j begin_for_11
end_for_11:
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
