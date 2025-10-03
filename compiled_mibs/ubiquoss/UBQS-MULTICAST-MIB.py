# SNMP MIB module (UBQS-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:26 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiMulticastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiMulticastMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiMulticastMIBNotificationPrefix = _UbiMulticastMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 0)
)
_UbiIgmpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
ubiIgmpSnoopingMIBObjects = _UbiIgmpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1)
)
_UbiIgmpSnoopVlanConfigTable_Object = MibTable
ubiIgmpSnoopVlanConfigTable = _UbiIgmpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1)
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanConfigTable.setStatus("current")
_UbiIgmpSnoopVlanConfigEntry_Object = MibTableRow
ubiIgmpSnoopVlanConfigEntry = _UbiIgmpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1)
)
ubiIgmpSnoopVlanConfigEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanConfigEntry.setStatus("current")
_UbiIgmpSnoopVlanIndex_Type = VlanIndex
_UbiIgmpSnoopVlanIndex_Object = MibTableColumn
ubiIgmpSnoopVlanIndex = _UbiIgmpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 1),
    _UbiIgmpSnoopVlanIndex_Type()
)
ubiIgmpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanIndex.setStatus("current")
_UbiIgmpSnoopVlanEnabled_Type = TruthValue
_UbiIgmpSnoopVlanEnabled_Object = MibTableColumn
ubiIgmpSnoopVlanEnabled = _UbiIgmpSnoopVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 2),
    _UbiIgmpSnoopVlanEnabled_Type()
)
ubiIgmpSnoopVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanEnabled.setStatus("current")
_UbiIgmpSnoopVlanFastLeaveEnabled_Type = TruthValue
_UbiIgmpSnoopVlanFastLeaveEnabled_Object = MibTableColumn
ubiIgmpSnoopVlanFastLeaveEnabled = _UbiIgmpSnoopVlanFastLeaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 3),
    _UbiIgmpSnoopVlanFastLeaveEnabled_Type()
)
ubiIgmpSnoopVlanFastLeaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanFastLeaveEnabled.setStatus("current")
_UbiIgmpSnoopVlanReportSuppressionEnabled_Type = TruthValue
_UbiIgmpSnoopVlanReportSuppressionEnabled_Object = MibTableColumn
ubiIgmpSnoopVlanReportSuppressionEnabled = _UbiIgmpSnoopVlanReportSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 4),
    _UbiIgmpSnoopVlanReportSuppressionEnabled_Type()
)
ubiIgmpSnoopVlanReportSuppressionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanReportSuppressionEnabled.setStatus("current")
_UbiIgmpSnoopVlanForcedSourceIP_Type = IpAddress
_UbiIgmpSnoopVlanForcedSourceIP_Object = MibTableColumn
ubiIgmpSnoopVlanForcedSourceIP = _UbiIgmpSnoopVlanForcedSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 5),
    _UbiIgmpSnoopVlanForcedSourceIP_Type()
)
ubiIgmpSnoopVlanForcedSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanForcedSourceIP.setStatus("current")
_UbiIgmpSnoopVlanRowStatus_Type = RowStatus
_UbiIgmpSnoopVlanRowStatus_Object = MibTableColumn
ubiIgmpSnoopVlanRowStatus = _UbiIgmpSnoopVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 6),
    _UbiIgmpSnoopVlanRowStatus_Type()
)
ubiIgmpSnoopVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanRowStatus.setStatus("current")
_UbiIgmpSnoopVlanSnoopingQuerier_Type = TruthValue
_UbiIgmpSnoopVlanSnoopingQuerier_Object = MibTableColumn
ubiIgmpSnoopVlanSnoopingQuerier = _UbiIgmpSnoopVlanSnoopingQuerier_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 7),
    _UbiIgmpSnoopVlanSnoopingQuerier_Type()
)
ubiIgmpSnoopVlanSnoopingQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanSnoopingQuerier.setStatus("current")
_UbiIgmpSnoopVlanLastMemberQuery_Type = TruthValue
_UbiIgmpSnoopVlanLastMemberQuery_Object = MibTableColumn
ubiIgmpSnoopVlanLastMemberQuery = _UbiIgmpSnoopVlanLastMemberQuery_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 8),
    _UbiIgmpSnoopVlanLastMemberQuery_Type()
)
ubiIgmpSnoopVlanLastMemberQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanLastMemberQuery.setStatus("current")


class _UbiIgmpSnoopVlanVlantagCos_Type(Integer32):
    """Custom type ubiIgmpSnoopVlanVlantagCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_UbiIgmpSnoopVlanVlantagCos_Type.__name__ = "Integer32"
_UbiIgmpSnoopVlanVlantagCos_Object = MibTableColumn
ubiIgmpSnoopVlanVlantagCos = _UbiIgmpSnoopVlanVlantagCos_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 1, 1, 9),
    _UbiIgmpSnoopVlanVlantagCos_Type()
)
ubiIgmpSnoopVlanVlantagCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanVlantagCos.setStatus("current")
_UbiIgmpSnoopMrouterTable_Object = MibTable
ubiIgmpSnoopMrouterTable = _UbiIgmpSnoopMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 2)
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopMrouterTable.setStatus("current")
_UbiIgmpSnoopMrouterEntry_Object = MibTableRow
ubiIgmpSnoopMrouterEntry = _UbiIgmpSnoopMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 2, 1)
)
ubiIgmpSnoopMrouterEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopMrouterVlanIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopMrouterIfIndex"),
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopMrouterEntry.setStatus("current")
_UbiIgmpSnoopMrouterVlanIndex_Type = VlanIndex
_UbiIgmpSnoopMrouterVlanIndex_Object = MibTableColumn
ubiIgmpSnoopMrouterVlanIndex = _UbiIgmpSnoopMrouterVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 2, 1, 1),
    _UbiIgmpSnoopMrouterVlanIndex_Type()
)
ubiIgmpSnoopMrouterVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopMrouterVlanIndex.setStatus("current")
_UbiIgmpSnoopMrouterIfIndex_Type = Integer32
_UbiIgmpSnoopMrouterIfIndex_Object = MibTableColumn
ubiIgmpSnoopMrouterIfIndex = _UbiIgmpSnoopMrouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 2, 1, 2),
    _UbiIgmpSnoopMrouterIfIndex_Type()
)
ubiIgmpSnoopMrouterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopMrouterIfIndex.setStatus("current")
_UbiIgmpSnoopMrouterSVlanID_Type = VlanIndex
_UbiIgmpSnoopMrouterSVlanID_Object = MibTableColumn
ubiIgmpSnoopMrouterSVlanID = _UbiIgmpSnoopMrouterSVlanID_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 2, 1, 3),
    _UbiIgmpSnoopMrouterSVlanID_Type()
)
ubiIgmpSnoopMrouterSVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopMrouterSVlanID.setStatus("current")
_UbiIgmpSnoopMrouterRowStatus_Type = RowStatus
_UbiIgmpSnoopMrouterRowStatus_Object = MibTableColumn
ubiIgmpSnoopMrouterRowStatus = _UbiIgmpSnoopMrouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 2, 1, 4),
    _UbiIgmpSnoopMrouterRowStatus_Type()
)
ubiIgmpSnoopMrouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIgmpSnoopMrouterRowStatus.setStatus("current")
_UbiIgmpSnoopStaticGroupTable_Object = MibTable
ubiIgmpSnoopStaticGroupTable = _UbiIgmpSnoopStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 3)
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopStaticGroupTable.setStatus("current")
_UbiIgmpSnoopStaticGroupEntry_Object = MibTableRow
ubiIgmpSnoopStaticGroupEntry = _UbiIgmpSnoopStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 3, 1)
)
ubiIgmpSnoopStaticGroupEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopStaticGroupVlanIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopStaticGroupIfIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopStaticGroupAddress"),
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopStaticGroupEntry.setStatus("current")
_UbiIgmpSnoopStaticGroupVlanIndex_Type = VlanIndex
_UbiIgmpSnoopStaticGroupVlanIndex_Object = MibTableColumn
ubiIgmpSnoopStaticGroupVlanIndex = _UbiIgmpSnoopStaticGroupVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 3, 1, 1),
    _UbiIgmpSnoopStaticGroupVlanIndex_Type()
)
ubiIgmpSnoopStaticGroupVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopStaticGroupVlanIndex.setStatus("current")
_UbiIgmpSnoopStaticGroupIfIndex_Type = Integer32
_UbiIgmpSnoopStaticGroupIfIndex_Object = MibTableColumn
ubiIgmpSnoopStaticGroupIfIndex = _UbiIgmpSnoopStaticGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 3, 1, 2),
    _UbiIgmpSnoopStaticGroupIfIndex_Type()
)
ubiIgmpSnoopStaticGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopStaticGroupIfIndex.setStatus("current")
_UbiIgmpSnoopStaticGroupAddress_Type = IpAddress
_UbiIgmpSnoopStaticGroupAddress_Object = MibTableColumn
ubiIgmpSnoopStaticGroupAddress = _UbiIgmpSnoopStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 3, 1, 3),
    _UbiIgmpSnoopStaticGroupAddress_Type()
)
ubiIgmpSnoopStaticGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopStaticGroupAddress.setStatus("current")
_UbiIgmpSnoopStaticGroupRowStatus_Type = RowStatus
_UbiIgmpSnoopStaticGroupRowStatus_Object = MibTableColumn
ubiIgmpSnoopStaticGroupRowStatus = _UbiIgmpSnoopStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 3, 1, 4),
    _UbiIgmpSnoopStaticGroupRowStatus_Type()
)
ubiIgmpSnoopStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIgmpSnoopStaticGroupRowStatus.setStatus("current")
_UbiIgmpSnoopPortConfigAclTable_Object = MibTable
ubiIgmpSnoopPortConfigAclTable = _UbiIgmpSnoopPortConfigAclTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 4)
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopPortConfigAclTable.setStatus("current")
_UbiIgmpSnoopPortConfigAclEntry_Object = MibTableRow
ubiIgmpSnoopPortConfigAclEntry = _UbiIgmpSnoopPortConfigAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 4, 1)
)
ubiIgmpSnoopPortConfigAclEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopPortConfigAclIfIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopPortConfigAclVlanID"),
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopPortConfigAclEntry.setStatus("current")
_UbiIgmpSnoopPortConfigAclIfIndex_Type = Integer32
_UbiIgmpSnoopPortConfigAclIfIndex_Object = MibTableColumn
ubiIgmpSnoopPortConfigAclIfIndex = _UbiIgmpSnoopPortConfigAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 4, 1, 1),
    _UbiIgmpSnoopPortConfigAclIfIndex_Type()
)
ubiIgmpSnoopPortConfigAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopPortConfigAclIfIndex.setStatus("current")
_UbiIgmpSnoopPortConfigAclVlanID_Type = VlanIndex
_UbiIgmpSnoopPortConfigAclVlanID_Object = MibTableColumn
ubiIgmpSnoopPortConfigAclVlanID = _UbiIgmpSnoopPortConfigAclVlanID_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 4, 1, 2),
    _UbiIgmpSnoopPortConfigAclVlanID_Type()
)
ubiIgmpSnoopPortConfigAclVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopPortConfigAclVlanID.setStatus("current")


class _UbiIgmpSnoopPortConfigAclName_Type(DisplayString):
    """Custom type ubiIgmpSnoopPortConfigAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_UbiIgmpSnoopPortConfigAclName_Type.__name__ = "DisplayString"
_UbiIgmpSnoopPortConfigAclName_Object = MibTableColumn
ubiIgmpSnoopPortConfigAclName = _UbiIgmpSnoopPortConfigAclName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 4, 1, 3),
    _UbiIgmpSnoopPortConfigAclName_Type()
)
ubiIgmpSnoopPortConfigAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpSnoopPortConfigAclName.setStatus("current")
_UbiIgmpSnoopPortConfigAclRowStatus_Type = RowStatus
_UbiIgmpSnoopPortConfigAclRowStatus_Object = MibTableColumn
ubiIgmpSnoopPortConfigAclRowStatus = _UbiIgmpSnoopPortConfigAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 4, 1, 4),
    _UbiIgmpSnoopPortConfigAclRowStatus_Type()
)
ubiIgmpSnoopPortConfigAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIgmpSnoopPortConfigAclRowStatus.setStatus("current")
_UbiIgmpSnoopReporterTable_Object = MibTable
ubiIgmpSnoopReporterTable = _UbiIgmpSnoopReporterTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 5)
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopReporterTable.setStatus("current")
_UbiIgmpSnoopReporterEntry_Object = MibTableRow
ubiIgmpSnoopReporterEntry = _UbiIgmpSnoopReporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 5, 1)
)
ubiIgmpSnoopReporterEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterIfIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterGroupAddress"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterAddress"),
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopReporterEntry.setStatus("current")
_UbiIgmpSnoopReporterIfIndex_Type = Integer32
_UbiIgmpSnoopReporterIfIndex_Object = MibTableColumn
ubiIgmpSnoopReporterIfIndex = _UbiIgmpSnoopReporterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 5, 1, 1),
    _UbiIgmpSnoopReporterIfIndex_Type()
)
ubiIgmpSnoopReporterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopReporterIfIndex.setStatus("current")
_UbiIgmpSnoopReporterGroupAddress_Type = IpAddress
_UbiIgmpSnoopReporterGroupAddress_Object = MibTableColumn
ubiIgmpSnoopReporterGroupAddress = _UbiIgmpSnoopReporterGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 5, 1, 2),
    _UbiIgmpSnoopReporterGroupAddress_Type()
)
ubiIgmpSnoopReporterGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopReporterGroupAddress.setStatus("current")
_UbiIgmpSnoopReporterAddress_Type = IpAddress
_UbiIgmpSnoopReporterAddress_Object = MibTableColumn
ubiIgmpSnoopReporterAddress = _UbiIgmpSnoopReporterAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 5, 1, 3),
    _UbiIgmpSnoopReporterAddress_Type()
)
ubiIgmpSnoopReporterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopReporterAddress.setStatus("current")
_UbiIgmpSnoopReporterUptime_Type = TimeTicks
_UbiIgmpSnoopReporterUptime_Object = MibTableColumn
ubiIgmpSnoopReporterUptime = _UbiIgmpSnoopReporterUptime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 5, 1, 4),
    _UbiIgmpSnoopReporterUptime_Type()
)
ubiIgmpSnoopReporterUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopReporterUptime.setStatus("current")
_UbiIgmpSnoopReporterExpireTime_Type = TimeTicks
_UbiIgmpSnoopReporterExpireTime_Object = MibTableColumn
ubiIgmpSnoopReporterExpireTime = _UbiIgmpSnoopReporterExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 5, 1, 5),
    _UbiIgmpSnoopReporterExpireTime_Type()
)
ubiIgmpSnoopReporterExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopReporterExpireTime.setStatus("current")
_UbiIgmpSnoopCacheTable_Object = MibTable
ubiIgmpSnoopCacheTable = _UbiIgmpSnoopCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6)
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheTable.setStatus("current")
_UbiIgmpSnoopCacheEntry_Object = MibTableRow
ubiIgmpSnoopCacheEntry = _UbiIgmpSnoopCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6, 1)
)
ubiIgmpSnoopCacheEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopCacheVlanIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopCacheIfIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopCacheAddress"),
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheEntry.setStatus("current")
_UbiIgmpSnoopCacheVlanIndex_Type = InterfaceIndex
_UbiIgmpSnoopCacheVlanIndex_Object = MibTableColumn
ubiIgmpSnoopCacheVlanIndex = _UbiIgmpSnoopCacheVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6, 1, 1),
    _UbiIgmpSnoopCacheVlanIndex_Type()
)
ubiIgmpSnoopCacheVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheVlanIndex.setStatus("current")
_UbiIgmpSnoopCacheIfIndex_Type = InterfaceIndex
_UbiIgmpSnoopCacheIfIndex_Object = MibTableColumn
ubiIgmpSnoopCacheIfIndex = _UbiIgmpSnoopCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6, 1, 2),
    _UbiIgmpSnoopCacheIfIndex_Type()
)
ubiIgmpSnoopCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheIfIndex.setStatus("current")


class _UbiIgmpSnoopCacheAddress_Type(InetAddress):
    """Custom type ubiIgmpSnoopCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_UbiIgmpSnoopCacheAddress_Type.__name__ = "InetAddress"
_UbiIgmpSnoopCacheAddress_Object = MibTableColumn
ubiIgmpSnoopCacheAddress = _UbiIgmpSnoopCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6, 1, 3),
    _UbiIgmpSnoopCacheAddress_Type()
)
ubiIgmpSnoopCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheAddress.setStatus("current")
_UbiIgmpSnoopCacheUpTime_Type = TimeTicks
_UbiIgmpSnoopCacheUpTime_Object = MibTableColumn
ubiIgmpSnoopCacheUpTime = _UbiIgmpSnoopCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6, 1, 4),
    _UbiIgmpSnoopCacheUpTime_Type()
)
ubiIgmpSnoopCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheUpTime.setStatus("current")
_UbiIgmpSnoopCacheExpireTime_Type = TimeTicks
_UbiIgmpSnoopCacheExpireTime_Object = MibTableColumn
ubiIgmpSnoopCacheExpireTime = _UbiIgmpSnoopCacheExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6, 1, 5),
    _UbiIgmpSnoopCacheExpireTime_Type()
)
ubiIgmpSnoopCacheExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheExpireTime.setStatus("current")


class _UbiIgmpSnoopCacheLastReporter_Type(InetAddress):
    """Custom type ubiIgmpSnoopCacheLastReporter based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_UbiIgmpSnoopCacheLastReporter_Type.__name__ = "InetAddress"
_UbiIgmpSnoopCacheLastReporter_Object = MibTableColumn
ubiIgmpSnoopCacheLastReporter = _UbiIgmpSnoopCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 1, 6, 1, 6),
    _UbiIgmpSnoopCacheLastReporter_Type()
)
ubiIgmpSnoopCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopCacheLastReporter.setStatus("current")
_UbiMvrMIBObjects_ObjectIdentity = ObjectIdentity
ubiMvrMIBObjects = _UbiMvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2)
)


class _UbiMvrGlobalConfigEnable_Type(Integer32):
    """Custom type ubiMvrGlobalConfigEnable based on Integer32"""
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


_UbiMvrGlobalConfigEnable_Type.__name__ = "Integer32"
_UbiMvrGlobalConfigEnable_Object = MibScalar
ubiMvrGlobalConfigEnable = _UbiMvrGlobalConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2, 1),
    _UbiMvrGlobalConfigEnable_Type()
)
ubiMvrGlobalConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiMvrGlobalConfigEnable.setStatus("current")
_UbiMvrPortConfigTable_Object = MibTable
ubiMvrPortConfigTable = _UbiMvrPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2, 2)
)
if mibBuilder.loadTexts:
    ubiMvrPortConfigTable.setStatus("current")
_UbiMvrPortConfigEntry_Object = MibTableRow
ubiMvrPortConfigEntry = _UbiMvrPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2, 2, 1)
)
ubiMvrPortConfigEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "IfIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiMvrPortConfigVlanid"),
    (0, "UBQS-MULTICAST-MIB", "ubiMvrPortConfigGroupaddress"),
    (0, "UBQS-MULTICAST-MIB", "ubiMvrPortConfigGroupCount"),
)
if mibBuilder.loadTexts:
    ubiMvrPortConfigEntry.setStatus("current")
_UbiMvrPortConfigVlanid_Type = Integer32
_UbiMvrPortConfigVlanid_Object = MibTableColumn
ubiMvrPortConfigVlanid = _UbiMvrPortConfigVlanid_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2, 2, 1, 1),
    _UbiMvrPortConfigVlanid_Type()
)
ubiMvrPortConfigVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiMvrPortConfigVlanid.setStatus("current")
_UbiMvrPortConfigGroupaddress_Type = IpAddress
_UbiMvrPortConfigGroupaddress_Object = MibTableColumn
ubiMvrPortConfigGroupaddress = _UbiMvrPortConfigGroupaddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2, 2, 1, 2),
    _UbiMvrPortConfigGroupaddress_Type()
)
ubiMvrPortConfigGroupaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiMvrPortConfigGroupaddress.setStatus("current")


class _UbiMvrPortConfigGroupCount_Type(Integer32):
    """Custom type ubiMvrPortConfigGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_UbiMvrPortConfigGroupCount_Type.__name__ = "Integer32"
_UbiMvrPortConfigGroupCount_Object = MibTableColumn
ubiMvrPortConfigGroupCount = _UbiMvrPortConfigGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2, 2, 1, 3),
    _UbiMvrPortConfigGroupCount_Type()
)
ubiMvrPortConfigGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiMvrPortConfigGroupCount.setStatus("current")
_UbiMvrPortConfigRowStatus_Type = RowStatus
_UbiMvrPortConfigRowStatus_Object = MibTableColumn
ubiMvrPortConfigRowStatus = _UbiMvrPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 2, 2, 1, 4),
    _UbiMvrPortConfigRowStatus_Type()
)
ubiMvrPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiMvrPortConfigRowStatus.setStatus("current")
_UbiIgmpStatsMIBObjects_ObjectIdentity = ObjectIdentity
ubiIgmpStatsMIBObjects = _UbiIgmpStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3)
)


class _UbiIgmpClearStatistics_Type(Integer32):
    """Custom type ubiIgmpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_UbiIgmpClearStatistics_Type.__name__ = "Integer32"
_UbiIgmpClearStatistics_Object = MibScalar
ubiIgmpClearStatistics = _UbiIgmpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 1),
    _UbiIgmpClearStatistics_Type()
)
ubiIgmpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiIgmpClearStatistics.setStatus("current")
_UbiIgmpVlanStatsTable_Object = MibTable
ubiIgmpVlanStatsTable = _UbiIgmpVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2)
)
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsTable.setStatus("current")
_UbiIgmpVlanStatsEntry_Object = MibTableRow
ubiIgmpVlanStatsEntry = _UbiIgmpVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1)
)
ubiIgmpVlanStatsEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiVlanIfIndex"),
)
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsEntry.setStatus("current")
_UbiIgmpVlanStatsEntryCount_Type = Counter64
_UbiIgmpVlanStatsEntryCount_Object = MibTableColumn
ubiIgmpVlanStatsEntryCount = _UbiIgmpVlanStatsEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 1),
    _UbiIgmpVlanStatsEntryCount_Type()
)
ubiIgmpVlanStatsEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsEntryCount.setStatus("current")
_UbiIgmpVlanStatsReportTxTotal_Type = Counter64
_UbiIgmpVlanStatsReportTxTotal_Object = MibTableColumn
ubiIgmpVlanStatsReportTxTotal = _UbiIgmpVlanStatsReportTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 2),
    _UbiIgmpVlanStatsReportTxTotal_Type()
)
ubiIgmpVlanStatsReportTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsReportTxTotal.setStatus("current")
_UbiIgmpVlanStatsReportRxTotal_Type = Counter64
_UbiIgmpVlanStatsReportRxTotal_Object = MibTableColumn
ubiIgmpVlanStatsReportRxTotal = _UbiIgmpVlanStatsReportRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 3),
    _UbiIgmpVlanStatsReportRxTotal_Type()
)
ubiIgmpVlanStatsReportRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsReportRxTotal.setStatus("current")
_UbiIgmpVlanStatsReportRxSuccess_Type = Counter64
_UbiIgmpVlanStatsReportRxSuccess_Object = MibTableColumn
ubiIgmpVlanStatsReportRxSuccess = _UbiIgmpVlanStatsReportRxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 4),
    _UbiIgmpVlanStatsReportRxSuccess_Type()
)
ubiIgmpVlanStatsReportRxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsReportRxSuccess.setStatus("current")
_UbiIgmpVlanStatsReportRxUnsuccess_Type = Counter64
_UbiIgmpVlanStatsReportRxUnsuccess_Object = MibTableColumn
ubiIgmpVlanStatsReportRxUnsuccess = _UbiIgmpVlanStatsReportRxUnsuccess_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 5),
    _UbiIgmpVlanStatsReportRxUnsuccess_Type()
)
ubiIgmpVlanStatsReportRxUnsuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsReportRxUnsuccess.setStatus("current")
_UbiIgmpVlanStatsLeaveTxTotal_Type = Counter64
_UbiIgmpVlanStatsLeaveTxTotal_Object = MibTableColumn
ubiIgmpVlanStatsLeaveTxTotal = _UbiIgmpVlanStatsLeaveTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 6),
    _UbiIgmpVlanStatsLeaveTxTotal_Type()
)
ubiIgmpVlanStatsLeaveTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsLeaveTxTotal.setStatus("current")
_UbiIgmpVlanStatsLeaveRxTotal_Type = Counter64
_UbiIgmpVlanStatsLeaveRxTotal_Object = MibTableColumn
ubiIgmpVlanStatsLeaveRxTotal = _UbiIgmpVlanStatsLeaveRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 7),
    _UbiIgmpVlanStatsLeaveRxTotal_Type()
)
ubiIgmpVlanStatsLeaveRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsLeaveRxTotal.setStatus("current")
_UbiIgmpVlanStatsGeneralQueryTxTotal_Type = Counter64
_UbiIgmpVlanStatsGeneralQueryTxTotal_Object = MibTableColumn
ubiIgmpVlanStatsGeneralQueryTxTotal = _UbiIgmpVlanStatsGeneralQueryTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 8),
    _UbiIgmpVlanStatsGeneralQueryTxTotal_Type()
)
ubiIgmpVlanStatsGeneralQueryTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsGeneralQueryTxTotal.setStatus("current")
_UbiIgmpVlanStatsGeneralQueryRxTotal_Type = Counter64
_UbiIgmpVlanStatsGeneralQueryRxTotal_Object = MibTableColumn
ubiIgmpVlanStatsGeneralQueryRxTotal = _UbiIgmpVlanStatsGeneralQueryRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 9),
    _UbiIgmpVlanStatsGeneralQueryRxTotal_Type()
)
ubiIgmpVlanStatsGeneralQueryRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsGeneralQueryRxTotal.setStatus("current")
_UbiIgmpVlanStatsGroupSpecificQueryTxTotal_Type = Counter64
_UbiIgmpVlanStatsGroupSpecificQueryTxTotal_Object = MibTableColumn
ubiIgmpVlanStatsGroupSpecificQueryTxTotal = _UbiIgmpVlanStatsGroupSpecificQueryTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 10),
    _UbiIgmpVlanStatsGroupSpecificQueryTxTotal_Type()
)
ubiIgmpVlanStatsGroupSpecificQueryTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsGroupSpecificQueryTxTotal.setStatus("current")
_UbiIgmpVlanStatsGroupSpecificQueryRxTotal_Type = Counter64
_UbiIgmpVlanStatsGroupSpecificQueryRxTotal_Object = MibTableColumn
ubiIgmpVlanStatsGroupSpecificQueryRxTotal = _UbiIgmpVlanStatsGroupSpecificQueryRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 11),
    _UbiIgmpVlanStatsGroupSpecificQueryRxTotal_Type()
)
ubiIgmpVlanStatsGroupSpecificQueryRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsGroupSpecificQueryRxTotal.setStatus("current")
_UbiIgmpVlanStatsInvalidMessageRxTotal_Type = Counter64
_UbiIgmpVlanStatsInvalidMessageRxTotal_Object = MibTableColumn
ubiIgmpVlanStatsInvalidMessageRxTotal = _UbiIgmpVlanStatsInvalidMessageRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 2, 1, 12),
    _UbiIgmpVlanStatsInvalidMessageRxTotal_Type()
)
ubiIgmpVlanStatsInvalidMessageRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpVlanStatsInvalidMessageRxTotal.setStatus("current")
_UbiIgmpSnoopMembershipCountTable_Object = MibTable
ubiIgmpSnoopMembershipCountTable = _UbiIgmpSnoopMembershipCountTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 3)
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopMembershipCountTable.setStatus("current")
_UbiIgmpSnoopMembershipCountEntry_Object = MibTableRow
ubiIgmpSnoopMembershipCountEntry = _UbiIgmpSnoopMembershipCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 3, 1)
)
ubiIgmpSnoopMembershipCountEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "ubiVlanIfIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpSnoopCacheAddress"),
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopMembershipCountEntry.setStatus("current")
_UbiIgmpSnoopMembershipCount_Type = Counter64
_UbiIgmpSnoopMembershipCount_Object = MibTableColumn
ubiIgmpSnoopMembershipCount = _UbiIgmpSnoopMembershipCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 3, 3, 1, 1),
    _UbiIgmpSnoopMembershipCount_Type()
)
ubiIgmpSnoopMembershipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpSnoopMembershipCount.setStatus("current")
_UbiMldSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
ubiMldSnoopingMIBObjects = _UbiMldSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 4)
)
_UbiIgmpProxyRoutingMIBObjects_ObjectIdentity = ObjectIdentity
ubiIgmpProxyRoutingMIBObjects = _UbiIgmpProxyRoutingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5)
)
_UbiIgmpProxyRoutingIfMRouteCountTable_Object = MibTable
ubiIgmpProxyRoutingIfMRouteCountTable = _UbiIgmpProxyRoutingIfMRouteCountTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 1)
)
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingIfMRouteCountTable.setStatus("mandatory")
_UbiIgmpProxyRoutingIfMRouteCountEntry_Object = MibTableRow
ubiIgmpProxyRoutingIfMRouteCountEntry = _UbiIgmpProxyRoutingIfMRouteCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 1, 1)
)
ubiIgmpProxyRoutingIfMRouteCountEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "IfIndex"),
)
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingIfMRouteCountEntry.setStatus("mandatory")
_UbiIgmpProxyRoutingIfMRouteCountInterface_Type = OctetString
_UbiIgmpProxyRoutingIfMRouteCountInterface_Object = MibTableColumn
ubiIgmpProxyRoutingIfMRouteCountInterface = _UbiIgmpProxyRoutingIfMRouteCountInterface_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 1, 1, 1),
    _UbiIgmpProxyRoutingIfMRouteCountInterface_Type()
)
ubiIgmpProxyRoutingIfMRouteCountInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingIfMRouteCountInterface.setStatus("mandatory")
_UbiIgmpProxyRoutingOutIfMRouteCount_Type = Counter32
_UbiIgmpProxyRoutingOutIfMRouteCount_Object = MibTableColumn
ubiIgmpProxyRoutingOutIfMRouteCount = _UbiIgmpProxyRoutingOutIfMRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 1, 1, 2),
    _UbiIgmpProxyRoutingOutIfMRouteCount_Type()
)
ubiIgmpProxyRoutingOutIfMRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingOutIfMRouteCount.setStatus("mandatory")
_UbiIgmpProxyRoutingOutIfMRouteTable_Object = MibTable
ubiIgmpProxyRoutingOutIfMRouteTable = _UbiIgmpProxyRoutingOutIfMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 2)
)
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingOutIfMRouteTable.setStatus("mandatory")
_UbiIgmpProxyRoutingOutIfMRouteEntry_Object = MibTableRow
ubiIgmpProxyRoutingOutIfMRouteEntry = _UbiIgmpProxyRoutingOutIfMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 2, 1)
)
ubiIgmpProxyRoutingOutIfMRouteEntry.setIndexNames(
    (0, "UBQS-MULTICAST-MIB", "IfIndex"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpProxyRoutingOutIfMRouteGroup"),
    (0, "UBQS-MULTICAST-MIB", "ubiIgmpProxyRoutingOutIfMRouteSource"),
)
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingOutIfMRouteEntry.setStatus("mandatory")
_UbiIgmpProxyRoutingOutIfMRouteInterface_Type = OctetString
_UbiIgmpProxyRoutingOutIfMRouteInterface_Object = MibTableColumn
ubiIgmpProxyRoutingOutIfMRouteInterface = _UbiIgmpProxyRoutingOutIfMRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 2, 1, 1),
    _UbiIgmpProxyRoutingOutIfMRouteInterface_Type()
)
ubiIgmpProxyRoutingOutIfMRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingOutIfMRouteInterface.setStatus("mandatory")
_UbiIgmpProxyRoutingOutIfMRouteGroup_Type = IpAddress
_UbiIgmpProxyRoutingOutIfMRouteGroup_Object = MibTableColumn
ubiIgmpProxyRoutingOutIfMRouteGroup = _UbiIgmpProxyRoutingOutIfMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 2, 1, 2),
    _UbiIgmpProxyRoutingOutIfMRouteGroup_Type()
)
ubiIgmpProxyRoutingOutIfMRouteGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingOutIfMRouteGroup.setStatus("mandatory")
_UbiIgmpProxyRoutingOutIfMRouteSource_Type = IpAddress
_UbiIgmpProxyRoutingOutIfMRouteSource_Object = MibTableColumn
ubiIgmpProxyRoutingOutIfMRouteSource = _UbiIgmpProxyRoutingOutIfMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 5, 2, 1, 3),
    _UbiIgmpProxyRoutingOutIfMRouteSource_Type()
)
ubiIgmpProxyRoutingOutIfMRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIgmpProxyRoutingOutIfMRouteSource.setStatus("mandatory")
_UbiMulticastMIBConformance_ObjectIdentity = ObjectIdentity
ubiMulticastMIBConformance = _UbiMulticastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 10)
)
_UbiMulticastMIBCompliances_ObjectIdentity = ObjectIdentity
ubiMulticastMIBCompliances = _UbiMulticastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 10, 1)
)
_UbiMulticastMIBGroups_ObjectIdentity = ObjectIdentity
ubiMulticastMIBGroups = _UbiMulticastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 10, 2)
)

# Managed Objects groups

ubiIgmpSnoopConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 10, 2, 1)
)
ubiIgmpSnoopConfigGroup.setObjects(
      *(("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanEnabled"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanFastLeaveEnabled"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanReportSuppressionEnabled"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanForcedSourceIP"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanRowStatus"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopMrouterVlanIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopMrouterIfIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopMrouterSVlanID"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopMrouterRowStatus"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopStaticGroupVlanIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopStaticGroupIfIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopStaticGroupIpAddress"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopStaticGroupRowStatus"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopPortConfigAclIfIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopPortConfigAclID"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopPortConfigAclVlanID"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopPortConfigAclRowStatus"))
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopConfigGroup.setStatus("current")

ubiIgmpSnoopInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 10, 2, 2)
)
ubiIgmpSnoopInfoGroup.setObjects(
      *(("UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterIfIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterGroupAddress"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterUptime"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterExpireTime"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopReporterLastAddress"))
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopInfoGroup.setStatus("current")


# Notification objects

ubiIgmpSnoopVlanNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 0, 1)
)
ubiIgmpSnoopVlanNotification.setObjects(
      *(("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanIndex"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopVlanEnabled"))
)
if mibBuilder.loadTexts:
    ubiIgmpSnoopVlanNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ubiMulticastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 21, 10, 1, 1)
)
ubiMulticastMIBCompliance.setObjects(
      *(("UBQS-MULTICAST-MIB", "ubiIgmpSnoopConfigGroup"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopInfoGroup"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopConfigGroup"),
        ("UBQS-MULTICAST-MIB", "ubiIgmpSnoopInfoGroup"))
)
if mibBuilder.loadTexts:
    ubiMulticastMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-MULTICAST-MIB",
    **{"ubiMulticastMIB": ubiMulticastMIB,
       "ubiMulticastMIBNotificationPrefix": ubiMulticastMIBNotificationPrefix,
       "ubiIgmpSnoopVlanNotification": ubiIgmpSnoopVlanNotification,
       "ubiIgmpSnoopingMIBObjects": ubiIgmpSnoopingMIBObjects,
       "ubiIgmpSnoopVlanConfigTable": ubiIgmpSnoopVlanConfigTable,
       "ubiIgmpSnoopVlanConfigEntry": ubiIgmpSnoopVlanConfigEntry,
       "ubiIgmpSnoopVlanIndex": ubiIgmpSnoopVlanIndex,
       "ubiIgmpSnoopVlanEnabled": ubiIgmpSnoopVlanEnabled,
       "ubiIgmpSnoopVlanFastLeaveEnabled": ubiIgmpSnoopVlanFastLeaveEnabled,
       "ubiIgmpSnoopVlanReportSuppressionEnabled": ubiIgmpSnoopVlanReportSuppressionEnabled,
       "ubiIgmpSnoopVlanForcedSourceIP": ubiIgmpSnoopVlanForcedSourceIP,
       "ubiIgmpSnoopVlanRowStatus": ubiIgmpSnoopVlanRowStatus,
       "ubiIgmpSnoopVlanSnoopingQuerier": ubiIgmpSnoopVlanSnoopingQuerier,
       "ubiIgmpSnoopVlanLastMemberQuery": ubiIgmpSnoopVlanLastMemberQuery,
       "ubiIgmpSnoopVlanVlantagCos": ubiIgmpSnoopVlanVlantagCos,
       "ubiIgmpSnoopMrouterTable": ubiIgmpSnoopMrouterTable,
       "ubiIgmpSnoopMrouterEntry": ubiIgmpSnoopMrouterEntry,
       "ubiIgmpSnoopMrouterVlanIndex": ubiIgmpSnoopMrouterVlanIndex,
       "ubiIgmpSnoopMrouterIfIndex": ubiIgmpSnoopMrouterIfIndex,
       "ubiIgmpSnoopMrouterSVlanID": ubiIgmpSnoopMrouterSVlanID,
       "ubiIgmpSnoopMrouterRowStatus": ubiIgmpSnoopMrouterRowStatus,
       "ubiIgmpSnoopStaticGroupTable": ubiIgmpSnoopStaticGroupTable,
       "ubiIgmpSnoopStaticGroupEntry": ubiIgmpSnoopStaticGroupEntry,
       "ubiIgmpSnoopStaticGroupVlanIndex": ubiIgmpSnoopStaticGroupVlanIndex,
       "ubiIgmpSnoopStaticGroupIfIndex": ubiIgmpSnoopStaticGroupIfIndex,
       "ubiIgmpSnoopStaticGroupAddress": ubiIgmpSnoopStaticGroupAddress,
       "ubiIgmpSnoopStaticGroupRowStatus": ubiIgmpSnoopStaticGroupRowStatus,
       "ubiIgmpSnoopPortConfigAclTable": ubiIgmpSnoopPortConfigAclTable,
       "ubiIgmpSnoopPortConfigAclEntry": ubiIgmpSnoopPortConfigAclEntry,
       "ubiIgmpSnoopPortConfigAclIfIndex": ubiIgmpSnoopPortConfigAclIfIndex,
       "ubiIgmpSnoopPortConfigAclVlanID": ubiIgmpSnoopPortConfigAclVlanID,
       "ubiIgmpSnoopPortConfigAclName": ubiIgmpSnoopPortConfigAclName,
       "ubiIgmpSnoopPortConfigAclRowStatus": ubiIgmpSnoopPortConfigAclRowStatus,
       "ubiIgmpSnoopReporterTable": ubiIgmpSnoopReporterTable,
       "ubiIgmpSnoopReporterEntry": ubiIgmpSnoopReporterEntry,
       "ubiIgmpSnoopReporterIfIndex": ubiIgmpSnoopReporterIfIndex,
       "ubiIgmpSnoopReporterGroupAddress": ubiIgmpSnoopReporterGroupAddress,
       "ubiIgmpSnoopReporterAddress": ubiIgmpSnoopReporterAddress,
       "ubiIgmpSnoopReporterUptime": ubiIgmpSnoopReporterUptime,
       "ubiIgmpSnoopReporterExpireTime": ubiIgmpSnoopReporterExpireTime,
       "ubiIgmpSnoopCacheTable": ubiIgmpSnoopCacheTable,
       "ubiIgmpSnoopCacheEntry": ubiIgmpSnoopCacheEntry,
       "ubiIgmpSnoopCacheVlanIndex": ubiIgmpSnoopCacheVlanIndex,
       "ubiIgmpSnoopCacheIfIndex": ubiIgmpSnoopCacheIfIndex,
       "ubiIgmpSnoopCacheAddress": ubiIgmpSnoopCacheAddress,
       "ubiIgmpSnoopCacheUpTime": ubiIgmpSnoopCacheUpTime,
       "ubiIgmpSnoopCacheExpireTime": ubiIgmpSnoopCacheExpireTime,
       "ubiIgmpSnoopCacheLastReporter": ubiIgmpSnoopCacheLastReporter,
       "ubiMvrMIBObjects": ubiMvrMIBObjects,
       "ubiMvrGlobalConfigEnable": ubiMvrGlobalConfigEnable,
       "ubiMvrPortConfigTable": ubiMvrPortConfigTable,
       "ubiMvrPortConfigEntry": ubiMvrPortConfigEntry,
       "ubiMvrPortConfigVlanid": ubiMvrPortConfigVlanid,
       "ubiMvrPortConfigGroupaddress": ubiMvrPortConfigGroupaddress,
       "ubiMvrPortConfigGroupCount": ubiMvrPortConfigGroupCount,
       "ubiMvrPortConfigRowStatus": ubiMvrPortConfigRowStatus,
       "ubiIgmpStatsMIBObjects": ubiIgmpStatsMIBObjects,
       "ubiIgmpClearStatistics": ubiIgmpClearStatistics,
       "ubiIgmpVlanStatsTable": ubiIgmpVlanStatsTable,
       "ubiIgmpVlanStatsEntry": ubiIgmpVlanStatsEntry,
       "ubiIgmpVlanStatsEntryCount": ubiIgmpVlanStatsEntryCount,
       "ubiIgmpVlanStatsReportTxTotal": ubiIgmpVlanStatsReportTxTotal,
       "ubiIgmpVlanStatsReportRxTotal": ubiIgmpVlanStatsReportRxTotal,
       "ubiIgmpVlanStatsReportRxSuccess": ubiIgmpVlanStatsReportRxSuccess,
       "ubiIgmpVlanStatsReportRxUnsuccess": ubiIgmpVlanStatsReportRxUnsuccess,
       "ubiIgmpVlanStatsLeaveTxTotal": ubiIgmpVlanStatsLeaveTxTotal,
       "ubiIgmpVlanStatsLeaveRxTotal": ubiIgmpVlanStatsLeaveRxTotal,
       "ubiIgmpVlanStatsGeneralQueryTxTotal": ubiIgmpVlanStatsGeneralQueryTxTotal,
       "ubiIgmpVlanStatsGeneralQueryRxTotal": ubiIgmpVlanStatsGeneralQueryRxTotal,
       "ubiIgmpVlanStatsGroupSpecificQueryTxTotal": ubiIgmpVlanStatsGroupSpecificQueryTxTotal,
       "ubiIgmpVlanStatsGroupSpecificQueryRxTotal": ubiIgmpVlanStatsGroupSpecificQueryRxTotal,
       "ubiIgmpVlanStatsInvalidMessageRxTotal": ubiIgmpVlanStatsInvalidMessageRxTotal,
       "ubiIgmpSnoopMembershipCountTable": ubiIgmpSnoopMembershipCountTable,
       "ubiIgmpSnoopMembershipCountEntry": ubiIgmpSnoopMembershipCountEntry,
       "ubiIgmpSnoopMembershipCount": ubiIgmpSnoopMembershipCount,
       "ubiMldSnoopingMIBObjects": ubiMldSnoopingMIBObjects,
       "ubiIgmpProxyRoutingMIBObjects": ubiIgmpProxyRoutingMIBObjects,
       "ubiIgmpProxyRoutingIfMRouteCountTable": ubiIgmpProxyRoutingIfMRouteCountTable,
       "ubiIgmpProxyRoutingIfMRouteCountEntry": ubiIgmpProxyRoutingIfMRouteCountEntry,
       "ubiIgmpProxyRoutingIfMRouteCountInterface": ubiIgmpProxyRoutingIfMRouteCountInterface,
       "ubiIgmpProxyRoutingOutIfMRouteCount": ubiIgmpProxyRoutingOutIfMRouteCount,
       "ubiIgmpProxyRoutingOutIfMRouteTable": ubiIgmpProxyRoutingOutIfMRouteTable,
       "ubiIgmpProxyRoutingOutIfMRouteEntry": ubiIgmpProxyRoutingOutIfMRouteEntry,
       "ubiIgmpProxyRoutingOutIfMRouteInterface": ubiIgmpProxyRoutingOutIfMRouteInterface,
       "ubiIgmpProxyRoutingOutIfMRouteGroup": ubiIgmpProxyRoutingOutIfMRouteGroup,
       "ubiIgmpProxyRoutingOutIfMRouteSource": ubiIgmpProxyRoutingOutIfMRouteSource,
       "ubiMulticastMIBConformance": ubiMulticastMIBConformance,
       "ubiMulticastMIBCompliances": ubiMulticastMIBCompliances,
       "ubiMulticastMIBCompliance": ubiMulticastMIBCompliance,
       "ubiMulticastMIBGroups": ubiMulticastMIBGroups,
       "ubiIgmpSnoopConfigGroup": ubiIgmpSnoopConfigGroup,
       "ubiIgmpSnoopInfoGroup": ubiIgmpSnoopInfoGroup}
)
