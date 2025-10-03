# SNMP MIB module (TERRA-sdi480-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\terra\TERRA-sdi480-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:15 2025
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

terra_sdi480 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17)
)
if mibBuilder.loadTexts:
    terra_sdi480.setRevisions(
        ("2017-01-19 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sdi480status_ObjectIdentity = ObjectIdentity
sdi480status = _Sdi480status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1)
)
_RFinStatus1_ObjectIdentity = ObjectIdentity
rFinStatus1 = _RFinStatus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 1)
)
_InLock1_Type = DisplayString
_InLock1_Object = MibScalar
inLock1 = _InLock1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 1, 1),
    _InLock1_Type()
)
inLock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock1.setStatus("current")
_Inlevel1_Type = Integer32
_Inlevel1_Object = MibScalar
inlevel1 = _Inlevel1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 1, 2),
    _Inlevel1_Type()
)
inlevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel1.setStatus("current")
if mibBuilder.loadTexts:
    inlevel1.setUnits("tenth of dbuV")
_Insnr1_Type = Integer32
_Insnr1_Object = MibScalar
insnr1 = _Insnr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 1, 3),
    _Insnr1_Type()
)
insnr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr1.setStatus("current")
if mibBuilder.loadTexts:
    insnr1.setUnits("tenth of db")
_Inbr1_Type = Integer32
_Inbr1_Object = MibScalar
inbr1 = _Inbr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 1, 4),
    _Inbr1_Type()
)
inbr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr1.setStatus("current")
if mibBuilder.loadTexts:
    inbr1.setUnits("tenth of Mbps")
_Inper1_Type = DisplayString
_Inper1_Object = MibScalar
inper1 = _Inper1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 1, 5),
    _Inper1_Type()
)
inper1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper1.setStatus("current")
_RFinStatus2_ObjectIdentity = ObjectIdentity
rFinStatus2 = _RFinStatus2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 2)
)
_InLock2_Type = DisplayString
_InLock2_Object = MibScalar
inLock2 = _InLock2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 2, 1),
    _InLock2_Type()
)
inLock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock2.setStatus("current")
_Inlevel2_Type = Integer32
_Inlevel2_Object = MibScalar
inlevel2 = _Inlevel2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 2, 2),
    _Inlevel2_Type()
)
inlevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel2.setStatus("current")
if mibBuilder.loadTexts:
    inlevel2.setUnits("tenth of dbuV")
_Insnr2_Type = Integer32
_Insnr2_Object = MibScalar
insnr2 = _Insnr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 2, 3),
    _Insnr2_Type()
)
insnr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr2.setStatus("current")
if mibBuilder.loadTexts:
    insnr2.setUnits("tenth of db")
_Inbr2_Type = Integer32
_Inbr2_Object = MibScalar
inbr2 = _Inbr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 2, 4),
    _Inbr2_Type()
)
inbr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr2.setStatus("current")
if mibBuilder.loadTexts:
    inbr2.setUnits("tenth of Mbps")
_Inper2_Type = DisplayString
_Inper2_Object = MibScalar
inper2 = _Inper2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 2, 5),
    _Inper2_Type()
)
inper2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper2.setStatus("current")
_RFinStatus3_ObjectIdentity = ObjectIdentity
rFinStatus3 = _RFinStatus3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 3)
)
_InLock3_Type = DisplayString
_InLock3_Object = MibScalar
inLock3 = _InLock3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 3, 1),
    _InLock3_Type()
)
inLock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock3.setStatus("current")
_Inlevel3_Type = Integer32
_Inlevel3_Object = MibScalar
inlevel3 = _Inlevel3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 3, 2),
    _Inlevel3_Type()
)
inlevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel3.setStatus("current")
if mibBuilder.loadTexts:
    inlevel3.setUnits("tenth of dbuV")
_Insnr3_Type = Integer32
_Insnr3_Object = MibScalar
insnr3 = _Insnr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 3, 3),
    _Insnr3_Type()
)
insnr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr3.setStatus("current")
if mibBuilder.loadTexts:
    insnr3.setUnits("tenth of db")
_Inbr3_Type = Integer32
_Inbr3_Object = MibScalar
inbr3 = _Inbr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 3, 4),
    _Inbr3_Type()
)
inbr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr3.setStatus("current")
if mibBuilder.loadTexts:
    inbr3.setUnits("tenth of Mbps")
_Inper3_Type = DisplayString
_Inper3_Object = MibScalar
inper3 = _Inper3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 3, 5),
    _Inper3_Type()
)
inper3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper3.setStatus("current")
_RFinStatus4_ObjectIdentity = ObjectIdentity
rFinStatus4 = _RFinStatus4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 4)
)
_InLock4_Type = DisplayString
_InLock4_Object = MibScalar
inLock4 = _InLock4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 4, 1),
    _InLock4_Type()
)
inLock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock4.setStatus("current")
_Inlevel4_Type = Integer32
_Inlevel4_Object = MibScalar
inlevel4 = _Inlevel4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 4, 2),
    _Inlevel4_Type()
)
inlevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel4.setStatus("current")
if mibBuilder.loadTexts:
    inlevel4.setUnits("tenth of dbuV")
_Insnr4_Type = Integer32
_Insnr4_Object = MibScalar
insnr4 = _Insnr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 4, 3),
    _Insnr4_Type()
)
insnr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr4.setStatus("current")
if mibBuilder.loadTexts:
    insnr4.setUnits("tenth of db")
_Inbr4_Type = Integer32
_Inbr4_Object = MibScalar
inbr4 = _Inbr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 4, 4),
    _Inbr4_Type()
)
inbr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr4.setStatus("current")
if mibBuilder.loadTexts:
    inbr4.setUnits("tenth of Mbps")
_Inper4_Type = DisplayString
_Inper4_Object = MibScalar
inper4 = _Inper4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 4, 5),
    _Inper4_Type()
)
inper4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper4.setStatus("current")
_RFinStatus5_ObjectIdentity = ObjectIdentity
rFinStatus5 = _RFinStatus5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 5)
)
_InLock5_Type = DisplayString
_InLock5_Object = MibScalar
inLock5 = _InLock5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 5, 1),
    _InLock5_Type()
)
inLock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock5.setStatus("current")
_Inlevel5_Type = Integer32
_Inlevel5_Object = MibScalar
inlevel5 = _Inlevel5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 5, 2),
    _Inlevel5_Type()
)
inlevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel5.setStatus("current")
if mibBuilder.loadTexts:
    inlevel5.setUnits("tenth of dbuV")
_Insnr5_Type = Integer32
_Insnr5_Object = MibScalar
insnr5 = _Insnr5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 5, 3),
    _Insnr5_Type()
)
insnr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr5.setStatus("current")
if mibBuilder.loadTexts:
    insnr5.setUnits("tenth of db")
_Inbr5_Type = Integer32
_Inbr5_Object = MibScalar
inbr5 = _Inbr5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 5, 4),
    _Inbr5_Type()
)
inbr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr5.setStatus("current")
if mibBuilder.loadTexts:
    inbr5.setUnits("tenth of Mbps")
_Inper5_Type = DisplayString
_Inper5_Object = MibScalar
inper5 = _Inper5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 5, 5),
    _Inper5_Type()
)
inper5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper5.setStatus("current")
_RFinStatus6_ObjectIdentity = ObjectIdentity
rFinStatus6 = _RFinStatus6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 6)
)
_InLock6_Type = DisplayString
_InLock6_Object = MibScalar
inLock6 = _InLock6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 6, 1),
    _InLock6_Type()
)
inLock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock6.setStatus("current")
_Inlevel6_Type = Integer32
_Inlevel6_Object = MibScalar
inlevel6 = _Inlevel6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 6, 2),
    _Inlevel6_Type()
)
inlevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel6.setStatus("current")
if mibBuilder.loadTexts:
    inlevel6.setUnits("tenth of dbuV")
_Insnr6_Type = Integer32
_Insnr6_Object = MibScalar
insnr6 = _Insnr6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 6, 3),
    _Insnr6_Type()
)
insnr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr6.setStatus("current")
if mibBuilder.loadTexts:
    insnr6.setUnits("tenth of db")
_Inbr6_Type = Integer32
_Inbr6_Object = MibScalar
inbr6 = _Inbr6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 6, 4),
    _Inbr6_Type()
)
inbr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr6.setStatus("current")
if mibBuilder.loadTexts:
    inbr6.setUnits("tenth of Mbps")
_Inper6_Type = DisplayString
_Inper6_Object = MibScalar
inper6 = _Inper6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 6, 5),
    _Inper6_Type()
)
inper6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper6.setStatus("current")
_RFinStatus7_ObjectIdentity = ObjectIdentity
rFinStatus7 = _RFinStatus7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 7)
)
_InLock7_Type = DisplayString
_InLock7_Object = MibScalar
inLock7 = _InLock7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 7, 1),
    _InLock7_Type()
)
inLock7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock7.setStatus("current")
_Inlevel7_Type = Integer32
_Inlevel7_Object = MibScalar
inlevel7 = _Inlevel7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 7, 2),
    _Inlevel7_Type()
)
inlevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel7.setStatus("current")
if mibBuilder.loadTexts:
    inlevel7.setUnits("tenth of dbuV")
_Insnr7_Type = Integer32
_Insnr7_Object = MibScalar
insnr7 = _Insnr7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 7, 3),
    _Insnr7_Type()
)
insnr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr7.setStatus("current")
if mibBuilder.loadTexts:
    insnr7.setUnits("tenth of db")
_Inbr7_Type = Integer32
_Inbr7_Object = MibScalar
inbr7 = _Inbr7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 7, 4),
    _Inbr7_Type()
)
inbr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr7.setStatus("current")
if mibBuilder.loadTexts:
    inbr7.setUnits("tenth of Mbps")
_Inper7_Type = DisplayString
_Inper7_Object = MibScalar
inper7 = _Inper7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 7, 5),
    _Inper7_Type()
)
inper7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper7.setStatus("current")
_RFinStatus8_ObjectIdentity = ObjectIdentity
rFinStatus8 = _RFinStatus8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 8)
)
_InLock8_Type = DisplayString
_InLock8_Object = MibScalar
inLock8 = _InLock8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 8, 1),
    _InLock8_Type()
)
inLock8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock8.setStatus("current")
_Inlevel8_Type = Integer32
_Inlevel8_Object = MibScalar
inlevel8 = _Inlevel8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 8, 2),
    _Inlevel8_Type()
)
inlevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel8.setStatus("current")
if mibBuilder.loadTexts:
    inlevel8.setUnits("tenth of dbuV")
_Insnr8_Type = Integer32
_Insnr8_Object = MibScalar
insnr8 = _Insnr8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 8, 3),
    _Insnr8_Type()
)
insnr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr8.setStatus("current")
if mibBuilder.loadTexts:
    insnr8.setUnits("tenth of db")
_Inbr8_Type = Integer32
_Inbr8_Object = MibScalar
inbr8 = _Inbr8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 8, 4),
    _Inbr8_Type()
)
inbr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr8.setStatus("current")
if mibBuilder.loadTexts:
    inbr8.setUnits("tenth of Mbps")
_Inper8_Type = DisplayString
_Inper8_Object = MibScalar
inper8 = _Inper8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 8, 5),
    _Inper8_Type()
)
inper8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper8.setStatus("current")
_UsbStatus_ObjectIdentity = ObjectIdentity
usbStatus = _UsbStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 9)
)
_UsbinBR_Type = Integer32
_UsbinBR_Object = MibScalar
usbinBR = _UsbinBR_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 9, 1),
    _UsbinBR_Type()
)
usbinBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbinBR.setStatus("current")
if mibBuilder.loadTexts:
    usbinBR.setUnits("tenth of Mbps")
_OutStream1_ObjectIdentity = ObjectIdentity
outStream1 = _OutStream1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 10)
)
_OutBr1_Type = Integer32
_OutBr1_Object = MibScalar
outBr1 = _OutBr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 10, 1),
    _OutBr1_Type()
)
outBr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr1.setStatus("current")
if mibBuilder.loadTexts:
    outBr1.setUnits("tenth of Mbps")
_OutStream2_ObjectIdentity = ObjectIdentity
outStream2 = _OutStream2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 11)
)
_OutBr2_Type = Integer32
_OutBr2_Object = MibScalar
outBr2 = _OutBr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 11, 1),
    _OutBr2_Type()
)
outBr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr2.setStatus("current")
if mibBuilder.loadTexts:
    outBr2.setUnits("tenth of Mbps")
_OutStream3_ObjectIdentity = ObjectIdentity
outStream3 = _OutStream3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 12)
)
_OutBr3_Type = Integer32
_OutBr3_Object = MibScalar
outBr3 = _OutBr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 12, 1),
    _OutBr3_Type()
)
outBr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr3.setStatus("current")
if mibBuilder.loadTexts:
    outBr3.setUnits("tenth of Mbps")
_OutStream4_ObjectIdentity = ObjectIdentity
outStream4 = _OutStream4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 13)
)
_OutBr4_Type = Integer32
_OutBr4_Object = MibScalar
outBr4 = _OutBr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 13, 1),
    _OutBr4_Type()
)
outBr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr4.setStatus("current")
if mibBuilder.loadTexts:
    outBr4.setUnits("tenth of Mbps")
_OutStream5_ObjectIdentity = ObjectIdentity
outStream5 = _OutStream5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 14)
)
_OutBr5_Type = Integer32
_OutBr5_Object = MibScalar
outBr5 = _OutBr5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 14, 1),
    _OutBr5_Type()
)
outBr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr5.setStatus("current")
if mibBuilder.loadTexts:
    outBr5.setUnits("tenth of Mbps")
_OutStream6_ObjectIdentity = ObjectIdentity
outStream6 = _OutStream6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 15)
)
_OutBr6_Type = Integer32
_OutBr6_Object = MibScalar
outBr6 = _OutBr6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 15, 1),
    _OutBr6_Type()
)
outBr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr6.setStatus("current")
if mibBuilder.loadTexts:
    outBr6.setUnits("tenth of Mbps")
_OutStream7_ObjectIdentity = ObjectIdentity
outStream7 = _OutStream7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 16)
)
_OutBr7_Type = Integer32
_OutBr7_Object = MibScalar
outBr7 = _OutBr7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 16, 1),
    _OutBr7_Type()
)
outBr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr7.setStatus("current")
if mibBuilder.loadTexts:
    outBr7.setUnits("tenth of Mbps")
_OutStream8_ObjectIdentity = ObjectIdentity
outStream8 = _OutStream8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 17)
)
_OutBr8_Type = Integer32
_OutBr8_Object = MibScalar
outBr8 = _OutBr8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 17, 1),
    _OutBr8_Type()
)
outBr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr8.setStatus("current")
if mibBuilder.loadTexts:
    outBr8.setUnits("tenth of Mbps")
_OutStream9_ObjectIdentity = ObjectIdentity
outStream9 = _OutStream9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 18)
)
_OutBr9_Type = Integer32
_OutBr9_Object = MibScalar
outBr9 = _OutBr9_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 18, 1),
    _OutBr9_Type()
)
outBr9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr9.setStatus("current")
if mibBuilder.loadTexts:
    outBr9.setUnits("tenth of Mbps")
_OutStream10_ObjectIdentity = ObjectIdentity
outStream10 = _OutStream10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 19)
)
_OutBr10_Type = Integer32
_OutBr10_Object = MibScalar
outBr10 = _OutBr10_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 19, 1),
    _OutBr10_Type()
)
outBr10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr10.setStatus("current")
if mibBuilder.loadTexts:
    outBr10.setUnits("tenth of Mbps")
_OutStream11_ObjectIdentity = ObjectIdentity
outStream11 = _OutStream11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 20)
)
_OutBr11_Type = Integer32
_OutBr11_Object = MibScalar
outBr11 = _OutBr11_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 20, 1),
    _OutBr11_Type()
)
outBr11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr11.setStatus("current")
if mibBuilder.loadTexts:
    outBr11.setUnits("tenth of Mbps")
_OutStream12_ObjectIdentity = ObjectIdentity
outStream12 = _OutStream12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 21)
)
_OutBr12_Type = Integer32
_OutBr12_Object = MibScalar
outBr12 = _OutBr12_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 21, 1),
    _OutBr12_Type()
)
outBr12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr12.setStatus("current")
if mibBuilder.loadTexts:
    outBr12.setUnits("tenth of Mbps")
_OutStream13_ObjectIdentity = ObjectIdentity
outStream13 = _OutStream13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 22)
)
_OutBr13_Type = Integer32
_OutBr13_Object = MibScalar
outBr13 = _OutBr13_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 22, 1),
    _OutBr13_Type()
)
outBr13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr13.setStatus("current")
if mibBuilder.loadTexts:
    outBr13.setUnits("tenth of Mbps")
_OutStream14_ObjectIdentity = ObjectIdentity
outStream14 = _OutStream14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 23)
)
_OutBr14_Type = Integer32
_OutBr14_Object = MibScalar
outBr14 = _OutBr14_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 23, 1),
    _OutBr14_Type()
)
outBr14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr14.setStatus("current")
if mibBuilder.loadTexts:
    outBr14.setUnits("tenth of Mbps")
_OutStream15_ObjectIdentity = ObjectIdentity
outStream15 = _OutStream15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 24)
)
_OutBr15_Type = Integer32
_OutBr15_Object = MibScalar
outBr15 = _OutBr15_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 24, 1),
    _OutBr15_Type()
)
outBr15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr15.setStatus("current")
if mibBuilder.loadTexts:
    outBr15.setUnits("tenth of Mbps")
_OutStream16_ObjectIdentity = ObjectIdentity
outStream16 = _OutStream16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 25)
)
_OutBr16_Type = Integer32
_OutBr16_Object = MibScalar
outBr16 = _OutBr16_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 25, 1),
    _OutBr16_Type()
)
outBr16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr16.setStatus("current")
if mibBuilder.loadTexts:
    outBr16.setUnits("tenth of Mbps")
_OutStream17_ObjectIdentity = ObjectIdentity
outStream17 = _OutStream17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 26)
)
_OutBr17_Type = Integer32
_OutBr17_Object = MibScalar
outBr17 = _OutBr17_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 26, 1),
    _OutBr17_Type()
)
outBr17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr17.setStatus("current")
if mibBuilder.loadTexts:
    outBr17.setUnits("tenth of Mbps")
_OutStream18_ObjectIdentity = ObjectIdentity
outStream18 = _OutStream18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 27)
)
_OutBr18_Type = Integer32
_OutBr18_Object = MibScalar
outBr18 = _OutBr18_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 27, 1),
    _OutBr18_Type()
)
outBr18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr18.setStatus("current")
if mibBuilder.loadTexts:
    outBr18.setUnits("tenth of Mbps")
_OutStream19_ObjectIdentity = ObjectIdentity
outStream19 = _OutStream19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 28)
)
_OutBr19_Type = Integer32
_OutBr19_Object = MibScalar
outBr19 = _OutBr19_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 28, 1),
    _OutBr19_Type()
)
outBr19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr19.setStatus("current")
if mibBuilder.loadTexts:
    outBr19.setUnits("tenth of Mbps")
_OutStream20_ObjectIdentity = ObjectIdentity
outStream20 = _OutStream20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 29)
)
_OutBr20_Type = Integer32
_OutBr20_Object = MibScalar
outBr20 = _OutBr20_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 29, 1),
    _OutBr20_Type()
)
outBr20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr20.setStatus("current")
if mibBuilder.loadTexts:
    outBr20.setUnits("tenth of Mbps")
_OutStream21_ObjectIdentity = ObjectIdentity
outStream21 = _OutStream21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 30)
)
_OutBr21_Type = Integer32
_OutBr21_Object = MibScalar
outBr21 = _OutBr21_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 30, 1),
    _OutBr21_Type()
)
outBr21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr21.setStatus("current")
if mibBuilder.loadTexts:
    outBr21.setUnits("tenth of Mbps")
_OutStream22_ObjectIdentity = ObjectIdentity
outStream22 = _OutStream22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 31)
)
_OutBr22_Type = Integer32
_OutBr22_Object = MibScalar
outBr22 = _OutBr22_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 31, 1),
    _OutBr22_Type()
)
outBr22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr22.setStatus("current")
if mibBuilder.loadTexts:
    outBr22.setUnits("tenth of Mbps")
_OutStream23_ObjectIdentity = ObjectIdentity
outStream23 = _OutStream23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 32)
)
_OutBr23_Type = Integer32
_OutBr23_Object = MibScalar
outBr23 = _OutBr23_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 32, 1),
    _OutBr23_Type()
)
outBr23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr23.setStatus("current")
if mibBuilder.loadTexts:
    outBr23.setUnits("tenth of Mbps")
_OutStream24_ObjectIdentity = ObjectIdentity
outStream24 = _OutStream24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 33)
)
_OutBr24_Type = Integer32
_OutBr24_Object = MibScalar
outBr24 = _OutBr24_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 33, 1),
    _OutBr24_Type()
)
outBr24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr24.setStatus("current")
if mibBuilder.loadTexts:
    outBr24.setUnits("tenth of Mbps")
_OutStream25_ObjectIdentity = ObjectIdentity
outStream25 = _OutStream25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 34)
)
_OutBr25_Type = Integer32
_OutBr25_Object = MibScalar
outBr25 = _OutBr25_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 34, 1),
    _OutBr25_Type()
)
outBr25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr25.setStatus("current")
if mibBuilder.loadTexts:
    outBr25.setUnits("tenth of Mbps")
_OutStream26_ObjectIdentity = ObjectIdentity
outStream26 = _OutStream26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 35)
)
_OutBr26_Type = Integer32
_OutBr26_Object = MibScalar
outBr26 = _OutBr26_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 35, 1),
    _OutBr26_Type()
)
outBr26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr26.setStatus("current")
if mibBuilder.loadTexts:
    outBr26.setUnits("tenth of Mbps")
_OutStream27_ObjectIdentity = ObjectIdentity
outStream27 = _OutStream27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 36)
)
_OutBr27_Type = Integer32
_OutBr27_Object = MibScalar
outBr27 = _OutBr27_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 36, 1),
    _OutBr27_Type()
)
outBr27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr27.setStatus("current")
if mibBuilder.loadTexts:
    outBr27.setUnits("tenth of Mbps")
_OutStream28_ObjectIdentity = ObjectIdentity
outStream28 = _OutStream28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 37)
)
_OutBr28_Type = Integer32
_OutBr28_Object = MibScalar
outBr28 = _OutBr28_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 37, 1),
    _OutBr28_Type()
)
outBr28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr28.setStatus("current")
if mibBuilder.loadTexts:
    outBr28.setUnits("tenth of Mbps")
_OutStream29_ObjectIdentity = ObjectIdentity
outStream29 = _OutStream29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 38)
)
_OutBr29_Type = Integer32
_OutBr29_Object = MibScalar
outBr29 = _OutBr29_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 38, 1),
    _OutBr29_Type()
)
outBr29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr29.setStatus("current")
if mibBuilder.loadTexts:
    outBr29.setUnits("tenth of Mbps")
_OutStream30_ObjectIdentity = ObjectIdentity
outStream30 = _OutStream30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 39)
)
_OutBr30_Type = Integer32
_OutBr30_Object = MibScalar
outBr30 = _OutBr30_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 39, 1),
    _OutBr30_Type()
)
outBr30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr30.setStatus("current")
if mibBuilder.loadTexts:
    outBr30.setUnits("tenth of Mbps")
_OutStream31_ObjectIdentity = ObjectIdentity
outStream31 = _OutStream31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 40)
)
_OutBr31_Type = Integer32
_OutBr31_Object = MibScalar
outBr31 = _OutBr31_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 40, 1),
    _OutBr31_Type()
)
outBr31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr31.setStatus("current")
if mibBuilder.loadTexts:
    outBr31.setUnits("tenth of Mbps")
_OutStream32_ObjectIdentity = ObjectIdentity
outStream32 = _OutStream32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 41)
)
_OutBr32_Type = Integer32
_OutBr32_Object = MibScalar
outBr32 = _OutBr32_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 41, 1),
    _OutBr32_Type()
)
outBr32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr32.setStatus("current")
if mibBuilder.loadTexts:
    outBr32.setUnits("tenth of Mbps")
_OutStream33_ObjectIdentity = ObjectIdentity
outStream33 = _OutStream33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 42)
)
_OutBr33_Type = Integer32
_OutBr33_Object = MibScalar
outBr33 = _OutBr33_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 42, 1),
    _OutBr33_Type()
)
outBr33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr33.setStatus("current")
if mibBuilder.loadTexts:
    outBr33.setUnits("tenth of Mbps")
_OutStream34_ObjectIdentity = ObjectIdentity
outStream34 = _OutStream34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 43)
)
_OutBr34_Type = Integer32
_OutBr34_Object = MibScalar
outBr34 = _OutBr34_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 43, 1),
    _OutBr34_Type()
)
outBr34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr34.setStatus("current")
if mibBuilder.loadTexts:
    outBr34.setUnits("tenth of Mbps")
_OutStream35_ObjectIdentity = ObjectIdentity
outStream35 = _OutStream35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 44)
)
_OutBr35_Type = Integer32
_OutBr35_Object = MibScalar
outBr35 = _OutBr35_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 44, 1),
    _OutBr35_Type()
)
outBr35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr35.setStatus("current")
if mibBuilder.loadTexts:
    outBr35.setUnits("tenth of Mbps")
_OutStream36_ObjectIdentity = ObjectIdentity
outStream36 = _OutStream36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 45)
)
_OutBr36_Type = Integer32
_OutBr36_Object = MibScalar
outBr36 = _OutBr36_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 45, 1),
    _OutBr36_Type()
)
outBr36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr36.setStatus("current")
if mibBuilder.loadTexts:
    outBr36.setUnits("tenth of Mbps")
_OutStream37_ObjectIdentity = ObjectIdentity
outStream37 = _OutStream37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 46)
)
_OutBr37_Type = Integer32
_OutBr37_Object = MibScalar
outBr37 = _OutBr37_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 46, 1),
    _OutBr37_Type()
)
outBr37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr37.setStatus("current")
if mibBuilder.loadTexts:
    outBr37.setUnits("tenth of Mbps")
_OutStream38_ObjectIdentity = ObjectIdentity
outStream38 = _OutStream38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 47)
)
_OutBr38_Type = Integer32
_OutBr38_Object = MibScalar
outBr38 = _OutBr38_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 47, 1),
    _OutBr38_Type()
)
outBr38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr38.setStatus("current")
if mibBuilder.loadTexts:
    outBr38.setUnits("tenth of Mbps")
_OutStream39_ObjectIdentity = ObjectIdentity
outStream39 = _OutStream39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 48)
)
_OutBr39_Type = Integer32
_OutBr39_Object = MibScalar
outBr39 = _OutBr39_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 48, 1),
    _OutBr39_Type()
)
outBr39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr39.setStatus("current")
if mibBuilder.loadTexts:
    outBr39.setUnits("tenth of Mbps")
_OutStream40_ObjectIdentity = ObjectIdentity
outStream40 = _OutStream40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 49)
)
_OutBr40_Type = Integer32
_OutBr40_Object = MibScalar
outBr40 = _OutBr40_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 49, 1),
    _OutBr40_Type()
)
outBr40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr40.setStatus("current")
if mibBuilder.loadTexts:
    outBr40.setUnits("tenth of Mbps")
_OutStream41_ObjectIdentity = ObjectIdentity
outStream41 = _OutStream41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 50)
)
_OutBr41_Type = Integer32
_OutBr41_Object = MibScalar
outBr41 = _OutBr41_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 50, 1),
    _OutBr41_Type()
)
outBr41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr41.setStatus("current")
if mibBuilder.loadTexts:
    outBr41.setUnits("tenth of Mbps")
_OutStream42_ObjectIdentity = ObjectIdentity
outStream42 = _OutStream42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 51)
)
_OutBr42_Type = Integer32
_OutBr42_Object = MibScalar
outBr42 = _OutBr42_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 51, 1),
    _OutBr42_Type()
)
outBr42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr42.setStatus("current")
if mibBuilder.loadTexts:
    outBr42.setUnits("tenth of Mbps")
_OutStream43_ObjectIdentity = ObjectIdentity
outStream43 = _OutStream43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 52)
)
_OutBr43_Type = Integer32
_OutBr43_Object = MibScalar
outBr43 = _OutBr43_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 52, 1),
    _OutBr43_Type()
)
outBr43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr43.setStatus("current")
if mibBuilder.loadTexts:
    outBr43.setUnits("tenth of Mbps")
_OutStream44_ObjectIdentity = ObjectIdentity
outStream44 = _OutStream44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 53)
)
_OutBr44_Type = Integer32
_OutBr44_Object = MibScalar
outBr44 = _OutBr44_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 53, 1),
    _OutBr44_Type()
)
outBr44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr44.setStatus("current")
if mibBuilder.loadTexts:
    outBr44.setUnits("tenth of Mbps")
_OutStream45_ObjectIdentity = ObjectIdentity
outStream45 = _OutStream45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 54)
)
_OutBr45_Type = Integer32
_OutBr45_Object = MibScalar
outBr45 = _OutBr45_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 54, 1),
    _OutBr45_Type()
)
outBr45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr45.setStatus("current")
if mibBuilder.loadTexts:
    outBr45.setUnits("tenth of Mbps")
_OutStream46_ObjectIdentity = ObjectIdentity
outStream46 = _OutStream46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 55)
)
_OutBr46_Type = Integer32
_OutBr46_Object = MibScalar
outBr46 = _OutBr46_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 55, 1),
    _OutBr46_Type()
)
outBr46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr46.setStatus("current")
if mibBuilder.loadTexts:
    outBr46.setUnits("tenth of Mbps")
_OutStream47_ObjectIdentity = ObjectIdentity
outStream47 = _OutStream47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 56)
)
_OutBr47_Type = Integer32
_OutBr47_Object = MibScalar
outBr47 = _OutBr47_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 56, 1),
    _OutBr47_Type()
)
outBr47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr47.setStatus("current")
if mibBuilder.loadTexts:
    outBr47.setUnits("tenth of Mbps")
_OutStream48_ObjectIdentity = ObjectIdentity
outStream48 = _OutStream48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 57)
)
_OutBr48_Type = Integer32
_OutBr48_Object = MibScalar
outBr48 = _OutBr48_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 57, 1),
    _OutBr48_Type()
)
outBr48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr48.setStatus("current")
if mibBuilder.loadTexts:
    outBr48.setUnits("tenth of Mbps")
_OutStream49_ObjectIdentity = ObjectIdentity
outStream49 = _OutStream49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 58)
)
_OutBr49_Type = Integer32
_OutBr49_Object = MibScalar
outBr49 = _OutBr49_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 58, 1),
    _OutBr49_Type()
)
outBr49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr49.setStatus("current")
if mibBuilder.loadTexts:
    outBr49.setUnits("tenth of Mbps")
_OutStream50_ObjectIdentity = ObjectIdentity
outStream50 = _OutStream50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 59)
)
_OutBr50_Type = Integer32
_OutBr50_Object = MibScalar
outBr50 = _OutBr50_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 59, 1),
    _OutBr50_Type()
)
outBr50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr50.setStatus("current")
if mibBuilder.loadTexts:
    outBr50.setUnits("tenth of Mbps")
_OutStream51_ObjectIdentity = ObjectIdentity
outStream51 = _OutStream51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 60)
)
_OutBr51_Type = Integer32
_OutBr51_Object = MibScalar
outBr51 = _OutBr51_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 60, 1),
    _OutBr51_Type()
)
outBr51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr51.setStatus("current")
if mibBuilder.loadTexts:
    outBr51.setUnits("tenth of Mbps")
_OutStream52_ObjectIdentity = ObjectIdentity
outStream52 = _OutStream52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 61)
)
_OutBr52_Type = Integer32
_OutBr52_Object = MibScalar
outBr52 = _OutBr52_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 61, 1),
    _OutBr52_Type()
)
outBr52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr52.setStatus("current")
if mibBuilder.loadTexts:
    outBr52.setUnits("tenth of Mbps")
_OutStream53_ObjectIdentity = ObjectIdentity
outStream53 = _OutStream53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 62)
)
_OutBr53_Type = Integer32
_OutBr53_Object = MibScalar
outBr53 = _OutBr53_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 62, 1),
    _OutBr53_Type()
)
outBr53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr53.setStatus("current")
if mibBuilder.loadTexts:
    outBr53.setUnits("tenth of Mbps")
_OutStream54_ObjectIdentity = ObjectIdentity
outStream54 = _OutStream54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 63)
)
_OutBr54_Type = Integer32
_OutBr54_Object = MibScalar
outBr54 = _OutBr54_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 63, 1),
    _OutBr54_Type()
)
outBr54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr54.setStatus("current")
if mibBuilder.loadTexts:
    outBr54.setUnits("tenth of Mbps")
_OutStream55_ObjectIdentity = ObjectIdentity
outStream55 = _OutStream55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 64)
)
_OutBr55_Type = Integer32
_OutBr55_Object = MibScalar
outBr55 = _OutBr55_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 64, 1),
    _OutBr55_Type()
)
outBr55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr55.setStatus("current")
if mibBuilder.loadTexts:
    outBr55.setUnits("tenth of Mbps")
_OutStream56_ObjectIdentity = ObjectIdentity
outStream56 = _OutStream56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 65)
)
_OutBr56_Type = Integer32
_OutBr56_Object = MibScalar
outBr56 = _OutBr56_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 65, 1),
    _OutBr56_Type()
)
outBr56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr56.setStatus("current")
if mibBuilder.loadTexts:
    outBr56.setUnits("tenth of Mbps")
_OutStream57_ObjectIdentity = ObjectIdentity
outStream57 = _OutStream57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 66)
)
_OutBr57_Type = Integer32
_OutBr57_Object = MibScalar
outBr57 = _OutBr57_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 66, 1),
    _OutBr57_Type()
)
outBr57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr57.setStatus("current")
if mibBuilder.loadTexts:
    outBr57.setUnits("tenth of Mbps")
_OutStream58_ObjectIdentity = ObjectIdentity
outStream58 = _OutStream58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 67)
)
_OutBr58_Type = Integer32
_OutBr58_Object = MibScalar
outBr58 = _OutBr58_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 67, 1),
    _OutBr58_Type()
)
outBr58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr58.setStatus("current")
if mibBuilder.loadTexts:
    outBr58.setUnits("tenth of Mbps")
_OutStream59_ObjectIdentity = ObjectIdentity
outStream59 = _OutStream59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 68)
)
_OutBr59_Type = Integer32
_OutBr59_Object = MibScalar
outBr59 = _OutBr59_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 68, 1),
    _OutBr59_Type()
)
outBr59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr59.setStatus("current")
if mibBuilder.loadTexts:
    outBr59.setUnits("tenth of Mbps")
_OutStream60_ObjectIdentity = ObjectIdentity
outStream60 = _OutStream60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 69)
)
_OutBr60_Type = Integer32
_OutBr60_Object = MibScalar
outBr60 = _OutBr60_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 69, 1),
    _OutBr60_Type()
)
outBr60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr60.setStatus("current")
if mibBuilder.loadTexts:
    outBr60.setUnits("tenth of Mbps")
_OutStream61_ObjectIdentity = ObjectIdentity
outStream61 = _OutStream61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 70)
)
_OutBr61_Type = Integer32
_OutBr61_Object = MibScalar
outBr61 = _OutBr61_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 70, 1),
    _OutBr61_Type()
)
outBr61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr61.setStatus("current")
if mibBuilder.loadTexts:
    outBr61.setUnits("tenth of Mbps")
_OutStream62_ObjectIdentity = ObjectIdentity
outStream62 = _OutStream62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 71)
)
_OutBr62_Type = Integer32
_OutBr62_Object = MibScalar
outBr62 = _OutBr62_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 71, 1),
    _OutBr62_Type()
)
outBr62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr62.setStatus("current")
if mibBuilder.loadTexts:
    outBr62.setUnits("tenth of Mbps")
_OutStream63_ObjectIdentity = ObjectIdentity
outStream63 = _OutStream63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 72)
)
_OutBr63_Type = Integer32
_OutBr63_Object = MibScalar
outBr63 = _OutBr63_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 72, 1),
    _OutBr63_Type()
)
outBr63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr63.setStatus("current")
if mibBuilder.loadTexts:
    outBr63.setUnits("tenth of Mbps")
_OutStream64_ObjectIdentity = ObjectIdentity
outStream64 = _OutStream64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 73)
)
_OutBr64_Type = Integer32
_OutBr64_Object = MibScalar
outBr64 = _OutBr64_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 73, 1),
    _OutBr64_Type()
)
outBr64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr64.setStatus("current")
if mibBuilder.loadTexts:
    outBr64.setUnits("tenth of Mbps")
_OutStream65_ObjectIdentity = ObjectIdentity
outStream65 = _OutStream65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 74)
)
_OutBr65_Type = Integer32
_OutBr65_Object = MibScalar
outBr65 = _OutBr65_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 74, 1),
    _OutBr65_Type()
)
outBr65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr65.setStatus("current")
if mibBuilder.loadTexts:
    outBr65.setUnits("tenth of Mbps")
_OutStream66_ObjectIdentity = ObjectIdentity
outStream66 = _OutStream66_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 75)
)
_OutBr66_Type = Integer32
_OutBr66_Object = MibScalar
outBr66 = _OutBr66_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 75, 1),
    _OutBr66_Type()
)
outBr66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr66.setStatus("current")
if mibBuilder.loadTexts:
    outBr66.setUnits("tenth of Mbps")
_OutStream67_ObjectIdentity = ObjectIdentity
outStream67 = _OutStream67_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 76)
)
_OutBr67_Type = Integer32
_OutBr67_Object = MibScalar
outBr67 = _OutBr67_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 76, 1),
    _OutBr67_Type()
)
outBr67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr67.setStatus("current")
if mibBuilder.loadTexts:
    outBr67.setUnits("tenth of Mbps")
_OutStream68_ObjectIdentity = ObjectIdentity
outStream68 = _OutStream68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 77)
)
_OutBr68_Type = Integer32
_OutBr68_Object = MibScalar
outBr68 = _OutBr68_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 77, 1),
    _OutBr68_Type()
)
outBr68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr68.setStatus("current")
if mibBuilder.loadTexts:
    outBr68.setUnits("tenth of Mbps")
_OutStream69_ObjectIdentity = ObjectIdentity
outStream69 = _OutStream69_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 78)
)
_OutBr69_Type = Integer32
_OutBr69_Object = MibScalar
outBr69 = _OutBr69_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 78, 1),
    _OutBr69_Type()
)
outBr69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr69.setStatus("current")
if mibBuilder.loadTexts:
    outBr69.setUnits("tenth of Mbps")
_OutStream70_ObjectIdentity = ObjectIdentity
outStream70 = _OutStream70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 79)
)
_OutBr70_Type = Integer32
_OutBr70_Object = MibScalar
outBr70 = _OutBr70_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 79, 1),
    _OutBr70_Type()
)
outBr70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr70.setStatus("current")
if mibBuilder.loadTexts:
    outBr70.setUnits("tenth of Mbps")
_OutStream71_ObjectIdentity = ObjectIdentity
outStream71 = _OutStream71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 80)
)
_OutBr71_Type = Integer32
_OutBr71_Object = MibScalar
outBr71 = _OutBr71_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 80, 1),
    _OutBr71_Type()
)
outBr71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr71.setStatus("current")
if mibBuilder.loadTexts:
    outBr71.setUnits("tenth of Mbps")
_OutStream72_ObjectIdentity = ObjectIdentity
outStream72 = _OutStream72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 81)
)
_OutBr72_Type = Integer32
_OutBr72_Object = MibScalar
outBr72 = _OutBr72_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 81, 1),
    _OutBr72_Type()
)
outBr72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr72.setStatus("current")
if mibBuilder.loadTexts:
    outBr72.setUnits("tenth of Mbps")
_OutStream73_ObjectIdentity = ObjectIdentity
outStream73 = _OutStream73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 82)
)
_OutBr73_Type = Integer32
_OutBr73_Object = MibScalar
outBr73 = _OutBr73_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 82, 1),
    _OutBr73_Type()
)
outBr73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr73.setStatus("current")
if mibBuilder.loadTexts:
    outBr73.setUnits("tenth of Mbps")
_OutStream74_ObjectIdentity = ObjectIdentity
outStream74 = _OutStream74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 83)
)
_OutBr74_Type = Integer32
_OutBr74_Object = MibScalar
outBr74 = _OutBr74_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 83, 1),
    _OutBr74_Type()
)
outBr74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr74.setStatus("current")
if mibBuilder.loadTexts:
    outBr74.setUnits("tenth of Mbps")
_OutStream75_ObjectIdentity = ObjectIdentity
outStream75 = _OutStream75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 84)
)
_OutBr75_Type = Integer32
_OutBr75_Object = MibScalar
outBr75 = _OutBr75_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 84, 1),
    _OutBr75_Type()
)
outBr75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr75.setStatus("current")
if mibBuilder.loadTexts:
    outBr75.setUnits("tenth of Mbps")
_OutStream76_ObjectIdentity = ObjectIdentity
outStream76 = _OutStream76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 85)
)
_OutBr76_Type = Integer32
_OutBr76_Object = MibScalar
outBr76 = _OutBr76_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 85, 1),
    _OutBr76_Type()
)
outBr76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr76.setStatus("current")
if mibBuilder.loadTexts:
    outBr76.setUnits("tenth of Mbps")
_OutStream77_ObjectIdentity = ObjectIdentity
outStream77 = _OutStream77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 86)
)
_OutBr77_Type = Integer32
_OutBr77_Object = MibScalar
outBr77 = _OutBr77_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 86, 1),
    _OutBr77_Type()
)
outBr77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr77.setStatus("current")
if mibBuilder.loadTexts:
    outBr77.setUnits("tenth of Mbps")
_OutStream78_ObjectIdentity = ObjectIdentity
outStream78 = _OutStream78_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 87)
)
_OutBr78_Type = Integer32
_OutBr78_Object = MibScalar
outBr78 = _OutBr78_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 87, 1),
    _OutBr78_Type()
)
outBr78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr78.setStatus("current")
if mibBuilder.loadTexts:
    outBr78.setUnits("tenth of Mbps")
_OutStream79_ObjectIdentity = ObjectIdentity
outStream79 = _OutStream79_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 88)
)
_OutBr79_Type = Integer32
_OutBr79_Object = MibScalar
outBr79 = _OutBr79_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 88, 1),
    _OutBr79_Type()
)
outBr79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr79.setStatus("current")
if mibBuilder.loadTexts:
    outBr79.setUnits("tenth of Mbps")
_OutStream80_ObjectIdentity = ObjectIdentity
outStream80 = _OutStream80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 89)
)
_OutBr80_Type = Integer32
_OutBr80_Object = MibScalar
outBr80 = _OutBr80_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 89, 1),
    _OutBr80_Type()
)
outBr80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr80.setStatus("current")
if mibBuilder.loadTexts:
    outBr80.setUnits("tenth of Mbps")
_OutStream81_ObjectIdentity = ObjectIdentity
outStream81 = _OutStream81_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 90)
)
_OutBr81_Type = Integer32
_OutBr81_Object = MibScalar
outBr81 = _OutBr81_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 90, 1),
    _OutBr81_Type()
)
outBr81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr81.setStatus("current")
if mibBuilder.loadTexts:
    outBr81.setUnits("tenth of Mbps")
_OutStream82_ObjectIdentity = ObjectIdentity
outStream82 = _OutStream82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 91)
)
_OutBr82_Type = Integer32
_OutBr82_Object = MibScalar
outBr82 = _OutBr82_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 91, 1),
    _OutBr82_Type()
)
outBr82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr82.setStatus("current")
if mibBuilder.loadTexts:
    outBr82.setUnits("tenth of Mbps")
_OutStream83_ObjectIdentity = ObjectIdentity
outStream83 = _OutStream83_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 92)
)
_OutBr83_Type = Integer32
_OutBr83_Object = MibScalar
outBr83 = _OutBr83_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 92, 1),
    _OutBr83_Type()
)
outBr83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr83.setStatus("current")
if mibBuilder.loadTexts:
    outBr83.setUnits("tenth of Mbps")
_OutStream84_ObjectIdentity = ObjectIdentity
outStream84 = _OutStream84_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 93)
)
_OutBr84_Type = Integer32
_OutBr84_Object = MibScalar
outBr84 = _OutBr84_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 93, 1),
    _OutBr84_Type()
)
outBr84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr84.setStatus("current")
if mibBuilder.loadTexts:
    outBr84.setUnits("tenth of Mbps")
_OutStream85_ObjectIdentity = ObjectIdentity
outStream85 = _OutStream85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 94)
)
_OutBr85_Type = Integer32
_OutBr85_Object = MibScalar
outBr85 = _OutBr85_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 94, 1),
    _OutBr85_Type()
)
outBr85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr85.setStatus("current")
if mibBuilder.loadTexts:
    outBr85.setUnits("tenth of Mbps")
_OutStream86_ObjectIdentity = ObjectIdentity
outStream86 = _OutStream86_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 95)
)
_OutBr86_Type = Integer32
_OutBr86_Object = MibScalar
outBr86 = _OutBr86_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 95, 1),
    _OutBr86_Type()
)
outBr86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr86.setStatus("current")
if mibBuilder.loadTexts:
    outBr86.setUnits("tenth of Mbps")
_OutStream87_ObjectIdentity = ObjectIdentity
outStream87 = _OutStream87_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 96)
)
_OutBr87_Type = Integer32
_OutBr87_Object = MibScalar
outBr87 = _OutBr87_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 96, 1),
    _OutBr87_Type()
)
outBr87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr87.setStatus("current")
if mibBuilder.loadTexts:
    outBr87.setUnits("tenth of Mbps")
_OutStream88_ObjectIdentity = ObjectIdentity
outStream88 = _OutStream88_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 97)
)
_OutBr88_Type = Integer32
_OutBr88_Object = MibScalar
outBr88 = _OutBr88_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 97, 1),
    _OutBr88_Type()
)
outBr88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr88.setStatus("current")
if mibBuilder.loadTexts:
    outBr88.setUnits("tenth of Mbps")
_OutStream89_ObjectIdentity = ObjectIdentity
outStream89 = _OutStream89_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 98)
)
_OutBr89_Type = Integer32
_OutBr89_Object = MibScalar
outBr89 = _OutBr89_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 98, 1),
    _OutBr89_Type()
)
outBr89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr89.setStatus("current")
if mibBuilder.loadTexts:
    outBr89.setUnits("tenth of Mbps")
_OutStream90_ObjectIdentity = ObjectIdentity
outStream90 = _OutStream90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 99)
)
_OutBr90_Type = Integer32
_OutBr90_Object = MibScalar
outBr90 = _OutBr90_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 99, 1),
    _OutBr90_Type()
)
outBr90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr90.setStatus("current")
if mibBuilder.loadTexts:
    outBr90.setUnits("tenth of Mbps")
_OutStream91_ObjectIdentity = ObjectIdentity
outStream91 = _OutStream91_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 100)
)
_OutBr91_Type = Integer32
_OutBr91_Object = MibScalar
outBr91 = _OutBr91_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 100, 1),
    _OutBr91_Type()
)
outBr91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr91.setStatus("current")
if mibBuilder.loadTexts:
    outBr91.setUnits("tenth of Mbps")
_OutStream92_ObjectIdentity = ObjectIdentity
outStream92 = _OutStream92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 101)
)
_OutBr92_Type = Integer32
_OutBr92_Object = MibScalar
outBr92 = _OutBr92_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 101, 1),
    _OutBr92_Type()
)
outBr92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr92.setStatus("current")
if mibBuilder.loadTexts:
    outBr92.setUnits("tenth of Mbps")
_OutStream93_ObjectIdentity = ObjectIdentity
outStream93 = _OutStream93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 102)
)
_OutBr93_Type = Integer32
_OutBr93_Object = MibScalar
outBr93 = _OutBr93_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 102, 1),
    _OutBr93_Type()
)
outBr93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr93.setStatus("current")
if mibBuilder.loadTexts:
    outBr93.setUnits("tenth of Mbps")
_OutStream94_ObjectIdentity = ObjectIdentity
outStream94 = _OutStream94_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 103)
)
_OutBr94_Type = Integer32
_OutBr94_Object = MibScalar
outBr94 = _OutBr94_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 103, 1),
    _OutBr94_Type()
)
outBr94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr94.setStatus("current")
if mibBuilder.loadTexts:
    outBr94.setUnits("tenth of Mbps")
_OutStream95_ObjectIdentity = ObjectIdentity
outStream95 = _OutStream95_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 104)
)
_OutBr95_Type = Integer32
_OutBr95_Object = MibScalar
outBr95 = _OutBr95_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 104, 1),
    _OutBr95_Type()
)
outBr95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr95.setStatus("current")
if mibBuilder.loadTexts:
    outBr95.setUnits("tenth of Mbps")
_OutStream96_ObjectIdentity = ObjectIdentity
outStream96 = _OutStream96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 105)
)
_OutBr96_Type = Integer32
_OutBr96_Object = MibScalar
outBr96 = _OutBr96_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 105, 1),
    _OutBr96_Type()
)
outBr96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr96.setStatus("current")
if mibBuilder.loadTexts:
    outBr96.setUnits("tenth of Mbps")
_OutStream97_ObjectIdentity = ObjectIdentity
outStream97 = _OutStream97_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 106)
)
_OutBr97_Type = Integer32
_OutBr97_Object = MibScalar
outBr97 = _OutBr97_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 106, 1),
    _OutBr97_Type()
)
outBr97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr97.setStatus("current")
if mibBuilder.loadTexts:
    outBr97.setUnits("tenth of Mbps")
_OutStream98_ObjectIdentity = ObjectIdentity
outStream98 = _OutStream98_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 107)
)
_OutBr98_Type = Integer32
_OutBr98_Object = MibScalar
outBr98 = _OutBr98_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 107, 1),
    _OutBr98_Type()
)
outBr98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr98.setStatus("current")
if mibBuilder.loadTexts:
    outBr98.setUnits("tenth of Mbps")
_OutStream99_ObjectIdentity = ObjectIdentity
outStream99 = _OutStream99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 108)
)
_OutBr99_Type = Integer32
_OutBr99_Object = MibScalar
outBr99 = _OutBr99_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 108, 1),
    _OutBr99_Type()
)
outBr99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr99.setStatus("current")
if mibBuilder.loadTexts:
    outBr99.setUnits("tenth of Mbps")
_OutStream100_ObjectIdentity = ObjectIdentity
outStream100 = _OutStream100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 109)
)
_OutBr100_Type = Integer32
_OutBr100_Object = MibScalar
outBr100 = _OutBr100_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 109, 1),
    _OutBr100_Type()
)
outBr100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr100.setStatus("current")
if mibBuilder.loadTexts:
    outBr100.setUnits("tenth of Mbps")
_OutStream101_ObjectIdentity = ObjectIdentity
outStream101 = _OutStream101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 110)
)
_OutBr101_Type = Integer32
_OutBr101_Object = MibScalar
outBr101 = _OutBr101_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 110, 1),
    _OutBr101_Type()
)
outBr101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr101.setStatus("current")
if mibBuilder.loadTexts:
    outBr101.setUnits("tenth of Mbps")
_OutStream102_ObjectIdentity = ObjectIdentity
outStream102 = _OutStream102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 111)
)
_OutBr102_Type = Integer32
_OutBr102_Object = MibScalar
outBr102 = _OutBr102_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 111, 1),
    _OutBr102_Type()
)
outBr102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr102.setStatus("current")
if mibBuilder.loadTexts:
    outBr102.setUnits("tenth of Mbps")
_OutStream103_ObjectIdentity = ObjectIdentity
outStream103 = _OutStream103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 112)
)
_OutBr103_Type = Integer32
_OutBr103_Object = MibScalar
outBr103 = _OutBr103_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 112, 1),
    _OutBr103_Type()
)
outBr103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr103.setStatus("current")
if mibBuilder.loadTexts:
    outBr103.setUnits("tenth of Mbps")
_OutStream104_ObjectIdentity = ObjectIdentity
outStream104 = _OutStream104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 113)
)
_OutBr104_Type = Integer32
_OutBr104_Object = MibScalar
outBr104 = _OutBr104_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 113, 1),
    _OutBr104_Type()
)
outBr104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr104.setStatus("current")
if mibBuilder.loadTexts:
    outBr104.setUnits("tenth of Mbps")
_OutStream105_ObjectIdentity = ObjectIdentity
outStream105 = _OutStream105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 114)
)
_OutBr105_Type = Integer32
_OutBr105_Object = MibScalar
outBr105 = _OutBr105_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 114, 1),
    _OutBr105_Type()
)
outBr105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr105.setStatus("current")
if mibBuilder.loadTexts:
    outBr105.setUnits("tenth of Mbps")
_OutStream106_ObjectIdentity = ObjectIdentity
outStream106 = _OutStream106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 115)
)
_OutBr106_Type = Integer32
_OutBr106_Object = MibScalar
outBr106 = _OutBr106_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 115, 1),
    _OutBr106_Type()
)
outBr106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr106.setStatus("current")
if mibBuilder.loadTexts:
    outBr106.setUnits("tenth of Mbps")
_OutStream107_ObjectIdentity = ObjectIdentity
outStream107 = _OutStream107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 116)
)
_OutBr107_Type = Integer32
_OutBr107_Object = MibScalar
outBr107 = _OutBr107_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 116, 1),
    _OutBr107_Type()
)
outBr107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr107.setStatus("current")
if mibBuilder.loadTexts:
    outBr107.setUnits("tenth of Mbps")
_OutStream108_ObjectIdentity = ObjectIdentity
outStream108 = _OutStream108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 117)
)
_OutBr108_Type = Integer32
_OutBr108_Object = MibScalar
outBr108 = _OutBr108_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 117, 1),
    _OutBr108_Type()
)
outBr108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr108.setStatus("current")
if mibBuilder.loadTexts:
    outBr108.setUnits("tenth of Mbps")
_OutStream109_ObjectIdentity = ObjectIdentity
outStream109 = _OutStream109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 118)
)
_OutBr109_Type = Integer32
_OutBr109_Object = MibScalar
outBr109 = _OutBr109_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 118, 1),
    _OutBr109_Type()
)
outBr109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr109.setStatus("current")
if mibBuilder.loadTexts:
    outBr109.setUnits("tenth of Mbps")
_OutStream110_ObjectIdentity = ObjectIdentity
outStream110 = _OutStream110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 119)
)
_OutBr110_Type = Integer32
_OutBr110_Object = MibScalar
outBr110 = _OutBr110_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 119, 1),
    _OutBr110_Type()
)
outBr110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr110.setStatus("current")
if mibBuilder.loadTexts:
    outBr110.setUnits("tenth of Mbps")
_OutStream111_ObjectIdentity = ObjectIdentity
outStream111 = _OutStream111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 120)
)
_OutBr111_Type = Integer32
_OutBr111_Object = MibScalar
outBr111 = _OutBr111_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 120, 1),
    _OutBr111_Type()
)
outBr111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr111.setStatus("current")
if mibBuilder.loadTexts:
    outBr111.setUnits("tenth of Mbps")
_OutStream112_ObjectIdentity = ObjectIdentity
outStream112 = _OutStream112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 121)
)
_OutBr112_Type = Integer32
_OutBr112_Object = MibScalar
outBr112 = _OutBr112_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 121, 1),
    _OutBr112_Type()
)
outBr112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr112.setStatus("current")
if mibBuilder.loadTexts:
    outBr112.setUnits("tenth of Mbps")
_OutStream113_ObjectIdentity = ObjectIdentity
outStream113 = _OutStream113_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 122)
)
_OutBr113_Type = Integer32
_OutBr113_Object = MibScalar
outBr113 = _OutBr113_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 122, 1),
    _OutBr113_Type()
)
outBr113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr113.setStatus("current")
if mibBuilder.loadTexts:
    outBr113.setUnits("tenth of Mbps")
_OutStream114_ObjectIdentity = ObjectIdentity
outStream114 = _OutStream114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 123)
)
_OutBr114_Type = Integer32
_OutBr114_Object = MibScalar
outBr114 = _OutBr114_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 123, 1),
    _OutBr114_Type()
)
outBr114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr114.setStatus("current")
if mibBuilder.loadTexts:
    outBr114.setUnits("tenth of Mbps")
_OutStream115_ObjectIdentity = ObjectIdentity
outStream115 = _OutStream115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 124)
)
_OutBr115_Type = Integer32
_OutBr115_Object = MibScalar
outBr115 = _OutBr115_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 124, 1),
    _OutBr115_Type()
)
outBr115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr115.setStatus("current")
if mibBuilder.loadTexts:
    outBr115.setUnits("tenth of Mbps")
_OutStream116_ObjectIdentity = ObjectIdentity
outStream116 = _OutStream116_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 125)
)
_OutBr116_Type = Integer32
_OutBr116_Object = MibScalar
outBr116 = _OutBr116_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 125, 1),
    _OutBr116_Type()
)
outBr116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr116.setStatus("current")
if mibBuilder.loadTexts:
    outBr116.setUnits("tenth of Mbps")
_OutStream117_ObjectIdentity = ObjectIdentity
outStream117 = _OutStream117_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 126)
)
_OutBr117_Type = Integer32
_OutBr117_Object = MibScalar
outBr117 = _OutBr117_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 126, 1),
    _OutBr117_Type()
)
outBr117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr117.setStatus("current")
if mibBuilder.loadTexts:
    outBr117.setUnits("tenth of Mbps")
_OutStream118_ObjectIdentity = ObjectIdentity
outStream118 = _OutStream118_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 127)
)
_OutBr118_Type = Integer32
_OutBr118_Object = MibScalar
outBr118 = _OutBr118_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 127, 1),
    _OutBr118_Type()
)
outBr118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr118.setStatus("current")
if mibBuilder.loadTexts:
    outBr118.setUnits("tenth of Mbps")
_OutStream119_ObjectIdentity = ObjectIdentity
outStream119 = _OutStream119_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 128)
)
_OutBr119_Type = Integer32
_OutBr119_Object = MibScalar
outBr119 = _OutBr119_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 128, 1),
    _OutBr119_Type()
)
outBr119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr119.setStatus("current")
if mibBuilder.loadTexts:
    outBr119.setUnits("tenth of Mbps")
_OutStream120_ObjectIdentity = ObjectIdentity
outStream120 = _OutStream120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 129)
)
_OutBr120_Type = Integer32
_OutBr120_Object = MibScalar
outBr120 = _OutBr120_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 129, 1),
    _OutBr120_Type()
)
outBr120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr120.setStatus("current")
if mibBuilder.loadTexts:
    outBr120.setUnits("tenth of Mbps")
_OutStream121_ObjectIdentity = ObjectIdentity
outStream121 = _OutStream121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 130)
)
_OutBr121_Type = Integer32
_OutBr121_Object = MibScalar
outBr121 = _OutBr121_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 130, 1),
    _OutBr121_Type()
)
outBr121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr121.setStatus("current")
if mibBuilder.loadTexts:
    outBr121.setUnits("tenth of Mbps")
_OutStream122_ObjectIdentity = ObjectIdentity
outStream122 = _OutStream122_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 131)
)
_OutBr122_Type = Integer32
_OutBr122_Object = MibScalar
outBr122 = _OutBr122_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 131, 1),
    _OutBr122_Type()
)
outBr122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr122.setStatus("current")
if mibBuilder.loadTexts:
    outBr122.setUnits("tenth of Mbps")
_OutStream123_ObjectIdentity = ObjectIdentity
outStream123 = _OutStream123_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 132)
)
_OutBr123_Type = Integer32
_OutBr123_Object = MibScalar
outBr123 = _OutBr123_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 132, 1),
    _OutBr123_Type()
)
outBr123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr123.setStatus("current")
if mibBuilder.loadTexts:
    outBr123.setUnits("tenth of Mbps")
_OutStream124_ObjectIdentity = ObjectIdentity
outStream124 = _OutStream124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 133)
)
_OutBr124_Type = Integer32
_OutBr124_Object = MibScalar
outBr124 = _OutBr124_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 133, 1),
    _OutBr124_Type()
)
outBr124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr124.setStatus("current")
if mibBuilder.loadTexts:
    outBr124.setUnits("tenth of Mbps")
_OutStream125_ObjectIdentity = ObjectIdentity
outStream125 = _OutStream125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 134)
)
_OutBr125_Type = Integer32
_OutBr125_Object = MibScalar
outBr125 = _OutBr125_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 134, 1),
    _OutBr125_Type()
)
outBr125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr125.setStatus("current")
if mibBuilder.loadTexts:
    outBr125.setUnits("tenth of Mbps")
_OutStream126_ObjectIdentity = ObjectIdentity
outStream126 = _OutStream126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 135)
)
_OutBr126_Type = Integer32
_OutBr126_Object = MibScalar
outBr126 = _OutBr126_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 135, 1),
    _OutBr126_Type()
)
outBr126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr126.setStatus("current")
if mibBuilder.loadTexts:
    outBr126.setUnits("tenth of Mbps")
_OutStream127_ObjectIdentity = ObjectIdentity
outStream127 = _OutStream127_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 136)
)
_OutBr127_Type = Integer32
_OutBr127_Object = MibScalar
outBr127 = _OutBr127_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 136, 1),
    _OutBr127_Type()
)
outBr127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr127.setStatus("current")
if mibBuilder.loadTexts:
    outBr127.setUnits("tenth of Mbps")
_OutStream128_ObjectIdentity = ObjectIdentity
outStream128 = _OutStream128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 137)
)
_OutBr128_Type = Integer32
_OutBr128_Object = MibScalar
outBr128 = _OutBr128_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 137, 1),
    _OutBr128_Type()
)
outBr128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr128.setStatus("current")
if mibBuilder.loadTexts:
    outBr128.setUnits("tenth of Mbps")
_OutStream129_ObjectIdentity = ObjectIdentity
outStream129 = _OutStream129_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 138)
)
_OutBr129_Type = Integer32
_OutBr129_Object = MibScalar
outBr129 = _OutBr129_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 138, 1),
    _OutBr129_Type()
)
outBr129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr129.setStatus("current")
if mibBuilder.loadTexts:
    outBr129.setUnits("tenth of Mbps")
_OutStream130_ObjectIdentity = ObjectIdentity
outStream130 = _OutStream130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 139)
)
_OutBr130_Type = Integer32
_OutBr130_Object = MibScalar
outBr130 = _OutBr130_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 139, 1),
    _OutBr130_Type()
)
outBr130.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr130.setStatus("current")
if mibBuilder.loadTexts:
    outBr130.setUnits("tenth of Mbps")
_OutStream131_ObjectIdentity = ObjectIdentity
outStream131 = _OutStream131_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 140)
)
_OutBr131_Type = Integer32
_OutBr131_Object = MibScalar
outBr131 = _OutBr131_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 140, 1),
    _OutBr131_Type()
)
outBr131.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr131.setStatus("current")
if mibBuilder.loadTexts:
    outBr131.setUnits("tenth of Mbps")
_OutStream132_ObjectIdentity = ObjectIdentity
outStream132 = _OutStream132_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 141)
)
_OutBr132_Type = Integer32
_OutBr132_Object = MibScalar
outBr132 = _OutBr132_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 141, 1),
    _OutBr132_Type()
)
outBr132.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr132.setStatus("current")
if mibBuilder.loadTexts:
    outBr132.setUnits("tenth of Mbps")
_OutStream133_ObjectIdentity = ObjectIdentity
outStream133 = _OutStream133_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 142)
)
_OutBr133_Type = Integer32
_OutBr133_Object = MibScalar
outBr133 = _OutBr133_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 142, 1),
    _OutBr133_Type()
)
outBr133.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr133.setStatus("current")
if mibBuilder.loadTexts:
    outBr133.setUnits("tenth of Mbps")
_OutStream134_ObjectIdentity = ObjectIdentity
outStream134 = _OutStream134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 143)
)
_OutBr134_Type = Integer32
_OutBr134_Object = MibScalar
outBr134 = _OutBr134_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 143, 1),
    _OutBr134_Type()
)
outBr134.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr134.setStatus("current")
if mibBuilder.loadTexts:
    outBr134.setUnits("tenth of Mbps")
_OutStream135_ObjectIdentity = ObjectIdentity
outStream135 = _OutStream135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 144)
)
_OutBr135_Type = Integer32
_OutBr135_Object = MibScalar
outBr135 = _OutBr135_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 144, 1),
    _OutBr135_Type()
)
outBr135.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr135.setStatus("current")
if mibBuilder.loadTexts:
    outBr135.setUnits("tenth of Mbps")
_OutStream136_ObjectIdentity = ObjectIdentity
outStream136 = _OutStream136_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 145)
)
_OutBr136_Type = Integer32
_OutBr136_Object = MibScalar
outBr136 = _OutBr136_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 145, 1),
    _OutBr136_Type()
)
outBr136.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr136.setStatus("current")
if mibBuilder.loadTexts:
    outBr136.setUnits("tenth of Mbps")
_OutStream137_ObjectIdentity = ObjectIdentity
outStream137 = _OutStream137_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 146)
)
_OutBr137_Type = Integer32
_OutBr137_Object = MibScalar
outBr137 = _OutBr137_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 146, 1),
    _OutBr137_Type()
)
outBr137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr137.setStatus("current")
if mibBuilder.loadTexts:
    outBr137.setUnits("tenth of Mbps")
_OutStream138_ObjectIdentity = ObjectIdentity
outStream138 = _OutStream138_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 147)
)
_OutBr138_Type = Integer32
_OutBr138_Object = MibScalar
outBr138 = _OutBr138_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 147, 1),
    _OutBr138_Type()
)
outBr138.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr138.setStatus("current")
if mibBuilder.loadTexts:
    outBr138.setUnits("tenth of Mbps")
_OutStream139_ObjectIdentity = ObjectIdentity
outStream139 = _OutStream139_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 148)
)
_OutBr139_Type = Integer32
_OutBr139_Object = MibScalar
outBr139 = _OutBr139_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 148, 1),
    _OutBr139_Type()
)
outBr139.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr139.setStatus("current")
if mibBuilder.loadTexts:
    outBr139.setUnits("tenth of Mbps")
_OutStream140_ObjectIdentity = ObjectIdentity
outStream140 = _OutStream140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 149)
)
_OutBr140_Type = Integer32
_OutBr140_Object = MibScalar
outBr140 = _OutBr140_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 149, 1),
    _OutBr140_Type()
)
outBr140.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr140.setStatus("current")
if mibBuilder.loadTexts:
    outBr140.setUnits("tenth of Mbps")
_OutStream141_ObjectIdentity = ObjectIdentity
outStream141 = _OutStream141_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 150)
)
_OutBr141_Type = Integer32
_OutBr141_Object = MibScalar
outBr141 = _OutBr141_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 150, 1),
    _OutBr141_Type()
)
outBr141.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr141.setStatus("current")
if mibBuilder.loadTexts:
    outBr141.setUnits("tenth of Mbps")
_OutStream142_ObjectIdentity = ObjectIdentity
outStream142 = _OutStream142_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 151)
)
_OutBr142_Type = Integer32
_OutBr142_Object = MibScalar
outBr142 = _OutBr142_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 151, 1),
    _OutBr142_Type()
)
outBr142.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr142.setStatus("current")
if mibBuilder.loadTexts:
    outBr142.setUnits("tenth of Mbps")
_OutStream143_ObjectIdentity = ObjectIdentity
outStream143 = _OutStream143_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 152)
)
_OutBr143_Type = Integer32
_OutBr143_Object = MibScalar
outBr143 = _OutBr143_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 152, 1),
    _OutBr143_Type()
)
outBr143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr143.setStatus("current")
if mibBuilder.loadTexts:
    outBr143.setUnits("tenth of Mbps")
_OutStream144_ObjectIdentity = ObjectIdentity
outStream144 = _OutStream144_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 153)
)
_OutBr144_Type = Integer32
_OutBr144_Object = MibScalar
outBr144 = _OutBr144_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 153, 1),
    _OutBr144_Type()
)
outBr144.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr144.setStatus("current")
if mibBuilder.loadTexts:
    outBr144.setUnits("tenth of Mbps")
_OutStream145_ObjectIdentity = ObjectIdentity
outStream145 = _OutStream145_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 154)
)
_OutBr145_Type = Integer32
_OutBr145_Object = MibScalar
outBr145 = _OutBr145_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 154, 1),
    _OutBr145_Type()
)
outBr145.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr145.setStatus("current")
if mibBuilder.loadTexts:
    outBr145.setUnits("tenth of Mbps")
_OutStream146_ObjectIdentity = ObjectIdentity
outStream146 = _OutStream146_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 155)
)
_OutBr146_Type = Integer32
_OutBr146_Object = MibScalar
outBr146 = _OutBr146_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 155, 1),
    _OutBr146_Type()
)
outBr146.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr146.setStatus("current")
if mibBuilder.loadTexts:
    outBr146.setUnits("tenth of Mbps")
_OutStream147_ObjectIdentity = ObjectIdentity
outStream147 = _OutStream147_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 156)
)
_OutBr147_Type = Integer32
_OutBr147_Object = MibScalar
outBr147 = _OutBr147_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 156, 1),
    _OutBr147_Type()
)
outBr147.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr147.setStatus("current")
if mibBuilder.loadTexts:
    outBr147.setUnits("tenth of Mbps")
_OutStream148_ObjectIdentity = ObjectIdentity
outStream148 = _OutStream148_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 157)
)
_OutBr148_Type = Integer32
_OutBr148_Object = MibScalar
outBr148 = _OutBr148_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 157, 1),
    _OutBr148_Type()
)
outBr148.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr148.setStatus("current")
if mibBuilder.loadTexts:
    outBr148.setUnits("tenth of Mbps")
_OutStream149_ObjectIdentity = ObjectIdentity
outStream149 = _OutStream149_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 158)
)
_OutBr149_Type = Integer32
_OutBr149_Object = MibScalar
outBr149 = _OutBr149_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 158, 1),
    _OutBr149_Type()
)
outBr149.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr149.setStatus("current")
if mibBuilder.loadTexts:
    outBr149.setUnits("tenth of Mbps")
_OutStream150_ObjectIdentity = ObjectIdentity
outStream150 = _OutStream150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 159)
)
_OutBr150_Type = Integer32
_OutBr150_Object = MibScalar
outBr150 = _OutBr150_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 159, 1),
    _OutBr150_Type()
)
outBr150.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr150.setStatus("current")
if mibBuilder.loadTexts:
    outBr150.setUnits("tenth of Mbps")
_OutStream151_ObjectIdentity = ObjectIdentity
outStream151 = _OutStream151_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 160)
)
_OutBr151_Type = Integer32
_OutBr151_Object = MibScalar
outBr151 = _OutBr151_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 160, 1),
    _OutBr151_Type()
)
outBr151.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr151.setStatus("current")
if mibBuilder.loadTexts:
    outBr151.setUnits("tenth of Mbps")
_OutStream152_ObjectIdentity = ObjectIdentity
outStream152 = _OutStream152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 161)
)
_OutBr152_Type = Integer32
_OutBr152_Object = MibScalar
outBr152 = _OutBr152_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 161, 1),
    _OutBr152_Type()
)
outBr152.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr152.setStatus("current")
if mibBuilder.loadTexts:
    outBr152.setUnits("tenth of Mbps")
_OutStream153_ObjectIdentity = ObjectIdentity
outStream153 = _OutStream153_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 162)
)
_OutBr153_Type = Integer32
_OutBr153_Object = MibScalar
outBr153 = _OutBr153_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 162, 1),
    _OutBr153_Type()
)
outBr153.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr153.setStatus("current")
if mibBuilder.loadTexts:
    outBr153.setUnits("tenth of Mbps")
_OutStream154_ObjectIdentity = ObjectIdentity
outStream154 = _OutStream154_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 163)
)
_OutBr154_Type = Integer32
_OutBr154_Object = MibScalar
outBr154 = _OutBr154_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 163, 1),
    _OutBr154_Type()
)
outBr154.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr154.setStatus("current")
if mibBuilder.loadTexts:
    outBr154.setUnits("tenth of Mbps")
_OutStream155_ObjectIdentity = ObjectIdentity
outStream155 = _OutStream155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 164)
)
_OutBr155_Type = Integer32
_OutBr155_Object = MibScalar
outBr155 = _OutBr155_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 164, 1),
    _OutBr155_Type()
)
outBr155.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr155.setStatus("current")
if mibBuilder.loadTexts:
    outBr155.setUnits("tenth of Mbps")
_OutStream156_ObjectIdentity = ObjectIdentity
outStream156 = _OutStream156_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 165)
)
_OutBr156_Type = Integer32
_OutBr156_Object = MibScalar
outBr156 = _OutBr156_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 165, 1),
    _OutBr156_Type()
)
outBr156.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr156.setStatus("current")
if mibBuilder.loadTexts:
    outBr156.setUnits("tenth of Mbps")
_OutStream157_ObjectIdentity = ObjectIdentity
outStream157 = _OutStream157_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 166)
)
_OutBr157_Type = Integer32
_OutBr157_Object = MibScalar
outBr157 = _OutBr157_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 166, 1),
    _OutBr157_Type()
)
outBr157.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr157.setStatus("current")
if mibBuilder.loadTexts:
    outBr157.setUnits("tenth of Mbps")
_OutStream158_ObjectIdentity = ObjectIdentity
outStream158 = _OutStream158_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 167)
)
_OutBr158_Type = Integer32
_OutBr158_Object = MibScalar
outBr158 = _OutBr158_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 167, 1),
    _OutBr158_Type()
)
outBr158.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr158.setStatus("current")
if mibBuilder.loadTexts:
    outBr158.setUnits("tenth of Mbps")
_OutStream159_ObjectIdentity = ObjectIdentity
outStream159 = _OutStream159_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 168)
)
_OutBr159_Type = Integer32
_OutBr159_Object = MibScalar
outBr159 = _OutBr159_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 168, 1),
    _OutBr159_Type()
)
outBr159.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr159.setStatus("current")
if mibBuilder.loadTexts:
    outBr159.setUnits("tenth of Mbps")
_OutStream160_ObjectIdentity = ObjectIdentity
outStream160 = _OutStream160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 169)
)
_OutBr160_Type = Integer32
_OutBr160_Object = MibScalar
outBr160 = _OutBr160_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 169, 1),
    _OutBr160_Type()
)
outBr160.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr160.setStatus("current")
if mibBuilder.loadTexts:
    outBr160.setUnits("tenth of Mbps")
_OutStream161_ObjectIdentity = ObjectIdentity
outStream161 = _OutStream161_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 170)
)
_OutBr161_Type = Integer32
_OutBr161_Object = MibScalar
outBr161 = _OutBr161_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 170, 1),
    _OutBr161_Type()
)
outBr161.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr161.setStatus("current")
if mibBuilder.loadTexts:
    outBr161.setUnits("tenth of Mbps")
_OutStream162_ObjectIdentity = ObjectIdentity
outStream162 = _OutStream162_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 171)
)
_OutBr162_Type = Integer32
_OutBr162_Object = MibScalar
outBr162 = _OutBr162_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 171, 1),
    _OutBr162_Type()
)
outBr162.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr162.setStatus("current")
if mibBuilder.loadTexts:
    outBr162.setUnits("tenth of Mbps")
_OutStream163_ObjectIdentity = ObjectIdentity
outStream163 = _OutStream163_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 172)
)
_OutBr163_Type = Integer32
_OutBr163_Object = MibScalar
outBr163 = _OutBr163_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 172, 1),
    _OutBr163_Type()
)
outBr163.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr163.setStatus("current")
if mibBuilder.loadTexts:
    outBr163.setUnits("tenth of Mbps")
_OutStream164_ObjectIdentity = ObjectIdentity
outStream164 = _OutStream164_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 173)
)
_OutBr164_Type = Integer32
_OutBr164_Object = MibScalar
outBr164 = _OutBr164_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 173, 1),
    _OutBr164_Type()
)
outBr164.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr164.setStatus("current")
if mibBuilder.loadTexts:
    outBr164.setUnits("tenth of Mbps")
_OutStream165_ObjectIdentity = ObjectIdentity
outStream165 = _OutStream165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 174)
)
_OutBr165_Type = Integer32
_OutBr165_Object = MibScalar
outBr165 = _OutBr165_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 174, 1),
    _OutBr165_Type()
)
outBr165.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr165.setStatus("current")
if mibBuilder.loadTexts:
    outBr165.setUnits("tenth of Mbps")
_OutStream166_ObjectIdentity = ObjectIdentity
outStream166 = _OutStream166_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 175)
)
_OutBr166_Type = Integer32
_OutBr166_Object = MibScalar
outBr166 = _OutBr166_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 175, 1),
    _OutBr166_Type()
)
outBr166.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr166.setStatus("current")
if mibBuilder.loadTexts:
    outBr166.setUnits("tenth of Mbps")
_OutStream167_ObjectIdentity = ObjectIdentity
outStream167 = _OutStream167_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 176)
)
_OutBr167_Type = Integer32
_OutBr167_Object = MibScalar
outBr167 = _OutBr167_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 176, 1),
    _OutBr167_Type()
)
outBr167.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr167.setStatus("current")
if mibBuilder.loadTexts:
    outBr167.setUnits("tenth of Mbps")
_OutStream168_ObjectIdentity = ObjectIdentity
outStream168 = _OutStream168_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 177)
)
_OutBr168_Type = Integer32
_OutBr168_Object = MibScalar
outBr168 = _OutBr168_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 177, 1),
    _OutBr168_Type()
)
outBr168.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr168.setStatus("current")
if mibBuilder.loadTexts:
    outBr168.setUnits("tenth of Mbps")
_OutStream169_ObjectIdentity = ObjectIdentity
outStream169 = _OutStream169_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 178)
)
_OutBr169_Type = Integer32
_OutBr169_Object = MibScalar
outBr169 = _OutBr169_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 178, 1),
    _OutBr169_Type()
)
outBr169.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr169.setStatus("current")
if mibBuilder.loadTexts:
    outBr169.setUnits("tenth of Mbps")
_OutStream170_ObjectIdentity = ObjectIdentity
outStream170 = _OutStream170_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 179)
)
_OutBr170_Type = Integer32
_OutBr170_Object = MibScalar
outBr170 = _OutBr170_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 179, 1),
    _OutBr170_Type()
)
outBr170.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr170.setStatus("current")
if mibBuilder.loadTexts:
    outBr170.setUnits("tenth of Mbps")
_OutStream171_ObjectIdentity = ObjectIdentity
outStream171 = _OutStream171_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 180)
)
_OutBr171_Type = Integer32
_OutBr171_Object = MibScalar
outBr171 = _OutBr171_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 180, 1),
    _OutBr171_Type()
)
outBr171.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr171.setStatus("current")
if mibBuilder.loadTexts:
    outBr171.setUnits("tenth of Mbps")
_OutStream172_ObjectIdentity = ObjectIdentity
outStream172 = _OutStream172_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 181)
)
_OutBr172_Type = Integer32
_OutBr172_Object = MibScalar
outBr172 = _OutBr172_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 181, 1),
    _OutBr172_Type()
)
outBr172.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr172.setStatus("current")
if mibBuilder.loadTexts:
    outBr172.setUnits("tenth of Mbps")
_OutStream173_ObjectIdentity = ObjectIdentity
outStream173 = _OutStream173_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 182)
)
_OutBr173_Type = Integer32
_OutBr173_Object = MibScalar
outBr173 = _OutBr173_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 182, 1),
    _OutBr173_Type()
)
outBr173.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr173.setStatus("current")
if mibBuilder.loadTexts:
    outBr173.setUnits("tenth of Mbps")
_OutStream174_ObjectIdentity = ObjectIdentity
outStream174 = _OutStream174_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 183)
)
_OutBr174_Type = Integer32
_OutBr174_Object = MibScalar
outBr174 = _OutBr174_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 183, 1),
    _OutBr174_Type()
)
outBr174.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr174.setStatus("current")
if mibBuilder.loadTexts:
    outBr174.setUnits("tenth of Mbps")
_OutStream175_ObjectIdentity = ObjectIdentity
outStream175 = _OutStream175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 184)
)
_OutBr175_Type = Integer32
_OutBr175_Object = MibScalar
outBr175 = _OutBr175_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 184, 1),
    _OutBr175_Type()
)
outBr175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr175.setStatus("current")
if mibBuilder.loadTexts:
    outBr175.setUnits("tenth of Mbps")
_OutStream176_ObjectIdentity = ObjectIdentity
outStream176 = _OutStream176_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 185)
)
_OutBr176_Type = Integer32
_OutBr176_Object = MibScalar
outBr176 = _OutBr176_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 185, 1),
    _OutBr176_Type()
)
outBr176.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr176.setStatus("current")
if mibBuilder.loadTexts:
    outBr176.setUnits("tenth of Mbps")
_OutStream177_ObjectIdentity = ObjectIdentity
outStream177 = _OutStream177_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 186)
)
_OutBr177_Type = Integer32
_OutBr177_Object = MibScalar
outBr177 = _OutBr177_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 186, 1),
    _OutBr177_Type()
)
outBr177.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr177.setStatus("current")
if mibBuilder.loadTexts:
    outBr177.setUnits("tenth of Mbps")
_OutStream178_ObjectIdentity = ObjectIdentity
outStream178 = _OutStream178_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 187)
)
_OutBr178_Type = Integer32
_OutBr178_Object = MibScalar
outBr178 = _OutBr178_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 187, 1),
    _OutBr178_Type()
)
outBr178.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr178.setStatus("current")
if mibBuilder.loadTexts:
    outBr178.setUnits("tenth of Mbps")
_OutStream179_ObjectIdentity = ObjectIdentity
outStream179 = _OutStream179_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 188)
)
_OutBr179_Type = Integer32
_OutBr179_Object = MibScalar
outBr179 = _OutBr179_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 188, 1),
    _OutBr179_Type()
)
outBr179.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr179.setStatus("current")
if mibBuilder.loadTexts:
    outBr179.setUnits("tenth of Mbps")
_OutStream180_ObjectIdentity = ObjectIdentity
outStream180 = _OutStream180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 189)
)
_OutBr180_Type = Integer32
_OutBr180_Object = MibScalar
outBr180 = _OutBr180_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 189, 1),
    _OutBr180_Type()
)
outBr180.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr180.setStatus("current")
if mibBuilder.loadTexts:
    outBr180.setUnits("tenth of Mbps")
_OutStream181_ObjectIdentity = ObjectIdentity
outStream181 = _OutStream181_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 190)
)
_OutBr181_Type = Integer32
_OutBr181_Object = MibScalar
outBr181 = _OutBr181_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 190, 1),
    _OutBr181_Type()
)
outBr181.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr181.setStatus("current")
if mibBuilder.loadTexts:
    outBr181.setUnits("tenth of Mbps")
_OutStream182_ObjectIdentity = ObjectIdentity
outStream182 = _OutStream182_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 191)
)
_OutBr182_Type = Integer32
_OutBr182_Object = MibScalar
outBr182 = _OutBr182_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 191, 1),
    _OutBr182_Type()
)
outBr182.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr182.setStatus("current")
if mibBuilder.loadTexts:
    outBr182.setUnits("tenth of Mbps")
_OutStream183_ObjectIdentity = ObjectIdentity
outStream183 = _OutStream183_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 192)
)
_OutBr183_Type = Integer32
_OutBr183_Object = MibScalar
outBr183 = _OutBr183_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 192, 1),
    _OutBr183_Type()
)
outBr183.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr183.setStatus("current")
if mibBuilder.loadTexts:
    outBr183.setUnits("tenth of Mbps")
_OutStream184_ObjectIdentity = ObjectIdentity
outStream184 = _OutStream184_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 193)
)
_OutBr184_Type = Integer32
_OutBr184_Object = MibScalar
outBr184 = _OutBr184_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 193, 1),
    _OutBr184_Type()
)
outBr184.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr184.setStatus("current")
if mibBuilder.loadTexts:
    outBr184.setUnits("tenth of Mbps")
_OutStream185_ObjectIdentity = ObjectIdentity
outStream185 = _OutStream185_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 194)
)
_OutBr185_Type = Integer32
_OutBr185_Object = MibScalar
outBr185 = _OutBr185_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 194, 1),
    _OutBr185_Type()
)
outBr185.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr185.setStatus("current")
if mibBuilder.loadTexts:
    outBr185.setUnits("tenth of Mbps")
_OutStream186_ObjectIdentity = ObjectIdentity
outStream186 = _OutStream186_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 195)
)
_OutBr186_Type = Integer32
_OutBr186_Object = MibScalar
outBr186 = _OutBr186_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 195, 1),
    _OutBr186_Type()
)
outBr186.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr186.setStatus("current")
if mibBuilder.loadTexts:
    outBr186.setUnits("tenth of Mbps")
_OutStream187_ObjectIdentity = ObjectIdentity
outStream187 = _OutStream187_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 196)
)
_OutBr187_Type = Integer32
_OutBr187_Object = MibScalar
outBr187 = _OutBr187_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 196, 1),
    _OutBr187_Type()
)
outBr187.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr187.setStatus("current")
if mibBuilder.loadTexts:
    outBr187.setUnits("tenth of Mbps")
_OutStream188_ObjectIdentity = ObjectIdentity
outStream188 = _OutStream188_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 197)
)
_OutBr188_Type = Integer32
_OutBr188_Object = MibScalar
outBr188 = _OutBr188_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 197, 1),
    _OutBr188_Type()
)
outBr188.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr188.setStatus("current")
if mibBuilder.loadTexts:
    outBr188.setUnits("tenth of Mbps")
_OutStream189_ObjectIdentity = ObjectIdentity
outStream189 = _OutStream189_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 198)
)
_OutBr189_Type = Integer32
_OutBr189_Object = MibScalar
outBr189 = _OutBr189_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 198, 1),
    _OutBr189_Type()
)
outBr189.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr189.setStatus("current")
if mibBuilder.loadTexts:
    outBr189.setUnits("tenth of Mbps")
_OutStream190_ObjectIdentity = ObjectIdentity
outStream190 = _OutStream190_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 199)
)
_OutBr190_Type = Integer32
_OutBr190_Object = MibScalar
outBr190 = _OutBr190_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 199, 1),
    _OutBr190_Type()
)
outBr190.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr190.setStatus("current")
if mibBuilder.loadTexts:
    outBr190.setUnits("tenth of Mbps")
_OutStream191_ObjectIdentity = ObjectIdentity
outStream191 = _OutStream191_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 200)
)
_OutBr191_Type = Integer32
_OutBr191_Object = MibScalar
outBr191 = _OutBr191_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 200, 1),
    _OutBr191_Type()
)
outBr191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr191.setStatus("current")
if mibBuilder.loadTexts:
    outBr191.setUnits("tenth of Mbps")
_OutStream192_ObjectIdentity = ObjectIdentity
outStream192 = _OutStream192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 201)
)
_OutBr192_Type = Integer32
_OutBr192_Object = MibScalar
outBr192 = _OutBr192_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 201, 1),
    _OutBr192_Type()
)
outBr192.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr192.setStatus("current")
if mibBuilder.loadTexts:
    outBr192.setUnits("tenth of Mbps")
_OutStream193_ObjectIdentity = ObjectIdentity
outStream193 = _OutStream193_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 202)
)
_OutBr193_Type = Integer32
_OutBr193_Object = MibScalar
outBr193 = _OutBr193_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 202, 1),
    _OutBr193_Type()
)
outBr193.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr193.setStatus("current")
if mibBuilder.loadTexts:
    outBr193.setUnits("tenth of Mbps")
_OutStream194_ObjectIdentity = ObjectIdentity
outStream194 = _OutStream194_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 203)
)
_OutBr194_Type = Integer32
_OutBr194_Object = MibScalar
outBr194 = _OutBr194_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 203, 1),
    _OutBr194_Type()
)
outBr194.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr194.setStatus("current")
if mibBuilder.loadTexts:
    outBr194.setUnits("tenth of Mbps")
_OutStream195_ObjectIdentity = ObjectIdentity
outStream195 = _OutStream195_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 204)
)
_OutBr195_Type = Integer32
_OutBr195_Object = MibScalar
outBr195 = _OutBr195_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 204, 1),
    _OutBr195_Type()
)
outBr195.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr195.setStatus("current")
if mibBuilder.loadTexts:
    outBr195.setUnits("tenth of Mbps")
_OutStream196_ObjectIdentity = ObjectIdentity
outStream196 = _OutStream196_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 205)
)
_OutBr196_Type = Integer32
_OutBr196_Object = MibScalar
outBr196 = _OutBr196_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 205, 1),
    _OutBr196_Type()
)
outBr196.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr196.setStatus("current")
if mibBuilder.loadTexts:
    outBr196.setUnits("tenth of Mbps")
_OutStream197_ObjectIdentity = ObjectIdentity
outStream197 = _OutStream197_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 206)
)
_OutBr197_Type = Integer32
_OutBr197_Object = MibScalar
outBr197 = _OutBr197_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 206, 1),
    _OutBr197_Type()
)
outBr197.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr197.setStatus("current")
if mibBuilder.loadTexts:
    outBr197.setUnits("tenth of Mbps")
_OutStream198_ObjectIdentity = ObjectIdentity
outStream198 = _OutStream198_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 207)
)
_OutBr198_Type = Integer32
_OutBr198_Object = MibScalar
outBr198 = _OutBr198_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 207, 1),
    _OutBr198_Type()
)
outBr198.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr198.setStatus("current")
if mibBuilder.loadTexts:
    outBr198.setUnits("tenth of Mbps")
_OutStream199_ObjectIdentity = ObjectIdentity
outStream199 = _OutStream199_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 208)
)
_OutBr199_Type = Integer32
_OutBr199_Object = MibScalar
outBr199 = _OutBr199_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 208, 1),
    _OutBr199_Type()
)
outBr199.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr199.setStatus("current")
if mibBuilder.loadTexts:
    outBr199.setUnits("tenth of Mbps")
_OutStream200_ObjectIdentity = ObjectIdentity
outStream200 = _OutStream200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 209)
)
_OutBr200_Type = Integer32
_OutBr200_Object = MibScalar
outBr200 = _OutBr200_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 209, 1),
    _OutBr200_Type()
)
outBr200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr200.setStatus("current")
if mibBuilder.loadTexts:
    outBr200.setUnits("tenth of Mbps")
_OutStream201_ObjectIdentity = ObjectIdentity
outStream201 = _OutStream201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 210)
)
_OutBr201_Type = Integer32
_OutBr201_Object = MibScalar
outBr201 = _OutBr201_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 210, 1),
    _OutBr201_Type()
)
outBr201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr201.setStatus("current")
if mibBuilder.loadTexts:
    outBr201.setUnits("tenth of Mbps")
_OutStream202_ObjectIdentity = ObjectIdentity
outStream202 = _OutStream202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 211)
)
_OutBr202_Type = Integer32
_OutBr202_Object = MibScalar
outBr202 = _OutBr202_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 211, 1),
    _OutBr202_Type()
)
outBr202.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr202.setStatus("current")
if mibBuilder.loadTexts:
    outBr202.setUnits("tenth of Mbps")
_OutStream203_ObjectIdentity = ObjectIdentity
outStream203 = _OutStream203_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 212)
)
_OutBr203_Type = Integer32
_OutBr203_Object = MibScalar
outBr203 = _OutBr203_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 212, 1),
    _OutBr203_Type()
)
outBr203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr203.setStatus("current")
if mibBuilder.loadTexts:
    outBr203.setUnits("tenth of Mbps")
_OutStream204_ObjectIdentity = ObjectIdentity
outStream204 = _OutStream204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 213)
)
_OutBr204_Type = Integer32
_OutBr204_Object = MibScalar
outBr204 = _OutBr204_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 213, 1),
    _OutBr204_Type()
)
outBr204.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr204.setStatus("current")
if mibBuilder.loadTexts:
    outBr204.setUnits("tenth of Mbps")
_OutStream205_ObjectIdentity = ObjectIdentity
outStream205 = _OutStream205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 214)
)
_OutBr205_Type = Integer32
_OutBr205_Object = MibScalar
outBr205 = _OutBr205_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 214, 1),
    _OutBr205_Type()
)
outBr205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr205.setStatus("current")
if mibBuilder.loadTexts:
    outBr205.setUnits("tenth of Mbps")
_OutStream206_ObjectIdentity = ObjectIdentity
outStream206 = _OutStream206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 215)
)
_OutBr206_Type = Integer32
_OutBr206_Object = MibScalar
outBr206 = _OutBr206_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 215, 1),
    _OutBr206_Type()
)
outBr206.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr206.setStatus("current")
if mibBuilder.loadTexts:
    outBr206.setUnits("tenth of Mbps")
_OutStream207_ObjectIdentity = ObjectIdentity
outStream207 = _OutStream207_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 216)
)
_OutBr207_Type = Integer32
_OutBr207_Object = MibScalar
outBr207 = _OutBr207_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 216, 1),
    _OutBr207_Type()
)
outBr207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr207.setStatus("current")
if mibBuilder.loadTexts:
    outBr207.setUnits("tenth of Mbps")
_OutStream208_ObjectIdentity = ObjectIdentity
outStream208 = _OutStream208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 217)
)
_OutBr208_Type = Integer32
_OutBr208_Object = MibScalar
outBr208 = _OutBr208_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 217, 1),
    _OutBr208_Type()
)
outBr208.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr208.setStatus("current")
if mibBuilder.loadTexts:
    outBr208.setUnits("tenth of Mbps")
_OutStream209_ObjectIdentity = ObjectIdentity
outStream209 = _OutStream209_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 218)
)
_OutBr209_Type = Integer32
_OutBr209_Object = MibScalar
outBr209 = _OutBr209_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 218, 1),
    _OutBr209_Type()
)
outBr209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr209.setStatus("current")
if mibBuilder.loadTexts:
    outBr209.setUnits("tenth of Mbps")
_OutStream210_ObjectIdentity = ObjectIdentity
outStream210 = _OutStream210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 219)
)
_OutBr210_Type = Integer32
_OutBr210_Object = MibScalar
outBr210 = _OutBr210_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 219, 1),
    _OutBr210_Type()
)
outBr210.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr210.setStatus("current")
if mibBuilder.loadTexts:
    outBr210.setUnits("tenth of Mbps")
_OutStream211_ObjectIdentity = ObjectIdentity
outStream211 = _OutStream211_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 220)
)
_OutBr211_Type = Integer32
_OutBr211_Object = MibScalar
outBr211 = _OutBr211_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 220, 1),
    _OutBr211_Type()
)
outBr211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr211.setStatus("current")
if mibBuilder.loadTexts:
    outBr211.setUnits("tenth of Mbps")
_OutStream212_ObjectIdentity = ObjectIdentity
outStream212 = _OutStream212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 221)
)
_OutBr212_Type = Integer32
_OutBr212_Object = MibScalar
outBr212 = _OutBr212_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 221, 1),
    _OutBr212_Type()
)
outBr212.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr212.setStatus("current")
if mibBuilder.loadTexts:
    outBr212.setUnits("tenth of Mbps")
_OutStream213_ObjectIdentity = ObjectIdentity
outStream213 = _OutStream213_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 222)
)
_OutBr213_Type = Integer32
_OutBr213_Object = MibScalar
outBr213 = _OutBr213_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 222, 1),
    _OutBr213_Type()
)
outBr213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr213.setStatus("current")
if mibBuilder.loadTexts:
    outBr213.setUnits("tenth of Mbps")
_OutStream214_ObjectIdentity = ObjectIdentity
outStream214 = _OutStream214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 223)
)
_OutBr214_Type = Integer32
_OutBr214_Object = MibScalar
outBr214 = _OutBr214_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 223, 1),
    _OutBr214_Type()
)
outBr214.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr214.setStatus("current")
if mibBuilder.loadTexts:
    outBr214.setUnits("tenth of Mbps")
_OutStream215_ObjectIdentity = ObjectIdentity
outStream215 = _OutStream215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 224)
)
_OutBr215_Type = Integer32
_OutBr215_Object = MibScalar
outBr215 = _OutBr215_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 224, 1),
    _OutBr215_Type()
)
outBr215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr215.setStatus("current")
if mibBuilder.loadTexts:
    outBr215.setUnits("tenth of Mbps")
_OutStream216_ObjectIdentity = ObjectIdentity
outStream216 = _OutStream216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 225)
)
_OutBr216_Type = Integer32
_OutBr216_Object = MibScalar
outBr216 = _OutBr216_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 225, 1),
    _OutBr216_Type()
)
outBr216.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr216.setStatus("current")
if mibBuilder.loadTexts:
    outBr216.setUnits("tenth of Mbps")
_OutStream217_ObjectIdentity = ObjectIdentity
outStream217 = _OutStream217_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 226)
)
_OutBr217_Type = Integer32
_OutBr217_Object = MibScalar
outBr217 = _OutBr217_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 226, 1),
    _OutBr217_Type()
)
outBr217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr217.setStatus("current")
if mibBuilder.loadTexts:
    outBr217.setUnits("tenth of Mbps")
_OutStream218_ObjectIdentity = ObjectIdentity
outStream218 = _OutStream218_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 227)
)
_OutBr218_Type = Integer32
_OutBr218_Object = MibScalar
outBr218 = _OutBr218_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 227, 1),
    _OutBr218_Type()
)
outBr218.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr218.setStatus("current")
if mibBuilder.loadTexts:
    outBr218.setUnits("tenth of Mbps")
_OutStream219_ObjectIdentity = ObjectIdentity
outStream219 = _OutStream219_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 228)
)
_OutBr219_Type = Integer32
_OutBr219_Object = MibScalar
outBr219 = _OutBr219_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 228, 1),
    _OutBr219_Type()
)
outBr219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr219.setStatus("current")
if mibBuilder.loadTexts:
    outBr219.setUnits("tenth of Mbps")
_OutStream220_ObjectIdentity = ObjectIdentity
outStream220 = _OutStream220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 229)
)
_OutBr220_Type = Integer32
_OutBr220_Object = MibScalar
outBr220 = _OutBr220_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 229, 1),
    _OutBr220_Type()
)
outBr220.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr220.setStatus("current")
if mibBuilder.loadTexts:
    outBr220.setUnits("tenth of Mbps")
_OutStream221_ObjectIdentity = ObjectIdentity
outStream221 = _OutStream221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 230)
)
_OutBr221_Type = Integer32
_OutBr221_Object = MibScalar
outBr221 = _OutBr221_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 230, 1),
    _OutBr221_Type()
)
outBr221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr221.setStatus("current")
if mibBuilder.loadTexts:
    outBr221.setUnits("tenth of Mbps")
_OutStream222_ObjectIdentity = ObjectIdentity
outStream222 = _OutStream222_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 231)
)
_OutBr222_Type = Integer32
_OutBr222_Object = MibScalar
outBr222 = _OutBr222_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 231, 1),
    _OutBr222_Type()
)
outBr222.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr222.setStatus("current")
if mibBuilder.loadTexts:
    outBr222.setUnits("tenth of Mbps")
_OutStream223_ObjectIdentity = ObjectIdentity
outStream223 = _OutStream223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 232)
)
_OutBr223_Type = Integer32
_OutBr223_Object = MibScalar
outBr223 = _OutBr223_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 232, 1),
    _OutBr223_Type()
)
outBr223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr223.setStatus("current")
if mibBuilder.loadTexts:
    outBr223.setUnits("tenth of Mbps")
_OutStream224_ObjectIdentity = ObjectIdentity
outStream224 = _OutStream224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 233)
)
_OutBr224_Type = Integer32
_OutBr224_Object = MibScalar
outBr224 = _OutBr224_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 233, 1),
    _OutBr224_Type()
)
outBr224.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr224.setStatus("current")
if mibBuilder.loadTexts:
    outBr224.setUnits("tenth of Mbps")
_OutStream225_ObjectIdentity = ObjectIdentity
outStream225 = _OutStream225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 234)
)
_OutBr225_Type = Integer32
_OutBr225_Object = MibScalar
outBr225 = _OutBr225_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 234, 1),
    _OutBr225_Type()
)
outBr225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr225.setStatus("current")
if mibBuilder.loadTexts:
    outBr225.setUnits("tenth of Mbps")
_OutStream226_ObjectIdentity = ObjectIdentity
outStream226 = _OutStream226_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 235)
)
_OutBr226_Type = Integer32
_OutBr226_Object = MibScalar
outBr226 = _OutBr226_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 235, 1),
    _OutBr226_Type()
)
outBr226.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr226.setStatus("current")
if mibBuilder.loadTexts:
    outBr226.setUnits("tenth of Mbps")
_OutStream227_ObjectIdentity = ObjectIdentity
outStream227 = _OutStream227_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 236)
)
_OutBr227_Type = Integer32
_OutBr227_Object = MibScalar
outBr227 = _OutBr227_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 236, 1),
    _OutBr227_Type()
)
outBr227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr227.setStatus("current")
if mibBuilder.loadTexts:
    outBr227.setUnits("tenth of Mbps")
_OutStream228_ObjectIdentity = ObjectIdentity
outStream228 = _OutStream228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 237)
)
_OutBr228_Type = Integer32
_OutBr228_Object = MibScalar
outBr228 = _OutBr228_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 237, 1),
    _OutBr228_Type()
)
outBr228.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr228.setStatus("current")
if mibBuilder.loadTexts:
    outBr228.setUnits("tenth of Mbps")
_OutStream229_ObjectIdentity = ObjectIdentity
outStream229 = _OutStream229_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 238)
)
_OutBr229_Type = Integer32
_OutBr229_Object = MibScalar
outBr229 = _OutBr229_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 238, 1),
    _OutBr229_Type()
)
outBr229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr229.setStatus("current")
if mibBuilder.loadTexts:
    outBr229.setUnits("tenth of Mbps")
_OutStream230_ObjectIdentity = ObjectIdentity
outStream230 = _OutStream230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 239)
)
_OutBr230_Type = Integer32
_OutBr230_Object = MibScalar
outBr230 = _OutBr230_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 239, 1),
    _OutBr230_Type()
)
outBr230.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr230.setStatus("current")
if mibBuilder.loadTexts:
    outBr230.setUnits("tenth of Mbps")
_OutStream231_ObjectIdentity = ObjectIdentity
outStream231 = _OutStream231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 240)
)
_OutBr231_Type = Integer32
_OutBr231_Object = MibScalar
outBr231 = _OutBr231_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 240, 1),
    _OutBr231_Type()
)
outBr231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr231.setStatus("current")
if mibBuilder.loadTexts:
    outBr231.setUnits("tenth of Mbps")
_OutStream232_ObjectIdentity = ObjectIdentity
outStream232 = _OutStream232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 241)
)
_OutBr232_Type = Integer32
_OutBr232_Object = MibScalar
outBr232 = _OutBr232_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 241, 1),
    _OutBr232_Type()
)
outBr232.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr232.setStatus("current")
if mibBuilder.loadTexts:
    outBr232.setUnits("tenth of Mbps")
_OutStream233_ObjectIdentity = ObjectIdentity
outStream233 = _OutStream233_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 242)
)
_OutBr233_Type = Integer32
_OutBr233_Object = MibScalar
outBr233 = _OutBr233_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 242, 1),
    _OutBr233_Type()
)
outBr233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr233.setStatus("current")
if mibBuilder.loadTexts:
    outBr233.setUnits("tenth of Mbps")
_OutStream234_ObjectIdentity = ObjectIdentity
outStream234 = _OutStream234_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 243)
)
_OutBr234_Type = Integer32
_OutBr234_Object = MibScalar
outBr234 = _OutBr234_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 243, 1),
    _OutBr234_Type()
)
outBr234.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr234.setStatus("current")
if mibBuilder.loadTexts:
    outBr234.setUnits("tenth of Mbps")
_OutStream235_ObjectIdentity = ObjectIdentity
outStream235 = _OutStream235_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 244)
)
_OutBr235_Type = Integer32
_OutBr235_Object = MibScalar
outBr235 = _OutBr235_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 244, 1),
    _OutBr235_Type()
)
outBr235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr235.setStatus("current")
if mibBuilder.loadTexts:
    outBr235.setUnits("tenth of Mbps")
_OutStream236_ObjectIdentity = ObjectIdentity
outStream236 = _OutStream236_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 245)
)
_OutBr236_Type = Integer32
_OutBr236_Object = MibScalar
outBr236 = _OutBr236_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 245, 1),
    _OutBr236_Type()
)
outBr236.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr236.setStatus("current")
if mibBuilder.loadTexts:
    outBr236.setUnits("tenth of Mbps")
_OutStream237_ObjectIdentity = ObjectIdentity
outStream237 = _OutStream237_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 246)
)
_OutBr237_Type = Integer32
_OutBr237_Object = MibScalar
outBr237 = _OutBr237_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 246, 1),
    _OutBr237_Type()
)
outBr237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr237.setStatus("current")
if mibBuilder.loadTexts:
    outBr237.setUnits("tenth of Mbps")
_OutStream238_ObjectIdentity = ObjectIdentity
outStream238 = _OutStream238_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 247)
)
_OutBr238_Type = Integer32
_OutBr238_Object = MibScalar
outBr238 = _OutBr238_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 247, 1),
    _OutBr238_Type()
)
outBr238.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr238.setStatus("current")
if mibBuilder.loadTexts:
    outBr238.setUnits("tenth of Mbps")
_OutStream239_ObjectIdentity = ObjectIdentity
outStream239 = _OutStream239_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 248)
)
_OutBr239_Type = Integer32
_OutBr239_Object = MibScalar
outBr239 = _OutBr239_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 248, 1),
    _OutBr239_Type()
)
outBr239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr239.setStatus("current")
if mibBuilder.loadTexts:
    outBr239.setUnits("tenth of Mbps")
_OutStream240_ObjectIdentity = ObjectIdentity
outStream240 = _OutStream240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 249)
)
_OutBr240_Type = Integer32
_OutBr240_Object = MibScalar
outBr240 = _OutBr240_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 249, 1),
    _OutBr240_Type()
)
outBr240.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr240.setStatus("current")
if mibBuilder.loadTexts:
    outBr240.setUnits("tenth of Mbps")
_OutStream241_ObjectIdentity = ObjectIdentity
outStream241 = _OutStream241_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 250)
)
_OutBr241_Type = Integer32
_OutBr241_Object = MibScalar
outBr241 = _OutBr241_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 250, 1),
    _OutBr241_Type()
)
outBr241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr241.setStatus("current")
if mibBuilder.loadTexts:
    outBr241.setUnits("tenth of Mbps")
_OutStream242_ObjectIdentity = ObjectIdentity
outStream242 = _OutStream242_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 251)
)
_OutBr242_Type = Integer32
_OutBr242_Object = MibScalar
outBr242 = _OutBr242_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 251, 1),
    _OutBr242_Type()
)
outBr242.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr242.setStatus("current")
if mibBuilder.loadTexts:
    outBr242.setUnits("tenth of Mbps")
_OutStream243_ObjectIdentity = ObjectIdentity
outStream243 = _OutStream243_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 252)
)
_OutBr243_Type = Integer32
_OutBr243_Object = MibScalar
outBr243 = _OutBr243_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 252, 1),
    _OutBr243_Type()
)
outBr243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr243.setStatus("current")
if mibBuilder.loadTexts:
    outBr243.setUnits("tenth of Mbps")
_OutStream244_ObjectIdentity = ObjectIdentity
outStream244 = _OutStream244_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 253)
)
_OutBr244_Type = Integer32
_OutBr244_Object = MibScalar
outBr244 = _OutBr244_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 253, 1),
    _OutBr244_Type()
)
outBr244.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr244.setStatus("current")
if mibBuilder.loadTexts:
    outBr244.setUnits("tenth of Mbps")
_OutStream245_ObjectIdentity = ObjectIdentity
outStream245 = _OutStream245_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 254)
)
_OutBr245_Type = Integer32
_OutBr245_Object = MibScalar
outBr245 = _OutBr245_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 254, 1),
    _OutBr245_Type()
)
outBr245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr245.setStatus("current")
if mibBuilder.loadTexts:
    outBr245.setUnits("tenth of Mbps")
_OutStream246_ObjectIdentity = ObjectIdentity
outStream246 = _OutStream246_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 255)
)
_OutBr246_Type = Integer32
_OutBr246_Object = MibScalar
outBr246 = _OutBr246_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 255, 1),
    _OutBr246_Type()
)
outBr246.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr246.setStatus("current")
if mibBuilder.loadTexts:
    outBr246.setUnits("tenth of Mbps")
_OutStream247_ObjectIdentity = ObjectIdentity
outStream247 = _OutStream247_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 256)
)
_OutBr247_Type = Integer32
_OutBr247_Object = MibScalar
outBr247 = _OutBr247_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 256, 1),
    _OutBr247_Type()
)
outBr247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr247.setStatus("current")
if mibBuilder.loadTexts:
    outBr247.setUnits("tenth of Mbps")
_OutStream248_ObjectIdentity = ObjectIdentity
outStream248 = _OutStream248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 257)
)
_OutBr248_Type = Integer32
_OutBr248_Object = MibScalar
outBr248 = _OutBr248_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 257, 1),
    _OutBr248_Type()
)
outBr248.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr248.setStatus("current")
if mibBuilder.loadTexts:
    outBr248.setUnits("tenth of Mbps")
_OutStream249_ObjectIdentity = ObjectIdentity
outStream249 = _OutStream249_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 258)
)
_OutBr249_Type = Integer32
_OutBr249_Object = MibScalar
outBr249 = _OutBr249_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 258, 1),
    _OutBr249_Type()
)
outBr249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr249.setStatus("current")
if mibBuilder.loadTexts:
    outBr249.setUnits("tenth of Mbps")
_OutStream250_ObjectIdentity = ObjectIdentity
outStream250 = _OutStream250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 259)
)
_OutBr250_Type = Integer32
_OutBr250_Object = MibScalar
outBr250 = _OutBr250_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 259, 1),
    _OutBr250_Type()
)
outBr250.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr250.setStatus("current")
if mibBuilder.loadTexts:
    outBr250.setUnits("tenth of Mbps")
_OutStream251_ObjectIdentity = ObjectIdentity
outStream251 = _OutStream251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 260)
)
_OutBr251_Type = Integer32
_OutBr251_Object = MibScalar
outBr251 = _OutBr251_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 260, 1),
    _OutBr251_Type()
)
outBr251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr251.setStatus("current")
if mibBuilder.loadTexts:
    outBr251.setUnits("tenth of Mbps")
_OutStream252_ObjectIdentity = ObjectIdentity
outStream252 = _OutStream252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 261)
)
_OutBr252_Type = Integer32
_OutBr252_Object = MibScalar
outBr252 = _OutBr252_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 261, 1),
    _OutBr252_Type()
)
outBr252.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr252.setStatus("current")
if mibBuilder.loadTexts:
    outBr252.setUnits("tenth of Mbps")
_OutStream253_ObjectIdentity = ObjectIdentity
outStream253 = _OutStream253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 262)
)
_OutBr253_Type = Integer32
_OutBr253_Object = MibScalar
outBr253 = _OutBr253_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 262, 1),
    _OutBr253_Type()
)
outBr253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr253.setStatus("current")
if mibBuilder.loadTexts:
    outBr253.setUnits("tenth of Mbps")
_OutStream254_ObjectIdentity = ObjectIdentity
outStream254 = _OutStream254_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 263)
)
_OutBr254_Type = Integer32
_OutBr254_Object = MibScalar
outBr254 = _OutBr254_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 263, 1),
    _OutBr254_Type()
)
outBr254.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr254.setStatus("current")
if mibBuilder.loadTexts:
    outBr254.setUnits("tenth of Mbps")
_OutStream255_ObjectIdentity = ObjectIdentity
outStream255 = _OutStream255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 264)
)
_OutBr255_Type = Integer32
_OutBr255_Object = MibScalar
outBr255 = _OutBr255_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 264, 1),
    _OutBr255_Type()
)
outBr255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr255.setStatus("current")
if mibBuilder.loadTexts:
    outBr255.setUnits("tenth of Mbps")
_OutStream256_ObjectIdentity = ObjectIdentity
outStream256 = _OutStream256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 265)
)
_OutBr256_Type = Integer32
_OutBr256_Object = MibScalar
outBr256 = _OutBr256_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 265, 1),
    _OutBr256_Type()
)
outBr256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr256.setStatus("current")
if mibBuilder.loadTexts:
    outBr256.setUnits("tenth of Mbps")
_OutStream257_ObjectIdentity = ObjectIdentity
outStream257 = _OutStream257_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 266)
)
_OutBr257_Type = Integer32
_OutBr257_Object = MibScalar
outBr257 = _OutBr257_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 266, 1),
    _OutBr257_Type()
)
outBr257.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr257.setStatus("current")
if mibBuilder.loadTexts:
    outBr257.setUnits("tenth of Mbps")
_OutStream258_ObjectIdentity = ObjectIdentity
outStream258 = _OutStream258_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 267)
)
_OutBr258_Type = Integer32
_OutBr258_Object = MibScalar
outBr258 = _OutBr258_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 267, 1),
    _OutBr258_Type()
)
outBr258.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr258.setStatus("current")
if mibBuilder.loadTexts:
    outBr258.setUnits("tenth of Mbps")
_OutStream259_ObjectIdentity = ObjectIdentity
outStream259 = _OutStream259_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 268)
)
_OutBr259_Type = Integer32
_OutBr259_Object = MibScalar
outBr259 = _OutBr259_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 268, 1),
    _OutBr259_Type()
)
outBr259.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr259.setStatus("current")
if mibBuilder.loadTexts:
    outBr259.setUnits("tenth of Mbps")
_OutStream260_ObjectIdentity = ObjectIdentity
outStream260 = _OutStream260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 269)
)
_OutBr260_Type = Integer32
_OutBr260_Object = MibScalar
outBr260 = _OutBr260_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 269, 1),
    _OutBr260_Type()
)
outBr260.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr260.setStatus("current")
if mibBuilder.loadTexts:
    outBr260.setUnits("tenth of Mbps")
_OutStream261_ObjectIdentity = ObjectIdentity
outStream261 = _OutStream261_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 270)
)
_OutBr261_Type = Integer32
_OutBr261_Object = MibScalar
outBr261 = _OutBr261_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 270, 1),
    _OutBr261_Type()
)
outBr261.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr261.setStatus("current")
if mibBuilder.loadTexts:
    outBr261.setUnits("tenth of Mbps")
_OutStream262_ObjectIdentity = ObjectIdentity
outStream262 = _OutStream262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 271)
)
_OutBr262_Type = Integer32
_OutBr262_Object = MibScalar
outBr262 = _OutBr262_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 271, 1),
    _OutBr262_Type()
)
outBr262.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr262.setStatus("current")
if mibBuilder.loadTexts:
    outBr262.setUnits("tenth of Mbps")
_OutStream263_ObjectIdentity = ObjectIdentity
outStream263 = _OutStream263_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 272)
)
_OutBr263_Type = Integer32
_OutBr263_Object = MibScalar
outBr263 = _OutBr263_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 272, 1),
    _OutBr263_Type()
)
outBr263.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr263.setStatus("current")
if mibBuilder.loadTexts:
    outBr263.setUnits("tenth of Mbps")
_OutStream264_ObjectIdentity = ObjectIdentity
outStream264 = _OutStream264_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 273)
)
_OutBr264_Type = Integer32
_OutBr264_Object = MibScalar
outBr264 = _OutBr264_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 273, 1),
    _OutBr264_Type()
)
outBr264.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr264.setStatus("current")
if mibBuilder.loadTexts:
    outBr264.setUnits("tenth of Mbps")
_OutStream265_ObjectIdentity = ObjectIdentity
outStream265 = _OutStream265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 274)
)
_OutBr265_Type = Integer32
_OutBr265_Object = MibScalar
outBr265 = _OutBr265_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 274, 1),
    _OutBr265_Type()
)
outBr265.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr265.setStatus("current")
if mibBuilder.loadTexts:
    outBr265.setUnits("tenth of Mbps")
_OutStream266_ObjectIdentity = ObjectIdentity
outStream266 = _OutStream266_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 275)
)
_OutBr266_Type = Integer32
_OutBr266_Object = MibScalar
outBr266 = _OutBr266_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 275, 1),
    _OutBr266_Type()
)
outBr266.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr266.setStatus("current")
if mibBuilder.loadTexts:
    outBr266.setUnits("tenth of Mbps")
_OutStream267_ObjectIdentity = ObjectIdentity
outStream267 = _OutStream267_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 276)
)
_OutBr267_Type = Integer32
_OutBr267_Object = MibScalar
outBr267 = _OutBr267_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 276, 1),
    _OutBr267_Type()
)
outBr267.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr267.setStatus("current")
if mibBuilder.loadTexts:
    outBr267.setUnits("tenth of Mbps")
_OutStream268_ObjectIdentity = ObjectIdentity
outStream268 = _OutStream268_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 277)
)
_OutBr268_Type = Integer32
_OutBr268_Object = MibScalar
outBr268 = _OutBr268_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 277, 1),
    _OutBr268_Type()
)
outBr268.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr268.setStatus("current")
if mibBuilder.loadTexts:
    outBr268.setUnits("tenth of Mbps")
_OutStream269_ObjectIdentity = ObjectIdentity
outStream269 = _OutStream269_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 278)
)
_OutBr269_Type = Integer32
_OutBr269_Object = MibScalar
outBr269 = _OutBr269_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 278, 1),
    _OutBr269_Type()
)
outBr269.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr269.setStatus("current")
if mibBuilder.loadTexts:
    outBr269.setUnits("tenth of Mbps")
_OutStream270_ObjectIdentity = ObjectIdentity
outStream270 = _OutStream270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 279)
)
_OutBr270_Type = Integer32
_OutBr270_Object = MibScalar
outBr270 = _OutBr270_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 279, 1),
    _OutBr270_Type()
)
outBr270.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr270.setStatus("current")
if mibBuilder.loadTexts:
    outBr270.setUnits("tenth of Mbps")
_OutStream271_ObjectIdentity = ObjectIdentity
outStream271 = _OutStream271_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 280)
)
_OutBr271_Type = Integer32
_OutBr271_Object = MibScalar
outBr271 = _OutBr271_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 280, 1),
    _OutBr271_Type()
)
outBr271.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr271.setStatus("current")
if mibBuilder.loadTexts:
    outBr271.setUnits("tenth of Mbps")
_OutStream272_ObjectIdentity = ObjectIdentity
outStream272 = _OutStream272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 281)
)
_OutBr272_Type = Integer32
_OutBr272_Object = MibScalar
outBr272 = _OutBr272_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 281, 1),
    _OutBr272_Type()
)
outBr272.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr272.setStatus("current")
if mibBuilder.loadTexts:
    outBr272.setUnits("tenth of Mbps")
_OutStream273_ObjectIdentity = ObjectIdentity
outStream273 = _OutStream273_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 282)
)
_OutBr273_Type = Integer32
_OutBr273_Object = MibScalar
outBr273 = _OutBr273_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 282, 1),
    _OutBr273_Type()
)
outBr273.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr273.setStatus("current")
if mibBuilder.loadTexts:
    outBr273.setUnits("tenth of Mbps")
_OutStream274_ObjectIdentity = ObjectIdentity
outStream274 = _OutStream274_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 283)
)
_OutBr274_Type = Integer32
_OutBr274_Object = MibScalar
outBr274 = _OutBr274_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 283, 1),
    _OutBr274_Type()
)
outBr274.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr274.setStatus("current")
if mibBuilder.loadTexts:
    outBr274.setUnits("tenth of Mbps")
_OutStream275_ObjectIdentity = ObjectIdentity
outStream275 = _OutStream275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 284)
)
_OutBr275_Type = Integer32
_OutBr275_Object = MibScalar
outBr275 = _OutBr275_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 284, 1),
    _OutBr275_Type()
)
outBr275.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr275.setStatus("current")
if mibBuilder.loadTexts:
    outBr275.setUnits("tenth of Mbps")
_OutStream276_ObjectIdentity = ObjectIdentity
outStream276 = _OutStream276_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 285)
)
_OutBr276_Type = Integer32
_OutBr276_Object = MibScalar
outBr276 = _OutBr276_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 285, 1),
    _OutBr276_Type()
)
outBr276.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr276.setStatus("current")
if mibBuilder.loadTexts:
    outBr276.setUnits("tenth of Mbps")
_OutStream277_ObjectIdentity = ObjectIdentity
outStream277 = _OutStream277_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 286)
)
_OutBr277_Type = Integer32
_OutBr277_Object = MibScalar
outBr277 = _OutBr277_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 286, 1),
    _OutBr277_Type()
)
outBr277.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr277.setStatus("current")
if mibBuilder.loadTexts:
    outBr277.setUnits("tenth of Mbps")
_OutStream278_ObjectIdentity = ObjectIdentity
outStream278 = _OutStream278_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 287)
)
_OutBr278_Type = Integer32
_OutBr278_Object = MibScalar
outBr278 = _OutBr278_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 287, 1),
    _OutBr278_Type()
)
outBr278.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr278.setStatus("current")
if mibBuilder.loadTexts:
    outBr278.setUnits("tenth of Mbps")
_OutStream279_ObjectIdentity = ObjectIdentity
outStream279 = _OutStream279_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 288)
)
_OutBr279_Type = Integer32
_OutBr279_Object = MibScalar
outBr279 = _OutBr279_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 288, 1),
    _OutBr279_Type()
)
outBr279.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr279.setStatus("current")
if mibBuilder.loadTexts:
    outBr279.setUnits("tenth of Mbps")
_OutStream280_ObjectIdentity = ObjectIdentity
outStream280 = _OutStream280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 289)
)
_OutBr280_Type = Integer32
_OutBr280_Object = MibScalar
outBr280 = _OutBr280_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 289, 1),
    _OutBr280_Type()
)
outBr280.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr280.setStatus("current")
if mibBuilder.loadTexts:
    outBr280.setUnits("tenth of Mbps")
_OutStream281_ObjectIdentity = ObjectIdentity
outStream281 = _OutStream281_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 290)
)
_OutBr281_Type = Integer32
_OutBr281_Object = MibScalar
outBr281 = _OutBr281_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 290, 1),
    _OutBr281_Type()
)
outBr281.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr281.setStatus("current")
if mibBuilder.loadTexts:
    outBr281.setUnits("tenth of Mbps")
_OutStream282_ObjectIdentity = ObjectIdentity
outStream282 = _OutStream282_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 291)
)
_OutBr282_Type = Integer32
_OutBr282_Object = MibScalar
outBr282 = _OutBr282_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 291, 1),
    _OutBr282_Type()
)
outBr282.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr282.setStatus("current")
if mibBuilder.loadTexts:
    outBr282.setUnits("tenth of Mbps")
_OutStream283_ObjectIdentity = ObjectIdentity
outStream283 = _OutStream283_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 292)
)
_OutBr283_Type = Integer32
_OutBr283_Object = MibScalar
outBr283 = _OutBr283_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 292, 1),
    _OutBr283_Type()
)
outBr283.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr283.setStatus("current")
if mibBuilder.loadTexts:
    outBr283.setUnits("tenth of Mbps")
_OutStream284_ObjectIdentity = ObjectIdentity
outStream284 = _OutStream284_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 293)
)
_OutBr284_Type = Integer32
_OutBr284_Object = MibScalar
outBr284 = _OutBr284_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 293, 1),
    _OutBr284_Type()
)
outBr284.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr284.setStatus("current")
if mibBuilder.loadTexts:
    outBr284.setUnits("tenth of Mbps")
_OutStream285_ObjectIdentity = ObjectIdentity
outStream285 = _OutStream285_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 294)
)
_OutBr285_Type = Integer32
_OutBr285_Object = MibScalar
outBr285 = _OutBr285_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 294, 1),
    _OutBr285_Type()
)
outBr285.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr285.setStatus("current")
if mibBuilder.loadTexts:
    outBr285.setUnits("tenth of Mbps")
_OutStream286_ObjectIdentity = ObjectIdentity
outStream286 = _OutStream286_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 295)
)
_OutBr286_Type = Integer32
_OutBr286_Object = MibScalar
outBr286 = _OutBr286_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 295, 1),
    _OutBr286_Type()
)
outBr286.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr286.setStatus("current")
if mibBuilder.loadTexts:
    outBr286.setUnits("tenth of Mbps")
_OutStream287_ObjectIdentity = ObjectIdentity
outStream287 = _OutStream287_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 296)
)
_OutBr287_Type = Integer32
_OutBr287_Object = MibScalar
outBr287 = _OutBr287_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 296, 1),
    _OutBr287_Type()
)
outBr287.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr287.setStatus("current")
if mibBuilder.loadTexts:
    outBr287.setUnits("tenth of Mbps")
_OutStream288_ObjectIdentity = ObjectIdentity
outStream288 = _OutStream288_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 297)
)
_OutBr288_Type = Integer32
_OutBr288_Object = MibScalar
outBr288 = _OutBr288_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 297, 1),
    _OutBr288_Type()
)
outBr288.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr288.setStatus("current")
if mibBuilder.loadTexts:
    outBr288.setUnits("tenth of Mbps")
_OutStream289_ObjectIdentity = ObjectIdentity
outStream289 = _OutStream289_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 298)
)
_OutBr289_Type = Integer32
_OutBr289_Object = MibScalar
outBr289 = _OutBr289_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 298, 1),
    _OutBr289_Type()
)
outBr289.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr289.setStatus("current")
if mibBuilder.loadTexts:
    outBr289.setUnits("tenth of Mbps")
_OutStream290_ObjectIdentity = ObjectIdentity
outStream290 = _OutStream290_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 299)
)
_OutBr290_Type = Integer32
_OutBr290_Object = MibScalar
outBr290 = _OutBr290_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 299, 1),
    _OutBr290_Type()
)
outBr290.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr290.setStatus("current")
if mibBuilder.loadTexts:
    outBr290.setUnits("tenth of Mbps")
_OutStream291_ObjectIdentity = ObjectIdentity
outStream291 = _OutStream291_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 300)
)
_OutBr291_Type = Integer32
_OutBr291_Object = MibScalar
outBr291 = _OutBr291_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 300, 1),
    _OutBr291_Type()
)
outBr291.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr291.setStatus("current")
if mibBuilder.loadTexts:
    outBr291.setUnits("tenth of Mbps")
_OutStream292_ObjectIdentity = ObjectIdentity
outStream292 = _OutStream292_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 301)
)
_OutBr292_Type = Integer32
_OutBr292_Object = MibScalar
outBr292 = _OutBr292_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 301, 1),
    _OutBr292_Type()
)
outBr292.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr292.setStatus("current")
if mibBuilder.loadTexts:
    outBr292.setUnits("tenth of Mbps")
_OutStream293_ObjectIdentity = ObjectIdentity
outStream293 = _OutStream293_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 302)
)
_OutBr293_Type = Integer32
_OutBr293_Object = MibScalar
outBr293 = _OutBr293_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 302, 1),
    _OutBr293_Type()
)
outBr293.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr293.setStatus("current")
if mibBuilder.loadTexts:
    outBr293.setUnits("tenth of Mbps")
_OutStream294_ObjectIdentity = ObjectIdentity
outStream294 = _OutStream294_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 303)
)
_OutBr294_Type = Integer32
_OutBr294_Object = MibScalar
outBr294 = _OutBr294_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 303, 1),
    _OutBr294_Type()
)
outBr294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr294.setStatus("current")
if mibBuilder.loadTexts:
    outBr294.setUnits("tenth of Mbps")
_OutStream295_ObjectIdentity = ObjectIdentity
outStream295 = _OutStream295_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 304)
)
_OutBr295_Type = Integer32
_OutBr295_Object = MibScalar
outBr295 = _OutBr295_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 304, 1),
    _OutBr295_Type()
)
outBr295.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr295.setStatus("current")
if mibBuilder.loadTexts:
    outBr295.setUnits("tenth of Mbps")
_OutStream296_ObjectIdentity = ObjectIdentity
outStream296 = _OutStream296_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 305)
)
_OutBr296_Type = Integer32
_OutBr296_Object = MibScalar
outBr296 = _OutBr296_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 305, 1),
    _OutBr296_Type()
)
outBr296.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr296.setStatus("current")
if mibBuilder.loadTexts:
    outBr296.setUnits("tenth of Mbps")
_OutStream297_ObjectIdentity = ObjectIdentity
outStream297 = _OutStream297_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 306)
)
_OutBr297_Type = Integer32
_OutBr297_Object = MibScalar
outBr297 = _OutBr297_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 306, 1),
    _OutBr297_Type()
)
outBr297.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr297.setStatus("current")
if mibBuilder.loadTexts:
    outBr297.setUnits("tenth of Mbps")
_OutStream298_ObjectIdentity = ObjectIdentity
outStream298 = _OutStream298_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 307)
)
_OutBr298_Type = Integer32
_OutBr298_Object = MibScalar
outBr298 = _OutBr298_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 307, 1),
    _OutBr298_Type()
)
outBr298.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr298.setStatus("current")
if mibBuilder.loadTexts:
    outBr298.setUnits("tenth of Mbps")
_OutStream299_ObjectIdentity = ObjectIdentity
outStream299 = _OutStream299_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 308)
)
_OutBr299_Type = Integer32
_OutBr299_Object = MibScalar
outBr299 = _OutBr299_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 308, 1),
    _OutBr299_Type()
)
outBr299.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr299.setStatus("current")
if mibBuilder.loadTexts:
    outBr299.setUnits("tenth of Mbps")
_OutStream300_ObjectIdentity = ObjectIdentity
outStream300 = _OutStream300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 309)
)
_OutBr300_Type = Integer32
_OutBr300_Object = MibScalar
outBr300 = _OutBr300_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 309, 1),
    _OutBr300_Type()
)
outBr300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr300.setStatus("current")
if mibBuilder.loadTexts:
    outBr300.setUnits("tenth of Mbps")
_OutStream301_ObjectIdentity = ObjectIdentity
outStream301 = _OutStream301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 310)
)
_OutBr301_Type = Integer32
_OutBr301_Object = MibScalar
outBr301 = _OutBr301_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 310, 1),
    _OutBr301_Type()
)
outBr301.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr301.setStatus("current")
if mibBuilder.loadTexts:
    outBr301.setUnits("tenth of Mbps")
_OutStream302_ObjectIdentity = ObjectIdentity
outStream302 = _OutStream302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 311)
)
_OutBr302_Type = Integer32
_OutBr302_Object = MibScalar
outBr302 = _OutBr302_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 311, 1),
    _OutBr302_Type()
)
outBr302.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr302.setStatus("current")
if mibBuilder.loadTexts:
    outBr302.setUnits("tenth of Mbps")
_OutStream303_ObjectIdentity = ObjectIdentity
outStream303 = _OutStream303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 312)
)
_OutBr303_Type = Integer32
_OutBr303_Object = MibScalar
outBr303 = _OutBr303_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 312, 1),
    _OutBr303_Type()
)
outBr303.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr303.setStatus("current")
if mibBuilder.loadTexts:
    outBr303.setUnits("tenth of Mbps")
_OutStream304_ObjectIdentity = ObjectIdentity
outStream304 = _OutStream304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 313)
)
_OutBr304_Type = Integer32
_OutBr304_Object = MibScalar
outBr304 = _OutBr304_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 313, 1),
    _OutBr304_Type()
)
outBr304.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr304.setStatus("current")
if mibBuilder.loadTexts:
    outBr304.setUnits("tenth of Mbps")
_OutStream305_ObjectIdentity = ObjectIdentity
outStream305 = _OutStream305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 314)
)
_OutBr305_Type = Integer32
_OutBr305_Object = MibScalar
outBr305 = _OutBr305_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 314, 1),
    _OutBr305_Type()
)
outBr305.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr305.setStatus("current")
if mibBuilder.loadTexts:
    outBr305.setUnits("tenth of Mbps")
_OutStream306_ObjectIdentity = ObjectIdentity
outStream306 = _OutStream306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 315)
)
_OutBr306_Type = Integer32
_OutBr306_Object = MibScalar
outBr306 = _OutBr306_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 315, 1),
    _OutBr306_Type()
)
outBr306.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr306.setStatus("current")
if mibBuilder.loadTexts:
    outBr306.setUnits("tenth of Mbps")
_OutStream307_ObjectIdentity = ObjectIdentity
outStream307 = _OutStream307_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 316)
)
_OutBr307_Type = Integer32
_OutBr307_Object = MibScalar
outBr307 = _OutBr307_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 316, 1),
    _OutBr307_Type()
)
outBr307.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr307.setStatus("current")
if mibBuilder.loadTexts:
    outBr307.setUnits("tenth of Mbps")
_OutStream308_ObjectIdentity = ObjectIdentity
outStream308 = _OutStream308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 317)
)
_OutBr308_Type = Integer32
_OutBr308_Object = MibScalar
outBr308 = _OutBr308_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 317, 1),
    _OutBr308_Type()
)
outBr308.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr308.setStatus("current")
if mibBuilder.loadTexts:
    outBr308.setUnits("tenth of Mbps")
_OutStream309_ObjectIdentity = ObjectIdentity
outStream309 = _OutStream309_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 318)
)
_OutBr309_Type = Integer32
_OutBr309_Object = MibScalar
outBr309 = _OutBr309_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 318, 1),
    _OutBr309_Type()
)
outBr309.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr309.setStatus("current")
if mibBuilder.loadTexts:
    outBr309.setUnits("tenth of Mbps")
_OutStream310_ObjectIdentity = ObjectIdentity
outStream310 = _OutStream310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 319)
)
_OutBr310_Type = Integer32
_OutBr310_Object = MibScalar
outBr310 = _OutBr310_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 319, 1),
    _OutBr310_Type()
)
outBr310.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr310.setStatus("current")
if mibBuilder.loadTexts:
    outBr310.setUnits("tenth of Mbps")
_OutStream311_ObjectIdentity = ObjectIdentity
outStream311 = _OutStream311_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 320)
)
_OutBr311_Type = Integer32
_OutBr311_Object = MibScalar
outBr311 = _OutBr311_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 320, 1),
    _OutBr311_Type()
)
outBr311.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr311.setStatus("current")
if mibBuilder.loadTexts:
    outBr311.setUnits("tenth of Mbps")
_OutStream312_ObjectIdentity = ObjectIdentity
outStream312 = _OutStream312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 321)
)
_OutBr312_Type = Integer32
_OutBr312_Object = MibScalar
outBr312 = _OutBr312_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 321, 1),
    _OutBr312_Type()
)
outBr312.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr312.setStatus("current")
if mibBuilder.loadTexts:
    outBr312.setUnits("tenth of Mbps")
_OutStream313_ObjectIdentity = ObjectIdentity
outStream313 = _OutStream313_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 322)
)
_OutBr313_Type = Integer32
_OutBr313_Object = MibScalar
outBr313 = _OutBr313_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 322, 1),
    _OutBr313_Type()
)
outBr313.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr313.setStatus("current")
if mibBuilder.loadTexts:
    outBr313.setUnits("tenth of Mbps")
_OutStream314_ObjectIdentity = ObjectIdentity
outStream314 = _OutStream314_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 323)
)
_OutBr314_Type = Integer32
_OutBr314_Object = MibScalar
outBr314 = _OutBr314_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 323, 1),
    _OutBr314_Type()
)
outBr314.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr314.setStatus("current")
if mibBuilder.loadTexts:
    outBr314.setUnits("tenth of Mbps")
_OutStream315_ObjectIdentity = ObjectIdentity
outStream315 = _OutStream315_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 324)
)
_OutBr315_Type = Integer32
_OutBr315_Object = MibScalar
outBr315 = _OutBr315_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 324, 1),
    _OutBr315_Type()
)
outBr315.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr315.setStatus("current")
if mibBuilder.loadTexts:
    outBr315.setUnits("tenth of Mbps")
_OutStream316_ObjectIdentity = ObjectIdentity
outStream316 = _OutStream316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 325)
)
_OutBr316_Type = Integer32
_OutBr316_Object = MibScalar
outBr316 = _OutBr316_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 325, 1),
    _OutBr316_Type()
)
outBr316.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr316.setStatus("current")
if mibBuilder.loadTexts:
    outBr316.setUnits("tenth of Mbps")
_OutStream317_ObjectIdentity = ObjectIdentity
outStream317 = _OutStream317_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 326)
)
_OutBr317_Type = Integer32
_OutBr317_Object = MibScalar
outBr317 = _OutBr317_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 326, 1),
    _OutBr317_Type()
)
outBr317.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr317.setStatus("current")
if mibBuilder.loadTexts:
    outBr317.setUnits("tenth of Mbps")
_OutStream318_ObjectIdentity = ObjectIdentity
outStream318 = _OutStream318_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 327)
)
_OutBr318_Type = Integer32
_OutBr318_Object = MibScalar
outBr318 = _OutBr318_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 327, 1),
    _OutBr318_Type()
)
outBr318.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr318.setStatus("current")
if mibBuilder.loadTexts:
    outBr318.setUnits("tenth of Mbps")
_OutStream319_ObjectIdentity = ObjectIdentity
outStream319 = _OutStream319_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 328)
)
_OutBr319_Type = Integer32
_OutBr319_Object = MibScalar
outBr319 = _OutBr319_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 328, 1),
    _OutBr319_Type()
)
outBr319.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr319.setStatus("current")
if mibBuilder.loadTexts:
    outBr319.setUnits("tenth of Mbps")
_OutStream320_ObjectIdentity = ObjectIdentity
outStream320 = _OutStream320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 329)
)
_OutBr320_Type = Integer32
_OutBr320_Object = MibScalar
outBr320 = _OutBr320_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 329, 1),
    _OutBr320_Type()
)
outBr320.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr320.setStatus("current")
if mibBuilder.loadTexts:
    outBr320.setUnits("tenth of Mbps")
_OutStream321_ObjectIdentity = ObjectIdentity
outStream321 = _OutStream321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 330)
)
_OutBr321_Type = Integer32
_OutBr321_Object = MibScalar
outBr321 = _OutBr321_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 330, 1),
    _OutBr321_Type()
)
outBr321.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr321.setStatus("current")
if mibBuilder.loadTexts:
    outBr321.setUnits("tenth of Mbps")
_OutStream322_ObjectIdentity = ObjectIdentity
outStream322 = _OutStream322_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 331)
)
_OutBr322_Type = Integer32
_OutBr322_Object = MibScalar
outBr322 = _OutBr322_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 331, 1),
    _OutBr322_Type()
)
outBr322.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr322.setStatus("current")
if mibBuilder.loadTexts:
    outBr322.setUnits("tenth of Mbps")
_OutStream323_ObjectIdentity = ObjectIdentity
outStream323 = _OutStream323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 332)
)
_OutBr323_Type = Integer32
_OutBr323_Object = MibScalar
outBr323 = _OutBr323_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 332, 1),
    _OutBr323_Type()
)
outBr323.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr323.setStatus("current")
if mibBuilder.loadTexts:
    outBr323.setUnits("tenth of Mbps")
_OutStream324_ObjectIdentity = ObjectIdentity
outStream324 = _OutStream324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 333)
)
_OutBr324_Type = Integer32
_OutBr324_Object = MibScalar
outBr324 = _OutBr324_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 333, 1),
    _OutBr324_Type()
)
outBr324.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr324.setStatus("current")
if mibBuilder.loadTexts:
    outBr324.setUnits("tenth of Mbps")
_OutStream325_ObjectIdentity = ObjectIdentity
outStream325 = _OutStream325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 334)
)
_OutBr325_Type = Integer32
_OutBr325_Object = MibScalar
outBr325 = _OutBr325_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 334, 1),
    _OutBr325_Type()
)
outBr325.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr325.setStatus("current")
if mibBuilder.loadTexts:
    outBr325.setUnits("tenth of Mbps")
_OutStream326_ObjectIdentity = ObjectIdentity
outStream326 = _OutStream326_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 335)
)
_OutBr326_Type = Integer32
_OutBr326_Object = MibScalar
outBr326 = _OutBr326_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 335, 1),
    _OutBr326_Type()
)
outBr326.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr326.setStatus("current")
if mibBuilder.loadTexts:
    outBr326.setUnits("tenth of Mbps")
_OutStream327_ObjectIdentity = ObjectIdentity
outStream327 = _OutStream327_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 336)
)
_OutBr327_Type = Integer32
_OutBr327_Object = MibScalar
outBr327 = _OutBr327_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 336, 1),
    _OutBr327_Type()
)
outBr327.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr327.setStatus("current")
if mibBuilder.loadTexts:
    outBr327.setUnits("tenth of Mbps")
_OutStream328_ObjectIdentity = ObjectIdentity
outStream328 = _OutStream328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 337)
)
_OutBr328_Type = Integer32
_OutBr328_Object = MibScalar
outBr328 = _OutBr328_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 337, 1),
    _OutBr328_Type()
)
outBr328.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr328.setStatus("current")
if mibBuilder.loadTexts:
    outBr328.setUnits("tenth of Mbps")
_OutStream329_ObjectIdentity = ObjectIdentity
outStream329 = _OutStream329_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 338)
)
_OutBr329_Type = Integer32
_OutBr329_Object = MibScalar
outBr329 = _OutBr329_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 338, 1),
    _OutBr329_Type()
)
outBr329.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr329.setStatus("current")
if mibBuilder.loadTexts:
    outBr329.setUnits("tenth of Mbps")
_OutStream330_ObjectIdentity = ObjectIdentity
outStream330 = _OutStream330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 339)
)
_OutBr330_Type = Integer32
_OutBr330_Object = MibScalar
outBr330 = _OutBr330_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 339, 1),
    _OutBr330_Type()
)
outBr330.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr330.setStatus("current")
if mibBuilder.loadTexts:
    outBr330.setUnits("tenth of Mbps")
_OutStream331_ObjectIdentity = ObjectIdentity
outStream331 = _OutStream331_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 340)
)
_OutBr331_Type = Integer32
_OutBr331_Object = MibScalar
outBr331 = _OutBr331_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 340, 1),
    _OutBr331_Type()
)
outBr331.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr331.setStatus("current")
if mibBuilder.loadTexts:
    outBr331.setUnits("tenth of Mbps")
_OutStream332_ObjectIdentity = ObjectIdentity
outStream332 = _OutStream332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 341)
)
_OutBr332_Type = Integer32
_OutBr332_Object = MibScalar
outBr332 = _OutBr332_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 341, 1),
    _OutBr332_Type()
)
outBr332.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr332.setStatus("current")
if mibBuilder.loadTexts:
    outBr332.setUnits("tenth of Mbps")
_OutStream333_ObjectIdentity = ObjectIdentity
outStream333 = _OutStream333_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 342)
)
_OutBr333_Type = Integer32
_OutBr333_Object = MibScalar
outBr333 = _OutBr333_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 342, 1),
    _OutBr333_Type()
)
outBr333.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr333.setStatus("current")
if mibBuilder.loadTexts:
    outBr333.setUnits("tenth of Mbps")
_OutStream334_ObjectIdentity = ObjectIdentity
outStream334 = _OutStream334_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 343)
)
_OutBr334_Type = Integer32
_OutBr334_Object = MibScalar
outBr334 = _OutBr334_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 343, 1),
    _OutBr334_Type()
)
outBr334.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr334.setStatus("current")
if mibBuilder.loadTexts:
    outBr334.setUnits("tenth of Mbps")
_OutStream335_ObjectIdentity = ObjectIdentity
outStream335 = _OutStream335_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 344)
)
_OutBr335_Type = Integer32
_OutBr335_Object = MibScalar
outBr335 = _OutBr335_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 344, 1),
    _OutBr335_Type()
)
outBr335.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr335.setStatus("current")
if mibBuilder.loadTexts:
    outBr335.setUnits("tenth of Mbps")
_OutStream336_ObjectIdentity = ObjectIdentity
outStream336 = _OutStream336_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 345)
)
_OutBr336_Type = Integer32
_OutBr336_Object = MibScalar
outBr336 = _OutBr336_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 345, 1),
    _OutBr336_Type()
)
outBr336.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr336.setStatus("current")
if mibBuilder.loadTexts:
    outBr336.setUnits("tenth of Mbps")
_OutStream337_ObjectIdentity = ObjectIdentity
outStream337 = _OutStream337_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 346)
)
_OutBr337_Type = Integer32
_OutBr337_Object = MibScalar
outBr337 = _OutBr337_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 346, 1),
    _OutBr337_Type()
)
outBr337.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr337.setStatus("current")
if mibBuilder.loadTexts:
    outBr337.setUnits("tenth of Mbps")
_OutStream338_ObjectIdentity = ObjectIdentity
outStream338 = _OutStream338_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 347)
)
_OutBr338_Type = Integer32
_OutBr338_Object = MibScalar
outBr338 = _OutBr338_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 347, 1),
    _OutBr338_Type()
)
outBr338.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr338.setStatus("current")
if mibBuilder.loadTexts:
    outBr338.setUnits("tenth of Mbps")
_OutStream339_ObjectIdentity = ObjectIdentity
outStream339 = _OutStream339_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 348)
)
_OutBr339_Type = Integer32
_OutBr339_Object = MibScalar
outBr339 = _OutBr339_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 348, 1),
    _OutBr339_Type()
)
outBr339.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr339.setStatus("current")
if mibBuilder.loadTexts:
    outBr339.setUnits("tenth of Mbps")
_OutStream340_ObjectIdentity = ObjectIdentity
outStream340 = _OutStream340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 349)
)
_OutBr340_Type = Integer32
_OutBr340_Object = MibScalar
outBr340 = _OutBr340_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 349, 1),
    _OutBr340_Type()
)
outBr340.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr340.setStatus("current")
if mibBuilder.loadTexts:
    outBr340.setUnits("tenth of Mbps")
_OutStream341_ObjectIdentity = ObjectIdentity
outStream341 = _OutStream341_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 350)
)
_OutBr341_Type = Integer32
_OutBr341_Object = MibScalar
outBr341 = _OutBr341_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 350, 1),
    _OutBr341_Type()
)
outBr341.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr341.setStatus("current")
if mibBuilder.loadTexts:
    outBr341.setUnits("tenth of Mbps")
_OutStream342_ObjectIdentity = ObjectIdentity
outStream342 = _OutStream342_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 351)
)
_OutBr342_Type = Integer32
_OutBr342_Object = MibScalar
outBr342 = _OutBr342_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 351, 1),
    _OutBr342_Type()
)
outBr342.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr342.setStatus("current")
if mibBuilder.loadTexts:
    outBr342.setUnits("tenth of Mbps")
_OutStream343_ObjectIdentity = ObjectIdentity
outStream343 = _OutStream343_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 352)
)
_OutBr343_Type = Integer32
_OutBr343_Object = MibScalar
outBr343 = _OutBr343_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 352, 1),
    _OutBr343_Type()
)
outBr343.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr343.setStatus("current")
if mibBuilder.loadTexts:
    outBr343.setUnits("tenth of Mbps")
_OutStream344_ObjectIdentity = ObjectIdentity
outStream344 = _OutStream344_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 353)
)
_OutBr344_Type = Integer32
_OutBr344_Object = MibScalar
outBr344 = _OutBr344_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 353, 1),
    _OutBr344_Type()
)
outBr344.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr344.setStatus("current")
if mibBuilder.loadTexts:
    outBr344.setUnits("tenth of Mbps")
_OutStream345_ObjectIdentity = ObjectIdentity
outStream345 = _OutStream345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 354)
)
_OutBr345_Type = Integer32
_OutBr345_Object = MibScalar
outBr345 = _OutBr345_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 354, 1),
    _OutBr345_Type()
)
outBr345.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr345.setStatus("current")
if mibBuilder.loadTexts:
    outBr345.setUnits("tenth of Mbps")
_OutStream346_ObjectIdentity = ObjectIdentity
outStream346 = _OutStream346_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 355)
)
_OutBr346_Type = Integer32
_OutBr346_Object = MibScalar
outBr346 = _OutBr346_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 355, 1),
    _OutBr346_Type()
)
outBr346.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr346.setStatus("current")
if mibBuilder.loadTexts:
    outBr346.setUnits("tenth of Mbps")
_OutStream347_ObjectIdentity = ObjectIdentity
outStream347 = _OutStream347_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 356)
)
_OutBr347_Type = Integer32
_OutBr347_Object = MibScalar
outBr347 = _OutBr347_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 356, 1),
    _OutBr347_Type()
)
outBr347.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr347.setStatus("current")
if mibBuilder.loadTexts:
    outBr347.setUnits("tenth of Mbps")
_OutStream348_ObjectIdentity = ObjectIdentity
outStream348 = _OutStream348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 357)
)
_OutBr348_Type = Integer32
_OutBr348_Object = MibScalar
outBr348 = _OutBr348_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 357, 1),
    _OutBr348_Type()
)
outBr348.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr348.setStatus("current")
if mibBuilder.loadTexts:
    outBr348.setUnits("tenth of Mbps")
_OutStream349_ObjectIdentity = ObjectIdentity
outStream349 = _OutStream349_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 358)
)
_OutBr349_Type = Integer32
_OutBr349_Object = MibScalar
outBr349 = _OutBr349_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 358, 1),
    _OutBr349_Type()
)
outBr349.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr349.setStatus("current")
if mibBuilder.loadTexts:
    outBr349.setUnits("tenth of Mbps")
_OutStream350_ObjectIdentity = ObjectIdentity
outStream350 = _OutStream350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 359)
)
_OutBr350_Type = Integer32
_OutBr350_Object = MibScalar
outBr350 = _OutBr350_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 359, 1),
    _OutBr350_Type()
)
outBr350.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr350.setStatus("current")
if mibBuilder.loadTexts:
    outBr350.setUnits("tenth of Mbps")
_OutStream351_ObjectIdentity = ObjectIdentity
outStream351 = _OutStream351_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 360)
)
_OutBr351_Type = Integer32
_OutBr351_Object = MibScalar
outBr351 = _OutBr351_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 360, 1),
    _OutBr351_Type()
)
outBr351.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr351.setStatus("current")
if mibBuilder.loadTexts:
    outBr351.setUnits("tenth of Mbps")
_OutStream352_ObjectIdentity = ObjectIdentity
outStream352 = _OutStream352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 361)
)
_OutBr352_Type = Integer32
_OutBr352_Object = MibScalar
outBr352 = _OutBr352_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 361, 1),
    _OutBr352_Type()
)
outBr352.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr352.setStatus("current")
if mibBuilder.loadTexts:
    outBr352.setUnits("tenth of Mbps")
_OutStream353_ObjectIdentity = ObjectIdentity
outStream353 = _OutStream353_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 362)
)
_OutBr353_Type = Integer32
_OutBr353_Object = MibScalar
outBr353 = _OutBr353_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 362, 1),
    _OutBr353_Type()
)
outBr353.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr353.setStatus("current")
if mibBuilder.loadTexts:
    outBr353.setUnits("tenth of Mbps")
_OutStream354_ObjectIdentity = ObjectIdentity
outStream354 = _OutStream354_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 363)
)
_OutBr354_Type = Integer32
_OutBr354_Object = MibScalar
outBr354 = _OutBr354_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 363, 1),
    _OutBr354_Type()
)
outBr354.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr354.setStatus("current")
if mibBuilder.loadTexts:
    outBr354.setUnits("tenth of Mbps")
_OutStream355_ObjectIdentity = ObjectIdentity
outStream355 = _OutStream355_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 364)
)
_OutBr355_Type = Integer32
_OutBr355_Object = MibScalar
outBr355 = _OutBr355_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 364, 1),
    _OutBr355_Type()
)
outBr355.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr355.setStatus("current")
if mibBuilder.loadTexts:
    outBr355.setUnits("tenth of Mbps")
_OutStream356_ObjectIdentity = ObjectIdentity
outStream356 = _OutStream356_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 365)
)
_OutBr356_Type = Integer32
_OutBr356_Object = MibScalar
outBr356 = _OutBr356_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 365, 1),
    _OutBr356_Type()
)
outBr356.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr356.setStatus("current")
if mibBuilder.loadTexts:
    outBr356.setUnits("tenth of Mbps")
_OutStream357_ObjectIdentity = ObjectIdentity
outStream357 = _OutStream357_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 366)
)
_OutBr357_Type = Integer32
_OutBr357_Object = MibScalar
outBr357 = _OutBr357_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 366, 1),
    _OutBr357_Type()
)
outBr357.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr357.setStatus("current")
if mibBuilder.loadTexts:
    outBr357.setUnits("tenth of Mbps")
_OutStream358_ObjectIdentity = ObjectIdentity
outStream358 = _OutStream358_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 367)
)
_OutBr358_Type = Integer32
_OutBr358_Object = MibScalar
outBr358 = _OutBr358_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 367, 1),
    _OutBr358_Type()
)
outBr358.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr358.setStatus("current")
if mibBuilder.loadTexts:
    outBr358.setUnits("tenth of Mbps")
_OutStream359_ObjectIdentity = ObjectIdentity
outStream359 = _OutStream359_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 368)
)
_OutBr359_Type = Integer32
_OutBr359_Object = MibScalar
outBr359 = _OutBr359_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 368, 1),
    _OutBr359_Type()
)
outBr359.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr359.setStatus("current")
if mibBuilder.loadTexts:
    outBr359.setUnits("tenth of Mbps")
_OutStream360_ObjectIdentity = ObjectIdentity
outStream360 = _OutStream360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 369)
)
_OutBr360_Type = Integer32
_OutBr360_Object = MibScalar
outBr360 = _OutBr360_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 369, 1),
    _OutBr360_Type()
)
outBr360.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr360.setStatus("current")
if mibBuilder.loadTexts:
    outBr360.setUnits("tenth of Mbps")
_OutStream361_ObjectIdentity = ObjectIdentity
outStream361 = _OutStream361_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 370)
)
_OutBr361_Type = Integer32
_OutBr361_Object = MibScalar
outBr361 = _OutBr361_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 370, 1),
    _OutBr361_Type()
)
outBr361.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr361.setStatus("current")
if mibBuilder.loadTexts:
    outBr361.setUnits("tenth of Mbps")
_OutStream362_ObjectIdentity = ObjectIdentity
outStream362 = _OutStream362_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 371)
)
_OutBr362_Type = Integer32
_OutBr362_Object = MibScalar
outBr362 = _OutBr362_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 371, 1),
    _OutBr362_Type()
)
outBr362.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr362.setStatus("current")
if mibBuilder.loadTexts:
    outBr362.setUnits("tenth of Mbps")
_OutStream363_ObjectIdentity = ObjectIdentity
outStream363 = _OutStream363_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 372)
)
_OutBr363_Type = Integer32
_OutBr363_Object = MibScalar
outBr363 = _OutBr363_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 372, 1),
    _OutBr363_Type()
)
outBr363.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr363.setStatus("current")
if mibBuilder.loadTexts:
    outBr363.setUnits("tenth of Mbps")
_OutStream364_ObjectIdentity = ObjectIdentity
outStream364 = _OutStream364_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 373)
)
_OutBr364_Type = Integer32
_OutBr364_Object = MibScalar
outBr364 = _OutBr364_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 373, 1),
    _OutBr364_Type()
)
outBr364.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr364.setStatus("current")
if mibBuilder.loadTexts:
    outBr364.setUnits("tenth of Mbps")
_OutStream365_ObjectIdentity = ObjectIdentity
outStream365 = _OutStream365_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 374)
)
_OutBr365_Type = Integer32
_OutBr365_Object = MibScalar
outBr365 = _OutBr365_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 374, 1),
    _OutBr365_Type()
)
outBr365.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr365.setStatus("current")
if mibBuilder.loadTexts:
    outBr365.setUnits("tenth of Mbps")
_OutStream366_ObjectIdentity = ObjectIdentity
outStream366 = _OutStream366_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 375)
)
_OutBr366_Type = Integer32
_OutBr366_Object = MibScalar
outBr366 = _OutBr366_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 375, 1),
    _OutBr366_Type()
)
outBr366.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr366.setStatus("current")
if mibBuilder.loadTexts:
    outBr366.setUnits("tenth of Mbps")
_OutStream367_ObjectIdentity = ObjectIdentity
outStream367 = _OutStream367_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 376)
)
_OutBr367_Type = Integer32
_OutBr367_Object = MibScalar
outBr367 = _OutBr367_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 376, 1),
    _OutBr367_Type()
)
outBr367.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr367.setStatus("current")
if mibBuilder.loadTexts:
    outBr367.setUnits("tenth of Mbps")
_OutStream368_ObjectIdentity = ObjectIdentity
outStream368 = _OutStream368_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 377)
)
_OutBr368_Type = Integer32
_OutBr368_Object = MibScalar
outBr368 = _OutBr368_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 377, 1),
    _OutBr368_Type()
)
outBr368.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr368.setStatus("current")
if mibBuilder.loadTexts:
    outBr368.setUnits("tenth of Mbps")
_OutStream369_ObjectIdentity = ObjectIdentity
outStream369 = _OutStream369_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 378)
)
_OutBr369_Type = Integer32
_OutBr369_Object = MibScalar
outBr369 = _OutBr369_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 378, 1),
    _OutBr369_Type()
)
outBr369.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr369.setStatus("current")
if mibBuilder.loadTexts:
    outBr369.setUnits("tenth of Mbps")
_OutStream370_ObjectIdentity = ObjectIdentity
outStream370 = _OutStream370_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 379)
)
_OutBr370_Type = Integer32
_OutBr370_Object = MibScalar
outBr370 = _OutBr370_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 379, 1),
    _OutBr370_Type()
)
outBr370.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr370.setStatus("current")
if mibBuilder.loadTexts:
    outBr370.setUnits("tenth of Mbps")
_OutStream371_ObjectIdentity = ObjectIdentity
outStream371 = _OutStream371_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 380)
)
_OutBr371_Type = Integer32
_OutBr371_Object = MibScalar
outBr371 = _OutBr371_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 380, 1),
    _OutBr371_Type()
)
outBr371.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr371.setStatus("current")
if mibBuilder.loadTexts:
    outBr371.setUnits("tenth of Mbps")
_OutStream372_ObjectIdentity = ObjectIdentity
outStream372 = _OutStream372_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 381)
)
_OutBr372_Type = Integer32
_OutBr372_Object = MibScalar
outBr372 = _OutBr372_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 381, 1),
    _OutBr372_Type()
)
outBr372.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr372.setStatus("current")
if mibBuilder.loadTexts:
    outBr372.setUnits("tenth of Mbps")
_OutStream373_ObjectIdentity = ObjectIdentity
outStream373 = _OutStream373_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 382)
)
_OutBr373_Type = Integer32
_OutBr373_Object = MibScalar
outBr373 = _OutBr373_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 382, 1),
    _OutBr373_Type()
)
outBr373.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr373.setStatus("current")
if mibBuilder.loadTexts:
    outBr373.setUnits("tenth of Mbps")
_OutStream374_ObjectIdentity = ObjectIdentity
outStream374 = _OutStream374_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 383)
)
_OutBr374_Type = Integer32
_OutBr374_Object = MibScalar
outBr374 = _OutBr374_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 383, 1),
    _OutBr374_Type()
)
outBr374.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr374.setStatus("current")
if mibBuilder.loadTexts:
    outBr374.setUnits("tenth of Mbps")
_OutStream375_ObjectIdentity = ObjectIdentity
outStream375 = _OutStream375_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 384)
)
_OutBr375_Type = Integer32
_OutBr375_Object = MibScalar
outBr375 = _OutBr375_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 384, 1),
    _OutBr375_Type()
)
outBr375.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr375.setStatus("current")
if mibBuilder.loadTexts:
    outBr375.setUnits("tenth of Mbps")
_OutStream376_ObjectIdentity = ObjectIdentity
outStream376 = _OutStream376_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 385)
)
_OutBr376_Type = Integer32
_OutBr376_Object = MibScalar
outBr376 = _OutBr376_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 385, 1),
    _OutBr376_Type()
)
outBr376.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr376.setStatus("current")
if mibBuilder.loadTexts:
    outBr376.setUnits("tenth of Mbps")
_OutStream377_ObjectIdentity = ObjectIdentity
outStream377 = _OutStream377_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 386)
)
_OutBr377_Type = Integer32
_OutBr377_Object = MibScalar
outBr377 = _OutBr377_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 386, 1),
    _OutBr377_Type()
)
outBr377.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr377.setStatus("current")
if mibBuilder.loadTexts:
    outBr377.setUnits("tenth of Mbps")
_OutStream378_ObjectIdentity = ObjectIdentity
outStream378 = _OutStream378_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 387)
)
_OutBr378_Type = Integer32
_OutBr378_Object = MibScalar
outBr378 = _OutBr378_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 387, 1),
    _OutBr378_Type()
)
outBr378.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr378.setStatus("current")
if mibBuilder.loadTexts:
    outBr378.setUnits("tenth of Mbps")
_OutStream379_ObjectIdentity = ObjectIdentity
outStream379 = _OutStream379_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 388)
)
_OutBr379_Type = Integer32
_OutBr379_Object = MibScalar
outBr379 = _OutBr379_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 388, 1),
    _OutBr379_Type()
)
outBr379.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr379.setStatus("current")
if mibBuilder.loadTexts:
    outBr379.setUnits("tenth of Mbps")
_OutStream380_ObjectIdentity = ObjectIdentity
outStream380 = _OutStream380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 389)
)
_OutBr380_Type = Integer32
_OutBr380_Object = MibScalar
outBr380 = _OutBr380_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 389, 1),
    _OutBr380_Type()
)
outBr380.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr380.setStatus("current")
if mibBuilder.loadTexts:
    outBr380.setUnits("tenth of Mbps")
_OutStream381_ObjectIdentity = ObjectIdentity
outStream381 = _OutStream381_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 390)
)
_OutBr381_Type = Integer32
_OutBr381_Object = MibScalar
outBr381 = _OutBr381_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 390, 1),
    _OutBr381_Type()
)
outBr381.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr381.setStatus("current")
if mibBuilder.loadTexts:
    outBr381.setUnits("tenth of Mbps")
_OutStream382_ObjectIdentity = ObjectIdentity
outStream382 = _OutStream382_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 391)
)
_OutBr382_Type = Integer32
_OutBr382_Object = MibScalar
outBr382 = _OutBr382_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 391, 1),
    _OutBr382_Type()
)
outBr382.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr382.setStatus("current")
if mibBuilder.loadTexts:
    outBr382.setUnits("tenth of Mbps")
_OutStream383_ObjectIdentity = ObjectIdentity
outStream383 = _OutStream383_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 392)
)
_OutBr383_Type = Integer32
_OutBr383_Object = MibScalar
outBr383 = _OutBr383_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 392, 1),
    _OutBr383_Type()
)
outBr383.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr383.setStatus("current")
if mibBuilder.loadTexts:
    outBr383.setUnits("tenth of Mbps")
_OutStream384_ObjectIdentity = ObjectIdentity
outStream384 = _OutStream384_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 393)
)
_OutBr384_Type = Integer32
_OutBr384_Object = MibScalar
outBr384 = _OutBr384_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 393, 1),
    _OutBr384_Type()
)
outBr384.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr384.setStatus("current")
if mibBuilder.loadTexts:
    outBr384.setUnits("tenth of Mbps")
_OutStream385_ObjectIdentity = ObjectIdentity
outStream385 = _OutStream385_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 394)
)
_OutBr385_Type = Integer32
_OutBr385_Object = MibScalar
outBr385 = _OutBr385_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 394, 1),
    _OutBr385_Type()
)
outBr385.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr385.setStatus("current")
if mibBuilder.loadTexts:
    outBr385.setUnits("tenth of Mbps")
_OutStream386_ObjectIdentity = ObjectIdentity
outStream386 = _OutStream386_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 395)
)
_OutBr386_Type = Integer32
_OutBr386_Object = MibScalar
outBr386 = _OutBr386_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 395, 1),
    _OutBr386_Type()
)
outBr386.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr386.setStatus("current")
if mibBuilder.loadTexts:
    outBr386.setUnits("tenth of Mbps")
_OutStream387_ObjectIdentity = ObjectIdentity
outStream387 = _OutStream387_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 396)
)
_OutBr387_Type = Integer32
_OutBr387_Object = MibScalar
outBr387 = _OutBr387_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 396, 1),
    _OutBr387_Type()
)
outBr387.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr387.setStatus("current")
if mibBuilder.loadTexts:
    outBr387.setUnits("tenth of Mbps")
_OutStream388_ObjectIdentity = ObjectIdentity
outStream388 = _OutStream388_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 397)
)
_OutBr388_Type = Integer32
_OutBr388_Object = MibScalar
outBr388 = _OutBr388_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 397, 1),
    _OutBr388_Type()
)
outBr388.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr388.setStatus("current")
if mibBuilder.loadTexts:
    outBr388.setUnits("tenth of Mbps")
_OutStream389_ObjectIdentity = ObjectIdentity
outStream389 = _OutStream389_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 398)
)
_OutBr389_Type = Integer32
_OutBr389_Object = MibScalar
outBr389 = _OutBr389_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 398, 1),
    _OutBr389_Type()
)
outBr389.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr389.setStatus("current")
if mibBuilder.loadTexts:
    outBr389.setUnits("tenth of Mbps")
_OutStream390_ObjectIdentity = ObjectIdentity
outStream390 = _OutStream390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 399)
)
_OutBr390_Type = Integer32
_OutBr390_Object = MibScalar
outBr390 = _OutBr390_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 399, 1),
    _OutBr390_Type()
)
outBr390.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr390.setStatus("current")
if mibBuilder.loadTexts:
    outBr390.setUnits("tenth of Mbps")
_OutStream391_ObjectIdentity = ObjectIdentity
outStream391 = _OutStream391_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 400)
)
_OutBr391_Type = Integer32
_OutBr391_Object = MibScalar
outBr391 = _OutBr391_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 400, 1),
    _OutBr391_Type()
)
outBr391.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr391.setStatus("current")
if mibBuilder.loadTexts:
    outBr391.setUnits("tenth of Mbps")
_OutStream392_ObjectIdentity = ObjectIdentity
outStream392 = _OutStream392_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 401)
)
_OutBr392_Type = Integer32
_OutBr392_Object = MibScalar
outBr392 = _OutBr392_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 401, 1),
    _OutBr392_Type()
)
outBr392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr392.setStatus("current")
if mibBuilder.loadTexts:
    outBr392.setUnits("tenth of Mbps")
_OutStream393_ObjectIdentity = ObjectIdentity
outStream393 = _OutStream393_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 402)
)
_OutBr393_Type = Integer32
_OutBr393_Object = MibScalar
outBr393 = _OutBr393_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 402, 1),
    _OutBr393_Type()
)
outBr393.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr393.setStatus("current")
if mibBuilder.loadTexts:
    outBr393.setUnits("tenth of Mbps")
_OutStream394_ObjectIdentity = ObjectIdentity
outStream394 = _OutStream394_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 403)
)
_OutBr394_Type = Integer32
_OutBr394_Object = MibScalar
outBr394 = _OutBr394_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 403, 1),
    _OutBr394_Type()
)
outBr394.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr394.setStatus("current")
if mibBuilder.loadTexts:
    outBr394.setUnits("tenth of Mbps")
_OutStream395_ObjectIdentity = ObjectIdentity
outStream395 = _OutStream395_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 404)
)
_OutBr395_Type = Integer32
_OutBr395_Object = MibScalar
outBr395 = _OutBr395_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 404, 1),
    _OutBr395_Type()
)
outBr395.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr395.setStatus("current")
if mibBuilder.loadTexts:
    outBr395.setUnits("tenth of Mbps")
_OutStream396_ObjectIdentity = ObjectIdentity
outStream396 = _OutStream396_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 405)
)
_OutBr396_Type = Integer32
_OutBr396_Object = MibScalar
outBr396 = _OutBr396_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 405, 1),
    _OutBr396_Type()
)
outBr396.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr396.setStatus("current")
if mibBuilder.loadTexts:
    outBr396.setUnits("tenth of Mbps")
_OutStream397_ObjectIdentity = ObjectIdentity
outStream397 = _OutStream397_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 406)
)
_OutBr397_Type = Integer32
_OutBr397_Object = MibScalar
outBr397 = _OutBr397_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 406, 1),
    _OutBr397_Type()
)
outBr397.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr397.setStatus("current")
if mibBuilder.loadTexts:
    outBr397.setUnits("tenth of Mbps")
_OutStream398_ObjectIdentity = ObjectIdentity
outStream398 = _OutStream398_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 407)
)
_OutBr398_Type = Integer32
_OutBr398_Object = MibScalar
outBr398 = _OutBr398_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 407, 1),
    _OutBr398_Type()
)
outBr398.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr398.setStatus("current")
if mibBuilder.loadTexts:
    outBr398.setUnits("tenth of Mbps")
_OutStream399_ObjectIdentity = ObjectIdentity
outStream399 = _OutStream399_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 408)
)
_OutBr399_Type = Integer32
_OutBr399_Object = MibScalar
outBr399 = _OutBr399_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 408, 1),
    _OutBr399_Type()
)
outBr399.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr399.setStatus("current")
if mibBuilder.loadTexts:
    outBr399.setUnits("tenth of Mbps")
_OutStream400_ObjectIdentity = ObjectIdentity
outStream400 = _OutStream400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 409)
)
_OutBr400_Type = Integer32
_OutBr400_Object = MibScalar
outBr400 = _OutBr400_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 409, 1),
    _OutBr400_Type()
)
outBr400.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr400.setStatus("current")
if mibBuilder.loadTexts:
    outBr400.setUnits("tenth of Mbps")
_OutStream401_ObjectIdentity = ObjectIdentity
outStream401 = _OutStream401_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 410)
)
_OutBr401_Type = Integer32
_OutBr401_Object = MibScalar
outBr401 = _OutBr401_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 410, 1),
    _OutBr401_Type()
)
outBr401.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr401.setStatus("current")
if mibBuilder.loadTexts:
    outBr401.setUnits("tenth of Mbps")
_OutStream402_ObjectIdentity = ObjectIdentity
outStream402 = _OutStream402_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 411)
)
_OutBr402_Type = Integer32
_OutBr402_Object = MibScalar
outBr402 = _OutBr402_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 411, 1),
    _OutBr402_Type()
)
outBr402.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr402.setStatus("current")
if mibBuilder.loadTexts:
    outBr402.setUnits("tenth of Mbps")
_OutStream403_ObjectIdentity = ObjectIdentity
outStream403 = _OutStream403_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 412)
)
_OutBr403_Type = Integer32
_OutBr403_Object = MibScalar
outBr403 = _OutBr403_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 412, 1),
    _OutBr403_Type()
)
outBr403.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr403.setStatus("current")
if mibBuilder.loadTexts:
    outBr403.setUnits("tenth of Mbps")
_OutStream404_ObjectIdentity = ObjectIdentity
outStream404 = _OutStream404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 413)
)
_OutBr404_Type = Integer32
_OutBr404_Object = MibScalar
outBr404 = _OutBr404_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 413, 1),
    _OutBr404_Type()
)
outBr404.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr404.setStatus("current")
if mibBuilder.loadTexts:
    outBr404.setUnits("tenth of Mbps")
_OutStream405_ObjectIdentity = ObjectIdentity
outStream405 = _OutStream405_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 414)
)
_OutBr405_Type = Integer32
_OutBr405_Object = MibScalar
outBr405 = _OutBr405_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 414, 1),
    _OutBr405_Type()
)
outBr405.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr405.setStatus("current")
if mibBuilder.loadTexts:
    outBr405.setUnits("tenth of Mbps")
_OutStream406_ObjectIdentity = ObjectIdentity
outStream406 = _OutStream406_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 415)
)
_OutBr406_Type = Integer32
_OutBr406_Object = MibScalar
outBr406 = _OutBr406_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 415, 1),
    _OutBr406_Type()
)
outBr406.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr406.setStatus("current")
if mibBuilder.loadTexts:
    outBr406.setUnits("tenth of Mbps")
_OutStream407_ObjectIdentity = ObjectIdentity
outStream407 = _OutStream407_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 416)
)
_OutBr407_Type = Integer32
_OutBr407_Object = MibScalar
outBr407 = _OutBr407_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 416, 1),
    _OutBr407_Type()
)
outBr407.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr407.setStatus("current")
if mibBuilder.loadTexts:
    outBr407.setUnits("tenth of Mbps")
_OutStream408_ObjectIdentity = ObjectIdentity
outStream408 = _OutStream408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 417)
)
_OutBr408_Type = Integer32
_OutBr408_Object = MibScalar
outBr408 = _OutBr408_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 417, 1),
    _OutBr408_Type()
)
outBr408.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr408.setStatus("current")
if mibBuilder.loadTexts:
    outBr408.setUnits("tenth of Mbps")
_OutStream409_ObjectIdentity = ObjectIdentity
outStream409 = _OutStream409_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 418)
)
_OutBr409_Type = Integer32
_OutBr409_Object = MibScalar
outBr409 = _OutBr409_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 418, 1),
    _OutBr409_Type()
)
outBr409.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr409.setStatus("current")
if mibBuilder.loadTexts:
    outBr409.setUnits("tenth of Mbps")
_OutStream410_ObjectIdentity = ObjectIdentity
outStream410 = _OutStream410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 419)
)
_OutBr410_Type = Integer32
_OutBr410_Object = MibScalar
outBr410 = _OutBr410_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 419, 1),
    _OutBr410_Type()
)
outBr410.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr410.setStatus("current")
if mibBuilder.loadTexts:
    outBr410.setUnits("tenth of Mbps")
_OutStream411_ObjectIdentity = ObjectIdentity
outStream411 = _OutStream411_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 420)
)
_OutBr411_Type = Integer32
_OutBr411_Object = MibScalar
outBr411 = _OutBr411_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 420, 1),
    _OutBr411_Type()
)
outBr411.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr411.setStatus("current")
if mibBuilder.loadTexts:
    outBr411.setUnits("tenth of Mbps")
_OutStream412_ObjectIdentity = ObjectIdentity
outStream412 = _OutStream412_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 421)
)
_OutBr412_Type = Integer32
_OutBr412_Object = MibScalar
outBr412 = _OutBr412_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 421, 1),
    _OutBr412_Type()
)
outBr412.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr412.setStatus("current")
if mibBuilder.loadTexts:
    outBr412.setUnits("tenth of Mbps")
_OutStream413_ObjectIdentity = ObjectIdentity
outStream413 = _OutStream413_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 422)
)
_OutBr413_Type = Integer32
_OutBr413_Object = MibScalar
outBr413 = _OutBr413_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 422, 1),
    _OutBr413_Type()
)
outBr413.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr413.setStatus("current")
if mibBuilder.loadTexts:
    outBr413.setUnits("tenth of Mbps")
_OutStream414_ObjectIdentity = ObjectIdentity
outStream414 = _OutStream414_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 423)
)
_OutBr414_Type = Integer32
_OutBr414_Object = MibScalar
outBr414 = _OutBr414_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 423, 1),
    _OutBr414_Type()
)
outBr414.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr414.setStatus("current")
if mibBuilder.loadTexts:
    outBr414.setUnits("tenth of Mbps")
_OutStream415_ObjectIdentity = ObjectIdentity
outStream415 = _OutStream415_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 424)
)
_OutBr415_Type = Integer32
_OutBr415_Object = MibScalar
outBr415 = _OutBr415_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 424, 1),
    _OutBr415_Type()
)
outBr415.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr415.setStatus("current")
if mibBuilder.loadTexts:
    outBr415.setUnits("tenth of Mbps")
_OutStream416_ObjectIdentity = ObjectIdentity
outStream416 = _OutStream416_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 425)
)
_OutBr416_Type = Integer32
_OutBr416_Object = MibScalar
outBr416 = _OutBr416_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 425, 1),
    _OutBr416_Type()
)
outBr416.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr416.setStatus("current")
if mibBuilder.loadTexts:
    outBr416.setUnits("tenth of Mbps")
_OutStream417_ObjectIdentity = ObjectIdentity
outStream417 = _OutStream417_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 426)
)
_OutBr417_Type = Integer32
_OutBr417_Object = MibScalar
outBr417 = _OutBr417_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 426, 1),
    _OutBr417_Type()
)
outBr417.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr417.setStatus("current")
if mibBuilder.loadTexts:
    outBr417.setUnits("tenth of Mbps")
_OutStream418_ObjectIdentity = ObjectIdentity
outStream418 = _OutStream418_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 427)
)
_OutBr418_Type = Integer32
_OutBr418_Object = MibScalar
outBr418 = _OutBr418_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 427, 1),
    _OutBr418_Type()
)
outBr418.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr418.setStatus("current")
if mibBuilder.loadTexts:
    outBr418.setUnits("tenth of Mbps")
_OutStream419_ObjectIdentity = ObjectIdentity
outStream419 = _OutStream419_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 428)
)
_OutBr419_Type = Integer32
_OutBr419_Object = MibScalar
outBr419 = _OutBr419_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 428, 1),
    _OutBr419_Type()
)
outBr419.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr419.setStatus("current")
if mibBuilder.loadTexts:
    outBr419.setUnits("tenth of Mbps")
_OutStream420_ObjectIdentity = ObjectIdentity
outStream420 = _OutStream420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 429)
)
_OutBr420_Type = Integer32
_OutBr420_Object = MibScalar
outBr420 = _OutBr420_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 429, 1),
    _OutBr420_Type()
)
outBr420.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr420.setStatus("current")
if mibBuilder.loadTexts:
    outBr420.setUnits("tenth of Mbps")
_OutStream421_ObjectIdentity = ObjectIdentity
outStream421 = _OutStream421_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 430)
)
_OutBr421_Type = Integer32
_OutBr421_Object = MibScalar
outBr421 = _OutBr421_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 430, 1),
    _OutBr421_Type()
)
outBr421.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr421.setStatus("current")
if mibBuilder.loadTexts:
    outBr421.setUnits("tenth of Mbps")
_OutStream422_ObjectIdentity = ObjectIdentity
outStream422 = _OutStream422_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 431)
)
_OutBr422_Type = Integer32
_OutBr422_Object = MibScalar
outBr422 = _OutBr422_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 431, 1),
    _OutBr422_Type()
)
outBr422.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr422.setStatus("current")
if mibBuilder.loadTexts:
    outBr422.setUnits("tenth of Mbps")
_OutStream423_ObjectIdentity = ObjectIdentity
outStream423 = _OutStream423_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 432)
)
_OutBr423_Type = Integer32
_OutBr423_Object = MibScalar
outBr423 = _OutBr423_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 432, 1),
    _OutBr423_Type()
)
outBr423.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr423.setStatus("current")
if mibBuilder.loadTexts:
    outBr423.setUnits("tenth of Mbps")
_OutStream424_ObjectIdentity = ObjectIdentity
outStream424 = _OutStream424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 433)
)
_OutBr424_Type = Integer32
_OutBr424_Object = MibScalar
outBr424 = _OutBr424_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 433, 1),
    _OutBr424_Type()
)
outBr424.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr424.setStatus("current")
if mibBuilder.loadTexts:
    outBr424.setUnits("tenth of Mbps")
_OutStream425_ObjectIdentity = ObjectIdentity
outStream425 = _OutStream425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 434)
)
_OutBr425_Type = Integer32
_OutBr425_Object = MibScalar
outBr425 = _OutBr425_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 434, 1),
    _OutBr425_Type()
)
outBr425.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr425.setStatus("current")
if mibBuilder.loadTexts:
    outBr425.setUnits("tenth of Mbps")
_OutStream426_ObjectIdentity = ObjectIdentity
outStream426 = _OutStream426_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 435)
)
_OutBr426_Type = Integer32
_OutBr426_Object = MibScalar
outBr426 = _OutBr426_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 435, 1),
    _OutBr426_Type()
)
outBr426.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr426.setStatus("current")
if mibBuilder.loadTexts:
    outBr426.setUnits("tenth of Mbps")
_OutStream427_ObjectIdentity = ObjectIdentity
outStream427 = _OutStream427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 436)
)
_OutBr427_Type = Integer32
_OutBr427_Object = MibScalar
outBr427 = _OutBr427_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 436, 1),
    _OutBr427_Type()
)
outBr427.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr427.setStatus("current")
if mibBuilder.loadTexts:
    outBr427.setUnits("tenth of Mbps")
_OutStream428_ObjectIdentity = ObjectIdentity
outStream428 = _OutStream428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 437)
)
_OutBr428_Type = Integer32
_OutBr428_Object = MibScalar
outBr428 = _OutBr428_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 437, 1),
    _OutBr428_Type()
)
outBr428.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr428.setStatus("current")
if mibBuilder.loadTexts:
    outBr428.setUnits("tenth of Mbps")
_OutStream429_ObjectIdentity = ObjectIdentity
outStream429 = _OutStream429_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 438)
)
_OutBr429_Type = Integer32
_OutBr429_Object = MibScalar
outBr429 = _OutBr429_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 438, 1),
    _OutBr429_Type()
)
outBr429.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr429.setStatus("current")
if mibBuilder.loadTexts:
    outBr429.setUnits("tenth of Mbps")
_OutStream430_ObjectIdentity = ObjectIdentity
outStream430 = _OutStream430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 439)
)
_OutBr430_Type = Integer32
_OutBr430_Object = MibScalar
outBr430 = _OutBr430_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 439, 1),
    _OutBr430_Type()
)
outBr430.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr430.setStatus("current")
if mibBuilder.loadTexts:
    outBr430.setUnits("tenth of Mbps")
_OutStream431_ObjectIdentity = ObjectIdentity
outStream431 = _OutStream431_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 440)
)
_OutBr431_Type = Integer32
_OutBr431_Object = MibScalar
outBr431 = _OutBr431_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 440, 1),
    _OutBr431_Type()
)
outBr431.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr431.setStatus("current")
if mibBuilder.loadTexts:
    outBr431.setUnits("tenth of Mbps")
_OutStream432_ObjectIdentity = ObjectIdentity
outStream432 = _OutStream432_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 441)
)
_OutBr432_Type = Integer32
_OutBr432_Object = MibScalar
outBr432 = _OutBr432_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 441, 1),
    _OutBr432_Type()
)
outBr432.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr432.setStatus("current")
if mibBuilder.loadTexts:
    outBr432.setUnits("tenth of Mbps")
_OutStream433_ObjectIdentity = ObjectIdentity
outStream433 = _OutStream433_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 442)
)
_OutBr433_Type = Integer32
_OutBr433_Object = MibScalar
outBr433 = _OutBr433_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 442, 1),
    _OutBr433_Type()
)
outBr433.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr433.setStatus("current")
if mibBuilder.loadTexts:
    outBr433.setUnits("tenth of Mbps")
_OutStream434_ObjectIdentity = ObjectIdentity
outStream434 = _OutStream434_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 443)
)
_OutBr434_Type = Integer32
_OutBr434_Object = MibScalar
outBr434 = _OutBr434_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 443, 1),
    _OutBr434_Type()
)
outBr434.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr434.setStatus("current")
if mibBuilder.loadTexts:
    outBr434.setUnits("tenth of Mbps")
_OutStream435_ObjectIdentity = ObjectIdentity
outStream435 = _OutStream435_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 444)
)
_OutBr435_Type = Integer32
_OutBr435_Object = MibScalar
outBr435 = _OutBr435_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 444, 1),
    _OutBr435_Type()
)
outBr435.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr435.setStatus("current")
if mibBuilder.loadTexts:
    outBr435.setUnits("tenth of Mbps")
_OutStream436_ObjectIdentity = ObjectIdentity
outStream436 = _OutStream436_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 445)
)
_OutBr436_Type = Integer32
_OutBr436_Object = MibScalar
outBr436 = _OutBr436_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 445, 1),
    _OutBr436_Type()
)
outBr436.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr436.setStatus("current")
if mibBuilder.loadTexts:
    outBr436.setUnits("tenth of Mbps")
_OutStream437_ObjectIdentity = ObjectIdentity
outStream437 = _OutStream437_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 446)
)
_OutBr437_Type = Integer32
_OutBr437_Object = MibScalar
outBr437 = _OutBr437_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 446, 1),
    _OutBr437_Type()
)
outBr437.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr437.setStatus("current")
if mibBuilder.loadTexts:
    outBr437.setUnits("tenth of Mbps")
_OutStream438_ObjectIdentity = ObjectIdentity
outStream438 = _OutStream438_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 447)
)
_OutBr438_Type = Integer32
_OutBr438_Object = MibScalar
outBr438 = _OutBr438_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 447, 1),
    _OutBr438_Type()
)
outBr438.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr438.setStatus("current")
if mibBuilder.loadTexts:
    outBr438.setUnits("tenth of Mbps")
_OutStream439_ObjectIdentity = ObjectIdentity
outStream439 = _OutStream439_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 448)
)
_OutBr439_Type = Integer32
_OutBr439_Object = MibScalar
outBr439 = _OutBr439_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 448, 1),
    _OutBr439_Type()
)
outBr439.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr439.setStatus("current")
if mibBuilder.loadTexts:
    outBr439.setUnits("tenth of Mbps")
_OutStream440_ObjectIdentity = ObjectIdentity
outStream440 = _OutStream440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 449)
)
_OutBr440_Type = Integer32
_OutBr440_Object = MibScalar
outBr440 = _OutBr440_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 449, 1),
    _OutBr440_Type()
)
outBr440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr440.setStatus("current")
if mibBuilder.loadTexts:
    outBr440.setUnits("tenth of Mbps")
_OutStream441_ObjectIdentity = ObjectIdentity
outStream441 = _OutStream441_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 450)
)
_OutBr441_Type = Integer32
_OutBr441_Object = MibScalar
outBr441 = _OutBr441_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 450, 1),
    _OutBr441_Type()
)
outBr441.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr441.setStatus("current")
if mibBuilder.loadTexts:
    outBr441.setUnits("tenth of Mbps")
_OutStream442_ObjectIdentity = ObjectIdentity
outStream442 = _OutStream442_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 451)
)
_OutBr442_Type = Integer32
_OutBr442_Object = MibScalar
outBr442 = _OutBr442_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 451, 1),
    _OutBr442_Type()
)
outBr442.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr442.setStatus("current")
if mibBuilder.loadTexts:
    outBr442.setUnits("tenth of Mbps")
_OutStream443_ObjectIdentity = ObjectIdentity
outStream443 = _OutStream443_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 452)
)
_OutBr443_Type = Integer32
_OutBr443_Object = MibScalar
outBr443 = _OutBr443_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 452, 1),
    _OutBr443_Type()
)
outBr443.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr443.setStatus("current")
if mibBuilder.loadTexts:
    outBr443.setUnits("tenth of Mbps")
_OutStream444_ObjectIdentity = ObjectIdentity
outStream444 = _OutStream444_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 453)
)
_OutBr444_Type = Integer32
_OutBr444_Object = MibScalar
outBr444 = _OutBr444_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 453, 1),
    _OutBr444_Type()
)
outBr444.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr444.setStatus("current")
if mibBuilder.loadTexts:
    outBr444.setUnits("tenth of Mbps")
_OutStream445_ObjectIdentity = ObjectIdentity
outStream445 = _OutStream445_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 454)
)
_OutBr445_Type = Integer32
_OutBr445_Object = MibScalar
outBr445 = _OutBr445_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 454, 1),
    _OutBr445_Type()
)
outBr445.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr445.setStatus("current")
if mibBuilder.loadTexts:
    outBr445.setUnits("tenth of Mbps")
_OutStream446_ObjectIdentity = ObjectIdentity
outStream446 = _OutStream446_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 455)
)
_OutBr446_Type = Integer32
_OutBr446_Object = MibScalar
outBr446 = _OutBr446_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 455, 1),
    _OutBr446_Type()
)
outBr446.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr446.setStatus("current")
if mibBuilder.loadTexts:
    outBr446.setUnits("tenth of Mbps")
_OutStream447_ObjectIdentity = ObjectIdentity
outStream447 = _OutStream447_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 456)
)
_OutBr447_Type = Integer32
_OutBr447_Object = MibScalar
outBr447 = _OutBr447_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 456, 1),
    _OutBr447_Type()
)
outBr447.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr447.setStatus("current")
if mibBuilder.loadTexts:
    outBr447.setUnits("tenth of Mbps")
_OutStream448_ObjectIdentity = ObjectIdentity
outStream448 = _OutStream448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 457)
)
_OutBr448_Type = Integer32
_OutBr448_Object = MibScalar
outBr448 = _OutBr448_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 457, 1),
    _OutBr448_Type()
)
outBr448.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr448.setStatus("current")
if mibBuilder.loadTexts:
    outBr448.setUnits("tenth of Mbps")
_OutStream449_ObjectIdentity = ObjectIdentity
outStream449 = _OutStream449_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 458)
)
_OutBr449_Type = Integer32
_OutBr449_Object = MibScalar
outBr449 = _OutBr449_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 458, 1),
    _OutBr449_Type()
)
outBr449.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr449.setStatus("current")
if mibBuilder.loadTexts:
    outBr449.setUnits("tenth of Mbps")
_OutStream450_ObjectIdentity = ObjectIdentity
outStream450 = _OutStream450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 459)
)
_OutBr450_Type = Integer32
_OutBr450_Object = MibScalar
outBr450 = _OutBr450_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 459, 1),
    _OutBr450_Type()
)
outBr450.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr450.setStatus("current")
if mibBuilder.loadTexts:
    outBr450.setUnits("tenth of Mbps")
_OutStream451_ObjectIdentity = ObjectIdentity
outStream451 = _OutStream451_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 460)
)
_OutBr451_Type = Integer32
_OutBr451_Object = MibScalar
outBr451 = _OutBr451_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 460, 1),
    _OutBr451_Type()
)
outBr451.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr451.setStatus("current")
if mibBuilder.loadTexts:
    outBr451.setUnits("tenth of Mbps")
_OutStream452_ObjectIdentity = ObjectIdentity
outStream452 = _OutStream452_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 461)
)
_OutBr452_Type = Integer32
_OutBr452_Object = MibScalar
outBr452 = _OutBr452_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 461, 1),
    _OutBr452_Type()
)
outBr452.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr452.setStatus("current")
if mibBuilder.loadTexts:
    outBr452.setUnits("tenth of Mbps")
_OutStream453_ObjectIdentity = ObjectIdentity
outStream453 = _OutStream453_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 462)
)
_OutBr453_Type = Integer32
_OutBr453_Object = MibScalar
outBr453 = _OutBr453_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 462, 1),
    _OutBr453_Type()
)
outBr453.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr453.setStatus("current")
if mibBuilder.loadTexts:
    outBr453.setUnits("tenth of Mbps")
_OutStream454_ObjectIdentity = ObjectIdentity
outStream454 = _OutStream454_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 463)
)
_OutBr454_Type = Integer32
_OutBr454_Object = MibScalar
outBr454 = _OutBr454_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 463, 1),
    _OutBr454_Type()
)
outBr454.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr454.setStatus("current")
if mibBuilder.loadTexts:
    outBr454.setUnits("tenth of Mbps")
_OutStream455_ObjectIdentity = ObjectIdentity
outStream455 = _OutStream455_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 464)
)
_OutBr455_Type = Integer32
_OutBr455_Object = MibScalar
outBr455 = _OutBr455_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 464, 1),
    _OutBr455_Type()
)
outBr455.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr455.setStatus("current")
if mibBuilder.loadTexts:
    outBr455.setUnits("tenth of Mbps")
_OutStream456_ObjectIdentity = ObjectIdentity
outStream456 = _OutStream456_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 465)
)
_OutBr456_Type = Integer32
_OutBr456_Object = MibScalar
outBr456 = _OutBr456_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 465, 1),
    _OutBr456_Type()
)
outBr456.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr456.setStatus("current")
if mibBuilder.loadTexts:
    outBr456.setUnits("tenth of Mbps")
_OutStream457_ObjectIdentity = ObjectIdentity
outStream457 = _OutStream457_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 466)
)
_OutBr457_Type = Integer32
_OutBr457_Object = MibScalar
outBr457 = _OutBr457_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 466, 1),
    _OutBr457_Type()
)
outBr457.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr457.setStatus("current")
if mibBuilder.loadTexts:
    outBr457.setUnits("tenth of Mbps")
_OutStream458_ObjectIdentity = ObjectIdentity
outStream458 = _OutStream458_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 467)
)
_OutBr458_Type = Integer32
_OutBr458_Object = MibScalar
outBr458 = _OutBr458_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 467, 1),
    _OutBr458_Type()
)
outBr458.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr458.setStatus("current")
if mibBuilder.loadTexts:
    outBr458.setUnits("tenth of Mbps")
_OutStream459_ObjectIdentity = ObjectIdentity
outStream459 = _OutStream459_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 468)
)
_OutBr459_Type = Integer32
_OutBr459_Object = MibScalar
outBr459 = _OutBr459_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 468, 1),
    _OutBr459_Type()
)
outBr459.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr459.setStatus("current")
if mibBuilder.loadTexts:
    outBr459.setUnits("tenth of Mbps")
_OutStream460_ObjectIdentity = ObjectIdentity
outStream460 = _OutStream460_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 469)
)
_OutBr460_Type = Integer32
_OutBr460_Object = MibScalar
outBr460 = _OutBr460_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 469, 1),
    _OutBr460_Type()
)
outBr460.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr460.setStatus("current")
if mibBuilder.loadTexts:
    outBr460.setUnits("tenth of Mbps")
_OutStream461_ObjectIdentity = ObjectIdentity
outStream461 = _OutStream461_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 470)
)
_OutBr461_Type = Integer32
_OutBr461_Object = MibScalar
outBr461 = _OutBr461_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 470, 1),
    _OutBr461_Type()
)
outBr461.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr461.setStatus("current")
if mibBuilder.loadTexts:
    outBr461.setUnits("tenth of Mbps")
_OutStream462_ObjectIdentity = ObjectIdentity
outStream462 = _OutStream462_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 471)
)
_OutBr462_Type = Integer32
_OutBr462_Object = MibScalar
outBr462 = _OutBr462_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 471, 1),
    _OutBr462_Type()
)
outBr462.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr462.setStatus("current")
if mibBuilder.loadTexts:
    outBr462.setUnits("tenth of Mbps")
_OutStream463_ObjectIdentity = ObjectIdentity
outStream463 = _OutStream463_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 472)
)
_OutBr463_Type = Integer32
_OutBr463_Object = MibScalar
outBr463 = _OutBr463_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 472, 1),
    _OutBr463_Type()
)
outBr463.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr463.setStatus("current")
if mibBuilder.loadTexts:
    outBr463.setUnits("tenth of Mbps")
_OutStream464_ObjectIdentity = ObjectIdentity
outStream464 = _OutStream464_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 473)
)
_OutBr464_Type = Integer32
_OutBr464_Object = MibScalar
outBr464 = _OutBr464_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 473, 1),
    _OutBr464_Type()
)
outBr464.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr464.setStatus("current")
if mibBuilder.loadTexts:
    outBr464.setUnits("tenth of Mbps")
_OutStream465_ObjectIdentity = ObjectIdentity
outStream465 = _OutStream465_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 474)
)
_OutBr465_Type = Integer32
_OutBr465_Object = MibScalar
outBr465 = _OutBr465_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 474, 1),
    _OutBr465_Type()
)
outBr465.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr465.setStatus("current")
if mibBuilder.loadTexts:
    outBr465.setUnits("tenth of Mbps")
_OutStream466_ObjectIdentity = ObjectIdentity
outStream466 = _OutStream466_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 475)
)
_OutBr466_Type = Integer32
_OutBr466_Object = MibScalar
outBr466 = _OutBr466_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 475, 1),
    _OutBr466_Type()
)
outBr466.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr466.setStatus("current")
if mibBuilder.loadTexts:
    outBr466.setUnits("tenth of Mbps")
_OutStream467_ObjectIdentity = ObjectIdentity
outStream467 = _OutStream467_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 476)
)
_OutBr467_Type = Integer32
_OutBr467_Object = MibScalar
outBr467 = _OutBr467_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 476, 1),
    _OutBr467_Type()
)
outBr467.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr467.setStatus("current")
if mibBuilder.loadTexts:
    outBr467.setUnits("tenth of Mbps")
_OutStream468_ObjectIdentity = ObjectIdentity
outStream468 = _OutStream468_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 477)
)
_OutBr468_Type = Integer32
_OutBr468_Object = MibScalar
outBr468 = _OutBr468_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 477, 1),
    _OutBr468_Type()
)
outBr468.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr468.setStatus("current")
if mibBuilder.loadTexts:
    outBr468.setUnits("tenth of Mbps")
_OutStream469_ObjectIdentity = ObjectIdentity
outStream469 = _OutStream469_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 478)
)
_OutBr469_Type = Integer32
_OutBr469_Object = MibScalar
outBr469 = _OutBr469_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 478, 1),
    _OutBr469_Type()
)
outBr469.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr469.setStatus("current")
if mibBuilder.loadTexts:
    outBr469.setUnits("tenth of Mbps")
_OutStream470_ObjectIdentity = ObjectIdentity
outStream470 = _OutStream470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 479)
)
_OutBr470_Type = Integer32
_OutBr470_Object = MibScalar
outBr470 = _OutBr470_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 479, 1),
    _OutBr470_Type()
)
outBr470.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr470.setStatus("current")
if mibBuilder.loadTexts:
    outBr470.setUnits("tenth of Mbps")
_OutStream471_ObjectIdentity = ObjectIdentity
outStream471 = _OutStream471_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 480)
)
_OutBr471_Type = Integer32
_OutBr471_Object = MibScalar
outBr471 = _OutBr471_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 480, 1),
    _OutBr471_Type()
)
outBr471.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr471.setStatus("current")
if mibBuilder.loadTexts:
    outBr471.setUnits("tenth of Mbps")
_OutStream472_ObjectIdentity = ObjectIdentity
outStream472 = _OutStream472_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 481)
)
_OutBr472_Type = Integer32
_OutBr472_Object = MibScalar
outBr472 = _OutBr472_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 481, 1),
    _OutBr472_Type()
)
outBr472.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr472.setStatus("current")
if mibBuilder.loadTexts:
    outBr472.setUnits("tenth of Mbps")
_OutStream473_ObjectIdentity = ObjectIdentity
outStream473 = _OutStream473_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 482)
)
_OutBr473_Type = Integer32
_OutBr473_Object = MibScalar
outBr473 = _OutBr473_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 482, 1),
    _OutBr473_Type()
)
outBr473.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr473.setStatus("current")
if mibBuilder.loadTexts:
    outBr473.setUnits("tenth of Mbps")
_OutStream474_ObjectIdentity = ObjectIdentity
outStream474 = _OutStream474_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 483)
)
_OutBr474_Type = Integer32
_OutBr474_Object = MibScalar
outBr474 = _OutBr474_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 483, 1),
    _OutBr474_Type()
)
outBr474.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr474.setStatus("current")
if mibBuilder.loadTexts:
    outBr474.setUnits("tenth of Mbps")
_OutStream475_ObjectIdentity = ObjectIdentity
outStream475 = _OutStream475_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 484)
)
_OutBr475_Type = Integer32
_OutBr475_Object = MibScalar
outBr475 = _OutBr475_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 484, 1),
    _OutBr475_Type()
)
outBr475.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr475.setStatus("current")
if mibBuilder.loadTexts:
    outBr475.setUnits("tenth of Mbps")
_OutStream476_ObjectIdentity = ObjectIdentity
outStream476 = _OutStream476_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 485)
)
_OutBr476_Type = Integer32
_OutBr476_Object = MibScalar
outBr476 = _OutBr476_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 485, 1),
    _OutBr476_Type()
)
outBr476.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr476.setStatus("current")
if mibBuilder.loadTexts:
    outBr476.setUnits("tenth of Mbps")
_OutStream477_ObjectIdentity = ObjectIdentity
outStream477 = _OutStream477_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 486)
)
_OutBr477_Type = Integer32
_OutBr477_Object = MibScalar
outBr477 = _OutBr477_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 486, 1),
    _OutBr477_Type()
)
outBr477.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr477.setStatus("current")
if mibBuilder.loadTexts:
    outBr477.setUnits("tenth of Mbps")
_OutStream478_ObjectIdentity = ObjectIdentity
outStream478 = _OutStream478_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 487)
)
_OutBr478_Type = Integer32
_OutBr478_Object = MibScalar
outBr478 = _OutBr478_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 487, 1),
    _OutBr478_Type()
)
outBr478.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr478.setStatus("current")
if mibBuilder.loadTexts:
    outBr478.setUnits("tenth of Mbps")
_OutStream479_ObjectIdentity = ObjectIdentity
outStream479 = _OutStream479_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 488)
)
_OutBr479_Type = Integer32
_OutBr479_Object = MibScalar
outBr479 = _OutBr479_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 488, 1),
    _OutBr479_Type()
)
outBr479.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr479.setStatus("current")
if mibBuilder.loadTexts:
    outBr479.setUnits("tenth of Mbps")
_OutStream480_ObjectIdentity = ObjectIdentity
outStream480 = _OutStream480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 489)
)
_OutBr480_Type = Integer32
_OutBr480_Object = MibScalar
outBr480 = _OutBr480_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 489, 1),
    _OutBr480_Type()
)
outBr480.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr480.setStatus("current")
if mibBuilder.loadTexts:
    outBr480.setUnits("tenth of Mbps")
_OutStream481_ObjectIdentity = ObjectIdentity
outStream481 = _OutStream481_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 490)
)
_OutBr481_Type = Integer32
_OutBr481_Object = MibScalar
outBr481 = _OutBr481_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 490, 1),
    _OutBr481_Type()
)
outBr481.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr481.setStatus("current")
if mibBuilder.loadTexts:
    outBr481.setUnits("tenth of Mbps")
_OutStream482_ObjectIdentity = ObjectIdentity
outStream482 = _OutStream482_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 491)
)
_OutBr482_Type = Integer32
_OutBr482_Object = MibScalar
outBr482 = _OutBr482_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 491, 1),
    _OutBr482_Type()
)
outBr482.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr482.setStatus("current")
if mibBuilder.loadTexts:
    outBr482.setUnits("tenth of Mbps")
_OutStream483_ObjectIdentity = ObjectIdentity
outStream483 = _OutStream483_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 492)
)
_OutBr483_Type = Integer32
_OutBr483_Object = MibScalar
outBr483 = _OutBr483_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 492, 1),
    _OutBr483_Type()
)
outBr483.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr483.setStatus("current")
if mibBuilder.loadTexts:
    outBr483.setUnits("tenth of Mbps")
_OutStream484_ObjectIdentity = ObjectIdentity
outStream484 = _OutStream484_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 493)
)
_OutBr484_Type = Integer32
_OutBr484_Object = MibScalar
outBr484 = _OutBr484_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 493, 1),
    _OutBr484_Type()
)
outBr484.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr484.setStatus("current")
if mibBuilder.loadTexts:
    outBr484.setUnits("tenth of Mbps")
_OutStream485_ObjectIdentity = ObjectIdentity
outStream485 = _OutStream485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 494)
)
_OutBr485_Type = Integer32
_OutBr485_Object = MibScalar
outBr485 = _OutBr485_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 494, 1),
    _OutBr485_Type()
)
outBr485.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr485.setStatus("current")
if mibBuilder.loadTexts:
    outBr485.setUnits("tenth of Mbps")
_OutStream486_ObjectIdentity = ObjectIdentity
outStream486 = _OutStream486_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 495)
)
_OutBr486_Type = Integer32
_OutBr486_Object = MibScalar
outBr486 = _OutBr486_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 495, 1),
    _OutBr486_Type()
)
outBr486.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr486.setStatus("current")
if mibBuilder.loadTexts:
    outBr486.setUnits("tenth of Mbps")
_OutStream487_ObjectIdentity = ObjectIdentity
outStream487 = _OutStream487_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 496)
)
_OutBr487_Type = Integer32
_OutBr487_Object = MibScalar
outBr487 = _OutBr487_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 496, 1),
    _OutBr487_Type()
)
outBr487.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr487.setStatus("current")
if mibBuilder.loadTexts:
    outBr487.setUnits("tenth of Mbps")
_OutStream488_ObjectIdentity = ObjectIdentity
outStream488 = _OutStream488_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 497)
)
_OutBr488_Type = Integer32
_OutBr488_Object = MibScalar
outBr488 = _OutBr488_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 497, 1),
    _OutBr488_Type()
)
outBr488.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr488.setStatus("current")
if mibBuilder.loadTexts:
    outBr488.setUnits("tenth of Mbps")
_OutStream489_ObjectIdentity = ObjectIdentity
outStream489 = _OutStream489_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 498)
)
_OutBr489_Type = Integer32
_OutBr489_Object = MibScalar
outBr489 = _OutBr489_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 498, 1),
    _OutBr489_Type()
)
outBr489.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr489.setStatus("current")
if mibBuilder.loadTexts:
    outBr489.setUnits("tenth of Mbps")
_OutStream490_ObjectIdentity = ObjectIdentity
outStream490 = _OutStream490_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 499)
)
_OutBr490_Type = Integer32
_OutBr490_Object = MibScalar
outBr490 = _OutBr490_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 499, 1),
    _OutBr490_Type()
)
outBr490.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr490.setStatus("current")
if mibBuilder.loadTexts:
    outBr490.setUnits("tenth of Mbps")
_OutStream491_ObjectIdentity = ObjectIdentity
outStream491 = _OutStream491_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 500)
)
_OutBr491_Type = Integer32
_OutBr491_Object = MibScalar
outBr491 = _OutBr491_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 500, 1),
    _OutBr491_Type()
)
outBr491.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr491.setStatus("current")
if mibBuilder.loadTexts:
    outBr491.setUnits("tenth of Mbps")
_OutStream492_ObjectIdentity = ObjectIdentity
outStream492 = _OutStream492_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 501)
)
_OutBr492_Type = Integer32
_OutBr492_Object = MibScalar
outBr492 = _OutBr492_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 501, 1),
    _OutBr492_Type()
)
outBr492.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr492.setStatus("current")
if mibBuilder.loadTexts:
    outBr492.setUnits("tenth of Mbps")
_OutStream493_ObjectIdentity = ObjectIdentity
outStream493 = _OutStream493_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 502)
)
_OutBr493_Type = Integer32
_OutBr493_Object = MibScalar
outBr493 = _OutBr493_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 502, 1),
    _OutBr493_Type()
)
outBr493.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr493.setStatus("current")
if mibBuilder.loadTexts:
    outBr493.setUnits("tenth of Mbps")
_OutStream494_ObjectIdentity = ObjectIdentity
outStream494 = _OutStream494_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 503)
)
_OutBr494_Type = Integer32
_OutBr494_Object = MibScalar
outBr494 = _OutBr494_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 503, 1),
    _OutBr494_Type()
)
outBr494.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr494.setStatus("current")
if mibBuilder.loadTexts:
    outBr494.setUnits("tenth of Mbps")
_OutStream495_ObjectIdentity = ObjectIdentity
outStream495 = _OutStream495_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 504)
)
_OutBr495_Type = Integer32
_OutBr495_Object = MibScalar
outBr495 = _OutBr495_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 504, 1),
    _OutBr495_Type()
)
outBr495.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr495.setStatus("current")
if mibBuilder.loadTexts:
    outBr495.setUnits("tenth of Mbps")
_OutStream496_ObjectIdentity = ObjectIdentity
outStream496 = _OutStream496_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 505)
)
_OutBr496_Type = Integer32
_OutBr496_Object = MibScalar
outBr496 = _OutBr496_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 505, 1),
    _OutBr496_Type()
)
outBr496.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr496.setStatus("current")
if mibBuilder.loadTexts:
    outBr496.setUnits("tenth of Mbps")
_OutStream497_ObjectIdentity = ObjectIdentity
outStream497 = _OutStream497_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 506)
)
_OutBr497_Type = Integer32
_OutBr497_Object = MibScalar
outBr497 = _OutBr497_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 506, 1),
    _OutBr497_Type()
)
outBr497.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr497.setStatus("current")
if mibBuilder.loadTexts:
    outBr497.setUnits("tenth of Mbps")
_OutStream498_ObjectIdentity = ObjectIdentity
outStream498 = _OutStream498_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 507)
)
_OutBr498_Type = Integer32
_OutBr498_Object = MibScalar
outBr498 = _OutBr498_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 507, 1),
    _OutBr498_Type()
)
outBr498.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr498.setStatus("current")
if mibBuilder.loadTexts:
    outBr498.setUnits("tenth of Mbps")
_OutStream499_ObjectIdentity = ObjectIdentity
outStream499 = _OutStream499_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 508)
)
_OutBr499_Type = Integer32
_OutBr499_Object = MibScalar
outBr499 = _OutBr499_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 508, 1),
    _OutBr499_Type()
)
outBr499.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr499.setStatus("current")
if mibBuilder.loadTexts:
    outBr499.setUnits("tenth of Mbps")
_OutStream500_ObjectIdentity = ObjectIdentity
outStream500 = _OutStream500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 509)
)
_OutBr500_Type = Integer32
_OutBr500_Object = MibScalar
outBr500 = _OutBr500_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 509, 1),
    _OutBr500_Type()
)
outBr500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr500.setStatus("current")
if mibBuilder.loadTexts:
    outBr500.setUnits("tenth of Mbps")
_OutStream501_ObjectIdentity = ObjectIdentity
outStream501 = _OutStream501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 510)
)
_OutBr501_Type = Integer32
_OutBr501_Object = MibScalar
outBr501 = _OutBr501_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 510, 1),
    _OutBr501_Type()
)
outBr501.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr501.setStatus("current")
if mibBuilder.loadTexts:
    outBr501.setUnits("tenth of Mbps")
_OutStream502_ObjectIdentity = ObjectIdentity
outStream502 = _OutStream502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 511)
)
_OutBr502_Type = Integer32
_OutBr502_Object = MibScalar
outBr502 = _OutBr502_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 511, 1),
    _OutBr502_Type()
)
outBr502.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr502.setStatus("current")
if mibBuilder.loadTexts:
    outBr502.setUnits("tenth of Mbps")
_OutStream503_ObjectIdentity = ObjectIdentity
outStream503 = _OutStream503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 512)
)
_OutBr503_Type = Integer32
_OutBr503_Object = MibScalar
outBr503 = _OutBr503_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 512, 1),
    _OutBr503_Type()
)
outBr503.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr503.setStatus("current")
if mibBuilder.loadTexts:
    outBr503.setUnits("tenth of Mbps")
_OutStream504_ObjectIdentity = ObjectIdentity
outStream504 = _OutStream504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 513)
)
_OutBr504_Type = Integer32
_OutBr504_Object = MibScalar
outBr504 = _OutBr504_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 513, 1),
    _OutBr504_Type()
)
outBr504.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr504.setStatus("current")
if mibBuilder.loadTexts:
    outBr504.setUnits("tenth of Mbps")
_OutStream505_ObjectIdentity = ObjectIdentity
outStream505 = _OutStream505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 514)
)
_OutBr505_Type = Integer32
_OutBr505_Object = MibScalar
outBr505 = _OutBr505_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 514, 1),
    _OutBr505_Type()
)
outBr505.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr505.setStatus("current")
if mibBuilder.loadTexts:
    outBr505.setUnits("tenth of Mbps")
_OutStream506_ObjectIdentity = ObjectIdentity
outStream506 = _OutStream506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 515)
)
_OutBr506_Type = Integer32
_OutBr506_Object = MibScalar
outBr506 = _OutBr506_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 515, 1),
    _OutBr506_Type()
)
outBr506.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr506.setStatus("current")
if mibBuilder.loadTexts:
    outBr506.setUnits("tenth of Mbps")
_OutStream507_ObjectIdentity = ObjectIdentity
outStream507 = _OutStream507_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 516)
)
_OutBr507_Type = Integer32
_OutBr507_Object = MibScalar
outBr507 = _OutBr507_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 516, 1),
    _OutBr507_Type()
)
outBr507.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr507.setStatus("current")
if mibBuilder.loadTexts:
    outBr507.setUnits("tenth of Mbps")
_OutStream508_ObjectIdentity = ObjectIdentity
outStream508 = _OutStream508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 517)
)
_OutBr508_Type = Integer32
_OutBr508_Object = MibScalar
outBr508 = _OutBr508_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 517, 1),
    _OutBr508_Type()
)
outBr508.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr508.setStatus("current")
if mibBuilder.loadTexts:
    outBr508.setUnits("tenth of Mbps")
_OutStream509_ObjectIdentity = ObjectIdentity
outStream509 = _OutStream509_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 518)
)
_OutBr509_Type = Integer32
_OutBr509_Object = MibScalar
outBr509 = _OutBr509_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 518, 1),
    _OutBr509_Type()
)
outBr509.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr509.setStatus("current")
if mibBuilder.loadTexts:
    outBr509.setUnits("tenth of Mbps")
_OutStream510_ObjectIdentity = ObjectIdentity
outStream510 = _OutStream510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 519)
)
_OutBr510_Type = Integer32
_OutBr510_Object = MibScalar
outBr510 = _OutBr510_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 519, 1),
    _OutBr510_Type()
)
outBr510.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr510.setStatus("current")
if mibBuilder.loadTexts:
    outBr510.setUnits("tenth of Mbps")
_OutStream511_ObjectIdentity = ObjectIdentity
outStream511 = _OutStream511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 520)
)
_OutBr511_Type = Integer32
_OutBr511_Object = MibScalar
outBr511 = _OutBr511_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 520, 1),
    _OutBr511_Type()
)
outBr511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr511.setStatus("current")
if mibBuilder.loadTexts:
    outBr511.setUnits("tenth of Mbps")
_OutStream512_ObjectIdentity = ObjectIdentity
outStream512 = _OutStream512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 521)
)
_OutBr512_Type = Integer32
_OutBr512_Object = MibScalar
outBr512 = _OutBr512_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 521, 1),
    _OutBr512_Type()
)
outBr512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr512.setStatus("current")
if mibBuilder.loadTexts:
    outBr512.setUnits("tenth of Mbps")
_OutStream513_ObjectIdentity = ObjectIdentity
outStream513 = _OutStream513_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 522)
)
_OutBr513_Type = Integer32
_OutBr513_Object = MibScalar
outBr513 = _OutBr513_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 522, 1),
    _OutBr513_Type()
)
outBr513.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr513.setStatus("current")
if mibBuilder.loadTexts:
    outBr513.setUnits("tenth of Mbps")
_OutStream514_ObjectIdentity = ObjectIdentity
outStream514 = _OutStream514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 523)
)
_OutBr514_Type = Integer32
_OutBr514_Object = MibScalar
outBr514 = _OutBr514_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 523, 1),
    _OutBr514_Type()
)
outBr514.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr514.setStatus("current")
if mibBuilder.loadTexts:
    outBr514.setUnits("tenth of Mbps")
_OutStream515_ObjectIdentity = ObjectIdentity
outStream515 = _OutStream515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 524)
)
_OutBr515_Type = Integer32
_OutBr515_Object = MibScalar
outBr515 = _OutBr515_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 524, 1),
    _OutBr515_Type()
)
outBr515.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr515.setStatus("current")
if mibBuilder.loadTexts:
    outBr515.setUnits("tenth of Mbps")
_OutStream516_ObjectIdentity = ObjectIdentity
outStream516 = _OutStream516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 525)
)
_OutBr516_Type = Integer32
_OutBr516_Object = MibScalar
outBr516 = _OutBr516_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 525, 1),
    _OutBr516_Type()
)
outBr516.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr516.setStatus("current")
if mibBuilder.loadTexts:
    outBr516.setUnits("tenth of Mbps")
_OutStream517_ObjectIdentity = ObjectIdentity
outStream517 = _OutStream517_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 526)
)
_OutBr517_Type = Integer32
_OutBr517_Object = MibScalar
outBr517 = _OutBr517_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 526, 1),
    _OutBr517_Type()
)
outBr517.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr517.setStatus("current")
if mibBuilder.loadTexts:
    outBr517.setUnits("tenth of Mbps")
_OutStream518_ObjectIdentity = ObjectIdentity
outStream518 = _OutStream518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 527)
)
_OutBr518_Type = Integer32
_OutBr518_Object = MibScalar
outBr518 = _OutBr518_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 527, 1),
    _OutBr518_Type()
)
outBr518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr518.setStatus("current")
if mibBuilder.loadTexts:
    outBr518.setUnits("tenth of Mbps")
_OutStream519_ObjectIdentity = ObjectIdentity
outStream519 = _OutStream519_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 528)
)
_OutBr519_Type = Integer32
_OutBr519_Object = MibScalar
outBr519 = _OutBr519_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 528, 1),
    _OutBr519_Type()
)
outBr519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr519.setStatus("current")
if mibBuilder.loadTexts:
    outBr519.setUnits("tenth of Mbps")
_OutStream520_ObjectIdentity = ObjectIdentity
outStream520 = _OutStream520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 529)
)
_OutBr520_Type = Integer32
_OutBr520_Object = MibScalar
outBr520 = _OutBr520_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 529, 1),
    _OutBr520_Type()
)
outBr520.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr520.setStatus("current")
if mibBuilder.loadTexts:
    outBr520.setUnits("tenth of Mbps")
_OutStream521_ObjectIdentity = ObjectIdentity
outStream521 = _OutStream521_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 530)
)
_OutBr521_Type = Integer32
_OutBr521_Object = MibScalar
outBr521 = _OutBr521_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 530, 1),
    _OutBr521_Type()
)
outBr521.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr521.setStatus("current")
if mibBuilder.loadTexts:
    outBr521.setUnits("tenth of Mbps")
_OutStream522_ObjectIdentity = ObjectIdentity
outStream522 = _OutStream522_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 531)
)
_OutBr522_Type = Integer32
_OutBr522_Object = MibScalar
outBr522 = _OutBr522_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 531, 1),
    _OutBr522_Type()
)
outBr522.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr522.setStatus("current")
if mibBuilder.loadTexts:
    outBr522.setUnits("tenth of Mbps")
_OutStream523_ObjectIdentity = ObjectIdentity
outStream523 = _OutStream523_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 532)
)
_OutBr523_Type = Integer32
_OutBr523_Object = MibScalar
outBr523 = _OutBr523_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 532, 1),
    _OutBr523_Type()
)
outBr523.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr523.setStatus("current")
if mibBuilder.loadTexts:
    outBr523.setUnits("tenth of Mbps")
_OutStream524_ObjectIdentity = ObjectIdentity
outStream524 = _OutStream524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 533)
)
_OutBr524_Type = Integer32
_OutBr524_Object = MibScalar
outBr524 = _OutBr524_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 533, 1),
    _OutBr524_Type()
)
outBr524.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr524.setStatus("current")
if mibBuilder.loadTexts:
    outBr524.setUnits("tenth of Mbps")
_OutStream525_ObjectIdentity = ObjectIdentity
outStream525 = _OutStream525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 534)
)
_OutBr525_Type = Integer32
_OutBr525_Object = MibScalar
outBr525 = _OutBr525_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 534, 1),
    _OutBr525_Type()
)
outBr525.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr525.setStatus("current")
if mibBuilder.loadTexts:
    outBr525.setUnits("tenth of Mbps")
_OutStream526_ObjectIdentity = ObjectIdentity
outStream526 = _OutStream526_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 535)
)
_OutBr526_Type = Integer32
_OutBr526_Object = MibScalar
outBr526 = _OutBr526_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 535, 1),
    _OutBr526_Type()
)
outBr526.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr526.setStatus("current")
if mibBuilder.loadTexts:
    outBr526.setUnits("tenth of Mbps")
_OutStream527_ObjectIdentity = ObjectIdentity
outStream527 = _OutStream527_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 536)
)
_OutBr527_Type = Integer32
_OutBr527_Object = MibScalar
outBr527 = _OutBr527_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 536, 1),
    _OutBr527_Type()
)
outBr527.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr527.setStatus("current")
if mibBuilder.loadTexts:
    outBr527.setUnits("tenth of Mbps")
_OutStream528_ObjectIdentity = ObjectIdentity
outStream528 = _OutStream528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 537)
)
_OutBr528_Type = Integer32
_OutBr528_Object = MibScalar
outBr528 = _OutBr528_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 537, 1),
    _OutBr528_Type()
)
outBr528.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr528.setStatus("current")
if mibBuilder.loadTexts:
    outBr528.setUnits("tenth of Mbps")
_OutStream529_ObjectIdentity = ObjectIdentity
outStream529 = _OutStream529_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 538)
)
_OutBr529_Type = Integer32
_OutBr529_Object = MibScalar
outBr529 = _OutBr529_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 538, 1),
    _OutBr529_Type()
)
outBr529.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr529.setStatus("current")
if mibBuilder.loadTexts:
    outBr529.setUnits("tenth of Mbps")
_OutStream530_ObjectIdentity = ObjectIdentity
outStream530 = _OutStream530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 539)
)
_OutBr530_Type = Integer32
_OutBr530_Object = MibScalar
outBr530 = _OutBr530_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 539, 1),
    _OutBr530_Type()
)
outBr530.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr530.setStatus("current")
if mibBuilder.loadTexts:
    outBr530.setUnits("tenth of Mbps")
_OutStream531_ObjectIdentity = ObjectIdentity
outStream531 = _OutStream531_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 540)
)
_OutBr531_Type = Integer32
_OutBr531_Object = MibScalar
outBr531 = _OutBr531_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 540, 1),
    _OutBr531_Type()
)
outBr531.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr531.setStatus("current")
if mibBuilder.loadTexts:
    outBr531.setUnits("tenth of Mbps")
_OutStream532_ObjectIdentity = ObjectIdentity
outStream532 = _OutStream532_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 541)
)
_OutBr532_Type = Integer32
_OutBr532_Object = MibScalar
outBr532 = _OutBr532_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 541, 1),
    _OutBr532_Type()
)
outBr532.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr532.setStatus("current")
if mibBuilder.loadTexts:
    outBr532.setUnits("tenth of Mbps")
_OutStream533_ObjectIdentity = ObjectIdentity
outStream533 = _OutStream533_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 542)
)
_OutBr533_Type = Integer32
_OutBr533_Object = MibScalar
outBr533 = _OutBr533_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 542, 1),
    _OutBr533_Type()
)
outBr533.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr533.setStatus("current")
if mibBuilder.loadTexts:
    outBr533.setUnits("tenth of Mbps")
_OutStream534_ObjectIdentity = ObjectIdentity
outStream534 = _OutStream534_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 543)
)
_OutBr534_Type = Integer32
_OutBr534_Object = MibScalar
outBr534 = _OutBr534_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 543, 1),
    _OutBr534_Type()
)
outBr534.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr534.setStatus("current")
if mibBuilder.loadTexts:
    outBr534.setUnits("tenth of Mbps")
_OutStream535_ObjectIdentity = ObjectIdentity
outStream535 = _OutStream535_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 544)
)
_OutBr535_Type = Integer32
_OutBr535_Object = MibScalar
outBr535 = _OutBr535_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 544, 1),
    _OutBr535_Type()
)
outBr535.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr535.setStatus("current")
if mibBuilder.loadTexts:
    outBr535.setUnits("tenth of Mbps")
_OutStream536_ObjectIdentity = ObjectIdentity
outStream536 = _OutStream536_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 545)
)
_OutBr536_Type = Integer32
_OutBr536_Object = MibScalar
outBr536 = _OutBr536_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 545, 1),
    _OutBr536_Type()
)
outBr536.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr536.setStatus("current")
if mibBuilder.loadTexts:
    outBr536.setUnits("tenth of Mbps")
_OutStream537_ObjectIdentity = ObjectIdentity
outStream537 = _OutStream537_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 546)
)
_OutBr537_Type = Integer32
_OutBr537_Object = MibScalar
outBr537 = _OutBr537_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 546, 1),
    _OutBr537_Type()
)
outBr537.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr537.setStatus("current")
if mibBuilder.loadTexts:
    outBr537.setUnits("tenth of Mbps")
_OutStream538_ObjectIdentity = ObjectIdentity
outStream538 = _OutStream538_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 547)
)
_OutBr538_Type = Integer32
_OutBr538_Object = MibScalar
outBr538 = _OutBr538_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 547, 1),
    _OutBr538_Type()
)
outBr538.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr538.setStatus("current")
if mibBuilder.loadTexts:
    outBr538.setUnits("tenth of Mbps")
_OutStream539_ObjectIdentity = ObjectIdentity
outStream539 = _OutStream539_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 548)
)
_OutBr539_Type = Integer32
_OutBr539_Object = MibScalar
outBr539 = _OutBr539_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 548, 1),
    _OutBr539_Type()
)
outBr539.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr539.setStatus("current")
if mibBuilder.loadTexts:
    outBr539.setUnits("tenth of Mbps")
_OutStream540_ObjectIdentity = ObjectIdentity
outStream540 = _OutStream540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 549)
)
_OutBr540_Type = Integer32
_OutBr540_Object = MibScalar
outBr540 = _OutBr540_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 549, 1),
    _OutBr540_Type()
)
outBr540.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr540.setStatus("current")
if mibBuilder.loadTexts:
    outBr540.setUnits("tenth of Mbps")
_OutStream541_ObjectIdentity = ObjectIdentity
outStream541 = _OutStream541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 550)
)
_OutBr541_Type = Integer32
_OutBr541_Object = MibScalar
outBr541 = _OutBr541_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 550, 1),
    _OutBr541_Type()
)
outBr541.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr541.setStatus("current")
if mibBuilder.loadTexts:
    outBr541.setUnits("tenth of Mbps")
_OutStream542_ObjectIdentity = ObjectIdentity
outStream542 = _OutStream542_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 551)
)
_OutBr542_Type = Integer32
_OutBr542_Object = MibScalar
outBr542 = _OutBr542_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 551, 1),
    _OutBr542_Type()
)
outBr542.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr542.setStatus("current")
if mibBuilder.loadTexts:
    outBr542.setUnits("tenth of Mbps")
_OutStream543_ObjectIdentity = ObjectIdentity
outStream543 = _OutStream543_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 552)
)
_OutBr543_Type = Integer32
_OutBr543_Object = MibScalar
outBr543 = _OutBr543_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 552, 1),
    _OutBr543_Type()
)
outBr543.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr543.setStatus("current")
if mibBuilder.loadTexts:
    outBr543.setUnits("tenth of Mbps")
_OutStream544_ObjectIdentity = ObjectIdentity
outStream544 = _OutStream544_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 553)
)
_OutBr544_Type = Integer32
_OutBr544_Object = MibScalar
outBr544 = _OutBr544_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 553, 1),
    _OutBr544_Type()
)
outBr544.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr544.setStatus("current")
if mibBuilder.loadTexts:
    outBr544.setUnits("tenth of Mbps")
_OutStream545_ObjectIdentity = ObjectIdentity
outStream545 = _OutStream545_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 554)
)
_OutBr545_Type = Integer32
_OutBr545_Object = MibScalar
outBr545 = _OutBr545_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 554, 1),
    _OutBr545_Type()
)
outBr545.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr545.setStatus("current")
if mibBuilder.loadTexts:
    outBr545.setUnits("tenth of Mbps")
_OutStream546_ObjectIdentity = ObjectIdentity
outStream546 = _OutStream546_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 555)
)
_OutBr546_Type = Integer32
_OutBr546_Object = MibScalar
outBr546 = _OutBr546_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 555, 1),
    _OutBr546_Type()
)
outBr546.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr546.setStatus("current")
if mibBuilder.loadTexts:
    outBr546.setUnits("tenth of Mbps")
_OutStream547_ObjectIdentity = ObjectIdentity
outStream547 = _OutStream547_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 556)
)
_OutBr547_Type = Integer32
_OutBr547_Object = MibScalar
outBr547 = _OutBr547_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 556, 1),
    _OutBr547_Type()
)
outBr547.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr547.setStatus("current")
if mibBuilder.loadTexts:
    outBr547.setUnits("tenth of Mbps")
_OutStream548_ObjectIdentity = ObjectIdentity
outStream548 = _OutStream548_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 557)
)
_OutBr548_Type = Integer32
_OutBr548_Object = MibScalar
outBr548 = _OutBr548_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 557, 1),
    _OutBr548_Type()
)
outBr548.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr548.setStatus("current")
if mibBuilder.loadTexts:
    outBr548.setUnits("tenth of Mbps")
_OutStream549_ObjectIdentity = ObjectIdentity
outStream549 = _OutStream549_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 558)
)
_OutBr549_Type = Integer32
_OutBr549_Object = MibScalar
outBr549 = _OutBr549_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 558, 1),
    _OutBr549_Type()
)
outBr549.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr549.setStatus("current")
if mibBuilder.loadTexts:
    outBr549.setUnits("tenth of Mbps")
_OutStream550_ObjectIdentity = ObjectIdentity
outStream550 = _OutStream550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 559)
)
_OutBr550_Type = Integer32
_OutBr550_Object = MibScalar
outBr550 = _OutBr550_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 559, 1),
    _OutBr550_Type()
)
outBr550.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr550.setStatus("current")
if mibBuilder.loadTexts:
    outBr550.setUnits("tenth of Mbps")
_OutStream551_ObjectIdentity = ObjectIdentity
outStream551 = _OutStream551_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 560)
)
_OutBr551_Type = Integer32
_OutBr551_Object = MibScalar
outBr551 = _OutBr551_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 560, 1),
    _OutBr551_Type()
)
outBr551.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr551.setStatus("current")
if mibBuilder.loadTexts:
    outBr551.setUnits("tenth of Mbps")
_OutStream552_ObjectIdentity = ObjectIdentity
outStream552 = _OutStream552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 561)
)
_OutBr552_Type = Integer32
_OutBr552_Object = MibScalar
outBr552 = _OutBr552_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 561, 1),
    _OutBr552_Type()
)
outBr552.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr552.setStatus("current")
if mibBuilder.loadTexts:
    outBr552.setUnits("tenth of Mbps")
_OutStream553_ObjectIdentity = ObjectIdentity
outStream553 = _OutStream553_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 562)
)
_OutBr553_Type = Integer32
_OutBr553_Object = MibScalar
outBr553 = _OutBr553_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 562, 1),
    _OutBr553_Type()
)
outBr553.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr553.setStatus("current")
if mibBuilder.loadTexts:
    outBr553.setUnits("tenth of Mbps")
_OutStream554_ObjectIdentity = ObjectIdentity
outStream554 = _OutStream554_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 563)
)
_OutBr554_Type = Integer32
_OutBr554_Object = MibScalar
outBr554 = _OutBr554_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 563, 1),
    _OutBr554_Type()
)
outBr554.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr554.setStatus("current")
if mibBuilder.loadTexts:
    outBr554.setUnits("tenth of Mbps")
_OutStream555_ObjectIdentity = ObjectIdentity
outStream555 = _OutStream555_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 564)
)
_OutBr555_Type = Integer32
_OutBr555_Object = MibScalar
outBr555 = _OutBr555_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 564, 1),
    _OutBr555_Type()
)
outBr555.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr555.setStatus("current")
if mibBuilder.loadTexts:
    outBr555.setUnits("tenth of Mbps")
_OutStream556_ObjectIdentity = ObjectIdentity
outStream556 = _OutStream556_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 565)
)
_OutBr556_Type = Integer32
_OutBr556_Object = MibScalar
outBr556 = _OutBr556_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 565, 1),
    _OutBr556_Type()
)
outBr556.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr556.setStatus("current")
if mibBuilder.loadTexts:
    outBr556.setUnits("tenth of Mbps")
_OutStream557_ObjectIdentity = ObjectIdentity
outStream557 = _OutStream557_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 566)
)
_OutBr557_Type = Integer32
_OutBr557_Object = MibScalar
outBr557 = _OutBr557_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 566, 1),
    _OutBr557_Type()
)
outBr557.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr557.setStatus("current")
if mibBuilder.loadTexts:
    outBr557.setUnits("tenth of Mbps")
_OutStream558_ObjectIdentity = ObjectIdentity
outStream558 = _OutStream558_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 567)
)
_OutBr558_Type = Integer32
_OutBr558_Object = MibScalar
outBr558 = _OutBr558_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 567, 1),
    _OutBr558_Type()
)
outBr558.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr558.setStatus("current")
if mibBuilder.loadTexts:
    outBr558.setUnits("tenth of Mbps")
_OutStream559_ObjectIdentity = ObjectIdentity
outStream559 = _OutStream559_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 568)
)
_OutBr559_Type = Integer32
_OutBr559_Object = MibScalar
outBr559 = _OutBr559_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 568, 1),
    _OutBr559_Type()
)
outBr559.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr559.setStatus("current")
if mibBuilder.loadTexts:
    outBr559.setUnits("tenth of Mbps")
_OutStream560_ObjectIdentity = ObjectIdentity
outStream560 = _OutStream560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 569)
)
_OutBr560_Type = Integer32
_OutBr560_Object = MibScalar
outBr560 = _OutBr560_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 569, 1),
    _OutBr560_Type()
)
outBr560.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr560.setStatus("current")
if mibBuilder.loadTexts:
    outBr560.setUnits("tenth of Mbps")
_OutStream561_ObjectIdentity = ObjectIdentity
outStream561 = _OutStream561_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 570)
)
_OutBr561_Type = Integer32
_OutBr561_Object = MibScalar
outBr561 = _OutBr561_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 570, 1),
    _OutBr561_Type()
)
outBr561.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr561.setStatus("current")
if mibBuilder.loadTexts:
    outBr561.setUnits("tenth of Mbps")
_OutStream562_ObjectIdentity = ObjectIdentity
outStream562 = _OutStream562_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 571)
)
_OutBr562_Type = Integer32
_OutBr562_Object = MibScalar
outBr562 = _OutBr562_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 571, 1),
    _OutBr562_Type()
)
outBr562.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr562.setStatus("current")
if mibBuilder.loadTexts:
    outBr562.setUnits("tenth of Mbps")
_OutStream563_ObjectIdentity = ObjectIdentity
outStream563 = _OutStream563_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 572)
)
_OutBr563_Type = Integer32
_OutBr563_Object = MibScalar
outBr563 = _OutBr563_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 572, 1),
    _OutBr563_Type()
)
outBr563.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr563.setStatus("current")
if mibBuilder.loadTexts:
    outBr563.setUnits("tenth of Mbps")
_OutStream564_ObjectIdentity = ObjectIdentity
outStream564 = _OutStream564_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 573)
)
_OutBr564_Type = Integer32
_OutBr564_Object = MibScalar
outBr564 = _OutBr564_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 573, 1),
    _OutBr564_Type()
)
outBr564.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr564.setStatus("current")
if mibBuilder.loadTexts:
    outBr564.setUnits("tenth of Mbps")
_OutStream565_ObjectIdentity = ObjectIdentity
outStream565 = _OutStream565_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 574)
)
_OutBr565_Type = Integer32
_OutBr565_Object = MibScalar
outBr565 = _OutBr565_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 574, 1),
    _OutBr565_Type()
)
outBr565.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr565.setStatus("current")
if mibBuilder.loadTexts:
    outBr565.setUnits("tenth of Mbps")
_OutStream566_ObjectIdentity = ObjectIdentity
outStream566 = _OutStream566_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 575)
)
_OutBr566_Type = Integer32
_OutBr566_Object = MibScalar
outBr566 = _OutBr566_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 575, 1),
    _OutBr566_Type()
)
outBr566.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr566.setStatus("current")
if mibBuilder.loadTexts:
    outBr566.setUnits("tenth of Mbps")
_OutStream567_ObjectIdentity = ObjectIdentity
outStream567 = _OutStream567_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 576)
)
_OutBr567_Type = Integer32
_OutBr567_Object = MibScalar
outBr567 = _OutBr567_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 576, 1),
    _OutBr567_Type()
)
outBr567.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr567.setStatus("current")
if mibBuilder.loadTexts:
    outBr567.setUnits("tenth of Mbps")
_OutStream568_ObjectIdentity = ObjectIdentity
outStream568 = _OutStream568_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 577)
)
_OutBr568_Type = Integer32
_OutBr568_Object = MibScalar
outBr568 = _OutBr568_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 577, 1),
    _OutBr568_Type()
)
outBr568.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr568.setStatus("current")
if mibBuilder.loadTexts:
    outBr568.setUnits("tenth of Mbps")
_OutStream569_ObjectIdentity = ObjectIdentity
outStream569 = _OutStream569_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 578)
)
_OutBr569_Type = Integer32
_OutBr569_Object = MibScalar
outBr569 = _OutBr569_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 578, 1),
    _OutBr569_Type()
)
outBr569.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr569.setStatus("current")
if mibBuilder.loadTexts:
    outBr569.setUnits("tenth of Mbps")
_OutStream570_ObjectIdentity = ObjectIdentity
outStream570 = _OutStream570_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 579)
)
_OutBr570_Type = Integer32
_OutBr570_Object = MibScalar
outBr570 = _OutBr570_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 579, 1),
    _OutBr570_Type()
)
outBr570.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr570.setStatus("current")
if mibBuilder.loadTexts:
    outBr570.setUnits("tenth of Mbps")
_OutStream571_ObjectIdentity = ObjectIdentity
outStream571 = _OutStream571_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 580)
)
_OutBr571_Type = Integer32
_OutBr571_Object = MibScalar
outBr571 = _OutBr571_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 580, 1),
    _OutBr571_Type()
)
outBr571.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr571.setStatus("current")
if mibBuilder.loadTexts:
    outBr571.setUnits("tenth of Mbps")
_OutStream572_ObjectIdentity = ObjectIdentity
outStream572 = _OutStream572_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 581)
)
_OutBr572_Type = Integer32
_OutBr572_Object = MibScalar
outBr572 = _OutBr572_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 581, 1),
    _OutBr572_Type()
)
outBr572.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr572.setStatus("current")
if mibBuilder.loadTexts:
    outBr572.setUnits("tenth of Mbps")
_OutStream573_ObjectIdentity = ObjectIdentity
outStream573 = _OutStream573_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 582)
)
_OutBr573_Type = Integer32
_OutBr573_Object = MibScalar
outBr573 = _OutBr573_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 582, 1),
    _OutBr573_Type()
)
outBr573.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr573.setStatus("current")
if mibBuilder.loadTexts:
    outBr573.setUnits("tenth of Mbps")
_OutStream574_ObjectIdentity = ObjectIdentity
outStream574 = _OutStream574_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 583)
)
_OutBr574_Type = Integer32
_OutBr574_Object = MibScalar
outBr574 = _OutBr574_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 583, 1),
    _OutBr574_Type()
)
outBr574.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr574.setStatus("current")
if mibBuilder.loadTexts:
    outBr574.setUnits("tenth of Mbps")
_OutStream575_ObjectIdentity = ObjectIdentity
outStream575 = _OutStream575_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 584)
)
_OutBr575_Type = Integer32
_OutBr575_Object = MibScalar
outBr575 = _OutBr575_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 584, 1),
    _OutBr575_Type()
)
outBr575.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr575.setStatus("current")
if mibBuilder.loadTexts:
    outBr575.setUnits("tenth of Mbps")
_OutStream576_ObjectIdentity = ObjectIdentity
outStream576 = _OutStream576_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 585)
)
_OutBr576_Type = Integer32
_OutBr576_Object = MibScalar
outBr576 = _OutBr576_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 585, 1),
    _OutBr576_Type()
)
outBr576.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr576.setStatus("current")
if mibBuilder.loadTexts:
    outBr576.setUnits("tenth of Mbps")
_CommStatus_ObjectIdentity = ObjectIdentity
commStatus = _CommStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 586)
)
_InTotbr_Type = Integer32
_InTotbr_Object = MibScalar
inTotbr = _InTotbr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 586, 1),
    _InTotbr_Type()
)
inTotbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inTotbr.setStatus("current")
if mibBuilder.loadTexts:
    inTotbr.setUnits("tenth of Mbps")
_OutTotbr_Type = Integer32
_OutTotbr_Object = MibScalar
outTotbr = _OutTotbr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 586, 2),
    _OutTotbr_Type()
)
outTotbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outTotbr.setStatus("current")
if mibBuilder.loadTexts:
    outTotbr.setUnits("tenth of Mbps")
_CpuLoad_Type = Integer32
_CpuLoad_Object = MibScalar
cpuLoad = _CpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 586, 3),
    _CpuLoad_Type()
)
cpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoad.setUnits("%")
_IntTemp_Type = Integer32
_IntTemp_Object = MibScalar
intTemp = _IntTemp_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 586, 4),
    _IntTemp_Type()
)
intTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intTemp.setStatus("current")
if mibBuilder.loadTexts:
    intTemp.setUnits("deg C")
_DemodTemp_Type = Integer32
_DemodTemp_Object = MibScalar
demodTemp = _DemodTemp_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 586, 5),
    _DemodTemp_Type()
)
demodTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demodTemp.setStatus("current")
if mibBuilder.loadTexts:
    demodTemp.setUnits("deg C")
_Volt_Type = Integer32
_Volt_Object = MibScalar
volt = _Volt_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 1, 586, 6),
    _Volt_Type()
)
volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt.setStatus("current")
if mibBuilder.loadTexts:
    volt.setUnits("tenth of volt")
_Sdi480alarms_ObjectIdentity = ObjectIdentity
sdi480alarms = _Sdi480alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2)
)
_AlarmLnb1_Type = DefStatus
_AlarmLnb1_Object = MibScalar
alarmLnb1 = _AlarmLnb1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 1),
    _AlarmLnb1_Type()
)
alarmLnb1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLnb1.setStatus("current")
_AlarmLnb2_Type = DefStatus
_AlarmLnb2_Object = MibScalar
alarmLnb2 = _AlarmLnb2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 2),
    _AlarmLnb2_Type()
)
alarmLnb2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLnb2.setStatus("current")
_AlarmLnb3_Type = DefStatus
_AlarmLnb3_Object = MibScalar
alarmLnb3 = _AlarmLnb3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 3),
    _AlarmLnb3_Type()
)
alarmLnb3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLnb3.setStatus("current")
_AlarmLnb4_Type = DefStatus
_AlarmLnb4_Object = MibScalar
alarmLnb4 = _AlarmLnb4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 4),
    _AlarmLnb4_Type()
)
alarmLnb4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLnb4.setStatus("current")
_AlarmStlink_Type = DefStatus
_AlarmStlink_Object = MibScalar
alarmStlink = _AlarmStlink_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 5),
    _AlarmStlink_Type()
)
alarmStlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStlink.setStatus("current")
_AlarmCtrlink_Type = DefStatus
_AlarmCtrlink_Object = MibScalar
alarmCtrlink = _AlarmCtrlink_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 6),
    _AlarmCtrlink_Type()
)
alarmCtrlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCtrlink.setStatus("current")
_AlarmBrovf_Type = DefStatus
_AlarmBrovf_Object = MibScalar
alarmBrovf = _AlarmBrovf_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 7),
    _AlarmBrovf_Type()
)
alarmBrovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBrovf.setStatus("current")
_AlarmUnlock1_Type = DefStatus
_AlarmUnlock1_Object = MibScalar
alarmUnlock1 = _AlarmUnlock1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 8),
    _AlarmUnlock1_Type()
)
alarmUnlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock1.setStatus("current")
_AlarmUnlock2_Type = DefStatus
_AlarmUnlock2_Object = MibScalar
alarmUnlock2 = _AlarmUnlock2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 9),
    _AlarmUnlock2_Type()
)
alarmUnlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock2.setStatus("current")
_AlarmUnlock3_Type = DefStatus
_AlarmUnlock3_Object = MibScalar
alarmUnlock3 = _AlarmUnlock3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 10),
    _AlarmUnlock3_Type()
)
alarmUnlock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock3.setStatus("current")
_AlarmUnlock4_Type = DefStatus
_AlarmUnlock4_Object = MibScalar
alarmUnlock4 = _AlarmUnlock4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 11),
    _AlarmUnlock4_Type()
)
alarmUnlock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock4.setStatus("current")
_AlarmUnlock5_Type = DefStatus
_AlarmUnlock5_Object = MibScalar
alarmUnlock5 = _AlarmUnlock5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 12),
    _AlarmUnlock5_Type()
)
alarmUnlock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock5.setStatus("current")
_AlarmUnlock6_Type = DefStatus
_AlarmUnlock6_Object = MibScalar
alarmUnlock6 = _AlarmUnlock6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 13),
    _AlarmUnlock6_Type()
)
alarmUnlock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock6.setStatus("current")
_AlarmUnlock7_Type = DefStatus
_AlarmUnlock7_Object = MibScalar
alarmUnlock7 = _AlarmUnlock7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 14),
    _AlarmUnlock7_Type()
)
alarmUnlock7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock7.setStatus("current")
_AlarmUnlock8_Type = DefStatus
_AlarmUnlock8_Object = MibScalar
alarmUnlock8 = _AlarmUnlock8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 15),
    _AlarmUnlock8_Type()
)
alarmUnlock8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock8.setStatus("current")
_AlarmUnlock9_Type = DefStatus
_AlarmUnlock9_Object = MibScalar
alarmUnlock9 = _AlarmUnlock9_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 16),
    _AlarmUnlock9_Type()
)
alarmUnlock9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock9.setStatus("current")
_AlarmPowerr_Type = DefStatus
_AlarmPowerr_Object = MibScalar
alarmPowerr = _AlarmPowerr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 17),
    _AlarmPowerr_Type()
)
alarmPowerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPowerr.setStatus("current")
_AlarmTemperr_Type = DefStatus
_AlarmTemperr_Object = MibScalar
alarmTemperr = _AlarmTemperr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 18),
    _AlarmTemperr_Type()
)
alarmTemperr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTemperr.setStatus("current")
_AlarmIbrer_Type = DefStatus
_AlarmIbrer_Object = MibScalar
alarmIbrer = _AlarmIbrer_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 2, 19),
    _AlarmIbrer_Type()
)
alarmIbrer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIbrer.setStatus("current")
_Sdi480notifications_ObjectIdentity = ObjectIdentity
sdi480notifications = _Sdi480notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3)
)
_Sdi480Info_ObjectIdentity = ObjectIdentity
sdi480Info = _Sdi480Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 4)
)
_InfVersion_Type = DisplayString
_InfVersion_Object = MibScalar
infVersion = _InfVersion_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 4, 1),
    _InfVersion_Type()
)
infVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infVersion.setStatus("current")
_InfSerNum_Type = DisplayString
_InfSerNum_Object = MibScalar
infSerNum = _InfSerNum_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 4, 2),
    _InfSerNum_Type()
)
infSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infSerNum.setStatus("current")
_Terrasdi480MIBConformance_ObjectIdentity = ObjectIdentity
terrasdi480MIBConformance = _Terrasdi480MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 5)
)
_Terrasdi480MIBGroups_ObjectIdentity = ObjectIdentity
terrasdi480MIBGroups = _Terrasdi480MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 5, 1)
)

# Managed Objects groups

sdi480TerraMibAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 5, 1, 1)
)
sdi480TerraMibAllObjects.setObjects(
      *(("TERRA-sdi480-MIB", "inLock1"),
        ("TERRA-sdi480-MIB", "inlevel1"),
        ("TERRA-sdi480-MIB", "insnr1"),
        ("TERRA-sdi480-MIB", "inbr1"),
        ("TERRA-sdi480-MIB", "inper1"),
        ("TERRA-sdi480-MIB", "inLock2"),
        ("TERRA-sdi480-MIB", "inlevel2"),
        ("TERRA-sdi480-MIB", "insnr2"),
        ("TERRA-sdi480-MIB", "inbr2"),
        ("TERRA-sdi480-MIB", "inper2"),
        ("TERRA-sdi480-MIB", "inLock3"),
        ("TERRA-sdi480-MIB", "inlevel3"),
        ("TERRA-sdi480-MIB", "insnr3"),
        ("TERRA-sdi480-MIB", "inbr3"),
        ("TERRA-sdi480-MIB", "inper3"),
        ("TERRA-sdi480-MIB", "inLock4"),
        ("TERRA-sdi480-MIB", "inlevel4"),
        ("TERRA-sdi480-MIB", "insnr4"),
        ("TERRA-sdi480-MIB", "inbr4"),
        ("TERRA-sdi480-MIB", "inper4"),
        ("TERRA-sdi480-MIB", "inLock5"),
        ("TERRA-sdi480-MIB", "inlevel5"),
        ("TERRA-sdi480-MIB", "insnr5"),
        ("TERRA-sdi480-MIB", "inbr5"),
        ("TERRA-sdi480-MIB", "inper5"),
        ("TERRA-sdi480-MIB", "inLock6"),
        ("TERRA-sdi480-MIB", "inlevel6"),
        ("TERRA-sdi480-MIB", "insnr6"),
        ("TERRA-sdi480-MIB", "inbr6"),
        ("TERRA-sdi480-MIB", "inper6"),
        ("TERRA-sdi480-MIB", "inLock7"),
        ("TERRA-sdi480-MIB", "inlevel7"),
        ("TERRA-sdi480-MIB", "insnr7"),
        ("TERRA-sdi480-MIB", "inbr7"),
        ("TERRA-sdi480-MIB", "inper7"),
        ("TERRA-sdi480-MIB", "inLock8"),
        ("TERRA-sdi480-MIB", "inlevel8"),
        ("TERRA-sdi480-MIB", "insnr8"),
        ("TERRA-sdi480-MIB", "inbr8"),
        ("TERRA-sdi480-MIB", "inper8"),
        ("TERRA-sdi480-MIB", "usbinBR"),
        ("TERRA-sdi480-MIB", "outBr1"),
        ("TERRA-sdi480-MIB", "outBr2"),
        ("TERRA-sdi480-MIB", "outBr3"),
        ("TERRA-sdi480-MIB", "outBr4"),
        ("TERRA-sdi480-MIB", "outBr5"),
        ("TERRA-sdi480-MIB", "outBr6"),
        ("TERRA-sdi480-MIB", "outBr7"),
        ("TERRA-sdi480-MIB", "outBr8"),
        ("TERRA-sdi480-MIB", "outBr9"),
        ("TERRA-sdi480-MIB", "outBr10"),
        ("TERRA-sdi480-MIB", "outBr11"),
        ("TERRA-sdi480-MIB", "outBr12"),
        ("TERRA-sdi480-MIB", "outBr13"),
        ("TERRA-sdi480-MIB", "outBr14"),
        ("TERRA-sdi480-MIB", "outBr15"),
        ("TERRA-sdi480-MIB", "outBr16"),
        ("TERRA-sdi480-MIB", "outBr17"),
        ("TERRA-sdi480-MIB", "outBr18"),
        ("TERRA-sdi480-MIB", "outBr19"),
        ("TERRA-sdi480-MIB", "outBr20"),
        ("TERRA-sdi480-MIB", "outBr21"),
        ("TERRA-sdi480-MIB", "outBr22"),
        ("TERRA-sdi480-MIB", "outBr23"),
        ("TERRA-sdi480-MIB", "outBr24"),
        ("TERRA-sdi480-MIB", "outBr25"),
        ("TERRA-sdi480-MIB", "outBr26"),
        ("TERRA-sdi480-MIB", "outBr27"),
        ("TERRA-sdi480-MIB", "outBr28"),
        ("TERRA-sdi480-MIB", "outBr29"),
        ("TERRA-sdi480-MIB", "outBr30"),
        ("TERRA-sdi480-MIB", "outBr31"),
        ("TERRA-sdi480-MIB", "outBr32"),
        ("TERRA-sdi480-MIB", "outBr33"),
        ("TERRA-sdi480-MIB", "outBr34"),
        ("TERRA-sdi480-MIB", "outBr35"),
        ("TERRA-sdi480-MIB", "outBr36"),
        ("TERRA-sdi480-MIB", "outBr37"),
        ("TERRA-sdi480-MIB", "outBr38"),
        ("TERRA-sdi480-MIB", "outBr39"),
        ("TERRA-sdi480-MIB", "outBr40"),
        ("TERRA-sdi480-MIB", "outBr41"),
        ("TERRA-sdi480-MIB", "outBr42"),
        ("TERRA-sdi480-MIB", "outBr43"),
        ("TERRA-sdi480-MIB", "outBr44"),
        ("TERRA-sdi480-MIB", "outBr45"),
        ("TERRA-sdi480-MIB", "outBr46"),
        ("TERRA-sdi480-MIB", "outBr47"),
        ("TERRA-sdi480-MIB", "outBr48"),
        ("TERRA-sdi480-MIB", "outBr49"),
        ("TERRA-sdi480-MIB", "outBr50"),
        ("TERRA-sdi480-MIB", "outBr51"),
        ("TERRA-sdi480-MIB", "outBr52"),
        ("TERRA-sdi480-MIB", "outBr53"),
        ("TERRA-sdi480-MIB", "outBr54"),
        ("TERRA-sdi480-MIB", "outBr55"),
        ("TERRA-sdi480-MIB", "outBr56"),
        ("TERRA-sdi480-MIB", "outBr57"),
        ("TERRA-sdi480-MIB", "outBr58"),
        ("TERRA-sdi480-MIB", "outBr59"),
        ("TERRA-sdi480-MIB", "outBr60"),
        ("TERRA-sdi480-MIB", "outBr61"),
        ("TERRA-sdi480-MIB", "outBr62"),
        ("TERRA-sdi480-MIB", "outBr63"),
        ("TERRA-sdi480-MIB", "outBr64"),
        ("TERRA-sdi480-MIB", "outBr65"),
        ("TERRA-sdi480-MIB", "outBr66"),
        ("TERRA-sdi480-MIB", "outBr67"),
        ("TERRA-sdi480-MIB", "outBr68"),
        ("TERRA-sdi480-MIB", "outBr69"),
        ("TERRA-sdi480-MIB", "outBr70"),
        ("TERRA-sdi480-MIB", "outBr71"),
        ("TERRA-sdi480-MIB", "outBr72"),
        ("TERRA-sdi480-MIB", "outBr73"),
        ("TERRA-sdi480-MIB", "outBr74"),
        ("TERRA-sdi480-MIB", "outBr75"),
        ("TERRA-sdi480-MIB", "outBr76"),
        ("TERRA-sdi480-MIB", "outBr77"),
        ("TERRA-sdi480-MIB", "outBr78"),
        ("TERRA-sdi480-MIB", "outBr79"),
        ("TERRA-sdi480-MIB", "outBr80"),
        ("TERRA-sdi480-MIB", "outBr81"),
        ("TERRA-sdi480-MIB", "outBr82"),
        ("TERRA-sdi480-MIB", "outBr83"),
        ("TERRA-sdi480-MIB", "outBr84"),
        ("TERRA-sdi480-MIB", "outBr85"),
        ("TERRA-sdi480-MIB", "outBr86"),
        ("TERRA-sdi480-MIB", "outBr87"),
        ("TERRA-sdi480-MIB", "outBr88"),
        ("TERRA-sdi480-MIB", "outBr89"),
        ("TERRA-sdi480-MIB", "outBr90"),
        ("TERRA-sdi480-MIB", "outBr91"),
        ("TERRA-sdi480-MIB", "outBr92"),
        ("TERRA-sdi480-MIB", "outBr93"),
        ("TERRA-sdi480-MIB", "outBr94"),
        ("TERRA-sdi480-MIB", "outBr95"),
        ("TERRA-sdi480-MIB", "outBr96"),
        ("TERRA-sdi480-MIB", "outBr97"),
        ("TERRA-sdi480-MIB", "outBr98"),
        ("TERRA-sdi480-MIB", "outBr99"),
        ("TERRA-sdi480-MIB", "outBr100"),
        ("TERRA-sdi480-MIB", "outBr101"),
        ("TERRA-sdi480-MIB", "outBr102"),
        ("TERRA-sdi480-MIB", "outBr103"),
        ("TERRA-sdi480-MIB", "outBr104"),
        ("TERRA-sdi480-MIB", "outBr105"),
        ("TERRA-sdi480-MIB", "outBr106"),
        ("TERRA-sdi480-MIB", "outBr107"),
        ("TERRA-sdi480-MIB", "outBr108"),
        ("TERRA-sdi480-MIB", "outBr109"),
        ("TERRA-sdi480-MIB", "outBr110"),
        ("TERRA-sdi480-MIB", "outBr111"),
        ("TERRA-sdi480-MIB", "outBr112"),
        ("TERRA-sdi480-MIB", "outBr113"),
        ("TERRA-sdi480-MIB", "outBr114"),
        ("TERRA-sdi480-MIB", "outBr115"),
        ("TERRA-sdi480-MIB", "outBr116"),
        ("TERRA-sdi480-MIB", "outBr117"),
        ("TERRA-sdi480-MIB", "outBr118"),
        ("TERRA-sdi480-MIB", "outBr119"),
        ("TERRA-sdi480-MIB", "outBr120"),
        ("TERRA-sdi480-MIB", "outBr121"),
        ("TERRA-sdi480-MIB", "outBr122"),
        ("TERRA-sdi480-MIB", "outBr123"),
        ("TERRA-sdi480-MIB", "outBr124"),
        ("TERRA-sdi480-MIB", "outBr125"),
        ("TERRA-sdi480-MIB", "outBr126"),
        ("TERRA-sdi480-MIB", "outBr127"),
        ("TERRA-sdi480-MIB", "outBr128"),
        ("TERRA-sdi480-MIB", "outBr129"),
        ("TERRA-sdi480-MIB", "outBr130"),
        ("TERRA-sdi480-MIB", "outBr131"),
        ("TERRA-sdi480-MIB", "outBr132"),
        ("TERRA-sdi480-MIB", "outBr133"),
        ("TERRA-sdi480-MIB", "outBr134"),
        ("TERRA-sdi480-MIB", "outBr135"),
        ("TERRA-sdi480-MIB", "outBr136"),
        ("TERRA-sdi480-MIB", "outBr137"),
        ("TERRA-sdi480-MIB", "outBr138"),
        ("TERRA-sdi480-MIB", "outBr139"),
        ("TERRA-sdi480-MIB", "outBr140"),
        ("TERRA-sdi480-MIB", "outBr141"),
        ("TERRA-sdi480-MIB", "outBr142"),
        ("TERRA-sdi480-MIB", "outBr143"),
        ("TERRA-sdi480-MIB", "outBr144"),
        ("TERRA-sdi480-MIB", "outBr145"),
        ("TERRA-sdi480-MIB", "outBr146"),
        ("TERRA-sdi480-MIB", "outBr147"),
        ("TERRA-sdi480-MIB", "outBr148"),
        ("TERRA-sdi480-MIB", "outBr149"),
        ("TERRA-sdi480-MIB", "outBr150"),
        ("TERRA-sdi480-MIB", "outBr151"),
        ("TERRA-sdi480-MIB", "outBr152"),
        ("TERRA-sdi480-MIB", "outBr153"),
        ("TERRA-sdi480-MIB", "outBr154"),
        ("TERRA-sdi480-MIB", "outBr155"),
        ("TERRA-sdi480-MIB", "outBr156"),
        ("TERRA-sdi480-MIB", "outBr157"),
        ("TERRA-sdi480-MIB", "outBr158"),
        ("TERRA-sdi480-MIB", "outBr159"),
        ("TERRA-sdi480-MIB", "outBr160"),
        ("TERRA-sdi480-MIB", "outBr161"),
        ("TERRA-sdi480-MIB", "outBr162"),
        ("TERRA-sdi480-MIB", "outBr163"),
        ("TERRA-sdi480-MIB", "outBr164"),
        ("TERRA-sdi480-MIB", "outBr165"),
        ("TERRA-sdi480-MIB", "outBr166"),
        ("TERRA-sdi480-MIB", "outBr167"),
        ("TERRA-sdi480-MIB", "outBr168"),
        ("TERRA-sdi480-MIB", "outBr169"),
        ("TERRA-sdi480-MIB", "outBr170"),
        ("TERRA-sdi480-MIB", "outBr171"),
        ("TERRA-sdi480-MIB", "outBr172"),
        ("TERRA-sdi480-MIB", "outBr173"),
        ("TERRA-sdi480-MIB", "outBr174"),
        ("TERRA-sdi480-MIB", "outBr175"),
        ("TERRA-sdi480-MIB", "outBr176"),
        ("TERRA-sdi480-MIB", "outBr177"),
        ("TERRA-sdi480-MIB", "outBr178"),
        ("TERRA-sdi480-MIB", "outBr179"),
        ("TERRA-sdi480-MIB", "outBr180"),
        ("TERRA-sdi480-MIB", "outBr181"),
        ("TERRA-sdi480-MIB", "outBr182"),
        ("TERRA-sdi480-MIB", "outBr183"),
        ("TERRA-sdi480-MIB", "outBr184"),
        ("TERRA-sdi480-MIB", "outBr185"),
        ("TERRA-sdi480-MIB", "outBr186"),
        ("TERRA-sdi480-MIB", "outBr187"),
        ("TERRA-sdi480-MIB", "outBr188"),
        ("TERRA-sdi480-MIB", "outBr189"),
        ("TERRA-sdi480-MIB", "outBr190"),
        ("TERRA-sdi480-MIB", "outBr191"),
        ("TERRA-sdi480-MIB", "outBr192"),
        ("TERRA-sdi480-MIB", "outBr193"),
        ("TERRA-sdi480-MIB", "outBr194"),
        ("TERRA-sdi480-MIB", "outBr195"),
        ("TERRA-sdi480-MIB", "outBr196"),
        ("TERRA-sdi480-MIB", "outBr197"),
        ("TERRA-sdi480-MIB", "outBr198"),
        ("TERRA-sdi480-MIB", "outBr199"),
        ("TERRA-sdi480-MIB", "outBr200"),
        ("TERRA-sdi480-MIB", "outBr201"),
        ("TERRA-sdi480-MIB", "outBr202"),
        ("TERRA-sdi480-MIB", "outBr203"),
        ("TERRA-sdi480-MIB", "outBr204"),
        ("TERRA-sdi480-MIB", "outBr205"),
        ("TERRA-sdi480-MIB", "outBr206"),
        ("TERRA-sdi480-MIB", "outBr207"),
        ("TERRA-sdi480-MIB", "outBr208"),
        ("TERRA-sdi480-MIB", "outBr209"),
        ("TERRA-sdi480-MIB", "outBr210"),
        ("TERRA-sdi480-MIB", "outBr211"),
        ("TERRA-sdi480-MIB", "outBr212"),
        ("TERRA-sdi480-MIB", "outBr213"),
        ("TERRA-sdi480-MIB", "outBr214"),
        ("TERRA-sdi480-MIB", "outBr215"),
        ("TERRA-sdi480-MIB", "outBr216"),
        ("TERRA-sdi480-MIB", "outBr217"),
        ("TERRA-sdi480-MIB", "outBr218"),
        ("TERRA-sdi480-MIB", "outBr219"),
        ("TERRA-sdi480-MIB", "outBr220"),
        ("TERRA-sdi480-MIB", "outBr221"),
        ("TERRA-sdi480-MIB", "outBr222"),
        ("TERRA-sdi480-MIB", "outBr223"),
        ("TERRA-sdi480-MIB", "outBr224"),
        ("TERRA-sdi480-MIB", "outBr225"),
        ("TERRA-sdi480-MIB", "outBr226"),
        ("TERRA-sdi480-MIB", "outBr227"),
        ("TERRA-sdi480-MIB", "outBr228"),
        ("TERRA-sdi480-MIB", "outBr229"),
        ("TERRA-sdi480-MIB", "outBr230"),
        ("TERRA-sdi480-MIB", "outBr231"),
        ("TERRA-sdi480-MIB", "outBr232"),
        ("TERRA-sdi480-MIB", "outBr233"),
        ("TERRA-sdi480-MIB", "outBr234"),
        ("TERRA-sdi480-MIB", "outBr235"),
        ("TERRA-sdi480-MIB", "outBr236"),
        ("TERRA-sdi480-MIB", "outBr237"),
        ("TERRA-sdi480-MIB", "outBr238"),
        ("TERRA-sdi480-MIB", "outBr239"),
        ("TERRA-sdi480-MIB", "outBr240"),
        ("TERRA-sdi480-MIB", "outBr241"),
        ("TERRA-sdi480-MIB", "outBr242"),
        ("TERRA-sdi480-MIB", "outBr243"),
        ("TERRA-sdi480-MIB", "outBr244"),
        ("TERRA-sdi480-MIB", "outBr245"),
        ("TERRA-sdi480-MIB", "outBr246"),
        ("TERRA-sdi480-MIB", "outBr247"),
        ("TERRA-sdi480-MIB", "outBr248"),
        ("TERRA-sdi480-MIB", "outBr249"),
        ("TERRA-sdi480-MIB", "outBr250"),
        ("TERRA-sdi480-MIB", "outBr251"),
        ("TERRA-sdi480-MIB", "outBr252"),
        ("TERRA-sdi480-MIB", "outBr253"),
        ("TERRA-sdi480-MIB", "outBr254"),
        ("TERRA-sdi480-MIB", "outBr255"),
        ("TERRA-sdi480-MIB", "outBr256"),
        ("TERRA-sdi480-MIB", "outBr257"),
        ("TERRA-sdi480-MIB", "outBr258"),
        ("TERRA-sdi480-MIB", "outBr259"),
        ("TERRA-sdi480-MIB", "outBr260"),
        ("TERRA-sdi480-MIB", "outBr261"),
        ("TERRA-sdi480-MIB", "outBr262"),
        ("TERRA-sdi480-MIB", "outBr263"),
        ("TERRA-sdi480-MIB", "outBr264"),
        ("TERRA-sdi480-MIB", "outBr265"),
        ("TERRA-sdi480-MIB", "outBr266"),
        ("TERRA-sdi480-MIB", "outBr267"),
        ("TERRA-sdi480-MIB", "outBr268"),
        ("TERRA-sdi480-MIB", "outBr269"),
        ("TERRA-sdi480-MIB", "outBr270"),
        ("TERRA-sdi480-MIB", "outBr271"),
        ("TERRA-sdi480-MIB", "outBr272"),
        ("TERRA-sdi480-MIB", "outBr273"),
        ("TERRA-sdi480-MIB", "outBr274"),
        ("TERRA-sdi480-MIB", "outBr275"),
        ("TERRA-sdi480-MIB", "outBr276"),
        ("TERRA-sdi480-MIB", "outBr277"),
        ("TERRA-sdi480-MIB", "outBr278"),
        ("TERRA-sdi480-MIB", "outBr279"),
        ("TERRA-sdi480-MIB", "outBr280"),
        ("TERRA-sdi480-MIB", "outBr281"),
        ("TERRA-sdi480-MIB", "outBr282"),
        ("TERRA-sdi480-MIB", "outBr283"),
        ("TERRA-sdi480-MIB", "outBr284"),
        ("TERRA-sdi480-MIB", "outBr285"),
        ("TERRA-sdi480-MIB", "outBr286"),
        ("TERRA-sdi480-MIB", "outBr287"),
        ("TERRA-sdi480-MIB", "outBr288"),
        ("TERRA-sdi480-MIB", "outBr289"),
        ("TERRA-sdi480-MIB", "outBr290"),
        ("TERRA-sdi480-MIB", "outBr291"),
        ("TERRA-sdi480-MIB", "outBr292"),
        ("TERRA-sdi480-MIB", "outBr293"),
        ("TERRA-sdi480-MIB", "outBr294"),
        ("TERRA-sdi480-MIB", "outBr295"),
        ("TERRA-sdi480-MIB", "outBr296"),
        ("TERRA-sdi480-MIB", "outBr297"),
        ("TERRA-sdi480-MIB", "outBr298"),
        ("TERRA-sdi480-MIB", "outBr299"),
        ("TERRA-sdi480-MIB", "outBr300"),
        ("TERRA-sdi480-MIB", "outBr301"),
        ("TERRA-sdi480-MIB", "outBr302"),
        ("TERRA-sdi480-MIB", "outBr303"),
        ("TERRA-sdi480-MIB", "outBr304"),
        ("TERRA-sdi480-MIB", "outBr305"),
        ("TERRA-sdi480-MIB", "outBr306"),
        ("TERRA-sdi480-MIB", "outBr307"),
        ("TERRA-sdi480-MIB", "outBr308"),
        ("TERRA-sdi480-MIB", "outBr309"),
        ("TERRA-sdi480-MIB", "outBr310"),
        ("TERRA-sdi480-MIB", "outBr311"),
        ("TERRA-sdi480-MIB", "outBr312"),
        ("TERRA-sdi480-MIB", "outBr313"),
        ("TERRA-sdi480-MIB", "outBr314"),
        ("TERRA-sdi480-MIB", "outBr315"),
        ("TERRA-sdi480-MIB", "outBr316"),
        ("TERRA-sdi480-MIB", "outBr317"),
        ("TERRA-sdi480-MIB", "outBr318"),
        ("TERRA-sdi480-MIB", "outBr319"),
        ("TERRA-sdi480-MIB", "outBr320"),
        ("TERRA-sdi480-MIB", "outBr321"),
        ("TERRA-sdi480-MIB", "outBr322"),
        ("TERRA-sdi480-MIB", "outBr323"),
        ("TERRA-sdi480-MIB", "outBr324"),
        ("TERRA-sdi480-MIB", "outBr325"),
        ("TERRA-sdi480-MIB", "outBr326"),
        ("TERRA-sdi480-MIB", "outBr327"),
        ("TERRA-sdi480-MIB", "outBr328"),
        ("TERRA-sdi480-MIB", "outBr329"),
        ("TERRA-sdi480-MIB", "outBr330"),
        ("TERRA-sdi480-MIB", "outBr331"),
        ("TERRA-sdi480-MIB", "outBr332"),
        ("TERRA-sdi480-MIB", "outBr333"),
        ("TERRA-sdi480-MIB", "outBr334"),
        ("TERRA-sdi480-MIB", "outBr335"),
        ("TERRA-sdi480-MIB", "outBr336"),
        ("TERRA-sdi480-MIB", "outBr337"),
        ("TERRA-sdi480-MIB", "outBr338"),
        ("TERRA-sdi480-MIB", "outBr339"),
        ("TERRA-sdi480-MIB", "outBr340"),
        ("TERRA-sdi480-MIB", "outBr341"),
        ("TERRA-sdi480-MIB", "outBr342"),
        ("TERRA-sdi480-MIB", "outBr343"),
        ("TERRA-sdi480-MIB", "outBr344"),
        ("TERRA-sdi480-MIB", "outBr345"),
        ("TERRA-sdi480-MIB", "outBr346"),
        ("TERRA-sdi480-MIB", "outBr347"),
        ("TERRA-sdi480-MIB", "outBr348"),
        ("TERRA-sdi480-MIB", "outBr349"),
        ("TERRA-sdi480-MIB", "outBr350"),
        ("TERRA-sdi480-MIB", "outBr351"),
        ("TERRA-sdi480-MIB", "outBr352"),
        ("TERRA-sdi480-MIB", "outBr353"),
        ("TERRA-sdi480-MIB", "outBr354"),
        ("TERRA-sdi480-MIB", "outBr355"),
        ("TERRA-sdi480-MIB", "outBr356"),
        ("TERRA-sdi480-MIB", "outBr357"),
        ("TERRA-sdi480-MIB", "outBr358"),
        ("TERRA-sdi480-MIB", "outBr359"),
        ("TERRA-sdi480-MIB", "outBr360"),
        ("TERRA-sdi480-MIB", "outBr361"),
        ("TERRA-sdi480-MIB", "outBr362"),
        ("TERRA-sdi480-MIB", "outBr363"),
        ("TERRA-sdi480-MIB", "outBr364"),
        ("TERRA-sdi480-MIB", "outBr365"),
        ("TERRA-sdi480-MIB", "outBr366"),
        ("TERRA-sdi480-MIB", "outBr367"),
        ("TERRA-sdi480-MIB", "outBr368"),
        ("TERRA-sdi480-MIB", "outBr369"),
        ("TERRA-sdi480-MIB", "outBr370"),
        ("TERRA-sdi480-MIB", "outBr371"),
        ("TERRA-sdi480-MIB", "outBr372"),
        ("TERRA-sdi480-MIB", "outBr373"),
        ("TERRA-sdi480-MIB", "outBr374"),
        ("TERRA-sdi480-MIB", "outBr375"),
        ("TERRA-sdi480-MIB", "outBr376"),
        ("TERRA-sdi480-MIB", "outBr377"),
        ("TERRA-sdi480-MIB", "outBr378"),
        ("TERRA-sdi480-MIB", "outBr379"),
        ("TERRA-sdi480-MIB", "outBr380"),
        ("TERRA-sdi480-MIB", "outBr381"),
        ("TERRA-sdi480-MIB", "outBr382"),
        ("TERRA-sdi480-MIB", "outBr383"),
        ("TERRA-sdi480-MIB", "outBr384"),
        ("TERRA-sdi480-MIB", "outBr385"),
        ("TERRA-sdi480-MIB", "outBr386"),
        ("TERRA-sdi480-MIB", "outBr387"),
        ("TERRA-sdi480-MIB", "outBr388"),
        ("TERRA-sdi480-MIB", "outBr389"),
        ("TERRA-sdi480-MIB", "outBr390"),
        ("TERRA-sdi480-MIB", "outBr391"),
        ("TERRA-sdi480-MIB", "outBr392"),
        ("TERRA-sdi480-MIB", "outBr393"),
        ("TERRA-sdi480-MIB", "outBr394"),
        ("TERRA-sdi480-MIB", "outBr395"),
        ("TERRA-sdi480-MIB", "outBr396"),
        ("TERRA-sdi480-MIB", "outBr397"),
        ("TERRA-sdi480-MIB", "outBr398"),
        ("TERRA-sdi480-MIB", "outBr399"),
        ("TERRA-sdi480-MIB", "outBr400"),
        ("TERRA-sdi480-MIB", "outBr401"),
        ("TERRA-sdi480-MIB", "outBr402"),
        ("TERRA-sdi480-MIB", "outBr403"),
        ("TERRA-sdi480-MIB", "outBr404"),
        ("TERRA-sdi480-MIB", "outBr405"),
        ("TERRA-sdi480-MIB", "outBr406"),
        ("TERRA-sdi480-MIB", "outBr407"),
        ("TERRA-sdi480-MIB", "outBr408"),
        ("TERRA-sdi480-MIB", "outBr409"),
        ("TERRA-sdi480-MIB", "outBr410"),
        ("TERRA-sdi480-MIB", "outBr411"),
        ("TERRA-sdi480-MIB", "outBr412"),
        ("TERRA-sdi480-MIB", "outBr413"),
        ("TERRA-sdi480-MIB", "outBr414"),
        ("TERRA-sdi480-MIB", "outBr415"),
        ("TERRA-sdi480-MIB", "outBr416"),
        ("TERRA-sdi480-MIB", "outBr417"),
        ("TERRA-sdi480-MIB", "outBr418"),
        ("TERRA-sdi480-MIB", "outBr419"),
        ("TERRA-sdi480-MIB", "outBr420"),
        ("TERRA-sdi480-MIB", "outBr421"),
        ("TERRA-sdi480-MIB", "outBr422"),
        ("TERRA-sdi480-MIB", "outBr423"),
        ("TERRA-sdi480-MIB", "outBr424"),
        ("TERRA-sdi480-MIB", "outBr425"),
        ("TERRA-sdi480-MIB", "outBr426"),
        ("TERRA-sdi480-MIB", "outBr427"),
        ("TERRA-sdi480-MIB", "outBr428"),
        ("TERRA-sdi480-MIB", "outBr429"),
        ("TERRA-sdi480-MIB", "outBr430"),
        ("TERRA-sdi480-MIB", "outBr431"),
        ("TERRA-sdi480-MIB", "outBr432"),
        ("TERRA-sdi480-MIB", "outBr433"),
        ("TERRA-sdi480-MIB", "outBr434"),
        ("TERRA-sdi480-MIB", "outBr435"),
        ("TERRA-sdi480-MIB", "outBr436"),
        ("TERRA-sdi480-MIB", "outBr437"),
        ("TERRA-sdi480-MIB", "outBr438"),
        ("TERRA-sdi480-MIB", "outBr439"),
        ("TERRA-sdi480-MIB", "outBr440"),
        ("TERRA-sdi480-MIB", "outBr441"),
        ("TERRA-sdi480-MIB", "outBr442"),
        ("TERRA-sdi480-MIB", "outBr443"),
        ("TERRA-sdi480-MIB", "outBr444"),
        ("TERRA-sdi480-MIB", "outBr445"),
        ("TERRA-sdi480-MIB", "outBr446"),
        ("TERRA-sdi480-MIB", "outBr447"),
        ("TERRA-sdi480-MIB", "outBr448"),
        ("TERRA-sdi480-MIB", "outBr449"),
        ("TERRA-sdi480-MIB", "outBr450"),
        ("TERRA-sdi480-MIB", "outBr451"),
        ("TERRA-sdi480-MIB", "outBr452"),
        ("TERRA-sdi480-MIB", "outBr453"),
        ("TERRA-sdi480-MIB", "outBr454"),
        ("TERRA-sdi480-MIB", "outBr455"),
        ("TERRA-sdi480-MIB", "outBr456"),
        ("TERRA-sdi480-MIB", "outBr457"),
        ("TERRA-sdi480-MIB", "outBr458"),
        ("TERRA-sdi480-MIB", "outBr459"),
        ("TERRA-sdi480-MIB", "outBr460"),
        ("TERRA-sdi480-MIB", "outBr461"),
        ("TERRA-sdi480-MIB", "outBr462"),
        ("TERRA-sdi480-MIB", "outBr463"),
        ("TERRA-sdi480-MIB", "outBr464"),
        ("TERRA-sdi480-MIB", "outBr465"),
        ("TERRA-sdi480-MIB", "outBr466"),
        ("TERRA-sdi480-MIB", "outBr467"),
        ("TERRA-sdi480-MIB", "outBr468"),
        ("TERRA-sdi480-MIB", "outBr469"),
        ("TERRA-sdi480-MIB", "outBr470"),
        ("TERRA-sdi480-MIB", "outBr471"),
        ("TERRA-sdi480-MIB", "outBr472"),
        ("TERRA-sdi480-MIB", "outBr473"),
        ("TERRA-sdi480-MIB", "outBr474"),
        ("TERRA-sdi480-MIB", "outBr475"),
        ("TERRA-sdi480-MIB", "outBr476"),
        ("TERRA-sdi480-MIB", "outBr477"),
        ("TERRA-sdi480-MIB", "outBr478"),
        ("TERRA-sdi480-MIB", "outBr479"),
        ("TERRA-sdi480-MIB", "outBr480"),
        ("TERRA-sdi480-MIB", "outBr481"),
        ("TERRA-sdi480-MIB", "outBr482"),
        ("TERRA-sdi480-MIB", "outBr483"),
        ("TERRA-sdi480-MIB", "outBr484"),
        ("TERRA-sdi480-MIB", "outBr485"),
        ("TERRA-sdi480-MIB", "outBr486"),
        ("TERRA-sdi480-MIB", "outBr487"),
        ("TERRA-sdi480-MIB", "outBr488"),
        ("TERRA-sdi480-MIB", "outBr489"),
        ("TERRA-sdi480-MIB", "outBr490"),
        ("TERRA-sdi480-MIB", "outBr491"),
        ("TERRA-sdi480-MIB", "outBr492"),
        ("TERRA-sdi480-MIB", "outBr493"),
        ("TERRA-sdi480-MIB", "outBr494"),
        ("TERRA-sdi480-MIB", "outBr495"),
        ("TERRA-sdi480-MIB", "outBr496"),
        ("TERRA-sdi480-MIB", "outBr497"),
        ("TERRA-sdi480-MIB", "outBr498"),
        ("TERRA-sdi480-MIB", "outBr499"),
        ("TERRA-sdi480-MIB", "outBr500"),
        ("TERRA-sdi480-MIB", "outBr501"),
        ("TERRA-sdi480-MIB", "outBr502"),
        ("TERRA-sdi480-MIB", "outBr503"),
        ("TERRA-sdi480-MIB", "outBr504"),
        ("TERRA-sdi480-MIB", "outBr505"),
        ("TERRA-sdi480-MIB", "outBr506"),
        ("TERRA-sdi480-MIB", "outBr507"),
        ("TERRA-sdi480-MIB", "outBr508"),
        ("TERRA-sdi480-MIB", "outBr509"),
        ("TERRA-sdi480-MIB", "outBr510"),
        ("TERRA-sdi480-MIB", "outBr511"),
        ("TERRA-sdi480-MIB", "outBr512"),
        ("TERRA-sdi480-MIB", "outBr513"),
        ("TERRA-sdi480-MIB", "outBr514"),
        ("TERRA-sdi480-MIB", "outBr515"),
        ("TERRA-sdi480-MIB", "outBr516"),
        ("TERRA-sdi480-MIB", "outBr517"),
        ("TERRA-sdi480-MIB", "outBr518"),
        ("TERRA-sdi480-MIB", "outBr519"),
        ("TERRA-sdi480-MIB", "outBr520"),
        ("TERRA-sdi480-MIB", "outBr521"),
        ("TERRA-sdi480-MIB", "outBr522"),
        ("TERRA-sdi480-MIB", "outBr523"),
        ("TERRA-sdi480-MIB", "outBr524"),
        ("TERRA-sdi480-MIB", "outBr525"),
        ("TERRA-sdi480-MIB", "outBr526"),
        ("TERRA-sdi480-MIB", "outBr527"),
        ("TERRA-sdi480-MIB", "outBr528"),
        ("TERRA-sdi480-MIB", "outBr529"),
        ("TERRA-sdi480-MIB", "outBr530"),
        ("TERRA-sdi480-MIB", "outBr531"),
        ("TERRA-sdi480-MIB", "outBr532"),
        ("TERRA-sdi480-MIB", "outBr533"),
        ("TERRA-sdi480-MIB", "outBr534"),
        ("TERRA-sdi480-MIB", "outBr535"),
        ("TERRA-sdi480-MIB", "outBr536"),
        ("TERRA-sdi480-MIB", "outBr537"),
        ("TERRA-sdi480-MIB", "outBr538"),
        ("TERRA-sdi480-MIB", "outBr539"),
        ("TERRA-sdi480-MIB", "outBr540"),
        ("TERRA-sdi480-MIB", "outBr541"),
        ("TERRA-sdi480-MIB", "outBr542"),
        ("TERRA-sdi480-MIB", "outBr543"),
        ("TERRA-sdi480-MIB", "outBr544"),
        ("TERRA-sdi480-MIB", "outBr545"),
        ("TERRA-sdi480-MIB", "outBr546"),
        ("TERRA-sdi480-MIB", "outBr547"),
        ("TERRA-sdi480-MIB", "outBr548"),
        ("TERRA-sdi480-MIB", "outBr549"),
        ("TERRA-sdi480-MIB", "outBr550"),
        ("TERRA-sdi480-MIB", "outBr551"),
        ("TERRA-sdi480-MIB", "outBr552"),
        ("TERRA-sdi480-MIB", "outBr553"),
        ("TERRA-sdi480-MIB", "outBr554"),
        ("TERRA-sdi480-MIB", "outBr555"),
        ("TERRA-sdi480-MIB", "outBr556"),
        ("TERRA-sdi480-MIB", "outBr557"),
        ("TERRA-sdi480-MIB", "outBr558"),
        ("TERRA-sdi480-MIB", "outBr559"),
        ("TERRA-sdi480-MIB", "outBr560"),
        ("TERRA-sdi480-MIB", "outBr561"),
        ("TERRA-sdi480-MIB", "outBr562"),
        ("TERRA-sdi480-MIB", "outBr563"),
        ("TERRA-sdi480-MIB", "outBr564"),
        ("TERRA-sdi480-MIB", "outBr565"),
        ("TERRA-sdi480-MIB", "outBr566"),
        ("TERRA-sdi480-MIB", "outBr567"),
        ("TERRA-sdi480-MIB", "outBr568"),
        ("TERRA-sdi480-MIB", "outBr569"),
        ("TERRA-sdi480-MIB", "outBr570"),
        ("TERRA-sdi480-MIB", "outBr571"),
        ("TERRA-sdi480-MIB", "outBr572"),
        ("TERRA-sdi480-MIB", "outBr573"),
        ("TERRA-sdi480-MIB", "outBr574"),
        ("TERRA-sdi480-MIB", "outBr575"),
        ("TERRA-sdi480-MIB", "outBr576"),
        ("TERRA-sdi480-MIB", "inTotbr"),
        ("TERRA-sdi480-MIB", "outTotbr"),
        ("TERRA-sdi480-MIB", "cpuLoad"),
        ("TERRA-sdi480-MIB", "intTemp"),
        ("TERRA-sdi480-MIB", "demodTemp"),
        ("TERRA-sdi480-MIB", "volt"),
        ("TERRA-sdi480-MIB", "alarmLnb1"),
        ("TERRA-sdi480-MIB", "alarmLnb2"),
        ("TERRA-sdi480-MIB", "alarmLnb3"),
        ("TERRA-sdi480-MIB", "alarmLnb4"),
        ("TERRA-sdi480-MIB", "alarmStlink"),
        ("TERRA-sdi480-MIB", "alarmCtrlink"),
        ("TERRA-sdi480-MIB", "alarmBrovf"),
        ("TERRA-sdi480-MIB", "alarmUnlock1"),
        ("TERRA-sdi480-MIB", "alarmUnlock2"),
        ("TERRA-sdi480-MIB", "alarmUnlock3"),
        ("TERRA-sdi480-MIB", "alarmUnlock4"),
        ("TERRA-sdi480-MIB", "alarmUnlock5"),
        ("TERRA-sdi480-MIB", "alarmUnlock6"),
        ("TERRA-sdi480-MIB", "alarmUnlock7"),
        ("TERRA-sdi480-MIB", "alarmUnlock8"),
        ("TERRA-sdi480-MIB", "alarmUnlock9"),
        ("TERRA-sdi480-MIB", "alarmPowerr"),
        ("TERRA-sdi480-MIB", "alarmTemperr"),
        ("TERRA-sdi480-MIB", "alarmIbrer"),
        ("TERRA-sdi480-MIB", "infVersion"),
        ("TERRA-sdi480-MIB", "infSerNum"))
)
if mibBuilder.loadTexts:
    sdi480TerraMibAllObjects.setStatus("current")


# Notification objects

notifyLnb1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 1)
)
notifyLnb1.setObjects(
    ("TERRA-sdi480-MIB", "alarmLnb1")
)
if mibBuilder.loadTexts:
    notifyLnb1.setStatus(
        "current"
    )

notifyLnb2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 2)
)
notifyLnb2.setObjects(
    ("TERRA-sdi480-MIB", "alarmLnb2")
)
if mibBuilder.loadTexts:
    notifyLnb2.setStatus(
        "current"
    )

notifyLnb3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 3)
)
notifyLnb3.setObjects(
    ("TERRA-sdi480-MIB", "alarmLnb3")
)
if mibBuilder.loadTexts:
    notifyLnb3.setStatus(
        "current"
    )

notifyLnb4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 4)
)
notifyLnb4.setObjects(
    ("TERRA-sdi480-MIB", "alarmLnb4")
)
if mibBuilder.loadTexts:
    notifyLnb4.setStatus(
        "current"
    )

notifyStlink = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 5)
)
notifyStlink.setObjects(
    ("TERRA-sdi480-MIB", "alarmStlink")
)
if mibBuilder.loadTexts:
    notifyStlink.setStatus(
        "current"
    )

notifyCtrlink = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 6)
)
notifyCtrlink.setObjects(
    ("TERRA-sdi480-MIB", "alarmCtrlink")
)
if mibBuilder.loadTexts:
    notifyCtrlink.setStatus(
        "current"
    )

notifyBrovf = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 7)
)
notifyBrovf.setObjects(
    ("TERRA-sdi480-MIB", "alarmBrovf")
)
if mibBuilder.loadTexts:
    notifyBrovf.setStatus(
        "current"
    )

notifyUnlock1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 8)
)
notifyUnlock1.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock1")
)
if mibBuilder.loadTexts:
    notifyUnlock1.setStatus(
        "current"
    )

notifyUnlock2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 9)
)
notifyUnlock2.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock2")
)
if mibBuilder.loadTexts:
    notifyUnlock2.setStatus(
        "current"
    )

notifyUnlock3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 10)
)
notifyUnlock3.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock3")
)
if mibBuilder.loadTexts:
    notifyUnlock3.setStatus(
        "current"
    )

notifyUnlock4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 11)
)
notifyUnlock4.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock4")
)
if mibBuilder.loadTexts:
    notifyUnlock4.setStatus(
        "current"
    )

notifyUnlock5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 12)
)
notifyUnlock5.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock5")
)
if mibBuilder.loadTexts:
    notifyUnlock5.setStatus(
        "current"
    )

notifyUnlock6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 13)
)
notifyUnlock6.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock6")
)
if mibBuilder.loadTexts:
    notifyUnlock6.setStatus(
        "current"
    )

notifyUnlock7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 14)
)
notifyUnlock7.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock7")
)
if mibBuilder.loadTexts:
    notifyUnlock7.setStatus(
        "current"
    )

notifyUnlock8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 15)
)
notifyUnlock8.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock8")
)
if mibBuilder.loadTexts:
    notifyUnlock8.setStatus(
        "current"
    )

notifyUnlock9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 16)
)
notifyUnlock9.setObjects(
    ("TERRA-sdi480-MIB", "alarmUnlock9")
)
if mibBuilder.loadTexts:
    notifyUnlock9.setStatus(
        "current"
    )

notifyPowerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 17)
)
notifyPowerr.setObjects(
    ("TERRA-sdi480-MIB", "alarmPowerr")
)
if mibBuilder.loadTexts:
    notifyPowerr.setStatus(
        "current"
    )

notifyTemperr = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 18)
)
notifyTemperr.setObjects(
    ("TERRA-sdi480-MIB", "alarmTemperr")
)
if mibBuilder.loadTexts:
    notifyTemperr.setStatus(
        "current"
    )

notifyIbrer = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 3, 19)
)
notifyIbrer.setObjects(
    ("TERRA-sdi480-MIB", "alarmIbrer")
)
if mibBuilder.loadTexts:
    notifyIbrer.setStatus(
        "current"
    )


# Notifications groups

sdi480TerraMibAllNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30631, 1, 17, 5, 1, 2)
)
sdi480TerraMibAllNotifications.setObjects(
      *(("TERRA-sdi480-MIB", "notifyLnb1"),
        ("TERRA-sdi480-MIB", "notifyLnb2"),
        ("TERRA-sdi480-MIB", "notifyLnb3"),
        ("TERRA-sdi480-MIB", "notifyLnb4"),
        ("TERRA-sdi480-MIB", "notifyStlink"),
        ("TERRA-sdi480-MIB", "notifyCtrlink"),
        ("TERRA-sdi480-MIB", "notifyBrovf"),
        ("TERRA-sdi480-MIB", "notifyUnlock1"),
        ("TERRA-sdi480-MIB", "notifyUnlock2"),
        ("TERRA-sdi480-MIB", "notifyUnlock3"),
        ("TERRA-sdi480-MIB", "notifyUnlock4"),
        ("TERRA-sdi480-MIB", "notifyUnlock5"),
        ("TERRA-sdi480-MIB", "notifyUnlock6"),
        ("TERRA-sdi480-MIB", "notifyUnlock7"),
        ("TERRA-sdi480-MIB", "notifyUnlock8"),
        ("TERRA-sdi480-MIB", "notifyUnlock9"),
        ("TERRA-sdi480-MIB", "notifyPowerr"),
        ("TERRA-sdi480-MIB", "notifyTemperr"),
        ("TERRA-sdi480-MIB", "notifyIbrer"))
)
if mibBuilder.loadTexts:
    sdi480TerraMibAllNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERRA-sdi480-MIB",
    **{"terra-sdi480": terra_sdi480,
       "sdi480status": sdi480status,
       "rFinStatus1": rFinStatus1,
       "inLock1": inLock1,
       "inlevel1": inlevel1,
       "insnr1": insnr1,
       "inbr1": inbr1,
       "inper1": inper1,
       "rFinStatus2": rFinStatus2,
       "inLock2": inLock2,
       "inlevel2": inlevel2,
       "insnr2": insnr2,
       "inbr2": inbr2,
       "inper2": inper2,
       "rFinStatus3": rFinStatus3,
       "inLock3": inLock3,
       "inlevel3": inlevel3,
       "insnr3": insnr3,
       "inbr3": inbr3,
       "inper3": inper3,
       "rFinStatus4": rFinStatus4,
       "inLock4": inLock4,
       "inlevel4": inlevel4,
       "insnr4": insnr4,
       "inbr4": inbr4,
       "inper4": inper4,
       "rFinStatus5": rFinStatus5,
       "inLock5": inLock5,
       "inlevel5": inlevel5,
       "insnr5": insnr5,
       "inbr5": inbr5,
       "inper5": inper5,
       "rFinStatus6": rFinStatus6,
       "inLock6": inLock6,
       "inlevel6": inlevel6,
       "insnr6": insnr6,
       "inbr6": inbr6,
       "inper6": inper6,
       "rFinStatus7": rFinStatus7,
       "inLock7": inLock7,
       "inlevel7": inlevel7,
       "insnr7": insnr7,
       "inbr7": inbr7,
       "inper7": inper7,
       "rFinStatus8": rFinStatus8,
       "inLock8": inLock8,
       "inlevel8": inlevel8,
       "insnr8": insnr8,
       "inbr8": inbr8,
       "inper8": inper8,
       "usbStatus": usbStatus,
       "usbinBR": usbinBR,
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
       "outStream26": outStream26,
       "outBr26": outBr26,
       "outStream27": outStream27,
       "outBr27": outBr27,
       "outStream28": outStream28,
       "outBr28": outBr28,
       "outStream29": outStream29,
       "outBr29": outBr29,
       "outStream30": outStream30,
       "outBr30": outBr30,
       "outStream31": outStream31,
       "outBr31": outBr31,
       "outStream32": outStream32,
       "outBr32": outBr32,
       "outStream33": outStream33,
       "outBr33": outBr33,
       "outStream34": outStream34,
       "outBr34": outBr34,
       "outStream35": outStream35,
       "outBr35": outBr35,
       "outStream36": outStream36,
       "outBr36": outBr36,
       "outStream37": outStream37,
       "outBr37": outBr37,
       "outStream38": outStream38,
       "outBr38": outBr38,
       "outStream39": outStream39,
       "outBr39": outBr39,
       "outStream40": outStream40,
       "outBr40": outBr40,
       "outStream41": outStream41,
       "outBr41": outBr41,
       "outStream42": outStream42,
       "outBr42": outBr42,
       "outStream43": outStream43,
       "outBr43": outBr43,
       "outStream44": outStream44,
       "outBr44": outBr44,
       "outStream45": outStream45,
       "outBr45": outBr45,
       "outStream46": outStream46,
       "outBr46": outBr46,
       "outStream47": outStream47,
       "outBr47": outBr47,
       "outStream48": outStream48,
       "outBr48": outBr48,
       "outStream49": outStream49,
       "outBr49": outBr49,
       "outStream50": outStream50,
       "outBr50": outBr50,
       "outStream51": outStream51,
       "outBr51": outBr51,
       "outStream52": outStream52,
       "outBr52": outBr52,
       "outStream53": outStream53,
       "outBr53": outBr53,
       "outStream54": outStream54,
       "outBr54": outBr54,
       "outStream55": outStream55,
       "outBr55": outBr55,
       "outStream56": outStream56,
       "outBr56": outBr56,
       "outStream57": outStream57,
       "outBr57": outBr57,
       "outStream58": outStream58,
       "outBr58": outBr58,
       "outStream59": outStream59,
       "outBr59": outBr59,
       "outStream60": outStream60,
       "outBr60": outBr60,
       "outStream61": outStream61,
       "outBr61": outBr61,
       "outStream62": outStream62,
       "outBr62": outBr62,
       "outStream63": outStream63,
       "outBr63": outBr63,
       "outStream64": outStream64,
       "outBr64": outBr64,
       "outStream65": outStream65,
       "outBr65": outBr65,
       "outStream66": outStream66,
       "outBr66": outBr66,
       "outStream67": outStream67,
       "outBr67": outBr67,
       "outStream68": outStream68,
       "outBr68": outBr68,
       "outStream69": outStream69,
       "outBr69": outBr69,
       "outStream70": outStream70,
       "outBr70": outBr70,
       "outStream71": outStream71,
       "outBr71": outBr71,
       "outStream72": outStream72,
       "outBr72": outBr72,
       "outStream73": outStream73,
       "outBr73": outBr73,
       "outStream74": outStream74,
       "outBr74": outBr74,
       "outStream75": outStream75,
       "outBr75": outBr75,
       "outStream76": outStream76,
       "outBr76": outBr76,
       "outStream77": outStream77,
       "outBr77": outBr77,
       "outStream78": outStream78,
       "outBr78": outBr78,
       "outStream79": outStream79,
       "outBr79": outBr79,
       "outStream80": outStream80,
       "outBr80": outBr80,
       "outStream81": outStream81,
       "outBr81": outBr81,
       "outStream82": outStream82,
       "outBr82": outBr82,
       "outStream83": outStream83,
       "outBr83": outBr83,
       "outStream84": outStream84,
       "outBr84": outBr84,
       "outStream85": outStream85,
       "outBr85": outBr85,
       "outStream86": outStream86,
       "outBr86": outBr86,
       "outStream87": outStream87,
       "outBr87": outBr87,
       "outStream88": outStream88,
       "outBr88": outBr88,
       "outStream89": outStream89,
       "outBr89": outBr89,
       "outStream90": outStream90,
       "outBr90": outBr90,
       "outStream91": outStream91,
       "outBr91": outBr91,
       "outStream92": outStream92,
       "outBr92": outBr92,
       "outStream93": outStream93,
       "outBr93": outBr93,
       "outStream94": outStream94,
       "outBr94": outBr94,
       "outStream95": outStream95,
       "outBr95": outBr95,
       "outStream96": outStream96,
       "outBr96": outBr96,
       "outStream97": outStream97,
       "outBr97": outBr97,
       "outStream98": outStream98,
       "outBr98": outBr98,
       "outStream99": outStream99,
       "outBr99": outBr99,
       "outStream100": outStream100,
       "outBr100": outBr100,
       "outStream101": outStream101,
       "outBr101": outBr101,
       "outStream102": outStream102,
       "outBr102": outBr102,
       "outStream103": outStream103,
       "outBr103": outBr103,
       "outStream104": outStream104,
       "outBr104": outBr104,
       "outStream105": outStream105,
       "outBr105": outBr105,
       "outStream106": outStream106,
       "outBr106": outBr106,
       "outStream107": outStream107,
       "outBr107": outBr107,
       "outStream108": outStream108,
       "outBr108": outBr108,
       "outStream109": outStream109,
       "outBr109": outBr109,
       "outStream110": outStream110,
       "outBr110": outBr110,
       "outStream111": outStream111,
       "outBr111": outBr111,
       "outStream112": outStream112,
       "outBr112": outBr112,
       "outStream113": outStream113,
       "outBr113": outBr113,
       "outStream114": outStream114,
       "outBr114": outBr114,
       "outStream115": outStream115,
       "outBr115": outBr115,
       "outStream116": outStream116,
       "outBr116": outBr116,
       "outStream117": outStream117,
       "outBr117": outBr117,
       "outStream118": outStream118,
       "outBr118": outBr118,
       "outStream119": outStream119,
       "outBr119": outBr119,
       "outStream120": outStream120,
       "outBr120": outBr120,
       "outStream121": outStream121,
       "outBr121": outBr121,
       "outStream122": outStream122,
       "outBr122": outBr122,
       "outStream123": outStream123,
       "outBr123": outBr123,
       "outStream124": outStream124,
       "outBr124": outBr124,
       "outStream125": outStream125,
       "outBr125": outBr125,
       "outStream126": outStream126,
       "outBr126": outBr126,
       "outStream127": outStream127,
       "outBr127": outBr127,
       "outStream128": outStream128,
       "outBr128": outBr128,
       "outStream129": outStream129,
       "outBr129": outBr129,
       "outStream130": outStream130,
       "outBr130": outBr130,
       "outStream131": outStream131,
       "outBr131": outBr131,
       "outStream132": outStream132,
       "outBr132": outBr132,
       "outStream133": outStream133,
       "outBr133": outBr133,
       "outStream134": outStream134,
       "outBr134": outBr134,
       "outStream135": outStream135,
       "outBr135": outBr135,
       "outStream136": outStream136,
       "outBr136": outBr136,
       "outStream137": outStream137,
       "outBr137": outBr137,
       "outStream138": outStream138,
       "outBr138": outBr138,
       "outStream139": outStream139,
       "outBr139": outBr139,
       "outStream140": outStream140,
       "outBr140": outBr140,
       "outStream141": outStream141,
       "outBr141": outBr141,
       "outStream142": outStream142,
       "outBr142": outBr142,
       "outStream143": outStream143,
       "outBr143": outBr143,
       "outStream144": outStream144,
       "outBr144": outBr144,
       "outStream145": outStream145,
       "outBr145": outBr145,
       "outStream146": outStream146,
       "outBr146": outBr146,
       "outStream147": outStream147,
       "outBr147": outBr147,
       "outStream148": outStream148,
       "outBr148": outBr148,
       "outStream149": outStream149,
       "outBr149": outBr149,
       "outStream150": outStream150,
       "outBr150": outBr150,
       "outStream151": outStream151,
       "outBr151": outBr151,
       "outStream152": outStream152,
       "outBr152": outBr152,
       "outStream153": outStream153,
       "outBr153": outBr153,
       "outStream154": outStream154,
       "outBr154": outBr154,
       "outStream155": outStream155,
       "outBr155": outBr155,
       "outStream156": outStream156,
       "outBr156": outBr156,
       "outStream157": outStream157,
       "outBr157": outBr157,
       "outStream158": outStream158,
       "outBr158": outBr158,
       "outStream159": outStream159,
       "outBr159": outBr159,
       "outStream160": outStream160,
       "outBr160": outBr160,
       "outStream161": outStream161,
       "outBr161": outBr161,
       "outStream162": outStream162,
       "outBr162": outBr162,
       "outStream163": outStream163,
       "outBr163": outBr163,
       "outStream164": outStream164,
       "outBr164": outBr164,
       "outStream165": outStream165,
       "outBr165": outBr165,
       "outStream166": outStream166,
       "outBr166": outBr166,
       "outStream167": outStream167,
       "outBr167": outBr167,
       "outStream168": outStream168,
       "outBr168": outBr168,
       "outStream169": outStream169,
       "outBr169": outBr169,
       "outStream170": outStream170,
       "outBr170": outBr170,
       "outStream171": outStream171,
       "outBr171": outBr171,
       "outStream172": outStream172,
       "outBr172": outBr172,
       "outStream173": outStream173,
       "outBr173": outBr173,
       "outStream174": outStream174,
       "outBr174": outBr174,
       "outStream175": outStream175,
       "outBr175": outBr175,
       "outStream176": outStream176,
       "outBr176": outBr176,
       "outStream177": outStream177,
       "outBr177": outBr177,
       "outStream178": outStream178,
       "outBr178": outBr178,
       "outStream179": outStream179,
       "outBr179": outBr179,
       "outStream180": outStream180,
       "outBr180": outBr180,
       "outStream181": outStream181,
       "outBr181": outBr181,
       "outStream182": outStream182,
       "outBr182": outBr182,
       "outStream183": outStream183,
       "outBr183": outBr183,
       "outStream184": outStream184,
       "outBr184": outBr184,
       "outStream185": outStream185,
       "outBr185": outBr185,
       "outStream186": outStream186,
       "outBr186": outBr186,
       "outStream187": outStream187,
       "outBr187": outBr187,
       "outStream188": outStream188,
       "outBr188": outBr188,
       "outStream189": outStream189,
       "outBr189": outBr189,
       "outStream190": outStream190,
       "outBr190": outBr190,
       "outStream191": outStream191,
       "outBr191": outBr191,
       "outStream192": outStream192,
       "outBr192": outBr192,
       "outStream193": outStream193,
       "outBr193": outBr193,
       "outStream194": outStream194,
       "outBr194": outBr194,
       "outStream195": outStream195,
       "outBr195": outBr195,
       "outStream196": outStream196,
       "outBr196": outBr196,
       "outStream197": outStream197,
       "outBr197": outBr197,
       "outStream198": outStream198,
       "outBr198": outBr198,
       "outStream199": outStream199,
       "outBr199": outBr199,
       "outStream200": outStream200,
       "outBr200": outBr200,
       "outStream201": outStream201,
       "outBr201": outBr201,
       "outStream202": outStream202,
       "outBr202": outBr202,
       "outStream203": outStream203,
       "outBr203": outBr203,
       "outStream204": outStream204,
       "outBr204": outBr204,
       "outStream205": outStream205,
       "outBr205": outBr205,
       "outStream206": outStream206,
       "outBr206": outBr206,
       "outStream207": outStream207,
       "outBr207": outBr207,
       "outStream208": outStream208,
       "outBr208": outBr208,
       "outStream209": outStream209,
       "outBr209": outBr209,
       "outStream210": outStream210,
       "outBr210": outBr210,
       "outStream211": outStream211,
       "outBr211": outBr211,
       "outStream212": outStream212,
       "outBr212": outBr212,
       "outStream213": outStream213,
       "outBr213": outBr213,
       "outStream214": outStream214,
       "outBr214": outBr214,
       "outStream215": outStream215,
       "outBr215": outBr215,
       "outStream216": outStream216,
       "outBr216": outBr216,
       "outStream217": outStream217,
       "outBr217": outBr217,
       "outStream218": outStream218,
       "outBr218": outBr218,
       "outStream219": outStream219,
       "outBr219": outBr219,
       "outStream220": outStream220,
       "outBr220": outBr220,
       "outStream221": outStream221,
       "outBr221": outBr221,
       "outStream222": outStream222,
       "outBr222": outBr222,
       "outStream223": outStream223,
       "outBr223": outBr223,
       "outStream224": outStream224,
       "outBr224": outBr224,
       "outStream225": outStream225,
       "outBr225": outBr225,
       "outStream226": outStream226,
       "outBr226": outBr226,
       "outStream227": outStream227,
       "outBr227": outBr227,
       "outStream228": outStream228,
       "outBr228": outBr228,
       "outStream229": outStream229,
       "outBr229": outBr229,
       "outStream230": outStream230,
       "outBr230": outBr230,
       "outStream231": outStream231,
       "outBr231": outBr231,
       "outStream232": outStream232,
       "outBr232": outBr232,
       "outStream233": outStream233,
       "outBr233": outBr233,
       "outStream234": outStream234,
       "outBr234": outBr234,
       "outStream235": outStream235,
       "outBr235": outBr235,
       "outStream236": outStream236,
       "outBr236": outBr236,
       "outStream237": outStream237,
       "outBr237": outBr237,
       "outStream238": outStream238,
       "outBr238": outBr238,
       "outStream239": outStream239,
       "outBr239": outBr239,
       "outStream240": outStream240,
       "outBr240": outBr240,
       "outStream241": outStream241,
       "outBr241": outBr241,
       "outStream242": outStream242,
       "outBr242": outBr242,
       "outStream243": outStream243,
       "outBr243": outBr243,
       "outStream244": outStream244,
       "outBr244": outBr244,
       "outStream245": outStream245,
       "outBr245": outBr245,
       "outStream246": outStream246,
       "outBr246": outBr246,
       "outStream247": outStream247,
       "outBr247": outBr247,
       "outStream248": outStream248,
       "outBr248": outBr248,
       "outStream249": outStream249,
       "outBr249": outBr249,
       "outStream250": outStream250,
       "outBr250": outBr250,
       "outStream251": outStream251,
       "outBr251": outBr251,
       "outStream252": outStream252,
       "outBr252": outBr252,
       "outStream253": outStream253,
       "outBr253": outBr253,
       "outStream254": outStream254,
       "outBr254": outBr254,
       "outStream255": outStream255,
       "outBr255": outBr255,
       "outStream256": outStream256,
       "outBr256": outBr256,
       "outStream257": outStream257,
       "outBr257": outBr257,
       "outStream258": outStream258,
       "outBr258": outBr258,
       "outStream259": outStream259,
       "outBr259": outBr259,
       "outStream260": outStream260,
       "outBr260": outBr260,
       "outStream261": outStream261,
       "outBr261": outBr261,
       "outStream262": outStream262,
       "outBr262": outBr262,
       "outStream263": outStream263,
       "outBr263": outBr263,
       "outStream264": outStream264,
       "outBr264": outBr264,
       "outStream265": outStream265,
       "outBr265": outBr265,
       "outStream266": outStream266,
       "outBr266": outBr266,
       "outStream267": outStream267,
       "outBr267": outBr267,
       "outStream268": outStream268,
       "outBr268": outBr268,
       "outStream269": outStream269,
       "outBr269": outBr269,
       "outStream270": outStream270,
       "outBr270": outBr270,
       "outStream271": outStream271,
       "outBr271": outBr271,
       "outStream272": outStream272,
       "outBr272": outBr272,
       "outStream273": outStream273,
       "outBr273": outBr273,
       "outStream274": outStream274,
       "outBr274": outBr274,
       "outStream275": outStream275,
       "outBr275": outBr275,
       "outStream276": outStream276,
       "outBr276": outBr276,
       "outStream277": outStream277,
       "outBr277": outBr277,
       "outStream278": outStream278,
       "outBr278": outBr278,
       "outStream279": outStream279,
       "outBr279": outBr279,
       "outStream280": outStream280,
       "outBr280": outBr280,
       "outStream281": outStream281,
       "outBr281": outBr281,
       "outStream282": outStream282,
       "outBr282": outBr282,
       "outStream283": outStream283,
       "outBr283": outBr283,
       "outStream284": outStream284,
       "outBr284": outBr284,
       "outStream285": outStream285,
       "outBr285": outBr285,
       "outStream286": outStream286,
       "outBr286": outBr286,
       "outStream287": outStream287,
       "outBr287": outBr287,
       "outStream288": outStream288,
       "outBr288": outBr288,
       "outStream289": outStream289,
       "outBr289": outBr289,
       "outStream290": outStream290,
       "outBr290": outBr290,
       "outStream291": outStream291,
       "outBr291": outBr291,
       "outStream292": outStream292,
       "outBr292": outBr292,
       "outStream293": outStream293,
       "outBr293": outBr293,
       "outStream294": outStream294,
       "outBr294": outBr294,
       "outStream295": outStream295,
       "outBr295": outBr295,
       "outStream296": outStream296,
       "outBr296": outBr296,
       "outStream297": outStream297,
       "outBr297": outBr297,
       "outStream298": outStream298,
       "outBr298": outBr298,
       "outStream299": outStream299,
       "outBr299": outBr299,
       "outStream300": outStream300,
       "outBr300": outBr300,
       "outStream301": outStream301,
       "outBr301": outBr301,
       "outStream302": outStream302,
       "outBr302": outBr302,
       "outStream303": outStream303,
       "outBr303": outBr303,
       "outStream304": outStream304,
       "outBr304": outBr304,
       "outStream305": outStream305,
       "outBr305": outBr305,
       "outStream306": outStream306,
       "outBr306": outBr306,
       "outStream307": outStream307,
       "outBr307": outBr307,
       "outStream308": outStream308,
       "outBr308": outBr308,
       "outStream309": outStream309,
       "outBr309": outBr309,
       "outStream310": outStream310,
       "outBr310": outBr310,
       "outStream311": outStream311,
       "outBr311": outBr311,
       "outStream312": outStream312,
       "outBr312": outBr312,
       "outStream313": outStream313,
       "outBr313": outBr313,
       "outStream314": outStream314,
       "outBr314": outBr314,
       "outStream315": outStream315,
       "outBr315": outBr315,
       "outStream316": outStream316,
       "outBr316": outBr316,
       "outStream317": outStream317,
       "outBr317": outBr317,
       "outStream318": outStream318,
       "outBr318": outBr318,
       "outStream319": outStream319,
       "outBr319": outBr319,
       "outStream320": outStream320,
       "outBr320": outBr320,
       "outStream321": outStream321,
       "outBr321": outBr321,
       "outStream322": outStream322,
       "outBr322": outBr322,
       "outStream323": outStream323,
       "outBr323": outBr323,
       "outStream324": outStream324,
       "outBr324": outBr324,
       "outStream325": outStream325,
       "outBr325": outBr325,
       "outStream326": outStream326,
       "outBr326": outBr326,
       "outStream327": outStream327,
       "outBr327": outBr327,
       "outStream328": outStream328,
       "outBr328": outBr328,
       "outStream329": outStream329,
       "outBr329": outBr329,
       "outStream330": outStream330,
       "outBr330": outBr330,
       "outStream331": outStream331,
       "outBr331": outBr331,
       "outStream332": outStream332,
       "outBr332": outBr332,
       "outStream333": outStream333,
       "outBr333": outBr333,
       "outStream334": outStream334,
       "outBr334": outBr334,
       "outStream335": outStream335,
       "outBr335": outBr335,
       "outStream336": outStream336,
       "outBr336": outBr336,
       "outStream337": outStream337,
       "outBr337": outBr337,
       "outStream338": outStream338,
       "outBr338": outBr338,
       "outStream339": outStream339,
       "outBr339": outBr339,
       "outStream340": outStream340,
       "outBr340": outBr340,
       "outStream341": outStream341,
       "outBr341": outBr341,
       "outStream342": outStream342,
       "outBr342": outBr342,
       "outStream343": outStream343,
       "outBr343": outBr343,
       "outStream344": outStream344,
       "outBr344": outBr344,
       "outStream345": outStream345,
       "outBr345": outBr345,
       "outStream346": outStream346,
       "outBr346": outBr346,
       "outStream347": outStream347,
       "outBr347": outBr347,
       "outStream348": outStream348,
       "outBr348": outBr348,
       "outStream349": outStream349,
       "outBr349": outBr349,
       "outStream350": outStream350,
       "outBr350": outBr350,
       "outStream351": outStream351,
       "outBr351": outBr351,
       "outStream352": outStream352,
       "outBr352": outBr352,
       "outStream353": outStream353,
       "outBr353": outBr353,
       "outStream354": outStream354,
       "outBr354": outBr354,
       "outStream355": outStream355,
       "outBr355": outBr355,
       "outStream356": outStream356,
       "outBr356": outBr356,
       "outStream357": outStream357,
       "outBr357": outBr357,
       "outStream358": outStream358,
       "outBr358": outBr358,
       "outStream359": outStream359,
       "outBr359": outBr359,
       "outStream360": outStream360,
       "outBr360": outBr360,
       "outStream361": outStream361,
       "outBr361": outBr361,
       "outStream362": outStream362,
       "outBr362": outBr362,
       "outStream363": outStream363,
       "outBr363": outBr363,
       "outStream364": outStream364,
       "outBr364": outBr364,
       "outStream365": outStream365,
       "outBr365": outBr365,
       "outStream366": outStream366,
       "outBr366": outBr366,
       "outStream367": outStream367,
       "outBr367": outBr367,
       "outStream368": outStream368,
       "outBr368": outBr368,
       "outStream369": outStream369,
       "outBr369": outBr369,
       "outStream370": outStream370,
       "outBr370": outBr370,
       "outStream371": outStream371,
       "outBr371": outBr371,
       "outStream372": outStream372,
       "outBr372": outBr372,
       "outStream373": outStream373,
       "outBr373": outBr373,
       "outStream374": outStream374,
       "outBr374": outBr374,
       "outStream375": outStream375,
       "outBr375": outBr375,
       "outStream376": outStream376,
       "outBr376": outBr376,
       "outStream377": outStream377,
       "outBr377": outBr377,
       "outStream378": outStream378,
       "outBr378": outBr378,
       "outStream379": outStream379,
       "outBr379": outBr379,
       "outStream380": outStream380,
       "outBr380": outBr380,
       "outStream381": outStream381,
       "outBr381": outBr381,
       "outStream382": outStream382,
       "outBr382": outBr382,
       "outStream383": outStream383,
       "outBr383": outBr383,
       "outStream384": outStream384,
       "outBr384": outBr384,
       "outStream385": outStream385,
       "outBr385": outBr385,
       "outStream386": outStream386,
       "outBr386": outBr386,
       "outStream387": outStream387,
       "outBr387": outBr387,
       "outStream388": outStream388,
       "outBr388": outBr388,
       "outStream389": outStream389,
       "outBr389": outBr389,
       "outStream390": outStream390,
       "outBr390": outBr390,
       "outStream391": outStream391,
       "outBr391": outBr391,
       "outStream392": outStream392,
       "outBr392": outBr392,
       "outStream393": outStream393,
       "outBr393": outBr393,
       "outStream394": outStream394,
       "outBr394": outBr394,
       "outStream395": outStream395,
       "outBr395": outBr395,
       "outStream396": outStream396,
       "outBr396": outBr396,
       "outStream397": outStream397,
       "outBr397": outBr397,
       "outStream398": outStream398,
       "outBr398": outBr398,
       "outStream399": outStream399,
       "outBr399": outBr399,
       "outStream400": outStream400,
       "outBr400": outBr400,
       "outStream401": outStream401,
       "outBr401": outBr401,
       "outStream402": outStream402,
       "outBr402": outBr402,
       "outStream403": outStream403,
       "outBr403": outBr403,
       "outStream404": outStream404,
       "outBr404": outBr404,
       "outStream405": outStream405,
       "outBr405": outBr405,
       "outStream406": outStream406,
       "outBr406": outBr406,
       "outStream407": outStream407,
       "outBr407": outBr407,
       "outStream408": outStream408,
       "outBr408": outBr408,
       "outStream409": outStream409,
       "outBr409": outBr409,
       "outStream410": outStream410,
       "outBr410": outBr410,
       "outStream411": outStream411,
       "outBr411": outBr411,
       "outStream412": outStream412,
       "outBr412": outBr412,
       "outStream413": outStream413,
       "outBr413": outBr413,
       "outStream414": outStream414,
       "outBr414": outBr414,
       "outStream415": outStream415,
       "outBr415": outBr415,
       "outStream416": outStream416,
       "outBr416": outBr416,
       "outStream417": outStream417,
       "outBr417": outBr417,
       "outStream418": outStream418,
       "outBr418": outBr418,
       "outStream419": outStream419,
       "outBr419": outBr419,
       "outStream420": outStream420,
       "outBr420": outBr420,
       "outStream421": outStream421,
       "outBr421": outBr421,
       "outStream422": outStream422,
       "outBr422": outBr422,
       "outStream423": outStream423,
       "outBr423": outBr423,
       "outStream424": outStream424,
       "outBr424": outBr424,
       "outStream425": outStream425,
       "outBr425": outBr425,
       "outStream426": outStream426,
       "outBr426": outBr426,
       "outStream427": outStream427,
       "outBr427": outBr427,
       "outStream428": outStream428,
       "outBr428": outBr428,
       "outStream429": outStream429,
       "outBr429": outBr429,
       "outStream430": outStream430,
       "outBr430": outBr430,
       "outStream431": outStream431,
       "outBr431": outBr431,
       "outStream432": outStream432,
       "outBr432": outBr432,
       "outStream433": outStream433,
       "outBr433": outBr433,
       "outStream434": outStream434,
       "outBr434": outBr434,
       "outStream435": outStream435,
       "outBr435": outBr435,
       "outStream436": outStream436,
       "outBr436": outBr436,
       "outStream437": outStream437,
       "outBr437": outBr437,
       "outStream438": outStream438,
       "outBr438": outBr438,
       "outStream439": outStream439,
       "outBr439": outBr439,
       "outStream440": outStream440,
       "outBr440": outBr440,
       "outStream441": outStream441,
       "outBr441": outBr441,
       "outStream442": outStream442,
       "outBr442": outBr442,
       "outStream443": outStream443,
       "outBr443": outBr443,
       "outStream444": outStream444,
       "outBr444": outBr444,
       "outStream445": outStream445,
       "outBr445": outBr445,
       "outStream446": outStream446,
       "outBr446": outBr446,
       "outStream447": outStream447,
       "outBr447": outBr447,
       "outStream448": outStream448,
       "outBr448": outBr448,
       "outStream449": outStream449,
       "outBr449": outBr449,
       "outStream450": outStream450,
       "outBr450": outBr450,
       "outStream451": outStream451,
       "outBr451": outBr451,
       "outStream452": outStream452,
       "outBr452": outBr452,
       "outStream453": outStream453,
       "outBr453": outBr453,
       "outStream454": outStream454,
       "outBr454": outBr454,
       "outStream455": outStream455,
       "outBr455": outBr455,
       "outStream456": outStream456,
       "outBr456": outBr456,
       "outStream457": outStream457,
       "outBr457": outBr457,
       "outStream458": outStream458,
       "outBr458": outBr458,
       "outStream459": outStream459,
       "outBr459": outBr459,
       "outStream460": outStream460,
       "outBr460": outBr460,
       "outStream461": outStream461,
       "outBr461": outBr461,
       "outStream462": outStream462,
       "outBr462": outBr462,
       "outStream463": outStream463,
       "outBr463": outBr463,
       "outStream464": outStream464,
       "outBr464": outBr464,
       "outStream465": outStream465,
       "outBr465": outBr465,
       "outStream466": outStream466,
       "outBr466": outBr466,
       "outStream467": outStream467,
       "outBr467": outBr467,
       "outStream468": outStream468,
       "outBr468": outBr468,
       "outStream469": outStream469,
       "outBr469": outBr469,
       "outStream470": outStream470,
       "outBr470": outBr470,
       "outStream471": outStream471,
       "outBr471": outBr471,
       "outStream472": outStream472,
       "outBr472": outBr472,
       "outStream473": outStream473,
       "outBr473": outBr473,
       "outStream474": outStream474,
       "outBr474": outBr474,
       "outStream475": outStream475,
       "outBr475": outBr475,
       "outStream476": outStream476,
       "outBr476": outBr476,
       "outStream477": outStream477,
       "outBr477": outBr477,
       "outStream478": outStream478,
       "outBr478": outBr478,
       "outStream479": outStream479,
       "outBr479": outBr479,
       "outStream480": outStream480,
       "outBr480": outBr480,
       "outStream481": outStream481,
       "outBr481": outBr481,
       "outStream482": outStream482,
       "outBr482": outBr482,
       "outStream483": outStream483,
       "outBr483": outBr483,
       "outStream484": outStream484,
       "outBr484": outBr484,
       "outStream485": outStream485,
       "outBr485": outBr485,
       "outStream486": outStream486,
       "outBr486": outBr486,
       "outStream487": outStream487,
       "outBr487": outBr487,
       "outStream488": outStream488,
       "outBr488": outBr488,
       "outStream489": outStream489,
       "outBr489": outBr489,
       "outStream490": outStream490,
       "outBr490": outBr490,
       "outStream491": outStream491,
       "outBr491": outBr491,
       "outStream492": outStream492,
       "outBr492": outBr492,
       "outStream493": outStream493,
       "outBr493": outBr493,
       "outStream494": outStream494,
       "outBr494": outBr494,
       "outStream495": outStream495,
       "outBr495": outBr495,
       "outStream496": outStream496,
       "outBr496": outBr496,
       "outStream497": outStream497,
       "outBr497": outBr497,
       "outStream498": outStream498,
       "outBr498": outBr498,
       "outStream499": outStream499,
       "outBr499": outBr499,
       "outStream500": outStream500,
       "outBr500": outBr500,
       "outStream501": outStream501,
       "outBr501": outBr501,
       "outStream502": outStream502,
       "outBr502": outBr502,
       "outStream503": outStream503,
       "outBr503": outBr503,
       "outStream504": outStream504,
       "outBr504": outBr504,
       "outStream505": outStream505,
       "outBr505": outBr505,
       "outStream506": outStream506,
       "outBr506": outBr506,
       "outStream507": outStream507,
       "outBr507": outBr507,
       "outStream508": outStream508,
       "outBr508": outBr508,
       "outStream509": outStream509,
       "outBr509": outBr509,
       "outStream510": outStream510,
       "outBr510": outBr510,
       "outStream511": outStream511,
       "outBr511": outBr511,
       "outStream512": outStream512,
       "outBr512": outBr512,
       "outStream513": outStream513,
       "outBr513": outBr513,
       "outStream514": outStream514,
       "outBr514": outBr514,
       "outStream515": outStream515,
       "outBr515": outBr515,
       "outStream516": outStream516,
       "outBr516": outBr516,
       "outStream517": outStream517,
       "outBr517": outBr517,
       "outStream518": outStream518,
       "outBr518": outBr518,
       "outStream519": outStream519,
       "outBr519": outBr519,
       "outStream520": outStream520,
       "outBr520": outBr520,
       "outStream521": outStream521,
       "outBr521": outBr521,
       "outStream522": outStream522,
       "outBr522": outBr522,
       "outStream523": outStream523,
       "outBr523": outBr523,
       "outStream524": outStream524,
       "outBr524": outBr524,
       "outStream525": outStream525,
       "outBr525": outBr525,
       "outStream526": outStream526,
       "outBr526": outBr526,
       "outStream527": outStream527,
       "outBr527": outBr527,
       "outStream528": outStream528,
       "outBr528": outBr528,
       "outStream529": outStream529,
       "outBr529": outBr529,
       "outStream530": outStream530,
       "outBr530": outBr530,
       "outStream531": outStream531,
       "outBr531": outBr531,
       "outStream532": outStream532,
       "outBr532": outBr532,
       "outStream533": outStream533,
       "outBr533": outBr533,
       "outStream534": outStream534,
       "outBr534": outBr534,
       "outStream535": outStream535,
       "outBr535": outBr535,
       "outStream536": outStream536,
       "outBr536": outBr536,
       "outStream537": outStream537,
       "outBr537": outBr537,
       "outStream538": outStream538,
       "outBr538": outBr538,
       "outStream539": outStream539,
       "outBr539": outBr539,
       "outStream540": outStream540,
       "outBr540": outBr540,
       "outStream541": outStream541,
       "outBr541": outBr541,
       "outStream542": outStream542,
       "outBr542": outBr542,
       "outStream543": outStream543,
       "outBr543": outBr543,
       "outStream544": outStream544,
       "outBr544": outBr544,
       "outStream545": outStream545,
       "outBr545": outBr545,
       "outStream546": outStream546,
       "outBr546": outBr546,
       "outStream547": outStream547,
       "outBr547": outBr547,
       "outStream548": outStream548,
       "outBr548": outBr548,
       "outStream549": outStream549,
       "outBr549": outBr549,
       "outStream550": outStream550,
       "outBr550": outBr550,
       "outStream551": outStream551,
       "outBr551": outBr551,
       "outStream552": outStream552,
       "outBr552": outBr552,
       "outStream553": outStream553,
       "outBr553": outBr553,
       "outStream554": outStream554,
       "outBr554": outBr554,
       "outStream555": outStream555,
       "outBr555": outBr555,
       "outStream556": outStream556,
       "outBr556": outBr556,
       "outStream557": outStream557,
       "outBr557": outBr557,
       "outStream558": outStream558,
       "outBr558": outBr558,
       "outStream559": outStream559,
       "outBr559": outBr559,
       "outStream560": outStream560,
       "outBr560": outBr560,
       "outStream561": outStream561,
       "outBr561": outBr561,
       "outStream562": outStream562,
       "outBr562": outBr562,
       "outStream563": outStream563,
       "outBr563": outBr563,
       "outStream564": outStream564,
       "outBr564": outBr564,
       "outStream565": outStream565,
       "outBr565": outBr565,
       "outStream566": outStream566,
       "outBr566": outBr566,
       "outStream567": outStream567,
       "outBr567": outBr567,
       "outStream568": outStream568,
       "outBr568": outBr568,
       "outStream569": outStream569,
       "outBr569": outBr569,
       "outStream570": outStream570,
       "outBr570": outBr570,
       "outStream571": outStream571,
       "outBr571": outBr571,
       "outStream572": outStream572,
       "outBr572": outBr572,
       "outStream573": outStream573,
       "outBr573": outBr573,
       "outStream574": outStream574,
       "outBr574": outBr574,
       "outStream575": outStream575,
       "outBr575": outBr575,
       "outStream576": outStream576,
       "outBr576": outBr576,
       "commStatus": commStatus,
       "inTotbr": inTotbr,
       "outTotbr": outTotbr,
       "cpuLoad": cpuLoad,
       "intTemp": intTemp,
       "demodTemp": demodTemp,
       "volt": volt,
       "sdi480alarms": sdi480alarms,
       "alarmLnb1": alarmLnb1,
       "alarmLnb2": alarmLnb2,
       "alarmLnb3": alarmLnb3,
       "alarmLnb4": alarmLnb4,
       "alarmStlink": alarmStlink,
       "alarmCtrlink": alarmCtrlink,
       "alarmBrovf": alarmBrovf,
       "alarmUnlock1": alarmUnlock1,
       "alarmUnlock2": alarmUnlock2,
       "alarmUnlock3": alarmUnlock3,
       "alarmUnlock4": alarmUnlock4,
       "alarmUnlock5": alarmUnlock5,
       "alarmUnlock6": alarmUnlock6,
       "alarmUnlock7": alarmUnlock7,
       "alarmUnlock8": alarmUnlock8,
       "alarmUnlock9": alarmUnlock9,
       "alarmPowerr": alarmPowerr,
       "alarmTemperr": alarmTemperr,
       "alarmIbrer": alarmIbrer,
       "sdi480notifications": sdi480notifications,
       "notifyLnb1": notifyLnb1,
       "notifyLnb2": notifyLnb2,
       "notifyLnb3": notifyLnb3,
       "notifyLnb4": notifyLnb4,
       "notifyStlink": notifyStlink,
       "notifyCtrlink": notifyCtrlink,
       "notifyBrovf": notifyBrovf,
       "notifyUnlock1": notifyUnlock1,
       "notifyUnlock2": notifyUnlock2,
       "notifyUnlock3": notifyUnlock3,
       "notifyUnlock4": notifyUnlock4,
       "notifyUnlock5": notifyUnlock5,
       "notifyUnlock6": notifyUnlock6,
       "notifyUnlock7": notifyUnlock7,
       "notifyUnlock8": notifyUnlock8,
       "notifyUnlock9": notifyUnlock9,
       "notifyPowerr": notifyPowerr,
       "notifyTemperr": notifyTemperr,
       "notifyIbrer": notifyIbrer,
       "sdi480Info": sdi480Info,
       "infVersion": infVersion,
       "infSerNum": infSerNum,
       "terrasdi480MIBConformance": terrasdi480MIBConformance,
       "terrasdi480MIBGroups": terrasdi480MIBGroups,
       "sdi480TerraMibAllObjects": sdi480TerraMibAllObjects,
       "sdi480TerraMibAllNotifications": sdi480TerraMibAllNotifications}
)
