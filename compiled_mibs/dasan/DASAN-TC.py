# SNMP MIB module (DASAN-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:53 2025
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

(dasanModules,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanModules")

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

dasanTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 12, 1)
)
if mibBuilder.loadTexts:
    dasanTextualConventions.setRevisions(
        ("2001-04-19 00:00",
         "2000-11-21 00:00",
         "1998-10-28 00:00",
         "1997-03-13 00:00",
         "1997-03-13 00:00",
         "1996-08-14 00:00",
         "1996-07-08 00:00",
         "1996-02-22 00:00",
         "1995-06-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DasanNetworkProtocol(TextualConvention, Integer32):
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
          ("unknown", 65535))
    )



class DasanNetworkAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"


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



class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class DasanRowOperStatus(TextualConvention, Integer32):
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



class DasanPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DasanIpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class DasanLocationClass(TextualConvention, Integer32):
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



class DasanLocationSpecifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class DasanInetAddressMask(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class DasanAbsZeroBasedCounter32(TextualConvention, Gauge32):
    status = "current"


class DasanSnapShotAbsCounter32(TextualConvention, Unsigned32):
    status = "current"


class DasanAlarmSeverity(TextualConvention, Integer32):
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



class ModuleIndex(TextualConvention, Integer32):
    status = "current"


class PortIndex(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-TC",
    **{"DasanNetworkProtocol": DasanNetworkProtocol,
       "DasanNetworkAddress": DasanNetworkAddress,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SAPType": SAPType,
       "CountryCode": CountryCode,
       "EntPhysicalIndexOrZero": EntPhysicalIndexOrZero,
       "DasanRowOperStatus": DasanRowOperStatus,
       "DasanPort": DasanPort,
       "DasanIpProtocol": DasanIpProtocol,
       "DasanLocationClass": DasanLocationClass,
       "DasanLocationSpecifier": DasanLocationSpecifier,
       "DasanInetAddressMask": DasanInetAddressMask,
       "DasanAbsZeroBasedCounter32": DasanAbsZeroBasedCounter32,
       "DasanSnapShotAbsCounter32": DasanSnapShotAbsCounter32,
       "DasanAlarmSeverity": DasanAlarmSeverity,
       "ModuleIndex": ModuleIndex,
       "PortIndex": PortIndex,
       "dasanTextualConventions": dasanTextualConventions}
)
