import numpy as np
import librosa as libro
import soundfile as sf


class AudioFilterer:
    def __init__(self, audio_file_name):
        self.f_name = audio_file_name
        self.low_freq_cutoff_= 80
        self.high_freq_cutoff_ = 3500

    def filter_audio(self):
        # load the audio from the supplied file
        sound_samples_, sampling_rate_ = libro.load(self.f_name, sr=None, mono=True)
        print(f"Loaded '{self.f_name}' at {sampling_rate_} Hz, {len(sound_samples_)} samples")

        # do a FFT to decompose the sound file
        fft_result_ = np.fft.fft(sound_samples_)
        present_frequencies_ = np.fft.fftfreq(len(sound_samples_), d=1/sampling_rate_)

        # do the filtering (by iterating through the fft'd frequencies and eliminating anything that's out of our threshold)
        filtered_results_ = fft_result_.copy()

        for i in range (len(present_frequencies_)):
            freq = np.abs(present_frequencies_[i])
            if freq < self.low_freq_cutoff_ or freq > self.high_freq_cutoff_:
                filtered_results_[i] = 0
        
        print(f"Original non-zero bins: {np.count_nonzero(fft_result_)}")
        print(f"Filtered non-zero bins: {np.count_nonzero(filtered_results_)}")

        # inverse fft to construct the filtered signal
        filtered_audio_samples_ = np.real(np.fft.ifft(filtered_results_)) # get rid of imaginary noise (introduced as a result of floating point precision rounding)

        # normalize the results to make sure there isn't distortion or clipping (or stuff that messes up the audio because of new amplitudes)
        max_val_ = np.max(np.abs(filtered_audio_samples_))
        if max_val_ != 0:
            filtered_audio_samples_ /= max_val_

        # convert filtered data into an audio file
        int16_conversion_data = (filtered_audio_samples_ * 32767).astype(np.int16)
        sf.write((self.f_name+"_filtered.wav"), int16_conversion_data, sampling_rate_)
        print(f"Filtered audio has been saved as '{self.f_name}_filtered'")