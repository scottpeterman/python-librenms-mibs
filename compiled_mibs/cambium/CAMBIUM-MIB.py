# SNMP MIB module (CAMBIUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\cnpilote\CAMBIUM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:38 2025
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
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cnPilotMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 22)
)
if mibBuilder.loadTexts:
    cnPilotMIB.setRevisions(
        ("2015-09-09 12:38",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cambium_ObjectIdentity = ObjectIdentity
cambium = _Cambium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
_CambiumStateGroup_ObjectIdentity = ObjectIdentity
cambiumStateGroup = _CambiumStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1)
)
_CambiumAccessPointTable_Object = MibTable
cambiumAccessPointTable = _CambiumAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1)
)
if mibBuilder.loadTexts:
    cambiumAccessPointTable.setStatus("current")
_CambiumAccessPointEntry_Object = MibTableRow
cambiumAccessPointEntry = _CambiumAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1)
)
cambiumAccessPointEntry.setIndexNames(
    (0, "CAMBIUM-MIB", "cambiumAPMACAddress"),
)
if mibBuilder.loadTexts:
    cambiumAccessPointEntry.setStatus("current")
_CambiumAPMACAddress_Type = MacAddress
_CambiumAPMACAddress_Object = MibTableColumn
cambiumAPMACAddress = _CambiumAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 1),
    _CambiumAPMACAddress_Type()
)
cambiumAPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPMACAddress.setStatus("current")


class _CambiumAPName_Type(DisplayString):
    """Custom type cambiumAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumAPName_Type.__name__ = "DisplayString"
_CambiumAPName_Object = MibTableColumn
cambiumAPName = _CambiumAPName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 2),
    _CambiumAPName_Type()
)
cambiumAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPName.setStatus("current")


class _CambiumAPIPAddress_Type(DisplayString):
    """Custom type cambiumAPIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumAPIPAddress_Type.__name__ = "DisplayString"
_CambiumAPIPAddress_Object = MibTableColumn
cambiumAPIPAddress = _CambiumAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 3),
    _CambiumAPIPAddress_Type()
)
cambiumAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPIPAddress.setStatus("current")


class _CambiumAPSerialNum_Type(DisplayString):
    """Custom type cambiumAPSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumAPSerialNum_Type.__name__ = "DisplayString"
_CambiumAPSerialNum_Object = MibTableColumn
cambiumAPSerialNum = _CambiumAPSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 4),
    _CambiumAPSerialNum_Type()
)
cambiumAPSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPSerialNum.setStatus("current")


class _CambiumAPModel_Type(DisplayString):
    """Custom type cambiumAPModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumAPModel_Type.__name__ = "DisplayString"
_CambiumAPModel_Object = MibTableColumn
cambiumAPModel = _CambiumAPModel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 5),
    _CambiumAPModel_Type()
)
cambiumAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPModel.setStatus("current")
_CambiumAPCPUUtilization_Type = Integer32
_CambiumAPCPUUtilization_Object = MibTableColumn
cambiumAPCPUUtilization = _CambiumAPCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 6),
    _CambiumAPCPUUtilization_Type()
)
cambiumAPCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPCPUUtilization.setStatus("current")
_CambiumAPMemoryFree_Type = Integer32
_CambiumAPMemoryFree_Object = MibTableColumn
cambiumAPMemoryFree = _CambiumAPMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 7),
    _CambiumAPMemoryFree_Type()
)
cambiumAPMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPMemoryFree.setStatus("current")


class _CambiumAPSWVersion_Type(DisplayString):
    """Custom type cambiumAPSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumAPSWVersion_Type.__name__ = "DisplayString"
_CambiumAPSWVersion_Object = MibTableColumn
cambiumAPSWVersion = _CambiumAPSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 8),
    _CambiumAPSWVersion_Type()
)
cambiumAPSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPSWVersion.setStatus("current")
_CambiumAPUptime_Type = TimeTicks
_CambiumAPUptime_Object = MibTableColumn
cambiumAPUptime = _CambiumAPUptime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 9),
    _CambiumAPUptime_Type()
)
cambiumAPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPUptime.setStatus("current")


class _CambiumAPHWType_Type(DisplayString):
    """Custom type cambiumAPHWType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumAPHWType_Type.__name__ = "DisplayString"
_CambiumAPHWType_Object = MibTableColumn
cambiumAPHWType = _CambiumAPHWType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 10),
    _CambiumAPHWType_Type()
)
cambiumAPHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPHWType.setStatus("current")


class _CambiumAPRegulatory_Type(DisplayString):
    """Custom type cambiumAPRegulatory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumAPRegulatory_Type.__name__ = "DisplayString"
_CambiumAPRegulatory_Object = MibTableColumn
cambiumAPRegulatory = _CambiumAPRegulatory_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 11),
    _CambiumAPRegulatory_Type()
)
cambiumAPRegulatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPRegulatory.setStatus("current")


class _CambiumAPCnmConstaus_Type(DisplayString):
    """Custom type cambiumAPCnmConstaus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumAPCnmConstaus_Type.__name__ = "DisplayString"
_CambiumAPCnmConstaus_Object = MibTableColumn
cambiumAPCnmConstaus = _CambiumAPCnmConstaus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 12),
    _CambiumAPCnmConstaus_Type()
)
cambiumAPCnmConstaus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPCnmConstaus.setStatus("current")


class _CambiumAPCnmAccID_Type(DisplayString):
    """Custom type cambiumAPCnmAccID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumAPCnmAccID_Type.__name__ = "DisplayString"
_CambiumAPCnmAccID_Object = MibTableColumn
cambiumAPCnmAccID = _CambiumAPCnmAccID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 13),
    _CambiumAPCnmAccID_Type()
)
cambiumAPCnmAccID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPCnmAccID.setStatus("current")
_CambiumAPTotalClients_Type = Integer32
_CambiumAPTotalClients_Object = MibTableColumn
cambiumAPTotalClients = _CambiumAPTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 14),
    _CambiumAPTotalClients_Type()
)
cambiumAPTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPTotalClients.setStatus("current")


class _CambiumAPCheckUpgradeStatus_Type(DisplayString):
    """Custom type cambiumAPCheckUpgradeStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumAPCheckUpgradeStatus_Type.__name__ = "DisplayString"
_CambiumAPCheckUpgradeStatus_Object = MibTableColumn
cambiumAPCheckUpgradeStatus = _CambiumAPCheckUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 15),
    _CambiumAPCheckUpgradeStatus_Type()
)
cambiumAPCheckUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPCheckUpgradeStatus.setStatus("current")
_CambiumRadioTable_Object = MibTable
cambiumRadioTable = _CambiumRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2)
)
if mibBuilder.loadTexts:
    cambiumRadioTable.setStatus("current")
_CambiumRadioEntry_Object = MibTableRow
cambiumRadioEntry = _CambiumRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1)
)
cambiumRadioEntry.setIndexNames(
    (0, "CAMBIUM-MIB", "cambiumRadioIndex"),
)
if mibBuilder.loadTexts:
    cambiumRadioEntry.setStatus("current")
_CambiumRadioIndex_Type = Integer32
_CambiumRadioIndex_Object = MibTableColumn
cambiumRadioIndex = _CambiumRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 1),
    _CambiumRadioIndex_Type()
)
cambiumRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioIndex.setStatus("current")
_CambiumRadioMACAddress_Type = MacAddress
_CambiumRadioMACAddress_Object = MibTableColumn
cambiumRadioMACAddress = _CambiumRadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 2),
    _CambiumRadioMACAddress_Type()
)
cambiumRadioMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioMACAddress.setStatus("current")


class _CambiumRadioBandType_Type(DisplayString):
    """Custom type cambiumRadioBandType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumRadioBandType_Type.__name__ = "DisplayString"
_CambiumRadioBandType_Object = MibTableColumn
cambiumRadioBandType = _CambiumRadioBandType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 3),
    _CambiumRadioBandType_Type()
)
cambiumRadioBandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioBandType.setStatus("current")
_CambiumRadioWlan_Type = Integer32
_CambiumRadioWlan_Object = MibTableColumn
cambiumRadioWlan = _CambiumRadioWlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 4),
    _CambiumRadioWlan_Type()
)
cambiumRadioWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioWlan.setStatus("current")
_CambiumRadioNumClients_Type = Integer32
_CambiumRadioNumClients_Object = MibTableColumn
cambiumRadioNumClients = _CambiumRadioNumClients_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 5),
    _CambiumRadioNumClients_Type()
)
cambiumRadioNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioNumClients.setStatus("current")


class _CambiumRadioChannel_Type(DisplayString):
    """Custom type cambiumRadioChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumRadioChannel_Type.__name__ = "DisplayString"
_CambiumRadioChannel_Object = MibTableColumn
cambiumRadioChannel = _CambiumRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 6),
    _CambiumRadioChannel_Type()
)
cambiumRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioChannel.setStatus("current")


class _CambiumRadioChannelWidth_Type(DisplayString):
    """Custom type cambiumRadioChannelWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumRadioChannelWidth_Type.__name__ = "DisplayString"
_CambiumRadioChannelWidth_Object = MibTableColumn
cambiumRadioChannelWidth = _CambiumRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 7),
    _CambiumRadioChannelWidth_Type()
)
cambiumRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioChannelWidth.setStatus("current")
_CambiumRadioTransmitPower_Type = Integer32
_CambiumRadioTransmitPower_Object = MibTableColumn
cambiumRadioTransmitPower = _CambiumRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 8),
    _CambiumRadioTransmitPower_Type()
)
cambiumRadioTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioTransmitPower.setStatus("current")
_CambiumRadioTotalTxPackets_Type = Counter32
_CambiumRadioTotalTxPackets_Object = MibTableColumn
cambiumRadioTotalTxPackets = _CambiumRadioTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 9),
    _CambiumRadioTotalTxPackets_Type()
)
cambiumRadioTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioTotalTxPackets.setStatus("current")
_CambiumRadioTotalRxPackets_Type = Counter32
_CambiumRadioTotalRxPackets_Object = MibTableColumn
cambiumRadioTotalRxPackets = _CambiumRadioTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 10),
    _CambiumRadioTotalRxPackets_Type()
)
cambiumRadioTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioTotalRxPackets.setStatus("current")
_CambiumRadioTxDataBytes_Type = Counter32
_CambiumRadioTxDataBytes_Object = MibTableColumn
cambiumRadioTxDataBytes = _CambiumRadioTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 11),
    _CambiumRadioTxDataBytes_Type()
)
cambiumRadioTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioTxDataBytes.setStatus("current")
_CambiumRadioRxDataBytes_Type = Counter32
_CambiumRadioRxDataBytes_Object = MibTableColumn
cambiumRadioRxDataBytes = _CambiumRadioRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 12),
    _CambiumRadioRxDataBytes_Type()
)
cambiumRadioRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioRxDataBytes.setStatus("current")


class _CambiumRadioState_Type(DisplayString):
    """Custom type cambiumRadioState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumRadioState_Type.__name__ = "DisplayString"
_CambiumRadioState_Object = MibTableColumn
cambiumRadioState = _CambiumRadioState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 13),
    _CambiumRadioState_Type()
)
cambiumRadioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioState.setStatus("current")
_CambiumRadioDfsStatus_Type = Integer32
_CambiumRadioDfsStatus_Object = MibTableColumn
cambiumRadioDfsStatus = _CambiumRadioDfsStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 14),
    _CambiumRadioDfsStatus_Type()
)
cambiumRadioDfsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioDfsStatus.setStatus("current")
_CambiumRadioDfsDetect_Type = Integer32
_CambiumRadioDfsDetect_Object = MibTableColumn
cambiumRadioDfsDetect = _CambiumRadioDfsDetect_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 15),
    _CambiumRadioDfsDetect_Type()
)
cambiumRadioDfsDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioDfsDetect.setStatus("current")


class _CambiumRadioNoiseFloor_Type(DisplayString):
    """Custom type cambiumRadioNoiseFloor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumRadioNoiseFloor_Type.__name__ = "DisplayString"
_CambiumRadioNoiseFloor_Object = MibTableColumn
cambiumRadioNoiseFloor = _CambiumRadioNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 16),
    _CambiumRadioNoiseFloor_Type()
)
cambiumRadioNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioNoiseFloor.setStatus("current")


class _CambiumRadioInterference_Type(DisplayString):
    """Custom type cambiumRadioInterference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumRadioInterference_Type.__name__ = "DisplayString"
_CambiumRadioInterference_Object = MibTableColumn
cambiumRadioInterference = _CambiumRadioInterference_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 17),
    _CambiumRadioInterference_Type()
)
cambiumRadioInterference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioInterference.setStatus("current")


class _CambiumRadioAirtime_Type(DisplayString):
    """Custom type cambiumRadioAirtime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumRadioAirtime_Type.__name__ = "DisplayString"
_CambiumRadioAirtime_Object = MibTableColumn
cambiumRadioAirtime = _CambiumRadioAirtime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 18),
    _CambiumRadioAirtime_Type()
)
cambiumRadioAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRadioAirtime.setStatus("current")
_CambiumClientTable_Object = MibTable
cambiumClientTable = _CambiumClientTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3)
)
if mibBuilder.loadTexts:
    cambiumClientTable.setStatus("current")
_CambiumClientEntry_Object = MibTableRow
cambiumClientEntry = _CambiumClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1)
)
cambiumClientEntry.setIndexNames(
    (0, "CAMBIUM-MIB", "cambiumClientMACAddressIndex"),
)
if mibBuilder.loadTexts:
    cambiumClientEntry.setStatus("current")
_CambiumClientMACAddressIndex_Type = Integer32
_CambiumClientMACAddressIndex_Object = MibTableColumn
cambiumClientMACAddressIndex = _CambiumClientMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 1),
    _CambiumClientMACAddressIndex_Type()
)
cambiumClientMACAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientMACAddressIndex.setStatus("current")
_CambiumClientMACAddress_Type = MacAddress
_CambiumClientMACAddress_Object = MibTableColumn
cambiumClientMACAddress = _CambiumClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 2),
    _CambiumClientMACAddress_Type()
)
cambiumClientMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientMACAddress.setStatus("current")


class _CambiumClientIPAddress_Type(DisplayString):
    """Custom type cambiumClientIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumClientIPAddress_Type.__name__ = "DisplayString"
_CambiumClientIPAddress_Object = MibTableColumn
cambiumClientIPAddress = _CambiumClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 3),
    _CambiumClientIPAddress_Type()
)
cambiumClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientIPAddress.setStatus("current")


class _CambiumClientName_Type(DisplayString):
    """Custom type cambiumClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumClientName_Type.__name__ = "DisplayString"
_CambiumClientName_Object = MibTableColumn
cambiumClientName = _CambiumClientName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 4),
    _CambiumClientName_Type()
)
cambiumClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientName.setStatus("current")


class _CambiumClientSsid_Type(DisplayString):
    """Custom type cambiumClientSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumClientSsid_Type.__name__ = "DisplayString"
_CambiumClientSsid_Object = MibTableColumn
cambiumClientSsid = _CambiumClientSsid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 5),
    _CambiumClientSsid_Type()
)
cambiumClientSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientSsid.setStatus("current")


class _CambiumClientVendorName_Type(DisplayString):
    """Custom type cambiumClientVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumClientVendorName_Type.__name__ = "DisplayString"
_CambiumClientVendorName_Object = MibTableColumn
cambiumClientVendorName = _CambiumClientVendorName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 6),
    _CambiumClientVendorName_Type()
)
cambiumClientVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientVendorName.setStatus("current")


class _CambiumClientHwmode_Type(DisplayString):
    """Custom type cambiumClientHwmode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumClientHwmode_Type.__name__ = "DisplayString"
_CambiumClientHwmode_Object = MibTableColumn
cambiumClientHwmode = _CambiumClientHwmode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 7),
    _CambiumClientHwmode_Type()
)
cambiumClientHwmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientHwmode.setStatus("current")
_CambiumClientRadioIndex_Type = Integer32
_CambiumClientRadioIndex_Object = MibTableColumn
cambiumClientRadioIndex = _CambiumClientRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 8),
    _CambiumClientRadioIndex_Type()
)
cambiumClientRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientRadioIndex.setStatus("current")
_CambiumClientWlan_Type = Integer32
_CambiumClientWlan_Object = MibTableColumn
cambiumClientWlan = _CambiumClientWlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 9),
    _CambiumClientWlan_Type()
)
cambiumClientWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientWlan.setStatus("current")
_CambiumClientVlan_Type = Integer32
_CambiumClientVlan_Object = MibTableColumn
cambiumClientVlan = _CambiumClientVlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 10),
    _CambiumClientVlan_Type()
)
cambiumClientVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientVlan.setStatus("current")
_CambiumClientSNR_Type = Integer32
_CambiumClientSNR_Object = MibTableColumn
cambiumClientSNR = _CambiumClientSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 11),
    _CambiumClientSNR_Type()
)
cambiumClientSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientSNR.setStatus("current")


class _CambiumClientTxRate_Type(DisplayString):
    """Custom type cambiumClientTxRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumClientTxRate_Type.__name__ = "DisplayString"
_CambiumClientTxRate_Object = MibTableColumn
cambiumClientTxRate = _CambiumClientTxRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 12),
    _CambiumClientTxRate_Type()
)
cambiumClientTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientTxRate.setStatus("current")
_CambiumClientTotalTxPackets_Type = Counter32
_CambiumClientTotalTxPackets_Object = MibTableColumn
cambiumClientTotalTxPackets = _CambiumClientTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 13),
    _CambiumClientTotalTxPackets_Type()
)
cambiumClientTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientTotalTxPackets.setStatus("current")
_CambiumClientTxDataBytes_Type = Counter32
_CambiumClientTxDataBytes_Object = MibTableColumn
cambiumClientTxDataBytes = _CambiumClientTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 14),
    _CambiumClientTxDataBytes_Type()
)
cambiumClientTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientTxDataBytes.setStatus("current")
_CambiumClientTotalRxPackets_Type = Counter32
_CambiumClientTotalRxPackets_Object = MibTableColumn
cambiumClientTotalRxPackets = _CambiumClientTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 15),
    _CambiumClientTotalRxPackets_Type()
)
cambiumClientTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientTotalRxPackets.setStatus("current")
_CambiumClientRxDataBytes_Type = Counter32
_CambiumClientRxDataBytes_Object = MibTableColumn
cambiumClientRxDataBytes = _CambiumClientRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 16),
    _CambiumClientRxDataBytes_Type()
)
cambiumClientRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumClientRxDataBytes.setStatus("current")
_CambiumWlanTable_Object = MibTable
cambiumWlanTable = _CambiumWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4)
)
if mibBuilder.loadTexts:
    cambiumWlanTable.setStatus("current")
_CambiumWlanEntry_Object = MibTableRow
cambiumWlanEntry = _CambiumWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1)
)
cambiumWlanEntry.setIndexNames(
    (0, "CAMBIUM-MIB", "cambiumWlanIndex"),
)
if mibBuilder.loadTexts:
    cambiumWlanEntry.setStatus("current")
_CambiumWlanIndex_Type = Integer32
_CambiumWlanIndex_Object = MibTableColumn
cambiumWlanIndex = _CambiumWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 1),
    _CambiumWlanIndex_Type()
)
cambiumWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanIndex.setStatus("current")


class _CambiumWlanSsid_Type(DisplayString):
    """Custom type cambiumWlanSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumWlanSsid_Type.__name__ = "DisplayString"
_CambiumWlanSsid_Object = MibTableColumn
cambiumWlanSsid = _CambiumWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 2),
    _CambiumWlanSsid_Type()
)
cambiumWlanSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanSsid.setStatus("current")


class _CambiumWlanBand_Type(DisplayString):
    """Custom type cambiumWlanBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumWlanBand_Type.__name__ = "DisplayString"
_CambiumWlanBand_Object = MibTableColumn
cambiumWlanBand = _CambiumWlanBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 3),
    _CambiumWlanBand_Type()
)
cambiumWlanBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanBand.setStatus("current")
_CambiumWlanVlan_Type = Integer32
_CambiumWlanVlan_Object = MibTableColumn
cambiumWlanVlan = _CambiumWlanVlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 4),
    _CambiumWlanVlan_Type()
)
cambiumWlanVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanVlan.setStatus("current")


class _CambiumWlanSecurity_Type(DisplayString):
    """Custom type cambiumWlanSecurity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumWlanSecurity_Type.__name__ = "DisplayString"
_CambiumWlanSecurity_Object = MibTableColumn
cambiumWlanSecurity = _CambiumWlanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 5),
    _CambiumWlanSecurity_Type()
)
cambiumWlanSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanSecurity.setStatus("current")


class _CambiumWlanGuestAccess_Type(DisplayString):
    """Custom type cambiumWlanGuestAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumWlanGuestAccess_Type.__name__ = "DisplayString"
_CambiumWlanGuestAccess_Object = MibTableColumn
cambiumWlanGuestAccess = _CambiumWlanGuestAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 6),
    _CambiumWlanGuestAccess_Type()
)
cambiumWlanGuestAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanGuestAccess.setStatus("current")
_CambiumWlanNumClients_Type = Integer32
_CambiumWlanNumClients_Object = MibTableColumn
cambiumWlanNumClients = _CambiumWlanNumClients_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 7),
    _CambiumWlanNumClients_Type()
)
cambiumWlanNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanNumClients.setStatus("current")
_CambiumWlanTotalTxPackets_Type = Counter32
_CambiumWlanTotalTxPackets_Object = MibTableColumn
cambiumWlanTotalTxPackets = _CambiumWlanTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 8),
    _CambiumWlanTotalTxPackets_Type()
)
cambiumWlanTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanTotalTxPackets.setStatus("current")
_CambiumWlanTxDataBytes_Type = Counter32
_CambiumWlanTxDataBytes_Object = MibTableColumn
cambiumWlanTxDataBytes = _CambiumWlanTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 9),
    _CambiumWlanTxDataBytes_Type()
)
cambiumWlanTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanTxDataBytes.setStatus("current")
_CambiumWlanTotalRxPackets_Type = Counter32
_CambiumWlanTotalRxPackets_Object = MibTableColumn
cambiumWlanTotalRxPackets = _CambiumWlanTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 10),
    _CambiumWlanTotalRxPackets_Type()
)
cambiumWlanTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanTotalRxPackets.setStatus("current")
_CambiumWlanRxDataBytes_Type = Counter32
_CambiumWlanRxDataBytes_Object = MibTableColumn
cambiumWlanRxDataBytes = _CambiumWlanRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 11),
    _CambiumWlanRxDataBytes_Type()
)
cambiumWlanRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWlanRxDataBytes.setStatus("current")
_CambiumMeshClientTable_Object = MibTable
cambiumMeshClientTable = _CambiumMeshClientTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5)
)
if mibBuilder.loadTexts:
    cambiumMeshClientTable.setStatus("current")
_CambiumMeshClientEntry_Object = MibTableRow
cambiumMeshClientEntry = _CambiumMeshClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1)
)
cambiumMeshClientEntry.setIndexNames(
    (0, "CAMBIUM-MIB", "cambiumMeshClientMACAddressIndex"),
)
if mibBuilder.loadTexts:
    cambiumMeshClientEntry.setStatus("current")
_CambiumMeshClientMACAddressIndex_Type = Integer32
_CambiumMeshClientMACAddressIndex_Object = MibTableColumn
cambiumMeshClientMACAddressIndex = _CambiumMeshClientMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 1),
    _CambiumMeshClientMACAddressIndex_Type()
)
cambiumMeshClientMACAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientMACAddressIndex.setStatus("current")
_CambiumMeshClientMACAddress_Type = MacAddress
_CambiumMeshClientMACAddress_Object = MibTableColumn
cambiumMeshClientMACAddress = _CambiumMeshClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 2),
    _CambiumMeshClientMACAddress_Type()
)
cambiumMeshClientMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientMACAddress.setStatus("current")
_CambiumMeshClientBaseMACAddress_Type = MacAddress
_CambiumMeshClientBaseMACAddress_Object = MibTableColumn
cambiumMeshClientBaseMACAddress = _CambiumMeshClientBaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 3),
    _CambiumMeshClientBaseMACAddress_Type()
)
cambiumMeshClientBaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientBaseMACAddress.setStatus("current")


class _CambiumMeshClientIPAddress_Type(DisplayString):
    """Custom type cambiumMeshClientIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumMeshClientIPAddress_Type.__name__ = "DisplayString"
_CambiumMeshClientIPAddress_Object = MibTableColumn
cambiumMeshClientIPAddress = _CambiumMeshClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 4),
    _CambiumMeshClientIPAddress_Type()
)
cambiumMeshClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientIPAddress.setStatus("current")


class _CambiumMeshClientName_Type(DisplayString):
    """Custom type cambiumMeshClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumMeshClientName_Type.__name__ = "DisplayString"
_CambiumMeshClientName_Object = MibTableColumn
cambiumMeshClientName = _CambiumMeshClientName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 5),
    _CambiumMeshClientName_Type()
)
cambiumMeshClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientName.setStatus("current")


class _CambiumMeshClientSsid_Type(DisplayString):
    """Custom type cambiumMeshClientSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumMeshClientSsid_Type.__name__ = "DisplayString"
_CambiumMeshClientSsid_Object = MibTableColumn
cambiumMeshClientSsid = _CambiumMeshClientSsid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 6),
    _CambiumMeshClientSsid_Type()
)
cambiumMeshClientSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientSsid.setStatus("current")


class _CambiumMeshClientRadioBand_Type(DisplayString):
    """Custom type cambiumMeshClientRadioBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumMeshClientRadioBand_Type.__name__ = "DisplayString"
_CambiumMeshClientRadioBand_Object = MibTableColumn
cambiumMeshClientRadioBand = _CambiumMeshClientRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 7),
    _CambiumMeshClientRadioBand_Type()
)
cambiumMeshClientRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientRadioBand.setStatus("current")
_CambiumMeshClientSNR_Type = Integer32
_CambiumMeshClientSNR_Object = MibTableColumn
cambiumMeshClientSNR = _CambiumMeshClientSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 8),
    _CambiumMeshClientSNR_Type()
)
cambiumMeshClientSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientSNR.setStatus("current")
_CambiumMeshClientRSSI_Type = Integer32
_CambiumMeshClientRSSI_Object = MibTableColumn
cambiumMeshClientRSSI = _CambiumMeshClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 9),
    _CambiumMeshClientRSSI_Type()
)
cambiumMeshClientRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientRSSI.setStatus("current")


class _CambiumMeshClientStatus_Type(DisplayString):
    """Custom type cambiumMeshClientStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumMeshClientStatus_Type.__name__ = "DisplayString"
_CambiumMeshClientStatus_Object = MibTableColumn
cambiumMeshClientStatus = _CambiumMeshClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 10),
    _CambiumMeshClientStatus_Type()
)
cambiumMeshClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientStatus.setStatus("current")


class _CambiumMeshClientDataRate_Type(DisplayString):
    """Custom type cambiumMeshClientDataRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CambiumMeshClientDataRate_Type.__name__ = "DisplayString"
_CambiumMeshClientDataRate_Object = MibTableColumn
cambiumMeshClientDataRate = _CambiumMeshClientDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 11),
    _CambiumMeshClientDataRate_Type()
)
cambiumMeshClientDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientDataRate.setStatus("current")
_CambiumMeshClientTotalTxPackets_Type = Counter32
_CambiumMeshClientTotalTxPackets_Object = MibTableColumn
cambiumMeshClientTotalTxPackets = _CambiumMeshClientTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 12),
    _CambiumMeshClientTotalTxPackets_Type()
)
cambiumMeshClientTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientTotalTxPackets.setStatus("current")
_CambiumMeshClientTxDataBytes_Type = Counter32
_CambiumMeshClientTxDataBytes_Object = MibTableColumn
cambiumMeshClientTxDataBytes = _CambiumMeshClientTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 13),
    _CambiumMeshClientTxDataBytes_Type()
)
cambiumMeshClientTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientTxDataBytes.setStatus("current")
_CambiumMeshClientTotalRxPackets_Type = Counter32
_CambiumMeshClientTotalRxPackets_Object = MibTableColumn
cambiumMeshClientTotalRxPackets = _CambiumMeshClientTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 14),
    _CambiumMeshClientTotalRxPackets_Type()
)
cambiumMeshClientTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientTotalRxPackets.setStatus("current")
_CambiumMeshClientRxDataBytes_Type = Counter32
_CambiumMeshClientRxDataBytes_Object = MibTableColumn
cambiumMeshClientRxDataBytes = _CambiumMeshClientRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 15),
    _CambiumMeshClientRxDataBytes_Type()
)
cambiumMeshClientRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMeshClientRxDataBytes.setStatus("current")


class _CambiumAPSetIPAddress_Type(DisplayString):
    """Custom type cambiumAPSetIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumAPSetIPAddress_Type.__name__ = "DisplayString"
_CambiumAPSetIPAddress_Object = MibScalar
cambiumAPSetIPAddress = _CambiumAPSetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 6),
    _CambiumAPSetIPAddress_Type()
)
cambiumAPSetIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumAPSetIPAddress.setStatus("current")


class _CambiumAPReboot_Type(Integer32):
    """Custom type cambiumAPReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumAPReboot_Type.__name__ = "Integer32"
_CambiumAPReboot_Object = MibScalar
cambiumAPReboot = _CambiumAPReboot_Object(
    (1, 3, 6, 1, 4, 1, 17713, 22, 1, 7),
    _CambiumAPReboot_Type()
)
cambiumAPReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumAPReboot.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-MIB",
    **{"cambium": cambium,
       "cnPilotMIB": cnPilotMIB,
       "cambiumStateGroup": cambiumStateGroup,
       "cambiumAccessPointTable": cambiumAccessPointTable,
       "cambiumAccessPointEntry": cambiumAccessPointEntry,
       "cambiumAPMACAddress": cambiumAPMACAddress,
       "cambiumAPName": cambiumAPName,
       "cambiumAPIPAddress": cambiumAPIPAddress,
       "cambiumAPSerialNum": cambiumAPSerialNum,
       "cambiumAPModel": cambiumAPModel,
       "cambiumAPCPUUtilization": cambiumAPCPUUtilization,
       "cambiumAPMemoryFree": cambiumAPMemoryFree,
       "cambiumAPSWVersion": cambiumAPSWVersion,
       "cambiumAPUptime": cambiumAPUptime,
       "cambiumAPHWType": cambiumAPHWType,
       "cambiumAPRegulatory": cambiumAPRegulatory,
       "cambiumAPCnmConstaus": cambiumAPCnmConstaus,
       "cambiumAPCnmAccID": cambiumAPCnmAccID,
       "cambiumAPTotalClients": cambiumAPTotalClients,
       "cambiumAPCheckUpgradeStatus": cambiumAPCheckUpgradeStatus,
       "cambiumRadioTable": cambiumRadioTable,
       "cambiumRadioEntry": cambiumRadioEntry,
       "cambiumRadioIndex": cambiumRadioIndex,
       "cambiumRadioMACAddress": cambiumRadioMACAddress,
       "cambiumRadioBandType": cambiumRadioBandType,
       "cambiumRadioWlan": cambiumRadioWlan,
       "cambiumRadioNumClients": cambiumRadioNumClients,
       "cambiumRadioChannel": cambiumRadioChannel,
       "cambiumRadioChannelWidth": cambiumRadioChannelWidth,
       "cambiumRadioTransmitPower": cambiumRadioTransmitPower,
       "cambiumRadioTotalTxPackets": cambiumRadioTotalTxPackets,
       "cambiumRadioTotalRxPackets": cambiumRadioTotalRxPackets,
       "cambiumRadioTxDataBytes": cambiumRadioTxDataBytes,
       "cambiumRadioRxDataBytes": cambiumRadioRxDataBytes,
       "cambiumRadioState": cambiumRadioState,
       "cambiumRadioDfsStatus": cambiumRadioDfsStatus,
       "cambiumRadioDfsDetect": cambiumRadioDfsDetect,
       "cambiumRadioNoiseFloor": cambiumRadioNoiseFloor,
       "cambiumRadioInterference": cambiumRadioInterference,
       "cambiumRadioAirtime": cambiumRadioAirtime,
       "cambiumClientTable": cambiumClientTable,
       "cambiumClientEntry": cambiumClientEntry,
       "cambiumClientMACAddressIndex": cambiumClientMACAddressIndex,
       "cambiumClientMACAddress": cambiumClientMACAddress,
       "cambiumClientIPAddress": cambiumClientIPAddress,
       "cambiumClientName": cambiumClientName,
       "cambiumClientSsid": cambiumClientSsid,
       "cambiumClientVendorName": cambiumClientVendorName,
       "cambiumClientHwmode": cambiumClientHwmode,
       "cambiumClientRadioIndex": cambiumClientRadioIndex,
       "cambiumClientWlan": cambiumClientWlan,
       "cambiumClientVlan": cambiumClientVlan,
       "cambiumClientSNR": cambiumClientSNR,
       "cambiumClientTxRate": cambiumClientTxRate,
       "cambiumClientTotalTxPackets": cambiumClientTotalTxPackets,
       "cambiumClientTxDataBytes": cambiumClientTxDataBytes,
       "cambiumClientTotalRxPackets": cambiumClientTotalRxPackets,
       "cambiumClientRxDataBytes": cambiumClientRxDataBytes,
       "cambiumWlanTable": cambiumWlanTable,
       "cambiumWlanEntry": cambiumWlanEntry,
       "cambiumWlanIndex": cambiumWlanIndex,
       "cambiumWlanSsid": cambiumWlanSsid,
       "cambiumWlanBand": cambiumWlanBand,
       "cambiumWlanVlan": cambiumWlanVlan,
       "cambiumWlanSecurity": cambiumWlanSecurity,
       "cambiumWlanGuestAccess": cambiumWlanGuestAccess,
       "cambiumWlanNumClients": cambiumWlanNumClients,
       "cambiumWlanTotalTxPackets": cambiumWlanTotalTxPackets,
       "cambiumWlanTxDataBytes": cambiumWlanTxDataBytes,
       "cambiumWlanTotalRxPackets": cambiumWlanTotalRxPackets,
       "cambiumWlanRxDataBytes": cambiumWlanRxDataBytes,
       "cambiumMeshClientTable": cambiumMeshClientTable,
       "cambiumMeshClientEntry": cambiumMeshClientEntry,
       "cambiumMeshClientMACAddressIndex": cambiumMeshClientMACAddressIndex,
       "cambiumMeshClientMACAddress": cambiumMeshClientMACAddress,
       "cambiumMeshClientBaseMACAddress": cambiumMeshClientBaseMACAddress,
       "cambiumMeshClientIPAddress": cambiumMeshClientIPAddress,
       "cambiumMeshClientName": cambiumMeshClientName,
       "cambiumMeshClientSsid": cambiumMeshClientSsid,
       "cambiumMeshClientRadioBand": cambiumMeshClientRadioBand,
       "cambiumMeshClientSNR": cambiumMeshClientSNR,
       "cambiumMeshClientRSSI": cambiumMeshClientRSSI,
       "cambiumMeshClientStatus": cambiumMeshClientStatus,
       "cambiumMeshClientDataRate": cambiumMeshClientDataRate,
       "cambiumMeshClientTotalTxPackets": cambiumMeshClientTotalTxPackets,
       "cambiumMeshClientTxDataBytes": cambiumMeshClientTxDataBytes,
       "cambiumMeshClientTotalRxPackets": cambiumMeshClientTotalRxPackets,
       "cambiumMeshClientRxDataBytes": cambiumMeshClientRxDataBytes,
       "cambiumAPSetIPAddress": cambiumAPSetIPAddress,
       "cambiumAPReboot": cambiumAPReboot}
)
