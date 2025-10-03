# SNMP MIB module (TN-DEV-VLAN-TRANSLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-VLAN-TRANSLATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:14 2025
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

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevVlanTranslation_ObjectIdentity = ObjectIdentity
tnDevVlanTranslation = _TnDevVlanTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37)
)
_TnVlanTransPort2GroupMapTable_Object = MibTable
tnVlanTransPort2GroupMapTable = _TnVlanTransPort2GroupMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 1)
)
if mibBuilder.loadTexts:
    tnVlanTransPort2GroupMapTable.setStatus("current")
_TnVlanTransPort2GroupMapEntry_Object = MibTableRow
tnVlanTransPort2GroupMapEntry = _TnVlanTransPort2GroupMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 1, 1)
)
tnVlanTransPort2GroupMapEntry.setIndexNames(
    (0, "TN-DEV-VLAN-TRANSLATION-MIB", "tnVlanTransPort2GroupMapGroupId"),
)
if mibBuilder.loadTexts:
    tnVlanTransPort2GroupMapEntry.setStatus("current")
_TnVlanTransPort2GroupMapGroupId_Type = Unsigned32
_TnVlanTransPort2GroupMapGroupId_Object = MibTableColumn
tnVlanTransPort2GroupMapGroupId = _TnVlanTransPort2GroupMapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 1, 1, 1),
    _TnVlanTransPort2GroupMapGroupId_Type()
)
tnVlanTransPort2GroupMapGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVlanTransPort2GroupMapGroupId.setStatus("current")
_TnVlanTransPort2GroupMapPortMember_Type = PortList
_TnVlanTransPort2GroupMapPortMember_Object = MibTableColumn
tnVlanTransPort2GroupMapPortMember = _TnVlanTransPort2GroupMapPortMember_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 1, 1, 2),
    _TnVlanTransPort2GroupMapPortMember_Type()
)
tnVlanTransPort2GroupMapPortMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanTransPort2GroupMapPortMember.setStatus("current")
_TnVlanTransPort2GroupMapRowStatus_Type = RowStatus
_TnVlanTransPort2GroupMapRowStatus_Object = MibTableColumn
tnVlanTransPort2GroupMapRowStatus = _TnVlanTransPort2GroupMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 1, 1, 3),
    _TnVlanTransPort2GroupMapRowStatus_Type()
)
tnVlanTransPort2GroupMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanTransPort2GroupMapRowStatus.setStatus("current")
_TnVlanTransMapTable_Object = MibTable
tnVlanTransMapTable = _TnVlanTransMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 2)
)
if mibBuilder.loadTexts:
    tnVlanTransMapTable.setStatus("current")
_TnVlanTransMapEntry_Object = MibTableRow
tnVlanTransMapEntry = _TnVlanTransMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 2, 1)
)
tnVlanTransMapEntry.setIndexNames(
    (0, "TN-DEV-VLAN-TRANSLATION-MIB", "tnVlanTransMapGroupId"),
    (0, "TN-DEV-VLAN-TRANSLATION-MIB", "tnVlanTransMapVlanId"),
)
if mibBuilder.loadTexts:
    tnVlanTransMapEntry.setStatus("current")
_TnVlanTransMapGroupId_Type = Unsigned32
_TnVlanTransMapGroupId_Object = MibTableColumn
tnVlanTransMapGroupId = _TnVlanTransMapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 2, 1, 1),
    _TnVlanTransMapGroupId_Type()
)
tnVlanTransMapGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVlanTransMapGroupId.setStatus("current")
_TnVlanTransMapVlanId_Type = VlanId
_TnVlanTransMapVlanId_Object = MibTableColumn
tnVlanTransMapVlanId = _TnVlanTransMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 2, 1, 2),
    _TnVlanTransMapVlanId_Type()
)
tnVlanTransMapVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVlanTransMapVlanId.setStatus("current")
_TnVlanTransMapTranslatedVlanId_Type = VlanId
_TnVlanTransMapTranslatedVlanId_Object = MibTableColumn
tnVlanTransMapTranslatedVlanId = _TnVlanTransMapTranslatedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 2, 1, 3),
    _TnVlanTransMapTranslatedVlanId_Type()
)
tnVlanTransMapTranslatedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVlanTransMapTranslatedVlanId.setStatus("current")
_TnVlanTransMapRowStatus_Type = RowStatus
_TnVlanTransMapRowStatus_Object = MibTableColumn
tnVlanTransMapRowStatus = _TnVlanTransMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 37, 2, 1, 4),
    _TnVlanTransMapRowStatus_Type()
)
tnVlanTransMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanTransMapRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-VLAN-TRANSLATION-MIB",
    **{"tnDevVlanTranslation": tnDevVlanTranslation,
       "tnVlanTransPort2GroupMapTable": tnVlanTransPort2GroupMapTable,
       "tnVlanTransPort2GroupMapEntry": tnVlanTransPort2GroupMapEntry,
       "tnVlanTransPort2GroupMapGroupId": tnVlanTransPort2GroupMapGroupId,
       "tnVlanTransPort2GroupMapPortMember": tnVlanTransPort2GroupMapPortMember,
       "tnVlanTransPort2GroupMapRowStatus": tnVlanTransPort2GroupMapRowStatus,
       "tnVlanTransMapTable": tnVlanTransMapTable,
       "tnVlanTransMapEntry": tnVlanTransMapEntry,
       "tnVlanTransMapGroupId": tnVlanTransMapGroupId,
       "tnVlanTransMapVlanId": tnVlanTransMapVlanId,
       "tnVlanTransMapTranslatedVlanId": tnVlanTransMapTranslatedVlanId,
       "tnVlanTransMapRowStatus": tnVlanTransMapRowStatus}
)
