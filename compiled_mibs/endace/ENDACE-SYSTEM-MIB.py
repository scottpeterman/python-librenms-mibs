# SNMP MIB module (ENDACE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:00 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

shogunSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1)
)
if mibBuilder.loadTexts:
    shogunSystemMIB.setRevisions(
        ("2022-05-03 00:07",
         "2021-02-18 20:25",
         "2017-04-28 03:51",
         "2015-05-29 01:10",
         "2014-06-20 02:10",
         "2013-11-24 21:03",
         "2013-07-24 06:40",
         "2013-06-30 06:40",
         "2013-01-14 19:28",
         "2012-10-05 03:36",
         "2012-08-28 21:43",
         "2012-07-15 22:13",
         "2011-10-24 00:00",
         "2011-09-12 00:00",
         "2011-03-01 00:00",
         "2007-09-22 00:00",
         "2007-05-23 00:00",
         "2007-04-24 00:00",
         "2007-04-17 00:00",
         "2007-02-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RaidStatusCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("initializing", 1),
          ("migrating", 2),
          ("rebuilding", 3),
          ("recovery", 4),
          ("degradedInit", 5),
          ("degradedRbld", 6),
          ("partiallyDegraded", 7),
          ("degraded", 8),
          ("inoperable", 9),
          ("unknown", 10))
    )



# MIB Managed Objects in the order of their OIDs

_Variables_ObjectIdentity = ObjectIdentity
variables = _Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1)
)
_SystemAppliance_ObjectIdentity = ObjectIdentity
systemAppliance = _SystemAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1)
)
_SystemVersion_Type = DisplayString
_SystemVersion_Object = MibScalar
systemVersion = _SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 1),
    _SystemVersion_Type()
)
systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVersion.setStatus("current")
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2)
)
_CpuLoad1_Type = Unsigned32
_CpuLoad1_Object = MibScalar
cpuLoad1 = _CpuLoad1_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 1),
    _CpuLoad1_Type()
)
cpuLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad1.setStatus("current")
_CpuLoad5_Type = Unsigned32
_CpuLoad5_Object = MibScalar
cpuLoad5 = _CpuLoad5_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 2),
    _CpuLoad5_Type()
)
cpuLoad5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad5.setStatus("current")
_CpuLoad15_Type = Unsigned32
_CpuLoad15_Object = MibScalar
cpuLoad15 = _CpuLoad15_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 3),
    _CpuLoad15_Type()
)
cpuLoad15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad15.setStatus("current")
_CpuUtil1_Type = Unsigned32
_CpuUtil1_Object = MibScalar
cpuUtil1 = _CpuUtil1_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 4),
    _CpuUtil1_Type()
)
cpuUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtil1.setStatus("current")
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("current")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 5, 1)
)
cpuEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("current")
_CpuIndex_Type = Unsigned32
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 5, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_IdleTime_Type = TimeTicks
_IdleTime_Object = MibTableColumn
idleTime = _IdleTime_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 5, 1, 2),
    _IdleTime_Type()
)
idleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idleTime.setStatus("current")
_SystemTime_Type = TimeTicks
_SystemTime_Object = MibTableColumn
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 5, 1, 3),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_UserTime_Type = TimeTicks
_UserTime_Object = MibTableColumn
userTime = _UserTime_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 5, 1, 4),
    _UserTime_Type()
)
userTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTime.setStatus("current")
_UtilPct1Min_Type = Unsigned32
_UtilPct1Min_Object = MibTableColumn
utilPct1Min = _UtilPct1Min_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 2, 5, 1, 5),
    _UtilPct1Min_Type()
)
utilPct1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utilPct1Min.setStatus("current")
_Procmgr_ObjectIdentity = ObjectIdentity
procmgr = _Procmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 3)
)
_ProcTable_Object = MibTable
procTable = _ProcTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    procTable.setStatus("current")
_ProcEntry_Object = MibTableRow
procEntry = _ProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 3, 1, 1)
)
procEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "procIndex"),
)
if mibBuilder.loadTexts:
    procEntry.setStatus("current")
_ProcIndex_Type = Unsigned32
_ProcIndex_Object = MibTableColumn
procIndex = _ProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 3, 1, 1, 1),
    _ProcIndex_Type()
)
procIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procIndex.setStatus("current")
_ProcName_Type = DisplayString
_ProcName_Object = MibTableColumn
procName = _ProcName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 3, 1, 1, 2),
    _ProcName_Type()
)
procName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procName.setStatus("current")
_ProcStatus_Type = DisplayString
_ProcStatus_Object = MibTableColumn
procStatus = _ProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 3, 1, 1, 3),
    _ProcStatus_Type()
)
procStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStatus.setStatus("current")
_ProcNumFailures_Type = Unsigned32
_ProcNumFailures_Object = MibTableColumn
procNumFailures = _ProcNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 3, 1, 1, 4),
    _ProcNumFailures_Type()
)
procNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procNumFailures.setStatus("current")
_Mountmgr_ObjectIdentity = ObjectIdentity
mountmgr = _Mountmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5)
)
_MountTable_Object = MibTable
mountTable = _MountTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mountTable.setStatus("current")
_MountEntry_Object = MibTableRow
mountEntry = _MountEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1)
)
mountEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "mountIndex"),
)
if mibBuilder.loadTexts:
    mountEntry.setStatus("current")
_MountIndex_Type = Unsigned32
_MountIndex_Object = MibTableColumn
mountIndex = _MountIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 1),
    _MountIndex_Type()
)
mountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountIndex.setStatus("current")
_MountBytesAvail_Type = Counter64
_MountBytesAvail_Object = MibTableColumn
mountBytesAvail = _MountBytesAvail_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 2),
    _MountBytesAvail_Type()
)
mountBytesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountBytesAvail.setStatus("current")
_MountBytesFree_Type = Counter64
_MountBytesFree_Object = MibTableColumn
mountBytesFree = _MountBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 3),
    _MountBytesFree_Type()
)
mountBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountBytesFree.setStatus("current")
_MountBytesPercentFree_Type = Unsigned32
_MountBytesPercentFree_Object = MibTableColumn
mountBytesPercentFree = _MountBytesPercentFree_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 4),
    _MountBytesPercentFree_Type()
)
mountBytesPercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountBytesPercentFree.setStatus("current")
_MountBytesTotal_Type = Counter64
_MountBytesTotal_Object = MibTableColumn
mountBytesTotal = _MountBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 5),
    _MountBytesTotal_Type()
)
mountBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountBytesTotal.setStatus("current")
_MountBytesUsed_Type = Counter64
_MountBytesUsed_Object = MibTableColumn
mountBytesUsed = _MountBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 6),
    _MountBytesUsed_Type()
)
mountBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountBytesUsed.setStatus("current")
_MountPoint_Type = DisplayString
_MountPoint_Object = MibTableColumn
mountPoint = _MountPoint_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 7),
    _MountPoint_Type()
)
mountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountPoint.setStatus("current")
_MountDeviceName_Type = DisplayString
_MountDeviceName_Object = MibTableColumn
mountDeviceName = _MountDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 8),
    _MountDeviceName_Type()
)
mountDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountDeviceName.setStatus("current")
_MountInodesFree_Type = Counter64
_MountInodesFree_Object = MibTableColumn
mountInodesFree = _MountInodesFree_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 9),
    _MountInodesFree_Type()
)
mountInodesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInodesFree.setStatus("current")
_MountInodesPercentFree_Type = Unsigned32
_MountInodesPercentFree_Object = MibTableColumn
mountInodesPercentFree = _MountInodesPercentFree_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 10),
    _MountInodesPercentFree_Type()
)
mountInodesPercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInodesPercentFree.setStatus("current")
_MountInodesTotal_Type = Counter64
_MountInodesTotal_Object = MibTableColumn
mountInodesTotal = _MountInodesTotal_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 11),
    _MountInodesTotal_Type()
)
mountInodesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInodesTotal.setStatus("current")
_MountInodesUsed_Type = Counter64
_MountInodesUsed_Object = MibTableColumn
mountInodesUsed = _MountInodesUsed_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 5, 1, 1, 12),
    _MountInodesUsed_Type()
)
mountInodesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountInodesUsed.setStatus("current")
_Sessions_ObjectIdentity = ObjectIdentity
sessions = _Sessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6)
)
_SessionTable_Object = MibTable
sessionTable = _SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sessionTable.setStatus("current")
_SessionEntry_Object = MibTableRow
sessionEntry = _SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1, 1)
)
sessionEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "sessionId"),
)
if mibBuilder.loadTexts:
    sessionEntry.setStatus("current")
_SessionId_Type = Unsigned32
_SessionId_Object = MibTableColumn
sessionId = _SessionId_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1, 1, 1),
    _SessionId_Type()
)
sessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionId.setStatus("current")
_Username_Type = DisplayString
_Username_Object = MibTableColumn
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1, 1, 2),
    _Username_Type()
)
username.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    username.setStatus("current")
_UsernameLocal_Type = DisplayString
_UsernameLocal_Object = MibTableColumn
usernameLocal = _UsernameLocal_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1, 1, 3),
    _UsernameLocal_Type()
)
usernameLocal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usernameLocal.setStatus("current")
_RemoteAddr_Type = IpAddress
_RemoteAddr_Object = MibTableColumn
remoteAddr = _RemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1, 1, 4),
    _RemoteAddr_Type()
)
remoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    remoteAddr.setStatus("current")
_RemoteHostname_Type = DisplayString
_RemoteHostname_Object = MibTableColumn
remoteHostname = _RemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1, 1, 5),
    _RemoteHostname_Type()
)
remoteHostname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    remoteHostname.setStatus("current")
_ClientDescr_Type = DisplayString
_ClientDescr_Object = MibTableColumn
clientDescr = _ClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 6, 1, 1, 6),
    _ClientDescr_Type()
)
clientDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clientDescr.setStatus("current")
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7)
)
_RaidDrvTable_Object = MibTable
raidDrvTable = _RaidDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    raidDrvTable.setStatus("current")
_RaidDrvEntry_Object = MibTableRow
raidDrvEntry = _RaidDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1)
)
raidDrvEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "raidDrvIndex"),
)
if mibBuilder.loadTexts:
    raidDrvEntry.setStatus("current")


class _RaidDrvIndex_Type(Integer32):
    """Custom type raidDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RaidDrvIndex_Type.__name__ = "Integer32"
_RaidDrvIndex_Object = MibTableColumn
raidDrvIndex = _RaidDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 1),
    _RaidDrvIndex_Type()
)
raidDrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raidDrvIndex.setStatus("current")


class _RaidDrvId_Type(Integer32):
    """Custom type raidDrvId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RaidDrvId_Type.__name__ = "Integer32"
_RaidDrvId_Object = MibTableColumn
raidDrvId = _RaidDrvId_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 2),
    _RaidDrvId_Type()
)
raidDrvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvId.setStatus("current")
_RaidDrvType_Type = DisplayString
_RaidDrvType_Object = MibTableColumn
raidDrvType = _RaidDrvType_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 3),
    _RaidDrvType_Type()
)
raidDrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvType.setStatus("current")
_RaidDrvSerialNo_Type = DisplayString
_RaidDrvSerialNo_Object = MibTableColumn
raidDrvSerialNo = _RaidDrvSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 4),
    _RaidDrvSerialNo_Type()
)
raidDrvSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvSerialNo.setStatus("current")


class _RaidDrvWearout_Type(Integer32):
    """Custom type raidDrvWearout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_RaidDrvWearout_Type.__name__ = "Integer32"
_RaidDrvWearout_Object = MibTableColumn
raidDrvWearout = _RaidDrvWearout_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 5),
    _RaidDrvWearout_Type()
)
raidDrvWearout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvWearout.setStatus("current")
_RaidDrvLbaWritten_Type = Counter64
_RaidDrvLbaWritten_Object = MibTableColumn
raidDrvLbaWritten = _RaidDrvLbaWritten_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 6),
    _RaidDrvLbaWritten_Type()
)
raidDrvLbaWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvLbaWritten.setStatus("current")
_RaidDrvRealloc_Type = Integer32
_RaidDrvRealloc_Object = MibTableColumn
raidDrvRealloc = _RaidDrvRealloc_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 7),
    _RaidDrvRealloc_Type()
)
raidDrvRealloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvRealloc.setStatus("current")
_RaidDrvPending_Type = Integer32
_RaidDrvPending_Object = MibTableColumn
raidDrvPending = _RaidDrvPending_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 8),
    _RaidDrvPending_Type()
)
raidDrvPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvPending.setStatus("current")
_RaidDrvUncorrErrors_Type = Integer32
_RaidDrvUncorrErrors_Object = MibTableColumn
raidDrvUncorrErrors = _RaidDrvUncorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 9),
    _RaidDrvUncorrErrors_Type()
)
raidDrvUncorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvUncorrErrors.setStatus("current")
_RaidDrvDefect_Type = Integer32
_RaidDrvDefect_Object = MibTableColumn
raidDrvDefect = _RaidDrvDefect_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 10),
    _RaidDrvDefect_Type()
)
raidDrvDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvDefect.setStatus("current")
_RaidDrvFdeCapable_Type = DisplayString
_RaidDrvFdeCapable_Object = MibTableColumn
raidDrvFdeCapable = _RaidDrvFdeCapable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 11),
    _RaidDrvFdeCapable_Type()
)
raidDrvFdeCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvFdeCapable.setStatus("current")
_RaidDrvSecurity_Type = DisplayString
_RaidDrvSecurity_Object = MibTableColumn
raidDrvSecurity = _RaidDrvSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 12),
    _RaidDrvSecurity_Type()
)
raidDrvSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvSecurity.setStatus("current")
_RaidDrvLocking_Type = DisplayString
_RaidDrvLocking_Object = MibTableColumn
raidDrvLocking = _RaidDrvLocking_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 1, 1, 13),
    _RaidDrvLocking_Type()
)
raidDrvLocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrvLocking.setStatus("current")
_RaidBbuTable_Object = MibTable
raidBbuTable = _RaidBbuTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    raidBbuTable.setStatus("current")
_RaidBbuEntry_Object = MibTableRow
raidBbuEntry = _RaidBbuEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 2, 1)
)
raidBbuEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "raidBbuIndex"),
)
if mibBuilder.loadTexts:
    raidBbuEntry.setStatus("current")


class _RaidBbuIndex_Type(Integer32):
    """Custom type raidBbuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RaidBbuIndex_Type.__name__ = "Integer32"
_RaidBbuIndex_Object = MibTableColumn
raidBbuIndex = _RaidBbuIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 2, 1, 1),
    _RaidBbuIndex_Type()
)
raidBbuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raidBbuIndex.setStatus("current")


class _RaidBbuId_Type(Integer32):
    """Custom type raidBbuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RaidBbuId_Type.__name__ = "Integer32"
_RaidBbuId_Object = MibTableColumn
raidBbuId = _RaidBbuId_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 2, 1, 2),
    _RaidBbuId_Type()
)
raidBbuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBbuId.setStatus("current")


class _RaidBbuStatus_Type(Integer32):
    """Custom type raidBbuStatus based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("warning", 2),
          ("error", 3))
    )


_RaidBbuStatus_Type.__name__ = "Integer32"
_RaidBbuStatus_Object = MibTableColumn
raidBbuStatus = _RaidBbuStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 2, 1, 3),
    _RaidBbuStatus_Type()
)
raidBbuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBbuStatus.setStatus("current")
_RaidBbuStatusInfo_Type = DisplayString
_RaidBbuStatusInfo_Object = MibTableColumn
raidBbuStatusInfo = _RaidBbuStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 7, 2, 1, 4),
    _RaidBbuStatusInfo_Type()
)
raidBbuStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBbuStatusInfo.setStatus("current")
_DataPart_ObjectIdentity = ObjectIdentity
dataPart = _DataPart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    dataPart.setStatus("current")
_DataPartTable_Object = MibTable
dataPartTable = _DataPartTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    dataPartTable.setStatus("current")
_DataPartEntry_Object = MibTableRow
dataPartEntry = _DataPartEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1)
)
dataPartEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "dataPartIndex"),
)
if mibBuilder.loadTexts:
    dataPartEntry.setStatus("current")
_DataPartIndex_Type = Integer32
_DataPartIndex_Object = MibTableColumn
dataPartIndex = _DataPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1, 1),
    _DataPartIndex_Type()
)
dataPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataPartIndex.setStatus("current")


class _DataPartType_Type(Integer32):
    """Custom type dataPartType based on Integer32"""
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
          ("rotationFileV1", 1),
          ("rotationFileV2", 2),
          ("virtualVolume", 3))
    )


_DataPartType_Type.__name__ = "Integer32"
_DataPartType_Object = MibTableColumn
dataPartType = _DataPartType_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1, 2),
    _DataPartType_Type()
)
dataPartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPartType.setStatus("current")
_DataPartName_Type = DisplayString
_DataPartName_Object = MibTableColumn
dataPartName = _DataPartName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1, 3),
    _DataPartName_Type()
)
dataPartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPartName.setStatus("current")
_DataPartSize_Type = Gauge32
_DataPartSize_Object = MibTableColumn
dataPartSize = _DataPartSize_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1, 4),
    _DataPartSize_Type()
)
dataPartSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPartSize.setStatus("current")
if mibBuilder.loadTexts:
    dataPartSize.setUnits("MB")
_DataPartSizeCap_Type = Gauge32
_DataPartSizeCap_Object = MibTableColumn
dataPartSizeCap = _DataPartSizeCap_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1, 5),
    _DataPartSizeCap_Type()
)
dataPartSizeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPartSizeCap.setStatus("current")
if mibBuilder.loadTexts:
    dataPartSizeCap.setUnits("MB")
_DataPartMetadataSize_Type = Gauge32
_DataPartMetadataSize_Object = MibTableColumn
dataPartMetadataSize = _DataPartMetadataSize_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1, 6),
    _DataPartMetadataSize_Type()
)
dataPartMetadataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPartMetadataSize.setStatus("current")
if mibBuilder.loadTexts:
    dataPartMetadataSize.setUnits("MB")
_DataPartMetadataSizeCap_Type = Gauge32
_DataPartMetadataSizeCap_Object = MibTableColumn
dataPartMetadataSizeCap = _DataPartMetadataSizeCap_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 8, 1, 1, 7),
    _DataPartMetadataSizeCap_Type()
)
dataPartMetadataSizeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPartMetadataSizeCap.setStatus("current")
if mibBuilder.loadTexts:
    dataPartMetadataSizeCap.setUnits("MB")
_SystemServiceLevel_Type = DisplayString
_SystemServiceLevel_Object = MibScalar
systemServiceLevel = _SystemServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 9),
    _SystemServiceLevel_Type()
)
systemServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServiceLevel.setStatus("current")
_SystemSerial_Type = DisplayString
_SystemSerial_Object = MibScalar
systemSerial = _SystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 10),
    _SystemSerial_Type()
)
systemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerial.setStatus("current")
_SystemModel_Type = DisplayString
_SystemModel_Object = MibScalar
systemModel = _SystemModel_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 1, 11),
    _SystemModel_Type()
)
systemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemModel.setStatus("current")
_Cmc_ObjectIdentity = ObjectIdentity
cmc = _Cmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 2)
)
_ApplTable_Object = MibTable
applTable = _ApplTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    applTable.setStatus("current")
_ApplEntry_Object = MibTableRow
applEntry = _ApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 2, 1, 1)
)
applEntry.setIndexNames(
    (0, "ENDACE-SYSTEM-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    applEntry.setStatus("current")
_ApplIndex_Type = Unsigned32
_ApplIndex_Object = MibTableColumn
applIndex = _ApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 2, 1, 1, 1),
    _ApplIndex_Type()
)
applIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applIndex.setStatus("current")


class _ApplName_Type(OctetString):
    """Custom type applName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ApplName_Type.__name__ = "OctetString"
_ApplName_Object = MibTableColumn
applName = _ApplName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 2, 1, 1, 2),
    _ApplName_Type()
)
applName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applName.setStatus("current")
_ApplConnected_Type = TruthValue
_ApplConnected_Object = MibTableColumn
applConnected = _ApplConnected_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 2, 1, 1, 3),
    _ApplConnected_Type()
)
applConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applConnected.setStatus("current")
_ApplOK_Type = TruthValue
_ApplOK_Object = MibTableColumn
applOK = _ApplOK_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 2, 1, 1, 4),
    _ApplOK_Type()
)
applOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOK.setStatus("current")
_RaidStatusCode_Type = RaidStatusCode
_RaidStatusCode_Object = MibScalar
raidStatusCode = _RaidStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 3),
    _RaidStatusCode_Type()
)
raidStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatusCode.setStatus("current")
_SysDiskRaidStatusCode_Type = RaidStatusCode
_SysDiskRaidStatusCode_Object = MibScalar
sysDiskRaidStatusCode = _SysDiskRaidStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 4),
    _SysDiskRaidStatusCode_Type()
)
sysDiskRaidStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDiskRaidStatusCode.setStatus("current")


class _RaidDiskStatusCode_Type(Integer32):
    """Custom type raidDiskStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("warning", 1),
          ("error", 2))
    )


_RaidDiskStatusCode_Type.__name__ = "Integer32"
_RaidDiskStatusCode_Object = MibScalar
raidDiskStatusCode = _RaidDiskStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 5),
    _RaidDiskStatusCode_Type()
)
raidDiskStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskStatusCode.setStatus("current")


class _RaidDiskSecurityMode_Type(Integer32):
    """Custom type raidDiskSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noSecurity", 0),
          ("securityEnabled", 1))
    )


_RaidDiskSecurityMode_Type.__name__ = "Integer32"
_RaidDiskSecurityMode_Object = MibScalar
raidDiskSecurityMode = _RaidDiskSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 6),
    _RaidDiskSecurityMode_Type()
)
raidDiskSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskSecurityMode.setStatus("current")
_Fips_ObjectIdentity = ObjectIdentity
fips = _Fips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fips.setStatus("current")
_FipsStatus_Type = DisplayString
_FipsStatus_Object = MibScalar
fipsStatus = _FipsStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 1, 1, 7, 1),
    _FipsStatus_Type()
)
fipsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fipsStatus.setStatus("current")
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3)
)
_NotificationPrefix_ObjectIdentity = ObjectIdentity
notificationPrefix = _NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0)
)
_SystemConformance_ObjectIdentity = ObjectIdentity
systemConformance = _SystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4)
)
_SystemGroups_ObjectIdentity = ObjectIdentity
systemGroups = _SystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1)
)
_SystemCompliances_ObjectIdentity = ObjectIdentity
systemCompliances = _SystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 2)
)

# Managed Objects groups

systemInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 1)
)
systemInformationGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "cpuIndex"),
        ("ENDACE-SYSTEM-MIB", "cpuLoad1"),
        ("ENDACE-SYSTEM-MIB", "cpuLoad5"),
        ("ENDACE-SYSTEM-MIB", "cpuLoad15"),
        ("ENDACE-SYSTEM-MIB", "cpuUtil1"),
        ("ENDACE-SYSTEM-MIB", "idleTime"),
        ("ENDACE-SYSTEM-MIB", "mountBytesAvail"),
        ("ENDACE-SYSTEM-MIB", "mountBytesFree"),
        ("ENDACE-SYSTEM-MIB", "mountBytesPercentFree"),
        ("ENDACE-SYSTEM-MIB", "mountBytesTotal"),
        ("ENDACE-SYSTEM-MIB", "mountBytesUsed"),
        ("ENDACE-SYSTEM-MIB", "mountDeviceName"),
        ("ENDACE-SYSTEM-MIB", "mountIndex"),
        ("ENDACE-SYSTEM-MIB", "mountPoint"),
        ("ENDACE-SYSTEM-MIB", "procIndex"),
        ("ENDACE-SYSTEM-MIB", "procName"),
        ("ENDACE-SYSTEM-MIB", "procNumFailures"),
        ("ENDACE-SYSTEM-MIB", "procStatus"),
        ("ENDACE-SYSTEM-MIB", "systemServiceLevel"),
        ("ENDACE-SYSTEM-MIB", "systemTime"),
        ("ENDACE-SYSTEM-MIB", "systemVersion"),
        ("ENDACE-SYSTEM-MIB", "userTime"),
        ("ENDACE-SYSTEM-MIB", "utilPct1Min"),
        ("ENDACE-SYSTEM-MIB", "systemModel"),
        ("ENDACE-SYSTEM-MIB", "systemSerial"))
)
if mibBuilder.loadTexts:
    systemInformationGroup.setStatus("current")

cmcInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 2)
)
cmcInformationGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "applIndex"),
        ("ENDACE-SYSTEM-MIB", "applName"),
        ("ENDACE-SYSTEM-MIB", "applConnected"),
        ("ENDACE-SYSTEM-MIB", "applOK"))
)
if mibBuilder.loadTexts:
    cmcInformationGroup.setStatus("current")

systemInformationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 5)
)
systemInformationGroup2.setObjects(
      *(("ENDACE-SYSTEM-MIB", "clientDescr"),
        ("ENDACE-SYSTEM-MIB", "mountInodesFree"),
        ("ENDACE-SYSTEM-MIB", "mountInodesPercentFree"),
        ("ENDACE-SYSTEM-MIB", "mountInodesTotal"),
        ("ENDACE-SYSTEM-MIB", "mountInodesUsed"),
        ("ENDACE-SYSTEM-MIB", "remoteAddr"),
        ("ENDACE-SYSTEM-MIB", "remoteHostname"),
        ("ENDACE-SYSTEM-MIB", "sessionId"),
        ("ENDACE-SYSTEM-MIB", "username"),
        ("ENDACE-SYSTEM-MIB", "usernameLocal"))
)
if mibBuilder.loadTexts:
    systemInformationGroup2.setStatus("current")

systemDiskRaidInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 6)
)
systemDiskRaidInformationGroup.setObjects(
    ("ENDACE-SYSTEM-MIB", "sysDiskRaidStatusCode")
)
if mibBuilder.loadTexts:
    systemDiskRaidInformationGroup.setStatus("current")

ssdRaidInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 8)
)
ssdRaidInformationGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "raidDiskSecurityMode"),
        ("ENDACE-SYSTEM-MIB", "raidDiskStatusCode"),
        ("ENDACE-SYSTEM-MIB", "raidDrvDefect"),
        ("ENDACE-SYSTEM-MIB", "raidDrvFdeCapable"),
        ("ENDACE-SYSTEM-MIB", "raidDrvId"),
        ("ENDACE-SYSTEM-MIB", "raidDrvLbaWritten"),
        ("ENDACE-SYSTEM-MIB", "raidDrvLocking"),
        ("ENDACE-SYSTEM-MIB", "raidDrvPending"),
        ("ENDACE-SYSTEM-MIB", "raidDrvRealloc"),
        ("ENDACE-SYSTEM-MIB", "raidDrvSecurity"),
        ("ENDACE-SYSTEM-MIB", "raidDrvSerialNo"),
        ("ENDACE-SYSTEM-MIB", "raidDrvType"),
        ("ENDACE-SYSTEM-MIB", "raidDrvUncorrErrors"),
        ("ENDACE-SYSTEM-MIB", "raidDrvWearout"),
        ("ENDACE-SYSTEM-MIB", "raidStatusCode"))
)
if mibBuilder.loadTexts:
    ssdRaidInformationGroup.setStatus("current")

bbuInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 10)
)
bbuInformationGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "raidBbuId"),
        ("ENDACE-SYSTEM-MIB", "raidBbuStatus"),
        ("ENDACE-SYSTEM-MIB", "raidBbuStatusInfo"))
)
if mibBuilder.loadTexts:
    bbuInformationGroup.setStatus("current")

dataPartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 12)
)
dataPartGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "dataPartMetadataSize"),
        ("ENDACE-SYSTEM-MIB", "dataPartMetadataSizeCap"),
        ("ENDACE-SYSTEM-MIB", "dataPartName"),
        ("ENDACE-SYSTEM-MIB", "dataPartSize"),
        ("ENDACE-SYSTEM-MIB", "dataPartSizeCap"),
        ("ENDACE-SYSTEM-MIB", "dataPartType"))
)
if mibBuilder.loadTexts:
    dataPartGroup.setStatus("current")

fipsInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 15)
)
fipsInformationGroup.setObjects(
    ("ENDACE-SYSTEM-MIB", "fipsStatus")
)
if mibBuilder.loadTexts:
    fipsInformationGroup.setStatus("current")


# Notification objects

procCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 1)
)
procCrash.setObjects(
      *(("ENDACE-SYSTEM-MIB", "procIndex"),
        ("ENDACE-SYSTEM-MIB", "procName"))
)
if mibBuilder.loadTexts:
    procCrash.setStatus(
        "current"
    )

procExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 2)
)
procExit.setObjects(
      *(("ENDACE-SYSTEM-MIB", "procIndex"),
        ("ENDACE-SYSTEM-MIB", "procName"))
)
if mibBuilder.loadTexts:
    procExit.setStatus(
        "current"
    )

procNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 3)
)
procNormal.setObjects(
      *(("ENDACE-SYSTEM-MIB", "procIndex"),
        ("ENDACE-SYSTEM-MIB", "procName"))
)
if mibBuilder.loadTexts:
    procNormal.setStatus(
        "current"
    )

cpuUtilHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 4)
)
cpuUtilHigh.setObjects(
    ("ENDACE-SYSTEM-MIB", "cpuIndex")
)
if mibBuilder.loadTexts:
    cpuUtilHigh.setStatus(
        "current"
    )

cpuUtilNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 5)
)
cpuUtilNormal.setObjects(
    ("ENDACE-SYSTEM-MIB", "cpuIndex")
)
if mibBuilder.loadTexts:
    cpuUtilNormal.setStatus(
        "current"
    )

pagingActivityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 6)
)
if mibBuilder.loadTexts:
    pagingActivityHigh.setStatus(
        "obsolete"
    )

pagingActivityNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 7)
)
if mibBuilder.loadTexts:
    pagingActivityNormal.setStatus(
        "obsolete"
    )

smartError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 8)
)
if mibBuilder.loadTexts:
    smartError.setStatus(
        "current"
    )

unexpectedShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 9)
)
if mibBuilder.loadTexts:
    unexpectedShutdown.setStatus(
        "current"
    )

diskSpaceLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 10)
)
diskSpaceLow.setObjects(
    ("ENDACE-SYSTEM-MIB", "mountPoint")
)
if mibBuilder.loadTexts:
    diskSpaceLow.setStatus(
        "current"
    )

diskSpaceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 11)
)
diskSpaceNormal.setObjects(
    ("ENDACE-SYSTEM-MIB", "mountPoint")
)
if mibBuilder.loadTexts:
    diskSpaceNormal.setStatus(
        "current"
    )

procLivenessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 12)
)
procLivenessFailure.setObjects(
      *(("ENDACE-SYSTEM-MIB", "procIndex"),
        ("ENDACE-SYSTEM-MIB", "procName"))
)
if mibBuilder.loadTexts:
    procLivenessFailure.setStatus(
        "current"
    )

cmcStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 13)
)
cmcStatusFailure.setObjects(
    ("ENDACE-SYSTEM-MIB", "applName")
)
if mibBuilder.loadTexts:
    cmcStatusFailure.setStatus(
        "current"
    )

cmcStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 14)
)
cmcStatusNormal.setObjects(
    ("ENDACE-SYSTEM-MIB", "applName")
)
if mibBuilder.loadTexts:
    cmcStatusNormal.setStatus(
        "current"
    )

memUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 15)
)
if mibBuilder.loadTexts:
    memUtilizationHigh.setStatus(
        "current"
    )

netUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 16)
)
if mibBuilder.loadTexts:
    netUtilizationHigh.setStatus(
        "current"
    )

diskIOHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 17)
)
if mibBuilder.loadTexts:
    diskIOHigh.setStatus(
        "current"
    )

cmcVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 18)
)
cmcVersionMismatch.setObjects(
    ("ENDACE-SYSTEM-MIB", "applName")
)
if mibBuilder.loadTexts:
    cmcVersionMismatch.setStatus(
        "current"
    )

raidStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 19)
)
if mibBuilder.loadTexts:
    raidStatusOk.setStatus(
        "current"
    )

raidStatusNotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 20)
)
raidStatusNotOk.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidStatusCode")
)
if mibBuilder.loadTexts:
    raidStatusNotOk.setStatus(
        "current"
    )

userLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 21)
)
userLogin.setObjects(
      *(("ENDACE-SYSTEM-MIB", "username"),
        ("ENDACE-SYSTEM-MIB", "usernameLocal"),
        ("ENDACE-SYSTEM-MIB", "remoteAddr"),
        ("ENDACE-SYSTEM-MIB", "remoteHostname"),
        ("ENDACE-SYSTEM-MIB", "clientDescr"))
)
if mibBuilder.loadTexts:
    userLogin.setStatus(
        "current"
    )

userLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 22)
)
userLogout.setObjects(
      *(("ENDACE-SYSTEM-MIB", "username"),
        ("ENDACE-SYSTEM-MIB", "usernameLocal"),
        ("ENDACE-SYSTEM-MIB", "remoteAddr"),
        ("ENDACE-SYSTEM-MIB", "remoteHostname"),
        ("ENDACE-SYSTEM-MIB", "clientDescr"))
)
if mibBuilder.loadTexts:
    userLogout.setStatus(
        "current"
    )

sysDiskRaidStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 23)
)
if mibBuilder.loadTexts:
    sysDiskRaidStatusOk.setStatus(
        "current"
    )

sysDiskRaidStatusNotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 24)
)
sysDiskRaidStatusNotOk.setObjects(
    ("ENDACE-SYSTEM-MIB", "sysDiskRaidStatusCode")
)
if mibBuilder.loadTexts:
    sysDiskRaidStatusNotOk.setStatus(
        "current"
    )

raidDiskStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 25)
)
if mibBuilder.loadTexts:
    raidDiskStatusOk.setStatus(
        "current"
    )

raidDiskStatusNotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 26)
)
raidDiskStatusNotOk.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidDiskStatusCode")
)
if mibBuilder.loadTexts:
    raidDiskStatusNotOk.setStatus(
        "current"
    )

raidDrvWearWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 27)
)
raidDrvWearWarning.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidDrvId")
)
if mibBuilder.loadTexts:
    raidDrvWearWarning.setStatus(
        "current"
    )

raidDrvWearCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 28)
)
raidDrvWearCritical.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidDrvId")
)
if mibBuilder.loadTexts:
    raidDrvWearCritical.setStatus(
        "current"
    )

raidBbuOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 29)
)
raidBbuOk.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidBbuId")
)
if mibBuilder.loadTexts:
    raidBbuOk.setStatus(
        "current"
    )

raidBbuWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 30)
)
raidBbuWarning.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidBbuId")
)
if mibBuilder.loadTexts:
    raidBbuWarning.setStatus(
        "current"
    )

raidBbuError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 31)
)
raidBbuError.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidBbuId")
)
if mibBuilder.loadTexts:
    raidBbuError.setStatus(
        "current"
    )

raidDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 32)
)
raidDiskWarning.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidDrvId")
)
if mibBuilder.loadTexts:
    raidDiskWarning.setStatus(
        "current"
    )

raidDiskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 33)
)
raidDiskError.setObjects(
    ("ENDACE-SYSTEM-MIB", "raidDrvId")
)
if mibBuilder.loadTexts:
    raidDiskError.setStatus(
        "current"
    )

cmcConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 34)
)
cmcConnectionDown.setObjects(
    ("ENDACE-SYSTEM-MIB", "applName")
)
if mibBuilder.loadTexts:
    cmcConnectionDown.setStatus(
        "current"
    )

cmcConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 35)
)
cmcConnectionUp.setObjects(
    ("ENDACE-SYSTEM-MIB", "applName")
)
if mibBuilder.loadTexts:
    cmcConnectionUp.setStatus(
        "current"
    )

ipfixEngineStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 40)
)
if mibBuilder.loadTexts:
    ipfixEngineStart.setStatus(
        "current"
    )

ipfixEngineStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 41)
)
if mibBuilder.loadTexts:
    ipfixEngineStop.setStatus(
        "current"
    )

diskIONormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 42)
)
if mibBuilder.loadTexts:
    diskIONormal.setStatus(
        "current"
    )

memUtilizationNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 43)
)
if mibBuilder.loadTexts:
    memUtilizationNormal.setStatus(
        "current"
    )

netUtilizationNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 44)
)
if mibBuilder.loadTexts:
    netUtilizationNormal.setStatus(
        "current"
    )

systemServiceLevelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 45)
)
systemServiceLevelChanged.setObjects(
    ("ENDACE-SYSTEM-MIB", "systemServiceLevel")
)
if mibBuilder.loadTexts:
    systemServiceLevelChanged.setStatus(
        "current"
    )

fipsStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 46)
)
fipsStatusChanged.setObjects(
    ("ENDACE-SYSTEM-MIB", "fipsStatus")
)
if mibBuilder.loadTexts:
    fipsStatusChanged.setStatus(
        "current"
    )

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 1, 3, 0, 100)
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        "current"
    )


# Notifications groups

systemNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 3)
)
systemNotificationsGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "cpuUtilHigh"),
        ("ENDACE-SYSTEM-MIB", "cpuUtilNormal"),
        ("ENDACE-SYSTEM-MIB", "diskIOHigh"),
        ("ENDACE-SYSTEM-MIB", "diskIONormal"),
        ("ENDACE-SYSTEM-MIB", "diskSpaceLow"),
        ("ENDACE-SYSTEM-MIB", "diskSpaceNormal"),
        ("ENDACE-SYSTEM-MIB", "memUtilizationHigh"),
        ("ENDACE-SYSTEM-MIB", "memUtilizationNormal"),
        ("ENDACE-SYSTEM-MIB", "netUtilizationHigh"),
        ("ENDACE-SYSTEM-MIB", "netUtilizationNormal"),
        ("ENDACE-SYSTEM-MIB", "procCrash"),
        ("ENDACE-SYSTEM-MIB", "procExit"),
        ("ENDACE-SYSTEM-MIB", "procLivenessFailure"),
        ("ENDACE-SYSTEM-MIB", "procNormal"),
        ("ENDACE-SYSTEM-MIB", "raidDiskError"),
        ("ENDACE-SYSTEM-MIB", "raidDiskStatusNotOk"),
        ("ENDACE-SYSTEM-MIB", "raidDiskStatusOk"),
        ("ENDACE-SYSTEM-MIB", "raidDiskWarning"),
        ("ENDACE-SYSTEM-MIB", "raidStatusNotOk"),
        ("ENDACE-SYSTEM-MIB", "raidStatusOk"),
        ("ENDACE-SYSTEM-MIB", "smartError"),
        ("ENDACE-SYSTEM-MIB", "testTrap"),
        ("ENDACE-SYSTEM-MIB", "unexpectedShutdown"),
        ("ENDACE-SYSTEM-MIB", "userLogin"),
        ("ENDACE-SYSTEM-MIB", "userLogout"),
        ("ENDACE-SYSTEM-MIB", "systemServiceLevelChanged"))
)
if mibBuilder.loadTexts:
    systemNotificationsGroup.setStatus(
        "current"
    )

cmcNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 4)
)
cmcNotificationsGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "cmcConnectionDown"),
        ("ENDACE-SYSTEM-MIB", "cmcConnectionUp"),
        ("ENDACE-SYSTEM-MIB", "cmcStatusFailure"),
        ("ENDACE-SYSTEM-MIB", "cmcStatusNormal"),
        ("ENDACE-SYSTEM-MIB", "cmcVersionMismatch"))
)
if mibBuilder.loadTexts:
    cmcNotificationsGroup.setStatus(
        "current"
    )

systemDiskRaidNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 7)
)
systemDiskRaidNotificationsGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "sysDiskRaidStatusNotOk"),
        ("ENDACE-SYSTEM-MIB", "sysDiskRaidStatusOk"))
)
if mibBuilder.loadTexts:
    systemDiskRaidNotificationsGroup.setStatus(
        "current"
    )

ssdRaidNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 9)
)
ssdRaidNotificationsGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "raidDrvWearCritical"),
        ("ENDACE-SYSTEM-MIB", "raidDrvWearWarning"))
)
if mibBuilder.loadTexts:
    ssdRaidNotificationsGroup.setStatus(
        "current"
    )

bbuNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 11)
)
bbuNotificationsGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "raidBbuError"),
        ("ENDACE-SYSTEM-MIB", "raidBbuOk"),
        ("ENDACE-SYSTEM-MIB", "raidBbuWarning"))
)
if mibBuilder.loadTexts:
    bbuNotificationsGroup.setStatus(
        "current"
    )

ipfixNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 13)
)
ipfixNotifyGroup.setObjects(
      *(("ENDACE-SYSTEM-MIB", "ipfixEngineStart"),
        ("ENDACE-SYSTEM-MIB", "ipfixEngineStop"))
)
if mibBuilder.loadTexts:
    ipfixNotifyGroup.setStatus(
        "current"
    )

obsoleteNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 14)
)
obsoleteNotifications.setObjects(
      *(("ENDACE-SYSTEM-MIB", "pagingActivityHigh"),
        ("ENDACE-SYSTEM-MIB", "pagingActivityNormal"))
)
if mibBuilder.loadTexts:
    obsoleteNotifications.setStatus(
        "obsolete"
    )

fipsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 1, 16)
)
fipsNotificationGroup.setObjects(
    ("ENDACE-SYSTEM-MIB", "fipsStatusChanged")
)
if mibBuilder.loadTexts:
    fipsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

systemCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 1, 4, 2, 1)
)
systemCompliance1.setObjects(
      *(("ENDACE-SYSTEM-MIB", "systemInformationGroup"),
        ("ENDACE-SYSTEM-MIB", "systemNotificationsGroup"),
        ("ENDACE-SYSTEM-MIB", "bbuNotificationsGroup"),
        ("ENDACE-SYSTEM-MIB", "bbuInformationGroup"),
        ("ENDACE-SYSTEM-MIB", "ssdRaidNotificationsGroup"),
        ("ENDACE-SYSTEM-MIB", "ssdRaidInformationGroup"),
        ("ENDACE-SYSTEM-MIB", "systemDiskRaidNotificationsGroup"),
        ("ENDACE-SYSTEM-MIB", "cmcNotificationsGroup"),
        ("ENDACE-SYSTEM-MIB", "cmcInformationGroup"),
        ("ENDACE-SYSTEM-MIB", "systemDiskRaidInformationGroup"),
        ("ENDACE-SYSTEM-MIB", "systemInformationGroup2"),
        ("ENDACE-SYSTEM-MIB", "ipfixNotifyGroup"))
)
if mibBuilder.loadTexts:
    systemCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-SYSTEM-MIB",
    **{"RaidStatusCode": RaidStatusCode,
       "shogunSystemMIB": shogunSystemMIB,
       "variables": variables,
       "systemAppliance": systemAppliance,
       "systemVersion": systemVersion,
       "cpu": cpu,
       "cpuLoad1": cpuLoad1,
       "cpuLoad5": cpuLoad5,
       "cpuLoad15": cpuLoad15,
       "cpuUtil1": cpuUtil1,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuIndex": cpuIndex,
       "idleTime": idleTime,
       "systemTime": systemTime,
       "userTime": userTime,
       "utilPct1Min": utilPct1Min,
       "procmgr": procmgr,
       "procTable": procTable,
       "procEntry": procEntry,
       "procIndex": procIndex,
       "procName": procName,
       "procStatus": procStatus,
       "procNumFailures": procNumFailures,
       "mountmgr": mountmgr,
       "mountTable": mountTable,
       "mountEntry": mountEntry,
       "mountIndex": mountIndex,
       "mountBytesAvail": mountBytesAvail,
       "mountBytesFree": mountBytesFree,
       "mountBytesPercentFree": mountBytesPercentFree,
       "mountBytesTotal": mountBytesTotal,
       "mountBytesUsed": mountBytesUsed,
       "mountPoint": mountPoint,
       "mountDeviceName": mountDeviceName,
       "mountInodesFree": mountInodesFree,
       "mountInodesPercentFree": mountInodesPercentFree,
       "mountInodesTotal": mountInodesTotal,
       "mountInodesUsed": mountInodesUsed,
       "sessions": sessions,
       "sessionTable": sessionTable,
       "sessionEntry": sessionEntry,
       "sessionId": sessionId,
       "username": username,
       "usernameLocal": usernameLocal,
       "remoteAddr": remoteAddr,
       "remoteHostname": remoteHostname,
       "clientDescr": clientDescr,
       "raid": raid,
       "raidDrvTable": raidDrvTable,
       "raidDrvEntry": raidDrvEntry,
       "raidDrvIndex": raidDrvIndex,
       "raidDrvId": raidDrvId,
       "raidDrvType": raidDrvType,
       "raidDrvSerialNo": raidDrvSerialNo,
       "raidDrvWearout": raidDrvWearout,
       "raidDrvLbaWritten": raidDrvLbaWritten,
       "raidDrvRealloc": raidDrvRealloc,
       "raidDrvPending": raidDrvPending,
       "raidDrvUncorrErrors": raidDrvUncorrErrors,
       "raidDrvDefect": raidDrvDefect,
       "raidDrvFdeCapable": raidDrvFdeCapable,
       "raidDrvSecurity": raidDrvSecurity,
       "raidDrvLocking": raidDrvLocking,
       "raidBbuTable": raidBbuTable,
       "raidBbuEntry": raidBbuEntry,
       "raidBbuIndex": raidBbuIndex,
       "raidBbuId": raidBbuId,
       "raidBbuStatus": raidBbuStatus,
       "raidBbuStatusInfo": raidBbuStatusInfo,
       "dataPart": dataPart,
       "dataPartTable": dataPartTable,
       "dataPartEntry": dataPartEntry,
       "dataPartIndex": dataPartIndex,
       "dataPartType": dataPartType,
       "dataPartName": dataPartName,
       "dataPartSize": dataPartSize,
       "dataPartSizeCap": dataPartSizeCap,
       "dataPartMetadataSize": dataPartMetadataSize,
       "dataPartMetadataSizeCap": dataPartMetadataSizeCap,
       "systemServiceLevel": systemServiceLevel,
       "systemSerial": systemSerial,
       "systemModel": systemModel,
       "cmc": cmc,
       "applTable": applTable,
       "applEntry": applEntry,
       "applIndex": applIndex,
       "applName": applName,
       "applConnected": applConnected,
       "applOK": applOK,
       "raidStatusCode": raidStatusCode,
       "sysDiskRaidStatusCode": sysDiskRaidStatusCode,
       "raidDiskStatusCode": raidDiskStatusCode,
       "raidDiskSecurityMode": raidDiskSecurityMode,
       "fips": fips,
       "fipsStatus": fipsStatus,
       "systemTraps": systemTraps,
       "notificationPrefix": notificationPrefix,
       "procCrash": procCrash,
       "procExit": procExit,
       "procNormal": procNormal,
       "cpuUtilHigh": cpuUtilHigh,
       "cpuUtilNormal": cpuUtilNormal,
       "pagingActivityHigh": pagingActivityHigh,
       "pagingActivityNormal": pagingActivityNormal,
       "smartError": smartError,
       "unexpectedShutdown": unexpectedShutdown,
       "diskSpaceLow": diskSpaceLow,
       "diskSpaceNormal": diskSpaceNormal,
       "procLivenessFailure": procLivenessFailure,
       "cmcStatusFailure": cmcStatusFailure,
       "cmcStatusNormal": cmcStatusNormal,
       "memUtilizationHigh": memUtilizationHigh,
       "netUtilizationHigh": netUtilizationHigh,
       "diskIOHigh": diskIOHigh,
       "cmcVersionMismatch": cmcVersionMismatch,
       "raidStatusOk": raidStatusOk,
       "raidStatusNotOk": raidStatusNotOk,
       "userLogin": userLogin,
       "userLogout": userLogout,
       "sysDiskRaidStatusOk": sysDiskRaidStatusOk,
       "sysDiskRaidStatusNotOk": sysDiskRaidStatusNotOk,
       "raidDiskStatusOk": raidDiskStatusOk,
       "raidDiskStatusNotOk": raidDiskStatusNotOk,
       "raidDrvWearWarning": raidDrvWearWarning,
       "raidDrvWearCritical": raidDrvWearCritical,
       "raidBbuOk": raidBbuOk,
       "raidBbuWarning": raidBbuWarning,
       "raidBbuError": raidBbuError,
       "raidDiskWarning": raidDiskWarning,
       "raidDiskError": raidDiskError,
       "cmcConnectionDown": cmcConnectionDown,
       "cmcConnectionUp": cmcConnectionUp,
       "ipfixEngineStart": ipfixEngineStart,
       "ipfixEngineStop": ipfixEngineStop,
       "diskIONormal": diskIONormal,
       "memUtilizationNormal": memUtilizationNormal,
       "netUtilizationNormal": netUtilizationNormal,
       "systemServiceLevelChanged": systemServiceLevelChanged,
       "fipsStatusChanged": fipsStatusChanged,
       "testTrap": testTrap,
       "systemConformance": systemConformance,
       "systemGroups": systemGroups,
       "systemInformationGroup": systemInformationGroup,
       "cmcInformationGroup": cmcInformationGroup,
       "systemNotificationsGroup": systemNotificationsGroup,
       "cmcNotificationsGroup": cmcNotificationsGroup,
       "systemInformationGroup2": systemInformationGroup2,
       "systemDiskRaidInformationGroup": systemDiskRaidInformationGroup,
       "systemDiskRaidNotificationsGroup": systemDiskRaidNotificationsGroup,
       "ssdRaidInformationGroup": ssdRaidInformationGroup,
       "ssdRaidNotificationsGroup": ssdRaidNotificationsGroup,
       "bbuInformationGroup": bbuInformationGroup,
       "bbuNotificationsGroup": bbuNotificationsGroup,
       "dataPartGroup": dataPartGroup,
       "ipfixNotifyGroup": ipfixNotifyGroup,
       "obsoleteNotifications": obsoleteNotifications,
       "fipsInformationGroup": fipsInformationGroup,
       "fipsNotificationGroup": fipsNotificationGroup,
       "systemCompliances": systemCompliances,
       "systemCompliance1": systemCompliance1}
)
