# SNMP MIB module (TAIT-TN9300-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tait\TAIT-TN9300-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:38 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(taitModules,
 taitProducts) = mibBuilder.importSymbols(
    "TAIT-COMMON-MIB",
    "taitModules",
    "taitProducts")

(ChannelState,
 DipLineState,
 EventSeverity,
 LicenseValidity,
 Mpt1327ChannelState,
 Mpt1327LinkState,
 NetworkCheckState,
 NgwLinkState,
 NodeRequestedState,
 NodeState,
 RemoteNodeState,
 RemoteNodeSyncState,
 SipCallSpeechVotingPriority,
 SipLineIncomingType,
 SipLineRegistrationType,
 SipLineState,
 UnitAuthentication,
 UnitStatusMessageId) = mibBuilder.importSymbols(
    "TAIT-TN9300-TC",
    "ChannelState",
    "DipLineState",
    "EventSeverity",
    "LicenseValidity",
    "Mpt1327ChannelState",
    "Mpt1327LinkState",
    "NetworkCheckState",
    "NgwLinkState",
    "NodeRequestedState",
    "NodeState",
    "RemoteNodeState",
    "RemoteNodeSyncState",
    "SipCallSpeechVotingPriority",
    "SipLineIncomingType",
    "SipLineRegistrationType",
    "SipLineState",
    "UnitAuthentication",
    "UnitStatusMessageId")


# MODULE-IDENTITY

tn9300MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tn9300MibModule.setRevisions(
        ("2019-03-18 14:00",
         "2019-01-28 16:30",
         "2019-01-09 12:00",
         "2018-12-04 12:00",
         "2018-11-23 12:00",
         "2018-11-21 12:00",
         "2018-10-25 12:00",
         "2018-07-31 12:00",
         "2018-07-17 10:05",
         "2018-05-29 12:00",
         "2018-04-23 12:00",
         "2018-04-17 12:00",
         "2018-03-18 22:03",
         "2018-03-08 12:00",
         "2018-03-05 12:00",
         "2018-01-26 00:00",
         "2017-11-22 00:00",
         "2017-05-24 00:00",
         "2017-03-16 00:54",
         "2016-08-22 12:00",
         "2015-10-30 12:00",
         "2015-03-17 22:08",
         "2014-04-04 23:07",
         "2012-11-29 22:01",
         "2012-06-28 22:28",
         "2012-06-27 09:02",
         "2012-05-28 23:17")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tn9300MIB_ObjectIdentity = ObjectIdentity
tn9300MIB = _Tn9300MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6)
)
_Tn9300Confs_ObjectIdentity = ObjectIdentity
tn9300Confs = _Tn9300Confs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1)
)
_Tn9300Groups_ObjectIdentity = ObjectIdentity
tn9300Groups = _Tn9300Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1)
)
_Tn9300Compl_ObjectIdentity = ObjectIdentity
tn9300Compl = _Tn9300Compl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 2)
)
_Tn9300Objs_ObjectIdentity = ObjectIdentity
tn9300Objs = _Tn9300Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2)
)
_Tn9300NodeObjs_ObjectIdentity = ObjectIdentity
tn9300NodeObjs = _Tn9300NodeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1)
)
_Tn9300Version_Type = DisplayString
_Tn9300Version_Object = MibScalar
tn9300Version = _Tn9300Version_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 1),
    _Tn9300Version_Type()
)
tn9300Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Version.setStatus("current")
_Tn9300Name_Type = DisplayString
_Tn9300Name_Object = MibScalar
tn9300Name = _Tn9300Name_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 2),
    _Tn9300Name_Type()
)
tn9300Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Name.setStatus("current")


class _Tn9300Priority_Type(Integer32):
    """Custom type tn9300Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_Tn9300Priority_Type.__name__ = "Integer32"
_Tn9300Priority_Object = MibScalar
tn9300Priority = _Tn9300Priority_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 3),
    _Tn9300Priority_Type()
)
tn9300Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Priority.setStatus("current")
_Tn9300RequestedState_Type = NodeRequestedState
_Tn9300RequestedState_Object = MibScalar
tn9300RequestedState = _Tn9300RequestedState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 4),
    _Tn9300RequestedState_Type()
)
tn9300RequestedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RequestedState.setStatus("current")
_Tn9300State_Type = NodeState
_Tn9300State_Object = MibScalar
tn9300State = _Tn9300State_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 5),
    _Tn9300State_Type()
)
tn9300State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300State.setStatus("current")
_Tn9300NetCheckAddressAType_Type = InetAddressType
_Tn9300NetCheckAddressAType_Object = MibScalar
tn9300NetCheckAddressAType = _Tn9300NetCheckAddressAType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 7),
    _Tn9300NetCheckAddressAType_Type()
)
tn9300NetCheckAddressAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300NetCheckAddressAType.setStatus("current")


class _Tn9300NetCheckAddressA_Type(InetAddress):
    """Custom type tn9300NetCheckAddressA based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300NetCheckAddressA_Type.__name__ = "InetAddress"
_Tn9300NetCheckAddressA_Object = MibScalar
tn9300NetCheckAddressA = _Tn9300NetCheckAddressA_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 8),
    _Tn9300NetCheckAddressA_Type()
)
tn9300NetCheckAddressA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300NetCheckAddressA.setStatus("current")
_Tn9300NetCheckStateA_Type = NetworkCheckState
_Tn9300NetCheckStateA_Object = MibScalar
tn9300NetCheckStateA = _Tn9300NetCheckStateA_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 9),
    _Tn9300NetCheckStateA_Type()
)
tn9300NetCheckStateA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300NetCheckStateA.setStatus("current")
_Tn9300NetCheckAddressBType_Type = InetAddressType
_Tn9300NetCheckAddressBType_Object = MibScalar
tn9300NetCheckAddressBType = _Tn9300NetCheckAddressBType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 10),
    _Tn9300NetCheckAddressBType_Type()
)
tn9300NetCheckAddressBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300NetCheckAddressBType.setStatus("current")


class _Tn9300NetCheckAddressB_Type(InetAddress):
    """Custom type tn9300NetCheckAddressB based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300NetCheckAddressB_Type.__name__ = "InetAddress"
_Tn9300NetCheckAddressB_Object = MibScalar
tn9300NetCheckAddressB = _Tn9300NetCheckAddressB_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 11),
    _Tn9300NetCheckAddressB_Type()
)
tn9300NetCheckAddressB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300NetCheckAddressB.setStatus("current")
_Tn9300NetCheckStateB_Type = NetworkCheckState
_Tn9300NetCheckStateB_Object = MibScalar
tn9300NetCheckStateB = _Tn9300NetCheckStateB_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 12),
    _Tn9300NetCheckStateB_Type()
)
tn9300NetCheckStateB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300NetCheckStateB.setStatus("current")
_Tn9300CallsSwitching_Type = Gauge32
_Tn9300CallsSwitching_Object = MibScalar
tn9300CallsSwitching = _Tn9300CallsSwitching_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 13),
    _Tn9300CallsSwitching_Type()
)
tn9300CallsSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300CallsSwitching.setStatus("current")
_Tn9300ConnectionsSwitching_Type = Gauge32
_Tn9300ConnectionsSwitching_Object = MibScalar
tn9300ConnectionsSwitching = _Tn9300ConnectionsSwitching_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 14),
    _Tn9300ConnectionsSwitching_Type()
)
tn9300ConnectionsSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ConnectionsSwitching.setStatus("current")
_Tn9300MemoryUsage_Type = Gauge32
_Tn9300MemoryUsage_Object = MibScalar
tn9300MemoryUsage = _Tn9300MemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 15),
    _Tn9300MemoryUsage_Type()
)
tn9300MemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MemoryUsage.setStatus("current")
_Tn9300CpuUsage_Type = Gauge32
_Tn9300CpuUsage_Object = MibScalar
tn9300CpuUsage = _Tn9300CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 16),
    _Tn9300CpuUsage_Type()
)
tn9300CpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300CpuUsage.setStatus("current")
_Tn9300DiskSpaceOk_Type = TruthValue
_Tn9300DiskSpaceOk_Object = MibScalar
tn9300DiskSpaceOk = _Tn9300DiskSpaceOk_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 17),
    _Tn9300DiskSpaceOk_Type()
)
tn9300DiskSpaceOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DiskSpaceOk.setStatus("current")
_Tn9300LicenseValidity_Type = LicenseValidity
_Tn9300LicenseValidity_Object = MibScalar
tn9300LicenseValidity = _Tn9300LicenseValidity_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 1, 18),
    _Tn9300LicenseValidity_Type()
)
tn9300LicenseValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300LicenseValidity.setStatus("current")
_Tn9300SiteObjs_ObjectIdentity = ObjectIdentity
tn9300SiteObjs = _Tn9300SiteObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2)
)
_Tn9300SiteTable_Object = MibTable
tn9300SiteTable = _Tn9300SiteTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tn9300SiteTable.setStatus("current")
_Tn9300SiteEntry_Object = MibTableRow
tn9300SiteEntry = _Tn9300SiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1)
)
tn9300SiteEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300SiteNumber"),
)
if mibBuilder.loadTexts:
    tn9300SiteEntry.setStatus("current")


class _Tn9300SiteNumber_Type(Integer32):
    """Custom type tn9300SiteNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_Tn9300SiteNumber_Type.__name__ = "Integer32"
_Tn9300SiteNumber_Object = MibTableColumn
tn9300SiteNumber = _Tn9300SiteNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 1),
    _Tn9300SiteNumber_Type()
)
tn9300SiteNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300SiteNumber.setStatus("current")
_Tn9300SiteName_Type = DisplayString
_Tn9300SiteName_Object = MibTableColumn
tn9300SiteName = _Tn9300SiteName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 2),
    _Tn9300SiteName_Type()
)
tn9300SiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteName.setStatus("current")
_Tn9300SiteSyscode_Type = DisplayString
_Tn9300SiteSyscode_Object = MibTableColumn
tn9300SiteSyscode = _Tn9300SiteSyscode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 3),
    _Tn9300SiteSyscode_Type()
)
tn9300SiteSyscode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteSyscode.setStatus("current")
_Tn9300SiteEnabled_Type = TruthValue
_Tn9300SiteEnabled_Object = MibTableColumn
tn9300SiteEnabled = _Tn9300SiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 4),
    _Tn9300SiteEnabled_Type()
)
tn9300SiteEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteEnabled.setStatus("current")
_Tn9300SiteOk_Type = TruthValue
_Tn9300SiteOk_Object = MibTableColumn
tn9300SiteOk = _Tn9300SiteOk_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 5),
    _Tn9300SiteOk_Type()
)
tn9300SiteOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteOk.setStatus("current")
_Tn9300SiteAutoQueueDepth_Type = TruthValue
_Tn9300SiteAutoQueueDepth_Object = MibTableColumn
tn9300SiteAutoQueueDepth = _Tn9300SiteAutoQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 6),
    _Tn9300SiteAutoQueueDepth_Type()
)
tn9300SiteAutoQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteAutoQueueDepth.setStatus("current")
_Tn9300SiteQueueDepth_Type = Integer32
_Tn9300SiteQueueDepth_Object = MibTableColumn
tn9300SiteQueueDepth = _Tn9300SiteQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 7),
    _Tn9300SiteQueueDepth_Type()
)
tn9300SiteQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteQueueDepth.setStatus("current")
_Tn9300SiteZone_Type = Integer32
_Tn9300SiteZone_Object = MibTableColumn
tn9300SiteZone = _Tn9300SiteZone_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 8),
    _Tn9300SiteZone_Type()
)
tn9300SiteZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteZone.setStatus("current")
_Tn9300SiteExtraWaitSlots_Type = Integer32
_Tn9300SiteExtraWaitSlots_Object = MibTableColumn
tn9300SiteExtraWaitSlots = _Tn9300SiteExtraWaitSlots_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 9),
    _Tn9300SiteExtraWaitSlots_Type()
)
tn9300SiteExtraWaitSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteExtraWaitSlots.setStatus("current")
_Tn9300SiteCCReassignTimeout_Type = Integer32
_Tn9300SiteCCReassignTimeout_Object = MibTableColumn
tn9300SiteCCReassignTimeout = _Tn9300SiteCCReassignTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 10),
    _Tn9300SiteCCReassignTimeout_Type()
)
tn9300SiteCCReassignTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteCCReassignTimeout.setStatus("current")
_Tn9300SiteTCRotation_Type = TruthValue
_Tn9300SiteTCRotation_Object = MibTableColumn
tn9300SiteTCRotation = _Tn9300SiteTCRotation_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 11),
    _Tn9300SiteTCRotation_Type()
)
tn9300SiteTCRotation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteTCRotation.setStatus("current")
_Tn9300SiteRxActivityTimeout_Type = Integer32
_Tn9300SiteRxActivityTimeout_Object = MibTableColumn
tn9300SiteRxActivityTimeout = _Tn9300SiteRxActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 12),
    _Tn9300SiteRxActivityTimeout_Type()
)
tn9300SiteRxActivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteRxActivityTimeout.setStatus("current")
_Tn9300SiteRxInactiveTimeout_Type = Integer32
_Tn9300SiteRxInactiveTimeout_Object = MibTableColumn
tn9300SiteRxInactiveTimeout = _Tn9300SiteRxInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 13),
    _Tn9300SiteRxInactiveTimeout_Type()
)
tn9300SiteRxInactiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteRxInactiveTimeout.setStatus("current")
_Tn9300SiteFramelength_Type = Integer32
_Tn9300SiteFramelength_Object = MibTableColumn
tn9300SiteFramelength = _Tn9300SiteFramelength_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 14),
    _Tn9300SiteFramelength_Type()
)
tn9300SiteFramelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteFramelength.setStatus("current")
_Tn9300SiteMinFramelength_Type = Integer32
_Tn9300SiteMinFramelength_Object = MibTableColumn
tn9300SiteMinFramelength = _Tn9300SiteMinFramelength_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 15),
    _Tn9300SiteMinFramelength_Type()
)
tn9300SiteMinFramelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteMinFramelength.setStatus("current")
_Tn9300SiteMaxFramelength_Type = Integer32
_Tn9300SiteMaxFramelength_Object = MibTableColumn
tn9300SiteMaxFramelength = _Tn9300SiteMaxFramelength_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 16),
    _Tn9300SiteMaxFramelength_Type()
)
tn9300SiteMaxFramelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteMaxFramelength.setStatus("current")
_Tn9300SiteDualCC_Type = Integer32
_Tn9300SiteDualCC_Object = MibTableColumn
tn9300SiteDualCC = _Tn9300SiteDualCC_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 17),
    _Tn9300SiteDualCC_Type()
)
tn9300SiteDualCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteDualCC.setStatus("current")
_Tn9300SiteOpenMuteTimeout_Type = Integer32
_Tn9300SiteOpenMuteTimeout_Object = MibTableColumn
tn9300SiteOpenMuteTimeout = _Tn9300SiteOpenMuteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 18),
    _Tn9300SiteOpenMuteTimeout_Type()
)
tn9300SiteOpenMuteTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteOpenMuteTimeout.setStatus("current")
_Tn9300SiteManAdjSiteRF_Type = Integer32
_Tn9300SiteManAdjSiteRF_Object = MibTableColumn
tn9300SiteManAdjSiteRF = _Tn9300SiteManAdjSiteRF_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 19),
    _Tn9300SiteManAdjSiteRF_Type()
)
tn9300SiteManAdjSiteRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteManAdjSiteRF.setStatus("current")
_Tn9300SiteManAdjSiteSyscode_Type = DisplayString
_Tn9300SiteManAdjSiteSyscode_Object = MibTableColumn
tn9300SiteManAdjSiteSyscode = _Tn9300SiteManAdjSiteSyscode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 20),
    _Tn9300SiteManAdjSiteSyscode_Type()
)
tn9300SiteManAdjSiteSyscode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteManAdjSiteSyscode.setStatus("current")
_Tn9300SiteNChannels_Type = Gauge32
_Tn9300SiteNChannels_Object = MibTableColumn
tn9300SiteNChannels = _Tn9300SiteNChannels_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 21),
    _Tn9300SiteNChannels_Type()
)
tn9300SiteNChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNChannels.setStatus("current")
_Tn9300SiteNControlChannels_Type = Gauge32
_Tn9300SiteNControlChannels_Object = MibTableColumn
tn9300SiteNControlChannels = _Tn9300SiteNControlChannels_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 22),
    _Tn9300SiteNControlChannels_Type()
)
tn9300SiteNControlChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNControlChannels.setStatus("current")
_Tn9300SiteNTrafficChannels_Type = Gauge32
_Tn9300SiteNTrafficChannels_Object = MibTableColumn
tn9300SiteNTrafficChannels = _Tn9300SiteNTrafficChannels_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 23),
    _Tn9300SiteNTrafficChannels_Type()
)
tn9300SiteNTrafficChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNTrafficChannels.setStatus("current")
_Tn9300SiteNIdleChannels_Type = Gauge32
_Tn9300SiteNIdleChannels_Object = MibTableColumn
tn9300SiteNIdleChannels = _Tn9300SiteNIdleChannels_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 24),
    _Tn9300SiteNIdleChannels_Type()
)
tn9300SiteNIdleChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNIdleChannels.setStatus("current")
_Tn9300SiteNDisabledChannels_Type = Gauge32
_Tn9300SiteNDisabledChannels_Object = MibTableColumn
tn9300SiteNDisabledChannels = _Tn9300SiteNDisabledChannels_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 25),
    _Tn9300SiteNDisabledChannels_Type()
)
tn9300SiteNDisabledChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNDisabledChannels.setStatus("current")
_Tn9300SiteNFailedChannels_Type = Gauge32
_Tn9300SiteNFailedChannels_Object = MibTableColumn
tn9300SiteNFailedChannels = _Tn9300SiteNFailedChannels_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 26),
    _Tn9300SiteNFailedChannels_Type()
)
tn9300SiteNFailedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNFailedChannels.setStatus("current")
_Tn9300SiteNOnAirCalls_Type = Gauge32
_Tn9300SiteNOnAirCalls_Object = MibTableColumn
tn9300SiteNOnAirCalls = _Tn9300SiteNOnAirCalls_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 27),
    _Tn9300SiteNOnAirCalls_Type()
)
tn9300SiteNOnAirCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNOnAirCalls.setStatus("current")
_Tn9300SiteNRingingCalls_Type = Gauge32
_Tn9300SiteNRingingCalls_Object = MibTableColumn
tn9300SiteNRingingCalls = _Tn9300SiteNRingingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 28),
    _Tn9300SiteNRingingCalls_Type()
)
tn9300SiteNRingingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNRingingCalls.setStatus("current")
_Tn9300SiteNQueuedCalls_Type = Gauge32
_Tn9300SiteNQueuedCalls_Object = MibTableColumn
tn9300SiteNQueuedCalls = _Tn9300SiteNQueuedCalls_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 29),
    _Tn9300SiteNQueuedCalls_Type()
)
tn9300SiteNQueuedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNQueuedCalls.setStatus("current")
_Tn9300SiteTotalCalls_Type = Counter32
_Tn9300SiteTotalCalls_Object = MibTableColumn
tn9300SiteTotalCalls = _Tn9300SiteTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 30),
    _Tn9300SiteTotalCalls_Type()
)
tn9300SiteTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteTotalCalls.setStatus("current")
_Tn9300SiteTotalChannelCalls_Type = Counter32
_Tn9300SiteTotalChannelCalls_Object = MibTableColumn
tn9300SiteTotalChannelCalls = _Tn9300SiteTotalChannelCalls_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 31),
    _Tn9300SiteTotalChannelCalls_Type()
)
tn9300SiteTotalChannelCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteTotalChannelCalls.setStatus("current")
_Tn9300SiteTotalQueueTime_Type = Counter32
_Tn9300SiteTotalQueueTime_Object = MibTableColumn
tn9300SiteTotalQueueTime = _Tn9300SiteTotalQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 32),
    _Tn9300SiteTotalQueueTime_Type()
)
tn9300SiteTotalQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteTotalQueueTime.setStatus("current")
_Tn9300SiteChannelTimeFailed_Type = Counter32
_Tn9300SiteChannelTimeFailed_Object = MibTableColumn
tn9300SiteChannelTimeFailed = _Tn9300SiteChannelTimeFailed_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 33),
    _Tn9300SiteChannelTimeFailed_Type()
)
tn9300SiteChannelTimeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteChannelTimeFailed.setStatus("current")
_Tn9300SiteChannelTimeTraffic_Type = Counter32
_Tn9300SiteChannelTimeTraffic_Object = MibTableColumn
tn9300SiteChannelTimeTraffic = _Tn9300SiteChannelTimeTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 34),
    _Tn9300SiteChannelTimeTraffic_Type()
)
tn9300SiteChannelTimeTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteChannelTimeTraffic.setStatus("current")
_Tn9300SiteChannelTimeControl_Type = Counter32
_Tn9300SiteChannelTimeControl_Object = MibTableColumn
tn9300SiteChannelTimeControl = _Tn9300SiteChannelTimeControl_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 35),
    _Tn9300SiteChannelTimeControl_Type()
)
tn9300SiteChannelTimeControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteChannelTimeControl.setStatus("current")
_Tn9300SiteChannelTimeIdle_Type = Counter32
_Tn9300SiteChannelTimeIdle_Object = MibTableColumn
tn9300SiteChannelTimeIdle = _Tn9300SiteChannelTimeIdle_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 36),
    _Tn9300SiteChannelTimeIdle_Type()
)
tn9300SiteChannelTimeIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteChannelTimeIdle.setStatus("current")
_Tn9300SiteCallsQueuedUnder5_Type = Counter32
_Tn9300SiteCallsQueuedUnder5_Object = MibTableColumn
tn9300SiteCallsQueuedUnder5 = _Tn9300SiteCallsQueuedUnder5_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 37),
    _Tn9300SiteCallsQueuedUnder5_Type()
)
tn9300SiteCallsQueuedUnder5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteCallsQueuedUnder5.setStatus("current")
_Tn9300SiteCallsQueued5To10_Type = Counter32
_Tn9300SiteCallsQueued5To10_Object = MibTableColumn
tn9300SiteCallsQueued5To10 = _Tn9300SiteCallsQueued5To10_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 38),
    _Tn9300SiteCallsQueued5To10_Type()
)
tn9300SiteCallsQueued5To10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteCallsQueued5To10.setStatus("current")
_Tn9300SiteCallsQueued10To20_Type = Counter32
_Tn9300SiteCallsQueued10To20_Object = MibTableColumn
tn9300SiteCallsQueued10To20 = _Tn9300SiteCallsQueued10To20_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 39),
    _Tn9300SiteCallsQueued10To20_Type()
)
tn9300SiteCallsQueued10To20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteCallsQueued10To20.setStatus("current")
_Tn9300SiteCallsQueuedOver20_Type = Counter32
_Tn9300SiteCallsQueuedOver20_Object = MibTableColumn
tn9300SiteCallsQueuedOver20 = _Tn9300SiteCallsQueuedOver20_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 40),
    _Tn9300SiteCallsQueuedOver20_Type()
)
tn9300SiteCallsQueuedOver20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteCallsQueuedOver20.setStatus("current")
_Tn9300SiteAlias_Type = DisplayString
_Tn9300SiteAlias_Object = MibTableColumn
tn9300SiteAlias = _Tn9300SiteAlias_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 41),
    _Tn9300SiteAlias_Type()
)
tn9300SiteAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteAlias.setStatus("current")
_Tn9300SiteControlChCountOk_Type = TruthValue
_Tn9300SiteControlChCountOk_Object = MibTableColumn
tn9300SiteControlChCountOk = _Tn9300SiteControlChCountOk_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 42),
    _Tn9300SiteControlChCountOk_Type()
)
tn9300SiteControlChCountOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteControlChCountOk.setStatus("current")
_Tn9300SiteNAlternateChannels_Type = Gauge32
_Tn9300SiteNAlternateChannels_Object = MibTableColumn
tn9300SiteNAlternateChannels = _Tn9300SiteNAlternateChannels_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 43),
    _Tn9300SiteNAlternateChannels_Type()
)
tn9300SiteNAlternateChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteNAlternateChannels.setStatus("current")
_Tn9300SiteChannelTimeAlternate_Type = Counter32
_Tn9300SiteChannelTimeAlternate_Object = MibTableColumn
tn9300SiteChannelTimeAlternate = _Tn9300SiteChannelTimeAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 1, 1, 44),
    _Tn9300SiteChannelTimeAlternate_Type()
)
tn9300SiteChannelTimeAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SiteChannelTimeAlternate.setStatus("current")
_Tn9300ChannelTable_Object = MibTable
tn9300ChannelTable = _Tn9300ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tn9300ChannelTable.setStatus("current")
_Tn9300ChannelEntry_Object = MibTableRow
tn9300ChannelEntry = _Tn9300ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1)
)
tn9300ChannelEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300SiteNumber"),
    (0, "TAIT-TN9300-MIB", "tn9300ChannelBaseStationNumber"),
    (0, "TAIT-TN9300-MIB", "tn9300ChannelNumber"),
)
if mibBuilder.loadTexts:
    tn9300ChannelEntry.setStatus("current")


class _Tn9300ChannelNumber_Type(Integer32):
    """Custom type tn9300ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Tn9300ChannelNumber_Type.__name__ = "Integer32"
_Tn9300ChannelNumber_Object = MibTableColumn
tn9300ChannelNumber = _Tn9300ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 1),
    _Tn9300ChannelNumber_Type()
)
tn9300ChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300ChannelNumber.setStatus("current")
_Tn9300ChannelIpAddressType_Type = InetAddressType
_Tn9300ChannelIpAddressType_Object = MibTableColumn
tn9300ChannelIpAddressType = _Tn9300ChannelIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 2),
    _Tn9300ChannelIpAddressType_Type()
)
tn9300ChannelIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelIpAddressType.setStatus("current")


class _Tn9300ChannelIpAddress_Type(InetAddress):
    """Custom type tn9300ChannelIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300ChannelIpAddress_Type.__name__ = "InetAddress"
_Tn9300ChannelIpAddress_Object = MibTableColumn
tn9300ChannelIpAddress = _Tn9300ChannelIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 3),
    _Tn9300ChannelIpAddress_Type()
)
tn9300ChannelIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelIpAddress.setStatus("current")
_Tn9300ChannelPort_Type = Integer32
_Tn9300ChannelPort_Object = MibTableColumn
tn9300ChannelPort = _Tn9300ChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 4),
    _Tn9300ChannelPort_Type()
)
tn9300ChannelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelPort.setStatus("current")
_Tn9300ChannelRf_Type = Integer32
_Tn9300ChannelRf_Object = MibTableColumn
tn9300ChannelRf = _Tn9300ChannelRf_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 5),
    _Tn9300ChannelRf_Type()
)
tn9300ChannelRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelRf.setStatus("current")
_Tn9300ChannelEnabled_Type = TruthValue
_Tn9300ChannelEnabled_Object = MibTableColumn
tn9300ChannelEnabled = _Tn9300ChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 6),
    _Tn9300ChannelEnabled_Type()
)
tn9300ChannelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelEnabled.setStatus("current")
_Tn9300ChannelControlAllowed_Type = TruthValue
_Tn9300ChannelControlAllowed_Object = MibTableColumn
tn9300ChannelControlAllowed = _Tn9300ChannelControlAllowed_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 7),
    _Tn9300ChannelControlAllowed_Type()
)
tn9300ChannelControlAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelControlAllowed.setStatus("current")
_Tn9300ChannelTrafficAllowed_Type = TruthValue
_Tn9300ChannelTrafficAllowed_Object = MibTableColumn
tn9300ChannelTrafficAllowed = _Tn9300ChannelTrafficAllowed_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 8),
    _Tn9300ChannelTrafficAllowed_Type()
)
tn9300ChannelTrafficAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelTrafficAllowed.setStatus("current")
_Tn9300ChannelInhibitIfJammed_Type = TruthValue
_Tn9300ChannelInhibitIfJammed_Object = MibTableColumn
tn9300ChannelInhibitIfJammed = _Tn9300ChannelInhibitIfJammed_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 9),
    _Tn9300ChannelInhibitIfJammed_Type()
)
tn9300ChannelInhibitIfJammed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelInhibitIfJammed.setStatus("current")
_Tn9300ChannelState_Type = ChannelState
_Tn9300ChannelState_Object = MibTableColumn
tn9300ChannelState = _Tn9300ChannelState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 10),
    _Tn9300ChannelState_Type()
)
tn9300ChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelState.setStatus("current")
_Tn9300ChannelJammed_Type = TruthValue
_Tn9300ChannelJammed_Object = MibTableColumn
tn9300ChannelJammed = _Tn9300ChannelJammed_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 11),
    _Tn9300ChannelJammed_Type()
)
tn9300ChannelJammed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelJammed.setStatus("current")
_Tn9300ChannelMinorAlarm_Type = TruthValue
_Tn9300ChannelMinorAlarm_Object = MibTableColumn
tn9300ChannelMinorAlarm = _Tn9300ChannelMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 12),
    _Tn9300ChannelMinorAlarm_Type()
)
tn9300ChannelMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelMinorAlarm.setStatus("current")
_Tn9300ChannelMajorAlarm_Type = TruthValue
_Tn9300ChannelMajorAlarm_Object = MibTableColumn
tn9300ChannelMajorAlarm = _Tn9300ChannelMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 13),
    _Tn9300ChannelMajorAlarm_Type()
)
tn9300ChannelMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelMajorAlarm.setStatus("current")
_Tn9300ChannelAParty_Type = DisplayString
_Tn9300ChannelAParty_Object = MibTableColumn
tn9300ChannelAParty = _Tn9300ChannelAParty_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 14),
    _Tn9300ChannelAParty_Type()
)
tn9300ChannelAParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelAParty.setStatus("current")
_Tn9300ChannelBParty_Type = DisplayString
_Tn9300ChannelBParty_Object = MibTableColumn
tn9300ChannelBParty = _Tn9300ChannelBParty_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 15),
    _Tn9300ChannelBParty_Type()
)
tn9300ChannelBParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelBParty.setStatus("current")
_Tn9300ChannelBspRxPackets_Type = Counter32
_Tn9300ChannelBspRxPackets_Object = MibTableColumn
tn9300ChannelBspRxPackets = _Tn9300ChannelBspRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 16),
    _Tn9300ChannelBspRxPackets_Type()
)
tn9300ChannelBspRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelBspRxPackets.setStatus("current")
_Tn9300ChannelBspTxPackets_Type = Counter32
_Tn9300ChannelBspTxPackets_Object = MibTableColumn
tn9300ChannelBspTxPackets = _Tn9300ChannelBspTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 17),
    _Tn9300ChannelBspTxPackets_Type()
)
tn9300ChannelBspTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelBspTxPackets.setStatus("current")
_Tn9300ChannelBspLostPackets_Type = Counter32
_Tn9300ChannelBspLostPackets_Object = MibTableColumn
tn9300ChannelBspLostPackets = _Tn9300ChannelBspLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 18),
    _Tn9300ChannelBspLostPackets_Type()
)
tn9300ChannelBspLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelBspLostPackets.setStatus("current")
_Tn9300ChannelRtpRxPackets_Type = Counter32
_Tn9300ChannelRtpRxPackets_Object = MibTableColumn
tn9300ChannelRtpRxPackets = _Tn9300ChannelRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 19),
    _Tn9300ChannelRtpRxPackets_Type()
)
tn9300ChannelRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelRtpRxPackets.setStatus("current")
_Tn9300ChannelRtpTxPackets_Type = Counter32
_Tn9300ChannelRtpTxPackets_Object = MibTableColumn
tn9300ChannelRtpTxPackets = _Tn9300ChannelRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 20),
    _Tn9300ChannelRtpTxPackets_Type()
)
tn9300ChannelRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelRtpTxPackets.setStatus("current")
_Tn9300ChannelRtpLostPackets_Type = Counter32
_Tn9300ChannelRtpLostPackets_Object = MibTableColumn
tn9300ChannelRtpLostPackets = _Tn9300ChannelRtpLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 21),
    _Tn9300ChannelRtpLostPackets_Type()
)
tn9300ChannelRtpLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelRtpLostPackets.setStatus("current")
_Tn9300ChannelRtpRtt_Type = Gauge32
_Tn9300ChannelRtpRtt_Object = MibTableColumn
tn9300ChannelRtpRtt = _Tn9300ChannelRtpRtt_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 22),
    _Tn9300ChannelRtpRtt_Type()
)
tn9300ChannelRtpRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelRtpRtt.setStatus("current")
_Tn9300ChannelRtpRttJitter_Type = Gauge32
_Tn9300ChannelRtpRttJitter_Object = MibTableColumn
tn9300ChannelRtpRttJitter = _Tn9300ChannelRtpRttJitter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 23),
    _Tn9300ChannelRtpRttJitter_Type()
)
tn9300ChannelRtpRttJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelRtpRttJitter.setStatus("current")
_Tn9300ChannelTimeFailed_Type = Counter32
_Tn9300ChannelTimeFailed_Object = MibTableColumn
tn9300ChannelTimeFailed = _Tn9300ChannelTimeFailed_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 24),
    _Tn9300ChannelTimeFailed_Type()
)
tn9300ChannelTimeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelTimeFailed.setStatus("current")
_Tn9300ChannelTimeTraffic_Type = Counter32
_Tn9300ChannelTimeTraffic_Object = MibTableColumn
tn9300ChannelTimeTraffic = _Tn9300ChannelTimeTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 25),
    _Tn9300ChannelTimeTraffic_Type()
)
tn9300ChannelTimeTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelTimeTraffic.setStatus("current")
_Tn9300ChannelTimeControl_Type = Counter32
_Tn9300ChannelTimeControl_Object = MibTableColumn
tn9300ChannelTimeControl = _Tn9300ChannelTimeControl_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 26),
    _Tn9300ChannelTimeControl_Type()
)
tn9300ChannelTimeControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelTimeControl.setStatus("current")
_Tn9300ChannelTimeIdle_Type = Counter32
_Tn9300ChannelTimeIdle_Object = MibTableColumn
tn9300ChannelTimeIdle = _Tn9300ChannelTimeIdle_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 27),
    _Tn9300ChannelTimeIdle_Type()
)
tn9300ChannelTimeIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelTimeIdle.setStatus("current")
_Tn9300ChannelAlternateAllowed_Type = TruthValue
_Tn9300ChannelAlternateAllowed_Object = MibTableColumn
tn9300ChannelAlternateAllowed = _Tn9300ChannelAlternateAllowed_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 28),
    _Tn9300ChannelAlternateAllowed_Type()
)
tn9300ChannelAlternateAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelAlternateAllowed.setStatus("current")
_Tn9300ChannelTimeAlternate_Type = Counter32
_Tn9300ChannelTimeAlternate_Object = MibTableColumn
tn9300ChannelTimeAlternate = _Tn9300ChannelTimeAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 29),
    _Tn9300ChannelTimeAlternate_Type()
)
tn9300ChannelTimeAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300ChannelTimeAlternate.setStatus("current")


class _Tn9300ChannelBaseStationNumber_Type(Integer32):
    """Custom type tn9300ChannelBaseStationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Tn9300ChannelBaseStationNumber_Type.__name__ = "Integer32"
_Tn9300ChannelBaseStationNumber_Object = MibTableColumn
tn9300ChannelBaseStationNumber = _Tn9300ChannelBaseStationNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 2, 1, 99),
    _Tn9300ChannelBaseStationNumber_Type()
)
tn9300ChannelBaseStationNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300ChannelBaseStationNumber.setStatus("current")
_Tn9300AdjacentSiteTable_Object = MibTable
tn9300AdjacentSiteTable = _Tn9300AdjacentSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tn9300AdjacentSiteTable.setStatus("current")
_Tn9300AdjacentSiteEntry_Object = MibTableRow
tn9300AdjacentSiteEntry = _Tn9300AdjacentSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5, 1)
)
tn9300AdjacentSiteEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300SiteNumber"),
    (0, "TAIT-TN9300-MIB", "tn9300AdjSiteSendOrder"),
)
if mibBuilder.loadTexts:
    tn9300AdjacentSiteEntry.setStatus("current")


class _Tn9300AdjSiteSendOrder_Type(Integer32):
    """Custom type tn9300AdjSiteSendOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Tn9300AdjSiteSendOrder_Type.__name__ = "Integer32"
_Tn9300AdjSiteSendOrder_Object = MibTableColumn
tn9300AdjSiteSendOrder = _Tn9300AdjSiteSendOrder_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5, 1, 1),
    _Tn9300AdjSiteSendOrder_Type()
)
tn9300AdjSiteSendOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300AdjSiteSendOrder.setStatus("current")
_Tn9300AdjSiteAlias_Type = DisplayString
_Tn9300AdjSiteAlias_Object = MibTableColumn
tn9300AdjSiteAlias = _Tn9300AdjSiteAlias_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5, 1, 2),
    _Tn9300AdjSiteAlias_Type()
)
tn9300AdjSiteAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300AdjSiteAlias.setStatus("current")
_Tn9300AdjSiteSyscode1_Type = DisplayString
_Tn9300AdjSiteSyscode1_Object = MibTableColumn
tn9300AdjSiteSyscode1 = _Tn9300AdjSiteSyscode1_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5, 1, 3),
    _Tn9300AdjSiteSyscode1_Type()
)
tn9300AdjSiteSyscode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300AdjSiteSyscode1.setStatus("current")
_Tn9300AdjSiteRF1_Type = Integer32
_Tn9300AdjSiteRF1_Object = MibTableColumn
tn9300AdjSiteRF1 = _Tn9300AdjSiteRF1_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5, 1, 4),
    _Tn9300AdjSiteRF1_Type()
)
tn9300AdjSiteRF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300AdjSiteRF1.setStatus("current")
_Tn9300AdjSiteSyscode2_Type = DisplayString
_Tn9300AdjSiteSyscode2_Object = MibTableColumn
tn9300AdjSiteSyscode2 = _Tn9300AdjSiteSyscode2_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5, 1, 5),
    _Tn9300AdjSiteSyscode2_Type()
)
tn9300AdjSiteSyscode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300AdjSiteSyscode2.setStatus("current")
_Tn9300AdjSiteRF2_Type = Integer32
_Tn9300AdjSiteRF2_Object = MibTableColumn
tn9300AdjSiteRF2 = _Tn9300AdjSiteRF2_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 2, 5, 1, 6),
    _Tn9300AdjSiteRF2_Type()
)
tn9300AdjSiteRF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300AdjSiteRF2.setStatus("current")
_Tn9300SipLineObjs_ObjectIdentity = ObjectIdentity
tn9300SipLineObjs = _Tn9300SipLineObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3)
)
_Tn9300SipLineTable_Object = MibTable
tn9300SipLineTable = _Tn9300SipLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tn9300SipLineTable.setStatus("current")
_Tn9300SipLineEntry_Object = MibTableRow
tn9300SipLineEntry = _Tn9300SipLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1)
)
tn9300SipLineEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300SipLineNumber"),
)
if mibBuilder.loadTexts:
    tn9300SipLineEntry.setStatus("current")


class _Tn9300SipLineNumber_Type(Integer32):
    """Custom type tn9300SipLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tn9300SipLineNumber_Type.__name__ = "Integer32"
_Tn9300SipLineNumber_Object = MibTableColumn
tn9300SipLineNumber = _Tn9300SipLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 1),
    _Tn9300SipLineNumber_Type()
)
tn9300SipLineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300SipLineNumber.setStatus("current")
_Tn9300SipLineName_Type = DisplayString
_Tn9300SipLineName_Object = MibTableColumn
tn9300SipLineName = _Tn9300SipLineName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 2),
    _Tn9300SipLineName_Type()
)
tn9300SipLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineName.setStatus("current")
_Tn9300SipLineRegistrationType_Type = SipLineRegistrationType
_Tn9300SipLineRegistrationType_Object = MibTableColumn
tn9300SipLineRegistrationType = _Tn9300SipLineRegistrationType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 3),
    _Tn9300SipLineRegistrationType_Type()
)
tn9300SipLineRegistrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineRegistrationType.setStatus("current")
_Tn9300SipLineUserName_Type = DisplayString
_Tn9300SipLineUserName_Object = MibTableColumn
tn9300SipLineUserName = _Tn9300SipLineUserName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 4),
    _Tn9300SipLineUserName_Type()
)
tn9300SipLineUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineUserName.setStatus("current")
_Tn9300SipLineEnabled_Type = TruthValue
_Tn9300SipLineEnabled_Object = MibTableColumn
tn9300SipLineEnabled = _Tn9300SipLineEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 5),
    _Tn9300SipLineEnabled_Type()
)
tn9300SipLineEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineEnabled.setStatus("current")
_Tn9300SipLineSpchVotePri_Type = SipCallSpeechVotingPriority
_Tn9300SipLineSpchVotePri_Object = MibTableColumn
tn9300SipLineSpchVotePri = _Tn9300SipLineSpchVotePri_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 6),
    _Tn9300SipLineSpchVotePri_Type()
)
tn9300SipLineSpchVotePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineSpchVotePri.setStatus("current")
_Tn9300SipLineAisMultipartContents_Type = TruthValue
_Tn9300SipLineAisMultipartContents_Object = MibTableColumn
tn9300SipLineAisMultipartContents = _Tn9300SipLineAisMultipartContents_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 7),
    _Tn9300SipLineAisMultipartContents_Type()
)
tn9300SipLineAisMultipartContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineAisMultipartContents.setStatus("current")
_Tn9300SipLineAisMonitor_Type = TruthValue
_Tn9300SipLineAisMonitor_Object = MibTableColumn
tn9300SipLineAisMonitor = _Tn9300SipLineAisMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 8),
    _Tn9300SipLineAisMonitor_Type()
)
tn9300SipLineAisMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineAisMonitor.setStatus("current")
_Tn9300SipLineSipGroup_Type = DisplayString
_Tn9300SipLineSipGroup_Object = MibTableColumn
tn9300SipLineSipGroup = _Tn9300SipLineSipGroup_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 9),
    _Tn9300SipLineSipGroup_Type()
)
tn9300SipLineSipGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineSipGroup.setStatus("current")
_Tn9300SipLineInphoneTable_Type = DisplayString
_Tn9300SipLineInphoneTable_Object = MibTableColumn
tn9300SipLineInphoneTable = _Tn9300SipLineInphoneTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 10),
    _Tn9300SipLineInphoneTable_Type()
)
tn9300SipLineInphoneTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineInphoneTable.setStatus("current")
_Tn9300SipLineIncomingType_Type = SipLineIncomingType
_Tn9300SipLineIncomingType_Object = MibTableColumn
tn9300SipLineIncomingType = _Tn9300SipLineIncomingType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 11),
    _Tn9300SipLineIncomingType_Type()
)
tn9300SipLineIncomingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineIncomingType.setStatus("current")
_Tn9300SipLineProxyAddressType_Type = InetAddressType
_Tn9300SipLineProxyAddressType_Object = MibTableColumn
tn9300SipLineProxyAddressType = _Tn9300SipLineProxyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 12),
    _Tn9300SipLineProxyAddressType_Type()
)
tn9300SipLineProxyAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineProxyAddressType.setStatus("current")


class _Tn9300SipLineProxyAddress_Type(InetAddress):
    """Custom type tn9300SipLineProxyAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300SipLineProxyAddress_Type.__name__ = "InetAddress"
_Tn9300SipLineProxyAddress_Object = MibTableColumn
tn9300SipLineProxyAddress = _Tn9300SipLineProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 13),
    _Tn9300SipLineProxyAddress_Type()
)
tn9300SipLineProxyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineProxyAddress.setStatus("current")
_Tn9300SipLineIpAddressType_Type = InetAddressType
_Tn9300SipLineIpAddressType_Object = MibTableColumn
tn9300SipLineIpAddressType = _Tn9300SipLineIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 14),
    _Tn9300SipLineIpAddressType_Type()
)
tn9300SipLineIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineIpAddressType.setStatus("current")


class _Tn9300SipLineIpAddress_Type(InetAddress):
    """Custom type tn9300SipLineIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300SipLineIpAddress_Type.__name__ = "InetAddress"
_Tn9300SipLineIpAddress_Object = MibTableColumn
tn9300SipLineIpAddress = _Tn9300SipLineIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 15),
    _Tn9300SipLineIpAddress_Type()
)
tn9300SipLineIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineIpAddress.setStatus("current")
_Tn9300SipLineState_Type = SipLineState
_Tn9300SipLineState_Object = MibTableColumn
tn9300SipLineState = _Tn9300SipLineState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 16),
    _Tn9300SipLineState_Type()
)
tn9300SipLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineState.setStatus("current")
_Tn9300SipLineUptime_Type = Counter32
_Tn9300SipLineUptime_Object = MibTableColumn
tn9300SipLineUptime = _Tn9300SipLineUptime_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 17),
    _Tn9300SipLineUptime_Type()
)
tn9300SipLineUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineUptime.setStatus("current")
_Tn9300SipLineConnects_Type = Counter32
_Tn9300SipLineConnects_Object = MibTableColumn
tn9300SipLineConnects = _Tn9300SipLineConnects_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 18),
    _Tn9300SipLineConnects_Type()
)
tn9300SipLineConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineConnects.setStatus("current")
_Tn9300SipLineCalls_Type = Counter32
_Tn9300SipLineCalls_Object = MibTableColumn
tn9300SipLineCalls = _Tn9300SipLineCalls_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 3, 1, 1, 19),
    _Tn9300SipLineCalls_Type()
)
tn9300SipLineCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300SipLineCalls.setStatus("current")
_Tn9300DipLineObjs_ObjectIdentity = ObjectIdentity
tn9300DipLineObjs = _Tn9300DipLineObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4)
)
_Tn9300DipLineTable_Object = MibTable
tn9300DipLineTable = _Tn9300DipLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tn9300DipLineTable.setStatus("current")
_Tn9300DipLineEntry_Object = MibTableRow
tn9300DipLineEntry = _Tn9300DipLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1)
)
tn9300DipLineEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300DipLineNumber"),
)
if mibBuilder.loadTexts:
    tn9300DipLineEntry.setStatus("current")


class _Tn9300DipLineNumber_Type(Integer32):
    """Custom type tn9300DipLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Tn9300DipLineNumber_Type.__name__ = "Integer32"
_Tn9300DipLineNumber_Object = MibTableColumn
tn9300DipLineNumber = _Tn9300DipLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 1),
    _Tn9300DipLineNumber_Type()
)
tn9300DipLineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300DipLineNumber.setStatus("current")
_Tn9300DipLineName_Type = DisplayString
_Tn9300DipLineName_Object = MibTableColumn
tn9300DipLineName = _Tn9300DipLineName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 2),
    _Tn9300DipLineName_Type()
)
tn9300DipLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineName.setStatus("current")
_Tn9300DipLineNgwIpAddrType_Type = InetAddressType
_Tn9300DipLineNgwIpAddrType_Object = MibTableColumn
tn9300DipLineNgwIpAddrType = _Tn9300DipLineNgwIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 3),
    _Tn9300DipLineNgwIpAddrType_Type()
)
tn9300DipLineNgwIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineNgwIpAddrType.setStatus("current")


class _Tn9300DipLineNgwIpAddr_Type(InetAddress):
    """Custom type tn9300DipLineNgwIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300DipLineNgwIpAddr_Type.__name__ = "InetAddress"
_Tn9300DipLineNgwIpAddr_Object = MibTableColumn
tn9300DipLineNgwIpAddr = _Tn9300DipLineNgwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 4),
    _Tn9300DipLineNgwIpAddr_Type()
)
tn9300DipLineNgwIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineNgwIpAddr.setStatus("current")
_Tn9300DipLineAddress_Type = DisplayString
_Tn9300DipLineAddress_Object = MibTableColumn
tn9300DipLineAddress = _Tn9300DipLineAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 5),
    _Tn9300DipLineAddress_Type()
)
tn9300DipLineAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineAddress.setStatus("current")
_Tn9300DipLinePilotAddress_Type = DisplayString
_Tn9300DipLinePilotAddress_Object = MibTableColumn
tn9300DipLinePilotAddress = _Tn9300DipLinePilotAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 6),
    _Tn9300DipLinePilotAddress_Type()
)
tn9300DipLinePilotAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLinePilotAddress.setStatus("current")
_Tn9300DipLineSpchVotePri_Type = SipCallSpeechVotingPriority
_Tn9300DipLineSpchVotePri_Object = MibTableColumn
tn9300DipLineSpchVotePri = _Tn9300DipLineSpchVotePri_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 7),
    _Tn9300DipLineSpchVotePri_Type()
)
tn9300DipLineSpchVotePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineSpchVotePri.setStatus("current")
_Tn9300DipLineState_Type = DipLineState
_Tn9300DipLineState_Object = MibTableColumn
tn9300DipLineState = _Tn9300DipLineState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 8),
    _Tn9300DipLineState_Type()
)
tn9300DipLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineState.setStatus("current")
_Tn9300DipLineNgwLinkState_Type = NgwLinkState
_Tn9300DipLineNgwLinkState_Object = MibTableColumn
tn9300DipLineNgwLinkState = _Tn9300DipLineNgwLinkState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 9),
    _Tn9300DipLineNgwLinkState_Type()
)
tn9300DipLineNgwLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineNgwLinkState.setStatus("current")
_Tn9300DipLineAParty_Type = DisplayString
_Tn9300DipLineAParty_Object = MibTableColumn
tn9300DipLineAParty = _Tn9300DipLineAParty_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 10),
    _Tn9300DipLineAParty_Type()
)
tn9300DipLineAParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineAParty.setStatus("current")
_Tn9300DipLineBParty_Type = DisplayString
_Tn9300DipLineBParty_Object = MibTableColumn
tn9300DipLineBParty = _Tn9300DipLineBParty_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 11),
    _Tn9300DipLineBParty_Type()
)
tn9300DipLineBParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineBParty.setStatus("current")
_Tn9300DipLnClientIpAddrType_Type = InetAddressType
_Tn9300DipLnClientIpAddrType_Object = MibTableColumn
tn9300DipLnClientIpAddrType = _Tn9300DipLnClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 12),
    _Tn9300DipLnClientIpAddrType_Type()
)
tn9300DipLnClientIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLnClientIpAddrType.setStatus("current")


class _Tn9300DipLnClientIpAddr_Type(InetAddress):
    """Custom type tn9300DipLnClientIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300DipLnClientIpAddr_Type.__name__ = "InetAddress"
_Tn9300DipLnClientIpAddr_Object = MibTableColumn
tn9300DipLnClientIpAddr = _Tn9300DipLnClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 13),
    _Tn9300DipLnClientIpAddr_Type()
)
tn9300DipLnClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLnClientIpAddr.setStatus("current")
_Tn9300DipLineClientUptime_Type = Counter32
_Tn9300DipLineClientUptime_Object = MibTableColumn
tn9300DipLineClientUptime = _Tn9300DipLineClientUptime_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 14),
    _Tn9300DipLineClientUptime_Type()
)
tn9300DipLineClientUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineClientUptime.setStatus("current")
_Tn9300DipLineClientConnects_Type = Counter32
_Tn9300DipLineClientConnects_Object = MibTableColumn
tn9300DipLineClientConnects = _Tn9300DipLineClientConnects_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 15),
    _Tn9300DipLineClientConnects_Type()
)
tn9300DipLineClientConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineClientConnects.setStatus("current")
_Tn9300DipLineNgpRxPackets_Type = Counter32
_Tn9300DipLineNgpRxPackets_Object = MibTableColumn
tn9300DipLineNgpRxPackets = _Tn9300DipLineNgpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 16),
    _Tn9300DipLineNgpRxPackets_Type()
)
tn9300DipLineNgpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineNgpRxPackets.setStatus("current")
_Tn9300DipLineNgpTxPackets_Type = Counter32
_Tn9300DipLineNgpTxPackets_Object = MibTableColumn
tn9300DipLineNgpTxPackets = _Tn9300DipLineNgpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 17),
    _Tn9300DipLineNgpTxPackets_Type()
)
tn9300DipLineNgpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineNgpTxPackets.setStatus("current")
_Tn9300DipLineNgpLostPackets_Type = Counter32
_Tn9300DipLineNgpLostPackets_Object = MibTableColumn
tn9300DipLineNgpLostPackets = _Tn9300DipLineNgpLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 18),
    _Tn9300DipLineNgpLostPackets_Type()
)
tn9300DipLineNgpLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineNgpLostPackets.setStatus("current")
_Tn9300DipLineRtpRxPackets_Type = Counter32
_Tn9300DipLineRtpRxPackets_Object = MibTableColumn
tn9300DipLineRtpRxPackets = _Tn9300DipLineRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 19),
    _Tn9300DipLineRtpRxPackets_Type()
)
tn9300DipLineRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineRtpRxPackets.setStatus("current")
_Tn9300DipLineRtpTxPackets_Type = Counter32
_Tn9300DipLineRtpTxPackets_Object = MibTableColumn
tn9300DipLineRtpTxPackets = _Tn9300DipLineRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 20),
    _Tn9300DipLineRtpTxPackets_Type()
)
tn9300DipLineRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineRtpTxPackets.setStatus("current")
_Tn9300DipLineRtpLostPackets_Type = Counter32
_Tn9300DipLineRtpLostPackets_Object = MibTableColumn
tn9300DipLineRtpLostPackets = _Tn9300DipLineRtpLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 21),
    _Tn9300DipLineRtpLostPackets_Type()
)
tn9300DipLineRtpLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineRtpLostPackets.setStatus("current")
_Tn9300DipLineRtpRtt_Type = Gauge32
_Tn9300DipLineRtpRtt_Object = MibTableColumn
tn9300DipLineRtpRtt = _Tn9300DipLineRtpRtt_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 22),
    _Tn9300DipLineRtpRtt_Type()
)
tn9300DipLineRtpRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineRtpRtt.setStatus("current")
_Tn9300DipLineRtpJitter_Type = Gauge32
_Tn9300DipLineRtpJitter_Object = MibTableColumn
tn9300DipLineRtpJitter = _Tn9300DipLineRtpJitter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 4, 1, 1, 23),
    _Tn9300DipLineRtpJitter_Type()
)
tn9300DipLineRtpJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300DipLineRtpJitter.setStatus("current")
_Tn9300Mpt1327Objs_ObjectIdentity = ObjectIdentity
tn9300Mpt1327Objs = _Tn9300Mpt1327Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5)
)
_Tn9300Mpt1327IpAddressType_Type = InetAddressType
_Tn9300Mpt1327IpAddressType_Object = MibScalar
tn9300Mpt1327IpAddressType = _Tn9300Mpt1327IpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 1),
    _Tn9300Mpt1327IpAddressType_Type()
)
tn9300Mpt1327IpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327IpAddressType.setStatus("current")


class _Tn9300Mpt1327IpAddress_Type(InetAddress):
    """Custom type tn9300Mpt1327IpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300Mpt1327IpAddress_Type.__name__ = "InetAddress"
_Tn9300Mpt1327IpAddress_Object = MibScalar
tn9300Mpt1327IpAddress = _Tn9300Mpt1327IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 2),
    _Tn9300Mpt1327IpAddress_Type()
)
tn9300Mpt1327IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327IpAddress.setStatus("current")
_Tn9300Mpt1327Port_Type = Integer32
_Tn9300Mpt1327Port_Object = MibScalar
tn9300Mpt1327Port = _Tn9300Mpt1327Port_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 3),
    _Tn9300Mpt1327Port_Type()
)
tn9300Mpt1327Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327Port.setStatus("current")
_Tn9300Mpt1327State_Type = Mpt1327LinkState
_Tn9300Mpt1327State_Object = MibScalar
tn9300Mpt1327State = _Tn9300Mpt1327State_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 4),
    _Tn9300Mpt1327State_Type()
)
tn9300Mpt1327State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327State.setStatus("current")
_Tn9300Mpt1327RxBytes_Type = Counter32
_Tn9300Mpt1327RxBytes_Object = MibScalar
tn9300Mpt1327RxBytes = _Tn9300Mpt1327RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 5),
    _Tn9300Mpt1327RxBytes_Type()
)
tn9300Mpt1327RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327RxBytes.setStatus("current")
_Tn9300Mpt1327TxBytes_Type = Counter32
_Tn9300Mpt1327TxBytes_Object = MibScalar
tn9300Mpt1327TxBytes = _Tn9300Mpt1327TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 6),
    _Tn9300Mpt1327TxBytes_Type()
)
tn9300Mpt1327TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327TxBytes.setStatus("current")
_Tn9300Mpt1327LinkErrors_Type = Counter32
_Tn9300Mpt1327LinkErrors_Object = MibScalar
tn9300Mpt1327LinkErrors = _Tn9300Mpt1327LinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 7),
    _Tn9300Mpt1327LinkErrors_Type()
)
tn9300Mpt1327LinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327LinkErrors.setStatus("current")
_Tn9300Mpt1327Connections_Type = Counter32
_Tn9300Mpt1327Connections_Object = MibScalar
tn9300Mpt1327Connections = _Tn9300Mpt1327Connections_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 5, 8),
    _Tn9300Mpt1327Connections_Type()
)
tn9300Mpt1327Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327Connections.setStatus("current")
_Tn9300Mpt1327ChObjs_ObjectIdentity = ObjectIdentity
tn9300Mpt1327ChObjs = _Tn9300Mpt1327ChObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6)
)
_Tn9300Mpt1327ChTable_Object = MibTable
tn9300Mpt1327ChTable = _Tn9300Mpt1327ChTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tn9300Mpt1327ChTable.setStatus("current")
_Tn9300Mpt1327ChEntry_Object = MibTableRow
tn9300Mpt1327ChEntry = _Tn9300Mpt1327ChEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1)
)
tn9300Mpt1327ChEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300Mpt1327ChNumber"),
)
if mibBuilder.loadTexts:
    tn9300Mpt1327ChEntry.setStatus("current")


class _Tn9300Mpt1327ChNumber_Type(Integer32):
    """Custom type tn9300Mpt1327ChNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Tn9300Mpt1327ChNumber_Type.__name__ = "Integer32"
_Tn9300Mpt1327ChNumber_Object = MibTableColumn
tn9300Mpt1327ChNumber = _Tn9300Mpt1327ChNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 1),
    _Tn9300Mpt1327ChNumber_Type()
)
tn9300Mpt1327ChNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChNumber.setStatus("current")
_Tn9300Mpt1327ChIpAddressType_Type = InetAddressType
_Tn9300Mpt1327ChIpAddressType_Object = MibTableColumn
tn9300Mpt1327ChIpAddressType = _Tn9300Mpt1327ChIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 2),
    _Tn9300Mpt1327ChIpAddressType_Type()
)
tn9300Mpt1327ChIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChIpAddressType.setStatus("current")


class _Tn9300Mpt1327ChIpAddress_Type(InetAddress):
    """Custom type tn9300Mpt1327ChIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300Mpt1327ChIpAddress_Type.__name__ = "InetAddress"
_Tn9300Mpt1327ChIpAddress_Object = MibTableColumn
tn9300Mpt1327ChIpAddress = _Tn9300Mpt1327ChIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 3),
    _Tn9300Mpt1327ChIpAddress_Type()
)
tn9300Mpt1327ChIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChIpAddress.setStatus("current")
_Tn9300Mpt1327ChPort_Type = Integer32
_Tn9300Mpt1327ChPort_Object = MibTableColumn
tn9300Mpt1327ChPort = _Tn9300Mpt1327ChPort_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 4),
    _Tn9300Mpt1327ChPort_Type()
)
tn9300Mpt1327ChPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChPort.setStatus("current")
_Tn9300Mpt1327ChState_Type = Mpt1327ChannelState
_Tn9300Mpt1327ChState_Object = MibTableColumn
tn9300Mpt1327ChState = _Tn9300Mpt1327ChState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 5),
    _Tn9300Mpt1327ChState_Type()
)
tn9300Mpt1327ChState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChState.setStatus("current")
_Tn9300Mpt1327ChLinkState_Type = NgwLinkState
_Tn9300Mpt1327ChLinkState_Object = MibTableColumn
tn9300Mpt1327ChLinkState = _Tn9300Mpt1327ChLinkState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 6),
    _Tn9300Mpt1327ChLinkState_Type()
)
tn9300Mpt1327ChLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChLinkState.setStatus("current")
_Tn9300Mpt1327ChAParty_Type = DisplayString
_Tn9300Mpt1327ChAParty_Object = MibTableColumn
tn9300Mpt1327ChAParty = _Tn9300Mpt1327ChAParty_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 7),
    _Tn9300Mpt1327ChAParty_Type()
)
tn9300Mpt1327ChAParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChAParty.setStatus("current")
_Tn9300Mpt1327ChBParty_Type = DisplayString
_Tn9300Mpt1327ChBParty_Object = MibTableColumn
tn9300Mpt1327ChBParty = _Tn9300Mpt1327ChBParty_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 8),
    _Tn9300Mpt1327ChBParty_Type()
)
tn9300Mpt1327ChBParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChBParty.setStatus("current")
_Tn9300Mpt1327ChNgpRxPackets_Type = Counter32
_Tn9300Mpt1327ChNgpRxPackets_Object = MibTableColumn
tn9300Mpt1327ChNgpRxPackets = _Tn9300Mpt1327ChNgpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 9),
    _Tn9300Mpt1327ChNgpRxPackets_Type()
)
tn9300Mpt1327ChNgpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChNgpRxPackets.setStatus("current")
_Tn9300Mpt1327ChNgpTxPackets_Type = Counter32
_Tn9300Mpt1327ChNgpTxPackets_Object = MibTableColumn
tn9300Mpt1327ChNgpTxPackets = _Tn9300Mpt1327ChNgpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 10),
    _Tn9300Mpt1327ChNgpTxPackets_Type()
)
tn9300Mpt1327ChNgpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChNgpTxPackets.setStatus("current")
_Tn9300Mpt1327ChNgpLostPackets_Type = Counter32
_Tn9300Mpt1327ChNgpLostPackets_Object = MibTableColumn
tn9300Mpt1327ChNgpLostPackets = _Tn9300Mpt1327ChNgpLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 11),
    _Tn9300Mpt1327ChNgpLostPackets_Type()
)
tn9300Mpt1327ChNgpLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChNgpLostPackets.setStatus("current")
_Tn9300Mpt1327ChRtpRxPackets_Type = Counter32
_Tn9300Mpt1327ChRtpRxPackets_Object = MibTableColumn
tn9300Mpt1327ChRtpRxPackets = _Tn9300Mpt1327ChRtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 12),
    _Tn9300Mpt1327ChRtpRxPackets_Type()
)
tn9300Mpt1327ChRtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChRtpRxPackets.setStatus("current")
_Tn9300Mpt1327ChRtpTxPackets_Type = Counter32
_Tn9300Mpt1327ChRtpTxPackets_Object = MibTableColumn
tn9300Mpt1327ChRtpTxPackets = _Tn9300Mpt1327ChRtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 13),
    _Tn9300Mpt1327ChRtpTxPackets_Type()
)
tn9300Mpt1327ChRtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChRtpTxPackets.setStatus("current")
_Tn9300Mpt1327ChRtpLostPackets_Type = Counter32
_Tn9300Mpt1327ChRtpLostPackets_Object = MibTableColumn
tn9300Mpt1327ChRtpLostPackets = _Tn9300Mpt1327ChRtpLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 14),
    _Tn9300Mpt1327ChRtpLostPackets_Type()
)
tn9300Mpt1327ChRtpLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChRtpLostPackets.setStatus("current")
_Tn9300Mpt1327ChRtpRtt_Type = Gauge32
_Tn9300Mpt1327ChRtpRtt_Object = MibTableColumn
tn9300Mpt1327ChRtpRtt = _Tn9300Mpt1327ChRtpRtt_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 15),
    _Tn9300Mpt1327ChRtpRtt_Type()
)
tn9300Mpt1327ChRtpRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChRtpRtt.setStatus("current")
_Tn9300Mpt1327ChRtpJitter_Type = Gauge32
_Tn9300Mpt1327ChRtpJitter_Object = MibTableColumn
tn9300Mpt1327ChRtpJitter = _Tn9300Mpt1327ChRtpJitter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 6, 1, 1, 16),
    _Tn9300Mpt1327ChRtpJitter_Type()
)
tn9300Mpt1327ChRtpJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300Mpt1327ChRtpJitter.setStatus("current")
_Tn9300RemoteNodeObjs_ObjectIdentity = ObjectIdentity
tn9300RemoteNodeObjs = _Tn9300RemoteNodeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7)
)
_Tn9300RemoteNodeTable_Object = MibTable
tn9300RemoteNodeTable = _Tn9300RemoteNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeTable.setStatus("current")
_Tn9300RemoteNodeEntry_Object = MibTableRow
tn9300RemoteNodeEntry = _Tn9300RemoteNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1)
)
tn9300RemoteNodeEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300RemoteNodeNumber"),
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeEntry.setStatus("current")


class _Tn9300RemoteNodeNumber_Type(Integer32):
    """Custom type tn9300RemoteNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Tn9300RemoteNodeNumber_Type.__name__ = "Integer32"
_Tn9300RemoteNodeNumber_Object = MibTableColumn
tn9300RemoteNodeNumber = _Tn9300RemoteNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 1),
    _Tn9300RemoteNodeNumber_Type()
)
tn9300RemoteNodeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300RemoteNodeNumber.setStatus("current")
_Tn9300RemoteNodeName_Type = DisplayString
_Tn9300RemoteNodeName_Object = MibTableColumn
tn9300RemoteNodeName = _Tn9300RemoteNodeName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 2),
    _Tn9300RemoteNodeName_Type()
)
tn9300RemoteNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodeName.setStatus("current")
_Tn9300RemoteNodeIpAddrType_Type = InetAddressType
_Tn9300RemoteNodeIpAddrType_Object = MibTableColumn
tn9300RemoteNodeIpAddrType = _Tn9300RemoteNodeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 3),
    _Tn9300RemoteNodeIpAddrType_Type()
)
tn9300RemoteNodeIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodeIpAddrType.setStatus("current")


class _Tn9300RemoteNodeIpAddr_Type(InetAddress):
    """Custom type tn9300RemoteNodeIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300RemoteNodeIpAddr_Type.__name__ = "InetAddress"
_Tn9300RemoteNodeIpAddr_Object = MibTableColumn
tn9300RemoteNodeIpAddr = _Tn9300RemoteNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 4),
    _Tn9300RemoteNodeIpAddr_Type()
)
tn9300RemoteNodeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodeIpAddr.setStatus("current")
_Tn9300RemoteNodePriority_Type = Integer32
_Tn9300RemoteNodePriority_Object = MibTableColumn
tn9300RemoteNodePriority = _Tn9300RemoteNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 5),
    _Tn9300RemoteNodePriority_Type()
)
tn9300RemoteNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodePriority.setStatus("current")
_Tn9300RemoteNodeState_Type = RemoteNodeState
_Tn9300RemoteNodeState_Object = MibTableColumn
tn9300RemoteNodeState = _Tn9300RemoteNodeState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 6),
    _Tn9300RemoteNodeState_Type()
)
tn9300RemoteNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodeState.setStatus("current")
_Tn9300RemoteNodeCallSw_Type = Gauge32
_Tn9300RemoteNodeCallSw_Object = MibTableColumn
tn9300RemoteNodeCallSw = _Tn9300RemoteNodeCallSw_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 7),
    _Tn9300RemoteNodeCallSw_Type()
)
tn9300RemoteNodeCallSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodeCallSw.setStatus("current")
_Tn9300RemoteNodeConnectSw_Type = Gauge32
_Tn9300RemoteNodeConnectSw_Object = MibTableColumn
tn9300RemoteNodeConnectSw = _Tn9300RemoteNodeConnectSw_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 8),
    _Tn9300RemoteNodeConnectSw_Type()
)
tn9300RemoteNodeConnectSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodeConnectSw.setStatus("current")
_Tn9300RemoteNodeSynced_Type = RemoteNodeSyncState
_Tn9300RemoteNodeSynced_Object = MibTableColumn
tn9300RemoteNodeSynced = _Tn9300RemoteNodeSynced_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 7, 1, 1, 9),
    _Tn9300RemoteNodeSynced_Type()
)
tn9300RemoteNodeSynced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300RemoteNodeSynced.setStatus("current")
_Tn9300MobileIpObjs_ObjectIdentity = ObjectIdentity
tn9300MobileIpObjs = _Tn9300MobileIpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8)
)
_Tn9300MipRegistered_Type = Integer32
_Tn9300MipRegistered_Object = MibScalar
tn9300MipRegistered = _Tn9300MipRegistered_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 1),
    _Tn9300MipRegistered_Type()
)
tn9300MipRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipRegistered.setStatus("current")
_Tn9300MipFailing_Type = Integer32
_Tn9300MipFailing_Object = MibScalar
tn9300MipFailing = _Tn9300MipFailing_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 2),
    _Tn9300MipFailing_Type()
)
tn9300MipFailing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipFailing.setStatus("current")
_Tn9300MipTimeouts_Type = Counter32
_Tn9300MipTimeouts_Object = MibScalar
tn9300MipTimeouts = _Tn9300MipTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 3),
    _Tn9300MipTimeouts_Type()
)
tn9300MipTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipTimeouts.setStatus("current")
_Tn9300MipRejections_Type = Counter32
_Tn9300MipRejections_Object = MibScalar
tn9300MipRejections = _Tn9300MipRejections_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 4),
    _Tn9300MipRejections_Type()
)
tn9300MipRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipRejections.setStatus("current")
_Tn9300MipIcmpRxPackets_Type = Counter32
_Tn9300MipIcmpRxPackets_Object = MibScalar
tn9300MipIcmpRxPackets = _Tn9300MipIcmpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 5),
    _Tn9300MipIcmpRxPackets_Type()
)
tn9300MipIcmpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipIcmpRxPackets.setStatus("current")
_Tn9300MipIcmpTxPackets_Type = Counter32
_Tn9300MipIcmpTxPackets_Object = MibScalar
tn9300MipIcmpTxPackets = _Tn9300MipIcmpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 6),
    _Tn9300MipIcmpTxPackets_Type()
)
tn9300MipIcmpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipIcmpTxPackets.setStatus("current")
_Tn9300MipUdpRxPackets_Type = Counter32
_Tn9300MipUdpRxPackets_Object = MibScalar
tn9300MipUdpRxPackets = _Tn9300MipUdpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 7),
    _Tn9300MipUdpRxPackets_Type()
)
tn9300MipUdpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipUdpRxPackets.setStatus("current")
_Tn9300MipUdpTxPackets_Type = Counter32
_Tn9300MipUdpTxPackets_Object = MibScalar
tn9300MipUdpTxPackets = _Tn9300MipUdpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 8),
    _Tn9300MipUdpTxPackets_Type()
)
tn9300MipUdpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipUdpTxPackets.setStatus("current")
_Tn9300MipRxBytes_Type = Counter32
_Tn9300MipRxBytes_Object = MibScalar
tn9300MipRxBytes = _Tn9300MipRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 9),
    _Tn9300MipRxBytes_Type()
)
tn9300MipRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipRxBytes.setStatus("current")
_Tn9300MipTxBytes_Type = Counter32
_Tn9300MipTxBytes_Object = MibScalar
tn9300MipTxBytes = _Tn9300MipTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 8, 10),
    _Tn9300MipTxBytes_Type()
)
tn9300MipTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300MipTxBytes.setStatus("current")
_Tn9300UnitObjs_ObjectIdentity = ObjectIdentity
tn9300UnitObjs = _Tn9300UnitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 9)
)
_Tn9300UnitTable_Object = MibTable
tn9300UnitTable = _Tn9300UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tn9300UnitTable.setStatus("current")
_Tn9300UnitEntry_Object = MibTableRow
tn9300UnitEntry = _Tn9300UnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 9, 1, 1)
)
tn9300UnitEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300UnitAddress"),
)
if mibBuilder.loadTexts:
    tn9300UnitEntry.setStatus("current")


class _Tn9300UnitAddress_Type(Integer32):
    """Custom type tn9300UnitAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_Tn9300UnitAddress_Type.__name__ = "Integer32"
_Tn9300UnitAddress_Object = MibTableColumn
tn9300UnitAddress = _Tn9300UnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 9, 1, 1, 1),
    _Tn9300UnitAddress_Type()
)
tn9300UnitAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300UnitAddress.setStatus("current")
_Tn9300UnitAlias_Type = DisplayString
_Tn9300UnitAlias_Object = MibTableColumn
tn9300UnitAlias = _Tn9300UnitAlias_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 9, 1, 1, 2),
    _Tn9300UnitAlias_Type()
)
tn9300UnitAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300UnitAlias.setStatus("current")
_Tn9300UnitAuthentication_Type = UnitAuthentication
_Tn9300UnitAuthentication_Object = MibTableColumn
tn9300UnitAuthentication = _Tn9300UnitAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 9, 1, 1, 3),
    _Tn9300UnitAuthentication_Type()
)
tn9300UnitAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn9300UnitAuthentication.setStatus("current")
_Tn9300UnitStatusMessageId_Type = UnitStatusMessageId
_Tn9300UnitStatusMessageId_Object = MibScalar
tn9300UnitStatusMessageId = _Tn9300UnitStatusMessageId_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 9, 2),
    _Tn9300UnitStatusMessageId_Type()
)
tn9300UnitStatusMessageId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300UnitStatusMessageId.setStatus("current")
_Tn9300NetworkGwObjs_ObjectIdentity = ObjectIdentity
tn9300NetworkGwObjs = _Tn9300NetworkGwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 10)
)
_Tn9300NetworkGwTable_Object = MibTable
tn9300NetworkGwTable = _Tn9300NetworkGwTable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 10, 1)
)
if mibBuilder.loadTexts:
    tn9300NetworkGwTable.setStatus("current")
_Tn9300NetworkGwEntry_Object = MibTableRow
tn9300NetworkGwEntry = _Tn9300NetworkGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 10, 1, 1)
)
tn9300NetworkGwEntry.setIndexNames(
    (0, "TAIT-TN9300-MIB", "tn9300NetworkGwId"),
)
if mibBuilder.loadTexts:
    tn9300NetworkGwEntry.setStatus("current")


class _Tn9300NetworkGwId_Type(Integer32):
    """Custom type tn9300NetworkGwId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Tn9300NetworkGwId_Type.__name__ = "Integer32"
_Tn9300NetworkGwId_Object = MibTableColumn
tn9300NetworkGwId = _Tn9300NetworkGwId_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 10, 1, 1, 1),
    _Tn9300NetworkGwId_Type()
)
tn9300NetworkGwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn9300NetworkGwId.setStatus("current")
_Tn9300NetworkGwConnOk_Type = TruthValue
_Tn9300NetworkGwConnOk_Object = MibTableColumn
tn9300NetworkGwConnOk = _Tn9300NetworkGwConnOk_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 10, 1, 1, 2),
    _Tn9300NetworkGwConnOk_Type()
)
tn9300NetworkGwConnOk.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300NetworkGwConnOk.setStatus("current")
_Tn9300NetworkGwIpAddrType_Type = InetAddressType
_Tn9300NetworkGwIpAddrType_Object = MibTableColumn
tn9300NetworkGwIpAddrType = _Tn9300NetworkGwIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 10, 1, 1, 3),
    _Tn9300NetworkGwIpAddrType_Type()
)
tn9300NetworkGwIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300NetworkGwIpAddrType.setStatus("current")


class _Tn9300NetworkGwIpAddr_Type(InetAddress):
    """Custom type tn9300NetworkGwIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Tn9300NetworkGwIpAddr_Type.__name__ = "InetAddress"
_Tn9300NetworkGwIpAddr_Object = MibTableColumn
tn9300NetworkGwIpAddr = _Tn9300NetworkGwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 10, 1, 1, 4),
    _Tn9300NetworkGwIpAddr_Type()
)
tn9300NetworkGwIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300NetworkGwIpAddr.setStatus("current")
_Tn9300EventObjs_ObjectIdentity = ObjectIdentity
tn9300EventObjs = _Tn9300EventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 99)
)
_Tn9300EventSeverity_Type = EventSeverity
_Tn9300EventSeverity_Object = MibScalar
tn9300EventSeverity = _Tn9300EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 99, 2),
    _Tn9300EventSeverity_Type()
)
tn9300EventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300EventSeverity.setStatus("current")
_Tn9300EventUnitAddress_Type = Integer32
_Tn9300EventUnitAddress_Object = MibScalar
tn9300EventUnitAddress = _Tn9300EventUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 99, 3),
    _Tn9300EventUnitAddress_Type()
)
tn9300EventUnitAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300EventUnitAddress.setStatus("current")
_Tn9300EventBaseStationNumber_Type = Integer32
_Tn9300EventBaseStationNumber_Object = MibScalar
tn9300EventBaseStationNumber = _Tn9300EventBaseStationNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 99, 4),
    _Tn9300EventBaseStationNumber_Type()
)
tn9300EventBaseStationNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300EventBaseStationNumber.setStatus("current")
_Tn9300EventChannelNumber_Type = Integer32
_Tn9300EventChannelNumber_Object = MibScalar
tn9300EventChannelNumber = _Tn9300EventChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 99, 5),
    _Tn9300EventChannelNumber_Type()
)
tn9300EventChannelNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300EventChannelNumber.setStatus("current")
_Tn9300EventNetworkGwId_Type = Integer32
_Tn9300EventNetworkGwId_Object = MibScalar
tn9300EventNetworkGwId = _Tn9300EventNetworkGwId_Object(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 2, 99, 6),
    _Tn9300EventNetworkGwId_Type()
)
tn9300EventNetworkGwId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tn9300EventNetworkGwId.setStatus("current")
_Tn9300Events_ObjectIdentity = ObjectIdentity
tn9300Events = _Tn9300Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3)
)
_Tn9300EventsV2_ObjectIdentity = ObjectIdentity
tn9300EventsV2 = _Tn9300EventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0)
)
_Tn9300ObjectsForEvents_ObjectIdentity = ObjectIdentity
tn9300ObjectsForEvents = _Tn9300ObjectsForEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 99)
)
_Tn9300CgmMIB_ObjectIdentity = ObjectIdentity
tn9300CgmMIB = _Tn9300CgmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 4)
)

# Managed Objects groups

tn9300StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 1)
)
tn9300StatusGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300Version"),
        ("TAIT-TN9300-MIB", "tn9300Name"),
        ("TAIT-TN9300-MIB", "tn9300Priority"),
        ("TAIT-TN9300-MIB", "tn9300RequestedState"),
        ("TAIT-TN9300-MIB", "tn9300State"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressAType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckStateA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressBType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressB"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckStateB"),
        ("TAIT-TN9300-MIB", "tn9300CallsSwitching"),
        ("TAIT-TN9300-MIB", "tn9300ConnectionsSwitching"),
        ("TAIT-TN9300-MIB", "tn9300MemoryUsage"),
        ("TAIT-TN9300-MIB", "tn9300CpuUsage"),
        ("TAIT-TN9300-MIB", "tn9300DiskSpaceOk"),
        ("TAIT-TN9300-MIB", "tn9300LicenseValidity"))
)
if mibBuilder.loadTexts:
    tn9300StatusGroup.setStatus("current")

tn9300SiteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 2)
)
tn9300SiteGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300SiteSyscode"),
        ("TAIT-TN9300-MIB", "tn9300SiteEnabled"),
        ("TAIT-TN9300-MIB", "tn9300SiteOk"),
        ("TAIT-TN9300-MIB", "tn9300SiteAutoQueueDepth"),
        ("TAIT-TN9300-MIB", "tn9300SiteQueueDepth"),
        ("TAIT-TN9300-MIB", "tn9300SiteZone"),
        ("TAIT-TN9300-MIB", "tn9300SiteExtraWaitSlots"),
        ("TAIT-TN9300-MIB", "tn9300SiteCCReassignTimeout"),
        ("TAIT-TN9300-MIB", "tn9300SiteTCRotation"),
        ("TAIT-TN9300-MIB", "tn9300SiteRxActivityTimeout"),
        ("TAIT-TN9300-MIB", "tn9300SiteRxInactiveTimeout"),
        ("TAIT-TN9300-MIB", "tn9300SiteFramelength"),
        ("TAIT-TN9300-MIB", "tn9300SiteMinFramelength"),
        ("TAIT-TN9300-MIB", "tn9300SiteMaxFramelength"),
        ("TAIT-TN9300-MIB", "tn9300SiteDualCC"),
        ("TAIT-TN9300-MIB", "tn9300SiteOpenMuteTimeout"),
        ("TAIT-TN9300-MIB", "tn9300SiteManAdjSiteRF"),
        ("TAIT-TN9300-MIB", "tn9300SiteManAdjSiteSyscode"),
        ("TAIT-TN9300-MIB", "tn9300SiteNChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteNControlChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteNTrafficChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteNIdleChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteNDisabledChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteNFailedChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteNOnAirCalls"),
        ("TAIT-TN9300-MIB", "tn9300SiteNRingingCalls"),
        ("TAIT-TN9300-MIB", "tn9300SiteNQueuedCalls"),
        ("TAIT-TN9300-MIB", "tn9300SiteTotalCalls"),
        ("TAIT-TN9300-MIB", "tn9300SiteTotalChannelCalls"),
        ("TAIT-TN9300-MIB", "tn9300SiteTotalQueueTime"),
        ("TAIT-TN9300-MIB", "tn9300SiteChannelTimeFailed"),
        ("TAIT-TN9300-MIB", "tn9300SiteChannelTimeTraffic"),
        ("TAIT-TN9300-MIB", "tn9300SiteChannelTimeControl"),
        ("TAIT-TN9300-MIB", "tn9300SiteChannelTimeIdle"),
        ("TAIT-TN9300-MIB", "tn9300SiteCallsQueuedUnder5"),
        ("TAIT-TN9300-MIB", "tn9300SiteCallsQueued5To10"),
        ("TAIT-TN9300-MIB", "tn9300SiteCallsQueued10To20"),
        ("TAIT-TN9300-MIB", "tn9300SiteCallsQueuedOver20"),
        ("TAIT-TN9300-MIB", "tn9300SiteAlias"),
        ("TAIT-TN9300-MIB", "tn9300AdjSiteAlias"),
        ("TAIT-TN9300-MIB", "tn9300AdjSiteSyscode1"),
        ("TAIT-TN9300-MIB", "tn9300AdjSiteSyscode2"),
        ("TAIT-TN9300-MIB", "tn9300AdjSiteRF1"),
        ("TAIT-TN9300-MIB", "tn9300AdjSiteRF2"),
        ("TAIT-TN9300-MIB", "tn9300SiteControlChCountOk"),
        ("TAIT-TN9300-MIB", "tn9300SiteNAlternateChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteChannelTimeAlternate"))
)
if mibBuilder.loadTexts:
    tn9300SiteGroup.setStatus("current")

tn9300ChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 3)
)
tn9300ChannelGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300ChannelIpAddressType"),
        ("TAIT-TN9300-MIB", "tn9300ChannelIpAddress"),
        ("TAIT-TN9300-MIB", "tn9300ChannelPort"),
        ("TAIT-TN9300-MIB", "tn9300ChannelRf"),
        ("TAIT-TN9300-MIB", "tn9300ChannelEnabled"),
        ("TAIT-TN9300-MIB", "tn9300ChannelControlAllowed"),
        ("TAIT-TN9300-MIB", "tn9300ChannelTrafficAllowed"),
        ("TAIT-TN9300-MIB", "tn9300ChannelInhibitIfJammed"),
        ("TAIT-TN9300-MIB", "tn9300ChannelState"),
        ("TAIT-TN9300-MIB", "tn9300ChannelJammed"),
        ("TAIT-TN9300-MIB", "tn9300ChannelMinorAlarm"),
        ("TAIT-TN9300-MIB", "tn9300ChannelMajorAlarm"),
        ("TAIT-TN9300-MIB", "tn9300ChannelAParty"),
        ("TAIT-TN9300-MIB", "tn9300ChannelBParty"),
        ("TAIT-TN9300-MIB", "tn9300ChannelBspRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300ChannelBspTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300ChannelBspLostPackets"),
        ("TAIT-TN9300-MIB", "tn9300ChannelRtpRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300ChannelRtpTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300ChannelRtpLostPackets"),
        ("TAIT-TN9300-MIB", "tn9300ChannelRtpRtt"),
        ("TAIT-TN9300-MIB", "tn9300ChannelRtpRttJitter"),
        ("TAIT-TN9300-MIB", "tn9300ChannelTimeFailed"),
        ("TAIT-TN9300-MIB", "tn9300ChannelTimeTraffic"),
        ("TAIT-TN9300-MIB", "tn9300ChannelTimeControl"),
        ("TAIT-TN9300-MIB", "tn9300ChannelTimeIdle"),
        ("TAIT-TN9300-MIB", "tn9300ChannelAlternateAllowed"),
        ("TAIT-TN9300-MIB", "tn9300ChannelTimeAlternate"))
)
if mibBuilder.loadTexts:
    tn9300ChannelGroup.setStatus("current")

tn9300Mpt1327Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 6)
)
tn9300Mpt1327Group.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300Mpt1327IpAddressType"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327IpAddress"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327Port"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327State"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327RxBytes"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327TxBytes"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327LinkErrors"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327Connections"))
)
if mibBuilder.loadTexts:
    tn9300Mpt1327Group.setStatus("current")

tn9300Mpt1327ChGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 7)
)
tn9300Mpt1327ChGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300Mpt1327ChIpAddressType"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChIpAddress"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChPort"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChState"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChLinkState"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChAParty"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChBParty"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChNgpRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChNgpTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChNgpLostPackets"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChRtpRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChRtpTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChRtpLostPackets"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChRtpRtt"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChRtpJitter"))
)
if mibBuilder.loadTexts:
    tn9300Mpt1327ChGroup.setStatus("current")

tn9300SipLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 8)
)
tn9300SipLineGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300SipLineName"),
        ("TAIT-TN9300-MIB", "tn9300SipLineIncomingType"),
        ("TAIT-TN9300-MIB", "tn9300SipLineSpchVotePri"),
        ("TAIT-TN9300-MIB", "tn9300SipLineIpAddressType"),
        ("TAIT-TN9300-MIB", "tn9300SipLineIpAddress"),
        ("TAIT-TN9300-MIB", "tn9300SipLineState"),
        ("TAIT-TN9300-MIB", "tn9300SipLineUptime"),
        ("TAIT-TN9300-MIB", "tn9300SipLineConnects"),
        ("TAIT-TN9300-MIB", "tn9300SipLineRegistrationType"),
        ("TAIT-TN9300-MIB", "tn9300SipLineUserName"),
        ("TAIT-TN9300-MIB", "tn9300SipLineEnabled"),
        ("TAIT-TN9300-MIB", "tn9300SipLineAisMultipartContents"),
        ("TAIT-TN9300-MIB", "tn9300SipLineAisMonitor"),
        ("TAIT-TN9300-MIB", "tn9300SipLineSipGroup"),
        ("TAIT-TN9300-MIB", "tn9300SipLineInphoneTable"),
        ("TAIT-TN9300-MIB", "tn9300SipLineProxyAddressType"),
        ("TAIT-TN9300-MIB", "tn9300SipLineProxyAddress"),
        ("TAIT-TN9300-MIB", "tn9300SipLineCalls"))
)
if mibBuilder.loadTexts:
    tn9300SipLineGroup.setStatus("current")

tn9300DipLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 9)
)
tn9300DipLineGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300DipLineName"),
        ("TAIT-TN9300-MIB", "tn9300DipLineNgwIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300DipLineNgwIpAddr"),
        ("TAIT-TN9300-MIB", "tn9300DipLineAddress"),
        ("TAIT-TN9300-MIB", "tn9300DipLinePilotAddress"),
        ("TAIT-TN9300-MIB", "tn9300DipLineSpchVotePri"),
        ("TAIT-TN9300-MIB", "tn9300DipLineState"),
        ("TAIT-TN9300-MIB", "tn9300DipLineNgwLinkState"),
        ("TAIT-TN9300-MIB", "tn9300DipLineAParty"),
        ("TAIT-TN9300-MIB", "tn9300DipLineBParty"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddr"),
        ("TAIT-TN9300-MIB", "tn9300DipLineClientUptime"),
        ("TAIT-TN9300-MIB", "tn9300DipLineClientConnects"),
        ("TAIT-TN9300-MIB", "tn9300DipLineNgpRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300DipLineNgpTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300DipLineNgpLostPackets"),
        ("TAIT-TN9300-MIB", "tn9300DipLineRtpRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300DipLineRtpTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300DipLineRtpLostPackets"),
        ("TAIT-TN9300-MIB", "tn9300DipLineRtpRtt"),
        ("TAIT-TN9300-MIB", "tn9300DipLineRtpJitter"))
)
if mibBuilder.loadTexts:
    tn9300DipLineGroup.setStatus("current")

tn9300RemoteNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 10)
)
tn9300RemoteNodeGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300RemoteNodeName"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddr"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodePriority"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeState"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeCallSw"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeConnectSw"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeSynced"))
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeGroup.setStatus("current")

tn9300MobileIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 13)
)
tn9300MobileIpGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300MipRegistered"),
        ("TAIT-TN9300-MIB", "tn9300MipFailing"),
        ("TAIT-TN9300-MIB", "tn9300MipTimeouts"),
        ("TAIT-TN9300-MIB", "tn9300MipRejections"),
        ("TAIT-TN9300-MIB", "tn9300MipIcmpRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300MipIcmpTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300MipUdpRxPackets"),
        ("TAIT-TN9300-MIB", "tn9300MipUdpTxPackets"),
        ("TAIT-TN9300-MIB", "tn9300MipRxBytes"),
        ("TAIT-TN9300-MIB", "tn9300MipTxBytes"))
)
if mibBuilder.loadTexts:
    tn9300MobileIpGroup.setStatus("current")

tn9300UnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 14)
)
tn9300UnitGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300UnitAlias"),
        ("TAIT-TN9300-MIB", "tn9300UnitStatusMessageId"),
        ("TAIT-TN9300-MIB", "tn9300UnitAuthentication"))
)
if mibBuilder.loadTexts:
    tn9300UnitGroup.setStatus("current")

tn9300EventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 15)
)
tn9300EventObjectGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300EventUnitAddress"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"),
        ("TAIT-TN9300-MIB", "tn9300EventChannelNumber"),
        ("TAIT-TN9300-MIB", "tn9300EventNetworkGwId"))
)
if mibBuilder.loadTexts:
    tn9300EventObjectGroup.setStatus("current")

tn9300NetworkGwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 17)
)
tn9300NetworkGwGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300NetworkGwConnOk"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGwIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGwIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300NetworkGwGroup.setStatus("current")


# Notification objects

tn9300NodeActivationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 1)
)
tn9300NodeActivationEvent.setObjects(
    ("TAIT-TN9300-MIB", "tn9300State")
)
if mibBuilder.loadTexts:
    tn9300NodeActivationEvent.setStatus(
        "current"
    )

tn9300SiteFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 2)
)
tn9300SiteFailureEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300SiteOk"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"))
)
if mibBuilder.loadTexts:
    tn9300SiteFailureEvent.setStatus(
        "current"
    )

tn9300SiteOkEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 3)
)
tn9300SiteOkEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300SiteOk"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"))
)
if mibBuilder.loadTexts:
    tn9300SiteOkEvent.setStatus(
        "current"
    )

tn9300ChannelMinorAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 4)
)
tn9300ChannelMinorAlarmEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300ChannelMinorAlarm"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelMinorAlarmEvent.setStatus(
        "current"
    )

tn9300ChannelMajorAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 5)
)
tn9300ChannelMajorAlarmEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300ChannelMajorAlarm"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelMajorAlarmEvent.setStatus(
        "current"
    )

tn9300ChannelFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 6)
)
tn9300ChannelFailureEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300ChannelState"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelFailureEvent.setStatus(
        "current"
    )

tn9300ChannelOkEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 7)
)
tn9300ChannelOkEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300ChannelState"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelOkEvent.setStatus(
        "current"
    )

tn9300ChannelJammedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 8)
)
tn9300ChannelJammedEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300ChannelJammed"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"),
        ("TAIT-TN9300-MIB", "tn9300EventChannelNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelJammedEvent.setStatus(
        "current"
    )

tn9300ChannelUnjammedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 9)
)
tn9300ChannelUnjammedEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300ChannelJammed"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"),
        ("TAIT-TN9300-MIB", "tn9300EventChannelNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelUnjammedEvent.setStatus(
        "current"
    )

tn9300SipLinkUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 14)
)
tn9300SipLinkUpEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300SipLineState"),
        ("TAIT-TN9300-MIB", "tn9300SipLineIpAddressType"),
        ("TAIT-TN9300-MIB", "tn9300SipLineIpAddress"))
)
if mibBuilder.loadTexts:
    tn9300SipLinkUpEvent.setStatus(
        "current"
    )

tn9300SipLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 15)
)
tn9300SipLinkDownEvent.setObjects(
    ("TAIT-TN9300-MIB", "tn9300SipLineState")
)
if mibBuilder.loadTexts:
    tn9300SipLinkDownEvent.setStatus(
        "current"
    )

tn9300DipLinkUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 16)
)
tn9300DipLinkUpEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300DipLineState"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddr"),
        ("TAIT-TN9300-MIB", "tn9300DipLineAddress"))
)
if mibBuilder.loadTexts:
    tn9300DipLinkUpEvent.setStatus(
        "current"
    )

tn9300DipLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 17)
)
tn9300DipLinkDownEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300DipLineState"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddr"),
        ("TAIT-TN9300-MIB", "tn9300DipLineAddress"))
)
if mibBuilder.loadTexts:
    tn9300DipLinkDownEvent.setStatus(
        "current"
    )

tn9300ControlChannelEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 18)
)
tn9300ControlChannelEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300SiteNControlChannels"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"))
)
if mibBuilder.loadTexts:
    tn9300ControlChannelEvent.setStatus(
        "current"
    )

tn9300NetworkErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 19)
)
tn9300NetworkErrorEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300NetCheckStateA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressAType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckStateB"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressBType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressB"))
)
if mibBuilder.loadTexts:
    tn9300NetworkErrorEvent.setStatus(
        "current"
    )

tn9300RemoteNodeUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 20)
)
tn9300RemoteNodeUpEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300RemoteNodeState"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeUpEvent.setStatus(
        "current"
    )

tn9300RemoteNodeDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 21)
)
tn9300RemoteNodeDownEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300RemoteNodeState"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeDownEvent.setStatus(
        "current"
    )

tn9300LowDiskSpaceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 22)
)
if mibBuilder.loadTexts:
    tn9300LowDiskSpaceEvent.setStatus(
        "current"
    )

tn9300LicenseCheckFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 23)
)
if mibBuilder.loadTexts:
    tn9300LicenseCheckFailedEvent.setStatus(
        "current"
    )

tn9300NetworkGatewayUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 24)
)
if mibBuilder.loadTexts:
    tn9300NetworkGatewayUpEvent.setStatus(
        "current"
    )

tn9300NetworkGatewayDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 25)
)
if mibBuilder.loadTexts:
    tn9300NetworkGatewayDownEvent.setStatus(
        "current"
    )

tn9300NodeFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 26)
)
tn9300NodeFailedEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300NetCheckStateA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressAType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckStateB"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressBType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressB"))
)
if mibBuilder.loadTexts:
    tn9300NodeFailedEvent.setStatus(
        "current"
    )

tn9300NetworkUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 27)
)
tn9300NetworkUpEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300NetCheckStateA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressAType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckStateB"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressBType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressB"))
)
if mibBuilder.loadTexts:
    tn9300NetworkUpEvent.setStatus(
        "current"
    )

tn9300AuthenticationOkEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 28)
)
if mibBuilder.loadTexts:
    tn9300AuthenticationOkEvent.setStatus(
        "current"
    )

tn9300AuthenticationFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 29)
)
if mibBuilder.loadTexts:
    tn9300AuthenticationFailureEvent.setStatus(
        "current"
    )

tn9300UnitStatusMessageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 30)
)
tn9300UnitStatusMessageEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300UnitStatusMessageId"),
        ("TAIT-TN9300-MIB", "tn9300EventUnitAddress"))
)
if mibBuilder.loadTexts:
    tn9300UnitStatusMessageEvent.setStatus(
        "current"
    )

tn9300RemoteNodeSyncFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 31)
)
tn9300RemoteNodeSyncFailedEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300RemoteNodeState"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeSyncFailedEvent.setStatus(
        "current"
    )

tn9300RemoteNodeSyncOkEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 32)
)
tn9300RemoteNodeSyncOkEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300RemoteNodeState"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeSyncOkEvent.setStatus(
        "current"
    )

tn9300UnitDeregisteredBySystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 33)
)
tn9300UnitDeregisteredBySystemEvent.setObjects(
    ("TAIT-TN9300-MIB", "tn9300EventUnitAddress")
)
if mibBuilder.loadTexts:
    tn9300UnitDeregisteredBySystemEvent.setStatus(
        "current"
    )

tn9300NodeStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 34)
)
tn9300NodeStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300State"))
)
if mibBuilder.loadTexts:
    tn9300NodeStateEvent.setStatus(
        "current"
    )

tn9300NodeIpNetworkStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 35)
)
tn9300NodeIpNetworkStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckStateA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressAType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressA"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckStateB"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressBType"),
        ("TAIT-TN9300-MIB", "tn9300NetCheckAddressB"))
)
if mibBuilder.loadTexts:
    tn9300NodeIpNetworkStateEvent.setStatus(
        "current"
    )

tn9300NodeDiskSpaceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 36)
)
tn9300NodeDiskSpaceEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300DiskSpaceOk"))
)
if mibBuilder.loadTexts:
    tn9300NodeDiskSpaceEvent.setStatus(
        "current"
    )

tn9300NodeLicenseEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 37)
)
tn9300NodeLicenseEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300LicenseValidity"))
)
if mibBuilder.loadTexts:
    tn9300NodeLicenseEvent.setStatus(
        "current"
    )

tn9300SiteStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 38)
)
tn9300SiteStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300SiteOk"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"))
)
if mibBuilder.loadTexts:
    tn9300SiteStateEvent.setStatus(
        "current"
    )

tn9300SiteControlChCountEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 39)
)
tn9300SiteControlChCountEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300SiteControlChCountOk"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300SiteNControlChannels"))
)
if mibBuilder.loadTexts:
    tn9300SiteControlChCountEvent.setStatus(
        "current"
    )

tn9300BSMinorAlarmStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 40)
)
tn9300BSMinorAlarmStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300ChannelMinorAlarm"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"))
)
if mibBuilder.loadTexts:
    tn9300BSMinorAlarmStateEvent.setStatus(
        "current"
    )

tn9300BSMajorAlarmStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 41)
)
tn9300BSMajorAlarmStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300ChannelMajorAlarm"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"))
)
if mibBuilder.loadTexts:
    tn9300BSMajorAlarmStateEvent.setStatus(
        "current"
    )

tn9300BSStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 42)
)
tn9300BSStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300ChannelState"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"))
)
if mibBuilder.loadTexts:
    tn9300BSStateEvent.setStatus(
        "current"
    )

tn9300ChannelJammedStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 43)
)
tn9300ChannelJammedStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300ChannelJammed"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"),
        ("TAIT-TN9300-MIB", "tn9300EventChannelNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelJammedStateEvent.setStatus(
        "current"
    )

tn9300ChannelStuckMuteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 44)
)
tn9300ChannelStuckMuteEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300SiteName"),
        ("TAIT-TN9300-MIB", "tn9300EventBaseStationNumber"),
        ("TAIT-TN9300-MIB", "tn9300EventChannelNumber"))
)
if mibBuilder.loadTexts:
    tn9300ChannelStuckMuteEvent.setStatus(
        "current"
    )

tn9300SipLinkStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 45)
)
tn9300SipLinkStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300SipLineState"),
        ("TAIT-TN9300-MIB", "tn9300SipLineName"),
        ("TAIT-TN9300-MIB", "tn9300SipLineIpAddressType"),
        ("TAIT-TN9300-MIB", "tn9300SipLineIpAddress"))
)
if mibBuilder.loadTexts:
    tn9300SipLinkStateEvent.setStatus(
        "current"
    )

tn9300DipLinkStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 46)
)
tn9300DipLinkStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300DipLineState"),
        ("TAIT-TN9300-MIB", "tn9300DipLineName"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300DipLnClientIpAddr"),
        ("TAIT-TN9300-MIB", "tn9300DipLineAddress"))
)
if mibBuilder.loadTexts:
    tn9300DipLinkStateEvent.setStatus(
        "current"
    )

tn9300RemoteNodeStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 47)
)
tn9300RemoteNodeStateEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeState"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeName"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeStateEvent.setStatus(
        "current"
    )

tn9300RemoteNodeSyncEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 48)
)
tn9300RemoteNodeSyncEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeSynced"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeName"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300RemoteNodeSyncEvent.setStatus(
        "current"
    )

tn9300NetworkGwConnEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 49)
)
tn9300NetworkGwConnEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGwConnOk"),
        ("TAIT-TN9300-MIB", "tn9300EventNetworkGwId"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGwIpAddrType"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGwIpAddr"))
)
if mibBuilder.loadTexts:
    tn9300NetworkGwConnEvent.setStatus(
        "current"
    )

tn9300UnitAuthenticationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 50)
)
tn9300UnitAuthenticationEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300UnitAuthentication"),
        ("TAIT-TN9300-MIB", "tn9300EventUnitAddress"))
)
if mibBuilder.loadTexts:
    tn9300UnitAuthenticationEvent.setStatus(
        "current"
    )

tn9300UnitStatusMsgEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 51)
)
tn9300UnitStatusMsgEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300UnitStatusMessageId"),
        ("TAIT-TN9300-MIB", "tn9300EventUnitAddress"))
)
if mibBuilder.loadTexts:
    tn9300UnitStatusMsgEvent.setStatus(
        "current"
    )

tn9300UnitRegTimeoutEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 3, 0, 52)
)
tn9300UnitRegTimeoutEvent.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300EventSeverity"),
        ("TAIT-TN9300-MIB", "tn9300EventUnitAddress"))
)
if mibBuilder.loadTexts:
    tn9300UnitRegTimeoutEvent.setStatus(
        "current"
    )


# Notifications groups

tn9300EventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 12)
)
tn9300EventGroup.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300NodeActivationEvent"),
        ("TAIT-TN9300-MIB", "tn9300SiteFailureEvent"),
        ("TAIT-TN9300-MIB", "tn9300SiteOkEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelMinorAlarmEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelMajorAlarmEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelFailureEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelOkEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelJammedEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelUnjammedEvent"),
        ("TAIT-TN9300-MIB", "tn9300SipLinkUpEvent"),
        ("TAIT-TN9300-MIB", "tn9300SipLinkDownEvent"),
        ("TAIT-TN9300-MIB", "tn9300DipLinkUpEvent"),
        ("TAIT-TN9300-MIB", "tn9300DipLinkDownEvent"),
        ("TAIT-TN9300-MIB", "tn9300ControlChannelEvent"),
        ("TAIT-TN9300-MIB", "tn9300NetworkErrorEvent"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeUpEvent"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeDownEvent"),
        ("TAIT-TN9300-MIB", "tn9300LowDiskSpaceEvent"),
        ("TAIT-TN9300-MIB", "tn9300LicenseCheckFailedEvent"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGatewayUpEvent"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGatewayDownEvent"),
        ("TAIT-TN9300-MIB", "tn9300NodeFailedEvent"),
        ("TAIT-TN9300-MIB", "tn9300NetworkUpEvent"),
        ("TAIT-TN9300-MIB", "tn9300AuthenticationOkEvent"),
        ("TAIT-TN9300-MIB", "tn9300AuthenticationFailureEvent"),
        ("TAIT-TN9300-MIB", "tn9300UnitStatusMessageEvent"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeSyncFailedEvent"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeSyncOkEvent"),
        ("TAIT-TN9300-MIB", "tn9300UnitDeregisteredBySystemEvent"))
)
if mibBuilder.loadTexts:
    tn9300EventGroup.setStatus(
        "current"
    )

tn9300EventGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 1, 16)
)
tn9300EventGroupV2.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300NodeStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300NodeIpNetworkStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300NodeDiskSpaceEvent"),
        ("TAIT-TN9300-MIB", "tn9300NodeLicenseEvent"),
        ("TAIT-TN9300-MIB", "tn9300SiteStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300SiteControlChCountEvent"),
        ("TAIT-TN9300-MIB", "tn9300BSMinorAlarmStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300BSMajorAlarmStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300BSStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelJammedStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300ChannelStuckMuteEvent"),
        ("TAIT-TN9300-MIB", "tn9300SipLinkStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300DipLinkStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeStateEvent"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeSyncEvent"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGwConnEvent"),
        ("TAIT-TN9300-MIB", "tn9300UnitAuthenticationEvent"),
        ("TAIT-TN9300-MIB", "tn9300UnitStatusMsgEvent"),
        ("TAIT-TN9300-MIB", "tn9300UnitRegTimeoutEvent"))
)
if mibBuilder.loadTexts:
    tn9300EventGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tn9300ComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3570, 3, 6, 1, 2, 1)
)
tn9300ComplianceV1.setObjects(
      *(("TAIT-TN9300-MIB", "tn9300StatusGroup"),
        ("TAIT-TN9300-MIB", "tn9300SiteGroup"),
        ("TAIT-TN9300-MIB", "tn9300ChannelGroup"),
        ("TAIT-TN9300-MIB", "tn9300SipLineGroup"),
        ("TAIT-TN9300-MIB", "tn9300DipLineGroup"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327Group"),
        ("TAIT-TN9300-MIB", "tn9300Mpt1327ChGroup"),
        ("TAIT-TN9300-MIB", "tn9300RemoteNodeGroup"),
        ("TAIT-TN9300-MIB", "tn9300EventGroup"),
        ("TAIT-TN9300-MIB", "tn9300MobileIpGroup"),
        ("TAIT-TN9300-MIB", "tn9300UnitGroup"),
        ("TAIT-TN9300-MIB", "tn9300EventObjectGroup"),
        ("TAIT-TN9300-MIB", "tn9300EventGroupV2"),
        ("TAIT-TN9300-MIB", "tn9300NetworkGwGroup"))
)
if mibBuilder.loadTexts:
    tn9300ComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAIT-TN9300-MIB",
    **{"tn9300MibModule": tn9300MibModule,
       "tn9300MIB": tn9300MIB,
       "tn9300Confs": tn9300Confs,
       "tn9300Groups": tn9300Groups,
       "tn9300StatusGroup": tn9300StatusGroup,
       "tn9300SiteGroup": tn9300SiteGroup,
       "tn9300ChannelGroup": tn9300ChannelGroup,
       "tn9300Mpt1327Group": tn9300Mpt1327Group,
       "tn9300Mpt1327ChGroup": tn9300Mpt1327ChGroup,
       "tn9300SipLineGroup": tn9300SipLineGroup,
       "tn9300DipLineGroup": tn9300DipLineGroup,
       "tn9300RemoteNodeGroup": tn9300RemoteNodeGroup,
       "tn9300EventGroup": tn9300EventGroup,
       "tn9300MobileIpGroup": tn9300MobileIpGroup,
       "tn9300UnitGroup": tn9300UnitGroup,
       "tn9300EventObjectGroup": tn9300EventObjectGroup,
       "tn9300EventGroupV2": tn9300EventGroupV2,
       "tn9300NetworkGwGroup": tn9300NetworkGwGroup,
       "tn9300Compl": tn9300Compl,
       "tn9300ComplianceV1": tn9300ComplianceV1,
       "tn9300Objs": tn9300Objs,
       "tn9300NodeObjs": tn9300NodeObjs,
       "tn9300Version": tn9300Version,
       "tn9300Name": tn9300Name,
       "tn9300Priority": tn9300Priority,
       "tn9300RequestedState": tn9300RequestedState,
       "tn9300State": tn9300State,
       "tn9300NetCheckAddressAType": tn9300NetCheckAddressAType,
       "tn9300NetCheckAddressA": tn9300NetCheckAddressA,
       "tn9300NetCheckStateA": tn9300NetCheckStateA,
       "tn9300NetCheckAddressBType": tn9300NetCheckAddressBType,
       "tn9300NetCheckAddressB": tn9300NetCheckAddressB,
       "tn9300NetCheckStateB": tn9300NetCheckStateB,
       "tn9300CallsSwitching": tn9300CallsSwitching,
       "tn9300ConnectionsSwitching": tn9300ConnectionsSwitching,
       "tn9300MemoryUsage": tn9300MemoryUsage,
       "tn9300CpuUsage": tn9300CpuUsage,
       "tn9300DiskSpaceOk": tn9300DiskSpaceOk,
       "tn9300LicenseValidity": tn9300LicenseValidity,
       "tn9300SiteObjs": tn9300SiteObjs,
       "tn9300SiteTable": tn9300SiteTable,
       "tn9300SiteEntry": tn9300SiteEntry,
       "tn9300SiteNumber": tn9300SiteNumber,
       "tn9300SiteName": tn9300SiteName,
       "tn9300SiteSyscode": tn9300SiteSyscode,
       "tn9300SiteEnabled": tn9300SiteEnabled,
       "tn9300SiteOk": tn9300SiteOk,
       "tn9300SiteAutoQueueDepth": tn9300SiteAutoQueueDepth,
       "tn9300SiteQueueDepth": tn9300SiteQueueDepth,
       "tn9300SiteZone": tn9300SiteZone,
       "tn9300SiteExtraWaitSlots": tn9300SiteExtraWaitSlots,
       "tn9300SiteCCReassignTimeout": tn9300SiteCCReassignTimeout,
       "tn9300SiteTCRotation": tn9300SiteTCRotation,
       "tn9300SiteRxActivityTimeout": tn9300SiteRxActivityTimeout,
       "tn9300SiteRxInactiveTimeout": tn9300SiteRxInactiveTimeout,
       "tn9300SiteFramelength": tn9300SiteFramelength,
       "tn9300SiteMinFramelength": tn9300SiteMinFramelength,
       "tn9300SiteMaxFramelength": tn9300SiteMaxFramelength,
       "tn9300SiteDualCC": tn9300SiteDualCC,
       "tn9300SiteOpenMuteTimeout": tn9300SiteOpenMuteTimeout,
       "tn9300SiteManAdjSiteRF": tn9300SiteManAdjSiteRF,
       "tn9300SiteManAdjSiteSyscode": tn9300SiteManAdjSiteSyscode,
       "tn9300SiteNChannels": tn9300SiteNChannels,
       "tn9300SiteNControlChannels": tn9300SiteNControlChannels,
       "tn9300SiteNTrafficChannels": tn9300SiteNTrafficChannels,
       "tn9300SiteNIdleChannels": tn9300SiteNIdleChannels,
       "tn9300SiteNDisabledChannels": tn9300SiteNDisabledChannels,
       "tn9300SiteNFailedChannels": tn9300SiteNFailedChannels,
       "tn9300SiteNOnAirCalls": tn9300SiteNOnAirCalls,
       "tn9300SiteNRingingCalls": tn9300SiteNRingingCalls,
       "tn9300SiteNQueuedCalls": tn9300SiteNQueuedCalls,
       "tn9300SiteTotalCalls": tn9300SiteTotalCalls,
       "tn9300SiteTotalChannelCalls": tn9300SiteTotalChannelCalls,
       "tn9300SiteTotalQueueTime": tn9300SiteTotalQueueTime,
       "tn9300SiteChannelTimeFailed": tn9300SiteChannelTimeFailed,
       "tn9300SiteChannelTimeTraffic": tn9300SiteChannelTimeTraffic,
       "tn9300SiteChannelTimeControl": tn9300SiteChannelTimeControl,
       "tn9300SiteChannelTimeIdle": tn9300SiteChannelTimeIdle,
       "tn9300SiteCallsQueuedUnder5": tn9300SiteCallsQueuedUnder5,
       "tn9300SiteCallsQueued5To10": tn9300SiteCallsQueued5To10,
       "tn9300SiteCallsQueued10To20": tn9300SiteCallsQueued10To20,
       "tn9300SiteCallsQueuedOver20": tn9300SiteCallsQueuedOver20,
       "tn9300SiteAlias": tn9300SiteAlias,
       "tn9300SiteControlChCountOk": tn9300SiteControlChCountOk,
       "tn9300SiteNAlternateChannels": tn9300SiteNAlternateChannels,
       "tn9300SiteChannelTimeAlternate": tn9300SiteChannelTimeAlternate,
       "tn9300ChannelTable": tn9300ChannelTable,
       "tn9300ChannelEntry": tn9300ChannelEntry,
       "tn9300ChannelNumber": tn9300ChannelNumber,
       "tn9300ChannelIpAddressType": tn9300ChannelIpAddressType,
       "tn9300ChannelIpAddress": tn9300ChannelIpAddress,
       "tn9300ChannelPort": tn9300ChannelPort,
       "tn9300ChannelRf": tn9300ChannelRf,
       "tn9300ChannelEnabled": tn9300ChannelEnabled,
       "tn9300ChannelControlAllowed": tn9300ChannelControlAllowed,
       "tn9300ChannelTrafficAllowed": tn9300ChannelTrafficAllowed,
       "tn9300ChannelInhibitIfJammed": tn9300ChannelInhibitIfJammed,
       "tn9300ChannelState": tn9300ChannelState,
       "tn9300ChannelJammed": tn9300ChannelJammed,
       "tn9300ChannelMinorAlarm": tn9300ChannelMinorAlarm,
       "tn9300ChannelMajorAlarm": tn9300ChannelMajorAlarm,
       "tn9300ChannelAParty": tn9300ChannelAParty,
       "tn9300ChannelBParty": tn9300ChannelBParty,
       "tn9300ChannelBspRxPackets": tn9300ChannelBspRxPackets,
       "tn9300ChannelBspTxPackets": tn9300ChannelBspTxPackets,
       "tn9300ChannelBspLostPackets": tn9300ChannelBspLostPackets,
       "tn9300ChannelRtpRxPackets": tn9300ChannelRtpRxPackets,
       "tn9300ChannelRtpTxPackets": tn9300ChannelRtpTxPackets,
       "tn9300ChannelRtpLostPackets": tn9300ChannelRtpLostPackets,
       "tn9300ChannelRtpRtt": tn9300ChannelRtpRtt,
       "tn9300ChannelRtpRttJitter": tn9300ChannelRtpRttJitter,
       "tn9300ChannelTimeFailed": tn9300ChannelTimeFailed,
       "tn9300ChannelTimeTraffic": tn9300ChannelTimeTraffic,
       "tn9300ChannelTimeControl": tn9300ChannelTimeControl,
       "tn9300ChannelTimeIdle": tn9300ChannelTimeIdle,
       "tn9300ChannelAlternateAllowed": tn9300ChannelAlternateAllowed,
       "tn9300ChannelTimeAlternate": tn9300ChannelTimeAlternate,
       "tn9300ChannelBaseStationNumber": tn9300ChannelBaseStationNumber,
       "tn9300AdjacentSiteTable": tn9300AdjacentSiteTable,
       "tn9300AdjacentSiteEntry": tn9300AdjacentSiteEntry,
       "tn9300AdjSiteSendOrder": tn9300AdjSiteSendOrder,
       "tn9300AdjSiteAlias": tn9300AdjSiteAlias,
       "tn9300AdjSiteSyscode1": tn9300AdjSiteSyscode1,
       "tn9300AdjSiteRF1": tn9300AdjSiteRF1,
       "tn9300AdjSiteSyscode2": tn9300AdjSiteSyscode2,
       "tn9300AdjSiteRF2": tn9300AdjSiteRF2,
       "tn9300SipLineObjs": tn9300SipLineObjs,
       "tn9300SipLineTable": tn9300SipLineTable,
       "tn9300SipLineEntry": tn9300SipLineEntry,
       "tn9300SipLineNumber": tn9300SipLineNumber,
       "tn9300SipLineName": tn9300SipLineName,
       "tn9300SipLineRegistrationType": tn9300SipLineRegistrationType,
       "tn9300SipLineUserName": tn9300SipLineUserName,
       "tn9300SipLineEnabled": tn9300SipLineEnabled,
       "tn9300SipLineSpchVotePri": tn9300SipLineSpchVotePri,
       "tn9300SipLineAisMultipartContents": tn9300SipLineAisMultipartContents,
       "tn9300SipLineAisMonitor": tn9300SipLineAisMonitor,
       "tn9300SipLineSipGroup": tn9300SipLineSipGroup,
       "tn9300SipLineInphoneTable": tn9300SipLineInphoneTable,
       "tn9300SipLineIncomingType": tn9300SipLineIncomingType,
       "tn9300SipLineProxyAddressType": tn9300SipLineProxyAddressType,
       "tn9300SipLineProxyAddress": tn9300SipLineProxyAddress,
       "tn9300SipLineIpAddressType": tn9300SipLineIpAddressType,
       "tn9300SipLineIpAddress": tn9300SipLineIpAddress,
       "tn9300SipLineState": tn9300SipLineState,
       "tn9300SipLineUptime": tn9300SipLineUptime,
       "tn9300SipLineConnects": tn9300SipLineConnects,
       "tn9300SipLineCalls": tn9300SipLineCalls,
       "tn9300DipLineObjs": tn9300DipLineObjs,
       "tn9300DipLineTable": tn9300DipLineTable,
       "tn9300DipLineEntry": tn9300DipLineEntry,
       "tn9300DipLineNumber": tn9300DipLineNumber,
       "tn9300DipLineName": tn9300DipLineName,
       "tn9300DipLineNgwIpAddrType": tn9300DipLineNgwIpAddrType,
       "tn9300DipLineNgwIpAddr": tn9300DipLineNgwIpAddr,
       "tn9300DipLineAddress": tn9300DipLineAddress,
       "tn9300DipLinePilotAddress": tn9300DipLinePilotAddress,
       "tn9300DipLineSpchVotePri": tn9300DipLineSpchVotePri,
       "tn9300DipLineState": tn9300DipLineState,
       "tn9300DipLineNgwLinkState": tn9300DipLineNgwLinkState,
       "tn9300DipLineAParty": tn9300DipLineAParty,
       "tn9300DipLineBParty": tn9300DipLineBParty,
       "tn9300DipLnClientIpAddrType": tn9300DipLnClientIpAddrType,
       "tn9300DipLnClientIpAddr": tn9300DipLnClientIpAddr,
       "tn9300DipLineClientUptime": tn9300DipLineClientUptime,
       "tn9300DipLineClientConnects": tn9300DipLineClientConnects,
       "tn9300DipLineNgpRxPackets": tn9300DipLineNgpRxPackets,
       "tn9300DipLineNgpTxPackets": tn9300DipLineNgpTxPackets,
       "tn9300DipLineNgpLostPackets": tn9300DipLineNgpLostPackets,
       "tn9300DipLineRtpRxPackets": tn9300DipLineRtpRxPackets,
       "tn9300DipLineRtpTxPackets": tn9300DipLineRtpTxPackets,
       "tn9300DipLineRtpLostPackets": tn9300DipLineRtpLostPackets,
       "tn9300DipLineRtpRtt": tn9300DipLineRtpRtt,
       "tn9300DipLineRtpJitter": tn9300DipLineRtpJitter,
       "tn9300Mpt1327Objs": tn9300Mpt1327Objs,
       "tn9300Mpt1327IpAddressType": tn9300Mpt1327IpAddressType,
       "tn9300Mpt1327IpAddress": tn9300Mpt1327IpAddress,
       "tn9300Mpt1327Port": tn9300Mpt1327Port,
       "tn9300Mpt1327State": tn9300Mpt1327State,
       "tn9300Mpt1327RxBytes": tn9300Mpt1327RxBytes,
       "tn9300Mpt1327TxBytes": tn9300Mpt1327TxBytes,
       "tn9300Mpt1327LinkErrors": tn9300Mpt1327LinkErrors,
       "tn9300Mpt1327Connections": tn9300Mpt1327Connections,
       "tn9300Mpt1327ChObjs": tn9300Mpt1327ChObjs,
       "tn9300Mpt1327ChTable": tn9300Mpt1327ChTable,
       "tn9300Mpt1327ChEntry": tn9300Mpt1327ChEntry,
       "tn9300Mpt1327ChNumber": tn9300Mpt1327ChNumber,
       "tn9300Mpt1327ChIpAddressType": tn9300Mpt1327ChIpAddressType,
       "tn9300Mpt1327ChIpAddress": tn9300Mpt1327ChIpAddress,
       "tn9300Mpt1327ChPort": tn9300Mpt1327ChPort,
       "tn9300Mpt1327ChState": tn9300Mpt1327ChState,
       "tn9300Mpt1327ChLinkState": tn9300Mpt1327ChLinkState,
       "tn9300Mpt1327ChAParty": tn9300Mpt1327ChAParty,
       "tn9300Mpt1327ChBParty": tn9300Mpt1327ChBParty,
       "tn9300Mpt1327ChNgpRxPackets": tn9300Mpt1327ChNgpRxPackets,
       "tn9300Mpt1327ChNgpTxPackets": tn9300Mpt1327ChNgpTxPackets,
       "tn9300Mpt1327ChNgpLostPackets": tn9300Mpt1327ChNgpLostPackets,
       "tn9300Mpt1327ChRtpRxPackets": tn9300Mpt1327ChRtpRxPackets,
       "tn9300Mpt1327ChRtpTxPackets": tn9300Mpt1327ChRtpTxPackets,
       "tn9300Mpt1327ChRtpLostPackets": tn9300Mpt1327ChRtpLostPackets,
       "tn9300Mpt1327ChRtpRtt": tn9300Mpt1327ChRtpRtt,
       "tn9300Mpt1327ChRtpJitter": tn9300Mpt1327ChRtpJitter,
       "tn9300RemoteNodeObjs": tn9300RemoteNodeObjs,
       "tn9300RemoteNodeTable": tn9300RemoteNodeTable,
       "tn9300RemoteNodeEntry": tn9300RemoteNodeEntry,
       "tn9300RemoteNodeNumber": tn9300RemoteNodeNumber,
       "tn9300RemoteNodeName": tn9300RemoteNodeName,
       "tn9300RemoteNodeIpAddrType": tn9300RemoteNodeIpAddrType,
       "tn9300RemoteNodeIpAddr": tn9300RemoteNodeIpAddr,
       "tn9300RemoteNodePriority": tn9300RemoteNodePriority,
       "tn9300RemoteNodeState": tn9300RemoteNodeState,
       "tn9300RemoteNodeCallSw": tn9300RemoteNodeCallSw,
       "tn9300RemoteNodeConnectSw": tn9300RemoteNodeConnectSw,
       "tn9300RemoteNodeSynced": tn9300RemoteNodeSynced,
       "tn9300MobileIpObjs": tn9300MobileIpObjs,
       "tn9300MipRegistered": tn9300MipRegistered,
       "tn9300MipFailing": tn9300MipFailing,
       "tn9300MipTimeouts": tn9300MipTimeouts,
       "tn9300MipRejections": tn9300MipRejections,
       "tn9300MipIcmpRxPackets": tn9300MipIcmpRxPackets,
       "tn9300MipIcmpTxPackets": tn9300MipIcmpTxPackets,
       "tn9300MipUdpRxPackets": tn9300MipUdpRxPackets,
       "tn9300MipUdpTxPackets": tn9300MipUdpTxPackets,
       "tn9300MipRxBytes": tn9300MipRxBytes,
       "tn9300MipTxBytes": tn9300MipTxBytes,
       "tn9300UnitObjs": tn9300UnitObjs,
       "tn9300UnitTable": tn9300UnitTable,
       "tn9300UnitEntry": tn9300UnitEntry,
       "tn9300UnitAddress": tn9300UnitAddress,
       "tn9300UnitAlias": tn9300UnitAlias,
       "tn9300UnitAuthentication": tn9300UnitAuthentication,
       "tn9300UnitStatusMessageId": tn9300UnitStatusMessageId,
       "tn9300NetworkGwObjs": tn9300NetworkGwObjs,
       "tn9300NetworkGwTable": tn9300NetworkGwTable,
       "tn9300NetworkGwEntry": tn9300NetworkGwEntry,
       "tn9300NetworkGwId": tn9300NetworkGwId,
       "tn9300NetworkGwConnOk": tn9300NetworkGwConnOk,
       "tn9300NetworkGwIpAddrType": tn9300NetworkGwIpAddrType,
       "tn9300NetworkGwIpAddr": tn9300NetworkGwIpAddr,
       "tn9300EventObjs": tn9300EventObjs,
       "tn9300EventSeverity": tn9300EventSeverity,
       "tn9300EventUnitAddress": tn9300EventUnitAddress,
       "tn9300EventBaseStationNumber": tn9300EventBaseStationNumber,
       "tn9300EventChannelNumber": tn9300EventChannelNumber,
       "tn9300EventNetworkGwId": tn9300EventNetworkGwId,
       "tn9300Events": tn9300Events,
       "tn9300EventsV2": tn9300EventsV2,
       "tn9300NodeActivationEvent": tn9300NodeActivationEvent,
       "tn9300SiteFailureEvent": tn9300SiteFailureEvent,
       "tn9300SiteOkEvent": tn9300SiteOkEvent,
       "tn9300ChannelMinorAlarmEvent": tn9300ChannelMinorAlarmEvent,
       "tn9300ChannelMajorAlarmEvent": tn9300ChannelMajorAlarmEvent,
       "tn9300ChannelFailureEvent": tn9300ChannelFailureEvent,
       "tn9300ChannelOkEvent": tn9300ChannelOkEvent,
       "tn9300ChannelJammedEvent": tn9300ChannelJammedEvent,
       "tn9300ChannelUnjammedEvent": tn9300ChannelUnjammedEvent,
       "tn9300SipLinkUpEvent": tn9300SipLinkUpEvent,
       "tn9300SipLinkDownEvent": tn9300SipLinkDownEvent,
       "tn9300DipLinkUpEvent": tn9300DipLinkUpEvent,
       "tn9300DipLinkDownEvent": tn9300DipLinkDownEvent,
       "tn9300ControlChannelEvent": tn9300ControlChannelEvent,
       "tn9300NetworkErrorEvent": tn9300NetworkErrorEvent,
       "tn9300RemoteNodeUpEvent": tn9300RemoteNodeUpEvent,
       "tn9300RemoteNodeDownEvent": tn9300RemoteNodeDownEvent,
       "tn9300LowDiskSpaceEvent": tn9300LowDiskSpaceEvent,
       "tn9300LicenseCheckFailedEvent": tn9300LicenseCheckFailedEvent,
       "tn9300NetworkGatewayUpEvent": tn9300NetworkGatewayUpEvent,
       "tn9300NetworkGatewayDownEvent": tn9300NetworkGatewayDownEvent,
       "tn9300NodeFailedEvent": tn9300NodeFailedEvent,
       "tn9300NetworkUpEvent": tn9300NetworkUpEvent,
       "tn9300AuthenticationOkEvent": tn9300AuthenticationOkEvent,
       "tn9300AuthenticationFailureEvent": tn9300AuthenticationFailureEvent,
       "tn9300UnitStatusMessageEvent": tn9300UnitStatusMessageEvent,
       "tn9300RemoteNodeSyncFailedEvent": tn9300RemoteNodeSyncFailedEvent,
       "tn9300RemoteNodeSyncOkEvent": tn9300RemoteNodeSyncOkEvent,
       "tn9300UnitDeregisteredBySystemEvent": tn9300UnitDeregisteredBySystemEvent,
       "tn9300NodeStateEvent": tn9300NodeStateEvent,
       "tn9300NodeIpNetworkStateEvent": tn9300NodeIpNetworkStateEvent,
       "tn9300NodeDiskSpaceEvent": tn9300NodeDiskSpaceEvent,
       "tn9300NodeLicenseEvent": tn9300NodeLicenseEvent,
       "tn9300SiteStateEvent": tn9300SiteStateEvent,
       "tn9300SiteControlChCountEvent": tn9300SiteControlChCountEvent,
       "tn9300BSMinorAlarmStateEvent": tn9300BSMinorAlarmStateEvent,
       "tn9300BSMajorAlarmStateEvent": tn9300BSMajorAlarmStateEvent,
       "tn9300BSStateEvent": tn9300BSStateEvent,
       "tn9300ChannelJammedStateEvent": tn9300ChannelJammedStateEvent,
       "tn9300ChannelStuckMuteEvent": tn9300ChannelStuckMuteEvent,
       "tn9300SipLinkStateEvent": tn9300SipLinkStateEvent,
       "tn9300DipLinkStateEvent": tn9300DipLinkStateEvent,
       "tn9300RemoteNodeStateEvent": tn9300RemoteNodeStateEvent,
       "tn9300RemoteNodeSyncEvent": tn9300RemoteNodeSyncEvent,
       "tn9300NetworkGwConnEvent": tn9300NetworkGwConnEvent,
       "tn9300UnitAuthenticationEvent": tn9300UnitAuthenticationEvent,
       "tn9300UnitStatusMsgEvent": tn9300UnitStatusMsgEvent,
       "tn9300UnitRegTimeoutEvent": tn9300UnitRegTimeoutEvent,
       "tn9300ObjectsForEvents": tn9300ObjectsForEvents,
       "tn9300CgmMIB": tn9300CgmMIB}
)
