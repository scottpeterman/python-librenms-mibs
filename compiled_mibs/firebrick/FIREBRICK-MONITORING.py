# SNMP MIB module (FIREBRICK-MONITORING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\firebrick\FIREBRICK-MONITORING
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:38 2025
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

(firebrickNewStyle,) = mibBuilder.importSymbols(
    "FIREBRICK-MIB",
    "firebrickNewStyle")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fbMonitoringMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1)
)
if mibBuilder.loadTexts:
    fbMonitoringMib.setRevisions(
        ("2020-06-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbMonReadingTable_Object = MibTable
fbMonReadingTable = _FbMonReadingTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1, 1)
)
if mibBuilder.loadTexts:
    fbMonReadingTable.setStatus("current")
_FbMonReadingEntry_Object = MibTableRow
fbMonReadingEntry = _FbMonReadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1)
)
fbMonReadingEntry.setIndexNames(
    (0, "FIREBRICK-MONITORING", "fbMonReadingIndex"),
)
if mibBuilder.loadTexts:
    fbMonReadingEntry.setStatus("current")
_FbMonReadingIndex_Type = Integer32
_FbMonReadingIndex_Object = MibTableColumn
fbMonReadingIndex = _FbMonReadingIndex_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 1),
    _FbMonReadingIndex_Type()
)
fbMonReadingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbMonReadingIndex.setStatus("current")
_FbMonReadingType_Type = DisplayString
_FbMonReadingType_Object = MibTableColumn
fbMonReadingType = _FbMonReadingType_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 2),
    _FbMonReadingType_Type()
)
fbMonReadingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbMonReadingType.setStatus("current")
_FbMonReadingName_Type = DisplayString
_FbMonReadingName_Object = MibTableColumn
fbMonReadingName = _FbMonReadingName_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 3),
    _FbMonReadingName_Type()
)
fbMonReadingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbMonReadingName.setStatus("current")
_FbMonReadingValue_Type = Integer32
_FbMonReadingValue_Object = MibTableColumn
fbMonReadingValue = _FbMonReadingValue_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 4),
    _FbMonReadingValue_Type()
)
fbMonReadingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbMonReadingValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-MONITORING",
    **{"fbMonitoringMib": fbMonitoringMib,
       "fbMonReadingTable": fbMonReadingTable,
       "fbMonReadingEntry": fbMonReadingEntry,
       "fbMonReadingIndex": fbMonReadingIndex,
       "fbMonReadingType": fbMonReadingType,
       "fbMonReadingName": fbMonReadingName,
       "fbMonReadingValue": fbMonReadingValue}
)
