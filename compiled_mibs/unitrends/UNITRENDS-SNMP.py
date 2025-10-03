# SNMP MIB module (UNITRENDS-SNMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\unitrends\UNITRENDS-SNMP
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:44 2025
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

unitrendsSnmpModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 1)
)


# Types definitions



class OneBasedIndex(Integer32):
    """Custom type OneBasedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



class UnitrendsStatus(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCritical", 4),
          ("critical", 5),
          ("nonRecoverable", 6),
          ("lowerCritical", 7),
          ("upperCritical", 8))
    )



class UnitrendsFeatureStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("unknown", 2),
          ("disabled", 3),
          ("enabled", 4),
          ("notImplemented", 5))
    )



class UnitrendsSeverity(TextualConvention, Integer32):
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
        *(("clearing", 0),
          ("error", 1),
          ("warning", 2),
          ("information", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Unitrends_ObjectIdentity = ObjectIdentity
unitrends = _Unitrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865)
)
_Rr_ObjectIdentity = ObjectIdentity
rr = _Rr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1)
)
_TrapMembers_ObjectIdentity = ObjectIdentity
trapMembers = _TrapMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1)
)
_TrapType_Type = DisplayString
_TrapType_Object = MibScalar
trapType = _TrapType_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 1),
    _TrapType_Type()
)
trapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapType.setStatus("current")
_TrapAffectedObj_Type = DisplayString
_TrapAffectedObj_Object = MibScalar
trapAffectedObj = _TrapAffectedObj_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 2),
    _TrapAffectedObj_Type()
)
trapAffectedObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAffectedObj.setStatus("current")
_TrapDescription_Type = DisplayString
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 3),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("current")
_TrapSeverity_Type = UnitrendsSeverity
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 4),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_TrapStatus_Type = Integer32
_TrapStatus_Object = MibScalar
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 5),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapStatus.setStatus("current")
_TrapLicenseId_Type = DisplayString
_TrapLicenseId_Object = MibScalar
trapLicenseId = _TrapLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 6),
    _TrapLicenseId_Type()
)
trapLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLicenseId.setStatus("current")
_TrapDpuId_Type = DisplayString
_TrapDpuId_Object = MibScalar
trapDpuId = _TrapDpuId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 7),
    _TrapDpuId_Type()
)
trapDpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDpuId.setStatus("current")
_TrapReleaseVersion_Type = DisplayString
_TrapReleaseVersion_Object = MibScalar
trapReleaseVersion = _TrapReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 1, 8),
    _TrapReleaseVersion_Type()
)
trapReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapReleaseVersion.setStatus("current")
_TrapGroups_ObjectIdentity = ObjectIdentity
trapGroups = _TrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2)
)
_Trap100_ObjectIdentity = ObjectIdentity
trap100 = _Trap100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0)
)
_BpGroup_ObjectIdentity = ObjectIdentity
bpGroup = _BpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3)
)
_BpBackupGroup_ObjectIdentity = ObjectIdentity
bpBackupGroup = _BpBackupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10)
)
_BackupProbeInstances_Type = Integer32
_BackupProbeInstances_Object = MibScalar
backupProbeInstances = _BackupProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 1),
    _BackupProbeInstances_Type()
)
backupProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupProbeInstances.setStatus("current")
_BackupProbeTable_Object = MibTable
backupProbeTable = _BackupProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    backupProbeTable.setStatus("current")
_BackupProbeTableEntry_Object = MibTableRow
backupProbeTableEntry = _BackupProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1)
)
backupProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "backupIndex"),
)
if mibBuilder.loadTexts:
    backupProbeTableEntry.setStatus("current")
_BackupIndex_Type = OneBasedIndex
_BackupIndex_Object = MibTableColumn
backupIndex = _BackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 1),
    _BackupIndex_Type()
)
backupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupIndex.setStatus("current")
_BackupId_Type = Integer32
_BackupId_Object = MibTableColumn
backupId = _BackupId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 2),
    _BackupId_Type()
)
backupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupId.setStatus("current")
_BackupClient_Type = DisplayString
_BackupClient_Object = MibTableColumn
backupClient = _BackupClient_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 3),
    _BackupClient_Type()
)
backupClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupClient.setStatus("current")
_BackupStatusString_Type = DisplayString
_BackupStatusString_Object = MibTableColumn
backupStatusString = _BackupStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 4),
    _BackupStatusString_Type()
)
backupStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupStatusString.setStatus("current")
_BackupStatusValue_Type = Integer32
_BackupStatusValue_Object = MibTableColumn
backupStatusValue = _BackupStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 5),
    _BackupStatusValue_Type()
)
backupStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupStatusValue.setStatus("current")
_BackupTime_Type = DisplayString
_BackupTime_Object = MibTableColumn
backupTime = _BackupTime_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 6),
    _BackupTime_Type()
)
backupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupTime.setStatus("current")
_BackupType_Type = DisplayString
_BackupType_Object = MibTableColumn
backupType = _BackupType_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 7),
    _BackupType_Type()
)
backupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupType.setStatus("current")
_BackupSize_Type = DisplayString
_BackupSize_Object = MibTableColumn
backupSize = _BackupSize_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 8),
    _BackupSize_Type()
)
backupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSize.setStatus("current")
_BackupNumFiles_Type = Integer32
_BackupNumFiles_Object = MibTableColumn
backupNumFiles = _BackupNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 9),
    _BackupNumFiles_Type()
)
backupNumFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupNumFiles.setStatus("current")
_BackupIsLast_Type = Integer32
_BackupIsLast_Object = MibTableColumn
backupIsLast = _BackupIsLast_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 10, 2, 1, 10),
    _BackupIsLast_Type()
)
backupIsLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupIsLast.setStatus("current")
_BpCapacityGroup_ObjectIdentity = ObjectIdentity
bpCapacityGroup = _BpCapacityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20)
)
_CapacityProbeInstances_Type = Integer32
_CapacityProbeInstances_Object = MibScalar
capacityProbeInstances = _CapacityProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 1),
    _CapacityProbeInstances_Type()
)
capacityProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityProbeInstances.setStatus("current")
_CapacityProbeTable_Object = MibTable
capacityProbeTable = _CapacityProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2)
)
if mibBuilder.loadTexts:
    capacityProbeTable.setStatus("current")
_CapacityProbeTableEntry_Object = MibTableRow
capacityProbeTableEntry = _CapacityProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1)
)
capacityProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "capacityIndex"),
)
if mibBuilder.loadTexts:
    capacityProbeTableEntry.setStatus("current")
_CapacityIndex_Type = OneBasedIndex
_CapacityIndex_Object = MibTableColumn
capacityIndex = _CapacityIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1, 1),
    _CapacityIndex_Type()
)
capacityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityIndex.setStatus("current")
_CapacityDeviceId_Type = Integer32
_CapacityDeviceId_Object = MibTableColumn
capacityDeviceId = _CapacityDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1, 2),
    _CapacityDeviceId_Type()
)
capacityDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityDeviceId.setStatus("current")
_CapacityDeviceName_Type = DisplayString
_CapacityDeviceName_Object = MibTableColumn
capacityDeviceName = _CapacityDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1, 3),
    _CapacityDeviceName_Type()
)
capacityDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityDeviceName.setStatus("current")
_CapacityDeviceFilename_Type = DisplayString
_CapacityDeviceFilename_Object = MibTableColumn
capacityDeviceFilename = _CapacityDeviceFilename_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1, 4),
    _CapacityDeviceFilename_Type()
)
capacityDeviceFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityDeviceFilename.setStatus("current")
_CapacitySize_Type = DisplayString
_CapacitySize_Object = MibTableColumn
capacitySize = _CapacitySize_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1, 5),
    _CapacitySize_Type()
)
capacitySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacitySize.setStatus("current")
_CapacityUsed_Type = DisplayString
_CapacityUsed_Object = MibTableColumn
capacityUsed = _CapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1, 6),
    _CapacityUsed_Type()
)
capacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityUsed.setStatus("current")
_CapacityFree_Type = DisplayString
_CapacityFree_Object = MibTableColumn
capacityFree = _CapacityFree_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 20, 2, 1, 7),
    _CapacityFree_Type()
)
capacityFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityFree.setStatus("current")
_BpReplicationGroup_ObjectIdentity = ObjectIdentity
bpReplicationGroup = _BpReplicationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30)
)
_ReplicationProbeInstances_Type = Integer32
_ReplicationProbeInstances_Object = MibScalar
replicationProbeInstances = _ReplicationProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 1),
    _ReplicationProbeInstances_Type()
)
replicationProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationProbeInstances.setStatus("current")
_ReplicationProbeTable_Object = MibTable
replicationProbeTable = _ReplicationProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2)
)
if mibBuilder.loadTexts:
    replicationProbeTable.setStatus("current")
_ReplicationProbeTableEntry_Object = MibTableRow
replicationProbeTableEntry = _ReplicationProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1)
)
replicationProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "replicationIndex"),
)
if mibBuilder.loadTexts:
    replicationProbeTableEntry.setStatus("current")
_ReplicationIndex_Type = OneBasedIndex
_ReplicationIndex_Object = MibTableColumn
replicationIndex = _ReplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 1),
    _ReplicationIndex_Type()
)
replicationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationIndex.setStatus("current")
_ReplicationBackupNo_Type = Integer32
_ReplicationBackupNo_Object = MibTableColumn
replicationBackupNo = _ReplicationBackupNo_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 2),
    _ReplicationBackupNo_Type()
)
replicationBackupNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationBackupNo.setStatus("current")
_ReplicationClient_Type = DisplayString
_ReplicationClient_Object = MibTableColumn
replicationClient = _ReplicationClient_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 3),
    _ReplicationClient_Type()
)
replicationClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationClient.setStatus("current")
_ReplicationDestination_Type = DisplayString
_ReplicationDestination_Object = MibTableColumn
replicationDestination = _ReplicationDestination_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 4),
    _ReplicationDestination_Type()
)
replicationDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationDestination.setStatus("current")
_ReplicationTime_Type = DisplayString
_ReplicationTime_Object = MibTableColumn
replicationTime = _ReplicationTime_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 5),
    _ReplicationTime_Type()
)
replicationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationTime.setStatus("current")
_ReplicationSize_Type = Integer32
_ReplicationSize_Object = MibTableColumn
replicationSize = _ReplicationSize_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 6),
    _ReplicationSize_Type()
)
replicationSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationSize.setStatus("current")
_ReplicationStatusString_Type = DisplayString
_ReplicationStatusString_Object = MibTableColumn
replicationStatusString = _ReplicationStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 7),
    _ReplicationStatusString_Type()
)
replicationStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationStatusString.setStatus("current")
_ReplicationStatus_Type = Integer32
_ReplicationStatus_Object = MibTableColumn
replicationStatus = _ReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 30, 2, 1, 8),
    _ReplicationStatus_Type()
)
replicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replicationStatus.setStatus("current")
_BpArchiveGroup_ObjectIdentity = ObjectIdentity
bpArchiveGroup = _BpArchiveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40)
)
_ArchiveProbeInstances_Type = Integer32
_ArchiveProbeInstances_Object = MibScalar
archiveProbeInstances = _ArchiveProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 1),
    _ArchiveProbeInstances_Type()
)
archiveProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveProbeInstances.setStatus("current")
_ArchiveProbeTable_Object = MibTable
archiveProbeTable = _ArchiveProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2)
)
if mibBuilder.loadTexts:
    archiveProbeTable.setStatus("current")
_ArchiveProbeTableEntry_Object = MibTableRow
archiveProbeTableEntry = _ArchiveProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1)
)
archiveProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "archiveIndex"),
)
if mibBuilder.loadTexts:
    archiveProbeTableEntry.setStatus("current")
_ArchiveIndex_Type = OneBasedIndex
_ArchiveIndex_Object = MibTableColumn
archiveIndex = _ArchiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 1),
    _ArchiveIndex_Type()
)
archiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveIndex.setStatus("current")
_ArchiveDeviceId_Type = Integer32
_ArchiveDeviceId_Object = MibTableColumn
archiveDeviceId = _ArchiveDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 2),
    _ArchiveDeviceId_Type()
)
archiveDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveDeviceId.setStatus("current")
_ArchiveClient_Type = DisplayString
_ArchiveClient_Object = MibTableColumn
archiveClient = _ArchiveClient_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 3),
    _ArchiveClient_Type()
)
archiveClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveClient.setStatus("current")
_ArchiveSuccess_Type = Integer32
_ArchiveSuccess_Object = MibTableColumn
archiveSuccess = _ArchiveSuccess_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 4),
    _ArchiveSuccess_Type()
)
archiveSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveSuccess.setStatus("current")
_ArchiveSize_Type = Integer32
_ArchiveSize_Object = MibTableColumn
archiveSize = _ArchiveSize_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 5),
    _ArchiveSize_Type()
)
archiveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveSize.setStatus("current")
_ArchiveBackupTime_Type = DisplayString
_ArchiveBackupTime_Object = MibTableColumn
archiveBackupTime = _ArchiveBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 6),
    _ArchiveBackupTime_Type()
)
archiveBackupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveBackupTime.setStatus("current")
_ArchiveBackupType_Type = Integer32
_ArchiveBackupType_Object = MibTableColumn
archiveBackupType = _ArchiveBackupType_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 7),
    _ArchiveBackupType_Type()
)
archiveBackupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveBackupType.setStatus("current")
_ArchiveBackupNo_Type = Integer32
_ArchiveBackupNo_Object = MibTableColumn
archiveBackupNo = _ArchiveBackupNo_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 8),
    _ArchiveBackupNo_Type()
)
archiveBackupNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveBackupNo.setStatus("current")
_ArchiveOSType_Type = DisplayString
_ArchiveOSType_Object = MibTableColumn
archiveOSType = _ArchiveOSType_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 9),
    _ArchiveOSType_Type()
)
archiveOSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveOSType.setStatus("current")
_ArchiveErrorMsg_Type = DisplayString
_ArchiveErrorMsg_Object = MibTableColumn
archiveErrorMsg = _ArchiveErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 10),
    _ArchiveErrorMsg_Type()
)
archiveErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveErrorMsg.setStatus("current")
_ArchiveElapsedSec_Type = Integer32
_ArchiveElapsedSec_Object = MibTableColumn
archiveElapsedSec = _ArchiveElapsedSec_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 11),
    _ArchiveElapsedSec_Type()
)
archiveElapsedSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveElapsedSec.setStatus("current")
_ArchiveCompressed_Type = Integer32
_ArchiveCompressed_Object = MibTableColumn
archiveCompressed = _ArchiveCompressed_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 12),
    _ArchiveCompressed_Type()
)
archiveCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveCompressed.setStatus("current")
_ArchiveEncrypted_Type = Integer32
_ArchiveEncrypted_Object = MibTableColumn
archiveEncrypted = _ArchiveEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 3, 40, 2, 1, 13),
    _ArchiveEncrypted_Type()
)
archiveEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveEncrypted.setStatus("current")
_IpmiGroup_ObjectIdentity = ObjectIdentity
ipmiGroup = _IpmiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4)
)
_CoolingGroup_ObjectIdentity = ObjectIdentity
coolingGroup = _CoolingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10)
)
_CoolingDeviceInstances_Type = Integer32
_CoolingDeviceInstances_Object = MibScalar
coolingDeviceInstances = _CoolingDeviceInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 1),
    _CoolingDeviceInstances_Type()
)
coolingDeviceInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceInstances.setStatus("current")
_CoolingDeviceTable_Object = MibTable
coolingDeviceTable = _CoolingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2)
)
if mibBuilder.loadTexts:
    coolingDeviceTable.setStatus("current")
_CoolingDeviceTableEntry_Object = MibTableRow
coolingDeviceTableEntry = _CoolingDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1)
)
coolingDeviceTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "coolingDeviceIndex"),
)
if mibBuilder.loadTexts:
    coolingDeviceTableEntry.setStatus("current")
_CoolingDeviceIndex_Type = OneBasedIndex
_CoolingDeviceIndex_Object = MibTableColumn
coolingDeviceIndex = _CoolingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 1),
    _CoolingDeviceIndex_Type()
)
coolingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceIndex.setStatus("current")
_CoolingDeviceId_Type = Integer32
_CoolingDeviceId_Object = MibTableColumn
coolingDeviceId = _CoolingDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 2),
    _CoolingDeviceId_Type()
)
coolingDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceId.setStatus("current")
_CoolingDeviceDescription_Type = DisplayString
_CoolingDeviceDescription_Object = MibTableColumn
coolingDeviceDescription = _CoolingDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 3),
    _CoolingDeviceDescription_Type()
)
coolingDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceDescription.setStatus("current")
_CoolingDeviceStatusString_Type = DisplayString
_CoolingDeviceStatusString_Object = MibTableColumn
coolingDeviceStatusString = _CoolingDeviceStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 4),
    _CoolingDeviceStatusString_Type()
)
coolingDeviceStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStatusString.setStatus("current")
_CoolingDeviceStatus_Type = UnitrendsStatus
_CoolingDeviceStatus_Object = MibTableColumn
coolingDeviceStatus = _CoolingDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 5),
    _CoolingDeviceStatus_Type()
)
coolingDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStatus.setStatus("current")
_CoolingDeviceReading_Type = DisplayString
_CoolingDeviceReading_Object = MibTableColumn
coolingDeviceReading = _CoolingDeviceReading_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 6),
    _CoolingDeviceReading_Type()
)
coolingDeviceReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceReading.setStatus("current")
_CoolingDeviceUpperCriticalThreshold_Type = DisplayString
_CoolingDeviceUpperCriticalThreshold_Object = MibTableColumn
coolingDeviceUpperCriticalThreshold = _CoolingDeviceUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 7),
    _CoolingDeviceUpperCriticalThreshold_Type()
)
coolingDeviceUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperCriticalThreshold.setStatus("current")
_CoolingDeviceLowerCriticalThreshold_Type = DisplayString
_CoolingDeviceLowerCriticalThreshold_Object = MibTableColumn
coolingDeviceLowerCriticalThreshold = _CoolingDeviceLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 10, 2, 1, 8),
    _CoolingDeviceLowerCriticalThreshold_Type()
)
coolingDeviceLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerCriticalThreshold.setStatus("current")
_TempGroup_ObjectIdentity = ObjectIdentity
tempGroup = _TempGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20)
)
_TemperatureProbeInstances_Type = Integer32
_TemperatureProbeInstances_Object = MibScalar
temperatureProbeInstances = _TemperatureProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 1),
    _TemperatureProbeInstances_Type()
)
temperatureProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeInstances.setStatus("current")
_TemperatureProbeTable_Object = MibTable
temperatureProbeTable = _TemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2)
)
if mibBuilder.loadTexts:
    temperatureProbeTable.setStatus("current")
_TemperatureProbeTableEntry_Object = MibTableRow
temperatureProbeTableEntry = _TemperatureProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1)
)
temperatureProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureProbeTableEntry.setStatus("current")
_TemperatureIndex_Type = OneBasedIndex
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("current")
_TemperatureDeviceId_Type = Integer32
_TemperatureDeviceId_Object = MibTableColumn
temperatureDeviceId = _TemperatureDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 2),
    _TemperatureDeviceId_Type()
)
temperatureDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDeviceId.setStatus("current")
_TemperatureDescription_Type = DisplayString
_TemperatureDescription_Object = MibTableColumn
temperatureDescription = _TemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 3),
    _TemperatureDescription_Type()
)
temperatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDescription.setStatus("current")
_TemperatureStatusString_Type = DisplayString
_TemperatureStatusString_Object = MibTableColumn
temperatureStatusString = _TemperatureStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 4),
    _TemperatureStatusString_Type()
)
temperatureStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureStatusString.setStatus("current")
_TemperatureStatus_Type = UnitrendsStatus
_TemperatureStatus_Object = MibTableColumn
temperatureStatus = _TemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 5),
    _TemperatureStatus_Type()
)
temperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureStatus.setStatus("current")
_TemperatureReading_Type = DisplayString
_TemperatureReading_Object = MibTableColumn
temperatureReading = _TemperatureReading_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 6),
    _TemperatureReading_Type()
)
temperatureReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureReading.setStatus("current")
_TemperatureUpperCriticalThreshold_Type = DisplayString
_TemperatureUpperCriticalThreshold_Object = MibTableColumn
temperatureUpperCriticalThreshold = _TemperatureUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 7),
    _TemperatureUpperCriticalThreshold_Type()
)
temperatureUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureUpperCriticalThreshold.setStatus("current")
_TemperatureLowerCriticalThreshold_Type = DisplayString
_TemperatureLowerCriticalThreshold_Object = MibTableColumn
temperatureLowerCriticalThreshold = _TemperatureLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 20, 2, 1, 8),
    _TemperatureLowerCriticalThreshold_Type()
)
temperatureLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureLowerCriticalThreshold.setStatus("current")
_VoltageGroup_ObjectIdentity = ObjectIdentity
voltageGroup = _VoltageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30)
)
_VoltageProbeInstances_Type = Integer32
_VoltageProbeInstances_Object = MibScalar
voltageProbeInstances = _VoltageProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 1),
    _VoltageProbeInstances_Type()
)
voltageProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeInstances.setStatus("current")
_VoltageProbeTable_Object = MibTable
voltageProbeTable = _VoltageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2)
)
if mibBuilder.loadTexts:
    voltageProbeTable.setStatus("current")
_VoltageProbeTableEntry_Object = MibTableRow
voltageProbeTableEntry = _VoltageProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1)
)
voltageProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageProbeTableEntry.setStatus("current")
_VoltageIndex_Type = OneBasedIndex
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")
_VoltageDeviceId_Type = Integer32
_VoltageDeviceId_Object = MibTableColumn
voltageDeviceId = _VoltageDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 2),
    _VoltageDeviceId_Type()
)
voltageDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDeviceId.setStatus("current")
_VoltageDescription_Type = DisplayString
_VoltageDescription_Object = MibTableColumn
voltageDescription = _VoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 3),
    _VoltageDescription_Type()
)
voltageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescription.setStatus("current")
_VoltageStatusString_Type = DisplayString
_VoltageStatusString_Object = MibTableColumn
voltageStatusString = _VoltageStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 4),
    _VoltageStatusString_Type()
)
voltageStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageStatusString.setStatus("current")
_VoltageStatus_Type = UnitrendsStatus
_VoltageStatus_Object = MibTableColumn
voltageStatus = _VoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 5),
    _VoltageStatus_Type()
)
voltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageStatus.setStatus("current")
_VoltageReading_Type = DisplayString
_VoltageReading_Object = MibTableColumn
voltageReading = _VoltageReading_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 6),
    _VoltageReading_Type()
)
voltageReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageReading.setStatus("current")
_VoltageUpperCriticalThreshold_Type = DisplayString
_VoltageUpperCriticalThreshold_Object = MibTableColumn
voltageUpperCriticalThreshold = _VoltageUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 7),
    _VoltageUpperCriticalThreshold_Type()
)
voltageUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageUpperCriticalThreshold.setStatus("current")
_VoltageLowerCriticalThreshold_Type = DisplayString
_VoltageLowerCriticalThreshold_Object = MibTableColumn
voltageLowerCriticalThreshold = _VoltageLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 30, 2, 1, 8),
    _VoltageLowerCriticalThreshold_Type()
)
voltageLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowerCriticalThreshold.setStatus("current")
_EventlogGroup_ObjectIdentity = ObjectIdentity
eventlogGroup = _EventlogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 40)
)
_EventlogProbeInstances_Type = Integer32
_EventlogProbeInstances_Object = MibScalar
eventlogProbeInstances = _EventlogProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 40, 1),
    _EventlogProbeInstances_Type()
)
eventlogProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogProbeInstances.setStatus("current")
_EventlogProbeTable_Object = MibTable
eventlogProbeTable = _EventlogProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 40, 2)
)
if mibBuilder.loadTexts:
    eventlogProbeTable.setStatus("current")
_EventlogProbeTableEntry_Object = MibTableRow
eventlogProbeTableEntry = _EventlogProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 40, 2, 1)
)
eventlogProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    eventlogProbeTableEntry.setStatus("current")
_EventlogEntryDescription_Type = DisplayString
_EventlogEntryDescription_Object = MibScalar
eventlogEntryDescription = _EventlogEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 4, 40, 2, 1, 2),
    _EventlogEntryDescription_Type()
)
eventlogEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogEntryDescription.setStatus("current")
_DiskGroup_ObjectIdentity = ObjectIdentity
diskGroup = _DiskGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5)
)
_PhysdiskGroup_ObjectIdentity = ObjectIdentity
physdiskGroup = _PhysdiskGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10)
)
_PhysdiskProbeInstances_Type = Integer32
_PhysdiskProbeInstances_Object = MibScalar
physdiskProbeInstances = _PhysdiskProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 1),
    _PhysdiskProbeInstances_Type()
)
physdiskProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskProbeInstances.setStatus("current")
_PhysdiskProbeTable_Object = MibTable
physdiskProbeTable = _PhysdiskProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2)
)
if mibBuilder.loadTexts:
    physdiskProbeTable.setStatus("current")
_PhysdiskProbeTableEntry_Object = MibTableRow
physdiskProbeTableEntry = _PhysdiskProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1)
)
physdiskProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "physdiskIndex"),
)
if mibBuilder.loadTexts:
    physdiskProbeTableEntry.setStatus("current")
_PhysdiskIndex_Type = OneBasedIndex
_PhysdiskIndex_Object = MibTableColumn
physdiskIndex = _PhysdiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 1),
    _PhysdiskIndex_Type()
)
physdiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskIndex.setStatus("current")
_PhysdiskDeviceId_Type = Integer32
_PhysdiskDeviceId_Object = MibTableColumn
physdiskDeviceId = _PhysdiskDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 2),
    _PhysdiskDeviceId_Type()
)
physdiskDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskDeviceId.setStatus("current")
_PhysdiskDescription_Type = DisplayString
_PhysdiskDescription_Object = MibTableColumn
physdiskDescription = _PhysdiskDescription_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 3),
    _PhysdiskDescription_Type()
)
physdiskDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskDescription.setStatus("current")
_PhysdiskStatusString_Type = DisplayString
_PhysdiskStatusString_Object = MibScalar
physdiskStatusString = _PhysdiskStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 4),
    _PhysdiskStatusString_Type()
)
physdiskStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskStatusString.setStatus("current")
_PhysdiskStatus_Type = Integer32
_PhysdiskStatus_Object = MibTableColumn
physdiskStatus = _PhysdiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 5),
    _PhysdiskStatus_Type()
)
physdiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskStatus.setStatus("current")
_PhysdiskModel_Type = DisplayString
_PhysdiskModel_Object = MibScalar
physdiskModel = _PhysdiskModel_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 6),
    _PhysdiskModel_Type()
)
physdiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskModel.setStatus("current")
_PhysdiskSerialNum_Type = DisplayString
_PhysdiskSerialNum_Object = MibScalar
physdiskSerialNum = _PhysdiskSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 7),
    _PhysdiskSerialNum_Type()
)
physdiskSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskSerialNum.setStatus("current")
_PhysdiskFirmware_Type = DisplayString
_PhysdiskFirmware_Object = MibScalar
physdiskFirmware = _PhysdiskFirmware_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 8),
    _PhysdiskFirmware_Type()
)
physdiskFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskFirmware.setStatus("current")
_PhysdiskCapacity_Type = DisplayString
_PhysdiskCapacity_Object = MibScalar
physdiskCapacity = _PhysdiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 9),
    _PhysdiskCapacity_Type()
)
physdiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskCapacity.setStatus("current")
_PhysdiskPowerOnHours_Type = Integer32
_PhysdiskPowerOnHours_Object = MibScalar
physdiskPowerOnHours = _PhysdiskPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 10),
    _PhysdiskPowerOnHours_Type()
)
physdiskPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskPowerOnHours.setStatus("current")
_PhysdiskPendingSectors_Type = Integer32
_PhysdiskPendingSectors_Object = MibScalar
physdiskPendingSectors = _PhysdiskPendingSectors_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 11),
    _PhysdiskPendingSectors_Type()
)
physdiskPendingSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskPendingSectors.setStatus("current")
_PhysdiskReallocSectors_Type = Integer32
_PhysdiskReallocSectors_Object = MibScalar
physdiskReallocSectors = _PhysdiskReallocSectors_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 12),
    _PhysdiskReallocSectors_Type()
)
physdiskReallocSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskReallocSectors.setStatus("current")
_PhysdiskSeekError_Type = Integer32
_PhysdiskSeekError_Object = MibScalar
physdiskSeekError = _PhysdiskSeekError_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 10, 2, 1, 13),
    _PhysdiskSeekError_Type()
)
physdiskSeekError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physdiskSeekError.setStatus("current")
_VolumeGroup_ObjectIdentity = ObjectIdentity
volumeGroup = _VolumeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20)
)
_VolumeProbeInstances_Type = Integer32
_VolumeProbeInstances_Object = MibScalar
volumeProbeInstances = _VolumeProbeInstances_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 1),
    _VolumeProbeInstances_Type()
)
volumeProbeInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeProbeInstances.setStatus("current")
_VolumeProbeTable_Object = MibTable
volumeProbeTable = _VolumeProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 2)
)
if mibBuilder.loadTexts:
    volumeProbeTable.setStatus("current")
_VolumeProbeTableEntry_Object = MibTableRow
volumeProbeTableEntry = _VolumeProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 2, 1)
)
volumeProbeTableEntry.setIndexNames(
    (0, "UNITRENDS-SNMP", "volumeIndex"),
)
if mibBuilder.loadTexts:
    volumeProbeTableEntry.setStatus("current")
_VolumeIndex_Type = OneBasedIndex
_VolumeIndex_Object = MibTableColumn
volumeIndex = _VolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 2, 1, 1),
    _VolumeIndex_Type()
)
volumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeIndex.setStatus("current")
_VolumeDeviceId_Type = Integer32
_VolumeDeviceId_Object = MibTableColumn
volumeDeviceId = _VolumeDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 2, 1, 2),
    _VolumeDeviceId_Type()
)
volumeDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeDeviceId.setStatus("current")
_VolumeDescription_Type = DisplayString
_VolumeDescription_Object = MibTableColumn
volumeDescription = _VolumeDescription_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 2, 1, 3),
    _VolumeDescription_Type()
)
volumeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeDescription.setStatus("current")
_VolumeStatusString_Type = DisplayString
_VolumeStatusString_Object = MibTableColumn
volumeStatusString = _VolumeStatusString_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 2, 1, 4),
    _VolumeStatusString_Type()
)
volumeStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeStatusString.setStatus("current")
_VolumeStatus_Type = Integer32
_VolumeStatus_Object = MibTableColumn
volumeStatus = _VolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 5, 20, 2, 1, 5),
    _VolumeStatus_Type()
)
volumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeStatus.setStatus("current")
_MgtGroup_ObjectIdentity = ObjectIdentity
mgtGroup = _MgtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6)
)
_MgtInfoAssetId_Type = DisplayString
_MgtInfoAssetId_Object = MibScalar
mgtInfoAssetId = _MgtInfoAssetId_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 1),
    _MgtInfoAssetId_Type()
)
mgtInfoAssetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoAssetId.setStatus("current")
_MgtInfoHostname_Type = DisplayString
_MgtInfoHostname_Object = MibScalar
mgtInfoHostname = _MgtInfoHostname_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 2),
    _MgtInfoHostname_Type()
)
mgtInfoHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoHostname.setStatus("current")
_MgtInfoKernelVersion_Type = DisplayString
_MgtInfoKernelVersion_Object = MibScalar
mgtInfoKernelVersion = _MgtInfoKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 3),
    _MgtInfoKernelVersion_Type()
)
mgtInfoKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoKernelVersion.setStatus("current")
_MgtInfoMemoryTotal_Type = DisplayString
_MgtInfoMemoryTotal_Object = MibScalar
mgtInfoMemoryTotal = _MgtInfoMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 4),
    _MgtInfoMemoryTotal_Type()
)
mgtInfoMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoMemoryTotal.setStatus("current")
_MgtInfoMemoryUsed_Type = DisplayString
_MgtInfoMemoryUsed_Object = MibScalar
mgtInfoMemoryUsed = _MgtInfoMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 5),
    _MgtInfoMemoryUsed_Type()
)
mgtInfoMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoMemoryUsed.setStatus("current")
_MgtInfoMemoryFree_Type = DisplayString
_MgtInfoMemoryFree_Object = MibScalar
mgtInfoMemoryFree = _MgtInfoMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 6),
    _MgtInfoMemoryFree_Type()
)
mgtInfoMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoMemoryFree.setStatus("current")
_MgtInfoCpuUsed_Type = DisplayString
_MgtInfoCpuUsed_Object = MibScalar
mgtInfoCpuUsed = _MgtInfoCpuUsed_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 7),
    _MgtInfoCpuUsed_Type()
)
mgtInfoCpuUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoCpuUsed.setStatus("current")
_MgtInfoBaseboard_Type = DisplayString
_MgtInfoBaseboard_Object = MibScalar
mgtInfoBaseboard = _MgtInfoBaseboard_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 8),
    _MgtInfoBaseboard_Type()
)
mgtInfoBaseboard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoBaseboard.setStatus("current")
_MgtInfoBiosVersion_Type = DisplayString
_MgtInfoBiosVersion_Object = MibScalar
mgtInfoBiosVersion = _MgtInfoBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 9),
    _MgtInfoBiosVersion_Type()
)
mgtInfoBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoBiosVersion.setStatus("current")
_MgtInfoFwVersion_Type = DisplayString
_MgtInfoFwVersion_Object = MibScalar
mgtInfoFwVersion = _MgtInfoFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 10),
    _MgtInfoFwVersion_Type()
)
mgtInfoFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoFwVersion.setStatus("current")
_MgtInfoDhcpMode_Type = DisplayString
_MgtInfoDhcpMode_Object = MibScalar
mgtInfoDhcpMode = _MgtInfoDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 11),
    _MgtInfoDhcpMode_Type()
)
mgtInfoDhcpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoDhcpMode.setStatus("current")
_MgtInfoIpAddress_Type = DisplayString
_MgtInfoIpAddress_Object = MibScalar
mgtInfoIpAddress = _MgtInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 12),
    _MgtInfoIpAddress_Type()
)
mgtInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoIpAddress.setStatus("current")
_MgtInfoMacAddress_Type = DisplayString
_MgtInfoMacAddress_Object = MibScalar
mgtInfoMacAddress = _MgtInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 13),
    _MgtInfoMacAddress_Type()
)
mgtInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoMacAddress.setStatus("current")
_MgtInfoSubnetMask_Type = DisplayString
_MgtInfoSubnetMask_Object = MibScalar
mgtInfoSubnetMask = _MgtInfoSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 14),
    _MgtInfoSubnetMask_Type()
)
mgtInfoSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoSubnetMask.setStatus("current")
_MgtInfoGatewayIP_Type = DisplayString
_MgtInfoGatewayIP_Object = MibScalar
mgtInfoGatewayIP = _MgtInfoGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 15),
    _MgtInfoGatewayIP_Type()
)
mgtInfoGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoGatewayIP.setStatus("current")
_MgtInfoGatewayMac_Type = DisplayString
_MgtInfoGatewayMac_Object = MibScalar
mgtInfoGatewayMac = _MgtInfoGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 16),
    _MgtInfoGatewayMac_Type()
)
mgtInfoGatewayMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoGatewayMac.setStatus("current")
_MgtInfoLanPort_Type = DisplayString
_MgtInfoLanPort_Object = MibScalar
mgtInfoLanPort = _MgtInfoLanPort_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 17),
    _MgtInfoLanPort_Type()
)
mgtInfoLanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoLanPort.setStatus("current")
_MgtInfoManufDate_Type = DisplayString
_MgtInfoManufDate_Object = MibScalar
mgtInfoManufDate = _MgtInfoManufDate_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 18),
    _MgtInfoManufDate_Type()
)
mgtInfoManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoManufDate.setStatus("current")
_MgtInfoRelease_Type = DisplayString
_MgtInfoRelease_Object = MibScalar
mgtInfoRelease = _MgtInfoRelease_Object(
    (1, 3, 6, 1, 4, 1, 21865, 1, 6, 19),
    _MgtInfoRelease_Type()
)
mgtInfoRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgtInfoRelease.setStatus("current")

# Managed Objects groups


# Notification objects

trapGroupClients = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 1)
)
trapGroupClients.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupClients.setStatus(
        "current"
    )

trapGroup3Ware = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 2)
)
trapGroup3Ware.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroup3Ware.setStatus(
        "current"
    )

trapGroupPCI = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 3)
)
trapGroupPCI.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupPCI.setStatus(
        "current"
    )

trapGroupProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 5)
)
trapGroupProcess.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupProcess.setStatus(
        "current"
    )

trapGroupDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 6)
)
trapGroupDisk.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupDisk.setStatus(
        "current"
    )

trapGroupCEP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 7)
)
trapGroupCEP.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupCEP.setStatus(
        "current"
    )

trapGroupDPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 8)
)
trapGroupDPU.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupDPU.setStatus(
        "current"
    )

trapGroupRAID = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 9)
)
trapGroupRAID.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupRAID.setStatus(
        "current"
    )

trapGroupBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 10)
)
trapGroupBackup.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupBackup.setStatus(
        "current"
    )

trapGroupArchive = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 11)
)
trapGroupArchive.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupArchive.setStatus(
        "current"
    )

trapGroupVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 12)
)
trapGroupVersion.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupVersion.setStatus(
        "current"
    )

trapGroupNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 14)
)
trapGroupNetwork.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupNetwork.setStatus(
        "current"
    )

trapGroupDiskHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 15)
)
trapGroupDiskHealth.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupDiskHealth.setStatus(
        "current"
    )

trapGroupIPMI = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 16)
)
trapGroupIPMI.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupIPMI.setStatus(
        "current"
    )

trapGroupInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 17)
)
trapGroupInstall.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupInstall.setStatus(
        "current"
    )

trapGroupTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 21865, 1, 2, 100, 0, 99)
)
trapGroupTest.setObjects(
      *(("UNITRENDS-SNMP", "trapType"),
        ("UNITRENDS-SNMP", "trapAffectedObj"),
        ("UNITRENDS-SNMP", "trapDescription"),
        ("UNITRENDS-SNMP", "trapSeverity"),
        ("UNITRENDS-SNMP", "trapStatus"),
        ("UNITRENDS-SNMP", "trapLicenseId"),
        ("UNITRENDS-SNMP", "trapDpuId"),
        ("UNITRENDS-SNMP", "trapReleaseVersion"))
)
if mibBuilder.loadTexts:
    trapGroupTest.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UNITRENDS-SNMP",
    **{"UnitrendsStatus": UnitrendsStatus,
       "UnitrendsFeatureStatus": UnitrendsFeatureStatus,
       "UnitrendsSeverity": UnitrendsSeverity,
       "OneBasedIndex": OneBasedIndex,
       "unitrends": unitrends,
       "rr": rr,
       "trapMembers": trapMembers,
       "trapType": trapType,
       "trapAffectedObj": trapAffectedObj,
       "trapDescription": trapDescription,
       "trapSeverity": trapSeverity,
       "trapStatus": trapStatus,
       "trapLicenseId": trapLicenseId,
       "trapDpuId": trapDpuId,
       "trapReleaseVersion": trapReleaseVersion,
       "trapGroups": trapGroups,
       "trap100": trap100,
       "trapPrefix": trapPrefix,
       "trapGroupClients": trapGroupClients,
       "trapGroup3Ware": trapGroup3Ware,
       "trapGroupPCI": trapGroupPCI,
       "trapGroupProcess": trapGroupProcess,
       "trapGroupDisk": trapGroupDisk,
       "trapGroupCEP": trapGroupCEP,
       "trapGroupDPU": trapGroupDPU,
       "trapGroupRAID": trapGroupRAID,
       "trapGroupBackup": trapGroupBackup,
       "trapGroupArchive": trapGroupArchive,
       "trapGroupVersion": trapGroupVersion,
       "trapGroupNetwork": trapGroupNetwork,
       "trapGroupDiskHealth": trapGroupDiskHealth,
       "trapGroupIPMI": trapGroupIPMI,
       "trapGroupInstall": trapGroupInstall,
       "trapGroupTest": trapGroupTest,
       "bpGroup": bpGroup,
       "unitrendsSnmpModule": unitrendsSnmpModule,
       "bpBackupGroup": bpBackupGroup,
       "backupProbeInstances": backupProbeInstances,
       "backupProbeTable": backupProbeTable,
       "backupProbeTableEntry": backupProbeTableEntry,
       "backupIndex": backupIndex,
       "backupId": backupId,
       "backupClient": backupClient,
       "backupStatusString": backupStatusString,
       "backupStatusValue": backupStatusValue,
       "backupTime": backupTime,
       "backupType": backupType,
       "backupSize": backupSize,
       "backupNumFiles": backupNumFiles,
       "backupIsLast": backupIsLast,
       "bpCapacityGroup": bpCapacityGroup,
       "capacityProbeInstances": capacityProbeInstances,
       "capacityProbeTable": capacityProbeTable,
       "capacityProbeTableEntry": capacityProbeTableEntry,
       "capacityIndex": capacityIndex,
       "capacityDeviceId": capacityDeviceId,
       "capacityDeviceName": capacityDeviceName,
       "capacityDeviceFilename": capacityDeviceFilename,
       "capacitySize": capacitySize,
       "capacityUsed": capacityUsed,
       "capacityFree": capacityFree,
       "bpReplicationGroup": bpReplicationGroup,
       "replicationProbeInstances": replicationProbeInstances,
       "replicationProbeTable": replicationProbeTable,
       "replicationProbeTableEntry": replicationProbeTableEntry,
       "replicationIndex": replicationIndex,
       "replicationBackupNo": replicationBackupNo,
       "replicationClient": replicationClient,
       "replicationDestination": replicationDestination,
       "replicationTime": replicationTime,
       "replicationSize": replicationSize,
       "replicationStatusString": replicationStatusString,
       "replicationStatus": replicationStatus,
       "bpArchiveGroup": bpArchiveGroup,
       "archiveProbeInstances": archiveProbeInstances,
       "archiveProbeTable": archiveProbeTable,
       "archiveProbeTableEntry": archiveProbeTableEntry,
       "archiveIndex": archiveIndex,
       "archiveDeviceId": archiveDeviceId,
       "archiveClient": archiveClient,
       "archiveSuccess": archiveSuccess,
       "archiveSize": archiveSize,
       "archiveBackupTime": archiveBackupTime,
       "archiveBackupType": archiveBackupType,
       "archiveBackupNo": archiveBackupNo,
       "archiveOSType": archiveOSType,
       "archiveErrorMsg": archiveErrorMsg,
       "archiveElapsedSec": archiveElapsedSec,
       "archiveCompressed": archiveCompressed,
       "archiveEncrypted": archiveEncrypted,
       "ipmiGroup": ipmiGroup,
       "coolingGroup": coolingGroup,
       "coolingDeviceInstances": coolingDeviceInstances,
       "coolingDeviceTable": coolingDeviceTable,
       "coolingDeviceTableEntry": coolingDeviceTableEntry,
       "coolingDeviceIndex": coolingDeviceIndex,
       "coolingDeviceId": coolingDeviceId,
       "coolingDeviceDescription": coolingDeviceDescription,
       "coolingDeviceStatusString": coolingDeviceStatusString,
       "coolingDeviceStatus": coolingDeviceStatus,
       "coolingDeviceReading": coolingDeviceReading,
       "coolingDeviceUpperCriticalThreshold": coolingDeviceUpperCriticalThreshold,
       "coolingDeviceLowerCriticalThreshold": coolingDeviceLowerCriticalThreshold,
       "tempGroup": tempGroup,
       "temperatureProbeInstances": temperatureProbeInstances,
       "temperatureProbeTable": temperatureProbeTable,
       "temperatureProbeTableEntry": temperatureProbeTableEntry,
       "temperatureIndex": temperatureIndex,
       "temperatureDeviceId": temperatureDeviceId,
       "temperatureDescription": temperatureDescription,
       "temperatureStatusString": temperatureStatusString,
       "temperatureStatus": temperatureStatus,
       "temperatureReading": temperatureReading,
       "temperatureUpperCriticalThreshold": temperatureUpperCriticalThreshold,
       "temperatureLowerCriticalThreshold": temperatureLowerCriticalThreshold,
       "voltageGroup": voltageGroup,
       "voltageProbeInstances": voltageProbeInstances,
       "voltageProbeTable": voltageProbeTable,
       "voltageProbeTableEntry": voltageProbeTableEntry,
       "voltageIndex": voltageIndex,
       "voltageDeviceId": voltageDeviceId,
       "voltageDescription": voltageDescription,
       "voltageStatusString": voltageStatusString,
       "voltageStatus": voltageStatus,
       "voltageReading": voltageReading,
       "voltageUpperCriticalThreshold": voltageUpperCriticalThreshold,
       "voltageLowerCriticalThreshold": voltageLowerCriticalThreshold,
       "eventlogGroup": eventlogGroup,
       "eventlogProbeInstances": eventlogProbeInstances,
       "eventlogProbeTable": eventlogProbeTable,
       "eventlogProbeTableEntry": eventlogProbeTableEntry,
       "eventlogEntryDescription": eventlogEntryDescription,
       "diskGroup": diskGroup,
       "physdiskGroup": physdiskGroup,
       "physdiskProbeInstances": physdiskProbeInstances,
       "physdiskProbeTable": physdiskProbeTable,
       "physdiskProbeTableEntry": physdiskProbeTableEntry,
       "physdiskIndex": physdiskIndex,
       "physdiskDeviceId": physdiskDeviceId,
       "physdiskDescription": physdiskDescription,
       "physdiskStatusString": physdiskStatusString,
       "physdiskStatus": physdiskStatus,
       "physdiskModel": physdiskModel,
       "physdiskSerialNum": physdiskSerialNum,
       "physdiskFirmware": physdiskFirmware,
       "physdiskCapacity": physdiskCapacity,
       "physdiskPowerOnHours": physdiskPowerOnHours,
       "physdiskPendingSectors": physdiskPendingSectors,
       "physdiskReallocSectors": physdiskReallocSectors,
       "physdiskSeekError": physdiskSeekError,
       "volumeGroup": volumeGroup,
       "volumeProbeInstances": volumeProbeInstances,
       "volumeProbeTable": volumeProbeTable,
       "volumeProbeTableEntry": volumeProbeTableEntry,
       "volumeIndex": volumeIndex,
       "volumeDeviceId": volumeDeviceId,
       "volumeDescription": volumeDescription,
       "volumeStatusString": volumeStatusString,
       "volumeStatus": volumeStatus,
       "mgtGroup": mgtGroup,
       "mgtInfoAssetId": mgtInfoAssetId,
       "mgtInfoHostname": mgtInfoHostname,
       "mgtInfoKernelVersion": mgtInfoKernelVersion,
       "mgtInfoMemoryTotal": mgtInfoMemoryTotal,
       "mgtInfoMemoryUsed": mgtInfoMemoryUsed,
       "mgtInfoMemoryFree": mgtInfoMemoryFree,
       "mgtInfoCpuUsed": mgtInfoCpuUsed,
       "mgtInfoBaseboard": mgtInfoBaseboard,
       "mgtInfoBiosVersion": mgtInfoBiosVersion,
       "mgtInfoFwVersion": mgtInfoFwVersion,
       "mgtInfoDhcpMode": mgtInfoDhcpMode,
       "mgtInfoIpAddress": mgtInfoIpAddress,
       "mgtInfoMacAddress": mgtInfoMacAddress,
       "mgtInfoSubnetMask": mgtInfoSubnetMask,
       "mgtInfoGatewayIP": mgtInfoGatewayIP,
       "mgtInfoGatewayMac": mgtInfoGatewayMac,
       "mgtInfoLanPort": mgtInfoLanPort,
       "mgtInfoManufDate": mgtInfoManufDate,
       "mgtInfoRelease": mgtInfoRelease}
)
