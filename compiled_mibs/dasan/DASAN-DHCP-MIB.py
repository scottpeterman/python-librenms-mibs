# SNMP MIB module (DASAN-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-DHCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:01 2025
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

(dasanMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanMgmt")

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
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

dsDhcpMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SubnetConfIndex(TextualConvention, Integer32):
    status = "current"


class SubnetConfRangeIndex(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Dasan_ObjectIdentity = ObjectIdentity
dasan = _Dasan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296)
)
_DasanSwitchMIB_ObjectIdentity = ObjectIdentity
dasanSwitchMIB = _DasanSwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1)
)
_DasanSwitchMIBObjects_ObjectIdentity = ObjectIdentity
dasanSwitchMIBObjects = _DasanSwitchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1)
)
_DsDhcpDaemonConf_ObjectIdentity = ObjectIdentity
dsDhcpDaemonConf = _DsDhcpDaemonConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1)
)
_DsDefaultLeaseTime_Type = Integer32
_DsDefaultLeaseTime_Object = MibScalar
dsDefaultLeaseTime = _DsDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 1),
    _DsDefaultLeaseTime_Type()
)
dsDefaultLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDefaultLeaseTime.setStatus("mandatory")
_DsMaxLeaseTime_Type = Integer32
_DsMaxLeaseTime_Object = MibScalar
dsMaxLeaseTime = _DsMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 2),
    _DsMaxLeaseTime_Type()
)
dsMaxLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMaxLeaseTime.setStatus("mandatory")
_DsSubnetMask_Type = IpAddress
_DsSubnetMask_Object = MibScalar
dsSubnetMask = _DsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 3),
    _DsSubnetMask_Type()
)
dsSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetMask.setStatus("mandatory")
_DsBroadcastAddress_Type = IpAddress
_DsBroadcastAddress_Object = MibScalar
dsBroadcastAddress = _DsBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 4),
    _DsBroadcastAddress_Type()
)
dsBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsBroadcastAddress.setStatus("obsolete")
_DsDomainName_Type = DisplayString
_DsDomainName_Object = MibScalar
dsDomainName = _DsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 5),
    _DsDomainName_Type()
)
dsDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDomainName.setStatus("mandatory")
_DsDomainNameServerTable_Object = MibTable
dsDomainNameServerTable = _DsDomainNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    dsDomainNameServerTable.setStatus("mandatory")
_DsDomainNameServerEntry_Object = MibTableRow
dsDomainNameServerEntry = _DsDomainNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 6, 1)
)
dsDomainNameServerEntry.setIndexNames(
    (0, "DASAN-DHCP-MIB", "dsDomainNameServerIpIdx"),
)
if mibBuilder.loadTexts:
    dsDomainNameServerEntry.setStatus("mandatory")
_DsDomainNameServerIpIdx_Type = Integer32
_DsDomainNameServerIpIdx_Object = MibTableColumn
dsDomainNameServerIpIdx = _DsDomainNameServerIpIdx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 6, 1, 1),
    _DsDomainNameServerIpIdx_Type()
)
dsDomainNameServerIpIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDomainNameServerIpIdx.setStatus("mandatory")
_DsDomainNameServerIp_Type = IpAddress
_DsDomainNameServerIp_Object = MibTableColumn
dsDomainNameServerIp = _DsDomainNameServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 6, 1, 2),
    _DsDomainNameServerIp_Type()
)
dsDomainNameServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDomainNameServerIp.setStatus("mandatory")
_DsSubnetConfTable_Object = MibTable
dsSubnetConfTable = _DsSubnetConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    dsSubnetConfTable.setStatus("mandatory")
_DsSubnetConfEntry_Object = MibTableRow
dsSubnetConfEntry = _DsSubnetConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1)
)
dsSubnetConfEntry.setIndexNames(
    (0, "DASAN-DHCP-MIB", "dsSubnetConfIndex"),
)
if mibBuilder.loadTexts:
    dsSubnetConfEntry.setStatus("mandatory")
_DsSubnetConfName_Type = DisplayString
_DsSubnetConfName_Object = MibTableColumn
dsSubnetConfName = _DsSubnetConfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 1),
    _DsSubnetConfName_Type()
)
dsSubnetConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfName.setStatus("mandatory")
_DsSubnetConfSubnet_Type = IpAddress
_DsSubnetConfSubnet_Object = MibTableColumn
dsSubnetConfSubnet = _DsSubnetConfSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 2),
    _DsSubnetConfSubnet_Type()
)
dsSubnetConfSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfSubnet.setStatus("mandatory")
_DsSubnetConfNetmask_Type = IpAddress
_DsSubnetConfNetmask_Object = MibTableColumn
dsSubnetConfNetmask = _DsSubnetConfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 3),
    _DsSubnetConfNetmask_Type()
)
dsSubnetConfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfNetmask.setStatus("mandatory")
_DsSubnetConfBroadcastAddr_Type = IpAddress
_DsSubnetConfBroadcastAddr_Object = MibTableColumn
dsSubnetConfBroadcastAddr = _DsSubnetConfBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 4),
    _DsSubnetConfBroadcastAddr_Type()
)
dsSubnetConfBroadcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfBroadcastAddr.setStatus("obsolete")
_DsSubnetConfDefaultLeaseTime_Type = Integer32
_DsSubnetConfDefaultLeaseTime_Object = MibTableColumn
dsSubnetConfDefaultLeaseTime = _DsSubnetConfDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 5),
    _DsSubnetConfDefaultLeaseTime_Type()
)
dsSubnetConfDefaultLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfDefaultLeaseTime.setStatus("mandatory")
_DsSubnetConfMaxLeaseTime_Type = Integer32
_DsSubnetConfMaxLeaseTime_Object = MibTableColumn
dsSubnetConfMaxLeaseTime = _DsSubnetConfMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 6),
    _DsSubnetConfMaxLeaseTime_Type()
)
dsSubnetConfMaxLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfMaxLeaseTime.setStatus("mandatory")
_DsSubnetConfTotalCount_Type = Integer32
_DsSubnetConfTotalCount_Object = MibTableColumn
dsSubnetConfTotalCount = _DsSubnetConfTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 7),
    _DsSubnetConfTotalCount_Type()
)
dsSubnetConfTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfTotalCount.setStatus("mandatory")
_DsSubnetConfAllocatedCount_Type = Integer32
_DsSubnetConfAllocatedCount_Object = MibTableColumn
dsSubnetConfAllocatedCount = _DsSubnetConfAllocatedCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 8),
    _DsSubnetConfAllocatedCount_Type()
)
dsSubnetConfAllocatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfAllocatedCount.setStatus("mandatory")
_DsSubnetConfRouters_Type = IpAddress
_DsSubnetConfRouters_Object = MibTableColumn
dsSubnetConfRouters = _DsSubnetConfRouters_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 9),
    _DsSubnetConfRouters_Type()
)
dsSubnetConfRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfRouters.setStatus("mandatory")


class _DsSubnetConfRangeBitmap_Type(OctetString):
    """Custom type dsSubnetConfRangeBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsSubnetConfRangeBitmap_Type.__name__ = "OctetString"
_DsSubnetConfRangeBitmap_Object = MibTableColumn
dsSubnetConfRangeBitmap = _DsSubnetConfRangeBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 10),
    _DsSubnetConfRangeBitmap_Type()
)
dsSubnetConfRangeBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfRangeBitmap.setStatus("obsolete")
_DsSubnetConfIndex_Type = SubnetConfIndex
_DsSubnetConfIndex_Object = MibTableColumn
dsSubnetConfIndex = _DsSubnetConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 11),
    _DsSubnetConfIndex_Type()
)
dsSubnetConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsSubnetConfIndex.setStatus("mandatory")


class _DsSubnetConfDomainName_Type(OctetString):
    """Custom type dsSubnetConfDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DsSubnetConfDomainName_Type.__name__ = "OctetString"
_DsSubnetConfDomainName_Object = MibTableColumn
dsSubnetConfDomainName = _DsSubnetConfDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 7, 1, 12),
    _DsSubnetConfDomainName_Type()
)
dsSubnetConfDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfDomainName.setStatus("mandatory")
_DsSubnetConfRangeTable_Object = MibTable
dsSubnetConfRangeTable = _DsSubnetConfRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    dsSubnetConfRangeTable.setStatus("mandatory")
_DsSubnetConfRangeEntry_Object = MibTableRow
dsSubnetConfRangeEntry = _DsSubnetConfRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 8, 1)
)
dsSubnetConfRangeEntry.setIndexNames(
    (0, "DASAN-DHCP-MIB", "dsSubnetConfIndex"),
    (0, "DASAN-DHCP-MIB", "dsSubnetConfRangeIndex"),
)
if mibBuilder.loadTexts:
    dsSubnetConfRangeEntry.setStatus("mandatory")
_DsSubnetConfRangeStart_Type = IpAddress
_DsSubnetConfRangeStart_Object = MibTableColumn
dsSubnetConfRangeStart = _DsSubnetConfRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 8, 1, 1),
    _DsSubnetConfRangeStart_Type()
)
dsSubnetConfRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfRangeStart.setStatus("mandatory")
_DsSubnetConfRangeEnd_Type = IpAddress
_DsSubnetConfRangeEnd_Object = MibTableColumn
dsSubnetConfRangeEnd = _DsSubnetConfRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 8, 1, 2),
    _DsSubnetConfRangeEnd_Type()
)
dsSubnetConfRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSubnetConfRangeEnd.setStatus("mandatory")
_DsSubnetConfRangeIndex_Type = SubnetConfRangeIndex
_DsSubnetConfRangeIndex_Object = MibTableColumn
dsSubnetConfRangeIndex = _DsSubnetConfRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 1, 1, 5, 1, 8, 1, 3),
    _DsSubnetConfRangeIndex_Type()
)
dsSubnetConfRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsSubnetConfRangeIndex.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 5)
)
_SnmpV2_ObjectIdentity = ObjectIdentity
snmpV2 = _SnmpV2_ObjectIdentity(
    (1, 3, 6, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-DHCP-MIB",
    **{"SubnetConfIndex": SubnetConfIndex,
       "SubnetConfRangeIndex": SubnetConfRangeIndex,
       "org": org,
       "dod": dod,
       "internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "transmission": transmission,
       "experimental": experimental,
       "private": private,
       "dasan": dasan,
       "dasanSwitchMIB": dasanSwitchMIB,
       "dasanSwitchMIBObjects": dasanSwitchMIBObjects,
       "dsDhcpMIBObjects": dsDhcpMIBObjects,
       "dsDhcpDaemonConf": dsDhcpDaemonConf,
       "dsDefaultLeaseTime": dsDefaultLeaseTime,
       "dsMaxLeaseTime": dsMaxLeaseTime,
       "dsSubnetMask": dsSubnetMask,
       "dsBroadcastAddress": dsBroadcastAddress,
       "dsDomainName": dsDomainName,
       "dsDomainNameServerTable": dsDomainNameServerTable,
       "dsDomainNameServerEntry": dsDomainNameServerEntry,
       "dsDomainNameServerIpIdx": dsDomainNameServerIpIdx,
       "dsDomainNameServerIp": dsDomainNameServerIp,
       "dsSubnetConfTable": dsSubnetConfTable,
       "dsSubnetConfEntry": dsSubnetConfEntry,
       "dsSubnetConfName": dsSubnetConfName,
       "dsSubnetConfSubnet": dsSubnetConfSubnet,
       "dsSubnetConfNetmask": dsSubnetConfNetmask,
       "dsSubnetConfBroadcastAddr": dsSubnetConfBroadcastAddr,
       "dsSubnetConfDefaultLeaseTime": dsSubnetConfDefaultLeaseTime,
       "dsSubnetConfMaxLeaseTime": dsSubnetConfMaxLeaseTime,
       "dsSubnetConfTotalCount": dsSubnetConfTotalCount,
       "dsSubnetConfAllocatedCount": dsSubnetConfAllocatedCount,
       "dsSubnetConfRouters": dsSubnetConfRouters,
       "dsSubnetConfRangeBitmap": dsSubnetConfRangeBitmap,
       "dsSubnetConfIndex": dsSubnetConfIndex,
       "dsSubnetConfDomainName": dsSubnetConfDomainName,
       "dsSubnetConfRangeTable": dsSubnetConfRangeTable,
       "dsSubnetConfRangeEntry": dsSubnetConfRangeEntry,
       "dsSubnetConfRangeStart": dsSubnetConfRangeStart,
       "dsSubnetConfRangeEnd": dsSubnetConfRangeEnd,
       "dsSubnetConfRangeIndex": dsSubnetConfRangeIndex,
       "security": security,
       "snmpV2": snmpV2}
)
