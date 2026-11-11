import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def add_test(dut):
    await Timer(1, unit="ns")
    dut.alu_control.value = 0b000
    await Timer(1, unit="ns")
    for _ in range(1000):
        src1 = random.randint(0, 0xFFFFFFFF)
        src2 = random.randint(0, 0xFFFFFFFF)
        dut.src1.value = src1
        dut.src2.value = src2
        # mask expected value to not take account for overflow
        expected = (src1 + src2) & 0xFFFFFFFF
        
        await Timer(1, unit="ns")
        assert int(dut.alu_result.value) == expected

@cocotb.test()
async def default_test(dut):
    await Timer(1, unit="ns")
    dut.alu_control.value = 0b111
    src1 = random.randint(0, 0xFFFFFFFF)
    src2 = random.randint(0, 0xFFFFFFFF)
    dut.src1.value = src1
    dut.src2.value = src2
    expected = 0

    await Timer(1, unit="ns")
    assert int(dut.alu_result.value) == expected

@cocotb.test()
async def zero_test(dut):
    await Timer(1, unit="ns")
    dut.alu_control.value = 0b000
    dut.src1.value = 123
    dut.src2.value = (-123) & 0xFFFFFFFF # coco raises errors when assigning a negative int to unsigned signal
    
    await Timer(1, unit="ns")
    
    assert int(dut.zero.value) == 1
    assert int(dut.alu_result.value) == 0

