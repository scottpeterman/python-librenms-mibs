# SNMP MIB module (RUCKUS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-ROOT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:39 2025
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

ruckusRootMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusObjects_ObjectIdentity = ObjectIdentity
ruckusObjects = _RuckusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1)
)
_RuckusCommon_ObjectIdentity = ObjectIdentity
ruckusCommon = _RuckusCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1)
)
_RuckusCommonTCModule_ObjectIdentity = ObjectIdentity
ruckusCommonTCModule = _RuckusCommonTCModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1)
)
_RuckusCommonHwInfoModule_ObjectIdentity = ObjectIdentity
ruckusCommonHwInfoModule = _RuckusCommonHwInfoModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2)
)
_RuckusCommonSwInfoModule_ObjectIdentity = ObjectIdentity
ruckusCommonSwInfoModule = _RuckusCommonSwInfoModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3)
)
_RuckusCommonDeviceModule_ObjectIdentity = ObjectIdentity
ruckusCommonDeviceModule = _RuckusCommonDeviceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4)
)
_RuckusCommonUpgradeModule_ObjectIdentity = ObjectIdentity
ruckusCommonUpgradeModule = _RuckusCommonUpgradeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5)
)
_RuckusCommonWLANModule_ObjectIdentity = ObjectIdentity
ruckusCommonWLANModule = _RuckusCommonWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6)
)
_RuckusCommonDHCPModule_ObjectIdentity = ObjectIdentity
ruckusCommonDHCPModule = _RuckusCommonDHCPModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7)
)
_RuckusCommonPPPOEModule_ObjectIdentity = ObjectIdentity
ruckusCommonPPPOEModule = _RuckusCommonPPPOEModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8)
)
_RuckusCommonAdapterModule_ObjectIdentity = ObjectIdentity
ruckusCommonAdapterModule = _RuckusCommonAdapterModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9)
)
_RuckusCommonQosModule_ObjectIdentity = ObjectIdentity
ruckusCommonQosModule = _RuckusCommonQosModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 10)
)
_RuckusCommonSystemModule_ObjectIdentity = ObjectIdentity
ruckusCommonSystemModule = _RuckusCommonSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11)
)
_RuckusCommonRadioModule_ObjectIdentity = ObjectIdentity
ruckusCommonRadioModule = _RuckusCommonRadioModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12)
)
_RuckusCommonEthModule_ObjectIdentity = ObjectIdentity
ruckusCommonEthModule = _RuckusCommonEthModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13)
)
_RuckusCommonL2TPModule_ObjectIdentity = ObjectIdentity
ruckusCommonL2TPModule = _RuckusCommonL2TPModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14)
)
_RuckusCommonWLINKModule_ObjectIdentity = ObjectIdentity
ruckusCommonWLINKModule = _RuckusCommonWLINKModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15)
)
_RuckusZD_ObjectIdentity = ObjectIdentity
ruckusZD = _RuckusZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2)
)
_RuckusZDSystemModule_ObjectIdentity = ObjectIdentity
ruckusZDSystemModule = _RuckusZDSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1)
)
_RuckusZDWLANModule_ObjectIdentity = ObjectIdentity
ruckusZDWLANModule = _RuckusZDWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2)
)
_RuckusSCG_ObjectIdentity = ObjectIdentity
ruckusSCG = _RuckusSCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3)
)
_RuckusSCGSystemModule_ObjectIdentity = ObjectIdentity
ruckusSCGSystemModule = _RuckusSCGSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1)
)
_RuckusSCGWLANModule_ObjectIdentity = ObjectIdentity
ruckusSCGWLANModule = _RuckusSCGWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2)
)
_RuckusSCGTTGModule_ObjectIdentity = ObjectIdentity
ruckusSCGTTGModule = _RuckusSCGTTGModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3)
)
_RuckusSZ_ObjectIdentity = ObjectIdentity
ruckusSZ = _RuckusSZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4)
)
_RuckusSZSystemModule_ObjectIdentity = ObjectIdentity
ruckusSZSystemModule = _RuckusSZSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1)
)
_RuckusSZWLANModule_ObjectIdentity = ObjectIdentity
ruckusSZWLANModule = _RuckusSZWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2)
)
_RuckusCTRL_ObjectIdentity = ObjectIdentity
ruckusCTRL = _RuckusCTRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8)
)
_RuckusCTRLWLANModule_ObjectIdentity = ObjectIdentity
ruckusCTRLWLANModule = _RuckusCTRLWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 8, 1)
)
_RuckusUnleashed_ObjectIdentity = ObjectIdentity
ruckusUnleashed = _RuckusUnleashed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15)
)
_RuckusUnleashedSystemModule_ObjectIdentity = ObjectIdentity
ruckusUnleashedSystemModule = _RuckusUnleashedSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1)
)
_RuckusUnleashedWLANModule_ObjectIdentity = ObjectIdentity
ruckusUnleashedWLANModule = _RuckusUnleashedWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 2)
)
_RuckusEvents_ObjectIdentity = ObjectIdentity
ruckusEvents = _RuckusEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2)
)
_RuckusProducts_ObjectIdentity = ObjectIdentity
ruckusProducts = _RuckusProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ROOT-MIB",
    **{"ruckusRootMIB": ruckusRootMIB,
       "ruckusObjects": ruckusObjects,
       "ruckusCommon": ruckusCommon,
       "ruckusCommonTCModule": ruckusCommonTCModule,
       "ruckusCommonHwInfoModule": ruckusCommonHwInfoModule,
       "ruckusCommonSwInfoModule": ruckusCommonSwInfoModule,
       "ruckusCommonDeviceModule": ruckusCommonDeviceModule,
       "ruckusCommonUpgradeModule": ruckusCommonUpgradeModule,
       "ruckusCommonWLANModule": ruckusCommonWLANModule,
       "ruckusCommonDHCPModule": ruckusCommonDHCPModule,
       "ruckusCommonPPPOEModule": ruckusCommonPPPOEModule,
       "ruckusCommonAdapterModule": ruckusCommonAdapterModule,
       "ruckusCommonQosModule": ruckusCommonQosModule,
       "ruckusCommonSystemModule": ruckusCommonSystemModule,
       "ruckusCommonRadioModule": ruckusCommonRadioModule,
       "ruckusCommonEthModule": ruckusCommonEthModule,
       "ruckusCommonL2TPModule": ruckusCommonL2TPModule,
       "ruckusCommonWLINKModule": ruckusCommonWLINKModule,
       "ruckusZD": ruckusZD,
       "ruckusZDSystemModule": ruckusZDSystemModule,
       "ruckusZDWLANModule": ruckusZDWLANModule,
       "ruckusSCG": ruckusSCG,
       "ruckusSCGSystemModule": ruckusSCGSystemModule,
       "ruckusSCGWLANModule": ruckusSCGWLANModule,
       "ruckusSCGTTGModule": ruckusSCGTTGModule,
       "ruckusSZ": ruckusSZ,
       "ruckusSZSystemModule": ruckusSZSystemModule,
       "ruckusSZWLANModule": ruckusSZWLANModule,
       "ruckusCTRL": ruckusCTRL,
       "ruckusCTRLWLANModule": ruckusCTRLWLANModule,
       "ruckusUnleashed": ruckusUnleashed,
       "ruckusUnleashedSystemModule": ruckusUnleashedSystemModule,
       "ruckusUnleashedWLANModule": ruckusUnleashedWLANModule,
       "ruckusEvents": ruckusEvents,
       "ruckusProducts": ruckusProducts}
)
