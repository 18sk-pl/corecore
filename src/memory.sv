// memory.sv

module memory #(
    parameter WORDS = 64
)   (
    input logic clk,
    input logic [31:0] address,
    input logic [31:0] write_data,
    input logic write_enable,
    input logic rst_n,

    output logic [31:0] read_data
);

/*
* byte addressed memory
* no support for mis-aligned writes/reads
*/

localparam INDEX_BITS = $clog2(WORDS);

reg [31:0] mem [0 : WORDS - 1]; // 32 bit memory array of words

always @ (posedge clk) begin
    // initialise all memory to be 0
    if (rst_n == 1'b0) begin
        for (int i=0; i < WORDS; i++) begin
            mem[i] <= 32'b0;
        end
    end
    else if (write_enable) begin
        // ensure address aligned to a word boundary
        // else ignore write
        if (address[1:0] == 2'b00) begin
            // [31:2] = word index
            mem[address[1 + INDEX_BITS : 2]] <= write_data;
        end
    end
end

always_comb begin
    // addresses [31:2] is the word index
    read_data = mem[address[1 + INDEX_BITS : 2]];
end

endmodule
