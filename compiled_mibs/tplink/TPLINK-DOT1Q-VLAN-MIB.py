# SNMP MIB module (TPLINK-DOT1Q-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-DOT1Q-VLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:30 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkDot1qVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14)
)
if mibBuilder.loadTexts:
    tplinkDot1qVlanMIB.setRevisions(
        ("2009-08-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDot1qVlanMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDot1qVlanMIBObjects = _TplinkDot1qVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1)
)
_VlanPortConfig_ObjectIdentity = ObjectIdentity
vlanPortConfig = _VlanPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1)
)
_VlanPortConfigTable_Object = MibTable
vlanPortConfigTable = _VlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vlanPortConfigTable.setStatus("current")
_VlanPortConifgEntry_Object = MibTableRow
vlanPortConifgEntry = _VlanPortConifgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1, 1, 1)
)
vlanPortConifgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPortConifgEntry.setStatus("current")


class _VlanPortNumber_Type(OctetString):
    """Custom type vlanPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanPortNumber_Type.__name__ = "OctetString"
_VlanPortNumber_Object = MibTableColumn
vlanPortNumber = _VlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1, 1, 1, 1),
    _VlanPortNumber_Type()
)
vlanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortNumber.setStatus("current")


class _VlanPortType_Type(Integer32):
    """Custom type vlanPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("trunk", 1),
          ("general", 2))
    )


_VlanPortType_Type.__name__ = "Integer32"
_VlanPortType_Object = MibTableColumn
vlanPortType = _VlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1, 1, 1, 2),
    _VlanPortType_Type()
)
vlanPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortType.setStatus("current")


class _VlanPortPvid_Type(Integer32):
    """Custom type vlanPortPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanPortPvid_Type.__name__ = "Integer32"
_VlanPortPvid_Object = MibTableColumn
vlanPortPvid = _VlanPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1, 1, 1, 3),
    _VlanPortPvid_Type()
)
vlanPortPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortPvid.setStatus("current")


class _VlanPortLag_Type(DisplayString):
    """Custom type vlanPortLag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VlanPortLag_Type.__name__ = "DisplayString"
_VlanPortLag_Object = MibTableColumn
vlanPortLag = _VlanPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1, 1, 1, 4),
    _VlanPortLag_Type()
)
vlanPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortLag.setStatus("current")


class _VlanPortUnknown_Type(DisplayString):
    """Custom type vlanPortUnknown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_VlanPortUnknown_Type.__name__ = "DisplayString"
_VlanPortUnknown_Object = MibScalar
vlanPortUnknown = _VlanPortUnknown_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 1, 1, 1, 5),
    _VlanPortUnknown_Type()
)
vlanPortUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortUnknown.setStatus("current")
_VlanConfig_ObjectIdentity = ObjectIdentity
vlanConfig = _VlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2)
)
_VlanConfigTable_Object = MibTable
vlanConfigTable = _VlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vlanConfigTable.setStatus("current")
_VlanConfigEntry_Object = MibTableRow
vlanConfigEntry = _VlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1, 1)
)
vlanConfigEntry.setIndexNames(
    (0, "TPLINK-DOT1Q-VLAN-MIB", "dot1qVlanId"),
)
if mibBuilder.loadTexts:
    vlanConfigEntry.setStatus("current")


class _Dot1qVlanId_Type(Integer32):
    """Custom type dot1qVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot1qVlanId_Type.__name__ = "Integer32"
_Dot1qVlanId_Object = MibTableColumn
dot1qVlanId = _Dot1qVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1, 1, 1),
    _Dot1qVlanId_Type()
)
dot1qVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanId.setStatus("current")


class _Dot1qVlanDescription_Type(OctetString):
    """Custom type dot1qVlanDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot1qVlanDescription_Type.__name__ = "OctetString"
_Dot1qVlanDescription_Object = MibTableColumn
dot1qVlanDescription = _Dot1qVlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1, 1, 2),
    _Dot1qVlanDescription_Type()
)
dot1qVlanDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanDescription.setStatus("current")
_VlanTagPortMemberAdd_Type = OctetString
_VlanTagPortMemberAdd_Object = MibTableColumn
vlanTagPortMemberAdd = _VlanTagPortMemberAdd_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1, 1, 3),
    _VlanTagPortMemberAdd_Type()
)
vlanTagPortMemberAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTagPortMemberAdd.setStatus("current")
_VlanUntagPortMemberAdd_Type = OctetString
_VlanUntagPortMemberAdd_Object = MibTableColumn
vlanUntagPortMemberAdd = _VlanUntagPortMemberAdd_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1, 1, 4),
    _VlanUntagPortMemberAdd_Type()
)
vlanUntagPortMemberAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanUntagPortMemberAdd.setStatus("current")
_VlanPortMemberRemove_Type = OctetString
_VlanPortMemberRemove_Object = MibTableColumn
vlanPortMemberRemove = _VlanPortMemberRemove_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1, 1, 5),
    _VlanPortMemberRemove_Type()
)
vlanPortMemberRemove.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortMemberRemove.setStatus("current")
_Dot1qVlanStatus_Type = TPRowStatus
_Dot1qVlanStatus_Object = MibTableColumn
dot1qVlanStatus = _Dot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 1, 2, 1, 1, 6),
    _Dot1qVlanStatus_Type()
)
dot1qVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanStatus.setStatus("current")
_TplinkDot1qVlanNotifications_ObjectIdentity = ObjectIdentity
tplinkDot1qVlanNotifications = _TplinkDot1qVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 2)
)

# Managed Objects groups


# Notification objects

vlanTableCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 14, 2, 1)
)
vlanTableCreate.setObjects(
    ("TPLINK-DOT1Q-VLAN-MIB", "dot1qVlanId")
)
if mibBuilder.loadTexts:
    vlanTableCreate.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DOT1Q-VLAN-MIB",
    **{"tplinkDot1qVlanMIB": tplinkDot1qVlanMIB,
       "tplinkDot1qVlanMIBObjects": tplinkDot1qVlanMIBObjects,
       "vlanPortConfig": vlanPortConfig,
       "vlanPortConfigTable": vlanPortConfigTable,
       "vlanPortConifgEntry": vlanPortConifgEntry,
       "vlanPortNumber": vlanPortNumber,
       "vlanPortType": vlanPortType,
       "vlanPortPvid": vlanPortPvid,
       "vlanPortLag": vlanPortLag,
       "vlanPortUnknown": vlanPortUnknown,
       "vlanConfig": vlanConfig,
       "vlanConfigTable": vlanConfigTable,
       "vlanConfigEntry": vlanConfigEntry,
       "dot1qVlanId": dot1qVlanId,
       "dot1qVlanDescription": dot1qVlanDescription,
       "vlanTagPortMemberAdd": vlanTagPortMemberAdd,
       "vlanUntagPortMemberAdd": vlanUntagPortMemberAdd,
       "vlanPortMemberRemove": vlanPortMemberRemove,
       "dot1qVlanStatus": dot1qVlanStatus,
       "tplinkDot1qVlanNotifications": tplinkDot1qVlanNotifications,
       "vlanTableCreate": vlanTableCreate}
)
