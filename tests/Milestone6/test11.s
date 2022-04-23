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
	### GLOBAL VAR 2_x
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
	# Swapping out reg $t6 for variable 2_x
	# Changed 2_x
	lw	$t6,0($sp)
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
	### GLOBAL VAR 2_x
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
	slt $t9, $t6, $t0
	xori $t9, $t9, 1
	slt $t7, $t0, $t6
	xori $t7, $t7, 1
	and $t9, $t9, $t7
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-4($sp)

	###STACK: -8
	add $t8, $t9, $0
	beqz $t8, else_12
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
	j end_12
else_12:
end_12:
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
