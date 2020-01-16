OdaleTown_Library_MapScripts::
	.byte 0

AlnerwickLibrary_Girl::
	lock
	faceplayer
	msgbox AlnerwickLibrary_Girl_Text_0, MSGBOX_AUTOCLOSE
	applymovement 3, Common_Movement_WalkInPlaceUp
	waitmovement 0
	end


AlnerwickLibrary_FatMan::
	lock
	faceplayer
	msgbox AlnerwickLibrary_FatMan_Text_0, MSGBOX_AUTOCLOSE
	applymovement 5, Common_Movement_WalkInPlaceUp
	waitmovement 0
	end


AlnerwickLibrary_Artist::
	lock
	faceplayer
	compare VAR_ALNERWICKLIBRARY_EVENT, 0
	goto_if_eq AlnerwickLibrary_Artist_1
	msgbox AlnerwickLibrary_Artist_Text_1, MSGBOX_AUTOCLOSE
	applymovement 4, Common_Movement_WalkInPlaceUp
	waitmovement 0
	end

AlnerwickLibrary_Artist_1:
	msgbox AlnerwickLibrary_Artist_Text_0, MSGBOX_NPC
	end


AlnerwickLibrary_Boy::
	msgbox AlnerwickLibrary_Boy_Text_0, MSGBOX_NPC
	end


AlnerwickLibrary_Librarian::
	msgbox AlnerwickLibrary_Librarian_Text_0, MSGBOX_AUTOCLOSE
	applymovement 2, Common_Movement_WalkInPlaceUp
	waitmovement 0
	end


AlnerwickLibrary_TeamProto_Event::
	compare VAR_ALNERWICKLIBRARY_EVENT, 0
	goto_if_eq AlnerwickLibrary_TeamProto_Event_1
	return

AlnerwickLibrary_TeamProto_Event_1:
	lockall
	applymovement 1, Common_Movement_WalkInPlaceLeft
	waitmovement 0
	delay 10
	msgbox AlnerwickLibrary_TeamProto_Event_Text_0
	closemessage
	applymovement 2, Common_Movement_WalkInPlaceRight
	waitmovement 0
	delay 10
	msgbox AlnerwickLibrary_TeamProto_Event_Text_1
	closemessage
	applymovement 1, Common_Movement_WalkInPlaceLeft
	waitmovement 0
	delay 10
	msgbox AlnerwickLibrary_TeamProto_Event_Text_2
	closemessage
	applymovement 1, Common_Movement_WalkInPlaceLeft
	waitmovement 0
	delay 5
	applymovement 2, Common_Movement_ExclamationMark
	playse SE_PIN
	waitmovement 0
	delay 10
	msgbox AlnerwickLibrary_TeamProto_Event_Text_3
	closemessage
	msgbox AlnerwickLibrary_TeamProto_Event_Text_4
	closemessage
	getplayerxy VAR_TEMP_0, VAR_TEMP_1
	compare VAR_TEMP_1, 5
	goto_if_eq AlnerwickLibrary_TeamProto_Event_4
	compare VAR_TEMP_1, 6
	goto_if_eq AlnerwickLibrary_TeamProto_Event_5
	compare VAR_TEMP_1, 7
	goto_if_eq AlnerwickLibrary_TeamProto_Event_6
AlnerwickLibrary_TeamProto_Event_3:
	msgbox AlnerwickLibrary_TeamProto_Event_Text_5
	closemessage
	trainerbattle_no_intro TRAINER_PROTOGRUNT_1, AlnerwickLibrary_TeamProto_Event_Text_6
	applymovement 1, Common_Movement_WalkInPlaceRight
	waitmovement 0
	delay 10
	msgbox AlnerwickLibrary_TeamProto_Event_Text_7
	closemessage
	fadescreen 3
	removeobject 1
	playse SE_W100
	delay 5
	playse SE_TK_WARPOUT
	fadescreen 2
	delay 10
	applymovement 2, AlnerwickLibrary_TeamProto_Movement_3
	waitmovement 0
	compare VAR_TEMP_1, 5
	goto_if_eq AlnerwickLibrary_TeamProto_Event_11
	compare VAR_TEMP_1, 6
	goto_if_eq AlnerwickLibrary_TeamProto_Event_12
	compare VAR_TEMP_1, 7
	goto_if_eq AlnerwickLibrary_TeamProto_Event_13
AlnerwickLibrary_TeamProto_Event_10:
	msgbox AlnerwickLibrary_TeamProto_Event_Text_8
	closemessage
	compare VAR_TEMP_1, 5
	goto_if_eq AlnerwickLibrary_TeamProto_Event_18
	compare VAR_TEMP_1, 6
	goto_if_eq AlnerwickLibrary_TeamProto_Event_19
	compare VAR_TEMP_1, 7
	goto_if_eq AlnerwickLibrary_TeamProto_Event_20
AlnerwickLibrary_TeamProto_Event_17:
	setvar VAR_ALNERWICKLIBRARY_EVENT, 1
	setflag FLAG_ALNERWICKLIBRARY_EVENT
	releaseall
	end

AlnerwickLibrary_TeamProto_Event_4:
	applymovement 1, AlnerwickLibrary_TeamProto_Movement_0
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_3

AlnerwickLibrary_TeamProto_Event_5:
	applymovement 1, AlnerwickLibrary_TeamProto_Movement_1
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_3

AlnerwickLibrary_TeamProto_Event_6:
	applymovement 1, AlnerwickLibrary_TeamProto_Movement_2
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_3

AlnerwickLibrary_TeamProto_Event_11:
	applymovement 2, AlnerwickLibrary_TeamProto_Movement_0
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_10

AlnerwickLibrary_TeamProto_Event_12:
	applymovement 2, AlnerwickLibrary_TeamProto_Movement_1
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_10

AlnerwickLibrary_TeamProto_Event_13:
	applymovement 2, AlnerwickLibrary_TeamProto_Movement_2
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_10

AlnerwickLibrary_TeamProto_Event_18:
	applymovement 2, AlnerwickLibrary_TeamProto_Movement_4
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_17

AlnerwickLibrary_TeamProto_Event_19:
	applymovement 2, AlnerwickLibrary_TeamProto_Movement_5
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_17

AlnerwickLibrary_TeamProto_Event_20:
	applymovement 2, AlnerwickLibrary_TeamProto_Movement_6
	waitmovement 0
	goto AlnerwickLibrary_TeamProto_Event_17


AlnerwickLibrary_TeamProto_Movement_0:
	walk_down
	walk_right
	step_end

AlnerwickLibrary_TeamProto_Movement_1:
	walk_down
	walk_down
	walk_right
	step_end

AlnerwickLibrary_TeamProto_Movement_2:
	walk_down
	walk_down
	walk_down
	walk_right
	step_end

AlnerwickLibrary_TeamProto_Movement_3:
	walk_right
	step_end

AlnerwickLibrary_TeamProto_Movement_4:
	walk_left
	walk_left
	walk_up
	walk_up
	step_end

AlnerwickLibrary_TeamProto_Movement_5:
	walk_left
	walk_left
	walk_up
	walk_up
	walk_up
	step_end

AlnerwickLibrary_TeamProto_Movement_6:
	walk_left
	walk_left
	walk_up
	walk_up
	walk_up
	walk_up
	step_end

AlnerwickLibrary_Girl_Text_0:
	.string "{COLOR RED}There are so many old books in this\n"
	.string "library!\p"
	.string "Look! I just found a book from 127\n"
	.string "years ago!$"

AlnerwickLibrary_FatMan_Text_0:
	.string "{COLOR BLUE}I'm trying to find {COLOR GREEN}Prof. Cypress'{COLOR BLUE}\n"
	.string "recently published book about\l"
	.string "fossilization.$"

AlnerwickLibrary_Artist_Text_0:
	.string "{COLOR RED}I wonder what that thug wants from\n"
	.string "this old library...$"

AlnerwickLibrary_Artist_Text_1:
	.string "{COLOR RED}That thug wanted an {COLOR GREEN}Ancient Tome{COLOR RED}?\p"
	.string "How interesting, since that thug\n"
	.string "probably doesn't even know how to read\l"
	.string "it!$"

AlnerwickLibrary_Boy_Text_0:
	.string "{COLOR BLUE}My mom forces me to play outside, but\n"
	.string "instead I come in here!\p"
	.string "I dunno, I think I'm more of an indoor\n"
	.string "person.$"

AlnerwickLibrary_Librarian_Text_0:
	.string "Librarian: {COLOR RED}The book that Grunt stole is\n"
	.string "written in an ancient language.\p"
	.string "It has yet to be translated, I don't\n"
	.string "think he can do much with that.$"

AlnerwickLibrary_TeamProto_Event_Text_0:
	.string "Grunt: {COLOR BLUE}I'm not gonna ask again old hag!\p"
	.string "Hand over that book!$"

AlnerwickLibrary_TeamProto_Event_Text_1:
	.string "Librarian: {COLOR RED}I'm sorry sir, but this book\n"
	.string "cannot be purchased nor checked out.\l"
	.string "This shelf here is for historical\l"
	.string "purposes only.$"

AlnerwickLibrary_TeamProto_Event_Text_2:
	.string "Grunt: {COLOR BLUE}Does it look like I care about\n"
	.string "history, old lady?\p"
	.string "{COLOR GREEN}Team Proto{COLOR BLUE} is going to write it's own\n"
	.string "history!\p"
	.string "{COLOR DARK_GREY}Grunt: {COLOR BLUE}Now, I'll be taking this!$"

AlnerwickLibrary_TeamProto_Event_Text_3:
	.string "The Grunt took the Ancient Tome from\n"
	.string "the Librarian.$"

AlnerwickLibrary_TeamProto_Event_Text_4:
	.string "Grunt: {COLOR BLUE}Hopefully our Boss will be fond\n"
	.string "of this find!$"

AlnerwickLibrary_TeamProto_Event_Text_5:
	.string "Grunt: {COLOR BLUE}What are you doin' kid?\n"
	.string "Eavesdroppin'?\p"
	.string "{COLOR DARK_GREY}Grunt: {COLOR BLUE}This is grown-up talk, now scram!$"

AlnerwickLibrary_TeamProto_Event_Text_6:
	.string "Huh...\n"
	.string "Y'Sure are strong for a kid.$"

AlnerwickLibrary_TeamProto_Event_Text_7:
	.string "Grunt: {COLOR BLUE}Did you think this little battle\n"
	.string "was gonna encourage me to return this\l"
	.string "book?\p"
	.string "{COLOR DARK_GREY}Grunt: {COLOR BLUE}Ha! Nope!\n"
	.string "Abra, use Teleport!$"

AlnerwickLibrary_TeamProto_Event_Text_8:
	.string "Librarian: {COLOR RED}Valiant effort young one.\n"
	.string "I can tell you are talented.\p"
	.string "{COLOR DARK_GREY}Librarian: {COLOR RED}I appreciate your effort in\n"
	.string "helping me keep that piece of history,\l"
	.string "but realistically that book is a bunch\l"
	.string "of jibber-jabber.\p"
	.string "Nothing in there is worth his time, as\n"
	.string "it's written in an ancient language,\l"
	.string "which no one understands.\p"
	.string "{COLOR DARK_GREY}Librarian: {COLOR RED}Now. I must get back to\n"
	.string "organizing these books.$"
