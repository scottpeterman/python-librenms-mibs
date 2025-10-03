# SNMP MIB module (WLSX-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\WLSX-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:56 2025
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

(wlsrEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsrEnterpriseMibModules")

(ArubaAPMasterStatus,
 ArubaAPUplinkChangeReason,
 ArubaAPUplinkType,
 ArubaARMChangeReason,
 ArubaAccessPointMode,
 ArubaAddressType,
 ArubaAuthenticationMethods,
 ArubaBlackListReason,
 ArubaConfigurationChangeType,
 ArubaConfigurationState,
 ArubaDBType,
 ArubaEnableValue,
 ArubaFrameType,
 ArubaHTExtChannel,
 ArubaIfState,
 ArubaIfStateChangeReason,
 ArubaOperStateValue,
 ArubaPortalServerDownReason,
 ArubaStackChangeEvent,
 ArubaStackIfTopoJoined,
 ArubaStackState,
 ArubaStationType,
 ArubaSwitchRole,
 ArubaThresholdResourceType,
 ArubaVrrpState,
 InterfaceIndex,
 TimeTicks) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaAPMasterStatus",
    "ArubaAPUplinkChangeReason",
    "ArubaAPUplinkType",
    "ArubaARMChangeReason",
    "ArubaAccessPointMode",
    "ArubaAddressType",
    "ArubaAuthenticationMethods",
    "ArubaBlackListReason",
    "ArubaConfigurationChangeType",
    "ArubaConfigurationState",
    "ArubaDBType",
    "ArubaEnableValue",
    "ArubaFrameType",
    "ArubaHTExtChannel",
    "ArubaIfState",
    "ArubaIfStateChangeReason",
    "ArubaOperStateValue",
    "ArubaPortalServerDownReason",
    "ArubaStackChangeEvent",
    "ArubaStackIfTopoJoined",
    "ArubaStackState",
    "ArubaStationType",
    "ArubaSwitchRole",
    "ArubaThresholdResourceType",
    "ArubaVrrpState",
    "InterfaceIndex",
    "TimeTicks")

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
 TextualConvention,
 TimeTicks,
 Unsigned32,
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
    "TextualConvention",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsrTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11)
)
if mibBuilder.loadTexts:
    wlsrTrapMIB.setRevisions(
        ("1921-06-01 19:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxTrapsGroup_ObjectIdentity = ObjectIdentity
wlsxTrapsGroup = _WlsxTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1)
)
_WlsxTrapObjectsGroup_ObjectIdentity = ObjectIdentity
wlsxTrapObjectsGroup = _WlsxTrapObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1)
)
_WlsxTrapAPMacAddress_Type = MacAddress
_WlsxTrapAPMacAddress_Object = MibScalar
wlsxTrapAPMacAddress = _WlsxTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 1),
    _WlsxTrapAPMacAddress_Type()
)
wlsxTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPMacAddress.setStatus("current")
_WlsxTrapAPIpAddress_Type = IpAddress
_WlsxTrapAPIpAddress_Object = MibScalar
wlsxTrapAPIpAddress = _WlsxTrapAPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 2),
    _WlsxTrapAPIpAddress_Type()
)
wlsxTrapAPIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPIpAddress.setStatus("current")
_WlsxTrapAPBSSID_Type = MacAddress
_WlsxTrapAPBSSID_Object = MibScalar
wlsxTrapAPBSSID = _WlsxTrapAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 3),
    _WlsxTrapAPBSSID_Type()
)
wlsxTrapAPBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPBSSID.setStatus("current")


class _WlsxTrapEssid_Type(DisplayString):
    """Custom type wlsxTrapEssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapEssid_Type.__name__ = "DisplayString"
_WlsxTrapEssid_Object = MibScalar
wlsxTrapEssid = _WlsxTrapEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 4),
    _WlsxTrapEssid_Type()
)
wlsxTrapEssid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapEssid.setStatus("current")
_WlsxTrapTargetAPBSSID_Type = MacAddress
_WlsxTrapTargetAPBSSID_Object = MibScalar
wlsxTrapTargetAPBSSID = _WlsxTrapTargetAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 5),
    _WlsxTrapTargetAPBSSID_Type()
)
wlsxTrapTargetAPBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPBSSID.setStatus("current")


class _WlsxTrapTargetAPSSID_Type(DisplayString):
    """Custom type wlsxTrapTargetAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTargetAPSSID_Type.__name__ = "DisplayString"
_WlsxTrapTargetAPSSID_Object = MibScalar
wlsxTrapTargetAPSSID = _WlsxTrapTargetAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 6),
    _WlsxTrapTargetAPSSID_Type()
)
wlsxTrapTargetAPSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPSSID.setStatus("current")
_WlsxTrapTargetAPChannel_Type = Integer32
_WlsxTrapTargetAPChannel_Object = MibScalar
wlsxTrapTargetAPChannel = _WlsxTrapTargetAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 7),
    _WlsxTrapTargetAPChannel_Type()
)
wlsxTrapTargetAPChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPChannel.setStatus("current")
_WlsxTrapNodeMac_Type = MacAddress
_WlsxTrapNodeMac_Object = MibScalar
wlsxTrapNodeMac = _WlsxTrapNodeMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 8),
    _WlsxTrapNodeMac_Type()
)
wlsxTrapNodeMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapNodeMac.setStatus("current")
_WlsxTrapSourceMac_Type = MacAddress
_WlsxTrapSourceMac_Object = MibScalar
wlsxTrapSourceMac = _WlsxTrapSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 9),
    _WlsxTrapSourceMac_Type()
)
wlsxTrapSourceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSourceMac.setStatus("current")
_WlsxReceiverMac_Type = MacAddress
_WlsxReceiverMac_Object = MibScalar
wlsxReceiverMac = _WlsxReceiverMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 10),
    _WlsxReceiverMac_Type()
)
wlsxReceiverMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxReceiverMac.setStatus("current")
_WlsxTrapTransmitterMac_Type = MacAddress
_WlsxTrapTransmitterMac_Object = MibScalar
wlsxTrapTransmitterMac = _WlsxTrapTransmitterMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 11),
    _WlsxTrapTransmitterMac_Type()
)
wlsxTrapTransmitterMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTransmitterMac.setStatus("current")
_WlsxTrapReceiverMac_Type = MacAddress
_WlsxTrapReceiverMac_Object = MibScalar
wlsxTrapReceiverMac = _WlsxTrapReceiverMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 12),
    _WlsxTrapReceiverMac_Type()
)
wlsxTrapReceiverMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapReceiverMac.setStatus("current")
_WlsxTrapSnr_Type = Integer32
_WlsxTrapSnr_Object = MibScalar
wlsxTrapSnr = _WlsxTrapSnr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 13),
    _WlsxTrapSnr_Type()
)
wlsxTrapSnr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSnr.setStatus("current")


class _WlsxTrapSignatureName_Type(DisplayString):
    """Custom type wlsxTrapSignatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapSignatureName_Type.__name__ = "DisplayString"
_WlsxTrapSignatureName_Object = MibScalar
wlsxTrapSignatureName = _WlsxTrapSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 14),
    _WlsxTrapSignatureName_Type()
)
wlsxTrapSignatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSignatureName.setStatus("current")
_WlsxTrapFrameType_Type = ArubaFrameType
_WlsxTrapFrameType_Object = MibScalar
wlsxTrapFrameType = _WlsxTrapFrameType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 15),
    _WlsxTrapFrameType_Type()
)
wlsxTrapFrameType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapFrameType.setStatus("current")
_WlsxTrapAddressType_Type = ArubaAddressType
_WlsxTrapAddressType_Object = MibScalar
wlsxTrapAddressType = _WlsxTrapAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 16),
    _WlsxTrapAddressType_Type()
)
wlsxTrapAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAddressType.setStatus("current")


class _WlsxTrapAPLocation_Type(DisplayString):
    """Custom type wlsxTrapAPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAPLocation_Type.__name__ = "DisplayString"
_WlsxTrapAPLocation_Object = MibScalar
wlsxTrapAPLocation = _WlsxTrapAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 17),
    _WlsxTrapAPLocation_Type()
)
wlsxTrapAPLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPLocation.setStatus("current")
_WlsxTrapAPChannel_Type = Integer32
_WlsxTrapAPChannel_Object = MibScalar
wlsxTrapAPChannel = _WlsxTrapAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 18),
    _WlsxTrapAPChannel_Type()
)
wlsxTrapAPChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPChannel.setStatus("current")
_WlsxTrapAPTxPower_Type = Integer32
_WlsxTrapAPTxPower_Object = MibScalar
wlsxTrapAPTxPower = _WlsxTrapAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 19),
    _WlsxTrapAPTxPower_Type()
)
wlsxTrapAPTxPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPTxPower.setStatus("current")
_WlsxTrapMatchedMac_Type = MacAddress
_WlsxTrapMatchedMac_Object = MibScalar
wlsxTrapMatchedMac = _WlsxTrapMatchedMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 20),
    _WlsxTrapMatchedMac_Type()
)
wlsxTrapMatchedMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMatchedMac.setStatus("current")
_WlsxTrapMatchedIp_Type = IpAddress
_WlsxTrapMatchedIp_Object = MibScalar
wlsxTrapMatchedIp = _WlsxTrapMatchedIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 21),
    _WlsxTrapMatchedIp_Type()
)
wlsxTrapMatchedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMatchedIp.setStatus("current")


class _WlsxTrapRogueIfoURL_Type(DisplayString):
    """Custom type wlsxTrapRogueIfoURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapRogueIfoURL_Type.__name__ = "DisplayString"
_WlsxTrapRogueIfoURL_Object = MibScalar
wlsxTrapRogueIfoURL = _WlsxTrapRogueIfoURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 22),
    _WlsxTrapRogueIfoURL_Type()
)
wlsxTrapRogueIfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapRogueIfoURL.setStatus("current")
_WlsxTrapVlanId_Type = Integer32
_WlsxTrapVlanId_Object = MibScalar
wlsxTrapVlanId = _WlsxTrapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 23),
    _WlsxTrapVlanId_Type()
)
wlsxTrapVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVlanId.setStatus("current")
_WlsxTrapAdminStatus_Type = ArubaEnableValue
_WlsxTrapAdminStatus_Object = MibScalar
wlsxTrapAdminStatus = _WlsxTrapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 24),
    _WlsxTrapAdminStatus_Type()
)
wlsxTrapAdminStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAdminStatus.setStatus("current")
_WlsxTrapOperStatus_Type = ArubaOperStateValue
_WlsxTrapOperStatus_Object = MibScalar
wlsxTrapOperStatus = _WlsxTrapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 25),
    _WlsxTrapOperStatus_Type()
)
wlsxTrapOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapOperStatus.setStatus("current")


class _WlsxTrapAuthServerName_Type(DisplayString):
    """Custom type wlsxTrapAuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAuthServerName_Type.__name__ = "DisplayString"
_WlsxTrapAuthServerName_Object = MibScalar
wlsxTrapAuthServerName = _WlsxTrapAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 26),
    _WlsxTrapAuthServerName_Type()
)
wlsxTrapAuthServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthServerName.setStatus("current")
_WlsxTrapAuthServerTimeout_Type = Integer32
_WlsxTrapAuthServerTimeout_Object = MibScalar
wlsxTrapAuthServerTimeout = _WlsxTrapAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 27),
    _WlsxTrapAuthServerTimeout_Type()
)
wlsxTrapAuthServerTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthServerTimeout.setStatus("current")
_WlsxTrapCardSlot_Type = Integer32
_WlsxTrapCardSlot_Object = MibScalar
wlsxTrapCardSlot = _WlsxTrapCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 28),
    _WlsxTrapCardSlot_Type()
)
wlsxTrapCardSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCardSlot.setStatus("current")


class _WlsxTrapTemperatureValue_Type(DisplayString):
    """Custom type wlsxTrapTemperatureValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTemperatureValue_Type.__name__ = "DisplayString"
_WlsxTrapTemperatureValue_Object = MibScalar
wlsxTrapTemperatureValue = _WlsxTrapTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 29),
    _WlsxTrapTemperatureValue_Type()
)
wlsxTrapTemperatureValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTemperatureValue.setStatus("current")


class _WlsxTrapProcessName_Type(DisplayString):
    """Custom type wlsxTrapProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapProcessName_Type.__name__ = "DisplayString"
_WlsxTrapProcessName_Object = MibScalar
wlsxTrapProcessName = _WlsxTrapProcessName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 30),
    _WlsxTrapProcessName_Type()
)
wlsxTrapProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapProcessName.setStatus("current")
_WlsxTrapFanNumber_Type = Integer32
_WlsxTrapFanNumber_Object = MibScalar
wlsxTrapFanNumber = _WlsxTrapFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 31),
    _WlsxTrapFanNumber_Type()
)
wlsxTrapFanNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapFanNumber.setStatus("current")


class _WlsxTrapVoltageType_Type(DisplayString):
    """Custom type wlsxTrapVoltageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapVoltageType_Type.__name__ = "DisplayString"
_WlsxTrapVoltageType_Object = MibScalar
wlsxTrapVoltageType = _WlsxTrapVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 32),
    _WlsxTrapVoltageType_Type()
)
wlsxTrapVoltageType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVoltageType.setStatus("current")


class _WlsxTrapVoltageValue_Type(DisplayString):
    """Custom type wlsxTrapVoltageValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapVoltageValue_Type.__name__ = "DisplayString"
_WlsxTrapVoltageValue_Object = MibScalar
wlsxTrapVoltageValue = _WlsxTrapVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 33),
    _WlsxTrapVoltageValue_Type()
)
wlsxTrapVoltageValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVoltageValue.setStatus("current")
_WlsxTrapStationBlackListReason_Type = ArubaBlackListReason
_WlsxTrapStationBlackListReason_Object = MibScalar
wlsxTrapStationBlackListReason = _WlsxTrapStationBlackListReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 34),
    _WlsxTrapStationBlackListReason_Type()
)
wlsxTrapStationBlackListReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapStationBlackListReason.setStatus("current")
_WlsxTrapSpoofedIpAddress_Type = IpAddress
_WlsxTrapSpoofedIpAddress_Object = MibScalar
wlsxTrapSpoofedIpAddress = _WlsxTrapSpoofedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 35),
    _WlsxTrapSpoofedIpAddress_Type()
)
wlsxTrapSpoofedIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedIpAddress.setStatus("current")
_WlsxTrapSpoofedOldPhyAddress_Type = MacAddress
_WlsxTrapSpoofedOldPhyAddress_Object = MibScalar
wlsxTrapSpoofedOldPhyAddress = _WlsxTrapSpoofedOldPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 36),
    _WlsxTrapSpoofedOldPhyAddress_Type()
)
wlsxTrapSpoofedOldPhyAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedOldPhyAddress.setStatus("current")
_WlsxTrapSpoofedNewPhyAddress_Type = MacAddress
_WlsxTrapSpoofedNewPhyAddress_Object = MibScalar
wlsxTrapSpoofedNewPhyAddress = _WlsxTrapSpoofedNewPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 37),
    _WlsxTrapSpoofedNewPhyAddress_Type()
)
wlsxTrapSpoofedNewPhyAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedNewPhyAddress.setStatus("current")


class _WlsxTrapDBName_Type(DisplayString):
    """Custom type wlsxTrapDBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapDBName_Type.__name__ = "DisplayString"
_WlsxTrapDBName_Object = MibScalar
wlsxTrapDBName = _WlsxTrapDBName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 38),
    _WlsxTrapDBName_Type()
)
wlsxTrapDBName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBName.setStatus("current")


class _WlsxTrapDBUserName_Type(DisplayString):
    """Custom type wlsxTrapDBUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapDBUserName_Type.__name__ = "DisplayString"
_WlsxTrapDBUserName_Object = MibScalar
wlsxTrapDBUserName = _WlsxTrapDBUserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 39),
    _WlsxTrapDBUserName_Type()
)
wlsxTrapDBUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBUserName.setStatus("current")


class _WlsxTrapDBIpAddress_Type(DisplayString):
    """Custom type wlsxTrapDBIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapDBIpAddress_Type.__name__ = "DisplayString"
_WlsxTrapDBIpAddress_Object = MibScalar
wlsxTrapDBIpAddress = _WlsxTrapDBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 40),
    _WlsxTrapDBIpAddress_Type()
)
wlsxTrapDBIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBIpAddress.setStatus("current")
_WlsxTrapDBType_Type = ArubaDBType
_WlsxTrapDBType_Object = MibScalar
wlsxTrapDBType = _WlsxTrapDBType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 41),
    _WlsxTrapDBType_Type()
)
wlsxTrapDBType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBType.setStatus("current")
_WlsxTrapVrrpID_Type = Integer32
_WlsxTrapVrrpID_Object = MibScalar
wlsxTrapVrrpID = _WlsxTrapVrrpID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 42),
    _WlsxTrapVrrpID_Type()
)
wlsxTrapVrrpID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVrrpID.setStatus("current")
_WlsxTrapVrrpMasterIp_Type = IpAddress
_WlsxTrapVrrpMasterIp_Object = MibScalar
wlsxTrapVrrpMasterIp = _WlsxTrapVrrpMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 43),
    _WlsxTrapVrrpMasterIp_Type()
)
wlsxTrapVrrpMasterIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVrrpMasterIp.setStatus("current")
_WlsxTrapVrrpOperState_Type = ArubaVrrpState
_WlsxTrapVrrpOperState_Object = MibScalar
wlsxTrapVrrpOperState = _WlsxTrapVrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 44),
    _WlsxTrapVrrpOperState_Type()
)
wlsxTrapVrrpOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVrrpOperState.setStatus("current")


class _WlsxTrapESIServerGrpName_Type(DisplayString):
    """Custom type wlsxTrapESIServerGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapESIServerGrpName_Type.__name__ = "DisplayString"
_WlsxTrapESIServerGrpName_Object = MibScalar
wlsxTrapESIServerGrpName = _WlsxTrapESIServerGrpName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 45),
    _WlsxTrapESIServerGrpName_Type()
)
wlsxTrapESIServerGrpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapESIServerGrpName.setStatus("current")


class _WlsxTrapESIServerName_Type(DisplayString):
    """Custom type wlsxTrapESIServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapESIServerName_Type.__name__ = "DisplayString"
_WlsxTrapESIServerName_Object = MibScalar
wlsxTrapESIServerName = _WlsxTrapESIServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 46),
    _WlsxTrapESIServerName_Type()
)
wlsxTrapESIServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapESIServerName.setStatus("current")
_WlsxTrapESIServerIpAddress_Type = IpAddress
_WlsxTrapESIServerIpAddress_Object = MibScalar
wlsxTrapESIServerIpAddress = _WlsxTrapESIServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 47),
    _WlsxTrapESIServerIpAddress_Type()
)
wlsxTrapESIServerIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapESIServerIpAddress.setStatus("current")
_WlsxTrapLicenseDaysRemaining_Type = Integer32
_WlsxTrapLicenseDaysRemaining_Object = MibScalar
wlsxTrapLicenseDaysRemaining = _WlsxTrapLicenseDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 48),
    _WlsxTrapLicenseDaysRemaining_Type()
)
wlsxTrapLicenseDaysRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLicenseDaysRemaining.setStatus("current")
_WlsxTrapSwitchIp_Type = IpAddress
_WlsxTrapSwitchIp_Object = MibScalar
wlsxTrapSwitchIp = _WlsxTrapSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 49),
    _WlsxTrapSwitchIp_Type()
)
wlsxTrapSwitchIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSwitchIp.setStatus("current")
_WlsxTrapSwitchRole_Type = ArubaSwitchRole
_WlsxTrapSwitchRole_Object = MibScalar
wlsxTrapSwitchRole = _WlsxTrapSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 50),
    _WlsxTrapSwitchRole_Type()
)
wlsxTrapSwitchRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSwitchRole.setStatus("current")
_WlsxTrapUserIpAddress_Type = IpAddress
_WlsxTrapUserIpAddress_Object = MibScalar
wlsxTrapUserIpAddress = _WlsxTrapUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 51),
    _WlsxTrapUserIpAddress_Type()
)
wlsxTrapUserIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserIpAddress.setStatus("current")
_WlsxTrapUserPhyAddress_Type = MacAddress
_WlsxTrapUserPhyAddress_Object = MibScalar
wlsxTrapUserPhyAddress = _WlsxTrapUserPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 52),
    _WlsxTrapUserPhyAddress_Type()
)
wlsxTrapUserPhyAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserPhyAddress.setStatus("current")


class _WlsxTrapUserName_Type(DisplayString):
    """Custom type wlsxTrapUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUserName_Type.__name__ = "DisplayString"
_WlsxTrapUserName_Object = MibScalar
wlsxTrapUserName = _WlsxTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 53),
    _WlsxTrapUserName_Type()
)
wlsxTrapUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserName.setStatus("current")


class _WlsxTrapUserRole_Type(DisplayString):
    """Custom type wlsxTrapUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUserRole_Type.__name__ = "DisplayString"
_WlsxTrapUserRole_Object = MibScalar
wlsxTrapUserRole = _WlsxTrapUserRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 54),
    _WlsxTrapUserRole_Type()
)
wlsxTrapUserRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserRole.setStatus("current")
_WlsxTrapUserAuthenticationMethod_Type = ArubaAuthenticationMethods
_WlsxTrapUserAuthenticationMethod_Object = MibScalar
wlsxTrapUserAuthenticationMethod = _WlsxTrapUserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 55),
    _WlsxTrapUserAuthenticationMethod_Type()
)
wlsxTrapUserAuthenticationMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserAuthenticationMethod.setStatus("current")
_WlsxTrapAPRadioNumber_Type = Integer32
_WlsxTrapAPRadioNumber_Object = MibScalar
wlsxTrapAPRadioNumber = _WlsxTrapAPRadioNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 56),
    _WlsxTrapAPRadioNumber_Type()
)
wlsxTrapAPRadioNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPRadioNumber.setStatus("current")


class _WlsxTrapRogueInfoURL_Type(DisplayString):
    """Custom type wlsxTrapRogueInfoURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapRogueInfoURL_Type.__name__ = "DisplayString"
_WlsxTrapRogueInfoURL_Object = MibScalar
wlsxTrapRogueInfoURL = _WlsxTrapRogueInfoURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 57),
    _WlsxTrapRogueInfoURL_Type()
)
wlsxTrapRogueInfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapRogueInfoURL.setStatus("current")


class _WlsxTrapInterferingAPInfoURL_Type(DisplayString):
    """Custom type wlsxTrapInterferingAPInfoURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapInterferingAPInfoURL_Type.__name__ = "DisplayString"
_WlsxTrapInterferingAPInfoURL_Object = MibScalar
wlsxTrapInterferingAPInfoURL = _WlsxTrapInterferingAPInfoURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 58),
    _WlsxTrapInterferingAPInfoURL_Type()
)
wlsxTrapInterferingAPInfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapInterferingAPInfoURL.setStatus("current")
_WlsxTrapPortNumber_Type = Integer32
_WlsxTrapPortNumber_Object = MibScalar
wlsxTrapPortNumber = _WlsxTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 59),
    _WlsxTrapPortNumber_Type()
)
wlsxTrapPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortNumber.setStatus("current")
_WlsxTrapTime_Type = DateAndTime
_WlsxTrapTime_Object = MibScalar
wlsxTrapTime = _WlsxTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 60),
    _WlsxTrapTime_Type()
)
wlsxTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTime.setStatus("current")
_WlsxTrapHostIp_Type = IpAddress
_WlsxTrapHostIp_Object = MibScalar
wlsxTrapHostIp = _WlsxTrapHostIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 61),
    _WlsxTrapHostIp_Type()
)
wlsxTrapHostIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapHostIp.setStatus("current")
_WlsxTrapHostPort_Type = Integer32
_WlsxTrapHostPort_Object = MibScalar
wlsxTrapHostPort = _WlsxTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 62),
    _WlsxTrapHostPort_Type()
)
wlsxTrapHostPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapHostPort.setStatus("current")
_WlsxTrapConfigurationId_Type = Integer32
_WlsxTrapConfigurationId_Object = MibScalar
wlsxTrapConfigurationId = _WlsxTrapConfigurationId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 63),
    _WlsxTrapConfigurationId_Type()
)
wlsxTrapConfigurationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapConfigurationId.setStatus("current")


class _WlsxTrapCTSURL_Type(DisplayString):
    """Custom type wlsxTrapCTSURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCTSURL_Type.__name__ = "DisplayString"
_WlsxTrapCTSURL_Object = MibScalar
wlsxTrapCTSURL = _WlsxTrapCTSURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 64),
    _WlsxTrapCTSURL_Type()
)
wlsxTrapCTSURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCTSURL.setStatus("current")


class _WlsxTrapCTSTransferType_Type(DisplayString):
    """Custom type wlsxTrapCTSTransferType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCTSTransferType_Type.__name__ = "DisplayString"
_WlsxTrapCTSTransferType_Object = MibScalar
wlsxTrapCTSTransferType = _WlsxTrapCTSTransferType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 65),
    _WlsxTrapCTSTransferType_Type()
)
wlsxTrapCTSTransferType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCTSTransferType.setStatus("current")
_WlsxTrapConfigurationState_Type = ArubaConfigurationState
_WlsxTrapConfigurationState_Object = MibScalar
wlsxTrapConfigurationState = _WlsxTrapConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 66),
    _WlsxTrapConfigurationState_Type()
)
wlsxTrapConfigurationState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapConfigurationState.setStatus("current")


class _WlsxTrapUpdateFailureReason_Type(DisplayString):
    """Custom type wlsxTrapUpdateFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUpdateFailureReason_Type.__name__ = "DisplayString"
_WlsxTrapUpdateFailureReason_Object = MibScalar
wlsxTrapUpdateFailureReason = _WlsxTrapUpdateFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 67),
    _WlsxTrapUpdateFailureReason_Type()
)
wlsxTrapUpdateFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUpdateFailureReason.setStatus("current")


class _WlsxTrapUpdateFailedObj_Type(DisplayString):
    """Custom type wlsxTrapUpdateFailedObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUpdateFailedObj_Type.__name__ = "DisplayString"
_WlsxTrapUpdateFailedObj_Object = MibScalar
wlsxTrapUpdateFailedObj = _WlsxTrapUpdateFailedObj_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 68),
    _WlsxTrapUpdateFailedObj_Type()
)
wlsxTrapUpdateFailedObj.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUpdateFailedObj.setStatus("current")
_WlsxTrapTableEntryChangeType_Type = ArubaConfigurationChangeType
_WlsxTrapTableEntryChangeType_Object = MibScalar
wlsxTrapTableEntryChangeType = _WlsxTrapTableEntryChangeType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 69),
    _WlsxTrapTableEntryChangeType_Type()
)
wlsxTrapTableEntryChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTableEntryChangeType.setStatus("current")


class _WlsxTrapGlobalConfigObj_Type(DisplayString):
    """Custom type wlsxTrapGlobalConfigObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapGlobalConfigObj_Type.__name__ = "DisplayString"
_WlsxTrapGlobalConfigObj_Object = MibScalar
wlsxTrapGlobalConfigObj = _WlsxTrapGlobalConfigObj_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 70),
    _WlsxTrapGlobalConfigObj_Type()
)
wlsxTrapGlobalConfigObj.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapGlobalConfigObj.setStatus("current")
_WlsxTrapTableGenNumber_Type = Integer32
_WlsxTrapTableGenNumber_Object = MibScalar
wlsxTrapTableGenNumber = _WlsxTrapTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 71),
    _WlsxTrapTableGenNumber_Type()
)
wlsxTrapTableGenNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTableGenNumber.setStatus("current")
_WlsxTrapLicenseId_Type = Integer32
_WlsxTrapLicenseId_Object = MibScalar
wlsxTrapLicenseId = _WlsxTrapLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 72),
    _WlsxTrapLicenseId_Type()
)
wlsxTrapLicenseId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLicenseId.setStatus("current")
_WlsxTrapConfidenceLevel_Type = Integer32
_WlsxTrapConfidenceLevel_Object = MibScalar
wlsxTrapConfidenceLevel = _WlsxTrapConfidenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 73),
    _WlsxTrapConfidenceLevel_Type()
)
wlsxTrapConfidenceLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapConfidenceLevel.setStatus("current")


class _WlsxTrapMissingLicenses_Type(DisplayString):
    """Custom type wlsxTrapMissingLicenses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapMissingLicenses_Type.__name__ = "DisplayString"
_WlsxTrapMissingLicenses_Object = MibScalar
wlsxTrapMissingLicenses = _WlsxTrapMissingLicenses_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 74),
    _WlsxTrapMissingLicenses_Type()
)
wlsxTrapMissingLicenses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMissingLicenses.setStatus("current")
_WlsxVoiceCurrentNumCdr_Type = Integer32
_WlsxVoiceCurrentNumCdr_Object = MibScalar
wlsxVoiceCurrentNumCdr = _WlsxVoiceCurrentNumCdr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 75),
    _WlsxVoiceCurrentNumCdr_Type()
)
wlsxVoiceCurrentNumCdr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxVoiceCurrentNumCdr.setStatus("current")
_WlsxTrapTunnelId_Type = Integer32
_WlsxTrapTunnelId_Object = MibScalar
wlsxTrapTunnelId = _WlsxTrapTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 76),
    _WlsxTrapTunnelId_Type()
)
wlsxTrapTunnelId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelId.setStatus("current")
_WlsxTrapTunnelStatus_Type = Integer32
_WlsxTrapTunnelStatus_Object = MibScalar
wlsxTrapTunnelStatus = _WlsxTrapTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 77),
    _WlsxTrapTunnelStatus_Type()
)
wlsxTrapTunnelStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelStatus.setStatus("current")


class _WlsxTrapTunnelUpReason_Type(DisplayString):
    """Custom type wlsxTrapTunnelUpReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTunnelUpReason_Type.__name__ = "DisplayString"
_WlsxTrapTunnelUpReason_Object = MibScalar
wlsxTrapTunnelUpReason = _WlsxTrapTunnelUpReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 78),
    _WlsxTrapTunnelUpReason_Type()
)
wlsxTrapTunnelUpReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelUpReason.setStatus("current")


class _WlsxTrapTunnelDownReason_Type(DisplayString):
    """Custom type wlsxTrapTunnelDownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTunnelDownReason_Type.__name__ = "DisplayString"
_WlsxTrapTunnelDownReason_Object = MibScalar
wlsxTrapTunnelDownReason = _WlsxTrapTunnelDownReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 79),
    _WlsxTrapTunnelDownReason_Type()
)
wlsxTrapTunnelDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelDownReason.setStatus("current")


class _WlsxTrapApSerialNumber_Type(DisplayString):
    """Custom type wlsxTrapApSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapApSerialNumber_Type.__name__ = "DisplayString"
_WlsxTrapApSerialNumber_Object = MibScalar
wlsxTrapApSerialNumber = _WlsxTrapApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 80),
    _WlsxTrapApSerialNumber_Type()
)
wlsxTrapApSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApSerialNumber.setStatus("current")


class _WlsxTrapTimeStr_Type(DisplayString):
    """Custom type wlsxTrapTimeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTimeStr_Type.__name__ = "DisplayString"
_WlsxTrapTimeStr_Object = MibScalar
wlsxTrapTimeStr = _WlsxTrapTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 81),
    _WlsxTrapTimeStr_Type()
)
wlsxTrapTimeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTimeStr.setStatus("current")
_WlsxTrapMasterIp_Type = IpAddress
_WlsxTrapMasterIp_Object = MibScalar
wlsxTrapMasterIp = _WlsxTrapMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 82),
    _WlsxTrapMasterIp_Type()
)
wlsxTrapMasterIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMasterIp.setStatus("current")
_WlsxTrapLocalIp_Type = IpAddress
_WlsxTrapLocalIp_Object = MibScalar
wlsxTrapLocalIp = _WlsxTrapLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 83),
    _WlsxTrapLocalIp_Type()
)
wlsxTrapLocalIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLocalIp.setStatus("current")


class _WlsxTrapMasterName_Type(DisplayString):
    """Custom type wlsxTrapMasterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapMasterName_Type.__name__ = "DisplayString"
_WlsxTrapMasterName_Object = MibScalar
wlsxTrapMasterName = _WlsxTrapMasterName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 84),
    _WlsxTrapMasterName_Type()
)
wlsxTrapMasterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMasterName.setStatus("current")


class _WlsxTrapLocalName_Type(DisplayString):
    """Custom type wlsxTrapLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapLocalName_Type.__name__ = "DisplayString"
_WlsxTrapLocalName_Object = MibScalar
wlsxTrapLocalName = _WlsxTrapLocalName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 85),
    _WlsxTrapLocalName_Type()
)
wlsxTrapLocalName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLocalName.setStatus("current")
_WlsxTrapPrimaryControllerIp_Type = IpAddress
_WlsxTrapPrimaryControllerIp_Object = MibScalar
wlsxTrapPrimaryControllerIp = _WlsxTrapPrimaryControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 86),
    _WlsxTrapPrimaryControllerIp_Type()
)
wlsxTrapPrimaryControllerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPrimaryControllerIp.setStatus("current")
_WlsxTrapBackupControllerIp_Type = IpAddress
_WlsxTrapBackupControllerIp_Object = MibScalar
wlsxTrapBackupControllerIp = _WlsxTrapBackupControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 87),
    _WlsxTrapBackupControllerIp_Type()
)
wlsxTrapBackupControllerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapBackupControllerIp.setStatus("current")


class _WlsxTrapSpoofedFrameType_Type(DisplayString):
    """Custom type wlsxTrapSpoofedFrameType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapSpoofedFrameType_Type.__name__ = "DisplayString"
_WlsxTrapSpoofedFrameType_Object = MibScalar
wlsxTrapSpoofedFrameType = _WlsxTrapSpoofedFrameType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 88),
    _WlsxTrapSpoofedFrameType_Type()
)
wlsxTrapSpoofedFrameType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedFrameType.setStatus("current")


class _WlsxTrapAssociationType_Type(DisplayString):
    """Custom type wlsxTrapAssociationType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAssociationType_Type.__name__ = "DisplayString"
_WlsxTrapAssociationType_Object = MibScalar
wlsxTrapAssociationType = _WlsxTrapAssociationType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 89),
    _WlsxTrapAssociationType_Type()
)
wlsxTrapAssociationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAssociationType.setStatus("current")
_WlsxTrapDeviceIpAddress_Type = IpAddress
_WlsxTrapDeviceIpAddress_Object = MibScalar
wlsxTrapDeviceIpAddress = _WlsxTrapDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 90),
    _WlsxTrapDeviceIpAddress_Type()
)
wlsxTrapDeviceIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDeviceIpAddress.setStatus("current")
_WlsxTrapDeviceMac_Type = MacAddress
_WlsxTrapDeviceMac_Object = MibScalar
wlsxTrapDeviceMac = _WlsxTrapDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 91),
    _WlsxTrapDeviceMac_Type()
)
wlsxTrapDeviceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDeviceMac.setStatus("current")
_WlsxTrapVcIpAddress_Type = IpAddress
_WlsxTrapVcIpAddress_Object = MibScalar
wlsxTrapVcIpAddress = _WlsxTrapVcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 92),
    _WlsxTrapVcIpAddress_Type()
)
wlsxTrapVcIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVcIpAddress.setStatus("current")
_WlsxTrapVcMacAddress_Type = MacAddress
_WlsxTrapVcMacAddress_Object = MibScalar
wlsxTrapVcMacAddress = _WlsxTrapVcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 93),
    _WlsxTrapVcMacAddress_Type()
)
wlsxTrapVcMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVcMacAddress.setStatus("current")


class _WlsxTrapAPName_Type(DisplayString):
    """Custom type wlsxTrapAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAPName_Type.__name__ = "DisplayString"
_WlsxTrapAPName_Object = MibScalar
wlsxTrapAPName = _WlsxTrapAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 94),
    _WlsxTrapAPName_Type()
)
wlsxTrapAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPName.setStatus("current")
_WlsxTrapApMode_Type = Integer32
_WlsxTrapApMode_Object = MibScalar
wlsxTrapApMode = _WlsxTrapApMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 95),
    _WlsxTrapApMode_Type()
)
wlsxTrapApMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApMode.setStatus("current")
_WlsxTrapAPPrevChannel_Type = Integer32
_WlsxTrapAPPrevChannel_Object = MibScalar
wlsxTrapAPPrevChannel = _WlsxTrapAPPrevChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 96),
    _WlsxTrapAPPrevChannel_Type()
)
wlsxTrapAPPrevChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevChannel.setStatus("current")
_WlsxTrapAPPrevChannelSec_Type = ArubaHTExtChannel
_WlsxTrapAPPrevChannelSec_Object = MibScalar
wlsxTrapAPPrevChannelSec = _WlsxTrapAPPrevChannelSec_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 97),
    _WlsxTrapAPPrevChannelSec_Type()
)
wlsxTrapAPPrevChannelSec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevChannelSec.setStatus("current")
_WlsxTrapAPPrevTxPower_Type = Integer32
_WlsxTrapAPPrevTxPower_Object = MibScalar
wlsxTrapAPPrevTxPower = _WlsxTrapAPPrevTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 98),
    _WlsxTrapAPPrevTxPower_Type()
)
wlsxTrapAPPrevTxPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevTxPower.setStatus("current")
_WlsxTrapAPCurMode_Type = ArubaAccessPointMode
_WlsxTrapAPCurMode_Object = MibScalar
wlsxTrapAPCurMode = _WlsxTrapAPCurMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 99),
    _WlsxTrapAPCurMode_Type()
)
wlsxTrapAPCurMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPCurMode.setStatus("current")
_WlsxTrapAPPrevMode_Type = ArubaAccessPointMode
_WlsxTrapAPPrevMode_Object = MibScalar
wlsxTrapAPPrevMode = _WlsxTrapAPPrevMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 100),
    _WlsxTrapAPPrevMode_Type()
)
wlsxTrapAPPrevMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevMode.setStatus("current")
_WlsxTrapAPARMChangeReason_Type = ArubaARMChangeReason
_WlsxTrapAPARMChangeReason_Object = MibScalar
wlsxTrapAPARMChangeReason = _WlsxTrapAPARMChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 101),
    _WlsxTrapAPARMChangeReason_Type()
)
wlsxTrapAPARMChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPARMChangeReason.setStatus("current")
_WlsxTrapAPChannelSec_Type = ArubaHTExtChannel
_WlsxTrapAPChannelSec_Object = MibScalar
wlsxTrapAPChannelSec = _WlsxTrapAPChannelSec_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 102),
    _WlsxTrapAPChannelSec_Type()
)
wlsxTrapAPChannelSec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPChannelSec.setStatus("current")
_WlsxTrapUserAttributeChangeType_Type = ArubaConfigurationChangeType
_WlsxTrapUserAttributeChangeType_Object = MibScalar
wlsxTrapUserAttributeChangeType = _WlsxTrapUserAttributeChangeType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 103),
    _WlsxTrapUserAttributeChangeType_Type()
)
wlsxTrapUserAttributeChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserAttributeChangeType.setStatus("current")
_WlsxTrapApControllerIp_Type = IpAddress
_WlsxTrapApControllerIp_Object = MibScalar
wlsxTrapApControllerIp = _WlsxTrapApControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 104),
    _WlsxTrapApControllerIp_Type()
)
wlsxTrapApControllerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApControllerIp.setStatus("current")
_WlsxTrapApMasterStatus_Type = ArubaAPMasterStatus
_WlsxTrapApMasterStatus_Object = MibScalar
wlsxTrapApMasterStatus = _WlsxTrapApMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 105),
    _WlsxTrapApMasterStatus_Type()
)
wlsxTrapApMasterStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApMasterStatus.setStatus("current")


class _WlsxTrapCaName_Type(DisplayString):
    """Custom type wlsxTrapCaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCaName_Type.__name__ = "DisplayString"
_WlsxTrapCaName_Object = MibScalar
wlsxTrapCaName = _WlsxTrapCaName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 106),
    _WlsxTrapCaName_Type()
)
wlsxTrapCaName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCaName.setStatus("current")


class _WlsxTrapCrlName_Type(DisplayString):
    """Custom type wlsxTrapCrlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCrlName_Type.__name__ = "DisplayString"
_WlsxTrapCrlName_Object = MibScalar
wlsxTrapCrlName = _WlsxTrapCrlName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 107),
    _WlsxTrapCrlName_Type()
)
wlsxTrapCrlName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCrlName.setStatus("current")
_WlsxTrapCount_Type = Integer32
_WlsxTrapCount_Object = MibScalar
wlsxTrapCount = _WlsxTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 108),
    _WlsxTrapCount_Type()
)
wlsxTrapCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCount.setStatus("current")
_WlsxTrapPowerSupplyNumber_Type = Integer32
_WlsxTrapPowerSupplyNumber_Object = MibScalar
wlsxTrapPowerSupplyNumber = _WlsxTrapPowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 109),
    _WlsxTrapPowerSupplyNumber_Type()
)
wlsxTrapPowerSupplyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPowerSupplyNumber.setStatus("current")
_WlsxTrapFanTrayNumber_Type = Integer32
_WlsxTrapFanTrayNumber_Object = MibScalar
wlsxTrapFanTrayNumber = _WlsxTrapFanTrayNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 110),
    _WlsxTrapFanTrayNumber_Type()
)
wlsxTrapFanTrayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapFanTrayNumber.setStatus("current")
_WlsxTrapClientClassification_Type = ArubaStationType
_WlsxTrapClientClassification_Object = MibScalar
wlsxTrapClientClassification = _WlsxTrapClientClassification_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 111),
    _WlsxTrapClientClassification_Type()
)
wlsxTrapClientClassification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapClientClassification.setStatus("current")
_WlsxThresholdResourceType_Type = ArubaThresholdResourceType
_WlsxThresholdResourceType_Object = MibScalar
wlsxThresholdResourceType = _WlsxThresholdResourceType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 112),
    _WlsxThresholdResourceType_Type()
)
wlsxThresholdResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxThresholdResourceType.setStatus("current")


class _WlsxThresholdResourceName_Type(DisplayString):
    """Custom type wlsxThresholdResourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxThresholdResourceName_Type.__name__ = "DisplayString"
_WlsxThresholdResourceName_Object = MibScalar
wlsxThresholdResourceName = _WlsxThresholdResourceName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 113),
    _WlsxThresholdResourceName_Type()
)
wlsxThresholdResourceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxThresholdResourceName.setStatus("current")
_WlsxThresholdValue_Type = Integer32
_WlsxThresholdValue_Object = MibScalar
wlsxThresholdValue = _WlsxThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 114),
    _WlsxThresholdValue_Type()
)
wlsxThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxThresholdValue.setStatus("current")
_WlsxResourceValue_Type = Integer32
_WlsxResourceValue_Object = MibScalar
wlsxResourceValue = _WlsxResourceValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 115),
    _WlsxResourceValue_Type()
)
wlsxResourceValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxResourceValue.setStatus("current")
_WlsxStackPrevSlot_Type = Integer32
_WlsxStackPrevSlot_Object = MibScalar
wlsxStackPrevSlot = _WlsxStackPrevSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 116),
    _WlsxStackPrevSlot_Type()
)
wlsxStackPrevSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackPrevSlot.setStatus("current")
_WlsxStackCurrentSlot_Type = Integer32
_WlsxStackCurrentSlot_Object = MibScalar
wlsxStackCurrentSlot = _WlsxStackCurrentSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 117),
    _WlsxStackCurrentSlot_Type()
)
wlsxStackCurrentSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackCurrentSlot.setStatus("current")
_WlsxStackPrevState_Type = ArubaStackState
_WlsxStackPrevState_Object = MibScalar
wlsxStackPrevState = _WlsxStackPrevState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 118),
    _WlsxStackPrevState_Type()
)
wlsxStackPrevState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackPrevState.setStatus("current")
_WlsxStackCurrentState_Type = ArubaStackState
_WlsxStackCurrentState_Object = MibScalar
wlsxStackCurrentState = _WlsxStackCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 119),
    _WlsxStackCurrentState_Type()
)
wlsxStackCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackCurrentState.setStatus("current")
_WlsxStackChangeEvent_Type = ArubaStackChangeEvent
_WlsxStackChangeEvent_Object = MibScalar
wlsxStackChangeEvent = _WlsxStackChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 120),
    _WlsxStackChangeEvent_Type()
)
wlsxStackChangeEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackChangeEvent.setStatus("current")
_WlsxStackProtoIfTopoJoined_Type = ArubaStackIfTopoJoined
_WlsxStackProtoIfTopoJoined_Object = MibScalar
wlsxStackProtoIfTopoJoined = _WlsxStackProtoIfTopoJoined_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 121),
    _WlsxStackProtoIfTopoJoined_Type()
)
wlsxStackProtoIfTopoJoined.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackProtoIfTopoJoined.setStatus("current")
_WlsxStackMemberMacAddress_Type = MacAddress
_WlsxStackMemberMacAddress_Object = MibScalar
wlsxStackMemberMacAddress = _WlsxStackMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 122),
    _WlsxStackMemberMacAddress_Type()
)
wlsxStackMemberMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackMemberMacAddress.setStatus("current")
_WlsxStackMemberSlotNumber_Type = Integer32
_WlsxStackMemberSlotNumber_Object = MibScalar
wlsxStackMemberSlotNumber = _WlsxStackMemberSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 123),
    _WlsxStackMemberSlotNumber_Type()
)
wlsxStackMemberSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackMemberSlotNumber.setStatus("current")


class _WlsxStackIfName_Type(DisplayString):
    """Custom type wlsxStackIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxStackIfName_Type.__name__ = "DisplayString"
_WlsxStackIfName_Object = MibScalar
wlsxStackIfName = _WlsxStackIfName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 124),
    _WlsxStackIfName_Type()
)
wlsxStackIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxStackIfName.setStatus("current")
_WlsxTrapLicenseServerDaysRemaining_Type = Integer32
_WlsxTrapLicenseServerDaysRemaining_Object = MibScalar
wlsxTrapLicenseServerDaysRemaining = _WlsxTrapLicenseServerDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 125),
    _WlsxTrapLicenseServerDaysRemaining_Type()
)
wlsxTrapLicenseServerDaysRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLicenseServerDaysRemaining.setStatus("current")
_WlsxTrapLicenseClientDaysRemaining_Type = Integer32
_WlsxTrapLicenseClientDaysRemaining_Object = MibScalar
wlsxTrapLicenseClientDaysRemaining = _WlsxTrapLicenseClientDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 126),
    _WlsxTrapLicenseClientDaysRemaining_Type()
)
wlsxTrapLicenseClientDaysRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLicenseClientDaysRemaining.setStatus("current")
_WlsxIfIndex_Type = InterfaceIndex
_WlsxIfIndex_Object = MibScalar
wlsxIfIndex = _WlsxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 127),
    _WlsxIfIndex_Type()
)
wlsxIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxIfIndex.setStatus("current")
_WlsxIfState_Type = ArubaIfState
_WlsxIfState_Object = MibScalar
wlsxIfState = _WlsxIfState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 128),
    _WlsxIfState_Type()
)
wlsxIfState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxIfState.setStatus("current")
_WlsxIfStateChangeReason_Type = ArubaIfStateChangeReason
_WlsxIfStateChangeReason_Object = MibScalar
wlsxIfStateChangeReason = _WlsxIfStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 129),
    _WlsxIfStateChangeReason_Type()
)
wlsxIfStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxIfStateChangeReason.setStatus("current")
_WlsxTrapAPPreviousUplinkType_Type = ArubaAPUplinkType
_WlsxTrapAPPreviousUplinkType_Object = MibScalar
wlsxTrapAPPreviousUplinkType = _WlsxTrapAPPreviousUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 130),
    _WlsxTrapAPPreviousUplinkType_Type()
)
wlsxTrapAPPreviousUplinkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPreviousUplinkType.setStatus("current")
_WlsxTrapAPPreviousUplinkActiveTime_Type = TimeTicks
_WlsxTrapAPPreviousUplinkActiveTime_Object = MibScalar
wlsxTrapAPPreviousUplinkActiveTime = _WlsxTrapAPPreviousUplinkActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 131),
    _WlsxTrapAPPreviousUplinkActiveTime_Type()
)
wlsxTrapAPPreviousUplinkActiveTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPreviousUplinkActiveTime.setStatus("current")
_WlsxTrapAPActiveUplinkType_Type = ArubaAPUplinkType
_WlsxTrapAPActiveUplinkType_Object = MibScalar
wlsxTrapAPActiveUplinkType = _WlsxTrapAPActiveUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 132),
    _WlsxTrapAPActiveUplinkType_Type()
)
wlsxTrapAPActiveUplinkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPActiveUplinkType.setStatus("current")
_WlsxTrapAPUplinkChangeReason_Type = ArubaAPUplinkChangeReason
_WlsxTrapAPUplinkChangeReason_Object = MibScalar
wlsxTrapAPUplinkChangeReason = _WlsxTrapAPUplinkChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 133),
    _WlsxTrapAPUplinkChangeReason_Type()
)
wlsxTrapAPUplinkChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPUplinkChangeReason.setStatus("current")


class _WlsxTrapExpiringCertName_Type(DisplayString):
    """Custom type wlsxTrapExpiringCertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapExpiringCertName_Type.__name__ = "DisplayString"
_WlsxTrapExpiringCertName_Object = MibScalar
wlsxTrapExpiringCertName = _WlsxTrapExpiringCertName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 134),
    _WlsxTrapExpiringCertName_Type()
)
wlsxTrapExpiringCertName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapExpiringCertName.setStatus("current")


class _WlsxTrapExpiredCertName_Type(DisplayString):
    """Custom type wlsxTrapExpiredCertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapExpiredCertName_Type.__name__ = "DisplayString"
_WlsxTrapExpiredCertName_Object = MibScalar
wlsxTrapExpiredCertName = _WlsxTrapExpiredCertName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 135),
    _WlsxTrapExpiredCertName_Type()
)
wlsxTrapExpiredCertName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapExpiredCertName.setStatus("current")
_WlsxTrapHTMode_Type = Integer32
_WlsxTrapHTMode_Object = MibScalar
wlsxTrapHTMode = _WlsxTrapHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 136),
    _WlsxTrapHTMode_Type()
)
wlsxTrapHTMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapHTMode.setStatus("current")
_WlsxTrapPhyType_Type = Integer32
_WlsxTrapPhyType_Object = MibScalar
wlsxTrapPhyType = _WlsxTrapPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 137),
    _WlsxTrapPhyType_Type()
)
wlsxTrapPhyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPhyType.setStatus("current")


class _WlsxTrapAPManagedModeConfigFailure_Type(DisplayString):
    """Custom type wlsxTrapAPManagedModeConfigFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAPManagedModeConfigFailure_Type.__name__ = "DisplayString"
_WlsxTrapAPManagedModeConfigFailure_Object = MibScalar
wlsxTrapAPManagedModeConfigFailure = _WlsxTrapAPManagedModeConfigFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 138),
    _WlsxTrapAPManagedModeConfigFailure_Type()
)
wlsxTrapAPManagedModeConfigFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPManagedModeConfigFailure.setStatus("current")
_WlsxTrapAuthServerAddress_Type = IpAddress
_WlsxTrapAuthServerAddress_Object = MibScalar
wlsxTrapAuthServerAddress = _WlsxTrapAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 139),
    _WlsxTrapAuthServerAddress_Type()
)
wlsxTrapAuthServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthServerAddress.setStatus("current")


class _WlsxTrapPortalServerName_Type(DisplayString):
    """Custom type wlsxTrapPortalServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapPortalServerName_Type.__name__ = "DisplayString"
_WlsxTrapPortalServerName_Object = MibScalar
wlsxTrapPortalServerName = _WlsxTrapPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 140),
    _WlsxTrapPortalServerName_Type()
)
wlsxTrapPortalServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortalServerName.setStatus("current")


class _WlsxTrapPortalServerAddress_Type(DisplayString):
    """Custom type wlsxTrapPortalServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapPortalServerAddress_Type.__name__ = "DisplayString"
_WlsxTrapPortalServerAddress_Object = MibScalar
wlsxTrapPortalServerAddress = _WlsxTrapPortalServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 141),
    _WlsxTrapPortalServerAddress_Type()
)
wlsxTrapPortalServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortalServerAddress.setStatus("current")
_WlsxTrapPortalServerDownReason_Type = ArubaPortalServerDownReason
_WlsxTrapPortalServerDownReason_Object = MibScalar
wlsxTrapPortalServerDownReason = _WlsxTrapPortalServerDownReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 142),
    _WlsxTrapPortalServerDownReason_Type()
)
wlsxTrapPortalServerDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortalServerDownReason.setStatus("current")


class _WlsxTrapLicensePlatformMismatchKey_Type(DisplayString):
    """Custom type wlsxTrapLicensePlatformMismatchKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapLicensePlatformMismatchKey_Type.__name__ = "DisplayString"
_WlsxTrapLicensePlatformMismatchKey_Object = MibScalar
wlsxTrapLicensePlatformMismatchKey = _WlsxTrapLicensePlatformMismatchKey_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 143),
    _WlsxTrapLicensePlatformMismatchKey_Type()
)
wlsxTrapLicensePlatformMismatchKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLicensePlatformMismatchKey.setStatus("current")


class _WlsxTrapTargetAPName_Type(DisplayString):
    """Custom type wlsxTrapTargetAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTargetAPName_Type.__name__ = "DisplayString"
_WlsxTrapTargetAPName_Object = MibScalar
wlsxTrapTargetAPName = _WlsxTrapTargetAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 144),
    _WlsxTrapTargetAPName_Type()
)
wlsxTrapTargetAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPName.setStatus("current")
_WlsxTrapTargetAPMac_Type = MacAddress
_WlsxTrapTargetAPMac_Object = MibScalar
wlsxTrapTargetAPMac = _WlsxTrapTargetAPMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 145),
    _WlsxTrapTargetAPMac_Type()
)
wlsxTrapTargetAPMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPMac.setStatus("current")


class _WlsxTrapAPUSBStatus_Type(DisplayString):
    """Custom type wlsxTrapAPUSBStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAPUSBStatus_Type.__name__ = "DisplayString"
_WlsxTrapAPUSBStatus_Object = MibScalar
wlsxTrapAPUSBStatus = _WlsxTrapAPUSBStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 146),
    _WlsxTrapAPUSBStatus_Type()
)
wlsxTrapAPUSBStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPUSBStatus.setStatus("current")


class _WlsxTrapUSBVendorProductID_Type(DisplayString):
    """Custom type wlsxTrapUSBVendorProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUSBVendorProductID_Type.__name__ = "DisplayString"
_WlsxTrapUSBVendorProductID_Object = MibScalar
wlsxTrapUSBVendorProductID = _WlsxTrapUSBVendorProductID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 147),
    _WlsxTrapUSBVendorProductID_Type()
)
wlsxTrapUSBVendorProductID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUSBVendorProductID.setStatus("current")


class _WlsxTrapSwitchIpv6_Type(DisplayString):
    """Custom type wlsxTrapSwitchIpv6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapSwitchIpv6_Type.__name__ = "DisplayString"
_WlsxTrapSwitchIpv6_Object = MibScalar
wlsxTrapSwitchIpv6 = _WlsxTrapSwitchIpv6_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 148),
    _WlsxTrapSwitchIpv6_Type()
)
wlsxTrapSwitchIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSwitchIpv6.setStatus("current")


class _WlsxTrapStationBlackListReasonStr_Type(DisplayString):
    """Custom type wlsxTrapStationBlackListReasonStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapStationBlackListReasonStr_Type.__name__ = "DisplayString"
_WlsxTrapStationBlackListReasonStr_Object = MibScalar
wlsxTrapStationBlackListReasonStr = _WlsxTrapStationBlackListReasonStr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 149),
    _WlsxTrapStationBlackListReasonStr_Type()
)
wlsxTrapStationBlackListReasonStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapStationBlackListReasonStr.setStatus("current")


class _WlsxTrapPeerIpAddress_Type(DisplayString):
    """Custom type wlsxTrapPeerIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapPeerIpAddress_Type.__name__ = "DisplayString"
_WlsxTrapPeerIpAddress_Object = MibScalar
wlsxTrapPeerIpAddress = _WlsxTrapPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 150),
    _WlsxTrapPeerIpAddress_Type()
)
wlsxTrapPeerIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPeerIpAddress.setStatus("current")


class _WlsxTrapConnectionStatus_Type(DisplayString):
    """Custom type wlsxTrapConnectionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapConnectionStatus_Type.__name__ = "DisplayString"
_WlsxTrapConnectionStatus_Object = MibScalar
wlsxTrapConnectionStatus = _WlsxTrapConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 151),
    _WlsxTrapConnectionStatus_Type()
)
wlsxTrapConnectionStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapConnectionStatus.setStatus("current")
_WlsxTrapFailedVlan_Type = Integer32
_WlsxTrapFailedVlan_Object = MibScalar
wlsxTrapFailedVlan = _WlsxTrapFailedVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 152),
    _WlsxTrapFailedVlan_Type()
)
wlsxTrapFailedVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapFailedVlan.setStatus("current")


class _WlsxTrapMatchedIpv6_Type(DisplayString):
    """Custom type wlsxTrapMatchedIpv6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapMatchedIpv6_Type.__name__ = "DisplayString"
_WlsxTrapMatchedIpv6_Object = MibScalar
wlsxTrapMatchedIpv6 = _WlsxTrapMatchedIpv6_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 153),
    _WlsxTrapMatchedIpv6_Type()
)
wlsxTrapMatchedIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMatchedIpv6.setStatus("current")


class _WlsxTrapDeviceIpv6Address_Type(DisplayString):
    """Custom type wlsxTrapDeviceIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapDeviceIpv6Address_Type.__name__ = "DisplayString"
_WlsxTrapDeviceIpv6Address_Object = MibScalar
wlsxTrapDeviceIpv6Address = _WlsxTrapDeviceIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 154),
    _WlsxTrapDeviceIpv6Address_Type()
)
wlsxTrapDeviceIpv6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDeviceIpv6Address.setStatus("current")


class _WlsxTrapAuthFailureReason_Type(DisplayString):
    """Custom type wlsxTrapAuthFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAuthFailureReason_Type.__name__ = "DisplayString"
_WlsxTrapAuthFailureReason_Object = MibScalar
wlsxTrapAuthFailureReason = _WlsxTrapAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 1, 155),
    _WlsxTrapAuthFailureReason_Type()
)
wlsxTrapAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthFailureReason.setStatus("current")
_WlsxTrapDefinitionsGroup_ObjectIdentity = ObjectIdentity
wlsxTrapDefinitionsGroup = _WlsxTrapDefinitionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2)
)

# Managed Objects groups


# Notification objects

wlsxVlanLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1000)
)
wlsxVlanLinkUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapVlanId"),
        ("WLSX-TRAP-MIB", "wlsxTrapAdminStatus"),
        ("WLSX-TRAP-MIB", "wlsxTrapOperStatus"))
)
if mibBuilder.loadTexts:
    wlsxVlanLinkUp.setStatus(
        "current"
    )

wlsxVlanLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1001)
)
wlsxVlanLinkDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapVlanId"),
        ("WLSX-TRAP-MIB", "wlsxTrapAdminStatus"),
        ("WLSX-TRAP-MIB", "wlsxTrapOperStatus"))
)
if mibBuilder.loadTexts:
    wlsxVlanLinkDown.setStatus(
        "current"
    )

wlsxSignatureMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1002)
)
wlsxSignatureMatch.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignatureMatch.setStatus(
        "current"
    )

wlsxNodeRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1003)
)
wlsxNodeRateAnomaly.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxNodeRateAnomaly.setStatus(
        "current"
    )

wlsxNormalTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1004)
)
wlsxNormalTemperature.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTemperatureValue"))
)
if mibBuilder.loadTexts:
    wlsxNormalTemperature.setStatus(
        "current"
    )

wlsxProcessRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1005)
)
wlsxProcessRestart.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapProcessName"))
)
if mibBuilder.loadTexts:
    wlsxProcessRestart.setStatus(
        "current"
    )

wlsxFlashSpaceOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1006)
)
wlsxFlashSpaceOK.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxFlashSpaceOK.setStatus(
        "current"
    )

wlsxMemoryUsageOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1007)
)
wlsxMemoryUsageOK.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxMemoryUsageOK.setStatus(
        "current"
    )

wlsxPowerSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1008)
)
wlsxPowerSupplyOK.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxPowerSupplyOK.setStatus(
        "current"
    )

wlsxFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1009)
)
wlsxFanOK.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFanNumber"))
)
if mibBuilder.loadTexts:
    wlsxFanOK.setStatus(
        "current"
    )

wlsxInRangeVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1010)
)
wlsxInRangeVoltage.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapVoltageType"),
        ("WLSX-TRAP-MIB", "wlsxTrapVoltageValue"))
)
if mibBuilder.loadTexts:
    wlsxInRangeVoltage.setStatus(
        "current"
    )

wlsxCoverageHoleResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1011)
)
wlsxCoverageHoleResolved.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"))
)
if mibBuilder.loadTexts:
    wlsxCoverageHoleResolved.setStatus(
        "current"
    )

wlsxNSwitchIPChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1012)
)
wlsxNSwitchIPChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSwitchIp"))
)
if mibBuilder.loadTexts:
    wlsxNSwitchIPChanged.setStatus(
        "current"
    )

wlsxNSwitchRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1013)
)
wlsxNSwitchRoleChange.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSwitchRole"))
)
if mibBuilder.loadTexts:
    wlsxNSwitchRoleChange.setStatus(
        "current"
    )

wlsxNUserEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1014)
)
wlsxNUserEntryCreated.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryCreated.setStatus(
        "current"
    )

wlsxNUserEntryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1015)
)
wlsxNUserEntryDeleted.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryDeleted.setStatus(
        "current"
    )

wlsxNUserEntryAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1016)
)
wlsxNUserEntryAuthenticated.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserName"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserAuthenticationMethod"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserRole"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryAuthenticated.setStatus(
        "current"
    )

wlsxNUserEntryDeAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1017)
)
wlsxNUserEntryDeAuthenticated.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryDeAuthenticated.setStatus(
        "current"
    )

wlsxNUserAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1018)
)
wlsxNUserAuthenticationFailed.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserName"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxNUserAuthenticationFailed.setStatus(
        "current"
    )

wlsxNAuthServerReqTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1019)
)
wlsxNAuthServerReqTimedOut.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserName"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerReqTimedOut.setStatus(
        "current"
    )

wlsxNAuthServerTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1020)
)
wlsxNAuthServerTimedOut.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerTimeout"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserName"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerTimedOut.setStatus(
        "current"
    )

wlsxNAuthServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1021)
)
wlsxNAuthServerIsUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerIsUp.setStatus(
        "current"
    )

wlsxNAuthMaxUserEntries = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1022)
)
wlsxNAuthMaxUserEntries.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNAuthMaxUserEntries.setStatus(
        "current"
    )

wlsxNAuthMaxAclEntries = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1023)
)
wlsxNAuthMaxAclEntries.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNAuthMaxAclEntries.setStatus(
        "current"
    )

wlsxNAuthMaxBWContracts = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1024)
)
wlsxNAuthMaxBWContracts.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNAuthMaxBWContracts.setStatus(
        "current"
    )

wlsxNPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1025)
)
wlsxNPowerSupplyFailure.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNPowerSupplyFailure.setStatus(
        "current"
    )

wlsxNFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1026)
)
wlsxNFanFailure.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFanNumber"))
)
if mibBuilder.loadTexts:
    wlsxNFanFailure.setStatus(
        "current"
    )

wlsxNOutOfRangeVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1027)
)
wlsxNOutOfRangeVoltage.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapVoltageType"),
        ("WLSX-TRAP-MIB", "wlsxTrapVoltageValue"))
)
if mibBuilder.loadTexts:
    wlsxNOutOfRangeVoltage.setStatus(
        "current"
    )

wlsxNOutOfRangeTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1028)
)
wlsxNOutOfRangeTemperature.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTemperatureValue"))
)
if mibBuilder.loadTexts:
    wlsxNOutOfRangeTemperature.setStatus(
        "current"
    )

wlsxNLCInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1029)
)
wlsxNLCInserted.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCardSlot"))
)
if mibBuilder.loadTexts:
    wlsxNLCInserted.setStatus(
        "current"
    )

wlsxNSCInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1030)
)
wlsxNSCInserted.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCardSlot"))
)
if mibBuilder.loadTexts:
    wlsxNSCInserted.setStatus(
        "current"
    )

wlsxNGBICInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1031)
)
wlsxNGBICInserted.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNGBICInserted.setStatus(
        "current"
    )

wlsxNProcessDied = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1032)
)
wlsxNProcessDied.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapProcessName"))
)
if mibBuilder.loadTexts:
    wlsxNProcessDied.setStatus(
        "current"
    )

wlsxNProcessExceedsMemoryLimits = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1033)
)
wlsxNProcessExceedsMemoryLimits.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapProcessName"))
)
if mibBuilder.loadTexts:
    wlsxNProcessExceedsMemoryLimits.setStatus(
        "current"
    )

wlsxNLowOnFlashSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1034)
)
wlsxNLowOnFlashSpace.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNLowOnFlashSpace.setStatus(
        "current"
    )

wlsxNLowMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1035)
)
wlsxNLowMemory.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNLowMemory.setStatus(
        "current"
    )

wlsxNFanTrayRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1036)
)
wlsxNFanTrayRemoved.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNFanTrayRemoved.setStatus(
        "current"
    )

wlsxNFanTrayInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1037)
)
wlsxNFanTrayInserted.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNFanTrayInserted.setStatus(
        "current"
    )

wlsxNLCRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1038)
)
wlsxNLCRemoved.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCardSlot"))
)
if mibBuilder.loadTexts:
    wlsxNLCRemoved.setStatus(
        "current"
    )

wlsxNPowerSupplyMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1039)
)
wlsxNPowerSupplyMissing.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNPowerSupplyMissing.setStatus(
        "current"
    )

wlsxNAccessPointIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1040)
)
wlsxNAccessPointIsUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAccessPointIsUp.setStatus(
        "current"
    )

wlsxNAccessPointIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1041)
)
wlsxNAccessPointIsDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAccessPointIsDown.setStatus(
        "current"
    )

wlsxNCoverageHoleDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1042)
)
wlsxNCoverageHoleDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"))
)
if mibBuilder.loadTexts:
    wlsxNCoverageHoleDetected.setStatus(
        "current"
    )

wlsxNChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1043)
)
wlsxNChannelChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNChannelChanged.setStatus(
        "current"
    )

wlsxNStationAddedToBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1044)
)
wlsxNStationAddedToBlackList.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapStationBlackListReason"),
        ("WLSX-TRAP-MIB", "wlsxTrapStationBlackListReasonStr"))
)
if mibBuilder.loadTexts:
    wlsxNStationAddedToBlackList.setStatus(
        "current"
    )

wlsxNStationRemovedFromBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1045)
)
wlsxNStationRemovedFromBlackList.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"))
)
if mibBuilder.loadTexts:
    wlsxNStationRemovedFromBlackList.setStatus(
        "current"
    )

wlsxNIpSpoofingDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1046)
)
wlsxNIpSpoofingDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSpoofedIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapSpoofedOldPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapSpoofedNewPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxNIpSpoofingDetected.setStatus(
        "current"
    )

wlsxNDBCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1047)
)
wlsxNDBCommunicationFailure.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapDBName"),
        ("WLSX-TRAP-MIB", "wlsxTrapDBUserName"),
        ("WLSX-TRAP-MIB", "wlsxTrapDBIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapDBType"))
)
if mibBuilder.loadTexts:
    wlsxNDBCommunicationFailure.setStatus(
        "current"
    )

wlsxNVrrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1048)
)
wlsxNVrrpStateChange.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapVrrpID"),
        ("WLSX-TRAP-MIB", "wlsxTrapVrrpMasterIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapVrrpOperState"))
)
if mibBuilder.loadTexts:
    wlsxNVrrpStateChange.setStatus(
        "current"
    )

wlsxNRadioAttributesChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1049)
)
wlsxNRadioAttributesChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPTxPower"))
)
if mibBuilder.loadTexts:
    wlsxNRadioAttributesChanged.setStatus(
        "current"
    )

wlsxNESIServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1050)
)
wlsxNESIServerUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerGrpName"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerIpAddress"))
)
if mibBuilder.loadTexts:
    wlsxNESIServerUp.setStatus(
        "current"
    )

wlsxNESIServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1051)
)
wlsxNESIServerDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerGrpName"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerIpAddress"))
)
if mibBuilder.loadTexts:
    wlsxNESIServerDown.setStatus(
        "current"
    )

wlsxNLicenseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1052)
)
wlsxNLicenseExpiry.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapLicenseDaysRemaining"))
)
if mibBuilder.loadTexts:
    wlsxNLicenseExpiry.setStatus(
        "current"
    )

wlsxUnsecureAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1053)
)
wlsxUnsecureAPDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapMatchedMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapMatchedIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapRogueInfoURL"),
        ("WLSX-TRAP-MIB", "wlsxTrapMatchedIpv6"))
)
if mibBuilder.loadTexts:
    wlsxUnsecureAPDetected.setStatus(
        "current"
    )

wlsxUnsecureAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1054)
)
wlsxUnsecureAPResolved.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxUnsecureAPResolved.setStatus(
        "current"
    )

wlsxStaImpersonation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1055)
)
wlsxStaImpersonation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxStaImpersonation.setStatus(
        "current"
    )

wlsxReservedChannelViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1056)
)
wlsxReservedChannelViolation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxReservedChannelViolation.setStatus(
        "current"
    )

wlsxValidSSIDViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1057)
)
wlsxValidSSIDViolation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxValidSSIDViolation.setStatus(
        "current"
    )

wlsxChannelMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1058)
)
wlsxChannelMisconfiguration.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelMisconfiguration.setStatus(
        "current"
    )

wlsxOUIMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1059)
)
wlsxOUIMisconfiguration.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxOUIMisconfiguration.setStatus(
        "current"
    )

wlsxSSIDMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1060)
)
wlsxSSIDMisconfiguration.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxSSIDMisconfiguration.setStatus(
        "current"
    )

wlsxShortPreableMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1061)
)
wlsxShortPreableMisconfiguration.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxShortPreableMisconfiguration.setStatus(
        "current"
    )

wlsxWPAMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1062)
)
wlsxWPAMisconfiguration.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWPAMisconfiguration.setStatus(
        "current"
    )

wlsxAdhocNetworkDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1063)
)
wlsxAdhocNetworkDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkDetected.setStatus(
        "current"
    )

wlsxAdhocNetworkRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1064)
)
wlsxAdhocNetworkRemoved.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkRemoved.setStatus(
        "current"
    )

wlsxStaPolicyViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1065)
)
wlsxStaPolicyViolation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaPolicyViolation.setStatus(
        "current"
    )

wlsxRepeatWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1066)
)
wlsxRepeatWEPIVViolation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxRepeatWEPIVViolation.setStatus(
        "current"
    )

wlsxWeakWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1067)
)
wlsxWeakWEPIVViolation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWeakWEPIVViolation.setStatus(
        "current"
    )

wlsxChannelInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1068)
)
wlsxChannelInterferenceDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelInterferenceDetected.setStatus(
        "current"
    )

wlsxChannelInterferenceCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1069)
)
wlsxChannelInterferenceCleared.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelInterferenceCleared.setStatus(
        "current"
    )

wlsxAPInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1070)
)
wlsxAPInterferenceDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPInterferenceDetected.setStatus(
        "current"
    )

wlsxAPInterferenceCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1071)
)
wlsxAPInterferenceCleared.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPInterferenceCleared.setStatus(
        "current"
    )

wlsxStaInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1072)
)
wlsxStaInterferenceDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaInterferenceDetected.setStatus(
        "current"
    )

wlsxStaInterferenceCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1073)
)
wlsxStaInterferenceCleared.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaInterferenceCleared.setStatus(
        "current"
    )

wlsxFrameRetryRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1074)
)
wlsxFrameRetryRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameRetryRateExceeded.setStatus(
        "current"
    )

wlsxFrameReceiveErrorRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1075)
)
wlsxFrameReceiveErrorRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxFrameReceiveErrorRateExceeded.setStatus(
        "current"
    )

wlsxFrameFragmentationRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1076)
)
wlsxFrameFragmentationRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxFrameFragmentationRateExceeded.setStatus(
        "current"
    )

wlsxFrameBandWidthRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1077)
)
wlsxFrameBandWidthRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameBandWidthRateExceeded.setStatus(
        "current"
    )

wlsxFrameLowSpeedRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1078)
)
wlsxFrameLowSpeedRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameLowSpeedRateExceeded.setStatus(
        "current"
    )

wlsxFrameNonUnicastRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1079)
)
wlsxFrameNonUnicastRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameNonUnicastRateExceeded.setStatus(
        "current"
    )

wlsxLoadbalancingEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1080)
)
wlsxLoadbalancingEnabled.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxLoadbalancingEnabled.setStatus(
        "current"
    )

wlsxLoadbalancingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1081)
)
wlsxLoadbalancingDisabled.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxLoadbalancingDisabled.setStatus(
        "current"
    )

wlsxChannelFrameRetryRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1082)
)
wlsxChannelFrameRetryRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelFrameRetryRateExceeded.setStatus(
        "current"
    )

wlsxChannelFrameFragmentationRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1083)
)
wlsxChannelFrameFragmentationRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelFrameFragmentationRateExceeded.setStatus(
        "current"
    )

wlsxChannelFrameErrorRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1084)
)
wlsxChannelFrameErrorRateExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelFrameErrorRateExceeded.setStatus(
        "current"
    )

wlsxSignatureMatchAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1085)
)
wlsxSignatureMatchAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignatureMatchAP.setStatus(
        "current"
    )

wlsxSignatureMatchSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1086)
)
wlsxSignatureMatchSta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignatureMatchSta.setStatus(
        "current"
    )

wlsxChannelRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1087)
)
wlsxChannelRateAnomaly.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelRateAnomaly.setStatus(
        "current"
    )

wlsxNodeRateAnomalyAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1088)
)
wlsxNodeRateAnomalyAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxNodeRateAnomalyAP.setStatus(
        "current"
    )

wlsxNodeRateAnomalySta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1089)
)
wlsxNodeRateAnomalySta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxNodeRateAnomalySta.setStatus(
        "current"
    )

wlsxEAPRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1090)
)
wlsxEAPRateAnomaly.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxEAPRateAnomaly.setStatus(
        "current"
    )

wlsxSignalAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1091)
)
wlsxSignalAnomaly.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxSignalAnomaly.setStatus(
        "current"
    )

wlsxSequenceNumberAnomalyAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1092)
)
wlsxSequenceNumberAnomalyAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSequenceNumberAnomalyAP.setStatus(
        "current"
    )

wlsxSequenceNumberAnomalySta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1093)
)
wlsxSequenceNumberAnomalySta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSequenceNumberAnomalySta.setStatus(
        "current"
    )

wlsxDisconnectStationAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1094)
)
wlsxDisconnectStationAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxDisconnectStationAttack.setStatus(
        "current"
    )

wlsxApFloodAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1095)
)
wlsxApFloodAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxApFloodAttack.setStatus(
        "current"
    )

wlsxAdhocNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1096)
)
wlsxAdhocNetwork.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetwork.setStatus(
        "current"
    )

wlsxWirelessBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1097)
)
wlsxWirelessBridge.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxWirelessBridge.setStatus(
        "current"
    )

wlsxInvalidMacOUIAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1098)
)
wlsxInvalidMacOUIAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAddressType"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxInvalidMacOUIAP.setStatus(
        "current"
    )

wlsxInvalidMacOUISta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1099)
)
wlsxInvalidMacOUISta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAddressType"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxInvalidMacOUISta.setStatus(
        "current"
    )

wlsxWEPMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1100)
)
wlsxWEPMisconfiguration.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWEPMisconfiguration.setStatus(
        "current"
    )

wlsxStaRepeatWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1101)
)
wlsxStaRepeatWEPIVViolation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaRepeatWEPIVViolation.setStatus(
        "current"
    )

wlsxStaWeakWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1102)
)
wlsxStaWeakWEPIVViolation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaWeakWEPIVViolation.setStatus(
        "current"
    )

wlsxStaAssociatedToUnsecureAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1103)
)
wlsxStaAssociatedToUnsecureAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapRogueInfoURL"))
)
if mibBuilder.loadTexts:
    wlsxStaAssociatedToUnsecureAP.setStatus(
        "current"
    )

wlsxStaUnAssociatedFromUnsecureAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1104)
)
wlsxStaUnAssociatedFromUnsecureAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"))
)
if mibBuilder.loadTexts:
    wlsxStaUnAssociatedFromUnsecureAP.setStatus(
        "current"
    )

wlsxAdhocNetworkBridgeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1105)
)
wlsxAdhocNetworkBridgeDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkBridgeDetected.setStatus(
        "current"
    )

wlsxInterferingApDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1106)
)
wlsxInterferingApDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapInterferingAPInfoURL"))
)
if mibBuilder.loadTexts:
    wlsxInterferingApDetected.setStatus(
        "current"
    )

wlsxPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1107)
)
wlsxPortUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCardSlot"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAdminStatus"),
        ("WLSX-TRAP-MIB", "wlsxTrapOperStatus"))
)
if mibBuilder.loadTexts:
    wlsxPortUp.setStatus(
        "deprecated"
    )

wlsxPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1108)
)
wlsxPortDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCardSlot"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAdminStatus"),
        ("WLSX-TRAP-MIB", "wlsxTrapOperStatus"))
)
if mibBuilder.loadTexts:
    wlsxPortDown.setStatus(
        "deprecated"
    )

wlsxBSSIDIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1109)
)
wlsxBSSIDIsUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxBSSIDIsUp.setStatus(
        "current"
    )

wlsxBSSIDIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1110)
)
wlsxBSSIDIsDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxBSSIDIsDown.setStatus(
        "current"
    )

wlsxColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1111)
)
wlsxColdStart.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxColdStart.setStatus(
        "current"
    )

wlsxWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1112)
)
wlsxWarmStart.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxWarmStart.setStatus(
        "current"
    )

wlsxAPImpersonation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1113)
)
wlsxAPImpersonation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPImpersonation.setStatus(
        "current"
    )

wlsxInformQueueOverFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1114)
)
wlsxInformQueueOverFlow.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapHostIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapHostPort"))
)
if mibBuilder.loadTexts:
    wlsxInformQueueOverFlow.setStatus(
        "current"
    )

wlsxNAuthServerIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1115)
)
wlsxNAuthServerIsDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerIsDown.setStatus(
        "current"
    )

wlsxCTSTransferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1116)
)
wlsxCTSTransferError.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCTSTransferType"),
        ("WLSX-TRAP-MIB", "wlsxTrapCTSURL"))
)
if mibBuilder.loadTexts:
    wlsxCTSTransferError.setStatus(
        "current"
    )

wlsxCTSTransferSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1117)
)
wlsxCTSTransferSucceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCTSTransferType"),
        ("WLSX-TRAP-MIB", "wlsxTrapCTSURL"))
)
if mibBuilder.loadTexts:
    wlsxCTSTransferSucceeded.setStatus(
        "current"
    )

wlsxConfigurationUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1118)
)
wlsxConfigurationUpdateError.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapConfigurationId"),
        ("WLSX-TRAP-MIB", "wlsxTrapUpdateFailureReason"),
        ("WLSX-TRAP-MIB", "wlsxTrapUpdateFailedObj"))
)
if mibBuilder.loadTexts:
    wlsxConfigurationUpdateError.setStatus(
        "current"
    )

wlsxConfigurationUpdateSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1119)
)
wlsxConfigurationUpdateSucceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapConfigurationId"))
)
if mibBuilder.loadTexts:
    wlsxConfigurationUpdateSucceeded.setStatus(
        "current"
    )

wlsxGlobalConfigurationChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1120)
)
wlsxGlobalConfigurationChangeNotification.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapConfigurationId"),
        ("WLSX-TRAP-MIB", "wlsxTrapGlobalConfigObj"))
)
if mibBuilder.loadTexts:
    wlsxGlobalConfigurationChangeNotification.setStatus(
        "current"
    )

wlsxUserEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1121)
)
wlsxUserEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxUserEntryChanged.setStatus(
        "current"
    )

wlsxAPBssidEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1122)
)
wlsxAPBssidEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxAPBssidEntryChanged.setStatus(
        "current"
    )

wlsxAPRadioEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1123)
)
wlsxAPRadioEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxAPRadioEntryChanged.setStatus(
        "current"
    )

wlsxAPEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1124)
)
wlsxAPEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxAPEntryChanged.setStatus(
        "current"
    )

wlsxSwitchListEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1125)
)
wlsxSwitchListEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapSwitchIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxSwitchListEntryChanged.setStatus(
        "current"
    )

wlsxPortEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1126)
)
wlsxPortEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapCardSlot"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxPortEntryChanged.setStatus(
        "current"
    )

wlsxVlanEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1127)
)
wlsxVlanEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapVlanId"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxVlanEntryChanged.setStatus(
        "current"
    )

wlsxVlanInterfaceEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1128)
)
wlsxVlanInterfaceEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapVlanId"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxVlanInterfaceEntryChanged.setStatus(
        "current"
    )

wlsxWindowsBridgeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1129)
)
wlsxWindowsBridgeDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWindowsBridgeDetected.setStatus(
        "current"
    )

wlsxLicenseEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1130)
)
wlsxLicenseEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapLicenseId"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxLicenseEntryChanged.setStatus(
        "current"
    )

wlsxEsiServerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1131)
)
wlsxEsiServerChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxEsiServerChanged.setStatus(
        "current"
    )

wlsxMonAPEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1132)
)
wlsxMonAPEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxMonAPEntryChanged.setStatus(
        "current"
    )

wlsxMonStationEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1133)
)
wlsxMonStationEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxMonStationEntryChanged.setStatus(
        "current"
    )

wlsxSignAPNetstumbler = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1134)
)
wlsxSignAPNetstumbler.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPNetstumbler.setStatus(
        "current"
    )

wlsxSignStaNetstumbler = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1135)
)
wlsxSignStaNetstumbler.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaNetstumbler.setStatus(
        "current"
    )

wlsxSignAPAsleap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1136)
)
wlsxSignAPAsleap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPAsleap.setStatus(
        "current"
    )

wlsxSignStaAsleap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1137)
)
wlsxSignStaAsleap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaAsleap.setStatus(
        "current"
    )

wlsxSignAPAirjack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1138)
)
wlsxSignAPAirjack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPAirjack.setStatus(
        "current"
    )

wlsxSignStaAirjack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1139)
)
wlsxSignStaAirjack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaAirjack.setStatus(
        "current"
    )

wlsxSignAPNullProbeResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1140)
)
wlsxSignAPNullProbeResp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPNullProbeResp.setStatus(
        "current"
    )

wlsxSignStaNullProbeResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1141)
)
wlsxSignStaNullProbeResp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaNullProbeResp.setStatus(
        "current"
    )

wlsxSignAPDeauthBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1142)
)
wlsxSignAPDeauthBcast.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPDeauthBcast.setStatus(
        "current"
    )

wlsxSignStaDeauthBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1143)
)
wlsxSignStaDeauthBcast.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaDeauthBcast.setStatus(
        "current"
    )

wlsxWindowsBridgeDetectedAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1144)
)
wlsxWindowsBridgeDetectedAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWindowsBridgeDetectedAP.setStatus(
        "current"
    )

wlsxWindowsBridgeDetectedSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1145)
)
wlsxWindowsBridgeDetectedSta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWindowsBridgeDetectedSta.setStatus(
        "current"
    )

wlsxAdhocNetworkBridgeDetectedAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1146)
)
wlsxAdhocNetworkBridgeDetectedAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkBridgeDetectedAP.setStatus(
        "current"
    )

wlsxAdhocNetworkBridgeDetectedSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1147)
)
wlsxAdhocNetworkBridgeDetectedSta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkBridgeDetectedSta.setStatus(
        "current"
    )

wlsxDisconnectStationAttackAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1148)
)
wlsxDisconnectStationAttackAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxDisconnectStationAttackAP.setStatus(
        "current"
    )

wlsxDisconnectStationAttackSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1149)
)
wlsxDisconnectStationAttackSta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxDisconnectStationAttackSta.setStatus(
        "current"
    )

wlsxSuspectUnsecureAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1150)
)
wlsxSuspectUnsecureAPDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapMatchedMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapMatchedIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapConfidenceLevel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapRogueInfoURL"),
        ("WLSX-TRAP-MIB", "wlsxTrapMatchedIpv6"))
)
if mibBuilder.loadTexts:
    wlsxSuspectUnsecureAPDetected.setStatus(
        "current"
    )

wlsxSuspectUnsecureAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1151)
)
wlsxSuspectUnsecureAPResolved.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"))
)
if mibBuilder.loadTexts:
    wlsxSuspectUnsecureAPResolved.setStatus(
        "current"
    )

wlsxConfigurationLicenseMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1152)
)
wlsxConfigurationLicenseMismatch.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapConfigurationId"),
        ("WLSX-TRAP-MIB", "wlsxTrapMissingLicenses"))
)
if mibBuilder.loadTexts:
    wlsxConfigurationLicenseMismatch.setStatus(
        "current"
    )

wlsxVoiceCdrBufferThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1153)
)
wlsxVoiceCdrBufferThresholdReached.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxVoiceCurrentNumCdr"))
)
if mibBuilder.loadTexts:
    wlsxVoiceCdrBufferThresholdReached.setStatus(
        "current"
    )

wlsxTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1154)
)
wlsxTunnelUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTunnelId"),
        ("WLSX-TRAP-MIB", "wlsxTrapTunnelUpReason"),
        ("WLSX-TRAP-MIB", "wlsxTrapTunnelStatus"))
)
if mibBuilder.loadTexts:
    wlsxTunnelUp.setStatus(
        "current"
    )

wlsxTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1155)
)
wlsxTunnelDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTunnelId"),
        ("WLSX-TRAP-MIB", "wlsxTrapTunnelDownReason"),
        ("WLSX-TRAP-MIB", "wlsxTrapTunnelStatus"))
)
if mibBuilder.loadTexts:
    wlsxTunnelDown.setStatus(
        "current"
    )

wlsxMeshNodeEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1156)
)
wlsxMeshNodeEntryChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableGenNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapTableEntryChangeType"))
)
if mibBuilder.loadTexts:
    wlsxMeshNodeEntryChanged.setStatus(
        "current"
    )

wlsxHtGreenfieldSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1157)
)
wlsxHtGreenfieldSupported.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxHtGreenfieldSupported.setStatus(
        "current"
    )

wlsxHT40MHzIntoleranceAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1158)
)
wlsxHT40MHzIntoleranceAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxHT40MHzIntoleranceAP.setStatus(
        "current"
    )

wlsxHT40MHzIntoleranceSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1159)
)
wlsxHT40MHzIntoleranceSta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxHT40MHzIntoleranceSta.setStatus(
        "current"
    )

wlsxNAuthServerAllInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1160)
)
wlsxNAuthServerAllInService.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapESIServerGrpName"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerAllInService.setStatus(
        "current"
    )

wlsxNAdhocNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1161)
)
wlsxNAdhocNetwork.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocNetwork.setStatus(
        "current"
    )

wlsxNAdhocNetworkBridgeDetectedAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1162)
)
wlsxNAdhocNetworkBridgeDetectedAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocNetworkBridgeDetectedAP.setStatus(
        "current"
    )

wlsxNAdhocNetworkBridgeDetectedSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1163)
)
wlsxNAdhocNetworkBridgeDetectedSta.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocNetworkBridgeDetectedSta.setStatus(
        "current"
    )

wlsxNAuthMaxXsecUserEntries = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1164)
)
wlsxNAuthMaxXsecUserEntries.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNAuthMaxXsecUserEntries.setStatus(
        "current"
    )

wlsxNVpnMaxSessions = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1165)
)
wlsxNVpnMaxSessions.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNVpnMaxSessions.setStatus(
        "current"
    )

wlsxNRapExpiredPSK = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1166)
)
wlsxNRapExpiredPSK.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapApSerialNumber"))
)
if mibBuilder.loadTexts:
    wlsxNRapExpiredPSK.setStatus(
        "current"
    )

wlsxNRapWarnExpiredPSK = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1167)
)
wlsxNRapWarnExpiredPSK.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTimeStr"))
)
if mibBuilder.loadTexts:
    wlsxNRapWarnExpiredPSK.setStatus(
        "current"
    )

wlsxNConnectionResetWithLocal = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1168)
)
wlsxNConnectionResetWithLocal.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapMasterName"),
        ("WLSX-TRAP-MIB", "wlsxTrapMasterIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapLocalName"),
        ("WLSX-TRAP-MIB", "wlsxTrapLocalIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapTimeStr"))
)
if mibBuilder.loadTexts:
    wlsxNConnectionResetWithLocal.setStatus(
        "current"
    )

wlsxNApOnBackupController = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1169)
)
wlsxNApOnBackupController.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapBackupControllerIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapPrimaryControllerIp"))
)
if mibBuilder.loadTexts:
    wlsxNApOnBackupController.setStatus(
        "current"
    )

wlsxClientFloodAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1170)
)
wlsxClientFloodAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxClientFloodAttack.setStatus(
        "current"
    )

wlsxValidClientNotUsingEncryption = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1171)
)
wlsxValidClientNotUsingEncryption.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxValidClientNotUsingEncryption.setStatus(
        "current"
    )

wlsxAdhocUsingValidSSID = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1172)
)
wlsxAdhocUsingValidSSID.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocUsingValidSSID.setStatus(
        "current"
    )

wlsxAPSpoofingDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1173)
)
wlsxAPSpoofingDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSpoofedFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPSpoofingDetected.setStatus(
        "current"
    )

wlsxClientAssociatingOnWrongChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1174)
)
wlsxClientAssociatingOnWrongChannel.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSpoofedFrameType"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxClientAssociatingOnWrongChannel.setStatus(
        "current"
    )

wlsxNDisconnectStationAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1175)
)
wlsxNDisconnectStationAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNDisconnectStationAttack.setStatus(
        "current"
    )

wlsxNStaUnAssociatedFromUnsecureAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1176)
)
wlsxNStaUnAssociatedFromUnsecureAP.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNStaUnAssociatedFromUnsecureAP.setStatus(
        "current"
    )

wlsxOmertaAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1177)
)
wlsxOmertaAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxOmertaAttack.setStatus(
        "current"
    )

wlsxTKIPReplayAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1178)
)
wlsxTKIPReplayAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxTKIPReplayAttack.setStatus(
        "current"
    )

wlsxChopChopAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1179)
)
wlsxChopChopAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxChopChopAttack.setStatus(
        "current"
    )

wlsxFataJackAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1180)
)
wlsxFataJackAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFataJackAttack.setStatus(
        "current"
    )

wlsxInvalidAddressCombination = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1181)
)
wlsxInvalidAddressCombination.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxInvalidAddressCombination.setStatus(
        "current"
    )

wlsxValidClientMisassociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1182)
)
wlsxValidClientMisassociation.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAssociationType"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxValidClientMisassociation.setStatus(
        "current"
    )

wlsxMalformedHTIEDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1183)
)
wlsxMalformedHTIEDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedHTIEDetected.setStatus(
        "current"
    )

wlsxMalformedAssocReqDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1184)
)
wlsxMalformedAssocReqDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedAssocReqDetected.setStatus(
        "current"
    )

wlsxOverflowIEDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1185)
)
wlsxOverflowIEDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxOverflowIEDetected.setStatus(
        "current"
    )

wlsxOverflowEAPOLKeyDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1186)
)
wlsxOverflowEAPOLKeyDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxOverflowEAPOLKeyDetected.setStatus(
        "current"
    )

wlsxMalformedFrameLargeDurationDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1187)
)
wlsxMalformedFrameLargeDurationDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedFrameLargeDurationDetected.setStatus(
        "current"
    )

wlsxMalformedFrameWrongChannelDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1188)
)
wlsxMalformedFrameWrongChannelDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedFrameWrongChannelDetected.setStatus(
        "current"
    )

wlsxMalformedAuthFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1189)
)
wlsxMalformedAuthFrame.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxMalformedAuthFrame.setStatus(
        "current"
    )

wlsxCTSRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1190)
)
wlsxCTSRateAnomaly.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxCTSRateAnomaly.setStatus(
        "current"
    )

wlsxRTSRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1191)
)
wlsxRTSRateAnomaly.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxRTSRateAnomaly.setStatus(
        "current"
    )

wlsxNRogueAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1192)
)
wlsxNRogueAPDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNRogueAPDetected.setStatus(
        "current"
    )

wlsxNRogueAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1193)
)
wlsxNRogueAPResolved.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNRogueAPResolved.setStatus(
        "current"
    )

wlsxNeighborAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1194)
)
wlsxNeighborAPDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNeighborAPDetected.setStatus(
        "current"
    )

wlsxNInterferingAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1195)
)
wlsxNInterferingAPDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNInterferingAPDetected.setStatus(
        "current"
    )

wlsxNSuspectRogueAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1196)
)
wlsxNSuspectRogueAPDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapConfidenceLevel"))
)
if mibBuilder.loadTexts:
    wlsxNSuspectRogueAPDetected.setStatus(
        "current"
    )

wlsxNSuspectRogueAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1197)
)
wlsxNSuspectRogueAPResolved.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSuspectRogueAPResolved.setStatus(
        "current"
    )

wlsxBlockAckAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1198)
)
wlsxBlockAckAttackDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxBlockAckAttackDetected.setStatus(
        "current"
    )

wlsxHotspotterAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1199)
)
wlsxHotspotterAttackDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"))
)
if mibBuilder.loadTexts:
    wlsxHotspotterAttackDetected.setStatus(
        "current"
    )

wlsxNSignatureMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1200)
)
wlsxNSignatureMatch.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatch.setStatus(
        "current"
    )

wlsxNSignatureMatchNetstumbler = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1201)
)
wlsxNSignatureMatchNetstumbler.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchNetstumbler.setStatus(
        "current"
    )

wlsxNSignatureMatchAsleap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1202)
)
wlsxNSignatureMatchAsleap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchAsleap.setStatus(
        "current"
    )

wlsxNSignatureMatchAirjack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1203)
)
wlsxNSignatureMatchAirjack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchAirjack.setStatus(
        "current"
    )

wlsxNSignatureMatchNullProbeResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1204)
)
wlsxNSignatureMatchNullProbeResp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchNullProbeResp.setStatus(
        "current"
    )

wlsxNSignatureMatchDeauthBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1205)
)
wlsxNSignatureMatchDeauthBcast.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchDeauthBcast.setStatus(
        "current"
    )

wlsxNSignatureMatchDisassocBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1206)
)
wlsxNSignatureMatchDisassocBcast.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchDisassocBcast.setStatus(
        "current"
    )

wlsxNSignatureMatchWellenreiter = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1207)
)
wlsxNSignatureMatchWellenreiter.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTransmitterMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapReceiverMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSignatureName"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchWellenreiter.setStatus(
        "current"
    )

wlsxAPDeauthContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1208)
)
wlsxAPDeauthContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPDeauthContainment.setStatus(
        "current"
    )

wlsxClientDeauthContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1209)
)
wlsxClientDeauthContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxClientDeauthContainment.setStatus(
        "current"
    )

wlsxAPWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1210)
)
wlsxAPWiredContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpv6Address"))
)
if mibBuilder.loadTexts:
    wlsxAPWiredContainment.setStatus(
        "current"
    )

wlsxClientWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1211)
)
wlsxClientWiredContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpv6Address"))
)
if mibBuilder.loadTexts:
    wlsxClientWiredContainment.setStatus(
        "current"
    )

wlsxAPTaggedWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1212)
)
wlsxAPTaggedWiredContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapVlanId"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpv6Address"))
)
if mibBuilder.loadTexts:
    wlsxAPTaggedWiredContainment.setStatus(
        "current"
    )

wlsxClientTaggedWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1213)
)
wlsxClientTaggedWiredContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapVlanId"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapDeviceIpv6Address"))
)
if mibBuilder.loadTexts:
    wlsxClientTaggedWiredContainment.setStatus(
        "current"
    )

wlsxTarpitContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1214)
)
wlsxTarpitContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxTarpitContainment.setStatus(
        "current"
    )

wlsxVoiceClientLocationUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1215)
)
wlsxVoiceClientLocationUpdate.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapVcIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapVcMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapSwitchIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapApMode"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxVoiceClientLocationUpdate.setStatus(
        "current"
    )

wlsxAPChannelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1216)
)
wlsxAPChannelChange.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannelSec"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPPrevChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPPrevChannelSec"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPARMChangeReason"))
)
if mibBuilder.loadTexts:
    wlsxAPChannelChange.setStatus(
        "current"
    )

wlsxAPPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1217)
)
wlsxAPPowerChange.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPTxPower"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPPrevTxPower"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPPowerChange.setStatus(
        "current"
    )

wlsxAPModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1218)
)
wlsxAPModeChange.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPCurMode"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPPrevMode"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPModeChange.setStatus(
        "current"
    )

wlsxUserEntryAttributesChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1219)
)
wlsxUserEntryAttributesChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapCardSlot"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserAttributeChangeType"),
        ("WLSX-TRAP-MIB", "wlsxTrapHTMode"),
        ("WLSX-TRAP-MIB", "wlsxTrapPhyType"))
)
if mibBuilder.loadTexts:
    wlsxUserEntryAttributesChanged.setStatus(
        "current"
    )

wlsxPowerSaveDosAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1220)
)
wlsxPowerSaveDosAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxPowerSaveDosAttack.setStatus(
        "current"
    )

wlsxNAPMasterStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1221)
)
wlsxNAPMasterStatusChange.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapApControllerIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapApMasterStatus"))
)
if mibBuilder.loadTexts:
    wlsxNAPMasterStatusChange.setStatus(
        "current"
    )

wlsxNAdhocUsingValidSSID = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1222)
)
wlsxNAdhocUsingValidSSID.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocUsingValidSSID.setStatus(
        "current"
    )

wlsxCRLExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1223)
)
wlsxCRLExpired.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCaName"),
        ("WLSX-TRAP-MIB", "wlsxTrapCrlName"))
)
if mibBuilder.loadTexts:
    wlsxCRLExpired.setStatus(
        "current"
    )

wlsxMgmtUserAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1224)
)
wlsxMgmtUserAuthenticationFailed.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserName"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerAddress"))
)
if mibBuilder.loadTexts:
    wlsxMgmtUserAuthenticationFailed.setStatus(
        "current"
    )

wlsxNConnectionBackfromLocal = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1225)
)
wlsxNConnectionBackfromLocal.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapMasterName"),
        ("WLSX-TRAP-MIB", "wlsxTrapMasterIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapLocalName"),
        ("WLSX-TRAP-MIB", "wlsxTrapLocalIp"),
        ("WLSX-TRAP-MIB", "wlsxTrapTimeStr"))
)
if mibBuilder.loadTexts:
    wlsxNConnectionBackfromLocal.setStatus(
        "current"
    )

wlsxAPNumUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1226)
)
wlsxAPNumUpgradeFailure.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxAPNumUpgradeFailure.setStatus(
        "current"
    )

wlsxAPNumWarmStarts = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1227)
)
wlsxAPNumWarmStarts.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxAPNumWarmStarts.setStatus(
        "current"
    )

wlsxAPNumColdStarts = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1228)
)
wlsxAPNumColdStarts.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxAPNumColdStarts.setStatus(
        "current"
    )

wlsxAPNumDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1229)
)
wlsxAPNumDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxAPNumDown.setStatus(
        "current"
    )

wlsxAPNumRadioDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1230)
)
wlsxAPNumRadioDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxAPNumRadioDown.setStatus(
        "current"
    )

wlsxNumClockSyncErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1231)
)
wlsxNumClockSyncErrors.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxNumClockSyncErrors.setStatus(
        "current"
    )

wlsxNumColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1232)
)
wlsxNumColdStart.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxNumColdStart.setStatus(
        "current"
    )

wlsxNumWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1233)
)
wlsxNumWarmStart.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxNumWarmStart.setStatus(
        "current"
    )

wlsxWirelessHostedNetworkDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1234)
)
wlsxWirelessHostedNetworkDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapClientClassification"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWirelessHostedNetworkDetected.setStatus(
        "current"
    )

wlsxClientAssociatedToHostedNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1235)
)
wlsxClientAssociatedToHostedNetwork.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxClientAssociatedToHostedNetwork.setStatus(
        "current"
    )

wlsxThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1236)
)
wlsxThresholdExceeded.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxThresholdResourceType"),
        ("WLSX-TRAP-MIB", "wlsxThresholdResourceName"),
        ("WLSX-TRAP-MIB", "wlsxThresholdValue"),
        ("WLSX-TRAP-MIB", "wlsxResourceValue"))
)
if mibBuilder.loadTexts:
    wlsxThresholdExceeded.setStatus(
        "current"
    )

wlsxThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1237)
)
wlsxThresholdCleared.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxThresholdResourceType"),
        ("WLSX-TRAP-MIB", "wlsxThresholdResourceName"),
        ("WLSX-TRAP-MIB", "wlsxThresholdValue"),
        ("WLSX-TRAP-MIB", "wlsxResourceValue"))
)
if mibBuilder.loadTexts:
    wlsxThresholdCleared.setStatus(
        "current"
    )

wlsxWirelessHostedNetworkContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1238)
)
wlsxWirelessHostedNetworkContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWirelessHostedNetworkContainment.setStatus(
        "current"
    )

wlsxHostOfWirelessNetworkContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1239)
)
wlsxHostOfWirelessNetworkContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxHostOfWirelessNetworkContainment.setStatus(
        "current"
    )

wlsxEnhancedAdhocContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1240)
)
wlsxEnhancedAdhocContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxEnhancedAdhocContainment.setStatus(
        "current"
    )

wlsxPowerSupplyOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1241)
)
wlsxPowerSupplyOKTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapPowerSupplyNumber"))
)
if mibBuilder.loadTexts:
    wlsxPowerSupplyOKTrap.setStatus(
        "current"
    )

wlsxPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1242)
)
wlsxPowerSupplyFailureTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapPowerSupplyNumber"))
)
if mibBuilder.loadTexts:
    wlsxPowerSupplyFailureTrap.setStatus(
        "current"
    )

wlsxFanTrayRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1243)
)
wlsxFanTrayRemovedTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFanTrayNumber"))
)
if mibBuilder.loadTexts:
    wlsxFanTrayRemovedTrap.setStatus(
        "current"
    )

wlsxFanTrayInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1244)
)
wlsxFanTrayInsertedTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFanTrayNumber"))
)
if mibBuilder.loadTexts:
    wlsxFanTrayInsertedTrap.setStatus(
        "current"
    )

wlsxPowerSupplyMissingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1245)
)
wlsxPowerSupplyMissingTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapPowerSupplyNumber"))
)
if mibBuilder.loadTexts:
    wlsxPowerSupplyMissingTrap.setStatus(
        "current"
    )

wlsxStackTopologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1246)
)
wlsxStackTopologyChangeTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxStackMemberMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxStackPrevSlot"),
        ("WLSX-TRAP-MIB", "wlsxStackCurrentSlot"),
        ("WLSX-TRAP-MIB", "wlsxStackPrevState"),
        ("WLSX-TRAP-MIB", "wlsxStackCurrentState"),
        ("WLSX-TRAP-MIB", "wlsxStackChangeEvent"))
)
if mibBuilder.loadTexts:
    wlsxStackTopologyChangeTrap.setStatus(
        "current"
    )

wlsxStackIfStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1247)
)
wlsxStackIfStateChangeTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxStackMemberMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxStackMemberSlotNumber"),
        ("WLSX-TRAP-MIB", "wlsxStackIfName"),
        ("WLSX-TRAP-MIB", "wlsxStackProtoIfTopoJoined"))
)
if mibBuilder.loadTexts:
    wlsxStackIfStateChangeTrap.setStatus(
        "current"
    )

wlsxLicenseServerExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1248)
)
wlsxLicenseServerExpiry.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapLicenseServerDaysRemaining"))
)
if mibBuilder.loadTexts:
    wlsxLicenseServerExpiry.setStatus(
        "current"
    )

wlsxLicenseClientExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1249)
)
wlsxLicenseClientExpiry.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapLicenseClientDaysRemaining"))
)
if mibBuilder.loadTexts:
    wlsxLicenseClientExpiry.setStatus(
        "current"
    )

wlsxIfStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1250)
)
wlsxIfStateChangeTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxIfIndex"),
        ("WLSX-TRAP-MIB", "wlsxIfState"),
        ("WLSX-TRAP-MIB", "wlsxIfStateChangeReason"))
)
if mibBuilder.loadTexts:
    wlsxIfStateChangeTrap.setStatus(
        "current"
    )

wlsxWMSOffloadRecommended = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1251)
)
wlsxWMSOffloadRecommended.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxWMSOffloadRecommended.setStatus(
        "current"
    )

wlsxAPActiveUplinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1252)
)
wlsxAPActiveUplinkChanged.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPPreviousUplinkType"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPPreviousUplinkActiveTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPActiveUplinkType"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPUplinkChangeReason"))
)
if mibBuilder.loadTexts:
    wlsxAPActiveUplinkChanged.setStatus(
        "current"
    )

wlsxCertExpiringSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1253)
)
wlsxCertExpiringSoon.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapExpiringCertName"))
)
if mibBuilder.loadTexts:
    wlsxCertExpiringSoon.setStatus(
        "current"
    )

wlsxCertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1254)
)
wlsxCertExpired.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapExpiredCertName"))
)
if mibBuilder.loadTexts:
    wlsxCertExpired.setStatus(
        "current"
    )

wlsxAPManagedModeConfigFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1255)
)
wlsxAPManagedModeConfigFailureTrap.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPManagedModeConfigFailure"))
)
if mibBuilder.loadTexts:
    wlsxAPManagedModeConfigFailureTrap.setStatus(
        "current"
    )

wlsxNAuthServerAcctTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1256)
)
wlsxNAuthServerAcctTimedOut.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserName"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerAcctTimedOut.setStatus(
        "current"
    )

wlsxAPUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1257)
)
wlsxAPUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"))
)
if mibBuilder.loadTexts:
    wlsxAPUp.setStatus(
        "current"
    )

wlsxAPDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1258)
)
wlsxAPDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"))
)
if mibBuilder.loadTexts:
    wlsxAPDown.setStatus(
        "current"
    )

wlsxPortalServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1259)
)
wlsxPortalServerDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortalServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortalServerAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortalServerDownReason"))
)
if mibBuilder.loadTexts:
    wlsxPortalServerDown.setStatus(
        "current"
    )

wlsxPortalServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1260)
)
wlsxPortalServerUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortalServerName"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortalServerAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxPortalServerUp.setStatus(
        "current"
    )

wlsxNAdhocUsingValidSSIDContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1261)
)
wlsxNAdhocUsingValidSSIDContainment.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocUsingValidSSIDContainment.setStatus(
        "current"
    )

wlsxLicensePlatformMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1262)
)
wlsxLicensePlatformMismatch.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapLicensePlatformMismatchKey"))
)
if mibBuilder.loadTexts:
    wlsxLicensePlatformMismatch.setStatus(
        "current"
    )

wlsxIAPVoiceClientLocationUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1263)
)
wlsxIAPVoiceClientLocationUpdate.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapVcIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapVcMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxIAPVoiceClientLocationUpdate.setStatus(
        "current"
    )

wlsxNAceUsageThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1264)
)
wlsxNAceUsageThreshold.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNAceUsageThreshold.setStatus(
        "current"
    )

wlsxNWebCCLicenseEnforcement = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1265)
)
wlsxNWebCCLicenseEnforcement.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNWebCCLicenseEnforcement.setStatus(
        "current"
    )

wlsxNFanAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1266)
)
wlsxNFanAbsent.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapFanNumber"))
)
if mibBuilder.loadTexts:
    wlsxNFanAbsent.setStatus(
        "current"
    )

wlsxWPAFTAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1267)
)
wlsxWPAFTAttack.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapNodeMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"))
)
if mibBuilder.loadTexts:
    wlsxWPAFTAttack.setStatus(
        "current"
    )

wlsxMitMDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1268)
)
wlsxMitMDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMitMDetected.setStatus(
        "current"
    )

wlsxAPPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1269)
)
wlsxAPPortUp.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapOperStatus"))
)
if mibBuilder.loadTexts:
    wlsxAPPortUp.setStatus(
        "current"
    )

wlsxAPPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1270)
)
wlsxAPPortDown.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapOperStatus"))
)
if mibBuilder.loadTexts:
    wlsxAPPortDown.setStatus(
        "current"
    )

wlsxAPLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1271)
)
wlsxAPLoopDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"))
)
if mibBuilder.loadTexts:
    wlsxAPLoopDetected.setStatus(
        "current"
    )

wlsxAPBROADCASTSTORM = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1272)
)
wlsxAPBROADCASTSTORM.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapPortNumber"))
)
if mibBuilder.loadTexts:
    wlsxAPBROADCASTSTORM.setStatus(
        "current"
    )

wlsxAPIPConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1273)
)
wlsxAPIPConflict.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapSourceMac"),
        ("WLSX-TRAP-MIB", "wlsxTrapCount"))
)
if mibBuilder.loadTexts:
    wlsxAPIPConflict.setStatus(
        "current"
    )

wlsxCLEARPASSSERVERINVALID = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1274)
)
wlsxCLEARPASSSERVERINVALID.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthServerName"))
)
if mibBuilder.loadTexts:
    wlsxCLEARPASSSERVERINVALID.setStatus(
        "current"
    )

wlsxNLowOnFlash1Space = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1275)
)
wlsxNLowOnFlash1Space.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNLowOnFlash1Space.setStatus(
        "current"
    )

wlsxFlash1SpaceOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1276)
)
wlsxFlash1SpaceOK.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxFlash1SpaceOK.setStatus(
        "current"
    )

wlsxTHERMALSHUTDOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1277)
)
wlsxTHERMALSHUTDOWN.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPIpAddress"))
)
if mibBuilder.loadTexts:
    wlsxTHERMALSHUTDOWN.setStatus(
        "current"
    )

wlsxPhonyBSSIDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1278)
)
wlsxPhonyBSSIDDetected.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPLocation"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPRadioNumber"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPChannel"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapTargetAPMac"))
)
if mibBuilder.loadTexts:
    wlsxPhonyBSSIDDetected.setStatus(
        "current"
    )

wlsxAPUSBPLUGALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1279)
)
wlsxAPUSBPLUGALARM.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapUSBVendorProductID"),
        ("WLSX-TRAP-MIB", "wlsxTrapUSBVendorProductID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPUSBStatus"))
)
if mibBuilder.loadTexts:
    wlsxAPUSBPLUGALARM.setStatus(
        "current"
    )

wlsxNSwitchIPv6Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1280)
)
wlsxNSwitchIPv6Changed.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapSwitchIpv6"))
)
if mibBuilder.loadTexts:
    wlsxNSwitchIPv6Changed.setStatus(
        "current"
    )

wlsxNDot1xThresholdLimitHit = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1281)
)
wlsxNDot1xThresholdLimitHit.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNDot1xThresholdLimitHit.setStatus(
        "current"
    )

wlsxNDot1xTotalLimitHit = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1282)
)
wlsxNDot1xTotalLimitHit.setObjects(
    ("WLSX-TRAP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxNDot1xTotalLimitHit.setStatus(
        "current"
    )

wlsxClusterVlanProbeStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1283)
)
wlsxClusterVlanProbeStatus.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapPeerIpAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapConnectionStatus"),
        ("WLSX-TRAP-MIB", "wlsxTrapFailedVlan"))
)
if mibBuilder.loadTexts:
    wlsxClusterVlanProbeStatus.setStatus(
        "current"
    )

wlsxClientRejectedByMaxClientCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1284)
)
wlsxClientRejectedByMaxClientCount.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapEssid"))
)
if mibBuilder.loadTexts:
    wlsxClientRejectedByMaxClientCount.setStatus(
        "current"
    )

wlsxClientPskAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 1, 11, 1, 2, 1285)
)
wlsxClientPskAuthenticationFailed.setObjects(
      *(("WLSX-TRAP-MIB", "wlsxTrapTime"),
        ("WLSX-TRAP-MIB", "wlsxTrapUserPhyAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAuthFailureReason"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPBSSID"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPMacAddress"),
        ("WLSX-TRAP-MIB", "wlsxTrapAPName"),
        ("WLSX-TRAP-MIB", "wlsxTrapEssid"))
)
if mibBuilder.loadTexts:
    wlsxClientPskAuthenticationFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-TRAP-MIB",
    **{"wlsrTrapMIB": wlsrTrapMIB,
       "wlsxTrapsGroup": wlsxTrapsGroup,
       "wlsxTrapObjectsGroup": wlsxTrapObjectsGroup,
       "wlsxTrapAPMacAddress": wlsxTrapAPMacAddress,
       "wlsxTrapAPIpAddress": wlsxTrapAPIpAddress,
       "wlsxTrapAPBSSID": wlsxTrapAPBSSID,
       "wlsxTrapEssid": wlsxTrapEssid,
       "wlsxTrapTargetAPBSSID": wlsxTrapTargetAPBSSID,
       "wlsxTrapTargetAPSSID": wlsxTrapTargetAPSSID,
       "wlsxTrapTargetAPChannel": wlsxTrapTargetAPChannel,
       "wlsxTrapNodeMac": wlsxTrapNodeMac,
       "wlsxTrapSourceMac": wlsxTrapSourceMac,
       "wlsxReceiverMac": wlsxReceiverMac,
       "wlsxTrapTransmitterMac": wlsxTrapTransmitterMac,
       "wlsxTrapReceiverMac": wlsxTrapReceiverMac,
       "wlsxTrapSnr": wlsxTrapSnr,
       "wlsxTrapSignatureName": wlsxTrapSignatureName,
       "wlsxTrapFrameType": wlsxTrapFrameType,
       "wlsxTrapAddressType": wlsxTrapAddressType,
       "wlsxTrapAPLocation": wlsxTrapAPLocation,
       "wlsxTrapAPChannel": wlsxTrapAPChannel,
       "wlsxTrapAPTxPower": wlsxTrapAPTxPower,
       "wlsxTrapMatchedMac": wlsxTrapMatchedMac,
       "wlsxTrapMatchedIp": wlsxTrapMatchedIp,
       "wlsxTrapRogueIfoURL": wlsxTrapRogueIfoURL,
       "wlsxTrapVlanId": wlsxTrapVlanId,
       "wlsxTrapAdminStatus": wlsxTrapAdminStatus,
       "wlsxTrapOperStatus": wlsxTrapOperStatus,
       "wlsxTrapAuthServerName": wlsxTrapAuthServerName,
       "wlsxTrapAuthServerTimeout": wlsxTrapAuthServerTimeout,
       "wlsxTrapCardSlot": wlsxTrapCardSlot,
       "wlsxTrapTemperatureValue": wlsxTrapTemperatureValue,
       "wlsxTrapProcessName": wlsxTrapProcessName,
       "wlsxTrapFanNumber": wlsxTrapFanNumber,
       "wlsxTrapVoltageType": wlsxTrapVoltageType,
       "wlsxTrapVoltageValue": wlsxTrapVoltageValue,
       "wlsxTrapStationBlackListReason": wlsxTrapStationBlackListReason,
       "wlsxTrapSpoofedIpAddress": wlsxTrapSpoofedIpAddress,
       "wlsxTrapSpoofedOldPhyAddress": wlsxTrapSpoofedOldPhyAddress,
       "wlsxTrapSpoofedNewPhyAddress": wlsxTrapSpoofedNewPhyAddress,
       "wlsxTrapDBName": wlsxTrapDBName,
       "wlsxTrapDBUserName": wlsxTrapDBUserName,
       "wlsxTrapDBIpAddress": wlsxTrapDBIpAddress,
       "wlsxTrapDBType": wlsxTrapDBType,
       "wlsxTrapVrrpID": wlsxTrapVrrpID,
       "wlsxTrapVrrpMasterIp": wlsxTrapVrrpMasterIp,
       "wlsxTrapVrrpOperState": wlsxTrapVrrpOperState,
       "wlsxTrapESIServerGrpName": wlsxTrapESIServerGrpName,
       "wlsxTrapESIServerName": wlsxTrapESIServerName,
       "wlsxTrapESIServerIpAddress": wlsxTrapESIServerIpAddress,
       "wlsxTrapLicenseDaysRemaining": wlsxTrapLicenseDaysRemaining,
       "wlsxTrapSwitchIp": wlsxTrapSwitchIp,
       "wlsxTrapSwitchRole": wlsxTrapSwitchRole,
       "wlsxTrapUserIpAddress": wlsxTrapUserIpAddress,
       "wlsxTrapUserPhyAddress": wlsxTrapUserPhyAddress,
       "wlsxTrapUserName": wlsxTrapUserName,
       "wlsxTrapUserRole": wlsxTrapUserRole,
       "wlsxTrapUserAuthenticationMethod": wlsxTrapUserAuthenticationMethod,
       "wlsxTrapAPRadioNumber": wlsxTrapAPRadioNumber,
       "wlsxTrapRogueInfoURL": wlsxTrapRogueInfoURL,
       "wlsxTrapInterferingAPInfoURL": wlsxTrapInterferingAPInfoURL,
       "wlsxTrapPortNumber": wlsxTrapPortNumber,
       "wlsxTrapTime": wlsxTrapTime,
       "wlsxTrapHostIp": wlsxTrapHostIp,
       "wlsxTrapHostPort": wlsxTrapHostPort,
       "wlsxTrapConfigurationId": wlsxTrapConfigurationId,
       "wlsxTrapCTSURL": wlsxTrapCTSURL,
       "wlsxTrapCTSTransferType": wlsxTrapCTSTransferType,
       "wlsxTrapConfigurationState": wlsxTrapConfigurationState,
       "wlsxTrapUpdateFailureReason": wlsxTrapUpdateFailureReason,
       "wlsxTrapUpdateFailedObj": wlsxTrapUpdateFailedObj,
       "wlsxTrapTableEntryChangeType": wlsxTrapTableEntryChangeType,
       "wlsxTrapGlobalConfigObj": wlsxTrapGlobalConfigObj,
       "wlsxTrapTableGenNumber": wlsxTrapTableGenNumber,
       "wlsxTrapLicenseId": wlsxTrapLicenseId,
       "wlsxTrapConfidenceLevel": wlsxTrapConfidenceLevel,
       "wlsxTrapMissingLicenses": wlsxTrapMissingLicenses,
       "wlsxVoiceCurrentNumCdr": wlsxVoiceCurrentNumCdr,
       "wlsxTrapTunnelId": wlsxTrapTunnelId,
       "wlsxTrapTunnelStatus": wlsxTrapTunnelStatus,
       "wlsxTrapTunnelUpReason": wlsxTrapTunnelUpReason,
       "wlsxTrapTunnelDownReason": wlsxTrapTunnelDownReason,
       "wlsxTrapApSerialNumber": wlsxTrapApSerialNumber,
       "wlsxTrapTimeStr": wlsxTrapTimeStr,
       "wlsxTrapMasterIp": wlsxTrapMasterIp,
       "wlsxTrapLocalIp": wlsxTrapLocalIp,
       "wlsxTrapMasterName": wlsxTrapMasterName,
       "wlsxTrapLocalName": wlsxTrapLocalName,
       "wlsxTrapPrimaryControllerIp": wlsxTrapPrimaryControllerIp,
       "wlsxTrapBackupControllerIp": wlsxTrapBackupControllerIp,
       "wlsxTrapSpoofedFrameType": wlsxTrapSpoofedFrameType,
       "wlsxTrapAssociationType": wlsxTrapAssociationType,
       "wlsxTrapDeviceIpAddress": wlsxTrapDeviceIpAddress,
       "wlsxTrapDeviceMac": wlsxTrapDeviceMac,
       "wlsxTrapVcIpAddress": wlsxTrapVcIpAddress,
       "wlsxTrapVcMacAddress": wlsxTrapVcMacAddress,
       "wlsxTrapAPName": wlsxTrapAPName,
       "wlsxTrapApMode": wlsxTrapApMode,
       "wlsxTrapAPPrevChannel": wlsxTrapAPPrevChannel,
       "wlsxTrapAPPrevChannelSec": wlsxTrapAPPrevChannelSec,
       "wlsxTrapAPPrevTxPower": wlsxTrapAPPrevTxPower,
       "wlsxTrapAPCurMode": wlsxTrapAPCurMode,
       "wlsxTrapAPPrevMode": wlsxTrapAPPrevMode,
       "wlsxTrapAPARMChangeReason": wlsxTrapAPARMChangeReason,
       "wlsxTrapAPChannelSec": wlsxTrapAPChannelSec,
       "wlsxTrapUserAttributeChangeType": wlsxTrapUserAttributeChangeType,
       "wlsxTrapApControllerIp": wlsxTrapApControllerIp,
       "wlsxTrapApMasterStatus": wlsxTrapApMasterStatus,
       "wlsxTrapCaName": wlsxTrapCaName,
       "wlsxTrapCrlName": wlsxTrapCrlName,
       "wlsxTrapCount": wlsxTrapCount,
       "wlsxTrapPowerSupplyNumber": wlsxTrapPowerSupplyNumber,
       "wlsxTrapFanTrayNumber": wlsxTrapFanTrayNumber,
       "wlsxTrapClientClassification": wlsxTrapClientClassification,
       "wlsxThresholdResourceType": wlsxThresholdResourceType,
       "wlsxThresholdResourceName": wlsxThresholdResourceName,
       "wlsxThresholdValue": wlsxThresholdValue,
       "wlsxResourceValue": wlsxResourceValue,
       "wlsxStackPrevSlot": wlsxStackPrevSlot,
       "wlsxStackCurrentSlot": wlsxStackCurrentSlot,
       "wlsxStackPrevState": wlsxStackPrevState,
       "wlsxStackCurrentState": wlsxStackCurrentState,
       "wlsxStackChangeEvent": wlsxStackChangeEvent,
       "wlsxStackProtoIfTopoJoined": wlsxStackProtoIfTopoJoined,
       "wlsxStackMemberMacAddress": wlsxStackMemberMacAddress,
       "wlsxStackMemberSlotNumber": wlsxStackMemberSlotNumber,
       "wlsxStackIfName": wlsxStackIfName,
       "wlsxTrapLicenseServerDaysRemaining": wlsxTrapLicenseServerDaysRemaining,
       "wlsxTrapLicenseClientDaysRemaining": wlsxTrapLicenseClientDaysRemaining,
       "wlsxIfIndex": wlsxIfIndex,
       "wlsxIfState": wlsxIfState,
       "wlsxIfStateChangeReason": wlsxIfStateChangeReason,
       "wlsxTrapAPPreviousUplinkType": wlsxTrapAPPreviousUplinkType,
       "wlsxTrapAPPreviousUplinkActiveTime": wlsxTrapAPPreviousUplinkActiveTime,
       "wlsxTrapAPActiveUplinkType": wlsxTrapAPActiveUplinkType,
       "wlsxTrapAPUplinkChangeReason": wlsxTrapAPUplinkChangeReason,
       "wlsxTrapExpiringCertName": wlsxTrapExpiringCertName,
       "wlsxTrapExpiredCertName": wlsxTrapExpiredCertName,
       "wlsxTrapHTMode": wlsxTrapHTMode,
       "wlsxTrapPhyType": wlsxTrapPhyType,
       "wlsxTrapAPManagedModeConfigFailure": wlsxTrapAPManagedModeConfigFailure,
       "wlsxTrapAuthServerAddress": wlsxTrapAuthServerAddress,
       "wlsxTrapPortalServerName": wlsxTrapPortalServerName,
       "wlsxTrapPortalServerAddress": wlsxTrapPortalServerAddress,
       "wlsxTrapPortalServerDownReason": wlsxTrapPortalServerDownReason,
       "wlsxTrapLicensePlatformMismatchKey": wlsxTrapLicensePlatformMismatchKey,
       "wlsxTrapTargetAPName": wlsxTrapTargetAPName,
       "wlsxTrapTargetAPMac": wlsxTrapTargetAPMac,
       "wlsxTrapAPUSBStatus": wlsxTrapAPUSBStatus,
       "wlsxTrapUSBVendorProductID": wlsxTrapUSBVendorProductID,
       "wlsxTrapSwitchIpv6": wlsxTrapSwitchIpv6,
       "wlsxTrapStationBlackListReasonStr": wlsxTrapStationBlackListReasonStr,
       "wlsxTrapPeerIpAddress": wlsxTrapPeerIpAddress,
       "wlsxTrapConnectionStatus": wlsxTrapConnectionStatus,
       "wlsxTrapFailedVlan": wlsxTrapFailedVlan,
       "wlsxTrapMatchedIpv6": wlsxTrapMatchedIpv6,
       "wlsxTrapDeviceIpv6Address": wlsxTrapDeviceIpv6Address,
       "wlsxTrapAuthFailureReason": wlsxTrapAuthFailureReason,
       "wlsxTrapDefinitionsGroup": wlsxTrapDefinitionsGroup,
       "wlsxVlanLinkUp": wlsxVlanLinkUp,
       "wlsxVlanLinkDown": wlsxVlanLinkDown,
       "wlsxSignatureMatch": wlsxSignatureMatch,
       "wlsxNodeRateAnomaly": wlsxNodeRateAnomaly,
       "wlsxNormalTemperature": wlsxNormalTemperature,
       "wlsxProcessRestart": wlsxProcessRestart,
       "wlsxFlashSpaceOK": wlsxFlashSpaceOK,
       "wlsxMemoryUsageOK": wlsxMemoryUsageOK,
       "wlsxPowerSupplyOK": wlsxPowerSupplyOK,
       "wlsxFanOK": wlsxFanOK,
       "wlsxInRangeVoltage": wlsxInRangeVoltage,
       "wlsxCoverageHoleResolved": wlsxCoverageHoleResolved,
       "wlsxNSwitchIPChanged": wlsxNSwitchIPChanged,
       "wlsxNSwitchRoleChange": wlsxNSwitchRoleChange,
       "wlsxNUserEntryCreated": wlsxNUserEntryCreated,
       "wlsxNUserEntryDeleted": wlsxNUserEntryDeleted,
       "wlsxNUserEntryAuthenticated": wlsxNUserEntryAuthenticated,
       "wlsxNUserEntryDeAuthenticated": wlsxNUserEntryDeAuthenticated,
       "wlsxNUserAuthenticationFailed": wlsxNUserAuthenticationFailed,
       "wlsxNAuthServerReqTimedOut": wlsxNAuthServerReqTimedOut,
       "wlsxNAuthServerTimedOut": wlsxNAuthServerTimedOut,
       "wlsxNAuthServerIsUp": wlsxNAuthServerIsUp,
       "wlsxNAuthMaxUserEntries": wlsxNAuthMaxUserEntries,
       "wlsxNAuthMaxAclEntries": wlsxNAuthMaxAclEntries,
       "wlsxNAuthMaxBWContracts": wlsxNAuthMaxBWContracts,
       "wlsxNPowerSupplyFailure": wlsxNPowerSupplyFailure,
       "wlsxNFanFailure": wlsxNFanFailure,
       "wlsxNOutOfRangeVoltage": wlsxNOutOfRangeVoltage,
       "wlsxNOutOfRangeTemperature": wlsxNOutOfRangeTemperature,
       "wlsxNLCInserted": wlsxNLCInserted,
       "wlsxNSCInserted": wlsxNSCInserted,
       "wlsxNGBICInserted": wlsxNGBICInserted,
       "wlsxNProcessDied": wlsxNProcessDied,
       "wlsxNProcessExceedsMemoryLimits": wlsxNProcessExceedsMemoryLimits,
       "wlsxNLowOnFlashSpace": wlsxNLowOnFlashSpace,
       "wlsxNLowMemory": wlsxNLowMemory,
       "wlsxNFanTrayRemoved": wlsxNFanTrayRemoved,
       "wlsxNFanTrayInserted": wlsxNFanTrayInserted,
       "wlsxNLCRemoved": wlsxNLCRemoved,
       "wlsxNPowerSupplyMissing": wlsxNPowerSupplyMissing,
       "wlsxNAccessPointIsUp": wlsxNAccessPointIsUp,
       "wlsxNAccessPointIsDown": wlsxNAccessPointIsDown,
       "wlsxNCoverageHoleDetected": wlsxNCoverageHoleDetected,
       "wlsxNChannelChanged": wlsxNChannelChanged,
       "wlsxNStationAddedToBlackList": wlsxNStationAddedToBlackList,
       "wlsxNStationRemovedFromBlackList": wlsxNStationRemovedFromBlackList,
       "wlsxNIpSpoofingDetected": wlsxNIpSpoofingDetected,
       "wlsxNDBCommunicationFailure": wlsxNDBCommunicationFailure,
       "wlsxNVrrpStateChange": wlsxNVrrpStateChange,
       "wlsxNRadioAttributesChanged": wlsxNRadioAttributesChanged,
       "wlsxNESIServerUp": wlsxNESIServerUp,
       "wlsxNESIServerDown": wlsxNESIServerDown,
       "wlsxNLicenseExpiry": wlsxNLicenseExpiry,
       "wlsxUnsecureAPDetected": wlsxUnsecureAPDetected,
       "wlsxUnsecureAPResolved": wlsxUnsecureAPResolved,
       "wlsxStaImpersonation": wlsxStaImpersonation,
       "wlsxReservedChannelViolation": wlsxReservedChannelViolation,
       "wlsxValidSSIDViolation": wlsxValidSSIDViolation,
       "wlsxChannelMisconfiguration": wlsxChannelMisconfiguration,
       "wlsxOUIMisconfiguration": wlsxOUIMisconfiguration,
       "wlsxSSIDMisconfiguration": wlsxSSIDMisconfiguration,
       "wlsxShortPreableMisconfiguration": wlsxShortPreableMisconfiguration,
       "wlsxWPAMisconfiguration": wlsxWPAMisconfiguration,
       "wlsxAdhocNetworkDetected": wlsxAdhocNetworkDetected,
       "wlsxAdhocNetworkRemoved": wlsxAdhocNetworkRemoved,
       "wlsxStaPolicyViolation": wlsxStaPolicyViolation,
       "wlsxRepeatWEPIVViolation": wlsxRepeatWEPIVViolation,
       "wlsxWeakWEPIVViolation": wlsxWeakWEPIVViolation,
       "wlsxChannelInterferenceDetected": wlsxChannelInterferenceDetected,
       "wlsxChannelInterferenceCleared": wlsxChannelInterferenceCleared,
       "wlsxAPInterferenceDetected": wlsxAPInterferenceDetected,
       "wlsxAPInterferenceCleared": wlsxAPInterferenceCleared,
       "wlsxStaInterferenceDetected": wlsxStaInterferenceDetected,
       "wlsxStaInterferenceCleared": wlsxStaInterferenceCleared,
       "wlsxFrameRetryRateExceeded": wlsxFrameRetryRateExceeded,
       "wlsxFrameReceiveErrorRateExceeded": wlsxFrameReceiveErrorRateExceeded,
       "wlsxFrameFragmentationRateExceeded": wlsxFrameFragmentationRateExceeded,
       "wlsxFrameBandWidthRateExceeded": wlsxFrameBandWidthRateExceeded,
       "wlsxFrameLowSpeedRateExceeded": wlsxFrameLowSpeedRateExceeded,
       "wlsxFrameNonUnicastRateExceeded": wlsxFrameNonUnicastRateExceeded,
       "wlsxLoadbalancingEnabled": wlsxLoadbalancingEnabled,
       "wlsxLoadbalancingDisabled": wlsxLoadbalancingDisabled,
       "wlsxChannelFrameRetryRateExceeded": wlsxChannelFrameRetryRateExceeded,
       "wlsxChannelFrameFragmentationRateExceeded": wlsxChannelFrameFragmentationRateExceeded,
       "wlsxChannelFrameErrorRateExceeded": wlsxChannelFrameErrorRateExceeded,
       "wlsxSignatureMatchAP": wlsxSignatureMatchAP,
       "wlsxSignatureMatchSta": wlsxSignatureMatchSta,
       "wlsxChannelRateAnomaly": wlsxChannelRateAnomaly,
       "wlsxNodeRateAnomalyAP": wlsxNodeRateAnomalyAP,
       "wlsxNodeRateAnomalySta": wlsxNodeRateAnomalySta,
       "wlsxEAPRateAnomaly": wlsxEAPRateAnomaly,
       "wlsxSignalAnomaly": wlsxSignalAnomaly,
       "wlsxSequenceNumberAnomalyAP": wlsxSequenceNumberAnomalyAP,
       "wlsxSequenceNumberAnomalySta": wlsxSequenceNumberAnomalySta,
       "wlsxDisconnectStationAttack": wlsxDisconnectStationAttack,
       "wlsxApFloodAttack": wlsxApFloodAttack,
       "wlsxAdhocNetwork": wlsxAdhocNetwork,
       "wlsxWirelessBridge": wlsxWirelessBridge,
       "wlsxInvalidMacOUIAP": wlsxInvalidMacOUIAP,
       "wlsxInvalidMacOUISta": wlsxInvalidMacOUISta,
       "wlsxWEPMisconfiguration": wlsxWEPMisconfiguration,
       "wlsxStaRepeatWEPIVViolation": wlsxStaRepeatWEPIVViolation,
       "wlsxStaWeakWEPIVViolation": wlsxStaWeakWEPIVViolation,
       "wlsxStaAssociatedToUnsecureAP": wlsxStaAssociatedToUnsecureAP,
       "wlsxStaUnAssociatedFromUnsecureAP": wlsxStaUnAssociatedFromUnsecureAP,
       "wlsxAdhocNetworkBridgeDetected": wlsxAdhocNetworkBridgeDetected,
       "wlsxInterferingApDetected": wlsxInterferingApDetected,
       "wlsxPortUp": wlsxPortUp,
       "wlsxPortDown": wlsxPortDown,
       "wlsxBSSIDIsUp": wlsxBSSIDIsUp,
       "wlsxBSSIDIsDown": wlsxBSSIDIsDown,
       "wlsxColdStart": wlsxColdStart,
       "wlsxWarmStart": wlsxWarmStart,
       "wlsxAPImpersonation": wlsxAPImpersonation,
       "wlsxInformQueueOverFlow": wlsxInformQueueOverFlow,
       "wlsxNAuthServerIsDown": wlsxNAuthServerIsDown,
       "wlsxCTSTransferError": wlsxCTSTransferError,
       "wlsxCTSTransferSucceeded": wlsxCTSTransferSucceeded,
       "wlsxConfigurationUpdateError": wlsxConfigurationUpdateError,
       "wlsxConfigurationUpdateSucceeded": wlsxConfigurationUpdateSucceeded,
       "wlsxGlobalConfigurationChangeNotification": wlsxGlobalConfigurationChangeNotification,
       "wlsxUserEntryChanged": wlsxUserEntryChanged,
       "wlsxAPBssidEntryChanged": wlsxAPBssidEntryChanged,
       "wlsxAPRadioEntryChanged": wlsxAPRadioEntryChanged,
       "wlsxAPEntryChanged": wlsxAPEntryChanged,
       "wlsxSwitchListEntryChanged": wlsxSwitchListEntryChanged,
       "wlsxPortEntryChanged": wlsxPortEntryChanged,
       "wlsxVlanEntryChanged": wlsxVlanEntryChanged,
       "wlsxVlanInterfaceEntryChanged": wlsxVlanInterfaceEntryChanged,
       "wlsxWindowsBridgeDetected": wlsxWindowsBridgeDetected,
       "wlsxLicenseEntryChanged": wlsxLicenseEntryChanged,
       "wlsxEsiServerChanged": wlsxEsiServerChanged,
       "wlsxMonAPEntryChanged": wlsxMonAPEntryChanged,
       "wlsxMonStationEntryChanged": wlsxMonStationEntryChanged,
       "wlsxSignAPNetstumbler": wlsxSignAPNetstumbler,
       "wlsxSignStaNetstumbler": wlsxSignStaNetstumbler,
       "wlsxSignAPAsleap": wlsxSignAPAsleap,
       "wlsxSignStaAsleap": wlsxSignStaAsleap,
       "wlsxSignAPAirjack": wlsxSignAPAirjack,
       "wlsxSignStaAirjack": wlsxSignStaAirjack,
       "wlsxSignAPNullProbeResp": wlsxSignAPNullProbeResp,
       "wlsxSignStaNullProbeResp": wlsxSignStaNullProbeResp,
       "wlsxSignAPDeauthBcast": wlsxSignAPDeauthBcast,
       "wlsxSignStaDeauthBcast": wlsxSignStaDeauthBcast,
       "wlsxWindowsBridgeDetectedAP": wlsxWindowsBridgeDetectedAP,
       "wlsxWindowsBridgeDetectedSta": wlsxWindowsBridgeDetectedSta,
       "wlsxAdhocNetworkBridgeDetectedAP": wlsxAdhocNetworkBridgeDetectedAP,
       "wlsxAdhocNetworkBridgeDetectedSta": wlsxAdhocNetworkBridgeDetectedSta,
       "wlsxDisconnectStationAttackAP": wlsxDisconnectStationAttackAP,
       "wlsxDisconnectStationAttackSta": wlsxDisconnectStationAttackSta,
       "wlsxSuspectUnsecureAPDetected": wlsxSuspectUnsecureAPDetected,
       "wlsxSuspectUnsecureAPResolved": wlsxSuspectUnsecureAPResolved,
       "wlsxConfigurationLicenseMismatch": wlsxConfigurationLicenseMismatch,
       "wlsxVoiceCdrBufferThresholdReached": wlsxVoiceCdrBufferThresholdReached,
       "wlsxTunnelUp": wlsxTunnelUp,
       "wlsxTunnelDown": wlsxTunnelDown,
       "wlsxMeshNodeEntryChanged": wlsxMeshNodeEntryChanged,
       "wlsxHtGreenfieldSupported": wlsxHtGreenfieldSupported,
       "wlsxHT40MHzIntoleranceAP": wlsxHT40MHzIntoleranceAP,
       "wlsxHT40MHzIntoleranceSta": wlsxHT40MHzIntoleranceSta,
       "wlsxNAuthServerAllInService": wlsxNAuthServerAllInService,
       "wlsxNAdhocNetwork": wlsxNAdhocNetwork,
       "wlsxNAdhocNetworkBridgeDetectedAP": wlsxNAdhocNetworkBridgeDetectedAP,
       "wlsxNAdhocNetworkBridgeDetectedSta": wlsxNAdhocNetworkBridgeDetectedSta,
       "wlsxNAuthMaxXsecUserEntries": wlsxNAuthMaxXsecUserEntries,
       "wlsxNVpnMaxSessions": wlsxNVpnMaxSessions,
       "wlsxNRapExpiredPSK": wlsxNRapExpiredPSK,
       "wlsxNRapWarnExpiredPSK": wlsxNRapWarnExpiredPSK,
       "wlsxNConnectionResetWithLocal": wlsxNConnectionResetWithLocal,
       "wlsxNApOnBackupController": wlsxNApOnBackupController,
       "wlsxClientFloodAttack": wlsxClientFloodAttack,
       "wlsxValidClientNotUsingEncryption": wlsxValidClientNotUsingEncryption,
       "wlsxAdhocUsingValidSSID": wlsxAdhocUsingValidSSID,
       "wlsxAPSpoofingDetected": wlsxAPSpoofingDetected,
       "wlsxClientAssociatingOnWrongChannel": wlsxClientAssociatingOnWrongChannel,
       "wlsxNDisconnectStationAttack": wlsxNDisconnectStationAttack,
       "wlsxNStaUnAssociatedFromUnsecureAP": wlsxNStaUnAssociatedFromUnsecureAP,
       "wlsxOmertaAttack": wlsxOmertaAttack,
       "wlsxTKIPReplayAttack": wlsxTKIPReplayAttack,
       "wlsxChopChopAttack": wlsxChopChopAttack,
       "wlsxFataJackAttack": wlsxFataJackAttack,
       "wlsxInvalidAddressCombination": wlsxInvalidAddressCombination,
       "wlsxValidClientMisassociation": wlsxValidClientMisassociation,
       "wlsxMalformedHTIEDetected": wlsxMalformedHTIEDetected,
       "wlsxMalformedAssocReqDetected": wlsxMalformedAssocReqDetected,
       "wlsxOverflowIEDetected": wlsxOverflowIEDetected,
       "wlsxOverflowEAPOLKeyDetected": wlsxOverflowEAPOLKeyDetected,
       "wlsxMalformedFrameLargeDurationDetected": wlsxMalformedFrameLargeDurationDetected,
       "wlsxMalformedFrameWrongChannelDetected": wlsxMalformedFrameWrongChannelDetected,
       "wlsxMalformedAuthFrame": wlsxMalformedAuthFrame,
       "wlsxCTSRateAnomaly": wlsxCTSRateAnomaly,
       "wlsxRTSRateAnomaly": wlsxRTSRateAnomaly,
       "wlsxNRogueAPDetected": wlsxNRogueAPDetected,
       "wlsxNRogueAPResolved": wlsxNRogueAPResolved,
       "wlsxNeighborAPDetected": wlsxNeighborAPDetected,
       "wlsxNInterferingAPDetected": wlsxNInterferingAPDetected,
       "wlsxNSuspectRogueAPDetected": wlsxNSuspectRogueAPDetected,
       "wlsxNSuspectRogueAPResolved": wlsxNSuspectRogueAPResolved,
       "wlsxBlockAckAttackDetected": wlsxBlockAckAttackDetected,
       "wlsxHotspotterAttackDetected": wlsxHotspotterAttackDetected,
       "wlsxNSignatureMatch": wlsxNSignatureMatch,
       "wlsxNSignatureMatchNetstumbler": wlsxNSignatureMatchNetstumbler,
       "wlsxNSignatureMatchAsleap": wlsxNSignatureMatchAsleap,
       "wlsxNSignatureMatchAirjack": wlsxNSignatureMatchAirjack,
       "wlsxNSignatureMatchNullProbeResp": wlsxNSignatureMatchNullProbeResp,
       "wlsxNSignatureMatchDeauthBcast": wlsxNSignatureMatchDeauthBcast,
       "wlsxNSignatureMatchDisassocBcast": wlsxNSignatureMatchDisassocBcast,
       "wlsxNSignatureMatchWellenreiter": wlsxNSignatureMatchWellenreiter,
       "wlsxAPDeauthContainment": wlsxAPDeauthContainment,
       "wlsxClientDeauthContainment": wlsxClientDeauthContainment,
       "wlsxAPWiredContainment": wlsxAPWiredContainment,
       "wlsxClientWiredContainment": wlsxClientWiredContainment,
       "wlsxAPTaggedWiredContainment": wlsxAPTaggedWiredContainment,
       "wlsxClientTaggedWiredContainment": wlsxClientTaggedWiredContainment,
       "wlsxTarpitContainment": wlsxTarpitContainment,
       "wlsxVoiceClientLocationUpdate": wlsxVoiceClientLocationUpdate,
       "wlsxAPChannelChange": wlsxAPChannelChange,
       "wlsxAPPowerChange": wlsxAPPowerChange,
       "wlsxAPModeChange": wlsxAPModeChange,
       "wlsxUserEntryAttributesChanged": wlsxUserEntryAttributesChanged,
       "wlsxPowerSaveDosAttack": wlsxPowerSaveDosAttack,
       "wlsxNAPMasterStatusChange": wlsxNAPMasterStatusChange,
       "wlsxNAdhocUsingValidSSID": wlsxNAdhocUsingValidSSID,
       "wlsxCRLExpired": wlsxCRLExpired,
       "wlsxMgmtUserAuthenticationFailed": wlsxMgmtUserAuthenticationFailed,
       "wlsxNConnectionBackfromLocal": wlsxNConnectionBackfromLocal,
       "wlsxAPNumUpgradeFailure": wlsxAPNumUpgradeFailure,
       "wlsxAPNumWarmStarts": wlsxAPNumWarmStarts,
       "wlsxAPNumColdStarts": wlsxAPNumColdStarts,
       "wlsxAPNumDown": wlsxAPNumDown,
       "wlsxAPNumRadioDown": wlsxAPNumRadioDown,
       "wlsxNumClockSyncErrors": wlsxNumClockSyncErrors,
       "wlsxNumColdStart": wlsxNumColdStart,
       "wlsxNumWarmStart": wlsxNumWarmStart,
       "wlsxWirelessHostedNetworkDetected": wlsxWirelessHostedNetworkDetected,
       "wlsxClientAssociatedToHostedNetwork": wlsxClientAssociatedToHostedNetwork,
       "wlsxThresholdExceeded": wlsxThresholdExceeded,
       "wlsxThresholdCleared": wlsxThresholdCleared,
       "wlsxWirelessHostedNetworkContainment": wlsxWirelessHostedNetworkContainment,
       "wlsxHostOfWirelessNetworkContainment": wlsxHostOfWirelessNetworkContainment,
       "wlsxEnhancedAdhocContainment": wlsxEnhancedAdhocContainment,
       "wlsxPowerSupplyOKTrap": wlsxPowerSupplyOKTrap,
       "wlsxPowerSupplyFailureTrap": wlsxPowerSupplyFailureTrap,
       "wlsxFanTrayRemovedTrap": wlsxFanTrayRemovedTrap,
       "wlsxFanTrayInsertedTrap": wlsxFanTrayInsertedTrap,
       "wlsxPowerSupplyMissingTrap": wlsxPowerSupplyMissingTrap,
       "wlsxStackTopologyChangeTrap": wlsxStackTopologyChangeTrap,
       "wlsxStackIfStateChangeTrap": wlsxStackIfStateChangeTrap,
       "wlsxLicenseServerExpiry": wlsxLicenseServerExpiry,
       "wlsxLicenseClientExpiry": wlsxLicenseClientExpiry,
       "wlsxIfStateChangeTrap": wlsxIfStateChangeTrap,
       "wlsxWMSOffloadRecommended": wlsxWMSOffloadRecommended,
       "wlsxAPActiveUplinkChanged": wlsxAPActiveUplinkChanged,
       "wlsxCertExpiringSoon": wlsxCertExpiringSoon,
       "wlsxCertExpired": wlsxCertExpired,
       "wlsxAPManagedModeConfigFailureTrap": wlsxAPManagedModeConfigFailureTrap,
       "wlsxNAuthServerAcctTimedOut": wlsxNAuthServerAcctTimedOut,
       "wlsxAPUp": wlsxAPUp,
       "wlsxAPDown": wlsxAPDown,
       "wlsxPortalServerDown": wlsxPortalServerDown,
       "wlsxPortalServerUp": wlsxPortalServerUp,
       "wlsxNAdhocUsingValidSSIDContainment": wlsxNAdhocUsingValidSSIDContainment,
       "wlsxLicensePlatformMismatch": wlsxLicensePlatformMismatch,
       "wlsxIAPVoiceClientLocationUpdate": wlsxIAPVoiceClientLocationUpdate,
       "wlsxNAceUsageThreshold": wlsxNAceUsageThreshold,
       "wlsxNWebCCLicenseEnforcement": wlsxNWebCCLicenseEnforcement,
       "wlsxNFanAbsent": wlsxNFanAbsent,
       "wlsxWPAFTAttack": wlsxWPAFTAttack,
       "wlsxMitMDetected": wlsxMitMDetected,
       "wlsxAPPortUp": wlsxAPPortUp,
       "wlsxAPPortDown": wlsxAPPortDown,
       "wlsxAPLoopDetected": wlsxAPLoopDetected,
       "wlsxAPBROADCASTSTORM": wlsxAPBROADCASTSTORM,
       "wlsxAPIPConflict": wlsxAPIPConflict,
       "wlsxCLEARPASSSERVERINVALID": wlsxCLEARPASSSERVERINVALID,
       "wlsxNLowOnFlash1Space": wlsxNLowOnFlash1Space,
       "wlsxFlash1SpaceOK": wlsxFlash1SpaceOK,
       "wlsxTHERMALSHUTDOWN": wlsxTHERMALSHUTDOWN,
       "wlsxPhonyBSSIDDetected": wlsxPhonyBSSIDDetected,
       "wlsxAPUSBPLUGALARM": wlsxAPUSBPLUGALARM,
       "wlsxNSwitchIPv6Changed": wlsxNSwitchIPv6Changed,
       "wlsxNDot1xThresholdLimitHit": wlsxNDot1xThresholdLimitHit,
       "wlsxNDot1xTotalLimitHit": wlsxNDot1xTotalLimitHit,
       "wlsxClusterVlanProbeStatus": wlsxClusterVlanProbeStatus,
       "wlsxClientRejectedByMaxClientCount": wlsxClientRejectedByMaxClientCount,
       "wlsxClientPskAuthenticationFailed": wlsxClientPskAuthenticationFailed}
)
