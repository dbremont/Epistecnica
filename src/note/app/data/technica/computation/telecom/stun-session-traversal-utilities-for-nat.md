# STUN (Session Traversal Utilities for NAT)

- [TURN (Traversal Using Relays around NAT)](note.html?n=technica/computation/telecom/turn-traversal-using-relays-around-nat.md), [Interactive Connectivity Establishment (ICE)](note.html?n=technica/computation/telecom/interactive-connectivity-establishment-ice.md)

> 

```jsx
NAT Traversal
      │
      ▼
     ICE
   ┌──┴──┐
   │     │
 STUN   TURN
```

- [ ]  What is it?
- [ ]  Which are the functionality?
- [ ]  Quite frankly I have a huge amount of non understanding of this.
- [ ]  When STUN is enougth?
- [ ]  What is the mechanisms?

device → NAT Router → internet device.

- (Temporal Comunication Window) When the device send the package the ip - will be re-written -  so when there is a resonse - the nat router - used its internal translation table - to pick the right device.
    - This creates an open channel between the relay - device - that is if a outboudn packge come - it will be relay to the device.
    - Instead, **the NAT router keeps the mapping in its own internal translation table**.
- Port Forwring (Permanmetn Communication Window) Every package that commes to this relay - port - will be send to the this ip |  port.

```jsx
Device
   │
   │  (1) Send packet
   ▼
NAT Router
   │
   │  Creates temporary communication window
   │
   │  192.168.1.10:5000
   │          ↔
   │ 203.0.113.25:62001
   ▼
STUN Server
```

**STUN**

- Discovers the external identifier (public IP and port) of an existing communication window.
- …

## References

- https://en.wikipedia.org/wiki/STUN
- https://en.wikipedia.org/wiki/UDP_hole_punching