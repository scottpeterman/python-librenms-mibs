# SNMP MIB module (STONESOFT-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\forcepoint\STONESOFT-SMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:41 2025
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

stonesoftSmiMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 3, 2)
)
if mibBuilder.loadTexts:
    stonesoftSmiMibModule.setRevisions(
        ("2018-08-09 00:00",
         "2017-06-19 00:00",
         "2016-05-06 00:00",
         "2004-06-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stonesoft_ObjectIdentity = ObjectIdentity
stonesoft = _Stonesoft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369)
)
_StonesoftModules_ObjectIdentity = ObjectIdentity
stonesoftModules = _StonesoftModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 3)
)
_StonesoftExperimental_ObjectIdentity = ObjectIdentity
stonesoftExperimental = _StonesoftExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 4)
)
_StonesoftProducts_ObjectIdentity = ObjectIdentity
stonesoftProducts = _StonesoftProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5)
)
_StonesoftLoadBalancer_ObjectIdentity = ObjectIdentity
stonesoftLoadBalancer = _StonesoftLoadBalancer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 1)
)
_StonesoftFirewall_ObjectIdentity = ObjectIdentity
stonesoftFirewall = _StonesoftFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2)
)
_StonesoftVPN_ObjectIdentity = ObjectIdentity
stonesoftVPN = _StonesoftVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 3)
)
_StonesoftIDS_ObjectIdentity = ObjectIdentity
stonesoftIDS = _StonesoftIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 4)
)
_StonesoftIPS_ObjectIdentity = ObjectIdentity
stonesoftIPS = _StonesoftIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 5)
)
_StonesoftGeneric_ObjectIdentity = ObjectIdentity
stonesoftGeneric = _StonesoftGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6)
)
_StonesoftNetworkNode_ObjectIdentity = ObjectIdentity
stonesoftNetworkNode = _StonesoftNetworkNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 1)
)
_StonesoftCluster_ObjectIdentity = ObjectIdentity
stonesoftCluster = _StonesoftCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 2)
)
_StonesoftLogForwarding_ObjectIdentity = ObjectIdentity
stonesoftLogForwarding = _StonesoftLogForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 6, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STONESOFT-SMI-MIB",
    **{"stonesoft": stonesoft,
       "stonesoftModules": stonesoftModules,
       "stonesoftSmiMibModule": stonesoftSmiMibModule,
       "stonesoftExperimental": stonesoftExperimental,
       "stonesoftProducts": stonesoftProducts,
       "stonesoftLoadBalancer": stonesoftLoadBalancer,
       "stonesoftFirewall": stonesoftFirewall,
       "stonesoftVPN": stonesoftVPN,
       "stonesoftIDS": stonesoftIDS,
       "stonesoftIPS": stonesoftIPS,
       "stonesoftGeneric": stonesoftGeneric,
       "stonesoftNetworkNode": stonesoftNetworkNode,
       "stonesoftCluster": stonesoftCluster,
       "stonesoftLogForwarding": stonesoftLogForwarding}
)
