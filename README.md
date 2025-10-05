# terminus-est

> Resolution and a plan are better than a sword, because a man whets his own edges on them.
> > Gene Wolfe - The Citadel of the Autarch

---

## Background
Terminus Est is a ergo-inspired keyboard tuned to my developer workflow.
I've tended to cluster my actions around vim-inpsired keybindings with discrete "leader" keys, and started to wish that my leader keys were a bit easier to hit.

This project was frustratingly complicated, too expensive, and ultimately worse than my perfectly fine, working keyboards. But it's worth it to build something cool.

Thanks to @dededecline for the great advice and @kh3dron for making the plate look nice when I couldn't figure out the CAD stuff.

---

## Gallery

<details open>
<summary>PCB</summary>

### Front
<img src="./assets/pcb_front.png" width="800">

### Back
<img src="./assets/pcb_back.png" width="800">

### Traces
<img src="./assets/pcb_traces.png" width="800">
</details>

<details open>
<summary>Layout</summary>

<img src="./assets/layout.png" width="800">
</details>

<details open>
<summary>Plate</summary>

<img src="./assets/plate.png" width="800">
</details>

<details open>
<summary>Case</summary>

<img src="./assets/case.png" width="800">
</details>

---

## Pinout

```mermaid
graph TB
    subgraph Left["Left Side - Columns & Rows"]
        L1["GP0 → COL0"]
        L2["GP1 → COL1"]
        L3["GP2 → COL2"]
        L4["GP3 → COL3"]
        L5["GP4 → COL4"]
        L6["GP5 → COL5"]
        L7["GP6 → COL6"]
        L8["GP7 → COL7"]
        L9["GP8 → COL8"]
        L10["GP9 → COL9"]
        L11["GP10 → ROW0"]
        L12["GP11 → ROW1"]
        L13["GP12 → ROW2"]
        L14["GP13 → ROW3"]
        L15["GP14 → ROW4"]
        L16["GP15 → ROW5"]
    end

    subgraph Right["Right Side - Columns"]
        R1["GP16 → COL12"]
        R2["GP17 → COL13"]
        R3["GP18 → COL14"]
        R4["GP19 → COL15"]
        R5["GP20 → COL16"]
        R6["GP21 → COL17"]
        R7["GP22 → COL18"]
        R8["GP26 → COL19"]
        R9["GP27 → COL20"]
        R10["GP28 → COL21"]
    end
```

---

## Built With

- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- [KLE (Keyboard Layout Editor)](http://www.keyboard-layout-editor.com/)
- [KiCad](https://www.kicad.org/)
- [Fusion 360](https://www.autodesk.com/products/fusion-360/)
- [keyboard-tools.xyz](https://keyboard-tools.xyz/)
- [kbplate (ai03)](https://kbplate.ai03.com/)
- [KMK Firmware](https://github.com/KMKfw/kmk_firmware)
- [OpenSCAD](https://openscad.org/)
