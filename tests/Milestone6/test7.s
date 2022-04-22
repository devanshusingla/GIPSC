.data



.text
.globl main
_f:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -0
	lw $t9, 8($fp)
	addi $v0, $, $0
	jr $ra
	_return_f:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
main:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	addi $sp, $sp, -4
	li $t8, 2
	add $a0, $t8, $0
	jal _f
	addi $t7, $v0, $0
	li $t6, 5
	slt $t5, $t7, $t6
	add $t4, $t5, $0
	beqz $t4, else_16
	li $t3, 6
	sw $t3, -4($fp)
	j end_16
else_16:
	li $t2, 4
	sw $t2, -4($fp)
end_16:
	_return_main:
	lw $ra, 4($sp)
	lw $fp, 0($fp)
	addi $sp, $sp, 0
	jr $ra
