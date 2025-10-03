# SNMP MIB module (BCN-DHCPV4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-DHCPV4-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:24 2025
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

(bcnServices,) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnServices")

(BcnAlarmSeverity,) = mibBuilder.importSymbols(
    "BCN-TC-MIB",
    "BcnAlarmSeverity")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bcnDhcpv4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bcnDhcpv4MIB.setRevisions(
        ("2010-12-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnDhcpv4_ObjectIdentity = ObjectIdentity
bcnDhcpv4 = _BcnDhcpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1)
)
_BcnDhcpv4Objects_ObjectIdentity = ObjectIdentity
bcnDhcpv4Objects = _BcnDhcpv4Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2)
)
_BcnDhcpv4ServiceStatus_ObjectIdentity = ObjectIdentity
bcnDhcpv4ServiceStatus = _BcnDhcpv4ServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bcnDhcpv4ServiceStatus.setStatus("current")


class _BcnDhcpv4SerOperState_Type(Integer32):
    """Custom type bcnDhcpv4SerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2),
          ("starting", 3),
          ("stopping", 4),
          ("fault", 5))
    )


_BcnDhcpv4SerOperState_Type.__name__ = "Integer32"
_BcnDhcpv4SerOperState_Object = MibScalar
bcnDhcpv4SerOperState = _BcnDhcpv4SerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 1),
    _BcnDhcpv4SerOperState_Type()
)
bcnDhcpv4SerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4SerOperState.setStatus("current")
_BcnDhcpv4FirstAlertIpAddr_Type = IpAddress
_BcnDhcpv4FirstAlertIpAddr_Object = MibScalar
bcnDhcpv4FirstAlertIpAddr = _BcnDhcpv4FirstAlertIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 2),
    _BcnDhcpv4FirstAlertIpAddr_Type()
)
bcnDhcpv4FirstAlertIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4FirstAlertIpAddr.setStatus("current")
_BcnDhcpv4LeaseStatsSuccess_Type = Gauge32
_BcnDhcpv4LeaseStatsSuccess_Object = MibScalar
bcnDhcpv4LeaseStatsSuccess = _BcnDhcpv4LeaseStatsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 3),
    _BcnDhcpv4LeaseStatsSuccess_Type()
)
bcnDhcpv4LeaseStatsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseStatsSuccess.setStatus("current")
_BcnDhcpv4ServiceStatistics_ObjectIdentity = ObjectIdentity
bcnDhcpv4ServiceStatistics = _BcnDhcpv4ServiceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bcnDhcpv4ServiceStatistics.setStatus("current")
_BcnDhcpv4LeaseTable_Object = MibTable
bcnDhcpv4LeaseTable = _BcnDhcpv4LeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseTable.setStatus("current")
_BcnDhcpv4LeaseEntry_Object = MibTableRow
bcnDhcpv4LeaseEntry = _BcnDhcpv4LeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1)
)
bcnDhcpv4LeaseEntry.setIndexNames(
    (0, "BCN-DHCPV4-MIB", "bcnDhcpv4LeaseIP"),
)
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseEntry.setStatus("current")
_BcnDhcpv4LeaseIP_Type = IpAddress
_BcnDhcpv4LeaseIP_Object = MibTableColumn
bcnDhcpv4LeaseIP = _BcnDhcpv4LeaseIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 1),
    _BcnDhcpv4LeaseIP_Type()
)
bcnDhcpv4LeaseIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseIP.setStatus("current")
_BcnDhcpv4LeaseStartTime_Type = Unsigned32
_BcnDhcpv4LeaseStartTime_Object = MibTableColumn
bcnDhcpv4LeaseStartTime = _BcnDhcpv4LeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 2),
    _BcnDhcpv4LeaseStartTime_Type()
)
bcnDhcpv4LeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseStartTime.setStatus("current")
_BcnDhcpv4LeaseEndTime_Type = Unsigned32
_BcnDhcpv4LeaseEndTime_Object = MibTableColumn
bcnDhcpv4LeaseEndTime = _BcnDhcpv4LeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 3),
    _BcnDhcpv4LeaseEndTime_Type()
)
bcnDhcpv4LeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseEndTime.setStatus("current")
_BcnDhcpv4LeaseTimeStamp_Type = Unsigned32
_BcnDhcpv4LeaseTimeStamp_Object = MibTableColumn
bcnDhcpv4LeaseTimeStamp = _BcnDhcpv4LeaseTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 4),
    _BcnDhcpv4LeaseTimeStamp_Type()
)
bcnDhcpv4LeaseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseTimeStamp.setStatus("current")
_BcnDhcpv4LeaseMacAddress_Type = MacAddress
_BcnDhcpv4LeaseMacAddress_Object = MibTableColumn
bcnDhcpv4LeaseMacAddress = _BcnDhcpv4LeaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 5),
    _BcnDhcpv4LeaseMacAddress_Type()
)
bcnDhcpv4LeaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseMacAddress.setStatus("current")
_BcnDhcpv4LeaseHostname_Type = DisplayString
_BcnDhcpv4LeaseHostname_Object = MibTableColumn
bcnDhcpv4LeaseHostname = _BcnDhcpv4LeaseHostname_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 6),
    _BcnDhcpv4LeaseHostname_Type()
)
bcnDhcpv4LeaseHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4LeaseHostname.setStatus("current")
_BcnDhcpv4SubnetTable_Object = MibTable
bcnDhcpv4SubnetTable = _BcnDhcpv4SubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetTable.setStatus("current")
_BcnDhcpv4SubnetEntry_Object = MibTableRow
bcnDhcpv4SubnetEntry = _BcnDhcpv4SubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1)
)
bcnDhcpv4SubnetEntry.setIndexNames(
    (0, "BCN-DHCPV4-MIB", "bcnDhcpv4SubnetIP"),
)
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetEntry.setStatus("current")
_BcnDhcpv4SubnetIP_Type = IpAddress
_BcnDhcpv4SubnetIP_Object = MibTableColumn
bcnDhcpv4SubnetIP = _BcnDhcpv4SubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 1),
    _BcnDhcpv4SubnetIP_Type()
)
bcnDhcpv4SubnetIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetIP.setStatus("current")
_BcnDhcpv4SubnetMask_Type = IpAddress
_BcnDhcpv4SubnetMask_Object = MibTableColumn
bcnDhcpv4SubnetMask = _BcnDhcpv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 2),
    _BcnDhcpv4SubnetMask_Type()
)
bcnDhcpv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetMask.setStatus("current")
_BcnDhcpv4SubnetSize_Type = Unsigned32
_BcnDhcpv4SubnetSize_Object = MibTableColumn
bcnDhcpv4SubnetSize = _BcnDhcpv4SubnetSize_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 3),
    _BcnDhcpv4SubnetSize_Type()
)
bcnDhcpv4SubnetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetSize.setStatus("current")
_BcnDhcpv4SubnetFreeAddresses_Type = Unsigned32
_BcnDhcpv4SubnetFreeAddresses_Object = MibTableColumn
bcnDhcpv4SubnetFreeAddresses = _BcnDhcpv4SubnetFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 4),
    _BcnDhcpv4SubnetFreeAddresses_Type()
)
bcnDhcpv4SubnetFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetFreeAddresses.setStatus("current")
_BcnDhcpv4SubnetLowThreshold_Type = Unsigned32
_BcnDhcpv4SubnetLowThreshold_Object = MibTableColumn
bcnDhcpv4SubnetLowThreshold = _BcnDhcpv4SubnetLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 5),
    _BcnDhcpv4SubnetLowThreshold_Type()
)
bcnDhcpv4SubnetLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetLowThreshold.setStatus("current")
_BcnDhcpv4SubnetHighThreshold_Type = Unsigned32
_BcnDhcpv4SubnetHighThreshold_Object = MibTableColumn
bcnDhcpv4SubnetHighThreshold = _BcnDhcpv4SubnetHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 6),
    _BcnDhcpv4SubnetHighThreshold_Type()
)
bcnDhcpv4SubnetHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetHighThreshold.setStatus("current")
_BcnDhcpv4PoolTable_Object = MibTable
bcnDhcpv4PoolTable = _BcnDhcpv4PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    bcnDhcpv4PoolTable.setStatus("current")
_BcnDhcpv4PoolEntry_Object = MibTableRow
bcnDhcpv4PoolEntry = _BcnDhcpv4PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1)
)
bcnDhcpv4PoolEntry.setIndexNames(
    (0, "BCN-DHCPV4-MIB", "bcnDhcpv4PoolStartIP"),
)
if mibBuilder.loadTexts:
    bcnDhcpv4PoolEntry.setStatus("current")
_BcnDhcpv4PoolStartIP_Type = IpAddress
_BcnDhcpv4PoolStartIP_Object = MibTableColumn
bcnDhcpv4PoolStartIP = _BcnDhcpv4PoolStartIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 1),
    _BcnDhcpv4PoolStartIP_Type()
)
bcnDhcpv4PoolStartIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcnDhcpv4PoolStartIP.setStatus("current")
_BcnDhcpv4PoolEndIP_Type = IpAddress
_BcnDhcpv4PoolEndIP_Object = MibTableColumn
bcnDhcpv4PoolEndIP = _BcnDhcpv4PoolEndIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 2),
    _BcnDhcpv4PoolEndIP_Type()
)
bcnDhcpv4PoolEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4PoolEndIP.setStatus("current")
_BcnDhcpv4PoolSubnetIP_Type = IpAddress
_BcnDhcpv4PoolSubnetIP_Object = MibTableColumn
bcnDhcpv4PoolSubnetIP = _BcnDhcpv4PoolSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 3),
    _BcnDhcpv4PoolSubnetIP_Type()
)
bcnDhcpv4PoolSubnetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4PoolSubnetIP.setStatus("current")
_BcnDhcpv4PoolSize_Type = Unsigned32
_BcnDhcpv4PoolSize_Object = MibTableColumn
bcnDhcpv4PoolSize = _BcnDhcpv4PoolSize_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 4),
    _BcnDhcpv4PoolSize_Type()
)
bcnDhcpv4PoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4PoolSize.setStatus("current")
_BcnDhcpv4PoolFreeAddresses_Type = Unsigned32
_BcnDhcpv4PoolFreeAddresses_Object = MibTableColumn
bcnDhcpv4PoolFreeAddresses = _BcnDhcpv4PoolFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 5),
    _BcnDhcpv4PoolFreeAddresses_Type()
)
bcnDhcpv4PoolFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4PoolFreeAddresses.setStatus("current")
_BcnDhcpv4FixedIPTable_Object = MibTable
bcnDhcpv4FixedIPTable = _BcnDhcpv4FixedIPTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    bcnDhcpv4FixedIPTable.setStatus("current")
_BcnDhcpv4FixedIPEntry_Object = MibTableRow
bcnDhcpv4FixedIPEntry = _BcnDhcpv4FixedIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4, 1)
)
bcnDhcpv4FixedIPEntry.setIndexNames(
    (0, "BCN-DHCPV4-MIB", "bcnDhcpv4FixedIP"),
)
if mibBuilder.loadTexts:
    bcnDhcpv4FixedIPEntry.setStatus("current")
_BcnDhcpv4FixedIP_Type = IpAddress
_BcnDhcpv4FixedIP_Object = MibTableColumn
bcnDhcpv4FixedIP = _BcnDhcpv4FixedIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4, 1, 1),
    _BcnDhcpv4FixedIP_Type()
)
bcnDhcpv4FixedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDhcpv4FixedIP.setStatus("current")
_BcnDhcpv4Notification_ObjectIdentity = ObjectIdentity
bcnDhcpv4Notification = _BcnDhcpv4Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3)
)
_BcnDhcpv4NotificationEvents_ObjectIdentity = ObjectIdentity
bcnDhcpv4NotificationEvents = _BcnDhcpv4NotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0)
)
_BcnDhcpv4NotificationData_ObjectIdentity = ObjectIdentity
bcnDhcpv4NotificationData = _BcnDhcpv4NotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1)
)
_BcnDhcpv4AlarmSeverity_Type = BcnAlarmSeverity
_BcnDhcpv4AlarmSeverity_Object = MibScalar
bcnDhcpv4AlarmSeverity = _BcnDhcpv4AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 1),
    _BcnDhcpv4AlarmSeverity_Type()
)
bcnDhcpv4AlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnDhcpv4AlarmSeverity.setStatus("current")
_BcnDhcpv4AlarmInfo_Type = DisplayString
_BcnDhcpv4AlarmInfo_Object = MibScalar
bcnDhcpv4AlarmInfo = _BcnDhcpv4AlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 2),
    _BcnDhcpv4AlarmInfo_Type()
)
bcnDhcpv4AlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnDhcpv4AlarmInfo.setStatus("current")


class _BcnDhcpv4FailOverState_Type(Integer32):
    """Custom type bcnDhcpv4FailOverState based on Integer32"""
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
              254)
        )
    )
    namedValues = NamedValues(
        *(("startup", 1),
          ("normal", 2),
          ("communicationsInterrupted", 3),
          ("partnerDown", 4),
          ("potentialConflict", 5),
          ("recover", 6),
          ("paused", 7),
          ("shutdown", 8),
          ("recoverDone", 9),
          ("recoverWait", 254))
    )


_BcnDhcpv4FailOverState_Type.__name__ = "Integer32"
_BcnDhcpv4FailOverState_Object = MibScalar
bcnDhcpv4FailOverState = _BcnDhcpv4FailOverState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 3),
    _BcnDhcpv4FailOverState_Type()
)
bcnDhcpv4FailOverState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnDhcpv4FailOverState.setStatus("current")
_BcnDhcpv4SubnetAlertIpAddr_Type = IpAddress
_BcnDhcpv4SubnetAlertIpAddr_Object = MibScalar
bcnDhcpv4SubnetAlertIpAddr = _BcnDhcpv4SubnetAlertIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 4),
    _BcnDhcpv4SubnetAlertIpAddr_Type()
)
bcnDhcpv4SubnetAlertIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetAlertIpAddr.setStatus("current")
_BcnDhcpv4Conformance_ObjectIdentity = ObjectIdentity
bcnDhcpv4Conformance = _BcnDhcpv4Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4)
)
_BcnDhcpv4ServiceCompliances_ObjectIdentity = ObjectIdentity
bcnDhcpv4ServiceCompliances = _BcnDhcpv4ServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 1)
)
_BcnDhcpv4ServiceGroups_ObjectIdentity = ObjectIdentity
bcnDhcpv4ServiceGroups = _BcnDhcpv4ServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2)
)

# Managed Objects groups

bcnDhcpv4ServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 1)
)
bcnDhcpv4ServiceStatusGroup.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4SerOperState"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4FirstAlertIpAddr"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseStatsSuccess"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4ServiceStatusGroup.setStatus("current")

bcnDhcpv4StatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 2)
)
bcnDhcpv4StatisticsGroup.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseStartTime"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseEndTime"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseTimeStamp"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseMacAddress"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseHostname"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetMask"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetSize"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowThreshold"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighThreshold"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolSubnetIP"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolEndIP"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolSize"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolFreeAddresses"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4FixedIP"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4StatisticsGroup.setStatus("current")

bcnDhcpv4NotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 4)
)
bcnDhcpv4NotificationDataGroup.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmSeverity"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmInfo"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverState"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4NotificationDataGroup.setStatus("current")


# Notification objects

bcnDhcpv4AlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 1)
)
bcnDhcpv4AlarmNotif.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4SerOperState"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmSeverity"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4AlarmNotif.setStatus(
        "current"
    )

bcnDhcpv4FailOverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 2)
)
bcnDhcpv4FailOverNotif.setObjects(
    ("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverState")
)
if mibBuilder.loadTexts:
    bcnDhcpv4FailOverNotif.setStatus(
        "current"
    )

bcnDhcpv4SubnetLowNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 3)
)
bcnDhcpv4SubnetLowNotif.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowThreshold"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetLowNotif.setStatus(
        "current"
    )

bcnDhcpv4SubnetHighNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 4)
)
bcnDhcpv4SubnetHighNotif.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighThreshold"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4SubnetHighNotif.setStatus(
        "current"
    )


# Notifications groups

bcnDhcpv4NotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 3)
)
bcnDhcpv4NotificationEventGroup.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmNotif"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverNotif"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowNotif"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighNotif"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4NotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnDhcpv4StatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 1, 1)
)
bcnDhcpv4StatusCompliance.setObjects(
      *(("BCN-DHCPV4-MIB", "bcnDhcpv4ServiceStatusGroup"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4StatisticsGroup"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4NotificationEventGroup"),
        ("BCN-DHCPV4-MIB", "bcnDhcpv4NotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnDhcpv4StatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-DHCPV4-MIB",
    **{"bcnDhcpv4": bcnDhcpv4,
       "bcnDhcpv4MIB": bcnDhcpv4MIB,
       "bcnDhcpv4Objects": bcnDhcpv4Objects,
       "bcnDhcpv4ServiceStatus": bcnDhcpv4ServiceStatus,
       "bcnDhcpv4SerOperState": bcnDhcpv4SerOperState,
       "bcnDhcpv4FirstAlertIpAddr": bcnDhcpv4FirstAlertIpAddr,
       "bcnDhcpv4LeaseStatsSuccess": bcnDhcpv4LeaseStatsSuccess,
       "bcnDhcpv4ServiceStatistics": bcnDhcpv4ServiceStatistics,
       "bcnDhcpv4LeaseTable": bcnDhcpv4LeaseTable,
       "bcnDhcpv4LeaseEntry": bcnDhcpv4LeaseEntry,
       "bcnDhcpv4LeaseIP": bcnDhcpv4LeaseIP,
       "bcnDhcpv4LeaseStartTime": bcnDhcpv4LeaseStartTime,
       "bcnDhcpv4LeaseEndTime": bcnDhcpv4LeaseEndTime,
       "bcnDhcpv4LeaseTimeStamp": bcnDhcpv4LeaseTimeStamp,
       "bcnDhcpv4LeaseMacAddress": bcnDhcpv4LeaseMacAddress,
       "bcnDhcpv4LeaseHostname": bcnDhcpv4LeaseHostname,
       "bcnDhcpv4SubnetTable": bcnDhcpv4SubnetTable,
       "bcnDhcpv4SubnetEntry": bcnDhcpv4SubnetEntry,
       "bcnDhcpv4SubnetIP": bcnDhcpv4SubnetIP,
       "bcnDhcpv4SubnetMask": bcnDhcpv4SubnetMask,
       "bcnDhcpv4SubnetSize": bcnDhcpv4SubnetSize,
       "bcnDhcpv4SubnetFreeAddresses": bcnDhcpv4SubnetFreeAddresses,
       "bcnDhcpv4SubnetLowThreshold": bcnDhcpv4SubnetLowThreshold,
       "bcnDhcpv4SubnetHighThreshold": bcnDhcpv4SubnetHighThreshold,
       "bcnDhcpv4PoolTable": bcnDhcpv4PoolTable,
       "bcnDhcpv4PoolEntry": bcnDhcpv4PoolEntry,
       "bcnDhcpv4PoolStartIP": bcnDhcpv4PoolStartIP,
       "bcnDhcpv4PoolEndIP": bcnDhcpv4PoolEndIP,
       "bcnDhcpv4PoolSubnetIP": bcnDhcpv4PoolSubnetIP,
       "bcnDhcpv4PoolSize": bcnDhcpv4PoolSize,
       "bcnDhcpv4PoolFreeAddresses": bcnDhcpv4PoolFreeAddresses,
       "bcnDhcpv4FixedIPTable": bcnDhcpv4FixedIPTable,
       "bcnDhcpv4FixedIPEntry": bcnDhcpv4FixedIPEntry,
       "bcnDhcpv4FixedIP": bcnDhcpv4FixedIP,
       "bcnDhcpv4Notification": bcnDhcpv4Notification,
       "bcnDhcpv4NotificationEvents": bcnDhcpv4NotificationEvents,
       "bcnDhcpv4AlarmNotif": bcnDhcpv4AlarmNotif,
       "bcnDhcpv4FailOverNotif": bcnDhcpv4FailOverNotif,
       "bcnDhcpv4SubnetLowNotif": bcnDhcpv4SubnetLowNotif,
       "bcnDhcpv4SubnetHighNotif": bcnDhcpv4SubnetHighNotif,
       "bcnDhcpv4NotificationData": bcnDhcpv4NotificationData,
       "bcnDhcpv4AlarmSeverity": bcnDhcpv4AlarmSeverity,
       "bcnDhcpv4AlarmInfo": bcnDhcpv4AlarmInfo,
       "bcnDhcpv4FailOverState": bcnDhcpv4FailOverState,
       "bcnDhcpv4SubnetAlertIpAddr": bcnDhcpv4SubnetAlertIpAddr,
       "bcnDhcpv4Conformance": bcnDhcpv4Conformance,
       "bcnDhcpv4ServiceCompliances": bcnDhcpv4ServiceCompliances,
       "bcnDhcpv4StatusCompliance": bcnDhcpv4StatusCompliance,
       "bcnDhcpv4ServiceGroups": bcnDhcpv4ServiceGroups,
       "bcnDhcpv4ServiceStatusGroup": bcnDhcpv4ServiceStatusGroup,
       "bcnDhcpv4StatisticsGroup": bcnDhcpv4StatisticsGroup,
       "bcnDhcpv4NotificationEventGroup": bcnDhcpv4NotificationEventGroup,
       "bcnDhcpv4NotificationDataGroup": bcnDhcpv4NotificationDataGroup}
)
