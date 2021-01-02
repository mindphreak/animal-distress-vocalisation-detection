import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

CLIP_LEN = 3
SAMPLE_RATE = 44100

def create_mel_spectrogram(args):
    cmap_type, file_path, save_loc = args
    base_name = os.path.basename(file_path)
    img_file_name = base_name.replace(".wav", "")
    img_file_path = os.path.join(save_loc, img_file_name + '.png')
    if os.path.exists(img_file_path):
        return

    signal, sr = librosa.load(file_path, sr=SAMPLE_RATE)
    duration = librosa.get_duration(y=signal, sr=SAMPLE_RATE)
    if duration != CLIP_LEN:
        return
    plt.figure(figsize=(10,3))
    stft = librosa.stft(signal)
    log_spectrogram = librosa.amplitude_to_db(abs(stft))
    librosa.display.specshow(log_spectrogram, sr=SAMPLE_RATE, cmap=cmap_type, x_axis='time', y_axis='hz')
    plt.ylim(0, 10000)
    plt.savefig(img_file_path)
    plt.clf()
    plt.close()