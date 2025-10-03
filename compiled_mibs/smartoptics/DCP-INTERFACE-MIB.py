# SNMP MIB module (DCP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\DCP-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:21 2025
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

(dcpGeneric,) = mibBuilder.importSymbols(
    "DCP-MIB",
    "dcpGeneric")

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

(InterfacePortMode,
 InterfaceStatus,
 ItuPerceivedSeverity,
 OpticalPower1Decimal) = mibBuilder.importSymbols(
    "SO-TC-MIB",
    "InterfacePortMode",
    "InterfaceStatus",
    "ItuPerceivedSeverity",
    "OpticalPower1Decimal")


# MODULE-IDENTITY

dcpInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dcpInterface.setRevisions(
        ("2022-03-18 13:00",
         "2021-02-25 12:00",
         "2019-10-29 15:00",
         "2018-10-08 14:44")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcpInterfaceObjects_ObjectIdentity = ObjectIdentity
dcpInterfaceObjects = _DcpInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1)
)
_DcpInterfaceTable_Object = MibTable
dcpInterfaceTable = _DcpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcpInterfaceTable.setStatus("current")
_DcpInterfaceEntry_Object = MibTableRow
dcpInterfaceEntry = _DcpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1)
)
dcpInterfaceEntry.setIndexNames(
    (0, "DCP-INTERFACE-MIB", "dcpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    dcpInterfaceEntry.setStatus("current")


class _DcpInterfaceIndex_Type(Unsigned32):
    """Custom type dcpInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpInterfaceIndex_Type.__name__ = "Unsigned32"
_DcpInterfaceIndex_Object = MibTableColumn
dcpInterfaceIndex = _DcpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 1),
    _DcpInterfaceIndex_Type()
)
dcpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpInterfaceIndex.setStatus("current")
_DcpInterfaceName_Type = DisplayString
_DcpInterfaceName_Object = MibTableColumn
dcpInterfaceName = _DcpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 2),
    _DcpInterfaceName_Type()
)
dcpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceName.setStatus("current")
_DcpInterfaceRxPower_Type = OpticalPower1Decimal
_DcpInterfaceRxPower_Object = MibTableColumn
dcpInterfaceRxPower = _DcpInterfaceRxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 3),
    _DcpInterfaceRxPower_Type()
)
dcpInterfaceRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceRxPower.setStatus("current")
_DcpInterfaceTxPower_Type = OpticalPower1Decimal
_DcpInterfaceTxPower_Object = MibTableColumn
dcpInterfaceTxPower = _DcpInterfaceTxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 4),
    _DcpInterfaceTxPower_Type()
)
dcpInterfaceTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTxPower.setStatus("current")
_DcpInterfaceStatus_Type = InterfaceStatus
_DcpInterfaceStatus_Object = MibTableColumn
dcpInterfaceStatus = _DcpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 5),
    _DcpInterfaceStatus_Type()
)
dcpInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceStatus.setStatus("current")
_DcpInterfaceAlarm_Type = ItuPerceivedSeverity
_DcpInterfaceAlarm_Object = MibTableColumn
dcpInterfaceAlarm = _DcpInterfaceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 6),
    _DcpInterfaceAlarm_Type()
)
dcpInterfaceAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceAlarm.setStatus("current")
_DcpInterfaceFormat_Type = DisplayString
_DcpInterfaceFormat_Object = MibTableColumn
dcpInterfaceFormat = _DcpInterfaceFormat_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 7),
    _DcpInterfaceFormat_Type()
)
dcpInterfaceFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceFormat.setStatus("current")
_DcpInterfaceWavelength_Type = DisplayString
_DcpInterfaceWavelength_Object = MibTableColumn
dcpInterfaceWavelength = _DcpInterfaceWavelength_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 8),
    _DcpInterfaceWavelength_Type()
)
dcpInterfaceWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceWavelength.setStatus("current")
_DcpInterfaceChannelId_Type = DisplayString
_DcpInterfaceChannelId_Object = MibTableColumn
dcpInterfaceChannelId = _DcpInterfaceChannelId_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 9),
    _DcpInterfaceChannelId_Type()
)
dcpInterfaceChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceChannelId.setStatus("current")


class _DcpInterfaceDescription_Type(DisplayString):
    """Custom type dcpInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcpInterfaceDescription_Type.__name__ = "DisplayString"
_DcpInterfaceDescription_Object = MibTableColumn
dcpInterfaceDescription = _DcpInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 10),
    _DcpInterfaceDescription_Type()
)
dcpInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceDescription.setStatus("current")


class _DcpInterfacePortType_Type(DisplayString):
    """Custom type dcpInterfacePortType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcpInterfacePortType_Type.__name__ = "DisplayString"
_DcpInterfacePortType_Object = MibTableColumn
dcpInterfacePortType = _DcpInterfacePortType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 11),
    _DcpInterfacePortType_Type()
)
dcpInterfacePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfacePortType.setStatus("current")
_DcpInterfacePortMode_Type = InterfacePortMode
_DcpInterfacePortMode_Object = MibTableColumn
dcpInterfacePortMode = _DcpInterfacePortMode_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 12),
    _DcpInterfacePortMode_Type()
)
dcpInterfacePortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfacePortMode.setStatus("current")
_DcpInterfaceMIBCompliance_ObjectIdentity = ObjectIdentity
dcpInterfaceMIBCompliance = _DcpInterfaceMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2)
)
_DcpInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
dcpInterfaceMIBGroups = _DcpInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1)
)
_DcpInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
dcpInterfaceMIBCompliances = _DcpInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2)
)

# Managed Objects groups

dcpInterfaceTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1, 1)
)
dcpInterfaceTableGroupV1.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceStatus"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceAlarm"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceFormat"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceWavelength"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTableGroupV1.setStatus("deprecated")

dcpInterfaceTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1, 2)
)
dcpInterfaceTableGroupV2.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceStatus"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceAlarm"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceFormat"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceWavelength"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTableGroupV2.setStatus("current")

dcpInterfaceTableGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1, 3)
)
dcpInterfaceTableGroupV3.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceStatus"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceAlarm"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceFormat"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceWavelength"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceDescription"),
        ("DCP-INTERFACE-MIB", "dcpInterfacePortType"),
        ("DCP-INTERFACE-MIB", "dcpInterfacePortMode"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTableGroupV3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dcpInterfaceBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 1)
)
dcpInterfaceBasicComplV1.setObjects(
    ("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV1")
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV1.setStatus(
        "deprecated"
    )

dcpInterfaceBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 2)
)
dcpInterfaceBasicComplV2.setObjects(
    ("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV2")
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV2.setStatus(
        "current"
    )

dcpInterfaceBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 3)
)
dcpInterfaceBasicComplV3.setObjects(
    ("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV3")
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-INTERFACE-MIB",
    **{"dcpInterface": dcpInterface,
       "dcpInterfaceObjects": dcpInterfaceObjects,
       "dcpInterfaceTable": dcpInterfaceTable,
       "dcpInterfaceEntry": dcpInterfaceEntry,
       "dcpInterfaceIndex": dcpInterfaceIndex,
       "dcpInterfaceName": dcpInterfaceName,
       "dcpInterfaceRxPower": dcpInterfaceRxPower,
       "dcpInterfaceTxPower": dcpInterfaceTxPower,
       "dcpInterfaceStatus": dcpInterfaceStatus,
       "dcpInterfaceAlarm": dcpInterfaceAlarm,
       "dcpInterfaceFormat": dcpInterfaceFormat,
       "dcpInterfaceWavelength": dcpInterfaceWavelength,
       "dcpInterfaceChannelId": dcpInterfaceChannelId,
       "dcpInterfaceDescription": dcpInterfaceDescription,
       "dcpInterfacePortType": dcpInterfacePortType,
       "dcpInterfacePortMode": dcpInterfacePortMode,
       "dcpInterfaceMIBCompliance": dcpInterfaceMIBCompliance,
       "dcpInterfaceMIBGroups": dcpInterfaceMIBGroups,
       "dcpInterfaceTableGroupV1": dcpInterfaceTableGroupV1,
       "dcpInterfaceTableGroupV2": dcpInterfaceTableGroupV2,
       "dcpInterfaceTableGroupV3": dcpInterfaceTableGroupV3,
       "dcpInterfaceMIBCompliances": dcpInterfaceMIBCompliances,
       "dcpInterfaceBasicComplV1": dcpInterfaceBasicComplV1,
       "dcpInterfaceBasicComplV2": dcpInterfaceBasicComplV2,
       "dcpInterfaceBasicComplV3": dcpInterfaceBasicComplV3}
)
