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
	addi $sp, $sp, -12
	### Need new register for $t9
	### Going to free register $t9
	###STACK: 0
	li $t9, 5
	# $t9, temp_0
	sw $t9, -4($fp)
	### Need new register for $t8
	### Going to free register $t8
	###STACK: 0
	addi $t8, $fp, -4
	# $t8, temp_1
	sw $t8, -8($fp)
	### Need new register for $t7
	### Going to free register $t7
	###STACK: 0
	addi $t7, $fp, -8
	# $t7, temp_2
	sw $t7, -12($fp)
	### Need new register for $t6
	### Going to free register $t6
	###STACK: 0
	### Need new register for $t5
	### Going to free register $t5
	###STACK: 0
	# Swapping out reg $t5 for variable 2_z
	# Changed 2_z
	lw	$t5,-12($fp)
	lw $t6, 0($t5)
	### Need new register for $t4
	### Going to free register $t4
	###STACK: 0
	lw $t4, 0($t6)
	### Need new register for $t3
	### Going to free register $t3
	###STACK: 0
	li $t3, 20
	# $t6, temp_3
	sw $t3, 0($t6)
	### Need new register for $t2
	### Going to free register $t2
	###STACK: 0
	li $t2, 1
	### Need new register for $t1
	### Going to free register $t1
	###STACK: 0
	lw $t1, 0($t5)
	### Need new register for $t0
	### Going to free register $t0
	###STACK: 0
	lw $t0, 0($t1)
	### Need new register for $s7
	### Going to free register $s7
	###STACK: 0
	### Need new register for $s6
	### Going to free register $s6
	###STACK: 0
	lw $s6, -4($fp)
	# $t0, temp_8
	mult $s6, $t0
	mflo $s7
	### Need new register for $s5
	### Going to free register $s5
	###STACK: 0
	add $s5, $s7, $0
	### Need new register for $s4
	### Going to free register $s4
	###STACK: 0
	### Need new register for $s3
	### Going to free register $s3
	###STACK: 0
	# Swapping out reg $s3 for variable 2_y
	# Changed 2_y
	lw	$s3,-8($fp)
	lw $s4, 0($s3)
	### Need new register for $s2
	### Going to free register $s2
	###STACK: 0
	# $s5, temp_9
	# $s4, temp_10
	mult $s5, $s4
	mflo $s2
	### Need new register for $s1
	### Going to free register $s1
	###STACK: 0
	add $s1, $s2, $0
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
	### offset: [0, '$s1'], temp_11
	add $a0, $s1, $0
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
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
