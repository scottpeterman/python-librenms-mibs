# SNMP MIB module (CONEL-XCCNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\icr-os\CONEL-XCCNT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:21 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 2)
)
_Xccnt_ObjectIdentity = ObjectIdentity
xccnt = _Xccnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1)
)
_XccntAn1_Type = Integer32
_XccntAn1_Object = MibScalar
xccntAn1 = _XccntAn1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 1),
    _XccntAn1_Type()
)
xccntAn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntAn1.setStatus("current")
_XccntAn2_Type = Integer32
_XccntAn2_Object = MibScalar
xccntAn2 = _XccntAn2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 2),
    _XccntAn2_Type()
)
xccntAn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntAn2.setStatus("current")
_XccntCnt1_Type = Counter32
_XccntCnt1_Object = MibScalar
xccntCnt1 = _XccntCnt1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 3),
    _XccntCnt1_Type()
)
xccntCnt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntCnt1.setStatus("current")
_XccntCnt2_Type = Counter32
_XccntCnt2_Object = MibScalar
xccntCnt2 = _XccntCnt2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 4),
    _XccntCnt2_Type()
)
xccntCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntCnt2.setStatus("current")
_XccntBin1_Type = Gauge32
_XccntBin1_Object = MibScalar
xccntBin1 = _XccntBin1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 5),
    _XccntBin1_Type()
)
xccntBin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin1.setStatus("current")
_XccntBin2_Type = Gauge32
_XccntBin2_Object = MibScalar
xccntBin2 = _XccntBin2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 6),
    _XccntBin2_Type()
)
xccntBin2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin2.setStatus("current")
_XccntBin3_Type = Gauge32
_XccntBin3_Object = MibScalar
xccntBin3 = _XccntBin3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 7),
    _XccntBin3_Type()
)
xccntBin3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin3.setStatus("current")
_XccntBin4_Type = Gauge32
_XccntBin4_Object = MibScalar
xccntBin4 = _XccntBin4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 8),
    _XccntBin4_Type()
)
xccntBin4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin4.setStatus("current")
_XccntOut1_Type = Gauge32
_XccntOut1_Object = MibScalar
xccntOut1 = _XccntOut1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 9),
    _XccntOut1_Type()
)
xccntOut1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xccntOut1.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-XCCNT-MIB",
    **{"conel": conel,
       "protocols": protocols,
       "xccnt": xccnt,
       "xccntAn1": xccntAn1,
       "xccntAn2": xccntAn2,
       "xccntCnt1": xccntCnt1,
       "xccntCnt2": xccntCnt2,
       "xccntBin1": xccntBin1,
       "xccntBin2": xccntBin2,
       "xccntBin3": xccntBin3,
       "xccntBin4": xccntBin4,
       "xccntOut1": xccntOut1}
)
