/**
    @file openAL.h
    @brief provides an implementation of "zzfx" using openAL
*/

#ifndef ZZFX_OPENAL_H
#define ZZFX_OPENAL_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>

struct ZZFXSound;

/// @brief play a sound immediately
/// @param pSound 
/// @return length of sound playing in seconds
float zzfx(struct ZZFXSound* pSound);

/// @brief initialize the backend - call this once before zzfx
int zzfx_InitBackend();

/// @brief destroy the backend when done
void zzfx_ShutdownBackend();

/// @brief master volume applied on top of volume from the zzfx call args
/// @param v 
void zzfx_SetMasterVolume(float v);

/// @brief get the master volue set with zzfx_SetMasterVolume
/// @return 
float zzfx_GetMasterVolume();

/// @brief tell the backend that time has passed, call regularly
/// @param deltaT seconds passed
/// @return 
void zzfx_Update(float deltaT);

/// @brief returns whether sound is playing or not
/// @return 
bool zzfx_IsSoundPlaying();

#ifdef __cplusplus
}
#endif

#endif