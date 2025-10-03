# SNMP MIB module (DCP-OCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\DCP-OCH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:26 2025
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

(DcpHundreds,
 DcpTenths,
 InterfaceStatus,
 ItuPerceivedSeverity,
 OchPortMode,
 OpticalPower1Decimal) = mibBuilder.importSymbols(
    "SO-TC-MIB",
    "DcpHundreds",
    "DcpTenths",
    "InterfaceStatus",
    "ItuPerceivedSeverity",
    "OchPortMode",
    "OpticalPower1Decimal")


# MODULE-IDENTITY

dcpOch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4)
)
if mibBuilder.loadTexts:
    dcpOch.setRevisions(
        ("2021-03-18 14:49",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcpOchGeneral_ObjectIdentity = ObjectIdentity
dcpOchGeneral = _DcpOchGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1)
)
_DcpOchGeneralTable_Object = MibTable
dcpOchGeneralTable = _DcpOchGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dcpOchGeneralTable.setStatus("current")
_DcpOchGeneralEntry_Object = MibTableRow
dcpOchGeneralEntry = _DcpOchGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1)
)
dcpOchGeneralEntry.setIndexNames(
    (0, "DCP-OCH-MIB", "dcpOchGeneralIndex"),
)
if mibBuilder.loadTexts:
    dcpOchGeneralEntry.setStatus("current")


class _DcpOchGeneralIndex_Type(Unsigned32):
    """Custom type dcpOchGeneralIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpOchGeneralIndex_Type.__name__ = "Unsigned32"
_DcpOchGeneralIndex_Object = MibTableColumn
dcpOchGeneralIndex = _DcpOchGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1, 1),
    _DcpOchGeneralIndex_Type()
)
dcpOchGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpOchGeneralIndex.setStatus("current")
_DcpOchGeneralPortName_Type = DisplayString
_DcpOchGeneralPortName_Object = MibTableColumn
dcpOchGeneralPortName = _DcpOchGeneralPortName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1, 2),
    _DcpOchGeneralPortName_Type()
)
dcpOchGeneralPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchGeneralPortName.setStatus("current")
_DcpOchGeneralSpacing_Type = DcpHundreds
_DcpOchGeneralSpacing_Object = MibTableColumn
dcpOchGeneralSpacing = _DcpOchGeneralSpacing_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1, 3),
    _DcpOchGeneralSpacing_Type()
)
dcpOchGeneralSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchGeneralSpacing.setStatus("current")
_DcpOchGeneralMaxChannels_Type = Unsigned32
_DcpOchGeneralMaxChannels_Object = MibTableColumn
dcpOchGeneralMaxChannels = _DcpOchGeneralMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1, 4),
    _DcpOchGeneralMaxChannels_Type()
)
dcpOchGeneralMaxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchGeneralMaxChannels.setStatus("current")
_DcpOchGeneralActiveChannels_Type = Unsigned32
_DcpOchGeneralActiveChannels_Object = MibTableColumn
dcpOchGeneralActiveChannels = _DcpOchGeneralActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1, 5),
    _DcpOchGeneralActiveChannels_Type()
)
dcpOchGeneralActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchGeneralActiveChannels.setStatus("current")


class _DcpOchGeneralUtilization_Type(Gauge32):
    """Custom type dcpOchGeneralUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DcpOchGeneralUtilization_Type.__name__ = "Gauge32"
_DcpOchGeneralUtilization_Object = MibTableColumn
dcpOchGeneralUtilization = _DcpOchGeneralUtilization_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1, 6),
    _DcpOchGeneralUtilization_Type()
)
dcpOchGeneralUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchGeneralUtilization.setStatus("current")
_DcpOchGeneralConfiguredChannels_Type = Unsigned32
_DcpOchGeneralConfiguredChannels_Object = MibTableColumn
dcpOchGeneralConfiguredChannels = _DcpOchGeneralConfiguredChannels_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 1, 1, 1, 7),
    _DcpOchGeneralConfiguredChannels_Type()
)
dcpOchGeneralConfiguredChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchGeneralConfiguredChannels.setStatus("current")
_DcpOchObjects_ObjectIdentity = ObjectIdentity
dcpOchObjects = _DcpOchObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2)
)
_DcpOchTable_Object = MibTable
dcpOchTable = _DcpOchTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dcpOchTable.setStatus("current")
_DcpOchEntry_Object = MibTableRow
dcpOchEntry = _DcpOchEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1)
)
dcpOchEntry.setIndexNames(
    (0, "DCP-OCH-MIB", "dcpOchIndex"),
)
if mibBuilder.loadTexts:
    dcpOchEntry.setStatus("current")


class _DcpOchIndex_Type(Unsigned32):
    """Custom type dcpOchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpOchIndex_Type.__name__ = "Unsigned32"
_DcpOchIndex_Object = MibTableColumn
dcpOchIndex = _DcpOchIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 1),
    _DcpOchIndex_Type()
)
dcpOchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpOchIndex.setStatus("current")
_DcpOchChannelId_Type = DisplayString
_DcpOchChannelId_Object = MibTableColumn
dcpOchChannelId = _DcpOchChannelId_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 2),
    _DcpOchChannelId_Type()
)
dcpOchChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchChannelId.setStatus("current")
_DcpOchRxPower_Type = DcpTenths
_DcpOchRxPower_Object = MibTableColumn
dcpOchRxPower = _DcpOchRxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 3),
    _DcpOchRxPower_Type()
)
dcpOchRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchRxPower.setStatus("current")
_DcpOchTxPower_Type = DcpTenths
_DcpOchTxPower_Object = MibTableColumn
dcpOchTxPower = _DcpOchTxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 4),
    _DcpOchTxPower_Type()
)
dcpOchTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchTxPower.setStatus("current")
_DcpOchWssAttenuation_Type = DcpTenths
_DcpOchWssAttenuation_Object = MibTableColumn
dcpOchWssAttenuation = _DcpOchWssAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 5),
    _DcpOchWssAttenuation_Type()
)
dcpOchWssAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchWssAttenuation.setStatus("current")
_DcpOchWssInsertionLoss_Type = DcpTenths
_DcpOchWssInsertionLoss_Object = MibTableColumn
dcpOchWssInsertionLoss = _DcpOchWssInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 6),
    _DcpOchWssInsertionLoss_Type()
)
dcpOchWssInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchWssInsertionLoss.setStatus("current")
_DcpOchWantedOutputPower_Type = DcpTenths
_DcpOchWantedOutputPower_Object = MibTableColumn
dcpOchWantedOutputPower = _DcpOchWantedOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 7),
    _DcpOchWantedOutputPower_Type()
)
dcpOchWantedOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchWantedOutputPower.setStatus("current")
_DcpOchPortMode_Type = OchPortMode
_DcpOchPortMode_Object = MibTableColumn
dcpOchPortMode = _DcpOchPortMode_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 8),
    _DcpOchPortMode_Type()
)
dcpOchPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchPortMode.setStatus("current")
_DcpOchStatus_Type = InterfaceStatus
_DcpOchStatus_Object = MibTableColumn
dcpOchStatus = _DcpOchStatus_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 9),
    _DcpOchStatus_Type()
)
dcpOchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchStatus.setStatus("current")


class _DcpOchDescription_Type(DisplayString):
    """Custom type dcpOchDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcpOchDescription_Type.__name__ = "DisplayString"
_DcpOchDescription_Object = MibTableColumn
dcpOchDescription = _DcpOchDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 10),
    _DcpOchDescription_Type()
)
dcpOchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchDescription.setStatus("current")
_DcpOchAlarm_Type = ItuPerceivedSeverity
_DcpOchAlarm_Object = MibTableColumn
dcpOchAlarm = _DcpOchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 2, 1, 1, 11),
    _DcpOchAlarm_Type()
)
dcpOchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpOchAlarm.setStatus("current")
_DcpOchMIBCompliance_ObjectIdentity = ObjectIdentity
dcpOchMIBCompliance = _DcpOchMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 3)
)
_DcpOchMIBGroups_ObjectIdentity = ObjectIdentity
dcpOchMIBGroups = _DcpOchMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 3, 1)
)
_DcpOchMIBCompliances_ObjectIdentity = ObjectIdentity
dcpOchMIBCompliances = _DcpOchMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 3, 2)
)

# Managed Objects groups

dcpOchGeneralTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 3, 1, 1)
)
dcpOchGeneralTableGroupV1.setObjects(
      *(("DCP-OCH-MIB", "dcpOchGeneralPortName"),
        ("DCP-OCH-MIB", "dcpOchGeneralSpacing"),
        ("DCP-OCH-MIB", "dcpOchGeneralMaxChannels"),
        ("DCP-OCH-MIB", "dcpOchGeneralActiveChannels"),
        ("DCP-OCH-MIB", "dcpOchGeneralUtilization"),
        ("DCP-OCH-MIB", "dcpOchGeneralConfiguredChannels"))
)
if mibBuilder.loadTexts:
    dcpOchGeneralTableGroupV1.setStatus("current")

dcpOchTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 3, 1, 2)
)
dcpOchTableGroupV1.setObjects(
      *(("DCP-OCH-MIB", "dcpOchChannelId"),
        ("DCP-OCH-MIB", "dcpOchRxPower"),
        ("DCP-OCH-MIB", "dcpOchTxPower"),
        ("DCP-OCH-MIB", "dcpOchWssAttenuation"),
        ("DCP-OCH-MIB", "dcpOchWssInsertionLoss"),
        ("DCP-OCH-MIB", "dcpOchWantedOutputPower"),
        ("DCP-OCH-MIB", "dcpOchPortMode"),
        ("DCP-OCH-MIB", "dcpOchStatus"),
        ("DCP-OCH-MIB", "dcpOchDescription"),
        ("DCP-OCH-MIB", "dcpOchAlarm"))
)
if mibBuilder.loadTexts:
    dcpOchTableGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dcpOchBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 4, 3, 2, 1)
)
dcpOchBasicComplV1.setObjects(
      *(("DCP-OCH-MIB", "dcpOchGeneralTableGroupV1"),
        ("DCP-OCH-MIB", "dcpOchTableGroupV1"))
)
if mibBuilder.loadTexts:
    dcpOchBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-OCH-MIB",
    **{"dcpOch": dcpOch,
       "dcpOchGeneral": dcpOchGeneral,
       "dcpOchGeneralTable": dcpOchGeneralTable,
       "dcpOchGeneralEntry": dcpOchGeneralEntry,
       "dcpOchGeneralIndex": dcpOchGeneralIndex,
       "dcpOchGeneralPortName": dcpOchGeneralPortName,
       "dcpOchGeneralSpacing": dcpOchGeneralSpacing,
       "dcpOchGeneralMaxChannels": dcpOchGeneralMaxChannels,
       "dcpOchGeneralActiveChannels": dcpOchGeneralActiveChannels,
       "dcpOchGeneralUtilization": dcpOchGeneralUtilization,
       "dcpOchGeneralConfiguredChannels": dcpOchGeneralConfiguredChannels,
       "dcpOchObjects": dcpOchObjects,
       "dcpOchTable": dcpOchTable,
       "dcpOchEntry": dcpOchEntry,
       "dcpOchIndex": dcpOchIndex,
       "dcpOchChannelId": dcpOchChannelId,
       "dcpOchRxPower": dcpOchRxPower,
       "dcpOchTxPower": dcpOchTxPower,
       "dcpOchWssAttenuation": dcpOchWssAttenuation,
       "dcpOchWssInsertionLoss": dcpOchWssInsertionLoss,
       "dcpOchWantedOutputPower": dcpOchWantedOutputPower,
       "dcpOchPortMode": dcpOchPortMode,
       "dcpOchStatus": dcpOchStatus,
       "dcpOchDescription": dcpOchDescription,
       "dcpOchAlarm": dcpOchAlarm,
       "dcpOchMIBCompliance": dcpOchMIBCompliance,
       "dcpOchMIBGroups": dcpOchMIBGroups,
       "dcpOchGeneralTableGroupV1": dcpOchGeneralTableGroupV1,
       "dcpOchTableGroupV1": dcpOchTableGroupV1,
       "dcpOchMIBCompliances": dcpOchMIBCompliances,
       "dcpOchBasicComplV1": dcpOchBasicComplV1}
)
