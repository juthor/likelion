import pysynth as ps
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest
from pprint import pprint
from MarkovMusic import MusicMatrix

# pyknon패키지를 사용해, 음계리스트를 midi파일로 만들어주는 함수.
def make_midi(midi_path, notes, bpm=120):
    note_names = 'c c# d d# e f f# g g# a a# b'.split()

    result = NoteSeq()
    for n in notes:
        duration = 1. / n[1]

        if n[0].lower() == 'r':
            result.append(Rest(dur=duration))
        else:
            pitch = n[0][:-1]
            octave = int(n[0][-1]) + 1
            pitch_number = note_names.index(pitch.lower())

            result.append(Note(pitch_number, octave=octave, dur=duration))

    midi = Midi(1, tempo=bpm)
    midi.seq_notes(result, track=0)
    midi.write(midi_path)


# 두가지 음악 합쳐보기

# 동요
song1 = [['c4', 4], ['c4', 4], ['c4', 4], ['d4', 8], ['e4', 4], ['e4', 4], ['d4', 8], ['e4', 4], ['f4', 8], ['g4', 2], ['c4', 8], ['c4', 8], ['c4', 8], ['g4', 8], ['g4', 8], ['g4', 8], ['e4', 8], ['e4', 8], ['e4', 8], ['c4', 8], ['c4', 8], ['c4', 8], ['g4', 4], ['f4', 8], ['e4', 4], ['d4', 8], ['c4', 2]]
# undertail
song2 = [('g#3', 16.0), ('e4', 16.0), ('d#4', 16.0), ('d4', 16.0), ('d#4', 16.0), ('r', 16.0), ('c#4', 16.0), ('b3', 16.0), ('a#3', 16.0), ('r', 16.0), ('g#3', 16.0), ('g3', 16.0), ('g#3', 16.0), ('r', 16.0), ('d#3', 16.0), ('e3', 16.0), ('d#3', 16.0), ('e3', 16.0), ('d#3', 16.0), ('d3', 16.0), ('d#3', 16.0), ('g3', 16.0), ('b3', 16.0), ('a#3', 16.0), ('g#3', 16.0), ('r', 16.0), ('g#3', 16.0), ('a#3', 16.0), ('b3', 16.0), ('r', 16.0), ('a#3', 16.0), ('b3', 16.0), ('c#4', 16.0), ('r', 16.0), ('b3', 16.0), ('a#3', 16.0), ('g3', 16.0), ('r', 16.0), ('g3', 16.0), ('a#3', 16.0), ('b3', 16.0), ('r', 16.0), ('a#3', 16.0), ('g#3', 16.0), ('d#3', 16.0), ('r', 16.0), ('d#3', 16.0), ('e3', 16.0), ('d#3', 16.0), ('e3', 16.0), ('d#3', 16.0), ('d3', 16.0), ('d#3', 16.0), ('g3', 16.0), ('b3', 16.0), ('a#3', 16.0), ('g#3', 16.0), ('r', 16.0), ('g#3', 16.0), ('g3', 16.0), ('g#3', 16.0), ('r', 16.0), ('g#4', 16.0)]

song = list(song1 * 2) + list(song2)

matrix = MusicMatrix(song)

pprint(matrix._markov._matrix)
pprint(matrix._timings._matrix)

start_note = ['e3', 8]

random_song = []
for i in range(0, 500):
    start_note = matrix.next_note(start_note)
    random_song.append(start_note)

ps.make_wav(random_song, fn='C:/Users/main5music.wav')
#make_midi(midi_path='C:/Users/seung/Desktop/ai_session_midi//random_mix.mid', notes=random_song)