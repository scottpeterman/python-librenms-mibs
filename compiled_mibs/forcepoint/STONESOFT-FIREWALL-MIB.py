# SNMP MIB module (STONESOFT-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\forcepoint\STONESOFT-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:41 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")

(stonesoftFirewall,
 stonesoftModules) = mibBuilder.importSymbols(
    "STONESOFT-SMI-MIB",
    "stonesoftFirewall",
    "stonesoftModules")


# MODULE-IDENTITY

stonesoftFirewallMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 3, 3)
)
if mibBuilder.loadTexts:
    stonesoftFirewallMibModule.setRevisions(
        ("2020-11-18 00:00",
         "2017-06-19 00:00",
         "2016-08-17 00:00",
         "2016-05-06 00:00",
         "2014-06-23 00:00",
         "2012-02-01 00:00",
         "2011-10-31 00:00",
         "2011-06-01 00:00",
         "2004-06-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VpnEndpointType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("static", 1),
          ("dynamic", 2),
          ("mobile", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FirewallObjects_ObjectIdentity = ObjectIdentity
firewallObjects = _FirewallObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1)
)
_FwSoftwareVersion_Type = DisplayString
_FwSoftwareVersion_Object = MibScalar
fwSoftwareVersion = _FwSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 1),
    _FwSoftwareVersion_Type()
)
fwSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSoftwareVersion.setStatus("current")
_FwSecurityPolicy_Type = DisplayString
_FwSecurityPolicy_Object = MibScalar
fwSecurityPolicy = _FwSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 2),
    _FwSecurityPolicy_Type()
)
fwSecurityPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSecurityPolicy.setStatus("current")
_FwPolicyTime_Type = TimeStamp
_FwPolicyTime_Object = MibScalar
fwPolicyTime = _FwPolicyTime_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 3),
    _FwPolicyTime_Type()
)
fwPolicyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPolicyTime.setStatus("current")
_FwConnNumber_Type = CounterBasedGauge64
_FwConnNumber_Object = MibScalar
fwConnNumber = _FwConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 4),
    _FwConnNumber_Type()
)
fwConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnNumber.setStatus("current")
_FwAccepted_Type = Counter64
_FwAccepted_Object = MibScalar
fwAccepted = _FwAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 5),
    _FwAccepted_Type()
)
fwAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAccepted.setStatus("current")
_FwDropped_Type = Counter64
_FwDropped_Object = MibScalar
fwDropped = _FwDropped_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 6),
    _FwDropped_Type()
)
fwDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropped.setStatus("current")
_FwLogged_Type = Counter64
_FwLogged_Object = MibScalar
fwLogged = _FwLogged_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 7),
    _FwLogged_Type()
)
fwLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogged.setStatus("current")
_FwAccounted_Type = Counter64
_FwAccounted_Object = MibScalar
fwAccounted = _FwAccounted_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 8),
    _FwAccounted_Type()
)
fwAccounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAccounted.setStatus("current")
_FwRejected_Type = Counter64
_FwRejected_Object = MibScalar
fwRejected = _FwRejected_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 9),
    _FwRejected_Type()
)
fwRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejected.setStatus("current")
_FwIfStatsTable_Object = MibTable
fwIfStatsTable = _FwIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    fwIfStatsTable.setStatus("current")
_FwIfStatsEntry_Object = MibTableRow
fwIfStatsEntry = _FwIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1)
)
fwIfStatsEntry.setIndexNames(
    (0, "STONESOFT-FIREWALL-MIB", "fwIfStatsIndex"),
)
if mibBuilder.loadTexts:
    fwIfStatsEntry.setStatus("current")


class _FwIfStatsIndex_Type(Integer32):
    """Custom type fwIfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwIfStatsIndex_Type.__name__ = "Integer32"
_FwIfStatsIndex_Object = MibTableColumn
fwIfStatsIndex = _FwIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 1),
    _FwIfStatsIndex_Type()
)
fwIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwIfStatsIndex.setStatus("current")
_FwIfName_Type = DisplayString
_FwIfName_Object = MibTableColumn
fwIfName = _FwIfName_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 2),
    _FwIfName_Type()
)
fwIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfName.setStatus("current")
_FwIfAcceptedPkts_Type = Counter64
_FwIfAcceptedPkts_Object = MibTableColumn
fwIfAcceptedPkts = _FwIfAcceptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 3),
    _FwIfAcceptedPkts_Type()
)
fwIfAcceptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAcceptedPkts.setStatus("current")
_FwIfDroppedPkts_Type = Counter64
_FwIfDroppedPkts_Object = MibTableColumn
fwIfDroppedPkts = _FwIfDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 4),
    _FwIfDroppedPkts_Type()
)
fwIfDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfDroppedPkts.setStatus("current")
_FwIfLoggedPkts_Type = Counter64
_FwIfLoggedPkts_Object = MibTableColumn
fwIfLoggedPkts = _FwIfLoggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 5),
    _FwIfLoggedPkts_Type()
)
fwIfLoggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfLoggedPkts.setStatus("current")
_FwIfAccountedPkts_Type = Counter64
_FwIfAccountedPkts_Object = MibTableColumn
fwIfAccountedPkts = _FwIfAccountedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 6),
    _FwIfAccountedPkts_Type()
)
fwIfAccountedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAccountedPkts.setStatus("current")
_FwIfRejectedPkts_Type = Counter64
_FwIfRejectedPkts_Object = MibTableColumn
fwIfRejectedPkts = _FwIfRejectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 7),
    _FwIfRejectedPkts_Type()
)
fwIfRejectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfRejectedPkts.setStatus("current")
_FwIfAcceptedBytes_Type = Counter64
_FwIfAcceptedBytes_Object = MibTableColumn
fwIfAcceptedBytes = _FwIfAcceptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 8),
    _FwIfAcceptedBytes_Type()
)
fwIfAcceptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAcceptedBytes.setStatus("current")
_FwIfDroppedBytes_Type = Counter64
_FwIfDroppedBytes_Object = MibTableColumn
fwIfDroppedBytes = _FwIfDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 9),
    _FwIfDroppedBytes_Type()
)
fwIfDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfDroppedBytes.setStatus("current")
_FwIfLoggedBytes_Type = Counter64
_FwIfLoggedBytes_Object = MibTableColumn
fwIfLoggedBytes = _FwIfLoggedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 10),
    _FwIfLoggedBytes_Type()
)
fwIfLoggedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfLoggedBytes.setStatus("current")
_FwIfAccountedBytes_Type = Counter64
_FwIfAccountedBytes_Object = MibTableColumn
fwIfAccountedBytes = _FwIfAccountedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 11),
    _FwIfAccountedBytes_Type()
)
fwIfAccountedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfAccountedBytes.setStatus("current")
_FwIfRejectedBytes_Type = Counter64
_FwIfRejectedBytes_Object = MibTableColumn
fwIfRejectedBytes = _FwIfRejectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 12),
    _FwIfRejectedBytes_Type()
)
fwIfRejectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfRejectedBytes.setStatus("current")
_FwIfForwardedPkts_Type = Counter64
_FwIfForwardedPkts_Object = MibTableColumn
fwIfForwardedPkts = _FwIfForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 13),
    _FwIfForwardedPkts_Type()
)
fwIfForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfForwardedPkts.setStatus("current")
_FwIfForwardedBytes_Type = Counter64
_FwIfForwardedBytes_Object = MibTableColumn
fwIfForwardedBytes = _FwIfForwardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 10, 1, 14),
    _FwIfForwardedBytes_Type()
)
fwIfForwardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfForwardedBytes.setStatus("current")
_FwHardware_ObjectIdentity = ObjectIdentity
fwHardware = _FwHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11)
)
_FwCpuStatsTable_Object = MibTable
fwCpuStatsTable = _FwCpuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    fwCpuStatsTable.setStatus("current")
_FwCpuStatsEntry_Object = MibTableRow
fwCpuStatsEntry = _FwCpuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1)
)
fwCpuStatsEntry.setIndexNames(
    (0, "STONESOFT-FIREWALL-MIB", "fwCpuStatsId"),
)
if mibBuilder.loadTexts:
    fwCpuStatsEntry.setStatus("current")


class _FwCpuStatsId_Type(Integer32):
    """Custom type fwCpuStatsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FwCpuStatsId_Type.__name__ = "Integer32"
_FwCpuStatsId_Object = MibTableColumn
fwCpuStatsId = _FwCpuStatsId_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 1),
    _FwCpuStatsId_Type()
)
fwCpuStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwCpuStatsId.setStatus("current")


class _FwCpuName_Type(DisplayString):
    """Custom type fwCpuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwCpuName_Type.__name__ = "DisplayString"
_FwCpuName_Object = MibTableColumn
fwCpuName = _FwCpuName_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 2),
    _FwCpuName_Type()
)
fwCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuName.setStatus("current")
_FwCpuTotal_Type = Unsigned32
_FwCpuTotal_Object = MibTableColumn
fwCpuTotal = _FwCpuTotal_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 3),
    _FwCpuTotal_Type()
)
fwCpuTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuTotal.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuTotal.setUnits("percent")
_FwCpuUser_Type = Unsigned32
_FwCpuUser_Object = MibTableColumn
fwCpuUser = _FwCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 4),
    _FwCpuUser_Type()
)
fwCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuUser.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuUser.setUnits("percent")
_FwCpuSystem_Type = Unsigned32
_FwCpuSystem_Object = MibTableColumn
fwCpuSystem = _FwCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 5),
    _FwCpuSystem_Type()
)
fwCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuSystem.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuSystem.setUnits("percent")
_FwCpuNice_Type = Unsigned32
_FwCpuNice_Object = MibTableColumn
fwCpuNice = _FwCpuNice_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 6),
    _FwCpuNice_Type()
)
fwCpuNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuNice.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuNice.setUnits("percent")
_FwCpuIdle_Type = Unsigned32
_FwCpuIdle_Object = MibTableColumn
fwCpuIdle = _FwCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 7),
    _FwCpuIdle_Type()
)
fwCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuIdle.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuIdle.setUnits("percent")
_FwCpuIoWait_Type = Unsigned32
_FwCpuIoWait_Object = MibTableColumn
fwCpuIoWait = _FwCpuIoWait_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 8),
    _FwCpuIoWait_Type()
)
fwCpuIoWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuIoWait.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuIoWait.setUnits("percent")
_FwCpuHwIrq_Type = Unsigned32
_FwCpuHwIrq_Object = MibTableColumn
fwCpuHwIrq = _FwCpuHwIrq_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 9),
    _FwCpuHwIrq_Type()
)
fwCpuHwIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuHwIrq.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuHwIrq.setUnits("percent")
_FwCpuSoftIrq_Type = Unsigned32
_FwCpuSoftIrq_Object = MibTableColumn
fwCpuSoftIrq = _FwCpuSoftIrq_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 1, 1, 10),
    _FwCpuSoftIrq_Type()
)
fwCpuSoftIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCpuSoftIrq.setStatus("current")
if mibBuilder.loadTexts:
    fwCpuSoftIrq.setUnits("percent")
_FwMemoryInfo_ObjectIdentity = ObjectIdentity
fwMemoryInfo = _FwMemoryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2)
)
_FwSwapBytesTotal_Type = CounterBasedGauge64
_FwSwapBytesTotal_Object = MibScalar
fwSwapBytesTotal = _FwSwapBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 1),
    _FwSwapBytesTotal_Type()
)
fwSwapBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSwapBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    fwSwapBytesTotal.setUnits("bytes")
_FwSwapBytesUsed_Type = CounterBasedGauge64
_FwSwapBytesUsed_Object = MibScalar
fwSwapBytesUsed = _FwSwapBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 2),
    _FwSwapBytesUsed_Type()
)
fwSwapBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSwapBytesUsed.setStatus("current")
if mibBuilder.loadTexts:
    fwSwapBytesUsed.setUnits("bytes")
_FwSwapBytesUnused_Type = CounterBasedGauge64
_FwSwapBytesUnused_Object = MibScalar
fwSwapBytesUnused = _FwSwapBytesUnused_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 3),
    _FwSwapBytesUnused_Type()
)
fwSwapBytesUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSwapBytesUnused.setStatus("current")
if mibBuilder.loadTexts:
    fwSwapBytesUnused.setUnits("bytes")
_FwMemBytesTotal_Type = CounterBasedGauge64
_FwMemBytesTotal_Object = MibScalar
fwMemBytesTotal = _FwMemBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 4),
    _FwMemBytesTotal_Type()
)
fwMemBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesTotal.setUnits("bytes")
_FwMemBytesUsed_Type = CounterBasedGauge64
_FwMemBytesUsed_Object = MibScalar
fwMemBytesUsed = _FwMemBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 5),
    _FwMemBytesUsed_Type()
)
fwMemBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesUsed.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesUsed.setUnits("bytes")
_FwMemBytesUnused_Type = CounterBasedGauge64
_FwMemBytesUnused_Object = MibScalar
fwMemBytesUnused = _FwMemBytesUnused_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 6),
    _FwMemBytesUnused_Type()
)
fwMemBytesUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesUnused.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesUnused.setUnits("bytes")
_FwMemBytesBuffers_Type = CounterBasedGauge64
_FwMemBytesBuffers_Object = MibScalar
fwMemBytesBuffers = _FwMemBytesBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 7),
    _FwMemBytesBuffers_Type()
)
fwMemBytesBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesBuffers.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesBuffers.setUnits("bytes")
_FwMemBytesCached_Type = CounterBasedGauge64
_FwMemBytesCached_Object = MibScalar
fwMemBytesCached = _FwMemBytesCached_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 8),
    _FwMemBytesCached_Type()
)
fwMemBytesCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesCached.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesCached.setUnits("bytes")
_FwMemBytesSReclaimable_Type = CounterBasedGauge64
_FwMemBytesSReclaimable_Object = MibScalar
fwMemBytesSReclaimable = _FwMemBytesSReclaimable_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 9),
    _FwMemBytesSReclaimable_Type()
)
fwMemBytesSReclaimable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesSReclaimable.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesSReclaimable.setUnits("bytes")
_FwMemBytesAvailable_Type = CounterBasedGauge64
_FwMemBytesAvailable_Object = MibScalar
fwMemBytesAvailable = _FwMemBytesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 2, 10),
    _FwMemBytesAvailable_Type()
)
fwMemBytesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMemBytesAvailable.setStatus("current")
if mibBuilder.loadTexts:
    fwMemBytesAvailable.setUnits("bytes")
_FwDiskStatsTable_Object = MibTable
fwDiskStatsTable = _FwDiskStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    fwDiskStatsTable.setStatus("current")
_FwDiskStatsEntry_Object = MibTableRow
fwDiskStatsEntry = _FwDiskStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3, 1)
)
fwDiskStatsEntry.setIndexNames(
    (0, "STONESOFT-FIREWALL-MIB", "fwPartitionIndex"),
)
if mibBuilder.loadTexts:
    fwDiskStatsEntry.setStatus("current")


class _FwPartitionIndex_Type(Integer32):
    """Custom type fwPartitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FwPartitionIndex_Type.__name__ = "Integer32"
_FwPartitionIndex_Object = MibTableColumn
fwPartitionIndex = _FwPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3, 1, 1),
    _FwPartitionIndex_Type()
)
fwPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwPartitionIndex.setStatus("current")


class _FwPartitionDevName_Type(DisplayString):
    """Custom type fwPartitionDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwPartitionDevName_Type.__name__ = "DisplayString"
_FwPartitionDevName_Object = MibTableColumn
fwPartitionDevName = _FwPartitionDevName_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3, 1, 2),
    _FwPartitionDevName_Type()
)
fwPartitionDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionDevName.setStatus("current")


class _FwMountPointName_Type(DisplayString):
    """Custom type fwMountPointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwMountPointName_Type.__name__ = "DisplayString"
_FwMountPointName_Object = MibTableColumn
fwMountPointName = _FwMountPointName_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3, 1, 3),
    _FwMountPointName_Type()
)
fwMountPointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMountPointName.setStatus("current")
_FwPartitionSize_Type = CounterBasedGauge64
_FwPartitionSize_Object = MibTableColumn
fwPartitionSize = _FwPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3, 1, 4),
    _FwPartitionSize_Type()
)
fwPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    fwPartitionSize.setUnits("kbytes")
_FwPartitionUsed_Type = CounterBasedGauge64
_FwPartitionUsed_Object = MibTableColumn
fwPartitionUsed = _FwPartitionUsed_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3, 1, 5),
    _FwPartitionUsed_Type()
)
fwPartitionUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionUsed.setStatus("current")
if mibBuilder.loadTexts:
    fwPartitionUsed.setUnits("kbytes")
_FwPartitionAvail_Type = CounterBasedGauge64
_FwPartitionAvail_Object = MibTableColumn
fwPartitionAvail = _FwPartitionAvail_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 11, 3, 1, 6),
    _FwPartitionAvail_Type()
)
fwPartitionAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPartitionAvail.setStatus("current")
if mibBuilder.loadTexts:
    fwPartitionAvail.setUnits("kbytes")
_FwADSL_ObjectIdentity = ObjectIdentity
fwADSL = _FwADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12)
)
_AdslModulation_Type = DisplayString
_AdslModulation_Object = MibScalar
adslModulation = _AdslModulation_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 1),
    _AdslModulation_Type()
)
adslModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslModulation.setStatus("current")
_AdslChannel_Type = DisplayString
_AdslChannel_Object = MibScalar
adslChannel = _AdslChannel_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 2),
    _AdslChannel_Type()
)
adslChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslChannel.setStatus("current")
_AdslConnStatus_Type = DisplayString
_AdslConnStatus_Object = MibScalar
adslConnStatus = _AdslConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 3),
    _AdslConnStatus_Type()
)
adslConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslConnStatus.setStatus("current")
_AdslConnUptime_Type = TimeStamp
_AdslConnUptime_Object = MibScalar
adslConnUptime = _AdslConnUptime_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 4),
    _AdslConnUptime_Type()
)
adslConnUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslConnUptime.setStatus("current")
_AdslLineStatus_Type = DisplayString
_AdslLineStatus_Object = MibScalar
adslLineStatus = _AdslLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 5),
    _AdslLineStatus_Type()
)
adslLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineStatus.setStatus("current")
_AdslInOctets_Type = Integer32
_AdslInOctets_Object = MibScalar
adslInOctets = _AdslInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 6),
    _AdslInOctets_Type()
)
adslInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslInOctets.setStatus("current")
_AdslOutOctets_Type = Integer32
_AdslOutOctets_Object = MibScalar
adslOutOctets = _AdslOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 7),
    _AdslOutOctets_Type()
)
adslOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslOutOctets.setStatus("current")
_AdslSynchroSpeedUp_Type = Integer32
_AdslSynchroSpeedUp_Object = MibScalar
adslSynchroSpeedUp = _AdslSynchroSpeedUp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 8),
    _AdslSynchroSpeedUp_Type()
)
adslSynchroSpeedUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslSynchroSpeedUp.setStatus("current")
_AdslSynchroSpeedDown_Type = Integer32
_AdslSynchroSpeedDown_Object = MibScalar
adslSynchroSpeedDown = _AdslSynchroSpeedDown_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 9),
    _AdslSynchroSpeedDown_Type()
)
adslSynchroSpeedDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslSynchroSpeedDown.setStatus("current")
_AdslAttenuationUp_Type = Integer32
_AdslAttenuationUp_Object = MibScalar
adslAttenuationUp = _AdslAttenuationUp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 10),
    _AdslAttenuationUp_Type()
)
adslAttenuationUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAttenuationUp.setStatus("current")
_AdslAttenuationDown_Type = Integer32
_AdslAttenuationDown_Object = MibScalar
adslAttenuationDown = _AdslAttenuationDown_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 11),
    _AdslAttenuationDown_Type()
)
adslAttenuationDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAttenuationDown.setStatus("current")
_AdslNoiseMarginUp_Type = Integer32
_AdslNoiseMarginUp_Object = MibScalar
adslNoiseMarginUp = _AdslNoiseMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 12),
    _AdslNoiseMarginUp_Type()
)
adslNoiseMarginUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslNoiseMarginUp.setStatus("current")
_AdslNoiseMarginDown_Type = Integer32
_AdslNoiseMarginDown_Object = MibScalar
adslNoiseMarginDown = _AdslNoiseMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 13),
    _AdslNoiseMarginDown_Type()
)
adslNoiseMarginDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslNoiseMarginDown.setStatus("current")
_AdslHecErrorsUp_Type = Integer32
_AdslHecErrorsUp_Object = MibScalar
adslHecErrorsUp = _AdslHecErrorsUp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 14),
    _AdslHecErrorsUp_Type()
)
adslHecErrorsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslHecErrorsUp.setStatus("current")
_AdslHecErrorsDown_Type = Integer32
_AdslHecErrorsDown_Object = MibScalar
adslHecErrorsDown = _AdslHecErrorsDown_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 15),
    _AdslHecErrorsDown_Type()
)
adslHecErrorsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslHecErrorsDown.setStatus("current")
_AdslOcdErrorsUp_Type = Integer32
_AdslOcdErrorsUp_Object = MibScalar
adslOcdErrorsUp = _AdslOcdErrorsUp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 16),
    _AdslOcdErrorsUp_Type()
)
adslOcdErrorsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslOcdErrorsUp.setStatus("current")
_AdslOcdErrorsDown_Type = Integer32
_AdslOcdErrorsDown_Object = MibScalar
adslOcdErrorsDown = _AdslOcdErrorsDown_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 17),
    _AdslOcdErrorsDown_Type()
)
adslOcdErrorsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslOcdErrorsDown.setStatus("current")
_AdslLcdErrorsUp_Type = Integer32
_AdslLcdErrorsUp_Object = MibScalar
adslLcdErrorsUp = _AdslLcdErrorsUp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 18),
    _AdslLcdErrorsUp_Type()
)
adslLcdErrorsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLcdErrorsUp.setStatus("current")
_AdslLcdErrorsDown_Type = Integer32
_AdslLcdErrorsDown_Object = MibScalar
adslLcdErrorsDown = _AdslLcdErrorsDown_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 19),
    _AdslLcdErrorsDown_Type()
)
adslLcdErrorsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLcdErrorsDown.setStatus("current")
_AdslBitErrorsUp_Type = Integer32
_AdslBitErrorsUp_Object = MibScalar
adslBitErrorsUp = _AdslBitErrorsUp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 20),
    _AdslBitErrorsUp_Type()
)
adslBitErrorsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslBitErrorsUp.setStatus("current")
_AdslBitErrorsDown_Type = Integer32
_AdslBitErrorsDown_Object = MibScalar
adslBitErrorsDown = _AdslBitErrorsDown_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 12, 21),
    _AdslBitErrorsDown_Type()
)
adslBitErrorsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslBitErrorsDown.setStatus("current")
_FwVpnEp4Table_Object = MibTable
fwVpnEp4Table = _FwVpnEp4Table_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13)
)
if mibBuilder.loadTexts:
    fwVpnEp4Table.setStatus("current")
_FwVpnEp4Entry_Object = MibTableRow
fwVpnEp4Entry = _FwVpnEp4Entry_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1)
)
fwVpnEp4Entry.setIndexNames(
    (0, "STONESOFT-FIREWALL-MIB", "fwVpnEp4Index"),
)
if mibBuilder.loadTexts:
    fwVpnEp4Entry.setStatus("current")


class _FwVpnEp4Index_Type(Integer32):
    """Custom type fwVpnEp4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwVpnEp4Index_Type.__name__ = "Integer32"
_FwVpnEp4Index_Object = MibTableColumn
fwVpnEp4Index = _FwVpnEp4Index_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1, 1),
    _FwVpnEp4Index_Type()
)
fwVpnEp4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwVpnEp4Index.setStatus("current")
_FwVpnEp4Local_Type = InetAddressIPv4
_FwVpnEp4Local_Object = MibTableColumn
fwVpnEp4Local = _FwVpnEp4Local_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1, 2),
    _FwVpnEp4Local_Type()
)
fwVpnEp4Local.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4Local.setStatus("current")
_FwVpnEp4Remote_Type = InetAddressIPv4
_FwVpnEp4Remote_Object = MibTableColumn
fwVpnEp4Remote = _FwVpnEp4Remote_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1, 3),
    _FwVpnEp4Remote_Type()
)
fwVpnEp4Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4Remote.setStatus("current")
_FwVpnEp4RemoteType_Type = VpnEndpointType
_FwVpnEp4RemoteType_Object = MibTableColumn
fwVpnEp4RemoteType = _FwVpnEp4RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1, 4),
    _FwVpnEp4RemoteType_Type()
)
fwVpnEp4RemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4RemoteType.setStatus("current")
_FwVpnEp4ReceivedBytes_Type = Counter64
_FwVpnEp4ReceivedBytes_Object = MibTableColumn
fwVpnEp4ReceivedBytes = _FwVpnEp4ReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1, 5),
    _FwVpnEp4ReceivedBytes_Type()
)
fwVpnEp4ReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4ReceivedBytes.setStatus("current")
_FwVpnEp4SentBytes_Type = Counter64
_FwVpnEp4SentBytes_Object = MibTableColumn
fwVpnEp4SentBytes = _FwVpnEp4SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1, 6),
    _FwVpnEp4SentBytes_Type()
)
fwVpnEp4SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4SentBytes.setStatus("current")
_FwVpnEp4IpsecSa_Type = Counter32
_FwVpnEp4IpsecSa_Object = MibTableColumn
fwVpnEp4IpsecSa = _FwVpnEp4IpsecSa_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 13, 1, 7),
    _FwVpnEp4IpsecSa_Type()
)
fwVpnEp4IpsecSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp4IpsecSa.setStatus("current")
_FwVpnEp6Table_Object = MibTable
fwVpnEp6Table = _FwVpnEp6Table_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14)
)
if mibBuilder.loadTexts:
    fwVpnEp6Table.setStatus("current")
_FwVpnEp6Entry_Object = MibTableRow
fwVpnEp6Entry = _FwVpnEp6Entry_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1)
)
fwVpnEp6Entry.setIndexNames(
    (0, "STONESOFT-FIREWALL-MIB", "fwVpnEp6Index"),
)
if mibBuilder.loadTexts:
    fwVpnEp6Entry.setStatus("current")


class _FwVpnEp6Index_Type(Integer32):
    """Custom type fwVpnEp6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwVpnEp6Index_Type.__name__ = "Integer32"
_FwVpnEp6Index_Object = MibTableColumn
fwVpnEp6Index = _FwVpnEp6Index_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1, 1),
    _FwVpnEp6Index_Type()
)
fwVpnEp6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwVpnEp6Index.setStatus("current")
_FwVpnEp6Local_Type = InetAddressIPv6
_FwVpnEp6Local_Object = MibTableColumn
fwVpnEp6Local = _FwVpnEp6Local_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1, 2),
    _FwVpnEp6Local_Type()
)
fwVpnEp6Local.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6Local.setStatus("current")
_FwVpnEp6Remote_Type = InetAddressIPv6
_FwVpnEp6Remote_Object = MibTableColumn
fwVpnEp6Remote = _FwVpnEp6Remote_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1, 3),
    _FwVpnEp6Remote_Type()
)
fwVpnEp6Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6Remote.setStatus("current")
_FwVpnEp6RemoteType_Type = VpnEndpointType
_FwVpnEp6RemoteType_Object = MibTableColumn
fwVpnEp6RemoteType = _FwVpnEp6RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1, 4),
    _FwVpnEp6RemoteType_Type()
)
fwVpnEp6RemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6RemoteType.setStatus("current")
_FwVpnEp6ReceivedBytes_Type = Counter64
_FwVpnEp6ReceivedBytes_Object = MibTableColumn
fwVpnEp6ReceivedBytes = _FwVpnEp6ReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1, 5),
    _FwVpnEp6ReceivedBytes_Type()
)
fwVpnEp6ReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6ReceivedBytes.setStatus("current")
_FwVpnEp6SentBytes_Type = Counter64
_FwVpnEp6SentBytes_Object = MibTableColumn
fwVpnEp6SentBytes = _FwVpnEp6SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1, 6),
    _FwVpnEp6SentBytes_Type()
)
fwVpnEp6SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6SentBytes.setStatus("current")
_FwVpnEp6IpsecSa_Type = Counter32
_FwVpnEp6IpsecSa_Object = MibTableColumn
fwVpnEp6IpsecSa = _FwVpnEp6IpsecSa_Object(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 1, 14, 1, 7),
    _FwVpnEp6IpsecSa_Type()
)
fwVpnEp6IpsecSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVpnEp6IpsecSa.setStatus("current")
_FirewallEvents_ObjectIdentity = ObjectIdentity
firewallEvents = _FirewallEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 2)
)
_FirewallEventsV2_ObjectIdentity = ObjectIdentity
firewallEventsV2 = _FirewallEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 2, 0)
)
_FirewallConformance_ObjectIdentity = ObjectIdentity
firewallConformance = _FirewallConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3)
)
_FirewallGroups_ObjectIdentity = ObjectIdentity
firewallGroups = _FirewallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1)
)
_FirewallCompliances_ObjectIdentity = ObjectIdentity
firewallCompliances = _FirewallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 2)
)

# Managed Objects groups

firewallGeneralInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1, 1)
)
firewallGeneralInformationGroup.setObjects(
      *(("STONESOFT-FIREWALL-MIB", "fwSoftwareVersion"),
        ("STONESOFT-FIREWALL-MIB", "fwSecurityPolicy"),
        ("STONESOFT-FIREWALL-MIB", "fwPolicyTime"))
)
if mibBuilder.loadTexts:
    firewallGeneralInformationGroup.setStatus("current")

firewallIfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1, 3)
)
firewallIfaceStatsGroup.setObjects(
      *(("STONESOFT-FIREWALL-MIB", "fwIfName"),
        ("STONESOFT-FIREWALL-MIB", "fwIfAcceptedPkts"),
        ("STONESOFT-FIREWALL-MIB", "fwIfDroppedPkts"),
        ("STONESOFT-FIREWALL-MIB", "fwIfLoggedPkts"),
        ("STONESOFT-FIREWALL-MIB", "fwIfAccountedPkts"),
        ("STONESOFT-FIREWALL-MIB", "fwIfRejectedPkts"),
        ("STONESOFT-FIREWALL-MIB", "fwIfForwardedPkts"),
        ("STONESOFT-FIREWALL-MIB", "fwIfAcceptedBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwIfDroppedBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwIfLoggedBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwIfAccountedBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwIfRejectedBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwIfForwardedBytes"))
)
if mibBuilder.loadTexts:
    firewallIfaceStatsGroup.setStatus("current")

firewallGeneralStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1, 4)
)
firewallGeneralStatsGroup.setObjects(
      *(("STONESOFT-FIREWALL-MIB", "fwConnNumber"),
        ("STONESOFT-FIREWALL-MIB", "fwAccepted"),
        ("STONESOFT-FIREWALL-MIB", "fwDropped"),
        ("STONESOFT-FIREWALL-MIB", "fwLogged"),
        ("STONESOFT-FIREWALL-MIB", "fwAccounted"),
        ("STONESOFT-FIREWALL-MIB", "fwRejected"))
)
if mibBuilder.loadTexts:
    firewallGeneralStatsGroup.setStatus("current")

firewallHardwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1, 5)
)
firewallHardwareGroup.setObjects(
      *(("STONESOFT-FIREWALL-MIB", "fwCpuName"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuTotal"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuUser"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuSystem"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuNice"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuIdle"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuIoWait"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuHwIrq"),
        ("STONESOFT-FIREWALL-MIB", "fwCpuSoftIrq"),
        ("STONESOFT-FIREWALL-MIB", "fwSwapBytesTotal"),
        ("STONESOFT-FIREWALL-MIB", "fwSwapBytesUsed"),
        ("STONESOFT-FIREWALL-MIB", "fwSwapBytesUnused"),
        ("STONESOFT-FIREWALL-MIB", "fwMemBytesTotal"),
        ("STONESOFT-FIREWALL-MIB", "fwMemBytesUsed"),
        ("STONESOFT-FIREWALL-MIB", "fwMemBytesUnused"),
        ("STONESOFT-FIREWALL-MIB", "fwMemBytesBuffers"),
        ("STONESOFT-FIREWALL-MIB", "fwMemBytesCached"),
        ("STONESOFT-FIREWALL-MIB", "fwMemBytesAvailable"),
        ("STONESOFT-FIREWALL-MIB", "fwMemBytesSReclaimable"),
        ("STONESOFT-FIREWALL-MIB", "fwPartitionDevName"),
        ("STONESOFT-FIREWALL-MIB", "fwMountPointName"),
        ("STONESOFT-FIREWALL-MIB", "fwPartitionSize"),
        ("STONESOFT-FIREWALL-MIB", "fwPartitionUsed"),
        ("STONESOFT-FIREWALL-MIB", "fwPartitionAvail"))
)
if mibBuilder.loadTexts:
    firewallHardwareGroup.setStatus("current")

firewallAdslGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1, 6)
)
firewallAdslGroup.setObjects(
      *(("STONESOFT-FIREWALL-MIB", "adslModulation"),
        ("STONESOFT-FIREWALL-MIB", "adslChannel"),
        ("STONESOFT-FIREWALL-MIB", "adslConnStatus"),
        ("STONESOFT-FIREWALL-MIB", "adslConnUptime"),
        ("STONESOFT-FIREWALL-MIB", "adslLineStatus"),
        ("STONESOFT-FIREWALL-MIB", "adslInOctets"),
        ("STONESOFT-FIREWALL-MIB", "adslOutOctets"),
        ("STONESOFT-FIREWALL-MIB", "adslSynchroSpeedUp"),
        ("STONESOFT-FIREWALL-MIB", "adslSynchroSpeedDown"),
        ("STONESOFT-FIREWALL-MIB", "adslAttenuationUp"),
        ("STONESOFT-FIREWALL-MIB", "adslAttenuationDown"),
        ("STONESOFT-FIREWALL-MIB", "adslNoiseMarginUp"),
        ("STONESOFT-FIREWALL-MIB", "adslNoiseMarginDown"),
        ("STONESOFT-FIREWALL-MIB", "adslHecErrorsUp"),
        ("STONESOFT-FIREWALL-MIB", "adslHecErrorsDown"),
        ("STONESOFT-FIREWALL-MIB", "adslOcdErrorsUp"),
        ("STONESOFT-FIREWALL-MIB", "adslOcdErrorsDown"),
        ("STONESOFT-FIREWALL-MIB", "adslLcdErrorsUp"),
        ("STONESOFT-FIREWALL-MIB", "adslLcdErrorsDown"),
        ("STONESOFT-FIREWALL-MIB", "adslBitErrorsUp"),
        ("STONESOFT-FIREWALL-MIB", "adslBitErrorsDown"))
)
if mibBuilder.loadTexts:
    firewallAdslGroup.setStatus("current")

firewallVpnEpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1, 7)
)
firewallVpnEpGroup.setObjects(
      *(("STONESOFT-FIREWALL-MIB", "fwVpnEp4Local"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp4Remote"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp4RemoteType"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp4ReceivedBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp4SentBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp4IpsecSa"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp6Local"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp6Remote"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp6RemoteType"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp6ReceivedBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp6SentBytes"),
        ("STONESOFT-FIREWALL-MIB", "fwVpnEp6IpsecSa"))
)
if mibBuilder.loadTexts:
    firewallVpnEpGroup.setStatus("current")


# Notification objects

fwPolicyInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 2, 0, 1)
)
fwPolicyInstall.setObjects(
    ("STONESOFT-FIREWALL-MIB", "fwSecurityPolicy")
)
if mibBuilder.loadTexts:
    fwPolicyInstall.setStatus(
        "current"
    )


# Notifications groups

firewallGeneralNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 1, 2)
)
firewallGeneralNotifGroup.setObjects(
    ("STONESOFT-FIREWALL-MIB", "fwPolicyInstall")
)
if mibBuilder.loadTexts:
    firewallGeneralNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

firewallCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1369, 5, 2, 3, 2, 1)
)
firewallCompliance1.setObjects(
      *(("STONESOFT-FIREWALL-MIB", "firewallGeneralInformationGroup"),
        ("STONESOFT-FIREWALL-MIB", "firewallGeneralNotifGroup"),
        ("STONESOFT-FIREWALL-MIB", "firewallGeneralStatsGroup"),
        ("STONESOFT-FIREWALL-MIB", "firewallIfaceStatsGroup"),
        ("STONESOFT-FIREWALL-MIB", "firewallHardwareGroup"),
        ("STONESOFT-FIREWALL-MIB", "firewallAdslGroup"),
        ("STONESOFT-FIREWALL-MIB", "firewallVpnEpGroup"))
)
if mibBuilder.loadTexts:
    firewallCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STONESOFT-FIREWALL-MIB",
    **{"VpnEndpointType": VpnEndpointType,
       "stonesoftFirewallMibModule": stonesoftFirewallMibModule,
       "firewallObjects": firewallObjects,
       "fwSoftwareVersion": fwSoftwareVersion,
       "fwSecurityPolicy": fwSecurityPolicy,
       "fwPolicyTime": fwPolicyTime,
       "fwConnNumber": fwConnNumber,
       "fwAccepted": fwAccepted,
       "fwDropped": fwDropped,
       "fwLogged": fwLogged,
       "fwAccounted": fwAccounted,
       "fwRejected": fwRejected,
       "fwIfStatsTable": fwIfStatsTable,
       "fwIfStatsEntry": fwIfStatsEntry,
       "fwIfStatsIndex": fwIfStatsIndex,
       "fwIfName": fwIfName,
       "fwIfAcceptedPkts": fwIfAcceptedPkts,
       "fwIfDroppedPkts": fwIfDroppedPkts,
       "fwIfLoggedPkts": fwIfLoggedPkts,
       "fwIfAccountedPkts": fwIfAccountedPkts,
       "fwIfRejectedPkts": fwIfRejectedPkts,
       "fwIfAcceptedBytes": fwIfAcceptedBytes,
       "fwIfDroppedBytes": fwIfDroppedBytes,
       "fwIfLoggedBytes": fwIfLoggedBytes,
       "fwIfAccountedBytes": fwIfAccountedBytes,
       "fwIfRejectedBytes": fwIfRejectedBytes,
       "fwIfForwardedPkts": fwIfForwardedPkts,
       "fwIfForwardedBytes": fwIfForwardedBytes,
       "fwHardware": fwHardware,
       "fwCpuStatsTable": fwCpuStatsTable,
       "fwCpuStatsEntry": fwCpuStatsEntry,
       "fwCpuStatsId": fwCpuStatsId,
       "fwCpuName": fwCpuName,
       "fwCpuTotal": fwCpuTotal,
       "fwCpuUser": fwCpuUser,
       "fwCpuSystem": fwCpuSystem,
       "fwCpuNice": fwCpuNice,
       "fwCpuIdle": fwCpuIdle,
       "fwCpuIoWait": fwCpuIoWait,
       "fwCpuHwIrq": fwCpuHwIrq,
       "fwCpuSoftIrq": fwCpuSoftIrq,
       "fwMemoryInfo": fwMemoryInfo,
       "fwSwapBytesTotal": fwSwapBytesTotal,
       "fwSwapBytesUsed": fwSwapBytesUsed,
       "fwSwapBytesUnused": fwSwapBytesUnused,
       "fwMemBytesTotal": fwMemBytesTotal,
       "fwMemBytesUsed": fwMemBytesUsed,
       "fwMemBytesUnused": fwMemBytesUnused,
       "fwMemBytesBuffers": fwMemBytesBuffers,
       "fwMemBytesCached": fwMemBytesCached,
       "fwMemBytesSReclaimable": fwMemBytesSReclaimable,
       "fwMemBytesAvailable": fwMemBytesAvailable,
       "fwDiskStatsTable": fwDiskStatsTable,
       "fwDiskStatsEntry": fwDiskStatsEntry,
       "fwPartitionIndex": fwPartitionIndex,
       "fwPartitionDevName": fwPartitionDevName,
       "fwMountPointName": fwMountPointName,
       "fwPartitionSize": fwPartitionSize,
       "fwPartitionUsed": fwPartitionUsed,
       "fwPartitionAvail": fwPartitionAvail,
       "fwADSL": fwADSL,
       "adslModulation": adslModulation,
       "adslChannel": adslChannel,
       "adslConnStatus": adslConnStatus,
       "adslConnUptime": adslConnUptime,
       "adslLineStatus": adslLineStatus,
       "adslInOctets": adslInOctets,
       "adslOutOctets": adslOutOctets,
       "adslSynchroSpeedUp": adslSynchroSpeedUp,
       "adslSynchroSpeedDown": adslSynchroSpeedDown,
       "adslAttenuationUp": adslAttenuationUp,
       "adslAttenuationDown": adslAttenuationDown,
       "adslNoiseMarginUp": adslNoiseMarginUp,
       "adslNoiseMarginDown": adslNoiseMarginDown,
       "adslHecErrorsUp": adslHecErrorsUp,
       "adslHecErrorsDown": adslHecErrorsDown,
       "adslOcdErrorsUp": adslOcdErrorsUp,
       "adslOcdErrorsDown": adslOcdErrorsDown,
       "adslLcdErrorsUp": adslLcdErrorsUp,
       "adslLcdErrorsDown": adslLcdErrorsDown,
       "adslBitErrorsUp": adslBitErrorsUp,
       "adslBitErrorsDown": adslBitErrorsDown,
       "fwVpnEp4Table": fwVpnEp4Table,
       "fwVpnEp4Entry": fwVpnEp4Entry,
       "fwVpnEp4Index": fwVpnEp4Index,
       "fwVpnEp4Local": fwVpnEp4Local,
       "fwVpnEp4Remote": fwVpnEp4Remote,
       "fwVpnEp4RemoteType": fwVpnEp4RemoteType,
       "fwVpnEp4ReceivedBytes": fwVpnEp4ReceivedBytes,
       "fwVpnEp4SentBytes": fwVpnEp4SentBytes,
       "fwVpnEp4IpsecSa": fwVpnEp4IpsecSa,
       "fwVpnEp6Table": fwVpnEp6Table,
       "fwVpnEp6Entry": fwVpnEp6Entry,
       "fwVpnEp6Index": fwVpnEp6Index,
       "fwVpnEp6Local": fwVpnEp6Local,
       "fwVpnEp6Remote": fwVpnEp6Remote,
       "fwVpnEp6RemoteType": fwVpnEp6RemoteType,
       "fwVpnEp6ReceivedBytes": fwVpnEp6ReceivedBytes,
       "fwVpnEp6SentBytes": fwVpnEp6SentBytes,
       "fwVpnEp6IpsecSa": fwVpnEp6IpsecSa,
       "firewallEvents": firewallEvents,
       "firewallEventsV2": firewallEventsV2,
       "fwPolicyInstall": fwPolicyInstall,
       "firewallConformance": firewallConformance,
       "firewallGroups": firewallGroups,
       "firewallGeneralInformationGroup": firewallGeneralInformationGroup,
       "firewallGeneralNotifGroup": firewallGeneralNotifGroup,
       "firewallIfaceStatsGroup": firewallIfaceStatsGroup,
       "firewallGeneralStatsGroup": firewallGeneralStatsGroup,
       "firewallHardwareGroup": firewallHardwareGroup,
       "firewallAdslGroup": firewallAdslGroup,
       "firewallVpnEpGroup": firewallVpnEpGroup,
       "firewallCompliances": firewallCompliances,
       "firewallCompliance1": firewallCompliance1}
)
