# SNMP MIB module (BENU-PLATFORM-DEFN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\benuos\BENU-PLATFORM-DEFN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:07 2025
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

(benuPlatform,) = mibBuilder.importSymbols(
    "BENU-PLATFORM-MIB",
    "benuPlatform")

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

benuPlatformDefn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2)
)
if mibBuilder.loadTexts:
    benuPlatformDefn.setRevisions(
        ("2016-11-17 00:00",
         "2016-10-13 00:00",
         "2016-04-12 00:00",
         "2012-10-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BenuPlatformTypes_ObjectIdentity = ObjectIdentity
benuPlatformTypes = _BenuPlatformTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1)
)
_PlatformUnknown_ObjectIdentity = ObjectIdentity
platformUnknown = _PlatformUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 0)
)
_Benu_xMEG_100_ObjectIdentity = ObjectIdentity
Benu_xMEG_100 = _Benu_xMEG_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 1)
)
_Benu_xMEG_10_ObjectIdentity = ObjectIdentity
Benu_xMEG_10 = _Benu_xMEG_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 2)
)
_Benu_Internal_ObjectIdentity = ObjectIdentity
Benu_Internal = _Benu_Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 3)
)
_Benu_Virtual_ObjectIdentity = ObjectIdentity
Benu_Virtual = _Benu_Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 4)
)
_Benu_KVM_ObjectIdentity = ObjectIdentity
Benu_KVM = _Benu_KVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 5)
)
_Benu_VMware_ObjectIdentity = ObjectIdentity
Benu_VMware = _Benu_VMware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 6)
)
_Benu_VirtualBox_ObjectIdentity = ObjectIdentity
Benu_VirtualBox = _Benu_VirtualBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 7)
)
_BenuChassisTypes_ObjectIdentity = ObjectIdentity
benuChassisTypes = _BenuChassisTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 2)
)
_BenuChassisTypeUnknown_ObjectIdentity = ObjectIdentity
benuChassisTypeUnknown = _BenuChassisTypeUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 0)
)
_BenuChassisTypeMEG100_ObjectIdentity = ObjectIdentity
benuChassisTypeMEG100 = _BenuChassisTypeMEG100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 1)
)
_BenuChassisTypeMEG400_ObjectIdentity = ObjectIdentity
benuChassisTypeMEG400 = _BenuChassisTypeMEG400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 2)
)
_BenuChassisTypeMEG1200_ObjectIdentity = ObjectIdentity
benuChassisTypeMEG1200 = _BenuChassisTypeMEG1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 3)
)
_BenuChassisTypeMEG50_ObjectIdentity = ObjectIdentity
benuChassisTypeMEG50 = _BenuChassisTypeMEG50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 4)
)
_BenuCardTypes_ObjectIdentity = ObjectIdentity
benuCardTypes = _BenuCardTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3)
)
_BenuCardUnknown_ObjectIdentity = ObjectIdentity
benuCardUnknown = _BenuCardUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 0)
)
_BenuCardRSM_ObjectIdentity = ObjectIdentity
benuCardRSM = _BenuCardRSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 1)
)
_BenuCardSwitchFabric_ObjectIdentity = ObjectIdentity
benuCardSwitchFabric = _BenuCardSwitchFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 2)
)
_BenuCardShelfMgr_ObjectIdentity = ObjectIdentity
benuCardShelfMgr = _BenuCardShelfMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 3)
)
_BenuCardSEFP_ObjectIdentity = ObjectIdentity
benuCardSEFP = _BenuCardSEFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 4)
)
_BenuCardIO_ObjectIdentity = ObjectIdentity
benuCardIO = _BenuCardIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 5)
)
_BenuCardSwitchMesh_ObjectIdentity = ObjectIdentity
benuCardSwitchMesh = _BenuCardSwitchMesh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 6)
)
_BenuPortTypes_ObjectIdentity = ObjectIdentity
benuPortTypes = _BenuPortTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4)
)
_BenuPortUnknown_ObjectIdentity = ObjectIdentity
benuPortUnknown = _BenuPortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 0)
)
_BenuPortGige_ObjectIdentity = ObjectIdentity
benuPortGige = _BenuPortGige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 1)
)
_BenuPortEthernet_ObjectIdentity = ObjectIdentity
benuPortEthernet = _BenuPortEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 2)
)
_BenuPortl2tp_ObjectIdentity = ObjectIdentity
benuPortl2tp = _BenuPortl2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 3)
)
_BenuPortLoopback_ObjectIdentity = ObjectIdentity
benuPortLoopback = _BenuPortLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 4)
)
_BenuPortT1_ObjectIdentity = ObjectIdentity
benuPortT1 = _BenuPortT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 5)
)
_BenuPortNULL_ObjectIdentity = ObjectIdentity
benuPortNULL = _BenuPortNULL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 6)
)
_BenuPortTunnel_ObjectIdentity = ObjectIdentity
benuPortTunnel = _BenuPortTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 7)
)
_BenuPortPOS_ObjectIdentity = ObjectIdentity
benuPortPOS = _BenuPortPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 8)
)
_BenuPortATM_ObjectIdentity = ObjectIdentity
benuPortATM = _BenuPortATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 9)
)
_BenuPortIpGre_ObjectIdentity = ObjectIdentity
benuPortIpGre = _BenuPortIpGre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 10)
)
_BenuPortBridge_ObjectIdentity = ObjectIdentity
benuPortBridge = _BenuPortBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 11)
)
_BenuPortLag_ObjectIdentity = ObjectIdentity
benuPortLag = _BenuPortLag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 12)
)
_BenuPortMultiBind_ObjectIdentity = ObjectIdentity
benuPortMultiBind = _BenuPortMultiBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 13)
)
_BenuPortMultiBindLastResort_ObjectIdentity = ObjectIdentity
benuPortMultiBindLastResort = _BenuPortMultiBindLastResort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-PLATFORM-DEFN-MIB",
    **{"benuPlatformDefn": benuPlatformDefn,
       "benuPlatformTypes": benuPlatformTypes,
       "platformUnknown": platformUnknown,
       "Benu-xMEG-100": Benu_xMEG_100,
       "Benu-xMEG-10": Benu_xMEG_10,
       "Benu-Internal": Benu_Internal,
       "Benu-Virtual": Benu_Virtual,
       "Benu-KVM": Benu_KVM,
       "Benu-VMware": Benu_VMware,
       "Benu-VirtualBox": Benu_VirtualBox,
       "benuChassisTypes": benuChassisTypes,
       "benuChassisTypeUnknown": benuChassisTypeUnknown,
       "benuChassisTypeMEG100": benuChassisTypeMEG100,
       "benuChassisTypeMEG400": benuChassisTypeMEG400,
       "benuChassisTypeMEG1200": benuChassisTypeMEG1200,
       "benuChassisTypeMEG50": benuChassisTypeMEG50,
       "benuCardTypes": benuCardTypes,
       "benuCardUnknown": benuCardUnknown,
       "benuCardRSM": benuCardRSM,
       "benuCardSwitchFabric": benuCardSwitchFabric,
       "benuCardShelfMgr": benuCardShelfMgr,
       "benuCardSEFP": benuCardSEFP,
       "benuCardIO": benuCardIO,
       "benuCardSwitchMesh": benuCardSwitchMesh,
       "benuPortTypes": benuPortTypes,
       "benuPortUnknown": benuPortUnknown,
       "benuPortGige": benuPortGige,
       "benuPortEthernet": benuPortEthernet,
       "benuPortl2tp": benuPortl2tp,
       "benuPortLoopback": benuPortLoopback,
       "benuPortT1": benuPortT1,
       "benuPortNULL": benuPortNULL,
       "benuPortTunnel": benuPortTunnel,
       "benuPortPOS": benuPortPOS,
       "benuPortATM": benuPortATM,
       "benuPortIpGre": benuPortIpGre,
       "benuPortBridge": benuPortBridge,
       "benuPortLag": benuPortLag,
       "benuPortMultiBind": benuPortMultiBind,
       "benuPortMultiBindLastResort": benuPortMultiBindLastResort}
)
