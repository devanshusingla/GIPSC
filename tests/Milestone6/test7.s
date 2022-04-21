.data


	_0_pre: .word 0



.text
.globl main
_Println:
	jr $ra
_f:
	jr $ra
main:
	li.s $f1, 7.3243245
	cvt.w.s $f2, $f1
	mfc1 $a0, $f2
	li $v0, 1
	syscall
	mtc1 $a0, $f3
	cvt.s.w $f12, $f3
	li $v0, 2
	syscall
	addi $sp, $sp, -4
	sw $t9, ($sp)
	li $v0, 10
	syscall
