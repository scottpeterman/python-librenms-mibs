# SNMP MIB module (VMWARE-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:16 2025
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

(vmwOID,
 vmwProductSpecific) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwOID",
    "vmwProductSpecific")


# MODULE-IDENTITY

vmwProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 11)
)
if mibBuilder.loadTexts:
    vmwProducts.setRevisions(
        ("2021-04-29 00:00",
         "2018-08-30 00:00",
         "2018-06-27 00:00",
         "2017-10-13 00:00",
         "2017-05-17 00:00",
         "2015-07-17 00:00",
         "2014-09-19 00:00",
         "2011-09-29 00:00",
         "2007-07-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwESX_ObjectIdentity = ObjectIdentity
vmwESX = _VmwESX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1)
)
_VmwDVS_ObjectIdentity = ObjectIdentity
vmwDVS = _VmwDVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 2)
)
_VmwVC_ObjectIdentity = ObjectIdentity
vmwVC = _VmwVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3)
)
_VmwServer_ObjectIdentity = ObjectIdentity
vmwServer = _VmwServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 4)
)
_VmwVCOps_ObjectIdentity = ObjectIdentity
vmwVCOps = _VmwVCOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5)
)
_VmwGenericAppliance_ObjectIdentity = ObjectIdentity
vmwGenericAppliance = _VmwGenericAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 6)
)
_VmwEmbeddedVirtualCenterAppliance_ObjectIdentity = ObjectIdentity
vmwEmbeddedVirtualCenterAppliance = _VmwEmbeddedVirtualCenterAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 7)
)
_VmwInfrastructureAppliance_ObjectIdentity = ObjectIdentity
vmwInfrastructureAppliance = _VmwInfrastructureAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 8)
)
_VmwManagementAppliance_ObjectIdentity = ObjectIdentity
vmwManagementAppliance = _VmwManagementAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 9)
)
_VmwNSX_ObjectIdentity = ObjectIdentity
vmwNSX = _VmwNSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 10)
)
_VmwHCXGateway_ObjectIdentity = ObjectIdentity
vmwHCXGateway = _VmwHCXGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 31)
)
_VmwVrops_ObjectIdentity = ObjectIdentity
vmwVrops = _VmwVrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50)
)
_VmwNSXEdgeAppliance_ObjectIdentity = ObjectIdentity
vmwNSXEdgeAppliance = _VmwNSXEdgeAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 130)
)
_VmwNSXManagerAppliance_ObjectIdentity = ObjectIdentity
vmwNSXManagerAppliance = _VmwNSXManagerAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 131)
)
_VmwNSXControllerAppliance_ObjectIdentity = ObjectIdentity
vmwNSXControllerAppliance = _VmwNSXControllerAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 132)
)
_VmwHCXManager_ObjectIdentity = ObjectIdentity
vmwHCXManager = _VmwHCXManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 230)
)
_VmwTunnelServer_ObjectIdentity = ObjectIdentity
vmwTunnelServer = _VmwTunnelServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 250)
)
_VmwHorizonCloudConnector_ObjectIdentity = ObjectIdentity
vmwHorizonCloudConnector = _VmwHorizonCloudConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 350)
)
_OidESX_ObjectIdentity = ObjectIdentity
oidESX = _OidESX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 60, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-PRODUCTS-MIB",
    **{"vmwESX": vmwESX,
       "vmwDVS": vmwDVS,
       "vmwVC": vmwVC,
       "vmwServer": vmwServer,
       "vmwVCOps": vmwVCOps,
       "vmwGenericAppliance": vmwGenericAppliance,
       "vmwEmbeddedVirtualCenterAppliance": vmwEmbeddedVirtualCenterAppliance,
       "vmwInfrastructureAppliance": vmwInfrastructureAppliance,
       "vmwManagementAppliance": vmwManagementAppliance,
       "vmwNSX": vmwNSX,
       "vmwProducts": vmwProducts,
       "vmwHCXGateway": vmwHCXGateway,
       "vmwVrops": vmwVrops,
       "vmwNSXEdgeAppliance": vmwNSXEdgeAppliance,
       "vmwNSXManagerAppliance": vmwNSXManagerAppliance,
       "vmwNSXControllerAppliance": vmwNSXControllerAppliance,
       "vmwHCXManager": vmwHCXManager,
       "vmwTunnelServer": vmwTunnelServer,
       "vmwHorizonCloudConnector": vmwHorizonCloudConnector,
       "oidESX": oidESX}
)
