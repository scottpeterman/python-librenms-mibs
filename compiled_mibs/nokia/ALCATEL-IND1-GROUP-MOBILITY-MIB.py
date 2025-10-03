# SNMP MIB module (ALCATEL-IND1-GROUP-MOBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-GROUP-MOBILITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:22 2025
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

(groupmobilityTraps,
 softentIND1GroupMobility) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "groupmobilityTraps",
    "softentIND1GroupMobility")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1GroupMobilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GroupMobilityMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1GroupMobilityMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1GroupMobilityMIBObjects = _AlcatelIND1GroupMobilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GroupMobilityMIBObjects.setStatus("current")
_GroupMobilityRule_ObjectIdentity = ObjectIdentity
groupMobilityRule = _GroupMobilityRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1)
)
_VIpNetRuleTable_Object = MibTable
vIpNetRuleTable = _VIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vIpNetRuleTable.setStatus("current")
_VIpNetRuleEntry_Object = MibTableRow
vIpNetRuleEntry = _VIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 1, 1)
)
vIpNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpNetRuleAddr"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpNetRuleMask"),
)
if mibBuilder.loadTexts:
    vIpNetRuleEntry.setStatus("current")
_VIpNetRuleAddr_Type = IpAddress
_VIpNetRuleAddr_Object = MibTableColumn
vIpNetRuleAddr = _VIpNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 1, 1, 1),
    _VIpNetRuleAddr_Type()
)
vIpNetRuleAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpNetRuleAddr.setStatus("current")
_VIpNetRuleMask_Type = IpAddress
_VIpNetRuleMask_Object = MibTableColumn
vIpNetRuleMask = _VIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 1, 1, 2),
    _VIpNetRuleMask_Type()
)
vIpNetRuleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpNetRuleMask.setStatus("current")


class _VIpNetRuleVlanId_Type(Integer32):
    """Custom type vIpNetRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VIpNetRuleVlanId_Type.__name__ = "Integer32"
_VIpNetRuleVlanId_Object = MibTableColumn
vIpNetRuleVlanId = _VIpNetRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 1, 1, 3),
    _VIpNetRuleVlanId_Type()
)
vIpNetRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpNetRuleVlanId.setStatus("current")
_VIpNetRuleStatus_Type = RowStatus
_VIpNetRuleStatus_Object = MibTableColumn
vIpNetRuleStatus = _VIpNetRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 1, 1, 4),
    _VIpNetRuleStatus_Type()
)
vIpNetRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpNetRuleStatus.setStatus("current")
_VIpxNetRuleTable_Object = MibTable
vIpxNetRuleTable = _VIpxNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vIpxNetRuleTable.setStatus("current")
_VIpxNetRuleEntry_Object = MibTableRow
vIpxNetRuleEntry = _VIpxNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 2, 1)
)
vIpxNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpxNetRuleAddr"),
)
if mibBuilder.loadTexts:
    vIpxNetRuleEntry.setStatus("current")


class _VIpxNetRuleAddr_Type(Unsigned32):
    """Custom type vIpxNetRuleAddr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_VIpxNetRuleAddr_Type.__name__ = "Unsigned32"
_VIpxNetRuleAddr_Object = MibTableColumn
vIpxNetRuleAddr = _VIpxNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 2, 1, 1),
    _VIpxNetRuleAddr_Type()
)
vIpxNetRuleAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpxNetRuleAddr.setStatus("current")


class _VIpxNetRuleEncap_Type(Integer32):
    """Custom type vIpxNetRuleEncap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet2", 1),
          ("novellraw", 2),
          ("llc", 3),
          ("snap", 4))
    )


_VIpxNetRuleEncap_Type.__name__ = "Integer32"
_VIpxNetRuleEncap_Object = MibTableColumn
vIpxNetRuleEncap = _VIpxNetRuleEncap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 2, 1, 2),
    _VIpxNetRuleEncap_Type()
)
vIpxNetRuleEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpxNetRuleEncap.setStatus("current")


class _VIpxNetRuleVlanId_Type(Integer32):
    """Custom type vIpxNetRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VIpxNetRuleVlanId_Type.__name__ = "Integer32"
_VIpxNetRuleVlanId_Object = MibTableColumn
vIpxNetRuleVlanId = _VIpxNetRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 2, 1, 3),
    _VIpxNetRuleVlanId_Type()
)
vIpxNetRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpxNetRuleVlanId.setStatus("current")
_VIpxNetRuleStatus_Type = RowStatus
_VIpxNetRuleStatus_Object = MibTableColumn
vIpxNetRuleStatus = _VIpxNetRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 2, 1, 4),
    _VIpxNetRuleStatus_Type()
)
vIpxNetRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpxNetRuleStatus.setStatus("current")
_VMacRuleTable_Object = MibTable
vMacRuleTable = _VMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vMacRuleTable.setStatus("current")
_VMacRuleEntry_Object = MibTableRow
vMacRuleEntry = _VMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 3, 1)
)
vMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRuleAddr"),
)
if mibBuilder.loadTexts:
    vMacRuleEntry.setStatus("current")
_VMacRuleAddr_Type = MacAddress
_VMacRuleAddr_Object = MibTableColumn
vMacRuleAddr = _VMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 3, 1, 1),
    _VMacRuleAddr_Type()
)
vMacRuleAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacRuleAddr.setStatus("current")


class _VMacRuleVlanId_Type(Integer32):
    """Custom type vMacRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VMacRuleVlanId_Type.__name__ = "Integer32"
_VMacRuleVlanId_Object = MibTableColumn
vMacRuleVlanId = _VMacRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 3, 1, 2),
    _VMacRuleVlanId_Type()
)
vMacRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacRuleVlanId.setStatus("current")
_VMacRuleStatus_Type = RowStatus
_VMacRuleStatus_Object = MibTableColumn
vMacRuleStatus = _VMacRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 3, 1, 3),
    _VMacRuleStatus_Type()
)
vMacRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacRuleStatus.setStatus("current")
_VMacRangeRuleTable_Object = MibTable
vMacRangeRuleTable = _VMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vMacRangeRuleTable.setStatus("current")
_VMacRangeRuleEntry_Object = MibTableRow
vMacRangeRuleEntry = _VMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 4, 1)
)
vMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    vMacRangeRuleEntry.setStatus("current")
_VMacRangeRuleLoAddr_Type = MacAddress
_VMacRangeRuleLoAddr_Object = MibTableColumn
vMacRangeRuleLoAddr = _VMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 4, 1, 1),
    _VMacRangeRuleLoAddr_Type()
)
vMacRangeRuleLoAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacRangeRuleLoAddr.setStatus("current")
_VMacRangeRuleHiAddr_Type = MacAddress
_VMacRangeRuleHiAddr_Object = MibTableColumn
vMacRangeRuleHiAddr = _VMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 4, 1, 2),
    _VMacRangeRuleHiAddr_Type()
)
vMacRangeRuleHiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacRangeRuleHiAddr.setStatus("current")


class _VMacRangeRuleVlanId_Type(Integer32):
    """Custom type vMacRangeRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VMacRangeRuleVlanId_Type.__name__ = "Integer32"
_VMacRangeRuleVlanId_Object = MibTableColumn
vMacRangeRuleVlanId = _VMacRangeRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 4, 1, 3),
    _VMacRangeRuleVlanId_Type()
)
vMacRangeRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacRangeRuleVlanId.setStatus("current")
_VMacRangeRuleStatus_Type = RowStatus
_VMacRangeRuleStatus_Object = MibTableColumn
vMacRangeRuleStatus = _VMacRangeRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 4, 1, 4),
    _VMacRangeRuleStatus_Type()
)
vMacRangeRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacRangeRuleStatus.setStatus("current")
_VMacPortIpBRuleTable_Object = MibTable
vMacPortIpBRuleTable = _VMacPortIpBRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    vMacPortIpBRuleTable.setStatus("current")
_VMacPortIpBRuleEntry_Object = MibTableRow
vMacPortIpBRuleEntry = _VMacPortIpBRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 5, 1)
)
vMacPortIpBRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortIpBRuleMac"),
)
if mibBuilder.loadTexts:
    vMacPortIpBRuleEntry.setStatus("current")
_VMacPortIpBRuleMac_Type = MacAddress
_VMacPortIpBRuleMac_Object = MibTableColumn
vMacPortIpBRuleMac = _VMacPortIpBRuleMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 5, 1, 1),
    _VMacPortIpBRuleMac_Type()
)
vMacPortIpBRuleMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortIpBRuleMac.setStatus("current")


class _VMacPortIpBRuleIfIndex_Type(Unsigned32):
    """Custom type vMacPortIpBRuleIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VMacPortIpBRuleIfIndex_Type.__name__ = "Unsigned32"
_VMacPortIpBRuleIfIndex_Object = MibTableColumn
vMacPortIpBRuleIfIndex = _VMacPortIpBRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 5, 1, 2),
    _VMacPortIpBRuleIfIndex_Type()
)
vMacPortIpBRuleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortIpBRuleIfIndex.setStatus("current")
_VMacPortIpBRuleIp_Type = IpAddress
_VMacPortIpBRuleIp_Object = MibTableColumn
vMacPortIpBRuleIp = _VMacPortIpBRuleIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 5, 1, 3),
    _VMacPortIpBRuleIp_Type()
)
vMacPortIpBRuleIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortIpBRuleIp.setStatus("current")


class _VMacPortIpBRuleVlanId_Type(Integer32):
    """Custom type vMacPortIpBRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VMacPortIpBRuleVlanId_Type.__name__ = "Integer32"
_VMacPortIpBRuleVlanId_Object = MibTableColumn
vMacPortIpBRuleVlanId = _VMacPortIpBRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 5, 1, 4),
    _VMacPortIpBRuleVlanId_Type()
)
vMacPortIpBRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortIpBRuleVlanId.setStatus("current")
_VMacPortIpBRuleStatus_Type = RowStatus
_VMacPortIpBRuleStatus_Object = MibTableColumn
vMacPortIpBRuleStatus = _VMacPortIpBRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 5, 1, 5),
    _VMacPortIpBRuleStatus_Type()
)
vMacPortIpBRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortIpBRuleStatus.setStatus("current")
_VPortIpBRuleTable_Object = MibTable
vPortIpBRuleTable = _VPortIpBRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    vPortIpBRuleTable.setStatus("current")
_VPortIpBRuleEntry_Object = MibTableRow
vPortIpBRuleEntry = _VPortIpBRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 6, 1)
)
vPortIpBRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortIpBRuleIp"),
)
if mibBuilder.loadTexts:
    vPortIpBRuleEntry.setStatus("current")
_VPortIpBRuleIp_Type = IpAddress
_VPortIpBRuleIp_Object = MibTableColumn
vPortIpBRuleIp = _VPortIpBRuleIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 6, 1, 1),
    _VPortIpBRuleIp_Type()
)
vPortIpBRuleIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortIpBRuleIp.setStatus("current")


class _VPortIpBRuleIfIndex_Type(Unsigned32):
    """Custom type vPortIpBRuleIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VPortIpBRuleIfIndex_Type.__name__ = "Unsigned32"
_VPortIpBRuleIfIndex_Object = MibTableColumn
vPortIpBRuleIfIndex = _VPortIpBRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 6, 1, 2),
    _VPortIpBRuleIfIndex_Type()
)
vPortIpBRuleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortIpBRuleIfIndex.setStatus("current")


class _VPortIpBRuleVlanId_Type(Integer32):
    """Custom type vPortIpBRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VPortIpBRuleVlanId_Type.__name__ = "Integer32"
_VPortIpBRuleVlanId_Object = MibTableColumn
vPortIpBRuleVlanId = _VPortIpBRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 6, 1, 3),
    _VPortIpBRuleVlanId_Type()
)
vPortIpBRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortIpBRuleVlanId.setStatus("current")
_VPortIpBRuleStatus_Type = RowStatus
_VPortIpBRuleStatus_Object = MibTableColumn
vPortIpBRuleStatus = _VPortIpBRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 6, 1, 4),
    _VPortIpBRuleStatus_Type()
)
vPortIpBRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortIpBRuleStatus.setStatus("current")
_VMacIpBRuleTable_Object = MibTable
vMacIpBRuleTable = _VMacIpBRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    vMacIpBRuleTable.setStatus("current")
_VMacIpBRuleEntry_Object = MibTableRow
vMacIpBRuleEntry = _VMacIpBRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 7, 1)
)
vMacIpBRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacIpBRuleMac"),
)
if mibBuilder.loadTexts:
    vMacIpBRuleEntry.setStatus("current")
_VMacIpBRuleMac_Type = MacAddress
_VMacIpBRuleMac_Object = MibTableColumn
vMacIpBRuleMac = _VMacIpBRuleMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 7, 1, 1),
    _VMacIpBRuleMac_Type()
)
vMacIpBRuleMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacIpBRuleMac.setStatus("current")
_VMacIpBRuleIp_Type = IpAddress
_VMacIpBRuleIp_Object = MibTableColumn
vMacIpBRuleIp = _VMacIpBRuleIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 7, 1, 2),
    _VMacIpBRuleIp_Type()
)
vMacIpBRuleIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacIpBRuleIp.setStatus("current")


class _VMacIpBRuleVlanId_Type(Integer32):
    """Custom type vMacIpBRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VMacIpBRuleVlanId_Type.__name__ = "Integer32"
_VMacIpBRuleVlanId_Object = MibTableColumn
vMacIpBRuleVlanId = _VMacIpBRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 7, 1, 3),
    _VMacIpBRuleVlanId_Type()
)
vMacIpBRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacIpBRuleVlanId.setStatus("current")
_VMacIpBRuleStatus_Type = RowStatus
_VMacIpBRuleStatus_Object = MibTableColumn
vMacIpBRuleStatus = _VMacIpBRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 7, 1, 4),
    _VMacIpBRuleStatus_Type()
)
vMacIpBRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacIpBRuleStatus.setStatus("current")
_VMacPortBRuleTable_Object = MibTable
vMacPortBRuleTable = _VMacPortBRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    vMacPortBRuleTable.setStatus("current")
_VMacPortBRuleEntry_Object = MibTableRow
vMacPortBRuleEntry = _VMacPortBRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 8, 1)
)
vMacPortBRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortBRuleMac"),
)
if mibBuilder.loadTexts:
    vMacPortBRuleEntry.setStatus("current")
_VMacPortBRuleMac_Type = MacAddress
_VMacPortBRuleMac_Object = MibTableColumn
vMacPortBRuleMac = _VMacPortBRuleMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 8, 1, 1),
    _VMacPortBRuleMac_Type()
)
vMacPortBRuleMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortBRuleMac.setStatus("current")


class _VMacPortBRuleIfIndex_Type(Unsigned32):
    """Custom type vMacPortBRuleIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VMacPortBRuleIfIndex_Type.__name__ = "Unsigned32"
_VMacPortBRuleIfIndex_Object = MibTableColumn
vMacPortBRuleIfIndex = _VMacPortBRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 8, 1, 2),
    _VMacPortBRuleIfIndex_Type()
)
vMacPortBRuleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortBRuleIfIndex.setStatus("current")


class _VMacPortBRuleVlanId_Type(Integer32):
    """Custom type vMacPortBRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VMacPortBRuleVlanId_Type.__name__ = "Integer32"
_VMacPortBRuleVlanId_Object = MibTableColumn
vMacPortBRuleVlanId = _VMacPortBRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 8, 1, 3),
    _VMacPortBRuleVlanId_Type()
)
vMacPortBRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortBRuleVlanId.setStatus("current")
_VMacPortBRuleStatus_Type = RowStatus
_VMacPortBRuleStatus_Object = MibTableColumn
vMacPortBRuleStatus = _VMacPortBRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 8, 1, 4),
    _VMacPortBRuleStatus_Type()
)
vMacPortBRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortBRuleStatus.setStatus("current")
_VMacPortProtoBRuleTable_Object = MibTable
vMacPortProtoBRuleTable = _VMacPortProtoBRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    vMacPortProtoBRuleTable.setStatus("current")
_VMacPortProtoBRuleEntry_Object = MibTableRow
vMacPortProtoBRuleEntry = _VMacPortProtoBRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1)
)
vMacPortProtoBRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleMacAddr"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleProtoClass"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleEthertype"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleDsapSsap"),
)
if mibBuilder.loadTexts:
    vMacPortProtoBRuleEntry.setStatus("current")
_VMacPortProtoBRuleMacAddr_Type = MacAddress
_VMacPortProtoBRuleMacAddr_Object = MibTableColumn
vMacPortProtoBRuleMacAddr = _VMacPortProtoBRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1, 1),
    _VMacPortProtoBRuleMacAddr_Type()
)
vMacPortProtoBRuleMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortProtoBRuleMacAddr.setStatus("current")


class _VMacPortProtoBRuleIfIndex_Type(Unsigned32):
    """Custom type vMacPortProtoBRuleIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VMacPortProtoBRuleIfIndex_Type.__name__ = "Unsigned32"
_VMacPortProtoBRuleIfIndex_Object = MibTableColumn
vMacPortProtoBRuleIfIndex = _VMacPortProtoBRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1, 2),
    _VMacPortProtoBRuleIfIndex_Type()
)
vMacPortProtoBRuleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortProtoBRuleIfIndex.setStatus("current")


class _VMacPortProtoBRuleProtoClass_Type(Integer32):
    """Custom type vMacPortProtoBRuleProtoClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ipE2", 1),
          ("ipSnap", 2),
          ("ipxE2", 3),
          ("ipxNov", 4),
          ("ipxLlc", 5),
          ("ipxSnap", 6),
          ("decnet", 7),
          ("appletalk", 8),
          ("ethertypeE2", 9),
          ("dsapSsap", 10),
          ("ethertypeSnap", 11))
    )


_VMacPortProtoBRuleProtoClass_Type.__name__ = "Integer32"
_VMacPortProtoBRuleProtoClass_Object = MibTableColumn
vMacPortProtoBRuleProtoClass = _VMacPortProtoBRuleProtoClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1, 3),
    _VMacPortProtoBRuleProtoClass_Type()
)
vMacPortProtoBRuleProtoClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortProtoBRuleProtoClass.setStatus("current")


class _VMacPortProtoBRuleEthertype_Type(Integer32):
    """Custom type vMacPortProtoBRuleEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_VMacPortProtoBRuleEthertype_Type.__name__ = "Integer32"
_VMacPortProtoBRuleEthertype_Object = MibTableColumn
vMacPortProtoBRuleEthertype = _VMacPortProtoBRuleEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1, 4),
    _VMacPortProtoBRuleEthertype_Type()
)
vMacPortProtoBRuleEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortProtoBRuleEthertype.setStatus("current")


class _VMacPortProtoBRuleDsapSsap_Type(Integer32):
    """Custom type vMacPortProtoBRuleDsapSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VMacPortProtoBRuleDsapSsap_Type.__name__ = "Integer32"
_VMacPortProtoBRuleDsapSsap_Object = MibTableColumn
vMacPortProtoBRuleDsapSsap = _VMacPortProtoBRuleDsapSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1, 5),
    _VMacPortProtoBRuleDsapSsap_Type()
)
vMacPortProtoBRuleDsapSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortProtoBRuleDsapSsap.setStatus("current")


class _VMacPortProtoBRuleVlanId_Type(Integer32):
    """Custom type vMacPortProtoBRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VMacPortProtoBRuleVlanId_Type.__name__ = "Integer32"
_VMacPortProtoBRuleVlanId_Object = MibTableColumn
vMacPortProtoBRuleVlanId = _VMacPortProtoBRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1, 6),
    _VMacPortProtoBRuleVlanId_Type()
)
vMacPortProtoBRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortProtoBRuleVlanId.setStatus("current")
_VMacPortProtoBRuleStatus_Type = RowStatus
_VMacPortProtoBRuleStatus_Object = MibTableColumn
vMacPortProtoBRuleStatus = _VMacPortProtoBRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 9, 1, 7),
    _VMacPortProtoBRuleStatus_Type()
)
vMacPortProtoBRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMacPortProtoBRuleStatus.setStatus("current")
_VPortProtoBRuleTable_Object = MibTable
vPortProtoBRuleTable = _VPortProtoBRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    vPortProtoBRuleTable.setStatus("current")
_VPortProtoBRuleEntry_Object = MibTableRow
vPortProtoBRuleEntry = _VPortProtoBRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10, 1)
)
vPortProtoBRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleIfIndex"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleProtoClass"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleEthertype"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleDsapSsap"),
)
if mibBuilder.loadTexts:
    vPortProtoBRuleEntry.setStatus("current")


class _VPortProtoBRuleIfIndex_Type(Unsigned32):
    """Custom type vPortProtoBRuleIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VPortProtoBRuleIfIndex_Type.__name__ = "Unsigned32"
_VPortProtoBRuleIfIndex_Object = MibTableColumn
vPortProtoBRuleIfIndex = _VPortProtoBRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10, 1, 1),
    _VPortProtoBRuleIfIndex_Type()
)
vPortProtoBRuleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortProtoBRuleIfIndex.setStatus("current")


class _VPortProtoBRuleProtoClass_Type(Integer32):
    """Custom type vPortProtoBRuleProtoClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ipE2", 1),
          ("ipSnap", 2),
          ("ipxE2", 3),
          ("ipxNov", 4),
          ("ipxLlc", 5),
          ("ipxSnap", 6),
          ("decnet", 7),
          ("appletalk", 8),
          ("ethertypeE2", 9),
          ("dsapSsap", 10),
          ("ethertypeSnap", 11),
          ("ipv6", 12))
    )


_VPortProtoBRuleProtoClass_Type.__name__ = "Integer32"
_VPortProtoBRuleProtoClass_Object = MibTableColumn
vPortProtoBRuleProtoClass = _VPortProtoBRuleProtoClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10, 1, 2),
    _VPortProtoBRuleProtoClass_Type()
)
vPortProtoBRuleProtoClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortProtoBRuleProtoClass.setStatus("current")


class _VPortProtoBRuleEthertype_Type(Integer32):
    """Custom type vPortProtoBRuleEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1536, 65535),
    )


_VPortProtoBRuleEthertype_Type.__name__ = "Integer32"
_VPortProtoBRuleEthertype_Object = MibTableColumn
vPortProtoBRuleEthertype = _VPortProtoBRuleEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10, 1, 3),
    _VPortProtoBRuleEthertype_Type()
)
vPortProtoBRuleEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortProtoBRuleEthertype.setStatus("current")


class _VPortProtoBRuleDsapSsap_Type(Integer32):
    """Custom type vPortProtoBRuleDsapSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VPortProtoBRuleDsapSsap_Type.__name__ = "Integer32"
_VPortProtoBRuleDsapSsap_Object = MibTableColumn
vPortProtoBRuleDsapSsap = _VPortProtoBRuleDsapSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10, 1, 4),
    _VPortProtoBRuleDsapSsap_Type()
)
vPortProtoBRuleDsapSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortProtoBRuleDsapSsap.setStatus("current")


class _VPortProtoBRuleVlanId_Type(Integer32):
    """Custom type vPortProtoBRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VPortProtoBRuleVlanId_Type.__name__ = "Integer32"
_VPortProtoBRuleVlanId_Object = MibTableColumn
vPortProtoBRuleVlanId = _VPortProtoBRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10, 1, 5),
    _VPortProtoBRuleVlanId_Type()
)
vPortProtoBRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortProtoBRuleVlanId.setStatus("current")
_VPortProtoBRuleStatus_Type = RowStatus
_VPortProtoBRuleStatus_Object = MibTableColumn
vPortProtoBRuleStatus = _VPortProtoBRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 10, 1, 6),
    _VPortProtoBRuleStatus_Type()
)
vPortProtoBRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortProtoBRuleStatus.setStatus("current")
_VDhcpMacRuleTable_Object = MibTable
vDhcpMacRuleTable = _VDhcpMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    vDhcpMacRuleTable.setStatus("current")
_VDhcpMacRuleEntry_Object = MibTableRow
vDhcpMacRuleEntry = _VDhcpMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 11, 1)
)
vDhcpMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRuleAddr"),
)
if mibBuilder.loadTexts:
    vDhcpMacRuleEntry.setStatus("current")
_VDhcpMacRuleAddr_Type = MacAddress
_VDhcpMacRuleAddr_Object = MibTableColumn
vDhcpMacRuleAddr = _VDhcpMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 11, 1, 1),
    _VDhcpMacRuleAddr_Type()
)
vDhcpMacRuleAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpMacRuleAddr.setStatus("current")


class _VDhcpMacRuleVlanId_Type(Integer32):
    """Custom type vDhcpMacRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VDhcpMacRuleVlanId_Type.__name__ = "Integer32"
_VDhcpMacRuleVlanId_Object = MibTableColumn
vDhcpMacRuleVlanId = _VDhcpMacRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 11, 1, 2),
    _VDhcpMacRuleVlanId_Type()
)
vDhcpMacRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpMacRuleVlanId.setStatus("current")
_VDhcpMacRuleStatus_Type = RowStatus
_VDhcpMacRuleStatus_Object = MibTableColumn
vDhcpMacRuleStatus = _VDhcpMacRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 11, 1, 3),
    _VDhcpMacRuleStatus_Type()
)
vDhcpMacRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpMacRuleStatus.setStatus("current")
_VDhcpPortRuleTable_Object = MibTable
vDhcpPortRuleTable = _VDhcpPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    vDhcpPortRuleTable.setStatus("current")
_VDhcpPortRuleEntry_Object = MibTableRow
vDhcpPortRuleEntry = _VDhcpPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 12, 1)
)
vDhcpPortRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpPortRuleIfIndex"),
)
if mibBuilder.loadTexts:
    vDhcpPortRuleEntry.setStatus("current")


class _VDhcpPortRuleIfIndex_Type(Unsigned32):
    """Custom type vDhcpPortRuleIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VDhcpPortRuleIfIndex_Type.__name__ = "Unsigned32"
_VDhcpPortRuleIfIndex_Object = MibTableColumn
vDhcpPortRuleIfIndex = _VDhcpPortRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 12, 1, 1),
    _VDhcpPortRuleIfIndex_Type()
)
vDhcpPortRuleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpPortRuleIfIndex.setStatus("current")


class _VDhcpPortRuleVlanId_Type(Integer32):
    """Custom type vDhcpPortRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VDhcpPortRuleVlanId_Type.__name__ = "Integer32"
_VDhcpPortRuleVlanId_Object = MibTableColumn
vDhcpPortRuleVlanId = _VDhcpPortRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 12, 1, 2),
    _VDhcpPortRuleVlanId_Type()
)
vDhcpPortRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpPortRuleVlanId.setStatus("current")
_VDhcpPortRuleStatus_Type = RowStatus
_VDhcpPortRuleStatus_Object = MibTableColumn
vDhcpPortRuleStatus = _VDhcpPortRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 12, 1, 3),
    _VDhcpPortRuleStatus_Type()
)
vDhcpPortRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpPortRuleStatus.setStatus("current")
_VDhcpGenericRuleTable_Object = MibTable
vDhcpGenericRuleTable = _VDhcpGenericRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    vDhcpGenericRuleTable.setStatus("current")
_VDhcpGenericRuleEntry_Object = MibTableRow
vDhcpGenericRuleEntry = _VDhcpGenericRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 13, 1)
)
vDhcpGenericRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpGenericRuleVlanId"),
)
if mibBuilder.loadTexts:
    vDhcpGenericRuleEntry.setStatus("current")


class _VDhcpGenericRuleVlanId_Type(Integer32):
    """Custom type vDhcpGenericRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VDhcpGenericRuleVlanId_Type.__name__ = "Integer32"
_VDhcpGenericRuleVlanId_Object = MibTableColumn
vDhcpGenericRuleVlanId = _VDhcpGenericRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 13, 1, 1),
    _VDhcpGenericRuleVlanId_Type()
)
vDhcpGenericRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpGenericRuleVlanId.setStatus("current")
_VDhcpGenericRuleStatus_Type = RowStatus
_VDhcpGenericRuleStatus_Object = MibTableColumn
vDhcpGenericRuleStatus = _VDhcpGenericRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 13, 1, 2),
    _VDhcpGenericRuleStatus_Type()
)
vDhcpGenericRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpGenericRuleStatus.setStatus("current")
_VProtoRuleTable_Object = MibTable
vProtoRuleTable = _VProtoRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    vProtoRuleTable.setStatus("current")
_VProtoRuleEntry_Object = MibTableRow
vProtoRuleEntry = _VProtoRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 14, 1)
)
vProtoRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleProtoClass"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleEthertype"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleDsapSsap"),
)
if mibBuilder.loadTexts:
    vProtoRuleEntry.setStatus("current")


class _VProtoRuleProtoClass_Type(Integer32):
    """Custom type vProtoRuleProtoClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ipE2", 1),
          ("ipSnap", 2),
          ("ipxE2", 3),
          ("ipxNov", 4),
          ("ipxLlc", 5),
          ("ipxSnap", 6),
          ("decnet", 7),
          ("appletalk", 8),
          ("ethertypeE2", 9),
          ("dsapSsap", 10),
          ("ethertypeSnap", 11),
          ("ipv6", 12))
    )


_VProtoRuleProtoClass_Type.__name__ = "Integer32"
_VProtoRuleProtoClass_Object = MibTableColumn
vProtoRuleProtoClass = _VProtoRuleProtoClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 14, 1, 1),
    _VProtoRuleProtoClass_Type()
)
vProtoRuleProtoClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProtoRuleProtoClass.setStatus("current")


class _VProtoRuleEthertype_Type(Integer32):
    """Custom type vProtoRuleEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_VProtoRuleEthertype_Type.__name__ = "Integer32"
_VProtoRuleEthertype_Object = MibTableColumn
vProtoRuleEthertype = _VProtoRuleEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 14, 1, 2),
    _VProtoRuleEthertype_Type()
)
vProtoRuleEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProtoRuleEthertype.setStatus("current")


class _VProtoRuleDsapSsap_Type(Integer32):
    """Custom type vProtoRuleDsapSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VProtoRuleDsapSsap_Type.__name__ = "Integer32"
_VProtoRuleDsapSsap_Object = MibTableColumn
vProtoRuleDsapSsap = _VProtoRuleDsapSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 14, 1, 3),
    _VProtoRuleDsapSsap_Type()
)
vProtoRuleDsapSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProtoRuleDsapSsap.setStatus("current")


class _VProtoRuleVlanId_Type(Integer32):
    """Custom type vProtoRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VProtoRuleVlanId_Type.__name__ = "Integer32"
_VProtoRuleVlanId_Object = MibTableColumn
vProtoRuleVlanId = _VProtoRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 14, 1, 4),
    _VProtoRuleVlanId_Type()
)
vProtoRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProtoRuleVlanId.setStatus("current")
_VProtoRuleStatus_Type = RowStatus
_VProtoRuleStatus_Object = MibTableColumn
vProtoRuleStatus = _VProtoRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 14, 1, 5),
    _VProtoRuleStatus_Type()
)
vProtoRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProtoRuleStatus.setStatus("current")
_VCustomRuleTable_Object = MibTable
vCustomRuleTable = _VCustomRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    vCustomRuleTable.setStatus("current")
_VCustomRuleEntry_Object = MibTableRow
vCustomRuleEntry = _VCustomRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 15, 1)
)
vCustomRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vCustomRuleOffset"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vCustomRuleValue"),
)
if mibBuilder.loadTexts:
    vCustomRuleEntry.setStatus("current")


class _VCustomRuleValue_Type(Unsigned32):
    """Custom type vCustomRuleValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VCustomRuleValue_Type.__name__ = "Unsigned32"
_VCustomRuleValue_Object = MibTableColumn
vCustomRuleValue = _VCustomRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 15, 1, 1),
    _VCustomRuleValue_Type()
)
vCustomRuleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vCustomRuleValue.setStatus("current")


class _VCustomRuleMask_Type(Unsigned32):
    """Custom type vCustomRuleMask based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VCustomRuleMask_Type.__name__ = "Unsigned32"
_VCustomRuleMask_Object = MibTableColumn
vCustomRuleMask = _VCustomRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 15, 1, 2),
    _VCustomRuleMask_Type()
)
vCustomRuleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vCustomRuleMask.setStatus("current")


class _VCustomRuleOffset_Type(Integer32):
    """Custom type vCustomRuleOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 72),
    )


_VCustomRuleOffset_Type.__name__ = "Integer32"
_VCustomRuleOffset_Object = MibTableColumn
vCustomRuleOffset = _VCustomRuleOffset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 15, 1, 3),
    _VCustomRuleOffset_Type()
)
vCustomRuleOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vCustomRuleOffset.setStatus("current")


class _VCustomRuleVlanId_Type(Integer32):
    """Custom type vCustomRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VCustomRuleVlanId_Type.__name__ = "Integer32"
_VCustomRuleVlanId_Object = MibTableColumn
vCustomRuleVlanId = _VCustomRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 15, 1, 4),
    _VCustomRuleVlanId_Type()
)
vCustomRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vCustomRuleVlanId.setStatus("current")
_VCustomRuleStatus_Type = RowStatus
_VCustomRuleStatus_Object = MibTableColumn
vCustomRuleStatus = _VCustomRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 15, 1, 5),
    _VCustomRuleStatus_Type()
)
vCustomRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vCustomRuleStatus.setStatus("current")
_VPortRuleTable_Object = MibTable
vPortRuleTable = _VPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    vPortRuleTable.setStatus("current")
_VPortRuleEntry_Object = MibTableRow
vPortRuleEntry = _VPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 16, 1)
)
vPortRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortRuleIfIndex"),
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortRuleVlanId"),
)
if mibBuilder.loadTexts:
    vPortRuleEntry.setStatus("current")


class _VPortRuleIfIndex_Type(Unsigned32):
    """Custom type vPortRuleIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VPortRuleIfIndex_Type.__name__ = "Unsigned32"
_VPortRuleIfIndex_Object = MibTableColumn
vPortRuleIfIndex = _VPortRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 16, 1, 1),
    _VPortRuleIfIndex_Type()
)
vPortRuleIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortRuleIfIndex.setStatus("current")


class _VPortRuleVlanId_Type(Integer32):
    """Custom type vPortRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VPortRuleVlanId_Type.__name__ = "Integer32"
_VPortRuleVlanId_Object = MibTableColumn
vPortRuleVlanId = _VPortRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 16, 1, 2),
    _VPortRuleVlanId_Type()
)
vPortRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortRuleVlanId.setStatus("current")
_VPortRuleStatus_Type = RowStatus
_VPortRuleStatus_Object = MibTableColumn
vPortRuleStatus = _VPortRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 16, 1, 3),
    _VPortRuleStatus_Type()
)
vPortRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortRuleStatus.setStatus("current")
_VDhcpMacRangeRuleTable_Object = MibTable
vDhcpMacRangeRuleTable = _VDhcpMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    vDhcpMacRangeRuleTable.setStatus("current")
_VDhcpMacRangeRuleEntry_Object = MibTableRow
vDhcpMacRangeRuleEntry = _VDhcpMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 17, 1)
)
vDhcpMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    vDhcpMacRangeRuleEntry.setStatus("current")
_VDhcpMacRangeRuleLoAddr_Type = MacAddress
_VDhcpMacRangeRuleLoAddr_Object = MibTableColumn
vDhcpMacRangeRuleLoAddr = _VDhcpMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 17, 1, 1),
    _VDhcpMacRangeRuleLoAddr_Type()
)
vDhcpMacRangeRuleLoAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpMacRangeRuleLoAddr.setStatus("current")
_VDhcpMacRangeRuleHiAddr_Type = MacAddress
_VDhcpMacRangeRuleHiAddr_Object = MibTableColumn
vDhcpMacRangeRuleHiAddr = _VDhcpMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 17, 1, 2),
    _VDhcpMacRangeRuleHiAddr_Type()
)
vDhcpMacRangeRuleHiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpMacRangeRuleHiAddr.setStatus("current")


class _VDhcpMacRangeRuleVlanId_Type(Integer32):
    """Custom type vDhcpMacRangeRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VDhcpMacRangeRuleVlanId_Type.__name__ = "Integer32"
_VDhcpMacRangeRuleVlanId_Object = MibTableColumn
vDhcpMacRangeRuleVlanId = _VDhcpMacRangeRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 17, 1, 3),
    _VDhcpMacRangeRuleVlanId_Type()
)
vDhcpMacRangeRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpMacRangeRuleVlanId.setStatus("current")
_VDhcpMacRangeRuleStatus_Type = RowStatus
_VDhcpMacRangeRuleStatus_Object = MibTableColumn
vDhcpMacRangeRuleStatus = _VDhcpMacRangeRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 1, 17, 1, 4),
    _VDhcpMacRangeRuleStatus_Type()
)
vDhcpMacRangeRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDhcpMacRangeRuleStatus.setStatus("current")
_GroupMobilityPort_ObjectIdentity = ObjectIdentity
groupMobilityPort = _GroupMobilityPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2)
)
_VMobilePortTable_Object = MibTable
vMobilePortTable = _VMobilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vMobilePortTable.setStatus("current")
_VMobilePortEntry_Object = MibTableRow
vMobilePortEntry = _VMobilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1)
)
vMobilePortEntry.setIndexNames(
    (0, "ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortIfIndex"),
)
if mibBuilder.loadTexts:
    vMobilePortEntry.setStatus("current")


class _VMobilePortIfIndex_Type(Unsigned32):
    """Custom type vMobilePortIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VMobilePortIfIndex_Type.__name__ = "Unsigned32"
_VMobilePortIfIndex_Object = MibTableColumn
vMobilePortIfIndex = _VMobilePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 1),
    _VMobilePortIfIndex_Type()
)
vMobilePortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMobilePortIfIndex.setStatus("current")


class _VMobilePortMobility_Type(Integer32):
    """Custom type vMobilePortMobility based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VMobilePortMobility_Type.__name__ = "Integer32"
_VMobilePortMobility_Object = MibTableColumn
vMobilePortMobility = _VMobilePortMobility_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 2),
    _VMobilePortMobility_Type()
)
vMobilePortMobility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMobilePortMobility.setStatus("current")


class _VMobilePortDefVlanRestore_Type(Integer32):
    """Custom type vMobilePortDefVlanRestore based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notApplicable", 3))
    )


_VMobilePortDefVlanRestore_Type.__name__ = "Integer32"
_VMobilePortDefVlanRestore_Object = MibTableColumn
vMobilePortDefVlanRestore = _VMobilePortDefVlanRestore_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 3),
    _VMobilePortDefVlanRestore_Type()
)
vMobilePortDefVlanRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMobilePortDefVlanRestore.setStatus("current")


class _VMobilePortDefVlanEnable_Type(Integer32):
    """Custom type vMobilePortDefVlanEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notApplicable", 3))
    )


_VMobilePortDefVlanEnable_Type.__name__ = "Integer32"
_VMobilePortDefVlanEnable_Object = MibTableColumn
vMobilePortDefVlanEnable = _VMobilePortDefVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 4),
    _VMobilePortDefVlanEnable_Type()
)
vMobilePortDefVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMobilePortDefVlanEnable.setStatus("current")


class _VMobilePortIgnoreBPDU_Type(Integer32):
    """Custom type vMobilePortIgnoreBPDU based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notApplicable", 3))
    )


_VMobilePortIgnoreBPDU_Type.__name__ = "Integer32"
_VMobilePortIgnoreBPDU_Object = MibTableColumn
vMobilePortIgnoreBPDU = _VMobilePortIgnoreBPDU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 5),
    _VMobilePortIgnoreBPDU_Type()
)
vMobilePortIgnoreBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMobilePortIgnoreBPDU.setStatus("current")


class _VMobilePortAuthenticate_Type(Integer32):
    """Custom type vMobilePortAuthenticate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enableAvlan", 1),
          ("disable", 2),
          ("notApplicable", 3),
          ("enable8021x", 4))
    )


_VMobilePortAuthenticate_Type.__name__ = "Integer32"
_VMobilePortAuthenticate_Object = MibTableColumn
vMobilePortAuthenticate = _VMobilePortAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 6),
    _VMobilePortAuthenticate_Type()
)
vMobilePortAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMobilePortAuthenticate.setStatus("current")


class _VMobilePortCfgDefVlan_Type(Integer32):
    """Custom type vMobilePortCfgDefVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VMobilePortCfgDefVlan_Type.__name__ = "Integer32"
_VMobilePortCfgDefVlan_Object = MibTableColumn
vMobilePortCfgDefVlan = _VMobilePortCfgDefVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 7),
    _VMobilePortCfgDefVlan_Type()
)
vMobilePortCfgDefVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vMobilePortCfgDefVlan.setStatus("current")


class _VMobilePortIngressFiltering_Type(Integer32):
    """Custom type vMobilePortIngressFiltering based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VMobilePortIngressFiltering_Type.__name__ = "Integer32"
_VMobilePortIngressFiltering_Object = MibTableColumn
vMobilePortIngressFiltering = _VMobilePortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 1, 2, 1, 1, 8),
    _VMobilePortIngressFiltering_Type()
)
vMobilePortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vMobilePortIngressFiltering.setStatus("current")
_AlcatelIND1GroupMobilityMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1GroupMobilityMIBConformance = _AlcatelIND1GroupMobilityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1GroupMobilityMIBConformance.setStatus("current")
_AlcatelIND1GroupMobilityMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1GroupMobilityMIBGroups = _AlcatelIND1GroupMobilityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GroupMobilityMIBGroups.setStatus("current")
_AlcatelIND1GroupMobilityMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1GroupMobilityMIBCompliances = _AlcatelIND1GroupMobilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1GroupMobilityMIBCompliances.setStatus("current")
_GroupmobilityTrapsDesc_ObjectIdentity = ObjectIdentity
groupmobilityTrapsDesc = _GroupmobilityTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 1)
)
_GroupmobilityTrapsObj_ObjectIdentity = ObjectIdentity
groupmobilityTrapsObj = _GroupmobilityTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2)
)


class _GmBindRuleType_Type(Integer32):
    """Custom type gmBindRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("macPortIp", 9),
          ("portIp", 10),
          ("macIp", 11),
          ("macPort", 12),
          ("macPortProto", 13))
    )


_GmBindRuleType_Type.__name__ = "Integer32"
_GmBindRuleType_Object = MibScalar
gmBindRuleType = _GmBindRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 1),
    _GmBindRuleType_Type()
)
gmBindRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmBindRuleType.setStatus("current")
_GmBindRuleVlanId_Type = Unsigned32
_GmBindRuleVlanId_Object = MibScalar
gmBindRuleVlanId = _GmBindRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 2),
    _GmBindRuleVlanId_Type()
)
gmBindRuleVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmBindRuleVlanId.setStatus("current")
_GmBindRuleIPAddress_Type = IpAddress
_GmBindRuleIPAddress_Object = MibScalar
gmBindRuleIPAddress = _GmBindRuleIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 3),
    _GmBindRuleIPAddress_Type()
)
gmBindRuleIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmBindRuleIPAddress.setStatus("current")
_GmBindRuleMacAddress_Type = MacAddress
_GmBindRuleMacAddress_Object = MibScalar
gmBindRuleMacAddress = _GmBindRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 4),
    _GmBindRuleMacAddress_Type()
)
gmBindRuleMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmBindRuleMacAddress.setStatus("current")


class _GmBindRulePortIfIndex_Type(Unsigned32):
    """Custom type gmBindRulePortIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_GmBindRulePortIfIndex_Type.__name__ = "Unsigned32"
_GmBindRulePortIfIndex_Object = MibScalar
gmBindRulePortIfIndex = _GmBindRulePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 5),
    _GmBindRulePortIfIndex_Type()
)
gmBindRulePortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmBindRulePortIfIndex.setStatus("current")


class _GmBindRuleProtoClass_Type(Integer32):
    """Custom type gmBindRuleProtoClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ipE2", 1),
          ("ipSnap", 2),
          ("ipxE2", 3),
          ("ipxNov", 4),
          ("ipxLlc", 5),
          ("ipxSnap", 6),
          ("decnet", 7),
          ("appletalk", 8),
          ("ethertypeE2", 9),
          ("dsapSsap", 10),
          ("ethertypeSnap", 11),
          ("ipv6", 12))
    )


_GmBindRuleProtoClass_Type.__name__ = "Integer32"
_GmBindRuleProtoClass_Object = MibScalar
gmBindRuleProtoClass = _GmBindRuleProtoClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 6),
    _GmBindRuleProtoClass_Type()
)
gmBindRuleProtoClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmBindRuleProtoClass.setStatus("current")


class _GmBindRuleEthertype_Type(Integer32):
    """Custom type gmBindRuleEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_GmBindRuleEthertype_Type.__name__ = "Integer32"
_GmBindRuleEthertype_Object = MibScalar
gmBindRuleEthertype = _GmBindRuleEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 7),
    _GmBindRuleEthertype_Type()
)
gmBindRuleEthertype.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmBindRuleEthertype.setStatus("current")


class _GmBindRuleDsapSsap_Type(Integer32):
    """Custom type gmBindRuleDsapSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GmBindRuleDsapSsap_Type.__name__ = "Integer32"
_GmBindRuleDsapSsap_Object = MibScalar
gmBindRuleDsapSsap = _GmBindRuleDsapSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 8),
    _GmBindRuleDsapSsap_Type()
)
gmBindRuleDsapSsap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmBindRuleDsapSsap.setStatus("current")


class _GmOverloadRuleTable_Type(Integer32):
    """Custom type gmOverloadRuleTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macVlanTable", 1),
          ("subnetVlanTable", 2),
          ("protocolVlanTable", 3))
    )


_GmOverloadRuleTable_Type.__name__ = "Integer32"
_GmOverloadRuleTable_Object = MibScalar
gmOverloadRuleTable = _GmOverloadRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 9),
    _GmOverloadRuleTable_Type()
)
gmOverloadRuleTable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleTable.setStatus("current")


class _GmOverloadRuleType_Type(Integer32):
    """Custom type gmOverloadRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("macPortIpBinding", 1),
          ("macPortBinding", 2),
          ("portProtocolBinding", 3),
          ("macRule", 4),
          ("macRangeRule", 5),
          ("avlan", 6),
          ("dot1x", 7),
          ("ipSubnetRule", 8),
          ("ipxNetworkRule", 9),
          ("protocolRule", 10))
    )


_GmOverloadRuleType_Type.__name__ = "Integer32"
_GmOverloadRuleType_Object = MibScalar
gmOverloadRuleType = _GmOverloadRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 10),
    _GmOverloadRuleType_Type()
)
gmOverloadRuleType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleType.setStatus("current")
_GmOverloadRuleVlanId_Type = Unsigned32
_GmOverloadRuleVlanId_Object = MibScalar
gmOverloadRuleVlanId = _GmOverloadRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 11),
    _GmOverloadRuleVlanId_Type()
)
gmOverloadRuleVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleVlanId.setStatus("current")
_GmOverloadRuleMacAddress_Type = MacAddress
_GmOverloadRuleMacAddress_Object = MibScalar
gmOverloadRuleMacAddress = _GmOverloadRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 12),
    _GmOverloadRuleMacAddress_Type()
)
gmOverloadRuleMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleMacAddress.setStatus("current")
_GmOverloadRuleIpAddress_Type = IpAddress
_GmOverloadRuleIpAddress_Object = MibScalar
gmOverloadRuleIpAddress = _GmOverloadRuleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 13),
    _GmOverloadRuleIpAddress_Type()
)
gmOverloadRuleIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleIpAddress.setStatus("current")


class _GmOverloadRuleProtocol_Type(Integer32):
    """Custom type gmOverloadRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ipE2", 1),
          ("ipSnap", 2),
          ("ipxE2", 3),
          ("ipxNov", 4),
          ("ipxLlc", 5),
          ("ipxSnap", 6),
          ("decnet", 7),
          ("appletalk", 8),
          ("ethertypeE2", 9),
          ("dsapSsap", 10),
          ("ethertypeSnap", 11),
          ("ipv6", 12))
    )


_GmOverloadRuleProtocol_Type.__name__ = "Integer32"
_GmOverloadRuleProtocol_Object = MibScalar
gmOverloadRuleProtocol = _GmOverloadRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 14),
    _GmOverloadRuleProtocol_Type()
)
gmOverloadRuleProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleProtocol.setStatus("current")


class _GmOverloadRuleIpxNetwork_Type(Unsigned32):
    """Custom type gmOverloadRuleIpxNetwork based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_GmOverloadRuleIpxNetwork_Type.__name__ = "Unsigned32"
_GmOverloadRuleIpxNetwork_Object = MibScalar
gmOverloadRuleIpxNetwork = _GmOverloadRuleIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 15),
    _GmOverloadRuleIpxNetwork_Type()
)
gmOverloadRuleIpxNetwork.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleIpxNetwork.setStatus("current")


class _GmSubnetRuleTable_Type(Integer32):
    """Custom type gmSubnetRuleTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483646),
    )


_GmSubnetRuleTable_Type.__name__ = "Integer32"
_GmSubnetRuleTable_Object = MibScalar
gmSubnetRuleTable = _GmSubnetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 16),
    _GmSubnetRuleTable_Type()
)
gmSubnetRuleTable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmSubnetRuleTable.setStatus("current")
_GmOverloadRuleSlice_Type = Unsigned32
_GmOverloadRuleSlice_Object = MibScalar
gmOverloadRuleSlice = _GmOverloadRuleSlice_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 2, 17),
    _GmOverloadRuleSlice_Type()
)
gmOverloadRuleSlice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gmOverloadRuleSlice.setStatus("current")

# Managed Objects groups

groupMobilityRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 2, 1, 1)
)
groupMobilityRuleGroup.setObjects(
      *(("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpNetRuleAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpNetRuleMask"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpNetRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpNetRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpxNetRuleAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpxNetRuleEncap"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpxNetRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vIpxNetRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRuleAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRangeRuleLoAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRangeRuleHiAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRangeRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacRangeRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortIpBRuleMac"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortIpBRuleIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortIpBRuleIp"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortIpBRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortIpBRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortIpBRuleIp"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortIpBRuleIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortIpBRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortIpBRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacIpBRuleMac"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacIpBRuleIp"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacIpBRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacIpBRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortBRuleMac"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortBRuleIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortBRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortBRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleMacAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleProtoClass"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleEthertype"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleDsapSsap"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMacPortProtoBRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleProtoClass"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleEthertype"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleDsapSsap"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortProtoBRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRuleAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpPortRuleIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpPortRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpPortRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpGenericRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpGenericRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleProtoClass"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleEthertype"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleDsapSsap"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vProtoRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vCustomRuleValue"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vCustomRuleMask"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vCustomRuleOffset"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vCustomRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vCustomRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortRuleIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vPortRuleStatus"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRangeRuleLoAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRangeRuleHiAddr"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRangeRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vDhcpMacRangeRuleStatus"))
)
if mibBuilder.loadTexts:
    groupMobilityRuleGroup.setStatus("current")

groupMobilityPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 2, 1, 2)
)
groupMobilityPortGroup.setObjects(
      *(("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortMobility"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortDefVlanRestore"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortDefVlanEnable"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortIgnoreBPDU"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortAuthenticate"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortCfgDefVlan"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "vMobilePortIngressFiltering"))
)
if mibBuilder.loadTexts:
    groupMobilityPortGroup.setStatus("current")


# Notification objects

gmBindRuleViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 1, 0, 1)
)
gmBindRuleViolation.setObjects(
      *(("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleType"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleIPAddress"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleMacAddress"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRulePortIfIndex"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleProtoClass"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleEthertype"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleDsapSsap"))
)
if mibBuilder.loadTexts:
    gmBindRuleViolation.setStatus(
        "current"
    )

gmHwVlanRuleTableOverloadAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 1, 0, 2)
)
gmHwVlanRuleTableOverloadAlert.setObjects(
      *(("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleTable"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleType"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleVlanId"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleMacAddress"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleIpAddress"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleProtocol"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleIpxNetwork"))
)
if mibBuilder.loadTexts:
    gmHwVlanRuleTableOverloadAlert.setStatus(
        "current"
    )

gmHwMixModeSubnetRuleTableOverloadAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 13, 1, 0, 3)
)
gmHwMixModeSubnetRuleTableOverloadAlert.setObjects(
      *(("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmSubnetRuleTable"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmOverloadRuleSlice"))
)
if mibBuilder.loadTexts:
    gmHwMixModeSubnetRuleTableOverloadAlert.setStatus(
        "current"
    )


# Notifications groups

groupMobilityTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 2, 1, 4)
)
groupMobilityTrapGroup.setObjects(
      *(("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmBindRuleViolation"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmHwVlanRuleTableOverloadAlert"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "gmHwMixModeSubnetRuleTableOverloadAlert"))
)
if mibBuilder.loadTexts:
    groupMobilityTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1GroupMobilityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 4, 1, 2, 2, 1)
)
alcatelIND1GroupMobilityMIBCompliance.setObjects(
      *(("ALCATEL-IND1-GROUP-MOBILITY-MIB", "groupMobilityRuleGroup"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "groupMobilityPortGroup"),
        ("ALCATEL-IND1-GROUP-MOBILITY-MIB", "groupMobilityTrapGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1GroupMobilityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-GROUP-MOBILITY-MIB",
    **{"alcatelIND1GroupMobilityMIB": alcatelIND1GroupMobilityMIB,
       "alcatelIND1GroupMobilityMIBObjects": alcatelIND1GroupMobilityMIBObjects,
       "groupMobilityRule": groupMobilityRule,
       "vIpNetRuleTable": vIpNetRuleTable,
       "vIpNetRuleEntry": vIpNetRuleEntry,
       "vIpNetRuleAddr": vIpNetRuleAddr,
       "vIpNetRuleMask": vIpNetRuleMask,
       "vIpNetRuleVlanId": vIpNetRuleVlanId,
       "vIpNetRuleStatus": vIpNetRuleStatus,
       "vIpxNetRuleTable": vIpxNetRuleTable,
       "vIpxNetRuleEntry": vIpxNetRuleEntry,
       "vIpxNetRuleAddr": vIpxNetRuleAddr,
       "vIpxNetRuleEncap": vIpxNetRuleEncap,
       "vIpxNetRuleVlanId": vIpxNetRuleVlanId,
       "vIpxNetRuleStatus": vIpxNetRuleStatus,
       "vMacRuleTable": vMacRuleTable,
       "vMacRuleEntry": vMacRuleEntry,
       "vMacRuleAddr": vMacRuleAddr,
       "vMacRuleVlanId": vMacRuleVlanId,
       "vMacRuleStatus": vMacRuleStatus,
       "vMacRangeRuleTable": vMacRangeRuleTable,
       "vMacRangeRuleEntry": vMacRangeRuleEntry,
       "vMacRangeRuleLoAddr": vMacRangeRuleLoAddr,
       "vMacRangeRuleHiAddr": vMacRangeRuleHiAddr,
       "vMacRangeRuleVlanId": vMacRangeRuleVlanId,
       "vMacRangeRuleStatus": vMacRangeRuleStatus,
       "vMacPortIpBRuleTable": vMacPortIpBRuleTable,
       "vMacPortIpBRuleEntry": vMacPortIpBRuleEntry,
       "vMacPortIpBRuleMac": vMacPortIpBRuleMac,
       "vMacPortIpBRuleIfIndex": vMacPortIpBRuleIfIndex,
       "vMacPortIpBRuleIp": vMacPortIpBRuleIp,
       "vMacPortIpBRuleVlanId": vMacPortIpBRuleVlanId,
       "vMacPortIpBRuleStatus": vMacPortIpBRuleStatus,
       "vPortIpBRuleTable": vPortIpBRuleTable,
       "vPortIpBRuleEntry": vPortIpBRuleEntry,
       "vPortIpBRuleIp": vPortIpBRuleIp,
       "vPortIpBRuleIfIndex": vPortIpBRuleIfIndex,
       "vPortIpBRuleVlanId": vPortIpBRuleVlanId,
       "vPortIpBRuleStatus": vPortIpBRuleStatus,
       "vMacIpBRuleTable": vMacIpBRuleTable,
       "vMacIpBRuleEntry": vMacIpBRuleEntry,
       "vMacIpBRuleMac": vMacIpBRuleMac,
       "vMacIpBRuleIp": vMacIpBRuleIp,
       "vMacIpBRuleVlanId": vMacIpBRuleVlanId,
       "vMacIpBRuleStatus": vMacIpBRuleStatus,
       "vMacPortBRuleTable": vMacPortBRuleTable,
       "vMacPortBRuleEntry": vMacPortBRuleEntry,
       "vMacPortBRuleMac": vMacPortBRuleMac,
       "vMacPortBRuleIfIndex": vMacPortBRuleIfIndex,
       "vMacPortBRuleVlanId": vMacPortBRuleVlanId,
       "vMacPortBRuleStatus": vMacPortBRuleStatus,
       "vMacPortProtoBRuleTable": vMacPortProtoBRuleTable,
       "vMacPortProtoBRuleEntry": vMacPortProtoBRuleEntry,
       "vMacPortProtoBRuleMacAddr": vMacPortProtoBRuleMacAddr,
       "vMacPortProtoBRuleIfIndex": vMacPortProtoBRuleIfIndex,
       "vMacPortProtoBRuleProtoClass": vMacPortProtoBRuleProtoClass,
       "vMacPortProtoBRuleEthertype": vMacPortProtoBRuleEthertype,
       "vMacPortProtoBRuleDsapSsap": vMacPortProtoBRuleDsapSsap,
       "vMacPortProtoBRuleVlanId": vMacPortProtoBRuleVlanId,
       "vMacPortProtoBRuleStatus": vMacPortProtoBRuleStatus,
       "vPortProtoBRuleTable": vPortProtoBRuleTable,
       "vPortProtoBRuleEntry": vPortProtoBRuleEntry,
       "vPortProtoBRuleIfIndex": vPortProtoBRuleIfIndex,
       "vPortProtoBRuleProtoClass": vPortProtoBRuleProtoClass,
       "vPortProtoBRuleEthertype": vPortProtoBRuleEthertype,
       "vPortProtoBRuleDsapSsap": vPortProtoBRuleDsapSsap,
       "vPortProtoBRuleVlanId": vPortProtoBRuleVlanId,
       "vPortProtoBRuleStatus": vPortProtoBRuleStatus,
       "vDhcpMacRuleTable": vDhcpMacRuleTable,
       "vDhcpMacRuleEntry": vDhcpMacRuleEntry,
       "vDhcpMacRuleAddr": vDhcpMacRuleAddr,
       "vDhcpMacRuleVlanId": vDhcpMacRuleVlanId,
       "vDhcpMacRuleStatus": vDhcpMacRuleStatus,
       "vDhcpPortRuleTable": vDhcpPortRuleTable,
       "vDhcpPortRuleEntry": vDhcpPortRuleEntry,
       "vDhcpPortRuleIfIndex": vDhcpPortRuleIfIndex,
       "vDhcpPortRuleVlanId": vDhcpPortRuleVlanId,
       "vDhcpPortRuleStatus": vDhcpPortRuleStatus,
       "vDhcpGenericRuleTable": vDhcpGenericRuleTable,
       "vDhcpGenericRuleEntry": vDhcpGenericRuleEntry,
       "vDhcpGenericRuleVlanId": vDhcpGenericRuleVlanId,
       "vDhcpGenericRuleStatus": vDhcpGenericRuleStatus,
       "vProtoRuleTable": vProtoRuleTable,
       "vProtoRuleEntry": vProtoRuleEntry,
       "vProtoRuleProtoClass": vProtoRuleProtoClass,
       "vProtoRuleEthertype": vProtoRuleEthertype,
       "vProtoRuleDsapSsap": vProtoRuleDsapSsap,
       "vProtoRuleVlanId": vProtoRuleVlanId,
       "vProtoRuleStatus": vProtoRuleStatus,
       "vCustomRuleTable": vCustomRuleTable,
       "vCustomRuleEntry": vCustomRuleEntry,
       "vCustomRuleValue": vCustomRuleValue,
       "vCustomRuleMask": vCustomRuleMask,
       "vCustomRuleOffset": vCustomRuleOffset,
       "vCustomRuleVlanId": vCustomRuleVlanId,
       "vCustomRuleStatus": vCustomRuleStatus,
       "vPortRuleTable": vPortRuleTable,
       "vPortRuleEntry": vPortRuleEntry,
       "vPortRuleIfIndex": vPortRuleIfIndex,
       "vPortRuleVlanId": vPortRuleVlanId,
       "vPortRuleStatus": vPortRuleStatus,
       "vDhcpMacRangeRuleTable": vDhcpMacRangeRuleTable,
       "vDhcpMacRangeRuleEntry": vDhcpMacRangeRuleEntry,
       "vDhcpMacRangeRuleLoAddr": vDhcpMacRangeRuleLoAddr,
       "vDhcpMacRangeRuleHiAddr": vDhcpMacRangeRuleHiAddr,
       "vDhcpMacRangeRuleVlanId": vDhcpMacRangeRuleVlanId,
       "vDhcpMacRangeRuleStatus": vDhcpMacRangeRuleStatus,
       "groupMobilityPort": groupMobilityPort,
       "vMobilePortTable": vMobilePortTable,
       "vMobilePortEntry": vMobilePortEntry,
       "vMobilePortIfIndex": vMobilePortIfIndex,
       "vMobilePortMobility": vMobilePortMobility,
       "vMobilePortDefVlanRestore": vMobilePortDefVlanRestore,
       "vMobilePortDefVlanEnable": vMobilePortDefVlanEnable,
       "vMobilePortIgnoreBPDU": vMobilePortIgnoreBPDU,
       "vMobilePortAuthenticate": vMobilePortAuthenticate,
       "vMobilePortCfgDefVlan": vMobilePortCfgDefVlan,
       "vMobilePortIngressFiltering": vMobilePortIngressFiltering,
       "alcatelIND1GroupMobilityMIBConformance": alcatelIND1GroupMobilityMIBConformance,
       "alcatelIND1GroupMobilityMIBGroups": alcatelIND1GroupMobilityMIBGroups,
       "groupMobilityRuleGroup": groupMobilityRuleGroup,
       "groupMobilityPortGroup": groupMobilityPortGroup,
       "groupMobilityTrapGroup": groupMobilityTrapGroup,
       "alcatelIND1GroupMobilityMIBCompliances": alcatelIND1GroupMobilityMIBCompliances,
       "alcatelIND1GroupMobilityMIBCompliance": alcatelIND1GroupMobilityMIBCompliance,
       "groupmobilityTrapsDesc": groupmobilityTrapsDesc,
       "gmBindRuleViolation": gmBindRuleViolation,
       "gmHwVlanRuleTableOverloadAlert": gmHwVlanRuleTableOverloadAlert,
       "gmHwMixModeSubnetRuleTableOverloadAlert": gmHwMixModeSubnetRuleTableOverloadAlert,
       "groupmobilityTrapsObj": groupmobilityTrapsObj,
       "gmBindRuleType": gmBindRuleType,
       "gmBindRuleVlanId": gmBindRuleVlanId,
       "gmBindRuleIPAddress": gmBindRuleIPAddress,
       "gmBindRuleMacAddress": gmBindRuleMacAddress,
       "gmBindRulePortIfIndex": gmBindRulePortIfIndex,
       "gmBindRuleProtoClass": gmBindRuleProtoClass,
       "gmBindRuleEthertype": gmBindRuleEthertype,
       "gmBindRuleDsapSsap": gmBindRuleDsapSsap,
       "gmOverloadRuleTable": gmOverloadRuleTable,
       "gmOverloadRuleType": gmOverloadRuleType,
       "gmOverloadRuleVlanId": gmOverloadRuleVlanId,
       "gmOverloadRuleMacAddress": gmOverloadRuleMacAddress,
       "gmOverloadRuleIpAddress": gmOverloadRuleIpAddress,
       "gmOverloadRuleProtocol": gmOverloadRuleProtocol,
       "gmOverloadRuleIpxNetwork": gmOverloadRuleIpxNetwork,
       "gmSubnetRuleTable": gmSubnetRuleTable,
       "gmOverloadRuleSlice": gmOverloadRuleSlice}
)
