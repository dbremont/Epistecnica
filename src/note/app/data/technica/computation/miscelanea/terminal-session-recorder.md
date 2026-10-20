---
tags: [tool]
---

# Terminal Session Recorder

- [Terminal Emulator](note.html?n=technica/computation/miscelanea/terminal-emulator.md)

> In this note, we will explore a class of systems called **Terminal Session Recorders**—systems that capture, store, and replay the interaction between a user and a terminal session.
> 

## Formulation

> What is a Terminal Session Recorder? A **Terminal Session Recorder** is a system that captures the interaction stream of a terminal session—including terminal input, process output, timing, and, depending on the implementation, terminal state—so that the session can be **replayed, inspected, audited, or shared**.
> 

## Interface

> What interface does a Terminal Session Recorder expose? How to interact with a ‘Terminal Session Recorder’?
> 

> **Terminal Session Recorder Interface:** an interface for starting/stopping recording, capturing terminal input/output, storing session recordings, and replaying or inspecting recorded sessions.
> 

| Operation | Interaction |
| --- | --- |
| **Start recording** | Attach the recorder to a terminal session |
| **Capture** | Observe terminal input/output events |
| **Stop recording** | Terminate the capture |
| **Store** | Persist the captured session |
| **List sessions** | Query available recordings |
| **Replay** | Reproduce the recorded terminal output over time |
| **Seek** | Jump to a point in the recording |
| **Inspect** | Examine commands, output, timestamps, metadata |
| **Export** | Produce a recording in a portable format |

## Implementation

> Which are the implementation mechanisms?
> 

| **Implementation Mechanism** | **Description** |
| --- | --- |
| **PTY Interception** | Place the recorder around a pseudo-terminal (PTY) so that terminal input/output passes through the recorder. |
| **I/O Capture** | Capture the byte streams flowing between the terminal endpoint and the session process. |
| **Timing Capture** | Record timestamps, durations, or inter-event delays so playback can reproduce the original temporal behavior. |
| **Terminal-State Capture** | Capture state required to reproduce the session, such as terminal dimensions, resize events, and terminal control sequences. |
| **Session Serialization** | Encode captured events, data, timing, and metadata into a persistent recording format. |
| **Replay Engine** | Read the serialized event stream and reproduce it against a terminal emulator or PTY. |

## Terminal Session Recorder System System

| **System Instance** | **Description** | **Capability Set** |
| --- | --- | --- |
| **script** | Records a terminal session by capturing terminal I/O to a file. | Input/Output Capture; Timing; Session Storage; Replay |
| **asciinema** | Records terminal sessions as structured terminal events that can be replayed or shared. | Input/Output Capture; Timing; Replay; Sharing; Publishing |
| **ttyrec** | Records terminal input/output together with timing information for later playback. | I/O Capture; Timing; Session Storage; Replay |
| **TermRecord** | Records terminal sessions and generates replayable recordings, commonly for documentation. | Recording; Replay; Export; Documentation |
| **tlog** | Records terminal sessions for auditing and security monitoring. | Session Recording; Audit Logging; Storage; Playback |

## QA

### How to start recording with script?

`script` starts a new shell session and records the terminal session's output.

```
script --timing=session.time session.log
```

### How to replay with script?

`script` itself is primarily a **recorder**, not a full replay engine. The traditional companion utility is `scriptreplay`.

If you recorded timing information:

```
script--timing=session.time session.log
```

you can replay it with:

```
scriptreplay session.time session.log
```

The timing file contains the delays between output events, allowing `scriptreplay` to reproduce the session approximately as it originally appeared.

### How can this tools be used to improve our productivity?

| Productivity Benefit | How the recorder helps |
| --- | --- |
| **Reproduce** | Replay a previously performed terminal procedure. |
| **Debug** | Review exactly what happened during a failed session. |
| **Document** | Turn a real terminal session into operational documentation. |
| **Share** | Give another person a recording of the actual workflow. |
| **Teach** | Demonstrate commands and their output as a single artifact. |
| **Audit** | Preserve a chronological record of terminal activity. |
| **Review** | Inspect commands, output, timing, and session behavior after the fact. |
| **Automate** | Use recorded workflows as candidates for scripts or automation. |

## References

- [Linux Graphics Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-graphics-stack.md)