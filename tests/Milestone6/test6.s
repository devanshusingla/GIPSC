.data


	_0_pre: .word 0



.text
.globl main
_Println:
	jr $ra
_x:
	beqz $t9, else_23
	jr $ra
	j end_23
else_23:
end_23:
	jr $ra
_dummy:
label_0:
	beqz $t8, else_46
	beqz $t7, else_34
	j label_0
	j end_34
else_34:
end_34:
	jr $ra
	j end_46
else_46:
end_46:
	jr $ra
main:
	li $v0 10
	syscall
