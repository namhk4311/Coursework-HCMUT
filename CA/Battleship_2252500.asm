.data
	
	firstP: .space 196
	secondP: .space 196
	welcome: .asciiz "                        ================== WELCOME TO THE BATTLESHIP GAME ==================\n"
	size: .word 7
	datasize: .word 4
	rowbow: .asciiz "Row index (bow): "
	rowstern: .asciiz "Row index (stern): "
	columnbow: .asciiz "Column index (bow): "
	columnstern: .asciiz "Column index (stern): "
	row_type: .asciiz "Row: "
	column_type: .asciiz "Column: "
	
	strInput: .space 100
	
	message1: .asciiz "Please setup your ships"
	first_player_: .asciiz "Player 1: "
	second_player_: .asciiz "Player 2: "
	newline: .asciiz "\n"
	space: .asciiz " "
	confirm: .asciiz "Confirm? (press: Y for YES, N for NO): "
	playerseparation: .asciiz "#############################################\n"
	
	print_2x1announce: .asciiz "\n2x1 ships:\n\n"
	print_3x1announce: .asciiz "3x1 ships:\n\n"
	print_4x1announce: .asciiz "4x1 ship:\n\n"
	
	print_2x1_former: .asciiz "Please set your 2x1 ship ("
	print_2x1_latter: .asciiz " ship(s) left)"
	
	print_3x1_former: .asciiz "Please set your 3x1 ship ("
	print_3x1_latter: .asciiz " ship(s) left)"
	
	print_4x1: .asciiz "Please set your 4x1 ship (1 ship(s) left)"
	
	prompt_type_position_attack: .asciiz "Please enter row and column you want to attack: \n"
	
	frame:  .asciiz     "   ====\n"
	hit_response: .asciiz "   HIT!\n"
	miss_response: .asciiz "   MISS!\n"
	
	#exception
	negative: .asciiz "ERROR! The input must NOT be a negative integer, try again!\n"
	out_range: .asciiz "ERROR! The input must NOT be OUT OF RANGE or any CHARACTER. Just enter a digit from 0 to 6, try again!\n"
	print_diagonal: .asciiz "ERROR! The ship must NOT be set diagonally, please enter the coordinate of the ship again:\n----------------------------------------------\n"
	print_overlap: .asciiz "ERROR! The ship must NOT overlap the other ship, please enter the coordinate of the ship again:\n----------------------------------------------\n"
	print_size_error: .asciiz "ERROR! The ship is in the WRONG size, please enter the coordinate of the ship again:\n----------------------------------------------\n"
	no_input_enter: .asciiz "You haven't entered anything, try again!\n"
	no_more_1digit: .asciiz "ERROR! No MORE than 1 digit is allowed, try again!\n"
	no_use_char: .asciiz "ERROR! Entering any character is not allowed, just enter a number digit only, try again!\n"
	
	error_confirm: .asciiz "Only enter (Y) or (N) to confirm, try again!\n"
	
	start_combat: .asciiz "                                   ================== COMBAT ==================\n"
	player1_turn: .asciiz "Player 1's turn:\n"
	player2_turn: .asciiz "Player 2's turn:\n"
	
	player1_win_print: .asciiz "\nPlayer 1 wins. Congratulation!"
	player2_win_print: .asciiz "Player 2 wins. Congratulation!"
	
	
	
	#writing file
	fileout: .asciiz "game_play.txt"
	buffer: .space 1024
	buffer_number: .space 100
.text
main: 
	#open writing file
	li $v0, 13 
  	la $a0, fileout 
 	li $a1, 1 
 	li $a2, 0 
 	syscall 
	move $s6 , $v0 
	#======================
	#la $a1, firstP
	#la $a2, secondP
	lw $t8, size
	lw $t9, datasize 
	
	li $v0, 4
	la $a0, welcome
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , welcome 
	li $a2, 93 
 	syscall 
	#==============================================
	
	#input first player
	li $v0, 4
	la $a0, first_player_
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , first_player_ 
	li $a2, 10
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , newline 
	li $a2, 1 
 	syscall 
	#==============================================
	
	#add $t0, $0, $a1
	la $t0, firstP
	jal input
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , newline
	li $a2, 1 
 	syscall 
	#==============================================
	jal clear_space
	
	li $v0, 4
	la $a0, playerseparation
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , playerseparation
	li $a2, 46 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , newline
	li $a2, 1 
 	syscall 
	#==============================================
	
	#input second player
	li $v0, 4
	la $a0, second_player_
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , second_player_ 
	li $a2, 10 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , newline 
	li $a2, 1 
 	syscall 
	#==============================================
	
	#add $t0, $0, $a2
	la $t0, secondP
	jal input
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , newline 
	li $a2, 1 
 	syscall 
	#==============================================
	
	jal clear_space
	
	#start_combat
	li $v0, 4
	la $a0, start_combat
	syscall	
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , start_combat 
	li $a2, 80 
 	syscall 
	#==============================================
	
	addi $s5, $0, 16 #player1's remain ship
	addi $s3, $0, 16 #player2's remain ship
	
loop_combat:
	
	#player 1 turns:
	li $v0, 4
	la $a0, player1_turn
	syscall 
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, player1_turn  
	li $a2, 17 
 	syscall 
	#==============================================
	
	la $t0, secondP
	jal attack
	beq $s3, 0, player1_win 
	
	li $v0, 4
	la $a0, newline
	syscall

	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline 
	li $a2, 1 
 	syscall 
	#==============================================
	
	#player 2 turns:
	li $v0, 4
	la $a0, player2_turn
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, player2_turn  
	li $a2, 17 
	syscall 
	#==============================================
	
	la $t0, firstP
	jal attack
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline  
	li $a2, 1 
 	syscall 
	#==============================================
	
	beq $s5, 0, player2_win
	
	
	j loop_combat
player1_win:
	li $v0, 4
	la $a0, player1_win_print
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , player1_win_print 
	li $a2, 30 
 	syscall 
	#==============================================
	j exit
player2_win:
	li $v0, 4
	la $a0, player2_win_print
	syscall

	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , player2_win_print 
	li $a2, 29 
 	syscall 
	#==============================================

exit:	
	#close writing file
	li $v0 , 16 
	move $a0 , $s6 
 	syscall 	
 	#===============================
	li $v0, 10
	syscall
#======================= clear area ==================================
clear_space:
	addi $sp, $sp, -4
	sw $t1, 0($sp)
	addi $t1, $0, 100
loop_clear:
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , newline 
	li $a2, 1
 	syscall 
	#==============================================
	addi $t1, $t1, -1
	beq $t1, 0, end_loop_clear
	j loop_clear
end_loop_clear:
	lw $t1, 0($sp)
	addi $sp, $sp, 4
	jr $ra			
			
#======================== INPUT =======================================
input:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
confirm_no_again:	
	jal insert_2x1
	
	jal insert_3x1
			
	jal insert_4x1
	
	li $v0, 4
	la $a0, newline
	syscall	
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline 
	li $a2, 1 
 	syscall 
	#==============================================	
	jal out_data	

	
confirm_again:
	li $v0, 4
	la $a0, confirm
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, confirm
	li $a2, 39
 	syscall 
	#==============================================
	
	la $a0, strInput
	addi $a1, $0, 100
	li $v0, 8
	syscall
	
	jal count_strInput
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , strInput 
	add $a2, $0, $t4 
 	syscall 
	#==============================================
	
	la $a0, strInput
	lb $t1, 0($a0)
	lb $t2, 1($a0)
	
	beq $t2, 10, continue_confirm
	#if enter other characters that not (Y) or (N) -> error
	li $v0, 4
	la $a0, error_confirm
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, error_confirm
	li $a2, 45
 	syscall 
	#==============================================
	
	j confirm_again
continue_confirm:
	 beq $t1, 89, done_user_input
	 beq $t1, 78, reset_matrix
	 
	 #if enter other characters that not (Y) or (N) -> error
	li $v0, 4
	la $a0, error_confirm
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, error_confirm
	li $a2, 45
 	syscall 
	#==============================================
	j confirm_again
reset_matrix:
	jal reset_matrix_board
	#jal out_data
	j confirm_no_again
done_user_input:
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	jr $ra
	
reset_matrix_board:
	addi $sp, $sp, -16
	sw $t1, 0($sp)
	sw $t2, 4($sp)
	sw $t3, 8($sp)
	sw $ra, 12($sp)
	
	addi $t1, $0, 0
	addi $t3, $0, 0
loop_reset:
	beq $t1, 49, done_reset
	sll $t2, $t1, 2
	add $t2, $t0, $t2 #matrix[idx]
	sw $t3, 0($t2)
	addi $t1, $t1, 1
	j loop_reset
done_reset:
	lw $t1, 0($sp)
	lw $t2, 4($sp)
	lw $t3, 8($sp)
	lw $ra, 12($sp)
	addi $sp, $sp, 16
	jr $ra

#====================== 2x1 input =========================
insert_2x1:
	addi $sp, $sp, -16
	sw $t2, 0($sp)
	sw $t3, 4($sp)
	sw $ra, 8($sp)
	sw $t4, 12($sp)
	
	addi $t2, $0, 1 #distance of 2 rows/ 2 columns 
	addi $t3, $0, 3 #number of 2x1 ship
	
	li $v0, 4
	la $a0, print_2x1announce
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_2x1announce
	li $a2, 13 
 	syscall 
	#==============================================
	
loop_insert2x1:	
	li $v0, 4
	la $a0, print_2x1_former
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_2x1_former  
	li $a2, 26 
 	syscall 
	#==============================================
	
	add $a0, $0, $t3
	li $v0, 1
	syscall
	
	#ascii convert -> write in the file
	addi $t4, $t3, 48
	la $a0, buffer_number
	sb $t4, 0($a0)
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, buffer_number  
	li $a2, 1 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, print_2x1_latter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_2x1_latter  
	li $a2, 14 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline 
	li $a2, 1 
 	syscall 
	#==============================================
	
	jal start_input
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline 
	li $a2, 1 
 	syscall 
	#==============================================
	
	addi $t3, $t3, -1
	bne $t3, 0, loop_insert2x1
	
	lw $t2, 0($sp)
	lw $t3, 4($sp)
	lw $ra, 8($sp)
	lw $t4, 12($sp)
	addi $sp, $sp, 16
	jr $ra
#===================== 3x1 input ========================
insert_3x1:
	addi $sp, $sp, -16
	sw $t2, 0($sp)
	sw $t3, 4($sp)
	sw $ra, 8($sp)
	sw $t4, 12($sp)
	
	addi $t2, $0, 2
	addi $t3, $0, 2 #number of 3x1 ship
	
	li $v0, 4
	la $a0, print_3x1announce
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_3x1announce
	li $a2, 12
 	syscall 
	#==============================================
	
loop_insert3x1:	
	li $v0, 4
	la $a0, print_3x1_former
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
	move $a0 , $s6 
 	la $a1, print_3x1_former 
	li $a2, 26 
 	syscall 
	#==============================================
	
	add $a0, $0, $t3
	li $v0, 1
	syscall
	
	addi $t4, $t3, 48
	la $a0, buffer_number
	sb $t4, 0($a0)
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, buffer_number  
	li $a2, 1 
 	syscall 
	#==============================================

	
	li $v0, 4
	la $a0, print_3x1_latter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_3x1_latter 
	li $a2, 14 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline  
	li $a2, 1 
 	syscall 
	#==============================================
	#start input:
	jal start_input
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline 
	li $a2, 1 
 	syscall 
	#==============================================
	
	addi $t3, $t3, -1
	bne $t3, 0, loop_insert3x1
	
	lw $t2, 0($sp)
	lw $t3, 4($sp)
	lw $ra, 8($sp)
	lw $t4, 12($sp)
	addi $sp, $sp, 16
	jr $ra
		
#=========================== 4x1 input =========================
insert_4x1:
	addi $sp, $sp, -8
	sw $ra, 0($sp)
	sw $t2, 4($sp)
	
	li $v0, 4
	la $a0, print_4x1announce
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_4x1announce
	li $a2, 11 
 	syscall 
	#==============================================
	
	addi $t2, $0, 3
	li $v0, 4
	la $a0, print_4x1
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_4x1 
	li $a2, 41 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, newline
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, newline 
	li $a2, 1 
	syscall 
	#==============================================
	
	jal start_input
	
	lw $ra, 0($sp)
	lw $t2, 4($sp)
	addi $sp, $sp, 8
	jr $ra
#=================================

count_strInput:
 	addi $sp, $sp, -8
 	sw $t0, 0($sp)
 	sw $t1, 4($sp)
 
 	la $t0, strInput
 	addi $t4, $0, 0
loop_count:	
 	addi $t4, $t4, 1
 	lb $t1, 0($t0)
 	beq $t1, 10, done_count
 	addi $t0, $t0, 1
 	j loop_count
done_count:
 	lw $t0, 0($sp)
 	lw $t1, 4($sp)
 	addi $sp, $sp, 8
 	jr $ra
 
#===========
start_input:
	addi $sp, $sp, -44
	sw $ra, 0($sp)
	sw $t5, 4($sp)
	sw $a0, 8($sp)
	sw $s7, 12($sp)
	sw $t7, 16($sp)
	sw $a1, 20($sp)
	sw $s5, 24($sp)
	sw $t1, 28($sp)
	sw $t2, 32($sp)
	sw $t3, 36($sp)
	sw $t4, 40($sp)
initial_input:
#row bow
input_row_bow_again:
	li $v0, 4
	la $a0, rowbow
	syscall
	
	#==================== WRITE ===================
	li $v0, 15 
 	move $a0, $s6 
 	la $a1, rowbow 
	li $a2, 17 
 	syscall 
	#==============================================
	
	la $a0, strInput
	addi $a1, $0, 100
	li $v0, 8
	syscall
	
	jal count_strInput
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , strInput 
	add $a2, $0, $t4 
 	syscall 
	#==============================================
	
	la $a0, strInput
	lb $t1, 0($a0)
	lb $t2, 1($a0)
	lb $t3, 2($a0)
	
	not_enter_rowbow:
	bne $t1, 10, entered_rowbow
	
	li $v0, 4
	la $a0, no_input_enter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_input_enter  
	li $a2, 41 
 	syscall 
	#==============================================
	
	j input_row_bow_again
	
	entered_rowbow:
	bne $t1, 45, no_negativerowbow
	jal exception_negative
	j input_row_bow_again
	
	no_negativerowbow:
	blt $t1, 55, no_out_range_rowbow1 #case input: 7 -> 9
	jal exception_out_of_range
	j input_row_bow_again
	
	no_out_range_rowbow1:	
	beq $t1, 48, continue_no_more_1digit_rowbow #case input: 01, 002, 04, 000003,...
	bgt $t1, 48, jumpto_out_range_rowbow
	
	continue_no_more_1digit_rowbow:
	beq $t2, 10, no_out_range_rowbow2
	jal exception_more_than_1digit
	j input_row_bow_again
	
	jumpto_out_range_rowbow:
	beq $t2, 10, no_out_range_rowbow2 #case input: 10 -> ...
	jal exception_out_of_range
	j input_row_bow_again
	
	no_out_range_rowbow2:
	subi $t1, $t1, 48
	add $s0, $0, $t1
#column bow
	input_column_bow_again:
	li $v0, 4
	la $a0, columnbow
	syscall
	
	
	#==================== WRITE ===================
	li $v0, 15 
 	move $a0, $s6 
 	la $a1, columnbow 
	li $a2, 20 
 	syscall 
	#==============================================
	
	la $a0, strInput
	addi $a1, $0, 100
	li $v0, 8
	syscall
	
	jal count_strInput
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , strInput 
	add $a2, $0, $t4 
 	syscall 
	#==============================================
	
	la $a0, strInput
	lb $t1, 0($a0)
	lb $t2, 1($a0)
	lb $t3, 2($a0)
	
not_enter_columnbow:
	bne $t1, 10, entered_columnbow
	li $v0, 4
	la $a0, no_input_enter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_input_enter  
	li $a2, 41 
 	syscall 
	#==============================================
	
	j input_column_bow_again	
	entered_columnbow:
	bne $t1, 45, no_negativecolumnbow
	jal exception_negative
	j input_column_bow_again
	
	no_negativecolumnbow:
	blt $t1, 55, no_out_range_columnbow1
	jal exception_out_of_range
	j input_column_bow_again
	
	no_out_range_columnbow1:	
	beq $t1, 48, continue_no_more_1digit_columnbow #case input: 01, 002, 04, 000003,...
	bgt $t1, 48, jumpto_out_range_columnbow
	
	continue_no_more_1digit_columnbow:
	beq $t2, 10, no_out_range_columnbow2
	jal exception_more_than_1digit
	j input_column_bow_again
	
	jumpto_out_range_columnbow:
	beq $t2, 10, no_out_range_columnbow2
	jal exception_out_of_range
	j input_column_bow_again
	
	no_out_range_columnbow2:
	subi $t1, $t1, 48
	add $s1, $0, $t1
#row stern
input_row_stern_again:
	li $v0, 4
	la $a0, rowstern
	syscall
	
	#==================== WRITE ===================
	li $v0, 15 
 	move $a0, $s6 
 	la $a1, rowstern 
	li $a2, 19 
 	syscall 
	#==============================================
	
	la $a0, strInput
	addi $a1, $0, 100
	li $v0, 8
	syscall
	
	jal count_strInput
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , strInput 
	add $a2, $0, $t4 
 	syscall 
	#==============================================
	
	la $a0, strInput
	lb $t1, 0($a0)
	lb $t2, 1($a0)
	lb $t3, 2($a0)
	
	
not_enter_rowstern:
	bne $t1, 10, entered_rowstern
	li $v0, 4
	la $a0, no_input_enter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_input_enter 
	li $a2, 41 
 	syscall 
	#==============================================
	
	j input_row_stern_again	
	entered_rowstern:
	bne $t1, 45, no_negativerowstern
	jal exception_negative
	j input_row_stern_again
	
	no_negativerowstern:
	blt $t1, 55, no_out_range_rowstern1
	jal exception_out_of_range
	j input_row_stern_again
	
	no_out_range_rowstern1:	
	beq $t1, 48, continue_no_more_1digit_rowstern #case input: 01, 002, 04, 000003,...
	bgt $t1, 48, jumpto_out_range_rowstern
	
	continue_no_more_1digit_rowstern:
	beq $t2, 10, no_out_range_rowstern2
	jal exception_more_than_1digit
	j input_row_stern_again
	
	jumpto_out_range_rowstern:
	beq $t2, 10, no_out_range_rowstern2
	jal exception_out_of_range
	j input_row_stern_again
	
	no_out_range_rowstern2:
	subi $t1, $t1, 48
	add $s2, $0, $t1
	
#column stern
input_column_stern_again:
	li $v0, 4
	la $a0, columnstern
	syscall
	
	#==================== WRITE ===================
	li $v0, 15 
 	move $a0, $s6 
 	la $a1, columnstern 
	li $a2, 22 
 	syscall 
	#==============================================
	
	la $a0, strInput
	addi $a1, $0, 100
	li $v0, 8
	syscall
	
	jal count_strInput
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , strInput 
	add $a2, $0, $t4 
 	syscall 
	#==============================================
	
	la $a0, strInput
	lb $t1, 0($a0)
	lb $t2, 1($a0)
	lb $t3, 2($a0)
	
	
not_enter_columnstern:
	bne $t1, 10, entered_columnstern
	li $v0, 4
	la $a0, no_input_enter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_input_enter 
	li $a2, 41 
 	syscall 
	#==============================================
	
	j input_column_stern_again	
	
	entered_columnstern:
	bne $t1, 45, no_negativecolumnstern
	jal exception_negative
	j input_column_stern_again
	
	no_negativecolumnstern:
	blt $t1, 55, no_out_range_columnstern1
	jal exception_out_of_range
	j input_column_stern_again
	
	no_out_range_columnstern1:	
	beq $t1, 48, continue_no_more_1digit_columnstern #case input: 01, 002, 04, 000003,...
	bgt $t1, 48, jumpto_out_range_columnstern
	
	continue_no_more_1digit_columnstern:
	beq $t2, 10, no_out_range_columnstern2
	jal exception_more_than_1digit
	j input_column_stern_again
	
	jumpto_out_range_columnstern:
	beq $t2, 10, no_out_range_columnstern2
	jal exception_out_of_range
	j input_column_stern_again
	
	no_out_range_columnstern2:
	subi $t1, $t1, 48
	add $s3, $0, $t1
	
#get back $t2 to get the distance row - row or column - column
	lw $t1, 28($sp)
	lw $t2, 32($sp)
	lw $t3, 36($sp) 		
	#processing input
	#if s0 == s2
	beq $s0, $s2, column
	#if s1 == s3
	beq $s1, $s3, row
	#if s0 != s2 || s1 != s3
	
diagonal_error:
	li $v0, 4
	la $a0, print_diagonal
	syscall
	
	#==================== WRITE ===================
	li $v0, 15 
 	move $a0, $s6 
 	la $a1, print_diagonal 
	li $a2, 138 
 	syscall 
	#==============================================
	
	j initial_input
	
done_input:
	lw $ra, 0($sp)
	lw $t5, 4($sp)
	lw $a0, 8($sp)
	lw $s7, 12($sp)
	lw $t7, 16($sp)
	lw $a1, 20($sp)
	lw $s5, 24($sp)
	lw $t1, 28($sp)
	lw $t2, 32($sp)
	lw $t3, 36($sp)
	lw $t4, 40($sp)
	addi $sp, $sp, 44
	jr $ra
	
#========== processing input ==========================
#================== column ==========================
exception_overlap_column:
	addi $sp, $sp, -24
	sw $t1, 0($sp)
	sw $s4, 4($sp)
	sw $s5, 8($sp)
	sw $ra, 12($sp)
	sw $t5, 16($sp)
	sw $t6, 20($sp)
	
	add $s4, $0, $s1 #initial
	add $s5, $0, $s3 #terminal
	addi $t1, $0, 0
	addi $t6, $0, 0
loop_overlap_column: 	
	mul $t1, $s0, $t8
	add $t1, $t1, $s4
	mul $t1, $t1, $t9
	
	add $t5, $t0, $t1
	
	lw $t6, 0($t5)
	
	beq $t6, 1, overlaped_column
	
	beq $s4, $s5, end_loop_overlap_column
	addi $s4, $s4, 1
	j loop_overlap_column

overlaped_column:
	li $v0, 4
	la $a0, print_overlap
	syscall
	
	#==================== WRITE ===================
	li $v0, 15 
 	move $a0, $s6 
 	la $a1, print_overlap 
	li $a2, 143 
 	syscall 
	#==============================================
	
	addi $s7, $0, 1
end_loop_overlap_column:
	lw $t1, 0($sp)
	lw $s4, 4($sp)
	lw $s5, 8($sp)
	lw $ra, 12($sp)
	lw $t5, 16($sp)
	lw $t6, 20($sp)
	addi $sp, $sp, 24
	jr $ra
	
#=================== row ========================
exception_overlap_row:
	addi $sp, $sp, -24
	sw $t1, 0($sp)
	sw $s4, 4($sp)
	sw $s5, 8($sp)
	sw $ra, 12($sp)
	sw $t5, 16($sp)
	sw $t6, 20($sp)
	
	add $s4, $0, $s0 #initial
	add $s5, $0, $s2 #terminal
	addi $t1, $0, 0
	addi $t6, $0, 0
loop_overlap_row: 	
	mul $t1, $s4, $t8
	add $t1, $t1, $s1
	mul $t1, $t1, $t9
	
	add $t5, $t0, $t1
	
	lw $t6, 0($t5)
	
	beq $t6, 1, overlaped_row
	
	beq $s4, $s5, end_loop_overlap_row
	addi $s4, $s4, 1
	j loop_overlap_row

overlaped_row:
	li $v0, 4
	la $a0, print_overlap
	syscall
	
	#==================== WRITE ===================
	li $v0, 15 
 	move $a0, $s6 
 	la $a1, print_overlap 
	li $a2, 143 
 	syscall 
	#==============================================
	
	addi $s7, $0, 1
end_loop_overlap_row:
	lw $t1, 0($sp)
	lw $s4, 4($sp)
	lw $s5, 8($sp)
	lw $ra, 12($sp)
	lw $t5, 16($sp)
	lw $t6, 20($sp)
	addi $sp, $sp, 24
	jr $ra
	
	
	
#--------------------------------------------
#$t6 has been use for load and store 1
column:
	sub $s7, $s1, $s3
	blt $s7, $0, continue_column
	add $s7, $0, $s1
	add $s1, $0, $s3
	add $s3, $0, $s7
	
	

continue_column:


	#exception wrong size
	sub $s7, $s3, $s1
	bne $s7, $t2, exception_size_error
	#exception overlap
	addi $s7, $0, 0
	jal exception_overlap_column
	beq $s7, 1, initial_input #enter input again
	
	add $s4, $0, $s1 #initial
	add $s5, $0, $s3 #terminal
	addi $t1, $0, 0
loop_column:	
	mul $t1, $s0, $t8
	add $t1, $t1, $s4
	mul $t1, $t1, $t9
	
	add $t5, $t0, $t1 # array[s4][s2], s2 == s0 same row
	addi $t6, $0, 1
	sw $t6, 0($t5) 

	beq $s4, $s5, done_loop_column
	addi $s4, $s4, 1
	j loop_column
done_loop_column:	
	j done_input
#----------------------------------------
row:
	sub $s7, $s0, $s2
	blt $s7, $0, continue_row
	add $s7, $0, $s0
	add $s0, $0, $s2
	add $s2, $0, $s7

continue_row:
	#exception wrong size
	sub $s7, $s2, $s0
	bne $s7, $t2, exception_size_error
	#exception overlap
	addi $s7, $0, 0
	jal exception_overlap_row
	beq $s7, 1, initial_input #enter input again
	
	add $s4, $0, $s1 #initial
	add $s5, $0, $s3 #terminal
	addi $t1, $0, 0
	add $s4, $0, $s0 #initial
	add $s5, $0, $s2 #terminal
	addi $t1, $0, 0
loop_row:	
	mul $t1, $s4, $t8
	add $t1, $t1, $s1
	mul $t1, $t1, $t9
	
	add $t5, $t0, $t1 # array[s4][s2], s2 == s0 same row
	addi $t6, $0, 1
	sw $t6, 0($t5) 
	
		
	beq $s4, $s5, done_loop_row
	addi $s4, $s4, 1
	j loop_row
done_loop_row:	
	j done_input
		
#=================================================================

#======================== OUTPUT ===========================================	

out_data:
	addi $sp, $sp, -12
	sw $t1, 0($sp)
	sw $t5, 4($sp)
	sw $t6, 8($sp)
	
	
	addi $t1, $0, 0 #count_num_of_element
	addi $t5, $0, 0 #count_num_of_row
	addi $t6, $0, 0 #count_num_of_column
print_array:
	beq $t1, 49, end
	sll $t2, $t1, 2
	add $t3, $t0, $t2
	lw $t4, 0($t3)
	
	add $a0, $0, $t4
	li $v0, 1
	syscall
	
	li $v0, 4
	la $a0, space
	syscall
	
	
	addi $t1, $t1, 1
	addi $t5, $t5, 1
	beq $t5, 7, next_line
	j print_array
next_line:
	addi $t5, $0, 0
	addi $t6, $t6, 1
	
	li $v0, 4
	la $a0, newline
	syscall
	
	bne $t6, 7, print_array
end:	
	lw $t1, 0($sp)
	lw $t5, 4($sp)
	lw $t6, 8($sp)
	addi $sp, $sp, 12
	jr $ra
#================ ATTACK ========================
attack:
	addi $sp, $sp, -44
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	sw $t5, 12($sp)
	sw $t6, 16($sp)
	sw $t7, 20($sp)
	sw $t1, 24($sp)
	sw $t2, 28($sp)
	sw $t3, 32($sp)
	sw $a1, 36($sp)
	sw $s2, 40($sp)
	
	li $v0, 4
	la $a0, prompt_type_position_attack
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6
 	la $a1 , prompt_type_position_attack 
	li $a2, 49 
 	syscall 
	#==============================================

row_again:
	li $v0, 4
	la $a0, row_type
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , row_type 
	li $a2, 5  
 	syscall 
	#==============================================
	
	la $a0, strInput
	addi $a1, $0, 100
	li $v0, 8
	syscall
	
	jal count_strInput
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , strInput 
	add $a2, $0, $t4 
 	syscall 
	#==============================================
	
	la $a0, strInput
	lb $t1, 0($a0)
	lb $t2, 1($a0)
	lb $t3, 2($a0)
	
	
not_enter_row:
	bne $t1, 10, entered_row
	li $v0, 4
	la $a0, no_input_enter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_input_enter 
	li $a2, 41 
 	syscall 
	#==============================================
	
	j row_again	
entered_row:
	bne $t1, 45, no_negativerow
	jal exception_negative
	j row_again
no_negativerow:
	blt $t1, 55, no_out_range_row1
	jal exception_out_of_range
	j row_again
no_out_range_row1:	

	beq $t1, 48, continue_no_more_1digit_row #case input: 01, 002, 04, 000003,...
	bgt $t1, 48, jumpto_out_range_row
continue_no_more_1digit_row:
	beq $t2, 10, no_out_range_row2
	jal exception_more_than_1digit
	j row_again
jumpto_out_range_row:

	beq $t2, 10, no_out_range_row2
	jal exception_out_of_range
	j row_again
no_out_range_row2:
	subi $t1, $t1, 48
	add $s0, $0, $t1
#column	
column_again:
	li $v0, 4
	la $a0, column_type
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , column_type 
	li $a2, 8  
 	syscall 
	#==============================================

	la $a0, strInput
	addi $a1, $0, 100
	li $v0, 8
	syscall
	
	jal count_strInput
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1 , strInput 
	add $a2, $0, $t4 
 	syscall 
	#==============================================
	
	la $a0, strInput
	lb $t1, 0($a0)
	lb $t2, 1($a0)
	lb $t3, 2($a0)
	
not_enter_column:
	bne $t1, 10, entered_column
	li $v0, 4
	la $a0, no_input_enter
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_input_enter  
	li $a2, 41 
 	syscall 
	#==============================================
	
	j column_again	
entered_column:
	bne $t1, 45, no_negativecolumn
	jal exception_negative
	j column_again
no_negativecolumn:
	blt $t1, 55, no_out_range_column1
	jal exception_out_of_range
	j column_again
no_out_range_column1:

	beq $t1, 48, continue_no_more_1digit_column #case input: 01, 002, 04, 000003,...
	bgt $t1, 48, jumpto_out_range_column
continue_no_more_1digit_column:
	beq $t2, 10, no_out_range_column2
	jal exception_more_than_1digit
	j column_again
jumpto_out_range_column:
	
	beq $t2, 10, no_out_range_column2
	jal exception_out_of_range
	j column_again
no_out_range_column2:
	subi $t1, $t1, 48
	add $s1, $0, $t1
#start attacking
	mul $t6, $s0, $t8
	add $t6, $t6, $s1
	mul $t6, $t6, $t9
	
	add $t6, $t6, $t0
	
	lw $t7, 0($t6)
#get_back_player1_matrix
	#lw $a1, 36($sp)
		
	#hit response
	beq $t7, 1, HIT_res
	
	#miss response
	li $v0, 4
	la $a0, frame
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, frame  
	li $a2, 8 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, miss_response
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, miss_response  
	li $a2, 9 
 	syscall 
	#==============================================

	
	li $v0, 4
	la $a0, frame
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, frame  
	li $a2, 8 
 	syscall 
	#==============================================

	
end_attack:	
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	lw $t5, 12($sp)
	lw $t6, 16($sp)
	lw $t7, 20($sp)
	lw $t1, 24($sp)
	lw $t2, 28($sp)
	lw $t3, 32($sp)
	lw $a1, 36($sp)
	lw $s2, 40($sp)
	addi $sp, $sp, 44
	jr $ra
	
HIT_res:
	li $v0, 4
	la $a0, frame
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, frame  
	li $a2, 8 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, hit_response
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, hit_response  
	li $a2, 8 
 	syscall 
	#==============================================
	
	li $v0, 4
	la $a0, frame
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6
 	la $a1, frame  
	li $a2, 8 
 	syscall 
	#==============================================
	
	#set the ceil to 0
	addi $t7, $0, 0
	sw $t7, 0($t6)
	la $s2, firstP
	beq $t0, $s2, player1_attacked #just fixed matrix here
player2_attacked:
	add $s3, $s3, -1
	j end_attack
player1_attacked:
	add $s5, $s5, -1
	j end_attack
	
#=================== exception handling =========================
exception_negative:
	li $v0, 4
	la $a0, negative 
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, negative 
	li $a2, 60 
 	syscall 
	#==============================================
	
	jr $ra
	
exception_out_of_range:
	li $v0, 4
	la $a0, out_range
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, out_range 
	li $a2, 103
 	syscall 
	#==============================================
	
	jr $ra 
exception_size_error:
	li $v0, 4
	la $a0, print_size_error
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, print_size_error 
	li $a2, 132
 	syscall 
	#==============================================
		
	j initial_input

exception_more_than_1digit:
	li $v0, 4
	la $a0, no_more_1digit
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_more_1digit 
	li $a2, 132
 	syscall 
	#==============================================
	 
	jr $ra

exception_char:
	li $v0, 4
	la $a0, no_use_char
	syscall
	
	#==================== WRITE ===================
	li $v0 , 15 
 	move $a0 , $s6 
 	la $a1, no_use_char
	li $a2, 89
 	syscall 
	#==============================================
	jr $ra
#==============================================
