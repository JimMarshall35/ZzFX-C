#################################################
#################################################
###                                           ###
###  Python bindings for zzfx openAL backend  ###
###                                           ###
#################################################
#################################################

import ctypes

zzfx_so = ctypes.CDLL("libZzFX_OpenAL.so")

zzfx_so.zzfx_InitBackend.argtypes = ()
zzfx_so.zzfx_InitBackend.restype = None

zzfx_so.zzfx_Update.argtypes = [ctypes.c_float]
zzfx_so.zzfx_Update.restype = None

zzfx_so.zzfx_ShutdownBackend.argtypes = ()
zzfx_so.zzfx_ShutdownBackend.restype = None

zzfx_so.zzfx.argtypes = (
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float
)
zzfx_so.zzfx.restype = ctypes.c_float

zzfx_so.zzfx_IsSoundPlaying.argtypes = ()
zzfx_so.zzfx_IsSoundPlaying.restype = ctypes.c_bool

zzfx_so.zzfx_GetMasterVolume.argtypes = ()
zzfx_so.zzfx_GetMasterVolume.restype = ctypes.c_float

zzfx_so.zzfx_SetMasterVolume.argtypes = [ctypes.c_float]
zzfx_so.zzfx_SetMasterVolume.restype = None


def zzfx_InitBackend():
    zzfx_so.zzfx_InitBackend()

def zzfx_ShutdownBackend():
    zzfx_so.zzfx_ShutdownBackend()

def zzfx_Update(deltaT):
    zzfx_so.zzfx_Update(ctypes.c_float(deltaT))

def zzfx_IsSoundPlaying():
    result = zzfx_so.zzfx_IsSoundPlaying()
    return bool(result)

def zzfx_GetMasterVolume():
    result = zzfx_so.zzfx_GetMasterVolume()
    return float(result)

def zzfx_SetMasterVolume(vol):
    zzfx_so.zzfx_SetMasterVolume(ctypes.c_float(vol))

def zzfx(
        volume,
        randomness,
        frequency,
        attack,
        sustain,
        release,
        shape,
        shapeCurve,
        slide,
        deltaSlide,
        pitchJump,
        pitchJumpTime,
        repeatTime,
        noise,
        modulation,
        bitCrush,
        delay,
        sustainVolume,
        decay,
        tremolo,
        filter
    ):
    result = zzfx_so.zzfx(
        ctypes.c_float(volume),
        ctypes.c_float(randomness),
        ctypes.c_float(frequency),
        ctypes.c_float(attack),
        ctypes.c_float(sustain),
        ctypes.c_float(release),
        ctypes.c_float(shape),
        ctypes.c_float(shapeCurve),
        ctypes.c_float(slide),
        ctypes.c_float(deltaSlide),
        ctypes.c_float(pitchJump),
        ctypes.c_float(pitchJumpTime),
        ctypes.c_float(repeatTime),
        ctypes.c_float(noise),
        ctypes.c_float(modulation),
        ctypes.c_float(bitCrush),
        ctypes.c_float(delay),
        ctypes.c_float(sustainVolume),
        ctypes.c_float(decay),
        ctypes.c_float(tremolo),
        ctypes.c_float(filter))
    return float(result)