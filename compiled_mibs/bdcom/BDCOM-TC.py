# SNMP MIB module (BDCOM-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bdcom\BDCOM-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:51 2025
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

(bdcomModules,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdcomModules")

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

bdcomTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 12, 1)
)
if mibBuilder.loadTexts:
    bdcomTextualConventions.setRevisions(
        ("2003-10-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BDCOMNetworkProtocol(TextualConvention, Integer32):
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
              65535)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("decnet", 2),
          ("pup", 3),
          ("chaos", 4),
          ("xns", 5),
          ("x121", 6),
          ("appletalk", 7),
          ("clns", 8),
          ("lat", 9),
          ("vines", 10),
          ("cons", 11),
          ("apollo", 12),
          ("stun", 13),
          ("novell", 14),
          ("qllc", 15),
          ("snapshot", 16),
          ("atmIlmi", 17),
          ("bstun", 18),
          ("x25pvc", 19),
          ("ipv6", 20),
          ("cdm", 21),
          ("nbf", 22),
          ("bpxIgx", 23),
          ("clnsPfx", 24),
          ("http", 25),
          ("unknown", 65535))
    )



class BDCOMNetworkAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"


class Unsigned64(TextualConvention, Counter64):
    status = "current"


class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SAPType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )



class CountryCode(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )



class CountryCodeITU(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class BDCOMRowOperStatus(TextualConvention, Integer32):
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
          ("activeDependencies", 2),
          ("inactiveDependency", 3),
          ("missingDependency", 4))
    )



class BDCOMPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BDCOMIpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class BDCOMLocationClass(TextualConvention, Integer32):
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
        *(("chassis", 1),
          ("shelf", 2),
          ("slot", 3),
          ("subSlot", 4),
          ("port", 5),
          ("subPort", 6),
          ("channel", 7),
          ("subChannel", 8))
    )



class BDCOMLocationSpecifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class BDCOMInetAddressMask(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class BDCOMAbsZeroBasedCounter32(TextualConvention, Gauge32):
    status = "current"


class BDCOMSnapShotAbsCounter32(TextualConvention, Unsigned32):
    status = "current"


class BDCOMAlarmSeverity(TextualConvention, Integer32):
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("info", 7))
    )



class PerfHighIntervalCount(TextualConvention, Counter64):
    status = "current"


class ConfigIterator(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BulkConfigResult(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ListIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ListIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TimeIntervalSec(TextualConvention, Unsigned32):
    status = "current"


class TimeIntervalMin(TextualConvention, Unsigned32):
    status = "current"


class BDCOMMilliSeconds(TextualConvention, Unsigned32):
    status = "current"


class MicroSeconds(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-TC",
    **{"BDCOMNetworkProtocol": BDCOMNetworkProtocol,
       "BDCOMNetworkAddress": BDCOMNetworkAddress,
       "Unsigned64": Unsigned64,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SAPType": SAPType,
       "CountryCode": CountryCode,
       "CountryCodeITU": CountryCodeITU,
       "EntPhysicalIndexOrZero": EntPhysicalIndexOrZero,
       "BDCOMRowOperStatus": BDCOMRowOperStatus,
       "BDCOMPort": BDCOMPort,
       "BDCOMIpProtocol": BDCOMIpProtocol,
       "BDCOMLocationClass": BDCOMLocationClass,
       "BDCOMLocationSpecifier": BDCOMLocationSpecifier,
       "BDCOMInetAddressMask": BDCOMInetAddressMask,
       "BDCOMAbsZeroBasedCounter32": BDCOMAbsZeroBasedCounter32,
       "BDCOMSnapShotAbsCounter32": BDCOMSnapShotAbsCounter32,
       "BDCOMAlarmSeverity": BDCOMAlarmSeverity,
       "PerfHighIntervalCount": PerfHighIntervalCount,
       "ConfigIterator": ConfigIterator,
       "BulkConfigResult": BulkConfigResult,
       "ListIndex": ListIndex,
       "ListIndexOrZero": ListIndexOrZero,
       "TimeIntervalSec": TimeIntervalSec,
       "TimeIntervalMin": TimeIntervalMin,
       "BDCOMMilliSeconds": BDCOMMilliSeconds,
       "MicroSeconds": MicroSeconds,
       "bdcomTextualConventions": bdcomTextualConventions}
)
