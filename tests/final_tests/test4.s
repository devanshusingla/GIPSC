.data

	_0_pre: .word 0
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
	#### YAYYY arg_[Print_char_-8]
	add $a0, $a0, $0
	li $v0, 11
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
	#### YAYYY arg_[Print_int_-8]
	add $a0, $a0, $0
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
	#### YAYYY temp_4
	### offset: [0, '$t6'], temp_4
	add $a0, $t6, $0
	jal _Print_char
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
	li $t5, 4
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
	#### YAYYY arg_[Print_string_-8]
	add $a0, $a0, $0
	li $v0, 4
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
	#### YAYYY temp_7
	### offset: [0, '$t3'], temp_7
	add $a0, $t3, $0
	jal _Print_char
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
	lw $t2, 0($a0)
	li $t1, 5
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
	li $v0, 5
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
	sw $v0, 0($a0)
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
	lw $t0, 0($a0)
	li $s7, 12
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
	li $v0, 12
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
	sw $v0, 0($a0)
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
	lw $s6, 0($a0)
	li $s5, 8
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
	li $v0, 8
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
	sw $v0, 0($a0)
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
_fibonacci:
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
	li $s4, 0
	# $s4, temp_14
	slt $s3, $a0, $s4
	xori $s3, $s3, 1
	slt $s2, $s4, $a0
	xori $s2, $s2, 1
	and $s3, $s3, $s2
	add $s1, $s3, $0
	li $s0, 1
	add $sp, $sp, -4
	sw	$t9,-68($fp)

	# $s0, temp_16
	add $sp, $sp, -4
	sw	$t8,-72($fp)

	slt $t9, $a0, $s0
	xori $t9, $t9, 1
	slt $t8, $s0, $a0
	xori $t8, $t8, 1
	and $t9, $t9, $t8
	add $sp, $sp, -4
	sw	$t7,-76($fp)

	add $t7, $t9, $0
	add $sp, $sp, -4
	sw	$t6,-80($fp)

	# $s1, temp_15
	# $t7, temp_17
	or $t6, $s1, $t7
	add $sp, $sp, -4
	sw	$t5,-84($fp)

	add $t5, $t6, $0
	beqz $t5, else_8
	add $sp, $sp, -4
	sw	$t4,-88($fp)

	li $t4, 1
	# $t4, temp_19
	addi $v0, $t4, 0
	j _return_fibonacci
	j end_8
else_8:
end_8:
	add $sp, $sp, -4
	sw	$t3,-92($fp)

	li $t3, 1
	add $sp, $sp, -4
	sw	$t2,-96($fp)

	# $t3, temp_20
	sub $t2, $a0, $t3
	add $sp, $sp, -4
	sw	$t1,-100($fp)

	add $t1, $t2, $0
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
	#### YAYYY temp_21
	### offset: [0, '$t1'], temp_21
	add $a0, $t1, $0
	jal _fibonacci
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
	### STACK1: -68, temp_22
	### False
	add $sp, $sp, -4
	sw	$t0,-104($fp)

	### STACK2: -72
	addi $t0, $v0, 0
	li $t9, 2
	# $t9, temp_23
	sub $t8, $a0, $t9
	add $t6, $t8, $0
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
	#### YAYYY temp_24
	### offset: [0, '$t6'], temp_24
	add $a0, $t6, $0
	jal _fibonacci
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
	### STACK1: -72, temp_25
	### False
	add $sp, $sp, -4
	sw	$t7,-108($fp)

	### STACK2: -76
	addi $t7, $v0, 0
	add $sp, $sp, -4
	sw	$t5,-112($fp)

	# $t0, temp_22
	# $t7, temp_25
	add $t5, $t0, $t7
	add $sp, $sp, -4
	sw	$t4,-116($fp)

	add $t4, $t5, $0
	# $t4, temp_26
	addi $v0, $t4, 0
	j _return_fibonacci
	_return_fibonacci:
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
	addi $sp, $sp, -8
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
	addi $t2, $fp, -36
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
	#### YAYYY temp_27
	### offset: [0, '$t2'], temp_27
	add $a0, $t2, $0
	jal _Scan_int
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
	#### YAYYY 6_a
	add $sp, $sp, -4
	sw	$t3,-132($fp)

	lw $t3, -36($fp)
	add $a0, $t3, $0
	jal _fibonacci
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
	### STACK1: -36, temp_28
	### False
	add $sp, $sp, -4
	sw	$t1,-80($fp)

	### STACK2: -40
	addi $t1, $v0, 0
	# $t1, temp_28
	sw $t1, -40($fp)
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
	#### YAYYY 6_b
	lw $t8, -40($fp)
	add $a0, $t8, $0
	jal _Print_int
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
