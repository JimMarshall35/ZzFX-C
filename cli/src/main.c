#include "openAL.h"
#include "stdio.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "ZzFX.h"

void Usage()
{
    const char* usage = 
    "zzfx cli:\n"
    "Play a sound generatd on https://killedbyapixel.github.io/ZzFX/ to see what it will sound like in the game"
    "[zzfx-args] [OPTIONS]\n"
    "zzfx-args:\n"
    "   the output from the inner function call generated from https://killedbyapixel.github.io/ZzFX/ when \"full\" is selected (defaults to \"compact\")"
    "   for example \"1.4,.05,61,.03,.27,.38,4,1.2,0,0,0,0,0,1.6,0,.4,.37,.35,.15,0,1256\"\n"
    "OPTIONS:\n"
    "--master-vol -v\n"
    "   master volume, defaults to 0.2\n"
    ;
    printf(usage);
}

int Str_Tokenize(char* string, char sep)
{
	int outNumTokens = 0;
	if(*string != '\0')
	{
		outNumTokens = 1;
	}
	while(*string != '\0')
	{
		if(*string == sep)
		{
			outNumTokens++;
			*string = '\0';
		}
		string++;
	}
	return outNumTokens;
}

void Str_AdvanceToNextToken(char** pNextToken)
{
	char* pC = *pNextToken;
	while(*pC != '\0') pC++;
	pC++;
	*pNextToken = pC;
}

char* CopyString(const char* s)
{
    char* s2 = malloc(strlen(s) + 1);
    strcpy(s2, s);
    return s2;
}

struct ZZFXSound ParseZzfxCall(char* call)
{
    struct ZZFXSound snd;
    float* asFloats = &snd.volume;
    char* copy = CopyString(call);
    char* token = copy;
    int numTokens = Str_Tokenize(copy, ',');
    for(int i=0; i<numTokens; i++)
    {
        float f = (double)atof(token);
        asFloats[i] = f;
        Str_AdvanceToNextToken(&token);
    }
    free(copy);
    return snd;
}

int main(int argc, char** argv)
{
    srand(time(NULL));
    int repeats = 1;
    float waitBetweenRepeats = 0.0f;
    float masterVol = 0.2f;
    if(argc <= 1)
    {
        Usage();
        return 1;
    }
    int onArg = 1;
    char* zzfxCall = argv[onArg++];
    struct ZZFXSound snd = ParseZzfxCall(zzfxCall);
    while(onArg < argc)
    {
        if(strcmp(argv[onArg], "--master-vol") == 0 || strcmp(argv[onArg], "-v") == 0)
        {
            onArg++;
            masterVol = (float)atof(argv[onArg]);
        }
        onArg++;
    }

    zzfx_InitBackend();
    printf("Inited backend\n");

    zzfx_SetMasterVolume(masterVol);
    printf("set master volume\n");
    float lengthSeconds = zzfx(&snd);
    printf("lenght seconds: %.2f\n", lengthSeconds);
    usleep(lengthSeconds * 1000000 + waitBetweenRepeats * 1000000);
    
    zzfx_ShutdownBackend();
}