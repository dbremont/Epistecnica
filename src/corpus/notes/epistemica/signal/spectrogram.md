---
tags: [note, signal, spectrogram]
---

# Spectrogram

> A **spectrogram** is a signal's spectrum read as a function of time: frequency on one axis, time on the other, and the amplitude of each frequency at each moment carried by the intensity of the mark.

> It is the squared magnitude of the [short-time Fourier transform](/view.html?p=notes/epistemica/signal/fourier-decomposition-toolkit.md) — a spectrum computed for each of many short frames and stacked side by side. That is the whole idea, and the whole difficulty: a single [Fourier transform](/view.html?p=notes/epistemica/signal/fourier-transform.md) tells you which frequencies are present in a signal but not when they occur; a spectrogram trades some of the precision of each for the ability to say when.

## Construction

1. **Frame** the signal into short segments of $N$ samples, advancing by a hop of $H$ samples. Overlap is usual, because a frame boundary is an artificial discontinuity.
2. **Window** each frame — Hann, Hamming, Blackman — to taper its ends, so the frame does not look to the transform like a signal switched on and off.
3. **Transform** each windowed frame with an [FFT](/view.html?p=notes/epistemica/signal/fast-fourier-transform-fft.md), giving one complex spectrum per frame.
4. **Square** the magnitude, discarding the phase, and **assemble** the results as columns of a matrix: time across, frequency down, power as the value.

Two quantities follow from the parameters and nothing else: the frequency spacing between rows is $\Delta f = f_s / N$, and the time between columns is $\Delta t = H / f_s$. Both are fixed by the frame length and the hop, which is why those two numbers carry most of the design decision.

| Parameter | Symbol | What it controls |
| --- | --- | --- |
| Sampling rate | $f_s$ | The highest frequency that can appear, $f_s/2$; anything above folds back as aliasing. |
| Frame length | $N$ | Frequency resolution ($\Delta f = f_s/N$) and the time span each column summarises. |
| Hop | $H$ | Column spacing ($\Delta t = H/f_s$) and how smooth the picture looks. |
| Window | $g[n]$ | Trade between a narrow main lobe (resolution) and low side lobes (leakage). |
| Magnitude scaling | dB | The dynamic range shown; below the floor, quiet structure disappears. |

## The trade-off that defines it

Time and frequency resolution are not independent, and no setting buys both. A short frame localises an event in time and smears its frequency content across a wide band; a long frame resolves two close partials and smears their onsets. The bound is the same one that governs the uncertainty principle — the Gabor limit — and it is a property of the transform, not of the implementation.

This is why a spectrogram is read, not measured: what it shows is a *choice* about which structures to resolve. A frame chosen to make a vowel's formants legible will render a drum hit as a single broadband stripe; a frame chosen to place the transient precisely will blur the formants. Windowing restates the trade in another form — a window with a narrow main lobe resolves close frequencies but leaks energy into distant ones, and every window function is an argued compromise between the two.

## Reading a spectrogram

| What appears | What it means |
| --- | --- |
| Parallel horizontal bands | A harmonic series: the fundamental and its integer multiples, as in a sustained note or a voiced vowel. |
| A horizontal band that wobbles | Vibrato or frequency modulation — the partial moves, the harmonics move with it. |
| A vertical stripe spanning many frequencies | A transient: a click, a plosive, an impact. Short in time, broadband by construction. |
| A straight sloped line | A chirp — a frequency sweeping linearly, as in a sonar ping or a bird call. |
| A grainy floor | Broadband noise, spread evenly because it has no preferred frequency. |
| Brightness against a dark field | Power: the same frequency can be strong at one moment and absent the next, which is the thing a spectrum cannot show. |
| A band that folds back at the top | Aliasing — content above $f_s/2$ appearing as a mirror image below it. |

## Variants

| Variant | Frequency axis | What changes |
| --- | --- | --- |
| Linear spectrogram | Uniform bins | The plain STFT reading; every hertz gets the same row height. |
| Mel spectrogram | Mel scale | Bands spaced by perceived pitch rather than by hertz, which is why speech and audio models use it. |
| Log-frequency / constant-Q | Logarithmic | Constant relative resolution, so an octave occupies the same height everywhere; the choice for music. |
| Reassigned spectrogram | Sharpened | Each value is moved to the time–frequency point its phase implies, trading smoothness for precision. |
| Synchrosqueezed transform | Sharpened | A related reassignment that stays invertible, so components can be separated and reconstructed. |
| Scalogram | Wavelet scale | The same time–frequency job with a [wavelet](/view.html?p=notes/epistemica/signal/wavelet.md) kernel: fine time resolution at high frequency, fine frequency resolution at low. |

## Limits

The phase is discarded, and with it the exact waveform: a magnitude spectrogram determines the signal only up to phase, so reconstruction is either an iterative estimate — Griffin–Lim and its descendants — or a return to the complex STFT. Each column also assumes the frame is stationary, which is false at exactly the moments a spectrogram is most useful. Leakage and scalloping shift apparent amplitudes when a component falls between bins. And the resolution trade-off is not a defect to be fixed by a better algorithm: it is the shape of the object.

## References

- [Spectrogram](https://en.wikipedia.org/wiki/Spectrogram)
- [Short-time Fourier transform](https://en.wikipedia.org/wiki/Short-time_Fourier_transform)
- [Uncertainty principle / Gabor limit](https://en.wikipedia.org/wiki/Uncertainty_principle)
- [Mel scale](https://en.wikipedia.org/wiki/Mel_scale)
- Allen, J. B., & Rabiner, L. R. (1977). A unified approach to short-time Fourier analysis and synthesis. *Proceedings of the IEEE*, 65(11), 1558–1564.
- Harris, F. J. (1978). On the use of windows for harmonic analysis with the discrete Fourier transform. *Proceedings of the IEEE*, 66(1), 51–83.
- Griffin, D., & Lim, J. (1984). Signal estimation from modified short-time Fourier transform. *IEEE Transactions on Acoustics, Speech, and Signal Processing*, 32(2), 236–243.
- Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-time signal processing* (3rd ed.). Pearson.
- [Signal Processing](/view.html?p=notes/epistemica/signal/signal-processing.md) — the practice the spectrogram belongs to
- [Fourier Decomposition Toolkit](/view.html?p=notes/epistemica/signal/fourier-decomposition-toolkit.md) — the transform family it is built from
- [Wavelet](/view.html?p=notes/epistemica/signal/wavelet.md) — the scale-based alternative
- [Frequency (Periodicity)](/view.html?p=notes/nature/frequency-periodicity.md) — the natural property being represented
