# SNMP MIB module (LENOVO-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\lenovo\LENOVO-SMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:24 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lenovo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19046)
)
if mibBuilder.loadTexts:
    lenovo.setRevisions(
        ("2016-10-27 18:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LenovoProducts_ObjectIdentity = ObjectIdentity
lenovoProducts = _LenovoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1)
)
if mibBuilder.loadTexts:
    lenovoProducts.setStatus("current")
_LenovoNetworkMibs_ObjectIdentity = ObjectIdentity
lenovoNetworkMibs = _LenovoNetworkMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2)
)
if mibBuilder.loadTexts:
    lenovoNetworkMibs.setStatus("current")
_Network_mibs_ObjectIdentity = ObjectIdentity
network_mibs = _Network_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3)
)
if mibBuilder.loadTexts:
    network_mibs.setStatus("current")
_Tor_mibs_ObjectIdentity = ObjectIdentity
tor_mibs = _Tor_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 7)
)
if mibBuilder.loadTexts:
    tor_mibs.setStatus("current")
_Flex_mibs_ObjectIdentity = ObjectIdentity
flex_mibs = _Flex_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 18)
)
if mibBuilder.loadTexts:
    flex_mibs.setStatus("current")
_LenovoModules_ObjectIdentity = ObjectIdentity
lenovoModules = _LenovoModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 4)
)
if mibBuilder.loadTexts:
    lenovoModules.setStatus("current")
_LenovoServerMibs_ObjectIdentity = ObjectIdentity
lenovoServerMibs = _LenovoServerMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11)
)
if mibBuilder.loadTexts:
    lenovoServerMibs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LENOVO-SMI-MIB",
    **{"lenovo": lenovo,
       "lenovoProducts": lenovoProducts,
       "lenovoNetworkMibs": lenovoNetworkMibs,
       "network-mibs": network_mibs,
       "tor-mibs": tor_mibs,
       "flex-mibs": flex_mibs,
       "lenovoModules": lenovoModules,
       "lenovoServerMibs": lenovoServerMibs}
)
