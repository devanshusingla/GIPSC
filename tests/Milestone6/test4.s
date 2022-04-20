.data


	_0_pre: .word 0



.text
.globl main
_Println:
	jr $ra
	jr $ra
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	mult $t6, $t7
	mflo $t9
	add $t5, $t9, $0
	add $t9, $t4, $t5
	add $t3, $t9, $0
	add $t1, $t2, $0
	addi $sp, $sp, -4
	sw $t1 ($sp)
	jr $ra
_ar:
	jr $ra
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	mult $t6, $t7
	mflo $t9
	add $t5, $t9, $0
	add $t9, $t4, $t5
	add $t3, $t9, $0
	add $t1, $t2, $0
	addi $sp, $sp, -4
	sw $t1 ($sp)
	jr $ra
main:
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	add $t9, $t8, $t7
	add $t8, $t9, $0
	mult $t6, $t7
	mflo $t9
	add $t5, $t9, $0
	add $t9, $t4, $t5
	add $t3, $t9, $0
	add $t1, $t2, $0
	addi $sp, $sp, -4
	sw $t1 ($sp)
	li $v0 10
	syscall
