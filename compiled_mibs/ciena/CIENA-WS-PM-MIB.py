# SNMP MIB module (CIENA-WS-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:11 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(ChannelsNumber,
 Decimal1Dig,
 Decimal3Dig,
 EnabledDisabledEnum,
 StringMaxl32,
 StringMaxl64,
 StringSci) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "ChannelsNumber",
    "Decimal1Dig",
    "Decimal3Dig",
    "EnabledDisabledEnum",
    "StringMaxl32",
    "StringMaxl64",
    "StringSci")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaWsPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22)
)
if mibBuilder.loadTexts:
    cienaWsPmMIB.setRevisions(
        ("2017-07-07 00:00",
         "2017-03-02 00:00",
         "2016-12-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmAlignment(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("startTime", 1),
          ("localClock", 2))
    )



class PmBinState(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 0),
          ("valid", 1),
          ("partial", 2),
          ("timeChange", 3),
          ("cleared", 4),
          ("idf", 5),
          ("overflow", 6))
    )



class PmConfigurationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("autoCreated", 1),
          ("userCreated", 2))
    )



class PmInstanceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proactive", 0),
          ("onDemand", 1),
          ("unknown", 2))
    )



class PmInterfaceType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("port", 0),
          ("subPort", 1),
          ("pbtTransit", 2),
          ("pbtService", 3),
          ("dataSource", 4),
          ("igmpVs", 5),
          ("accessFlow", 6),
          ("mplsVc", 7),
          ("qosFlow", 8),
          ("queueGroupInstance", 9),
          ("lineModule", 10),
          ("mplsTransitLsp", 11),
          ("mplsTransitUnidirLsp", 12),
          ("mplsTransitCoroutLsp", 13),
          ("mplsEncapLsp", 14),
          ("mplsDecapLsp", 15),
          ("ptp", 16),
          ("otu", 17),
          ("odu", 18),
          ("unknown", 19))
    )



class PmPersistenceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notInitialized", 0),
          ("initialized", 1))
    )



class PmPersistenceStatus(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("inprogress", 1),
          ("complete", 2),
          ("notFound", 3),
          ("inaccessible", 4),
          ("aborted", 5),
          ("corrupt", 6),
          ("failed", 7),
          ("partial", 8),
          ("notReady", 9))
    )



class PmProfileType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("basicTxRx", 0),
          ("basicTxRxBiDir", 1),
          ("extendedTxRx", 2),
          ("basicCounter", 3),
          ("accessStats", 4),
          ("igmpVsStats", 5),
          ("floodContainer", 6),
          ("basicRx", 7),
          ("queueGroupStats", 8),
          ("egressQueueStats", 9),
          ("basicTx", 10),
          ("basicPtp", 11),
          ("advancePtp", 12),
          ("basicOtu", 13),
          ("basicOdu", 14),
          ("unknown", 15))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsPmObjects_ObjectIdentity = ObjectIdentity
cienaWsPmObjects = _CienaWsPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 1)
)
_CienaWsPmConformance_ObjectIdentity = ObjectIdentity
cienaWsPmConformance = _CienaWsPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 2)
)
_CienaWsPmGroups_ObjectIdentity = ObjectIdentity
cienaWsPmGroups = _CienaWsPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 2, 1)
)
_CienaWsPmCompliances_ObjectIdentity = ObjectIdentity
cienaWsPmCompliances = _CienaWsPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 2, 2)
)
_CwsPmGlobalConfigTable_Object = MibTable
cwsPmGlobalConfigTable = _CwsPmGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 3)
)
if mibBuilder.loadTexts:
    cwsPmGlobalConfigTable.setStatus("current")
_CwsPmGlobalConfigEntry_Object = MibTableRow
cwsPmGlobalConfigEntry = _CwsPmGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 3, 1)
)
cwsPmGlobalConfigEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmGlobalConfigTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmGlobalConfigEntry.setStatus("current")


class _CwsPmGlobalConfigTableSnmpKey_Type(Integer32):
    """Custom type cwsPmGlobalConfigTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmGlobalConfigTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmGlobalConfigTableSnmpKey_Object = MibTableColumn
cwsPmGlobalConfigTableSnmpKey = _CwsPmGlobalConfigTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 3, 1, 1),
    _CwsPmGlobalConfigTableSnmpKey_Type()
)
cwsPmGlobalConfigTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmGlobalConfigTableSnmpKey.setStatus("current")
_CwsPmGlobalConfigAdminState_Type = EnabledDisabledEnum
_CwsPmGlobalConfigAdminState_Object = MibTableColumn
cwsPmGlobalConfigAdminState = _CwsPmGlobalConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 3, 1, 2),
    _CwsPmGlobalConfigAdminState_Type()
)
cwsPmGlobalConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmGlobalConfigAdminState.setStatus("current")
_CwsPmGlobalConfigPersistenceInterval_Type = Unsigned32
_CwsPmGlobalConfigPersistenceInterval_Object = MibTableColumn
cwsPmGlobalConfigPersistenceInterval = _CwsPmGlobalConfigPersistenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 3, 1, 3),
    _CwsPmGlobalConfigPersistenceInterval_Type()
)
cwsPmGlobalConfigPersistenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmGlobalConfigPersistenceInterval.setStatus("current")


class _CwsPmGlobalConfigPersistenceStorageLocation_Type(Integer32):
    """Custom type cwsPmGlobalConfigPersistenceStorageLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onBoard", 0),
          ("usbFlash", 1),
          ("notFound", 2))
    )


_CwsPmGlobalConfigPersistenceStorageLocation_Type.__name__ = "Integer32"
_CwsPmGlobalConfigPersistenceStorageLocation_Object = MibTableColumn
cwsPmGlobalConfigPersistenceStorageLocation = _CwsPmGlobalConfigPersistenceStorageLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 3, 1, 4),
    _CwsPmGlobalConfigPersistenceStorageLocation_Type()
)
cwsPmGlobalConfigPersistenceStorageLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmGlobalConfigPersistenceStorageLocation.setStatus("current")
_CwsPmPersistenceStateTable_Object = MibTable
cwsPmPersistenceStateTable = _CwsPmPersistenceStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4)
)
if mibBuilder.loadTexts:
    cwsPmPersistenceStateTable.setStatus("current")
_CwsPmPersistenceStateEntry_Object = MibTableRow
cwsPmPersistenceStateEntry = _CwsPmPersistenceStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1)
)
cwsPmPersistenceStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPersistenceStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmPersistenceStateEntry.setStatus("current")


class _CwsPmPersistenceStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmPersistenceStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmPersistenceStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmPersistenceStateTableSnmpKey_Object = MibTableColumn
cwsPmPersistenceStateTableSnmpKey = _CwsPmPersistenceStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 1),
    _CwsPmPersistenceStateTableSnmpKey_Type()
)
cwsPmPersistenceStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateTableSnmpKey.setStatus("current")
_CwsPmPersistenceStateState_Type = PmPersistenceState
_CwsPmPersistenceStateState_Object = MibTableColumn
cwsPmPersistenceStateState = _CwsPmPersistenceStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 2),
    _CwsPmPersistenceStateState_Type()
)
cwsPmPersistenceStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateState.setStatus("current")
_CwsPmPersistenceStateNextHistoryBinSave_Type = Unsigned32
_CwsPmPersistenceStateNextHistoryBinSave_Object = MibTableColumn
cwsPmPersistenceStateNextHistoryBinSave = _CwsPmPersistenceStateNextHistoryBinSave_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 3),
    _CwsPmPersistenceStateNextHistoryBinSave_Type()
)
cwsPmPersistenceStateNextHistoryBinSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateNextHistoryBinSave.setStatus("current")
_CwsPmPersistenceStateCurrentFileSize_Type = Unsigned32
_CwsPmPersistenceStateCurrentFileSize_Object = MibTableColumn
cwsPmPersistenceStateCurrentFileSize = _CwsPmPersistenceStateCurrentFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 4),
    _CwsPmPersistenceStateCurrentFileSize_Type()
)
cwsPmPersistenceStateCurrentFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateCurrentFileSize.setStatus("current")
_CwsPmPersistenceStateSaveStatus_Type = PmPersistenceStatus
_CwsPmPersistenceStateSaveStatus_Object = MibTableColumn
cwsPmPersistenceStateSaveStatus = _CwsPmPersistenceStateSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 5),
    _CwsPmPersistenceStateSaveStatus_Type()
)
cwsPmPersistenceStateSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateSaveStatus.setStatus("current")
_CwsPmPersistenceStateInstancesSaved_Type = Unsigned32
_CwsPmPersistenceStateInstancesSaved_Object = MibTableColumn
cwsPmPersistenceStateInstancesSaved = _CwsPmPersistenceStateInstancesSaved_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 6),
    _CwsPmPersistenceStateInstancesSaved_Type()
)
cwsPmPersistenceStateInstancesSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateInstancesSaved.setStatus("current")
_CwsPmPersistenceStateElapsedSaveTime_Type = Unsigned32
_CwsPmPersistenceStateElapsedSaveTime_Object = MibTableColumn
cwsPmPersistenceStateElapsedSaveTime = _CwsPmPersistenceStateElapsedSaveTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 7),
    _CwsPmPersistenceStateElapsedSaveTime_Type()
)
cwsPmPersistenceStateElapsedSaveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateElapsedSaveTime.setStatus("current")
_CwsPmPersistenceStateLoadStatus_Type = PmPersistenceStatus
_CwsPmPersistenceStateLoadStatus_Object = MibTableColumn
cwsPmPersistenceStateLoadStatus = _CwsPmPersistenceStateLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 8),
    _CwsPmPersistenceStateLoadStatus_Type()
)
cwsPmPersistenceStateLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateLoadStatus.setStatus("current")
_CwsPmPersistenceStateInstancesInFile_Type = Unsigned32
_CwsPmPersistenceStateInstancesInFile_Object = MibTableColumn
cwsPmPersistenceStateInstancesInFile = _CwsPmPersistenceStateInstancesInFile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 9),
    _CwsPmPersistenceStateInstancesInFile_Type()
)
cwsPmPersistenceStateInstancesInFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateInstancesInFile.setStatus("current")
_CwsPmPersistenceStateInstancesLoaded_Type = Unsigned32
_CwsPmPersistenceStateInstancesLoaded_Object = MibTableColumn
cwsPmPersistenceStateInstancesLoaded = _CwsPmPersistenceStateInstancesLoaded_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 10),
    _CwsPmPersistenceStateInstancesLoaded_Type()
)
cwsPmPersistenceStateInstancesLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateInstancesLoaded.setStatus("current")
_CwsPmPersistenceStateElapsedLoadTime_Type = Unsigned32
_CwsPmPersistenceStateElapsedLoadTime_Object = MibTableColumn
cwsPmPersistenceStateElapsedLoadTime = _CwsPmPersistenceStateElapsedLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 4, 1, 11),
    _CwsPmPersistenceStateElapsedLoadTime_Type()
)
cwsPmPersistenceStateElapsedLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPersistenceStateElapsedLoadTime.setStatus("current")
_CwsPmInstancesTable_Object = MibTable
cwsPmInstancesTable = _CwsPmInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5)
)
if mibBuilder.loadTexts:
    cwsPmInstancesTable.setStatus("current")
_CwsPmInstancesEntry_Object = MibTableRow
cwsPmInstancesEntry = _CwsPmInstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1)
)
cwsPmInstancesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmInstancesInstanceId"),
)
if mibBuilder.loadTexts:
    cwsPmInstancesEntry.setStatus("current")


class _CwsPmInstancesInstanceId_Type(Integer32):
    """Custom type cwsPmInstancesInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmInstancesInstanceId_Type.__name__ = "Integer32"
_CwsPmInstancesInstanceId_Object = MibTableColumn
cwsPmInstancesInstanceId = _CwsPmInstancesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 1),
    _CwsPmInstancesInstanceId_Type()
)
cwsPmInstancesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmInstancesInstanceId.setStatus("current")
_CwsPmInstancesInstanceName_Type = StringMaxl32
_CwsPmInstancesInstanceName_Object = MibTableColumn
cwsPmInstancesInstanceName = _CwsPmInstancesInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 2),
    _CwsPmInstancesInstanceName_Type()
)
cwsPmInstancesInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesInstanceName.setStatus("current")
_CwsPmInstancesAdminState_Type = EnabledDisabledEnum
_CwsPmInstancesAdminState_Object = MibTableColumn
cwsPmInstancesAdminState = _CwsPmInstancesAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 3),
    _CwsPmInstancesAdminState_Type()
)
cwsPmInstancesAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesAdminState.setStatus("current")
_CwsPmInstancesOperationalState_Type = EnabledDisabledEnum
_CwsPmInstancesOperationalState_Object = MibTableColumn
cwsPmInstancesOperationalState = _CwsPmInstancesOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 4),
    _CwsPmInstancesOperationalState_Type()
)
cwsPmInstancesOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesOperationalState.setStatus("current")
_CwsPmInstancesInstanceType_Type = PmInstanceType
_CwsPmInstancesInstanceType_Object = MibTableColumn
cwsPmInstancesInstanceType = _CwsPmInstancesInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 5),
    _CwsPmInstancesInstanceType_Type()
)
cwsPmInstancesInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesInstanceType.setStatus("current")
_CwsPmInstancesBinCount_Type = Unsigned32
_CwsPmInstancesBinCount_Object = MibTableColumn
cwsPmInstancesBinCount = _CwsPmInstancesBinCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 6),
    _CwsPmInstancesBinCount_Type()
)
cwsPmInstancesBinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesBinCount.setStatus("current")
_CwsPmInstancesBinDuration_Type = Unsigned32
_CwsPmInstancesBinDuration_Object = MibTableColumn
cwsPmInstancesBinDuration = _CwsPmInstancesBinDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 7),
    _CwsPmInstancesBinDuration_Type()
)
cwsPmInstancesBinDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesBinDuration.setStatus("current")
_CwsPmInstancesAttachedInterfaceType_Type = PmInterfaceType
_CwsPmInstancesAttachedInterfaceType_Object = MibTableColumn
cwsPmInstancesAttachedInterfaceType = _CwsPmInstancesAttachedInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 8),
    _CwsPmInstancesAttachedInterfaceType_Type()
)
cwsPmInstancesAttachedInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesAttachedInterfaceType.setStatus("current")
_CwsPmInstancesAttachedInterfaceName_Type = StringMaxl32
_CwsPmInstancesAttachedInterfaceName_Object = MibTableColumn
cwsPmInstancesAttachedInterfaceName = _CwsPmInstancesAttachedInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 5, 1, 9),
    _CwsPmInstancesAttachedInterfaceName_Type()
)
cwsPmInstancesAttachedInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmInstancesAttachedInterfaceName.setStatus("current")
_CwsPmPortExtendedTxRxInstancesTable_Object = MibTable
cwsPmPortExtendedTxRxInstancesTable = _CwsPmPortExtendedTxRxInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 6)
)
if mibBuilder.loadTexts:
    cwsPmPortExtendedTxRxInstancesTable.setStatus("current")
_CwsPmPortExtendedTxRxInstancesEntry_Object = MibTableRow
cwsPmPortExtendedTxRxInstancesEntry = _CwsPmPortExtendedTxRxInstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 6, 1)
)
cwsPmPortExtendedTxRxInstancesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
)
if mibBuilder.loadTexts:
    cwsPmPortExtendedTxRxInstancesEntry.setStatus("current")


class _CwsPmPortExtendedTxRxInstancesInstanceName_Type(Integer32):
    """Custom type cwsPmPortExtendedTxRxInstancesInstanceName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmPortExtendedTxRxInstancesInstanceName_Type.__name__ = "Integer32"
_CwsPmPortExtendedTxRxInstancesInstanceName_Object = MibTableColumn
cwsPmPortExtendedTxRxInstancesInstanceName = _CwsPmPortExtendedTxRxInstancesInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 6, 1, 1),
    _CwsPmPortExtendedTxRxInstancesInstanceName_Type()
)
cwsPmPortExtendedTxRxInstancesInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPortExtendedTxRxInstancesInstanceName.setStatus("current")
_CwsPmExtendedIdTable_Object = MibTable
cwsPmExtendedIdTable = _CwsPmExtendedIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 7)
)
if mibBuilder.loadTexts:
    cwsPmExtendedIdTable.setStatus("current")
_CwsPmExtendedIdEntry_Object = MibTableRow
cwsPmExtendedIdEntry = _CwsPmExtendedIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 7, 1)
)
cwsPmExtendedIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedIdEntry.setStatus("current")


class _CwsPmExtendedIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedIdTableSnmpKey_Object = MibTableColumn
cwsPmExtendedIdTableSnmpKey = _CwsPmExtendedIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 7, 1, 1),
    _CwsPmExtendedIdTableSnmpKey_Type()
)
cwsPmExtendedIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedIdTableSnmpKey.setStatus("current")
_CwsPmExtendedIdInstanceId_Type = Unsigned32
_CwsPmExtendedIdInstanceId_Object = MibTableColumn
cwsPmExtendedIdInstanceId = _CwsPmExtendedIdInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 7, 1, 2),
    _CwsPmExtendedIdInstanceId_Type()
)
cwsPmExtendedIdInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedIdInstanceId.setStatus("current")
_CwsPmExtendedIdInstanceType_Type = PmInstanceType
_CwsPmExtendedIdInstanceType_Object = MibTableColumn
cwsPmExtendedIdInstanceType = _CwsPmExtendedIdInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 7, 1, 3),
    _CwsPmExtendedIdInstanceType_Type()
)
cwsPmExtendedIdInstanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedIdInstanceType.setStatus("current")
_CwsPmExtendedIdProfileType_Type = PmProfileType
_CwsPmExtendedIdProfileType_Object = MibTableColumn
cwsPmExtendedIdProfileType = _CwsPmExtendedIdProfileType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 7, 1, 4),
    _CwsPmExtendedIdProfileType_Type()
)
cwsPmExtendedIdProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedIdProfileType.setStatus("current")
_CwsPmExtendedStateTable_Object = MibTable
cwsPmExtendedStateTable = _CwsPmExtendedStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8)
)
if mibBuilder.loadTexts:
    cwsPmExtendedStateTable.setStatus("current")
_CwsPmExtendedStateEntry_Object = MibTableRow
cwsPmExtendedStateEntry = _CwsPmExtendedStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8, 1)
)
cwsPmExtendedStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedStateEntry.setStatus("current")


class _CwsPmExtendedStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedStateTableSnmpKey_Object = MibTableColumn
cwsPmExtendedStateTableSnmpKey = _CwsPmExtendedStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8, 1, 1),
    _CwsPmExtendedStateTableSnmpKey_Type()
)
cwsPmExtendedStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedStateTableSnmpKey.setStatus("current")
_CwsPmExtendedStateAdminState_Type = EnabledDisabledEnum
_CwsPmExtendedStateAdminState_Object = MibTableColumn
cwsPmExtendedStateAdminState = _CwsPmExtendedStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8, 1, 2),
    _CwsPmExtendedStateAdminState_Type()
)
cwsPmExtendedStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedStateAdminState.setStatus("current")
_CwsPmExtendedStateOperationalState_Type = EnabledDisabledEnum
_CwsPmExtendedStateOperationalState_Object = MibTableColumn
cwsPmExtendedStateOperationalState = _CwsPmExtendedStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8, 1, 3),
    _CwsPmExtendedStateOperationalState_Type()
)
cwsPmExtendedStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedStateOperationalState.setStatus("current")
_CwsPmExtendedStateCurrentBinId_Type = Unsigned32
_CwsPmExtendedStateCurrentBinId_Object = MibTableColumn
cwsPmExtendedStateCurrentBinId = _CwsPmExtendedStateCurrentBinId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8, 1, 4),
    _CwsPmExtendedStateCurrentBinId_Type()
)
cwsPmExtendedStateCurrentBinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedStateCurrentBinId.setStatus("current")
_CwsPmExtendedStateCollectionStartDateTime_Type = StringMaxl64
_CwsPmExtendedStateCollectionStartDateTime_Object = MibTableColumn
cwsPmExtendedStateCollectionStartDateTime = _CwsPmExtendedStateCollectionStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8, 1, 5),
    _CwsPmExtendedStateCollectionStartDateTime_Type()
)
cwsPmExtendedStateCollectionStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedStateCollectionStartDateTime.setStatus("current")
_CwsPmExtendedStateCollectionEndDateTime_Type = StringMaxl64
_CwsPmExtendedStateCollectionEndDateTime_Object = MibTableColumn
cwsPmExtendedStateCollectionEndDateTime = _CwsPmExtendedStateCollectionEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 8, 1, 6),
    _CwsPmExtendedStateCollectionEndDateTime_Type()
)
cwsPmExtendedStateCollectionEndDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedStateCollectionEndDateTime.setStatus("current")
_CwsPmExtendedPropertiesTable_Object = MibTable
cwsPmExtendedPropertiesTable = _CwsPmExtendedPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 9)
)
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesTable.setStatus("current")
_CwsPmExtendedPropertiesEntry_Object = MibTableRow
cwsPmExtendedPropertiesEntry = _CwsPmExtendedPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 9, 1)
)
cwsPmExtendedPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesEntry.setStatus("current")


class _CwsPmExtendedPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedPropertiesTableSnmpKey_Object = MibTableColumn
cwsPmExtendedPropertiesTableSnmpKey = _CwsPmExtendedPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 9, 1, 1),
    _CwsPmExtendedPropertiesTableSnmpKey_Type()
)
cwsPmExtendedPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesTableSnmpKey.setStatus("current")
_CwsPmExtendedPropertiesConfigurationMode_Type = PmConfigurationMode
_CwsPmExtendedPropertiesConfigurationMode_Object = MibTableColumn
cwsPmExtendedPropertiesConfigurationMode = _CwsPmExtendedPropertiesConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 9, 1, 2),
    _CwsPmExtendedPropertiesConfigurationMode_Type()
)
cwsPmExtendedPropertiesConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesConfigurationMode.setStatus("current")
_CwsPmExtendedPropertiesAlignment_Type = PmAlignment
_CwsPmExtendedPropertiesAlignment_Object = MibTableColumn
cwsPmExtendedPropertiesAlignment = _CwsPmExtendedPropertiesAlignment_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 9, 1, 3),
    _CwsPmExtendedPropertiesAlignment_Type()
)
cwsPmExtendedPropertiesAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesAlignment.setStatus("current")
_CwsPmExtendedPropertiesConfiguredBinCount_Type = Unsigned32
_CwsPmExtendedPropertiesConfiguredBinCount_Object = MibTableColumn
cwsPmExtendedPropertiesConfiguredBinCount = _CwsPmExtendedPropertiesConfiguredBinCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 9, 1, 4),
    _CwsPmExtendedPropertiesConfiguredBinCount_Type()
)
cwsPmExtendedPropertiesConfiguredBinCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesConfiguredBinCount.setStatus("current")
_CwsPmExtendedPropertiesConfiguredBinDuration_Type = Unsigned32
_CwsPmExtendedPropertiesConfiguredBinDuration_Object = MibTableColumn
cwsPmExtendedPropertiesConfiguredBinDuration = _CwsPmExtendedPropertiesConfiguredBinDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 9, 1, 5),
    _CwsPmExtendedPropertiesConfiguredBinDuration_Type()
)
cwsPmExtendedPropertiesConfiguredBinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesConfiguredBinDuration.setStatus("current")
_CwsPmExtendedPropertiesAttachedInterfacesTable_Object = MibTable
cwsPmExtendedPropertiesAttachedInterfacesTable = _CwsPmExtendedPropertiesAttachedInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 10)
)
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesAttachedInterfacesTable.setStatus("current")
_CwsPmExtendedPropertiesAttachedInterfacesEntry_Object = MibTableRow
cwsPmExtendedPropertiesAttachedInterfacesEntry = _CwsPmExtendedPropertiesAttachedInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 10, 1)
)
cwsPmExtendedPropertiesAttachedInterfacesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesAttachedInterfacesEntry.setStatus("current")


class _CwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey_Object = MibTableColumn
cwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey = _CwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 10, 1, 1),
    _CwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey_Type()
)
cwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey.setStatus("current")
_CwsPmExtendedPropertiesAttachedInterfacesType_Type = PmInterfaceType
_CwsPmExtendedPropertiesAttachedInterfacesType_Object = MibTableColumn
cwsPmExtendedPropertiesAttachedInterfacesType = _CwsPmExtendedPropertiesAttachedInterfacesType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 10, 1, 2),
    _CwsPmExtendedPropertiesAttachedInterfacesType_Type()
)
cwsPmExtendedPropertiesAttachedInterfacesType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesAttachedInterfacesType.setStatus("current")
_CwsPmExtendedPropertiesAttachedInterfacesName_Type = StringMaxl32
_CwsPmExtendedPropertiesAttachedInterfacesName_Object = MibTableColumn
cwsPmExtendedPropertiesAttachedInterfacesName = _CwsPmExtendedPropertiesAttachedInterfacesName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 10, 1, 3),
    _CwsPmExtendedPropertiesAttachedInterfacesName_Type()
)
cwsPmExtendedPropertiesAttachedInterfacesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesAttachedInterfacesName.setStatus("current")
_CwsPmExtendedPropertiesAttachedInterfacesOperationalState_Type = EnabledDisabledEnum
_CwsPmExtendedPropertiesAttachedInterfacesOperationalState_Object = MibTableColumn
cwsPmExtendedPropertiesAttachedInterfacesOperationalState = _CwsPmExtendedPropertiesAttachedInterfacesOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 10, 1, 4),
    _CwsPmExtendedPropertiesAttachedInterfacesOperationalState_Type()
)
cwsPmExtendedPropertiesAttachedInterfacesOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedPropertiesAttachedInterfacesOperationalState.setStatus("current")
_CwsPmExtendedCurrentIdTable_Object = MibTable
cwsPmExtendedCurrentIdTable = _CwsPmExtendedCurrentIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 11)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentIdTable.setStatus("current")
_CwsPmExtendedCurrentIdEntry_Object = MibTableRow
cwsPmExtendedCurrentIdEntry = _CwsPmExtendedCurrentIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 11, 1)
)
cwsPmExtendedCurrentIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentIdEntry.setStatus("current")


class _CwsPmExtendedCurrentIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentIdTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentIdTableSnmpKey = _CwsPmExtendedCurrentIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 11, 1, 1),
    _CwsPmExtendedCurrentIdTableSnmpKey_Type()
)
cwsPmExtendedCurrentIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentIdTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentIdBinNumber_Type = Unsigned32
_CwsPmExtendedCurrentIdBinNumber_Object = MibTableColumn
cwsPmExtendedCurrentIdBinNumber = _CwsPmExtendedCurrentIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 11, 1, 2),
    _CwsPmExtendedCurrentIdBinNumber_Type()
)
cwsPmExtendedCurrentIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentIdBinNumber.setStatus("current")
_CwsPmExtendedCurrentIdBinName_Type = StringMaxl32
_CwsPmExtendedCurrentIdBinName_Object = MibTableColumn
cwsPmExtendedCurrentIdBinName = _CwsPmExtendedCurrentIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 11, 1, 3),
    _CwsPmExtendedCurrentIdBinName_Type()
)
cwsPmExtendedCurrentIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentIdBinName.setStatus("current")
_CwsPmExtendedCurrentStateTable_Object = MibTable
cwsPmExtendedCurrentStateTable = _CwsPmExtendedCurrentStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 12)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStateTable.setStatus("current")
_CwsPmExtendedCurrentStateEntry_Object = MibTableRow
cwsPmExtendedCurrentStateEntry = _CwsPmExtendedCurrentStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 12, 1)
)
cwsPmExtendedCurrentStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStateEntry.setStatus("current")


class _CwsPmExtendedCurrentStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentStateTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentStateTableSnmpKey = _CwsPmExtendedCurrentStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 12, 1, 1),
    _CwsPmExtendedCurrentStateTableSnmpKey_Type()
)
cwsPmExtendedCurrentStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStateTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentStateStartDateTime_Type = StringMaxl32
_CwsPmExtendedCurrentStateStartDateTime_Object = MibTableColumn
cwsPmExtendedCurrentStateStartDateTime = _CwsPmExtendedCurrentStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 12, 1, 2),
    _CwsPmExtendedCurrentStateStartDateTime_Type()
)
cwsPmExtendedCurrentStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStateStartDateTime.setStatus("current")
_CwsPmExtendedCurrentStateClearedDateTime_Type = StringMaxl32
_CwsPmExtendedCurrentStateClearedDateTime_Object = MibTableColumn
cwsPmExtendedCurrentStateClearedDateTime = _CwsPmExtendedCurrentStateClearedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 12, 1, 3),
    _CwsPmExtendedCurrentStateClearedDateTime_Type()
)
cwsPmExtendedCurrentStateClearedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStateClearedDateTime.setStatus("current")
_CwsPmExtendedCurrentStateState_Type = PmBinState
_CwsPmExtendedCurrentStateState_Object = MibTableColumn
cwsPmExtendedCurrentStateState = _CwsPmExtendedCurrentStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 12, 1, 4),
    _CwsPmExtendedCurrentStateState_Type()
)
cwsPmExtendedCurrentStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStateState.setStatus("current")
_CwsPmExtendedCurrentStatisticsTable_Object = MibTable
cwsPmExtendedCurrentStatisticsTable = _CwsPmExtendedCurrentStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 13)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStatisticsTable.setStatus("current")
_CwsPmExtendedCurrentStatisticsEntry_Object = MibTableRow
cwsPmExtendedCurrentStatisticsEntry = _CwsPmExtendedCurrentStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 13, 1)
)
cwsPmExtendedCurrentStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStatisticsEntry.setStatus("current")


class _CwsPmExtendedCurrentStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentStatisticsTableSnmpKey = _CwsPmExtendedCurrentStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 13, 1, 1),
    _CwsPmExtendedCurrentStatisticsTableSnmpKey_Type()
)
cwsPmExtendedCurrentStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStatisticsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentStatisticsFrameErrorRatio_Type = Counter64
_CwsPmExtendedCurrentStatisticsFrameErrorRatio_Object = MibTableColumn
cwsPmExtendedCurrentStatisticsFrameErrorRatio = _CwsPmExtendedCurrentStatisticsFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 13, 1, 2),
    _CwsPmExtendedCurrentStatisticsFrameErrorRatio_Type()
)
cwsPmExtendedCurrentStatisticsFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentStatisticsFrameErrorRatio.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsTable_Object = MibTable
cwsPmExtendedCurrentRxIfCountsTable = _CwsPmExtendedCurrentRxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsTable.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsEntry_Object = MibTableRow
cwsPmExtendedCurrentRxIfCountsEntry = _CwsPmExtendedCurrentRxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1)
)
cwsPmExtendedCurrentRxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsEntry.setStatus("current")


class _CwsPmExtendedCurrentRxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentRxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentRxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentRxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsTableSnmpKey = _CwsPmExtendedCurrentRxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 1),
    _CwsPmExtendedCurrentRxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedCurrentRxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsBytes_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsBytes = _CwsPmExtendedCurrentRxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 2),
    _CwsPmExtendedCurrentRxIfCountsBytes_Type()
)
cwsPmExtendedCurrentRxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsBytes.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPackets = _CwsPmExtendedCurrentRxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 3),
    _CwsPmExtendedCurrentRxIfCountsPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsCrcErroredPackets = _CwsPmExtendedCurrentRxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 4),
    _CwsPmExtendedCurrentRxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsMulticastPackets = _CwsPmExtendedCurrentRxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 5),
    _CwsPmExtendedCurrentRxIfCountsMulticastPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsBroadcastPackets = _CwsPmExtendedCurrentRxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 6),
    _CwsPmExtendedCurrentRxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPausePackets = _CwsPmExtendedCurrentRxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 7),
    _CwsPmExtendedCurrentRxIfCountsPausePackets_Type()
)
cwsPmExtendedCurrentRxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsUndersizedPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsUndersizedPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsUndersizedPackets = _CwsPmExtendedCurrentRxIfCountsUndersizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 8),
    _CwsPmExtendedCurrentRxIfCountsUndersizedPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsUndersizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsUndersizedPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsOversizedPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsOversizedPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsOversizedPackets = _CwsPmExtendedCurrentRxIfCountsOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 9),
    _CwsPmExtendedCurrentRxIfCountsOversizedPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsOversizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsOversizedPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsFragmentPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsFragmentPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsFragmentPackets = _CwsPmExtendedCurrentRxIfCountsFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 10),
    _CwsPmExtendedCurrentRxIfCountsFragmentPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsFragmentPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsFragmentPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsJabberPackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsJabberPackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsJabberPackets = _CwsPmExtendedCurrentRxIfCountsJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 11),
    _CwsPmExtendedCurrentRxIfCountsJabberPackets_Type()
)
cwsPmExtendedCurrentRxIfCountsJabberPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsJabberPackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsLengthOutRangePackets = _CwsPmExtendedCurrentRxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 12),
    _CwsPmExtendedCurrentRxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedCurrentRxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPackets64Octet_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPackets64Octet_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPackets64Octet = _CwsPmExtendedCurrentRxIfCountsPackets64Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 13),
    _CwsPmExtendedCurrentRxIfCountsPackets64Octet_Type()
)
cwsPmExtendedCurrentRxIfCountsPackets64Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPackets64Octet.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPackets65127Octet_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPackets65127Octet_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPackets65127Octet = _CwsPmExtendedCurrentRxIfCountsPackets65127Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 14),
    _CwsPmExtendedCurrentRxIfCountsPackets65127Octet_Type()
)
cwsPmExtendedCurrentRxIfCountsPackets65127Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPackets65127Octet.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPackets128255Octet_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPackets128255Octet_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPackets128255Octet = _CwsPmExtendedCurrentRxIfCountsPackets128255Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 15),
    _CwsPmExtendedCurrentRxIfCountsPackets128255Octet_Type()
)
cwsPmExtendedCurrentRxIfCountsPackets128255Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPackets128255Octet.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPackets256511Octet_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPackets256511Octet_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPackets256511Octet = _CwsPmExtendedCurrentRxIfCountsPackets256511Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 16),
    _CwsPmExtendedCurrentRxIfCountsPackets256511Octet_Type()
)
cwsPmExtendedCurrentRxIfCountsPackets256511Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPackets256511Octet.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPackets5121023Octet_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPackets5121023Octet_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPackets5121023Octet = _CwsPmExtendedCurrentRxIfCountsPackets5121023Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 17),
    _CwsPmExtendedCurrentRxIfCountsPackets5121023Octet_Type()
)
cwsPmExtendedCurrentRxIfCountsPackets5121023Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPackets5121023Octet.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsPackets10241518Octet_Type = Counter64
_CwsPmExtendedCurrentRxIfCountsPackets10241518Octet_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsPackets10241518Octet = _CwsPmExtendedCurrentRxIfCountsPackets10241518Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 18),
    _CwsPmExtendedCurrentRxIfCountsPackets10241518Octet_Type()
)
cwsPmExtendedCurrentRxIfCountsPackets10241518Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsPackets10241518Octet.setStatus("current")
_CwsPmExtendedCurrentRxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedCurrentRxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedCurrentRxIfCountsAverageLinkUtilization = _CwsPmExtendedCurrentRxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 14, 1, 19),
    _CwsPmExtendedCurrentRxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedCurrentRxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentRxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsTable_Object = MibTable
cwsPmExtendedCurrentTxIfCountsTable = _CwsPmExtendedCurrentTxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsTable.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsEntry_Object = MibTableRow
cwsPmExtendedCurrentTxIfCountsEntry = _CwsPmExtendedCurrentTxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1)
)
cwsPmExtendedCurrentTxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsEntry.setStatus("current")


class _CwsPmExtendedCurrentTxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentTxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentTxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentTxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsTableSnmpKey = _CwsPmExtendedCurrentTxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 1),
    _CwsPmExtendedCurrentTxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedCurrentTxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsBytes_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsBytes = _CwsPmExtendedCurrentTxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 2),
    _CwsPmExtendedCurrentTxIfCountsBytes_Type()
)
cwsPmExtendedCurrentTxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsBytes.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsPackets = _CwsPmExtendedCurrentTxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 3),
    _CwsPmExtendedCurrentTxIfCountsPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsCrcErroredPackets = _CwsPmExtendedCurrentTxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 4),
    _CwsPmExtendedCurrentTxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsMulticastPackets = _CwsPmExtendedCurrentTxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 5),
    _CwsPmExtendedCurrentTxIfCountsMulticastPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsBroadcastPackets = _CwsPmExtendedCurrentTxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 6),
    _CwsPmExtendedCurrentTxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsPausePackets = _CwsPmExtendedCurrentTxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 7),
    _CwsPmExtendedCurrentTxIfCountsPausePackets_Type()
)
cwsPmExtendedCurrentTxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets = _CwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 8),
    _CwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsGiantPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsGiantPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsGiantPackets = _CwsPmExtendedCurrentTxIfCountsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 9),
    _CwsPmExtendedCurrentTxIfCountsGiantPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsGiantPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsGiantPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsUnderrunPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsUnderrunPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsUnderrunPackets = _CwsPmExtendedCurrentTxIfCountsUnderrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 10),
    _CwsPmExtendedCurrentTxIfCountsUnderrunPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsUnderrunPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsUnderrunPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets = _CwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 11),
    _CwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets_Type()
)
cwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedCurrentTxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsLengthOutRangePackets = _CwsPmExtendedCurrentTxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 12),
    _CwsPmExtendedCurrentTxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedCurrentTxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedCurrentTxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedCurrentTxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedCurrentTxIfCountsAverageLinkUtilization = _CwsPmExtendedCurrentTxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 15, 1, 13),
    _CwsPmExtendedCurrentTxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedCurrentTxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmExtendedCurrentTxQueueTable_Object = MibTable
cwsPmExtendedCurrentTxQueueTable = _CwsPmExtendedCurrentTxQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueTable.setStatus("current")
_CwsPmExtendedCurrentTxQueueEntry_Object = MibTableRow
cwsPmExtendedCurrentTxQueueEntry = _CwsPmExtendedCurrentTxQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1)
)
cwsPmExtendedCurrentTxQueueEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueEntry.setStatus("current")


class _CwsPmExtendedCurrentTxQueueTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentTxQueueTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentTxQueueTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentTxQueueTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueTableSnmpKey = _CwsPmExtendedCurrentTxQueueTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 1),
    _CwsPmExtendedCurrentTxQueueTableSnmpKey_Type()
)
cwsPmExtendedCurrentTxQueueTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentTxQueuePacketDropCountSummary_Type = Counter64
_CwsPmExtendedCurrentTxQueuePacketDropCountSummary_Object = MibTableColumn
cwsPmExtendedCurrentTxQueuePacketDropCountSummary = _CwsPmExtendedCurrentTxQueuePacketDropCountSummary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 2),
    _CwsPmExtendedCurrentTxQueuePacketDropCountSummary_Type()
)
cwsPmExtendedCurrentTxQueuePacketDropCountSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueuePacketDropCountSummary.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ0PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ0PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ0PacketDropCount = _CwsPmExtendedCurrentTxQueueQ0PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 3),
    _CwsPmExtendedCurrentTxQueueQ0PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ0PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ0PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ1PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ1PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ1PacketDropCount = _CwsPmExtendedCurrentTxQueueQ1PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 4),
    _CwsPmExtendedCurrentTxQueueQ1PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ1PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ1PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ2PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ2PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ2PacketDropCount = _CwsPmExtendedCurrentTxQueueQ2PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 5),
    _CwsPmExtendedCurrentTxQueueQ2PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ2PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ2PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ3PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ3PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ3PacketDropCount = _CwsPmExtendedCurrentTxQueueQ3PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 6),
    _CwsPmExtendedCurrentTxQueueQ3PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ3PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ3PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ4PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ4PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ4PacketDropCount = _CwsPmExtendedCurrentTxQueueQ4PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 7),
    _CwsPmExtendedCurrentTxQueueQ4PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ4PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ4PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ5PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ5PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ5PacketDropCount = _CwsPmExtendedCurrentTxQueueQ5PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 8),
    _CwsPmExtendedCurrentTxQueueQ5PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ5PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ5PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ6PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ6PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ6PacketDropCount = _CwsPmExtendedCurrentTxQueueQ6PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 9),
    _CwsPmExtendedCurrentTxQueueQ6PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ6PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ6PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentTxQueueQ7PacketDropCount_Type = Counter64
_CwsPmExtendedCurrentTxQueueQ7PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrentTxQueueQ7PacketDropCount = _CwsPmExtendedCurrentTxQueueQ7PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 16, 1, 10),
    _CwsPmExtendedCurrentTxQueueQ7PacketDropCount_Type()
)
cwsPmExtendedCurrentTxQueueQ7PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentTxQueueQ7PacketDropCount.setStatus("current")
_CwsPmExtendedCurrentMacLayerTable_Object = MibTable
cwsPmExtendedCurrentMacLayerTable = _CwsPmExtendedCurrentMacLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 17)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentMacLayerTable.setStatus("obsolete")
_CwsPmExtendedCurrentMacLayerEntry_Object = MibTableRow
cwsPmExtendedCurrentMacLayerEntry = _CwsPmExtendedCurrentMacLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 17, 1)
)
cwsPmExtendedCurrentMacLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentMacLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentMacLayerEntry.setStatus("obsolete")


class _CwsPmExtendedCurrentMacLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentMacLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentMacLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentMacLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentMacLayerTableSnmpKey = _CwsPmExtendedCurrentMacLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 17, 1, 1),
    _CwsPmExtendedCurrentMacLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrentMacLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentMacLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentMacLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedCurrentMacLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedCurrentMacLayerUnavailableSeconds = _CwsPmExtendedCurrentMacLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 17, 1, 2),
    _CwsPmExtendedCurrentMacLayerUnavailableSeconds_Type()
)
cwsPmExtendedCurrentMacLayerUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentMacLayerUnavailableSeconds.setStatus("obsolete")
_CwsPmExtendedCurrentPcsLayerTable_Object = MibTable
cwsPmExtendedCurrentPcsLayerTable = _CwsPmExtendedCurrentPcsLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 18)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsLayerTable.setStatus("current")
_CwsPmExtendedCurrentPcsLayerEntry_Object = MibTableRow
cwsPmExtendedCurrentPcsLayerEntry = _CwsPmExtendedCurrentPcsLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 18, 1)
)
cwsPmExtendedCurrentPcsLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsLayerEntry.setStatus("current")


class _CwsPmExtendedCurrentPcsLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentPcsLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentPcsLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentPcsLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentPcsLayerTableSnmpKey = _CwsPmExtendedCurrentPcsLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 18, 1, 1),
    _CwsPmExtendedCurrentPcsLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrentPcsLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentPcsLayerErroredSeconds_Type = Counter64
_CwsPmExtendedCurrentPcsLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrentPcsLayerErroredSeconds = _CwsPmExtendedCurrentPcsLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 18, 1, 2),
    _CwsPmExtendedCurrentPcsLayerErroredSeconds_Type()
)
cwsPmExtendedCurrentPcsLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsLayerErroredSeconds.setStatus("current")
_CwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds = _CwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 18, 1, 3),
    _CwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedCurrentPcsLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedCurrentPcsLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedCurrentPcsLayerUnavailableSeconds = _CwsPmExtendedCurrentPcsLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 18, 1, 4),
    _CwsPmExtendedCurrentPcsLayerUnavailableSeconds_Type()
)
cwsPmExtendedCurrentPcsLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsLayerUnavailableSeconds.setStatus("current")
_CwsPmExtendedCurrentPcsSyncHeaderErrorsTable_Object = MibTable
cwsPmExtendedCurrentPcsSyncHeaderErrorsTable = _CwsPmExtendedCurrentPcsSyncHeaderErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 19)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsSyncHeaderErrorsTable.setStatus("current")
_CwsPmExtendedCurrentPcsSyncHeaderErrorsEntry_Object = MibTableRow
cwsPmExtendedCurrentPcsSyncHeaderErrorsEntry = _CwsPmExtendedCurrentPcsSyncHeaderErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 19, 1)
)
cwsPmExtendedCurrentPcsSyncHeaderErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsSyncHeaderErrorsEntry.setStatus("current")


class _CwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey = _CwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 19, 1, 1),
    _CwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey_Type()
)
cwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentPcsSyncHeaderErrorsCount_Type = Counter64
_CwsPmExtendedCurrentPcsSyncHeaderErrorsCount_Object = MibTableColumn
cwsPmExtendedCurrentPcsSyncHeaderErrorsCount = _CwsPmExtendedCurrentPcsSyncHeaderErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 19, 1, 2),
    _CwsPmExtendedCurrentPcsSyncHeaderErrorsCount_Type()
)
cwsPmExtendedCurrentPcsSyncHeaderErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsSyncHeaderErrorsCount.setStatus("current")
_CwsPmExtendedCurrentPcsBlockErrorsTable_Object = MibTable
cwsPmExtendedCurrentPcsBlockErrorsTable = _CwsPmExtendedCurrentPcsBlockErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 20)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsBlockErrorsTable.setStatus("current")
_CwsPmExtendedCurrentPcsBlockErrorsEntry_Object = MibTableRow
cwsPmExtendedCurrentPcsBlockErrorsEntry = _CwsPmExtendedCurrentPcsBlockErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 20, 1)
)
cwsPmExtendedCurrentPcsBlockErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsBlockErrorsEntry.setStatus("current")


class _CwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey = _CwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 20, 1, 1),
    _CwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey_Type()
)
cwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentPcsBlockErrorsCount_Type = Counter64
_CwsPmExtendedCurrentPcsBlockErrorsCount_Object = MibTableColumn
cwsPmExtendedCurrentPcsBlockErrorsCount = _CwsPmExtendedCurrentPcsBlockErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 20, 1, 2),
    _CwsPmExtendedCurrentPcsBlockErrorsCount_Type()
)
cwsPmExtendedCurrentPcsBlockErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsBlockErrorsCount.setStatus("current")
_CwsPmExtendedCurrentPcsMultilaneBipErrorsTable_Object = MibTable
cwsPmExtendedCurrentPcsMultilaneBipErrorsTable = _CwsPmExtendedCurrentPcsMultilaneBipErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 21)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsMultilaneBipErrorsTable.setStatus("current")
_CwsPmExtendedCurrentPcsMultilaneBipErrorsEntry_Object = MibTableRow
cwsPmExtendedCurrentPcsMultilaneBipErrorsEntry = _CwsPmExtendedCurrentPcsMultilaneBipErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 21, 1)
)
cwsPmExtendedCurrentPcsMultilaneBipErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsMultilaneBipErrorsEntry.setStatus("current")


class _CwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey = _CwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 21, 1, 1),
    _CwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey_Type()
)
cwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentPcsMultilaneBipErrorsCount_Type = Counter64
_CwsPmExtendedCurrentPcsMultilaneBipErrorsCount_Object = MibTableColumn
cwsPmExtendedCurrentPcsMultilaneBipErrorsCount = _CwsPmExtendedCurrentPcsMultilaneBipErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 21, 1, 2),
    _CwsPmExtendedCurrentPcsMultilaneBipErrorsCount_Type()
)
cwsPmExtendedCurrentPcsMultilaneBipErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentPcsMultilaneBipErrorsCount.setStatus("current")
_CwsPmExtendedCurrentFecLayerTable_Object = MibTable
cwsPmExtendedCurrentFecLayerTable = _CwsPmExtendedCurrentFecLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 22)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentFecLayerTable.setStatus("current")
_CwsPmExtendedCurrentFecLayerEntry_Object = MibTableRow
cwsPmExtendedCurrentFecLayerEntry = _CwsPmExtendedCurrentFecLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 22, 1)
)
cwsPmExtendedCurrentFecLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentFecLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentFecLayerEntry.setStatus("current")


class _CwsPmExtendedCurrentFecLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentFecLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentFecLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentFecLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentFecLayerTableSnmpKey = _CwsPmExtendedCurrentFecLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 22, 1, 1),
    _CwsPmExtendedCurrentFecLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrentFecLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentFecLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentFecLayerCorrectedBlockCount_Type = Counter64
_CwsPmExtendedCurrentFecLayerCorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedCurrentFecLayerCorrectedBlockCount = _CwsPmExtendedCurrentFecLayerCorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 22, 1, 2),
    _CwsPmExtendedCurrentFecLayerCorrectedBlockCount_Type()
)
cwsPmExtendedCurrentFecLayerCorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentFecLayerCorrectedBlockCount.setStatus("current")
_CwsPmExtendedCurrentFecLayerUncorrectedBlockCount_Type = Counter64
_CwsPmExtendedCurrentFecLayerUncorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedCurrentFecLayerUncorrectedBlockCount = _CwsPmExtendedCurrentFecLayerUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 22, 1, 3),
    _CwsPmExtendedCurrentFecLayerUncorrectedBlockCount_Type()
)
cwsPmExtendedCurrentFecLayerUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentFecLayerUncorrectedBlockCount.setStatus("current")
_CwsPmExtendedCurrentFecLayerSymbolErrorCount_Type = Counter64
_CwsPmExtendedCurrentFecLayerSymbolErrorCount_Object = MibTableColumn
cwsPmExtendedCurrentFecLayerSymbolErrorCount = _CwsPmExtendedCurrentFecLayerSymbolErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 22, 1, 4),
    _CwsPmExtendedCurrentFecLayerSymbolErrorCount_Type()
)
cwsPmExtendedCurrentFecLayerSymbolErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentFecLayerSymbolErrorCount.setStatus("current")
_CwsPmExtendedCurrent24hIdTable_Object = MibTable
cwsPmExtendedCurrent24hIdTable = _CwsPmExtendedCurrent24hIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 23)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hIdTable.setStatus("current")
_CwsPmExtendedCurrent24hIdEntry_Object = MibTableRow
cwsPmExtendedCurrent24hIdEntry = _CwsPmExtendedCurrent24hIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 23, 1)
)
cwsPmExtendedCurrent24hIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hIdEntry.setStatus("current")


class _CwsPmExtendedCurrent24hIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hIdTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hIdTableSnmpKey = _CwsPmExtendedCurrent24hIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 23, 1, 1),
    _CwsPmExtendedCurrent24hIdTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hIdTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hIdBinNumber_Type = Unsigned32
_CwsPmExtendedCurrent24hIdBinNumber_Object = MibTableColumn
cwsPmExtendedCurrent24hIdBinNumber = _CwsPmExtendedCurrent24hIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 23, 1, 2),
    _CwsPmExtendedCurrent24hIdBinNumber_Type()
)
cwsPmExtendedCurrent24hIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hIdBinNumber.setStatus("current")
_CwsPmExtendedCurrent24hIdBinName_Type = StringMaxl32
_CwsPmExtendedCurrent24hIdBinName_Object = MibTableColumn
cwsPmExtendedCurrent24hIdBinName = _CwsPmExtendedCurrent24hIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 23, 1, 3),
    _CwsPmExtendedCurrent24hIdBinName_Type()
)
cwsPmExtendedCurrent24hIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hIdBinName.setStatus("current")
_CwsPmExtendedCurrent24hStateTable_Object = MibTable
cwsPmExtendedCurrent24hStateTable = _CwsPmExtendedCurrent24hStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 24)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStateTable.setStatus("current")
_CwsPmExtendedCurrent24hStateEntry_Object = MibTableRow
cwsPmExtendedCurrent24hStateEntry = _CwsPmExtendedCurrent24hStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 24, 1)
)
cwsPmExtendedCurrent24hStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStateEntry.setStatus("current")


class _CwsPmExtendedCurrent24hStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hStateTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hStateTableSnmpKey = _CwsPmExtendedCurrent24hStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 24, 1, 1),
    _CwsPmExtendedCurrent24hStateTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStateTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hStateStartDateTime_Type = StringMaxl32
_CwsPmExtendedCurrent24hStateStartDateTime_Object = MibTableColumn
cwsPmExtendedCurrent24hStateStartDateTime = _CwsPmExtendedCurrent24hStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 24, 1, 2),
    _CwsPmExtendedCurrent24hStateStartDateTime_Type()
)
cwsPmExtendedCurrent24hStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStateStartDateTime.setStatus("current")
_CwsPmExtendedCurrent24hStateClearedDateTime_Type = StringMaxl32
_CwsPmExtendedCurrent24hStateClearedDateTime_Object = MibTableColumn
cwsPmExtendedCurrent24hStateClearedDateTime = _CwsPmExtendedCurrent24hStateClearedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 24, 1, 3),
    _CwsPmExtendedCurrent24hStateClearedDateTime_Type()
)
cwsPmExtendedCurrent24hStateClearedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStateClearedDateTime.setStatus("current")
_CwsPmExtendedCurrent24hStateState_Type = PmBinState
_CwsPmExtendedCurrent24hStateState_Object = MibTableColumn
cwsPmExtendedCurrent24hStateState = _CwsPmExtendedCurrent24hStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 24, 1, 4),
    _CwsPmExtendedCurrent24hStateState_Type()
)
cwsPmExtendedCurrent24hStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStateState.setStatus("current")
_CwsPmExtendedCurrent24hStatisticsTable_Object = MibTable
cwsPmExtendedCurrent24hStatisticsTable = _CwsPmExtendedCurrent24hStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 25)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStatisticsTable.setStatus("current")
_CwsPmExtendedCurrent24hStatisticsEntry_Object = MibTableRow
cwsPmExtendedCurrent24hStatisticsEntry = _CwsPmExtendedCurrent24hStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 25, 1)
)
cwsPmExtendedCurrent24hStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStatisticsEntry.setStatus("current")


class _CwsPmExtendedCurrent24hStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hStatisticsTableSnmpKey = _CwsPmExtendedCurrent24hStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 25, 1, 1),
    _CwsPmExtendedCurrent24hStatisticsTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStatisticsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hStatisticsFrameErrorRatio_Type = Counter64
_CwsPmExtendedCurrent24hStatisticsFrameErrorRatio_Object = MibTableColumn
cwsPmExtendedCurrent24hStatisticsFrameErrorRatio = _CwsPmExtendedCurrent24hStatisticsFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 25, 1, 2),
    _CwsPmExtendedCurrent24hStatisticsFrameErrorRatio_Type()
)
cwsPmExtendedCurrent24hStatisticsFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hStatisticsFrameErrorRatio.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsTable_Object = MibTable
cwsPmExtendedCurrent24hRxIfCountsTable = _CwsPmExtendedCurrent24hRxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsTable.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsEntry_Object = MibTableRow
cwsPmExtendedCurrent24hRxIfCountsEntry = _CwsPmExtendedCurrent24hRxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1)
)
cwsPmExtendedCurrent24hRxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsEntry.setStatus("current")


class _CwsPmExtendedCurrent24hRxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hRxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hRxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hRxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsTableSnmpKey = _CwsPmExtendedCurrent24hRxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 1),
    _CwsPmExtendedCurrent24hRxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hRxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsBytes_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsBytes = _CwsPmExtendedCurrent24hRxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 2),
    _CwsPmExtendedCurrent24hRxIfCountsBytes_Type()
)
cwsPmExtendedCurrent24hRxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsBytes.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPackets = _CwsPmExtendedCurrent24hRxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 3),
    _CwsPmExtendedCurrent24hRxIfCountsPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets = _CwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 4),
    _CwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsMulticastPackets = _CwsPmExtendedCurrent24hRxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 5),
    _CwsPmExtendedCurrent24hRxIfCountsMulticastPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsBroadcastPackets = _CwsPmExtendedCurrent24hRxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 6),
    _CwsPmExtendedCurrent24hRxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPausePackets = _CwsPmExtendedCurrent24hRxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 7),
    _CwsPmExtendedCurrent24hRxIfCountsPausePackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsUndersizedPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsUndersizedPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsUndersizedPackets = _CwsPmExtendedCurrent24hRxIfCountsUndersizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 8),
    _CwsPmExtendedCurrent24hRxIfCountsUndersizedPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsUndersizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsUndersizedPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsOversizedPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsOversizedPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsOversizedPackets = _CwsPmExtendedCurrent24hRxIfCountsOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 9),
    _CwsPmExtendedCurrent24hRxIfCountsOversizedPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsOversizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsOversizedPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsFragmentPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsFragmentPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsFragmentPackets = _CwsPmExtendedCurrent24hRxIfCountsFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 10),
    _CwsPmExtendedCurrent24hRxIfCountsFragmentPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsFragmentPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsFragmentPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsJabberPackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsJabberPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsJabberPackets = _CwsPmExtendedCurrent24hRxIfCountsJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 11),
    _CwsPmExtendedCurrent24hRxIfCountsJabberPackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsJabberPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsJabberPackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets = _CwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 12),
    _CwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPackets64Octet_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPackets64Octet_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPackets64Octet = _CwsPmExtendedCurrent24hRxIfCountsPackets64Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 13),
    _CwsPmExtendedCurrent24hRxIfCountsPackets64Octet_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPackets64Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPackets64Octet.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPackets65127Octet_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPackets65127Octet_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPackets65127Octet = _CwsPmExtendedCurrent24hRxIfCountsPackets65127Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 14),
    _CwsPmExtendedCurrent24hRxIfCountsPackets65127Octet_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPackets65127Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPackets65127Octet.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPackets128255Octet_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPackets128255Octet_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPackets128255Octet = _CwsPmExtendedCurrent24hRxIfCountsPackets128255Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 15),
    _CwsPmExtendedCurrent24hRxIfCountsPackets128255Octet_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPackets128255Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPackets128255Octet.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPackets256511Octet_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPackets256511Octet_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPackets256511Octet = _CwsPmExtendedCurrent24hRxIfCountsPackets256511Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 16),
    _CwsPmExtendedCurrent24hRxIfCountsPackets256511Octet_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPackets256511Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPackets256511Octet.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet = _CwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 17),
    _CwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet_Type = Counter64
_CwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet = _CwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 18),
    _CwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet_Type()
)
cwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet.setStatus("current")
_CwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization = _CwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 26, 1, 19),
    _CwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsTable_Object = MibTable
cwsPmExtendedCurrent24hTxIfCountsTable = _CwsPmExtendedCurrent24hTxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsTable.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsEntry_Object = MibTableRow
cwsPmExtendedCurrent24hTxIfCountsEntry = _CwsPmExtendedCurrent24hTxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1)
)
cwsPmExtendedCurrent24hTxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsEntry.setStatus("current")


class _CwsPmExtendedCurrent24hTxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hTxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hTxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hTxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsTableSnmpKey = _CwsPmExtendedCurrent24hTxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 1),
    _CwsPmExtendedCurrent24hTxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hTxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsBytes_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsBytes = _CwsPmExtendedCurrent24hTxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 2),
    _CwsPmExtendedCurrent24hTxIfCountsBytes_Type()
)
cwsPmExtendedCurrent24hTxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsBytes.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsPackets = _CwsPmExtendedCurrent24hTxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 3),
    _CwsPmExtendedCurrent24hTxIfCountsPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets = _CwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 4),
    _CwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsMulticastPackets = _CwsPmExtendedCurrent24hTxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 5),
    _CwsPmExtendedCurrent24hTxIfCountsMulticastPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsBroadcastPackets = _CwsPmExtendedCurrent24hTxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 6),
    _CwsPmExtendedCurrent24hTxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsPausePackets = _CwsPmExtendedCurrent24hTxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 7),
    _CwsPmExtendedCurrent24hTxIfCountsPausePackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets = _CwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 8),
    _CwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsGiantPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsGiantPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsGiantPackets = _CwsPmExtendedCurrent24hTxIfCountsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 9),
    _CwsPmExtendedCurrent24hTxIfCountsGiantPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsGiantPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsGiantPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsUnderrunPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsUnderrunPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsUnderrunPackets = _CwsPmExtendedCurrent24hTxIfCountsUnderrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 10),
    _CwsPmExtendedCurrent24hTxIfCountsUnderrunPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsUnderrunPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsUnderrunPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets = _CwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 11),
    _CwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets = _CwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 12),
    _CwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization = _CwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 27, 1, 13),
    _CwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueTable_Object = MibTable
cwsPmExtendedCurrent24hTxQueueTable = _CwsPmExtendedCurrent24hTxQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueTable.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueEntry_Object = MibTableRow
cwsPmExtendedCurrent24hTxQueueEntry = _CwsPmExtendedCurrent24hTxQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1)
)
cwsPmExtendedCurrent24hTxQueueEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueEntry.setStatus("current")


class _CwsPmExtendedCurrent24hTxQueueTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hTxQueueTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hTxQueueTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hTxQueueTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueTableSnmpKey = _CwsPmExtendedCurrent24hTxQueueTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 1),
    _CwsPmExtendedCurrent24hTxQueueTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hTxQueueTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hTxQueuePacketDropCountSummary_Type = Counter64
_CwsPmExtendedCurrent24hTxQueuePacketDropCountSummary_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueuePacketDropCountSummary = _CwsPmExtendedCurrent24hTxQueuePacketDropCountSummary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 2),
    _CwsPmExtendedCurrent24hTxQueuePacketDropCountSummary_Type()
)
cwsPmExtendedCurrent24hTxQueuePacketDropCountSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueuePacketDropCountSummary.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ0PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ0PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ0PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ0PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 3),
    _CwsPmExtendedCurrent24hTxQueueQ0PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ0PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ0PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ1PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ1PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ1PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ1PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 4),
    _CwsPmExtendedCurrent24hTxQueueQ1PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ1PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ1PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ2PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ2PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ2PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ2PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 5),
    _CwsPmExtendedCurrent24hTxQueueQ2PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ2PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ2PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ3PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ3PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ3PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ3PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 6),
    _CwsPmExtendedCurrent24hTxQueueQ3PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ3PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ3PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ4PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ4PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ4PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ4PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 7),
    _CwsPmExtendedCurrent24hTxQueueQ4PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ4PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ4PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ5PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ5PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ5PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ5PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 8),
    _CwsPmExtendedCurrent24hTxQueueQ5PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ5PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ5PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ6PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ6PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ6PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ6PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 9),
    _CwsPmExtendedCurrent24hTxQueueQ6PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ6PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ6PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hTxQueueQ7PacketDropCount_Type = Counter64
_CwsPmExtendedCurrent24hTxQueueQ7PacketDropCount_Object = MibTableColumn
cwsPmExtendedCurrent24hTxQueueQ7PacketDropCount = _CwsPmExtendedCurrent24hTxQueueQ7PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 28, 1, 10),
    _CwsPmExtendedCurrent24hTxQueueQ7PacketDropCount_Type()
)
cwsPmExtendedCurrent24hTxQueueQ7PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hTxQueueQ7PacketDropCount.setStatus("current")
_CwsPmExtendedCurrent24hMacLayerTable_Object = MibTable
cwsPmExtendedCurrent24hMacLayerTable = _CwsPmExtendedCurrent24hMacLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 29)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hMacLayerTable.setStatus("obsolete")
_CwsPmExtendedCurrent24hMacLayerEntry_Object = MibTableRow
cwsPmExtendedCurrent24hMacLayerEntry = _CwsPmExtendedCurrent24hMacLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 29, 1)
)
cwsPmExtendedCurrent24hMacLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hMacLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hMacLayerEntry.setStatus("obsolete")


class _CwsPmExtendedCurrent24hMacLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hMacLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hMacLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hMacLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hMacLayerTableSnmpKey = _CwsPmExtendedCurrent24hMacLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 29, 1, 1),
    _CwsPmExtendedCurrent24hMacLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hMacLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hMacLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hMacLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedCurrent24hMacLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedCurrent24hMacLayerUnavailableSeconds = _CwsPmExtendedCurrent24hMacLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 29, 1, 2),
    _CwsPmExtendedCurrent24hMacLayerUnavailableSeconds_Type()
)
cwsPmExtendedCurrent24hMacLayerUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hMacLayerUnavailableSeconds.setStatus("obsolete")
_CwsPmExtendedCurrent24hPcsLayerTable_Object = MibTable
cwsPmExtendedCurrent24hPcsLayerTable = _CwsPmExtendedCurrent24hPcsLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 30)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsLayerTable.setStatus("current")
_CwsPmExtendedCurrent24hPcsLayerEntry_Object = MibTableRow
cwsPmExtendedCurrent24hPcsLayerEntry = _CwsPmExtendedCurrent24hPcsLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 30, 1)
)
cwsPmExtendedCurrent24hPcsLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsLayerEntry.setStatus("current")


class _CwsPmExtendedCurrent24hPcsLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hPcsLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hPcsLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hPcsLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsLayerTableSnmpKey = _CwsPmExtendedCurrent24hPcsLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 30, 1, 1),
    _CwsPmExtendedCurrent24hPcsLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hPcsLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hPcsLayerErroredSeconds_Type = Counter64
_CwsPmExtendedCurrent24hPcsLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsLayerErroredSeconds = _CwsPmExtendedCurrent24hPcsLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 30, 1, 2),
    _CwsPmExtendedCurrent24hPcsLayerErroredSeconds_Type()
)
cwsPmExtendedCurrent24hPcsLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsLayerErroredSeconds.setStatus("current")
_CwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds = _CwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 30, 1, 3),
    _CwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedCurrent24hPcsLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedCurrent24hPcsLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsLayerUnavailableSeconds = _CwsPmExtendedCurrent24hPcsLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 30, 1, 4),
    _CwsPmExtendedCurrent24hPcsLayerUnavailableSeconds_Type()
)
cwsPmExtendedCurrent24hPcsLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsLayerUnavailableSeconds.setStatus("current")
_CwsPmExtendedCurrent24hPcsSyncHeaderErrorsTable_Object = MibTable
cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTable = _CwsPmExtendedCurrent24hPcsSyncHeaderErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 31)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTable.setStatus("current")
_CwsPmExtendedCurrent24hPcsSyncHeaderErrorsEntry_Object = MibTableRow
cwsPmExtendedCurrent24hPcsSyncHeaderErrorsEntry = _CwsPmExtendedCurrent24hPcsSyncHeaderErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 31, 1)
)
cwsPmExtendedCurrent24hPcsSyncHeaderErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsSyncHeaderErrorsEntry.setStatus("current")


class _CwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey = _CwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 31, 1, 1),
    _CwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount_Type = Counter64
_CwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount = _CwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 31, 1, 2),
    _CwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount_Type()
)
cwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount.setStatus("current")
_CwsPmExtendedCurrent24hPcsBlockErrorsTable_Object = MibTable
cwsPmExtendedCurrent24hPcsBlockErrorsTable = _CwsPmExtendedCurrent24hPcsBlockErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 32)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsBlockErrorsTable.setStatus("current")
_CwsPmExtendedCurrent24hPcsBlockErrorsEntry_Object = MibTableRow
cwsPmExtendedCurrent24hPcsBlockErrorsEntry = _CwsPmExtendedCurrent24hPcsBlockErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 32, 1)
)
cwsPmExtendedCurrent24hPcsBlockErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsBlockErrorsEntry.setStatus("current")


class _CwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey = _CwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 32, 1, 1),
    _CwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hPcsBlockErrorsCount_Type = Counter64
_CwsPmExtendedCurrent24hPcsBlockErrorsCount_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsBlockErrorsCount = _CwsPmExtendedCurrent24hPcsBlockErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 32, 1, 2),
    _CwsPmExtendedCurrent24hPcsBlockErrorsCount_Type()
)
cwsPmExtendedCurrent24hPcsBlockErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsBlockErrorsCount.setStatus("current")
_CwsPmExtendedCurrent24hPcsMultilaneBipErrorsTable_Object = MibTable
cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTable = _CwsPmExtendedCurrent24hPcsMultilaneBipErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 33)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTable.setStatus("current")
_CwsPmExtendedCurrent24hPcsMultilaneBipErrorsEntry_Object = MibTableRow
cwsPmExtendedCurrent24hPcsMultilaneBipErrorsEntry = _CwsPmExtendedCurrent24hPcsMultilaneBipErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 33, 1)
)
cwsPmExtendedCurrent24hPcsMultilaneBipErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsMultilaneBipErrorsEntry.setStatus("current")


class _CwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey = _CwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 33, 1, 1),
    _CwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount_Type = Counter64
_CwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount_Object = MibTableColumn
cwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount = _CwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 33, 1, 2),
    _CwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount_Type()
)
cwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount.setStatus("current")
_CwsPmExtendedCurrent24hFecLayerTable_Object = MibTable
cwsPmExtendedCurrent24hFecLayerTable = _CwsPmExtendedCurrent24hFecLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 34)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hFecLayerTable.setStatus("current")
_CwsPmExtendedCurrent24hFecLayerEntry_Object = MibTableRow
cwsPmExtendedCurrent24hFecLayerEntry = _CwsPmExtendedCurrent24hFecLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 34, 1)
)
cwsPmExtendedCurrent24hFecLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hFecLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hFecLayerEntry.setStatus("current")


class _CwsPmExtendedCurrent24hFecLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hFecLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hFecLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hFecLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hFecLayerTableSnmpKey = _CwsPmExtendedCurrent24hFecLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 34, 1, 1),
    _CwsPmExtendedCurrent24hFecLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hFecLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hFecLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hFecLayerCorrectedBlockCount_Type = Counter64
_CwsPmExtendedCurrent24hFecLayerCorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedCurrent24hFecLayerCorrectedBlockCount = _CwsPmExtendedCurrent24hFecLayerCorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 34, 1, 2),
    _CwsPmExtendedCurrent24hFecLayerCorrectedBlockCount_Type()
)
cwsPmExtendedCurrent24hFecLayerCorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hFecLayerCorrectedBlockCount.setStatus("current")
_CwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount_Type = Counter64
_CwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount = _CwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 34, 1, 3),
    _CwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount_Type()
)
cwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount.setStatus("current")
_CwsPmExtendedCurrent24hFecLayerSymbolErrorCount_Type = Counter64
_CwsPmExtendedCurrent24hFecLayerSymbolErrorCount_Object = MibTableColumn
cwsPmExtendedCurrent24hFecLayerSymbolErrorCount = _CwsPmExtendedCurrent24hFecLayerSymbolErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 34, 1, 4),
    _CwsPmExtendedCurrent24hFecLayerSymbolErrorCount_Type()
)
cwsPmExtendedCurrent24hFecLayerSymbolErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hFecLayerSymbolErrorCount.setStatus("current")
_CwsPmBinsTable_Object = MibTable
cwsPmBinsTable = _CwsPmBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 35)
)
if mibBuilder.loadTexts:
    cwsPmBinsTable.setStatus("current")
_CwsPmBinsEntry_Object = MibTableRow
cwsPmBinsEntry = _CwsPmBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 35, 1)
)
cwsPmBinsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
)
if mibBuilder.loadTexts:
    cwsPmBinsEntry.setStatus("current")


class _CwsPmBinsBinNumber_Type(Integer32):
    """Custom type cwsPmBinsBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBinsBinNumber_Type.__name__ = "Integer32"
_CwsPmBinsBinNumber_Object = MibTableColumn
cwsPmBinsBinNumber = _CwsPmBinsBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 35, 1, 1),
    _CwsPmBinsBinNumber_Type()
)
cwsPmBinsBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBinsBinNumber.setStatus("current")
_CwsPmExtendedHistoryStateTable_Object = MibTable
cwsPmExtendedHistoryStateTable = _CwsPmExtendedHistoryStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 36)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStateTable.setStatus("current")
_CwsPmExtendedHistoryStateEntry_Object = MibTableRow
cwsPmExtendedHistoryStateEntry = _CwsPmExtendedHistoryStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 36, 1)
)
cwsPmExtendedHistoryStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStateEntry.setStatus("current")


class _CwsPmExtendedHistoryStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryStateTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryStateTableSnmpKey = _CwsPmExtendedHistoryStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 36, 1, 1),
    _CwsPmExtendedHistoryStateTableSnmpKey_Type()
)
cwsPmExtendedHistoryStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStateTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryStateStartDateTime_Type = StringMaxl32
_CwsPmExtendedHistoryStateStartDateTime_Object = MibTableColumn
cwsPmExtendedHistoryStateStartDateTime = _CwsPmExtendedHistoryStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 36, 1, 2),
    _CwsPmExtendedHistoryStateStartDateTime_Type()
)
cwsPmExtendedHistoryStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStateStartDateTime.setStatus("current")
_CwsPmExtendedHistoryStateEndDateTime_Type = StringMaxl32
_CwsPmExtendedHistoryStateEndDateTime_Object = MibTableColumn
cwsPmExtendedHistoryStateEndDateTime = _CwsPmExtendedHistoryStateEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 36, 1, 3),
    _CwsPmExtendedHistoryStateEndDateTime_Type()
)
cwsPmExtendedHistoryStateEndDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStateEndDateTime.setStatus("current")
_CwsPmExtendedHistoryStateState_Type = PmBinState
_CwsPmExtendedHistoryStateState_Object = MibTableColumn
cwsPmExtendedHistoryStateState = _CwsPmExtendedHistoryStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 36, 1, 4),
    _CwsPmExtendedHistoryStateState_Type()
)
cwsPmExtendedHistoryStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStateState.setStatus("current")
_CwsPmExtendedHistoryStatisticsTable_Object = MibTable
cwsPmExtendedHistoryStatisticsTable = _CwsPmExtendedHistoryStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 37)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStatisticsTable.setStatus("current")
_CwsPmExtendedHistoryStatisticsEntry_Object = MibTableRow
cwsPmExtendedHistoryStatisticsEntry = _CwsPmExtendedHistoryStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 37, 1)
)
cwsPmExtendedHistoryStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStatisticsEntry.setStatus("current")


class _CwsPmExtendedHistoryStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryStatisticsTableSnmpKey = _CwsPmExtendedHistoryStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 37, 1, 1),
    _CwsPmExtendedHistoryStatisticsTableSnmpKey_Type()
)
cwsPmExtendedHistoryStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStatisticsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryStatisticsFrameErrorRatio_Type = Counter64
_CwsPmExtendedHistoryStatisticsFrameErrorRatio_Object = MibTableColumn
cwsPmExtendedHistoryStatisticsFrameErrorRatio = _CwsPmExtendedHistoryStatisticsFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 37, 1, 2),
    _CwsPmExtendedHistoryStatisticsFrameErrorRatio_Type()
)
cwsPmExtendedHistoryStatisticsFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryStatisticsFrameErrorRatio.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsTable_Object = MibTable
cwsPmExtendedHistoryRxIfCountsTable = _CwsPmExtendedHistoryRxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsTable.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsEntry_Object = MibTableRow
cwsPmExtendedHistoryRxIfCountsEntry = _CwsPmExtendedHistoryRxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1)
)
cwsPmExtendedHistoryRxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsEntry.setStatus("current")


class _CwsPmExtendedHistoryRxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryRxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryRxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryRxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsTableSnmpKey = _CwsPmExtendedHistoryRxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 1),
    _CwsPmExtendedHistoryRxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedHistoryRxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsBytes_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsBytes = _CwsPmExtendedHistoryRxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 2),
    _CwsPmExtendedHistoryRxIfCountsBytes_Type()
)
cwsPmExtendedHistoryRxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsBytes.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPackets = _CwsPmExtendedHistoryRxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 3),
    _CwsPmExtendedHistoryRxIfCountsPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsCrcErroredPackets = _CwsPmExtendedHistoryRxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 4),
    _CwsPmExtendedHistoryRxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsMulticastPackets = _CwsPmExtendedHistoryRxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 5),
    _CwsPmExtendedHistoryRxIfCountsMulticastPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsBroadcastPackets = _CwsPmExtendedHistoryRxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 6),
    _CwsPmExtendedHistoryRxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPausePackets = _CwsPmExtendedHistoryRxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 7),
    _CwsPmExtendedHistoryRxIfCountsPausePackets_Type()
)
cwsPmExtendedHistoryRxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsUndersizedPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsUndersizedPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsUndersizedPackets = _CwsPmExtendedHistoryRxIfCountsUndersizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 8),
    _CwsPmExtendedHistoryRxIfCountsUndersizedPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsUndersizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsUndersizedPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsOversizedPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsOversizedPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsOversizedPackets = _CwsPmExtendedHistoryRxIfCountsOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 9),
    _CwsPmExtendedHistoryRxIfCountsOversizedPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsOversizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsOversizedPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsFragmentPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsFragmentPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsFragmentPackets = _CwsPmExtendedHistoryRxIfCountsFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 10),
    _CwsPmExtendedHistoryRxIfCountsFragmentPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsFragmentPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsFragmentPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsJabberPackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsJabberPackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsJabberPackets = _CwsPmExtendedHistoryRxIfCountsJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 11),
    _CwsPmExtendedHistoryRxIfCountsJabberPackets_Type()
)
cwsPmExtendedHistoryRxIfCountsJabberPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsJabberPackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsLengthOutRangePackets = _CwsPmExtendedHistoryRxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 12),
    _CwsPmExtendedHistoryRxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedHistoryRxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPackets64Octet_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPackets64Octet_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPackets64Octet = _CwsPmExtendedHistoryRxIfCountsPackets64Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 13),
    _CwsPmExtendedHistoryRxIfCountsPackets64Octet_Type()
)
cwsPmExtendedHistoryRxIfCountsPackets64Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPackets64Octet.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPackets65127Octet_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPackets65127Octet_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPackets65127Octet = _CwsPmExtendedHistoryRxIfCountsPackets65127Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 14),
    _CwsPmExtendedHistoryRxIfCountsPackets65127Octet_Type()
)
cwsPmExtendedHistoryRxIfCountsPackets65127Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPackets65127Octet.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPackets128255Octet_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPackets128255Octet_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPackets128255Octet = _CwsPmExtendedHistoryRxIfCountsPackets128255Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 15),
    _CwsPmExtendedHistoryRxIfCountsPackets128255Octet_Type()
)
cwsPmExtendedHistoryRxIfCountsPackets128255Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPackets128255Octet.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPackets256511Octet_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPackets256511Octet_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPackets256511Octet = _CwsPmExtendedHistoryRxIfCountsPackets256511Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 16),
    _CwsPmExtendedHistoryRxIfCountsPackets256511Octet_Type()
)
cwsPmExtendedHistoryRxIfCountsPackets256511Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPackets256511Octet.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPackets5121023Octet_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPackets5121023Octet_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPackets5121023Octet = _CwsPmExtendedHistoryRxIfCountsPackets5121023Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 17),
    _CwsPmExtendedHistoryRxIfCountsPackets5121023Octet_Type()
)
cwsPmExtendedHistoryRxIfCountsPackets5121023Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPackets5121023Octet.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsPackets10241518Octet_Type = Counter64
_CwsPmExtendedHistoryRxIfCountsPackets10241518Octet_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsPackets10241518Octet = _CwsPmExtendedHistoryRxIfCountsPackets10241518Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 18),
    _CwsPmExtendedHistoryRxIfCountsPackets10241518Octet_Type()
)
cwsPmExtendedHistoryRxIfCountsPackets10241518Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsPackets10241518Octet.setStatus("current")
_CwsPmExtendedHistoryRxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedHistoryRxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedHistoryRxIfCountsAverageLinkUtilization = _CwsPmExtendedHistoryRxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 38, 1, 19),
    _CwsPmExtendedHistoryRxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedHistoryRxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryRxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsTable_Object = MibTable
cwsPmExtendedHistoryTxIfCountsTable = _CwsPmExtendedHistoryTxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsTable.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsEntry_Object = MibTableRow
cwsPmExtendedHistoryTxIfCountsEntry = _CwsPmExtendedHistoryTxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1)
)
cwsPmExtendedHistoryTxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsEntry.setStatus("current")


class _CwsPmExtendedHistoryTxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryTxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryTxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryTxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsTableSnmpKey = _CwsPmExtendedHistoryTxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 1),
    _CwsPmExtendedHistoryTxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedHistoryTxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsBytes_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsBytes = _CwsPmExtendedHistoryTxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 2),
    _CwsPmExtendedHistoryTxIfCountsBytes_Type()
)
cwsPmExtendedHistoryTxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsBytes.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsPackets = _CwsPmExtendedHistoryTxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 3),
    _CwsPmExtendedHistoryTxIfCountsPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsCrcErroredPackets = _CwsPmExtendedHistoryTxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 4),
    _CwsPmExtendedHistoryTxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsMulticastPackets = _CwsPmExtendedHistoryTxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 5),
    _CwsPmExtendedHistoryTxIfCountsMulticastPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsBroadcastPackets = _CwsPmExtendedHistoryTxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 6),
    _CwsPmExtendedHistoryTxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsPausePackets = _CwsPmExtendedHistoryTxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 7),
    _CwsPmExtendedHistoryTxIfCountsPausePackets_Type()
)
cwsPmExtendedHistoryTxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets = _CwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 8),
    _CwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsGiantPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsGiantPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsGiantPackets = _CwsPmExtendedHistoryTxIfCountsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 9),
    _CwsPmExtendedHistoryTxIfCountsGiantPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsGiantPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsGiantPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsUnderrunPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsUnderrunPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsUnderrunPackets = _CwsPmExtendedHistoryTxIfCountsUnderrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 10),
    _CwsPmExtendedHistoryTxIfCountsUnderrunPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsUnderrunPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsUnderrunPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets = _CwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 11),
    _CwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets_Type()
)
cwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedHistoryTxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsLengthOutRangePackets = _CwsPmExtendedHistoryTxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 12),
    _CwsPmExtendedHistoryTxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedHistoryTxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedHistoryTxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedHistoryTxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedHistoryTxIfCountsAverageLinkUtilization = _CwsPmExtendedHistoryTxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 39, 1, 13),
    _CwsPmExtendedHistoryTxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedHistoryTxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryTxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmCurrentBinTxQueueTable_Object = MibTable
cwsPmCurrentBinTxQueueTable = _CwsPmCurrentBinTxQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40)
)
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueTable.setStatus("current")
_CwsPmCurrentBinTxQueueEntry_Object = MibTableRow
cwsPmCurrentBinTxQueueEntry = _CwsPmCurrentBinTxQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1)
)
cwsPmCurrentBinTxQueueEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueEntry.setStatus("current")


class _CwsPmCurrentBinTxQueueTableSnmpKey_Type(Integer32):
    """Custom type cwsPmCurrentBinTxQueueTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmCurrentBinTxQueueTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmCurrentBinTxQueueTableSnmpKey_Object = MibTableColumn
cwsPmCurrentBinTxQueueTableSnmpKey = _CwsPmCurrentBinTxQueueTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 1),
    _CwsPmCurrentBinTxQueueTableSnmpKey_Type()
)
cwsPmCurrentBinTxQueueTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueTableSnmpKey.setStatus("current")
_CwsPmCurrentBinTxQueuePacketDropCountSummary_Type = Counter64
_CwsPmCurrentBinTxQueuePacketDropCountSummary_Object = MibTableColumn
cwsPmCurrentBinTxQueuePacketDropCountSummary = _CwsPmCurrentBinTxQueuePacketDropCountSummary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 2),
    _CwsPmCurrentBinTxQueuePacketDropCountSummary_Type()
)
cwsPmCurrentBinTxQueuePacketDropCountSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueuePacketDropCountSummary.setStatus("current")
_CwsPmCurrentBinTxQueueQ0PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ0PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ0PacketDropCount = _CwsPmCurrentBinTxQueueQ0PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 3),
    _CwsPmCurrentBinTxQueueQ0PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ0PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ0PacketDropCount.setStatus("current")
_CwsPmCurrentBinTxQueueQ1PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ1PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ1PacketDropCount = _CwsPmCurrentBinTxQueueQ1PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 4),
    _CwsPmCurrentBinTxQueueQ1PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ1PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ1PacketDropCount.setStatus("current")
_CwsPmCurrentBinTxQueueQ2PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ2PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ2PacketDropCount = _CwsPmCurrentBinTxQueueQ2PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 5),
    _CwsPmCurrentBinTxQueueQ2PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ2PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ2PacketDropCount.setStatus("current")
_CwsPmCurrentBinTxQueueQ3PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ3PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ3PacketDropCount = _CwsPmCurrentBinTxQueueQ3PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 6),
    _CwsPmCurrentBinTxQueueQ3PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ3PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ3PacketDropCount.setStatus("current")
_CwsPmCurrentBinTxQueueQ4PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ4PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ4PacketDropCount = _CwsPmCurrentBinTxQueueQ4PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 7),
    _CwsPmCurrentBinTxQueueQ4PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ4PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ4PacketDropCount.setStatus("current")
_CwsPmCurrentBinTxQueueQ5PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ5PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ5PacketDropCount = _CwsPmCurrentBinTxQueueQ5PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 8),
    _CwsPmCurrentBinTxQueueQ5PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ5PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ5PacketDropCount.setStatus("current")
_CwsPmCurrentBinTxQueueQ6PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ6PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ6PacketDropCount = _CwsPmCurrentBinTxQueueQ6PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 9),
    _CwsPmCurrentBinTxQueueQ6PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ6PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ6PacketDropCount.setStatus("current")
_CwsPmCurrentBinTxQueueQ7PacketDropCount_Type = Counter64
_CwsPmCurrentBinTxQueueQ7PacketDropCount_Object = MibTableColumn
cwsPmCurrentBinTxQueueQ7PacketDropCount = _CwsPmCurrentBinTxQueueQ7PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 40, 1, 10),
    _CwsPmCurrentBinTxQueueQ7PacketDropCount_Type()
)
cwsPmCurrentBinTxQueueQ7PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmCurrentBinTxQueueQ7PacketDropCount.setStatus("current")
_CwsPmExtendedHistoryMacLayerTable_Object = MibTable
cwsPmExtendedHistoryMacLayerTable = _CwsPmExtendedHistoryMacLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 41)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryMacLayerTable.setStatus("obsolete")
_CwsPmExtendedHistoryMacLayerEntry_Object = MibTableRow
cwsPmExtendedHistoryMacLayerEntry = _CwsPmExtendedHistoryMacLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 41, 1)
)
cwsPmExtendedHistoryMacLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryMacLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryMacLayerEntry.setStatus("obsolete")


class _CwsPmExtendedHistoryMacLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryMacLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryMacLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryMacLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryMacLayerTableSnmpKey = _CwsPmExtendedHistoryMacLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 41, 1, 1),
    _CwsPmExtendedHistoryMacLayerTableSnmpKey_Type()
)
cwsPmExtendedHistoryMacLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryMacLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryMacLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedHistoryMacLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedHistoryMacLayerUnavailableSeconds = _CwsPmExtendedHistoryMacLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 41, 1, 2),
    _CwsPmExtendedHistoryMacLayerUnavailableSeconds_Type()
)
cwsPmExtendedHistoryMacLayerUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryMacLayerUnavailableSeconds.setStatus("obsolete")
_CwsPmExtendedHistoryPcsLayerTable_Object = MibTable
cwsPmExtendedHistoryPcsLayerTable = _CwsPmExtendedHistoryPcsLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 42)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsLayerTable.setStatus("current")
_CwsPmExtendedHistoryPcsLayerEntry_Object = MibTableRow
cwsPmExtendedHistoryPcsLayerEntry = _CwsPmExtendedHistoryPcsLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 42, 1)
)
cwsPmExtendedHistoryPcsLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsLayerEntry.setStatus("current")


class _CwsPmExtendedHistoryPcsLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryPcsLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryPcsLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryPcsLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryPcsLayerTableSnmpKey = _CwsPmExtendedHistoryPcsLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 42, 1, 1),
    _CwsPmExtendedHistoryPcsLayerTableSnmpKey_Type()
)
cwsPmExtendedHistoryPcsLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryPcsLayerErroredSeconds_Type = Counter64
_CwsPmExtendedHistoryPcsLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistoryPcsLayerErroredSeconds = _CwsPmExtendedHistoryPcsLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 42, 1, 2),
    _CwsPmExtendedHistoryPcsLayerErroredSeconds_Type()
)
cwsPmExtendedHistoryPcsLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsLayerErroredSeconds.setStatus("current")
_CwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds = _CwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 42, 1, 3),
    _CwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedHistoryPcsLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedHistoryPcsLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedHistoryPcsLayerUnavailableSeconds = _CwsPmExtendedHistoryPcsLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 42, 1, 4),
    _CwsPmExtendedHistoryPcsLayerUnavailableSeconds_Type()
)
cwsPmExtendedHistoryPcsLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsLayerUnavailableSeconds.setStatus("current")
_CwsPmExtendedHistoryPcsSyncHeaderErrorsTable_Object = MibTable
cwsPmExtendedHistoryPcsSyncHeaderErrorsTable = _CwsPmExtendedHistoryPcsSyncHeaderErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 43)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsSyncHeaderErrorsTable.setStatus("current")
_CwsPmExtendedHistoryPcsSyncHeaderErrorsEntry_Object = MibTableRow
cwsPmExtendedHistoryPcsSyncHeaderErrorsEntry = _CwsPmExtendedHistoryPcsSyncHeaderErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 43, 1)
)
cwsPmExtendedHistoryPcsSyncHeaderErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsSyncHeaderErrorsEntry.setStatus("current")


class _CwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey = _CwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 43, 1, 1),
    _CwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey_Type()
)
cwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryPcsSyncHeaderErrorsCount_Type = Counter64
_CwsPmExtendedHistoryPcsSyncHeaderErrorsCount_Object = MibTableColumn
cwsPmExtendedHistoryPcsSyncHeaderErrorsCount = _CwsPmExtendedHistoryPcsSyncHeaderErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 43, 1, 2),
    _CwsPmExtendedHistoryPcsSyncHeaderErrorsCount_Type()
)
cwsPmExtendedHistoryPcsSyncHeaderErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsSyncHeaderErrorsCount.setStatus("current")
_CwsPmExtendedHistoryPcsBlockErrorsTable_Object = MibTable
cwsPmExtendedHistoryPcsBlockErrorsTable = _CwsPmExtendedHistoryPcsBlockErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 44)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsBlockErrorsTable.setStatus("current")
_CwsPmExtendedHistoryPcsBlockErrorsEntry_Object = MibTableRow
cwsPmExtendedHistoryPcsBlockErrorsEntry = _CwsPmExtendedHistoryPcsBlockErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 44, 1)
)
cwsPmExtendedHistoryPcsBlockErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsBlockErrorsEntry.setStatus("current")


class _CwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey = _CwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 44, 1, 1),
    _CwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey_Type()
)
cwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryPcsBlockErrorsCount_Type = Counter64
_CwsPmExtendedHistoryPcsBlockErrorsCount_Object = MibTableColumn
cwsPmExtendedHistoryPcsBlockErrorsCount = _CwsPmExtendedHistoryPcsBlockErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 44, 1, 2),
    _CwsPmExtendedHistoryPcsBlockErrorsCount_Type()
)
cwsPmExtendedHistoryPcsBlockErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsBlockErrorsCount.setStatus("current")
_CwsPmExtendedHistoryPcsMultilaneBipErrorsTable_Object = MibTable
cwsPmExtendedHistoryPcsMultilaneBipErrorsTable = _CwsPmExtendedHistoryPcsMultilaneBipErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 45)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsMultilaneBipErrorsTable.setStatus("current")
_CwsPmExtendedHistoryPcsMultilaneBipErrorsEntry_Object = MibTableRow
cwsPmExtendedHistoryPcsMultilaneBipErrorsEntry = _CwsPmExtendedHistoryPcsMultilaneBipErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 45, 1)
)
cwsPmExtendedHistoryPcsMultilaneBipErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsMultilaneBipErrorsEntry.setStatus("current")


class _CwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey = _CwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 45, 1, 1),
    _CwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey_Type()
)
cwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryPcsMultilaneBipErrorsCount_Type = Counter64
_CwsPmExtendedHistoryPcsMultilaneBipErrorsCount_Object = MibTableColumn
cwsPmExtendedHistoryPcsMultilaneBipErrorsCount = _CwsPmExtendedHistoryPcsMultilaneBipErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 45, 1, 2),
    _CwsPmExtendedHistoryPcsMultilaneBipErrorsCount_Type()
)
cwsPmExtendedHistoryPcsMultilaneBipErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryPcsMultilaneBipErrorsCount.setStatus("current")
_CwsPmExtendedHistoryFecLayerTable_Object = MibTable
cwsPmExtendedHistoryFecLayerTable = _CwsPmExtendedHistoryFecLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 46)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryFecLayerTable.setStatus("current")
_CwsPmExtendedHistoryFecLayerEntry_Object = MibTableRow
cwsPmExtendedHistoryFecLayerEntry = _CwsPmExtendedHistoryFecLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 46, 1)
)
cwsPmExtendedHistoryFecLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryFecLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryFecLayerEntry.setStatus("current")


class _CwsPmExtendedHistoryFecLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryFecLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryFecLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryFecLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryFecLayerTableSnmpKey = _CwsPmExtendedHistoryFecLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 46, 1, 1),
    _CwsPmExtendedHistoryFecLayerTableSnmpKey_Type()
)
cwsPmExtendedHistoryFecLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryFecLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryFecLayerCorrectedBlockCount_Type = Counter64
_CwsPmExtendedHistoryFecLayerCorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedHistoryFecLayerCorrectedBlockCount = _CwsPmExtendedHistoryFecLayerCorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 46, 1, 2),
    _CwsPmExtendedHistoryFecLayerCorrectedBlockCount_Type()
)
cwsPmExtendedHistoryFecLayerCorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryFecLayerCorrectedBlockCount.setStatus("current")
_CwsPmExtendedHistoryFecLayerUncorrectedBlockCount_Type = Counter64
_CwsPmExtendedHistoryFecLayerUncorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedHistoryFecLayerUncorrectedBlockCount = _CwsPmExtendedHistoryFecLayerUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 46, 1, 3),
    _CwsPmExtendedHistoryFecLayerUncorrectedBlockCount_Type()
)
cwsPmExtendedHistoryFecLayerUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryFecLayerUncorrectedBlockCount.setStatus("current")
_CwsPmExtendedHistoryFecLayerSymbolErrorCount_Type = Counter64
_CwsPmExtendedHistoryFecLayerSymbolErrorCount_Object = MibTableColumn
cwsPmExtendedHistoryFecLayerSymbolErrorCount = _CwsPmExtendedHistoryFecLayerSymbolErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 46, 1, 4),
    _CwsPmExtendedHistoryFecLayerSymbolErrorCount_Type()
)
cwsPmExtendedHistoryFecLayerSymbolErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryFecLayerSymbolErrorCount.setStatus("current")
_CwsPmExtendedHistory24hIdTable_Object = MibTable
cwsPmExtendedHistory24hIdTable = _CwsPmExtendedHistory24hIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 47)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hIdTable.setStatus("current")
_CwsPmExtendedHistory24hIdEntry_Object = MibTableRow
cwsPmExtendedHistory24hIdEntry = _CwsPmExtendedHistory24hIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 47, 1)
)
cwsPmExtendedHistory24hIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hIdEntry.setStatus("current")


class _CwsPmExtendedHistory24hIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hIdTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hIdTableSnmpKey = _CwsPmExtendedHistory24hIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 47, 1, 1),
    _CwsPmExtendedHistory24hIdTableSnmpKey_Type()
)
cwsPmExtendedHistory24hIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hIdTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hIdBinNumber_Type = Unsigned32
_CwsPmExtendedHistory24hIdBinNumber_Object = MibTableColumn
cwsPmExtendedHistory24hIdBinNumber = _CwsPmExtendedHistory24hIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 47, 1, 2),
    _CwsPmExtendedHistory24hIdBinNumber_Type()
)
cwsPmExtendedHistory24hIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hIdBinNumber.setStatus("current")
_CwsPmExtendedHistory24hIdBinName_Type = StringMaxl32
_CwsPmExtendedHistory24hIdBinName_Object = MibTableColumn
cwsPmExtendedHistory24hIdBinName = _CwsPmExtendedHistory24hIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 47, 1, 3),
    _CwsPmExtendedHistory24hIdBinName_Type()
)
cwsPmExtendedHistory24hIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hIdBinName.setStatus("current")
_CwsPmExtendedHistory24hStateTable_Object = MibTable
cwsPmExtendedHistory24hStateTable = _CwsPmExtendedHistory24hStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 48)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStateTable.setStatus("current")
_CwsPmExtendedHistory24hStateEntry_Object = MibTableRow
cwsPmExtendedHistory24hStateEntry = _CwsPmExtendedHistory24hStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 48, 1)
)
cwsPmExtendedHistory24hStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStateEntry.setStatus("current")


class _CwsPmExtendedHistory24hStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hStateTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hStateTableSnmpKey = _CwsPmExtendedHistory24hStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 48, 1, 1),
    _CwsPmExtendedHistory24hStateTableSnmpKey_Type()
)
cwsPmExtendedHistory24hStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStateTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hStateStartDateTime_Type = StringMaxl32
_CwsPmExtendedHistory24hStateStartDateTime_Object = MibTableColumn
cwsPmExtendedHistory24hStateStartDateTime = _CwsPmExtendedHistory24hStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 48, 1, 2),
    _CwsPmExtendedHistory24hStateStartDateTime_Type()
)
cwsPmExtendedHistory24hStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStateStartDateTime.setStatus("current")
_CwsPmExtendedHistory24hStateEndDateTime_Type = StringMaxl32
_CwsPmExtendedHistory24hStateEndDateTime_Object = MibTableColumn
cwsPmExtendedHistory24hStateEndDateTime = _CwsPmExtendedHistory24hStateEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 48, 1, 3),
    _CwsPmExtendedHistory24hStateEndDateTime_Type()
)
cwsPmExtendedHistory24hStateEndDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStateEndDateTime.setStatus("current")
_CwsPmExtendedHistory24hStateState_Type = PmBinState
_CwsPmExtendedHistory24hStateState_Object = MibTableColumn
cwsPmExtendedHistory24hStateState = _CwsPmExtendedHistory24hStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 48, 1, 4),
    _CwsPmExtendedHistory24hStateState_Type()
)
cwsPmExtendedHistory24hStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStateState.setStatus("current")
_CwsPmExtendedHistory24hStatisticsTable_Object = MibTable
cwsPmExtendedHistory24hStatisticsTable = _CwsPmExtendedHistory24hStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 49)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStatisticsTable.setStatus("current")
_CwsPmExtendedHistory24hStatisticsEntry_Object = MibTableRow
cwsPmExtendedHistory24hStatisticsEntry = _CwsPmExtendedHistory24hStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 49, 1)
)
cwsPmExtendedHistory24hStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStatisticsEntry.setStatus("current")


class _CwsPmExtendedHistory24hStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hStatisticsTableSnmpKey = _CwsPmExtendedHistory24hStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 49, 1, 1),
    _CwsPmExtendedHistory24hStatisticsTableSnmpKey_Type()
)
cwsPmExtendedHistory24hStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStatisticsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hStatisticsFrameErrorRatio_Type = Counter64
_CwsPmExtendedHistory24hStatisticsFrameErrorRatio_Object = MibTableColumn
cwsPmExtendedHistory24hStatisticsFrameErrorRatio = _CwsPmExtendedHistory24hStatisticsFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 49, 1, 2),
    _CwsPmExtendedHistory24hStatisticsFrameErrorRatio_Type()
)
cwsPmExtendedHistory24hStatisticsFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hStatisticsFrameErrorRatio.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsTable_Object = MibTable
cwsPmExtendedHistory24hRxIfCountsTable = _CwsPmExtendedHistory24hRxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsTable.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsEntry_Object = MibTableRow
cwsPmExtendedHistory24hRxIfCountsEntry = _CwsPmExtendedHistory24hRxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1)
)
cwsPmExtendedHistory24hRxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsEntry.setStatus("current")


class _CwsPmExtendedHistory24hRxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hRxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hRxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hRxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsTableSnmpKey = _CwsPmExtendedHistory24hRxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 1),
    _CwsPmExtendedHistory24hRxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedHistory24hRxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsBytes_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsBytes = _CwsPmExtendedHistory24hRxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 2),
    _CwsPmExtendedHistory24hRxIfCountsBytes_Type()
)
cwsPmExtendedHistory24hRxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsBytes.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPackets = _CwsPmExtendedHistory24hRxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 3),
    _CwsPmExtendedHistory24hRxIfCountsPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsCrcErroredPackets = _CwsPmExtendedHistory24hRxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 4),
    _CwsPmExtendedHistory24hRxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsMulticastPackets = _CwsPmExtendedHistory24hRxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 5),
    _CwsPmExtendedHistory24hRxIfCountsMulticastPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsBroadcastPackets = _CwsPmExtendedHistory24hRxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 6),
    _CwsPmExtendedHistory24hRxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPausePackets = _CwsPmExtendedHistory24hRxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 7),
    _CwsPmExtendedHistory24hRxIfCountsPausePackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsUndersizedPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsUndersizedPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsUndersizedPackets = _CwsPmExtendedHistory24hRxIfCountsUndersizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 8),
    _CwsPmExtendedHistory24hRxIfCountsUndersizedPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsUndersizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsUndersizedPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsOversizedPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsOversizedPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsOversizedPackets = _CwsPmExtendedHistory24hRxIfCountsOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 9),
    _CwsPmExtendedHistory24hRxIfCountsOversizedPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsOversizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsOversizedPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsFragmentPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsFragmentPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsFragmentPackets = _CwsPmExtendedHistory24hRxIfCountsFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 10),
    _CwsPmExtendedHistory24hRxIfCountsFragmentPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsFragmentPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsFragmentPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsJabberPackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsJabberPackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsJabberPackets = _CwsPmExtendedHistory24hRxIfCountsJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 11),
    _CwsPmExtendedHistory24hRxIfCountsJabberPackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsJabberPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsJabberPackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets = _CwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 12),
    _CwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPackets64Octet_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPackets64Octet_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPackets64Octet = _CwsPmExtendedHistory24hRxIfCountsPackets64Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 13),
    _CwsPmExtendedHistory24hRxIfCountsPackets64Octet_Type()
)
cwsPmExtendedHistory24hRxIfCountsPackets64Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPackets64Octet.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPackets65127Octet_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPackets65127Octet_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPackets65127Octet = _CwsPmExtendedHistory24hRxIfCountsPackets65127Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 14),
    _CwsPmExtendedHistory24hRxIfCountsPackets65127Octet_Type()
)
cwsPmExtendedHistory24hRxIfCountsPackets65127Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPackets65127Octet.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPackets128255Octet_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPackets128255Octet_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPackets128255Octet = _CwsPmExtendedHistory24hRxIfCountsPackets128255Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 15),
    _CwsPmExtendedHistory24hRxIfCountsPackets128255Octet_Type()
)
cwsPmExtendedHistory24hRxIfCountsPackets128255Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPackets128255Octet.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPackets256511Octet_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPackets256511Octet_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPackets256511Octet = _CwsPmExtendedHistory24hRxIfCountsPackets256511Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 16),
    _CwsPmExtendedHistory24hRxIfCountsPackets256511Octet_Type()
)
cwsPmExtendedHistory24hRxIfCountsPackets256511Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPackets256511Octet.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPackets5121023Octet_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPackets5121023Octet_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPackets5121023Octet = _CwsPmExtendedHistory24hRxIfCountsPackets5121023Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 17),
    _CwsPmExtendedHistory24hRxIfCountsPackets5121023Octet_Type()
)
cwsPmExtendedHistory24hRxIfCountsPackets5121023Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPackets5121023Octet.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsPackets10241518Octet_Type = Counter64
_CwsPmExtendedHistory24hRxIfCountsPackets10241518Octet_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsPackets10241518Octet = _CwsPmExtendedHistory24hRxIfCountsPackets10241518Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 18),
    _CwsPmExtendedHistory24hRxIfCountsPackets10241518Octet_Type()
)
cwsPmExtendedHistory24hRxIfCountsPackets10241518Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsPackets10241518Octet.setStatus("current")
_CwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization = _CwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 50, 1, 19),
    _CwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsTable_Object = MibTable
cwsPmExtendedHistory24hTxIfCountsTable = _CwsPmExtendedHistory24hTxIfCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsTable.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsEntry_Object = MibTableRow
cwsPmExtendedHistory24hTxIfCountsEntry = _CwsPmExtendedHistory24hTxIfCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1)
)
cwsPmExtendedHistory24hTxIfCountsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsEntry.setStatus("current")


class _CwsPmExtendedHistory24hTxIfCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hTxIfCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hTxIfCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hTxIfCountsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsTableSnmpKey = _CwsPmExtendedHistory24hTxIfCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 1),
    _CwsPmExtendedHistory24hTxIfCountsTableSnmpKey_Type()
)
cwsPmExtendedHistory24hTxIfCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsBytes_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsBytes_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsBytes = _CwsPmExtendedHistory24hTxIfCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 2),
    _CwsPmExtendedHistory24hTxIfCountsBytes_Type()
)
cwsPmExtendedHistory24hTxIfCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsBytes.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsPackets = _CwsPmExtendedHistory24hTxIfCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 3),
    _CwsPmExtendedHistory24hTxIfCountsPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsCrcErroredPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsCrcErroredPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsCrcErroredPackets = _CwsPmExtendedHistory24hTxIfCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 4),
    _CwsPmExtendedHistory24hTxIfCountsCrcErroredPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsCrcErroredPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsMulticastPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsMulticastPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsMulticastPackets = _CwsPmExtendedHistory24hTxIfCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 5),
    _CwsPmExtendedHistory24hTxIfCountsMulticastPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsMulticastPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsBroadcastPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsBroadcastPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsBroadcastPackets = _CwsPmExtendedHistory24hTxIfCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 6),
    _CwsPmExtendedHistory24hTxIfCountsBroadcastPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsBroadcastPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsPausePackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsPausePackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsPausePackets = _CwsPmExtendedHistory24hTxIfCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 7),
    _CwsPmExtendedHistory24hTxIfCountsPausePackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsPausePackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets = _CwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 8),
    _CwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsGiantPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsGiantPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsGiantPackets = _CwsPmExtendedHistory24hTxIfCountsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 9),
    _CwsPmExtendedHistory24hTxIfCountsGiantPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsGiantPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsGiantPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsUnderrunPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsUnderrunPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsUnderrunPackets = _CwsPmExtendedHistory24hTxIfCountsUnderrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 10),
    _CwsPmExtendedHistory24hTxIfCountsUnderrunPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsUnderrunPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsUnderrunPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets = _CwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 11),
    _CwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets_Type = Counter64
_CwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets = _CwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 12),
    _CwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets_Type()
)
cwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets.setStatus("current")
_CwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization_Object = MibTableColumn
cwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization = _CwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 51, 1, 13),
    _CwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization_Type()
)
cwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization.setStatus("current")
_CwsPmExtendedHistory24hTxQueueTable_Object = MibTable
cwsPmExtendedHistory24hTxQueueTable = _CwsPmExtendedHistory24hTxQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueTable.setStatus("current")
_CwsPmExtendedHistory24hTxQueueEntry_Object = MibTableRow
cwsPmExtendedHistory24hTxQueueEntry = _CwsPmExtendedHistory24hTxQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1)
)
cwsPmExtendedHistory24hTxQueueEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueEntry.setStatus("current")


class _CwsPmExtendedHistory24hTxQueueTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hTxQueueTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hTxQueueTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hTxQueueTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueTableSnmpKey = _CwsPmExtendedHistory24hTxQueueTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 1),
    _CwsPmExtendedHistory24hTxQueueTableSnmpKey_Type()
)
cwsPmExtendedHistory24hTxQueueTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hTxQueuePacketDropCountSummary_Type = Counter64
_CwsPmExtendedHistory24hTxQueuePacketDropCountSummary_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueuePacketDropCountSummary = _CwsPmExtendedHistory24hTxQueuePacketDropCountSummary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 2),
    _CwsPmExtendedHistory24hTxQueuePacketDropCountSummary_Type()
)
cwsPmExtendedHistory24hTxQueuePacketDropCountSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueuePacketDropCountSummary.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ0PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ0PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ0PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ0PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 3),
    _CwsPmExtendedHistory24hTxQueueQ0PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ0PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ0PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ1PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ1PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ1PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ1PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 4),
    _CwsPmExtendedHistory24hTxQueueQ1PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ1PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ1PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ2PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ2PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ2PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ2PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 5),
    _CwsPmExtendedHistory24hTxQueueQ2PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ2PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ2PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ3PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ3PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ3PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ3PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 6),
    _CwsPmExtendedHistory24hTxQueueQ3PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ3PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ3PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ4PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ4PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ4PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ4PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 7),
    _CwsPmExtendedHistory24hTxQueueQ4PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ4PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ4PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ5PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ5PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ5PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ5PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 8),
    _CwsPmExtendedHistory24hTxQueueQ5PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ5PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ5PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ6PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ6PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ6PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ6PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 9),
    _CwsPmExtendedHistory24hTxQueueQ6PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ6PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ6PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hTxQueueQ7PacketDropCount_Type = Counter64
_CwsPmExtendedHistory24hTxQueueQ7PacketDropCount_Object = MibTableColumn
cwsPmExtendedHistory24hTxQueueQ7PacketDropCount = _CwsPmExtendedHistory24hTxQueueQ7PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 52, 1, 10),
    _CwsPmExtendedHistory24hTxQueueQ7PacketDropCount_Type()
)
cwsPmExtendedHistory24hTxQueueQ7PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hTxQueueQ7PacketDropCount.setStatus("current")
_CwsPmExtendedHistory24hMacLayerTable_Object = MibTable
cwsPmExtendedHistory24hMacLayerTable = _CwsPmExtendedHistory24hMacLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 53)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hMacLayerTable.setStatus("obsolete")
_CwsPmExtendedHistory24hMacLayerEntry_Object = MibTableRow
cwsPmExtendedHistory24hMacLayerEntry = _CwsPmExtendedHistory24hMacLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 53, 1)
)
cwsPmExtendedHistory24hMacLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hMacLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hMacLayerEntry.setStatus("obsolete")


class _CwsPmExtendedHistory24hMacLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hMacLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hMacLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hMacLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hMacLayerTableSnmpKey = _CwsPmExtendedHistory24hMacLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 53, 1, 1),
    _CwsPmExtendedHistory24hMacLayerTableSnmpKey_Type()
)
cwsPmExtendedHistory24hMacLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hMacLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hMacLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedHistory24hMacLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedHistory24hMacLayerUnavailableSeconds = _CwsPmExtendedHistory24hMacLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 53, 1, 2),
    _CwsPmExtendedHistory24hMacLayerUnavailableSeconds_Type()
)
cwsPmExtendedHistory24hMacLayerUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hMacLayerUnavailableSeconds.setStatus("obsolete")
_CwsPmExtendedHistory24hPcsLayerTable_Object = MibTable
cwsPmExtendedHistory24hPcsLayerTable = _CwsPmExtendedHistory24hPcsLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 54)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsLayerTable.setStatus("current")
_CwsPmExtendedHistory24hPcsLayerEntry_Object = MibTableRow
cwsPmExtendedHistory24hPcsLayerEntry = _CwsPmExtendedHistory24hPcsLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 54, 1)
)
cwsPmExtendedHistory24hPcsLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsLayerEntry.setStatus("current")


class _CwsPmExtendedHistory24hPcsLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hPcsLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hPcsLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hPcsLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hPcsLayerTableSnmpKey = _CwsPmExtendedHistory24hPcsLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 54, 1, 1),
    _CwsPmExtendedHistory24hPcsLayerTableSnmpKey_Type()
)
cwsPmExtendedHistory24hPcsLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hPcsLayerErroredSeconds_Type = Counter64
_CwsPmExtendedHistory24hPcsLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistory24hPcsLayerErroredSeconds = _CwsPmExtendedHistory24hPcsLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 54, 1, 2),
    _CwsPmExtendedHistory24hPcsLayerErroredSeconds_Type()
)
cwsPmExtendedHistory24hPcsLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsLayerErroredSeconds.setStatus("current")
_CwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds = _CwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 54, 1, 3),
    _CwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedHistory24hPcsLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedHistory24hPcsLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedHistory24hPcsLayerUnavailableSeconds = _CwsPmExtendedHistory24hPcsLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 54, 1, 4),
    _CwsPmExtendedHistory24hPcsLayerUnavailableSeconds_Type()
)
cwsPmExtendedHistory24hPcsLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsLayerUnavailableSeconds.setStatus("current")
_CwsPmExtendedHistory24hPcsSyncHeaderErrorsTable_Object = MibTable
cwsPmExtendedHistory24hPcsSyncHeaderErrorsTable = _CwsPmExtendedHistory24hPcsSyncHeaderErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 55)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsSyncHeaderErrorsTable.setStatus("current")
_CwsPmExtendedHistory24hPcsSyncHeaderErrorsEntry_Object = MibTableRow
cwsPmExtendedHistory24hPcsSyncHeaderErrorsEntry = _CwsPmExtendedHistory24hPcsSyncHeaderErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 55, 1)
)
cwsPmExtendedHistory24hPcsSyncHeaderErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsSyncHeaderErrorsEntry.setStatus("current")


class _CwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey = _CwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 55, 1, 1),
    _CwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey_Type()
)
cwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hPcsSyncHeaderErrorsCount_Type = Counter64
_CwsPmExtendedHistory24hPcsSyncHeaderErrorsCount_Object = MibTableColumn
cwsPmExtendedHistory24hPcsSyncHeaderErrorsCount = _CwsPmExtendedHistory24hPcsSyncHeaderErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 55, 1, 2),
    _CwsPmExtendedHistory24hPcsSyncHeaderErrorsCount_Type()
)
cwsPmExtendedHistory24hPcsSyncHeaderErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsSyncHeaderErrorsCount.setStatus("current")
_CwsPmExtendedHistory24hPcsBlockErrorsTable_Object = MibTable
cwsPmExtendedHistory24hPcsBlockErrorsTable = _CwsPmExtendedHistory24hPcsBlockErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 56)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsBlockErrorsTable.setStatus("current")
_CwsPmExtendedHistory24hPcsBlockErrorsEntry_Object = MibTableRow
cwsPmExtendedHistory24hPcsBlockErrorsEntry = _CwsPmExtendedHistory24hPcsBlockErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 56, 1)
)
cwsPmExtendedHistory24hPcsBlockErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsBlockErrorsEntry.setStatus("current")


class _CwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey = _CwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 56, 1, 1),
    _CwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey_Type()
)
cwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hPcsBlockErrorsCount_Type = Counter64
_CwsPmExtendedHistory24hPcsBlockErrorsCount_Object = MibTableColumn
cwsPmExtendedHistory24hPcsBlockErrorsCount = _CwsPmExtendedHistory24hPcsBlockErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 56, 1, 2),
    _CwsPmExtendedHistory24hPcsBlockErrorsCount_Type()
)
cwsPmExtendedHistory24hPcsBlockErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsBlockErrorsCount.setStatus("current")
_CwsPmExtendedHistory24hPcsMultilaneBipErrorsTable_Object = MibTable
cwsPmExtendedHistory24hPcsMultilaneBipErrorsTable = _CwsPmExtendedHistory24hPcsMultilaneBipErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 57)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsMultilaneBipErrorsTable.setStatus("current")
_CwsPmExtendedHistory24hPcsMultilaneBipErrorsEntry_Object = MibTableRow
cwsPmExtendedHistory24hPcsMultilaneBipErrorsEntry = _CwsPmExtendedHistory24hPcsMultilaneBipErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 57, 1)
)
cwsPmExtendedHistory24hPcsMultilaneBipErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsMultilaneBipErrorsEntry.setStatus("current")


class _CwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey = _CwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 57, 1, 1),
    _CwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey_Type()
)
cwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hPcsMultilaneBipErrorsCount_Type = Counter64
_CwsPmExtendedHistory24hPcsMultilaneBipErrorsCount_Object = MibTableColumn
cwsPmExtendedHistory24hPcsMultilaneBipErrorsCount = _CwsPmExtendedHistory24hPcsMultilaneBipErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 57, 1, 2),
    _CwsPmExtendedHistory24hPcsMultilaneBipErrorsCount_Type()
)
cwsPmExtendedHistory24hPcsMultilaneBipErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hPcsMultilaneBipErrorsCount.setStatus("current")
_CwsPmExtendedHistory24hFecLayerTable_Object = MibTable
cwsPmExtendedHistory24hFecLayerTable = _CwsPmExtendedHistory24hFecLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 58)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hFecLayerTable.setStatus("current")
_CwsPmExtendedHistory24hFecLayerEntry_Object = MibTableRow
cwsPmExtendedHistory24hFecLayerEntry = _CwsPmExtendedHistory24hFecLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 58, 1)
)
cwsPmExtendedHistory24hFecLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hFecLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hFecLayerEntry.setStatus("current")


class _CwsPmExtendedHistory24hFecLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hFecLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hFecLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hFecLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hFecLayerTableSnmpKey = _CwsPmExtendedHistory24hFecLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 58, 1, 1),
    _CwsPmExtendedHistory24hFecLayerTableSnmpKey_Type()
)
cwsPmExtendedHistory24hFecLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hFecLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hFecLayerCorrectedBlockCount_Type = Counter64
_CwsPmExtendedHistory24hFecLayerCorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedHistory24hFecLayerCorrectedBlockCount = _CwsPmExtendedHistory24hFecLayerCorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 58, 1, 2),
    _CwsPmExtendedHistory24hFecLayerCorrectedBlockCount_Type()
)
cwsPmExtendedHistory24hFecLayerCorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hFecLayerCorrectedBlockCount.setStatus("current")
_CwsPmExtendedHistory24hFecLayerUncorrectedBlockCount_Type = Counter64
_CwsPmExtendedHistory24hFecLayerUncorrectedBlockCount_Object = MibTableColumn
cwsPmExtendedHistory24hFecLayerUncorrectedBlockCount = _CwsPmExtendedHistory24hFecLayerUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 58, 1, 3),
    _CwsPmExtendedHistory24hFecLayerUncorrectedBlockCount_Type()
)
cwsPmExtendedHistory24hFecLayerUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hFecLayerUncorrectedBlockCount.setStatus("current")
_CwsPmExtendedHistory24hFecLayerSymbolErrorCount_Type = Counter64
_CwsPmExtendedHistory24hFecLayerSymbolErrorCount_Object = MibTableColumn
cwsPmExtendedHistory24hFecLayerSymbolErrorCount = _CwsPmExtendedHistory24hFecLayerSymbolErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 58, 1, 4),
    _CwsPmExtendedHistory24hFecLayerSymbolErrorCount_Type()
)
cwsPmExtendedHistory24hFecLayerSymbolErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hFecLayerSymbolErrorCount.setStatus("current")
_CwsPmPtpBasicInstancesTable_Object = MibTable
cwsPmPtpBasicInstancesTable = _CwsPmPtpBasicInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 59)
)
if mibBuilder.loadTexts:
    cwsPmPtpBasicInstancesTable.setStatus("current")
_CwsPmPtpBasicInstancesEntry_Object = MibTableRow
cwsPmPtpBasicInstancesEntry = _CwsPmPtpBasicInstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 59, 1)
)
cwsPmPtpBasicInstancesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
)
if mibBuilder.loadTexts:
    cwsPmPtpBasicInstancesEntry.setStatus("current")


class _CwsPmPtpBasicInstancesInstanceName_Type(Integer32):
    """Custom type cwsPmPtpBasicInstancesInstanceName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmPtpBasicInstancesInstanceName_Type.__name__ = "Integer32"
_CwsPmPtpBasicInstancesInstanceName_Object = MibTableColumn
cwsPmPtpBasicInstancesInstanceName = _CwsPmPtpBasicInstancesInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 59, 1, 1),
    _CwsPmPtpBasicInstancesInstanceName_Type()
)
cwsPmPtpBasicInstancesInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPtpBasicInstancesInstanceName.setStatus("current")
_CwsPmBasicIdTable_Object = MibTable
cwsPmBasicIdTable = _CwsPmBasicIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 60)
)
if mibBuilder.loadTexts:
    cwsPmBasicIdTable.setStatus("current")
_CwsPmBasicIdEntry_Object = MibTableRow
cwsPmBasicIdEntry = _CwsPmBasicIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 60, 1)
)
cwsPmBasicIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicIdEntry.setStatus("current")


class _CwsPmBasicIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicIdTableSnmpKey_Object = MibTableColumn
cwsPmBasicIdTableSnmpKey = _CwsPmBasicIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 60, 1, 1),
    _CwsPmBasicIdTableSnmpKey_Type()
)
cwsPmBasicIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicIdTableSnmpKey.setStatus("current")
_CwsPmBasicIdInstanceId_Type = Unsigned32
_CwsPmBasicIdInstanceId_Object = MibTableColumn
cwsPmBasicIdInstanceId = _CwsPmBasicIdInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 60, 1, 2),
    _CwsPmBasicIdInstanceId_Type()
)
cwsPmBasicIdInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicIdInstanceId.setStatus("current")
_CwsPmBasicIdInstanceType_Type = PmInstanceType
_CwsPmBasicIdInstanceType_Object = MibTableColumn
cwsPmBasicIdInstanceType = _CwsPmBasicIdInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 60, 1, 3),
    _CwsPmBasicIdInstanceType_Type()
)
cwsPmBasicIdInstanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicIdInstanceType.setStatus("current")
_CwsPmBasicIdProfileType_Type = PmProfileType
_CwsPmBasicIdProfileType_Object = MibTableColumn
cwsPmBasicIdProfileType = _CwsPmBasicIdProfileType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 60, 1, 4),
    _CwsPmBasicIdProfileType_Type()
)
cwsPmBasicIdProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicIdProfileType.setStatus("current")
_CwsPmBasicStateTable_Object = MibTable
cwsPmBasicStateTable = _CwsPmBasicStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61)
)
if mibBuilder.loadTexts:
    cwsPmBasicStateTable.setStatus("current")
_CwsPmBasicStateEntry_Object = MibTableRow
cwsPmBasicStateEntry = _CwsPmBasicStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61, 1)
)
cwsPmBasicStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicStateEntry.setStatus("current")


class _CwsPmBasicStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicStateTableSnmpKey_Object = MibTableColumn
cwsPmBasicStateTableSnmpKey = _CwsPmBasicStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61, 1, 1),
    _CwsPmBasicStateTableSnmpKey_Type()
)
cwsPmBasicStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicStateTableSnmpKey.setStatus("current")
_CwsPmBasicStateAdminState_Type = EnabledDisabledEnum
_CwsPmBasicStateAdminState_Object = MibTableColumn
cwsPmBasicStateAdminState = _CwsPmBasicStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61, 1, 2),
    _CwsPmBasicStateAdminState_Type()
)
cwsPmBasicStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicStateAdminState.setStatus("current")
_CwsPmBasicStateOperationalState_Type = EnabledDisabledEnum
_CwsPmBasicStateOperationalState_Object = MibTableColumn
cwsPmBasicStateOperationalState = _CwsPmBasicStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61, 1, 3),
    _CwsPmBasicStateOperationalState_Type()
)
cwsPmBasicStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicStateOperationalState.setStatus("current")
_CwsPmBasicStateCurrentBinId_Type = Unsigned32
_CwsPmBasicStateCurrentBinId_Object = MibTableColumn
cwsPmBasicStateCurrentBinId = _CwsPmBasicStateCurrentBinId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61, 1, 4),
    _CwsPmBasicStateCurrentBinId_Type()
)
cwsPmBasicStateCurrentBinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicStateCurrentBinId.setStatus("current")
_CwsPmBasicStateCollectionStartDateTime_Type = StringMaxl64
_CwsPmBasicStateCollectionStartDateTime_Object = MibTableColumn
cwsPmBasicStateCollectionStartDateTime = _CwsPmBasicStateCollectionStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61, 1, 5),
    _CwsPmBasicStateCollectionStartDateTime_Type()
)
cwsPmBasicStateCollectionStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicStateCollectionStartDateTime.setStatus("current")
_CwsPmBasicStateCollectionEndDateTime_Type = StringMaxl64
_CwsPmBasicStateCollectionEndDateTime_Object = MibTableColumn
cwsPmBasicStateCollectionEndDateTime = _CwsPmBasicStateCollectionEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 61, 1, 6),
    _CwsPmBasicStateCollectionEndDateTime_Type()
)
cwsPmBasicStateCollectionEndDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicStateCollectionEndDateTime.setStatus("current")
_CwsPmBasicPropertiesTable_Object = MibTable
cwsPmBasicPropertiesTable = _CwsPmBasicPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 62)
)
if mibBuilder.loadTexts:
    cwsPmBasicPropertiesTable.setStatus("current")
_CwsPmBasicPropertiesEntry_Object = MibTableRow
cwsPmBasicPropertiesEntry = _CwsPmBasicPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 62, 1)
)
cwsPmBasicPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicPropertiesEntry.setStatus("current")


class _CwsPmBasicPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicPropertiesTableSnmpKey_Object = MibTableColumn
cwsPmBasicPropertiesTableSnmpKey = _CwsPmBasicPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 62, 1, 1),
    _CwsPmBasicPropertiesTableSnmpKey_Type()
)
cwsPmBasicPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicPropertiesTableSnmpKey.setStatus("current")
_CwsPmBasicPropertiesConfigurationMode_Type = PmConfigurationMode
_CwsPmBasicPropertiesConfigurationMode_Object = MibTableColumn
cwsPmBasicPropertiesConfigurationMode = _CwsPmBasicPropertiesConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 62, 1, 2),
    _CwsPmBasicPropertiesConfigurationMode_Type()
)
cwsPmBasicPropertiesConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicPropertiesConfigurationMode.setStatus("current")
_CwsPmBasicPropertiesAlignment_Type = PmAlignment
_CwsPmBasicPropertiesAlignment_Object = MibTableColumn
cwsPmBasicPropertiesAlignment = _CwsPmBasicPropertiesAlignment_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 62, 1, 3),
    _CwsPmBasicPropertiesAlignment_Type()
)
cwsPmBasicPropertiesAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicPropertiesAlignment.setStatus("current")
_CwsPmBasicPropertiesConfiguredBinCount_Type = Unsigned32
_CwsPmBasicPropertiesConfiguredBinCount_Object = MibTableColumn
cwsPmBasicPropertiesConfiguredBinCount = _CwsPmBasicPropertiesConfiguredBinCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 62, 1, 4),
    _CwsPmBasicPropertiesConfiguredBinCount_Type()
)
cwsPmBasicPropertiesConfiguredBinCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicPropertiesConfiguredBinCount.setStatus("current")
_CwsPmBasicPropertiesConfiguredBinDuration_Type = Unsigned32
_CwsPmBasicPropertiesConfiguredBinDuration_Object = MibTableColumn
cwsPmBasicPropertiesConfiguredBinDuration = _CwsPmBasicPropertiesConfiguredBinDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 62, 1, 5),
    _CwsPmBasicPropertiesConfiguredBinDuration_Type()
)
cwsPmBasicPropertiesConfiguredBinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicPropertiesConfiguredBinDuration.setStatus("current")
_CwsPmBasicAttachedInterfaceTable_Object = MibTable
cwsPmBasicAttachedInterfaceTable = _CwsPmBasicAttachedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 63)
)
if mibBuilder.loadTexts:
    cwsPmBasicAttachedInterfaceTable.setStatus("current")
_CwsPmBasicAttachedInterfaceEntry_Object = MibTableRow
cwsPmBasicAttachedInterfaceEntry = _CwsPmBasicAttachedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 63, 1)
)
cwsPmBasicAttachedInterfaceEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicAttachedInterfaceTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicAttachedInterfaceEntry.setStatus("current")


class _CwsPmBasicAttachedInterfaceTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicAttachedInterfaceTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicAttachedInterfaceTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicAttachedInterfaceTableSnmpKey_Object = MibTableColumn
cwsPmBasicAttachedInterfaceTableSnmpKey = _CwsPmBasicAttachedInterfaceTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 63, 1, 1),
    _CwsPmBasicAttachedInterfaceTableSnmpKey_Type()
)
cwsPmBasicAttachedInterfaceTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicAttachedInterfaceTableSnmpKey.setStatus("current")
_CwsPmBasicAttachedInterfaceType_Type = PmInterfaceType
_CwsPmBasicAttachedInterfaceType_Object = MibTableColumn
cwsPmBasicAttachedInterfaceType = _CwsPmBasicAttachedInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 63, 1, 2),
    _CwsPmBasicAttachedInterfaceType_Type()
)
cwsPmBasicAttachedInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicAttachedInterfaceType.setStatus("current")
_CwsPmBasicAttachedInterfaceName_Type = StringMaxl32
_CwsPmBasicAttachedInterfaceName_Object = MibTableColumn
cwsPmBasicAttachedInterfaceName = _CwsPmBasicAttachedInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 63, 1, 3),
    _CwsPmBasicAttachedInterfaceName_Type()
)
cwsPmBasicAttachedInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicAttachedInterfaceName.setStatus("current")
_CwsPmBasicAttachedInterfaceOperationalState_Type = EnabledDisabledEnum
_CwsPmBasicAttachedInterfaceOperationalState_Object = MibTableColumn
cwsPmBasicAttachedInterfaceOperationalState = _CwsPmBasicAttachedInterfaceOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 63, 1, 4),
    _CwsPmBasicAttachedInterfaceOperationalState_Type()
)
cwsPmBasicAttachedInterfaceOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicAttachedInterfaceOperationalState.setStatus("current")
_CwsPmBasicCurrentIdTable_Object = MibTable
cwsPmBasicCurrentIdTable = _CwsPmBasicCurrentIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 64)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentIdTable.setStatus("current")
_CwsPmBasicCurrentIdEntry_Object = MibTableRow
cwsPmBasicCurrentIdEntry = _CwsPmBasicCurrentIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 64, 1)
)
cwsPmBasicCurrentIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentIdEntry.setStatus("current")


class _CwsPmBasicCurrentIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrentIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrentIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrentIdTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrentIdTableSnmpKey = _CwsPmBasicCurrentIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 64, 1, 1),
    _CwsPmBasicCurrentIdTableSnmpKey_Type()
)
cwsPmBasicCurrentIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentIdTableSnmpKey.setStatus("current")
_CwsPmBasicCurrentIdBinNumber_Type = Unsigned32
_CwsPmBasicCurrentIdBinNumber_Object = MibTableColumn
cwsPmBasicCurrentIdBinNumber = _CwsPmBasicCurrentIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 64, 1, 2),
    _CwsPmBasicCurrentIdBinNumber_Type()
)
cwsPmBasicCurrentIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentIdBinNumber.setStatus("current")
_CwsPmBasicCurrentIdBinName_Type = StringMaxl32
_CwsPmBasicCurrentIdBinName_Object = MibTableColumn
cwsPmBasicCurrentIdBinName = _CwsPmBasicCurrentIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 64, 1, 3),
    _CwsPmBasicCurrentIdBinName_Type()
)
cwsPmBasicCurrentIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentIdBinName.setStatus("current")
_CwsPmBasicCurrentStateTable_Object = MibTable
cwsPmBasicCurrentStateTable = _CwsPmBasicCurrentStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 65)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStateTable.setStatus("current")
_CwsPmBasicCurrentStateEntry_Object = MibTableRow
cwsPmBasicCurrentStateEntry = _CwsPmBasicCurrentStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 65, 1)
)
cwsPmBasicCurrentStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStateEntry.setStatus("current")


class _CwsPmBasicCurrentStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrentStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrentStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrentStateTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrentStateTableSnmpKey = _CwsPmBasicCurrentStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 65, 1, 1),
    _CwsPmBasicCurrentStateTableSnmpKey_Type()
)
cwsPmBasicCurrentStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStateTableSnmpKey.setStatus("current")
_CwsPmBasicCurrentStateStartDateTime_Type = StringMaxl32
_CwsPmBasicCurrentStateStartDateTime_Object = MibTableColumn
cwsPmBasicCurrentStateStartDateTime = _CwsPmBasicCurrentStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 65, 1, 2),
    _CwsPmBasicCurrentStateStartDateTime_Type()
)
cwsPmBasicCurrentStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStateStartDateTime.setStatus("current")
_CwsPmBasicCurrentStateClearedDateTime_Type = StringMaxl32
_CwsPmBasicCurrentStateClearedDateTime_Object = MibTableColumn
cwsPmBasicCurrentStateClearedDateTime = _CwsPmBasicCurrentStateClearedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 65, 1, 3),
    _CwsPmBasicCurrentStateClearedDateTime_Type()
)
cwsPmBasicCurrentStateClearedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStateClearedDateTime.setStatus("current")
_CwsPmBasicCurrentStateState_Type = PmBinState
_CwsPmBasicCurrentStateState_Object = MibTableColumn
cwsPmBasicCurrentStateState = _CwsPmBasicCurrentStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 65, 1, 4),
    _CwsPmBasicCurrentStateState_Type()
)
cwsPmBasicCurrentStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStateState.setStatus("current")
_CwsPmBasicCurrentStatisticsTable_Object = MibTable
cwsPmBasicCurrentStatisticsTable = _CwsPmBasicCurrentStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 66)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStatisticsTable.setStatus("current")
_CwsPmBasicCurrentStatisticsEntry_Object = MibTableRow
cwsPmBasicCurrentStatisticsEntry = _CwsPmBasicCurrentStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 66, 1)
)
cwsPmBasicCurrentStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStatisticsEntry.setStatus("current")


class _CwsPmBasicCurrentStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrentStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrentStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrentStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrentStatisticsTableSnmpKey = _CwsPmBasicCurrentStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 66, 1, 1),
    _CwsPmBasicCurrentStatisticsTableSnmpKey_Type()
)
cwsPmBasicCurrentStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStatisticsTableSnmpKey.setStatus("current")
_CwsPmBasicCurrentStatisticsNumberOfChannels_Type = Unsigned32
_CwsPmBasicCurrentStatisticsNumberOfChannels_Object = MibTableColumn
cwsPmBasicCurrentStatisticsNumberOfChannels = _CwsPmBasicCurrentStatisticsNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 66, 1, 2),
    _CwsPmBasicCurrentStatisticsNumberOfChannels_Type()
)
cwsPmBasicCurrentStatisticsNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentStatisticsNumberOfChannels.setStatus("current")
_CwsPmBasicCurrentOpticalPowerTable_Object = MibTable
cwsPmBasicCurrentOpticalPowerTable = _CwsPmBasicCurrentOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 67)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalPowerTable.setStatus("current")
_CwsPmBasicCurrentOpticalPowerEntry_Object = MibTableRow
cwsPmBasicCurrentOpticalPowerEntry = _CwsPmBasicCurrentOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 67, 1)
)
cwsPmBasicCurrentOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalPowerChannelNumber"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalPowerEntry.setStatus("current")


class _CwsPmBasicCurrentOpticalPowerChannelNumber_Type(Integer32):
    """Custom type cwsPmBasicCurrentOpticalPowerChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrentOpticalPowerChannelNumber_Type.__name__ = "Integer32"
_CwsPmBasicCurrentOpticalPowerChannelNumber_Object = MibTableColumn
cwsPmBasicCurrentOpticalPowerChannelNumber = _CwsPmBasicCurrentOpticalPowerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 67, 1, 1),
    _CwsPmBasicCurrentOpticalPowerChannelNumber_Type()
)
cwsPmBasicCurrentOpticalPowerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalPowerChannelNumber.setStatus("current")
_CwsPmBasicCurrentOpticalRxPowerTable_Object = MibTable
cwsPmBasicCurrentOpticalRxPowerTable = _CwsPmBasicCurrentOpticalRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 68)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalRxPowerTable.setStatus("current")
_CwsPmBasicCurrentOpticalRxPowerEntry_Object = MibTableRow
cwsPmBasicCurrentOpticalRxPowerEntry = _CwsPmBasicCurrentOpticalRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 68, 1)
)
cwsPmBasicCurrentOpticalRxPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalRxPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalRxPowerEntry.setStatus("current")


class _CwsPmBasicCurrentOpticalRxPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrentOpticalRxPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrentOpticalRxPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrentOpticalRxPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrentOpticalRxPowerTableSnmpKey = _CwsPmBasicCurrentOpticalRxPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 68, 1, 1),
    _CwsPmBasicCurrentOpticalRxPowerTableSnmpKey_Type()
)
cwsPmBasicCurrentOpticalRxPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalRxPowerTableSnmpKey.setStatus("current")
_CwsPmBasicCurrentOpticalRxPowerActual_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalRxPowerActual_Object = MibTableColumn
cwsPmBasicCurrentOpticalRxPowerActual = _CwsPmBasicCurrentOpticalRxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 68, 1, 2),
    _CwsPmBasicCurrentOpticalRxPowerActual_Type()
)
cwsPmBasicCurrentOpticalRxPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalRxPowerActual.setStatus("current")
_CwsPmBasicCurrentOpticalRxPowerMinimum_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalRxPowerMinimum_Object = MibTableColumn
cwsPmBasicCurrentOpticalRxPowerMinimum = _CwsPmBasicCurrentOpticalRxPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 68, 1, 3),
    _CwsPmBasicCurrentOpticalRxPowerMinimum_Type()
)
cwsPmBasicCurrentOpticalRxPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalRxPowerMinimum.setStatus("current")
_CwsPmBasicCurrentOpticalRxPowerMaximum_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalRxPowerMaximum_Object = MibTableColumn
cwsPmBasicCurrentOpticalRxPowerMaximum = _CwsPmBasicCurrentOpticalRxPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 68, 1, 4),
    _CwsPmBasicCurrentOpticalRxPowerMaximum_Type()
)
cwsPmBasicCurrentOpticalRxPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalRxPowerMaximum.setStatus("current")
_CwsPmBasicCurrentOpticalRxPowerAverage_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalRxPowerAverage_Object = MibTableColumn
cwsPmBasicCurrentOpticalRxPowerAverage = _CwsPmBasicCurrentOpticalRxPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 68, 1, 5),
    _CwsPmBasicCurrentOpticalRxPowerAverage_Type()
)
cwsPmBasicCurrentOpticalRxPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalRxPowerAverage.setStatus("current")
_CwsPmBasicCurrentOpticalTxPowerTable_Object = MibTable
cwsPmBasicCurrentOpticalTxPowerTable = _CwsPmBasicCurrentOpticalTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 69)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalTxPowerTable.setStatus("current")
_CwsPmBasicCurrentOpticalTxPowerEntry_Object = MibTableRow
cwsPmBasicCurrentOpticalTxPowerEntry = _CwsPmBasicCurrentOpticalTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 69, 1)
)
cwsPmBasicCurrentOpticalTxPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalTxPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalTxPowerEntry.setStatus("current")


class _CwsPmBasicCurrentOpticalTxPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrentOpticalTxPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrentOpticalTxPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrentOpticalTxPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrentOpticalTxPowerTableSnmpKey = _CwsPmBasicCurrentOpticalTxPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 69, 1, 1),
    _CwsPmBasicCurrentOpticalTxPowerTableSnmpKey_Type()
)
cwsPmBasicCurrentOpticalTxPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalTxPowerTableSnmpKey.setStatus("current")
_CwsPmBasicCurrentOpticalTxPowerActual_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalTxPowerActual_Object = MibTableColumn
cwsPmBasicCurrentOpticalTxPowerActual = _CwsPmBasicCurrentOpticalTxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 69, 1, 2),
    _CwsPmBasicCurrentOpticalTxPowerActual_Type()
)
cwsPmBasicCurrentOpticalTxPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalTxPowerActual.setStatus("current")
_CwsPmBasicCurrentOpticalTxPowerMinimum_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalTxPowerMinimum_Object = MibTableColumn
cwsPmBasicCurrentOpticalTxPowerMinimum = _CwsPmBasicCurrentOpticalTxPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 69, 1, 3),
    _CwsPmBasicCurrentOpticalTxPowerMinimum_Type()
)
cwsPmBasicCurrentOpticalTxPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalTxPowerMinimum.setStatus("current")
_CwsPmBasicCurrentOpticalTxPowerMaximum_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalTxPowerMaximum_Object = MibTableColumn
cwsPmBasicCurrentOpticalTxPowerMaximum = _CwsPmBasicCurrentOpticalTxPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 69, 1, 4),
    _CwsPmBasicCurrentOpticalTxPowerMaximum_Type()
)
cwsPmBasicCurrentOpticalTxPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalTxPowerMaximum.setStatus("current")
_CwsPmBasicCurrentOpticalTxPowerAverage_Type = Decimal3Dig
_CwsPmBasicCurrentOpticalTxPowerAverage_Object = MibTableColumn
cwsPmBasicCurrentOpticalTxPowerAverage = _CwsPmBasicCurrentOpticalTxPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 69, 1, 5),
    _CwsPmBasicCurrentOpticalTxPowerAverage_Type()
)
cwsPmBasicCurrentOpticalTxPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentOpticalTxPowerAverage.setStatus("current")
_CwsPmBasicCurrentChannelRxPowerTable_Object = MibTable
cwsPmBasicCurrentChannelRxPowerTable = _CwsPmBasicCurrentChannelRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 70)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentChannelRxPowerTable.setStatus("current")
_CwsPmBasicCurrentChannelRxPowerEntry_Object = MibTableRow
cwsPmBasicCurrentChannelRxPowerEntry = _CwsPmBasicCurrentChannelRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 70, 1)
)
cwsPmBasicCurrentChannelRxPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrentChannelRxPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrentChannelRxPowerEntry.setStatus("current")


class _CwsPmBasicCurrentChannelRxPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrentChannelRxPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrentChannelRxPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrentChannelRxPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrentChannelRxPowerTableSnmpKey = _CwsPmBasicCurrentChannelRxPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 70, 1, 1),
    _CwsPmBasicCurrentChannelRxPowerTableSnmpKey_Type()
)
cwsPmBasicCurrentChannelRxPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentChannelRxPowerTableSnmpKey.setStatus("current")
_CwsPmBasicCurrentChannelRxPowerActual_Type = Decimal3Dig
_CwsPmBasicCurrentChannelRxPowerActual_Object = MibTableColumn
cwsPmBasicCurrentChannelRxPowerActual = _CwsPmBasicCurrentChannelRxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 70, 1, 2),
    _CwsPmBasicCurrentChannelRxPowerActual_Type()
)
cwsPmBasicCurrentChannelRxPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentChannelRxPowerActual.setStatus("current")
_CwsPmBasicCurrentChannelRxPowerMinimum_Type = Decimal3Dig
_CwsPmBasicCurrentChannelRxPowerMinimum_Object = MibTableColumn
cwsPmBasicCurrentChannelRxPowerMinimum = _CwsPmBasicCurrentChannelRxPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 70, 1, 3),
    _CwsPmBasicCurrentChannelRxPowerMinimum_Type()
)
cwsPmBasicCurrentChannelRxPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentChannelRxPowerMinimum.setStatus("current")
_CwsPmBasicCurrentChannelRxPowerMaximum_Type = Decimal3Dig
_CwsPmBasicCurrentChannelRxPowerMaximum_Object = MibTableColumn
cwsPmBasicCurrentChannelRxPowerMaximum = _CwsPmBasicCurrentChannelRxPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 70, 1, 4),
    _CwsPmBasicCurrentChannelRxPowerMaximum_Type()
)
cwsPmBasicCurrentChannelRxPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentChannelRxPowerMaximum.setStatus("current")
_CwsPmBasicCurrentChannelRxPowerAverage_Type = Decimal3Dig
_CwsPmBasicCurrentChannelRxPowerAverage_Object = MibTableColumn
cwsPmBasicCurrentChannelRxPowerAverage = _CwsPmBasicCurrentChannelRxPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 70, 1, 5),
    _CwsPmBasicCurrentChannelRxPowerAverage_Type()
)
cwsPmBasicCurrentChannelRxPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrentChannelRxPowerAverage.setStatus("current")
_CwsPmBasicCurrent24hIdTable_Object = MibTable
cwsPmBasicCurrent24hIdTable = _CwsPmBasicCurrent24hIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 71)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hIdTable.setStatus("current")
_CwsPmBasicCurrent24hIdEntry_Object = MibTableRow
cwsPmBasicCurrent24hIdEntry = _CwsPmBasicCurrent24hIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 71, 1)
)
cwsPmBasicCurrent24hIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hIdEntry.setStatus("current")


class _CwsPmBasicCurrent24hIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrent24hIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrent24hIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrent24hIdTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrent24hIdTableSnmpKey = _CwsPmBasicCurrent24hIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 71, 1, 1),
    _CwsPmBasicCurrent24hIdTableSnmpKey_Type()
)
cwsPmBasicCurrent24hIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hIdTableSnmpKey.setStatus("current")
_CwsPmBasicCurrent24hIdBinNumber_Type = Unsigned32
_CwsPmBasicCurrent24hIdBinNumber_Object = MibTableColumn
cwsPmBasicCurrent24hIdBinNumber = _CwsPmBasicCurrent24hIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 71, 1, 2),
    _CwsPmBasicCurrent24hIdBinNumber_Type()
)
cwsPmBasicCurrent24hIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hIdBinNumber.setStatus("current")
_CwsPmBasicCurrent24hIdBinName_Type = StringMaxl32
_CwsPmBasicCurrent24hIdBinName_Object = MibTableColumn
cwsPmBasicCurrent24hIdBinName = _CwsPmBasicCurrent24hIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 71, 1, 3),
    _CwsPmBasicCurrent24hIdBinName_Type()
)
cwsPmBasicCurrent24hIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hIdBinName.setStatus("current")
_CwsPmBasicCurrent24hStateTable_Object = MibTable
cwsPmBasicCurrent24hStateTable = _CwsPmBasicCurrent24hStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 72)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hStateTable.setStatus("current")
_CwsPmBasicCurrent24hStateEntry_Object = MibTableRow
cwsPmBasicCurrent24hStateEntry = _CwsPmBasicCurrent24hStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 72, 1)
)
cwsPmBasicCurrent24hStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hStateEntry.setStatus("current")


class _CwsPmBasicCurrent24hStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrent24hStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrent24hStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrent24hStateTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrent24hStateTableSnmpKey = _CwsPmBasicCurrent24hStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 72, 1, 1),
    _CwsPmBasicCurrent24hStateTableSnmpKey_Type()
)
cwsPmBasicCurrent24hStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hStateTableSnmpKey.setStatus("current")
_CwsPmBasicCurrent24hStateStartDateTime_Type = StringMaxl32
_CwsPmBasicCurrent24hStateStartDateTime_Object = MibTableColumn
cwsPmBasicCurrent24hStateStartDateTime = _CwsPmBasicCurrent24hStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 72, 1, 2),
    _CwsPmBasicCurrent24hStateStartDateTime_Type()
)
cwsPmBasicCurrent24hStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hStateStartDateTime.setStatus("current")
_CwsPmBasicCurrent24hStateClearedDateTime_Type = StringMaxl32
_CwsPmBasicCurrent24hStateClearedDateTime_Object = MibTableColumn
cwsPmBasicCurrent24hStateClearedDateTime = _CwsPmBasicCurrent24hStateClearedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 72, 1, 3),
    _CwsPmBasicCurrent24hStateClearedDateTime_Type()
)
cwsPmBasicCurrent24hStateClearedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hStateClearedDateTime.setStatus("current")
_CwsPmBasicCurrent24hStateState_Type = PmBinState
_CwsPmBasicCurrent24hStateState_Object = MibTableColumn
cwsPmBasicCurrent24hStateState = _CwsPmBasicCurrent24hStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 72, 1, 4),
    _CwsPmBasicCurrent24hStateState_Type()
)
cwsPmBasicCurrent24hStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hStateState.setStatus("current")
_CwsPmBasicCurrent24hBinStatisticsTable_Object = MibTable
cwsPmBasicCurrent24hBinStatisticsTable = _CwsPmBasicCurrent24hBinStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 73)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hBinStatisticsTable.setStatus("current")
_CwsPmBasicCurrent24hBinStatisticsEntry_Object = MibTableRow
cwsPmBasicCurrent24hBinStatisticsEntry = _CwsPmBasicCurrent24hBinStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 73, 1)
)
cwsPmBasicCurrent24hBinStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hBinStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hBinStatisticsEntry.setStatus("current")


class _CwsPmBasicCurrent24hBinStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrent24hBinStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrent24hBinStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrent24hBinStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrent24hBinStatisticsTableSnmpKey = _CwsPmBasicCurrent24hBinStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 73, 1, 1),
    _CwsPmBasicCurrent24hBinStatisticsTableSnmpKey_Type()
)
cwsPmBasicCurrent24hBinStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hBinStatisticsTableSnmpKey.setStatus("current")
_CwsPmBasicCurrent24hBinStatisticsNumberOfChannels_Type = Unsigned32
_CwsPmBasicCurrent24hBinStatisticsNumberOfChannels_Object = MibTableColumn
cwsPmBasicCurrent24hBinStatisticsNumberOfChannels = _CwsPmBasicCurrent24hBinStatisticsNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 73, 1, 2),
    _CwsPmBasicCurrent24hBinStatisticsNumberOfChannels_Type()
)
cwsPmBasicCurrent24hBinStatisticsNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hBinStatisticsNumberOfChannels.setStatus("current")
_CwsPmBasicCurrent24hOpticalPowerTable_Object = MibTable
cwsPmBasicCurrent24hOpticalPowerTable = _CwsPmBasicCurrent24hOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 74)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hOpticalPowerTable.setStatus("current")
_CwsPmBasicCurrent24hOpticalPowerEntry_Object = MibTableRow
cwsPmBasicCurrent24hOpticalPowerEntry = _CwsPmBasicCurrent24hOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 74, 1)
)
cwsPmBasicCurrent24hOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hOpticalPowerChannelNumber"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hOpticalPowerEntry.setStatus("current")


class _CwsPmBasicCurrent24hOpticalPowerChannelNumber_Type(Integer32):
    """Custom type cwsPmBasicCurrent24hOpticalPowerChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrent24hOpticalPowerChannelNumber_Type.__name__ = "Integer32"
_CwsPmBasicCurrent24hOpticalPowerChannelNumber_Object = MibTableColumn
cwsPmBasicCurrent24hOpticalPowerChannelNumber = _CwsPmBasicCurrent24hOpticalPowerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 74, 1, 1),
    _CwsPmBasicCurrent24hOpticalPowerChannelNumber_Type()
)
cwsPmBasicCurrent24hOpticalPowerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hOpticalPowerChannelNumber.setStatus("current")
_CwsPmBasicCurrent24hRxOpticalPowerTable_Object = MibTable
cwsPmBasicCurrent24hRxOpticalPowerTable = _CwsPmBasicCurrent24hRxOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 75)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxOpticalPowerTable.setStatus("current")
_CwsPmBasicCurrent24hRxOpticalPowerEntry_Object = MibTableRow
cwsPmBasicCurrent24hRxOpticalPowerEntry = _CwsPmBasicCurrent24hRxOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 75, 1)
)
cwsPmBasicCurrent24hRxOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxOpticalPowerEntry.setStatus("current")


class _CwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey = _CwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 75, 1, 1),
    _CwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey_Type()
)
cwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey.setStatus("current")
_CwsPmBasicCurrent24hRxOpticalPowerActual_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxOpticalPowerActual_Object = MibTableColumn
cwsPmBasicCurrent24hRxOpticalPowerActual = _CwsPmBasicCurrent24hRxOpticalPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 75, 1, 2),
    _CwsPmBasicCurrent24hRxOpticalPowerActual_Type()
)
cwsPmBasicCurrent24hRxOpticalPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxOpticalPowerActual.setStatus("current")
_CwsPmBasicCurrent24hRxOpticalPowerMinimum_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxOpticalPowerMinimum_Object = MibTableColumn
cwsPmBasicCurrent24hRxOpticalPowerMinimum = _CwsPmBasicCurrent24hRxOpticalPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 75, 1, 3),
    _CwsPmBasicCurrent24hRxOpticalPowerMinimum_Type()
)
cwsPmBasicCurrent24hRxOpticalPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxOpticalPowerMinimum.setStatus("current")
_CwsPmBasicCurrent24hRxOpticalPowerMaximum_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxOpticalPowerMaximum_Object = MibTableColumn
cwsPmBasicCurrent24hRxOpticalPowerMaximum = _CwsPmBasicCurrent24hRxOpticalPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 75, 1, 4),
    _CwsPmBasicCurrent24hRxOpticalPowerMaximum_Type()
)
cwsPmBasicCurrent24hRxOpticalPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxOpticalPowerMaximum.setStatus("current")
_CwsPmBasicCurrent24hRxOpticalPowerAverage_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxOpticalPowerAverage_Object = MibTableColumn
cwsPmBasicCurrent24hRxOpticalPowerAverage = _CwsPmBasicCurrent24hRxOpticalPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 75, 1, 5),
    _CwsPmBasicCurrent24hRxOpticalPowerAverage_Type()
)
cwsPmBasicCurrent24hRxOpticalPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxOpticalPowerAverage.setStatus("current")
_CwsPmBasicCurrent24hTxOpticalPowerTable_Object = MibTable
cwsPmBasicCurrent24hTxOpticalPowerTable = _CwsPmBasicCurrent24hTxOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 76)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hTxOpticalPowerTable.setStatus("current")
_CwsPmBasicCurrent24hTxOpticalPowerEntry_Object = MibTableRow
cwsPmBasicCurrent24hTxOpticalPowerEntry = _CwsPmBasicCurrent24hTxOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 76, 1)
)
cwsPmBasicCurrent24hTxOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hTxOpticalPowerEntry.setStatus("current")


class _CwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey = _CwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 76, 1, 1),
    _CwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey_Type()
)
cwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey.setStatus("current")
_CwsPmBasicCurrent24hTxOpticalPowerActual_Type = Decimal3Dig
_CwsPmBasicCurrent24hTxOpticalPowerActual_Object = MibTableColumn
cwsPmBasicCurrent24hTxOpticalPowerActual = _CwsPmBasicCurrent24hTxOpticalPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 76, 1, 2),
    _CwsPmBasicCurrent24hTxOpticalPowerActual_Type()
)
cwsPmBasicCurrent24hTxOpticalPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hTxOpticalPowerActual.setStatus("current")
_CwsPmBasicCurrent24hTxOpticalPowerMinimum_Type = Decimal3Dig
_CwsPmBasicCurrent24hTxOpticalPowerMinimum_Object = MibTableColumn
cwsPmBasicCurrent24hTxOpticalPowerMinimum = _CwsPmBasicCurrent24hTxOpticalPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 76, 1, 3),
    _CwsPmBasicCurrent24hTxOpticalPowerMinimum_Type()
)
cwsPmBasicCurrent24hTxOpticalPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hTxOpticalPowerMinimum.setStatus("current")
_CwsPmBasicCurrent24hTxOpticalPowerMaximum_Type = Decimal3Dig
_CwsPmBasicCurrent24hTxOpticalPowerMaximum_Object = MibTableColumn
cwsPmBasicCurrent24hTxOpticalPowerMaximum = _CwsPmBasicCurrent24hTxOpticalPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 76, 1, 4),
    _CwsPmBasicCurrent24hTxOpticalPowerMaximum_Type()
)
cwsPmBasicCurrent24hTxOpticalPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hTxOpticalPowerMaximum.setStatus("current")
_CwsPmBasicCurrent24hTxOpticalPowerAverage_Type = Decimal3Dig
_CwsPmBasicCurrent24hTxOpticalPowerAverage_Object = MibTableColumn
cwsPmBasicCurrent24hTxOpticalPowerAverage = _CwsPmBasicCurrent24hTxOpticalPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 76, 1, 5),
    _CwsPmBasicCurrent24hTxOpticalPowerAverage_Type()
)
cwsPmBasicCurrent24hTxOpticalPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hTxOpticalPowerAverage.setStatus("current")
_CwsPmBasicCurrent24hRxChannelPowerTable_Object = MibTable
cwsPmBasicCurrent24hRxChannelPowerTable = _CwsPmBasicCurrent24hRxChannelPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 77)
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxChannelPowerTable.setStatus("current")
_CwsPmBasicCurrent24hRxChannelPowerEntry_Object = MibTableRow
cwsPmBasicCurrent24hRxChannelPowerEntry = _CwsPmBasicCurrent24hRxChannelPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 77, 1)
)
cwsPmBasicCurrent24hRxChannelPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxChannelPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxChannelPowerEntry.setStatus("current")


class _CwsPmBasicCurrent24hRxChannelPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicCurrent24hRxChannelPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicCurrent24hRxChannelPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicCurrent24hRxChannelPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicCurrent24hRxChannelPowerTableSnmpKey = _CwsPmBasicCurrent24hRxChannelPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 77, 1, 1),
    _CwsPmBasicCurrent24hRxChannelPowerTableSnmpKey_Type()
)
cwsPmBasicCurrent24hRxChannelPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxChannelPowerTableSnmpKey.setStatus("current")
_CwsPmBasicCurrent24hRxChannelPowerActual_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxChannelPowerActual_Object = MibTableColumn
cwsPmBasicCurrent24hRxChannelPowerActual = _CwsPmBasicCurrent24hRxChannelPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 77, 1, 2),
    _CwsPmBasicCurrent24hRxChannelPowerActual_Type()
)
cwsPmBasicCurrent24hRxChannelPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxChannelPowerActual.setStatus("current")
_CwsPmBasicCurrent24hRxChannelPowerMinimum_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxChannelPowerMinimum_Object = MibTableColumn
cwsPmBasicCurrent24hRxChannelPowerMinimum = _CwsPmBasicCurrent24hRxChannelPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 77, 1, 3),
    _CwsPmBasicCurrent24hRxChannelPowerMinimum_Type()
)
cwsPmBasicCurrent24hRxChannelPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxChannelPowerMinimum.setStatus("current")
_CwsPmBasicCurrent24hRxChannelPowerMaximum_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxChannelPowerMaximum_Object = MibTableColumn
cwsPmBasicCurrent24hRxChannelPowerMaximum = _CwsPmBasicCurrent24hRxChannelPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 77, 1, 4),
    _CwsPmBasicCurrent24hRxChannelPowerMaximum_Type()
)
cwsPmBasicCurrent24hRxChannelPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxChannelPowerMaximum.setStatus("current")
_CwsPmBasicCurrent24hRxChannelPowerAverage_Type = Decimal3Dig
_CwsPmBasicCurrent24hRxChannelPowerAverage_Object = MibTableColumn
cwsPmBasicCurrent24hRxChannelPowerAverage = _CwsPmBasicCurrent24hRxChannelPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 77, 1, 5),
    _CwsPmBasicCurrent24hRxChannelPowerAverage_Type()
)
cwsPmBasicCurrent24hRxChannelPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicCurrent24hRxChannelPowerAverage.setStatus("current")
_CwsPmBasicHistoryBinsTable_Object = MibTable
cwsPmBasicHistoryBinsTable = _CwsPmBasicHistoryBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 78)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryBinsTable.setStatus("current")
_CwsPmBasicHistoryBinsEntry_Object = MibTableRow
cwsPmBasicHistoryBinsEntry = _CwsPmBasicHistoryBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 78, 1)
)
cwsPmBasicHistoryBinsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryBinsEntry.setStatus("current")


class _CwsPmBasicHistoryBinsBinNumber_Type(Integer32):
    """Custom type cwsPmBasicHistoryBinsBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistoryBinsBinNumber_Type.__name__ = "Integer32"
_CwsPmBasicHistoryBinsBinNumber_Object = MibTableColumn
cwsPmBasicHistoryBinsBinNumber = _CwsPmBasicHistoryBinsBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 78, 1, 1),
    _CwsPmBasicHistoryBinsBinNumber_Type()
)
cwsPmBasicHistoryBinsBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryBinsBinNumber.setStatus("current")
_CwsPmBasicHistoryStateTable_Object = MibTable
cwsPmBasicHistoryStateTable = _CwsPmBasicHistoryStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 79)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStateTable.setStatus("current")
_CwsPmBasicHistoryStateEntry_Object = MibTableRow
cwsPmBasicHistoryStateEntry = _CwsPmBasicHistoryStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 79, 1)
)
cwsPmBasicHistoryStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStateEntry.setStatus("current")


class _CwsPmBasicHistoryStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistoryStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistoryStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistoryStateTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistoryStateTableSnmpKey = _CwsPmBasicHistoryStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 79, 1, 1),
    _CwsPmBasicHistoryStateTableSnmpKey_Type()
)
cwsPmBasicHistoryStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStateTableSnmpKey.setStatus("current")
_CwsPmBasicHistoryStateStartDateTime_Type = StringMaxl32
_CwsPmBasicHistoryStateStartDateTime_Object = MibTableColumn
cwsPmBasicHistoryStateStartDateTime = _CwsPmBasicHistoryStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 79, 1, 2),
    _CwsPmBasicHistoryStateStartDateTime_Type()
)
cwsPmBasicHistoryStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStateStartDateTime.setStatus("current")
_CwsPmBasicHistoryStateEndDateTime_Type = StringMaxl32
_CwsPmBasicHistoryStateEndDateTime_Object = MibTableColumn
cwsPmBasicHistoryStateEndDateTime = _CwsPmBasicHistoryStateEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 79, 1, 3),
    _CwsPmBasicHistoryStateEndDateTime_Type()
)
cwsPmBasicHistoryStateEndDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStateEndDateTime.setStatus("current")
_CwsPmBasicHistoryStateState_Type = PmBinState
_CwsPmBasicHistoryStateState_Object = MibTableColumn
cwsPmBasicHistoryStateState = _CwsPmBasicHistoryStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 79, 1, 4),
    _CwsPmBasicHistoryStateState_Type()
)
cwsPmBasicHistoryStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStateState.setStatus("current")
_CwsPmBasicHistoryStatisticsTable_Object = MibTable
cwsPmBasicHistoryStatisticsTable = _CwsPmBasicHistoryStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 80)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStatisticsTable.setStatus("current")
_CwsPmBasicHistoryStatisticsEntry_Object = MibTableRow
cwsPmBasicHistoryStatisticsEntry = _CwsPmBasicHistoryStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 80, 1)
)
cwsPmBasicHistoryStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStatisticsEntry.setStatus("current")


class _CwsPmBasicHistoryStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistoryStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistoryStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistoryStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistoryStatisticsTableSnmpKey = _CwsPmBasicHistoryStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 80, 1, 1),
    _CwsPmBasicHistoryStatisticsTableSnmpKey_Type()
)
cwsPmBasicHistoryStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStatisticsTableSnmpKey.setStatus("current")
_CwsPmBasicHistoryStatisticsNumberOfChannels_Type = Unsigned32
_CwsPmBasicHistoryStatisticsNumberOfChannels_Object = MibTableColumn
cwsPmBasicHistoryStatisticsNumberOfChannels = _CwsPmBasicHistoryStatisticsNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 80, 1, 2),
    _CwsPmBasicHistoryStatisticsNumberOfChannels_Type()
)
cwsPmBasicHistoryStatisticsNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryStatisticsNumberOfChannels.setStatus("current")
_CwsPmBasicHistoryOpticalPowerTable_Object = MibTable
cwsPmBasicHistoryOpticalPowerTable = _CwsPmBasicHistoryOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 81)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryOpticalPowerTable.setStatus("current")
_CwsPmBasicHistoryOpticalPowerEntry_Object = MibTableRow
cwsPmBasicHistoryOpticalPowerEntry = _CwsPmBasicHistoryOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 81, 1)
)
cwsPmBasicHistoryOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryOpticalPowerChannelNumber"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryOpticalPowerEntry.setStatus("current")


class _CwsPmBasicHistoryOpticalPowerChannelNumber_Type(Integer32):
    """Custom type cwsPmBasicHistoryOpticalPowerChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistoryOpticalPowerChannelNumber_Type.__name__ = "Integer32"
_CwsPmBasicHistoryOpticalPowerChannelNumber_Object = MibTableColumn
cwsPmBasicHistoryOpticalPowerChannelNumber = _CwsPmBasicHistoryOpticalPowerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 81, 1, 1),
    _CwsPmBasicHistoryOpticalPowerChannelNumber_Type()
)
cwsPmBasicHistoryOpticalPowerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryOpticalPowerChannelNumber.setStatus("current")
_CwsPmBasicHistoryRxOpticalPowerTable_Object = MibTable
cwsPmBasicHistoryRxOpticalPowerTable = _CwsPmBasicHistoryRxOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 82)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryRxOpticalPowerTable.setStatus("current")
_CwsPmBasicHistoryRxOpticalPowerEntry_Object = MibTableRow
cwsPmBasicHistoryRxOpticalPowerEntry = _CwsPmBasicHistoryRxOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 82, 1)
)
cwsPmBasicHistoryRxOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryRxOpticalPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryRxOpticalPowerEntry.setStatus("current")


class _CwsPmBasicHistoryRxOpticalPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistoryRxOpticalPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistoryRxOpticalPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistoryRxOpticalPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistoryRxOpticalPowerTableSnmpKey = _CwsPmBasicHistoryRxOpticalPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 82, 1, 1),
    _CwsPmBasicHistoryRxOpticalPowerTableSnmpKey_Type()
)
cwsPmBasicHistoryRxOpticalPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryRxOpticalPowerTableSnmpKey.setStatus("current")
_CwsPmBasicHistoryRxOpticalPowerActual_Type = Decimal3Dig
_CwsPmBasicHistoryRxOpticalPowerActual_Object = MibTableColumn
cwsPmBasicHistoryRxOpticalPowerActual = _CwsPmBasicHistoryRxOpticalPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 82, 1, 2),
    _CwsPmBasicHistoryRxOpticalPowerActual_Type()
)
cwsPmBasicHistoryRxOpticalPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryRxOpticalPowerActual.setStatus("current")
_CwsPmBasicHistoryRxOpticalPowerMinimum_Type = Decimal3Dig
_CwsPmBasicHistoryRxOpticalPowerMinimum_Object = MibTableColumn
cwsPmBasicHistoryRxOpticalPowerMinimum = _CwsPmBasicHistoryRxOpticalPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 82, 1, 3),
    _CwsPmBasicHistoryRxOpticalPowerMinimum_Type()
)
cwsPmBasicHistoryRxOpticalPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryRxOpticalPowerMinimum.setStatus("current")
_CwsPmBasicHistoryRxOpticalPowerMaximum_Type = Decimal3Dig
_CwsPmBasicHistoryRxOpticalPowerMaximum_Object = MibTableColumn
cwsPmBasicHistoryRxOpticalPowerMaximum = _CwsPmBasicHistoryRxOpticalPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 82, 1, 4),
    _CwsPmBasicHistoryRxOpticalPowerMaximum_Type()
)
cwsPmBasicHistoryRxOpticalPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryRxOpticalPowerMaximum.setStatus("current")
_CwsPmBasicHistoryRxOpticalPowerAverage_Type = Decimal3Dig
_CwsPmBasicHistoryRxOpticalPowerAverage_Object = MibTableColumn
cwsPmBasicHistoryRxOpticalPowerAverage = _CwsPmBasicHistoryRxOpticalPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 82, 1, 5),
    _CwsPmBasicHistoryRxOpticalPowerAverage_Type()
)
cwsPmBasicHistoryRxOpticalPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryRxOpticalPowerAverage.setStatus("current")
_CwsPmBasicHistoryTxOpticalPowerTable_Object = MibTable
cwsPmBasicHistoryTxOpticalPowerTable = _CwsPmBasicHistoryTxOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 83)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxOpticalPowerTable.setStatus("current")
_CwsPmBasicHistoryTxOpticalPowerEntry_Object = MibTableRow
cwsPmBasicHistoryTxOpticalPowerEntry = _CwsPmBasicHistoryTxOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 83, 1)
)
cwsPmBasicHistoryTxOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxOpticalPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxOpticalPowerEntry.setStatus("current")


class _CwsPmBasicHistoryTxOpticalPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistoryTxOpticalPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistoryTxOpticalPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistoryTxOpticalPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistoryTxOpticalPowerTableSnmpKey = _CwsPmBasicHistoryTxOpticalPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 83, 1, 1),
    _CwsPmBasicHistoryTxOpticalPowerTableSnmpKey_Type()
)
cwsPmBasicHistoryTxOpticalPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxOpticalPowerTableSnmpKey.setStatus("current")
_CwsPmBasicHistoryTxOpticalPowerActual_Type = Decimal3Dig
_CwsPmBasicHistoryTxOpticalPowerActual_Object = MibTableColumn
cwsPmBasicHistoryTxOpticalPowerActual = _CwsPmBasicHistoryTxOpticalPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 83, 1, 2),
    _CwsPmBasicHistoryTxOpticalPowerActual_Type()
)
cwsPmBasicHistoryTxOpticalPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxOpticalPowerActual.setStatus("current")
_CwsPmBasicHistoryTxOpticalPowerMinimum_Type = Decimal3Dig
_CwsPmBasicHistoryTxOpticalPowerMinimum_Object = MibTableColumn
cwsPmBasicHistoryTxOpticalPowerMinimum = _CwsPmBasicHistoryTxOpticalPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 83, 1, 3),
    _CwsPmBasicHistoryTxOpticalPowerMinimum_Type()
)
cwsPmBasicHistoryTxOpticalPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxOpticalPowerMinimum.setStatus("current")
_CwsPmBasicHistoryTxOpticalPowerMaximum_Type = Decimal3Dig
_CwsPmBasicHistoryTxOpticalPowerMaximum_Object = MibTableColumn
cwsPmBasicHistoryTxOpticalPowerMaximum = _CwsPmBasicHistoryTxOpticalPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 83, 1, 4),
    _CwsPmBasicHistoryTxOpticalPowerMaximum_Type()
)
cwsPmBasicHistoryTxOpticalPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxOpticalPowerMaximum.setStatus("current")
_CwsPmBasicHistoryTxOpticalPowerAverage_Type = Decimal3Dig
_CwsPmBasicHistoryTxOpticalPowerAverage_Object = MibTableColumn
cwsPmBasicHistoryTxOpticalPowerAverage = _CwsPmBasicHistoryTxOpticalPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 83, 1, 5),
    _CwsPmBasicHistoryTxOpticalPowerAverage_Type()
)
cwsPmBasicHistoryTxOpticalPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxOpticalPowerAverage.setStatus("current")
_CwsPmBasicHistoryTxChannelPowerTable_Object = MibTable
cwsPmBasicHistoryTxChannelPowerTable = _CwsPmBasicHistoryTxChannelPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 84)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxChannelPowerTable.setStatus("current")
_CwsPmBasicHistoryTxChannelPowerEntry_Object = MibTableRow
cwsPmBasicHistoryTxChannelPowerEntry = _CwsPmBasicHistoryTxChannelPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 84, 1)
)
cwsPmBasicHistoryTxChannelPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxChannelPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxChannelPowerEntry.setStatus("current")


class _CwsPmBasicHistoryTxChannelPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistoryTxChannelPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistoryTxChannelPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistoryTxChannelPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistoryTxChannelPowerTableSnmpKey = _CwsPmBasicHistoryTxChannelPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 84, 1, 1),
    _CwsPmBasicHistoryTxChannelPowerTableSnmpKey_Type()
)
cwsPmBasicHistoryTxChannelPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxChannelPowerTableSnmpKey.setStatus("current")
_CwsPmBasicHistoryTxChannelPowerActual_Type = Decimal3Dig
_CwsPmBasicHistoryTxChannelPowerActual_Object = MibTableColumn
cwsPmBasicHistoryTxChannelPowerActual = _CwsPmBasicHistoryTxChannelPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 84, 1, 2),
    _CwsPmBasicHistoryTxChannelPowerActual_Type()
)
cwsPmBasicHistoryTxChannelPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxChannelPowerActual.setStatus("current")
_CwsPmBasicHistoryTxChannelPowerMinimum_Type = Decimal3Dig
_CwsPmBasicHistoryTxChannelPowerMinimum_Object = MibTableColumn
cwsPmBasicHistoryTxChannelPowerMinimum = _CwsPmBasicHistoryTxChannelPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 84, 1, 3),
    _CwsPmBasicHistoryTxChannelPowerMinimum_Type()
)
cwsPmBasicHistoryTxChannelPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxChannelPowerMinimum.setStatus("current")
_CwsPmBasicHistoryTxChannelPowerMaximum_Type = Decimal3Dig
_CwsPmBasicHistoryTxChannelPowerMaximum_Object = MibTableColumn
cwsPmBasicHistoryTxChannelPowerMaximum = _CwsPmBasicHistoryTxChannelPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 84, 1, 4),
    _CwsPmBasicHistoryTxChannelPowerMaximum_Type()
)
cwsPmBasicHistoryTxChannelPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxChannelPowerMaximum.setStatus("current")
_CwsPmBasicHistoryTxChannelPowerAverage_Type = Decimal3Dig
_CwsPmBasicHistoryTxChannelPowerAverage_Object = MibTableColumn
cwsPmBasicHistoryTxChannelPowerAverage = _CwsPmBasicHistoryTxChannelPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 84, 1, 5),
    _CwsPmBasicHistoryTxChannelPowerAverage_Type()
)
cwsPmBasicHistoryTxChannelPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistoryTxChannelPowerAverage.setStatus("current")
_CwsPmBasicHistory24hIdTable_Object = MibTable
cwsPmBasicHistory24hIdTable = _CwsPmBasicHistory24hIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 85)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hIdTable.setStatus("current")
_CwsPmBasicHistory24hIdEntry_Object = MibTableRow
cwsPmBasicHistory24hIdEntry = _CwsPmBasicHistory24hIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 85, 1)
)
cwsPmBasicHistory24hIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hIdEntry.setStatus("current")


class _CwsPmBasicHistory24hIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistory24hIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistory24hIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistory24hIdTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistory24hIdTableSnmpKey = _CwsPmBasicHistory24hIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 85, 1, 1),
    _CwsPmBasicHistory24hIdTableSnmpKey_Type()
)
cwsPmBasicHistory24hIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hIdTableSnmpKey.setStatus("current")
_CwsPmBasicHistory24hIdBinNumber_Type = Unsigned32
_CwsPmBasicHistory24hIdBinNumber_Object = MibTableColumn
cwsPmBasicHistory24hIdBinNumber = _CwsPmBasicHistory24hIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 85, 1, 2),
    _CwsPmBasicHistory24hIdBinNumber_Type()
)
cwsPmBasicHistory24hIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hIdBinNumber.setStatus("current")
_CwsPmBasicHistory24hIdBinName_Type = StringMaxl32
_CwsPmBasicHistory24hIdBinName_Object = MibTableColumn
cwsPmBasicHistory24hIdBinName = _CwsPmBasicHistory24hIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 85, 1, 3),
    _CwsPmBasicHistory24hIdBinName_Type()
)
cwsPmBasicHistory24hIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hIdBinName.setStatus("current")
_CwsPmBasicHistory24hStateTable_Object = MibTable
cwsPmBasicHistory24hStateTable = _CwsPmBasicHistory24hStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 86)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStateTable.setStatus("current")
_CwsPmBasicHistory24hStateEntry_Object = MibTableRow
cwsPmBasicHistory24hStateEntry = _CwsPmBasicHistory24hStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 86, 1)
)
cwsPmBasicHistory24hStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStateEntry.setStatus("current")


class _CwsPmBasicHistory24hStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistory24hStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistory24hStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistory24hStateTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistory24hStateTableSnmpKey = _CwsPmBasicHistory24hStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 86, 1, 1),
    _CwsPmBasicHistory24hStateTableSnmpKey_Type()
)
cwsPmBasicHistory24hStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStateTableSnmpKey.setStatus("current")
_CwsPmBasicHistory24hStateStartDateTime_Type = StringMaxl32
_CwsPmBasicHistory24hStateStartDateTime_Object = MibTableColumn
cwsPmBasicHistory24hStateStartDateTime = _CwsPmBasicHistory24hStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 86, 1, 2),
    _CwsPmBasicHistory24hStateStartDateTime_Type()
)
cwsPmBasicHistory24hStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStateStartDateTime.setStatus("current")
_CwsPmBasicHistory24hStateEndDateTime_Type = StringMaxl32
_CwsPmBasicHistory24hStateEndDateTime_Object = MibTableColumn
cwsPmBasicHistory24hStateEndDateTime = _CwsPmBasicHistory24hStateEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 86, 1, 3),
    _CwsPmBasicHistory24hStateEndDateTime_Type()
)
cwsPmBasicHistory24hStateEndDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStateEndDateTime.setStatus("current")
_CwsPmBasicHistory24hStateState_Type = PmBinState
_CwsPmBasicHistory24hStateState_Object = MibTableColumn
cwsPmBasicHistory24hStateState = _CwsPmBasicHistory24hStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 86, 1, 4),
    _CwsPmBasicHistory24hStateState_Type()
)
cwsPmBasicHistory24hStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStateState.setStatus("current")
_CwsPmBasicHistory24hStatisticsTable_Object = MibTable
cwsPmBasicHistory24hStatisticsTable = _CwsPmBasicHistory24hStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 87)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStatisticsTable.setStatus("current")
_CwsPmBasicHistory24hStatisticsEntry_Object = MibTableRow
cwsPmBasicHistory24hStatisticsEntry = _CwsPmBasicHistory24hStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 87, 1)
)
cwsPmBasicHistory24hStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStatisticsEntry.setStatus("current")


class _CwsPmBasicHistory24hStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistory24hStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistory24hStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistory24hStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistory24hStatisticsTableSnmpKey = _CwsPmBasicHistory24hStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 87, 1, 1),
    _CwsPmBasicHistory24hStatisticsTableSnmpKey_Type()
)
cwsPmBasicHistory24hStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStatisticsTableSnmpKey.setStatus("current")
_CwsPmBasicHistory24hStatisticsNumberOfChannels_Type = Unsigned32
_CwsPmBasicHistory24hStatisticsNumberOfChannels_Object = MibTableColumn
cwsPmBasicHistory24hStatisticsNumberOfChannels = _CwsPmBasicHistory24hStatisticsNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 87, 1, 2),
    _CwsPmBasicHistory24hStatisticsNumberOfChannels_Type()
)
cwsPmBasicHistory24hStatisticsNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hStatisticsNumberOfChannels.setStatus("current")
_CwsPmBasicHistory24hOpticalPowerTable_Object = MibTable
cwsPmBasicHistory24hOpticalPowerTable = _CwsPmBasicHistory24hOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 88)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hOpticalPowerTable.setStatus("current")
_CwsPmBasicHistory24hOpticalPowerEntry_Object = MibTableRow
cwsPmBasicHistory24hOpticalPowerEntry = _CwsPmBasicHistory24hOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 88, 1)
)
cwsPmBasicHistory24hOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hOpticalPowerChannelNumber"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hOpticalPowerEntry.setStatus("current")


class _CwsPmBasicHistory24hOpticalPowerChannelNumber_Type(Integer32):
    """Custom type cwsPmBasicHistory24hOpticalPowerChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistory24hOpticalPowerChannelNumber_Type.__name__ = "Integer32"
_CwsPmBasicHistory24hOpticalPowerChannelNumber_Object = MibTableColumn
cwsPmBasicHistory24hOpticalPowerChannelNumber = _CwsPmBasicHistory24hOpticalPowerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 88, 1, 1),
    _CwsPmBasicHistory24hOpticalPowerChannelNumber_Type()
)
cwsPmBasicHistory24hOpticalPowerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hOpticalPowerChannelNumber.setStatus("current")
_CwsPmBasicHistory24hRxOpticalPowerTable_Object = MibTable
cwsPmBasicHistory24hRxOpticalPowerTable = _CwsPmBasicHistory24hRxOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 89)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxOpticalPowerTable.setStatus("current")
_CwsPmBasicHistory24hRxOpticalPowerEntry_Object = MibTableRow
cwsPmBasicHistory24hRxOpticalPowerEntry = _CwsPmBasicHistory24hRxOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 89, 1)
)
cwsPmBasicHistory24hRxOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxOpticalPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxOpticalPowerEntry.setStatus("current")


class _CwsPmBasicHistory24hRxOpticalPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistory24hRxOpticalPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistory24hRxOpticalPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistory24hRxOpticalPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistory24hRxOpticalPowerTableSnmpKey = _CwsPmBasicHistory24hRxOpticalPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 89, 1, 1),
    _CwsPmBasicHistory24hRxOpticalPowerTableSnmpKey_Type()
)
cwsPmBasicHistory24hRxOpticalPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxOpticalPowerTableSnmpKey.setStatus("current")
_CwsPmBasicHistory24hRxOpticalPowerActual_Type = Decimal3Dig
_CwsPmBasicHistory24hRxOpticalPowerActual_Object = MibTableColumn
cwsPmBasicHistory24hRxOpticalPowerActual = _CwsPmBasicHistory24hRxOpticalPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 89, 1, 2),
    _CwsPmBasicHistory24hRxOpticalPowerActual_Type()
)
cwsPmBasicHistory24hRxOpticalPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxOpticalPowerActual.setStatus("current")
_CwsPmBasicHistory24hRxOpticalPowerMinimum_Type = Decimal3Dig
_CwsPmBasicHistory24hRxOpticalPowerMinimum_Object = MibTableColumn
cwsPmBasicHistory24hRxOpticalPowerMinimum = _CwsPmBasicHistory24hRxOpticalPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 89, 1, 3),
    _CwsPmBasicHistory24hRxOpticalPowerMinimum_Type()
)
cwsPmBasicHistory24hRxOpticalPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxOpticalPowerMinimum.setStatus("current")
_CwsPmBasicHistory24hRxOpticalPowerMaximum_Type = Decimal3Dig
_CwsPmBasicHistory24hRxOpticalPowerMaximum_Object = MibTableColumn
cwsPmBasicHistory24hRxOpticalPowerMaximum = _CwsPmBasicHistory24hRxOpticalPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 89, 1, 4),
    _CwsPmBasicHistory24hRxOpticalPowerMaximum_Type()
)
cwsPmBasicHistory24hRxOpticalPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxOpticalPowerMaximum.setStatus("current")
_CwsPmBasicHistory24hRxOpticalPowerAverage_Type = Decimal3Dig
_CwsPmBasicHistory24hRxOpticalPowerAverage_Object = MibTableColumn
cwsPmBasicHistory24hRxOpticalPowerAverage = _CwsPmBasicHistory24hRxOpticalPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 89, 1, 5),
    _CwsPmBasicHistory24hRxOpticalPowerAverage_Type()
)
cwsPmBasicHistory24hRxOpticalPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxOpticalPowerAverage.setStatus("current")
_CwsPmBasicHistory24hTxOpticalPowerTable_Object = MibTable
cwsPmBasicHistory24hTxOpticalPowerTable = _CwsPmBasicHistory24hTxOpticalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 90)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hTxOpticalPowerTable.setStatus("current")
_CwsPmBasicHistory24hTxOpticalPowerEntry_Object = MibTableRow
cwsPmBasicHistory24hTxOpticalPowerEntry = _CwsPmBasicHistory24hTxOpticalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 90, 1)
)
cwsPmBasicHistory24hTxOpticalPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hOpticalPowerChannelNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hTxOpticalPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hTxOpticalPowerEntry.setStatus("current")


class _CwsPmBasicHistory24hTxOpticalPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistory24hTxOpticalPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistory24hTxOpticalPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistory24hTxOpticalPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistory24hTxOpticalPowerTableSnmpKey = _CwsPmBasicHistory24hTxOpticalPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 90, 1, 1),
    _CwsPmBasicHistory24hTxOpticalPowerTableSnmpKey_Type()
)
cwsPmBasicHistory24hTxOpticalPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hTxOpticalPowerTableSnmpKey.setStatus("current")
_CwsPmBasicHistory24hTxOpticalPowerActual_Type = Decimal3Dig
_CwsPmBasicHistory24hTxOpticalPowerActual_Object = MibTableColumn
cwsPmBasicHistory24hTxOpticalPowerActual = _CwsPmBasicHistory24hTxOpticalPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 90, 1, 2),
    _CwsPmBasicHistory24hTxOpticalPowerActual_Type()
)
cwsPmBasicHistory24hTxOpticalPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hTxOpticalPowerActual.setStatus("current")
_CwsPmBasicHistory24hTxOpticalPowerMinimum_Type = Decimal3Dig
_CwsPmBasicHistory24hTxOpticalPowerMinimum_Object = MibTableColumn
cwsPmBasicHistory24hTxOpticalPowerMinimum = _CwsPmBasicHistory24hTxOpticalPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 90, 1, 3),
    _CwsPmBasicHistory24hTxOpticalPowerMinimum_Type()
)
cwsPmBasicHistory24hTxOpticalPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hTxOpticalPowerMinimum.setStatus("current")
_CwsPmBasicHistory24hTxOpticalPowerMaximum_Type = Decimal3Dig
_CwsPmBasicHistory24hTxOpticalPowerMaximum_Object = MibTableColumn
cwsPmBasicHistory24hTxOpticalPowerMaximum = _CwsPmBasicHistory24hTxOpticalPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 90, 1, 4),
    _CwsPmBasicHistory24hTxOpticalPowerMaximum_Type()
)
cwsPmBasicHistory24hTxOpticalPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hTxOpticalPowerMaximum.setStatus("current")
_CwsPmBasicHistory24hTxOpticalPowerAverage_Type = Decimal3Dig
_CwsPmBasicHistory24hTxOpticalPowerAverage_Object = MibTableColumn
cwsPmBasicHistory24hTxOpticalPowerAverage = _CwsPmBasicHistory24hTxOpticalPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 90, 1, 5),
    _CwsPmBasicHistory24hTxOpticalPowerAverage_Type()
)
cwsPmBasicHistory24hTxOpticalPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hTxOpticalPowerAverage.setStatus("current")
_CwsPmBasicHistory24hRxChannelPowerTable_Object = MibTable
cwsPmBasicHistory24hRxChannelPowerTable = _CwsPmBasicHistory24hRxChannelPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 91)
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxChannelPowerTable.setStatus("current")
_CwsPmBasicHistory24hRxChannelPowerEntry_Object = MibTableRow
cwsPmBasicHistory24hRxChannelPowerEntry = _CwsPmBasicHistory24hRxChannelPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 91, 1)
)
cwsPmBasicHistory24hRxChannelPowerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxChannelPowerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxChannelPowerEntry.setStatus("current")


class _CwsPmBasicHistory24hRxChannelPowerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmBasicHistory24hRxChannelPowerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmBasicHistory24hRxChannelPowerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmBasicHistory24hRxChannelPowerTableSnmpKey_Object = MibTableColumn
cwsPmBasicHistory24hRxChannelPowerTableSnmpKey = _CwsPmBasicHistory24hRxChannelPowerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 91, 1, 1),
    _CwsPmBasicHistory24hRxChannelPowerTableSnmpKey_Type()
)
cwsPmBasicHistory24hRxChannelPowerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxChannelPowerTableSnmpKey.setStatus("current")
_CwsPmBasicHistory24hRxChannelPowerActual_Type = Decimal3Dig
_CwsPmBasicHistory24hRxChannelPowerActual_Object = MibTableColumn
cwsPmBasicHistory24hRxChannelPowerActual = _CwsPmBasicHistory24hRxChannelPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 91, 1, 2),
    _CwsPmBasicHistory24hRxChannelPowerActual_Type()
)
cwsPmBasicHistory24hRxChannelPowerActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxChannelPowerActual.setStatus("current")
_CwsPmBasicHistory24hRxChannelPowerMinimum_Type = Decimal3Dig
_CwsPmBasicHistory24hRxChannelPowerMinimum_Object = MibTableColumn
cwsPmBasicHistory24hRxChannelPowerMinimum = _CwsPmBasicHistory24hRxChannelPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 91, 1, 3),
    _CwsPmBasicHistory24hRxChannelPowerMinimum_Type()
)
cwsPmBasicHistory24hRxChannelPowerMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxChannelPowerMinimum.setStatus("current")
_CwsPmBasicHistory24hRxChannelPowerMaximum_Type = Decimal3Dig
_CwsPmBasicHistory24hRxChannelPowerMaximum_Object = MibTableColumn
cwsPmBasicHistory24hRxChannelPowerMaximum = _CwsPmBasicHistory24hRxChannelPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 91, 1, 4),
    _CwsPmBasicHistory24hRxChannelPowerMaximum_Type()
)
cwsPmBasicHistory24hRxChannelPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxChannelPowerMaximum.setStatus("current")
_CwsPmBasicHistory24hRxChannelPowerAverage_Type = Decimal3Dig
_CwsPmBasicHistory24hRxChannelPowerAverage_Object = MibTableColumn
cwsPmBasicHistory24hRxChannelPowerAverage = _CwsPmBasicHistory24hRxChannelPowerAverage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 91, 1, 5),
    _CwsPmBasicHistory24hRxChannelPowerAverage_Type()
)
cwsPmBasicHistory24hRxChannelPowerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmBasicHistory24hRxChannelPowerAverage.setStatus("current")
_CwsPmPtpAdvancedInstancesTable_Object = MibTable
cwsPmPtpAdvancedInstancesTable = _CwsPmPtpAdvancedInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 92)
)
if mibBuilder.loadTexts:
    cwsPmPtpAdvancedInstancesTable.setStatus("current")
_CwsPmPtpAdvancedInstancesEntry_Object = MibTableRow
cwsPmPtpAdvancedInstancesEntry = _CwsPmPtpAdvancedInstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 92, 1)
)
cwsPmPtpAdvancedInstancesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
)
if mibBuilder.loadTexts:
    cwsPmPtpAdvancedInstancesEntry.setStatus("current")


class _CwsPmPtpAdvancedInstancesInstanceName_Type(Integer32):
    """Custom type cwsPmPtpAdvancedInstancesInstanceName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmPtpAdvancedInstancesInstanceName_Type.__name__ = "Integer32"
_CwsPmPtpAdvancedInstancesInstanceName_Object = MibTableColumn
cwsPmPtpAdvancedInstancesInstanceName = _CwsPmPtpAdvancedInstancesInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 92, 1, 1),
    _CwsPmPtpAdvancedInstancesInstanceName_Type()
)
cwsPmPtpAdvancedInstancesInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmPtpAdvancedInstancesInstanceName.setStatus("current")
_CwsPmAdvancedIdTable_Object = MibTable
cwsPmAdvancedIdTable = _CwsPmAdvancedIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 93)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedIdTable.setStatus("current")
_CwsPmAdvancedIdEntry_Object = MibTableRow
cwsPmAdvancedIdEntry = _CwsPmAdvancedIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 93, 1)
)
cwsPmAdvancedIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedIdEntry.setStatus("current")


class _CwsPmAdvancedIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedIdTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedIdTableSnmpKey = _CwsPmAdvancedIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 93, 1, 1),
    _CwsPmAdvancedIdTableSnmpKey_Type()
)
cwsPmAdvancedIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedIdTableSnmpKey.setStatus("current")
_CwsPmAdvancedIdInstanceId_Type = Unsigned32
_CwsPmAdvancedIdInstanceId_Object = MibTableColumn
cwsPmAdvancedIdInstanceId = _CwsPmAdvancedIdInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 93, 1, 2),
    _CwsPmAdvancedIdInstanceId_Type()
)
cwsPmAdvancedIdInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedIdInstanceId.setStatus("current")
_CwsPmAdvancedIdInstanceType_Type = PmInstanceType
_CwsPmAdvancedIdInstanceType_Object = MibTableColumn
cwsPmAdvancedIdInstanceType = _CwsPmAdvancedIdInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 93, 1, 3),
    _CwsPmAdvancedIdInstanceType_Type()
)
cwsPmAdvancedIdInstanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedIdInstanceType.setStatus("current")
_CwsPmAdvancedIdProfileType_Type = PmProfileType
_CwsPmAdvancedIdProfileType_Object = MibTableColumn
cwsPmAdvancedIdProfileType = _CwsPmAdvancedIdProfileType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 93, 1, 4),
    _CwsPmAdvancedIdProfileType_Type()
)
cwsPmAdvancedIdProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedIdProfileType.setStatus("current")
_CwsPmAdvancedStateTable_Object = MibTable
cwsPmAdvancedStateTable = _CwsPmAdvancedStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedStateTable.setStatus("current")
_CwsPmAdvancedStateEntry_Object = MibTableRow
cwsPmAdvancedStateEntry = _CwsPmAdvancedStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94, 1)
)
cwsPmAdvancedStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedStateEntry.setStatus("current")


class _CwsPmAdvancedStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedStateTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedStateTableSnmpKey = _CwsPmAdvancedStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94, 1, 1),
    _CwsPmAdvancedStateTableSnmpKey_Type()
)
cwsPmAdvancedStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedStateTableSnmpKey.setStatus("current")
_CwsPmAdvancedStateAdminState_Type = EnabledDisabledEnum
_CwsPmAdvancedStateAdminState_Object = MibTableColumn
cwsPmAdvancedStateAdminState = _CwsPmAdvancedStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94, 1, 2),
    _CwsPmAdvancedStateAdminState_Type()
)
cwsPmAdvancedStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedStateAdminState.setStatus("current")
_CwsPmAdvancedStateOperationalState_Type = EnabledDisabledEnum
_CwsPmAdvancedStateOperationalState_Object = MibTableColumn
cwsPmAdvancedStateOperationalState = _CwsPmAdvancedStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94, 1, 3),
    _CwsPmAdvancedStateOperationalState_Type()
)
cwsPmAdvancedStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedStateOperationalState.setStatus("current")
_CwsPmAdvancedStateCurrentBinId_Type = Unsigned32
_CwsPmAdvancedStateCurrentBinId_Object = MibTableColumn
cwsPmAdvancedStateCurrentBinId = _CwsPmAdvancedStateCurrentBinId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94, 1, 4),
    _CwsPmAdvancedStateCurrentBinId_Type()
)
cwsPmAdvancedStateCurrentBinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedStateCurrentBinId.setStatus("current")
_CwsPmAdvancedStateCollectionStartDateTime_Type = StringMaxl64
_CwsPmAdvancedStateCollectionStartDateTime_Object = MibTableColumn
cwsPmAdvancedStateCollectionStartDateTime = _CwsPmAdvancedStateCollectionStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94, 1, 5),
    _CwsPmAdvancedStateCollectionStartDateTime_Type()
)
cwsPmAdvancedStateCollectionStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedStateCollectionStartDateTime.setStatus("current")
_CwsPmAdvancedStateCollectionEndDateTime_Type = StringMaxl64
_CwsPmAdvancedStateCollectionEndDateTime_Object = MibTableColumn
cwsPmAdvancedStateCollectionEndDateTime = _CwsPmAdvancedStateCollectionEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 94, 1, 6),
    _CwsPmAdvancedStateCollectionEndDateTime_Type()
)
cwsPmAdvancedStateCollectionEndDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedStateCollectionEndDateTime.setStatus("current")
_CwsPmAdvancedPropertiesTable_Object = MibTable
cwsPmAdvancedPropertiesTable = _CwsPmAdvancedPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 95)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedPropertiesTable.setStatus("current")
_CwsPmAdvancedPropertiesEntry_Object = MibTableRow
cwsPmAdvancedPropertiesEntry = _CwsPmAdvancedPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 95, 1)
)
cwsPmAdvancedPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedPropertiesEntry.setStatus("current")


class _CwsPmAdvancedPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedPropertiesTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedPropertiesTableSnmpKey = _CwsPmAdvancedPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 95, 1, 1),
    _CwsPmAdvancedPropertiesTableSnmpKey_Type()
)
cwsPmAdvancedPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedPropertiesTableSnmpKey.setStatus("current")
_CwsPmAdvancedPropertiesConfigurationMode_Type = PmConfigurationMode
_CwsPmAdvancedPropertiesConfigurationMode_Object = MibTableColumn
cwsPmAdvancedPropertiesConfigurationMode = _CwsPmAdvancedPropertiesConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 95, 1, 2),
    _CwsPmAdvancedPropertiesConfigurationMode_Type()
)
cwsPmAdvancedPropertiesConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedPropertiesConfigurationMode.setStatus("current")
_CwsPmAdvancedPropertiesAlignment_Type = PmAlignment
_CwsPmAdvancedPropertiesAlignment_Object = MibTableColumn
cwsPmAdvancedPropertiesAlignment = _CwsPmAdvancedPropertiesAlignment_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 95, 1, 3),
    _CwsPmAdvancedPropertiesAlignment_Type()
)
cwsPmAdvancedPropertiesAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedPropertiesAlignment.setStatus("current")
_CwsPmAdvancedPropertiesConfiguredBinCount_Type = Unsigned32
_CwsPmAdvancedPropertiesConfiguredBinCount_Object = MibTableColumn
cwsPmAdvancedPropertiesConfiguredBinCount = _CwsPmAdvancedPropertiesConfiguredBinCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 95, 1, 4),
    _CwsPmAdvancedPropertiesConfiguredBinCount_Type()
)
cwsPmAdvancedPropertiesConfiguredBinCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedPropertiesConfiguredBinCount.setStatus("current")
_CwsPmAdvancedPropertiesConfiguredBinDuration_Type = Unsigned32
_CwsPmAdvancedPropertiesConfiguredBinDuration_Object = MibTableColumn
cwsPmAdvancedPropertiesConfiguredBinDuration = _CwsPmAdvancedPropertiesConfiguredBinDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 95, 1, 5),
    _CwsPmAdvancedPropertiesConfiguredBinDuration_Type()
)
cwsPmAdvancedPropertiesConfiguredBinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedPropertiesConfiguredBinDuration.setStatus("current")
_CwsPmAdvancedAttachedInterfaceTable_Object = MibTable
cwsPmAdvancedAttachedInterfaceTable = _CwsPmAdvancedAttachedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 96)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedAttachedInterfaceTable.setStatus("current")
_CwsPmAdvancedAttachedInterfaceEntry_Object = MibTableRow
cwsPmAdvancedAttachedInterfaceEntry = _CwsPmAdvancedAttachedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 96, 1)
)
cwsPmAdvancedAttachedInterfaceEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedAttachedInterfaceTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedAttachedInterfaceEntry.setStatus("current")


class _CwsPmAdvancedAttachedInterfaceTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedAttachedInterfaceTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedAttachedInterfaceTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedAttachedInterfaceTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedAttachedInterfaceTableSnmpKey = _CwsPmAdvancedAttachedInterfaceTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 96, 1, 1),
    _CwsPmAdvancedAttachedInterfaceTableSnmpKey_Type()
)
cwsPmAdvancedAttachedInterfaceTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedAttachedInterfaceTableSnmpKey.setStatus("current")
_CwsPmAdvancedAttachedInterfaceType_Type = PmInterfaceType
_CwsPmAdvancedAttachedInterfaceType_Object = MibTableColumn
cwsPmAdvancedAttachedInterfaceType = _CwsPmAdvancedAttachedInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 96, 1, 2),
    _CwsPmAdvancedAttachedInterfaceType_Type()
)
cwsPmAdvancedAttachedInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedAttachedInterfaceType.setStatus("current")
_CwsPmAdvancedAttachedInterfaceName_Type = StringMaxl32
_CwsPmAdvancedAttachedInterfaceName_Object = MibTableColumn
cwsPmAdvancedAttachedInterfaceName = _CwsPmAdvancedAttachedInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 96, 1, 3),
    _CwsPmAdvancedAttachedInterfaceName_Type()
)
cwsPmAdvancedAttachedInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedAttachedInterfaceName.setStatus("current")
_CwsPmAdvancedAttachedInterfaceOperationalState_Type = EnabledDisabledEnum
_CwsPmAdvancedAttachedInterfaceOperationalState_Object = MibTableColumn
cwsPmAdvancedAttachedInterfaceOperationalState = _CwsPmAdvancedAttachedInterfaceOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 96, 1, 4),
    _CwsPmAdvancedAttachedInterfaceOperationalState_Type()
)
cwsPmAdvancedAttachedInterfaceOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedAttachedInterfaceOperationalState.setStatus("current")
_CwsPmAdvancedCurrentIdTable_Object = MibTable
cwsPmAdvancedCurrentIdTable = _CwsPmAdvancedCurrentIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 97)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentIdTable.setStatus("current")
_CwsPmAdvancedCurrentIdEntry_Object = MibTableRow
cwsPmAdvancedCurrentIdEntry = _CwsPmAdvancedCurrentIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 97, 1)
)
cwsPmAdvancedCurrentIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentIdEntry.setStatus("current")


class _CwsPmAdvancedCurrentIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrentIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrentIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrentIdTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrentIdTableSnmpKey = _CwsPmAdvancedCurrentIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 97, 1, 1),
    _CwsPmAdvancedCurrentIdTableSnmpKey_Type()
)
cwsPmAdvancedCurrentIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentIdTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrentIdBinNumber_Type = Unsigned32
_CwsPmAdvancedCurrentIdBinNumber_Object = MibTableColumn
cwsPmAdvancedCurrentIdBinNumber = _CwsPmAdvancedCurrentIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 97, 1, 2),
    _CwsPmAdvancedCurrentIdBinNumber_Type()
)
cwsPmAdvancedCurrentIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentIdBinNumber.setStatus("current")
_CwsPmAdvancedCurrentIdBinName_Type = StringMaxl32
_CwsPmAdvancedCurrentIdBinName_Object = MibTableColumn
cwsPmAdvancedCurrentIdBinName = _CwsPmAdvancedCurrentIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 97, 1, 3),
    _CwsPmAdvancedCurrentIdBinName_Type()
)
cwsPmAdvancedCurrentIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentIdBinName.setStatus("current")
_CwsPmAdvancedCurrentStateTable_Object = MibTable
cwsPmAdvancedCurrentStateTable = _CwsPmAdvancedCurrentStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 98)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStateTable.setStatus("current")
_CwsPmAdvancedCurrentStateEntry_Object = MibTableRow
cwsPmAdvancedCurrentStateEntry = _CwsPmAdvancedCurrentStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 98, 1)
)
cwsPmAdvancedCurrentStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStateEntry.setStatus("current")


class _CwsPmAdvancedCurrentStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrentStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrentStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrentStateTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrentStateTableSnmpKey = _CwsPmAdvancedCurrentStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 98, 1, 1),
    _CwsPmAdvancedCurrentStateTableSnmpKey_Type()
)
cwsPmAdvancedCurrentStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStateTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrentStateStartDateTime_Type = StringMaxl32
_CwsPmAdvancedCurrentStateStartDateTime_Object = MibTableColumn
cwsPmAdvancedCurrentStateStartDateTime = _CwsPmAdvancedCurrentStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 98, 1, 2),
    _CwsPmAdvancedCurrentStateStartDateTime_Type()
)
cwsPmAdvancedCurrentStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStateStartDateTime.setStatus("current")
_CwsPmAdvancedCurrentStateClearedDateTime_Type = StringMaxl32
_CwsPmAdvancedCurrentStateClearedDateTime_Object = MibTableColumn
cwsPmAdvancedCurrentStateClearedDateTime = _CwsPmAdvancedCurrentStateClearedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 98, 1, 3),
    _CwsPmAdvancedCurrentStateClearedDateTime_Type()
)
cwsPmAdvancedCurrentStateClearedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStateClearedDateTime.setStatus("current")
_CwsPmAdvancedCurrentStateState_Type = PmBinState
_CwsPmAdvancedCurrentStateState_Object = MibTableColumn
cwsPmAdvancedCurrentStateState = _CwsPmAdvancedCurrentStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 98, 1, 4),
    _CwsPmAdvancedCurrentStateState_Type()
)
cwsPmAdvancedCurrentStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStateState.setStatus("current")
_CwsPmAdvancedCurrentStatisticsTable_Object = MibTable
cwsPmAdvancedCurrentStatisticsTable = _CwsPmAdvancedCurrentStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 99)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStatisticsTable.setStatus("current")
_CwsPmAdvancedCurrentStatisticsEntry_Object = MibTableRow
cwsPmAdvancedCurrentStatisticsEntry = _CwsPmAdvancedCurrentStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 99, 1)
)
cwsPmAdvancedCurrentStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStatisticsEntry.setStatus("current")


class _CwsPmAdvancedCurrentStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrentStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrentStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrentStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrentStatisticsTableSnmpKey = _CwsPmAdvancedCurrentStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 99, 1, 1),
    _CwsPmAdvancedCurrentStatisticsTableSnmpKey_Type()
)
cwsPmAdvancedCurrentStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStatisticsTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrentStatisticsPostFecBitErrorRate_Type = StringSci
_CwsPmAdvancedCurrentStatisticsPostFecBitErrorRate_Object = MibTableColumn
cwsPmAdvancedCurrentStatisticsPostFecBitErrorRate = _CwsPmAdvancedCurrentStatisticsPostFecBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 99, 1, 2),
    _CwsPmAdvancedCurrentStatisticsPostFecBitErrorRate_Type()
)
cwsPmAdvancedCurrentStatisticsPostFecBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentStatisticsPostFecBitErrorRate.setStatus("current")
_CwsPmPreFecBitErrorRateTable_Object = MibTable
cwsPmPreFecBitErrorRateTable = _CwsPmPreFecBitErrorRateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 100)
)
if mibBuilder.loadTexts:
    cwsPmPreFecBitErrorRateTable.setStatus("current")
_CwsPmPreFecBitErrorRateEntry_Object = MibTableRow
cwsPmPreFecBitErrorRateEntry = _CwsPmPreFecBitErrorRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 100, 1)
)
cwsPmPreFecBitErrorRateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmPreFecBitErrorRateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmPreFecBitErrorRateEntry.setStatus("current")


class _CwsPmPreFecBitErrorRateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmPreFecBitErrorRateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmPreFecBitErrorRateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmPreFecBitErrorRateTableSnmpKey_Object = MibTableColumn
cwsPmPreFecBitErrorRateTableSnmpKey = _CwsPmPreFecBitErrorRateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 100, 1, 1),
    _CwsPmPreFecBitErrorRateTableSnmpKey_Type()
)
cwsPmPreFecBitErrorRateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmPreFecBitErrorRateTableSnmpKey.setStatus("current")
_CwsPmPreFecBitErrorRateBitErrorRate_Type = StringSci
_CwsPmPreFecBitErrorRateBitErrorRate_Object = MibTableColumn
cwsPmPreFecBitErrorRateBitErrorRate = _CwsPmPreFecBitErrorRateBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 100, 1, 2),
    _CwsPmPreFecBitErrorRateBitErrorRate_Type()
)
cwsPmPreFecBitErrorRateBitErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmPreFecBitErrorRateBitErrorRate.setStatus("current")
_CwsPmPreFecBitErrorRateMaximum_Type = StringSci
_CwsPmPreFecBitErrorRateMaximum_Object = MibTableColumn
cwsPmPreFecBitErrorRateMaximum = _CwsPmPreFecBitErrorRateMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 100, 1, 3),
    _CwsPmPreFecBitErrorRateMaximum_Type()
)
cwsPmPreFecBitErrorRateMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmPreFecBitErrorRateMaximum.setStatus("current")
_CwsPmAdvancedCurrentQFactorTable_Object = MibTable
cwsPmAdvancedCurrentQFactorTable = _CwsPmAdvancedCurrentQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 101)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentQFactorTable.setStatus("current")
_CwsPmAdvancedCurrentQFactorEntry_Object = MibTableRow
cwsPmAdvancedCurrentQFactorEntry = _CwsPmAdvancedCurrentQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 101, 1)
)
cwsPmAdvancedCurrentQFactorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentQFactorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentQFactorEntry.setStatus("current")


class _CwsPmAdvancedCurrentQFactorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrentQFactorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrentQFactorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrentQFactorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrentQFactorTableSnmpKey = _CwsPmAdvancedCurrentQFactorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 101, 1, 1),
    _CwsPmAdvancedCurrentQFactorTableSnmpKey_Type()
)
cwsPmAdvancedCurrentQFactorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentQFactorTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrentQFactorQFactor_Type = Decimal3Dig
_CwsPmAdvancedCurrentQFactorQFactor_Object = MibTableColumn
cwsPmAdvancedCurrentQFactorQFactor = _CwsPmAdvancedCurrentQFactorQFactor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 101, 1, 2),
    _CwsPmAdvancedCurrentQFactorQFactor_Type()
)
cwsPmAdvancedCurrentQFactorQFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentQFactorQFactor.setStatus("current")
_CwsPmAdvancedCurrentQFactorMinimum_Type = Decimal3Dig
_CwsPmAdvancedCurrentQFactorMinimum_Object = MibTableColumn
cwsPmAdvancedCurrentQFactorMinimum = _CwsPmAdvancedCurrentQFactorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 101, 1, 3),
    _CwsPmAdvancedCurrentQFactorMinimum_Type()
)
cwsPmAdvancedCurrentQFactorMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentQFactorMinimum.setStatus("current")
_CwsPmAdvancedCurrentQFactorMaximum_Type = Decimal3Dig
_CwsPmAdvancedCurrentQFactorMaximum_Object = MibTableColumn
cwsPmAdvancedCurrentQFactorMaximum = _CwsPmAdvancedCurrentQFactorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 101, 1, 4),
    _CwsPmAdvancedCurrentQFactorMaximum_Type()
)
cwsPmAdvancedCurrentQFactorMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentQFactorMaximum.setStatus("current")
_CwsPmAdvancedCurrentFecErrorTable_Object = MibTable
cwsPmAdvancedCurrentFecErrorTable = _CwsPmAdvancedCurrentFecErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 102)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentFecErrorTable.setStatus("current")
_CwsPmAdvancedCurrentFecErrorEntry_Object = MibTableRow
cwsPmAdvancedCurrentFecErrorEntry = _CwsPmAdvancedCurrentFecErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 102, 1)
)
cwsPmAdvancedCurrentFecErrorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentFecErrorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentFecErrorEntry.setStatus("current")


class _CwsPmAdvancedCurrentFecErrorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrentFecErrorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrentFecErrorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrentFecErrorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrentFecErrorTableSnmpKey = _CwsPmAdvancedCurrentFecErrorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 102, 1, 1),
    _CwsPmAdvancedCurrentFecErrorTableSnmpKey_Type()
)
cwsPmAdvancedCurrentFecErrorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentFecErrorTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrentFecErrorFrameErrorCount_Type = Counter64
_CwsPmAdvancedCurrentFecErrorFrameErrorCount_Object = MibTableColumn
cwsPmAdvancedCurrentFecErrorFrameErrorCount = _CwsPmAdvancedCurrentFecErrorFrameErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 102, 1, 2),
    _CwsPmAdvancedCurrentFecErrorFrameErrorCount_Type()
)
cwsPmAdvancedCurrentFecErrorFrameErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentFecErrorFrameErrorCount.setStatus("current")
_CwsPmAdvancedCurrentFecErrorFrameErrorCountSecond_Type = Counter64
_CwsPmAdvancedCurrentFecErrorFrameErrorCountSecond_Object = MibTableColumn
cwsPmAdvancedCurrentFecErrorFrameErrorCountSecond = _CwsPmAdvancedCurrentFecErrorFrameErrorCountSecond_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 102, 1, 3),
    _CwsPmAdvancedCurrentFecErrorFrameErrorCountSecond_Type()
)
cwsPmAdvancedCurrentFecErrorFrameErrorCountSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentFecErrorFrameErrorCountSecond.setStatus("current")
_CwsPmAdvancedCurrentFecErrorUncorrectedBlockCount_Type = Counter64
_CwsPmAdvancedCurrentFecErrorUncorrectedBlockCount_Object = MibTableColumn
cwsPmAdvancedCurrentFecErrorUncorrectedBlockCount = _CwsPmAdvancedCurrentFecErrorUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 102, 1, 4),
    _CwsPmAdvancedCurrentFecErrorUncorrectedBlockCount_Type()
)
cwsPmAdvancedCurrentFecErrorUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentFecErrorUncorrectedBlockCount.setStatus("current")
_CwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds_Type = Counter64
_CwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds_Object = MibTableColumn
cwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds = _CwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 102, 1, 5),
    _CwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds_Type()
)
cwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds.setStatus("current")
_CwsPmAdvancedCurrent24hIdTable_Object = MibTable
cwsPmAdvancedCurrent24hIdTable = _CwsPmAdvancedCurrent24hIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 103)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hIdTable.setStatus("current")
_CwsPmAdvancedCurrent24hIdEntry_Object = MibTableRow
cwsPmAdvancedCurrent24hIdEntry = _CwsPmAdvancedCurrent24hIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 103, 1)
)
cwsPmAdvancedCurrent24hIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hIdEntry.setStatus("current")


class _CwsPmAdvancedCurrent24hIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrent24hIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrent24hIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrent24hIdTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrent24hIdTableSnmpKey = _CwsPmAdvancedCurrent24hIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 103, 1, 1),
    _CwsPmAdvancedCurrent24hIdTableSnmpKey_Type()
)
cwsPmAdvancedCurrent24hIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hIdTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrent24hIdBinNumber_Type = Unsigned32
_CwsPmAdvancedCurrent24hIdBinNumber_Object = MibTableColumn
cwsPmAdvancedCurrent24hIdBinNumber = _CwsPmAdvancedCurrent24hIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 103, 1, 2),
    _CwsPmAdvancedCurrent24hIdBinNumber_Type()
)
cwsPmAdvancedCurrent24hIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hIdBinNumber.setStatus("current")
_CwsPmAdvancedCurrent24hIdBinName_Type = StringMaxl32
_CwsPmAdvancedCurrent24hIdBinName_Object = MibTableColumn
cwsPmAdvancedCurrent24hIdBinName = _CwsPmAdvancedCurrent24hIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 103, 1, 3),
    _CwsPmAdvancedCurrent24hIdBinName_Type()
)
cwsPmAdvancedCurrent24hIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hIdBinName.setStatus("current")
_CwsPmAdvancedCurrent24hStateTable_Object = MibTable
cwsPmAdvancedCurrent24hStateTable = _CwsPmAdvancedCurrent24hStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 104)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStateTable.setStatus("current")
_CwsPmAdvancedCurrent24hStateEntry_Object = MibTableRow
cwsPmAdvancedCurrent24hStateEntry = _CwsPmAdvancedCurrent24hStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 104, 1)
)
cwsPmAdvancedCurrent24hStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStateEntry.setStatus("current")


class _CwsPmAdvancedCurrent24hStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrent24hStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrent24hStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrent24hStateTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrent24hStateTableSnmpKey = _CwsPmAdvancedCurrent24hStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 104, 1, 1),
    _CwsPmAdvancedCurrent24hStateTableSnmpKey_Type()
)
cwsPmAdvancedCurrent24hStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStateTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrent24hStateStartDateTime_Type = StringMaxl32
_CwsPmAdvancedCurrent24hStateStartDateTime_Object = MibTableColumn
cwsPmAdvancedCurrent24hStateStartDateTime = _CwsPmAdvancedCurrent24hStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 104, 1, 2),
    _CwsPmAdvancedCurrent24hStateStartDateTime_Type()
)
cwsPmAdvancedCurrent24hStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStateStartDateTime.setStatus("current")
_CwsPmAdvancedCurrent24hStateClearedDateTime_Type = StringMaxl32
_CwsPmAdvancedCurrent24hStateClearedDateTime_Object = MibTableColumn
cwsPmAdvancedCurrent24hStateClearedDateTime = _CwsPmAdvancedCurrent24hStateClearedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 104, 1, 3),
    _CwsPmAdvancedCurrent24hStateClearedDateTime_Type()
)
cwsPmAdvancedCurrent24hStateClearedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStateClearedDateTime.setStatus("current")
_CwsPmAdvancedCurrent24hStateState_Type = PmBinState
_CwsPmAdvancedCurrent24hStateState_Object = MibTableColumn
cwsPmAdvancedCurrent24hStateState = _CwsPmAdvancedCurrent24hStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 104, 1, 4),
    _CwsPmAdvancedCurrent24hStateState_Type()
)
cwsPmAdvancedCurrent24hStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStateState.setStatus("current")
_CwsPmAdvancedCurrent24hStatisticsTable_Object = MibTable
cwsPmAdvancedCurrent24hStatisticsTable = _CwsPmAdvancedCurrent24hStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 105)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStatisticsTable.setStatus("current")
_CwsPmAdvancedCurrent24hStatisticsEntry_Object = MibTableRow
cwsPmAdvancedCurrent24hStatisticsEntry = _CwsPmAdvancedCurrent24hStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 105, 1)
)
cwsPmAdvancedCurrent24hStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStatisticsEntry.setStatus("current")


class _CwsPmAdvancedCurrent24hStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrent24hStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrent24hStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrent24hStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrent24hStatisticsTableSnmpKey = _CwsPmAdvancedCurrent24hStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 105, 1, 1),
    _CwsPmAdvancedCurrent24hStatisticsTableSnmpKey_Type()
)
cwsPmAdvancedCurrent24hStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStatisticsTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate_Type = StringSci
_CwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate_Object = MibTableColumn
cwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate = _CwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 105, 1, 2),
    _CwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate_Type()
)
cwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate.setStatus("current")
_CwsPmAdvancedCurrent24hPreFecBerTable_Object = MibTable
cwsPmAdvancedCurrent24hPreFecBerTable = _CwsPmAdvancedCurrent24hPreFecBerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 106)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hPreFecBerTable.setStatus("current")
_CwsPmAdvancedCurrent24hPreFecBerEntry_Object = MibTableRow
cwsPmAdvancedCurrent24hPreFecBerEntry = _CwsPmAdvancedCurrent24hPreFecBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 106, 1)
)
cwsPmAdvancedCurrent24hPreFecBerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hPreFecBerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hPreFecBerEntry.setStatus("current")


class _CwsPmAdvancedCurrent24hPreFecBerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrent24hPreFecBerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrent24hPreFecBerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrent24hPreFecBerTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrent24hPreFecBerTableSnmpKey = _CwsPmAdvancedCurrent24hPreFecBerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 106, 1, 1),
    _CwsPmAdvancedCurrent24hPreFecBerTableSnmpKey_Type()
)
cwsPmAdvancedCurrent24hPreFecBerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hPreFecBerTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrent24hPreFecBerBitErrorRate_Type = StringSci
_CwsPmAdvancedCurrent24hPreFecBerBitErrorRate_Object = MibTableColumn
cwsPmAdvancedCurrent24hPreFecBerBitErrorRate = _CwsPmAdvancedCurrent24hPreFecBerBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 106, 1, 2),
    _CwsPmAdvancedCurrent24hPreFecBerBitErrorRate_Type()
)
cwsPmAdvancedCurrent24hPreFecBerBitErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hPreFecBerBitErrorRate.setStatus("current")
_CwsPmAdvancedCurrent24hPreFecBerMaximum_Type = StringSci
_CwsPmAdvancedCurrent24hPreFecBerMaximum_Object = MibTableColumn
cwsPmAdvancedCurrent24hPreFecBerMaximum = _CwsPmAdvancedCurrent24hPreFecBerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 106, 1, 3),
    _CwsPmAdvancedCurrent24hPreFecBerMaximum_Type()
)
cwsPmAdvancedCurrent24hPreFecBerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hPreFecBerMaximum.setStatus("current")
_CwsPmAdvancedCurrent24hQFactorTable_Object = MibTable
cwsPmAdvancedCurrent24hQFactorTable = _CwsPmAdvancedCurrent24hQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 107)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hQFactorTable.setStatus("current")
_CwsPmAdvancedCurrent24hQFactorEntry_Object = MibTableRow
cwsPmAdvancedCurrent24hQFactorEntry = _CwsPmAdvancedCurrent24hQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 107, 1)
)
cwsPmAdvancedCurrent24hQFactorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hQFactorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hQFactorEntry.setStatus("current")


class _CwsPmAdvancedCurrent24hQFactorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrent24hQFactorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrent24hQFactorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrent24hQFactorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrent24hQFactorTableSnmpKey = _CwsPmAdvancedCurrent24hQFactorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 107, 1, 1),
    _CwsPmAdvancedCurrent24hQFactorTableSnmpKey_Type()
)
cwsPmAdvancedCurrent24hQFactorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hQFactorTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrent24hQFactorQFactor_Type = Decimal3Dig
_CwsPmAdvancedCurrent24hQFactorQFactor_Object = MibTableColumn
cwsPmAdvancedCurrent24hQFactorQFactor = _CwsPmAdvancedCurrent24hQFactorQFactor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 107, 1, 2),
    _CwsPmAdvancedCurrent24hQFactorQFactor_Type()
)
cwsPmAdvancedCurrent24hQFactorQFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hQFactorQFactor.setStatus("current")
_CwsPmAdvancedCurrent24hQFactorMinimum_Type = Decimal3Dig
_CwsPmAdvancedCurrent24hQFactorMinimum_Object = MibTableColumn
cwsPmAdvancedCurrent24hQFactorMinimum = _CwsPmAdvancedCurrent24hQFactorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 107, 1, 3),
    _CwsPmAdvancedCurrent24hQFactorMinimum_Type()
)
cwsPmAdvancedCurrent24hQFactorMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hQFactorMinimum.setStatus("current")
_CwsPmAdvancedCurrent24hQFactorMaximum_Type = Decimal3Dig
_CwsPmAdvancedCurrent24hQFactorMaximum_Object = MibTableColumn
cwsPmAdvancedCurrent24hQFactorMaximum = _CwsPmAdvancedCurrent24hQFactorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 107, 1, 4),
    _CwsPmAdvancedCurrent24hQFactorMaximum_Type()
)
cwsPmAdvancedCurrent24hQFactorMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hQFactorMaximum.setStatus("current")
_CwsPmAdvancedCurrent24hFecErrorTable_Object = MibTable
cwsPmAdvancedCurrent24hFecErrorTable = _CwsPmAdvancedCurrent24hFecErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 108)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hFecErrorTable.setStatus("current")
_CwsPmAdvancedCurrent24hFecErrorEntry_Object = MibTableRow
cwsPmAdvancedCurrent24hFecErrorEntry = _CwsPmAdvancedCurrent24hFecErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 108, 1)
)
cwsPmAdvancedCurrent24hFecErrorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hFecErrorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hFecErrorEntry.setStatus("current")


class _CwsPmAdvancedCurrent24hFecErrorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedCurrent24hFecErrorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedCurrent24hFecErrorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedCurrent24hFecErrorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedCurrent24hFecErrorTableSnmpKey = _CwsPmAdvancedCurrent24hFecErrorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 108, 1, 1),
    _CwsPmAdvancedCurrent24hFecErrorTableSnmpKey_Type()
)
cwsPmAdvancedCurrent24hFecErrorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hFecErrorTableSnmpKey.setStatus("current")
_CwsPmAdvancedCurrent24hFecErrorFrameErrorCount_Type = Counter64
_CwsPmAdvancedCurrent24hFecErrorFrameErrorCount_Object = MibTableColumn
cwsPmAdvancedCurrent24hFecErrorFrameErrorCount = _CwsPmAdvancedCurrent24hFecErrorFrameErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 108, 1, 2),
    _CwsPmAdvancedCurrent24hFecErrorFrameErrorCount_Type()
)
cwsPmAdvancedCurrent24hFecErrorFrameErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hFecErrorFrameErrorCount.setStatus("current")
_CwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond_Type = Counter64
_CwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond_Object = MibTableColumn
cwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond = _CwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 108, 1, 3),
    _CwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond_Type()
)
cwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond.setStatus("current")
_CwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount_Type = Counter64
_CwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount_Object = MibTableColumn
cwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount = _CwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 108, 1, 4),
    _CwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount_Type()
)
cwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount.setStatus("current")
_CwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds_Type = Counter64
_CwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds_Object = MibTableColumn
cwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds = _CwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 108, 1, 5),
    _CwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds_Type()
)
cwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds.setStatus("current")
_CwsPmAdvancedHistoryBinsTable_Object = MibTable
cwsPmAdvancedHistoryBinsTable = _CwsPmAdvancedHistoryBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 109)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryBinsTable.setStatus("current")
_CwsPmAdvancedHistoryBinsEntry_Object = MibTableRow
cwsPmAdvancedHistoryBinsEntry = _CwsPmAdvancedHistoryBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 109, 1)
)
cwsPmAdvancedHistoryBinsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryBinsBinNumber"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryBinsEntry.setStatus("current")


class _CwsPmAdvancedHistoryBinsBinNumber_Type(Integer32):
    """Custom type cwsPmAdvancedHistoryBinsBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistoryBinsBinNumber_Type.__name__ = "Integer32"
_CwsPmAdvancedHistoryBinsBinNumber_Object = MibTableColumn
cwsPmAdvancedHistoryBinsBinNumber = _CwsPmAdvancedHistoryBinsBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 109, 1, 1),
    _CwsPmAdvancedHistoryBinsBinNumber_Type()
)
cwsPmAdvancedHistoryBinsBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryBinsBinNumber.setStatus("current")
_CwsPmAdvancedHistoryStateTable_Object = MibTable
cwsPmAdvancedHistoryStateTable = _CwsPmAdvancedHistoryStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 110)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStateTable.setStatus("current")
_CwsPmAdvancedHistoryStateEntry_Object = MibTableRow
cwsPmAdvancedHistoryStateEntry = _CwsPmAdvancedHistoryStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 110, 1)
)
cwsPmAdvancedHistoryStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStateEntry.setStatus("current")


class _CwsPmAdvancedHistoryStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistoryStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistoryStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistoryStateTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistoryStateTableSnmpKey = _CwsPmAdvancedHistoryStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 110, 1, 1),
    _CwsPmAdvancedHistoryStateTableSnmpKey_Type()
)
cwsPmAdvancedHistoryStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStateTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistoryStateStartDateTime_Type = StringMaxl32
_CwsPmAdvancedHistoryStateStartDateTime_Object = MibTableColumn
cwsPmAdvancedHistoryStateStartDateTime = _CwsPmAdvancedHistoryStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 110, 1, 2),
    _CwsPmAdvancedHistoryStateStartDateTime_Type()
)
cwsPmAdvancedHistoryStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStateStartDateTime.setStatus("current")
_CwsPmAdvancedHistoryStateEndDateTime_Type = StringMaxl32
_CwsPmAdvancedHistoryStateEndDateTime_Object = MibTableColumn
cwsPmAdvancedHistoryStateEndDateTime = _CwsPmAdvancedHistoryStateEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 110, 1, 3),
    _CwsPmAdvancedHistoryStateEndDateTime_Type()
)
cwsPmAdvancedHistoryStateEndDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStateEndDateTime.setStatus("current")
_CwsPmAdvancedHistoryStateState_Type = PmBinState
_CwsPmAdvancedHistoryStateState_Object = MibTableColumn
cwsPmAdvancedHistoryStateState = _CwsPmAdvancedHistoryStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 110, 1, 4),
    _CwsPmAdvancedHistoryStateState_Type()
)
cwsPmAdvancedHistoryStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStateState.setStatus("current")
_CwsPmAdvancedHistoryStatisticsTable_Object = MibTable
cwsPmAdvancedHistoryStatisticsTable = _CwsPmAdvancedHistoryStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 111)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStatisticsTable.setStatus("current")
_CwsPmAdvancedHistoryStatisticsEntry_Object = MibTableRow
cwsPmAdvancedHistoryStatisticsEntry = _CwsPmAdvancedHistoryStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 111, 1)
)
cwsPmAdvancedHistoryStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStatisticsEntry.setStatus("current")


class _CwsPmAdvancedHistoryStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistoryStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistoryStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistoryStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistoryStatisticsTableSnmpKey = _CwsPmAdvancedHistoryStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 111, 1, 1),
    _CwsPmAdvancedHistoryStatisticsTableSnmpKey_Type()
)
cwsPmAdvancedHistoryStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStatisticsTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistoryStatisticsPostFecBitErrorRate_Type = StringSci
_CwsPmAdvancedHistoryStatisticsPostFecBitErrorRate_Object = MibTableColumn
cwsPmAdvancedHistoryStatisticsPostFecBitErrorRate = _CwsPmAdvancedHistoryStatisticsPostFecBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 111, 1, 2),
    _CwsPmAdvancedHistoryStatisticsPostFecBitErrorRate_Type()
)
cwsPmAdvancedHistoryStatisticsPostFecBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryStatisticsPostFecBitErrorRate.setStatus("current")
_CwsPmAdvancedHistoryPreFecBerTable_Object = MibTable
cwsPmAdvancedHistoryPreFecBerTable = _CwsPmAdvancedHistoryPreFecBerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 112)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryPreFecBerTable.setStatus("current")
_CwsPmAdvancedHistoryPreFecBerEntry_Object = MibTableRow
cwsPmAdvancedHistoryPreFecBerEntry = _CwsPmAdvancedHistoryPreFecBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 112, 1)
)
cwsPmAdvancedHistoryPreFecBerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryPreFecBerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryPreFecBerEntry.setStatus("current")


class _CwsPmAdvancedHistoryPreFecBerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistoryPreFecBerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistoryPreFecBerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistoryPreFecBerTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistoryPreFecBerTableSnmpKey = _CwsPmAdvancedHistoryPreFecBerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 112, 1, 1),
    _CwsPmAdvancedHistoryPreFecBerTableSnmpKey_Type()
)
cwsPmAdvancedHistoryPreFecBerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryPreFecBerTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistoryPreFecBerBitErrorRate_Type = StringSci
_CwsPmAdvancedHistoryPreFecBerBitErrorRate_Object = MibTableColumn
cwsPmAdvancedHistoryPreFecBerBitErrorRate = _CwsPmAdvancedHistoryPreFecBerBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 112, 1, 2),
    _CwsPmAdvancedHistoryPreFecBerBitErrorRate_Type()
)
cwsPmAdvancedHistoryPreFecBerBitErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryPreFecBerBitErrorRate.setStatus("current")
_CwsPmAdvancedHistoryPreFecBerMaximum_Type = StringSci
_CwsPmAdvancedHistoryPreFecBerMaximum_Object = MibTableColumn
cwsPmAdvancedHistoryPreFecBerMaximum = _CwsPmAdvancedHistoryPreFecBerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 112, 1, 3),
    _CwsPmAdvancedHistoryPreFecBerMaximum_Type()
)
cwsPmAdvancedHistoryPreFecBerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryPreFecBerMaximum.setStatus("current")
_CwsPmAdvancedHistoryQFactorTable_Object = MibTable
cwsPmAdvancedHistoryQFactorTable = _CwsPmAdvancedHistoryQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 113)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryQFactorTable.setStatus("current")
_CwsPmAdvancedHistoryQFactorEntry_Object = MibTableRow
cwsPmAdvancedHistoryQFactorEntry = _CwsPmAdvancedHistoryQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 113, 1)
)
cwsPmAdvancedHistoryQFactorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryQFactorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryQFactorEntry.setStatus("current")


class _CwsPmAdvancedHistoryQFactorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistoryQFactorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistoryQFactorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistoryQFactorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistoryQFactorTableSnmpKey = _CwsPmAdvancedHistoryQFactorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 113, 1, 1),
    _CwsPmAdvancedHistoryQFactorTableSnmpKey_Type()
)
cwsPmAdvancedHistoryQFactorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryQFactorTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistoryQFactorQFactor_Type = Decimal3Dig
_CwsPmAdvancedHistoryQFactorQFactor_Object = MibTableColumn
cwsPmAdvancedHistoryQFactorQFactor = _CwsPmAdvancedHistoryQFactorQFactor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 113, 1, 2),
    _CwsPmAdvancedHistoryQFactorQFactor_Type()
)
cwsPmAdvancedHistoryQFactorQFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryQFactorQFactor.setStatus("current")
_CwsPmAdvancedHistoryQFactorMinimum_Type = Decimal3Dig
_CwsPmAdvancedHistoryQFactorMinimum_Object = MibTableColumn
cwsPmAdvancedHistoryQFactorMinimum = _CwsPmAdvancedHistoryQFactorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 113, 1, 3),
    _CwsPmAdvancedHistoryQFactorMinimum_Type()
)
cwsPmAdvancedHistoryQFactorMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryQFactorMinimum.setStatus("current")
_CwsPmAdvancedHistoryQFactorMaximum_Type = Decimal3Dig
_CwsPmAdvancedHistoryQFactorMaximum_Object = MibTableColumn
cwsPmAdvancedHistoryQFactorMaximum = _CwsPmAdvancedHistoryQFactorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 113, 1, 4),
    _CwsPmAdvancedHistoryQFactorMaximum_Type()
)
cwsPmAdvancedHistoryQFactorMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryQFactorMaximum.setStatus("current")
_CwsPmAdvancedHistoryFecErrorTable_Object = MibTable
cwsPmAdvancedHistoryFecErrorTable = _CwsPmAdvancedHistoryFecErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 114)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryFecErrorTable.setStatus("current")
_CwsPmAdvancedHistoryFecErrorEntry_Object = MibTableRow
cwsPmAdvancedHistoryFecErrorEntry = _CwsPmAdvancedHistoryFecErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 114, 1)
)
cwsPmAdvancedHistoryFecErrorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryFecErrorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryFecErrorEntry.setStatus("current")


class _CwsPmAdvancedHistoryFecErrorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistoryFecErrorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistoryFecErrorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistoryFecErrorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistoryFecErrorTableSnmpKey = _CwsPmAdvancedHistoryFecErrorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 114, 1, 1),
    _CwsPmAdvancedHistoryFecErrorTableSnmpKey_Type()
)
cwsPmAdvancedHistoryFecErrorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryFecErrorTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistoryFecErrorFrameErrorCount_Type = Counter64
_CwsPmAdvancedHistoryFecErrorFrameErrorCount_Object = MibTableColumn
cwsPmAdvancedHistoryFecErrorFrameErrorCount = _CwsPmAdvancedHistoryFecErrorFrameErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 114, 1, 2),
    _CwsPmAdvancedHistoryFecErrorFrameErrorCount_Type()
)
cwsPmAdvancedHistoryFecErrorFrameErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryFecErrorFrameErrorCount.setStatus("current")
_CwsPmAdvancedHistoryFecErrorFrameErrorCountSecond_Type = Counter64
_CwsPmAdvancedHistoryFecErrorFrameErrorCountSecond_Object = MibTableColumn
cwsPmAdvancedHistoryFecErrorFrameErrorCountSecond = _CwsPmAdvancedHistoryFecErrorFrameErrorCountSecond_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 114, 1, 3),
    _CwsPmAdvancedHistoryFecErrorFrameErrorCountSecond_Type()
)
cwsPmAdvancedHistoryFecErrorFrameErrorCountSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryFecErrorFrameErrorCountSecond.setStatus("current")
_CwsPmAdvancedHistoryFecErrorUncorrectedBlockCount_Type = Counter64
_CwsPmAdvancedHistoryFecErrorUncorrectedBlockCount_Object = MibTableColumn
cwsPmAdvancedHistoryFecErrorUncorrectedBlockCount = _CwsPmAdvancedHistoryFecErrorUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 114, 1, 4),
    _CwsPmAdvancedHistoryFecErrorUncorrectedBlockCount_Type()
)
cwsPmAdvancedHistoryFecErrorUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryFecErrorUncorrectedBlockCount.setStatus("current")
_CwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds_Type = Counter64
_CwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds_Object = MibTableColumn
cwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds = _CwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 114, 1, 5),
    _CwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds_Type()
)
cwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds.setStatus("current")
_CwsPmAdvancedHistory24hIdTable_Object = MibTable
cwsPmAdvancedHistory24hIdTable = _CwsPmAdvancedHistory24hIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 115)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hIdTable.setStatus("current")
_CwsPmAdvancedHistory24hIdEntry_Object = MibTableRow
cwsPmAdvancedHistory24hIdEntry = _CwsPmAdvancedHistory24hIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 115, 1)
)
cwsPmAdvancedHistory24hIdEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hIdEntry.setStatus("current")


class _CwsPmAdvancedHistory24hIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistory24hIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistory24hIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistory24hIdTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistory24hIdTableSnmpKey = _CwsPmAdvancedHistory24hIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 115, 1, 1),
    _CwsPmAdvancedHistory24hIdTableSnmpKey_Type()
)
cwsPmAdvancedHistory24hIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hIdTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistory24hIdBinNumber_Type = Unsigned32
_CwsPmAdvancedHistory24hIdBinNumber_Object = MibTableColumn
cwsPmAdvancedHistory24hIdBinNumber = _CwsPmAdvancedHistory24hIdBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 115, 1, 2),
    _CwsPmAdvancedHistory24hIdBinNumber_Type()
)
cwsPmAdvancedHistory24hIdBinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hIdBinNumber.setStatus("current")
_CwsPmAdvancedHistory24hIdBinName_Type = StringMaxl32
_CwsPmAdvancedHistory24hIdBinName_Object = MibTableColumn
cwsPmAdvancedHistory24hIdBinName = _CwsPmAdvancedHistory24hIdBinName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 115, 1, 3),
    _CwsPmAdvancedHistory24hIdBinName_Type()
)
cwsPmAdvancedHistory24hIdBinName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hIdBinName.setStatus("current")
_CwsPmAdvancedHistory24hStateTable_Object = MibTable
cwsPmAdvancedHistory24hStateTable = _CwsPmAdvancedHistory24hStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 116)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStateTable.setStatus("current")
_CwsPmAdvancedHistory24hStateEntry_Object = MibTableRow
cwsPmAdvancedHistory24hStateEntry = _CwsPmAdvancedHistory24hStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 116, 1)
)
cwsPmAdvancedHistory24hStateEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStateEntry.setStatus("current")


class _CwsPmAdvancedHistory24hStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistory24hStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistory24hStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistory24hStateTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistory24hStateTableSnmpKey = _CwsPmAdvancedHistory24hStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 116, 1, 1),
    _CwsPmAdvancedHistory24hStateTableSnmpKey_Type()
)
cwsPmAdvancedHistory24hStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStateTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistory24hStateStartDateTime_Type = StringMaxl32
_CwsPmAdvancedHistory24hStateStartDateTime_Object = MibTableColumn
cwsPmAdvancedHistory24hStateStartDateTime = _CwsPmAdvancedHistory24hStateStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 116, 1, 2),
    _CwsPmAdvancedHistory24hStateStartDateTime_Type()
)
cwsPmAdvancedHistory24hStateStartDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStateStartDateTime.setStatus("current")
_CwsPmAdvancedHistory24hStateEndDateTime_Type = StringMaxl32
_CwsPmAdvancedHistory24hStateEndDateTime_Object = MibTableColumn
cwsPmAdvancedHistory24hStateEndDateTime = _CwsPmAdvancedHistory24hStateEndDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 116, 1, 3),
    _CwsPmAdvancedHistory24hStateEndDateTime_Type()
)
cwsPmAdvancedHistory24hStateEndDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStateEndDateTime.setStatus("current")
_CwsPmAdvancedHistory24hStateState_Type = PmBinState
_CwsPmAdvancedHistory24hStateState_Object = MibTableColumn
cwsPmAdvancedHistory24hStateState = _CwsPmAdvancedHistory24hStateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 116, 1, 4),
    _CwsPmAdvancedHistory24hStateState_Type()
)
cwsPmAdvancedHistory24hStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStateState.setStatus("current")
_CwsPmAdvancedHistory24hStatisticsTable_Object = MibTable
cwsPmAdvancedHistory24hStatisticsTable = _CwsPmAdvancedHistory24hStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 117)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStatisticsTable.setStatus("current")
_CwsPmAdvancedHistory24hStatisticsEntry_Object = MibTableRow
cwsPmAdvancedHistory24hStatisticsEntry = _CwsPmAdvancedHistory24hStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 117, 1)
)
cwsPmAdvancedHistory24hStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hStatisticsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStatisticsEntry.setStatus("current")


class _CwsPmAdvancedHistory24hStatisticsTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistory24hStatisticsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistory24hStatisticsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistory24hStatisticsTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistory24hStatisticsTableSnmpKey = _CwsPmAdvancedHistory24hStatisticsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 117, 1, 1),
    _CwsPmAdvancedHistory24hStatisticsTableSnmpKey_Type()
)
cwsPmAdvancedHistory24hStatisticsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStatisticsTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate_Type = StringSci
_CwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate_Object = MibTableColumn
cwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate = _CwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 117, 1, 2),
    _CwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate_Type()
)
cwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate.setStatus("current")
_CwsPmAdvancedHistory24hPreFecBerTable_Object = MibTable
cwsPmAdvancedHistory24hPreFecBerTable = _CwsPmAdvancedHistory24hPreFecBerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 118)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hPreFecBerTable.setStatus("current")
_CwsPmAdvancedHistory24hPreFecBerEntry_Object = MibTableRow
cwsPmAdvancedHistory24hPreFecBerEntry = _CwsPmAdvancedHistory24hPreFecBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 118, 1)
)
cwsPmAdvancedHistory24hPreFecBerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hPreFecBerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hPreFecBerEntry.setStatus("current")


class _CwsPmAdvancedHistory24hPreFecBerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistory24hPreFecBerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistory24hPreFecBerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistory24hPreFecBerTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistory24hPreFecBerTableSnmpKey = _CwsPmAdvancedHistory24hPreFecBerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 118, 1, 1),
    _CwsPmAdvancedHistory24hPreFecBerTableSnmpKey_Type()
)
cwsPmAdvancedHistory24hPreFecBerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hPreFecBerTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistory24hPreFecBerBitErrorRate_Type = StringSci
_CwsPmAdvancedHistory24hPreFecBerBitErrorRate_Object = MibTableColumn
cwsPmAdvancedHistory24hPreFecBerBitErrorRate = _CwsPmAdvancedHistory24hPreFecBerBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 118, 1, 2),
    _CwsPmAdvancedHistory24hPreFecBerBitErrorRate_Type()
)
cwsPmAdvancedHistory24hPreFecBerBitErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hPreFecBerBitErrorRate.setStatus("current")
_CwsPmAdvancedHistory24hPreFecBerMaximum_Type = StringSci
_CwsPmAdvancedHistory24hPreFecBerMaximum_Object = MibTableColumn
cwsPmAdvancedHistory24hPreFecBerMaximum = _CwsPmAdvancedHistory24hPreFecBerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 118, 1, 3),
    _CwsPmAdvancedHistory24hPreFecBerMaximum_Type()
)
cwsPmAdvancedHistory24hPreFecBerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hPreFecBerMaximum.setStatus("current")
_CwsPmAdvancedHistory24hQFactorTable_Object = MibTable
cwsPmAdvancedHistory24hQFactorTable = _CwsPmAdvancedHistory24hQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 119)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hQFactorTable.setStatus("current")
_CwsPmAdvancedHistory24hQFactorEntry_Object = MibTableRow
cwsPmAdvancedHistory24hQFactorEntry = _CwsPmAdvancedHistory24hQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 119, 1)
)
cwsPmAdvancedHistory24hQFactorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hQFactorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hQFactorEntry.setStatus("current")


class _CwsPmAdvancedHistory24hQFactorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistory24hQFactorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistory24hQFactorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistory24hQFactorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistory24hQFactorTableSnmpKey = _CwsPmAdvancedHistory24hQFactorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 119, 1, 1),
    _CwsPmAdvancedHistory24hQFactorTableSnmpKey_Type()
)
cwsPmAdvancedHistory24hQFactorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hQFactorTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistory24hQFactorQFactor_Type = Decimal3Dig
_CwsPmAdvancedHistory24hQFactorQFactor_Object = MibTableColumn
cwsPmAdvancedHistory24hQFactorQFactor = _CwsPmAdvancedHistory24hQFactorQFactor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 119, 1, 2),
    _CwsPmAdvancedHistory24hQFactorQFactor_Type()
)
cwsPmAdvancedHistory24hQFactorQFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hQFactorQFactor.setStatus("current")
_CwsPmAdvancedHistory24hQFactorMinimum_Type = Decimal3Dig
_CwsPmAdvancedHistory24hQFactorMinimum_Object = MibTableColumn
cwsPmAdvancedHistory24hQFactorMinimum = _CwsPmAdvancedHistory24hQFactorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 119, 1, 3),
    _CwsPmAdvancedHistory24hQFactorMinimum_Type()
)
cwsPmAdvancedHistory24hQFactorMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hQFactorMinimum.setStatus("current")
_CwsPmAdvancedHistory24hQFactorMaximum_Type = Decimal3Dig
_CwsPmAdvancedHistory24hQFactorMaximum_Object = MibTableColumn
cwsPmAdvancedHistory24hQFactorMaximum = _CwsPmAdvancedHistory24hQFactorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 119, 1, 4),
    _CwsPmAdvancedHistory24hQFactorMaximum_Type()
)
cwsPmAdvancedHistory24hQFactorMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hQFactorMaximum.setStatus("current")
_CwsPmAdvancedHistory24hFecErrorTable_Object = MibTable
cwsPmAdvancedHistory24hFecErrorTable = _CwsPmAdvancedHistory24hFecErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 120)
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hFecErrorTable.setStatus("current")
_CwsPmAdvancedHistory24hFecErrorEntry_Object = MibTableRow
cwsPmAdvancedHistory24hFecErrorEntry = _CwsPmAdvancedHistory24hFecErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 120, 1)
)
cwsPmAdvancedHistory24hFecErrorEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hFecErrorTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hFecErrorEntry.setStatus("current")


class _CwsPmAdvancedHistory24hFecErrorTableSnmpKey_Type(Integer32):
    """Custom type cwsPmAdvancedHistory24hFecErrorTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmAdvancedHistory24hFecErrorTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmAdvancedHistory24hFecErrorTableSnmpKey_Object = MibTableColumn
cwsPmAdvancedHistory24hFecErrorTableSnmpKey = _CwsPmAdvancedHistory24hFecErrorTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 120, 1, 1),
    _CwsPmAdvancedHistory24hFecErrorTableSnmpKey_Type()
)
cwsPmAdvancedHistory24hFecErrorTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hFecErrorTableSnmpKey.setStatus("current")
_CwsPmAdvancedHistory24hFecErrorFrameErrorCount_Type = Counter64
_CwsPmAdvancedHistory24hFecErrorFrameErrorCount_Object = MibTableColumn
cwsPmAdvancedHistory24hFecErrorFrameErrorCount = _CwsPmAdvancedHistory24hFecErrorFrameErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 120, 1, 2),
    _CwsPmAdvancedHistory24hFecErrorFrameErrorCount_Type()
)
cwsPmAdvancedHistory24hFecErrorFrameErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hFecErrorFrameErrorCount.setStatus("current")
_CwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond_Type = Counter64
_CwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond_Object = MibTableColumn
cwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond = _CwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 120, 1, 3),
    _CwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond_Type()
)
cwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond.setStatus("current")
_CwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount_Type = Counter64
_CwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount_Object = MibTableColumn
cwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount = _CwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 120, 1, 4),
    _CwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount_Type()
)
cwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount.setStatus("current")
_CwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds_Type = Counter64
_CwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds_Object = MibTableColumn
cwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds = _CwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 120, 1, 5),
    _CwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds_Type()
)
cwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds.setStatus("current")
_CwsPmExtendedCurrentOduLayerTable_Object = MibTable
cwsPmExtendedCurrentOduLayerTable = _CwsPmExtendedCurrentOduLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 121)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentOduLayerTable.setStatus("current")
_CwsPmExtendedCurrentOduLayerEntry_Object = MibTableRow
cwsPmExtendedCurrentOduLayerEntry = _CwsPmExtendedCurrentOduLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 121, 1)
)
cwsPmExtendedCurrentOduLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrentOduLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentOduLayerEntry.setStatus("current")


class _CwsPmExtendedCurrentOduLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrentOduLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrentOduLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrentOduLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrentOduLayerTableSnmpKey = _CwsPmExtendedCurrentOduLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 121, 1, 1),
    _CwsPmExtendedCurrentOduLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrentOduLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentOduLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrentOduLayerErroredSeconds_Type = Counter64
_CwsPmExtendedCurrentOduLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrentOduLayerErroredSeconds = _CwsPmExtendedCurrentOduLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 121, 1, 2),
    _CwsPmExtendedCurrentOduLayerErroredSeconds_Type()
)
cwsPmExtendedCurrentOduLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentOduLayerErroredSeconds.setStatus("current")
_CwsPmExtendedCurrentOduLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedCurrentOduLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrentOduLayerSeverelyErroredSeconds = _CwsPmExtendedCurrentOduLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 121, 1, 3),
    _CwsPmExtendedCurrentOduLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedCurrentOduLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentOduLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedCurrentOduLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedCurrentOduLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedCurrentOduLayerUnavailableSeconds = _CwsPmExtendedCurrentOduLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 121, 1, 4),
    _CwsPmExtendedCurrentOduLayerUnavailableSeconds_Type()
)
cwsPmExtendedCurrentOduLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrentOduLayerUnavailableSeconds.setStatus("current")
_CwsPmExtendedCurrent24hOduLayerTable_Object = MibTable
cwsPmExtendedCurrent24hOduLayerTable = _CwsPmExtendedCurrent24hOduLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 122)
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hOduLayerTable.setStatus("current")
_CwsPmExtendedCurrent24hOduLayerEntry_Object = MibTableRow
cwsPmExtendedCurrent24hOduLayerEntry = _CwsPmExtendedCurrent24hOduLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 122, 1)
)
cwsPmExtendedCurrent24hOduLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hOduLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hOduLayerEntry.setStatus("current")


class _CwsPmExtendedCurrent24hOduLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedCurrent24hOduLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedCurrent24hOduLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedCurrent24hOduLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedCurrent24hOduLayerTableSnmpKey = _CwsPmExtendedCurrent24hOduLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 122, 1, 1),
    _CwsPmExtendedCurrent24hOduLayerTableSnmpKey_Type()
)
cwsPmExtendedCurrent24hOduLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hOduLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedCurrent24hOduLayerErroredSeconds_Type = Counter64
_CwsPmExtendedCurrent24hOduLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrent24hOduLayerErroredSeconds = _CwsPmExtendedCurrent24hOduLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 122, 1, 2),
    _CwsPmExtendedCurrent24hOduLayerErroredSeconds_Type()
)
cwsPmExtendedCurrent24hOduLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hOduLayerErroredSeconds.setStatus("current")
_CwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds = _CwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 122, 1, 3),
    _CwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedCurrent24hOduLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedCurrent24hOduLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedCurrent24hOduLayerUnavailableSeconds = _CwsPmExtendedCurrent24hOduLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 122, 1, 4),
    _CwsPmExtendedCurrent24hOduLayerUnavailableSeconds_Type()
)
cwsPmExtendedCurrent24hOduLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedCurrent24hOduLayerUnavailableSeconds.setStatus("current")
_CwsPmExtendedHistoryOduLayerTable_Object = MibTable
cwsPmExtendedHistoryOduLayerTable = _CwsPmExtendedHistoryOduLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 123)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryOduLayerTable.setStatus("current")
_CwsPmExtendedHistoryOduLayerEntry_Object = MibTableRow
cwsPmExtendedHistoryOduLayerEntry = _CwsPmExtendedHistoryOduLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 123, 1)
)
cwsPmExtendedHistoryOduLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistoryOduLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryOduLayerEntry.setStatus("current")


class _CwsPmExtendedHistoryOduLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistoryOduLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistoryOduLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistoryOduLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistoryOduLayerTableSnmpKey = _CwsPmExtendedHistoryOduLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 123, 1, 1),
    _CwsPmExtendedHistoryOduLayerTableSnmpKey_Type()
)
cwsPmExtendedHistoryOduLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryOduLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistoryOduLayerErroredSeconds_Type = Counter64
_CwsPmExtendedHistoryOduLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistoryOduLayerErroredSeconds = _CwsPmExtendedHistoryOduLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 123, 1, 2),
    _CwsPmExtendedHistoryOduLayerErroredSeconds_Type()
)
cwsPmExtendedHistoryOduLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryOduLayerErroredSeconds.setStatus("current")
_CwsPmExtendedHistoryOduLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedHistoryOduLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistoryOduLayerSeverelyErroredSeconds = _CwsPmExtendedHistoryOduLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 123, 1, 3),
    _CwsPmExtendedHistoryOduLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedHistoryOduLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryOduLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedHistoryOduLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedHistoryOduLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedHistoryOduLayerUnavailableSeconds = _CwsPmExtendedHistoryOduLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 123, 1, 4),
    _CwsPmExtendedHistoryOduLayerUnavailableSeconds_Type()
)
cwsPmExtendedHistoryOduLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistoryOduLayerUnavailableSeconds.setStatus("current")
_CwsPmExtendedHistory24hOduLayerTable_Object = MibTable
cwsPmExtendedHistory24hOduLayerTable = _CwsPmExtendedHistory24hOduLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 124)
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hOduLayerTable.setStatus("current")
_CwsPmExtendedHistory24hOduLayerEntry_Object = MibTableRow
cwsPmExtendedHistory24hOduLayerEntry = _CwsPmExtendedHistory24hOduLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 124, 1)
)
cwsPmExtendedHistory24hOduLayerEntry.setIndexNames(
    (0, "CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
    (0, "CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hOduLayerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hOduLayerEntry.setStatus("current")


class _CwsPmExtendedHistory24hOduLayerTableSnmpKey_Type(Integer32):
    """Custom type cwsPmExtendedHistory24hOduLayerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPmExtendedHistory24hOduLayerTableSnmpKey_Type.__name__ = "Integer32"
_CwsPmExtendedHistory24hOduLayerTableSnmpKey_Object = MibTableColumn
cwsPmExtendedHistory24hOduLayerTableSnmpKey = _CwsPmExtendedHistory24hOduLayerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 124, 1, 1),
    _CwsPmExtendedHistory24hOduLayerTableSnmpKey_Type()
)
cwsPmExtendedHistory24hOduLayerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hOduLayerTableSnmpKey.setStatus("current")
_CwsPmExtendedHistory24hOduLayerErroredSeconds_Type = Counter64
_CwsPmExtendedHistory24hOduLayerErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistory24hOduLayerErroredSeconds = _CwsPmExtendedHistory24hOduLayerErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 124, 1, 2),
    _CwsPmExtendedHistory24hOduLayerErroredSeconds_Type()
)
cwsPmExtendedHistory24hOduLayerErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hOduLayerErroredSeconds.setStatus("current")
_CwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds_Type = Counter64
_CwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds_Object = MibTableColumn
cwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds = _CwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 124, 1, 3),
    _CwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds_Type()
)
cwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds.setStatus("current")
_CwsPmExtendedHistory24hOduLayerUnavailableSeconds_Type = Counter64
_CwsPmExtendedHistory24hOduLayerUnavailableSeconds_Object = MibTableColumn
cwsPmExtendedHistory24hOduLayerUnavailableSeconds = _CwsPmExtendedHistory24hOduLayerUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 124, 1, 4),
    _CwsPmExtendedHistory24hOduLayerUnavailableSeconds_Type()
)
cwsPmExtendedHistory24hOduLayerUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPmExtendedHistory24hOduLayerUnavailableSeconds.setStatus("current")

# Managed Objects groups

cienaWsPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 2, 1, 1)
)
cienaWsPmGroup.setObjects(
      *(("CIENA-WS-PM-MIB", "cwsPmGlobalConfigAdminState"),
        ("CIENA-WS-PM-MIB", "cwsPmGlobalConfigPersistenceInterval"),
        ("CIENA-WS-PM-MIB", "cwsPmGlobalConfigPersistenceStorageLocation"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateNextHistoryBinSave"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateCurrentFileSize"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateSaveStatus"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateInstancesSaved"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateElapsedSaveTime"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateLoadStatus"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateInstancesInFile"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateInstancesLoaded"),
        ("CIENA-WS-PM-MIB", "cwsPmPersistenceStateElapsedLoadTime"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesInstanceName"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesAdminState"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesOperationalState"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesInstanceType"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesBinCount"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesBinDuration"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesAttachedInterfaceType"),
        ("CIENA-WS-PM-MIB", "cwsPmInstancesAttachedInterfaceName"),
        ("CIENA-WS-PM-MIB", "cwsPmPortExtendedTxRxInstancesInstanceName"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedIdInstanceId"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedIdInstanceType"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedIdProfileType"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedStateAdminState"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedStateOperationalState"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedStateCurrentBinId"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedStateCollectionStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedStateCollectionEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesConfigurationMode"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesAlignment"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesConfiguredBinCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesConfiguredBinDuration"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesAttachedInterfacesType"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesAttachedInterfacesName"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedPropertiesAttachedInterfacesOperationalState"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentStateClearedDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentStatisticsFrameErrorRatio"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsUndersizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsOversizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsFragmentPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsJabberPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPackets64Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPackets65127Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPackets128255Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPackets256511Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPackets5121023Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentRxIfCountsPackets10241518Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsGiantPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsUnderrunPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueuePacketDropCountSummary"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ0PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ1PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ2PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ3PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ4PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ5PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ6PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentTxQueueQ7PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentMacLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsSyncHeaderErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsBlockErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentPcsMultilaneBipErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentOduLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentOduLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentOduLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentFecLayerCorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentFecLayerUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrentFecLayerSymbolErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hStateClearedDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hStatisticsFrameErrorRatio"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsUndersizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsOversizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsFragmentPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsJabberPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPackets64Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPackets65127Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPackets128255Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPackets256511Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsGiantPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsUnderrunPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueuePacketDropCountSummary"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ0PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ1PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ2PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ3PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ4PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ5PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ6PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hTxQueueQ7PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hMacLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsBlockErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hOduLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hOduLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hFecLayerCorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedCurrent24hFecLayerSymbolErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmBinsBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryStateEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryStatisticsFrameErrorRatio"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsUndersizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsOversizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsFragmentPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsJabberPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPackets64Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPackets65127Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPackets128255Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPackets256511Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPackets5121023Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryRxIfCountsPackets10241518Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsGiantPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsUnderrunPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryTxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueuePacketDropCountSummary"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ0PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ1PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ2PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ3PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ4PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ5PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ6PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmCurrentBinTxQueueQ7PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryMacLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsSyncHeaderErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsBlockErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryPcsMultilaneBipErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryOduLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryOduLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryOduLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryFecLayerCorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryFecLayerUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistoryFecLayerSymbolErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hStateEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hStatisticsFrameErrorRatio"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsUndersizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsOversizedPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsFragmentPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsJabberPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPackets64Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPackets65127Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPackets128255Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPackets256511Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPackets5121023Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hRxIfCountsPackets10241518Octet"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsBytes"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsCrcErroredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsMulticastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsBroadcastPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsPausePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsGiantPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsUnderrunPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueuePacketDropCountSummary"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ0PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ1PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ2PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ3PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ4PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ5PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ6PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hTxQueueQ7PacketDropCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hMacLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsSyncHeaderErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsBlockErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hPcsMultilaneBipErrorsCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hOduLayerErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hOduLayerUnavailableSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hFecLayerCorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hFecLayerUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmExtendedHistory24hFecLayerSymbolErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmPtpBasicInstancesInstanceName"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicIdInstanceId"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicIdInstanceType"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicIdProfileType"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicStateAdminState"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicStateOperationalState"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicStateCurrentBinId"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicStateCollectionStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicStateCollectionEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicPropertiesConfigurationMode"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicPropertiesAlignment"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicPropertiesConfiguredBinCount"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicPropertiesConfiguredBinDuration"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicAttachedInterfaceType"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicAttachedInterfaceName"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicAttachedInterfaceOperationalState"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentStateClearedDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentStatisticsNumberOfChannels"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalPowerChannelNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalRxPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalRxPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalRxPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalRxPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalTxPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalTxPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalTxPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentOpticalTxPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentChannelRxPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentChannelRxPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentChannelRxPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrentChannelRxPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hStateClearedDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hBinStatisticsNumberOfChannels"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hOpticalPowerChannelNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxOpticalPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxOpticalPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxOpticalPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxOpticalPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hTxOpticalPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hTxOpticalPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hTxOpticalPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hTxOpticalPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxChannelPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxChannelPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxChannelPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicCurrent24hRxChannelPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryBinsBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryStateEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryStatisticsNumberOfChannels"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryOpticalPowerChannelNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryRxOpticalPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryRxOpticalPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryRxOpticalPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryRxOpticalPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxOpticalPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxOpticalPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxOpticalPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxOpticalPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxChannelPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxChannelPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxChannelPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistoryTxChannelPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hStateEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hStatisticsNumberOfChannels"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hOpticalPowerChannelNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxOpticalPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxOpticalPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxOpticalPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxOpticalPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hTxOpticalPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hTxOpticalPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hTxOpticalPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hTxOpticalPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxChannelPowerActual"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxChannelPowerMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxChannelPowerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmBasicHistory24hRxChannelPowerAverage"),
        ("CIENA-WS-PM-MIB", "cwsPmPtpAdvancedInstancesInstanceName"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedIdInstanceId"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedIdInstanceType"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedIdProfileType"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedStateAdminState"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedStateOperationalState"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedStateCurrentBinId"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedStateCollectionStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedStateCollectionEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedPropertiesConfigurationMode"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedPropertiesAlignment"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedPropertiesConfiguredBinCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedPropertiesConfiguredBinDuration"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedAttachedInterfaceType"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedAttachedInterfaceName"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedAttachedInterfaceOperationalState"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentStateClearedDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentStatisticsPostFecBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmPreFecBitErrorRateBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmPreFecBitErrorRateMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentQFactorQFactor"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentQFactorMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentQFactorMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentFecErrorFrameErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentFecErrorFrameErrorCountSecond"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentFecErrorUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hStateClearedDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hPreFecBerBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hPreFecBerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hQFactorQFactor"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hQFactorMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hQFactorMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hFecErrorFrameErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryBinsBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryStateEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryStatisticsPostFecBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryPreFecBerBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryPreFecBerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryQFactorQFactor"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryQFactorMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryQFactorMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryFecErrorFrameErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryFecErrorFrameErrorCountSecond"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryFecErrorUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hIdBinNumber"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hIdBinName"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hStateStartDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hStateEndDateTime"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hStateState"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hPreFecBerBitErrorRate"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hPreFecBerMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hQFactorQFactor"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hQFactorMinimum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hQFactorMaximum"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hFecErrorFrameErrorCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount"),
        ("CIENA-WS-PM-MIB", "cwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds"))
)
if mibBuilder.loadTexts:
    cienaWsPmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 22, 2, 2, 1)
)
cienaWsPmCompliance.setObjects(
    ("CIENA-WS-PM-MIB", "cienaWsPmGroup")
)
if mibBuilder.loadTexts:
    cienaWsPmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PM-MIB",
    **{"PmAlignment": PmAlignment,
       "PmBinState": PmBinState,
       "PmConfigurationMode": PmConfigurationMode,
       "PmInstanceType": PmInstanceType,
       "PmInterfaceType": PmInterfaceType,
       "PmPersistenceState": PmPersistenceState,
       "PmPersistenceStatus": PmPersistenceStatus,
       "PmProfileType": PmProfileType,
       "cienaWsPmMIB": cienaWsPmMIB,
       "cienaWsPmObjects": cienaWsPmObjects,
       "cienaWsPmConformance": cienaWsPmConformance,
       "cienaWsPmGroups": cienaWsPmGroups,
       "cienaWsPmGroup": cienaWsPmGroup,
       "cienaWsPmCompliances": cienaWsPmCompliances,
       "cienaWsPmCompliance": cienaWsPmCompliance,
       "cwsPmGlobalConfigTable": cwsPmGlobalConfigTable,
       "cwsPmGlobalConfigEntry": cwsPmGlobalConfigEntry,
       "cwsPmGlobalConfigTableSnmpKey": cwsPmGlobalConfigTableSnmpKey,
       "cwsPmGlobalConfigAdminState": cwsPmGlobalConfigAdminState,
       "cwsPmGlobalConfigPersistenceInterval": cwsPmGlobalConfigPersistenceInterval,
       "cwsPmGlobalConfigPersistenceStorageLocation": cwsPmGlobalConfigPersistenceStorageLocation,
       "cwsPmPersistenceStateTable": cwsPmPersistenceStateTable,
       "cwsPmPersistenceStateEntry": cwsPmPersistenceStateEntry,
       "cwsPmPersistenceStateTableSnmpKey": cwsPmPersistenceStateTableSnmpKey,
       "cwsPmPersistenceStateState": cwsPmPersistenceStateState,
       "cwsPmPersistenceStateNextHistoryBinSave": cwsPmPersistenceStateNextHistoryBinSave,
       "cwsPmPersistenceStateCurrentFileSize": cwsPmPersistenceStateCurrentFileSize,
       "cwsPmPersistenceStateSaveStatus": cwsPmPersistenceStateSaveStatus,
       "cwsPmPersistenceStateInstancesSaved": cwsPmPersistenceStateInstancesSaved,
       "cwsPmPersistenceStateElapsedSaveTime": cwsPmPersistenceStateElapsedSaveTime,
       "cwsPmPersistenceStateLoadStatus": cwsPmPersistenceStateLoadStatus,
       "cwsPmPersistenceStateInstancesInFile": cwsPmPersistenceStateInstancesInFile,
       "cwsPmPersistenceStateInstancesLoaded": cwsPmPersistenceStateInstancesLoaded,
       "cwsPmPersistenceStateElapsedLoadTime": cwsPmPersistenceStateElapsedLoadTime,
       "cwsPmInstancesTable": cwsPmInstancesTable,
       "cwsPmInstancesEntry": cwsPmInstancesEntry,
       "cwsPmInstancesInstanceId": cwsPmInstancesInstanceId,
       "cwsPmInstancesInstanceName": cwsPmInstancesInstanceName,
       "cwsPmInstancesAdminState": cwsPmInstancesAdminState,
       "cwsPmInstancesOperationalState": cwsPmInstancesOperationalState,
       "cwsPmInstancesInstanceType": cwsPmInstancesInstanceType,
       "cwsPmInstancesBinCount": cwsPmInstancesBinCount,
       "cwsPmInstancesBinDuration": cwsPmInstancesBinDuration,
       "cwsPmInstancesAttachedInterfaceType": cwsPmInstancesAttachedInterfaceType,
       "cwsPmInstancesAttachedInterfaceName": cwsPmInstancesAttachedInterfaceName,
       "cwsPmPortExtendedTxRxInstancesTable": cwsPmPortExtendedTxRxInstancesTable,
       "cwsPmPortExtendedTxRxInstancesEntry": cwsPmPortExtendedTxRxInstancesEntry,
       "cwsPmPortExtendedTxRxInstancesInstanceName": cwsPmPortExtendedTxRxInstancesInstanceName,
       "cwsPmExtendedIdTable": cwsPmExtendedIdTable,
       "cwsPmExtendedIdEntry": cwsPmExtendedIdEntry,
       "cwsPmExtendedIdTableSnmpKey": cwsPmExtendedIdTableSnmpKey,
       "cwsPmExtendedIdInstanceId": cwsPmExtendedIdInstanceId,
       "cwsPmExtendedIdInstanceType": cwsPmExtendedIdInstanceType,
       "cwsPmExtendedIdProfileType": cwsPmExtendedIdProfileType,
       "cwsPmExtendedStateTable": cwsPmExtendedStateTable,
       "cwsPmExtendedStateEntry": cwsPmExtendedStateEntry,
       "cwsPmExtendedStateTableSnmpKey": cwsPmExtendedStateTableSnmpKey,
       "cwsPmExtendedStateAdminState": cwsPmExtendedStateAdminState,
       "cwsPmExtendedStateOperationalState": cwsPmExtendedStateOperationalState,
       "cwsPmExtendedStateCurrentBinId": cwsPmExtendedStateCurrentBinId,
       "cwsPmExtendedStateCollectionStartDateTime": cwsPmExtendedStateCollectionStartDateTime,
       "cwsPmExtendedStateCollectionEndDateTime": cwsPmExtendedStateCollectionEndDateTime,
       "cwsPmExtendedPropertiesTable": cwsPmExtendedPropertiesTable,
       "cwsPmExtendedPropertiesEntry": cwsPmExtendedPropertiesEntry,
       "cwsPmExtendedPropertiesTableSnmpKey": cwsPmExtendedPropertiesTableSnmpKey,
       "cwsPmExtendedPropertiesConfigurationMode": cwsPmExtendedPropertiesConfigurationMode,
       "cwsPmExtendedPropertiesAlignment": cwsPmExtendedPropertiesAlignment,
       "cwsPmExtendedPropertiesConfiguredBinCount": cwsPmExtendedPropertiesConfiguredBinCount,
       "cwsPmExtendedPropertiesConfiguredBinDuration": cwsPmExtendedPropertiesConfiguredBinDuration,
       "cwsPmExtendedPropertiesAttachedInterfacesTable": cwsPmExtendedPropertiesAttachedInterfacesTable,
       "cwsPmExtendedPropertiesAttachedInterfacesEntry": cwsPmExtendedPropertiesAttachedInterfacesEntry,
       "cwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey": cwsPmExtendedPropertiesAttachedInterfacesTableSnmpKey,
       "cwsPmExtendedPropertiesAttachedInterfacesType": cwsPmExtendedPropertiesAttachedInterfacesType,
       "cwsPmExtendedPropertiesAttachedInterfacesName": cwsPmExtendedPropertiesAttachedInterfacesName,
       "cwsPmExtendedPropertiesAttachedInterfacesOperationalState": cwsPmExtendedPropertiesAttachedInterfacesOperationalState,
       "cwsPmExtendedCurrentIdTable": cwsPmExtendedCurrentIdTable,
       "cwsPmExtendedCurrentIdEntry": cwsPmExtendedCurrentIdEntry,
       "cwsPmExtendedCurrentIdTableSnmpKey": cwsPmExtendedCurrentIdTableSnmpKey,
       "cwsPmExtendedCurrentIdBinNumber": cwsPmExtendedCurrentIdBinNumber,
       "cwsPmExtendedCurrentIdBinName": cwsPmExtendedCurrentIdBinName,
       "cwsPmExtendedCurrentStateTable": cwsPmExtendedCurrentStateTable,
       "cwsPmExtendedCurrentStateEntry": cwsPmExtendedCurrentStateEntry,
       "cwsPmExtendedCurrentStateTableSnmpKey": cwsPmExtendedCurrentStateTableSnmpKey,
       "cwsPmExtendedCurrentStateStartDateTime": cwsPmExtendedCurrentStateStartDateTime,
       "cwsPmExtendedCurrentStateClearedDateTime": cwsPmExtendedCurrentStateClearedDateTime,
       "cwsPmExtendedCurrentStateState": cwsPmExtendedCurrentStateState,
       "cwsPmExtendedCurrentStatisticsTable": cwsPmExtendedCurrentStatisticsTable,
       "cwsPmExtendedCurrentStatisticsEntry": cwsPmExtendedCurrentStatisticsEntry,
       "cwsPmExtendedCurrentStatisticsTableSnmpKey": cwsPmExtendedCurrentStatisticsTableSnmpKey,
       "cwsPmExtendedCurrentStatisticsFrameErrorRatio": cwsPmExtendedCurrentStatisticsFrameErrorRatio,
       "cwsPmExtendedCurrentRxIfCountsTable": cwsPmExtendedCurrentRxIfCountsTable,
       "cwsPmExtendedCurrentRxIfCountsEntry": cwsPmExtendedCurrentRxIfCountsEntry,
       "cwsPmExtendedCurrentRxIfCountsTableSnmpKey": cwsPmExtendedCurrentRxIfCountsTableSnmpKey,
       "cwsPmExtendedCurrentRxIfCountsBytes": cwsPmExtendedCurrentRxIfCountsBytes,
       "cwsPmExtendedCurrentRxIfCountsPackets": cwsPmExtendedCurrentRxIfCountsPackets,
       "cwsPmExtendedCurrentRxIfCountsCrcErroredPackets": cwsPmExtendedCurrentRxIfCountsCrcErroredPackets,
       "cwsPmExtendedCurrentRxIfCountsMulticastPackets": cwsPmExtendedCurrentRxIfCountsMulticastPackets,
       "cwsPmExtendedCurrentRxIfCountsBroadcastPackets": cwsPmExtendedCurrentRxIfCountsBroadcastPackets,
       "cwsPmExtendedCurrentRxIfCountsPausePackets": cwsPmExtendedCurrentRxIfCountsPausePackets,
       "cwsPmExtendedCurrentRxIfCountsUndersizedPackets": cwsPmExtendedCurrentRxIfCountsUndersizedPackets,
       "cwsPmExtendedCurrentRxIfCountsOversizedPackets": cwsPmExtendedCurrentRxIfCountsOversizedPackets,
       "cwsPmExtendedCurrentRxIfCountsFragmentPackets": cwsPmExtendedCurrentRxIfCountsFragmentPackets,
       "cwsPmExtendedCurrentRxIfCountsJabberPackets": cwsPmExtendedCurrentRxIfCountsJabberPackets,
       "cwsPmExtendedCurrentRxIfCountsLengthOutRangePackets": cwsPmExtendedCurrentRxIfCountsLengthOutRangePackets,
       "cwsPmExtendedCurrentRxIfCountsPackets64Octet": cwsPmExtendedCurrentRxIfCountsPackets64Octet,
       "cwsPmExtendedCurrentRxIfCountsPackets65127Octet": cwsPmExtendedCurrentRxIfCountsPackets65127Octet,
       "cwsPmExtendedCurrentRxIfCountsPackets128255Octet": cwsPmExtendedCurrentRxIfCountsPackets128255Octet,
       "cwsPmExtendedCurrentRxIfCountsPackets256511Octet": cwsPmExtendedCurrentRxIfCountsPackets256511Octet,
       "cwsPmExtendedCurrentRxIfCountsPackets5121023Octet": cwsPmExtendedCurrentRxIfCountsPackets5121023Octet,
       "cwsPmExtendedCurrentRxIfCountsPackets10241518Octet": cwsPmExtendedCurrentRxIfCountsPackets10241518Octet,
       "cwsPmExtendedCurrentRxIfCountsAverageLinkUtilization": cwsPmExtendedCurrentRxIfCountsAverageLinkUtilization,
       "cwsPmExtendedCurrentTxIfCountsTable": cwsPmExtendedCurrentTxIfCountsTable,
       "cwsPmExtendedCurrentTxIfCountsEntry": cwsPmExtendedCurrentTxIfCountsEntry,
       "cwsPmExtendedCurrentTxIfCountsTableSnmpKey": cwsPmExtendedCurrentTxIfCountsTableSnmpKey,
       "cwsPmExtendedCurrentTxIfCountsBytes": cwsPmExtendedCurrentTxIfCountsBytes,
       "cwsPmExtendedCurrentTxIfCountsPackets": cwsPmExtendedCurrentTxIfCountsPackets,
       "cwsPmExtendedCurrentTxIfCountsCrcErroredPackets": cwsPmExtendedCurrentTxIfCountsCrcErroredPackets,
       "cwsPmExtendedCurrentTxIfCountsMulticastPackets": cwsPmExtendedCurrentTxIfCountsMulticastPackets,
       "cwsPmExtendedCurrentTxIfCountsBroadcastPackets": cwsPmExtendedCurrentTxIfCountsBroadcastPackets,
       "cwsPmExtendedCurrentTxIfCountsPausePackets": cwsPmExtendedCurrentTxIfCountsPausePackets,
       "cwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets": cwsPmExtendedCurrentTxIfCountsExcessiveDeferredPackets,
       "cwsPmExtendedCurrentTxIfCountsGiantPackets": cwsPmExtendedCurrentTxIfCountsGiantPackets,
       "cwsPmExtendedCurrentTxIfCountsUnderrunPackets": cwsPmExtendedCurrentTxIfCountsUnderrunPackets,
       "cwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets": cwsPmExtendedCurrentTxIfCountsLengthCheckErrorPackets,
       "cwsPmExtendedCurrentTxIfCountsLengthOutRangePackets": cwsPmExtendedCurrentTxIfCountsLengthOutRangePackets,
       "cwsPmExtendedCurrentTxIfCountsAverageLinkUtilization": cwsPmExtendedCurrentTxIfCountsAverageLinkUtilization,
       "cwsPmExtendedCurrentTxQueueTable": cwsPmExtendedCurrentTxQueueTable,
       "cwsPmExtendedCurrentTxQueueEntry": cwsPmExtendedCurrentTxQueueEntry,
       "cwsPmExtendedCurrentTxQueueTableSnmpKey": cwsPmExtendedCurrentTxQueueTableSnmpKey,
       "cwsPmExtendedCurrentTxQueuePacketDropCountSummary": cwsPmExtendedCurrentTxQueuePacketDropCountSummary,
       "cwsPmExtendedCurrentTxQueueQ0PacketDropCount": cwsPmExtendedCurrentTxQueueQ0PacketDropCount,
       "cwsPmExtendedCurrentTxQueueQ1PacketDropCount": cwsPmExtendedCurrentTxQueueQ1PacketDropCount,
       "cwsPmExtendedCurrentTxQueueQ2PacketDropCount": cwsPmExtendedCurrentTxQueueQ2PacketDropCount,
       "cwsPmExtendedCurrentTxQueueQ3PacketDropCount": cwsPmExtendedCurrentTxQueueQ3PacketDropCount,
       "cwsPmExtendedCurrentTxQueueQ4PacketDropCount": cwsPmExtendedCurrentTxQueueQ4PacketDropCount,
       "cwsPmExtendedCurrentTxQueueQ5PacketDropCount": cwsPmExtendedCurrentTxQueueQ5PacketDropCount,
       "cwsPmExtendedCurrentTxQueueQ6PacketDropCount": cwsPmExtendedCurrentTxQueueQ6PacketDropCount,
       "cwsPmExtendedCurrentTxQueueQ7PacketDropCount": cwsPmExtendedCurrentTxQueueQ7PacketDropCount,
       "cwsPmExtendedCurrentMacLayerTable": cwsPmExtendedCurrentMacLayerTable,
       "cwsPmExtendedCurrentMacLayerEntry": cwsPmExtendedCurrentMacLayerEntry,
       "cwsPmExtendedCurrentMacLayerTableSnmpKey": cwsPmExtendedCurrentMacLayerTableSnmpKey,
       "cwsPmExtendedCurrentMacLayerUnavailableSeconds": cwsPmExtendedCurrentMacLayerUnavailableSeconds,
       "cwsPmExtendedCurrentPcsLayerTable": cwsPmExtendedCurrentPcsLayerTable,
       "cwsPmExtendedCurrentPcsLayerEntry": cwsPmExtendedCurrentPcsLayerEntry,
       "cwsPmExtendedCurrentPcsLayerTableSnmpKey": cwsPmExtendedCurrentPcsLayerTableSnmpKey,
       "cwsPmExtendedCurrentPcsLayerErroredSeconds": cwsPmExtendedCurrentPcsLayerErroredSeconds,
       "cwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds": cwsPmExtendedCurrentPcsLayerSeverelyErroredSeconds,
       "cwsPmExtendedCurrentPcsLayerUnavailableSeconds": cwsPmExtendedCurrentPcsLayerUnavailableSeconds,
       "cwsPmExtendedCurrentPcsSyncHeaderErrorsTable": cwsPmExtendedCurrentPcsSyncHeaderErrorsTable,
       "cwsPmExtendedCurrentPcsSyncHeaderErrorsEntry": cwsPmExtendedCurrentPcsSyncHeaderErrorsEntry,
       "cwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey": cwsPmExtendedCurrentPcsSyncHeaderErrorsTableSnmpKey,
       "cwsPmExtendedCurrentPcsSyncHeaderErrorsCount": cwsPmExtendedCurrentPcsSyncHeaderErrorsCount,
       "cwsPmExtendedCurrentPcsBlockErrorsTable": cwsPmExtendedCurrentPcsBlockErrorsTable,
       "cwsPmExtendedCurrentPcsBlockErrorsEntry": cwsPmExtendedCurrentPcsBlockErrorsEntry,
       "cwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey": cwsPmExtendedCurrentPcsBlockErrorsTableSnmpKey,
       "cwsPmExtendedCurrentPcsBlockErrorsCount": cwsPmExtendedCurrentPcsBlockErrorsCount,
       "cwsPmExtendedCurrentPcsMultilaneBipErrorsTable": cwsPmExtendedCurrentPcsMultilaneBipErrorsTable,
       "cwsPmExtendedCurrentPcsMultilaneBipErrorsEntry": cwsPmExtendedCurrentPcsMultilaneBipErrorsEntry,
       "cwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey": cwsPmExtendedCurrentPcsMultilaneBipErrorsTableSnmpKey,
       "cwsPmExtendedCurrentPcsMultilaneBipErrorsCount": cwsPmExtendedCurrentPcsMultilaneBipErrorsCount,
       "cwsPmExtendedCurrentFecLayerTable": cwsPmExtendedCurrentFecLayerTable,
       "cwsPmExtendedCurrentFecLayerEntry": cwsPmExtendedCurrentFecLayerEntry,
       "cwsPmExtendedCurrentFecLayerTableSnmpKey": cwsPmExtendedCurrentFecLayerTableSnmpKey,
       "cwsPmExtendedCurrentFecLayerCorrectedBlockCount": cwsPmExtendedCurrentFecLayerCorrectedBlockCount,
       "cwsPmExtendedCurrentFecLayerUncorrectedBlockCount": cwsPmExtendedCurrentFecLayerUncorrectedBlockCount,
       "cwsPmExtendedCurrentFecLayerSymbolErrorCount": cwsPmExtendedCurrentFecLayerSymbolErrorCount,
       "cwsPmExtendedCurrent24hIdTable": cwsPmExtendedCurrent24hIdTable,
       "cwsPmExtendedCurrent24hIdEntry": cwsPmExtendedCurrent24hIdEntry,
       "cwsPmExtendedCurrent24hIdTableSnmpKey": cwsPmExtendedCurrent24hIdTableSnmpKey,
       "cwsPmExtendedCurrent24hIdBinNumber": cwsPmExtendedCurrent24hIdBinNumber,
       "cwsPmExtendedCurrent24hIdBinName": cwsPmExtendedCurrent24hIdBinName,
       "cwsPmExtendedCurrent24hStateTable": cwsPmExtendedCurrent24hStateTable,
       "cwsPmExtendedCurrent24hStateEntry": cwsPmExtendedCurrent24hStateEntry,
       "cwsPmExtendedCurrent24hStateTableSnmpKey": cwsPmExtendedCurrent24hStateTableSnmpKey,
       "cwsPmExtendedCurrent24hStateStartDateTime": cwsPmExtendedCurrent24hStateStartDateTime,
       "cwsPmExtendedCurrent24hStateClearedDateTime": cwsPmExtendedCurrent24hStateClearedDateTime,
       "cwsPmExtendedCurrent24hStateState": cwsPmExtendedCurrent24hStateState,
       "cwsPmExtendedCurrent24hStatisticsTable": cwsPmExtendedCurrent24hStatisticsTable,
       "cwsPmExtendedCurrent24hStatisticsEntry": cwsPmExtendedCurrent24hStatisticsEntry,
       "cwsPmExtendedCurrent24hStatisticsTableSnmpKey": cwsPmExtendedCurrent24hStatisticsTableSnmpKey,
       "cwsPmExtendedCurrent24hStatisticsFrameErrorRatio": cwsPmExtendedCurrent24hStatisticsFrameErrorRatio,
       "cwsPmExtendedCurrent24hRxIfCountsTable": cwsPmExtendedCurrent24hRxIfCountsTable,
       "cwsPmExtendedCurrent24hRxIfCountsEntry": cwsPmExtendedCurrent24hRxIfCountsEntry,
       "cwsPmExtendedCurrent24hRxIfCountsTableSnmpKey": cwsPmExtendedCurrent24hRxIfCountsTableSnmpKey,
       "cwsPmExtendedCurrent24hRxIfCountsBytes": cwsPmExtendedCurrent24hRxIfCountsBytes,
       "cwsPmExtendedCurrent24hRxIfCountsPackets": cwsPmExtendedCurrent24hRxIfCountsPackets,
       "cwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets": cwsPmExtendedCurrent24hRxIfCountsCrcErroredPackets,
       "cwsPmExtendedCurrent24hRxIfCountsMulticastPackets": cwsPmExtendedCurrent24hRxIfCountsMulticastPackets,
       "cwsPmExtendedCurrent24hRxIfCountsBroadcastPackets": cwsPmExtendedCurrent24hRxIfCountsBroadcastPackets,
       "cwsPmExtendedCurrent24hRxIfCountsPausePackets": cwsPmExtendedCurrent24hRxIfCountsPausePackets,
       "cwsPmExtendedCurrent24hRxIfCountsUndersizedPackets": cwsPmExtendedCurrent24hRxIfCountsUndersizedPackets,
       "cwsPmExtendedCurrent24hRxIfCountsOversizedPackets": cwsPmExtendedCurrent24hRxIfCountsOversizedPackets,
       "cwsPmExtendedCurrent24hRxIfCountsFragmentPackets": cwsPmExtendedCurrent24hRxIfCountsFragmentPackets,
       "cwsPmExtendedCurrent24hRxIfCountsJabberPackets": cwsPmExtendedCurrent24hRxIfCountsJabberPackets,
       "cwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets": cwsPmExtendedCurrent24hRxIfCountsLengthOutRangePackets,
       "cwsPmExtendedCurrent24hRxIfCountsPackets64Octet": cwsPmExtendedCurrent24hRxIfCountsPackets64Octet,
       "cwsPmExtendedCurrent24hRxIfCountsPackets65127Octet": cwsPmExtendedCurrent24hRxIfCountsPackets65127Octet,
       "cwsPmExtendedCurrent24hRxIfCountsPackets128255Octet": cwsPmExtendedCurrent24hRxIfCountsPackets128255Octet,
       "cwsPmExtendedCurrent24hRxIfCountsPackets256511Octet": cwsPmExtendedCurrent24hRxIfCountsPackets256511Octet,
       "cwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet": cwsPmExtendedCurrent24hRxIfCountsPackets5121023Octet,
       "cwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet": cwsPmExtendedCurrent24hRxIfCountsPackets10241518Octet,
       "cwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization": cwsPmExtendedCurrent24hRxIfCountsAverageLinkUtilization,
       "cwsPmExtendedCurrent24hTxIfCountsTable": cwsPmExtendedCurrent24hTxIfCountsTable,
       "cwsPmExtendedCurrent24hTxIfCountsEntry": cwsPmExtendedCurrent24hTxIfCountsEntry,
       "cwsPmExtendedCurrent24hTxIfCountsTableSnmpKey": cwsPmExtendedCurrent24hTxIfCountsTableSnmpKey,
       "cwsPmExtendedCurrent24hTxIfCountsBytes": cwsPmExtendedCurrent24hTxIfCountsBytes,
       "cwsPmExtendedCurrent24hTxIfCountsPackets": cwsPmExtendedCurrent24hTxIfCountsPackets,
       "cwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets": cwsPmExtendedCurrent24hTxIfCountsCrcErroredPackets,
       "cwsPmExtendedCurrent24hTxIfCountsMulticastPackets": cwsPmExtendedCurrent24hTxIfCountsMulticastPackets,
       "cwsPmExtendedCurrent24hTxIfCountsBroadcastPackets": cwsPmExtendedCurrent24hTxIfCountsBroadcastPackets,
       "cwsPmExtendedCurrent24hTxIfCountsPausePackets": cwsPmExtendedCurrent24hTxIfCountsPausePackets,
       "cwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets": cwsPmExtendedCurrent24hTxIfCountsExcessiveDeferredPackets,
       "cwsPmExtendedCurrent24hTxIfCountsGiantPackets": cwsPmExtendedCurrent24hTxIfCountsGiantPackets,
       "cwsPmExtendedCurrent24hTxIfCountsUnderrunPackets": cwsPmExtendedCurrent24hTxIfCountsUnderrunPackets,
       "cwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets": cwsPmExtendedCurrent24hTxIfCountsLengthCheckErrorPackets,
       "cwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets": cwsPmExtendedCurrent24hTxIfCountsLengthOutRangePackets,
       "cwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization": cwsPmExtendedCurrent24hTxIfCountsAverageLinkUtilization,
       "cwsPmExtendedCurrent24hTxQueueTable": cwsPmExtendedCurrent24hTxQueueTable,
       "cwsPmExtendedCurrent24hTxQueueEntry": cwsPmExtendedCurrent24hTxQueueEntry,
       "cwsPmExtendedCurrent24hTxQueueTableSnmpKey": cwsPmExtendedCurrent24hTxQueueTableSnmpKey,
       "cwsPmExtendedCurrent24hTxQueuePacketDropCountSummary": cwsPmExtendedCurrent24hTxQueuePacketDropCountSummary,
       "cwsPmExtendedCurrent24hTxQueueQ0PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ0PacketDropCount,
       "cwsPmExtendedCurrent24hTxQueueQ1PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ1PacketDropCount,
       "cwsPmExtendedCurrent24hTxQueueQ2PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ2PacketDropCount,
       "cwsPmExtendedCurrent24hTxQueueQ3PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ3PacketDropCount,
       "cwsPmExtendedCurrent24hTxQueueQ4PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ4PacketDropCount,
       "cwsPmExtendedCurrent24hTxQueueQ5PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ5PacketDropCount,
       "cwsPmExtendedCurrent24hTxQueueQ6PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ6PacketDropCount,
       "cwsPmExtendedCurrent24hTxQueueQ7PacketDropCount": cwsPmExtendedCurrent24hTxQueueQ7PacketDropCount,
       "cwsPmExtendedCurrent24hMacLayerTable": cwsPmExtendedCurrent24hMacLayerTable,
       "cwsPmExtendedCurrent24hMacLayerEntry": cwsPmExtendedCurrent24hMacLayerEntry,
       "cwsPmExtendedCurrent24hMacLayerTableSnmpKey": cwsPmExtendedCurrent24hMacLayerTableSnmpKey,
       "cwsPmExtendedCurrent24hMacLayerUnavailableSeconds": cwsPmExtendedCurrent24hMacLayerUnavailableSeconds,
       "cwsPmExtendedCurrent24hPcsLayerTable": cwsPmExtendedCurrent24hPcsLayerTable,
       "cwsPmExtendedCurrent24hPcsLayerEntry": cwsPmExtendedCurrent24hPcsLayerEntry,
       "cwsPmExtendedCurrent24hPcsLayerTableSnmpKey": cwsPmExtendedCurrent24hPcsLayerTableSnmpKey,
       "cwsPmExtendedCurrent24hPcsLayerErroredSeconds": cwsPmExtendedCurrent24hPcsLayerErroredSeconds,
       "cwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds": cwsPmExtendedCurrent24hPcsLayerSeverelyErroredSeconds,
       "cwsPmExtendedCurrent24hPcsLayerUnavailableSeconds": cwsPmExtendedCurrent24hPcsLayerUnavailableSeconds,
       "cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTable": cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTable,
       "cwsPmExtendedCurrent24hPcsSyncHeaderErrorsEntry": cwsPmExtendedCurrent24hPcsSyncHeaderErrorsEntry,
       "cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey": cwsPmExtendedCurrent24hPcsSyncHeaderErrorsTableSnmpKey,
       "cwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount": cwsPmExtendedCurrent24hPcsSyncHeaderErrorsCount,
       "cwsPmExtendedCurrent24hPcsBlockErrorsTable": cwsPmExtendedCurrent24hPcsBlockErrorsTable,
       "cwsPmExtendedCurrent24hPcsBlockErrorsEntry": cwsPmExtendedCurrent24hPcsBlockErrorsEntry,
       "cwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey": cwsPmExtendedCurrent24hPcsBlockErrorsTableSnmpKey,
       "cwsPmExtendedCurrent24hPcsBlockErrorsCount": cwsPmExtendedCurrent24hPcsBlockErrorsCount,
       "cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTable": cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTable,
       "cwsPmExtendedCurrent24hPcsMultilaneBipErrorsEntry": cwsPmExtendedCurrent24hPcsMultilaneBipErrorsEntry,
       "cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey": cwsPmExtendedCurrent24hPcsMultilaneBipErrorsTableSnmpKey,
       "cwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount": cwsPmExtendedCurrent24hPcsMultilaneBipErrorsCount,
       "cwsPmExtendedCurrent24hFecLayerTable": cwsPmExtendedCurrent24hFecLayerTable,
       "cwsPmExtendedCurrent24hFecLayerEntry": cwsPmExtendedCurrent24hFecLayerEntry,
       "cwsPmExtendedCurrent24hFecLayerTableSnmpKey": cwsPmExtendedCurrent24hFecLayerTableSnmpKey,
       "cwsPmExtendedCurrent24hFecLayerCorrectedBlockCount": cwsPmExtendedCurrent24hFecLayerCorrectedBlockCount,
       "cwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount": cwsPmExtendedCurrent24hFecLayerUncorrectedBlockCount,
       "cwsPmExtendedCurrent24hFecLayerSymbolErrorCount": cwsPmExtendedCurrent24hFecLayerSymbolErrorCount,
       "cwsPmBinsTable": cwsPmBinsTable,
       "cwsPmBinsEntry": cwsPmBinsEntry,
       "cwsPmBinsBinNumber": cwsPmBinsBinNumber,
       "cwsPmExtendedHistoryStateTable": cwsPmExtendedHistoryStateTable,
       "cwsPmExtendedHistoryStateEntry": cwsPmExtendedHistoryStateEntry,
       "cwsPmExtendedHistoryStateTableSnmpKey": cwsPmExtendedHistoryStateTableSnmpKey,
       "cwsPmExtendedHistoryStateStartDateTime": cwsPmExtendedHistoryStateStartDateTime,
       "cwsPmExtendedHistoryStateEndDateTime": cwsPmExtendedHistoryStateEndDateTime,
       "cwsPmExtendedHistoryStateState": cwsPmExtendedHistoryStateState,
       "cwsPmExtendedHistoryStatisticsTable": cwsPmExtendedHistoryStatisticsTable,
       "cwsPmExtendedHistoryStatisticsEntry": cwsPmExtendedHistoryStatisticsEntry,
       "cwsPmExtendedHistoryStatisticsTableSnmpKey": cwsPmExtendedHistoryStatisticsTableSnmpKey,
       "cwsPmExtendedHistoryStatisticsFrameErrorRatio": cwsPmExtendedHistoryStatisticsFrameErrorRatio,
       "cwsPmExtendedHistoryRxIfCountsTable": cwsPmExtendedHistoryRxIfCountsTable,
       "cwsPmExtendedHistoryRxIfCountsEntry": cwsPmExtendedHistoryRxIfCountsEntry,
       "cwsPmExtendedHistoryRxIfCountsTableSnmpKey": cwsPmExtendedHistoryRxIfCountsTableSnmpKey,
       "cwsPmExtendedHistoryRxIfCountsBytes": cwsPmExtendedHistoryRxIfCountsBytes,
       "cwsPmExtendedHistoryRxIfCountsPackets": cwsPmExtendedHistoryRxIfCountsPackets,
       "cwsPmExtendedHistoryRxIfCountsCrcErroredPackets": cwsPmExtendedHistoryRxIfCountsCrcErroredPackets,
       "cwsPmExtendedHistoryRxIfCountsMulticastPackets": cwsPmExtendedHistoryRxIfCountsMulticastPackets,
       "cwsPmExtendedHistoryRxIfCountsBroadcastPackets": cwsPmExtendedHistoryRxIfCountsBroadcastPackets,
       "cwsPmExtendedHistoryRxIfCountsPausePackets": cwsPmExtendedHistoryRxIfCountsPausePackets,
       "cwsPmExtendedHistoryRxIfCountsUndersizedPackets": cwsPmExtendedHistoryRxIfCountsUndersizedPackets,
       "cwsPmExtendedHistoryRxIfCountsOversizedPackets": cwsPmExtendedHistoryRxIfCountsOversizedPackets,
       "cwsPmExtendedHistoryRxIfCountsFragmentPackets": cwsPmExtendedHistoryRxIfCountsFragmentPackets,
       "cwsPmExtendedHistoryRxIfCountsJabberPackets": cwsPmExtendedHistoryRxIfCountsJabberPackets,
       "cwsPmExtendedHistoryRxIfCountsLengthOutRangePackets": cwsPmExtendedHistoryRxIfCountsLengthOutRangePackets,
       "cwsPmExtendedHistoryRxIfCountsPackets64Octet": cwsPmExtendedHistoryRxIfCountsPackets64Octet,
       "cwsPmExtendedHistoryRxIfCountsPackets65127Octet": cwsPmExtendedHistoryRxIfCountsPackets65127Octet,
       "cwsPmExtendedHistoryRxIfCountsPackets128255Octet": cwsPmExtendedHistoryRxIfCountsPackets128255Octet,
       "cwsPmExtendedHistoryRxIfCountsPackets256511Octet": cwsPmExtendedHistoryRxIfCountsPackets256511Octet,
       "cwsPmExtendedHistoryRxIfCountsPackets5121023Octet": cwsPmExtendedHistoryRxIfCountsPackets5121023Octet,
       "cwsPmExtendedHistoryRxIfCountsPackets10241518Octet": cwsPmExtendedHistoryRxIfCountsPackets10241518Octet,
       "cwsPmExtendedHistoryRxIfCountsAverageLinkUtilization": cwsPmExtendedHistoryRxIfCountsAverageLinkUtilization,
       "cwsPmExtendedHistoryTxIfCountsTable": cwsPmExtendedHistoryTxIfCountsTable,
       "cwsPmExtendedHistoryTxIfCountsEntry": cwsPmExtendedHistoryTxIfCountsEntry,
       "cwsPmExtendedHistoryTxIfCountsTableSnmpKey": cwsPmExtendedHistoryTxIfCountsTableSnmpKey,
       "cwsPmExtendedHistoryTxIfCountsBytes": cwsPmExtendedHistoryTxIfCountsBytes,
       "cwsPmExtendedHistoryTxIfCountsPackets": cwsPmExtendedHistoryTxIfCountsPackets,
       "cwsPmExtendedHistoryTxIfCountsCrcErroredPackets": cwsPmExtendedHistoryTxIfCountsCrcErroredPackets,
       "cwsPmExtendedHistoryTxIfCountsMulticastPackets": cwsPmExtendedHistoryTxIfCountsMulticastPackets,
       "cwsPmExtendedHistoryTxIfCountsBroadcastPackets": cwsPmExtendedHistoryTxIfCountsBroadcastPackets,
       "cwsPmExtendedHistoryTxIfCountsPausePackets": cwsPmExtendedHistoryTxIfCountsPausePackets,
       "cwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets": cwsPmExtendedHistoryTxIfCountsExcessiveDeferredPackets,
       "cwsPmExtendedHistoryTxIfCountsGiantPackets": cwsPmExtendedHistoryTxIfCountsGiantPackets,
       "cwsPmExtendedHistoryTxIfCountsUnderrunPackets": cwsPmExtendedHistoryTxIfCountsUnderrunPackets,
       "cwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets": cwsPmExtendedHistoryTxIfCountsLengthCheckErrorPackets,
       "cwsPmExtendedHistoryTxIfCountsLengthOutRangePackets": cwsPmExtendedHistoryTxIfCountsLengthOutRangePackets,
       "cwsPmExtendedHistoryTxIfCountsAverageLinkUtilization": cwsPmExtendedHistoryTxIfCountsAverageLinkUtilization,
       "cwsPmCurrentBinTxQueueTable": cwsPmCurrentBinTxQueueTable,
       "cwsPmCurrentBinTxQueueEntry": cwsPmCurrentBinTxQueueEntry,
       "cwsPmCurrentBinTxQueueTableSnmpKey": cwsPmCurrentBinTxQueueTableSnmpKey,
       "cwsPmCurrentBinTxQueuePacketDropCountSummary": cwsPmCurrentBinTxQueuePacketDropCountSummary,
       "cwsPmCurrentBinTxQueueQ0PacketDropCount": cwsPmCurrentBinTxQueueQ0PacketDropCount,
       "cwsPmCurrentBinTxQueueQ1PacketDropCount": cwsPmCurrentBinTxQueueQ1PacketDropCount,
       "cwsPmCurrentBinTxQueueQ2PacketDropCount": cwsPmCurrentBinTxQueueQ2PacketDropCount,
       "cwsPmCurrentBinTxQueueQ3PacketDropCount": cwsPmCurrentBinTxQueueQ3PacketDropCount,
       "cwsPmCurrentBinTxQueueQ4PacketDropCount": cwsPmCurrentBinTxQueueQ4PacketDropCount,
       "cwsPmCurrentBinTxQueueQ5PacketDropCount": cwsPmCurrentBinTxQueueQ5PacketDropCount,
       "cwsPmCurrentBinTxQueueQ6PacketDropCount": cwsPmCurrentBinTxQueueQ6PacketDropCount,
       "cwsPmCurrentBinTxQueueQ7PacketDropCount": cwsPmCurrentBinTxQueueQ7PacketDropCount,
       "cwsPmExtendedHistoryMacLayerTable": cwsPmExtendedHistoryMacLayerTable,
       "cwsPmExtendedHistoryMacLayerEntry": cwsPmExtendedHistoryMacLayerEntry,
       "cwsPmExtendedHistoryMacLayerTableSnmpKey": cwsPmExtendedHistoryMacLayerTableSnmpKey,
       "cwsPmExtendedHistoryMacLayerUnavailableSeconds": cwsPmExtendedHistoryMacLayerUnavailableSeconds,
       "cwsPmExtendedHistoryPcsLayerTable": cwsPmExtendedHistoryPcsLayerTable,
       "cwsPmExtendedHistoryPcsLayerEntry": cwsPmExtendedHistoryPcsLayerEntry,
       "cwsPmExtendedHistoryPcsLayerTableSnmpKey": cwsPmExtendedHistoryPcsLayerTableSnmpKey,
       "cwsPmExtendedHistoryPcsLayerErroredSeconds": cwsPmExtendedHistoryPcsLayerErroredSeconds,
       "cwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds": cwsPmExtendedHistoryPcsLayerSeverelyErroredSeconds,
       "cwsPmExtendedHistoryPcsLayerUnavailableSeconds": cwsPmExtendedHistoryPcsLayerUnavailableSeconds,
       "cwsPmExtendedHistoryPcsSyncHeaderErrorsTable": cwsPmExtendedHistoryPcsSyncHeaderErrorsTable,
       "cwsPmExtendedHistoryPcsSyncHeaderErrorsEntry": cwsPmExtendedHistoryPcsSyncHeaderErrorsEntry,
       "cwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey": cwsPmExtendedHistoryPcsSyncHeaderErrorsTableSnmpKey,
       "cwsPmExtendedHistoryPcsSyncHeaderErrorsCount": cwsPmExtendedHistoryPcsSyncHeaderErrorsCount,
       "cwsPmExtendedHistoryPcsBlockErrorsTable": cwsPmExtendedHistoryPcsBlockErrorsTable,
       "cwsPmExtendedHistoryPcsBlockErrorsEntry": cwsPmExtendedHistoryPcsBlockErrorsEntry,
       "cwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey": cwsPmExtendedHistoryPcsBlockErrorsTableSnmpKey,
       "cwsPmExtendedHistoryPcsBlockErrorsCount": cwsPmExtendedHistoryPcsBlockErrorsCount,
       "cwsPmExtendedHistoryPcsMultilaneBipErrorsTable": cwsPmExtendedHistoryPcsMultilaneBipErrorsTable,
       "cwsPmExtendedHistoryPcsMultilaneBipErrorsEntry": cwsPmExtendedHistoryPcsMultilaneBipErrorsEntry,
       "cwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey": cwsPmExtendedHistoryPcsMultilaneBipErrorsTableSnmpKey,
       "cwsPmExtendedHistoryPcsMultilaneBipErrorsCount": cwsPmExtendedHistoryPcsMultilaneBipErrorsCount,
       "cwsPmExtendedHistoryFecLayerTable": cwsPmExtendedHistoryFecLayerTable,
       "cwsPmExtendedHistoryFecLayerEntry": cwsPmExtendedHistoryFecLayerEntry,
       "cwsPmExtendedHistoryFecLayerTableSnmpKey": cwsPmExtendedHistoryFecLayerTableSnmpKey,
       "cwsPmExtendedHistoryFecLayerCorrectedBlockCount": cwsPmExtendedHistoryFecLayerCorrectedBlockCount,
       "cwsPmExtendedHistoryFecLayerUncorrectedBlockCount": cwsPmExtendedHistoryFecLayerUncorrectedBlockCount,
       "cwsPmExtendedHistoryFecLayerSymbolErrorCount": cwsPmExtendedHistoryFecLayerSymbolErrorCount,
       "cwsPmExtendedHistory24hIdTable": cwsPmExtendedHistory24hIdTable,
       "cwsPmExtendedHistory24hIdEntry": cwsPmExtendedHistory24hIdEntry,
       "cwsPmExtendedHistory24hIdTableSnmpKey": cwsPmExtendedHistory24hIdTableSnmpKey,
       "cwsPmExtendedHistory24hIdBinNumber": cwsPmExtendedHistory24hIdBinNumber,
       "cwsPmExtendedHistory24hIdBinName": cwsPmExtendedHistory24hIdBinName,
       "cwsPmExtendedHistory24hStateTable": cwsPmExtendedHistory24hStateTable,
       "cwsPmExtendedHistory24hStateEntry": cwsPmExtendedHistory24hStateEntry,
       "cwsPmExtendedHistory24hStateTableSnmpKey": cwsPmExtendedHistory24hStateTableSnmpKey,
       "cwsPmExtendedHistory24hStateStartDateTime": cwsPmExtendedHistory24hStateStartDateTime,
       "cwsPmExtendedHistory24hStateEndDateTime": cwsPmExtendedHistory24hStateEndDateTime,
       "cwsPmExtendedHistory24hStateState": cwsPmExtendedHistory24hStateState,
       "cwsPmExtendedHistory24hStatisticsTable": cwsPmExtendedHistory24hStatisticsTable,
       "cwsPmExtendedHistory24hStatisticsEntry": cwsPmExtendedHistory24hStatisticsEntry,
       "cwsPmExtendedHistory24hStatisticsTableSnmpKey": cwsPmExtendedHistory24hStatisticsTableSnmpKey,
       "cwsPmExtendedHistory24hStatisticsFrameErrorRatio": cwsPmExtendedHistory24hStatisticsFrameErrorRatio,
       "cwsPmExtendedHistory24hRxIfCountsTable": cwsPmExtendedHistory24hRxIfCountsTable,
       "cwsPmExtendedHistory24hRxIfCountsEntry": cwsPmExtendedHistory24hRxIfCountsEntry,
       "cwsPmExtendedHistory24hRxIfCountsTableSnmpKey": cwsPmExtendedHistory24hRxIfCountsTableSnmpKey,
       "cwsPmExtendedHistory24hRxIfCountsBytes": cwsPmExtendedHistory24hRxIfCountsBytes,
       "cwsPmExtendedHistory24hRxIfCountsPackets": cwsPmExtendedHistory24hRxIfCountsPackets,
       "cwsPmExtendedHistory24hRxIfCountsCrcErroredPackets": cwsPmExtendedHistory24hRxIfCountsCrcErroredPackets,
       "cwsPmExtendedHistory24hRxIfCountsMulticastPackets": cwsPmExtendedHistory24hRxIfCountsMulticastPackets,
       "cwsPmExtendedHistory24hRxIfCountsBroadcastPackets": cwsPmExtendedHistory24hRxIfCountsBroadcastPackets,
       "cwsPmExtendedHistory24hRxIfCountsPausePackets": cwsPmExtendedHistory24hRxIfCountsPausePackets,
       "cwsPmExtendedHistory24hRxIfCountsUndersizedPackets": cwsPmExtendedHistory24hRxIfCountsUndersizedPackets,
       "cwsPmExtendedHistory24hRxIfCountsOversizedPackets": cwsPmExtendedHistory24hRxIfCountsOversizedPackets,
       "cwsPmExtendedHistory24hRxIfCountsFragmentPackets": cwsPmExtendedHistory24hRxIfCountsFragmentPackets,
       "cwsPmExtendedHistory24hRxIfCountsJabberPackets": cwsPmExtendedHistory24hRxIfCountsJabberPackets,
       "cwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets": cwsPmExtendedHistory24hRxIfCountsLengthOutRangePackets,
       "cwsPmExtendedHistory24hRxIfCountsPackets64Octet": cwsPmExtendedHistory24hRxIfCountsPackets64Octet,
       "cwsPmExtendedHistory24hRxIfCountsPackets65127Octet": cwsPmExtendedHistory24hRxIfCountsPackets65127Octet,
       "cwsPmExtendedHistory24hRxIfCountsPackets128255Octet": cwsPmExtendedHistory24hRxIfCountsPackets128255Octet,
       "cwsPmExtendedHistory24hRxIfCountsPackets256511Octet": cwsPmExtendedHistory24hRxIfCountsPackets256511Octet,
       "cwsPmExtendedHistory24hRxIfCountsPackets5121023Octet": cwsPmExtendedHistory24hRxIfCountsPackets5121023Octet,
       "cwsPmExtendedHistory24hRxIfCountsPackets10241518Octet": cwsPmExtendedHistory24hRxIfCountsPackets10241518Octet,
       "cwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization": cwsPmExtendedHistory24hRxIfCountsAverageLinkUtilization,
       "cwsPmExtendedHistory24hTxIfCountsTable": cwsPmExtendedHistory24hTxIfCountsTable,
       "cwsPmExtendedHistory24hTxIfCountsEntry": cwsPmExtendedHistory24hTxIfCountsEntry,
       "cwsPmExtendedHistory24hTxIfCountsTableSnmpKey": cwsPmExtendedHistory24hTxIfCountsTableSnmpKey,
       "cwsPmExtendedHistory24hTxIfCountsBytes": cwsPmExtendedHistory24hTxIfCountsBytes,
       "cwsPmExtendedHistory24hTxIfCountsPackets": cwsPmExtendedHistory24hTxIfCountsPackets,
       "cwsPmExtendedHistory24hTxIfCountsCrcErroredPackets": cwsPmExtendedHistory24hTxIfCountsCrcErroredPackets,
       "cwsPmExtendedHistory24hTxIfCountsMulticastPackets": cwsPmExtendedHistory24hTxIfCountsMulticastPackets,
       "cwsPmExtendedHistory24hTxIfCountsBroadcastPackets": cwsPmExtendedHistory24hTxIfCountsBroadcastPackets,
       "cwsPmExtendedHistory24hTxIfCountsPausePackets": cwsPmExtendedHistory24hTxIfCountsPausePackets,
       "cwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets": cwsPmExtendedHistory24hTxIfCountsExcessiveDeferredPackets,
       "cwsPmExtendedHistory24hTxIfCountsGiantPackets": cwsPmExtendedHistory24hTxIfCountsGiantPackets,
       "cwsPmExtendedHistory24hTxIfCountsUnderrunPackets": cwsPmExtendedHistory24hTxIfCountsUnderrunPackets,
       "cwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets": cwsPmExtendedHistory24hTxIfCountsLengthCheckErrorPackets,
       "cwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets": cwsPmExtendedHistory24hTxIfCountsLengthOutRangePackets,
       "cwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization": cwsPmExtendedHistory24hTxIfCountsAverageLinkUtilization,
       "cwsPmExtendedHistory24hTxQueueTable": cwsPmExtendedHistory24hTxQueueTable,
       "cwsPmExtendedHistory24hTxQueueEntry": cwsPmExtendedHistory24hTxQueueEntry,
       "cwsPmExtendedHistory24hTxQueueTableSnmpKey": cwsPmExtendedHistory24hTxQueueTableSnmpKey,
       "cwsPmExtendedHistory24hTxQueuePacketDropCountSummary": cwsPmExtendedHistory24hTxQueuePacketDropCountSummary,
       "cwsPmExtendedHistory24hTxQueueQ0PacketDropCount": cwsPmExtendedHistory24hTxQueueQ0PacketDropCount,
       "cwsPmExtendedHistory24hTxQueueQ1PacketDropCount": cwsPmExtendedHistory24hTxQueueQ1PacketDropCount,
       "cwsPmExtendedHistory24hTxQueueQ2PacketDropCount": cwsPmExtendedHistory24hTxQueueQ2PacketDropCount,
       "cwsPmExtendedHistory24hTxQueueQ3PacketDropCount": cwsPmExtendedHistory24hTxQueueQ3PacketDropCount,
       "cwsPmExtendedHistory24hTxQueueQ4PacketDropCount": cwsPmExtendedHistory24hTxQueueQ4PacketDropCount,
       "cwsPmExtendedHistory24hTxQueueQ5PacketDropCount": cwsPmExtendedHistory24hTxQueueQ5PacketDropCount,
       "cwsPmExtendedHistory24hTxQueueQ6PacketDropCount": cwsPmExtendedHistory24hTxQueueQ6PacketDropCount,
       "cwsPmExtendedHistory24hTxQueueQ7PacketDropCount": cwsPmExtendedHistory24hTxQueueQ7PacketDropCount,
       "cwsPmExtendedHistory24hMacLayerTable": cwsPmExtendedHistory24hMacLayerTable,
       "cwsPmExtendedHistory24hMacLayerEntry": cwsPmExtendedHistory24hMacLayerEntry,
       "cwsPmExtendedHistory24hMacLayerTableSnmpKey": cwsPmExtendedHistory24hMacLayerTableSnmpKey,
       "cwsPmExtendedHistory24hMacLayerUnavailableSeconds": cwsPmExtendedHistory24hMacLayerUnavailableSeconds,
       "cwsPmExtendedHistory24hPcsLayerTable": cwsPmExtendedHistory24hPcsLayerTable,
       "cwsPmExtendedHistory24hPcsLayerEntry": cwsPmExtendedHistory24hPcsLayerEntry,
       "cwsPmExtendedHistory24hPcsLayerTableSnmpKey": cwsPmExtendedHistory24hPcsLayerTableSnmpKey,
       "cwsPmExtendedHistory24hPcsLayerErroredSeconds": cwsPmExtendedHistory24hPcsLayerErroredSeconds,
       "cwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds": cwsPmExtendedHistory24hPcsLayerSeverelyErroredSeconds,
       "cwsPmExtendedHistory24hPcsLayerUnavailableSeconds": cwsPmExtendedHistory24hPcsLayerUnavailableSeconds,
       "cwsPmExtendedHistory24hPcsSyncHeaderErrorsTable": cwsPmExtendedHistory24hPcsSyncHeaderErrorsTable,
       "cwsPmExtendedHistory24hPcsSyncHeaderErrorsEntry": cwsPmExtendedHistory24hPcsSyncHeaderErrorsEntry,
       "cwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey": cwsPmExtendedHistory24hPcsSyncHeaderErrorsTableSnmpKey,
       "cwsPmExtendedHistory24hPcsSyncHeaderErrorsCount": cwsPmExtendedHistory24hPcsSyncHeaderErrorsCount,
       "cwsPmExtendedHistory24hPcsBlockErrorsTable": cwsPmExtendedHistory24hPcsBlockErrorsTable,
       "cwsPmExtendedHistory24hPcsBlockErrorsEntry": cwsPmExtendedHistory24hPcsBlockErrorsEntry,
       "cwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey": cwsPmExtendedHistory24hPcsBlockErrorsTableSnmpKey,
       "cwsPmExtendedHistory24hPcsBlockErrorsCount": cwsPmExtendedHistory24hPcsBlockErrorsCount,
       "cwsPmExtendedHistory24hPcsMultilaneBipErrorsTable": cwsPmExtendedHistory24hPcsMultilaneBipErrorsTable,
       "cwsPmExtendedHistory24hPcsMultilaneBipErrorsEntry": cwsPmExtendedHistory24hPcsMultilaneBipErrorsEntry,
       "cwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey": cwsPmExtendedHistory24hPcsMultilaneBipErrorsTableSnmpKey,
       "cwsPmExtendedHistory24hPcsMultilaneBipErrorsCount": cwsPmExtendedHistory24hPcsMultilaneBipErrorsCount,
       "cwsPmExtendedHistory24hFecLayerTable": cwsPmExtendedHistory24hFecLayerTable,
       "cwsPmExtendedHistory24hFecLayerEntry": cwsPmExtendedHistory24hFecLayerEntry,
       "cwsPmExtendedHistory24hFecLayerTableSnmpKey": cwsPmExtendedHistory24hFecLayerTableSnmpKey,
       "cwsPmExtendedHistory24hFecLayerCorrectedBlockCount": cwsPmExtendedHistory24hFecLayerCorrectedBlockCount,
       "cwsPmExtendedHistory24hFecLayerUncorrectedBlockCount": cwsPmExtendedHistory24hFecLayerUncorrectedBlockCount,
       "cwsPmExtendedHistory24hFecLayerSymbolErrorCount": cwsPmExtendedHistory24hFecLayerSymbolErrorCount,
       "cwsPmPtpBasicInstancesTable": cwsPmPtpBasicInstancesTable,
       "cwsPmPtpBasicInstancesEntry": cwsPmPtpBasicInstancesEntry,
       "cwsPmPtpBasicInstancesInstanceName": cwsPmPtpBasicInstancesInstanceName,
       "cwsPmBasicIdTable": cwsPmBasicIdTable,
       "cwsPmBasicIdEntry": cwsPmBasicIdEntry,
       "cwsPmBasicIdTableSnmpKey": cwsPmBasicIdTableSnmpKey,
       "cwsPmBasicIdInstanceId": cwsPmBasicIdInstanceId,
       "cwsPmBasicIdInstanceType": cwsPmBasicIdInstanceType,
       "cwsPmBasicIdProfileType": cwsPmBasicIdProfileType,
       "cwsPmBasicStateTable": cwsPmBasicStateTable,
       "cwsPmBasicStateEntry": cwsPmBasicStateEntry,
       "cwsPmBasicStateTableSnmpKey": cwsPmBasicStateTableSnmpKey,
       "cwsPmBasicStateAdminState": cwsPmBasicStateAdminState,
       "cwsPmBasicStateOperationalState": cwsPmBasicStateOperationalState,
       "cwsPmBasicStateCurrentBinId": cwsPmBasicStateCurrentBinId,
       "cwsPmBasicStateCollectionStartDateTime": cwsPmBasicStateCollectionStartDateTime,
       "cwsPmBasicStateCollectionEndDateTime": cwsPmBasicStateCollectionEndDateTime,
       "cwsPmBasicPropertiesTable": cwsPmBasicPropertiesTable,
       "cwsPmBasicPropertiesEntry": cwsPmBasicPropertiesEntry,
       "cwsPmBasicPropertiesTableSnmpKey": cwsPmBasicPropertiesTableSnmpKey,
       "cwsPmBasicPropertiesConfigurationMode": cwsPmBasicPropertiesConfigurationMode,
       "cwsPmBasicPropertiesAlignment": cwsPmBasicPropertiesAlignment,
       "cwsPmBasicPropertiesConfiguredBinCount": cwsPmBasicPropertiesConfiguredBinCount,
       "cwsPmBasicPropertiesConfiguredBinDuration": cwsPmBasicPropertiesConfiguredBinDuration,
       "cwsPmBasicAttachedInterfaceTable": cwsPmBasicAttachedInterfaceTable,
       "cwsPmBasicAttachedInterfaceEntry": cwsPmBasicAttachedInterfaceEntry,
       "cwsPmBasicAttachedInterfaceTableSnmpKey": cwsPmBasicAttachedInterfaceTableSnmpKey,
       "cwsPmBasicAttachedInterfaceType": cwsPmBasicAttachedInterfaceType,
       "cwsPmBasicAttachedInterfaceName": cwsPmBasicAttachedInterfaceName,
       "cwsPmBasicAttachedInterfaceOperationalState": cwsPmBasicAttachedInterfaceOperationalState,
       "cwsPmBasicCurrentIdTable": cwsPmBasicCurrentIdTable,
       "cwsPmBasicCurrentIdEntry": cwsPmBasicCurrentIdEntry,
       "cwsPmBasicCurrentIdTableSnmpKey": cwsPmBasicCurrentIdTableSnmpKey,
       "cwsPmBasicCurrentIdBinNumber": cwsPmBasicCurrentIdBinNumber,
       "cwsPmBasicCurrentIdBinName": cwsPmBasicCurrentIdBinName,
       "cwsPmBasicCurrentStateTable": cwsPmBasicCurrentStateTable,
       "cwsPmBasicCurrentStateEntry": cwsPmBasicCurrentStateEntry,
       "cwsPmBasicCurrentStateTableSnmpKey": cwsPmBasicCurrentStateTableSnmpKey,
       "cwsPmBasicCurrentStateStartDateTime": cwsPmBasicCurrentStateStartDateTime,
       "cwsPmBasicCurrentStateClearedDateTime": cwsPmBasicCurrentStateClearedDateTime,
       "cwsPmBasicCurrentStateState": cwsPmBasicCurrentStateState,
       "cwsPmBasicCurrentStatisticsTable": cwsPmBasicCurrentStatisticsTable,
       "cwsPmBasicCurrentStatisticsEntry": cwsPmBasicCurrentStatisticsEntry,
       "cwsPmBasicCurrentStatisticsTableSnmpKey": cwsPmBasicCurrentStatisticsTableSnmpKey,
       "cwsPmBasicCurrentStatisticsNumberOfChannels": cwsPmBasicCurrentStatisticsNumberOfChannels,
       "cwsPmBasicCurrentOpticalPowerTable": cwsPmBasicCurrentOpticalPowerTable,
       "cwsPmBasicCurrentOpticalPowerEntry": cwsPmBasicCurrentOpticalPowerEntry,
       "cwsPmBasicCurrentOpticalPowerChannelNumber": cwsPmBasicCurrentOpticalPowerChannelNumber,
       "cwsPmBasicCurrentOpticalRxPowerTable": cwsPmBasicCurrentOpticalRxPowerTable,
       "cwsPmBasicCurrentOpticalRxPowerEntry": cwsPmBasicCurrentOpticalRxPowerEntry,
       "cwsPmBasicCurrentOpticalRxPowerTableSnmpKey": cwsPmBasicCurrentOpticalRxPowerTableSnmpKey,
       "cwsPmBasicCurrentOpticalRxPowerActual": cwsPmBasicCurrentOpticalRxPowerActual,
       "cwsPmBasicCurrentOpticalRxPowerMinimum": cwsPmBasicCurrentOpticalRxPowerMinimum,
       "cwsPmBasicCurrentOpticalRxPowerMaximum": cwsPmBasicCurrentOpticalRxPowerMaximum,
       "cwsPmBasicCurrentOpticalRxPowerAverage": cwsPmBasicCurrentOpticalRxPowerAverage,
       "cwsPmBasicCurrentOpticalTxPowerTable": cwsPmBasicCurrentOpticalTxPowerTable,
       "cwsPmBasicCurrentOpticalTxPowerEntry": cwsPmBasicCurrentOpticalTxPowerEntry,
       "cwsPmBasicCurrentOpticalTxPowerTableSnmpKey": cwsPmBasicCurrentOpticalTxPowerTableSnmpKey,
       "cwsPmBasicCurrentOpticalTxPowerActual": cwsPmBasicCurrentOpticalTxPowerActual,
       "cwsPmBasicCurrentOpticalTxPowerMinimum": cwsPmBasicCurrentOpticalTxPowerMinimum,
       "cwsPmBasicCurrentOpticalTxPowerMaximum": cwsPmBasicCurrentOpticalTxPowerMaximum,
       "cwsPmBasicCurrentOpticalTxPowerAverage": cwsPmBasicCurrentOpticalTxPowerAverage,
       "cwsPmBasicCurrentChannelRxPowerTable": cwsPmBasicCurrentChannelRxPowerTable,
       "cwsPmBasicCurrentChannelRxPowerEntry": cwsPmBasicCurrentChannelRxPowerEntry,
       "cwsPmBasicCurrentChannelRxPowerTableSnmpKey": cwsPmBasicCurrentChannelRxPowerTableSnmpKey,
       "cwsPmBasicCurrentChannelRxPowerActual": cwsPmBasicCurrentChannelRxPowerActual,
       "cwsPmBasicCurrentChannelRxPowerMinimum": cwsPmBasicCurrentChannelRxPowerMinimum,
       "cwsPmBasicCurrentChannelRxPowerMaximum": cwsPmBasicCurrentChannelRxPowerMaximum,
       "cwsPmBasicCurrentChannelRxPowerAverage": cwsPmBasicCurrentChannelRxPowerAverage,
       "cwsPmBasicCurrent24hIdTable": cwsPmBasicCurrent24hIdTable,
       "cwsPmBasicCurrent24hIdEntry": cwsPmBasicCurrent24hIdEntry,
       "cwsPmBasicCurrent24hIdTableSnmpKey": cwsPmBasicCurrent24hIdTableSnmpKey,
       "cwsPmBasicCurrent24hIdBinNumber": cwsPmBasicCurrent24hIdBinNumber,
       "cwsPmBasicCurrent24hIdBinName": cwsPmBasicCurrent24hIdBinName,
       "cwsPmBasicCurrent24hStateTable": cwsPmBasicCurrent24hStateTable,
       "cwsPmBasicCurrent24hStateEntry": cwsPmBasicCurrent24hStateEntry,
       "cwsPmBasicCurrent24hStateTableSnmpKey": cwsPmBasicCurrent24hStateTableSnmpKey,
       "cwsPmBasicCurrent24hStateStartDateTime": cwsPmBasicCurrent24hStateStartDateTime,
       "cwsPmBasicCurrent24hStateClearedDateTime": cwsPmBasicCurrent24hStateClearedDateTime,
       "cwsPmBasicCurrent24hStateState": cwsPmBasicCurrent24hStateState,
       "cwsPmBasicCurrent24hBinStatisticsTable": cwsPmBasicCurrent24hBinStatisticsTable,
       "cwsPmBasicCurrent24hBinStatisticsEntry": cwsPmBasicCurrent24hBinStatisticsEntry,
       "cwsPmBasicCurrent24hBinStatisticsTableSnmpKey": cwsPmBasicCurrent24hBinStatisticsTableSnmpKey,
       "cwsPmBasicCurrent24hBinStatisticsNumberOfChannels": cwsPmBasicCurrent24hBinStatisticsNumberOfChannels,
       "cwsPmBasicCurrent24hOpticalPowerTable": cwsPmBasicCurrent24hOpticalPowerTable,
       "cwsPmBasicCurrent24hOpticalPowerEntry": cwsPmBasicCurrent24hOpticalPowerEntry,
       "cwsPmBasicCurrent24hOpticalPowerChannelNumber": cwsPmBasicCurrent24hOpticalPowerChannelNumber,
       "cwsPmBasicCurrent24hRxOpticalPowerTable": cwsPmBasicCurrent24hRxOpticalPowerTable,
       "cwsPmBasicCurrent24hRxOpticalPowerEntry": cwsPmBasicCurrent24hRxOpticalPowerEntry,
       "cwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey": cwsPmBasicCurrent24hRxOpticalPowerTableSnmpKey,
       "cwsPmBasicCurrent24hRxOpticalPowerActual": cwsPmBasicCurrent24hRxOpticalPowerActual,
       "cwsPmBasicCurrent24hRxOpticalPowerMinimum": cwsPmBasicCurrent24hRxOpticalPowerMinimum,
       "cwsPmBasicCurrent24hRxOpticalPowerMaximum": cwsPmBasicCurrent24hRxOpticalPowerMaximum,
       "cwsPmBasicCurrent24hRxOpticalPowerAverage": cwsPmBasicCurrent24hRxOpticalPowerAverage,
       "cwsPmBasicCurrent24hTxOpticalPowerTable": cwsPmBasicCurrent24hTxOpticalPowerTable,
       "cwsPmBasicCurrent24hTxOpticalPowerEntry": cwsPmBasicCurrent24hTxOpticalPowerEntry,
       "cwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey": cwsPmBasicCurrent24hTxOpticalPowerTableSnmpKey,
       "cwsPmBasicCurrent24hTxOpticalPowerActual": cwsPmBasicCurrent24hTxOpticalPowerActual,
       "cwsPmBasicCurrent24hTxOpticalPowerMinimum": cwsPmBasicCurrent24hTxOpticalPowerMinimum,
       "cwsPmBasicCurrent24hTxOpticalPowerMaximum": cwsPmBasicCurrent24hTxOpticalPowerMaximum,
       "cwsPmBasicCurrent24hTxOpticalPowerAverage": cwsPmBasicCurrent24hTxOpticalPowerAverage,
       "cwsPmBasicCurrent24hRxChannelPowerTable": cwsPmBasicCurrent24hRxChannelPowerTable,
       "cwsPmBasicCurrent24hRxChannelPowerEntry": cwsPmBasicCurrent24hRxChannelPowerEntry,
       "cwsPmBasicCurrent24hRxChannelPowerTableSnmpKey": cwsPmBasicCurrent24hRxChannelPowerTableSnmpKey,
       "cwsPmBasicCurrent24hRxChannelPowerActual": cwsPmBasicCurrent24hRxChannelPowerActual,
       "cwsPmBasicCurrent24hRxChannelPowerMinimum": cwsPmBasicCurrent24hRxChannelPowerMinimum,
       "cwsPmBasicCurrent24hRxChannelPowerMaximum": cwsPmBasicCurrent24hRxChannelPowerMaximum,
       "cwsPmBasicCurrent24hRxChannelPowerAverage": cwsPmBasicCurrent24hRxChannelPowerAverage,
       "cwsPmBasicHistoryBinsTable": cwsPmBasicHistoryBinsTable,
       "cwsPmBasicHistoryBinsEntry": cwsPmBasicHistoryBinsEntry,
       "cwsPmBasicHistoryBinsBinNumber": cwsPmBasicHistoryBinsBinNumber,
       "cwsPmBasicHistoryStateTable": cwsPmBasicHistoryStateTable,
       "cwsPmBasicHistoryStateEntry": cwsPmBasicHistoryStateEntry,
       "cwsPmBasicHistoryStateTableSnmpKey": cwsPmBasicHistoryStateTableSnmpKey,
       "cwsPmBasicHistoryStateStartDateTime": cwsPmBasicHistoryStateStartDateTime,
       "cwsPmBasicHistoryStateEndDateTime": cwsPmBasicHistoryStateEndDateTime,
       "cwsPmBasicHistoryStateState": cwsPmBasicHistoryStateState,
       "cwsPmBasicHistoryStatisticsTable": cwsPmBasicHistoryStatisticsTable,
       "cwsPmBasicHistoryStatisticsEntry": cwsPmBasicHistoryStatisticsEntry,
       "cwsPmBasicHistoryStatisticsTableSnmpKey": cwsPmBasicHistoryStatisticsTableSnmpKey,
       "cwsPmBasicHistoryStatisticsNumberOfChannels": cwsPmBasicHistoryStatisticsNumberOfChannels,
       "cwsPmBasicHistoryOpticalPowerTable": cwsPmBasicHistoryOpticalPowerTable,
       "cwsPmBasicHistoryOpticalPowerEntry": cwsPmBasicHistoryOpticalPowerEntry,
       "cwsPmBasicHistoryOpticalPowerChannelNumber": cwsPmBasicHistoryOpticalPowerChannelNumber,
       "cwsPmBasicHistoryRxOpticalPowerTable": cwsPmBasicHistoryRxOpticalPowerTable,
       "cwsPmBasicHistoryRxOpticalPowerEntry": cwsPmBasicHistoryRxOpticalPowerEntry,
       "cwsPmBasicHistoryRxOpticalPowerTableSnmpKey": cwsPmBasicHistoryRxOpticalPowerTableSnmpKey,
       "cwsPmBasicHistoryRxOpticalPowerActual": cwsPmBasicHistoryRxOpticalPowerActual,
       "cwsPmBasicHistoryRxOpticalPowerMinimum": cwsPmBasicHistoryRxOpticalPowerMinimum,
       "cwsPmBasicHistoryRxOpticalPowerMaximum": cwsPmBasicHistoryRxOpticalPowerMaximum,
       "cwsPmBasicHistoryRxOpticalPowerAverage": cwsPmBasicHistoryRxOpticalPowerAverage,
       "cwsPmBasicHistoryTxOpticalPowerTable": cwsPmBasicHistoryTxOpticalPowerTable,
       "cwsPmBasicHistoryTxOpticalPowerEntry": cwsPmBasicHistoryTxOpticalPowerEntry,
       "cwsPmBasicHistoryTxOpticalPowerTableSnmpKey": cwsPmBasicHistoryTxOpticalPowerTableSnmpKey,
       "cwsPmBasicHistoryTxOpticalPowerActual": cwsPmBasicHistoryTxOpticalPowerActual,
       "cwsPmBasicHistoryTxOpticalPowerMinimum": cwsPmBasicHistoryTxOpticalPowerMinimum,
       "cwsPmBasicHistoryTxOpticalPowerMaximum": cwsPmBasicHistoryTxOpticalPowerMaximum,
       "cwsPmBasicHistoryTxOpticalPowerAverage": cwsPmBasicHistoryTxOpticalPowerAverage,
       "cwsPmBasicHistoryTxChannelPowerTable": cwsPmBasicHistoryTxChannelPowerTable,
       "cwsPmBasicHistoryTxChannelPowerEntry": cwsPmBasicHistoryTxChannelPowerEntry,
       "cwsPmBasicHistoryTxChannelPowerTableSnmpKey": cwsPmBasicHistoryTxChannelPowerTableSnmpKey,
       "cwsPmBasicHistoryTxChannelPowerActual": cwsPmBasicHistoryTxChannelPowerActual,
       "cwsPmBasicHistoryTxChannelPowerMinimum": cwsPmBasicHistoryTxChannelPowerMinimum,
       "cwsPmBasicHistoryTxChannelPowerMaximum": cwsPmBasicHistoryTxChannelPowerMaximum,
       "cwsPmBasicHistoryTxChannelPowerAverage": cwsPmBasicHistoryTxChannelPowerAverage,
       "cwsPmBasicHistory24hIdTable": cwsPmBasicHistory24hIdTable,
       "cwsPmBasicHistory24hIdEntry": cwsPmBasicHistory24hIdEntry,
       "cwsPmBasicHistory24hIdTableSnmpKey": cwsPmBasicHistory24hIdTableSnmpKey,
       "cwsPmBasicHistory24hIdBinNumber": cwsPmBasicHistory24hIdBinNumber,
       "cwsPmBasicHistory24hIdBinName": cwsPmBasicHistory24hIdBinName,
       "cwsPmBasicHistory24hStateTable": cwsPmBasicHistory24hStateTable,
       "cwsPmBasicHistory24hStateEntry": cwsPmBasicHistory24hStateEntry,
       "cwsPmBasicHistory24hStateTableSnmpKey": cwsPmBasicHistory24hStateTableSnmpKey,
       "cwsPmBasicHistory24hStateStartDateTime": cwsPmBasicHistory24hStateStartDateTime,
       "cwsPmBasicHistory24hStateEndDateTime": cwsPmBasicHistory24hStateEndDateTime,
       "cwsPmBasicHistory24hStateState": cwsPmBasicHistory24hStateState,
       "cwsPmBasicHistory24hStatisticsTable": cwsPmBasicHistory24hStatisticsTable,
       "cwsPmBasicHistory24hStatisticsEntry": cwsPmBasicHistory24hStatisticsEntry,
       "cwsPmBasicHistory24hStatisticsTableSnmpKey": cwsPmBasicHistory24hStatisticsTableSnmpKey,
       "cwsPmBasicHistory24hStatisticsNumberOfChannels": cwsPmBasicHistory24hStatisticsNumberOfChannels,
       "cwsPmBasicHistory24hOpticalPowerTable": cwsPmBasicHistory24hOpticalPowerTable,
       "cwsPmBasicHistory24hOpticalPowerEntry": cwsPmBasicHistory24hOpticalPowerEntry,
       "cwsPmBasicHistory24hOpticalPowerChannelNumber": cwsPmBasicHistory24hOpticalPowerChannelNumber,
       "cwsPmBasicHistory24hRxOpticalPowerTable": cwsPmBasicHistory24hRxOpticalPowerTable,
       "cwsPmBasicHistory24hRxOpticalPowerEntry": cwsPmBasicHistory24hRxOpticalPowerEntry,
       "cwsPmBasicHistory24hRxOpticalPowerTableSnmpKey": cwsPmBasicHistory24hRxOpticalPowerTableSnmpKey,
       "cwsPmBasicHistory24hRxOpticalPowerActual": cwsPmBasicHistory24hRxOpticalPowerActual,
       "cwsPmBasicHistory24hRxOpticalPowerMinimum": cwsPmBasicHistory24hRxOpticalPowerMinimum,
       "cwsPmBasicHistory24hRxOpticalPowerMaximum": cwsPmBasicHistory24hRxOpticalPowerMaximum,
       "cwsPmBasicHistory24hRxOpticalPowerAverage": cwsPmBasicHistory24hRxOpticalPowerAverage,
       "cwsPmBasicHistory24hTxOpticalPowerTable": cwsPmBasicHistory24hTxOpticalPowerTable,
       "cwsPmBasicHistory24hTxOpticalPowerEntry": cwsPmBasicHistory24hTxOpticalPowerEntry,
       "cwsPmBasicHistory24hTxOpticalPowerTableSnmpKey": cwsPmBasicHistory24hTxOpticalPowerTableSnmpKey,
       "cwsPmBasicHistory24hTxOpticalPowerActual": cwsPmBasicHistory24hTxOpticalPowerActual,
       "cwsPmBasicHistory24hTxOpticalPowerMinimum": cwsPmBasicHistory24hTxOpticalPowerMinimum,
       "cwsPmBasicHistory24hTxOpticalPowerMaximum": cwsPmBasicHistory24hTxOpticalPowerMaximum,
       "cwsPmBasicHistory24hTxOpticalPowerAverage": cwsPmBasicHistory24hTxOpticalPowerAverage,
       "cwsPmBasicHistory24hRxChannelPowerTable": cwsPmBasicHistory24hRxChannelPowerTable,
       "cwsPmBasicHistory24hRxChannelPowerEntry": cwsPmBasicHistory24hRxChannelPowerEntry,
       "cwsPmBasicHistory24hRxChannelPowerTableSnmpKey": cwsPmBasicHistory24hRxChannelPowerTableSnmpKey,
       "cwsPmBasicHistory24hRxChannelPowerActual": cwsPmBasicHistory24hRxChannelPowerActual,
       "cwsPmBasicHistory24hRxChannelPowerMinimum": cwsPmBasicHistory24hRxChannelPowerMinimum,
       "cwsPmBasicHistory24hRxChannelPowerMaximum": cwsPmBasicHistory24hRxChannelPowerMaximum,
       "cwsPmBasicHistory24hRxChannelPowerAverage": cwsPmBasicHistory24hRxChannelPowerAverage,
       "cwsPmPtpAdvancedInstancesTable": cwsPmPtpAdvancedInstancesTable,
       "cwsPmPtpAdvancedInstancesEntry": cwsPmPtpAdvancedInstancesEntry,
       "cwsPmPtpAdvancedInstancesInstanceName": cwsPmPtpAdvancedInstancesInstanceName,
       "cwsPmAdvancedIdTable": cwsPmAdvancedIdTable,
       "cwsPmAdvancedIdEntry": cwsPmAdvancedIdEntry,
       "cwsPmAdvancedIdTableSnmpKey": cwsPmAdvancedIdTableSnmpKey,
       "cwsPmAdvancedIdInstanceId": cwsPmAdvancedIdInstanceId,
       "cwsPmAdvancedIdInstanceType": cwsPmAdvancedIdInstanceType,
       "cwsPmAdvancedIdProfileType": cwsPmAdvancedIdProfileType,
       "cwsPmAdvancedStateTable": cwsPmAdvancedStateTable,
       "cwsPmAdvancedStateEntry": cwsPmAdvancedStateEntry,
       "cwsPmAdvancedStateTableSnmpKey": cwsPmAdvancedStateTableSnmpKey,
       "cwsPmAdvancedStateAdminState": cwsPmAdvancedStateAdminState,
       "cwsPmAdvancedStateOperationalState": cwsPmAdvancedStateOperationalState,
       "cwsPmAdvancedStateCurrentBinId": cwsPmAdvancedStateCurrentBinId,
       "cwsPmAdvancedStateCollectionStartDateTime": cwsPmAdvancedStateCollectionStartDateTime,
       "cwsPmAdvancedStateCollectionEndDateTime": cwsPmAdvancedStateCollectionEndDateTime,
       "cwsPmAdvancedPropertiesTable": cwsPmAdvancedPropertiesTable,
       "cwsPmAdvancedPropertiesEntry": cwsPmAdvancedPropertiesEntry,
       "cwsPmAdvancedPropertiesTableSnmpKey": cwsPmAdvancedPropertiesTableSnmpKey,
       "cwsPmAdvancedPropertiesConfigurationMode": cwsPmAdvancedPropertiesConfigurationMode,
       "cwsPmAdvancedPropertiesAlignment": cwsPmAdvancedPropertiesAlignment,
       "cwsPmAdvancedPropertiesConfiguredBinCount": cwsPmAdvancedPropertiesConfiguredBinCount,
       "cwsPmAdvancedPropertiesConfiguredBinDuration": cwsPmAdvancedPropertiesConfiguredBinDuration,
       "cwsPmAdvancedAttachedInterfaceTable": cwsPmAdvancedAttachedInterfaceTable,
       "cwsPmAdvancedAttachedInterfaceEntry": cwsPmAdvancedAttachedInterfaceEntry,
       "cwsPmAdvancedAttachedInterfaceTableSnmpKey": cwsPmAdvancedAttachedInterfaceTableSnmpKey,
       "cwsPmAdvancedAttachedInterfaceType": cwsPmAdvancedAttachedInterfaceType,
       "cwsPmAdvancedAttachedInterfaceName": cwsPmAdvancedAttachedInterfaceName,
       "cwsPmAdvancedAttachedInterfaceOperationalState": cwsPmAdvancedAttachedInterfaceOperationalState,
       "cwsPmAdvancedCurrentIdTable": cwsPmAdvancedCurrentIdTable,
       "cwsPmAdvancedCurrentIdEntry": cwsPmAdvancedCurrentIdEntry,
       "cwsPmAdvancedCurrentIdTableSnmpKey": cwsPmAdvancedCurrentIdTableSnmpKey,
       "cwsPmAdvancedCurrentIdBinNumber": cwsPmAdvancedCurrentIdBinNumber,
       "cwsPmAdvancedCurrentIdBinName": cwsPmAdvancedCurrentIdBinName,
       "cwsPmAdvancedCurrentStateTable": cwsPmAdvancedCurrentStateTable,
       "cwsPmAdvancedCurrentStateEntry": cwsPmAdvancedCurrentStateEntry,
       "cwsPmAdvancedCurrentStateTableSnmpKey": cwsPmAdvancedCurrentStateTableSnmpKey,
       "cwsPmAdvancedCurrentStateStartDateTime": cwsPmAdvancedCurrentStateStartDateTime,
       "cwsPmAdvancedCurrentStateClearedDateTime": cwsPmAdvancedCurrentStateClearedDateTime,
       "cwsPmAdvancedCurrentStateState": cwsPmAdvancedCurrentStateState,
       "cwsPmAdvancedCurrentStatisticsTable": cwsPmAdvancedCurrentStatisticsTable,
       "cwsPmAdvancedCurrentStatisticsEntry": cwsPmAdvancedCurrentStatisticsEntry,
       "cwsPmAdvancedCurrentStatisticsTableSnmpKey": cwsPmAdvancedCurrentStatisticsTableSnmpKey,
       "cwsPmAdvancedCurrentStatisticsPostFecBitErrorRate": cwsPmAdvancedCurrentStatisticsPostFecBitErrorRate,
       "cwsPmPreFecBitErrorRateTable": cwsPmPreFecBitErrorRateTable,
       "cwsPmPreFecBitErrorRateEntry": cwsPmPreFecBitErrorRateEntry,
       "cwsPmPreFecBitErrorRateTableSnmpKey": cwsPmPreFecBitErrorRateTableSnmpKey,
       "cwsPmPreFecBitErrorRateBitErrorRate": cwsPmPreFecBitErrorRateBitErrorRate,
       "cwsPmPreFecBitErrorRateMaximum": cwsPmPreFecBitErrorRateMaximum,
       "cwsPmAdvancedCurrentQFactorTable": cwsPmAdvancedCurrentQFactorTable,
       "cwsPmAdvancedCurrentQFactorEntry": cwsPmAdvancedCurrentQFactorEntry,
       "cwsPmAdvancedCurrentQFactorTableSnmpKey": cwsPmAdvancedCurrentQFactorTableSnmpKey,
       "cwsPmAdvancedCurrentQFactorQFactor": cwsPmAdvancedCurrentQFactorQFactor,
       "cwsPmAdvancedCurrentQFactorMinimum": cwsPmAdvancedCurrentQFactorMinimum,
       "cwsPmAdvancedCurrentQFactorMaximum": cwsPmAdvancedCurrentQFactorMaximum,
       "cwsPmAdvancedCurrentFecErrorTable": cwsPmAdvancedCurrentFecErrorTable,
       "cwsPmAdvancedCurrentFecErrorEntry": cwsPmAdvancedCurrentFecErrorEntry,
       "cwsPmAdvancedCurrentFecErrorTableSnmpKey": cwsPmAdvancedCurrentFecErrorTableSnmpKey,
       "cwsPmAdvancedCurrentFecErrorFrameErrorCount": cwsPmAdvancedCurrentFecErrorFrameErrorCount,
       "cwsPmAdvancedCurrentFecErrorFrameErrorCountSecond": cwsPmAdvancedCurrentFecErrorFrameErrorCountSecond,
       "cwsPmAdvancedCurrentFecErrorUncorrectedBlockCount": cwsPmAdvancedCurrentFecErrorUncorrectedBlockCount,
       "cwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds": cwsPmAdvancedCurrentFecErrorHighCorrectionCountSeconds,
       "cwsPmAdvancedCurrent24hIdTable": cwsPmAdvancedCurrent24hIdTable,
       "cwsPmAdvancedCurrent24hIdEntry": cwsPmAdvancedCurrent24hIdEntry,
       "cwsPmAdvancedCurrent24hIdTableSnmpKey": cwsPmAdvancedCurrent24hIdTableSnmpKey,
       "cwsPmAdvancedCurrent24hIdBinNumber": cwsPmAdvancedCurrent24hIdBinNumber,
       "cwsPmAdvancedCurrent24hIdBinName": cwsPmAdvancedCurrent24hIdBinName,
       "cwsPmAdvancedCurrent24hStateTable": cwsPmAdvancedCurrent24hStateTable,
       "cwsPmAdvancedCurrent24hStateEntry": cwsPmAdvancedCurrent24hStateEntry,
       "cwsPmAdvancedCurrent24hStateTableSnmpKey": cwsPmAdvancedCurrent24hStateTableSnmpKey,
       "cwsPmAdvancedCurrent24hStateStartDateTime": cwsPmAdvancedCurrent24hStateStartDateTime,
       "cwsPmAdvancedCurrent24hStateClearedDateTime": cwsPmAdvancedCurrent24hStateClearedDateTime,
       "cwsPmAdvancedCurrent24hStateState": cwsPmAdvancedCurrent24hStateState,
       "cwsPmAdvancedCurrent24hStatisticsTable": cwsPmAdvancedCurrent24hStatisticsTable,
       "cwsPmAdvancedCurrent24hStatisticsEntry": cwsPmAdvancedCurrent24hStatisticsEntry,
       "cwsPmAdvancedCurrent24hStatisticsTableSnmpKey": cwsPmAdvancedCurrent24hStatisticsTableSnmpKey,
       "cwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate": cwsPmAdvancedCurrent24hStatisticsPostFecBitErrorRate,
       "cwsPmAdvancedCurrent24hPreFecBerTable": cwsPmAdvancedCurrent24hPreFecBerTable,
       "cwsPmAdvancedCurrent24hPreFecBerEntry": cwsPmAdvancedCurrent24hPreFecBerEntry,
       "cwsPmAdvancedCurrent24hPreFecBerTableSnmpKey": cwsPmAdvancedCurrent24hPreFecBerTableSnmpKey,
       "cwsPmAdvancedCurrent24hPreFecBerBitErrorRate": cwsPmAdvancedCurrent24hPreFecBerBitErrorRate,
       "cwsPmAdvancedCurrent24hPreFecBerMaximum": cwsPmAdvancedCurrent24hPreFecBerMaximum,
       "cwsPmAdvancedCurrent24hQFactorTable": cwsPmAdvancedCurrent24hQFactorTable,
       "cwsPmAdvancedCurrent24hQFactorEntry": cwsPmAdvancedCurrent24hQFactorEntry,
       "cwsPmAdvancedCurrent24hQFactorTableSnmpKey": cwsPmAdvancedCurrent24hQFactorTableSnmpKey,
       "cwsPmAdvancedCurrent24hQFactorQFactor": cwsPmAdvancedCurrent24hQFactorQFactor,
       "cwsPmAdvancedCurrent24hQFactorMinimum": cwsPmAdvancedCurrent24hQFactorMinimum,
       "cwsPmAdvancedCurrent24hQFactorMaximum": cwsPmAdvancedCurrent24hQFactorMaximum,
       "cwsPmAdvancedCurrent24hFecErrorTable": cwsPmAdvancedCurrent24hFecErrorTable,
       "cwsPmAdvancedCurrent24hFecErrorEntry": cwsPmAdvancedCurrent24hFecErrorEntry,
       "cwsPmAdvancedCurrent24hFecErrorTableSnmpKey": cwsPmAdvancedCurrent24hFecErrorTableSnmpKey,
       "cwsPmAdvancedCurrent24hFecErrorFrameErrorCount": cwsPmAdvancedCurrent24hFecErrorFrameErrorCount,
       "cwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond": cwsPmAdvancedCurrent24hFecErrorFrameErrorCountSecond,
       "cwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount": cwsPmAdvancedCurrent24hFecErrorUncorrectedBlockCount,
       "cwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds": cwsPmAdvancedCurrent24hFecErrorHighCorrectionCountSeconds,
       "cwsPmAdvancedHistoryBinsTable": cwsPmAdvancedHistoryBinsTable,
       "cwsPmAdvancedHistoryBinsEntry": cwsPmAdvancedHistoryBinsEntry,
       "cwsPmAdvancedHistoryBinsBinNumber": cwsPmAdvancedHistoryBinsBinNumber,
       "cwsPmAdvancedHistoryStateTable": cwsPmAdvancedHistoryStateTable,
       "cwsPmAdvancedHistoryStateEntry": cwsPmAdvancedHistoryStateEntry,
       "cwsPmAdvancedHistoryStateTableSnmpKey": cwsPmAdvancedHistoryStateTableSnmpKey,
       "cwsPmAdvancedHistoryStateStartDateTime": cwsPmAdvancedHistoryStateStartDateTime,
       "cwsPmAdvancedHistoryStateEndDateTime": cwsPmAdvancedHistoryStateEndDateTime,
       "cwsPmAdvancedHistoryStateState": cwsPmAdvancedHistoryStateState,
       "cwsPmAdvancedHistoryStatisticsTable": cwsPmAdvancedHistoryStatisticsTable,
       "cwsPmAdvancedHistoryStatisticsEntry": cwsPmAdvancedHistoryStatisticsEntry,
       "cwsPmAdvancedHistoryStatisticsTableSnmpKey": cwsPmAdvancedHistoryStatisticsTableSnmpKey,
       "cwsPmAdvancedHistoryStatisticsPostFecBitErrorRate": cwsPmAdvancedHistoryStatisticsPostFecBitErrorRate,
       "cwsPmAdvancedHistoryPreFecBerTable": cwsPmAdvancedHistoryPreFecBerTable,
       "cwsPmAdvancedHistoryPreFecBerEntry": cwsPmAdvancedHistoryPreFecBerEntry,
       "cwsPmAdvancedHistoryPreFecBerTableSnmpKey": cwsPmAdvancedHistoryPreFecBerTableSnmpKey,
       "cwsPmAdvancedHistoryPreFecBerBitErrorRate": cwsPmAdvancedHistoryPreFecBerBitErrorRate,
       "cwsPmAdvancedHistoryPreFecBerMaximum": cwsPmAdvancedHistoryPreFecBerMaximum,
       "cwsPmAdvancedHistoryQFactorTable": cwsPmAdvancedHistoryQFactorTable,
       "cwsPmAdvancedHistoryQFactorEntry": cwsPmAdvancedHistoryQFactorEntry,
       "cwsPmAdvancedHistoryQFactorTableSnmpKey": cwsPmAdvancedHistoryQFactorTableSnmpKey,
       "cwsPmAdvancedHistoryQFactorQFactor": cwsPmAdvancedHistoryQFactorQFactor,
       "cwsPmAdvancedHistoryQFactorMinimum": cwsPmAdvancedHistoryQFactorMinimum,
       "cwsPmAdvancedHistoryQFactorMaximum": cwsPmAdvancedHistoryQFactorMaximum,
       "cwsPmAdvancedHistoryFecErrorTable": cwsPmAdvancedHistoryFecErrorTable,
       "cwsPmAdvancedHistoryFecErrorEntry": cwsPmAdvancedHistoryFecErrorEntry,
       "cwsPmAdvancedHistoryFecErrorTableSnmpKey": cwsPmAdvancedHistoryFecErrorTableSnmpKey,
       "cwsPmAdvancedHistoryFecErrorFrameErrorCount": cwsPmAdvancedHistoryFecErrorFrameErrorCount,
       "cwsPmAdvancedHistoryFecErrorFrameErrorCountSecond": cwsPmAdvancedHistoryFecErrorFrameErrorCountSecond,
       "cwsPmAdvancedHistoryFecErrorUncorrectedBlockCount": cwsPmAdvancedHistoryFecErrorUncorrectedBlockCount,
       "cwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds": cwsPmAdvancedHistoryFecErrorHighCorrectionCountSeconds,
       "cwsPmAdvancedHistory24hIdTable": cwsPmAdvancedHistory24hIdTable,
       "cwsPmAdvancedHistory24hIdEntry": cwsPmAdvancedHistory24hIdEntry,
       "cwsPmAdvancedHistory24hIdTableSnmpKey": cwsPmAdvancedHistory24hIdTableSnmpKey,
       "cwsPmAdvancedHistory24hIdBinNumber": cwsPmAdvancedHistory24hIdBinNumber,
       "cwsPmAdvancedHistory24hIdBinName": cwsPmAdvancedHistory24hIdBinName,
       "cwsPmAdvancedHistory24hStateTable": cwsPmAdvancedHistory24hStateTable,
       "cwsPmAdvancedHistory24hStateEntry": cwsPmAdvancedHistory24hStateEntry,
       "cwsPmAdvancedHistory24hStateTableSnmpKey": cwsPmAdvancedHistory24hStateTableSnmpKey,
       "cwsPmAdvancedHistory24hStateStartDateTime": cwsPmAdvancedHistory24hStateStartDateTime,
       "cwsPmAdvancedHistory24hStateEndDateTime": cwsPmAdvancedHistory24hStateEndDateTime,
       "cwsPmAdvancedHistory24hStateState": cwsPmAdvancedHistory24hStateState,
       "cwsPmAdvancedHistory24hStatisticsTable": cwsPmAdvancedHistory24hStatisticsTable,
       "cwsPmAdvancedHistory24hStatisticsEntry": cwsPmAdvancedHistory24hStatisticsEntry,
       "cwsPmAdvancedHistory24hStatisticsTableSnmpKey": cwsPmAdvancedHistory24hStatisticsTableSnmpKey,
       "cwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate": cwsPmAdvancedHistory24hStatisticsPostFecBitErrorRate,
       "cwsPmAdvancedHistory24hPreFecBerTable": cwsPmAdvancedHistory24hPreFecBerTable,
       "cwsPmAdvancedHistory24hPreFecBerEntry": cwsPmAdvancedHistory24hPreFecBerEntry,
       "cwsPmAdvancedHistory24hPreFecBerTableSnmpKey": cwsPmAdvancedHistory24hPreFecBerTableSnmpKey,
       "cwsPmAdvancedHistory24hPreFecBerBitErrorRate": cwsPmAdvancedHistory24hPreFecBerBitErrorRate,
       "cwsPmAdvancedHistory24hPreFecBerMaximum": cwsPmAdvancedHistory24hPreFecBerMaximum,
       "cwsPmAdvancedHistory24hQFactorTable": cwsPmAdvancedHistory24hQFactorTable,
       "cwsPmAdvancedHistory24hQFactorEntry": cwsPmAdvancedHistory24hQFactorEntry,
       "cwsPmAdvancedHistory24hQFactorTableSnmpKey": cwsPmAdvancedHistory24hQFactorTableSnmpKey,
       "cwsPmAdvancedHistory24hQFactorQFactor": cwsPmAdvancedHistory24hQFactorQFactor,
       "cwsPmAdvancedHistory24hQFactorMinimum": cwsPmAdvancedHistory24hQFactorMinimum,
       "cwsPmAdvancedHistory24hQFactorMaximum": cwsPmAdvancedHistory24hQFactorMaximum,
       "cwsPmAdvancedHistory24hFecErrorTable": cwsPmAdvancedHistory24hFecErrorTable,
       "cwsPmAdvancedHistory24hFecErrorEntry": cwsPmAdvancedHistory24hFecErrorEntry,
       "cwsPmAdvancedHistory24hFecErrorTableSnmpKey": cwsPmAdvancedHistory24hFecErrorTableSnmpKey,
       "cwsPmAdvancedHistory24hFecErrorFrameErrorCount": cwsPmAdvancedHistory24hFecErrorFrameErrorCount,
       "cwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond": cwsPmAdvancedHistory24hFecErrorFrameErrorCountSecond,
       "cwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount": cwsPmAdvancedHistory24hFecErrorUncorrectedBlockCount,
       "cwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds": cwsPmAdvancedHistory24hFecErrorHighCorrectionCountSeconds,
       "cwsPmExtendedCurrentOduLayerTable": cwsPmExtendedCurrentOduLayerTable,
       "cwsPmExtendedCurrentOduLayerEntry": cwsPmExtendedCurrentOduLayerEntry,
       "cwsPmExtendedCurrentOduLayerTableSnmpKey": cwsPmExtendedCurrentOduLayerTableSnmpKey,
       "cwsPmExtendedCurrentOduLayerErroredSeconds": cwsPmExtendedCurrentOduLayerErroredSeconds,
       "cwsPmExtendedCurrentOduLayerSeverelyErroredSeconds": cwsPmExtendedCurrentOduLayerSeverelyErroredSeconds,
       "cwsPmExtendedCurrentOduLayerUnavailableSeconds": cwsPmExtendedCurrentOduLayerUnavailableSeconds,
       "cwsPmExtendedCurrent24hOduLayerTable": cwsPmExtendedCurrent24hOduLayerTable,
       "cwsPmExtendedCurrent24hOduLayerEntry": cwsPmExtendedCurrent24hOduLayerEntry,
       "cwsPmExtendedCurrent24hOduLayerTableSnmpKey": cwsPmExtendedCurrent24hOduLayerTableSnmpKey,
       "cwsPmExtendedCurrent24hOduLayerErroredSeconds": cwsPmExtendedCurrent24hOduLayerErroredSeconds,
       "cwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds": cwsPmExtendedCurrent24hOduLayerSeverelyErroredSeconds,
       "cwsPmExtendedCurrent24hOduLayerUnavailableSeconds": cwsPmExtendedCurrent24hOduLayerUnavailableSeconds,
       "cwsPmExtendedHistoryOduLayerTable": cwsPmExtendedHistoryOduLayerTable,
       "cwsPmExtendedHistoryOduLayerEntry": cwsPmExtendedHistoryOduLayerEntry,
       "cwsPmExtendedHistoryOduLayerTableSnmpKey": cwsPmExtendedHistoryOduLayerTableSnmpKey,
       "cwsPmExtendedHistoryOduLayerErroredSeconds": cwsPmExtendedHistoryOduLayerErroredSeconds,
       "cwsPmExtendedHistoryOduLayerSeverelyErroredSeconds": cwsPmExtendedHistoryOduLayerSeverelyErroredSeconds,
       "cwsPmExtendedHistoryOduLayerUnavailableSeconds": cwsPmExtendedHistoryOduLayerUnavailableSeconds,
       "cwsPmExtendedHistory24hOduLayerTable": cwsPmExtendedHistory24hOduLayerTable,
       "cwsPmExtendedHistory24hOduLayerEntry": cwsPmExtendedHistory24hOduLayerEntry,
       "cwsPmExtendedHistory24hOduLayerTableSnmpKey": cwsPmExtendedHistory24hOduLayerTableSnmpKey,
       "cwsPmExtendedHistory24hOduLayerErroredSeconds": cwsPmExtendedHistory24hOduLayerErroredSeconds,
       "cwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds": cwsPmExtendedHistory24hOduLayerSeverelyErroredSeconds,
       "cwsPmExtendedHistory24hOduLayerUnavailableSeconds": cwsPmExtendedHistory24hOduLayerUnavailableSeconds}
)
