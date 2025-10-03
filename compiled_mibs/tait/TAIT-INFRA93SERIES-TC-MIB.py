# SNMP MIB module (TAIT-INFRA93SERIES-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tait\TAIT-INFRA93SERIES-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:36 2025
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

(infra93_94TC,) = mibBuilder.importSymbols(
    "TAIT-INFRA93-94SERIES-TC-MIB",
    "infra93-94TC")


# MODULE-IDENTITY

infra93TC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    infra93TC.setRevisions(
        ("2019-05-29 00:26",
         "2018-05-22 00:26",
         "2017-07-28 00:00",
         "2016-11-18 00:00",
         "2016-07-01 00:00",
         "2014-10-30 15:00",
         "2014-04-14 00:00",
         "2014-01-26 00:00",
         "2014-01-14 11:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Ratio(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-256, 255),
    )



class LeveldBm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class SINADLevel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class Temperature(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class FrequencydHz(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class DcsCode(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "o"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class SubAudibleType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("ctcss", 1),
          ("dcs", 2))
    )



class TxFrequencyResponse(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pre-emph-speech", 1),
          ("flat-speech", 2))
    )



class RxFrequencyResponse(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("de-emph-speech", 1)
    )



class OperationalMode(TextualConvention, Integer32):
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
        *(("analogConventional", 1),
          ("dmrConventional", 2),
          ("dmrTrunking", 3),
          ("mptTrunking", 4))
    )



class MPTControlProtocolStatus(TextualConvention, Integer32):
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
        *(("unconnected", 0),
          ("idle", 1),
          ("control", 2),
          ("traffic", 3),
          ("conventional", 4))
    )



class FallbackNodeStatus(TextualConvention, Integer32):
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
        *(("active", 1),
          ("inactive", 2),
          ("settling", 3),
          ("disabled", 4))
    )



class ColourCode(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TransmitterSyncStatus(TextualConvention, Integer32):
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
        *(("no-license", 0),
          ("non-simulcast-operation", 1),
          ("frequency-reference-bad-or-absent", 2),
          ("never-had-1pps", 3),
          ("never-had-ntp", 4),
          ("missing-1pps-or-ntp", 5),
          ("synchronized", 6),
          ("non-channelgroup-operation", 7))
    )



class ReceiverSyncStatus(TextualConvention, Integer32):
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
        *(("no-license", 0),
          ("non-channelgroup-operation", 1),
          ("synchronized", 2),
          ("never-had-1pps", 3),
          ("never-had-ntp", 4),
          ("missing-1pps-or-ntp", 5))
    )



class ControlProtocolStatus(TextualConvention, Integer32):
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
        *(("unconnected", 0),
          ("deprecatedUnconnected", 1),
          ("standby", 2),
          ("dmrAligned", 3),
          ("dmrOffset", 4),
          ("dmr2SlotData", 5),
          ("dmrHibernate", 6),
          ("analogue", 7),
          ("testMode", 8),
          ("dmrTier2Aligned", 9))
    )



class LogicalChannelState(TextualConvention, Integer32):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("idle", 1),
          ("traffic", 2),
          ("control", 3),
          ("test", 4),
          ("poll", 5),
          ("invalid", 255))
    )



class StandaloneNodeStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("standby", 1),
          ("active", 2),
          ("disabled", 4),
          ("running", 5),
          ("master", 6))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAIT-INFRA93SERIES-TC-MIB",
    **{"Ratio": Ratio,
       "LeveldBm": LeveldBm,
       "SINADLevel": SINADLevel,
       "Temperature": Temperature,
       "FrequencydHz": FrequencydHz,
       "DcsCode": DcsCode,
       "SubAudibleType": SubAudibleType,
       "TxFrequencyResponse": TxFrequencyResponse,
       "RxFrequencyResponse": RxFrequencyResponse,
       "OperationalMode": OperationalMode,
       "MPTControlProtocolStatus": MPTControlProtocolStatus,
       "FallbackNodeStatus": FallbackNodeStatus,
       "ColourCode": ColourCode,
       "TransmitterSyncStatus": TransmitterSyncStatus,
       "ReceiverSyncStatus": ReceiverSyncStatus,
       "ControlProtocolStatus": ControlProtocolStatus,
       "LogicalChannelState": LogicalChannelState,
       "StandaloneNodeStatus": StandaloneNodeStatus,
       "infra93TC": infra93TC}
)
