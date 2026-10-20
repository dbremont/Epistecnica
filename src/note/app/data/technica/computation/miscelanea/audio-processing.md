# Audio Processing


> 

> Sound:  In a very technical sense, **sound** is a propagating mechanical wave that results from oscillations in a medium (such as air, water, or solid materials). It consists of **pressure variations** that travel through the medium due to the displacement of particles.
> 

QA:

- Why Sine Waves? Sine waves are the "building blocks" of sound because they are the simplest and purest form of vibration.
- Does very wave be represented in terms of sines waves? Any complex sound can be represented as a combination of sine waves, making them fundamental to understanding and creating sound.
- Does every sound can be decomposed into sine waves?
- How to create realistic sound  representation? Yes, every sound can be decomposed into sine waves, thanks to a fundamental principle in mathematics and signal processing called Fourier's Theorem (or Fourier Analysis). . Even **non-periodic** sounds (like noise or transient sounds) can be represented using sine waves, though the process is more complex.
- Are complex sounds composed of many fundamental waves? Yes; See [Sound Anatomy](note.html?n=technica/computation/miscelanea/audio-processing.md).
- How do we hear? How do we perceive waves as sound?
- How is stored sound converted into waves and played?

## Representation

> 

| **Representation Method** | **Description** | **Use Case** |
| --- | --- | --- |
| **Waveform** | Amplitude vs. time graph. | Visualizing raw audio signals, basic editing. |
| **Spectrogram** | Time vs. frequency graph with intensity (amplitude) represented as color. | Analyzing frequency content over time (e.g., music, speech). |
| **Frequency Spectrum** | Amplitude vs. frequency graph at a specific point in time. | Analyzing frequency components of a sound. |
| **Mel Spectrogram** | Spectrogram scaled to the Mel scale, which approximates human hearing. | Speech recognition, music analysis. |
| **MFCC (Mel-Frequency Cepstral Coefficients)** | Compact representation of spectral envelope, derived from Mel spectrogram. | Speech and speaker recognition, music classification. |
| **Chromagram** | Represents pitch classes (e.g., C, D, E) over time, ignoring octave. | Music analysis, chord recognition. |
| **Constant-Q Transform (CQT)** | Time-frequency representation with logarithmic frequency scaling. | Music transcription, harmonic analysis. |
| **Wavelet Transform** | Represents audio in time-frequency domain with variable resolution. | Analyzing transient signals, compression. |
| **STFT (Short-Time Fourier Transform)** | Breaks audio into short frames and computes frequency spectrum for each. | Time-frequency analysis, spectrogram generation. |
| **Raw Audio (Time Domain)** | Direct representation of audio samples in the time domain. | Machine learning models (e.g., raw audio input for neural networks). |

## **Synthesis** Methods

Here’s a table summarizing various **audio synthesis methods**, their characteristics, and common applications:

| **Synthesis Method** | **Description** | **Characteristics** | **Applications** |
| --- | --- | --- | --- |
| **Subtractive Synthesis** | Starts with a rich waveform (e.g., sawtooth, square) and filters out frequencies. | Warm, analog-like sounds; intuitive for shaping tones. | Basslines, leads, pads, classic synth sounds. |
| **Additive Synthesis** | Builds sounds by adding multiple sine waves at different frequencies. | Highly customizable; can create complex timbres. | Bell-like tones, harmonic-rich sounds, sound design. |
| **FM Synthesis** | Modulates the frequency of one waveform with another to create complex harmonics. | Bright, metallic, or gritty sounds; capable of dynamic timbral changes. | Electric pianos, bells, percussion, futuristic sounds. |
| **Wavetable Synthesis** | Uses pre-recorded waveforms (wavetables) that can be morphed or scanned. | Smooth transitions between tones; versatile for evolving sounds. | Evolving pads, modern basslines, cinematic textures. |
| **Granular Synthesis** | Splits audio into tiny grains and rearranges or processes them. | Textural, atmospheric, or glitchy sounds; highly experimental. | Ambient music, soundscapes, experimental sound design. |
| **Physical Modeling** | Simulates the physical properties of real-world instruments or objects. | Realistic acoustic instrument sounds; computationally intensive. | Virtual acoustic instruments (e.g., guitars, drums, wind instruments). |
| **Sample-Based Synthesis** | Uses recorded samples of real instruments or sounds as the basis for synthesis. | Highly realistic or hybrid sounds; relies on sample libraries. | Orchestral music, drum kits, realistic instrument emulation. |
| **Phase Distortion** | Modifies the phase of a waveform to alter its harmonic content. | Unique, aggressive tones; similar to FM but with a different approach. | Harsh leads, metallic textures, experimental sounds. |
| **Karplus-Strong** | Simulates string or drum vibrations using delay lines and feedback. | Realistic plucked string or drum sounds; simple and efficient. | Virtual strings, percussion, and resonant sounds. |
| **Spectral Synthesis** | Manipulates the frequency spectrum of a sound directly. | Highly detailed control over harmonics; complex and resource-intensive. | Sound design, experimental music, and acoustic analysis. |
| **Vector Synthesis** | Morphs between multiple sound sources using a joystick or automation. | Dynamic, evolving sounds; often used in hybrid synthesizers. | Pads, evolving textures, and layered sounds. |
| **Formant Synthesis** | Emulates the resonant frequencies of the human voice or other acoustic systems. | Vocal-like or speech-like sounds; used in voice synthesis. | Vocal synthesis, speech synthesis, and vocal effects. |
| **Wave Shaping** | Distorts a waveform using mathematical functions to create new harmonics. | Aggressive or harmonically rich tones; often used for distortion effects. | Distorted leads, basses, and experimental sounds. |
| **Linear Arithmetic (LA)** | Combines short attack samples with subtractive synthesis for the sustain portion. | Realistic attack transients with synthetic sustain; used in Roland D-50 synths. | Hybrid acoustic/electronic sounds, pads, and realistic instrument emulation. |
| **Resynthesis** | Analyzes and reconstructs sounds using spectral data. | Can recreate or transform existing sounds with high accuracy. | Sound design, remixing, and experimental music. |

## Sound Anatomy

> **Complex sounds** are often composed of many **fundamental waves**, particularly **sine waves**, which are the simplest and purest form of sound. This concept is rooted in **Fourier's  Theorem**,  which states that any complex periodic sound can be broken down into a  series of sine waves with different frequencies, amplitudes, and phases.  These sine waves are called **harmonics** or **partials**.
> 

> 

## References

- [Wave](https://app.notion.com/p/Wave-abe8be3df7354f11a8e84fa436de2e0b?pvs=21)
- [Wavelet](https://app.notion.com/p/Wavelet-7b19eaee77db4a42bf9c1c9027f158c2?pvs=21)
- [Harmonic Analysis](https://app.notion.com/p/Harmonic-Analysis-1bbc0f5171ec8015a56bc2d92c1438a9?pvs=21)
https://en.wikipedia.org/wiki/Harmonic_analysis
- [**Acoustics P**henomena](https://app.notion.com/p/Acoustics-Phenomena-1aec0f5171ec806fb1f2e35f9adfd2fb?pvs=21)
- https://www.youtube.com/watch?v=wGkdb6YlLgg
- https://www.reddit.com/r/musictheory/comments/126bcrb/creating_real_sounds_with_sine_waves/
- https://en.wikipedia.org/wiki/Linear_prediction
- https://en.wikipedia.org/wiki/Audio_signal_processing
- https://en.wikipedia.org/wiki/Karplus%E2%80%93Strong_string_synthesis
- https://www.youtube.com/watch?v=LkGOGzpbrCk
- https://arxiv.org/abs/2009.09761
- https://www.youtube.com/watch?v=vc-MrwZBxtg