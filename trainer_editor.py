#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
import glob
import os.path
import sys

class Party:
    def __init__(self):
        self.mons = [None, None, None, None, None, None]
        self._add_mon_index = 0

    def add_mon(self, mon):
        if self._add_mon_index == 6:
            print(f'Programmer error. {self.identifier} added too many mons', file=sys.stderr)
            sys.exit(1)
        self.mons[self._add_mon_index] = mon
        self._add_mon_index += 1

    def set_mon(self, mon, position):
        mons[position] = mon

    def get_mons_compact(self):
        return [ mon for mon in self.mons if mon is not None ]

    def mons_have_items(self):
        if not hasattr(self, 'mons'):
            return False
        for mon in self.get_mons_compact():
            if mon.has_item():
                return True
        return False

    def mons_have_moves(self):
        if not hasattr(self, 'mons'):
            return False
        for mon in self.get_mons_compact():
            if mon.has_moves():
                return True
        return False

    def revalidate_party(self):
        has_moves = self.mons_have_moves()
        has_items = self.mons_have_items()
        move_string = 'CustomMoves' if has_moves else 'DefaultMoves'
        item_string = 'Item' if has_items else 'NoItem'
        self.party_type = item_string + move_string
        for mon in self.mons:
            if mon is None:
                continue
            if has_moves:
                if not hasattr(mon, 'moves'):
                    mon.moves = ['MOVE_NONE', 'MOVE_NONE', 'MOVE_NONE', 'MOVE_NONE']
            if has_items:
                if not hasattr(mon, 'heldItem'):
                    mon.heldItem = 'ITEM_NONE'

class Trainer:

    def __init__(self):
        self.items = [None, None, None, None]
        self._add_item_index = 0
        self.trainer_class = 'TRAINER_CLASS_YOUNGSTER'
        self.music = 'TRAINER_ENCOUNTER_MUSIC_MALE'
        self.trainer_pic = 'TRAINER_PIC_YOUNGSTER'
        self.double_battle = False
        self.check_bad_move = True
        self.check_viability = True
        self.try_to_faint = True
        self.setup_first_turn = False
        self.risky = False
        self.prefer_strongest_move = False
        self.prefer_baton_pass = False
        self.hp_aware = False
        self.is_female = False

    def add_item(self, item):
        if self._add_item_index == 5:
            print(f'Programmer error. {self.identifier} added too many items', file=sys.stderr)
            sys.exit(1)
        self.items[self._add_item_index] = item
        self._add_item_index += 1

    def get_items_compact(self):
        return [ item for item in self.items if item is not None ]

    def get_ai_flags(self):
        flags = ''
        if self.check_bad_move:
            flags += 'AI_SCRIPT_CHECK_BAD_MOVE | '
        if self.try_to_faint:
            flags += 'AI_SCRIPT_TRY_TO_FAINT | '
        if self.check_viability:
            flags += 'AI_SCRIPT_CHECK_VIABILITY | '
        if self.setup_first_turn:
            flags += 'AI_SCRIPT_SETUP_FIRST_TURN | '
        if self.risky:
            flags += 'AI_SCRIPT_RISKY | '
        if self.prefer_strongest_move:
            flags += 'AI_SCRIPT_PREFER_STRONGEST_MOVE | '
        if self.prefer_baton_pass:
            flags += 'AI_SCRIPT_PREFER_BATON_PASS | '
        if self.hp_aware:
            flags += 'AI_SCRIPT_HP_AWARE | '
        if flags == '':
            flags += '0'
        return flags.rstrip(' |')

    def get_party_flags(self):
        if self.party == None:
            return '0'
        flags = ''
        if self.party.mons_have_items():
            flags += 'F_TRAINER_PARTY_HELD_ITEM | '
        if self.party.mons_have_moves():
            flags += 'F_TRAINER_PARTY_CUSTOM_MOVESET'
        if flags == '':
            flags = '0'
        return flags.rstrip(' |')

class Mon:
    def __init__(self, species='SPECIES_NONE'):
        self.iv = 0
        self.lvl = 1
        self.species = species

    def has_moves(self):
        return hasattr(self, 'moves')

    def has_item(self):
        return hasattr(self, 'heldItem')

    def set_move(self, move, position):
        if not self.has_moves():
            self.moves = ['MOVE_NONE', 'MOVE_NONE', 'MOVE_NONE', 'MOVE_NONE']
        self.moves[position] = move

    def add_item(self, item):
        self.heldItem = item

def parse_party(lines):
    party = Party()
    party.party_type = lines[0].split()[3][len('TrainerMon'):]
    party.identifier = lines[0].split()[4].rstrip('[]')
    mon = Mon()
    for line in lines[2:]:
        tokens = line.split()
        if tokens[-1].rstrip(',') == '}':
            party.add_mon(mon)
            mon = Mon()
        elif tokens[0][0] == '.':
            if tokens[0] == '.moves':
                moves = [move.rstrip(',') for move in tokens[2:] ]
                setattr(mon, 'moves', moves)
            else:
                setattr(mon, tokens[0].lstrip('.'), tokens[-1].rstrip(','))
    return party

def get_parties():
    parties = {}
    with open('src/data/trainer_parties.h') as f:
        party_lines = []
        for line in f:
            if line == '\n':
                continue
            elif line == "};\n":
                party = parse_party(party_lines)
                parties[party.identifier] = party
                party_lines = []
            else:
                party_lines.append(line.rstrip('\n'))
    return parties

def get_trainers(parties):
    trainers = {}
    trainer = Trainer()
    with open('src/data/trainers.h') as f:
        for line in f:
            if line == '};\n':
                break
            tokens = line.split()
            if line == '\n' or tokens[0] == 'const' or tokens[0] == '{':
                continue
            elif tokens[0] == '},':
                trainers[trainer.identifier] = trainer
                trainer = Trainer()
            elif tokens[0][0] == '[':
                trainer.identifier = tokens[0].lstrip('[').rstrip(']')
            elif tokens[0] == '.trainerClass':
                trainer.trainer_class = tokens[-1].rstrip(',')
            elif tokens[0] == '.encounterMusic_gender':
                if tokens[2] == 'F_TRAINER_FEMALE':
                    trainer.is_female = True
                trainer.music = (tokens[-1].rstrip(','))
            elif tokens[0] == '.trainerPic':
                trainer.trainer_pic = tokens[-1].rstrip(',')
            elif tokens[0] == '.trainerName':
                trainer.name = line.split('"')[1]
            elif tokens[0] == '.items':
                if tokens[-1] == '{},':
                    continue
                else:
                    for token in tokens[2:]:
                        trainer.add_item((token.lstrip('{').rstrip('},')))
            elif tokens[0] == '.doubleBattle':
                if tokens[-1] == 'TRUE,':
                    trainer.double_battle = True
                else:
                    trainer.double_battle = False
            elif tokens[0] == '.aiFlags':
                ai_flags = []
                for token in tokens[2:]:
                    if token == '|':
                        continue
                    ai_flags.append(token.rstrip(','))
                trainer.check_bad_move = True if 'AI_SCRIPT_CHECK_BAD_MOVE' in ai_flags else False
                trainer.try_to_faint = True if 'AI_SCRIPT_TRY_TO_FAINT' in ai_flags else False
                trainer.check_viability = True if 'AI_SCRIPT_CHECK_VIABILITY' in ai_flags else False
                trainer.setup_first_turn = True if 'AI_SCRIPT_SETUP_FIRST_TURN' in ai_flags else False
                trainer.risky = True if 'AI_SCRIPT_RISKY' in ai_flags else False
                trainer.prefer_strongest_move = True if 'AI_SCRIPT_PREFER_STRONGEST_MOVE' in ai_flags else False
                trainer.prefer_baton_pass = True if 'AI_SCRIPT_PREFER_BATON_PASS' in ai_flags else False
                trainer.hp_aware = True if 'AI_SCRIPT_HP_AWARE' in ai_flags else False
            elif tokens[0] == '.party':
                party_id = tokens[-1].rstrip('},')
                if party_id != "NULL":
                    trainer.party = parties[party_id]
                else:
                    trainer.party = None
    return trainers

def write_opponents_header(trainers):
    with open('include/constants/opponents.h', 'w') as f:
        print('#ifndef GUARD_CONSTANTS_OPPONENTS_H', file=f)
        print('#define GUARD_CONSTANTS_OPPONENTS_H\n', file=f)
        for count, trainer in enumerate(trainers.values()):
            trainer_string = f'#define {trainer.identifier}'
            print(f'{trainer_string} {count:>{34-len(trainer_string)}}', file=f)
        print(f'\n#define TRAINERS_COUNT {len(trainers):>12}\n', file=f)
        print('#endif  // GUARD_CONSTANTS_OPPONENTS_H', file=f)

def array_text_generator(items):
    string = ''
    for count, item in enumerate(items, start=1):
        if count == len(items):
            string += item
        else:
            string += item + ', '
    return string

def write_trainers_header(trainers):
    with open('src/data/trainers.h', 'w') as f:
        print('const struct Trainer gTrainers[] = {', file=f)
        for count, trainer in enumerate(trainers.values(), start=1):
            gender_flags = ''
            if trainer.is_female:
                gender_flags += 'F_TRAINER_FEMALE | '
            gender_flags += trainer.music
            print(f'    [{trainer.identifier}] =', file=f)
            print('    {', file=f)
            print(f'        .partyFlags = {trainer.get_party_flags()},', file=f)
            print(f'        .trainerClass = {trainer.trainer_class},', file=f)
            print(f'        .encounterMusic_gender = {gender_flags},', file=f)
            print(f'        .trainerPic = {trainer.trainer_pic},', file=f)
            print(f'        .trainerName = _("{trainer.name}"),', file=f)
            if not hasattr(trainer, 'items'):
                print('        .items = {{}},', file=f)
            else:
                print(f'        .items = {{{array_text_generator(trainer.get_items_compact())}}},', file=f)
            print(f'        .doubleBattle = {"TRUE" if trainer.double_battle else "FALSE"},', file=f)
            print(f'        .aiFlags = {trainer.get_ai_flags()},', file=f)
            print(f'        .partySize = {"0" if trainer.identifier == "TRAINER_NONE" else f"ARRAY_COUNT({trainer.party.identifier})"},', file=f)
            if trainer.identifier == 'TRAINER_NONE':
                print('        .party = {.NoItemDefaultMoves = NULL},', file=f)
            else:
                print(f'        .party = {{.{trainer.party.party_type} = {trainer.party.identifier}}},', file=f)
            print('    },', file=f)
            if count != len(trainers):
                print(file=f)
        print('};', file=f)

def write_parties_header(parties):
    with open('src/data/trainer_parties.h', 'w') as f:
        for count, party in enumerate(parties.values(), start=1):
            print(f'static const struct TrainerMon{party.party_type} {party.identifier}[] = {{', file=f)
            for mon_count, mon in enumerate(party.get_mons_compact(), start=1):
                print('    {', file=f)
                print(f'    .iv = {mon.iv},', file=f)
                print(f'    .lvl = {mon.lvl},', file=f)
                print(f'    .species = {mon.species},', file=f)
                if mon.has_item():
                    print(f'    .heldItem = {mon.heldItem}{"," if mon.has_moves() else ""}', file=f)
                if mon.has_moves():
                    print(f'    .moves = {array_text_generator(mon.moves)}', file=f)
                if mon_count == len(party.get_mons_compact()):
                    print('    }', file=f)
                else:
                    print('    },', file=f)
            if count == len(parties):
                print('};', file=f)
            else:
                print('};\n', file=f)

@Gtk.Template.from_file('searchable_list.ui')
class SearchableList(Gtk.Grid):
    __gtype_name__ = 'SearchableList'
    search_entry = Gtk.Template.Child()
    list_box = Gtk.Template.Child()
    create_new_button = Gtk.Template.Child()
    search_string = ""

    def __init__(self, width = 200, height = 400):
        super().__init__()
        self.set_size_request(width, height)
        self.list_box.set_filter_func(self.filter_labels)

    def add_label(self, text):
        label = Gtk.Label.new(text)
        self.list_box.insert(label, -1)
        label.show()

    def add_sprites(self, sprites):
        self.sprites = sprites
        self.list_box.set_filter_func(self.filter_images)
        for sprite in self.sprites:
            image = Gtk.Image.new_from_pixbuf(self.sprites[sprite])
            image.sprite_label = sprite
            self.list_box.insert(image, -1)
            image.show()

    def show_button(self):
        self.create_new_button.show()

    @Gtk.Template.Callback('on_search')
    def on_search(self, entry):
        self.search_string = entry.get_text()
        self.list_box.invalidate_filter()

    def filter_images(self, row):
        return self.search_string.upper() in row.get_children()[0].sprite_label

    def filter_labels(self, row):
        return self.search_string.upper() in row.get_children()[0].get_text()

@Gtk.Template.from_file('pokemon_panel.ui')
class PokemonPanel(Gtk.Popover):
    __gtype_name__ = 'PokemonPanel'
    pokemon_grid = Gtk.Template.Child()
    species_button = Gtk.Template.Child()
    level_spin_box = Gtk.Template.Child()
    iv_spin_box = Gtk.Template.Child()
    held_item_button = Gtk.Template.Child()
    move_button1 = Gtk.Template.Child()
    move_button2 = Gtk.Template.Child()
    move_button3 = Gtk.Template.Child()
    move_button4 = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self.active_button = None
        self.mon = None
        self.move_buttons = [getattr(self, f'move_button{i}') for i in range(1,5)]
        self.iv_spin_box.set_range(0, 255)
        self.level_spin_box.set_range(1,100)

        self.pokemon_searchable = SearchableList()
        with open('include/constants/species.h') as f:
            for line in f:
                if '#define SPECIES' in line:
                    tokens = line.split()
                    self.pokemon_searchable.add_label(tokens[1])
        self.pokemon_searchable.list_box.connect('row-activated', self.on_mon_selected)

        self.held_item_searchable = SearchableList()
        with open('include/constants/items.h') as f:
            for line in f:
                if '#define ITEM' in line:
                    tokens = line.split()
                    self.held_item_searchable.add_label(tokens[1])
        self.held_item_searchable.list_box.connect('row-activated', self.on_item_selected)

        self.move_searchable = SearchableList()
        with open('include/constants/moves.h') as f:
            for line in f:
                if '#define MOVE' in line:
                    tokens = line.split()
                    self.move_searchable.add_label(tokens[1])
        self.move_searchable.list_box.connect('row-activated', self.on_move_selected)

    @Gtk.Template.Callback('on_move_clicked')
    def on_move_clicked(self, button):
        self.active_button = button
        self.remove(self.pokemon_grid)
        self.add(self.move_searchable)

    @Gtk.Template.Callback('on_species_clicked')
    def on_species_clicked(self, button):
        self.remove(self.pokemon_grid)
        self.add(self.pokemon_searchable)

    @Gtk.Template.Callback('on_held_item_clicked')
    def on_held_item_clicked(self, button):
        self.remove(self.pokemon_grid)
        self.add(self.held_item_searchable)

    @Gtk.Template.Callback('on_level_set')
    def on_level_set(self, button):
        if self.mon is not None:
            self.mon.lvl = int(button.get_value())

    @Gtk.Template.Callback('on_iv_set')
    def on_held_iv_set(self, button):
        if self.mon is not None:
            self.mon.iv = int(button.get_value())

    @Gtk.Template.Callback('on_hide')
    def on_hide(self, popover):
        if self.get_child() is not self.pokemon_grid:
            self.remove(self.get_child())
            self.add(self.pokemon_grid)

    def on_move_selected(self, box, row):
        for i in range(0,4):
            if self.active_button is self.move_buttons[i]:
                move = row.get_children()[0].get_text()
                self.active_button.set_label(move)
                self.active_button = None
                self.mon.set_move(move, i)
        self.remove(self.move_searchable)
        self.add(self.pokemon_grid)

    def on_mon_selected(self, box, row):
        species = row.get_children()[0].get_text()
        if species == 'SPECIES_NONE':
            self.set_mon(None)
        else:
            if self.mon is None:
                self.set_mon(Mon(species))
            else:
                self.mon.species = species
                self.species_button.set_label(species)
        self.remove(self.pokemon_searchable)
        self.add(self.pokemon_grid)

    def on_item_selected(self, box, row):
        item = row.get_children()[0].get_text()
        self.mon.heldItem = item
        self.held_item_button.set_label(item)
        self.remove(self.held_item_searchable)
        self.add(self.pokemon_grid)

    def set_widgets_sensitivity(self, sensitivity):
            self.iv_spin_box.set_sensitive(sensitivity)
            self.level_spin_box.set_sensitive(sensitivity)
            self.held_item_button.set_sensitive(sensitivity)
            for i in range(0, 4):
                self.move_buttons[i].set_sensitive(sensitivity)

    def set_mon(self, mon = None):
        self.mon = mon
        if mon is None:
            self.species_button.set_label('Select Species')
            self.iv_spin_box.set_value(0)
            self.level_spin_box.set_value(1)
            self.held_item_button.set_label('Select Item')
            for i in range(0, 4):
                self.move_buttons[i].set_label('Select Move')
            self.set_widgets_sensitivity(False)
        else:
            self.set_widgets_sensitivity(True)
            self.iv_spin_box.set_value(int(mon.iv))
            self.level_spin_box.set_value(int(mon.lvl))
            self.species_button.set_label(mon.species)
            if mon.has_item() and mon.heldItem is not 'ITEM_NONE':
                self.held_item_button.set_label(mon.heldItem)
            else:
                self.held_item_button.set_label('Select Item')
            for i in range(0, 4):
                button = self.move_buttons[i]
                if not mon.has_moves():
                    button.set_label('Select Move')
                else:
                    if mon.moves[i] == 'MOVE_NONE':
                        button.set_label('Select Move')
                    else:
                        button.set_label(mon.moves[i])

@Gtk.Template.from_file('new_trainer_dialog.ui')
class NewTrainerDialog(Gtk.Dialog):
    __gtype_name__ = 'NewTrainerDialog'
    create_button = Gtk.Template.Child()
    def __init__(self):
        super().__init__()
        self.reset()

    def set_create_button_state(self):
        self.create_button.set_sensitive(self.name and self.trainer_identifier and self.party_identifier)

    @Gtk.Template.Callback('on_name_changed')
    def on_name_changed(self, entry):
        self.name = entry.get_text()
        self.set_create_button_state()

    @Gtk.Template.Callback('on_trainer_identifier_changed')
    def on_trainer_identifier_changed(self, entry):
        self.trainer_identifier = entry.get_text()
        self.set_create_button_state()

    @Gtk.Template.Callback('on_party_identifier_changed')
    def on_party_identifier_changed(self, entry):
        self.party_identifier = entry.get_text()
        self.set_create_button_state()

    @Gtk.Template.Callback('on_close')
    def on_close(self, button):
        self.response(Gtk.ResponseType.CANCEL)

    @Gtk.Template.Callback('on_delete')
    def on_delete(self, event, data):
        self.hide()
        return True

    def reset(self):
        self.name = ''
        self.trainer_identifier = ''
        self.party_identifier = ''
        self.create_button.set_sensitive(False)

class Editor:
    items = {
        'None': 'ITEM_NONE',
        'Potion': 'ITEM_POTION',
        'Super Potion': 'ITEM_SUPER_POTION',
        'Hyper Potion': 'ITEM_HYPER_POTION',
        'Full Restore': 'ITEM_FULL_RESTORE'
    }
    def __init__(self):
        self.parties = get_parties()
        self.trainers = get_trainers(self.parties)
        self.load_sprite_list()

        builder = Gtk.Builder()
        builder.add_from_file('editor.ui')
        for widget in ['window', 'save_button', 'choose_trainer_button',
                       'choose_trainer_label', 'identifier_entry', 'trainer_class_button',
                       'trainer_class_label', 'music_button', 'music_label',
                       'sprite_button', 'sprite_image', 'double_battle_switch',
                       'check_bad_move_switch', 'check_viability_switch', 'setup_first_turn_switch',
                       'item_button1', 'item_label1', 'item_button2',
                       'item_label2', 'item_button3', 'item_label3',
                       'item_label4', 'item_button4', 'mon_button1',
                       'mon_label1', 'mon_button2', 'mon_label2',
                       'mon_button3', 'mon_label3', 'mon_button4',
                       'mon_label4', 'mon_button5', 'mon_label5',
                       'mon_button6', 'mon_label6', 'trainer_list_box',
                       'try_to_faint_switch', 'trainer_name_entry',
                       'risky_switch', 'item_popover', 'item_list_box',
                       'male_radio_button', 'female_radio_button', 'prefer_strongest_move_switch',
                       'prefer_baton_pass_switch', 'hp_aware_switch']:
            setattr(self, widget, builder.get_object(widget))

        self.trainer_popover = Gtk.Popover()
        self.trainer_searchable = SearchableList(300, 450)
        self.trainer_searchable.list_box.connect('row-activated', self.on_trainer_row_activated)
        self.trainer_searchable.create_new_button.connect('clicked', self.on_create_new_button_clicked)
        self.trainer_searchable.show_button()
        self.trainer_popover.add(self.trainer_searchable)
        self.choose_trainer_button.set_popover(self.trainer_popover)
        self.trainer_popover.set_relative_to(self.choose_trainer_button)
        for trainer in self.trainers:
            if trainer == 'TRAINER_NONE':
                continue
            self.trainer_searchable.add_label(trainer)

        self.sprite_popover = Gtk.Popover()
        self.sprite_searchable = SearchableList(200, 450)
        self.sprite_searchable.add_sprites(self.sprites)
        self.sprite_searchable.list_box.connect('row-activated', self.on_sprite_row_activated)
        self.sprite_popover.add(self.sprite_searchable)
        self.sprite_button.set_popover(self.sprite_popover)
        self.sprite_popover.set_relative_to(self.sprite_button)

        self.music_popover = Gtk.Popover()
        self.music_searchable = SearchableList(300,400)
        self.trainer_class_popover = Gtk.Popover()
        self.trainer_class_searchable = SearchableList(300, 450)
        with open('include/constants/trainers.h') as f:
            for line in f:
                if '#define TRAINER_ENCOUNTER_MUSIC' in line:
                    self.music_searchable.add_label(line.split()[1]
                                                    .replace('TRAINER_ENCOUNTER_MUSIC_', '')
                                                    .replace("_", ' ')
                                                    .title())
                elif '#define TRAINER_CLASS' in line:
                    self.trainer_class_searchable.add_label(line.split()[1]
                                                            .replace('TRAINER_CLASS_', '')
                                                            .replace("_", ' ')
                                                            .title())
        self.music_searchable.list_box.connect('row-activated', self.on_music_row_activated)
        self.music_popover.add(self.music_searchable)
        self.music_button.set_popover(self.music_popover)
        self.music_popover.set_relative_to(self.music_button)
        self.trainer_class_searchable.list_box.connect('row-activated', self.on_trainer_class_row_activated)
        self.trainer_class_popover.add(self.trainer_class_searchable)
        self.trainer_class_button.set_popover(self.trainer_class_popover)
        self.trainer_class_popover.set_relative_to(self.trainer_class_button)

        self.new_trainer_dialog = NewTrainerDialog()
        self.new_trainer_dialog.set_transient_for(self.window)

        for item in self.items.keys():
            label = Gtk.Label.new(item)
            self.item_list_box.insert(label, -1)
            label.show()

        self.pokemon_panel = PokemonPanel()

        self.mon_buttons = []
        for i in range(1,7):
            button = getattr(self, f'mon_button{i}')
            button.set_popover(self.pokemon_panel)
            self.mon_buttons.append(button)
        self.item_buttons = [getattr(self, f'item_button{i}') for i in range(1,5)]

        builder.connect_signals(self)
        key = list(self.trainers.keys())[1]
        self.set_current_trainer(self.trainers[key])
        self.update_sprite()

    def update_sprite(self):
        original_pixbuf = self.sprites[self.current_trainer.trainer_pic]
        pixbuf = original_pixbuf.scale_simple(160, 160, GdkPixbuf.InterpType.NEAREST)
        self.sprite_image.set_from_pixbuf(pixbuf)

    def on_quit(self, data):
        Gtk.main_quit()

    def on_save(self, data):
        write_parties_header(self.parties)
        write_opponents_header(self.trainers)
        write_trainers_header(self.trainers)

    def on_sprite_row_activated(self, box, row):
        sprite = row.get_children()[0].sprite_label
        self.current_trainer.trainer_pic = row.get_children()[0].sprite_label
        self.update_sprite()

    def on_music_row_activated(self, box, row):
        label = row.get_children()[0].get_text()
        music = f'TRAINER_ENCOUNTER_MUSIC_{label.replace(" ", "_").upper()}'
        self.current_trainer.music = music
        self.music_label.set_text(label)
        self.music_popover.popdown()

    def on_trainer_class_row_activated(self, box, row):
        label = row.get_children()[0].get_text()
        trainer_class = f'TRAINER_CLASS_{label.replace(" ", "_").upper()}'
        self.current_trainer.trainer_class = trainer_class
        self.trainer_class_label.set_text(label)

    def on_mon_button_toggled(self, button):
        if button.get_active():
            for i, b in enumerate(self.mon_buttons):
                if b is button:
                    self.pokemon_panel.set_relative_to(b)
                    self.pokemon_panel.set_mon(self.current_trainer.party.mons[i])
        else:
            for i, b in enumerate(self.mon_buttons):
                if b is button:
                    self.current_trainer.party.mons[i] = self.pokemon_panel.mon
                    if self.pokemon_panel.mon is not None:
                        button.get_child().set_text(self.pokemon_panel.mon.species)
                    else:
                        button.get_child().set_text('Select Pokemon')
                    self.current_trainer.party.revalidate_party()

    def on_item_button_toggled(self, button):
        if button.get_active():
            self.item_popover.set_relative_to(button)

    def on_gender_toggled(self, button):
        self.current_trainer.is_female = self.female_radio_button.get_active()

    def on_double_battle_switch_activate(self, switch, data):
        self.current_trainer.double_battle = switch.get_active()
    def on_check_bad_move_switch_activate(self, switch, data):
        self.current_trainer.check_bad_move = switch.get_active()
    def on_try_to_faint_switch_activate(self, switch, data):
        self.current_trainer.try_to_faint = switch.get_active()
    def on_check_viability_switch_activate(self, switch, data):
        self.current_trainer.check_viability = switch.get_active()
    def on_setup_first_turn_switch_activate(self, switch, data):
        self.current_trainer.setup_first_turn = switch.get_active()
    def on_risky_switch_activate(self, switch, data):
        self.current_trainer.risky = switch.get_active()
    def on_prefer_strongest_move_switch_activate(self, switch, data):
        self.current_trainer.prefer_strongest_move = switch.get_active()
    def on_prefer_baton_pass_switch_activate(self, switch, data):
        self.current_trainer.prefer_baton_pass = switch.get_active()
    def on_hp_aware_switch_activate(self, switch, data):
        self.current_trainer.hp_aware = switch.get_active()

    def set_trainer_class_label(self, text):
        self.trainer_class_label.set_text(text.replace('TRAINER_CLASS_', '').replace('_', ' ').title())

    def set_current_trainer(self, trainer):
        self.current_trainer = trainer
        party = self.current_trainer.party
        self.update_sprite()
        self.trainer_name_entry.set_text(self.current_trainer.name)
        self.identifier_entry.set_text(self.current_trainer.identifier)
        self.set_trainer_class_label(self.current_trainer.trainer_class)
        self.music_label.set_text(trainer.music.replace('TRAINER_ENCOUNTER_MUSIC_', '').title())
        if self.current_trainer.is_female:
            self.female_radio_button.set_active(True)
        else:
            self.male_radio_button.set_active(True)
        self.double_battle_switch.set_active(self.current_trainer.double_battle)

        self.check_bad_move_switch.set_active(self.current_trainer.check_bad_move)
        self.try_to_faint_switch.set_active(self.current_trainer.try_to_faint)
        self.check_viability_switch.set_active(self.current_trainer.check_viability)
        self.setup_first_turn_switch.set_active(self.current_trainer.setup_first_turn)
        self.risky_switch.set_active(self.current_trainer.risky)
        self.prefer_strongest_move_switch.set_active(self.current_trainer.prefer_strongest_move)
        self.prefer_baton_pass_switch.set_active(self.current_trainer.prefer_baton_pass)
        self.hp_aware_switch.set_active(self.current_trainer.hp_aware)

        items = self.current_trainer.get_items_compact()
        if len(items) > 0:
            for count, item in enumerate(items, start=1):
                getattr(self, f'item_label{count}').set_text('Select Item' if item == "ITEM_NONE" else item)
        else:
            for i in range(1,5):
                getattr(self, f'item_label{i}').set_text('Select Item')

        for count, mon in enumerate(party.mons, start=1):
            if mon is None:
                getattr(self, f'mon_label{count}').set_text('Select Pokemon')
            else:
                getattr(self, f'mon_label{count}').set_text(party.mons[count-1].species)

    def load_sprite_list(self):
        self.sprites = {}
        image_files = glob.glob('graphics/trainers/front_pics/*.png')
        for entry in image_files:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(entry)
            self.sprites[f'TRAINER_PIC_{os.path.basename(entry)}'
                         .replace('cool_trainer', 'COOLTRAINER')
                         .replace('_front_pic.png', '')
                         .upper()] = pixbuf

    def on_trainer_row_activated(self, box, row):
        self.set_current_trainer(self.trainers[row.get_children()[0].get_text()])
        self.trainer_popover.popdown()

    def on_trainer_name_entry_changed(self, entry):
        self.current_trainer.name = entry.get_text()

    def on_identifier_entry_changed(self, entry):
        self.current_trainer.identifier = entry.get_text()

    def on_item_list_box_row_activated(self, box, row):
        item_text = row.get_children()[0].get_text()
        for count, button in enumerate(self.item_buttons, start=1):
            if button.get_active():
                label = getattr(self, f'item_label{count}')
                if item_text == 'None':
                    label.set_text('Select Item')
                else:
                    label.set_text(item_text)
                self.current_trainer.items[count-1] = self.items[item_text]
        self.item_popover.popdown()

    def on_create_new_button_clicked(self, button):
        self.trainer_popover.popdown()
        response = self.new_trainer_dialog.run()
        self.new_trainer_dialog.hide()
        if response == Gtk.ResponseType.APPLY:
            trainer = Trainer()
            trainer.identifier = self.new_trainer_dialog.trainer_identifier
            trainer.name = self.new_trainer_dialog.name
            trainer.party = Party()
            trainer.party.identifier = self.new_trainer_dialog.party_identifier
            self.parties[trainer.party.identifier] = trainer.party
            self.trainers[trainer.identifier] = trainer
            self.set_current_trainer(trainer)
        else:
            self.new_trainer_dialog.reset()
            self.new_trainer_dialog.hide()

def main():
    editor = Editor()
    Gtk.main()

if __name__ == "__main__":
    main()

