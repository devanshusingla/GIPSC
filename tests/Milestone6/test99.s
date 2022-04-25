.data



.text
.globl main

_f:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	add $fp, $sp, $0
	addi $sp, $sp, -0
	### Need new register for $f23
	### Going to free register $f23
	###STACK: 0
	li.s $f23, 2.0
	### Need new register for $t9
	### Going to free register $t9
	###STACK: 0
	li $t9, 4
	# $f23, temp_0
	li $a0 8
	li $v0 9
	syscall
	# $f23, temp_0
	swc1 $f23, 0($v0)
	# $t9, temp_1
	sw $t9, 4($v0)
	addi $v1, $0, 8
	j _return_f
	_return_f:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	jr $ra
_g:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	addi $sp, $sp, -4
	sw $fp, 0($sp)
	add $fp, $sp, $0
	addi $sp, $sp, -0
	### Need new register for $f22
	### Going to free register $f22
	###STACK: 0
	li.s $f22, 6.43
	# $f22, temp_2
	mov.s $f0, $f22
	j _return_g
	_return_g:
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
	addi $sp, $sp, -8
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
	### Need new register for $f21
	### Going to free register $f21
	###STACK: -88
	lwc1 $f21 0($v0)
	### Need new register for $f20
	### Going to free register $f20
	###STACK: -88
	mov.s $f20, $f21
	### Need new register for $t8
	### Going to free register $t8
	###STACK: -88
	lw $t8, 4($v0)
	### Need new register for $t7
	### Going to free register $t7
	###STACK: -88
	addi $t7, $t8, 0
	# $f20, temp_3
	swc1 $f20, -4($fp)
	# $t7, temp_4
	sw $t7, -8($fp)
	### Need new register for $f11
	### Going to free register $f11
	###STACK: -88
	li.s $f11, 1.0
	### Need new register for $f10
	### Going to free register $f10
	###STACK: -88
	### Need new register for $f9
	### Going to free register $f9
	###STACK: -88
	lwc1 $f9, -4($fp)
	# $f11, temp_5
	### Need new register for $f8
	### Going to free register $f8
	###STACK: -88
	add.s $f8, $f9, $f11
	mov.s $f10, $f8
	### Need new register for $f7
	### Going to free register $f7
	###STACK: -88
	mov.s $f7, $f10
	swc1 $f7, -4($fp)
	### Need new register for $t6
	### Going to free register $t6
	###STACK: -88
	li $t6, 2
	### Need new register for $f6
	### Going to free register $f6
	###STACK: -88
	lwc1 $f6, -4($fp)
	mov.s $f12, $f6
	li $v0, 2
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
	### Need new register for $f5
	### Going to free register $f5
	###STACK: -32
	li.s $f5, 4.0
	### Need new register for $t5
	### Going to free register $t5
	###STACK: -32
	### Need new register for $f4
	### Going to free register $f4
	###STACK: -32
	lwc1 $f4, -4($fp)
	# $f5, temp_7
	### Need new register for $f3
	### Going to free register $f3
	###STACK: -32
	c.lt.s $f5, $f4
	cfc1 $t5,  $f31
	### Need new register for $t4
	### Going to free register $t4
	###STACK: -32
	add $t4, $t5, $0
	beqz $t4, else_21
	### Need new register for $t3
	### Going to free register $t3
	###STACK: -32
	li $t3, 1
	### Need new register for $t2
	### Going to free register $t2
	###STACK: -32
	li $t2, 5
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
	#### YAYYY temp_10
	### offset: [0, '$t2'], temp_10
	add $a0, $t2, $0
	### STACK: -88
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
	j end_21
else_21:
	### Need new register for $t1
	### Going to free register $t1
	###STACK: -32
	li $t1, 1
	### Need new register for $t0
	### Going to free register $t0
	###STACK: -32
	li $t0, 4
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
	#### YAYYY temp_12
	### offset: [0, '$t0'], temp_12
	add $a0, $t0, $0
	### STACK: -88
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
end_21:
	_return_main:
	lw $ra, 4($fp)
	addi $sp, $fp, 8
	lw $fp, 0($fp)
	li $v0 10
	syscall
