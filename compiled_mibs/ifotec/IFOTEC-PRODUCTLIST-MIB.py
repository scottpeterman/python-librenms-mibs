# SNMP MIB module (IFOTEC-PRODUCTLIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ifotec\IFOTEC-PRODUCTLIST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:26 2025
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

(ifotec,) = mibBuilder.importSymbols(
    "IFOTEC-SMI",
    "ifotec")

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

ifotecProductList = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfotecEthernetProducts_ObjectIdentity = ObjectIdentity
ifotecEthernetProducts = _IfotecEthernetProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1)
)
_IfotecL2ManagedSwitches_ObjectIdentity = ObjectIdentity
ifotecL2ManagedSwitches = _IfotecL2ManagedSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1, 4)
)
_IfotecINETFamilly_ObjectIdentity = ObjectIdentity
ifotecINETFamilly = _IfotecINETFamilly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3)
)
_INET_2GE2GF_AS_101_ObjectIdentity = ObjectIdentity
INET_2GE2GF_AS_101 = _INET_2GE2GF_AS_101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 1)
)
_INET_2GP2GF_AS_101_ObjectIdentity = ObjectIdentity
INET_2GP2GF_AS_101 = _INET_2GP2GF_AS_101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 2)
)
_INET_4GE2GF_KS_001_ObjectIdentity = ObjectIdentity
INET_4GE2GF_KS_001 = _INET_4GE2GF_KS_001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 3)
)
_INET_4GP2GF_AS_001_ObjectIdentity = ObjectIdentity
INET_4GP2GF_AS_001 = _INET_4GP2GF_AS_001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 4)
)
_INET_4GE2GF2XF_R1_001_ObjectIdentity = ObjectIdentity
INET_4GE2GF2XF_R1_001 = _INET_4GE2GF2XF_R1_001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IFOTEC-PRODUCTLIST-MIB",
    **{"ifotecProductList": ifotecProductList,
       "ifotecEthernetProducts": ifotecEthernetProducts,
       "ifotecL2ManagedSwitches": ifotecL2ManagedSwitches,
       "ifotecINETFamilly": ifotecINETFamilly,
       "INET-2GE2GF-AS-101": INET_2GE2GF_AS_101,
       "INET-2GP2GF-AS-101": INET_2GP2GF_AS_101,
       "INET-4GE2GF-KS-001": INET_4GE2GF_KS_001,
       "INET-4GP2GF-AS-001": INET_4GP2GF_AS_001,
       "INET-4GE2GF2XF-R1-001": INET_4GE2GF2XF_R1_001}
)
