# SNMP MIB module (TEGILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tegile\TEGILE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:43 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

tegile = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43906)
)
if mibBuilder.loadTexts:
    tegile.setRevisions(
        ("2015-09-23 10:10",
         "2016-04-06 10:10",
         "2016-09-10 10:10",
         "2017-03-21 10:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TegileArray_ObjectIdentity = ObjectIdentity
tegileArray = _TegileArray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1)
)
_Properties_ObjectIdentity = ObjectIdentity
properties = _Properties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1)
)
_HaControllerA_Name_Type = OctetString
_HaControllerA_Name_Object = MibScalar
haControllerA_Name = _HaControllerA_Name_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 1),
    _HaControllerA_Name_Type()
)
haControllerA_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerA_Name.setStatus("current")
_HaControllerA_IPAddr_Type = IpAddress
_HaControllerA_IPAddr_Object = MibScalar
haControllerA_IPAddr = _HaControllerA_IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 2),
    _HaControllerA_IPAddr_Type()
)
haControllerA_IPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerA_IPAddr.setStatus("current")
_HaControllerA_SoftwareVersion_Type = OctetString
_HaControllerA_SoftwareVersion_Object = MibScalar
haControllerA_SoftwareVersion = _HaControllerA_SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 3),
    _HaControllerA_SoftwareVersion_Type()
)
haControllerA_SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerA_SoftwareVersion.setStatus("current")
_HaControllerA_Uptime_Type = OctetString
_HaControllerA_Uptime_Object = MibScalar
haControllerA_Uptime = _HaControllerA_Uptime_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 4),
    _HaControllerA_Uptime_Type()
)
haControllerA_Uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerA_Uptime.setStatus("current")
_HaControllerB_Name_Type = OctetString
_HaControllerB_Name_Object = MibScalar
haControllerB_Name = _HaControllerB_Name_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 5),
    _HaControllerB_Name_Type()
)
haControllerB_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerB_Name.setStatus("current")
_HaControllerB_IPAddr_Type = IpAddress
_HaControllerB_IPAddr_Object = MibScalar
haControllerB_IPAddr = _HaControllerB_IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 6),
    _HaControllerB_IPAddr_Type()
)
haControllerB_IPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerB_IPAddr.setStatus("current")
_HaControllerB_SoftwareVersion_Type = OctetString
_HaControllerB_SoftwareVersion_Object = MibScalar
haControllerB_SoftwareVersion = _HaControllerB_SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 7),
    _HaControllerB_SoftwareVersion_Type()
)
haControllerB_SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerB_SoftwareVersion.setStatus("current")
_HaControllerB_Uptime_Type = OctetString
_HaControllerB_Uptime_Object = MibScalar
haControllerB_Uptime = _HaControllerB_Uptime_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 8),
    _HaControllerB_Uptime_Type()
)
haControllerB_Uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haControllerB_Uptime.setStatus("current")
_ControllerHardwareModel_Type = OctetString
_ControllerHardwareModel_Object = MibScalar
controllerHardwareModel = _ControllerHardwareModel_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 9),
    _ControllerHardwareModel_Type()
)
controllerHardwareModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerHardwareModel.setStatus("current")
_SnmpAgentVersion_Type = OctetString
_SnmpAgentVersion_Object = MibScalar
snmpAgentVersion = _SnmpAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 1, 10),
    _SnmpAgentVersion_Type()
)
snmpAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentVersion.setStatus("current")
_GlobalStatistics_ObjectIdentity = ObjectIdentity
globalStatistics = _GlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2)
)
_CpuTotalUsage_Type = Unsigned32
_CpuTotalUsage_Object = MibScalar
cpuTotalUsage = _CpuTotalUsage_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 1),
    _CpuTotalUsage_Type()
)
cpuTotalUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalUsage.setStatus("current")
_CpuSystemCalls_Type = Unsigned32
_CpuSystemCalls_Object = MibScalar
cpuSystemCalls = _CpuSystemCalls_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 2),
    _CpuSystemCalls_Type()
)
cpuSystemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuSystemCalls.setStatus("current")
_CpuInterrupts_Type = Unsigned32
_CpuInterrupts_Object = MibScalar
cpuInterrupts = _CpuInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 3),
    _CpuInterrupts_Type()
)
cpuInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInterrupts.setStatus("current")
_CacheTotalWriteMbps_Type = Unsigned32
_CacheTotalWriteMbps_Object = MibScalar
cacheTotalWriteMbps = _CacheTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 4),
    _CacheTotalWriteMbps_Type()
)
cacheTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalWriteMbps.setStatus("current")
_CacheTotalReadMbps_Type = Unsigned32
_CacheTotalReadMbps_Object = MibScalar
cacheTotalReadMbps = _CacheTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 5),
    _CacheTotalReadMbps_Type()
)
cacheTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalReadMbps.setStatus("current")
_CacheTotalWriteIops_Type = Unsigned32
_CacheTotalWriteIops_Object = MibScalar
cacheTotalWriteIops = _CacheTotalWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 6),
    _CacheTotalWriteIops_Type()
)
cacheTotalWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalWriteIops.setStatus("current")
_CacheTotalReadIops_Type = Unsigned32
_CacheTotalReadIops_Object = MibScalar
cacheTotalReadIops = _CacheTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 7),
    _CacheTotalReadIops_Type()
)
cacheTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalReadIops.setStatus("current")
_CacheRAMReads_Type = Unsigned32
_CacheRAMReads_Object = MibScalar
cacheRAMReads = _CacheRAMReads_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 8),
    _CacheRAMReads_Type()
)
cacheRAMReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRAMReads.setStatus("current")
_CacheSSDReads_Type = Unsigned32
_CacheSSDReads_Object = MibScalar
cacheSSDReads = _CacheSSDReads_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 9),
    _CacheSSDReads_Type()
)
cacheSSDReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSSDReads.setStatus("current")
_DiskTotalWriteMbps_Type = Unsigned32
_DiskTotalWriteMbps_Object = MibScalar
diskTotalWriteMbps = _DiskTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 10),
    _DiskTotalWriteMbps_Type()
)
diskTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalWriteMbps.setStatus("current")
_DiskTotalReadMbps_Type = Unsigned32
_DiskTotalReadMbps_Object = MibScalar
diskTotalReadMbps = _DiskTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 11),
    _DiskTotalReadMbps_Type()
)
diskTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalReadMbps.setStatus("current")
_DiskTotalWriteIops_Type = Unsigned32
_DiskTotalWriteIops_Object = MibScalar
diskTotalWriteIops = _DiskTotalWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 12),
    _DiskTotalWriteIops_Type()
)
diskTotalWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalWriteIops.setStatus("current")
_DiskTotalReadIops_Type = Unsigned32
_DiskTotalReadIops_Object = MibScalar
diskTotalReadIops = _DiskTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 13),
    _DiskTotalReadIops_Type()
)
diskTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalReadIops.setStatus("current")
_DiskDataWriteMbps_Type = Unsigned32
_DiskDataWriteMbps_Object = MibScalar
diskDataWriteMbps = _DiskDataWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 14),
    _DiskDataWriteMbps_Type()
)
diskDataWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDataWriteMbps.setStatus("current")
_DiskDataReadMbps_Type = Unsigned32
_DiskDataReadMbps_Object = MibScalar
diskDataReadMbps = _DiskDataReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 15),
    _DiskDataReadMbps_Type()
)
diskDataReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDataReadMbps.setStatus("current")
_DiskDataWriteIops_Type = Unsigned32
_DiskDataWriteIops_Object = MibScalar
diskDataWriteIops = _DiskDataWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 16),
    _DiskDataWriteIops_Type()
)
diskDataWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDataWriteIops.setStatus("current")
_DiskDataReadIops_Type = Unsigned32
_DiskDataReadIops_Object = MibScalar
diskDataReadIops = _DiskDataReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 17),
    _DiskDataReadIops_Type()
)
diskDataReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDataReadIops.setStatus("current")
_DiskAvgWriteLatency_Type = Unsigned32
_DiskAvgWriteLatency_Object = MibScalar
diskAvgWriteLatency = _DiskAvgWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 18),
    _DiskAvgWriteLatency_Type()
)
diskAvgWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskAvgWriteLatency.setStatus("current")
_DiskAvgReadLatency_Type = Unsigned32
_DiskAvgReadLatency_Object = MibScalar
diskAvgReadLatency = _DiskAvgReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 19),
    _DiskAvgReadLatency_Type()
)
diskAvgReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskAvgReadLatency.setStatus("current")
_DiskIOCount_Type = Unsigned32
_DiskIOCount_Object = MibScalar
diskIOCount = _DiskIOCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 20),
    _DiskIOCount_Type()
)
diskIOCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOCount.setStatus("current")
_DiskRandomIOCount_Type = Unsigned32
_DiskRandomIOCount_Object = MibScalar
diskRandomIOCount = _DiskRandomIOCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 21),
    _DiskRandomIOCount_Type()
)
diskRandomIOCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskRandomIOCount.setStatus("current")
_DiskSequentialIOCount_Type = Unsigned32
_DiskSequentialIOCount_Object = MibScalar
diskSequentialIOCount = _DiskSequentialIOCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 22),
    _DiskSequentialIOCount_Type()
)
diskSequentialIOCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSequentialIOCount.setStatus("current")
_PoolTotalWriteMbps_Type = Unsigned32
_PoolTotalWriteMbps_Object = MibScalar
poolTotalWriteMbps = _PoolTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 23),
    _PoolTotalWriteMbps_Type()
)
poolTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalWriteMbps.setStatus("current")
_PoolTotalReadMbps_Type = Unsigned32
_PoolTotalReadMbps_Object = MibScalar
poolTotalReadMbps = _PoolTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 24),
    _PoolTotalReadMbps_Type()
)
poolTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalReadMbps.setStatus("current")
_PoolTotalWriteIops_Type = Unsigned32
_PoolTotalWriteIops_Object = MibScalar
poolTotalWriteIops = _PoolTotalWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 25),
    _PoolTotalWriteIops_Type()
)
poolTotalWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalWriteIops.setStatus("current")
_PoolTotalReadIops_Type = Unsigned32
_PoolTotalReadIops_Object = MibScalar
poolTotalReadIops = _PoolTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 26),
    _PoolTotalReadIops_Type()
)
poolTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalReadIops.setStatus("current")
_PoolAvgWriteLatency_Type = Unsigned32
_PoolAvgWriteLatency_Object = MibScalar
poolAvgWriteLatency = _PoolAvgWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 27),
    _PoolAvgWriteLatency_Type()
)
poolAvgWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolAvgWriteLatency.setStatus("current")
_PoolAvgReadLatency_Type = Unsigned32
_PoolAvgReadLatency_Object = MibScalar
poolAvgReadLatency = _PoolAvgReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 28),
    _PoolAvgReadLatency_Type()
)
poolAvgReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolAvgReadLatency.setStatus("current")
_CifsTotalWriteMbps_Type = Unsigned32
_CifsTotalWriteMbps_Object = MibScalar
cifsTotalWriteMbps = _CifsTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 29),
    _CifsTotalWriteMbps_Type()
)
cifsTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTotalWriteMbps.setStatus("current")
_CifsTotalReadMbps_Type = Unsigned32
_CifsTotalReadMbps_Object = MibScalar
cifsTotalReadMbps = _CifsTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 30),
    _CifsTotalReadMbps_Type()
)
cifsTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTotalReadMbps.setStatus("current")
_CifsTotalWriteIops_Type = Unsigned32
_CifsTotalWriteIops_Object = MibScalar
cifsTotalWriteIops = _CifsTotalWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 31),
    _CifsTotalWriteIops_Type()
)
cifsTotalWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTotalWriteIops.setStatus("current")
_CifsTotalReadIops_Type = Unsigned32
_CifsTotalReadIops_Object = MibScalar
cifsTotalReadIops = _CifsTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 32),
    _CifsTotalReadIops_Type()
)
cifsTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTotalReadIops.setStatus("current")
_CifsAvgWriteLatency_Type = Unsigned32
_CifsAvgWriteLatency_Object = MibScalar
cifsAvgWriteLatency = _CifsAvgWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 33),
    _CifsAvgWriteLatency_Type()
)
cifsAvgWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsAvgWriteLatency.setStatus("current")
_CifsAvgReadLatency_Type = Unsigned32
_CifsAvgReadLatency_Object = MibScalar
cifsAvgReadLatency = _CifsAvgReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 34),
    _CifsAvgReadLatency_Type()
)
cifsAvgReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsAvgReadLatency.setStatus("current")
_NfsTotalWriteMbps_Type = Unsigned32
_NfsTotalWriteMbps_Object = MibScalar
nfsTotalWriteMbps = _NfsTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 35),
    _NfsTotalWriteMbps_Type()
)
nfsTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsTotalWriteMbps.setStatus("current")
_NfsTotalReadMbps_Type = Unsigned32
_NfsTotalReadMbps_Object = MibScalar
nfsTotalReadMbps = _NfsTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 36),
    _NfsTotalReadMbps_Type()
)
nfsTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsTotalReadMbps.setStatus("current")
_NfsTotalWriteIops_Type = Unsigned32
_NfsTotalWriteIops_Object = MibScalar
nfsTotalWriteIops = _NfsTotalWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 37),
    _NfsTotalWriteIops_Type()
)
nfsTotalWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsTotalWriteIops.setStatus("current")
_NfsTotalReadIops_Type = Unsigned32
_NfsTotalReadIops_Object = MibScalar
nfsTotalReadIops = _NfsTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 38),
    _NfsTotalReadIops_Type()
)
nfsTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsTotalReadIops.setStatus("current")
_NfsAvgWriteLatency_Type = Unsigned32
_NfsAvgWriteLatency_Object = MibScalar
nfsAvgWriteLatency = _NfsAvgWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 39),
    _NfsAvgWriteLatency_Type()
)
nfsAvgWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsAvgWriteLatency.setStatus("current")
_NfsAvgReadLatency_Type = Unsigned32
_NfsAvgReadLatency_Object = MibScalar
nfsAvgReadLatency = _NfsAvgReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 40),
    _NfsAvgReadLatency_Type()
)
nfsAvgReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsAvgReadLatency.setStatus("current")
_IscsiTotalWriteMbps_Type = Unsigned32
_IscsiTotalWriteMbps_Object = MibScalar
iscsiTotalWriteMbps = _IscsiTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 41),
    _IscsiTotalWriteMbps_Type()
)
iscsiTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTotalWriteMbps.setStatus("current")
_IscsiTotalReadMbps_Type = Unsigned32
_IscsiTotalReadMbps_Object = MibScalar
iscsiTotalReadMbps = _IscsiTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 42),
    _IscsiTotalReadMbps_Type()
)
iscsiTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTotalReadMbps.setStatus("current")
_IscsiWriteIops_Type = Unsigned32
_IscsiWriteIops_Object = MibScalar
iscsiWriteIops = _IscsiWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 43),
    _IscsiWriteIops_Type()
)
iscsiWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiWriteIops.setStatus("current")
_IscsiTotalReadIops_Type = Unsigned32
_IscsiTotalReadIops_Object = MibScalar
iscsiTotalReadIops = _IscsiTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 44),
    _IscsiTotalReadIops_Type()
)
iscsiTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTotalReadIops.setStatus("current")
_IscsiAvgWriteLatency_Type = Unsigned32
_IscsiAvgWriteLatency_Object = MibScalar
iscsiAvgWriteLatency = _IscsiAvgWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 45),
    _IscsiAvgWriteLatency_Type()
)
iscsiAvgWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiAvgWriteLatency.setStatus("current")
_IscsiAvgReadLatency_Type = Unsigned32
_IscsiAvgReadLatency_Object = MibScalar
iscsiAvgReadLatency = _IscsiAvgReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 46),
    _IscsiAvgReadLatency_Type()
)
iscsiAvgReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiAvgReadLatency.setStatus("current")
_FcTotalWriteMbps_Type = Unsigned32
_FcTotalWriteMbps_Object = MibScalar
fcTotalWriteMbps = _FcTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 47),
    _FcTotalWriteMbps_Type()
)
fcTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTotalWriteMbps.setStatus("current")
_FcTotalReadMbps_Type = Unsigned32
_FcTotalReadMbps_Object = MibScalar
fcTotalReadMbps = _FcTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 48),
    _FcTotalReadMbps_Type()
)
fcTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTotalReadMbps.setStatus("current")
_FcTotalWriteIops_Type = Unsigned32
_FcTotalWriteIops_Object = MibScalar
fcTotalWriteIops = _FcTotalWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 49),
    _FcTotalWriteIops_Type()
)
fcTotalWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTotalWriteIops.setStatus("current")
_FcTotalReadIops_Type = Unsigned32
_FcTotalReadIops_Object = MibScalar
fcTotalReadIops = _FcTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 50),
    _FcTotalReadIops_Type()
)
fcTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTotalReadIops.setStatus("current")
_FcAvgWriteLatency_Type = Unsigned32
_FcAvgWriteLatency_Object = MibScalar
fcAvgWriteLatency = _FcAvgWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 51),
    _FcAvgWriteLatency_Type()
)
fcAvgWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcAvgWriteLatency.setStatus("current")
_FcAvgReadLatency_Type = Unsigned32
_FcAvgReadLatency_Object = MibScalar
fcAvgReadLatency = _FcAvgReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 52),
    _FcAvgReadLatency_Type()
)
fcAvgReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcAvgReadLatency.setStatus("current")
_VmwareNFSDatastoresTotalWriteMbps_Type = Unsigned32
_VmwareNFSDatastoresTotalWriteMbps_Object = MibScalar
vmwareNFSDatastoresTotalWriteMbps = _VmwareNFSDatastoresTotalWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 53),
    _VmwareNFSDatastoresTotalWriteMbps_Type()
)
vmwareNFSDatastoresTotalWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoresTotalWriteMbps.setStatus("current")
_VmwareNFSDatastoresTotalReadMbps_Type = Unsigned32
_VmwareNFSDatastoresTotalReadMbps_Object = MibScalar
vmwareNFSDatastoresTotalReadMbps = _VmwareNFSDatastoresTotalReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 54),
    _VmwareNFSDatastoresTotalReadMbps_Type()
)
vmwareNFSDatastoresTotalReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoresTotalReadMbps.setStatus("current")
_VmwareNFSDatastoresTotalWriteIops_Type = Unsigned32
_VmwareNFSDatastoresTotalWriteIops_Object = MibScalar
vmwareNFSDatastoresTotalWriteIops = _VmwareNFSDatastoresTotalWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 55),
    _VmwareNFSDatastoresTotalWriteIops_Type()
)
vmwareNFSDatastoresTotalWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoresTotalWriteIops.setStatus("current")
_VmwareNFSDatastoresTotalReadIops_Type = Unsigned32
_VmwareNFSDatastoresTotalReadIops_Object = MibScalar
vmwareNFSDatastoresTotalReadIops = _VmwareNFSDatastoresTotalReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 56),
    _VmwareNFSDatastoresTotalReadIops_Type()
)
vmwareNFSDatastoresTotalReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoresTotalReadIops.setStatus("current")
_VmwareNFSDatastoresAvgWriteLatency_Type = Unsigned32
_VmwareNFSDatastoresAvgWriteLatency_Object = MibScalar
vmwareNFSDatastoresAvgWriteLatency = _VmwareNFSDatastoresAvgWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 57),
    _VmwareNFSDatastoresAvgWriteLatency_Type()
)
vmwareNFSDatastoresAvgWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoresAvgWriteLatency.setStatus("current")
_VmwareNFSDatastoresAvgReadLatency_Type = Unsigned32
_VmwareNFSDatastoresAvgReadLatency_Object = MibScalar
vmwareNFSDatastoresAvgReadLatency = _VmwareNFSDatastoresAvgReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 58),
    _VmwareNFSDatastoresAvgReadLatency_Type()
)
vmwareNFSDatastoresAvgReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoresAvgReadLatency.setStatus("current")
_NetworkTotalReceiveMbps_Type = Unsigned32
_NetworkTotalReceiveMbps_Object = MibScalar
networkTotalReceiveMbps = _NetworkTotalReceiveMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 59),
    _NetworkTotalReceiveMbps_Type()
)
networkTotalReceiveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkTotalReceiveMbps.setStatus("current")
_NetworkTotalTransmitMbps_Type = Unsigned32
_NetworkTotalTransmitMbps_Object = MibScalar
networkTotalTransmitMbps = _NetworkTotalTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 2, 60),
    _NetworkTotalTransmitMbps_Type()
)
networkTotalTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkTotalTransmitMbps.setStatus("current")
_Disks_ObjectIdentity = ObjectIdentity
disks = _Disks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3)
)
_DiskCount_Type = Unsigned32
_DiskCount_Object = MibScalar
diskCount = _DiskCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 1),
    _DiskCount_Type()
)
diskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCount.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1)
)
diskEntry.setIndexNames(
    (0, "TEGILE-MIB", "diskChassisIdx"),
    (0, "TEGILE-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")
_DiskChassisIdx_Type = Unsigned32
_DiskChassisIdx_Object = MibTableColumn
diskChassisIdx = _DiskChassisIdx_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 1),
    _DiskChassisIdx_Type()
)
diskChassisIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskChassisIdx.setStatus("current")
_DiskIndex_Type = Unsigned32
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 2),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskIndex.setStatus("current")
_DiskAlias_Type = DisplayString
_DiskAlias_Object = MibTableColumn
diskAlias = _DiskAlias_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 3),
    _DiskAlias_Type()
)
diskAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskAlias.setStatus("current")
_DiskSizeLow_Type = Unsigned32
_DiskSizeLow_Object = MibTableColumn
diskSizeLow = _DiskSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 4),
    _DiskSizeLow_Type()
)
diskSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSizeLow.setStatus("current")
_DiskSizeHigh_Type = Unsigned32
_DiskSizeHigh_Object = MibTableColumn
diskSizeHigh = _DiskSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 5),
    _DiskSizeHigh_Type()
)
diskSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSizeHigh.setStatus("current")
_DiskState_Type = DisplayString
_DiskState_Object = MibTableColumn
diskState = _DiskState_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 6),
    _DiskState_Type()
)
diskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskState.setStatus("current")
_DiskType_Type = DisplayString
_DiskType_Object = MibTableColumn
diskType = _DiskType_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 7),
    _DiskType_Type()
)
diskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskType.setStatus("current")
_DiskPoolName_Type = DisplayString
_DiskPoolName_Object = MibTableColumn
diskPoolName = _DiskPoolName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 3, 2, 1, 8),
    _DiskPoolName_Type()
)
diskPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPoolName.setStatus("current")
_Pools_ObjectIdentity = ObjectIdentity
pools = _Pools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4)
)
_PoolCount_Type = Unsigned32
_PoolCount_Object = MibScalar
poolCount = _PoolCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 1),
    _PoolCount_Type()
)
poolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCount.setStatus("current")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("current")
_PoolEntry_Object = MibTableRow
poolEntry = _PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1)
)
poolEntry.setIndexNames(
    (0, "TEGILE-MIB", "poolIndex"),
)
if mibBuilder.loadTexts:
    poolEntry.setStatus("current")
_PoolIndex_Type = Unsigned32
_PoolIndex_Object = MibTableColumn
poolIndex = _PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 1),
    _PoolIndex_Type()
)
poolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poolIndex.setStatus("current")
_PoolName_Type = DisplayString
_PoolName_Object = MibTableColumn
poolName = _PoolName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 2),
    _PoolName_Type()
)
poolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolName.setStatus("current")
_PoolState_Type = DisplayString
_PoolState_Object = MibTableColumn
poolState = _PoolState_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 3),
    _PoolState_Type()
)
poolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolState.setStatus("current")
_PoolHealth_Type = DisplayString
_PoolHealth_Object = MibTableColumn
poolHealth = _PoolHealth_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 4),
    _PoolHealth_Type()
)
poolHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolHealth.setStatus("current")
_PoolOwnerController_Type = DisplayString
_PoolOwnerController_Object = MibTableColumn
poolOwnerController = _PoolOwnerController_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 5),
    _PoolOwnerController_Type()
)
poolOwnerController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolOwnerController.setStatus("current")
_PoolProjectCount_Type = Unsigned32
_PoolProjectCount_Object = MibTableColumn
poolProjectCount = _PoolProjectCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 6),
    _PoolProjectCount_Type()
)
poolProjectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolProjectCount.setStatus("current")
_PoolSizeLow_Type = Unsigned32
_PoolSizeLow_Object = MibTableColumn
poolSizeLow = _PoolSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 7),
    _PoolSizeLow_Type()
)
poolSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSizeLow.setStatus("current")
_PoolSizeHigh_Type = Unsigned32
_PoolSizeHigh_Object = MibTableColumn
poolSizeHigh = _PoolSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 8),
    _PoolSizeHigh_Type()
)
poolSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSizeHigh.setStatus("current")
_PoolUsedSizeLow_Type = Unsigned32
_PoolUsedSizeLow_Object = MibTableColumn
poolUsedSizeLow = _PoolUsedSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 9),
    _PoolUsedSizeLow_Type()
)
poolUsedSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolUsedSizeLow.setStatus("current")
_PoolUsedSizeHigh_Type = Unsigned32
_PoolUsedSizeHigh_Object = MibTableColumn
poolUsedSizeHigh = _PoolUsedSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 10),
    _PoolUsedSizeHigh_Type()
)
poolUsedSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolUsedSizeHigh.setStatus("current")
_PoolFreeSizeLow_Type = Unsigned32
_PoolFreeSizeLow_Object = MibTableColumn
poolFreeSizeLow = _PoolFreeSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 11),
    _PoolFreeSizeLow_Type()
)
poolFreeSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolFreeSizeLow.setStatus("current")
_PoolFreeSizeHigh_Type = Unsigned32
_PoolFreeSizeHigh_Object = MibTableColumn
poolFreeSizeHigh = _PoolFreeSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 12),
    _PoolFreeSizeHigh_Type()
)
poolFreeSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolFreeSizeHigh.setStatus("current")
_PoolDataSizeLow_Type = Unsigned32
_PoolDataSizeLow_Object = MibTableColumn
poolDataSizeLow = _PoolDataSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 13),
    _PoolDataSizeLow_Type()
)
poolDataSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataSizeLow.setStatus("current")
_PoolDataSizeHigh_Type = Unsigned32
_PoolDataSizeHigh_Object = MibTableColumn
poolDataSizeHigh = _PoolDataSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 14),
    _PoolDataSizeHigh_Type()
)
poolDataSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataSizeHigh.setStatus("current")
_PoolPostDedupDataSizeLow_Type = Unsigned32
_PoolPostDedupDataSizeLow_Object = MibTableColumn
poolPostDedupDataSizeLow = _PoolPostDedupDataSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 15),
    _PoolPostDedupDataSizeLow_Type()
)
poolPostDedupDataSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPostDedupDataSizeLow.setStatus("current")
_PoolPostDedupDataSizeHigh_Type = Unsigned32
_PoolPostDedupDataSizeHigh_Object = MibTableColumn
poolPostDedupDataSizeHigh = _PoolPostDedupDataSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 16),
    _PoolPostDedupDataSizeHigh_Type()
)
poolPostDedupDataSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPostDedupDataSizeHigh.setStatus("current")
_PoolPostCompressionDataSizeLow_Type = Unsigned32
_PoolPostCompressionDataSizeLow_Object = MibTableColumn
poolPostCompressionDataSizeLow = _PoolPostCompressionDataSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 17),
    _PoolPostCompressionDataSizeLow_Type()
)
poolPostCompressionDataSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPostCompressionDataSizeLow.setStatus("current")
_PoolPostCompressionDataSizeHigh_Type = Unsigned32
_PoolPostCompressionDataSizeHigh_Object = MibTableColumn
poolPostCompressionDataSizeHigh = _PoolPostCompressionDataSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 18),
    _PoolPostCompressionDataSizeHigh_Type()
)
poolPostCompressionDataSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPostCompressionDataSizeHigh.setStatus("current")
_PoolUnusedReservedSizeLow_Type = Unsigned32
_PoolUnusedReservedSizeLow_Object = MibTableColumn
poolUnusedReservedSizeLow = _PoolUnusedReservedSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 19),
    _PoolUnusedReservedSizeLow_Type()
)
poolUnusedReservedSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolUnusedReservedSizeLow.setStatus("current")
_PoolUnusedReservedSizeHigh_Type = Unsigned32
_PoolUnusedReservedSizeHigh_Object = MibTableColumn
poolUnusedReservedSizeHigh = _PoolUnusedReservedSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 20),
    _PoolUnusedReservedSizeHigh_Type()
)
poolUnusedReservedSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolUnusedReservedSizeHigh.setStatus("current")
_PoolTotalSaving_Type = DisplayString
_PoolTotalSaving_Object = MibTableColumn
poolTotalSaving = _PoolTotalSaving_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 21),
    _PoolTotalSaving_Type()
)
poolTotalSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalSaving.setStatus("current")
_PoolDataWriteMbps_Type = Unsigned32
_PoolDataWriteMbps_Object = MibTableColumn
poolDataWriteMbps = _PoolDataWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 22),
    _PoolDataWriteMbps_Type()
)
poolDataWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataWriteMbps.setStatus("current")
_PoolDataReadMbps_Type = Unsigned32
_PoolDataReadMbps_Object = MibTableColumn
poolDataReadMbps = _PoolDataReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 23),
    _PoolDataReadMbps_Type()
)
poolDataReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataReadMbps.setStatus("current")
_PoolDataWriteIops_Type = Unsigned32
_PoolDataWriteIops_Object = MibTableColumn
poolDataWriteIops = _PoolDataWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 24),
    _PoolDataWriteIops_Type()
)
poolDataWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataWriteIops.setStatus("current")
_PoolDataReadIops_Type = Unsigned32
_PoolDataReadIops_Object = MibTableColumn
poolDataReadIops = _PoolDataReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 25),
    _PoolDataReadIops_Type()
)
poolDataReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataReadIops.setStatus("current")
_PoolDataWriteLatency_Type = Unsigned32
_PoolDataWriteLatency_Object = MibTableColumn
poolDataWriteLatency = _PoolDataWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 26),
    _PoolDataWriteLatency_Type()
)
poolDataWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataWriteLatency.setStatus("current")
_PoolDataReadLatency_Type = Unsigned32
_PoolDataReadLatency_Object = MibTableColumn
poolDataReadLatency = _PoolDataReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 27),
    _PoolDataReadLatency_Type()
)
poolDataReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDataReadLatency.setStatus("current")
_PoolMetaWriteMbps_Type = Unsigned32
_PoolMetaWriteMbps_Object = MibTableColumn
poolMetaWriteMbps = _PoolMetaWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 28),
    _PoolMetaWriteMbps_Type()
)
poolMetaWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMetaWriteMbps.setStatus("current")
_PoolMetaReadMbps_Type = Unsigned32
_PoolMetaReadMbps_Object = MibTableColumn
poolMetaReadMbps = _PoolMetaReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 29),
    _PoolMetaReadMbps_Type()
)
poolMetaReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMetaReadMbps.setStatus("current")
_PoolMetaWriteIops_Type = Unsigned32
_PoolMetaWriteIops_Object = MibTableColumn
poolMetaWriteIops = _PoolMetaWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 30),
    _PoolMetaWriteIops_Type()
)
poolMetaWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMetaWriteIops.setStatus("current")
_PoolMetaReadIops_Type = Unsigned32
_PoolMetaReadIops_Object = MibTableColumn
poolMetaReadIops = _PoolMetaReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 31),
    _PoolMetaReadIops_Type()
)
poolMetaReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMetaReadIops.setStatus("current")
_PoolMetaWriteLatency_Type = Unsigned32
_PoolMetaWriteLatency_Object = MibTableColumn
poolMetaWriteLatency = _PoolMetaWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 32),
    _PoolMetaWriteLatency_Type()
)
poolMetaWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMetaWriteLatency.setStatus("current")
_PoolMetaReadLatency_Type = Unsigned32
_PoolMetaReadLatency_Object = MibTableColumn
poolMetaReadLatency = _PoolMetaReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 33),
    _PoolMetaReadLatency_Type()
)
poolMetaReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMetaReadLatency.setStatus("current")
_PoolReadCacheWriteMbps_Type = Unsigned32
_PoolReadCacheWriteMbps_Object = MibTableColumn
poolReadCacheWriteMbps = _PoolReadCacheWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 34),
    _PoolReadCacheWriteMbps_Type()
)
poolReadCacheWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolReadCacheWriteMbps.setStatus("current")
_PoolReadCacheReadMbps_Type = Unsigned32
_PoolReadCacheReadMbps_Object = MibTableColumn
poolReadCacheReadMbps = _PoolReadCacheReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 35),
    _PoolReadCacheReadMbps_Type()
)
poolReadCacheReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolReadCacheReadMbps.setStatus("current")
_PoolReadCacheWriteIops_Type = Unsigned32
_PoolReadCacheWriteIops_Object = MibTableColumn
poolReadCacheWriteIops = _PoolReadCacheWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 36),
    _PoolReadCacheWriteIops_Type()
)
poolReadCacheWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolReadCacheWriteIops.setStatus("current")
_PoolReadCacheReadIops_Type = Unsigned32
_PoolReadCacheReadIops_Object = MibTableColumn
poolReadCacheReadIops = _PoolReadCacheReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 37),
    _PoolReadCacheReadIops_Type()
)
poolReadCacheReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolReadCacheReadIops.setStatus("current")
_PoolReadCacheWriteLatency_Type = Unsigned32
_PoolReadCacheWriteLatency_Object = MibTableColumn
poolReadCacheWriteLatency = _PoolReadCacheWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 38),
    _PoolReadCacheWriteLatency_Type()
)
poolReadCacheWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolReadCacheWriteLatency.setStatus("current")
_PoolReadCacheReadLatency_Type = Unsigned32
_PoolReadCacheReadLatency_Object = MibTableColumn
poolReadCacheReadLatency = _PoolReadCacheReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 39),
    _PoolReadCacheReadLatency_Type()
)
poolReadCacheReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolReadCacheReadLatency.setStatus("current")
_PoolWriteCacheWriteMbps_Type = Unsigned32
_PoolWriteCacheWriteMbps_Object = MibTableColumn
poolWriteCacheWriteMbps = _PoolWriteCacheWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 40),
    _PoolWriteCacheWriteMbps_Type()
)
poolWriteCacheWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolWriteCacheWriteMbps.setStatus("current")
_PoolWriteCacheWriteIops_Type = Unsigned32
_PoolWriteCacheWriteIops_Object = MibTableColumn
poolWriteCacheWriteIops = _PoolWriteCacheWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 41),
    _PoolWriteCacheWriteIops_Type()
)
poolWriteCacheWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolWriteCacheWriteIops.setStatus("current")
_PoolWriteCacheWriteLatency_Type = Unsigned32
_PoolWriteCacheWriteLatency_Object = MibTableColumn
poolWriteCacheWriteLatency = _PoolWriteCacheWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 2, 1, 42),
    _PoolWriteCacheWriteLatency_Type()
)
poolWriteCacheWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolWriteCacheWriteLatency.setStatus("current")
_PoolProjects_ObjectIdentity = ObjectIdentity
poolProjects = _PoolProjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3)
)
_ProjectTable_Object = MibTable
projectTable = _ProjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    projectTable.setStatus("current")
_ProjectEntry_Object = MibTableRow
projectEntry = _ProjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1)
)
projectEntry.setIndexNames(
    (0, "TEGILE-MIB", "poolIndex"),
    (0, "TEGILE-MIB", "projectIndex"),
)
if mibBuilder.loadTexts:
    projectEntry.setStatus("current")
_ProjectIndex_Type = Unsigned32
_ProjectIndex_Object = MibTableColumn
projectIndex = _ProjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 1),
    _ProjectIndex_Type()
)
projectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    projectIndex.setStatus("current")
_ProjectName_Type = DisplayString
_ProjectName_Object = MibTableColumn
projectName = _ProjectName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 2),
    _ProjectName_Type()
)
projectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectName.setStatus("current")
_ProjectPoolName_Type = DisplayString
_ProjectPoolName_Object = MibTableColumn
projectPoolName = _ProjectPoolName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 3),
    _ProjectPoolName_Type()
)
projectPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectPoolName.setStatus("current")
_ProjectDedupEnabled_Type = DisplayString
_ProjectDedupEnabled_Object = MibTableColumn
projectDedupEnabled = _ProjectDedupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 4),
    _ProjectDedupEnabled_Type()
)
projectDedupEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectDedupEnabled.setStatus("current")
_ProjectCompressionEnabled_Type = DisplayString
_ProjectCompressionEnabled_Object = MibTableColumn
projectCompressionEnabled = _ProjectCompressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 5),
    _ProjectCompressionEnabled_Type()
)
projectCompressionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectCompressionEnabled.setStatus("current")
_ProjectQuotaSizeLow_Type = Unsigned32
_ProjectQuotaSizeLow_Object = MibTableColumn
projectQuotaSizeLow = _ProjectQuotaSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 6),
    _ProjectQuotaSizeLow_Type()
)
projectQuotaSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectQuotaSizeLow.setStatus("current")
_ProjectQuotaSizeHigh_Type = Unsigned32
_ProjectQuotaSizeHigh_Object = MibTableColumn
projectQuotaSizeHigh = _ProjectQuotaSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 7),
    _ProjectQuotaSizeHigh_Type()
)
projectQuotaSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectQuotaSizeHigh.setStatus("current")
_ProjectDataSizeLow_Type = Unsigned32
_ProjectDataSizeLow_Object = MibTableColumn
projectDataSizeLow = _ProjectDataSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 8),
    _ProjectDataSizeLow_Type()
)
projectDataSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectDataSizeLow.setStatus("current")
_ProjectDataSizeHigh_Type = Unsigned32
_ProjectDataSizeHigh_Object = MibTableColumn
projectDataSizeHigh = _ProjectDataSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 9),
    _ProjectDataSizeHigh_Type()
)
projectDataSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectDataSizeHigh.setStatus("current")
_ProjectFreeSizeLow_Type = Unsigned32
_ProjectFreeSizeLow_Object = MibTableColumn
projectFreeSizeLow = _ProjectFreeSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 10),
    _ProjectFreeSizeLow_Type()
)
projectFreeSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectFreeSizeLow.setStatus("current")
_ProjectFreeSizeHigh_Type = Unsigned32
_ProjectFreeSizeHigh_Object = MibTableColumn
projectFreeSizeHigh = _ProjectFreeSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 11),
    _ProjectFreeSizeHigh_Type()
)
projectFreeSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectFreeSizeHigh.setStatus("current")
_ProjectSnapshotSizeLow_Type = Unsigned32
_ProjectSnapshotSizeLow_Object = MibTableColumn
projectSnapshotSizeLow = _ProjectSnapshotSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 12),
    _ProjectSnapshotSizeLow_Type()
)
projectSnapshotSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectSnapshotSizeLow.setStatus("current")
_ProjectSnapshotSizeHigh_Type = Unsigned32
_ProjectSnapshotSizeHigh_Object = MibTableColumn
projectSnapshotSizeHigh = _ProjectSnapshotSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 13),
    _ProjectSnapshotSizeHigh_Type()
)
projectSnapshotSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectSnapshotSizeHigh.setStatus("current")
_ProjectPostCompressionDataSizeLow_Type = Unsigned32
_ProjectPostCompressionDataSizeLow_Object = MibTableColumn
projectPostCompressionDataSizeLow = _ProjectPostCompressionDataSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 14),
    _ProjectPostCompressionDataSizeLow_Type()
)
projectPostCompressionDataSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectPostCompressionDataSizeLow.setStatus("current")
_ProjectPostCompressionDataSizeHigh_Type = Unsigned32
_ProjectPostCompressionDataSizeHigh_Object = MibTableColumn
projectPostCompressionDataSizeHigh = _ProjectPostCompressionDataSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 15),
    _ProjectPostCompressionDataSizeHigh_Type()
)
projectPostCompressionDataSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectPostCompressionDataSizeHigh.setStatus("current")
_ProjectUnusedReservedSizeLow_Type = Unsigned32
_ProjectUnusedReservedSizeLow_Object = MibTableColumn
projectUnusedReservedSizeLow = _ProjectUnusedReservedSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 16),
    _ProjectUnusedReservedSizeLow_Type()
)
projectUnusedReservedSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectUnusedReservedSizeLow.setStatus("current")
_ProjectUnusedReservedSizeHigh_Type = Unsigned32
_ProjectUnusedReservedSizeHigh_Object = MibTableColumn
projectUnusedReservedSizeHigh = _ProjectUnusedReservedSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 17),
    _ProjectUnusedReservedSizeHigh_Type()
)
projectUnusedReservedSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectUnusedReservedSizeHigh.setStatus("current")
_ProjectTotalSaving_Type = DisplayString
_ProjectTotalSaving_Object = MibTableColumn
projectTotalSaving = _ProjectTotalSaving_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 18),
    _ProjectTotalSaving_Type()
)
projectTotalSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectTotalSaving.setStatus("current")
_ProjectLunCount_Type = Unsigned32
_ProjectLunCount_Object = MibTableColumn
projectLunCount = _ProjectLunCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 19),
    _ProjectLunCount_Type()
)
projectLunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectLunCount.setStatus("current")
_ProjectShareCount_Type = Unsigned32
_ProjectShareCount_Object = MibTableColumn
projectShareCount = _ProjectShareCount_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 1, 1, 20),
    _ProjectShareCount_Type()
)
projectShareCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    projectShareCount.setStatus("current")
_ProjectLUNs_ObjectIdentity = ObjectIdentity
projectLUNs = _ProjectLUNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2)
)
_LunTable_Object = MibTable
lunTable = _LunTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3)
)
if mibBuilder.loadTexts:
    lunTable.setStatus("current")
_LunEntry_Object = MibTableRow
lunEntry = _LunEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1)
)
lunEntry.setIndexNames(
    (0, "TEGILE-MIB", "poolIndex"),
    (0, "TEGILE-MIB", "projectIndex"),
    (0, "TEGILE-MIB", "lunIndex"),
)
if mibBuilder.loadTexts:
    lunEntry.setStatus("current")
_LunIndex_Type = Unsigned32
_LunIndex_Object = MibTableColumn
lunIndex = _LunIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 1),
    _LunIndex_Type()
)
lunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lunIndex.setStatus("current")
_LunName_Type = DisplayString
_LunName_Object = MibTableColumn
lunName = _LunName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 2),
    _LunName_Type()
)
lunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunName.setStatus("current")
_LunProjectName_Type = DisplayString
_LunProjectName_Object = MibTableColumn
lunProjectName = _LunProjectName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 3),
    _LunProjectName_Type()
)
lunProjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunProjectName.setStatus("current")
_LunPoolName_Type = DisplayString
_LunPoolName_Object = MibTableColumn
lunPoolName = _LunPoolName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 4),
    _LunPoolName_Type()
)
lunPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunPoolName.setStatus("current")
_LunGUID_Type = DisplayString
_LunGUID_Object = MibTableColumn
lunGUID = _LunGUID_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 5),
    _LunGUID_Type()
)
lunGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunGUID.setStatus("current")
_LunBlockSize_Type = DisplayString
_LunBlockSize_Object = MibTableColumn
lunBlockSize = _LunBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 6),
    _LunBlockSize_Type()
)
lunBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunBlockSize.setStatus("current")
_LunDedupEnabled_Type = DisplayString
_LunDedupEnabled_Object = MibTableColumn
lunDedupEnabled = _LunDedupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 7),
    _LunDedupEnabled_Type()
)
lunDedupEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunDedupEnabled.setStatus("current")
_LunCompressionEnabled_Type = DisplayString
_LunCompressionEnabled_Object = MibTableColumn
lunCompressionEnabled = _LunCompressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 8),
    _LunCompressionEnabled_Type()
)
lunCompressionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunCompressionEnabled.setStatus("current")
_LunSizeLow_Type = Unsigned32
_LunSizeLow_Object = MibTableColumn
lunSizeLow = _LunSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 9),
    _LunSizeLow_Type()
)
lunSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSizeLow.setStatus("current")
_LunSizeHigh_Type = Unsigned32
_LunSizeHigh_Object = MibTableColumn
lunSizeHigh = _LunSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 10),
    _LunSizeHigh_Type()
)
lunSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSizeHigh.setStatus("current")
_LunDataSizeLow_Type = Unsigned32
_LunDataSizeLow_Object = MibTableColumn
lunDataSizeLow = _LunDataSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 11),
    _LunDataSizeLow_Type()
)
lunDataSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunDataSizeLow.setStatus("current")
_LunDataSizeHigh_Type = Unsigned32
_LunDataSizeHigh_Object = MibTableColumn
lunDataSizeHigh = _LunDataSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 12),
    _LunDataSizeHigh_Type()
)
lunDataSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunDataSizeHigh.setStatus("current")
_LunSnapshotSizeLow_Type = Unsigned32
_LunSnapshotSizeLow_Object = MibTableColumn
lunSnapshotSizeLow = _LunSnapshotSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 13),
    _LunSnapshotSizeLow_Type()
)
lunSnapshotSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSnapshotSizeLow.setStatus("current")
_LunSnapshotSizeHigh_Type = Unsigned32
_LunSnapshotSizeHigh_Object = MibTableColumn
lunSnapshotSizeHigh = _LunSnapshotSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 14),
    _LunSnapshotSizeHigh_Type()
)
lunSnapshotSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSnapshotSizeHigh.setStatus("current")
_LunFreeSizeLow_Type = Unsigned32
_LunFreeSizeLow_Object = MibTableColumn
lunFreeSizeLow = _LunFreeSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 15),
    _LunFreeSizeLow_Type()
)
lunFreeSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunFreeSizeLow.setStatus("current")
_LunFreeSizeHigh_Type = Unsigned32
_LunFreeSizeHigh_Object = MibTableColumn
lunFreeSizeHigh = _LunFreeSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 16),
    _LunFreeSizeHigh_Type()
)
lunFreeSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunFreeSizeHigh.setStatus("current")
_LunReservedSizeLow_Type = Unsigned32
_LunReservedSizeLow_Object = MibTableColumn
lunReservedSizeLow = _LunReservedSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 17),
    _LunReservedSizeLow_Type()
)
lunReservedSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunReservedSizeLow.setStatus("current")
_LunReservedSizeHigh_Type = Unsigned32
_LunReservedSizeHigh_Object = MibTableColumn
lunReservedSizeHigh = _LunReservedSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 18),
    _LunReservedSizeHigh_Type()
)
lunReservedSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunReservedSizeHigh.setStatus("current")
_LunCompressedRatio_Type = Unsigned32
_LunCompressedRatio_Object = MibTableColumn
lunCompressedRatio = _LunCompressedRatio_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 19),
    _LunCompressedRatio_Type()
)
lunCompressedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunCompressedRatio.setStatus("current")
_LunProtocol_Type = DisplayString
_LunProtocol_Object = MibTableColumn
lunProtocol = _LunProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 20),
    _LunProtocol_Type()
)
lunProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunProtocol.setStatus("current")
_LunTargetGroup_Type = DisplayString
_LunTargetGroup_Object = MibTableColumn
lunTargetGroup = _LunTargetGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 21),
    _LunTargetGroup_Type()
)
lunTargetGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunTargetGroup.setStatus("current")
_LunInitiatorGroup_Type = DisplayString
_LunInitiatorGroup_Object = MibTableColumn
lunInitiatorGroup = _LunInitiatorGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 22),
    _LunInitiatorGroup_Type()
)
lunInitiatorGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunInitiatorGroup.setStatus("current")
_LunWriteMbps_Type = Unsigned32
_LunWriteMbps_Object = MibTableColumn
lunWriteMbps = _LunWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 23),
    _LunWriteMbps_Type()
)
lunWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunWriteMbps.setStatus("current")
_LunReadMbps_Type = Unsigned32
_LunReadMbps_Object = MibTableColumn
lunReadMbps = _LunReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 24),
    _LunReadMbps_Type()
)
lunReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunReadMbps.setStatus("current")
_LunWriteIops_Type = Unsigned32
_LunWriteIops_Object = MibTableColumn
lunWriteIops = _LunWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 25),
    _LunWriteIops_Type()
)
lunWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunWriteIops.setStatus("current")
_LunReadIops_Type = Unsigned32
_LunReadIops_Object = MibTableColumn
lunReadIops = _LunReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 26),
    _LunReadIops_Type()
)
lunReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunReadIops.setStatus("current")
_LunWriteLatency_Type = Unsigned32
_LunWriteLatency_Object = MibTableColumn
lunWriteLatency = _LunWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 27),
    _LunWriteLatency_Type()
)
lunWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunWriteLatency.setStatus("current")
_LunReadLatency_Type = Unsigned32
_LunReadLatency_Object = MibTableColumn
lunReadLatency = _LunReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 2, 3, 1, 28),
    _LunReadLatency_Type()
)
lunReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunReadLatency.setStatus("current")
_ProjectShares_ObjectIdentity = ObjectIdentity
projectShares = _ProjectShares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3)
)
_ShareTable_Object = MibTable
shareTable = _ShareTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    shareTable.setStatus("current")
_ShareEntry_Object = MibTableRow
shareEntry = _ShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1)
)
shareEntry.setIndexNames(
    (0, "TEGILE-MIB", "poolIndex"),
    (0, "TEGILE-MIB", "projectIndex"),
    (0, "TEGILE-MIB", "shareIndex"),
)
if mibBuilder.loadTexts:
    shareEntry.setStatus("current")
_ShareIndex_Type = Unsigned32
_ShareIndex_Object = MibTableColumn
shareIndex = _ShareIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 1),
    _ShareIndex_Type()
)
shareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shareIndex.setStatus("current")
_ShareName_Type = DisplayString
_ShareName_Object = MibTableColumn
shareName = _ShareName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 2),
    _ShareName_Type()
)
shareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareName.setStatus("current")
_ShareMountPoint_Type = DisplayString
_ShareMountPoint_Object = MibTableColumn
shareMountPoint = _ShareMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 3),
    _ShareMountPoint_Type()
)
shareMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareMountPoint.setStatus("current")
_ShareProjectName_Type = DisplayString
_ShareProjectName_Object = MibTableColumn
shareProjectName = _ShareProjectName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 4),
    _ShareProjectName_Type()
)
shareProjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareProjectName.setStatus("current")
_SharePoolName_Type = DisplayString
_SharePoolName_Object = MibTableColumn
sharePoolName = _SharePoolName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 5),
    _SharePoolName_Type()
)
sharePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharePoolName.setStatus("current")
_ShareQuotaLow_Type = Unsigned32
_ShareQuotaLow_Object = MibTableColumn
shareQuotaLow = _ShareQuotaLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 6),
    _ShareQuotaLow_Type()
)
shareQuotaLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareQuotaLow.setStatus("current")
_ShareQuotaHigh_Type = Unsigned32
_ShareQuotaHigh_Object = MibTableColumn
shareQuotaHigh = _ShareQuotaHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 7),
    _ShareQuotaHigh_Type()
)
shareQuotaHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareQuotaHigh.setStatus("current")
_ShareNFSEnabled_Type = DisplayString
_ShareNFSEnabled_Object = MibTableColumn
shareNFSEnabled = _ShareNFSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 8),
    _ShareNFSEnabled_Type()
)
shareNFSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNFSEnabled.setStatus("current")
_ShareCIFSEnabled_Type = DisplayString
_ShareCIFSEnabled_Object = MibTableColumn
shareCIFSEnabled = _ShareCIFSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 9),
    _ShareCIFSEnabled_Type()
)
shareCIFSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCIFSEnabled.setStatus("current")
_ShareDedupEnabled_Type = DisplayString
_ShareDedupEnabled_Object = MibTableColumn
shareDedupEnabled = _ShareDedupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 10),
    _ShareDedupEnabled_Type()
)
shareDedupEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareDedupEnabled.setStatus("current")
_ShareCompressionEnabled_Type = DisplayString
_ShareCompressionEnabled_Object = MibTableColumn
shareCompressionEnabled = _ShareCompressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 11),
    _ShareCompressionEnabled_Type()
)
shareCompressionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCompressionEnabled.setStatus("current")
_ShareDataSizeLow_Type = Unsigned32
_ShareDataSizeLow_Object = MibTableColumn
shareDataSizeLow = _ShareDataSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 12),
    _ShareDataSizeLow_Type()
)
shareDataSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareDataSizeLow.setStatus("current")
_ShareDataSizeHigh_Type = Unsigned32
_ShareDataSizeHigh_Object = MibTableColumn
shareDataSizeHigh = _ShareDataSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 13),
    _ShareDataSizeHigh_Type()
)
shareDataSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareDataSizeHigh.setStatus("current")
_ShareSnapshotSizeLow_Type = Unsigned32
_ShareSnapshotSizeLow_Object = MibTableColumn
shareSnapshotSizeLow = _ShareSnapshotSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 14),
    _ShareSnapshotSizeLow_Type()
)
shareSnapshotSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareSnapshotSizeLow.setStatus("current")
_ShareSnapshotSizeHigh_Type = Unsigned32
_ShareSnapshotSizeHigh_Object = MibTableColumn
shareSnapshotSizeHigh = _ShareSnapshotSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 15),
    _ShareSnapshotSizeHigh_Type()
)
shareSnapshotSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareSnapshotSizeHigh.setStatus("current")
_ShareReservedSizeLow_Type = Unsigned32
_ShareReservedSizeLow_Object = MibTableColumn
shareReservedSizeLow = _ShareReservedSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 16),
    _ShareReservedSizeLow_Type()
)
shareReservedSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareReservedSizeLow.setStatus("current")
_ShareReservedSizeHigh_Type = Unsigned32
_ShareReservedSizeHigh_Object = MibTableColumn
shareReservedSizeHigh = _ShareReservedSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 17),
    _ShareReservedSizeHigh_Type()
)
shareReservedSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareReservedSizeHigh.setStatus("current")
_ShareCompressedRatio_Type = Unsigned32
_ShareCompressedRatio_Object = MibTableColumn
shareCompressedRatio = _ShareCompressedRatio_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 18),
    _ShareCompressedRatio_Type()
)
shareCompressedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCompressedRatio.setStatus("current")
_ShareCIFSWriteMbps_Type = Unsigned32
_ShareCIFSWriteMbps_Object = MibTableColumn
shareCIFSWriteMbps = _ShareCIFSWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 19),
    _ShareCIFSWriteMbps_Type()
)
shareCIFSWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCIFSWriteMbps.setStatus("current")
_ShareCIFSReadMbps_Type = Unsigned32
_ShareCIFSReadMbps_Object = MibTableColumn
shareCIFSReadMbps = _ShareCIFSReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 20),
    _ShareCIFSReadMbps_Type()
)
shareCIFSReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCIFSReadMbps.setStatus("current")
_ShareCIFSWriteIops_Type = Unsigned32
_ShareCIFSWriteIops_Object = MibTableColumn
shareCIFSWriteIops = _ShareCIFSWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 21),
    _ShareCIFSWriteIops_Type()
)
shareCIFSWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCIFSWriteIops.setStatus("current")
_ShareCIFSReadIops_Type = Unsigned32
_ShareCIFSReadIops_Object = MibTableColumn
shareCIFSReadIops = _ShareCIFSReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 22),
    _ShareCIFSReadIops_Type()
)
shareCIFSReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCIFSReadIops.setStatus("current")
_ShareCIFSWriteLatency_Type = Unsigned32
_ShareCIFSWriteLatency_Object = MibTableColumn
shareCIFSWriteLatency = _ShareCIFSWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 23),
    _ShareCIFSWriteLatency_Type()
)
shareCIFSWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCIFSWriteLatency.setStatus("current")
_ShareCIFSReadLatency_Type = Unsigned32
_ShareCIFSReadLatency_Object = MibTableColumn
shareCIFSReadLatency = _ShareCIFSReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 24),
    _ShareCIFSReadLatency_Type()
)
shareCIFSReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareCIFSReadLatency.setStatus("current")
_ShareNFSWriteMbps_Type = Unsigned32
_ShareNFSWriteMbps_Object = MibTableColumn
shareNFSWriteMbps = _ShareNFSWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 25),
    _ShareNFSWriteMbps_Type()
)
shareNFSWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNFSWriteMbps.setStatus("current")
_ShareNFSReadMbps_Type = Unsigned32
_ShareNFSReadMbps_Object = MibTableColumn
shareNFSReadMbps = _ShareNFSReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 26),
    _ShareNFSReadMbps_Type()
)
shareNFSReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNFSReadMbps.setStatus("current")
_ShareNFSWriteIops_Type = Unsigned32
_ShareNFSWriteIops_Object = MibTableColumn
shareNFSWriteIops = _ShareNFSWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 27),
    _ShareNFSWriteIops_Type()
)
shareNFSWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNFSWriteIops.setStatus("current")
_ShareNFSReadIops_Type = Unsigned32
_ShareNFSReadIops_Object = MibTableColumn
shareNFSReadIops = _ShareNFSReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 28),
    _ShareNFSReadIops_Type()
)
shareNFSReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNFSReadIops.setStatus("current")
_ShareNFSWriteLatency_Type = Unsigned32
_ShareNFSWriteLatency_Object = MibTableColumn
shareNFSWriteLatency = _ShareNFSWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 29),
    _ShareNFSWriteLatency_Type()
)
shareNFSWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNFSWriteLatency.setStatus("current")
_ShareNFSReadLatency_Type = Unsigned32
_ShareNFSReadLatency_Object = MibTableColumn
shareNFSReadLatency = _ShareNFSReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 4, 3, 3, 1, 1, 30),
    _ShareNFSReadLatency_Type()
)
shareNFSReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareNFSReadLatency.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5)
)
_NicTable_Object = MibTable
nicTable = _NicTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1)
)
if mibBuilder.loadTexts:
    nicTable.setStatus("current")
_NicEntry_Object = MibTableRow
nicEntry = _NicEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1)
)
nicEntry.setIndexNames(
    (0, "TEGILE-MIB", "nicIndex"),
)
if mibBuilder.loadTexts:
    nicEntry.setStatus("current")
_NicIndex_Type = Unsigned32
_NicIndex_Object = MibTableColumn
nicIndex = _NicIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1, 1),
    _NicIndex_Type()
)
nicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nicIndex.setStatus("current")
_NicName_Type = DisplayString
_NicName_Object = MibTableColumn
nicName = _NicName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1, 2),
    _NicName_Type()
)
nicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicName.setStatus("current")
_NicState_Type = DisplayString
_NicState_Object = MibTableColumn
nicState = _NicState_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1, 3),
    _NicState_Type()
)
nicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicState.setStatus("current")
_NicGroup_Type = DisplayString
_NicGroup_Object = MibTableColumn
nicGroup = _NicGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1, 4),
    _NicGroup_Type()
)
nicGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicGroup.setStatus("current")
_NicMTU_Type = Unsigned32
_NicMTU_Object = MibTableColumn
nicMTU = _NicMTU_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1, 5),
    _NicMTU_Type()
)
nicMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicMTU.setStatus("current")
_NicReceiveMbps_Type = Unsigned32
_NicReceiveMbps_Object = MibTableColumn
nicReceiveMbps = _NicReceiveMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1, 6),
    _NicReceiveMbps_Type()
)
nicReceiveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicReceiveMbps.setStatus("current")
_NicTransmitMbps_Type = Unsigned32
_NicTransmitMbps_Object = MibTableColumn
nicTransmitMbps = _NicTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 5, 1, 1, 7),
    _NicTransmitMbps_Type()
)
nicTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTransmitMbps.setStatus("current")
_SanProperties_ObjectIdentity = ObjectIdentity
sanProperties = _SanProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6)
)
_IscsiProperties_ObjectIdentity = ObjectIdentity
iscsiProperties = _IscsiProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1)
)
_IscsiTargets_ObjectIdentity = ObjectIdentity
iscsiTargets = _IscsiTargets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1)
)
_IscsiTargetsTable_Object = MibTable
iscsiTargetsTable = _IscsiTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiTargetsTable.setStatus("current")
_IscsiTargetEntry_Object = MibTableRow
iscsiTargetEntry = _IscsiTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1)
)
iscsiTargetEntry.setIndexNames(
    (0, "TEGILE-MIB", "iscsiTargetIndex"),
)
if mibBuilder.loadTexts:
    iscsiTargetEntry.setStatus("current")
_IscsiTargetIndex_Type = Unsigned32
_IscsiTargetIndex_Object = MibTableColumn
iscsiTargetIndex = _IscsiTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 1),
    _IscsiTargetIndex_Type()
)
iscsiTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiTargetIndex.setStatus("current")
_IscsiTargetName_Type = DisplayString
_IscsiTargetName_Object = MibTableColumn
iscsiTargetName = _IscsiTargetName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 2),
    _IscsiTargetName_Type()
)
iscsiTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetName.setStatus("current")
_IscsiTargetAlias_Type = DisplayString
_IscsiTargetAlias_Object = MibTableColumn
iscsiTargetAlias = _IscsiTargetAlias_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 3),
    _IscsiTargetAlias_Type()
)
iscsiTargetAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetAlias.setStatus("current")
_IscsiTargetGroup_Type = DisplayString
_IscsiTargetGroup_Object = MibTableColumn
iscsiTargetGroup = _IscsiTargetGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 4),
    _IscsiTargetGroup_Type()
)
iscsiTargetGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetGroup.setStatus("current")
_IscsiTargetAuth_Type = DisplayString
_IscsiTargetAuth_Object = MibTableColumn
iscsiTargetAuth = _IscsiTargetAuth_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 5),
    _IscsiTargetAuth_Type()
)
iscsiTargetAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetAuth.setStatus("current")
_IscsiTargetWriteMbps_Type = Unsigned32
_IscsiTargetWriteMbps_Object = MibTableColumn
iscsiTargetWriteMbps = _IscsiTargetWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 6),
    _IscsiTargetWriteMbps_Type()
)
iscsiTargetWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetWriteMbps.setStatus("current")
_IscsiTargetReadMbps_Type = Unsigned32
_IscsiTargetReadMbps_Object = MibTableColumn
iscsiTargetReadMbps = _IscsiTargetReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 7),
    _IscsiTargetReadMbps_Type()
)
iscsiTargetReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetReadMbps.setStatus("current")
_IscsiTargetWriteIops_Type = Unsigned32
_IscsiTargetWriteIops_Object = MibTableColumn
iscsiTargetWriteIops = _IscsiTargetWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 8),
    _IscsiTargetWriteIops_Type()
)
iscsiTargetWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetWriteIops.setStatus("current")
_IscsiTargetReadIops_Type = Unsigned32
_IscsiTargetReadIops_Object = MibTableColumn
iscsiTargetReadIops = _IscsiTargetReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 9),
    _IscsiTargetReadIops_Type()
)
iscsiTargetReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetReadIops.setStatus("current")
_IscsiTargetWriteLatency_Type = Unsigned32
_IscsiTargetWriteLatency_Object = MibTableColumn
iscsiTargetWriteLatency = _IscsiTargetWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 10),
    _IscsiTargetWriteLatency_Type()
)
iscsiTargetWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetWriteLatency.setStatus("current")
_IscsiTargetReadLatency_Type = Unsigned32
_IscsiTargetReadLatency_Object = MibTableColumn
iscsiTargetReadLatency = _IscsiTargetReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 1, 1, 1, 11),
    _IscsiTargetReadLatency_Type()
)
iscsiTargetReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTargetReadLatency.setStatus("current")
_IscsiInitiators_ObjectIdentity = ObjectIdentity
iscsiInitiators = _IscsiInitiators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 2)
)
_IscsiInitiatorsTable_Object = MibTable
iscsiInitiatorsTable = _IscsiInitiatorsTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiInitiatorsTable.setStatus("current")
_IscsiInitiatorEntry_Object = MibTableRow
iscsiInitiatorEntry = _IscsiInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 2, 1, 1)
)
iscsiInitiatorEntry.setIndexNames(
    (0, "TEGILE-MIB", "iscsiInitiatorIndex"),
)
if mibBuilder.loadTexts:
    iscsiInitiatorEntry.setStatus("current")
_IscsiInitiatorIndex_Type = Unsigned32
_IscsiInitiatorIndex_Object = MibTableColumn
iscsiInitiatorIndex = _IscsiInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 2, 1, 1, 1),
    _IscsiInitiatorIndex_Type()
)
iscsiInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiInitiatorIndex.setStatus("current")
_IscsiInitiatorName_Type = DisplayString
_IscsiInitiatorName_Object = MibTableColumn
iscsiInitiatorName = _IscsiInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 2, 1, 1, 2),
    _IscsiInitiatorName_Type()
)
iscsiInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInitiatorName.setStatus("current")
_IscsiInitiatorChapUser_Type = DisplayString
_IscsiInitiatorChapUser_Object = MibTableColumn
iscsiInitiatorChapUser = _IscsiInitiatorChapUser_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 2, 1, 1, 3),
    _IscsiInitiatorChapUser_Type()
)
iscsiInitiatorChapUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInitiatorChapUser.setStatus("current")
_IscsiInitiatorGroup_Type = DisplayString
_IscsiInitiatorGroup_Object = MibTableColumn
iscsiInitiatorGroup = _IscsiInitiatorGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 1, 2, 1, 1, 4),
    _IscsiInitiatorGroup_Type()
)
iscsiInitiatorGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInitiatorGroup.setStatus("current")
_FcProperties_ObjectIdentity = ObjectIdentity
fcProperties = _FcProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2)
)
_FcTargets_ObjectIdentity = ObjectIdentity
fcTargets = _FcTargets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1)
)
_FcTargetsTable_Object = MibTable
fcTargetsTable = _FcTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcTargetsTable.setStatus("current")
_FcTargetEntry_Object = MibTableRow
fcTargetEntry = _FcTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1)
)
fcTargetEntry.setIndexNames(
    (0, "TEGILE-MIB", "fcTargetIndex"),
)
if mibBuilder.loadTexts:
    fcTargetEntry.setStatus("current")
_FcTargetIndex_Type = Unsigned32
_FcTargetIndex_Object = MibTableColumn
fcTargetIndex = _FcTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 1),
    _FcTargetIndex_Type()
)
fcTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcTargetIndex.setStatus("current")
_FcTargetName_Type = DisplayString
_FcTargetName_Object = MibTableColumn
fcTargetName = _FcTargetName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 2),
    _FcTargetName_Type()
)
fcTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetName.setStatus("current")
_FcTargetStatus_Type = DisplayString
_FcTargetStatus_Object = MibTableColumn
fcTargetStatus = _FcTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 3),
    _FcTargetStatus_Type()
)
fcTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetStatus.setStatus("current")
_FcTargetGroup_Type = DisplayString
_FcTargetGroup_Object = MibTableColumn
fcTargetGroup = _FcTargetGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 4),
    _FcTargetGroup_Type()
)
fcTargetGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetGroup.setStatus("current")
_FcTargetWriteMbps_Type = Unsigned32
_FcTargetWriteMbps_Object = MibTableColumn
fcTargetWriteMbps = _FcTargetWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 5),
    _FcTargetWriteMbps_Type()
)
fcTargetWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetWriteMbps.setStatus("current")
_FcTargetReadMbps_Type = Unsigned32
_FcTargetReadMbps_Object = MibTableColumn
fcTargetReadMbps = _FcTargetReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 6),
    _FcTargetReadMbps_Type()
)
fcTargetReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetReadMbps.setStatus("current")
_FcTargetWriteIops_Type = Unsigned32
_FcTargetWriteIops_Object = MibTableColumn
fcTargetWriteIops = _FcTargetWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 7),
    _FcTargetWriteIops_Type()
)
fcTargetWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetWriteIops.setStatus("current")
_FcTargetReadIops_Type = Unsigned32
_FcTargetReadIops_Object = MibTableColumn
fcTargetReadIops = _FcTargetReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 8),
    _FcTargetReadIops_Type()
)
fcTargetReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetReadIops.setStatus("current")
_FcTargetWriteLatency_Type = Unsigned32
_FcTargetWriteLatency_Object = MibTableColumn
fcTargetWriteLatency = _FcTargetWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 9),
    _FcTargetWriteLatency_Type()
)
fcTargetWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetWriteLatency.setStatus("current")
_FcTargetReadLatency_Type = Unsigned32
_FcTargetReadLatency_Object = MibTableColumn
fcTargetReadLatency = _FcTargetReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 1, 1, 1, 10),
    _FcTargetReadLatency_Type()
)
fcTargetReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetReadLatency.setStatus("current")
_FcInitiators_ObjectIdentity = ObjectIdentity
fcInitiators = _FcInitiators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 2)
)
_FcInitiatorsTable_Object = MibTable
fcInitiatorsTable = _FcInitiatorsTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fcInitiatorsTable.setStatus("current")
_FcInitiatorEntry_Object = MibTableRow
fcInitiatorEntry = _FcInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 2, 1, 1)
)
fcInitiatorEntry.setIndexNames(
    (0, "TEGILE-MIB", "fcInitiatorIndex"),
)
if mibBuilder.loadTexts:
    fcInitiatorEntry.setStatus("current")
_FcInitiatorIndex_Type = Unsigned32
_FcInitiatorIndex_Object = MibTableColumn
fcInitiatorIndex = _FcInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 2, 1, 1, 1),
    _FcInitiatorIndex_Type()
)
fcInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcInitiatorIndex.setStatus("current")
_FcInitiatorName_Type = DisplayString
_FcInitiatorName_Object = MibTableColumn
fcInitiatorName = _FcInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 2, 1, 1, 2),
    _FcInitiatorName_Type()
)
fcInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInitiatorName.setStatus("current")
_FcInitiatorGroup_Type = DisplayString
_FcInitiatorGroup_Object = MibTableColumn
fcInitiatorGroup = _FcInitiatorGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 6, 2, 2, 1, 1, 3),
    _FcInitiatorGroup_Type()
)
fcInitiatorGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInitiatorGroup.setStatus("current")
_VmwareNFSDatastores_ObjectIdentity = ObjectIdentity
vmwareNFSDatastores = _VmwareNFSDatastores_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7)
)
_VmwareNFSDatastoresTable_Object = MibTable
vmwareNFSDatastoresTable = _VmwareNFSDatastoresTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1)
)
if mibBuilder.loadTexts:
    vmwareNFSDatastoresTable.setStatus("current")
_VmwareNFSDatastoreEntry_Object = MibTableRow
vmwareNFSDatastoreEntry = _VmwareNFSDatastoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1)
)
vmwareNFSDatastoreEntry.setIndexNames(
    (0, "TEGILE-MIB", "vmwareNFSDatastoreIndex"),
)
if mibBuilder.loadTexts:
    vmwareNFSDatastoreEntry.setStatus("current")
_VmwareNFSDatastoreIndex_Type = Unsigned32
_VmwareNFSDatastoreIndex_Object = MibTableColumn
vmwareNFSDatastoreIndex = _VmwareNFSDatastoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 1),
    _VmwareNFSDatastoreIndex_Type()
)
vmwareNFSDatastoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreIndex.setStatus("current")
_VmwareNFSDatastoreVMName_Type = DisplayString
_VmwareNFSDatastoreVMName_Object = MibTableColumn
vmwareNFSDatastoreVMName = _VmwareNFSDatastoreVMName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 2),
    _VmwareNFSDatastoreVMName_Type()
)
vmwareNFSDatastoreVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreVMName.setStatus("current")
_VmwareNFSDatastoreESXName_Type = DisplayString
_VmwareNFSDatastoreESXName_Object = MibTableColumn
vmwareNFSDatastoreESXName = _VmwareNFSDatastoreESXName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 3),
    _VmwareNFSDatastoreESXName_Type()
)
vmwareNFSDatastoreESXName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreESXName.setStatus("current")
_VmwareNFSDatastoreWriteMbps_Type = Unsigned32
_VmwareNFSDatastoreWriteMbps_Object = MibTableColumn
vmwareNFSDatastoreWriteMbps = _VmwareNFSDatastoreWriteMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 4),
    _VmwareNFSDatastoreWriteMbps_Type()
)
vmwareNFSDatastoreWriteMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreWriteMbps.setStatus("current")
_VmwareNFSDatastoreReadMbps_Type = Unsigned32
_VmwareNFSDatastoreReadMbps_Object = MibTableColumn
vmwareNFSDatastoreReadMbps = _VmwareNFSDatastoreReadMbps_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 5),
    _VmwareNFSDatastoreReadMbps_Type()
)
vmwareNFSDatastoreReadMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreReadMbps.setStatus("current")
_VmwareNFSDatastoreWriteIops_Type = Unsigned32
_VmwareNFSDatastoreWriteIops_Object = MibTableColumn
vmwareNFSDatastoreWriteIops = _VmwareNFSDatastoreWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 6),
    _VmwareNFSDatastoreWriteIops_Type()
)
vmwareNFSDatastoreWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreWriteIops.setStatus("current")
_VmwareNFSDatastoreReadIops_Type = Unsigned32
_VmwareNFSDatastoreReadIops_Object = MibTableColumn
vmwareNFSDatastoreReadIops = _VmwareNFSDatastoreReadIops_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 7),
    _VmwareNFSDatastoreReadIops_Type()
)
vmwareNFSDatastoreReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreReadIops.setStatus("current")
_VmwareNFSDatastoreWriteLatency_Type = Unsigned32
_VmwareNFSDatastoreWriteLatency_Object = MibTableColumn
vmwareNFSDatastoreWriteLatency = _VmwareNFSDatastoreWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 8),
    _VmwareNFSDatastoreWriteLatency_Type()
)
vmwareNFSDatastoreWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreWriteLatency.setStatus("current")
_VmwareNFSDatastoreReadLatency_Type = Unsigned32
_VmwareNFSDatastoreReadLatency_Object = MibTableColumn
vmwareNFSDatastoreReadLatency = _VmwareNFSDatastoreReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 7, 1, 1, 9),
    _VmwareNFSDatastoreReadLatency_Type()
)
vmwareNFSDatastoreReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwareNFSDatastoreReadLatency.setStatus("current")
_HaResources_ObjectIdentity = ObjectIdentity
haResources = _HaResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8)
)
_HaResourcesTable_Object = MibTable
haResourcesTable = _HaResourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1)
)
if mibBuilder.loadTexts:
    haResourcesTable.setStatus("current")
_HaResourceEntry_Object = MibTableRow
haResourceEntry = _HaResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1, 1)
)
haResourceEntry.setIndexNames(
    (0, "TEGILE-MIB", "haResourceIndex"),
)
if mibBuilder.loadTexts:
    haResourceEntry.setStatus("current")
_HaResourceIndex_Type = Unsigned32
_HaResourceIndex_Object = MibTableColumn
haResourceIndex = _HaResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1, 1, 1),
    _HaResourceIndex_Type()
)
haResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    haResourceIndex.setStatus("current")
_HaResourceName_Type = DisplayString
_HaResourceName_Object = MibTableColumn
haResourceName = _HaResourceName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1, 1, 2),
    _HaResourceName_Type()
)
haResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haResourceName.setStatus("current")
_HaResourceDescription_Type = DisplayString
_HaResourceDescription_Object = MibTableColumn
haResourceDescription = _HaResourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1, 1, 3),
    _HaResourceDescription_Type()
)
haResourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haResourceDescription.setStatus("current")
_HaResourceStatus_Type = DisplayString
_HaResourceStatus_Object = MibTableColumn
haResourceStatus = _HaResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1, 1, 4),
    _HaResourceStatus_Type()
)
haResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haResourceStatus.setStatus("current")
_HaResourceGroup_Type = DisplayString
_HaResourceGroup_Object = MibTableColumn
haResourceGroup = _HaResourceGroup_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1, 1, 5),
    _HaResourceGroup_Type()
)
haResourceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haResourceGroup.setStatus("current")
_HaResourceActiveNode_Type = DisplayString
_HaResourceActiveNode_Object = MibTableColumn
haResourceActiveNode = _HaResourceActiveNode_Object(
    (1, 3, 6, 1, 4, 1, 43906, 1, 8, 1, 1, 6),
    _HaResourceActiveNode_Type()
)
haResourceActiveNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haResourceActiveNode.setStatus("current")
_TegileArray_notifications_ObjectIdentity = ObjectIdentity
tegileArray_notifications = _TegileArray_notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 2)
)
_NotificationObjects_ObjectIdentity = ObjectIdentity
notificationObjects = _NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1)
)
_NotificationProps_ObjectIdentity = ObjectIdentity
notificationProps = _NotificationProps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1)
)
_NotificationDescription_Type = DisplayString
_NotificationDescription_Object = MibScalar
notificationDescription = _NotificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 1),
    _NotificationDescription_Type()
)
notificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationDescription.setStatus("current")
_NotificationTime_Type = DisplayString
_NotificationTime_Object = MibScalar
notificationTime = _NotificationTime_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 2),
    _NotificationTime_Type()
)
notificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationTime.setStatus("current")
_NotificationSeverity_Type = DisplayString
_NotificationSeverity_Object = MibScalar
notificationSeverity = _NotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 3),
    _NotificationSeverity_Type()
)
notificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationSeverity.setStatus("current")
_NotificationComponentName_Type = DisplayString
_NotificationComponentName_Object = MibScalar
notificationComponentName = _NotificationComponentName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 4),
    _NotificationComponentName_Type()
)
notificationComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationComponentName.setStatus("current")
_NotificationTargetEntityName_Type = DisplayString
_NotificationTargetEntityName_Object = MibScalar
notificationTargetEntityName = _NotificationTargetEntityName_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 5),
    _NotificationTargetEntityName_Type()
)
notificationTargetEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationTargetEntityName.setStatus("current")
_NotificationEventCode_Type = DisplayString
_NotificationEventCode_Object = MibScalar
notificationEventCode = _NotificationEventCode_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 6),
    _NotificationEventCode_Type()
)
notificationEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationEventCode.setStatus("current")
_NotificationSensorAction_Type = DisplayString
_NotificationSensorAction_Object = MibScalar
notificationSensorAction = _NotificationSensorAction_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 7),
    _NotificationSensorAction_Type()
)
notificationSensorAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationSensorAction.setStatus("current")
_NotificationSensorNumber_Type = DisplayString
_NotificationSensorNumber_Object = MibScalar
notificationSensorNumber = _NotificationSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 8),
    _NotificationSensorNumber_Type()
)
notificationSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationSensorNumber.setStatus("current")
_NotificationSensorSuspect_Type = DisplayString
_NotificationSensorSuspect_Object = MibScalar
notificationSensorSuspect = _NotificationSensorSuspect_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 9),
    _NotificationSensorSuspect_Type()
)
notificationSensorSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationSensorSuspect.setStatus("current")
_NotificationReadingTriggerValue_Type = DisplayString
_NotificationReadingTriggerValue_Object = MibScalar
notificationReadingTriggerValue = _NotificationReadingTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 10),
    _NotificationReadingTriggerValue_Type()
)
notificationReadingTriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationReadingTriggerValue.setStatus("current")
_NotificationThresholdTriggerValue_Type = DisplayString
_NotificationThresholdTriggerValue_Object = MibScalar
notificationThresholdTriggerValue = _NotificationThresholdTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 11),
    _NotificationThresholdTriggerValue_Type()
)
notificationThresholdTriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationThresholdTriggerValue.setStatus("current")
_NotificationReadingUnit_Type = DisplayString
_NotificationReadingUnit_Object = MibScalar
notificationReadingUnit = _NotificationReadingUnit_Object(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 1, 12),
    _NotificationReadingUnit_Type()
)
notificationReadingUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationReadingUnit.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2)
)
_TegileConformance_ObjectIdentity = ObjectIdentity
tegileConformance = _TegileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 3)
)
_TegileGroups_ObjectIdentity = ObjectIdentity
tegileGroups = _TegileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 3, 1)
)
_TegileCompliances_ObjectIdentity = ObjectIdentity
tegileCompliances = _TegileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43906, 3, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43906, 3, 1, 1)
)
currentObjectGroup.setObjects(
      *(("TEGILE-MIB", "haControllerA-Name"),
        ("TEGILE-MIB", "haControllerA-IPAddr"),
        ("TEGILE-MIB", "haControllerA-SoftwareVersion"),
        ("TEGILE-MIB", "haControllerA-Uptime"),
        ("TEGILE-MIB", "haControllerB-Name"),
        ("TEGILE-MIB", "haControllerB-IPAddr"),
        ("TEGILE-MIB", "haControllerB-SoftwareVersion"),
        ("TEGILE-MIB", "haControllerB-Uptime"),
        ("TEGILE-MIB", "controllerHardwareModel"),
        ("TEGILE-MIB", "snmpAgentVersion"),
        ("TEGILE-MIB", "cpuTotalUsage"),
        ("TEGILE-MIB", "cpuSystemCalls"),
        ("TEGILE-MIB", "cpuInterrupts"),
        ("TEGILE-MIB", "cacheTotalWriteMbps"),
        ("TEGILE-MIB", "cacheTotalReadMbps"),
        ("TEGILE-MIB", "cacheTotalWriteIops"),
        ("TEGILE-MIB", "cacheTotalReadIops"),
        ("TEGILE-MIB", "cacheRAMReads"),
        ("TEGILE-MIB", "cacheSSDReads"),
        ("TEGILE-MIB", "diskTotalWriteMbps"),
        ("TEGILE-MIB", "diskTotalReadMbps"),
        ("TEGILE-MIB", "diskTotalWriteIops"),
        ("TEGILE-MIB", "diskTotalReadIops"),
        ("TEGILE-MIB", "diskDataWriteMbps"),
        ("TEGILE-MIB", "diskDataReadMbps"),
        ("TEGILE-MIB", "diskDataWriteIops"),
        ("TEGILE-MIB", "diskDataReadIops"),
        ("TEGILE-MIB", "diskAvgWriteLatency"),
        ("TEGILE-MIB", "diskAvgReadLatency"),
        ("TEGILE-MIB", "diskIOCount"),
        ("TEGILE-MIB", "diskRandomIOCount"),
        ("TEGILE-MIB", "diskSequentialIOCount"),
        ("TEGILE-MIB", "poolTotalWriteMbps"),
        ("TEGILE-MIB", "poolTotalReadMbps"),
        ("TEGILE-MIB", "poolTotalWriteIops"),
        ("TEGILE-MIB", "poolTotalReadIops"),
        ("TEGILE-MIB", "poolAvgWriteLatency"),
        ("TEGILE-MIB", "poolAvgReadLatency"),
        ("TEGILE-MIB", "cifsTotalWriteMbps"),
        ("TEGILE-MIB", "cifsTotalReadMbps"),
        ("TEGILE-MIB", "cifsTotalWriteIops"),
        ("TEGILE-MIB", "cifsTotalReadIops"),
        ("TEGILE-MIB", "cifsAvgWriteLatency"),
        ("TEGILE-MIB", "cifsAvgReadLatency"),
        ("TEGILE-MIB", "nfsTotalWriteMbps"),
        ("TEGILE-MIB", "nfsTotalReadMbps"),
        ("TEGILE-MIB", "nfsTotalWriteIops"),
        ("TEGILE-MIB", "nfsTotalReadIops"),
        ("TEGILE-MIB", "nfsAvgWriteLatency"),
        ("TEGILE-MIB", "nfsAvgReadLatency"),
        ("TEGILE-MIB", "iscsiTotalWriteMbps"),
        ("TEGILE-MIB", "iscsiTotalReadMbps"),
        ("TEGILE-MIB", "iscsiWriteIops"),
        ("TEGILE-MIB", "iscsiTotalReadIops"),
        ("TEGILE-MIB", "iscsiAvgWriteLatency"),
        ("TEGILE-MIB", "iscsiAvgReadLatency"),
        ("TEGILE-MIB", "fcTotalWriteMbps"),
        ("TEGILE-MIB", "fcTotalReadMbps"),
        ("TEGILE-MIB", "fcTotalWriteIops"),
        ("TEGILE-MIB", "fcTotalReadIops"),
        ("TEGILE-MIB", "fcAvgWriteLatency"),
        ("TEGILE-MIB", "fcAvgReadLatency"),
        ("TEGILE-MIB", "vmwareNFSDatastoresTotalWriteMbps"),
        ("TEGILE-MIB", "vmwareNFSDatastoresTotalReadMbps"),
        ("TEGILE-MIB", "vmwareNFSDatastoresTotalWriteIops"),
        ("TEGILE-MIB", "vmwareNFSDatastoresTotalReadIops"),
        ("TEGILE-MIB", "vmwareNFSDatastoresAvgWriteLatency"),
        ("TEGILE-MIB", "vmwareNFSDatastoresAvgReadLatency"),
        ("TEGILE-MIB", "networkTotalReceiveMbps"),
        ("TEGILE-MIB", "networkTotalTransmitMbps"),
        ("TEGILE-MIB", "diskCount"),
        ("TEGILE-MIB", "diskAlias"),
        ("TEGILE-MIB", "diskSizeLow"),
        ("TEGILE-MIB", "diskSizeHigh"),
        ("TEGILE-MIB", "diskState"),
        ("TEGILE-MIB", "diskType"),
        ("TEGILE-MIB", "diskPoolName"),
        ("TEGILE-MIB", "poolCount"),
        ("TEGILE-MIB", "poolName"),
        ("TEGILE-MIB", "poolState"),
        ("TEGILE-MIB", "poolHealth"),
        ("TEGILE-MIB", "poolOwnerController"),
        ("TEGILE-MIB", "poolProjectCount"),
        ("TEGILE-MIB", "poolSizeLow"),
        ("TEGILE-MIB", "poolSizeHigh"),
        ("TEGILE-MIB", "poolUsedSizeLow"),
        ("TEGILE-MIB", "poolUsedSizeHigh"),
        ("TEGILE-MIB", "poolFreeSizeLow"),
        ("TEGILE-MIB", "poolFreeSizeHigh"),
        ("TEGILE-MIB", "poolDataSizeLow"),
        ("TEGILE-MIB", "poolDataSizeHigh"),
        ("TEGILE-MIB", "poolPostDedupDataSizeLow"),
        ("TEGILE-MIB", "poolPostDedupDataSizeHigh"),
        ("TEGILE-MIB", "poolPostCompressionDataSizeLow"),
        ("TEGILE-MIB", "poolPostCompressionDataSizeHigh"),
        ("TEGILE-MIB", "poolUnusedReservedSizeLow"),
        ("TEGILE-MIB", "poolUnusedReservedSizeHigh"),
        ("TEGILE-MIB", "poolTotalSaving"),
        ("TEGILE-MIB", "poolDataWriteMbps"),
        ("TEGILE-MIB", "poolDataReadMbps"),
        ("TEGILE-MIB", "poolDataWriteIops"),
        ("TEGILE-MIB", "poolDataReadIops"),
        ("TEGILE-MIB", "poolDataWriteLatency"),
        ("TEGILE-MIB", "poolDataReadLatency"),
        ("TEGILE-MIB", "poolMetaWriteMbps"),
        ("TEGILE-MIB", "poolMetaReadMbps"),
        ("TEGILE-MIB", "poolMetaWriteIops"),
        ("TEGILE-MIB", "poolMetaReadIops"),
        ("TEGILE-MIB", "poolMetaWriteLatency"),
        ("TEGILE-MIB", "poolMetaReadLatency"),
        ("TEGILE-MIB", "poolReadCacheWriteMbps"),
        ("TEGILE-MIB", "poolReadCacheReadMbps"),
        ("TEGILE-MIB", "poolReadCacheWriteIops"),
        ("TEGILE-MIB", "poolReadCacheReadIops"),
        ("TEGILE-MIB", "poolReadCacheWriteLatency"),
        ("TEGILE-MIB", "poolReadCacheReadLatency"),
        ("TEGILE-MIB", "poolWriteCacheWriteMbps"),
        ("TEGILE-MIB", "poolWriteCacheWriteIops"),
        ("TEGILE-MIB", "poolWriteCacheWriteLatency"),
        ("TEGILE-MIB", "projectName"),
        ("TEGILE-MIB", "projectPoolName"),
        ("TEGILE-MIB", "projectDedupEnabled"),
        ("TEGILE-MIB", "projectCompressionEnabled"),
        ("TEGILE-MIB", "projectQuotaSizeLow"),
        ("TEGILE-MIB", "projectQuotaSizeHigh"),
        ("TEGILE-MIB", "projectDataSizeLow"),
        ("TEGILE-MIB", "projectDataSizeHigh"),
        ("TEGILE-MIB", "projectFreeSizeLow"),
        ("TEGILE-MIB", "projectFreeSizeHigh"),
        ("TEGILE-MIB", "projectSnapshotSizeLow"),
        ("TEGILE-MIB", "projectSnapshotSizeHigh"),
        ("TEGILE-MIB", "projectPostCompressionDataSizeLow"),
        ("TEGILE-MIB", "projectPostCompressionDataSizeHigh"),
        ("TEGILE-MIB", "projectUnusedReservedSizeLow"),
        ("TEGILE-MIB", "projectUnusedReservedSizeHigh"),
        ("TEGILE-MIB", "projectTotalSaving"),
        ("TEGILE-MIB", "projectLunCount"),
        ("TEGILE-MIB", "projectShareCount"),
        ("TEGILE-MIB", "lunName"),
        ("TEGILE-MIB", "lunProjectName"),
        ("TEGILE-MIB", "lunPoolName"),
        ("TEGILE-MIB", "lunGUID"),
        ("TEGILE-MIB", "lunBlockSize"),
        ("TEGILE-MIB", "lunDedupEnabled"),
        ("TEGILE-MIB", "lunCompressionEnabled"),
        ("TEGILE-MIB", "lunSizeLow"),
        ("TEGILE-MIB", "lunSizeHigh"),
        ("TEGILE-MIB", "lunDataSizeLow"),
        ("TEGILE-MIB", "lunDataSizeHigh"),
        ("TEGILE-MIB", "lunSnapshotSizeLow"),
        ("TEGILE-MIB", "lunSnapshotSizeHigh"),
        ("TEGILE-MIB", "lunFreeSizeLow"),
        ("TEGILE-MIB", "lunFreeSizeHigh"),
        ("TEGILE-MIB", "lunReservedSizeLow"),
        ("TEGILE-MIB", "lunReservedSizeHigh"),
        ("TEGILE-MIB", "lunCompressedRatio"),
        ("TEGILE-MIB", "lunProtocol"),
        ("TEGILE-MIB", "lunTargetGroup"),
        ("TEGILE-MIB", "lunInitiatorGroup"),
        ("TEGILE-MIB", "lunWriteMbps"),
        ("TEGILE-MIB", "lunReadMbps"),
        ("TEGILE-MIB", "lunWriteIops"),
        ("TEGILE-MIB", "lunReadIops"),
        ("TEGILE-MIB", "lunWriteLatency"),
        ("TEGILE-MIB", "lunReadLatency"),
        ("TEGILE-MIB", "shareName"),
        ("TEGILE-MIB", "shareMountPoint"),
        ("TEGILE-MIB", "shareProjectName"),
        ("TEGILE-MIB", "sharePoolName"),
        ("TEGILE-MIB", "shareQuotaLow"),
        ("TEGILE-MIB", "shareQuotaHigh"),
        ("TEGILE-MIB", "shareNFSEnabled"),
        ("TEGILE-MIB", "shareCIFSEnabled"),
        ("TEGILE-MIB", "shareDedupEnabled"),
        ("TEGILE-MIB", "shareCompressionEnabled"),
        ("TEGILE-MIB", "shareDataSizeLow"),
        ("TEGILE-MIB", "shareDataSizeHigh"),
        ("TEGILE-MIB", "shareSnapshotSizeLow"),
        ("TEGILE-MIB", "shareSnapshotSizeHigh"),
        ("TEGILE-MIB", "shareReservedSizeLow"),
        ("TEGILE-MIB", "shareReservedSizeHigh"),
        ("TEGILE-MIB", "shareCompressedRatio"),
        ("TEGILE-MIB", "shareCIFSWriteMbps"),
        ("TEGILE-MIB", "shareCIFSReadMbps"),
        ("TEGILE-MIB", "shareCIFSWriteIops"),
        ("TEGILE-MIB", "shareCIFSReadIops"),
        ("TEGILE-MIB", "shareCIFSWriteLatency"),
        ("TEGILE-MIB", "shareCIFSReadLatency"),
        ("TEGILE-MIB", "shareNFSWriteMbps"),
        ("TEGILE-MIB", "shareNFSReadMbps"),
        ("TEGILE-MIB", "shareNFSWriteIops"),
        ("TEGILE-MIB", "shareNFSReadIops"),
        ("TEGILE-MIB", "shareNFSWriteLatency"),
        ("TEGILE-MIB", "shareNFSReadLatency"),
        ("TEGILE-MIB", "iscsiTargetName"),
        ("TEGILE-MIB", "iscsiTargetAlias"),
        ("TEGILE-MIB", "iscsiTargetGroup"),
        ("TEGILE-MIB", "iscsiTargetAuth"),
        ("TEGILE-MIB", "iscsiTargetWriteMbps"),
        ("TEGILE-MIB", "iscsiTargetReadMbps"),
        ("TEGILE-MIB", "iscsiTargetWriteIops"),
        ("TEGILE-MIB", "iscsiTargetReadIops"),
        ("TEGILE-MIB", "iscsiTargetWriteLatency"),
        ("TEGILE-MIB", "iscsiTargetReadLatency"),
        ("TEGILE-MIB", "iscsiInitiatorName"),
        ("TEGILE-MIB", "iscsiInitiatorChapUser"),
        ("TEGILE-MIB", "iscsiInitiatorGroup"),
        ("TEGILE-MIB", "fcTargetName"),
        ("TEGILE-MIB", "fcTargetStatus"),
        ("TEGILE-MIB", "fcTargetGroup"),
        ("TEGILE-MIB", "fcTargetWriteMbps"),
        ("TEGILE-MIB", "fcTargetReadMbps"),
        ("TEGILE-MIB", "fcTargetWriteIops"),
        ("TEGILE-MIB", "fcTargetReadIops"),
        ("TEGILE-MIB", "fcTargetWriteLatency"),
        ("TEGILE-MIB", "fcTargetReadLatency"),
        ("TEGILE-MIB", "fcInitiatorName"),
        ("TEGILE-MIB", "fcInitiatorGroup"),
        ("TEGILE-MIB", "vmwareNFSDatastoreVMName"),
        ("TEGILE-MIB", "vmwareNFSDatastoreESXName"),
        ("TEGILE-MIB", "vmwareNFSDatastoreWriteMbps"),
        ("TEGILE-MIB", "vmwareNFSDatastoreReadMbps"),
        ("TEGILE-MIB", "vmwareNFSDatastoreWriteIops"),
        ("TEGILE-MIB", "vmwareNFSDatastoreReadIops"),
        ("TEGILE-MIB", "vmwareNFSDatastoreWriteLatency"),
        ("TEGILE-MIB", "vmwareNFSDatastoreReadLatency"),
        ("TEGILE-MIB", "haResourceName"),
        ("TEGILE-MIB", "haResourceDescription"),
        ("TEGILE-MIB", "haResourceStatus"),
        ("TEGILE-MIB", "haResourceGroup"),
        ("TEGILE-MIB", "haResourceActiveNode"),
        ("TEGILE-MIB", "nicName"),
        ("TEGILE-MIB", "nicState"),
        ("TEGILE-MIB", "nicGroup"),
        ("TEGILE-MIB", "nicMTU"),
        ("TEGILE-MIB", "nicReceiveMbps"),
        ("TEGILE-MIB", "nicTransmitMbps"),
        ("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"),
        ("TEGILE-MIB", "notificationReadingTriggerValue"),
        ("TEGILE-MIB", "notificationThresholdTriggerValue"),
        ("TEGILE-MIB", "notificationReadingUnit"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects

testNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 10)
)
testNotification.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    testNotification.setStatus(
        "current"
    )

diskIsOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 101)
)
diskIsOnline.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    diskIsOnline.setStatus(
        "current"
    )

diskGoneOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 102)
)
diskGoneOffline.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    diskGoneOffline.setStatus(
        "current"
    )

diskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 103)
)
diskError.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    diskError.setStatus(
        "current"
    )

spareDiskReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 104)
)
spareDiskReplaced.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    spareDiskReplaced.setStatus(
        "current"
    )

diskSlowIo = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 105)
)
diskSlowIo.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    diskSlowIo.setStatus(
        "current"
    )

poolCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 201)
)
poolCreated.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolCreated.setStatus(
        "current"
    )

poolDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 202)
)
poolDeleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolDeleted.setStatus(
        "current"
    )

poolDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 203)
)
poolDeletionFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolDeletionFailed.setStatus(
        "current"
    )

poolExpanded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 204)
)
poolExpanded.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolExpanded.setStatus(
        "current"
    )

poolExported = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 205)
)
poolExported.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolExported.setStatus(
        "current"
    )

poolImported = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 206)
)
poolImported.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolImported.setStatus(
        "current"
    )

poolUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 207)
)
poolUpgraded.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolUpgraded.setStatus(
        "current"
    )

poolQuotaExceedThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 208)
)
poolQuotaExceedThresholdWarning.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolQuotaExceedThresholdWarning.setStatus(
        "current"
    )

poolMetaDataQuotaExceedThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 209)
)
poolMetaDataQuotaExceedThresholdWarning.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolMetaDataQuotaExceedThresholdWarning.setStatus(
        "current"
    )

poolAvailableMetaToDataRatioBelowThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 210)
)
poolAvailableMetaToDataRatioBelowThresholdWarning.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolAvailableMetaToDataRatioBelowThresholdWarning.setStatus(
        "current"
    )

poolQuotaFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 211)
)
poolQuotaFinished.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolQuotaFinished.setStatus(
        "current"
    )

poolDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 212)
)
poolDegraded.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    poolDegraded.setStatus(
        "current"
    )

projectCreatedSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 301)
)
projectCreatedSuccessfully.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    projectCreatedSuccessfully.setStatus(
        "current"
    )

projectDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 302)
)
projectDeletionFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    projectDeletionFailed.setStatus(
        "current"
    )

projectDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 303)
)
projectDeleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    projectDeleted.setStatus(
        "current"
    )

projectModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 304)
)
projectModified.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    projectModified.setStatus(
        "current"
    )

projectThresholdExceedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 305)
)
projectThresholdExceedWarning.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    projectThresholdExceedWarning.setStatus(
        "current"
    )

projectQuotaFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 306)
)
projectQuotaFinished.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    projectQuotaFinished.setStatus(
        "current"
    )

projectCreatedWithNonOptimalBlockSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 307)
)
projectCreatedWithNonOptimalBlockSize.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    projectCreatedWithNonOptimalBlockSize.setStatus(
        "current"
    )

volumeCreatedSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 401)
)
volumeCreatedSuccessfully.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    volumeCreatedSuccessfully.setStatus(
        "current"
    )

volumeModifyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 402)
)
volumeModifyCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    volumeModifyCompleted.setStatus(
        "current"
    )

volumeDeleteCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 403)
)
volumeDeleteCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    volumeDeleteCompleted.setStatus(
        "current"
    )

volumeDeleteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 404)
)
volumeDeleteFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    volumeDeleteFailed.setStatus(
        "current"
    )

volumeExceedsThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 405)
)
volumeExceedsThresholdWarning.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    volumeExceedsThresholdWarning.setStatus(
        "current"
    )

volumeQuotaFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 406)
)
volumeQuotaFinished.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    volumeQuotaFinished.setStatus(
        "current"
    )

volumeCreatedWithNonOptimalBlockSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 407)
)
volumeCreatedWithNonOptimalBlockSize.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    volumeCreatedWithNonOptimalBlockSize.setStatus(
        "current"
    )

shareCreatedSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 501)
)
shareCreatedSuccessfully.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    shareCreatedSuccessfully.setStatus(
        "current"
    )

shareDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 502)
)
shareDeletionFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    shareDeletionFailed.setStatus(
        "current"
    )

shareDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 503)
)
shareDeleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    shareDeleted.setStatus(
        "current"
    )

shareExceedThresholdWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 504)
)
shareExceedThresholdWarning.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    shareExceedThresholdWarning.setStatus(
        "current"
    )

shareQuotaFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 505)
)
shareQuotaFinished.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    shareQuotaFinished.setStatus(
        "current"
    )

shareCreatedWithNonOptimalBlockSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 506)
)
shareCreatedWithNonOptimalBlockSize.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    shareCreatedWithNonOptimalBlockSize.setStatus(
        "current"
    )

aclMigrationStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 601)
)
aclMigrationStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    aclMigrationStarted.setStatus(
        "current"
    )

aclMigrationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 602)
)
aclMigrationCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    aclMigrationCompleted.setStatus(
        "current"
    )

deleteFolderCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 701)
)
deleteFolderCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    deleteFolderCompleted.setStatus(
        "current"
    )

deleteFolderFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 702)
)
deleteFolderFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    deleteFolderFailed.setStatus(
        "current"
    )

snapshotCreatedSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 801)
)
snapshotCreatedSuccessfully.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotCreatedSuccessfully.setStatus(
        "current"
    )

snapshotCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 802)
)
snapshotCreationFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotCreationFailed.setStatus(
        "current"
    )

snapshotDeletedSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 803)
)
snapshotDeletedSuccessfully.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotDeletedSuccessfully.setStatus(
        "current"
    )

snapshotDeleteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 804)
)
snapshotDeleteFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotDeleteFailed.setStatus(
        "current"
    )

snapshotCloningFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 805)
)
snapshotCloningFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotCloningFailed.setStatus(
        "current"
    )

snapshotCloneCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 806)
)
snapshotCloneCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotCloneCompleted.setStatus(
        "current"
    )

snapshotRollbackFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 807)
)
snapshotRollbackFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotRollbackFailed.setStatus(
        "current"
    )

snapshotRollbackCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 808)
)
snapshotRollbackCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snapshotRollbackCompleted.setStatus(
        "current"
    )

haResourceGroupTakeBackCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 901)
)
haResourceGroupTakeBackCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    haResourceGroupTakeBackCompleted.setStatus(
        "current"
    )

haResourceGroupTakeOverCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 902)
)
haResourceGroupTakeOverCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    haResourceGroupTakeOverCompleted.setStatus(
        "current"
    )

controllerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1001)
)
controllerUp.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    controllerUp.setStatus(
        "current"
    )

controllerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1002)
)
controllerDown.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    controllerDown.setStatus(
        "current"
    )

intelliFlashSoftwareUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1003)
)
intelliFlashSoftwareUp.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    intelliFlashSoftwareUp.setStatus(
        "current"
    )

intelliFlashSoftwareDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1004)
)
intelliFlashSoftwareDown.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    intelliFlashSoftwareDown.setStatus(
        "current"
    )

controllerTimeDrift = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1005)
)
controllerTimeDrift.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    controllerTimeDrift.setStatus(
        "current"
    )

fcInitiatorCreateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1101)
)
fcInitiatorCreateCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcInitiatorCreateCompleted.setStatus(
        "current"
    )

fcInitiatorCreateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1102)
)
fcInitiatorCreateFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcInitiatorCreateFailed.setStatus(
        "current"
    )

fcInitiatorModifyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1103)
)
fcInitiatorModifyCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcInitiatorModifyCompleted.setStatus(
        "current"
    )

fcTargetResetHbaPortCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1104)
)
fcTargetResetHbaPortCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcTargetResetHbaPortCompleted.setStatus(
        "current"
    )

fcTargetResetHbaPortFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1105)
)
fcTargetResetHbaPortFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcTargetResetHbaPortFailed.setStatus(
        "current"
    )

fcTargetModifyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1106)
)
fcTargetModifyCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcTargetModifyCompleted.setStatus(
        "current"
    )

fcPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1107)
)
fcPortOnline.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcPortOnline.setStatus(
        "current"
    )

fcPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1108)
)
fcPortOffline.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    fcPortOffline.setStatus(
        "current"
    )

initiatorGroupCreateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1201)
)
initiatorGroupCreateCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    initiatorGroupCreateCompleted.setStatus(
        "current"
    )

initiatorGroupMemberAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1202)
)
initiatorGroupMemberAdded.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    initiatorGroupMemberAdded.setStatus(
        "current"
    )

initiatorGroupMemberRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1203)
)
initiatorGroupMemberRemoved.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    initiatorGroupMemberRemoved.setStatus(
        "current"
    )

initiatorGroupDeleteCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1204)
)
initiatorGroupDeleteCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    initiatorGroupDeleteCompleted.setStatus(
        "current"
    )

iscsiInitiatorCreateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1301)
)
iscsiInitiatorCreateCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorCreateCompleted.setStatus(
        "current"
    )

iscsiInitiatorCreateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1302)
)
iscsiInitiatorCreateFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorCreateFailed.setStatus(
        "current"
    )

iscsiInitiatorModifyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1303)
)
iscsiInitiatorModifyCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorModifyCompleted.setStatus(
        "current"
    )

iscsiInitiatorDeleteCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1304)
)
iscsiInitiatorDeleteCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorDeleteCompleted.setStatus(
        "current"
    )

iscsiTargetCreateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1305)
)
iscsiTargetCreateCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiTargetCreateCompleted.setStatus(
        "current"
    )

iscsiTargetModifyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1306)
)
iscsiTargetModifyCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiTargetModifyCompleted.setStatus(
        "current"
    )

iscsiTargetDeleteCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1307)
)
iscsiTargetDeleteCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiTargetDeleteCompleted.setStatus(
        "current"
    )

iscsiTargetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1308)
)
iscsiTargetError.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiTargetError.setStatus(
        "current"
    )

iscsiTargetGroupError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1309)
)
iscsiTargetGroupError.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiTargetGroupError.setStatus(
        "current"
    )

iscsiImproperTargetGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1310)
)
iscsiImproperTargetGroup.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    iscsiImproperTargetGroup.setStatus(
        "current"
    )

targetGroupCreateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1401)
)
targetGroupCreateCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    targetGroupCreateCompleted.setStatus(
        "current"
    )

targetGroupMemberAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1402)
)
targetGroupMemberAdded.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    targetGroupMemberAdded.setStatus(
        "current"
    )

targetGroupMemberRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1403)
)
targetGroupMemberRemoved.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    targetGroupMemberRemoved.setStatus(
        "current"
    )

targetGroupDeleteCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1404)
)
targetGroupDeleteCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    targetGroupDeleteCompleted.setStatus(
        "current"
    )

adServerTimeDrift = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1501)
)
adServerTimeDrift.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    adServerTimeDrift.setStatus(
        "current"
    )

maintenanceModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1502)
)
maintenanceModeEnabled.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    maintenanceModeEnabled.setStatus(
        "current"
    )

maintenanceModeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1503)
)
maintenanceModeDisabled.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    maintenanceModeDisabled.setStatus(
        "current"
    )

diagnosticDataUploaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1504)
)
diagnosticDataUploaded.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    diagnosticDataUploaded.setStatus(
        "current"
    )

diagnosticDataUploadingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1505)
)
diagnosticDataUploadingFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    diagnosticDataUploadingFailed.setStatus(
        "current"
    )

alertsCleanupCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1506)
)
alertsCleanupCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    alertsCleanupCompleted.setStatus(
        "current"
    )

userLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1507)
)
userLoginFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    userLoginFailed.setStatus(
        "current"
    )

ntpServerTimeDrift = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1508)
)
ntpServerTimeDrift.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    ntpServerTimeDrift.setStatus(
        "current"
    )

smbSocketFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1601)
)
smbSocketFailure.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    smbSocketFailure.setStatus(
        "current"
    )

netbiosSocketFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1602)
)
netbiosSocketFailure.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    netbiosSocketFailure.setStatus(
        "current"
    )

upgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1701)
)
upgradeStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeStarted.setStatus(
        "current"
    )

upgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1702)
)
upgradeCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeCompleted.setStatus(
        "current"
    )

upgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1703)
)
upgradeFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeFailed.setStatus(
        "current"
    )

upgradeTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1704)
)
upgradeTimeout.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeTimeout.setStatus(
        "current"
    )

upgradeCantProcessFilesManually = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1705)
)
upgradeCantProcessFilesManually.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeCantProcessFilesManually.setStatus(
        "current"
    )

upgradeDownloadStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1706)
)
upgradeDownloadStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeDownloadStarted.setStatus(
        "current"
    )

upgradeDownloadCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1707)
)
upgradeDownloadCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeDownloadCompleted.setStatus(
        "current"
    )

upgradeDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1708)
)
upgradeDownloadFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    upgradeDownloadFailed.setStatus(
        "current"
    )

tdpsUpgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1709)
)
tdpsUpgradeCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    tdpsUpgradeCompleted.setStatus(
        "current"
    )

tdpsUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1710)
)
tdpsUpgradeFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    tdpsUpgradeFailed.setStatus(
        "current"
    )

tdpsUpgradeTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1711)
)
tdpsUpgradeTimeout.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    tdpsUpgradeTimeout.setStatus(
        "current"
    )

tdpsUpgradeDownloadStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1712)
)
tdpsUpgradeDownloadStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    tdpsUpgradeDownloadStarted.setStatus(
        "current"
    )

tdpsUpgradeDownloadCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1713)
)
tdpsUpgradeDownloadCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    tdpsUpgradeDownloadCompleted.setStatus(
        "current"
    )

tdpsUpgradeDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1714)
)
tdpsUpgradeDownloadFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    tdpsUpgradeDownloadFailed.setStatus(
        "current"
    )

webdocsUpgradeDownloadStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1715)
)
webdocsUpgradeDownloadStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    webdocsUpgradeDownloadStarted.setStatus(
        "current"
    )

webdocsUpgradeDownloadCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1716)
)
webdocsUpgradeDownloadCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    webdocsUpgradeDownloadCompleted.setStatus(
        "current"
    )

webdocsUpgradeDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1717)
)
webdocsUpgradeDownloadFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    webdocsUpgradeDownloadFailed.setStatus(
        "current"
    )

webdocsUpgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1718)
)
webdocsUpgradeCompleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    webdocsUpgradeCompleted.setStatus(
        "current"
    )

webdocsUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1719)
)
webdocsUpgradeFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    webdocsUpgradeFailed.setStatus(
        "current"
    )

replicationTargetDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1801)
)
replicationTargetDeleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationTargetDeleted.setStatus(
        "current"
    )

replicationComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1802)
)
replicationComplete.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationComplete.setStatus(
        "current"
    )

replicationAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1803)
)
replicationAborted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationAborted.setStatus(
        "current"
    )

replicationAbandoned = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1804)
)
replicationAbandoned.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationAbandoned.setStatus(
        "current"
    )

replicationResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1805)
)
replicationResumed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationResumed.setStatus(
        "current"
    )

replicationStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1806)
)
replicationStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationStarted.setStatus(
        "current"
    )

replicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1807)
)
replicationFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationFailed.setStatus(
        "current"
    )

replicationSourceRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1808)
)
replicationSourceRegistered.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationSourceRegistered.setStatus(
        "current"
    )

replicationPaused = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1809)
)
replicationPaused.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    replicationPaused.setStatus(
        "current"
    )

snmpServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1901)
)
snmpServiceStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snmpServiceStarted.setStatus(
        "current"
    )

snmpServiceStartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1902)
)
snmpServiceStartFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snmpServiceStartFailed.setStatus(
        "current"
    )

snmpServiceStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1903)
)
snmpServiceStopped.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snmpServiceStopped.setStatus(
        "current"
    )

snmpServiceStopFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1904)
)
snmpServiceStopFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    snmpServiceStopFailed.setStatus(
        "current"
    )

smisServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1905)
)
smisServiceStarted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    smisServiceStarted.setStatus(
        "current"
    )

smisServiceStartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1906)
)
smisServiceStartFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    smisServiceStartFailed.setStatus(
        "current"
    )

smisServiceStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1907)
)
smisServiceStopped.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    smisServiceStopped.setStatus(
        "current"
    )

smisServiceStopFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 1908)
)
smisServiceStopFailed.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    smisServiceStopFailed.setStatus(
        "current"
    )

ipmiTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2001)
)
ipmiTemperature.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"),
        ("TEGILE-MIB", "notificationReadingTriggerValue"),
        ("TEGILE-MIB", "notificationThresholdTriggerValue"),
        ("TEGILE-MIB", "notificationReadingUnit"))
)
if mibBuilder.loadTexts:
    ipmiTemperature.setStatus(
        "current"
    )

ipmiVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2002)
)
ipmiVoltage.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"),
        ("TEGILE-MIB", "notificationReadingTriggerValue"),
        ("TEGILE-MIB", "notificationThresholdTriggerValue"),
        ("TEGILE-MIB", "notificationReadingUnit"))
)
if mibBuilder.loadTexts:
    ipmiVoltage.setStatus(
        "current"
    )

ipmiCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2003)
)
ipmiCurrent.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"),
        ("TEGILE-MIB", "notificationReadingTriggerValue"),
        ("TEGILE-MIB", "notificationThresholdTriggerValue"),
        ("TEGILE-MIB", "notificationReadingUnit"))
)
if mibBuilder.loadTexts:
    ipmiCurrent.setStatus(
        "current"
    )

ipmiFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2004)
)
ipmiFan.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"),
        ("TEGILE-MIB", "notificationReadingTriggerValue"),
        ("TEGILE-MIB", "notificationThresholdTriggerValue"),
        ("TEGILE-MIB", "notificationReadingUnit"))
)
if mibBuilder.loadTexts:
    ipmiFan.setStatus(
        "current"
    )

ipmiPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2005)
)
ipmiPowerSupply.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"))
)
if mibBuilder.loadTexts:
    ipmiPowerSupply.setStatus(
        "current"
    )

ipmiMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2006)
)
ipmiMemory.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"))
)
if mibBuilder.loadTexts:
    ipmiMemory.setStatus(
        "current"
    )

ipmiCriticalInterrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2007)
)
ipmiCriticalInterrupt.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"))
)
if mibBuilder.loadTexts:
    ipmiCriticalInterrupt.setStatus(
        "current"
    )

ipmiThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2008)
)
ipmiThreshold.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"),
        ("TEGILE-MIB", "notificationReadingTriggerValue"),
        ("TEGILE-MIB", "notificationThresholdTriggerValue"),
        ("TEGILE-MIB", "notificationReadingUnit"))
)
if mibBuilder.loadTexts:
    ipmiThreshold.setStatus(
        "current"
    )

ipmiOther = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2009)
)
ipmiOther.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationEventCode"),
        ("TEGILE-MIB", "notificationSensorAction"),
        ("TEGILE-MIB", "notificationSensorNumber"),
        ("TEGILE-MIB", "notificationSensorSuspect"))
)
if mibBuilder.loadTexts:
    ipmiOther.setStatus(
        "current"
    )

memoryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2051)
)
memoryFailure.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    memoryFailure.setStatus(
        "current"
    )

sensorFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2052)
)
sensorFailureEvent.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    sensorFailureEvent.setStatus(
        "current"
    )

unknownSensorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2053)
)
unknownSensorEvent.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    unknownSensorEvent.setStatus(
        "current"
    )

networkIpmpGroupUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2201)
)
networkIpmpGroupUp.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    networkIpmpGroupUp.setStatus(
        "current"
    )

networkIpmpGroupDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2202)
)
networkIpmpGroupDown.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    networkIpmpGroupDown.setStatus(
        "current"
    )

networkIpmpMemberInterfaceAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2203)
)
networkIpmpMemberInterfaceAdded.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    networkIpmpMemberInterfaceAdded.setStatus(
        "current"
    )

networkIpmpMemberInterfaceRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2204)
)
networkIpmpMemberInterfaceRemoved.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    networkIpmpMemberInterfaceRemoved.setStatus(
        "current"
    )

networkInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2205)
)
networkInterfaceUp.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    networkInterfaceUp.setStatus(
        "current"
    )

networkInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2206)
)
networkInterfaceDown.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    networkInterfaceDown.setStatus(
        "current"
    )

vmwareNFSDatastoreCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2301)
)
vmwareNFSDatastoreCreated.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    vmwareNFSDatastoreCreated.setStatus(
        "current"
    )

vmwareNFSDatastoreDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2302)
)
vmwareNFSDatastoreDeleted.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    vmwareNFSDatastoreDeleted.setStatus(
        "current"
    )

nvdimmFailDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2401)
)
nvdimmFailDeviceError.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    nvdimmFailDeviceError.setStatus(
        "current"
    )

nvdimmFailSoftError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2402)
)
nvdimmFailSoftError.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    nvdimmFailSoftError.setStatus(
        "current"
    )

nvdimmFailInitializationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2403)
)
nvdimmFailInitializationError.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    nvdimmFailInitializationError.setStatus(
        "current"
    )

nvdimmFailUnknownError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43906, 2, 1, 2, 2404)
)
nvdimmFailUnknownError.setObjects(
      *(("TEGILE-MIB", "notificationDescription"),
        ("TEGILE-MIB", "notificationTime"),
        ("TEGILE-MIB", "notificationSeverity"),
        ("TEGILE-MIB", "notificationComponentName"),
        ("TEGILE-MIB", "notificationTargetEntityName"),
        ("TEGILE-MIB", "notificationEventCode"))
)
if mibBuilder.loadTexts:
    nvdimmFailUnknownError.setStatus(
        "current"
    )


# Notifications groups

currentNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43906, 3, 1, 2)
)
currentNotificationGroup.setObjects(
      *(("TEGILE-MIB", "testNotification"),
        ("TEGILE-MIB", "diskIsOnline"),
        ("TEGILE-MIB", "diskGoneOffline"),
        ("TEGILE-MIB", "diskError"),
        ("TEGILE-MIB", "spareDiskReplaced"),
        ("TEGILE-MIB", "diskSlowIo"),
        ("TEGILE-MIB", "poolCreated"),
        ("TEGILE-MIB", "poolDeleted"),
        ("TEGILE-MIB", "poolDeletionFailed"),
        ("TEGILE-MIB", "poolExpanded"),
        ("TEGILE-MIB", "poolExported"),
        ("TEGILE-MIB", "poolImported"),
        ("TEGILE-MIB", "poolUpgraded"),
        ("TEGILE-MIB", "poolQuotaExceedThresholdWarning"),
        ("TEGILE-MIB", "poolMetaDataQuotaExceedThresholdWarning"),
        ("TEGILE-MIB", "poolAvailableMetaToDataRatioBelowThresholdWarning"),
        ("TEGILE-MIB", "poolQuotaFinished"),
        ("TEGILE-MIB", "poolDegraded"),
        ("TEGILE-MIB", "projectCreatedSuccessfully"),
        ("TEGILE-MIB", "projectDeletionFailed"),
        ("TEGILE-MIB", "projectDeleted"),
        ("TEGILE-MIB", "projectModified"),
        ("TEGILE-MIB", "projectThresholdExceedWarning"),
        ("TEGILE-MIB", "projectQuotaFinished"),
        ("TEGILE-MIB", "projectCreatedWithNonOptimalBlockSize"),
        ("TEGILE-MIB", "volumeCreatedSuccessfully"),
        ("TEGILE-MIB", "volumeModifyCompleted"),
        ("TEGILE-MIB", "volumeDeleteCompleted"),
        ("TEGILE-MIB", "volumeDeleteFailed"),
        ("TEGILE-MIB", "volumeExceedsThresholdWarning"),
        ("TEGILE-MIB", "volumeQuotaFinished"),
        ("TEGILE-MIB", "volumeCreatedWithNonOptimalBlockSize"),
        ("TEGILE-MIB", "shareCreatedSuccessfully"),
        ("TEGILE-MIB", "shareDeletionFailed"),
        ("TEGILE-MIB", "shareDeleted"),
        ("TEGILE-MIB", "shareExceedThresholdWarning"),
        ("TEGILE-MIB", "shareQuotaFinished"),
        ("TEGILE-MIB", "shareCreatedWithNonOptimalBlockSize"),
        ("TEGILE-MIB", "aclMigrationStarted"),
        ("TEGILE-MIB", "aclMigrationCompleted"),
        ("TEGILE-MIB", "deleteFolderCompleted"),
        ("TEGILE-MIB", "deleteFolderFailed"),
        ("TEGILE-MIB", "snapshotCreatedSuccessfully"),
        ("TEGILE-MIB", "snapshotCreationFailed"),
        ("TEGILE-MIB", "snapshotDeletedSuccessfully"),
        ("TEGILE-MIB", "snapshotDeleteFailed"),
        ("TEGILE-MIB", "snapshotCloningFailed"),
        ("TEGILE-MIB", "snapshotCloneCompleted"),
        ("TEGILE-MIB", "snapshotRollbackFailed"),
        ("TEGILE-MIB", "snapshotRollbackCompleted"),
        ("TEGILE-MIB", "haResourceGroupTakeBackCompleted"),
        ("TEGILE-MIB", "haResourceGroupTakeOverCompleted"),
        ("TEGILE-MIB", "controllerUp"),
        ("TEGILE-MIB", "controllerDown"),
        ("TEGILE-MIB", "intelliFlashSoftwareUp"),
        ("TEGILE-MIB", "intelliFlashSoftwareDown"),
        ("TEGILE-MIB", "controllerTimeDrift"),
        ("TEGILE-MIB", "fcInitiatorCreateCompleted"),
        ("TEGILE-MIB", "fcInitiatorCreateFailed"),
        ("TEGILE-MIB", "fcInitiatorModifyCompleted"),
        ("TEGILE-MIB", "fcTargetResetHbaPortCompleted"),
        ("TEGILE-MIB", "fcTargetResetHbaPortFailed"),
        ("TEGILE-MIB", "fcTargetModifyCompleted"),
        ("TEGILE-MIB", "fcPortOnline"),
        ("TEGILE-MIB", "fcPortOffline"),
        ("TEGILE-MIB", "initiatorGroupCreateCompleted"),
        ("TEGILE-MIB", "initiatorGroupMemberAdded"),
        ("TEGILE-MIB", "initiatorGroupMemberRemoved"),
        ("TEGILE-MIB", "initiatorGroupDeleteCompleted"),
        ("TEGILE-MIB", "iscsiInitiatorCreateCompleted"),
        ("TEGILE-MIB", "iscsiInitiatorCreateFailed"),
        ("TEGILE-MIB", "iscsiInitiatorModifyCompleted"),
        ("TEGILE-MIB", "iscsiInitiatorDeleteCompleted"),
        ("TEGILE-MIB", "iscsiTargetCreateCompleted"),
        ("TEGILE-MIB", "iscsiTargetModifyCompleted"),
        ("TEGILE-MIB", "iscsiTargetDeleteCompleted"),
        ("TEGILE-MIB", "iscsiTargetError"),
        ("TEGILE-MIB", "iscsiTargetGroupError"),
        ("TEGILE-MIB", "iscsiImproperTargetGroup"),
        ("TEGILE-MIB", "targetGroupCreateCompleted"),
        ("TEGILE-MIB", "targetGroupMemberAdded"),
        ("TEGILE-MIB", "targetGroupMemberRemoved"),
        ("TEGILE-MIB", "targetGroupDeleteCompleted"),
        ("TEGILE-MIB", "adServerTimeDrift"),
        ("TEGILE-MIB", "maintenanceModeEnabled"),
        ("TEGILE-MIB", "maintenanceModeDisabled"),
        ("TEGILE-MIB", "diagnosticDataUploaded"),
        ("TEGILE-MIB", "diagnosticDataUploadingFailed"),
        ("TEGILE-MIB", "alertsCleanupCompleted"),
        ("TEGILE-MIB", "userLoginFailed"),
        ("TEGILE-MIB", "ntpServerTimeDrift"),
        ("TEGILE-MIB", "smbSocketFailure"),
        ("TEGILE-MIB", "netbiosSocketFailure"),
        ("TEGILE-MIB", "upgradeStarted"),
        ("TEGILE-MIB", "upgradeCompleted"),
        ("TEGILE-MIB", "upgradeFailed"),
        ("TEGILE-MIB", "upgradeTimeout"),
        ("TEGILE-MIB", "upgradeCantProcessFilesManually"),
        ("TEGILE-MIB", "upgradeDownloadStarted"),
        ("TEGILE-MIB", "upgradeDownloadCompleted"),
        ("TEGILE-MIB", "upgradeDownloadFailed"),
        ("TEGILE-MIB", "tdpsUpgradeCompleted"),
        ("TEGILE-MIB", "tdpsUpgradeFailed"),
        ("TEGILE-MIB", "tdpsUpgradeTimeout"),
        ("TEGILE-MIB", "tdpsUpgradeDownloadStarted"),
        ("TEGILE-MIB", "tdpsUpgradeDownloadCompleted"),
        ("TEGILE-MIB", "tdpsUpgradeDownloadFailed"),
        ("TEGILE-MIB", "webdocsUpgradeDownloadStarted"),
        ("TEGILE-MIB", "webdocsUpgradeDownloadCompleted"),
        ("TEGILE-MIB", "webdocsUpgradeDownloadFailed"),
        ("TEGILE-MIB", "webdocsUpgradeCompleted"),
        ("TEGILE-MIB", "webdocsUpgradeFailed"),
        ("TEGILE-MIB", "replicationTargetDeleted"),
        ("TEGILE-MIB", "replicationComplete"),
        ("TEGILE-MIB", "replicationAborted"),
        ("TEGILE-MIB", "replicationAbandoned"),
        ("TEGILE-MIB", "replicationResumed"),
        ("TEGILE-MIB", "replicationStarted"),
        ("TEGILE-MIB", "replicationFailed"),
        ("TEGILE-MIB", "replicationSourceRegistered"),
        ("TEGILE-MIB", "replicationPaused"),
        ("TEGILE-MIB", "snmpServiceStarted"),
        ("TEGILE-MIB", "snmpServiceStartFailed"),
        ("TEGILE-MIB", "snmpServiceStopped"),
        ("TEGILE-MIB", "snmpServiceStopFailed"),
        ("TEGILE-MIB", "smisServiceStarted"),
        ("TEGILE-MIB", "smisServiceStartFailed"),
        ("TEGILE-MIB", "smisServiceStopped"),
        ("TEGILE-MIB", "smisServiceStopFailed"),
        ("TEGILE-MIB", "ipmiTemperature"),
        ("TEGILE-MIB", "ipmiVoltage"),
        ("TEGILE-MIB", "ipmiCurrent"),
        ("TEGILE-MIB", "ipmiFan"),
        ("TEGILE-MIB", "ipmiPowerSupply"),
        ("TEGILE-MIB", "ipmiMemory"),
        ("TEGILE-MIB", "ipmiCriticalInterrupt"),
        ("TEGILE-MIB", "ipmiThreshold"),
        ("TEGILE-MIB", "ipmiOther"),
        ("TEGILE-MIB", "memoryFailure"),
        ("TEGILE-MIB", "sensorFailureEvent"),
        ("TEGILE-MIB", "unknownSensorEvent"),
        ("TEGILE-MIB", "networkIpmpGroupUp"),
        ("TEGILE-MIB", "networkIpmpGroupDown"),
        ("TEGILE-MIB", "networkIpmpMemberInterfaceAdded"),
        ("TEGILE-MIB", "networkIpmpMemberInterfaceRemoved"),
        ("TEGILE-MIB", "networkInterfaceUp"),
        ("TEGILE-MIB", "networkInterfaceDown"),
        ("TEGILE-MIB", "vmwareNFSDatastoreCreated"),
        ("TEGILE-MIB", "vmwareNFSDatastoreDeleted"),
        ("TEGILE-MIB", "nvdimmFailDeviceError"),
        ("TEGILE-MIB", "nvdimmFailSoftError"),
        ("TEGILE-MIB", "nvdimmFailInitializationError"),
        ("TEGILE-MIB", "nvdimmFailUnknownError"))
)
if mibBuilder.loadTexts:
    currentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43906, 3, 2, 1)
)
basicCompliance.setObjects(
    ("TEGILE-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TEGILE-MIB",
    **{"tegile": tegile,
       "tegileArray": tegileArray,
       "properties": properties,
       "haControllerA-Name": haControllerA_Name,
       "haControllerA-IPAddr": haControllerA_IPAddr,
       "haControllerA-SoftwareVersion": haControllerA_SoftwareVersion,
       "haControllerA-Uptime": haControllerA_Uptime,
       "haControllerB-Name": haControllerB_Name,
       "haControllerB-IPAddr": haControllerB_IPAddr,
       "haControllerB-SoftwareVersion": haControllerB_SoftwareVersion,
       "haControllerB-Uptime": haControllerB_Uptime,
       "controllerHardwareModel": controllerHardwareModel,
       "snmpAgentVersion": snmpAgentVersion,
       "globalStatistics": globalStatistics,
       "cpuTotalUsage": cpuTotalUsage,
       "cpuSystemCalls": cpuSystemCalls,
       "cpuInterrupts": cpuInterrupts,
       "cacheTotalWriteMbps": cacheTotalWriteMbps,
       "cacheTotalReadMbps": cacheTotalReadMbps,
       "cacheTotalWriteIops": cacheTotalWriteIops,
       "cacheTotalReadIops": cacheTotalReadIops,
       "cacheRAMReads": cacheRAMReads,
       "cacheSSDReads": cacheSSDReads,
       "diskTotalWriteMbps": diskTotalWriteMbps,
       "diskTotalReadMbps": diskTotalReadMbps,
       "diskTotalWriteIops": diskTotalWriteIops,
       "diskTotalReadIops": diskTotalReadIops,
       "diskDataWriteMbps": diskDataWriteMbps,
       "diskDataReadMbps": diskDataReadMbps,
       "diskDataWriteIops": diskDataWriteIops,
       "diskDataReadIops": diskDataReadIops,
       "diskAvgWriteLatency": diskAvgWriteLatency,
       "diskAvgReadLatency": diskAvgReadLatency,
       "diskIOCount": diskIOCount,
       "diskRandomIOCount": diskRandomIOCount,
       "diskSequentialIOCount": diskSequentialIOCount,
       "poolTotalWriteMbps": poolTotalWriteMbps,
       "poolTotalReadMbps": poolTotalReadMbps,
       "poolTotalWriteIops": poolTotalWriteIops,
       "poolTotalReadIops": poolTotalReadIops,
       "poolAvgWriteLatency": poolAvgWriteLatency,
       "poolAvgReadLatency": poolAvgReadLatency,
       "cifsTotalWriteMbps": cifsTotalWriteMbps,
       "cifsTotalReadMbps": cifsTotalReadMbps,
       "cifsTotalWriteIops": cifsTotalWriteIops,
       "cifsTotalReadIops": cifsTotalReadIops,
       "cifsAvgWriteLatency": cifsAvgWriteLatency,
       "cifsAvgReadLatency": cifsAvgReadLatency,
       "nfsTotalWriteMbps": nfsTotalWriteMbps,
       "nfsTotalReadMbps": nfsTotalReadMbps,
       "nfsTotalWriteIops": nfsTotalWriteIops,
       "nfsTotalReadIops": nfsTotalReadIops,
       "nfsAvgWriteLatency": nfsAvgWriteLatency,
       "nfsAvgReadLatency": nfsAvgReadLatency,
       "iscsiTotalWriteMbps": iscsiTotalWriteMbps,
       "iscsiTotalReadMbps": iscsiTotalReadMbps,
       "iscsiWriteIops": iscsiWriteIops,
       "iscsiTotalReadIops": iscsiTotalReadIops,
       "iscsiAvgWriteLatency": iscsiAvgWriteLatency,
       "iscsiAvgReadLatency": iscsiAvgReadLatency,
       "fcTotalWriteMbps": fcTotalWriteMbps,
       "fcTotalReadMbps": fcTotalReadMbps,
       "fcTotalWriteIops": fcTotalWriteIops,
       "fcTotalReadIops": fcTotalReadIops,
       "fcAvgWriteLatency": fcAvgWriteLatency,
       "fcAvgReadLatency": fcAvgReadLatency,
       "vmwareNFSDatastoresTotalWriteMbps": vmwareNFSDatastoresTotalWriteMbps,
       "vmwareNFSDatastoresTotalReadMbps": vmwareNFSDatastoresTotalReadMbps,
       "vmwareNFSDatastoresTotalWriteIops": vmwareNFSDatastoresTotalWriteIops,
       "vmwareNFSDatastoresTotalReadIops": vmwareNFSDatastoresTotalReadIops,
       "vmwareNFSDatastoresAvgWriteLatency": vmwareNFSDatastoresAvgWriteLatency,
       "vmwareNFSDatastoresAvgReadLatency": vmwareNFSDatastoresAvgReadLatency,
       "networkTotalReceiveMbps": networkTotalReceiveMbps,
       "networkTotalTransmitMbps": networkTotalTransmitMbps,
       "disks": disks,
       "diskCount": diskCount,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskChassisIdx": diskChassisIdx,
       "diskIndex": diskIndex,
       "diskAlias": diskAlias,
       "diskSizeLow": diskSizeLow,
       "diskSizeHigh": diskSizeHigh,
       "diskState": diskState,
       "diskType": diskType,
       "diskPoolName": diskPoolName,
       "pools": pools,
       "poolCount": poolCount,
       "poolTable": poolTable,
       "poolEntry": poolEntry,
       "poolIndex": poolIndex,
       "poolName": poolName,
       "poolState": poolState,
       "poolHealth": poolHealth,
       "poolOwnerController": poolOwnerController,
       "poolProjectCount": poolProjectCount,
       "poolSizeLow": poolSizeLow,
       "poolSizeHigh": poolSizeHigh,
       "poolUsedSizeLow": poolUsedSizeLow,
       "poolUsedSizeHigh": poolUsedSizeHigh,
       "poolFreeSizeLow": poolFreeSizeLow,
       "poolFreeSizeHigh": poolFreeSizeHigh,
       "poolDataSizeLow": poolDataSizeLow,
       "poolDataSizeHigh": poolDataSizeHigh,
       "poolPostDedupDataSizeLow": poolPostDedupDataSizeLow,
       "poolPostDedupDataSizeHigh": poolPostDedupDataSizeHigh,
       "poolPostCompressionDataSizeLow": poolPostCompressionDataSizeLow,
       "poolPostCompressionDataSizeHigh": poolPostCompressionDataSizeHigh,
       "poolUnusedReservedSizeLow": poolUnusedReservedSizeLow,
       "poolUnusedReservedSizeHigh": poolUnusedReservedSizeHigh,
       "poolTotalSaving": poolTotalSaving,
       "poolDataWriteMbps": poolDataWriteMbps,
       "poolDataReadMbps": poolDataReadMbps,
       "poolDataWriteIops": poolDataWriteIops,
       "poolDataReadIops": poolDataReadIops,
       "poolDataWriteLatency": poolDataWriteLatency,
       "poolDataReadLatency": poolDataReadLatency,
       "poolMetaWriteMbps": poolMetaWriteMbps,
       "poolMetaReadMbps": poolMetaReadMbps,
       "poolMetaWriteIops": poolMetaWriteIops,
       "poolMetaReadIops": poolMetaReadIops,
       "poolMetaWriteLatency": poolMetaWriteLatency,
       "poolMetaReadLatency": poolMetaReadLatency,
       "poolReadCacheWriteMbps": poolReadCacheWriteMbps,
       "poolReadCacheReadMbps": poolReadCacheReadMbps,
       "poolReadCacheWriteIops": poolReadCacheWriteIops,
       "poolReadCacheReadIops": poolReadCacheReadIops,
       "poolReadCacheWriteLatency": poolReadCacheWriteLatency,
       "poolReadCacheReadLatency": poolReadCacheReadLatency,
       "poolWriteCacheWriteMbps": poolWriteCacheWriteMbps,
       "poolWriteCacheWriteIops": poolWriteCacheWriteIops,
       "poolWriteCacheWriteLatency": poolWriteCacheWriteLatency,
       "poolProjects": poolProjects,
       "projectTable": projectTable,
       "projectEntry": projectEntry,
       "projectIndex": projectIndex,
       "projectName": projectName,
       "projectPoolName": projectPoolName,
       "projectDedupEnabled": projectDedupEnabled,
       "projectCompressionEnabled": projectCompressionEnabled,
       "projectQuotaSizeLow": projectQuotaSizeLow,
       "projectQuotaSizeHigh": projectQuotaSizeHigh,
       "projectDataSizeLow": projectDataSizeLow,
       "projectDataSizeHigh": projectDataSizeHigh,
       "projectFreeSizeLow": projectFreeSizeLow,
       "projectFreeSizeHigh": projectFreeSizeHigh,
       "projectSnapshotSizeLow": projectSnapshotSizeLow,
       "projectSnapshotSizeHigh": projectSnapshotSizeHigh,
       "projectPostCompressionDataSizeLow": projectPostCompressionDataSizeLow,
       "projectPostCompressionDataSizeHigh": projectPostCompressionDataSizeHigh,
       "projectUnusedReservedSizeLow": projectUnusedReservedSizeLow,
       "projectUnusedReservedSizeHigh": projectUnusedReservedSizeHigh,
       "projectTotalSaving": projectTotalSaving,
       "projectLunCount": projectLunCount,
       "projectShareCount": projectShareCount,
       "projectLUNs": projectLUNs,
       "lunTable": lunTable,
       "lunEntry": lunEntry,
       "lunIndex": lunIndex,
       "lunName": lunName,
       "lunProjectName": lunProjectName,
       "lunPoolName": lunPoolName,
       "lunGUID": lunGUID,
       "lunBlockSize": lunBlockSize,
       "lunDedupEnabled": lunDedupEnabled,
       "lunCompressionEnabled": lunCompressionEnabled,
       "lunSizeLow": lunSizeLow,
       "lunSizeHigh": lunSizeHigh,
       "lunDataSizeLow": lunDataSizeLow,
       "lunDataSizeHigh": lunDataSizeHigh,
       "lunSnapshotSizeLow": lunSnapshotSizeLow,
       "lunSnapshotSizeHigh": lunSnapshotSizeHigh,
       "lunFreeSizeLow": lunFreeSizeLow,
       "lunFreeSizeHigh": lunFreeSizeHigh,
       "lunReservedSizeLow": lunReservedSizeLow,
       "lunReservedSizeHigh": lunReservedSizeHigh,
       "lunCompressedRatio": lunCompressedRatio,
       "lunProtocol": lunProtocol,
       "lunTargetGroup": lunTargetGroup,
       "lunInitiatorGroup": lunInitiatorGroup,
       "lunWriteMbps": lunWriteMbps,
       "lunReadMbps": lunReadMbps,
       "lunWriteIops": lunWriteIops,
       "lunReadIops": lunReadIops,
       "lunWriteLatency": lunWriteLatency,
       "lunReadLatency": lunReadLatency,
       "projectShares": projectShares,
       "shareTable": shareTable,
       "shareEntry": shareEntry,
       "shareIndex": shareIndex,
       "shareName": shareName,
       "shareMountPoint": shareMountPoint,
       "shareProjectName": shareProjectName,
       "sharePoolName": sharePoolName,
       "shareQuotaLow": shareQuotaLow,
       "shareQuotaHigh": shareQuotaHigh,
       "shareNFSEnabled": shareNFSEnabled,
       "shareCIFSEnabled": shareCIFSEnabled,
       "shareDedupEnabled": shareDedupEnabled,
       "shareCompressionEnabled": shareCompressionEnabled,
       "shareDataSizeLow": shareDataSizeLow,
       "shareDataSizeHigh": shareDataSizeHigh,
       "shareSnapshotSizeLow": shareSnapshotSizeLow,
       "shareSnapshotSizeHigh": shareSnapshotSizeHigh,
       "shareReservedSizeLow": shareReservedSizeLow,
       "shareReservedSizeHigh": shareReservedSizeHigh,
       "shareCompressedRatio": shareCompressedRatio,
       "shareCIFSWriteMbps": shareCIFSWriteMbps,
       "shareCIFSReadMbps": shareCIFSReadMbps,
       "shareCIFSWriteIops": shareCIFSWriteIops,
       "shareCIFSReadIops": shareCIFSReadIops,
       "shareCIFSWriteLatency": shareCIFSWriteLatency,
       "shareCIFSReadLatency": shareCIFSReadLatency,
       "shareNFSWriteMbps": shareNFSWriteMbps,
       "shareNFSReadMbps": shareNFSReadMbps,
       "shareNFSWriteIops": shareNFSWriteIops,
       "shareNFSReadIops": shareNFSReadIops,
       "shareNFSWriteLatency": shareNFSWriteLatency,
       "shareNFSReadLatency": shareNFSReadLatency,
       "network": network,
       "nicTable": nicTable,
       "nicEntry": nicEntry,
       "nicIndex": nicIndex,
       "nicName": nicName,
       "nicState": nicState,
       "nicGroup": nicGroup,
       "nicMTU": nicMTU,
       "nicReceiveMbps": nicReceiveMbps,
       "nicTransmitMbps": nicTransmitMbps,
       "sanProperties": sanProperties,
       "iscsiProperties": iscsiProperties,
       "iscsiTargets": iscsiTargets,
       "iscsiTargetsTable": iscsiTargetsTable,
       "iscsiTargetEntry": iscsiTargetEntry,
       "iscsiTargetIndex": iscsiTargetIndex,
       "iscsiTargetName": iscsiTargetName,
       "iscsiTargetAlias": iscsiTargetAlias,
       "iscsiTargetGroup": iscsiTargetGroup,
       "iscsiTargetAuth": iscsiTargetAuth,
       "iscsiTargetWriteMbps": iscsiTargetWriteMbps,
       "iscsiTargetReadMbps": iscsiTargetReadMbps,
       "iscsiTargetWriteIops": iscsiTargetWriteIops,
       "iscsiTargetReadIops": iscsiTargetReadIops,
       "iscsiTargetWriteLatency": iscsiTargetWriteLatency,
       "iscsiTargetReadLatency": iscsiTargetReadLatency,
       "iscsiInitiators": iscsiInitiators,
       "iscsiInitiatorsTable": iscsiInitiatorsTable,
       "iscsiInitiatorEntry": iscsiInitiatorEntry,
       "iscsiInitiatorIndex": iscsiInitiatorIndex,
       "iscsiInitiatorName": iscsiInitiatorName,
       "iscsiInitiatorChapUser": iscsiInitiatorChapUser,
       "iscsiInitiatorGroup": iscsiInitiatorGroup,
       "fcProperties": fcProperties,
       "fcTargets": fcTargets,
       "fcTargetsTable": fcTargetsTable,
       "fcTargetEntry": fcTargetEntry,
       "fcTargetIndex": fcTargetIndex,
       "fcTargetName": fcTargetName,
       "fcTargetStatus": fcTargetStatus,
       "fcTargetGroup": fcTargetGroup,
       "fcTargetWriteMbps": fcTargetWriteMbps,
       "fcTargetReadMbps": fcTargetReadMbps,
       "fcTargetWriteIops": fcTargetWriteIops,
       "fcTargetReadIops": fcTargetReadIops,
       "fcTargetWriteLatency": fcTargetWriteLatency,
       "fcTargetReadLatency": fcTargetReadLatency,
       "fcInitiators": fcInitiators,
       "fcInitiatorsTable": fcInitiatorsTable,
       "fcInitiatorEntry": fcInitiatorEntry,
       "fcInitiatorIndex": fcInitiatorIndex,
       "fcInitiatorName": fcInitiatorName,
       "fcInitiatorGroup": fcInitiatorGroup,
       "vmwareNFSDatastores": vmwareNFSDatastores,
       "vmwareNFSDatastoresTable": vmwareNFSDatastoresTable,
       "vmwareNFSDatastoreEntry": vmwareNFSDatastoreEntry,
       "vmwareNFSDatastoreIndex": vmwareNFSDatastoreIndex,
       "vmwareNFSDatastoreVMName": vmwareNFSDatastoreVMName,
       "vmwareNFSDatastoreESXName": vmwareNFSDatastoreESXName,
       "vmwareNFSDatastoreWriteMbps": vmwareNFSDatastoreWriteMbps,
       "vmwareNFSDatastoreReadMbps": vmwareNFSDatastoreReadMbps,
       "vmwareNFSDatastoreWriteIops": vmwareNFSDatastoreWriteIops,
       "vmwareNFSDatastoreReadIops": vmwareNFSDatastoreReadIops,
       "vmwareNFSDatastoreWriteLatency": vmwareNFSDatastoreWriteLatency,
       "vmwareNFSDatastoreReadLatency": vmwareNFSDatastoreReadLatency,
       "haResources": haResources,
       "haResourcesTable": haResourcesTable,
       "haResourceEntry": haResourceEntry,
       "haResourceIndex": haResourceIndex,
       "haResourceName": haResourceName,
       "haResourceDescription": haResourceDescription,
       "haResourceStatus": haResourceStatus,
       "haResourceGroup": haResourceGroup,
       "haResourceActiveNode": haResourceActiveNode,
       "tegileArray-notifications": tegileArray_notifications,
       "notificationObjects": notificationObjects,
       "notificationProps": notificationProps,
       "notificationDescription": notificationDescription,
       "notificationTime": notificationTime,
       "notificationSeverity": notificationSeverity,
       "notificationComponentName": notificationComponentName,
       "notificationTargetEntityName": notificationTargetEntityName,
       "notificationEventCode": notificationEventCode,
       "notificationSensorAction": notificationSensorAction,
       "notificationSensorNumber": notificationSensorNumber,
       "notificationSensorSuspect": notificationSensorSuspect,
       "notificationReadingTriggerValue": notificationReadingTriggerValue,
       "notificationThresholdTriggerValue": notificationThresholdTriggerValue,
       "notificationReadingUnit": notificationReadingUnit,
       "notifications": notifications,
       "testNotification": testNotification,
       "diskIsOnline": diskIsOnline,
       "diskGoneOffline": diskGoneOffline,
       "diskError": diskError,
       "spareDiskReplaced": spareDiskReplaced,
       "diskSlowIo": diskSlowIo,
       "poolCreated": poolCreated,
       "poolDeleted": poolDeleted,
       "poolDeletionFailed": poolDeletionFailed,
       "poolExpanded": poolExpanded,
       "poolExported": poolExported,
       "poolImported": poolImported,
       "poolUpgraded": poolUpgraded,
       "poolQuotaExceedThresholdWarning": poolQuotaExceedThresholdWarning,
       "poolMetaDataQuotaExceedThresholdWarning": poolMetaDataQuotaExceedThresholdWarning,
       "poolAvailableMetaToDataRatioBelowThresholdWarning": poolAvailableMetaToDataRatioBelowThresholdWarning,
       "poolQuotaFinished": poolQuotaFinished,
       "poolDegraded": poolDegraded,
       "projectCreatedSuccessfully": projectCreatedSuccessfully,
       "projectDeletionFailed": projectDeletionFailed,
       "projectDeleted": projectDeleted,
       "projectModified": projectModified,
       "projectThresholdExceedWarning": projectThresholdExceedWarning,
       "projectQuotaFinished": projectQuotaFinished,
       "projectCreatedWithNonOptimalBlockSize": projectCreatedWithNonOptimalBlockSize,
       "volumeCreatedSuccessfully": volumeCreatedSuccessfully,
       "volumeModifyCompleted": volumeModifyCompleted,
       "volumeDeleteCompleted": volumeDeleteCompleted,
       "volumeDeleteFailed": volumeDeleteFailed,
       "volumeExceedsThresholdWarning": volumeExceedsThresholdWarning,
       "volumeQuotaFinished": volumeQuotaFinished,
       "volumeCreatedWithNonOptimalBlockSize": volumeCreatedWithNonOptimalBlockSize,
       "shareCreatedSuccessfully": shareCreatedSuccessfully,
       "shareDeletionFailed": shareDeletionFailed,
       "shareDeleted": shareDeleted,
       "shareExceedThresholdWarning": shareExceedThresholdWarning,
       "shareQuotaFinished": shareQuotaFinished,
       "shareCreatedWithNonOptimalBlockSize": shareCreatedWithNonOptimalBlockSize,
       "aclMigrationStarted": aclMigrationStarted,
       "aclMigrationCompleted": aclMigrationCompleted,
       "deleteFolderCompleted": deleteFolderCompleted,
       "deleteFolderFailed": deleteFolderFailed,
       "snapshotCreatedSuccessfully": snapshotCreatedSuccessfully,
       "snapshotCreationFailed": snapshotCreationFailed,
       "snapshotDeletedSuccessfully": snapshotDeletedSuccessfully,
       "snapshotDeleteFailed": snapshotDeleteFailed,
       "snapshotCloningFailed": snapshotCloningFailed,
       "snapshotCloneCompleted": snapshotCloneCompleted,
       "snapshotRollbackFailed": snapshotRollbackFailed,
       "snapshotRollbackCompleted": snapshotRollbackCompleted,
       "haResourceGroupTakeBackCompleted": haResourceGroupTakeBackCompleted,
       "haResourceGroupTakeOverCompleted": haResourceGroupTakeOverCompleted,
       "controllerUp": controllerUp,
       "controllerDown": controllerDown,
       "intelliFlashSoftwareUp": intelliFlashSoftwareUp,
       "intelliFlashSoftwareDown": intelliFlashSoftwareDown,
       "controllerTimeDrift": controllerTimeDrift,
       "fcInitiatorCreateCompleted": fcInitiatorCreateCompleted,
       "fcInitiatorCreateFailed": fcInitiatorCreateFailed,
       "fcInitiatorModifyCompleted": fcInitiatorModifyCompleted,
       "fcTargetResetHbaPortCompleted": fcTargetResetHbaPortCompleted,
       "fcTargetResetHbaPortFailed": fcTargetResetHbaPortFailed,
       "fcTargetModifyCompleted": fcTargetModifyCompleted,
       "fcPortOnline": fcPortOnline,
       "fcPortOffline": fcPortOffline,
       "initiatorGroupCreateCompleted": initiatorGroupCreateCompleted,
       "initiatorGroupMemberAdded": initiatorGroupMemberAdded,
       "initiatorGroupMemberRemoved": initiatorGroupMemberRemoved,
       "initiatorGroupDeleteCompleted": initiatorGroupDeleteCompleted,
       "iscsiInitiatorCreateCompleted": iscsiInitiatorCreateCompleted,
       "iscsiInitiatorCreateFailed": iscsiInitiatorCreateFailed,
       "iscsiInitiatorModifyCompleted": iscsiInitiatorModifyCompleted,
       "iscsiInitiatorDeleteCompleted": iscsiInitiatorDeleteCompleted,
       "iscsiTargetCreateCompleted": iscsiTargetCreateCompleted,
       "iscsiTargetModifyCompleted": iscsiTargetModifyCompleted,
       "iscsiTargetDeleteCompleted": iscsiTargetDeleteCompleted,
       "iscsiTargetError": iscsiTargetError,
       "iscsiTargetGroupError": iscsiTargetGroupError,
       "iscsiImproperTargetGroup": iscsiImproperTargetGroup,
       "targetGroupCreateCompleted": targetGroupCreateCompleted,
       "targetGroupMemberAdded": targetGroupMemberAdded,
       "targetGroupMemberRemoved": targetGroupMemberRemoved,
       "targetGroupDeleteCompleted": targetGroupDeleteCompleted,
       "adServerTimeDrift": adServerTimeDrift,
       "maintenanceModeEnabled": maintenanceModeEnabled,
       "maintenanceModeDisabled": maintenanceModeDisabled,
       "diagnosticDataUploaded": diagnosticDataUploaded,
       "diagnosticDataUploadingFailed": diagnosticDataUploadingFailed,
       "alertsCleanupCompleted": alertsCleanupCompleted,
       "userLoginFailed": userLoginFailed,
       "ntpServerTimeDrift": ntpServerTimeDrift,
       "smbSocketFailure": smbSocketFailure,
       "netbiosSocketFailure": netbiosSocketFailure,
       "upgradeStarted": upgradeStarted,
       "upgradeCompleted": upgradeCompleted,
       "upgradeFailed": upgradeFailed,
       "upgradeTimeout": upgradeTimeout,
       "upgradeCantProcessFilesManually": upgradeCantProcessFilesManually,
       "upgradeDownloadStarted": upgradeDownloadStarted,
       "upgradeDownloadCompleted": upgradeDownloadCompleted,
       "upgradeDownloadFailed": upgradeDownloadFailed,
       "tdpsUpgradeCompleted": tdpsUpgradeCompleted,
       "tdpsUpgradeFailed": tdpsUpgradeFailed,
       "tdpsUpgradeTimeout": tdpsUpgradeTimeout,
       "tdpsUpgradeDownloadStarted": tdpsUpgradeDownloadStarted,
       "tdpsUpgradeDownloadCompleted": tdpsUpgradeDownloadCompleted,
       "tdpsUpgradeDownloadFailed": tdpsUpgradeDownloadFailed,
       "webdocsUpgradeDownloadStarted": webdocsUpgradeDownloadStarted,
       "webdocsUpgradeDownloadCompleted": webdocsUpgradeDownloadCompleted,
       "webdocsUpgradeDownloadFailed": webdocsUpgradeDownloadFailed,
       "webdocsUpgradeCompleted": webdocsUpgradeCompleted,
       "webdocsUpgradeFailed": webdocsUpgradeFailed,
       "replicationTargetDeleted": replicationTargetDeleted,
       "replicationComplete": replicationComplete,
       "replicationAborted": replicationAborted,
       "replicationAbandoned": replicationAbandoned,
       "replicationResumed": replicationResumed,
       "replicationStarted": replicationStarted,
       "replicationFailed": replicationFailed,
       "replicationSourceRegistered": replicationSourceRegistered,
       "replicationPaused": replicationPaused,
       "snmpServiceStarted": snmpServiceStarted,
       "snmpServiceStartFailed": snmpServiceStartFailed,
       "snmpServiceStopped": snmpServiceStopped,
       "snmpServiceStopFailed": snmpServiceStopFailed,
       "smisServiceStarted": smisServiceStarted,
       "smisServiceStartFailed": smisServiceStartFailed,
       "smisServiceStopped": smisServiceStopped,
       "smisServiceStopFailed": smisServiceStopFailed,
       "ipmiTemperature": ipmiTemperature,
       "ipmiVoltage": ipmiVoltage,
       "ipmiCurrent": ipmiCurrent,
       "ipmiFan": ipmiFan,
       "ipmiPowerSupply": ipmiPowerSupply,
       "ipmiMemory": ipmiMemory,
       "ipmiCriticalInterrupt": ipmiCriticalInterrupt,
       "ipmiThreshold": ipmiThreshold,
       "ipmiOther": ipmiOther,
       "memoryFailure": memoryFailure,
       "sensorFailureEvent": sensorFailureEvent,
       "unknownSensorEvent": unknownSensorEvent,
       "networkIpmpGroupUp": networkIpmpGroupUp,
       "networkIpmpGroupDown": networkIpmpGroupDown,
       "networkIpmpMemberInterfaceAdded": networkIpmpMemberInterfaceAdded,
       "networkIpmpMemberInterfaceRemoved": networkIpmpMemberInterfaceRemoved,
       "networkInterfaceUp": networkInterfaceUp,
       "networkInterfaceDown": networkInterfaceDown,
       "vmwareNFSDatastoreCreated": vmwareNFSDatastoreCreated,
       "vmwareNFSDatastoreDeleted": vmwareNFSDatastoreDeleted,
       "nvdimmFailDeviceError": nvdimmFailDeviceError,
       "nvdimmFailSoftError": nvdimmFailSoftError,
       "nvdimmFailInitializationError": nvdimmFailInitializationError,
       "nvdimmFailUnknownError": nvdimmFailUnknownError,
       "tegileConformance": tegileConformance,
       "tegileGroups": tegileGroups,
       "currentObjectGroup": currentObjectGroup,
       "currentNotificationGroup": currentNotificationGroup,
       "tegileCompliances": tegileCompliances,
       "basicCompliance": basicCompliance}
)
