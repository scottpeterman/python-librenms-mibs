# SNMP MIB module (UBQS-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-DHCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:15 2025
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
 TimeTicks) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeTicks")

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiDhcpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiDhcpMIBNotificationPrefix = _UbiDhcpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 0)
)
_UbiDhcpMIBNotifications_ObjectIdentity = ObjectIdentity
ubiDhcpMIBNotifications = _UbiDhcpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 0, 0)
)
_UbiDhcpServerMIBObjects_ObjectIdentity = ObjectIdentity
ubiDhcpServerMIBObjects = _UbiDhcpServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1)
)
_UbiDhcpStatisticsTable_Object = MibTable
ubiDhcpStatisticsTable = _UbiDhcpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ubiDhcpStatisticsTable.setStatus("current")
_UbiDhcpStatisticsEntry_Object = MibTableRow
ubiDhcpStatisticsEntry = _UbiDhcpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1)
)
ubiDhcpStatisticsEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "noIndex"),
)
if mibBuilder.loadTexts:
    ubiDhcpStatisticsEntry.setStatus("current")
_UbiDhcpCurPktMFMessage_Type = Unsigned32
_UbiDhcpCurPktMFMessage_Object = MibTableColumn
ubiDhcpCurPktMFMessage = _UbiDhcpCurPktMFMessage_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 1),
    _UbiDhcpCurPktMFMessage_Type()
)
ubiDhcpCurPktMFMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktMFMessage.setStatus("current")
_UbiDhcpCurPktBootReq_Type = Unsigned32
_UbiDhcpCurPktBootReq_Object = MibTableColumn
ubiDhcpCurPktBootReq = _UbiDhcpCurPktBootReq_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 2),
    _UbiDhcpCurPktBootReq_Type()
)
ubiDhcpCurPktBootReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktBootReq.setStatus("current")
_UbiDhcpCurPktDiscover_Type = Unsigned32
_UbiDhcpCurPktDiscover_Object = MibTableColumn
ubiDhcpCurPktDiscover = _UbiDhcpCurPktDiscover_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 3),
    _UbiDhcpCurPktDiscover_Type()
)
ubiDhcpCurPktDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktDiscover.setStatus("current")
_UbiDhcpCurPktReq_Type = Unsigned32
_UbiDhcpCurPktReq_Object = MibTableColumn
ubiDhcpCurPktReq = _UbiDhcpCurPktReq_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 4),
    _UbiDhcpCurPktReq_Type()
)
ubiDhcpCurPktReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktReq.setStatus("current")
_UbiDhcpCurPktDecline_Type = Unsigned32
_UbiDhcpCurPktDecline_Object = MibTableColumn
ubiDhcpCurPktDecline = _UbiDhcpCurPktDecline_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 5),
    _UbiDhcpCurPktDecline_Type()
)
ubiDhcpCurPktDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktDecline.setStatus("current")
_UbiDhcpCurPktRelease_Type = Unsigned32
_UbiDhcpCurPktRelease_Object = MibTableColumn
ubiDhcpCurPktRelease = _UbiDhcpCurPktRelease_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 6),
    _UbiDhcpCurPktRelease_Type()
)
ubiDhcpCurPktRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktRelease.setStatus("current")
_UbiDhcpCurPktInform_Type = Unsigned32
_UbiDhcpCurPktInform_Object = MibTableColumn
ubiDhcpCurPktInform = _UbiDhcpCurPktInform_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 7),
    _UbiDhcpCurPktInform_Type()
)
ubiDhcpCurPktInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktInform.setStatus("current")
_UbiDhcpCurPktEcho_Type = Unsigned32
_UbiDhcpCurPktEcho_Object = MibTableColumn
ubiDhcpCurPktEcho = _UbiDhcpCurPktEcho_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 8),
    _UbiDhcpCurPktEcho_Type()
)
ubiDhcpCurPktEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktEcho.setStatus("current")
_UbiDhcpCurPktReply_Type = Unsigned32
_UbiDhcpCurPktReply_Object = MibTableColumn
ubiDhcpCurPktReply = _UbiDhcpCurPktReply_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 9),
    _UbiDhcpCurPktReply_Type()
)
ubiDhcpCurPktReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktReply.setStatus("current")
_UbiDhcpCurPktOffer_Type = Unsigned32
_UbiDhcpCurPktOffer_Object = MibTableColumn
ubiDhcpCurPktOffer = _UbiDhcpCurPktOffer_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 10),
    _UbiDhcpCurPktOffer_Type()
)
ubiDhcpCurPktOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktOffer.setStatus("current")
_UbiDhcpCurPktAck_Type = Unsigned32
_UbiDhcpCurPktAck_Object = MibTableColumn
ubiDhcpCurPktAck = _UbiDhcpCurPktAck_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 11),
    _UbiDhcpCurPktAck_Type()
)
ubiDhcpCurPktAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktAck.setStatus("current")
_UbiDhcpCurPktNak_Type = Unsigned32
_UbiDhcpCurPktNak_Object = MibTableColumn
ubiDhcpCurPktNak = _UbiDhcpCurPktNak_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 1, 1, 12),
    _UbiDhcpCurPktNak_Type()
)
ubiDhcpCurPktNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpCurPktNak.setStatus("current")
_UbiDhcpServerPoolTable_Object = MibTable
ubiDhcpServerPoolTable = _UbiDhcpServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ubiDhcpServerPoolTable.setStatus("current")
_UbiDhcpServerPoolEntry_Object = MibTableRow
ubiDhcpServerPoolEntry = _UbiDhcpServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1)
)
ubiDhcpServerPoolEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerPoolName"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerPoolEntry.setStatus("current")
_UbiDhcpServerPoolName_Type = DisplayString
_UbiDhcpServerPoolName_Object = MibTableColumn
ubiDhcpServerPoolName = _UbiDhcpServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 1),
    _UbiDhcpServerPoolName_Type()
)
ubiDhcpServerPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolName.setStatus("current")
_UbiDhcpServerPoolSubnet_Type = IpAddress
_UbiDhcpServerPoolSubnet_Object = MibTableColumn
ubiDhcpServerPoolSubnet = _UbiDhcpServerPoolSubnet_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 2),
    _UbiDhcpServerPoolSubnet_Type()
)
ubiDhcpServerPoolSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSubnet.setStatus("current")
_UbiDhcpServerPoolSubnetMask_Type = IpAddress
_UbiDhcpServerPoolSubnetMask_Object = MibTableColumn
ubiDhcpServerPoolSubnetMask = _UbiDhcpServerPoolSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 3),
    _UbiDhcpServerPoolSubnetMask_Type()
)
ubiDhcpServerPoolSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSubnetMask.setStatus("current")
_UbiDhcpServerPoolSubnetFreeAddress_Type = Unsigned32
_UbiDhcpServerPoolSubnetFreeAddress_Object = MibTableColumn
ubiDhcpServerPoolSubnetFreeAddress = _UbiDhcpServerPoolSubnetFreeAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 4),
    _UbiDhcpServerPoolSubnetFreeAddress_Type()
)
ubiDhcpServerPoolSubnetFreeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSubnetFreeAddress.setStatus("current")
_UbiDhcpServerPoolSubnetTotalAddress_Type = Unsigned32
_UbiDhcpServerPoolSubnetTotalAddress_Object = MibTableColumn
ubiDhcpServerPoolSubnetTotalAddress = _UbiDhcpServerPoolSubnetTotalAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 5),
    _UbiDhcpServerPoolSubnetTotalAddress_Type()
)
ubiDhcpServerPoolSubnetTotalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSubnetTotalAddress.setStatus("current")
_UbiDhcpServerPoolSubnetInUse_Type = Gauge32
_UbiDhcpServerPoolSubnetInUse_Object = MibTableColumn
ubiDhcpServerPoolSubnetInUse = _UbiDhcpServerPoolSubnetInUse_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 6),
    _UbiDhcpServerPoolSubnetInUse_Type()
)
ubiDhcpServerPoolSubnetInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSubnetInUse.setStatus("current")
_UbiDhcpServerPoolSubnetGroup_Type = DisplayString
_UbiDhcpServerPoolSubnetGroup_Object = MibTableColumn
ubiDhcpServerPoolSubnetGroup = _UbiDhcpServerPoolSubnetGroup_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 7),
    _UbiDhcpServerPoolSubnetGroup_Type()
)
ubiDhcpServerPoolSubnetGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSubnetGroup.setStatus("current")


class _UbiDhcpServerPoolType_Type(Integer32):
    """Custom type ubiDhcpServerPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("network", 1),
          ("host", 2))
    )


_UbiDhcpServerPoolType_Type.__name__ = "Integer32"
_UbiDhcpServerPoolType_Object = MibTableColumn
ubiDhcpServerPoolType = _UbiDhcpServerPoolType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 8),
    _UbiDhcpServerPoolType_Type()
)
ubiDhcpServerPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolType.setStatus("current")
_UbiDhcpServerPoolDomainName_Type = OctetString
_UbiDhcpServerPoolDomainName_Object = MibTableColumn
ubiDhcpServerPoolDomainName = _UbiDhcpServerPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 9),
    _UbiDhcpServerPoolDomainName_Type()
)
ubiDhcpServerPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolDomainName.setStatus("current")


class _UbiDhcpServerPoolLeaseTimeMode_Type(Integer32):
    """Custom type ubiDhcpServerPoolLeaseTimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("infinite", 1),
          ("manual", 2))
    )


_UbiDhcpServerPoolLeaseTimeMode_Type.__name__ = "Integer32"
_UbiDhcpServerPoolLeaseTimeMode_Object = MibTableColumn
ubiDhcpServerPoolLeaseTimeMode = _UbiDhcpServerPoolLeaseTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 10),
    _UbiDhcpServerPoolLeaseTimeMode_Type()
)
ubiDhcpServerPoolLeaseTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolLeaseTimeMode.setStatus("current")


class _UbiDhcpServerPoolLeaseTimeDays_Type(Integer32):
    """Custom type ubiDhcpServerPoolLeaseTimeDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UbiDhcpServerPoolLeaseTimeDays_Type.__name__ = "Integer32"
_UbiDhcpServerPoolLeaseTimeDays_Object = MibTableColumn
ubiDhcpServerPoolLeaseTimeDays = _UbiDhcpServerPoolLeaseTimeDays_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 11),
    _UbiDhcpServerPoolLeaseTimeDays_Type()
)
ubiDhcpServerPoolLeaseTimeDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolLeaseTimeDays.setStatus("current")


class _UbiDhcpServerPoolLeaseTimeHours_Type(Integer32):
    """Custom type ubiDhcpServerPoolLeaseTimeHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_UbiDhcpServerPoolLeaseTimeHours_Type.__name__ = "Integer32"
_UbiDhcpServerPoolLeaseTimeHours_Object = MibTableColumn
ubiDhcpServerPoolLeaseTimeHours = _UbiDhcpServerPoolLeaseTimeHours_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 12),
    _UbiDhcpServerPoolLeaseTimeHours_Type()
)
ubiDhcpServerPoolLeaseTimeHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolLeaseTimeHours.setStatus("current")


class _UbiDhcpServerPoolLeaseTimeMinutes_Type(Integer32):
    """Custom type ubiDhcpServerPoolLeaseTimeMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_UbiDhcpServerPoolLeaseTimeMinutes_Type.__name__ = "Integer32"
_UbiDhcpServerPoolLeaseTimeMinutes_Object = MibTableColumn
ubiDhcpServerPoolLeaseTimeMinutes = _UbiDhcpServerPoolLeaseTimeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 13),
    _UbiDhcpServerPoolLeaseTimeMinutes_Type()
)
ubiDhcpServerPoolLeaseTimeMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolLeaseTimeMinutes.setStatus("current")


class _UbiDhcpServerPoolUsageThreshold_Type(Integer32):
    """Custom type ubiDhcpServerPoolUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbiDhcpServerPoolUsageThreshold_Type.__name__ = "Integer32"
_UbiDhcpServerPoolUsageThreshold_Object = MibTableColumn
ubiDhcpServerPoolUsageThreshold = _UbiDhcpServerPoolUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 14),
    _UbiDhcpServerPoolUsageThreshold_Type()
)
ubiDhcpServerPoolUsageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolUsageThreshold.setStatus("current")
_UbiDhcpServerDefaultRouterInfo_Type = IpAddress
_UbiDhcpServerDefaultRouterInfo_Object = MibTableColumn
ubiDhcpServerDefaultRouterInfo = _UbiDhcpServerDefaultRouterInfo_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 2, 1, 15),
    _UbiDhcpServerDefaultRouterInfo_Type()
)
ubiDhcpServerDefaultRouterInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerDefaultRouterInfo.setStatus("current")
_UbiDhcpServerRangeTable_Object = MibTable
ubiDhcpServerRangeTable = _UbiDhcpServerRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 3)
)
if mibBuilder.loadTexts:
    ubiDhcpServerRangeTable.setStatus("current")
_UbiDhcpServerRangeEntry_Object = MibTableRow
ubiDhcpServerRangeEntry = _UbiDhcpServerRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 3, 1)
)
ubiDhcpServerRangeEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerPoolIndex"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpRangeStart"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerRangeEntry.setStatus("current")
_UbiDhcpServerPoolIndex_Type = Integer32
_UbiDhcpServerPoolIndex_Object = MibTableColumn
ubiDhcpServerPoolIndex = _UbiDhcpServerPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 3, 1, 1),
    _UbiDhcpServerPoolIndex_Type()
)
ubiDhcpServerPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolIndex.setStatus("current")
_UbiDhcpServerRangeStart_Type = IpAddress
_UbiDhcpServerRangeStart_Object = MibTableColumn
ubiDhcpServerRangeStart = _UbiDhcpServerRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 3, 1, 2),
    _UbiDhcpServerRangeStart_Type()
)
ubiDhcpServerRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerRangeStart.setStatus("current")
_UbiDhcpServerRangeEnd_Type = IpAddress
_UbiDhcpServerRangeEnd_Object = MibTableColumn
ubiDhcpServerRangeEnd = _UbiDhcpServerRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 3, 1, 3),
    _UbiDhcpServerRangeEnd_Type()
)
ubiDhcpServerRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerRangeEnd.setStatus("current")
_UbiDhcpServerNetPoolRangeTable_Object = MibTable
ubiDhcpServerNetPoolRangeTable = _UbiDhcpServerNetPoolRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 4)
)
if mibBuilder.loadTexts:
    ubiDhcpServerNetPoolRangeTable.setStatus("current")
_UbiDhcpServerNetPoolRangeEntry_Object = MibTableRow
ubiDhcpServerNetPoolRangeEntry = _UbiDhcpServerNetPoolRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 4, 1)
)
ubiDhcpServerNetPoolRangeEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerNetPoolRangePoolIndex"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerNetPoolRangeStartIpAddr"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerNetPoolRangeEndIpAddr"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerNetPoolRangeEntry.setStatus("current")
_UbiDhcpServerNetPoolRangePoolIndex_Type = Integer32
_UbiDhcpServerNetPoolRangePoolIndex_Object = MibTableColumn
ubiDhcpServerNetPoolRangePoolIndex = _UbiDhcpServerNetPoolRangePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 4, 1, 1),
    _UbiDhcpServerNetPoolRangePoolIndex_Type()
)
ubiDhcpServerNetPoolRangePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerNetPoolRangePoolIndex.setStatus("current")
_UbiDhcpServerNetPoolRangeStartIpAddr_Type = IpAddress
_UbiDhcpServerNetPoolRangeStartIpAddr_Object = MibTableColumn
ubiDhcpServerNetPoolRangeStartIpAddr = _UbiDhcpServerNetPoolRangeStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 4, 1, 2),
    _UbiDhcpServerNetPoolRangeStartIpAddr_Type()
)
ubiDhcpServerNetPoolRangeStartIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerNetPoolRangeStartIpAddr.setStatus("current")
_UbiDhcpServerNetPoolRangeEndIpAddr_Type = IpAddress
_UbiDhcpServerNetPoolRangeEndIpAddr_Object = MibTableColumn
ubiDhcpServerNetPoolRangeEndIpAddr = _UbiDhcpServerNetPoolRangeEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 4, 1, 3),
    _UbiDhcpServerNetPoolRangeEndIpAddr_Type()
)
ubiDhcpServerNetPoolRangeEndIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerNetPoolRangeEndIpAddr.setStatus("current")
_UbiDhcpServerNetPoolRangeRowstatus_Type = RowStatus
_UbiDhcpServerNetPoolRangeRowstatus_Object = MibTableColumn
ubiDhcpServerNetPoolRangeRowstatus = _UbiDhcpServerNetPoolRangeRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 4, 1, 4),
    _UbiDhcpServerNetPoolRangeRowstatus_Type()
)
ubiDhcpServerNetPoolRangeRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiDhcpServerNetPoolRangeRowstatus.setStatus("current")
_UbiDhcpServerPoolRowTable_Object = MibTable
ubiDhcpServerPoolRowTable = _UbiDhcpServerPoolRowTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 5)
)
if mibBuilder.loadTexts:
    ubiDhcpServerPoolRowTable.setStatus("current")
_UbiDhcpServerPoolRowEntry_Object = MibTableRow
ubiDhcpServerPoolRowEntry = _UbiDhcpServerPoolRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 5, 1)
)
ubiDhcpServerPoolRowEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerPoolIndex"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerRangeStart"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerRangeEnd"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerPoolRowEntry.setStatus("current")
_UbiDhcpServerPoolRowStatus_Type = RowStatus
_UbiDhcpServerPoolRowStatus_Object = MibTableColumn
ubiDhcpServerPoolRowStatus = _UbiDhcpServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 5, 1, 1),
    _UbiDhcpServerPoolRowStatus_Type()
)
ubiDhcpServerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolRowStatus.setStatus("current")
_UbiDhcpServerFixedAddrTable_Object = MibTable
ubiDhcpServerFixedAddrTable = _UbiDhcpServerFixedAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 6)
)
if mibBuilder.loadTexts:
    ubiDhcpServerFixedAddrTable.setStatus("current")
_UbiDhcpServerFixedAddrEntry_Object = MibTableRow
ubiDhcpServerFixedAddrEntry = _UbiDhcpServerFixedAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 6, 1)
)
ubiDhcpServerFixedAddrEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerFixedAddrHostPoolName"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerFixedAddrIp"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerFixedAddrNetmask"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerFixedAddrEntry.setStatus("current")


class _UbiDhcpServerFixedAddrHostPoolName_Type(DisplayString):
    """Custom type ubiDhcpServerFixedAddrHostPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UbiDhcpServerFixedAddrHostPoolName_Type.__name__ = "DisplayString"
_UbiDhcpServerFixedAddrHostPoolName_Object = MibTableColumn
ubiDhcpServerFixedAddrHostPoolName = _UbiDhcpServerFixedAddrHostPoolName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 6, 1, 1),
    _UbiDhcpServerFixedAddrHostPoolName_Type()
)
ubiDhcpServerFixedAddrHostPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerFixedAddrHostPoolName.setStatus("current")
_UbiDhcpServerFixedAddrMac_Type = MacAddress
_UbiDhcpServerFixedAddrMac_Object = MibTableColumn
ubiDhcpServerFixedAddrMac = _UbiDhcpServerFixedAddrMac_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 6, 1, 2),
    _UbiDhcpServerFixedAddrMac_Type()
)
ubiDhcpServerFixedAddrMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerFixedAddrMac.setStatus("current")
_UbiDhcpServerFixedAddrIp_Type = IpAddress
_UbiDhcpServerFixedAddrIp_Object = MibTableColumn
ubiDhcpServerFixedAddrIp = _UbiDhcpServerFixedAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 6, 1, 3),
    _UbiDhcpServerFixedAddrIp_Type()
)
ubiDhcpServerFixedAddrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerFixedAddrIp.setStatus("current")
_UbiDhcpServerFixedAddrNetmask_Type = IpAddress
_UbiDhcpServerFixedAddrNetmask_Object = MibTableColumn
ubiDhcpServerFixedAddrNetmask = _UbiDhcpServerFixedAddrNetmask_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 6, 1, 4),
    _UbiDhcpServerFixedAddrNetmask_Type()
)
ubiDhcpServerFixedAddrNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerFixedAddrNetmask.setStatus("current")
_UbiDhcpServerFixedAddrRowStatus_Type = RowStatus
_UbiDhcpServerFixedAddrRowStatus_Object = MibTableColumn
ubiDhcpServerFixedAddrRowStatus = _UbiDhcpServerFixedAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 6, 1, 5),
    _UbiDhcpServerFixedAddrRowStatus_Type()
)
ubiDhcpServerFixedAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiDhcpServerFixedAddrRowStatus.setStatus("current")
_UbiDhcpServerDnsTable_Object = MibTable
ubiDhcpServerDnsTable = _UbiDhcpServerDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 7)
)
if mibBuilder.loadTexts:
    ubiDhcpServerDnsTable.setStatus("current")
_UbiDhcpServerDnsEntry_Object = MibTableRow
ubiDhcpServerDnsEntry = _UbiDhcpServerDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 7, 1)
)
ubiDhcpServerDnsEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerDnsPoolIndex"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerDnsServerAddr"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerDnsEntry.setStatus("current")
_UbiDhcpServerDnsPoolIndex_Type = Integer32
_UbiDhcpServerDnsPoolIndex_Object = MibTableColumn
ubiDhcpServerDnsPoolIndex = _UbiDhcpServerDnsPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 7, 1, 1),
    _UbiDhcpServerDnsPoolIndex_Type()
)
ubiDhcpServerDnsPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerDnsPoolIndex.setStatus("current")
_UbiDhcpServerDnsServerAddr_Type = IpAddress
_UbiDhcpServerDnsServerAddr_Object = MibTableColumn
ubiDhcpServerDnsServerAddr = _UbiDhcpServerDnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 7, 1, 2),
    _UbiDhcpServerDnsServerAddr_Type()
)
ubiDhcpServerDnsServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerDnsServerAddr.setStatus("current")
_UbiDhcpServerDnsRowStatus_Type = RowStatus
_UbiDhcpServerDnsRowStatus_Object = MibTableColumn
ubiDhcpServerDnsRowStatus = _UbiDhcpServerDnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 7, 1, 3),
    _UbiDhcpServerDnsRowStatus_Type()
)
ubiDhcpServerDnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiDhcpServerDnsRowStatus.setStatus("current")
_UbiDhcpServerBindingTable_Object = MibTable
ubiDhcpServerBindingTable = _UbiDhcpServerBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 8)
)
if mibBuilder.loadTexts:
    ubiDhcpServerBindingTable.setStatus("current")
_UbiDhcpServerBindingEntry_Object = MibTableRow
ubiDhcpServerBindingEntry = _UbiDhcpServerBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 8, 1)
)
ubiDhcpServerBindingEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerBindingIndex"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerBindingEntry.setStatus("current")
_UbiDhcpServerBindingIndex_Type = Integer32
_UbiDhcpServerBindingIndex_Object = MibTableColumn
ubiDhcpServerBindingIndex = _UbiDhcpServerBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 8, 1, 1),
    _UbiDhcpServerBindingIndex_Type()
)
ubiDhcpServerBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerBindingIndex.setStatus("current")
_UbiDhcpServerBindingIpAddr_Type = IpAddress
_UbiDhcpServerBindingIpAddr_Object = MibTableColumn
ubiDhcpServerBindingIpAddr = _UbiDhcpServerBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 8, 1, 2),
    _UbiDhcpServerBindingIpAddr_Type()
)
ubiDhcpServerBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerBindingIpAddr.setStatus("current")
_UbiDhcpServerBindingMacAddr_Type = MacAddress
_UbiDhcpServerBindingMacAddr_Object = MibTableColumn
ubiDhcpServerBindingMacAddr = _UbiDhcpServerBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 8, 1, 3),
    _UbiDhcpServerBindingMacAddr_Type()
)
ubiDhcpServerBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerBindingMacAddr.setStatus("current")
_UbiDhspServerBindingLeaseExpiration_Type = OctetString
_UbiDhspServerBindingLeaseExpiration_Object = MibTableColumn
ubiDhspServerBindingLeaseExpiration = _UbiDhspServerBindingLeaseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 8, 1, 4),
    _UbiDhspServerBindingLeaseExpiration_Type()
)
ubiDhspServerBindingLeaseExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhspServerBindingLeaseExpiration.setStatus("current")


class _UbiDhcpServerBindingType_Type(Integer32):
    """Custom type ubiDhcpServerBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_UbiDhcpServerBindingType_Type.__name__ = "Integer32"
_UbiDhcpServerBindingType_Object = MibTableColumn
ubiDhcpServerBindingType = _UbiDhcpServerBindingType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 8, 1, 5),
    _UbiDhcpServerBindingType_Type()
)
ubiDhcpServerBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerBindingType.setStatus("current")
_UbiDhcpServerPoolSingleRangeTable_Object = MibTable
ubiDhcpServerPoolSingleRangeTable = _UbiDhcpServerPoolSingleRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 9)
)
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSingleRangeTable.setStatus("current")
_UbiDhcpServerPoolSingleRangeEntry_Object = MibTableRow
ubiDhcpServerPoolSingleRangeEntry = _UbiDhcpServerPoolSingleRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 9, 1)
)
ubiDhcpServerPoolSingleRangeEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerPoolSingleRangePoolIndex"),
    (0, "UBQS-DHCP-MIB", "ubiDhcpServerPoolSingleRangeIpAddr"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSingleRangeEntry.setStatus("current")
_UbiDhcpServerPoolSingleRangePoolIndex_Type = Integer32
_UbiDhcpServerPoolSingleRangePoolIndex_Object = MibTableColumn
ubiDhcpServerPoolSingleRangePoolIndex = _UbiDhcpServerPoolSingleRangePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 9, 1, 1),
    _UbiDhcpServerPoolSingleRangePoolIndex_Type()
)
ubiDhcpServerPoolSingleRangePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSingleRangePoolIndex.setStatus("current")
_UbiDhcpServerPoolSingleRangeIpAddr_Type = IpAddress
_UbiDhcpServerPoolSingleRangeIpAddr_Object = MibTableColumn
ubiDhcpServerPoolSingleRangeIpAddr = _UbiDhcpServerPoolSingleRangeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 9, 1, 2),
    _UbiDhcpServerPoolSingleRangeIpAddr_Type()
)
ubiDhcpServerPoolSingleRangeIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSingleRangeIpAddr.setStatus("current")
_UbiDhcpServerPoolSingleRangeRowstatus_Type = RowStatus
_UbiDhcpServerPoolSingleRangeRowstatus_Object = MibTableColumn
ubiDhcpServerPoolSingleRangeRowstatus = _UbiDhcpServerPoolSingleRangeRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 9, 1, 3),
    _UbiDhcpServerPoolSingleRangeRowstatus_Type()
)
ubiDhcpServerPoolSingleRangeRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiDhcpServerPoolSingleRangeRowstatus.setStatus("current")
_UbiDhcpServerInfoTable_Object = MibTable
ubiDhcpServerInfoTable = _UbiDhcpServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 10)
)
if mibBuilder.loadTexts:
    ubiDhcpServerInfoTable.setStatus("current")
_UbiDhcpServerInfoEntry_Object = MibTableRow
ubiDhcpServerInfoEntry = _UbiDhcpServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 10, 1)
)
ubiDhcpServerInfoEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "noIndex"),
)
if mibBuilder.loadTexts:
    ubiDhcpServerInfoEntry.setStatus("current")


class _UbiDhcpServerAdminStatus_Type(Integer32):
    """Custom type ubiDhcpServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_UbiDhcpServerAdminStatus_Type.__name__ = "Integer32"
_UbiDhcpServerAdminStatus_Object = MibTableColumn
ubiDhcpServerAdminStatus = _UbiDhcpServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 10, 1, 1),
    _UbiDhcpServerAdminStatus_Type()
)
ubiDhcpServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpServerAdminStatus.setStatus("current")
_UbiDhcpLeaseTimeMode_ObjectIdentity = ObjectIdentity
ubiDhcpLeaseTimeMode = _UbiDhcpLeaseTimeMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 11)
)


class _UbiDhcpLeaseTimeModeDays_Type(Integer32):
    """Custom type ubiDhcpLeaseTimeModeDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_UbiDhcpLeaseTimeModeDays_Type.__name__ = "Integer32"
_UbiDhcpLeaseTimeModeDays_Object = MibScalar
ubiDhcpLeaseTimeModeDays = _UbiDhcpLeaseTimeModeDays_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 11, 1),
    _UbiDhcpLeaseTimeModeDays_Type()
)
ubiDhcpLeaseTimeModeDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpLeaseTimeModeDays.setStatus("current")


class _UbiDhcpLeaseTimeModeHours_Type(Integer32):
    """Custom type ubiDhcpLeaseTimeModeHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_UbiDhcpLeaseTimeModeHours_Type.__name__ = "Integer32"
_UbiDhcpLeaseTimeModeHours_Object = MibScalar
ubiDhcpLeaseTimeModeHours = _UbiDhcpLeaseTimeModeHours_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 11, 2),
    _UbiDhcpLeaseTimeModeHours_Type()
)
ubiDhcpLeaseTimeModeHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpLeaseTimeModeHours.setStatus("current")


class _UbiDhcpLeaseTimeModeMinutes_Type(Integer32):
    """Custom type ubiDhcpLeaseTimeModeMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_UbiDhcpLeaseTimeModeMinutes_Type.__name__ = "Integer32"
_UbiDhcpLeaseTimeModeMinutes_Object = MibScalar
ubiDhcpLeaseTimeModeMinutes = _UbiDhcpLeaseTimeModeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 11, 3),
    _UbiDhcpLeaseTimeModeMinutes_Type()
)
ubiDhcpLeaseTimeModeMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpLeaseTimeModeMinutes.setStatus("current")


class _UbiDhcpLeaseTimeModeStatus_Type(Integer32):
    """Custom type ubiDhcpLeaseTimeModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLease", 0),
          ("infinite", 1),
          ("manual", 2))
    )


_UbiDhcpLeaseTimeModeStatus_Type.__name__ = "Integer32"
_UbiDhcpLeaseTimeModeStatus_Object = MibScalar
ubiDhcpLeaseTimeModeStatus = _UbiDhcpLeaseTimeModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 1, 11, 4),
    _UbiDhcpLeaseTimeModeStatus_Type()
)
ubiDhcpLeaseTimeModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpLeaseTimeModeStatus.setStatus("current")
_UbiDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
ubiDhcpRelayMIBObjects = _UbiDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2)
)
_UbiDhcpRelayInfoTable_Object = MibTable
ubiDhcpRelayInfoTable = _UbiDhcpRelayInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ubiDhcpRelayInfoTable.setStatus("current")
_UbiDhcpRelayInfoEntry_Object = MibTableRow
ubiDhcpRelayInfoEntry = _UbiDhcpRelayInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 1, 1)
)
ubiDhcpRelayInfoEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "noIndex"),
)
if mibBuilder.loadTexts:
    ubiDhcpRelayInfoEntry.setStatus("current")


class _UbiDhcpRelayAdminStatus_Type(Integer32):
    """Custom type ubiDhcpRelayAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_UbiDhcpRelayAdminStatus_Type.__name__ = "Integer32"
_UbiDhcpRelayAdminStatus_Object = MibTableColumn
ubiDhcpRelayAdminStatus = _UbiDhcpRelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 1, 1, 1),
    _UbiDhcpRelayAdminStatus_Type()
)
ubiDhcpRelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpRelayAdminStatus.setStatus("current")


class _UbiDhcpRelayOption82Status_Type(Integer32):
    """Custom type ubiDhcpRelayOption82Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiDhcpRelayOption82Status_Type.__name__ = "Integer32"
_UbiDhcpRelayOption82Status_Object = MibTableColumn
ubiDhcpRelayOption82Status = _UbiDhcpRelayOption82Status_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 1, 1, 2),
    _UbiDhcpRelayOption82Status_Type()
)
ubiDhcpRelayOption82Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpRelayOption82Status.setStatus("current")


class _UbiDhcpRelayOption82Policy_Type(Integer32):
    """Custom type ubiDhcpRelayOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("keep", 1),
          ("replace", 2))
    )


_UbiDhcpRelayOption82Policy_Type.__name__ = "Integer32"
_UbiDhcpRelayOption82Policy_Object = MibTableColumn
ubiDhcpRelayOption82Policy = _UbiDhcpRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 1, 1, 3),
    _UbiDhcpRelayOption82Policy_Type()
)
ubiDhcpRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpRelayOption82Policy.setStatus("current")


class _UbiDhcpRelayBindingListDisplayOption_Type(Integer32):
    """Custom type ubiDhcpRelayBindingListDisplayOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiDhcpRelayBindingListDisplayOption_Type.__name__ = "Integer32"
_UbiDhcpRelayBindingListDisplayOption_Object = MibTableColumn
ubiDhcpRelayBindingListDisplayOption = _UbiDhcpRelayBindingListDisplayOption_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 1, 1, 4),
    _UbiDhcpRelayBindingListDisplayOption_Type()
)
ubiDhcpRelayBindingListDisplayOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpRelayBindingListDisplayOption.setStatus("current")


class _UbiDhcpRelayVerifyMAC_Type(Integer32):
    """Custom type ubiDhcpRelayVerifyMAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiDhcpRelayVerifyMAC_Type.__name__ = "Integer32"
_UbiDhcpRelayVerifyMAC_Object = MibTableColumn
ubiDhcpRelayVerifyMAC = _UbiDhcpRelayVerifyMAC_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 1, 1, 5),
    _UbiDhcpRelayVerifyMAC_Type()
)
ubiDhcpRelayVerifyMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpRelayVerifyMAC.setStatus("current")
_UbiDhcpRelayServerIPTable_Object = MibTable
ubiDhcpRelayServerIPTable = _UbiDhcpRelayServerIPTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 2)
)
if mibBuilder.loadTexts:
    ubiDhcpRelayServerIPTable.setStatus("current")
_UbiDhcpRelayServerIPEntry_Object = MibTableRow
ubiDhcpRelayServerIPEntry = _UbiDhcpRelayServerIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 2, 1)
)
ubiDhcpRelayServerIPEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpRelayServerIP"),
)
if mibBuilder.loadTexts:
    ubiDhcpRelayServerIPEntry.setStatus("current")
_UbiDhcpRelayServerIP_Type = IpAddress
_UbiDhcpRelayServerIP_Object = MibTableColumn
ubiDhcpRelayServerIP = _UbiDhcpRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 2, 1, 1),
    _UbiDhcpRelayServerIP_Type()
)
ubiDhcpRelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpRelayServerIP.setStatus("current")
_UbiDhcpRelayServerIPRowStatus_Type = RowStatus
_UbiDhcpRelayServerIPRowStatus_Object = MibTableColumn
ubiDhcpRelayServerIPRowStatus = _UbiDhcpRelayServerIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 2, 1, 2),
    _UbiDhcpRelayServerIPRowStatus_Type()
)
ubiDhcpRelayServerIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiDhcpRelayServerIPRowStatus.setStatus("current")
_UbiDhcpRelayStatistics_ObjectIdentity = ObjectIdentity
ubiDhcpRelayStatistics = _UbiDhcpRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 3)
)
_UbiDhcpRelayCurPktDiscover_Type = Unsigned32
_UbiDhcpRelayCurPktDiscover_Object = MibScalar
ubiDhcpRelayCurPktDiscover = _UbiDhcpRelayCurPktDiscover_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 3, 3),
    _UbiDhcpRelayCurPktDiscover_Type()
)
ubiDhcpRelayCurPktDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpRelayCurPktDiscover.setStatus("current")
_UbiDhcpRelayCurPktReq_Type = Unsigned32
_UbiDhcpRelayCurPktReq_Object = MibScalar
ubiDhcpRelayCurPktReq = _UbiDhcpRelayCurPktReq_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 3, 4),
    _UbiDhcpRelayCurPktReq_Type()
)
ubiDhcpRelayCurPktReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpRelayCurPktReq.setStatus("current")
_UbiDhcpRelayCurPktOffer_Type = Unsigned32
_UbiDhcpRelayCurPktOffer_Object = MibScalar
ubiDhcpRelayCurPktOffer = _UbiDhcpRelayCurPktOffer_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 3, 10),
    _UbiDhcpRelayCurPktOffer_Type()
)
ubiDhcpRelayCurPktOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpRelayCurPktOffer.setStatus("current")
_UbiDhcpRelayCurPktAck_Type = Unsigned32
_UbiDhcpRelayCurPktAck_Object = MibScalar
ubiDhcpRelayCurPktAck = _UbiDhcpRelayCurPktAck_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 2, 3, 11),
    _UbiDhcpRelayCurPktAck_Type()
)
ubiDhcpRelayCurPktAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpRelayCurPktAck.setStatus("current")
_UbiDhcpSnoopMIBObjects_ObjectIdentity = ObjectIdentity
ubiDhcpSnoopMIBObjects = _UbiDhcpSnoopMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3)
)
_UbiDhcpSnoopInfoTable_Object = MibTable
ubiDhcpSnoopInfoTable = _UbiDhcpSnoopInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1)
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopInfoTable.setStatus("current")
_UbiDhcpSnoopInfoEntry_Object = MibTableRow
ubiDhcpSnoopInfoEntry = _UbiDhcpSnoopInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1)
)
ubiDhcpSnoopInfoEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "noIndex"),
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopInfoEntry.setStatus("current")


class _UbiDhcpSnoopAdminStatus_Type(Integer32):
    """Custom type ubiDhcpSnoopAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_UbiDhcpSnoopAdminStatus_Type.__name__ = "Integer32"
_UbiDhcpSnoopAdminStatus_Object = MibTableColumn
ubiDhcpSnoopAdminStatus = _UbiDhcpSnoopAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 1),
    _UbiDhcpSnoopAdminStatus_Type()
)
ubiDhcpSnoopAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopAdminStatus.setStatus("current")


class _UbiDhcpSnoopLeaseTimeExtention_Type(Integer32):
    """Custom type ubiDhcpSnoopLeaseTimeExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_UbiDhcpSnoopLeaseTimeExtention_Type.__name__ = "Integer32"
_UbiDhcpSnoopLeaseTimeExtention_Object = MibTableColumn
ubiDhcpSnoopLeaseTimeExtention = _UbiDhcpSnoopLeaseTimeExtention_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 2),
    _UbiDhcpSnoopLeaseTimeExtention_Type()
)
ubiDhcpSnoopLeaseTimeExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopLeaseTimeExtention.setStatus("current")


class _UbiDhcpSnoopBlockLogClear_Type(Integer32):
    """Custom type ubiDhcpSnoopBlockLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_UbiDhcpSnoopBlockLogClear_Type.__name__ = "Integer32"
_UbiDhcpSnoopBlockLogClear_Object = MibTableColumn
ubiDhcpSnoopBlockLogClear = _UbiDhcpSnoopBlockLogClear_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 3),
    _UbiDhcpSnoopBlockLogClear_Type()
)
ubiDhcpSnoopBlockLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBlockLogClear.setStatus("current")


class _UbiDhcpSnoopOption82Status_Type(Integer32):
    """Custom type ubiDhcpSnoopOption82Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiDhcpSnoopOption82Status_Type.__name__ = "Integer32"
_UbiDhcpSnoopOption82Status_Object = MibTableColumn
ubiDhcpSnoopOption82Status = _UbiDhcpSnoopOption82Status_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 4),
    _UbiDhcpSnoopOption82Status_Type()
)
ubiDhcpSnoopOption82Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopOption82Status.setStatus("current")


class _UbiDhcpSnoopOption82Policy_Type(Integer32):
    """Custom type ubiDhcpSnoopOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("keep", 1),
          ("replace", 2))
    )


_UbiDhcpSnoopOption82Policy_Type.__name__ = "Integer32"
_UbiDhcpSnoopOption82Policy_Object = MibTableColumn
ubiDhcpSnoopOption82Policy = _UbiDhcpSnoopOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 5),
    _UbiDhcpSnoopOption82Policy_Type()
)
ubiDhcpSnoopOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopOption82Policy.setStatus("current")


class _UbiDhcpSnoopVerifyMAC_Type(Integer32):
    """Custom type ubiDhcpSnoopVerifyMAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiDhcpSnoopVerifyMAC_Type.__name__ = "Integer32"
_UbiDhcpSnoopVerifyMAC_Object = MibTableColumn
ubiDhcpSnoopVerifyMAC = _UbiDhcpSnoopVerifyMAC_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 6),
    _UbiDhcpSnoopVerifyMAC_Type()
)
ubiDhcpSnoopVerifyMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopVerifyMAC.setStatus("current")
_UbiDhcpSnoopBindingCount_Type = Integer32
_UbiDhcpSnoopBindingCount_Object = MibTableColumn
ubiDhcpSnoopBindingCount = _UbiDhcpSnoopBindingCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 7),
    _UbiDhcpSnoopBindingCount_Type()
)
ubiDhcpSnoopBindingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingCount.setStatus("current")
_UbiDhcpSnoopInvalidCount_Type = Integer32
_UbiDhcpSnoopInvalidCount_Object = MibTableColumn
ubiDhcpSnoopInvalidCount = _UbiDhcpSnoopInvalidCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 1, 1, 8),
    _UbiDhcpSnoopInvalidCount_Type()
)
ubiDhcpSnoopInvalidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopInvalidCount.setStatus("current")
_UbiDhcpSnoopVlanTable_Object = MibTable
ubiDhcpSnoopVlanTable = _UbiDhcpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 2)
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopVlanTable.setStatus("current")
_UbiDhcpSnoopVlanEntry_Object = MibTableRow
ubiDhcpSnoopVlanEntry = _UbiDhcpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 2, 1)
)
ubiDhcpSnoopVlanEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiVlanId"),
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopVlanEntry.setStatus("current")
_UbiDhcpSnoopVlanIfName_Type = DisplayString
_UbiDhcpSnoopVlanIfName_Object = MibTableColumn
ubiDhcpSnoopVlanIfName = _UbiDhcpSnoopVlanIfName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 2, 1, 1),
    _UbiDhcpSnoopVlanIfName_Type()
)
ubiDhcpSnoopVlanIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopVlanIfName.setStatus("current")
_UbiDhcpSnoopVlanRowStatus_Type = RowStatus
_UbiDhcpSnoopVlanRowStatus_Object = MibTableColumn
ubiDhcpSnoopVlanRowStatus = _UbiDhcpSnoopVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 2, 1, 2),
    _UbiDhcpSnoopVlanRowStatus_Type()
)
ubiDhcpSnoopVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiDhcpSnoopVlanRowStatus.setStatus("current")
_UbiDhcpSnoopBindingTable_Object = MibTable
ubiDhcpSnoopBindingTable = _UbiDhcpSnoopBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3)
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingTable.setStatus("current")
_UbiDhcpSnoopBindingEntry_Object = MibTableRow
ubiDhcpSnoopBindingEntry = _UbiDhcpSnoopBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1)
)
ubiDhcpSnoopBindingEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiDhcpSnoopBindingIndex"),
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingEntry.setStatus("current")
_UbiDhcpSnoopBindingIndex_Type = Integer32
_UbiDhcpSnoopBindingIndex_Object = MibTableColumn
ubiDhcpSnoopBindingIndex = _UbiDhcpSnoopBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 1),
    _UbiDhcpSnoopBindingIndex_Type()
)
ubiDhcpSnoopBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingIndex.setStatus("current")
_UbiDhcpSnoopBindingMacAddr_Type = MacAddress
_UbiDhcpSnoopBindingMacAddr_Object = MibTableColumn
ubiDhcpSnoopBindingMacAddr = _UbiDhcpSnoopBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 2),
    _UbiDhcpSnoopBindingMacAddr_Type()
)
ubiDhcpSnoopBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingMacAddr.setStatus("current")
_UbiDhcpSnoopBindingIpAddr_Type = IpAddress
_UbiDhcpSnoopBindingIpAddr_Object = MibTableColumn
ubiDhcpSnoopBindingIpAddr = _UbiDhcpSnoopBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 3),
    _UbiDhcpSnoopBindingIpAddr_Type()
)
ubiDhcpSnoopBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingIpAddr.setStatus("current")
_UbiDhcpSnoopBindingState_Type = DisplayString
_UbiDhcpSnoopBindingState_Object = MibTableColumn
ubiDhcpSnoopBindingState = _UbiDhcpSnoopBindingState_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 4),
    _UbiDhcpSnoopBindingState_Type()
)
ubiDhcpSnoopBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingState.setStatus("current")
_UbiDhcpSnoopBindingVlanName_Type = DisplayString
_UbiDhcpSnoopBindingVlanName_Object = MibTableColumn
ubiDhcpSnoopBindingVlanName = _UbiDhcpSnoopBindingVlanName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 5),
    _UbiDhcpSnoopBindingVlanName_Type()
)
ubiDhcpSnoopBindingVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingVlanName.setStatus("current")
_UbiDhcpSnoopBindingPortName_Type = DisplayString
_UbiDhcpSnoopBindingPortName_Object = MibTableColumn
ubiDhcpSnoopBindingPortName = _UbiDhcpSnoopBindingPortName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 6),
    _UbiDhcpSnoopBindingPortName_Type()
)
ubiDhcpSnoopBindingPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingPortName.setStatus("current")


class _UbiDhcpSnoopBindingUpdate_Type(Integer32):
    """Custom type ubiDhcpSnoopBindingUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_UbiDhcpSnoopBindingUpdate_Type.__name__ = "Integer32"
_UbiDhcpSnoopBindingUpdate_Object = MibTableColumn
ubiDhcpSnoopBindingUpdate = _UbiDhcpSnoopBindingUpdate_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 7),
    _UbiDhcpSnoopBindingUpdate_Type()
)
ubiDhcpSnoopBindingUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingUpdate.setStatus("current")
_UbiDhcpSnoopBindingLeaseTime_Type = Unsigned32
_UbiDhcpSnoopBindingLeaseTime_Object = MibTableColumn
ubiDhcpSnoopBindingLeaseTime = _UbiDhcpSnoopBindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 3, 1, 8),
    _UbiDhcpSnoopBindingLeaseTime_Type()
)
ubiDhcpSnoopBindingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiDhcpSnoopBindingLeaseTime.setStatus("current")
_UbiDhcpSnoopIfTable_Object = MibTable
ubiDhcpSnoopIfTable = _UbiDhcpSnoopIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 4)
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopIfTable.setStatus("current")
_UbiDhcpSnoopIfEntry_Object = MibTableRow
ubiDhcpSnoopIfEntry = _UbiDhcpSnoopIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 4, 1)
)
ubiDhcpSnoopIfEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ubiDhcpSnoopIfEntry.setStatus("current")


class _UbiDhcpSnoopIfTrust_Type(Integer32):
    """Custom type ubiDhcpSnoopIfTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trusted", 1))
    )


_UbiDhcpSnoopIfTrust_Type.__name__ = "Integer32"
_UbiDhcpSnoopIfTrust_Object = MibTableColumn
ubiDhcpSnoopIfTrust = _UbiDhcpSnoopIfTrust_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 3, 4, 1, 1),
    _UbiDhcpSnoopIfTrust_Type()
)
ubiDhcpSnoopIfTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiDhcpSnoopIfTrust.setStatus("current")
_UbiDaiMIBObjects_ObjectIdentity = ObjectIdentity
ubiDaiMIBObjects = _UbiDaiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4)
)
_UbiArpInspection_ObjectIdentity = ObjectIdentity
ubiArpInspection = _UbiArpInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1)
)
_UbiArpInspectTable_Object = MibTable
ubiArpInspectTable = _UbiArpInspectTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ubiArpInspectTable.setStatus("current")
_UbiArpInspectEntry_Object = MibTableRow
ubiArpInspectEntry = _UbiArpInspectEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 1, 1)
)
ubiArpInspectEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiVlanId"),
)
if mibBuilder.loadTexts:
    ubiArpInspectEntry.setStatus("current")
_UbiArpInspectRowStatus_Type = RowStatus
_UbiArpInspectRowStatus_Object = MibTableColumn
ubiArpInspectRowStatus = _UbiArpInspectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 1, 1, 1),
    _UbiArpInspectRowStatus_Type()
)
ubiArpInspectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiArpInspectRowStatus.setStatus("current")
_UbiArpInspectValidateTable_Object = MibTable
ubiArpInspectValidateTable = _UbiArpInspectValidateTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ubiArpInspectValidateTable.setStatus("current")
_UbiArpInspectValidateEntry_Object = MibTableRow
ubiArpInspectValidateEntry = _UbiArpInspectValidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 2, 1)
)
ubiArpInspectValidateEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "noIndex"),
)
if mibBuilder.loadTexts:
    ubiArpInspectValidateEntry.setStatus("current")


class _UbiArpInspectValidateDestMac_Type(Integer32):
    """Custom type ubiArpInspectValidateDestMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiArpInspectValidateDestMac_Type.__name__ = "Integer32"
_UbiArpInspectValidateDestMac_Object = MibTableColumn
ubiArpInspectValidateDestMac = _UbiArpInspectValidateDestMac_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 2, 1, 1),
    _UbiArpInspectValidateDestMac_Type()
)
ubiArpInspectValidateDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspectValidateDestMac.setStatus("current")


class _UbiArpInspectValidateSrcMac_Type(Integer32):
    """Custom type ubiArpInspectValidateSrcMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiArpInspectValidateSrcMac_Type.__name__ = "Integer32"
_UbiArpInspectValidateSrcMac_Object = MibTableColumn
ubiArpInspectValidateSrcMac = _UbiArpInspectValidateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 2, 1, 2),
    _UbiArpInspectValidateSrcMac_Type()
)
ubiArpInspectValidateSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspectValidateSrcMac.setStatus("current")


class _UbiArpInspectValidateIpAddr_Type(Integer32):
    """Custom type ubiArpInspectValidateIpAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiArpInspectValidateIpAddr_Type.__name__ = "Integer32"
_UbiArpInspectValidateIpAddr_Object = MibTableColumn
ubiArpInspectValidateIpAddr = _UbiArpInspectValidateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 2, 1, 3),
    _UbiArpInspectValidateIpAddr_Type()
)
ubiArpInspectValidateIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspectValidateIpAddr.setStatus("current")


class _UbiArpInspectValidateArpField_Type(Integer32):
    """Custom type ubiArpInspectValidateArpField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UbiArpInspectValidateArpField_Type.__name__ = "Integer32"
_UbiArpInspectValidateArpField_Object = MibTableColumn
ubiArpInspectValidateArpField = _UbiArpInspectValidateArpField_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 2, 1, 4),
    _UbiArpInspectValidateArpField_Type()
)
ubiArpInspectValidateArpField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspectValidateArpField.setStatus("current")
_UbiArpInspectLog_ObjectIdentity = ObjectIdentity
ubiArpInspectLog = _UbiArpInspectLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3)
)
_UbiArpInspectLogInfoTable_Object = MibTable
ubiArpInspectLogInfoTable = _UbiArpInspectLogInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ubiArpInspectLogInfoTable.setStatus("current")
_UbiArpInspectLogInfoEntry_Object = MibTableRow
ubiArpInspectLogInfoEntry = _UbiArpInspectLogInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 1, 1)
)
ubiArpInspectLogInfoEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "noIndex"),
)
if mibBuilder.loadTexts:
    ubiArpInspectLogInfoEntry.setStatus("current")
_UbiArpInspecLogInfoTotalLogBuffer_Type = Integer32
_UbiArpInspecLogInfoTotalLogBuffer_Object = MibTableColumn
ubiArpInspecLogInfoTotalLogBuffer = _UbiArpInspecLogInfoTotalLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 1, 1, 1),
    _UbiArpInspecLogInfoTotalLogBuffer_Type()
)
ubiArpInspecLogInfoTotalLogBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspecLogInfoTotalLogBuffer.setStatus("current")
_UbiArpInspecLogInfoLogRate_Type = DisplayString
_UbiArpInspecLogInfoLogRate_Object = MibTableColumn
ubiArpInspecLogInfoLogRate = _UbiArpInspecLogInfoLogRate_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 1, 1, 2),
    _UbiArpInspecLogInfoLogRate_Type()
)
ubiArpInspecLogInfoLogRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspecLogInfoLogRate.setStatus("current")


class _UbiArpInspecLogInfoRepeatCount_Type(Integer32):
    """Custom type ubiArpInspecLogInfoRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_UbiArpInspecLogInfoRepeatCount_Type.__name__ = "Integer32"
_UbiArpInspecLogInfoRepeatCount_Object = MibTableColumn
ubiArpInspecLogInfoRepeatCount = _UbiArpInspecLogInfoRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 1, 1, 3),
    _UbiArpInspecLogInfoRepeatCount_Type()
)
ubiArpInspecLogInfoRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspecLogInfoRepeatCount.setStatus("current")
_UbiArpInspecLogInfoLogClear_Type = Integer32
_UbiArpInspecLogInfoLogClear_Object = MibTableColumn
ubiArpInspecLogInfoLogClear = _UbiArpInspecLogInfoLogClear_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 1, 1, 4),
    _UbiArpInspecLogInfoLogClear_Type()
)
ubiArpInspecLogInfoLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiArpInspecLogInfoLogClear.setStatus("current")
_UbiArpInspectLogTable_Object = MibTable
ubiArpInspectLogTable = _UbiArpInspectLogTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ubiArpInspectLogTable.setStatus("current")
_UbiArpInspectLogEntry_Object = MibTableRow
ubiArpInspectLogEntry = _UbiArpInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2, 1)
)
ubiArpInspectLogEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "ubiArpInspecLogIndex"),
)
if mibBuilder.loadTexts:
    ubiArpInspectLogEntry.setStatus("current")
_UbiArpInspecLogIndex_Type = Integer32
_UbiArpInspecLogIndex_Object = MibTableColumn
ubiArpInspecLogIndex = _UbiArpInspecLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2, 1, 1),
    _UbiArpInspecLogIndex_Type()
)
ubiArpInspecLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiArpInspecLogIndex.setStatus("current")
_UbiArpInspecLogIfName_Type = DisplayString
_UbiArpInspecLogIfName_Object = MibTableColumn
ubiArpInspecLogIfName = _UbiArpInspecLogIfName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2, 1, 2),
    _UbiArpInspecLogIfName_Type()
)
ubiArpInspecLogIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiArpInspecLogIfName.setStatus("current")
_UbiArpInspectLogVlanName_Type = DisplayString
_UbiArpInspectLogVlanName_Object = MibTableColumn
ubiArpInspectLogVlanName = _UbiArpInspectLogVlanName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2, 1, 3),
    _UbiArpInspectLogVlanName_Type()
)
ubiArpInspectLogVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiArpInspectLogVlanName.setStatus("current")
_UbiArpInspectLogMacAddr_Type = PhysAddress
_UbiArpInspectLogMacAddr_Object = MibTableColumn
ubiArpInspectLogMacAddr = _UbiArpInspectLogMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2, 1, 4),
    _UbiArpInspectLogMacAddr_Type()
)
ubiArpInspectLogMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiArpInspectLogMacAddr.setStatus("current")
_UbiArpInspectLogIpAddr_Type = IpAddress
_UbiArpInspectLogIpAddr_Object = MibTableColumn
ubiArpInspectLogIpAddr = _UbiArpInspectLogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2, 1, 5),
    _UbiArpInspectLogIpAddr_Type()
)
ubiArpInspectLogIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiArpInspectLogIpAddr.setStatus("current")
_UbiArpInspectLogCount_Type = Integer32
_UbiArpInspectLogCount_Object = MibTableColumn
ubiArpInspectLogCount = _UbiArpInspectLogCount_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 3, 2, 1, 6),
    _UbiArpInspectLogCount_Type()
)
ubiArpInspectLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiArpInspectLogCount.setStatus("current")
_UbiArpInspectAclTable_Object = MibTable
ubiArpInspectAclTable = _UbiArpInspectAclTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ubiArpInspectAclTable.setStatus("current")
_UbiArpInspectAclEntry_Object = MibTableRow
ubiArpInspectAclEntry = _UbiArpInspectAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 4, 1)
)
ubiArpInspectAclEntry.setIndexNames(
    (0, "UBQS-DHCP-MIB", "uibAclName"),
    (0, "UBQS-DHCP-MIB", "ubiVlanId"),
)
if mibBuilder.loadTexts:
    ubiArpInspectAclEntry.setStatus("current")
_UbiArpInspectAclRowStatus_Type = RowStatus
_UbiArpInspectAclRowStatus_Object = MibTableColumn
ubiArpInspectAclRowStatus = _UbiArpInspectAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 4, 1, 4, 1, 1),
    _UbiArpInspectAclRowStatus_Type()
)
ubiArpInspectAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiArpInspectAclRowStatus.setStatus("current")
_UbiDhcpMIBConformance_ObjectIdentity = ObjectIdentity
ubiDhcpMIBConformance = _UbiDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6)
)
_UbiDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
ubiDhcpMIBCompliances = _UbiDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6, 1)
)
_UbiDhcpMIBGroups_ObjectIdentity = ObjectIdentity
ubiDhcpMIBGroups = _UbiDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6, 2)
)

# Managed Objects groups

ubiDhcpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6, 2, 1)
)
ubiDhcpMIBGroup.setObjects(
      *(("UBQS-DHCP-MIB", "ubiDhcpTotalSubnets"),
        ("UBQS-DHCP-MIB", "ubiDhcpFreeAddress"),
        ("UBQS-DHCP-MIB", "ubiDhcpTotalAddress"),
        ("UBQS-DHCP-MIB", "ubiDhcpInUse"),
        ("UBQS-DHCP-MIB", "ubiDhcpAutomatic"),
        ("UBQS-DHCP-MIB", "ubiDhcpManual"),
        ("UBQS-DHCP-MIB", "ubiDhcpLowThreshold"),
        ("UBQS-DHCP-MIB", "ubiDhcpHighThreshold"),
        ("UBQS-DHCP-MIB", "ubiDhcpFreeAddrValue"),
        ("UBQS-DHCP-MIB", "ubiDhcpFreeAddrUnit"),
        ("UBQS-DHCP-MIB", "ubiDhcpPoolSubnetName"),
        ("UBQS-DHCP-MIB", "ubiDhcpPoolSubnet"),
        ("UBQS-DHCP-MIB", "ubiDhcpPoolSubnetMask"),
        ("UBQS-DHCP-MIB", "ubiDhcpPoolSubnetFreeAddress"),
        ("UBQS-DHCP-MIB", "ubiDhcpPoolSubnetTotalAddress"),
        ("UBQS-DHCP-MIB", "ubiDhcpPoolSubnetInUse"))
)
if mibBuilder.loadTexts:
    ubiDhcpMIBGroup.setStatus("current")

ubiDaiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6, 2, 3)
)
ubiDaiMIBGroup.setObjects(
      *(("UBQS-DHCP-MIB", "ubiArpInspectRowStatus"),
        ("UBQS-DHCP-MIB", "ubiArpInspectValidateDestMac"),
        ("UBQS-DHCP-MIB", "ubiArpInspectValidateSrcMac"),
        ("UBQS-DHCP-MIB", "ubiArpInspectValidateIpAddr"),
        ("UBQS-DHCP-MIB", "ubiArpInspectValidateArpField"),
        ("UBQS-DHCP-MIB", "ubiArpInspecLoggingTotalLogBuffer"),
        ("UBQS-DHCP-MIB", "ubiArpInspecLoggingLogNum"))
)
if mibBuilder.loadTexts:
    ubiDaiMIBGroup.setStatus("current")


# Notification objects

ubiDhcpServerInUseAddressHighNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 0, 0, 1)
)
ubiDhcpServerInUseAddressHighNotification.setObjects(
      *(("UBQS-DHCP-MIB", "ubiAlarmIndex"),
        ("UBQS-DHCP-MIB", "ubiAlarmId"),
        ("UBQS-DHCP-MIB", "ubiAlarmType"),
        ("UBQS-DHCP-MIB", "ubiAlarmSeverity"),
        ("UBQS-DHCP-MIB", "ubiAlarmPhysicalLoc"),
        ("UBQS-DHCP-MIB", "ubiAlarmLogicalLoc"),
        ("UBQS-DHCP-MIB", "ubiAlarmCurStatus"),
        ("UBQS-DHCP-MIB", "ubiAlarmAuxinfo"),
        ("UBQS-DHCP-MIB", "ubiAlarmDateTime"),
        ("UBQS-DHCP-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiDhcpServerInUseAddressHighNotification.setStatus(
        "current"
    )

ubiDhcpServerInUseAddressLowNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 0, 0, 2)
)
ubiDhcpServerInUseAddressLowNotification.setObjects(
      *(("UBQS-DHCP-MIB", "ubiAlarmIndex"),
        ("UBQS-DHCP-MIB", "ubiAlarmId"),
        ("UBQS-DHCP-MIB", "ubiAlarmType"),
        ("UBQS-DHCP-MIB", "ubiAlarmSeverity"),
        ("UBQS-DHCP-MIB", "ubiAlarmPhysicalLoc"),
        ("UBQS-DHCP-MIB", "ubiAlarmLogicalLoc"),
        ("UBQS-DHCP-MIB", "ubiAlarmCurStatus"),
        ("UBQS-DHCP-MIB", "ubiAlarmAuxinfo"),
        ("UBQS-DHCP-MIB", "ubiAlarmDateTime"),
        ("UBQS-DHCP-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiDhcpServerInUseAddressLowNotification.setStatus(
        "current"
    )


# Notifications groups

ubiDhcpMIBStatusChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6, 2, 2)
)
ubiDhcpMIBStatusChangeNotifGroup.setObjects(
      *(("UBQS-DHCP-MIB", "ubiDhcpServerInUseAddressHighNotification"),
        ("UBQS-DHCP-MIB", "ubiDhcpServerInUseAddressLowNotification"))
)
if mibBuilder.loadTexts:
    ubiDhcpMIBStatusChangeNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ubiDhcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6, 1, 1)
)
ubiDhcpMIBCompliance.setObjects(
      *(("UBQS-DHCP-MIB", "ubiDhcpMIBGroup"),
        ("UBQS-DHCP-MIB", "ubiDhcpMIBStatusChangeNotifGroup"),
        ("UBQS-DHCP-MIB", "ubiDhcpMIBGroup"),
        ("UBQS-DHCP-MIB", "ubiDhcpMIBStatusChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    ubiDhcpMIBCompliance.setStatus(
        "current"
    )

ubiDaiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 6, 6, 1, 2)
)
ubiDaiMIBCompliance.setObjects(
      *(("UBQS-DHCP-MIB", "ubiDaiMIBGroup"),
        ("UBQS-DHCP-MIB", "ubiDaiMIBGroup"))
)
if mibBuilder.loadTexts:
    ubiDaiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-DHCP-MIB",
    **{"ubiDhcpMIB": ubiDhcpMIB,
       "ubiDhcpMIBNotificationPrefix": ubiDhcpMIBNotificationPrefix,
       "ubiDhcpMIBNotifications": ubiDhcpMIBNotifications,
       "ubiDhcpServerInUseAddressHighNotification": ubiDhcpServerInUseAddressHighNotification,
       "ubiDhcpServerInUseAddressLowNotification": ubiDhcpServerInUseAddressLowNotification,
       "ubiDhcpServerMIBObjects": ubiDhcpServerMIBObjects,
       "ubiDhcpStatisticsTable": ubiDhcpStatisticsTable,
       "ubiDhcpStatisticsEntry": ubiDhcpStatisticsEntry,
       "ubiDhcpCurPktMFMessage": ubiDhcpCurPktMFMessage,
       "ubiDhcpCurPktBootReq": ubiDhcpCurPktBootReq,
       "ubiDhcpCurPktDiscover": ubiDhcpCurPktDiscover,
       "ubiDhcpCurPktReq": ubiDhcpCurPktReq,
       "ubiDhcpCurPktDecline": ubiDhcpCurPktDecline,
       "ubiDhcpCurPktRelease": ubiDhcpCurPktRelease,
       "ubiDhcpCurPktInform": ubiDhcpCurPktInform,
       "ubiDhcpCurPktEcho": ubiDhcpCurPktEcho,
       "ubiDhcpCurPktReply": ubiDhcpCurPktReply,
       "ubiDhcpCurPktOffer": ubiDhcpCurPktOffer,
       "ubiDhcpCurPktAck": ubiDhcpCurPktAck,
       "ubiDhcpCurPktNak": ubiDhcpCurPktNak,
       "ubiDhcpServerPoolTable": ubiDhcpServerPoolTable,
       "ubiDhcpServerPoolEntry": ubiDhcpServerPoolEntry,
       "ubiDhcpServerPoolName": ubiDhcpServerPoolName,
       "ubiDhcpServerPoolSubnet": ubiDhcpServerPoolSubnet,
       "ubiDhcpServerPoolSubnetMask": ubiDhcpServerPoolSubnetMask,
       "ubiDhcpServerPoolSubnetFreeAddress": ubiDhcpServerPoolSubnetFreeAddress,
       "ubiDhcpServerPoolSubnetTotalAddress": ubiDhcpServerPoolSubnetTotalAddress,
       "ubiDhcpServerPoolSubnetInUse": ubiDhcpServerPoolSubnetInUse,
       "ubiDhcpServerPoolSubnetGroup": ubiDhcpServerPoolSubnetGroup,
       "ubiDhcpServerPoolType": ubiDhcpServerPoolType,
       "ubiDhcpServerPoolDomainName": ubiDhcpServerPoolDomainName,
       "ubiDhcpServerPoolLeaseTimeMode": ubiDhcpServerPoolLeaseTimeMode,
       "ubiDhcpServerPoolLeaseTimeDays": ubiDhcpServerPoolLeaseTimeDays,
       "ubiDhcpServerPoolLeaseTimeHours": ubiDhcpServerPoolLeaseTimeHours,
       "ubiDhcpServerPoolLeaseTimeMinutes": ubiDhcpServerPoolLeaseTimeMinutes,
       "ubiDhcpServerPoolUsageThreshold": ubiDhcpServerPoolUsageThreshold,
       "ubiDhcpServerDefaultRouterInfo": ubiDhcpServerDefaultRouterInfo,
       "ubiDhcpServerRangeTable": ubiDhcpServerRangeTable,
       "ubiDhcpServerRangeEntry": ubiDhcpServerRangeEntry,
       "ubiDhcpServerPoolIndex": ubiDhcpServerPoolIndex,
       "ubiDhcpServerRangeStart": ubiDhcpServerRangeStart,
       "ubiDhcpServerRangeEnd": ubiDhcpServerRangeEnd,
       "ubiDhcpServerNetPoolRangeTable": ubiDhcpServerNetPoolRangeTable,
       "ubiDhcpServerNetPoolRangeEntry": ubiDhcpServerNetPoolRangeEntry,
       "ubiDhcpServerNetPoolRangePoolIndex": ubiDhcpServerNetPoolRangePoolIndex,
       "ubiDhcpServerNetPoolRangeStartIpAddr": ubiDhcpServerNetPoolRangeStartIpAddr,
       "ubiDhcpServerNetPoolRangeEndIpAddr": ubiDhcpServerNetPoolRangeEndIpAddr,
       "ubiDhcpServerNetPoolRangeRowstatus": ubiDhcpServerNetPoolRangeRowstatus,
       "ubiDhcpServerPoolRowTable": ubiDhcpServerPoolRowTable,
       "ubiDhcpServerPoolRowEntry": ubiDhcpServerPoolRowEntry,
       "ubiDhcpServerPoolRowStatus": ubiDhcpServerPoolRowStatus,
       "ubiDhcpServerFixedAddrTable": ubiDhcpServerFixedAddrTable,
       "ubiDhcpServerFixedAddrEntry": ubiDhcpServerFixedAddrEntry,
       "ubiDhcpServerFixedAddrHostPoolName": ubiDhcpServerFixedAddrHostPoolName,
       "ubiDhcpServerFixedAddrMac": ubiDhcpServerFixedAddrMac,
       "ubiDhcpServerFixedAddrIp": ubiDhcpServerFixedAddrIp,
       "ubiDhcpServerFixedAddrNetmask": ubiDhcpServerFixedAddrNetmask,
       "ubiDhcpServerFixedAddrRowStatus": ubiDhcpServerFixedAddrRowStatus,
       "ubiDhcpServerDnsTable": ubiDhcpServerDnsTable,
       "ubiDhcpServerDnsEntry": ubiDhcpServerDnsEntry,
       "ubiDhcpServerDnsPoolIndex": ubiDhcpServerDnsPoolIndex,
       "ubiDhcpServerDnsServerAddr": ubiDhcpServerDnsServerAddr,
       "ubiDhcpServerDnsRowStatus": ubiDhcpServerDnsRowStatus,
       "ubiDhcpServerBindingTable": ubiDhcpServerBindingTable,
       "ubiDhcpServerBindingEntry": ubiDhcpServerBindingEntry,
       "ubiDhcpServerBindingIndex": ubiDhcpServerBindingIndex,
       "ubiDhcpServerBindingIpAddr": ubiDhcpServerBindingIpAddr,
       "ubiDhcpServerBindingMacAddr": ubiDhcpServerBindingMacAddr,
       "ubiDhspServerBindingLeaseExpiration": ubiDhspServerBindingLeaseExpiration,
       "ubiDhcpServerBindingType": ubiDhcpServerBindingType,
       "ubiDhcpServerPoolSingleRangeTable": ubiDhcpServerPoolSingleRangeTable,
       "ubiDhcpServerPoolSingleRangeEntry": ubiDhcpServerPoolSingleRangeEntry,
       "ubiDhcpServerPoolSingleRangePoolIndex": ubiDhcpServerPoolSingleRangePoolIndex,
       "ubiDhcpServerPoolSingleRangeIpAddr": ubiDhcpServerPoolSingleRangeIpAddr,
       "ubiDhcpServerPoolSingleRangeRowstatus": ubiDhcpServerPoolSingleRangeRowstatus,
       "ubiDhcpServerInfoTable": ubiDhcpServerInfoTable,
       "ubiDhcpServerInfoEntry": ubiDhcpServerInfoEntry,
       "ubiDhcpServerAdminStatus": ubiDhcpServerAdminStatus,
       "ubiDhcpLeaseTimeMode": ubiDhcpLeaseTimeMode,
       "ubiDhcpLeaseTimeModeDays": ubiDhcpLeaseTimeModeDays,
       "ubiDhcpLeaseTimeModeHours": ubiDhcpLeaseTimeModeHours,
       "ubiDhcpLeaseTimeModeMinutes": ubiDhcpLeaseTimeModeMinutes,
       "ubiDhcpLeaseTimeModeStatus": ubiDhcpLeaseTimeModeStatus,
       "ubiDhcpRelayMIBObjects": ubiDhcpRelayMIBObjects,
       "ubiDhcpRelayInfoTable": ubiDhcpRelayInfoTable,
       "ubiDhcpRelayInfoEntry": ubiDhcpRelayInfoEntry,
       "ubiDhcpRelayAdminStatus": ubiDhcpRelayAdminStatus,
       "ubiDhcpRelayOption82Status": ubiDhcpRelayOption82Status,
       "ubiDhcpRelayOption82Policy": ubiDhcpRelayOption82Policy,
       "ubiDhcpRelayBindingListDisplayOption": ubiDhcpRelayBindingListDisplayOption,
       "ubiDhcpRelayVerifyMAC": ubiDhcpRelayVerifyMAC,
       "ubiDhcpRelayServerIPTable": ubiDhcpRelayServerIPTable,
       "ubiDhcpRelayServerIPEntry": ubiDhcpRelayServerIPEntry,
       "ubiDhcpRelayServerIP": ubiDhcpRelayServerIP,
       "ubiDhcpRelayServerIPRowStatus": ubiDhcpRelayServerIPRowStatus,
       "ubiDhcpRelayStatistics": ubiDhcpRelayStatistics,
       "ubiDhcpRelayCurPktDiscover": ubiDhcpRelayCurPktDiscover,
       "ubiDhcpRelayCurPktReq": ubiDhcpRelayCurPktReq,
       "ubiDhcpRelayCurPktOffer": ubiDhcpRelayCurPktOffer,
       "ubiDhcpRelayCurPktAck": ubiDhcpRelayCurPktAck,
       "ubiDhcpSnoopMIBObjects": ubiDhcpSnoopMIBObjects,
       "ubiDhcpSnoopInfoTable": ubiDhcpSnoopInfoTable,
       "ubiDhcpSnoopInfoEntry": ubiDhcpSnoopInfoEntry,
       "ubiDhcpSnoopAdminStatus": ubiDhcpSnoopAdminStatus,
       "ubiDhcpSnoopLeaseTimeExtention": ubiDhcpSnoopLeaseTimeExtention,
       "ubiDhcpSnoopBlockLogClear": ubiDhcpSnoopBlockLogClear,
       "ubiDhcpSnoopOption82Status": ubiDhcpSnoopOption82Status,
       "ubiDhcpSnoopOption82Policy": ubiDhcpSnoopOption82Policy,
       "ubiDhcpSnoopVerifyMAC": ubiDhcpSnoopVerifyMAC,
       "ubiDhcpSnoopBindingCount": ubiDhcpSnoopBindingCount,
       "ubiDhcpSnoopInvalidCount": ubiDhcpSnoopInvalidCount,
       "ubiDhcpSnoopVlanTable": ubiDhcpSnoopVlanTable,
       "ubiDhcpSnoopVlanEntry": ubiDhcpSnoopVlanEntry,
       "ubiDhcpSnoopVlanIfName": ubiDhcpSnoopVlanIfName,
       "ubiDhcpSnoopVlanRowStatus": ubiDhcpSnoopVlanRowStatus,
       "ubiDhcpSnoopBindingTable": ubiDhcpSnoopBindingTable,
       "ubiDhcpSnoopBindingEntry": ubiDhcpSnoopBindingEntry,
       "ubiDhcpSnoopBindingIndex": ubiDhcpSnoopBindingIndex,
       "ubiDhcpSnoopBindingMacAddr": ubiDhcpSnoopBindingMacAddr,
       "ubiDhcpSnoopBindingIpAddr": ubiDhcpSnoopBindingIpAddr,
       "ubiDhcpSnoopBindingState": ubiDhcpSnoopBindingState,
       "ubiDhcpSnoopBindingVlanName": ubiDhcpSnoopBindingVlanName,
       "ubiDhcpSnoopBindingPortName": ubiDhcpSnoopBindingPortName,
       "ubiDhcpSnoopBindingUpdate": ubiDhcpSnoopBindingUpdate,
       "ubiDhcpSnoopBindingLeaseTime": ubiDhcpSnoopBindingLeaseTime,
       "ubiDhcpSnoopIfTable": ubiDhcpSnoopIfTable,
       "ubiDhcpSnoopIfEntry": ubiDhcpSnoopIfEntry,
       "ubiDhcpSnoopIfTrust": ubiDhcpSnoopIfTrust,
       "ubiDaiMIBObjects": ubiDaiMIBObjects,
       "ubiArpInspection": ubiArpInspection,
       "ubiArpInspectTable": ubiArpInspectTable,
       "ubiArpInspectEntry": ubiArpInspectEntry,
       "ubiArpInspectRowStatus": ubiArpInspectRowStatus,
       "ubiArpInspectValidateTable": ubiArpInspectValidateTable,
       "ubiArpInspectValidateEntry": ubiArpInspectValidateEntry,
       "ubiArpInspectValidateDestMac": ubiArpInspectValidateDestMac,
       "ubiArpInspectValidateSrcMac": ubiArpInspectValidateSrcMac,
       "ubiArpInspectValidateIpAddr": ubiArpInspectValidateIpAddr,
       "ubiArpInspectValidateArpField": ubiArpInspectValidateArpField,
       "ubiArpInspectLog": ubiArpInspectLog,
       "ubiArpInspectLogInfoTable": ubiArpInspectLogInfoTable,
       "ubiArpInspectLogInfoEntry": ubiArpInspectLogInfoEntry,
       "ubiArpInspecLogInfoTotalLogBuffer": ubiArpInspecLogInfoTotalLogBuffer,
       "ubiArpInspecLogInfoLogRate": ubiArpInspecLogInfoLogRate,
       "ubiArpInspecLogInfoRepeatCount": ubiArpInspecLogInfoRepeatCount,
       "ubiArpInspecLogInfoLogClear": ubiArpInspecLogInfoLogClear,
       "ubiArpInspectLogTable": ubiArpInspectLogTable,
       "ubiArpInspectLogEntry": ubiArpInspectLogEntry,
       "ubiArpInspecLogIndex": ubiArpInspecLogIndex,
       "ubiArpInspecLogIfName": ubiArpInspecLogIfName,
       "ubiArpInspectLogVlanName": ubiArpInspectLogVlanName,
       "ubiArpInspectLogMacAddr": ubiArpInspectLogMacAddr,
       "ubiArpInspectLogIpAddr": ubiArpInspectLogIpAddr,
       "ubiArpInspectLogCount": ubiArpInspectLogCount,
       "ubiArpInspectAclTable": ubiArpInspectAclTable,
       "ubiArpInspectAclEntry": ubiArpInspectAclEntry,
       "ubiArpInspectAclRowStatus": ubiArpInspectAclRowStatus,
       "ubiDhcpMIBConformance": ubiDhcpMIBConformance,
       "ubiDhcpMIBCompliances": ubiDhcpMIBCompliances,
       "ubiDhcpMIBCompliance": ubiDhcpMIBCompliance,
       "ubiDaiMIBCompliance": ubiDaiMIBCompliance,
       "ubiDhcpMIBGroups": ubiDhcpMIBGroups,
       "ubiDhcpMIBGroup": ubiDhcpMIBGroup,
       "ubiDhcpMIBStatusChangeNotifGroup": ubiDhcpMIBStatusChangeNotifGroup,
       "ubiDaiMIBGroup": ubiDaiMIBGroup}
)
