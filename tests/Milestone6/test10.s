.data



.text
.globl main

_f:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	add $fp, $sp, $0
	addi $sp, $sp, -0
	### Need new register for $t9
	### Going to free register $t9
	###STACK: 0
	li $t9, 0
	### Need new register for $t8
	### Going to free register $t8
	###STACK: 0
	# $t9, temp_0
	### Need new register for $t7
	### Going to free register $t7
	###STACK: 0
	slt $t8, $a0, $t9
	xori $t8, $t8, 1
	slt $t7, $t9, $a0
	xori $t7, $t7, 1
	and $t8, $t8, $t7
	### Need new register for $t6
	### Going to free register $t6
	###STACK: 0
	add $t6, $t8, $0
	### Need new register for $t5
	### Going to free register $t5
	###STACK: 0
	li $t5, 1
	### Need new register for $t4
	### Going to free register $t4
	###STACK: 0
	# $t5, temp_2
	### Need new register for $t3
	### Going to free register $t3
	###STACK: 0
	slt $t4, $a0, $t5
	xori $t4, $t4, 1
	slt $t3, $t5, $a0
	xori $t3, $t3, 1
	and $t4, $t4, $t3
	### Need new register for $t2
	### Going to free register $t2
	###STACK: 0
	add $t2, $t4, $0
	### Need new register for $t1
	### Going to free register $t1
	###STACK: 0
	# $t6, temp_1
	# $t2, temp_3
	or $t1, $t6, $t2
	### Need new register for $t0
	### Going to free register $t0
	###STACK: 0
	add $t0, $t1, $0
	beqz $t0, else_6
	### Need new register for $t8
	### Going to free register $t8
	###STACK: 0
	li $t8, 1
	# $t8, temp_5
	addi $v0, $t8, 0
	j _return_f
	j end_6
else_6:
end_6:
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,0($sp)

	###STACK: -4
	li $t9, 2
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -4
	# $t9, temp_6
	sub $t7, $a0, $t9
	### Need new register for $t4
	### Going to free register $t4
	###STACK: -4
	add $t4, $t7, $0
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
	### offset: [0, '$t4'], temp_7
	add $a0, $t4, $0
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
	### STACK1: -4, temp_8
	### False
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,0($sp)

	###STACK: -8
	### STACK2: -8
	addi $t5, $v0, 0
	### Need new register for $t3
	### Going to free register $t3
	###STACK: -8
	li $t3, 1
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -8
	# $t3, temp_9
	sub $t1, $a0, $t3
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,0($sp)

	###STACK: -12
	add $t6, $t1, $0
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
	### offset: [0, '$t6'], temp_10
	add $a0, $t6, $0
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
	### STACK1: -12, temp_11
	### False
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,0($sp)

	###STACK: -16
	### STACK2: -16
	addi $t2, $v0, 0
	### Need new register for $t0
	### Going to free register $t0
	add $sp, $sp, -4
	sw	$t0,0($sp)

	###STACK: -20
	# $t5, temp_8
	# $t2, temp_11
	add $t0, $t5, $t2
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,0($sp)

	###STACK: -24
	add $t8, $t0, $0
	# $t8, temp_12
	addi $v0, $t8, 0
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
	### Need new register for $t7
	### Going to free register $t7
	###STACK: 0
	li $t7, 8
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
	### offset: [0, '$t7'], temp_13
	add $a0, $t7, $0
	### STACK: -56
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
	### STACK1: 0, temp_14
	### False
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,0($sp)

	###STACK: -4
	### STACK2: -4
	addi $t9, $v0, 0
	# $t9, temp_14
	sw $t9, -4($fp)
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,0($sp)

	###STACK: -8
	li $t4, 1
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
	### offset: [1, 0], 6_x
	lw $a0, -4($fp)
	### STACK: -64
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
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
