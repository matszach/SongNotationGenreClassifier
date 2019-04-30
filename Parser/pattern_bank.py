
# ===========================================================================
# base pitch (C -1)
base_pitch = 0

# ===========================================================================
# patterns for instrument / base pitch recognition
pitch_pattern_bank = []


# == GUITARS ==

# e4 B3 G3 D3 A2 E2
guitar6_note_symbols = ['E', 'B', 'G', 'D', 'A', 'E']
guitar6_pitch_values = [64, 59, 55, 50, 45, 40]
guitar6 = (guitar6_note_symbols, guitar6_pitch_values)
pitch_pattern_bank.append(guitar6)
# e4 B3 G3 D3 A2 A1
guitar6_doubleA_note_symbols = ['E', 'B', 'G', 'D', 'A', 'A']
guitar6_doubleA_pitch_values = [64, 59, 55, 50, 45, 33]
guitar6_doubleA = (guitar6_doubleA_note_symbols, guitar6_doubleA_pitch_values)
pitch_pattern_bank.append(guitar6_doubleA)
# e4 B3 G3 D3 A2 D2
guitar6_dropD_note_symbols = ['E', 'B', 'G', 'D', 'A', 'D']
guitar6_dropD_pitch_values = [64, 59, 55, 50, 45, 38]
guitar6_dropD = (guitar6_dropD_note_symbols, guitar6_dropD_pitch_values)
pitch_pattern_bank.append(guitar6_dropD)
# e4 B3 G3 D3 G2 D2
guitar6_dropDG_note_symbols = ['E', 'B', 'G', 'D', 'G', 'D']
guitar6_dropDG_pitch_values = [64, 59, 55, 50, 43, 38]
guitar6_dropDG = (guitar6_dropDG_note_symbols, guitar6_dropDG_pitch_values)
pitch_pattern_bank.append(guitar6_dropDG)
# e4 B3 G3 B3 G2 E2
guitar6_openEm_note_symbols = ['E', 'B', 'G', 'B', 'G', 'E']
guitar6_openEm_pitch_values = [64, 59, 55, 47, 43, 40]
guitar6_openEm = (guitar6_openEm_note_symbols, guitar6_openEm_pitch_values)
pitch_pattern_bank.append(guitar6_openEm)
# d4 A3 G3 D3 A2 D2
guitar6_openDsus4_note_symbols = ['D', 'A', 'G', 'D', 'A', 'D']
guitar6_openDsus4_pitch_values = [62, 57, 55, 50, 45, 38]
guitar6_openDsus4 = (guitar6_openDsus4_note_symbols, guitar6_openDsus4_pitch_values)
pitch_pattern_bank.append(guitar6_openDsus4)
# d4 B3 G3 D3 G2 D2
guitar6_openD6_note_symbols = ['D', 'B', 'G', 'D', 'G', 'D']
guitar6_openD6_pitch_values = [62, 59, 55, 50, 43, 38]
guitar6_openD6 = (guitar6_openD6_note_symbols, guitar6_openD6_pitch_values)
pitch_pattern_bank.append(guitar6_openD6)
# d4 A3 F3 C3 G2 D2
guitar6_Dst_note_symbols = ['D', 'A', 'F', 'C', 'G', 'D']
guitar6_Dst_pitch_values = [62, 57, 53, 48, 43, 38]
guitar6_Dst = (guitar6_Dst_note_symbols, guitar6_Dst_pitch_values)
pitch_pattern_bank.append(guitar6_Dst)
# d4 A3 F3 C3 G2 C2
guitar6_dropC_note_symbols = ['D', 'A', 'F', 'C', 'G', 'C']
guitar6_dropC_pitch_values = [62, 57, 53, 48, 43, 36]
guitar6_dropC = (guitar6_dropC_note_symbols, guitar6_dropC_pitch_values)
pitch_pattern_bank.append(guitar6_dropC)
# e4 B3 G3 D3 A2 E2 B2
guitar7_note_symbols = guitar6_note_symbols + ['B']
guitar7_pitch_values = guitar6_pitch_values + [35]
guitar7 = (guitar7_note_symbols, guitar7_pitch_values)
pitch_pattern_bank.append(guitar7)
# e4 B3 G3 D3 A2 E2 B2 F#1
guitar8_note_symbols = guitar7_note_symbols + ['F#']
guitar8_pitch_values = guitar7_pitch_values + [30]
guitar8 = (guitar8_note_symbols, guitar8_pitch_values)
pitch_pattern_bank.append(guitar8)


# == BASSES ==

# G2 D2 A1 E1
bass4_note_symbols = ['G', 'D', 'A', 'E']
bass4_pitch_values = [43, 38, 33, 28]
bass4 = (bass4_note_symbols, bass4_pitch_values)
pitch_pattern_bank.append(bass4)
# G2 D2 A1 E1 rev
bass4_Erev_note_symbols = ['E', 'A', 'D', 'G']
bass4_Erev_pitch_values = [28, 33, 38, 43]
bass4_Erev = (bass4_Erev_note_symbols, bass4_Erev_pitch_values)
pitch_pattern_bank.append(bass4_Erev)
# C3 G2 D2 A1
bass4_Ast_note_symbols = ['C', 'G', 'D', 'A']
bass4_Ast_pitch_values = [48, 43, 38, 33]
bass4_Ast = (bass4_Ast_note_symbols, bass4_Ast_pitch_values)
pitch_pattern_bank.append(bass4_Ast)
# C3 G2 D2 A1 rev
bass4_Arev_note_symbols = ['A' ,'D', 'G','C']
bass4_Arev_pitch_values = [33, 38, 43, 48]
bass4_Arev = (bass4_Arev_note_symbols, bass4_Arev_pitch_values)
pitch_pattern_bank.append(bass4_Arev)
# G2 D2 A1 A0
bass4_doubleA_note_symbols = ['G', 'D', 'A', 'A']
bass4_doubleA_pitch_values = [43, 38, 33, 21]
bass4_doubleA = (bass4_doubleA_note_symbols, bass4_doubleA_pitch_values)
pitch_pattern_bank.append(bass4_doubleA)
# F2 C2 G1 D1
bass4_Dst_note_symbols = ['F', 'C', 'G', 'D']
bass4_Dst_pitch_values = [41, 36, 31, 26]
bass4_Dst = (bass4_Dst_note_symbols, bass4_Dst_pitch_values)
pitch_pattern_bank.append(bass4_Dst)
# F2 C2 G1 C1
bass4_dropC_note_symbols = ['F', 'C', 'G', 'C']
bass4_dropC_pitch_values = [41, 36, 31, 24]
bass4_dropC = (bass4_dropC_note_symbols, bass4_dropC_pitch_values)
pitch_pattern_bank.append(bass4_dropC)
# C2 F2 A1 C1
bass4_CFAC_note_symbols = ['C', 'F', 'A', 'C']
bass4_CFAC_pitch_values = [36, 29, 33, 24]
bass4_CFAC = (bass4_CFAC_note_symbols, bass4_CFAC_pitch_values)
pitch_pattern_bank.append(bass4_CFAC)
# G2 D2 A1 D1
bass4_dropD_note_symbols = ['G', 'D', 'A', 'D']
bass4_dropD_pitch_values = [43, 38, 33, 26]
bass4_dropD = (bass4_dropD_note_symbols, bass4_dropD_pitch_values)
pitch_pattern_bank.append(bass4_dropD)
# G2 D2 A1 E1 A0
bass5_dropA_note_symbols = bass4_note_symbols + ['A']
bass5_dropA_pitch_values = bass4_pitch_values + [21]
bass5_dropA = (bass5_dropA_note_symbols, bass5_dropA_pitch_values)
pitch_pattern_bank.append(bass5_dropA)
# G2 D2 A1 E1 B0
bass5_note_symbols = bass4_note_symbols + ['B']
bass5_pitch_values = bass4_pitch_values + [23]
bass5 = (bass5_note_symbols, bass5_pitch_values)
pitch_pattern_bank.append(bass5)
# F2 C2 G1 D1 A0
bass5_Dst_note_symbols = bass4_Dst_note_symbols + ['A']
bass5_Dst_pitch_values = bass4_Dst_pitch_values + [21]
bass5_Dst = (bass5_Dst_note_symbols, bass5_Dst_pitch_values)
pitch_pattern_bank.append(bass5_Dst)
# C3 G2 D2 A1 E1 B0
bass6_note_symbols = ['C'] + bass5_note_symbols
bass6_pitch_values = [48] + bass5_pitch_values
bass6 = (bass6_note_symbols, bass6_pitch_values)
pitch_pattern_bank.append(bass6)


# == DRUMS ==

# C C C C C C
drums_note_symbols = ['C', 'C', 'C', 'C', 'C', 'C']
drums_pitch_values = [0, 0, 0, 0, 0, 0]
drums = (drums_note_symbols, drums_pitch_values)
pitch_pattern_bank.append(drums)


# == OTHER ==
other1_note_symbols = ['E', 'A', 'A', 'E', 'E', 'A']
other1_pitch_values = [64, 57, 57, 52, 40, 33]
other1 = (other1_note_symbols, other1_pitch_values)
pitch_pattern_bank.append(other1)

