import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random
import numpy as np

@cocotb.test()
async def random_write_read_test(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    await RisingEdge(dut.clk)

    dut.rst_n.value = 0
    dut.write_enable.value = 0
    dut.address1.value = 0
    dut.address2.value = 0
    dut.address3.value = 0
    dut.write_data.value = 0

    await RisingEdge(dut.clk)
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    theoretical_regs = [0 for _ in range(32)]

    for _ in range(1000): # write & read random values
        address1 = random.randint(1, 31)
        address2 = random.randint(1, 31)
        address3 = random.randint(1, 31)
        write_value = random.randint(1, 0xFFFFFFFF)
        
        await Timer(1, unit="ns")
        dut.address1.value = address1
        dut.address2.value = address2
       
        await Timer(1, unit="ns")
        assert dut.read_data1.value == theoretical_regs[address1]
        assert dut.read_data2.value == theoretical_regs[address2]
        
        dut.address3.value = address3
        dut.write_enable.value = 1
        dut.write_data.value = write_value
        await RisingEdge(dut.clk)
        dut.write_enable.value = 0
        theoretical_regs[address3] = write_value
        await Timer(1, unit="ns")

    await Timer(1, unit="ns")
    dut.address3.value = 0
    dut.write_enable.value = 1
    dut.write_data.value = 0xAEAEAEAE
    await RisingEdge(dut.clk)
    dut.write_enable.value = 0
   

    await Timer(1, unit="ns")
    dut.address1.value = 0
    await Timer(1, unit="ns")
 
    assert int(dut.read_data1.value) == 0

    print("random read/write test completed successfully")






