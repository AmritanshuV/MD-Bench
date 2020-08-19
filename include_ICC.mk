CC  = icc
CXX = icpc
LINKER = $(CC)

PROFILE  = #-g  -pg
OPTS     = -Ofast -xCORE-AVX512 -qopt-zmm-usage=high $(PROFILE)
#OPTS     = -O3 -xCORE-AVX2  $(PROFILE)
#OPTS     = -O3 -xAVX  $(PROFILE)
#OPTS     = -O3 -xSSE4.2 $(PROFILE)
#OPTS     = -O3 -no-vec $(PROFILE)
#OPTS     =  -Ofast -xHost $(PROFILE)
CFLAGS   = $(PROFILE) -restrict $(OPTS)
CXXFLAGS = $(CFLAGS)
ASFLAGS  = -masm=intel
FCFLAGS  =
LFLAGS   = $(PROFILE) $(OPTS)
DEFINES  = -D_GNU_SOURCE  -DALIGNMENT=64 # -DLIKWID_PERFMON   -DPRECISION=1
INCLUDES =
LIBS     =
