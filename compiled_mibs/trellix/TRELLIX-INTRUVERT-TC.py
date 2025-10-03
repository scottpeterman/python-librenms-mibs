# SNMP MIB module (TRELLIX-INTRUVERT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\trellix\TRELLIX-INTRUVERT-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:47 2025
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

(ivConventions,) = mibBuilder.importSymbols(
    "TRELLIX-INTRUVERT-SMI",
    "ivConventions")


# MODULE-IDENTITY

ivTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrellixEventCategory(TextualConvention, Integer32):
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
        *(("other", 0),
          ("equipment", 1),
          ("commnunication", 2),
          ("qos", 3),
          ("environment", 4),
          ("application", 5))
    )



class TrellixEventSeverity(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("inform", 1),
          ("clear", 2),
          ("warning", 3),
          ("error", 4),
          ("critical", 5))
    )



class TrellixFEType(TextualConvention, Integer32):
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
        *(("other", 0),
          ("ten-Mbps", 1),
          ("hundred-Mbps", 2),
          ("auto-negotiate", 3))
    )



class TrellixGEType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("one-gbps", 2),
          ("auto-negotiate", 3))
    )



class TrellixIDSAction(TextualConvention, Integer32):
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
        *(("other", 0),
          ("enable", 1),
          ("disable", 2),
          ("reset", 3),
          ("sigupdate", 4),
          ("swupdate", 5),
          ("sensordown", 6),
          ("certupdate", 7),
          ("hitlessreboot", 8))
    )



class TrellixIDSActionResult(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TrellixIDSActionStatus(TextualConvention, Integer32):
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
        *(("failed", 0),
          ("succeeded", 1),
          ("sigupdated", 2),
          ("enabled", 3),
          ("disabled", 4))
    )



class TrellixIDSCardType(TextualConvention, Integer32):
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
        *(("other", 0),
          ("mgmt", 1),
          ("sensor", 2))
    )



class TrellixIDSOperatingMode(TextualConvention, Integer32):
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
        *(("inline-fail-open-passive", 1),
          ("monitor-dual-intf", 2),
          ("monitor-single-intf", 3),
          ("inline-fail-close", 4),
          ("inline-fail-open-active", 5))
    )



class TrellixIDSPortType(TextualConvention, Integer32):
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
        *(("other", 0),
          ("gigabitEthernet", 1),
          ("fastEthernet", 2),
          ("copperGigabitEthernet", 3),
          ("tenGigabitEthernet", 4),
          ("fortyGigabitEthernet", 5),
          ("vnic", 6))
    )



class TrellixIDSResponseMode(TextualConvention, Integer32):
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
        *(("interace-port", 0),
          ("response-port", 1),
          ("management-port", 2))
    )



class TrellixProductType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ids", 0)
    )



class TrellixTFTPAction(TextualConvention, Integer32):
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
              25,
              28,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("download-image", 1),
          ("download-signature", 2),
          ("upload-dos", 3),
          ("upload-trace", 4),
          ("download-dos", 5),
          ("abort-transfer", 6),
          ("download-sslcert", 7),
          ("download-image-and-signature", 8),
          ("download-mpecert", 9),
          ("download-sgap-ssl-cert", 10),
          ("upload-sgap-ssl-csr", 11),
          ("upload-ibac-ad-file", 12),
          ("download-ibac-ad-file", 13),
          ("upload-sw-tlv-file", 14),
          ("download-PacketCaptureFilter-file", 15),
          ("upload-PacketCaptureFilter-file", 16),
          ("download-geolocation-db-file", 17),
          ("upload-PacketCapturePCAP-file", 18),
          ("download-usrid-acl-file", 19),
          ("download-bot-dat-file", 20),
          ("download-ntba-ssl-cert-file", 21),
          ("upload-dev-prof-file", 22),
          ("download-matd-ssl-cert-file", 25),
          ("download-ffp-bulk-update", 28),
          ("download-zcenter-ssl-cert", 33),
          ("download-gti-pc-ssl-cert", 34),
          ("upload-suricata-failed-rules-file", 35),
          ("upload-ca-sensor-csr", 36),
          ("download-ca-sensor-cert", 37),
          ("download-syslog-ssl-cert", 38))
    )



class TrellixTFTPFailedResult(TextualConvention, Integer32):
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
              53,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("invalidFileName", 1),
          ("invalidFileType", 2),
          ("cannotReachServer", 3),
          ("noResponseFromServer", 4),
          ("insufficientDiskSpace", 5),
          ("decryptionError", 6),
          ("accessViolation", 7),
          ("fileAlreadyExists", 8),
          ("channelOutOfSync", 9),
          ("sensorNotInitialized", 10),
          ("realtimeUpdateError", 11),
          ("sigfile1OpenError", 12),
          ("sigfile1StatError", 13),
          ("sigfile1MemoryError", 14),
          ("sigfile1ReadError", 15),
          ("sigfile1NullError", 16),
          ("sigfile1MD5Error", 17),
          ("sigfile1InsufficientSpaceForTotalRules", 18),
          ("sigfile1ConvertError", 19),
          ("sigfile1SplitError", 20),
          ("sigfile2OpenError", 21),
          ("sigfile2StatError", 22),
          ("sigfile2MemoryError", 23),
          ("sigfile2ReadError", 24),
          ("sigfile2NullError", 25),
          ("sigfile2MD5Error", 26),
          ("sigfile2InsufficientSpaceForTotalRules", 27),
          ("sigfile2ConvertError", 28),
          ("sigfile2SplitError", 29),
          ("initIDConvertTablesError", 30),
          ("sigfileMarkError", 31),
          ("sigfileUndoMarkError", 32),
          ("compareSigfilesError", 33),
          ("updateBaseSigfileError", 34),
          ("sensorRebootRequired", 35),
          ("fileParseError", 36),
          ("sigfile1FormatVersionError", 37),
          ("sigfile2FormatVersionError", 38),
          ("fileDoesNotExists", 39),
          ("outOfMemoryError", 40),
          ("transferAborted", 41),
          ("internalApplyError", 42),
          ("incrSigfileUnspportedError", 53),
          ("incrSigfileFormatError", 61),
          ("incrSigfileHasSigsetMismatchError", 62),
          ("incrSigfileMergeError", 63))
    )



class TrellixTFTPFileType(TextualConvention, Integer32):
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
        *(("other", 0),
          ("image", 1),
          ("signature", 2),
          ("trace", 3),
          ("dos", 4),
          ("configuration", 5),
          ("sslcert", 6),
          ("image-and-signature", 7),
          ("mpecert", 8))
    )



class TrellixTFTPInProgressResult(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TrellixTFTPStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              11,
              12,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("failed", 1),
          ("inProgress", 2),
          ("succeeded", 3),
          ("dwnldFailed", 11),
          ("applyFailed", 12),
          ("dwnlding", 21),
          ("dwnldingComplete", 22),
          ("applying", 23),
          ("applyingComplete", 24))
    )



class TrellixCUGEType(TextualConvention, Integer32):
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
        *(("other", 0),
          ("ten-Mbps", 1),
          ("hundred-Mbps", 2),
          ("auto-negotiate", 3),
          ("one-gbps", 4))
    )



class TrellixPortSpeed(TextualConvention, Integer32):
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
        *(("other", 0),
          ("fixed-ten-Mbps", 1),
          ("fixed-hundred-Mbps", 2),
          ("auto-negotiate-down-hundred-Mbps", 3),
          ("fixed-one-Gbps", 4),
          ("fixed-ten-Gbps", 5),
          ("auto-negotiate-ten-Mbps", 6),
          ("auto-negotiate-hundred-Mbps", 7),
          ("auto-negotiate-one-Gbps", 8),
          ("auto-negotiate-ten-Gbps", 9),
          ("auto-negotiate-down-one-Gbps", 10),
          ("fixed-forty-Gbps", 11))
    )



class TrellixPluggableModuleType(TextualConvention, Integer32):
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
        *(("other", 0),
          ("pluggable-module-qsfp", 1),
          ("pluggable-module-sfp-plus", 2),
          ("pluggable-module-qsfp-4", 3),
          ("pluggable-module-sfp-plus-12", 4),
          ("pluggable-module-rj45-6", 5),
          ("pluggable-module-sfp-plus-pfo-4-sm", 6),
          ("pluggable-module-sfp-plus-pfo-4-mm-50um", 7),
          ("pluggable-module-sfp-plus-pfo-4-mm-62-5um", 8),
          ("fixed-ports-sfp-12", 9),
          ("pluggable-module-rj45-4", 10))
    )



class TrellixPortLinearIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRELLIX-INTRUVERT-TC",
    **{"TrellixEventCategory": TrellixEventCategory,
       "TrellixEventSeverity": TrellixEventSeverity,
       "TrellixFEType": TrellixFEType,
       "TrellixGEType": TrellixGEType,
       "TrellixIDSAction": TrellixIDSAction,
       "TrellixIDSActionResult": TrellixIDSActionResult,
       "TrellixIDSActionStatus": TrellixIDSActionStatus,
       "TrellixIDSCardType": TrellixIDSCardType,
       "TrellixIDSOperatingMode": TrellixIDSOperatingMode,
       "TrellixIDSPortType": TrellixIDSPortType,
       "TrellixIDSResponseMode": TrellixIDSResponseMode,
       "TrellixProductType": TrellixProductType,
       "TrellixTFTPAction": TrellixTFTPAction,
       "TrellixTFTPFailedResult": TrellixTFTPFailedResult,
       "TrellixTFTPFileType": TrellixTFTPFileType,
       "TrellixTFTPInProgressResult": TrellixTFTPInProgressResult,
       "TrellixTFTPStatus": TrellixTFTPStatus,
       "TrellixCUGEType": TrellixCUGEType,
       "TrellixPortSpeed": TrellixPortSpeed,
       "TrellixPluggableModuleType": TrellixPluggableModuleType,
       "TrellixPortLinearIndex": TrellixPortLinearIndex,
       "ivTextualConventions": ivTextualConventions}
)
