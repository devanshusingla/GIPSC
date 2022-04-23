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
	addi $v0, $t6, $0
	jr $ra
	_return_f:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 8
	jr $ra
main:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -4
	li $t5, 2
	li $t4, 4
	add $a0, $t5, $0
	add $a1, $t4, $0
	jal _f
	addi $t3, $v0, $0
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

	add $t7, $t6, $0
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

	add $t3, $t2, $0
	sw	$t0,0($sp)

	sw	$t9,0($sp)

	add $t0, $t6, $t9
	sw	$t8,0($sp)

	add $t8, $t0, $0
	add $t8, $t6, $0
	j begin_for_20
end_for_20:
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 28
	jr $ra
