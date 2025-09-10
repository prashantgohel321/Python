# First, ensure you have the midiutil library installed:
# pip install MIDIUtil

from midiutil import MIDIFile

# --- 1. Setup and Constants ---

SONG_TITLE = "pirate_violin_solo.mid"
TEMPO = 145  # A brisk, adventurous tempo
DURATION_MINUTES = 2.5
INSTRUMENT = 40  # General MIDI program number for Violin

# The "He's a Pirate" theme is in a 6/8 time signature.
# This means 6 eighth notes per bar. In MIDIUtil, 1 beat = 1 quarter note.
# So, a 6/8 bar has a duration of 3 beats (6 * 0.5 = 3).
BEATS_PER_BAR = 3
BARS_TO_GENERATE = int((TEMPO / BEATS_PER_BAR) * DURATION_MINUTES)

# Key of D Minor. Notes are defined by their MIDI number.
D4, E4, F4, G4, A4, Bb4 = 62, 64, 65, 67, 69, 70
C5, D5, E5, F5, G5, A5 = 72, 74, 76, 77, 79, 81

# --- 2. Musical Phrases (Violin Techniques) ---

def add_main_theme(midi, start_beat, velocity=110):
    """Adds the iconic, rhythmic main theme."""
    # This pattern is based on the recognizable melody, using short, sharp notes.
    # Each tuple is (MIDI_note, duration_in_beats)
    melody = [
        (A4, 0.5), (D5, 0.5), (D5, 0.5), (D5, 0.5), (E5, 0.5), (F5, 0.5),
        (F5, 0.5), (G5, 0.5), (E5, 0.5), (E5, 0.5), (F5, 0.5), (D5, 0.5),
        (A4, 0.5), (D5, 0.5), (D5, 0.5), (D5, 0.5), (E5, 0.5), (F5, 0.5),
        (F5, 0.5), (G5, 0.5), (E5, 0.5), (E5, 0.5), (F5, 0.5), (D5, 0.5),
    ]
    time = start_beat
    for note, duration in melody:
        midi.addNote(0, 0, note, time, duration, velocity)
        time += duration
    return time # Return the new current time

def add_driving_arpeggios(midi, start_beat, num_bars, chord, velocity=100):
    """Simulates a rhythmic backing by playing fast chord arpeggios."""
    # This creates the driving energy of the full orchestra's string section.
    time = start_beat
    # 16th notes (duration 0.25) fit perfectly into 6/8 time.
    for _ in range(num_bars * 2): # 2 arpeggio patterns per bar
        for note in chord:
            midi.addNote(0, 0, note, time, 0.25, velocity)
            time += 0.25
        for note in reversed(chord[1:]): # Go back down
             midi.addNote(0, 0, note, time, 0.25, velocity)
             time += 0.25
    return time

def add_virtuosic_run(midi, start_beat, velocity=120):
    """Adds a fast, impressive scale run to build excitement."""
    # A fast run up and down the D minor scale
    d_minor_scale_up = [D4, E4, F4, G4, A4, Bb4, C5, D5, E5, F5, G5, A5]
    time = start_beat
    # Play up the scale as 16th notes
    for note in d_minor_scale_up:
        midi.addNote(0, 0, note, time, 0.25, velocity)
        time += 0.25
    # Play back down
    for note in reversed(d_minor_scale_up):
        midi.addNote(0, 0, note, time, 0.25, velocity)
        time += 0.25
    return time

# --- 3. Main Song Assembly ---

# Create a MIDIFile object with 1 track
my_midi = MIDIFile(1)

# Add track name, tempo, and instrument
my_midi.addTrackName(0, 0, "Pirate Violin Solo")
my_midi.addTempo(0, 0, TEMPO)
my_midi.addProgramChange(0, 0, 0, INSTRUMENT)

# Define the chord progression for the piece
d_minor_arp = [D4, F4, A4]
g_minor_arp = [G4, Bb4, D5]
c_major_arp = [C5, E5, G5]

# Build the song section by section
current_beat = 0
print("🏴‍☠️ Hoisting the sails... Generating pirate violin solo...")

# Section 1: Tense Intro (16 bars)
print("- Section 1: Tense intro with driving rhythm...")
current_beat = add_driving_arpeggios(my_midi, current_beat, 16, d_minor_arp, velocity=95)

# Section 2: Main Theme (8 bars)
print("- Section 2: Main theme, full power!")
current_beat = add_main_theme(my_midi, current_beat, velocity=115)

# Section 3: Bridge with new harmony (16 bars)
print("- Section 3: Bridge with changing harmony...")
current_beat = add_driving_arpeggios(my_midi, current_beat, 8, g_minor_arp, velocity=105)
current_beat = add_driving_arpeggios(my_midi, current_beat, 8, c_major_arp, velocity=110)

# Section 4: Main Theme, higher and more intense (8 bars)
print("- Section 4: Main theme returns, higher and more intense!")
# Transpose the theme up by a perfect fifth (7 semitones) for variation
theme_2_vel = 120
time = current_beat
melody_part_2 = [
    (A4+7, 0.5), (D5+7, 0.5), (D5+7, 0.5), (D5+7, 0.5), (E5+7, 0.5), (F5+7, 0.5),
    (F5+7, 0.5), (G5+7, 0.5), (E5+7, 0.5), (E5+7, 0.5), (F5+7, 0.5), (D5+7, 0.5),
] * 2
for note, duration in melody_part_2:
    my_midi.addNote(0, 0, note, time, duration, theme_2_vel)
    time += duration
current_beat = time

# Section 5: The Virtuosic Run (4 bars)
print("- Section 5: The virtuosic climax!")
current_beat = add_virtuosic_run(my_midi, current_beat, velocity=127) # Max velocity

# Section 6: Final statement of the Main Theme (8 bars)
print("- Section 6: Final, powerful theme statement...")
current_beat = add_main_theme(my_midi, current_beat, velocity=120)

# Section 7: Outro
print("- Section 7: Grand finale...")
# End with a fast arpeggio and a long, held note
current_beat = add_driving_arpeggios(my_midi, current_beat, 3, d_minor_arp, velocity=125)
my_midi.addNote(0, 0, D5, current_beat, 4, 127) # Final triumphant note

# --- 4. Save the MIDI File ---
print(f"\n✅ MIDI file '{SONG_TITLE}' has been written to disk.")
with open(SONG_TITLE, "wb") as output_file:
    my_midi.writeFile(output_file)

print("Arr, she's ready to play! 🎻")