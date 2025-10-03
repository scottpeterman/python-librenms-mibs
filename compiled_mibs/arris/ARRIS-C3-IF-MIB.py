# SNMP MIB module (ARRIS-C3-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-IF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:03 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

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

cmtsC3IfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxIfObjects_ObjectIdentity = ObjectIdentity
dcxIfObjects = _DcxIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1)
)
_DcxIfTable_Object = MibTable
dcxIfTable = _DcxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1)
)
if mibBuilder.loadTexts:
    dcxIfTable.setStatus("current")
_DcxIfEntry_Object = MibTableRow
dcxIfEntry = _DcxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcxIfEntry.setStatus("current")
_DcxIfLoadInterval_Type = Unsigned32
_DcxIfLoadInterval_Object = MibTableColumn
dcxIfLoadInterval = _DcxIfLoadInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 1),
    _DcxIfLoadInterval_Type()
)
dcxIfLoadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxIfLoadInterval.setStatus("current")
_DcxIfInputBitRate_Type = Unsigned32
_DcxIfInputBitRate_Object = MibTableColumn
dcxIfInputBitRate = _DcxIfInputBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 2),
    _DcxIfInputBitRate_Type()
)
dcxIfInputBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxIfInputBitRate.setStatus("current")
_DcxIfInputPacketRate_Type = Unsigned32
_DcxIfInputPacketRate_Object = MibTableColumn
dcxIfInputPacketRate = _DcxIfInputPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 3),
    _DcxIfInputPacketRate_Type()
)
dcxIfInputPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxIfInputPacketRate.setStatus("current")
_DcxIfOutputBitRate_Type = Unsigned32
_DcxIfOutputBitRate_Object = MibTableColumn
dcxIfOutputBitRate = _DcxIfOutputBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 4),
    _DcxIfOutputBitRate_Type()
)
dcxIfOutputBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxIfOutputBitRate.setStatus("current")
_DcxIfOutputPacketRate_Type = Unsigned32
_DcxIfOutputPacketRate_Object = MibTableColumn
dcxIfOutputPacketRate = _DcxIfOutputPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 5),
    _DcxIfOutputPacketRate_Type()
)
dcxIfOutputPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxIfOutputPacketRate.setStatus("current")
ifEntry.registerAugmentions(
    ("ARRIS-C3-IF-MIB",
     "dcxIfEntry")
)
dcxIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-IF-MIB",
    **{"cmtsC3IfMIB": cmtsC3IfMIB,
       "dcxIfObjects": dcxIfObjects,
       "dcxIfTable": dcxIfTable,
       "dcxIfEntry": dcxIfEntry,
       "dcxIfLoadInterval": dcxIfLoadInterval,
       "dcxIfInputBitRate": dcxIfInputBitRate,
       "dcxIfInputPacketRate": dcxIfInputPacketRate,
       "dcxIfOutputBitRate": dcxIfOutputBitRate,
       "dcxIfOutputPacketRate": dcxIfOutputPacketRate}
)
