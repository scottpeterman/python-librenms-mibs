# SNMP MIB module (IANA-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\IANA-PWE3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:31 2025
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

ianaPwe3MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 174)
)
if mibBuilder.loadTexts:
    ianaPwe3MIB.setRevisions(
        ("2009-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAPwTypeTC(TextualConvention, Integer32):
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
              32767)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("frameRelayDlciMartiniMode", 1),
          ("atmAal5SduVcc", 2),
          ("atmTransparent", 3),
          ("ethernetTagged", 4),
          ("ethernet", 5),
          ("hdlc", 6),
          ("ppp", 7),
          ("cem", 8),
          ("atmCellNto1Vcc", 9),
          ("atmCellNto1Vpc", 10),
          ("ipLayer2Transport", 11),
          ("atmCell1to1Vcc", 12),
          ("atmCell1to1Vpc", 13),
          ("atmAal5PduVcc", 14),
          ("frameRelayPortMode", 15),
          ("cep", 16),
          ("e1Satop", 17),
          ("t1Satop", 18),
          ("e3Satop", 19),
          ("t3Satop", 20),
          ("basicCesPsn", 21),
          ("basicTdmIp", 22),
          ("tdmCasCesPsn", 23),
          ("tdmCasTdmIp", 24),
          ("frDlci", 25),
          ("wildcard", 32767))
    )



class IANAPwPsnTypeTC(TextualConvention, Integer32):
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
        *(("mpls", 1),
          ("l2tp", 2),
          ("udpOverIp", 3),
          ("mplsOverIp", 4),
          ("mplsOverGre", 5),
          ("other", 6))
    )



class IANAPwCapabilities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pwStatusIndication", 0),
          ("pwVCCV", 1))
    )


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-PWE3-MIB",
    **{"IANAPwTypeTC": IANAPwTypeTC,
       "IANAPwPsnTypeTC": IANAPwPsnTypeTC,
       "IANAPwCapabilities": IANAPwCapabilities,
       "ianaPwe3MIB": ianaPwe3MIB}
)
