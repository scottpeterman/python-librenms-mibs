# SNMP MIB module (MIB-Dell-10892) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\MIB-Dell-10892
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:17 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DellString(DisplayString):
    """Custom type DellString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class DellSecurityString(DisplayString):
    """Custom type DellSecurityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class DellCostofOwnershipString(DisplayString):
    """Custom type DellCostofOwnershipString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class DellMACAddress(OctetString):
    """Custom type DellMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class DellObjectRange(Integer32):
    """Custom type DellObjectRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )





class DellUnsigned8BitRange(Integer32):
    """Custom type DellUnsigned8BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class DellUnsigned16BitRange(Integer32):
    """Custom type DellUnsigned16BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DellUnsigned32BitRange(Gauge32):
    """Custom type DellUnsigned32BitRange based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class DellSigned32BitRange(Integer32):
    """Custom type DellSigned32BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )





class DellBoolean(Integer32):
    """Custom type DellBoolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )





class DellUnsigned64BitRange(OctetString):
    """Custom type DellUnsigned64BitRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class DellDateName(DisplayString):
    """Custom type DellDateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )
    fixed_length = 25





class DellStateCapabilities(Integer32):
    """Custom type DellStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("enableAndNotReadyCapable", 6))
    )





class DellStateSettings(Integer32):
    """Custom type DellStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("notReady", 4),
          ("enabledAndNotReady", 6))
    )





class DellProbeCapabilities(Integer32):
    """Custom type DellProbeCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("upperNonCriticalThresholdSetCapable", 1),
          ("lowerNonCriticalThresholdSetCapable", 2),
          ("upperNonCriticalThresholdDefaultCapable", 4),
          ("lowerNonCriticalThresholdDefaultCapable", 8))
    )





class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCritical", 4),
          ("critical", 5),
          ("nonRecoverable", 6),
          ("absent", 7))
    )





class DellStatusRedundancy(Integer32):
    """Custom type DellStatusRedundancy based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("full", 3),
          ("degraded", 4),
          ("lost", 5),
          ("notRedundant", 6),
          ("redundancyOffline", 7))
    )





class DellStatusProbe(Integer32):
    """Custom type DellStatusProbe based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCriticalUpper", 4),
          ("criticalUpper", 5),
          ("nonRecoverableUpper", 6),
          ("nonCriticalLower", 7),
          ("criticalLower", 8),
          ("nonRecoverableLower", 9),
          ("failed", 10))
    )





class SMSSupportedTypes(Integer32):
    """Custom type SMSSupportedTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("supportsSNMP", 1),
          ("supportsDMI", 2),
          ("supportsSNMPandDMI", 3),
          ("supportsCIMOM", 4),
          ("supportsSNMPandCIMOM", 5),
          ("supportsSNMPandDMIandCIMOM", 7))
    )





class SMSFeatureFlags(Integer32):
    """Custom type SMSFeatureFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("webOneToOneManagementPreferred", 1)
    )





class SMSSNMPAgentFeatureFlags(Integer32):
    """Custom type SMSSNMPAgentFeatureFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("supportsSparseTables", 1)
    )





class DellStateCapabilitiesLogUnique(Integer32):
    """Custom type DellStateCapabilitiesLogUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onlineCapable", 2),
          ("notReadyCapable", 4),
          ("resetCapable", 8))
    )





class DellStateSettingsLogUnique(Integer32):
    """Custom type DellStateSettingsLogUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("online", 2),
          ("notReady", 4),
          ("reset", 8))
    )





class DellLogFormat(Integer32):
    """Custom type DellLogFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("ascii", 2),
          ("uniCode", 3))
    )





class DellChassisType(Integer32):
    """Custom type DellChassisType based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("desktop", 3),
          ("lowProfileDesktop", 4),
          ("pizzaBox", 5),
          ("miniTower", 6),
          ("tower", 7),
          ("portable", 8),
          ("lapTop", 9),
          ("noteBook", 10),
          ("handHeld", 11),
          ("dockingStation", 12),
          ("allInOne", 13),
          ("subNoteBook", 14),
          ("spaceSaving", 15),
          ("lunchBox", 16),
          ("mainSystemChassis", 17),
          ("expansionChassis", 18),
          ("subChassis", 19),
          ("busExpansionChassis", 20),
          ("peripheralChassis", 21),
          ("raidChassis", 22),
          ("rackMountChassis", 23),
          ("sealedCasePC", 24),
          ("multiSystemChassis", 25))
    )





class DellChassisSystemClass(Integer32):
    """Custom type DellChassisSystemClass based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("workstationClass", 3),
          ("serverClass", 4),
          ("desktopClass", 5),
          ("portableClass", 6),
          ("netPCClass", 7),
          ("storageClass", 8))
    )





class DellConnectionStatus(Integer32):
    """Custom type DellConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("ok", 3),
          ("failure", 4))
    )





class DellFanControlCapabilities(Integer32):
    """Custom type DellFanControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("lowSpeedCapable", 2),
          ("highSpeedCapable", 4),
          ("lowOrHighSpeedCapable", 6))
    )





class DellFanControlSettings(Integer32):
    """Custom type DellFanControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("lowSpeed", 2),
          ("highSpeed", 4))
    )





class DellLEDControlCapabilities(Integer32):
    """Custom type DellLEDControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("alertOnErrorCapable", 2),
          ("alertOnWarningAndErrorCapable", 4),
          ("alertOnWarningOrErrorCapable", 6))
    )





class DellLEDControlSettings(Integer32):
    """Custom type DellLEDControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("alertOnError", 2),
          ("alertOnWarningAndError", 4))
    )





class DellHDFaultLEDControlCapabilities(Integer32):
    """Custom type DellHDFaultLEDControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("resetCapable", 8))
    )





class DellHDFaultLEDControlSettings(Integer32):
    """Custom type DellHDFaultLEDControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("notReady", 4),
          ("reset", 8),
          ("resetAndEnable", 10))
    )





class DellChassisIdentifyControlCapabilities(Integer32):
    """Custom type DellChassisIdentifyControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("identifyCapable", 8))
    )





class DellChassisIdentifyControlSettings(Integer32):
    """Custom type DellChassisIdentifyControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("notReady", 4),
          ("identifyChassis", 8),
          ("identifyChassisAndEnable", 10))
    )





class DellHostControlCapabilities(Integer32):
    """Custom type DellHostControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7,
              8,
              15,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("manualRebootCapable", 1),
          ("manualPowerOFFCapable", 2),
          ("manualPowerCycleCapable", 4),
          ("manualAllExceptOperatingSystemShutdownCapable", 7),
          ("manualOperatingSystemShutdownCapable", 8),
          ("manualFullyCapable", 15),
          ("manualRebootWithOSShutdownCapable", 16),
          ("manualRebootWithoutOSShutdownCapable", 32),
          ("manualPowerOffWithOSShutdownCapable", 64),
          ("manualPowerOffWithoutOSShutdownCapable", 128),
          ("manualPowerCycleWithOSShutdownCapable", 256),
          ("manualPowerCycleWithoutOSShutdownCapable", 512))
    )





class DellHostControlSettings(Integer32):
    """Custom type DellHostControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              9,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("manualReboot", 1),
          ("manualPowerOFF", 2),
          ("manualPowerCycle", 4),
          ("manualOperatingSystemShutdown", 8),
          ("manualOperatingSystemShutdownThenReboot", 9),
          ("manualOperatingSystemShutdownThenPowerOFF", 10),
          ("manualOperatingSystemShutdownThenPowerCycle", 12))
    )





class DellWatchDogControlCapabilities(Integer32):
    """Custom type DellWatchDogControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              27,
              31)
        )
    )
    namedValues = NamedValues(
        *(("automaticRebootCapable", 1),
          ("automaticPowerCycleCapable", 2),
          ("automaticNotificationCapable", 4),
          ("automaticWatchDogTimerCapable", 8),
          ("automaticPowerOffCapable", 16),
          ("automaticAllExceptNotificationCapable", 27),
          ("automaticFullyCapable", 31))
    )





class DellWatchControlSettings(Integer32):
    """Custom type DellWatchControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("automaticRebootEnabled", 1),
          ("automaticPowerCycleEnabled", 2),
          ("automaticNotificationEnabled", 4),
          ("automaticPowerOffEnabled", 8))
    )





class DellWatchDogTimerCapabilities(Integer32):
    """Custom type DellWatchDogTimerCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("type1Capable", 1),
          ("type2Capable", 2),
          ("type3Capable", 4))
    )





class DellPowerButtonControlCapabilities(Integer32):
    """Custom type DellPowerButtonControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2))
    )





class DellPowerButtonControlSettings(Integer32):
    """Custom type DellPowerButtonControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("disabled", 4))
    )





class DellNMIButtonControlCapabilities(Integer32):
    """Custom type DellNMIButtonControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2))
    )





class DellNMIButtonControlSettings(Integer32):
    """Custom type DellNMIButtonControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("disabled", 4))
    )





class DellSystemProperties(Integer32):
    """Custom type DellSystemProperties based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("energySmart", 1)
    )





class DellUUIDType(Integer32):
    """Custom type DellUUIDType based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("motherBoard", 3),
          ("systemBackPlane", 4),
          ("powerSupplyParallelingBoard", 5),
          ("peripheralBayBackPlane", 6),
          ("secondaryBackPlane", 7))
    )





class DellFirmwareType(Integer32):
    """Custom type DellFirmwareType based on Integer32"""
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
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("systemBIOS", 3),
          ("embeddedSystemManagementController", 4),
          ("powerSupplyParallelingBoard", 5),
          ("systemBackPlane", 6),
          ("powerVault2XXSKernel", 7),
          ("powerVault2XXSApplication", 8),
          ("frontPanel", 9),
          ("baseboardManagementController", 10),
          ("hotPlugPCI", 11),
          ("sensorData", 12),
          ("peripheralBay", 13),
          ("secondaryBackPlane", 14),
          ("secondaryBackPlaneESM3And4", 15),
          ("rac", 16),
          ("iDRAC", 17),
          ("iDRAC6", 18),
          ("unifiedServerConfigurator", 19),
          ("lifecycleController", 20),
          ("iDRAC7", 21),
          ("iDRAC8", 22),
          ("iDRAC9", 23))
    )





class DellIntrusionReading(Integer32):
    """Custom type DellIntrusionReading based on Integer32"""
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
        *(("chassisNotBreached", 1),
          ("chassisBreached", 2),
          ("chassisBreachedPrior", 3),
          ("chassisBreachSensorFailure", 4),
          ("driveBayOpen", 5),
          ("driveBayOpenExtended", 6))
    )





class DellIntrusionType(Integer32):
    """Custom type DellIntrusionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassisBreachDetectionWhenPowerON", 1),
          ("chassisBreachDetectionWhenPowerOFF", 2))
    )





class DellBaseBoardType(Integer32):
    """Custom type DellBaseBoardType based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("serverBlade", 3),
          ("connectivitySwitch", 4),
          ("systemManagementModule", 5),
          ("processorModule", 6),
          ("ioModule", 7),
          ("memoryModule", 8),
          ("daughterBoard", 9),
          ("motherboard", 10),
          ("processorMemoryModule", 11),
          ("processorIOModule", 12),
          ("interconnectBoard", 13))
    )





class DellBaseBoardFeatureFlags(Integer32):
    """Custom type DellBaseBoardFeatureFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("boardIsHostingBoard", 1),
          ("boardRequiresDaughterBoard", 2),
          ("boardIsRemovable", 4),
          ("boardIsReplaceable", 8),
          ("boardIsHotSwappable", 16))
    )





class DellSystemResourceMapType(Integer32):
    """Custom type DellSystemResourceMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("typeOne", 3))
    )





class DellResourceOwnerInterfaceType(Integer32):
    """Custom type DellResourceOwnerInterfaceType based on Integer32"""
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
        *(("typeIsOther", 1),
          ("typeIsUnknown", 2),
          ("typeIsInternal", 3),
          ("typeIsISA", 4),
          ("typeIsEISA", 5),
          ("typeIsMCA", 6),
          ("typeIsTurboChannel", 7),
          ("typeIsPCI", 8))
    )





class DellResourceShareDisposition(Integer32):
    """Custom type DellResourceShareDisposition based on Integer32"""
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
        *(("shareIsOther", 1),
          ("shareIsUnknown", 2),
          ("shareIsDeviceExclusive", 3),
          ("shareIsDriverExclusive", 4),
          ("shareIsShared", 5))
    )





class DellResourceMemoryFlags(Integer32):
    """Custom type DellResourceMemoryFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("memoryIsReadOnly", 1),
          ("memoryIsWriteOnly", 2),
          ("memoryIsReadAndWrite", 3),
          ("memoryIsPreFetchable", 4),
          ("memoryIsCombinedWritable", 8),
          ("memoryIsF24", 16))
    )





class DellResourceInterruptType(Integer32):
    """Custom type DellResourceInterruptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interruptIsLevelSensitive", 1),
          ("interruptIsLatched", 2))
    )





class DellResourceInterruptTrigger(Integer32):
    """Custom type DellResourceInterruptTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interruptIsActiveWhenLow", 1),
          ("interruptIsActiveWhenHigh", 2))
    )





class DellResourceDMATransferWidth(Integer32):
    """Custom type DellResourceDMATransferWidth based on Integer32"""
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
        *(("dmaTransferWidthIsOther", 1),
          ("dmaTransferWidthIsunknown", 2),
          ("dmaTransferWidthIs8Bits", 3),
          ("dmaTransferWidthIs16Bits", 4),
          ("dmaTransferWidthIs32Bits", 5),
          ("dmaTransferWidthIs64Bits", 6),
          ("dmaTransferWidthIs128Bits", 7))
    )





class DellResourceDMABusMaster(Integer32):
    """Custom type DellResourceDMABusMaster based on Integer32"""
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
        *(("dmaIsOther", 1),
          ("dmaIsUnknown", 2),
          ("dmaIsNotABusmaster", 3),
          ("dmaIsABusmaster", 4))
    )





class DellPowerSupplyStateCapabilitiesUnique(Integer32):
    """Custom type DellPowerSupplyStateCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onlineCapable", 2),
          ("notReadyCapable", 4))
    )





class DellPowerSupplyStateSettingsUnique(Integer32):
    """Custom type DellPowerSupplyStateSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              32,
              64,
              66,
              128,
              130,
              210,
              242)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onLine", 2),
          ("notReady", 4),
          ("fanFailure", 8),
          ("onlineAndFanFailure", 10),
          ("powerSupplyIsON", 16),
          ("powerSupplyIsOK", 32),
          ("acSwitchIsON", 64),
          ("onlineandAcSwitchIsON", 66),
          ("acPowerIsON", 128),
          ("onlineAndAcPowerIsON", 130),
          ("onlineAndPredictiveFailure", 210),
          ("acPowerAndSwitchAreOnPowerSupplyIsOnIsOkAndOnline", 242))
    )





class DellPowerSupplyType(Integer32):
    """Custom type DellPowerSupplyType based on Integer32"""
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
        *(("powerSupplyTypeIsOther", 1),
          ("powerSupplyTypeIsUnknown", 2),
          ("powerSupplyTypeIsLinear", 3),
          ("powerSupplyTypeIsSwitching", 4),
          ("powerSupplyTypeIsBattery", 5),
          ("powerSupplyTypeIsUPS", 6),
          ("powerSupplyTypeIsConverter", 7),
          ("powerSupplyTypeIsRegulator", 8),
          ("powerSupplyTypeIsAC", 9),
          ("powerSupplyTypeIsDC", 10),
          ("powerSupplyTypeIsVRM", 11))
    )





class DellPowerSupplySensorState(Integer32):
    """Custom type DellPowerSupplySensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("presenceDetected", 1),
          ("psFailureDetected", 2),
          ("predictiveFailure", 4),
          ("psACLost", 8),
          ("acLostOrOutOfRange", 16),
          ("acOutOfRangeButPresent", 32),
          ("configurationError", 64))
    )





class DellPowerSupplyConfigurationErrorType(Integer32):
    """Custom type DellPowerSupplyConfigurationErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vendorMismatch", 1),
          ("revisionMismatch", 2),
          ("processorMissing", 3))
    )





class DellVoltageType(Integer32):
    """Custom type DellVoltageType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("voltageProbeTypeIsOther", 1),
          ("voltageProbeTypeIsUnknown", 2),
          ("voltageProbeTypeIs1Point5Volt", 3),
          ("voltageProbeTypeIs3Point3Volt", 4),
          ("voltageProbeTypeIs5Volt", 5),
          ("voltageProbeTypeIsMinus5Volt", 6),
          ("voltageProbeTypeIs12Volt", 7),
          ("voltageProbeTypeIsMinus12Volt", 8),
          ("voltageProbeTypeIsIO", 9),
          ("voltageProbeTypeIsCore", 10),
          ("voltageProbeTypeIsFLEA", 11),
          ("voltageProbeTypeIsBattery", 12),
          ("voltageProbeTypeIsTerminator", 13),
          ("voltageProbeTypeIs2Point5Volt", 14),
          ("voltageProbeTypeIsGTL", 15),
          ("voltageProbeTypeIsDiscrete", 16))
    )





class DellVoltageDiscreteReading(Integer32):
    """Custom type DellVoltageDiscreteReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voltageIsGood", 1),
          ("voltageIsBad", 2))
    )





class DellAmperageProbeType(Integer32):
    """Custom type DellAmperageProbeType based on Integer32"""
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
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("amperageProbeTypeIsOther", 1),
          ("amperageProbeTypeIsUnknown", 2),
          ("amperageProbeTypeIs1Point5Volt", 3),
          ("amperageProbeTypeIs3Point3volt", 4),
          ("amperageProbeTypeIs5Volt", 5),
          ("amperageProbeTypeIsMinus5Volt", 6),
          ("amperageProbeTypeIs12Volt", 7),
          ("amperageProbeTypeIsMinus12Volt", 8),
          ("amperageProbeTypeIsIO", 9),
          ("amperageProbeTypeIsCore", 10),
          ("amperageProbeTypeIsFLEA", 11),
          ("amperageProbeTypeIsBattery", 12),
          ("amperageProbeTypeIsTerminator", 13),
          ("amperageProbeTypeIs2Point5Volt", 14),
          ("amperageProbeTypeIsGTL", 15),
          ("amperageProbeTypeIsDiscrete", 16),
          ("amperageProbeTypeIsPowerSupplyAmps", 23),
          ("amperageProbeTypeIsPowerSupplyWatts", 24),
          ("amperageProbeTypeIsSystemAmps", 25),
          ("amperageProbeTypeIsSystemWatts", 26))
    )





class DellAmperageDiscreteReading(Integer32):
    """Custom type DellAmperageDiscreteReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("amperageIsGood", 1),
          ("amperageIsBad", 2))
    )





class DellACPowerSwitchCapabilities(Integer32):
    """Custom type DellACPowerSwitchCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              14,
              16,
              30,
              32,
              62)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("inputSourceCord1NoReturnCapable", 2),
          ("inputSourceCord1ReturnCapable", 4),
          ("inputSourceCord2NoReturnCapable", 8),
          ("inputSourceCord1NoReturnCord1ReturnAndCord2NoReturnCapable", 14),
          ("inputSourceCord2ReturnCapable", 16),
          ("inputSourceAllExceptSharedCapable", 30),
          ("inputSourceSharedCapable", 32),
          ("inputSourceAllCapable", 62))
    )





class DellACPowerSwitchSettings(Integer32):
    """Custom type DellACPowerSwitchSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("inputSourceCord1NoReturn", 2),
          ("inputSourceCord1Return", 4),
          ("inputSourceCord2NoReturn", 8),
          ("inputSourceCord2Return", 16),
          ("inputSourceShared", 32))
    )





class DellACPowerSwitchRedundancyMode(Integer32):
    """Custom type DellACPowerSwitchRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRedundant", 1),
          ("redundant", 2))
    )





class DellACPowerCordStateCapabilities(Integer32):
    """Custom type DellACPowerCordStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enableCapable", 2),
          ("notReadyCapable", 4))
    )





class DellACPowerCordStateSettings(Integer32):
    """Custom type DellACPowerCordStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              26)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("notReady", 4),
          ("acPowerCordHasPower", 8),
          ("acPowerCordIsEnabledAndHasPower", 10),
          ("acPowerCordIsActiveSource", 16),
          ("acPowerCordIsEnabledHasPowerAndIsActiveSource", 26))
    )





class DellBatteryReading(Integer32):
    """Custom type DellBatteryReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("predictiveFailure", 1),
          ("failed", 2),
          ("presenceDetected", 4))
    )





class DellPowerCapCapabilities(Integer32):
    """Custom type DellPowerCapCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )





class DellPowerCapSetting(Integer32):
    """Custom type DellPowerCapSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )





class DellPowerProfileType(Integer32):
    """Custom type DellPowerProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("maxPerformance", 1),
          ("osControl", 2),
          ("activePowerController", 4),
          ("custom", 8))
    )





class DellCPUPowerPerformanceManagementType(Integer32):
    """Custom type DellCPUPowerPerformanceManagementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("maxPerformance", 1),
          ("minPower", 2),
          ("osDBPM", 4),
          ("systemDBPM", 8))
    )





class DellMemoryPowerPerformanceManagementType(Integer32):
    """Custom type DellMemoryPowerPerformanceManagementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("maxPerformance", 1),
          ("mhz1333", 2),
          ("mhz1067", 4),
          ("mhz800", 8),
          ("minPower", 16))
    )





class DellFanPowerPerformanceManagementType(Integer32):
    """Custom type DellFanPowerPerformanceManagementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maxPerformance", 1),
          ("minPower", 2))
    )





class DellCoolingDeviceType(Integer32):
    """Custom type DellCoolingDeviceType based on Integer32"""
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
        *(("coolingDeviceTypeIsOther", 1),
          ("coolingDeviceTypeIsUnknown", 2),
          ("coolingDeviceTypeIsAFan", 3),
          ("coolingDeviceTypeIsABlower", 4),
          ("coolingDeviceTypeIsAChipFan", 5),
          ("coolingDeviceTypeIsACabinetFan", 6),
          ("coolingDeviceTypeIsAPowerSupplyFan", 7),
          ("coolingDeviceTypeIsAHeatPipe", 8),
          ("coolingDeviceTypeIsRefrigeration", 9),
          ("coolingDeviceTypeIsActiveCooling", 10),
          ("coolingDeviceTypeIsPassiveCooling", 11))
    )





class DellCoolingDeviceSubType(Integer32):
    """Custom type DellCoolingDeviceSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              16)
        )
    )
    namedValues = NamedValues(
        *(("coolingDeviceSubTypeIsOther", 1),
          ("coolingDeviceSubTypeIsUnknown", 2),
          ("coolingDeviceSubTypeIsAFanThatReadsInRPM", 3),
          ("coolingDeviceSubTypeIsAFanReadsONorOFF", 4),
          ("coolingDeviceSubTypeIsAPowerSupplyFanThatReadsinRPM", 5),
          ("coolingDeviceSubTypeIsAPowerSupplyFanThatReadsONorOFF", 6),
          ("coolingDeviceSubTypeIsDiscrete", 16))
    )





class DellCoolingDeviceDiscreteReading(Integer32):
    """Custom type DellCoolingDeviceDiscreteReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coolingDeviceIsGood", 1),
          ("coolingDeviceIsBad", 2))
    )





class DellTemperatureProbeType(Integer32):
    """Custom type DellTemperatureProbeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16)
        )
    )
    namedValues = NamedValues(
        *(("temperatureProbeTypeIsOther", 1),
          ("temperatureProbeTypeIsUnknown", 2),
          ("temperatureProbeTypeIsAmbientESM", 3),
          ("temperatureProbeTypeIsDiscrete", 16))
    )





class DellTemperatureDiscreteReading(Integer32):
    """Custom type DellTemperatureDiscreteReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureIsGood", 1),
          ("temperatureIsBad", 2))
    )





class DellRemoteFlashBIOSStateCapabilitiesUnique(Integer32):
    """Custom type DellRemoteFlashBIOSStateCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("cancelCapable", 8),
          ("enableAndCancelCapable", 10))
    )





class DellRemoteFlashBIOSStateSettingsUnique(Integer32):
    """Custom type DellRemoteFlashBIOSStateSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("notReady", 4),
          ("canceled", 8),
          ("pending", 16),
          ("other", 32))
    )





class DellRemoteFlashBIOSCompletionCode(Integer32):
    """Custom type DellRemoteFlashBIOSCompletionCode based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("completionCodeIsOther", 1),
          ("completionCodeIsUnknown", 2),
          ("completionCodeIsOK", 3),
          ("completionCodeIsBadImage", 4),
          ("completionCodeIsNoFileAccess", 5),
          ("completionCodeIsNotReady", 6),
          ("completionCodeIsDisabled", 7),
          ("completionCodeIsNoBattery", 8),
          ("completionCodeIsNoChargedBattery", 9),
          ("completionCodeIsNoExternalPower", 10),
          ("completionCodeIsNo12VoltSet", 11),
          ("completionCodeIsNo12VoltRemoval", 12),
          ("completionCodeIsFlashMemoryFailed", 13),
          ("completionCodeIsGeneralFailure", 14),
          ("completionCodeIsDataMiscompare", 15),
          ("completionCodeIsNoImageFound", 16),
          ("completionCodeIsNoUpdatePerformed", 17))
    )





class DellGenericPortConnectorType(Integer32):
    """Custom type DellGenericPortConnectorType based on Integer32"""
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
              40)
        )
    )
    namedValues = NamedValues(
        *(("portConnectorTypeIsOther", 1),
          ("portConnectorTypeIsNone", 2),
          ("portConnectorTypeIsCentronics", 3),
          ("portConnectorTypeIsMiniCentronics", 4),
          ("portConnectorTypeIsProprietary", 5),
          ("portConnectorTypeIsDB25Male", 6),
          ("portConnectorTypeIsDB25Female", 7),
          ("portConnectorTypeIsDB15Male", 8),
          ("portConnectorTypeIsDB15Female", 9),
          ("portConnectorTypeIsDB9Male", 10),
          ("portConnectorTypeIsDB9Female", 11),
          ("portConnectorTypeIsRJ11", 12),
          ("portConnectorTypeIsRJ45", 13),
          ("portConnectorTypeIsMiniSCSI50Pin", 14),
          ("portConnectorTypeIsMiniDIN", 15),
          ("portConnectorTypeIsMicroDIN", 16),
          ("portConnectorTypeIsPS2", 17),
          ("portConnectorTypeIsInfrared", 18),
          ("portConnectorTypeIsHPHIL", 19),
          ("portConnectorTypeIsAccessBussUSB", 20),
          ("portConnectorTypeISSASCSI", 21),
          ("portConnectorTypeIsCirdin8Male", 22),
          ("portConnectorTypeIsCirdin8Female", 23),
          ("portConnectorTypeIsIDE", 24),
          ("portConnectorTypeIsFloppy", 25),
          ("portConnectorTypeIsDIN9Pin", 26),
          ("portConnectorTypeIsDIN25Pin", 27),
          ("portConnectorTypeIsDIN50Pin", 28),
          ("portConnectorTypeIsDIN68Pin", 29),
          ("portConnectorTypeIsCDROMLineOut", 30),
          ("portConnectorTypeIsMiniCentronics14", 31),
          ("portConnectorTypeIsMiniCentronics26", 32),
          ("portConnectorTypeIsMiniJack", 33),
          ("portConnectorTypeIsBNC", 34),
          ("portConnectorTypeIs1394", 35),
          ("portConnectorTypeIsPC98", 36),
          ("portConnectorTypeIsPC98Hireso", 37),
          ("portConnectorTypeIsPCH98", 38),
          ("portConnectorTypeIsPC98Note", 39),
          ("portConnectorTypeIsPC98Full", 40))
    )





class DellPortSecurityState(Integer32):
    """Custom type DellPortSecurityState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("none", 3),
          ("externalIsDisabled", 4),
          ("externalIsEnabled", 5),
          ("bootByPass", 6))
    )





class DellPointingPortConnectorType(Integer32):
    """Custom type DellPointingPortConnectorType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsSerial", 3),
          ("connectorPortTypeIsPS2", 4),
          ("connectorPortTypeIsInfrared", 5),
          ("connectorPortTypeIsHPHIL", 6),
          ("connectorPortTypeIsBusMouse", 7),
          ("connectorPortTypeIsADB", 8),
          ("connectorPortTypeIsDB9", 9),
          ("connectorPortTypeIsMicroDIN", 10),
          ("connectorPortTypeIsAccessBusUSB", 11),
          ("connectorPortTypeIsPC98", 12))
    )





class DellKeyboardPortConnectorType(Integer32):
    """Custom type DellKeyboardPortConnectorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsMiniDIN", 3),
          ("connectorPortTypeIsMicroDIN", 4),
          ("connectorPortTypeIsPS2", 5),
          ("connectorPortTypeIsInfrared", 6),
          ("connectorPortTypeIsHPHIL", 7),
          ("connectorPortTypeIsDB9", 8),
          ("connectorPortTypeIsAccessBusUSB", 9),
          ("connectorPortTypeIsPC98", 10))
    )





class DellProcessorPortConnectorType(Integer32):
    """Custom type DellProcessorPortConnectorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsDaughterdBoard", 3),
          ("connectorPortTypeIsZIFSocket", 4),
          ("connectorPortTypeIsAPiggyBackBoard", 5),
          ("connectorPortTypeIsNone", 6),
          ("connectorPortTypeIsLIFSocket", 7),
          ("connectorPortTypeIsSlot1", 8),
          ("connectorPortTypeIsSlot2", 9),
          ("connectorPortTypeIs370PinSocket", 10))
    )





class DellMemoryDevicePortConnectorType(Integer32):
    """Custom type DellMemoryDevicePortConnectorType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsSIMM", 3),
          ("connectorPortTypeIsSIP", 4),
          ("connectorPortTypeIsAChip", 5),
          ("connectorPortTypeIsDIP", 6),
          ("connectorPortTypeIsZIP", 7),
          ("connectorPortTypeIsAProprietaryCard", 8),
          ("connectorPortTypeIsDIMM", 9),
          ("connectorPortTypeIsTSOP", 10),
          ("connectorPortTypeIsARowOfChips", 11),
          ("connectorPortTypeIsRIMM", 12),
          ("connectorPortTypeIsSODIMM", 13),
          ("connectorPortTypeIsSRIMM", 14))
    )





class DellMonitorPortConnectorType(Integer32):
    """Custom type DellMonitorPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsDB15PinMale", 3),
          ("connectorPortTypeIsDB15PinFemale", 4))
    )





class DellSCSIPortConnectorType(Integer32):
    """Custom type DellSCSIPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsDIN25pin", 3),
          ("connectorPortTypeIsDIN50pin", 4),
          ("connectorPortTypeIsDIN68pin", 5))
    )





class DellParallelPortConnectorType(Integer32):
    """Custom type DellParallelPortConnectorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsDB25PinFemale", 3),
          ("connectorPortTypeIsDB25PinMale", 4),
          ("connectorPortTypeIsCentronics", 5),
          ("connectorPortTypeIsMiniCentronics", 6),
          ("connectorPortTypeIsProprietary", 7),
          ("connectorPortTypeIsCentronics14", 8),
          ("connectorPortTypeIsDB36PinFemale", 9),
          ("connectorPortTypeIsMiniCentronics20", 10))
    )





class DellParallelPortConnectorPinout(Integer32):
    """Custom type DellParallelPortConnectorPinout based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortPinoutIsOther", 1),
          ("connectorPortPinoutIsUnknown", 2),
          ("connectorPortPinoutIsXTorAT", 3),
          ("connectorPortPinoutIsPS2", 4),
          ("connectorPortPinoutIsIEEE1284", 5),
          ("connectorPortPinoutIsProprietary", 6),
          ("connectorPortPinoutIsPC98", 7),
          ("connectorPortPinoutIsPC98Hireso", 8),
          ("connectorPortPinoutIsPC98Note", 9),
          ("connectorPortPinoutIsPC98Full", 10))
    )





class DellParallelPortCapabilitiesUnique(Integer32):
    """Custom type DellParallelPortCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              30,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("atCapable", 2),
          ("ps2Capable", 4),
          ("ecpCapable", 8),
          ("eppCapable", 16),
          ("atOrPS2OrECPOrEPPCapable", 30),
          ("pc98Capable", 32),
          ("pc98HiresoCapable", 64),
          ("pc98HCapable", 128))
    )





class DellSerialPortConnectorType(Integer32):
    """Custom type DellSerialPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsDB9PinMale", 3),
          ("connectorPortTypeIsDB9PinFemale", 4),
          ("connectorPortTypeIsDB25PinMale", 5),
          ("connectorPortTypeIsDB25PinFemale", 6),
          ("connectorPortTypeIsRJ11", 7),
          ("connectorPortTypeIsRJ45", 8),
          ("connectorPortTypeIsProprietary", 9),
          ("connectorPortTypeIsCirdin8Male", 10),
          ("connectorPortTypeIsCirdin8Female", 11),
          ("connectorPortTypeIsMiniCentronics14", 12),
          ("connectorPortTypeIsMiniCentronics26", 13))
    )





class DellSerialPortCapabilitiesUnique(Integer32):
    """Custom type DellSerialPortCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("xtorATCapable", 4),
          ("c16450Capable", 8),
          ("c16550Capable", 16),
          ("c16550aCapable", 32),
          ("c8251Capable", 64),
          ("c8251FIFOCapable", 128))
    )





class DellUSBPortConnectorType(Integer32):
    """Custom type DellUSBPortConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsUSB", 3))
    )





class DellPointingDeviceType(Integer32):
    """Custom type DellPointingDeviceType based on Integer32"""
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
        *(("deviceTypeIsOther", 1),
          ("deviceTypeIsUnknown", 2),
          ("deviceTypeIsAMouse", 3),
          ("deviceTypeIsATrackBall", 4),
          ("deviceTypeIsATrackPoint", 5),
          ("deviceTypeIsAGlidePoint", 6),
          ("deviceTypeIsATouchPad", 7))
    )





class DellProcessorDeviceType(Integer32):
    """Custom type DellProcessorDeviceType based on Integer32"""
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
        *(("deviceTypeIsOther", 1),
          ("deviceTypeIsUnknown", 2),
          ("deviceTypeIsCPU", 3),
          ("deviceTypeIsMathProcessor", 4),
          ("deviceTypeIsDSP", 5),
          ("deviceTypeIsAVideoProcessor", 6))
    )





class DellProcessorDeviceFamily(Integer32):
    """Custom type DellProcessorDeviceFamily based on Integer32"""
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
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              96,
              97,
              98,
              99,
              100,
              101,
              107,
              112,
              120,
              121,
              122,
              128,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              179,
              180,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
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
              221,
              222,
              223,
              224,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              250,
              251)
        )
    )
    namedValues = NamedValues(
        *(("deviceFamilyIsOther", 1),
          ("deviceFamilyIsUnknown", 2),
          ("deviceFamilyIs8086", 3),
          ("deviceFamilyIs80286", 4),
          ("deviceFamilyIsIntel386", 5),
          ("deviceFamilyIsIntel486", 6),
          ("deviceFamilyIs8087", 7),
          ("deviceFamilyIs80287", 8),
          ("deviceFamilyIs80387", 9),
          ("deviceFamilyIs80487", 10),
          ("deviceFamilyIsPentium", 11),
          ("deviceFamilyIsPentiumPro", 12),
          ("deviceFamilyIsPentiumII", 13),
          ("deviceFamilyIsPentiumMMX", 14),
          ("deviceFamilyIsCeleron", 15),
          ("deviceFamilyIsPentiumIIXeon", 16),
          ("deviceFamilyIsPentiumIII", 17),
          ("deviceFamilyIsPentiumIIIXeon", 18),
          ("deviceFamilyIsPentiumIIISpeedStep", 19),
          ("deviceFamilyIsItanium", 20),
          ("deviceFamilyIsIntelXeon", 21),
          ("deviceFamilyIsPentium4", 22),
          ("deviceFamilyIsIntelXeonMP", 23),
          ("deviceFamilyIsIntelItanium2", 24),
          ("deviceFamilyIsK5", 25),
          ("deviceFamilyIsK6", 26),
          ("deviceFamilyIsK6-2", 27),
          ("deviceFamilyIsK6-3", 28),
          ("deviceFamilyIsAMDAthlon", 29),
          ("deviceFamilyIsAMD2900", 30),
          ("deviceFamilyIsK6-2Plus", 31),
          ("deviceFamilyIsPowerPC", 32),
          ("deviceFamilyIsPowerPC601", 33),
          ("deviceFamilyIsPowerPC603", 34),
          ("deviceFamilyIsPowerPC603Plus", 35),
          ("deviceFamilyIsPowerPC604", 36),
          ("deviceFamilyIsPowerPC620", 37),
          ("deviceFamilyIsPowerPCx704", 38),
          ("deviceFamilyIsPowerPC750", 39),
          ("deviceFamilyIsIntelCoreDuo", 40),
          ("deviceFamilyIsIntelCoreDuoMobile", 41),
          ("deviceFamilyIsIntelCoreSoloMobile", 42),
          ("deviceFamilyIsIntelAtom", 43),
          ("deviceFamilyIsAlpha", 48),
          ("deviceFamilyIsAlpha21064", 49),
          ("deviceFamilyIsAlpha21066", 50),
          ("deviceFamilyIsAlpha21164", 51),
          ("deviceFamilyIsAlpha21164PC", 52),
          ("deviceFamilyIsAlpha21164a", 53),
          ("deviceFamilyIsAlpha21264", 54),
          ("deviceFamilyIsAlpha21364", 55),
          ("deviceFamilyIsAMDTurionIIUltraDualMobileM", 56),
          ("deviceFamilyIsAMDTurionIIDualMobileM", 57),
          ("deviceFamilyIsAMDAthlonIIDualMobileM", 58),
          ("deviceFamilyIsAMDOpteron6100", 59),
          ("deviceFamilyIsAMDOpteron4100", 60),
          ("deviceFamilyIsAMDOpteron6200", 61),
          ("deviceFamilyIsAMDOpteron4200", 62),
          ("deviceFamilyIsMIPS", 64),
          ("deviceFamilyIsMIPSR4000", 65),
          ("deviceFamilyIsMIPSR4200", 66),
          ("deviceFamilyIsMIPSR4400", 67),
          ("deviceFamilyIsMIPSR4600", 68),
          ("deviceFamilyIsMIPSR10000", 69),
          ("deviceFamilyIsSPARC", 80),
          ("deviceFamilyIsSuperSPARC", 81),
          ("deviceFamilyIsmicroSPARCII", 82),
          ("deviceFamilyIsmicroSPARCIIep", 83),
          ("deviceFamilyIsUltraSPARC", 84),
          ("deviceFamilyIsUltraSPARCII", 85),
          ("deviceFamilyIsUltraSPARCIIi", 86),
          ("deviceFamilyIsUltraSPARCIII", 87),
          ("deviceFamilyIsUltraSPARCIIIi", 88),
          ("deviceFamilyIs68040", 96),
          ("deviceFamilyIs68xxx", 97),
          ("deviceFamilyIs68000", 98),
          ("deviceFamilyIs68010", 99),
          ("deviceFamilyIs68020", 100),
          ("deviceFamilyIs68030", 101),
          ("deviceFamilyIsAMDZen", 107),
          ("deviceFamilyIsHobbit", 112),
          ("deviceFamilyIsCrusoeTM5000", 120),
          ("deviceFamilyIsCrusoeTM3000", 121),
          ("deviceFamilyIsEfficeonTM8000", 122),
          ("deviceFamilyIsWeitek", 128),
          ("deviceFamilyIsIntelCeleronM", 130),
          ("deviceFamilyIsAMDAthlon64", 131),
          ("deviceFamilyIsAMDOpteron", 132),
          ("deviceFamilyIsAMDSempron", 133),
          ("deviceFamilyIsAMDTurion64Mobile", 134),
          ("deviceFamilyIsDualCoreAMDOpteron", 135),
          ("deviceFamilyIsAMDAthlon64X2DualCore", 136),
          ("deviceFamilyIsAMDTurion64X2Mobile", 137),
          ("deviceFamilyIsQuadCoreAMDOpteron", 138),
          ("deviceFamilyIsThirdGenerationAMDOpteron", 139),
          ("deviceFamilyIsAMDPhenomFXQuadCore", 140),
          ("deviceFamilyIsAMDPhenomX4QuadCore", 141),
          ("deviceFamilyIsAMDPhenomX2DualCore", 142),
          ("deviceFamilyIsAMDAthlonX2DualCore", 143),
          ("deviceFamilyIsPA-RISC", 144),
          ("deviceFamilyIsPA-RISC8500", 145),
          ("deviceFamilyIsPA-RISC8000", 146),
          ("deviceFamilyIsPA-RISC7300LC", 147),
          ("deviceFamilyIsPA-RISC7200", 148),
          ("deviceFamilyIsPA-RISC7100LC", 149),
          ("deviceFamilyIsPA-RISC7100", 150),
          ("deviceFamilyIsV30", 160),
          ("deviceFamilyIsQuadCoreIntelXeon3200", 161),
          ("deviceFamilyIsDualCoreIntelXeon3000", 162),
          ("deviceFamilyIsQuadCoreIntelXeon5300", 163),
          ("deviceFamilyIsDualCoreIntelXeon5100", 164),
          ("deviceFamilyIsDualCoreIntelXeon5000", 165),
          ("deviceFamilyIsDualCoreIntelXeonLV", 166),
          ("deviceFamilyIsDualCoreIntelXeonULV", 167),
          ("deviceFamilyIsDualCoreIntelXeon7100", 168),
          ("deviceFamilyIsQuadCoreIntelXeon5400", 169),
          ("deviceFamilyIsQuadCoreIntelXeon", 170),
          ("deviceFamilyIsDualCoreIntelXeon5200", 171),
          ("deviceFamilyIsDualCoreIntelXeon7200", 172),
          ("deviceFamilyIsQuadCoreIntelXeon7300", 173),
          ("deviceFamilyIsQuadCoreIntelXeon7400", 174),
          ("deviceFamilyIsMultiCoreIntelXeon7400", 175),
          ("deviceFamilyIsM1", 176),
          ("deviceFamilyIsM2", 177),
          ("deviceFamilyIsIntelPentium4HT", 179),
          ("deviceFamilyIsAS400", 180),
          ("deviceFamilyIsAMDAthlonXP", 182),
          ("deviceFamilyIsAMDAthlonMP", 183),
          ("deviceFamilyIsAMDDuron", 184),
          ("deviceFamilyIsIntelPentiumM", 185),
          ("deviceFamilyIsIntelCeleronD", 186),
          ("deviceFamilyIsIntelPentiumD", 187),
          ("deviceFamilyIsIntelPentiumExtreme", 188),
          ("deviceFamilyIsIntelCoreSolo", 189),
          ("deviceFamilyIsIntelCore2", 190),
          ("deviceFamilyIsIntelCore2Duo", 191),
          ("deviceFamilyIsIntelCore2Solo", 192),
          ("deviceFamilyIsIntelCore2Extreme", 193),
          ("deviceFamilyIsIntelCore2Quad", 194),
          ("deviceFamilyIsIntelCore2ExtremeMobile", 195),
          ("deviceFamilyIsIntelCore2DuoMobile", 196),
          ("deviceFamilyIsIntelCore2SoloMobile", 197),
          ("deviceFamilyIsIntelCorei7", 198),
          ("deviceFamilyIsDualCoreIntelCeleron", 199),
          ("deviceFamilyIsIBM390", 200),
          ("deviceFamilyIsG4", 201),
          ("deviceFamilyIsG5", 202),
          ("deviceFamilyIsESA390G6", 203),
          ("deviceFamilyIszArchitectur", 204),
          ("deviceFamilyIsIntelCorei5", 205),
          ("deviceFamilyIsIntelCorei3", 206),
          ("deviceFamilyIsVIAC7-M", 210),
          ("deviceFamilyIsVIAC7-D", 211),
          ("deviceFamilyIsVIAC7", 212),
          ("deviceFamilyIsVIAEden", 213),
          ("deviceFamilyIsMultiCoreIntelXeon", 214),
          ("deviceFamilyIsDualCoreIntelXeon3xxx", 215),
          ("deviceFamilyIsQuadCoreIntelXeon3xxx", 216),
          ("deviceFamilyIsVIANano", 217),
          ("deviceFamilyIsDualCoreIntelXeon5xxx", 218),
          ("deviceFamilyIsQuadCoreIntelXeon5xxx", 219),
          ("deviceFamilyIsDualCoreIntelXeon7xxx", 221),
          ("deviceFamilyIsQuadCoreIntelXeon7xxx", 222),
          ("deviceFamilyIsMultiCoreIntelXeon7xxx", 223),
          ("deviceFamilyIsMultiCoreIntelXeon3400", 224),
          ("deviceFamilyIsEmbeddedAMDOpertonQuadCore", 230),
          ("deviceFamilyIsAMDPhenomTripleCore", 231),
          ("deviceFamilyIsAMDTurionUltraDualCoreMobile", 232),
          ("deviceFamilyIsAMDTurionDualCoreMobile", 233),
          ("deviceFamilyIsAMDAthlonDualCore", 234),
          ("deviceFamilyIsAMDSempronSI", 235),
          ("deviceFamilyIsAMDPhenomII", 236),
          ("deviceFamilyIsAMDAthlonII", 237),
          ("deviceFamilyIsSixCoreAMDOpteron", 238),
          ("deviceFamilyIsAMDSempronM", 239),
          ("deviceFamilyIsi860", 250),
          ("deviceFamilyIsi960", 251))
    )





class DellProcessorDeviceStatusState(Integer32):
    """Custom type DellProcessorDeviceStatusState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("enabled", 3),
          ("userDisabled", 4),
          ("biosDisabled", 5),
          ("idle", 6))
    )





class DellProcessorUpgradeInformation(Integer32):
    """Custom type DellProcessorUpgradeInformation based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("processorUpgradeIsOther", 1),
          ("processorUpgradeIsUnknown", 2),
          ("processorUpgradeIsByDaughterBoard", 3),
          ("processorUpgradeIsByZIFSocket", 4),
          ("processorUpgradeIsByReplacement", 5),
          ("processorUpgradeIsNone", 6),
          ("processorUpgradeIsByLIFSocket", 7),
          ("processorUpgradeIsBySlot1", 8),
          ("processorUpgradeIsBySlot2", 9),
          ("processorUpgradeIsBy370PinSocket", 10),
          ("processorUpgradeIsBySlotA", 11),
          ("processorUpgradeIsBySlotM", 12),
          ("processorUpgradeIsByScoket423", 13),
          ("processorUpgradeIsBySocketA", 14),
          ("processorUpgradeIsBySocket478", 15),
          ("processorUpgradeIsBySocket754", 16),
          ("processorUpgradeIsBySocket940", 17),
          ("processorUpgradeIsBySocket939", 18),
          ("processorUpgradeIsBySocketmPGA604", 19),
          ("processorUpgradeIsBySocketLGA771", 20),
          ("processorUpgradeIsBySocketLGA775", 21),
          ("processorUpgradeIsBySocketS1", 22),
          ("processorUpgradeIsBySocketAM2", 23),
          ("processorUpgradeIsBySocketF", 24),
          ("processorUpgradeIsBySocketLGA1366", 25))
    )





class DellProcessorDeviceStatusReading(Integer32):
    """Custom type DellProcessorDeviceStatusReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              32,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 1),
          ("thermalTrip", 2),
          ("configurationError", 32),
          ("processorPresent", 128),
          ("processorDisabled", 256),
          ("terminatorPresent", 512),
          ("processorThrottled", 1024))
    )





class DellCacheDeviceType(Integer32):
    """Custom type DellCacheDeviceType based on Integer32"""
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
        *(("deviceTypeIsOther", 1),
          ("deviceTypeIsUnknown", 2),
          ("deviceTypeIsInstruction", 3),
          ("deviceTypeIsData", 4),
          ("deviceTypeIsUnified", 5))
    )





class DellCacheDeviceLevel(Integer32):
    """Custom type DellCacheDeviceLevel based on Integer32"""
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
        *(("deviceLevelIsOther", 1),
          ("deviceLevelIsUnknown", 2),
          ("deviceLevelIsPrimary", 3),
          ("deviceLevelIsSecondary", 4),
          ("deviceLevelIsTertiary", 5))
    )





class DellCacheDeviceWritePolicy(Integer32):
    """Custom type DellCacheDeviceWritePolicy based on Integer32"""
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
        *(("deviceWritePolicyIsOther", 1),
          ("deviceWritePolicyIsUnknown", 2),
          ("deviceWritePolicyIsWriteBack", 3),
          ("deviceWritePolicyIsWriteThrough", 4),
          ("deviceWritePolicyIsVariesByAddress", 5),
          ("deviceWritePolicyIsDeterminedByIO", 6))
    )





class DellCacheDeviceStatusState(Integer32):
    """Custom type DellCacheDeviceStatusState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("enabled", 3),
          ("userDisabled", 4),
          ("biosDisabled", 5))
    )





class DellCacheDeviceECCType(Integer32):
    """Custom type DellCacheDeviceECCType based on Integer32"""
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
        *(("deviceECCTypeIsOther", 1),
          ("deviceECCTypeIsUnknown", 2),
          ("deviceECCTypeIsNone", 3),
          ("deviceECCTypeIsParity", 4),
          ("deviceECCTypeIsSingleBitECC", 5),
          ("deviceECCTypeIsMultiBitECC", 6),
          ("deviceECCTypeIsCRC", 7))
    )





class DellCacheDeviceAssociativity(Integer32):
    """Custom type DellCacheDeviceAssociativity based on Integer32"""
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
        *(("deviceAssociativityIsOther", 1),
          ("deviceAssociativityIsUnknown", 2),
          ("deviceAssociativityIsDirectMapped", 3),
          ("deviceAssociativityIsTwoWaySetAssociative", 4),
          ("deviceAssociativityIsFourWaySetAssociative", 5),
          ("deviceAssociativityIsFullyAssociative", 6),
          ("deviceAssociativityIsEightWaySetAssociative", 7),
          ("deviceAssociativityIsSixteenWaySetAssociative", 8),
          ("deviceAssociativityIs12WaySetAssociative", 9),
          ("deviceAssociativityIs24WaySetAssociative", 10),
          ("deviceAssociativityIs32WaySetAssociative", 11),
          ("deviceAssociativityIs48WaySetAssociative", 12),
          ("deviceAssociativityIs64WaySetAssociative", 13))
    )





class DellCacheDeviceLocation(Integer32):
    """Custom type DellCacheDeviceLocation based on Integer32"""
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
        *(("deviceLocationIsOther", 1),
          ("deviceLocationIsUnknown", 2),
          ("deviceLocationIsInternal", 3),
          ("deviceLocationIsExternal", 4))
    )





class DellCacheDeviceSRAMType(Integer32):
    """Custom type DellCacheDeviceSRAMType based on Integer32"""
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
        *(("deviceSRAMTypeIsOther", 1),
          ("deviceSRAMTypeIsUnknown", 2),
          ("deviceSRAMTypeIsNonBurst", 3),
          ("deviceSRAMTypeIsBurst", 4),
          ("deviceSRAMTypeIsPipeBurst", 5),
          ("deviceSRAMTypeIsSynchronous", 6),
          ("deviceSRAMTypeIsAsynchronous", 7))
    )





class DellMemoryDeviceFormFactor(Integer32):
    """Custom type DellMemoryDeviceFormFactor based on Integer32"""
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
        *(("deviceFormFactorIsOther", 1),
          ("deviceFormFactorIsUnknown", 2),
          ("deviceFormFactorIsSIMM", 3),
          ("deviceFormFactorIsSIP", 4),
          ("deviceFormFactorIsAChip", 5),
          ("deviceFormFactorIsDIP", 6),
          ("deviceFormFactorIsZIP", 7),
          ("deviceFormFactorIsAProprietaryCard", 8),
          ("deviceFormFactorIsDIMM", 9),
          ("deviceFormFactorIsTSOP", 10),
          ("deviceFormFactorIsARowOfChips", 11),
          ("deviceFormFactorIsRIMM", 12),
          ("deviceFormFactorIsSODIMM", 13),
          ("deviceFormFactorIsSRIMM", 14),
          ("deviceFormFactorIsFBDIMM", 15))
    )





class DellMemoryDeviceType(Integer32):
    """Custom type DellMemoryDeviceType based on Integer32"""
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
              20,
              24,
              25,
              34)
        )
    )
    namedValues = NamedValues(
        *(("deviceTypeIsOther", 1),
          ("deviceTypeIsUnknown", 2),
          ("deviceTypeIsDRAM", 3),
          ("deviceTypeIsEDRAM", 4),
          ("deviceTypeIsVRAM", 5),
          ("deviceTypeIsSRAM", 6),
          ("deviceTypeIsRAM", 7),
          ("deviceTypeIsROM", 8),
          ("deviceTypeIsFLASH", 9),
          ("deviceTypeIsEEPROM", 10),
          ("deviceTypeIsFEPROM", 11),
          ("deviceTypeIsEPROM", 12),
          ("deviceTypeIsCDRAM", 13),
          ("deviceTypeIs3DRAM", 14),
          ("deviceTypeIsSDRAM", 15),
          ("deviceTypeIsSGRAM", 16),
          ("deviceTypeIsRDRAM", 17),
          ("deviceTypeIsDDR", 18),
          ("deviceTypeIsDDR2", 19),
          ("deviceTypeIsDDR2FBDIMM", 20),
          ("deviceTypeIsDDR3", 24),
          ("deviceTypeIsFBD2", 25),
          ("deviceTypeIsDDR4", 34))
    )





class DellMemoryDeviceRank(Integer32):
    """Custom type DellMemoryDeviceRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("deviceRankIsUnknown", 1),
          ("deviceRankIsSingle", 2),
          ("deviceRankIsDual", 4),
          ("deviceRankIsQuad", 8),
          ("deviceRankIsOctal", 16),
          ("deviceRankIsHexa", 32))
    )





class DellMemoryDeviceTypeDetails(Integer32):
    """Custom type DellMemoryDeviceTypeDetails based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              4096,
              8192,
              16384)
        )
    )
    namedValues = NamedValues(
        *(("deviceTypeDetailIsOther", 2),
          ("deviceTypeDetailIsUnknown", 4),
          ("deviceTypeDetailIsFastPaged", 8),
          ("deviceTypeDetailIsStaticColumn", 16),
          ("deviceTypeDetailIsPseudoStatic", 32),
          ("deviceTypeDetailIsRAMBUS", 64),
          ("deviceTypeDetailIsSynchronous", 128),
          ("deviceTypeDetailIsCMOS", 256),
          ("deviceTypeDetailIsEDO", 512),
          ("deviceTypeDetailIsWindowDRAM", 1024),
          ("deviceTypeDetailIsCacheDRAM", 2048),
          ("deviceTypeDetailIsNonVolatile", 4096),
          ("deviceTypeDetailIsRegistered", 8192),
          ("deviceTypeDetailIsNonRegistered", 16384))
    )





class DellMemoryDeviceFailureModes(Integer32):
    """Custom type DellMemoryDeviceFailureModes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              4096,
              8192,
              16384,
              32768,
              65536,
              131072,
              262144)
        )
    )
    namedValues = NamedValues(
        *(("eccSingleBitCorrectionWarningRate", 1),
          ("eccSingleBitCorrectionFailureRate", 2),
          ("eccMultiBitFault", 4),
          ("eccSingleBitCorrectionLoggingDisabled", 8),
          ("deviceDisabledBySpareActivation", 16),
          ("nvdimmNotReady", 32),
          ("nvdimmSaveError", 64),
          ("nvdimmRestoreErrorOrTimeout", 128),
          ("nvdimmIllegalConfiguration", 256),
          ("nvdimmNotResponding", 512),
          ("nvdimmArmFailureOrTimeout", 1024),
          ("nvdimmsInWriteProtectMode", 2048),
          ("nvmLifetimeExpired", 4096),
          ("nvdimmPersistencyLost", 8192),
          ("nvdimmPersistencyRestored", 16384),
          ("nvmLifetimeLessThanFivePercent", 32768),
          ("aepUnCorrectableError", 65536),
          ("aepCorrectableError", 131072),
          ("aepOperatingNormally", 262144))
    )





class DellMemoryDeviceMemoryTechnology(Integer32):
    """Custom type DellMemoryDeviceMemoryTechnology based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("dram", 3),
          ("nvdimm-n", 4),
          ("nvdimm-f", 5),
          ("nvdimm-p", 6),
          ("intelpersistentmemory", 7))
    )





class DellGenericDeviceType(Integer32):
    """Custom type DellGenericDeviceType based on Integer32"""
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
        *(("deviceTypeIsOther", 1),
          ("deviceTypeIsUnknown", 2),
          ("deviceTypeIsAVideoDevice", 3),
          ("deviceTypeIsASCSIController", 4),
          ("deviceTypeIsAnEthernetDevice", 5),
          ("deviceTypeIsTokenRingDevice", 6),
          ("deviceTypeIsASoundDevice", 7))
    )





class DellNetworkDeviceConnectionStatus(Integer32):
    """Custom type DellNetworkDeviceConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2),
          ("driverBad", 3),
          ("driverDisabled", 4),
          ("hardwareInitalizing", 10),
          ("hardwareResetting", 11),
          ("hardwareClosing", 12),
          ("hardwareNotReady", 13))
    )





class DellNetworkDeviceTeamingFlags(Integer32):
    """Custom type DellNetworkDeviceTeamingFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noTeam", 1),
          ("teamingEnabled", 2),
          ("adapterFaultToleranceMode", 4),
          ("loadBalancingMode", 8))
    )





class DellNetworkDeviceTOECapabilityFlags(Integer32):
    """Custom type DellNetworkDeviceTOECapabilityFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("available", 2),
          ("notAvailable", 4),
          ("cannotBeDetermined", 8),
          ("driverNotResponding", 16))
    )





class DellNetworkDeviceRDMACapabilityFlags(Integer32):
    """Custom type DellNetworkDeviceRDMACapabilityFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("available", 2),
          ("notAvailable", 4),
          ("cannotBeDetermined", 8),
          ("driverNotResponding", 16))
    )





class DellNetworkDeviceiSCSICapabilityFlags(Integer32):
    """Custom type DellNetworkDeviceiSCSICapabilityFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("available", 2),
          ("notAvailable", 4),
          ("cannotBeDetermined", 8),
          ("driverNotResponding", 16))
    )





class DellNetworkDeviceCapabilities(Integer32):
    """Custom type DellNetworkDeviceCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("toe", 2),
          ("iscsiOffload", 4),
          ("fcoeOffload", 8),
          ("unknown", 16))
    )





class DellNetworkDeviceNParEPEnabled(Integer32):
    """Custom type DellNetworkDeviceNParEPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", 3))
    )





class DellManagedSystemServicesDeviceType(Integer32):
    """Custom type DellManagedSystemServicesDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("optionalDevice", 1)
    )





class DellSDCardDeviceType(Integer32):
    """Custom type DellSDCardDeviceType based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("hypervisor", 3),
          ("vFlash", 4))
    )





class DellSDCardDeviceConfigCapabilities(Integer32):
    """Custom type DellSDCardDeviceConfigCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdCapable", 1),
          ("vFlashCapable", 2))
    )





class DellSDCardDeviceConfigSettings(Integer32):
    """Custom type DellSDCardDeviceConfigSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdEnabled", 1),
          ("vFlashEnabled", 2))
    )





class DellSDCardDeviceCardState(Integer32):
    """Custom type DellSDCardDeviceCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("ipmiReady", 2),
          ("fullReady", 4),
          ("offline", 8),
          ("failed", 16),
          ("active", 32),
          ("bootable", 64),
          ("writeProtect", 128),
          ("standby", 256))
    )





class DellSDCardDeviceCardLicensed(Integer32):
    """Custom type DellSDCardDeviceCardLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("licensed", 1)
    )





class DellSystemSlotStateCapabilities(Integer32):
    """Custom type DellSystemSlotStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              126,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32640,
              32766)
        )
    )
    namedValues = NamedValues(
        *(("systemSlotHotPlugIsUnknown", 1),
          ("systemSlotHotPlugIsHotPluggableCapable", 2),
          ("systemSlotHotPlugCanBePoweredOn", 4),
          ("systemSlotHotPlugCanSignalAttention", 8),
          ("systemSlotHotPlugCanSignalPowerFault", 16),
          ("systemSlotHotPlugCanSignalAdapterPresent", 32),
          ("systemSlotHotPlugCanSignalPowerButtonPressed", 64),
          ("canSupportAllHotPlugCapabilities", 126),
          ("systemSlotCanProvide5Volts", 128),
          ("systemSlotCanProvide3Point3Volts", 256),
          ("systemSlotCanSignalIfShared", 512),
          ("systemSlotCanSupportCard16", 1024),
          ("systemSlotCanSupportCardBus", 2048),
          ("systemSlotCanSupportZoomVideo", 4096),
          ("systemSlotCanSupportModemRingResume", 8192),
          ("systemSlotCanSupportPMESignal", 16384),
          ("canSupportAllSlotCapabilities", 32640),
          ("canSupportAllSlotAndAllHotPlugCapabilities", 32766))
    )





class DellSystemSlotStateSettings(Integer32):
    """Custom type DellSystemSlotStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              36,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              16770,
              16804,
              16806,
              17316)
        )
    )
    namedValues = NamedValues(
        *(("systemSlotHotPlugIsUnknown", 1),
          ("systemSlotHotPlugIsHotPluggable", 2),
          ("systemSlotHotPlugIsPoweredOn", 4),
          ("systemSlotHotPlugIsAtAttention", 8),
          ("systemSlotHotPlugHasPowerFaulted", 16),
          ("systemSlotHotPlugAdapterIsPresent", 32),
          ("systemSlotHotPlugAdapterPresentAndPoweredOn", 36),
          ("systemSlotHotPlugPowerButtonPressed", 64),
          ("systemSlotProvides5Volts", 128),
          ("systemSlotProvides3Point3Volts", 256),
          ("systemSlotIsShared", 512),
          ("systemSlotSupportsCard16", 1024),
          ("systemSlotSupportsCardBus", 2048),
          ("systemSlotSupportsZoomVideo", 4096),
          ("systemSlotSupportsModemRingResume", 8192),
          ("systemSlotSupportsPMESignal", 16384),
          ("supportsPMEand3P3Vand5VandHotPluggable", 16770),
          ("supportsPMEand3P3Vand5VhasAdapterOn", 16804),
          ("supportsPMEand3P3Vand5VhasAdapterOnandisHotPluggable", 16806),
          ("supportsPMEand3P3VIsSharedand5VhasAdapterOnandHotPlugable", 17316))
    )





class DellSystemSlotType(Integer32):
    """Custom type DellSystemSlotType based on Integer32"""
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
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              184,
              185,
              186,
              187,
              188,
              189)
        )
    )
    namedValues = NamedValues(
        *(("systemSlotIsOther", 1),
          ("systemSlotIsUnknown", 2),
          ("systemSlotIsISA", 3),
          ("systemSlotIsMCA", 4),
          ("systemSlotIsEISA", 5),
          ("systemSlotIsPCI", 6),
          ("systemSlotIsPCMCIA", 7),
          ("systemSlotIsVLVESA", 8),
          ("systemSlotIsProprietary", 9),
          ("systemSlotIsProcessorCard", 10),
          ("systemSlotIsProprietaryMemory", 11),
          ("systemSlotIsIORiserCard", 12),
          ("systemSlotIsNuBUS", 13),
          ("systemSlotIsPCI66MHz", 14),
          ("systemSlotIsAGP", 15),
          ("systemSlotIsAGP2X", 16),
          ("systemSlotIsAGP4X", 17),
          ("systemSlotIsPCIX", 18),
          ("systemSlotIsAGP8X", 19),
          ("systemSlotIsM2Socket1DP", 20),
          ("systemSlotIsM2Socket1SD", 21),
          ("systemSlotIsM2Socket2", 22),
          ("systemSlotIsM2Socket3", 23),
          ("systemSlotIsMXMT1", 24),
          ("systemSlotIsMXMT2", 25),
          ("systemSlotIsMXMT3SC", 26),
          ("systemSlotIsMXMT3HEC", 27),
          ("systemSlotIsMXMT4", 28),
          ("systemSlotIsMXM3TA", 29),
          ("systemSlotIsMXM3TB", 30),
          ("systemSlotIsPCIEGEN2SFF8639", 31),
          ("systemSlotIsPCIEGEN3SFF8639", 32),
          ("systemSlotIsPCIEMINI52PWBK", 33),
          ("systemSlotIsPCIEMINI52PWOBK", 34),
          ("systemSlotIsPCIEMINI76P", 35),
          ("systemSlotIsPC98C20", 160),
          ("systemSlotIsPC98C24", 161),
          ("systemSlotIsPC98E", 162),
          ("systemSlotIsPC98LocalBus", 163),
          ("systemSlotIsPC98Card", 164),
          ("systemSlotIsPCIExpress", 165),
          ("systemSlotIsPCIExpressX1", 166),
          ("systemSlotIsPCIExpressX2", 167),
          ("systemSlotIsPCIExpressX4", 168),
          ("systemSlotIsPCIExpressX8", 169),
          ("systemSlotIsPCIExpressX16", 170),
          ("systemSlotIsPCIExpressGen2", 171),
          ("systemSlotIsPCIExpressGen2X1", 172),
          ("systemSlotIsPCIExpressGen2X2", 173),
          ("systemSlotIsPCIExpressGen2X4", 174),
          ("systemSlotIsPCIExpressGen2X8", 175),
          ("systemSlotIsPCIExpressGen2X16", 176),
          ("systemSlotIsPCIExpressGen3", 177),
          ("systemSlotIsPCIExpressGen3X1", 178),
          ("systemSlotIsPCIExpressGen3X2", 179),
          ("systemSlotIsPCIExpressGen3X4", 180),
          ("systemSlotIsPCIExpressGen3X8", 181),
          ("systemSlotIsPCIExpressGen3X16", 182),
          ("systemSlotIsPCIExpressGen4", 184),
          ("systemSlotIsPCIExpressGen4X1", 185),
          ("systemSlotIsPCIExpressGen4X2", 186),
          ("systemSlotIsPCIExpressGen4X4", 187),
          ("systemSlotIsPCIExpressGen4X8", 188),
          ("systemSlotIsPCIExpressGen4X16", 189))
    )





class DellSystemSlotUsage(Integer32):
    """Custom type DellSystemSlotUsage based on Integer32"""
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
        *(("systemSlotUsageIsOther", 1),
          ("systemSlotUsageIsUnknown", 2),
          ("systemSlotUsageIsAvailable", 3),
          ("systemSlotUsageIsInUse", 4),
          ("systemSlotUsageIsUnAvailable", 5))
    )





class DellSystemSlotLength(Integer32):
    """Custom type DellSystemSlotLength based on Integer32"""
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
        *(("systemSlotLengthIsOther", 1),
          ("systemSlotLengthIsUnknown", 2),
          ("systemSlotLengthIsShort", 3),
          ("systemSlotLengthIsLong", 4),
          ("systemSlotLengthIs25dff", 5),
          ("systemSlotLengthIs35dff", 6))
    )





class DellSystemSlotCategory(Integer32):
    """Custom type DellSystemSlotCategory based on Integer32"""
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
        *(("systemSlotCategoryIsOther", 1),
          ("systemSlotCategoryIsUnknown", 2),
          ("systemSlotCategoryIsBusConnector", 3),
          ("systemSlotCategoryIsPCMCIA", 4),
          ("systemSlotCategoryIsMotherboard", 5))
    )





class DellSystemSlotHotPlugBusWidth(Integer32):
    """Custom type DellSystemSlotHotPlugBusWidth based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("busWidthIsOther", 1),
          ("busWidthIsUnknown", 2),
          ("busWidthIs8bits", 3),
          ("busWidthIs16bits", 4),
          ("busWidthIs32bits", 5),
          ("busWidthIs64bits", 6),
          ("busWidthIs128bits", 7),
          ("busWidthIs1xOrx1", 8),
          ("busWidthIs2xOrx2", 9),
          ("busWidthIs4xOrx4", 10),
          ("busWidthIs8xOrx8", 11),
          ("busWidthIs12xOrx12", 12),
          ("busWidthIs16xOrx16", 13),
          ("busWidthIs32xOrx32", 14))
    )





class DellPhysicalMemoryArrayLocation(Integer32):
    """Custom type DellPhysicalMemoryArrayLocation based on Integer32"""
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
        *(("memoryArrayLocationIsOther", 1),
          ("memoryArrayLocationIsUnknown", 2),
          ("memoryArrayLocationIsSystemOrMotherboard", 3),
          ("memoryArrayLocationIsISA", 4),
          ("memoryArrayLocationIsEISA", 5),
          ("memoryArrayLocationIsPCI", 6),
          ("memoryArrayLocationIsMCA", 7),
          ("memoryArrayLocationIsPCMCIA", 8),
          ("memoryArrayLocationIsProprietary", 9),
          ("memoryArrayLocationIsNUBUS", 10),
          ("memoryArrayLocationIsPC98C20", 11),
          ("memoryArrayLocationIsPC98C24", 12),
          ("memoryArrayLocationIsPC98E", 13),
          ("memoryArrayLocationIsPC98LocalBus", 14),
          ("memoryArrayLocationIsPC98Card", 15))
    )





class DellPhysicalMemoryArrayUse(Integer32):
    """Custom type DellPhysicalMemoryArrayUse based on Integer32"""
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
        *(("memoryArrayUseIsOther", 1),
          ("memoryArrayUseIsUnknown", 2),
          ("memoryArrayUseIsSystemMemory", 3),
          ("memoryArrayUseIsVideoMemory", 4),
          ("memoryArrayUseIsFLASHMemory", 5),
          ("memoryArrayUseIsNonVolatileRAMMemory", 6),
          ("memoryArrayUseIsCacheMemory", 7))
    )





class DellPhysicalMemoryArrayECCType(Integer32):
    """Custom type DellPhysicalMemoryArrayECCType based on Integer32"""
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
        *(("memoryArrayECCTypeIsOther", 1),
          ("memoryArrayECCTypeIsUnknown", 2),
          ("memoryArrayECCTypeIsNone", 3),
          ("memoryArrayECCTypeIsParity", 4),
          ("memoryArrayECCTypeIsSingleBitECC", 5),
          ("memoryArrayECCTypeIsMultiBitECC", 6),
          ("memoryArrayECCTypeIsCRC", 7))
    )





class DellPhysicalMemoryConfigStateCapabilities(Integer32):
    """Custom type DellPhysicalMemoryConfigStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2),
          ("notReadyCapable", 4))
    )





class DellPhysicalMemoryConfigStateSettings(Integer32):
    """Custom type DellPhysicalMemoryConfigStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("notReady", 4),
          ("redundantMemoryIsActive", 8),
          ("enabledAndRedundantMemoryIsActive", 10))
    )





class DellPhysicalMemoryConfigRedundantCapabilities(Integer32):
    """Custom type DellPhysicalMemoryConfigRedundantCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("spareCapable", 2),
          ("mirrorCapable", 4),
          ("spareAndMirrorCapable", 6),
          ("raidCapable", 8),
          ("dddcCapable", 16))
    )





class DellPhysicalMemoryConfigRedundantSettings(Integer32):
    """Custom type DellPhysicalMemoryConfigRedundantSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("spareEnabled", 2),
          ("mirrorEnabled", 4),
          ("raidEnabled", 8),
          ("dddcEnabled", 16))
    )





class DellPhysicalMemoryConfigMOMCapabilities(Integer32):
    """Custom type DellPhysicalMemoryConfigMOMCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("momOptimizerCapable", 2),
          ("momSpareCapable", 4),
          ("momMirrorCapable", 8),
          ("momAdvancedECCCapable", 16))
    )





class DellPhysicalMemoryConfigMOMSettings(Integer32):
    """Custom type DellPhysicalMemoryConfigMOMSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("momOptimizerEnabled", 2),
          ("momSpareEnabled", 4),
          ("momMirrorEnabled", 8),
          ("momAdvancedECCEnabled", 16))
    )





class DellPhysicalMemoryLoggingCapabilities(Integer32):
    """Custom type DellPhysicalMemoryLoggingCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2))
    )





class DellPhysicalMemoryLoggingSettings(Integer32):
    """Custom type DellPhysicalMemoryLoggingSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2))
    )





class DellSpeakerControlCapabilitiesUnique(Integer32):
    """Custom type DellSpeakerControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              30)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enableCapable", 2),
          ("lowCapable", 4),
          ("mediumCapable", 8),
          ("highCapable", 16),
          ("allVolumeCapable", 30))
    )





class DellSpeakerControlSettingsUnique(Integer32):
    """Custom type DellSpeakerControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("low", 4),
          ("medium", 8),
          ("high", 16))
    )





class DellNIFwakeonLanControlCapabilitiesUnique(Integer32):
    """Custom type DellNIFwakeonLanControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enableCapable", 2),
          ("addInCardCapable", 4),
          ("onBoardCapable", 8),
          ("bothCapable", 14))
    )





class DellNIFwakeonLanControlSettingsUnique(Integer32):
    """Custom type DellNIFwakeonLanControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("addInCard", 4),
          ("onBoard", 8),
          ("addInCardOrOnBoard", 12))
    )





class DellBootSequenceControlCapabilitiesUnique(Integer32):
    """Custom type DellBootSequenceControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              16,
              30)
        )
    )
    namedValues = NamedValues(
        *(("bootSequenceUnknown", 1),
          ("bootFromDisketteFirstCapable", 2),
          ("bootFromHardDriveFirstCapable", 4),
          ("bootFromDisketteORHardDriveFirstCapable", 6),
          ("bootFromDeviceListCapable", 8),
          ("bootFromCDROMFirstCapable", 16),
          ("allFirstCapable", 30))
    )





class DellBootSequenceControlSettingsUnique(Integer32):
    """Custom type DellBootSequenceControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bootSequenceUnknown", 1),
          ("bootFromDisketteFirst", 2),
          ("bootFromHardDriveFirst", 4),
          ("bootFromDeviceList", 8),
          ("bootFromCDROMFirst", 16))
    )





class DellBIOSPasswordControlCapabilitiesUnique(Integer32):
    """Custom type DellBIOSPasswordControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("passwordControlCapabilitiesUnknown", 1),
          ("passwordControlEnableCapable", 2),
          ("passwordControlJumperDisableCapable", 4),
          ("passwordControlEnableAndJumperDisableCapable", 6))
    )





class DellBIOSPasswordControlSettingsUnique(Integer32):
    """Custom type DellBIOSPasswordControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("passwordControlSettingsUnknown", 1),
          ("passwordControlEnabled", 2),
          ("passwordControlJumperDisabled", 4))
    )





class DellTPMSecurityControlCapabilities(Integer32):
    """Custom type DellTPMSecurityControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("offCapable", 1),
          ("onWithPrebootMeasurementsCapable", 2),
          ("onWithoutPrebootMeasurementsCapable", 4))
    )





class DellTPMSecurityControlSetting(Integer32):
    """Custom type DellTPMSecurityControlSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onWithPrebootMeasurements", 1),
          ("onWithoutPrebootMeasurements", 2))
    )





class DellParallelPortControlCapabilitiesUnique(Integer32):
    """Custom type DellParallelPortControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18,
              30)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enableCapable", 2),
          ("lpt1Capable", 4),
          ("lpt1andEnableCapable", 6),
          ("lpt2Capable", 8),
          ("lpt2andEnableCapable", 10),
          ("lpt3Capable", 16),
          ("lpt3andEnableCapable", 18),
          ("allParallelPortCapable", 30))
    )





class DellParallelPortControlSettingsUnique(Integer32):
    """Custom type DellParallelPortControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("lpt1", 4),
          ("lpt1Enabled", 6),
          ("lpt2", 8),
          ("lpt2Enabled", 10),
          ("lpt3", 16),
          ("lpt3Enabled", 18))
    )





class DellParallelPortControlModeCapabilitiesUnique(Integer32):
    """Custom type DellParallelPortControlModeCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              16,
              30)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("atCapable", 2),
          ("ps2Capable", 4),
          ("atAndPS2Capable", 6),
          ("ecpCapable", 8),
          ("eppCapable", 16),
          ("allModeCapable", 30))
    )





class DellParallelPortControlModeSettingsUnique(Integer32):
    """Custom type DellParallelPortControlModeSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("atModeEnabled", 2),
          ("ps2ModeEnabled", 4),
          ("ecpModeEnabled", 8),
          ("eppModeEnabled", 16))
    )





class DellSerialPortControlCapabilitiesUnique(Integer32):
    """Custom type DellSerialPortControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18,
              32,
              34,
              64,
              86,
              106,
              126)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enableCapable", 2),
          ("com1Capable", 4),
          ("enableAndCom1Capable", 6),
          ("com2Capable", 8),
          ("enableAndCom2Capable", 10),
          ("com3Capable", 16),
          ("enableAndCom3Capable", 18),
          ("com4Capable", 32),
          ("enableAndCom4Capable", 34),
          ("autoConfigCapable", 64),
          ("com1OrCom3CapableAndAutoConfigCapable", 86),
          ("com2OrCom4CapableAndAutoConfigCapable", 106),
          ("allcomCapable", 126))
    )





class DellSerialPortControlSettingsUnique(Integer32):
    """Custom type DellSerialPortControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18,
              32,
              34,
              64,
              66)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("com1", 4),
          ("com1Enabled", 6),
          ("com2", 8),
          ("com2Enabled", 10),
          ("com3", 16),
          ("com3Enabled", 18),
          ("com4", 32),
          ("com4Enabled", 34),
          ("comPortsAutoConfig", 64),
          ("enabledAndAutoConfig", 66))
    )





class DellideControlCapabilitiesUnique(Integer32):
    """Custom type DellideControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ideControlAutoConfigOrEnableCapable", 2))
    )





class DellideControlSettingsUnique(Integer32):
    """Custom type DellideControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ideControlAutoConfigEnabledOrEnabled", 2))
    )





class DellDisketteControlCapabilitiesUnique(Integer32):
    """Custom type DellDisketteControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disketteAutoConfigOrEnableCapable", 2),
          ("disketteReadOnlyCapable", 4),
          ("disketteAutoConfigOrEnableCapableandReadOnlyCapable", 6))
    )





class DellDisketteControlSettingsUnique(Integer32):
    """Custom type DellDisketteControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disketteAutoConfigEnabledOrEnabled", 2),
          ("disketteisReadOnly", 4))
    )





class DellNetworkInterfaceControlCapabilitiesUnique(Integer32):
    """Custom type DellNetworkInterfaceControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enableCapable", 2),
          ("enableWithoutPXECapable", 4))
    )





class DellNetworkInterfaceControlSettingsUnique(Integer32):
    """Custom type DellNetworkInterfaceControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("enabledWithoutPXE", 4))
    )





class DellBIOSSettingValueType(Integer32):
    """Custom type DellBIOSSettingValueType based on Integer32"""
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
        *(("integer", 1),
          ("string", 2),
          ("enumeration", 3),
          ("orderedList", 4))
    )





class DellLocalResponseAgentCapabilitiesUnique(Integer32):
    """Custom type DellLocalResponseAgentCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              256,
              383)
        )
    )
    namedValues = NamedValues(
        *(("speakerControlCapable", 1),
          ("consoleAlertCapable", 2),
          ("broadcastMessageCapable", 4),
          ("osShutDownCapable", 8),
          ("rebootCapable", 16),
          ("powerCycleCapable", 32),
          ("powerOFFCapable", 64),
          ("executeApplicationCapable", 256),
          ("lraFullyCapable", 383))
    )





class DellLRAThermalShutdownCapabilitiesUnique(Integer32):
    """Custom type DellLRAThermalShutdownCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknownCapabilities", 1),
          ("enableCapable", 2),
          ("warningCapable", 4),
          ("enableOnWarningCapable", 6),
          ("failureCapable", 8),
          ("enableOnFailureCapable", 10),
          ("enableOnWarningOrFailureCapable", 14))
    )





class DellLRAThermalShutdownStateSettingsUnique(Integer32):
    """Custom type DellLRAThermalShutdownStateSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("activatedOnWarning", 6),
          ("activatedOnFailure", 10))
    )





class DellLocalResponseAgentSettingsUnique(Integer32):
    """Custom type DellLocalResponseAgentSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              256,
              383)
        )
    )
    namedValues = NamedValues(
        *(("speakerControl", 1),
          ("consoleAlert", 2),
          ("broadcastMessage", 4),
          ("osShutDown", 8),
          ("reboot", 16),
          ("powerCycle", 32),
          ("powerOFF", 64),
          ("executeApplication", 256),
          ("allLRASettingsUnique", 383))
    )





class DellCooOwnershipCodes(Integer32):
    """Custom type DellCooOwnershipCodes based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("owned", 3),
          ("leased", 4),
          ("rented", 5),
          ("offOfLease", 6),
          ("transfer", 7))
    )





class DellCooHourDayDurationType(Integer32):
    """Custom type DellCooHourDayDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("hours", 2),
          ("days", 3))
    )





class DellCooDayMonthDurationType(Integer32):
    """Custom type DellCooDayMonthDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("days", 3),
          ("months", 4))
    )





class DellCooMonthYearDurationType(Integer32):
    """Custom type DellCooMonthYearDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("months", 4),
          ("years", 5))
    )





class DellClusterType(Integer32):
    """Custom type DellClusterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("highAvailabilityCluster", 2))
    )





class DellManagementControllerType(Integer32):
    """Custom type DellManagementControllerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              10,
              11,
              13,
              16,
              17,
              18,
              19,
              32,
              33,
              34,
              48,
              49,
              50)
        )
    )
    namedValues = NamedValues(
        *(("iDRAC", 8),
          ("iDRAC6", 10),
          ("iDRAC6Modular", 11),
          ("iDRAC6BMC", 13),
          ("iDRAC7", 16),
          ("iDRAC7Modular", 17),
          ("vrtxCMC", 18),
          ("fx2CMC", 19),
          ("iDRAC8", 32),
          ("iDRAC8Modular", 33),
          ("iDRAC8DCS", 34),
          ("iDRAC9", 48),
          ("iDRAC9Modular", 49),
          ("iDRAC9DCS", 50))
    )





class DellBladeFormFactorType(Integer32):
    """Custom type DellBladeFormFactorType based on Integer32"""
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("formFactorTypeIsSingleWidthHalfHeight", 1),
          ("formFactorTypeIsDualWidthHalfHeight", 2),
          ("formFactorTypeIsSingleWidthFullHeight", 3),
          ("formFactorTypeIsDualWidthFullHeight", 4),
          ("formFactorTypeIsSingleWidthQuarterHeight", 5),
          ("formFactorTypeIs1UHalfWidth", 6),
          ("formFactorTypeIs1UQuarterWidth", 7),
          ("formFactorTypeIs1UFullWidth", 8),
          ("notApplicable", 256))
    )





class DellBMCSerialConnectionModeCapabilities(Integer32):
    """Custom type DellBMCSerialConnectionModeCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("modemBasic", 1),
          ("modemPPP", 2),
          ("modemTerminal", 4),
          ("directBasic", 8),
          ("directPPP", 16),
          ("directTerminal", 32))
    )





class DellBMCSerialConnectionModeSettings(Integer32):
    """Custom type DellBMCSerialConnectionModeSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("modemBasic", 1),
          ("modemPPP", 2),
          ("modemTerminal", 4),
          ("directBasic", 8),
          ("directPPP", 16),
          ("directTerminal", 32))
    )





class DellBMCSerialFlowControlType(Integer32):
    """Custom type DellBMCSerialFlowControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtsCts", 1),
          ("xonXoff", 2))
    )





class DellBMCSerialBitRateType(Integer32):
    """Custom type DellBMCSerialBitRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bps9600", 6),
          ("bps19200", 7),
          ("bps38400", 8),
          ("bps57600", 9),
          ("bps115200", 10))
    )





class DellBMCLANIPAddressSourceType(Integer32):
    """Custom type DellBMCLANIPAddressSourceType based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("biosOrSystemSoftware", 3),
          ("other", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_BaseboardGroup_ObjectIdentity = ObjectIdentity
baseboardGroup = _BaseboardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1)
)
_MIBVersionGroup_ObjectIdentity = ObjectIdentity
mIBVersionGroup = _MIBVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1)
)
_MIBMajorVersionNumber_Type = DellUnsigned8BitRange
_MIBMajorVersionNumber_Object = MibScalar
mIBMajorVersionNumber = _MIBMajorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1, 1),
    _MIBMajorVersionNumber_Type()
)
mIBMajorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMajorVersionNumber.setStatus("mandatory")
_MIBMinorVersionNumber_Type = DellUnsigned8BitRange
_MIBMinorVersionNumber_Object = MibScalar
mIBMinorVersionNumber = _MIBMinorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1, 2),
    _MIBMinorVersionNumber_Type()
)
mIBMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMinorVersionNumber.setStatus("mandatory")
_MIBMaintenanceVersionNumber_Type = DellUnsigned8BitRange
_MIBMaintenanceVersionNumber_Object = MibScalar
mIBMaintenanceVersionNumber = _MIBMaintenanceVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1, 3),
    _MIBMaintenanceVersionNumber_Type()
)
mIBMaintenanceVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMaintenanceVersionNumber.setStatus("mandatory")
_SystemManagementSoftwareGroup_ObjectIdentity = ObjectIdentity
systemManagementSoftwareGroup = _SystemManagementSoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100)
)
_SystemManagementSoftwareName_Type = DellString
_SystemManagementSoftwareName_Object = MibScalar
systemManagementSoftwareName = _SystemManagementSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 1),
    _SystemManagementSoftwareName_Type()
)
systemManagementSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareName.setStatus("mandatory")
_SystemManagementSoftwareVersionNumberName_Type = DellString
_SystemManagementSoftwareVersionNumberName_Object = MibScalar
systemManagementSoftwareVersionNumberName = _SystemManagementSoftwareVersionNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 2),
    _SystemManagementSoftwareVersionNumberName_Type()
)
systemManagementSoftwareVersionNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareVersionNumberName.setStatus("mandatory")
_SystemManagementSoftwareBuildNumber_Type = DellUnsigned16BitRange
_SystemManagementSoftwareBuildNumber_Object = MibScalar
systemManagementSoftwareBuildNumber = _SystemManagementSoftwareBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 3),
    _SystemManagementSoftwareBuildNumber_Type()
)
systemManagementSoftwareBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareBuildNumber.setStatus("mandatory")
_SystemManagementSoftwareDescriptionName_Type = DellString
_SystemManagementSoftwareDescriptionName_Object = MibScalar
systemManagementSoftwareDescriptionName = _SystemManagementSoftwareDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 4),
    _SystemManagementSoftwareDescriptionName_Type()
)
systemManagementSoftwareDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareDescriptionName.setStatus("mandatory")
_SystemManagementSoftwareSupportedProtocol_Type = SMSSupportedTypes
_SystemManagementSoftwareSupportedProtocol_Object = MibScalar
systemManagementSoftwareSupportedProtocol = _SystemManagementSoftwareSupportedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 5),
    _SystemManagementSoftwareSupportedProtocol_Type()
)
systemManagementSoftwareSupportedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareSupportedProtocol.setStatus("mandatory")
_SystemManagementSoftwarePreferredProtocol_Type = SMSSupportedTypes
_SystemManagementSoftwarePreferredProtocol_Object = MibScalar
systemManagementSoftwarePreferredProtocol = _SystemManagementSoftwarePreferredProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 6),
    _SystemManagementSoftwarePreferredProtocol_Type()
)
systemManagementSoftwarePreferredProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwarePreferredProtocol.setStatus("mandatory")
_SystemManagementSoftwareUpdateLevelName_Type = DellString
_SystemManagementSoftwareUpdateLevelName_Object = MibScalar
systemManagementSoftwareUpdateLevelName = _SystemManagementSoftwareUpdateLevelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 7),
    _SystemManagementSoftwareUpdateLevelName_Type()
)
systemManagementSoftwareUpdateLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareUpdateLevelName.setStatus("mandatory")


class _SystemManagementSoftwareURLName_Type(DisplayString):
    """Custom type systemManagementSoftwareURLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SystemManagementSoftwareURLName_Type.__name__ = "DisplayString"
_SystemManagementSoftwareURLName_Object = MibScalar
systemManagementSoftwareURLName = _SystemManagementSoftwareURLName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 8),
    _SystemManagementSoftwareURLName_Type()
)
systemManagementSoftwareURLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareURLName.setStatus("mandatory")


class _SystemManagementSoftwareLanguageName_Type(DisplayString):
    """Custom type systemManagementSoftwareLanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemManagementSoftwareLanguageName_Type.__name__ = "DisplayString"
_SystemManagementSoftwareLanguageName_Object = MibScalar
systemManagementSoftwareLanguageName = _SystemManagementSoftwareLanguageName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 9),
    _SystemManagementSoftwareLanguageName_Type()
)
systemManagementSoftwareLanguageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareLanguageName.setStatus("mandatory")
_SystemManagementSoftwareGlobalVersionName_Type = DellString
_SystemManagementSoftwareGlobalVersionName_Object = MibScalar
systemManagementSoftwareGlobalVersionName = _SystemManagementSoftwareGlobalVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 10),
    _SystemManagementSoftwareGlobalVersionName_Type()
)
systemManagementSoftwareGlobalVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareGlobalVersionName.setStatus("mandatory")
_SystemManagementSoftwareFeatureFlags_Type = SMSFeatureFlags
_SystemManagementSoftwareFeatureFlags_Object = MibScalar
systemManagementSoftwareFeatureFlags = _SystemManagementSoftwareFeatureFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 11),
    _SystemManagementSoftwareFeatureFlags_Type()
)
systemManagementSoftwareFeatureFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareFeatureFlags.setStatus("mandatory")
_SystemManagementSoftwareSNMPAgentFeatureFlags_Type = SMSSNMPAgentFeatureFlags
_SystemManagementSoftwareSNMPAgentFeatureFlags_Object = MibScalar
systemManagementSoftwareSNMPAgentFeatureFlags = _SystemManagementSoftwareSNMPAgentFeatureFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 12),
    _SystemManagementSoftwareSNMPAgentFeatureFlags_Type()
)
systemManagementSoftwareSNMPAgentFeatureFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareSNMPAgentFeatureFlags.setStatus("mandatory")
_SystemManagementSoftwareManufacturerName_Type = DellString
_SystemManagementSoftwareManufacturerName_Object = MibScalar
systemManagementSoftwareManufacturerName = _SystemManagementSoftwareManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 13),
    _SystemManagementSoftwareManufacturerName_Type()
)
systemManagementSoftwareManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareManufacturerName.setStatus("mandatory")
_SystemManagementSoftwareProdUseFeedback_Type = DellUnsigned16BitRange
_SystemManagementSoftwareProdUseFeedback_Object = MibScalar
systemManagementSoftwareProdUseFeedback = _SystemManagementSoftwareProdUseFeedback_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 14),
    _SystemManagementSoftwareProdUseFeedback_Type()
)
systemManagementSoftwareProdUseFeedback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareProdUseFeedback.setStatus("mandatory")
_SystemStateGroup_ObjectIdentity = ObjectIdentity
systemStateGroup = _SystemStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200)
)
_SystemStateTable_Object = MibTable
systemStateTable = _SystemStateTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10)
)
if mibBuilder.loadTexts:
    systemStateTable.setStatus("mandatory")
_SystemStateTableEntry_Object = MibTableRow
systemStateTableEntry = _SystemStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1)
)
systemStateTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemStatechassisIndex"),
)
if mibBuilder.loadTexts:
    systemStateTableEntry.setStatus("mandatory")
_SystemStatechassisIndex_Type = DellObjectRange
_SystemStatechassisIndex_Object = MibTableColumn
systemStatechassisIndex = _SystemStatechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 1),
    _SystemStatechassisIndex_Type()
)
systemStatechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatechassisIndex.setStatus("mandatory")
_SystemStateGlobalSystemStatus_Type = DellStatus
_SystemStateGlobalSystemStatus_Object = MibTableColumn
systemStateGlobalSystemStatus = _SystemStateGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 2),
    _SystemStateGlobalSystemStatus_Type()
)
systemStateGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateGlobalSystemStatus.setStatus("mandatory")
_SystemStateChassisState_Type = DellStateSettings
_SystemStateChassisState_Object = MibTableColumn
systemStateChassisState = _SystemStateChassisState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 3),
    _SystemStateChassisState_Type()
)
systemStateChassisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisState.setStatus("mandatory")
_SystemStateChassisStatus_Type = DellStatus
_SystemStateChassisStatus_Object = MibTableColumn
systemStateChassisStatus = _SystemStateChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 4),
    _SystemStateChassisStatus_Type()
)
systemStateChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisStatus.setStatus("mandatory")


class _SystemStatePowerUnitStateDetails_Type(OctetString):
    """Custom type systemStatePowerUnitStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStateDetails_Type.__name__ = "OctetString"
_SystemStatePowerUnitStateDetails_Object = MibTableColumn
systemStatePowerUnitStateDetails = _SystemStatePowerUnitStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 5),
    _SystemStatePowerUnitStateDetails_Type()
)
systemStatePowerUnitStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStateDetails.setStatus("mandatory")
_SystemStatePowerUnitStatusRedundancy_Type = DellStatusRedundancy
_SystemStatePowerUnitStatusRedundancy_Object = MibTableColumn
systemStatePowerUnitStatusRedundancy = _SystemStatePowerUnitStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 6),
    _SystemStatePowerUnitStatusRedundancy_Type()
)
systemStatePowerUnitStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusRedundancy.setStatus("mandatory")


class _SystemStatePowerUnitStatusDetails_Type(OctetString):
    """Custom type systemStatePowerUnitStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStatusDetails_Type.__name__ = "OctetString"
_SystemStatePowerUnitStatusDetails_Object = MibTableColumn
systemStatePowerUnitStatusDetails = _SystemStatePowerUnitStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 7),
    _SystemStatePowerUnitStatusDetails_Type()
)
systemStatePowerUnitStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusDetails.setStatus("mandatory")


class _SystemStatePowerSupplyStateDetails_Type(OctetString):
    """Custom type systemStatePowerSupplyStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerSupplyStateDetails_Type.__name__ = "OctetString"
_SystemStatePowerSupplyStateDetails_Object = MibTableColumn
systemStatePowerSupplyStateDetails = _SystemStatePowerSupplyStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 8),
    _SystemStatePowerSupplyStateDetails_Type()
)
systemStatePowerSupplyStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStateDetails.setStatus("mandatory")
_SystemStatePowerSupplyStatusCombined_Type = DellStatus
_SystemStatePowerSupplyStatusCombined_Object = MibTableColumn
systemStatePowerSupplyStatusCombined = _SystemStatePowerSupplyStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 9),
    _SystemStatePowerSupplyStatusCombined_Type()
)
systemStatePowerSupplyStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusCombined.setStatus("mandatory")


class _SystemStatePowerSupplyStatusDetails_Type(OctetString):
    """Custom type systemStatePowerSupplyStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerSupplyStatusDetails_Type.__name__ = "OctetString"
_SystemStatePowerSupplyStatusDetails_Object = MibTableColumn
systemStatePowerSupplyStatusDetails = _SystemStatePowerSupplyStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 10),
    _SystemStatePowerSupplyStatusDetails_Type()
)
systemStatePowerSupplyStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusDetails.setStatus("mandatory")


class _SystemStateVoltageStateDetails_Type(OctetString):
    """Custom type systemStateVoltageStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateVoltageStateDetails_Type.__name__ = "OctetString"
_SystemStateVoltageStateDetails_Object = MibTableColumn
systemStateVoltageStateDetails = _SystemStateVoltageStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 11),
    _SystemStateVoltageStateDetails_Type()
)
systemStateVoltageStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStateDetails.setStatus("mandatory")
_SystemStateVoltageStatusCombined_Type = DellStatus
_SystemStateVoltageStatusCombined_Object = MibTableColumn
systemStateVoltageStatusCombined = _SystemStateVoltageStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 12),
    _SystemStateVoltageStatusCombined_Type()
)
systemStateVoltageStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStatusCombined.setStatus("mandatory")


class _SystemStateVoltageStatusDetails_Type(OctetString):
    """Custom type systemStateVoltageStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateVoltageStatusDetails_Type.__name__ = "OctetString"
_SystemStateVoltageStatusDetails_Object = MibTableColumn
systemStateVoltageStatusDetails = _SystemStateVoltageStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 13),
    _SystemStateVoltageStatusDetails_Type()
)
systemStateVoltageStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStatusDetails.setStatus("mandatory")


class _SystemStateAmperageStateDetails_Type(OctetString):
    """Custom type systemStateAmperageStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateAmperageStateDetails_Type.__name__ = "OctetString"
_SystemStateAmperageStateDetails_Object = MibTableColumn
systemStateAmperageStateDetails = _SystemStateAmperageStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 14),
    _SystemStateAmperageStateDetails_Type()
)
systemStateAmperageStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStateDetails.setStatus("mandatory")
_SystemStateAmperageStatusCombined_Type = DellStatus
_SystemStateAmperageStatusCombined_Object = MibTableColumn
systemStateAmperageStatusCombined = _SystemStateAmperageStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 15),
    _SystemStateAmperageStatusCombined_Type()
)
systemStateAmperageStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStatusCombined.setStatus("mandatory")


class _SystemStateAmperageStatusDetails_Type(OctetString):
    """Custom type systemStateAmperageStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateAmperageStatusDetails_Type.__name__ = "OctetString"
_SystemStateAmperageStatusDetails_Object = MibTableColumn
systemStateAmperageStatusDetails = _SystemStateAmperageStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 16),
    _SystemStateAmperageStatusDetails_Type()
)
systemStateAmperageStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStatusDetails.setStatus("mandatory")


class _SystemStateCoolingUnitStateDetails_Type(OctetString):
    """Custom type systemStateCoolingUnitStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStateDetails_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStateDetails_Object = MibTableColumn
systemStateCoolingUnitStateDetails = _SystemStateCoolingUnitStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 17),
    _SystemStateCoolingUnitStateDetails_Type()
)
systemStateCoolingUnitStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStateDetails.setStatus("mandatory")
_SystemStateCoolingUnitStatusRedundancy_Type = DellStatusRedundancy
_SystemStateCoolingUnitStatusRedundancy_Object = MibTableColumn
systemStateCoolingUnitStatusRedundancy = _SystemStateCoolingUnitStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 18),
    _SystemStateCoolingUnitStatusRedundancy_Type()
)
systemStateCoolingUnitStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusRedundancy.setStatus("mandatory")


class _SystemStateCoolingUnitStatusDetails_Type(OctetString):
    """Custom type systemStateCoolingUnitStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStatusDetails_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStatusDetails_Object = MibTableColumn
systemStateCoolingUnitStatusDetails = _SystemStateCoolingUnitStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 19),
    _SystemStateCoolingUnitStatusDetails_Type()
)
systemStateCoolingUnitStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusDetails.setStatus("mandatory")


class _SystemStateCoolingDeviceStateDetails_Type(OctetString):
    """Custom type systemStateCoolingDeviceStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingDeviceStateDetails_Type.__name__ = "OctetString"
_SystemStateCoolingDeviceStateDetails_Object = MibTableColumn
systemStateCoolingDeviceStateDetails = _SystemStateCoolingDeviceStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 20),
    _SystemStateCoolingDeviceStateDetails_Type()
)
systemStateCoolingDeviceStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStateDetails.setStatus("mandatory")
_SystemStateCoolingDeviceStatusCombined_Type = DellStatus
_SystemStateCoolingDeviceStatusCombined_Object = MibTableColumn
systemStateCoolingDeviceStatusCombined = _SystemStateCoolingDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 21),
    _SystemStateCoolingDeviceStatusCombined_Type()
)
systemStateCoolingDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusCombined.setStatus("mandatory")


class _SystemStateCoolingDeviceStatusDetails_Type(OctetString):
    """Custom type systemStateCoolingDeviceStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingDeviceStatusDetails_Type.__name__ = "OctetString"
_SystemStateCoolingDeviceStatusDetails_Object = MibTableColumn
systemStateCoolingDeviceStatusDetails = _SystemStateCoolingDeviceStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 22),
    _SystemStateCoolingDeviceStatusDetails_Type()
)
systemStateCoolingDeviceStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusDetails.setStatus("mandatory")


class _SystemStateTemperatureStateDetails_Type(OctetString):
    """Custom type systemStateTemperatureStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStateDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStateDetails_Object = MibTableColumn
systemStateTemperatureStateDetails = _SystemStateTemperatureStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 23),
    _SystemStateTemperatureStateDetails_Type()
)
systemStateTemperatureStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStateDetails.setStatus("mandatory")
_SystemStateTemperatureStatusCombined_Type = DellStatus
_SystemStateTemperatureStatusCombined_Object = MibTableColumn
systemStateTemperatureStatusCombined = _SystemStateTemperatureStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 24),
    _SystemStateTemperatureStatusCombined_Type()
)
systemStateTemperatureStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusCombined.setStatus("mandatory")


class _SystemStateTemperatureStatusDetails_Type(OctetString):
    """Custom type systemStateTemperatureStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStatusDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStatusDetails_Object = MibTableColumn
systemStateTemperatureStatusDetails = _SystemStateTemperatureStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 25),
    _SystemStateTemperatureStatusDetails_Type()
)
systemStateTemperatureStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusDetails.setStatus("mandatory")


class _SystemStateMemoryDeviceStateDetails_Type(OctetString):
    """Custom type systemStateMemoryDeviceStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateMemoryDeviceStateDetails_Type.__name__ = "OctetString"
_SystemStateMemoryDeviceStateDetails_Object = MibTableColumn
systemStateMemoryDeviceStateDetails = _SystemStateMemoryDeviceStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 26),
    _SystemStateMemoryDeviceStateDetails_Type()
)
systemStateMemoryDeviceStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStateDetails.setStatus("mandatory")
_SystemStateMemoryDeviceStatusCombined_Type = DellStatus
_SystemStateMemoryDeviceStatusCombined_Object = MibTableColumn
systemStateMemoryDeviceStatusCombined = _SystemStateMemoryDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 27),
    _SystemStateMemoryDeviceStatusCombined_Type()
)
systemStateMemoryDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusCombined.setStatus("mandatory")


class _SystemStateMemoryDeviceStatusDetails_Type(OctetString):
    """Custom type systemStateMemoryDeviceStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateMemoryDeviceStatusDetails_Type.__name__ = "OctetString"
_SystemStateMemoryDeviceStatusDetails_Object = MibTableColumn
systemStateMemoryDeviceStatusDetails = _SystemStateMemoryDeviceStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 28),
    _SystemStateMemoryDeviceStatusDetails_Type()
)
systemStateMemoryDeviceStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusDetails.setStatus("mandatory")


class _SystemStateChassisIntrusionStateDetails_Type(OctetString):
    """Custom type systemStateChassisIntrusionStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateChassisIntrusionStateDetails_Type.__name__ = "OctetString"
_SystemStateChassisIntrusionStateDetails_Object = MibTableColumn
systemStateChassisIntrusionStateDetails = _SystemStateChassisIntrusionStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 29),
    _SystemStateChassisIntrusionStateDetails_Type()
)
systemStateChassisIntrusionStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStateDetails.setStatus("mandatory")
_SystemStateChassisIntrusionStatusCombined_Type = DellStatus
_SystemStateChassisIntrusionStatusCombined_Object = MibTableColumn
systemStateChassisIntrusionStatusCombined = _SystemStateChassisIntrusionStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 30),
    _SystemStateChassisIntrusionStatusCombined_Type()
)
systemStateChassisIntrusionStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusCombined.setStatus("mandatory")


class _SystemStateChassisIntrusionStatusDetails_Type(OctetString):
    """Custom type systemStateChassisIntrusionStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateChassisIntrusionStatusDetails_Type.__name__ = "OctetString"
_SystemStateChassisIntrusionStatusDetails_Object = MibTableColumn
systemStateChassisIntrusionStatusDetails = _SystemStateChassisIntrusionStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 31),
    _SystemStateChassisIntrusionStatusDetails_Type()
)
systemStateChassisIntrusionStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusDetails.setStatus("mandatory")


class _SystemStateACPowerSwitchStateDetails_Type(OctetString):
    """Custom type systemStateACPowerSwitchStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerSwitchStateDetails_Type.__name__ = "OctetString"
_SystemStateACPowerSwitchStateDetails_Object = MibTableColumn
systemStateACPowerSwitchStateDetails = _SystemStateACPowerSwitchStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 32),
    _SystemStateACPowerSwitchStateDetails_Type()
)
systemStateACPowerSwitchStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStateDetails.setStatus("mandatory")
_SystemStateACPowerSwitchStatusRedundancy_Type = DellStatusRedundancy
_SystemStateACPowerSwitchStatusRedundancy_Object = MibTableColumn
systemStateACPowerSwitchStatusRedundancy = _SystemStateACPowerSwitchStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 33),
    _SystemStateACPowerSwitchStatusRedundancy_Type()
)
systemStateACPowerSwitchStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusRedundancy.setStatus("mandatory")


class _SystemStateACPowerSwitchStatusDetails_Type(OctetString):
    """Custom type systemStateACPowerSwitchStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerSwitchStatusDetails_Type.__name__ = "OctetString"
_SystemStateACPowerSwitchStatusDetails_Object = MibTableColumn
systemStateACPowerSwitchStatusDetails = _SystemStateACPowerSwitchStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 34),
    _SystemStateACPowerSwitchStatusDetails_Type()
)
systemStateACPowerSwitchStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusDetails.setStatus("mandatory")


class _SystemStateACPowerCordStateDetails_Type(OctetString):
    """Custom type systemStateACPowerCordStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerCordStateDetails_Type.__name__ = "OctetString"
_SystemStateACPowerCordStateDetails_Object = MibTableColumn
systemStateACPowerCordStateDetails = _SystemStateACPowerCordStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 35),
    _SystemStateACPowerCordStateDetails_Type()
)
systemStateACPowerCordStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerCordStateDetails.setStatus("mandatory")
_SystemStateACPowerCordStatusCombined_Type = DellStatus
_SystemStateACPowerCordStatusCombined_Object = MibTableColumn
systemStateACPowerCordStatusCombined = _SystemStateACPowerCordStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 36),
    _SystemStateACPowerCordStatusCombined_Type()
)
systemStateACPowerCordStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerCordStatusCombined.setStatus("mandatory")


class _SystemStateACPowerCordStatusDetails_Type(OctetString):
    """Custom type systemStateACPowerCordStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerCordStatusDetails_Type.__name__ = "OctetString"
_SystemStateACPowerCordStatusDetails_Object = MibTableColumn
systemStateACPowerCordStatusDetails = _SystemStateACPowerCordStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 37),
    _SystemStateACPowerCordStatusDetails_Type()
)
systemStateACPowerCordStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerCordStatusDetails.setStatus("mandatory")


class _SystemStateRedundantMemoryUnitStateDetails_Type(OctetString):
    """Custom type systemStateRedundantMemoryUnitStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateRedundantMemoryUnitStateDetails_Type.__name__ = "OctetString"
_SystemStateRedundantMemoryUnitStateDetails_Object = MibTableColumn
systemStateRedundantMemoryUnitStateDetails = _SystemStateRedundantMemoryUnitStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 38),
    _SystemStateRedundantMemoryUnitStateDetails_Type()
)
systemStateRedundantMemoryUnitStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateRedundantMemoryUnitStateDetails.setStatus("mandatory")
_SystemStateRedundantMemoryUnitStatusRedundancy_Type = DellStatusRedundancy
_SystemStateRedundantMemoryUnitStatusRedundancy_Object = MibTableColumn
systemStateRedundantMemoryUnitStatusRedundancy = _SystemStateRedundantMemoryUnitStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 39),
    _SystemStateRedundantMemoryUnitStatusRedundancy_Type()
)
systemStateRedundantMemoryUnitStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateRedundantMemoryUnitStatusRedundancy.setStatus("mandatory")


class _SystemStateRedundantMemoryUnitStatusDetails_Type(OctetString):
    """Custom type systemStateRedundantMemoryUnitStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateRedundantMemoryUnitStatusDetails_Type.__name__ = "OctetString"
_SystemStateRedundantMemoryUnitStatusDetails_Object = MibTableColumn
systemStateRedundantMemoryUnitStatusDetails = _SystemStateRedundantMemoryUnitStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 40),
    _SystemStateRedundantMemoryUnitStatusDetails_Type()
)
systemStateRedundantMemoryUnitStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateRedundantMemoryUnitStatusDetails.setStatus("mandatory")
_SystemStateEventLogStatus_Type = DellStatus
_SystemStateEventLogStatus_Object = MibTableColumn
systemStateEventLogStatus = _SystemStateEventLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 41),
    _SystemStateEventLogStatus_Type()
)
systemStateEventLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateEventLogStatus.setStatus("mandatory")
_SystemStatePowerUnitStatusCombined_Type = DellStatus
_SystemStatePowerUnitStatusCombined_Object = MibTableColumn
systemStatePowerUnitStatusCombined = _SystemStatePowerUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 42),
    _SystemStatePowerUnitStatusCombined_Type()
)
systemStatePowerUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusCombined.setStatus("mandatory")


class _SystemStatePowerUnitStatusList_Type(OctetString):
    """Custom type systemStatePowerUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStatusList_Type.__name__ = "OctetString"
_SystemStatePowerUnitStatusList_Object = MibTableColumn
systemStatePowerUnitStatusList = _SystemStatePowerUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 43),
    _SystemStatePowerUnitStatusList_Type()
)
systemStatePowerUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusList.setStatus("mandatory")
_SystemStateCoolingUnitStatusCombined_Type = DellStatus
_SystemStateCoolingUnitStatusCombined_Object = MibTableColumn
systemStateCoolingUnitStatusCombined = _SystemStateCoolingUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 44),
    _SystemStateCoolingUnitStatusCombined_Type()
)
systemStateCoolingUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusCombined.setStatus("mandatory")


class _SystemStateCoolingUnitStatusList_Type(OctetString):
    """Custom type systemStateCoolingUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStatusList_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStatusList_Object = MibTableColumn
systemStateCoolingUnitStatusList = _SystemStateCoolingUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 45),
    _SystemStateCoolingUnitStatusList_Type()
)
systemStateCoolingUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusList.setStatus("mandatory")
_SystemStateACPowerSwitchStatusCombined_Type = DellStatus
_SystemStateACPowerSwitchStatusCombined_Object = MibTableColumn
systemStateACPowerSwitchStatusCombined = _SystemStateACPowerSwitchStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 46),
    _SystemStateACPowerSwitchStatusCombined_Type()
)
systemStateACPowerSwitchStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusCombined.setStatus("mandatory")


class _SystemStateACPowerSwitchStatusList_Type(OctetString):
    """Custom type systemStateACPowerSwitchStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerSwitchStatusList_Type.__name__ = "OctetString"
_SystemStateACPowerSwitchStatusList_Object = MibTableColumn
systemStateACPowerSwitchStatusList = _SystemStateACPowerSwitchStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 47),
    _SystemStateACPowerSwitchStatusList_Type()
)
systemStateACPowerSwitchStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusList.setStatus("mandatory")
_SystemStateRedundantMemoryUnitStatusCombined_Type = DellStatus
_SystemStateRedundantMemoryUnitStatusCombined_Object = MibTableColumn
systemStateRedundantMemoryUnitStatusCombined = _SystemStateRedundantMemoryUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 48),
    _SystemStateRedundantMemoryUnitStatusCombined_Type()
)
systemStateRedundantMemoryUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateRedundantMemoryUnitStatusCombined.setStatus("mandatory")


class _SystemStateRedundantMemoryUnitStatusList_Type(OctetString):
    """Custom type systemStateRedundantMemoryUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateRedundantMemoryUnitStatusList_Type.__name__ = "OctetString"
_SystemStateRedundantMemoryUnitStatusList_Object = MibTableColumn
systemStateRedundantMemoryUnitStatusList = _SystemStateRedundantMemoryUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 49),
    _SystemStateRedundantMemoryUnitStatusList_Type()
)
systemStateRedundantMemoryUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateRedundantMemoryUnitStatusList.setStatus("mandatory")
_SystemStateProcessorDeviceStatusCombined_Type = DellStatus
_SystemStateProcessorDeviceStatusCombined_Object = MibTableColumn
systemStateProcessorDeviceStatusCombined = _SystemStateProcessorDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 50),
    _SystemStateProcessorDeviceStatusCombined_Type()
)
systemStateProcessorDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateProcessorDeviceStatusCombined.setStatus("mandatory")


class _SystemStateProcessorDeviceStatusList_Type(OctetString):
    """Custom type systemStateProcessorDeviceStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateProcessorDeviceStatusList_Type.__name__ = "OctetString"
_SystemStateProcessorDeviceStatusList_Object = MibTableColumn
systemStateProcessorDeviceStatusList = _SystemStateProcessorDeviceStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 51),
    _SystemStateProcessorDeviceStatusList_Type()
)
systemStateProcessorDeviceStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateProcessorDeviceStatusList.setStatus("mandatory")
_SystemStateBatteryStatusCombined_Type = DellStatus
_SystemStateBatteryStatusCombined_Object = MibTableColumn
systemStateBatteryStatusCombined = _SystemStateBatteryStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 52),
    _SystemStateBatteryStatusCombined_Type()
)
systemStateBatteryStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateBatteryStatusCombined.setStatus("mandatory")


class _SystemStateBatteryStatusList_Type(OctetString):
    """Custom type systemStateBatteryStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateBatteryStatusList_Type.__name__ = "OctetString"
_SystemStateBatteryStatusList_Object = MibTableColumn
systemStateBatteryStatusList = _SystemStateBatteryStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 53),
    _SystemStateBatteryStatusList_Type()
)
systemStateBatteryStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateBatteryStatusList.setStatus("mandatory")
_SystemStateSDCardUnitStatusCombined_Type = DellStatus
_SystemStateSDCardUnitStatusCombined_Object = MibTableColumn
systemStateSDCardUnitStatusCombined = _SystemStateSDCardUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 54),
    _SystemStateSDCardUnitStatusCombined_Type()
)
systemStateSDCardUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardUnitStatusCombined.setStatus("mandatory")


class _SystemStateSDCardUnitStatusList_Type(OctetString):
    """Custom type systemStateSDCardUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateSDCardUnitStatusList_Type.__name__ = "OctetString"
_SystemStateSDCardUnitStatusList_Object = MibTableColumn
systemStateSDCardUnitStatusList = _SystemStateSDCardUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 55),
    _SystemStateSDCardUnitStatusList_Type()
)
systemStateSDCardUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardUnitStatusList.setStatus("mandatory")
_SystemStateSDCardDeviceStatusCombined_Type = DellStatus
_SystemStateSDCardDeviceStatusCombined_Object = MibTableColumn
systemStateSDCardDeviceStatusCombined = _SystemStateSDCardDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 56),
    _SystemStateSDCardDeviceStatusCombined_Type()
)
systemStateSDCardDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardDeviceStatusCombined.setStatus("mandatory")


class _SystemStateSDCardDeviceStatusList_Type(OctetString):
    """Custom type systemStateSDCardDeviceStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateSDCardDeviceStatusList_Type.__name__ = "OctetString"
_SystemStateSDCardDeviceStatusList_Object = MibTableColumn
systemStateSDCardDeviceStatusList = _SystemStateSDCardDeviceStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 57),
    _SystemStateSDCardDeviceStatusList_Type()
)
systemStateSDCardDeviceStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardDeviceStatusList.setStatus("mandatory")
_ChassisInformationGroup_ObjectIdentity = ObjectIdentity
chassisInformationGroup = _ChassisInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300)
)
_ChassisInformationTable_Object = MibTable
chassisInformationTable = _ChassisInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10)
)
if mibBuilder.loadTexts:
    chassisInformationTable.setStatus("mandatory")
_ChassisInformationTableEntry_Object = MibTableRow
chassisInformationTableEntry = _ChassisInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1)
)
chassisInformationTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "chassisIndexChassisInformation"),
)
if mibBuilder.loadTexts:
    chassisInformationTableEntry.setStatus("mandatory")
_ChassisIndexChassisInformation_Type = DellObjectRange
_ChassisIndexChassisInformation_Object = MibTableColumn
chassisIndexChassisInformation = _ChassisIndexChassisInformation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 1),
    _ChassisIndexChassisInformation_Type()
)
chassisIndexChassisInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIndexChassisInformation.setStatus("mandatory")
_ChassisStateCapabilities_Type = DellStateCapabilities
_ChassisStateCapabilities_Object = MibTableColumn
chassisStateCapabilities = _ChassisStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 2),
    _ChassisStateCapabilities_Type()
)
chassisStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStateCapabilities.setStatus("mandatory")
_ChassisStateSettings_Type = DellStateSettings
_ChassisStateSettings_Object = MibTableColumn
chassisStateSettings = _ChassisStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 3),
    _ChassisStateSettings_Type()
)
chassisStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStateSettings.setStatus("mandatory")
_ChassisStatus_Type = DellStatus
_ChassisStatus_Object = MibTableColumn
chassisStatus = _ChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 4),
    _ChassisStatus_Type()
)
chassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStatus.setStatus("mandatory")
_ChassisparentIndexReference_Type = DellObjectRange
_ChassisparentIndexReference_Object = MibTableColumn
chassisparentIndexReference = _ChassisparentIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 5),
    _ChassisparentIndexReference_Type()
)
chassisparentIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisparentIndexReference.setStatus("mandatory")
_ChassisType_Type = DellChassisType
_ChassisType_Object = MibTableColumn
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 6),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("mandatory")
_ChassisName_Type = DellString
_ChassisName_Object = MibTableColumn
chassisName = _ChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 7),
    _ChassisName_Type()
)
chassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisName.setStatus("mandatory")
_ChassisManufacturerName_Type = DellString
_ChassisManufacturerName_Object = MibTableColumn
chassisManufacturerName = _ChassisManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 8),
    _ChassisManufacturerName_Type()
)
chassisManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisManufacturerName.setStatus("mandatory")
_ChassisModelName_Type = DellString
_ChassisModelName_Object = MibTableColumn
chassisModelName = _ChassisModelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 9),
    _ChassisModelName_Type()
)
chassisModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModelName.setStatus("mandatory")


class _ChassisAssetTagName_Type(DisplayString):
    """Custom type chassisAssetTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ChassisAssetTagName_Type.__name__ = "DisplayString"
_ChassisAssetTagName_Object = MibTableColumn
chassisAssetTagName = _ChassisAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 10),
    _ChassisAssetTagName_Type()
)
chassisAssetTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisAssetTagName.setStatus("mandatory")


class _ChassisServiceTagName_Type(DisplayString):
    """Custom type chassisServiceTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChassisServiceTagName_Type.__name__ = "DisplayString"
_ChassisServiceTagName_Object = MibTableColumn
chassisServiceTagName = _ChassisServiceTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 11),
    _ChassisServiceTagName_Type()
)
chassisServiceTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisServiceTagName.setStatus("mandatory")
_ChassisID_Type = DellUnsigned8BitRange
_ChassisID_Object = MibTableColumn
chassisID = _ChassisID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 12),
    _ChassisID_Type()
)
chassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisID.setStatus("mandatory")
_ChassisIDExtension_Type = DellUnsigned16BitRange
_ChassisIDExtension_Object = MibTableColumn
chassisIDExtension = _ChassisIDExtension_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 13),
    _ChassisIDExtension_Type()
)
chassisIDExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIDExtension.setStatus("mandatory")
_ChassisSystemClass_Type = DellChassisSystemClass
_ChassisSystemClass_Object = MibTableColumn
chassisSystemClass = _ChassisSystemClass_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 14),
    _ChassisSystemClass_Type()
)
chassisSystemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemClass.setStatus("mandatory")
_ChassisSystemName_Type = DellString
_ChassisSystemName_Object = MibTableColumn
chassisSystemName = _ChassisSystemName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 15),
    _ChassisSystemName_Type()
)
chassisSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemName.setStatus("mandatory")
_ChassisSystemBootDateName_Type = DellDateName
_ChassisSystemBootDateName_Object = MibTableColumn
chassisSystemBootDateName = _ChassisSystemBootDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 16),
    _ChassisSystemBootDateName_Type()
)
chassisSystemBootDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemBootDateName.setStatus("mandatory")
_ChassisSystemDateName_Type = DellDateName
_ChassisSystemDateName_Object = MibTableColumn
chassisSystemDateName = _ChassisSystemDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 17),
    _ChassisSystemDateName_Type()
)
chassisSystemDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemDateName.setStatus("mandatory")
_ChassisSystemLocationName_Type = DellString
_ChassisSystemLocationName_Object = MibTableColumn
chassisSystemLocationName = _ChassisSystemLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 18),
    _ChassisSystemLocationName_Type()
)
chassisSystemLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemLocationName.setStatus("mandatory")
_ChassisSystemPrimaryUserName_Type = DellString
_ChassisSystemPrimaryUserName_Object = MibTableColumn
chassisSystemPrimaryUserName = _ChassisSystemPrimaryUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 19),
    _ChassisSystemPrimaryUserName_Type()
)
chassisSystemPrimaryUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemPrimaryUserName.setStatus("mandatory")
_ChassisSystemUserPhoneNumberName_Type = DellString
_ChassisSystemUserPhoneNumberName_Object = MibTableColumn
chassisSystemUserPhoneNumberName = _ChassisSystemUserPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 20),
    _ChassisSystemUserPhoneNumberName_Type()
)
chassisSystemUserPhoneNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemUserPhoneNumberName.setStatus("mandatory")
_ChassisConnectionStatusUnique_Type = DellConnectionStatus
_ChassisConnectionStatusUnique_Object = MibTableColumn
chassisConnectionStatusUnique = _ChassisConnectionStatusUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 21),
    _ChassisConnectionStatusUnique_Type()
)
chassisConnectionStatusUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisConnectionStatusUnique.setStatus("mandatory")
_ChassisFanControlCapabilitiesUnique_Type = DellFanControlCapabilities
_ChassisFanControlCapabilitiesUnique_Object = MibTableColumn
chassisFanControlCapabilitiesUnique = _ChassisFanControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 22),
    _ChassisFanControlCapabilitiesUnique_Type()
)
chassisFanControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanControlCapabilitiesUnique.setStatus("mandatory")
_ChassisFanControlSettingsUnique_Type = DellFanControlSettings
_ChassisFanControlSettingsUnique_Object = MibTableColumn
chassisFanControlSettingsUnique = _ChassisFanControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 23),
    _ChassisFanControlSettingsUnique_Type()
)
chassisFanControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanControlSettingsUnique.setStatus("mandatory")
_ChassisLEDControlCapabilitiesUnique_Type = DellLEDControlCapabilities
_ChassisLEDControlCapabilitiesUnique_Object = MibTableColumn
chassisLEDControlCapabilitiesUnique = _ChassisLEDControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 24),
    _ChassisLEDControlCapabilitiesUnique_Type()
)
chassisLEDControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLEDControlCapabilitiesUnique.setStatus("mandatory")
_ChassisLEDControlSettingsUnique_Type = DellLEDControlSettings
_ChassisLEDControlSettingsUnique_Object = MibTableColumn
chassisLEDControlSettingsUnique = _ChassisLEDControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 25),
    _ChassisLEDControlSettingsUnique_Type()
)
chassisLEDControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLEDControlSettingsUnique.setStatus("mandatory")
_ChassisHDFaultClearControlCapabilities_Type = DellHDFaultLEDControlCapabilities
_ChassisHDFaultClearControlCapabilities_Object = MibTableColumn
chassisHDFaultClearControlCapabilities = _ChassisHDFaultClearControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 26),
    _ChassisHDFaultClearControlCapabilities_Type()
)
chassisHDFaultClearControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHDFaultClearControlCapabilities.setStatus("mandatory")
_ChassisHDFaultClearControlSettings_Type = DellHDFaultLEDControlSettings
_ChassisHDFaultClearControlSettings_Object = MibTableColumn
chassisHDFaultClearControlSettings = _ChassisHDFaultClearControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 27),
    _ChassisHDFaultClearControlSettings_Type()
)
chassisHDFaultClearControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHDFaultClearControlSettings.setStatus("mandatory")
_ChassisIdentifyFlashControlCapabilities_Type = DellChassisIdentifyControlCapabilities
_ChassisIdentifyFlashControlCapabilities_Object = MibTableColumn
chassisIdentifyFlashControlCapabilities = _ChassisIdentifyFlashControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 28),
    _ChassisIdentifyFlashControlCapabilities_Type()
)
chassisIdentifyFlashControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlCapabilities.setStatus("mandatory")
_ChassisIdentifyFlashControlSettings_Type = DellChassisIdentifyControlSettings
_ChassisIdentifyFlashControlSettings_Object = MibTableColumn
chassisIdentifyFlashControlSettings = _ChassisIdentifyFlashControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 29),
    _ChassisIdentifyFlashControlSettings_Type()
)
chassisIdentifyFlashControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlSettings.setStatus("mandatory")
_ChassisLockPresent_Type = DellBoolean
_ChassisLockPresent_Object = MibTableColumn
chassisLockPresent = _ChassisLockPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 30),
    _ChassisLockPresent_Type()
)
chassisLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLockPresent.setStatus("mandatory")
_ChassishostControlCapabilitiesUnique_Type = DellHostControlCapabilities
_ChassishostControlCapabilitiesUnique_Object = MibTableColumn
chassishostControlCapabilitiesUnique = _ChassishostControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 31),
    _ChassishostControlCapabilitiesUnique_Type()
)
chassishostControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassishostControlCapabilitiesUnique.setStatus("mandatory")
_ChassishostControlSettingsUnique_Type = DellHostControlSettings
_ChassishostControlSettingsUnique_Object = MibTableColumn
chassishostControlSettingsUnique = _ChassishostControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 32),
    _ChassishostControlSettingsUnique_Type()
)
chassishostControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassishostControlSettingsUnique.setStatus("mandatory")
_ChassiswatchDogControlCapabilitiesUnique_Type = DellWatchDogControlCapabilities
_ChassiswatchDogControlCapabilitiesUnique_Object = MibTableColumn
chassiswatchDogControlCapabilitiesUnique = _ChassiswatchDogControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 33),
    _ChassiswatchDogControlCapabilitiesUnique_Type()
)
chassiswatchDogControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlCapabilitiesUnique.setStatus("mandatory")
_ChassiswatchDogControlSettingsUnique_Type = DellWatchControlSettings
_ChassiswatchDogControlSettingsUnique_Object = MibTableColumn
chassiswatchDogControlSettingsUnique = _ChassiswatchDogControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 34),
    _ChassiswatchDogControlSettingsUnique_Type()
)
chassiswatchDogControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlSettingsUnique.setStatus("mandatory")
_ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Type = DellWatchDogTimerCapabilities
_ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Object = MibTableColumn
chassiswatchDogControlExpiryTimeCapabilitiesUnique = _ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 35),
    _ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Type()
)
chassiswatchDogControlExpiryTimeCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTimeCapabilitiesUnique.setStatus("mandatory")
_ChassiswatchDogControlExpiryTime_Type = DellUnsigned16BitRange
_ChassiswatchDogControlExpiryTime_Object = MibTableColumn
chassiswatchDogControlExpiryTime = _ChassiswatchDogControlExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 36),
    _ChassiswatchDogControlExpiryTime_Type()
)
chassiswatchDogControlExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTime.setStatus("mandatory")
_ChassisallowSETCommandsfromSNMP_Type = DellBoolean
_ChassisallowSETCommandsfromSNMP_Object = MibTableColumn
chassisallowSETCommandsfromSNMP = _ChassisallowSETCommandsfromSNMP_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 37),
    _ChassisallowSETCommandsfromSNMP_Type()
)
chassisallowSETCommandsfromSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisallowSETCommandsfromSNMP.setStatus("mandatory")
_ChassisPowerButtonControlCapabilitiesUnique_Type = DellPowerButtonControlCapabilities
_ChassisPowerButtonControlCapabilitiesUnique_Object = MibTableColumn
chassisPowerButtonControlCapabilitiesUnique = _ChassisPowerButtonControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 38),
    _ChassisPowerButtonControlCapabilitiesUnique_Type()
)
chassisPowerButtonControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerButtonControlCapabilitiesUnique.setStatus("mandatory")
_ChassisPowerButtonControlSettingsUnique_Type = DellPowerButtonControlSettings
_ChassisPowerButtonControlSettingsUnique_Object = MibTableColumn
chassisPowerButtonControlSettingsUnique = _ChassisPowerButtonControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 39),
    _ChassisPowerButtonControlSettingsUnique_Type()
)
chassisPowerButtonControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerButtonControlSettingsUnique.setStatus("mandatory")


class _ChassisResellerName_Type(DisplayString):
    """Custom type chassisResellerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisResellerName_Type.__name__ = "DisplayString"
_ChassisResellerName_Object = MibTableColumn
chassisResellerName = _ChassisResellerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 40),
    _ChassisResellerName_Type()
)
chassisResellerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisResellerName.setStatus("mandatory")


class _ChassisResellerContactInformationName_Type(DisplayString):
    """Custom type chassisResellerContactInformationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisResellerContactInformationName_Type.__name__ = "DisplayString"
_ChassisResellerContactInformationName_Object = MibTableColumn
chassisResellerContactInformationName = _ChassisResellerContactInformationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 41),
    _ChassisResellerContactInformationName_Type()
)
chassisResellerContactInformationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisResellerContactInformationName.setStatus("mandatory")


class _ChassisResellerProductName_Type(DisplayString):
    """Custom type chassisResellerProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChassisResellerProductName_Type.__name__ = "DisplayString"
_ChassisResellerProductName_Object = MibTableColumn
chassisResellerProductName = _ChassisResellerProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 42),
    _ChassisResellerProductName_Type()
)
chassisResellerProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisResellerProductName.setStatus("mandatory")
_ChassisResellerSystemID_Type = DellUnsigned16BitRange
_ChassisResellerSystemID_Object = MibTableColumn
chassisResellerSystemID = _ChassisResellerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 43),
    _ChassisResellerSystemID_Type()
)
chassisResellerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisResellerSystemID.setStatus("mandatory")
_ChassisNMIButtonControlCapabilitiesUnique_Type = DellNMIButtonControlCapabilities
_ChassisNMIButtonControlCapabilitiesUnique_Object = MibTableColumn
chassisNMIButtonControlCapabilitiesUnique = _ChassisNMIButtonControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 44),
    _ChassisNMIButtonControlCapabilitiesUnique_Type()
)
chassisNMIButtonControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNMIButtonControlCapabilitiesUnique.setStatus("mandatory")
_ChassisNMIButtonControlSettingsUnique_Type = DellNMIButtonControlSettings
_ChassisNMIButtonControlSettingsUnique_Object = MibTableColumn
chassisNMIButtonControlSettingsUnique = _ChassisNMIButtonControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 45),
    _ChassisNMIButtonControlSettingsUnique_Type()
)
chassisNMIButtonControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNMIButtonControlSettingsUnique.setStatus("mandatory")
_ChassisSystemProperties_Type = DellSystemProperties
_ChassisSystemProperties_Object = MibTableColumn
chassisSystemProperties = _ChassisSystemProperties_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 46),
    _ChassisSystemProperties_Type()
)
chassisSystemProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemProperties.setStatus("mandatory")
_ChassisSystemRevisionNumber_Type = DellUnsigned8BitRange
_ChassisSystemRevisionNumber_Object = MibTableColumn
chassisSystemRevisionNumber = _ChassisSystemRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 47),
    _ChassisSystemRevisionNumber_Type()
)
chassisSystemRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemRevisionNumber.setStatus("mandatory")
_ChassisSystemRevisionName_Type = DellString
_ChassisSystemRevisionName_Object = MibTableColumn
chassisSystemRevisionName = _ChassisSystemRevisionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 48),
    _ChassisSystemRevisionName_Type()
)
chassisSystemRevisionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemRevisionName.setStatus("mandatory")
_ChassisExpressServiceCodeName_Type = DellString
_ChassisExpressServiceCodeName_Object = MibTableColumn
chassisExpressServiceCodeName = _ChassisExpressServiceCodeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 49),
    _ChassisExpressServiceCodeName_Type()
)
chassisExpressServiceCodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisExpressServiceCodeName.setStatus("mandatory")
_ChassisNodeIDName_Type = DellString
_ChassisNodeIDName_Object = MibTableColumn
chassisNodeIDName = _ChassisNodeIDName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 50),
    _ChassisNodeIDName_Type()
)
chassisNodeIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNodeIDName.setStatus("mandatory")
_UUIDTable_Object = MibTable
uUIDTable = _UUIDTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20)
)
if mibBuilder.loadTexts:
    uUIDTable.setStatus("mandatory")
_UUIDTableEntry_Object = MibTableRow
uUIDTableEntry = _UUIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1)
)
uUIDTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "uUIDchassisIndex"),
    (0, "MIB-Dell-10892", "uUIDIndex"),
)
if mibBuilder.loadTexts:
    uUIDTableEntry.setStatus("mandatory")
_UUIDchassisIndex_Type = DellObjectRange
_UUIDchassisIndex_Object = MibTableColumn
uUIDchassisIndex = _UUIDchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 1),
    _UUIDchassisIndex_Type()
)
uUIDchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDchassisIndex.setStatus("mandatory")
_UUIDIndex_Type = DellObjectRange
_UUIDIndex_Object = MibTableColumn
uUIDIndex = _UUIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 2),
    _UUIDIndex_Type()
)
uUIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDIndex.setStatus("mandatory")
_UUIDType_Type = DellUUIDType
_UUIDType_Object = MibTableColumn
uUIDType = _UUIDType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 3),
    _UUIDType_Type()
)
uUIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDType.setStatus("mandatory")


class _UUIDValue_Type(OctetString):
    """Custom type uUIDValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_UUIDValue_Type.__name__ = "OctetString"
_UUIDValue_Object = MibTableColumn
uUIDValue = _UUIDValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 4),
    _UUIDValue_Type()
)
uUIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDValue.setStatus("mandatory")
_PostLogTable_Object = MibTable
postLogTable = _PostLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30)
)
if mibBuilder.loadTexts:
    postLogTable.setStatus("mandatory")
_PostLogTableEntry_Object = MibTableRow
postLogTableEntry = _PostLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1)
)
postLogTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "postLogchassisIndex"),
    (0, "MIB-Dell-10892", "postLogRecordIndex"),
)
if mibBuilder.loadTexts:
    postLogTableEntry.setStatus("mandatory")
_PostLogchassisIndex_Type = DellObjectRange
_PostLogchassisIndex_Object = MibTableColumn
postLogchassisIndex = _PostLogchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 1),
    _PostLogchassisIndex_Type()
)
postLogchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogchassisIndex.setStatus("mandatory")
_PostLogRecordIndex_Type = DellUnsigned32BitRange
_PostLogRecordIndex_Object = MibTableColumn
postLogRecordIndex = _PostLogRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 2),
    _PostLogRecordIndex_Type()
)
postLogRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogRecordIndex.setStatus("mandatory")
_PostLogStateCapabilitiesUnique_Type = DellStateCapabilitiesLogUnique
_PostLogStateCapabilitiesUnique_Object = MibTableColumn
postLogStateCapabilitiesUnique = _PostLogStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 3),
    _PostLogStateCapabilitiesUnique_Type()
)
postLogStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogStateCapabilitiesUnique.setStatus("mandatory")
_PostLogStateSettingsUnique_Type = DellStateSettingsLogUnique
_PostLogStateSettingsUnique_Object = MibTableColumn
postLogStateSettingsUnique = _PostLogStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 4),
    _PostLogStateSettingsUnique_Type()
)
postLogStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogStateSettingsUnique.setStatus("mandatory")


class _PostLogRecord_Type(DisplayString):
    """Custom type postLogRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PostLogRecord_Type.__name__ = "DisplayString"
_PostLogRecord_Object = MibTableColumn
postLogRecord = _PostLogRecord_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 5),
    _PostLogRecord_Type()
)
postLogRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogRecord.setStatus("mandatory")
_PostLogFormat_Type = DellLogFormat
_PostLogFormat_Object = MibTableColumn
postLogFormat = _PostLogFormat_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 6),
    _PostLogFormat_Type()
)
postLogFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogFormat.setStatus("mandatory")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
_EventLogTableEntry_Object = MibTableRow
eventLogTableEntry = _EventLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1)
)
eventLogTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "eventLogchassisIndex"),
    (0, "MIB-Dell-10892", "eventLogRecordIndex"),
)
if mibBuilder.loadTexts:
    eventLogTableEntry.setStatus("mandatory")
_EventLogchassisIndex_Type = DellObjectRange
_EventLogchassisIndex_Object = MibTableColumn
eventLogchassisIndex = _EventLogchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 1),
    _EventLogchassisIndex_Type()
)
eventLogchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogchassisIndex.setStatus("mandatory")
_EventLogRecordIndex_Type = DellUnsigned32BitRange
_EventLogRecordIndex_Object = MibTableColumn
eventLogRecordIndex = _EventLogRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 2),
    _EventLogRecordIndex_Type()
)
eventLogRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRecordIndex.setStatus("mandatory")
_EventLogStateCapabilitiesUnique_Type = DellStateCapabilitiesLogUnique
_EventLogStateCapabilitiesUnique_Object = MibTableColumn
eventLogStateCapabilitiesUnique = _EventLogStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 3),
    _EventLogStateCapabilitiesUnique_Type()
)
eventLogStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogStateCapabilitiesUnique.setStatus("mandatory")
_EventLogStateSettingsUnique_Type = DellStateSettingsLogUnique
_EventLogStateSettingsUnique_Object = MibTableColumn
eventLogStateSettingsUnique = _EventLogStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 4),
    _EventLogStateSettingsUnique_Type()
)
eventLogStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogStateSettingsUnique.setStatus("mandatory")


class _EventLogRecord_Type(DisplayString):
    """Custom type eventLogRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_EventLogRecord_Type.__name__ = "DisplayString"
_EventLogRecord_Object = MibTableColumn
eventLogRecord = _EventLogRecord_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 5),
    _EventLogRecord_Type()
)
eventLogRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRecord.setStatus("mandatory")
_EventLogFormat_Type = DellLogFormat
_EventLogFormat_Object = MibTableColumn
eventLogFormat = _EventLogFormat_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 6),
    _EventLogFormat_Type()
)
eventLogFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogFormat.setStatus("mandatory")
_EventLogSeverityStatus_Type = DellStatus
_EventLogSeverityStatus_Object = MibTableColumn
eventLogSeverityStatus = _EventLogSeverityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 7),
    _EventLogSeverityStatus_Type()
)
eventLogSeverityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSeverityStatus.setStatus("mandatory")
_EventLogDateName_Type = DellDateName
_EventLogDateName_Object = MibTableColumn
eventLogDateName = _EventLogDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 8),
    _EventLogDateName_Type()
)
eventLogDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDateName.setStatus("mandatory")
_SystemBIOSTable_Object = MibTable
systemBIOSTable = _SystemBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50)
)
if mibBuilder.loadTexts:
    systemBIOSTable.setStatus("mandatory")
_SystemBIOSTableEntry_Object = MibTableRow
systemBIOSTableEntry = _SystemBIOSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1)
)
systemBIOSTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemBIOSchassisIndex"),
    (0, "MIB-Dell-10892", "systemBIOSIndex"),
)
if mibBuilder.loadTexts:
    systemBIOSTableEntry.setStatus("mandatory")
_SystemBIOSchassisIndex_Type = DellObjectRange
_SystemBIOSchassisIndex_Object = MibTableColumn
systemBIOSchassisIndex = _SystemBIOSchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 1),
    _SystemBIOSchassisIndex_Type()
)
systemBIOSchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSchassisIndex.setStatus("mandatory")
_SystemBIOSIndex_Type = DellObjectRange
_SystemBIOSIndex_Object = MibTableColumn
systemBIOSIndex = _SystemBIOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 2),
    _SystemBIOSIndex_Type()
)
systemBIOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSIndex.setStatus("mandatory")
_SystemBIOSStateCapabilities_Type = DellStateCapabilities
_SystemBIOSStateCapabilities_Object = MibTableColumn
systemBIOSStateCapabilities = _SystemBIOSStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 3),
    _SystemBIOSStateCapabilities_Type()
)
systemBIOSStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStateCapabilities.setStatus("mandatory")
_SystemBIOSStateSettings_Type = DellStateSettings
_SystemBIOSStateSettings_Object = MibTableColumn
systemBIOSStateSettings = _SystemBIOSStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 4),
    _SystemBIOSStateSettings_Type()
)
systemBIOSStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStateSettings.setStatus("mandatory")
_SystemBIOSStatus_Type = DellStatus
_SystemBIOSStatus_Object = MibTableColumn
systemBIOSStatus = _SystemBIOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 5),
    _SystemBIOSStatus_Type()
)
systemBIOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStatus.setStatus("mandatory")
_SystemBIOSSize_Type = DellUnsigned32BitRange
_SystemBIOSSize_Object = MibTableColumn
systemBIOSSize = _SystemBIOSSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 6),
    _SystemBIOSSize_Type()
)
systemBIOSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSSize.setStatus("mandatory")
_SystemBIOSReleaseDateName_Type = DellDateName
_SystemBIOSReleaseDateName_Object = MibTableColumn
systemBIOSReleaseDateName = _SystemBIOSReleaseDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 7),
    _SystemBIOSReleaseDateName_Type()
)
systemBIOSReleaseDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSReleaseDateName.setStatus("mandatory")
_SystemBIOSVersionName_Type = DellString
_SystemBIOSVersionName_Object = MibTableColumn
systemBIOSVersionName = _SystemBIOSVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 8),
    _SystemBIOSVersionName_Type()
)
systemBIOSVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSVersionName.setStatus("mandatory")
_SystemBIOSStartingAddress_Type = DellUnsigned64BitRange
_SystemBIOSStartingAddress_Object = MibTableColumn
systemBIOSStartingAddress = _SystemBIOSStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 9),
    _SystemBIOSStartingAddress_Type()
)
systemBIOSStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStartingAddress.setStatus("mandatory")
_SystemBIOSEndingAddress_Type = DellUnsigned64BitRange
_SystemBIOSEndingAddress_Object = MibTableColumn
systemBIOSEndingAddress = _SystemBIOSEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 10),
    _SystemBIOSEndingAddress_Type()
)
systemBIOSEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSEndingAddress.setStatus("mandatory")
_SystemBIOSManufacturerName_Type = DellString
_SystemBIOSManufacturerName_Object = MibTableColumn
systemBIOSManufacturerName = _SystemBIOSManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 11),
    _SystemBIOSManufacturerName_Type()
)
systemBIOSManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSManufacturerName.setStatus("mandatory")
_SystemBIOSCharacteristics_Type = DellUnsigned64BitRange
_SystemBIOSCharacteristics_Object = MibTableColumn
systemBIOSCharacteristics = _SystemBIOSCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 12),
    _SystemBIOSCharacteristics_Type()
)
systemBIOSCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSCharacteristics.setStatus("mandatory")
_SystemBIOSCharacteristicsExt1_Type = DellUnsigned8BitRange
_SystemBIOSCharacteristicsExt1_Object = MibTableColumn
systemBIOSCharacteristicsExt1 = _SystemBIOSCharacteristicsExt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 13),
    _SystemBIOSCharacteristicsExt1_Type()
)
systemBIOSCharacteristicsExt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSCharacteristicsExt1.setStatus("mandatory")
_SystemBIOSCharacteristicsExt2_Type = DellUnsigned8BitRange
_SystemBIOSCharacteristicsExt2_Object = MibTableColumn
systemBIOSCharacteristicsExt2 = _SystemBIOSCharacteristicsExt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 14),
    _SystemBIOSCharacteristicsExt2_Type()
)
systemBIOSCharacteristicsExt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSCharacteristicsExt2.setStatus("mandatory")
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("mandatory")
_FirmwareTableEntry_Object = MibTableRow
firmwareTableEntry = _FirmwareTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1)
)
firmwareTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "firmwarechassisIndex"),
    (0, "MIB-Dell-10892", "firmwareIndex"),
)
if mibBuilder.loadTexts:
    firmwareTableEntry.setStatus("mandatory")
_FirmwarechassisIndex_Type = DellObjectRange
_FirmwarechassisIndex_Object = MibTableColumn
firmwarechassisIndex = _FirmwarechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 1),
    _FirmwarechassisIndex_Type()
)
firmwarechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwarechassisIndex.setStatus("mandatory")
_FirmwareIndex_Type = DellObjectRange
_FirmwareIndex_Object = MibTableColumn
firmwareIndex = _FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 2),
    _FirmwareIndex_Type()
)
firmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareIndex.setStatus("mandatory")
_FirmwareStateCapabilities_Type = DellStateCapabilities
_FirmwareStateCapabilities_Object = MibTableColumn
firmwareStateCapabilities = _FirmwareStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 3),
    _FirmwareStateCapabilities_Type()
)
firmwareStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStateCapabilities.setStatus("mandatory")
_FirmwareStateSettings_Type = DellStateSettings
_FirmwareStateSettings_Object = MibTableColumn
firmwareStateSettings = _FirmwareStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 4),
    _FirmwareStateSettings_Type()
)
firmwareStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStateSettings.setStatus("mandatory")
_FirmwareStatus_Type = DellStatus
_FirmwareStatus_Object = MibTableColumn
firmwareStatus = _FirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 5),
    _FirmwareStatus_Type()
)
firmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStatus.setStatus("mandatory")
_FirmwareSize_Type = DellUnsigned16BitRange
_FirmwareSize_Object = MibTableColumn
firmwareSize = _FirmwareSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 6),
    _FirmwareSize_Type()
)
firmwareSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareSize.setStatus("mandatory")
_FirmwareType_Type = DellFirmwareType
_FirmwareType_Object = MibTableColumn
firmwareType = _FirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 7),
    _FirmwareType_Type()
)
firmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareType.setStatus("mandatory")
_FirmwareTypeName_Type = DellString
_FirmwareTypeName_Object = MibTableColumn
firmwareTypeName = _FirmwareTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 8),
    _FirmwareTypeName_Type()
)
firmwareTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareTypeName.setStatus("mandatory")
_FirmwareUpdateCapabilities_Type = DellUnsigned16BitRange
_FirmwareUpdateCapabilities_Object = MibTableColumn
firmwareUpdateCapabilities = _FirmwareUpdateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 9),
    _FirmwareUpdateCapabilities_Type()
)
firmwareUpdateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateCapabilities.setStatus("mandatory")


class _FirmwareDateName_Type(OctetString):
    """Custom type firmwareDateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FirmwareDateName_Type.__name__ = "OctetString"
_FirmwareDateName_Object = MibTableColumn
firmwareDateName = _FirmwareDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 10),
    _FirmwareDateName_Type()
)
firmwareDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareDateName.setStatus("mandatory")
_FirmwareVersionName_Type = DellString
_FirmwareVersionName_Object = MibTableColumn
firmwareVersionName = _FirmwareVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 11),
    _FirmwareVersionName_Type()
)
firmwareVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionName.setStatus("mandatory")
_IntrusionTable_Object = MibTable
intrusionTable = _IntrusionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70)
)
if mibBuilder.loadTexts:
    intrusionTable.setStatus("mandatory")
_IntrusionTableEntry_Object = MibTableRow
intrusionTableEntry = _IntrusionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1)
)
intrusionTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "intrusionchassisIndex"),
    (0, "MIB-Dell-10892", "intrusionIndex"),
)
if mibBuilder.loadTexts:
    intrusionTableEntry.setStatus("mandatory")
_IntrusionchassisIndex_Type = DellObjectRange
_IntrusionchassisIndex_Object = MibTableColumn
intrusionchassisIndex = _IntrusionchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 1),
    _IntrusionchassisIndex_Type()
)
intrusionchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionchassisIndex.setStatus("mandatory")
_IntrusionIndex_Type = DellObjectRange
_IntrusionIndex_Object = MibTableColumn
intrusionIndex = _IntrusionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 2),
    _IntrusionIndex_Type()
)
intrusionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionIndex.setStatus("mandatory")
_IntrusionStateCapabilities_Type = DellStateCapabilities
_IntrusionStateCapabilities_Object = MibTableColumn
intrusionStateCapabilities = _IntrusionStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 3),
    _IntrusionStateCapabilities_Type()
)
intrusionStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStateCapabilities.setStatus("mandatory")
_IntrusionStateSettings_Type = DellStateSettings
_IntrusionStateSettings_Object = MibTableColumn
intrusionStateSettings = _IntrusionStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 4),
    _IntrusionStateSettings_Type()
)
intrusionStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStateSettings.setStatus("mandatory")
_IntrusionStatus_Type = DellStatus
_IntrusionStatus_Object = MibTableColumn
intrusionStatus = _IntrusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 5),
    _IntrusionStatus_Type()
)
intrusionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStatus.setStatus("mandatory")
_IntrusionReading_Type = DellIntrusionReading
_IntrusionReading_Object = MibTableColumn
intrusionReading = _IntrusionReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 6),
    _IntrusionReading_Type()
)
intrusionReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionReading.setStatus("mandatory")
_IntrusionType_Type = DellIntrusionType
_IntrusionType_Object = MibTableColumn
intrusionType = _IntrusionType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 7),
    _IntrusionType_Type()
)
intrusionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionType.setStatus("mandatory")
_IntrusionLocationName_Type = DellString
_IntrusionLocationName_Object = MibTableColumn
intrusionLocationName = _IntrusionLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 8),
    _IntrusionLocationName_Type()
)
intrusionLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionLocationName.setStatus("mandatory")
_BaseBoardTable_Object = MibTable
baseBoardTable = _BaseBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80)
)
if mibBuilder.loadTexts:
    baseBoardTable.setStatus("mandatory")
_BaseBoardTableEntry_Object = MibTableRow
baseBoardTableEntry = _BaseBoardTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1)
)
baseBoardTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "baseBoardChassisIndex"),
    (0, "MIB-Dell-10892", "baseBoardIndex"),
)
if mibBuilder.loadTexts:
    baseBoardTableEntry.setStatus("mandatory")
_BaseBoardChassisIndex_Type = DellObjectRange
_BaseBoardChassisIndex_Object = MibTableColumn
baseBoardChassisIndex = _BaseBoardChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 1),
    _BaseBoardChassisIndex_Type()
)
baseBoardChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardChassisIndex.setStatus("mandatory")
_BaseBoardIndex_Type = DellObjectRange
_BaseBoardIndex_Object = MibTableColumn
baseBoardIndex = _BaseBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 2),
    _BaseBoardIndex_Type()
)
baseBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardIndex.setStatus("mandatory")
_BaseBoardStateCapabilities_Type = DellStateCapabilities
_BaseBoardStateCapabilities_Object = MibTableColumn
baseBoardStateCapabilities = _BaseBoardStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 3),
    _BaseBoardStateCapabilities_Type()
)
baseBoardStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardStateCapabilities.setStatus("mandatory")
_BaseBoardStateSettings_Type = DellStateSettings
_BaseBoardStateSettings_Object = MibTableColumn
baseBoardStateSettings = _BaseBoardStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 4),
    _BaseBoardStateSettings_Type()
)
baseBoardStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardStateSettings.setStatus("mandatory")
_BaseBoardStatus_Type = DellStatus
_BaseBoardStatus_Object = MibTableColumn
baseBoardStatus = _BaseBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 5),
    _BaseBoardStatus_Type()
)
baseBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardStatus.setStatus("mandatory")
_BaseBoardFeatureFlags_Type = DellBaseBoardFeatureFlags
_BaseBoardFeatureFlags_Object = MibTableColumn
baseBoardFeatureFlags = _BaseBoardFeatureFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 6),
    _BaseBoardFeatureFlags_Type()
)
baseBoardFeatureFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardFeatureFlags.setStatus("mandatory")
_BaseBoardType_Type = DellBaseBoardType
_BaseBoardType_Object = MibTableColumn
baseBoardType = _BaseBoardType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 7),
    _BaseBoardType_Type()
)
baseBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardType.setStatus("mandatory")
_BaseBoardTypeName_Type = DellString
_BaseBoardTypeName_Object = MibTableColumn
baseBoardTypeName = _BaseBoardTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 8),
    _BaseBoardTypeName_Type()
)
baseBoardTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardTypeName.setStatus("mandatory")
_BaseBoardLocationName_Type = DellString
_BaseBoardLocationName_Object = MibTableColumn
baseBoardLocationName = _BaseBoardLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 9),
    _BaseBoardLocationName_Type()
)
baseBoardLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardLocationName.setStatus("mandatory")
_BaseBoardManufacturerName_Type = DellString
_BaseBoardManufacturerName_Object = MibTableColumn
baseBoardManufacturerName = _BaseBoardManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 10),
    _BaseBoardManufacturerName_Type()
)
baseBoardManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardManufacturerName.setStatus("mandatory")
_BaseBoardProductName_Type = DellString
_BaseBoardProductName_Object = MibTableColumn
baseBoardProductName = _BaseBoardProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 11),
    _BaseBoardProductName_Type()
)
baseBoardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardProductName.setStatus("mandatory")
_BaseBoardVersionName_Type = DellString
_BaseBoardVersionName_Object = MibTableColumn
baseBoardVersionName = _BaseBoardVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 12),
    _BaseBoardVersionName_Type()
)
baseBoardVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardVersionName.setStatus("mandatory")
_BaseBoardServiceTagName_Type = DellString
_BaseBoardServiceTagName_Object = MibTableColumn
baseBoardServiceTagName = _BaseBoardServiceTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 13),
    _BaseBoardServiceTagName_Type()
)
baseBoardServiceTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardServiceTagName.setStatus("mandatory")
_BaseBoardPiecePartIDName_Type = DellString
_BaseBoardPiecePartIDName_Object = MibTableColumn
baseBoardPiecePartIDName = _BaseBoardPiecePartIDName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 14),
    _BaseBoardPiecePartIDName_Type()
)
baseBoardPiecePartIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardPiecePartIDName.setStatus("mandatory")
_BaseBoardAssetTagName_Type = DellString
_BaseBoardAssetTagName_Object = MibTableColumn
baseBoardAssetTagName = _BaseBoardAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 15),
    _BaseBoardAssetTagName_Type()
)
baseBoardAssetTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardAssetTagName.setStatus("mandatory")
_BaseBoardExpressServiceCodeName_Type = DellString
_BaseBoardExpressServiceCodeName_Object = MibTableColumn
baseBoardExpressServiceCodeName = _BaseBoardExpressServiceCodeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 80, 1, 16),
    _BaseBoardExpressServiceCodeName_Type()
)
baseBoardExpressServiceCodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBoardExpressServiceCodeName.setStatus("mandatory")
_OperatingSystemGroup_ObjectIdentity = ObjectIdentity
operatingSystemGroup = _OperatingSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400)
)
_OperatingSystemTable_Object = MibTable
operatingSystemTable = _OperatingSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10)
)
if mibBuilder.loadTexts:
    operatingSystemTable.setStatus("mandatory")
_OperatingSystemTableEntry_Object = MibTableRow
operatingSystemTableEntry = _OperatingSystemTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1)
)
operatingSystemTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "operatingSystemchassisIndex"),
)
if mibBuilder.loadTexts:
    operatingSystemTableEntry.setStatus("mandatory")
_OperatingSystemchassisIndex_Type = DellObjectRange
_OperatingSystemchassisIndex_Object = MibTableColumn
operatingSystemchassisIndex = _OperatingSystemchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 1),
    _OperatingSystemchassisIndex_Type()
)
operatingSystemchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemchassisIndex.setStatus("mandatory")
_OperatingSystemStateCapabilities_Type = DellStateCapabilities
_OperatingSystemStateCapabilities_Object = MibTableColumn
operatingSystemStateCapabilities = _OperatingSystemStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 2),
    _OperatingSystemStateCapabilities_Type()
)
operatingSystemStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemStateCapabilities.setStatus("mandatory")
_OperatingSystemStateSettings_Type = DellStateSettings
_OperatingSystemStateSettings_Object = MibTableColumn
operatingSystemStateSettings = _OperatingSystemStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 3),
    _OperatingSystemStateSettings_Type()
)
operatingSystemStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemStateSettings.setStatus("mandatory")
_OperatingSystemStatus_Type = DellStatus
_OperatingSystemStatus_Object = MibTableColumn
operatingSystemStatus = _OperatingSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 4),
    _OperatingSystemStatus_Type()
)
operatingSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemStatus.setStatus("mandatory")
_OperatingSystemIsPrimary_Type = DellBoolean
_OperatingSystemIsPrimary_Object = MibTableColumn
operatingSystemIsPrimary = _OperatingSystemIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 5),
    _OperatingSystemIsPrimary_Type()
)
operatingSystemIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemIsPrimary.setStatus("mandatory")


class _OperatingSystemOperatingSystemName_Type(DisplayString):
    """Custom type operatingSystemOperatingSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OperatingSystemOperatingSystemName_Type.__name__ = "DisplayString"
_OperatingSystemOperatingSystemName_Object = MibTableColumn
operatingSystemOperatingSystemName = _OperatingSystemOperatingSystemName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 6),
    _OperatingSystemOperatingSystemName_Type()
)
operatingSystemOperatingSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemOperatingSystemName.setStatus("mandatory")


class _OperatingSystemOperatingSystemVersionName_Type(DisplayString):
    """Custom type operatingSystemOperatingSystemVersionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OperatingSystemOperatingSystemVersionName_Type.__name__ = "DisplayString"
_OperatingSystemOperatingSystemVersionName_Object = MibTableColumn
operatingSystemOperatingSystemVersionName = _OperatingSystemOperatingSystemVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 7),
    _OperatingSystemOperatingSystemVersionName_Type()
)
operatingSystemOperatingSystemVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemOperatingSystemVersionName.setStatus("mandatory")
_OperatingSystemMemoryTable_Object = MibTable
operatingSystemMemoryTable = _OperatingSystemMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20)
)
if mibBuilder.loadTexts:
    operatingSystemMemoryTable.setStatus("mandatory")
_OperatingSystemMemoryTableEntry_Object = MibTableRow
operatingSystemMemoryTableEntry = _OperatingSystemMemoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1)
)
operatingSystemMemoryTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "operatingSystemMemorychassisIndex"),
)
if mibBuilder.loadTexts:
    operatingSystemMemoryTableEntry.setStatus("mandatory")
_OperatingSystemMemorychassisIndex_Type = DellObjectRange
_OperatingSystemMemorychassisIndex_Object = MibTableColumn
operatingSystemMemorychassisIndex = _OperatingSystemMemorychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 1),
    _OperatingSystemMemorychassisIndex_Type()
)
operatingSystemMemorychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemorychassisIndex.setStatus("mandatory")
_OperatingSystemMemoryStateCapabilities_Type = DellStateCapabilities
_OperatingSystemMemoryStateCapabilities_Object = MibTableColumn
operatingSystemMemoryStateCapabilities = _OperatingSystemMemoryStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 2),
    _OperatingSystemMemoryStateCapabilities_Type()
)
operatingSystemMemoryStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryStateCapabilities.setStatus("mandatory")
_OperatingSystemMemoryStateSettings_Type = DellStateSettings
_OperatingSystemMemoryStateSettings_Object = MibTableColumn
operatingSystemMemoryStateSettings = _OperatingSystemMemoryStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 3),
    _OperatingSystemMemoryStateSettings_Type()
)
operatingSystemMemoryStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryStateSettings.setStatus("mandatory")
_OperatingSystemMemoryStatus_Type = DellStatus
_OperatingSystemMemoryStatus_Object = MibTableColumn
operatingSystemMemoryStatus = _OperatingSystemMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 4),
    _OperatingSystemMemoryStatus_Type()
)
operatingSystemMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryStatus.setStatus("mandatory")
_OperatingSystemMemoryTotalPhysicalSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryTotalPhysicalSize_Object = MibTableColumn
operatingSystemMemoryTotalPhysicalSize = _OperatingSystemMemoryTotalPhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 5),
    _OperatingSystemMemoryTotalPhysicalSize_Type()
)
operatingSystemMemoryTotalPhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalPhysicalSize.setStatus("deprecated")
_OperatingSystemMemoryAvailablePhysicalSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryAvailablePhysicalSize_Object = MibTableColumn
operatingSystemMemoryAvailablePhysicalSize = _OperatingSystemMemoryAvailablePhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 6),
    _OperatingSystemMemoryAvailablePhysicalSize_Type()
)
operatingSystemMemoryAvailablePhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailablePhysicalSize.setStatus("mandatory")
_OperatingSystemMemoryTotalPageFileSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryTotalPageFileSize_Object = MibTableColumn
operatingSystemMemoryTotalPageFileSize = _OperatingSystemMemoryTotalPageFileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 7),
    _OperatingSystemMemoryTotalPageFileSize_Type()
)
operatingSystemMemoryTotalPageFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalPageFileSize.setStatus("mandatory")
_OperatingSystemMemoryAvailablePageFileSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryAvailablePageFileSize_Object = MibTableColumn
operatingSystemMemoryAvailablePageFileSize = _OperatingSystemMemoryAvailablePageFileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 8),
    _OperatingSystemMemoryAvailablePageFileSize_Type()
)
operatingSystemMemoryAvailablePageFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailablePageFileSize.setStatus("mandatory")
_OperatingSystemMemoryTotalVirtualSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryTotalVirtualSize_Object = MibTableColumn
operatingSystemMemoryTotalVirtualSize = _OperatingSystemMemoryTotalVirtualSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 9),
    _OperatingSystemMemoryTotalVirtualSize_Type()
)
operatingSystemMemoryTotalVirtualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalVirtualSize.setStatus("mandatory")
_OperatingSystemMemoryAvailableVirtualSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryAvailableVirtualSize_Object = MibTableColumn
operatingSystemMemoryAvailableVirtualSize = _OperatingSystemMemoryAvailableVirtualSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 10),
    _OperatingSystemMemoryAvailableVirtualSize_Type()
)
operatingSystemMemoryAvailableVirtualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailableVirtualSize.setStatus("mandatory")
_OperatingSystemMemoryExtTotalPhysicalSize_Type = DellUnsigned64BitRange
_OperatingSystemMemoryExtTotalPhysicalSize_Object = MibTableColumn
operatingSystemMemoryExtTotalPhysicalSize = _OperatingSystemMemoryExtTotalPhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 11),
    _OperatingSystemMemoryExtTotalPhysicalSize_Type()
)
operatingSystemMemoryExtTotalPhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryExtTotalPhysicalSize.setStatus("mandatory")
_SystemResourceGroup_ObjectIdentity = ObjectIdentity
systemResourceGroup = _SystemResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500)
)
_SystemResourceMapTable_Object = MibTable
systemResourceMapTable = _SystemResourceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10)
)
if mibBuilder.loadTexts:
    systemResourceMapTable.setStatus("mandatory")
_SystemResourceMapTableEntry_Object = MibTableRow
systemResourceMapTableEntry = _SystemResourceMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1)
)
systemResourceMapTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceMapchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceMapIndex"),
)
if mibBuilder.loadTexts:
    systemResourceMapTableEntry.setStatus("mandatory")
_SystemResourceMapchassisIndex_Type = DellObjectRange
_SystemResourceMapchassisIndex_Object = MibTableColumn
systemResourceMapchassisIndex = _SystemResourceMapchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 1),
    _SystemResourceMapchassisIndex_Type()
)
systemResourceMapchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapchassisIndex.setStatus("mandatory")
_SystemResourceMapIndex_Type = DellObjectRange
_SystemResourceMapIndex_Object = MibTableColumn
systemResourceMapIndex = _SystemResourceMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 2),
    _SystemResourceMapIndex_Type()
)
systemResourceMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapIndex.setStatus("mandatory")
_SystemResourceMapStateCapabilities_Type = DellStateCapabilities
_SystemResourceMapStateCapabilities_Object = MibTableColumn
systemResourceMapStateCapabilities = _SystemResourceMapStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 3),
    _SystemResourceMapStateCapabilities_Type()
)
systemResourceMapStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapStateCapabilities.setStatus("mandatory")
_SystemResourceMapStateSettings_Type = DellStateSettings
_SystemResourceMapStateSettings_Object = MibTableColumn
systemResourceMapStateSettings = _SystemResourceMapStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 4),
    _SystemResourceMapStateSettings_Type()
)
systemResourceMapStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapStateSettings.setStatus("mandatory")
_SystemResourceMapStatus_Type = DellStatus
_SystemResourceMapStatus_Object = MibTableColumn
systemResourceMapStatus = _SystemResourceMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 5),
    _SystemResourceMapStatus_Type()
)
systemResourceMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapStatus.setStatus("mandatory")
_SystemResourceMapType_Type = DellSystemResourceMapType
_SystemResourceMapType_Object = MibTableColumn
systemResourceMapType = _SystemResourceMapType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 6),
    _SystemResourceMapType_Type()
)
systemResourceMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapType.setStatus("mandatory")
_SystemResourceOwnerTable_Object = MibTable
systemResourceOwnerTable = _SystemResourceOwnerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20)
)
if mibBuilder.loadTexts:
    systemResourceOwnerTable.setStatus("mandatory")
_SystemResourceOwnerTableEntry_Object = MibTableRow
systemResourceOwnerTableEntry = _SystemResourceOwnerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1)
)
systemResourceOwnerTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceOwnerchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceOwnerIndex"),
)
if mibBuilder.loadTexts:
    systemResourceOwnerTableEntry.setStatus("mandatory")
_SystemResourceOwnerchassisIndex_Type = DellObjectRange
_SystemResourceOwnerchassisIndex_Object = MibTableColumn
systemResourceOwnerchassisIndex = _SystemResourceOwnerchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 1),
    _SystemResourceOwnerchassisIndex_Type()
)
systemResourceOwnerchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerchassisIndex.setStatus("mandatory")
_SystemResourceOwnerIndex_Type = DellObjectRange
_SystemResourceOwnerIndex_Object = MibTableColumn
systemResourceOwnerIndex = _SystemResourceOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 2),
    _SystemResourceOwnerIndex_Type()
)
systemResourceOwnerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerIndex.setStatus("mandatory")
_SystemResourceOwnerStateCapabilities_Type = DellStateCapabilities
_SystemResourceOwnerStateCapabilities_Object = MibTableColumn
systemResourceOwnerStateCapabilities = _SystemResourceOwnerStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 3),
    _SystemResourceOwnerStateCapabilities_Type()
)
systemResourceOwnerStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerStateCapabilities.setStatus("mandatory")
_SystemResourceOwnerStateSettings_Type = DellStateSettings
_SystemResourceOwnerStateSettings_Object = MibTableColumn
systemResourceOwnerStateSettings = _SystemResourceOwnerStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 4),
    _SystemResourceOwnerStateSettings_Type()
)
systemResourceOwnerStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerStateSettings.setStatus("mandatory")
_SystemResourceOwnerStatus_Type = DellStatus
_SystemResourceOwnerStatus_Object = MibTableColumn
systemResourceOwnerStatus = _SystemResourceOwnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 5),
    _SystemResourceOwnerStatus_Type()
)
systemResourceOwnerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerStatus.setStatus("mandatory")
_SystemResourceOwnerInterfaceType_Type = DellResourceOwnerInterfaceType
_SystemResourceOwnerInterfaceType_Object = MibTableColumn
systemResourceOwnerInterfaceType = _SystemResourceOwnerInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 6),
    _SystemResourceOwnerInterfaceType_Type()
)
systemResourceOwnerInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerInterfaceType.setStatus("mandatory")
_SystemResourceMapIndexReference_Type = DellObjectRange
_SystemResourceMapIndexReference_Object = MibTableColumn
systemResourceMapIndexReference = _SystemResourceMapIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 7),
    _SystemResourceMapIndexReference_Type()
)
systemResourceMapIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapIndexReference.setStatus("mandatory")
_SystemResourceOwnerDescriptionName_Type = DellString
_SystemResourceOwnerDescriptionName_Object = MibTableColumn
systemResourceOwnerDescriptionName = _SystemResourceOwnerDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 8),
    _SystemResourceOwnerDescriptionName_Type()
)
systemResourceOwnerDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerDescriptionName.setStatus("mandatory")
_SystemResourceOwnerInterfaceInstance_Type = DellObjectRange
_SystemResourceOwnerInterfaceInstance_Object = MibTableColumn
systemResourceOwnerInterfaceInstance = _SystemResourceOwnerInterfaceInstance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 9),
    _SystemResourceOwnerInterfaceInstance_Type()
)
systemResourceOwnerInterfaceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerInterfaceInstance.setStatus("mandatory")
_SystemResourceIOPortTable_Object = MibTable
systemResourceIOPortTable = _SystemResourceIOPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30)
)
if mibBuilder.loadTexts:
    systemResourceIOPortTable.setStatus("mandatory")
_SystemResourceIOPortTableEntry_Object = MibTableRow
systemResourceIOPortTableEntry = _SystemResourceIOPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1)
)
systemResourceIOPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceIOPortchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceIOPortIndex"),
)
if mibBuilder.loadTexts:
    systemResourceIOPortTableEntry.setStatus("mandatory")
_SystemResourceIOPortchassisIndex_Type = DellObjectRange
_SystemResourceIOPortchassisIndex_Object = MibTableColumn
systemResourceIOPortchassisIndex = _SystemResourceIOPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 1),
    _SystemResourceIOPortchassisIndex_Type()
)
systemResourceIOPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortchassisIndex.setStatus("mandatory")
_SystemResourceIOPortIndex_Type = DellObjectRange
_SystemResourceIOPortIndex_Object = MibTableColumn
systemResourceIOPortIndex = _SystemResourceIOPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 2),
    _SystemResourceIOPortIndex_Type()
)
systemResourceIOPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortIndex.setStatus("mandatory")
_SystemResourceIOPortStateCapabilities_Type = DellStateCapabilities
_SystemResourceIOPortStateCapabilities_Object = MibTableColumn
systemResourceIOPortStateCapabilities = _SystemResourceIOPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 3),
    _SystemResourceIOPortStateCapabilities_Type()
)
systemResourceIOPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortStateCapabilities.setStatus("mandatory")
_SystemResourceIOPortStateSettings_Type = DellStateSettings
_SystemResourceIOPortStateSettings_Object = MibTableColumn
systemResourceIOPortStateSettings = _SystemResourceIOPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 4),
    _SystemResourceIOPortStateSettings_Type()
)
systemResourceIOPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortStateSettings.setStatus("mandatory")
_SystemResourceIOPortStatus_Type = DellStatus
_SystemResourceIOPortStatus_Object = MibTableColumn
systemResourceIOPortStatus = _SystemResourceIOPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 5),
    _SystemResourceIOPortStatus_Type()
)
systemResourceIOPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortStatus.setStatus("mandatory")
_SystemResourceIOPortOwnerIndexReference_Type = DellObjectRange
_SystemResourceIOPortOwnerIndexReference_Object = MibTableColumn
systemResourceIOPortOwnerIndexReference = _SystemResourceIOPortOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 6),
    _SystemResourceIOPortOwnerIndexReference_Type()
)
systemResourceIOPortOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortOwnerIndexReference.setStatus("mandatory")
_SystemResourceIOPortShareDisposition_Type = DellResourceShareDisposition
_SystemResourceIOPortShareDisposition_Object = MibTableColumn
systemResourceIOPortShareDisposition = _SystemResourceIOPortShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 7),
    _SystemResourceIOPortShareDisposition_Type()
)
systemResourceIOPortShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortShareDisposition.setStatus("mandatory")
_SystemResourceIOPortStartingAddress_Type = DellUnsigned64BitRange
_SystemResourceIOPortStartingAddress_Object = MibTableColumn
systemResourceIOPortStartingAddress = _SystemResourceIOPortStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 8),
    _SystemResourceIOPortStartingAddress_Type()
)
systemResourceIOPortStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortStartingAddress.setStatus("mandatory")
_SystemResourceIOPortEndingAddress_Type = DellUnsigned64BitRange
_SystemResourceIOPortEndingAddress_Object = MibTableColumn
systemResourceIOPortEndingAddress = _SystemResourceIOPortEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 9),
    _SystemResourceIOPortEndingAddress_Type()
)
systemResourceIOPortEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortEndingAddress.setStatus("mandatory")
_SystemResourceMemoryTable_Object = MibTable
systemResourceMemoryTable = _SystemResourceMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40)
)
if mibBuilder.loadTexts:
    systemResourceMemoryTable.setStatus("mandatory")
_SystemResourceMemoryTableEntry_Object = MibTableRow
systemResourceMemoryTableEntry = _SystemResourceMemoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1)
)
systemResourceMemoryTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceMemorychassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceMemoryIndex"),
)
if mibBuilder.loadTexts:
    systemResourceMemoryTableEntry.setStatus("mandatory")
_SystemResourceMemorychassisIndex_Type = DellObjectRange
_SystemResourceMemorychassisIndex_Object = MibTableColumn
systemResourceMemorychassisIndex = _SystemResourceMemorychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 1),
    _SystemResourceMemorychassisIndex_Type()
)
systemResourceMemorychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemorychassisIndex.setStatus("mandatory")
_SystemResourceMemoryIndex_Type = DellObjectRange
_SystemResourceMemoryIndex_Object = MibTableColumn
systemResourceMemoryIndex = _SystemResourceMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 2),
    _SystemResourceMemoryIndex_Type()
)
systemResourceMemoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryIndex.setStatus("mandatory")
_SystemResourceMemoryStateCapabilities_Type = DellStateCapabilities
_SystemResourceMemoryStateCapabilities_Object = MibTableColumn
systemResourceMemoryStateCapabilities = _SystemResourceMemoryStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 3),
    _SystemResourceMemoryStateCapabilities_Type()
)
systemResourceMemoryStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryStateCapabilities.setStatus("mandatory")
_SystemResourceMemoryStateSettings_Type = DellStateSettings
_SystemResourceMemoryStateSettings_Object = MibTableColumn
systemResourceMemoryStateSettings = _SystemResourceMemoryStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 4),
    _SystemResourceMemoryStateSettings_Type()
)
systemResourceMemoryStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryStateSettings.setStatus("mandatory")
_SystemResourceMemoryStatus_Type = DellStatus
_SystemResourceMemoryStatus_Object = MibTableColumn
systemResourceMemoryStatus = _SystemResourceMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 5),
    _SystemResourceMemoryStatus_Type()
)
systemResourceMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryStatus.setStatus("mandatory")
_SystemResourceMemoryOwnerIndexReference_Type = DellObjectRange
_SystemResourceMemoryOwnerIndexReference_Object = MibTableColumn
systemResourceMemoryOwnerIndexReference = _SystemResourceMemoryOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 6),
    _SystemResourceMemoryOwnerIndexReference_Type()
)
systemResourceMemoryOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryOwnerIndexReference.setStatus("mandatory")
_SystemResourceMemoryShareDisposition_Type = DellResourceShareDisposition
_SystemResourceMemoryShareDisposition_Object = MibTableColumn
systemResourceMemoryShareDisposition = _SystemResourceMemoryShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 7),
    _SystemResourceMemoryShareDisposition_Type()
)
systemResourceMemoryShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryShareDisposition.setStatus("mandatory")
_SystemResourceMemoryStartingAddress_Type = DellUnsigned64BitRange
_SystemResourceMemoryStartingAddress_Object = MibTableColumn
systemResourceMemoryStartingAddress = _SystemResourceMemoryStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 8),
    _SystemResourceMemoryStartingAddress_Type()
)
systemResourceMemoryStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryStartingAddress.setStatus("mandatory")
_SystemResourceMemoryEndingAddress_Type = DellUnsigned64BitRange
_SystemResourceMemoryEndingAddress_Object = MibTableColumn
systemResourceMemoryEndingAddress = _SystemResourceMemoryEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 9),
    _SystemResourceMemoryEndingAddress_Type()
)
systemResourceMemoryEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryEndingAddress.setStatus("mandatory")
_SystemResourceMemoryFlags_Type = DellResourceMemoryFlags
_SystemResourceMemoryFlags_Object = MibTableColumn
systemResourceMemoryFlags = _SystemResourceMemoryFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 10),
    _SystemResourceMemoryFlags_Type()
)
systemResourceMemoryFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryFlags.setStatus("mandatory")
_SystemResourceInterruptTable_Object = MibTable
systemResourceInterruptTable = _SystemResourceInterruptTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50)
)
if mibBuilder.loadTexts:
    systemResourceInterruptTable.setStatus("mandatory")
_SystemResourceInterruptTableEntry_Object = MibTableRow
systemResourceInterruptTableEntry = _SystemResourceInterruptTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1)
)
systemResourceInterruptTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceInterruptchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceInterruptIndex"),
)
if mibBuilder.loadTexts:
    systemResourceInterruptTableEntry.setStatus("mandatory")
_SystemResourceInterruptchassisIndex_Type = DellObjectRange
_SystemResourceInterruptchassisIndex_Object = MibTableColumn
systemResourceInterruptchassisIndex = _SystemResourceInterruptchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 1),
    _SystemResourceInterruptchassisIndex_Type()
)
systemResourceInterruptchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptchassisIndex.setStatus("mandatory")
_SystemResourceInterruptIndex_Type = DellObjectRange
_SystemResourceInterruptIndex_Object = MibTableColumn
systemResourceInterruptIndex = _SystemResourceInterruptIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 2),
    _SystemResourceInterruptIndex_Type()
)
systemResourceInterruptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptIndex.setStatus("mandatory")
_SystemResourceInterruptStateCapabilities_Type = DellStateCapabilities
_SystemResourceInterruptStateCapabilities_Object = MibTableColumn
systemResourceInterruptStateCapabilities = _SystemResourceInterruptStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 3),
    _SystemResourceInterruptStateCapabilities_Type()
)
systemResourceInterruptStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptStateCapabilities.setStatus("mandatory")
_SystemResourceInterruptStateSettings_Type = DellStateSettings
_SystemResourceInterruptStateSettings_Object = MibTableColumn
systemResourceInterruptStateSettings = _SystemResourceInterruptStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 4),
    _SystemResourceInterruptStateSettings_Type()
)
systemResourceInterruptStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptStateSettings.setStatus("mandatory")
_SystemResourceInterruptStatus_Type = DellStatus
_SystemResourceInterruptStatus_Object = MibTableColumn
systemResourceInterruptStatus = _SystemResourceInterruptStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 5),
    _SystemResourceInterruptStatus_Type()
)
systemResourceInterruptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptStatus.setStatus("mandatory")
_SystemResourceInterruptOwnerIndexReference_Type = DellObjectRange
_SystemResourceInterruptOwnerIndexReference_Object = MibTableColumn
systemResourceInterruptOwnerIndexReference = _SystemResourceInterruptOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 6),
    _SystemResourceInterruptOwnerIndexReference_Type()
)
systemResourceInterruptOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptOwnerIndexReference.setStatus("mandatory")
_SystemResourceInterruptShareDisposition_Type = DellResourceShareDisposition
_SystemResourceInterruptShareDisposition_Object = MibTableColumn
systemResourceInterruptShareDisposition = _SystemResourceInterruptShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 7),
    _SystemResourceInterruptShareDisposition_Type()
)
systemResourceInterruptShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptShareDisposition.setStatus("mandatory")
_SystemResourceInterruptLevel_Type = DellUnsigned32BitRange
_SystemResourceInterruptLevel_Object = MibTableColumn
systemResourceInterruptLevel = _SystemResourceInterruptLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 8),
    _SystemResourceInterruptLevel_Type()
)
systemResourceInterruptLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptLevel.setStatus("mandatory")
_SystemResourceInterruptType_Type = DellResourceInterruptType
_SystemResourceInterruptType_Object = MibTableColumn
systemResourceInterruptType = _SystemResourceInterruptType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 9),
    _SystemResourceInterruptType_Type()
)
systemResourceInterruptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptType.setStatus("mandatory")
_SystemResourceInterruptTrigger_Type = DellResourceInterruptTrigger
_SystemResourceInterruptTrigger_Object = MibTableColumn
systemResourceInterruptTrigger = _SystemResourceInterruptTrigger_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 10),
    _SystemResourceInterruptTrigger_Type()
)
systemResourceInterruptTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptTrigger.setStatus("mandatory")
_SystemResourceDMATable_Object = MibTable
systemResourceDMATable = _SystemResourceDMATable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60)
)
if mibBuilder.loadTexts:
    systemResourceDMATable.setStatus("mandatory")
_SystemResourceDMATableEntry_Object = MibTableRow
systemResourceDMATableEntry = _SystemResourceDMATableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1)
)
systemResourceDMATableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceDMAchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceDMAIndex"),
)
if mibBuilder.loadTexts:
    systemResourceDMATableEntry.setStatus("mandatory")
_SystemResourceDMAchassisIndex_Type = DellObjectRange
_SystemResourceDMAchassisIndex_Object = MibTableColumn
systemResourceDMAchassisIndex = _SystemResourceDMAchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 1),
    _SystemResourceDMAchassisIndex_Type()
)
systemResourceDMAchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAchassisIndex.setStatus("mandatory")
_SystemResourceDMAIndex_Type = DellObjectRange
_SystemResourceDMAIndex_Object = MibTableColumn
systemResourceDMAIndex = _SystemResourceDMAIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 2),
    _SystemResourceDMAIndex_Type()
)
systemResourceDMAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAIndex.setStatus("mandatory")
_SystemResourceDMAStateCapabilities_Type = DellStateCapabilities
_SystemResourceDMAStateCapabilities_Object = MibTableColumn
systemResourceDMAStateCapabilities = _SystemResourceDMAStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 3),
    _SystemResourceDMAStateCapabilities_Type()
)
systemResourceDMAStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAStateCapabilities.setStatus("mandatory")
_SystemResourceDMAStateSettings_Type = DellStateSettings
_SystemResourceDMAStateSettings_Object = MibTableColumn
systemResourceDMAStateSettings = _SystemResourceDMAStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 4),
    _SystemResourceDMAStateSettings_Type()
)
systemResourceDMAStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAStateSettings.setStatus("mandatory")
_SystemResourceDMAStatus_Type = DellStatus
_SystemResourceDMAStatus_Object = MibTableColumn
systemResourceDMAStatus = _SystemResourceDMAStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 5),
    _SystemResourceDMAStatus_Type()
)
systemResourceDMAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAStatus.setStatus("mandatory")
_SystemResourceDMAOwnerIndexReference_Type = DellObjectRange
_SystemResourceDMAOwnerIndexReference_Object = MibTableColumn
systemResourceDMAOwnerIndexReference = _SystemResourceDMAOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 6),
    _SystemResourceDMAOwnerIndexReference_Type()
)
systemResourceDMAOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAOwnerIndexReference.setStatus("mandatory")
_SystemResourceDMAShareDisposition_Type = DellResourceShareDisposition
_SystemResourceDMAShareDisposition_Object = MibTableColumn
systemResourceDMAShareDisposition = _SystemResourceDMAShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 7),
    _SystemResourceDMAShareDisposition_Type()
)
systemResourceDMAShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAShareDisposition.setStatus("mandatory")
_SystemResourceDMAMaximumTransferSize_Type = DellUnsigned32BitRange
_SystemResourceDMAMaximumTransferSize_Object = MibTableColumn
systemResourceDMAMaximumTransferSize = _SystemResourceDMAMaximumTransferSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 8),
    _SystemResourceDMAMaximumTransferSize_Type()
)
systemResourceDMAMaximumTransferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAMaximumTransferSize.setStatus("mandatory")
_SystemResourceDMATransferWidth_Type = DellResourceDMATransferWidth
_SystemResourceDMATransferWidth_Object = MibTableColumn
systemResourceDMATransferWidth = _SystemResourceDMATransferWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 9),
    _SystemResourceDMATransferWidth_Type()
)
systemResourceDMATransferWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMATransferWidth.setStatus("mandatory")
_SystemResourceDMABusMaster_Type = DellResourceDMABusMaster
_SystemResourceDMABusMaster_Object = MibTableColumn
systemResourceDMABusMaster = _SystemResourceDMABusMaster_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 10),
    _SystemResourceDMABusMaster_Type()
)
systemResourceDMABusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMABusMaster.setStatus("mandatory")
_PowerGroup_ObjectIdentity = ObjectIdentity
powerGroup = _PowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600)
)
_PowerUnitTable_Object = MibTable
powerUnitTable = _PowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10)
)
if mibBuilder.loadTexts:
    powerUnitTable.setStatus("mandatory")
_PowerUnitTableEntry_Object = MibTableRow
powerUnitTableEntry = _PowerUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1)
)
powerUnitTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "powerUnitchassisIndex"),
    (0, "MIB-Dell-10892", "powerUnitIndex"),
)
if mibBuilder.loadTexts:
    powerUnitTableEntry.setStatus("mandatory")
_PowerUnitchassisIndex_Type = DellObjectRange
_PowerUnitchassisIndex_Object = MibTableColumn
powerUnitchassisIndex = _PowerUnitchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 1),
    _PowerUnitchassisIndex_Type()
)
powerUnitchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitchassisIndex.setStatus("mandatory")
_PowerUnitIndex_Type = DellObjectRange
_PowerUnitIndex_Object = MibTableColumn
powerUnitIndex = _PowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 2),
    _PowerUnitIndex_Type()
)
powerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitIndex.setStatus("mandatory")
_PowerUnitStateCapabilities_Type = DellStateCapabilities
_PowerUnitStateCapabilities_Object = MibTableColumn
powerUnitStateCapabilities = _PowerUnitStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 3),
    _PowerUnitStateCapabilities_Type()
)
powerUnitStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStateCapabilities.setStatus("mandatory")
_PowerUnitStateSettings_Type = DellStateSettings
_PowerUnitStateSettings_Object = MibTableColumn
powerUnitStateSettings = _PowerUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 4),
    _PowerUnitStateSettings_Type()
)
powerUnitStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStateSettings.setStatus("mandatory")
_PowerUnitRedundancyStatus_Type = DellStatusRedundancy
_PowerUnitRedundancyStatus_Object = MibTableColumn
powerUnitRedundancyStatus = _PowerUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 5),
    _PowerUnitRedundancyStatus_Type()
)
powerUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitRedundancyStatus.setStatus("mandatory")
_PowerSupplyCountForRedundancy_Type = DellObjectRange
_PowerSupplyCountForRedundancy_Object = MibTableColumn
powerSupplyCountForRedundancy = _PowerSupplyCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 6),
    _PowerSupplyCountForRedundancy_Type()
)
powerSupplyCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyCountForRedundancy.setStatus("mandatory")
_PowerUnitName_Type = DellString
_PowerUnitName_Object = MibTableColumn
powerUnitName = _PowerUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 7),
    _PowerUnitName_Type()
)
powerUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitName.setStatus("mandatory")
_PowerUnitStatus_Type = DellStatus
_PowerUnitStatus_Object = MibTableColumn
powerUnitStatus = _PowerUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 8),
    _PowerUnitStatus_Type()
)
powerUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatus.setStatus("mandatory")
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("mandatory")
_PowerSupplyTableEntry_Object = MibTableRow
powerSupplyTableEntry = _PowerSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1)
)
powerSupplyTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "powerSupplychassisIndex"),
    (0, "MIB-Dell-10892", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyTableEntry.setStatus("mandatory")
_PowerSupplychassisIndex_Type = DellObjectRange
_PowerSupplychassisIndex_Object = MibTableColumn
powerSupplychassisIndex = _PowerSupplychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 1),
    _PowerSupplychassisIndex_Type()
)
powerSupplychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplychassisIndex.setStatus("mandatory")
_PowerSupplyIndex_Type = DellObjectRange
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 2),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("mandatory")
_PowerSupplyStateCapabilitiesUnique_Type = DellPowerSupplyStateCapabilitiesUnique
_PowerSupplyStateCapabilitiesUnique_Object = MibTableColumn
powerSupplyStateCapabilitiesUnique = _PowerSupplyStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 3),
    _PowerSupplyStateCapabilitiesUnique_Type()
)
powerSupplyStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStateCapabilitiesUnique.setStatus("mandatory")
_PowerSupplyStateSettingsUnique_Type = DellPowerSupplyStateSettingsUnique
_PowerSupplyStateSettingsUnique_Object = MibTableColumn
powerSupplyStateSettingsUnique = _PowerSupplyStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 4),
    _PowerSupplyStateSettingsUnique_Type()
)
powerSupplyStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStateSettingsUnique.setStatus("mandatory")
_PowerSupplyStatus_Type = DellStatus
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 5),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("mandatory")
_PowerSupplyOutputWatts_Type = DellSigned32BitRange
_PowerSupplyOutputWatts_Object = MibTableColumn
powerSupplyOutputWatts = _PowerSupplyOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 6),
    _PowerSupplyOutputWatts_Type()
)
powerSupplyOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyOutputWatts.setStatus("mandatory")
_PowerSupplyType_Type = DellPowerSupplyType
_PowerSupplyType_Object = MibTableColumn
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 7),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("mandatory")
_PowerSupplyLocationName_Type = DellString
_PowerSupplyLocationName_Object = MibTableColumn
powerSupplyLocationName = _PowerSupplyLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 8),
    _PowerSupplyLocationName_Type()
)
powerSupplyLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyLocationName.setStatus("mandatory")
_PowerSupplyInputVoltage_Type = DellSigned32BitRange
_PowerSupplyInputVoltage_Object = MibTableColumn
powerSupplyInputVoltage = _PowerSupplyInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 9),
    _PowerSupplyInputVoltage_Type()
)
powerSupplyInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyInputVoltage.setStatus("mandatory")
_PowerSupplypowerUnitIndexReference_Type = DellObjectRange
_PowerSupplypowerUnitIndexReference_Object = MibTableColumn
powerSupplypowerUnitIndexReference = _PowerSupplypowerUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 10),
    _PowerSupplypowerUnitIndexReference_Type()
)
powerSupplypowerUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplypowerUnitIndexReference.setStatus("mandatory")
_PowerSupplySensorState_Type = DellPowerSupplySensorState
_PowerSupplySensorState_Object = MibTableColumn
powerSupplySensorState = _PowerSupplySensorState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 11),
    _PowerSupplySensorState_Type()
)
powerSupplySensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplySensorState.setStatus("mandatory")
_PowerSupplyConfigurationErrorType_Type = DellPowerSupplyConfigurationErrorType
_PowerSupplyConfigurationErrorType_Object = MibTableColumn
powerSupplyConfigurationErrorType = _PowerSupplyConfigurationErrorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 12),
    _PowerSupplyConfigurationErrorType_Type()
)
powerSupplyConfigurationErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConfigurationErrorType.setStatus("mandatory")
_PowerSupplyPowerMonitorCapable_Type = DellBoolean
_PowerSupplyPowerMonitorCapable_Object = MibTableColumn
powerSupplyPowerMonitorCapable = _PowerSupplyPowerMonitorCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 13),
    _PowerSupplyPowerMonitorCapable_Type()
)
powerSupplyPowerMonitorCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPowerMonitorCapable.setStatus("mandatory")
_PowerSupplyRatedInputWattage_Type = DellSigned32BitRange
_PowerSupplyRatedInputWattage_Object = MibTableColumn
powerSupplyRatedInputWattage = _PowerSupplyRatedInputWattage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 14),
    _PowerSupplyRatedInputWattage_Type()
)
powerSupplyRatedInputWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRatedInputWattage.setStatus("mandatory")
_VoltageProbeTable_Object = MibTable
voltageProbeTable = _VoltageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20)
)
if mibBuilder.loadTexts:
    voltageProbeTable.setStatus("mandatory")
_VoltageProbeTableEntry_Object = MibTableRow
voltageProbeTableEntry = _VoltageProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1)
)
voltageProbeTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "voltageProbechassisIndex"),
    (0, "MIB-Dell-10892", "voltageProbeIndex"),
)
if mibBuilder.loadTexts:
    voltageProbeTableEntry.setStatus("mandatory")
_VoltageProbechassisIndex_Type = DellObjectRange
_VoltageProbechassisIndex_Object = MibTableColumn
voltageProbechassisIndex = _VoltageProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 1),
    _VoltageProbechassisIndex_Type()
)
voltageProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbechassisIndex.setStatus("mandatory")
_VoltageProbeIndex_Type = DellObjectRange
_VoltageProbeIndex_Object = MibTableColumn
voltageProbeIndex = _VoltageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 2),
    _VoltageProbeIndex_Type()
)
voltageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeIndex.setStatus("mandatory")
_VoltageProbeStateCapabilities_Type = DellStateCapabilities
_VoltageProbeStateCapabilities_Object = MibTableColumn
voltageProbeStateCapabilities = _VoltageProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 3),
    _VoltageProbeStateCapabilities_Type()
)
voltageProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStateCapabilities.setStatus("mandatory")
_VoltageProbeStateSettings_Type = DellStateSettings
_VoltageProbeStateSettings_Object = MibTableColumn
voltageProbeStateSettings = _VoltageProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 4),
    _VoltageProbeStateSettings_Type()
)
voltageProbeStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStateSettings.setStatus("mandatory")
_VoltageProbeStatus_Type = DellStatusProbe
_VoltageProbeStatus_Object = MibTableColumn
voltageProbeStatus = _VoltageProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 5),
    _VoltageProbeStatus_Type()
)
voltageProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStatus.setStatus("mandatory")
_VoltageProbeReading_Type = DellSigned32BitRange
_VoltageProbeReading_Object = MibTableColumn
voltageProbeReading = _VoltageProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 6),
    _VoltageProbeReading_Type()
)
voltageProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeReading.setStatus("mandatory")
_VoltageProbeType_Type = DellVoltageType
_VoltageProbeType_Object = MibTableColumn
voltageProbeType = _VoltageProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 7),
    _VoltageProbeType_Type()
)
voltageProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeType.setStatus("mandatory")
_VoltageProbeLocationName_Type = DellString
_VoltageProbeLocationName_Object = MibTableColumn
voltageProbeLocationName = _VoltageProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 8),
    _VoltageProbeLocationName_Type()
)
voltageProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLocationName.setStatus("mandatory")
_VoltageProbeUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_VoltageProbeUpperNonRecoverableThreshold_Object = MibTableColumn
voltageProbeUpperNonRecoverableThreshold = _VoltageProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 9),
    _VoltageProbeUpperNonRecoverableThreshold_Type()
)
voltageProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperNonRecoverableThreshold.setStatus("mandatory")
_VoltageProbeUpperCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeUpperCriticalThreshold_Object = MibTableColumn
voltageProbeUpperCriticalThreshold = _VoltageProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 10),
    _VoltageProbeUpperCriticalThreshold_Type()
)
voltageProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperCriticalThreshold.setStatus("mandatory")
_VoltageProbeUpperNonCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeUpperNonCriticalThreshold_Object = MibTableColumn
voltageProbeUpperNonCriticalThreshold = _VoltageProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 11),
    _VoltageProbeUpperNonCriticalThreshold_Type()
)
voltageProbeUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperNonCriticalThreshold.setStatus("mandatory")
_VoltageProbeLowerNonCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeLowerNonCriticalThreshold_Object = MibTableColumn
voltageProbeLowerNonCriticalThreshold = _VoltageProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 12),
    _VoltageProbeLowerNonCriticalThreshold_Type()
)
voltageProbeLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerNonCriticalThreshold.setStatus("mandatory")
_VoltageProbeLowerCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeLowerCriticalThreshold_Object = MibTableColumn
voltageProbeLowerCriticalThreshold = _VoltageProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 13),
    _VoltageProbeLowerCriticalThreshold_Type()
)
voltageProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerCriticalThreshold.setStatus("mandatory")
_VoltageProbeLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_VoltageProbeLowerNonRecoverableThreshold_Object = MibTableColumn
voltageProbeLowerNonRecoverableThreshold = _VoltageProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 14),
    _VoltageProbeLowerNonRecoverableThreshold_Type()
)
voltageProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerNonRecoverableThreshold.setStatus("mandatory")
_VoltageProbeProbeCapabilities_Type = DellProbeCapabilities
_VoltageProbeProbeCapabilities_Object = MibTableColumn
voltageProbeProbeCapabilities = _VoltageProbeProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 15),
    _VoltageProbeProbeCapabilities_Type()
)
voltageProbeProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeProbeCapabilities.setStatus("mandatory")
_VoltageProbeDiscreteReading_Type = DellVoltageDiscreteReading
_VoltageProbeDiscreteReading_Object = MibTableColumn
voltageProbeDiscreteReading = _VoltageProbeDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 16),
    _VoltageProbeDiscreteReading_Type()
)
voltageProbeDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeDiscreteReading.setStatus("mandatory")
_AmperageProbeTable_Object = MibTable
amperageProbeTable = _AmperageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30)
)
if mibBuilder.loadTexts:
    amperageProbeTable.setStatus("mandatory")
_AmperageProbeTableEntry_Object = MibTableRow
amperageProbeTableEntry = _AmperageProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1)
)
amperageProbeTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "amperageProbechassisIndex"),
    (0, "MIB-Dell-10892", "amperageProbeIndex"),
)
if mibBuilder.loadTexts:
    amperageProbeTableEntry.setStatus("mandatory")
_AmperageProbechassisIndex_Type = DellObjectRange
_AmperageProbechassisIndex_Object = MibTableColumn
amperageProbechassisIndex = _AmperageProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 1),
    _AmperageProbechassisIndex_Type()
)
amperageProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbechassisIndex.setStatus("mandatory")
_AmperageProbeIndex_Type = DellObjectRange
_AmperageProbeIndex_Object = MibTableColumn
amperageProbeIndex = _AmperageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 2),
    _AmperageProbeIndex_Type()
)
amperageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeIndex.setStatus("mandatory")
_AmperageProbeStateCapabilities_Type = DellStateCapabilities
_AmperageProbeStateCapabilities_Object = MibTableColumn
amperageProbeStateCapabilities = _AmperageProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 3),
    _AmperageProbeStateCapabilities_Type()
)
amperageProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStateCapabilities.setStatus("mandatory")
_AmperageProbeStateSettings_Type = DellStateSettings
_AmperageProbeStateSettings_Object = MibTableColumn
amperageProbeStateSettings = _AmperageProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 4),
    _AmperageProbeStateSettings_Type()
)
amperageProbeStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStateSettings.setStatus("mandatory")
_AmperageProbeStatus_Type = DellStatusProbe
_AmperageProbeStatus_Object = MibTableColumn
amperageProbeStatus = _AmperageProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 5),
    _AmperageProbeStatus_Type()
)
amperageProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStatus.setStatus("mandatory")
_AmperageProbeReading_Type = DellSigned32BitRange
_AmperageProbeReading_Object = MibTableColumn
amperageProbeReading = _AmperageProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 6),
    _AmperageProbeReading_Type()
)
amperageProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeReading.setStatus("mandatory")
_AmperageProbeType_Type = DellAmperageProbeType
_AmperageProbeType_Object = MibTableColumn
amperageProbeType = _AmperageProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 7),
    _AmperageProbeType_Type()
)
amperageProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeType.setStatus("mandatory")
_AmperageProbeLocationName_Type = DellString
_AmperageProbeLocationName_Object = MibTableColumn
amperageProbeLocationName = _AmperageProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 8),
    _AmperageProbeLocationName_Type()
)
amperageProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLocationName.setStatus("mandatory")
_AmperageProbeUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_AmperageProbeUpperNonRecoverableThreshold_Object = MibTableColumn
amperageProbeUpperNonRecoverableThreshold = _AmperageProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 9),
    _AmperageProbeUpperNonRecoverableThreshold_Type()
)
amperageProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperNonRecoverableThreshold.setStatus("mandatory")
_AmperageProbeUpperCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeUpperCriticalThreshold_Object = MibTableColumn
amperageProbeUpperCriticalThreshold = _AmperageProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 10),
    _AmperageProbeUpperCriticalThreshold_Type()
)
amperageProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperCriticalThreshold.setStatus("mandatory")
_AmperageProbeUpperNonCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeUpperNonCriticalThreshold_Object = MibTableColumn
amperageProbeUpperNonCriticalThreshold = _AmperageProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 11),
    _AmperageProbeUpperNonCriticalThreshold_Type()
)
amperageProbeUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperNonCriticalThreshold.setStatus("mandatory")
_AmperageProbeLowerNonCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeLowerNonCriticalThreshold_Object = MibTableColumn
amperageProbeLowerNonCriticalThreshold = _AmperageProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 12),
    _AmperageProbeLowerNonCriticalThreshold_Type()
)
amperageProbeLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerNonCriticalThreshold.setStatus("mandatory")
_AmperageProbeLowerCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeLowerCriticalThreshold_Object = MibTableColumn
amperageProbeLowerCriticalThreshold = _AmperageProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 13),
    _AmperageProbeLowerCriticalThreshold_Type()
)
amperageProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerCriticalThreshold.setStatus("mandatory")
_AmperageProbeLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_AmperageProbeLowerNonRecoverableThreshold_Object = MibTableColumn
amperageProbeLowerNonRecoverableThreshold = _AmperageProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 14),
    _AmperageProbeLowerNonRecoverableThreshold_Type()
)
amperageProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerNonRecoverableThreshold.setStatus("mandatory")
_AmperageProbeProbeCapabilities_Type = DellProbeCapabilities
_AmperageProbeProbeCapabilities_Object = MibTableColumn
amperageProbeProbeCapabilities = _AmperageProbeProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 15),
    _AmperageProbeProbeCapabilities_Type()
)
amperageProbeProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeProbeCapabilities.setStatus("mandatory")
_AmperageProbeDiscreteReading_Type = DellAmperageDiscreteReading
_AmperageProbeDiscreteReading_Object = MibTableColumn
amperageProbeDiscreteReading = _AmperageProbeDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 16),
    _AmperageProbeDiscreteReading_Type()
)
amperageProbeDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeDiscreteReading.setStatus("mandatory")
_ACPowerSwitchTable_Object = MibTable
aCPowerSwitchTable = _ACPowerSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40)
)
if mibBuilder.loadTexts:
    aCPowerSwitchTable.setStatus("mandatory")
_ACPowerSwitchTableEntry_Object = MibTableRow
aCPowerSwitchTableEntry = _ACPowerSwitchTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1)
)
aCPowerSwitchTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "aCPowerSwitchchassisIndex"),
    (0, "MIB-Dell-10892", "aCPowerSwitchIndex"),
)
if mibBuilder.loadTexts:
    aCPowerSwitchTableEntry.setStatus("mandatory")
_ACPowerSwitchchassisIndex_Type = DellObjectRange
_ACPowerSwitchchassisIndex_Object = MibTableColumn
aCPowerSwitchchassisIndex = _ACPowerSwitchchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 1),
    _ACPowerSwitchchassisIndex_Type()
)
aCPowerSwitchchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchchassisIndex.setStatus("mandatory")
_ACPowerSwitchIndex_Type = DellObjectRange
_ACPowerSwitchIndex_Object = MibTableColumn
aCPowerSwitchIndex = _ACPowerSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 2),
    _ACPowerSwitchIndex_Type()
)
aCPowerSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchIndex.setStatus("mandatory")
_ACPowerSwitchCapabilities_Type = DellACPowerSwitchCapabilities
_ACPowerSwitchCapabilities_Object = MibTableColumn
aCPowerSwitchCapabilities = _ACPowerSwitchCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 3),
    _ACPowerSwitchCapabilities_Type()
)
aCPowerSwitchCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchCapabilities.setStatus("mandatory")
_ACPowerSwitchSettings_Type = DellACPowerSwitchSettings
_ACPowerSwitchSettings_Object = MibTableColumn
aCPowerSwitchSettings = _ACPowerSwitchSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 4),
    _ACPowerSwitchSettings_Type()
)
aCPowerSwitchSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchSettings.setStatus("mandatory")
_ACPowerSwitchRedundancyStatus_Type = DellStatusRedundancy
_ACPowerSwitchRedundancyStatus_Object = MibTableColumn
aCPowerSwitchRedundancyStatus = _ACPowerSwitchRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 5),
    _ACPowerSwitchRedundancyStatus_Type()
)
aCPowerSwitchRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchRedundancyStatus.setStatus("mandatory")
_ACPowerCordCountForRedundancy_Type = DellObjectRange
_ACPowerCordCountForRedundancy_Object = MibTableColumn
aCPowerCordCountForRedundancy = _ACPowerCordCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 6),
    _ACPowerCordCountForRedundancy_Type()
)
aCPowerCordCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordCountForRedundancy.setStatus("mandatory")
_ACPowerSwitchName_Type = DellString
_ACPowerSwitchName_Object = MibTableColumn
aCPowerSwitchName = _ACPowerSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 7),
    _ACPowerSwitchName_Type()
)
aCPowerSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchName.setStatus("mandatory")
_ACPowerSwitchRedundancyMode_Type = DellACPowerSwitchRedundancyMode
_ACPowerSwitchRedundancyMode_Object = MibTableColumn
aCPowerSwitchRedundancyMode = _ACPowerSwitchRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 8),
    _ACPowerSwitchRedundancyMode_Type()
)
aCPowerSwitchRedundancyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchRedundancyMode.setStatus("mandatory")
_ACPowerSwitchStatus_Type = DellStatus
_ACPowerSwitchStatus_Object = MibTableColumn
aCPowerSwitchStatus = _ACPowerSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 9),
    _ACPowerSwitchStatus_Type()
)
aCPowerSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchStatus.setStatus("mandatory")
_ACPowerCordTable_Object = MibTable
aCPowerCordTable = _ACPowerCordTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42)
)
if mibBuilder.loadTexts:
    aCPowerCordTable.setStatus("mandatory")
_ACPowerCordTableEntry_Object = MibTableRow
aCPowerCordTableEntry = _ACPowerCordTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1)
)
aCPowerCordTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "aCPowerCordchassisIndex"),
    (0, "MIB-Dell-10892", "aCPowerCordIndex"),
)
if mibBuilder.loadTexts:
    aCPowerCordTableEntry.setStatus("mandatory")
_ACPowerCordchassisIndex_Type = DellObjectRange
_ACPowerCordchassisIndex_Object = MibTableColumn
aCPowerCordchassisIndex = _ACPowerCordchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 1),
    _ACPowerCordchassisIndex_Type()
)
aCPowerCordchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordchassisIndex.setStatus("mandatory")
_ACPowerCordIndex_Type = DellObjectRange
_ACPowerCordIndex_Object = MibTableColumn
aCPowerCordIndex = _ACPowerCordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 2),
    _ACPowerCordIndex_Type()
)
aCPowerCordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordIndex.setStatus("mandatory")
_ACPowerCordStateCapabilities_Type = DellACPowerCordStateCapabilities
_ACPowerCordStateCapabilities_Object = MibTableColumn
aCPowerCordStateCapabilities = _ACPowerCordStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 3),
    _ACPowerCordStateCapabilities_Type()
)
aCPowerCordStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordStateCapabilities.setStatus("mandatory")
_ACPowerCordStateSettings_Type = DellACPowerCordStateSettings
_ACPowerCordStateSettings_Object = MibTableColumn
aCPowerCordStateSettings = _ACPowerCordStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 4),
    _ACPowerCordStateSettings_Type()
)
aCPowerCordStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordStateSettings.setStatus("mandatory")
_ACPowerCordStatus_Type = DellStatus
_ACPowerCordStatus_Object = MibTableColumn
aCPowerCordStatus = _ACPowerCordStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 5),
    _ACPowerCordStatus_Type()
)
aCPowerCordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordStatus.setStatus("mandatory")
_ACPowerCordaCPowerSwitchIndexReference_Type = DellObjectRange
_ACPowerCordaCPowerSwitchIndexReference_Object = MibTableColumn
aCPowerCordaCPowerSwitchIndexReference = _ACPowerCordaCPowerSwitchIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 6),
    _ACPowerCordaCPowerSwitchIndexReference_Type()
)
aCPowerCordaCPowerSwitchIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordaCPowerSwitchIndexReference.setStatus("mandatory")
_ACPowerCordLocationName_Type = DellString
_ACPowerCordLocationName_Object = MibTableColumn
aCPowerCordLocationName = _ACPowerCordLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 7),
    _ACPowerCordLocationName_Type()
)
aCPowerCordLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordLocationName.setStatus("mandatory")
_BatteryTable_Object = MibTable
batteryTable = _BatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50)
)
if mibBuilder.loadTexts:
    batteryTable.setStatus("mandatory")
_BatteryTableEntry_Object = MibTableRow
batteryTableEntry = _BatteryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1)
)
batteryTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "batteryChassisIndex"),
    (0, "MIB-Dell-10892", "batteryIndex"),
)
if mibBuilder.loadTexts:
    batteryTableEntry.setStatus("mandatory")
_BatteryChassisIndex_Type = DellObjectRange
_BatteryChassisIndex_Object = MibTableColumn
batteryChassisIndex = _BatteryChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1, 1),
    _BatteryChassisIndex_Type()
)
batteryChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryChassisIndex.setStatus("mandatory")
_BatteryIndex_Type = DellObjectRange
_BatteryIndex_Object = MibTableColumn
batteryIndex = _BatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1, 2),
    _BatteryIndex_Type()
)
batteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryIndex.setStatus("mandatory")
_BatteryStateCapabilities_Type = DellStateCapabilities
_BatteryStateCapabilities_Object = MibTableColumn
batteryStateCapabilities = _BatteryStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1, 3),
    _BatteryStateCapabilities_Type()
)
batteryStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStateCapabilities.setStatus("mandatory")
_BatteryStateSettings_Type = DellStateSettings
_BatteryStateSettings_Object = MibTableColumn
batteryStateSettings = _BatteryStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1, 4),
    _BatteryStateSettings_Type()
)
batteryStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStateSettings.setStatus("mandatory")
_BatteryStatus_Type = DellStatus
_BatteryStatus_Object = MibTableColumn
batteryStatus = _BatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1, 5),
    _BatteryStatus_Type()
)
batteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStatus.setStatus("mandatory")
_BatteryReading_Type = DellBatteryReading
_BatteryReading_Object = MibTableColumn
batteryReading = _BatteryReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1, 6),
    _BatteryReading_Type()
)
batteryReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryReading.setStatus("mandatory")
_BatteryLocationName_Type = DellString
_BatteryLocationName_Object = MibTableColumn
batteryLocationName = _BatteryLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 50, 1, 7),
    _BatteryLocationName_Type()
)
batteryLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLocationName.setStatus("mandatory")
_PowerUsageTable_Object = MibTable
powerUsageTable = _PowerUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60)
)
if mibBuilder.loadTexts:
    powerUsageTable.setStatus("mandatory")
_PowerUsageTableEntry_Object = MibTableRow
powerUsageTableEntry = _PowerUsageTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1)
)
powerUsageTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "powerUsageChassisIndex"),
    (0, "MIB-Dell-10892", "powerUsageIndex"),
)
if mibBuilder.loadTexts:
    powerUsageTableEntry.setStatus("mandatory")
_PowerUsageChassisIndex_Type = DellObjectRange
_PowerUsageChassisIndex_Object = MibTableColumn
powerUsageChassisIndex = _PowerUsageChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 1),
    _PowerUsageChassisIndex_Type()
)
powerUsageChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageChassisIndex.setStatus("mandatory")
_PowerUsageIndex_Type = DellObjectRange
_PowerUsageIndex_Object = MibTableColumn
powerUsageIndex = _PowerUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 2),
    _PowerUsageIndex_Type()
)
powerUsageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageIndex.setStatus("mandatory")
_PowerUsageStateCapabilities_Type = DellStateCapabilities
_PowerUsageStateCapabilities_Object = MibTableColumn
powerUsageStateCapabilities = _PowerUsageStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 3),
    _PowerUsageStateCapabilities_Type()
)
powerUsageStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageStateCapabilities.setStatus("mandatory")
_PowerUsageStateSettings_Type = DellStateSettings
_PowerUsageStateSettings_Object = MibTableColumn
powerUsageStateSettings = _PowerUsageStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 4),
    _PowerUsageStateSettings_Type()
)
powerUsageStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageStateSettings.setStatus("mandatory")
_PowerUsageStatus_Type = DellStatus
_PowerUsageStatus_Object = MibTableColumn
powerUsageStatus = _PowerUsageStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 5),
    _PowerUsageStatus_Type()
)
powerUsageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageStatus.setStatus("mandatory")
_PowerUsageEntityName_Type = DellString
_PowerUsageEntityName_Object = MibTableColumn
powerUsageEntityName = _PowerUsageEntityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 6),
    _PowerUsageEntityName_Type()
)
powerUsageEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageEntityName.setStatus("mandatory")
_PowerUsageCumulativeWattage_Type = DellUnsigned32BitRange
_PowerUsageCumulativeWattage_Object = MibTableColumn
powerUsageCumulativeWattage = _PowerUsageCumulativeWattage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 7),
    _PowerUsageCumulativeWattage_Type()
)
powerUsageCumulativeWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageCumulativeWattage.setStatus("mandatory")
_PowerUsageCumulativeWattageStartDateName_Type = DellDateName
_PowerUsageCumulativeWattageStartDateName_Object = MibTableColumn
powerUsageCumulativeWattageStartDateName = _PowerUsageCumulativeWattageStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 8),
    _PowerUsageCumulativeWattageStartDateName_Type()
)
powerUsageCumulativeWattageStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageCumulativeWattageStartDateName.setStatus("mandatory")
_PowerUsagePeakWatts_Type = DellUnsigned32BitRange
_PowerUsagePeakWatts_Object = MibTableColumn
powerUsagePeakWatts = _PowerUsagePeakWatts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 9),
    _PowerUsagePeakWatts_Type()
)
powerUsagePeakWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakWatts.setStatus("mandatory")
_PowerUsagePeakWattsStartDateName_Type = DellDateName
_PowerUsagePeakWattsStartDateName_Object = MibTableColumn
powerUsagePeakWattsStartDateName = _PowerUsagePeakWattsStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 10),
    _PowerUsagePeakWattsStartDateName_Type()
)
powerUsagePeakWattsStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakWattsStartDateName.setStatus("mandatory")
_PowerUsagePeakWattsReadingDateName_Type = DellDateName
_PowerUsagePeakWattsReadingDateName_Object = MibTableColumn
powerUsagePeakWattsReadingDateName = _PowerUsagePeakWattsReadingDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 11),
    _PowerUsagePeakWattsReadingDateName_Type()
)
powerUsagePeakWattsReadingDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakWattsReadingDateName.setStatus("mandatory")
_PowerUsagePeakAmps_Type = DellUnsigned32BitRange
_PowerUsagePeakAmps_Object = MibTableColumn
powerUsagePeakAmps = _PowerUsagePeakAmps_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 12),
    _PowerUsagePeakAmps_Type()
)
powerUsagePeakAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakAmps.setStatus("mandatory")
_PowerUsagePeakAmpsStartDateName_Type = DellDateName
_PowerUsagePeakAmpsStartDateName_Object = MibTableColumn
powerUsagePeakAmpsStartDateName = _PowerUsagePeakAmpsStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 13),
    _PowerUsagePeakAmpsStartDateName_Type()
)
powerUsagePeakAmpsStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakAmpsStartDateName.setStatus("mandatory")
_PowerUsagePeakAmpsReadingDateName_Type = DellDateName
_PowerUsagePeakAmpsReadingDateName_Object = MibTableColumn
powerUsagePeakAmpsReadingDateName = _PowerUsagePeakAmpsReadingDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 14),
    _PowerUsagePeakAmpsReadingDateName_Type()
)
powerUsagePeakAmpsReadingDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakAmpsReadingDateName.setStatus("mandatory")
_PowerUsageIdlePower_Type = DellUnsigned32BitRange
_PowerUsageIdlePower_Object = MibTableColumn
powerUsageIdlePower = _PowerUsageIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 15),
    _PowerUsageIdlePower_Type()
)
powerUsageIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageIdlePower.setStatus("mandatory")
_PowerUsageMaxPotentialPower_Type = DellUnsigned32BitRange
_PowerUsageMaxPotentialPower_Object = MibTableColumn
powerUsageMaxPotentialPower = _PowerUsageMaxPotentialPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 16),
    _PowerUsageMaxPotentialPower_Type()
)
powerUsageMaxPotentialPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageMaxPotentialPower.setStatus("mandatory")
_PowerUsagePowerCapCapabilities_Type = DellPowerCapCapabilities
_PowerUsagePowerCapCapabilities_Object = MibTableColumn
powerUsagePowerCapCapabilities = _PowerUsagePowerCapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 17),
    _PowerUsagePowerCapCapabilities_Type()
)
powerUsagePowerCapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePowerCapCapabilities.setStatus("mandatory")
_PowerUsagePowerCapSetting_Type = DellPowerCapSetting
_PowerUsagePowerCapSetting_Object = MibTableColumn
powerUsagePowerCapSetting = _PowerUsagePowerCapSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 18),
    _PowerUsagePowerCapSetting_Type()
)
powerUsagePowerCapSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePowerCapSetting.setStatus("mandatory")
_PowerUsagePowerCapValue_Type = DellUnsigned32BitRange
_PowerUsagePowerCapValue_Object = MibTableColumn
powerUsagePowerCapValue = _PowerUsagePowerCapValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 19),
    _PowerUsagePowerCapValue_Type()
)
powerUsagePowerCapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePowerCapValue.setStatus("mandatory")
_PowerUsageInstantaneousHeadroom_Type = DellUnsigned32BitRange
_PowerUsageInstantaneousHeadroom_Object = MibTableColumn
powerUsageInstantaneousHeadroom = _PowerUsageInstantaneousHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 20),
    _PowerUsageInstantaneousHeadroom_Type()
)
powerUsageInstantaneousHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageInstantaneousHeadroom.setStatus("mandatory")
_PowerUsagePeakHeadroom_Type = DellUnsigned32BitRange
_PowerUsagePeakHeadroom_Object = MibTableColumn
powerUsagePeakHeadroom = _PowerUsagePeakHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 60, 1, 21),
    _PowerUsagePeakHeadroom_Type()
)
powerUsagePeakHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakHeadroom.setStatus("mandatory")
_PowerProfileTable_Object = MibTable
powerProfileTable = _PowerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70)
)
if mibBuilder.loadTexts:
    powerProfileTable.setStatus("mandatory")
_PowerProfileTableEntry_Object = MibTableRow
powerProfileTableEntry = _PowerProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1)
)
powerProfileTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "powerProfileChassisIndex"),
    (0, "MIB-Dell-10892", "powerProfileIndex"),
)
if mibBuilder.loadTexts:
    powerProfileTableEntry.setStatus("mandatory")
_PowerProfileChassisIndex_Type = DellObjectRange
_PowerProfileChassisIndex_Object = MibTableColumn
powerProfileChassisIndex = _PowerProfileChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 1),
    _PowerProfileChassisIndex_Type()
)
powerProfileChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileChassisIndex.setStatus("mandatory")
_PowerProfileIndex_Type = DellObjectRange
_PowerProfileIndex_Object = MibTableColumn
powerProfileIndex = _PowerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 2),
    _PowerProfileIndex_Type()
)
powerProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileIndex.setStatus("mandatory")
_PowerProfileSupportedProfiles_Type = DellPowerProfileType
_PowerProfileSupportedProfiles_Object = MibTableColumn
powerProfileSupportedProfiles = _PowerProfileSupportedProfiles_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 3),
    _PowerProfileSupportedProfiles_Type()
)
powerProfileSupportedProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileSupportedProfiles.setStatus("mandatory")
_PowerProfileSetting_Type = DellPowerProfileType
_PowerProfileSetting_Object = MibTableColumn
powerProfileSetting = _PowerProfileSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 4),
    _PowerProfileSetting_Type()
)
powerProfileSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileSetting.setStatus("mandatory")
_PowerProfileCustomCPUMgmtCapabilities_Type = DellCPUPowerPerformanceManagementType
_PowerProfileCustomCPUMgmtCapabilities_Object = MibTableColumn
powerProfileCustomCPUMgmtCapabilities = _PowerProfileCustomCPUMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 5),
    _PowerProfileCustomCPUMgmtCapabilities_Type()
)
powerProfileCustomCPUMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileCustomCPUMgmtCapabilities.setStatus("mandatory")
_PowerProfileCustomCPUMgmtSetting_Type = DellCPUPowerPerformanceManagementType
_PowerProfileCustomCPUMgmtSetting_Object = MibTableColumn
powerProfileCustomCPUMgmtSetting = _PowerProfileCustomCPUMgmtSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 6),
    _PowerProfileCustomCPUMgmtSetting_Type()
)
powerProfileCustomCPUMgmtSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileCustomCPUMgmtSetting.setStatus("mandatory")
_PowerProfileCustomMemoryMgmtCapabilities_Type = DellMemoryPowerPerformanceManagementType
_PowerProfileCustomMemoryMgmtCapabilities_Object = MibTableColumn
powerProfileCustomMemoryMgmtCapabilities = _PowerProfileCustomMemoryMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 7),
    _PowerProfileCustomMemoryMgmtCapabilities_Type()
)
powerProfileCustomMemoryMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileCustomMemoryMgmtCapabilities.setStatus("mandatory")
_PowerProfileCustomMemoryMgmtSetting_Type = DellMemoryPowerPerformanceManagementType
_PowerProfileCustomMemoryMgmtSetting_Object = MibTableColumn
powerProfileCustomMemoryMgmtSetting = _PowerProfileCustomMemoryMgmtSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 8),
    _PowerProfileCustomMemoryMgmtSetting_Type()
)
powerProfileCustomMemoryMgmtSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileCustomMemoryMgmtSetting.setStatus("mandatory")
_PowerProfileCustomFanMgmtCapabilities_Type = DellFanPowerPerformanceManagementType
_PowerProfileCustomFanMgmtCapabilities_Object = MibTableColumn
powerProfileCustomFanMgmtCapabilities = _PowerProfileCustomFanMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 9),
    _PowerProfileCustomFanMgmtCapabilities_Type()
)
powerProfileCustomFanMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileCustomFanMgmtCapabilities.setStatus("mandatory")
_PowerProfileCustomFanMgmtSetting_Type = DellFanPowerPerformanceManagementType
_PowerProfileCustomFanMgmtSetting_Object = MibTableColumn
powerProfileCustomFanMgmtSetting = _PowerProfileCustomFanMgmtSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 70, 1, 10),
    _PowerProfileCustomFanMgmtSetting_Type()
)
powerProfileCustomFanMgmtSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerProfileCustomFanMgmtSetting.setStatus("mandatory")
_ThermalGroup_ObjectIdentity = ObjectIdentity
thermalGroup = _ThermalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700)
)
_CoolingUnitTable_Object = MibTable
coolingUnitTable = _CoolingUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10)
)
if mibBuilder.loadTexts:
    coolingUnitTable.setStatus("mandatory")
_CoolingUnitTableEntry_Object = MibTableRow
coolingUnitTableEntry = _CoolingUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1)
)
coolingUnitTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "coolingUnitchassisIndex"),
    (0, "MIB-Dell-10892", "coolingUnitIndex"),
)
if mibBuilder.loadTexts:
    coolingUnitTableEntry.setStatus("mandatory")
_CoolingUnitchassisIndex_Type = DellObjectRange
_CoolingUnitchassisIndex_Object = MibTableColumn
coolingUnitchassisIndex = _CoolingUnitchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 1),
    _CoolingUnitchassisIndex_Type()
)
coolingUnitchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitchassisIndex.setStatus("mandatory")
_CoolingUnitIndex_Type = DellObjectRange
_CoolingUnitIndex_Object = MibTableColumn
coolingUnitIndex = _CoolingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 2),
    _CoolingUnitIndex_Type()
)
coolingUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitIndex.setStatus("mandatory")
_CoolingUnitStateCapabilties_Type = DellStateCapabilities
_CoolingUnitStateCapabilties_Object = MibTableColumn
coolingUnitStateCapabilties = _CoolingUnitStateCapabilties_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 3),
    _CoolingUnitStateCapabilties_Type()
)
coolingUnitStateCapabilties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitStateCapabilties.setStatus("mandatory")
_CoolingUnitStateSettings_Type = DellStateSettings
_CoolingUnitStateSettings_Object = MibTableColumn
coolingUnitStateSettings = _CoolingUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 4),
    _CoolingUnitStateSettings_Type()
)
coolingUnitStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitStateSettings.setStatus("mandatory")
_CoolingUnitRedundancyStatus_Type = DellStatusRedundancy
_CoolingUnitRedundancyStatus_Object = MibTableColumn
coolingUnitRedundancyStatus = _CoolingUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 5),
    _CoolingUnitRedundancyStatus_Type()
)
coolingUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitRedundancyStatus.setStatus("mandatory")
_CoolingDeviceCountForRedundancy_Type = DellObjectRange
_CoolingDeviceCountForRedundancy_Object = MibTableColumn
coolingDeviceCountForRedundancy = _CoolingDeviceCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 6),
    _CoolingDeviceCountForRedundancy_Type()
)
coolingDeviceCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceCountForRedundancy.setStatus("mandatory")
_CoolingUnitName_Type = DellString
_CoolingUnitName_Object = MibTableColumn
coolingUnitName = _CoolingUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 7),
    _CoolingUnitName_Type()
)
coolingUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitName.setStatus("mandatory")
_CoolingUnitStatus_Type = DellStatus
_CoolingUnitStatus_Object = MibTableColumn
coolingUnitStatus = _CoolingUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 8),
    _CoolingUnitStatus_Type()
)
coolingUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitStatus.setStatus("mandatory")
_CoolingDeviceTable_Object = MibTable
coolingDeviceTable = _CoolingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12)
)
if mibBuilder.loadTexts:
    coolingDeviceTable.setStatus("mandatory")
_CoolingDeviceTableEntry_Object = MibTableRow
coolingDeviceTableEntry = _CoolingDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1)
)
coolingDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "coolingDevicechassisIndex"),
    (0, "MIB-Dell-10892", "coolingDeviceIndex"),
)
if mibBuilder.loadTexts:
    coolingDeviceTableEntry.setStatus("mandatory")
_CoolingDevicechassisIndex_Type = DellObjectRange
_CoolingDevicechassisIndex_Object = MibTableColumn
coolingDevicechassisIndex = _CoolingDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 1),
    _CoolingDevicechassisIndex_Type()
)
coolingDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDevicechassisIndex.setStatus("mandatory")
_CoolingDeviceIndex_Type = DellObjectRange
_CoolingDeviceIndex_Object = MibTableColumn
coolingDeviceIndex = _CoolingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 2),
    _CoolingDeviceIndex_Type()
)
coolingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceIndex.setStatus("mandatory")
_CoolingDeviceStateCapabilities_Type = DellStateCapabilities
_CoolingDeviceStateCapabilities_Object = MibTableColumn
coolingDeviceStateCapabilities = _CoolingDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 3),
    _CoolingDeviceStateCapabilities_Type()
)
coolingDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStateCapabilities.setStatus("mandatory")
_CoolingDeviceStateSettings_Type = DellStateSettings
_CoolingDeviceStateSettings_Object = MibTableColumn
coolingDeviceStateSettings = _CoolingDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 4),
    _CoolingDeviceStateSettings_Type()
)
coolingDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStateSettings.setStatus("mandatory")
_CoolingDeviceStatus_Type = DellStatusProbe
_CoolingDeviceStatus_Object = MibTableColumn
coolingDeviceStatus = _CoolingDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 5),
    _CoolingDeviceStatus_Type()
)
coolingDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStatus.setStatus("mandatory")
_CoolingDeviceReading_Type = DellSigned32BitRange
_CoolingDeviceReading_Object = MibTableColumn
coolingDeviceReading = _CoolingDeviceReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 6),
    _CoolingDeviceReading_Type()
)
coolingDeviceReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceReading.setStatus("mandatory")
_CoolingDeviceType_Type = DellCoolingDeviceType
_CoolingDeviceType_Object = MibTableColumn
coolingDeviceType = _CoolingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 7),
    _CoolingDeviceType_Type()
)
coolingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceType.setStatus("mandatory")
_CoolingDeviceLocationName_Type = DellString
_CoolingDeviceLocationName_Object = MibTableColumn
coolingDeviceLocationName = _CoolingDeviceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 8),
    _CoolingDeviceLocationName_Type()
)
coolingDeviceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLocationName.setStatus("mandatory")
_CoolingDeviceUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_CoolingDeviceUpperNonRecoverableThreshold_Object = MibTableColumn
coolingDeviceUpperNonRecoverableThreshold = _CoolingDeviceUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 9),
    _CoolingDeviceUpperNonRecoverableThreshold_Type()
)
coolingDeviceUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonRecoverableThreshold.setStatus("mandatory")
_CoolingDeviceUpperCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceUpperCriticalThreshold_Object = MibTableColumn
coolingDeviceUpperCriticalThreshold = _CoolingDeviceUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 10),
    _CoolingDeviceUpperCriticalThreshold_Type()
)
coolingDeviceUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperCriticalThreshold.setStatus("mandatory")
_CoolingDeviceUpperNonCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceUpperNonCriticalThreshold_Object = MibTableColumn
coolingDeviceUpperNonCriticalThreshold = _CoolingDeviceUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 11),
    _CoolingDeviceUpperNonCriticalThreshold_Type()
)
coolingDeviceUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonCriticalThreshold.setStatus("mandatory")
_CoolingDeviceLowerNonCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceLowerNonCriticalThreshold_Object = MibTableColumn
coolingDeviceLowerNonCriticalThreshold = _CoolingDeviceLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 12),
    _CoolingDeviceLowerNonCriticalThreshold_Type()
)
coolingDeviceLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonCriticalThreshold.setStatus("mandatory")
_CoolingDeviceLowerCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceLowerCriticalThreshold_Object = MibTableColumn
coolingDeviceLowerCriticalThreshold = _CoolingDeviceLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 13),
    _CoolingDeviceLowerCriticalThreshold_Type()
)
coolingDeviceLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerCriticalThreshold.setStatus("mandatory")
_CoolingDeviceLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_CoolingDeviceLowerNonRecoverableThreshold_Object = MibTableColumn
coolingDeviceLowerNonRecoverableThreshold = _CoolingDeviceLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 14),
    _CoolingDeviceLowerNonRecoverableThreshold_Type()
)
coolingDeviceLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonRecoverableThreshold.setStatus("mandatory")
_CoolingDevicecoolingUnitIndexReference_Type = DellObjectRange
_CoolingDevicecoolingUnitIndexReference_Object = MibTableColumn
coolingDevicecoolingUnitIndexReference = _CoolingDevicecoolingUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 15),
    _CoolingDevicecoolingUnitIndexReference_Type()
)
coolingDevicecoolingUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDevicecoolingUnitIndexReference.setStatus("mandatory")
_CoolingDeviceSubType_Type = DellCoolingDeviceSubType
_CoolingDeviceSubType_Object = MibTableColumn
coolingDeviceSubType = _CoolingDeviceSubType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 16),
    _CoolingDeviceSubType_Type()
)
coolingDeviceSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceSubType.setStatus("mandatory")
_CoolingDeviceProbeCapabilities_Type = DellProbeCapabilities
_CoolingDeviceProbeCapabilities_Object = MibTableColumn
coolingDeviceProbeCapabilities = _CoolingDeviceProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 17),
    _CoolingDeviceProbeCapabilities_Type()
)
coolingDeviceProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceProbeCapabilities.setStatus("mandatory")
_CoolingDeviceDiscreteReading_Type = DellCoolingDeviceDiscreteReading
_CoolingDeviceDiscreteReading_Object = MibTableColumn
coolingDeviceDiscreteReading = _CoolingDeviceDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 18),
    _CoolingDeviceDiscreteReading_Type()
)
coolingDeviceDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceDiscreteReading.setStatus("mandatory")
_TemperatureProbeTable_Object = MibTable
temperatureProbeTable = _TemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20)
)
if mibBuilder.loadTexts:
    temperatureProbeTable.setStatus("mandatory")
_TemperatureProbeTableEntry_Object = MibTableRow
temperatureProbeTableEntry = _TemperatureProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1)
)
temperatureProbeTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "temperatureProbechassisIndex"),
    (0, "MIB-Dell-10892", "temperatureProbeIndex"),
)
if mibBuilder.loadTexts:
    temperatureProbeTableEntry.setStatus("mandatory")
_TemperatureProbechassisIndex_Type = DellObjectRange
_TemperatureProbechassisIndex_Object = MibTableColumn
temperatureProbechassisIndex = _TemperatureProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 1),
    _TemperatureProbechassisIndex_Type()
)
temperatureProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbechassisIndex.setStatus("mandatory")
_TemperatureProbeIndex_Type = DellObjectRange
_TemperatureProbeIndex_Object = MibTableColumn
temperatureProbeIndex = _TemperatureProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 2),
    _TemperatureProbeIndex_Type()
)
temperatureProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeIndex.setStatus("mandatory")
_TemperatureProbeStateCapabilities_Type = DellStateCapabilities
_TemperatureProbeStateCapabilities_Object = MibTableColumn
temperatureProbeStateCapabilities = _TemperatureProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 3),
    _TemperatureProbeStateCapabilities_Type()
)
temperatureProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStateCapabilities.setStatus("mandatory")
_TemperatureProbeStateSettings_Type = DellStateSettings
_TemperatureProbeStateSettings_Object = MibTableColumn
temperatureProbeStateSettings = _TemperatureProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 4),
    _TemperatureProbeStateSettings_Type()
)
temperatureProbeStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStateSettings.setStatus("mandatory")
_TemperatureProbeStatus_Type = DellStatusProbe
_TemperatureProbeStatus_Object = MibTableColumn
temperatureProbeStatus = _TemperatureProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 5),
    _TemperatureProbeStatus_Type()
)
temperatureProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStatus.setStatus("mandatory")
_TemperatureProbeReading_Type = DellSigned32BitRange
_TemperatureProbeReading_Object = MibTableColumn
temperatureProbeReading = _TemperatureProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 6),
    _TemperatureProbeReading_Type()
)
temperatureProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeReading.setStatus("mandatory")
_TemperatureProbeType_Type = DellTemperatureProbeType
_TemperatureProbeType_Object = MibTableColumn
temperatureProbeType = _TemperatureProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 7),
    _TemperatureProbeType_Type()
)
temperatureProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeType.setStatus("mandatory")
_TemperatureProbeLocationName_Type = DellString
_TemperatureProbeLocationName_Object = MibTableColumn
temperatureProbeLocationName = _TemperatureProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 8),
    _TemperatureProbeLocationName_Type()
)
temperatureProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLocationName.setStatus("mandatory")
_TemperatureProbeUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_TemperatureProbeUpperNonRecoverableThreshold_Object = MibTableColumn
temperatureProbeUpperNonRecoverableThreshold = _TemperatureProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 9),
    _TemperatureProbeUpperNonRecoverableThreshold_Type()
)
temperatureProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonRecoverableThreshold.setStatus("mandatory")
_TemperatureProbeUpperCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeUpperCriticalThreshold_Object = MibTableColumn
temperatureProbeUpperCriticalThreshold = _TemperatureProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 10),
    _TemperatureProbeUpperCriticalThreshold_Type()
)
temperatureProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperCriticalThreshold.setStatus("mandatory")
_TemperatureProbeUpperNonCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeUpperNonCriticalThreshold_Object = MibTableColumn
temperatureProbeUpperNonCriticalThreshold = _TemperatureProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 11),
    _TemperatureProbeUpperNonCriticalThreshold_Type()
)
temperatureProbeUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonCriticalThreshold.setStatus("mandatory")
_TemperatureProbeLowerNonCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeLowerNonCriticalThreshold_Object = MibTableColumn
temperatureProbeLowerNonCriticalThreshold = _TemperatureProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 12),
    _TemperatureProbeLowerNonCriticalThreshold_Type()
)
temperatureProbeLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonCriticalThreshold.setStatus("mandatory")
_TemperatureProbeLowerCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeLowerCriticalThreshold_Object = MibTableColumn
temperatureProbeLowerCriticalThreshold = _TemperatureProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 13),
    _TemperatureProbeLowerCriticalThreshold_Type()
)
temperatureProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerCriticalThreshold.setStatus("mandatory")
_TemperatureProbeLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_TemperatureProbeLowerNonRecoverableThreshold_Object = MibTableColumn
temperatureProbeLowerNonRecoverableThreshold = _TemperatureProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 14),
    _TemperatureProbeLowerNonRecoverableThreshold_Type()
)
temperatureProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonRecoverableThreshold.setStatus("mandatory")
_TemperatureProbeProbeCapabilities_Type = DellProbeCapabilities
_TemperatureProbeProbeCapabilities_Object = MibTableColumn
temperatureProbeProbeCapabilities = _TemperatureProbeProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 15),
    _TemperatureProbeProbeCapabilities_Type()
)
temperatureProbeProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeProbeCapabilities.setStatus("mandatory")
_TemperatureProbeDiscreteReading_Type = DellTemperatureDiscreteReading
_TemperatureProbeDiscreteReading_Object = MibTableColumn
temperatureProbeDiscreteReading = _TemperatureProbeDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 16),
    _TemperatureProbeDiscreteReading_Type()
)
temperatureProbeDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeDiscreteReading.setStatus("mandatory")
_UserSecurityGroup_ObjectIdentity = ObjectIdentity
userSecurityGroup = _UserSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800)
)
_UserSecurityTable_Object = MibTable
userSecurityTable = _UserSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10)
)
if mibBuilder.loadTexts:
    userSecurityTable.setStatus("mandatory")
_UserSecurityTableEntry_Object = MibTableRow
userSecurityTableEntry = _UserSecurityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1)
)
userSecurityTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "userSecuritychassisIndex"),
    (0, "MIB-Dell-10892", "userSecurityIndex"),
)
if mibBuilder.loadTexts:
    userSecurityTableEntry.setStatus("mandatory")
_UserSecuritychassisIndex_Type = DellObjectRange
_UserSecuritychassisIndex_Object = MibTableColumn
userSecuritychassisIndex = _UserSecuritychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 1),
    _UserSecuritychassisIndex_Type()
)
userSecuritychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecuritychassisIndex.setStatus("mandatory")
_UserSecurityIndex_Type = DellObjectRange
_UserSecurityIndex_Object = MibTableColumn
userSecurityIndex = _UserSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 2),
    _UserSecurityIndex_Type()
)
userSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityIndex.setStatus("mandatory")
_UserSecurityUserName_Type = DellSecurityString
_UserSecurityUserName_Object = MibTableColumn
userSecurityUserName = _UserSecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 3),
    _UserSecurityUserName_Type()
)
userSecurityUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityUserName.setStatus("mandatory")
_UserSecurityControlName_Type = DellSecurityString
_UserSecurityControlName_Object = MibTableColumn
userSecurityControlName = _UserSecurityControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 4),
    _UserSecurityControlName_Type()
)
userSecurityControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityControlName.setStatus("mandatory")
_UserSecurityRequestName_Type = DellSecurityString
_UserSecurityRequestName_Object = MibTableColumn
userSecurityRequestName = _UserSecurityRequestName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 5),
    _UserSecurityRequestName_Type()
)
userSecurityRequestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityRequestName.setStatus("mandatory")
_RemoteFlashBIOSGroup_ObjectIdentity = ObjectIdentity
remoteFlashBIOSGroup = _RemoteFlashBIOSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900)
)
_RemoteFlashBIOSTable_Object = MibTable
remoteFlashBIOSTable = _RemoteFlashBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10)
)
if mibBuilder.loadTexts:
    remoteFlashBIOSTable.setStatus("mandatory")
_RemoteFlashBIOSTableEntry_Object = MibTableRow
remoteFlashBIOSTableEntry = _RemoteFlashBIOSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1)
)
remoteFlashBIOSTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteFlashBIOSchassisIndex"),
    (0, "MIB-Dell-10892", "remoteFlashBIOSIndex"),
)
if mibBuilder.loadTexts:
    remoteFlashBIOSTableEntry.setStatus("mandatory")
_RemoteFlashBIOSchassisIndex_Type = DellObjectRange
_RemoteFlashBIOSchassisIndex_Object = MibTableColumn
remoteFlashBIOSchassisIndex = _RemoteFlashBIOSchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 1),
    _RemoteFlashBIOSchassisIndex_Type()
)
remoteFlashBIOSchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSchassisIndex.setStatus("mandatory")
_RemoteFlashBIOSIndex_Type = DellObjectRange
_RemoteFlashBIOSIndex_Object = MibTableColumn
remoteFlashBIOSIndex = _RemoteFlashBIOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 2),
    _RemoteFlashBIOSIndex_Type()
)
remoteFlashBIOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSIndex.setStatus("mandatory")
_RemoteFlashBIOSStateCapabilitiesUnique_Type = DellRemoteFlashBIOSStateCapabilitiesUnique
_RemoteFlashBIOSStateCapabilitiesUnique_Object = MibTableColumn
remoteFlashBIOSStateCapabilitiesUnique = _RemoteFlashBIOSStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 3),
    _RemoteFlashBIOSStateCapabilitiesUnique_Type()
)
remoteFlashBIOSStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSStateCapabilitiesUnique.setStatus("mandatory")
_RemoteFlashBIOSStateSettingsUnique_Type = DellRemoteFlashBIOSStateSettingsUnique
_RemoteFlashBIOSStateSettingsUnique_Object = MibTableColumn
remoteFlashBIOSStateSettingsUnique = _RemoteFlashBIOSStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 4),
    _RemoteFlashBIOSStateSettingsUnique_Type()
)
remoteFlashBIOSStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSStateSettingsUnique.setStatus("mandatory")
_RemoteFlashBIOSStatus_Type = DellStatus
_RemoteFlashBIOSStatus_Object = MibTableColumn
remoteFlashBIOSStatus = _RemoteFlashBIOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 5),
    _RemoteFlashBIOSStatus_Type()
)
remoteFlashBIOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSStatus.setStatus("mandatory")
_RemoteFlashBIOSLastBIOSDateName_Type = DellDateName
_RemoteFlashBIOSLastBIOSDateName_Object = MibTableColumn
remoteFlashBIOSLastBIOSDateName = _RemoteFlashBIOSLastBIOSDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 6),
    _RemoteFlashBIOSLastBIOSDateName_Type()
)
remoteFlashBIOSLastBIOSDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSLastBIOSDateName.setStatus("mandatory")
_RemoteFlashBIOSCompletionCode_Type = DellRemoteFlashBIOSCompletionCode
_RemoteFlashBIOSCompletionCode_Object = MibTableColumn
remoteFlashBIOSCompletionCode = _RemoteFlashBIOSCompletionCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 7),
    _RemoteFlashBIOSCompletionCode_Type()
)
remoteFlashBIOSCompletionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSCompletionCode.setStatus("mandatory")
_RemoteFlashBIOSMinimumContiguousMemory_Type = DellUnsigned32BitRange
_RemoteFlashBIOSMinimumContiguousMemory_Object = MibTableColumn
remoteFlashBIOSMinimumContiguousMemory = _RemoteFlashBIOSMinimumContiguousMemory_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 8),
    _RemoteFlashBIOSMinimumContiguousMemory_Type()
)
remoteFlashBIOSMinimumContiguousMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSMinimumContiguousMemory.setStatus("mandatory")
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000)
)
_PointingPortTable_Object = MibTable
pointingPortTable = _PointingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10)
)
if mibBuilder.loadTexts:
    pointingPortTable.setStatus("mandatory")
_PointingPortTableEntry_Object = MibTableRow
pointingPortTableEntry = _PointingPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1)
)
pointingPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pointingPortchassisIndex"),
    (0, "MIB-Dell-10892", "pointingPortIndex"),
)
if mibBuilder.loadTexts:
    pointingPortTableEntry.setStatus("mandatory")
_PointingPortchassisIndex_Type = DellObjectRange
_PointingPortchassisIndex_Object = MibTableColumn
pointingPortchassisIndex = _PointingPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 1),
    _PointingPortchassisIndex_Type()
)
pointingPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortchassisIndex.setStatus("mandatory")
_PointingPortIndex_Type = DellObjectRange
_PointingPortIndex_Object = MibTableColumn
pointingPortIndex = _PointingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 2),
    _PointingPortIndex_Type()
)
pointingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortIndex.setStatus("mandatory")
_PointingPortStateCapabilities_Type = DellStateCapabilities
_PointingPortStateCapabilities_Object = MibTableColumn
pointingPortStateCapabilities = _PointingPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 3),
    _PointingPortStateCapabilities_Type()
)
pointingPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortStateCapabilities.setStatus("mandatory")
_PointingPortStateSettings_Type = DellStateSettings
_PointingPortStateSettings_Object = MibTableColumn
pointingPortStateSettings = _PointingPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 4),
    _PointingPortStateSettings_Type()
)
pointingPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortStateSettings.setStatus("mandatory")
_PointingPortStatus_Type = DellStatus
_PointingPortStatus_Object = MibTableColumn
pointingPortStatus = _PointingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 5),
    _PointingPortStatus_Type()
)
pointingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortStatus.setStatus("mandatory")
_PointingPortSecurityState_Type = DellPortSecurityState
_PointingPortSecurityState_Object = MibTableColumn
pointingPortSecurityState = _PointingPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 6),
    _PointingPortSecurityState_Type()
)
pointingPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortSecurityState.setStatus("mandatory")
_PointingPortConnectorType_Type = DellPointingPortConnectorType
_PointingPortConnectorType_Object = MibTableColumn
pointingPortConnectorType = _PointingPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 7),
    _PointingPortConnectorType_Type()
)
pointingPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortConnectorType.setStatus("mandatory")
_PointingPortName_Type = DellString
_PointingPortName_Object = MibTableColumn
pointingPortName = _PointingPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 8),
    _PointingPortName_Type()
)
pointingPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortName.setStatus("mandatory")
_PointingPortBIOSConnectorType_Type = DellGenericPortConnectorType
_PointingPortBIOSConnectorType_Object = MibTableColumn
pointingPortBIOSConnectorType = _PointingPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 9),
    _PointingPortBIOSConnectorType_Type()
)
pointingPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortBIOSConnectorType.setStatus("mandatory")
_KeyboardPortTable_Object = MibTable
keyboardPortTable = _KeyboardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20)
)
if mibBuilder.loadTexts:
    keyboardPortTable.setStatus("mandatory")
_KeyboardPortTableEntry_Object = MibTableRow
keyboardPortTableEntry = _KeyboardPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1)
)
keyboardPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "keyboardPortchassisIndex"),
    (0, "MIB-Dell-10892", "keyboardPortIndex"),
)
if mibBuilder.loadTexts:
    keyboardPortTableEntry.setStatus("mandatory")
_KeyboardPortchassisIndex_Type = DellObjectRange
_KeyboardPortchassisIndex_Object = MibTableColumn
keyboardPortchassisIndex = _KeyboardPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 1),
    _KeyboardPortchassisIndex_Type()
)
keyboardPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortchassisIndex.setStatus("mandatory")
_KeyboardPortIndex_Type = DellObjectRange
_KeyboardPortIndex_Object = MibTableColumn
keyboardPortIndex = _KeyboardPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 2),
    _KeyboardPortIndex_Type()
)
keyboardPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortIndex.setStatus("mandatory")
_KeyboardPortStateCapabilities_Type = DellStateCapabilities
_KeyboardPortStateCapabilities_Object = MibTableColumn
keyboardPortStateCapabilities = _KeyboardPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 3),
    _KeyboardPortStateCapabilities_Type()
)
keyboardPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortStateCapabilities.setStatus("mandatory")
_KeyboardPortStateSettings_Type = DellStateSettings
_KeyboardPortStateSettings_Object = MibTableColumn
keyboardPortStateSettings = _KeyboardPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 4),
    _KeyboardPortStateSettings_Type()
)
keyboardPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortStateSettings.setStatus("mandatory")
_KeyboardPortStatus_Type = DellStatus
_KeyboardPortStatus_Object = MibTableColumn
keyboardPortStatus = _KeyboardPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 5),
    _KeyboardPortStatus_Type()
)
keyboardPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortStatus.setStatus("mandatory")
_KeyboardPortSecurityState_Type = DellPortSecurityState
_KeyboardPortSecurityState_Object = MibTableColumn
keyboardPortSecurityState = _KeyboardPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 6),
    _KeyboardPortSecurityState_Type()
)
keyboardPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortSecurityState.setStatus("mandatory")
_KeyboardPortConnectorType_Type = DellKeyboardPortConnectorType
_KeyboardPortConnectorType_Object = MibTableColumn
keyboardPortConnectorType = _KeyboardPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 7),
    _KeyboardPortConnectorType_Type()
)
keyboardPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortConnectorType.setStatus("mandatory")
_KeyboardPortName_Type = DellString
_KeyboardPortName_Object = MibTableColumn
keyboardPortName = _KeyboardPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 8),
    _KeyboardPortName_Type()
)
keyboardPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortName.setStatus("mandatory")
_KeyboardPortBIOSConnectorType_Type = DellGenericPortConnectorType
_KeyboardPortBIOSConnectorType_Object = MibTableColumn
keyboardPortBIOSConnectorType = _KeyboardPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 9),
    _KeyboardPortBIOSConnectorType_Type()
)
keyboardPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortBIOSConnectorType.setStatus("mandatory")
_ProcessorPortTable_Object = MibTable
processorPortTable = _ProcessorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30)
)
if mibBuilder.loadTexts:
    processorPortTable.setStatus("mandatory")
_ProcessorPortTableEntry_Object = MibTableRow
processorPortTableEntry = _ProcessorPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1)
)
processorPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "processorPortchassisIndex"),
    (0, "MIB-Dell-10892", "processorPortIndex"),
)
if mibBuilder.loadTexts:
    processorPortTableEntry.setStatus("mandatory")
_ProcessorPortchassisIndex_Type = DellObjectRange
_ProcessorPortchassisIndex_Object = MibTableColumn
processorPortchassisIndex = _ProcessorPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 1),
    _ProcessorPortchassisIndex_Type()
)
processorPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortchassisIndex.setStatus("mandatory")
_ProcessorPortIndex_Type = DellObjectRange
_ProcessorPortIndex_Object = MibTableColumn
processorPortIndex = _ProcessorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 2),
    _ProcessorPortIndex_Type()
)
processorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortIndex.setStatus("mandatory")
_ProcessorPortStateCapabilities_Type = DellStateCapabilities
_ProcessorPortStateCapabilities_Object = MibTableColumn
processorPortStateCapabilities = _ProcessorPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 3),
    _ProcessorPortStateCapabilities_Type()
)
processorPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortStateCapabilities.setStatus("mandatory")
_ProcessorPortStateSettings_Type = DellStateSettings
_ProcessorPortStateSettings_Object = MibTableColumn
processorPortStateSettings = _ProcessorPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 4),
    _ProcessorPortStateSettings_Type()
)
processorPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortStateSettings.setStatus("mandatory")
_ProcessorPortStatus_Type = DellStatus
_ProcessorPortStatus_Object = MibTableColumn
processorPortStatus = _ProcessorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 5),
    _ProcessorPortStatus_Type()
)
processorPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortStatus.setStatus("mandatory")
_ProcessorPortSecurityState_Type = DellPortSecurityState
_ProcessorPortSecurityState_Object = MibTableColumn
processorPortSecurityState = _ProcessorPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 6),
    _ProcessorPortSecurityState_Type()
)
processorPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortSecurityState.setStatus("mandatory")
_ProcessorPortConnectorType_Type = DellProcessorPortConnectorType
_ProcessorPortConnectorType_Object = MibTableColumn
processorPortConnectorType = _ProcessorPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 7),
    _ProcessorPortConnectorType_Type()
)
processorPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortConnectorType.setStatus("mandatory")
_ProcessorPortName_Type = DellString
_ProcessorPortName_Object = MibTableColumn
processorPortName = _ProcessorPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 8),
    _ProcessorPortName_Type()
)
processorPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortName.setStatus("mandatory")
_ProcessorPortBIOSConnectorType_Type = DellGenericPortConnectorType
_ProcessorPortBIOSConnectorType_Object = MibTableColumn
processorPortBIOSConnectorType = _ProcessorPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 9),
    _ProcessorPortBIOSConnectorType_Type()
)
processorPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortBIOSConnectorType.setStatus("mandatory")
_MemoryDevicePortTable_Object = MibTable
memoryDevicePortTable = _MemoryDevicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40)
)
if mibBuilder.loadTexts:
    memoryDevicePortTable.setStatus("mandatory")
_MemoryDevicePortTableEntry_Object = MibTableRow
memoryDevicePortTableEntry = _MemoryDevicePortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1)
)
memoryDevicePortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "memoryDevicePortchassisIndex"),
    (0, "MIB-Dell-10892", "memoryDevicePortIndex"),
)
if mibBuilder.loadTexts:
    memoryDevicePortTableEntry.setStatus("mandatory")
_MemoryDevicePortchassisIndex_Type = DellObjectRange
_MemoryDevicePortchassisIndex_Object = MibTableColumn
memoryDevicePortchassisIndex = _MemoryDevicePortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 1),
    _MemoryDevicePortchassisIndex_Type()
)
memoryDevicePortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortchassisIndex.setStatus("mandatory")
_MemoryDevicePortIndex_Type = DellObjectRange
_MemoryDevicePortIndex_Object = MibTableColumn
memoryDevicePortIndex = _MemoryDevicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 2),
    _MemoryDevicePortIndex_Type()
)
memoryDevicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortIndex.setStatus("mandatory")
_MemoryDevicePortStateCapabilities_Type = DellStateCapabilities
_MemoryDevicePortStateCapabilities_Object = MibTableColumn
memoryDevicePortStateCapabilities = _MemoryDevicePortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 3),
    _MemoryDevicePortStateCapabilities_Type()
)
memoryDevicePortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortStateCapabilities.setStatus("mandatory")
_MemoryDevicePortStateSettings_Type = DellStateSettings
_MemoryDevicePortStateSettings_Object = MibTableColumn
memoryDevicePortStateSettings = _MemoryDevicePortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 4),
    _MemoryDevicePortStateSettings_Type()
)
memoryDevicePortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortStateSettings.setStatus("mandatory")
_MemoryDevicePortStatus_Type = DellStatus
_MemoryDevicePortStatus_Object = MibTableColumn
memoryDevicePortStatus = _MemoryDevicePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 5),
    _MemoryDevicePortStatus_Type()
)
memoryDevicePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortStatus.setStatus("mandatory")
_MemoryDevicePortSecurityState_Type = DellPortSecurityState
_MemoryDevicePortSecurityState_Object = MibTableColumn
memoryDevicePortSecurityState = _MemoryDevicePortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 6),
    _MemoryDevicePortSecurityState_Type()
)
memoryDevicePortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortSecurityState.setStatus("mandatory")
_MemoryDevicePortConnectorType_Type = DellMemoryDevicePortConnectorType
_MemoryDevicePortConnectorType_Object = MibTableColumn
memoryDevicePortConnectorType = _MemoryDevicePortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 7),
    _MemoryDevicePortConnectorType_Type()
)
memoryDevicePortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortConnectorType.setStatus("mandatory")
_MemoryDevicePortName_Type = DellString
_MemoryDevicePortName_Object = MibTableColumn
memoryDevicePortName = _MemoryDevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 8),
    _MemoryDevicePortName_Type()
)
memoryDevicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortName.setStatus("mandatory")
_MemoryDevicePortBIOSConnectorType_Type = DellGenericPortConnectorType
_MemoryDevicePortBIOSConnectorType_Object = MibTableColumn
memoryDevicePortBIOSConnectorType = _MemoryDevicePortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 9),
    _MemoryDevicePortBIOSConnectorType_Type()
)
memoryDevicePortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortBIOSConnectorType.setStatus("mandatory")
_MemoryDevicePortPhysicalMemoryArrayIndexReference_Type = DellUnsigned32BitRange
_MemoryDevicePortPhysicalMemoryArrayIndexReference_Object = MibTableColumn
memoryDevicePortPhysicalMemoryArrayIndexReference = _MemoryDevicePortPhysicalMemoryArrayIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 10),
    _MemoryDevicePortPhysicalMemoryArrayIndexReference_Type()
)
memoryDevicePortPhysicalMemoryArrayIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortPhysicalMemoryArrayIndexReference.setStatus("mandatory")
_MemoryDevicePortPhysicalMemoryCardIndexReference_Type = DellUnsigned32BitRange
_MemoryDevicePortPhysicalMemoryCardIndexReference_Object = MibTableColumn
memoryDevicePortPhysicalMemoryCardIndexReference = _MemoryDevicePortPhysicalMemoryCardIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 11),
    _MemoryDevicePortPhysicalMemoryCardIndexReference_Type()
)
memoryDevicePortPhysicalMemoryCardIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortPhysicalMemoryCardIndexReference.setStatus("mandatory")
_MonitorPortTable_Object = MibTable
monitorPortTable = _MonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50)
)
if mibBuilder.loadTexts:
    monitorPortTable.setStatus("mandatory")
_MonitorPortTableEntry_Object = MibTableRow
monitorPortTableEntry = _MonitorPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1)
)
monitorPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "monitorPortchassisIndex"),
    (0, "MIB-Dell-10892", "monitorPortIndex"),
)
if mibBuilder.loadTexts:
    monitorPortTableEntry.setStatus("mandatory")
_MonitorPortchassisIndex_Type = DellObjectRange
_MonitorPortchassisIndex_Object = MibTableColumn
monitorPortchassisIndex = _MonitorPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 1),
    _MonitorPortchassisIndex_Type()
)
monitorPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortchassisIndex.setStatus("mandatory")
_MonitorPortIndex_Type = DellObjectRange
_MonitorPortIndex_Object = MibTableColumn
monitorPortIndex = _MonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 2),
    _MonitorPortIndex_Type()
)
monitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortIndex.setStatus("mandatory")
_MonitorPortStateCapabilities_Type = DellStateCapabilities
_MonitorPortStateCapabilities_Object = MibTableColumn
monitorPortStateCapabilities = _MonitorPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 3),
    _MonitorPortStateCapabilities_Type()
)
monitorPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortStateCapabilities.setStatus("mandatory")
_MonitorPortStateSettings_Type = DellStateSettings
_MonitorPortStateSettings_Object = MibTableColumn
monitorPortStateSettings = _MonitorPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 4),
    _MonitorPortStateSettings_Type()
)
monitorPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortStateSettings.setStatus("mandatory")
_MonitorPortStatus_Type = DellStatus
_MonitorPortStatus_Object = MibTableColumn
monitorPortStatus = _MonitorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 5),
    _MonitorPortStatus_Type()
)
monitorPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortStatus.setStatus("mandatory")
_MonitorPortSecurityState_Type = DellPortSecurityState
_MonitorPortSecurityState_Object = MibTableColumn
monitorPortSecurityState = _MonitorPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 6),
    _MonitorPortSecurityState_Type()
)
monitorPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortSecurityState.setStatus("mandatory")
_MonitorPortConnectorType_Type = DellMonitorPortConnectorType
_MonitorPortConnectorType_Object = MibTableColumn
monitorPortConnectorType = _MonitorPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 7),
    _MonitorPortConnectorType_Type()
)
monitorPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortConnectorType.setStatus("mandatory")
_MonitorPortName_Type = DellString
_MonitorPortName_Object = MibTableColumn
monitorPortName = _MonitorPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 8),
    _MonitorPortName_Type()
)
monitorPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortName.setStatus("mandatory")
_MonitorPortBIOSConnectorType_Type = DellGenericPortConnectorType
_MonitorPortBIOSConnectorType_Object = MibTableColumn
monitorPortBIOSConnectorType = _MonitorPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 9),
    _MonitorPortBIOSConnectorType_Type()
)
monitorPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortBIOSConnectorType.setStatus("mandatory")
_SCSIPortTable_Object = MibTable
sCSIPortTable = _SCSIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60)
)
if mibBuilder.loadTexts:
    sCSIPortTable.setStatus("mandatory")
_SCSIPortTableEntry_Object = MibTableRow
sCSIPortTableEntry = _SCSIPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1)
)
sCSIPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "sCSIPortchassisIndex"),
    (0, "MIB-Dell-10892", "sCSIPortIndex"),
)
if mibBuilder.loadTexts:
    sCSIPortTableEntry.setStatus("mandatory")
_SCSIPortchassisIndex_Type = DellObjectRange
_SCSIPortchassisIndex_Object = MibTableColumn
sCSIPortchassisIndex = _SCSIPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 1),
    _SCSIPortchassisIndex_Type()
)
sCSIPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortchassisIndex.setStatus("mandatory")
_SCSIPortIndex_Type = DellObjectRange
_SCSIPortIndex_Object = MibTableColumn
sCSIPortIndex = _SCSIPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 2),
    _SCSIPortIndex_Type()
)
sCSIPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortIndex.setStatus("mandatory")
_SCSIPortStateCapabilities_Type = DellStateCapabilities
_SCSIPortStateCapabilities_Object = MibTableColumn
sCSIPortStateCapabilities = _SCSIPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 3),
    _SCSIPortStateCapabilities_Type()
)
sCSIPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortStateCapabilities.setStatus("mandatory")
_SCSIPortStateSettings_Type = DellStateSettings
_SCSIPortStateSettings_Object = MibTableColumn
sCSIPortStateSettings = _SCSIPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 4),
    _SCSIPortStateSettings_Type()
)
sCSIPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortStateSettings.setStatus("mandatory")
_SCSIPortStatus_Type = DellStatus
_SCSIPortStatus_Object = MibTableColumn
sCSIPortStatus = _SCSIPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 5),
    _SCSIPortStatus_Type()
)
sCSIPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortStatus.setStatus("mandatory")
_SCSIPortSecurityState_Type = DellPortSecurityState
_SCSIPortSecurityState_Object = MibTableColumn
sCSIPortSecurityState = _SCSIPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 6),
    _SCSIPortSecurityState_Type()
)
sCSIPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortSecurityState.setStatus("mandatory")
_SCSIPortConnectorType_Type = DellSCSIPortConnectorType
_SCSIPortConnectorType_Object = MibTableColumn
sCSIPortConnectorType = _SCSIPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 7),
    _SCSIPortConnectorType_Type()
)
sCSIPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortConnectorType.setStatus("mandatory")
_SCSIPortName_Type = DellString
_SCSIPortName_Object = MibTableColumn
sCSIPortName = _SCSIPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 8),
    _SCSIPortName_Type()
)
sCSIPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortName.setStatus("mandatory")
_SCSIPortBIOSConnectorType_Type = DellGenericPortConnectorType
_SCSIPortBIOSConnectorType_Object = MibTableColumn
sCSIPortBIOSConnectorType = _SCSIPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 9),
    _SCSIPortBIOSConnectorType_Type()
)
sCSIPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortBIOSConnectorType.setStatus("mandatory")
_ParallelPortTable_Object = MibTable
parallelPortTable = _ParallelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70)
)
if mibBuilder.loadTexts:
    parallelPortTable.setStatus("mandatory")
_ParallelPortTableEntry_Object = MibTableRow
parallelPortTableEntry = _ParallelPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1)
)
parallelPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "parallelPortchassisIndex"),
    (0, "MIB-Dell-10892", "parallelPortIndex"),
)
if mibBuilder.loadTexts:
    parallelPortTableEntry.setStatus("mandatory")
_ParallelPortchassisIndex_Type = DellObjectRange
_ParallelPortchassisIndex_Object = MibTableColumn
parallelPortchassisIndex = _ParallelPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 1),
    _ParallelPortchassisIndex_Type()
)
parallelPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortchassisIndex.setStatus("mandatory")
_ParallelPortIndex_Type = DellObjectRange
_ParallelPortIndex_Object = MibTableColumn
parallelPortIndex = _ParallelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 2),
    _ParallelPortIndex_Type()
)
parallelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortIndex.setStatus("mandatory")
_ParallelPortStateCapabilities_Type = DellStateCapabilities
_ParallelPortStateCapabilities_Object = MibTableColumn
parallelPortStateCapabilities = _ParallelPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 3),
    _ParallelPortStateCapabilities_Type()
)
parallelPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortStateCapabilities.setStatus("mandatory")
_ParallelPortStateSettings_Type = DellStateSettings
_ParallelPortStateSettings_Object = MibTableColumn
parallelPortStateSettings = _ParallelPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 4),
    _ParallelPortStateSettings_Type()
)
parallelPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortStateSettings.setStatus("mandatory")
_ParallelPortStatus_Type = DellStatus
_ParallelPortStatus_Object = MibTableColumn
parallelPortStatus = _ParallelPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 5),
    _ParallelPortStatus_Type()
)
parallelPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortStatus.setStatus("mandatory")
_ParallelPortSecurityState_Type = DellPortSecurityState
_ParallelPortSecurityState_Object = MibTableColumn
parallelPortSecurityState = _ParallelPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 6),
    _ParallelPortSecurityState_Type()
)
parallelPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortSecurityState.setStatus("mandatory")
_ParallelPortConnectorType_Type = DellParallelPortConnectorType
_ParallelPortConnectorType_Object = MibTableColumn
parallelPortConnectorType = _ParallelPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 7),
    _ParallelPortConnectorType_Type()
)
parallelPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortConnectorType.setStatus("mandatory")
_ParallelPortName_Type = DellString
_ParallelPortName_Object = MibTableColumn
parallelPortName = _ParallelPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 8),
    _ParallelPortName_Type()
)
parallelPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortName.setStatus("mandatory")
_ParallelPortConnectorPinOut_Type = DellParallelPortConnectorPinout
_ParallelPortConnectorPinOut_Object = MibTableColumn
parallelPortConnectorPinOut = _ParallelPortConnectorPinOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 9),
    _ParallelPortConnectorPinOut_Type()
)
parallelPortConnectorPinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortConnectorPinOut.setStatus("mandatory")
_ParallelPortCapabilitiesUnique_Type = DellParallelPortCapabilitiesUnique
_ParallelPortCapabilitiesUnique_Object = MibTableColumn
parallelPortCapabilitiesUnique = _ParallelPortCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 10),
    _ParallelPortCapabilitiesUnique_Type()
)
parallelPortCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortCapabilitiesUnique.setStatus("mandatory")
_ParallelPortBaseIOAddress_Type = DellUnsigned64BitRange
_ParallelPortBaseIOAddress_Object = MibTableColumn
parallelPortBaseIOAddress = _ParallelPortBaseIOAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 11),
    _ParallelPortBaseIOAddress_Type()
)
parallelPortBaseIOAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortBaseIOAddress.setStatus("mandatory")
_ParallelPortIRQLevel_Type = DellUnsigned8BitRange
_ParallelPortIRQLevel_Object = MibTableColumn
parallelPortIRQLevel = _ParallelPortIRQLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 12),
    _ParallelPortIRQLevel_Type()
)
parallelPortIRQLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortIRQLevel.setStatus("mandatory")
_ParallelPortDMASupport_Type = DellBoolean
_ParallelPortDMASupport_Object = MibTableColumn
parallelPortDMASupport = _ParallelPortDMASupport_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 13),
    _ParallelPortDMASupport_Type()
)
parallelPortDMASupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortDMASupport.setStatus("mandatory")
_SerialPortTable_Object = MibTable
serialPortTable = _SerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80)
)
if mibBuilder.loadTexts:
    serialPortTable.setStatus("mandatory")
_SerialPortTableEntry_Object = MibTableRow
serialPortTableEntry = _SerialPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1)
)
serialPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "serialPortchassisIndex"),
    (0, "MIB-Dell-10892", "serialPortIndex"),
)
if mibBuilder.loadTexts:
    serialPortTableEntry.setStatus("mandatory")
_SerialPortchassisIndex_Type = DellObjectRange
_SerialPortchassisIndex_Object = MibTableColumn
serialPortchassisIndex = _SerialPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 1),
    _SerialPortchassisIndex_Type()
)
serialPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortchassisIndex.setStatus("mandatory")
_SerialPortIndex_Type = DellObjectRange
_SerialPortIndex_Object = MibTableColumn
serialPortIndex = _SerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 2),
    _SerialPortIndex_Type()
)
serialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortIndex.setStatus("mandatory")
_SerialPortStateCapabilities_Type = DellStateCapabilities
_SerialPortStateCapabilities_Object = MibTableColumn
serialPortStateCapabilities = _SerialPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 3),
    _SerialPortStateCapabilities_Type()
)
serialPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortStateCapabilities.setStatus("mandatory")
_SerialPortStateSettings_Type = DellStateSettings
_SerialPortStateSettings_Object = MibTableColumn
serialPortStateSettings = _SerialPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 4),
    _SerialPortStateSettings_Type()
)
serialPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortStateSettings.setStatus("mandatory")
_SerialPortStatus_Type = DellStatus
_SerialPortStatus_Object = MibTableColumn
serialPortStatus = _SerialPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 5),
    _SerialPortStatus_Type()
)
serialPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortStatus.setStatus("mandatory")
_SerialPortSecurityState_Type = DellPortSecurityState
_SerialPortSecurityState_Object = MibTableColumn
serialPortSecurityState = _SerialPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 6),
    _SerialPortSecurityState_Type()
)
serialPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortSecurityState.setStatus("mandatory")
_SerialPortConnectorType_Type = DellSerialPortConnectorType
_SerialPortConnectorType_Object = MibTableColumn
serialPortConnectorType = _SerialPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 7),
    _SerialPortConnectorType_Type()
)
serialPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortConnectorType.setStatus("mandatory")
_SerialPortName_Type = DellString
_SerialPortName_Object = MibTableColumn
serialPortName = _SerialPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 8),
    _SerialPortName_Type()
)
serialPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortName.setStatus("mandatory")
_SerialPortMaximumSpeed_Type = DellUnsigned32BitRange
_SerialPortMaximumSpeed_Object = MibTableColumn
serialPortMaximumSpeed = _SerialPortMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 9),
    _SerialPortMaximumSpeed_Type()
)
serialPortMaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortMaximumSpeed.setStatus("mandatory")
_SerialPortCapabilitiesUnique_Type = DellSerialPortCapabilitiesUnique
_SerialPortCapabilitiesUnique_Object = MibTableColumn
serialPortCapabilitiesUnique = _SerialPortCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 10),
    _SerialPortCapabilitiesUnique_Type()
)
serialPortCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortCapabilitiesUnique.setStatus("mandatory")
_SerialPortBaseIOAddress_Type = DellUnsigned64BitRange
_SerialPortBaseIOAddress_Object = MibTableColumn
serialPortBaseIOAddress = _SerialPortBaseIOAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 11),
    _SerialPortBaseIOAddress_Type()
)
serialPortBaseIOAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortBaseIOAddress.setStatus("mandatory")
_SerialPortIRQLevel_Type = DellUnsigned8BitRange
_SerialPortIRQLevel_Object = MibTableColumn
serialPortIRQLevel = _SerialPortIRQLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 12),
    _SerialPortIRQLevel_Type()
)
serialPortIRQLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortIRQLevel.setStatus("mandatory")
_USBPortTable_Object = MibTable
uSBPortTable = _USBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90)
)
if mibBuilder.loadTexts:
    uSBPortTable.setStatus("mandatory")
_USBPortTableEntry_Object = MibTableRow
uSBPortTableEntry = _USBPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1)
)
uSBPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "uSBPortchassisIndex"),
    (0, "MIB-Dell-10892", "uSBPortIndex"),
)
if mibBuilder.loadTexts:
    uSBPortTableEntry.setStatus("mandatory")
_USBPortchassisIndex_Type = DellObjectRange
_USBPortchassisIndex_Object = MibTableColumn
uSBPortchassisIndex = _USBPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 1),
    _USBPortchassisIndex_Type()
)
uSBPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortchassisIndex.setStatus("mandatory")
_USBPortIndex_Type = DellObjectRange
_USBPortIndex_Object = MibTableColumn
uSBPortIndex = _USBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 2),
    _USBPortIndex_Type()
)
uSBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortIndex.setStatus("mandatory")
_USBPortStateCapabilities_Type = DellStateCapabilities
_USBPortStateCapabilities_Object = MibTableColumn
uSBPortStateCapabilities = _USBPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 3),
    _USBPortStateCapabilities_Type()
)
uSBPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortStateCapabilities.setStatus("mandatory")
_USBPortStateSettings_Type = DellStateSettings
_USBPortStateSettings_Object = MibTableColumn
uSBPortStateSettings = _USBPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 4),
    _USBPortStateSettings_Type()
)
uSBPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortStateSettings.setStatus("mandatory")
_USBPortStatus_Type = DellStatus
_USBPortStatus_Object = MibTableColumn
uSBPortStatus = _USBPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 5),
    _USBPortStatus_Type()
)
uSBPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortStatus.setStatus("mandatory")
_USBPortSecurityState_Type = DellPortSecurityState
_USBPortSecurityState_Object = MibTableColumn
uSBPortSecurityState = _USBPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 6),
    _USBPortSecurityState_Type()
)
uSBPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortSecurityState.setStatus("mandatory")
_USBPortConnectorType_Type = DellUSBPortConnectorType
_USBPortConnectorType_Object = MibTableColumn
uSBPortConnectorType = _USBPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 7),
    _USBPortConnectorType_Type()
)
uSBPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortConnectorType.setStatus("mandatory")
_USBPortName_Type = DellString
_USBPortName_Object = MibTableColumn
uSBPortName = _USBPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 8),
    _USBPortName_Type()
)
uSBPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortName.setStatus("mandatory")
_USBPortBIOSConnectorType_Type = DellGenericPortConnectorType
_USBPortBIOSConnectorType_Object = MibTableColumn
uSBPortBIOSConnectorType = _USBPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 9),
    _USBPortBIOSConnectorType_Type()
)
uSBPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortBIOSConnectorType.setStatus("mandatory")
_DeviceGroup_ObjectIdentity = ObjectIdentity
deviceGroup = _DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100)
)
_PointingDeviceTable_Object = MibTable
pointingDeviceTable = _PointingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10)
)
if mibBuilder.loadTexts:
    pointingDeviceTable.setStatus("mandatory")
_PointingDeviceTableEntry_Object = MibTableRow
pointingDeviceTableEntry = _PointingDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1)
)
pointingDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pointingDevicechassisIndex"),
    (0, "MIB-Dell-10892", "pointingDeviceIndex"),
)
if mibBuilder.loadTexts:
    pointingDeviceTableEntry.setStatus("mandatory")
_PointingDevicechassisIndex_Type = DellObjectRange
_PointingDevicechassisIndex_Object = MibTableColumn
pointingDevicechassisIndex = _PointingDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 1),
    _PointingDevicechassisIndex_Type()
)
pointingDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDevicechassisIndex.setStatus("mandatory")
_PointingDeviceIndex_Type = DellObjectRange
_PointingDeviceIndex_Object = MibTableColumn
pointingDeviceIndex = _PointingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 2),
    _PointingDeviceIndex_Type()
)
pointingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceIndex.setStatus("mandatory")
_PointingDeviceStateCapabilities_Type = DellStateCapabilities
_PointingDeviceStateCapabilities_Object = MibTableColumn
pointingDeviceStateCapabilities = _PointingDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 3),
    _PointingDeviceStateCapabilities_Type()
)
pointingDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceStateCapabilities.setStatus("mandatory")
_PointingDeviceStateSettings_Type = DellStateSettings
_PointingDeviceStateSettings_Object = MibTableColumn
pointingDeviceStateSettings = _PointingDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 4),
    _PointingDeviceStateSettings_Type()
)
pointingDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceStateSettings.setStatus("mandatory")
_PointingDeviceStatus_Type = DellStatus
_PointingDeviceStatus_Object = MibTableColumn
pointingDeviceStatus = _PointingDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 5),
    _PointingDeviceStatus_Type()
)
pointingDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceStatus.setStatus("mandatory")
_PointingPortIndexReference_Type = DellObjectRange
_PointingPortIndexReference_Object = MibTableColumn
pointingPortIndexReference = _PointingPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 6),
    _PointingPortIndexReference_Type()
)
pointingPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortIndexReference.setStatus("mandatory")
_PointingDeviceType_Type = DellPointingDeviceType
_PointingDeviceType_Object = MibTableColumn
pointingDeviceType = _PointingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 7),
    _PointingDeviceType_Type()
)
pointingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceType.setStatus("mandatory")
_PointingDeviceNumberofButtons_Type = DellUnsigned8BitRange
_PointingDeviceNumberofButtons_Object = MibTableColumn
pointingDeviceNumberofButtons = _PointingDeviceNumberofButtons_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 8),
    _PointingDeviceNumberofButtons_Type()
)
pointingDeviceNumberofButtons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceNumberofButtons.setStatus("mandatory")
_KeyboardDeviceTable_Object = MibTable
keyboardDeviceTable = _KeyboardDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20)
)
if mibBuilder.loadTexts:
    keyboardDeviceTable.setStatus("mandatory")
_KeyboardDeviceTableEntry_Object = MibTableRow
keyboardDeviceTableEntry = _KeyboardDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1)
)
keyboardDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "keyboardDevicechassisIndex"),
    (0, "MIB-Dell-10892", "keyboardDeviceIndex"),
)
if mibBuilder.loadTexts:
    keyboardDeviceTableEntry.setStatus("mandatory")
_KeyboardDevicechassisIndex_Type = DellObjectRange
_KeyboardDevicechassisIndex_Object = MibTableColumn
keyboardDevicechassisIndex = _KeyboardDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 1),
    _KeyboardDevicechassisIndex_Type()
)
keyboardDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDevicechassisIndex.setStatus("mandatory")
_KeyboardDeviceIndex_Type = DellObjectRange
_KeyboardDeviceIndex_Object = MibTableColumn
keyboardDeviceIndex = _KeyboardDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 2),
    _KeyboardDeviceIndex_Type()
)
keyboardDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceIndex.setStatus("mandatory")
_KeyboardDeviceStateCapabilities_Type = DellStateCapabilities
_KeyboardDeviceStateCapabilities_Object = MibTableColumn
keyboardDeviceStateCapabilities = _KeyboardDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 3),
    _KeyboardDeviceStateCapabilities_Type()
)
keyboardDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceStateCapabilities.setStatus("mandatory")
_KeyboardDeviceStateSettings_Type = DellStateSettings
_KeyboardDeviceStateSettings_Object = MibTableColumn
keyboardDeviceStateSettings = _KeyboardDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 4),
    _KeyboardDeviceStateSettings_Type()
)
keyboardDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceStateSettings.setStatus("mandatory")
_KeyboardDeviceStatus_Type = DellStatus
_KeyboardDeviceStatus_Object = MibTableColumn
keyboardDeviceStatus = _KeyboardDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 5),
    _KeyboardDeviceStatus_Type()
)
keyboardDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceStatus.setStatus("mandatory")
_KeyboardPortIndexReference_Type = DellObjectRange
_KeyboardPortIndexReference_Object = MibTableColumn
keyboardPortIndexReference = _KeyboardPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 6),
    _KeyboardPortIndexReference_Type()
)
keyboardPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortIndexReference.setStatus("mandatory")
_KeyboardDeviceTypeName_Type = DellString
_KeyboardDeviceTypeName_Object = MibTableColumn
keyboardDeviceTypeName = _KeyboardDeviceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 7),
    _KeyboardDeviceTypeName_Type()
)
keyboardDeviceTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceTypeName.setStatus("mandatory")
_KeyboardDeviceLayoutName_Type = DellString
_KeyboardDeviceLayoutName_Object = MibTableColumn
keyboardDeviceLayoutName = _KeyboardDeviceLayoutName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 8),
    _KeyboardDeviceLayoutName_Type()
)
keyboardDeviceLayoutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceLayoutName.setStatus("mandatory")
_ProcessorDeviceTable_Object = MibTable
processorDeviceTable = _ProcessorDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30)
)
if mibBuilder.loadTexts:
    processorDeviceTable.setStatus("mandatory")
_ProcessorDeviceTableEntry_Object = MibTableRow
processorDeviceTableEntry = _ProcessorDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1)
)
processorDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "processorDevicechassisIndex"),
    (0, "MIB-Dell-10892", "processorDeviceIndex"),
)
if mibBuilder.loadTexts:
    processorDeviceTableEntry.setStatus("mandatory")
_ProcessorDevicechassisIndex_Type = DellObjectRange
_ProcessorDevicechassisIndex_Object = MibTableColumn
processorDevicechassisIndex = _ProcessorDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 1),
    _ProcessorDevicechassisIndex_Type()
)
processorDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDevicechassisIndex.setStatus("mandatory")
_ProcessorDeviceIndex_Type = DellObjectRange
_ProcessorDeviceIndex_Object = MibTableColumn
processorDeviceIndex = _ProcessorDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 2),
    _ProcessorDeviceIndex_Type()
)
processorDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceIndex.setStatus("mandatory")
_ProcessorDeviceStateCapabilities_Type = DellStateCapabilities
_ProcessorDeviceStateCapabilities_Object = MibTableColumn
processorDeviceStateCapabilities = _ProcessorDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 3),
    _ProcessorDeviceStateCapabilities_Type()
)
processorDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStateCapabilities.setStatus("mandatory")
_ProcessorDeviceStateSettings_Type = DellStateSettings
_ProcessorDeviceStateSettings_Object = MibTableColumn
processorDeviceStateSettings = _ProcessorDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 4),
    _ProcessorDeviceStateSettings_Type()
)
processorDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStateSettings.setStatus("mandatory")
_ProcessorDeviceStatus_Type = DellStatus
_ProcessorDeviceStatus_Object = MibTableColumn
processorDeviceStatus = _ProcessorDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 5),
    _ProcessorDeviceStatus_Type()
)
processorDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatus.setStatus("mandatory")
_ProcessorPortIndexReference_Type = DellObjectRange
_ProcessorPortIndexReference_Object = MibTableColumn
processorPortIndexReference = _ProcessorPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 6),
    _ProcessorPortIndexReference_Type()
)
processorPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortIndexReference.setStatus("mandatory")
_ProcessorDeviceType_Type = DellProcessorDeviceType
_ProcessorDeviceType_Object = MibTableColumn
processorDeviceType = _ProcessorDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 7),
    _ProcessorDeviceType_Type()
)
processorDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceType.setStatus("mandatory")
_ProcessorDeviceManufacturerName_Type = DellString
_ProcessorDeviceManufacturerName_Object = MibTableColumn
processorDeviceManufacturerName = _ProcessorDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 8),
    _ProcessorDeviceManufacturerName_Type()
)
processorDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceManufacturerName.setStatus("mandatory")
_ProcessorDeviceStatusState_Type = DellProcessorDeviceStatusState
_ProcessorDeviceStatusState_Object = MibTableColumn
processorDeviceStatusState = _ProcessorDeviceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 9),
    _ProcessorDeviceStatusState_Type()
)
processorDeviceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusState.setStatus("mandatory")
_ProcessorDeviceFamily_Type = DellProcessorDeviceFamily
_ProcessorDeviceFamily_Object = MibTableColumn
processorDeviceFamily = _ProcessorDeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 10),
    _ProcessorDeviceFamily_Type()
)
processorDeviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceFamily.setStatus("mandatory")
_ProcessorDeviceMaximumSpeed_Type = DellUnsigned32BitRange
_ProcessorDeviceMaximumSpeed_Object = MibTableColumn
processorDeviceMaximumSpeed = _ProcessorDeviceMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 11),
    _ProcessorDeviceMaximumSpeed_Type()
)
processorDeviceMaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceMaximumSpeed.setStatus("mandatory")
_ProcessorDeviceCurrentSpeed_Type = DellUnsigned32BitRange
_ProcessorDeviceCurrentSpeed_Object = MibTableColumn
processorDeviceCurrentSpeed = _ProcessorDeviceCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 12),
    _ProcessorDeviceCurrentSpeed_Type()
)
processorDeviceCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCurrentSpeed.setStatus("mandatory")
_ProcessorDeviceExternalClockSpeed_Type = DellUnsigned32BitRange
_ProcessorDeviceExternalClockSpeed_Object = MibTableColumn
processorDeviceExternalClockSpeed = _ProcessorDeviceExternalClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 13),
    _ProcessorDeviceExternalClockSpeed_Type()
)
processorDeviceExternalClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceExternalClockSpeed.setStatus("mandatory")
_ProcessorDeviceVoltage_Type = DellSigned32BitRange
_ProcessorDeviceVoltage_Object = MibTableColumn
processorDeviceVoltage = _ProcessorDeviceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 14),
    _ProcessorDeviceVoltage_Type()
)
processorDeviceVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceVoltage.setStatus("mandatory")
_ProcessorDeviceUpgradeInformation_Type = DellProcessorUpgradeInformation
_ProcessorDeviceUpgradeInformation_Object = MibTableColumn
processorDeviceUpgradeInformation = _ProcessorDeviceUpgradeInformation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 15),
    _ProcessorDeviceUpgradeInformation_Type()
)
processorDeviceUpgradeInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceUpgradeInformation.setStatus("mandatory")
_ProcessorDeviceVersionName_Type = DellString
_ProcessorDeviceVersionName_Object = MibTableColumn
processorDeviceVersionName = _ProcessorDeviceVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 16),
    _ProcessorDeviceVersionName_Type()
)
processorDeviceVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceVersionName.setStatus("mandatory")
_ProcessorDeviceCoreCount_Type = DellUnsigned32BitRange
_ProcessorDeviceCoreCount_Object = MibTableColumn
processorDeviceCoreCount = _ProcessorDeviceCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 17),
    _ProcessorDeviceCoreCount_Type()
)
processorDeviceCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCoreCount.setStatus("mandatory")
_ProcessorDeviceCoreEnabledCount_Type = DellUnsigned32BitRange
_ProcessorDeviceCoreEnabledCount_Object = MibTableColumn
processorDeviceCoreEnabledCount = _ProcessorDeviceCoreEnabledCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 18),
    _ProcessorDeviceCoreEnabledCount_Type()
)
processorDeviceCoreEnabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCoreEnabledCount.setStatus("mandatory")
_ProcessorDeviceThreadCount_Type = DellUnsigned32BitRange
_ProcessorDeviceThreadCount_Object = MibTableColumn
processorDeviceThreadCount = _ProcessorDeviceThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 19),
    _ProcessorDeviceThreadCount_Type()
)
processorDeviceThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceThreadCount.setStatus("mandatory")
_ProcessorDeviceCharacteristics_Type = DellUnsigned16BitRange
_ProcessorDeviceCharacteristics_Object = MibTableColumn
processorDeviceCharacteristics = _ProcessorDeviceCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 20),
    _ProcessorDeviceCharacteristics_Type()
)
processorDeviceCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCharacteristics.setStatus("mandatory")
_ProcessorDeviceExtendedCapabilities_Type = DellUnsigned16BitRange
_ProcessorDeviceExtendedCapabilities_Object = MibTableColumn
processorDeviceExtendedCapabilities = _ProcessorDeviceExtendedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 21),
    _ProcessorDeviceExtendedCapabilities_Type()
)
processorDeviceExtendedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceExtendedCapabilities.setStatus("mandatory")
_ProcessorDeviceExtendedSettings_Type = DellUnsigned16BitRange
_ProcessorDeviceExtendedSettings_Object = MibTableColumn
processorDeviceExtendedSettings = _ProcessorDeviceExtendedSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 22),
    _ProcessorDeviceExtendedSettings_Type()
)
processorDeviceExtendedSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceExtendedSettings.setStatus("mandatory")
_ProcessorDeviceBrandName_Type = DellString
_ProcessorDeviceBrandName_Object = MibTableColumn
processorDeviceBrandName = _ProcessorDeviceBrandName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 23),
    _ProcessorDeviceBrandName_Type()
)
processorDeviceBrandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceBrandName.setStatus("mandatory")
_ProcessorDeviceModelName_Type = DellString
_ProcessorDeviceModelName_Object = MibTableColumn
processorDeviceModelName = _ProcessorDeviceModelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 24),
    _ProcessorDeviceModelName_Type()
)
processorDeviceModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceModelName.setStatus("mandatory")
_ProcessorDeviceSteppingName_Type = DellString
_ProcessorDeviceSteppingName_Object = MibTableColumn
processorDeviceSteppingName = _ProcessorDeviceSteppingName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 25),
    _ProcessorDeviceSteppingName_Type()
)
processorDeviceSteppingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceSteppingName.setStatus("mandatory")
_ProcessorDeviceDeprecatedCapabilities_Type = DellUnsigned16BitRange
_ProcessorDeviceDeprecatedCapabilities_Object = MibTableColumn
processorDeviceDeprecatedCapabilities = _ProcessorDeviceDeprecatedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 26),
    _ProcessorDeviceDeprecatedCapabilities_Type()
)
processorDeviceDeprecatedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceDeprecatedCapabilities.setStatus("mandatory")
_ProcessorDeviceStatusTable_Object = MibTable
processorDeviceStatusTable = _ProcessorDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32)
)
if mibBuilder.loadTexts:
    processorDeviceStatusTable.setStatus("mandatory")
_ProcessorDeviceStatusTableEntry_Object = MibTableRow
processorDeviceStatusTableEntry = _ProcessorDeviceStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1)
)
processorDeviceStatusTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "processorDeviceStatusChassisIndex"),
    (0, "MIB-Dell-10892", "processorDeviceStatusIndex"),
)
if mibBuilder.loadTexts:
    processorDeviceStatusTableEntry.setStatus("mandatory")
_ProcessorDeviceStatusChassisIndex_Type = DellObjectRange
_ProcessorDeviceStatusChassisIndex_Object = MibTableColumn
processorDeviceStatusChassisIndex = _ProcessorDeviceStatusChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 1),
    _ProcessorDeviceStatusChassisIndex_Type()
)
processorDeviceStatusChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusChassisIndex.setStatus("mandatory")
_ProcessorDeviceStatusIndex_Type = DellObjectRange
_ProcessorDeviceStatusIndex_Object = MibTableColumn
processorDeviceStatusIndex = _ProcessorDeviceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 2),
    _ProcessorDeviceStatusIndex_Type()
)
processorDeviceStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusIndex.setStatus("mandatory")
_ProcessorDeviceStatusStateCapabilities_Type = DellStateCapabilities
_ProcessorDeviceStatusStateCapabilities_Object = MibTableColumn
processorDeviceStatusStateCapabilities = _ProcessorDeviceStatusStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 3),
    _ProcessorDeviceStatusStateCapabilities_Type()
)
processorDeviceStatusStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusStateCapabilities.setStatus("mandatory")
_ProcessorDeviceStatusStateSettings_Type = DellStateSettings
_ProcessorDeviceStatusStateSettings_Object = MibTableColumn
processorDeviceStatusStateSettings = _ProcessorDeviceStatusStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 4),
    _ProcessorDeviceStatusStateSettings_Type()
)
processorDeviceStatusStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusStateSettings.setStatus("mandatory")
_ProcessorDeviceStatusStatus_Type = DellStatus
_ProcessorDeviceStatusStatus_Object = MibTableColumn
processorDeviceStatusStatus = _ProcessorDeviceStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 5),
    _ProcessorDeviceStatusStatus_Type()
)
processorDeviceStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusStatus.setStatus("mandatory")
_ProcessorDeviceStatusReading_Type = DellProcessorDeviceStatusReading
_ProcessorDeviceStatusReading_Object = MibTableColumn
processorDeviceStatusReading = _ProcessorDeviceStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 6),
    _ProcessorDeviceStatusReading_Type()
)
processorDeviceStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusReading.setStatus("mandatory")
_ProcessorDeviceStatusLocationName_Type = DellString
_ProcessorDeviceStatusLocationName_Object = MibTableColumn
processorDeviceStatusLocationName = _ProcessorDeviceStatusLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 7),
    _ProcessorDeviceStatusLocationName_Type()
)
processorDeviceStatusLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusLocationName.setStatus("mandatory")
_ProcessorDeviceStatusPortIndexReference_Type = DellObjectRange
_ProcessorDeviceStatusPortIndexReference_Object = MibTableColumn
processorDeviceStatusPortIndexReference = _ProcessorDeviceStatusPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 32, 1, 8),
    _ProcessorDeviceStatusPortIndexReference_Type()
)
processorDeviceStatusPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusPortIndexReference.setStatus("mandatory")
_CacheDeviceTable_Object = MibTable
cacheDeviceTable = _CacheDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40)
)
if mibBuilder.loadTexts:
    cacheDeviceTable.setStatus("mandatory")
_CacheDeviceTableEntry_Object = MibTableRow
cacheDeviceTableEntry = _CacheDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1)
)
cacheDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cacheDevicechassisIndex"),
    (0, "MIB-Dell-10892", "cacheDeviceIndex"),
)
if mibBuilder.loadTexts:
    cacheDeviceTableEntry.setStatus("mandatory")
_CacheDevicechassisIndex_Type = DellObjectRange
_CacheDevicechassisIndex_Object = MibTableColumn
cacheDevicechassisIndex = _CacheDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 1),
    _CacheDevicechassisIndex_Type()
)
cacheDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDevicechassisIndex.setStatus("mandatory")
_CacheDeviceIndex_Type = DellObjectRange
_CacheDeviceIndex_Object = MibTableColumn
cacheDeviceIndex = _CacheDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 2),
    _CacheDeviceIndex_Type()
)
cacheDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceIndex.setStatus("mandatory")
_CacheDeviceStateCapabilities_Type = DellStateCapabilities
_CacheDeviceStateCapabilities_Object = MibTableColumn
cacheDeviceStateCapabilities = _CacheDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 3),
    _CacheDeviceStateCapabilities_Type()
)
cacheDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceStateCapabilities.setStatus("mandatory")
_CacheDeviceStateSettings_Type = DellStateSettings
_CacheDeviceStateSettings_Object = MibTableColumn
cacheDeviceStateSettings = _CacheDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 4),
    _CacheDeviceStateSettings_Type()
)
cacheDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceStateSettings.setStatus("mandatory")
_CacheDeviceStatus_Type = DellStatus
_CacheDeviceStatus_Object = MibTableColumn
cacheDeviceStatus = _CacheDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 5),
    _CacheDeviceStatus_Type()
)
cacheDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceStatus.setStatus("mandatory")
_CacheDeviceprocessorDeviceIndexReference_Type = DellObjectRange
_CacheDeviceprocessorDeviceIndexReference_Object = MibTableColumn
cacheDeviceprocessorDeviceIndexReference = _CacheDeviceprocessorDeviceIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 6),
    _CacheDeviceprocessorDeviceIndexReference_Type()
)
cacheDeviceprocessorDeviceIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceprocessorDeviceIndexReference.setStatus("mandatory")
_CacheDeviceType_Type = DellCacheDeviceType
_CacheDeviceType_Object = MibTableColumn
cacheDeviceType = _CacheDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 7),
    _CacheDeviceType_Type()
)
cacheDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceType.setStatus("mandatory")
_CacheDeviceLocation_Type = DellCacheDeviceLocation
_CacheDeviceLocation_Object = MibTableColumn
cacheDeviceLocation = _CacheDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 8),
    _CacheDeviceLocation_Type()
)
cacheDeviceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceLocation.setStatus("mandatory")
_CacheDeviceStatusState_Type = DellCacheDeviceStatusState
_CacheDeviceStatusState_Object = MibTableColumn
cacheDeviceStatusState = _CacheDeviceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 9),
    _CacheDeviceStatusState_Type()
)
cacheDeviceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceStatusState.setStatus("mandatory")
_CacheDeviceExternalSocketName_Type = DellString
_CacheDeviceExternalSocketName_Object = MibTableColumn
cacheDeviceExternalSocketName = _CacheDeviceExternalSocketName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 10),
    _CacheDeviceExternalSocketName_Type()
)
cacheDeviceExternalSocketName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceExternalSocketName.setStatus("mandatory")
_CacheDeviceLevel_Type = DellCacheDeviceLevel
_CacheDeviceLevel_Object = MibTableColumn
cacheDeviceLevel = _CacheDeviceLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 11),
    _CacheDeviceLevel_Type()
)
cacheDeviceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceLevel.setStatus("mandatory")
_CacheDeviceMaximumSize_Type = DellUnsigned32BitRange
_CacheDeviceMaximumSize_Object = MibTableColumn
cacheDeviceMaximumSize = _CacheDeviceMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 12),
    _CacheDeviceMaximumSize_Type()
)
cacheDeviceMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceMaximumSize.setStatus("mandatory")
_CacheDeviceCurrentSize_Type = DellUnsigned32BitRange
_CacheDeviceCurrentSize_Object = MibTableColumn
cacheDeviceCurrentSize = _CacheDeviceCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 13),
    _CacheDeviceCurrentSize_Type()
)
cacheDeviceCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceCurrentSize.setStatus("mandatory")
_CacheDeviceSpeed_Type = DellUnsigned32BitRange
_CacheDeviceSpeed_Object = MibTableColumn
cacheDeviceSpeed = _CacheDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 14),
    _CacheDeviceSpeed_Type()
)
cacheDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceSpeed.setStatus("mandatory")
_CacheDeviceWritePolicy_Type = DellCacheDeviceWritePolicy
_CacheDeviceWritePolicy_Object = MibTableColumn
cacheDeviceWritePolicy = _CacheDeviceWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 15),
    _CacheDeviceWritePolicy_Type()
)
cacheDeviceWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceWritePolicy.setStatus("mandatory")
_CacheDeviceIsSocketed_Type = DellBoolean
_CacheDeviceIsSocketed_Object = MibTableColumn
cacheDeviceIsSocketed = _CacheDeviceIsSocketed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 16),
    _CacheDeviceIsSocketed_Type()
)
cacheDeviceIsSocketed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceIsSocketed.setStatus("mandatory")
_CacheDeviceECCType_Type = DellCacheDeviceECCType
_CacheDeviceECCType_Object = MibTableColumn
cacheDeviceECCType = _CacheDeviceECCType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 17),
    _CacheDeviceECCType_Type()
)
cacheDeviceECCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceECCType.setStatus("mandatory")
_CacheDeviceAssociativity_Type = DellCacheDeviceAssociativity
_CacheDeviceAssociativity_Object = MibTableColumn
cacheDeviceAssociativity = _CacheDeviceAssociativity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 18),
    _CacheDeviceAssociativity_Type()
)
cacheDeviceAssociativity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceAssociativity.setStatus("mandatory")
_CacheDeviceSupportedType_Type = DellCacheDeviceSRAMType
_CacheDeviceSupportedType_Object = MibTableColumn
cacheDeviceSupportedType = _CacheDeviceSupportedType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 19),
    _CacheDeviceSupportedType_Type()
)
cacheDeviceSupportedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceSupportedType.setStatus("mandatory")
_CacheDeviceCurrentType_Type = DellCacheDeviceSRAMType
_CacheDeviceCurrentType_Object = MibTableColumn
cacheDeviceCurrentType = _CacheDeviceCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 20),
    _CacheDeviceCurrentType_Type()
)
cacheDeviceCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceCurrentType.setStatus("mandatory")
_MemoryDeviceTable_Object = MibTable
memoryDeviceTable = _MemoryDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50)
)
if mibBuilder.loadTexts:
    memoryDeviceTable.setStatus("mandatory")
_MemoryDeviceTableEntry_Object = MibTableRow
memoryDeviceTableEntry = _MemoryDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1)
)
memoryDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "memoryDevicechassisIndex"),
    (0, "MIB-Dell-10892", "memoryDeviceIndex"),
)
if mibBuilder.loadTexts:
    memoryDeviceTableEntry.setStatus("mandatory")
_MemoryDevicechassisIndex_Type = DellObjectRange
_MemoryDevicechassisIndex_Object = MibTableColumn
memoryDevicechassisIndex = _MemoryDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 1),
    _MemoryDevicechassisIndex_Type()
)
memoryDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicechassisIndex.setStatus("mandatory")
_MemoryDeviceIndex_Type = DellObjectRange
_MemoryDeviceIndex_Object = MibTableColumn
memoryDeviceIndex = _MemoryDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 2),
    _MemoryDeviceIndex_Type()
)
memoryDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceIndex.setStatus("mandatory")
_MemoryDeviceStateCapabilities_Type = DellStateCapabilities
_MemoryDeviceStateCapabilities_Object = MibTableColumn
memoryDeviceStateCapabilities = _MemoryDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 3),
    _MemoryDeviceStateCapabilities_Type()
)
memoryDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStateCapabilities.setStatus("mandatory")
_MemoryDeviceStateSettings_Type = DellStateSettings
_MemoryDeviceStateSettings_Object = MibTableColumn
memoryDeviceStateSettings = _MemoryDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 4),
    _MemoryDeviceStateSettings_Type()
)
memoryDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStateSettings.setStatus("mandatory")
_MemoryDeviceStatus_Type = DellStatus
_MemoryDeviceStatus_Object = MibTableColumn
memoryDeviceStatus = _MemoryDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 5),
    _MemoryDeviceStatus_Type()
)
memoryDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStatus.setStatus("mandatory")
_MemoryDeviceMemoryPortIndexReference_Type = DellObjectRange
_MemoryDeviceMemoryPortIndexReference_Object = MibTableColumn
memoryDeviceMemoryPortIndexReference = _MemoryDeviceMemoryPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 6),
    _MemoryDeviceMemoryPortIndexReference_Type()
)
memoryDeviceMemoryPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMemoryPortIndexReference.setStatus("mandatory")
_MemoryDeviceType_Type = DellMemoryDeviceType
_MemoryDeviceType_Object = MibTableColumn
memoryDeviceType = _MemoryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 7),
    _MemoryDeviceType_Type()
)
memoryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceType.setStatus("mandatory")
_MemoryDeviceLocationName_Type = DellString
_MemoryDeviceLocationName_Object = MibTableColumn
memoryDeviceLocationName = _MemoryDeviceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 8),
    _MemoryDeviceLocationName_Type()
)
memoryDeviceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceLocationName.setStatus("mandatory")
_MemoryDeviceErrorCount_Type = DellSigned32BitRange
_MemoryDeviceErrorCount_Object = MibTableColumn
memoryDeviceErrorCount = _MemoryDeviceErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 9),
    _MemoryDeviceErrorCount_Type()
)
memoryDeviceErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceErrorCount.setStatus("deprecated")
_MemoryDeviceBankLocationName_Type = DellString
_MemoryDeviceBankLocationName_Object = MibTableColumn
memoryDeviceBankLocationName = _MemoryDeviceBankLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 10),
    _MemoryDeviceBankLocationName_Type()
)
memoryDeviceBankLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceBankLocationName.setStatus("mandatory")
_MemoryDeviceTypeDetails_Type = DellMemoryDeviceTypeDetails
_MemoryDeviceTypeDetails_Object = MibTableColumn
memoryDeviceTypeDetails = _MemoryDeviceTypeDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 11),
    _MemoryDeviceTypeDetails_Type()
)
memoryDeviceTypeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceTypeDetails.setStatus("mandatory")
_MemoryDeviceFormFactor_Type = DellMemoryDeviceFormFactor
_MemoryDeviceFormFactor_Object = MibTableColumn
memoryDeviceFormFactor = _MemoryDeviceFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 12),
    _MemoryDeviceFormFactor_Type()
)
memoryDeviceFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceFormFactor.setStatus("mandatory")
_MemoryDeviceSet_Type = DellUnsigned32BitRange
_MemoryDeviceSet_Object = MibTableColumn
memoryDeviceSet = _MemoryDeviceSet_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 13),
    _MemoryDeviceSet_Type()
)
memoryDeviceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSet.setStatus("mandatory")
_MemoryDeviceSize_Type = DellUnsigned32BitRange
_MemoryDeviceSize_Object = MibTableColumn
memoryDeviceSize = _MemoryDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 14),
    _MemoryDeviceSize_Type()
)
memoryDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSize.setStatus("deprecated")
_MemoryDeviceSpeed_Type = DellUnsigned32BitRange
_MemoryDeviceSpeed_Object = MibTableColumn
memoryDeviceSpeed = _MemoryDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 15),
    _MemoryDeviceSpeed_Type()
)
memoryDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSpeed.setStatus("mandatory")
_MemoryDeviceTotalBusWidth_Type = DellUnsigned32BitRange
_MemoryDeviceTotalBusWidth_Object = MibTableColumn
memoryDeviceTotalBusWidth = _MemoryDeviceTotalBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 16),
    _MemoryDeviceTotalBusWidth_Type()
)
memoryDeviceTotalBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceTotalBusWidth.setStatus("mandatory")
_MemoryDeviceTotalDataBusWidth_Type = DellUnsigned32BitRange
_MemoryDeviceTotalDataBusWidth_Object = MibTableColumn
memoryDeviceTotalDataBusWidth = _MemoryDeviceTotalDataBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 17),
    _MemoryDeviceTotalDataBusWidth_Type()
)
memoryDeviceTotalDataBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceTotalDataBusWidth.setStatus("mandatory")
_MemoryDeviceSingleBitErrorCount_Type = DellSigned32BitRange
_MemoryDeviceSingleBitErrorCount_Object = MibTableColumn
memoryDeviceSingleBitErrorCount = _MemoryDeviceSingleBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 18),
    _MemoryDeviceSingleBitErrorCount_Type()
)
memoryDeviceSingleBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSingleBitErrorCount.setStatus("deprecated")
_MemoryDeviceMultiBitErrorCount_Type = DellSigned32BitRange
_MemoryDeviceMultiBitErrorCount_Object = MibTableColumn
memoryDeviceMultiBitErrorCount = _MemoryDeviceMultiBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 19),
    _MemoryDeviceMultiBitErrorCount_Type()
)
memoryDeviceMultiBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMultiBitErrorCount.setStatus("deprecated")
_MemoryDeviceFailureModes_Type = DellMemoryDeviceFailureModes
_MemoryDeviceFailureModes_Object = MibTableColumn
memoryDeviceFailureModes = _MemoryDeviceFailureModes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 20),
    _MemoryDeviceFailureModes_Type()
)
memoryDeviceFailureModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceFailureModes.setStatus("mandatory")
_MemoryDeviceManufacturerName_Type = DellString
_MemoryDeviceManufacturerName_Object = MibTableColumn
memoryDeviceManufacturerName = _MemoryDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 21),
    _MemoryDeviceManufacturerName_Type()
)
memoryDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceManufacturerName.setStatus("mandatory")
_MemoryDevicePartNumberName_Type = DellString
_MemoryDevicePartNumberName_Object = MibTableColumn
memoryDevicePartNumberName = _MemoryDevicePartNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 22),
    _MemoryDevicePartNumberName_Type()
)
memoryDevicePartNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePartNumberName.setStatus("mandatory")
_MemoryDeviceSerialNumberName_Type = DellString
_MemoryDeviceSerialNumberName_Object = MibTableColumn
memoryDeviceSerialNumberName = _MemoryDeviceSerialNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 23),
    _MemoryDeviceSerialNumberName_Type()
)
memoryDeviceSerialNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSerialNumberName.setStatus("mandatory")
_MemoryDeviceAssetTagName_Type = DellString
_MemoryDeviceAssetTagName_Object = MibTableColumn
memoryDeviceAssetTagName = _MemoryDeviceAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 24),
    _MemoryDeviceAssetTagName_Type()
)
memoryDeviceAssetTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceAssetTagName.setStatus("mandatory")
_MemoryDeviceSpeedName_Type = DellString
_MemoryDeviceSpeedName_Object = MibTableColumn
memoryDeviceSpeedName = _MemoryDeviceSpeedName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 25),
    _MemoryDeviceSpeedName_Type()
)
memoryDeviceSpeedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSpeedName.setStatus("mandatory")
_MemoryDeviceRank_Type = DellMemoryDeviceRank
_MemoryDeviceRank_Object = MibTableColumn
memoryDeviceRank = _MemoryDeviceRank_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 26),
    _MemoryDeviceRank_Type()
)
memoryDeviceRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceRank.setStatus("mandatory")
_MemoryDeviceExtendedSize_Type = DellUnsigned32BitRange
_MemoryDeviceExtendedSize_Object = MibTableColumn
memoryDeviceExtendedSize = _MemoryDeviceExtendedSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 27),
    _MemoryDeviceExtendedSize_Type()
)
memoryDeviceExtendedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceExtendedSize.setStatus("mandatory")
_MemoryDeviceMemoryTechnology_Type = DellMemoryDeviceMemoryTechnology
_MemoryDeviceMemoryTechnology_Object = MibTableColumn
memoryDeviceMemoryTechnology = _MemoryDeviceMemoryTechnology_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 28),
    _MemoryDeviceMemoryTechnology_Type()
)
memoryDeviceMemoryTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMemoryTechnology.setStatus("mandatory")
_MemoryDeviceNonVolatileSize_Type = DellUnsigned32BitRange
_MemoryDeviceNonVolatileSize_Object = MibTableColumn
memoryDeviceNonVolatileSize = _MemoryDeviceNonVolatileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 29),
    _MemoryDeviceNonVolatileSize_Type()
)
memoryDeviceNonVolatileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceNonVolatileSize.setStatus("mandatory")
_MemoryDeviceVolatileSize_Type = DellUnsigned32BitRange
_MemoryDeviceVolatileSize_Object = MibTableColumn
memoryDeviceVolatileSize = _MemoryDeviceVolatileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 30),
    _MemoryDeviceVolatileSize_Type()
)
memoryDeviceVolatileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceVolatileSize.setStatus("mandatory")
_MemoryDeviceCacheSize_Type = DellUnsigned32BitRange
_MemoryDeviceCacheSize_Object = MibTableColumn
memoryDeviceCacheSize = _MemoryDeviceCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 31),
    _MemoryDeviceCacheSize_Type()
)
memoryDeviceCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceCacheSize.setStatus("mandatory")
_MemoryDeviceWearLevel_Type = DellUnsigned32BitRange
_MemoryDeviceWearLevel_Object = MibTableColumn
memoryDeviceWearLevel = _MemoryDeviceWearLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 32),
    _MemoryDeviceWearLevel_Type()
)
memoryDeviceWearLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceWearLevel.setStatus("mandatory")
_MemoryDeviceMappedAddressTable_Object = MibTable
memoryDeviceMappedAddressTable = _MemoryDeviceMappedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60)
)
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressTable.setStatus("mandatory")
_MemoryDeviceMappedAddressTableEntry_Object = MibTableRow
memoryDeviceMappedAddressTableEntry = _MemoryDeviceMappedAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1)
)
memoryDeviceMappedAddressTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "memoryDeviceMappedAddresschassisIndex"),
    (0, "MIB-Dell-10892", "memoryDeviceMappedAddressIndex"),
)
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressTableEntry.setStatus("mandatory")
_MemoryDeviceMappedAddresschassisIndex_Type = DellObjectRange
_MemoryDeviceMappedAddresschassisIndex_Object = MibTableColumn
memoryDeviceMappedAddresschassisIndex = _MemoryDeviceMappedAddresschassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 1),
    _MemoryDeviceMappedAddresschassisIndex_Type()
)
memoryDeviceMappedAddresschassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddresschassisIndex.setStatus("mandatory")
_MemoryDeviceMappedAddressIndex_Type = DellObjectRange
_MemoryDeviceMappedAddressIndex_Object = MibTableColumn
memoryDeviceMappedAddressIndex = _MemoryDeviceMappedAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 2),
    _MemoryDeviceMappedAddressIndex_Type()
)
memoryDeviceMappedAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressIndex.setStatus("mandatory")
_MemoryDeviceMappedAddressStateCapabilities_Type = DellStateCapabilities
_MemoryDeviceMappedAddressStateCapabilities_Object = MibTableColumn
memoryDeviceMappedAddressStateCapabilities = _MemoryDeviceMappedAddressStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 3),
    _MemoryDeviceMappedAddressStateCapabilities_Type()
)
memoryDeviceMappedAddressStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStateCapabilities.setStatus("mandatory")
_MemoryDeviceMappedAddressStateSettings_Type = DellStateSettings
_MemoryDeviceMappedAddressStateSettings_Object = MibTableColumn
memoryDeviceMappedAddressStateSettings = _MemoryDeviceMappedAddressStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 4),
    _MemoryDeviceMappedAddressStateSettings_Type()
)
memoryDeviceMappedAddressStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStateSettings.setStatus("mandatory")
_MemoryDeviceMappedAddressStatus_Type = DellStatus
_MemoryDeviceMappedAddressStatus_Object = MibTableColumn
memoryDeviceMappedAddressStatus = _MemoryDeviceMappedAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 5),
    _MemoryDeviceMappedAddressStatus_Type()
)
memoryDeviceMappedAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStatus.setStatus("mandatory")
_MemoryDeviceIndexReference_Type = DellObjectRange
_MemoryDeviceIndexReference_Object = MibTableColumn
memoryDeviceIndexReference = _MemoryDeviceIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 6),
    _MemoryDeviceIndexReference_Type()
)
memoryDeviceIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceIndexReference.setStatus("mandatory")
_MemoryDeviceMappedAddressRowPosition_Type = DellUnsigned32BitRange
_MemoryDeviceMappedAddressRowPosition_Object = MibTableColumn
memoryDeviceMappedAddressRowPosition = _MemoryDeviceMappedAddressRowPosition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 7),
    _MemoryDeviceMappedAddressRowPosition_Type()
)
memoryDeviceMappedAddressRowPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressRowPosition.setStatus("mandatory")
_MemoryDeviceMappedAddressInterleavePosition_Type = DellUnsigned32BitRange
_MemoryDeviceMappedAddressInterleavePosition_Object = MibTableColumn
memoryDeviceMappedAddressInterleavePosition = _MemoryDeviceMappedAddressInterleavePosition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 8),
    _MemoryDeviceMappedAddressInterleavePosition_Type()
)
memoryDeviceMappedAddressInterleavePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressInterleavePosition.setStatus("mandatory")
_MemoryDeviceMappedAddressInterleaveDepth_Type = DellUnsigned32BitRange
_MemoryDeviceMappedAddressInterleaveDepth_Object = MibTableColumn
memoryDeviceMappedAddressInterleaveDepth = _MemoryDeviceMappedAddressInterleaveDepth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 9),
    _MemoryDeviceMappedAddressInterleaveDepth_Type()
)
memoryDeviceMappedAddressInterleaveDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressInterleaveDepth.setStatus("mandatory")
_MemoryDeviceMappedAddressStartingAddress_Type = DellUnsigned64BitRange
_MemoryDeviceMappedAddressStartingAddress_Object = MibTableColumn
memoryDeviceMappedAddressStartingAddress = _MemoryDeviceMappedAddressStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 10),
    _MemoryDeviceMappedAddressStartingAddress_Type()
)
memoryDeviceMappedAddressStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStartingAddress.setStatus("mandatory")
_MemoryDeviceMappedAddressEndingAddress_Type = DellUnsigned64BitRange
_MemoryDeviceMappedAddressEndingAddress_Object = MibTableColumn
memoryDeviceMappedAddressEndingAddress = _MemoryDeviceMappedAddressEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 11),
    _MemoryDeviceMappedAddressEndingAddress_Type()
)
memoryDeviceMappedAddressEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressEndingAddress.setStatus("mandatory")
_GenericDeviceTable_Object = MibTable
genericDeviceTable = _GenericDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70)
)
if mibBuilder.loadTexts:
    genericDeviceTable.setStatus("mandatory")
_GenericDeviceTableEntry_Object = MibTableRow
genericDeviceTableEntry = _GenericDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1)
)
genericDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "genericDevicechassisIndex"),
    (0, "MIB-Dell-10892", "genericDeviceIndex"),
)
if mibBuilder.loadTexts:
    genericDeviceTableEntry.setStatus("mandatory")
_GenericDevicechassisIndex_Type = DellObjectRange
_GenericDevicechassisIndex_Object = MibTableColumn
genericDevicechassisIndex = _GenericDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 1),
    _GenericDevicechassisIndex_Type()
)
genericDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDevicechassisIndex.setStatus("mandatory")
_GenericDeviceIndex_Type = DellObjectRange
_GenericDeviceIndex_Object = MibTableColumn
genericDeviceIndex = _GenericDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 2),
    _GenericDeviceIndex_Type()
)
genericDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceIndex.setStatus("mandatory")
_GenericDeviceStateCapabilities_Type = DellStateCapabilities
_GenericDeviceStateCapabilities_Object = MibTableColumn
genericDeviceStateCapabilities = _GenericDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 3),
    _GenericDeviceStateCapabilities_Type()
)
genericDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceStateCapabilities.setStatus("mandatory")
_GenericDeviceStateSettings_Type = DellStateSettings
_GenericDeviceStateSettings_Object = MibTableColumn
genericDeviceStateSettings = _GenericDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 4),
    _GenericDeviceStateSettings_Type()
)
genericDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceStateSettings.setStatus("mandatory")
_GenericDeviceStatus_Type = DellStatus
_GenericDeviceStatus_Object = MibTableColumn
genericDeviceStatus = _GenericDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 5),
    _GenericDeviceStatus_Type()
)
genericDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceStatus.setStatus("mandatory")
_GenericDeviceSystemSlotIndexReference_Type = DellObjectRange
_GenericDeviceSystemSlotIndexReference_Object = MibTableColumn
genericDeviceSystemSlotIndexReference = _GenericDeviceSystemSlotIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 6),
    _GenericDeviceSystemSlotIndexReference_Type()
)
genericDeviceSystemSlotIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceSystemSlotIndexReference.setStatus("mandatory")
_GenericDeviceType_Type = DellGenericDeviceType
_GenericDeviceType_Object = MibTableColumn
genericDeviceType = _GenericDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 7),
    _GenericDeviceType_Type()
)
genericDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceType.setStatus("mandatory")
_GenericDeviceName_Type = DellString
_GenericDeviceName_Object = MibTableColumn
genericDeviceName = _GenericDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 8),
    _GenericDeviceName_Type()
)
genericDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceName.setStatus("mandatory")
_PCIDeviceTable_Object = MibTable
pCIDeviceTable = _PCIDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80)
)
if mibBuilder.loadTexts:
    pCIDeviceTable.setStatus("mandatory")
_PCIDeviceTableEntry_Object = MibTableRow
pCIDeviceTableEntry = _PCIDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1)
)
pCIDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pCIDevicechassisIndex"),
    (0, "MIB-Dell-10892", "pCIDeviceIndex"),
)
if mibBuilder.loadTexts:
    pCIDeviceTableEntry.setStatus("mandatory")
_PCIDevicechassisIndex_Type = DellObjectRange
_PCIDevicechassisIndex_Object = MibTableColumn
pCIDevicechassisIndex = _PCIDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 1),
    _PCIDevicechassisIndex_Type()
)
pCIDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDevicechassisIndex.setStatus("mandatory")
_PCIDeviceIndex_Type = DellObjectRange
_PCIDeviceIndex_Object = MibTableColumn
pCIDeviceIndex = _PCIDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 2),
    _PCIDeviceIndex_Type()
)
pCIDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceIndex.setStatus("mandatory")
_PCIDeviceStateCapabilities_Type = DellStateCapabilities
_PCIDeviceStateCapabilities_Object = MibTableColumn
pCIDeviceStateCapabilities = _PCIDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 3),
    _PCIDeviceStateCapabilities_Type()
)
pCIDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStateCapabilities.setStatus("mandatory")
_PCIDeviceStateSettings_Type = DellStateSettings
_PCIDeviceStateSettings_Object = MibTableColumn
pCIDeviceStateSettings = _PCIDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 4),
    _PCIDeviceStateSettings_Type()
)
pCIDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStateSettings.setStatus("mandatory")
_PCIDeviceStatus_Type = DellStatus
_PCIDeviceStatus_Object = MibTableColumn
pCIDeviceStatus = _PCIDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 5),
    _PCIDeviceStatus_Type()
)
pCIDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStatus.setStatus("mandatory")
_PCIDeviceSystemSlotIndexReference_Type = DellObjectRange
_PCIDeviceSystemSlotIndexReference_Object = MibTableColumn
pCIDeviceSystemSlotIndexReference = _PCIDeviceSystemSlotIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 6),
    _PCIDeviceSystemSlotIndexReference_Type()
)
pCIDeviceSystemSlotIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceSystemSlotIndexReference.setStatus("mandatory")
_PCIDeviceDataBusWidth_Type = DellUnsigned32BitRange
_PCIDeviceDataBusWidth_Object = MibTableColumn
pCIDeviceDataBusWidth = _PCIDeviceDataBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 7),
    _PCIDeviceDataBusWidth_Type()
)
pCIDeviceDataBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceDataBusWidth.setStatus("mandatory")
_PCIDeviceManufacturerName_Type = DellString
_PCIDeviceManufacturerName_Object = MibTableColumn
pCIDeviceManufacturerName = _PCIDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 8),
    _PCIDeviceManufacturerName_Type()
)
pCIDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceManufacturerName.setStatus("mandatory")
_PCIDeviceDescriptionName_Type = DellString
_PCIDeviceDescriptionName_Object = MibTableColumn
pCIDeviceDescriptionName = _PCIDeviceDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 9),
    _PCIDeviceDescriptionName_Type()
)
pCIDeviceDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceDescriptionName.setStatus("mandatory")
_PCIDeviceSpeed_Type = DellUnsigned32BitRange
_PCIDeviceSpeed_Object = MibTableColumn
pCIDeviceSpeed = _PCIDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 10),
    _PCIDeviceSpeed_Type()
)
pCIDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceSpeed.setStatus("mandatory")
_PCIDeviceAdapterFault_Type = DellBoolean
_PCIDeviceAdapterFault_Object = MibTableColumn
pCIDeviceAdapterFault = _PCIDeviceAdapterFault_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 11),
    _PCIDeviceAdapterFault_Type()
)
pCIDeviceAdapterFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceAdapterFault.setStatus("mandatory")
_PCIDeviceConfigurationSpaceTable_Object = MibTable
pCIDeviceConfigurationSpaceTable = _PCIDeviceConfigurationSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82)
)
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceTable.setStatus("mandatory")
_PCIDeviceConfigurationSpaceTableEntry_Object = MibTableRow
pCIDeviceConfigurationSpaceTableEntry = _PCIDeviceConfigurationSpaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1)
)
pCIDeviceConfigurationSpaceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pCIDeviceConfigurationSpacechassisIndex"),
    (0, "MIB-Dell-10892", "pCIDeviceConfigurationSpaceIndex"),
)
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceTableEntry.setStatus("mandatory")
_PCIDeviceConfigurationSpacechassisIndex_Type = DellObjectRange
_PCIDeviceConfigurationSpacechassisIndex_Object = MibTableColumn
pCIDeviceConfigurationSpacechassisIndex = _PCIDeviceConfigurationSpacechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 1),
    _PCIDeviceConfigurationSpacechassisIndex_Type()
)
pCIDeviceConfigurationSpacechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpacechassisIndex.setStatus("mandatory")
_PCIDeviceConfigurationSpaceIndex_Type = DellObjectRange
_PCIDeviceConfigurationSpaceIndex_Object = MibTableColumn
pCIDeviceConfigurationSpaceIndex = _PCIDeviceConfigurationSpaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 2),
    _PCIDeviceConfigurationSpaceIndex_Type()
)
pCIDeviceConfigurationSpaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceIndex.setStatus("mandatory")
_PCIDeviceConfigurationSpaceStateCapabilities_Type = DellStateCapabilities
_PCIDeviceConfigurationSpaceStateCapabilities_Object = MibTableColumn
pCIDeviceConfigurationSpaceStateCapabilities = _PCIDeviceConfigurationSpaceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 3),
    _PCIDeviceConfigurationSpaceStateCapabilities_Type()
)
pCIDeviceConfigurationSpaceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStateCapabilities.setStatus("mandatory")
_PCIDeviceConfigurationSpaceStateSettings_Type = DellStateSettings
_PCIDeviceConfigurationSpaceStateSettings_Object = MibTableColumn
pCIDeviceConfigurationSpaceStateSettings = _PCIDeviceConfigurationSpaceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 4),
    _PCIDeviceConfigurationSpaceStateSettings_Type()
)
pCIDeviceConfigurationSpaceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStateSettings.setStatus("mandatory")
_PCIDeviceConfigurationSpaceStatus_Type = DellStatus
_PCIDeviceConfigurationSpaceStatus_Object = MibTableColumn
pCIDeviceConfigurationSpaceStatus = _PCIDeviceConfigurationSpaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 5),
    _PCIDeviceConfigurationSpaceStatus_Type()
)
pCIDeviceConfigurationSpaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStatus.setStatus("mandatory")
_PCIDeviceIndexReference_Type = DellObjectRange
_PCIDeviceIndexReference_Object = MibTableColumn
pCIDeviceIndexReference = _PCIDeviceIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 6),
    _PCIDeviceIndexReference_Type()
)
pCIDeviceIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceIndexReference.setStatus("mandatory")
_PCIDeviceConfigurationSpaceBusNumber_Type = DellUnsigned32BitRange
_PCIDeviceConfigurationSpaceBusNumber_Object = MibTableColumn
pCIDeviceConfigurationSpaceBusNumber = _PCIDeviceConfigurationSpaceBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 7),
    _PCIDeviceConfigurationSpaceBusNumber_Type()
)
pCIDeviceConfigurationSpaceBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceBusNumber.setStatus("mandatory")
_PCIDeviceConfigurationSpaceDeviceNumber_Type = DellUnsigned32BitRange
_PCIDeviceConfigurationSpaceDeviceNumber_Object = MibTableColumn
pCIDeviceConfigurationSpaceDeviceNumber = _PCIDeviceConfigurationSpaceDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 8),
    _PCIDeviceConfigurationSpaceDeviceNumber_Type()
)
pCIDeviceConfigurationSpaceDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceDeviceNumber.setStatus("mandatory")
_PCIDeviceConfigurationSpaceFunctionNumber_Type = DellUnsigned32BitRange
_PCIDeviceConfigurationSpaceFunctionNumber_Object = MibTableColumn
pCIDeviceConfigurationSpaceFunctionNumber = _PCIDeviceConfigurationSpaceFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 9),
    _PCIDeviceConfigurationSpaceFunctionNumber_Type()
)
pCIDeviceConfigurationSpaceFunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceFunctionNumber.setStatus("mandatory")


class _PCIDeviceConfigurationSpaceHeader_Type(OctetString):
    """Custom type pCIDeviceConfigurationSpaceHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1025),
    )


_PCIDeviceConfigurationSpaceHeader_Type.__name__ = "OctetString"
_PCIDeviceConfigurationSpaceHeader_Object = MibTableColumn
pCIDeviceConfigurationSpaceHeader = _PCIDeviceConfigurationSpaceHeader_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 10),
    _PCIDeviceConfigurationSpaceHeader_Type()
)
pCIDeviceConfigurationSpaceHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceHeader.setStatus("mandatory")
_NetworkDeviceTable_Object = MibTable
networkDeviceTable = _NetworkDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90)
)
if mibBuilder.loadTexts:
    networkDeviceTable.setStatus("mandatory")
_NetworkDeviceTableEntry_Object = MibTableRow
networkDeviceTableEntry = _NetworkDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1)
)
networkDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "networkDeviceChassisIndex"),
    (0, "MIB-Dell-10892", "networkDeviceIndex"),
)
if mibBuilder.loadTexts:
    networkDeviceTableEntry.setStatus("mandatory")
_NetworkDeviceChassisIndex_Type = DellObjectRange
_NetworkDeviceChassisIndex_Object = MibTableColumn
networkDeviceChassisIndex = _NetworkDeviceChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 1),
    _NetworkDeviceChassisIndex_Type()
)
networkDeviceChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceChassisIndex.setStatus("mandatory")
_NetworkDeviceIndex_Type = DellObjectRange
_NetworkDeviceIndex_Object = MibTableColumn
networkDeviceIndex = _NetworkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 2),
    _NetworkDeviceIndex_Type()
)
networkDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceIndex.setStatus("mandatory")
_NetworkDeviceStatus_Type = DellStatus
_NetworkDeviceStatus_Object = MibTableColumn
networkDeviceStatus = _NetworkDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 3),
    _NetworkDeviceStatus_Type()
)
networkDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceStatus.setStatus("mandatory")
_NetworkDeviceConnectionStatus_Type = DellNetworkDeviceConnectionStatus
_NetworkDeviceConnectionStatus_Object = MibTableColumn
networkDeviceConnectionStatus = _NetworkDeviceConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 4),
    _NetworkDeviceConnectionStatus_Type()
)
networkDeviceConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceConnectionStatus.setStatus("mandatory")
_NetworkDeviceDescriptionName_Type = DellString
_NetworkDeviceDescriptionName_Object = MibTableColumn
networkDeviceDescriptionName = _NetworkDeviceDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 5),
    _NetworkDeviceDescriptionName_Type()
)
networkDeviceDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceDescriptionName.setStatus("mandatory")
_NetworkDeviceProductName_Type = DellString
_NetworkDeviceProductName_Object = MibTableColumn
networkDeviceProductName = _NetworkDeviceProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 6),
    _NetworkDeviceProductName_Type()
)
networkDeviceProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceProductName.setStatus("mandatory")
_NetworkDeviceVendorName_Type = DellString
_NetworkDeviceVendorName_Object = MibTableColumn
networkDeviceVendorName = _NetworkDeviceVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 7),
    _NetworkDeviceVendorName_Type()
)
networkDeviceVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceVendorName.setStatus("mandatory")
_NetworkDeviceServiceName_Type = DellString
_NetworkDeviceServiceName_Object = MibTableColumn
networkDeviceServiceName = _NetworkDeviceServiceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 8),
    _NetworkDeviceServiceName_Type()
)
networkDeviceServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceServiceName.setStatus("mandatory")
_NetworkDeviceDriverImagePathName_Type = DellString
_NetworkDeviceDriverImagePathName_Object = MibTableColumn
networkDeviceDriverImagePathName = _NetworkDeviceDriverImagePathName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 9),
    _NetworkDeviceDriverImagePathName_Type()
)
networkDeviceDriverImagePathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceDriverImagePathName.setStatus("mandatory")
_NetworkDeviceDriverVersionName_Type = DellString
_NetworkDeviceDriverVersionName_Object = MibTableColumn
networkDeviceDriverVersionName = _NetworkDeviceDriverVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 10),
    _NetworkDeviceDriverVersionName_Type()
)
networkDeviceDriverVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceDriverVersionName.setStatus("mandatory")
_NetworkDeviceIPAddress_Type = IpAddress
_NetworkDeviceIPAddress_Object = MibTableColumn
networkDeviceIPAddress = _NetworkDeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 11),
    _NetworkDeviceIPAddress_Type()
)
networkDeviceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceIPAddress.setStatus("mandatory")
_NetworkDeviceIPSubnetMask_Type = IpAddress
_NetworkDeviceIPSubnetMask_Object = MibTableColumn
networkDeviceIPSubnetMask = _NetworkDeviceIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 12),
    _NetworkDeviceIPSubnetMask_Type()
)
networkDeviceIPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceIPSubnetMask.setStatus("mandatory")
_NetworkDeviceDefaultGatewayIPAddress_Type = IpAddress
_NetworkDeviceDefaultGatewayIPAddress_Object = MibTableColumn
networkDeviceDefaultGatewayIPAddress = _NetworkDeviceDefaultGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 13),
    _NetworkDeviceDefaultGatewayIPAddress_Type()
)
networkDeviceDefaultGatewayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceDefaultGatewayIPAddress.setStatus("mandatory")
_NetworkDeviceDHCPServerIPAddress_Type = IpAddress
_NetworkDeviceDHCPServerIPAddress_Object = MibTableColumn
networkDeviceDHCPServerIPAddress = _NetworkDeviceDHCPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 14),
    _NetworkDeviceDHCPServerIPAddress_Type()
)
networkDeviceDHCPServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceDHCPServerIPAddress.setStatus("mandatory")
_NetworkDeviceCurrentMACAddress_Type = DellMACAddress
_NetworkDeviceCurrentMACAddress_Object = MibTableColumn
networkDeviceCurrentMACAddress = _NetworkDeviceCurrentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 15),
    _NetworkDeviceCurrentMACAddress_Type()
)
networkDeviceCurrentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceCurrentMACAddress.setStatus("mandatory")
_NetworkDevicePermanentMACAddress_Type = DellMACAddress
_NetworkDevicePermanentMACAddress_Object = MibTableColumn
networkDevicePermanentMACAddress = _NetworkDevicePermanentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 16),
    _NetworkDevicePermanentMACAddress_Type()
)
networkDevicePermanentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePermanentMACAddress.setStatus("mandatory")
_NetworkDevicePCIBusNumber_Type = DellUnsigned8BitRange
_NetworkDevicePCIBusNumber_Object = MibTableColumn
networkDevicePCIBusNumber = _NetworkDevicePCIBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 17),
    _NetworkDevicePCIBusNumber_Type()
)
networkDevicePCIBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePCIBusNumber.setStatus("mandatory")
_NetworkDevicePCIDeviceNumber_Type = DellUnsigned8BitRange
_NetworkDevicePCIDeviceNumber_Object = MibTableColumn
networkDevicePCIDeviceNumber = _NetworkDevicePCIDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 18),
    _NetworkDevicePCIDeviceNumber_Type()
)
networkDevicePCIDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePCIDeviceNumber.setStatus("mandatory")
_NetworkDevicePCIFunctionNumber_Type = DellUnsigned8BitRange
_NetworkDevicePCIFunctionNumber_Object = MibTableColumn
networkDevicePCIFunctionNumber = _NetworkDevicePCIFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 19),
    _NetworkDevicePCIFunctionNumber_Type()
)
networkDevicePCIFunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePCIFunctionNumber.setStatus("mandatory")
_NetworkDeviceIRQ_Type = DellUnsigned32BitRange
_NetworkDeviceIRQ_Object = MibTableColumn
networkDeviceIRQ = _NetworkDeviceIRQ_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 20),
    _NetworkDeviceIRQ_Type()
)
networkDeviceIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceIRQ.setStatus("mandatory")
_NetworkDeviceBaseIOPortAddress_Type = DellUnsigned32BitRange
_NetworkDeviceBaseIOPortAddress_Object = MibTableColumn
networkDeviceBaseIOPortAddress = _NetworkDeviceBaseIOPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 21),
    _NetworkDeviceBaseIOPortAddress_Type()
)
networkDeviceBaseIOPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceBaseIOPortAddress.setStatus("mandatory")
_NetworkDeviceTeamingFlags_Type = DellNetworkDeviceTeamingFlags
_NetworkDeviceTeamingFlags_Object = MibTableColumn
networkDeviceTeamingFlags = _NetworkDeviceTeamingFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 22),
    _NetworkDeviceTeamingFlags_Type()
)
networkDeviceTeamingFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceTeamingFlags.setStatus("mandatory")
_NetworkDeviceTOECapabilityFlags_Type = DellNetworkDeviceTOECapabilityFlags
_NetworkDeviceTOECapabilityFlags_Object = MibTableColumn
networkDeviceTOECapabilityFlags = _NetworkDeviceTOECapabilityFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 23),
    _NetworkDeviceTOECapabilityFlags_Type()
)
networkDeviceTOECapabilityFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceTOECapabilityFlags.setStatus("mandatory")
_NetworkDeviceTOEEnabled_Type = DellBoolean
_NetworkDeviceTOEEnabled_Object = MibTableColumn
networkDeviceTOEEnabled = _NetworkDeviceTOEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 24),
    _NetworkDeviceTOEEnabled_Type()
)
networkDeviceTOEEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceTOEEnabled.setStatus("mandatory")
_NetworkDeviceRDMACapabilityFlags_Type = DellNetworkDeviceRDMACapabilityFlags
_NetworkDeviceRDMACapabilityFlags_Object = MibTableColumn
networkDeviceRDMACapabilityFlags = _NetworkDeviceRDMACapabilityFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 25),
    _NetworkDeviceRDMACapabilityFlags_Type()
)
networkDeviceRDMACapabilityFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceRDMACapabilityFlags.setStatus("mandatory")
_NetworkDeviceRDMAEnabled_Type = DellBoolean
_NetworkDeviceRDMAEnabled_Object = MibTableColumn
networkDeviceRDMAEnabled = _NetworkDeviceRDMAEnabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 26),
    _NetworkDeviceRDMAEnabled_Type()
)
networkDeviceRDMAEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceRDMAEnabled.setStatus("mandatory")
_NetworkDeviceiSCSICapabilityFlags_Type = DellNetworkDeviceiSCSICapabilityFlags
_NetworkDeviceiSCSICapabilityFlags_Object = MibTableColumn
networkDeviceiSCSICapabilityFlags = _NetworkDeviceiSCSICapabilityFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 27),
    _NetworkDeviceiSCSICapabilityFlags_Type()
)
networkDeviceiSCSICapabilityFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceiSCSICapabilityFlags.setStatus("mandatory")
_NetworkDeviceiSCSIEnabled_Type = DellBoolean
_NetworkDeviceiSCSIEnabled_Object = MibTableColumn
networkDeviceiSCSIEnabled = _NetworkDeviceiSCSIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 28),
    _NetworkDeviceiSCSIEnabled_Type()
)
networkDeviceiSCSIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceiSCSIEnabled.setStatus("mandatory")
_NetworkDeviceCapabilities_Type = DellNetworkDeviceCapabilities
_NetworkDeviceCapabilities_Object = MibTableColumn
networkDeviceCapabilities = _NetworkDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 29),
    _NetworkDeviceCapabilities_Type()
)
networkDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceCapabilities.setStatus("mandatory")
_NetworkDeviceNParEPEnabled_Type = DellNetworkDeviceNParEPEnabled
_NetworkDeviceNParEPEnabled_Object = MibTableColumn
networkDeviceNParEPEnabled = _NetworkDeviceNParEPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 90, 1, 30),
    _NetworkDeviceNParEPEnabled_Type()
)
networkDeviceNParEPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceNParEPEnabled.setStatus("mandatory")
_ManagedSystemServicesDeviceTable_Object = MibTable
managedSystemServicesDeviceTable = _ManagedSystemServicesDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100)
)
if mibBuilder.loadTexts:
    managedSystemServicesDeviceTable.setStatus("mandatory")
_ManagedSystemServicesDeviceTableEntry_Object = MibTableRow
managedSystemServicesDeviceTableEntry = _ManagedSystemServicesDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100, 1)
)
managedSystemServicesDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "managedSystemServicesDeviceChassisIndex"),
    (0, "MIB-Dell-10892", "managedSystemServicesDeviceIndex"),
)
if mibBuilder.loadTexts:
    managedSystemServicesDeviceTableEntry.setStatus("mandatory")
_ManagedSystemServicesDeviceChassisIndex_Type = DellObjectRange
_ManagedSystemServicesDeviceChassisIndex_Object = MibTableColumn
managedSystemServicesDeviceChassisIndex = _ManagedSystemServicesDeviceChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100, 1, 1),
    _ManagedSystemServicesDeviceChassisIndex_Type()
)
managedSystemServicesDeviceChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemServicesDeviceChassisIndex.setStatus("mandatory")
_ManagedSystemServicesDeviceIndex_Type = DellObjectRange
_ManagedSystemServicesDeviceIndex_Object = MibTableColumn
managedSystemServicesDeviceIndex = _ManagedSystemServicesDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100, 1, 2),
    _ManagedSystemServicesDeviceIndex_Type()
)
managedSystemServicesDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemServicesDeviceIndex.setStatus("mandatory")
_ManagedSystemServicesDeviceStatus_Type = DellStatus
_ManagedSystemServicesDeviceStatus_Object = MibTableColumn
managedSystemServicesDeviceStatus = _ManagedSystemServicesDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100, 1, 3),
    _ManagedSystemServicesDeviceStatus_Type()
)
managedSystemServicesDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemServicesDeviceStatus.setStatus("mandatory")
_ManagedSystemServicesDeviceType_Type = DellManagedSystemServicesDeviceType
_ManagedSystemServicesDeviceType_Object = MibTableColumn
managedSystemServicesDeviceType = _ManagedSystemServicesDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100, 1, 4),
    _ManagedSystemServicesDeviceType_Type()
)
managedSystemServicesDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemServicesDeviceType.setStatus("mandatory")
_ManagedSystemServicesDeviceStoragePresent_Type = DellBoolean
_ManagedSystemServicesDeviceStoragePresent_Object = MibTableColumn
managedSystemServicesDeviceStoragePresent = _ManagedSystemServicesDeviceStoragePresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100, 1, 5),
    _ManagedSystemServicesDeviceStoragePresent_Type()
)
managedSystemServicesDeviceStoragePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemServicesDeviceStoragePresent.setStatus("mandatory")
_ManagedSystemServicesDeviceStorageSize_Type = DellUnsigned32BitRange
_ManagedSystemServicesDeviceStorageSize_Object = MibTableColumn
managedSystemServicesDeviceStorageSize = _ManagedSystemServicesDeviceStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 100, 1, 6),
    _ManagedSystemServicesDeviceStorageSize_Type()
)
managedSystemServicesDeviceStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemServicesDeviceStorageSize.setStatus("mandatory")
_SdCardUnitTable_Object = MibTable
sdCardUnitTable = _SdCardUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110)
)
if mibBuilder.loadTexts:
    sdCardUnitTable.setStatus("mandatory")
_SdCardUnitTableEntry_Object = MibTableRow
sdCardUnitTableEntry = _SdCardUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1)
)
sdCardUnitTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "sdCardUnitChassisIndex"),
    (0, "MIB-Dell-10892", "sdCardUnitIndex"),
)
if mibBuilder.loadTexts:
    sdCardUnitTableEntry.setStatus("mandatory")
_SdCardUnitChassisIndex_Type = DellObjectRange
_SdCardUnitChassisIndex_Object = MibTableColumn
sdCardUnitChassisIndex = _SdCardUnitChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 1),
    _SdCardUnitChassisIndex_Type()
)
sdCardUnitChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitChassisIndex.setStatus("mandatory")
_SdCardUnitIndex_Type = DellObjectRange
_SdCardUnitIndex_Object = MibTableColumn
sdCardUnitIndex = _SdCardUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 2),
    _SdCardUnitIndex_Type()
)
sdCardUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitIndex.setStatus("mandatory")
_SdCardUnitStateCapabilities_Type = DellStateCapabilities
_SdCardUnitStateCapabilities_Object = MibTableColumn
sdCardUnitStateCapabilities = _SdCardUnitStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 3),
    _SdCardUnitStateCapabilities_Type()
)
sdCardUnitStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitStateCapabilities.setStatus("mandatory")
_SdCardUnitStateSettings_Type = DellStateSettings
_SdCardUnitStateSettings_Object = MibTableColumn
sdCardUnitStateSettings = _SdCardUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 4),
    _SdCardUnitStateSettings_Type()
)
sdCardUnitStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitStateSettings.setStatus("mandatory")
_SdCardUnitRedundancyStatus_Type = DellStatusRedundancy
_SdCardUnitRedundancyStatus_Object = MibTableColumn
sdCardUnitRedundancyStatus = _SdCardUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 5),
    _SdCardUnitRedundancyStatus_Type()
)
sdCardUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitRedundancyStatus.setStatus("mandatory")
_SdCardUnitCountForRedundancy_Type = DellObjectRange
_SdCardUnitCountForRedundancy_Object = MibTableColumn
sdCardUnitCountForRedundancy = _SdCardUnitCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 6),
    _SdCardUnitCountForRedundancy_Type()
)
sdCardUnitCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitCountForRedundancy.setStatus("mandatory")
_SdCardUnitName_Type = DellString
_SdCardUnitName_Object = MibTableColumn
sdCardUnitName = _SdCardUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 7),
    _SdCardUnitName_Type()
)
sdCardUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitName.setStatus("mandatory")
_SdCardUnitStatus_Type = DellStatus
_SdCardUnitStatus_Object = MibTableColumn
sdCardUnitStatus = _SdCardUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 110, 1, 8),
    _SdCardUnitStatus_Type()
)
sdCardUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardUnitStatus.setStatus("mandatory")
_SdCardDeviceTable_Object = MibTable
sdCardDeviceTable = _SdCardDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112)
)
if mibBuilder.loadTexts:
    sdCardDeviceTable.setStatus("mandatory")
_SdCardDeviceTableEntry_Object = MibTableRow
sdCardDeviceTableEntry = _SdCardDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1)
)
sdCardDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "sdCardDeviceChassisIndex"),
    (0, "MIB-Dell-10892", "sdCardDeviceIndex"),
)
if mibBuilder.loadTexts:
    sdCardDeviceTableEntry.setStatus("mandatory")
_SdCardDeviceChassisIndex_Type = DellObjectRange
_SdCardDeviceChassisIndex_Object = MibTableColumn
sdCardDeviceChassisIndex = _SdCardDeviceChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 1),
    _SdCardDeviceChassisIndex_Type()
)
sdCardDeviceChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceChassisIndex.setStatus("mandatory")
_SdCardDeviceIndex_Type = DellObjectRange
_SdCardDeviceIndex_Object = MibTableColumn
sdCardDeviceIndex = _SdCardDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 2),
    _SdCardDeviceIndex_Type()
)
sdCardDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceIndex.setStatus("mandatory")
_SdCardDeviceStatus_Type = DellStatus
_SdCardDeviceStatus_Object = MibTableColumn
sdCardDeviceStatus = _SdCardDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 3),
    _SdCardDeviceStatus_Type()
)
sdCardDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceStatus.setStatus("mandatory")
_SdCardDeviceType_Type = DellSDCardDeviceType
_SdCardDeviceType_Object = MibTableColumn
sdCardDeviceType = _SdCardDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 4),
    _SdCardDeviceType_Type()
)
sdCardDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceType.setStatus("mandatory")
_SdCardDeviceConfigCapabilities_Type = DellSDCardDeviceConfigCapabilities
_SdCardDeviceConfigCapabilities_Object = MibTableColumn
sdCardDeviceConfigCapabilities = _SdCardDeviceConfigCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 5),
    _SdCardDeviceConfigCapabilities_Type()
)
sdCardDeviceConfigCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceConfigCapabilities.setStatus("mandatory")
_SdCardDeviceConfigSettings_Type = DellSDCardDeviceConfigSettings
_SdCardDeviceConfigSettings_Object = MibTableColumn
sdCardDeviceConfigSettings = _SdCardDeviceConfigSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 6),
    _SdCardDeviceConfigSettings_Type()
)
sdCardDeviceConfigSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceConfigSettings.setStatus("mandatory")
_SdCardDeviceLocationName_Type = DellString
_SdCardDeviceLocationName_Object = MibTableColumn
sdCardDeviceLocationName = _SdCardDeviceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 7),
    _SdCardDeviceLocationName_Type()
)
sdCardDeviceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceLocationName.setStatus("mandatory")
_SdCardDeviceCardPresent_Type = DellBoolean
_SdCardDeviceCardPresent_Object = MibTableColumn
sdCardDeviceCardPresent = _SdCardDeviceCardPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 8),
    _SdCardDeviceCardPresent_Type()
)
sdCardDeviceCardPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceCardPresent.setStatus("mandatory")
_SdCardDeviceCardState_Type = DellSDCardDeviceCardState
_SdCardDeviceCardState_Object = MibTableColumn
sdCardDeviceCardState = _SdCardDeviceCardState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 9),
    _SdCardDeviceCardState_Type()
)
sdCardDeviceCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceCardState.setStatus("mandatory")
_SdCardDeviceCardStorageSize_Type = DellUnsigned32BitRange
_SdCardDeviceCardStorageSize_Object = MibTableColumn
sdCardDeviceCardStorageSize = _SdCardDeviceCardStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 10),
    _SdCardDeviceCardStorageSize_Type()
)
sdCardDeviceCardStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceCardStorageSize.setStatus("mandatory")
_SdCardDeviceUnitIndexReference_Type = DellObjectRange
_SdCardDeviceUnitIndexReference_Object = MibTableColumn
sdCardDeviceUnitIndexReference = _SdCardDeviceUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 11),
    _SdCardDeviceUnitIndexReference_Type()
)
sdCardDeviceUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceUnitIndexReference.setStatus("mandatory")
_SdCardDeviceCardAvailableStorageSize_Type = DellSigned32BitRange
_SdCardDeviceCardAvailableStorageSize_Object = MibTableColumn
sdCardDeviceCardAvailableStorageSize = _SdCardDeviceCardAvailableStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 12),
    _SdCardDeviceCardAvailableStorageSize_Type()
)
sdCardDeviceCardAvailableStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceCardAvailableStorageSize.setStatus("mandatory")
_SdCardDeviceCardLicensed_Type = DellSDCardDeviceCardLicensed
_SdCardDeviceCardLicensed_Object = MibTableColumn
sdCardDeviceCardLicensed = _SdCardDeviceCardLicensed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 112, 1, 13),
    _SdCardDeviceCardLicensed_Type()
)
sdCardDeviceCardLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdCardDeviceCardLicensed.setStatus("mandatory")
_SlotGroup_ObjectIdentity = ObjectIdentity
slotGroup = _SlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200)
)
_SystemSlotTable_Object = MibTable
systemSlotTable = _SystemSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10)
)
if mibBuilder.loadTexts:
    systemSlotTable.setStatus("mandatory")
_SystemSlotTableEntry_Object = MibTableRow
systemSlotTableEntry = _SystemSlotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1)
)
systemSlotTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemSlotchassisIndex"),
    (0, "MIB-Dell-10892", "systemSlotIndex"),
)
if mibBuilder.loadTexts:
    systemSlotTableEntry.setStatus("mandatory")
_SystemSlotchassisIndex_Type = DellObjectRange
_SystemSlotchassisIndex_Object = MibTableColumn
systemSlotchassisIndex = _SystemSlotchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 1),
    _SystemSlotchassisIndex_Type()
)
systemSlotchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotchassisIndex.setStatus("mandatory")
_SystemSlotIndex_Type = DellObjectRange
_SystemSlotIndex_Object = MibTableColumn
systemSlotIndex = _SystemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 2),
    _SystemSlotIndex_Type()
)
systemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotIndex.setStatus("mandatory")
_SystemSlotStateCapabilitiesUnique_Type = DellSystemSlotStateCapabilities
_SystemSlotStateCapabilitiesUnique_Object = MibTableColumn
systemSlotStateCapabilitiesUnique = _SystemSlotStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 3),
    _SystemSlotStateCapabilitiesUnique_Type()
)
systemSlotStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStateCapabilitiesUnique.setStatus("mandatory")
_SystemSlotStateSettingsUnique_Type = DellSystemSlotStateSettings
_SystemSlotStateSettingsUnique_Object = MibTableColumn
systemSlotStateSettingsUnique = _SystemSlotStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 4),
    _SystemSlotStateSettingsUnique_Type()
)
systemSlotStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStateSettingsUnique.setStatus("mandatory")
_SystemSlotStatus_Type = DellStatus
_SystemSlotStatus_Object = MibTableColumn
systemSlotStatus = _SystemSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 5),
    _SystemSlotStatus_Type()
)
systemSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStatus.setStatus("mandatory")
_SystemSlotCurrentUsage_Type = DellSystemSlotUsage
_SystemSlotCurrentUsage_Object = MibTableColumn
systemSlotCurrentUsage = _SystemSlotCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 6),
    _SystemSlotCurrentUsage_Type()
)
systemSlotCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotCurrentUsage.setStatus("mandatory")
_SystemSlotType_Type = DellSystemSlotType
_SystemSlotType_Object = MibTableColumn
systemSlotType = _SystemSlotType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 7),
    _SystemSlotType_Type()
)
systemSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotType.setStatus("mandatory")
_SystemSlotSlotExternalSlotName_Type = DellString
_SystemSlotSlotExternalSlotName_Object = MibTableColumn
systemSlotSlotExternalSlotName = _SystemSlotSlotExternalSlotName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 8),
    _SystemSlotSlotExternalSlotName_Type()
)
systemSlotSlotExternalSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotSlotExternalSlotName.setStatus("mandatory")
_SystemSlotLength_Type = DellSystemSlotLength
_SystemSlotLength_Object = MibTableColumn
systemSlotLength = _SystemSlotLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 9),
    _SystemSlotLength_Type()
)
systemSlotLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotLength.setStatus("mandatory")
_SystemSlotSlotID_Type = DellUnsigned32BitRange
_SystemSlotSlotID_Object = MibTableColumn
systemSlotSlotID = _SystemSlotSlotID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 10),
    _SystemSlotSlotID_Type()
)
systemSlotSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotSlotID.setStatus("mandatory")
_SystemSlotCategory_Type = DellSystemSlotCategory
_SystemSlotCategory_Object = MibTableColumn
systemSlotCategory = _SystemSlotCategory_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 11),
    _SystemSlotCategory_Type()
)
systemSlotCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotCategory.setStatus("mandatory")
_SystemSlotHotPlugBusWidth_Type = DellSystemSlotHotPlugBusWidth
_SystemSlotHotPlugBusWidth_Object = MibTableColumn
systemSlotHotPlugBusWidth = _SystemSlotHotPlugBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 12),
    _SystemSlotHotPlugBusWidth_Type()
)
systemSlotHotPlugBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotHotPlugBusWidth.setStatus("mandatory")
_SystemSlotHotPlugSlotSpeed_Type = DellUnsigned32BitRange
_SystemSlotHotPlugSlotSpeed_Object = MibTableColumn
systemSlotHotPlugSlotSpeed = _SystemSlotHotPlugSlotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 13),
    _SystemSlotHotPlugSlotSpeed_Type()
)
systemSlotHotPlugSlotSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotHotPlugSlotSpeed.setStatus("mandatory")
_SystemSlotHotPlugAdapterSpeed_Type = DellUnsigned32BitRange
_SystemSlotHotPlugAdapterSpeed_Object = MibTableColumn
systemSlotHotPlugAdapterSpeed = _SystemSlotHotPlugAdapterSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 14),
    _SystemSlotHotPlugAdapterSpeed_Type()
)
systemSlotHotPlugAdapterSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotHotPlugAdapterSpeed.setStatus("mandatory")
_MemoryGroup_ObjectIdentity = ObjectIdentity
memoryGroup = _MemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300)
)
_PhysicalMemoryArrayTable_Object = MibTable
physicalMemoryArrayTable = _PhysicalMemoryArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10)
)
if mibBuilder.loadTexts:
    physicalMemoryArrayTable.setStatus("mandatory")
_PhysicalMemoryArrayTableEntry_Object = MibTableRow
physicalMemoryArrayTableEntry = _PhysicalMemoryArrayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1)
)
physicalMemoryArrayTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "physicalMemoryArraychassisIndex"),
    (0, "MIB-Dell-10892", "physicalMemoryArrayIndex"),
)
if mibBuilder.loadTexts:
    physicalMemoryArrayTableEntry.setStatus("mandatory")
_PhysicalMemoryArraychassisIndex_Type = DellObjectRange
_PhysicalMemoryArraychassisIndex_Object = MibTableColumn
physicalMemoryArraychassisIndex = _PhysicalMemoryArraychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 1),
    _PhysicalMemoryArraychassisIndex_Type()
)
physicalMemoryArraychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArraychassisIndex.setStatus("mandatory")
_PhysicalMemoryArrayIndex_Type = DellObjectRange
_PhysicalMemoryArrayIndex_Object = MibTableColumn
physicalMemoryArrayIndex = _PhysicalMemoryArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 2),
    _PhysicalMemoryArrayIndex_Type()
)
physicalMemoryArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayIndex.setStatus("mandatory")
_PhysicalMemoryArrayStateCapabilities_Type = DellStateCapabilities
_PhysicalMemoryArrayStateCapabilities_Object = MibTableColumn
physicalMemoryArrayStateCapabilities = _PhysicalMemoryArrayStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 3),
    _PhysicalMemoryArrayStateCapabilities_Type()
)
physicalMemoryArrayStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayStateCapabilities.setStatus("mandatory")
_PhysicalMemoryArrayStateSettings_Type = DellStateSettings
_PhysicalMemoryArrayStateSettings_Object = MibTableColumn
physicalMemoryArrayStateSettings = _PhysicalMemoryArrayStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 4),
    _PhysicalMemoryArrayStateSettings_Type()
)
physicalMemoryArrayStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayStateSettings.setStatus("mandatory")
_PhysicalMemoryArrayStatus_Type = DellStatus
_PhysicalMemoryArrayStatus_Object = MibTableColumn
physicalMemoryArrayStatus = _PhysicalMemoryArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 5),
    _PhysicalMemoryArrayStatus_Type()
)
physicalMemoryArrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayStatus.setStatus("mandatory")
_PhysicalMemoryArrayUse_Type = DellPhysicalMemoryArrayUse
_PhysicalMemoryArrayUse_Object = MibTableColumn
physicalMemoryArrayUse = _PhysicalMemoryArrayUse_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 6),
    _PhysicalMemoryArrayUse_Type()
)
physicalMemoryArrayUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayUse.setStatus("mandatory")
_PhysicalMemoryArrayECCType_Type = DellPhysicalMemoryArrayECCType
_PhysicalMemoryArrayECCType_Object = MibTableColumn
physicalMemoryArrayECCType = _PhysicalMemoryArrayECCType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 7),
    _PhysicalMemoryArrayECCType_Type()
)
physicalMemoryArrayECCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCType.setStatus("mandatory")
_PhysicalMemoryArrayLocation_Type = DellPhysicalMemoryArrayLocation
_PhysicalMemoryArrayLocation_Object = MibTableColumn
physicalMemoryArrayLocation = _PhysicalMemoryArrayLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 8),
    _PhysicalMemoryArrayLocation_Type()
)
physicalMemoryArrayLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayLocation.setStatus("mandatory")
_PhysicalMemoryArrayMaximumSize_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayMaximumSize_Object = MibTableColumn
physicalMemoryArrayMaximumSize = _PhysicalMemoryArrayMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 9),
    _PhysicalMemoryArrayMaximumSize_Type()
)
physicalMemoryArrayMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMaximumSize.setStatus("deprecated")
_PhysicalMemoryArrayTotalNumberSockets_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayTotalNumberSockets_Object = MibTableColumn
physicalMemoryArrayTotalNumberSockets = _PhysicalMemoryArrayTotalNumberSockets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 10),
    _PhysicalMemoryArrayTotalNumberSockets_Type()
)
physicalMemoryArrayTotalNumberSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayTotalNumberSockets.setStatus("mandatory")
_PhysicalMemoryArrayInUseNumberSockets_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayInUseNumberSockets_Object = MibTableColumn
physicalMemoryArrayInUseNumberSockets = _PhysicalMemoryArrayInUseNumberSockets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 11),
    _PhysicalMemoryArrayInUseNumberSockets_Type()
)
physicalMemoryArrayInUseNumberSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayInUseNumberSockets.setStatus("mandatory")
_PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Type = DellSigned32BitRange
_PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Object = MibTableColumn
physicalMemoryArrayECCErrorNonRecoverableThreshold = _PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 12),
    _PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Type()
)
physicalMemoryArrayECCErrorNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorNonRecoverableThreshold.setStatus("mandatory")
_PhysicalMemoryArrayECCErrorCriticalThreshold_Type = DellSigned32BitRange
_PhysicalMemoryArrayECCErrorCriticalThreshold_Object = MibTableColumn
physicalMemoryArrayECCErrorCriticalThreshold = _PhysicalMemoryArrayECCErrorCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 13),
    _PhysicalMemoryArrayECCErrorCriticalThreshold_Type()
)
physicalMemoryArrayECCErrorCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorCriticalThreshold.setStatus("mandatory")
_PhysicalMemoryArrayECCErrorNonCriticalThreshold_Type = DellSigned32BitRange
_PhysicalMemoryArrayECCErrorNonCriticalThreshold_Object = MibTableColumn
physicalMemoryArrayECCErrorNonCriticalThreshold = _PhysicalMemoryArrayECCErrorNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 14),
    _PhysicalMemoryArrayECCErrorNonCriticalThreshold_Type()
)
physicalMemoryArrayECCErrorNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorNonCriticalThreshold.setStatus("mandatory")
_PhysicalMemoryArrayRedundantMemoryUnitIndexReference_Type = DellObjectRange
_PhysicalMemoryArrayRedundantMemoryUnitIndexReference_Object = MibTableColumn
physicalMemoryArrayRedundantMemoryUnitIndexReference = _PhysicalMemoryArrayRedundantMemoryUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 15),
    _PhysicalMemoryArrayRedundantMemoryUnitIndexReference_Type()
)
physicalMemoryArrayRedundantMemoryUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayRedundantMemoryUnitIndexReference.setStatus("mandatory")
_PhysicalMemoryArrayExtendedMaximumSize_Type = DellUnsigned64BitRange
_PhysicalMemoryArrayExtendedMaximumSize_Object = MibTableColumn
physicalMemoryArrayExtendedMaximumSize = _PhysicalMemoryArrayExtendedMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 16),
    _PhysicalMemoryArrayExtendedMaximumSize_Type()
)
physicalMemoryArrayExtendedMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayExtendedMaximumSize.setStatus("mandatory")
_PhysicalMemoryArrayMappedTable_Object = MibTable
physicalMemoryArrayMappedTable = _PhysicalMemoryArrayMappedTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20)
)
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedTable.setStatus("mandatory")
_PhysicalMemoryArrayMappedTableEntry_Object = MibTableRow
physicalMemoryArrayMappedTableEntry = _PhysicalMemoryArrayMappedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1)
)
physicalMemoryArrayMappedTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "physicalMemoryArrayMappedchassisIndex"),
    (0, "MIB-Dell-10892", "physicalMemoryArrayMappedIndex"),
)
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedTableEntry.setStatus("mandatory")
_PhysicalMemoryArrayMappedchassisIndex_Type = DellObjectRange
_PhysicalMemoryArrayMappedchassisIndex_Object = MibTableColumn
physicalMemoryArrayMappedchassisIndex = _PhysicalMemoryArrayMappedchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 1),
    _PhysicalMemoryArrayMappedchassisIndex_Type()
)
physicalMemoryArrayMappedchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedchassisIndex.setStatus("mandatory")
_PhysicalMemoryArrayMappedIndex_Type = DellObjectRange
_PhysicalMemoryArrayMappedIndex_Object = MibTableColumn
physicalMemoryArrayMappedIndex = _PhysicalMemoryArrayMappedIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 2),
    _PhysicalMemoryArrayMappedIndex_Type()
)
physicalMemoryArrayMappedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedIndex.setStatus("mandatory")
_PhysicalMemoryArrayMappedStateCapabilities_Type = DellStateCapabilities
_PhysicalMemoryArrayMappedStateCapabilities_Object = MibTableColumn
physicalMemoryArrayMappedStateCapabilities = _PhysicalMemoryArrayMappedStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 3),
    _PhysicalMemoryArrayMappedStateCapabilities_Type()
)
physicalMemoryArrayMappedStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStateCapabilities.setStatus("mandatory")
_PhysicalMemoryArrayMappedStateSettings_Type = DellStateSettings
_PhysicalMemoryArrayMappedStateSettings_Object = MibTableColumn
physicalMemoryArrayMappedStateSettings = _PhysicalMemoryArrayMappedStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 4),
    _PhysicalMemoryArrayMappedStateSettings_Type()
)
physicalMemoryArrayMappedStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStateSettings.setStatus("mandatory")
_PhysicalMemoryArrayMappedStatus_Type = DellStatus
_PhysicalMemoryArrayMappedStatus_Object = MibTableColumn
physicalMemoryArrayMappedStatus = _PhysicalMemoryArrayMappedStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 5),
    _PhysicalMemoryArrayMappedStatus_Type()
)
physicalMemoryArrayMappedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStatus.setStatus("mandatory")
_PhysicalMemoryArrayIndexReference_Type = DellObjectRange
_PhysicalMemoryArrayIndexReference_Object = MibTableColumn
physicalMemoryArrayIndexReference = _PhysicalMemoryArrayIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 6),
    _PhysicalMemoryArrayIndexReference_Type()
)
physicalMemoryArrayIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayIndexReference.setStatus("mandatory")
_PhysicalMemoryArrayMappedStartingAddress_Type = DellUnsigned64BitRange
_PhysicalMemoryArrayMappedStartingAddress_Object = MibTableColumn
physicalMemoryArrayMappedStartingAddress = _PhysicalMemoryArrayMappedStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 7),
    _PhysicalMemoryArrayMappedStartingAddress_Type()
)
physicalMemoryArrayMappedStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStartingAddress.setStatus("mandatory")
_PhysicalMemoryArrayMappedEndingAddress_Type = DellUnsigned64BitRange
_PhysicalMemoryArrayMappedEndingAddress_Object = MibTableColumn
physicalMemoryArrayMappedEndingAddress = _PhysicalMemoryArrayMappedEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 8),
    _PhysicalMemoryArrayMappedEndingAddress_Type()
)
physicalMemoryArrayMappedEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedEndingAddress.setStatus("mandatory")
_PhysicalMemoryArrayMappedPartitionWidth_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayMappedPartitionWidth_Object = MibTableColumn
physicalMemoryArrayMappedPartitionWidth = _PhysicalMemoryArrayMappedPartitionWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 9),
    _PhysicalMemoryArrayMappedPartitionWidth_Type()
)
physicalMemoryArrayMappedPartitionWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedPartitionWidth.setStatus("mandatory")
_PhysicalMemoryConfigTable_Object = MibTable
physicalMemoryConfigTable = _PhysicalMemoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30)
)
if mibBuilder.loadTexts:
    physicalMemoryConfigTable.setStatus("mandatory")
_PhysicalMemoryConfigTableEntry_Object = MibTableRow
physicalMemoryConfigTableEntry = _PhysicalMemoryConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1)
)
physicalMemoryConfigTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "physicalMemoryConfigChassisIndex"),
    (0, "MIB-Dell-10892", "physicalMemoryConfigIndex"),
)
if mibBuilder.loadTexts:
    physicalMemoryConfigTableEntry.setStatus("mandatory")
_PhysicalMemoryConfigChassisIndex_Type = DellObjectRange
_PhysicalMemoryConfigChassisIndex_Object = MibTableColumn
physicalMemoryConfigChassisIndex = _PhysicalMemoryConfigChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 1),
    _PhysicalMemoryConfigChassisIndex_Type()
)
physicalMemoryConfigChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigChassisIndex.setStatus("mandatory")
_PhysicalMemoryConfigIndex_Type = DellObjectRange
_PhysicalMemoryConfigIndex_Object = MibTableColumn
physicalMemoryConfigIndex = _PhysicalMemoryConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 2),
    _PhysicalMemoryConfigIndex_Type()
)
physicalMemoryConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigIndex.setStatus("mandatory")
_PhysicalMemoryConfigStateCapabilities_Type = DellPhysicalMemoryConfigStateCapabilities
_PhysicalMemoryConfigStateCapabilities_Object = MibTableColumn
physicalMemoryConfigStateCapabilities = _PhysicalMemoryConfigStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 3),
    _PhysicalMemoryConfigStateCapabilities_Type()
)
physicalMemoryConfigStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigStateCapabilities.setStatus("mandatory")
_PhysicalMemoryConfigStateSettings_Type = DellPhysicalMemoryConfigStateSettings
_PhysicalMemoryConfigStateSettings_Object = MibTableColumn
physicalMemoryConfigStateSettings = _PhysicalMemoryConfigStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 4),
    _PhysicalMemoryConfigStateSettings_Type()
)
physicalMemoryConfigStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigStateSettings.setStatus("mandatory")
_PhysicalMemoryConfigStatus_Type = DellStatus
_PhysicalMemoryConfigStatus_Object = MibTableColumn
physicalMemoryConfigStatus = _PhysicalMemoryConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 5),
    _PhysicalMemoryConfigStatus_Type()
)
physicalMemoryConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigStatus.setStatus("mandatory")
_PhysicalMemoryConfigRedundantCapabilities_Type = DellPhysicalMemoryConfigRedundantCapabilities
_PhysicalMemoryConfigRedundantCapabilities_Object = MibTableColumn
physicalMemoryConfigRedundantCapabilities = _PhysicalMemoryConfigRedundantCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 6),
    _PhysicalMemoryConfigRedundantCapabilities_Type()
)
physicalMemoryConfigRedundantCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigRedundantCapabilities.setStatus("mandatory")
_PhysicalMemoryConfigRedundantSettings_Type = DellPhysicalMemoryConfigRedundantSettings
_PhysicalMemoryConfigRedundantSettings_Object = MibTableColumn
physicalMemoryConfigRedundantSettings = _PhysicalMemoryConfigRedundantSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 7),
    _PhysicalMemoryConfigRedundantSettings_Type()
)
physicalMemoryConfigRedundantSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigRedundantSettings.setStatus("mandatory")
_PhysicalMemoryConfigMOMCapabilities_Type = DellPhysicalMemoryConfigMOMCapabilities
_PhysicalMemoryConfigMOMCapabilities_Object = MibTableColumn
physicalMemoryConfigMOMCapabilities = _PhysicalMemoryConfigMOMCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 8),
    _PhysicalMemoryConfigMOMCapabilities_Type()
)
physicalMemoryConfigMOMCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigMOMCapabilities.setStatus("mandatory")
_PhysicalMemoryConfigMOMSettings_Type = DellPhysicalMemoryConfigMOMSettings
_PhysicalMemoryConfigMOMSettings_Object = MibTableColumn
physicalMemoryConfigMOMSettings = _PhysicalMemoryConfigMOMSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 30, 1, 9),
    _PhysicalMemoryConfigMOMSettings_Type()
)
physicalMemoryConfigMOMSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryConfigMOMSettings.setStatus("mandatory")
_PhysicalMemoryLoggingTable_Object = MibTable
physicalMemoryLoggingTable = _PhysicalMemoryLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 40)
)
if mibBuilder.loadTexts:
    physicalMemoryLoggingTable.setStatus("mandatory")
_PhysicalMemoryLoggingTableEntry_Object = MibTableRow
physicalMemoryLoggingTableEntry = _PhysicalMemoryLoggingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 40, 1)
)
physicalMemoryLoggingTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "physicalMemoryLoggingChassisIndex"),
    (0, "MIB-Dell-10892", "physicalMemoryLoggingIndex"),
)
if mibBuilder.loadTexts:
    physicalMemoryLoggingTableEntry.setStatus("mandatory")
_PhysicalMemoryLoggingChassisIndex_Type = DellObjectRange
_PhysicalMemoryLoggingChassisIndex_Object = MibTableColumn
physicalMemoryLoggingChassisIndex = _PhysicalMemoryLoggingChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 40, 1, 1),
    _PhysicalMemoryLoggingChassisIndex_Type()
)
physicalMemoryLoggingChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryLoggingChassisIndex.setStatus("mandatory")
_PhysicalMemoryLoggingIndex_Type = DellObjectRange
_PhysicalMemoryLoggingIndex_Object = MibTableColumn
physicalMemoryLoggingIndex = _PhysicalMemoryLoggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 40, 1, 2),
    _PhysicalMemoryLoggingIndex_Type()
)
physicalMemoryLoggingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryLoggingIndex.setStatus("mandatory")
_PhysicalMemoryLoggingCapabilities_Type = DellPhysicalMemoryLoggingCapabilities
_PhysicalMemoryLoggingCapabilities_Object = MibTableColumn
physicalMemoryLoggingCapabilities = _PhysicalMemoryLoggingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 40, 1, 3),
    _PhysicalMemoryLoggingCapabilities_Type()
)
physicalMemoryLoggingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryLoggingCapabilities.setStatus("mandatory")
_PhysicalMemoryLoggingSettings_Type = DellPhysicalMemoryLoggingSettings
_PhysicalMemoryLoggingSettings_Object = MibTableColumn
physicalMemoryLoggingSettings = _PhysicalMemoryLoggingSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 40, 1, 4),
    _PhysicalMemoryLoggingSettings_Type()
)
physicalMemoryLoggingSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryLoggingSettings.setStatus("mandatory")
_PhysicalMemoryLoggingStatus_Type = DellStatus
_PhysicalMemoryLoggingStatus_Object = MibTableColumn
physicalMemoryLoggingStatus = _PhysicalMemoryLoggingStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 40, 1, 5),
    _PhysicalMemoryLoggingStatus_Type()
)
physicalMemoryLoggingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryLoggingStatus.setStatus("mandatory")
_RedundantMemoryUnitTable_Object = MibTable
redundantMemoryUnitTable = _RedundantMemoryUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50)
)
if mibBuilder.loadTexts:
    redundantMemoryUnitTable.setStatus("mandatory")
_RedundantMemoryUnitTableEntry_Object = MibTableRow
redundantMemoryUnitTableEntry = _RedundantMemoryUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1)
)
redundantMemoryUnitTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "redundantMemoryUnitChassisIndex"),
    (0, "MIB-Dell-10892", "redundantMemoryUnitIndex"),
)
if mibBuilder.loadTexts:
    redundantMemoryUnitTableEntry.setStatus("mandatory")
_RedundantMemoryUnitChassisIndex_Type = DellObjectRange
_RedundantMemoryUnitChassisIndex_Object = MibTableColumn
redundantMemoryUnitChassisIndex = _RedundantMemoryUnitChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1, 1),
    _RedundantMemoryUnitChassisIndex_Type()
)
redundantMemoryUnitChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantMemoryUnitChassisIndex.setStatus("mandatory")
_RedundantMemoryUnitIndex_Type = DellObjectRange
_RedundantMemoryUnitIndex_Object = MibTableColumn
redundantMemoryUnitIndex = _RedundantMemoryUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1, 2),
    _RedundantMemoryUnitIndex_Type()
)
redundantMemoryUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantMemoryUnitIndex.setStatus("mandatory")
_RedundantMemoryUnitStateCapabilities_Type = DellStateCapabilities
_RedundantMemoryUnitStateCapabilities_Object = MibTableColumn
redundantMemoryUnitStateCapabilities = _RedundantMemoryUnitStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1, 3),
    _RedundantMemoryUnitStateCapabilities_Type()
)
redundantMemoryUnitStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantMemoryUnitStateCapabilities.setStatus("mandatory")
_RedundantMemoryUnitStateSettings_Type = DellStateSettings
_RedundantMemoryUnitStateSettings_Object = MibTableColumn
redundantMemoryUnitStateSettings = _RedundantMemoryUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1, 4),
    _RedundantMemoryUnitStateSettings_Type()
)
redundantMemoryUnitStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantMemoryUnitStateSettings.setStatus("mandatory")
_RedundantMemoryUnitRedundancyStatus_Type = DellStatusRedundancy
_RedundantMemoryUnitRedundancyStatus_Object = MibTableColumn
redundantMemoryUnitRedundancyStatus = _RedundantMemoryUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1, 5),
    _RedundantMemoryUnitRedundancyStatus_Type()
)
redundantMemoryUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantMemoryUnitRedundancyStatus.setStatus("mandatory")
_RedundantMemoryUnitName_Type = DellString
_RedundantMemoryUnitName_Object = MibTableColumn
redundantMemoryUnitName = _RedundantMemoryUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1, 6),
    _RedundantMemoryUnitName_Type()
)
redundantMemoryUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantMemoryUnitName.setStatus("mandatory")
_RedundantMemoryUnitStatus_Type = DellStatus
_RedundantMemoryUnitStatus_Object = MibTableColumn
redundantMemoryUnitStatus = _RedundantMemoryUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 50, 1, 7),
    _RedundantMemoryUnitStatus_Type()
)
redundantMemoryUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantMemoryUnitStatus.setStatus("mandatory")
_PhysicalMemoryCardTable_Object = MibTable
physicalMemoryCardTable = _PhysicalMemoryCardTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60)
)
if mibBuilder.loadTexts:
    physicalMemoryCardTable.setStatus("mandatory")
_PhysicalMemoryCardTableEntry_Object = MibTableRow
physicalMemoryCardTableEntry = _PhysicalMemoryCardTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1)
)
physicalMemoryCardTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "physicalMemoryCardChassisIndex"),
    (0, "MIB-Dell-10892", "physicalMemoryCardIndex"),
)
if mibBuilder.loadTexts:
    physicalMemoryCardTableEntry.setStatus("mandatory")
_PhysicalMemoryCardChassisIndex_Type = DellObjectRange
_PhysicalMemoryCardChassisIndex_Object = MibTableColumn
physicalMemoryCardChassisIndex = _PhysicalMemoryCardChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 1),
    _PhysicalMemoryCardChassisIndex_Type()
)
physicalMemoryCardChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardChassisIndex.setStatus("mandatory")
_PhysicalMemoryCardIndex_Type = DellObjectRange
_PhysicalMemoryCardIndex_Object = MibTableColumn
physicalMemoryCardIndex = _PhysicalMemoryCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 2),
    _PhysicalMemoryCardIndex_Type()
)
physicalMemoryCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardIndex.setStatus("mandatory")
_PhysicalMemoryCardStateCapabilities_Type = DellStateCapabilities
_PhysicalMemoryCardStateCapabilities_Object = MibTableColumn
physicalMemoryCardStateCapabilities = _PhysicalMemoryCardStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 3),
    _PhysicalMemoryCardStateCapabilities_Type()
)
physicalMemoryCardStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardStateCapabilities.setStatus("mandatory")
_PhysicalMemoryCardStateSettings_Type = DellStateSettings
_PhysicalMemoryCardStateSettings_Object = MibTableColumn
physicalMemoryCardStateSettings = _PhysicalMemoryCardStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 4),
    _PhysicalMemoryCardStateSettings_Type()
)
physicalMemoryCardStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardStateSettings.setStatus("mandatory")
_PhysicalMemoryCardStatus_Type = DellStatus
_PhysicalMemoryCardStatus_Object = MibTableColumn
physicalMemoryCardStatus = _PhysicalMemoryCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 5),
    _PhysicalMemoryCardStatus_Type()
)
physicalMemoryCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardStatus.setStatus("mandatory")
_PhysicalMemoryCardName_Type = DellString
_PhysicalMemoryCardName_Object = MibTableColumn
physicalMemoryCardName = _PhysicalMemoryCardName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 6),
    _PhysicalMemoryCardName_Type()
)
physicalMemoryCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardName.setStatus("mandatory")
_PhysicalMemoryCardTotalNumberSockets_Type = DellUnsigned32BitRange
_PhysicalMemoryCardTotalNumberSockets_Object = MibTableColumn
physicalMemoryCardTotalNumberSockets = _PhysicalMemoryCardTotalNumberSockets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 7),
    _PhysicalMemoryCardTotalNumberSockets_Type()
)
physicalMemoryCardTotalNumberSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardTotalNumberSockets.setStatus("mandatory")
_PhysicalMemoryCardInUseNumberSockets_Type = DellUnsigned32BitRange
_PhysicalMemoryCardInUseNumberSockets_Object = MibTableColumn
physicalMemoryCardInUseNumberSockets = _PhysicalMemoryCardInUseNumberSockets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 8),
    _PhysicalMemoryCardInUseNumberSockets_Type()
)
physicalMemoryCardInUseNumberSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardInUseNumberSockets.setStatus("mandatory")
_PhysicalMemoryCardPhyMemArrayIndexReference_Type = DellObjectRange
_PhysicalMemoryCardPhyMemArrayIndexReference_Object = MibTableColumn
physicalMemoryCardPhyMemArrayIndexReference = _PhysicalMemoryCardPhyMemArrayIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 60, 1, 9),
    _PhysicalMemoryCardPhyMemArrayIndexReference_Type()
)
physicalMemoryCardPhyMemArrayIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryCardPhyMemArrayIndexReference.setStatus("mandatory")
_BiosSetUpControlGroup_ObjectIdentity = ObjectIdentity
biosSetUpControlGroup = _BiosSetUpControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400)
)
_BiosSetUpControlTable_Object = MibTable
biosSetUpControlTable = _BiosSetUpControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10)
)
if mibBuilder.loadTexts:
    biosSetUpControlTable.setStatus("mandatory")
_BiosSetUpControlTableEntry_Object = MibTableRow
biosSetUpControlTableEntry = _BiosSetUpControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1)
)
biosSetUpControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "biosSetUpControlchassisIndex"),
)
if mibBuilder.loadTexts:
    biosSetUpControlTableEntry.setStatus("mandatory")
_BiosSetUpControlchassisIndex_Type = DellObjectRange
_BiosSetUpControlchassisIndex_Object = MibTableColumn
biosSetUpControlchassisIndex = _BiosSetUpControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 1),
    _BiosSetUpControlchassisIndex_Type()
)
biosSetUpControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSetUpControlchassisIndex.setStatus("mandatory")
_BSUCpointingDeviceControlCapabilities_Type = DellStateCapabilities
_BSUCpointingDeviceControlCapabilities_Object = MibTableColumn
bSUCpointingDeviceControlCapabilities = _BSUCpointingDeviceControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 2),
    _BSUCpointingDeviceControlCapabilities_Type()
)
bSUCpointingDeviceControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlCapabilities.setStatus("mandatory")
_BSUCpointingDeviceControlSettings_Type = DellStateSettings
_BSUCpointingDeviceControlSettings_Object = MibTableColumn
bSUCpointingDeviceControlSettings = _BSUCpointingDeviceControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 3),
    _BSUCpointingDeviceControlSettings_Type()
)
bSUCpointingDeviceControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlSettings.setStatus("mandatory")
_BSUCpointingDeviceControlStatus_Type = DellStatus
_BSUCpointingDeviceControlStatus_Object = MibTableColumn
bSUCpointingDeviceControlStatus = _BSUCpointingDeviceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 4),
    _BSUCpointingDeviceControlStatus_Type()
)
bSUCpointingDeviceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlStatus.setStatus("mandatory")
_BSUCpointingDeviceControlName_Type = DellString
_BSUCpointingDeviceControlName_Object = MibTableColumn
bSUCpointingDeviceControlName = _BSUCpointingDeviceControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 5),
    _BSUCpointingDeviceControlName_Type()
)
bSUCpointingDeviceControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlName.setStatus("mandatory")
_BSUCnumLockControlCapabilities_Type = DellStateCapabilities
_BSUCnumLockControlCapabilities_Object = MibTableColumn
bSUCnumLockControlCapabilities = _BSUCnumLockControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 6),
    _BSUCnumLockControlCapabilities_Type()
)
bSUCnumLockControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnumLockControlCapabilities.setStatus("mandatory")
_BSUCnumLockControlSettings_Type = DellStateSettings
_BSUCnumLockControlSettings_Object = MibTableColumn
bSUCnumLockControlSettings = _BSUCnumLockControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 7),
    _BSUCnumLockControlSettings_Type()
)
bSUCnumLockControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnumLockControlSettings.setStatus("mandatory")
_BSUCnumLockControlStatus_Type = DellStatus
_BSUCnumLockControlStatus_Object = MibTableColumn
bSUCnumLockControlStatus = _BSUCnumLockControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 8),
    _BSUCnumLockControlStatus_Type()
)
bSUCnumLockControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnumLockControlStatus.setStatus("mandatory")
_BSUCnumLockControlName_Type = DellString
_BSUCnumLockControlName_Object = MibTableColumn
bSUCnumLockControlName = _BSUCnumLockControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 9),
    _BSUCnumLockControlName_Type()
)
bSUCnumLockControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnumLockControlName.setStatus("mandatory")
_BSUCprocessorSerialNumberControlCapabilities_Type = DellStateCapabilities
_BSUCprocessorSerialNumberControlCapabilities_Object = MibTableColumn
bSUCprocessorSerialNumberControlCapabilities = _BSUCprocessorSerialNumberControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 10),
    _BSUCprocessorSerialNumberControlCapabilities_Type()
)
bSUCprocessorSerialNumberControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlCapabilities.setStatus("mandatory")
_BSUCprocessorSerialNumberControlSettings_Type = DellStateSettings
_BSUCprocessorSerialNumberControlSettings_Object = MibTableColumn
bSUCprocessorSerialNumberControlSettings = _BSUCprocessorSerialNumberControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 11),
    _BSUCprocessorSerialNumberControlSettings_Type()
)
bSUCprocessorSerialNumberControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlSettings.setStatus("mandatory")
_BSUCprocessorSerialNumberControlStatus_Type = DellStatus
_BSUCprocessorSerialNumberControlStatus_Object = MibTableColumn
bSUCprocessorSerialNumberControlStatus = _BSUCprocessorSerialNumberControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 12),
    _BSUCprocessorSerialNumberControlStatus_Type()
)
bSUCprocessorSerialNumberControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlStatus.setStatus("mandatory")
_BSUCprocessorSerialNumberControlName_Type = DellString
_BSUCprocessorSerialNumberControlName_Object = MibTableColumn
bSUCprocessorSerialNumberControlName = _BSUCprocessorSerialNumberControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 13),
    _BSUCprocessorSerialNumberControlName_Type()
)
bSUCprocessorSerialNumberControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlName.setStatus("mandatory")
_BSUCspeakerControlCapabilitiesUnique_Type = DellSpeakerControlCapabilitiesUnique
_BSUCspeakerControlCapabilitiesUnique_Object = MibTableColumn
bSUCspeakerControlCapabilitiesUnique = _BSUCspeakerControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 14),
    _BSUCspeakerControlCapabilitiesUnique_Type()
)
bSUCspeakerControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCspeakerControlCapabilitiesUnique.setStatus("mandatory")
_BSUCspeakerControlSettingsUnique_Type = DellSpeakerControlSettingsUnique
_BSUCspeakerControlSettingsUnique_Object = MibTableColumn
bSUCspeakerControlSettingsUnique = _BSUCspeakerControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 15),
    _BSUCspeakerControlSettingsUnique_Type()
)
bSUCspeakerControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCspeakerControlSettingsUnique.setStatus("mandatory")
_BSUCspeakerControlStatus_Type = DellStatus
_BSUCspeakerControlStatus_Object = MibTableColumn
bSUCspeakerControlStatus = _BSUCspeakerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 16),
    _BSUCspeakerControlStatus_Type()
)
bSUCspeakerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCspeakerControlStatus.setStatus("mandatory")
_BSUCspeakerControlName_Type = DellString
_BSUCspeakerControlName_Object = MibTableColumn
bSUCspeakerControlName = _BSUCspeakerControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 17),
    _BSUCspeakerControlName_Type()
)
bSUCspeakerControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCspeakerControlName.setStatus("mandatory")
_BSUCnIFwakeonLanControlCapabilitiesUnique_Type = DellNIFwakeonLanControlCapabilitiesUnique
_BSUCnIFwakeonLanControlCapabilitiesUnique_Object = MibTableColumn
bSUCnIFwakeonLanControlCapabilitiesUnique = _BSUCnIFwakeonLanControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 18),
    _BSUCnIFwakeonLanControlCapabilitiesUnique_Type()
)
bSUCnIFwakeonLanControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlCapabilitiesUnique.setStatus("mandatory")
_BSUCnIFwakeonLanControlSettingsUnique_Type = DellNIFwakeonLanControlSettingsUnique
_BSUCnIFwakeonLanControlSettingsUnique_Object = MibTableColumn
bSUCnIFwakeonLanControlSettingsUnique = _BSUCnIFwakeonLanControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 19),
    _BSUCnIFwakeonLanControlSettingsUnique_Type()
)
bSUCnIFwakeonLanControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlSettingsUnique.setStatus("mandatory")
_BSUCnIFwakeonLanControlStatus_Type = DellStatus
_BSUCnIFwakeonLanControlStatus_Object = MibTableColumn
bSUCnIFwakeonLanControlStatus = _BSUCnIFwakeonLanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 20),
    _BSUCnIFwakeonLanControlStatus_Type()
)
bSUCnIFwakeonLanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlStatus.setStatus("mandatory")
_BSUCnIFwakeonLanControlName_Type = DellString
_BSUCnIFwakeonLanControlName_Object = MibTableColumn
bSUCnIFwakeonLanControlName = _BSUCnIFwakeonLanControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 21),
    _BSUCnIFwakeonLanControlName_Type()
)
bSUCnIFwakeonLanControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlName.setStatus("mandatory")
_BSUCbootSequenceControlCapabilitiesUnique_Type = DellBootSequenceControlCapabilitiesUnique
_BSUCbootSequenceControlCapabilitiesUnique_Object = MibTableColumn
bSUCbootSequenceControlCapabilitiesUnique = _BSUCbootSequenceControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 22),
    _BSUCbootSequenceControlCapabilitiesUnique_Type()
)
bSUCbootSequenceControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlCapabilitiesUnique.setStatus("mandatory")
_BSUCbootSequenceControlSettingsUnique_Type = DellBootSequenceControlSettingsUnique
_BSUCbootSequenceControlSettingsUnique_Object = MibTableColumn
bSUCbootSequenceControlSettingsUnique = _BSUCbootSequenceControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 23),
    _BSUCbootSequenceControlSettingsUnique_Type()
)
bSUCbootSequenceControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlSettingsUnique.setStatus("mandatory")
_BSUCbootSequenceControlStatus_Type = DellStatus
_BSUCbootSequenceControlStatus_Object = MibTableColumn
bSUCbootSequenceControlStatus = _BSUCbootSequenceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 24),
    _BSUCbootSequenceControlStatus_Type()
)
bSUCbootSequenceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlStatus.setStatus("mandatory")
_BSUCbootSequenceControlName_Type = DellString
_BSUCbootSequenceControlName_Object = MibTableColumn
bSUCbootSequenceControlName = _BSUCbootSequenceControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 25),
    _BSUCbootSequenceControlName_Type()
)
bSUCbootSequenceControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlName.setStatus("mandatory")
_BSUCadministratorPasswordControlCapabilitiesUnique_Type = DellBIOSPasswordControlCapabilitiesUnique
_BSUCadministratorPasswordControlCapabilitiesUnique_Object = MibTableColumn
bSUCadministratorPasswordControlCapabilitiesUnique = _BSUCadministratorPasswordControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 26),
    _BSUCadministratorPasswordControlCapabilitiesUnique_Type()
)
bSUCadministratorPasswordControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlCapabilitiesUnique.setStatus("mandatory")
_BSUCadministratorPasswordControlSettingsUnique_Type = DellBIOSPasswordControlSettingsUnique
_BSUCadministratorPasswordControlSettingsUnique_Object = MibTableColumn
bSUCadministratorPasswordControlSettingsUnique = _BSUCadministratorPasswordControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 27),
    _BSUCadministratorPasswordControlSettingsUnique_Type()
)
bSUCadministratorPasswordControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlSettingsUnique.setStatus("mandatory")
_BSUCadministratorPasswordControlStatus_Type = DellStatus
_BSUCadministratorPasswordControlStatus_Object = MibTableColumn
bSUCadministratorPasswordControlStatus = _BSUCadministratorPasswordControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 28),
    _BSUCadministratorPasswordControlStatus_Type()
)
bSUCadministratorPasswordControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlStatus.setStatus("mandatory")
_BSUCadministratorPasswordPasswordVerifyName_Type = DellString
_BSUCadministratorPasswordPasswordVerifyName_Object = MibTableColumn
bSUCadministratorPasswordPasswordVerifyName = _BSUCadministratorPasswordPasswordVerifyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 29),
    _BSUCadministratorPasswordPasswordVerifyName_Type()
)
bSUCadministratorPasswordPasswordVerifyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordPasswordVerifyName.setStatus("mandatory")
_BSUCadministratorPasswordNewPasswordName_Type = DellString
_BSUCadministratorPasswordNewPasswordName_Object = MibTableColumn
bSUCadministratorPasswordNewPasswordName = _BSUCadministratorPasswordNewPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 30),
    _BSUCadministratorPasswordNewPasswordName_Type()
)
bSUCadministratorPasswordNewPasswordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordNewPasswordName.setStatus("mandatory")
_BSUCuserPasswordControlCapabilitiesUnique_Type = DellBIOSPasswordControlCapabilitiesUnique
_BSUCuserPasswordControlCapabilitiesUnique_Object = MibTableColumn
bSUCuserPasswordControlCapabilitiesUnique = _BSUCuserPasswordControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 31),
    _BSUCuserPasswordControlCapabilitiesUnique_Type()
)
bSUCuserPasswordControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlCapabilitiesUnique.setStatus("mandatory")
_BSUCuserPasswordControlSettingsUnique_Type = DellBIOSPasswordControlSettingsUnique
_BSUCuserPasswordControlSettingsUnique_Object = MibTableColumn
bSUCuserPasswordControlSettingsUnique = _BSUCuserPasswordControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 32),
    _BSUCuserPasswordControlSettingsUnique_Type()
)
bSUCuserPasswordControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlSettingsUnique.setStatus("mandatory")
_BSUCuserPasswordControlStatus_Type = DellStatus
_BSUCuserPasswordControlStatus_Object = MibTableColumn
bSUCuserPasswordControlStatus = _BSUCuserPasswordControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 33),
    _BSUCuserPasswordControlStatus_Type()
)
bSUCuserPasswordControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlStatus.setStatus("mandatory")
_BSUCuserPasswordPasswordVerifyName_Type = DellString
_BSUCuserPasswordPasswordVerifyName_Object = MibTableColumn
bSUCuserPasswordPasswordVerifyName = _BSUCuserPasswordPasswordVerifyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 34),
    _BSUCuserPasswordPasswordVerifyName_Type()
)
bSUCuserPasswordPasswordVerifyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCuserPasswordPasswordVerifyName.setStatus("mandatory")
_BSUCuserPasswordNewPasswordName_Type = DellString
_BSUCuserPasswordNewPasswordName_Object = MibTableColumn
bSUCuserPasswordNewPasswordName = _BSUCuserPasswordNewPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 35),
    _BSUCuserPasswordNewPasswordName_Type()
)
bSUCuserPasswordNewPasswordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCuserPasswordNewPasswordName.setStatus("mandatory")
_BSUCtpmSecurityControlCapabilities_Type = DellTPMSecurityControlCapabilities
_BSUCtpmSecurityControlCapabilities_Object = MibTableColumn
bSUCtpmSecurityControlCapabilities = _BSUCtpmSecurityControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 36),
    _BSUCtpmSecurityControlCapabilities_Type()
)
bSUCtpmSecurityControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCtpmSecurityControlCapabilities.setStatus("mandatory")
_BSUCtpmSecurityControlSetting_Type = DellTPMSecurityControlSetting
_BSUCtpmSecurityControlSetting_Object = MibTableColumn
bSUCtpmSecurityControlSetting = _BSUCtpmSecurityControlSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 37),
    _BSUCtpmSecurityControlSetting_Type()
)
bSUCtpmSecurityControlSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCtpmSecurityControlSetting.setStatus("mandatory")
_BSUCtpmSecurityControlStatus_Type = DellStatus
_BSUCtpmSecurityControlStatus_Object = MibTableColumn
bSUCtpmSecurityControlStatus = _BSUCtpmSecurityControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 38),
    _BSUCtpmSecurityControlStatus_Type()
)
bSUCtpmSecurityControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCtpmSecurityControlStatus.setStatus("mandatory")
_BSUCtpmSecurityControlName_Type = DellString
_BSUCtpmSecurityControlName_Object = MibTableColumn
bSUCtpmSecurityControlName = _BSUCtpmSecurityControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 39),
    _BSUCtpmSecurityControlName_Type()
)
bSUCtpmSecurityControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCtpmSecurityControlName.setStatus("mandatory")
_SCSIControlTable_Object = MibTable
sCSIControlTable = _SCSIControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20)
)
if mibBuilder.loadTexts:
    sCSIControlTable.setStatus("mandatory")
_SCSIControlTableEntry_Object = MibTableRow
sCSIControlTableEntry = _SCSIControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1)
)
sCSIControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "sCSIControlchassisIndex"),
    (0, "MIB-Dell-10892", "sCSIControlIndex"),
)
if mibBuilder.loadTexts:
    sCSIControlTableEntry.setStatus("mandatory")
_SCSIControlchassisIndex_Type = DellObjectRange
_SCSIControlchassisIndex_Object = MibTableColumn
sCSIControlchassisIndex = _SCSIControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 1),
    _SCSIControlchassisIndex_Type()
)
sCSIControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlchassisIndex.setStatus("mandatory")
_SCSIControlIndex_Type = DellObjectRange
_SCSIControlIndex_Object = MibTableColumn
sCSIControlIndex = _SCSIControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 2),
    _SCSIControlIndex_Type()
)
sCSIControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlIndex.setStatus("mandatory")
_SCSIControlCapabilities_Type = DellStateCapabilities
_SCSIControlCapabilities_Object = MibTableColumn
sCSIControlCapabilities = _SCSIControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 3),
    _SCSIControlCapabilities_Type()
)
sCSIControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlCapabilities.setStatus("mandatory")
_SCSIControlSettings_Type = DellStateSettings
_SCSIControlSettings_Object = MibTableColumn
sCSIControlSettings = _SCSIControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 4),
    _SCSIControlSettings_Type()
)
sCSIControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlSettings.setStatus("mandatory")
_SCSIControlStatus_Type = DellStatus
_SCSIControlStatus_Object = MibTableColumn
sCSIControlStatus = _SCSIControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 5),
    _SCSIControlStatus_Type()
)
sCSIControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlStatus.setStatus("mandatory")
_SCSIControlName_Type = DellString
_SCSIControlName_Object = MibTableColumn
sCSIControlName = _SCSIControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 6),
    _SCSIControlName_Type()
)
sCSIControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlName.setStatus("mandatory")
_ParallelPortControlTable_Object = MibTable
parallelPortControlTable = _ParallelPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30)
)
if mibBuilder.loadTexts:
    parallelPortControlTable.setStatus("mandatory")
_ParallelPortControlTableEntry_Object = MibTableRow
parallelPortControlTableEntry = _ParallelPortControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1)
)
parallelPortControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "parallelPortControlchassisIndex"),
    (0, "MIB-Dell-10892", "parallelPortControlIndex"),
)
if mibBuilder.loadTexts:
    parallelPortControlTableEntry.setStatus("mandatory")
_ParallelPortControlchassisIndex_Type = DellObjectRange
_ParallelPortControlchassisIndex_Object = MibTableColumn
parallelPortControlchassisIndex = _ParallelPortControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 1),
    _ParallelPortControlchassisIndex_Type()
)
parallelPortControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlchassisIndex.setStatus("mandatory")
_ParallelPortControlIndex_Type = DellObjectRange
_ParallelPortControlIndex_Object = MibTableColumn
parallelPortControlIndex = _ParallelPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 2),
    _ParallelPortControlIndex_Type()
)
parallelPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlIndex.setStatus("mandatory")
_ParallelPortControlCapabilitiesUnique_Type = DellParallelPortControlCapabilitiesUnique
_ParallelPortControlCapabilitiesUnique_Object = MibTableColumn
parallelPortControlCapabilitiesUnique = _ParallelPortControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 3),
    _ParallelPortControlCapabilitiesUnique_Type()
)
parallelPortControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlCapabilitiesUnique.setStatus("mandatory")
_ParallelPortControlSettingsUnique_Type = DellParallelPortControlSettingsUnique
_ParallelPortControlSettingsUnique_Object = MibTableColumn
parallelPortControlSettingsUnique = _ParallelPortControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 4),
    _ParallelPortControlSettingsUnique_Type()
)
parallelPortControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlSettingsUnique.setStatus("mandatory")
_ParallelPortControlStatus_Type = DellStatus
_ParallelPortControlStatus_Object = MibTableColumn
parallelPortControlStatus = _ParallelPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 5),
    _ParallelPortControlStatus_Type()
)
parallelPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlStatus.setStatus("mandatory")
_ParallelPortControlName_Type = DellString
_ParallelPortControlName_Object = MibTableColumn
parallelPortControlName = _ParallelPortControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 6),
    _ParallelPortControlName_Type()
)
parallelPortControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlName.setStatus("mandatory")
_ParallelPortControlModeCapabilitiesUnique_Type = DellParallelPortControlModeCapabilitiesUnique
_ParallelPortControlModeCapabilitiesUnique_Object = MibTableColumn
parallelPortControlModeCapabilitiesUnique = _ParallelPortControlModeCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 7),
    _ParallelPortControlModeCapabilitiesUnique_Type()
)
parallelPortControlModeCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlModeCapabilitiesUnique.setStatus("mandatory")
_ParallelPortControlModeSettingsUnique_Type = DellParallelPortControlModeSettingsUnique
_ParallelPortControlModeSettingsUnique_Object = MibTableColumn
parallelPortControlModeSettingsUnique = _ParallelPortControlModeSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 8),
    _ParallelPortControlModeSettingsUnique_Type()
)
parallelPortControlModeSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlModeSettingsUnique.setStatus("mandatory")
_SerialPortControlTable_Object = MibTable
serialPortControlTable = _SerialPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40)
)
if mibBuilder.loadTexts:
    serialPortControlTable.setStatus("mandatory")
_SerialPortControlTableEntry_Object = MibTableRow
serialPortControlTableEntry = _SerialPortControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1)
)
serialPortControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "serialPortControlchassisIndex"),
    (0, "MIB-Dell-10892", "serialPortControlIndex"),
)
if mibBuilder.loadTexts:
    serialPortControlTableEntry.setStatus("mandatory")
_SerialPortControlchassisIndex_Type = DellObjectRange
_SerialPortControlchassisIndex_Object = MibTableColumn
serialPortControlchassisIndex = _SerialPortControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 1),
    _SerialPortControlchassisIndex_Type()
)
serialPortControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlchassisIndex.setStatus("mandatory")
_SerialPortControlIndex_Type = DellObjectRange
_SerialPortControlIndex_Object = MibTableColumn
serialPortControlIndex = _SerialPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 2),
    _SerialPortControlIndex_Type()
)
serialPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlIndex.setStatus("mandatory")
_SerialPortControlCapabilitiesUnique_Type = DellSerialPortControlCapabilitiesUnique
_SerialPortControlCapabilitiesUnique_Object = MibTableColumn
serialPortControlCapabilitiesUnique = _SerialPortControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 3),
    _SerialPortControlCapabilitiesUnique_Type()
)
serialPortControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlCapabilitiesUnique.setStatus("mandatory")
_SerialPortControlSettingsUnique_Type = DellSerialPortControlSettingsUnique
_SerialPortControlSettingsUnique_Object = MibTableColumn
serialPortControlSettingsUnique = _SerialPortControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 4),
    _SerialPortControlSettingsUnique_Type()
)
serialPortControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlSettingsUnique.setStatus("mandatory")
_SerialPortControlStatus_Type = DellStatus
_SerialPortControlStatus_Object = MibTableColumn
serialPortControlStatus = _SerialPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 5),
    _SerialPortControlStatus_Type()
)
serialPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlStatus.setStatus("mandatory")
_SerialPortControlName_Type = DellString
_SerialPortControlName_Object = MibTableColumn
serialPortControlName = _SerialPortControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 6),
    _SerialPortControlName_Type()
)
serialPortControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlName.setStatus("mandatory")
_UsbControlTable_Object = MibTable
usbControlTable = _UsbControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50)
)
if mibBuilder.loadTexts:
    usbControlTable.setStatus("mandatory")
_UsbControlTableEntry_Object = MibTableRow
usbControlTableEntry = _UsbControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1)
)
usbControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "usbControlchassisIndex"),
    (0, "MIB-Dell-10892", "usbControlIndex"),
)
if mibBuilder.loadTexts:
    usbControlTableEntry.setStatus("mandatory")
_UsbControlchassisIndex_Type = DellObjectRange
_UsbControlchassisIndex_Object = MibTableColumn
usbControlchassisIndex = _UsbControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 1),
    _UsbControlchassisIndex_Type()
)
usbControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlchassisIndex.setStatus("mandatory")
_UsbControlIndex_Type = DellObjectRange
_UsbControlIndex_Object = MibTableColumn
usbControlIndex = _UsbControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 2),
    _UsbControlIndex_Type()
)
usbControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlIndex.setStatus("mandatory")
_UsbControlCapabilities_Type = DellStateCapabilities
_UsbControlCapabilities_Object = MibTableColumn
usbControlCapabilities = _UsbControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 3),
    _UsbControlCapabilities_Type()
)
usbControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlCapabilities.setStatus("mandatory")
_UsbControlSettings_Type = DellStateSettings
_UsbControlSettings_Object = MibTableColumn
usbControlSettings = _UsbControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 4),
    _UsbControlSettings_Type()
)
usbControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlSettings.setStatus("mandatory")
_UsbControlStatus_Type = DellStatus
_UsbControlStatus_Object = MibTableColumn
usbControlStatus = _UsbControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 5),
    _UsbControlStatus_Type()
)
usbControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlStatus.setStatus("mandatory")
_UsbControlName_Type = DellString
_UsbControlName_Object = MibTableColumn
usbControlName = _UsbControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 6),
    _UsbControlName_Type()
)
usbControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlName.setStatus("mandatory")
_IdeControlTable_Object = MibTable
ideControlTable = _IdeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60)
)
if mibBuilder.loadTexts:
    ideControlTable.setStatus("mandatory")
_IdeControlTableEntry_Object = MibTableRow
ideControlTableEntry = _IdeControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1)
)
ideControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "ideControlchassisIndex"),
    (0, "MIB-Dell-10892", "ideControlIndex"),
)
if mibBuilder.loadTexts:
    ideControlTableEntry.setStatus("mandatory")
_IdeControlchassisIndex_Type = DellObjectRange
_IdeControlchassisIndex_Object = MibTableColumn
ideControlchassisIndex = _IdeControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 1),
    _IdeControlchassisIndex_Type()
)
ideControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlchassisIndex.setStatus("mandatory")
_IdeControlIndex_Type = DellObjectRange
_IdeControlIndex_Object = MibTableColumn
ideControlIndex = _IdeControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 2),
    _IdeControlIndex_Type()
)
ideControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlIndex.setStatus("mandatory")
_IdeControlCapabilitiesUnique_Type = DellideControlCapabilitiesUnique
_IdeControlCapabilitiesUnique_Object = MibTableColumn
ideControlCapabilitiesUnique = _IdeControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 3),
    _IdeControlCapabilitiesUnique_Type()
)
ideControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlCapabilitiesUnique.setStatus("mandatory")
_IdeControlSettingsUnique_Type = DellideControlSettingsUnique
_IdeControlSettingsUnique_Object = MibTableColumn
ideControlSettingsUnique = _IdeControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 4),
    _IdeControlSettingsUnique_Type()
)
ideControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlSettingsUnique.setStatus("mandatory")
_IdeControlStatus_Type = DellStatus
_IdeControlStatus_Object = MibTableColumn
ideControlStatus = _IdeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 5),
    _IdeControlStatus_Type()
)
ideControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlStatus.setStatus("mandatory")
_IdeControlName_Type = DellString
_IdeControlName_Object = MibTableColumn
ideControlName = _IdeControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 6),
    _IdeControlName_Type()
)
ideControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlName.setStatus("mandatory")
_DisketteControlTable_Object = MibTable
disketteControlTable = _DisketteControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70)
)
if mibBuilder.loadTexts:
    disketteControlTable.setStatus("mandatory")
_DisketteControlTableEntry_Object = MibTableRow
disketteControlTableEntry = _DisketteControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1)
)
disketteControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "disketteControlchassisIndex"),
    (0, "MIB-Dell-10892", "disketteControlIndex"),
)
if mibBuilder.loadTexts:
    disketteControlTableEntry.setStatus("mandatory")
_DisketteControlchassisIndex_Type = DellObjectRange
_DisketteControlchassisIndex_Object = MibTableColumn
disketteControlchassisIndex = _DisketteControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 1),
    _DisketteControlchassisIndex_Type()
)
disketteControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlchassisIndex.setStatus("mandatory")
_DisketteControlIndex_Type = DellObjectRange
_DisketteControlIndex_Object = MibTableColumn
disketteControlIndex = _DisketteControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 2),
    _DisketteControlIndex_Type()
)
disketteControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlIndex.setStatus("mandatory")
_DisketteControlCapabilitiesUnique_Type = DellDisketteControlCapabilitiesUnique
_DisketteControlCapabilitiesUnique_Object = MibTableColumn
disketteControlCapabilitiesUnique = _DisketteControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 3),
    _DisketteControlCapabilitiesUnique_Type()
)
disketteControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlCapabilitiesUnique.setStatus("mandatory")
_DisketteControlSettingsUnique_Type = DellDisketteControlSettingsUnique
_DisketteControlSettingsUnique_Object = MibTableColumn
disketteControlSettingsUnique = _DisketteControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 4),
    _DisketteControlSettingsUnique_Type()
)
disketteControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlSettingsUnique.setStatus("mandatory")
_DisketteControlStatus_Type = DellStatus
_DisketteControlStatus_Object = MibTableColumn
disketteControlStatus = _DisketteControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 5),
    _DisketteControlStatus_Type()
)
disketteControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlStatus.setStatus("mandatory")
_DisketteControlName_Type = DellString
_DisketteControlName_Object = MibTableColumn
disketteControlName = _DisketteControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 6),
    _DisketteControlName_Type()
)
disketteControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlName.setStatus("mandatory")
_NetworkInterfaceControlTable_Object = MibTable
networkInterfaceControlTable = _NetworkInterfaceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80)
)
if mibBuilder.loadTexts:
    networkInterfaceControlTable.setStatus("mandatory")
_NetworkInterfaceControlTableEntry_Object = MibTableRow
networkInterfaceControlTableEntry = _NetworkInterfaceControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1)
)
networkInterfaceControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "networkInterfaceControlchassisIndex"),
    (0, "MIB-Dell-10892", "networkInterfaceControlIndex"),
)
if mibBuilder.loadTexts:
    networkInterfaceControlTableEntry.setStatus("mandatory")
_NetworkInterfaceControlchassisIndex_Type = DellObjectRange
_NetworkInterfaceControlchassisIndex_Object = MibTableColumn
networkInterfaceControlchassisIndex = _NetworkInterfaceControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 1),
    _NetworkInterfaceControlchassisIndex_Type()
)
networkInterfaceControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlchassisIndex.setStatus("mandatory")
_NetworkInterfaceControlIndex_Type = DellObjectRange
_NetworkInterfaceControlIndex_Object = MibTableColumn
networkInterfaceControlIndex = _NetworkInterfaceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 2),
    _NetworkInterfaceControlIndex_Type()
)
networkInterfaceControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlIndex.setStatus("mandatory")
_NetworkInterfaceControlCapabilitiesUnique_Type = DellNetworkInterfaceControlCapabilitiesUnique
_NetworkInterfaceControlCapabilitiesUnique_Object = MibTableColumn
networkInterfaceControlCapabilitiesUnique = _NetworkInterfaceControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 3),
    _NetworkInterfaceControlCapabilitiesUnique_Type()
)
networkInterfaceControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlCapabilitiesUnique.setStatus("mandatory")
_NetworkInterfaceControlSettingsUnique_Type = DellNetworkInterfaceControlSettingsUnique
_NetworkInterfaceControlSettingsUnique_Object = MibTableColumn
networkInterfaceControlSettingsUnique = _NetworkInterfaceControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 4),
    _NetworkInterfaceControlSettingsUnique_Type()
)
networkInterfaceControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlSettingsUnique.setStatus("mandatory")
_NetworkInterfaceControlStatus_Type = DellStatus
_NetworkInterfaceControlStatus_Object = MibTableColumn
networkInterfaceControlStatus = _NetworkInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 5),
    _NetworkInterfaceControlStatus_Type()
)
networkInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlStatus.setStatus("mandatory")
_NetworkInterfaceControlName_Type = DellString
_NetworkInterfaceControlName_Object = MibTableColumn
networkInterfaceControlName = _NetworkInterfaceControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 6),
    _NetworkInterfaceControlName_Type()
)
networkInterfaceControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlName.setStatus("mandatory")
_BiosSettingTable_Object = MibTable
biosSettingTable = _BiosSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90)
)
if mibBuilder.loadTexts:
    biosSettingTable.setStatus("mandatory")
_BiosSettingTableEntry_Object = MibTableRow
biosSettingTableEntry = _BiosSettingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1)
)
biosSettingTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "biosSettingChassisIndex"),
    (0, "MIB-Dell-10892", "biosSettingIndex"),
)
if mibBuilder.loadTexts:
    biosSettingTableEntry.setStatus("mandatory")
_BiosSettingChassisIndex_Type = DellObjectRange
_BiosSettingChassisIndex_Object = MibTableColumn
biosSettingChassisIndex = _BiosSettingChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 1),
    _BiosSettingChassisIndex_Type()
)
biosSettingChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingChassisIndex.setStatus("mandatory")
_BiosSettingIndex_Type = DellObjectRange
_BiosSettingIndex_Object = MibTableColumn
biosSettingIndex = _BiosSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 2),
    _BiosSettingIndex_Type()
)
biosSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingIndex.setStatus("mandatory")
_BiosSettingName_Type = DisplayString
_BiosSettingName_Object = MibTableColumn
biosSettingName = _BiosSettingName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 3),
    _BiosSettingName_Type()
)
biosSettingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingName.setStatus("mandatory")
_BiosSettingDisplayName_Type = DisplayString
_BiosSettingDisplayName_Object = MibTableColumn
biosSettingDisplayName = _BiosSettingDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 4),
    _BiosSettingDisplayName_Type()
)
biosSettingDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingDisplayName.setStatus("mandatory")
_BiosSettingValueType_Type = DellBIOSSettingValueType
_BiosSettingValueType_Object = MibTableColumn
biosSettingValueType = _BiosSettingValueType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 5),
    _BiosSettingValueType_Type()
)
biosSettingValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingValueType.setStatus("mandatory")
_BiosSettingCurrentValue_Type = DisplayString
_BiosSettingCurrentValue_Object = MibTableColumn
biosSettingCurrentValue = _BiosSettingCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 6),
    _BiosSettingCurrentValue_Type()
)
biosSettingCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingCurrentValue.setStatus("mandatory")
_BiosSettingPendingValue_Type = DisplayString
_BiosSettingPendingValue_Object = MibTableColumn
biosSettingPendingValue = _BiosSettingPendingValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 7),
    _BiosSettingPendingValue_Type()
)
biosSettingPendingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingPendingValue.setStatus("mandatory")
_BiosSettingDefaultValue_Type = DisplayString
_BiosSettingDefaultValue_Object = MibTableColumn
biosSettingDefaultValue = _BiosSettingDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 8),
    _BiosSettingDefaultValue_Type()
)
biosSettingDefaultValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingDefaultValue.setStatus("mandatory")
_BiosSettingPossibleValues_Type = DisplayString
_BiosSettingPossibleValues_Object = MibTableColumn
biosSettingPossibleValues = _BiosSettingPossibleValues_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 9),
    _BiosSettingPossibleValues_Type()
)
biosSettingPossibleValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingPossibleValues.setStatus("mandatory")
_BiosSettingDisplayOrder_Type = DellUnsigned32BitRange
_BiosSettingDisplayOrder_Object = MibTableColumn
biosSettingDisplayOrder = _BiosSettingDisplayOrder_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 10),
    _BiosSettingDisplayOrder_Type()
)
biosSettingDisplayOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingDisplayOrder.setStatus("mandatory")
_BiosSettingGroupDisplayName_Type = DisplayString
_BiosSettingGroupDisplayName_Object = MibTableColumn
biosSettingGroupDisplayName = _BiosSettingGroupDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 11),
    _BiosSettingGroupDisplayName_Type()
)
biosSettingGroupDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingGroupDisplayName.setStatus("mandatory")
_BiosSettingFQDD_Type = DisplayString
_BiosSettingFQDD_Object = MibTableColumn
biosSettingFQDD = _BiosSettingFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 90, 1, 12),
    _BiosSettingFQDD_Type()
)
biosSettingFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSettingFQDD.setStatus("mandatory")
_LraGroup_ObjectIdentity = ObjectIdentity
lraGroup = _LraGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500)
)
_LRAGlobalSettingsTable_Object = MibTable
lRAGlobalSettingsTable = _LRAGlobalSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10)
)
if mibBuilder.loadTexts:
    lRAGlobalSettingsTable.setStatus("mandatory")
_LRAGlobalSettingsTableEntry_Object = MibTableRow
lRAGlobalSettingsTableEntry = _LRAGlobalSettingsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1)
)
lRAGlobalSettingsTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "lRAGlobalchassisIndex"),
)
if mibBuilder.loadTexts:
    lRAGlobalSettingsTableEntry.setStatus("mandatory")
_LRAGlobalchassisIndex_Type = DellObjectRange
_LRAGlobalchassisIndex_Object = MibTableColumn
lRAGlobalchassisIndex = _LRAGlobalchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 1),
    _LRAGlobalchassisIndex_Type()
)
lRAGlobalchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalchassisIndex.setStatus("mandatory")
_LRAGlobalState_Type = DellStateSettings
_LRAGlobalState_Object = MibTableColumn
lRAGlobalState = _LRAGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 2),
    _LRAGlobalState_Type()
)
lRAGlobalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalState.setStatus("mandatory")
_LRAGlobalSettingsDisableTimeoutValue_Type = DellUnsigned32BitRange
_LRAGlobalSettingsDisableTimeoutValue_Object = MibTableColumn
lRAGlobalSettingsDisableTimeoutValue = _LRAGlobalSettingsDisableTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 3),
    _LRAGlobalSettingsDisableTimeoutValue_Type()
)
lRAGlobalSettingsDisableTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalSettingsDisableTimeoutValue.setStatus("mandatory")
_LRAGlobalSettingsCapabilitiesUnique_Type = DellLocalResponseAgentCapabilitiesUnique
_LRAGlobalSettingsCapabilitiesUnique_Object = MibTableColumn
lRAGlobalSettingsCapabilitiesUnique = _LRAGlobalSettingsCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 4),
    _LRAGlobalSettingsCapabilitiesUnique_Type()
)
lRAGlobalSettingsCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalSettingsCapabilitiesUnique.setStatus("mandatory")
_LRAGlobalThermalShutdownCapabilitiesUnique_Type = DellLRAThermalShutdownCapabilitiesUnique
_LRAGlobalThermalShutdownCapabilitiesUnique_Object = MibTableColumn
lRAGlobalThermalShutdownCapabilitiesUnique = _LRAGlobalThermalShutdownCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 5),
    _LRAGlobalThermalShutdownCapabilitiesUnique_Type()
)
lRAGlobalThermalShutdownCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalThermalShutdownCapabilitiesUnique.setStatus("mandatory")
_LRAGlobalThermalShutdownStateSettingsUnique_Type = DellLRAThermalShutdownStateSettingsUnique
_LRAGlobalThermalShutdownStateSettingsUnique_Object = MibTableColumn
lRAGlobalThermalShutdownStateSettingsUnique = _LRAGlobalThermalShutdownStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 6),
    _LRAGlobalThermalShutdownStateSettingsUnique_Type()
)
lRAGlobalThermalShutdownStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalThermalShutdownStateSettingsUnique.setStatus("mandatory")
_LRAActionTableTable_Object = MibTable
lRAActionTableTable = _LRAActionTableTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20)
)
if mibBuilder.loadTexts:
    lRAActionTableTable.setStatus("mandatory")
_LRAActionTableTableEntry_Object = MibTableRow
lRAActionTableTableEntry = _LRAActionTableTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1)
)
lRAActionTableTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "lRAActionTablechassisIndex"),
    (0, "MIB-Dell-10892", "lRAActionTableActionNumberIndex"),
)
if mibBuilder.loadTexts:
    lRAActionTableTableEntry.setStatus("mandatory")
_LRAActionTablechassisIndex_Type = DellObjectRange
_LRAActionTablechassisIndex_Object = MibTableColumn
lRAActionTablechassisIndex = _LRAActionTablechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 1),
    _LRAActionTablechassisIndex_Type()
)
lRAActionTablechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAActionTablechassisIndex.setStatus("mandatory")
_LRAActionTableActionNumberIndex_Type = DellUnsigned16BitRange
_LRAActionTableActionNumberIndex_Object = MibTableColumn
lRAActionTableActionNumberIndex = _LRAActionTableActionNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 2),
    _LRAActionTableActionNumberIndex_Type()
)
lRAActionTableActionNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAActionTableActionNumberIndex.setStatus("mandatory")


class _LRAActionTableUserApplicationName_Type(DisplayString):
    """Custom type lRAActionTableUserApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LRAActionTableUserApplicationName_Type.__name__ = "DisplayString"
_LRAActionTableUserApplicationName_Object = MibTableColumn
lRAActionTableUserApplicationName = _LRAActionTableUserApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 3),
    _LRAActionTableUserApplicationName_Type()
)
lRAActionTableUserApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAActionTableUserApplicationName.setStatus("mandatory")
_LRAActionTableSettingsUnique_Type = DellLocalResponseAgentSettingsUnique
_LRAActionTableSettingsUnique_Object = MibTableColumn
lRAActionTableSettingsUnique = _LRAActionTableSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 4),
    _LRAActionTableSettingsUnique_Type()
)
lRAActionTableSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAActionTableSettingsUnique.setStatus("mandatory")
_CooGroup_ObjectIdentity = ObjectIdentity
cooGroup = _CooGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600)
)
_CooTable_Object = MibTable
cooTable = _CooTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10)
)
if mibBuilder.loadTexts:
    cooTable.setStatus("mandatory")
_CooTableEntry_Object = MibTableRow
cooTableEntry = _CooTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1)
)
cooTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "coochassisIndex"),
)
if mibBuilder.loadTexts:
    cooTableEntry.setStatus("mandatory")
_CoochassisIndex_Type = DellObjectRange
_CoochassisIndex_Object = MibTableColumn
coochassisIndex = _CoochassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 1),
    _CoochassisIndex_Type()
)
coochassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coochassisIndex.setStatus("mandatory")
_CooState_Type = DellStateSettings
_CooState_Object = MibTableColumn
cooState = _CooState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 2),
    _CooState_Type()
)
cooState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooState.setStatus("mandatory")
_CooAquisitionPurchaseCost_Type = DellUnsigned32BitRange
_CooAquisitionPurchaseCost_Object = MibTableColumn
cooAquisitionPurchaseCost = _CooAquisitionPurchaseCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 3),
    _CooAquisitionPurchaseCost_Type()
)
cooAquisitionPurchaseCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseCost.setStatus("mandatory")
_CooAquisitionWayBillNumber_Type = DellUnsigned32BitRange
_CooAquisitionWayBillNumber_Object = MibTableColumn
cooAquisitionWayBillNumber = _CooAquisitionWayBillNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 4),
    _CooAquisitionWayBillNumber_Type()
)
cooAquisitionWayBillNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooAquisitionWayBillNumber.setStatus("mandatory")
_CooAquisitionInstallDateName_Type = DellDateName
_CooAquisitionInstallDateName_Object = MibTableColumn
cooAquisitionInstallDateName = _CooAquisitionInstallDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 5),
    _CooAquisitionInstallDateName_Type()
)
cooAquisitionInstallDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooAquisitionInstallDateName.setStatus("mandatory")
_CooAquisitionPurchaseOrder_Type = DellUnsigned32BitRange
_CooAquisitionPurchaseOrder_Object = MibTableColumn
cooAquisitionPurchaseOrder = _CooAquisitionPurchaseOrder_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 6),
    _CooAquisitionPurchaseOrder_Type()
)
cooAquisitionPurchaseOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseOrder.setStatus("mandatory")
_CooAquisitionPurchaseDateName_Type = DellDateName
_CooAquisitionPurchaseDateName_Object = MibTableColumn
cooAquisitionPurchaseDateName = _CooAquisitionPurchaseDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 7),
    _CooAquisitionPurchaseDateName_Type()
)
cooAquisitionPurchaseDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseDateName.setStatus("mandatory")
_CooAquisitionSigningAuthorityName_Type = DellCostofOwnershipString
_CooAquisitionSigningAuthorityName_Object = MibTableColumn
cooAquisitionSigningAuthorityName = _CooAquisitionSigningAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 8),
    _CooAquisitionSigningAuthorityName_Type()
)
cooAquisitionSigningAuthorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooAquisitionSigningAuthorityName.setStatus("mandatory")
_CooOriginalMachineConfigurationExpensed_Type = DellBoolean
_CooOriginalMachineConfigurationExpensed_Object = MibTableColumn
cooOriginalMachineConfigurationExpensed = _CooOriginalMachineConfigurationExpensed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 9),
    _CooOriginalMachineConfigurationExpensed_Type()
)
cooOriginalMachineConfigurationExpensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOriginalMachineConfigurationExpensed.setStatus("mandatory")
_CooOriginalMachineConfigurationVendorName_Type = DellCostofOwnershipString
_CooOriginalMachineConfigurationVendorName_Object = MibTableColumn
cooOriginalMachineConfigurationVendorName = _CooOriginalMachineConfigurationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 10),
    _CooOriginalMachineConfigurationVendorName_Type()
)
cooOriginalMachineConfigurationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOriginalMachineConfigurationVendorName.setStatus("mandatory")
_CooCostCenterInformationVendorName_Type = DellCostofOwnershipString
_CooCostCenterInformationVendorName_Object = MibTableColumn
cooCostCenterInformationVendorName = _CooCostCenterInformationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 11),
    _CooCostCenterInformationVendorName_Type()
)
cooCostCenterInformationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostCenterInformationVendorName.setStatus("mandatory")
_CooUserInformationUserName_Type = DellCostofOwnershipString
_CooUserInformationUserName_Object = MibTableColumn
cooUserInformationUserName = _CooUserInformationUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 12),
    _CooUserInformationUserName_Type()
)
cooUserInformationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooUserInformationUserName.setStatus("mandatory")
_CooExtendedWarrantyStartDateName_Type = DellDateName
_CooExtendedWarrantyStartDateName_Object = MibTableColumn
cooExtendedWarrantyStartDateName = _CooExtendedWarrantyStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 13),
    _CooExtendedWarrantyStartDateName_Type()
)
cooExtendedWarrantyStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooExtendedWarrantyStartDateName.setStatus("mandatory")
_CooExtendedWarrantyEndDateName_Type = DellDateName
_CooExtendedWarrantyEndDateName_Object = MibTableColumn
cooExtendedWarrantyEndDateName = _CooExtendedWarrantyEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 14),
    _CooExtendedWarrantyEndDateName_Type()
)
cooExtendedWarrantyEndDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooExtendedWarrantyEndDateName.setStatus("mandatory")
_CooExtendedWarrantyCost_Type = DellUnsigned32BitRange
_CooExtendedWarrantyCost_Object = MibTableColumn
cooExtendedWarrantyCost = _CooExtendedWarrantyCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 15),
    _CooExtendedWarrantyCost_Type()
)
cooExtendedWarrantyCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooExtendedWarrantyCost.setStatus("mandatory")
_CooExtendedWarrantyProviderName_Type = DellCostofOwnershipString
_CooExtendedWarrantyProviderName_Object = MibTableColumn
cooExtendedWarrantyProviderName = _CooExtendedWarrantyProviderName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 16),
    _CooExtendedWarrantyProviderName_Type()
)
cooExtendedWarrantyProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooExtendedWarrantyProviderName.setStatus("mandatory")
_CooOwnershipCode_Type = DellCooOwnershipCodes
_CooOwnershipCode_Object = MibTableColumn
cooOwnershipCode = _CooOwnershipCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 17),
    _CooOwnershipCode_Type()
)
cooOwnershipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOwnershipCode.setStatus("mandatory")
_CooCorporateOwnerName_Type = DellCostofOwnershipString
_CooCorporateOwnerName_Object = MibTableColumn
cooCorporateOwnerName = _CooCorporateOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 18),
    _CooCorporateOwnerName_Type()
)
cooCorporateOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCorporateOwnerName.setStatus("mandatory")
_CooHazardousWasteCodeName_Type = DellCostofOwnershipString
_CooHazardousWasteCodeName_Object = MibTableColumn
cooHazardousWasteCodeName = _CooHazardousWasteCodeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 19),
    _CooHazardousWasteCodeName_Type()
)
cooHazardousWasteCodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooHazardousWasteCodeName.setStatus("mandatory")
_CooDeploymentDateLength_Type = DellUnsigned32BitRange
_CooDeploymentDateLength_Object = MibTableColumn
cooDeploymentDateLength = _CooDeploymentDateLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 20),
    _CooDeploymentDateLength_Type()
)
cooDeploymentDateLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooDeploymentDateLength.setStatus("mandatory")
_CooDeploymentDurationType_Type = DellCooHourDayDurationType
_CooDeploymentDurationType_Object = MibTableColumn
cooDeploymentDurationType = _CooDeploymentDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 21),
    _CooDeploymentDurationType_Type()
)
cooDeploymentDurationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooDeploymentDurationType.setStatus("mandatory")
_CooTrainingName_Type = DellCostofOwnershipString
_CooTrainingName_Object = MibTableColumn
cooTrainingName = _CooTrainingName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 22),
    _CooTrainingName_Type()
)
cooTrainingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTrainingName.setStatus("mandatory")
_CooOutsourcingProblemDescriptionName_Type = DellCostofOwnershipString
_CooOutsourcingProblemDescriptionName_Object = MibTableColumn
cooOutsourcingProblemDescriptionName = _CooOutsourcingProblemDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 23),
    _CooOutsourcingProblemDescriptionName_Type()
)
cooOutsourcingProblemDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOutsourcingProblemDescriptionName.setStatus("mandatory")
_CooOutsourcingServiceFeeName_Type = DellCostofOwnershipString
_CooOutsourcingServiceFeeName_Object = MibTableColumn
cooOutsourcingServiceFeeName = _CooOutsourcingServiceFeeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 24),
    _CooOutsourcingServiceFeeName_Type()
)
cooOutsourcingServiceFeeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOutsourcingServiceFeeName.setStatus("mandatory")
_CooOutsourcingSigningAuthorityName_Type = DellCostofOwnershipString
_CooOutsourcingSigningAuthorityName_Object = MibTableColumn
cooOutsourcingSigningAuthorityName = _CooOutsourcingSigningAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 25),
    _CooOutsourcingSigningAuthorityName_Type()
)
cooOutsourcingSigningAuthorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOutsourcingSigningAuthorityName.setStatus("mandatory")
_CooOutsourcingProviderFeeName_Type = DellCostofOwnershipString
_CooOutsourcingProviderFeeName_Object = MibTableColumn
cooOutsourcingProviderFeeName = _CooOutsourcingProviderFeeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 26),
    _CooOutsourcingProviderFeeName_Type()
)
cooOutsourcingProviderFeeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOutsourcingProviderFeeName.setStatus("mandatory")
_CooOutsourcingProviderServiceLevelName_Type = DellCostofOwnershipString
_CooOutsourcingProviderServiceLevelName_Object = MibTableColumn
cooOutsourcingProviderServiceLevelName = _CooOutsourcingProviderServiceLevelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 27),
    _CooOutsourcingProviderServiceLevelName_Type()
)
cooOutsourcingProviderServiceLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOutsourcingProviderServiceLevelName.setStatus("mandatory")
_CooInsuranceCompanyName_Type = DellCostofOwnershipString
_CooInsuranceCompanyName_Object = MibTableColumn
cooInsuranceCompanyName = _CooInsuranceCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 28),
    _CooInsuranceCompanyName_Type()
)
cooInsuranceCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooInsuranceCompanyName.setStatus("mandatory")
_CooBoxAssetTagName_Type = DellCostofOwnershipString
_CooBoxAssetTagName_Object = MibTableColumn
cooBoxAssetTagName = _CooBoxAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 29),
    _CooBoxAssetTagName_Type()
)
cooBoxAssetTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooBoxAssetTagName.setStatus("mandatory")
_CooBoxSystemName_Type = DellCostofOwnershipString
_CooBoxSystemName_Object = MibTableColumn
cooBoxSystemName = _CooBoxSystemName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 30),
    _CooBoxSystemName_Type()
)
cooBoxSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooBoxSystemName.setStatus("mandatory")
_CooBoxCPUSerialNumberName_Type = DellCostofOwnershipString
_CooBoxCPUSerialNumberName_Object = MibTableColumn
cooBoxCPUSerialNumberName = _CooBoxCPUSerialNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 31),
    _CooBoxCPUSerialNumberName_Type()
)
cooBoxCPUSerialNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooBoxCPUSerialNumberName.setStatus("mandatory")
_CooOperatingSystemUpgradeTypeName_Type = DellCostofOwnershipString
_CooOperatingSystemUpgradeTypeName_Object = MibTableColumn
cooOperatingSystemUpgradeTypeName = _CooOperatingSystemUpgradeTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 32),
    _CooOperatingSystemUpgradeTypeName_Type()
)
cooOperatingSystemUpgradeTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradeTypeName.setStatus("mandatory")
_CooOperatingSystemUpgradePatchLevelName_Type = DellCostofOwnershipString
_CooOperatingSystemUpgradePatchLevelName_Object = MibTableColumn
cooOperatingSystemUpgradePatchLevelName = _CooOperatingSystemUpgradePatchLevelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 33),
    _CooOperatingSystemUpgradePatchLevelName_Type()
)
cooOperatingSystemUpgradePatchLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradePatchLevelName.setStatus("mandatory")
_CooOperatingSystemUpgradeDate_Type = DellCostofOwnershipString
_CooOperatingSystemUpgradeDate_Object = MibTableColumn
cooOperatingSystemUpgradeDate = _CooOperatingSystemUpgradeDate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 34),
    _CooOperatingSystemUpgradeDate_Type()
)
cooOperatingSystemUpgradeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradeDate.setStatus("mandatory")
_CooDepreciationDuration_Type = DellUnsigned32BitRange
_CooDepreciationDuration_Object = MibTableColumn
cooDepreciationDuration = _CooDepreciationDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 35),
    _CooDepreciationDuration_Type()
)
cooDepreciationDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooDepreciationDuration.setStatus("mandatory")
_CooDepreciationDurationType_Type = DellCooMonthYearDurationType
_CooDepreciationDurationType_Object = MibTableColumn
cooDepreciationDurationType = _CooDepreciationDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 36),
    _CooDepreciationDurationType_Type()
)
cooDepreciationDurationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooDepreciationDurationType.setStatus("mandatory")
_CooDepreciationPercentage_Type = DellUnsigned32BitRange
_CooDepreciationPercentage_Object = MibTableColumn
cooDepreciationPercentage = _CooDepreciationPercentage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 37),
    _CooDepreciationPercentage_Type()
)
cooDepreciationPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooDepreciationPercentage.setStatus("mandatory")
_CooDepreciationMethodName_Type = DellCostofOwnershipString
_CooDepreciationMethodName_Object = MibTableColumn
cooDepreciationMethodName = _CooDepreciationMethodName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 38),
    _CooDepreciationMethodName_Type()
)
cooDepreciationMethodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooDepreciationMethodName.setStatus("mandatory")
_CooRegistrationIsRegistered_Type = DellBoolean
_CooRegistrationIsRegistered_Object = MibTableColumn
cooRegistrationIsRegistered = _CooRegistrationIsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 39),
    _CooRegistrationIsRegistered_Type()
)
cooRegistrationIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRegistrationIsRegistered.setStatus("mandatory")
_CooServiceContractTable_Object = MibTable
cooServiceContractTable = _CooServiceContractTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20)
)
if mibBuilder.loadTexts:
    cooServiceContractTable.setStatus("mandatory")
_CooServiceContractTableEntry_Object = MibTableRow
cooServiceContractTableEntry = _CooServiceContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1)
)
cooServiceContractTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooServiceContractchassisIndex"),
    (0, "MIB-Dell-10892", "cooServiceContractIndex"),
)
if mibBuilder.loadTexts:
    cooServiceContractTableEntry.setStatus("mandatory")
_CooServiceContractchassisIndex_Type = DellObjectRange
_CooServiceContractchassisIndex_Object = MibTableColumn
cooServiceContractchassisIndex = _CooServiceContractchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 1),
    _CooServiceContractchassisIndex_Type()
)
cooServiceContractchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractchassisIndex.setStatus("mandatory")
_CooServiceContractIndex_Type = DellObjectRange
_CooServiceContractIndex_Object = MibTableColumn
cooServiceContractIndex = _CooServiceContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 2),
    _CooServiceContractIndex_Type()
)
cooServiceContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractIndex.setStatus("mandatory")
_CooServiceContractState_Type = DellStateSettings
_CooServiceContractState_Object = MibTableColumn
cooServiceContractState = _CooServiceContractState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 3),
    _CooServiceContractState_Type()
)
cooServiceContractState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractState.setStatus("mandatory")
_CooServiceContractWasRenewed_Type = DellBoolean
_CooServiceContractWasRenewed_Object = MibTableColumn
cooServiceContractWasRenewed = _CooServiceContractWasRenewed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 4),
    _CooServiceContractWasRenewed_Type()
)
cooServiceContractWasRenewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractWasRenewed.setStatus("mandatory")
_CooServiceContractTypeName_Type = DellCostofOwnershipString
_CooServiceContractTypeName_Object = MibTableColumn
cooServiceContractTypeName = _CooServiceContractTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 5),
    _CooServiceContractTypeName_Type()
)
cooServiceContractTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractTypeName.setStatus("mandatory")
_CooServiceContractVendorName_Type = DellCostofOwnershipString
_CooServiceContractVendorName_Object = MibTableColumn
cooServiceContractVendorName = _CooServiceContractVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 6),
    _CooServiceContractVendorName_Type()
)
cooServiceContractVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractVendorName.setStatus("mandatory")
_CooCostEventLogTable_Object = MibTable
cooCostEventLogTable = _CooCostEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30)
)
if mibBuilder.loadTexts:
    cooCostEventLogTable.setStatus("mandatory")
_CooCostEventLogTableEntry_Object = MibTableRow
cooCostEventLogTableEntry = _CooCostEventLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1)
)
cooCostEventLogTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooCostEventLogchassisIndex"),
    (0, "MIB-Dell-10892", "cooCostEventLogIndex"),
)
if mibBuilder.loadTexts:
    cooCostEventLogTableEntry.setStatus("mandatory")
_CooCostEventLogchassisIndex_Type = DellObjectRange
_CooCostEventLogchassisIndex_Object = MibTableColumn
cooCostEventLogchassisIndex = _CooCostEventLogchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 1),
    _CooCostEventLogchassisIndex_Type()
)
cooCostEventLogchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogchassisIndex.setStatus("mandatory")
_CooCostEventLogIndex_Type = DellObjectRange
_CooCostEventLogIndex_Object = MibTableColumn
cooCostEventLogIndex = _CooCostEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 2),
    _CooCostEventLogIndex_Type()
)
cooCostEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogIndex.setStatus("mandatory")
_CooCostEventLogState_Type = DellStateSettings
_CooCostEventLogState_Object = MibTableColumn
cooCostEventLogState = _CooCostEventLogState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 3),
    _CooCostEventLogState_Type()
)
cooCostEventLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogState.setStatus("mandatory")
_CooCostEventLogDuration_Type = DellUnsigned32BitRange
_CooCostEventLogDuration_Object = MibTableColumn
cooCostEventLogDuration = _CooCostEventLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 4),
    _CooCostEventLogDuration_Type()
)
cooCostEventLogDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogDuration.setStatus("mandatory")
_CooCostEventLogDurationType_Type = DellCooHourDayDurationType
_CooCostEventLogDurationType_Object = MibTableColumn
cooCostEventLogDurationType = _CooCostEventLogDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 5),
    _CooCostEventLogDurationType_Type()
)
cooCostEventLogDurationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogDurationType.setStatus("mandatory")
_CooCostEventLogDescriptionName_Type = DellCostofOwnershipString
_CooCostEventLogDescriptionName_Object = MibTableColumn
cooCostEventLogDescriptionName = _CooCostEventLogDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 6),
    _CooCostEventLogDescriptionName_Type()
)
cooCostEventLogDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogDescriptionName.setStatus("mandatory")
_CooWarrantyTable_Object = MibTable
cooWarrantyTable = _CooWarrantyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40)
)
if mibBuilder.loadTexts:
    cooWarrantyTable.setStatus("mandatory")
_CooWarrantyTableEntry_Object = MibTableRow
cooWarrantyTableEntry = _CooWarrantyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1)
)
cooWarrantyTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooWarrantychassisIndex"),
    (0, "MIB-Dell-10892", "cooWarrantyIndex"),
)
if mibBuilder.loadTexts:
    cooWarrantyTableEntry.setStatus("mandatory")
_CooWarrantychassisIndex_Type = DellObjectRange
_CooWarrantychassisIndex_Object = MibTableColumn
cooWarrantychassisIndex = _CooWarrantychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 1),
    _CooWarrantychassisIndex_Type()
)
cooWarrantychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantychassisIndex.setStatus("mandatory")
_CooWarrantyIndex_Type = DellObjectRange
_CooWarrantyIndex_Object = MibTableColumn
cooWarrantyIndex = _CooWarrantyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 2),
    _CooWarrantyIndex_Type()
)
cooWarrantyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyIndex.setStatus("mandatory")
_CooWarrantyState_Type = DellStateSettings
_CooWarrantyState_Object = MibTableColumn
cooWarrantyState = _CooWarrantyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 3),
    _CooWarrantyState_Type()
)
cooWarrantyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyState.setStatus("mandatory")
_CooWarrantyDuration_Type = DellUnsigned32BitRange
_CooWarrantyDuration_Object = MibTableColumn
cooWarrantyDuration = _CooWarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 4),
    _CooWarrantyDuration_Type()
)
cooWarrantyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyDuration.setStatus("mandatory")
_CooWarrantyDurationType_Type = DellCooDayMonthDurationType
_CooWarrantyDurationType_Object = MibTableColumn
cooWarrantyDurationType = _CooWarrantyDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 5),
    _CooWarrantyDurationType_Type()
)
cooWarrantyDurationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyDurationType.setStatus("mandatory")
_CooWarrantyEndDateName_Type = DellDateName
_CooWarrantyEndDateName_Object = MibTableColumn
cooWarrantyEndDateName = _CooWarrantyEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 6),
    _CooWarrantyEndDateName_Type()
)
cooWarrantyEndDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyEndDateName.setStatus("mandatory")
_CooWarrantyCost_Type = DellUnsigned32BitRange
_CooWarrantyCost_Object = MibTableColumn
cooWarrantyCost = _CooWarrantyCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 7),
    _CooWarrantyCost_Type()
)
cooWarrantyCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyCost.setStatus("mandatory")
_CooLeaseInformationTable_Object = MibTable
cooLeaseInformationTable = _CooLeaseInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50)
)
if mibBuilder.loadTexts:
    cooLeaseInformationTable.setStatus("mandatory")
_CooLeaseInformationTableEntry_Object = MibTableRow
cooLeaseInformationTableEntry = _CooLeaseInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1)
)
cooLeaseInformationTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooLeaseInformationchassisIndex"),
    (0, "MIB-Dell-10892", "cooLeaseInformationIndex"),
)
if mibBuilder.loadTexts:
    cooLeaseInformationTableEntry.setStatus("mandatory")
_CooLeaseInformationchassisIndex_Type = DellObjectRange
_CooLeaseInformationchassisIndex_Object = MibTableColumn
cooLeaseInformationchassisIndex = _CooLeaseInformationchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 1),
    _CooLeaseInformationchassisIndex_Type()
)
cooLeaseInformationchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationchassisIndex.setStatus("mandatory")
_CooLeaseInformationIndex_Type = DellObjectRange
_CooLeaseInformationIndex_Object = MibTableColumn
cooLeaseInformationIndex = _CooLeaseInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 2),
    _CooLeaseInformationIndex_Type()
)
cooLeaseInformationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationIndex.setStatus("mandatory")
_CooLeaseInformationState_Type = DellStateSettings
_CooLeaseInformationState_Object = MibTableColumn
cooLeaseInformationState = _CooLeaseInformationState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 3),
    _CooLeaseInformationState_Type()
)
cooLeaseInformationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationState.setStatus("mandatory")
_CooLeaseInformationMultipleSchedules_Type = DellBoolean
_CooLeaseInformationMultipleSchedules_Object = MibTableColumn
cooLeaseInformationMultipleSchedules = _CooLeaseInformationMultipleSchedules_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 4),
    _CooLeaseInformationMultipleSchedules_Type()
)
cooLeaseInformationMultipleSchedules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationMultipleSchedules.setStatus("mandatory")
_CooLeaseInformationBuyOutAmount_Type = DellUnsigned32BitRange
_CooLeaseInformationBuyOutAmount_Object = MibTableColumn
cooLeaseInformationBuyOutAmount = _CooLeaseInformationBuyOutAmount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 5),
    _CooLeaseInformationBuyOutAmount_Type()
)
cooLeaseInformationBuyOutAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationBuyOutAmount.setStatus("mandatory")
_CooLeaseInformationLeaseRateFactor_Type = DellUnsigned32BitRange
_CooLeaseInformationLeaseRateFactor_Object = MibTableColumn
cooLeaseInformationLeaseRateFactor = _CooLeaseInformationLeaseRateFactor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 6),
    _CooLeaseInformationLeaseRateFactor_Type()
)
cooLeaseInformationLeaseRateFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationLeaseRateFactor.setStatus("mandatory")
_CooLeaseInformationEndDateName_Type = DellDateName
_CooLeaseInformationEndDateName_Object = MibTableColumn
cooLeaseInformationEndDateName = _CooLeaseInformationEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 7),
    _CooLeaseInformationEndDateName_Type()
)
cooLeaseInformationEndDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationEndDateName.setStatus("mandatory")
_CooLeaseInformationFairMarketValue_Type = DellUnsigned32BitRange
_CooLeaseInformationFairMarketValue_Object = MibTableColumn
cooLeaseInformationFairMarketValue = _CooLeaseInformationFairMarketValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 8),
    _CooLeaseInformationFairMarketValue_Type()
)
cooLeaseInformationFairMarketValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationFairMarketValue.setStatus("mandatory")
_CooLeaseInformationLessorName_Type = DellCostofOwnershipString
_CooLeaseInformationLessorName_Object = MibTableColumn
cooLeaseInformationLessorName = _CooLeaseInformationLessorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 9),
    _CooLeaseInformationLessorName_Type()
)
cooLeaseInformationLessorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationLessorName.setStatus("mandatory")
_CooScheduleNumberTable_Object = MibTable
cooScheduleNumberTable = _CooScheduleNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60)
)
if mibBuilder.loadTexts:
    cooScheduleNumberTable.setStatus("mandatory")
_CooScheduleNumberTableEntry_Object = MibTableRow
cooScheduleNumberTableEntry = _CooScheduleNumberTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1)
)
cooScheduleNumberTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooScheduleNumberchassisIndex"),
    (0, "MIB-Dell-10892", "cooScheduleNumberIndex"),
)
if mibBuilder.loadTexts:
    cooScheduleNumberTableEntry.setStatus("mandatory")
_CooScheduleNumberchassisIndex_Type = DellObjectRange
_CooScheduleNumberchassisIndex_Object = MibTableColumn
cooScheduleNumberchassisIndex = _CooScheduleNumberchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 1),
    _CooScheduleNumberchassisIndex_Type()
)
cooScheduleNumberchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberchassisIndex.setStatus("mandatory")
_CooScheduleNumberIndex_Type = DellObjectRange
_CooScheduleNumberIndex_Object = MibTableColumn
cooScheduleNumberIndex = _CooScheduleNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 2),
    _CooScheduleNumberIndex_Type()
)
cooScheduleNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberIndex.setStatus("mandatory")
_CooScheduleNumberState_Type = DellStateSettings
_CooScheduleNumberState_Object = MibTableColumn
cooScheduleNumberState = _CooScheduleNumberState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 3),
    _CooScheduleNumberState_Type()
)
cooScheduleNumberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberState.setStatus("mandatory")
_CooScheduleNumberLeaseInformationIndexReference_Type = DellUnsigned32BitRange
_CooScheduleNumberLeaseInformationIndexReference_Object = MibTableColumn
cooScheduleNumberLeaseInformationIndexReference = _CooScheduleNumberLeaseInformationIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 4),
    _CooScheduleNumberLeaseInformationIndexReference_Type()
)
cooScheduleNumberLeaseInformationIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberLeaseInformationIndexReference.setStatus("mandatory")
_CooScheduleNumberDescriptionName_Type = DellCostofOwnershipString
_CooScheduleNumberDescriptionName_Object = MibTableColumn
cooScheduleNumberDescriptionName = _CooScheduleNumberDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 5),
    _CooScheduleNumberDescriptionName_Type()
)
cooScheduleNumberDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberDescriptionName.setStatus("mandatory")
_CooOptionsTable_Object = MibTable
cooOptionsTable = _CooOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70)
)
if mibBuilder.loadTexts:
    cooOptionsTable.setStatus("mandatory")
_CooOptionsTableEntry_Object = MibTableRow
cooOptionsTableEntry = _CooOptionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1)
)
cooOptionsTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooOptionschassisIndex"),
    (0, "MIB-Dell-10892", "cooOptionsIndex"),
)
if mibBuilder.loadTexts:
    cooOptionsTableEntry.setStatus("mandatory")
_CooOptionschassisIndex_Type = DellObjectRange
_CooOptionschassisIndex_Object = MibTableColumn
cooOptionschassisIndex = _CooOptionschassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 1),
    _CooOptionschassisIndex_Type()
)
cooOptionschassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionschassisIndex.setStatus("mandatory")
_CooOptionsIndex_Type = DellObjectRange
_CooOptionsIndex_Object = MibTableColumn
cooOptionsIndex = _CooOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 2),
    _CooOptionsIndex_Type()
)
cooOptionsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionsIndex.setStatus("mandatory")
_CooOptionsState_Type = DellStateSettings
_CooOptionsState_Object = MibTableColumn
cooOptionsState = _CooOptionsState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 3),
    _CooOptionsState_Type()
)
cooOptionsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionsState.setStatus("mandatory")
_CooOptionsLeaseInformationIndexReference_Type = DellUnsigned32BitRange
_CooOptionsLeaseInformationIndexReference_Object = MibTableColumn
cooOptionsLeaseInformationIndexReference = _CooOptionsLeaseInformationIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 4),
    _CooOptionsLeaseInformationIndexReference_Type()
)
cooOptionsLeaseInformationIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionsLeaseInformationIndexReference.setStatus("mandatory")
_CooOptionsDescriptionName_Type = DellCostofOwnershipString
_CooOptionsDescriptionName_Object = MibTableColumn
cooOptionsDescriptionName = _CooOptionsDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 5),
    _CooOptionsDescriptionName_Type()
)
cooOptionsDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionsDescriptionName.setStatus("mandatory")
_CooMaintenanceTable_Object = MibTable
cooMaintenanceTable = _CooMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80)
)
if mibBuilder.loadTexts:
    cooMaintenanceTable.setStatus("mandatory")
_CooMaintenanceTableEntry_Object = MibTableRow
cooMaintenanceTableEntry = _CooMaintenanceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1)
)
cooMaintenanceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooMaintenancechassisIndex"),
    (0, "MIB-Dell-10892", "cooMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    cooMaintenanceTableEntry.setStatus("mandatory")
_CooMaintenancechassisIndex_Type = DellObjectRange
_CooMaintenancechassisIndex_Object = MibTableColumn
cooMaintenancechassisIndex = _CooMaintenancechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 1),
    _CooMaintenancechassisIndex_Type()
)
cooMaintenancechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenancechassisIndex.setStatus("mandatory")
_CooMaintenanceIndex_Type = DellObjectRange
_CooMaintenanceIndex_Object = MibTableColumn
cooMaintenanceIndex = _CooMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 2),
    _CooMaintenanceIndex_Type()
)
cooMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceIndex.setStatus("mandatory")
_CooMaintenanceState_Type = DellStateSettings
_CooMaintenanceState_Object = MibTableColumn
cooMaintenanceState = _CooMaintenanceState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 3),
    _CooMaintenanceState_Type()
)
cooMaintenanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceState.setStatus("mandatory")
_CooMaintenanceStartDateName_Type = DellDateName
_CooMaintenanceStartDateName_Object = MibTableColumn
cooMaintenanceStartDateName = _CooMaintenanceStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 4),
    _CooMaintenanceStartDateName_Type()
)
cooMaintenanceStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceStartDateName.setStatus("mandatory")
_CooMaintenanceEndDateName_Type = DellDateName
_CooMaintenanceEndDateName_Object = MibTableColumn
cooMaintenanceEndDateName = _CooMaintenanceEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 5),
    _CooMaintenanceEndDateName_Type()
)
cooMaintenanceEndDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceEndDateName.setStatus("mandatory")
_CooMaintenanceProviderName_Type = DellCostofOwnershipString
_CooMaintenanceProviderName_Object = MibTableColumn
cooMaintenanceProviderName = _CooMaintenanceProviderName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 6),
    _CooMaintenanceProviderName_Type()
)
cooMaintenanceProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceProviderName.setStatus("mandatory")
_CooMaintenanceRestrictionsName_Type = DellCostofOwnershipString
_CooMaintenanceRestrictionsName_Object = MibTableColumn
cooMaintenanceRestrictionsName = _CooMaintenanceRestrictionsName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 7),
    _CooMaintenanceRestrictionsName_Type()
)
cooMaintenanceRestrictionsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceRestrictionsName.setStatus("mandatory")
_CooRepairTable_Object = MibTable
cooRepairTable = _CooRepairTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90)
)
if mibBuilder.loadTexts:
    cooRepairTable.setStatus("mandatory")
_CooRepairTableEntry_Object = MibTableRow
cooRepairTableEntry = _CooRepairTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1)
)
cooRepairTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooRepairchassisIndex"),
    (0, "MIB-Dell-10892", "cooRepairIndex"),
)
if mibBuilder.loadTexts:
    cooRepairTableEntry.setStatus("mandatory")
_CooRepairchassisIndex_Type = DellObjectRange
_CooRepairchassisIndex_Object = MibTableColumn
cooRepairchassisIndex = _CooRepairchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 1),
    _CooRepairchassisIndex_Type()
)
cooRepairchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairchassisIndex.setStatus("mandatory")
_CooRepairIndex_Type = DellObjectRange
_CooRepairIndex_Object = MibTableColumn
cooRepairIndex = _CooRepairIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 2),
    _CooRepairIndex_Type()
)
cooRepairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairIndex.setStatus("mandatory")
_CooRepairState_Type = DellStateSettings
_CooRepairState_Object = MibTableColumn
cooRepairState = _CooRepairState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 3),
    _CooRepairState_Type()
)
cooRepairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairState.setStatus("mandatory")
_CooRepairCounter_Type = DellUnsigned32BitRange
_CooRepairCounter_Object = MibTableColumn
cooRepairCounter = _CooRepairCounter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 4),
    _CooRepairCounter_Type()
)
cooRepairCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairCounter.setStatus("mandatory")
_CooRepairVendorName_Type = DellCostofOwnershipString
_CooRepairVendorName_Object = MibTableColumn
cooRepairVendorName = _CooRepairVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 5),
    _CooRepairVendorName_Type()
)
cooRepairVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairVendorName.setStatus("mandatory")
_CooSupportInformationTable_Object = MibTable
cooSupportInformationTable = _CooSupportInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100)
)
if mibBuilder.loadTexts:
    cooSupportInformationTable.setStatus("mandatory")
_CooSupportInformationTableEntry_Object = MibTableRow
cooSupportInformationTableEntry = _CooSupportInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1)
)
cooSupportInformationTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooSupportInformationchassisIndex"),
    (0, "MIB-Dell-10892", "cooSupportInformationIndex"),
)
if mibBuilder.loadTexts:
    cooSupportInformationTableEntry.setStatus("mandatory")
_CooSupportInformationchassisIndex_Type = DellObjectRange
_CooSupportInformationchassisIndex_Object = MibTableColumn
cooSupportInformationchassisIndex = _CooSupportInformationchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 1),
    _CooSupportInformationchassisIndex_Type()
)
cooSupportInformationchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationchassisIndex.setStatus("mandatory")
_CooSupportInformationIndex_Type = DellObjectRange
_CooSupportInformationIndex_Object = MibTableColumn
cooSupportInformationIndex = _CooSupportInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 2),
    _CooSupportInformationIndex_Type()
)
cooSupportInformationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationIndex.setStatus("mandatory")
_CooSupportInformationState_Type = DellStateSettings
_CooSupportInformationState_Object = MibTableColumn
cooSupportInformationState = _CooSupportInformationState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 3),
    _CooSupportInformationState_Type()
)
cooSupportInformationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationState.setStatus("mandatory")
_CooSupportInformationIsOutsourced_Type = DellBoolean
_CooSupportInformationIsOutsourced_Object = MibTableColumn
cooSupportInformationIsOutsourced = _CooSupportInformationIsOutsourced_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 4),
    _CooSupportInformationIsOutsourced_Type()
)
cooSupportInformationIsOutsourced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationIsOutsourced.setStatus("mandatory")
_CooSupportInformationType_Type = DellUnsigned32BitRange
_CooSupportInformationType_Object = MibTableColumn
cooSupportInformationType = _CooSupportInformationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 5),
    _CooSupportInformationType_Type()
)
cooSupportInformationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationType.setStatus("mandatory")
_CooSupportInformationHelpDeskName_Type = DellCostofOwnershipString
_CooSupportInformationHelpDeskName_Object = MibTableColumn
cooSupportInformationHelpDeskName = _CooSupportInformationHelpDeskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 6),
    _CooSupportInformationHelpDeskName_Type()
)
cooSupportInformationHelpDeskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationHelpDeskName.setStatus("mandatory")
_CooSupportInformationFixTypeName_Type = DellCostofOwnershipString
_CooSupportInformationFixTypeName_Object = MibTableColumn
cooSupportInformationFixTypeName = _CooSupportInformationFixTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 7),
    _CooSupportInformationFixTypeName_Type()
)
cooSupportInformationFixTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationFixTypeName.setStatus("mandatory")
_CooTroubleTicketTable_Object = MibTable
cooTroubleTicketTable = _CooTroubleTicketTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110)
)
if mibBuilder.loadTexts:
    cooTroubleTicketTable.setStatus("mandatory")
_CooTroubleTicketTableEntry_Object = MibTableRow
cooTroubleTicketTableEntry = _CooTroubleTicketTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1)
)
cooTroubleTicketTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooTroubleTicketchassisIndex"),
    (0, "MIB-Dell-10892", "cooTroubleTicketIndex"),
)
if mibBuilder.loadTexts:
    cooTroubleTicketTableEntry.setStatus("mandatory")
_CooTroubleTicketchassisIndex_Type = DellObjectRange
_CooTroubleTicketchassisIndex_Object = MibTableColumn
cooTroubleTicketchassisIndex = _CooTroubleTicketchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 1),
    _CooTroubleTicketchassisIndex_Type()
)
cooTroubleTicketchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketchassisIndex.setStatus("mandatory")
_CooTroubleTicketIndex_Type = DellObjectRange
_CooTroubleTicketIndex_Object = MibTableColumn
cooTroubleTicketIndex = _CooTroubleTicketIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 2),
    _CooTroubleTicketIndex_Type()
)
cooTroubleTicketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketIndex.setStatus("mandatory")
_CooTroubleTicketState_Type = DellStateSettings
_CooTroubleTicketState_Object = MibTableColumn
cooTroubleTicketState = _CooTroubleTicketState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 3),
    _CooTroubleTicketState_Type()
)
cooTroubleTicketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketState.setStatus("mandatory")
_CooTroubleTicketSupportInformationIndexReference_Type = DellUnsigned32BitRange
_CooTroubleTicketSupportInformationIndexReference_Object = MibTableColumn
cooTroubleTicketSupportInformationIndexReference = _CooTroubleTicketSupportInformationIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 4),
    _CooTroubleTicketSupportInformationIndexReference_Type()
)
cooTroubleTicketSupportInformationIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketSupportInformationIndexReference.setStatus("mandatory")
_CooTroubleTicketNumberName_Type = DellCostofOwnershipString
_CooTroubleTicketNumberName_Object = MibTableColumn
cooTroubleTicketNumberName = _CooTroubleTicketNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 5),
    _CooTroubleTicketNumberName_Type()
)
cooTroubleTicketNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketNumberName.setStatus("mandatory")
_ClusterGroup_ObjectIdentity = ObjectIdentity
clusterGroup = _ClusterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800)
)
_ClusterTable_Object = MibTable
clusterTable = _ClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10)
)
if mibBuilder.loadTexts:
    clusterTable.setStatus("mandatory")
_ClusterTableEntry_Object = MibTableRow
clusterTableEntry = _ClusterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1)
)
clusterTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "clusterChassisIndex"),
    (0, "MIB-Dell-10892", "clusterIndex"),
)
if mibBuilder.loadTexts:
    clusterTableEntry.setStatus("mandatory")
_ClusterChassisIndex_Type = DellObjectRange
_ClusterChassisIndex_Object = MibTableColumn
clusterChassisIndex = _ClusterChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 1),
    _ClusterChassisIndex_Type()
)
clusterChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterChassisIndex.setStatus("mandatory")
_ClusterIndex_Type = DellObjectRange
_ClusterIndex_Object = MibTableColumn
clusterIndex = _ClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 2),
    _ClusterIndex_Type()
)
clusterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIndex.setStatus("mandatory")
_ClusterStateCapabilities_Type = DellStateCapabilities
_ClusterStateCapabilities_Object = MibTableColumn
clusterStateCapabilities = _ClusterStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 3),
    _ClusterStateCapabilities_Type()
)
clusterStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStateCapabilities.setStatus("mandatory")
_ClusterStateSettings_Type = DellStateSettings
_ClusterStateSettings_Object = MibTableColumn
clusterStateSettings = _ClusterStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 4),
    _ClusterStateSettings_Type()
)
clusterStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStateSettings.setStatus("mandatory")
_ClusterStatus_Type = DellStatus
_ClusterStatus_Object = MibTableColumn
clusterStatus = _ClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 5),
    _ClusterStatus_Type()
)
clusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatus.setStatus("mandatory")
_ClusterType_Type = DellClusterType
_ClusterType_Object = MibTableColumn
clusterType = _ClusterType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 6),
    _ClusterType_Type()
)
clusterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterType.setStatus("mandatory")
_ClusterTypeDescriptionName_Type = DellString
_ClusterTypeDescriptionName_Object = MibTableColumn
clusterTypeDescriptionName = _ClusterTypeDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 7),
    _ClusterTypeDescriptionName_Type()
)
clusterTypeDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterTypeDescriptionName.setStatus("mandatory")
_ClusterName_Type = DellString
_ClusterName_Object = MibTableColumn
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1800, 10, 1, 8),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("mandatory")
_BmcGroup_ObjectIdentity = ObjectIdentity
bmcGroup = _BmcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900)
)
_BmcTable_Object = MibTable
bmcTable = _BmcTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10)
)
if mibBuilder.loadTexts:
    bmcTable.setStatus("mandatory")
_BmcTableEntry_Object = MibTableRow
bmcTableEntry = _BmcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1)
)
bmcTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "bmcChassisIndex"),
    (0, "MIB-Dell-10892", "bmcIndex"),
)
if mibBuilder.loadTexts:
    bmcTableEntry.setStatus("mandatory")
_BmcChassisIndex_Type = DellObjectRange
_BmcChassisIndex_Object = MibTableColumn
bmcChassisIndex = _BmcChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 1),
    _BmcChassisIndex_Type()
)
bmcChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcChassisIndex.setStatus("mandatory")
_BmcIndex_Type = DellObjectRange
_BmcIndex_Object = MibTableColumn
bmcIndex = _BmcIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 2),
    _BmcIndex_Type()
)
bmcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcIndex.setStatus("mandatory")
_BmcStateCapabilities_Type = DellStateCapabilities
_BmcStateCapabilities_Object = MibTableColumn
bmcStateCapabilities = _BmcStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 3),
    _BmcStateCapabilities_Type()
)
bmcStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcStateCapabilities.setStatus("mandatory")
_BmcStateSettings_Type = DellStateSettings
_BmcStateSettings_Object = MibTableColumn
bmcStateSettings = _BmcStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 4),
    _BmcStateSettings_Type()
)
bmcStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcStateSettings.setStatus("mandatory")
_BmcStatus_Type = DellStatus
_BmcStatus_Object = MibTableColumn
bmcStatus = _BmcStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 5),
    _BmcStatus_Type()
)
bmcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcStatus.setStatus("mandatory")
_BmcDisplayName_Type = DellString
_BmcDisplayName_Object = MibTableColumn
bmcDisplayName = _BmcDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 6),
    _BmcDisplayName_Type()
)
bmcDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcDisplayName.setStatus("mandatory")


class _BmcDescriptionName_Type(DisplayString):
    """Custom type bmcDescriptionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BmcDescriptionName_Type.__name__ = "DisplayString"
_BmcDescriptionName_Object = MibTableColumn
bmcDescriptionName = _BmcDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 7),
    _BmcDescriptionName_Type()
)
bmcDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcDescriptionName.setStatus("mandatory")
_BmcIPMIVersionName_Type = DellString
_BmcIPMIVersionName_Object = MibTableColumn
bmcIPMIVersionName = _BmcIPMIVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 8),
    _BmcIPMIVersionName_Type()
)
bmcIPMIVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcIPMIVersionName.setStatus("mandatory")


class _BmcGUID_Type(OctetString):
    """Custom type bmcGUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_BmcGUID_Type.__name__ = "OctetString"
_BmcGUID_Object = MibTableColumn
bmcGUID = _BmcGUID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 9),
    _BmcGUID_Type()
)
bmcGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcGUID.setStatus("mandatory")
_BmcType_Type = DellManagementControllerType
_BmcType_Object = MibTableColumn
bmcType = _BmcType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 10),
    _BmcType_Type()
)
bmcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcType.setStatus("mandatory")
_BmcModuleName_Type = DellString
_BmcModuleName_Object = MibTableColumn
bmcModuleName = _BmcModuleName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 11),
    _BmcModuleName_Type()
)
bmcModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcModuleName.setStatus("mandatory")


class _BmcIPv4URLName_Type(DisplayString):
    """Custom type bmcIPv4URLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_BmcIPv4URLName_Type.__name__ = "DisplayString"
_BmcIPv4URLName_Object = MibTableColumn
bmcIPv4URLName = _BmcIPv4URLName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 12),
    _BmcIPv4URLName_Type()
)
bmcIPv4URLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcIPv4URLName.setStatus("mandatory")


class _BmcIPv6URLName_Type(DisplayString):
    """Custom type bmcIPv6URLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_BmcIPv6URLName_Type.__name__ = "DisplayString"
_BmcIPv6URLName_Object = MibTableColumn
bmcIPv6URLName = _BmcIPv6URLName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 13),
    _BmcIPv6URLName_Type()
)
bmcIPv6URLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcIPv6URLName.setStatus("mandatory")
_BmcBladeFormFactorName_Type = DellBladeFormFactorType
_BmcBladeFormFactorName_Object = MibTableColumn
bmcBladeFormFactorName = _BmcBladeFormFactorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 10, 1, 14),
    _BmcBladeFormFactorName_Type()
)
bmcBladeFormFactorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcBladeFormFactorName.setStatus("mandatory")
_BmcSerialInterfaceTable_Object = MibTable
bmcSerialInterfaceTable = _BmcSerialInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20)
)
if mibBuilder.loadTexts:
    bmcSerialInterfaceTable.setStatus("mandatory")
_BmcSerialInterfaceTableEntry_Object = MibTableRow
bmcSerialInterfaceTableEntry = _BmcSerialInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1)
)
bmcSerialInterfaceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "bmcSerialInterfaceChassisIndex"),
    (0, "MIB-Dell-10892", "bmcSerialInterfaceBMCIndex"),
    (0, "MIB-Dell-10892", "bmcSerialInterfaceIndex"),
)
if mibBuilder.loadTexts:
    bmcSerialInterfaceTableEntry.setStatus("mandatory")
_BmcSerialInterfaceChassisIndex_Type = DellObjectRange
_BmcSerialInterfaceChassisIndex_Object = MibTableColumn
bmcSerialInterfaceChassisIndex = _BmcSerialInterfaceChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 1),
    _BmcSerialInterfaceChassisIndex_Type()
)
bmcSerialInterfaceChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceChassisIndex.setStatus("mandatory")
_BmcSerialInterfaceBMCIndex_Type = DellObjectRange
_BmcSerialInterfaceBMCIndex_Object = MibTableColumn
bmcSerialInterfaceBMCIndex = _BmcSerialInterfaceBMCIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 2),
    _BmcSerialInterfaceBMCIndex_Type()
)
bmcSerialInterfaceBMCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceBMCIndex.setStatus("mandatory")
_BmcSerialInterfaceIndex_Type = DellObjectRange
_BmcSerialInterfaceIndex_Object = MibTableColumn
bmcSerialInterfaceIndex = _BmcSerialInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 3),
    _BmcSerialInterfaceIndex_Type()
)
bmcSerialInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceIndex.setStatus("mandatory")
_BmcSerialInterfaceStateCapabilities_Type = DellStateCapabilities
_BmcSerialInterfaceStateCapabilities_Object = MibTableColumn
bmcSerialInterfaceStateCapabilities = _BmcSerialInterfaceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 4),
    _BmcSerialInterfaceStateCapabilities_Type()
)
bmcSerialInterfaceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceStateCapabilities.setStatus("mandatory")
_BmcSerialInterfaceStateSettings_Type = DellStateSettings
_BmcSerialInterfaceStateSettings_Object = MibTableColumn
bmcSerialInterfaceStateSettings = _BmcSerialInterfaceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 5),
    _BmcSerialInterfaceStateSettings_Type()
)
bmcSerialInterfaceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceStateSettings.setStatus("mandatory")
_BmcSerialInterfaceStatus_Type = DellStatus
_BmcSerialInterfaceStatus_Object = MibTableColumn
bmcSerialInterfaceStatus = _BmcSerialInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 6),
    _BmcSerialInterfaceStatus_Type()
)
bmcSerialInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceStatus.setStatus("mandatory")
_BmcSerialInterfaceChannelNumber_Type = DellUnsigned8BitRange
_BmcSerialInterfaceChannelNumber_Object = MibTableColumn
bmcSerialInterfaceChannelNumber = _BmcSerialInterfaceChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 7),
    _BmcSerialInterfaceChannelNumber_Type()
)
bmcSerialInterfaceChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceChannelNumber.setStatus("mandatory")
_BmcSerialInterfaceConnectionModeCapabilities_Type = DellBMCSerialConnectionModeCapabilities
_BmcSerialInterfaceConnectionModeCapabilities_Object = MibTableColumn
bmcSerialInterfaceConnectionModeCapabilities = _BmcSerialInterfaceConnectionModeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 8),
    _BmcSerialInterfaceConnectionModeCapabilities_Type()
)
bmcSerialInterfaceConnectionModeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceConnectionModeCapabilities.setStatus("mandatory")
_BmcSerialInterfaceConnectionModeSettings_Type = DellBMCSerialConnectionModeSettings
_BmcSerialInterfaceConnectionModeSettings_Object = MibTableColumn
bmcSerialInterfaceConnectionModeSettings = _BmcSerialInterfaceConnectionModeSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 9),
    _BmcSerialInterfaceConnectionModeSettings_Type()
)
bmcSerialInterfaceConnectionModeSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceConnectionModeSettings.setStatus("mandatory")
_BmcSerialInterfaceFlowControl_Type = DellBMCSerialFlowControlType
_BmcSerialInterfaceFlowControl_Object = MibTableColumn
bmcSerialInterfaceFlowControl = _BmcSerialInterfaceFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 10),
    _BmcSerialInterfaceFlowControl_Type()
)
bmcSerialInterfaceFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceFlowControl.setStatus("mandatory")
_BmcSerialInterfaceBitRate_Type = DellBMCSerialBitRateType
_BmcSerialInterfaceBitRate_Object = MibTableColumn
bmcSerialInterfaceBitRate = _BmcSerialInterfaceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 20, 1, 11),
    _BmcSerialInterfaceBitRate_Type()
)
bmcSerialInterfaceBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcSerialInterfaceBitRate.setStatus("mandatory")
_BmcLANInterfaceTable_Object = MibTable
bmcLANInterfaceTable = _BmcLANInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30)
)
if mibBuilder.loadTexts:
    bmcLANInterfaceTable.setStatus("mandatory")
_BmcLANInterfaceTableEntry_Object = MibTableRow
bmcLANInterfaceTableEntry = _BmcLANInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1)
)
bmcLANInterfaceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "bmcLANInterfaceChassisIndex"),
    (0, "MIB-Dell-10892", "bmcLANInterfaceBMCIndex"),
    (0, "MIB-Dell-10892", "bmcLANInterfaceIndex"),
)
if mibBuilder.loadTexts:
    bmcLANInterfaceTableEntry.setStatus("mandatory")
_BmcLANInterfaceChassisIndex_Type = DellObjectRange
_BmcLANInterfaceChassisIndex_Object = MibTableColumn
bmcLANInterfaceChassisIndex = _BmcLANInterfaceChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 1),
    _BmcLANInterfaceChassisIndex_Type()
)
bmcLANInterfaceChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceChassisIndex.setStatus("mandatory")
_BmcLANInterfaceBMCIndex_Type = DellObjectRange
_BmcLANInterfaceBMCIndex_Object = MibTableColumn
bmcLANInterfaceBMCIndex = _BmcLANInterfaceBMCIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 2),
    _BmcLANInterfaceBMCIndex_Type()
)
bmcLANInterfaceBMCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceBMCIndex.setStatus("mandatory")
_BmcLANInterfaceIndex_Type = DellObjectRange
_BmcLANInterfaceIndex_Object = MibTableColumn
bmcLANInterfaceIndex = _BmcLANInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 3),
    _BmcLANInterfaceIndex_Type()
)
bmcLANInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceIndex.setStatus("mandatory")
_BmcLANInterfaceStateCapabilities_Type = DellStateCapabilities
_BmcLANInterfaceStateCapabilities_Object = MibTableColumn
bmcLANInterfaceStateCapabilities = _BmcLANInterfaceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 4),
    _BmcLANInterfaceStateCapabilities_Type()
)
bmcLANInterfaceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceStateCapabilities.setStatus("mandatory")
_BmcLANInterfaceStateSettings_Type = DellStateSettings
_BmcLANInterfaceStateSettings_Object = MibTableColumn
bmcLANInterfaceStateSettings = _BmcLANInterfaceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 5),
    _BmcLANInterfaceStateSettings_Type()
)
bmcLANInterfaceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceStateSettings.setStatus("mandatory")
_BmcLANInterfaceStatus_Type = DellStatus
_BmcLANInterfaceStatus_Object = MibTableColumn
bmcLANInterfaceStatus = _BmcLANInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 6),
    _BmcLANInterfaceStatus_Type()
)
bmcLANInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceStatus.setStatus("mandatory")
_BmcLANInterfaceChannelNumber_Type = DellUnsigned8BitRange
_BmcLANInterfaceChannelNumber_Object = MibTableColumn
bmcLANInterfaceChannelNumber = _BmcLANInterfaceChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 7),
    _BmcLANInterfaceChannelNumber_Type()
)
bmcLANInterfaceChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceChannelNumber.setStatus("mandatory")
_BmcLANInterfaceIPAddressSource_Type = DellBMCLANIPAddressSourceType
_BmcLANInterfaceIPAddressSource_Object = MibTableColumn
bmcLANInterfaceIPAddressSource = _BmcLANInterfaceIPAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 8),
    _BmcLANInterfaceIPAddressSource_Type()
)
bmcLANInterfaceIPAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceIPAddressSource.setStatus("mandatory")
_BmcLANInterfaceIPAddress_Type = IpAddress
_BmcLANInterfaceIPAddress_Object = MibTableColumn
bmcLANInterfaceIPAddress = _BmcLANInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 9),
    _BmcLANInterfaceIPAddress_Type()
)
bmcLANInterfaceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceIPAddress.setStatus("mandatory")
_BmcLANInterfaceSubnetMaskAddress_Type = IpAddress
_BmcLANInterfaceSubnetMaskAddress_Object = MibTableColumn
bmcLANInterfaceSubnetMaskAddress = _BmcLANInterfaceSubnetMaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 10),
    _BmcLANInterfaceSubnetMaskAddress_Type()
)
bmcLANInterfaceSubnetMaskAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceSubnetMaskAddress.setStatus("mandatory")
_BmcLANInterfaceDefaultGatewayAddress_Type = IpAddress
_BmcLANInterfaceDefaultGatewayAddress_Object = MibTableColumn
bmcLANInterfaceDefaultGatewayAddress = _BmcLANInterfaceDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 11),
    _BmcLANInterfaceDefaultGatewayAddress_Type()
)
bmcLANInterfaceDefaultGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceDefaultGatewayAddress.setStatus("mandatory")
_BmcLANInterfaceMACAddress_Type = DellMACAddress
_BmcLANInterfaceMACAddress_Object = MibTableColumn
bmcLANInterfaceMACAddress = _BmcLANInterfaceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 12),
    _BmcLANInterfaceMACAddress_Type()
)
bmcLANInterfaceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceMACAddress.setStatus("mandatory")


class _BmcLANInterfaceAlertCommunityName_Type(DisplayString):
    """Custom type bmcLANInterfaceAlertCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BmcLANInterfaceAlertCommunityName_Type.__name__ = "DisplayString"
_BmcLANInterfaceAlertCommunityName_Object = MibTableColumn
bmcLANInterfaceAlertCommunityName = _BmcLANInterfaceAlertCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1900, 30, 1, 13),
    _BmcLANInterfaceAlertCommunityName_Type()
)
bmcLANInterfaceAlertCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcLANInterfaceAlertCommunityName.setStatus("mandatory")
_AlertGroup_ObjectIdentity = ObjectIdentity
alertGroup = _AlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000)
)
_AlertVariables_ObjectIdentity = ObjectIdentity
alertVariables = _AlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10)
)


class _AlertSystem_Type(DisplayString):
    """Custom type alertSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertSystem_Type.__name__ = "DisplayString"
_AlertSystem_Object = MibScalar
alertSystem = _AlertSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 1),
    _AlertSystem_Type()
)
alertSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSystem.setStatus("mandatory")
_AlertTableIndexOID_Type = ObjectIdentifier
_AlertTableIndexOID_Object = MibScalar
alertTableIndexOID = _AlertTableIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 2),
    _AlertTableIndexOID_Type()
)
alertTableIndexOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertTableIndexOID.setStatus("mandatory")


class _AlertMessage_Type(DisplayString):
    """Custom type alertMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertMessage_Type.__name__ = "DisplayString"
_AlertMessage_Object = MibScalar
alertMessage = _AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 3),
    _AlertMessage_Type()
)
alertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMessage.setStatus("mandatory")
_AlertCurrentStatus_Type = DellStatus
_AlertCurrentStatus_Object = MibScalar
alertCurrentStatus = _AlertCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 4),
    _AlertCurrentStatus_Type()
)
alertCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertCurrentStatus.setStatus("mandatory")
_AlertPreviousStatus_Type = DellStatus
_AlertPreviousStatus_Object = MibScalar
alertPreviousStatus = _AlertPreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 5),
    _AlertPreviousStatus_Type()
)
alertPreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertPreviousStatus.setStatus("mandatory")


class _AlertData_Type(OctetString):
    """Custom type alertData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertData_Type.__name__ = "OctetString"
_AlertData_Object = MibScalar
alertData = _AlertData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 6),
    _AlertData_Type()
)
alertData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertData.setStatus("mandatory")


class _AlertMsgID_Type(DisplayString):
    """Custom type alertMsgID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertMsgID_Type.__name__ = "DisplayString"
_AlertMsgID_Object = MibScalar
alertMsgID = _AlertMsgID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 7),
    _AlertMsgID_Type()
)
alertMsgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMsgID.setStatus("mandatory")


class _AlertSystemFQDN_Type(DisplayString):
    """Custom type alertSystemFQDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertSystemFQDN_Type.__name__ = "DisplayString"
_AlertSystemFQDN_Object = MibScalar
alertSystemFQDN = _AlertSystemFQDN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 8),
    _AlertSystemFQDN_Type()
)
alertSystemFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSystemFQDN.setStatus("mandatory")


class _AlertServiceTag_Type(DisplayString):
    """Custom type alertServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertServiceTag_Type.__name__ = "DisplayString"
_AlertServiceTag_Object = MibScalar
alertServiceTag = _AlertServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 9),
    _AlertServiceTag_Type()
)
alertServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertServiceTag.setStatus("mandatory")


class _AlertChassisServiceTag_Type(DisplayString):
    """Custom type alertChassisServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertChassisServiceTag_Type.__name__ = "DisplayString"
_AlertChassisServiceTag_Object = MibScalar
alertChassisServiceTag = _AlertChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 10),
    _AlertChassisServiceTag_Type()
)
alertChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertChassisServiceTag.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alertSystemHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1)
)
alertSystemHeartBeat.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertSystemHeartBeat.setStatus(
        ""
    )

alertSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1001)
)
alertSystemUp.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertSystemUp.setStatus(
        ""
    )

alertThermalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1004)
)
alertThermalShutdown.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertThermalShutdown.setStatus(
        ""
    )

alertAutomaticSystemRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1006)
)
alertAutomaticSystemRecovery.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAutomaticSystemRecovery.setStatus(
        ""
    )

alertUserHostSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1007)
)
alertUserHostSystemReset.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertUserHostSystemReset.setStatus(
        ""
    )

alertSystemPeakPowerNewPeak = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1013)
)
alertSystemPeakPowerNewPeak.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertSystemPeakPowerNewPeak.setStatus(
        ""
    )

alertSystemSoftwareEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1014)
)
alertSystemSoftwareEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertSystemSoftwareEvent.setStatus(
        ""
    )

alertUnMonitoredSensorInfoEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1018)
)
alertUnMonitoredSensorInfoEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertUnMonitoredSensorInfoEvent.setStatus(
        ""
    )

alertUnMonitoredSensorWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1019)
)
alertUnMonitoredSensorWarningEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertUnMonitoredSensorWarningEvent.setStatus(
        ""
    )

alertUnMonitoredSensorCriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1020)
)
alertUnMonitoredSensorCriticalEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertUnMonitoredSensorCriticalEvent.setStatus(
        ""
    )

alertTemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1052)
)
alertTemperatureProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeNormal.setStatus(
        ""
    )

alertTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1053)
)
alertTemperatureProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeWarning.setStatus(
        ""
    )

alertTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1054)
)
alertTemperatureProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeFailure.setStatus(
        ""
    )

alertTemperatureProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1055)
)
alertTemperatureProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeNonRecoverable.setStatus(
        ""
    )

alertCoolingDeviceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1102)
)
alertCoolingDeviceNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceNormal.setStatus(
        ""
    )

alertCoolingDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1103)
)
alertCoolingDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceWarning.setStatus(
        ""
    )

alertCoolingDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1104)
)
alertCoolingDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceFailure.setStatus(
        ""
    )

alertCoolingDeviceNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1105)
)
alertCoolingDeviceNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceNonRecoverable.setStatus(
        ""
    )

alertVoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1152)
)
alertVoltageProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeNormal.setStatus(
        ""
    )

alertVoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1153)
)
alertVoltageProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeWarning.setStatus(
        ""
    )

alertVoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1154)
)
alertVoltageProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeFailure.setStatus(
        ""
    )

alertVoltageProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1155)
)
alertVoltageProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeNonRecoverable.setStatus(
        ""
    )

alertAmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1202)
)
alertAmperageProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeNormal.setStatus(
        ""
    )

alertAmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1203)
)
alertAmperageProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeWarning.setStatus(
        ""
    )

alertAmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1204)
)
alertAmperageProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeFailure.setStatus(
        ""
    )

alertAmperageProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1205)
)
alertAmperageProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeNonRecoverable.setStatus(
        ""
    )

alertChassisIntrusionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1252)
)
alertChassisIntrusionNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertChassisIntrusionNormal.setStatus(
        ""
    )

alertChassisIntrusionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1254)
)
alertChassisIntrusionDetected.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertChassisIntrusionDetected.setStatus(
        ""
    )

alertDriveBayIntrusionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1258)
)
alertDriveBayIntrusionNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertDriveBayIntrusionNormal.setStatus(
        ""
    )

alertDriveBayIntrusionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1259)
)
alertDriveBayIntrusionDetected.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertDriveBayIntrusionDetected.setStatus(
        ""
    )

alertDriveBayIntrusionDetectedExtended = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1261)
)
alertDriveBayIntrusionDetectedExtended.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertDriveBayIntrusionDetectedExtended.setStatus(
        ""
    )

alertRedundancyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1304)
)
alertRedundancyNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertRedundancyNormal.setStatus(
        ""
    )

alertRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1305)
)
alertRedundancyDegraded.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertRedundancyDegraded.setStatus(
        ""
    )

alertRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1306)
)
alertRedundancyLost.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertRedundancyLost.setStatus(
        ""
    )

alertPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1352)
)
alertPowerSupplyNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyNormal.setStatus(
        ""
    )

alertPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1353)
)
alertPowerSupplyWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyWarning.setStatus(
        ""
    )

alertPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1354)
)
alertPowerSupplyFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyFailure.setStatus(
        ""
    )

alertMemoryDeviceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1402)
)
alertMemoryDeviceNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNormal.setStatus(
        ""
    )

alertMemoryDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1403)
)
alertMemoryDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceWarning.setStatus(
        ""
    )

alertMemoryDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1404)
)
alertMemoryDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceFailure.setStatus(
        ""
    )

alertMemoryDeviceNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1405)
)
alertMemoryDeviceNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNonRecoverable.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMPersistencyRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1425)
)
alertMemoryDeviceNVDIMMPersistencyRestored.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMPersistencyRestored.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1426)
)
alertMemoryDeviceNVDIMMWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMWarning.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1427)
)
alertMemoryDeviceNVDIMMNotReady.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMNotReady.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMSaveError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1428)
)
alertMemoryDeviceNVDIMMSaveError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMSaveError.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMRestoreError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1429)
)
alertMemoryDeviceNVDIMMRestoreError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMRestoreError.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMConfigErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1430)
)
alertMemoryDeviceNVDIMMConfigErr.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMConfigErr.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1431)
)
alertMemoryDeviceNVDIMMNotResponding.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMNotResponding.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMArmFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1432)
)
alertMemoryDeviceNVDIMMArmFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMArmFailure.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMWriteProtectMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1433)
)
alertMemoryDeviceNVDIMMWriteProtectMode.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMWriteProtectMode.setStatus(
        ""
    )

alertMemoryDeviceNVMLifetimeExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1434)
)
alertMemoryDeviceNVMLifetimeExpired.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVMLifetimeExpired.setStatus(
        ""
    )

alertMemoryDeviceNVDIMMPersistencyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1435)
)
alertMemoryDeviceNVDIMMPersistencyLost.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNVDIMMPersistencyLost.setStatus(
        ""
    )

alertMemoryDeviceAEPWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1436)
)
alertMemoryDeviceAEPWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceAEPWarning.setStatus(
        ""
    )

alertMemoryDeviceAEPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1437)
)
alertMemoryDeviceAEPError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceAEPError.setStatus(
        ""
    )

alertMemoryDeviceAEPInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1438)
)
alertMemoryDeviceAEPInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceAEPInfo.setStatus(
        ""
    )

alertMemorySelfhealInitiate = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1439)
)
alertMemorySelfhealInitiate.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemorySelfhealInitiate.setStatus(
        ""
    )

alertMemoryDevicePPRSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1440)
)
alertMemoryDevicePPRSuccess.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDevicePPRSuccess.setStatus(
        ""
    )

alertMemoryDevicePPRFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1441)
)
alertMemoryDevicePPRFail.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDevicePPRFail.setStatus(
        ""
    )

alertFanEnclosureInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1452)
)
alertFanEnclosureInsertion.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertFanEnclosureInsertion.setStatus(
        ""
    )

alertFanEnclosureRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1453)
)
alertFanEnclosureRemoval.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertFanEnclosureRemoval.setStatus(
        ""
    )

alertFanEnclosureExtendedRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1454)
)
alertFanEnclosureExtendedRemoval.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertFanEnclosureExtendedRemoval.setStatus(
        ""
    )

alertACPowerCordNoPowerNonRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1501)
)
alertACPowerCordNoPowerNonRedundant.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertACPowerCordNoPowerNonRedundant.setStatus(
        ""
    )

alertACPowerCordNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1502)
)
alertACPowerCordNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertACPowerCordNormal.setStatus(
        ""
    )

alertACPowerCordFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1504)
)
alertACPowerCordFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertACPowerCordFailure.setStatus(
        ""
    )

alertLogNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1552)
)
alertLogNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertLogNormal.setStatus(
        ""
    )

alertLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1553)
)
alertLogWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertLogWarning.setStatus(
        ""
    )

alertLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1554)
)
alertLogFull.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertLogFull.setStatus(
        ""
    )

alertProcessorDeviceStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1602)
)
alertProcessorDeviceStatusNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertProcessorDeviceStatusNormal.setStatus(
        ""
    )

alertProcessorDeviceStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1603)
)
alertProcessorDeviceStatusWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertProcessorDeviceStatusWarning.setStatus(
        ""
    )

alertProcessorDeviceStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1604)
)
alertProcessorDeviceStatusFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertProcessorDeviceStatusFailure.setStatus(
        ""
    )

alertDeviceAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1651)
)
alertDeviceAdd.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertDeviceAdd.setStatus(
        ""
    )

alertDeviceRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1652)
)
alertDeviceRemove.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertDeviceRemove.setStatus(
        ""
    )

alertDeviceConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1653)
)
alertDeviceConfigError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertDeviceConfigError.setStatus(
        ""
    )

alertBatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1702)
)
alertBatteryNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertBatteryNormal.setStatus(
        ""
    )

alertBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1703)
)
alertBatteryWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertBatteryWarning.setStatus(
        ""
    )

alertBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1704)
)
alertBatteryFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertBatteryFailure.setStatus(
        ""
    )

alertBatteryAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1706)
)
alertBatteryAbsent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertBatteryAbsent.setStatus(
        ""
    )

alertSDCardDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1753)
)
alertSDCardDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertSDCardDeviceWarning.setStatus(
        ""
    )

alertSDCardDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1754)
)
alertSDCardDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertSDCardDeviceFailure.setStatus(
        ""
    )

alertMemoryOEMNoAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1801)
)
alertMemoryOEMNoAction.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMNoAction.setStatus(
        ""
    )

alertMemoryOEMCheckConfigInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1802)
)
alertMemoryOEMCheckConfigInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMCheckConfigInfo.setStatus(
        ""
    )

alertMemoryOEMReseatInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1803)
)
alertMemoryOEMReseatInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMReseatInfo.setStatus(
        ""
    )

alertMemoryOEMWarmBootInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1804)
)
alertMemoryOEMWarmBootInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMWarmBootInfo.setStatus(
        ""
    )

alertMemoryOEMColdBootInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1805)
)
alertMemoryOEMColdBootInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMColdBootInfo.setStatus(
        ""
    )

alertMemoryOEMRetryInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1806)
)
alertMemoryOEMRetryInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMRetryInfo.setStatus(
        ""
    )

alertMemoryOEMSecureEraseInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1807)
)
alertMemoryOEMSecureEraseInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMSecureEraseInfo.setStatus(
        ""
    )

alertMemoryOEMUnknownInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1808)
)
alertMemoryOEMUnknownInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMUnknownInfo.setStatus(
        ""
    )

alertMemoryOEMCheckConfigWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1809)
)
alertMemoryOEMCheckConfigWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMCheckConfigWarn.setStatus(
        ""
    )

alertMemoryOEMReseatWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1810)
)
alertMemoryOEMReseatWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMReseatWarn.setStatus(
        ""
    )

alertMemoryOEMColdBootWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1811)
)
alertMemoryOEMColdBootWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMColdBootWarn.setStatus(
        ""
    )

alertMemoryOEMContactSupportRepWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1812)
)
alertMemoryOEMContactSupportRepWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMContactSupportRepWarn.setStatus(
        ""
    )

alertMemoryOEMRetryWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1813)
)
alertMemoryOEMRetryWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMRetryWarn.setStatus(
        ""
    )

alertMemoryOEMUpdateFrmwareWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1814)
)
alertMemoryOEMUpdateFrmwareWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMUpdateFrmwareWarn.setStatus(
        ""
    )

alertMemoryOEMContactSupportImmWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1815)
)
alertMemoryOEMContactSupportImmWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMContactSupportImmWarn.setStatus(
        ""
    )

alertMemoryOEMUnknownWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1816)
)
alertMemoryOEMUnknownWarn.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMUnknownWarn.setStatus(
        ""
    )

alertMemoryOEMCheckConfigCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1817)
)
alertMemoryOEMCheckConfigCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMCheckConfigCrit.setStatus(
        ""
    )

alertMemoryOEMReseatCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1818)
)
alertMemoryOEMReseatCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMReseatCrit.setStatus(
        ""
    )

alertMemoryOEMColdBootCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1819)
)
alertMemoryOEMColdBootCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMColdBootCrit.setStatus(
        ""
    )

alertMemoryOEMRetryCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1820)
)
alertMemoryOEMRetryCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMRetryCrit.setStatus(
        ""
    )

alertMemoryOEMSantizeCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1821)
)
alertMemoryOEMSantizeCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMSantizeCrit.setStatus(
        ""
    )

alertMemoryOEMUpdateFirwareCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1822)
)
alertMemoryOEMUpdateFirwareCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMUpdateFirwareCrit.setStatus(
        ""
    )

alertMemoryOEMContactSupportImmCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1823)
)
alertMemoryOEMContactSupportImmCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMContactSupportImmCrit.setStatus(
        ""
    )

alertMemoryOEMUnknownCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1824)
)
alertMemoryOEMUnknownCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryOEMUnknownCrit.setStatus(
        ""
    )

enhancedAlertSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5001)
)
enhancedAlertSystemUp.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertSystemUp.setStatus(
        ""
    )

enhancedAlertThermalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5004)
)
enhancedAlertThermalShutdown.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertThermalShutdown.setStatus(
        ""
    )

enhancedAlertAutomaticSystemRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5006)
)
enhancedAlertAutomaticSystemRecovery.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertAutomaticSystemRecovery.setStatus(
        ""
    )

enhancedAlertUserHostSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5007)
)
enhancedAlertUserHostSystemReset.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertUserHostSystemReset.setStatus(
        ""
    )

enhancedAlertSystemPeakPowerNewPeak = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5013)
)
enhancedAlertSystemPeakPowerNewPeak.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertSystemPeakPowerNewPeak.setStatus(
        ""
    )

enhancedAlertSystemSoftwareEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5014)
)
enhancedAlertSystemSoftwareEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertSystemSoftwareEvent.setStatus(
        ""
    )

enhancedAlertUnMonitoredSensorInfoEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5015)
)
enhancedAlertUnMonitoredSensorInfoEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertUnMonitoredSensorInfoEvent.setStatus(
        ""
    )

enhancedAlertUnMonitoredSensorWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5016)
)
enhancedAlertUnMonitoredSensorWarningEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertUnMonitoredSensorWarningEvent.setStatus(
        ""
    )

enhancedAlertUnMonitoredSensorCriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5017)
)
enhancedAlertUnMonitoredSensorCriticalEvent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertUnMonitoredSensorCriticalEvent.setStatus(
        ""
    )

enhancedAlertTemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5052)
)
enhancedAlertTemperatureProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertTemperatureProbeNormal.setStatus(
        ""
    )

enhancedAlertTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5053)
)
enhancedAlertTemperatureProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertTemperatureProbeWarning.setStatus(
        ""
    )

enhancedAlertTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5054)
)
enhancedAlertTemperatureProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertTemperatureProbeFailure.setStatus(
        ""
    )

enhancedAlertTemperatureProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5055)
)
enhancedAlertTemperatureProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertTemperatureProbeNonRecoverable.setStatus(
        ""
    )

enhancedAlertCoolingDeviceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5102)
)
enhancedAlertCoolingDeviceNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertCoolingDeviceNormal.setStatus(
        ""
    )

enhancedAlertCoolingDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5103)
)
enhancedAlertCoolingDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertCoolingDeviceWarning.setStatus(
        ""
    )

enhancedAlertCoolingDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5104)
)
enhancedAlertCoolingDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertCoolingDeviceFailure.setStatus(
        ""
    )

enhancedAlertCoolingDeviceNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5105)
)
enhancedAlertCoolingDeviceNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertCoolingDeviceNonRecoverable.setStatus(
        ""
    )

enhancedAlertVoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5152)
)
enhancedAlertVoltageProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertVoltageProbeNormal.setStatus(
        ""
    )

enhancedAlertVoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5153)
)
enhancedAlertVoltageProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertVoltageProbeWarning.setStatus(
        ""
    )

enhancedAlertVoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5154)
)
enhancedAlertVoltageProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertVoltageProbeFailure.setStatus(
        ""
    )

enhancedAlertVoltageProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5155)
)
enhancedAlertVoltageProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertVoltageProbeNonRecoverable.setStatus(
        ""
    )

enhancedAlertAmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5202)
)
enhancedAlertAmperageProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertAmperageProbeNormal.setStatus(
        ""
    )

enhancedAlertAmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5203)
)
enhancedAlertAmperageProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertAmperageProbeWarning.setStatus(
        ""
    )

enhancedAlertAmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5204)
)
enhancedAlertAmperageProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertAmperageProbeFailure.setStatus(
        ""
    )

enhancedAlertAmperageProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5205)
)
enhancedAlertAmperageProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertAmperageProbeNonRecoverable.setStatus(
        ""
    )

enhancedAlertChassisIntrusionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5252)
)
enhancedAlertChassisIntrusionNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertChassisIntrusionNormal.setStatus(
        ""
    )

enhancedAlertChassisIntrusionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5254)
)
enhancedAlertChassisIntrusionDetected.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertChassisIntrusionDetected.setStatus(
        ""
    )

enhancedAlertDriveBayIntrusionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5258)
)
enhancedAlertDriveBayIntrusionNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertDriveBayIntrusionNormal.setStatus(
        ""
    )

enhancedAlertDriveBayIntrusionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5259)
)
enhancedAlertDriveBayIntrusionDetected.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertDriveBayIntrusionDetected.setStatus(
        ""
    )

enhancedAlertDriveBayIntrusionDetectedExtended = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5261)
)
enhancedAlertDriveBayIntrusionDetectedExtended.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertDriveBayIntrusionDetectedExtended.setStatus(
        ""
    )

enhancedAlertRedundancyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5304)
)
enhancedAlertRedundancyNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertRedundancyNormal.setStatus(
        ""
    )

enhancedAlertRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5305)
)
enhancedAlertRedundancyDegraded.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertRedundancyDegraded.setStatus(
        ""
    )

enhancedAlertRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5306)
)
enhancedAlertRedundancyLost.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertRedundancyLost.setStatus(
        ""
    )

enhancedAlertPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5352)
)
enhancedAlertPowerSupplyNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertPowerSupplyNormal.setStatus(
        ""
    )

enhancedAlertPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5353)
)
enhancedAlertPowerSupplyWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertPowerSupplyWarning.setStatus(
        ""
    )

enhancedAlertPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5354)
)
enhancedAlertPowerSupplyFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertPowerSupplyFailure.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5402)
)
enhancedAlertMemoryDeviceNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNormal.setStatus(
        ""
    )

enhancedAlertMemoryDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5403)
)
enhancedAlertMemoryDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceWarning.setStatus(
        ""
    )

enhancedAlertMemoryDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5404)
)
enhancedAlertMemoryDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceFailure.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5405)
)
enhancedAlertMemoryDeviceNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNonRecoverable.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMPersistencyRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5425)
)
enhancedAlertMemoryDeviceNVDIMMPersistencyRestored.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMPersistencyRestored.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5426)
)
enhancedAlertMemoryDeviceNVDIMMWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMWarning.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5427)
)
enhancedAlertMemoryDeviceNVDIMMNotReady.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMNotReady.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMSaveError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5428)
)
enhancedAlertMemoryDeviceNVDIMMSaveError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMSaveError.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMRestoreError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5429)
)
enhancedAlertMemoryDeviceNVDIMMRestoreError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMRestoreError.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMConfigErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5430)
)
enhancedAlertMemoryDeviceNVDIMMConfigErr.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMConfigErr.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5431)
)
enhancedAlertMemoryDeviceNVDIMMNotResponding.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMNotResponding.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMArmFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5432)
)
enhancedAlertMemoryDeviceNVDIMMArmFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMArmFailure.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMWriteProtectMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5433)
)
enhancedAlertMemoryDeviceNVDIMMWriteProtectMode.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMWriteProtectMode.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVMLifetimeExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5434)
)
enhancedAlertMemoryDeviceNVMLifetimeExpired.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVMLifetimeExpired.setStatus(
        ""
    )

enhancedAlertMemoryDeviceNVDIMMPersistencyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5435)
)
enhancedAlertMemoryDeviceNVDIMMPersistencyLost.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceNVDIMMPersistencyLost.setStatus(
        ""
    )

enhancedAlertMemoryDeviceAEPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5436)
)
enhancedAlertMemoryDeviceAEPError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceAEPError.setStatus(
        ""
    )

enhancedAlertMemoryDeviceAEPWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5437)
)
enhancedAlertMemoryDeviceAEPWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceAEPWarning.setStatus(
        ""
    )

enhancedAlertMemoryDeviceAEPInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5438)
)
enhancedAlertMemoryDeviceAEPInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDeviceAEPInfo.setStatus(
        ""
    )

enhancedAlertMemorySelfhealInitiate = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5439)
)
enhancedAlertMemorySelfhealInitiate.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemorySelfhealInitiate.setStatus(
        ""
    )

enhancedAlertMemoryDevicePPRSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5440)
)
enhancedAlertMemoryDevicePPRSuccess.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDevicePPRSuccess.setStatus(
        ""
    )

enhancedAlertMemoryDevicePPRFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5441)
)
enhancedAlertMemoryDevicePPRFail.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryDevicePPRFail.setStatus(
        ""
    )

enhancedAlertFanEnclosureInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5452)
)
enhancedAlertFanEnclosureInsertion.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertFanEnclosureInsertion.setStatus(
        ""
    )

enhancedAlertFanEnclosureRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5453)
)
enhancedAlertFanEnclosureRemoval.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertFanEnclosureRemoval.setStatus(
        ""
    )

enhancedAlertFanEnclosureExtendedRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5454)
)
enhancedAlertFanEnclosureExtendedRemoval.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertFanEnclosureExtendedRemoval.setStatus(
        ""
    )

enhancedAlertACPowerCordNoPowerNonRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5501)
)
enhancedAlertACPowerCordNoPowerNonRedundant.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertACPowerCordNoPowerNonRedundant.setStatus(
        ""
    )

enhancedAlertACPowerCordNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5502)
)
enhancedAlertACPowerCordNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertACPowerCordNormal.setStatus(
        ""
    )

enhancedAlertACPowerCordFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5504)
)
enhancedAlertACPowerCordFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertACPowerCordFailure.setStatus(
        ""
    )

enhancedAlertLogNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5552)
)
enhancedAlertLogNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertLogNormal.setStatus(
        ""
    )

enhancedAlertLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5553)
)
enhancedAlertLogWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertLogWarning.setStatus(
        ""
    )

enhancedAlertLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5554)
)
enhancedAlertLogFull.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertLogFull.setStatus(
        ""
    )

enhancedAlertProcessorDeviceStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5602)
)
enhancedAlertProcessorDeviceStatusNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertProcessorDeviceStatusNormal.setStatus(
        ""
    )

enhancedAlertProcessorDeviceStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5603)
)
enhancedAlertProcessorDeviceStatusWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertProcessorDeviceStatusWarning.setStatus(
        ""
    )

enhancedAlertProcessorDeviceStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5604)
)
enhancedAlertProcessorDeviceStatusFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertProcessorDeviceStatusFailure.setStatus(
        ""
    )

enhancedAlertDeviceAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5651)
)
enhancedAlertDeviceAdd.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertDeviceAdd.setStatus(
        ""
    )

enhancedAlertDeviceRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5652)
)
enhancedAlertDeviceRemove.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertDeviceRemove.setStatus(
        ""
    )

enhancedAlertDeviceConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5653)
)
enhancedAlertDeviceConfigError.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertDeviceConfigError.setStatus(
        ""
    )

enhancedAlertBatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5702)
)
enhancedAlertBatteryNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertBatteryNormal.setStatus(
        ""
    )

enhancedAlertBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5703)
)
enhancedAlertBatteryWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertBatteryWarning.setStatus(
        ""
    )

enhancedAlertBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5704)
)
enhancedAlertBatteryFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertBatteryFailure.setStatus(
        ""
    )

enhancedAlertBatteryAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5706)
)
enhancedAlertBatteryAbsent.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertBatteryAbsent.setStatus(
        ""
    )

enhancedAlertSDCardDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5753)
)
enhancedAlertSDCardDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertSDCardDeviceWarning.setStatus(
        ""
    )

enhancedAlertSDCardDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5754)
)
enhancedAlertSDCardDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertSDCardDeviceFailure.setStatus(
        ""
    )

enhancedAlertMemoryOEMNoAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5801)
)
enhancedAlertMemoryOEMNoAction.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMNoAction.setStatus(
        ""
    )

enhancedAlertMemoryOEMCheckConfigInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5802)
)
enhancedAlertMemoryOEMCheckConfigInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMCheckConfigInfo.setStatus(
        ""
    )

enhancedAlertMemoryOEMReseatInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5803)
)
enhancedAlertMemoryOEMReseatInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMReseatInfo.setStatus(
        ""
    )

enhancedAlertMemoryOEMWarmBootInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5804)
)
enhancedAlertMemoryOEMWarmBootInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMWarmBootInfo.setStatus(
        ""
    )

enhancedAlertMemoryOEMColdBootInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5805)
)
enhancedAlertMemoryOEMColdBootInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMColdBootInfo.setStatus(
        ""
    )

enhancedAlertMemoryOEMRetryInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5806)
)
enhancedAlertMemoryOEMRetryInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMRetryInfo.setStatus(
        ""
    )

enhancedAlertMemoryOEMSecureEraseInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5807)
)
enhancedAlertMemoryOEMSecureEraseInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMSecureEraseInfo.setStatus(
        ""
    )

enhancedAlertMemoryOEMUnknownInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5808)
)
enhancedAlertMemoryOEMUnknownInfo.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"),
        ("MIB-Dell-10892", "alertMsgID"),
        ("MIB-Dell-10892", "alertSystemFQDN"),
        ("MIB-Dell-10892", "alertServiceTag"),
        ("MIB-Dell-10892", "alertChassisServiceTag"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMUnknownInfo.setStatus(
        ""
    )

enhancedAlertMemomoryOEMCheckConfigWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5809)
)
enhancedAlertMemomoryOEMCheckConfigWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryOEMCheckConfigWarning.setStatus(
        ""
    )

enhancedAlertMemomoryOEMReseatWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5810)
)
enhancedAlertMemomoryOEMReseatWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryOEMReseatWarning.setStatus(
        ""
    )

enhancedAlertMemomoryOEMColdBootWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5811)
)
enhancedAlertMemomoryOEMColdBootWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryOEMColdBootWarning.setStatus(
        ""
    )

enhancedAlertMemomoryOEMContactServiceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5812)
)
enhancedAlertMemomoryOEMContactServiceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryOEMContactServiceWarning.setStatus(
        ""
    )

enhancedAlertMemomoryOEMRetryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5813)
)
enhancedAlertMemomoryOEMRetryWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryOEMRetryWarning.setStatus(
        ""
    )

enhancedAlertMemomoryOEMUpdateFirmwareWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5814)
)
enhancedAlertMemomoryOEMUpdateFirmwareWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryOEMUpdateFirmwareWarning.setStatus(
        ""
    )

enhancedAlertMemomoryContactAssistanceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5815)
)
enhancedAlertMemomoryContactAssistanceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryContactAssistanceWarning.setStatus(
        ""
    )

enhancedAlertMemomoryOEMUnknownWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5816)
)
enhancedAlertMemomoryOEMUnknownWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemomoryOEMUnknownWarning.setStatus(
        ""
    )

enhancedAlertMemoryOEMCheckConfigCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5817)
)
enhancedAlertMemoryOEMCheckConfigCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMCheckConfigCrit.setStatus(
        ""
    )

enhancedAlertMemoryOEMReseatCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5818)
)
enhancedAlertMemoryOEMReseatCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMReseatCrit.setStatus(
        ""
    )

enhancedAlertMemoryOEMColdBootCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5819)
)
enhancedAlertMemoryOEMColdBootCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMColdBootCrit.setStatus(
        ""
    )

enhancedAlertMemoryOEMRetryCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5820)
)
enhancedAlertMemoryOEMRetryCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMRetryCrit.setStatus(
        ""
    )

enhancedAlertMemoryOEMSantizeCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5821)
)
enhancedAlertMemoryOEMSantizeCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMSantizeCrit.setStatus(
        ""
    )

enhancedAlertMemoryOEMUpdateFirwareCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5822)
)
enhancedAlertMemoryOEMUpdateFirwareCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMUpdateFirwareCrit.setStatus(
        ""
    )

enhancedAlertMemoryOEMContactSupportImmCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5823)
)
enhancedAlertMemoryOEMContactSupportImmCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMContactSupportImmCrit.setStatus(
        ""
    )

enhancedAlertMemoryOEMUnknownCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 5824)
)
enhancedAlertMemoryOEMUnknownCrit.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    enhancedAlertMemoryOEMUnknownCrit.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-Dell-10892",
    **{"DellString": DellString,
       "DellSecurityString": DellSecurityString,
       "DellCostofOwnershipString": DellCostofOwnershipString,
       "DellMACAddress": DellMACAddress,
       "DellObjectRange": DellObjectRange,
       "DellUnsigned8BitRange": DellUnsigned8BitRange,
       "DellUnsigned16BitRange": DellUnsigned16BitRange,
       "DellUnsigned32BitRange": DellUnsigned32BitRange,
       "DellSigned32BitRange": DellSigned32BitRange,
       "DellBoolean": DellBoolean,
       "DellUnsigned64BitRange": DellUnsigned64BitRange,
       "DellDateName": DellDateName,
       "DellStateCapabilities": DellStateCapabilities,
       "DellStateSettings": DellStateSettings,
       "DellProbeCapabilities": DellProbeCapabilities,
       "DellStatus": DellStatus,
       "DellStatusRedundancy": DellStatusRedundancy,
       "DellStatusProbe": DellStatusProbe,
       "SMSSupportedTypes": SMSSupportedTypes,
       "SMSFeatureFlags": SMSFeatureFlags,
       "SMSSNMPAgentFeatureFlags": SMSSNMPAgentFeatureFlags,
       "DellStateCapabilitiesLogUnique": DellStateCapabilitiesLogUnique,
       "DellStateSettingsLogUnique": DellStateSettingsLogUnique,
       "DellLogFormat": DellLogFormat,
       "DellChassisType": DellChassisType,
       "DellChassisSystemClass": DellChassisSystemClass,
       "DellConnectionStatus": DellConnectionStatus,
       "DellFanControlCapabilities": DellFanControlCapabilities,
       "DellFanControlSettings": DellFanControlSettings,
       "DellLEDControlCapabilities": DellLEDControlCapabilities,
       "DellLEDControlSettings": DellLEDControlSettings,
       "DellHDFaultLEDControlCapabilities": DellHDFaultLEDControlCapabilities,
       "DellHDFaultLEDControlSettings": DellHDFaultLEDControlSettings,
       "DellChassisIdentifyControlCapabilities": DellChassisIdentifyControlCapabilities,
       "DellChassisIdentifyControlSettings": DellChassisIdentifyControlSettings,
       "DellHostControlCapabilities": DellHostControlCapabilities,
       "DellHostControlSettings": DellHostControlSettings,
       "DellWatchDogControlCapabilities": DellWatchDogControlCapabilities,
       "DellWatchControlSettings": DellWatchControlSettings,
       "DellWatchDogTimerCapabilities": DellWatchDogTimerCapabilities,
       "DellPowerButtonControlCapabilities": DellPowerButtonControlCapabilities,
       "DellPowerButtonControlSettings": DellPowerButtonControlSettings,
       "DellNMIButtonControlCapabilities": DellNMIButtonControlCapabilities,
       "DellNMIButtonControlSettings": DellNMIButtonControlSettings,
       "DellSystemProperties": DellSystemProperties,
       "DellUUIDType": DellUUIDType,
       "DellFirmwareType": DellFirmwareType,
       "DellIntrusionReading": DellIntrusionReading,
       "DellIntrusionType": DellIntrusionType,
       "DellBaseBoardType": DellBaseBoardType,
       "DellBaseBoardFeatureFlags": DellBaseBoardFeatureFlags,
       "DellSystemResourceMapType": DellSystemResourceMapType,
       "DellResourceOwnerInterfaceType": DellResourceOwnerInterfaceType,
       "DellResourceShareDisposition": DellResourceShareDisposition,
       "DellResourceMemoryFlags": DellResourceMemoryFlags,
       "DellResourceInterruptType": DellResourceInterruptType,
       "DellResourceInterruptTrigger": DellResourceInterruptTrigger,
       "DellResourceDMATransferWidth": DellResourceDMATransferWidth,
       "DellResourceDMABusMaster": DellResourceDMABusMaster,
       "DellPowerSupplyStateCapabilitiesUnique": DellPowerSupplyStateCapabilitiesUnique,
       "DellPowerSupplyStateSettingsUnique": DellPowerSupplyStateSettingsUnique,
       "DellPowerSupplyType": DellPowerSupplyType,
       "DellPowerSupplySensorState": DellPowerSupplySensorState,
       "DellPowerSupplyConfigurationErrorType": DellPowerSupplyConfigurationErrorType,
       "DellVoltageType": DellVoltageType,
       "DellVoltageDiscreteReading": DellVoltageDiscreteReading,
       "DellAmperageProbeType": DellAmperageProbeType,
       "DellAmperageDiscreteReading": DellAmperageDiscreteReading,
       "DellACPowerSwitchCapabilities": DellACPowerSwitchCapabilities,
       "DellACPowerSwitchSettings": DellACPowerSwitchSettings,
       "DellACPowerSwitchRedundancyMode": DellACPowerSwitchRedundancyMode,
       "DellACPowerCordStateCapabilities": DellACPowerCordStateCapabilities,
       "DellACPowerCordStateSettings": DellACPowerCordStateSettings,
       "DellBatteryReading": DellBatteryReading,
       "DellPowerCapCapabilities": DellPowerCapCapabilities,
       "DellPowerCapSetting": DellPowerCapSetting,
       "DellPowerProfileType": DellPowerProfileType,
       "DellCPUPowerPerformanceManagementType": DellCPUPowerPerformanceManagementType,
       "DellMemoryPowerPerformanceManagementType": DellMemoryPowerPerformanceManagementType,
       "DellFanPowerPerformanceManagementType": DellFanPowerPerformanceManagementType,
       "DellCoolingDeviceType": DellCoolingDeviceType,
       "DellCoolingDeviceSubType": DellCoolingDeviceSubType,
       "DellCoolingDeviceDiscreteReading": DellCoolingDeviceDiscreteReading,
       "DellTemperatureProbeType": DellTemperatureProbeType,
       "DellTemperatureDiscreteReading": DellTemperatureDiscreteReading,
       "DellRemoteFlashBIOSStateCapabilitiesUnique": DellRemoteFlashBIOSStateCapabilitiesUnique,
       "DellRemoteFlashBIOSStateSettingsUnique": DellRemoteFlashBIOSStateSettingsUnique,
       "DellRemoteFlashBIOSCompletionCode": DellRemoteFlashBIOSCompletionCode,
       "DellGenericPortConnectorType": DellGenericPortConnectorType,
       "DellPortSecurityState": DellPortSecurityState,
       "DellPointingPortConnectorType": DellPointingPortConnectorType,
       "DellKeyboardPortConnectorType": DellKeyboardPortConnectorType,
       "DellProcessorPortConnectorType": DellProcessorPortConnectorType,
       "DellMemoryDevicePortConnectorType": DellMemoryDevicePortConnectorType,
       "DellMonitorPortConnectorType": DellMonitorPortConnectorType,
       "DellSCSIPortConnectorType": DellSCSIPortConnectorType,
       "DellParallelPortConnectorType": DellParallelPortConnectorType,
       "DellParallelPortConnectorPinout": DellParallelPortConnectorPinout,
       "DellParallelPortCapabilitiesUnique": DellParallelPortCapabilitiesUnique,
       "DellSerialPortConnectorType": DellSerialPortConnectorType,
       "DellSerialPortCapabilitiesUnique": DellSerialPortCapabilitiesUnique,
       "DellUSBPortConnectorType": DellUSBPortConnectorType,
       "DellPointingDeviceType": DellPointingDeviceType,
       "DellProcessorDeviceType": DellProcessorDeviceType,
       "DellProcessorDeviceFamily": DellProcessorDeviceFamily,
       "DellProcessorDeviceStatusState": DellProcessorDeviceStatusState,
       "DellProcessorUpgradeInformation": DellProcessorUpgradeInformation,
       "DellProcessorDeviceStatusReading": DellProcessorDeviceStatusReading,
       "DellCacheDeviceType": DellCacheDeviceType,
       "DellCacheDeviceLevel": DellCacheDeviceLevel,
       "DellCacheDeviceWritePolicy": DellCacheDeviceWritePolicy,
       "DellCacheDeviceStatusState": DellCacheDeviceStatusState,
       "DellCacheDeviceECCType": DellCacheDeviceECCType,
       "DellCacheDeviceAssociativity": DellCacheDeviceAssociativity,
       "DellCacheDeviceLocation": DellCacheDeviceLocation,
       "DellCacheDeviceSRAMType": DellCacheDeviceSRAMType,
       "DellMemoryDeviceFormFactor": DellMemoryDeviceFormFactor,
       "DellMemoryDeviceType": DellMemoryDeviceType,
       "DellMemoryDeviceRank": DellMemoryDeviceRank,
       "DellMemoryDeviceTypeDetails": DellMemoryDeviceTypeDetails,
       "DellMemoryDeviceFailureModes": DellMemoryDeviceFailureModes,
       "DellMemoryDeviceMemoryTechnology": DellMemoryDeviceMemoryTechnology,
       "DellGenericDeviceType": DellGenericDeviceType,
       "DellNetworkDeviceConnectionStatus": DellNetworkDeviceConnectionStatus,
       "DellNetworkDeviceTeamingFlags": DellNetworkDeviceTeamingFlags,
       "DellNetworkDeviceTOECapabilityFlags": DellNetworkDeviceTOECapabilityFlags,
       "DellNetworkDeviceRDMACapabilityFlags": DellNetworkDeviceRDMACapabilityFlags,
       "DellNetworkDeviceiSCSICapabilityFlags": DellNetworkDeviceiSCSICapabilityFlags,
       "DellNetworkDeviceCapabilities": DellNetworkDeviceCapabilities,
       "DellNetworkDeviceNParEPEnabled": DellNetworkDeviceNParEPEnabled,
       "DellManagedSystemServicesDeviceType": DellManagedSystemServicesDeviceType,
       "DellSDCardDeviceType": DellSDCardDeviceType,
       "DellSDCardDeviceConfigCapabilities": DellSDCardDeviceConfigCapabilities,
       "DellSDCardDeviceConfigSettings": DellSDCardDeviceConfigSettings,
       "DellSDCardDeviceCardState": DellSDCardDeviceCardState,
       "DellSDCardDeviceCardLicensed": DellSDCardDeviceCardLicensed,
       "DellSystemSlotStateCapabilities": DellSystemSlotStateCapabilities,
       "DellSystemSlotStateSettings": DellSystemSlotStateSettings,
       "DellSystemSlotType": DellSystemSlotType,
       "DellSystemSlotUsage": DellSystemSlotUsage,
       "DellSystemSlotLength": DellSystemSlotLength,
       "DellSystemSlotCategory": DellSystemSlotCategory,
       "DellSystemSlotHotPlugBusWidth": DellSystemSlotHotPlugBusWidth,
       "DellPhysicalMemoryArrayLocation": DellPhysicalMemoryArrayLocation,
       "DellPhysicalMemoryArrayUse": DellPhysicalMemoryArrayUse,
       "DellPhysicalMemoryArrayECCType": DellPhysicalMemoryArrayECCType,
       "DellPhysicalMemoryConfigStateCapabilities": DellPhysicalMemoryConfigStateCapabilities,
       "DellPhysicalMemoryConfigStateSettings": DellPhysicalMemoryConfigStateSettings,
       "DellPhysicalMemoryConfigRedundantCapabilities": DellPhysicalMemoryConfigRedundantCapabilities,
       "DellPhysicalMemoryConfigRedundantSettings": DellPhysicalMemoryConfigRedundantSettings,
       "DellPhysicalMemoryConfigMOMCapabilities": DellPhysicalMemoryConfigMOMCapabilities,
       "DellPhysicalMemoryConfigMOMSettings": DellPhysicalMemoryConfigMOMSettings,
       "DellPhysicalMemoryLoggingCapabilities": DellPhysicalMemoryLoggingCapabilities,
       "DellPhysicalMemoryLoggingSettings": DellPhysicalMemoryLoggingSettings,
       "DellSpeakerControlCapabilitiesUnique": DellSpeakerControlCapabilitiesUnique,
       "DellSpeakerControlSettingsUnique": DellSpeakerControlSettingsUnique,
       "DellNIFwakeonLanControlCapabilitiesUnique": DellNIFwakeonLanControlCapabilitiesUnique,
       "DellNIFwakeonLanControlSettingsUnique": DellNIFwakeonLanControlSettingsUnique,
       "DellBootSequenceControlCapabilitiesUnique": DellBootSequenceControlCapabilitiesUnique,
       "DellBootSequenceControlSettingsUnique": DellBootSequenceControlSettingsUnique,
       "DellBIOSPasswordControlCapabilitiesUnique": DellBIOSPasswordControlCapabilitiesUnique,
       "DellBIOSPasswordControlSettingsUnique": DellBIOSPasswordControlSettingsUnique,
       "DellTPMSecurityControlCapabilities": DellTPMSecurityControlCapabilities,
       "DellTPMSecurityControlSetting": DellTPMSecurityControlSetting,
       "DellParallelPortControlCapabilitiesUnique": DellParallelPortControlCapabilitiesUnique,
       "DellParallelPortControlSettingsUnique": DellParallelPortControlSettingsUnique,
       "DellParallelPortControlModeCapabilitiesUnique": DellParallelPortControlModeCapabilitiesUnique,
       "DellParallelPortControlModeSettingsUnique": DellParallelPortControlModeSettingsUnique,
       "DellSerialPortControlCapabilitiesUnique": DellSerialPortControlCapabilitiesUnique,
       "DellSerialPortControlSettingsUnique": DellSerialPortControlSettingsUnique,
       "DellideControlCapabilitiesUnique": DellideControlCapabilitiesUnique,
       "DellideControlSettingsUnique": DellideControlSettingsUnique,
       "DellDisketteControlCapabilitiesUnique": DellDisketteControlCapabilitiesUnique,
       "DellDisketteControlSettingsUnique": DellDisketteControlSettingsUnique,
       "DellNetworkInterfaceControlCapabilitiesUnique": DellNetworkInterfaceControlCapabilitiesUnique,
       "DellNetworkInterfaceControlSettingsUnique": DellNetworkInterfaceControlSettingsUnique,
       "DellBIOSSettingValueType": DellBIOSSettingValueType,
       "DellLocalResponseAgentCapabilitiesUnique": DellLocalResponseAgentCapabilitiesUnique,
       "DellLRAThermalShutdownCapabilitiesUnique": DellLRAThermalShutdownCapabilitiesUnique,
       "DellLRAThermalShutdownStateSettingsUnique": DellLRAThermalShutdownStateSettingsUnique,
       "DellLocalResponseAgentSettingsUnique": DellLocalResponseAgentSettingsUnique,
       "DellCooOwnershipCodes": DellCooOwnershipCodes,
       "DellCooHourDayDurationType": DellCooHourDayDurationType,
       "DellCooDayMonthDurationType": DellCooDayMonthDurationType,
       "DellCooMonthYearDurationType": DellCooMonthYearDurationType,
       "DellClusterType": DellClusterType,
       "DellManagementControllerType": DellManagementControllerType,
       "DellBladeFormFactorType": DellBladeFormFactorType,
       "DellBMCSerialConnectionModeCapabilities": DellBMCSerialConnectionModeCapabilities,
       "DellBMCSerialConnectionModeSettings": DellBMCSerialConnectionModeSettings,
       "DellBMCSerialFlowControlType": DellBMCSerialFlowControlType,
       "DellBMCSerialBitRateType": DellBMCSerialBitRateType,
       "DellBMCLANIPAddressSourceType": DellBMCLANIPAddressSourceType,
       "dell": dell,
       "server3": server3,
       "baseboardGroup": baseboardGroup,
       "alertSystemHeartBeat": alertSystemHeartBeat,
       "alertSystemUp": alertSystemUp,
       "alertThermalShutdown": alertThermalShutdown,
       "alertAutomaticSystemRecovery": alertAutomaticSystemRecovery,
       "alertUserHostSystemReset": alertUserHostSystemReset,
       "alertSystemPeakPowerNewPeak": alertSystemPeakPowerNewPeak,
       "alertSystemSoftwareEvent": alertSystemSoftwareEvent,
       "alertUnMonitoredSensorInfoEvent": alertUnMonitoredSensorInfoEvent,
       "alertUnMonitoredSensorWarningEvent": alertUnMonitoredSensorWarningEvent,
       "alertUnMonitoredSensorCriticalEvent": alertUnMonitoredSensorCriticalEvent,
       "alertTemperatureProbeNormal": alertTemperatureProbeNormal,
       "alertTemperatureProbeWarning": alertTemperatureProbeWarning,
       "alertTemperatureProbeFailure": alertTemperatureProbeFailure,
       "alertTemperatureProbeNonRecoverable": alertTemperatureProbeNonRecoverable,
       "alertCoolingDeviceNormal": alertCoolingDeviceNormal,
       "alertCoolingDeviceWarning": alertCoolingDeviceWarning,
       "alertCoolingDeviceFailure": alertCoolingDeviceFailure,
       "alertCoolingDeviceNonRecoverable": alertCoolingDeviceNonRecoverable,
       "alertVoltageProbeNormal": alertVoltageProbeNormal,
       "alertVoltageProbeWarning": alertVoltageProbeWarning,
       "alertVoltageProbeFailure": alertVoltageProbeFailure,
       "alertVoltageProbeNonRecoverable": alertVoltageProbeNonRecoverable,
       "alertAmperageProbeNormal": alertAmperageProbeNormal,
       "alertAmperageProbeWarning": alertAmperageProbeWarning,
       "alertAmperageProbeFailure": alertAmperageProbeFailure,
       "alertAmperageProbeNonRecoverable": alertAmperageProbeNonRecoverable,
       "alertChassisIntrusionNormal": alertChassisIntrusionNormal,
       "alertChassisIntrusionDetected": alertChassisIntrusionDetected,
       "alertDriveBayIntrusionNormal": alertDriveBayIntrusionNormal,
       "alertDriveBayIntrusionDetected": alertDriveBayIntrusionDetected,
       "alertDriveBayIntrusionDetectedExtended": alertDriveBayIntrusionDetectedExtended,
       "alertRedundancyNormal": alertRedundancyNormal,
       "alertRedundancyDegraded": alertRedundancyDegraded,
       "alertRedundancyLost": alertRedundancyLost,
       "alertPowerSupplyNormal": alertPowerSupplyNormal,
       "alertPowerSupplyWarning": alertPowerSupplyWarning,
       "alertPowerSupplyFailure": alertPowerSupplyFailure,
       "alertMemoryDeviceNormal": alertMemoryDeviceNormal,
       "alertMemoryDeviceWarning": alertMemoryDeviceWarning,
       "alertMemoryDeviceFailure": alertMemoryDeviceFailure,
       "alertMemoryDeviceNonRecoverable": alertMemoryDeviceNonRecoverable,
       "alertMemoryDeviceNVDIMMPersistencyRestored": alertMemoryDeviceNVDIMMPersistencyRestored,
       "alertMemoryDeviceNVDIMMWarning": alertMemoryDeviceNVDIMMWarning,
       "alertMemoryDeviceNVDIMMNotReady": alertMemoryDeviceNVDIMMNotReady,
       "alertMemoryDeviceNVDIMMSaveError": alertMemoryDeviceNVDIMMSaveError,
       "alertMemoryDeviceNVDIMMRestoreError": alertMemoryDeviceNVDIMMRestoreError,
       "alertMemoryDeviceNVDIMMConfigErr": alertMemoryDeviceNVDIMMConfigErr,
       "alertMemoryDeviceNVDIMMNotResponding": alertMemoryDeviceNVDIMMNotResponding,
       "alertMemoryDeviceNVDIMMArmFailure": alertMemoryDeviceNVDIMMArmFailure,
       "alertMemoryDeviceNVDIMMWriteProtectMode": alertMemoryDeviceNVDIMMWriteProtectMode,
       "alertMemoryDeviceNVMLifetimeExpired": alertMemoryDeviceNVMLifetimeExpired,
       "alertMemoryDeviceNVDIMMPersistencyLost": alertMemoryDeviceNVDIMMPersistencyLost,
       "alertMemoryDeviceAEPWarning": alertMemoryDeviceAEPWarning,
       "alertMemoryDeviceAEPError": alertMemoryDeviceAEPError,
       "alertMemoryDeviceAEPInfo": alertMemoryDeviceAEPInfo,
       "alertMemorySelfhealInitiate": alertMemorySelfhealInitiate,
       "alertMemoryDevicePPRSuccess": alertMemoryDevicePPRSuccess,
       "alertMemoryDevicePPRFail": alertMemoryDevicePPRFail,
       "alertFanEnclosureInsertion": alertFanEnclosureInsertion,
       "alertFanEnclosureRemoval": alertFanEnclosureRemoval,
       "alertFanEnclosureExtendedRemoval": alertFanEnclosureExtendedRemoval,
       "alertACPowerCordNoPowerNonRedundant": alertACPowerCordNoPowerNonRedundant,
       "alertACPowerCordNormal": alertACPowerCordNormal,
       "alertACPowerCordFailure": alertACPowerCordFailure,
       "alertLogNormal": alertLogNormal,
       "alertLogWarning": alertLogWarning,
       "alertLogFull": alertLogFull,
       "alertProcessorDeviceStatusNormal": alertProcessorDeviceStatusNormal,
       "alertProcessorDeviceStatusWarning": alertProcessorDeviceStatusWarning,
       "alertProcessorDeviceStatusFailure": alertProcessorDeviceStatusFailure,
       "alertDeviceAdd": alertDeviceAdd,
       "alertDeviceRemove": alertDeviceRemove,
       "alertDeviceConfigError": alertDeviceConfigError,
       "alertBatteryNormal": alertBatteryNormal,
       "alertBatteryWarning": alertBatteryWarning,
       "alertBatteryFailure": alertBatteryFailure,
       "alertBatteryAbsent": alertBatteryAbsent,
       "alertSDCardDeviceWarning": alertSDCardDeviceWarning,
       "alertSDCardDeviceFailure": alertSDCardDeviceFailure,
       "alertMemoryOEMNoAction": alertMemoryOEMNoAction,
       "alertMemoryOEMCheckConfigInfo": alertMemoryOEMCheckConfigInfo,
       "alertMemoryOEMReseatInfo": alertMemoryOEMReseatInfo,
       "alertMemoryOEMWarmBootInfo": alertMemoryOEMWarmBootInfo,
       "alertMemoryOEMColdBootInfo": alertMemoryOEMColdBootInfo,
       "alertMemoryOEMRetryInfo": alertMemoryOEMRetryInfo,
       "alertMemoryOEMSecureEraseInfo": alertMemoryOEMSecureEraseInfo,
       "alertMemoryOEMUnknownInfo": alertMemoryOEMUnknownInfo,
       "alertMemoryOEMCheckConfigWarn": alertMemoryOEMCheckConfigWarn,
       "alertMemoryOEMReseatWarn": alertMemoryOEMReseatWarn,
       "alertMemoryOEMColdBootWarn": alertMemoryOEMColdBootWarn,
       "alertMemoryOEMContactSupportRepWarn": alertMemoryOEMContactSupportRepWarn,
       "alertMemoryOEMRetryWarn": alertMemoryOEMRetryWarn,
       "alertMemoryOEMUpdateFrmwareWarn": alertMemoryOEMUpdateFrmwareWarn,
       "alertMemoryOEMContactSupportImmWarn": alertMemoryOEMContactSupportImmWarn,
       "alertMemoryOEMUnknownWarn": alertMemoryOEMUnknownWarn,
       "alertMemoryOEMCheckConfigCrit": alertMemoryOEMCheckConfigCrit,
       "alertMemoryOEMReseatCrit": alertMemoryOEMReseatCrit,
       "alertMemoryOEMColdBootCrit": alertMemoryOEMColdBootCrit,
       "alertMemoryOEMRetryCrit": alertMemoryOEMRetryCrit,
       "alertMemoryOEMSantizeCrit": alertMemoryOEMSantizeCrit,
       "alertMemoryOEMUpdateFirwareCrit": alertMemoryOEMUpdateFirwareCrit,
       "alertMemoryOEMContactSupportImmCrit": alertMemoryOEMContactSupportImmCrit,
       "alertMemoryOEMUnknownCrit": alertMemoryOEMUnknownCrit,
       "enhancedAlertSystemUp": enhancedAlertSystemUp,
       "enhancedAlertThermalShutdown": enhancedAlertThermalShutdown,
       "enhancedAlertAutomaticSystemRecovery": enhancedAlertAutomaticSystemRecovery,
       "enhancedAlertUserHostSystemReset": enhancedAlertUserHostSystemReset,
       "enhancedAlertSystemPeakPowerNewPeak": enhancedAlertSystemPeakPowerNewPeak,
       "enhancedAlertSystemSoftwareEvent": enhancedAlertSystemSoftwareEvent,
       "enhancedAlertUnMonitoredSensorInfoEvent": enhancedAlertUnMonitoredSensorInfoEvent,
       "enhancedAlertUnMonitoredSensorWarningEvent": enhancedAlertUnMonitoredSensorWarningEvent,
       "enhancedAlertUnMonitoredSensorCriticalEvent": enhancedAlertUnMonitoredSensorCriticalEvent,
       "enhancedAlertTemperatureProbeNormal": enhancedAlertTemperatureProbeNormal,
       "enhancedAlertTemperatureProbeWarning": enhancedAlertTemperatureProbeWarning,
       "enhancedAlertTemperatureProbeFailure": enhancedAlertTemperatureProbeFailure,
       "enhancedAlertTemperatureProbeNonRecoverable": enhancedAlertTemperatureProbeNonRecoverable,
       "enhancedAlertCoolingDeviceNormal": enhancedAlertCoolingDeviceNormal,
       "enhancedAlertCoolingDeviceWarning": enhancedAlertCoolingDeviceWarning,
       "enhancedAlertCoolingDeviceFailure": enhancedAlertCoolingDeviceFailure,
       "enhancedAlertCoolingDeviceNonRecoverable": enhancedAlertCoolingDeviceNonRecoverable,
       "enhancedAlertVoltageProbeNormal": enhancedAlertVoltageProbeNormal,
       "enhancedAlertVoltageProbeWarning": enhancedAlertVoltageProbeWarning,
       "enhancedAlertVoltageProbeFailure": enhancedAlertVoltageProbeFailure,
       "enhancedAlertVoltageProbeNonRecoverable": enhancedAlertVoltageProbeNonRecoverable,
       "enhancedAlertAmperageProbeNormal": enhancedAlertAmperageProbeNormal,
       "enhancedAlertAmperageProbeWarning": enhancedAlertAmperageProbeWarning,
       "enhancedAlertAmperageProbeFailure": enhancedAlertAmperageProbeFailure,
       "enhancedAlertAmperageProbeNonRecoverable": enhancedAlertAmperageProbeNonRecoverable,
       "enhancedAlertChassisIntrusionNormal": enhancedAlertChassisIntrusionNormal,
       "enhancedAlertChassisIntrusionDetected": enhancedAlertChassisIntrusionDetected,
       "enhancedAlertDriveBayIntrusionNormal": enhancedAlertDriveBayIntrusionNormal,
       "enhancedAlertDriveBayIntrusionDetected": enhancedAlertDriveBayIntrusionDetected,
       "enhancedAlertDriveBayIntrusionDetectedExtended": enhancedAlertDriveBayIntrusionDetectedExtended,
       "enhancedAlertRedundancyNormal": enhancedAlertRedundancyNormal,
       "enhancedAlertRedundancyDegraded": enhancedAlertRedundancyDegraded,
       "enhancedAlertRedundancyLost": enhancedAlertRedundancyLost,
       "enhancedAlertPowerSupplyNormal": enhancedAlertPowerSupplyNormal,
       "enhancedAlertPowerSupplyWarning": enhancedAlertPowerSupplyWarning,
       "enhancedAlertPowerSupplyFailure": enhancedAlertPowerSupplyFailure,
       "enhancedAlertMemoryDeviceNormal": enhancedAlertMemoryDeviceNormal,
       "enhancedAlertMemoryDeviceWarning": enhancedAlertMemoryDeviceWarning,
       "enhancedAlertMemoryDeviceFailure": enhancedAlertMemoryDeviceFailure,
       "enhancedAlertMemoryDeviceNonRecoverable": enhancedAlertMemoryDeviceNonRecoverable,
       "enhancedAlertMemoryDeviceNVDIMMPersistencyRestored": enhancedAlertMemoryDeviceNVDIMMPersistencyRestored,
       "enhancedAlertMemoryDeviceNVDIMMWarning": enhancedAlertMemoryDeviceNVDIMMWarning,
       "enhancedAlertMemoryDeviceNVDIMMNotReady": enhancedAlertMemoryDeviceNVDIMMNotReady,
       "enhancedAlertMemoryDeviceNVDIMMSaveError": enhancedAlertMemoryDeviceNVDIMMSaveError,
       "enhancedAlertMemoryDeviceNVDIMMRestoreError": enhancedAlertMemoryDeviceNVDIMMRestoreError,
       "enhancedAlertMemoryDeviceNVDIMMConfigErr": enhancedAlertMemoryDeviceNVDIMMConfigErr,
       "enhancedAlertMemoryDeviceNVDIMMNotResponding": enhancedAlertMemoryDeviceNVDIMMNotResponding,
       "enhancedAlertMemoryDeviceNVDIMMArmFailure": enhancedAlertMemoryDeviceNVDIMMArmFailure,
       "enhancedAlertMemoryDeviceNVDIMMWriteProtectMode": enhancedAlertMemoryDeviceNVDIMMWriteProtectMode,
       "enhancedAlertMemoryDeviceNVMLifetimeExpired": enhancedAlertMemoryDeviceNVMLifetimeExpired,
       "enhancedAlertMemoryDeviceNVDIMMPersistencyLost": enhancedAlertMemoryDeviceNVDIMMPersistencyLost,
       "enhancedAlertMemoryDeviceAEPError": enhancedAlertMemoryDeviceAEPError,
       "enhancedAlertMemoryDeviceAEPWarning": enhancedAlertMemoryDeviceAEPWarning,
       "enhancedAlertMemoryDeviceAEPInfo": enhancedAlertMemoryDeviceAEPInfo,
       "enhancedAlertMemorySelfhealInitiate": enhancedAlertMemorySelfhealInitiate,
       "enhancedAlertMemoryDevicePPRSuccess": enhancedAlertMemoryDevicePPRSuccess,
       "enhancedAlertMemoryDevicePPRFail": enhancedAlertMemoryDevicePPRFail,
       "enhancedAlertFanEnclosureInsertion": enhancedAlertFanEnclosureInsertion,
       "enhancedAlertFanEnclosureRemoval": enhancedAlertFanEnclosureRemoval,
       "enhancedAlertFanEnclosureExtendedRemoval": enhancedAlertFanEnclosureExtendedRemoval,
       "enhancedAlertACPowerCordNoPowerNonRedundant": enhancedAlertACPowerCordNoPowerNonRedundant,
       "enhancedAlertACPowerCordNormal": enhancedAlertACPowerCordNormal,
       "enhancedAlertACPowerCordFailure": enhancedAlertACPowerCordFailure,
       "enhancedAlertLogNormal": enhancedAlertLogNormal,
       "enhancedAlertLogWarning": enhancedAlertLogWarning,
       "enhancedAlertLogFull": enhancedAlertLogFull,
       "enhancedAlertProcessorDeviceStatusNormal": enhancedAlertProcessorDeviceStatusNormal,
       "enhancedAlertProcessorDeviceStatusWarning": enhancedAlertProcessorDeviceStatusWarning,
       "enhancedAlertProcessorDeviceStatusFailure": enhancedAlertProcessorDeviceStatusFailure,
       "enhancedAlertDeviceAdd": enhancedAlertDeviceAdd,
       "enhancedAlertDeviceRemove": enhancedAlertDeviceRemove,
       "enhancedAlertDeviceConfigError": enhancedAlertDeviceConfigError,
       "enhancedAlertBatteryNormal": enhancedAlertBatteryNormal,
       "enhancedAlertBatteryWarning": enhancedAlertBatteryWarning,
       "enhancedAlertBatteryFailure": enhancedAlertBatteryFailure,
       "enhancedAlertBatteryAbsent": enhancedAlertBatteryAbsent,
       "enhancedAlertSDCardDeviceWarning": enhancedAlertSDCardDeviceWarning,
       "enhancedAlertSDCardDeviceFailure": enhancedAlertSDCardDeviceFailure,
       "enhancedAlertMemoryOEMNoAction": enhancedAlertMemoryOEMNoAction,
       "enhancedAlertMemoryOEMCheckConfigInfo": enhancedAlertMemoryOEMCheckConfigInfo,
       "enhancedAlertMemoryOEMReseatInfo": enhancedAlertMemoryOEMReseatInfo,
       "enhancedAlertMemoryOEMWarmBootInfo": enhancedAlertMemoryOEMWarmBootInfo,
       "enhancedAlertMemoryOEMColdBootInfo": enhancedAlertMemoryOEMColdBootInfo,
       "enhancedAlertMemoryOEMRetryInfo": enhancedAlertMemoryOEMRetryInfo,
       "enhancedAlertMemoryOEMSecureEraseInfo": enhancedAlertMemoryOEMSecureEraseInfo,
       "enhancedAlertMemoryOEMUnknownInfo": enhancedAlertMemoryOEMUnknownInfo,
       "enhancedAlertMemomoryOEMCheckConfigWarning": enhancedAlertMemomoryOEMCheckConfigWarning,
       "enhancedAlertMemomoryOEMReseatWarning": enhancedAlertMemomoryOEMReseatWarning,
       "enhancedAlertMemomoryOEMColdBootWarning": enhancedAlertMemomoryOEMColdBootWarning,
       "enhancedAlertMemomoryOEMContactServiceWarning": enhancedAlertMemomoryOEMContactServiceWarning,
       "enhancedAlertMemomoryOEMRetryWarning": enhancedAlertMemomoryOEMRetryWarning,
       "enhancedAlertMemomoryOEMUpdateFirmwareWarning": enhancedAlertMemomoryOEMUpdateFirmwareWarning,
       "enhancedAlertMemomoryContactAssistanceWarning": enhancedAlertMemomoryContactAssistanceWarning,
       "enhancedAlertMemomoryOEMUnknownWarning": enhancedAlertMemomoryOEMUnknownWarning,
       "enhancedAlertMemoryOEMCheckConfigCrit": enhancedAlertMemoryOEMCheckConfigCrit,
       "enhancedAlertMemoryOEMReseatCrit": enhancedAlertMemoryOEMReseatCrit,
       "enhancedAlertMemoryOEMColdBootCrit": enhancedAlertMemoryOEMColdBootCrit,
       "enhancedAlertMemoryOEMRetryCrit": enhancedAlertMemoryOEMRetryCrit,
       "enhancedAlertMemoryOEMSantizeCrit": enhancedAlertMemoryOEMSantizeCrit,
       "enhancedAlertMemoryOEMUpdateFirwareCrit": enhancedAlertMemoryOEMUpdateFirwareCrit,
       "enhancedAlertMemoryOEMContactSupportImmCrit": enhancedAlertMemoryOEMContactSupportImmCrit,
       "enhancedAlertMemoryOEMUnknownCrit": enhancedAlertMemoryOEMUnknownCrit,
       "mIBVersionGroup": mIBVersionGroup,
       "mIBMajorVersionNumber": mIBMajorVersionNumber,
       "mIBMinorVersionNumber": mIBMinorVersionNumber,
       "mIBMaintenanceVersionNumber": mIBMaintenanceVersionNumber,
       "systemManagementSoftwareGroup": systemManagementSoftwareGroup,
       "systemManagementSoftwareName": systemManagementSoftwareName,
       "systemManagementSoftwareVersionNumberName": systemManagementSoftwareVersionNumberName,
       "systemManagementSoftwareBuildNumber": systemManagementSoftwareBuildNumber,
       "systemManagementSoftwareDescriptionName": systemManagementSoftwareDescriptionName,
       "systemManagementSoftwareSupportedProtocol": systemManagementSoftwareSupportedProtocol,
       "systemManagementSoftwarePreferredProtocol": systemManagementSoftwarePreferredProtocol,
       "systemManagementSoftwareUpdateLevelName": systemManagementSoftwareUpdateLevelName,
       "systemManagementSoftwareURLName": systemManagementSoftwareURLName,
       "systemManagementSoftwareLanguageName": systemManagementSoftwareLanguageName,
       "systemManagementSoftwareGlobalVersionName": systemManagementSoftwareGlobalVersionName,
       "systemManagementSoftwareFeatureFlags": systemManagementSoftwareFeatureFlags,
       "systemManagementSoftwareSNMPAgentFeatureFlags": systemManagementSoftwareSNMPAgentFeatureFlags,
       "systemManagementSoftwareManufacturerName": systemManagementSoftwareManufacturerName,
       "systemManagementSoftwareProdUseFeedback": systemManagementSoftwareProdUseFeedback,
       "systemStateGroup": systemStateGroup,
       "systemStateTable": systemStateTable,
       "systemStateTableEntry": systemStateTableEntry,
       "systemStatechassisIndex": systemStatechassisIndex,
       "systemStateGlobalSystemStatus": systemStateGlobalSystemStatus,
       "systemStateChassisState": systemStateChassisState,
       "systemStateChassisStatus": systemStateChassisStatus,
       "systemStatePowerUnitStateDetails": systemStatePowerUnitStateDetails,
       "systemStatePowerUnitStatusRedundancy": systemStatePowerUnitStatusRedundancy,
       "systemStatePowerUnitStatusDetails": systemStatePowerUnitStatusDetails,
       "systemStatePowerSupplyStateDetails": systemStatePowerSupplyStateDetails,
       "systemStatePowerSupplyStatusCombined": systemStatePowerSupplyStatusCombined,
       "systemStatePowerSupplyStatusDetails": systemStatePowerSupplyStatusDetails,
       "systemStateVoltageStateDetails": systemStateVoltageStateDetails,
       "systemStateVoltageStatusCombined": systemStateVoltageStatusCombined,
       "systemStateVoltageStatusDetails": systemStateVoltageStatusDetails,
       "systemStateAmperageStateDetails": systemStateAmperageStateDetails,
       "systemStateAmperageStatusCombined": systemStateAmperageStatusCombined,
       "systemStateAmperageStatusDetails": systemStateAmperageStatusDetails,
       "systemStateCoolingUnitStateDetails": systemStateCoolingUnitStateDetails,
       "systemStateCoolingUnitStatusRedundancy": systemStateCoolingUnitStatusRedundancy,
       "systemStateCoolingUnitStatusDetails": systemStateCoolingUnitStatusDetails,
       "systemStateCoolingDeviceStateDetails": systemStateCoolingDeviceStateDetails,
       "systemStateCoolingDeviceStatusCombined": systemStateCoolingDeviceStatusCombined,
       "systemStateCoolingDeviceStatusDetails": systemStateCoolingDeviceStatusDetails,
       "systemStateTemperatureStateDetails": systemStateTemperatureStateDetails,
       "systemStateTemperatureStatusCombined": systemStateTemperatureStatusCombined,
       "systemStateTemperatureStatusDetails": systemStateTemperatureStatusDetails,
       "systemStateMemoryDeviceStateDetails": systemStateMemoryDeviceStateDetails,
       "systemStateMemoryDeviceStatusCombined": systemStateMemoryDeviceStatusCombined,
       "systemStateMemoryDeviceStatusDetails": systemStateMemoryDeviceStatusDetails,
       "systemStateChassisIntrusionStateDetails": systemStateChassisIntrusionStateDetails,
       "systemStateChassisIntrusionStatusCombined": systemStateChassisIntrusionStatusCombined,
       "systemStateChassisIntrusionStatusDetails": systemStateChassisIntrusionStatusDetails,
       "systemStateACPowerSwitchStateDetails": systemStateACPowerSwitchStateDetails,
       "systemStateACPowerSwitchStatusRedundancy": systemStateACPowerSwitchStatusRedundancy,
       "systemStateACPowerSwitchStatusDetails": systemStateACPowerSwitchStatusDetails,
       "systemStateACPowerCordStateDetails": systemStateACPowerCordStateDetails,
       "systemStateACPowerCordStatusCombined": systemStateACPowerCordStatusCombined,
       "systemStateACPowerCordStatusDetails": systemStateACPowerCordStatusDetails,
       "systemStateRedundantMemoryUnitStateDetails": systemStateRedundantMemoryUnitStateDetails,
       "systemStateRedundantMemoryUnitStatusRedundancy": systemStateRedundantMemoryUnitStatusRedundancy,
       "systemStateRedundantMemoryUnitStatusDetails": systemStateRedundantMemoryUnitStatusDetails,
       "systemStateEventLogStatus": systemStateEventLogStatus,
       "systemStatePowerUnitStatusCombined": systemStatePowerUnitStatusCombined,
       "systemStatePowerUnitStatusList": systemStatePowerUnitStatusList,
       "systemStateCoolingUnitStatusCombined": systemStateCoolingUnitStatusCombined,
       "systemStateCoolingUnitStatusList": systemStateCoolingUnitStatusList,
       "systemStateACPowerSwitchStatusCombined": systemStateACPowerSwitchStatusCombined,
       "systemStateACPowerSwitchStatusList": systemStateACPowerSwitchStatusList,
       "systemStateRedundantMemoryUnitStatusCombined": systemStateRedundantMemoryUnitStatusCombined,
       "systemStateRedundantMemoryUnitStatusList": systemStateRedundantMemoryUnitStatusList,
       "systemStateProcessorDeviceStatusCombined": systemStateProcessorDeviceStatusCombined,
       "systemStateProcessorDeviceStatusList": systemStateProcessorDeviceStatusList,
       "systemStateBatteryStatusCombined": systemStateBatteryStatusCombined,
       "systemStateBatteryStatusList": systemStateBatteryStatusList,
       "systemStateSDCardUnitStatusCombined": systemStateSDCardUnitStatusCombined,
       "systemStateSDCardUnitStatusList": systemStateSDCardUnitStatusList,
       "systemStateSDCardDeviceStatusCombined": systemStateSDCardDeviceStatusCombined,
       "systemStateSDCardDeviceStatusList": systemStateSDCardDeviceStatusList,
       "chassisInformationGroup": chassisInformationGroup,
       "chassisInformationTable": chassisInformationTable,
       "chassisInformationTableEntry": chassisInformationTableEntry,
       "chassisIndexChassisInformation": chassisIndexChassisInformation,
       "chassisStateCapabilities": chassisStateCapabilities,
       "chassisStateSettings": chassisStateSettings,
       "chassisStatus": chassisStatus,
       "chassisparentIndexReference": chassisparentIndexReference,
       "chassisType": chassisType,
       "chassisName": chassisName,
       "chassisManufacturerName": chassisManufacturerName,
       "chassisModelName": chassisModelName,
       "chassisAssetTagName": chassisAssetTagName,
       "chassisServiceTagName": chassisServiceTagName,
       "chassisID": chassisID,
       "chassisIDExtension": chassisIDExtension,
       "chassisSystemClass": chassisSystemClass,
       "chassisSystemName": chassisSystemName,
       "chassisSystemBootDateName": chassisSystemBootDateName,
       "chassisSystemDateName": chassisSystemDateName,
       "chassisSystemLocationName": chassisSystemLocationName,
       "chassisSystemPrimaryUserName": chassisSystemPrimaryUserName,
       "chassisSystemUserPhoneNumberName": chassisSystemUserPhoneNumberName,
       "chassisConnectionStatusUnique": chassisConnectionStatusUnique,
       "chassisFanControlCapabilitiesUnique": chassisFanControlCapabilitiesUnique,
       "chassisFanControlSettingsUnique": chassisFanControlSettingsUnique,
       "chassisLEDControlCapabilitiesUnique": chassisLEDControlCapabilitiesUnique,
       "chassisLEDControlSettingsUnique": chassisLEDControlSettingsUnique,
       "chassisHDFaultClearControlCapabilities": chassisHDFaultClearControlCapabilities,
       "chassisHDFaultClearControlSettings": chassisHDFaultClearControlSettings,
       "chassisIdentifyFlashControlCapabilities": chassisIdentifyFlashControlCapabilities,
       "chassisIdentifyFlashControlSettings": chassisIdentifyFlashControlSettings,
       "chassisLockPresent": chassisLockPresent,
       "chassishostControlCapabilitiesUnique": chassishostControlCapabilitiesUnique,
       "chassishostControlSettingsUnique": chassishostControlSettingsUnique,
       "chassiswatchDogControlCapabilitiesUnique": chassiswatchDogControlCapabilitiesUnique,
       "chassiswatchDogControlSettingsUnique": chassiswatchDogControlSettingsUnique,
       "chassiswatchDogControlExpiryTimeCapabilitiesUnique": chassiswatchDogControlExpiryTimeCapabilitiesUnique,
       "chassiswatchDogControlExpiryTime": chassiswatchDogControlExpiryTime,
       "chassisallowSETCommandsfromSNMP": chassisallowSETCommandsfromSNMP,
       "chassisPowerButtonControlCapabilitiesUnique": chassisPowerButtonControlCapabilitiesUnique,
       "chassisPowerButtonControlSettingsUnique": chassisPowerButtonControlSettingsUnique,
       "chassisResellerName": chassisResellerName,
       "chassisResellerContactInformationName": chassisResellerContactInformationName,
       "chassisResellerProductName": chassisResellerProductName,
       "chassisResellerSystemID": chassisResellerSystemID,
       "chassisNMIButtonControlCapabilitiesUnique": chassisNMIButtonControlCapabilitiesUnique,
       "chassisNMIButtonControlSettingsUnique": chassisNMIButtonControlSettingsUnique,
       "chassisSystemProperties": chassisSystemProperties,
       "chassisSystemRevisionNumber": chassisSystemRevisionNumber,
       "chassisSystemRevisionName": chassisSystemRevisionName,
       "chassisExpressServiceCodeName": chassisExpressServiceCodeName,
       "chassisNodeIDName": chassisNodeIDName,
       "uUIDTable": uUIDTable,
       "uUIDTableEntry": uUIDTableEntry,
       "uUIDchassisIndex": uUIDchassisIndex,
       "uUIDIndex": uUIDIndex,
       "uUIDType": uUIDType,
       "uUIDValue": uUIDValue,
       "postLogTable": postLogTable,
       "postLogTableEntry": postLogTableEntry,
       "postLogchassisIndex": postLogchassisIndex,
       "postLogRecordIndex": postLogRecordIndex,
       "postLogStateCapabilitiesUnique": postLogStateCapabilitiesUnique,
       "postLogStateSettingsUnique": postLogStateSettingsUnique,
       "postLogRecord": postLogRecord,
       "postLogFormat": postLogFormat,
       "eventLogTable": eventLogTable,
       "eventLogTableEntry": eventLogTableEntry,
       "eventLogchassisIndex": eventLogchassisIndex,
       "eventLogRecordIndex": eventLogRecordIndex,
       "eventLogStateCapabilitiesUnique": eventLogStateCapabilitiesUnique,
       "eventLogStateSettingsUnique": eventLogStateSettingsUnique,
       "eventLogRecord": eventLogRecord,
       "eventLogFormat": eventLogFormat,
       "eventLogSeverityStatus": eventLogSeverityStatus,
       "eventLogDateName": eventLogDateName,
       "systemBIOSTable": systemBIOSTable,
       "systemBIOSTableEntry": systemBIOSTableEntry,
       "systemBIOSchassisIndex": systemBIOSchassisIndex,
       "systemBIOSIndex": systemBIOSIndex,
       "systemBIOSStateCapabilities": systemBIOSStateCapabilities,
       "systemBIOSStateSettings": systemBIOSStateSettings,
       "systemBIOSStatus": systemBIOSStatus,
       "systemBIOSSize": systemBIOSSize,
       "systemBIOSReleaseDateName": systemBIOSReleaseDateName,
       "systemBIOSVersionName": systemBIOSVersionName,
       "systemBIOSStartingAddress": systemBIOSStartingAddress,
       "systemBIOSEndingAddress": systemBIOSEndingAddress,
       "systemBIOSManufacturerName": systemBIOSManufacturerName,
       "systemBIOSCharacteristics": systemBIOSCharacteristics,
       "systemBIOSCharacteristicsExt1": systemBIOSCharacteristicsExt1,
       "systemBIOSCharacteristicsExt2": systemBIOSCharacteristicsExt2,
       "firmwareTable": firmwareTable,
       "firmwareTableEntry": firmwareTableEntry,
       "firmwarechassisIndex": firmwarechassisIndex,
       "firmwareIndex": firmwareIndex,
       "firmwareStateCapabilities": firmwareStateCapabilities,
       "firmwareStateSettings": firmwareStateSettings,
       "firmwareStatus": firmwareStatus,
       "firmwareSize": firmwareSize,
       "firmwareType": firmwareType,
       "firmwareTypeName": firmwareTypeName,
       "firmwareUpdateCapabilities": firmwareUpdateCapabilities,
       "firmwareDateName": firmwareDateName,
       "firmwareVersionName": firmwareVersionName,
       "intrusionTable": intrusionTable,
       "intrusionTableEntry": intrusionTableEntry,
       "intrusionchassisIndex": intrusionchassisIndex,
       "intrusionIndex": intrusionIndex,
       "intrusionStateCapabilities": intrusionStateCapabilities,
       "intrusionStateSettings": intrusionStateSettings,
       "intrusionStatus": intrusionStatus,
       "intrusionReading": intrusionReading,
       "intrusionType": intrusionType,
       "intrusionLocationName": intrusionLocationName,
       "baseBoardTable": baseBoardTable,
       "baseBoardTableEntry": baseBoardTableEntry,
       "baseBoardChassisIndex": baseBoardChassisIndex,
       "baseBoardIndex": baseBoardIndex,
       "baseBoardStateCapabilities": baseBoardStateCapabilities,
       "baseBoardStateSettings": baseBoardStateSettings,
       "baseBoardStatus": baseBoardStatus,
       "baseBoardFeatureFlags": baseBoardFeatureFlags,
       "baseBoardType": baseBoardType,
       "baseBoardTypeName": baseBoardTypeName,
       "baseBoardLocationName": baseBoardLocationName,
       "baseBoardManufacturerName": baseBoardManufacturerName,
       "baseBoardProductName": baseBoardProductName,
       "baseBoardVersionName": baseBoardVersionName,
       "baseBoardServiceTagName": baseBoardServiceTagName,
       "baseBoardPiecePartIDName": baseBoardPiecePartIDName,
       "baseBoardAssetTagName": baseBoardAssetTagName,
       "baseBoardExpressServiceCodeName": baseBoardExpressServiceCodeName,
       "operatingSystemGroup": operatingSystemGroup,
       "operatingSystemTable": operatingSystemTable,
       "operatingSystemTableEntry": operatingSystemTableEntry,
       "operatingSystemchassisIndex": operatingSystemchassisIndex,
       "operatingSystemStateCapabilities": operatingSystemStateCapabilities,
       "operatingSystemStateSettings": operatingSystemStateSettings,
       "operatingSystemStatus": operatingSystemStatus,
       "operatingSystemIsPrimary": operatingSystemIsPrimary,
       "operatingSystemOperatingSystemName": operatingSystemOperatingSystemName,
       "operatingSystemOperatingSystemVersionName": operatingSystemOperatingSystemVersionName,
       "operatingSystemMemoryTable": operatingSystemMemoryTable,
       "operatingSystemMemoryTableEntry": operatingSystemMemoryTableEntry,
       "operatingSystemMemorychassisIndex": operatingSystemMemorychassisIndex,
       "operatingSystemMemoryStateCapabilities": operatingSystemMemoryStateCapabilities,
       "operatingSystemMemoryStateSettings": operatingSystemMemoryStateSettings,
       "operatingSystemMemoryStatus": operatingSystemMemoryStatus,
       "operatingSystemMemoryTotalPhysicalSize": operatingSystemMemoryTotalPhysicalSize,
       "operatingSystemMemoryAvailablePhysicalSize": operatingSystemMemoryAvailablePhysicalSize,
       "operatingSystemMemoryTotalPageFileSize": operatingSystemMemoryTotalPageFileSize,
       "operatingSystemMemoryAvailablePageFileSize": operatingSystemMemoryAvailablePageFileSize,
       "operatingSystemMemoryTotalVirtualSize": operatingSystemMemoryTotalVirtualSize,
       "operatingSystemMemoryAvailableVirtualSize": operatingSystemMemoryAvailableVirtualSize,
       "operatingSystemMemoryExtTotalPhysicalSize": operatingSystemMemoryExtTotalPhysicalSize,
       "systemResourceGroup": systemResourceGroup,
       "systemResourceMapTable": systemResourceMapTable,
       "systemResourceMapTableEntry": systemResourceMapTableEntry,
       "systemResourceMapchassisIndex": systemResourceMapchassisIndex,
       "systemResourceMapIndex": systemResourceMapIndex,
       "systemResourceMapStateCapabilities": systemResourceMapStateCapabilities,
       "systemResourceMapStateSettings": systemResourceMapStateSettings,
       "systemResourceMapStatus": systemResourceMapStatus,
       "systemResourceMapType": systemResourceMapType,
       "systemResourceOwnerTable": systemResourceOwnerTable,
       "systemResourceOwnerTableEntry": systemResourceOwnerTableEntry,
       "systemResourceOwnerchassisIndex": systemResourceOwnerchassisIndex,
       "systemResourceOwnerIndex": systemResourceOwnerIndex,
       "systemResourceOwnerStateCapabilities": systemResourceOwnerStateCapabilities,
       "systemResourceOwnerStateSettings": systemResourceOwnerStateSettings,
       "systemResourceOwnerStatus": systemResourceOwnerStatus,
       "systemResourceOwnerInterfaceType": systemResourceOwnerInterfaceType,
       "systemResourceMapIndexReference": systemResourceMapIndexReference,
       "systemResourceOwnerDescriptionName": systemResourceOwnerDescriptionName,
       "systemResourceOwnerInterfaceInstance": systemResourceOwnerInterfaceInstance,
       "systemResourceIOPortTable": systemResourceIOPortTable,
       "systemResourceIOPortTableEntry": systemResourceIOPortTableEntry,
       "systemResourceIOPortchassisIndex": systemResourceIOPortchassisIndex,
       "systemResourceIOPortIndex": systemResourceIOPortIndex,
       "systemResourceIOPortStateCapabilities": systemResourceIOPortStateCapabilities,
       "systemResourceIOPortStateSettings": systemResourceIOPortStateSettings,
       "systemResourceIOPortStatus": systemResourceIOPortStatus,
       "systemResourceIOPortOwnerIndexReference": systemResourceIOPortOwnerIndexReference,
       "systemResourceIOPortShareDisposition": systemResourceIOPortShareDisposition,
       "systemResourceIOPortStartingAddress": systemResourceIOPortStartingAddress,
       "systemResourceIOPortEndingAddress": systemResourceIOPortEndingAddress,
       "systemResourceMemoryTable": systemResourceMemoryTable,
       "systemResourceMemoryTableEntry": systemResourceMemoryTableEntry,
       "systemResourceMemorychassisIndex": systemResourceMemorychassisIndex,
       "systemResourceMemoryIndex": systemResourceMemoryIndex,
       "systemResourceMemoryStateCapabilities": systemResourceMemoryStateCapabilities,
       "systemResourceMemoryStateSettings": systemResourceMemoryStateSettings,
       "systemResourceMemoryStatus": systemResourceMemoryStatus,
       "systemResourceMemoryOwnerIndexReference": systemResourceMemoryOwnerIndexReference,
       "systemResourceMemoryShareDisposition": systemResourceMemoryShareDisposition,
       "systemResourceMemoryStartingAddress": systemResourceMemoryStartingAddress,
       "systemResourceMemoryEndingAddress": systemResourceMemoryEndingAddress,
       "systemResourceMemoryFlags": systemResourceMemoryFlags,
       "systemResourceInterruptTable": systemResourceInterruptTable,
       "systemResourceInterruptTableEntry": systemResourceInterruptTableEntry,
       "systemResourceInterruptchassisIndex": systemResourceInterruptchassisIndex,
       "systemResourceInterruptIndex": systemResourceInterruptIndex,
       "systemResourceInterruptStateCapabilities": systemResourceInterruptStateCapabilities,
       "systemResourceInterruptStateSettings": systemResourceInterruptStateSettings,
       "systemResourceInterruptStatus": systemResourceInterruptStatus,
       "systemResourceInterruptOwnerIndexReference": systemResourceInterruptOwnerIndexReference,
       "systemResourceInterruptShareDisposition": systemResourceInterruptShareDisposition,
       "systemResourceInterruptLevel": systemResourceInterruptLevel,
       "systemResourceInterruptType": systemResourceInterruptType,
       "systemResourceInterruptTrigger": systemResourceInterruptTrigger,
       "systemResourceDMATable": systemResourceDMATable,
       "systemResourceDMATableEntry": systemResourceDMATableEntry,
       "systemResourceDMAchassisIndex": systemResourceDMAchassisIndex,
       "systemResourceDMAIndex": systemResourceDMAIndex,
       "systemResourceDMAStateCapabilities": systemResourceDMAStateCapabilities,
       "systemResourceDMAStateSettings": systemResourceDMAStateSettings,
       "systemResourceDMAStatus": systemResourceDMAStatus,
       "systemResourceDMAOwnerIndexReference": systemResourceDMAOwnerIndexReference,
       "systemResourceDMAShareDisposition": systemResourceDMAShareDisposition,
       "systemResourceDMAMaximumTransferSize": systemResourceDMAMaximumTransferSize,
       "systemResourceDMATransferWidth": systemResourceDMATransferWidth,
       "systemResourceDMABusMaster": systemResourceDMABusMaster,
       "powerGroup": powerGroup,
       "powerUnitTable": powerUnitTable,
       "powerUnitTableEntry": powerUnitTableEntry,
       "powerUnitchassisIndex": powerUnitchassisIndex,
       "powerUnitIndex": powerUnitIndex,
       "powerUnitStateCapabilities": powerUnitStateCapabilities,
       "powerUnitStateSettings": powerUnitStateSettings,
       "powerUnitRedundancyStatus": powerUnitRedundancyStatus,
       "powerSupplyCountForRedundancy": powerSupplyCountForRedundancy,
       "powerUnitName": powerUnitName,
       "powerUnitStatus": powerUnitStatus,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyTableEntry": powerSupplyTableEntry,
       "powerSupplychassisIndex": powerSupplychassisIndex,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyStateCapabilitiesUnique": powerSupplyStateCapabilitiesUnique,
       "powerSupplyStateSettingsUnique": powerSupplyStateSettingsUnique,
       "powerSupplyStatus": powerSupplyStatus,
       "powerSupplyOutputWatts": powerSupplyOutputWatts,
       "powerSupplyType": powerSupplyType,
       "powerSupplyLocationName": powerSupplyLocationName,
       "powerSupplyInputVoltage": powerSupplyInputVoltage,
       "powerSupplypowerUnitIndexReference": powerSupplypowerUnitIndexReference,
       "powerSupplySensorState": powerSupplySensorState,
       "powerSupplyConfigurationErrorType": powerSupplyConfigurationErrorType,
       "powerSupplyPowerMonitorCapable": powerSupplyPowerMonitorCapable,
       "powerSupplyRatedInputWattage": powerSupplyRatedInputWattage,
       "voltageProbeTable": voltageProbeTable,
       "voltageProbeTableEntry": voltageProbeTableEntry,
       "voltageProbechassisIndex": voltageProbechassisIndex,
       "voltageProbeIndex": voltageProbeIndex,
       "voltageProbeStateCapabilities": voltageProbeStateCapabilities,
       "voltageProbeStateSettings": voltageProbeStateSettings,
       "voltageProbeStatus": voltageProbeStatus,
       "voltageProbeReading": voltageProbeReading,
       "voltageProbeType": voltageProbeType,
       "voltageProbeLocationName": voltageProbeLocationName,
       "voltageProbeUpperNonRecoverableThreshold": voltageProbeUpperNonRecoverableThreshold,
       "voltageProbeUpperCriticalThreshold": voltageProbeUpperCriticalThreshold,
       "voltageProbeUpperNonCriticalThreshold": voltageProbeUpperNonCriticalThreshold,
       "voltageProbeLowerNonCriticalThreshold": voltageProbeLowerNonCriticalThreshold,
       "voltageProbeLowerCriticalThreshold": voltageProbeLowerCriticalThreshold,
       "voltageProbeLowerNonRecoverableThreshold": voltageProbeLowerNonRecoverableThreshold,
       "voltageProbeProbeCapabilities": voltageProbeProbeCapabilities,
       "voltageProbeDiscreteReading": voltageProbeDiscreteReading,
       "amperageProbeTable": amperageProbeTable,
       "amperageProbeTableEntry": amperageProbeTableEntry,
       "amperageProbechassisIndex": amperageProbechassisIndex,
       "amperageProbeIndex": amperageProbeIndex,
       "amperageProbeStateCapabilities": amperageProbeStateCapabilities,
       "amperageProbeStateSettings": amperageProbeStateSettings,
       "amperageProbeStatus": amperageProbeStatus,
       "amperageProbeReading": amperageProbeReading,
       "amperageProbeType": amperageProbeType,
       "amperageProbeLocationName": amperageProbeLocationName,
       "amperageProbeUpperNonRecoverableThreshold": amperageProbeUpperNonRecoverableThreshold,
       "amperageProbeUpperCriticalThreshold": amperageProbeUpperCriticalThreshold,
       "amperageProbeUpperNonCriticalThreshold": amperageProbeUpperNonCriticalThreshold,
       "amperageProbeLowerNonCriticalThreshold": amperageProbeLowerNonCriticalThreshold,
       "amperageProbeLowerCriticalThreshold": amperageProbeLowerCriticalThreshold,
       "amperageProbeLowerNonRecoverableThreshold": amperageProbeLowerNonRecoverableThreshold,
       "amperageProbeProbeCapabilities": amperageProbeProbeCapabilities,
       "amperageProbeDiscreteReading": amperageProbeDiscreteReading,
       "aCPowerSwitchTable": aCPowerSwitchTable,
       "aCPowerSwitchTableEntry": aCPowerSwitchTableEntry,
       "aCPowerSwitchchassisIndex": aCPowerSwitchchassisIndex,
       "aCPowerSwitchIndex": aCPowerSwitchIndex,
       "aCPowerSwitchCapabilities": aCPowerSwitchCapabilities,
       "aCPowerSwitchSettings": aCPowerSwitchSettings,
       "aCPowerSwitchRedundancyStatus": aCPowerSwitchRedundancyStatus,
       "aCPowerCordCountForRedundancy": aCPowerCordCountForRedundancy,
       "aCPowerSwitchName": aCPowerSwitchName,
       "aCPowerSwitchRedundancyMode": aCPowerSwitchRedundancyMode,
       "aCPowerSwitchStatus": aCPowerSwitchStatus,
       "aCPowerCordTable": aCPowerCordTable,
       "aCPowerCordTableEntry": aCPowerCordTableEntry,
       "aCPowerCordchassisIndex": aCPowerCordchassisIndex,
       "aCPowerCordIndex": aCPowerCordIndex,
       "aCPowerCordStateCapabilities": aCPowerCordStateCapabilities,
       "aCPowerCordStateSettings": aCPowerCordStateSettings,
       "aCPowerCordStatus": aCPowerCordStatus,
       "aCPowerCordaCPowerSwitchIndexReference": aCPowerCordaCPowerSwitchIndexReference,
       "aCPowerCordLocationName": aCPowerCordLocationName,
       "batteryTable": batteryTable,
       "batteryTableEntry": batteryTableEntry,
       "batteryChassisIndex": batteryChassisIndex,
       "batteryIndex": batteryIndex,
       "batteryStateCapabilities": batteryStateCapabilities,
       "batteryStateSettings": batteryStateSettings,
       "batteryStatus": batteryStatus,
       "batteryReading": batteryReading,
       "batteryLocationName": batteryLocationName,
       "powerUsageTable": powerUsageTable,
       "powerUsageTableEntry": powerUsageTableEntry,
       "powerUsageChassisIndex": powerUsageChassisIndex,
       "powerUsageIndex": powerUsageIndex,
       "powerUsageStateCapabilities": powerUsageStateCapabilities,
       "powerUsageStateSettings": powerUsageStateSettings,
       "powerUsageStatus": powerUsageStatus,
       "powerUsageEntityName": powerUsageEntityName,
       "powerUsageCumulativeWattage": powerUsageCumulativeWattage,
       "powerUsageCumulativeWattageStartDateName": powerUsageCumulativeWattageStartDateName,
       "powerUsagePeakWatts": powerUsagePeakWatts,
       "powerUsagePeakWattsStartDateName": powerUsagePeakWattsStartDateName,
       "powerUsagePeakWattsReadingDateName": powerUsagePeakWattsReadingDateName,
       "powerUsagePeakAmps": powerUsagePeakAmps,
       "powerUsagePeakAmpsStartDateName": powerUsagePeakAmpsStartDateName,
       "powerUsagePeakAmpsReadingDateName": powerUsagePeakAmpsReadingDateName,
       "powerUsageIdlePower": powerUsageIdlePower,
       "powerUsageMaxPotentialPower": powerUsageMaxPotentialPower,
       "powerUsagePowerCapCapabilities": powerUsagePowerCapCapabilities,
       "powerUsagePowerCapSetting": powerUsagePowerCapSetting,
       "powerUsagePowerCapValue": powerUsagePowerCapValue,
       "powerUsageInstantaneousHeadroom": powerUsageInstantaneousHeadroom,
       "powerUsagePeakHeadroom": powerUsagePeakHeadroom,
       "powerProfileTable": powerProfileTable,
       "powerProfileTableEntry": powerProfileTableEntry,
       "powerProfileChassisIndex": powerProfileChassisIndex,
       "powerProfileIndex": powerProfileIndex,
       "powerProfileSupportedProfiles": powerProfileSupportedProfiles,
       "powerProfileSetting": powerProfileSetting,
       "powerProfileCustomCPUMgmtCapabilities": powerProfileCustomCPUMgmtCapabilities,
       "powerProfileCustomCPUMgmtSetting": powerProfileCustomCPUMgmtSetting,
       "powerProfileCustomMemoryMgmtCapabilities": powerProfileCustomMemoryMgmtCapabilities,
       "powerProfileCustomMemoryMgmtSetting": powerProfileCustomMemoryMgmtSetting,
       "powerProfileCustomFanMgmtCapabilities": powerProfileCustomFanMgmtCapabilities,
       "powerProfileCustomFanMgmtSetting": powerProfileCustomFanMgmtSetting,
       "thermalGroup": thermalGroup,
       "coolingUnitTable": coolingUnitTable,
       "coolingUnitTableEntry": coolingUnitTableEntry,
       "coolingUnitchassisIndex": coolingUnitchassisIndex,
       "coolingUnitIndex": coolingUnitIndex,
       "coolingUnitStateCapabilties": coolingUnitStateCapabilties,
       "coolingUnitStateSettings": coolingUnitStateSettings,
       "coolingUnitRedundancyStatus": coolingUnitRedundancyStatus,
       "coolingDeviceCountForRedundancy": coolingDeviceCountForRedundancy,
       "coolingUnitName": coolingUnitName,
       "coolingUnitStatus": coolingUnitStatus,
       "coolingDeviceTable": coolingDeviceTable,
       "coolingDeviceTableEntry": coolingDeviceTableEntry,
       "coolingDevicechassisIndex": coolingDevicechassisIndex,
       "coolingDeviceIndex": coolingDeviceIndex,
       "coolingDeviceStateCapabilities": coolingDeviceStateCapabilities,
       "coolingDeviceStateSettings": coolingDeviceStateSettings,
       "coolingDeviceStatus": coolingDeviceStatus,
       "coolingDeviceReading": coolingDeviceReading,
       "coolingDeviceType": coolingDeviceType,
       "coolingDeviceLocationName": coolingDeviceLocationName,
       "coolingDeviceUpperNonRecoverableThreshold": coolingDeviceUpperNonRecoverableThreshold,
       "coolingDeviceUpperCriticalThreshold": coolingDeviceUpperCriticalThreshold,
       "coolingDeviceUpperNonCriticalThreshold": coolingDeviceUpperNonCriticalThreshold,
       "coolingDeviceLowerNonCriticalThreshold": coolingDeviceLowerNonCriticalThreshold,
       "coolingDeviceLowerCriticalThreshold": coolingDeviceLowerCriticalThreshold,
       "coolingDeviceLowerNonRecoverableThreshold": coolingDeviceLowerNonRecoverableThreshold,
       "coolingDevicecoolingUnitIndexReference": coolingDevicecoolingUnitIndexReference,
       "coolingDeviceSubType": coolingDeviceSubType,
       "coolingDeviceProbeCapabilities": coolingDeviceProbeCapabilities,
       "coolingDeviceDiscreteReading": coolingDeviceDiscreteReading,
       "temperatureProbeTable": temperatureProbeTable,
       "temperatureProbeTableEntry": temperatureProbeTableEntry,
       "temperatureProbechassisIndex": temperatureProbechassisIndex,
       "temperatureProbeIndex": temperatureProbeIndex,
       "temperatureProbeStateCapabilities": temperatureProbeStateCapabilities,
       "temperatureProbeStateSettings": temperatureProbeStateSettings,
       "temperatureProbeStatus": temperatureProbeStatus,
       "temperatureProbeReading": temperatureProbeReading,
       "temperatureProbeType": temperatureProbeType,
       "temperatureProbeLocationName": temperatureProbeLocationName,
       "temperatureProbeUpperNonRecoverableThreshold": temperatureProbeUpperNonRecoverableThreshold,
       "temperatureProbeUpperCriticalThreshold": temperatureProbeUpperCriticalThreshold,
       "temperatureProbeUpperNonCriticalThreshold": temperatureProbeUpperNonCriticalThreshold,
       "temperatureProbeLowerNonCriticalThreshold": temperatureProbeLowerNonCriticalThreshold,
       "temperatureProbeLowerCriticalThreshold": temperatureProbeLowerCriticalThreshold,
       "temperatureProbeLowerNonRecoverableThreshold": temperatureProbeLowerNonRecoverableThreshold,
       "temperatureProbeProbeCapabilities": temperatureProbeProbeCapabilities,
       "temperatureProbeDiscreteReading": temperatureProbeDiscreteReading,
       "userSecurityGroup": userSecurityGroup,
       "userSecurityTable": userSecurityTable,
       "userSecurityTableEntry": userSecurityTableEntry,
       "userSecuritychassisIndex": userSecuritychassisIndex,
       "userSecurityIndex": userSecurityIndex,
       "userSecurityUserName": userSecurityUserName,
       "userSecurityControlName": userSecurityControlName,
       "userSecurityRequestName": userSecurityRequestName,
       "remoteFlashBIOSGroup": remoteFlashBIOSGroup,
       "remoteFlashBIOSTable": remoteFlashBIOSTable,
       "remoteFlashBIOSTableEntry": remoteFlashBIOSTableEntry,
       "remoteFlashBIOSchassisIndex": remoteFlashBIOSchassisIndex,
       "remoteFlashBIOSIndex": remoteFlashBIOSIndex,
       "remoteFlashBIOSStateCapabilitiesUnique": remoteFlashBIOSStateCapabilitiesUnique,
       "remoteFlashBIOSStateSettingsUnique": remoteFlashBIOSStateSettingsUnique,
       "remoteFlashBIOSStatus": remoteFlashBIOSStatus,
       "remoteFlashBIOSLastBIOSDateName": remoteFlashBIOSLastBIOSDateName,
       "remoteFlashBIOSCompletionCode": remoteFlashBIOSCompletionCode,
       "remoteFlashBIOSMinimumContiguousMemory": remoteFlashBIOSMinimumContiguousMemory,
       "portGroup": portGroup,
       "pointingPortTable": pointingPortTable,
       "pointingPortTableEntry": pointingPortTableEntry,
       "pointingPortchassisIndex": pointingPortchassisIndex,
       "pointingPortIndex": pointingPortIndex,
       "pointingPortStateCapabilities": pointingPortStateCapabilities,
       "pointingPortStateSettings": pointingPortStateSettings,
       "pointingPortStatus": pointingPortStatus,
       "pointingPortSecurityState": pointingPortSecurityState,
       "pointingPortConnectorType": pointingPortConnectorType,
       "pointingPortName": pointingPortName,
       "pointingPortBIOSConnectorType": pointingPortBIOSConnectorType,
       "keyboardPortTable": keyboardPortTable,
       "keyboardPortTableEntry": keyboardPortTableEntry,
       "keyboardPortchassisIndex": keyboardPortchassisIndex,
       "keyboardPortIndex": keyboardPortIndex,
       "keyboardPortStateCapabilities": keyboardPortStateCapabilities,
       "keyboardPortStateSettings": keyboardPortStateSettings,
       "keyboardPortStatus": keyboardPortStatus,
       "keyboardPortSecurityState": keyboardPortSecurityState,
       "keyboardPortConnectorType": keyboardPortConnectorType,
       "keyboardPortName": keyboardPortName,
       "keyboardPortBIOSConnectorType": keyboardPortBIOSConnectorType,
       "processorPortTable": processorPortTable,
       "processorPortTableEntry": processorPortTableEntry,
       "processorPortchassisIndex": processorPortchassisIndex,
       "processorPortIndex": processorPortIndex,
       "processorPortStateCapabilities": processorPortStateCapabilities,
       "processorPortStateSettings": processorPortStateSettings,
       "processorPortStatus": processorPortStatus,
       "processorPortSecurityState": processorPortSecurityState,
       "processorPortConnectorType": processorPortConnectorType,
       "processorPortName": processorPortName,
       "processorPortBIOSConnectorType": processorPortBIOSConnectorType,
       "memoryDevicePortTable": memoryDevicePortTable,
       "memoryDevicePortTableEntry": memoryDevicePortTableEntry,
       "memoryDevicePortchassisIndex": memoryDevicePortchassisIndex,
       "memoryDevicePortIndex": memoryDevicePortIndex,
       "memoryDevicePortStateCapabilities": memoryDevicePortStateCapabilities,
       "memoryDevicePortStateSettings": memoryDevicePortStateSettings,
       "memoryDevicePortStatus": memoryDevicePortStatus,
       "memoryDevicePortSecurityState": memoryDevicePortSecurityState,
       "memoryDevicePortConnectorType": memoryDevicePortConnectorType,
       "memoryDevicePortName": memoryDevicePortName,
       "memoryDevicePortBIOSConnectorType": memoryDevicePortBIOSConnectorType,
       "memoryDevicePortPhysicalMemoryArrayIndexReference": memoryDevicePortPhysicalMemoryArrayIndexReference,
       "memoryDevicePortPhysicalMemoryCardIndexReference": memoryDevicePortPhysicalMemoryCardIndexReference,
       "monitorPortTable": monitorPortTable,
       "monitorPortTableEntry": monitorPortTableEntry,
       "monitorPortchassisIndex": monitorPortchassisIndex,
       "monitorPortIndex": monitorPortIndex,
       "monitorPortStateCapabilities": monitorPortStateCapabilities,
       "monitorPortStateSettings": monitorPortStateSettings,
       "monitorPortStatus": monitorPortStatus,
       "monitorPortSecurityState": monitorPortSecurityState,
       "monitorPortConnectorType": monitorPortConnectorType,
       "monitorPortName": monitorPortName,
       "monitorPortBIOSConnectorType": monitorPortBIOSConnectorType,
       "sCSIPortTable": sCSIPortTable,
       "sCSIPortTableEntry": sCSIPortTableEntry,
       "sCSIPortchassisIndex": sCSIPortchassisIndex,
       "sCSIPortIndex": sCSIPortIndex,
       "sCSIPortStateCapabilities": sCSIPortStateCapabilities,
       "sCSIPortStateSettings": sCSIPortStateSettings,
       "sCSIPortStatus": sCSIPortStatus,
       "sCSIPortSecurityState": sCSIPortSecurityState,
       "sCSIPortConnectorType": sCSIPortConnectorType,
       "sCSIPortName": sCSIPortName,
       "sCSIPortBIOSConnectorType": sCSIPortBIOSConnectorType,
       "parallelPortTable": parallelPortTable,
       "parallelPortTableEntry": parallelPortTableEntry,
       "parallelPortchassisIndex": parallelPortchassisIndex,
       "parallelPortIndex": parallelPortIndex,
       "parallelPortStateCapabilities": parallelPortStateCapabilities,
       "parallelPortStateSettings": parallelPortStateSettings,
       "parallelPortStatus": parallelPortStatus,
       "parallelPortSecurityState": parallelPortSecurityState,
       "parallelPortConnectorType": parallelPortConnectorType,
       "parallelPortName": parallelPortName,
       "parallelPortConnectorPinOut": parallelPortConnectorPinOut,
       "parallelPortCapabilitiesUnique": parallelPortCapabilitiesUnique,
       "parallelPortBaseIOAddress": parallelPortBaseIOAddress,
       "parallelPortIRQLevel": parallelPortIRQLevel,
       "parallelPortDMASupport": parallelPortDMASupport,
       "serialPortTable": serialPortTable,
       "serialPortTableEntry": serialPortTableEntry,
       "serialPortchassisIndex": serialPortchassisIndex,
       "serialPortIndex": serialPortIndex,
       "serialPortStateCapabilities": serialPortStateCapabilities,
       "serialPortStateSettings": serialPortStateSettings,
       "serialPortStatus": serialPortStatus,
       "serialPortSecurityState": serialPortSecurityState,
       "serialPortConnectorType": serialPortConnectorType,
       "serialPortName": serialPortName,
       "serialPortMaximumSpeed": serialPortMaximumSpeed,
       "serialPortCapabilitiesUnique": serialPortCapabilitiesUnique,
       "serialPortBaseIOAddress": serialPortBaseIOAddress,
       "serialPortIRQLevel": serialPortIRQLevel,
       "uSBPortTable": uSBPortTable,
       "uSBPortTableEntry": uSBPortTableEntry,
       "uSBPortchassisIndex": uSBPortchassisIndex,
       "uSBPortIndex": uSBPortIndex,
       "uSBPortStateCapabilities": uSBPortStateCapabilities,
       "uSBPortStateSettings": uSBPortStateSettings,
       "uSBPortStatus": uSBPortStatus,
       "uSBPortSecurityState": uSBPortSecurityState,
       "uSBPortConnectorType": uSBPortConnectorType,
       "uSBPortName": uSBPortName,
       "uSBPortBIOSConnectorType": uSBPortBIOSConnectorType,
       "deviceGroup": deviceGroup,
       "pointingDeviceTable": pointingDeviceTable,
       "pointingDeviceTableEntry": pointingDeviceTableEntry,
       "pointingDevicechassisIndex": pointingDevicechassisIndex,
       "pointingDeviceIndex": pointingDeviceIndex,
       "pointingDeviceStateCapabilities": pointingDeviceStateCapabilities,
       "pointingDeviceStateSettings": pointingDeviceStateSettings,
       "pointingDeviceStatus": pointingDeviceStatus,
       "pointingPortIndexReference": pointingPortIndexReference,
       "pointingDeviceType": pointingDeviceType,
       "pointingDeviceNumberofButtons": pointingDeviceNumberofButtons,
       "keyboardDeviceTable": keyboardDeviceTable,
       "keyboardDeviceTableEntry": keyboardDeviceTableEntry,
       "keyboardDevicechassisIndex": keyboardDevicechassisIndex,
       "keyboardDeviceIndex": keyboardDeviceIndex,
       "keyboardDeviceStateCapabilities": keyboardDeviceStateCapabilities,
       "keyboardDeviceStateSettings": keyboardDeviceStateSettings,
       "keyboardDeviceStatus": keyboardDeviceStatus,
       "keyboardPortIndexReference": keyboardPortIndexReference,
       "keyboardDeviceTypeName": keyboardDeviceTypeName,
       "keyboardDeviceLayoutName": keyboardDeviceLayoutName,
       "processorDeviceTable": processorDeviceTable,
       "processorDeviceTableEntry": processorDeviceTableEntry,
       "processorDevicechassisIndex": processorDevicechassisIndex,
       "processorDeviceIndex": processorDeviceIndex,
       "processorDeviceStateCapabilities": processorDeviceStateCapabilities,
       "processorDeviceStateSettings": processorDeviceStateSettings,
       "processorDeviceStatus": processorDeviceStatus,
       "processorPortIndexReference": processorPortIndexReference,
       "processorDeviceType": processorDeviceType,
       "processorDeviceManufacturerName": processorDeviceManufacturerName,
       "processorDeviceStatusState": processorDeviceStatusState,
       "processorDeviceFamily": processorDeviceFamily,
       "processorDeviceMaximumSpeed": processorDeviceMaximumSpeed,
       "processorDeviceCurrentSpeed": processorDeviceCurrentSpeed,
       "processorDeviceExternalClockSpeed": processorDeviceExternalClockSpeed,
       "processorDeviceVoltage": processorDeviceVoltage,
       "processorDeviceUpgradeInformation": processorDeviceUpgradeInformation,
       "processorDeviceVersionName": processorDeviceVersionName,
       "processorDeviceCoreCount": processorDeviceCoreCount,
       "processorDeviceCoreEnabledCount": processorDeviceCoreEnabledCount,
       "processorDeviceThreadCount": processorDeviceThreadCount,
       "processorDeviceCharacteristics": processorDeviceCharacteristics,
       "processorDeviceExtendedCapabilities": processorDeviceExtendedCapabilities,
       "processorDeviceExtendedSettings": processorDeviceExtendedSettings,
       "processorDeviceBrandName": processorDeviceBrandName,
       "processorDeviceModelName": processorDeviceModelName,
       "processorDeviceSteppingName": processorDeviceSteppingName,
       "processorDeviceDeprecatedCapabilities": processorDeviceDeprecatedCapabilities,
       "processorDeviceStatusTable": processorDeviceStatusTable,
       "processorDeviceStatusTableEntry": processorDeviceStatusTableEntry,
       "processorDeviceStatusChassisIndex": processorDeviceStatusChassisIndex,
       "processorDeviceStatusIndex": processorDeviceStatusIndex,
       "processorDeviceStatusStateCapabilities": processorDeviceStatusStateCapabilities,
       "processorDeviceStatusStateSettings": processorDeviceStatusStateSettings,
       "processorDeviceStatusStatus": processorDeviceStatusStatus,
       "processorDeviceStatusReading": processorDeviceStatusReading,
       "processorDeviceStatusLocationName": processorDeviceStatusLocationName,
       "processorDeviceStatusPortIndexReference": processorDeviceStatusPortIndexReference,
       "cacheDeviceTable": cacheDeviceTable,
       "cacheDeviceTableEntry": cacheDeviceTableEntry,
       "cacheDevicechassisIndex": cacheDevicechassisIndex,
       "cacheDeviceIndex": cacheDeviceIndex,
       "cacheDeviceStateCapabilities": cacheDeviceStateCapabilities,
       "cacheDeviceStateSettings": cacheDeviceStateSettings,
       "cacheDeviceStatus": cacheDeviceStatus,
       "cacheDeviceprocessorDeviceIndexReference": cacheDeviceprocessorDeviceIndexReference,
       "cacheDeviceType": cacheDeviceType,
       "cacheDeviceLocation": cacheDeviceLocation,
       "cacheDeviceStatusState": cacheDeviceStatusState,
       "cacheDeviceExternalSocketName": cacheDeviceExternalSocketName,
       "cacheDeviceLevel": cacheDeviceLevel,
       "cacheDeviceMaximumSize": cacheDeviceMaximumSize,
       "cacheDeviceCurrentSize": cacheDeviceCurrentSize,
       "cacheDeviceSpeed": cacheDeviceSpeed,
       "cacheDeviceWritePolicy": cacheDeviceWritePolicy,
       "cacheDeviceIsSocketed": cacheDeviceIsSocketed,
       "cacheDeviceECCType": cacheDeviceECCType,
       "cacheDeviceAssociativity": cacheDeviceAssociativity,
       "cacheDeviceSupportedType": cacheDeviceSupportedType,
       "cacheDeviceCurrentType": cacheDeviceCurrentType,
       "memoryDeviceTable": memoryDeviceTable,
       "memoryDeviceTableEntry": memoryDeviceTableEntry,
       "memoryDevicechassisIndex": memoryDevicechassisIndex,
       "memoryDeviceIndex": memoryDeviceIndex,
       "memoryDeviceStateCapabilities": memoryDeviceStateCapabilities,
       "memoryDeviceStateSettings": memoryDeviceStateSettings,
       "memoryDeviceStatus": memoryDeviceStatus,
       "memoryDeviceMemoryPortIndexReference": memoryDeviceMemoryPortIndexReference,
       "memoryDeviceType": memoryDeviceType,
       "memoryDeviceLocationName": memoryDeviceLocationName,
       "memoryDeviceErrorCount": memoryDeviceErrorCount,
       "memoryDeviceBankLocationName": memoryDeviceBankLocationName,
       "memoryDeviceTypeDetails": memoryDeviceTypeDetails,
       "memoryDeviceFormFactor": memoryDeviceFormFactor,
       "memoryDeviceSet": memoryDeviceSet,
       "memoryDeviceSize": memoryDeviceSize,
       "memoryDeviceSpeed": memoryDeviceSpeed,
       "memoryDeviceTotalBusWidth": memoryDeviceTotalBusWidth,
       "memoryDeviceTotalDataBusWidth": memoryDeviceTotalDataBusWidth,
       "memoryDeviceSingleBitErrorCount": memoryDeviceSingleBitErrorCount,
       "memoryDeviceMultiBitErrorCount": memoryDeviceMultiBitErrorCount,
       "memoryDeviceFailureModes": memoryDeviceFailureModes,
       "memoryDeviceManufacturerName": memoryDeviceManufacturerName,
       "memoryDevicePartNumberName": memoryDevicePartNumberName,
       "memoryDeviceSerialNumberName": memoryDeviceSerialNumberName,
       "memoryDeviceAssetTagName": memoryDeviceAssetTagName,
       "memoryDeviceSpeedName": memoryDeviceSpeedName,
       "memoryDeviceRank": memoryDeviceRank,
       "memoryDeviceExtendedSize": memoryDeviceExtendedSize,
       "memoryDeviceMemoryTechnology": memoryDeviceMemoryTechnology,
       "memoryDeviceNonVolatileSize": memoryDeviceNonVolatileSize,
       "memoryDeviceVolatileSize": memoryDeviceVolatileSize,
       "memoryDeviceCacheSize": memoryDeviceCacheSize,
       "memoryDeviceWearLevel": memoryDeviceWearLevel,
       "memoryDeviceMappedAddressTable": memoryDeviceMappedAddressTable,
       "memoryDeviceMappedAddressTableEntry": memoryDeviceMappedAddressTableEntry,
       "memoryDeviceMappedAddresschassisIndex": memoryDeviceMappedAddresschassisIndex,
       "memoryDeviceMappedAddressIndex": memoryDeviceMappedAddressIndex,
       "memoryDeviceMappedAddressStateCapabilities": memoryDeviceMappedAddressStateCapabilities,
       "memoryDeviceMappedAddressStateSettings": memoryDeviceMappedAddressStateSettings,
       "memoryDeviceMappedAddressStatus": memoryDeviceMappedAddressStatus,
       "memoryDeviceIndexReference": memoryDeviceIndexReference,
       "memoryDeviceMappedAddressRowPosition": memoryDeviceMappedAddressRowPosition,
       "memoryDeviceMappedAddressInterleavePosition": memoryDeviceMappedAddressInterleavePosition,
       "memoryDeviceMappedAddressInterleaveDepth": memoryDeviceMappedAddressInterleaveDepth,
       "memoryDeviceMappedAddressStartingAddress": memoryDeviceMappedAddressStartingAddress,
       "memoryDeviceMappedAddressEndingAddress": memoryDeviceMappedAddressEndingAddress,
       "genericDeviceTable": genericDeviceTable,
       "genericDeviceTableEntry": genericDeviceTableEntry,
       "genericDevicechassisIndex": genericDevicechassisIndex,
       "genericDeviceIndex": genericDeviceIndex,
       "genericDeviceStateCapabilities": genericDeviceStateCapabilities,
       "genericDeviceStateSettings": genericDeviceStateSettings,
       "genericDeviceStatus": genericDeviceStatus,
       "genericDeviceSystemSlotIndexReference": genericDeviceSystemSlotIndexReference,
       "genericDeviceType": genericDeviceType,
       "genericDeviceName": genericDeviceName,
       "pCIDeviceTable": pCIDeviceTable,
       "pCIDeviceTableEntry": pCIDeviceTableEntry,
       "pCIDevicechassisIndex": pCIDevicechassisIndex,
       "pCIDeviceIndex": pCIDeviceIndex,
       "pCIDeviceStateCapabilities": pCIDeviceStateCapabilities,
       "pCIDeviceStateSettings": pCIDeviceStateSettings,
       "pCIDeviceStatus": pCIDeviceStatus,
       "pCIDeviceSystemSlotIndexReference": pCIDeviceSystemSlotIndexReference,
       "pCIDeviceDataBusWidth": pCIDeviceDataBusWidth,
       "pCIDeviceManufacturerName": pCIDeviceManufacturerName,
       "pCIDeviceDescriptionName": pCIDeviceDescriptionName,
       "pCIDeviceSpeed": pCIDeviceSpeed,
       "pCIDeviceAdapterFault": pCIDeviceAdapterFault,
       "pCIDeviceConfigurationSpaceTable": pCIDeviceConfigurationSpaceTable,
       "pCIDeviceConfigurationSpaceTableEntry": pCIDeviceConfigurationSpaceTableEntry,
       "pCIDeviceConfigurationSpacechassisIndex": pCIDeviceConfigurationSpacechassisIndex,
       "pCIDeviceConfigurationSpaceIndex": pCIDeviceConfigurationSpaceIndex,
       "pCIDeviceConfigurationSpaceStateCapabilities": pCIDeviceConfigurationSpaceStateCapabilities,
       "pCIDeviceConfigurationSpaceStateSettings": pCIDeviceConfigurationSpaceStateSettings,
       "pCIDeviceConfigurationSpaceStatus": pCIDeviceConfigurationSpaceStatus,
       "pCIDeviceIndexReference": pCIDeviceIndexReference,
       "pCIDeviceConfigurationSpaceBusNumber": pCIDeviceConfigurationSpaceBusNumber,
       "pCIDeviceConfigurationSpaceDeviceNumber": pCIDeviceConfigurationSpaceDeviceNumber,
       "pCIDeviceConfigurationSpaceFunctionNumber": pCIDeviceConfigurationSpaceFunctionNumber,
       "pCIDeviceConfigurationSpaceHeader": pCIDeviceConfigurationSpaceHeader,
       "networkDeviceTable": networkDeviceTable,
       "networkDeviceTableEntry": networkDeviceTableEntry,
       "networkDeviceChassisIndex": networkDeviceChassisIndex,
       "networkDeviceIndex": networkDeviceIndex,
       "networkDeviceStatus": networkDeviceStatus,
       "networkDeviceConnectionStatus": networkDeviceConnectionStatus,
       "networkDeviceDescriptionName": networkDeviceDescriptionName,
       "networkDeviceProductName": networkDeviceProductName,
       "networkDeviceVendorName": networkDeviceVendorName,
       "networkDeviceServiceName": networkDeviceServiceName,
       "networkDeviceDriverImagePathName": networkDeviceDriverImagePathName,
       "networkDeviceDriverVersionName": networkDeviceDriverVersionName,
       "networkDeviceIPAddress": networkDeviceIPAddress,
       "networkDeviceIPSubnetMask": networkDeviceIPSubnetMask,
       "networkDeviceDefaultGatewayIPAddress": networkDeviceDefaultGatewayIPAddress,
       "networkDeviceDHCPServerIPAddress": networkDeviceDHCPServerIPAddress,
       "networkDeviceCurrentMACAddress": networkDeviceCurrentMACAddress,
       "networkDevicePermanentMACAddress": networkDevicePermanentMACAddress,
       "networkDevicePCIBusNumber": networkDevicePCIBusNumber,
       "networkDevicePCIDeviceNumber": networkDevicePCIDeviceNumber,
       "networkDevicePCIFunctionNumber": networkDevicePCIFunctionNumber,
       "networkDeviceIRQ": networkDeviceIRQ,
       "networkDeviceBaseIOPortAddress": networkDeviceBaseIOPortAddress,
       "networkDeviceTeamingFlags": networkDeviceTeamingFlags,
       "networkDeviceTOECapabilityFlags": networkDeviceTOECapabilityFlags,
       "networkDeviceTOEEnabled": networkDeviceTOEEnabled,
       "networkDeviceRDMACapabilityFlags": networkDeviceRDMACapabilityFlags,
       "networkDeviceRDMAEnabled": networkDeviceRDMAEnabled,
       "networkDeviceiSCSICapabilityFlags": networkDeviceiSCSICapabilityFlags,
       "networkDeviceiSCSIEnabled": networkDeviceiSCSIEnabled,
       "networkDeviceCapabilities": networkDeviceCapabilities,
       "networkDeviceNParEPEnabled": networkDeviceNParEPEnabled,
       "managedSystemServicesDeviceTable": managedSystemServicesDeviceTable,
       "managedSystemServicesDeviceTableEntry": managedSystemServicesDeviceTableEntry,
       "managedSystemServicesDeviceChassisIndex": managedSystemServicesDeviceChassisIndex,
       "managedSystemServicesDeviceIndex": managedSystemServicesDeviceIndex,
       "managedSystemServicesDeviceStatus": managedSystemServicesDeviceStatus,
       "managedSystemServicesDeviceType": managedSystemServicesDeviceType,
       "managedSystemServicesDeviceStoragePresent": managedSystemServicesDeviceStoragePresent,
       "managedSystemServicesDeviceStorageSize": managedSystemServicesDeviceStorageSize,
       "sdCardUnitTable": sdCardUnitTable,
       "sdCardUnitTableEntry": sdCardUnitTableEntry,
       "sdCardUnitChassisIndex": sdCardUnitChassisIndex,
       "sdCardUnitIndex": sdCardUnitIndex,
       "sdCardUnitStateCapabilities": sdCardUnitStateCapabilities,
       "sdCardUnitStateSettings": sdCardUnitStateSettings,
       "sdCardUnitRedundancyStatus": sdCardUnitRedundancyStatus,
       "sdCardUnitCountForRedundancy": sdCardUnitCountForRedundancy,
       "sdCardUnitName": sdCardUnitName,
       "sdCardUnitStatus": sdCardUnitStatus,
       "sdCardDeviceTable": sdCardDeviceTable,
       "sdCardDeviceTableEntry": sdCardDeviceTableEntry,
       "sdCardDeviceChassisIndex": sdCardDeviceChassisIndex,
       "sdCardDeviceIndex": sdCardDeviceIndex,
       "sdCardDeviceStatus": sdCardDeviceStatus,
       "sdCardDeviceType": sdCardDeviceType,
       "sdCardDeviceConfigCapabilities": sdCardDeviceConfigCapabilities,
       "sdCardDeviceConfigSettings": sdCardDeviceConfigSettings,
       "sdCardDeviceLocationName": sdCardDeviceLocationName,
       "sdCardDeviceCardPresent": sdCardDeviceCardPresent,
       "sdCardDeviceCardState": sdCardDeviceCardState,
       "sdCardDeviceCardStorageSize": sdCardDeviceCardStorageSize,
       "sdCardDeviceUnitIndexReference": sdCardDeviceUnitIndexReference,
       "sdCardDeviceCardAvailableStorageSize": sdCardDeviceCardAvailableStorageSize,
       "sdCardDeviceCardLicensed": sdCardDeviceCardLicensed,
       "slotGroup": slotGroup,
       "systemSlotTable": systemSlotTable,
       "systemSlotTableEntry": systemSlotTableEntry,
       "systemSlotchassisIndex": systemSlotchassisIndex,
       "systemSlotIndex": systemSlotIndex,
       "systemSlotStateCapabilitiesUnique": systemSlotStateCapabilitiesUnique,
       "systemSlotStateSettingsUnique": systemSlotStateSettingsUnique,
       "systemSlotStatus": systemSlotStatus,
       "systemSlotCurrentUsage": systemSlotCurrentUsage,
       "systemSlotType": systemSlotType,
       "systemSlotSlotExternalSlotName": systemSlotSlotExternalSlotName,
       "systemSlotLength": systemSlotLength,
       "systemSlotSlotID": systemSlotSlotID,
       "systemSlotCategory": systemSlotCategory,
       "systemSlotHotPlugBusWidth": systemSlotHotPlugBusWidth,
       "systemSlotHotPlugSlotSpeed": systemSlotHotPlugSlotSpeed,
       "systemSlotHotPlugAdapterSpeed": systemSlotHotPlugAdapterSpeed,
       "memoryGroup": memoryGroup,
       "physicalMemoryArrayTable": physicalMemoryArrayTable,
       "physicalMemoryArrayTableEntry": physicalMemoryArrayTableEntry,
       "physicalMemoryArraychassisIndex": physicalMemoryArraychassisIndex,
       "physicalMemoryArrayIndex": physicalMemoryArrayIndex,
       "physicalMemoryArrayStateCapabilities": physicalMemoryArrayStateCapabilities,
       "physicalMemoryArrayStateSettings": physicalMemoryArrayStateSettings,
       "physicalMemoryArrayStatus": physicalMemoryArrayStatus,
       "physicalMemoryArrayUse": physicalMemoryArrayUse,
       "physicalMemoryArrayECCType": physicalMemoryArrayECCType,
       "physicalMemoryArrayLocation": physicalMemoryArrayLocation,
       "physicalMemoryArrayMaximumSize": physicalMemoryArrayMaximumSize,
       "physicalMemoryArrayTotalNumberSockets": physicalMemoryArrayTotalNumberSockets,
       "physicalMemoryArrayInUseNumberSockets": physicalMemoryArrayInUseNumberSockets,
       "physicalMemoryArrayECCErrorNonRecoverableThreshold": physicalMemoryArrayECCErrorNonRecoverableThreshold,
       "physicalMemoryArrayECCErrorCriticalThreshold": physicalMemoryArrayECCErrorCriticalThreshold,
       "physicalMemoryArrayECCErrorNonCriticalThreshold": physicalMemoryArrayECCErrorNonCriticalThreshold,
       "physicalMemoryArrayRedundantMemoryUnitIndexReference": physicalMemoryArrayRedundantMemoryUnitIndexReference,
       "physicalMemoryArrayExtendedMaximumSize": physicalMemoryArrayExtendedMaximumSize,
       "physicalMemoryArrayMappedTable": physicalMemoryArrayMappedTable,
       "physicalMemoryArrayMappedTableEntry": physicalMemoryArrayMappedTableEntry,
       "physicalMemoryArrayMappedchassisIndex": physicalMemoryArrayMappedchassisIndex,
       "physicalMemoryArrayMappedIndex": physicalMemoryArrayMappedIndex,
       "physicalMemoryArrayMappedStateCapabilities": physicalMemoryArrayMappedStateCapabilities,
       "physicalMemoryArrayMappedStateSettings": physicalMemoryArrayMappedStateSettings,
       "physicalMemoryArrayMappedStatus": physicalMemoryArrayMappedStatus,
       "physicalMemoryArrayIndexReference": physicalMemoryArrayIndexReference,
       "physicalMemoryArrayMappedStartingAddress": physicalMemoryArrayMappedStartingAddress,
       "physicalMemoryArrayMappedEndingAddress": physicalMemoryArrayMappedEndingAddress,
       "physicalMemoryArrayMappedPartitionWidth": physicalMemoryArrayMappedPartitionWidth,
       "physicalMemoryConfigTable": physicalMemoryConfigTable,
       "physicalMemoryConfigTableEntry": physicalMemoryConfigTableEntry,
       "physicalMemoryConfigChassisIndex": physicalMemoryConfigChassisIndex,
       "physicalMemoryConfigIndex": physicalMemoryConfigIndex,
       "physicalMemoryConfigStateCapabilities": physicalMemoryConfigStateCapabilities,
       "physicalMemoryConfigStateSettings": physicalMemoryConfigStateSettings,
       "physicalMemoryConfigStatus": physicalMemoryConfigStatus,
       "physicalMemoryConfigRedundantCapabilities": physicalMemoryConfigRedundantCapabilities,
       "physicalMemoryConfigRedundantSettings": physicalMemoryConfigRedundantSettings,
       "physicalMemoryConfigMOMCapabilities": physicalMemoryConfigMOMCapabilities,
       "physicalMemoryConfigMOMSettings": physicalMemoryConfigMOMSettings,
       "physicalMemoryLoggingTable": physicalMemoryLoggingTable,
       "physicalMemoryLoggingTableEntry": physicalMemoryLoggingTableEntry,
       "physicalMemoryLoggingChassisIndex": physicalMemoryLoggingChassisIndex,
       "physicalMemoryLoggingIndex": physicalMemoryLoggingIndex,
       "physicalMemoryLoggingCapabilities": physicalMemoryLoggingCapabilities,
       "physicalMemoryLoggingSettings": physicalMemoryLoggingSettings,
       "physicalMemoryLoggingStatus": physicalMemoryLoggingStatus,
       "redundantMemoryUnitTable": redundantMemoryUnitTable,
       "redundantMemoryUnitTableEntry": redundantMemoryUnitTableEntry,
       "redundantMemoryUnitChassisIndex": redundantMemoryUnitChassisIndex,
       "redundantMemoryUnitIndex": redundantMemoryUnitIndex,
       "redundantMemoryUnitStateCapabilities": redundantMemoryUnitStateCapabilities,
       "redundantMemoryUnitStateSettings": redundantMemoryUnitStateSettings,
       "redundantMemoryUnitRedundancyStatus": redundantMemoryUnitRedundancyStatus,
       "redundantMemoryUnitName": redundantMemoryUnitName,
       "redundantMemoryUnitStatus": redundantMemoryUnitStatus,
       "physicalMemoryCardTable": physicalMemoryCardTable,
       "physicalMemoryCardTableEntry": physicalMemoryCardTableEntry,
       "physicalMemoryCardChassisIndex": physicalMemoryCardChassisIndex,
       "physicalMemoryCardIndex": physicalMemoryCardIndex,
       "physicalMemoryCardStateCapabilities": physicalMemoryCardStateCapabilities,
       "physicalMemoryCardStateSettings": physicalMemoryCardStateSettings,
       "physicalMemoryCardStatus": physicalMemoryCardStatus,
       "physicalMemoryCardName": physicalMemoryCardName,
       "physicalMemoryCardTotalNumberSockets": physicalMemoryCardTotalNumberSockets,
       "physicalMemoryCardInUseNumberSockets": physicalMemoryCardInUseNumberSockets,
       "physicalMemoryCardPhyMemArrayIndexReference": physicalMemoryCardPhyMemArrayIndexReference,
       "biosSetUpControlGroup": biosSetUpControlGroup,
       "biosSetUpControlTable": biosSetUpControlTable,
       "biosSetUpControlTableEntry": biosSetUpControlTableEntry,
       "biosSetUpControlchassisIndex": biosSetUpControlchassisIndex,
       "bSUCpointingDeviceControlCapabilities": bSUCpointingDeviceControlCapabilities,
       "bSUCpointingDeviceControlSettings": bSUCpointingDeviceControlSettings,
       "bSUCpointingDeviceControlStatus": bSUCpointingDeviceControlStatus,
       "bSUCpointingDeviceControlName": bSUCpointingDeviceControlName,
       "bSUCnumLockControlCapabilities": bSUCnumLockControlCapabilities,
       "bSUCnumLockControlSettings": bSUCnumLockControlSettings,
       "bSUCnumLockControlStatus": bSUCnumLockControlStatus,
       "bSUCnumLockControlName": bSUCnumLockControlName,
       "bSUCprocessorSerialNumberControlCapabilities": bSUCprocessorSerialNumberControlCapabilities,
       "bSUCprocessorSerialNumberControlSettings": bSUCprocessorSerialNumberControlSettings,
       "bSUCprocessorSerialNumberControlStatus": bSUCprocessorSerialNumberControlStatus,
       "bSUCprocessorSerialNumberControlName": bSUCprocessorSerialNumberControlName,
       "bSUCspeakerControlCapabilitiesUnique": bSUCspeakerControlCapabilitiesUnique,
       "bSUCspeakerControlSettingsUnique": bSUCspeakerControlSettingsUnique,
       "bSUCspeakerControlStatus": bSUCspeakerControlStatus,
       "bSUCspeakerControlName": bSUCspeakerControlName,
       "bSUCnIFwakeonLanControlCapabilitiesUnique": bSUCnIFwakeonLanControlCapabilitiesUnique,
       "bSUCnIFwakeonLanControlSettingsUnique": bSUCnIFwakeonLanControlSettingsUnique,
       "bSUCnIFwakeonLanControlStatus": bSUCnIFwakeonLanControlStatus,
       "bSUCnIFwakeonLanControlName": bSUCnIFwakeonLanControlName,
       "bSUCbootSequenceControlCapabilitiesUnique": bSUCbootSequenceControlCapabilitiesUnique,
       "bSUCbootSequenceControlSettingsUnique": bSUCbootSequenceControlSettingsUnique,
       "bSUCbootSequenceControlStatus": bSUCbootSequenceControlStatus,
       "bSUCbootSequenceControlName": bSUCbootSequenceControlName,
       "bSUCadministratorPasswordControlCapabilitiesUnique": bSUCadministratorPasswordControlCapabilitiesUnique,
       "bSUCadministratorPasswordControlSettingsUnique": bSUCadministratorPasswordControlSettingsUnique,
       "bSUCadministratorPasswordControlStatus": bSUCadministratorPasswordControlStatus,
       "bSUCadministratorPasswordPasswordVerifyName": bSUCadministratorPasswordPasswordVerifyName,
       "bSUCadministratorPasswordNewPasswordName": bSUCadministratorPasswordNewPasswordName,
       "bSUCuserPasswordControlCapabilitiesUnique": bSUCuserPasswordControlCapabilitiesUnique,
       "bSUCuserPasswordControlSettingsUnique": bSUCuserPasswordControlSettingsUnique,
       "bSUCuserPasswordControlStatus": bSUCuserPasswordControlStatus,
       "bSUCuserPasswordPasswordVerifyName": bSUCuserPasswordPasswordVerifyName,
       "bSUCuserPasswordNewPasswordName": bSUCuserPasswordNewPasswordName,
       "bSUCtpmSecurityControlCapabilities": bSUCtpmSecurityControlCapabilities,
       "bSUCtpmSecurityControlSetting": bSUCtpmSecurityControlSetting,
       "bSUCtpmSecurityControlStatus": bSUCtpmSecurityControlStatus,
       "bSUCtpmSecurityControlName": bSUCtpmSecurityControlName,
       "sCSIControlTable": sCSIControlTable,
       "sCSIControlTableEntry": sCSIControlTableEntry,
       "sCSIControlchassisIndex": sCSIControlchassisIndex,
       "sCSIControlIndex": sCSIControlIndex,
       "sCSIControlCapabilities": sCSIControlCapabilities,
       "sCSIControlSettings": sCSIControlSettings,
       "sCSIControlStatus": sCSIControlStatus,
       "sCSIControlName": sCSIControlName,
       "parallelPortControlTable": parallelPortControlTable,
       "parallelPortControlTableEntry": parallelPortControlTableEntry,
       "parallelPortControlchassisIndex": parallelPortControlchassisIndex,
       "parallelPortControlIndex": parallelPortControlIndex,
       "parallelPortControlCapabilitiesUnique": parallelPortControlCapabilitiesUnique,
       "parallelPortControlSettingsUnique": parallelPortControlSettingsUnique,
       "parallelPortControlStatus": parallelPortControlStatus,
       "parallelPortControlName": parallelPortControlName,
       "parallelPortControlModeCapabilitiesUnique": parallelPortControlModeCapabilitiesUnique,
       "parallelPortControlModeSettingsUnique": parallelPortControlModeSettingsUnique,
       "serialPortControlTable": serialPortControlTable,
       "serialPortControlTableEntry": serialPortControlTableEntry,
       "serialPortControlchassisIndex": serialPortControlchassisIndex,
       "serialPortControlIndex": serialPortControlIndex,
       "serialPortControlCapabilitiesUnique": serialPortControlCapabilitiesUnique,
       "serialPortControlSettingsUnique": serialPortControlSettingsUnique,
       "serialPortControlStatus": serialPortControlStatus,
       "serialPortControlName": serialPortControlName,
       "usbControlTable": usbControlTable,
       "usbControlTableEntry": usbControlTableEntry,
       "usbControlchassisIndex": usbControlchassisIndex,
       "usbControlIndex": usbControlIndex,
       "usbControlCapabilities": usbControlCapabilities,
       "usbControlSettings": usbControlSettings,
       "usbControlStatus": usbControlStatus,
       "usbControlName": usbControlName,
       "ideControlTable": ideControlTable,
       "ideControlTableEntry": ideControlTableEntry,
       "ideControlchassisIndex": ideControlchassisIndex,
       "ideControlIndex": ideControlIndex,
       "ideControlCapabilitiesUnique": ideControlCapabilitiesUnique,
       "ideControlSettingsUnique": ideControlSettingsUnique,
       "ideControlStatus": ideControlStatus,
       "ideControlName": ideControlName,
       "disketteControlTable": disketteControlTable,
       "disketteControlTableEntry": disketteControlTableEntry,
       "disketteControlchassisIndex": disketteControlchassisIndex,
       "disketteControlIndex": disketteControlIndex,
       "disketteControlCapabilitiesUnique": disketteControlCapabilitiesUnique,
       "disketteControlSettingsUnique": disketteControlSettingsUnique,
       "disketteControlStatus": disketteControlStatus,
       "disketteControlName": disketteControlName,
       "networkInterfaceControlTable": networkInterfaceControlTable,
       "networkInterfaceControlTableEntry": networkInterfaceControlTableEntry,
       "networkInterfaceControlchassisIndex": networkInterfaceControlchassisIndex,
       "networkInterfaceControlIndex": networkInterfaceControlIndex,
       "networkInterfaceControlCapabilitiesUnique": networkInterfaceControlCapabilitiesUnique,
       "networkInterfaceControlSettingsUnique": networkInterfaceControlSettingsUnique,
       "networkInterfaceControlStatus": networkInterfaceControlStatus,
       "networkInterfaceControlName": networkInterfaceControlName,
       "biosSettingTable": biosSettingTable,
       "biosSettingTableEntry": biosSettingTableEntry,
       "biosSettingChassisIndex": biosSettingChassisIndex,
       "biosSettingIndex": biosSettingIndex,
       "biosSettingName": biosSettingName,
       "biosSettingDisplayName": biosSettingDisplayName,
       "biosSettingValueType": biosSettingValueType,
       "biosSettingCurrentValue": biosSettingCurrentValue,
       "biosSettingPendingValue": biosSettingPendingValue,
       "biosSettingDefaultValue": biosSettingDefaultValue,
       "biosSettingPossibleValues": biosSettingPossibleValues,
       "biosSettingDisplayOrder": biosSettingDisplayOrder,
       "biosSettingGroupDisplayName": biosSettingGroupDisplayName,
       "biosSettingFQDD": biosSettingFQDD,
       "lraGroup": lraGroup,
       "lRAGlobalSettingsTable": lRAGlobalSettingsTable,
       "lRAGlobalSettingsTableEntry": lRAGlobalSettingsTableEntry,
       "lRAGlobalchassisIndex": lRAGlobalchassisIndex,
       "lRAGlobalState": lRAGlobalState,
       "lRAGlobalSettingsDisableTimeoutValue": lRAGlobalSettingsDisableTimeoutValue,
       "lRAGlobalSettingsCapabilitiesUnique": lRAGlobalSettingsCapabilitiesUnique,
       "lRAGlobalThermalShutdownCapabilitiesUnique": lRAGlobalThermalShutdownCapabilitiesUnique,
       "lRAGlobalThermalShutdownStateSettingsUnique": lRAGlobalThermalShutdownStateSettingsUnique,
       "lRAActionTableTable": lRAActionTableTable,
       "lRAActionTableTableEntry": lRAActionTableTableEntry,
       "lRAActionTablechassisIndex": lRAActionTablechassisIndex,
       "lRAActionTableActionNumberIndex": lRAActionTableActionNumberIndex,
       "lRAActionTableUserApplicationName": lRAActionTableUserApplicationName,
       "lRAActionTableSettingsUnique": lRAActionTableSettingsUnique,
       "cooGroup": cooGroup,
       "cooTable": cooTable,
       "cooTableEntry": cooTableEntry,
       "coochassisIndex": coochassisIndex,
       "cooState": cooState,
       "cooAquisitionPurchaseCost": cooAquisitionPurchaseCost,
       "cooAquisitionWayBillNumber": cooAquisitionWayBillNumber,
       "cooAquisitionInstallDateName": cooAquisitionInstallDateName,
       "cooAquisitionPurchaseOrder": cooAquisitionPurchaseOrder,
       "cooAquisitionPurchaseDateName": cooAquisitionPurchaseDateName,
       "cooAquisitionSigningAuthorityName": cooAquisitionSigningAuthorityName,
       "cooOriginalMachineConfigurationExpensed": cooOriginalMachineConfigurationExpensed,
       "cooOriginalMachineConfigurationVendorName": cooOriginalMachineConfigurationVendorName,
       "cooCostCenterInformationVendorName": cooCostCenterInformationVendorName,
       "cooUserInformationUserName": cooUserInformationUserName,
       "cooExtendedWarrantyStartDateName": cooExtendedWarrantyStartDateName,
       "cooExtendedWarrantyEndDateName": cooExtendedWarrantyEndDateName,
       "cooExtendedWarrantyCost": cooExtendedWarrantyCost,
       "cooExtendedWarrantyProviderName": cooExtendedWarrantyProviderName,
       "cooOwnershipCode": cooOwnershipCode,
       "cooCorporateOwnerName": cooCorporateOwnerName,
       "cooHazardousWasteCodeName": cooHazardousWasteCodeName,
       "cooDeploymentDateLength": cooDeploymentDateLength,
       "cooDeploymentDurationType": cooDeploymentDurationType,
       "cooTrainingName": cooTrainingName,
       "cooOutsourcingProblemDescriptionName": cooOutsourcingProblemDescriptionName,
       "cooOutsourcingServiceFeeName": cooOutsourcingServiceFeeName,
       "cooOutsourcingSigningAuthorityName": cooOutsourcingSigningAuthorityName,
       "cooOutsourcingProviderFeeName": cooOutsourcingProviderFeeName,
       "cooOutsourcingProviderServiceLevelName": cooOutsourcingProviderServiceLevelName,
       "cooInsuranceCompanyName": cooInsuranceCompanyName,
       "cooBoxAssetTagName": cooBoxAssetTagName,
       "cooBoxSystemName": cooBoxSystemName,
       "cooBoxCPUSerialNumberName": cooBoxCPUSerialNumberName,
       "cooOperatingSystemUpgradeTypeName": cooOperatingSystemUpgradeTypeName,
       "cooOperatingSystemUpgradePatchLevelName": cooOperatingSystemUpgradePatchLevelName,
       "cooOperatingSystemUpgradeDate": cooOperatingSystemUpgradeDate,
       "cooDepreciationDuration": cooDepreciationDuration,
       "cooDepreciationDurationType": cooDepreciationDurationType,
       "cooDepreciationPercentage": cooDepreciationPercentage,
       "cooDepreciationMethodName": cooDepreciationMethodName,
       "cooRegistrationIsRegistered": cooRegistrationIsRegistered,
       "cooServiceContractTable": cooServiceContractTable,
       "cooServiceContractTableEntry": cooServiceContractTableEntry,
       "cooServiceContractchassisIndex": cooServiceContractchassisIndex,
       "cooServiceContractIndex": cooServiceContractIndex,
       "cooServiceContractState": cooServiceContractState,
       "cooServiceContractWasRenewed": cooServiceContractWasRenewed,
       "cooServiceContractTypeName": cooServiceContractTypeName,
       "cooServiceContractVendorName": cooServiceContractVendorName,
       "cooCostEventLogTable": cooCostEventLogTable,
       "cooCostEventLogTableEntry": cooCostEventLogTableEntry,
       "cooCostEventLogchassisIndex": cooCostEventLogchassisIndex,
       "cooCostEventLogIndex": cooCostEventLogIndex,
       "cooCostEventLogState": cooCostEventLogState,
       "cooCostEventLogDuration": cooCostEventLogDuration,
       "cooCostEventLogDurationType": cooCostEventLogDurationType,
       "cooCostEventLogDescriptionName": cooCostEventLogDescriptionName,
       "cooWarrantyTable": cooWarrantyTable,
       "cooWarrantyTableEntry": cooWarrantyTableEntry,
       "cooWarrantychassisIndex": cooWarrantychassisIndex,
       "cooWarrantyIndex": cooWarrantyIndex,
       "cooWarrantyState": cooWarrantyState,
       "cooWarrantyDuration": cooWarrantyDuration,
       "cooWarrantyDurationType": cooWarrantyDurationType,
       "cooWarrantyEndDateName": cooWarrantyEndDateName,
       "cooWarrantyCost": cooWarrantyCost,
       "cooLeaseInformationTable": cooLeaseInformationTable,
       "cooLeaseInformationTableEntry": cooLeaseInformationTableEntry,
       "cooLeaseInformationchassisIndex": cooLeaseInformationchassisIndex,
       "cooLeaseInformationIndex": cooLeaseInformationIndex,
       "cooLeaseInformationState": cooLeaseInformationState,
       "cooLeaseInformationMultipleSchedules": cooLeaseInformationMultipleSchedules,
       "cooLeaseInformationBuyOutAmount": cooLeaseInformationBuyOutAmount,
       "cooLeaseInformationLeaseRateFactor": cooLeaseInformationLeaseRateFactor,
       "cooLeaseInformationEndDateName": cooLeaseInformationEndDateName,
       "cooLeaseInformationFairMarketValue": cooLeaseInformationFairMarketValue,
       "cooLeaseInformationLessorName": cooLeaseInformationLessorName,
       "cooScheduleNumberTable": cooScheduleNumberTable,
       "cooScheduleNumberTableEntry": cooScheduleNumberTableEntry,
       "cooScheduleNumberchassisIndex": cooScheduleNumberchassisIndex,
       "cooScheduleNumberIndex": cooScheduleNumberIndex,
       "cooScheduleNumberState": cooScheduleNumberState,
       "cooScheduleNumberLeaseInformationIndexReference": cooScheduleNumberLeaseInformationIndexReference,
       "cooScheduleNumberDescriptionName": cooScheduleNumberDescriptionName,
       "cooOptionsTable": cooOptionsTable,
       "cooOptionsTableEntry": cooOptionsTableEntry,
       "cooOptionschassisIndex": cooOptionschassisIndex,
       "cooOptionsIndex": cooOptionsIndex,
       "cooOptionsState": cooOptionsState,
       "cooOptionsLeaseInformationIndexReference": cooOptionsLeaseInformationIndexReference,
       "cooOptionsDescriptionName": cooOptionsDescriptionName,
       "cooMaintenanceTable": cooMaintenanceTable,
       "cooMaintenanceTableEntry": cooMaintenanceTableEntry,
       "cooMaintenancechassisIndex": cooMaintenancechassisIndex,
       "cooMaintenanceIndex": cooMaintenanceIndex,
       "cooMaintenanceState": cooMaintenanceState,
       "cooMaintenanceStartDateName": cooMaintenanceStartDateName,
       "cooMaintenanceEndDateName": cooMaintenanceEndDateName,
       "cooMaintenanceProviderName": cooMaintenanceProviderName,
       "cooMaintenanceRestrictionsName": cooMaintenanceRestrictionsName,
       "cooRepairTable": cooRepairTable,
       "cooRepairTableEntry": cooRepairTableEntry,
       "cooRepairchassisIndex": cooRepairchassisIndex,
       "cooRepairIndex": cooRepairIndex,
       "cooRepairState": cooRepairState,
       "cooRepairCounter": cooRepairCounter,
       "cooRepairVendorName": cooRepairVendorName,
       "cooSupportInformationTable": cooSupportInformationTable,
       "cooSupportInformationTableEntry": cooSupportInformationTableEntry,
       "cooSupportInformationchassisIndex": cooSupportInformationchassisIndex,
       "cooSupportInformationIndex": cooSupportInformationIndex,
       "cooSupportInformationState": cooSupportInformationState,
       "cooSupportInformationIsOutsourced": cooSupportInformationIsOutsourced,
       "cooSupportInformationType": cooSupportInformationType,
       "cooSupportInformationHelpDeskName": cooSupportInformationHelpDeskName,
       "cooSupportInformationFixTypeName": cooSupportInformationFixTypeName,
       "cooTroubleTicketTable": cooTroubleTicketTable,
       "cooTroubleTicketTableEntry": cooTroubleTicketTableEntry,
       "cooTroubleTicketchassisIndex": cooTroubleTicketchassisIndex,
       "cooTroubleTicketIndex": cooTroubleTicketIndex,
       "cooTroubleTicketState": cooTroubleTicketState,
       "cooTroubleTicketSupportInformationIndexReference": cooTroubleTicketSupportInformationIndexReference,
       "cooTroubleTicketNumberName": cooTroubleTicketNumberName,
       "clusterGroup": clusterGroup,
       "clusterTable": clusterTable,
       "clusterTableEntry": clusterTableEntry,
       "clusterChassisIndex": clusterChassisIndex,
       "clusterIndex": clusterIndex,
       "clusterStateCapabilities": clusterStateCapabilities,
       "clusterStateSettings": clusterStateSettings,
       "clusterStatus": clusterStatus,
       "clusterType": clusterType,
       "clusterTypeDescriptionName": clusterTypeDescriptionName,
       "clusterName": clusterName,
       "bmcGroup": bmcGroup,
       "bmcTable": bmcTable,
       "bmcTableEntry": bmcTableEntry,
       "bmcChassisIndex": bmcChassisIndex,
       "bmcIndex": bmcIndex,
       "bmcStateCapabilities": bmcStateCapabilities,
       "bmcStateSettings": bmcStateSettings,
       "bmcStatus": bmcStatus,
       "bmcDisplayName": bmcDisplayName,
       "bmcDescriptionName": bmcDescriptionName,
       "bmcIPMIVersionName": bmcIPMIVersionName,
       "bmcGUID": bmcGUID,
       "bmcType": bmcType,
       "bmcModuleName": bmcModuleName,
       "bmcIPv4URLName": bmcIPv4URLName,
       "bmcIPv6URLName": bmcIPv6URLName,
       "bmcBladeFormFactorName": bmcBladeFormFactorName,
       "bmcSerialInterfaceTable": bmcSerialInterfaceTable,
       "bmcSerialInterfaceTableEntry": bmcSerialInterfaceTableEntry,
       "bmcSerialInterfaceChassisIndex": bmcSerialInterfaceChassisIndex,
       "bmcSerialInterfaceBMCIndex": bmcSerialInterfaceBMCIndex,
       "bmcSerialInterfaceIndex": bmcSerialInterfaceIndex,
       "bmcSerialInterfaceStateCapabilities": bmcSerialInterfaceStateCapabilities,
       "bmcSerialInterfaceStateSettings": bmcSerialInterfaceStateSettings,
       "bmcSerialInterfaceStatus": bmcSerialInterfaceStatus,
       "bmcSerialInterfaceChannelNumber": bmcSerialInterfaceChannelNumber,
       "bmcSerialInterfaceConnectionModeCapabilities": bmcSerialInterfaceConnectionModeCapabilities,
       "bmcSerialInterfaceConnectionModeSettings": bmcSerialInterfaceConnectionModeSettings,
       "bmcSerialInterfaceFlowControl": bmcSerialInterfaceFlowControl,
       "bmcSerialInterfaceBitRate": bmcSerialInterfaceBitRate,
       "bmcLANInterfaceTable": bmcLANInterfaceTable,
       "bmcLANInterfaceTableEntry": bmcLANInterfaceTableEntry,
       "bmcLANInterfaceChassisIndex": bmcLANInterfaceChassisIndex,
       "bmcLANInterfaceBMCIndex": bmcLANInterfaceBMCIndex,
       "bmcLANInterfaceIndex": bmcLANInterfaceIndex,
       "bmcLANInterfaceStateCapabilities": bmcLANInterfaceStateCapabilities,
       "bmcLANInterfaceStateSettings": bmcLANInterfaceStateSettings,
       "bmcLANInterfaceStatus": bmcLANInterfaceStatus,
       "bmcLANInterfaceChannelNumber": bmcLANInterfaceChannelNumber,
       "bmcLANInterfaceIPAddressSource": bmcLANInterfaceIPAddressSource,
       "bmcLANInterfaceIPAddress": bmcLANInterfaceIPAddress,
       "bmcLANInterfaceSubnetMaskAddress": bmcLANInterfaceSubnetMaskAddress,
       "bmcLANInterfaceDefaultGatewayAddress": bmcLANInterfaceDefaultGatewayAddress,
       "bmcLANInterfaceMACAddress": bmcLANInterfaceMACAddress,
       "bmcLANInterfaceAlertCommunityName": bmcLANInterfaceAlertCommunityName,
       "alertGroup": alertGroup,
       "alertVariables": alertVariables,
       "alertSystem": alertSystem,
       "alertTableIndexOID": alertTableIndexOID,
       "alertMessage": alertMessage,
       "alertCurrentStatus": alertCurrentStatus,
       "alertPreviousStatus": alertPreviousStatus,
       "alertData": alertData,
       "alertMsgID": alertMsgID,
       "alertSystemFQDN": alertSystemFQDN,
       "alertServiceTag": alertServiceTag,
       "alertChassisServiceTag": alertChassisServiceTag}
)
