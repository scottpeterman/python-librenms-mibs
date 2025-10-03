# SNMP MIB module (MERU-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:59 2025
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

(meru_modules,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "meru-modules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

meruTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MwlAclEnvState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aclEnvDisabled", 0),
          ("aclEnvAllow", 1),
          ("aclEnvDeny", 2))
    )



class MwlAddressAssignmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipAssignmentStatic", 1),
          ("ipAssignmentDynamic", 2),
          ("ipAssignmentDynamicDhcp", 3),
          ("ipAssignmentUnknown", 4))
    )



class MwlAddressIfAssignmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifIpAssignmentNone", 0),
          ("ifIpAssignmentStatic", 1),
          ("ifIpAssignmentDhcp", 2))
    )



class MwlApIpAssignmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apIpAssignmentNone", 0),
          ("apIpAssignmentStatic", 1),
          ("apIpAssignmentDhcp", 2))
    )



class MwlAdministrativeState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("adminStateUnlocked", 1),
          ("adminStateLocked", 2),
          ("adminStateShuttingDown", 3),
          ("adminStateUnknown", 4),
          ("adminStateForceShuttingDown", 5))
    )



class MwlAdmissionControl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admitall", 0),
          ("pendingflag", 1),
          ("rejectflag", 2))
    )



class MwlAntennaSet(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("antennaSetUnknown", 0),
          ("antennaSetInternal", 1),
          ("antennaSetExternal", 2),
          ("antennaSetExternalDualMode", 3),
          ("antennaSetRsAntenna", 4))
    )



class MwlApAssignType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assignApUnknown", 0),
          ("siblingAp", 1),
          ("assignedAp", 2),
          ("discoveredAp", 3))
    )



class MwlApType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apUnknown", 0),
          ("apStation", 1),
          ("apAccessPoint", 2))
    )



class MwlApIndoorOutdoorType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apIndoor", 0),
          ("apOutdoor", 1))
    )



class MwlApMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("apModeService", 1),
          ("apModeScanRogues", 100),
          ("apModeScanSpectrum", 101))
    )



class MwlAuthenticationAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nmsAuthenticationAlg8021x", 1),
          ("nmsAuthenticationAlgMd5", 2),
          ("nmsAuthenticationAlgTls", 3),
          ("nmsAuthenticationAlgTtls", 4),
          ("nmsAuthenticationAlgPeap", 5),
          ("nmsAuthenticationAlgWeb", 6))
    )



class MwlAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsAuthenticationTypeLocal", 1),
          ("nmsAuthenticationTypeRadius", 2),
          ("nmsAuthenticationTypeTacacs", 3))
    )



class MwlManagementFrameProtection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsManagementFrameProtectionTypeDisable", 0),
          ("nmsManagementFrameProtectionTypeCapable", 1),
          ("nmsManagementFrameProtectionTypeRequired", 2))
    )



class MwlCaptivePortalAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsCaptivePortalAuthenticationTypeRadius", 0),
          ("nmsCaptivePortalAuthenticationTypeLocal", 1),
          ("nmsCaptivePortalAuthenticationTypeLocalRadius", 2))
    )



class MwlCaptivePortalExternalServerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsCpExternalServerFortinetConnect", 0),
          ("nmsCpExternalServerFortinetPresence", 1))
    )



class MwlCaptivePortalModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsCaptivePortalModeTypeDefault", 0),
          ("nmsCaptivePortalModeTypeCustom", 1))
    )



class MwlAuthSuiteBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("authNone", 0),
          ("authEap", 1),
          ("authPsk", 2),
          ("authCert", 3),
          ("authAll", 4))
    )


class MwlActionStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("actionNone", 0),
          ("actionStart", 1),
          ("actionStop", 2),
          ("actionInProgress", 3),
          ("actionError", 4),
          ("actionDone", 5),
          ("actionForceStart", 6))
    )



class MwlAlarmState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alarmStateNoAlarm", 1),
          ("alarmStateMinor", 2),
          ("alarmStateMajor", 3),
          ("alarmStateCritical", 4))
    )



class MwlNotificationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230)
        )
    )
    namedValues = NamedValues(
        *(("notifUnknown", 0),
          ("notifLinkDown", 101),
          ("notifApDown", 102),
          ("notifApWirelessIfDown", 103),
          ("notifApSoftwareVersionMismatch", 104),
          ("notifSoftwareLicenseExpired", 105),
          ("notifSoftwareLicenseViolated", 106),
          ("notifMasterDown", 107),
          ("notifApWirelessIfStationCapacityFull", 108),
          ("notifWncMemoryUsageHigh", 109),
          ("notifWncCpuUsageHigh", 110),
          ("notifApMemoryUsageHigh", 111),
          ("notifApCpuUsageHigh", 112),
          ("notifDhcpAddressPoolExhausted", 113),
          ("notifWatchdogFailure", 114),
          ("notifApRadioCardFailure", 115),
          ("notifRadiusServerFailure", 116),
          ("notifRogueApDetected", 117),
          ("notifApRuntimeError", 118),
          ("notifAlarmHistoryFull", 119),
          ("notifEventLogFull", 120),
          ("notifPowerModuleFailure", 121),
          ("notifFanModuleFailure", 122),
          ("notifApWirelessIfDownDuetoFallbackChannelNotFound", 123),
          ("notifApLicenseExceeded", 124),
          ("notifNewApPostChPl", 125),
          ("notifAdminLoginFailure", 201),
          ("notif8021xAuthFailure", 202),
          ("notifTkipIntegrityCheckFailure", 203),
          ("notifMicCounterMeasureActivation", 204),
          ("notifCacLimitReached", 205),
          ("notifControllerIpAddressChange", 206),
          ("notifDfsChannelUpdate", 207),
          ("notifCertificateError", 208),
          ("notifCertificateInstalled", 209),
          ("notifRadiusServerSwitchover", 210),
          ("notifRadiusServerSwitchoverFailure", 211),
          ("notifAlarmHistoryThresholdExceed", 212),
          ("notifEventLogThresholdExceed", 213),
          ("notifRadiusServerRestored", 214),
          ("notifSystemIdChanged", 215),
          ("notifInterferenceDetected", 216),
          ("notifHighChannelUtilization", 217),
          ("notifLowChannelQuality", 218),
          ("notifNoLicenseEnforcementExpired", 219),
          ("notifPowerNotAtDisableLacp", 220),
          ("notifSwitchNotSupportDisableLacp", 221),
          ("notifAp822HwRevNotSupported", 222),
          ("notifOap832PowerNotSupported", 223),
          ("notifReinitDb", 224),
          ("notifApModelNotSupported", 225),
          ("notifServiceDown", 226),
          ("notifPlanningChannelBad", 227),
          ("notifImproperApRfPositioning", 228),
          ("notifMcaChannelChange", 229),
          ("notifApPowerChanged", 230))
    )



class MwlNotificationSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notificationSevInfo", 0),
          ("notificationSevMajor", 1),
          ("notificationSevMinor", 2),
          ("notificationSevCritical", 3),
          ("notificationSevClear", 4),
          ("notificationSevUpdate", 5))
    )



class MwlAntenna(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("antennaNothing", 0),
          ("antenna1", 1),
          ("antenna2", 2),
          ("antennaBoth", 3),
          ("antennaAll", 4))
    )



class MwlAssignmentAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("assignmentAlgoRssi", 1),
          ("assignmentAlgoPressure", 2),
          ("assignmentAlgoActivity", 3),
          ("assignmentAlgoRssiTrending", 4),
          ("assignmentAlgoAvailRsrc", 5),
          ("assignmentAlgoUnknown", 6))
    )



class MwlAssociationState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assocstateprobing", 0),
          ("assocstateauthentication", 1),
          ("assocstateassociated", 2))
    )



class MwlApAuthState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apAuthKeyed", 0),
          ("apAuthNokey", 1),
          ("apUnauth", 2))
    )



class MwlAvailabilityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("availStatusPowerOff", 1),
          ("availStatusOffline", 2),
          ("availStatusOnline", 3),
          ("availStatusFailed", 4),
          ("availStatusInTest", 5),
          ("availStatusNotInstalled", 6))
    )



class MwlBeaconCoordinationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beaconCoordinationModeCoordinated", 0),
          ("beaconCoordinationModeLocal", 1),
          ("beaconCoordinationModeDistributed", 2))
    )



class MwlBlock(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockNone", 0),
          ("blockSelected", 1),
          ("blockAll", 2),
          ("wiredRogue", 3))
    )



class MwlCoordAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coordAlgoDefault", 1),
          ("coordAlgoUnknown", 2))
    )



class MwlCypherSuiteBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cypherNone", 0),
          ("cypherWep40", 1),
          ("cypherWep104", 2),
          ("cypherTkip", 4),
          ("cypherCcmp", 8),
          ("cypherCcmpTkip", 16),
          ("cypherWpiSms4", 32),
          ("cypherClear", 64),
          ("cypherAll", 127))
    )


class MwlL2BridgingsBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bridgingNone", 0),
          ("bridgingAirf", 1),
          ("bridgingIpv6", 2),
          ("bridgingAtalk", 4))
    )


class MwlACMSupportsBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("acmNone", 0),
          ("acmVoice", 1),
          ("acmVideo", 2))
    )


class MwlDropPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drophead", 0),
          ("droptail", 1))
    )



class MwlDataplaneMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dataplaneModeTunneled", 0),
          ("dataplaneModeBridged", 1))
    )



class MwlProfileOwner(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("profileOwnerController", 0),
          ("profileOwnerNmsServer", 1))
    )



class MwlApRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apRoleAccess", 0),
          ("apRoleGateway", 1),
          ("apRoleWireless", 2))
    )



class MwlEncryptionAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("encryptionWep", 1),
          ("encryptionTkip", 2),
          ("encryptionCcmp", 3),
          ("encryptionUnknown", 4),
          ("encryptionClear", 5))
    )



class MwlIfAdministrativeState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminStateDown", 1),
          ("adminStateUp", 2),
          ("adminStateTesting", 3))
    )



class MwlOperChanChangeReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operChanChangeNone", 0),
          ("operChanChangeDfs", 1),
          ("operChanChangeMesh", 2))
    )



class MwlOperStatusChangeReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("operStatusChangeFailure", 0),
          ("operStatusChangeDfs", 1))
    )



class MwlEssApAdminMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("essApAdminModeDown", 1),
          ("essApAdminModeUp", 2),
          ("essApAdminModeScanRogues", 3),
          ("essApAdminModeUnlicensed", 4),
          ("essAdminModeDisabled", 5),
          ("essAdminModeNoservice", 6),
          ("essApAdminModePowerdown", 7),
          ("essApAdminModeScanSpectrum", 8))
    )



class MwlLedMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ledModeNormal", 0),
          ("ledModeNodeId", 1),
          ("ledModeBlink", 2),
          ("ledModeDark", 3))
    )



class MwlLogSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("logSevEmerg", 0),
          ("logSevAlert", 1),
          ("logSevCritical", 2),
          ("logSevError", 3),
          ("logSevWarn", 4),
          ("logSevNotice", 5),
          ("logSevInfo", 6),
          ("logSevDebug", 7),
          ("logSevTotal", 8))
    )



class MwlLogType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("logUnknown", 0),
          ("logApDetected", 1),
          ("logDbBackup", 2),
          ("logDbRestore", 3),
          ("logSwUpgrade", 4),
          ("logConfigAdd", 5),
          ("logConfigMod", 6),
          ("logConfigDel", 7),
          ("logCertExpiry", 8),
          ("logVlan", 9),
          ("logHaStart", 10),
          ("logHaShutdown", 11),
          ("logHaNodeDead", 12),
          ("logHaStatus", 13),
          ("logHaConfigErr", 14),
          ("logHaLinkStatus", 15),
          ("logApAdministrativeReboot", 16),
          ("logControllerAdministrativeReboot", 17),
          ("logDiscLicensingFailure", 18),
          ("logMicCountermeasure", 19),
          ("logMicFailureAp", 20),
          ("logMicFailureClient", 21),
          ("logTypeTotal", 22))
    )



class MwlMimoMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsMimoMode2x2", 0),
          ("nmsMimoMode3x3", 1),
          ("nmsMimoMode1x1", 2),
          ("nmsMimoMode4x4", 3))
    )



class MwlNatType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("natTypeNone", 1),
          ("natTypeStaticOneToOne", 2),
          ("natTypeDynamicOneToOne", 3),
          ("natTypeDynamicNapt", 4),
          ("natTypeUnknown", 5))
    )



class MwlNetProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("nmsIpprotoUnknown", 0),
          ("nmsIpprotoTcp", 6),
          ("nmsIpprotoUdp", 17))
    )



class MwlNmsInterfaceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ifTypeActive", 0),
          ("ifTypeRedundant", 1))
    )



class MwlNodeRelationship(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noderelationshipnone", 1),
          ("noderelationshipbound", 2),
          ("noderelationshipvisible", 3))
    )



class MwlNodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("nodeTypeWnc", 1),
          ("nodeTypeAp", 2),
          ("nodeTypeAsc", 3),
          ("nodeTypeSta", 10),
          ("nodeTypeOther", 11),
          ("nodeTypeUnknown", 12))
    )



class MwlOperationalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operationalStateUnknown", 0),
          ("operationalStateEnabled", 1),
          ("operationalStateDisabled", 2),
          ("operationalStateUnlicensed", 3),
          ("operationalStateEnabledWith11nlic", 4),
          ("operationalStatePowerDown", 5))
    )



class MwlPowerSupply(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("powerSupply8023Af", 0),
          ("powerSupply8023At", 1),
          ("powerSupply5vDc", 2),
          ("powerSupplyDual8023Af", 3),
          ("powerSupply12vDc", 4),
          ("powerSupply8023AtPlus", 5))
    )



class MwlRadiusMacDelimiter(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("radiusMacDelimiterNone", 0),
          ("radiusMacDelimiterHyphen", 1),
          ("radiusMacDelimiterSingleHyphen", 2),
          ("radiusMacDelimiterColon", 4))
    )



class MwlRadiusPasswordType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("radiusPasswordTypeSharedSecret", 0),
          ("radiusPasswordTypeMacAddress", 1))
    )



class MwlWlanOptimize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("optimizeNone", 0),
          ("optimizePerformance", 1),
          ("optimizeHandoff", 2),
          ("optimizeCoverage", 3),
          ("optimizeInteroperability", 4),
          ("optimizeRogueap", 5))
    )



class MwlOnOffSwitch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsOff", 0),
          ("nmsOn", 1))
    )



class MwlPublishEssId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("publishEssidOff", 0),
          ("publishEssidOn", 1),
          ("publishEssid24g", 2),
          ("publishEssid5g", 3))
    )



class MwlAllOnSelectedSwitch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsSelected", 0),
          ("nmsAllOn", 1))
    )



class MwlPrivacyBit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("privacyBitAuto", 0),
          ("privacyBitOn", 1),
          ("privacyBitOff", 2))
    )



class MwlQosAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsQosActionForward", 1),
          ("nmsQosActionCapture", 2),
          ("nmsQosActionDrop", 3))
    )



class MwlQosCodec(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("nmsCodecDefault", 1),
          ("nmsCodecaG711ULaw64k", 2),
          ("nmsCodeca1016", 3),
          ("nmsCodecaG721", 4),
          ("nmsCodecaGsm", 5),
          ("nmsCodecaG7231", 6),
          ("nmsCodecaDv14", 7),
          ("nmsCodecaDv142", 8),
          ("nmsCodecaLpc", 9),
          ("nmsCodecaG711ALaw64k", 10),
          ("nmsCodecaG722", 11),
          ("nmsCodecaG7221", 12),
          ("nmsCodecaG722132k", 13),
          ("nmsCodecaMpa", 14),
          ("nmsCodecaG728", 15),
          ("nmsCodecaG729", 16),
          ("nmsCodecaRed", 17),
          ("nmsCodecaSiren", 18),
          ("nmsCodecvH261", 19),
          ("nmsCodecvH263", 20))
    )



class MwlQosProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("qosprotocolsip", 1),
          ("qosprotocolh323", 2),
          ("qosprotocolsccp", 3),
          ("qosprotocolhttp", 4),
          ("qosprotocolother", 5),
          ("qosprotocolnone", 6),
          ("qosprotocolunknown", 7))
    )



class MwlQosCodecProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("qoscodecprotocolsip", 1),
          ("qoscodecprotocolh323", 2),
          ("qoscodecprotocolsccp", 3),
          ("qoscodecprotocolhttp", 4),
          ("qoscodecprotocolnone", 5),
          ("qoscodecprotocolunknown", 6))
    )



class MwlQosCallState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qoscalldisconnectedstate", 0),
          ("qoscallconnectedstate", 1),
          ("qoscallholdstate", 2),
          ("qoscallconferencingstate", 3))
    )



class MwlServiceAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsServiceActionAdd", 1),
          ("nmsServiceActionRemove", 2),
          ("nmsServiceActionChange", 3))
    )



class MwlSecurityPolicyAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("securityPolicyActionDeny", 0),
          ("securityPolicyActionAllow", 1),
          ("securityPolicyActionRedirect", 2),
          ("securityPolicyActionNum", 3))
    )



class MwlL2SecurityModeBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("l2SecurityModeNone", 0),
          ("l2SecurityModeOpen", 1),
          ("l2SecurityMode8021x", 2),
          ("l2SecurityModeSwk", 4),
          ("l2SecurityModeWpa", 8),
          ("l2SecurityModeWpaPsk", 16),
          ("l2SecurityModeWpa2", 32),
          ("l2SecurityModeWpa2Psk", 64),
          ("l2SecurityModeMixed", 128),
          ("l2SecurityModeMixedPsk", 256),
          ("l2SecurityModeWai", 512),
          ("l2SecurityModeWaiPsk", 1024),
          ("l2SecurityModeAll", 2047))
    )


class MwlL2SecurityMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2047)
        )
    )
    namedValues = NamedValues(
        *(("l2SecurityModeNone", 0),
          ("l2SecurityModeOpen", 1),
          ("l2SecurityMode8021x", 2),
          ("l2SecurityModeSwk", 4),
          ("l2SecurityModeWpa", 8),
          ("l2SecurityModeWpaPsk", 16),
          ("l2SecurityModeWpa2", 32),
          ("l2SecurityModeWpa2Psk", 64),
          ("l2SecurityModeMixed", 128),
          ("l2SecurityModeMixedPsk", 256),
          ("l2SecurityModeWai", 512),
          ("l2SecurityModeWaiPsk", 1024),
          ("l2SecurityModeAll", 2047))
    )



class MwlTunnelTerminationModeBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tunnelTerminationNone", 0),
          ("tunnelTerminationPeap", 1),
          ("tunnelTerminationTtls", 2))
    )


class MwlL2SecurityDetailMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              511,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("stationSecurityModeNone", 0),
          ("stationSecurityModeOpen", 1),
          ("stationSecurityMode8021x", 2),
          ("stationSecurityModeSwk", 4),
          ("stationSecurityModeWpa", 8),
          ("stationSecurityModeWpaPsk", 16),
          ("stationSecurityModeWpa2", 32),
          ("stationSecurityModeWpa2Psk", 64),
          ("stationSecurityModeMixed", 128),
          ("stationSecurityModeMixedPsk", 256),
          ("stationSecurityModeAll", 511),
          ("stationSecurityMode8021xInProgress", 512),
          ("stationSecurityModeWpaInProgress", 1024),
          ("stationSecurityModeWpaPskInProgress", 2048),
          ("stationSecurityModeWpa2InProgress", 4096),
          ("stationSecurityModeWpa2PskInProgress", 8192),
          ("stationSecurityModeMixedInProgress", 16384),
          ("stationSecurityModeMixedPskInProgress", 32768))
    )



class MwlL3SecurityMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("l3SecurityModeOpen", 1),
          ("l3SecurityModeVpn", 2),
          ("l3SecurityModeWebauth", 4),
          ("l3SecurityModeAll", 7))
    )



class MwlCaptivePortalMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortalDisabled", 0),
          ("captivePortalModeVpn", 1),
          ("captivePortalModeWebauth", 2),
          ("captivePortalModeAll", 3))
    )



class MwlCaptivePortalAuthState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("captivePortalStateClear", 0),
          ("captivePortalStateWebauth", 1))
    )



class MwlCaptivePortalAuthMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("captivePortalAuthMethodInternal", 0),
          ("captivePortalAuthMethodExternal", 1))
    )



class MwlSnmpPrivilege(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpRo", 1),
          ("snmpRw", 2))
    )



class MwlSnmpV3AuthProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpV3UsmNoAuth", 0),
          ("snmpV3UsmHmacMd5Auth", 1),
          ("snmpV3UsmHmacShaAuth", 2))
    )



class MwlSnmpV3PrivProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("snmpV3UsmNoPriv", 0),
          ("snmpV3UsmDesPriv", 1))
    )



class MwlTransmitRateBGBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bgtransmitRateNotSupported", 0),
          ("bgtransmitRate1", 1),
          ("bgtransmitRate2", 2),
          ("bgtransmitRate55", 4),
          ("bgtransmitRate11", 8),
          ("bgtransmitRate6", 16),
          ("bgtransmitRate9", 32),
          ("bgtransmitRate12", 64),
          ("bgtransmitRate18", 128),
          ("bgtransmitRate22", 256),
          ("bgtransmitRate24", 512),
          ("bgtransmitRate33", 1024),
          ("bgtransmitRate36", 2048),
          ("bgtransmitRate48", 4096),
          ("bgtransmitRate54", 8192))
    )


class MwlTransmitRateBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("transmitRateNotSupported", 0),
          ("transmitRate1", 1),
          ("transmitRate2", 2),
          ("transmitRate55", 4),
          ("transmitRate11", 8))
    )


class MwlTransmitRateAGBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("agtransmitRateNotSupported", 0),
          ("agtransmitRate6", 16),
          ("agtransmitRate9", 32),
          ("agtransmitRate12", 64),
          ("agtransmitRate18", 128),
          ("agtransmitRate22", 256),
          ("agtransmitRate24", 512),
          ("agtransmitRate33", 1024),
          ("agtransmitRate36", 2048),
          ("agtransmitRate48", 4096),
          ("agtransmitRate54", 8192))
    )


class MwlTransmitRateHTBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("httransmitRateNotSupported", 0),
          ("httransmitRate0", 1),
          ("httransmitRate1", 2),
          ("httransmitRate2", 4),
          ("httransmitRate3", 8),
          ("httransmitRate4", 16),
          ("httransmitRate5", 32),
          ("httransmitRate6", 64),
          ("httransmitRate7", 128),
          ("httransmitRate8", 256),
          ("httransmitRate9", 512),
          ("httransmitRate10", 1024),
          ("httransmitRate11", 2048),
          ("httransmitRate12", 4096),
          ("httransmitRate13", 8192),
          ("httransmitRate14", 16384),
          ("httransmitRate15", 32768),
          ("httransmitRate16", 65536),
          ("httransmitRate17", 131072),
          ("httransmitRate18", 262144),
          ("httransmitRate19", 524288),
          ("httransmitRate20", 1048576),
          ("httransmitRate21", 2097152),
          ("httransmitRate22", 4194304),
          ("httransmitRate23", 8388608),
          ("httransmitRate24", 16777216),
          ("httransmitRate25", 33554432),
          ("httransmitRate26", 67108864),
          ("httransmitRate27", 134217728),
          ("httransmitRate28", 268435456),
          ("httransmitRate29", 536870912),
          ("httransmitRate30", 1073741824),
          ("httransmitRate31", 2147483648))
    )


class MwlTransmitRateVHT(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acTransmitRateMcs07", 0),
          ("acTransmitRateMcs08", 1),
          ("acTransmitRateMcs09", 2),
          ("acTransmitRateNone", 3))
    )



class MwlUpgradeState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("upgradeStart", 1),
          ("upgradeInProgress", 2),
          ("upgradeFailed", 3),
          ("upgradeDone", 4))
    )



class MwlVlanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vlanNone", 0),
          ("vlanDefaultOnly", 1),
          ("vlanRadiusOnly", 2),
          ("vlanRadiusAndDefault", 3),
          ("vlanGre", 4),
          ("vlanPool", 5))
    )



class MwlAirFirewall(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("airfirewallNone", 0),
          ("airfirewallOuis", 1))
    )



class MwlOffHours(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offhoursNone", 0),
          ("offhours", 1))
    )



class MwlOffHoursService(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offhoursNoservice", 0),
          ("offhoursNowireless", 1))
    )



class MwlDailyOutOfService(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDailyOutOfService", 0),
          ("dailyOutOfServiceOff", 1),
          ("dailyOutOfServiceOn", 2))
    )



class MwlVpnStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clearActive", 0),
          ("vpnBypass", 1),
          ("vpnActive", 2),
          ("webAuthActive", 4),
          ("vpnWebActive", 5))
    )



class MwlVpnDetailStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("stationClearActive", 0),
          ("stationVpnBypass", 1),
          ("stationVpnActive", 2),
          ("stationWebAuthActive", 4),
          ("stationVpnWebActive", 5),
          ("stationVpnInProgress", 8),
          ("stationWebauthInProgress", 16),
          ("stationVpnWebauthInProgress", 32))
    )



class MwlSslUsrAuthProtocolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sslAuthProtocolUnknown", 0),
          ("sslAuthProtocolNone", 1),
          ("sslAuthProtocolChap", 2))
    )



class MwlDhGroupType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dhGroup2", 2),
          ("dhGroup3", 3),
          ("dhGroup4", 4),
          ("dhGroup5", 5))
    )



class MwlIpSecModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipsecUnknownMode", 0),
          ("ipsecTunnelMode", 1))
    )



class MwlIpSecDataChannelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipsecUnknown", 0),
          ("ipsecEsp", 1))
    )



class MwlIpEncryptionAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encryptionUnknownAlgorithm", 0),
          ("encryption3des", 1))
    )



class MwlIpAuthenticateAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authUnknown", 0),
          ("authPreShareKey", 1))
    )



class MwlIpHashAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hashUnknown", 0),
          ("hashSha", 1),
          ("hashMd5", 2))
    )



class MwlIpSecAuthAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipsecAuthUnknown", 0),
          ("ipsecAuthShaHmac", 1),
          ("ipsecAuthMd5Hmac", 2))
    )



class MwlCertFileType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("certUnknownType", 0),
          ("certPemType", 1),
          ("certPfxType", 2))
    )



class MwlUrlType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cliBadUrl", 0),
          ("cliFtpUrl", 1),
          ("cliTftpUrl", 2),
          ("cliSftpUrl", 3),
          ("cliHttpUrl", 4),
          ("cliHttpsUrl", 5),
          ("cliScpUrl", 6),
          ("cliFileUrl", 7))
    )



class MwlCertificateFormType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsShortForm", 0),
          ("nmsLongForm", 1))
    )



class MwlRadiusServerSelect(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsRadiusServerNone", 0),
          ("nmsRadiusServerPrimary", 1),
          ("nmsRadiusServerSecondary", 2),
          ("nmsRadiusServerAll", 3))
    )



class MwlDiscoveryOrder(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discoveryFromL2First", 0),
          ("discoveryFromL2Only", 1),
          ("discoveryFromL3First", 2),
          ("discoveryFromL3Only", 3))
    )



class MwlApDiscoveryState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDiscoveryLayer", 0),
          ("discoveryFromL2", 1),
          ("discoveryFromL3", 2))
    )



class MwlLicenseType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("featureTrial", 0),
          ("featurePermanent", 1))
    )



class MwlLicenseReserveType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("countedLicense", 0),
          ("uncountedLicense", 1))
    )



class MwlSofwFeatureType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sofwControllerBasic", 0),
          ("sofwApBasic", 1),
          ("sofwFeatMax", 2))
    )



class MwlSofwControllerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sofwAll", 0),
          ("sofwController", 1),
          ("sofwStdbyController", 2))
    )



class MwlDscpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              8,
              10,
              12,
              14,
              16,
              18,
              20,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              46,
              48,
              56)
        )
    )
    namedValues = NamedValues(
        *(("dscpDisabled", -1),
          ("dscpCs0", 0),
          ("dscpCs1", 8),
          ("dscpAf11", 10),
          ("dscpAf12", 12),
          ("dscpAf13", 14),
          ("dscpCs2", 16),
          ("dscpAf21", 18),
          ("dscpAf22", 20),
          ("dscpAf23", 22),
          ("dscpCs3", 24),
          ("dscpAf31", 26),
          ("dscpAf32", 28),
          ("dscpAf33", 30),
          ("dscpCs4", 32),
          ("dscpAf41", 34),
          ("dscpAf42", 36),
          ("dscpAf43", 38),
          ("dscpCs5", 40),
          ("dscpEfphb", 46),
          ("dscpCs6", 48),
          ("dscpCs7", 56))
    )



class MwlControllerHwType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              11,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("wncUnknownModel", 0),
          ("wncDevelPc", 1),
          ("wncMc1000", 2),
          ("wncMc1100", 3),
          ("wncMc3000", 4),
          ("wncMc500", 5),
          ("wncMc500a", 6),
          ("wncMc5000", 7),
          ("wncMc4000", 8),
          ("wncMc4100", 9),
          ("wncMc1500", 11),
          ("wncMc3200", 13),
          ("wncMc4200", 14),
          ("wncMc6000", 15),
          ("wncMc1500v", 16),
          ("wncMc3200v", 17),
          ("wncMc4200v", 18),
          ("wncMc1550", 19),
          ("wncMc1550v", 20),
          ("wncFwc50d", 21),
          ("wncFwc2hd", 22),
          ("wncFwc5hd", 23))
    )



class MwlWncControllerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wncStandalone", 0),
          ("wncMaster", 1),
          ("wncSlave", 2),
          ("wncCluster", 3))
    )



class MwlApHwType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              12,
              13,
              14,
              15,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52)
        )
    )
    namedValues = NamedValues(
        *(("apUnknownModel", 0),
          ("ap300", 12),
          ("ap310", 13),
          ("ap311", 14),
          ("ap320", 15),
          ("ap301", 18),
          ("ap302", 19),
          ("ap301i", 20),
          ("ap310i", 21),
          ("ap302i", 22),
          ("ap320i", 23),
          ("ap1010", 24),
          ("ap1020", 25),
          ("psm3x", 26),
          ("ap400", 27),
          ("ap433e", 28),
          ("ap433i", 29),
          ("ap432e", 30),
          ("ap432i", 31),
          ("ap1010e", 32),
          ("ap1020e", 33),
          ("ap433is", 34),
          ("ap433es", 35),
          ("oap432e", 36),
          ("oap433e", 37),
          ("oap433es", 38),
          ("ap110", 39),
          ("ap120", 40),
          ("ap1014i", 41),
          ("ap332e", 42),
          ("ap332i", 43),
          ("ap832e", 44),
          ("ap832i", 45),
          ("ap822e", 46),
          ("ap822i", 47),
          ("ap122", 48),
          ("oap832e", 49),
          ("fap421evi", 50),
          ("fap423eve", 51),
          ("ofap422ev", 52))
    )



class MwlApRegulatoryType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ap1000RegIndex", 1),
          ("ap300Mb72RegIndex", 2),
          ("ap300Mb82RegIndex", 3),
          ("ap400RegIndex", 4),
          ("ap110RegIndex", 5),
          ("ap330RegIndex", 6),
          ("ap800RegIndex", 7),
          ("ap800bRegIndex", 8),
          ("ap122RegIndex", 9),
          ("oap800RegIndex", 10),
          ("fap421RegIndex", 11),
          ("fap423RegIndex", 12),
          ("ofap422RegIndex", 13))
    )



class MwlApRfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("apRfUnknownModel", 0),
          ("apRf1", 1),
          ("apRf2", 2),
          ("apRf3", 3),
          ("apRf4", 4),
          ("apRf5", 5),
          ("apRf6", 6),
          ("apRf7", 7),
          ("apRf8", 8),
          ("apRf9", 9),
          ("apRf10", 10),
          ("apRf11", 11),
          ("apRf12", 12),
          ("apRf13", 13),
          ("apRf14", 14),
          ("apRf15", 15),
          ("apRf16", 16),
          ("apRf17", 17),
          ("apRf18", 18),
          ("apRf19", 19),
          ("apRf20", 20),
          ("apRf21", 21),
          ("apRf22", 22))
    )



class MwlApIfModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("apModeUnknown", 0),
          ("apBMode", 1),
          ("apAMode", 2),
          ("apAbMode", 3),
          ("apGMode", 4),
          ("apBgMode", 5),
          ("apAgMode", 6),
          ("apAbgMode", 7),
          ("apNMode", 8),
          ("apBnMode", 9),
          ("apAnMode", 10),
          ("apAbnMode", 11),
          ("apGnMode", 12),
          ("apBgnMode", 13),
          ("apAgnMode", 14),
          ("apAbgnMode", 15),
          ("apAn1s20Mode", 16),
          ("apAn1s40Mode", 17),
          ("apAn2s20Mode", 18),
          ("apAn2s40Mode", 19),
          ("apAn3s20Mode", 20),
          ("apAn3s40Mode", 21),
          ("apBgn1s20Mode", 22),
          ("apBgn1s40Mode", 23),
          ("apBgn2s20Mode", 24),
          ("apBgn2s40Mode", 25),
          ("apBgn3s20Mode", 26),
          ("apBgn3s40Mode", 27),
          ("apAc1s20Mode", 28),
          ("apAc1s40Mode", 29),
          ("apAc1s80Mode", 30),
          ("apAbgnAcMode", 31),
          ("apAc2s20Mode", 32),
          ("apAc2s40Mode", 33),
          ("apAc2s80Mode", 34),
          ("apAc3s20Mode", 35),
          ("apAc3s40Mode", 36),
          ("apAc3s80Mode", 37),
          ("apAnAcMode", 38),
          ("apAn4s20Mode", 39),
          ("apAn4s40Mode", 40),
          ("apBgn4s20Mode", 41),
          ("apBgn4s40Mode", 42),
          ("apAc4s20Mode", 43),
          ("apAc4s40Mode", 44),
          ("apAc4s80Mode", 45))
    )



class MwlApIfConfigModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              10,
              13,
              18)
        )
    )
    namedValues = NamedValues(
        *(("apConfigModeUnknown", 0),
          ("apConfigBMode", 1),
          ("apConfigAMode", 2),
          ("apConfigGMode", 4),
          ("apConfigBgMode", 5),
          ("apConfigAnMode", 10),
          ("apConfigBgnMode", 13),
          ("apConfigAcMode", 18))
    )



class MwlAntennaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("antennaConnNone", 0),
          ("antennaConn24g", 1),
          ("antennaConn5g", 2),
          ("antennaConnDual", 3),
          ("antennaConnExt", 4),
          ("antennaConnInt", 5))
    )



class MwlBandType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfband24g", 1),
          ("rfband5g", 2))
    )



class MwlChannelBandType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("channelBMode", 1),
          ("channelAMode", 2),
          ("channelGMode", 3),
          ("channelBgMode", 4),
          ("channelAbgnMode20mhz", 5),
          ("channelAbgnMode40mhzAbove", 6),
          ("channelAbgnMode40mhzBelow", 7),
          ("channelNMode20mhz", 8),
          ("channelNMode40mhzAbove", 9),
          ("channelNMode40mhzBelow", 10),
          ("channelAcMode", 11))
    )



class MwlAntennaSetLocation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("antennaSetLocUnknown", 0),
          ("antennaSetLocLeft", 1),
          ("antennaSetLocRight", 2),
          ("antennaSetLoc1", 4),
          ("antennaSetLoc2", 8),
          ("antennaSetLoc3", 16),
          ("antennaSetLoc4", 32),
          ("antennaSetLoc5", 64),
          ("antennaSetLoc6", 128),
          ("antennaSetLoc7", 256),
          ("antennaSetLoc8", 512),
          ("antennaSetLoc9", 1024),
          ("antennaSetLocIntegrated", 2048),
          ("antennaSetLocInternal", 4096))
    )



class MwlIfDataRateOptionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dataRateManual", 0),
          ("dataRateAuto", 1))
    )



class MwlAntennaLinkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("antennaLinkUnknown", 0),
          ("antennaLinkPmp", 1),
          ("antennaLinkPtp", 2))
    )



class MwlDuplexModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsDuplexFull", 0),
          ("nmsDuplexHalf", 1))
    )



class MwlBgProtectionModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bgProtectionAuto", 0),
          ("bgProtectionOn", 1),
          ("bgProtectionOff", 2))
    )



class MwlHtProtectionModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("htProtectionAuto", 0),
          ("htProtectionOn", 1),
          ("htProtectionOff", 2))
    )



class MwlIpProxyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsGeneric", 0),
          ("nmsIpPathFinder", 1),
          ("nmsEnumerationHeader", 2))
    )



class MwlFirewallCapability(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firewallNone", 0),
          ("firewallConfigured", 1),
          ("firewallRadiusConfigured", 2))
    )



class MwlSecurityLogging(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("securityloggingOff", 0),
          ("securityloggingAllow", 1),
          ("securityloggingDeny", 2),
          ("securityloggingAll", 3))
    )



class MwlPMKcachingBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pmkCachingDisabled", 0),
          ("pmkCachingEnabled", 1))
    )


class MwlKDDI(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kddiDisabled", 0),
          ("kddiEnabled", 1))
    )



class MwlVcellType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsVcellPap", 0),
          ("nmsVcellVcell", 1))
    )



class MwlFilterModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1))
    )



class MwlBgRadioMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("virtualMode", 1),
          ("nonVirtualMode", 2))
    )



class MwlThrdPartyIdsIps(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("thrdPidsIpsSnortWireless", 1),
          ("thrdPidsIpsNone", 2))
    )



class MwlQosRulesMatchClassBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("qosrulesmatchclassOff", 0),
          ("qosrulesmatchclassOn", 1))
    )


class MwlQosRulesMatchClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosrulesmatchclassOff", 0),
          ("qosrulesmatchclassOn", 1))
    )



class MwlChannelWidth(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("channelWidth20", 1),
          ("channelWidth40Above", 2),
          ("channelWidth40Below", 3),
          ("channelWidth80", 4))
    )



class MwlBonding(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bondingSingle", 0),
          ("bondingDual", 1),
          ("bondingNone", 2))
    )



class MwlConnectivityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsDisconnected", 0),
          ("nmsConnected", 1))
    )



class MwlCapabilityModeBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("nmsStaCapabilityNone", 0),
          ("nmsStaWmmMode", 1),
          ("nmsStaApsdMode", 2),
          ("nmsSta80211RMode", 4),
          ("nmsSta80211KMode", 8),
          ("nmsSta80211UMode", 16),
          ("nmsSta80211VMode", 32),
          ("nmsSta80211WMode", 64))
    )


class MwlClientType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsClientData", 1),
          ("nmsClientSipPhone", 2))
    )



class MwlDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsStationWireless", 0),
          ("nmsStationWired", 1))
    )



class MwlStationState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nmsStationStateUnknown", 0),
          ("nmsStationStateInit", 1),
          ("nmsStationStateVlan", 2),
          ("nmsStationStateAssign", 3),
          ("nmsStationStateAssociated", 4),
          ("nmsStationState8021x", 5),
          ("nmsStationStateKey", 6),
          ("nmsStationStateIpDiscover", 7),
          ("nmsStationStateCaptivePortal", 8),
          ("nmsStationStateDisassociated", 9))
    )



class MwlStaDiagStap(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("staMacFilterAclCnt", 1),
          ("staMacFilterAclFailCnt", 2),
          ("staWepKeyIndexMismatchCnt", 3),
          ("staAssignFailCnt", 4),
          ("staAssociationCnt", 5),
          ("staKeyExchangeCnt", 6),
          ("staKeyExchangeFailCnt", 7),
          ("staMicFailCnt", 8),
          ("staIpDiscoveryCnt", 9),
          ("staRadiusAuthCnt", 10),
          ("staRadiusAuthFailCnt", 11),
          ("staCpGuestUserAuthCnt", 12),
          ("staCpGuestUserFailCnt", 13),
          ("staDecryptFailCnt", 14),
          ("staSoftHandoffCnt", 15))
    )



class MwlEnableDisableOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsDisable", 0),
          ("nmsEnable", 1))
    )



class MwlSourceEnableDisableOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsSourceEnable", 1),
          ("nmsSourceDisable", 2))
    )



class MwlLocationSourceOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmsLocationSourceWifi", 1),
          ("nmsLocationSourceBle", 2),
          ("nmsLocationSourceAll", 3))
    )



class MwlReportFormatType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsReportFormatFortiPresence", 1),
          ("nmsReportFormatLegacy", 2))
    )



class MwlPacketCaptureMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("l2Mode", 0),
          ("l3Mode", 1))
    )



class MwlRxTxOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxOnly", 0),
          ("txOnly", 1),
          ("rxTxBoth", 2))
    )



class MwlRateLimitMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("station", 0),
          ("cumulative", 1))
    )



class MwlBandSteeringMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandSteeringDisable", 0),
          ("bandASteering", 1),
          ("bandNSteering", 2))
    )



class MwlPapBroadcastSsidMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("papBroadcastSsidDisabled", 0),
          ("papBroadcastSsidAlways", 1),
          ("papBroadcastSsidTillAssociation", 2))
    )



class MwlEncapsulationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ppi", 0),
          ("legacy", 1))
    )



class MwlUplinkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsUplink", 0),
          ("nmsDownlink", 1),
          ("nmsUplinkLacp", 2))
    )



class MwlVpnConnectivityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpnDisconnected", 0),
          ("vpnConnected", 1))
    )



class MwlVpnAuthenticationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vpnUnknown", 0),
          ("vpnNoCertificate", 1),
          ("vpnValidCertificate", 2),
          ("vpnInvalidCertificate", 3),
          ("vpnCertificateRevoked", 4),
          ("vpnCertificateExpired", 5),
          ("vpnCertificateUnknownCa", 6))
    )



class MwlVpnAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpnAuthTypeUnknown", 0),
          ("vpnAuthTypeX509Certificate", 1))
    )



class MwlCertificateStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("certStatusUnknown", 0),
          ("certStatusNotInstalled", 1),
          ("certStatusInstalled", 2))
    )



class MwlCertRequestStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("certReqStatusNone", 0),
          ("certReqStatusCsrGenerated", 1),
          ("certReqStatusCsrGenerationInProgress", 2),
          ("certReqStatusCsrGenerationFailed", 3),
          ("certReqStatusCsrUploadFailed", 4),
          ("certReqStatusCertInstalled", 5),
          ("certReqStatusCertInstallationInProgress", 6),
          ("certReqStatusCertDownloadFailed", 7),
          ("certReqStatusCertInstallationFailed", 8),
          ("certReqStatusCertDeleted", 9),
          ("certReqStatusCertDeletionInProgress", 10),
          ("certReqStatusCertDeletionFailed", 11),
          ("certReqStatusCaCertDownloaded", 12),
          ("certReqStatusCaCertDownloadInProgress", 13),
          ("certReqStatusCaCertDownloadFailed", 14))
    )



class MwlFastEthernetType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsPrimaryFastethernet", 1),
          ("nmsSecondaryFastethernet", 2))
    )



class MwlVpnMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("modeNonVpn", 0),
          ("modeVpn", 1))
    )



class MwlRegionSettings(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regionUnknown", 0),
          ("regionUs", 1),
          ("regionIntl", 2))
    )



class MwlSpectrumBandsBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("spectrumSubbandNone", 0),
          ("spectrumSubband24ghz", 1),
          ("spectrumSubband5ghzLow", 2),
          ("spectrumSubband5ghzMedium", 4),
          ("spectrumSubband5ghzHigh", 8))
    )


class MwlESSRFVirtualizationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("essRfVmodeVcell", 0),
          ("essRfVmodeVport", 1),
          ("essRfVmodeNcell", 2))
    )



class MwlIFRFVirtualizationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ifRfVmodeVport", 0),
          ("ifRfVmodeNcell", 1))
    )



class MwlYesNoSwitch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsNo", 0),
          ("nmsYes", 1))
    )



class MwlIpMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeUnknown", 0),
          ("modeIpv4", 1),
          ("modeIpv6", 2),
          ("modeDualStackIp", 3))
    )



class MwlChannelCenterFrequency(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              42,
              58,
              106,
              122,
              155)
        )
    )
    namedValues = NamedValues(
        *(("channelCenterFrequency0", 0),
          ("channelCenterFrequency42", 42),
          ("channelCenterFrequency58", 58),
          ("channelCenterFrequency106", 106),
          ("channelCenterFrequency122", 122),
          ("channelCenterFrequency155", 155))
    )



class MwlNetworkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkTypeWired", 0),
          ("networkTypeWireless", 1))
    )



class MwlIpv6AddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 0),
          ("globalUnicastAddr", 1),
          ("globalUnicastDhcpAddr", 2),
          ("linkLocalAddr", 3),
          ("tempAddr", 4))
    )



class MwlvenueGroup(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("venueGroupUnspecified", 0),
          ("venueGroupAssembly", 1),
          ("venueGroupBusiness", 2),
          ("venueGroupEducational", 3),
          ("venueGroupFactoryIndustrial", 4),
          ("venueGroupInstitutional", 5),
          ("venueGroupMercantile", 6),
          ("venueGroupResidential", 7),
          ("venueGroupStorage", 8),
          ("venueGroupUtilityMiscellaneous", 9),
          ("venueGroupVehicular", 10),
          ("venueGroupOutdoor", 11))
    )



class MwlvenueType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              201,
              202,
              203,
              204,
              206,
              207,
              208,
              209,
              301,
              302,
              303,
              401,
              501,
              502,
              503,
              504,
              505,
              601,
              602,
              603,
              604,
              605,
              701,
              702,
              703,
              704,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106)
        )
    )
    namedValues = NamedValues(
        *(("venueGroupTypeUnspecified", 0),
          ("venueTypeAssemblyArena", 101),
          ("venueTypeAssemblyStadium", 102),
          ("venueTypeAssemblyPassengerTerminal", 103),
          ("venueTypeAssemblyAmphitheater", 104),
          ("venueTypeAssemblyAmusementPark", 105),
          ("venueTypeAssemblyPlaceOfWorship", 106),
          ("venueTypeAssemblyConventionCenter", 107),
          ("venueTypeAssemblyLibrary", 108),
          ("venueTypeAssemblyMuseum", 109),
          ("venueTypeAssemblyRestaurant", 110),
          ("venueTypeAssemblyTheater", 111),
          ("venueTypeAssemblyBar", 112),
          ("venueTypeAssemblyCoffeeShop", 113),
          ("venueTypeAssemblyZooAquarium", 114),
          ("venueTypeAssemblyEmergencyCoordinationCenter", 115),
          ("venueTypeBusinessDoctorDentistOffice", 201),
          ("venueTypeBusinessBank", 202),
          ("venueTypeBusinessFireStation", 203),
          ("venueTypeBusinessPoliceStation", 204),
          ("venueTypeBusinessPostOffice", 206),
          ("venueTypeBusinessProfessionalOffice", 207),
          ("venueTypeBusinessResearchDevelopmentFacility", 208),
          ("venueTypeBusinessAttorneyOffice", 209),
          ("venueTypeEducationalSchoolPrimary", 301),
          ("venueTypeEducationalSchoolSecondary", 302),
          ("venueTypeEducationalUniversityCollege", 303),
          ("venueTypeFactoryIndustrialFactory", 401),
          ("venueTypeInstitutionalHospital", 501),
          ("venueTypeInstitutionalLongTermCareFacility", 502),
          ("venueTypeInstitutionalAlcoholDrugRehabilitationCenter", 503),
          ("venueTypeInstitutionalGroupHome", 504),
          ("venueTypeInstitutionalPrisonJail", 505),
          ("venueTypeMercantileRetailStore", 601),
          ("venueTypeMercantileGroceryMarket", 602),
          ("venueTypeMercantileAutomotiveServiceStation", 603),
          ("venueTypeMercantileShoppingMall", 604),
          ("venueTypeMercantileGasStation", 605),
          ("venueTypeResidentialPrivateResidence", 701),
          ("venueTypeResidentialHotelMotel", 702),
          ("venueTypeResidentialDormitory", 703),
          ("venueTypeResidentialBoardingHouse", 704),
          ("venueTypeVehicularAutomobileTruck", 1001),
          ("venueTypeVehicularAirplane", 1002),
          ("venueTypeVehicularBus", 1003),
          ("venueTypeVehicularFerry", 1004),
          ("venueTypeVehicularShipBoat", 1005),
          ("venueTypeVehicularTrain", 1006),
          ("venueTypeVehicularMortorBike", 1007),
          ("venueTypeOutdoorMuniMesh", 1101),
          ("venueTypeOutdoorCityPark", 1102),
          ("venueTypeOutdoorRestArea", 1103),
          ("venueTypeOutdoorTrafficControl", 1104),
          ("venueTypeOutdoorBusStop", 1105),
          ("venueTypeOutdoorKiosk", 1106))
    )



class MwlHotspotAccessNetworkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("hotspotAccessNetworkTypePrivateNetwork", 0),
          ("hotspotAccessNetworkTypePrivateNetworkWithGuestAccess", 1),
          ("hotspotAccessNetworkTypeChargeablePublicNetwork", 2),
          ("hotspotAccessNetworkTypeFreePublicNetwork", 3),
          ("hotspotAccessNetworkTypePersonalDeviceNetwork", 4),
          ("hotspotAccessNetworkTypeEmergencyServicesOnlyNetwork", 5),
          ("hotspotAccessNetworkTypeTestExperimentalNetwork", 14),
          ("hotspotAccessNetworkTypeWildcardNetwork", 15))
    )



class MwlHotspotAuthenType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotspotAuthenTypeAcceptanceTermsConditions", 0),
          ("hotspotAuthenTypeOnlineEnrollmentSupported", 1),
          ("hotspotAuthenTypeHttpHttpsRedirection", 2),
          ("hotspotAuthenTypeDnsRedirection", 3))
    )



class MwlIPv6AvailabilityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv6AvailabilityTypeNotAvailable", 0),
          ("ipv6AvailabilityTypeAvailable", 1),
          ("ipv6AvailabilityTypeNotKnown", 2))
    )



class MwlIPv4AvailabilityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipv4AvailabilityTypeNotAvailable", 0),
          ("ipv4AvailabilityTypeAvailable", 1),
          ("ipv4AvailabilityTypePortRestrictedAddressAvailable", 2),
          ("ipv4AvailabilityTypeSingleNatedPrivateAddressAvailable", 3),
          ("ipv4AvailabilityTypeDoubleNatedPrivateAddressAvailable", 4),
          ("ipv4AvailabilityTypePortRestrictedSingleNatedPrivateAddressAvailable", 5),
          ("ipv4AvailabilityTypePortRestrictedDoubleNatedPrivateAddressAvailable", 6),
          ("ipv4AvailabilityTypeNotKnown", 7))
    )



class MwlNAIRealmAuthMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("naiRealmAuthMethodEapTlsCertificate", 0),
          ("naiRealmAuthMethodEapTtlsMschapv2UsernamePassword", 1))
    )



class MwlApGroupType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("apGroupTypeLocation", 0)
    )



class MwlVpnClientProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpnClientProtoTcp", 0),
          ("vpnClientProtoUdp", 1))
    )



class MwlRadiusCalledStationIdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radiusCalledStationIdTypeDefault", 0),
          ("radiusCalledStationIdTypeMacAddress", 1),
          ("radiusCalledStationIdTypeMacAddressSsid", 2))
    )



class MwlServiceDataFeature(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("serviceDataServiceConnect", 0),
          ("serviceDataApplicationVisibility", 1))
    )



class MwlServiceDataType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("serviceDataServiceConnectService", 0),
          ("serviceDataServiceConnectLocation", 1),
          ("serviceDataServiceConnectEssidVlan", 2),
          ("serviceDataServiceConnectNetwork", 3),
          ("serviceDataAppVisibilityApplication", 4),
          ("serviceDataAppVisibilityEssid", 5),
          ("serviceDataAppVisibilityStation", 6),
          ("serviceDataAppVisibilityAp", 7))
    )



class MwlServiceDataFilterType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("serviceDataFilterEssid", 0),
          ("serviceDataFilterAp", 1),
          ("serviceDataFilterLocation", 2),
          ("serviceDataFilterEssidAp", 3),
          ("serviceDataFilterEssidLocation", 4))
    )



class MwlRedirectionProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("redirectionProtocolHttps", 0),
          ("redirectionProtocolHttp", 1))
    )



class MwlApRebootReasonCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("apRebootReasonCodeInvalid", 0),
          ("apRebootReasonCodeManual", 1),
          ("apRebootReasonCodeConfigChange", 2),
          ("apRebootReasonCodeWatchdog", 3),
          ("apRebootReasonCodeLostConnection", 4),
          ("apRebootReasonCodeSoftwareUpgrade", 5),
          ("apRebootReasonCodeRadioFailure", 6),
          ("apRebootReasonCodeInvalidPower", 7),
          ("apRebootReasonCodeUnknown", 8),
          ("apRebootReasonCodeCannotDownloadConfig", 9),
          ("apRebootReasonCodeRestoreDefault", 10),
          ("apRebootReasonCodeApCrash", 11),
          ("apRebootReasonCodeKernelCrash", 12),
          ("apRebootReasonCodeSoftLockup", 13),
          ("apRebootReasonCodeBandspeedTerminated", 14),
          ("apRebootReasonCodeLastEntry", 15))
    )



class MwlBridgedVlanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noVlan", 0),
          ("staticVlanOnly", 1),
          ("radiusVlanOnly", 2),
          ("radiusAndStaticVlan", 3))
    )



class MwlCliCmdGenWriteMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cliCmdGenWriteModeOverwrite", 0),
          ("cliCmdGenWriteModeAppend", 1))
    )



class MwlVoiceClientType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voiceClientTypeNone", 0),
          ("voiceClientTypeAscom", 1),
          ("voiceClientTypeSpectralink", 2))
    )



class MwlMMProtocolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mmpTypeBinary", 0),
          ("mmpTypeKv", 1))
    )



class MwlApMacAssignOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsEth0", 0),
          ("nmsEth1", 1))
    )



class MwlNplus1NotifType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nplus1NotifTypeNp1Stop", 1),
          ("nplus1NotifTypeReboot", 2),
          ("nplus1NotifTypeUpgrade", 3),
          ("nplus1NotifTypeTakeover", 4),
          ("nplus1NotifTypeFallback", 5),
          ("nplus1NotifTypeIpConflict", 6),
          ("nplus1NotifTypeGatewayUp", 7),
          ("nplus1NotifTypeGatewayDown", 8),
          ("nplus1NotifTypeSlave", 9))
    )



class MwlTimerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("timerTypeAbsolute", 0),
          ("timerTypePeriodic", 1))
    )



class MwlApplicationActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appActionTypeAllow", 0),
          ("appActionTypeBlock", 1))
    )



class MwlAppVisibilityFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appVisibilityFlowTypeAllowed", 0),
          ("appVisibilityFlowTypeBlocked", 1))
    )



class MwlApplicationBWUnit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("appBwUnitKbps", 0),
          ("appBwUnitMbps", 1),
          ("appBwUnitGbps", 2))
    )



class MwlDaysOfTheWeekBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("daysOfTheWeekNotSupported", 0),
          ("daysOfTheWeekSunday", 1),
          ("daysOfTheWeekMonday", 2),
          ("daysOfTheWeekTuesday", 4),
          ("daysOfTheWeekWednesday", 8),
          ("daysOfTheWeekThursday", 16),
          ("daysOfTheWeekFriday", 32),
          ("daysOfTheWeekSaturday", 64))
    )


class MwlTimerIntervalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsTimerStateInInterval", 0),
          ("nmsTimerStateOutOfInterval", 1))
    )



class MwlEssIdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsEssidTypeRegular", 0),
          ("nmsEssidTypeBackup", 1))
    )



class MwlState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsStateUnknown", 0),
          ("nmsStateStart", 1),
          ("nmsStateDone", 2))
    )



class MwlTxBeamSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmsTxBeamformingDisabled", 0),
          ("nmsTxBeamformingSuMimo", 1),
          ("nmsTxBeamformingMuMimo", 2))
    )



class MwlMcaApStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nmsMcaUnplanned", 0),
          ("nmsMcaPlanned", 1))
    )



class MwlArrayDataTypeAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addValue", 1),
          ("deleteValue", 2),
          ("updateValue", 3))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-TC",
    **{"MwlAclEnvState": MwlAclEnvState,
       "MwlAddressAssignmentType": MwlAddressAssignmentType,
       "MwlAddressIfAssignmentType": MwlAddressIfAssignmentType,
       "MwlApIpAssignmentType": MwlApIpAssignmentType,
       "MwlAdministrativeState": MwlAdministrativeState,
       "MwlAdmissionControl": MwlAdmissionControl,
       "MwlAntennaSet": MwlAntennaSet,
       "MwlApAssignType": MwlApAssignType,
       "MwlApType": MwlApType,
       "MwlApIndoorOutdoorType": MwlApIndoorOutdoorType,
       "MwlApMode": MwlApMode,
       "MwlAuthenticationAlgorithm": MwlAuthenticationAlgorithm,
       "MwlAuthenticationType": MwlAuthenticationType,
       "MwlManagementFrameProtection": MwlManagementFrameProtection,
       "MwlCaptivePortalAuthenticationType": MwlCaptivePortalAuthenticationType,
       "MwlCaptivePortalExternalServerType": MwlCaptivePortalExternalServerType,
       "MwlCaptivePortalModeType": MwlCaptivePortalModeType,
       "MwlAuthSuiteBits": MwlAuthSuiteBits,
       "MwlActionStatus": MwlActionStatus,
       "MwlAlarmState": MwlAlarmState,
       "MwlNotificationType": MwlNotificationType,
       "MwlNotificationSeverity": MwlNotificationSeverity,
       "MwlAntenna": MwlAntenna,
       "MwlAssignmentAlgorithm": MwlAssignmentAlgorithm,
       "MwlAssociationState": MwlAssociationState,
       "MwlApAuthState": MwlApAuthState,
       "MwlAvailabilityStatus": MwlAvailabilityStatus,
       "MwlBeaconCoordinationMode": MwlBeaconCoordinationMode,
       "MwlBlock": MwlBlock,
       "MwlCoordAlgorithm": MwlCoordAlgorithm,
       "MwlCypherSuiteBits": MwlCypherSuiteBits,
       "MwlL2BridgingsBits": MwlL2BridgingsBits,
       "MwlACMSupportsBits": MwlACMSupportsBits,
       "MwlDropPolicy": MwlDropPolicy,
       "MwlDataplaneMode": MwlDataplaneMode,
       "MwlProfileOwner": MwlProfileOwner,
       "MwlApRole": MwlApRole,
       "MwlEncryptionAlgorithm": MwlEncryptionAlgorithm,
       "MwlIfAdministrativeState": MwlIfAdministrativeState,
       "MwlOperChanChangeReason": MwlOperChanChangeReason,
       "MwlOperStatusChangeReason": MwlOperStatusChangeReason,
       "MwlEssApAdminMode": MwlEssApAdminMode,
       "MwlLedMode": MwlLedMode,
       "MwlLogSeverity": MwlLogSeverity,
       "MwlLogType": MwlLogType,
       "MwlMimoMode": MwlMimoMode,
       "MwlNatType": MwlNatType,
       "MwlNetProtocol": MwlNetProtocol,
       "MwlNmsInterfaceType": MwlNmsInterfaceType,
       "MwlNodeRelationship": MwlNodeRelationship,
       "MwlNodeType": MwlNodeType,
       "MwlOperationalState": MwlOperationalState,
       "MwlPowerSupply": MwlPowerSupply,
       "MwlRadiusMacDelimiter": MwlRadiusMacDelimiter,
       "MwlRadiusPasswordType": MwlRadiusPasswordType,
       "MwlWlanOptimize": MwlWlanOptimize,
       "MwlOnOffSwitch": MwlOnOffSwitch,
       "MwlPublishEssId": MwlPublishEssId,
       "MwlAllOnSelectedSwitch": MwlAllOnSelectedSwitch,
       "MwlPrivacyBit": MwlPrivacyBit,
       "MwlQosAction": MwlQosAction,
       "MwlQosCodec": MwlQosCodec,
       "MwlQosProtocol": MwlQosProtocol,
       "MwlQosCodecProtocol": MwlQosCodecProtocol,
       "MwlQosCallState": MwlQosCallState,
       "MwlServiceAction": MwlServiceAction,
       "MwlSecurityPolicyAction": MwlSecurityPolicyAction,
       "MwlL2SecurityModeBits": MwlL2SecurityModeBits,
       "MwlL2SecurityMode": MwlL2SecurityMode,
       "MwlTunnelTerminationModeBits": MwlTunnelTerminationModeBits,
       "MwlL2SecurityDetailMode": MwlL2SecurityDetailMode,
       "MwlL3SecurityMode": MwlL3SecurityMode,
       "MwlCaptivePortalMode": MwlCaptivePortalMode,
       "MwlCaptivePortalAuthState": MwlCaptivePortalAuthState,
       "MwlCaptivePortalAuthMethod": MwlCaptivePortalAuthMethod,
       "MwlSnmpPrivilege": MwlSnmpPrivilege,
       "MwlSnmpV3AuthProtocol": MwlSnmpV3AuthProtocol,
       "MwlSnmpV3PrivProtocol": MwlSnmpV3PrivProtocol,
       "MwlTransmitRateBGBits": MwlTransmitRateBGBits,
       "MwlTransmitRateBits": MwlTransmitRateBits,
       "MwlTransmitRateAGBits": MwlTransmitRateAGBits,
       "MwlTransmitRateHTBits": MwlTransmitRateHTBits,
       "MwlTransmitRateVHT": MwlTransmitRateVHT,
       "MwlUpgradeState": MwlUpgradeState,
       "MwlVlanType": MwlVlanType,
       "MwlAirFirewall": MwlAirFirewall,
       "MwlOffHours": MwlOffHours,
       "MwlOffHoursService": MwlOffHoursService,
       "MwlDailyOutOfService": MwlDailyOutOfService,
       "MwlVpnStatus": MwlVpnStatus,
       "MwlVpnDetailStatus": MwlVpnDetailStatus,
       "MwlSslUsrAuthProtocolType": MwlSslUsrAuthProtocolType,
       "MwlDhGroupType": MwlDhGroupType,
       "MwlIpSecModeType": MwlIpSecModeType,
       "MwlIpSecDataChannelType": MwlIpSecDataChannelType,
       "MwlIpEncryptionAlgorithm": MwlIpEncryptionAlgorithm,
       "MwlIpAuthenticateAlgorithm": MwlIpAuthenticateAlgorithm,
       "MwlIpHashAlgorithm": MwlIpHashAlgorithm,
       "MwlIpSecAuthAlgorithm": MwlIpSecAuthAlgorithm,
       "MwlCertFileType": MwlCertFileType,
       "MwlUrlType": MwlUrlType,
       "MwlCertificateFormType": MwlCertificateFormType,
       "MwlRadiusServerSelect": MwlRadiusServerSelect,
       "MwlDiscoveryOrder": MwlDiscoveryOrder,
       "MwlApDiscoveryState": MwlApDiscoveryState,
       "MwlLicenseType": MwlLicenseType,
       "MwlLicenseReserveType": MwlLicenseReserveType,
       "MwlSofwFeatureType": MwlSofwFeatureType,
       "MwlSofwControllerType": MwlSofwControllerType,
       "MwlDscpType": MwlDscpType,
       "MwlControllerHwType": MwlControllerHwType,
       "MwlWncControllerState": MwlWncControllerState,
       "MwlApHwType": MwlApHwType,
       "MwlApRegulatoryType": MwlApRegulatoryType,
       "MwlApRfType": MwlApRfType,
       "MwlApIfModeType": MwlApIfModeType,
       "MwlApIfConfigModeType": MwlApIfConfigModeType,
       "MwlAntennaType": MwlAntennaType,
       "MwlBandType": MwlBandType,
       "MwlChannelBandType": MwlChannelBandType,
       "MwlAntennaSetLocation": MwlAntennaSetLocation,
       "MwlIfDataRateOptionType": MwlIfDataRateOptionType,
       "MwlAntennaLinkType": MwlAntennaLinkType,
       "MwlDuplexModeType": MwlDuplexModeType,
       "MwlBgProtectionModeType": MwlBgProtectionModeType,
       "MwlHtProtectionModeType": MwlHtProtectionModeType,
       "MwlIpProxyType": MwlIpProxyType,
       "MwlFirewallCapability": MwlFirewallCapability,
       "MwlSecurityLogging": MwlSecurityLogging,
       "MwlPMKcachingBits": MwlPMKcachingBits,
       "MwlKDDI": MwlKDDI,
       "MwlVcellType": MwlVcellType,
       "MwlFilterModeType": MwlFilterModeType,
       "MwlBgRadioMode": MwlBgRadioMode,
       "MwlThrdPartyIdsIps": MwlThrdPartyIdsIps,
       "MwlQosRulesMatchClassBits": MwlQosRulesMatchClassBits,
       "MwlQosRulesMatchClass": MwlQosRulesMatchClass,
       "MwlChannelWidth": MwlChannelWidth,
       "MwlBonding": MwlBonding,
       "MwlConnectivityStatus": MwlConnectivityStatus,
       "MwlCapabilityModeBits": MwlCapabilityModeBits,
       "MwlClientType": MwlClientType,
       "MwlDeviceType": MwlDeviceType,
       "MwlStationState": MwlStationState,
       "MwlStaDiagStap": MwlStaDiagStap,
       "MwlEnableDisableOption": MwlEnableDisableOption,
       "MwlSourceEnableDisableOption": MwlSourceEnableDisableOption,
       "MwlLocationSourceOption": MwlLocationSourceOption,
       "MwlReportFormatType": MwlReportFormatType,
       "MwlPacketCaptureMode": MwlPacketCaptureMode,
       "MwlRxTxOption": MwlRxTxOption,
       "MwlRateLimitMode": MwlRateLimitMode,
       "MwlBandSteeringMode": MwlBandSteeringMode,
       "MwlPapBroadcastSsidMode": MwlPapBroadcastSsidMode,
       "MwlEncapsulationType": MwlEncapsulationType,
       "MwlUplinkType": MwlUplinkType,
       "MwlVpnConnectivityStatus": MwlVpnConnectivityStatus,
       "MwlVpnAuthenticationStatus": MwlVpnAuthenticationStatus,
       "MwlVpnAuthenticationType": MwlVpnAuthenticationType,
       "MwlCertificateStatus": MwlCertificateStatus,
       "MwlCertRequestStatus": MwlCertRequestStatus,
       "MwlFastEthernetType": MwlFastEthernetType,
       "MwlVpnMode": MwlVpnMode,
       "MwlRegionSettings": MwlRegionSettings,
       "MwlSpectrumBandsBits": MwlSpectrumBandsBits,
       "MwlESSRFVirtualizationMode": MwlESSRFVirtualizationMode,
       "MwlIFRFVirtualizationMode": MwlIFRFVirtualizationMode,
       "MwlYesNoSwitch": MwlYesNoSwitch,
       "MwlIpMode": MwlIpMode,
       "MwlChannelCenterFrequency": MwlChannelCenterFrequency,
       "MwlNetworkType": MwlNetworkType,
       "MwlIpv6AddrType": MwlIpv6AddrType,
       "MwlvenueGroup": MwlvenueGroup,
       "MwlvenueType": MwlvenueType,
       "MwlHotspotAccessNetworkType": MwlHotspotAccessNetworkType,
       "MwlHotspotAuthenType": MwlHotspotAuthenType,
       "MwlIPv6AvailabilityType": MwlIPv6AvailabilityType,
       "MwlIPv4AvailabilityType": MwlIPv4AvailabilityType,
       "MwlNAIRealmAuthMethod": MwlNAIRealmAuthMethod,
       "MwlApGroupType": MwlApGroupType,
       "MwlVpnClientProtocol": MwlVpnClientProtocol,
       "MwlRadiusCalledStationIdType": MwlRadiusCalledStationIdType,
       "MwlServiceDataFeature": MwlServiceDataFeature,
       "MwlServiceDataType": MwlServiceDataType,
       "MwlServiceDataFilterType": MwlServiceDataFilterType,
       "MwlRedirectionProtocol": MwlRedirectionProtocol,
       "MwlApRebootReasonCode": MwlApRebootReasonCode,
       "MwlBridgedVlanType": MwlBridgedVlanType,
       "MwlCliCmdGenWriteMode": MwlCliCmdGenWriteMode,
       "MwlVoiceClientType": MwlVoiceClientType,
       "MwlMMProtocolType": MwlMMProtocolType,
       "MwlApMacAssignOption": MwlApMacAssignOption,
       "MwlNplus1NotifType": MwlNplus1NotifType,
       "MwlTimerType": MwlTimerType,
       "MwlApplicationActionType": MwlApplicationActionType,
       "MwlAppVisibilityFlowType": MwlAppVisibilityFlowType,
       "MwlApplicationBWUnit": MwlApplicationBWUnit,
       "MwlDaysOfTheWeekBits": MwlDaysOfTheWeekBits,
       "MwlTimerIntervalState": MwlTimerIntervalState,
       "MwlEssIdType": MwlEssIdType,
       "MwlState": MwlState,
       "MwlTxBeamSupport": MwlTxBeamSupport,
       "MwlMcaApStatus": MwlMcaApStatus,
       "MwlArrayDataTypeAction": MwlArrayDataTypeAction,
       "meruTextualConventions": meruTextualConventions}
)
