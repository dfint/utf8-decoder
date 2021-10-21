# utf8-decoder

[![Python UTF-8 Decoder Test](https://github.com/dfint/utf8-decoder/actions/workflows/py-utf8-decoder-test.yml/badge.svg)](https://github.com/dfint/utf8-decoder/actions/workflows/py-utf8-decoder-test.yml) 
[![C UTF-8 Decoder Test](https://github.com/dfint/utf8-decoder/actions/workflows/c-utf8-decoder-test.yml/badge.svg)](https://github.com/dfint/utf8-decoder/actions/workflows/c-utf8-decoder-test.yml)

A prototype of a minimalistic utf-8 to utf-16 converter. Includes implementations in Python and C.

Why? To patch standard DF [cp437_to_unicode](https://github.com/svenstaro/dwarf_fortress_unfuck/blob/4dd42cda9d439d9cf89a32f1f57a54836e6723ce/g_src/ttf_manager.cpp#L59) to add support of utf-8.
