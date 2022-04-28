.data

	_nl: .asciiz "\n"


.text
.globl main

_Print_char:
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
	li $t9, 11
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY arg_[Print_char_-8]
	add $a0, $a0, $0
	li $v0, 11
	syscall
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	_return_Print_char:
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
_Print_int:
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
	li $t8, 1
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY arg_[Print_int_-8]
	add $a0, $a0, $0
	li $v0, 1
	syscall
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	li $t7, 10
	li $t6, '
'
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY temp_3
	### offset: [0, '$t6'], temp_3
	add $a0, $t6, $0
	### STACK: -176
	jal _Print_char
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	_return_Print_int:
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
_Print_float:
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
	li $t5, 2
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY arg_[Print_float_-8]
	add $a0, $a0, $0
	li $v0, 2
	syscall
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	li $t4, 10
	li $t3, '
'
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY temp_6
	### offset: [0, '$t3'], temp_6
	add $a0, $t3, $0
	### STACK: -176
	jal _Print_char
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	_return_Print_float:
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
_Print_string:
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
	li $t2, 4
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY arg_[Print_string_-8]
	add $a0, $a0, $0
	li $v0, 4
	syscall
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	li $t1, 10
	li $t0, '
'
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY temp_9
	### offset: [0, '$t0'], temp_9
	add $a0, $t0, $0
	### STACK: -176
	jal _Print_char
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	_return_Print_string:
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
_Scan_int:
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
	lw $s7, 0($a0)
	li $s6, 5
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	li $v0, 5
	syscall
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	addi $s5, $v0, 0
	sw $s5 0($a0)
	_return_Scan_int:
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
_Scan_char:
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
	lw $s4, 0($a0)
	li $s3, 12
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	li $v0, 12
	syscall
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	addi $s2, $v0, 0
	sw $s2 0($a0)
	_return_Scan_char:
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
_Scan_string:
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
	lw $s1, 0($a0)
	li $s0, 8
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	li $v0, 8
	syscall
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	add $sp, $sp, -4
	sw	$t9,-68($fp)

	addi $t9, $v0, 0
	sw $t9 0($a0)
	_return_Scan_string:
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
_add:
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
	add $sp, $sp, -4
	sw	$t8,-68($fp)

	add $t8, $a0, $a1
	add $sp, $sp, -4
	sw	$t7,-72($fp)

	add $t7, $t8, $0
	add $sp, $sp, -4
	sw	$t6,-76($fp)

	sub $t6, $a0, $a1
	add $sp, $sp, -4
	sw	$t5,-80($fp)

	add $t5, $t6, $0
	# $t7, temp_19
	li $a0 8
	li $v0 9
	syscall
	# $t7, temp_19
	sw $t7, 0($v0)
	# $t5, temp_20
	sw $t5, 4($v0)
	addi $v1, $0, 8
	j _return_add
	_return_add:
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
	addi $sp, $sp, -12
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
	add $sp, $sp, -4
	sw	$t4,-80($fp)

	li $t4, 2
	add $sp, $sp, -4
	sw	$t3,-84($fp)

	li $t3, 3
	add $sp, $sp, -4
	sw	$t2,-88($fp)

	li $t2, 5
	# $t4, temp_21
	sw $t4, -36($fp)
	# $t3, temp_22
	sw $t3, -40($fp)
	# $t2, temp_23
	sw $t2, -44($fp)
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_a
	add $sp, $sp, -4
	sw	$t1,-236($fp)

	lw $t1, -36($fp)
	add $a0, $t1, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_b
	add $sp, $sp, -4
	sw	$t0,-240($fp)

	lw $t0, -40($fp)
	add $a0, $t0, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_c
	add $sp, $sp, -4
	sw	$t9,-244($fp)

	lw $t9, -44($fp)
	add $a0, $t9, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	lw $t8, -36($fp)
	addi $t6, $t8, 0
	add $sp, $sp, -4
	sw	$t7,-104($fp)

	lw $t7, -40($fp)
	add $sp, $sp, -4
	sw	$t5,-108($fp)

	addi $t5, $t7, 0
	add $sp, $sp, -4
	sw	$t4,-112($fp)

	lw $t4, -44($fp)
	add $sp, $sp, -4
	sw	$t3,-116($fp)

	addi $t3, $t4, 0
	# $t6, temp_24
	sw $t6, -40($fp)
	# $t5, temp_25
	sw $t5, -44($fp)
	# $t3, temp_26
	sw $t3, -36($fp)
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_a
	add $sp, $sp, -4
	sw	$t2,-264($fp)

	lw $t2, -36($fp)
	add $a0, $t2, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_b
	lw $t1, -40($fp)
	add $a0, $t1, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_c
	lw $t0, -44($fp)
	add $a0, $t0, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	lw $t9, -36($fp)
	addi $t8, $t9, 0
	lw $t7, -40($fp)
	addi $t4, $t7, 0
	add $sp, $sp, -4
	sw	$t6,-124($fp)

	lw $t6, -44($fp)
	add $sp, $sp, -4
	sw	$t5,-128($fp)

	addi $t5, $t6, 0
	# $t8, temp_27
	sw $t8, -40($fp)
	# $t4, temp_28
	sw $t4, -44($fp)
	# $t5, temp_29
	sw $t5, -36($fp)
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_a
	add $sp, $sp, -4
	sw	$t3,-276($fp)

	lw $t3, -36($fp)
	add $a0, $t3, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_b
	lw $t2, -40($fp)
	add $a0, $t2, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
	#### Saving Floating Point registers
	add $sp, $sp, -4
	swc1 $f1, 0($sp)
	add $sp, $sp, -4
	swc1 $f3, 0($sp)
	add $sp, $sp, -4
	swc1 $f4, 0($sp)
	add $sp, $sp, -4
	swc1 $f5, 0($sp)
	add $sp, $sp, -4
	swc1 $f6, 0($sp)
	add $sp, $sp, -4
	swc1 $f7, 0($sp)
	add $sp, $sp, -4
	swc1 $f8, 0($sp)
	add $sp, $sp, -4
	swc1 $f9, 0($sp)
	add $sp, $sp, -4
	swc1 $f10, 0($sp)
	add $sp, $sp, -4
	swc1 $f11, 0($sp)
	add $sp, $sp, -4
	swc1 $f20, 0($sp)
	add $sp, $sp, -4
	swc1 $f21, 0($sp)
	add $sp, $sp, -4
	swc1 $f22, 0($sp)
	add $sp, $sp, -4
	swc1 $f23, 0($sp)
	#### Done saving Floating Point registers
	#### Saving Floating Point Argument registers
	add $sp, $sp, -4
	swc1 $f12, 0($sp)
	add $sp, $sp, -4
	swc1 $f13, 0($sp)
	add $sp, $sp, -4
	swc1 $f14, 0($sp)
	add $sp, $sp, -4
	swc1 $f15, 0($sp)
	add $sp, $sp, -4
	swc1 $f16, 0($sp)
	add $sp, $sp, -4
	swc1 $f17, 0($sp)
	add $sp, $sp, -4
	swc1 $f18, 0($sp)
	add $sp, $sp, -4
	swc1 $f19, 0($sp)
	#### Done saving Floating Point Argument registers
	#### YAYYY 4_c
	lw $t1, -44($fp)
	add $a0, $t1, $0
	jal _Print_int
	#### Restoring Floating Point Argument registers
	lwc1 $f19, 0($sp)
	add $sp, $sp, 4
	lwc1 $f18, 0($sp)
	add $sp, $sp, 4
	lwc1 $f17, 0($sp)
	add $sp, $sp, 4
	lwc1 $f16, 0($sp)
	add $sp, $sp, 4
	lwc1 $f15, 0($sp)
	add $sp, $sp, 4
	lwc1 $f14, 0($sp)
	add $sp, $sp, 4
	lwc1 $f13, 0($sp)
	add $sp, $sp, 4
	lwc1 $f12, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point Argument registers
	#### Saving restoring Point registers
	lwc1 $f23, 0($sp)
	add $sp, $sp, 4
	lwc1 $f22, 0($sp)
	add $sp, $sp, 4
	lwc1 $f21, 0($sp)
	add $sp, $sp, 4
	lwc1 $f20, 0($sp)
	add $sp, $sp, 4
	lwc1 $f11, 0($sp)
	add $sp, $sp, 4
	lwc1 $f10, 0($sp)
	add $sp, $sp, 4
	lwc1 $f9, 0($sp)
	add $sp, $sp, 4
	lwc1 $f8, 0($sp)
	add $sp, $sp, 4
	lwc1 $f7, 0($sp)
	add $sp, $sp, 4
	lwc1 $f6, 0($sp)
	add $sp, $sp, 4
	lwc1 $f5, 0($sp)
	add $sp, $sp, 4
	lwc1 $f4, 0($sp)
	add $sp, $sp, 4
	lwc1 $f3, 0($sp)
	add $sp, $sp, 4
	lwc1 $f1, 0($sp)
	add $sp, $sp, 4
	#### Done restoring Floating Point registers
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
