# SNMP MIB module (IANA-ADDRESS-FAMILY-NUMBERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\IANA-ADDRESS-FAMILY-NUMBERS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:18 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianaAddressFamilyNumbers = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 72)
)
if mibBuilder.loadTexts:
    ianaAddressFamilyNumbers.setRevisions(
        ("2019-11-04 00:00",
         "2014-09-02 00:00",
         "2013-09-25 00:00",
         "2013-07-16 00:00",
         "2013-06-26 00:00",
         "2013-06-18 00:00",
         "2002-03-14 00:00",
         "2000-09-08 00:00",
         "2000-03-01 00:00",
         "2000-02-04 00:00",
         "1999-08-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AddressFamilyNumbers(TextualConvention, Integer32):
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
              16384,
              16385,
              16386,
              16387,
              16388,
              16389,
              16390,
              16391,
              16392,
              16393,
              16394,
              16395,
              16396,
              16397,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ipV4", 1),
          ("ipV6", 2),
          ("nsap", 3),
          ("hdlc", 4),
          ("bbn1822", 5),
          ("all802", 6),
          ("e163", 7),
          ("e164", 8),
          ("f69", 9),
          ("x121", 10),
          ("ipx", 11),
          ("appleTalk", 12),
          ("decnetIV", 13),
          ("banyanVines", 14),
          ("e164withNsap", 15),
          ("dns", 16),
          ("distinguishedName", 17),
          ("asNumber", 18),
          ("xtpOverIpv4", 19),
          ("xtpOverIpv6", 20),
          ("xtpNativeModeXTP", 21),
          ("fibreChannelWWPN", 22),
          ("fibreChannelWWNN", 23),
          ("gwid", 24),
          ("afi", 25),
          ("mplsTpSectionEndpointIdentifier", 26),
          ("mplsTpLspEndpointIdentifier", 27),
          ("mplsTpPseudowireEndpointIdentifier", 28),
          ("eigrpCommonServiceFamily", 16384),
          ("eigrpIpv4ServiceFamily", 16385),
          ("eigrpIpv6ServiceFamily", 16386),
          ("lispCanonicalAddressFormat", 16387),
          ("bgpLs", 16388),
          ("fortyeightBitMac", 16389),
          ("sixtyfourBitMac", 16390),
          ("oui", 16391),
          ("mac24", 16392),
          ("mac40", 16393),
          ("ipv664", 16394),
          ("rBridgePortID", 16395),
          ("trillNickname", 16396),
          ("universallyUniqueIdentifier", 16397),
          ("reserved", 65535))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    **{"AddressFamilyNumbers": AddressFamilyNumbers,
       "ianaAddressFamilyNumbers": ianaAddressFamilyNumbers}
)
