# Devlog

### Findings up to log

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

### 09/23/2025
Talked to @dededecline, she directed me to:
- Go with SMD, bc I don't wanna care about soldering.
- Diode direction doesn't matter for my current use case, they're all going the same way now.
- Generate BOM for JCLPCB.
- No need to use the schematic editor, just use the PCB editor.

Remaining tasks:
- Finish routing -- I did this successfully yesterday and got the big check mark from Dani, but I messed up and forgot a whole column. Going to redo them today, and I realized I might as well just use 4 layers instead of 2 for cleanliness.
- Mounting holes.
- Grab a graphic from the homie Trevor and use that on the board.
- Generate BOM and send to JCLPCB.
- Write firmwarre.
- Figure out case stuff (wait until pcb gets here).

### 09/24/2025
Ask about the following:
- How to make the pcb symettrical? 
- Does the mounting hole placement matter? 
- Workflow for filling out BOM.
- Make sure I'm choosing the right components.
- How to make sure the silkscreen design gets printed? 
- Add ground? dedicated grounding layer? and how not to short out? 

Got answers from Dani:
- Don't worry about that, draw straight lines.
- Delete the holes, silly.
- I just ended up using a plugin that was available in Kicad.
- Site helps you choose.
- Exclude the violations.
- No ground layer || dedicated pour needed and I can leave the ground pins unconnected.

### 09/25/2025

- Fixed up the pcb, ordered. Expensive! Messed up the silkscreen logo on the back lol but I'm keeping it in as a fun quirk.
- Made a plate, @kh3dron helped me actually fix it up in fusion 360 because I couldn't figure out the software. By fix it up he did it all.
- For switches, taking the glorious pandas that were in my keychron. For keycaps, found some blank PBT keycaps on amazon I liked.

### 10/16/2025

Everything is here! After looking at the layout a bit and pretending to type, I've realized my layout is a little silly. I'm removing the bottom three keys in the thumb clusters and the bottom two keys on either side of the board (just going to hide them with the plate). I've also decided to reorder the plate, but this time powder coated, along with a 3d printed case that will be nicer to look at.
