# SNMP MIB module (HH3C-PBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-PBR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:29 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cPBR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113)
)
if mibBuilder.loadTexts:
    hh3cPBR.setRevisions(
        ("2010-12-10 15:58",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPBRObjects_ObjectIdentity = ObjectIdentity
hh3cPBRObjects = _Hh3cPBRObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1)
)
_Hh3cPBRGlobal_ObjectIdentity = ObjectIdentity
hh3cPBRGlobal = _Hh3cPBRGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 1)
)


class _Hh3cPBRNexthopTrapEnabled_Type(TruthValue):
    """Custom type hh3cPBRNexthopTrapEnabled based on TruthValue"""
    defaultValue = 1


_Hh3cPBRNexthopTrapEnabled_Type.__name__ = "TruthValue"
_Hh3cPBRNexthopTrapEnabled_Object = MibScalar
hh3cPBRNexthopTrapEnabled = _Hh3cPBRNexthopTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 1, 1),
    _Hh3cPBRNexthopTrapEnabled_Type()
)
hh3cPBRNexthopTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPBRNexthopTrapEnabled.setStatus("current")


class _Hh3cPBRLocalPolicy_Type(DisplayString):
    """Custom type hh3cPBRLocalPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Hh3cPBRLocalPolicy_Type.__name__ = "DisplayString"
_Hh3cPBRLocalPolicy_Object = MibScalar
hh3cPBRLocalPolicy = _Hh3cPBRLocalPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 1, 2),
    _Hh3cPBRLocalPolicy_Type()
)
hh3cPBRLocalPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPBRLocalPolicy.setStatus("current")


class _Hh3cPBRIPv6NexthopTrapEnabled_Type(TruthValue):
    """Custom type hh3cPBRIPv6NexthopTrapEnabled based on TruthValue"""
    defaultValue = 1


_Hh3cPBRIPv6NexthopTrapEnabled_Type.__name__ = "TruthValue"
_Hh3cPBRIPv6NexthopTrapEnabled_Object = MibScalar
hh3cPBRIPv6NexthopTrapEnabled = _Hh3cPBRIPv6NexthopTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 1, 3),
    _Hh3cPBRIPv6NexthopTrapEnabled_Type()
)
hh3cPBRIPv6NexthopTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPBRIPv6NexthopTrapEnabled.setStatus("current")
_Hh3cPBRMibTrap_ObjectIdentity = ObjectIdentity
hh3cPBRMibTrap = _Hh3cPBRMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2)
)
_Hh3cPBRTrapObjects_ObjectIdentity = ObjectIdentity
hh3cPBRTrapObjects = _Hh3cPBRTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 1)
)
_Hh3cPBRNexthopAddrType_Type = InetAddressType
_Hh3cPBRNexthopAddrType_Object = MibScalar
hh3cPBRNexthopAddrType = _Hh3cPBRNexthopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 1, 1),
    _Hh3cPBRNexthopAddrType_Type()
)
hh3cPBRNexthopAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPBRNexthopAddrType.setStatus("current")
_Hh3cPBRNexthopAddr_Type = InetAddress
_Hh3cPBRNexthopAddr_Object = MibScalar
hh3cPBRNexthopAddr = _Hh3cPBRNexthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 1, 2),
    _Hh3cPBRNexthopAddr_Type()
)
hh3cPBRNexthopAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPBRNexthopAddr.setStatus("current")
_Hh3cPBRTraps_ObjectIdentity = ObjectIdentity
hh3cPBRTraps = _Hh3cPBRTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 2)
)
_Hh3cPBRTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cPBRTrapsPrefix = _Hh3cPBRTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 2, 0)
)
_Hh3cPBRTables_ObjectIdentity = ObjectIdentity
hh3cPBRTables = _Hh3cPBRTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2)
)
_Hh3cPBRMibPolicyNodeTable_Object = MibTable
hh3cPBRMibPolicyNodeTable = _Hh3cPBRMibPolicyNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyNodeTable.setStatus("current")
_Hh3cPBRMibPolicyNodeEntry_Object = MibTableRow
hh3cPBRMibPolicyNodeEntry = _Hh3cPBRMibPolicyNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 1, 1)
)
hh3cPBRMibPolicyNodeEntry.setIndexNames(
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeAddrType"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyName"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeId"),
)
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyNodeEntry.setStatus("current")
_Hh3cPBRMibPolicyNodeAddrType_Type = InetAddressType
_Hh3cPBRMibPolicyNodeAddrType_Object = MibTableColumn
hh3cPBRMibPolicyNodeAddrType = _Hh3cPBRMibPolicyNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 1, 1, 1),
    _Hh3cPBRMibPolicyNodeAddrType_Type()
)
hh3cPBRMibPolicyNodeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyNodeAddrType.setStatus("current")


class _Hh3cPBRMibPolicyName_Type(DisplayString):
    """Custom type hh3cPBRMibPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cPBRMibPolicyName_Type.__name__ = "DisplayString"
_Hh3cPBRMibPolicyName_Object = MibTableColumn
hh3cPBRMibPolicyName = _Hh3cPBRMibPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 1, 1, 2),
    _Hh3cPBRMibPolicyName_Type()
)
hh3cPBRMibPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyName.setStatus("current")


class _Hh3cPBRMibPolicyNodeId_Type(Integer32):
    """Custom type hh3cPBRMibPolicyNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cPBRMibPolicyNodeId_Type.__name__ = "Integer32"
_Hh3cPBRMibPolicyNodeId_Object = MibTableColumn
hh3cPBRMibPolicyNodeId = _Hh3cPBRMibPolicyNodeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 1, 1, 3),
    _Hh3cPBRMibPolicyNodeId_Type()
)
hh3cPBRMibPolicyNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyNodeId.setStatus("current")


class _Hh3cPBRMibPolicyNodeMode_Type(TruthValue):
    """Custom type hh3cPBRMibPolicyNodeMode based on TruthValue"""
    defaultValue = 1


_Hh3cPBRMibPolicyNodeMode_Type.__name__ = "TruthValue"
_Hh3cPBRMibPolicyNodeMode_Object = MibTableColumn
hh3cPBRMibPolicyNodeMode = _Hh3cPBRMibPolicyNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 1, 1, 4),
    _Hh3cPBRMibPolicyNodeMode_Type()
)
hh3cPBRMibPolicyNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyNodeMode.setStatus("current")
_Hh3cPBRMibPolicyNodeRowStatus_Type = RowStatus
_Hh3cPBRMibPolicyNodeRowStatus_Object = MibTableColumn
hh3cPBRMibPolicyNodeRowStatus = _Hh3cPBRMibPolicyNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 1, 1, 5),
    _Hh3cPBRMibPolicyNodeRowStatus_Type()
)
hh3cPBRMibPolicyNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyNodeRowStatus.setStatus("current")
_Hh3cPBRMibIfPolicyTable_Object = MibTable
hh3cPBRMibIfPolicyTable = _Hh3cPBRMibIfPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cPBRMibIfPolicyTable.setStatus("current")
_Hh3cPBRMibIfPolicyEntry_Object = MibTableRow
hh3cPBRMibIfPolicyEntry = _Hh3cPBRMibIfPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 2, 1)
)
hh3cPBRMibIfPolicyEntry.setIndexNames(
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyAddressType"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cPBRMibIfPolicyEntry.setStatus("current")
_Hh3cPBRMibPolicyAddressType_Type = InetAddressType
_Hh3cPBRMibPolicyAddressType_Object = MibTableColumn
hh3cPBRMibPolicyAddressType = _Hh3cPBRMibPolicyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 2, 1, 1),
    _Hh3cPBRMibPolicyAddressType_Type()
)
hh3cPBRMibPolicyAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPBRMibPolicyAddressType.setStatus("current")


class _Hh3cPBRMibAppliedPolicyName_Type(DisplayString):
    """Custom type hh3cPBRMibAppliedPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cPBRMibAppliedPolicyName_Type.__name__ = "DisplayString"
_Hh3cPBRMibAppliedPolicyName_Object = MibTableColumn
hh3cPBRMibAppliedPolicyName = _Hh3cPBRMibAppliedPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 2, 1, 2),
    _Hh3cPBRMibAppliedPolicyName_Type()
)
hh3cPBRMibAppliedPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibAppliedPolicyName.setStatus("current")
_Hh3cPBRMibIfPolicyRowStatus_Type = RowStatus
_Hh3cPBRMibIfPolicyRowStatus_Object = MibTableColumn
hh3cPBRMibIfPolicyRowStatus = _Hh3cPBRMibIfPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 2, 1, 3),
    _Hh3cPBRMibIfPolicyRowStatus_Type()
)
hh3cPBRMibIfPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibIfPolicyRowStatus.setStatus("current")
_Hh3cPBRMibMatchAclTable_Object = MibTable
hh3cPBRMibMatchAclTable = _Hh3cPBRMibMatchAclTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cPBRMibMatchAclTable.setStatus("current")
_Hh3cPBRMibMatchAclEntry_Object = MibTableRow
hh3cPBRMibMatchAclEntry = _Hh3cPBRMibMatchAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 3, 1)
)
hh3cPBRMibMatchAclEntry.setIndexNames(
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeAddrType"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyName"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeId"),
)
if mibBuilder.loadTexts:
    hh3cPBRMibMatchAclEntry.setStatus("current")
_Hh3cPBRMibAclGroupId_Type = Integer32
_Hh3cPBRMibAclGroupId_Object = MibTableColumn
hh3cPBRMibAclGroupId = _Hh3cPBRMibAclGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 3, 1, 1),
    _Hh3cPBRMibAclGroupId_Type()
)
hh3cPBRMibAclGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPBRMibAclGroupId.setStatus("current")
_Hh3cPBRMibApplyPrecedenceTable_Object = MibTable
hh3cPBRMibApplyPrecedenceTable = _Hh3cPBRMibApplyPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cPBRMibApplyPrecedenceTable.setStatus("current")
_Hh3cPBRMibApplyPrecedenceEntry_Object = MibTableRow
hh3cPBRMibApplyPrecedenceEntry = _Hh3cPBRMibApplyPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 4, 1)
)
hh3cPBRMibApplyPrecedenceEntry.setIndexNames(
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeAddrType"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyName"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeId"),
)
if mibBuilder.loadTexts:
    hh3cPBRMibApplyPrecedenceEntry.setStatus("current")
_Hh3cPBRMibApplyPrecedenceValue_Type = Integer32
_Hh3cPBRMibApplyPrecedenceValue_Object = MibTableColumn
hh3cPBRMibApplyPrecedenceValue = _Hh3cPBRMibApplyPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 4, 1, 1),
    _Hh3cPBRMibApplyPrecedenceValue_Type()
)
hh3cPBRMibApplyPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyPrecedenceValue.setStatus("current")
_Hh3cPBRMibApplyNexthopTable_Object = MibTable
hh3cPBRMibApplyNexthopTable = _Hh3cPBRMibApplyNexthopTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopTable.setStatus("current")
_Hh3cPBRMibApplyNexthopEntry_Object = MibTableRow
hh3cPBRMibApplyNexthopEntry = _Hh3cPBRMibApplyNexthopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1)
)
hh3cPBRMibApplyNexthopEntry.setIndexNames(
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeAddrType"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyName"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeId"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibApplyNexthopIndex"),
)
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopEntry.setStatus("current")


class _Hh3cPBRMibApplyNexthopIndex_Type(Integer32):
    """Custom type hh3cPBRMibApplyNexthopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPBRMibApplyNexthopIndex_Type.__name__ = "Integer32"
_Hh3cPBRMibApplyNexthopIndex_Object = MibTableColumn
hh3cPBRMibApplyNexthopIndex = _Hh3cPBRMibApplyNexthopIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1, 1),
    _Hh3cPBRMibApplyNexthopIndex_Type()
)
hh3cPBRMibApplyNexthopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopIndex.setStatus("current")


class _Hh3cPBRMibApplyNexthopVpnName_Type(DisplayString):
    """Custom type hh3cPBRMibApplyNexthopVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cPBRMibApplyNexthopVpnName_Type.__name__ = "DisplayString"
_Hh3cPBRMibApplyNexthopVpnName_Object = MibTableColumn
hh3cPBRMibApplyNexthopVpnName = _Hh3cPBRMibApplyNexthopVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1, 2),
    _Hh3cPBRMibApplyNexthopVpnName_Type()
)
hh3cPBRMibApplyNexthopVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopVpnName.setStatus("current")
_Hh3cPBRMibApplyNexthopAddressType_Type = InetAddressType
_Hh3cPBRMibApplyNexthopAddressType_Object = MibTableColumn
hh3cPBRMibApplyNexthopAddressType = _Hh3cPBRMibApplyNexthopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1, 3),
    _Hh3cPBRMibApplyNexthopAddressType_Type()
)
hh3cPBRMibApplyNexthopAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopAddressType.setStatus("current")
_Hh3cPBRMibApplyNexthopAddress_Type = InetAddress
_Hh3cPBRMibApplyNexthopAddress_Object = MibTableColumn
hh3cPBRMibApplyNexthopAddress = _Hh3cPBRMibApplyNexthopAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1, 4),
    _Hh3cPBRMibApplyNexthopAddress_Type()
)
hh3cPBRMibApplyNexthopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopAddress.setStatus("current")
_Hh3cPBRMibApplyNexthopTrackId_Type = Integer32
_Hh3cPBRMibApplyNexthopTrackId_Object = MibTableColumn
hh3cPBRMibApplyNexthopTrackId = _Hh3cPBRMibApplyNexthopTrackId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1, 5),
    _Hh3cPBRMibApplyNexthopTrackId_Type()
)
hh3cPBRMibApplyNexthopTrackId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopTrackId.setStatus("current")


class _Hh3cPBRMibApplyNexthopDirect_Type(TruthValue):
    """Custom type hh3cPBRMibApplyNexthopDirect based on TruthValue"""
    defaultValue = 2


_Hh3cPBRMibApplyNexthopDirect_Type.__name__ = "TruthValue"
_Hh3cPBRMibApplyNexthopDirect_Object = MibTableColumn
hh3cPBRMibApplyNexthopDirect = _Hh3cPBRMibApplyNexthopDirect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1, 6),
    _Hh3cPBRMibApplyNexthopDirect_Type()
)
hh3cPBRMibApplyNexthopDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopDirect.setStatus("current")
_Hh3cPBRMibApplyNexthopRowStatus_Type = RowStatus
_Hh3cPBRMibApplyNexthopRowStatus_Object = MibTableColumn
hh3cPBRMibApplyNexthopRowStatus = _Hh3cPBRMibApplyNexthopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 5, 1, 7),
    _Hh3cPBRMibApplyNexthopRowStatus_Type()
)
hh3cPBRMibApplyNexthopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyNexthopRowStatus.setStatus("current")
_Hh3cPBRMibApplyDefaultNexthopTable_Object = MibTable
hh3cPBRMibApplyDefaultNexthopTable = _Hh3cPBRMibApplyDefaultNexthopTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopTable.setStatus("current")
_Hh3cPBRMibApplyDefaultNexthopEntry_Object = MibTableRow
hh3cPBRMibApplyDefaultNexthopEntry = _Hh3cPBRMibApplyDefaultNexthopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1)
)
hh3cPBRMibApplyDefaultNexthopEntry.setIndexNames(
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeAddrType"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyName"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibPolicyNodeId"),
    (0, "HH3C-PBR-MIB", "hh3cPBRMibApplyDefaultNexthopIndex"),
)
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopEntry.setStatus("current")


class _Hh3cPBRMibApplyDefaultNexthopIndex_Type(Integer32):
    """Custom type hh3cPBRMibApplyDefaultNexthopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPBRMibApplyDefaultNexthopIndex_Type.__name__ = "Integer32"
_Hh3cPBRMibApplyDefaultNexthopIndex_Object = MibTableColumn
hh3cPBRMibApplyDefaultNexthopIndex = _Hh3cPBRMibApplyDefaultNexthopIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1, 1),
    _Hh3cPBRMibApplyDefaultNexthopIndex_Type()
)
hh3cPBRMibApplyDefaultNexthopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopIndex.setStatus("current")


class _Hh3cPBRMibApplyDefaultNexthopVpnName_Type(DisplayString):
    """Custom type hh3cPBRMibApplyDefaultNexthopVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cPBRMibApplyDefaultNexthopVpnName_Type.__name__ = "DisplayString"
_Hh3cPBRMibApplyDefaultNexthopVpnName_Object = MibTableColumn
hh3cPBRMibApplyDefaultNexthopVpnName = _Hh3cPBRMibApplyDefaultNexthopVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1, 2),
    _Hh3cPBRMibApplyDefaultNexthopVpnName_Type()
)
hh3cPBRMibApplyDefaultNexthopVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopVpnName.setStatus("current")
_Hh3cPBRMibApplyDefaultNexthopAddressType_Type = InetAddressType
_Hh3cPBRMibApplyDefaultNexthopAddressType_Object = MibTableColumn
hh3cPBRMibApplyDefaultNexthopAddressType = _Hh3cPBRMibApplyDefaultNexthopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1, 3),
    _Hh3cPBRMibApplyDefaultNexthopAddressType_Type()
)
hh3cPBRMibApplyDefaultNexthopAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopAddressType.setStatus("current")
_Hh3cPBRMibApplyDefaultNexthopAddress_Type = InetAddress
_Hh3cPBRMibApplyDefaultNexthopAddress_Object = MibTableColumn
hh3cPBRMibApplyDefaultNexthopAddress = _Hh3cPBRMibApplyDefaultNexthopAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1, 4),
    _Hh3cPBRMibApplyDefaultNexthopAddress_Type()
)
hh3cPBRMibApplyDefaultNexthopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopAddress.setStatus("current")
_Hh3cPBRMibApplyDefaultNexthopTrackId_Type = Integer32
_Hh3cPBRMibApplyDefaultNexthopTrackId_Object = MibTableColumn
hh3cPBRMibApplyDefaultNexthopTrackId = _Hh3cPBRMibApplyDefaultNexthopTrackId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1, 5),
    _Hh3cPBRMibApplyDefaultNexthopTrackId_Type()
)
hh3cPBRMibApplyDefaultNexthopTrackId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopTrackId.setStatus("current")


class _Hh3cPBRMibApplyDefaultNexthopDirect_Type(TruthValue):
    """Custom type hh3cPBRMibApplyDefaultNexthopDirect based on TruthValue"""
    defaultValue = 2


_Hh3cPBRMibApplyDefaultNexthopDirect_Type.__name__ = "TruthValue"
_Hh3cPBRMibApplyDefaultNexthopDirect_Object = MibTableColumn
hh3cPBRMibApplyDefaultNexthopDirect = _Hh3cPBRMibApplyDefaultNexthopDirect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1, 6),
    _Hh3cPBRMibApplyDefaultNexthopDirect_Type()
)
hh3cPBRMibApplyDefaultNexthopDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopDirect.setStatus("current")
_Hh3cPBRMibApplyDefaultNexthopRowStatus_Type = RowStatus
_Hh3cPBRMibApplyDefaultNexthopRowStatus_Object = MibTableColumn
hh3cPBRMibApplyDefaultNexthopRowStatus = _Hh3cPBRMibApplyDefaultNexthopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 2, 6, 1, 7),
    _Hh3cPBRMibApplyDefaultNexthopRowStatus_Type()
)
hh3cPBRMibApplyDefaultNexthopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPBRMibApplyDefaultNexthopRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cPBRNexthopFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 2, 0, 1)
)
hh3cPBRNexthopFailedTrap.setObjects(
      *(("HH3C-PBR-MIB", "hh3cPBRNexthopAddrType"),
        ("HH3C-PBR-MIB", "hh3cPBRNexthopAddr"))
)
if mibBuilder.loadTexts:
    hh3cPBRNexthopFailedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PBR-MIB",
    **{"hh3cPBR": hh3cPBR,
       "hh3cPBRObjects": hh3cPBRObjects,
       "hh3cPBRGlobal": hh3cPBRGlobal,
       "hh3cPBRNexthopTrapEnabled": hh3cPBRNexthopTrapEnabled,
       "hh3cPBRLocalPolicy": hh3cPBRLocalPolicy,
       "hh3cPBRIPv6NexthopTrapEnabled": hh3cPBRIPv6NexthopTrapEnabled,
       "hh3cPBRMibTrap": hh3cPBRMibTrap,
       "hh3cPBRTrapObjects": hh3cPBRTrapObjects,
       "hh3cPBRNexthopAddrType": hh3cPBRNexthopAddrType,
       "hh3cPBRNexthopAddr": hh3cPBRNexthopAddr,
       "hh3cPBRTraps": hh3cPBRTraps,
       "hh3cPBRTrapsPrefix": hh3cPBRTrapsPrefix,
       "hh3cPBRNexthopFailedTrap": hh3cPBRNexthopFailedTrap,
       "hh3cPBRTables": hh3cPBRTables,
       "hh3cPBRMibPolicyNodeTable": hh3cPBRMibPolicyNodeTable,
       "hh3cPBRMibPolicyNodeEntry": hh3cPBRMibPolicyNodeEntry,
       "hh3cPBRMibPolicyNodeAddrType": hh3cPBRMibPolicyNodeAddrType,
       "hh3cPBRMibPolicyName": hh3cPBRMibPolicyName,
       "hh3cPBRMibPolicyNodeId": hh3cPBRMibPolicyNodeId,
       "hh3cPBRMibPolicyNodeMode": hh3cPBRMibPolicyNodeMode,
       "hh3cPBRMibPolicyNodeRowStatus": hh3cPBRMibPolicyNodeRowStatus,
       "hh3cPBRMibIfPolicyTable": hh3cPBRMibIfPolicyTable,
       "hh3cPBRMibIfPolicyEntry": hh3cPBRMibIfPolicyEntry,
       "hh3cPBRMibPolicyAddressType": hh3cPBRMibPolicyAddressType,
       "hh3cPBRMibAppliedPolicyName": hh3cPBRMibAppliedPolicyName,
       "hh3cPBRMibIfPolicyRowStatus": hh3cPBRMibIfPolicyRowStatus,
       "hh3cPBRMibMatchAclTable": hh3cPBRMibMatchAclTable,
       "hh3cPBRMibMatchAclEntry": hh3cPBRMibMatchAclEntry,
       "hh3cPBRMibAclGroupId": hh3cPBRMibAclGroupId,
       "hh3cPBRMibApplyPrecedenceTable": hh3cPBRMibApplyPrecedenceTable,
       "hh3cPBRMibApplyPrecedenceEntry": hh3cPBRMibApplyPrecedenceEntry,
       "hh3cPBRMibApplyPrecedenceValue": hh3cPBRMibApplyPrecedenceValue,
       "hh3cPBRMibApplyNexthopTable": hh3cPBRMibApplyNexthopTable,
       "hh3cPBRMibApplyNexthopEntry": hh3cPBRMibApplyNexthopEntry,
       "hh3cPBRMibApplyNexthopIndex": hh3cPBRMibApplyNexthopIndex,
       "hh3cPBRMibApplyNexthopVpnName": hh3cPBRMibApplyNexthopVpnName,
       "hh3cPBRMibApplyNexthopAddressType": hh3cPBRMibApplyNexthopAddressType,
       "hh3cPBRMibApplyNexthopAddress": hh3cPBRMibApplyNexthopAddress,
       "hh3cPBRMibApplyNexthopTrackId": hh3cPBRMibApplyNexthopTrackId,
       "hh3cPBRMibApplyNexthopDirect": hh3cPBRMibApplyNexthopDirect,
       "hh3cPBRMibApplyNexthopRowStatus": hh3cPBRMibApplyNexthopRowStatus,
       "hh3cPBRMibApplyDefaultNexthopTable": hh3cPBRMibApplyDefaultNexthopTable,
       "hh3cPBRMibApplyDefaultNexthopEntry": hh3cPBRMibApplyDefaultNexthopEntry,
       "hh3cPBRMibApplyDefaultNexthopIndex": hh3cPBRMibApplyDefaultNexthopIndex,
       "hh3cPBRMibApplyDefaultNexthopVpnName": hh3cPBRMibApplyDefaultNexthopVpnName,
       "hh3cPBRMibApplyDefaultNexthopAddressType": hh3cPBRMibApplyDefaultNexthopAddressType,
       "hh3cPBRMibApplyDefaultNexthopAddress": hh3cPBRMibApplyDefaultNexthopAddress,
       "hh3cPBRMibApplyDefaultNexthopTrackId": hh3cPBRMibApplyDefaultNexthopTrackId,
       "hh3cPBRMibApplyDefaultNexthopDirect": hh3cPBRMibApplyDefaultNexthopDirect,
       "hh3cPBRMibApplyDefaultNexthopRowStatus": hh3cPBRMibApplyDefaultNexthopRowStatus}
)
