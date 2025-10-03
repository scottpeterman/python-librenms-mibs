# SNMP MIB module (DLINKSW-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-VLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:07 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(VlanId,
 dot1vProtocolPortGroupId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "dot1vProtocolPortGroupId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 21)
)
if mibBuilder.loadTexts:
    dlinkSwVlanMIB.setRevisions(
        ("2013-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DVlanMIBNotifications_ObjectIdentity = ObjectIdentity
dVlanMIBNotifications = _DVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 0)
)
_DVlanMIBObjects_ObjectIdentity = ObjectIdentity
dVlanMIBObjects = _DVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1)
)
_DVlanStaticMacVlanTable_Object = MibTable
dVlanStaticMacVlanTable = _DVlanStaticMacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 1)
)
if mibBuilder.loadTexts:
    dVlanStaticMacVlanTable.setStatus("current")
_DVlanStaticMacVlanEntry_Object = MibTableRow
dVlanStaticMacVlanEntry = _DVlanStaticMacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 1, 1)
)
dVlanStaticMacVlanEntry.setIndexNames(
    (0, "DLINKSW-VLAN-MIB", "dVlanStaticMacVlanAddress"),
)
if mibBuilder.loadTexts:
    dVlanStaticMacVlanEntry.setStatus("current")
_DVlanStaticMacVlanAddress_Type = MacAddress
_DVlanStaticMacVlanAddress_Object = MibTableColumn
dVlanStaticMacVlanAddress = _DVlanStaticMacVlanAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 1, 1, 1),
    _DVlanStaticMacVlanAddress_Type()
)
dVlanStaticMacVlanAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVlanStaticMacVlanAddress.setStatus("current")
_DVlanStaticMacVlanId_Type = VlanId
_DVlanStaticMacVlanId_Object = MibTableColumn
dVlanStaticMacVlanId = _DVlanStaticMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 1, 1, 2),
    _DVlanStaticMacVlanId_Type()
)
dVlanStaticMacVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVlanStaticMacVlanId.setStatus("current")


class _DVlanStaticMacVlanPriority_Type(Unsigned32):
    """Custom type dVlanStaticMacVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DVlanStaticMacVlanPriority_Type.__name__ = "Unsigned32"
_DVlanStaticMacVlanPriority_Object = MibTableColumn
dVlanStaticMacVlanPriority = _DVlanStaticMacVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 1, 1, 3),
    _DVlanStaticMacVlanPriority_Type()
)
dVlanStaticMacVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVlanStaticMacVlanPriority.setStatus("current")
_DVlanStaticMacVlanRowStatus_Type = RowStatus
_DVlanStaticMacVlanRowStatus_Object = MibTableColumn
dVlanStaticMacVlanRowStatus = _DVlanStaticMacVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 1, 1, 4),
    _DVlanStaticMacVlanRowStatus_Type()
)
dVlanStaticMacVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVlanStaticMacVlanRowStatus.setStatus("current")
_DVlanCurrentMacVlanTable_Object = MibTable
dVlanCurrentMacVlanTable = _DVlanCurrentMacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 2)
)
if mibBuilder.loadTexts:
    dVlanCurrentMacVlanTable.setStatus("current")
_DVlanCurrentMacVlanEntry_Object = MibTableRow
dVlanCurrentMacVlanEntry = _DVlanCurrentMacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 2, 1)
)
dVlanCurrentMacVlanEntry.setIndexNames(
    (0, "DLINKSW-VLAN-MIB", "dVlanCurrentMacVlanAddress"),
    (0, "DLINKSW-VLAN-MIB", "dVlanCurrentMacVlanStatus"),
)
if mibBuilder.loadTexts:
    dVlanCurrentMacVlanEntry.setStatus("current")
_DVlanCurrentMacVlanAddress_Type = MacAddress
_DVlanCurrentMacVlanAddress_Object = MibTableColumn
dVlanCurrentMacVlanAddress = _DVlanCurrentMacVlanAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 2, 1, 1),
    _DVlanCurrentMacVlanAddress_Type()
)
dVlanCurrentMacVlanAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVlanCurrentMacVlanAddress.setStatus("current")


class _DVlanCurrentMacVlanStatus_Type(Integer32):
    """Custom type dVlanCurrentMacVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DVlanCurrentMacVlanStatus_Type.__name__ = "Integer32"
_DVlanCurrentMacVlanStatus_Object = MibTableColumn
dVlanCurrentMacVlanStatus = _DVlanCurrentMacVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 2, 1, 2),
    _DVlanCurrentMacVlanStatus_Type()
)
dVlanCurrentMacVlanStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVlanCurrentMacVlanStatus.setStatus("current")
_DVlanCurrentMacVlanId_Type = VlanId
_DVlanCurrentMacVlanId_Object = MibTableColumn
dVlanCurrentMacVlanId = _DVlanCurrentMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 2, 1, 3),
    _DVlanCurrentMacVlanId_Type()
)
dVlanCurrentMacVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVlanCurrentMacVlanId.setStatus("current")


class _DVlanCurrentMacVlanPriority_Type(Unsigned32):
    """Custom type dVlanCurrentMacVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DVlanCurrentMacVlanPriority_Type.__name__ = "Unsigned32"
_DVlanCurrentMacVlanPriority_Object = MibTableColumn
dVlanCurrentMacVlanPriority = _DVlanCurrentMacVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 2, 1, 4),
    _DVlanCurrentMacVlanPriority_Type()
)
dVlanCurrentMacVlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dVlanCurrentMacVlanPriority.setStatus("current")
_DVlanSubnetVlanTable_Object = MibTable
dVlanSubnetVlanTable = _DVlanSubnetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3)
)
if mibBuilder.loadTexts:
    dVlanSubnetVlanTable.setStatus("current")
_DVlanSubnetVlanEntry_Object = MibTableRow
dVlanSubnetVlanEntry = _DVlanSubnetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3, 1)
)
dVlanSubnetVlanEntry.setIndexNames(
    (0, "DLINKSW-VLAN-MIB", "dVlanSubnetVlanType"),
    (0, "DLINKSW-VLAN-MIB", "dVlanSubnetVlanNetPrefix"),
    (0, "DLINKSW-VLAN-MIB", "dVlanSubnetVlanNetPrefixLen"),
)
if mibBuilder.loadTexts:
    dVlanSubnetVlanEntry.setStatus("current")
_DVlanSubnetVlanType_Type = InetAddressType
_DVlanSubnetVlanType_Object = MibTableColumn
dVlanSubnetVlanType = _DVlanSubnetVlanType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3, 1, 1),
    _DVlanSubnetVlanType_Type()
)
dVlanSubnetVlanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVlanSubnetVlanType.setStatus("current")
_DVlanSubnetVlanNetPrefix_Type = InetAddress
_DVlanSubnetVlanNetPrefix_Object = MibTableColumn
dVlanSubnetVlanNetPrefix = _DVlanSubnetVlanNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3, 1, 2),
    _DVlanSubnetVlanNetPrefix_Type()
)
dVlanSubnetVlanNetPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVlanSubnetVlanNetPrefix.setStatus("current")
_DVlanSubnetVlanNetPrefixLen_Type = InetAddressPrefixLength
_DVlanSubnetVlanNetPrefixLen_Object = MibTableColumn
dVlanSubnetVlanNetPrefixLen = _DVlanSubnetVlanNetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3, 1, 3),
    _DVlanSubnetVlanNetPrefixLen_Type()
)
dVlanSubnetVlanNetPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dVlanSubnetVlanNetPrefixLen.setStatus("current")
_DVlanSubnetVlanId_Type = VlanId
_DVlanSubnetVlanId_Object = MibTableColumn
dVlanSubnetVlanId = _DVlanSubnetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3, 1, 4),
    _DVlanSubnetVlanId_Type()
)
dVlanSubnetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVlanSubnetVlanId.setStatus("current")


class _DVlanSubnetVlanPriority_Type(Unsigned32):
    """Custom type dVlanSubnetVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DVlanSubnetVlanPriority_Type.__name__ = "Unsigned32"
_DVlanSubnetVlanPriority_Object = MibTableColumn
dVlanSubnetVlanPriority = _DVlanSubnetVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3, 1, 5),
    _DVlanSubnetVlanPriority_Type()
)
dVlanSubnetVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVlanSubnetVlanPriority.setStatus("current")
_DVlanSubnetVlanRowStatus_Type = RowStatus
_DVlanSubnetVlanRowStatus_Object = MibTableColumn
dVlanSubnetVlanRowStatus = _DVlanSubnetVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 3, 1, 6),
    _DVlanSubnetVlanRowStatus_Type()
)
dVlanSubnetVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dVlanSubnetVlanRowStatus.setStatus("current")
_DVlanPortIfCtrlTable_Object = MibTable
dVlanPortIfCtrlTable = _DVlanPortIfCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4)
)
if mibBuilder.loadTexts:
    dVlanPortIfCtrlTable.setStatus("current")
_DVlanPortIfCtrlEntry_Object = MibTableRow
dVlanPortIfCtrlEntry = _DVlanPortIfCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1)
)
dVlanPortIfCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dVlanPortIfCtrlEntry.setStatus("current")


class _DVlanPortIfMode_Type(Integer32):
    """Custom type dVlanPortIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("hybrid", 2),
          ("trunk", 3),
          ("dot1qTunnel", 4),
          ("privateVlanHost", 5),
          ("privateVlanPromiscuous", 6))
    )


_DVlanPortIfMode_Type.__name__ = "Integer32"
_DVlanPortIfMode_Object = MibTableColumn
dVlanPortIfMode = _DVlanPortIfMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 1),
    _DVlanPortIfMode_Type()
)
dVlanPortIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfMode.setStatus("current")
_DVlanPortIfTrunkNativeVlanTagged_Type = TruthValue
_DVlanPortIfTrunkNativeVlanTagged_Object = MibTableColumn
dVlanPortIfTrunkNativeVlanTagged = _DVlanPortIfTrunkNativeVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 2),
    _DVlanPortIfTrunkNativeVlanTagged_Type()
)
dVlanPortIfTrunkNativeVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfTrunkNativeVlanTagged.setStatus("current")


class _DVlanPortIfAcceptableFrameTypes_Type(Integer32):
    """Custom type dVlanPortIfAcceptableFrameTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitUntaggedAndPriority", 2),
          ("admitTagged", 3))
    )


_DVlanPortIfAcceptableFrameTypes_Type.__name__ = "Integer32"
_DVlanPortIfAcceptableFrameTypes_Object = MibTableColumn
dVlanPortIfAcceptableFrameTypes = _DVlanPortIfAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 3),
    _DVlanPortIfAcceptableFrameTypes_Type()
)
dVlanPortIfAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfAcceptableFrameTypes.setStatus("current")


class _DVlanPortIfVlanPrecedence_Type(Integer32):
    """Custom type dVlanPortIfVlanPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macVlan", 1),
          ("subnetVlan", 2))
    )


_DVlanPortIfVlanPrecedence_Type.__name__ = "Integer32"
_DVlanPortIfVlanPrecedence_Object = MibTableColumn
dVlanPortIfVlanPrecedence = _DVlanPortIfVlanPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 4),
    _DVlanPortIfVlanPrecedence_Type()
)
dVlanPortIfVlanPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfVlanPrecedence.setStatus("current")
_DVlanPortIfTagAllowVlanLstFirst2K_Type = Dlink2kVlanList
_DVlanPortIfTagAllowVlanLstFirst2K_Object = MibTableColumn
dVlanPortIfTagAllowVlanLstFirst2K = _DVlanPortIfTagAllowVlanLstFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 5),
    _DVlanPortIfTagAllowVlanLstFirst2K_Type()
)
dVlanPortIfTagAllowVlanLstFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfTagAllowVlanLstFirst2K.setStatus("current")
_DVlanPortIfTagAllowVlanLstSecond2K_Type = Dlink2kVlanList
_DVlanPortIfTagAllowVlanLstSecond2K_Object = MibTableColumn
dVlanPortIfTagAllowVlanLstSecond2K = _DVlanPortIfTagAllowVlanLstSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 6),
    _DVlanPortIfTagAllowVlanLstSecond2K_Type()
)
dVlanPortIfTagAllowVlanLstSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfTagAllowVlanLstSecond2K.setStatus("current")
_DVlanPortIfUntagAllowVlanLstFirst2K_Type = Dlink2kVlanList
_DVlanPortIfUntagAllowVlanLstFirst2K_Object = MibTableColumn
dVlanPortIfUntagAllowVlanLstFirst2K = _DVlanPortIfUntagAllowVlanLstFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 7),
    _DVlanPortIfUntagAllowVlanLstFirst2K_Type()
)
dVlanPortIfUntagAllowVlanLstFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfUntagAllowVlanLstFirst2K.setStatus("current")
_DVlanPortIfUntagAllowVlanLstSecond2K_Type = Dlink2kVlanList
_DVlanPortIfUntagAllowVlanLstSecond2K_Object = MibTableColumn
dVlanPortIfUntagAllowVlanLstSecond2K = _DVlanPortIfUntagAllowVlanLstSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 4, 1, 8),
    _DVlanPortIfUntagAllowVlanLstSecond2K_Type()
)
dVlanPortIfUntagAllowVlanLstSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanPortIfUntagAllowVlanLstSecond2K.setStatus("current")
_DVlanProtocolVlanIfCtrlTable_Object = MibTable
dVlanProtocolVlanIfCtrlTable = _DVlanProtocolVlanIfCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 5)
)
if mibBuilder.loadTexts:
    dVlanProtocolVlanIfCtrlTable.setStatus("current")
_DVlanProtocolVlanIfCtrlEntry_Object = MibTableRow
dVlanProtocolVlanIfCtrlEntry = _DVlanProtocolVlanIfCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 5, 1)
)
dVlanProtocolVlanIfCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Q-BRIDGE-MIB", "dot1vProtocolPortGroupId"),
)
if mibBuilder.loadTexts:
    dVlanProtocolVlanIfCtrlEntry.setStatus("current")


class _DVlanProtocolVlanPriority_Type(Unsigned32):
    """Custom type dVlanProtocolVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DVlanProtocolVlanPriority_Type.__name__ = "Unsigned32"
_DVlanProtocolVlanPriority_Object = MibTableColumn
dVlanProtocolVlanPriority = _DVlanProtocolVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 5, 1, 1),
    _DVlanProtocolVlanPriority_Type()
)
dVlanProtocolVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanProtocolVlanPriority.setStatus("current")
_DVlanAsymVlanStateEnabled_Type = TruthValue
_DVlanAsymVlanStateEnabled_Object = MibScalar
dVlanAsymVlanStateEnabled = _DVlanAsymVlanStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 1, 6),
    _DVlanAsymVlanStateEnabled_Type()
)
dVlanAsymVlanStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dVlanAsymVlanStateEnabled.setStatus("current")
_DVlanMIBConformance_ObjectIdentity = ObjectIdentity
dVlanMIBConformance = _DVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2)
)
_DVlanCompliances_ObjectIdentity = ObjectIdentity
dVlanCompliances = _DVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 1)
)
_DVlanGroups_ObjectIdentity = ObjectIdentity
dVlanGroups = _DVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 2)
)

# Managed Objects groups

dVlanIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 2, 1)
)
dVlanIfCfgGroup.setObjects(
      *(("DLINKSW-VLAN-MIB", "dVlanPortIfMode"),
        ("DLINKSW-VLAN-MIB", "dVlanPortIfTrunkNativeVlanTagged"),
        ("DLINKSW-VLAN-MIB", "dVlanPortIfVlanPrecedence"),
        ("DLINKSW-VLAN-MIB", "dVlanPortIfAcceptableFrameTypes"),
        ("DLINKSW-VLAN-MIB", "dVlanPortIfTagAllowVlanLstFirst2K"),
        ("DLINKSW-VLAN-MIB", "dVlanPortIfTagAllowVlanLstSecond2K"),
        ("DLINKSW-VLAN-MIB", "dVlanPortIfUntagAllowVlanLstFirst2K"),
        ("DLINKSW-VLAN-MIB", "dVlanPortIfUntagAllowVlanLstSecond2K"))
)
if mibBuilder.loadTexts:
    dVlanIfCfgGroup.setStatus("current")

dVlanStaticMacVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 2, 2)
)
dVlanStaticMacVlanCfgGroup.setObjects(
      *(("DLINKSW-VLAN-MIB", "dVlanStaticMacVlanId"),
        ("DLINKSW-VLAN-MIB", "dVlanStaticMacVlanPriority"),
        ("DLINKSW-VLAN-MIB", "dVlanStaticMacVlanRowStatus"))
)
if mibBuilder.loadTexts:
    dVlanStaticMacVlanCfgGroup.setStatus("current")

dVlanCurrentMacVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 2, 3)
)
dVlanCurrentMacVlanCfgGroup.setObjects(
      *(("DLINKSW-VLAN-MIB", "dVlanCurrentMacVlanId"),
        ("DLINKSW-VLAN-MIB", "dVlanCurrentMacVlanPriority"))
)
if mibBuilder.loadTexts:
    dVlanCurrentMacVlanCfgGroup.setStatus("current")

dVlanSubnetVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 2, 4)
)
dVlanSubnetVlanCfgGroup.setObjects(
      *(("DLINKSW-VLAN-MIB", "dVlanSubnetVlanId"),
        ("DLINKSW-VLAN-MIB", "dVlanSubnetVlanPriority"),
        ("DLINKSW-VLAN-MIB", "dVlanSubnetVlanRowStatus"))
)
if mibBuilder.loadTexts:
    dVlanSubnetVlanCfgGroup.setStatus("current")

dVlanProtocolVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 2, 5)
)
dVlanProtocolVlanCfgGroup.setObjects(
    ("DLINKSW-VLAN-MIB", "dVlanProtocolVlanPriority")
)
if mibBuilder.loadTexts:
    dVlanProtocolVlanCfgGroup.setStatus("current")

dVlanAsymmetricVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 2, 6)
)
dVlanAsymmetricVlanCfgGroup.setObjects(
    ("DLINKSW-VLAN-MIB", "dVlanAsymVlanStateEnabled")
)
if mibBuilder.loadTexts:
    dVlanAsymmetricVlanCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 21, 2, 1, 1)
)
dVlanCompliance.setObjects(
      *(("DLINKSW-VLAN-MIB", "dVlanIfCfgGroup"),
        ("DLINKSW-VLAN-MIB", "dVlanStaticMacVlanCfgGroup"),
        ("DLINKSW-VLAN-MIB", "dVlanCurrentMacVlanCfgGroup"),
        ("DLINKSW-VLAN-MIB", "dVlanSubnetVlanCfgGroup"),
        ("DLINKSW-VLAN-MIB", "dVlanProtocolVlanCfgGroup"),
        ("DLINKSW-VLAN-MIB", "dVlanAsymmetricVlanCfgGroup"))
)
if mibBuilder.loadTexts:
    dVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-VLAN-MIB",
    **{"dlinkSwVlanMIB": dlinkSwVlanMIB,
       "dVlanMIBNotifications": dVlanMIBNotifications,
       "dVlanMIBObjects": dVlanMIBObjects,
       "dVlanStaticMacVlanTable": dVlanStaticMacVlanTable,
       "dVlanStaticMacVlanEntry": dVlanStaticMacVlanEntry,
       "dVlanStaticMacVlanAddress": dVlanStaticMacVlanAddress,
       "dVlanStaticMacVlanId": dVlanStaticMacVlanId,
       "dVlanStaticMacVlanPriority": dVlanStaticMacVlanPriority,
       "dVlanStaticMacVlanRowStatus": dVlanStaticMacVlanRowStatus,
       "dVlanCurrentMacVlanTable": dVlanCurrentMacVlanTable,
       "dVlanCurrentMacVlanEntry": dVlanCurrentMacVlanEntry,
       "dVlanCurrentMacVlanAddress": dVlanCurrentMacVlanAddress,
       "dVlanCurrentMacVlanStatus": dVlanCurrentMacVlanStatus,
       "dVlanCurrentMacVlanId": dVlanCurrentMacVlanId,
       "dVlanCurrentMacVlanPriority": dVlanCurrentMacVlanPriority,
       "dVlanSubnetVlanTable": dVlanSubnetVlanTable,
       "dVlanSubnetVlanEntry": dVlanSubnetVlanEntry,
       "dVlanSubnetVlanType": dVlanSubnetVlanType,
       "dVlanSubnetVlanNetPrefix": dVlanSubnetVlanNetPrefix,
       "dVlanSubnetVlanNetPrefixLen": dVlanSubnetVlanNetPrefixLen,
       "dVlanSubnetVlanId": dVlanSubnetVlanId,
       "dVlanSubnetVlanPriority": dVlanSubnetVlanPriority,
       "dVlanSubnetVlanRowStatus": dVlanSubnetVlanRowStatus,
       "dVlanPortIfCtrlTable": dVlanPortIfCtrlTable,
       "dVlanPortIfCtrlEntry": dVlanPortIfCtrlEntry,
       "dVlanPortIfMode": dVlanPortIfMode,
       "dVlanPortIfTrunkNativeVlanTagged": dVlanPortIfTrunkNativeVlanTagged,
       "dVlanPortIfAcceptableFrameTypes": dVlanPortIfAcceptableFrameTypes,
       "dVlanPortIfVlanPrecedence": dVlanPortIfVlanPrecedence,
       "dVlanPortIfTagAllowVlanLstFirst2K": dVlanPortIfTagAllowVlanLstFirst2K,
       "dVlanPortIfTagAllowVlanLstSecond2K": dVlanPortIfTagAllowVlanLstSecond2K,
       "dVlanPortIfUntagAllowVlanLstFirst2K": dVlanPortIfUntagAllowVlanLstFirst2K,
       "dVlanPortIfUntagAllowVlanLstSecond2K": dVlanPortIfUntagAllowVlanLstSecond2K,
       "dVlanProtocolVlanIfCtrlTable": dVlanProtocolVlanIfCtrlTable,
       "dVlanProtocolVlanIfCtrlEntry": dVlanProtocolVlanIfCtrlEntry,
       "dVlanProtocolVlanPriority": dVlanProtocolVlanPriority,
       "dVlanAsymVlanStateEnabled": dVlanAsymVlanStateEnabled,
       "dVlanMIBConformance": dVlanMIBConformance,
       "dVlanCompliances": dVlanCompliances,
       "dVlanCompliance": dVlanCompliance,
       "dVlanGroups": dVlanGroups,
       "dVlanIfCfgGroup": dVlanIfCfgGroup,
       "dVlanStaticMacVlanCfgGroup": dVlanStaticMacVlanCfgGroup,
       "dVlanCurrentMacVlanCfgGroup": dVlanCurrentMacVlanCfgGroup,
       "dVlanSubnetVlanCfgGroup": dVlanSubnetVlanCfgGroup,
       "dVlanProtocolVlanCfgGroup": dVlanProtocolVlanCfgGroup,
       "dVlanAsymmetricVlanCfgGroup": dVlanAsymmetricVlanCfgGroup}
)
