# SNMP MIB module (TAIT-TN9300-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tait\TAIT-TN9300-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:38 2025
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

(taitModules,) = mibBuilder.importSymbols(
    "TAIT-COMMON-MIB",
    "taitModules")


# MODULE-IDENTITY

taittn9300TC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    taittn9300TC.setRevisions(
        ("2018-12-04 12:00",
         "2018-07-17 10:05",
         "2018-03-18 22:03",
         "2017-03-16 01:23",
         "2016-08-22 12:00",
         "2015-10-30 12:00",
         "2015-03-17 22:08",
         "2012-06-27 09:02",
         "2012-05-28 23:17")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeRequestedState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("offline", 1),
          ("program", 2),
          ("online", 3))
    )



class NodeState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("offline", 1),
          ("program", 2),
          ("switching", 3),
          ("control", 4))
    )



class NetworkCheckState(TextualConvention, Integer32):
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
        *(("notConfigured", 0),
          ("ok", 1),
          ("failed", 2))
    )



class ChannelState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("disabled", 1),
          ("idle", 2),
          ("control", 3),
          ("traffic", 4),
          ("data", 5),
          ("failed", 6))
    )



class SipLineRegistrationType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("inbound", 1),
          ("outbound", 2),
          ("ais", 3))
    )



class SipLineIncomingType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("pstni", 1),
          ("pabxi", 2))
    )



class SipCallSpeechVotingPriority(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("normal", 1),
          ("override", 2))
    )



class SipLineState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("disabled", 1),
          ("up", 2),
          ("down", 3))
    )



class DipLineState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("unconfigured", 1),
          ("idle", 2),
          ("active", 3),
          ("failed", 4))
    )



class NgwLinkState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ok", 1),
          ("failed", 2))
    )



class Mpt1327LinkState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ok", 1),
          ("failed", 2))
    )



class Mpt1327ChannelState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("idle", 1),
          ("traffic", 2),
          ("control", 3),
          ("failed", 4))
    )



class RemoteNodeState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("offline", 1),
          ("program", 2),
          ("switching", 3),
          ("control", 4),
          ("failed", 5),
          ("gracefulShutdown", 6))
    )



class UnitStatusMessageId(TextualConvention, Integer32):
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
              128)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 0),
          ("pppLinkToMpcDown", 1),
          ("gpsSignalLost", 2),
          ("gpsSignalRegainedAfterLoss", 3),
          ("terminalAntennaConnectionFailureVswrOutOfRange", 4),
          ("terminalSupplyVoltageOutOfRange", 5),
          ("radioTemperatureT0NormalRange", 6),
          ("radioTemperatureT1OverTemp", 7),
          ("radioTemperatureT2OverTemp", 8),
          ("radioTemperatureT3OverTemp", 9),
          ("terminalLossOfService", 10),
          ("radioFrequencyOutOfLockServiceRegained", 11),
          ("mcpConfigurationError", 12),
          ("terminalAntennaConnectionGood", 13),
          ("terminalUnsolicitedReset", 14),
          ("terminalGainedService", 15),
          ("unknown", 128))
    )



class EventSeverity(TextualConvention, Integer32):
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
        *(("ok", 0),
          ("minor", 1),
          ("major", 2))
    )



class LicenseValidity(TextualConvention, Integer32):
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
        *(("valid", 0),
          ("fileNotFound", 1),
          ("invalidHostId", 2),
          ("invalidProductCode", 3),
          ("invalidVersion", 4),
          ("invalidExpiryDate", 5),
          ("expired", 6),
          ("corruptSignature", 7),
          ("conflictingFeatures", 8),
          ("invalidTierMode", 9),
          ("invalidLicenseFormat", 10))
    )



class UnitAuthentication(TextualConvention, Integer32):
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
        *(("notPolled", 0),
          ("polling", 1),
          ("notHome", 2),
          ("busy", 3),
          ("badAuthentication", 4),
          ("badCrcReceived", 5),
          ("goodAuthenticationReceived", 6),
          ("rejected", 7),
          ("notRegistered", 8))
    )



class RemoteNodeSyncState(TextualConvention, Integer32):
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
        *(("ok", 0),
          ("failed", 1),
          ("unknown", 2),
          ("none", 3))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAIT-TN9300-TC",
    **{"NodeRequestedState": NodeRequestedState,
       "NodeState": NodeState,
       "NetworkCheckState": NetworkCheckState,
       "ChannelState": ChannelState,
       "SipLineRegistrationType": SipLineRegistrationType,
       "SipLineIncomingType": SipLineIncomingType,
       "SipCallSpeechVotingPriority": SipCallSpeechVotingPriority,
       "SipLineState": SipLineState,
       "DipLineState": DipLineState,
       "NgwLinkState": NgwLinkState,
       "Mpt1327LinkState": Mpt1327LinkState,
       "Mpt1327ChannelState": Mpt1327ChannelState,
       "RemoteNodeState": RemoteNodeState,
       "UnitStatusMessageId": UnitStatusMessageId,
       "EventSeverity": EventSeverity,
       "LicenseValidity": LicenseValidity,
       "UnitAuthentication": UnitAuthentication,
       "RemoteNodeSyncState": RemoteNodeSyncState,
       "taittn9300TC": taittn9300TC}
)
