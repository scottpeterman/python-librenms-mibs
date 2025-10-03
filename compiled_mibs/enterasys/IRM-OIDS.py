# SNMP MIB module (IRM-OIDS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\IRM-OIDS
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:34 2025
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommsDevice_ObjectIdentity = ObjectIdentity
commsDevice = _CommsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1)
)
_CommonRev1_ObjectIdentity = ObjectIdentity
commonRev1 = _CommonRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1)
)
_SysOIDs_ObjectIdentity = ObjectIdentity
sysOIDs = _SysOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2)
)
_SysOtherType_ObjectIdentity = ObjectIdentity
sysOtherType = _SysOtherType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 1)
)
_SysChassis_ObjectIdentity = ObjectIdentity
sysChassis = _SysChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2)
)
_SysRepeaters_ObjectIdentity = ObjectIdentity
sysRepeaters = _SysRepeaters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3)
)
_SysBridges_ObjectIdentity = ObjectIdentity
sysBridges = _SysBridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 4)
)
_SysRouters_ObjectIdentity = ObjectIdentity
sysRouters = _SysRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 5)
)
_SysIntDev_ObjectIdentity = ObjectIdentity
sysIntDev = _SysIntDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 6)
)
_Repeater_ObjectIdentity = ObjectIdentity
repeater = _Repeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2)
)
_RepeaterRev1_ObjectIdentity = ObjectIdentity
repeaterRev1 = _RepeaterRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1)
)
_RepeaterRev2_ObjectIdentity = ObjectIdentity
repeaterRev2 = _RepeaterRev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 4)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 5)
)
_Subsystem_ObjectIdentity = ObjectIdentity
subsystem = _Subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6)
)
_SubSysMMAC_ObjectIdentity = ObjectIdentity
subSysMMAC = _SubSysMMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1)
)
_SubSysDevice_ObjectIdentity = ObjectIdentity
subSysDevice = _SubSysDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3)
)
_Dl_ObjectIdentity = ObjectIdentity
dl = _Dl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4)
)
_BackplaneProtocol_ObjectIdentity = ObjectIdentity
backplaneProtocol = _BackplaneProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 5)
)
_Nb30Rev1_ObjectIdentity = ObjectIdentity
nb30Rev1 = _Nb30Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12)
)
_LayerMgmt_ObjectIdentity = ObjectIdentity
layerMgmt = _LayerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IRM-OIDS",
    **{"commsDevice": commsDevice,
       "common": common,
       "commonRev1": commonRev1,
       "sysOIDs": sysOIDs,
       "sysOtherType": sysOtherType,
       "sysChassis": sysChassis,
       "sysRepeaters": sysRepeaters,
       "sysBridges": sysBridges,
       "sysRouters": sysRouters,
       "sysIntDev": sysIntDev,
       "repeater": repeater,
       "repeaterRev1": repeaterRev1,
       "repeaterRev2": repeaterRev2,
       "bridge": bridge,
       "router": router,
       "product": product,
       "subsystem": subsystem,
       "subSysMMAC": subSysMMAC,
       "subSysDevice": subSysDevice,
       "ups": ups,
       "dl": dl,
       "backplaneProtocol": backplaneProtocol,
       "nb30Rev1": nb30Rev1,
       "layerMgmt": layerMgmt}
)
