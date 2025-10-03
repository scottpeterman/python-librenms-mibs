# SNMP MIB module (TRANSITION-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TRANSITION-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:43 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(tnModules,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnModules")


# MODULE-IDENTITY

transitionTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 5, 1)
)
if mibBuilder.loadTexts:
    transitionTC.setRevisions(
        ("2013-11-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CpsConnector(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
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
              38,
              40)
        )
    )
    namedValues = NamedValues(
        *(("rj45", 10),
          ("stmm", 11),
          ("stsm", 12),
          ("scmm", 13),
          ("scsm", 14),
          ("scsmlh", 15),
          ("scsmelh", 16),
          ("scsmlhlw", 17),
          ("mtrjmm", 18),
          ("lc", 19),
          ("bnc", 20),
          ("stsmlh", 21),
          ("stsmelh", 22),
          ("scmm1300", 23),
          ("stmm1300", 24),
          ("mtrjsm", 25),
          ("serial26", 26),
          ("stmmlh", 27),
          ("scsmsh", 28),
          ("scsimplex", 29),
          ("bncdual", 30),
          ("db9rsxxx", 31),
          ("termblock", 32),
          ("rj11", 33),
          ("sc40km", 34),
          ("sc125km", 35),
          ("din6", 38),
          ("sfp", 40))
    )



class TNEthernetSpeed(TextualConvention, Integer32):
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
        *(("mbps10", 1),
          ("mbps100", 2),
          ("gbps1", 3),
          ("gbps10", 4),
          ("mbps2500", 5),
          ("gbps5", 6),
          ("gbps12", 7))
    )



class TNEthernetDuplex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )



class TNEthernetAutoCross(TextualConvention, Integer32):
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
        *(("mdi", 1),
          ("mdiX", 2),
          ("autocross", 3),
          ("notApplicable", 4))
    )



class TNLoopbackModeCapBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("unused", 0),
          ("phyLayerLBCapable", 1),
          ("macLayerLBCapable", 2),
          ("alternateLBCapable", 3),
          ("remotePeerLBCapable", 4))
    )


class TNLoopbackModes(TextualConvention, Integer32):
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
        *(("noLoopback", 0),
          ("phyLayerLB", 1),
          ("macLayerLB", 2),
          ("alternateLB", 3),
          ("remotePeerLB", 4))
    )



class TNVlanIndexOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class TNEthPhyMode(TextualConvention, Integer32):
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
          ("phy10x100BaseT", 1),
          ("phy100BaseFX", 2),
          ("phy1000BaseX", 3),
          ("phy10x100x1000BaseT", 4),
          ("phySGMII", 5))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANSITION-TC",
    **{"CpsConnector": CpsConnector,
       "TNEthernetSpeed": TNEthernetSpeed,
       "TNEthernetDuplex": TNEthernetDuplex,
       "TNEthernetAutoCross": TNEthernetAutoCross,
       "TNLoopbackModeCapBits": TNLoopbackModeCapBits,
       "TNLoopbackModes": TNLoopbackModes,
       "TNVlanIndexOrZero": TNVlanIndexOrZero,
       "TNEthPhyMode": TNEthPhyMode,
       "transitionTC": transitionTC}
)
