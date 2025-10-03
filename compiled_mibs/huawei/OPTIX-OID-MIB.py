# SNMP MIB module (OPTIX-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\OPTIX-OID-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:01 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25)
)
_OptixCommon_ObjectIdentity = ObjectIdentity
optixCommon = _OptixCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3)
)
_OptixCommonSnmp_ObjectIdentity = ObjectIdentity
optixCommonSnmp = _OptixCommonSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 1)
)
_OptixCommonSdh_ObjectIdentity = ObjectIdentity
optixCommonSdh = _OptixCommonSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 10)
)
_OptixCommonSonet_ObjectIdentity = ObjectIdentity
optixCommonSonet = _OptixCommonSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20)
)
_OptixNGWDM_ObjectIdentity = ObjectIdentity
optixNGWDM = _OptixNGWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 30)
)
_OptixCommonGlobal_ObjectIdentity = ObjectIdentity
optixCommonGlobal = _OptixCommonGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40)
)
_OptixNGWDMGlobal_ObjectIdentity = ObjectIdentity
optixNGWDMGlobal = _OptixNGWDMGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 50)
)
_OptixPtnGlobal_ObjectIdentity = ObjectIdentity
optixPtnGlobal = _OptixPtnGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 60)
)
_Rtn_ObjectIdentity = ObjectIdentity
rtn = _Rtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 70)
)
_OptixProvision_ObjectIdentity = ObjectIdentity
optixProvision = _OptixProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4)
)
_OptixProvisionSdh_ObjectIdentity = ObjectIdentity
optixProvisionSdh = _OptixProvisionSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 10)
)
_OptixProvisionSonet_ObjectIdentity = ObjectIdentity
optixProvisionSonet = _OptixProvisionSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20)
)
_OptixProvisionEqpt_ObjectIdentity = ObjectIdentity
optixProvisionEqpt = _OptixProvisionEqpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30)
)
_OptixProvisionRtn_ObjectIdentity = ObjectIdentity
optixProvisionRtn = _OptixProvisionRtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 40)
)
_OptixProvisionPtn_ObjectIdentity = ObjectIdentity
optixProvisionPtn = _OptixProvisionPtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-OID-MIB",
    **{"huawei": huawei,
       "products": products,
       "transmission": transmission,
       "optixCommon": optixCommon,
       "optixCommonSnmp": optixCommonSnmp,
       "optixCommonSdh": optixCommonSdh,
       "optixCommonSonet": optixCommonSonet,
       "optixNGWDM": optixNGWDM,
       "optixCommonGlobal": optixCommonGlobal,
       "optixNGWDMGlobal": optixNGWDMGlobal,
       "optixPtnGlobal": optixPtnGlobal,
       "rtn": rtn,
       "optixProvision": optixProvision,
       "optixProvisionSdh": optixProvisionSdh,
       "optixProvisionSonet": optixProvisionSonet,
       "optixProvisionEqpt": optixProvisionEqpt,
       "optixProvisionRtn": optixProvisionRtn,
       "optixProvisionPtn": optixProvisionPtn}
)
