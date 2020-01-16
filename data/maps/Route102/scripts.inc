Route102_MapScripts:: @ 81EC0E0
	.byte 0

Route102_EventScript_1EC0E1:: @ 81EC0E1
	msgbox Route102_Text_1EC2C0, MSGBOX_NPC
	end

Route102_EventScript_1EC0EA:: @ 81EC0EA
	msgbox Route102_Text_1EC35B, MSGBOX_SIGN
	end

Route102_EventScript_1EC0F3:: @ 81EC0F3
	msgbox Route102_Text_1EC373, MSGBOX_SIGN
	end

Route102_EventScript_1EC0FC:: @ 81EC0FC
	msgbox Route102_Text_1EC32E, MSGBOX_NPC
	end

Route102_EventScript_1EC105:: @ 81EC105
	trainerbattle_single TRAINER_CALVIN_1, Route102_Text_294513, Route102_Text_29457C, Route102_EventScript_1EC146
	specialvar VAR_RESULT, ShouldTryRematchBattle
	compare VAR_RESULT, 1
	goto_if_eq Route102_EventScript_1EC19C
	setvar VAR_0x8004, 318
	specialvar VAR_RESULT, sub_813B4E0
	compare VAR_RESULT, 0
	goto_if_eq Route102_EventScript_1EC170
	msgbox Route102_Text_2945AC, MSGBOX_DEFAULT
	release
	end

Route102_EventScript_1EC146:: @ 81EC146
	special sub_80B4808
	waitmovement 0
	goto_if_set FLAG_HAS_MATCH_CALL, Route102_EventScript_1EC157
	release
	end

Route102_EventScript_1EC157:: @ 81EC157
	msgbox Route102_Text_294668, MSGBOX_DEFAULT
	register_matchcall TRAINER_CALVIN_1
	release
	end

Route102_EventScript_1EC170:: @ 81EC170
	goto_if_set FLAG_HAS_MATCH_CALL, Route102_EventScript_1EC183
	msgbox Route102_Text_2945AC, MSGBOX_DEFAULT
	release
	end

Route102_EventScript_1EC183:: @ 81EC183
	msgbox Route102_Text_2945EB, MSGBOX_DEFAULT
	register_matchcall TRAINER_CALVIN_1
	release
	end

Route102_EventScript_1EC19C:: @ 81EC19C
	trainerbattle_rematch TRAINER_CALVIN_1, Route102_Text_2946AE, Route102_Text_29470C
	msgbox Route102_Text_29473C, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_1EC1B3:: @ 81EC1B3
	trainerbattle_single TRAINER_RICK, Route102_Text_29480C, Route102_Text_294847
	msgbox Route102_Text_294859, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_1EC1CA:: @ 81EC1CA
	trainerbattle_single TRAINER_TIANA, Route102_Text_29489E, Route102_Text_2948F3
	msgbox Route102_Text_294916, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_1EC1E1:: @ 81EC1E1
	trainerbattle_single TRAINER_ALLEN, Route102_Text_294775, Route102_Text_2947AA
	msgbox Route102_Text_2947DB, MSGBOX_AUTOCLOSE
	end

PetalburgCity_Text_1EC1F8: @ 81EC1F8
	.string "WALLY: {PLAYER}…\n"
	.string "POKéMON hide in tall grass like this,\l"
	.string "don't they?\p"
	.string "Please watch me and see if I can\n"
	.string "catch one properly.\p"
	.string "…Whoa!$"

PetalburgCity_Text_1EC271: @ 81EC271
	.string "WALLY: I did it… It's my…\n"
	.string "My POKéMON!$"

PetalburgCity_Text_1EC297: @ 81EC297
	.string "{PLAYER}, thank you!\n"
	.string "Let's go back to the GYM!$"

Route102_Text_1EC2C0: @ 81EC2C0
	.string "I'm…not very tall, so I sink right\n"
	.string "into tall grass.\p"
	.string "The grass goes up my nose and…\n"
	.string "Fwafwafwafwafwa…\p"
	.string "Fwatchoo!$"

Route102_Text_1EC32E: @ 81EC32E
	.string "I'm going to catch a whole bunch of\n"
	.string "POKéMON!$"

Route102_Text_1EC35B: @ 81EC35B
	.string "ROUTE 102\n"
	.string "{RIGHT_ARROW} OLDALE TOWN$"

Route102_Text_1EC373: @ 81EC373
	.string "ROUTE 102\n"
	.string "{LEFT_ARROW} PETALBURG CITY$"

AlnerwickPass_Sign_RouteSign::
	msgbox AlnerwickPass_Sign_RouteSign_Text_0, MSGBOX_SIGN
	end


AlnerwickPass_TrainerBattle_Lass::
	trainerbattle_single TRAINER_ALNERWICKPASS_LASS, AlnerwickPass_TrainerBattle_Lass_Text_0, AlnerwickPass_TrainerBattle_Lass_Text_1
	msgbox AlnerwickPass_TrainerBattle_Lass_Text_2, MSGBOX_AUTOCLOSE
	end


AlnerwickPass_TrainerBattle_Fisherman::
	trainerbattle_single TRAINER_ALNERWICKPASS_FISHERMAN, AlnerwickPass_TrainerBattle_Fisherman_Text_0, AlnerwickPass_TrainerBattle_Fisherman_Text_1
	msgbox AlnerwickPass_TrainerBattle_Fisherman_Text_2, MSGBOX_AUTOCLOSE
	end


AlnerwickPass_TrainerBattle_Gentleman::
	trainerbattle_single TRAINER_ALNERWICKPASS_GENTLEMAN, AlnerwickPass_TrainerBattle_Gentleman_Text_0, AlnerwickPass_TrainerBattle_Gentleman_Text_1
	msgbox AlnerwickPass_TrainerBattle_Gentleman_Text_2, MSGBOX_AUTOCLOSE
	end


AlnerwickPass_TrainerBattle_RichBoy::
	trainerbattle_single TRAINER_ALNERWICKPASS_RICHBOY, AlnerwickPass_TrainerBattle_RichBoy_Text_0, AlnerwickPass_TrainerBattle_RichBoy_Text_1
	msgbox AlnerwickPass_TrainerBattle_RichBoy_Text_2, MSGBOX_AUTOCLOSE
	end


AlnerwickPass_TrainerBattle_Hiker::
	trainerbattle_single TRAINER_ALNERWICKPASS_HIKER, AlnerwickPass_TrainerBattle_Hiker_Text_0, AlnerwickPass_TrainerBattle_Hiker_Text_1
	msgbox AlnerwickPass_TrainerBattle_Hiker_Text_2, MSGBOX_AUTOCLOSE
	end


AlnerwickPass_TrainerBattle_LittleBoy::
	trainerbattle_single TRAINER_ALNERWICKPASS_LITTLEBOY, AlnerwickPass_TrainerBattle_LittleBoy_Text_0, AlnerwickPass_TrainerBattle_LittleBoy_Text_1
	msgbox AlnerwickPass_TrainerBattle_LittleBoy_Text_2, MSGBOX_AUTOCLOSE
	end


AlnerwickPass_Sign_RouteSign_Text_0:
	.string "{LEFT_ARROW} Alnerwick City\n{RIGHT_ARROW} Davnridge Town$"

AlnerwickPass_TrainerBattle_Lass_Text_0:
	.string "{COLOR RED}Now that we've made eye contact, you\n"
	.string "have to battle me!$"

AlnerwickPass_TrainerBattle_Lass_Text_1:
	.string "Sometimes other trainers are just\n"
	.string "stronger$"

AlnerwickPass_TrainerBattle_Lass_Text_2:
	.string "{COLOR RED}Sometimes other trainers are stronger\n"
	.string "than you think.$"

AlnerwickPass_TrainerBattle_Fisherman_Text_0:
	.string "{COLOR BLUE}Shh!$"

AlnerwickPass_TrainerBattle_Fisherman_Text_1:
	.string "Gah!\n"
	.string "Lost the catch!$"

AlnerwickPass_TrainerBattle_Fisherman_Text_2:
	.string "{COLOR BLUE}You made me lose my catch...$"

AlnerwickPass_TrainerBattle_Gentleman_Text_0:
	.string "{COLOR BLUE}Have you seen any Geodes?$"

AlnerwickPass_TrainerBattle_Gentleman_Text_1:
	.string "Geodudes come from Geode chunks, and\n"
	.string "from there they roam$"

AlnerwickPass_TrainerBattle_Gentleman_Text_2:
	.string "{COLOR BLUE}Geodudes are my favorite Pokémon!$"

AlnerwickPass_TrainerBattle_RichBoy_Text_0:
	.string "{COLOR BLUE}I only use rare Pokémon$"

AlnerwickPass_TrainerBattle_RichBoy_Text_1:
	.string "No!\n"
	.string "My rarest one!$"

AlnerwickPass_TrainerBattle_RichBoy_Text_2:
	.string "{COLOR BLUE}My mother and father collect rare\n"
	.string "Pokémon, and they give me their\l"
	.string "favorites!$"

AlnerwickPass_TrainerBattle_Hiker_Text_0:
	.string "{COLOR BLUE}These hills are fantastic for amateur\n"
	.string "hikers!$"

AlnerwickPass_TrainerBattle_Hiker_Text_1:
	.string "Wow!\n"
	.string "With that team, you could be a great\l"
	.string "hiker!$"

AlnerwickPass_TrainerBattle_Hiker_Text_2:
	.string "{COLOR BLUE}These hills is where I learned I wanted\n"
	.string "to become a hiker!$"

AlnerwickPass_TrainerBattle_LittleBoy_Text_0:
	.string "{COLOR BLUE}My mommy gave me a Pokémon!$"

AlnerwickPass_TrainerBattle_LittleBoy_Text_1:
	.string "Meanie!$"

AlnerwickPass_TrainerBattle_LittleBoy_Text_2:
	.string "{COLOR BLUE}My mommy gave me that Pokémon!$"
