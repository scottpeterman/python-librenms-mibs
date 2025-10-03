# SNMP MIB module (VLAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\exalt\VLAN
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:08 2025
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

(interface,) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "interface")

(VlanGroupT,
 VlanStatusT) = mibBuilder.importSymbols(
    "ExaltComm",
    "VlanGroupT",
    "VlanStatusT")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    vlan.setStatus("current")
_VlanStatus_Type = VlanStatusT
_VlanStatus_Object = MibScalar
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("current")


class _VlanDefaultMgmtId_Type(Integer32):
    """Custom type vlanDefaultMgmtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanDefaultMgmtId_Type.__name__ = "Integer32"
_VlanDefaultMgmtId_Object = MibScalar
vlanDefaultMgmtId = _VlanDefaultMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 5),
    _VlanDefaultMgmtId_Type()
)
vlanDefaultMgmtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultMgmtId.setStatus("current")
_VlanInterfaces_Object = MibTable
vlanInterfaces = _VlanInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6)
)
if mibBuilder.loadTexts:
    vlanInterfaces.setStatus("current")
_VlanInterfacesEntry_Object = MibTableRow
vlanInterfacesEntry = _VlanInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1)
)
vlanInterfacesEntry.setIndexNames(
    (0, "VLAN", "vlanDefaultId"),
)
if mibBuilder.loadTexts:
    vlanInterfacesEntry.setStatus("current")


class _VlanDefaultId_Type(Integer32):
    """Custom type vlanDefaultId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanDefaultId_Type.__name__ = "Integer32"
_VlanDefaultId_Object = MibTableColumn
vlanDefaultId = _VlanDefaultId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 1),
    _VlanDefaultId_Type()
)
vlanDefaultId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultId.setStatus("current")


class _VlanID_Type(DisplayString):
    """Custom type vlanID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_VlanID_Type.__name__ = "DisplayString"
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 2),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")


class _CommitVlanSettings_Type(DisplayString):
    """Custom type commitVlanSettings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 200),
    )


_CommitVlanSettings_Type.__name__ = "DisplayString"
_CommitVlanSettings_Object = MibScalar
commitVlanSettings = _CommitVlanSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1000),
    _CommitVlanSettings_Type()
)
commitVlanSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitVlanSettings.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VLAN",
    **{"vlan": vlan,
       "vlanStatus": vlanStatus,
       "vlanDefaultMgmtId": vlanDefaultMgmtId,
       "vlanInterfaces": vlanInterfaces,
       "vlanInterfacesEntry": vlanInterfacesEntry,
       "vlanDefaultId": vlanDefaultId,
       "vlanID": vlanID,
       "commitVlanSettings": commitVlanSettings}
)
