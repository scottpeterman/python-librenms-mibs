# SNMP MIB module (MSERIES-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\MSERIES-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:31 2025
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

(mseries,) = mibBuilder.importSymbols(
    "MSERIES-MIB",
    "mseries")

(PortMode,
 PortStatus,
 PortType) = mibBuilder.importSymbols(
    "MSERIES-TC",
    "PortMode",
    "PortStatus",
    "PortType")

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


# MODULE-IDENTITY

smartPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3)
)
if mibBuilder.loadTexts:
    smartPort.setRevisions(
        ("2014-02-12 13:44",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmartPortObjects_ObjectIdentity = ObjectIdentity
smartPortObjects = _SmartPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1)
)
_SmartPortGeneral_ObjectIdentity = ObjectIdentity
smartPortGeneral = _SmartPortGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 1)
)
_SmartPortList_ObjectIdentity = ObjectIdentity
smartPortList = _SmartPortList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2)
)
_SmartPortTable_Object = MibTable
smartPortTable = _SmartPortTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    smartPortTable.setStatus("current")
_SmartPortEntry_Object = MibTableRow
smartPortEntry = _SmartPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1)
)
smartPortEntry.setIndexNames(
    (0, "MSERIES-PORT-MIB", "smartPortIndex"),
)
if mibBuilder.loadTexts:
    smartPortEntry.setStatus("current")


class _SmartPortIndex_Type(Unsigned32):
    """Custom type smartPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmartPortIndex_Type.__name__ = "Unsigned32"
_SmartPortIndex_Object = MibTableColumn
smartPortIndex = _SmartPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 1),
    _SmartPortIndex_Type()
)
smartPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartPortIndex.setStatus("current")
_SmartPortName_Type = DisplayString
_SmartPortName_Object = MibTableColumn
smartPortName = _SmartPortName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 2),
    _SmartPortName_Type()
)
smartPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartPortName.setStatus("current")
_SmartPortAlias_Type = DisplayString
_SmartPortAlias_Object = MibTableColumn
smartPortAlias = _SmartPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 3),
    _SmartPortAlias_Type()
)
smartPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartPortAlias.setStatus("current")
_SmartPortType_Type = PortType
_SmartPortType_Object = MibTableColumn
smartPortType = _SmartPortType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 4),
    _SmartPortType_Type()
)
smartPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartPortType.setStatus("current")
_SmartPortPower_Type = Integer32
_SmartPortPower_Object = MibTableColumn
smartPortPower = _SmartPortPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 5),
    _SmartPortPower_Type()
)
smartPortPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartPortPower.setStatus("current")
_SmartPortStatus_Type = PortStatus
_SmartPortStatus_Object = MibTableColumn
smartPortStatus = _SmartPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 6),
    _SmartPortStatus_Type()
)
smartPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartPortStatus.setStatus("current")
_SmartPortMode_Type = PortMode
_SmartPortMode_Object = MibTableColumn
smartPortMode = _SmartPortMode_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 7),
    _SmartPortMode_Type()
)
smartPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartPortMode.setStatus("current")
_SmartPortHighPowerAlarmThreshold_Type = Integer32
_SmartPortHighPowerAlarmThreshold_Object = MibTableColumn
smartPortHighPowerAlarmThreshold = _SmartPortHighPowerAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 8),
    _SmartPortHighPowerAlarmThreshold_Type()
)
smartPortHighPowerAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartPortHighPowerAlarmThreshold.setStatus("current")
_SmartPortLowPowerAlarmThreshold_Type = Integer32
_SmartPortLowPowerAlarmThreshold_Object = MibTableColumn
smartPortLowPowerAlarmThreshold = _SmartPortLowPowerAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 1, 2, 1, 1, 9),
    _SmartPortLowPowerAlarmThreshold_Type()
)
smartPortLowPowerAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartPortLowPowerAlarmThreshold.setStatus("current")
_SmartPortMIBConformance_ObjectIdentity = ObjectIdentity
smartPortMIBConformance = _SmartPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 2)
)
_SmartPortGroups_ObjectIdentity = ObjectIdentity
smartPortGroups = _SmartPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 1)
)
_SmartPortCompliances_ObjectIdentity = ObjectIdentity
smartPortCompliances = _SmartPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 2)
)

# Managed Objects groups

smartPortListGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 1, 1)
)
smartPortListGroupV1.setObjects(
      *(("MSERIES-PORT-MIB", "smartPortIndex"),
        ("MSERIES-PORT-MIB", "smartPortName"),
        ("MSERIES-PORT-MIB", "smartPortAlias"),
        ("MSERIES-PORT-MIB", "smartPortType"),
        ("MSERIES-PORT-MIB", "smartPortPower"),
        ("MSERIES-PORT-MIB", "smartPortStatus"),
        ("MSERIES-PORT-MIB", "smartPortMode"),
        ("MSERIES-PORT-MIB", "smartPortHighPowerAlarmThreshold"),
        ("MSERIES-PORT-MIB", "smartPortLowPowerAlarmThreshold"))
)
if mibBuilder.loadTexts:
    smartPortListGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

smartPortBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 1, 3, 2, 2, 1)
)
smartPortBasicComplV1.setObjects(
    ("MSERIES-PORT-MIB", "smartPortListGroupV1")
)
if mibBuilder.loadTexts:
    smartPortBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSERIES-PORT-MIB",
    **{"smartPort": smartPort,
       "smartPortObjects": smartPortObjects,
       "smartPortGeneral": smartPortGeneral,
       "smartPortList": smartPortList,
       "smartPortTable": smartPortTable,
       "smartPortEntry": smartPortEntry,
       "smartPortIndex": smartPortIndex,
       "smartPortName": smartPortName,
       "smartPortAlias": smartPortAlias,
       "smartPortType": smartPortType,
       "smartPortPower": smartPortPower,
       "smartPortStatus": smartPortStatus,
       "smartPortMode": smartPortMode,
       "smartPortHighPowerAlarmThreshold": smartPortHighPowerAlarmThreshold,
       "smartPortLowPowerAlarmThreshold": smartPortLowPowerAlarmThreshold,
       "smartPortMIBConformance": smartPortMIBConformance,
       "smartPortGroups": smartPortGroups,
       "smartPortListGroupV1": smartPortListGroupV1,
       "smartPortCompliances": smartPortCompliances,
       "smartPortBasicComplV1": smartPortBasicComplV1}
)
