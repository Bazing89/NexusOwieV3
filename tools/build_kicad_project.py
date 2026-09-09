from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ESP8266-12_KiCad"
OUT.mkdir(parents=True, exist_ok=True)


CUSTOM_LIB = r'''EESchema-LIBRARY Version 2.4
#encoding utf-8
#
# R
#
DEF R R 0 0 N Y 1 F N
F0 "R" 80 50 50 H V L CNN
F1 "R" 80 -50 50 H V L CNN
DRAW
S -40 60 40 -60 0 1 10 N
X ~ 1 0 100 40 D 30 30 1 1 P
X ~ 2 0 -100 40 U 30 30 1 1 P
ENDDRAW
ENDDEF
#
# C
#
DEF C C 0 0 N Y 1 F N
F0 "C" 80 50 50 H V L CNN
F1 "C" 80 -50 50 H V L CNN
DRAW
P 2 0 1 12 -70 20 70 20
P 2 0 1 12 -70 -20 70 -20
X ~ 1 0 100 80 D 30 30 1 1 P
X ~ 2 0 -100 80 U 30 30 1 1 P
ENDDRAW
ENDDEF
#
# LED
#
DEF LED D 0 0 N Y 1 F N
F0 "D" 100 50 50 H V L CNN
F1 "LED" 100 -50 50 H V L CNN
DRAW
P 3 0 1 10 -60 40 60 0 -60 -40 F
P 2 0 1 10 60 50 60 -50
P 2 0 1 8 80 60 130 110
P 2 0 1 8 105 35 155 85
X K 1 0 -100 50 U 30 30 1 1 P
X A 2 0 100 50 D 30 30 1 1 P
ENDDRAW
ENDDEF
#
# SW_PUSH
#
DEF SW_PUSH SW 0 0 N Y 1 F N
F0 "SW" 0 100 50 H V C CNN
F1 "SW_PUSH" 0 -100 50 H V C CNN
DRAW
C -60 0 15 0 1 10 N
C 60 0 15 0 1 10 N
P 2 0 1 10 -45 15 45 65
X ~ 1 -150 0 75 R 30 30 1 1 P
X ~ 2 150 0 75 L 30 30 1 1 P
ENDDRAW
ENDDEF
#
# NPN_SOT23
#
DEF NPN_SOT23 Q 0 0 N Y 1 F N
F0 "Q" 150 100 50 H V L CNN
F1 "MMBT3904" 150 0 50 H V L CNN
DRAW
C 0 0 120 0 1 10 N
P 2 0 1 10 -80 0 0 0
P 2 0 1 10 0 -60 60 -120
P 2 0 1 10 0 60 60 120
P 3 0 1 10 35 -105 60 -120 45 -90 F
X B 1 -200 0 120 R 30 30 1 1 I
X E 2 100 -200 100 U 30 30 1 1 P
X C 3 100 200 100 D 30 30 1 1 P
ENDDRAW
ENDDEF
#
# LDO5
#
DEF LDO5 U 0 0 Y Y 1 F N
F0 "U" 0 350 50 H V C CNN
F1 "LDO (value not shown in PDF)" 0 -350 50 H V C CNN
DRAW
S -300 250 300 -250 0 1 10 f
X VIN 1 -500 150 200 R 40 40 1 1 W
X VSS 2 -500 0 200 R 40 40 1 1 W
X EN 3 -500 -150 200 R 40 40 1 1 I
X NC 4 500 -150 200 L 40 40 1 1 N
X VOUT 5 500 150 200 L 40 40 1 1 w
ENDDRAW
ENDDEF
#
# USB_C_16
#
DEF USB_C_16 J 0 0 Y Y 1 F N
F0 "J" 0 1100 50 H V C CNN
F1 "TYPE-C-31-M-31" 0 -1100 50 H V C CNN
DRAW
S -500 1000 500 -1000 0 1 10 f
X MP1 MP1 -700 750 200 R 35 35 1 1 P
X MP2 MP2 -700 500 200 R 35 35 1 1 P
X MP3 MP3 -700 250 200 R 35 35 1 1 P
X MP4 MP4 -700 0 200 R 35 35 1 1 P
X GND A1B12 -700 -400 200 R 35 35 1 1 W
X GND B1A12 -700 -700 200 R 35 35 1 1 W
X VBUS A4B9 700 800 200 L 35 35 1 1 W
X VBUS B4A9 700 600 200 L 35 35 1 1 W
X CC1 A5 700 400 200 L 35 35 1 1 B
X CC2 B5 700 200 200 L 35 35 1 1 B
X DP2 B6 700 0 200 L 35 35 1 1 B
X DP1 A6 700 -200 200 L 35 35 1 1 B
X DN2 B7 700 -400 200 L 35 35 1 1 B
X DN1 A7 700 -600 200 L 35 35 1 1 B
X SBU1 A8 700 -800 200 L 35 35 1 1 B
X SBU2 B8 700 -950 200 L 35 35 1 1 B
ENDDRAW
ENDDEF
#
# CH9102X
#
DEF CH9102X U 0 0 Y Y 1 F N
F0 "U" 0 1000 50 H V C CNN
F1 "CH9102X\nQFN-28_5x5" 0 -1250 50 H V C CNN
DRAW
S -600 900 600 -900 0 1 10 f
X GND 0 -800 700 200 R 35 35 1 1 W
X DCD 1 -800 500 200 R 35 35 1 1 I
X RI 2 -800 300 200 R 35 35 1 1 I
X GND 3 -800 100 200 R 35 35 1 1 W
X UD+ 4 -800 -100 200 R 35 35 1 1 B
X UD- 5 -800 -300 200 R 35 35 1 1 B
X V3 6 -800 -500 200 R 35 35 1 1 w
X VDD5 7 -800 -700 200 R 35 35 1 1 W
X VBUS 8 -600 -1100 200 U 35 35 1 1 W
X RTS# 9 -400 -1100 200 U 35 35 1 1 O
X ACT# 10 -200 -1100 200 U 35 35 1 1 O
X SUSPEND# 11 0 -1100 200 U 35 35 1 1 O
X SUSPEND 12 200 -1100 200 U 35 35 1 1 O
X NC 13 400 -1100 200 U 35 35 1 1 N
X NC 14 600 -1100 200 U 35 35 1 1 N
X NC 15 800 -700 200 L 35 35 1 1 N
X WAKEUP/GPIO3 16 800 -500 200 L 35 35 1 1 B
X TNOW/GPIO2 17 800 -300 200 L 35 35 1 1 B
X RXS/GPIO1 18 800 -100 200 L 35 35 1 1 B
X TXS/GPIO0 19 800 100 200 L 35 35 1 1 B
X GPIO6 20 800 300 200 L 35 35 1 1 B
X GPIO5 21 800 500 200 L 35 35 1 1 B
X 3V 22 -600 1100 200 D 35 35 1 1 w
X CTS 23 -400 1100 200 D 35 35 1 1 I
X RTS 24 -200 1100 200 D 35 35 1 1 O
X RXD 25 0 1100 200 D 35 35 1 1 I
X TXD 26 200 1100 200 D 35 35 1 1 O
X DSR 27 400 1100 200 D 35 35 1 1 I
X DTR 28 600 1100 200 D 35 35 1 1 O
ENDDRAW
ENDDEF
#
# ESP12F
#
DEF ESP12F U 0 0 Y Y 1 F N
F0 "U" 0 950 50 H V C CNN
F1 "ESP-12F(ESP8266MOD)" 0 -1150 50 H V C CNN
DRAW
S -550 800 550 -800 0 1 10 f
X RST 1 -750 700 200 R 35 35 1 1 I
X ADC 2 -750 500 200 R 35 35 1 1 I
X EN 3 -750 300 200 R 35 35 1 1 I
X IO16 4 -750 100 200 R 35 35 1 1 B
X IO14 5 -750 -100 200 R 35 35 1 1 B
X IO12 6 -750 -300 200 R 35 35 1 1 B
X IO13 7 -750 -500 200 R 35 35 1 1 B
X VCC 8 -750 -700 200 R 35 35 1 1 W
X CS0 9 -500 -1000 200 U 35 35 1 1 B
X MISO 10 -300 -1000 200 U 35 35 1 1 B
X IO9 11 -100 -1000 200 U 35 35 1 1 B
X IO10 12 100 -1000 200 U 35 35 1 1 B
X MOSI 13 300 -1000 200 U 35 35 1 1 B
X SCLK 14 500 -1000 200 U 35 35 1 1 B
X GND 15 750 -700 200 L 35 35 1 1 W
X IO15 16 750 -500 200 L 35 35 1 1 B
X IO2 17 750 -300 200 L 35 35 1 1 B
X IO0 18 750 -100 200 L 35 35 1 1 B
X IO4 19 750 100 200 L 35 35 1 1 B
X IO5 20 750 300 200 L 35 35 1 1 B
X RXD 21 750 500 200 L 35 35 1 1 I
X TXD 22 750 700 200 L 35 35 1 1 O
ENDDRAW
ENDDEF
#
# CONN3
#
DEF CONN3 J 0 0 Y Y 1 F N
F0 "J" 0 300 50 H V C CNN
F1 "CONN3" 0 -300 50 H V C CNN
DRAW
S -150 200 150 -200 0 1 10 f
X 1 1 -350 120 200 R 35 35 1 1 P
X 2 2 -350 0 200 R 35 35 1 1 P
X 3 3 -350 -120 200 R 35 35 1 1 P
ENDDRAW
ENDDEF
#
# CONN6_SH
#
DEF CONN6_SH J 0 0 Y Y 1 F N
F0 "J" 0 500 50 H V C CNN
F1 "CONN6_SH" 0 -650 50 H V C CNN
DRAW
S -150 420 150 -420 0 1 10 f
X 1 1 -350 300 200 R 35 35 1 1 P
X 2 2 -350 180 200 R 35 35 1 1 P
X 3 3 -350 60 200 R 35 35 1 1 P
X 4 4 -350 -60 200 R 35 35 1 1 P
X 5 5 -350 -180 200 R 35 35 1 1 P
X 6 6 -350 -300 200 R 35 35 1 1 P
X SHIELD S1 350 -180 200 L 35 35 1 1 P
X SHIELD S2 350 -300 200 L 35 35 1 1 P
ENDDRAW
ENDDEF
#End Library
'''


def comp(lib_id, ref, value, x, y, footprint="", orient=(1, 0, 0, -1)):
    uid = f"{abs(hash((ref, x, y))) & 0xFFFFFFFF:08X}"
    return [
        "$Comp", f"L {lib_id} {ref}", f"U 1 1 {uid}", f"P {x} {y}",
        f'F 0 "{ref}" H {x+100} {y-100} 50  0000 L CNN',
        f'F 1 "{value}" H {x+100} {y+100} 50  0000 L CNN',
        f'F 2 "{footprint}" H {x} {y} 50  0001 C CNN',
        f'F 3 "" H {x} {y} 50  0001 C CNN',
        f"\t1    {x} {y}", f"\t{orient[0]}    {orient[1]}    {orient[2]}    {orient[3]}", "$EndComp"
    ]


def label(name, x, y, orient=0):
    return [f"Text Label {x} {y} {orient}    50   ~ 0", name]


def wire(x1, y1, x2, y2):
    return ["Wire Wire Line", f"\t{x1} {y1} {x2} {y2}"]


def nocon(x, y):
    return [f"NoConn ~ {x} {y}"]


def note(text, x, y, size=80):
    return [f"Text Notes {x} {y} 0    {size}   ~ 12", text]


sch = [
    "EESchema Schematic File Version 4", "LIBS:owie_custom", "EELAYER 29 0", "EELAYER END",
    "$Descr A3 16535 11693", "Sheet 1 1", 'Title "ESP8266-12 Tested Schematic Recreation"',
    'Date "2026-09-07"', 'Rev "PDF recreation"', 'Comp "Recreated without intentional circuit changes"',
    'Comment1 "Source: Schematic_ESP8266-12.SchDoc_2026-09-07.pdf"',
    'Comment2 "PDF lacks native netlist and some exact library/footprint metadata"',
    'Comment3 "Verify against original Altium source before fabrication"', 'Comment4 ""', "$EndDescr"
]

# USB-C power and data section
sch += note("USB-C POWER AND DATA", 900, 650, 100)
sch += comp("owie_custom:USB_C_16", "J1", "TYPE-C-31-M-31", 1900, 1800, "")
for yy in (1050, 1300, 1550, 1800, 2200, 2500):
    sch += label("GND", 1200, yy)
sch += label("VSYS", 2600, 1000); sch += label("VSYS", 2600, 1200)
sch += label("CC1", 2600, 1400); sch += label("CC2", 2600, 1600)
sch += label("USB_P", 2600, 1800); sch += label("USB_P", 2600, 2000)
sch += label("USB_N", 2600, 2200); sch += label("USB_N", 2600, 2400)
sch += label("GND", 2600, 2600); sch += label("GND", 2600, 2750)

for ref, net, x in (("R3", "CC1", 3300), ("R4", "CC2", 3900)):
    sch += comp("owie_custom:R", ref, "5.1k 1% 0402", x, 1700, "Resistor_SMD:R_0402_1005Metric")
    sch += wire(x, 1600, x, 1500); sch += label(net, x, 1500)
    sch += wire(x, 1800, x, 1900); sch += label("GND", x, 1900)
for ref, val, x in (("C2", "10uF 10V X7R 0402", 4600), ("C3", "100nF 16V X7R 0402", 5200)):
    sch += comp("owie_custom:C", ref, val, x, 1500, "Capacitor_SMD:C_0402_1005Metric")
    sch += wire(x, 1400, x, 1300); sch += label("VSYS", x, 1300)
    sch += wire(x, 1600, x, 1700); sch += label("GND", x, 1700)

# LDO and LED
sch += note("LDO 5V TO 3.3V", 6500, 650, 100)
sch += comp("owie_custom:LDO5", "U2", "LDO (value not shown in PDF)", 7600, 1500, "Package_TO_SOT_SMD:SOT-23-5")
sch += label("VSYS", 7100, 1350); sch += label("GND", 7100, 1500); sch += label("EN_LDO", 7100, 1650)
sch += label("3.3V", 8100, 1350); sch += nocon(8100, 1650)
for ref, val, net, x, fp in (
    ("C1", "4.7uF 25V X5R 0603", "VSYS", 6100, "Capacitor_SMD:C_0603_1608Metric"),
    ("C4", "1uF 25V X5R 0603", "VSYS", 6600, "Capacitor_SMD:C_0603_1608Metric"),
    ("C5", "4.7uF 25V X5R 0603", "3.3V", 8600, "Capacitor_SMD:C_0603_1608Metric"),
    ("C6", "1uF 25V X5R 0603", "3.3V", 9100, "Capacitor_SMD:C_0603_1608Metric"),
):
    sch += comp("owie_custom:C", ref, val, x, 1500, fp)
    sch += wire(x, 1400, x, 1300); sch += label(net, x, 1300)
    sch += wire(x, 1600, x, 1700); sch += label("GND", x, 1700)
sch += comp("owie_custom:R", "R14", "10K 0402", 7000, 2100, "Resistor_SMD:R_0402_1005Metric")
sch += wire(7000, 2000, 7000, 1900); sch += label("VSYS", 7000, 1900)
sch += wire(7000, 2200, 7000, 2300); sch += label("EN_LDO", 7000, 2300)
sch += comp("owie_custom:R", "R1", "1K 0402", 10500, 1300, "Resistor_SMD:R_0402_1005Metric")
sch += wire(10500, 1200, 10500, 1100); sch += label("3.3V", 10500, 1100)
sch += comp("owie_custom:LED", "D1", "LED 0402", 10500, 1700, "LED_SMD:LED_0402_1005Metric")
sch += wire(10500, 1400, 10500, 1600); sch += wire(10500, 1800, 10500, 1900); sch += label("GND", 10500, 1900)

# USB-UART bridge
sch += note("USB TO UART SECTION", 900, 3300, 100)
sch += comp("owie_custom:CH9102X", "U3", "CH9102X QFN-28_5x5", 2700, 4700, "Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.1x3.1mm")
# left pins 0..7
for net, yy in (("GND",4000),(None,4200),(None,4400),("GND",4600),("USB_P",4800),("USB_N",5000),("3.3V",5200),("VSYS",5400)):
    if net: sch += label(net, 1900, yy)
    else: sch += nocon(1900, yy)
# bottom pins 8..14
sch += label("VSYS", 2100, 5800)
for xx in (2300,2500,2700,3100,3300): sch += nocon(xx, 5800)
sch += nocon(2900, 5800)  # pin 12 SUSPEND is NC in source
# right pins 15..21
for yy in (5400,5200,5000,4800,4600,4400,4200): sch += nocon(3500, yy)
# top 22..28
sch += label("3.3V", 2100, 3600); sch += nocon(2300, 3600)
sch += label("RTS", 2500, 3600); sch += label("RXD0", 2700, 3600); sch += label("TXD0", 2900, 3600)
sch += nocon(3100, 3600); sch += label("DTR", 3300, 3600)
sch += comp("owie_custom:C", "C7", "100nF 25V X7R 0402", 1500, 5200, "Capacitor_SMD:C_0402_1005Metric")
sch += wire(1500,5100,1500,5000); sch += label("3.3V",1500,5000); sch += wire(1500,5300,1500,5400); sch += label("GND",1500,5400)
sch += comp("owie_custom:C", "C8", "100nF 25V X7R 0402", 1500, 5800, "Capacitor_SMD:C_0402_1005Metric")
sch += wire(1500,5700,1500,5600); sch += label("VSYS",1500,5600); sch += wire(1500,5900,1500,6000); sch += label("GND",1500,6000)

# Auto-programming transistor network
sch += note("AUTO-PROGRAM RESET / BOOT", 4300, 3300, 90)
sch += comp("owie_custom:R", "R6", "10K 0402", 4700, 4100, "Resistor_SMD:R_0402_1005Metric", (0,-1,-1,0))
sch += wire(4600,4100,4400,4100); sch += label("DTR",4400,4100)
sch += comp("owie_custom:NPN_SOT23", "Q1", "MMBT3904 SOT23-3", 5400, 4100, "Package_TO_SOT_SMD:SOT-23")
sch += wire(4800,4100,5200,4100); sch += label("RTS",5500,4300); sch += label("RST",5500,3900)
sch += comp("owie_custom:R", "R8", "10K 0402", 4700, 5000, "Resistor_SMD:R_0402_1005Metric", (0,-1,-1,0))
sch += wire(4600,5000,4400,5000); sch += label("RTS",4400,5000)
sch += comp("owie_custom:NPN_SOT23", "Q2", "MMBT3904 SOT23-3", 5400, 5000, "Package_TO_SOT_SMD:SOT-23")
sch += wire(4800,5000,5200,5000); sch += label("DTR",5500,5200); sch += label("IO0",5500,4800)

# Boot straps and pullups
sch += note("BOOT STRAPS", 6800, 3300, 90)
for ref, net, x in (("R7","EN",7000),("R9","RST",7900),("R10","IO0",8800),("R11","IO2",9700)):
    sch += comp("owie_custom:R", ref, "10K 0402", x, 4100, "Resistor_SMD:R_0402_1005Metric")
    sch += wire(x,4000,x,3900); sch += label("3.3V",x,3900)
    sch += wire(x,4200,x,4300); sch += label(net,x,4300)
sch += comp("owie_custom:C", "C15", "100nF 16V X7R 0402", 7000, 4700, "Capacitor_SMD:C_0402_1005Metric")
sch += wire(7000,4600,7000,4500); sch += label("EN",7000,4500); sch += wire(7000,4800,7000,4900); sch += label("GND",7000,4900)
sch += comp("owie_custom:R", "R13", "0R 0402 - DNP", 8800, 4700, "Resistor_SMD:R_0402_1005Metric")
sch += wire(8800,4600,8800,4500); sch += label("IO0",8800,4500); sch += wire(8800,4800,8800,4900); sch += label("GND",8800,4900)
sch += note("DONT PLACE", 8950, 4725, 55)
sch += comp("owie_custom:R", "R12", "10K 0402", 10600, 4700, "Resistor_SMD:R_0402_1005Metric")
sch += wire(10600,4600,10600,4500); sch += label("IO15",10600,4500); sch += wire(10600,4800,10600,4900); sch += label("GND",10600,4900)

# ESP module
sch += note("ESP8266 MODULE", 900, 6500, 100)
sch += comp("owie_custom:ESP12F", "U1", "ESP-12F(ESP8266MOD) SMD-22", 2600, 7800, "RF_Module:ESP-12E")
for net, yy in (("RST",7100),(None,7300),("EN",7500),("D0",7700),(None,7900),(None,8100),(None,8300),("3.3V",8500)):
    if net: sch += label(net,1850,yy)
    else: sch += nocon(1850,yy)
for xx in (2100,2300,2500,2700,2900,3100): sch += nocon(xx,8800)
for net, yy in (("GND",8500),("IO15",8300),("IO2",8100),("IO0",7900),("TXD0",7700),("GREEN",7500),("RXD0",7300),("TXD0",7100)):
    sch += label(net,3350,yy)
sch += note("Pin 19 (IO4) is tied to TXD0 exactly as drawn in source PDF", 3450, 7775, 45)

# Optional self-wake link and buttons
sch += comp("owie_custom:R", "R5", "0R 0402 - OPTIONAL", 5200, 8800, "Resistor_SMD:R_0402_1005Metric", (0,-1,-1,0))
sch += wire(5100,8800,4900,8800); sch += label("D0",4900,8800); sch += wire(5300,8800,5500,8800); sch += label("RST",5500,8800)
sch += note("self wake from deep sleep (optional)", 4550, 8500, 65)
sch += note("R5 is only soldered if self-wake from deep sleep is desired", 4550, 9000, 45)
for ref, net, x in (("SW1","RST",1600),("SW2","IO0",3100)):
    sch += comp("owie_custom:SW_PUSH", ref, "TS1185A16020 SMD,4x3mm", x, 9800, "")
    sch += label("GND",x-150,9800); sch += label(net,x+150,9800)

# Input/output connectors
sch += note("INPUT", 9000, 6500, 110)
sch += comp("owie_custom:CONN3", "J3", "SM03B-GHS-TB(LF)(SN) SMD", 9200, 7200, "Connector_JST:JST_GH_SM03B-GHS-TB_1x03-1MP_P1.25mm_Horizontal")
for net, yy in (("GND",7080),("SIGNAL",7200),("VSYS",7320)): sch += label(net,8850,yy)
sch += comp("owie_custom:CONN6_SH", "J2", "SM06B-GHS-TB(LF)(SN) SMD", 12400, 7200, "Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal")
for net, yy in (("ORANGE",6900),("YELLOW",7020),("BLUE",7140),("BLACK",7260),("WHITE_IN",7380)):
    sch += label(net,12050,yy)
sch += nocon(12050,7500); sch += label("GND",12750,7380); sch += label("GND",12750,7500)
sch += note("OUTPUT", 9000, 8600, 110)
sch += comp("owie_custom:CONN3", "J5", "SM03B-GHS-TB(LF)(SN) SMD", 9200, 9300, "Connector_JST:JST_GH_SM03B-GHS-TB_1x03-1MP_P1.25mm_Horizontal")
for net, yy in (("VSYS",9180),("SIGNAL",9300),("GND",9420)): sch += label(net,8850,yy)
sch += comp("owie_custom:CONN6_SH", "J4", "SM06B-GHS-TB(LF)(SN) SMD", 12400, 9300, "Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal")
for net, yy in (("GREEN",9000),("WHITE_OUT",9120),("BLACK",9240),("BLUE",9360),("YELLOW",9480),("ORANGE",9600)):
    sch += label(net,12050,yy)
sch += label("GND",12750,9480); sch += label("GND",12750,9600)

sch += note("RECREATION NOTE: Circuit topology follows the supplied tested PDF. Native Altium source is needed to recover exact hidden metadata and remove remaining footprint uncertainty.", 900, 10800, 55)
sch += ["$EndSCHEMATC"]

(OUT / "owie_custom.lib").write_text(CUSTOM_LIB, encoding="utf-8", newline="\n")
(OUT / "sym-lib-table").write_text('(sym_lib_table\n  (lib (name "owie_custom")(type "Legacy")(uri "${KIPRJMOD}/owie_custom.lib")(options "")(descr "Symbols recreated from supplied PDF"))\n)\n', encoding="utf-8")
(OUT / "ESP8266-12.sch").write_text("\n".join(sch) + "\n", encoding="utf-8", newline="\n")
(OUT / "ESP8266-12.pro").write_text("update=2026-09-07\nlast_client=eeschema\n", encoding="utf-8", newline="\n")
(OUT / "ESP8266-12.kicad_pro").write_text("{}\n", encoding="utf-8", newline="\n")
(OUT / "README.md").write_text("""# ESP8266-12 KiCad project

This schematic is a faithful manual recreation of the supplied tested PDF. No intentional circuit changes were made.

## Important source limitation

The PDF contains the visible drawing but not Altium's native electrical netlist, component parameters, hidden pin mappings, exact library links, PCB placement/routing, or every exact footprint identifier. The project therefore preserves the visible topology and uses custom symbols plus footprints only where the PDF identifies the package clearly.

Before fabrication, compare against the original Altium `.SchDoc`/project and run a human schematic review. The original Altium source is strongly recommended for lossless conversion and is required to reproduce the PCB.

Open `ESP8266-12.kicad_sch` in KiCad 10 or later.
""", encoding="utf-8", newline="\n")
print(OUT)
