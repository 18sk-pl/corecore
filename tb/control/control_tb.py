import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray 


async def set_unknown(dut):
    # dut.func3.value = BinaryValue("XXX")
    # dut.func7.value = BinaryValue("XXXXXXX")
    # dut.alu_zero.value = BinaryValue("X")
    # dut.alu_last_bit.value = BinaryValue("X")
    await Timer(1, unit="ns")

@cocotb.test()
async def control_test(dut):
    await set_unknown(dut)

    # test control signals for lw 
    dut.op.value = 0b0000011 # lw !
    await Timer(1, unit="ns")
    assert dut.alu_control.value == 0b000 
    assert dut.imm_source.value == 0b00
    assert dut.mem_write.value == 0 
    assert dut.reg_write.value == 1 

