# Advanced Linux Sound Architecture


> 

Guiding questions:

- How does the Linux audio subsystem interact with Bluetooth audio devices?
    - How can connection and disconnection issues be debugged effectively?
    - What is the structure of the implementation, and what is the interaction map?
    - What mechanisms mediate interactions between components?
    - Which types of signal interference or latency issues can affect Bluetooth audio performance?
- How can I identify the components and configuration of my user-space audio stack?
- What additional questions should be considered when analyzing Linux audio and Bluetooth interactions?
- Which user space tools can I used to interact with the audio sub system?

## QA

### How to identify the Linux audio user Stack?

```bash
ps -e | grep -E 'pipewire|pulseaudio'
ls /run/user/$(id -u)/ | grep -E 'pulse|pipewire'
```

### How can connection and disconnection issues be debugged effectively?

> Assumptions: Pipewire; Linux.
> 

> The issue (connect-disconect)  when not playing audio - was trigger  by some Idle suspend / auto-release behavior in PipeWire / WirePlumber for Bluetooth A2DP. This is actually a feature.
> 

> Test:  `speaker-test -t sine -f 440`
> 

> Unable to fix this  - let play an audio automatically when nothing is getting play - a slow audio stuff jut to keep the bluetooth connection.
> 

```bash
while true; do pw-play /usr/share/sounds/alsa/Front_Center.wav; sleep 5; done

or 

aplay -D pipewire -f S16_LE -r 48000 -c 2 /dev/zero
```

To fix this  jut disable auto-release:

```bash
mkdir -p ~/.config/wireplumber/main.lua.d
nano ~/.config/wireplumber/main.lua.d/disable-suspend.lua
```

```bash
if bluez_monitor and bluez_monitor.rules then
  table.insert(bluez_monitor.rules, {
    matches = {
      {
        { "node.name", "matches", "*" },
      },
    },
    apply_properties = {
      ["session.suspend-timeout-seconds"] = 300,
    },
  })
end
```

```bash
sudo sh -c 'echo Y > /sys/module/bluetooth/parameters/disable_ertm'
```

- `pw-top`: …
- `pw-cli list-objects | grep -i bluez`: …
- `wpctl status`: …
- `dpkg -l | grep libspa-0.2-bluetooth`
- journalctl -u bluetooth -f
- journalctl --user -u pipewire -f
- journalctl --user -u wireplumber -f
- bluetoothctl
- 

## References

- https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture
- https://www.yashagarwal.in/notes/debug-bluetooth-on-linux/
- https://www.reddit.com/r/linuxmint/comments/1e32j6t/fixing_bluetooth_issues_on_linux_a_stepbystep/
- https://www.bluez.org/
- https://pipewire.org/
- https://en.wikipedia.org/wiki/List_of_Bluetooth_profiles