OldaleTown_PokemonCenter_1F_MapScripts:: @ 81FC006
	map_script MAP_SCRIPT_ON_TRANSITION, OldaleTown_PokemonCenter_1F_OnTransition
	map_script MAP_SCRIPT_ON_RESUME, OldaleTown_PokemonCenter_1F_MapScript1_277C30
	.byte 0
    
OldaleTown_PokemonCenter_1F_OnTransition: @ 81FC011
	setrespawn HEAL_LOCATION_OLDALE_TOWN
	call OldaleTown_PokemonCenter_1F_EventScript_2718DE
	end

OldaleTown_PokemonCenter_1F_EventScript_1FC01A:: @ 81FC01A
	setvar VAR_0x800B, 1
	call OldaleTown_PokemonCenter_1F_EventScript_27191E
	waitmessage
	waitbuttonpress
	release
	end

OldaleTown_PokemonCenter_1F_EventScript_1FC028:: @ 81FC028
	msgbox OldaleTown_PokemonCenter_1F_Text_1FC059, MSGBOX_NPC
	end

OldaleTown_PokemonCenter_1F_EventScript_1FC031:: @ 81FC031
	msgbox OldaleTown_PokemonCenter_1F_Text_1FC0CD, MSGBOX_NPC
	end

OldaleTown_PokemonCenter_1F_EventScript_1FC03A:: @ 81FC03A
	lock
	faceplayer
	goto_if_set FLAG_SYS_POKEDEX_GET, OldaleTown_PokemonCenter_1F_EventScript_1FC04F
	msgbox OldaleTown_PokemonCenter_1F_Text_1FC148, MSGBOX_DEFAULT
	release
	end

OldaleTown_PokemonCenter_1F_EventScript_1FC04F:: @ 81FC04F
	msgbox OldaleTown_PokemonCenter_1F_Text_1FC1B9, MSGBOX_DEFAULT
	release
	end

OldaleTown_PokemonCenter_1F_Text_1FC059: @ 81FC059
	.string "That PC in the corner there is\n"
	.string "for any POKéMON TRAINER to use.\p"
	.string "Naturally, that means you're welcome\n"
	.string "to use it, too.$"

OldaleTown_PokemonCenter_1F_Text_1FC0CD: @ 81FC0CD
	.string "POKéMON CENTERS are great!\p"
	.string "You can use their services as much\n"
	.string "as you like, and it's all for free.\l"
	.string "You never have to worry!$"

OldaleTown_PokemonCenter_1F_Text_1FC148: @ 81FC148
	.string "The POKéMON WIRELESS CLUB on\n"
	.string "the second floor was built recently.\p"
	.string "But they say they're still making\n"
	.string "adjustments.$"

OldaleTown_PokemonCenter_1F_Text_1FC1B9: @ 81FC1B9
	.string "The POKéMON WIRELESS CLUB on\n"
	.string "the second floor was built recently.\p"
	.string "I traded POKéMON right away.$"

Global_PokeMart_Shop::
	lock
	message Global_PokeMart_Shop_Text_0
	goto_if_set FLAG_BADGE08_GET, Global_PokeMart_Shop_2
	goto_if_set FLAG_BADGE07_GET, Global_PokeMart_Shop_3
	goto_if_set FLAG_BADGE06_GET, Global_PokeMart_Shop_4
	goto_if_set FLAG_BADGE05_GET, Global_PokeMart_Shop_5
	goto_if_set FLAG_BADGE04_GET, Global_PokeMart_Shop_6
	goto_if_set FLAG_BADGE03_GET, Global_PokeMart_Shop_7
	goto_if_set FLAG_BADGE02_GET, Global_PokeMart_Shop_8
	goto_if_set FLAG_BADGE01_GET, Global_PokeMart_Shop_9
	pokemart Global_PokeMart_BadgeNone
Global_PokeMart_Shop_1:
	release
	end

Global_PokeMart_Shop_2:
	pokemart Global_PokeMart_Badge08
	goto Global_PokeMart_Shop_1

Global_PokeMart_Shop_3:
	pokemart Global_PokeMart_Badge07
	goto Global_PokeMart_Shop_1

Global_PokeMart_Shop_4:
	pokemart Global_PokeMart_Badge06
	goto Global_PokeMart_Shop_1

Global_PokeMart_Shop_5:
	pokemart Global_PokeMart_Badge05
	goto Global_PokeMart_Shop_1

Global_PokeMart_Shop_6:
	pokemart Global_PokeMart_Badge04
	goto Global_PokeMart_Shop_1

Global_PokeMart_Shop_7:
	pokemart Global_PokeMart_Badge03
	goto Global_PokeMart_Shop_1

Global_PokeMart_Shop_8:
	pokemart Global_PokeMart_Badge02
	goto Global_PokeMart_Shop_1

Global_PokeMart_Shop_9:
	pokemart Global_PokeMart_Badge01
	goto Global_PokeMart_Shop_1


Global_PokeMart_Badge08::
    .2byte ITEM_ULTRA_BALL
    .2byte ITEM_GREAT_BALL
    .2byte ITEM_POKE_BALL
    .2byte ITEM_MAX_POTION
    .2byte ITEM_HYPER_POTION
    .2byte ITEM_SUPER_POTION
    .2byte ITEM_POTION
    .2byte ITEM_FULL_HEAL
    .2byte ITEM_REVIVE
    .2byte ITEM_MAX_ETHER
    .2byte ITEM_NONE
    release
    end

Global_PokeMart_Badge07::
    .2byte ITEM_ULTRA_BALL
    .2byte ITEM_GREAT_BALL
    .2byte ITEM_POKE_BALL
    .2byte ITEM_HYPER_POTION
    .2byte ITEM_SUPER_POTION
    .2byte ITEM_POTION
    .2byte ITEM_FULL_HEAL
    .2byte ITEM_ETHER
    .2byte ITEM_NONE
    release
    end

Global_PokeMart_Badge06::
    .2byte ITEM_ULTRA_BALL
    .2byte ITEM_GREAT_BALL
    .2byte ITEM_POKE_BALL
    .2byte ITEM_HYPER_POTION
    .2byte ITEM_SUPER_POTION
    .2byte ITEM_POTION
    .2byte ITEM_ANTIDOTE
    .2byte ITEM_BURN_HEAL
    .2byte ITEM_ICE_HEAL
    .2byte ITEM_AWAKENING
    .2byte ITEM_PARALYZE_HEAL
    .2byte ITEM_NONE
    release
    end 

Global_PokeMart_Badge05::
    .2byte ITEM_GREAT_BALL
    .2byte ITEM_POKE_BALL
    .2byte ITEM_SUPER_POTION
    .2byte ITEM_POTION
    .2byte ITEM_ANTIDOTE
    .2byte ITEM_BURN_HEAL
    .2byte ITEM_AWAKENING
    .2byte ITEM_PARALYZE_HEAL
    .2byte ITEM_NONE
    release
    end 
Global_PokeMart_Badge04::
    .2byte ITEM_GREAT_BALL
    .2byte ITEM_POKE_BALL
    .2byte ITEM_SUPER_POTION
    .2byte ITEM_POTION
    .2byte ITEM_ANTIDOTE
    .2byte ITEM_BURN_HEAL
    .2byte ITEM_PARALYZE_HEAL
    .2byte ITEM_NONE
    release
    end 
Global_PokeMart_Badge03::
    .2byte ITEM_GREAT_BALL
    .2byte ITEM_POKE_BALL
    .2byte ITEM_SUPER_POTION
    .2byte ITEM_POTION
    .2byte ITEM_ANTIDOTE
    .2byte ITEM_PARALYZE_HEAL
    .2byte ITEM_NONE
    release
    end 
Global_PokeMart_Badge02::
    .2byte ITEM_POKE_BALL
    .2byte ITEM_SUPER_POTION
    .2byte ITEM_POTION
    .2byte ITEM_ANTIDOTE
    .2byte ITEM_PARALYZE_HEAL
    .2byte ITEM_NONE
    release
    end 
Global_PokeMart_Badge01::
    .2byte ITEM_POKE_BALL
    .2byte ITEM_POTION
    .2byte ITEM_ANTIDOTE
    .2byte ITEM_PARALYZE_HEAL
    .2byte ITEM_NONE
    release
    end 
Global_PokeMart_BadgeNone::
    .2byte ITEM_POKE_BALL
    .2byte ITEM_POTION
    .2byte ITEM_ANTIDOTE
    .2byte ITEM_PARALYZE_HEAL
    .2byte ITEM_NONE
    release
    end

Global_PokeMart_Shop_Text_0:
	.string "Employee: {COLOR BLUE}Hello!\n"
	.string "What could I interest you in?$"
