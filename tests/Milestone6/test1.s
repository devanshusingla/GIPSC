.data



.text
.globl main
main:
addi $sp, $sp, -4
sw $ra, 0($sp)
addi $sp, $sp, -4
sw $fp, 0($sp)
addi $sp, $sp, -8
	li $t9, 6
	li $t8, 6
	sw $t8, []($fp)
	la $t7, 0($fp)
	la $t8, 0($fp)
	sw $t8, []($fp)
	li $t6, 2
	li $t8, 2
	sw $t8, []($fp)
_return_main:
lw $ra, -4($sp)
lw $fp, 0($fp)
addi $sp, $sp, 0
jr $ra
