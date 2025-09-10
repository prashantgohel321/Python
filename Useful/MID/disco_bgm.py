# First, ensure you have the midiutil library installed:
# pip install MIDIUtil

from midiutil import MIDIFile

# --- 1. Setup and Constants ---

# Song Parameters
SONG_TITLE = "rasputin_style_bgm.mid"
TEMPO = 128  # BPM, typical for Rasputin
DURATION_MINUTES = 5
BEATS_PER_MINUTE = TEMPO
TOTAL_BEATS = BEATS_PER_MINUTE * DURATION_MINUTES
BEATS_PER_BAR = 4

# MIDI Tracks and Channels
# (Tracks hold the notes, channels control the sound/instrument)
DRUM_TRACK = 0
BASS_TRACK = 1
CHORDS_TRACK = 2
LEAD_TRACK = 3
RIFF_TRACK = 4
# Use channel 9 for percussion, as is standard
DRUM_CHANNEL = 9
BASS_CHANNEL = 1
CHORDS_CHANNEL = 2
LEAD_CHANNEL = 3
RIFF_CHANNEL = 4

# MIDI Instrument Programs (General MIDI)
ELECTRIC_BASS_FINGER = 33
STRING_ENSEMBLE_1 = 48
SITAR = 104  # Used to mimic the balalaika sound in the instrumental hook

# Drum Note Numbers (for Channel 9)
KICK = 36
SNARE = 38
CLOSED_HI_HAT = 42
OPEN_HI_HAT = 46

# --- 2. Note and Chord Definitions (Key of B minor) ---

# Using MIDI note numbers. Middle C (C4) is 60.
# Bass root notes
NOTE_MAP = {
    'B': 47, 'F#': 54, 'G': 43, 'E': 52, 'A': 45, 'D': 50
}

# Chord voicings (root, third, fifth)
CHORD_MAP = {
    'Bm': [59, 62, 66],   # B3, D4, F#4
    'F#': [54, 58, 61],   # F#3, A#3, C#4 (Major for dominant feel)
    'G':  [55, 59, 62],   # G3, B3, D4
    'Em': [52, 55, 59],   # E3, G3, B3
    'A':  [57, 61, 64],   # A3, C#4, E4
    'D':  [50, 54, 57]    # D3, F#3, A3
}

# --- 3. Musical Pattern Functions ---

def add_disco_drums(midi, total_beats):
    """Adds a continuous 4-on-the-floor disco beat for the whole song."""
    for beat in range(0, total_beats):
        # Kick on every beat
        midi.addNote(DRUM_TRACK, DRUM_CHANNEL, KICK, beat, 1, 110)
        # Snare on beats 2 and 4
        if beat % 2 == 1:
            midi.addNote(DRUM_TRACK, DRUM_CHANNEL, SNARE, beat, 1, 90)

    # 16th-note hi-hats for energy
    for i in range(total_beats * 4):
        time = i * 0.25
        # Emphasize the beat with an open hat
        if i % 4 == 0:
            midi.addNote(DRUM_TRACK, DRUM_CHANNEL, OPEN_HI_HAT, time, 0.25, 80)
        else:
            midi.addNote(DRUM_TRACK, DRUM_CHANNEL, CLOSED_HI_HAT, time, 0.25, 60)

def add_octave_bassline(midi, start_beat, num_beats, root_note_name):
    """Adds the iconic octave-jumping bassline for a given chord."""
    root_midi_note = NOTE_MAP[root_note_name]
    octave_note = root_midi_note + 12
    # Add 8th notes
    for i in range(num_beats * 2):
        time = start_beat + i * 0.5
        # Play root for the first half, octave for the second
        note = root_midi_note if i < num_beats else octave_note
        midi.addNote(BASS_TRACK, BASS_CHANNEL, note, time, 0.5, 100)

def add_chords(midi, start_beat, num_beats, chord_name):
    """Adds sustained chords as a background layer."""
    notes = CHORD_MAP[chord_name]
    for note in notes:
        midi.addNote(CHORDS_TRACK, CHORDS_CHANNEL, note, start_beat, num_beats, 70)

def add_intro_riff(midi, start_beat):
    """Adds the famous ascending/descending string riff."""
    # Bm scale run (B, C#, D, E, F#, G, A, B) up and down
    riff_up = [71, 73, 74, 76, 78, 79, 81, 83]
    riff_down = [81, 79, 78, 76, 74, 73, 71]
    
    time = start_beat
    # Add the ascending part twice
    for _ in range(2):
        for note in riff_up:
            midi.addNote(RIFF_TRACK, RIFF_CHANNEL, note, time, 0.25, 95)
            time += 0.25
    
    # Add the descending part twice
    for _ in range(2):
        for note in riff_down:
            midi.addNote(RIFF_TRACK, RIFF_CHANNEL, note, time, 0.25, 95)
            # Add a final note to complete the bar
            if riff_down.index(note) == len(riff_down) -1:
                midi.addNote(RIFF_TRACK, RIFF_CHANNEL, 71, time + 0.25, 0.25, 95)
            time += 0.25

def add_instrumental_hook(midi, start_beat):
    """Adds the balalaika-style lead melody."""
    melody = [
        (71, 0.5), (71, 0.5), (69, 0.5), (69, 0.5), # B, B, A, A
        (67, 0.5), (67, 0.5), (66, 0.5), (66, 0.5), # G, G, F#, F#
        (64, 0.5), (64, 0.5), (62, 0.5), (62, 0.5), # E, E, D, D
        (61, 0.5), (61, 0.5), (59, 1.0)             # C#, C#, B
    ]
    time = start_beat
    for note, duration in melody * 2: # Repeat hook twice for 8 bars
        midi.addNote(LEAD_TRACK, LEAD_CHANNEL, note, time, duration, 105)
        time += duration

# --- 4. Main Song Assembly ---

# Create a MIDIFile object with the specified number of tracks
my_midi = MIDIFile(5)

# Add track names and tempo
my_midi.addTrackName(DRUM_TRACK, 0, "Drums")
my_midi.addTrackName(BASS_TRACK, 0, "Bass")
my_midi.addTrackName(CHORDS_TRACK, 0, "Chords")
my_midi.addTrackName(LEAD_TRACK, 0, "Lead")
my_midi.addTrackName(RIFF_TRACK, 0, "Riff")
my_midi.addTempo(DRUM_TRACK, 0, TEMPO)

# Set instrument for each track
my_midi.addProgramChange(BASS_TRACK, BASS_CHANNEL, 0, ELECTRIC_BASS_FINGER)
my_midi.addProgramChange(CHORDS_TRACK, CHORDS_CHANNEL, 0, STRING_ENSEMBLE_1)
my_midi.addProgramChange(RIFF_TRACK, RIFF_CHANNEL, 0, STRING_ENSEMBLE_1)
my_midi.addProgramChange(LEAD_TRACK, LEAD_CHANNEL, 0, SITAR)

# Add the drum track for the entire duration
print("Adding drums...")
add_disco_drums(my_midi, TOTAL_BEATS)

# Define the chord progressions for different sections (chord, duration in bars)
verse_progression = [('Bm', 2), ('Em', 1), ('A', 1), ('D', 1), ('G', 1), ('Em', 1), ('F#', 1)] # 8 bars
chorus_progression = [('Bm', 2), ('G', 1), ('D', 1), ('A', 2), ('Bm', 1), ('F#', 1)] # 8 bars

# Define the song structure (section_function, progression, duration_in_bars)
song_structure = [
    ('intro', None, 8),
    ('verse', verse_progression, 16),
    ('chorus', chorus_progression, 16),
    ('instrumental', None, 8),
    ('verse', verse_progression, 16),
    ('chorus', chorus_progression, 16),
    ('instrumental', None, 8),
    ('verse', verse_progression, 16),
    ('chorus', chorus_progression, 16),
    ('instrumental', None, 8),
    ('chorus', chorus_progression, 16),
    ('outro', None, 8)
]

# Build the song section by section
current_beat = 0
print("Building song structure...")
for section, progression, num_bars in song_structure:
    print(f"- Adding {section} ({num_bars} bars)")
    section_duration_beats = num_bars * BEATS_PER_BAR
    
    if section == 'intro':
        add_intro_riff(my_midi, current_beat)
        # Add a simple bass note during the intro
        add_octave_bassline(my_midi, current_beat, section_duration_beats, 'B')
    
    elif section == 'instrumental' or section == 'outro':
        add_instrumental_hook(my_midi, current_beat)
        # Follow the verse progression for bass/chords underneath
        beat_in_section = 0
        while beat_in_section < section_duration_beats:
            for chord, bars in verse_progression:
                duration = bars * BEATS_PER_BAR
                if beat_in_section >= section_duration_beats: break
                
                # *** FIX IS HERE ***
                root_note = chord.replace('m', '')
                add_octave_bassline(my_midi, current_beat + beat_in_section, duration, root_note)
                add_chords(my_midi, current_beat + beat_in_section, duration, chord)
                beat_in_section += duration
    
    elif progression:
        # For verse and chorus, loop through their progressions
        beat_in_section = 0
        while beat_in_section < section_duration_beats:
            for chord, bars in progression:
                duration = bars * BEATS_PER_BAR
                if beat_in_section >= section_duration_beats: break
                
                # *** AND FIX IS HERE ***
                root_note = chord.replace('m', '')
                add_octave_bassline(my_midi, current_beat + beat_in_section, duration, root_note)
                add_chords(my_midi, current_beat + beat_in_section, duration, chord)
                beat_in_section += duration
                
    current_beat += section_duration_beats

# --- 5. Save the MIDI File ---
print(f"\nSaving MIDI file: {SONG_TITLE}")
with open(SONG_TITLE, "wb") as output_file:
    my_midi.writeFile(output_file)

print("🎵 MIDI file created successfully!")