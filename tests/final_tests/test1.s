.data

	_nl: .asciiz "\n"


.text
.globl main

_ackermann:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	add $fp, $sp, $0
	addi $sp, $sp, -0
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
	### Need new register for $t9
	### Going to free register $t9
	###STACK: -32
	li $t9, 0
	### Need new register for $t8
	### Going to free register $t8
	###STACK: -32
	# $t9, temp_0
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -32
	slt $t8, $a0, $t9
	xori $t8, $t8, 1
	slt $t7, $t9, $a0
	xori $t7, $t7, 1
	and $t8, $t8, $t7
	### Need new register for $t6
	### Going to free register $t6
	###STACK: -32
	add $t6, $t8, $0
	beqz $t6, else_8
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -32
	li $t5, 1
	### Need new register for $t4
	### Going to free register $t4
	###STACK: -32
	# $t5, temp_2
	add $t4, $a1, $t5
	### Need new register for $t3
	### Going to free register $t3
	###STACK: -32
	add $t3, $t4, $0
	# $t3, temp_3
	addi $v0, $t3, 0
	j _return_ackermann
	j end_8
else_8:
end_8:
	### Need new register for $t2
	### Going to free register $t2
	###STACK: -32
	li $t2, 0
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -32
	# $t2, temp_4
	### Need new register for $t0
	### Going to free register $t0
	###STACK: -32
	slt $t1, $a1, $t2
	xori $t1, $t1, 1
	slt $t0, $t2, $a1
	xori $t0, $t0, 1
	and $t1, $t1, $t0
	### Need new register for $t8
	### Going to free register $t8
	###STACK: -32
	add $t8, $t1, $0
	beqz $t8, else_12
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,-68($fp)

	###STACK: -36
	li $t9, 1
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -36
	# $t9, temp_6
	sub $t7, $a0, $t9
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,-72($fp)

	###STACK: -40
	add $t6, $t7, $0
	### Need new register for $t4
	### Going to free register $t4
	###STACK: -40
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
	#### YAYYY temp_7
	### offset: [0, '$t6'], temp_7
	add $a0, $t6, $0
	#### YAYYY temp_8
	### offset: [0, '$t4'], temp_8
	add $a1, $t4, $0
	jal _ackermann
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
	### STACK1: -40, temp_9
	### False
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,-76($fp)

	###STACK: -44
	### STACK2: -44
	addi $t5, $v0, 0
	# $t5, temp_9
	addi $v0, $t5, 0
	j _return_ackermann
	j end_12
else_12:
end_12:
	### Need new register for $t3
	### Going to free register $t3
	add $sp, $sp, -4
	sw	$t3,-80($fp)

	###STACK: -48
	li $t3, 1
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -48
	# $t3, temp_10
	sub $t1, $a0, $t3
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,-84($fp)

	###STACK: -52
	add $t2, $t1, $0
	### Need new register for $t0
	### Going to free register $t0
	###STACK: -52
	li $t0, 1
	### Need new register for $t8
	### Going to free register $t8
	add $sp, $sp, -4
	sw	$t8,-88($fp)

	###STACK: -56
	# $t0, temp_12
	sub $t8, $a1, $t0
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -56
	add $t7, $t8, $0
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
	#### YAYYY arg_[ackermann_-8]
	add $a0, $a0, $0
	#### YAYYY temp_13
	### offset: [0, '$t7'], temp_13
	add $a1, $t7, $0
	jal _ackermann
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
	### STACK1: -56, temp_14
	### False
	### Need new register for $t9
	### Going to free register $t9
	add $sp, $sp, -4
	sw	$t9,-92($fp)

	###STACK: -60
	### STACK2: -60
	addi $t9, $v0, 0
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
	#### YAYYY temp_11
	### offset: [0, '$t2'], temp_11
	add $a0, $t2, $0
	#### YAYYY temp_14
	### offset: [0, '$t9'], temp_14
	add $a1, $t9, $0
	jal _ackermann
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
	### STACK1: -60, temp_15
	### False
	### Need new register for $t6
	### Going to free register $t6
	add $sp, $sp, -4
	sw	$t6,-96($fp)

	###STACK: -64
	### STACK2: -64
	addi $t6, $v0, 0
	# $t6, temp_15
	addi $v0, $t6, 0
	j _return_ackermann
	_return_ackermann:
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
	### Need new register for $t4
	### Going to free register $t4
	add $sp, $sp, -4
	sw	$t4,-72($fp)

	###STACK: -36
	li $t4, 3
	### Need new register for $t5
	### Going to free register $t5
	add $sp, $sp, -4
	sw	$t5,-76($fp)

	###STACK: -40
	li $t5, 4
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
	#### YAYYY temp_16
	### offset: [0, '$t4'], temp_16
	add $a0, $t4, $0
	#### YAYYY temp_17
	### offset: [0, '$t5'], temp_17
	add $a1, $t5, $0
	jal _ackermann
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
	### STACK1: -40, temp_18
	### False
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -40
	### STACK2: -40
	addi $t1, $v0, 0
	# $t1, temp_18
	sw $t1, -36($fp)
	### Need new register for $t3
	### Going to free register $t3
	add $sp, $sp, -4
	sw	$t3,-80($fp)

	###STACK: -44
	li $t3, 1
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
	#### YAYYY 8_b
	### Need new register for $t2
	### Going to free register $t2
	add $sp, $sp, -4
	sw	$t2,-140($fp)

	###STACK: -104
	lw $t2, -36($fp)
	add $a0, $t2, $0
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
