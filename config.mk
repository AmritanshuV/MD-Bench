# Supported: GCC, CLANG, ICC
TAG ?= ICC
ENABLE_LIKWID ?= false
# SP or DP
DATA_TYPE ?= DP
# AOS or SOA
DATA_LAYOUT ?= AOS

# Number of times to run the neighbors loop
NEIGHBORS_LOOP_RUNS ?= 1
# Explicitly store and load atom types
EXPLICIT_TYPES ?= false
# Trace memory addresses for cache simulator
MEM_TRACER ?= false

#Feature options
OPTIONS =  -DALIGNMENT=64
#OPTIONS +=  More options