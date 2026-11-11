# Defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog
EXTRA_ARGS += --trace --trace-structs
WAVES = 1

# Include testbench path in Python module lookup
PYTHONPATH += $(PWD):$(PYTHONPATH)

VERILOG_SOURCES += $(PWD)/../../src/registers.sv

TOPLEVEL = registers
COCOTB_TEST_MODULES = register_tb

# Include cocotb's make rules
include $(shell cocotb-config --makefiles)/Makefile.sim
