import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random
import numpy as np

@cocotb.test()
async def random_write_read_test(dut):
     # test positive imm = 123 with source = 0
     imm = 0b000001111011 # 123
     imm <<= 13 
     source = 0b00
     # 25 bits sent to sign extend - data before will be ignored
     # masked for space for testing
     random = 0b000000000000_1010101010101
     raw_data = random | imm
     await Timer(1, unit="ns")
     dut.raw_src.value = raw_data
     dut.imm_source.value = source
     await Timer(1, units="ns")
     assert dut.immediate.value == "00000000000000000000000001111011"
     assert int(dut.immediate.value) == 123

     # testing negative, imm = -42, source = 0

     imm = 0b111111010110 # -42
     imm <<= 13 
     source = 0b00
     random = 0b000000000000_1010101010101
     raw_data = random | imm
     await Timer(1, unit="ns")
     dut.raw_src.value = raw_data
     dut.imm_source.value = source
     await Timer(1, unit="ns")
     assert dut.immediate.value == "11111111111111111111111111010110"
     # python interprets int as uint, sub 1<<32 as int to get corresponding negative
     assert int(dut.immediate.value) - (1 << 32) == -42
     


