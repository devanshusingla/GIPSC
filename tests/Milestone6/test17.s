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
main:
	addi $sp, $sp, -128
	add $fp, $sp, $0
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
	li.s $f23, 1.0
	li.s $f22, 4.0
	li.s $f21, 5.60
	# $f22, temp_20
	# $f21, temp_21
	div.s $f11, $f22, $f21
	mov.s $f20, $f11
	mov.s $f10, $f20
	# $f23, temp_19
	# $f10, temp_22
	add.s $f8, $f23, $f10
	mov.s $f9, $f8
	mov.s $f7, $f9
	li.s $f6, 43.0
	li.s $f5, 344.9
	# $f6, temp_24
	# $f5, temp_25
	mul.s $f3, $f6, $f5
	mov.s $f4, $f3
	mov.s $f1, $f4
	# $f7, temp_23
	# $f1, temp_26
	add.s $f22, $f7, $f1
	mov.s $f20, $f22
	mov.s $f21, $f20
	mov.s $f12, $f21
	jal _Print_float
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
