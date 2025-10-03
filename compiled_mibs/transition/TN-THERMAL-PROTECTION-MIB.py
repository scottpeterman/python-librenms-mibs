# SNMP MIB module (TN-THERMAL-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-THERMAL-PROTECTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:32 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnThermalProtectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32)
)
if mibBuilder.loadTexts:
    tnThermalProtectionMIB.setRevisions(
        ("2012-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnThermalProtectionMIBNotifications_ObjectIdentity = ObjectIdentity
tnThermalProtectionMIBNotifications = _TnThermalProtectionMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 0)
)
_TnThermalProtectionMIBObjects_ObjectIdentity = ObjectIdentity
tnThermalProtectionMIBObjects = _TnThermalProtectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1)
)
_TnThermalProtectionMgmt_ObjectIdentity = ObjectIdentity
tnThermalProtectionMgmt = _TnThermalProtectionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1)
)
_TnThermalProtectionPriorityTable_Object = MibTable
tnThermalProtectionPriorityTable = _TnThermalProtectionPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnThermalProtectionPriorityTable.setStatus("current")
_TnThermalProtectionPriorityEntry_Object = MibTableRow
tnThermalProtectionPriorityEntry = _TnThermalProtectionPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 1, 1)
)
tnThermalProtectionPriorityEntry.setIndexNames(
    (0, "TN-THERMAL-PROTECTION-MIB", "tnThermalProtectionPriorityIndex"),
)
if mibBuilder.loadTexts:
    tnThermalProtectionPriorityEntry.setStatus("current")


class _TnThermalProtectionPriorityIndex_Type(Integer32):
    """Custom type tnThermalProtectionPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnThermalProtectionPriorityIndex_Type.__name__ = "Integer32"
_TnThermalProtectionPriorityIndex_Object = MibTableColumn
tnThermalProtectionPriorityIndex = _TnThermalProtectionPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 1, 1, 1),
    _TnThermalProtectionPriorityIndex_Type()
)
tnThermalProtectionPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnThermalProtectionPriorityIndex.setStatus("current")


class _TnThermalProtectionPriorityTemperature_Type(Integer32):
    """Custom type tnThermalProtectionPriorityTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnThermalProtectionPriorityTemperature_Type.__name__ = "Integer32"
_TnThermalProtectionPriorityTemperature_Object = MibTableColumn
tnThermalProtectionPriorityTemperature = _TnThermalProtectionPriorityTemperature_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 1, 1, 2),
    _TnThermalProtectionPriorityTemperature_Type()
)
tnThermalProtectionPriorityTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnThermalProtectionPriorityTemperature.setStatus("current")
_TnThermalProtectionIfTable_Object = MibTable
tnThermalProtectionIfTable = _TnThermalProtectionIfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnThermalProtectionIfTable.setStatus("current")
_TnThermalProtectionIfEntry_Object = MibTableRow
tnThermalProtectionIfEntry = _TnThermalProtectionIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 2, 1)
)
tnThermalProtectionIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnThermalProtectionIfEntry.setStatus("current")


class _TnThermalProtectionIfPriority_Type(Integer32):
    """Custom type tnThermalProtectionIfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnThermalProtectionIfPriority_Type.__name__ = "Integer32"
_TnThermalProtectionIfPriority_Object = MibTableColumn
tnThermalProtectionIfPriority = _TnThermalProtectionIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 2, 1, 1),
    _TnThermalProtectionIfPriority_Type()
)
tnThermalProtectionIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnThermalProtectionIfPriority.setStatus("current")
_TnThermalProtectionIfStatusTable_Object = MibTable
tnThermalProtectionIfStatusTable = _TnThermalProtectionIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnThermalProtectionIfStatusTable.setStatus("current")
_TnThermalProtectionIfStatusEntry_Object = MibTableRow
tnThermalProtectionIfStatusEntry = _TnThermalProtectionIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 3, 1)
)
tnThermalProtectionIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnThermalProtectionIfStatusEntry.setStatus("current")
_TnThermalProtectionIfStatusTemperature_Type = Integer32
_TnThermalProtectionIfStatusTemperature_Object = MibTableColumn
tnThermalProtectionIfStatusTemperature = _TnThermalProtectionIfStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 3, 1, 1),
    _TnThermalProtectionIfStatusTemperature_Type()
)
tnThermalProtectionIfStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnThermalProtectionIfStatusTemperature.setStatus("current")


class _TnThermalProtectionIfStatusCode_Type(Integer32):
    """Custom type tnThermalProtectionIfStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("linkdown", 1))
    )


_TnThermalProtectionIfStatusCode_Type.__name__ = "Integer32"
_TnThermalProtectionIfStatusCode_Object = MibTableColumn
tnThermalProtectionIfStatusCode = _TnThermalProtectionIfStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 1, 1, 3, 1, 2),
    _TnThermalProtectionIfStatusCode_Type()
)
tnThermalProtectionIfStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnThermalProtectionIfStatusCode.setStatus("current")

# Managed Objects groups


# Notification objects

tnThermalProtectionPortStatusChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 32, 0, 1)
)
tnThermalProtectionPortStatusChangedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-THERMAL-PROTECTION-MIB", "tnThermalProtectionPriorityTemperature"),
        ("TN-THERMAL-PROTECTION-MIB", "tnThermalProtectionIfStatusTemperature"),
        ("TN-THERMAL-PROTECTION-MIB", "tnThermalProtectionIfStatusCode"))
)
if mibBuilder.loadTexts:
    tnThermalProtectionPortStatusChangedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-THERMAL-PROTECTION-MIB",
    **{"tnThermalProtectionMIB": tnThermalProtectionMIB,
       "tnThermalProtectionMIBNotifications": tnThermalProtectionMIBNotifications,
       "tnThermalProtectionPortStatusChangedNotification": tnThermalProtectionPortStatusChangedNotification,
       "tnThermalProtectionMIBObjects": tnThermalProtectionMIBObjects,
       "tnThermalProtectionMgmt": tnThermalProtectionMgmt,
       "tnThermalProtectionPriorityTable": tnThermalProtectionPriorityTable,
       "tnThermalProtectionPriorityEntry": tnThermalProtectionPriorityEntry,
       "tnThermalProtectionPriorityIndex": tnThermalProtectionPriorityIndex,
       "tnThermalProtectionPriorityTemperature": tnThermalProtectionPriorityTemperature,
       "tnThermalProtectionIfTable": tnThermalProtectionIfTable,
       "tnThermalProtectionIfEntry": tnThermalProtectionIfEntry,
       "tnThermalProtectionIfPriority": tnThermalProtectionIfPriority,
       "tnThermalProtectionIfStatusTable": tnThermalProtectionIfStatusTable,
       "tnThermalProtectionIfStatusEntry": tnThermalProtectionIfStatusEntry,
       "tnThermalProtectionIfStatusTemperature": tnThermalProtectionIfStatusTemperature,
       "tnThermalProtectionIfStatusCode": tnThermalProtectionIfStatusCode}
)
