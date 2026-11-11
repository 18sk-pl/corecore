# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog
EXTRA_ARGS += --trace --trace-structs
WAVES = 1

VERILOG_SOURCES += $(PWD)/../../src/memory.sv

TOPLEVEL = memory

MODULE = memory_tb

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
