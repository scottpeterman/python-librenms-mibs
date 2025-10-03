# SNMP MIB module (ADVA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\ADVA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:39 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 mib_2,
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
    "mib-2",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

advaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544)
)
if mibBuilder.loadTexts:
    advaMIB.setRevisions(
        ("2018-12-14 00:00",
         "2017-12-07 00:00",
         "2017-03-23 00:00",
         "2016-04-01 00:00",
         "2015-12-10 00:00",
         "2015-09-03 00:00",
         "2015-03-20 00:00",
         "2014-09-29 00:00",
         "2012-02-07 00:00",
         "2008-02-21 00:00",
         "2004-12-14 00:00",
         "2004-02-20 00:00",
         "2003-12-12 00:00",
         "2003-10-07 00:00",
         "2003-06-27 00:00",
         "2002-07-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OnOff(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class AvailState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )



class EnableState(TextualConvention, Integer32):
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
        *(("stateNotApplicable", 0),
          ("stateEnabled", 1),
          ("stateDisabled", 2))
    )



class ArcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alm", 1),
          ("nalm", 2))
    )



class TrapAlarmSeverity(TextualConvention, Integer32):
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
        *(("indeterminate", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5),
          ("cleared", 6),
          ("notReported", 7))
    )



class ServiceImpairment(TextualConvention, Integer32):
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
        *(("serviceAffecting", 1),
          ("nonServiceAffecting", 2),
          ("serviceAffectingInstall", 3),
          ("serviceAffectingActivate", 4))
    )



class TrapCounter(TextualConvention, Counter32):
    status = "current"


class Counter64String(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class KBytes(TextualConvention, Gauge32):
    status = "current"


class IdentityTranslation(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class NeSwUpgradeStatusType(TextualConvention, Integer32):
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
              39)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("downloading", 2),
          ("downloadLoginFailed", 3),
          ("downloadFileNotFound", 4),
          ("downloadFileNoAccess", 5),
          ("downloadFailure", 6),
          ("downloadReadyForInstallation", 7),
          ("installingSoftware", 8),
          ("installationFailed", 9),
          ("softwareReadyForActivation", 10),
          ("activatingSoftware", 11),
          ("activationFailed", 12),
          ("softwareActivated", 13),
          ("rebooting", 14),
          ("downloadServerUnreachable", 15),
          ("noSpaceLeft", 16),
          ("internalError", 17),
          ("downloadFileProtocolFailed", 18),
          ("downloadFileCheckFailed", 19),
          ("downloadSSHHostkeyFailed", 20),
          ("uploading", 21),
          ("uploadLoginFailed", 22),
          ("uploadFileNotFound", 23),
          ("uploadFileNoAccess", 24),
          ("uploadFailure", 25),
          ("uploadServerUnreachable", 26),
          ("uploadFileProtocolFailed", 27),
          ("uploadFileCheckFailed", 28),
          ("uploadSSHHostkeyFailed", 29),
          ("installationFailedDeny", 30),
          ("installationFailedWrongCrc", 31),
          ("installationFailedVersionMismatch", 32),
          ("installationFailedStbyInWrongState", 33),
          ("installationFailedDamagedConfFile", 34),
          ("installationFailedFsckFailed", 35),
          ("installationFailedNotExist", 36),
          ("downloadFileFailedProtocolDisabled", 37),
          ("uploadFileFailedProtocolDisabled", 38),
          ("backupFailedGeneration", 39))
    )



class NeSwInstallStatusType(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("idle", 1),
          ("downloadingCon", 2),
          ("installingCon", 3),
          ("downloadingNcu", 4),
          ("installingNcu", 5),
          ("downloadingFwp", 6),
          ("installingFwp", 7),
          ("downloadingPgm", 8),
          ("installingPgm", 9))
    )



class FileTransferProtocol(TextualConvention, Integer32):
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
        *(("ftp", 2),
          ("scp", 3),
          ("http", 4),
          ("sftp", 5))
    )



class SourceIpAddress(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("sysIp", 1),
          ("defaultIp", 2))
    )



class F7FileTimeStamp(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("add", 1),
          ("omit", 2))
    )



class F7AutoBackupInterval(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("every1Day", 2),
          ("every2Day", 3),
          ("every3Day", 4),
          ("every4Day", 5),
          ("every5Day", 6),
          ("every6Day", 7),
          ("every1Week", 8),
          ("every2Week", 9),
          ("every3Week", 10),
          ("every1Month", 11),
          ("every2Month", 12),
          ("every3Month", 13))
    )



class F7AutoBackupRunState(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("no", 1),
          ("yes", 2))
    )



class PartitionStatus(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("empty", 1),
          ("configFileInstalled", 2),
          ("ncuFileInstalled", 3),
          ("softwareReadyForActivation", 4),
          ("fwpsInstalled", 5))
    )



class FspDate(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class FspTime(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d-1d-1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class ApsDirection(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("bidirectional", 1),
          ("unidirectional", 2))
    )



class ApsDirectionCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capBidirectional", 1),
          ("capUnidirectional", 2))
    )


class ApsHoldoffTime(TextualConvention, Integer32):
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
              45,
              46,
              47,
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
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("e20ms", 2),
          ("e100ms", 3),
          ("e200ms", 4),
          ("e300ms", 5),
          ("e400ms", 6),
          ("e500ms", 7),
          ("e600ms", 8),
          ("e700ms", 9),
          ("e800ms", 10),
          ("e900ms", 11),
          ("e1000ms", 12),
          ("e1100ms", 13),
          ("e1200ms", 14),
          ("e1300ms", 15),
          ("e1400ms", 16),
          ("e1500ms", 17),
          ("e1600ms", 18),
          ("e1700ms", 19),
          ("e1800ms", 20),
          ("e1900ms", 21),
          ("e2000ms", 22),
          ("e2100ms", 23),
          ("e2200ms", 24),
          ("e2300ms", 25),
          ("e2400ms", 26),
          ("e2500ms", 27),
          ("e2600ms", 28),
          ("e2700ms", 29),
          ("e2800ms", 30),
          ("e2900ms", 31),
          ("e3000ms", 32),
          ("e3100ms", 33),
          ("e3200ms", 34),
          ("e3300ms", 35),
          ("e3400ms", 36),
          ("e3500ms", 37),
          ("e3600ms", 38),
          ("e3700ms", 39),
          ("e3800ms", 40),
          ("e3900ms", 41),
          ("e4000ms", 42),
          ("e4100ms", 43),
          ("e4200ms", 44),
          ("e4300ms", 45),
          ("e4400ms", 46),
          ("e4500ms", 47),
          ("e4600ms", 48),
          ("e4700ms", 49),
          ("e4800ms", 50),
          ("e4900ms", 51),
          ("e5000ms", 52),
          ("e5100ms", 53),
          ("e5200ms", 54),
          ("e5300ms", 55),
          ("e5400ms", 56),
          ("e5500ms", 57),
          ("e5600ms", 58),
          ("e5700ms", 59),
          ("e5800ms", 60),
          ("e5900ms", 61),
          ("e6000ms", 62),
          ("e6100ms", 63),
          ("e6200ms", 64),
          ("e6300ms", 65),
          ("e6400ms", 66),
          ("e6500ms", 67),
          ("e6600ms", 68),
          ("e6700ms", 69),
          ("e6800ms", 70),
          ("e6900ms", 71),
          ("e7000ms", 72),
          ("e7100ms", 73),
          ("e7200ms", 74),
          ("e7300ms", 75),
          ("e7400ms", 76),
          ("e7500ms", 77),
          ("e7600ms", 78),
          ("e7700ms", 79),
          ("e7800ms", 80),
          ("e7900ms", 81),
          ("e8000ms", 82),
          ("e8100ms", 83),
          ("e8200ms", 84),
          ("e8300ms", 85),
          ("e8400ms", 86),
          ("e8500ms", 87),
          ("e8600ms", 88),
          ("e8700ms", 89),
          ("e8800ms", 90),
          ("e8900ms", 91),
          ("e9000ms", 92),
          ("e9100ms", 93),
          ("e9200ms", 94),
          ("e9300ms", 95),
          ("e9400ms", 96),
          ("e9500ms", 97),
          ("e9600ms", 98),
          ("e9700ms", 99),
          ("e9800ms", 100),
          ("e9900ms", 101),
          ("e10000ms", 102))
    )



class ApsHoldoffTimeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNone", 1),
          ("capE20ms", 2),
          ("capE100ms", 3),
          ("capE200ms", 4),
          ("capE300ms", 5),
          ("capE400ms", 6),
          ("capE500ms", 7),
          ("capE600ms", 8),
          ("capE700ms", 9),
          ("capE800ms", 10),
          ("capE900ms", 11),
          ("capE1000ms", 12),
          ("capE1100ms", 13),
          ("capE1200ms", 14),
          ("capE1300ms", 15),
          ("capE1400ms", 16),
          ("capE1500ms", 17),
          ("capE1600ms", 18),
          ("capE1700ms", 19),
          ("capE1800ms", 20),
          ("capE1900ms", 21),
          ("capE2000ms", 22),
          ("capE2100ms", 23),
          ("capE2200ms", 24),
          ("capE2300ms", 25),
          ("capE2400ms", 26),
          ("capE2500ms", 27),
          ("capE2600ms", 28),
          ("capE2700ms", 29),
          ("capE2800ms", 30),
          ("capE2900ms", 31),
          ("capE3000ms", 32),
          ("capE3100ms", 33),
          ("capE3200ms", 34),
          ("capE3300ms", 35),
          ("capE3400ms", 36),
          ("capE3500ms", 37),
          ("capE3600ms", 38),
          ("capE3700ms", 39),
          ("capE3800ms", 40),
          ("capE3900ms", 41),
          ("capE4000ms", 42),
          ("capE4100ms", 43),
          ("capE4200ms", 44),
          ("capE4300ms", 45),
          ("capE4400ms", 46),
          ("capE4500ms", 47),
          ("capE4600ms", 48),
          ("capE4700ms", 49),
          ("capE4800ms", 50),
          ("capE4900ms", 51),
          ("capE5000ms", 52),
          ("capE5100ms", 53),
          ("capE5200ms", 54),
          ("capE5300ms", 55),
          ("capE5400ms", 56),
          ("capE5500ms", 57),
          ("capE5600ms", 58),
          ("capE5700ms", 59),
          ("capE5800ms", 60),
          ("capE5900ms", 61),
          ("capE6000ms", 62),
          ("capE6100ms", 63),
          ("capE6200ms", 64),
          ("capE6300ms", 65),
          ("capE6400ms", 66),
          ("capE6500ms", 67),
          ("capE6600ms", 68),
          ("capE6700ms", 69),
          ("capE6800ms", 70),
          ("capE6900ms", 71),
          ("capE7000ms", 72),
          ("capE7100ms", 73),
          ("capE7200ms", 74),
          ("capE7300ms", 75),
          ("capE7400ms", 76),
          ("capE7500ms", 77),
          ("capE7600ms", 78),
          ("capE7700ms", 79),
          ("capE7800ms", 80),
          ("capE7900ms", 81),
          ("capE8000ms", 82),
          ("capE8100ms", 83),
          ("capE8200ms", 84),
          ("capE8300ms", 85),
          ("capE8400ms", 86),
          ("capE8500ms", 87),
          ("capE8600ms", 88),
          ("capE8700ms", 89),
          ("capE8800ms", 90),
          ("capE8900ms", 91),
          ("capE9000ms", 92),
          ("capE9100ms", 93),
          ("capE9200ms", 94),
          ("capE9300ms", 95),
          ("capE9400ms", 96),
          ("capE9500ms", 97),
          ("capE9600ms", 98),
          ("capE9700ms", 99),
          ("capE9800ms", 100),
          ("capE9900ms", 101),
          ("capE10000ms", 102))
    )


class AssignmentState(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("assigned", 1),
          ("unassigned", 2),
          ("notassignable", 3))
    )



class BootState(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("complete", 1),
          ("started", 2),
          ("failed", 3),
          ("reject", 4),
          ("install", 5),
          ("installFail", 6),
          ("installComplete", 7),
          ("activate", 8),
          ("activateFail", 9),
          ("activateReject", 10),
          ("activateComplete", 11))
    )



class CommandEqpt(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("none", 1),
          ("install", 2),
          ("reboot", 3),
          ("activate", 4),
          ("update", 5),
          ("installFromStby", 6),
          ("forceInstall", 7))
    )



class CpWdmEntityClass(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("cp", 1),
          ("tunnel", 2),
          ("connection", 3),
          ("path", 4),
          ("pathElement", 5),
          ("logicalInterface", 6),
          ("remoteAlarm", 7),
          ("portBinding", 8),
          ("reservation", 9),
          ("diversity", 10))
    )



class EnableStateCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capStateEnabled", 1),
          ("capStateDisabled", 2))
    )


class EntityClass(TextualConvention, Integer32):
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
              45,
              47,
              48,
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
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("other", 1),
          ("unknown", 2),
          ("chassis", 3),
          ("backplane", 4),
          ("container", 5),
          ("powerSupply", 6),
          ("fan", 7),
          ("sensor", 8),
          ("module", 9),
          ("plug", 10),
          ("stack", 11),
          ("group", 12),
          ("clientPort", 13),
          ("networkPort", 14),
          ("virtualChannel", 15),
          ("connection", 16),
          ("vc4Container", 17),
          ("vc3sts1Container", 18),
          ("vc12vt15Container", 19),
          ("dcnChannel", 20),
          ("routerConfig", 21),
          ("environmentPort", 22),
          ("internalPort", 23),
          ("upgradePort", 24),
          ("midstagePort", 25),
          ("serialPort", 26),
          ("pppIpInterface", 27),
          ("lanIp", 28),
          ("vs1Container", 29),
          ("sts3cContainer", 30),
          ("payloadChannel", 31),
          ("passiveShelf", 32),
          ("sts24cContainer", 33),
          ("sts48cContainer", 34),
          ("vs2cContainer", 35),
          ("vs4cContainer", 36),
          ("tifInputPort", 37),
          ("tifOutputPort", 38),
          ("opticalLink", 39),
          ("virtualOpticalChannel", 40),
          ("logicalInterface", 41),
          ("physicalTerminationPoint", 42),
          ("ethClient", 43),
          ("ethNetwork", 44),
          ("veth", 45),
          ("flow", 47),
          ("ctrans", 48),
          ("policerOnFlow", 50),
          ("queueOnPort", 51),
          ("queueOnFlow", 52),
          ("farEndPlug", 53),
          ("farEndChannel", 54),
          ("vc4c8Container", 55),
          ("vc4c16Container", 56),
          ("vs0Container", 57),
          ("virtualSubChannel", 58),
          ("bridge", 59),
          ("queueOnBridge", 60),
          ("backwardVirtualOptMux", 61),
          ("forwardVirtualOptMux", 62),
          ("optChannelTransportLane", 63),
          ("virtualChannelN", 64),
          ("externalChannel", 65),
          ("virtualTerminationPoint", 66),
          ("virtualConnection", 67),
          ("virtualOptMux", 68),
          ("optTransportLaneGroup", 69),
          ("optWaveLengthGroup", 70),
          ("crossConnectionChannel", 71),
          ("crossOpticalLineChannel", 72),
          ("versatilePort", 73),
          ("system", 74),
          ("crossConnectionDcn", 75),
          ("protectionFfp", 76),
          ("protectionCable", 77),
          ("unidirectionalChannel", 78),
          ("filterCable", 79),
          ("groupTerminationPoint", 80),
          ("externalOm", 81),
          ("externalVch", 82),
          ("virtualModule", 83),
          ("virtualMap", 84),
          ("lldp", 85),
          ("managementPort", 86),
          ("licenseManager", 87),
          ("license", 88))
    )



class EntityIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EntityType(TextualConvention, Integer32):
    status = "current"


class EquipmentState(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("equipped", 1),
          ("unequipped", 2))
    )



class EthDuplexMode(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("ethHalfDuplex", 1),
          ("ethFullDuplex", 2))
    )



class EthDuplexModeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capEthHalfDuplex", 1),
          ("capEthFullDuplex", 2))
    )


class FileArea(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("activeArea", 1),
          ("standbyArea", 2),
          ("rDisk", 3),
          ("backupDisk", 4),
          ("alpDisk", 5),
          ("pDisk", 6),
          ("cfDisk", 7),
          ("paDisk", 8))
    )



class FileType(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("pgm", 1),
          ("dbs", 2),
          ("unknown", 3),
          ("alp", 4),
          ("ncu", 5),
          ("fwps", 6),
          ("con", 7),
          ("prf", 8),
          ("paf", 9),
          ("dbx", 10),
          ("alm", 11),
          ("pak", 12),
          ("map", 13))
    )



class FspR7AdminStateSnmpProxy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("is", 2),
          ("dsbld", 6))
    )



class FspR7AdminStateSnmpProxyCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capIs", 2),
          ("capDsbld", 6))
    )


class FspR7Date(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class FspR7EnableDisable(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("enable", 1),
          ("disable", 2))
    )



class FspR7EquipmentType(TextualConvention, Integer32):
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
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
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
              122,
              123,
              124,
              125,
              126,
              127,
              130,
              131,
              132,
              133,
              137,
              138,
              140,
              141,
              142,
              143,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
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
              180,
              182,
              183,
              185,
              186,
              187,
              188,
              190,
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
              234,
              235,
              236,
              237,
              239,
              240,
              241,
              242,
              243,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              264,
              267,
              268,
              269,
              270,
              272,
              273,
              274,
              280,
              282,
              283,
              284,
              285,
              286,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              297,
              298,
              300,
              303,
              304,
              305,
              307,
              308,
              309,
              311,
              312,
              314,
              317,
              318,
              319,
              320,
              321,
              323,
              324,
              450,
              453,
              454,
              455,
              456,
              457,
              458,
              459,
              461,
              462,
              463,
              464,
              465,
              466,
              467,
              468,
              472,
              473,
              474,
              475,
              476,
              478,
              479,
              480,
              481,
              482,
              483,
              485,
              486,
              487,
              488,
              489,
              490,
              491,
              499)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("eqpSh1hu", 1),
          ("eqpSh1huDc", 2),
          ("eqpSh3hu", 3),
          ("eqpSh7hu", 4),
          ("eqpF2kSh5hu", 5),
          ("eqpF2kSh6hu", 6),
          ("eqpDcm", 7),
          ("eqpSh9hu", 8),
          ("eqpUnknown", 19),
          ("eqpNcu", 20),
          ("eqpNcutif", 21),
          ("eqpScu", 22),
          ("eqpScue", 23),
          ("eqpR6cu", 24),
          ("eqpPsu1huac", 25),
          ("eqpPsu7huac", 26),
          ("eqpPsu7hudc", 27),
          ("eqpFcu7hu", 28),
          ("eqp2clsmd", 29),
          ("eqp2absmc", 30),
          ("eqp2bsmd", 31),
          ("eqp1Gsmud", 32),
          ("eqp4gsmd", 33),
          ("eqp8gsmd", 34),
          ("eqp1csmuc", 35),
          ("eqp1csmuewc", 36),
          ("eqp4csmd", 37),
          ("eqp4csmud", 38),
          ("eqp4csmc", 39),
          ("eqpOsfm", 40),
          ("eqp1pm", 41),
          ("eqp2pm", 42),
          ("eqp40csmd", 43),
          ("eqpDcf", 44),
          ("eqpEdfas", 45),
          ("eqpEdfasgc", 46),
          ("eqpEdfadgc", 47),
          ("eqpRaman", 48),
          ("eqp4tcc2g5", 49),
          ("eqp4tcc2g5d", 50),
          ("eqp4tcc10gd", 51),
          ("eqp4tcc10gc", 52),
          ("eqpWcc10gd", 53),
          ("eqpWcc10gc", 54),
          ("eqpWcc2g71N", 55),
          ("eqpWcc2g7d", 56),
          ("eqp2tcm2g5", 57),
          ("eqp2tca2g5", 58),
          ("eqp8tca10gd", 59),
          ("eqp8tca10gc", 60),
          ("eqpWca10gd", 61),
          ("eqpWca10gc", 62),
          ("eqp4tca4gd", 63),
          ("eqp4tca4gc", 64),
          ("eqpwca2g5", 65),
          ("eqp4tca1g3d", 66),
          ("eqp4tca1g3c", 67),
          ("eqp8tce2g5d", 68),
          ("eqp8tce2g5c", 69),
          ("eqpWcelsd", 70),
          ("eqpWcelsc", 71),
          ("eqpVsm", 72),
          ("eqpRsmolm", 73),
          ("eqpRsmsf", 74),
          ("eqpOscm", 75),
          ("eqp2oscm", 76),
          ("eqpDrm", 77),
          ("eqpXfpG", 78),
          ("eqpsfpd", 79),
          ("eqpSfpc", 80),
          ("eqpSfpg", 81),
          ("eqpSfpe", 82),
          ("eqpSh1hudcm", 83),
          ("eqpCustomc", 84),
          ("eqpCustomd", 85),
          ("eqpPsu1hudc", 86),
          ("eqpWcc2g7c", 87),
          ("eqp1csmuEwD", 88),
          ("eqp1csmuG", 89),
          ("eqp3BsmC", 90),
          ("eqp2Tca2g5s", 91),
          ("eqp8Csmuc", 92),
          ("eqpEdfaDgcb", 93),
          ("eqpOscmPn", 94),
          ("eqp4Tcc10gtd", 95),
          ("eqp4Tca4g", 96),
          ("eqpDcg", 97),
          ("eqp2Tcm2g5d", 98),
          ("eqp2Tcm2g5c", 99),
          ("eqpWcm2g5d", 100),
          ("eqpWcm2g5c", 101),
          ("eqpEdfmSgc", 102),
          ("eqpF2kDemiV2", 103),
          ("eqpPsm", 104),
          ("eqpNcu2e", 105),
          ("eqp8TceGl2g5d", 106),
          ("eqp8TceGl2g5c", 107),
          ("eqpDcf1hu", 108),
          ("eqp10tcc10gtd", 109),
          ("eqp10tcc10gd", 110),
          ("eqp10tcc10gc", 111),
          ("eqp16csmSfd", 112),
          ("eqpOsfmSf", 113),
          ("eqp2clsmSfd", 114),
          ("eqp3bsmEwc", 115),
          ("eqpEdfaSgcb", 116),
          ("eqpEdfaDgcv", 117),
          ("eqpWcc10gtd", 118),
          ("eqp2csmuEwc", 119),
          ("eqpEroadmDc", 120),
          ("eqpScuS", 122),
          ("eqp4opcm", 123),
          ("eqpUtm", 124),
          ("eqpPscu", 125),
          ("eqp40Csm2hu", 126),
          ("eqp2Twcc2g7", 127),
          ("eqp2Wca10g", 130),
          ("eqpNcuHp", 131),
          ("eqpNcu20085hu", 132),
          ("eqp20Pca10G", 133),
          ("eqpXfpC", 137),
          ("eqpXfpD", 138),
          ("eqpWcc40gtd", 140),
          ("eqpIlm", 141),
          ("eqpNcuII", 142),
          ("eqpCem9hu", 143),
          ("eqp8roadmC40", 148),
          ("eqp4Tcc40gtd", 149),
          ("eqp2pca10g", 150),
          ("eqp10pca10g", 151),
          ("eqp1csmuD", 152),
          ("eqpSfpOsC", 153),
          ("eqpSfpOdC", 154),
          ("eqpSfpOsG", 155),
          ("eqpSfpOdG", 156),
          ("eqpRoadmC80", 157),
          ("eqpccm8", 158),
          ("eqpPsu9hudc", 159),
          ("eqp4tca4gus", 160),
          ("eqp40Csm3huD", 161),
          ("eqp5psm", 162),
          ("eqpFan9hu", 163),
          ("eqp5tce10gtd", 164),
          ("eqp10tccs10gtd", 165),
          ("eqp40Csm3hudcD", 166),
          ("eqp40Csm3hudcDi", 167),
          ("eqp5gsmD", 169),
          ("eqp8csmD", 170),
          ("eqp2otfm", 171),
          ("eqp8otdr3hu", 172),
          ("eqpXfptD", 173),
          ("eqp40Csm3huDi", 174),
          ("eqp8CcmC80", 175),
          ("eqpEdfaD27", 176),
          ("eqp2Wcc10g", 177),
          ("eqp8RoadmC80", 178),
          ("eqp2Wcc10gAes", 180),
          ("eqp5tce10gtaesd", 182),
          ("eqpSh1hupf", 183),
          ("eqpFan1hu", 185),
          ("eqp10tcc10g", 186),
          ("eqpXfpOtnD", 187),
          ("eqpNcu2p", 188),
          ("eqpPsu9huac", 190),
          ("eqp2Raman", 192),
          ("eqpEdfaS26", 193),
          ("eqp5tces10gtd", 194),
          ("eqpScuII", 195),
          ("eqp11RoadmC96", 196),
          ("eqp8AdmC96", 197),
          ("eqp8CxmC96", 198),
          ("eqp8Shm", 199),
          ("eqpAmpShgcv", 200),
          ("eqpAmpSlgcv", 201),
          ("eqp2RamanC15", 202),
          ("eqpWcc100gtD", 203),
          ("eqpCfp4g", 204),
          ("eqpCfp10g", 205),
          ("eqpXfpTlnD", 213),
          ("eqp5tces10gtaesd", 214),
          ("eqp10tce100g", 215),
          ("eqp96Csm4HuD", 216),
          ("eqp4CfptD", 217),
          ("eqp2psm", 218),
          ("eqpWce100G", 219),
          ("eqp10Wxc10g", 220),
          ("eqpShx9hu", 221),
          ("eqpFanXhu", 222),
          ("eqp10tcc100gtbD", 223),
          ("eqp9RoadmC96", 224),
          ("eqp4Wce16g", 225),
          ("eqpSfpBG", 226),
          ("eqpSfpCdrG", 227),
          ("eqp10tce100gGf", 228),
          ("eqpSfpCdrC", 229),
          ("eqp5tce10gaes", 234),
          ("eqp5tce10g", 235),
          ("eqp5tces10gaes", 236),
          ("eqp5tces10g", 237),
          ("eqp4roadmC96", 239),
          ("eqpWcc100gtbD", 240),
          ("eqpEdfaS20", 241),
          ("eqp10tccSdi10g", 242),
          ("eqp4roadmEC96", 243),
          ("eqpSfptD", 245),
          ("eqpSfp2TxG", 246),
          ("eqpSfp2RxG", 247),
          ("eqpSfp2Txe", 248),
          ("eqpSfp2Rxe", 249),
          ("eqp2EdfaS20S10", 250),
          ("eqp10Tce100Gb", 251),
          ("eqp10Tce100gAes", 252),
          ("eqpSfpCdrD", 253),
          ("eqpSh1huDcEtemp", 254),
          ("eqp8psm", 255),
          ("eqp9ccmC96", 256),
          ("eqpWce100GB", 257),
          ("eqp16tcc10G", 258),
          ("eqp4Wcc10g", 259),
          ("eqp5wca16G", 260),
          ("eqpCfptCd", 261),
          ("eqpWccPcn100g", 264),
          ("eqpOppm", 267),
          ("eqp4cfpd", 268),
          ("eqpNcuS", 269),
          ("eqp10csmuD", 270),
          ("eqpUtmS", 272),
          ("eqpSfpBC", 273),
          ("eqp10Tce100gAesBsi", 274),
          ("eqpWccPcn100gAes", 280),
          ("eqpSfpRxTxG", 282),
          ("eqpSfpTlnD", 283),
          ("eqpCfpTfCd", 284),
          ("eqpXfpBG", 285),
          ("eqpFd128D", 286),
          ("eqpSfpBCdrG", 289),
          ("eqpMroadmC96", 290),
          ("eqpPsm40Mroadm", 291),
          ("eqpOsfma", 292),
          ("eqp10tcc100g", 293),
          ("eqpCfpTgCd", 294),
          ("eqpPsm80Mroadm", 295),
          ("eqp10Tce100gbAes", 297),
          ("eqpL3CmSina", 298),
          ("eqp9Tce10gAesG", 300),
          ("eqp9RoadmRs", 303),
          ("eqp16psm4", 304),
          ("eqp96Csm2HuD", 305),
          ("eqp9Tce10gAesF", 307),
          ("eqp10Tce100gAesF", 308),
          ("eqpMtpOscC", 309),
          ("eqpWcc100gAesF", 311),
          ("eqpCfpTrCd", 312),
          ("eqpWcc100gAesB", 314),
          ("eqpMapOscC", 317),
          ("eqpMtpbOscC", 318),
          ("eqpMapbOscC", 319),
          ("eqpWccPcn100gB", 320),
          ("eqp4psmS", 321),
          ("eqpWcc100gAesG", 323),
          ("eqpHdScm", 324),
          ("eqpCfp2tgCd", 450),
          ("eqpMaB2C3LtA", 453),
          ("eqpMaB5Lt", 454),
          ("eqpCfp2tCd", 455),
          ("eqpMp2B4CtS", 456),
          ("eqpPsmdc3", 457),
          ("eqpQSfpNotApproved", 458),
          ("eqpQSfp10g", 459),
          ("eqpMa2C2C3LtA", 461),
          ("eqpQSfpDacCr", 462),
          ("eqpCem3", 463),
          ("eqpFtm3", 464),
          ("eqpPsmac3", 465),
          ("eqpSh1R", 466),
          ("eqpEcm3", 467),
          ("eqp4QsfpG", 468),
          ("eqpScm2", 472),
          ("eqpMa2C5Lt", 473),
          ("eqpPsmac6", 474),
          ("eqpQSfpDac", 475),
          ("eqpQSfpAoc", 476),
          ("eqpPsmdc4", 478),
          ("eqpPsmac5", 479),
          ("eqpFtm4", 480),
          ("eqpFtm2", 481),
          ("eqpPsmac4", 482),
          ("eqpPsmdc", 483),
          ("eqpCem2", 485),
          ("eqpCem4", 486),
          ("eqpEcm2", 487),
          ("eqpQSfp4g", 488),
          ("eqpMp2B4Ct", 489),
          ("eqpSh12", 490),
          ("eqpSh4R", 491),
          ("eqpPtp", 499))
    )



class FspR7EquipmentTypeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capEqpSh1hu", 1),
          ("capEqpSh1huDc", 2),
          ("capEqpSh3hu", 3),
          ("capEqpSh7hu", 4),
          ("capEqpF2kSh5hu", 5),
          ("capEqpF2kSh6hu", 6),
          ("capEqpDcm", 7),
          ("capEqpSh9hu", 8),
          ("capEqpUnknown", 19),
          ("capEqpNcu", 20),
          ("capEqpNcutif", 21),
          ("capEqpScu", 22),
          ("capEqpScue", 23),
          ("capEqpR6cu", 24),
          ("capEqpPsu1huac", 25),
          ("capEqpPsu7huac", 26),
          ("capEqpPsu7hudc", 27),
          ("capEqpFcu7hu", 28),
          ("capEqp2clsmd", 29),
          ("capEqp2absmc", 30),
          ("capEqp2bsmd", 31),
          ("capEqp1Gsmud", 32),
          ("capEqp4gsmd", 33),
          ("capEqp8gsmd", 34),
          ("capEqp1csmuc", 35),
          ("capEqp1csmuewc", 36),
          ("capEqp4csmd", 37),
          ("capEqp4csmud", 38),
          ("capEqp4csmc", 39),
          ("capEqpOsfm", 40),
          ("capEqp1pm", 41),
          ("capEqp2pm", 42),
          ("capEqp40csmd", 43),
          ("capEqpDcf", 44),
          ("capEqpEdfas", 45),
          ("capEqpEdfasgc", 46),
          ("capEqpEdfadgc", 47),
          ("capEqpRaman", 48),
          ("capEqp4tcc2g5", 49),
          ("capEqp4tcc2g5d", 50),
          ("capEqp4tcc10gd", 51),
          ("capEqp4tcc10gc", 52),
          ("capEqpWcc10gd", 53),
          ("capEqpWcc10gc", 54),
          ("capEqpWcc2g71N", 55),
          ("capEqpWcc2g7d", 56),
          ("capEqp2tcm2g5", 57),
          ("capEqp2tca2g5", 58),
          ("capEqp8tca10gd", 59),
          ("capEqp8tca10gc", 60),
          ("capEqpWca10gd", 61),
          ("capEqpWca10gc", 62),
          ("capEqp4tca4gd", 63),
          ("capEqp4tca4gc", 64),
          ("capEqpwca2g5", 65),
          ("capEqp4tca1g3d", 66),
          ("capEqp4tca1g3c", 67),
          ("capEqp8tce2g5d", 68),
          ("capEqp8tce2g5c", 69),
          ("capEqpWcelsd", 70),
          ("capEqpWcelsc", 71),
          ("capEqpVsm", 72),
          ("capEqpRsmolm", 73),
          ("capEqpRsmsf", 74),
          ("capEqpOscm", 75),
          ("capEqp2oscm", 76),
          ("capEqpDrm", 77),
          ("capEqpXfpG", 78),
          ("capEqpsfpd", 79),
          ("capEqpSfpc", 80),
          ("capEqpSfpg", 81),
          ("capEqpSfpe", 82),
          ("capEqpSh1hudcm", 83),
          ("capEqpCustomc", 84),
          ("capEqpCustomd", 85),
          ("capEqpPsu1hudc", 86),
          ("capEqpWcc2g7c", 87),
          ("capEqp1csmuEwD", 88),
          ("capEqp1csmuG", 89),
          ("capEqp3BsmC", 90),
          ("capEqp2Tca2g5s", 91),
          ("capEqp8Csmuc", 92),
          ("capEqpEdfaDgcb", 93),
          ("capEqpOscmPn", 94),
          ("capEqp4Tcc10gtd", 95),
          ("capEqp4Tca4g", 96),
          ("capEqpDcg", 97),
          ("capEqp2Tcm2g5d", 98),
          ("capEqp2Tcm2g5c", 99),
          ("capEqpWcm2g5d", 100),
          ("capEqpWcm2g5c", 101),
          ("capEqpEdfmSgc", 102),
          ("capEqpF2kDemiV2", 103),
          ("capEqpPsm", 104),
          ("capEqpNcu2e", 105),
          ("capEqp8TceGl2g5d", 106),
          ("capEqp8TceGl2g5c", 107),
          ("capEqpDcf1hu", 108),
          ("capEqp10tcc10gtd", 109),
          ("capEqp10tcc10gd", 110),
          ("capEqp10tcc10gc", 111),
          ("capEqp16csmSfd", 112),
          ("capEqpOsfmSf", 113),
          ("capEqp2clsmSfd", 114),
          ("capEqp3bsmEwc", 115),
          ("capEqpEdfaSgcb", 116),
          ("capEqpEdfaDgcv", 117),
          ("capEqpWcc10gtd", 118),
          ("capEqp2csmuEwc", 119),
          ("capEqpEroadmDc", 120),
          ("capEqpScuS", 122),
          ("capEqp4opcm", 123),
          ("capEqpUtm", 124),
          ("capEqpPscu", 125),
          ("capEqp40Csm2hu", 126),
          ("capEqp2Twcc2g7", 127),
          ("capEqp2Wca10g", 130),
          ("capEqpNcuHp", 131),
          ("capEqpNcu20085hu", 132),
          ("capEqp20Pca10G", 133),
          ("capEqpXfpC", 137),
          ("capEqpXfpD", 138),
          ("capEqpWcc40gtd", 140),
          ("capEqpIlm", 141),
          ("capEqpNcuII", 142),
          ("capEqpCem9hu", 143),
          ("capEqp8roadmC40", 148),
          ("capEqp4Tcc40gtd", 149),
          ("capEqp2pca10g", 150),
          ("capEqp10pca10g", 151),
          ("capEqp1csmuD", 152),
          ("capEqpSfpOsC", 153),
          ("capEqpSfpOdC", 154),
          ("capEqpSfpOsG", 155),
          ("capEqpSfpOdG", 156),
          ("capEqpRoadmC80", 157),
          ("capEqpccm8", 158),
          ("capEqpPsu9hudc", 159),
          ("capEqp4tca4gus", 160),
          ("capEqp40Csm3huD", 161),
          ("capEqp5psm", 162),
          ("capEqpFan9hu", 163),
          ("capEqp5tce10gtd", 164),
          ("capEqp10tccs10gtd", 165),
          ("capEqp40Csm3hudcD", 166),
          ("capEqp40Csm3hudcDi", 167),
          ("capEqp5gsmD", 169),
          ("capEqp8csmD", 170),
          ("capEqp2otfm", 171),
          ("capEqp8otdr3hu", 172),
          ("capEqpXfptD", 173),
          ("capEqp40Csm3huDi", 174),
          ("capEqp8CcmC80", 175),
          ("capEqpEdfaD27", 176),
          ("capEqp2Wcc10g", 177),
          ("capEqp8RoadmC80", 178),
          ("capEqp2Wcc10gAes", 180),
          ("capEqp5tce10gtaesd", 182),
          ("capEqpSh1hupf", 183),
          ("capEqpFan1hu", 185),
          ("capEqp10tcc10g", 186),
          ("capEqpXfpOtnD", 187),
          ("capEqpNcu2p", 188),
          ("capEqpPsu9huac", 190),
          ("capEqp2Raman", 192),
          ("capEqpEdfaS26", 193),
          ("capEqp5tces10gtd", 194),
          ("capEqpScuII", 195),
          ("capEqp11RoadmC96", 196),
          ("capEqp8AdmC96", 197),
          ("capEqp8CxmC96", 198),
          ("capEqp8Shm", 199),
          ("capEqpAmpShgcv", 200),
          ("capEqpAmpSlgcv", 201),
          ("capEqp2RamanC15", 202),
          ("capEqpWcc100gtD", 203),
          ("capEqpCfp4g", 204),
          ("capEqpCfp10g", 205),
          ("capEqpXfpTlnD", 213),
          ("capEqp5tces10gtaesd", 214),
          ("capEqp10tce100g", 215),
          ("capEqp96Csm4HuD", 216),
          ("capEqp4CfptD", 217),
          ("capEqp2psm", 218),
          ("capEqpWce100G", 219),
          ("capEqp10Wxc10g", 220),
          ("capEqpShx9hu", 221),
          ("capEqpFanXhu", 222),
          ("capEqp10tcc100gtbD", 223),
          ("capEqp9RoadmC96", 224),
          ("capEqp4Wce16g", 225),
          ("capEqpSfpBG", 226),
          ("capEqpSfpCdrG", 227),
          ("capEqp10tce100gGf", 228),
          ("capEqpSfpCdrC", 229),
          ("capEqp5tce10gaes", 234),
          ("capEqp5tce10g", 235),
          ("capEqp5tces10gaes", 236),
          ("capEqp5tces10g", 237),
          ("capEqp4roadmC96", 239),
          ("capEqpWcc100gtbD", 240),
          ("capEqpEdfaS20", 241),
          ("capEqp10tccSdi10g", 242),
          ("capEqp4roadmEC96", 243),
          ("capEqpSfptD", 245),
          ("capEqpSfp2TxG", 246),
          ("capEqpSfp2RxG", 247),
          ("capEqpSfp2Txe", 248),
          ("capEqpSfp2Rxe", 249),
          ("capEqp2EdfaS20S10", 250),
          ("capEqp10Tce100Gb", 251),
          ("capEqp10Tce100gAes", 252),
          ("capEqpSfpCdrD", 253),
          ("capEqpSh1huDcEtemp", 254),
          ("capEqp8psm", 255),
          ("capEqp9ccmC96", 256),
          ("capEqpWce100GB", 257),
          ("capEqp16tcc10G", 258),
          ("capEqp4Wcc10g", 259),
          ("capEqp5wca16G", 260),
          ("capEqpCfptCd", 261),
          ("capEqpWccPcn100g", 264),
          ("capEqpOppm", 267),
          ("capEqp4cfpd", 268),
          ("capEqpNcuS", 269),
          ("capEqp10csmuD", 270),
          ("capEqpUtmS", 272),
          ("capEqpSfpBC", 273),
          ("capEqp10Tce100gAesBsi", 274),
          ("capEqpWccPcn100gAes", 280),
          ("capEqpSfpRxTxG", 282),
          ("capEqpSfpTlnD", 283),
          ("capEqpCfpTfCd", 284),
          ("capEqpXfpBG", 285),
          ("capEqpFd128D", 286),
          ("capEqpSfpBCdrG", 289),
          ("capEqpMroadmC96", 290),
          ("capEqpPsm40Mroadm", 291),
          ("capEqpOsfma", 292),
          ("capEqp10tcc100g", 293),
          ("capEqpCfpTgCd", 294),
          ("capEqpPsm80Mroadm", 295),
          ("capEqp10Tce100gbAes", 297),
          ("capEqpL3CmSina", 298),
          ("capEqp9Tce10gAesG", 300),
          ("capEqp9RoadmRs", 303),
          ("capEqp16psm4", 304),
          ("capEqp96Csm2HuD", 305),
          ("capEqp9Tce10gAesF", 307),
          ("capEqp10Tce100gAesF", 308),
          ("capEqpMtpOscC", 309),
          ("capEqpWcc100gAesF", 311),
          ("capEqpCfpTrCd", 312),
          ("capEqpWcc100gAesB", 314),
          ("capEqpMapOscC", 317),
          ("capEqpMtpbOscC", 318),
          ("capEqpMapbOscC", 319),
          ("capEqpWccPcn100gB", 320),
          ("capEqp4psmS", 321),
          ("capEqpWcc100gAesG", 323),
          ("capEqpHdScm", 324),
          ("capEqpCfp2tgCd", 450),
          ("capEqpMaB2C3LtA", 453),
          ("capEqpMaB5Lt", 454),
          ("capEqpCfp2tCd", 455),
          ("capEqpMp2B4CtS", 456),
          ("capEqpPsmdc3", 457),
          ("capEqpQSfpNotApproved", 458),
          ("capEqpQSfp10g", 459),
          ("capEqpMa2C2C3LtA", 461),
          ("capEqpQSfpDacCr", 462),
          ("capEqpCem3", 463),
          ("capEqpFtm3", 464),
          ("capEqpPsmac3", 465),
          ("capEqpSh1R", 466),
          ("capEqpEcm3", 467),
          ("capEqp4QsfpG", 468),
          ("capEqpScm2", 472),
          ("capEqpMa2C5Lt", 473),
          ("capEqpPsmac6", 474),
          ("capEqpQSfpDac", 475),
          ("capEqpQSfpAoc", 476),
          ("capEqpPsmdc4", 478),
          ("capEqpPsmac5", 479),
          ("capEqpFtm4", 480),
          ("capEqpFtm2", 481),
          ("capEqpPsmac4", 482),
          ("capEqpPsmdc", 483),
          ("capEqpCem2", 485),
          ("capEqpCem4", 486),
          ("capEqpEcm2", 487),
          ("capEqpQSfp4g", 488),
          ("capEqpMp2B4Ct", 489),
          ("capEqpSh12", 490),
          ("capEqpSh4R", 491),
          ("capEqpPtp", 499))
    )


class FspR7FalseTrue(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("false", 1),
          ("true", 2))
    )



class FspR7Time(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d-1d-1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class FspR7YesNo(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )



class FspR7UsersDb(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2),
          ("keepCurrent", 3))
    )



class Grade(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("gradeA", 1),
          ("gradeB", 2),
          ("gradeGdps", 3),
          ("gradeC", 4))
    )



class LoopConfig(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("noLoop", 1),
          ("lineLoop", 2),
          ("inwardLoop", 3))
    )



class LoopConfigCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNoLoop", 1),
          ("capLineLoop", 2),
          ("capInwardLoop", 3))
    )


class DestinationNodeOrAgentState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("inactive", 1))
    )



class NcuAutoActivation(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("no", 1),
          ("yes", 2))
    )



class NoYesNA(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("no", 1),
          ("yes", 2),
          ("notApplicable", 3))
    )



class OhTerminationLevel(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("phys", 1),
          ("otnOtu", 2),
          ("otnOdu", 3),
          ("otnOpu", 4),
          ("sonetSection", 5),
          ("sonetLine", 6),
          ("sonetPath", 7),
          ("none", 8),
          ("pcs", 9),
          ("if10GbE", 10))
    )



class OhTerminationLevelCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capPhys", 1),
          ("capOtnOtu", 2),
          ("capOtnOdu", 3),
          ("capOtnOpu", 4),
          ("capSonetSection", 5),
          ("capSonetLine", 6),
          ("capSonetPath", 7),
          ("capNone", 8),
          ("capPcs", 9),
          ("capIf10GbE", 10))
    )


class OtnPayloadType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7,
              8,
              12,
              15,
              16,
              17,
              18,
              36,
              39,
              41,
              52,
              54,
              55,
              56,
              58,
              85,
              86,
              87,
              88,
              110,
              127,
              129,
              150,
              178,
              192,
              194,
              195,
              196,
              200,
              206,
              212,
              214,
              215,
              499)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ifType10GbE", 3),
          ("ifTypeOc192", 4),
          ("ifTypeOc48", 5),
          ("ifTypeStm16", 6),
          ("ifTypeStm64", 7),
          ("ifType10GFC", 8),
          ("ifType1GFC", 12),
          ("ifTypeF9953", 15),
          ("ifTypeF10312", 16),
          ("ifTypeF10518", 17),
          ("ifTypeF2488", 18),
          ("ifTypeE10or100bt", 36),
          ("ifType2GFC", 39),
          ("ifType1GbE", 41),
          ("ifTypeF4250", 52),
          ("ifTypeF10709", 54),
          ("ifTypeF11095", 55),
          ("ifTypeF11318", 56),
          ("ifType4GFC", 58),
          ("ifTypeStm1", 85),
          ("ifTypeStm4", 86),
          ("ifTypeOc3", 87),
          ("ifTypeOc12", 88),
          ("ifTypeF8500", 110),
          ("ifType8GFC", 127),
          ("ifTypeF10000", 129),
          ("ifTypeF5000", 150),
          ("ifTypeF14025", 178),
          ("ifType40GbE", 192),
          ("ifTypeF41250", 194),
          ("ifTypeF103125", 195),
          ("ifType16GFC", 196),
          ("ifTypeF2457", 200),
          ("ifTypeFe", 206),
          ("ifTypeE10to1000t", 212),
          ("ifType25GbE", 214),
          ("ifType32GFC", 215),
          ("ifTypeNotDefined", 499))
    )



class OtnPayloadTypeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capIfType10GbE", 3),
          ("capIfTypeOc192", 4),
          ("capIfTypeOc48", 5),
          ("capIfTypeStm16", 6),
          ("capIfTypeStm64", 7),
          ("capIfType10GFC", 8),
          ("capIfType1GFC", 12),
          ("capIfTypeF9953", 15),
          ("capIfTypeF10312", 16),
          ("capIfTypeF10518", 17),
          ("capIfTypeF2488", 18),
          ("capIfTypeE10or100bt", 36),
          ("capIfType2GFC", 39),
          ("capIfType1GbE", 41),
          ("capIfTypeF4250", 52),
          ("capIfTypeF10709", 54),
          ("capIfTypeF11095", 55),
          ("capIfTypeF11318", 56),
          ("capIfType4GFC", 58),
          ("capIfTypeStm1", 85),
          ("capIfTypeStm4", 86),
          ("capIfTypeOc3", 87),
          ("capIfTypeOc12", 88),
          ("capIfTypeF8500", 110),
          ("capIfType8GFC", 127),
          ("capIfTypeF10000", 129),
          ("capIfTypeF5000", 150),
          ("capIfTypeF14025", 178),
          ("capIfType40GbE", 192),
          ("capIfTypeF41250", 194),
          ("capIfTypeF103125", 195),
          ("capIfType16GFC", 196),
          ("capIfTypeF2457", 200),
          ("capIfTypeFe", 206),
          ("capIfTypeE10to1000t", 212),
          ("capIfType25GbE", 214),
          ("capIfType32GFC", 215),
          ("capIfTypeNotDefined", 499))
    )


class OtnTcmLevel(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6),
          ("disabled", 7))
    )



class OtnTcmLevelCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capTcm1", 1),
          ("capTcm2", 2),
          ("capTcm3", 3),
          ("capTcm4", 4),
          ("capTcm5", 5),
          ("capTcm6", 6),
          ("capDisabled", 7))
    )


class PgmType(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("null", 1),
          ("ncu", 2),
          ("ncuHp", 3),
          ("fwps", 4),
          ("legacy", 5),
          ("nscuS", 6),
          ("fwpe", 7))
    )



class ProtectionMech(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("pathProtection", 1),
          ("channelCardProtection", 2),
          ("channelProtection", 3),
          ("versatileSwitchedProtection", 4),
          ("flowProtection", 5),
          ("clientCardProtection", 6),
          ("controller", 7),
          ("none", 8))
    )



class ProtectionMechCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capPathProtection", 1),
          ("capChannelCardProtection", 2),
          ("capChannelProtection", 3),
          ("capVersatileSwitchedProtection", 4),
          ("capFlowProtection", 5),
          ("capClientCardProtection", 6),
          ("capController", 7),
          ("capNone", 8))
    )


class RestoreActivation(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("notRestore", 1),
          ("restoreFromStdBy", 2),
          ("restoreToFactory", 3),
          ("restoreFromEqpt", 4),
          ("acceptDatabase", 5))
    )



class RestoreActivationCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNotRestore", 1),
          ("capRestoreFromStdBy", 2),
          ("capRestoreToFactory", 3),
          ("capRestoreFromEqpt", 4),
          ("capAcceptDatabase", 5))
    )


class ServiceAffecting(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("nsa", 1),
          ("sa", 2),
          ("saActivate", 3),
          ("saInstall", 4),
          ("none", 5))
    )



class ServiceAffectingCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNsa", 1),
          ("capSa", 2),
          ("capSaActivate", 3),
          ("capSaInstall", 4),
          ("capNone", 5))
    )


class StandbyServiceAffecting(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("nsa", 1),
          ("sa", 2),
          ("saActivate", 3),
          ("saInstall", 4),
          ("none", 5))
    )



class SnmpProxySynchronizationState(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("inactive", 1),
          ("active", 2))
    )



class SnmpProxySynchronizationStage(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("started", 1),
          ("finished", 2))
    )



class SonetSectSigDegThres(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("ber10exp5", 1),
          ("ber10exp6", 2),
          ("ber10exp7", 3),
          ("ber10exp8", 4),
          ("ber10exp9", 5))
    )



class SonetSectSigDegThresCaps(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("capBer10exp5", 1),
          ("capBer10exp6", 2),
          ("capBer10exp7", 3),
          ("capBer10exp8", 4),
          ("capBer10exp9", 5))
    )



class SonetTimingSource(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("loopTiming", 1),
          ("internal", 2))
    )



class SonetTimingSourceCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capLoopTiming", 1),
          ("capInternal", 2))
    )


class SonetTraceForm(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("form64CRLF", 1),
          ("form16CRC7", 2),
          ("form1Byte", 3))
    )



class SonetTraceFormCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capForm64CRLF", 1),
          ("capForm16CRC7", 2),
          ("capForm1Byte", 3))
    )


class SonetVcBundleAllocation(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class SonetVcBundleAllocationCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("vc1", 0),
          ("vc2", 1),
          ("vc3", 2),
          ("vc4", 3),
          ("vc5", 4),
          ("vc6", 5),
          ("vc7", 6),
          ("vc8", 7),
          ("vc9", 8),
          ("vc10", 9),
          ("vc11", 10),
          ("vc12", 11),
          ("vc13", 12),
          ("vc14", 13),
          ("vc15", 14),
          ("vc16", 15),
          ("vc17", 16),
          ("vc18", 17),
          ("vc19", 18),
          ("vc20", 19),
          ("vc21", 20),
          ("vc22", 21),
          ("vc23", 22),
          ("vc24", 23),
          ("vc25", 24),
          ("vc26", 25),
          ("vc27", 26),
          ("vc28", 27),
          ("vc29", 28),
          ("vc30", 29),
          ("vc31", 30),
          ("vc32", 31),
          ("vc33", 32),
          ("vc34", 33),
          ("vc35", 34),
          ("vc36", 35),
          ("vc37", 36),
          ("vc38", 37),
          ("vc39", 38),
          ("vc40", 39),
          ("vc41", 40),
          ("vc42", 41),
          ("vc43", 42),
          ("vc44", 43),
          ("vc45", 44),
          ("vc46", 45),
          ("vc47", 46),
          ("vc48", 47),
          ("vc49", 48),
          ("vc50", 49),
          ("vc51", 50),
          ("vc52", 51),
          ("vc53", 52),
          ("vc54", 53),
          ("vc55", 54),
          ("vc56", 55),
          ("vc57", 56),
          ("vc58", 57),
          ("vc59", 58),
          ("vc60", 59),
          ("vc61", 60),
          ("vc62", 61),
          ("vc63", 62),
          ("vc64", 63))
    )


class TimMode(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("disabled", 1),
          ("enableAisDisabled", 2),
          ("enableAisEnabled", 3))
    )



class TimModeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capDisabled", 1),
          ("capEnableAisDisabled", 2),
          ("capEnableAisEnabled", 3))
    )


class FspR7TrapsinkLifetime(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("duration1hour", 1),
          ("duration1day", 2),
          ("duration3days", 3),
          ("duration1week", 4),
          ("duration1month", 5),
          ("unlimited", 6))
    )



class VirtualContainerType(TextualConvention, Integer32):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("vc4Type", 1),
          ("vc3Au4Type", 2),
          ("sts1", 3),
          ("sts3c", 4),
          ("vs1", 5),
          ("vs2c", 6),
          ("sts24c", 7),
          ("sts48c", 8),
          ("vs4c", 9),
          ("vc4c8", 10),
          ("vc4c16", 11),
          ("vs0", 12),
          ("vs3c", 13),
          ("vs5c", 14),
          ("vs8c", 15),
          ("vs6c", 16),
          ("odu0", 17),
          ("odu1", 18),
          ("oduFlex", 19),
          ("vs7c", 20))
    )



class VirtualContainerTypeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capVc4Type", 1),
          ("capVc3Au4Type", 2),
          ("capSts1", 3),
          ("capSts3c", 4),
          ("capVs1", 5),
          ("capVs2c", 6),
          ("capSts24c", 7),
          ("capSts48c", 8),
          ("capVs4c", 9),
          ("capVc4c8", 10),
          ("capVc4c16", 11),
          ("capVs0", 12),
          ("capVs3c", 13),
          ("capVs5c", 14),
          ("capVs8c", 15),
          ("capVs6c", 16),
          ("capOdu0", 17),
          ("capOdu1", 18),
          ("capOduFlex", 19),
          ("capVs7c", 20))
    )


class YesNoNA(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2),
          ("notApplicable", 3))
    )



class LogicalIfTransport(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class LogicalIfTransportCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("lif1", 0),
          ("lif2", 1),
          ("lif3", 2),
          ("lif4", 3),
          ("lif5", 4),
          ("lif6", 5),
          ("lif7", 6),
          ("lif8", 7),
          ("lif9", 8),
          ("lif10", 9),
          ("lif11", 10),
          ("lif12", 11),
          ("lif13", 12),
          ("lif14", 13),
          ("lif15", 14),
          ("lif16", 15))
    )


class ModuleForm(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("native", 1),
          ("legacy", 2),
          ("compatible", 3),
          ("cloudConnect", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1)
)
_Fsp3000_ObjectIdentity = ObjectIdentity
fsp3000 = _Fsp3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 4)
)
_Fsp1000_ObjectIdentity = ObjectIdentity
fsp1000 = _Fsp1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6)
)
_Fsp2000_ObjectIdentity = ObjectIdentity
fsp2000 = _Fsp2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 7)
)
_Fsp1000adm_ObjectIdentity = ObjectIdentity
fsp1000adm = _Fsp1000adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 8)
)
_Fsp1500_ObjectIdentity = ObjectIdentity
fsp1500 = _Fsp1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 9)
)
_Fsp150_ObjectIdentity = ObjectIdentity
fsp150 = _Fsp150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10)
)
_FspR7_ObjectIdentity = ObjectIdentity
fspR7 = _FspR7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11)
)
_Fsp150cm_ObjectIdentity = ObjectIdentity
fsp150cm = _Fsp150cm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12)
)
_FspNm_ObjectIdentity = ObjectIdentity
fspNm = _FspNm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 13)
)
_Fsp3000alm_ObjectIdentity = ObjectIdentity
fsp3000alm = _Fsp3000alm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14)
)
_Aos_ObjectIdentity = ObjectIdentity
aos = _Aos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20)
)
_AosCommon_ObjectIdentity = ObjectIdentity
aosCommon = _AosCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1)
)
_AosProducts_ObjectIdentity = ObjectIdentity
aosProducts = _AosProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2)
)
_Fsp3000c_ObjectIdentity = ObjectIdentity
fsp3000c = _Fsp3000c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1)
)
_Fspxg480_ObjectIdentity = ObjectIdentity
fspxg480 = _Fspxg480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 2)
)
_Fspxg404_ObjectIdentity = ObjectIdentity
fspxg404 = _Fspxg404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 3)
)
_Fspxg418_ObjectIdentity = ObjectIdentity
fspxg418 = _Fspxg418_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 4)
)
_Fspxg480_25g_100g_ObjectIdentity = ObjectIdentity
fspxg480_25g_100g = _Fspxg480_25g_100g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 5)
)
_Fspxg480_100g_ObjectIdentity = ObjectIdentity
fspxg480_100g = _Fspxg480_100g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 6)
)
_Fspxg480_100gcfp2_ObjectIdentity = ObjectIdentity
fspxg480_100gcfp2 = _Fspxg480_100gcfp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 7)
)
_Fspxg404_100g_ObjectIdentity = ObjectIdentity
fspxg404_100g = _Fspxg404_100g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 8)
)
_Fspxg404_100gcfp2_ObjectIdentity = ObjectIdentity
fspxg404_100gcfp2 = _Fspxg404_100gcfp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 9)
)
_Fspxg418_100g_ObjectIdentity = ObjectIdentity
fspxg418_100g = _Fspxg418_100g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 10)
)
_Fspxg418_100gcfp2_ObjectIdentity = ObjectIdentity
fspxg418_100gcfp2 = _Fspxg418_100gcfp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 11)
)
_Fspxg118pro_cshac_ObjectIdentity = ObjectIdentity
fspxg118pro_cshac = _Fspxg118pro_cshac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 12)
)
_Fspxg118pro_cshdc_ObjectIdentity = ObjectIdentity
fspxg118pro_cshdc = _Fspxg118pro_cshdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 13)
)
_Fspxg118pro_cshac_g_ObjectIdentity = ObjectIdentity
fspxg118pro_cshac_g = _Fspxg118pro_cshac_g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 14)
)
_Fspxg118pro_cshdc_g_ObjectIdentity = ObjectIdentity
fspxg118pro_cshdc_g = _Fspxg118pro_cshdc_g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 15)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2)
)
_NeInfo_ObjectIdentity = ObjectIdentity
neInfo = _NeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1)
)


class _NeMibVariant_Type(Integer32):
    """Custom type neMibVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_NeMibVariant_Type.__name__ = "Integer32"
_NeMibVariant_Object = MibScalar
neMibVariant = _NeMibVariant_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 1),
    _NeMibVariant_Type()
)
neMibVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMibVariant.setStatus("current")
_NeManufacturer_Type = SnmpAdminString
_NeManufacturer_Object = MibScalar
neManufacturer = _NeManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 2),
    _NeManufacturer_Type()
)
neManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neManufacturer.setStatus("current")
_NeDateAndTime_Type = DateAndTime
_NeDateAndTime_Object = MibScalar
neDateAndTime = _NeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 3),
    _NeDateAndTime_Type()
)
neDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neDateAndTime.setStatus("current")
_NeMemorySizeTotal_Type = KBytes
_NeMemorySizeTotal_Object = MibScalar
neMemorySizeTotal = _NeMemorySizeTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 4),
    _NeMemorySizeTotal_Type()
)
neMemorySizeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMemorySizeTotal.setStatus("current")
if mibBuilder.loadTexts:
    neMemorySizeTotal.setUnits("kBytes")
_NeMemorySizeFree_Type = KBytes
_NeMemorySizeFree_Object = MibScalar
neMemorySizeFree = _NeMemorySizeFree_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 5),
    _NeMemorySizeFree_Type()
)
neMemorySizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMemorySizeFree.setStatus("current")
if mibBuilder.loadTexts:
    neMemorySizeFree.setUnits("kBytes")
_NeStorageTable_Object = MibTable
neStorageTable = _NeStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 6)
)
if mibBuilder.loadTexts:
    neStorageTable.setStatus("current")
_NeStorageEntry_Object = MibTableRow
neStorageEntry = _NeStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1)
)
neStorageEntry.setIndexNames(
    (0, "ADVA-MIB", "neStorageIndex"),
)
if mibBuilder.loadTexts:
    neStorageEntry.setStatus("current")
_NeStorageIndex_Type = Unsigned32
_NeStorageIndex_Object = MibTableColumn
neStorageIndex = _NeStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 1),
    _NeStorageIndex_Type()
)
neStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neStorageIndex.setStatus("current")
_NeStorageDescr_Type = SnmpAdminString
_NeStorageDescr_Object = MibTableColumn
neStorageDescr = _NeStorageDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 2),
    _NeStorageDescr_Type()
)
neStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStorageDescr.setStatus("current")
_NeStorageCapacity_Type = KBytes
_NeStorageCapacity_Object = MibTableColumn
neStorageCapacity = _NeStorageCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 3),
    _NeStorageCapacity_Type()
)
neStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStorageCapacity.setStatus("current")
if mibBuilder.loadTexts:
    neStorageCapacity.setUnits("kBytes")
_NeStorageAvailable_Type = KBytes
_NeStorageAvailable_Object = MibTableColumn
neStorageAvailable = _NeStorageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 4),
    _NeStorageAvailable_Type()
)
neStorageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStorageAvailable.setStatus("current")
if mibBuilder.loadTexts:
    neStorageAvailable.setUnits("kBytes")
_NeAlarmStatus_Type = TrapAlarmSeverity
_NeAlarmStatus_Object = MibScalar
neAlarmStatus = _NeAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 1, 7),
    _NeAlarmStatus_Type()
)
neAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmStatus.setStatus("current")
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 2)
)
_SnmpWriteAccessRestriction_Type = EnableState
_SnmpWriteAccessRestriction_Object = MibScalar
snmpWriteAccessRestriction = _SnmpWriteAccessRestriction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 2, 1),
    _SnmpWriteAccessRestriction_Type()
)
snmpWriteAccessRestriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpWriteAccessRestriction.setStatus("current")
_SnmpWriteAccessTable_Object = MibTable
snmpWriteAccessTable = _SnmpWriteAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 2, 2)
)
if mibBuilder.loadTexts:
    snmpWriteAccessTable.setStatus("current")
_SnmpWriteAccessEntry_Object = MibTableRow
snmpWriteAccessEntry = _SnmpWriteAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1)
)
snmpWriteAccessEntry.setIndexNames(
    (0, "ADVA-MIB", "snmpWriteAccessNmsAddress"),
)
if mibBuilder.loadTexts:
    snmpWriteAccessEntry.setStatus("current")
_SnmpWriteAccessNmsAddress_Type = IpAddress
_SnmpWriteAccessNmsAddress_Object = MibTableColumn
snmpWriteAccessNmsAddress = _SnmpWriteAccessNmsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1, 1),
    _SnmpWriteAccessNmsAddress_Type()
)
snmpWriteAccessNmsAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpWriteAccessNmsAddress.setStatus("current")
_SnmpWriteAccessNmsName_Type = SnmpAdminString
_SnmpWriteAccessNmsName_Object = MibTableColumn
snmpWriteAccessNmsName = _SnmpWriteAccessNmsName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1, 2),
    _SnmpWriteAccessNmsName_Type()
)
snmpWriteAccessNmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpWriteAccessNmsName.setStatus("current")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3)
)
_NeEventsLogged_Type = TrapCounter
_NeEventsLogged_Object = MibScalar
neEventsLogged = _NeEventsLogged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 1),
    _NeEventsLogged_Type()
)
neEventsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventsLogged.setStatus("current")
_NeEventLogTable_Object = MibTable
neEventLogTable = _NeEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 2)
)
if mibBuilder.loadTexts:
    neEventLogTable.setStatus("current")
_NeEventLogEntry_Object = MibTableRow
neEventLogEntry = _NeEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1)
)
neEventLogEntry.setIndexNames(
    (0, "ADVA-MIB", "neEventLogIndex"),
)
if mibBuilder.loadTexts:
    neEventLogEntry.setStatus("current")
_NeEventLogIndex_Type = TrapCounter
_NeEventLogIndex_Object = MibTableColumn
neEventLogIndex = _NeEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 1),
    _NeEventLogIndex_Type()
)
neEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neEventLogIndex.setStatus("current")
_NeEventLogTimeStamp_Type = DateAndTime
_NeEventLogTimeStamp_Object = MibTableColumn
neEventLogTimeStamp = _NeEventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 2),
    _NeEventLogTimeStamp_Type()
)
neEventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogTimeStamp.setStatus("current")
_NeEventLogNotificationOID_Type = ObjectIdentifier
_NeEventLogNotificationOID_Object = MibTableColumn
neEventLogNotificationOID = _NeEventLogNotificationOID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 3),
    _NeEventLogNotificationOID_Type()
)
neEventLogNotificationOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogNotificationOID.setStatus("current")
_NeEventLogIdentityTranslation_Type = IdentityTranslation
_NeEventLogIdentityTranslation_Object = MibTableColumn
neEventLogIdentityTranslation = _NeEventLogIdentityTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 4),
    _NeEventLogIdentityTranslation_Type()
)
neEventLogIdentityTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogIdentityTranslation.setStatus("current")
_NeEventLogVarTable_Object = MibTable
neEventLogVarTable = _NeEventLogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3)
)
if mibBuilder.loadTexts:
    neEventLogVarTable.setStatus("current")
_NeEventLogVarEntry_Object = MibTableRow
neEventLogVarEntry = _NeEventLogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1)
)
neEventLogVarEntry.setIndexNames(
    (0, "ADVA-MIB", "neEventLogIndex"),
    (0, "ADVA-MIB", "neEventLogVarIndex"),
)
if mibBuilder.loadTexts:
    neEventLogVarEntry.setStatus("current")
_NeEventLogVarIndex_Type = Unsigned32
_NeEventLogVarIndex_Object = MibTableColumn
neEventLogVarIndex = _NeEventLogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 1),
    _NeEventLogVarIndex_Type()
)
neEventLogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neEventLogVarIndex.setStatus("current")
_NeEventLogVarId_Type = ObjectIdentifier
_NeEventLogVarId_Object = MibTableColumn
neEventLogVarId = _NeEventLogVarId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 2),
    _NeEventLogVarId_Type()
)
neEventLogVarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarId.setStatus("current")


class _NeEventLogVarType_Type(Integer32):
    """Custom type neEventLogVarType based on Integer32"""
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
        *(("integer32", 1),
          ("ipAddress", 2),
          ("octetString", 3),
          ("objectId", 4),
          ("counter64", 5),
          ("unsigned32", 7))
    )


_NeEventLogVarType_Type.__name__ = "Integer32"
_NeEventLogVarType_Object = MibTableColumn
neEventLogVarType = _NeEventLogVarType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 3),
    _NeEventLogVarType_Type()
)
neEventLogVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarType.setStatus("current")
_NeEventLogVarInteger32Val_Type = Integer32
_NeEventLogVarInteger32Val_Object = MibTableColumn
neEventLogVarInteger32Val = _NeEventLogVarInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 4),
    _NeEventLogVarInteger32Val_Type()
)
neEventLogVarInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarInteger32Val.setStatus("current")
_NeEventLogVarIpAddressVal_Type = IpAddress
_NeEventLogVarIpAddressVal_Object = MibTableColumn
neEventLogVarIpAddressVal = _NeEventLogVarIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 5),
    _NeEventLogVarIpAddressVal_Type()
)
neEventLogVarIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarIpAddressVal.setStatus("current")


class _NeEventLogVarOctetStringVal_Type(OctetString):
    """Custom type neEventLogVarOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NeEventLogVarOctetStringVal_Type.__name__ = "OctetString"
_NeEventLogVarOctetStringVal_Object = MibTableColumn
neEventLogVarOctetStringVal = _NeEventLogVarOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 6),
    _NeEventLogVarOctetStringVal_Type()
)
neEventLogVarOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarOctetStringVal.setStatus("current")
_NeEventLogVarOidVal_Type = ObjectIdentifier
_NeEventLogVarOidVal_Object = MibTableColumn
neEventLogVarOidVal = _NeEventLogVarOidVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 7),
    _NeEventLogVarOidVal_Type()
)
neEventLogVarOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarOidVal.setStatus("current")
_NeEventLogVarCounter64Val_Type = Counter64
_NeEventLogVarCounter64Val_Object = MibTableColumn
neEventLogVarCounter64Val = _NeEventLogVarCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 8),
    _NeEventLogVarCounter64Val_Type()
)
neEventLogVarCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarCounter64Val.setStatus("current")
_NeEventLogVarUnsigned32Val_Type = Unsigned32
_NeEventLogVarUnsigned32Val_Object = MibTableColumn
neEventLogVarUnsigned32Val = _NeEventLogVarUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 10),
    _NeEventLogVarUnsigned32Val_Type()
)
neEventLogVarUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neEventLogVarUnsigned32Val.setStatus("current")
_NeTrapsinkTable_Object = MibTable
neTrapsinkTable = _NeTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4)
)
if mibBuilder.loadTexts:
    neTrapsinkTable.setStatus("current")
_NeTrapsinkEntry_Object = MibTableRow
neTrapsinkEntry = _NeTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1)
)
neTrapsinkEntry.setIndexNames(
    (0, "ADVA-MIB", "neTrapsinkAddress"),
    (0, "ADVA-MIB", "neTrapsinkPort"),
)
if mibBuilder.loadTexts:
    neTrapsinkEntry.setStatus("current")
_NeTrapsinkAddress_Type = IpAddress
_NeTrapsinkAddress_Object = MibTableColumn
neTrapsinkAddress = _NeTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 1),
    _NeTrapsinkAddress_Type()
)
neTrapsinkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    neTrapsinkAddress.setStatus("current")


class _NeTrapsinkPort_Type(Integer32):
    """Custom type neTrapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NeTrapsinkPort_Type.__name__ = "Integer32"
_NeTrapsinkPort_Object = MibTableColumn
neTrapsinkPort = _NeTrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 2),
    _NeTrapsinkPort_Type()
)
neTrapsinkPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neTrapsinkPort.setStatus("current")


class _NeTrapsinkCommunity_Type(DisplayString):
    """Custom type neTrapsinkCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NeTrapsinkCommunity_Type.__name__ = "DisplayString"
_NeTrapsinkCommunity_Object = MibTableColumn
neTrapsinkCommunity = _NeTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 3),
    _NeTrapsinkCommunity_Type()
)
neTrapsinkCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkCommunity.setStatus("current")
_NeTrapsinkRowStatus_Type = RowStatus
_NeTrapsinkRowStatus_Object = MibTableColumn
neTrapsinkRowStatus = _NeTrapsinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 4),
    _NeTrapsinkRowStatus_Type()
)
neTrapsinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkRowStatus.setStatus("current")
_NeTrapsinkVersion_Type = Unsigned32
_NeTrapsinkVersion_Object = MibTableColumn
neTrapsinkVersion = _NeTrapsinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 5),
    _NeTrapsinkVersion_Type()
)
neTrapsinkVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkVersion.setStatus("current")
_NeTrapsinkUserName_Type = DisplayString
_NeTrapsinkUserName_Object = MibTableColumn
neTrapsinkUserName = _NeTrapsinkUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 6),
    _NeTrapsinkUserName_Type()
)
neTrapsinkUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkUserName.setStatus("current")
_NeTrapsinkType_Type = FspR7TrapsinkLifetime
_NeTrapsinkType_Object = MibTableColumn
neTrapsinkType = _NeTrapsinkType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 7),
    _NeTrapsinkType_Type()
)
neTrapsinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neTrapsinkType.setStatus("current")
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4)
)
_SwVersionTable_Object = MibTable
swVersionTable = _SwVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 1)
)
if mibBuilder.loadTexts:
    swVersionTable.setStatus("current")
_SwVersionEntry_Object = MibTableRow
swVersionEntry = _SwVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1)
)
swVersionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    swVersionEntry.setStatus("current")
_SwVersionActiveApplSw_Type = SnmpAdminString
_SwVersionActiveApplSw_Object = MibTableColumn
swVersionActiveApplSw = _SwVersionActiveApplSw_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 1),
    _SwVersionActiveApplSw_Type()
)
swVersionActiveApplSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionActiveApplSw.setStatus("current")
_SwVersionInactiveApplSw_Type = SnmpAdminString
_SwVersionInactiveApplSw_Object = MibTableColumn
swVersionInactiveApplSw = _SwVersionInactiveApplSw_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 2),
    _SwVersionInactiveApplSw_Type()
)
swVersionInactiveApplSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionInactiveApplSw.setStatus("current")
_SwVersionActiveOperatingSw_Type = SnmpAdminString
_SwVersionActiveOperatingSw_Object = MibTableColumn
swVersionActiveOperatingSw = _SwVersionActiveOperatingSw_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 3),
    _SwVersionActiveOperatingSw_Type()
)
swVersionActiveOperatingSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionActiveOperatingSw.setStatus("current")
_SwVersionInactiveOperatingSw_Type = SnmpAdminString
_SwVersionInactiveOperatingSw_Object = MibTableColumn
swVersionInactiveOperatingSw = _SwVersionInactiveOperatingSw_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 4),
    _SwVersionInactiveOperatingSw_Type()
)
swVersionInactiveOperatingSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionInactiveOperatingSw.setStatus("current")


class _SwVersionNextBoot_Type(Integer32):
    """Custom type swVersionNextBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeVersion", 1),
          ("inactiveVersion", 2))
    )


_SwVersionNextBoot_Type.__name__ = "Integer32"
_SwVersionNextBoot_Object = MibTableColumn
swVersionNextBoot = _SwVersionNextBoot_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 5),
    _SwVersionNextBoot_Type()
)
swVersionNextBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionNextBoot.setStatus("current")
_NeSoftwareUpgrade_ObjectIdentity = ObjectIdentity
neSoftwareUpgrade = _NeSoftwareUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2)
)


class _NeSwUpgradeRequest_Type(Integer32):
    """Custom type neSwUpgradeRequest based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("download", 2),
          ("install", 3),
          ("activate", 4),
          ("revertToPrevious", 5),
          ("reboot", 6),
          ("downloadInstallActivateReboot", 7),
          ("installActivateReboot", 8),
          ("revertToPreviousReboot", 9),
          ("activateAlp", 10),
          ("activateDefaultAlp", 11),
          ("upload", 12),
          ("autoDownloadInstall", 13),
          ("autoInstall", 14),
          ("fwpInstall", 15),
          ("fwpDownloadInstall", 16),
          ("downloadCf", 17),
          ("uploadCf", 18),
          ("installCf", 19),
          ("autoInstallCf", 20),
          ("uploadPa", 21),
          ("activateWithFwp", 22),
          ("forceReboot", 23),
          ("stbyFwpInstall", 24))
    )


_NeSwUpgradeRequest_Type.__name__ = "Integer32"
_NeSwUpgradeRequest_Object = MibScalar
neSwUpgradeRequest = _NeSwUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 1),
    _NeSwUpgradeRequest_Type()
)
neSwUpgradeRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeRequest.setStatus("current")
_NeSwUpgradeState_Type = NeSwUpgradeStatusType
_NeSwUpgradeState_Object = MibScalar
neSwUpgradeState = _NeSwUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 2),
    _NeSwUpgradeState_Type()
)
neSwUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neSwUpgradeState.setStatus("current")
_NeSwUpgradeServerAddress_Type = IpAddress
_NeSwUpgradeServerAddress_Object = MibScalar
neSwUpgradeServerAddress = _NeSwUpgradeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 3),
    _NeSwUpgradeServerAddress_Type()
)
neSwUpgradeServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeServerAddress.setStatus("current")
_NeSwUpgradeServerLogin_Type = SnmpAdminString
_NeSwUpgradeServerLogin_Object = MibScalar
neSwUpgradeServerLogin = _NeSwUpgradeServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 4),
    _NeSwUpgradeServerLogin_Type()
)
neSwUpgradeServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeServerLogin.setStatus("current")
_NeSwUpgradeServerPasswd_Type = SnmpAdminString
_NeSwUpgradeServerPasswd_Object = MibScalar
neSwUpgradeServerPasswd = _NeSwUpgradeServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 5),
    _NeSwUpgradeServerPasswd_Type()
)
neSwUpgradeServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeServerPasswd.setStatus("current")
_NeSwUpgradeServerDirectory_Type = SnmpAdminString
_NeSwUpgradeServerDirectory_Object = MibScalar
neSwUpgradeServerDirectory = _NeSwUpgradeServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 6),
    _NeSwUpgradeServerDirectory_Type()
)
neSwUpgradeServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeServerDirectory.setStatus("current")
_NeSwUpgradeFileName_Type = SnmpAdminString
_NeSwUpgradeFileName_Object = MibScalar
neSwUpgradeFileName = _NeSwUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 7),
    _NeSwUpgradeFileName_Type()
)
neSwUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeFileName.setStatus("current")
_NeSwUpgradeNeDirectory_Type = SnmpAdminString
_NeSwUpgradeNeDirectory_Object = MibScalar
neSwUpgradeNeDirectory = _NeSwUpgradeNeDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 8),
    _NeSwUpgradeNeDirectory_Type()
)
neSwUpgradeNeDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neSwUpgradeNeDirectory.setStatus("current")
_NeSwUpgradeTransferProtocol_Type = FileTransferProtocol
_NeSwUpgradeTransferProtocol_Object = MibScalar
neSwUpgradeTransferProtocol = _NeSwUpgradeTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 9),
    _NeSwUpgradeTransferProtocol_Type()
)
neSwUpgradeTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeTransferProtocol.setStatus("current")
_SourceIpAddress_Type = SourceIpAddress
_SourceIpAddress_Object = MibScalar
sourceIpAddress = _SourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 10),
    _SourceIpAddress_Type()
)
sourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceIpAddress.setStatus("current")
_NeSwInstallState_Type = NeSwInstallStatusType
_NeSwInstallState_Object = MibScalar
neSwInstallState = _NeSwInstallState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 11),
    _NeSwInstallState_Type()
)
neSwInstallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neSwInstallState.setStatus("current")


class _NeSwUpgradeType_Type(Integer32):
    """Custom type neSwUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("legacy", 1),
          ("revised", 2))
    )


_NeSwUpgradeType_Type.__name__ = "Integer32"
_NeSwUpgradeType_Object = MibScalar
neSwUpgradeType = _NeSwUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 12),
    _NeSwUpgradeType_Type()
)
neSwUpgradeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeType.setStatus("current")


class _NeSwDownloadProgress_Type(Integer32):
    """Custom type neSwDownloadProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_NeSwDownloadProgress_Type.__name__ = "Integer32"
_NeSwDownloadProgress_Object = MibScalar
neSwDownloadProgress = _NeSwDownloadProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 13),
    _NeSwDownloadProgress_Type()
)
neSwDownloadProgress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neSwDownloadProgress.setStatus("current")
if mibBuilder.loadTexts:
    neSwDownloadProgress.setUnits("%")
_NeSwUpgradeCommonIpSrv_Type = SnmpAdminString
_NeSwUpgradeCommonIpSrv_Object = MibScalar
neSwUpgradeCommonIpSrv = _NeSwUpgradeCommonIpSrv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 14),
    _NeSwUpgradeCommonIpSrv_Type()
)
neSwUpgradeCommonIpSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSwUpgradeCommonIpSrv.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5)
)
_ProvContainerTable_Object = MibTable
provContainerTable = _ProvContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 1)
)
if mibBuilder.loadTexts:
    provContainerTable.setStatus("current")
_ProvContainerEntry_Object = MibTableRow
provContainerEntry = _ProvContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1)
)
provContainerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    provContainerEntry.setStatus("current")


class _ProvAssignmentState_Type(Integer32):
    """Custom type provAssignmentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("unassigned", 2))
    )


_ProvAssignmentState_Type.__name__ = "Integer32"
_ProvAssignmentState_Object = MibTableColumn
provAssignmentState = _ProvAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1, 1),
    _ProvAssignmentState_Type()
)
provAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provAssignmentState.setStatus("current")


class _ProvEquipmentState_Type(Integer32):
    """Custom type provEquipmentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unequipped", 2),
          ("invalid", 3))
    )


_ProvEquipmentState_Type.__name__ = "Integer32"
_ProvEquipmentState_Object = MibTableColumn
provEquipmentState = _ProvEquipmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1, 2),
    _ProvEquipmentState_Type()
)
provEquipmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provEquipmentState.setStatus("current")
_NeBackupRestore_ObjectIdentity = ObjectIdentity
neBackupRestore = _NeBackupRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2)
)


class _NeBackupRestoreRequest_Type(Integer32):
    """Custom type neBackupRestoreRequest based on Integer32"""
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
        *(("none", 1),
          ("runBackup", 2),
          ("runRestore", 3),
          ("dBdownload", 4),
          ("dBupload", 5),
          ("dbDownloadScu", 6),
          ("dbUploadScu", 7),
          ("alpDownload", 8),
          ("alpUpload", 9),
          ("runBackupScu", 10))
    )


_NeBackupRestoreRequest_Type.__name__ = "Integer32"
_NeBackupRestoreRequest_Object = MibScalar
neBackupRestoreRequest = _NeBackupRestoreRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 1),
    _NeBackupRestoreRequest_Type()
)
neBackupRestoreRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neBackupRestoreRequest.setStatus("current")


class _NeBackupRestoreState_Type(Integer32):
    """Custom type neBackupRestoreState based on Integer32"""
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
        *(("noBackupAvailable", 1),
          ("backupInProgress", 2),
          ("backupAvailable", 3),
          ("restoreInProgress", 4),
          ("backupRestoreFail", 5),
          ("backupRestoreIdle", 6),
          ("backupRestoreCompleted", 7),
          ("dbActivationFailed", 8),
          ("dbActivationInProgress", 9))
    )


_NeBackupRestoreState_Type.__name__ = "Integer32"
_NeBackupRestoreState_Object = MibScalar
neBackupRestoreState = _NeBackupRestoreState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 2),
    _NeBackupRestoreState_Type()
)
neBackupRestoreState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neBackupRestoreState.setStatus("current")
_NeBackupRestoreFile_Type = SnmpAdminString
_NeBackupRestoreFile_Object = MibScalar
neBackupRestoreFile = _NeBackupRestoreFile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 3),
    _NeBackupRestoreFile_Type()
)
neBackupRestoreFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neBackupRestoreFile.setStatus("current")
_NeRestoreFileBackupDate_Type = DateAndTime
_NeRestoreFileBackupDate_Object = MibScalar
neRestoreFileBackupDate = _NeRestoreFileBackupDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 4),
    _NeRestoreFileBackupDate_Type()
)
neRestoreFileBackupDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neRestoreFileBackupDate.setStatus("current")
_NeF7AutomaticRemoteBackupSrvIp_Type = IpAddress
_NeF7AutomaticRemoteBackupSrvIp_Object = MibScalar
neF7AutomaticRemoteBackupSrvIp = _NeF7AutomaticRemoteBackupSrvIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 5),
    _NeF7AutomaticRemoteBackupSrvIp_Type()
)
neF7AutomaticRemoteBackupSrvIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupSrvIp.setStatus("current")
_NeF7AutomaticRemoteBackupSrvDir_Type = SnmpAdminString
_NeF7AutomaticRemoteBackupSrvDir_Object = MibScalar
neF7AutomaticRemoteBackupSrvDir = _NeF7AutomaticRemoteBackupSrvDir_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 6),
    _NeF7AutomaticRemoteBackupSrvDir_Type()
)
neF7AutomaticRemoteBackupSrvDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupSrvDir.setStatus("current")
_NeF7AutomaticRemoteBackupSrvLogin_Type = SnmpAdminString
_NeF7AutomaticRemoteBackupSrvLogin_Object = MibScalar
neF7AutomaticRemoteBackupSrvLogin = _NeF7AutomaticRemoteBackupSrvLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 7),
    _NeF7AutomaticRemoteBackupSrvLogin_Type()
)
neF7AutomaticRemoteBackupSrvLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupSrvLogin.setStatus("current")
_NeF7AutomaticRemoteBackupSrvPass_Type = SnmpAdminString
_NeF7AutomaticRemoteBackupSrvPass_Object = MibScalar
neF7AutomaticRemoteBackupSrvPass = _NeF7AutomaticRemoteBackupSrvPass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 8),
    _NeF7AutomaticRemoteBackupSrvPass_Type()
)
neF7AutomaticRemoteBackupSrvPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupSrvPass.setStatus("current")
_NeF7AutomaticRemoteBackupProtocol_Type = FileTransferProtocol
_NeF7AutomaticRemoteBackupProtocol_Object = MibScalar
neF7AutomaticRemoteBackupProtocol = _NeF7AutomaticRemoteBackupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 10),
    _NeF7AutomaticRemoteBackupProtocol_Type()
)
neF7AutomaticRemoteBackupProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupProtocol.setStatus("current")
_NeF7AutomaticRemoteBackupSrcIp_Type = SourceIpAddress
_NeF7AutomaticRemoteBackupSrcIp_Object = MibScalar
neF7AutomaticRemoteBackupSrcIp = _NeF7AutomaticRemoteBackupSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 11),
    _NeF7AutomaticRemoteBackupSrcIp_Type()
)
neF7AutomaticRemoteBackupSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupSrcIp.setStatus("current")
_NeF7AutomaticRemoteBackupTimeStamp_Type = F7FileTimeStamp
_NeF7AutomaticRemoteBackupTimeStamp_Object = MibScalar
neF7AutomaticRemoteBackupTimeStamp = _NeF7AutomaticRemoteBackupTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 12),
    _NeF7AutomaticRemoteBackupTimeStamp_Type()
)
neF7AutomaticRemoteBackupTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupTimeStamp.setStatus("deprecated")
_NeF7AutomaticRemoteBackupCommonIpSrv_Type = SnmpAdminString
_NeF7AutomaticRemoteBackupCommonIpSrv_Object = MibScalar
neF7AutomaticRemoteBackupCommonIpSrv = _NeF7AutomaticRemoteBackupCommonIpSrv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 13),
    _NeF7AutomaticRemoteBackupCommonIpSrv_Type()
)
neF7AutomaticRemoteBackupCommonIpSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupCommonIpSrv.setStatus("current")
_NeF7AutomaticBackupTable_Object = MibTable
neF7AutomaticBackupTable = _NeF7AutomaticBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20)
)
if mibBuilder.loadTexts:
    neF7AutomaticBackupTable.setStatus("current")
_NeF7AutomaticBackupEntry_Object = MibTableRow
neF7AutomaticBackupEntry = _NeF7AutomaticBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1)
)
neF7AutomaticBackupEntry.setIndexNames(
    (0, "ADVA-MIB", "neF7AutomaticBackupIndex"),
)
if mibBuilder.loadTexts:
    neF7AutomaticBackupEntry.setStatus("current")
_NeF7AutomaticBackupIndex_Type = EntityIndex
_NeF7AutomaticBackupIndex_Object = MibTableColumn
neF7AutomaticBackupIndex = _NeF7AutomaticBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 1),
    _NeF7AutomaticBackupIndex_Type()
)
neF7AutomaticBackupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neF7AutomaticBackupIndex.setStatus("current")
_NeF7AutomaticBackupInterval_Type = F7AutoBackupInterval
_NeF7AutomaticBackupInterval_Object = MibTableColumn
neF7AutomaticBackupInterval = _NeF7AutomaticBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 2),
    _NeF7AutomaticBackupInterval_Type()
)
neF7AutomaticBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticBackupInterval.setStatus("current")
_NeF7AutomaticBackupStartDate_Type = FspDate
_NeF7AutomaticBackupStartDate_Object = MibTableColumn
neF7AutomaticBackupStartDate = _NeF7AutomaticBackupStartDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 3),
    _NeF7AutomaticBackupStartDate_Type()
)
neF7AutomaticBackupStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticBackupStartDate.setStatus("current")
_NeF7AutomaticBackupStartTime_Type = FspTime
_NeF7AutomaticBackupStartTime_Object = MibTableColumn
neF7AutomaticBackupStartTime = _NeF7AutomaticBackupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 4),
    _NeF7AutomaticBackupStartTime_Type()
)
neF7AutomaticBackupStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticBackupStartTime.setStatus("current")
_NeF7AutomaticBackupNextDate_Type = FspDate
_NeF7AutomaticBackupNextDate_Object = MibTableColumn
neF7AutomaticBackupNextDate = _NeF7AutomaticBackupNextDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 5),
    _NeF7AutomaticBackupNextDate_Type()
)
neF7AutomaticBackupNextDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neF7AutomaticBackupNextDate.setStatus("current")
_NeF7AutomaticBackupRunState_Type = F7AutoBackupRunState
_NeF7AutomaticBackupRunState_Object = MibTableColumn
neF7AutomaticBackupRunState = _NeF7AutomaticBackupRunState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 6),
    _NeF7AutomaticBackupRunState_Type()
)
neF7AutomaticBackupRunState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticBackupRunState.setStatus("current")
_NeF7AutomaticBackupTimeStamp_Type = F7FileTimeStamp
_NeF7AutomaticBackupTimeStamp_Object = MibTableColumn
neF7AutomaticBackupTimeStamp = _NeF7AutomaticBackupTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 7),
    _NeF7AutomaticBackupTimeStamp_Type()
)
neF7AutomaticBackupTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticBackupTimeStamp.setStatus("current")
_NeAutoBackup_ObjectIdentity = ObjectIdentity
neAutoBackup = _NeAutoBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3)
)


class _NeAutoBackupConfig_Type(Integer32):
    """Custom type neAutoBackupConfig based on Integer32"""
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
          ("autoBackup", 2),
          ("autoBackupAndUpload", 3))
    )


_NeAutoBackupConfig_Type.__name__ = "Integer32"
_NeAutoBackupConfig_Object = MibScalar
neAutoBackupConfig = _NeAutoBackupConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 1),
    _NeAutoBackupConfig_Type()
)
neAutoBackupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoBackupConfig.setStatus("current")
_NeAutoBackupInterval_Type = Unsigned32
_NeAutoBackupInterval_Object = MibScalar
neAutoBackupInterval = _NeAutoBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 2),
    _NeAutoBackupInterval_Type()
)
neAutoBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoBackupInterval.setStatus("current")
if mibBuilder.loadTexts:
    neAutoBackupInterval.setUnits("hours")
_NeAutoBackupNextActionAt_Type = DateAndTime
_NeAutoBackupNextActionAt_Object = MibScalar
neAutoBackupNextActionAt = _NeAutoBackupNextActionAt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 3),
    _NeAutoBackupNextActionAt_Type()
)
neAutoBackupNextActionAt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoBackupNextActionAt.setStatus("current")
_NeAutoBackupServerAddress_Type = IpAddress
_NeAutoBackupServerAddress_Object = MibScalar
neAutoBackupServerAddress = _NeAutoBackupServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 4),
    _NeAutoBackupServerAddress_Type()
)
neAutoBackupServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoBackupServerAddress.setStatus("current")
_NeAutoBackupServerLogin_Type = SnmpAdminString
_NeAutoBackupServerLogin_Object = MibScalar
neAutoBackupServerLogin = _NeAutoBackupServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 5),
    _NeAutoBackupServerLogin_Type()
)
neAutoBackupServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoBackupServerLogin.setStatus("current")
_NeAutoBackupServerPasswd_Type = SnmpAdminString
_NeAutoBackupServerPasswd_Object = MibScalar
neAutoBackupServerPasswd = _NeAutoBackupServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 6),
    _NeAutoBackupServerPasswd_Type()
)
neAutoBackupServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoBackupServerPasswd.setStatus("current")
_NeAutoBackupServerDirectory_Type = SnmpAdminString
_NeAutoBackupServerDirectory_Object = MibScalar
neAutoBackupServerDirectory = _NeAutoBackupServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 7),
    _NeAutoBackupServerDirectory_Type()
)
neAutoBackupServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAutoBackupServerDirectory.setStatus("current")
_TransportStandards_ObjectIdentity = ObjectIdentity
transportStandards = _TransportStandards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4)
)
_Sonet_ObjectIdentity = ObjectIdentity
sonet = _Sonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1)
)
_SonetConfig_ObjectIdentity = ObjectIdentity
sonetConfig = _SonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1)
)
_SonetSectionConfigTable_Object = MibTable
sonetSectionConfigTable = _SonetSectionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonetSectionConfigTable.setStatus("current")
_SonetSectionConfigEntry_Object = MibTableRow
sonetSectionConfigEntry = _SonetSectionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1)
)
sonetSectionConfigEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionConfigEntry.setStatus("current")
_SonetSectionConfigTimingSource_Type = SonetTimingSource
_SonetSectionConfigTimingSource_Object = MibTableColumn
sonetSectionConfigTimingSource = _SonetSectionConfigTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 1),
    _SonetSectionConfigTimingSource_Type()
)
sonetSectionConfigTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTimingSource.setStatus("current")


class _SonetSectionConfigSignalDegradeThreshhold_Type(Unsigned32):
    """Custom type sonetSectionConfigSignalDegradeThreshhold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_SonetSectionConfigSignalDegradeThreshhold_Type.__name__ = "Unsigned32"
_SonetSectionConfigSignalDegradeThreshhold_Object = MibTableColumn
sonetSectionConfigSignalDegradeThreshhold = _SonetSectionConfigSignalDegradeThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 2),
    _SonetSectionConfigSignalDegradeThreshhold_Type()
)
sonetSectionConfigSignalDegradeThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradeThreshhold.setStatus("current")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradeThreshhold.setUnits("%")


class _SonetSectionConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type sonetSectionConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_SonetSectionConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_SonetSectionConfigSignalDegradePeriod_Object = MibTableColumn
sonetSectionConfigSignalDegradePeriod = _SonetSectionConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 3),
    _SonetSectionConfigSignalDegradePeriod_Type()
)
sonetSectionConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradePeriod.setUnits("s")
_SonetSectionConfigTraceForm_Type = SonetTraceForm
_SonetSectionConfigTraceForm_Object = MibTableColumn
sonetSectionConfigTraceForm = _SonetSectionConfigTraceForm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 4),
    _SonetSectionConfigTraceForm_Type()
)
sonetSectionConfigTraceForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTraceForm.setStatus("current")


class _SonetSectionConfigTraceExpected_Type(OctetString):
    """Custom type sonetSectionConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_SonetSectionConfigTraceExpected_Type.__name__ = "OctetString"
_SonetSectionConfigTraceExpected_Object = MibTableColumn
sonetSectionConfigTraceExpected = _SonetSectionConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 5),
    _SonetSectionConfigTraceExpected_Type()
)
sonetSectionConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTraceExpected.setStatus("current")


class _SonetSectionConfigTraceTransmit_Type(OctetString):
    """Custom type sonetSectionConfigTraceTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_SonetSectionConfigTraceTransmit_Type.__name__ = "OctetString"
_SonetSectionConfigTraceTransmit_Object = MibTableColumn
sonetSectionConfigTraceTransmit = _SonetSectionConfigTraceTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 6),
    _SonetSectionConfigTraceTransmit_Type()
)
sonetSectionConfigTraceTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTraceTransmit.setStatus("current")
_SonetSectionConfigTimMode_Type = TimMode
_SonetSectionConfigTimMode_Object = MibTableColumn
sonetSectionConfigTimMode = _SonetSectionConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 7),
    _SonetSectionConfigTimMode_Type()
)
sonetSectionConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTimMode.setStatus("current")
_SonetSectionDataTable_Object = MibTable
sonetSectionDataTable = _SonetSectionDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonetSectionDataTable.setStatus("current")
_SonetSectionDataEntry_Object = MibTableRow
sonetSectionDataEntry = _SonetSectionDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1)
)
sonetSectionDataEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionDataEntry.setStatus("current")


class _SonetSectionDataTraceReceived_Type(OctetString):
    """Custom type sonetSectionDataTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_SonetSectionDataTraceReceived_Type.__name__ = "OctetString"
_SonetSectionDataTraceReceived_Object = MibTableColumn
sonetSectionDataTraceReceived = _SonetSectionDataTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1, 1),
    _SonetSectionDataTraceReceived_Type()
)
sonetSectionDataTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDataTraceReceived.setStatus("current")
_Otn_ObjectIdentity = ObjectIdentity
otn = _Otn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2)
)
_OtuConfig_ObjectIdentity = ObjectIdentity
otuConfig = _OtuConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1)
)
_OtuSectionConfigTable_Object = MibTable
otuSectionConfigTable = _OtuSectionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    otuSectionConfigTable.setStatus("current")
_OtuSectionConfigEntry_Object = MibTableRow
otuSectionConfigEntry = _OtuSectionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1)
)
otuSectionConfigEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    otuSectionConfigEntry.setStatus("current")


class _OtuSectionConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type otuSectionConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_OtuSectionConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OtuSectionConfigSignalDegradeThreshold_Object = MibTableColumn
otuSectionConfigSignalDegradeThreshold = _OtuSectionConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 1),
    _OtuSectionConfigSignalDegradeThreshold_Type()
)
otuSectionConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradeThreshold.setUnits("%")


class _OtuSectionConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type otuSectionConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_OtuSectionConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OtuSectionConfigSignalDegradePeriod_Object = MibTableColumn
otuSectionConfigSignalDegradePeriod = _OtuSectionConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 2),
    _OtuSectionConfigSignalDegradePeriod_Type()
)
otuSectionConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradePeriod.setUnits("s")
_OtuSectionConfigPayload_Type = OtnPayloadType
_OtuSectionConfigPayload_Object = MibTableColumn
otuSectionConfigPayload = _OtuSectionConfigPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 3),
    _OtuSectionConfigPayload_Type()
)
otuSectionConfigPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigPayload.setStatus("current")
_OtuSectionConfigStuffing_Type = EnableState
_OtuSectionConfigStuffing_Object = MibTableColumn
otuSectionConfigStuffing = _OtuSectionConfigStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 4),
    _OtuSectionConfigStuffing_Type()
)
otuSectionConfigStuffing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigStuffing.setStatus("current")


class _OtuSectionConfigTraceExpected_Type(OctetString):
    """Custom type otuSectionConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtuSectionConfigTraceExpected_Type.__name__ = "OctetString"
_OtuSectionConfigTraceExpected_Object = MibTableColumn
otuSectionConfigTraceExpected = _OtuSectionConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 5),
    _OtuSectionConfigTraceExpected_Type()
)
otuSectionConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceExpected.setStatus("current")


class _OtuSectionConfigTraceTransmitSapi_Type(OctetString):
    """Custom type otuSectionConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtuSectionConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OtuSectionConfigTraceTransmitSapi_Object = MibTableColumn
otuSectionConfigTraceTransmitSapi = _OtuSectionConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 6),
    _OtuSectionConfigTraceTransmitSapi_Type()
)
otuSectionConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceTransmitSapi.setStatus("current")


class _OtuSectionConfigTraceTransmitDapi_Type(OctetString):
    """Custom type otuSectionConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtuSectionConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OtuSectionConfigTraceTransmitDapi_Object = MibTableColumn
otuSectionConfigTraceTransmitDapi = _OtuSectionConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 7),
    _OtuSectionConfigTraceTransmitDapi_Type()
)
otuSectionConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceTransmitDapi.setStatus("current")


class _OtuSectionConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type otuSectionConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OtuSectionConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OtuSectionConfigTraceTransmitOpsp_Object = MibTableColumn
otuSectionConfigTraceTransmitOpsp = _OtuSectionConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 8),
    _OtuSectionConfigTraceTransmitOpsp_Type()
)
otuSectionConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceTransmitOpsp.setStatus("current")
_OtuSectionConfigTimMode_Type = TimMode
_OtuSectionConfigTimMode_Object = MibTableColumn
otuSectionConfigTimMode = _OtuSectionConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 9),
    _OtuSectionConfigTimMode_Type()
)
otuSectionConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTimMode.setStatus("current")
_OtuSectionDataTable_Object = MibTable
otuSectionDataTable = _OtuSectionDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    otuSectionDataTable.setStatus("current")
_OtuSectionDataEntry_Object = MibTableRow
otuSectionDataEntry = _OtuSectionDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1)
)
otuSectionDataEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    otuSectionDataEntry.setStatus("current")
_OtuSectionDataResultingTotalBitrate_Type = Unsigned32
_OtuSectionDataResultingTotalBitrate_Object = MibTableColumn
otuSectionDataResultingTotalBitrate = _OtuSectionDataResultingTotalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 1),
    _OtuSectionDataResultingTotalBitrate_Type()
)
otuSectionDataResultingTotalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataResultingTotalBitrate.setStatus("current")
if mibBuilder.loadTexts:
    otuSectionDataResultingTotalBitrate.setUnits("Mbps")


class _OtuSectionDataTraceReceivedSapi_Type(OctetString):
    """Custom type otuSectionDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtuSectionDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OtuSectionDataTraceReceivedSapi_Object = MibTableColumn
otuSectionDataTraceReceivedSapi = _OtuSectionDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 2),
    _OtuSectionDataTraceReceivedSapi_Type()
)
otuSectionDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataTraceReceivedSapi.setStatus("current")


class _OtuSectionDataTraceReceivedDapi_Type(OctetString):
    """Custom type otuSectionDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtuSectionDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OtuSectionDataTraceReceivedDapi_Object = MibTableColumn
otuSectionDataTraceReceivedDapi = _OtuSectionDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 3),
    _OtuSectionDataTraceReceivedDapi_Type()
)
otuSectionDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataTraceReceivedDapi.setStatus("current")


class _OtuSectionDataTraceReceivedOpsp_Type(OctetString):
    """Custom type otuSectionDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OtuSectionDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OtuSectionDataTraceReceivedOpsp_Object = MibTableColumn
otuSectionDataTraceReceivedOpsp = _OtuSectionDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 4),
    _OtuSectionDataTraceReceivedOpsp_Type()
)
otuSectionDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataTraceReceivedOpsp.setStatus("current")
_OduConfig_ObjectIdentity = ObjectIdentity
oduConfig = _OduConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2)
)
_OduSectionConfigTable_Object = MibTable
oduSectionConfigTable = _OduSectionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oduSectionConfigTable.setStatus("current")
_OduSectionConfigEntry_Object = MibTableRow
oduSectionConfigEntry = _OduSectionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1)
)
oduSectionConfigEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduSectionConfigEntry.setStatus("current")


class _OduSectionConfigSignalDegradeThres_Type(Integer32):
    """Custom type oduSectionConfigSignalDegradeThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_OduSectionConfigSignalDegradeThres_Type.__name__ = "Integer32"
_OduSectionConfigSignalDegradeThres_Object = MibTableColumn
oduSectionConfigSignalDegradeThres = _OduSectionConfigSignalDegradeThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 1),
    _OduSectionConfigSignalDegradeThres_Type()
)
oduSectionConfigSignalDegradeThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradeThres.setStatus("current")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradeThres.setUnits("%")


class _OduSectionConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduSectionConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_OduSectionConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduSectionConfigSignalDegradePeriod_Object = MibTableColumn
oduSectionConfigSignalDegradePeriod = _OduSectionConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 2),
    _OduSectionConfigSignalDegradePeriod_Type()
)
oduSectionConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradePeriod.setUnits("s")


class _OduSectionConfigTraceExpected_Type(OctetString):
    """Custom type oduSectionConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduSectionConfigTraceExpected_Type.__name__ = "OctetString"
_OduSectionConfigTraceExpected_Object = MibTableColumn
oduSectionConfigTraceExpected = _OduSectionConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 3),
    _OduSectionConfigTraceExpected_Type()
)
oduSectionConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceExpected.setStatus("current")


class _OduSectionConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduSectionConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduSectionConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduSectionConfigTraceTransmitSapi_Object = MibTableColumn
oduSectionConfigTraceTransmitSapi = _OduSectionConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 4),
    _OduSectionConfigTraceTransmitSapi_Type()
)
oduSectionConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceTransmitSapi.setStatus("current")


class _OduSectionConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduSectionConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduSectionConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduSectionConfigTraceTransmitDapi_Object = MibTableColumn
oduSectionConfigTraceTransmitDapi = _OduSectionConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 5),
    _OduSectionConfigTraceTransmitDapi_Type()
)
oduSectionConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceTransmitDapi.setStatus("current")


class _OduSectionConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduSectionConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduSectionConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduSectionConfigTraceTransmitOpsp_Object = MibTableColumn
oduSectionConfigTraceTransmitOpsp = _OduSectionConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 6),
    _OduSectionConfigTraceTransmitOpsp_Type()
)
oduSectionConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceTransmitOpsp.setStatus("current")
_OduSectionConfigTimMode_Type = TimMode
_OduSectionConfigTimMode_Object = MibTableColumn
oduSectionConfigTimMode = _OduSectionConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 7),
    _OduSectionConfigTimMode_Type()
)
oduSectionConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTimMode.setStatus("current")
_OduSectionDataTable_Object = MibTable
oduSectionDataTable = _OduSectionDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oduSectionDataTable.setStatus("current")
_OduSectionDataEntry_Object = MibTableRow
oduSectionDataEntry = _OduSectionDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1)
)
oduSectionDataEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduSectionDataEntry.setStatus("current")


class _OduSectionDataTraceReceivedSapi_Type(OctetString):
    """Custom type oduSectionDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduSectionDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduSectionDataTraceReceivedSapi_Object = MibTableColumn
oduSectionDataTraceReceivedSapi = _OduSectionDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 1),
    _OduSectionDataTraceReceivedSapi_Type()
)
oduSectionDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduSectionDataTraceReceivedSapi.setStatus("current")


class _OduSectionDataTraceReceivedDapi_Type(OctetString):
    """Custom type oduSectionDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduSectionDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduSectionDataTraceReceivedDapi_Object = MibTableColumn
oduSectionDataTraceReceivedDapi = _OduSectionDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 2),
    _OduSectionDataTraceReceivedDapi_Type()
)
oduSectionDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduSectionDataTraceReceivedDapi.setStatus("current")


class _OduSectionDataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduSectionDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduSectionDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduSectionDataTraceReceivedOpsp_Object = MibTableColumn
oduSectionDataTraceReceivedOpsp = _OduSectionDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 3),
    _OduSectionDataTraceReceivedOpsp_Type()
)
oduSectionDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduSectionDataTraceReceivedOpsp.setStatus("current")
_OduTcmAConfigTable_Object = MibTable
oduTcmAConfigTable = _OduTcmAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    oduTcmAConfigTable.setStatus("current")
_OduTcmAConfigEntry_Object = MibTableRow
oduTcmAConfigEntry = _OduTcmAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1)
)
oduTcmAConfigEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmAConfigEntry.setStatus("current")


class _OduTcmAConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type oduTcmAConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_OduTcmAConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OduTcmAConfigSignalDegradeThreshold_Object = MibTableColumn
oduTcmAConfigSignalDegradeThreshold = _OduTcmAConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 1),
    _OduTcmAConfigSignalDegradeThreshold_Type()
)
oduTcmAConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradeThreshold.setUnits("%")


class _OduTcmAConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduTcmAConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_OduTcmAConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduTcmAConfigSignalDegradePeriod_Object = MibTableColumn
oduTcmAConfigSignalDegradePeriod = _OduTcmAConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 2),
    _OduTcmAConfigSignalDegradePeriod_Type()
)
oduTcmAConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradePeriod.setUnits("s")
_OduTcmAConfigTcmLevel_Type = OtnTcmLevel
_OduTcmAConfigTcmLevel_Object = MibTableColumn
oduTcmAConfigTcmLevel = _OduTcmAConfigTcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 3),
    _OduTcmAConfigTcmLevel_Type()
)
oduTcmAConfigTcmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTcmLevel.setStatus("current")


class _OduTcmAConfigTraceExpected_Type(OctetString):
    """Custom type oduTcmAConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmAConfigTraceExpected_Type.__name__ = "OctetString"
_OduTcmAConfigTraceExpected_Object = MibTableColumn
oduTcmAConfigTraceExpected = _OduTcmAConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 4),
    _OduTcmAConfigTraceExpected_Type()
)
oduTcmAConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceExpected.setStatus("current")


class _OduTcmAConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduTcmAConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmAConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduTcmAConfigTraceTransmitSapi_Object = MibTableColumn
oduTcmAConfigTraceTransmitSapi = _OduTcmAConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 5),
    _OduTcmAConfigTraceTransmitSapi_Type()
)
oduTcmAConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceTransmitSapi.setStatus("current")


class _OduTcmAConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduTcmAConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmAConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduTcmAConfigTraceTransmitDapi_Object = MibTableColumn
oduTcmAConfigTraceTransmitDapi = _OduTcmAConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 6),
    _OduTcmAConfigTraceTransmitDapi_Type()
)
oduTcmAConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceTransmitDapi.setStatus("current")


class _OduTcmAConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduTcmAConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduTcmAConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduTcmAConfigTraceTransmitOpsp_Object = MibTableColumn
oduTcmAConfigTraceTransmitOpsp = _OduTcmAConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 7),
    _OduTcmAConfigTraceTransmitOpsp_Type()
)
oduTcmAConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceTransmitOpsp.setStatus("current")
_OduTcmAConfigTimMode_Type = TimMode
_OduTcmAConfigTimMode_Object = MibTableColumn
oduTcmAConfigTimMode = _OduTcmAConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 8),
    _OduTcmAConfigTimMode_Type()
)
oduTcmAConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTimMode.setStatus("current")
_OduTcmBConfigTable_Object = MibTable
oduTcmBConfigTable = _OduTcmBConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    oduTcmBConfigTable.setStatus("current")
_OduTcmBConfigEntry_Object = MibTableRow
oduTcmBConfigEntry = _OduTcmBConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1)
)
oduTcmBConfigEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmBConfigEntry.setStatus("current")


class _OduTcmBConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type oduTcmBConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_OduTcmBConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OduTcmBConfigSignalDegradeThreshold_Object = MibTableColumn
oduTcmBConfigSignalDegradeThreshold = _OduTcmBConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 1),
    _OduTcmBConfigSignalDegradeThreshold_Type()
)
oduTcmBConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradeThreshold.setUnits("%")


class _OduTcmBConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduTcmBConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_OduTcmBConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduTcmBConfigSignalDegradePeriod_Object = MibTableColumn
oduTcmBConfigSignalDegradePeriod = _OduTcmBConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 2),
    _OduTcmBConfigSignalDegradePeriod_Type()
)
oduTcmBConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradePeriod.setUnits("s")
_OduTcmBConfigTcmLevel_Type = OtnTcmLevel
_OduTcmBConfigTcmLevel_Object = MibTableColumn
oduTcmBConfigTcmLevel = _OduTcmBConfigTcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 3),
    _OduTcmBConfigTcmLevel_Type()
)
oduTcmBConfigTcmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTcmLevel.setStatus("current")


class _OduTcmBConfigTraceExpected_Type(OctetString):
    """Custom type oduTcmBConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmBConfigTraceExpected_Type.__name__ = "OctetString"
_OduTcmBConfigTraceExpected_Object = MibTableColumn
oduTcmBConfigTraceExpected = _OduTcmBConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 4),
    _OduTcmBConfigTraceExpected_Type()
)
oduTcmBConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceExpected.setStatus("current")


class _OduTcmBConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduTcmBConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmBConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduTcmBConfigTraceTransmitSapi_Object = MibTableColumn
oduTcmBConfigTraceTransmitSapi = _OduTcmBConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 5),
    _OduTcmBConfigTraceTransmitSapi_Type()
)
oduTcmBConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceTransmitSapi.setStatus("current")


class _OduTcmBConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduTcmBConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmBConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduTcmBConfigTraceTransmitDapi_Object = MibTableColumn
oduTcmBConfigTraceTransmitDapi = _OduTcmBConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 6),
    _OduTcmBConfigTraceTransmitDapi_Type()
)
oduTcmBConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceTransmitDapi.setStatus("current")


class _OduTcmBConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduTcmBConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduTcmBConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduTcmBConfigTraceTransmitOpsp_Object = MibTableColumn
oduTcmBConfigTraceTransmitOpsp = _OduTcmBConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 7),
    _OduTcmBConfigTraceTransmitOpsp_Type()
)
oduTcmBConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceTransmitOpsp.setStatus("current")
_OduTcmBConfigTimMode_Type = TimMode
_OduTcmBConfigTimMode_Object = MibTableColumn
oduTcmBConfigTimMode = _OduTcmBConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 8),
    _OduTcmBConfigTimMode_Type()
)
oduTcmBConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTimMode.setStatus("current")
_OduTcmCConfigTable_Object = MibTable
oduTcmCConfigTable = _OduTcmCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5)
)
if mibBuilder.loadTexts:
    oduTcmCConfigTable.setStatus("current")
_OduTcmCConfigEntry_Object = MibTableRow
oduTcmCConfigEntry = _OduTcmCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1)
)
oduTcmCConfigEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmCConfigEntry.setStatus("current")


class _OduTcmCConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type oduTcmCConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_OduTcmCConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OduTcmCConfigSignalDegradeThreshold_Object = MibTableColumn
oduTcmCConfigSignalDegradeThreshold = _OduTcmCConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 1),
    _OduTcmCConfigSignalDegradeThreshold_Type()
)
oduTcmCConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradeThreshold.setUnits("%")


class _OduTcmCConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduTcmCConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_OduTcmCConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduTcmCConfigSignalDegradePeriod_Object = MibTableColumn
oduTcmCConfigSignalDegradePeriod = _OduTcmCConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 2),
    _OduTcmCConfigSignalDegradePeriod_Type()
)
oduTcmCConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradePeriod.setUnits("s")
_OduTcmCConfigTcmLevel_Type = OtnTcmLevel
_OduTcmCConfigTcmLevel_Object = MibTableColumn
oduTcmCConfigTcmLevel = _OduTcmCConfigTcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 3),
    _OduTcmCConfigTcmLevel_Type()
)
oduTcmCConfigTcmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTcmLevel.setStatus("current")


class _OduTcmCConfigTraceExpected_Type(OctetString):
    """Custom type oduTcmCConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmCConfigTraceExpected_Type.__name__ = "OctetString"
_OduTcmCConfigTraceExpected_Object = MibTableColumn
oduTcmCConfigTraceExpected = _OduTcmCConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 4),
    _OduTcmCConfigTraceExpected_Type()
)
oduTcmCConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceExpected.setStatus("current")


class _OduTcmCConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduTcmCConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmCConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduTcmCConfigTraceTransmitSapi_Object = MibTableColumn
oduTcmCConfigTraceTransmitSapi = _OduTcmCConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 5),
    _OduTcmCConfigTraceTransmitSapi_Type()
)
oduTcmCConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceTransmitSapi.setStatus("current")


class _OduTcmCConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduTcmCConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmCConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduTcmCConfigTraceTransmitDapi_Object = MibTableColumn
oduTcmCConfigTraceTransmitDapi = _OduTcmCConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 6),
    _OduTcmCConfigTraceTransmitDapi_Type()
)
oduTcmCConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceTransmitDapi.setStatus("current")


class _OduTcmCConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduTcmCConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduTcmCConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduTcmCConfigTraceTransmitOpsp_Object = MibTableColumn
oduTcmCConfigTraceTransmitOpsp = _OduTcmCConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 7),
    _OduTcmCConfigTraceTransmitOpsp_Type()
)
oduTcmCConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceTransmitOpsp.setStatus("current")
_OduTcmCConfigTimMode_Type = TimMode
_OduTcmCConfigTimMode_Object = MibTableColumn
oduTcmCConfigTimMode = _OduTcmCConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 8),
    _OduTcmCConfigTimMode_Type()
)
oduTcmCConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTimMode.setStatus("current")
_OduTcmADataTable_Object = MibTable
oduTcmADataTable = _OduTcmADataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6)
)
if mibBuilder.loadTexts:
    oduTcmADataTable.setStatus("current")
_OduTcmADataEntry_Object = MibTableRow
oduTcmADataEntry = _OduTcmADataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1)
)
oduTcmADataEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmADataEntry.setStatus("current")


class _OduTcmADataTraceReceivedSapi_Type(OctetString):
    """Custom type oduTcmADataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmADataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduTcmADataTraceReceivedSapi_Object = MibTableColumn
oduTcmADataTraceReceivedSapi = _OduTcmADataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 1),
    _OduTcmADataTraceReceivedSapi_Type()
)
oduTcmADataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmADataTraceReceivedSapi.setStatus("current")


class _OduTcmADataTraceReceivedDapi_Type(OctetString):
    """Custom type oduTcmADataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmADataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduTcmADataTraceReceivedDapi_Object = MibTableColumn
oduTcmADataTraceReceivedDapi = _OduTcmADataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 2),
    _OduTcmADataTraceReceivedDapi_Type()
)
oduTcmADataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmADataTraceReceivedDapi.setStatus("current")


class _OduTcmADataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduTcmADataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduTcmADataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduTcmADataTraceReceivedOpsp_Object = MibTableColumn
oduTcmADataTraceReceivedOpsp = _OduTcmADataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 3),
    _OduTcmADataTraceReceivedOpsp_Type()
)
oduTcmADataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmADataTraceReceivedOpsp.setStatus("current")
_OduTcmBDataTable_Object = MibTable
oduTcmBDataTable = _OduTcmBDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7)
)
if mibBuilder.loadTexts:
    oduTcmBDataTable.setStatus("current")
_OduTcmBDataEntry_Object = MibTableRow
oduTcmBDataEntry = _OduTcmBDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1)
)
oduTcmBDataEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmBDataEntry.setStatus("current")


class _OduTcmBDataTraceReceivedSapi_Type(OctetString):
    """Custom type oduTcmBDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmBDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduTcmBDataTraceReceivedSapi_Object = MibTableColumn
oduTcmBDataTraceReceivedSapi = _OduTcmBDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 1),
    _OduTcmBDataTraceReceivedSapi_Type()
)
oduTcmBDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmBDataTraceReceivedSapi.setStatus("current")


class _OduTcmBDataTraceReceivedDapi_Type(OctetString):
    """Custom type oduTcmBDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmBDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduTcmBDataTraceReceivedDapi_Object = MibTableColumn
oduTcmBDataTraceReceivedDapi = _OduTcmBDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 2),
    _OduTcmBDataTraceReceivedDapi_Type()
)
oduTcmBDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmBDataTraceReceivedDapi.setStatus("current")


class _OduTcmBDataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduTcmBDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduTcmBDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduTcmBDataTraceReceivedOpsp_Object = MibTableColumn
oduTcmBDataTraceReceivedOpsp = _OduTcmBDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 3),
    _OduTcmBDataTraceReceivedOpsp_Type()
)
oduTcmBDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmBDataTraceReceivedOpsp.setStatus("current")
_OduTcmCDataTable_Object = MibTable
oduTcmCDataTable = _OduTcmCDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8)
)
if mibBuilder.loadTexts:
    oduTcmCDataTable.setStatus("current")
_OduTcmCDataEntry_Object = MibTableRow
oduTcmCDataEntry = _OduTcmCDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1)
)
oduTcmCDataEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmCDataEntry.setStatus("current")


class _OduTcmCDataTraceReceivedSapi_Type(OctetString):
    """Custom type oduTcmCDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmCDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduTcmCDataTraceReceivedSapi_Object = MibTableColumn
oduTcmCDataTraceReceivedSapi = _OduTcmCDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 1),
    _OduTcmCDataTraceReceivedSapi_Type()
)
oduTcmCDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmCDataTraceReceivedSapi.setStatus("current")


class _OduTcmCDataTraceReceivedDapi_Type(OctetString):
    """Custom type oduTcmCDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OduTcmCDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduTcmCDataTraceReceivedDapi_Object = MibTableColumn
oduTcmCDataTraceReceivedDapi = _OduTcmCDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 2),
    _OduTcmCDataTraceReceivedDapi_Type()
)
oduTcmCDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmCDataTraceReceivedDapi.setStatus("current")


class _OduTcmCDataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduTcmCDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OduTcmCDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduTcmCDataTraceReceivedOpsp_Object = MibTableColumn
oduTcmCDataTraceReceivedOpsp = _OduTcmCDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 3),
    _OduTcmCDataTraceReceivedOpsp_Type()
)
oduTcmCDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmCDataTraceReceivedOpsp.setStatus("current")
_InventoryMib_ObjectIdentity = ObjectIdentity
inventoryMib = _InventoryMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5)
)
_InventoryTable_Object = MibTable
inventoryTable = _InventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    inventoryTable.setStatus("current")
_InventoryEntry_Object = MibTableRow
inventoryEntry = _InventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1)
)
inventoryEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    inventoryEntry.setStatus("current")
_InventoryUnitName_Type = SnmpAdminString
_InventoryUnitName_Object = MibTableColumn
inventoryUnitName = _InventoryUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 1),
    _InventoryUnitName_Type()
)
inventoryUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryUnitName.setStatus("current")
_InventoryFirmwarePackageRev_Type = SnmpAdminString
_InventoryFirmwarePackageRev_Object = MibTableColumn
inventoryFirmwarePackageRev = _InventoryFirmwarePackageRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 2),
    _InventoryFirmwarePackageRev_Type()
)
inventoryFirmwarePackageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryFirmwarePackageRev.setStatus("current")
_InventoryHardwareRev_Type = SnmpAdminString
_InventoryHardwareRev_Object = MibTableColumn
inventoryHardwareRev = _InventoryHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 3),
    _InventoryHardwareRev_Type()
)
inventoryHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryHardwareRev.setStatus("current")
_InventorySoftwareRev_Type = SnmpAdminString
_InventorySoftwareRev_Object = MibTableColumn
inventorySoftwareRev = _InventorySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 4),
    _InventorySoftwareRev_Type()
)
inventorySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySoftwareRev.setStatus("current")
_InventoryFpgaRev_Type = SnmpAdminString
_InventoryFpgaRev_Object = MibTableColumn
inventoryFpgaRev = _InventoryFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 5),
    _InventoryFpgaRev_Type()
)
inventoryFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryFpgaRev.setStatus("current")
_InventorySerialNum_Type = SnmpAdminString
_InventorySerialNum_Object = MibTableColumn
inventorySerialNum = _InventorySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 6),
    _InventorySerialNum_Type()
)
inventorySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySerialNum.setStatus("current")
_InventoryPartnumber_Type = SnmpAdminString
_InventoryPartnumber_Object = MibTableColumn
inventoryPartnumber = _InventoryPartnumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 7),
    _InventoryPartnumber_Type()
)
inventoryPartnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryPartnumber.setStatus("current")
_InventoryCleiCode_Type = SnmpAdminString
_InventoryCleiCode_Object = MibTableColumn
inventoryCleiCode = _InventoryCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 8),
    _InventoryCleiCode_Type()
)
inventoryCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryCleiCode.setStatus("current")
_InventoryVendorId_Type = SnmpAdminString
_InventoryVendorId_Object = MibTableColumn
inventoryVendorId = _InventoryVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 9),
    _InventoryVendorId_Type()
)
inventoryVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryVendorId.setStatus("current")
_InventoryType_Type = EntityType
_InventoryType_Object = MibTableColumn
inventoryType = _InventoryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 10),
    _InventoryType_Type()
)
inventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryType.setStatus("current")
_InventoryUniversalSerialIdent_Type = SnmpAdminString
_InventoryUniversalSerialIdent_Object = MibTableColumn
inventoryUniversalSerialIdent = _InventoryUniversalSerialIdent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 11),
    _InventoryUniversalSerialIdent_Type()
)
inventoryUniversalSerialIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryUniversalSerialIdent.setStatus("current")
_InventoryMacAddress_Type = MacAddress
_InventoryMacAddress_Object = MibTableColumn
inventoryMacAddress = _InventoryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 12),
    _InventoryMacAddress_Type()
)
inventoryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryMacAddress.setStatus("current")
_InventoryGradeInventory_Type = Grade
_InventoryGradeInventory_Object = MibTableColumn
inventoryGradeInventory = _InventoryGradeInventory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 13),
    _InventoryGradeInventory_Type()
)
inventoryGradeInventory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryGradeInventory.setStatus("current")
_InventoryCfSerialNum_Type = SnmpAdminString
_InventoryCfSerialNum_Object = MibTableColumn
inventoryCfSerialNum = _InventoryCfSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 14),
    _InventoryCfSerialNum_Type()
)
inventoryCfSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryCfSerialNum.setStatus("current")
_InventoryCfModel_Type = SnmpAdminString
_InventoryCfModel_Object = MibTableColumn
inventoryCfModel = _InventoryCfModel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 15),
    _InventoryCfModel_Type()
)
inventoryCfModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryCfModel.setStatus("current")
_EntityTable_Object = MibTable
entityTable = _EntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2)
)
if mibBuilder.loadTexts:
    entityTable.setStatus("current")
_EntityEntry_Object = MibTableRow
entityEntry = _EntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1)
)
entityEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    entityEntry.setStatus("current")
_EntityIndex_Type = EntityIndex
_EntityIndex_Object = MibTableColumn
entityIndex = _EntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 1),
    _EntityIndex_Type()
)
entityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    entityIndex.setStatus("current")
_EntityContainedIn_Type = EntityIndex
_EntityContainedIn_Object = MibTableColumn
entityContainedIn = _EntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 2),
    _EntityContainedIn_Type()
)
entityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityContainedIn.setStatus("current")
_EntityClass_Type = EntityClass
_EntityClass_Object = MibTableColumn
entityClass = _EntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 3),
    _EntityClass_Type()
)
entityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityClass.setStatus("current")


class _EntityClassInstanceNumber_Type(Integer32):
    """Custom type entityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_EntityClassInstanceNumber_Type.__name__ = "Integer32"
_EntityClassInstanceNumber_Object = MibTableColumn
entityClassInstanceNumber = _EntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 4),
    _EntityClassInstanceNumber_Type()
)
entityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityClassInstanceNumber.setStatus("current")
_EntityIndexAid_Type = SnmpAdminString
_EntityIndexAid_Object = MibTableColumn
entityIndexAid = _EntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 5),
    _EntityIndexAid_Type()
)
entityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityIndexAid.setStatus("current")
_EntityType_Type = EntityType
_EntityType_Object = MibTableColumn
entityType = _EntityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 6),
    _EntityType_Type()
)
entityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityType.setStatus("current")
_EntityAssignmentState_Type = AssignmentState
_EntityAssignmentState_Object = MibTableColumn
entityAssignmentState = _EntityAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 7),
    _EntityAssignmentState_Type()
)
entityAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityAssignmentState.setStatus("current")
_EntityEquipmentState_Type = EquipmentState
_EntityEquipmentState_Object = MibTableColumn
entityEquipmentState = _EntityEquipmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 8),
    _EntityEquipmentState_Type()
)
entityEquipmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityEquipmentState.setStatus("current")
_ContainsTable_Object = MibTable
containsTable = _ContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3)
)
if mibBuilder.loadTexts:
    containsTable.setStatus("current")
_ContainsEntry_Object = MibTableRow
containsEntry = _ContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1)
)
containsEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
    (0, "ADVA-MIB", "containsIndex"),
)
if mibBuilder.loadTexts:
    containsEntry.setStatus("current")
_ContainsIndex_Type = EntityIndex
_ContainsIndex_Object = MibTableColumn
containsIndex = _ContainsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1, 1),
    _ContainsIndex_Type()
)
containsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containsIndex.setStatus("current")
_ControlPlaneWdmEntityTable_Object = MibTable
controlPlaneWdmEntityTable = _ControlPlaneWdmEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4)
)
if mibBuilder.loadTexts:
    controlPlaneWdmEntityTable.setStatus("current")
_ControlPlaneWdmEntityEntry_Object = MibTableRow
controlPlaneWdmEntityEntry = _ControlPlaneWdmEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1)
)
controlPlaneWdmEntityEntry.setIndexNames(
    (0, "ADVA-MIB", "controlPlaneWdmEntityIndex"),
)
if mibBuilder.loadTexts:
    controlPlaneWdmEntityEntry.setStatus("current")
_ControlPlaneWdmEntityIndex_Type = EntityIndex
_ControlPlaneWdmEntityIndex_Object = MibTableColumn
controlPlaneWdmEntityIndex = _ControlPlaneWdmEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 1),
    _ControlPlaneWdmEntityIndex_Type()
)
controlPlaneWdmEntityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    controlPlaneWdmEntityIndex.setStatus("current")
_ControlPlaneWdmEntityContainedIn_Type = EntityIndex
_ControlPlaneWdmEntityContainedIn_Object = MibTableColumn
controlPlaneWdmEntityContainedIn = _ControlPlaneWdmEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 2),
    _ControlPlaneWdmEntityContainedIn_Type()
)
controlPlaneWdmEntityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneWdmEntityContainedIn.setStatus("current")
_ControlPlaneWdmEntityClass_Type = CpWdmEntityClass
_ControlPlaneWdmEntityClass_Object = MibTableColumn
controlPlaneWdmEntityClass = _ControlPlaneWdmEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 3),
    _ControlPlaneWdmEntityClass_Type()
)
controlPlaneWdmEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneWdmEntityClass.setStatus("current")


class _ControlPlaneWdmEntityClassInstanceNumber_Type(Integer32):
    """Custom type controlPlaneWdmEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_ControlPlaneWdmEntityClassInstanceNumber_Type.__name__ = "Integer32"
_ControlPlaneWdmEntityClassInstanceNumber_Object = MibTableColumn
controlPlaneWdmEntityClassInstanceNumber = _ControlPlaneWdmEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 4),
    _ControlPlaneWdmEntityClassInstanceNumber_Type()
)
controlPlaneWdmEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneWdmEntityClassInstanceNumber.setStatus("current")
_ControlPlaneWdmEntityIndexAid_Type = SnmpAdminString
_ControlPlaneWdmEntityIndexAid_Object = MibTableColumn
controlPlaneWdmEntityIndexAid = _ControlPlaneWdmEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 5),
    _ControlPlaneWdmEntityIndexAid_Type()
)
controlPlaneWdmEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneWdmEntityIndexAid.setStatus("current")
_ControlPlaneWdmEntityAssignmentState_Type = AssignmentState
_ControlPlaneWdmEntityAssignmentState_Object = MibTableColumn
controlPlaneWdmEntityAssignmentState = _ControlPlaneWdmEntityAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 6),
    _ControlPlaneWdmEntityAssignmentState_Type()
)
controlPlaneWdmEntityAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneWdmEntityAssignmentState.setStatus("current")
_ControlPlaneWdmContainsTable_Object = MibTable
controlPlaneWdmContainsTable = _ControlPlaneWdmContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5)
)
if mibBuilder.loadTexts:
    controlPlaneWdmContainsTable.setStatus("current")
_ControlPlaneWdmContainsEntry_Object = MibTableRow
controlPlaneWdmContainsEntry = _ControlPlaneWdmContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5, 1)
)
controlPlaneWdmContainsEntry.setIndexNames(
    (0, "ADVA-MIB", "controlPlaneWdmEntityIndex"),
    (0, "ADVA-MIB", "controlPlaneWdmContainsIndex"),
)
if mibBuilder.loadTexts:
    controlPlaneWdmContainsEntry.setStatus("current")
_ControlPlaneWdmContainsIndex_Type = EntityIndex
_ControlPlaneWdmContainsIndex_Object = MibTableColumn
controlPlaneWdmContainsIndex = _ControlPlaneWdmContainsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5, 1, 1),
    _ControlPlaneWdmContainsIndex_Type()
)
controlPlaneWdmContainsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneWdmContainsIndex.setStatus("current")
_ControlPlaneEthEntityTable_Object = MibTable
controlPlaneEthEntityTable = _ControlPlaneEthEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6)
)
if mibBuilder.loadTexts:
    controlPlaneEthEntityTable.setStatus("current")
_ControlPlaneEthEntityEntry_Object = MibTableRow
controlPlaneEthEntityEntry = _ControlPlaneEthEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1)
)
controlPlaneEthEntityEntry.setIndexNames(
    (0, "ADVA-MIB", "controlPlaneEthEntityIndex"),
)
if mibBuilder.loadTexts:
    controlPlaneEthEntityEntry.setStatus("current")
_ControlPlaneEthEntityIndex_Type = EntityIndex
_ControlPlaneEthEntityIndex_Object = MibTableColumn
controlPlaneEthEntityIndex = _ControlPlaneEthEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 1),
    _ControlPlaneEthEntityIndex_Type()
)
controlPlaneEthEntityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    controlPlaneEthEntityIndex.setStatus("current")
_ControlPlaneEthEntityContainedIn_Type = EntityIndex
_ControlPlaneEthEntityContainedIn_Object = MibTableColumn
controlPlaneEthEntityContainedIn = _ControlPlaneEthEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 2),
    _ControlPlaneEthEntityContainedIn_Type()
)
controlPlaneEthEntityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneEthEntityContainedIn.setStatus("current")
_ControlPlaneEthEntityClass_Type = CpWdmEntityClass
_ControlPlaneEthEntityClass_Object = MibTableColumn
controlPlaneEthEntityClass = _ControlPlaneEthEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 3),
    _ControlPlaneEthEntityClass_Type()
)
controlPlaneEthEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneEthEntityClass.setStatus("current")


class _ControlPlaneEthEntityClassInstanceNumber_Type(Integer32):
    """Custom type controlPlaneEthEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_ControlPlaneEthEntityClassInstanceNumber_Type.__name__ = "Integer32"
_ControlPlaneEthEntityClassInstanceNumber_Object = MibTableColumn
controlPlaneEthEntityClassInstanceNumber = _ControlPlaneEthEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 4),
    _ControlPlaneEthEntityClassInstanceNumber_Type()
)
controlPlaneEthEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneEthEntityClassInstanceNumber.setStatus("current")
_ControlPlaneEthEntityIndexAid_Type = SnmpAdminString
_ControlPlaneEthEntityIndexAid_Object = MibTableColumn
controlPlaneEthEntityIndexAid = _ControlPlaneEthEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 5),
    _ControlPlaneEthEntityIndexAid_Type()
)
controlPlaneEthEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneEthEntityIndexAid.setStatus("current")
_ControlPlaneEthEntityAssignmentState_Type = AssignmentState
_ControlPlaneEthEntityAssignmentState_Object = MibTableColumn
controlPlaneEthEntityAssignmentState = _ControlPlaneEthEntityAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 6),
    _ControlPlaneEthEntityAssignmentState_Type()
)
controlPlaneEthEntityAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneEthEntityAssignmentState.setStatus("current")
_ControlPlaneEthContainsTable_Object = MibTable
controlPlaneEthContainsTable = _ControlPlaneEthContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7)
)
if mibBuilder.loadTexts:
    controlPlaneEthContainsTable.setStatus("current")
_ControlPlaneEthContainsEntry_Object = MibTableRow
controlPlaneEthContainsEntry = _ControlPlaneEthContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7, 1)
)
controlPlaneEthContainsEntry.setIndexNames(
    (0, "ADVA-MIB", "controlPlaneEthEntityIndex"),
    (0, "ADVA-MIB", "controlPlaneEthContainsIndex"),
)
if mibBuilder.loadTexts:
    controlPlaneEthContainsEntry.setStatus("current")
_ControlPlaneEthContainsIndex_Type = EntityIndex
_ControlPlaneEthContainsIndex_Object = MibTableColumn
controlPlaneEthContainsIndex = _ControlPlaneEthContainsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7, 1, 1),
    _ControlPlaneEthContainsIndex_Type()
)
controlPlaneEthContainsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneEthContainsIndex.setStatus("current")
_PtpEntityTable_Object = MibTable
ptpEntityTable = _PtpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    ptpEntityTable.setStatus("current")
_PtpEntityEntry_Object = MibTableRow
ptpEntityEntry = _PtpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1)
)
ptpEntityEntry.setIndexNames(
    (0, "ADVA-MIB", "ptpEntityIndex"),
)
if mibBuilder.loadTexts:
    ptpEntityEntry.setStatus("current")
_PtpEntityIndex_Type = EntityIndex
_PtpEntityIndex_Object = MibTableColumn
ptpEntityIndex = _PtpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 1),
    _PtpEntityIndex_Type()
)
ptpEntityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ptpEntityIndex.setStatus("current")
_PtpEntityContainedIn_Type = EntityIndex
_PtpEntityContainedIn_Object = MibTableColumn
ptpEntityContainedIn = _PtpEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 2),
    _PtpEntityContainedIn_Type()
)
ptpEntityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityContainedIn.setStatus("current")
_PtpEntityClass_Type = EntityClass
_PtpEntityClass_Object = MibTableColumn
ptpEntityClass = _PtpEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 3),
    _PtpEntityClass_Type()
)
ptpEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityClass.setStatus("current")


class _PtpEntityClassInstanceNumber_Type(Integer32):
    """Custom type ptpEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_PtpEntityClassInstanceNumber_Type.__name__ = "Integer32"
_PtpEntityClassInstanceNumber_Object = MibTableColumn
ptpEntityClassInstanceNumber = _PtpEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 4),
    _PtpEntityClassInstanceNumber_Type()
)
ptpEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityClassInstanceNumber.setStatus("current")
_PtpEntityIndexAid_Type = SnmpAdminString
_PtpEntityIndexAid_Object = MibTableColumn
ptpEntityIndexAid = _PtpEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 5),
    _PtpEntityIndexAid_Type()
)
ptpEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityIndexAid.setStatus("current")
_PtpEntityType_Type = EntityType
_PtpEntityType_Object = MibTableColumn
ptpEntityType = _PtpEntityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 6),
    _PtpEntityType_Type()
)
ptpEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityType.setStatus("current")
_PtpEntityAssignmentState_Type = AssignmentState
_PtpEntityAssignmentState_Object = MibTableColumn
ptpEntityAssignmentState = _PtpEntityAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 7),
    _PtpEntityAssignmentState_Type()
)
ptpEntityAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityAssignmentState.setStatus("current")
_PtpEntityEquipmentState_Type = EquipmentState
_PtpEntityEquipmentState_Object = MibTableColumn
ptpEntityEquipmentState = _PtpEntityEquipmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 8),
    _PtpEntityEquipmentState_Type()
)
ptpEntityEquipmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityEquipmentState.setStatus("current")
_PtpEntityReferencedTo_Type = EntityIndex
_PtpEntityReferencedTo_Object = MibTableColumn
ptpEntityReferencedTo = _PtpEntityReferencedTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 9),
    _PtpEntityReferencedTo_Type()
)
ptpEntityReferencedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpEntityReferencedTo.setStatus("current")
_VtpEntityTable_Object = MibTable
vtpEntityTable = _VtpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11)
)
if mibBuilder.loadTexts:
    vtpEntityTable.setStatus("current")
_VtpEntityEntry_Object = MibTableRow
vtpEntityEntry = _VtpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1)
)
vtpEntityEntry.setIndexNames(
    (0, "ADVA-MIB", "vtpEntityIndex"),
)
if mibBuilder.loadTexts:
    vtpEntityEntry.setStatus("current")
_VtpEntityIndex_Type = EntityIndex
_VtpEntityIndex_Object = MibTableColumn
vtpEntityIndex = _VtpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 1),
    _VtpEntityIndex_Type()
)
vtpEntityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vtpEntityIndex.setStatus("current")
_VtpEntityContainedIn_Type = EntityIndex
_VtpEntityContainedIn_Object = MibTableColumn
vtpEntityContainedIn = _VtpEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 2),
    _VtpEntityContainedIn_Type()
)
vtpEntityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityContainedIn.setStatus("current")
_VtpEntityClass_Type = EntityClass
_VtpEntityClass_Object = MibTableColumn
vtpEntityClass = _VtpEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 3),
    _VtpEntityClass_Type()
)
vtpEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityClass.setStatus("current")


class _VtpEntityClassInstanceNumber_Type(Integer32):
    """Custom type vtpEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_VtpEntityClassInstanceNumber_Type.__name__ = "Integer32"
_VtpEntityClassInstanceNumber_Object = MibTableColumn
vtpEntityClassInstanceNumber = _VtpEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 4),
    _VtpEntityClassInstanceNumber_Type()
)
vtpEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityClassInstanceNumber.setStatus("current")
_VtpEntityIndexAid_Type = SnmpAdminString
_VtpEntityIndexAid_Object = MibTableColumn
vtpEntityIndexAid = _VtpEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 5),
    _VtpEntityIndexAid_Type()
)
vtpEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityIndexAid.setStatus("current")
_VtpEntityType_Type = EntityType
_VtpEntityType_Object = MibTableColumn
vtpEntityType = _VtpEntityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 6),
    _VtpEntityType_Type()
)
vtpEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityType.setStatus("current")
_VtpEntityAssignmentState_Type = AssignmentState
_VtpEntityAssignmentState_Object = MibTableColumn
vtpEntityAssignmentState = _VtpEntityAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 7),
    _VtpEntityAssignmentState_Type()
)
vtpEntityAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityAssignmentState.setStatus("current")
_VtpEntityEquipmentState_Type = EquipmentState
_VtpEntityEquipmentState_Object = MibTableColumn
vtpEntityEquipmentState = _VtpEntityEquipmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 8),
    _VtpEntityEquipmentState_Type()
)
vtpEntityEquipmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityEquipmentState.setStatus("current")
_VtpEntityReferencedTo_Type = EntityIndex
_VtpEntityReferencedTo_Object = MibTableColumn
vtpEntityReferencedTo = _VtpEntityReferencedTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 9),
    _VtpEntityReferencedTo_Type()
)
vtpEntityReferencedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpEntityReferencedTo.setStatus("current")
_ControlPlaneOtnEntityTable_Object = MibTable
controlPlaneOtnEntityTable = _ControlPlaneOtnEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12)
)
if mibBuilder.loadTexts:
    controlPlaneOtnEntityTable.setStatus("current")
_ControlPlaneOtnEntityEntry_Object = MibTableRow
controlPlaneOtnEntityEntry = _ControlPlaneOtnEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1)
)
controlPlaneOtnEntityEntry.setIndexNames(
    (0, "ADVA-MIB", "controlPlaneOtnEntityIndex"),
)
if mibBuilder.loadTexts:
    controlPlaneOtnEntityEntry.setStatus("current")
_ControlPlaneOtnEntityIndex_Type = EntityIndex
_ControlPlaneOtnEntityIndex_Object = MibTableColumn
controlPlaneOtnEntityIndex = _ControlPlaneOtnEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 1),
    _ControlPlaneOtnEntityIndex_Type()
)
controlPlaneOtnEntityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    controlPlaneOtnEntityIndex.setStatus("current")
_ControlPlaneOtnEntityContainedIn_Type = EntityIndex
_ControlPlaneOtnEntityContainedIn_Object = MibTableColumn
controlPlaneOtnEntityContainedIn = _ControlPlaneOtnEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 2),
    _ControlPlaneOtnEntityContainedIn_Type()
)
controlPlaneOtnEntityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneOtnEntityContainedIn.setStatus("current")
_ControlPlaneOtnEntityClass_Type = CpWdmEntityClass
_ControlPlaneOtnEntityClass_Object = MibTableColumn
controlPlaneOtnEntityClass = _ControlPlaneOtnEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 3),
    _ControlPlaneOtnEntityClass_Type()
)
controlPlaneOtnEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneOtnEntityClass.setStatus("current")


class _ControlPlaneOtnEntityClassInstanceNumber_Type(Integer32):
    """Custom type controlPlaneOtnEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_ControlPlaneOtnEntityClassInstanceNumber_Type.__name__ = "Integer32"
_ControlPlaneOtnEntityClassInstanceNumber_Object = MibTableColumn
controlPlaneOtnEntityClassInstanceNumber = _ControlPlaneOtnEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 4),
    _ControlPlaneOtnEntityClassInstanceNumber_Type()
)
controlPlaneOtnEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneOtnEntityClassInstanceNumber.setStatus("current")
_ControlPlaneOtnEntityIndexAid_Type = SnmpAdminString
_ControlPlaneOtnEntityIndexAid_Object = MibTableColumn
controlPlaneOtnEntityIndexAid = _ControlPlaneOtnEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 5),
    _ControlPlaneOtnEntityIndexAid_Type()
)
controlPlaneOtnEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneOtnEntityIndexAid.setStatus("current")
_ControlPlaneOtnEntityAssignmentState_Type = AssignmentState
_ControlPlaneOtnEntityAssignmentState_Object = MibTableColumn
controlPlaneOtnEntityAssignmentState = _ControlPlaneOtnEntityAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 6),
    _ControlPlaneOtnEntityAssignmentState_Type()
)
controlPlaneOtnEntityAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneOtnEntityAssignmentState.setStatus("current")
_ControlPlaneOtnContainsTable_Object = MibTable
controlPlaneOtnContainsTable = _ControlPlaneOtnContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13)
)
if mibBuilder.loadTexts:
    controlPlaneOtnContainsTable.setStatus("current")
_ControlPlaneOtnContainsEntry_Object = MibTableRow
controlPlaneOtnContainsEntry = _ControlPlaneOtnContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13, 1)
)
controlPlaneOtnContainsEntry.setIndexNames(
    (0, "ADVA-MIB", "controlPlaneOtnEntityIndex"),
    (0, "ADVA-MIB", "controlPlaneOtnContainsIndex"),
)
if mibBuilder.loadTexts:
    controlPlaneOtnContainsEntry.setStatus("current")
_ControlPlaneOtnContainsIndex_Type = EntityIndex
_ControlPlaneOtnContainsIndex_Object = MibTableColumn
controlPlaneOtnContainsIndex = _ControlPlaneOtnContainsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13, 1, 1),
    _ControlPlaneOtnContainsIndex_Type()
)
controlPlaneOtnContainsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPlaneOtnContainsIndex.setStatus("current")
_UpdateBackupRestoreMib_ObjectIdentity = ObjectIdentity
updateBackupRestoreMib = _UpdateBackupRestoreMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6)
)
_SwAdmin_ObjectIdentity = ObjectIdentity
swAdmin = _SwAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1)
)
_SwDbFileTable_Object = MibTable
swDbFileTable = _SwDbFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    swDbFileTable.setStatus("current")
_SwDbFileEntry_Object = MibTableRow
swDbFileEntry = _SwDbFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1)
)
swDbFileEntry.setIndexNames(
    (0, "ADVA-MIB", "swDbFileIndex"),
)
if mibBuilder.loadTexts:
    swDbFileEntry.setStatus("current")
_SwDbFileIndex_Type = EntityIndex
_SwDbFileIndex_Object = MibTableColumn
swDbFileIndex = _SwDbFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 1),
    _SwDbFileIndex_Type()
)
swDbFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDbFileIndex.setStatus("current")
_SwDbFileArea_Type = FileArea
_SwDbFileArea_Object = MibTableColumn
swDbFileArea = _SwDbFileArea_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 2),
    _SwDbFileArea_Type()
)
swDbFileArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileArea.setStatus("current")
_SwDbFileType_Type = FileType
_SwDbFileType_Object = MibTableColumn
swDbFileType = _SwDbFileType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 3),
    _SwDbFileType_Type()
)
swDbFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileType.setStatus("current")
_SwDbFileSize_Type = Unsigned32
_SwDbFileSize_Object = MibTableColumn
swDbFileSize = _SwDbFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 4),
    _SwDbFileSize_Type()
)
swDbFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileSize.setStatus("current")
if mibBuilder.loadTexts:
    swDbFileSize.setUnits("Byte")
_SwDbFileCreationTime_Type = DateAndTime
_SwDbFileCreationTime_Object = MibTableColumn
swDbFileCreationTime = _SwDbFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 5),
    _SwDbFileCreationTime_Type()
)
swDbFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileCreationTime.setStatus("current")
_SwDbFileVersion_Type = SnmpAdminString
_SwDbFileVersion_Object = MibTableColumn
swDbFileVersion = _SwDbFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 6),
    _SwDbFileVersion_Type()
)
swDbFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileVersion.setStatus("current")
_SwDbFileGrade_Type = Grade
_SwDbFileGrade_Object = MibTableColumn
swDbFileGrade = _SwDbFileGrade_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 7),
    _SwDbFileGrade_Type()
)
swDbFileGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileGrade.setStatus("current")
_SwDbFileComment_Type = SnmpAdminString
_SwDbFileComment_Object = MibTableColumn
swDbFileComment = _SwDbFileComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 8),
    _SwDbFileComment_Type()
)
swDbFileComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDbFileComment.setStatus("current")
_SwDbFileFileName_Type = SnmpAdminString
_SwDbFileFileName_Object = MibTableColumn
swDbFileFileName = _SwDbFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 9),
    _SwDbFileFileName_Type()
)
swDbFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileFileName.setStatus("current")
_SwDbFileRowStatus_Type = RowStatus
_SwDbFileRowStatus_Object = MibTableColumn
swDbFileRowStatus = _SwDbFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 10),
    _SwDbFileRowStatus_Type()
)
swDbFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDbFileRowStatus.setStatus("current")
_SwDbFilePgmType_Type = PgmType
_SwDbFilePgmType_Object = MibTableColumn
swDbFilePgmType = _SwDbFilePgmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 11),
    _SwDbFilePgmType_Type()
)
swDbFilePgmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFilePgmType.setStatus("current")
_FwDataTable_Object = MibTable
fwDataTable = _FwDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    fwDataTable.setStatus("current")
_FwDataEntry_Object = MibTableRow
fwDataEntry = _FwDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1)
)
fwDataEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    fwDataEntry.setStatus("current")
_FwDataNewVersion_Type = SnmpAdminString
_FwDataNewVersion_Object = MibTableColumn
fwDataNewVersion = _FwDataNewVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 1),
    _FwDataNewVersion_Type()
)
fwDataNewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataNewVersion.setStatus("current")
_FwDataStandbyVersion_Type = SnmpAdminString
_FwDataStandbyVersion_Object = MibTableColumn
fwDataStandbyVersion = _FwDataStandbyVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 2),
    _FwDataStandbyVersion_Type()
)
fwDataStandbyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataStandbyVersion.setStatus("current")
_FwDataServiceImpairment_Type = ServiceAffecting
_FwDataServiceImpairment_Object = MibTableColumn
fwDataServiceImpairment = _FwDataServiceImpairment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 3),
    _FwDataServiceImpairment_Type()
)
fwDataServiceImpairment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataServiceImpairment.setStatus("current")
_FwDataBootStatus_Type = BootState
_FwDataBootStatus_Object = MibTableColumn
fwDataBootStatus = _FwDataBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 4),
    _FwDataBootStatus_Type()
)
fwDataBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataBootStatus.setStatus("current")
_FwDataFirmwarePackageRev_Type = SnmpAdminString
_FwDataFirmwarePackageRev_Object = MibTableColumn
fwDataFirmwarePackageRev = _FwDataFirmwarePackageRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 5),
    _FwDataFirmwarePackageRev_Type()
)
fwDataFirmwarePackageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataFirmwarePackageRev.setStatus("current")
_FwDataStandbyServiceImpairment_Type = StandbyServiceAffecting
_FwDataStandbyServiceImpairment_Object = MibTableColumn
fwDataStandbyServiceImpairment = _FwDataStandbyServiceImpairment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 6),
    _FwDataStandbyServiceImpairment_Type()
)
fwDataStandbyServiceImpairment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataStandbyServiceImpairment.setStatus("current")
_FwDataFirmwareAvailable_Type = NoYesNA
_FwDataFirmwareAvailable_Object = MibTableColumn
fwDataFirmwareAvailable = _FwDataFirmwareAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 7),
    _FwDataFirmwareAvailable_Type()
)
fwDataFirmwareAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataFirmwareAvailable.setStatus("current")
_FwDataFirmwareApproved_Type = NoYesNA
_FwDataFirmwareApproved_Object = MibTableColumn
fwDataFirmwareApproved = _FwDataFirmwareApproved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 8),
    _FwDataFirmwareApproved_Type()
)
fwDataFirmwareApproved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataFirmwareApproved.setStatus("current")
_FwDataFirmwarePackageRevBackup_Type = SnmpAdminString
_FwDataFirmwarePackageRevBackup_Object = MibTableColumn
fwDataFirmwarePackageRevBackup = _FwDataFirmwarePackageRevBackup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 9),
    _FwDataFirmwarePackageRevBackup_Type()
)
fwDataFirmwarePackageRevBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataFirmwarePackageRevBackup.setStatus("current")
_FwDataReadyForActivation_Type = YesNoNA
_FwDataReadyForActivation_Object = MibTableColumn
fwDataReadyForActivation = _FwDataReadyForActivation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 10),
    _FwDataReadyForActivation_Type()
)
fwDataReadyForActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataReadyForActivation.setStatus("current")
_FwDataActivationReadyOnStandby_Type = YesNoNA
_FwDataActivationReadyOnStandby_Object = MibTableColumn
fwDataActivationReadyOnStandby = _FwDataActivationReadyOnStandby_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 11),
    _FwDataActivationReadyOnStandby_Type()
)
fwDataActivationReadyOnStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataActivationReadyOnStandby.setStatus("current")
_FwDataProtectionPart_Type = FspR7YesNo
_FwDataProtectionPart_Object = MibTableColumn
fwDataProtectionPart = _FwDataProtectionPart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 12),
    _FwDataProtectionPart_Type()
)
fwDataProtectionPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataProtectionPart.setStatus("current")
_FwDataForm_Type = ModuleForm
_FwDataForm_Object = MibTableColumn
fwDataForm = _FwDataForm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 13),
    _FwDataForm_Type()
)
fwDataForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataForm.setStatus("current")
_FwDataStandbyFirmwareAvailable_Type = NoYesNA
_FwDataStandbyFirmwareAvailable_Object = MibTableColumn
fwDataStandbyFirmwareAvailable = _FwDataStandbyFirmwareAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 14),
    _FwDataStandbyFirmwareAvailable_Type()
)
fwDataStandbyFirmwareAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataStandbyFirmwareAvailable.setStatus("current")
_ColdRestartCapTable_Object = MibTable
coldRestartCapTable = _ColdRestartCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3)
)
if mibBuilder.loadTexts:
    coldRestartCapTable.setStatus("current")
_ColdRestartCapEntry_Object = MibTableRow
coldRestartCapEntry = _ColdRestartCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3, 1)
)
coldRestartCapEntry.setIndexNames(
    (0, "ADVA-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    coldRestartCapEntry.setStatus("current")
_ColdRestartCapServiceAffectingCap_Type = ServiceAffectingCaps
_ColdRestartCapServiceAffectingCap_Object = MibTableColumn
coldRestartCapServiceAffectingCap = _ColdRestartCapServiceAffectingCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3, 1, 1),
    _ColdRestartCapServiceAffectingCap_Type()
)
coldRestartCapServiceAffectingCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coldRestartCapServiceAffectingCap.setStatus("current")
_EqpFwUpgradeRequest_Type = CommandEqpt
_EqpFwUpgradeRequest_Object = MibScalar
eqpFwUpgradeRequest = _EqpFwUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 10),
    _EqpFwUpgradeRequest_Type()
)
eqpFwUpgradeRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwUpgradeRequest.setStatus("current")
_EqpFwServiceImpairment_Type = ServiceAffecting
_EqpFwServiceImpairment_Object = MibScalar
eqpFwServiceImpairment = _EqpFwServiceImpairment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 11),
    _EqpFwServiceImpairment_Type()
)
eqpFwServiceImpairment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwServiceImpairment.setStatus("current")
_EqpFwNextEqpForUpdate_Type = EntityIndex
_EqpFwNextEqpForUpdate_Object = MibScalar
eqpFwNextEqpForUpdate = _EqpFwNextEqpForUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 12),
    _EqpFwNextEqpForUpdate_Type()
)
eqpFwNextEqpForUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwNextEqpForUpdate.setStatus("current")
_EqpFwEqpType_Type = FspR7EquipmentType
_EqpFwEqpType_Object = MibScalar
eqpFwEqpType = _EqpFwEqpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 13),
    _EqpFwEqpType_Type()
)
eqpFwEqpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwEqpType.setStatus("current")
_EqpFwNcuServerBusy_Type = FspR7FalseTrue
_EqpFwNcuServerBusy_Object = MibScalar
eqpFwNcuServerBusy = _EqpFwNcuServerBusy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 14),
    _EqpFwNcuServerBusy_Type()
)
eqpFwNcuServerBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqpFwNcuServerBusy.setStatus("current")
_EqpFwEqpServerBusy_Type = FspR7FalseTrue
_EqpFwEqpServerBusy_Object = MibScalar
eqpFwEqpServerBusy = _EqpFwEqpServerBusy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 15),
    _EqpFwEqpServerBusy_Type()
)
eqpFwEqpServerBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqpFwEqpServerBusy.setStatus("current")
_UpdateEqpt_Type = Unsigned32
_UpdateEqpt_Object = MibScalar
updateEqpt = _UpdateEqpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 16),
    _UpdateEqpt_Type()
)
updateEqpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateEqpt.setStatus("current")
_InstalledEqpt_Type = Unsigned32
_InstalledEqpt_Object = MibScalar
installedEqpt = _InstalledEqpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 17),
    _InstalledEqpt_Type()
)
installedEqpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedEqpt.setStatus("current")
_SelectedFile_Type = SnmpAdminString
_SelectedFile_Object = MibScalar
selectedFile = _SelectedFile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 18),
    _SelectedFile_Type()
)
selectedFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectedFile.setStatus("current")
_NcuActivationDate_Type = FspR7Date
_NcuActivationDate_Object = MibScalar
ncuActivationDate = _NcuActivationDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 19),
    _NcuActivationDate_Type()
)
ncuActivationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncuActivationDate.setStatus("current")
_NcuActivationTime_Type = FspR7Time
_NcuActivationTime_Object = MibScalar
ncuActivationTime = _NcuActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 20),
    _NcuActivationTime_Type()
)
ncuActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncuActivationTime.setStatus("current")
_NcuScheduledActivation_Type = NcuAutoActivation
_NcuScheduledActivation_Object = MibScalar
ncuScheduledActivation = _NcuScheduledActivation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 21),
    _NcuScheduledActivation_Type()
)
ncuScheduledActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncuScheduledActivation.setStatus("current")
_NcuScheduledDbRestore_Type = RestoreActivation
_NcuScheduledDbRestore_Object = MibScalar
ncuScheduledDbRestore = _NcuScheduledDbRestore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 22),
    _NcuScheduledDbRestore_Type()
)
ncuScheduledDbRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncuScheduledDbRestore.setStatus("current")
_EncryptionFwpFile_Type = SnmpAdminString
_EncryptionFwpFile_Object = MibScalar
encryptionFwpFile = _EncryptionFwpFile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 23),
    _EncryptionFwpFile_Type()
)
encryptionFwpFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionFwpFile.setStatus("current")


class _ClearRdiskRequest_Type(Integer32):
    """Custom type clearRdiskRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("active", 1),
          ("inactive", 2))
    )


_ClearRdiskRequest_Type.__name__ = "Integer32"
_ClearRdiskRequest_Object = MibScalar
clearRdiskRequest = _ClearRdiskRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 24),
    _ClearRdiskRequest_Type()
)
clearRdiskRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearRdiskRequest.setStatus("current")
_NcuActivationDateUtc_Type = FspR7Date
_NcuActivationDateUtc_Object = MibScalar
ncuActivationDateUtc = _NcuActivationDateUtc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 25),
    _NcuActivationDateUtc_Type()
)
ncuActivationDateUtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncuActivationDateUtc.setStatus("current")
_NcuActivationTimeUtc_Type = FspR7Time
_NcuActivationTimeUtc_Object = MibScalar
ncuActivationTimeUtc = _NcuActivationTimeUtc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 26),
    _NcuActivationTimeUtc_Type()
)
ncuActivationTimeUtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncuActivationTimeUtc.setStatus("current")
_NeBackupEncryption_Type = EnableState
_NeBackupEncryption_Object = MibScalar
neBackupEncryption = _NeBackupEncryption_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 38),
    _NeBackupEncryption_Type()
)
neBackupEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neBackupEncryption.setStatus("current")
_NeBackupPassword_Type = SnmpAdminString
_NeBackupPassword_Object = MibScalar
neBackupPassword = _NeBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 39),
    _NeBackupPassword_Type()
)
neBackupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neBackupPassword.setStatus("current")
_NeF7AutomaticRemoteBackupEncryption_Type = EnableState
_NeF7AutomaticRemoteBackupEncryption_Object = MibScalar
neF7AutomaticRemoteBackupEncryption = _NeF7AutomaticRemoteBackupEncryption_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 40),
    _NeF7AutomaticRemoteBackupEncryption_Type()
)
neF7AutomaticRemoteBackupEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupEncryption.setStatus("current")
_NeF7AutomaticRemoteBackupPassword_Type = SnmpAdminString
_NeF7AutomaticRemoteBackupPassword_Object = MibScalar
neF7AutomaticRemoteBackupPassword = _NeF7AutomaticRemoteBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 41),
    _NeF7AutomaticRemoteBackupPassword_Type()
)
neF7AutomaticRemoteBackupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupPassword.setStatus("current")
_NeBackupUsers_Type = FspR7UsersDb
_NeBackupUsers_Object = MibScalar
neBackupUsers = _NeBackupUsers_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 42),
    _NeBackupUsers_Type()
)
neBackupUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neBackupUsers.setStatus("current")
_NeInitialConnectionMode_Type = FspR7EnableDisable
_NeInitialConnectionMode_Object = MibScalar
neInitialConnectionMode = _NeInitialConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 43),
    _NeInitialConnectionMode_Type()
)
neInitialConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neInitialConnectionMode.setStatus("current")
_NeF7AutomaticRemoteBackupUsers_Type = FspR7UsersDb
_NeF7AutomaticRemoteBackupUsers_Object = MibScalar
neF7AutomaticRemoteBackupUsers = _NeF7AutomaticRemoteBackupUsers_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 44),
    _NeF7AutomaticRemoteBackupUsers_Type()
)
neF7AutomaticRemoteBackupUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neF7AutomaticRemoteBackupUsers.setStatus("current")
_DbAdmin_ObjectIdentity = ObjectIdentity
dbAdmin = _DbAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2)
)
_NeRestoreConfig_Type = RestoreActivation
_NeRestoreConfig_Object = MibScalar
neRestoreConfig = _NeRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 1),
    _NeRestoreConfig_Type()
)
neRestoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neRestoreConfig.setStatus("current")
_SwDbDataTable_Object = MibTable
swDbDataTable = _SwDbDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2)
)
if mibBuilder.loadTexts:
    swDbDataTable.setStatus("current")
_SwDbDataEntry_Object = MibTableRow
swDbDataEntry = _SwDbDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1)
)
swDbDataEntry.setIndexNames(
    (0, "ADVA-MIB", "swDbDataIndex"),
)
if mibBuilder.loadTexts:
    swDbDataEntry.setStatus("current")
_SwDbDataIndex_Type = EntityIndex
_SwDbDataIndex_Object = MibTableColumn
swDbDataIndex = _SwDbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 1),
    _SwDbDataIndex_Type()
)
swDbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDbDataIndex.setStatus("current")
_SwDbDataArea_Type = FileArea
_SwDbDataArea_Object = MibTableColumn
swDbDataArea = _SwDbDataArea_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 2),
    _SwDbDataArea_Type()
)
swDbDataArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataArea.setStatus("current")
_SwDbDataProgramVersion_Type = SnmpAdminString
_SwDbDataProgramVersion_Object = MibTableColumn
swDbDataProgramVersion = _SwDbDataProgramVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 3),
    _SwDbDataProgramVersion_Type()
)
swDbDataProgramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataProgramVersion.setStatus("current")
_SwDbDataDatabaseVersion_Type = SnmpAdminString
_SwDbDataDatabaseVersion_Object = MibTableColumn
swDbDataDatabaseVersion = _SwDbDataDatabaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 4),
    _SwDbDataDatabaseVersion_Type()
)
swDbDataDatabaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataDatabaseVersion.setStatus("current")
_SwDbDataActivationTime_Type = DateAndTime
_SwDbDataActivationTime_Object = MibTableColumn
swDbDataActivationTime = _SwDbDataActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 5),
    _SwDbDataActivationTime_Type()
)
swDbDataActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataActivationTime.setStatus("current")
_SwDbDataRestoreConfig_Type = RestoreActivation
_SwDbDataRestoreConfig_Object = MibTableColumn
swDbDataRestoreConfig = _SwDbDataRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 6),
    _SwDbDataRestoreConfig_Type()
)
swDbDataRestoreConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataRestoreConfig.setStatus("current")
_SwDbDataFirmwareSetVersion_Type = SnmpAdminString
_SwDbDataFirmwareSetVersion_Object = MibTableColumn
swDbDataFirmwareSetVersion = _SwDbDataFirmwareSetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 7),
    _SwDbDataFirmwareSetVersion_Type()
)
swDbDataFirmwareSetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataFirmwareSetVersion.setStatus("current")
_SwDbDataNcuSoftwareVersion_Type = SnmpAdminString
_SwDbDataNcuSoftwareVersion_Object = MibTableColumn
swDbDataNcuSoftwareVersion = _SwDbDataNcuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 8),
    _SwDbDataNcuSoftwareVersion_Type()
)
swDbDataNcuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNcuSoftwareVersion.setStatus("current")
_SwDbDataStandbyPartitionStatus_Type = PartitionStatus
_SwDbDataStandbyPartitionStatus_Object = MibTableColumn
swDbDataStandbyPartitionStatus = _SwDbDataStandbyPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 9),
    _SwDbDataStandbyPartitionStatus_Type()
)
swDbDataStandbyPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataStandbyPartitionStatus.setStatus("current")
_SwDbDataNumEqpt_Type = Unsigned32
_SwDbDataNumEqpt_Object = MibTableColumn
swDbDataNumEqpt = _SwDbDataNumEqpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 10),
    _SwDbDataNumEqpt_Type()
)
swDbDataNumEqpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNumEqpt.setStatus("current")
_SwDbDataNumLegacyEqpt_Type = Unsigned32
_SwDbDataNumLegacyEqpt_Object = MibTableColumn
swDbDataNumLegacyEqpt = _SwDbDataNumLegacyEqpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 11),
    _SwDbDataNumLegacyEqpt_Type()
)
swDbDataNumLegacyEqpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNumLegacyEqpt.setStatus("current")
_SwDbDataNumNativeSaUpdate_Type = Unsigned32
_SwDbDataNumNativeSaUpdate_Object = MibTableColumn
swDbDataNumNativeSaUpdate = _SwDbDataNumNativeSaUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 12),
    _SwDbDataNumNativeSaUpdate_Type()
)
swDbDataNumNativeSaUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNumNativeSaUpdate.setStatus("current")
_SwDbDataNumNativeNsaUpdate_Type = Unsigned32
_SwDbDataNumNativeNsaUpdate_Object = MibTableColumn
swDbDataNumNativeNsaUpdate = _SwDbDataNumNativeNsaUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 13),
    _SwDbDataNumNativeNsaUpdate_Type()
)
swDbDataNumNativeNsaUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNumNativeNsaUpdate.setStatus("current")
_SwDbDataNumLegacyUpdate_Type = Unsigned32
_SwDbDataNumLegacyUpdate_Object = MibTableColumn
swDbDataNumLegacyUpdate = _SwDbDataNumLegacyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 14),
    _SwDbDataNumLegacyUpdate_Type()
)
swDbDataNumLegacyUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNumLegacyUpdate.setStatus("current")
_SwDbDataNumSaNotReady_Type = Unsigned32
_SwDbDataNumSaNotReady_Object = MibTableColumn
swDbDataNumSaNotReady = _SwDbDataNumSaNotReady_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 15),
    _SwDbDataNumSaNotReady_Type()
)
swDbDataNumSaNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNumSaNotReady.setStatus("current")
_SwDbDataNumNsaNotReady_Type = Unsigned32
_SwDbDataNumNsaNotReady_Object = MibTableColumn
swDbDataNumNsaNotReady = _SwDbDataNumNsaNotReady_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 16),
    _SwDbDataNumNsaNotReady_Type()
)
swDbDataNumNsaNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataNumNsaNotReady.setStatus("current")
_SwDbDataCapTable_Object = MibTable
swDbDataCapTable = _SwDbDataCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3)
)
if mibBuilder.loadTexts:
    swDbDataCapTable.setStatus("current")
_SwDbDataCapEntry_Object = MibTableRow
swDbDataCapEntry = _SwDbDataCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1)
)
swDbDataCapEntry.setIndexNames(
    (0, "ADVA-MIB", "swDbDataCapUpgradeRequest"),
)
if mibBuilder.loadTexts:
    swDbDataCapEntry.setStatus("current")


class _SwDbDataCapUpgradeRequest_Type(Integer32):
    """Custom type swDbDataCapUpgradeRequest based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("download", 2),
          ("install", 3),
          ("activate", 4),
          ("revertToPrevious", 5),
          ("reboot", 6),
          ("downloadInstallActivateReboot", 7),
          ("installActivateReboot", 8),
          ("revertToPreviousReboot", 9),
          ("activateAlp", 10),
          ("activateDefaultAlp", 11),
          ("upload", 12),
          ("autoDownloadInstall", 13),
          ("autoInstall", 14),
          ("fwpInstall", 15),
          ("fwpDownloadInstall", 16),
          ("downloadCf", 17),
          ("uploadCf", 18),
          ("installCf", 19),
          ("autoInstallCf", 20),
          ("uploadPa", 21),
          ("activateWithFwp", 22),
          ("forceReboot", 23),
          ("stbyFwpInstall", 24))
    )


_SwDbDataCapUpgradeRequest_Type.__name__ = "Integer32"
_SwDbDataCapUpgradeRequest_Object = MibTableColumn
swDbDataCapUpgradeRequest = _SwDbDataCapUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1, 1),
    _SwDbDataCapUpgradeRequest_Type()
)
swDbDataCapUpgradeRequest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDbDataCapUpgradeRequest.setStatus("current")
_SwDbDataCapRestoreConfig_Type = RestoreActivationCaps
_SwDbDataCapRestoreConfig_Object = MibTableColumn
swDbDataCapRestoreConfig = _SwDbDataCapRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1, 2),
    _SwDbDataCapRestoreConfig_Type()
)
swDbDataCapRestoreConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataCapRestoreConfig.setStatus("current")
_SwDbDataDefaultsTable_Object = MibTable
swDbDataDefaultsTable = _SwDbDataDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4)
)
if mibBuilder.loadTexts:
    swDbDataDefaultsTable.setStatus("current")
_SwDbDataDefaultsEntry_Object = MibTableRow
swDbDataDefaultsEntry = _SwDbDataDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1)
)
swDbDataDefaultsEntry.setIndexNames(
    (0, "ADVA-MIB", "swDbDataDefaultsUpgradeRequest"),
)
if mibBuilder.loadTexts:
    swDbDataDefaultsEntry.setStatus("current")


class _SwDbDataDefaultsUpgradeRequest_Type(Integer32):
    """Custom type swDbDataDefaultsUpgradeRequest based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("download", 2),
          ("install", 3),
          ("activate", 4),
          ("revertToPrevious", 5),
          ("reboot", 6),
          ("downloadInstallActivateReboot", 7),
          ("installActivateReboot", 8),
          ("revertToPreviousReboot", 9),
          ("activateAlp", 10),
          ("activateDefaultAlp", 11),
          ("upload", 12),
          ("autoDownloadInstall", 13),
          ("autoInstall", 14),
          ("fwpInstall", 15),
          ("fwpDownloadInstall", 16),
          ("downloadCf", 17),
          ("uploadCf", 18),
          ("installCf", 19),
          ("autoInstallCf", 20),
          ("uploadPa", 21),
          ("activateWithFwp", 22),
          ("forceReboot", 23),
          ("stbyFwpInstall", 24))
    )


_SwDbDataDefaultsUpgradeRequest_Type.__name__ = "Integer32"
_SwDbDataDefaultsUpgradeRequest_Object = MibTableColumn
swDbDataDefaultsUpgradeRequest = _SwDbDataDefaultsUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1, 1),
    _SwDbDataDefaultsUpgradeRequest_Type()
)
swDbDataDefaultsUpgradeRequest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDbDataDefaultsUpgradeRequest.setStatus("current")
_SwDbDataDefaultsRestoreConfig_Type = RestoreActivation
_SwDbDataDefaultsRestoreConfig_Object = MibTableColumn
swDbDataDefaultsRestoreConfig = _SwDbDataDefaultsRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1, 2),
    _SwDbDataDefaultsRestoreConfig_Type()
)
swDbDataDefaultsRestoreConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataDefaultsRestoreConfig.setStatus("current")
_SnmpAgent_ObjectIdentity = ObjectIdentity
snmpAgent = _SnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7)
)
_SnmpServerPort_Type = Integer32
_SnmpServerPort_Object = MibScalar
snmpServerPort = _SnmpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 2),
    _SnmpServerPort_Type()
)
snmpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpServerPort.setStatus("current")
_SnmpProxyServerAdminState_Type = FspR7AdminStateSnmpProxy
_SnmpProxyServerAdminState_Object = MibScalar
snmpProxyServerAdminState = _SnmpProxyServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 3),
    _SnmpProxyServerAdminState_Type()
)
snmpProxyServerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyServerAdminState.setStatus("current")
_SnmpProxyServerPort_Type = Integer32
_SnmpProxyServerPort_Object = MibScalar
snmpProxyServerPort = _SnmpProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 4),
    _SnmpProxyServerPort_Type()
)
snmpProxyServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpProxyServerPort.setStatus("current")
_SnmpProxyServerSynchroState_Type = SnmpProxySynchronizationState
_SnmpProxyServerSynchroState_Object = MibScalar
snmpProxyServerSynchroState = _SnmpProxyServerSynchroState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 5),
    _SnmpProxyServerSynchroState_Type()
)
snmpProxyServerSynchroState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyServerSynchroState.setStatus("current")
_SnmpProxyServerSynchroStage_Type = SnmpProxySynchronizationStage
_SnmpProxyServerSynchroStage_Object = MibScalar
snmpProxyServerSynchroStage = _SnmpProxyServerSynchroStage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 6),
    _SnmpProxyServerSynchroStage_Type()
)
snmpProxyServerSynchroStage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpProxyServerSynchroStage.setStatus("current")
_SnmpProxyEntrySingleTargetOutTable_Object = MibTable
snmpProxyEntrySingleTargetOutTable = _SnmpProxyEntrySingleTargetOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutTable.setStatus("current")
_SnmpProxyEntrySingleTargetOutEntry_Object = MibTableRow
snmpProxyEntrySingleTargetOutEntry = _SnmpProxyEntrySingleTargetOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1)
)
snmpProxyEntrySingleTargetOutEntry.setIndexNames(
    (0, "ADVA-MIB", "snmpProxyEntrySingleTargetOutAddress"),
    (0, "ADVA-MIB", "snmpProxyEntrySingleTargetOutPort"),
)
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutEntry.setStatus("current")
_SnmpProxyEntrySingleTargetOutAddress_Type = IpAddress
_SnmpProxyEntrySingleTargetOutAddress_Object = MibTableColumn
snmpProxyEntrySingleTargetOutAddress = _SnmpProxyEntrySingleTargetOutAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 1),
    _SnmpProxyEntrySingleTargetOutAddress_Type()
)
snmpProxyEntrySingleTargetOutAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutAddress.setStatus("current")


class _SnmpProxyEntrySingleTargetOutPort_Type(Unsigned32):
    """Custom type snmpProxyEntrySingleTargetOutPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpProxyEntrySingleTargetOutPort_Type.__name__ = "Unsigned32"
_SnmpProxyEntrySingleTargetOutPort_Object = MibTableColumn
snmpProxyEntrySingleTargetOutPort = _SnmpProxyEntrySingleTargetOutPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 2),
    _SnmpProxyEntrySingleTargetOutPort_Type()
)
snmpProxyEntrySingleTargetOutPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutPort.setStatus("current")
_SnmpProxyEntrySingleTargetOutNodeAgentStatus_Type = DestinationNodeOrAgentState
_SnmpProxyEntrySingleTargetOutNodeAgentStatus_Object = MibTableColumn
snmpProxyEntrySingleTargetOutNodeAgentStatus = _SnmpProxyEntrySingleTargetOutNodeAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 3),
    _SnmpProxyEntrySingleTargetOutNodeAgentStatus_Type()
)
snmpProxyEntrySingleTargetOutNodeAgentStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutNodeAgentStatus.setStatus("current")
_SnmpProxyEntrySingleTargetOutContext_Type = SnmpAdminString
_SnmpProxyEntrySingleTargetOutContext_Object = MibTableColumn
snmpProxyEntrySingleTargetOutContext = _SnmpProxyEntrySingleTargetOutContext_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 4),
    _SnmpProxyEntrySingleTargetOutContext_Type()
)
snmpProxyEntrySingleTargetOutContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutContext.setStatus("current")
_SnmpProxyEntrySingleTargetOutRowStatus_Type = RowStatus
_SnmpProxyEntrySingleTargetOutRowStatus_Object = MibTableColumn
snmpProxyEntrySingleTargetOutRowStatus = _SnmpProxyEntrySingleTargetOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 5),
    _SnmpProxyEntrySingleTargetOutRowStatus_Type()
)
snmpProxyEntrySingleTargetOutRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutRowStatus.setStatus("current")
_SnmpProxyEntrySingleTargetOutAdminState_Type = FspR7AdminStateSnmpProxy
_SnmpProxyEntrySingleTargetOutAdminState_Object = MibTableColumn
snmpProxyEntrySingleTargetOutAdminState = _SnmpProxyEntrySingleTargetOutAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 6),
    _SnmpProxyEntrySingleTargetOutAdminState_Type()
)
snmpProxyEntrySingleTargetOutAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutAdminState.setStatus("current")
_SnmpProxyEntrySingleTargetOutUserName_Type = SnmpAdminString
_SnmpProxyEntrySingleTargetOutUserName_Object = MibTableColumn
snmpProxyEntrySingleTargetOutUserName = _SnmpProxyEntrySingleTargetOutUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 7),
    _SnmpProxyEntrySingleTargetOutUserName_Type()
)
snmpProxyEntrySingleTargetOutUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyEntrySingleTargetOutUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-MIB",
    **{"OnOff": OnOff,
       "AvailState": AvailState,
       "EnableState": EnableState,
       "ArcState": ArcState,
       "TrapAlarmSeverity": TrapAlarmSeverity,
       "ServiceImpairment": ServiceImpairment,
       "TrapCounter": TrapCounter,
       "Counter64String": Counter64String,
       "KBytes": KBytes,
       "IdentityTranslation": IdentityTranslation,
       "NeSwUpgradeStatusType": NeSwUpgradeStatusType,
       "NeSwInstallStatusType": NeSwInstallStatusType,
       "FileTransferProtocol": FileTransferProtocol,
       "SourceIpAddress": SourceIpAddress,
       "F7FileTimeStamp": F7FileTimeStamp,
       "F7AutoBackupInterval": F7AutoBackupInterval,
       "F7AutoBackupRunState": F7AutoBackupRunState,
       "PartitionStatus": PartitionStatus,
       "FspDate": FspDate,
       "FspTime": FspTime,
       "ApsDirection": ApsDirection,
       "ApsDirectionCaps": ApsDirectionCaps,
       "ApsHoldoffTime": ApsHoldoffTime,
       "ApsHoldoffTimeCaps": ApsHoldoffTimeCaps,
       "AssignmentState": AssignmentState,
       "BootState": BootState,
       "CommandEqpt": CommandEqpt,
       "CpWdmEntityClass": CpWdmEntityClass,
       "EnableStateCaps": EnableStateCaps,
       "EntityClass": EntityClass,
       "EntityIndex": EntityIndex,
       "EntityType": EntityType,
       "EquipmentState": EquipmentState,
       "EthDuplexMode": EthDuplexMode,
       "EthDuplexModeCaps": EthDuplexModeCaps,
       "FileArea": FileArea,
       "FileType": FileType,
       "FspR7AdminStateSnmpProxy": FspR7AdminStateSnmpProxy,
       "FspR7AdminStateSnmpProxyCaps": FspR7AdminStateSnmpProxyCaps,
       "FspR7Date": FspR7Date,
       "FspR7EnableDisable": FspR7EnableDisable,
       "FspR7EquipmentType": FspR7EquipmentType,
       "FspR7EquipmentTypeCaps": FspR7EquipmentTypeCaps,
       "FspR7FalseTrue": FspR7FalseTrue,
       "FspR7Time": FspR7Time,
       "FspR7YesNo": FspR7YesNo,
       "FspR7UsersDb": FspR7UsersDb,
       "Grade": Grade,
       "LoopConfig": LoopConfig,
       "LoopConfigCaps": LoopConfigCaps,
       "DestinationNodeOrAgentState": DestinationNodeOrAgentState,
       "NcuAutoActivation": NcuAutoActivation,
       "NoYesNA": NoYesNA,
       "OhTerminationLevel": OhTerminationLevel,
       "OhTerminationLevelCaps": OhTerminationLevelCaps,
       "OtnPayloadType": OtnPayloadType,
       "OtnPayloadTypeCaps": OtnPayloadTypeCaps,
       "OtnTcmLevel": OtnTcmLevel,
       "OtnTcmLevelCaps": OtnTcmLevelCaps,
       "PgmType": PgmType,
       "ProtectionMech": ProtectionMech,
       "ProtectionMechCaps": ProtectionMechCaps,
       "RestoreActivation": RestoreActivation,
       "RestoreActivationCaps": RestoreActivationCaps,
       "ServiceAffecting": ServiceAffecting,
       "ServiceAffectingCaps": ServiceAffectingCaps,
       "StandbyServiceAffecting": StandbyServiceAffecting,
       "SnmpProxySynchronizationState": SnmpProxySynchronizationState,
       "SnmpProxySynchronizationStage": SnmpProxySynchronizationStage,
       "SonetSectSigDegThres": SonetSectSigDegThres,
       "SonetSectSigDegThresCaps": SonetSectSigDegThresCaps,
       "SonetTimingSource": SonetTimingSource,
       "SonetTimingSourceCaps": SonetTimingSourceCaps,
       "SonetTraceForm": SonetTraceForm,
       "SonetTraceFormCaps": SonetTraceFormCaps,
       "SonetVcBundleAllocation": SonetVcBundleAllocation,
       "SonetVcBundleAllocationCaps": SonetVcBundleAllocationCaps,
       "TimMode": TimMode,
       "TimModeCaps": TimModeCaps,
       "FspR7TrapsinkLifetime": FspR7TrapsinkLifetime,
       "VirtualContainerType": VirtualContainerType,
       "VirtualContainerTypeCaps": VirtualContainerTypeCaps,
       "YesNoNA": YesNoNA,
       "LogicalIfTransport": LogicalIfTransport,
       "LogicalIfTransportCaps": LogicalIfTransportCaps,
       "ModuleForm": ModuleForm,
       "advaMIB": advaMIB,
       "products": products,
       "fsp3000": fsp3000,
       "fsp1000": fsp1000,
       "fsp2000": fsp2000,
       "fsp1000adm": fsp1000adm,
       "fsp1500": fsp1500,
       "fsp150": fsp150,
       "fspR7": fspR7,
       "fsp150cm": fsp150cm,
       "fspNm": fspNm,
       "fsp3000alm": fsp3000alm,
       "aos": aos,
       "aosCommon": aosCommon,
       "aosProducts": aosProducts,
       "fsp3000c": fsp3000c,
       "fspxg480": fspxg480,
       "fspxg404": fspxg404,
       "fspxg418": fspxg418,
       "fspxg480-25g-100g": fspxg480_25g_100g,
       "fspxg480-100g": fspxg480_100g,
       "fspxg480-100gcfp2": fspxg480_100gcfp2,
       "fspxg404-100g": fspxg404_100g,
       "fspxg404-100gcfp2": fspxg404_100gcfp2,
       "fspxg418-100g": fspxg418_100g,
       "fspxg418-100gcfp2": fspxg418_100gcfp2,
       "fspxg118pro-cshac": fspxg118pro_cshac,
       "fspxg118pro-cshdc": fspxg118pro_cshdc,
       "fspxg118pro-cshac-g": fspxg118pro_cshac_g,
       "fspxg118pro-cshdc-g": fspxg118pro_cshdc_g,
       "common": common,
       "neInfo": neInfo,
       "neMibVariant": neMibVariant,
       "neManufacturer": neManufacturer,
       "neDateAndTime": neDateAndTime,
       "neMemorySizeTotal": neMemorySizeTotal,
       "neMemorySizeFree": neMemorySizeFree,
       "neStorageTable": neStorageTable,
       "neStorageEntry": neStorageEntry,
       "neStorageIndex": neStorageIndex,
       "neStorageDescr": neStorageDescr,
       "neStorageCapacity": neStorageCapacity,
       "neStorageAvailable": neStorageAvailable,
       "neAlarmStatus": neAlarmStatus,
       "admin": admin,
       "snmpWriteAccessRestriction": snmpWriteAccessRestriction,
       "snmpWriteAccessTable": snmpWriteAccessTable,
       "snmpWriteAccessEntry": snmpWriteAccessEntry,
       "snmpWriteAccessNmsAddress": snmpWriteAccessNmsAddress,
       "snmpWriteAccessNmsName": snmpWriteAccessNmsName,
       "events": events,
       "neEventsLogged": neEventsLogged,
       "neEventLogTable": neEventLogTable,
       "neEventLogEntry": neEventLogEntry,
       "neEventLogIndex": neEventLogIndex,
       "neEventLogTimeStamp": neEventLogTimeStamp,
       "neEventLogNotificationOID": neEventLogNotificationOID,
       "neEventLogIdentityTranslation": neEventLogIdentityTranslation,
       "neEventLogVarTable": neEventLogVarTable,
       "neEventLogVarEntry": neEventLogVarEntry,
       "neEventLogVarIndex": neEventLogVarIndex,
       "neEventLogVarId": neEventLogVarId,
       "neEventLogVarType": neEventLogVarType,
       "neEventLogVarInteger32Val": neEventLogVarInteger32Val,
       "neEventLogVarIpAddressVal": neEventLogVarIpAddressVal,
       "neEventLogVarOctetStringVal": neEventLogVarOctetStringVal,
       "neEventLogVarOidVal": neEventLogVarOidVal,
       "neEventLogVarCounter64Val": neEventLogVarCounter64Val,
       "neEventLogVarUnsigned32Val": neEventLogVarUnsigned32Val,
       "neTrapsinkTable": neTrapsinkTable,
       "neTrapsinkEntry": neTrapsinkEntry,
       "neTrapsinkAddress": neTrapsinkAddress,
       "neTrapsinkPort": neTrapsinkPort,
       "neTrapsinkCommunity": neTrapsinkCommunity,
       "neTrapsinkRowStatus": neTrapsinkRowStatus,
       "neTrapsinkVersion": neTrapsinkVersion,
       "neTrapsinkUserName": neTrapsinkUserName,
       "neTrapsinkType": neTrapsinkType,
       "software": software,
       "swVersionTable": swVersionTable,
       "swVersionEntry": swVersionEntry,
       "swVersionActiveApplSw": swVersionActiveApplSw,
       "swVersionInactiveApplSw": swVersionInactiveApplSw,
       "swVersionActiveOperatingSw": swVersionActiveOperatingSw,
       "swVersionInactiveOperatingSw": swVersionInactiveOperatingSw,
       "swVersionNextBoot": swVersionNextBoot,
       "neSoftwareUpgrade": neSoftwareUpgrade,
       "neSwUpgradeRequest": neSwUpgradeRequest,
       "neSwUpgradeState": neSwUpgradeState,
       "neSwUpgradeServerAddress": neSwUpgradeServerAddress,
       "neSwUpgradeServerLogin": neSwUpgradeServerLogin,
       "neSwUpgradeServerPasswd": neSwUpgradeServerPasswd,
       "neSwUpgradeServerDirectory": neSwUpgradeServerDirectory,
       "neSwUpgradeFileName": neSwUpgradeFileName,
       "neSwUpgradeNeDirectory": neSwUpgradeNeDirectory,
       "neSwUpgradeTransferProtocol": neSwUpgradeTransferProtocol,
       "sourceIpAddress": sourceIpAddress,
       "neSwInstallState": neSwInstallState,
       "neSwUpgradeType": neSwUpgradeType,
       "neSwDownloadProgress": neSwDownloadProgress,
       "neSwUpgradeCommonIpSrv": neSwUpgradeCommonIpSrv,
       "config": config,
       "provContainerTable": provContainerTable,
       "provContainerEntry": provContainerEntry,
       "provAssignmentState": provAssignmentState,
       "provEquipmentState": provEquipmentState,
       "neBackupRestore": neBackupRestore,
       "neBackupRestoreRequest": neBackupRestoreRequest,
       "neBackupRestoreState": neBackupRestoreState,
       "neBackupRestoreFile": neBackupRestoreFile,
       "neRestoreFileBackupDate": neRestoreFileBackupDate,
       "neF7AutomaticRemoteBackupSrvIp": neF7AutomaticRemoteBackupSrvIp,
       "neF7AutomaticRemoteBackupSrvDir": neF7AutomaticRemoteBackupSrvDir,
       "neF7AutomaticRemoteBackupSrvLogin": neF7AutomaticRemoteBackupSrvLogin,
       "neF7AutomaticRemoteBackupSrvPass": neF7AutomaticRemoteBackupSrvPass,
       "neF7AutomaticRemoteBackupProtocol": neF7AutomaticRemoteBackupProtocol,
       "neF7AutomaticRemoteBackupSrcIp": neF7AutomaticRemoteBackupSrcIp,
       "neF7AutomaticRemoteBackupTimeStamp": neF7AutomaticRemoteBackupTimeStamp,
       "neF7AutomaticRemoteBackupCommonIpSrv": neF7AutomaticRemoteBackupCommonIpSrv,
       "neF7AutomaticBackupTable": neF7AutomaticBackupTable,
       "neF7AutomaticBackupEntry": neF7AutomaticBackupEntry,
       "neF7AutomaticBackupIndex": neF7AutomaticBackupIndex,
       "neF7AutomaticBackupInterval": neF7AutomaticBackupInterval,
       "neF7AutomaticBackupStartDate": neF7AutomaticBackupStartDate,
       "neF7AutomaticBackupStartTime": neF7AutomaticBackupStartTime,
       "neF7AutomaticBackupNextDate": neF7AutomaticBackupNextDate,
       "neF7AutomaticBackupRunState": neF7AutomaticBackupRunState,
       "neF7AutomaticBackupTimeStamp": neF7AutomaticBackupTimeStamp,
       "neAutoBackup": neAutoBackup,
       "neAutoBackupConfig": neAutoBackupConfig,
       "neAutoBackupInterval": neAutoBackupInterval,
       "neAutoBackupNextActionAt": neAutoBackupNextActionAt,
       "neAutoBackupServerAddress": neAutoBackupServerAddress,
       "neAutoBackupServerLogin": neAutoBackupServerLogin,
       "neAutoBackupServerPasswd": neAutoBackupServerPasswd,
       "neAutoBackupServerDirectory": neAutoBackupServerDirectory,
       "transportStandards": transportStandards,
       "sonet": sonet,
       "sonetConfig": sonetConfig,
       "sonetSectionConfigTable": sonetSectionConfigTable,
       "sonetSectionConfigEntry": sonetSectionConfigEntry,
       "sonetSectionConfigTimingSource": sonetSectionConfigTimingSource,
       "sonetSectionConfigSignalDegradeThreshhold": sonetSectionConfigSignalDegradeThreshhold,
       "sonetSectionConfigSignalDegradePeriod": sonetSectionConfigSignalDegradePeriod,
       "sonetSectionConfigTraceForm": sonetSectionConfigTraceForm,
       "sonetSectionConfigTraceExpected": sonetSectionConfigTraceExpected,
       "sonetSectionConfigTraceTransmit": sonetSectionConfigTraceTransmit,
       "sonetSectionConfigTimMode": sonetSectionConfigTimMode,
       "sonetSectionDataTable": sonetSectionDataTable,
       "sonetSectionDataEntry": sonetSectionDataEntry,
       "sonetSectionDataTraceReceived": sonetSectionDataTraceReceived,
       "otn": otn,
       "otuConfig": otuConfig,
       "otuSectionConfigTable": otuSectionConfigTable,
       "otuSectionConfigEntry": otuSectionConfigEntry,
       "otuSectionConfigSignalDegradeThreshold": otuSectionConfigSignalDegradeThreshold,
       "otuSectionConfigSignalDegradePeriod": otuSectionConfigSignalDegradePeriod,
       "otuSectionConfigPayload": otuSectionConfigPayload,
       "otuSectionConfigStuffing": otuSectionConfigStuffing,
       "otuSectionConfigTraceExpected": otuSectionConfigTraceExpected,
       "otuSectionConfigTraceTransmitSapi": otuSectionConfigTraceTransmitSapi,
       "otuSectionConfigTraceTransmitDapi": otuSectionConfigTraceTransmitDapi,
       "otuSectionConfigTraceTransmitOpsp": otuSectionConfigTraceTransmitOpsp,
       "otuSectionConfigTimMode": otuSectionConfigTimMode,
       "otuSectionDataTable": otuSectionDataTable,
       "otuSectionDataEntry": otuSectionDataEntry,
       "otuSectionDataResultingTotalBitrate": otuSectionDataResultingTotalBitrate,
       "otuSectionDataTraceReceivedSapi": otuSectionDataTraceReceivedSapi,
       "otuSectionDataTraceReceivedDapi": otuSectionDataTraceReceivedDapi,
       "otuSectionDataTraceReceivedOpsp": otuSectionDataTraceReceivedOpsp,
       "oduConfig": oduConfig,
       "oduSectionConfigTable": oduSectionConfigTable,
       "oduSectionConfigEntry": oduSectionConfigEntry,
       "oduSectionConfigSignalDegradeThres": oduSectionConfigSignalDegradeThres,
       "oduSectionConfigSignalDegradePeriod": oduSectionConfigSignalDegradePeriod,
       "oduSectionConfigTraceExpected": oduSectionConfigTraceExpected,
       "oduSectionConfigTraceTransmitSapi": oduSectionConfigTraceTransmitSapi,
       "oduSectionConfigTraceTransmitDapi": oduSectionConfigTraceTransmitDapi,
       "oduSectionConfigTraceTransmitOpsp": oduSectionConfigTraceTransmitOpsp,
       "oduSectionConfigTimMode": oduSectionConfigTimMode,
       "oduSectionDataTable": oduSectionDataTable,
       "oduSectionDataEntry": oduSectionDataEntry,
       "oduSectionDataTraceReceivedSapi": oduSectionDataTraceReceivedSapi,
       "oduSectionDataTraceReceivedDapi": oduSectionDataTraceReceivedDapi,
       "oduSectionDataTraceReceivedOpsp": oduSectionDataTraceReceivedOpsp,
       "oduTcmAConfigTable": oduTcmAConfigTable,
       "oduTcmAConfigEntry": oduTcmAConfigEntry,
       "oduTcmAConfigSignalDegradeThreshold": oduTcmAConfigSignalDegradeThreshold,
       "oduTcmAConfigSignalDegradePeriod": oduTcmAConfigSignalDegradePeriod,
       "oduTcmAConfigTcmLevel": oduTcmAConfigTcmLevel,
       "oduTcmAConfigTraceExpected": oduTcmAConfigTraceExpected,
       "oduTcmAConfigTraceTransmitSapi": oduTcmAConfigTraceTransmitSapi,
       "oduTcmAConfigTraceTransmitDapi": oduTcmAConfigTraceTransmitDapi,
       "oduTcmAConfigTraceTransmitOpsp": oduTcmAConfigTraceTransmitOpsp,
       "oduTcmAConfigTimMode": oduTcmAConfigTimMode,
       "oduTcmBConfigTable": oduTcmBConfigTable,
       "oduTcmBConfigEntry": oduTcmBConfigEntry,
       "oduTcmBConfigSignalDegradeThreshold": oduTcmBConfigSignalDegradeThreshold,
       "oduTcmBConfigSignalDegradePeriod": oduTcmBConfigSignalDegradePeriod,
       "oduTcmBConfigTcmLevel": oduTcmBConfigTcmLevel,
       "oduTcmBConfigTraceExpected": oduTcmBConfigTraceExpected,
       "oduTcmBConfigTraceTransmitSapi": oduTcmBConfigTraceTransmitSapi,
       "oduTcmBConfigTraceTransmitDapi": oduTcmBConfigTraceTransmitDapi,
       "oduTcmBConfigTraceTransmitOpsp": oduTcmBConfigTraceTransmitOpsp,
       "oduTcmBConfigTimMode": oduTcmBConfigTimMode,
       "oduTcmCConfigTable": oduTcmCConfigTable,
       "oduTcmCConfigEntry": oduTcmCConfigEntry,
       "oduTcmCConfigSignalDegradeThreshold": oduTcmCConfigSignalDegradeThreshold,
       "oduTcmCConfigSignalDegradePeriod": oduTcmCConfigSignalDegradePeriod,
       "oduTcmCConfigTcmLevel": oduTcmCConfigTcmLevel,
       "oduTcmCConfigTraceExpected": oduTcmCConfigTraceExpected,
       "oduTcmCConfigTraceTransmitSapi": oduTcmCConfigTraceTransmitSapi,
       "oduTcmCConfigTraceTransmitDapi": oduTcmCConfigTraceTransmitDapi,
       "oduTcmCConfigTraceTransmitOpsp": oduTcmCConfigTraceTransmitOpsp,
       "oduTcmCConfigTimMode": oduTcmCConfigTimMode,
       "oduTcmADataTable": oduTcmADataTable,
       "oduTcmADataEntry": oduTcmADataEntry,
       "oduTcmADataTraceReceivedSapi": oduTcmADataTraceReceivedSapi,
       "oduTcmADataTraceReceivedDapi": oduTcmADataTraceReceivedDapi,
       "oduTcmADataTraceReceivedOpsp": oduTcmADataTraceReceivedOpsp,
       "oduTcmBDataTable": oduTcmBDataTable,
       "oduTcmBDataEntry": oduTcmBDataEntry,
       "oduTcmBDataTraceReceivedSapi": oduTcmBDataTraceReceivedSapi,
       "oduTcmBDataTraceReceivedDapi": oduTcmBDataTraceReceivedDapi,
       "oduTcmBDataTraceReceivedOpsp": oduTcmBDataTraceReceivedOpsp,
       "oduTcmCDataTable": oduTcmCDataTable,
       "oduTcmCDataEntry": oduTcmCDataEntry,
       "oduTcmCDataTraceReceivedSapi": oduTcmCDataTraceReceivedSapi,
       "oduTcmCDataTraceReceivedDapi": oduTcmCDataTraceReceivedDapi,
       "oduTcmCDataTraceReceivedOpsp": oduTcmCDataTraceReceivedOpsp,
       "inventoryMib": inventoryMib,
       "inventoryTable": inventoryTable,
       "inventoryEntry": inventoryEntry,
       "inventoryUnitName": inventoryUnitName,
       "inventoryFirmwarePackageRev": inventoryFirmwarePackageRev,
       "inventoryHardwareRev": inventoryHardwareRev,
       "inventorySoftwareRev": inventorySoftwareRev,
       "inventoryFpgaRev": inventoryFpgaRev,
       "inventorySerialNum": inventorySerialNum,
       "inventoryPartnumber": inventoryPartnumber,
       "inventoryCleiCode": inventoryCleiCode,
       "inventoryVendorId": inventoryVendorId,
       "inventoryType": inventoryType,
       "inventoryUniversalSerialIdent": inventoryUniversalSerialIdent,
       "inventoryMacAddress": inventoryMacAddress,
       "inventoryGradeInventory": inventoryGradeInventory,
       "inventoryCfSerialNum": inventoryCfSerialNum,
       "inventoryCfModel": inventoryCfModel,
       "entityTable": entityTable,
       "entityEntry": entityEntry,
       "entityIndex": entityIndex,
       "entityContainedIn": entityContainedIn,
       "entityClass": entityClass,
       "entityClassInstanceNumber": entityClassInstanceNumber,
       "entityIndexAid": entityIndexAid,
       "entityType": entityType,
       "entityAssignmentState": entityAssignmentState,
       "entityEquipmentState": entityEquipmentState,
       "containsTable": containsTable,
       "containsEntry": containsEntry,
       "containsIndex": containsIndex,
       "controlPlaneWdmEntityTable": controlPlaneWdmEntityTable,
       "controlPlaneWdmEntityEntry": controlPlaneWdmEntityEntry,
       "controlPlaneWdmEntityIndex": controlPlaneWdmEntityIndex,
       "controlPlaneWdmEntityContainedIn": controlPlaneWdmEntityContainedIn,
       "controlPlaneWdmEntityClass": controlPlaneWdmEntityClass,
       "controlPlaneWdmEntityClassInstanceNumber": controlPlaneWdmEntityClassInstanceNumber,
       "controlPlaneWdmEntityIndexAid": controlPlaneWdmEntityIndexAid,
       "controlPlaneWdmEntityAssignmentState": controlPlaneWdmEntityAssignmentState,
       "controlPlaneWdmContainsTable": controlPlaneWdmContainsTable,
       "controlPlaneWdmContainsEntry": controlPlaneWdmContainsEntry,
       "controlPlaneWdmContainsIndex": controlPlaneWdmContainsIndex,
       "controlPlaneEthEntityTable": controlPlaneEthEntityTable,
       "controlPlaneEthEntityEntry": controlPlaneEthEntityEntry,
       "controlPlaneEthEntityIndex": controlPlaneEthEntityIndex,
       "controlPlaneEthEntityContainedIn": controlPlaneEthEntityContainedIn,
       "controlPlaneEthEntityClass": controlPlaneEthEntityClass,
       "controlPlaneEthEntityClassInstanceNumber": controlPlaneEthEntityClassInstanceNumber,
       "controlPlaneEthEntityIndexAid": controlPlaneEthEntityIndexAid,
       "controlPlaneEthEntityAssignmentState": controlPlaneEthEntityAssignmentState,
       "controlPlaneEthContainsTable": controlPlaneEthContainsTable,
       "controlPlaneEthContainsEntry": controlPlaneEthContainsEntry,
       "controlPlaneEthContainsIndex": controlPlaneEthContainsIndex,
       "ptpEntityTable": ptpEntityTable,
       "ptpEntityEntry": ptpEntityEntry,
       "ptpEntityIndex": ptpEntityIndex,
       "ptpEntityContainedIn": ptpEntityContainedIn,
       "ptpEntityClass": ptpEntityClass,
       "ptpEntityClassInstanceNumber": ptpEntityClassInstanceNumber,
       "ptpEntityIndexAid": ptpEntityIndexAid,
       "ptpEntityType": ptpEntityType,
       "ptpEntityAssignmentState": ptpEntityAssignmentState,
       "ptpEntityEquipmentState": ptpEntityEquipmentState,
       "ptpEntityReferencedTo": ptpEntityReferencedTo,
       "vtpEntityTable": vtpEntityTable,
       "vtpEntityEntry": vtpEntityEntry,
       "vtpEntityIndex": vtpEntityIndex,
       "vtpEntityContainedIn": vtpEntityContainedIn,
       "vtpEntityClass": vtpEntityClass,
       "vtpEntityClassInstanceNumber": vtpEntityClassInstanceNumber,
       "vtpEntityIndexAid": vtpEntityIndexAid,
       "vtpEntityType": vtpEntityType,
       "vtpEntityAssignmentState": vtpEntityAssignmentState,
       "vtpEntityEquipmentState": vtpEntityEquipmentState,
       "vtpEntityReferencedTo": vtpEntityReferencedTo,
       "controlPlaneOtnEntityTable": controlPlaneOtnEntityTable,
       "controlPlaneOtnEntityEntry": controlPlaneOtnEntityEntry,
       "controlPlaneOtnEntityIndex": controlPlaneOtnEntityIndex,
       "controlPlaneOtnEntityContainedIn": controlPlaneOtnEntityContainedIn,
       "controlPlaneOtnEntityClass": controlPlaneOtnEntityClass,
       "controlPlaneOtnEntityClassInstanceNumber": controlPlaneOtnEntityClassInstanceNumber,
       "controlPlaneOtnEntityIndexAid": controlPlaneOtnEntityIndexAid,
       "controlPlaneOtnEntityAssignmentState": controlPlaneOtnEntityAssignmentState,
       "controlPlaneOtnContainsTable": controlPlaneOtnContainsTable,
       "controlPlaneOtnContainsEntry": controlPlaneOtnContainsEntry,
       "controlPlaneOtnContainsIndex": controlPlaneOtnContainsIndex,
       "updateBackupRestoreMib": updateBackupRestoreMib,
       "swAdmin": swAdmin,
       "swDbFileTable": swDbFileTable,
       "swDbFileEntry": swDbFileEntry,
       "swDbFileIndex": swDbFileIndex,
       "swDbFileArea": swDbFileArea,
       "swDbFileType": swDbFileType,
       "swDbFileSize": swDbFileSize,
       "swDbFileCreationTime": swDbFileCreationTime,
       "swDbFileVersion": swDbFileVersion,
       "swDbFileGrade": swDbFileGrade,
       "swDbFileComment": swDbFileComment,
       "swDbFileFileName": swDbFileFileName,
       "swDbFileRowStatus": swDbFileRowStatus,
       "swDbFilePgmType": swDbFilePgmType,
       "fwDataTable": fwDataTable,
       "fwDataEntry": fwDataEntry,
       "fwDataNewVersion": fwDataNewVersion,
       "fwDataStandbyVersion": fwDataStandbyVersion,
       "fwDataServiceImpairment": fwDataServiceImpairment,
       "fwDataBootStatus": fwDataBootStatus,
       "fwDataFirmwarePackageRev": fwDataFirmwarePackageRev,
       "fwDataStandbyServiceImpairment": fwDataStandbyServiceImpairment,
       "fwDataFirmwareAvailable": fwDataFirmwareAvailable,
       "fwDataFirmwareApproved": fwDataFirmwareApproved,
       "fwDataFirmwarePackageRevBackup": fwDataFirmwarePackageRevBackup,
       "fwDataReadyForActivation": fwDataReadyForActivation,
       "fwDataActivationReadyOnStandby": fwDataActivationReadyOnStandby,
       "fwDataProtectionPart": fwDataProtectionPart,
       "fwDataForm": fwDataForm,
       "fwDataStandbyFirmwareAvailable": fwDataStandbyFirmwareAvailable,
       "coldRestartCapTable": coldRestartCapTable,
       "coldRestartCapEntry": coldRestartCapEntry,
       "coldRestartCapServiceAffectingCap": coldRestartCapServiceAffectingCap,
       "eqpFwUpgradeRequest": eqpFwUpgradeRequest,
       "eqpFwServiceImpairment": eqpFwServiceImpairment,
       "eqpFwNextEqpForUpdate": eqpFwNextEqpForUpdate,
       "eqpFwEqpType": eqpFwEqpType,
       "eqpFwNcuServerBusy": eqpFwNcuServerBusy,
       "eqpFwEqpServerBusy": eqpFwEqpServerBusy,
       "updateEqpt": updateEqpt,
       "installedEqpt": installedEqpt,
       "selectedFile": selectedFile,
       "ncuActivationDate": ncuActivationDate,
       "ncuActivationTime": ncuActivationTime,
       "ncuScheduledActivation": ncuScheduledActivation,
       "ncuScheduledDbRestore": ncuScheduledDbRestore,
       "encryptionFwpFile": encryptionFwpFile,
       "clearRdiskRequest": clearRdiskRequest,
       "ncuActivationDateUtc": ncuActivationDateUtc,
       "ncuActivationTimeUtc": ncuActivationTimeUtc,
       "neBackupEncryption": neBackupEncryption,
       "neBackupPassword": neBackupPassword,
       "neF7AutomaticRemoteBackupEncryption": neF7AutomaticRemoteBackupEncryption,
       "neF7AutomaticRemoteBackupPassword": neF7AutomaticRemoteBackupPassword,
       "neBackupUsers": neBackupUsers,
       "neInitialConnectionMode": neInitialConnectionMode,
       "neF7AutomaticRemoteBackupUsers": neF7AutomaticRemoteBackupUsers,
       "dbAdmin": dbAdmin,
       "neRestoreConfig": neRestoreConfig,
       "swDbDataTable": swDbDataTable,
       "swDbDataEntry": swDbDataEntry,
       "swDbDataIndex": swDbDataIndex,
       "swDbDataArea": swDbDataArea,
       "swDbDataProgramVersion": swDbDataProgramVersion,
       "swDbDataDatabaseVersion": swDbDataDatabaseVersion,
       "swDbDataActivationTime": swDbDataActivationTime,
       "swDbDataRestoreConfig": swDbDataRestoreConfig,
       "swDbDataFirmwareSetVersion": swDbDataFirmwareSetVersion,
       "swDbDataNcuSoftwareVersion": swDbDataNcuSoftwareVersion,
       "swDbDataStandbyPartitionStatus": swDbDataStandbyPartitionStatus,
       "swDbDataNumEqpt": swDbDataNumEqpt,
       "swDbDataNumLegacyEqpt": swDbDataNumLegacyEqpt,
       "swDbDataNumNativeSaUpdate": swDbDataNumNativeSaUpdate,
       "swDbDataNumNativeNsaUpdate": swDbDataNumNativeNsaUpdate,
       "swDbDataNumLegacyUpdate": swDbDataNumLegacyUpdate,
       "swDbDataNumSaNotReady": swDbDataNumSaNotReady,
       "swDbDataNumNsaNotReady": swDbDataNumNsaNotReady,
       "swDbDataCapTable": swDbDataCapTable,
       "swDbDataCapEntry": swDbDataCapEntry,
       "swDbDataCapUpgradeRequest": swDbDataCapUpgradeRequest,
       "swDbDataCapRestoreConfig": swDbDataCapRestoreConfig,
       "swDbDataDefaultsTable": swDbDataDefaultsTable,
       "swDbDataDefaultsEntry": swDbDataDefaultsEntry,
       "swDbDataDefaultsUpgradeRequest": swDbDataDefaultsUpgradeRequest,
       "swDbDataDefaultsRestoreConfig": swDbDataDefaultsRestoreConfig,
       "snmpAgent": snmpAgent,
       "snmpServerPort": snmpServerPort,
       "snmpProxyServerAdminState": snmpProxyServerAdminState,
       "snmpProxyServerPort": snmpProxyServerPort,
       "snmpProxyServerSynchroState": snmpProxyServerSynchroState,
       "snmpProxyServerSynchroStage": snmpProxyServerSynchroStage,
       "snmpProxyEntrySingleTargetOutTable": snmpProxyEntrySingleTargetOutTable,
       "snmpProxyEntrySingleTargetOutEntry": snmpProxyEntrySingleTargetOutEntry,
       "snmpProxyEntrySingleTargetOutAddress": snmpProxyEntrySingleTargetOutAddress,
       "snmpProxyEntrySingleTargetOutPort": snmpProxyEntrySingleTargetOutPort,
       "snmpProxyEntrySingleTargetOutNodeAgentStatus": snmpProxyEntrySingleTargetOutNodeAgentStatus,
       "snmpProxyEntrySingleTargetOutContext": snmpProxyEntrySingleTargetOutContext,
       "snmpProxyEntrySingleTargetOutRowStatus": snmpProxyEntrySingleTargetOutRowStatus,
       "snmpProxyEntrySingleTargetOutAdminState": snmpProxyEntrySingleTargetOutAdminState,
       "snmpProxyEntrySingleTargetOutUserName": snmpProxyEntrySingleTargetOutUserName}
)
