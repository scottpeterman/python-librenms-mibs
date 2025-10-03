# SNMP MIB module (MERU-CONFIG-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-CONFIG-WLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:14 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlACMSupportsBits,
 MwlAntennaLinkType,
 MwlAntennaSet,
 MwlAntennaSetLocation,
 MwlAntennaType,
 MwlApHwType,
 MwlApIfConfigModeType,
 MwlApIfModeType,
 MwlApMode,
 MwlApRfType,
 MwlArrayDataTypeAction,
 MwlAvailabilityStatus,
 MwlBandSteeringMode,
 MwlBgProtectionModeType,
 MwlBridgedVlanType,
 MwlChannelCenterFrequency,
 MwlChannelWidth,
 MwlDataplaneMode,
 MwlDaysOfTheWeekBits,
 MwlESSRFVirtualizationMode,
 MwlEnableDisableOption,
 MwlEssApAdminMode,
 MwlEssIdType,
 MwlHtProtectionModeType,
 MwlIFRFVirtualizationMode,
 MwlIfAdministrativeState,
 MwlL2BridgingsBits,
 MwlMimoMode,
 MwlNotificationSeverity,
 MwlNotificationType,
 MwlOnOffSwitch,
 MwlOperationalState,
 MwlPapBroadcastSsidMode,
 MwlProfileOwner,
 MwlPublishEssId,
 MwlTimerType,
 MwlTransmitRateAGBits,
 MwlTransmitRateBGBits,
 MwlTransmitRateBits,
 MwlTransmitRateHTBits,
 MwlTransmitRateVHT,
 MwlTxBeamSupport,
 MwlUplinkType,
 MwlVlanType,
 MwlVoiceClientType,
 MwlYesNoSwitch) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlACMSupportsBits",
    "MwlAntennaLinkType",
    "MwlAntennaSet",
    "MwlAntennaSetLocation",
    "MwlAntennaType",
    "MwlApHwType",
    "MwlApIfConfigModeType",
    "MwlApIfModeType",
    "MwlApMode",
    "MwlApRfType",
    "MwlArrayDataTypeAction",
    "MwlAvailabilityStatus",
    "MwlBandSteeringMode",
    "MwlBgProtectionModeType",
    "MwlBridgedVlanType",
    "MwlChannelCenterFrequency",
    "MwlChannelWidth",
    "MwlDataplaneMode",
    "MwlDaysOfTheWeekBits",
    "MwlESSRFVirtualizationMode",
    "MwlEnableDisableOption",
    "MwlEssApAdminMode",
    "MwlEssIdType",
    "MwlHtProtectionModeType",
    "MwlIFRFVirtualizationMode",
    "MwlIfAdministrativeState",
    "MwlL2BridgingsBits",
    "MwlMimoMode",
    "MwlNotificationSeverity",
    "MwlNotificationType",
    "MwlOnOffSwitch",
    "MwlOperationalState",
    "MwlPapBroadcastSsidMode",
    "MwlProfileOwner",
    "MwlPublishEssId",
    "MwlTimerType",
    "MwlTransmitRateAGBits",
    "MwlTransmitRateBGBits",
    "MwlTransmitRateBits",
    "MwlTransmitRateHTBits",
    "MwlTransmitRateVHT",
    "MwlTxBeamSupport",
    "MwlUplinkType",
    "MwlVlanType",
    "MwlVoiceClientType",
    "MwlYesNoSwitch")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigWlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwIf80211CapabilityTable_Object = MibTable
mwIf80211CapabilityTable = _MwIf80211CapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mwIf80211CapabilityTable.setStatus("current")
_MwIf80211CapabilityEntry_Object = MibTableRow
mwIf80211CapabilityEntry = _MwIf80211CapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1)
)
mwIf80211CapabilityEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwIf80211CapabilityTableIndex"),
)
if mibBuilder.loadTexts:
    mwIf80211CapabilityEntry.setStatus("current")
_MwIf80211CapabilityTableIndex_Type = Integer32
_MwIf80211CapabilityTableIndex_Object = MibTableColumn
mwIf80211CapabilityTableIndex = _MwIf80211CapabilityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 1),
    _MwIf80211CapabilityTableIndex_Type()
)
mwIf80211CapabilityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwIf80211CapabilityTableIndex.setStatus("current")
_MwIf80211CapabilityIfAGain_Type = Unsigned32
_MwIf80211CapabilityIfAGain_Object = MibTableColumn
mwIf80211CapabilityIfAGain = _MwIf80211CapabilityIfAGain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 2),
    _MwIf80211CapabilityIfAGain_Type()
)
mwIf80211CapabilityIfAGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAGain.setStatus("current")
_MwIf80211CapabilityIfBgGain_Type = Unsigned32
_MwIf80211CapabilityIfBgGain_Object = MibTableColumn
mwIf80211CapabilityIfBgGain = _MwIf80211CapabilityIfBgGain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 3),
    _MwIf80211CapabilityIfBgGain_Type()
)
mwIf80211CapabilityIfBgGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfBgGain.setStatus("current")
_MwIf80211CapabilityIfLinkType_Type = MwlAntennaLinkType
_MwIf80211CapabilityIfLinkType_Object = MibTableColumn
mwIf80211CapabilityIfLinkType = _MwIf80211CapabilityIfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 4),
    _MwIf80211CapabilityIfLinkType_Type()
)
mwIf80211CapabilityIfLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfLinkType.setStatus("current")
_MwIf80211CapabilityIfAntennaSet_Type = MwlAntennaSet
_MwIf80211CapabilityIfAntennaSet_Object = MibTableColumn
mwIf80211CapabilityIfAntennaSet = _MwIf80211CapabilityIfAntennaSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 5),
    _MwIf80211CapabilityIfAntennaSet_Type()
)
mwIf80211CapabilityIfAntennaSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAntennaSet.setStatus("current")
_MwIf80211CapabilityIfConnectorType_Type = MwlAntennaType
_MwIf80211CapabilityIfConnectorType_Object = MibTableColumn
mwIf80211CapabilityIfConnectorType = _MwIf80211CapabilityIfConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 6),
    _MwIf80211CapabilityIfConnectorType_Type()
)
mwIf80211CapabilityIfConnectorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfConnectorType.setStatus("current")
_MwIf80211CapabilityIfIndex_Type = Integer32
_MwIf80211CapabilityIfIndex_Object = MibTableColumn
mwIf80211CapabilityIfIndex = _MwIf80211CapabilityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 7),
    _MwIf80211CapabilityIfIndex_Type()
)
mwIf80211CapabilityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfIndex.setStatus("current")
_MwIf80211CapabilityApHwType_Type = MwlApHwType
_MwIf80211CapabilityApHwType_Object = MibTableColumn
mwIf80211CapabilityApHwType = _MwIf80211CapabilityApHwType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 8),
    _MwIf80211CapabilityApHwType_Type()
)
mwIf80211CapabilityApHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityApHwType.setStatus("current")
_MwIf80211CapabilityIfNmsNodeId_Type = Integer32
_MwIf80211CapabilityIfNmsNodeId_Object = MibTableColumn
mwIf80211CapabilityIfNmsNodeId = _MwIf80211CapabilityIfNmsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 9),
    _MwIf80211CapabilityIfNmsNodeId_Type()
)
mwIf80211CapabilityIfNmsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfNmsNodeId.setStatus("current")
_MwIf80211CapabilityIfConnectorGain_Type = Unsigned32
_MwIf80211CapabilityIfConnectorGain_Object = MibTableColumn
mwIf80211CapabilityIfConnectorGain = _MwIf80211CapabilityIfConnectorGain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 10),
    _MwIf80211CapabilityIfConnectorGain_Type()
)
mwIf80211CapabilityIfConnectorGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfConnectorGain.setStatus("current")
_MwIf80211CapabilityIfAntennaLocation_Type = MwlAntennaSetLocation
_MwIf80211CapabilityIfAntennaLocation_Object = MibTableColumn
mwIf80211CapabilityIfAntennaLocation = _MwIf80211CapabilityIfAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 11),
    _MwIf80211CapabilityIfAntennaLocation_Type()
)
mwIf80211CapabilityIfAntennaLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAntennaLocation.setStatus("current")
_MwIf80211CapabilityIfAntennaConnector_Type = Integer32
_MwIf80211CapabilityIfAntennaConnector_Object = MibTableColumn
mwIf80211CapabilityIfAntennaConnector = _MwIf80211CapabilityIfAntennaConnector_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 1, 1, 12),
    _MwIf80211CapabilityIfAntennaConnector_Type()
)
mwIf80211CapabilityIfAntennaConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211CapabilityIfAntennaConnector.setStatus("current")
_MwEssTable_Object = MibTable
mwEssTable = _MwEssTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    mwEssTable.setStatus("current")
_MwEssEntry_Object = MibTableRow
mwEssEntry = _MwEssEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1)
)
mwEssEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwEssTableIndex"),
)
if mibBuilder.loadTexts:
    mwEssEntry.setStatus("current")
_MwEssTableIndex_Type = Integer32
_MwEssTableIndex_Object = MibTableColumn
mwEssTableIndex = _MwEssTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 1),
    _MwEssTableIndex_Type()
)
mwEssTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwEssTableIndex.setStatus("current")


class _MwEssSsId_Type(DisplayString):
    """Custom type mwEssSsId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssSsId_Type.__name__ = "DisplayString"
_MwEssSsId_Object = MibTableColumn
mwEssSsId = _MwEssSsId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 2),
    _MwEssSsId_Type()
)
mwEssSsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSsId.setStatus("current")


class _MwEssId_Type(DisplayString):
    """Custom type mwEssId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwEssId_Type.__name__ = "DisplayString"
_MwEssId_Object = MibTableColumn
mwEssId = _MwEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 3),
    _MwEssId_Type()
)
mwEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssId.setStatus("current")


class _MwEssGreName_Type(DisplayString):
    """Custom type mwEssGreName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssGreName_Type.__name__ = "DisplayString"
_MwEssGreName_Object = MibTableColumn
mwEssGreName = _MwEssGreName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 4),
    _MwEssGreName_Type()
)
mwEssGreName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssGreName.setStatus("current")


class _MwEssVlanName_Type(DisplayString):
    """Custom type mwEssVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssVlanName_Type.__name__ = "DisplayString"
_MwEssVlanName_Object = MibTableColumn
mwEssVlanName = _MwEssVlanName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 5),
    _MwEssVlanName_Type()
)
mwEssVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVlanName.setStatus("current")
_MwEssL2Bridging_Type = MwlL2BridgingsBits
_MwEssL2Bridging_Object = MibTableColumn
mwEssL2Bridging = _MwEssL2Bridging_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 8),
    _MwEssL2Bridging_Type()
)
mwEssL2Bridging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssL2Bridging.setStatus("current")


class _MwEssDTIMPeriod_Type(Integer32):
    """Custom type mwEssDTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MwEssDTIMPeriod_Type.__name__ = "Integer32"
_MwEssDTIMPeriod_Object = MibTableColumn
mwEssDTIMPeriod = _MwEssDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 9),
    _MwEssDTIMPeriod_Type()
)
mwEssDTIMPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssDTIMPeriod.setStatus("current")
_MwEssVlanSupport_Type = MwlVlanType
_MwEssVlanSupport_Object = MibTableColumn
mwEssVlanSupport = _MwEssVlanSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 10),
    _MwEssVlanSupport_Type()
)
mwEssVlanSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVlanSupport.setStatus("current")
_MwEssBaseTxRates_Type = MwlTransmitRateBits
_MwEssBaseTxRates_Object = MibTableColumn
mwEssBaseTxRates = _MwEssBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 11),
    _MwEssBaseTxRates_Type()
)
mwEssBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBaseTxRates.setStatus("current")
_MwPublishEssId_Type = MwlPublishEssId
_MwPublishEssId_Object = MibTableColumn
mwPublishEssId = _MwPublishEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 12),
    _MwPublishEssId_Type()
)
mwPublishEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPublishEssId.setStatus("current")
_MwEssABaseTxRates_Type = MwlTransmitRateAGBits
_MwEssABaseTxRates_Object = MibTableColumn
mwEssABaseTxRates = _MwEssABaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 13),
    _MwEssABaseTxRates_Type()
)
mwEssABaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssABaseTxRates.setStatus("current")
_MwEssGBaseTxRates_Type = MwlTransmitRateAGBits
_MwEssGBaseTxRates_Object = MibTableColumn
mwEssGBaseTxRates = _MwEssGBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 14),
    _MwEssGBaseTxRates_Type()
)
mwEssGBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssGBaseTxRates.setStatus("current")
_MwEssDataplaneMode_Type = MwlDataplaneMode
_MwEssDataplaneMode_Object = MibTableColumn
mwEssDataplaneMode = _MwEssDataplaneMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 15),
    _MwEssDataplaneMode_Type()
)
mwEssDataplaneMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssDataplaneMode.setStatus("current")
_MwEssBGBaseTxRates_Type = MwlTransmitRateBGBits
_MwEssBGBaseTxRates_Object = MibTableColumn
mwEssBGBaseTxRates = _MwEssBGBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 16),
    _MwEssBGBaseTxRates_Type()
)
mwEssBGBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGBaseTxRates.setStatus("current")
_MwEssANBaseTxRates_Type = MwlTransmitRateAGBits
_MwEssANBaseTxRates_Object = MibTableColumn
mwEssANBaseTxRates = _MwEssANBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 17),
    _MwEssANBaseTxRates_Type()
)
mwEssANBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANBaseTxRates.setStatus("current")
_MwEssBeaconInterval_Type = Unsigned32
_MwEssBeaconInterval_Object = MibTableColumn
mwEssBeaconInterval = _MwEssBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 18),
    _MwEssBeaconInterval_Type()
)
mwEssBeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBeaconInterval.setStatus("current")
_MwEssAllowMulticast_Type = MwlOnOffSwitch
_MwEssAllowMulticast_Object = MibTableColumn
mwEssAllowMulticast = _MwEssAllowMulticast_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 19),
    _MwEssAllowMulticast_Type()
)
mwEssAllowMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssAllowMulticast.setStatus("current")
_MwEssBGNBaseTxRates_Type = MwlTransmitRateBGBits
_MwEssBGNBaseTxRates_Object = MibTableColumn
mwEssBGNBaseTxRates = _MwEssBGNBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 20),
    _MwEssBGNBaseTxRates_Type()
)
mwEssBGNBaseTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNBaseTxRates.setStatus("current")
_MwEssCountermeasure_Type = MwlOnOffSwitch
_MwEssCountermeasure_Object = MibTableColumn
mwEssCountermeasure = _MwEssCountermeasure_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 21),
    _MwEssCountermeasure_Type()
)
mwEssCountermeasure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssCountermeasure.setStatus("current")
_MwEssJoinOnDiscovery_Type = MwlOnOffSwitch
_MwEssJoinOnDiscovery_Object = MibTableColumn
mwEssJoinOnDiscovery = _MwEssJoinOnDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 22),
    _MwEssJoinOnDiscovery_Type()
)
mwEssJoinOnDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssJoinOnDiscovery.setStatus("current")
_MwEssANBaseHTTxRates_Type = MwlTransmitRateHTBits
_MwEssANBaseHTTxRates_Object = MibTableColumn
mwEssANBaseHTTxRates = _MwEssANBaseHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 23),
    _MwEssANBaseHTTxRates_Type()
)
mwEssANBaseHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANBaseHTTxRates.setStatus("current")
_MwEssSupportedTxRates_Type = MwlTransmitRateBits
_MwEssSupportedTxRates_Object = MibTableColumn
mwEssSupportedTxRates = _MwEssSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 24),
    _MwEssSupportedTxRates_Type()
)
mwEssSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSupportedTxRates.setStatus("current")
_MwEssBGNBaseHTTxRates_Type = MwlTransmitRateHTBits
_MwEssBGNBaseHTTxRates_Object = MibTableColumn
mwEssBGNBaseHTTxRates = _MwEssBGNBaseHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 25),
    _MwEssBGNBaseHTTxRates_Type()
)
mwEssBGNBaseHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNBaseHTTxRates.setStatus("current")
_MwEssASupportedTxRates_Type = MwlTransmitRateAGBits
_MwEssASupportedTxRates_Object = MibTableColumn
mwEssASupportedTxRates = _MwEssASupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 26),
    _MwEssASupportedTxRates_Type()
)
mwEssASupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssASupportedTxRates.setStatus("current")
_MwEssGSupportedTxRates_Type = MwlTransmitRateAGBits
_MwEssGSupportedTxRates_Object = MibTableColumn
mwEssGSupportedTxRates = _MwEssGSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 27),
    _MwEssGSupportedTxRates_Type()
)
mwEssGSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssGSupportedTxRates.setStatus("current")
_MwEssBGSupportedTxRates_Type = MwlTransmitRateBGBits
_MwEssBGSupportedTxRates_Object = MibTableColumn
mwEssBGSupportedTxRates = _MwEssBGSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 29),
    _MwEssBGSupportedTxRates_Type()
)
mwEssBGSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGSupportedTxRates.setStatus("current")
_MwEssANSupportedTxRates_Type = MwlTransmitRateAGBits
_MwEssANSupportedTxRates_Object = MibTableColumn
mwEssANSupportedTxRates = _MwEssANSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 30),
    _MwEssANSupportedTxRates_Type()
)
mwEssANSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANSupportedTxRates.setStatus("current")
_MwEssSecurityProfileName_Type = DisplayString
_MwEssSecurityProfileName_Object = MibTableColumn
mwEssSecurityProfileName = _MwEssSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 31),
    _MwEssSecurityProfileName_Type()
)
mwEssSecurityProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSecurityProfileName.setStatus("current")
_MwEssBGNSupportedTxRates_Type = MwlTransmitRateBGBits
_MwEssBGNSupportedTxRates_Object = MibTableColumn
mwEssBGNSupportedTxRates = _MwEssBGNSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 32),
    _MwEssBGNSupportedTxRates_Type()
)
mwEssBGNSupportedTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNSupportedTxRates.setStatus("current")
_MwEssANSupportedHTTxRates_Type = MwlTransmitRateHTBits
_MwEssANSupportedHTTxRates_Object = MibTableColumn
mwEssANSupportedHTTxRates = _MwEssANSupportedHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 33),
    _MwEssANSupportedHTTxRates_Type()
)
mwEssANSupportedHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssANSupportedHTTxRates.setStatus("current")
_MwEssBGNSupportedHTTxRates_Type = MwlTransmitRateHTBits
_MwEssBGNSupportedHTTxRates_Object = MibTableColumn
mwEssBGNSupportedHTTxRates = _MwEssBGNSupportedHTTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 34),
    _MwEssBGNSupportedHTTxRates_Type()
)
mwEssBGNSupportedHTTxRates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBGNSupportedHTTxRates.setStatus("current")
_MwEssAccountingInterimInterval_Type = Unsigned32
_MwEssAccountingInterimInterval_Object = MibTableColumn
mwEssAccountingInterimInterval = _MwEssAccountingInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 36),
    _MwEssAccountingInterimInterval_Type()
)
mwEssAccountingInterimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssAccountingInterimInterval.setStatus("current")
_MwEssPrimaryAccountingRadiusName_Type = DisplayString
_MwEssPrimaryAccountingRadiusName_Object = MibTableColumn
mwEssPrimaryAccountingRadiusName = _MwEssPrimaryAccountingRadiusName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 37),
    _MwEssPrimaryAccountingRadiusName_Type()
)
mwEssPrimaryAccountingRadiusName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssPrimaryAccountingRadiusName.setStatus("current")
_MwEssSecondaryAccountingRadiusName_Type = DisplayString
_MwEssSecondaryAccountingRadiusName_Object = MibTableColumn
mwEssSecondaryAccountingRadiusName = _MwEssSecondaryAccountingRadiusName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 38),
    _MwEssSecondaryAccountingRadiusName_Type()
)
mwEssSecondaryAccountingRadiusName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssSecondaryAccountingRadiusName.setStatus("current")
_MwEssMulticastMACTransparency_Type = MwlOnOffSwitch
_MwEssMulticastMACTransparency_Object = MibTableColumn
mwEssMulticastMACTransparency = _MwEssMulticastMACTransparency_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 39),
    _MwEssMulticastMACTransparency_Type()
)
mwEssMulticastMACTransparency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssMulticastMACTransparency.setStatus("current")
_MwEssBandSteering_Type = MwlBandSteeringMode
_MwEssBandSteering_Object = MibTableColumn
mwEssBandSteering = _MwEssBandSteering_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 43),
    _MwEssBandSteering_Type()
)
mwEssBandSteering.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBandSteering.setStatus("current")
_MwEssBandSteeringTimeout_Type = Unsigned32
_MwEssBandSteeringTimeout_Object = MibTableColumn
mwEssBandSteeringTimeout = _MwEssBandSteeringTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 44),
    _MwEssBandSteeringTimeout_Type()
)
mwEssBandSteeringTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssBandSteeringTimeout.setStatus("current")
_MwEssApVlanTag_Type = Unsigned32
_MwEssApVlanTag_Object = MibTableColumn
mwEssApVlanTag = _MwEssApVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 45),
    _MwEssApVlanTag_Type()
)
mwEssApVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApVlanTag.setStatus("current")
_MwEssEnableApVlanPriority_Type = MwlOnOffSwitch
_MwEssEnableApVlanPriority_Object = MibTableColumn
mwEssEnableApVlanPriority = _MwEssEnableApVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 46),
    _MwEssEnableApVlanPriority_Type()
)
mwEssEnableApVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssEnableApVlanPriority.setStatus("current")
_MwEssOwner_Type = MwlProfileOwner
_MwEssOwner_Object = MibTableColumn
mwEssOwner = _MwEssOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 47),
    _MwEssOwner_Type()
)
mwEssOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssOwner.setStatus("current")
_MwEssEnableAPSD_Type = MwlOnOffSwitch
_MwEssEnableAPSD_Object = MibTableColumn
mwEssEnableAPSD = _MwEssEnableAPSD_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 49),
    _MwEssEnableAPSD_Type()
)
mwEssEnableAPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssEnableAPSD.setStatus("current")
_MwEssState_Type = MwlEnableDisableOption
_MwEssState_Object = MibTableColumn
mwEssState = _MwEssState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 50),
    _MwEssState_Type()
)
mwEssState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssState.setStatus("current")
_MwEssMulticastToUnicastConversion_Type = MwlOnOffSwitch
_MwEssMulticastToUnicastConversion_Object = MibTableColumn
mwEssMulticastToUnicastConversion = _MwEssMulticastToUnicastConversion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 52),
    _MwEssMulticastToUnicastConversion_Type()
)
mwEssMulticastToUnicastConversion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssMulticastToUnicastConversion.setStatus("current")
_MwEssEfOverride_Type = MwlOnOffSwitch
_MwEssEfOverride_Object = MibTableColumn
mwEssEfOverride = _MwEssEfOverride_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 53),
    _MwEssEfOverride_Type()
)
mwEssEfOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssEfOverride.setStatus("current")
_MwEssPapBroadcastSsid_Type = MwlPapBroadcastSsidMode
_MwEssPapBroadcastSsid_Object = MibTableColumn
mwEssPapBroadcastSsid = _MwEssPapBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 54),
    _MwEssPapBroadcastSsid_Type()
)
mwEssPapBroadcastSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssPapBroadcastSsid.setStatus("current")


class _MwEssVirtualInterfaceProfileName_Type(DisplayString):
    """Custom type mwEssVirtualInterfaceProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssVirtualInterfaceProfileName_Type.__name__ = "DisplayString"
_MwEssVirtualInterfaceProfileName_Object = MibTableColumn
mwEssVirtualInterfaceProfileName = _MwEssVirtualInterfaceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 56),
    _MwEssVirtualInterfaceProfileName_Type()
)
mwEssVirtualInterfaceProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVirtualInterfaceProfileName.setStatus("current")
_MwEssWirelessToWirelessIsolation_Type = MwlOnOffSwitch
_MwEssWirelessToWirelessIsolation_Object = MibTableColumn
mwEssWirelessToWirelessIsolation = _MwEssWirelessToWirelessIsolation_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 58),
    _MwEssWirelessToWirelessIsolation_Type()
)
mwEssWirelessToWirelessIsolation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssWirelessToWirelessIsolation.setStatus("current")
_MwEssRFVMode_Type = MwlESSRFVirtualizationMode
_MwEssRFVMode_Object = MibTableColumn
mwEssRFVMode = _MwEssRFVMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 59),
    _MwEssRFVMode_Type()
)
mwEssRFVMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssRFVMode.setStatus("current")
_MwEssS1VHTBaseMCSSet_Type = MwlTransmitRateVHT
_MwEssS1VHTBaseMCSSet_Object = MibTableColumn
mwEssS1VHTBaseMCSSet = _MwEssS1VHTBaseMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 62),
    _MwEssS1VHTBaseMCSSet_Type()
)
mwEssS1VHTBaseMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS1VHTBaseMCSSet.setStatus("current")
_MwEssS2VHTBaseMCSSet_Type = MwlTransmitRateVHT
_MwEssS2VHTBaseMCSSet_Object = MibTableColumn
mwEssS2VHTBaseMCSSet = _MwEssS2VHTBaseMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 63),
    _MwEssS2VHTBaseMCSSet_Type()
)
mwEssS2VHTBaseMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS2VHTBaseMCSSet.setStatus("current")
_MwEssS3VHTBaseMCSSet_Type = MwlTransmitRateVHT
_MwEssS3VHTBaseMCSSet_Object = MibTableColumn
mwEssS3VHTBaseMCSSet = _MwEssS3VHTBaseMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 64),
    _MwEssS3VHTBaseMCSSet_Type()
)
mwEssS3VHTBaseMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS3VHTBaseMCSSet.setStatus("current")
_MwEssS1VHTSupportMCSSet_Type = MwlTransmitRateVHT
_MwEssS1VHTSupportMCSSet_Object = MibTableColumn
mwEssS1VHTSupportMCSSet = _MwEssS1VHTSupportMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 65),
    _MwEssS1VHTSupportMCSSet_Type()
)
mwEssS1VHTSupportMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS1VHTSupportMCSSet.setStatus("current")
_MwEssS2VHTSupportMCSSet_Type = MwlTransmitRateVHT
_MwEssS2VHTSupportMCSSet_Object = MibTableColumn
mwEssS2VHTSupportMCSSet = _MwEssS2VHTSupportMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 66),
    _MwEssS2VHTSupportMCSSet_Type()
)
mwEssS2VHTSupportMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS2VHTSupportMCSSet.setStatus("current")
_MwEssS3VHTSupportMCSSet_Type = MwlTransmitRateVHT
_MwEssS3VHTSupportMCSSet_Object = MibTableColumn
mwEssS3VHTSupportMCSSet = _MwEssS3VHTSupportMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 67),
    _MwEssS3VHTSupportMCSSet_Type()
)
mwEssS3VHTSupportMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS3VHTSupportMCSSet.setStatus("current")
_MwEssApVlanPolicy_Type = MwlBridgedVlanType
_MwEssApVlanPolicy_Object = MibTableColumn
mwEssApVlanPolicy = _MwEssApVlanPolicy_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 68),
    _MwEssApVlanPolicy_Type()
)
mwEssApVlanPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApVlanPolicy.setStatus("current")
_MwEssVoiceClientType_Type = MwlVoiceClientType
_MwEssVoiceClientType_Object = MibTableColumn
mwEssVoiceClientType = _MwEssVoiceClientType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 70),
    _MwEssVoiceClientType_Type()
)
mwEssVoiceClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVoiceClientType.setStatus("current")
_MwEssIpPrefixLookup_Type = MwlOnOffSwitch
_MwEssIpPrefixLookup_Object = MibTableColumn
mwEssIpPrefixLookup = _MwEssIpPrefixLookup_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 71),
    _MwEssIpPrefixLookup_Type()
)
mwEssIpPrefixLookup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssIpPrefixLookup.setStatus("current")
_MwEssFastHandoff_Type = MwlOnOffSwitch
_MwEssFastHandoff_Object = MibTableColumn
mwEssFastHandoff = _MwEssFastHandoff_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 72),
    _MwEssFastHandoff_Type()
)
mwEssFastHandoff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssFastHandoff.setStatus("current")


class _MwEssMobilityDomain_Type(Integer32):
    """Custom type mwEssMobilityDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MwEssMobilityDomain_Type.__name__ = "Integer32"
_MwEssMobilityDomain_Object = MibTableColumn
mwEssMobilityDomain = _MwEssMobilityDomain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 73),
    _MwEssMobilityDomain_Type()
)
mwEssMobilityDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssMobilityDomain.setStatus("current")


class _MwEssVlanPoolName_Type(DisplayString):
    """Custom type mwEssVlanPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwEssVlanPoolName_Type.__name__ = "DisplayString"
_MwEssVlanPoolName_Object = MibTableColumn
mwEssVlanPoolName = _MwEssVlanPoolName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 74),
    _MwEssVlanPoolName_Type()
)
mwEssVlanPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssVlanPoolName.setStatus("current")
_MwEssDot11kEnabled_Type = MwlOnOffSwitch
_MwEssDot11kEnabled_Object = MibTableColumn
mwEssDot11kEnabled = _MwEssDot11kEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 76),
    _MwEssDot11kEnabled_Type()
)
mwEssDot11kEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssDot11kEnabled.setStatus("current")
_MwEssTimerProfileName_Type = DisplayString
_MwEssTimerProfileName_Object = MibTableColumn
mwEssTimerProfileName = _MwEssTimerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 77),
    _MwEssTimerProfileName_Type()
)
mwEssTimerProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssTimerProfileName.setStatus("current")
_MwEssIdType_Type = MwlEssIdType
_MwEssIdType_Object = MibTableColumn
mwEssIdType = _MwEssIdType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 79),
    _MwEssIdType_Type()
)
mwEssIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssIdType.setStatus("current")


class _MwBackupEssId_Type(DisplayString):
    """Custom type mwBackupEssId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwBackupEssId_Type.__name__ = "DisplayString"
_MwBackupEssId_Object = MibTableColumn
mwBackupEssId = _MwBackupEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 80),
    _MwBackupEssId_Type()
)
mwBackupEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwBackupEssId.setStatus("current")
_MwEssACMSupport_Type = MwlACMSupportsBits
_MwEssACMSupport_Object = MibTableColumn
mwEssACMSupport = _MwEssACMSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 82),
    _MwEssACMSupport_Type()
)
mwEssACMSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssACMSupport.setStatus("current")
_MwEssS4VHTBaseMCSSet_Type = MwlTransmitRateVHT
_MwEssS4VHTBaseMCSSet_Object = MibTableColumn
mwEssS4VHTBaseMCSSet = _MwEssS4VHTBaseMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 83),
    _MwEssS4VHTBaseMCSSet_Type()
)
mwEssS4VHTBaseMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS4VHTBaseMCSSet.setStatus("current")
_MwEssS4VHTSupportMCSSet_Type = MwlTransmitRateVHT
_MwEssS4VHTSupportMCSSet_Object = MibTableColumn
mwEssS4VHTSupportMCSSet = _MwEssS4VHTSupportMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 84),
    _MwEssS4VHTSupportMCSSet_Type()
)
mwEssS4VHTSupportMCSSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssS4VHTSupportMCSSet.setStatus("current")
_MwEssQamSupport_Type = MwlOnOffSwitch
_MwEssQamSupport_Object = MibTableColumn
mwEssQamSupport = _MwEssQamSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 85),
    _MwEssQamSupport_Type()
)
mwEssQamSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssQamSupport.setStatus("current")


class _MwEssReconnectPrimaryServer_Type(Integer32):
    """Custom type mwEssReconnectPrimaryServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_MwEssReconnectPrimaryServer_Type.__name__ = "Integer32"
_MwEssReconnectPrimaryServer_Object = MibTableColumn
mwEssReconnectPrimaryServer = _MwEssReconnectPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 86),
    _MwEssReconnectPrimaryServer_Type()
)
mwEssReconnectPrimaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssReconnectPrimaryServer.setStatus("current")
_MwEssRowStatus_Type = RowStatus
_MwEssRowStatus_Object = MibTableColumn
mwEssRowStatus = _MwEssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 2, 1, 88),
    _MwEssRowStatus_Type()
)
mwEssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssRowStatus.setStatus("current")
_MwIf80211Table_Object = MibTable
mwIf80211Table = _MwIf80211Table_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    mwIf80211Table.setStatus("current")
_MwIf80211Entry_Object = MibTableRow
mwIf80211Entry = _MwIf80211Entry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1)
)
mwIf80211Entry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwIf80211TableIndex"),
)
if mibBuilder.loadTexts:
    mwIf80211Entry.setStatus("current")
_MwIf80211TableIndex_Type = Integer32
_MwIf80211TableIndex_Object = MibTableColumn
mwIf80211TableIndex = _MwIf80211TableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 1),
    _MwIf80211TableIndex_Type()
)
mwIf80211TableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwIf80211TableIndex.setStatus("current")
_MwIf80211IfMode_Type = MwlApIfConfigModeType
_MwIf80211IfMode_Object = MibTableColumn
mwIf80211IfMode = _MwIf80211IfMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 2),
    _MwIf80211IfMode_Type()
)
mwIf80211IfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfMode.setStatus("current")


class _MwIf80211IfDescr_Type(DisplayString):
    """Custom type mwIf80211IfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MwIf80211IfDescr_Type.__name__ = "DisplayString"
_MwIf80211IfDescr_Object = MibTableColumn
mwIf80211IfDescr = _MwIf80211IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 3),
    _MwIf80211IfDescr_Type()
)
mwIf80211IfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfDescr.setStatus("current")
_MwIf80211IfApMode_Type = MwlApMode
_MwIf80211IfApMode_Object = MibTableColumn
mwIf80211IfApMode = _MwIf80211IfApMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 4),
    _MwIf80211IfApMode_Type()
)
mwIf80211IfApMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfApMode.setStatus("current")
_MwIf80211IfChannel_Type = Integer32
_MwIf80211IfChannel_Object = MibTableColumn
mwIf80211IfChannel = _MwIf80211IfChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 5),
    _MwIf80211IfChannel_Type()
)
mwIf80211IfChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfChannel.setStatus("current")
_MwIf80211NOnlyMode_Type = MwlOnOffSwitch
_MwIf80211NOnlyMode_Object = MibTableColumn
mwIf80211NOnlyMode = _MwIf80211NOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 7),
    _MwIf80211NOnlyMode_Type()
)
mwIf80211NOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211NOnlyMode.setStatus("current")
_MwIf80211IfMimoMode_Type = MwlMimoMode
_MwIf80211IfMimoMode_Object = MibTableColumn
mwIf80211IfMimoMode = _MwIf80211IfMimoMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 11),
    _MwIf80211IfMimoMode_Type()
)
mwIf80211IfMimoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfMimoMode.setStatus("current")
_MwIf80211channelWidth_Type = MwlChannelWidth
_MwIf80211channelWidth_Object = MibTableColumn
mwIf80211channelWidth = _MwIf80211channelWidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 13),
    _MwIf80211channelWidth_Type()
)
mwIf80211channelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211channelWidth.setStatus("current")
_MwIf80211IfAdminStatus_Type = MwlIfAdministrativeState
_MwIf80211IfAdminStatus_Object = MibTableColumn
mwIf80211IfAdminStatus = _MwIf80211IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 17),
    _MwIf80211IfAdminStatus_Type()
)
mwIf80211IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfAdminStatus.setStatus("current")
_MwIf80211IfTxPowerHigh_Type = Integer32
_MwIf80211IfTxPowerHigh_Object = MibTableColumn
mwIf80211IfTxPowerHigh = _MwIf80211IfTxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 18),
    _MwIf80211IfTxPowerHigh_Type()
)
mwIf80211IfTxPowerHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfTxPowerHigh.setStatus("current")
_MwIf80211IfBgProtectionMode_Type = MwlBgProtectionModeType
_MwIf80211IfBgProtectionMode_Object = MibTableColumn
mwIf80211IfBgProtectionMode = _MwIf80211IfBgProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 19),
    _MwIf80211IfBgProtectionMode_Type()
)
mwIf80211IfBgProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfBgProtectionMode.setStatus("current")
_MwIf80211IfShortPreambleFlag_Type = MwlOnOffSwitch
_MwIf80211IfShortPreambleFlag_Object = MibTableColumn
mwIf80211IfShortPreambleFlag = _MwIf80211IfShortPreambleFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 20),
    _MwIf80211IfShortPreambleFlag_Type()
)
mwIf80211IfShortPreambleFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfShortPreambleFlag.setStatus("current")
_MwIf80211IfMtu_Type = Unsigned32
_MwIf80211IfMtu_Object = MibTableColumn
mwIf80211IfMtu = _MwIf80211IfMtu_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 21),
    _MwIf80211IfMtu_Type()
)
mwIf80211IfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfMtu.setStatus("current")
_MwIf80211IfType_Type = MwlApRfType
_MwIf80211IfType_Object = MibTableColumn
mwIf80211IfType = _MwIf80211IfType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 22),
    _MwIf80211IfType_Type()
)
mwIf80211IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfType.setStatus("current")
_MwIf80211IfIndex_Type = Integer32
_MwIf80211IfIndex_Object = MibTableColumn
mwIf80211IfIndex = _MwIf80211IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 23),
    _MwIf80211IfIndex_Type()
)
mwIf80211IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfIndex.setStatus("current")
_MwIf80211IfNodeId_Type = Unsigned32
_MwIf80211IfNodeId_Object = MibTableColumn
mwIf80211IfNodeId = _MwIf80211IfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 24),
    _MwIf80211IfNodeId_Type()
)
mwIf80211IfNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfNodeId.setStatus("current")
_MwIf80211ApHwType_Type = MwlApHwType
_MwIf80211ApHwType_Object = MibTableColumn
mwIf80211ApHwType = _MwIf80211ApHwType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 25),
    _MwIf80211ApHwType_Type()
)
mwIf80211ApHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211ApHwType.setStatus("current")
_MwIf80211IfNodeName_Type = DisplayString
_MwIf80211IfNodeName_Object = MibTableColumn
mwIf80211IfNodeName = _MwIf80211IfNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 26),
    _MwIf80211IfNodeName_Type()
)
mwIf80211IfNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfNodeName.setStatus("current")
_MwIf80211IfOperStatus_Type = MwlOperationalState
_MwIf80211IfOperStatus_Object = MibTableColumn
mwIf80211IfOperStatus = _MwIf80211IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 27),
    _MwIf80211IfOperStatus_Type()
)
mwIf80211IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfOperStatus.setStatus("current")
_MwIf80211IfLastChange_Type = DateAndTime
_MwIf80211IfLastChange_Object = MibTableColumn
mwIf80211IfLastChange = _MwIf80211IfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 28),
    _MwIf80211IfLastChange_Type()
)
mwIf80211IfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfLastChange.setStatus("current")
_MwIf80211IfOperChannel_Type = Integer32
_MwIf80211IfOperChannel_Object = MibTableColumn
mwIf80211IfOperChannel = _MwIf80211IfOperChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 29),
    _MwIf80211IfOperChannel_Type()
)
mwIf80211IfOperChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfOperChannel.setStatus("current")
_MwIf80211IfBandSupport_Type = MwlApIfModeType
_MwIf80211IfBandSupport_Object = MibTableColumn
mwIf80211IfBandSupport = _MwIf80211IfBandSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 30),
    _MwIf80211IfBandSupport_Type()
)
mwIf80211IfBandSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfBandSupport.setStatus("current")
_MwIf80211IfNumAntennas_Type = Integer32
_MwIf80211IfNumAntennas_Object = MibTableColumn
mwIf80211IfNumAntennas = _MwIf80211IfNumAntennas_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 40),
    _MwIf80211IfNumAntennas_Type()
)
mwIf80211IfNumAntennas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211IfNumAntennas.setStatus("current")
_MwIf80211ProbeResponseThreshold_Type = Unsigned32
_MwIf80211ProbeResponseThreshold_Object = MibTableColumn
mwIf80211ProbeResponseThreshold = _MwIf80211ProbeResponseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 42),
    _MwIf80211ProbeResponseThreshold_Type()
)
mwIf80211ProbeResponseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211ProbeResponseThreshold.setStatus("current")
_MwIf80211IfMeshStatus_Type = MwlEnableDisableOption
_MwIf80211IfMeshStatus_Object = MibTableColumn
mwIf80211IfMeshStatus = _MwIf80211IfMeshStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 44),
    _MwIf80211IfMeshStatus_Type()
)
mwIf80211IfMeshStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfMeshStatus.setStatus("current")
_MwIf80211UplinkType_Type = MwlUplinkType
_MwIf80211UplinkType_Object = MibTableColumn
mwIf80211UplinkType = _MwIf80211UplinkType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 45),
    _MwIf80211UplinkType_Type()
)
mwIf80211UplinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211UplinkType.setStatus("current")
_MwIf80211IfHtProtectionMode_Type = MwlHtProtectionModeType
_MwIf80211IfHtProtectionMode_Object = MibTableColumn
mwIf80211IfHtProtectionMode = _MwIf80211IfHtProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 46),
    _MwIf80211IfHtProtectionMode_Type()
)
mwIf80211IfHtProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfHtProtectionMode.setStatus("current")
_MwIf80211IfFallbackChannel_Type = Integer32
_MwIf80211IfFallbackChannel_Object = MibTableColumn
mwIf80211IfFallbackChannel = _MwIf80211IfFallbackChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 47),
    _MwIf80211IfFallbackChannel_Type()
)
mwIf80211IfFallbackChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfFallbackChannel.setStatus("current")
_MwIf80211RFVMode_Type = MwlIFRFVirtualizationMode
_MwIf80211RFVMode_Object = MibTableColumn
mwIf80211RFVMode = _MwIf80211RFVMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 48),
    _MwIf80211RFVMode_Type()
)
mwIf80211RFVMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211RFVMode.setStatus("current")
_MwIf80211ChannelCenterFrequency_Type = MwlChannelCenterFrequency
_MwIf80211ChannelCenterFrequency_Object = MibTableColumn
mwIf80211ChannelCenterFrequency = _MwIf80211ChannelCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 49),
    _MwIf80211ChannelCenterFrequency_Type()
)
mwIf80211ChannelCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211ChannelCenterFrequency.setStatus("current")
_MwIf80211TransmitBeamformingSupport_Type = MwlTxBeamSupport
_MwIf80211TransmitBeamformingSupport_Object = MibTableColumn
mwIf80211TransmitBeamformingSupport = _MwIf80211TransmitBeamformingSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 50),
    _MwIf80211TransmitBeamformingSupport_Type()
)
mwIf80211TransmitBeamformingSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211TransmitBeamformingSupport.setStatus("current")
_MwIf80211STBCSupport_Type = MwlOnOffSwitch
_MwIf80211STBCSupport_Object = MibTableColumn
mwIf80211STBCSupport = _MwIf80211STBCSupport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 51),
    _MwIf80211STBCSupport_Type()
)
mwIf80211STBCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211STBCSupport.setStatus("current")
_MwIf80211DFSFallbackOption_Type = MwlEnableDisableOption
_MwIf80211DFSFallbackOption_Object = MibTableColumn
mwIf80211DFSFallbackOption = _MwIf80211DFSFallbackOption_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 52),
    _MwIf80211DFSFallbackOption_Type()
)
mwIf80211DFSFallbackOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211DFSFallbackOption.setStatus("current")


class _MwIf80211DFSChanRevertive_Type(Integer32):
    """Custom type mwIf80211DFSChanRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_MwIf80211DFSChanRevertive_Type.__name__ = "Integer32"
_MwIf80211DFSChanRevertive_Object = MibTableColumn
mwIf80211DFSChanRevertive = _MwIf80211DFSChanRevertive_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 53),
    _MwIf80211DFSChanRevertive_Type()
)
mwIf80211DFSChanRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211DFSChanRevertive.setStatus("current")
_MwIf80211FallbackChannelCenterFrequency_Type = MwlChannelCenterFrequency
_MwIf80211FallbackChannelCenterFrequency_Object = MibTableColumn
mwIf80211FallbackChannelCenterFrequency = _MwIf80211FallbackChannelCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 54),
    _MwIf80211FallbackChannelCenterFrequency_Type()
)
mwIf80211FallbackChannelCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211FallbackChannelCenterFrequency.setStatus("current")
_MwIf80211IfVhtStatus_Type = MwlEnableDisableOption
_MwIf80211IfVhtStatus_Object = MibTableColumn
mwIf80211IfVhtStatus = _MwIf80211IfVhtStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 3, 1, 55),
    _MwIf80211IfVhtStatus_Type()
)
mwIf80211IfVhtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwIf80211IfVhtStatus.setStatus("current")
_MwEssApTable_Object = MibTable
mwEssApTable = _MwEssApTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    mwEssApTable.setStatus("current")
_MwEssApEntry_Object = MibTableRow
mwEssApEntry = _MwEssApEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1)
)
mwEssApEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwEssApTableIndex"),
)
if mibBuilder.loadTexts:
    mwEssApEntry.setStatus("current")
_MwEssApTableIndex_Type = Integer32
_MwEssApTableIndex_Object = MibTableColumn
mwEssApTableIndex = _MwEssApTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 1),
    _MwEssApTableIndex_Type()
)
mwEssApTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwEssApTableIndex.setStatus("current")
_MwEssApEssId_Type = DisplayString
_MwEssApEssId_Object = MibTableColumn
mwEssApEssId = _MwEssApEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 2),
    _MwEssApEssId_Type()
)
mwEssApEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApEssId.setStatus("current")
_MwEssApIfIndex_Type = Integer32
_MwEssApIfIndex_Object = MibTableColumn
mwEssApIfIndex = _MwEssApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 3),
    _MwEssApIfIndex_Type()
)
mwEssApIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApIfIndex.setStatus("current")
_MwEssApMaxCalls_Type = Unsigned32
_MwEssApMaxCalls_Object = MibTableColumn
mwEssApMaxCalls = _MwEssApMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 4),
    _MwEssApMaxCalls_Type()
)
mwEssApMaxCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApMaxCalls.setStatus("current")


class _MwEssApApNodeId_Type(Integer32):
    """Custom type mwEssApApNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MwEssApApNodeId_Type.__name__ = "Integer32"
_MwEssApApNodeId_Object = MibTableColumn
mwEssApApNodeId = _MwEssApApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 5),
    _MwEssApApNodeId_Type()
)
mwEssApApNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApApNodeId.setStatus("current")
_MwEssApBssId_Type = MacAddress
_MwEssApBssId_Object = MibTableColumn
mwEssApBssId = _MwEssApBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 6),
    _MwEssApBssId_Type()
)
mwEssApBssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApBssId.setStatus("current")
_MwEssApIfMode_Type = MwlApIfConfigModeType
_MwEssApIfMode_Object = MibTableColumn
mwEssApIfMode = _MwEssApIfMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 7),
    _MwEssApIfMode_Type()
)
mwEssApIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApIfMode.setStatus("current")
_MwEssApApNodeName_Type = DisplayString
_MwEssApApNodeName_Object = MibTableColumn
mwEssApApNodeName = _MwEssApApNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 8),
    _MwEssApApNodeName_Type()
)
mwEssApApNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApApNodeName.setStatus("current")
_MwEssApBaseTxRates_Type = MwlTransmitRateBGBits
_MwEssApBaseTxRates_Object = MibTableColumn
mwEssApBaseTxRates = _MwEssApBaseTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 9),
    _MwEssApBaseTxRates_Type()
)
mwEssApBaseTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApBaseTxRates.setStatus("current")
_MwEssApChannelNumber_Type = Integer32
_MwEssApChannelNumber_Object = MibTableColumn
mwEssApChannelNumber = _MwEssApChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 10),
    _MwEssApChannelNumber_Type()
)
mwEssApChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApChannelNumber.setStatus("current")
_MwEssApIfOperChannel_Type = Integer32
_MwEssApIfOperChannel_Object = MibTableColumn
mwEssApIfOperChannel = _MwEssApIfOperChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 11),
    _MwEssApIfOperChannel_Type()
)
mwEssApIfOperChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApIfOperChannel.setStatus("current")
_MwEssApSupportedTxRates_Type = MwlTransmitRateBGBits
_MwEssApSupportedTxRates_Object = MibTableColumn
mwEssApSupportedTxRates = _MwEssApSupportedTxRates_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 12),
    _MwEssApSupportedTxRates_Type()
)
mwEssApSupportedTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApSupportedTxRates.setStatus("current")
_MwEssApAdminMode_Type = MwlEssApAdminMode
_MwEssApAdminMode_Object = MibTableColumn
mwEssApAdminMode = _MwEssApAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 13),
    _MwEssApAdminMode_Type()
)
mwEssApAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssApAdminMode.setStatus("current")
_MwEssApRowStatus_Type = RowStatus
_MwEssApRowStatus_Object = MibTableColumn
mwEssApRowStatus = _MwEssApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 4, 1, 14),
    _MwEssApRowStatus_Type()
)
mwEssApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwEssApRowStatus.setStatus("current")
_MwMeshProfileTable_Object = MibTable
mwMeshProfileTable = _MwMeshProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7)
)
if mibBuilder.loadTexts:
    mwMeshProfileTable.setStatus("current")
_MwMeshProfileEntry_Object = MibTableRow
mwMeshProfileEntry = _MwMeshProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1)
)
mwMeshProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwMeshProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwMeshProfileEntry.setStatus("current")
_MwMeshProfileTableIndex_Type = Integer32
_MwMeshProfileTableIndex_Object = MibTableColumn
mwMeshProfileTableIndex = _MwMeshProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 1),
    _MwMeshProfileTableIndex_Type()
)
mwMeshProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwMeshProfileTableIndex.setStatus("current")


class _MwMeshProfileName_Type(DisplayString):
    """Custom type mwMeshProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwMeshProfileName_Type.__name__ = "DisplayString"
_MwMeshProfileName_Object = MibTableColumn
mwMeshProfileName = _MwMeshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 2),
    _MwMeshProfileName_Type()
)
mwMeshProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileName.setStatus("current")


class _MwMeshProfileDescr_Type(DisplayString):
    """Custom type mwMeshProfileDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MwMeshProfileDescr_Type.__name__ = "DisplayString"
_MwMeshProfileDescr_Object = MibTableColumn
mwMeshProfileDescr = _MwMeshProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 3),
    _MwMeshProfileDescr_Type()
)
mwMeshProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileDescr.setStatus("current")


class _MwMeshProfilePSK_Type(DisplayString):
    """Custom type mwMeshProfilePSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_MwMeshProfilePSK_Type.__name__ = "DisplayString"
_MwMeshProfilePSK_Object = MibTableColumn
mwMeshProfilePSK = _MwMeshProfilePSK_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 4),
    _MwMeshProfilePSK_Type()
)
mwMeshProfilePSK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfilePSK.setStatus("current")
_MwMeshProfileAdminMode_Type = MwlEnableDisableOption
_MwMeshProfileAdminMode_Object = MibTableColumn
mwMeshProfileAdminMode = _MwMeshProfileAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 5),
    _MwMeshProfileAdminMode_Type()
)
mwMeshProfileAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileAdminMode.setStatus("current")
_MwMeshProfilePlugNPlayStatus_Type = MwlEnableDisableOption
_MwMeshProfilePlugNPlayStatus_Object = MibTableColumn
mwMeshProfilePlugNPlayStatus = _MwMeshProfilePlugNPlayStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 6),
    _MwMeshProfilePlugNPlayStatus_Type()
)
mwMeshProfilePlugNPlayStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfilePlugNPlayStatus.setStatus("current")
_MwMeshProfileMeshVlanTrunk_Type = MwlEnableDisableOption
_MwMeshProfileMeshVlanTrunk_Object = MibTableColumn
mwMeshProfileMeshVlanTrunk = _MwMeshProfileMeshVlanTrunk_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 7),
    _MwMeshProfileMeshVlanTrunk_Type()
)
mwMeshProfileMeshVlanTrunk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileMeshVlanTrunk.setStatus("current")
_MwMeshProfileRowStatus_Type = RowStatus
_MwMeshProfileRowStatus_Object = MibTableColumn
mwMeshProfileRowStatus = _MwMeshProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 7, 1, 25),
    _MwMeshProfileRowStatus_Type()
)
mwMeshProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshProfileRowStatus.setStatus("current")
_MwMeshApTable_Object = MibTable
mwMeshApTable = _MwMeshApTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8)
)
if mibBuilder.loadTexts:
    mwMeshApTable.setStatus("current")
_MwMeshApEntry_Object = MibTableRow
mwMeshApEntry = _MwMeshApEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1)
)
mwMeshApEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwMeshApTableIndex"),
)
if mibBuilder.loadTexts:
    mwMeshApEntry.setStatus("current")
_MwMeshApTableIndex_Type = Integer32
_MwMeshApTableIndex_Object = MibTableColumn
mwMeshApTableIndex = _MwMeshApTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 1),
    _MwMeshApTableIndex_Type()
)
mwMeshApTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwMeshApTableIndex.setStatus("current")


class _MwMeshApName_Type(DisplayString):
    """Custom type mwMeshApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwMeshApName_Type.__name__ = "DisplayString"
_MwMeshApName_Object = MibTableColumn
mwMeshApName = _MwMeshApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 2),
    _MwMeshApName_Type()
)
mwMeshApName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshApName.setStatus("current")
_MwMeshApAPId_Type = Integer32
_MwMeshApAPId_Object = MibTableColumn
mwMeshApAPId = _MwMeshApAPId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 3),
    _MwMeshApAPId_Type()
)
mwMeshApAPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshApAPId.setStatus("current")
_MwMeshApAPMac_Type = MacAddress
_MwMeshApAPMac_Object = MibTableColumn
mwMeshApAPMac = _MwMeshApAPMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 4),
    _MwMeshApAPMac_Type()
)
mwMeshApAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApAPMac.setStatus("current")
_MwMeshApAvailState_Type = MwlAvailabilityStatus
_MwMeshApAvailState_Object = MibTableColumn
mwMeshApAvailState = _MwMeshApAvailState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 5),
    _MwMeshApAvailState_Type()
)
mwMeshApAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApAvailState.setStatus("current")
_MwMeshApParentAPId_Type = Integer32
_MwMeshApParentAPId_Object = MibTableColumn
mwMeshApParentAPId = _MwMeshApParentAPId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 6),
    _MwMeshApParentAPId_Type()
)
mwMeshApParentAPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApParentAPId.setStatus("current")
_MwMeshApParentAPMac_Type = MacAddress
_MwMeshApParentAPMac_Object = MibTableColumn
mwMeshApParentAPMac = _MwMeshApParentAPMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 7),
    _MwMeshApParentAPMac_Type()
)
mwMeshApParentAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApParentAPMac.setStatus("current")
_MwMeshApUpIfIndex_Type = Integer32
_MwMeshApUpIfIndex_Object = MibTableColumn
mwMeshApUpIfIndex = _MwMeshApUpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 8),
    _MwMeshApUpIfIndex_Type()
)
mwMeshApUpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApUpIfIndex.setStatus("current")
_MwMeshApUpChannel_Type = Integer32
_MwMeshApUpChannel_Object = MibTableColumn
mwMeshApUpChannel = _MwMeshApUpChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 9),
    _MwMeshApUpChannel_Type()
)
mwMeshApUpChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApUpChannel.setStatus("current")
_MwMeshApDownIfIndex_Type = Integer32
_MwMeshApDownIfIndex_Object = MibTableColumn
mwMeshApDownIfIndex = _MwMeshApDownIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 10),
    _MwMeshApDownIfIndex_Type()
)
mwMeshApDownIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApDownIfIndex.setStatus("current")
_MwMeshApDownChannel_Type = Integer32
_MwMeshApDownChannel_Object = MibTableColumn
mwMeshApDownChannel = _MwMeshApDownChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 11),
    _MwMeshApDownChannel_Type()
)
mwMeshApDownChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApDownChannel.setStatus("current")


class _MwMeshApDescr_Type(DisplayString):
    """Custom type mwMeshApDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_MwMeshApDescr_Type.__name__ = "DisplayString"
_MwMeshApDescr_Object = MibTableColumn
mwMeshApDescr = _MwMeshApDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 12),
    _MwMeshApDescr_Type()
)
mwMeshApDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMeshApDescr.setStatus("current")
_MwMeshApRowStatus_Type = RowStatus
_MwMeshApRowStatus_Object = MibTableColumn
mwMeshApRowStatus = _MwMeshApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 8, 1, 13),
    _MwMeshApRowStatus_Type()
)
mwMeshApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMeshApRowStatus.setStatus("current")
_MwDefaultIf80211SettingsTable_Object = MibTable
mwDefaultIf80211SettingsTable = _MwDefaultIf80211SettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9)
)
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsTable.setStatus("current")
_MwDefaultIf80211SettingsEntry_Object = MibTableRow
mwDefaultIf80211SettingsEntry = _MwDefaultIf80211SettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1)
)
mwDefaultIf80211SettingsEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwDefaultIf80211SettingsTableIndex"),
)
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsEntry.setStatus("current")
_MwDefaultIf80211SettingsTableIndex_Type = Integer32
_MwDefaultIf80211SettingsTableIndex_Object = MibTableColumn
mwDefaultIf80211SettingsTableIndex = _MwDefaultIf80211SettingsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 1),
    _MwDefaultIf80211SettingsTableIndex_Type()
)
mwDefaultIf80211SettingsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsTableIndex.setStatus("current")
_MwDefaultIf80211SettingsIfIndex_Type = Integer32
_MwDefaultIf80211SettingsIfIndex_Object = MibTableColumn
mwDefaultIf80211SettingsIfIndex = _MwDefaultIf80211SettingsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 2),
    _MwDefaultIf80211SettingsIfIndex_Type()
)
mwDefaultIf80211SettingsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfIndex.setStatus("current")
_MwDefaultIf80211SettingsIfMode_Type = MwlApIfConfigModeType
_MwDefaultIf80211SettingsIfMode_Object = MibTableColumn
mwDefaultIf80211SettingsIfMode = _MwDefaultIf80211SettingsIfMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 3),
    _MwDefaultIf80211SettingsIfMode_Type()
)
mwDefaultIf80211SettingsIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfMode.setStatus("current")
_MwDefaultIf80211SettingsIfChannel_Type = Integer32
_MwDefaultIf80211SettingsIfChannel_Object = MibTableColumn
mwDefaultIf80211SettingsIfChannel = _MwDefaultIf80211SettingsIfChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 4),
    _MwDefaultIf80211SettingsIfChannel_Type()
)
mwDefaultIf80211SettingsIfChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfChannel.setStatus("current")
_MwDefaultIf80211SettingsIfChannelWidth_Type = MwlChannelWidth
_MwDefaultIf80211SettingsIfChannelWidth_Object = MibTableColumn
mwDefaultIf80211SettingsIfChannelWidth = _MwDefaultIf80211SettingsIfChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 9, 1, 5),
    _MwDefaultIf80211SettingsIfChannelWidth_Type()
)
mwDefaultIf80211SettingsIfChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDefaultIf80211SettingsIfChannelWidth.setStatus("current")
_MwEventConfigurationTable_Object = MibTable
mwEventConfigurationTable = _MwEventConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mwEventConfigurationTable.setStatus("current")
_MwEventConfigurationEntry_Object = MibTableRow
mwEventConfigurationEntry = _MwEventConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1)
)
mwEventConfigurationEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwEventConfigurationTableIndex"),
)
if mibBuilder.loadTexts:
    mwEventConfigurationEntry.setStatus("current")
_MwEventConfigurationTableIndex_Type = Integer32
_MwEventConfigurationTableIndex_Object = MibTableColumn
mwEventConfigurationTableIndex = _MwEventConfigurationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1, 1),
    _MwEventConfigurationTableIndex_Type()
)
mwEventConfigurationTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwEventConfigurationTableIndex.setStatus("current")
_MwEventConfigurationEventType_Type = MwlNotificationType
_MwEventConfigurationEventType_Object = MibTableColumn
mwEventConfigurationEventType = _MwEventConfigurationEventType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1, 2),
    _MwEventConfigurationEventType_Type()
)
mwEventConfigurationEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEventConfigurationEventType.setStatus("current")
_MwEventConfigurationState_Type = MwlEnableDisableOption
_MwEventConfigurationState_Object = MibTableColumn
mwEventConfigurationState = _MwEventConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1, 3),
    _MwEventConfigurationState_Type()
)
mwEventConfigurationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEventConfigurationState.setStatus("current")
_MwEventConfigurationSeverity_Type = MwlNotificationSeverity
_MwEventConfigurationSeverity_Object = MibTableColumn
mwEventConfigurationSeverity = _MwEventConfigurationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1, 4),
    _MwEventConfigurationSeverity_Type()
)
mwEventConfigurationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEventConfigurationSeverity.setStatus("current")
_MwEventConfigurationSyslog_Type = MwlEnableDisableOption
_MwEventConfigurationSyslog_Object = MibTableColumn
mwEventConfigurationSyslog = _MwEventConfigurationSyslog_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1, 5),
    _MwEventConfigurationSyslog_Type()
)
mwEventConfigurationSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEventConfigurationSyslog.setStatus("current")
_MwEventConfigurationSnmp_Type = MwlEnableDisableOption
_MwEventConfigurationSnmp_Object = MibTableColumn
mwEventConfigurationSnmp = _MwEventConfigurationSnmp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1, 6),
    _MwEventConfigurationSnmp_Type()
)
mwEventConfigurationSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEventConfigurationSnmp.setStatus("current")
_MwEventConfigurationThreshold_Type = Integer32
_MwEventConfigurationThreshold_Object = MibTableColumn
mwEventConfigurationThreshold = _MwEventConfigurationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 10, 1, 7),
    _MwEventConfigurationThreshold_Type()
)
mwEventConfigurationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEventConfigurationThreshold.setStatus("current")
_MwAlarmConfigurationTable_Object = MibTable
mwAlarmConfigurationTable = _MwAlarmConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11)
)
if mibBuilder.loadTexts:
    mwAlarmConfigurationTable.setStatus("current")
_MwAlarmConfigurationEntry_Object = MibTableRow
mwAlarmConfigurationEntry = _MwAlarmConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1)
)
mwAlarmConfigurationEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwAlarmConfigurationTableIndex"),
)
if mibBuilder.loadTexts:
    mwAlarmConfigurationEntry.setStatus("current")
_MwAlarmConfigurationTableIndex_Type = Integer32
_MwAlarmConfigurationTableIndex_Object = MibTableColumn
mwAlarmConfigurationTableIndex = _MwAlarmConfigurationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1, 1),
    _MwAlarmConfigurationTableIndex_Type()
)
mwAlarmConfigurationTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAlarmConfigurationTableIndex.setStatus("current")
_MwAlarmConfigurationAlarmType_Type = MwlNotificationType
_MwAlarmConfigurationAlarmType_Object = MibTableColumn
mwAlarmConfigurationAlarmType = _MwAlarmConfigurationAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1, 2),
    _MwAlarmConfigurationAlarmType_Type()
)
mwAlarmConfigurationAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAlarmConfigurationAlarmType.setStatus("current")
_MwAlarmConfigurationState_Type = MwlEnableDisableOption
_MwAlarmConfigurationState_Object = MibTableColumn
mwAlarmConfigurationState = _MwAlarmConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1, 3),
    _MwAlarmConfigurationState_Type()
)
mwAlarmConfigurationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAlarmConfigurationState.setStatus("current")
_MwAlarmConfigurationSeverity_Type = MwlNotificationSeverity
_MwAlarmConfigurationSeverity_Object = MibTableColumn
mwAlarmConfigurationSeverity = _MwAlarmConfigurationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1, 4),
    _MwAlarmConfigurationSeverity_Type()
)
mwAlarmConfigurationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAlarmConfigurationSeverity.setStatus("current")
_MwAlarmConfigurationSyslog_Type = MwlEnableDisableOption
_MwAlarmConfigurationSyslog_Object = MibTableColumn
mwAlarmConfigurationSyslog = _MwAlarmConfigurationSyslog_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1, 5),
    _MwAlarmConfigurationSyslog_Type()
)
mwAlarmConfigurationSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAlarmConfigurationSyslog.setStatus("current")
_MwAlarmConfigurationSnmp_Type = MwlEnableDisableOption
_MwAlarmConfigurationSnmp_Object = MibTableColumn
mwAlarmConfigurationSnmp = _MwAlarmConfigurationSnmp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1, 6),
    _MwAlarmConfigurationSnmp_Type()
)
mwAlarmConfigurationSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAlarmConfigurationSnmp.setStatus("current")
_MwAlarmConfigurationThreshold_Type = Integer32
_MwAlarmConfigurationThreshold_Object = MibTableColumn
mwAlarmConfigurationThreshold = _MwAlarmConfigurationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 11, 1, 7),
    _MwAlarmConfigurationThreshold_Type()
)
mwAlarmConfigurationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAlarmConfigurationThreshold.setStatus("current")
_MwTimerProfileTable_Object = MibTable
mwTimerProfileTable = _MwTimerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14)
)
if mibBuilder.loadTexts:
    mwTimerProfileTable.setStatus("current")
_MwTimerProfileEntry_Object = MibTableRow
mwTimerProfileEntry = _MwTimerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1)
)
mwTimerProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-WLAN-MIB", "mwTimerProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwTimerProfileEntry.setStatus("current")
_MwTimerProfileTableIndex_Type = Integer32
_MwTimerProfileTableIndex_Object = MibTableColumn
mwTimerProfileTableIndex = _MwTimerProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 1),
    _MwTimerProfileTableIndex_Type()
)
mwTimerProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTimerProfileTableIndex.setStatus("current")


class _MwTimerProfileName_Type(DisplayString):
    """Custom type mwTimerProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwTimerProfileName_Type.__name__ = "DisplayString"
_MwTimerProfileName_Object = MibTableColumn
mwTimerProfileName = _MwTimerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 2),
    _MwTimerProfileName_Type()
)
mwTimerProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileName.setStatus("current")
_MwTimerProfileOwner_Type = MwlProfileOwner
_MwTimerProfileOwner_Object = MibTableColumn
mwTimerProfileOwner = _MwTimerProfileOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 3),
    _MwTimerProfileOwner_Type()
)
mwTimerProfileOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTimerProfileOwner.setStatus("current")
_MwTimerProfileTimerType_Type = MwlTimerType
_MwTimerProfileTimerType_Object = MibTableColumn
mwTimerProfileTimerType = _MwTimerProfileTimerType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 4),
    _MwTimerProfileTimerType_Type()
)
mwTimerProfileTimerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileTimerType.setStatus("current")
_MwTimerProfileAbsStartTime1_Type = DateAndTime
_MwTimerProfileAbsStartTime1_Object = MibTableColumn
mwTimerProfileAbsStartTime1 = _MwTimerProfileAbsStartTime1_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 5),
    _MwTimerProfileAbsStartTime1_Type()
)
mwTimerProfileAbsStartTime1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileAbsStartTime1.setStatus("current")
_MwTimerProfileAbsEndTime1_Type = DateAndTime
_MwTimerProfileAbsEndTime1_Object = MibTableColumn
mwTimerProfileAbsEndTime1 = _MwTimerProfileAbsEndTime1_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 6),
    _MwTimerProfileAbsEndTime1_Type()
)
mwTimerProfileAbsEndTime1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileAbsEndTime1.setStatus("current")
_MwTimerProfileAbsStartTime2_Type = DateAndTime
_MwTimerProfileAbsStartTime2_Object = MibTableColumn
mwTimerProfileAbsStartTime2 = _MwTimerProfileAbsStartTime2_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 7),
    _MwTimerProfileAbsStartTime2_Type()
)
mwTimerProfileAbsStartTime2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileAbsStartTime2.setStatus("current")
_MwTimerProfileAbsEndTime2_Type = DateAndTime
_MwTimerProfileAbsEndTime2_Object = MibTableColumn
mwTimerProfileAbsEndTime2 = _MwTimerProfileAbsEndTime2_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 8),
    _MwTimerProfileAbsEndTime2_Type()
)
mwTimerProfileAbsEndTime2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileAbsEndTime2.setStatus("current")
_MwTimerProfileAbsStartTime3_Type = DateAndTime
_MwTimerProfileAbsStartTime3_Object = MibTableColumn
mwTimerProfileAbsStartTime3 = _MwTimerProfileAbsStartTime3_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 9),
    _MwTimerProfileAbsStartTime3_Type()
)
mwTimerProfileAbsStartTime3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileAbsStartTime3.setStatus("current")
_MwTimerProfileAbsEndTime3_Type = DateAndTime
_MwTimerProfileAbsEndTime3_Object = MibTableColumn
mwTimerProfileAbsEndTime3 = _MwTimerProfileAbsEndTime3_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 10),
    _MwTimerProfileAbsEndTime3_Type()
)
mwTimerProfileAbsEndTime3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileAbsEndTime3.setStatus("current")
_MwTimerProfileDaysOfTheWeek_Type = MwlDaysOfTheWeekBits
_MwTimerProfileDaysOfTheWeek_Object = MibTableColumn
mwTimerProfileDaysOfTheWeek = _MwTimerProfileDaysOfTheWeek_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 11),
    _MwTimerProfileDaysOfTheWeek_Type()
)
mwTimerProfileDaysOfTheWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileDaysOfTheWeek.setStatus("current")
_MwTimerProfileInPeriodicStartTime1_Type = DisplayString
_MwTimerProfileInPeriodicStartTime1_Object = MibTableColumn
mwTimerProfileInPeriodicStartTime1 = _MwTimerProfileInPeriodicStartTime1_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 12),
    _MwTimerProfileInPeriodicStartTime1_Type()
)
mwTimerProfileInPeriodicStartTime1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileInPeriodicStartTime1.setStatus("current")
_MwTimerProfileInPeriodicEndTime1_Type = DisplayString
_MwTimerProfileInPeriodicEndTime1_Object = MibTableColumn
mwTimerProfileInPeriodicEndTime1 = _MwTimerProfileInPeriodicEndTime1_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 13),
    _MwTimerProfileInPeriodicEndTime1_Type()
)
mwTimerProfileInPeriodicEndTime1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileInPeriodicEndTime1.setStatus("current")
_MwTimerProfileInPeriodicStartTime2_Type = DisplayString
_MwTimerProfileInPeriodicStartTime2_Object = MibTableColumn
mwTimerProfileInPeriodicStartTime2 = _MwTimerProfileInPeriodicStartTime2_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 14),
    _MwTimerProfileInPeriodicStartTime2_Type()
)
mwTimerProfileInPeriodicStartTime2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileInPeriodicStartTime2.setStatus("current")
_MwTimerProfileInPeriodicEndTime2_Type = DisplayString
_MwTimerProfileInPeriodicEndTime2_Object = MibTableColumn
mwTimerProfileInPeriodicEndTime2 = _MwTimerProfileInPeriodicEndTime2_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 15),
    _MwTimerProfileInPeriodicEndTime2_Type()
)
mwTimerProfileInPeriodicEndTime2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileInPeriodicEndTime2.setStatus("current")
_MwTimerProfileInPeriodicStartTime3_Type = DisplayString
_MwTimerProfileInPeriodicStartTime3_Object = MibTableColumn
mwTimerProfileInPeriodicStartTime3 = _MwTimerProfileInPeriodicStartTime3_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 16),
    _MwTimerProfileInPeriodicStartTime3_Type()
)
mwTimerProfileInPeriodicStartTime3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileInPeriodicStartTime3.setStatus("current")
_MwTimerProfileInPeriodicEndTime3_Type = DisplayString
_MwTimerProfileInPeriodicEndTime3_Object = MibTableColumn
mwTimerProfileInPeriodicEndTime3 = _MwTimerProfileInPeriodicEndTime3_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 17),
    _MwTimerProfileInPeriodicEndTime3_Type()
)
mwTimerProfileInPeriodicEndTime3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileInPeriodicEndTime3.setStatus("current")
_MwTimerProfileRowStatus_Type = RowStatus
_MwTimerProfileRowStatus_Object = MibTableColumn
mwTimerProfileRowStatus = _MwTimerProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 14, 1, 26),
    _MwTimerProfileRowStatus_Type()
)
mwTimerProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwTimerProfileRowStatus.setStatus("current")
_MwMcaVars_ObjectIdentity = ObjectIdentity
mwMcaVars = _MwMcaVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16)
)
_MwMcaVarsAutoChannelMode_Type = MwlEnableDisableOption
_MwMcaVarsAutoChannelMode_Object = MibScalar
mwMcaVarsAutoChannelMode = _MwMcaVarsAutoChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 3),
    _MwMcaVarsAutoChannelMode_Type()
)
mwMcaVarsAutoChannelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsAutoChannelMode.setStatus("current")


class _MwMcaVarsRadio1Channel_Type(Integer32):
    """Custom type mwMcaVarsRadio1Channel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_MwMcaVarsRadio1Channel_Type.__name__ = "Integer32"
_MwMcaVarsRadio1Channel_Object = MibScalar
mwMcaVarsRadio1Channel = _MwMcaVarsRadio1Channel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 4),
    _MwMcaVarsRadio1Channel_Type()
)
mwMcaVarsRadio1Channel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsRadio1Channel.setStatus("current")
_MwMcaVarsRadio1ChannelWidth_Type = MwlChannelWidth
_MwMcaVarsRadio1ChannelWidth_Object = MibScalar
mwMcaVarsRadio1ChannelWidth = _MwMcaVarsRadio1ChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 5),
    _MwMcaVarsRadio1ChannelWidth_Type()
)
mwMcaVarsRadio1ChannelWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsRadio1ChannelWidth.setStatus("current")


class _MwMcaVarsRadio2Channel_Type(Integer32):
    """Custom type mwMcaVarsRadio2Channel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 165),
    )


_MwMcaVarsRadio2Channel_Type.__name__ = "Integer32"
_MwMcaVarsRadio2Channel_Object = MibScalar
mwMcaVarsRadio2Channel = _MwMcaVarsRadio2Channel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 6),
    _MwMcaVarsRadio2Channel_Type()
)
mwMcaVarsRadio2Channel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsRadio2Channel.setStatus("current")
_MwMcaVarsRadio2ChannelWidth_Type = MwlChannelWidth
_MwMcaVarsRadio2ChannelWidth_Object = MibScalar
mwMcaVarsRadio2ChannelWidth = _MwMcaVarsRadio2ChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 7),
    _MwMcaVarsRadio2ChannelWidth_Type()
)
mwMcaVarsRadio2ChannelWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsRadio2ChannelWidth.setStatus("current")
_MwMcaVarsAutoPower_Type = MwlOnOffSwitch
_MwMcaVarsAutoPower_Object = MibScalar
mwMcaVarsAutoPower = _MwMcaVarsAutoPower_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 8),
    _MwMcaVarsAutoPower_Type()
)
mwMcaVarsAutoPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsAutoPower.setStatus("current")
_MwMcaVarsFreeze_Type = MwlYesNoSwitch
_MwMcaVarsFreeze_Object = MibScalar
mwMcaVarsFreeze = _MwMcaVarsFreeze_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 9),
    _MwMcaVarsFreeze_Type()
)
mwMcaVarsFreeze.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsFreeze.setStatus("current")


class _MwMcaVarsTimer_Type(Integer32):
    """Custom type mwMcaVarsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 3600),
    )


_MwMcaVarsTimer_Type.__name__ = "Integer32"
_MwMcaVarsTimer_Object = MibScalar
mwMcaVarsTimer = _MwMcaVarsTimer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 10),
    _MwMcaVarsTimer_Type()
)
mwMcaVarsTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsTimer.setStatus("current")
_MwMcaVarsDfs_Type = MwlOnOffSwitch
_MwMcaVarsDfs_Object = MibScalar
mwMcaVarsDfs = _MwMcaVarsDfs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 11),
    _MwMcaVarsDfs_Type()
)
mwMcaVarsDfs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsDfs.setStatus("current")
_MwMcaVarsTimerState_Type = MwlOnOffSwitch
_MwMcaVarsTimerState_Object = MibScalar
mwMcaVarsTimerState = _MwMcaVarsTimerState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 3, 16, 12),
    _MwMcaVarsTimerState_Type()
)
mwMcaVarsTimerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwMcaVarsTimerState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-WLAN-MIB",
    **{"mwConfigWlan": mwConfigWlan,
       "mwIf80211CapabilityTable": mwIf80211CapabilityTable,
       "mwIf80211CapabilityEntry": mwIf80211CapabilityEntry,
       "mwIf80211CapabilityTableIndex": mwIf80211CapabilityTableIndex,
       "mwIf80211CapabilityIfAGain": mwIf80211CapabilityIfAGain,
       "mwIf80211CapabilityIfBgGain": mwIf80211CapabilityIfBgGain,
       "mwIf80211CapabilityIfLinkType": mwIf80211CapabilityIfLinkType,
       "mwIf80211CapabilityIfAntennaSet": mwIf80211CapabilityIfAntennaSet,
       "mwIf80211CapabilityIfConnectorType": mwIf80211CapabilityIfConnectorType,
       "mwIf80211CapabilityIfIndex": mwIf80211CapabilityIfIndex,
       "mwIf80211CapabilityApHwType": mwIf80211CapabilityApHwType,
       "mwIf80211CapabilityIfNmsNodeId": mwIf80211CapabilityIfNmsNodeId,
       "mwIf80211CapabilityIfConnectorGain": mwIf80211CapabilityIfConnectorGain,
       "mwIf80211CapabilityIfAntennaLocation": mwIf80211CapabilityIfAntennaLocation,
       "mwIf80211CapabilityIfAntennaConnector": mwIf80211CapabilityIfAntennaConnector,
       "mwEssTable": mwEssTable,
       "mwEssEntry": mwEssEntry,
       "mwEssTableIndex": mwEssTableIndex,
       "mwEssSsId": mwEssSsId,
       "mwEssId": mwEssId,
       "mwEssGreName": mwEssGreName,
       "mwEssVlanName": mwEssVlanName,
       "mwEssL2Bridging": mwEssL2Bridging,
       "mwEssDTIMPeriod": mwEssDTIMPeriod,
       "mwEssVlanSupport": mwEssVlanSupport,
       "mwEssBaseTxRates": mwEssBaseTxRates,
       "mwPublishEssId": mwPublishEssId,
       "mwEssABaseTxRates": mwEssABaseTxRates,
       "mwEssGBaseTxRates": mwEssGBaseTxRates,
       "mwEssDataplaneMode": mwEssDataplaneMode,
       "mwEssBGBaseTxRates": mwEssBGBaseTxRates,
       "mwEssANBaseTxRates": mwEssANBaseTxRates,
       "mwEssBeaconInterval": mwEssBeaconInterval,
       "mwEssAllowMulticast": mwEssAllowMulticast,
       "mwEssBGNBaseTxRates": mwEssBGNBaseTxRates,
       "mwEssCountermeasure": mwEssCountermeasure,
       "mwEssJoinOnDiscovery": mwEssJoinOnDiscovery,
       "mwEssANBaseHTTxRates": mwEssANBaseHTTxRates,
       "mwEssSupportedTxRates": mwEssSupportedTxRates,
       "mwEssBGNBaseHTTxRates": mwEssBGNBaseHTTxRates,
       "mwEssASupportedTxRates": mwEssASupportedTxRates,
       "mwEssGSupportedTxRates": mwEssGSupportedTxRates,
       "mwEssBGSupportedTxRates": mwEssBGSupportedTxRates,
       "mwEssANSupportedTxRates": mwEssANSupportedTxRates,
       "mwEssSecurityProfileName": mwEssSecurityProfileName,
       "mwEssBGNSupportedTxRates": mwEssBGNSupportedTxRates,
       "mwEssANSupportedHTTxRates": mwEssANSupportedHTTxRates,
       "mwEssBGNSupportedHTTxRates": mwEssBGNSupportedHTTxRates,
       "mwEssAccountingInterimInterval": mwEssAccountingInterimInterval,
       "mwEssPrimaryAccountingRadiusName": mwEssPrimaryAccountingRadiusName,
       "mwEssSecondaryAccountingRadiusName": mwEssSecondaryAccountingRadiusName,
       "mwEssMulticastMACTransparency": mwEssMulticastMACTransparency,
       "mwEssBandSteering": mwEssBandSteering,
       "mwEssBandSteeringTimeout": mwEssBandSteeringTimeout,
       "mwEssApVlanTag": mwEssApVlanTag,
       "mwEssEnableApVlanPriority": mwEssEnableApVlanPriority,
       "mwEssOwner": mwEssOwner,
       "mwEssEnableAPSD": mwEssEnableAPSD,
       "mwEssState": mwEssState,
       "mwEssMulticastToUnicastConversion": mwEssMulticastToUnicastConversion,
       "mwEssEfOverride": mwEssEfOverride,
       "mwEssPapBroadcastSsid": mwEssPapBroadcastSsid,
       "mwEssVirtualInterfaceProfileName": mwEssVirtualInterfaceProfileName,
       "mwEssWirelessToWirelessIsolation": mwEssWirelessToWirelessIsolation,
       "mwEssRFVMode": mwEssRFVMode,
       "mwEssS1VHTBaseMCSSet": mwEssS1VHTBaseMCSSet,
       "mwEssS2VHTBaseMCSSet": mwEssS2VHTBaseMCSSet,
       "mwEssS3VHTBaseMCSSet": mwEssS3VHTBaseMCSSet,
       "mwEssS1VHTSupportMCSSet": mwEssS1VHTSupportMCSSet,
       "mwEssS2VHTSupportMCSSet": mwEssS2VHTSupportMCSSet,
       "mwEssS3VHTSupportMCSSet": mwEssS3VHTSupportMCSSet,
       "mwEssApVlanPolicy": mwEssApVlanPolicy,
       "mwEssVoiceClientType": mwEssVoiceClientType,
       "mwEssIpPrefixLookup": mwEssIpPrefixLookup,
       "mwEssFastHandoff": mwEssFastHandoff,
       "mwEssMobilityDomain": mwEssMobilityDomain,
       "mwEssVlanPoolName": mwEssVlanPoolName,
       "mwEssDot11kEnabled": mwEssDot11kEnabled,
       "mwEssTimerProfileName": mwEssTimerProfileName,
       "mwEssIdType": mwEssIdType,
       "mwBackupEssId": mwBackupEssId,
       "mwEssACMSupport": mwEssACMSupport,
       "mwEssS4VHTBaseMCSSet": mwEssS4VHTBaseMCSSet,
       "mwEssS4VHTSupportMCSSet": mwEssS4VHTSupportMCSSet,
       "mwEssQamSupport": mwEssQamSupport,
       "mwEssReconnectPrimaryServer": mwEssReconnectPrimaryServer,
       "mwEssRowStatus": mwEssRowStatus,
       "mwIf80211Table": mwIf80211Table,
       "mwIf80211Entry": mwIf80211Entry,
       "mwIf80211TableIndex": mwIf80211TableIndex,
       "mwIf80211IfMode": mwIf80211IfMode,
       "mwIf80211IfDescr": mwIf80211IfDescr,
       "mwIf80211IfApMode": mwIf80211IfApMode,
       "mwIf80211IfChannel": mwIf80211IfChannel,
       "mwIf80211NOnlyMode": mwIf80211NOnlyMode,
       "mwIf80211IfMimoMode": mwIf80211IfMimoMode,
       "mwIf80211channelWidth": mwIf80211channelWidth,
       "mwIf80211IfAdminStatus": mwIf80211IfAdminStatus,
       "mwIf80211IfTxPowerHigh": mwIf80211IfTxPowerHigh,
       "mwIf80211IfBgProtectionMode": mwIf80211IfBgProtectionMode,
       "mwIf80211IfShortPreambleFlag": mwIf80211IfShortPreambleFlag,
       "mwIf80211IfMtu": mwIf80211IfMtu,
       "mwIf80211IfType": mwIf80211IfType,
       "mwIf80211IfIndex": mwIf80211IfIndex,
       "mwIf80211IfNodeId": mwIf80211IfNodeId,
       "mwIf80211ApHwType": mwIf80211ApHwType,
       "mwIf80211IfNodeName": mwIf80211IfNodeName,
       "mwIf80211IfOperStatus": mwIf80211IfOperStatus,
       "mwIf80211IfLastChange": mwIf80211IfLastChange,
       "mwIf80211IfOperChannel": mwIf80211IfOperChannel,
       "mwIf80211IfBandSupport": mwIf80211IfBandSupport,
       "mwIf80211IfNumAntennas": mwIf80211IfNumAntennas,
       "mwIf80211ProbeResponseThreshold": mwIf80211ProbeResponseThreshold,
       "mwIf80211IfMeshStatus": mwIf80211IfMeshStatus,
       "mwIf80211UplinkType": mwIf80211UplinkType,
       "mwIf80211IfHtProtectionMode": mwIf80211IfHtProtectionMode,
       "mwIf80211IfFallbackChannel": mwIf80211IfFallbackChannel,
       "mwIf80211RFVMode": mwIf80211RFVMode,
       "mwIf80211ChannelCenterFrequency": mwIf80211ChannelCenterFrequency,
       "mwIf80211TransmitBeamformingSupport": mwIf80211TransmitBeamformingSupport,
       "mwIf80211STBCSupport": mwIf80211STBCSupport,
       "mwIf80211DFSFallbackOption": mwIf80211DFSFallbackOption,
       "mwIf80211DFSChanRevertive": mwIf80211DFSChanRevertive,
       "mwIf80211FallbackChannelCenterFrequency": mwIf80211FallbackChannelCenterFrequency,
       "mwIf80211IfVhtStatus": mwIf80211IfVhtStatus,
       "mwEssApTable": mwEssApTable,
       "mwEssApEntry": mwEssApEntry,
       "mwEssApTableIndex": mwEssApTableIndex,
       "mwEssApEssId": mwEssApEssId,
       "mwEssApIfIndex": mwEssApIfIndex,
       "mwEssApMaxCalls": mwEssApMaxCalls,
       "mwEssApApNodeId": mwEssApApNodeId,
       "mwEssApBssId": mwEssApBssId,
       "mwEssApIfMode": mwEssApIfMode,
       "mwEssApApNodeName": mwEssApApNodeName,
       "mwEssApBaseTxRates": mwEssApBaseTxRates,
       "mwEssApChannelNumber": mwEssApChannelNumber,
       "mwEssApIfOperChannel": mwEssApIfOperChannel,
       "mwEssApSupportedTxRates": mwEssApSupportedTxRates,
       "mwEssApAdminMode": mwEssApAdminMode,
       "mwEssApRowStatus": mwEssApRowStatus,
       "mwMeshProfileTable": mwMeshProfileTable,
       "mwMeshProfileEntry": mwMeshProfileEntry,
       "mwMeshProfileTableIndex": mwMeshProfileTableIndex,
       "mwMeshProfileName": mwMeshProfileName,
       "mwMeshProfileDescr": mwMeshProfileDescr,
       "mwMeshProfilePSK": mwMeshProfilePSK,
       "mwMeshProfileAdminMode": mwMeshProfileAdminMode,
       "mwMeshProfilePlugNPlayStatus": mwMeshProfilePlugNPlayStatus,
       "mwMeshProfileMeshVlanTrunk": mwMeshProfileMeshVlanTrunk,
       "mwMeshProfileRowStatus": mwMeshProfileRowStatus,
       "mwMeshApTable": mwMeshApTable,
       "mwMeshApEntry": mwMeshApEntry,
       "mwMeshApTableIndex": mwMeshApTableIndex,
       "mwMeshApName": mwMeshApName,
       "mwMeshApAPId": mwMeshApAPId,
       "mwMeshApAPMac": mwMeshApAPMac,
       "mwMeshApAvailState": mwMeshApAvailState,
       "mwMeshApParentAPId": mwMeshApParentAPId,
       "mwMeshApParentAPMac": mwMeshApParentAPMac,
       "mwMeshApUpIfIndex": mwMeshApUpIfIndex,
       "mwMeshApUpChannel": mwMeshApUpChannel,
       "mwMeshApDownIfIndex": mwMeshApDownIfIndex,
       "mwMeshApDownChannel": mwMeshApDownChannel,
       "mwMeshApDescr": mwMeshApDescr,
       "mwMeshApRowStatus": mwMeshApRowStatus,
       "mwDefaultIf80211SettingsTable": mwDefaultIf80211SettingsTable,
       "mwDefaultIf80211SettingsEntry": mwDefaultIf80211SettingsEntry,
       "mwDefaultIf80211SettingsTableIndex": mwDefaultIf80211SettingsTableIndex,
       "mwDefaultIf80211SettingsIfIndex": mwDefaultIf80211SettingsIfIndex,
       "mwDefaultIf80211SettingsIfMode": mwDefaultIf80211SettingsIfMode,
       "mwDefaultIf80211SettingsIfChannel": mwDefaultIf80211SettingsIfChannel,
       "mwDefaultIf80211SettingsIfChannelWidth": mwDefaultIf80211SettingsIfChannelWidth,
       "mwEventConfigurationTable": mwEventConfigurationTable,
       "mwEventConfigurationEntry": mwEventConfigurationEntry,
       "mwEventConfigurationTableIndex": mwEventConfigurationTableIndex,
       "mwEventConfigurationEventType": mwEventConfigurationEventType,
       "mwEventConfigurationState": mwEventConfigurationState,
       "mwEventConfigurationSeverity": mwEventConfigurationSeverity,
       "mwEventConfigurationSyslog": mwEventConfigurationSyslog,
       "mwEventConfigurationSnmp": mwEventConfigurationSnmp,
       "mwEventConfigurationThreshold": mwEventConfigurationThreshold,
       "mwAlarmConfigurationTable": mwAlarmConfigurationTable,
       "mwAlarmConfigurationEntry": mwAlarmConfigurationEntry,
       "mwAlarmConfigurationTableIndex": mwAlarmConfigurationTableIndex,
       "mwAlarmConfigurationAlarmType": mwAlarmConfigurationAlarmType,
       "mwAlarmConfigurationState": mwAlarmConfigurationState,
       "mwAlarmConfigurationSeverity": mwAlarmConfigurationSeverity,
       "mwAlarmConfigurationSyslog": mwAlarmConfigurationSyslog,
       "mwAlarmConfigurationSnmp": mwAlarmConfigurationSnmp,
       "mwAlarmConfigurationThreshold": mwAlarmConfigurationThreshold,
       "mwTimerProfileTable": mwTimerProfileTable,
       "mwTimerProfileEntry": mwTimerProfileEntry,
       "mwTimerProfileTableIndex": mwTimerProfileTableIndex,
       "mwTimerProfileName": mwTimerProfileName,
       "mwTimerProfileOwner": mwTimerProfileOwner,
       "mwTimerProfileTimerType": mwTimerProfileTimerType,
       "mwTimerProfileAbsStartTime1": mwTimerProfileAbsStartTime1,
       "mwTimerProfileAbsEndTime1": mwTimerProfileAbsEndTime1,
       "mwTimerProfileAbsStartTime2": mwTimerProfileAbsStartTime2,
       "mwTimerProfileAbsEndTime2": mwTimerProfileAbsEndTime2,
       "mwTimerProfileAbsStartTime3": mwTimerProfileAbsStartTime3,
       "mwTimerProfileAbsEndTime3": mwTimerProfileAbsEndTime3,
       "mwTimerProfileDaysOfTheWeek": mwTimerProfileDaysOfTheWeek,
       "mwTimerProfileInPeriodicStartTime1": mwTimerProfileInPeriodicStartTime1,
       "mwTimerProfileInPeriodicEndTime1": mwTimerProfileInPeriodicEndTime1,
       "mwTimerProfileInPeriodicStartTime2": mwTimerProfileInPeriodicStartTime2,
       "mwTimerProfileInPeriodicEndTime2": mwTimerProfileInPeriodicEndTime2,
       "mwTimerProfileInPeriodicStartTime3": mwTimerProfileInPeriodicStartTime3,
       "mwTimerProfileInPeriodicEndTime3": mwTimerProfileInPeriodicEndTime3,
       "mwTimerProfileRowStatus": mwTimerProfileRowStatus,
       "mwMcaVars": mwMcaVars,
       "mwMcaVarsAutoChannelMode": mwMcaVarsAutoChannelMode,
       "mwMcaVarsRadio1Channel": mwMcaVarsRadio1Channel,
       "mwMcaVarsRadio1ChannelWidth": mwMcaVarsRadio1ChannelWidth,
       "mwMcaVarsRadio2Channel": mwMcaVarsRadio2Channel,
       "mwMcaVarsRadio2ChannelWidth": mwMcaVarsRadio2ChannelWidth,
       "mwMcaVarsAutoPower": mwMcaVarsAutoPower,
       "mwMcaVarsFreeze": mwMcaVarsFreeze,
       "mwMcaVarsTimer": mwMcaVarsTimer,
       "mwMcaVarsDfs": mwMcaVarsDfs,
       "mwMcaVarsTimerState": mwMcaVarsTimerState}
)
