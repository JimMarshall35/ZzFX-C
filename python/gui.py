import tkinter as tk
import zzfx

BACKEND_TICK_MS = 100
BACKEND_TICK_S = 0.1



class SynthParams:
    def set_default_values(self, params):
        for p in params:
            if p == "volume":
                self.params["volume"]["var"].set(1.0)
            elif p == "randomness":
                self.params["randomness"]["var"].set(0.05)
            elif p == "frequency":
                self.params["frequency"]["var"].set(220)
            elif p == "attack":
                self.params["attack"]["var"].set(0)
            elif p == "sustain":
                self.params["sustain"]["var"].set(0)
            elif p == "release":
                self.params["release"]["var"].set(0.1)
            elif p == "shape":
                self.params["shape"]["var"].set(0.1)
            elif p == "shapeCurve":
                self.params["shapeCurve"]["var"].set(1)
            elif p == "slide":
                self.params["slide"]["var"].set(0)
            elif p == "deltaSlide":
                self.params["deltaSlide"]["var"].set(0)
            elif p == "pitchJump":
                self.params["pitchJump"]["var"].set(0)
            elif p == "pitchJumpTime":
                self.params["pitchJumpTime"]["var"].set(0)
            elif p == "repeatTime":
                self.params["repeatTime"]["var"].set(0)
            elif p == "noise":
                self.params["noise"]["var"].set(0)
            elif p == "modulation":
                self.params["modulation"]["var"].set(0)
            elif p == "bitCrush":
                self.params["bitCrush"]["var"].set(0)
            elif p == "delay":
                self.params["delay"]["var"].set(0)
            elif p == "sustainVolume":
                self.params["sustainVolume"]["var"].set(0)
            elif p == "decay":
                self.params["decay"]["var"].set(0)
            elif p == "tremolo":
                self.params["tremolo"]["var"].set(0)
            elif p == "filter":
                self.params["filter"]["var"].set(0)
                
    def __init__(self):
        self.params = {
            "volume" : { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "Volume",
                "help" : "Volume scale (percent)"
            },
            "randomness": { 
                "var" : tk.DoubleVar(),
                "step" : .05,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "Randomness",
                "help" : "How much to randomize frequency (percent Hz)"
            },
            "frequency": { 
                "var" : tk.DoubleVar(),
                "step" : 1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "Frequency",
                "help" : "Frequency of sound (Hz)"
            },
            "attack": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "sustain": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "release": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "shape": { 
                "var" : tk.IntVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "shapeCurve": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "slide": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "deltaSlide": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "pitchJump": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "pitchJumpTime": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "repeatTime": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "noise": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "modulation": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "bitCrush": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "delay": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "sustainVolume": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "decay": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "tremolo": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            },
            "filter": { 
                "var" : tk.DoubleVar(),
                "step" : 0.1,
                "min" : -1e9,
                "max" : 1e9,
                "nicename" : "",
                "help" : ""
            }
        }
        self.set_default_values(self.params.keys())


root = None

params = None

def update_zzfx_backend():
    zzfx.zzfx_Update(BACKEND_TICK_S)
    root.after(BACKEND_TICK_MS, update_zzfx_backend)

def add_entry_rows(frame):
    onRow = 0
    for key in params.params.keys():
        val = params.params[key]
        l = tk.Label(frame, text=key)
        l.grid(column=0, row=onRow)
        e = tk.Entry(frame, textvariable=val["var"])
        e.grid(column=1, row=onRow)
        onRow += 1
    pass

def main():
    global root, params
    zzfx.zzfx_InitBackend()
    root = tk.Tk()
    root.title = "ZzFX GUI"
    root.after(BACKEND_TICK_MS, update_zzfx_backend)

    # initialize params
    params = SynthParams()

    # setup widgets
    text_entries_frame = tk.Frame(root)
    text_entries_frame.grid(row=0, column=0)
    add_entry_rows(text_entries_frame)

    root.mainloop()
    zzfx.zzfx_ShutdownBackend()

main()