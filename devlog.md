# Devlog

## Learning things

## Findings up to log

So far I've:
- Gone through a bunch of keyboard designs on KLE. Realized ergogen might have been the thing to start with, but for this build I'll stick with KLE.
- Finally landed on one that sorta matches the normal keyboard layout (but split) that I was going for. Seems straightforward, not too crazy.
- Found something to generate a kicad schematic (keyboard tools xyz).
- Found a microcontroller (rpi pico 2). It has 26 available GPIO pins for me to use, and I have 6 rows and 20 columns, so it seems kinda perfect for my needs. 
- Started learning about PCB basics. Routes/traces, vias, Kicad software, etc. The python scripting console is useful but kinda hard to hook into.

### 09/22/2025

The realization I came to yesterday with @kh3dron was that I should add some more layers to the PCB.
Rather than punch a bunch of holes in the PCB, this would let me run connections over each other (if I understand it right).
Shouldn't need many more. I want to keep the microcontroller centered so I think this would work fine. This way I can keep my vertical traces on one layer, my horizontal traces on another,
and my connections from ROW/COL to the microcontroller on a third layer. That way, nothing is going to actually run into each other.

To figure out:
- SMD vs THT for the microcontroller -- I'm going to pay the fab to just solder on all the components so IDK if there's any real diff here.
- Diode direction impact on direction of traces. Also, can I just have the trace from a ROW/COL start anywhere on that thing or is it specifically at one end?
- Throwing a graphic on this bad boy.
- How the heck (once finished) I can tell JCLPCB to use the right components. 
- What is the kicad schematic editor used for lol. Seems like it's mentioned in guides but I haven't need to touch it? I just add footbprints from public libraries in the PCB editor itself when I need to? 
