# SNMP MIB module (ADONIS-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\ADONIS-DNS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:23 2025
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

(appliances,) = mibBuilder.importSymbols(
    "BLUECATNETWORKS-MIB",
    "appliances")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adonis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdonisObjects_ObjectIdentity = ObjectIdentity
adonisObjects = _AdonisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1)
)
_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1)
)
_DnsDaemon_ObjectIdentity = ObjectIdentity
dnsDaemon = _DnsDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1)
)
_DnsDaemonRunning_Type = Integer32
_DnsDaemonRunning_Object = MibScalar
dnsDaemonRunning = _DnsDaemonRunning_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 1),
    _DnsDaemonRunning_Type()
)
dnsDaemonRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonRunning.setStatus("current")
_DnsDaemonNumberOfZones_Type = Gauge32
_DnsDaemonNumberOfZones_Object = MibScalar
dnsDaemonNumberOfZones = _DnsDaemonNumberOfZones_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 2),
    _DnsDaemonNumberOfZones_Type()
)
dnsDaemonNumberOfZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonNumberOfZones.setStatus("current")
_DnsDaemonDebugLevel_Type = Gauge32
_DnsDaemonDebugLevel_Object = MibScalar
dnsDaemonDebugLevel = _DnsDaemonDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 3),
    _DnsDaemonDebugLevel_Type()
)
dnsDaemonDebugLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonDebugLevel.setStatus("current")
_DnsDaemonZoneTransfersInProgress_Type = Gauge32
_DnsDaemonZoneTransfersInProgress_Object = MibScalar
dnsDaemonZoneTransfersInProgress = _DnsDaemonZoneTransfersInProgress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 4),
    _DnsDaemonZoneTransfersInProgress_Type()
)
dnsDaemonZoneTransfersInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonZoneTransfersInProgress.setStatus("current")
_DnsDaemonZoneTransfersDeferred_Type = Gauge32
_DnsDaemonZoneTransfersDeferred_Object = MibScalar
dnsDaemonZoneTransfersDeferred = _DnsDaemonZoneTransfersDeferred_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 5),
    _DnsDaemonZoneTransfersDeferred_Type()
)
dnsDaemonZoneTransfersDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonZoneTransfersDeferred.setStatus("current")
_DnsDaemonSOAQueriesInProgress_Type = Gauge32
_DnsDaemonSOAQueriesInProgress_Object = MibScalar
dnsDaemonSOAQueriesInProgress = _DnsDaemonSOAQueriesInProgress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 6),
    _DnsDaemonSOAQueriesInProgress_Type()
)
dnsDaemonSOAQueriesInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonSOAQueriesInProgress.setStatus("current")


class _DnsDaemonQueryLoggingState_Type(Integer32):
    """Custom type dnsDaemonQueryLoggingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DnsDaemonQueryLoggingState_Type.__name__ = "Integer32"
_DnsDaemonQueryLoggingState_Object = MibScalar
dnsDaemonQueryLoggingState = _DnsDaemonQueryLoggingState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 7),
    _DnsDaemonQueryLoggingState_Type()
)
dnsDaemonQueryLoggingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonQueryLoggingState.setStatus("current")
_DnsDaemonZoneTransferFailure_Type = OctetString
_DnsDaemonZoneTransferFailure_Object = MibScalar
dnsDaemonZoneTransferFailure = _DnsDaemonZoneTransferFailure_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 8),
    _DnsDaemonZoneTransferFailure_Type()
)
dnsDaemonZoneTransferFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDaemonZoneTransferFailure.setStatus("current")
_DnsStats_ObjectIdentity = ObjectIdentity
dnsStats = _DnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2)
)
_DnsStatsSuccess_Type = Counter64
_DnsStatsSuccess_Object = MibScalar
dnsStatsSuccess = _DnsStatsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 1),
    _DnsStatsSuccess_Type()
)
dnsStatsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatsSuccess.setStatus("current")
_DnsStatsReferral_Type = Counter64
_DnsStatsReferral_Object = MibScalar
dnsStatsReferral = _DnsStatsReferral_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 2),
    _DnsStatsReferral_Type()
)
dnsStatsReferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatsReferral.setStatus("current")
_DnsStatsNXRRSet_Type = Counter64
_DnsStatsNXRRSet_Object = MibScalar
dnsStatsNXRRSet = _DnsStatsNXRRSet_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 3),
    _DnsStatsNXRRSet_Type()
)
dnsStatsNXRRSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatsNXRRSet.setStatus("current")
_DnsStatsNXDomain_Type = Counter64
_DnsStatsNXDomain_Object = MibScalar
dnsStatsNXDomain = _DnsStatsNXDomain_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 4),
    _DnsStatsNXDomain_Type()
)
dnsStatsNXDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatsNXDomain.setStatus("current")
_DnsStatsRecursion_Type = Counter64
_DnsStatsRecursion_Object = MibScalar
dnsStatsRecursion = _DnsStatsRecursion_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 5),
    _DnsStatsRecursion_Type()
)
dnsStatsRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatsRecursion.setStatus("current")
_DnsStatsFailure_Type = Counter64
_DnsStatsFailure_Object = MibScalar
dnsStatsFailure = _DnsStatsFailure_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 6),
    _DnsStatsFailure_Type()
)
dnsStatsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatsFailure.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2)
)
_DhcpDaemon_ObjectIdentity = ObjectIdentity
dhcpDaemon = _DhcpDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1)
)
_DhcpDaemonRunning_Type = Integer32
_DhcpDaemonRunning_Object = MibScalar
dhcpDaemonRunning = _DhcpDaemonRunning_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 1),
    _DhcpDaemonRunning_Type()
)
dhcpDaemonRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDaemonRunning.setStatus("current")
_DhcpDaemonSubnetAlert_Type = IpAddress
_DhcpDaemonSubnetAlert_Object = MibScalar
dhcpDaemonSubnetAlert = _DhcpDaemonSubnetAlert_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 2),
    _DhcpDaemonSubnetAlert_Type()
)
dhcpDaemonSubnetAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDaemonSubnetAlert.setStatus("current")
_DhcpDaemonLeaseStatsSuccess_Type = Integer32
_DhcpDaemonLeaseStatsSuccess_Object = MibScalar
dhcpDaemonLeaseStatsSuccess = _DhcpDaemonLeaseStatsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 3),
    _DhcpDaemonLeaseStatsSuccess_Type()
)
dhcpDaemonLeaseStatsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDaemonLeaseStatsSuccess.setStatus("current")
_DhcpFailOverState_Type = Integer32
_DhcpFailOverState_Object = MibScalar
dhcpFailOverState = _DhcpFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 4),
    _DhcpFailOverState_Type()
)
dhcpFailOverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpFailOverState.setStatus("current")
_DhcpStats_ObjectIdentity = ObjectIdentity
dhcpStats = _DhcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2)
)
_DhcpLeaseTable_Object = MibTable
dhcpLeaseTable = _DhcpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpLeaseTable.setStatus("current")
_DhcpLeaseEntry_Object = MibTableRow
dhcpLeaseEntry = _DhcpLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1)
)
dhcpLeaseEntry.setIndexNames(
    (0, "ADONIS-DNS-MIB", "dhcpIP"),
)
if mibBuilder.loadTexts:
    dhcpLeaseEntry.setStatus("current")
_DhcpIP_Type = IpAddress
_DhcpIP_Object = MibTableColumn
dhcpIP = _DhcpIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 1),
    _DhcpIP_Type()
)
dhcpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIP.setStatus("current")
_DhcpLeaseStartTime_Type = Unsigned32
_DhcpLeaseStartTime_Object = MibTableColumn
dhcpLeaseStartTime = _DhcpLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 2),
    _DhcpLeaseStartTime_Type()
)
dhcpLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseStartTime.setStatus("current")
_DhcpLeaseEndTime_Type = Unsigned32
_DhcpLeaseEndTime_Object = MibTableColumn
dhcpLeaseEndTime = _DhcpLeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 3),
    _DhcpLeaseEndTime_Type()
)
dhcpLeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseEndTime.setStatus("current")
_DhcpLeaseTimeStamp_Type = Unsigned32
_DhcpLeaseTimeStamp_Object = MibTableColumn
dhcpLeaseTimeStamp = _DhcpLeaseTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 4),
    _DhcpLeaseTimeStamp_Type()
)
dhcpLeaseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseTimeStamp.setStatus("current")


class _DhcpLeaseBindState_Type(Integer32):
    """Custom type dhcpLeaseBindState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("free", 0),
          ("active", 1),
          ("fixed", 2))
    )


_DhcpLeaseBindState_Type.__name__ = "Integer32"
_DhcpLeaseBindState_Object = MibTableColumn
dhcpLeaseBindState = _DhcpLeaseBindState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 5),
    _DhcpLeaseBindState_Type()
)
dhcpLeaseBindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseBindState.setStatus("current")
_DhcpLeaseHardwareAddress_Type = OctetString
_DhcpLeaseHardwareAddress_Object = MibTableColumn
dhcpLeaseHardwareAddress = _DhcpLeaseHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 6),
    _DhcpLeaseHardwareAddress_Type()
)
dhcpLeaseHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseHardwareAddress.setStatus("current")
_DhcpLeaseHostname_Type = OctetString
_DhcpLeaseHostname_Object = MibTableColumn
dhcpLeaseHostname = _DhcpLeaseHostname_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 7),
    _DhcpLeaseHostname_Type()
)
dhcpLeaseHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseHostname.setStatus("current")
_DhcpSubnetTable_Object = MibTable
dhcpSubnetTable = _DhcpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpSubnetTable.setStatus("current")
_DhcpSubnetEntry_Object = MibTableRow
dhcpSubnetEntry = _DhcpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1)
)
dhcpSubnetEntry.setIndexNames(
    (0, "ADONIS-DNS-MIB", "dhcpSubnetIP"),
)
if mibBuilder.loadTexts:
    dhcpSubnetEntry.setStatus("current")
_DhcpSubnetIP_Type = IpAddress
_DhcpSubnetIP_Object = MibTableColumn
dhcpSubnetIP = _DhcpSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 1),
    _DhcpSubnetIP_Type()
)
dhcpSubnetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetIP.setStatus("current")
_DhcpSubnetMask_Type = IpAddress
_DhcpSubnetMask_Object = MibTableColumn
dhcpSubnetMask = _DhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 2),
    _DhcpSubnetMask_Type()
)
dhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetMask.setStatus("current")
_DhcpSubnetSize_Type = Unsigned32
_DhcpSubnetSize_Object = MibTableColumn
dhcpSubnetSize = _DhcpSubnetSize_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 3),
    _DhcpSubnetSize_Type()
)
dhcpSubnetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetSize.setStatus("current")
_DhcpSubnetUsed_Type = Unsigned32
_DhcpSubnetUsed_Object = MibTableColumn
dhcpSubnetUsed = _DhcpSubnetUsed_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 4),
    _DhcpSubnetUsed_Type()
)
dhcpSubnetUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetUsed.setStatus("current")
_DhcpSubnetAlert_Type = Unsigned32
_DhcpSubnetAlert_Object = MibTableColumn
dhcpSubnetAlert = _DhcpSubnetAlert_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 5),
    _DhcpSubnetAlert_Type()
)
dhcpSubnetAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetAlert.setStatus("current")
_DhcpPoolTable_Object = MibTable
dhcpPoolTable = _DhcpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dhcpPoolTable.setStatus("current")
_DhcpPoolEntry_Object = MibTableRow
dhcpPoolEntry = _DhcpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1)
)
dhcpPoolEntry.setIndexNames(
    (0, "ADONIS-DNS-MIB", "dhcpPoolStartIP"),
)
if mibBuilder.loadTexts:
    dhcpPoolEntry.setStatus("current")
_DhcpPoolSubnetIP_Type = IpAddress
_DhcpPoolSubnetIP_Object = MibTableColumn
dhcpPoolSubnetIP = _DhcpPoolSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 1),
    _DhcpPoolSubnetIP_Type()
)
dhcpPoolSubnetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPoolSubnetIP.setStatus("current")
_DhcpPoolStartIP_Type = IpAddress
_DhcpPoolStartIP_Object = MibTableColumn
dhcpPoolStartIP = _DhcpPoolStartIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 2),
    _DhcpPoolStartIP_Type()
)
dhcpPoolStartIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPoolStartIP.setStatus("current")
_DhcpPoolEndIP_Type = IpAddress
_DhcpPoolEndIP_Object = MibTableColumn
dhcpPoolEndIP = _DhcpPoolEndIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 3),
    _DhcpPoolEndIP_Type()
)
dhcpPoolEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPoolEndIP.setStatus("current")
_DhcpPoolSize_Type = Unsigned32
_DhcpPoolSize_Object = MibTableColumn
dhcpPoolSize = _DhcpPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 4),
    _DhcpPoolSize_Type()
)
dhcpPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPoolSize.setStatus("current")
_DhcpPoolUsed_Type = Unsigned32
_DhcpPoolUsed_Object = MibTableColumn
dhcpPoolUsed = _DhcpPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 5),
    _DhcpPoolUsed_Type()
)
dhcpPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPoolUsed.setStatus("current")
_DhcpPoolAlert_Type = Unsigned32
_DhcpPoolAlert_Object = MibTableColumn
dhcpPoolAlert = _DhcpPoolAlert_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 6),
    _DhcpPoolAlert_Type()
)
dhcpPoolAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPoolAlert.setStatus("current")
_DhcpConfig_ObjectIdentity = ObjectIdentity
dhcpConfig = _DhcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3)
)
_DhcpFixedIPTable_Object = MibTable
dhcpFixedIPTable = _DhcpFixedIPTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpFixedIPTable.setStatus("current")
_DhcpFixedIPEntry_Object = MibTableRow
dhcpFixedIPEntry = _DhcpFixedIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1, 1)
)
dhcpFixedIPEntry.setIndexNames(
    (0, "ADONIS-DNS-MIB", "dhcpFixedIP"),
)
if mibBuilder.loadTexts:
    dhcpFixedIPEntry.setStatus("current")
_DhcpFixedIP_Type = IpAddress
_DhcpFixedIP_Object = MibTableColumn
dhcpFixedIP = _DhcpFixedIP_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1, 1, 1),
    _DhcpFixedIP_Type()
)
dhcpFixedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpFixedIP.setStatus("current")
_Ha_ObjectIdentity = ObjectIdentity
ha = _Ha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3)
)
_HaService_ObjectIdentity = ObjectIdentity
haService = _HaService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1)
)


class _HaServiceRunning_Type(Integer32):
    """Custom type haServiceRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HaServiceRunning_Type.__name__ = "Integer32"
_HaServiceRunning_Object = MibScalar
haServiceRunning = _HaServiceRunning_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 1),
    _HaServiceRunning_Type()
)
haServiceRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haServiceRunning.setStatus("current")


class _HaServiceNodeType_Type(Integer32):
    """Custom type haServiceNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HaServiceNodeType_Type.__name__ = "Integer32"
_HaServiceNodeType_Object = MibScalar
haServiceNodeType = _HaServiceNodeType_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 2),
    _HaServiceNodeType_Type()
)
haServiceNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haServiceNodeType.setStatus("current")


class _HaReplicationBinding_Type(Integer32):
    """Custom type haReplicationBinding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HaReplicationBinding_Type.__name__ = "Integer32"
_HaReplicationBinding_Object = MibScalar
haReplicationBinding = _HaReplicationBinding_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 3),
    _HaReplicationBinding_Type()
)
haReplicationBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haReplicationBinding.setStatus("current")
_CommandServer_ObjectIdentity = ObjectIdentity
commandServer = _CommandServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4)
)
_CommandServerDaemon_ObjectIdentity = ObjectIdentity
commandServerDaemon = _CommandServerDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4, 1)
)


class _CommandServerDaemonRunning_Type(Integer32):
    """Custom type commandServerDaemonRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CommandServerDaemonRunning_Type.__name__ = "Integer32"
_CommandServerDaemonRunning_Object = MibScalar
commandServerDaemonRunning = _CommandServerDaemonRunning_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4, 1, 1),
    _CommandServerDaemonRunning_Type()
)
commandServerDaemonRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandServerDaemonRunning.setStatus("current")
_Lcd_ObjectIdentity = ObjectIdentity
lcd = _Lcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5)
)
_LcdDaemon_ObjectIdentity = ObjectIdentity
lcdDaemon = _LcdDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1)
)


class _LicenseValid_Type(Integer32):
    """Custom type licenseValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LicenseValid_Type.__name__ = "Integer32"
_LicenseValid_Object = MibScalar
licenseValid = _LicenseValid_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1, 1),
    _LicenseValid_Type()
)
licenseValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseValid.setStatus("current")
_LicenseExpiry_Type = Gauge32
_LicenseExpiry_Object = MibScalar
licenseExpiry = _LicenseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1, 2),
    _LicenseExpiry_Type()
)
licenseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpiry.setStatus("current")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6)
)
_TftpDaemon_ObjectIdentity = ObjectIdentity
tftpDaemon = _TftpDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6, 1)
)


class _TftpDaemonRunning_Type(Integer32):
    """Custom type tftpDaemonRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TftpDaemonRunning_Type.__name__ = "Integer32"
_TftpDaemonRunning_Object = MibScalar
tftpDaemonRunning = _TftpDaemonRunning_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6, 1, 1),
    _TftpDaemonRunning_Type()
)
tftpDaemonRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpDaemonRunning.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7)
)
_SystemDaemon_ObjectIdentity = ObjectIdentity
systemDaemon = _SystemDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7, 1)
)


class _SystemState_Type(Integer32):
    """Custom type systemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SystemState_Type.__name__ = "Integer32"
_SystemState_Object = MibScalar
systemState = _SystemState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7, 1, 1),
    _SystemState_Type()
)
systemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemState.setStatus("current")
_AdonisTraps_ObjectIdentity = ObjectIdentity
adonisTraps = _AdonisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2)
)
_TrapDNS_ObjectIdentity = ObjectIdentity
trapDNS = _TrapDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 1)
)
_TrapHA_ObjectIdentity = ObjectIdentity
trapHA = _TrapHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 2)
)
_TrapCommandServer_ObjectIdentity = ObjectIdentity
trapCommandServer = _TrapCommandServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 3)
)
_TrapDHCP_ObjectIdentity = ObjectIdentity
trapDHCP = _TrapDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 4)
)
_TrapReplication_ObjectIdentity = ObjectIdentity
trapReplication = _TrapReplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 5)
)
_TrapTFTP_ObjectIdentity = ObjectIdentity
trapTFTP = _TrapTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 6)
)
_TrapSystem_ObjectIdentity = ObjectIdentity
trapSystem = _TrapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 7)
)

# Managed Objects groups


# Notification objects

trapDNSDaemon = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 1, 1)
)
trapDNSDaemon.setObjects(
      *(("ADONIS-DNS-MIB", "dnsDaemonRunning"),
        ("ADONIS-DNS-MIB", "dnsDaemonZoneTransferFailure"))
)
if mibBuilder.loadTexts:
    trapDNSDaemon.setStatus(
        "current"
    )

trapHAServiceFailOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 2, 1)
)
trapHAServiceFailOver.setObjects(
    ("ADONIS-DNS-MIB", "haServiceNodeType")
)
if mibBuilder.loadTexts:
    trapHAServiceFailOver.setStatus(
        "current"
    )

trapCommandServerDaemon = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 3, 1)
)
trapCommandServerDaemon.setObjects(
    ("ADONIS-DNS-MIB", "commandServerDaemonRunning")
)
if mibBuilder.loadTexts:
    trapCommandServerDaemon.setStatus(
        "current"
    )

trapDHCPDaemon = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 4, 1)
)
trapDHCPDaemon.setObjects(
      *(("ADONIS-DNS-MIB", "dhcpDaemonRunning"),
        ("ADONIS-DNS-MIB", "dhcpDaemonSubnetAlert"),
        ("ADONIS-DNS-MIB", "dhcpFailOverState"))
)
if mibBuilder.loadTexts:
    trapDHCPDaemon.setStatus(
        "current"
    )

trapReplicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 5, 1)
)
if mibBuilder.loadTexts:
    trapReplicationFailure.setStatus(
        "current"
    )

trapTFTPDaemon = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 6, 1)
)
trapTFTPDaemon.setObjects(
    ("ADONIS-DNS-MIB", "tftpDaemonRunning")
)
if mibBuilder.loadTexts:
    trapTFTPDaemon.setStatus(
        "current"
    )

trapSystemDaemon = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 7, 1)
)
trapSystemDaemon.setObjects(
    ("ADONIS-DNS-MIB", "systemState")
)
if mibBuilder.loadTexts:
    trapSystemDaemon.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADONIS-DNS-MIB",
    **{"adonis": adonis,
       "adonisObjects": adonisObjects,
       "dns": dns,
       "dnsDaemon": dnsDaemon,
       "dnsDaemonRunning": dnsDaemonRunning,
       "dnsDaemonNumberOfZones": dnsDaemonNumberOfZones,
       "dnsDaemonDebugLevel": dnsDaemonDebugLevel,
       "dnsDaemonZoneTransfersInProgress": dnsDaemonZoneTransfersInProgress,
       "dnsDaemonZoneTransfersDeferred": dnsDaemonZoneTransfersDeferred,
       "dnsDaemonSOAQueriesInProgress": dnsDaemonSOAQueriesInProgress,
       "dnsDaemonQueryLoggingState": dnsDaemonQueryLoggingState,
       "dnsDaemonZoneTransferFailure": dnsDaemonZoneTransferFailure,
       "dnsStats": dnsStats,
       "dnsStatsSuccess": dnsStatsSuccess,
       "dnsStatsReferral": dnsStatsReferral,
       "dnsStatsNXRRSet": dnsStatsNXRRSet,
       "dnsStatsNXDomain": dnsStatsNXDomain,
       "dnsStatsRecursion": dnsStatsRecursion,
       "dnsStatsFailure": dnsStatsFailure,
       "dhcp": dhcp,
       "dhcpDaemon": dhcpDaemon,
       "dhcpDaemonRunning": dhcpDaemonRunning,
       "dhcpDaemonSubnetAlert": dhcpDaemonSubnetAlert,
       "dhcpDaemonLeaseStatsSuccess": dhcpDaemonLeaseStatsSuccess,
       "dhcpFailOverState": dhcpFailOverState,
       "dhcpStats": dhcpStats,
       "dhcpLeaseTable": dhcpLeaseTable,
       "dhcpLeaseEntry": dhcpLeaseEntry,
       "dhcpIP": dhcpIP,
       "dhcpLeaseStartTime": dhcpLeaseStartTime,
       "dhcpLeaseEndTime": dhcpLeaseEndTime,
       "dhcpLeaseTimeStamp": dhcpLeaseTimeStamp,
       "dhcpLeaseBindState": dhcpLeaseBindState,
       "dhcpLeaseHardwareAddress": dhcpLeaseHardwareAddress,
       "dhcpLeaseHostname": dhcpLeaseHostname,
       "dhcpSubnetTable": dhcpSubnetTable,
       "dhcpSubnetEntry": dhcpSubnetEntry,
       "dhcpSubnetIP": dhcpSubnetIP,
       "dhcpSubnetMask": dhcpSubnetMask,
       "dhcpSubnetSize": dhcpSubnetSize,
       "dhcpSubnetUsed": dhcpSubnetUsed,
       "dhcpSubnetAlert": dhcpSubnetAlert,
       "dhcpPoolTable": dhcpPoolTable,
       "dhcpPoolEntry": dhcpPoolEntry,
       "dhcpPoolSubnetIP": dhcpPoolSubnetIP,
       "dhcpPoolStartIP": dhcpPoolStartIP,
       "dhcpPoolEndIP": dhcpPoolEndIP,
       "dhcpPoolSize": dhcpPoolSize,
       "dhcpPoolUsed": dhcpPoolUsed,
       "dhcpPoolAlert": dhcpPoolAlert,
       "dhcpConfig": dhcpConfig,
       "dhcpFixedIPTable": dhcpFixedIPTable,
       "dhcpFixedIPEntry": dhcpFixedIPEntry,
       "dhcpFixedIP": dhcpFixedIP,
       "ha": ha,
       "haService": haService,
       "haServiceRunning": haServiceRunning,
       "haServiceNodeType": haServiceNodeType,
       "haReplicationBinding": haReplicationBinding,
       "commandServer": commandServer,
       "commandServerDaemon": commandServerDaemon,
       "commandServerDaemonRunning": commandServerDaemonRunning,
       "lcd": lcd,
       "lcdDaemon": lcdDaemon,
       "licenseValid": licenseValid,
       "licenseExpiry": licenseExpiry,
       "tftp": tftp,
       "tftpDaemon": tftpDaemon,
       "tftpDaemonRunning": tftpDaemonRunning,
       "system": system,
       "systemDaemon": systemDaemon,
       "systemState": systemState,
       "adonisTraps": adonisTraps,
       "trapDNS": trapDNS,
       "trapDNSDaemon": trapDNSDaemon,
       "trapHA": trapHA,
       "trapHAServiceFailOver": trapHAServiceFailOver,
       "trapCommandServer": trapCommandServer,
       "trapCommandServerDaemon": trapCommandServerDaemon,
       "trapDHCP": trapDHCP,
       "trapDHCPDaemon": trapDHCPDaemon,
       "trapReplication": trapReplication,
       "trapReplicationFailure": trapReplicationFailure,
       "trapTFTP": trapTFTP,
       "trapTFTPDaemon": trapTFTPDaemon,
       "trapSystem": trapSystem,
       "trapSystemDaemon": trapSystemDaemon}
)
