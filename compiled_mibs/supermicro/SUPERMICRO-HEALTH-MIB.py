# SNMP MIB module (SUPERMICRO-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\supermicro\SUPERMICRO-HEALTH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:22 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(smHealth,) = mibBuilder.importSymbols(
    "SUPERMICRO-SMI",
    "smHealth")


# MODULE-IDENTITY

smHealthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SMHealthInfoTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_SmHealthObjects_ObjectIdentity = ObjectIdentity
smHealthObjects = _SmHealthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1)
)
_SmHealthMonitorTable_Object = MibTable
smHealthMonitorTable = _SmHealthMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    smHealthMonitorTable.setStatus("current")
_SmHealthMonitorEntry_Object = MibTableRow
smHealthMonitorEntry = _SmHealthMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1)
)
smHealthMonitorEntry.setIndexNames(
    (0, "SUPERMICRO-HEALTH-MIB", "smHealthMonitorIndex"),
)
if mibBuilder.loadTexts:
    smHealthMonitorEntry.setStatus("current")


class _SmHealthMonitorIndex_Type(Integer32):
    """Custom type smHealthMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SmHealthMonitorIndex_Type.__name__ = "Integer32"
_SmHealthMonitorIndex_Object = MibTableColumn
smHealthMonitorIndex = _SmHealthMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 1),
    _SmHealthMonitorIndex_Type()
)
smHealthMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smHealthMonitorIndex.setStatus("current")
_SmHealthMonitorName_Type = DisplayString
_SmHealthMonitorName_Object = MibTableColumn
smHealthMonitorName = _SmHealthMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 2),
    _SmHealthMonitorName_Type()
)
smHealthMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthMonitorName.setStatus("current")
_SmHealthMonitorType_Type = SMHealthInfoTypes
_SmHealthMonitorType_Object = MibTableColumn
smHealthMonitorType = _SmHealthMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 3),
    _SmHealthMonitorType_Type()
)
smHealthMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthMonitorType.setStatus("current")


class _SmHealthMonitorReading_Type(Integer32):
    """Custom type smHealthMonitorReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmHealthMonitorReading_Type.__name__ = "Integer32"
_SmHealthMonitorReading_Object = MibTableColumn
smHealthMonitorReading = _SmHealthMonitorReading_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 4),
    _SmHealthMonitorReading_Type()
)
smHealthMonitorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthMonitorReading.setStatus("current")


class _SmHealthMonitorHighLimit_Type(Integer32):
    """Custom type smHealthMonitorHighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmHealthMonitorHighLimit_Type.__name__ = "Integer32"
_SmHealthMonitorHighLimit_Object = MibTableColumn
smHealthMonitorHighLimit = _SmHealthMonitorHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 5),
    _SmHealthMonitorHighLimit_Type()
)
smHealthMonitorHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smHealthMonitorHighLimit.setStatus("current")


class _SmHealthMonitorLowLimit_Type(Integer32):
    """Custom type smHealthMonitorLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmHealthMonitorLowLimit_Type.__name__ = "Integer32"
_SmHealthMonitorLowLimit_Object = MibTableColumn
smHealthMonitorLowLimit = _SmHealthMonitorLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 6),
    _SmHealthMonitorLowLimit_Type()
)
smHealthMonitorLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smHealthMonitorLowLimit.setStatus("current")


class _SmHealthMonitorMaxReading_Type(Integer32):
    """Custom type smHealthMonitorMaxReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmHealthMonitorMaxReading_Type.__name__ = "Integer32"
_SmHealthMonitorMaxReading_Object = MibTableColumn
smHealthMonitorMaxReading = _SmHealthMonitorMaxReading_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 7),
    _SmHealthMonitorMaxReading_Type()
)
smHealthMonitorMaxReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthMonitorMaxReading.setStatus("current")


class _SmHealthMonitorMinReading_Type(Integer32):
    """Custom type smHealthMonitorMinReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmHealthMonitorMinReading_Type.__name__ = "Integer32"
_SmHealthMonitorMinReading_Object = MibTableColumn
smHealthMonitorMinReading = _SmHealthMonitorMinReading_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 8),
    _SmHealthMonitorMinReading_Type()
)
smHealthMonitorMinReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthMonitorMinReading.setStatus("current")
_SmHealthMonitorDivisor_Type = Integer32
_SmHealthMonitorDivisor_Object = MibTableColumn
smHealthMonitorDivisor = _SmHealthMonitorDivisor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 9),
    _SmHealthMonitorDivisor_Type()
)
smHealthMonitorDivisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smHealthMonitorDivisor.setStatus("current")
_SmHealthMonitorMonitor_Type = TruthValue
_SmHealthMonitorMonitor_Object = MibTableColumn
smHealthMonitorMonitor = _SmHealthMonitorMonitor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 10),
    _SmHealthMonitorMonitor_Type()
)
smHealthMonitorMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smHealthMonitorMonitor.setStatus("current")
_SmHealthMonitorReadingUnit_Type = DisplayString
_SmHealthMonitorReadingUnit_Object = MibTableColumn
smHealthMonitorReadingUnit = _SmHealthMonitorReadingUnit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 11),
    _SmHealthMonitorReadingUnit_Type()
)
smHealthMonitorReadingUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthMonitorReadingUnit.setStatus("current")
_SmHealthMonitorStatus_Type = Integer32
_SmHealthMonitorStatus_Object = MibTableColumn
smHealthMonitorStatus = _SmHealthMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 1, 1, 1, 12),
    _SmHealthMonitorStatus_Type()
)
smHealthMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthMonitorStatus.setStatus("current")
_SmHealthNotifications_ObjectIdentity = ObjectIdentity
smHealthNotifications = _SmHealthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 2)
)
_SmHealthConformance_ObjectIdentity = ObjectIdentity
smHealthConformance = _SmHealthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 3)
)
_SmHealthCompliances_ObjectIdentity = ObjectIdentity
smHealthCompliances = _SmHealthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1)
)
_SmHealthGroups_ObjectIdentity = ObjectIdentity
smHealthGroups = _SmHealthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2)
)
_SmHealthAllinoneStatus_Type = Integer32
_SmHealthAllinoneStatus_Object = MibScalar
smHealthAllinoneStatus = _SmHealthAllinoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 2),
    _SmHealthAllinoneStatus_Type()
)
smHealthAllinoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthAllinoneStatus.setStatus("current")
_SmHealthAllinoneMsg_Type = DisplayString
_SmHealthAllinoneMsg_Object = MibScalar
smHealthAllinoneMsg = _SmHealthAllinoneMsg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 2, 3),
    _SmHealthAllinoneMsg_Type()
)
smHealthAllinoneMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHealthAllinoneMsg.setStatus("current")

# Managed Objects groups

smHealthMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 2, 1)
)
smHealthMonitorGroup.setObjects(
      *(("SUPERMICRO-HEALTH-MIB", "smHealthMonitorType"),
        ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorName"),
        ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorReading"),
        ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorHighLimit"),
        ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorLowLimit"),
        ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMaxReading"),
        ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMinReading"),
        ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorMonitor"))
)
if mibBuilder.loadTexts:
    smHealthMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

smHealthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10876, 2, 1, 3, 1, 1)
)
smHealthCompliance.setObjects(
    ("SUPERMICRO-HEALTH-MIB", "smHealthMonitorGroup")
)
if mibBuilder.loadTexts:
    smHealthCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-HEALTH-MIB",
    **{"SMHealthInfoTypes": SMHealthInfoTypes,
       "smHealthMIB": smHealthMIB,
       "smHealthObjects": smHealthObjects,
       "smHealthMonitorTable": smHealthMonitorTable,
       "smHealthMonitorEntry": smHealthMonitorEntry,
       "smHealthMonitorIndex": smHealthMonitorIndex,
       "smHealthMonitorName": smHealthMonitorName,
       "smHealthMonitorType": smHealthMonitorType,
       "smHealthMonitorReading": smHealthMonitorReading,
       "smHealthMonitorHighLimit": smHealthMonitorHighLimit,
       "smHealthMonitorLowLimit": smHealthMonitorLowLimit,
       "smHealthMonitorMaxReading": smHealthMonitorMaxReading,
       "smHealthMonitorMinReading": smHealthMonitorMinReading,
       "smHealthMonitorDivisor": smHealthMonitorDivisor,
       "smHealthMonitorMonitor": smHealthMonitorMonitor,
       "smHealthMonitorReadingUnit": smHealthMonitorReadingUnit,
       "smHealthMonitorStatus": smHealthMonitorStatus,
       "smHealthNotifications": smHealthNotifications,
       "smHealthConformance": smHealthConformance,
       "smHealthCompliances": smHealthCompliances,
       "smHealthCompliance": smHealthCompliance,
       "smHealthGroups": smHealthGroups,
       "smHealthMonitorGroup": smHealthMonitorGroup,
       "smHealthAllinoneStatus": smHealthAllinoneStatus,
       "smHealthAllinoneMsg": smHealthAllinoneMsg}
)
