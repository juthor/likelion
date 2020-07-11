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





# 1 . 동요 음악 test.
song = [['c4', 4], ['c4', 4], ['c4', 4], ['d4', 8], ['e4', 4], ['e4', 4], ['d4', 8], ['e4', 4], ['f4', 8], ['g4', 2], ['c4', 8], ['c4', 8], ['c4', 8], ['g4', 8], ['g4', 8], ['g4', 8], ['e4', 8], ['e4', 8], ['e4', 8], ['c4', 8], ['c4', 8], ['c4', 8], ['g4', 4], ['f4', 8], ['e4', 4], ['d4', 8], ['c4', 2]]

    # pysynth패키지를 활용해서 음표 리스트를, wav파일로 바탕화면에 저장.
#ps.make_wav(song, fn='C:/Users/hyunju/Desktop/temp/first.wav')

# # 마르코프 체인 모델로 음악 학습하기. matrix변수에 마르코프 체인으로 학습한 확률표가 저장되게 된다. 
matrix = MusicMatrix(song)

# # 새로운 데이터 입력, 처음 시작하는 음표 제시.
start_note = ['c4', 4]

# # 학습한 음악을 바탕으로 random_song을 작곡.
random_song = []
# # 학습한 마르코프체인 인접행렬표를 따라서 100개의 음표를 만들겠다!
for i in range(0, 100):
    start_note = matrix.next_note(start_note)
    random_song.append(start_note)

#ps.make_wav(random_song, fn='C:/Users/hyunju/Desktop/temp/seccond.wav')
make_midi(midi_path='C:/Users/hyunju/Desktop/temp/second.mid', notes=random_song)


