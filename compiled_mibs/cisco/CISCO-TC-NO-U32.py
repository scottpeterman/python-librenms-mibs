# SNMP MIB module (CISCO-TC-NO-U32) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-TC-NO-U32
# Produced by pysmi-1.6.2 at Thu Oct  2 11:27:37 2025
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

(ciscoModules,
 ciscoProducts) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules",
    "ciscoProducts")

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

ciscoTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 1)
)
if mibBuilder.loadTexts:
    ciscoTextualConventions.setRevisions(
        ("1997-03-13 00:00",
         "1997-03-13 00:00",
         "1996-08-14 00:00",
         "1996-07-08 00:00",
         "1995-06-07 00:00",
         "1998-10-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoNetworkProtocol(TextualConvention, Integer32):
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



class CiscoNetworkAddress(TextualConvention, OctetString):
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
    displayHint = "1x:"
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



class CiscoRowOperStatus(TextualConvention, Integer32):
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



class CiscoPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CiscoIpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TC-NO-U32",
    **{"CiscoNetworkProtocol": CiscoNetworkProtocol,
       "CiscoNetworkAddress": CiscoNetworkAddress,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SAPType": SAPType,
       "CountryCode": CountryCode,
       "EntPhysicalIndexOrZero": EntPhysicalIndexOrZero,
       "CiscoRowOperStatus": CiscoRowOperStatus,
       "CiscoPort": CiscoPort,
       "CiscoIpProtocol": CiscoIpProtocol,
       "ciscoTextualConventions": ciscoTextualConventions}
)
