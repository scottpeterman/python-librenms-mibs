# SNMP MIB module (CISCO-LWAPP-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-LWAPP-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:26:51 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoLwappTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 514)
)
if mibBuilder.loadTexts:
    ciscoLwappTextualConventions.setRevisions(
        ("2022-11-29 00:00",
         "2016-08-23 00:00",
         "2016-08-23 00:00",
         "2011-09-13 00:00",
         "2010-02-23 00:00",
         "2007-09-11 00:00",
         "2007-02-05 00:00",
         "2006-10-31 00:00",
         "2006-04-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CLApIfType(TextualConvention, Integer32):
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
        *(("dot11bg", 1),
          ("dot11a", 2),
          ("uwb", 3),
          ("dot11abgn", 4),
          ("rlan", 5),
          ("dot11-6ghz", 6),
          ("dot11-xor-5-6ghz", 7))
    )



class CLDot11Channel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
    )



class CLDot11ClientStatus(TextualConvention, Integer32):
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
        *(("idle", 1),
          ("aaaPending", 2),
          ("authenticated", 3),
          ("associated", 4),
          ("powersave", 5),
          ("disassociated", 6),
          ("tobedeleted", 7),
          ("probing", 8),
          ("excluded", 9))
    )



class CLEventFrames(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cLAssocRequestFrm", 0),
          ("cLAssocResponseFrm", 1),
          ("cLReAssocRequestFrm", 2),
          ("cLReAssocResponseFrm", 3),
          ("cLProbeRequestFrm", 4),
          ("cLProbeResponseFrm", 5),
          ("cLReserved1", 6),
          ("cLReserved2", 7),
          ("cLBeaconFrm", 8),
          ("cLAtimFrm", 9),
          ("cLDissociationFrm", 10),
          ("cLAuthenticationFrm", 11),
          ("cLDeAuthenticationFrm", 12))
    )


class CLMfpEventType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16,
              17,
              19,
              20,
              21,
              22,
              23,
              24,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("invalidMic", 1),
          ("invalidSeq", 2),
          ("noMic", 3),
          ("unexpectedMic", 4),
          ("ccmpNoEncryptError", 16),
          ("ccmpDecryptError", 17),
          ("ccmpInvalidReplayCtr", 19),
          ("tkipNoEncryptError", 20),
          ("tkipInvalidIcv", 21),
          ("tkipInvalidMic", 22),
          ("tkipInvalidMhdrIe", 23),
          ("tkipInvalidReplayCtr", 24),
          ("bcastDisassociationFrameRcvd", 32),
          ("bcastDeauthenticationFrameRcvd", 33),
          ("bcastActionFrameRcvd", 34))
    )



class CLMfpEventSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("infrastructureMfp", 1),
          ("clientMfp", 2))
    )



class CLMfpVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mfpv1", 1),
          ("mfpv2", 2))
    )



class CLTimeBaseStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cTimeBaseInSync", 1),
          ("cTimeBaseNotInSync", 2))
    )



class CLSecEncryptType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tkip", 0),
          ("aes", 1))
    )


class CLSecKeyFormat(TextualConvention, Integer32):
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
        *(("default", 1),
          ("hex", 2),
          ("ascii", 3))
    )



class CLDot11RfParamMode(TextualConvention, Integer32):
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
        *(("default", 1),
          ("custom", 2),
          ("auto", 3))
    )



class CLTsmDot11CurrentPackets(TextualConvention, Gauge32):
    status = "current"


class CLCdpAdvtVersionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdpv1", 1),
          ("cdpv2", 2))
    )



class CLDot11ChannelBandwidth(TextualConvention, Integer32):
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("aboveforty", 4),
          ("belowforty", 5))
    )



class CLDot11Band(TextualConvention, Integer32):
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
        *(("band2dot4", 1),
          ("band5", 2),
          ("maui-6ghz", 3))
    )



class CLApAssocFailureReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notSupported", 2))
    )



class CLWebAuthType(TextualConvention, Integer32):
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
        *(("internalDefault", 1),
          ("internalCustom", 2),
          ("external", 3))
    )



class CLClientPowerSaveMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )



class CLApDot11RadioSubband(TextualConvention, Integer32):
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
        *(("all", 1),
          ("sub49", 2),
          ("sub52", 3),
          ("sub54", 4),
          ("sub58", 5))
    )



class CLApDot11RadioRole(TextualConvention, Integer32):
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
        *(("shutdown", 0),
          ("upDownlink", 1),
          ("uplink", 2),
          ("downlink", 3),
          ("access", 4),
          ("uplinkAccess", 5),
          ("downlinkAccess", 6),
          ("upDownlinkAccess", 7),
          ("unknown", 8))
    )



class CcxServiceVersion(TextualConvention, Integer32):
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
        *(("none", 1),
          ("version1", 2),
          ("version2", 3))
    )



class CLApMode(TextualConvention, Integer32):
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
        *(("local", 0),
          ("monitor", 1),
          ("remote", 2),
          ("rogueDetector", 3),
          ("sniffer", 4),
          ("bridge", 5),
          ("seConnect", 6),
          ("remoteBridge", 7),
          ("remoteHybrid", 8),
          ("sensor", 9))
    )



class Dscp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class CLApNtpStatus(TextualConvention, Integer32):
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
        *(("notValid", 1),
          ("none", 2),
          ("unreachable", 3),
          ("synched", 4),
          ("notSynched", 5),
          ("waitSynch", 6),
          ("authFail", 7),
          ("notSuitable", 8),
          ("unknown", 9))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-TC-MIB",
    **{"CLApIfType": CLApIfType,
       "CLDot11Channel": CLDot11Channel,
       "CLDot11ClientStatus": CLDot11ClientStatus,
       "CLEventFrames": CLEventFrames,
       "CLMfpEventType": CLMfpEventType,
       "CLMfpEventSource": CLMfpEventSource,
       "CLMfpVersion": CLMfpVersion,
       "CLTimeBaseStatus": CLTimeBaseStatus,
       "CLSecEncryptType": CLSecEncryptType,
       "CLSecKeyFormat": CLSecKeyFormat,
       "CLDot11RfParamMode": CLDot11RfParamMode,
       "CLTsmDot11CurrentPackets": CLTsmDot11CurrentPackets,
       "CLCdpAdvtVersionType": CLCdpAdvtVersionType,
       "CLDot11ChannelBandwidth": CLDot11ChannelBandwidth,
       "CLDot11Band": CLDot11Band,
       "CLApAssocFailureReason": CLApAssocFailureReason,
       "CLWebAuthType": CLWebAuthType,
       "CLClientPowerSaveMode": CLClientPowerSaveMode,
       "CLApDot11RadioSubband": CLApDot11RadioSubband,
       "CLApDot11RadioRole": CLApDot11RadioRole,
       "CcxServiceVersion": CcxServiceVersion,
       "CLApMode": CLApMode,
       "Dscp": Dscp,
       "CLApNtpStatus": CLApNtpStatus,
       "ciscoLwappTextualConventions": ciscoLwappTextualConventions}
)
