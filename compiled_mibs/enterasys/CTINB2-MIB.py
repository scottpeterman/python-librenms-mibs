# SNMP MIB module (CTINB2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTINB2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:26 2025
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

(ctINBinfo2,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctINBinfo2")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtInbUtil_ObjectIdentity = ObjectIdentity
ctInbUtil = _CtInbUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1)
)


class _CtInbUtilInterval_Type(Integer32):
    """Custom type ctInbUtilInterval based on Integer32"""
    defaultValue = 1


_CtInbUtilInterval_Type.__name__ = "Integer32"
_CtInbUtilInterval_Object = MibScalar
ctInbUtilInterval = _CtInbUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 1),
    _CtInbUtilInterval_Type()
)
ctInbUtilInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctInbUtilInterval.setStatus("mandatory")
_CtInbUtilTable_Object = MibTable
ctInbUtilTable = _CtInbUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ctInbUtilTable.setStatus("mandatory")
_CtInbUtilEntry_Object = MibTableRow
ctInbUtilEntry = _CtInbUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1)
)
ctInbUtilEntry.setIndexNames(
    (0, "CTINB2-MIB", "ctInbUtilSrcSlot"),
    (0, "CTINB2-MIB", "ctInbUtilDestSlot"),
)
if mibBuilder.loadTexts:
    ctInbUtilEntry.setStatus("mandatory")
_CtInbUtilSrcSlot_Type = Integer32
_CtInbUtilSrcSlot_Object = MibTableColumn
ctInbUtilSrcSlot = _CtInbUtilSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 1),
    _CtInbUtilSrcSlot_Type()
)
ctInbUtilSrcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilSrcSlot.setStatus("mandatory")
_CtInbUtilDestSlot_Type = Integer32
_CtInbUtilDestSlot_Object = MibTableColumn
ctInbUtilDestSlot = _CtInbUtilDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 2),
    _CtInbUtilDestSlot_Type()
)
ctInbUtilDestSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilDestSlot.setStatus("mandatory")
_CtInbUtilHiByteCountA_Type = Integer32
_CtInbUtilHiByteCountA_Object = MibTableColumn
ctInbUtilHiByteCountA = _CtInbUtilHiByteCountA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 3),
    _CtInbUtilHiByteCountA_Type()
)
ctInbUtilHiByteCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilHiByteCountA.setStatus("mandatory")
_CtInbUtilLoByteCountA_Type = Integer32
_CtInbUtilLoByteCountA_Object = MibTableColumn
ctInbUtilLoByteCountA = _CtInbUtilLoByteCountA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 4),
    _CtInbUtilLoByteCountA_Type()
)
ctInbUtilLoByteCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilLoByteCountA.setStatus("mandatory")
_CtInbUtilHiByteCountB_Type = Integer32
_CtInbUtilHiByteCountB_Object = MibTableColumn
ctInbUtilHiByteCountB = _CtInbUtilHiByteCountB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 5),
    _CtInbUtilHiByteCountB_Type()
)
ctInbUtilHiByteCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilHiByteCountB.setStatus("mandatory")
_CtInbUtilLoByteCountB_Type = Integer32
_CtInbUtilLoByteCountB_Object = MibTableColumn
ctInbUtilLoByteCountB = _CtInbUtilLoByteCountB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 6),
    _CtInbUtilLoByteCountB_Type()
)
ctInbUtilLoByteCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilLoByteCountB.setStatus("mandatory")
_CtInbUtilAbsoluteA_Type = Integer32
_CtInbUtilAbsoluteA_Object = MibTableColumn
ctInbUtilAbsoluteA = _CtInbUtilAbsoluteA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 7),
    _CtInbUtilAbsoluteA_Type()
)
ctInbUtilAbsoluteA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilAbsoluteA.setStatus("mandatory")
_CtInbUtilAbsoluteB_Type = Integer32
_CtInbUtilAbsoluteB_Object = MibTableColumn
ctInbUtilAbsoluteB = _CtInbUtilAbsoluteB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 8),
    _CtInbUtilAbsoluteB_Type()
)
ctInbUtilAbsoluteB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilAbsoluteB.setStatus("mandatory")
_CtInbUtilAbsoluteTotal_Type = Integer32
_CtInbUtilAbsoluteTotal_Object = MibTableColumn
ctInbUtilAbsoluteTotal = _CtInbUtilAbsoluteTotal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 9),
    _CtInbUtilAbsoluteTotal_Type()
)
ctInbUtilAbsoluteTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctInbUtilAbsoluteTotal.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTINB2-MIB",
    **{"ctInbUtil": ctInbUtil,
       "ctInbUtilInterval": ctInbUtilInterval,
       "ctInbUtilTable": ctInbUtilTable,
       "ctInbUtilEntry": ctInbUtilEntry,
       "ctInbUtilSrcSlot": ctInbUtilSrcSlot,
       "ctInbUtilDestSlot": ctInbUtilDestSlot,
       "ctInbUtilHiByteCountA": ctInbUtilHiByteCountA,
       "ctInbUtilLoByteCountA": ctInbUtilLoByteCountA,
       "ctInbUtilHiByteCountB": ctInbUtilHiByteCountB,
       "ctInbUtilLoByteCountB": ctInbUtilLoByteCountB,
       "ctInbUtilAbsoluteA": ctInbUtilAbsoluteA,
       "ctInbUtilAbsoluteB": ctInbUtilAbsoluteB,
       "ctInbUtilAbsoluteTotal": ctInbUtilAbsoluteTotal}
)
