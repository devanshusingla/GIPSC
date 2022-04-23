.data



.text
.globl main

_f:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -0
	li $t9, 2
	add $a0, $t9, $0
	li $t8, 4
	add $a1, $t8, $0
	add $t7, $a0, $a1
	add $t6, $t7, $0
	addi $v0, $t6, 0
	jr $ra
	_return_f:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 8
	jr $ra
main:
	addi $sp, $sp, -128
	add $fp, $sp, $0
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -4
	li $t5, 2
	li $t4, 4
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
	add $a0, $t5, $0
	add $a1, $t4, $0
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
	addi $t3, $v0, 0
	li $t2, 5
	slt $t1, $t3, $t2
	add $t0, $t1, $0
	beqz $t0, else_18
	sw	$t9,0($sp)

	li $t9, 6
	sw $t9, -4($fp)
	j end_18
else_18:
	sw	$t8,0($sp)

	li $t8, 4
	sw $t8, -4($fp)
end_18:
	li $t7, 0
	sw	$t6,0($sp)

	add $t6, $t7, $0
begin_for_20:
	sw	$t5,0($sp)

	li $t5, 5
	sw	$t4,0($sp)

	slt $t4, $t6, $t5
	add $t1, $t4, $0
	beqz $t1, end_for_20
	sw	$t3,0($sp)

	li $t3, 1
	sw	$t2,0($sp)

	add $t2, $t3, $0
	sw	$t0,0($sp)

	sw	$t9,0($sp)

	li $t9, 1
	add $t0, $t6, $t9
	sw	$t8,0($sp)

	add $t8, $t0, $0
	add $t6, $t8, $0
	j begin_for_20
end_for_20:
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 28
	li $v0 10
	syscall
