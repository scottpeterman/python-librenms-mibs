# SNMP MIB module (DLINKSW-LACP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-LACP-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:27 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwLacpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 4)
)
if mibBuilder.loadTexts:
    dlinkSwLacpExtMIB.setRevisions(
        ("2013-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DLacpExtMIBNotifications_ObjectIdentity = ObjectIdentity
dLacpExtMIBNotifications = _DLacpExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 0)
)
_DLacpExtMIBObjects_ObjectIdentity = ObjectIdentity
dLacpExtMIBObjects = _DLacpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1)
)


class _DLacpExtLoadBalanceAlgorithm_Type(Integer32):
    """Custom type dLacpExtLoadBalanceAlgorithm based on Integer32"""
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
        *(("dstIp", 1),
          ("dstMac", 2),
          ("srcDstIp", 3),
          ("srcDstMac", 4),
          ("srcIp", 5),
          ("srcMac", 6))
    )


_DLacpExtLoadBalanceAlgorithm_Type.__name__ = "Integer32"
_DLacpExtLoadBalanceAlgorithm_Object = MibScalar
dLacpExtLoadBalanceAlgorithm = _DLacpExtLoadBalanceAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 1),
    _DLacpExtLoadBalanceAlgorithm_Type()
)
dLacpExtLoadBalanceAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLacpExtLoadBalanceAlgorithm.setStatus("current")
_DLacpExtGroupTable_Object = MibTable
dLacpExtGroupTable = _DLacpExtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dLacpExtGroupTable.setStatus("current")
_DLacpExtGroupEntry_Object = MibTableRow
dLacpExtGroupEntry = _DLacpExtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1)
)
dLacpExtGroupEntry.setIndexNames(
    (0, "DLINKSW-LACP-EXT-MIB", "dLacpExtGroupChannelNo"),
)
if mibBuilder.loadTexts:
    dLacpExtGroupEntry.setStatus("current")


class _DLacpExtGroupChannelNo_Type(Integer32):
    """Custom type dLacpExtGroupChannelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DLacpExtGroupChannelNo_Type.__name__ = "Integer32"
_DLacpExtGroupChannelNo_Object = MibTableColumn
dLacpExtGroupChannelNo = _DLacpExtGroupChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 1),
    _DLacpExtGroupChannelNo_Type()
)
dLacpExtGroupChannelNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dLacpExtGroupChannelNo.setStatus("current")
_DLacpExtGroupIfIndex_Type = InterfaceIndex
_DLacpExtGroupIfIndex_Object = MibTableColumn
dLacpExtGroupIfIndex = _DLacpExtGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 2),
    _DLacpExtGroupIfIndex_Type()
)
dLacpExtGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dLacpExtGroupIfIndex.setStatus("current")


class _DLacpExtGroupType_Type(Integer32):
    """Custom type dLacpExtGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2))
    )


_DLacpExtGroupType_Type.__name__ = "Integer32"
_DLacpExtGroupType_Object = MibTableColumn
dLacpExtGroupType = _DLacpExtGroupType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 3),
    _DLacpExtGroupType_Type()
)
dLacpExtGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dLacpExtGroupType.setStatus("current")
_DLacpExtGroupMemberPorts_Type = PortList
_DLacpExtGroupMemberPorts_Object = MibTableColumn
dLacpExtGroupMemberPorts = _DLacpExtGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 4),
    _DLacpExtGroupMemberPorts_Type()
)
dLacpExtGroupMemberPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dLacpExtGroupMemberPorts.setStatus("current")
_DLacpExtGroupActiveMemberPorts_Type = PortList
_DLacpExtGroupActiveMemberPorts_Object = MibTableColumn
dLacpExtGroupActiveMemberPorts = _DLacpExtGroupActiveMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 5),
    _DLacpExtGroupActiveMemberPorts_Type()
)
dLacpExtGroupActiveMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dLacpExtGroupActiveMemberPorts.setStatus("current")
_DLacpExtGroupRowStatus_Type = RowStatus
_DLacpExtGroupRowStatus_Object = MibTableColumn
dLacpExtGroupRowStatus = _DLacpExtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 6),
    _DLacpExtGroupRowStatus_Type()
)
dLacpExtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dLacpExtGroupRowStatus.setStatus("current")
_DLacpExtMIBConformance_ObjectIdentity = ObjectIdentity
dLacpExtMIBConformance = _DLacpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 2)
)
_DLacpExtCompliances_ObjectIdentity = ObjectIdentity
dLacpExtCompliances = _DLacpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 1)
)
_DLacpExtGroups_ObjectIdentity = ObjectIdentity
dLacpExtGroups = _DLacpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 2)
)

# Managed Objects groups

dLacpExtAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 2, 1)
)
dLacpExtAlgGroup.setObjects(
    ("DLINKSW-LACP-EXT-MIB", "dLacpExtLoadBalanceAlgorithm")
)
if mibBuilder.loadTexts:
    dLacpExtAlgGroup.setStatus("current")

dLacpExtChannelGrpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 2, 2)
)
dLacpExtChannelGrpInfoGroup.setObjects(
      *(("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupIfIndex"),
        ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupType"),
        ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupMemberPorts"),
        ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupActiveMemberPorts"),
        ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupRowStatus"))
)
if mibBuilder.loadTexts:
    dLacpExtChannelGrpInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dLacpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 1, 1)
)
dLacpExtCompliance.setObjects(
      *(("DLINKSW-LACP-EXT-MIB", "dLacpExtAlgGroup"),
        ("DLINKSW-LACP-EXT-MIB", "dLacpExtChannelGrpInfoGroup"))
)
if mibBuilder.loadTexts:
    dLacpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-LACP-EXT-MIB",
    **{"dlinkSwLacpExtMIB": dlinkSwLacpExtMIB,
       "dLacpExtMIBNotifications": dLacpExtMIBNotifications,
       "dLacpExtMIBObjects": dLacpExtMIBObjects,
       "dLacpExtLoadBalanceAlgorithm": dLacpExtLoadBalanceAlgorithm,
       "dLacpExtGroupTable": dLacpExtGroupTable,
       "dLacpExtGroupEntry": dLacpExtGroupEntry,
       "dLacpExtGroupChannelNo": dLacpExtGroupChannelNo,
       "dLacpExtGroupIfIndex": dLacpExtGroupIfIndex,
       "dLacpExtGroupType": dLacpExtGroupType,
       "dLacpExtGroupMemberPorts": dLacpExtGroupMemberPorts,
       "dLacpExtGroupActiveMemberPorts": dLacpExtGroupActiveMemberPorts,
       "dLacpExtGroupRowStatus": dLacpExtGroupRowStatus,
       "dLacpExtMIBConformance": dLacpExtMIBConformance,
       "dLacpExtCompliances": dLacpExtCompliances,
       "dLacpExtCompliance": dLacpExtCompliance,
       "dLacpExtGroups": dLacpExtGroups,
       "dLacpExtAlgGroup": dLacpExtAlgGroup,
       "dLacpExtChannelGrpInfoGroup": dLacpExtChannelGrpInfoGroup}
)
