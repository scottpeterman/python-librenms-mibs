# SNMP MIB module (TAIT-INFRA93-94SERIES-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tait\TAIT-INFRA93-94SERIES-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:34 2025
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

(infra93_94MibModule,) = mibBuilder.importSymbols(
    "TAIT-INFRA93-94SERIES-COMMON-MIB",
    "infra93-94MibModule")


# MODULE-IDENTITY

infra93_94TC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    infra93_94TC.setRevisions(
        ("2018-08-31 00:00",
         "2018-05-22 00:26",
         "2017-11-28 00:00",
         "2017-07-28 00:00",
         "2016-03-21 00:00",
         "2015-05-15 12:00",
         "2014-10-30 15:00",
         "2014-01-14 11:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BaseStationMode(TextualConvention, Integer32):
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
        *(("offline", 0),
          ("online", 1),
          ("unknown", 2))
    )



class Condition(TextualConvention, Integer32):
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
        *(("bad", 0),
          ("good", 1),
          ("notFitted", 2))
    )



class CurrentmA(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AlarmState(TextualConvention, Integer32):
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
        *(("unavailable", 0),
          ("cleared", 1),
          ("raised", 2),
          ("disabled", 3))
    )



class FrequencyHz(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-6"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class PowerW(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TransmitterStatus(TextualConvention, Integer32):
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
          ("unconfigured", 1),
          ("untuned", 2),
          ("idle", 3),
          ("transmitting", 4),
          ("calibrating", 5),
          ("fault", 6))
    )



class VoltageV(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class Milliseconds(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ChannelGroupStatus(TextualConvention, Integer32):
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
        *(("noLicense", 0),
          ("offline", 1),
          ("isolated", 2),
          ("satellite", 3),
          ("centralVoter", 4),
          ("singleBaseStation", 5),
          ("backupCentral", 6))
    )



class TimingControlType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("selfRegulating", 1))
    )



class GateState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )



class OptionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAIT-INFRA93-94SERIES-TC-MIB",
    **{"BaseStationMode": BaseStationMode,
       "Condition": Condition,
       "CurrentmA": CurrentmA,
       "AlarmState": AlarmState,
       "FrequencyHz": FrequencyHz,
       "PowerW": PowerW,
       "TransmitterStatus": TransmitterStatus,
       "VoltageV": VoltageV,
       "Milliseconds": Milliseconds,
       "ChannelGroupStatus": ChannelGroupStatus,
       "TimingControlType": TimingControlType,
       "GateState": GateState,
       "OptionState": OptionState,
       "infra93-94TC": infra93_94TC}
)
