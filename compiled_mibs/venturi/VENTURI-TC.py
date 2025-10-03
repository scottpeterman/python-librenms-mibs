# SNMP MIB module (VENTURI-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\venturi\VENTURI-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:48 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



class VenturiProtocolType(TextualConvention, Integer32):
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
        *(("all", 0),
          ("other", 1),
          ("http", 2),
          ("pop3", 3),
          ("imap", 4),
          ("smtp", 5),
          ("ftp", 6),
          ("telnet", 7),
          ("rtsp", 8))
    )



class VenturiSubscriberType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("clientless", 2))
    )



class VenturiConditionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1))
    )



class VenturiBooleanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )



class VenturiConditionType(TextualConvention, Integer32):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("softwareStopped", 1),
          ("swapOverload", 2),
          ("networkError", 3),
          ("kernelError", 4),
          ("licenseError", 5),
          ("sharedMemoryError", 6),
          ("fileSystemError", 7),
          ("tcpOverload", 8),
          ("cacheOverload", 9),
          ("logOverload", 10),
          ("fanFailure", 11),
          ("powerSupplyFailure", 12),
          ("highTemperature", 13),
          ("moduleInitFalure", 14),
          ("radiusServerFailure", 15),
          ("lowCriticalBuffers", 16),
          ("statsCollectionError", 17),
          ("logCollectionError", 18),
          ("urlCollectionError", 19),
          ("clientStatsCollectionError", 20),
          ("clientUpgradeCollectionError", 21),
          ("cdcLogCollectionError", 22))
    )



class VenturiPhysicalIfMode(TextualConvention, Integer32):
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
        *(("auto", 1),
          ("tenHalf", 2),
          ("tenFull", 3),
          ("hundredHalf", 4),
          ("hundredFull", 5),
          ("thousandFull", 6))
    )



class VenturiLogicalIfMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("bonding", 2))
    )



class VenturiLicenseName(TextualConvention, Integer32):
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
        *(("iproute", 0),
          ("vvs", 1),
          ("iptrans", 2),
          ("radiusAcct", 3),
          ("rtsp", 4))
    )



class VenturiLevel(TextualConvention, Integer32):
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
        *(("levelOne", 1),
          ("levelTwo", 2),
          ("levelThree", 3),
          ("levelFour", 4))
    )



class VenturiImageColorType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("lossy", 2),
          ("lossless", 3),
          ("noanim", 4))
    )



class VenturiImageColorValue(TextualConvention, Integer32):
    status = "current"
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("colorTwoBit", 2),
          ("colorFourBit", 4),
          ("colorEightBit", 8),
          ("colorSixteenBit", 16),
          ("colorThirtytwoBit", 32),
          ("colorSixtyfourBit", 64),
          ("colorOneTwentyeithyBit", 128),
          ("colorTwoFiftySixbit", 256))
    )



class VenturiLogLevels(TextualConvention, Integer32):
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warn", 5),
          ("notice", 6),
          ("info", 7),
          ("verbose", 8),
          ("extraverbose", 9),
          ("off", 100))
    )



class VenturiThresholdLevels(TextualConvention, Integer32):
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
        *(("off", 0),
          ("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warn", 5),
          ("notice", 6),
          ("info", 7),
          ("verbose", 8),
          ("extraverbose", 9))
    )



class VenturiTrapType(TextualConvention, Integer32):
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
        *(("v1Trap", 1),
          ("v2Trap", 2),
          ("v2Inform", 3))
    )



class VenturiTrapSeverity(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("informational", 5))
    )



class VenturiFTPDeliveryPeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              30,
              60,
              120,
              180,
              240)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 15),
          ("thirtyMin", 30),
          ("oneHour", 60),
          ("twoHour", 120),
          ("threeHour", 180),
          ("fourHour", 240))
    )



class VenturiContentRecognitionProtocol(TextualConvention, Integer32):
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
        *(("ftp", 1),
          ("http", 2),
          ("email", 3))
    )



class VenturiPFMode(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("pfCache", 2),
          ("pfProxy", 3))
    )



class VenturiCacheMode(TextualConvention, Integer32):
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
        *(("internal", 1),
          ("external", 2),
          ("nocache", 3))
    )



class VenturiCacheType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("parent", 1),
          ("sibling", 2))
    )



class VenturiClientAuthorization(TextualConvention, Integer32):
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
        *(("radius", 1),
          ("sourceIP", 2),
          ("none", 3))
    )



class VenturiSyslogFacilityType(TextualConvention, Integer32):
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
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )



class VenturiUpgradeStatus(TextualConvention, Integer32):
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
        *(("none", 1),
          ("downloading", 2),
          ("crcError", 3),
          ("ok", 4))
    )



class VenturiBlockingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )



class VenturiPercentageValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ten", 10),
          ("fifteen", 15),
          ("twenty", 20),
          ("twentyfive", 25),
          ("thirty", 30),
          ("thirtyfive", 35),
          ("forty", 40),
          ("fortyfive", 45),
          ("fifty", 50),
          ("fiftyfive", 55),
          ("sixty", 60),
          ("sixtyfive", 65),
          ("seventy", 70),
          ("seventyfive", 75),
          ("eighty", 80),
          ("eightyfive", 85),
          ("ninety", 90),
          ("ninetyfive", 95),
          ("hundred", 100))
    )



class VenturiIfConfig(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonforwarding", 1),
          ("forwarding", 2))
    )



class VenturiTransportType(TextualConvention, Integer32):
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
        *(("transportNone", 1),
          ("transportProxy", 2),
          ("transportCache", 3),
          ("transportRtspProxy", 4),
          ("transportDirectTCP", 5))
    )



class VenturiLogModuleType(TextualConvention, Integer32):
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("lmvos", 1),
          ("lmvtp", 2),
          ("lmvap", 3),
          ("lmvcp", 4),
          ("lmdb", 5),
          ("lmpostq", 6),
          ("lmbox", 7),
          ("lmlog", 8),
          ("lmsnmp", 9),
          ("lmcache", 10),
          ("lmndb", 11),
          ("lmbmc", 12),
          ("lmdiag", 13),
          ("lmauth", 14),
          ("lmstats", 15),
          ("lmsmp", 16),
          ("lmcrypto", 17),
          ("lmuiweb", 18),
          ("lmtrans", 19),
          ("lmhttpsproxy", 20),
          ("lmradius", 21),
          ("lmvrtsp", 22),
          ("lmstaging", 23),
          ("lmcli", 24))
    )



class VenturiHexUnsigned32(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VENTURI-TC",
    **{"VenturiProtocolType": VenturiProtocolType,
       "VenturiSubscriberType": VenturiSubscriberType,
       "VenturiConditionState": VenturiConditionState,
       "VenturiBooleanType": VenturiBooleanType,
       "VenturiConditionType": VenturiConditionType,
       "VenturiPhysicalIfMode": VenturiPhysicalIfMode,
       "VenturiLogicalIfMode": VenturiLogicalIfMode,
       "VenturiLicenseName": VenturiLicenseName,
       "VenturiLevel": VenturiLevel,
       "VenturiImageColorType": VenturiImageColorType,
       "VenturiImageColorValue": VenturiImageColorValue,
       "VenturiLogLevels": VenturiLogLevels,
       "VenturiThresholdLevels": VenturiThresholdLevels,
       "VenturiTrapType": VenturiTrapType,
       "VenturiTrapSeverity": VenturiTrapSeverity,
       "VenturiFTPDeliveryPeriod": VenturiFTPDeliveryPeriod,
       "VenturiContentRecognitionProtocol": VenturiContentRecognitionProtocol,
       "VenturiPFMode": VenturiPFMode,
       "VenturiCacheMode": VenturiCacheMode,
       "VenturiCacheType": VenturiCacheType,
       "VenturiClientAuthorization": VenturiClientAuthorization,
       "VenturiSyslogFacilityType": VenturiSyslogFacilityType,
       "VenturiUpgradeStatus": VenturiUpgradeStatus,
       "VenturiBlockingType": VenturiBlockingType,
       "VenturiPercentageValue": VenturiPercentageValue,
       "VenturiIfConfig": VenturiIfConfig,
       "VenturiTransportType": VenturiTransportType,
       "VenturiLogModuleType": VenturiLogModuleType,
       "VenturiHexUnsigned32": VenturiHexUnsigned32}
)
