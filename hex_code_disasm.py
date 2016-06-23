#!/usr/bin/python
# -*- coding: UTF-8 -*-

from capstone import *

# arm 64
Architecture = CS_ARCH_ARM64 # CS_ARCH_X86
BasicMode = CS_MODE_ARM # CS_MODE_64

# modify 
kernel_base_addr = 0xffffffc000080000
disasm_start_addr = 0xffffffc0003431b4
kernel_file_path = "/Users/idhyt/OneDrive/doing/kernel/redmi_note2_kernel"


def get_hex_code(f_name, start, len=0x100):
    f = open(f_name,"rb")
    f.seek(start, 0);
    content = f.read(len)
    f.close()
    return content


def disasm_hex_code(hex_code, base_addr=0x1000):
    try:
        md = Cs(Architecture, BasicMode)
        for i in md.disasm(hex_code, base_addr):
            print "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)
    except CsError as e:
        print str(e)

def main():

    disasm_file_offset = disasm_start_addr - kernel_base_addr

    buf = get_hex_code(kernel_file_path, disasm_file_offset, 0x100)

    disasm_hex_code(buf, disasm_start_addr)


if __name__ == '__main__':
    main()



