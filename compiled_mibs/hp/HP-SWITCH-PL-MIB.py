# SNMP MIB module (HP-SWITCH-PL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hp\HP-SWITCH-PL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:32 2025
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_HpEtherSwitch_ObjectIdentity = ObjectIdentity
hpEtherSwitch = _HpEtherSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11)
)
_HpSwitchProliant_ObjectIdentity = ObjectIdentity
hpSwitchProliant = _HpSwitchProliant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33)
)
_HpSwitchModuleBladetype2_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype2 = _HpSwitchModuleBladetype2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1)
)
_HpSwitchBladeType2_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType2_Products = _HpSwitchBladeType2_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 1)
)
_HpSwitchBladeType2_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType2_Mgmt = _HpSwitchBladeType2_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2)
)
_HpSwitchModuleBladetype4_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype4 = _HpSwitchModuleBladetype4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 4)
)
_HpSwitchBladeType4_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType4_Products = _HpSwitchBladeType4_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 4, 1)
)
_HpSwitchBladeType4_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType4_Mgmt = _HpSwitchBladeType4_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 4, 2)
)
_HpSwitchModuleBladetype5_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype5 = _HpSwitchModuleBladetype5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 5)
)
_HpSwitchBladeType5_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType5_Products = _HpSwitchBladeType5_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 5, 1)
)
_HpSwitchBladeType5_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType5_Mgmt = _HpSwitchBladeType5_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 5, 2)
)
_HpSwitchModuleBladetype6_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype6 = _HpSwitchModuleBladetype6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 6)
)
_HpSwitchBladeType6_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType6_Products = _HpSwitchBladeType6_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 6, 1)
)
_HpSwitchBladeType6_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType6_Mgmt = _HpSwitchBladeType6_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 6, 2)
)
_HpSwitchModuleBladetype7_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype7 = _HpSwitchModuleBladetype7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 7)
)
_HpSwitchBladeType7_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType7_Products = _HpSwitchBladeType7_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 7, 1)
)
_HpSwitchBladeType7_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType7_Mgmt = _HpSwitchBladeType7_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 7, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SWITCH-PL-MIB",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "netElement": netElement,
       "hpEtherSwitch": hpEtherSwitch,
       "hpSwitchProliant": hpSwitchProliant,
       "hpSwitchModuleBladetype2": hpSwitchModuleBladetype2,
       "hpSwitchBladeType2-Products": hpSwitchBladeType2_Products,
       "hpSwitchBladeType2-Mgmt": hpSwitchBladeType2_Mgmt,
       "hpSwitchModuleBladetype4": hpSwitchModuleBladetype4,
       "hpSwitchBladeType4-Products": hpSwitchBladeType4_Products,
       "hpSwitchBladeType4-Mgmt": hpSwitchBladeType4_Mgmt,
       "hpSwitchModuleBladetype5": hpSwitchModuleBladetype5,
       "hpSwitchBladeType5-Products": hpSwitchBladeType5_Products,
       "hpSwitchBladeType5-Mgmt": hpSwitchBladeType5_Mgmt,
       "hpSwitchModuleBladetype6": hpSwitchModuleBladetype6,
       "hpSwitchBladeType6-Products": hpSwitchBladeType6_Products,
       "hpSwitchBladeType6-Mgmt": hpSwitchBladeType6_Mgmt,
       "hpSwitchModuleBladetype7": hpSwitchModuleBladetype7,
       "hpSwitchBladeType7-Products": hpSwitchBladeType7_Products,
       "hpSwitchBladeType7-Mgmt": hpSwitchBladeType7_Mgmt}
)
