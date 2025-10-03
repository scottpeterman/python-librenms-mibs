# SNMP MIB module (ERICSSON-ROUTER-SYS-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-SYS-RESOURCES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:35 2025
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

(EriRouterAlarmId,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-ALARM-TC",
    "EriRouterAlarmId")

(eriRouterMgmt,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SMI",
    "eriRouterMgmt")

(EriRouterKBytes,
 EriRouterPercentage,
 EriRouterSlot) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-TC",
    "EriRouterKBytes",
    "EriRouterPercentage",
    "EriRouterSlot")

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

eriRouterSysResourcesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24)
)
if mibBuilder.loadTexts:
    eriRouterSysResourcesMib.setRevisions(
        ("2015-01-14 18:00",
         "2011-04-29 18:00",
         "2011-01-19 18:00",
         "2009-07-16 00:00",
         "2007-05-29 00:00",
         "2005-04-18 00:00",
         "2003-09-02 18:00",
         "2002-10-10 00:00",
         "2002-06-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EriRouterSRMIBNotifications_ObjectIdentity = ObjectIdentity
eriRouterSRMIBNotifications = _EriRouterSRMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0)
)
_EriRouterSRMIBObjects_ObjectIdentity = ObjectIdentity
eriRouterSRMIBObjects = _EriRouterSRMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1)
)
_EriRouterSRProcess_ObjectIdentity = ObjectIdentity
eriRouterSRProcess = _EriRouterSRProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1)
)
_EriRouterSRProcessNotifyLastUpdate_Type = TimeTicks
_EriRouterSRProcessNotifyLastUpdate_Object = MibScalar
eriRouterSRProcessNotifyLastUpdate = _EriRouterSRProcessNotifyLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 1),
    _EriRouterSRProcessNotifyLastUpdate_Type()
)
eriRouterSRProcessNotifyLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyLastUpdate.setStatus("current")


class _EriRouterSRProcessEventNotifyEnable_Type(Integer32):
    """Custom type eriRouterSRProcessEventNotifyEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EriRouterSRProcessEventNotifyEnable_Type.__name__ = "Integer32"
_EriRouterSRProcessEventNotifyEnable_Object = MibScalar
eriRouterSRProcessEventNotifyEnable = _EriRouterSRProcessEventNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 2),
    _EriRouterSRProcessEventNotifyEnable_Type()
)
eriRouterSRProcessEventNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eriRouterSRProcessEventNotifyEnable.setStatus("current")
_EriRouterSRProcessNotifyTable_Object = MibTable
eriRouterSRProcessNotifyTable = _EriRouterSRProcessNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyTable.setStatus("current")
_EriRouterSRProcessNotifyEntry_Object = MibTableRow
eriRouterSRProcessNotifyEntry = _EriRouterSRProcessNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3, 1)
)
eriRouterSRProcessNotifyEntry.setIndexNames(
    (0, "ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyProcName"),
)
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyEntry.setStatus("current")


class _EriRouterSRProcessNotifyProcName_Type(SnmpAdminString):
    """Custom type eriRouterSRProcessNotifyProcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EriRouterSRProcessNotifyProcName_Type.__name__ = "SnmpAdminString"
_EriRouterSRProcessNotifyProcName_Object = MibTableColumn
eriRouterSRProcessNotifyProcName = _EriRouterSRProcessNotifyProcName_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3, 1, 1),
    _EriRouterSRProcessNotifyProcName_Type()
)
eriRouterSRProcessNotifyProcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyProcName.setStatus("current")


class _EriRouterSRProcessNotifyPID_Type(Unsigned32):
    """Custom type eriRouterSRProcessNotifyPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EriRouterSRProcessNotifyPID_Type.__name__ = "Unsigned32"
_EriRouterSRProcessNotifyPID_Object = MibTableColumn
eriRouterSRProcessNotifyPID = _EriRouterSRProcessNotifyPID_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3, 1, 2),
    _EriRouterSRProcessNotifyPID_Type()
)
eriRouterSRProcessNotifyPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyPID.setStatus("current")


class _EriRouterSRProcessNotifyEventCause_Type(Integer32):
    """Custom type eriRouterSRProcessNotifyEventCause based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("firstStart", 1),
          ("hangup", 2),
          ("interrupt", 3),
          ("quit", 4),
          ("illegalInstruction", 5),
          ("traceTrap", 6),
          ("abort", 7),
          ("emt", 8),
          ("floatingPointException", 9),
          ("kill", 10),
          ("busError", 11),
          ("segmentFault", 12),
          ("systemCallError", 13),
          ("pipeError", 14),
          ("alarmClock", 15),
          ("softwareTermination", 16),
          ("urgentConditionOnIOChannel", 17),
          ("stopNotFromTty", 18),
          ("stopFromTty", 19),
          ("continueStopped", 20),
          ("childExit", 21),
          ("ttyInput", 22),
          ("ttyOutput", 23),
          ("inputOutput", 24),
          ("exceededCpuTime", 25),
          ("exceededFileSize", 26),
          ("virtualAlarm", 27),
          ("profilingAlarm", 28),
          ("windowResize", 29),
          ("infoRequest", 30),
          ("userDefined1", 31),
          ("userDefined2", 32),
          ("powerFailRestart", 33),
          ("unknown", 34))
    )


_EriRouterSRProcessNotifyEventCause_Type.__name__ = "Integer32"
_EriRouterSRProcessNotifyEventCause_Object = MibTableColumn
eriRouterSRProcessNotifyEventCause = _EriRouterSRProcessNotifyEventCause_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3, 1, 3),
    _EriRouterSRProcessNotifyEventCause_Type()
)
eriRouterSRProcessNotifyEventCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyEventCause.setStatus("current")


class _EriRouterSRProcessNotifyEventType_Type(Integer32):
    """Custom type eriRouterSRProcessNotifyEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("death", 1),
          ("birth", 2))
    )


_EriRouterSRProcessNotifyEventType_Type.__name__ = "Integer32"
_EriRouterSRProcessNotifyEventType_Object = MibTableColumn
eriRouterSRProcessNotifyEventType = _EriRouterSRProcessNotifyEventType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3, 1, 4),
    _EriRouterSRProcessNotifyEventType_Type()
)
eriRouterSRProcessNotifyEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyEventType.setStatus("current")


class _EriRouterSRProcessNumOfSpawn_Type(Unsigned32):
    """Custom type eriRouterSRProcessNumOfSpawn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EriRouterSRProcessNumOfSpawn_Type.__name__ = "Unsigned32"
_EriRouterSRProcessNumOfSpawn_Object = MibTableColumn
eriRouterSRProcessNumOfSpawn = _EriRouterSRProcessNumOfSpawn_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3, 1, 5),
    _EriRouterSRProcessNumOfSpawn_Type()
)
eriRouterSRProcessNumOfSpawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRProcessNumOfSpawn.setStatus("current")
_EriRouterSRProcessNotifyLastTimeSent_Type = TimeTicks
_EriRouterSRProcessNotifyLastTimeSent_Object = MibTableColumn
eriRouterSRProcessNotifyLastTimeSent = _EriRouterSRProcessNotifyLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 1, 3, 1, 6),
    _EriRouterSRProcessNotifyLastTimeSent_Type()
)
eriRouterSRProcessNotifyLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyLastTimeSent.setStatus("current")
_EriRouterSRStorage_ObjectIdentity = ObjectIdentity
eriRouterSRStorage = _EriRouterSRStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2)
)
_EriRouterSRStorageTable_Object = MibTable
eriRouterSRStorageTable = _EriRouterSRStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eriRouterSRStorageTable.setStatus("current")
_EriRouterSRStorageEntry_Object = MibTableRow
eriRouterSRStorageEntry = _EriRouterSRStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1)
)
eriRouterSRStorageEntry.setIndexNames(
    (0, "ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageIndex"),
)
if mibBuilder.loadTexts:
    eriRouterSRStorageEntry.setStatus("current")


class _EriRouterSRStorageIndex_Type(Integer32):
    """Custom type eriRouterSRStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EriRouterSRStorageIndex_Type.__name__ = "Integer32"
_EriRouterSRStorageIndex_Object = MibTableColumn
eriRouterSRStorageIndex = _EriRouterSRStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 1),
    _EriRouterSRStorageIndex_Type()
)
eriRouterSRStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterSRStorageIndex.setStatus("current")


class _EriRouterSRStorageDescr_Type(SnmpAdminString):
    """Custom type eriRouterSRStorageDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EriRouterSRStorageDescr_Type.__name__ = "SnmpAdminString"
_EriRouterSRStorageDescr_Object = MibTableColumn
eriRouterSRStorageDescr = _EriRouterSRStorageDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 2),
    _EriRouterSRStorageDescr_Type()
)
eriRouterSRStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageDescr.setStatus("current")


class _EriRouterSRStorageMedia_Type(Integer32):
    """Custom type eriRouterSRStorageMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("hardDisk", 2),
          ("flashMemory", 3))
    )


_EriRouterSRStorageMedia_Type.__name__ = "Integer32"
_EriRouterSRStorageMedia_Object = MibTableColumn
eriRouterSRStorageMedia = _EriRouterSRStorageMedia_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 3),
    _EriRouterSRStorageMedia_Type()
)
eriRouterSRStorageMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageMedia.setStatus("current")
_EriRouterSRStorageRemovable_Type = TruthValue
_EriRouterSRStorageRemovable_Object = MibTableColumn
eriRouterSRStorageRemovable = _EriRouterSRStorageRemovable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 4),
    _EriRouterSRStorageRemovable_Type()
)
eriRouterSRStorageRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageRemovable.setStatus("current")
_EriRouterSRStorageSize_Type = EriRouterKBytes
_EriRouterSRStorageSize_Object = MibTableColumn
eriRouterSRStorageSize = _EriRouterSRStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 5),
    _EriRouterSRStorageSize_Type()
)
eriRouterSRStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    eriRouterSRStorageSize.setUnits("KBytes")
_EriRouterSRStorageUtilization_Type = EriRouterPercentage
_EriRouterSRStorageUtilization_Object = MibTableColumn
eriRouterSRStorageUtilization = _EriRouterSRStorageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 6),
    _EriRouterSRStorageUtilization_Type()
)
eriRouterSRStorageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageUtilization.setStatus("current")
_EriRouterSRStorageSlot_Type = EriRouterSlot
_EriRouterSRStorageSlot_Object = MibTableColumn
eriRouterSRStorageSlot = _EriRouterSRStorageSlot_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 7),
    _EriRouterSRStorageSlot_Type()
)
eriRouterSRStorageSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageSlot.setStatus("current")
_EriRouterSRStorageMountTime_Type = TimeTicks
_EriRouterSRStorageMountTime_Object = MibTableColumn
eriRouterSRStorageMountTime = _EriRouterSRStorageMountTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 8),
    _EriRouterSRStorageMountTime_Type()
)
eriRouterSRStorageMountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageMountTime.setStatus("current")


class _EriRouterSRStorageStatus_Type(Integer32):
    """Custom type eriRouterSRStorageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("degrading", 2),
          ("failed", 3))
    )


_EriRouterSRStorageStatus_Type.__name__ = "Integer32"
_EriRouterSRStorageStatus_Object = MibTableColumn
eriRouterSRStorageStatus = _EriRouterSRStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 9),
    _EriRouterSRStorageStatus_Type()
)
eriRouterSRStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageStatus.setStatus("current")
_EriRouterSRStorageErrors_Type = Counter32
_EriRouterSRStorageErrors_Object = MibTableColumn
eriRouterSRStorageErrors = _EriRouterSRStorageErrors_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 1, 1, 10),
    _EriRouterSRStorageErrors_Type()
)
eriRouterSRStorageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRStorageErrors.setStatus("current")
_EriRouterSseDiskStorageTable_Object = MibTable
eriRouterSseDiskStorageTable = _EriRouterSseDiskStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eriRouterSseDiskStorageTable.setStatus("current")
_EriRouterSseDiskStorageEntry_Object = MibTableRow
eriRouterSseDiskStorageEntry = _EriRouterSseDiskStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 2, 1)
)
eriRouterSseDiskStorageEntry.setIndexNames(
    (0, "ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskSlot"),
    (0, "ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskNum"),
)
if mibBuilder.loadTexts:
    eriRouterSseDiskStorageEntry.setStatus("current")
_EriRouterSseDiskSlot_Type = EriRouterSlot
_EriRouterSseDiskSlot_Object = MibTableColumn
eriRouterSseDiskSlot = _EriRouterSseDiskSlot_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 2, 1, 1),
    _EriRouterSseDiskSlot_Type()
)
eriRouterSseDiskSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterSseDiskSlot.setStatus("current")


class _EriRouterSseDiskNum_Type(Unsigned32):
    """Custom type eriRouterSseDiskNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EriRouterSseDiskNum_Type.__name__ = "Unsigned32"
_EriRouterSseDiskNum_Object = MibTableColumn
eriRouterSseDiskNum = _EriRouterSseDiskNum_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 2, 1, 2),
    _EriRouterSseDiskNum_Type()
)
eriRouterSseDiskNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterSseDiskNum.setStatus("current")


class _EriRouterSseDiskState_Type(Integer32):
    """Custom type eriRouterSseDiskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_EriRouterSseDiskState_Type.__name__ = "Integer32"
_EriRouterSseDiskState_Object = MibTableColumn
eriRouterSseDiskState = _EriRouterSseDiskState_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 2, 1, 3),
    _EriRouterSseDiskState_Type()
)
eriRouterSseDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSseDiskState.setStatus("current")
_EriRouterSseDiskSize_Type = Unsigned32
_EriRouterSseDiskSize_Object = MibTableColumn
eriRouterSseDiskSize = _EriRouterSseDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 2, 1, 4),
    _EriRouterSseDiskSize_Type()
)
eriRouterSseDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSseDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    eriRouterSseDiskSize.setUnits("GBytes")
_EriRouterSseDiskUsed_Type = Unsigned32
_EriRouterSseDiskUsed_Object = MibTableColumn
eriRouterSseDiskUsed = _EriRouterSseDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 2, 2, 1, 5),
    _EriRouterSseDiskUsed_Type()
)
eriRouterSseDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSseDiskUsed.setStatus("current")
if mibBuilder.loadTexts:
    eriRouterSseDiskUsed.setUnits("GBytes")
_EriRouterSRSystem_ObjectIdentity = ObjectIdentity
eriRouterSRSystem = _EriRouterSRSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 3)
)
_EriRouterSRSystemUptime_Type = TimeTicks
_EriRouterSRSystemUptime_Object = MibScalar
eriRouterSRSystemUptime = _EriRouterSRSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 3, 1),
    _EriRouterSRSystemUptime_Type()
)
eriRouterSRSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSRSystemUptime.setStatus("current")
_EriRouterSRSystemDate_Type = DateAndTime
_EriRouterSRSystemDate_Object = MibScalar
eriRouterSRSystemDate = _EriRouterSRSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 3, 2),
    _EriRouterSRSystemDate_Type()
)
eriRouterSRSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eriRouterSRSystemDate.setStatus("current")
_EriRouterPowerExceeded_ObjectIdentity = ObjectIdentity
eriRouterPowerExceeded = _EriRouterPowerExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 4)
)


class _EriRouterSRPowerExceededStatus_Type(Integer32):
    """Custom type eriRouterSRPowerExceededStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("failed", 2))
    )


_EriRouterSRPowerExceededStatus_Type.__name__ = "Integer32"
_EriRouterSRPowerExceededStatus_Object = MibScalar
eriRouterSRPowerExceededStatus = _EriRouterSRPowerExceededStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 4, 1),
    _EriRouterSRPowerExceededStatus_Type()
)
eriRouterSRPowerExceededStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterSRPowerExceededStatus.setStatus("current")
_EriRouterSseDiskAlarmDateAndTime_Type = DateAndTime
_EriRouterSseDiskAlarmDateAndTime_Object = MibScalar
eriRouterSseDiskAlarmDateAndTime = _EriRouterSseDiskAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 5),
    _EriRouterSseDiskAlarmDateAndTime_Type()
)
eriRouterSseDiskAlarmDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterSseDiskAlarmDateAndTime.setStatus("current")
_EriRouterSseDiskAlarmSeverity_Type = ItuPerceivedSeverity
_EriRouterSseDiskAlarmSeverity_Object = MibScalar
eriRouterSseDiskAlarmSeverity = _EriRouterSseDiskAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 6),
    _EriRouterSseDiskAlarmSeverity_Type()
)
eriRouterSseDiskAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterSseDiskAlarmSeverity.setStatus("current")
_EriRouterSseDiskAlarmProbableCause_Type = IANAItuProbableCause
_EriRouterSseDiskAlarmProbableCause_Object = MibScalar
eriRouterSseDiskAlarmProbableCause = _EriRouterSseDiskAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 7),
    _EriRouterSseDiskAlarmProbableCause_Type()
)
eriRouterSseDiskAlarmProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterSseDiskAlarmProbableCause.setStatus("current")
_EriRouterSseDiskEventType_Type = IANAItuEventType
_EriRouterSseDiskEventType_Object = MibScalar
eriRouterSseDiskEventType = _EriRouterSseDiskEventType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 8),
    _EriRouterSseDiskEventType_Type()
)
eriRouterSseDiskEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterSseDiskEventType.setStatus("current")


class _EriRouterSseDiskAlarmDescription_Type(SnmpAdminString):
    """Custom type eriRouterSseDiskAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EriRouterSseDiskAlarmDescription_Type.__name__ = "SnmpAdminString"
_EriRouterSseDiskAlarmDescription_Object = MibScalar
eriRouterSseDiskAlarmDescription = _EriRouterSseDiskAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 9),
    _EriRouterSseDiskAlarmDescription_Type()
)
eriRouterSseDiskAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterSseDiskAlarmDescription.setStatus("current")
_EriRouterIssuObjects_ObjectIdentity = ObjectIdentity
eriRouterIssuObjects = _EriRouterIssuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 10)
)


class _EriRouterIssuState_Type(Integer32):
    """Custom type eriRouterIssuState based on Integer32"""
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
          ("start", 1),
          ("complete", 2),
          ("aborted", 3))
    )


_EriRouterIssuState_Type.__name__ = "Integer32"
_EriRouterIssuState_Object = MibScalar
eriRouterIssuState = _EriRouterIssuState_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 10, 1),
    _EriRouterIssuState_Type()
)
eriRouterIssuState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterIssuState.setStatus("current")
_EriRouterChassisGroup_ObjectIdentity = ObjectIdentity
eriRouterChassisGroup = _EriRouterChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 11)
)
_EriRouterChassisAlarmId_Type = EriRouterAlarmId
_EriRouterChassisAlarmId_Object = MibScalar
eriRouterChassisAlarmId = _EriRouterChassisAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 11, 1),
    _EriRouterChassisAlarmId_Type()
)
eriRouterChassisAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterChassisAlarmId.setStatus("current")
_EriRouterChassisAlarmType_Type = IANAItuEventType
_EriRouterChassisAlarmType_Object = MibScalar
eriRouterChassisAlarmType = _EriRouterChassisAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 11, 2),
    _EriRouterChassisAlarmType_Type()
)
eriRouterChassisAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterChassisAlarmType.setStatus("current")
_EriRouterChassisAlarmDateAndTime_Type = DateAndTime
_EriRouterChassisAlarmDateAndTime_Object = MibScalar
eriRouterChassisAlarmDateAndTime = _EriRouterChassisAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 11, 3),
    _EriRouterChassisAlarmDateAndTime_Type()
)
eriRouterChassisAlarmDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterChassisAlarmDateAndTime.setStatus("current")


class _EriRouterChassisAlarmDescription_Type(SnmpAdminString):
    """Custom type eriRouterChassisAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EriRouterChassisAlarmDescription_Type.__name__ = "SnmpAdminString"
_EriRouterChassisAlarmDescription_Object = MibScalar
eriRouterChassisAlarmDescription = _EriRouterChassisAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 11, 4),
    _EriRouterChassisAlarmDescription_Type()
)
eriRouterChassisAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterChassisAlarmDescription.setStatus("current")
_EriRouterChassisAlarmProbableCause_Type = IANAItuProbableCause
_EriRouterChassisAlarmProbableCause_Object = MibScalar
eriRouterChassisAlarmProbableCause = _EriRouterChassisAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 11, 5),
    _EriRouterChassisAlarmProbableCause_Type()
)
eriRouterChassisAlarmProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterChassisAlarmProbableCause.setStatus("current")
_EriRouterChassisAlarmSeverity_Type = ItuPerceivedSeverity
_EriRouterChassisAlarmSeverity_Object = MibScalar
eriRouterChassisAlarmSeverity = _EriRouterChassisAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 1, 11, 6),
    _EriRouterChassisAlarmSeverity_Type()
)
eriRouterChassisAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriRouterChassisAlarmSeverity.setStatus("current")
_EriRouterSRMIBConformance_ObjectIdentity = ObjectIdentity
eriRouterSRMIBConformance = _EriRouterSRMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2)
)
_EriRouterSRMIBCompliances_ObjectIdentity = ObjectIdentity
eriRouterSRMIBCompliances = _EriRouterSRMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 1)
)
_EriRouterSRMIBGroups_ObjectIdentity = ObjectIdentity
eriRouterSRMIBGroups = _EriRouterSRMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2)
)

# Managed Objects groups

eriRouterSRProcessNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 1)
)
eriRouterSRProcessNotifyGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyLastUpdate"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessEventNotifyEnable"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyPID"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyEventCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNumOfSpawn"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyLastTimeSent"))
)
if mibBuilder.loadTexts:
    eriRouterSRProcessNotifyGroup.setStatus("current")

eriRouterSRStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 2)
)
eriRouterSRStorageGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageDescr"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageMedia"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageRemovable"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageSize"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageUtilization"))
)
if mibBuilder.loadTexts:
    eriRouterSRStorageGroup.setStatus("deprecated")

eriRouterSRStorageGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 5)
)
eriRouterSRStorageGroup2.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageDescr"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageMedia"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageRemovable"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageSize"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageUtilization"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageSlot"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageMountTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageStatus"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageErrors"))
)
if mibBuilder.loadTexts:
    eriRouterSRStorageGroup2.setStatus("current")

eriRouterSRSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 7)
)
eriRouterSRSystemGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRSystemUptime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRSystemDate"))
)
if mibBuilder.loadTexts:
    eriRouterSRSystemGroup.setStatus("current")

eriRouterSRPowerExceededGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 9)
)
eriRouterSRPowerExceededGroup.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRPowerExceededStatus")
)
if mibBuilder.loadTexts:
    eriRouterSRPowerExceededGroup.setStatus("current")

eriRouterSseDiskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 10)
)
eriRouterSseDiskGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskSize"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskUsed"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskGroup.setStatus("current")

eriRouterSseDiskEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 11)
)
eriRouterSseDiskEventObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskEventObjectGroup.setStatus("current")

eriRouterIssuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 13)
)
eriRouterIssuGroup.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterIssuState")
)
if mibBuilder.loadTexts:
    eriRouterIssuGroup.setStatus("current")

eriRouterChassisEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 15)
)
eriRouterChassisEventObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmId"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmSeverity"))
)
if mibBuilder.loadTexts:
    eriRouterChassisEventObjectGroup.setStatus("current")


# Notification objects

eriRouterSRProcessEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 1)
)
eriRouterSRProcessEvent.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyPID"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyEventCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNumOfSpawn"))
)
if mibBuilder.loadTexts:
    eriRouterSRProcessEvent.setStatus(
        "current"
    )

eriRouterSRSwitchoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 2)
)
if mibBuilder.loadTexts:
    eriRouterSRSwitchoverEvent.setStatus(
        "current"
    )

eriRouterSRStorageFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 3)
)
eriRouterSRStorageFailedEvent.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageDescr"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageMedia"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageSlot"))
)
if mibBuilder.loadTexts:
    eriRouterSRStorageFailedEvent.setStatus(
        "current"
    )

eriRouterSRPowerExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 4)
)
eriRouterSRPowerExceededEvent.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRPowerExceededStatus")
)
if mibBuilder.loadTexts:
    eriRouterSRPowerExceededEvent.setStatus(
        "current"
    )

eriRouterSseDiskHealthDegradedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 5)
)
eriRouterSseDiskHealthDegradedAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskHealthDegradedAlarm.setStatus(
        "current"
    )

eriRouterSseDiskFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 6)
)
eriRouterSseDiskFailedAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskFailedAlarm.setStatus(
        "current"
    )

eriRouterSseDiskMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 7)
)
eriRouterSseDiskMissingAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskMissingAlarm.setStatus(
        "current"
    )

eriRouterSseDiskUnsupportedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 8)
)
eriRouterSseDiskUnsupportedAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskUnsupportedAlarm.setStatus(
        "current"
    )

eriRouterSseDiskOOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 9)
)
eriRouterSseDiskOOSAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskOOSAlarm.setStatus(
        "current"
    )

eriRouterSseDiskVoltageFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 10)
)
eriRouterSseDiskVoltageFailureAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskVoltageFailureAlarm.setStatus(
        "current"
    )

eriRouterSseDiskOverHeatAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 11)
)
eriRouterSseDiskOverHeatAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskOverHeatAlarm.setStatus(
        "current"
    )

eriRouterSseDiskReadFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 12)
)
eriRouterSseDiskReadFailureAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmSeverity"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskEventType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskState"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskReadFailureAlarm.setStatus(
        "current"
    )

eriRouterIssuStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 13)
)
eriRouterIssuStateChange.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterIssuState")
)
if mibBuilder.loadTexts:
    eriRouterIssuStateChange.setStatus(
        "current"
    )

eriRouterChassisAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 0, 14)
)
eriRouterChassisAlarm.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmId"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmType"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmDescription"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmProbableCause"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarmSeverity"))
)
if mibBuilder.loadTexts:
    eriRouterChassisAlarm.setStatus(
        "current"
    )


# Notifications groups

eriRouterSRProcessEventNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 3)
)
eriRouterSRProcessEventNotificationGroup.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessEvent")
)
if mibBuilder.loadTexts:
    eriRouterSRProcessEventNotificationGroup.setStatus(
        "obsolete"
    )

eriRouterSRNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 4)
)
eriRouterSRNotificationGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessEvent"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRSwitchoverEvent"))
)
if mibBuilder.loadTexts:
    eriRouterSRNotificationGroup.setStatus(
        "deprecated"
    )

eriRouterSRNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 6)
)
eriRouterSRNotificationGroup2.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessEvent"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRSwitchoverEvent"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRStorageFailedEvent"))
)
if mibBuilder.loadTexts:
    eriRouterSRNotificationGroup2.setStatus(
        "current"
    )

eriRouterSRPowerNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 8)
)
eriRouterSRPowerNotifyGroup.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRPowerExceededEvent")
)
if mibBuilder.loadTexts:
    eriRouterSRPowerNotifyGroup.setStatus(
        "current"
    )

eriRouterSseDiskNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 12)
)
eriRouterSseDiskNotifyGroup.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskHealthDegradedAlarm"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskFailedAlarm"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskMissingAlarm"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskUnsupportedAlarm"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskOOSAlarm"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskVoltageFailureAlarm"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskOverHeatAlarm"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSseDiskReadFailureAlarm"))
)
if mibBuilder.loadTexts:
    eriRouterSseDiskNotifyGroup.setStatus(
        "current"
    )

eriRouterIssuNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 14)
)
eriRouterIssuNotifyGroup.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterIssuStateChange")
)
if mibBuilder.loadTexts:
    eriRouterIssuNotifyGroup.setStatus(
        "current"
    )

eriRouterChassisNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 2, 16)
)
eriRouterChassisNotifyGroup.setObjects(
    ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterChassisAlarm")
)
if mibBuilder.loadTexts:
    eriRouterChassisNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eriRouterSRMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eriRouterSRMIBCompliance1.setStatus(
        "obsolete"
    )

eriRouterSRMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 1, 2)
)
eriRouterSRMIBCompliance2.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyGroup"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRNotificationGroup"))
)
if mibBuilder.loadTexts:
    eriRouterSRMIBCompliance2.setStatus(
        "deprecated"
    )

eriRouterSRMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 1, 3)
)
eriRouterSRMIBCompliance3.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyGroup"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRNotificationGroup2"))
)
if mibBuilder.loadTexts:
    eriRouterSRMIBCompliance3.setStatus(
        "deprecated"
    )

eriRouterSRMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 1, 4)
)
eriRouterSRMIBCompliance4.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyGroup"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRNotificationGroup2"))
)
if mibBuilder.loadTexts:
    eriRouterSRMIBCompliance4.setStatus(
        "deprecated"
    )

eriRouterSRMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 1, 5)
)
eriRouterSRMIBCompliance.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyGroup"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRNotificationGroup2"))
)
if mibBuilder.loadTexts:
    eriRouterSRMIBCompliance.setStatus(
        "deprecated"
    )

eriRouterSRMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 24, 2, 1, 6)
)
eriRouterSRMIBCompliance6.setObjects(
      *(("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRProcessNotifyGroup"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterSRNotificationGroup2"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterIssuGroup"),
        ("ERICSSON-ROUTER-SYS-RESOURCES-MIB", "eriRouterIssuNotifyGroup"))
)
if mibBuilder.loadTexts:
    eriRouterSRMIBCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-SYS-RESOURCES-MIB",
    **{"eriRouterSysResourcesMib": eriRouterSysResourcesMib,
       "eriRouterSRMIBNotifications": eriRouterSRMIBNotifications,
       "eriRouterSRProcessEvent": eriRouterSRProcessEvent,
       "eriRouterSRSwitchoverEvent": eriRouterSRSwitchoverEvent,
       "eriRouterSRStorageFailedEvent": eriRouterSRStorageFailedEvent,
       "eriRouterSRPowerExceededEvent": eriRouterSRPowerExceededEvent,
       "eriRouterSseDiskHealthDegradedAlarm": eriRouterSseDiskHealthDegradedAlarm,
       "eriRouterSseDiskFailedAlarm": eriRouterSseDiskFailedAlarm,
       "eriRouterSseDiskMissingAlarm": eriRouterSseDiskMissingAlarm,
       "eriRouterSseDiskUnsupportedAlarm": eriRouterSseDiskUnsupportedAlarm,
       "eriRouterSseDiskOOSAlarm": eriRouterSseDiskOOSAlarm,
       "eriRouterSseDiskVoltageFailureAlarm": eriRouterSseDiskVoltageFailureAlarm,
       "eriRouterSseDiskOverHeatAlarm": eriRouterSseDiskOverHeatAlarm,
       "eriRouterSseDiskReadFailureAlarm": eriRouterSseDiskReadFailureAlarm,
       "eriRouterIssuStateChange": eriRouterIssuStateChange,
       "eriRouterChassisAlarm": eriRouterChassisAlarm,
       "eriRouterSRMIBObjects": eriRouterSRMIBObjects,
       "eriRouterSRProcess": eriRouterSRProcess,
       "eriRouterSRProcessNotifyLastUpdate": eriRouterSRProcessNotifyLastUpdate,
       "eriRouterSRProcessEventNotifyEnable": eriRouterSRProcessEventNotifyEnable,
       "eriRouterSRProcessNotifyTable": eriRouterSRProcessNotifyTable,
       "eriRouterSRProcessNotifyEntry": eriRouterSRProcessNotifyEntry,
       "eriRouterSRProcessNotifyProcName": eriRouterSRProcessNotifyProcName,
       "eriRouterSRProcessNotifyPID": eriRouterSRProcessNotifyPID,
       "eriRouterSRProcessNotifyEventCause": eriRouterSRProcessNotifyEventCause,
       "eriRouterSRProcessNotifyEventType": eriRouterSRProcessNotifyEventType,
       "eriRouterSRProcessNumOfSpawn": eriRouterSRProcessNumOfSpawn,
       "eriRouterSRProcessNotifyLastTimeSent": eriRouterSRProcessNotifyLastTimeSent,
       "eriRouterSRStorage": eriRouterSRStorage,
       "eriRouterSRStorageTable": eriRouterSRStorageTable,
       "eriRouterSRStorageEntry": eriRouterSRStorageEntry,
       "eriRouterSRStorageIndex": eriRouterSRStorageIndex,
       "eriRouterSRStorageDescr": eriRouterSRStorageDescr,
       "eriRouterSRStorageMedia": eriRouterSRStorageMedia,
       "eriRouterSRStorageRemovable": eriRouterSRStorageRemovable,
       "eriRouterSRStorageSize": eriRouterSRStorageSize,
       "eriRouterSRStorageUtilization": eriRouterSRStorageUtilization,
       "eriRouterSRStorageSlot": eriRouterSRStorageSlot,
       "eriRouterSRStorageMountTime": eriRouterSRStorageMountTime,
       "eriRouterSRStorageStatus": eriRouterSRStorageStatus,
       "eriRouterSRStorageErrors": eriRouterSRStorageErrors,
       "eriRouterSseDiskStorageTable": eriRouterSseDiskStorageTable,
       "eriRouterSseDiskStorageEntry": eriRouterSseDiskStorageEntry,
       "eriRouterSseDiskSlot": eriRouterSseDiskSlot,
       "eriRouterSseDiskNum": eriRouterSseDiskNum,
       "eriRouterSseDiskState": eriRouterSseDiskState,
       "eriRouterSseDiskSize": eriRouterSseDiskSize,
       "eriRouterSseDiskUsed": eriRouterSseDiskUsed,
       "eriRouterSRSystem": eriRouterSRSystem,
       "eriRouterSRSystemUptime": eriRouterSRSystemUptime,
       "eriRouterSRSystemDate": eriRouterSRSystemDate,
       "eriRouterPowerExceeded": eriRouterPowerExceeded,
       "eriRouterSRPowerExceededStatus": eriRouterSRPowerExceededStatus,
       "eriRouterSseDiskAlarmDateAndTime": eriRouterSseDiskAlarmDateAndTime,
       "eriRouterSseDiskAlarmSeverity": eriRouterSseDiskAlarmSeverity,
       "eriRouterSseDiskAlarmProbableCause": eriRouterSseDiskAlarmProbableCause,
       "eriRouterSseDiskEventType": eriRouterSseDiskEventType,
       "eriRouterSseDiskAlarmDescription": eriRouterSseDiskAlarmDescription,
       "eriRouterIssuObjects": eriRouterIssuObjects,
       "eriRouterIssuState": eriRouterIssuState,
       "eriRouterChassisGroup": eriRouterChassisGroup,
       "eriRouterChassisAlarmId": eriRouterChassisAlarmId,
       "eriRouterChassisAlarmType": eriRouterChassisAlarmType,
       "eriRouterChassisAlarmDateAndTime": eriRouterChassisAlarmDateAndTime,
       "eriRouterChassisAlarmDescription": eriRouterChassisAlarmDescription,
       "eriRouterChassisAlarmProbableCause": eriRouterChassisAlarmProbableCause,
       "eriRouterChassisAlarmSeverity": eriRouterChassisAlarmSeverity,
       "eriRouterSRMIBConformance": eriRouterSRMIBConformance,
       "eriRouterSRMIBCompliances": eriRouterSRMIBCompliances,
       "eriRouterSRMIBCompliance1": eriRouterSRMIBCompliance1,
       "eriRouterSRMIBCompliance2": eriRouterSRMIBCompliance2,
       "eriRouterSRMIBCompliance3": eriRouterSRMIBCompliance3,
       "eriRouterSRMIBCompliance4": eriRouterSRMIBCompliance4,
       "eriRouterSRMIBCompliance": eriRouterSRMIBCompliance,
       "eriRouterSRMIBCompliance6": eriRouterSRMIBCompliance6,
       "eriRouterSRMIBGroups": eriRouterSRMIBGroups,
       "eriRouterSRProcessNotifyGroup": eriRouterSRProcessNotifyGroup,
       "eriRouterSRStorageGroup": eriRouterSRStorageGroup,
       "eriRouterSRProcessEventNotificationGroup": eriRouterSRProcessEventNotificationGroup,
       "eriRouterSRNotificationGroup": eriRouterSRNotificationGroup,
       "eriRouterSRStorageGroup2": eriRouterSRStorageGroup2,
       "eriRouterSRNotificationGroup2": eriRouterSRNotificationGroup2,
       "eriRouterSRSystemGroup": eriRouterSRSystemGroup,
       "eriRouterSRPowerNotifyGroup": eriRouterSRPowerNotifyGroup,
       "eriRouterSRPowerExceededGroup": eriRouterSRPowerExceededGroup,
       "eriRouterSseDiskGroup": eriRouterSseDiskGroup,
       "eriRouterSseDiskEventObjectGroup": eriRouterSseDiskEventObjectGroup,
       "eriRouterSseDiskNotifyGroup": eriRouterSseDiskNotifyGroup,
       "eriRouterIssuGroup": eriRouterIssuGroup,
       "eriRouterIssuNotifyGroup": eriRouterIssuNotifyGroup,
       "eriRouterChassisEventObjectGroup": eriRouterChassisEventObjectGroup,
       "eriRouterChassisNotifyGroup": eriRouterChassisNotifyGroup}
)
