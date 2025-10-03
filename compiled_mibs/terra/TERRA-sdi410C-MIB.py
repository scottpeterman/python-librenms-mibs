# SNMP MIB module (TERRA-sdi410C-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\terra\TERRA-sdi410C-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:14 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(DefStatus,) = mibBuilder.importSymbols(
    "TERRA-DEFINITIONS-MIB",
    "DefStatus")

(terraProducts,) = mibBuilder.importSymbols(
    "TERRA-PRODUCTS-MIB",
    "terraProducts")


# MODULE-IDENTITY

terra_sdi410C = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8)
)
if mibBuilder.loadTexts:
    terra_sdi410C.setRevisions(
        ("2017-10-09 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sdi410cstatus_ObjectIdentity = ObjectIdentity
sdi410cstatus = _Sdi410cstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1)
)
_MainStatus_ObjectIdentity = ObjectIdentity
mainStatus = _MainStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 1)
)
_InBR_Type = Integer32
_InBR_Object = MibScalar
inBR = _InBR_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 1, 1),
    _InBR_Type()
)
inBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBR.setStatus("current")
if mibBuilder.loadTexts:
    inBR.setUnits("kbps")
_OutBR_Type = Integer32
_OutBR_Object = MibScalar
outBR = _OutBR_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 1, 2),
    _OutBR_Type()
)
outBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBR.setStatus("current")
if mibBuilder.loadTexts:
    outBR.setUnits("kbps")
_Load_Type = Integer32
_Load_Object = MibScalar
load = _Load_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 1, 3),
    _Load_Type()
)
load.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    load.setStatus("current")
if mibBuilder.loadTexts:
    load.setUnits("percents")
_Temp_Type = Integer32
_Temp_Object = MibScalar
temp = _Temp_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 1, 4),
    _Temp_Type()
)
temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp.setStatus("current")
if mibBuilder.loadTexts:
    temp.setUnits("deg C")
_Supply_Type = Integer32
_Supply_Object = MibScalar
supply = _Supply_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 1, 5),
    _Supply_Type()
)
supply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supply.setStatus("current")
if mibBuilder.loadTexts:
    supply.setUnits("volts V")
_OutStream1_ObjectIdentity = ObjectIdentity
outStream1 = _OutStream1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 2)
)
_OutBr1_Type = Integer32
_OutBr1_Object = MibScalar
outBr1 = _OutBr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 2, 1),
    _OutBr1_Type()
)
outBr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr1.setStatus("current")
if mibBuilder.loadTexts:
    outBr1.setUnits("kbps")
_OutStream2_ObjectIdentity = ObjectIdentity
outStream2 = _OutStream2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 3)
)
_OutBr2_Type = Integer32
_OutBr2_Object = MibScalar
outBr2 = _OutBr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 3, 1),
    _OutBr2_Type()
)
outBr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr2.setStatus("current")
if mibBuilder.loadTexts:
    outBr2.setUnits("kbps")
_OutStream3_ObjectIdentity = ObjectIdentity
outStream3 = _OutStream3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 4)
)
_OutBr3_Type = Integer32
_OutBr3_Object = MibScalar
outBr3 = _OutBr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 4, 1),
    _OutBr3_Type()
)
outBr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr3.setStatus("current")
if mibBuilder.loadTexts:
    outBr3.setUnits("kbps")
_OutStream4_ObjectIdentity = ObjectIdentity
outStream4 = _OutStream4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 5)
)
_OutBr4_Type = Integer32
_OutBr4_Object = MibScalar
outBr4 = _OutBr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 5, 1),
    _OutBr4_Type()
)
outBr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr4.setStatus("current")
if mibBuilder.loadTexts:
    outBr4.setUnits("kbps")
_OutStream5_ObjectIdentity = ObjectIdentity
outStream5 = _OutStream5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 6)
)
_OutBr5_Type = Integer32
_OutBr5_Object = MibScalar
outBr5 = _OutBr5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 6, 1),
    _OutBr5_Type()
)
outBr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr5.setStatus("current")
if mibBuilder.loadTexts:
    outBr5.setUnits("kbps")
_OutStream6_ObjectIdentity = ObjectIdentity
outStream6 = _OutStream6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 7)
)
_OutBr6_Type = Integer32
_OutBr6_Object = MibScalar
outBr6 = _OutBr6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 7, 1),
    _OutBr6_Type()
)
outBr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr6.setStatus("current")
if mibBuilder.loadTexts:
    outBr6.setUnits("kbps")
_OutStream7_ObjectIdentity = ObjectIdentity
outStream7 = _OutStream7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 8)
)
_OutBr7_Type = Integer32
_OutBr7_Object = MibScalar
outBr7 = _OutBr7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 8, 1),
    _OutBr7_Type()
)
outBr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr7.setStatus("current")
if mibBuilder.loadTexts:
    outBr7.setUnits("kbps")
_OutStream8_ObjectIdentity = ObjectIdentity
outStream8 = _OutStream8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 9)
)
_OutBr8_Type = Integer32
_OutBr8_Object = MibScalar
outBr8 = _OutBr8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 9, 1),
    _OutBr8_Type()
)
outBr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr8.setStatus("current")
if mibBuilder.loadTexts:
    outBr8.setUnits("kbps")
_OutStream9_ObjectIdentity = ObjectIdentity
outStream9 = _OutStream9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 10)
)
_OutBr9_Type = Integer32
_OutBr9_Object = MibScalar
outBr9 = _OutBr9_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 10, 1),
    _OutBr9_Type()
)
outBr9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr9.setStatus("current")
if mibBuilder.loadTexts:
    outBr9.setUnits("kbps")
_OutStream10_ObjectIdentity = ObjectIdentity
outStream10 = _OutStream10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 11)
)
_OutBr10_Type = Integer32
_OutBr10_Object = MibScalar
outBr10 = _OutBr10_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 11, 1),
    _OutBr10_Type()
)
outBr10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr10.setStatus("current")
if mibBuilder.loadTexts:
    outBr10.setUnits("kbps")
_OutStream11_ObjectIdentity = ObjectIdentity
outStream11 = _OutStream11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 12)
)
_OutBr11_Type = Integer32
_OutBr11_Object = MibScalar
outBr11 = _OutBr11_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 12, 1),
    _OutBr11_Type()
)
outBr11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr11.setStatus("current")
if mibBuilder.loadTexts:
    outBr11.setUnits("kbps")
_OutStream12_ObjectIdentity = ObjectIdentity
outStream12 = _OutStream12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 13)
)
_OutBr12_Type = Integer32
_OutBr12_Object = MibScalar
outBr12 = _OutBr12_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 13, 1),
    _OutBr12_Type()
)
outBr12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr12.setStatus("current")
if mibBuilder.loadTexts:
    outBr12.setUnits("kbps")
_OutStream13_ObjectIdentity = ObjectIdentity
outStream13 = _OutStream13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 14)
)
_OutBr13_Type = Integer32
_OutBr13_Object = MibScalar
outBr13 = _OutBr13_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 14, 1),
    _OutBr13_Type()
)
outBr13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr13.setStatus("current")
if mibBuilder.loadTexts:
    outBr13.setUnits("kbps")
_OutStream14_ObjectIdentity = ObjectIdentity
outStream14 = _OutStream14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 15)
)
_OutBr14_Type = Integer32
_OutBr14_Object = MibScalar
outBr14 = _OutBr14_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 15, 1),
    _OutBr14_Type()
)
outBr14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr14.setStatus("current")
if mibBuilder.loadTexts:
    outBr14.setUnits("kbps")
_OutStream15_ObjectIdentity = ObjectIdentity
outStream15 = _OutStream15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 16)
)
_OutBr15_Type = Integer32
_OutBr15_Object = MibScalar
outBr15 = _OutBr15_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 16, 1),
    _OutBr15_Type()
)
outBr15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr15.setStatus("current")
if mibBuilder.loadTexts:
    outBr15.setUnits("kbps")
_OutStream16_ObjectIdentity = ObjectIdentity
outStream16 = _OutStream16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 17)
)
_OutBr16_Type = Integer32
_OutBr16_Object = MibScalar
outBr16 = _OutBr16_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 17, 1),
    _OutBr16_Type()
)
outBr16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr16.setStatus("current")
if mibBuilder.loadTexts:
    outBr16.setUnits("kbps")
_OutStream17_ObjectIdentity = ObjectIdentity
outStream17 = _OutStream17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 18)
)
_OutBr17_Type = Integer32
_OutBr17_Object = MibScalar
outBr17 = _OutBr17_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 18, 1),
    _OutBr17_Type()
)
outBr17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr17.setStatus("current")
if mibBuilder.loadTexts:
    outBr17.setUnits("kbps")
_OutStream18_ObjectIdentity = ObjectIdentity
outStream18 = _OutStream18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 19)
)
_OutBr18_Type = Integer32
_OutBr18_Object = MibScalar
outBr18 = _OutBr18_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 19, 1),
    _OutBr18_Type()
)
outBr18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr18.setStatus("current")
if mibBuilder.loadTexts:
    outBr18.setUnits("kbps")
_OutStream19_ObjectIdentity = ObjectIdentity
outStream19 = _OutStream19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 20)
)
_OutBr19_Type = Integer32
_OutBr19_Object = MibScalar
outBr19 = _OutBr19_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 20, 1),
    _OutBr19_Type()
)
outBr19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr19.setStatus("current")
if mibBuilder.loadTexts:
    outBr19.setUnits("kbps")
_OutStream20_ObjectIdentity = ObjectIdentity
outStream20 = _OutStream20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 21)
)
_OutBr20_Type = Integer32
_OutBr20_Object = MibScalar
outBr20 = _OutBr20_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 21, 1),
    _OutBr20_Type()
)
outBr20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr20.setStatus("current")
if mibBuilder.loadTexts:
    outBr20.setUnits("kbps")
_OutStream21_ObjectIdentity = ObjectIdentity
outStream21 = _OutStream21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 22)
)
_OutBr21_Type = Integer32
_OutBr21_Object = MibScalar
outBr21 = _OutBr21_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 22, 1),
    _OutBr21_Type()
)
outBr21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr21.setStatus("current")
if mibBuilder.loadTexts:
    outBr21.setUnits("kbps")
_OutStream22_ObjectIdentity = ObjectIdentity
outStream22 = _OutStream22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 23)
)
_OutBr22_Type = Integer32
_OutBr22_Object = MibScalar
outBr22 = _OutBr22_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 23, 1),
    _OutBr22_Type()
)
outBr22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr22.setStatus("current")
if mibBuilder.loadTexts:
    outBr22.setUnits("kbps")
_OutStream23_ObjectIdentity = ObjectIdentity
outStream23 = _OutStream23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 24)
)
_OutBr23_Type = Integer32
_OutBr23_Object = MibScalar
outBr23 = _OutBr23_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 24, 1),
    _OutBr23_Type()
)
outBr23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr23.setStatus("current")
if mibBuilder.loadTexts:
    outBr23.setUnits("kbps")
_OutStream24_ObjectIdentity = ObjectIdentity
outStream24 = _OutStream24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 25)
)
_OutBr24_Type = Integer32
_OutBr24_Object = MibScalar
outBr24 = _OutBr24_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 25, 1),
    _OutBr24_Type()
)
outBr24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr24.setStatus("current")
if mibBuilder.loadTexts:
    outBr24.setUnits("kbps")
_OutStream25_ObjectIdentity = ObjectIdentity
outStream25 = _OutStream25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 26)
)
_OutBr25_Type = Integer32
_OutBr25_Object = MibScalar
outBr25 = _OutBr25_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 26, 1),
    _OutBr25_Type()
)
outBr25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr25.setStatus("current")
if mibBuilder.loadTexts:
    outBr25.setUnits("kbps")
_InputStatus_ObjectIdentity = ObjectIdentity
inputStatus = _InputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27)
)
_Lock_Type = DisplayString
_Lock_Object = MibScalar
lock = _Lock_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 1),
    _Lock_Type()
)
lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lock.setStatus("current")
_Std_Type = DisplayString
_Std_Object = MibScalar
std = _Std_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 2),
    _Std_Type()
)
std.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    std.setStatus("current")
_Level_Type = DisplayString
_Level_Object = MibScalar
level = _Level_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 3),
    _Level_Type()
)
level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    level.setStatus("current")
if mibBuilder.loadTexts:
    level.setUnits("dbuV")
_Mod_Type = DisplayString
_Mod_Object = MibScalar
mod = _Mod_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 4),
    _Mod_Type()
)
mod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod.setStatus("current")
_Freq_Type = Integer32
_Freq_Object = MibScalar
freq = _Freq_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 5),
    _Freq_Type()
)
freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freq.setStatus("current")
if mibBuilder.loadTexts:
    freq.setUnits("MHz")
_Sr_Type = Integer32
_Sr_Object = MibScalar
sr = _Sr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 6),
    _Sr_Type()
)
sr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sr.setStatus("current")
if mibBuilder.loadTexts:
    sr.setUnits("Ks/s")
_Fec_Type = DisplayString
_Fec_Object = MibScalar
fec = _Fec_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 7),
    _Fec_Type()
)
fec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fec.setStatus("current")
_Snr_Type = Integer32
_Snr_Object = MibScalar
snr = _Snr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 8),
    _Snr_Type()
)
snr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snr.setStatus("current")
if mibBuilder.loadTexts:
    snr.setUnits("tenths of dB")
_Vber_Type = DisplayString
_Vber_Object = MibScalar
vber = _Vber_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 9),
    _Vber_Type()
)
vber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vber.setStatus("current")
_Per_Type = DisplayString
_Per_Object = MibScalar
per = _Per_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 10),
    _Per_Type()
)
per.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    per.setStatus("current")
_InCCerr_Type = Integer32
_InCCerr_Object = MibScalar
inCCerr = _InCCerr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 1, 27, 11),
    _InCCerr_Type()
)
inCCerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inCCerr.setStatus("current")
_Sdi410calarms_ObjectIdentity = ObjectIdentity
sdi410calarms = _Sdi410calarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2)
)
_AlarmCam_Type = DefStatus
_AlarmCam_Object = MibScalar
alarmCam = _AlarmCam_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 1),
    _AlarmCam_Type()
)
alarmCam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCam.setStatus("current")
_AlarmDesc_Type = DefStatus
_AlarmDesc_Object = MibScalar
alarmDesc = _AlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 2),
    _AlarmDesc_Type()
)
alarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDesc.setStatus("current")
_AlarmInpsig_Type = DefStatus
_AlarmInpsig_Object = MibScalar
alarmInpsig = _AlarmInpsig_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 3),
    _AlarmInpsig_Type()
)
alarmInpsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInpsig.setStatus("current")
_AlarmBitovf_Type = DefStatus
_AlarmBitovf_Object = MibScalar
alarmBitovf = _AlarmBitovf_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 4),
    _AlarmBitovf_Type()
)
alarmBitovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBitovf.setStatus("current")
_AlarmLinks_Type = DefStatus
_AlarmLinks_Object = MibScalar
alarmLinks = _AlarmLinks_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 5),
    _AlarmLinks_Type()
)
alarmLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLinks.setStatus("current")
_AlarmLinkc_Type = DefStatus
_AlarmLinkc_Object = MibScalar
alarmLinkc = _AlarmLinkc_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 6),
    _AlarmLinkc_Type()
)
alarmLinkc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLinkc.setStatus("current")
_AlarmPowovl_Type = DefStatus
_AlarmPowovl_Object = MibScalar
alarmPowovl = _AlarmPowovl_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 7),
    _AlarmPowovl_Type()
)
alarmPowovl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPowovl.setStatus("current")
_AlarmPowv_Type = DefStatus
_AlarmPowv_Object = MibScalar
alarmPowv = _AlarmPowv_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 8),
    _AlarmPowv_Type()
)
alarmPowv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPowv.setStatus("current")
_AlarmTemps_Type = DefStatus
_AlarmTemps_Object = MibScalar
alarmTemps = _AlarmTemps_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 9),
    _AlarmTemps_Type()
)
alarmTemps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTemps.setStatus("current")
_AlarmOvh_Type = DefStatus
_AlarmOvh_Object = MibScalar
alarmOvh = _AlarmOvh_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 10),
    _AlarmOvh_Type()
)
alarmOvh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOvh.setStatus("current")
_AlarmTsErr_Type = DefStatus
_AlarmTsErr_Object = MibScalar
alarmTsErr = _AlarmTsErr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 2, 11),
    _AlarmTsErr_Type()
)
alarmTsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTsErr.setStatus("current")
_Sdi410cnotifications_ObjectIdentity = ObjectIdentity
sdi410cnotifications = _Sdi410cnotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3)
)
_Sdi410cInfo_ObjectIdentity = ObjectIdentity
sdi410cInfo = _Sdi410cInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 4)
)
_InfVersion_Type = DisplayString
_InfVersion_Object = MibScalar
infVersion = _InfVersion_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 4, 1),
    _InfVersion_Type()
)
infVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infVersion.setStatus("current")
_InfSerNum_Type = DisplayString
_InfSerNum_Object = MibScalar
infSerNum = _InfSerNum_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 4, 2),
    _InfSerNum_Type()
)
infSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infSerNum.setStatus("current")
_Terrasdi410cMIBConformance_ObjectIdentity = ObjectIdentity
terrasdi410cMIBConformance = _Terrasdi410cMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 5)
)
_Terrasdi410cMIBGroups_ObjectIdentity = ObjectIdentity
terrasdi410cMIBGroups = _Terrasdi410cMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 5, 1)
)

# Managed Objects groups

sdi410cTerraMibAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 5, 1, 1)
)
sdi410cTerraMibAllObjects.setObjects(
      *(("TERRA-sdi410C-MIB", "inBR"),
        ("TERRA-sdi410C-MIB", "outBR"),
        ("TERRA-sdi410C-MIB", "load"),
        ("TERRA-sdi410C-MIB", "temp"),
        ("TERRA-sdi410C-MIB", "outBr1"),
        ("TERRA-sdi410C-MIB", "outBr2"),
        ("TERRA-sdi410C-MIB", "outBr3"),
        ("TERRA-sdi410C-MIB", "outBr4"),
        ("TERRA-sdi410C-MIB", "outBr5"),
        ("TERRA-sdi410C-MIB", "outBr6"),
        ("TERRA-sdi410C-MIB", "outBr7"),
        ("TERRA-sdi410C-MIB", "outBr8"),
        ("TERRA-sdi410C-MIB", "outBr9"),
        ("TERRA-sdi410C-MIB", "outBr10"),
        ("TERRA-sdi410C-MIB", "outBr11"),
        ("TERRA-sdi410C-MIB", "outBr12"),
        ("TERRA-sdi410C-MIB", "outBr13"),
        ("TERRA-sdi410C-MIB", "outBr14"),
        ("TERRA-sdi410C-MIB", "outBr15"),
        ("TERRA-sdi410C-MIB", "outBr16"),
        ("TERRA-sdi410C-MIB", "outBr17"),
        ("TERRA-sdi410C-MIB", "outBr18"),
        ("TERRA-sdi410C-MIB", "outBr19"),
        ("TERRA-sdi410C-MIB", "outBr20"),
        ("TERRA-sdi410C-MIB", "outBr21"),
        ("TERRA-sdi410C-MIB", "outBr22"),
        ("TERRA-sdi410C-MIB", "outBr23"),
        ("TERRA-sdi410C-MIB", "outBr24"),
        ("TERRA-sdi410C-MIB", "outBr25"),
        ("TERRA-sdi410C-MIB", "lock"),
        ("TERRA-sdi410C-MIB", "std"),
        ("TERRA-sdi410C-MIB", "level"),
        ("TERRA-sdi410C-MIB", "mod"),
        ("TERRA-sdi410C-MIB", "freq"),
        ("TERRA-sdi410C-MIB", "sr"),
        ("TERRA-sdi410C-MIB", "fec"),
        ("TERRA-sdi410C-MIB", "snr"),
        ("TERRA-sdi410C-MIB", "vber"),
        ("TERRA-sdi410C-MIB", "per"),
        ("TERRA-sdi410C-MIB", "inCCerr"),
        ("TERRA-sdi410C-MIB", "alarmCam"),
        ("TERRA-sdi410C-MIB", "alarmDesc"),
        ("TERRA-sdi410C-MIB", "alarmInpsig"),
        ("TERRA-sdi410C-MIB", "alarmBitovf"),
        ("TERRA-sdi410C-MIB", "alarmLinks"),
        ("TERRA-sdi410C-MIB", "alarmLinkc"),
        ("TERRA-sdi410C-MIB", "alarmPowovl"),
        ("TERRA-sdi410C-MIB", "alarmPowv"),
        ("TERRA-sdi410C-MIB", "alarmTemps"),
        ("TERRA-sdi410C-MIB", "alarmOvh"),
        ("TERRA-sdi410C-MIB", "alarmTsErr"),
        ("TERRA-sdi410C-MIB", "infVersion"),
        ("TERRA-sdi410C-MIB", "infSerNum"))
)
if mibBuilder.loadTexts:
    sdi410cTerraMibAllObjects.setStatus("current")


# Notification objects

notifyCam = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 1)
)
notifyCam.setObjects(
    ("TERRA-sdi410C-MIB", "alarmCam")
)
if mibBuilder.loadTexts:
    notifyCam.setStatus(
        "current"
    )

notifyDesc = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 2)
)
notifyDesc.setObjects(
    ("TERRA-sdi410C-MIB", "alarmDesc")
)
if mibBuilder.loadTexts:
    notifyDesc.setStatus(
        "current"
    )

notifyInpsig = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 3)
)
notifyInpsig.setObjects(
    ("TERRA-sdi410C-MIB", "alarmInpsig")
)
if mibBuilder.loadTexts:
    notifyInpsig.setStatus(
        "current"
    )

notifyBitovf = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 4)
)
notifyBitovf.setObjects(
    ("TERRA-sdi410C-MIB", "alarmBitovf")
)
if mibBuilder.loadTexts:
    notifyBitovf.setStatus(
        "current"
    )

notifyLinks = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 5)
)
notifyLinks.setObjects(
    ("TERRA-sdi410C-MIB", "alarmLinks")
)
if mibBuilder.loadTexts:
    notifyLinks.setStatus(
        "current"
    )

notifyLinkc = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 6)
)
notifyLinkc.setObjects(
    ("TERRA-sdi410C-MIB", "alarmLinkc")
)
if mibBuilder.loadTexts:
    notifyLinkc.setStatus(
        "current"
    )

notifyPowovl = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 7)
)
notifyPowovl.setObjects(
    ("TERRA-sdi410C-MIB", "alarmPowovl")
)
if mibBuilder.loadTexts:
    notifyPowovl.setStatus(
        "current"
    )

notifyPowv = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 8)
)
notifyPowv.setObjects(
    ("TERRA-sdi410C-MIB", "alarmPowv")
)
if mibBuilder.loadTexts:
    notifyPowv.setStatus(
        "current"
    )

notifyTemps = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 9)
)
notifyTemps.setObjects(
    ("TERRA-sdi410C-MIB", "alarmTemps")
)
if mibBuilder.loadTexts:
    notifyTemps.setStatus(
        "current"
    )

notifyOvh = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 10)
)
notifyOvh.setObjects(
    ("TERRA-sdi410C-MIB", "alarmOvh")
)
if mibBuilder.loadTexts:
    notifyOvh.setStatus(
        "current"
    )

notifyTsErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 3, 11)
)
notifyTsErr.setObjects(
    ("TERRA-sdi410C-MIB", "alarmTsErr")
)
if mibBuilder.loadTexts:
    notifyTsErr.setStatus(
        "current"
    )


# Notifications groups

sdi410cTerraMibAllNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30631, 1, 8, 5, 1, 2)
)
sdi410cTerraMibAllNotifications.setObjects(
      *(("TERRA-sdi410C-MIB", "notifyCam"),
        ("TERRA-sdi410C-MIB", "notifyDesc"),
        ("TERRA-sdi410C-MIB", "notifyInpsig"),
        ("TERRA-sdi410C-MIB", "notifyBitovf"),
        ("TERRA-sdi410C-MIB", "notifyLinks"),
        ("TERRA-sdi410C-MIB", "notifyLinkc"),
        ("TERRA-sdi410C-MIB", "notifyPowovl"),
        ("TERRA-sdi410C-MIB", "notifyPowv"),
        ("TERRA-sdi410C-MIB", "notifyTemps"),
        ("TERRA-sdi410C-MIB", "notifyOvh"),
        ("TERRA-sdi410C-MIB", "notifyTsErr"))
)
if mibBuilder.loadTexts:
    sdi410cTerraMibAllNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERRA-sdi410C-MIB",
    **{"terra-sdi410C": terra_sdi410C,
       "sdi410cstatus": sdi410cstatus,
       "mainStatus": mainStatus,
       "inBR": inBR,
       "outBR": outBR,
       "load": load,
       "temp": temp,
       "supply": supply,
       "outStream1": outStream1,
       "outBr1": outBr1,
       "outStream2": outStream2,
       "outBr2": outBr2,
       "outStream3": outStream3,
       "outBr3": outBr3,
       "outStream4": outStream4,
       "outBr4": outBr4,
       "outStream5": outStream5,
       "outBr5": outBr5,
       "outStream6": outStream6,
       "outBr6": outBr6,
       "outStream7": outStream7,
       "outBr7": outBr7,
       "outStream8": outStream8,
       "outBr8": outBr8,
       "outStream9": outStream9,
       "outBr9": outBr9,
       "outStream10": outStream10,
       "outBr10": outBr10,
       "outStream11": outStream11,
       "outBr11": outBr11,
       "outStream12": outStream12,
       "outBr12": outBr12,
       "outStream13": outStream13,
       "outBr13": outBr13,
       "outStream14": outStream14,
       "outBr14": outBr14,
       "outStream15": outStream15,
       "outBr15": outBr15,
       "outStream16": outStream16,
       "outBr16": outBr16,
       "outStream17": outStream17,
       "outBr17": outBr17,
       "outStream18": outStream18,
       "outBr18": outBr18,
       "outStream19": outStream19,
       "outBr19": outBr19,
       "outStream20": outStream20,
       "outBr20": outBr20,
       "outStream21": outStream21,
       "outBr21": outBr21,
       "outStream22": outStream22,
       "outBr22": outBr22,
       "outStream23": outStream23,
       "outBr23": outBr23,
       "outStream24": outStream24,
       "outBr24": outBr24,
       "outStream25": outStream25,
       "outBr25": outBr25,
       "inputStatus": inputStatus,
       "lock": lock,
       "std": std,
       "level": level,
       "mod": mod,
       "freq": freq,
       "sr": sr,
       "fec": fec,
       "snr": snr,
       "vber": vber,
       "per": per,
       "inCCerr": inCCerr,
       "sdi410calarms": sdi410calarms,
       "alarmCam": alarmCam,
       "alarmDesc": alarmDesc,
       "alarmInpsig": alarmInpsig,
       "alarmBitovf": alarmBitovf,
       "alarmLinks": alarmLinks,
       "alarmLinkc": alarmLinkc,
       "alarmPowovl": alarmPowovl,
       "alarmPowv": alarmPowv,
       "alarmTemps": alarmTemps,
       "alarmOvh": alarmOvh,
       "alarmTsErr": alarmTsErr,
       "sdi410cnotifications": sdi410cnotifications,
       "notifyCam": notifyCam,
       "notifyDesc": notifyDesc,
       "notifyInpsig": notifyInpsig,
       "notifyBitovf": notifyBitovf,
       "notifyLinks": notifyLinks,
       "notifyLinkc": notifyLinkc,
       "notifyPowovl": notifyPowovl,
       "notifyPowv": notifyPowv,
       "notifyTemps": notifyTemps,
       "notifyOvh": notifyOvh,
       "notifyTsErr": notifyTsErr,
       "sdi410cInfo": sdi410cInfo,
       "infVersion": infVersion,
       "infSerNum": infSerNum,
       "terrasdi410cMIBConformance": terrasdi410cMIBConformance,
       "terrasdi410cMIBGroups": terrasdi410cMIBGroups,
       "sdi410cTerraMibAllObjects": sdi410cTerraMibAllObjects,
       "sdi410cTerraMibAllNotifications": sdi410cTerraMibAllNotifications}
)
