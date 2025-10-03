# SNMP MIB module (SLE-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-RMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:01 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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

sleRmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9)
)
if mibBuilder.loadTexts:
    sleRmon.setRevisions(
        ("2004-12-08 08:40",)
    )


# Types definitions



class OwnerString(OctetString):
    """Custom type OwnerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class SleEntryStatus(Integer32):
    """Custom type SleEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleHistory_ObjectIdentity = ObjectIdentity
sleHistory = _SleHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1)
)
_SleHistoryTable_Object = MibTable
sleHistoryTable = _SleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sleHistoryTable.setStatus("current")
_SleHistoryEntry_Object = MibTableRow
sleHistoryEntry = _SleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1)
)
sleHistoryEntry.setIndexNames(
    (0, "SLE-RMON-MIB", "sleHistoryIndex"),
)
if mibBuilder.loadTexts:
    sleHistoryEntry.setStatus("current")


class _SleHistoryIndex_Type(Integer32):
    """Custom type sleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleHistoryIndex_Type.__name__ = "Integer32"
_SleHistoryIndex_Object = MibTableColumn
sleHistoryIndex = _SleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1, 1),
    _SleHistoryIndex_Type()
)
sleHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryIndex.setStatus("current")
_SleHistoryDataSource_Type = ObjectIdentifier
_SleHistoryDataSource_Object = MibTableColumn
sleHistoryDataSource = _SleHistoryDataSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1, 2),
    _SleHistoryDataSource_Type()
)
sleHistoryDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryDataSource.setStatus("current")


class _SleHistoryBucketsRequested_Type(Integer32):
    """Custom type sleHistoryBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleHistoryBucketsRequested_Type.__name__ = "Integer32"
_SleHistoryBucketsRequested_Object = MibTableColumn
sleHistoryBucketsRequested = _SleHistoryBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1, 3),
    _SleHistoryBucketsRequested_Type()
)
sleHistoryBucketsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryBucketsRequested.setStatus("current")


class _SleHistoryBucketsGranted_Type(Integer32):
    """Custom type sleHistoryBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleHistoryBucketsGranted_Type.__name__ = "Integer32"
_SleHistoryBucketsGranted_Object = MibTableColumn
sleHistoryBucketsGranted = _SleHistoryBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1, 4),
    _SleHistoryBucketsGranted_Type()
)
sleHistoryBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryBucketsGranted.setStatus("current")


class _SleHistoryInterval_Type(Integer32):
    """Custom type sleHistoryInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SleHistoryInterval_Type.__name__ = "Integer32"
_SleHistoryInterval_Object = MibTableColumn
sleHistoryInterval = _SleHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1, 5),
    _SleHistoryInterval_Type()
)
sleHistoryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryInterval.setStatus("current")
_SleHistoryOwner_Type = OwnerString
_SleHistoryOwner_Object = MibTableColumn
sleHistoryOwner = _SleHistoryOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1, 6),
    _SleHistoryOwner_Type()
)
sleHistoryOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryOwner.setStatus("current")
_SleHistoryStatus_Type = SleEntryStatus
_SleHistoryStatus_Object = MibTableColumn
sleHistoryStatus = _SleHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 1, 1, 7),
    _SleHistoryStatus_Type()
)
sleHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryStatus.setStatus("current")
_SleHistoryControl_ObjectIdentity = ObjectIdentity
sleHistoryControl = _SleHistoryControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2)
)


class _SleHistoryControlRequest_Type(Integer32):
    """Custom type sleHistoryControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createHistory", 1),
          ("destroyHistory", 2),
          ("setHistoryProfile", 3))
    )


_SleHistoryControlRequest_Type.__name__ = "Integer32"
_SleHistoryControlRequest_Object = MibScalar
sleHistoryControlRequest = _SleHistoryControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 1),
    _SleHistoryControlRequest_Type()
)
sleHistoryControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlRequest.setStatus("current")
_SleHistoryControlStatus_Type = SleControlStatusType
_SleHistoryControlStatus_Object = MibScalar
sleHistoryControlStatus = _SleHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 2),
    _SleHistoryControlStatus_Type()
)
sleHistoryControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryControlStatus.setStatus("current")
_SleHistoryControlTimer_Type = Gauge32
_SleHistoryControlTimer_Object = MibScalar
sleHistoryControlTimer = _SleHistoryControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 3),
    _SleHistoryControlTimer_Type()
)
sleHistoryControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlTimer.setStatus("current")
_SleHistoryControlTimeStamp_Type = TimeTicks
_SleHistoryControlTimeStamp_Object = MibScalar
sleHistoryControlTimeStamp = _SleHistoryControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 4),
    _SleHistoryControlTimeStamp_Type()
)
sleHistoryControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryControlTimeStamp.setStatus("current")
_SleHistoryControlReqResult_Type = SleControlRequestResultType
_SleHistoryControlReqResult_Object = MibScalar
sleHistoryControlReqResult = _SleHistoryControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 5),
    _SleHistoryControlReqResult_Type()
)
sleHistoryControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleHistoryControlReqResult.setStatus("current")


class _SleHistoryControlIndex_Type(Integer32):
    """Custom type sleHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleHistoryControlIndex_Type.__name__ = "Integer32"
_SleHistoryControlIndex_Object = MibScalar
sleHistoryControlIndex = _SleHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 6),
    _SleHistoryControlIndex_Type()
)
sleHistoryControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlIndex.setStatus("current")
_SleHistoryControlDataSource_Type = ObjectIdentifier
_SleHistoryControlDataSource_Object = MibScalar
sleHistoryControlDataSource = _SleHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 7),
    _SleHistoryControlDataSource_Type()
)
sleHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlDataSource.setStatus("current")


class _SleHistoryControlBucketsRequested_Type(Integer32):
    """Custom type sleHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_SleHistoryControlBucketsRequested_Object = MibScalar
sleHistoryControlBucketsRequested = _SleHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 8),
    _SleHistoryControlBucketsRequested_Type()
)
sleHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlBucketsRequested.setStatus("current")


class _SleHistoryControlInterval_Type(Integer32):
    """Custom type sleHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SleHistoryControlInterval_Type.__name__ = "Integer32"
_SleHistoryControlInterval_Object = MibScalar
sleHistoryControlInterval = _SleHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 9),
    _SleHistoryControlInterval_Type()
)
sleHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlInterval.setStatus("current")
_SleHistoryControlOwner_Type = OwnerString
_SleHistoryControlOwner_Object = MibScalar
sleHistoryControlOwner = _SleHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 10),
    _SleHistoryControlOwner_Type()
)
sleHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlOwner.setStatus("current")
_SleHistoryControlSts_Type = SleEntryStatus
_SleHistoryControlSts_Object = MibScalar
sleHistoryControlSts = _SleHistoryControlSts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 2, 11),
    _SleHistoryControlSts_Type()
)
sleHistoryControlSts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleHistoryControlSts.setStatus("current")
_SleHistoryNotification_ObjectIdentity = ObjectIdentity
sleHistoryNotification = _SleHistoryNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 3)
)
_SleAlarm_ObjectIdentity = ObjectIdentity
sleAlarm = _SleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2)
)
_SleAlarmTable_Object = MibTable
sleAlarmTable = _SleAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1)
)
if mibBuilder.loadTexts:
    sleAlarmTable.setStatus("current")
_SleAlarmEntry_Object = MibTableRow
sleAlarmEntry = _SleAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1)
)
sleAlarmEntry.setIndexNames(
    (0, "SLE-RMON-MIB", "sleAlarmIndex"),
)
if mibBuilder.loadTexts:
    sleAlarmEntry.setStatus("current")


class _SleAlarmIndex_Type(Integer32):
    """Custom type sleAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleAlarmIndex_Type.__name__ = "Integer32"
_SleAlarmIndex_Object = MibTableColumn
sleAlarmIndex = _SleAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 1),
    _SleAlarmIndex_Type()
)
sleAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmIndex.setStatus("current")
_SleAlarmInterval_Type = Integer32
_SleAlarmInterval_Object = MibTableColumn
sleAlarmInterval = _SleAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 2),
    _SleAlarmInterval_Type()
)
sleAlarmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmInterval.setStatus("current")
_SleAlarmVariable_Type = ObjectIdentifier
_SleAlarmVariable_Object = MibTableColumn
sleAlarmVariable = _SleAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 3),
    _SleAlarmVariable_Type()
)
sleAlarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmVariable.setStatus("current")


class _SleAlarmSampleType_Type(Integer32):
    """Custom type sleAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_SleAlarmSampleType_Type.__name__ = "Integer32"
_SleAlarmSampleType_Object = MibTableColumn
sleAlarmSampleType = _SleAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 4),
    _SleAlarmSampleType_Type()
)
sleAlarmSampleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmSampleType.setStatus("current")
_SleAlarmValue_Type = Integer32
_SleAlarmValue_Object = MibTableColumn
sleAlarmValue = _SleAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 5),
    _SleAlarmValue_Type()
)
sleAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmValue.setStatus("current")


class _SleAlarmStartupAlarm_Type(Integer32):
    """Custom type sleAlarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("risingAlarm", 1),
          ("fallingAlarm", 2),
          ("risingOrFallingAlarm", 3))
    )


_SleAlarmStartupAlarm_Type.__name__ = "Integer32"
_SleAlarmStartupAlarm_Object = MibTableColumn
sleAlarmStartupAlarm = _SleAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 6),
    _SleAlarmStartupAlarm_Type()
)
sleAlarmStartupAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmStartupAlarm.setStatus("current")
_SleAlarmRisingThreshold_Type = Integer32
_SleAlarmRisingThreshold_Object = MibTableColumn
sleAlarmRisingThreshold = _SleAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 7),
    _SleAlarmRisingThreshold_Type()
)
sleAlarmRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmRisingThreshold.setStatus("current")
_SleAlarmFallingThreshold_Type = Integer32
_SleAlarmFallingThreshold_Object = MibTableColumn
sleAlarmFallingThreshold = _SleAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 8),
    _SleAlarmFallingThreshold_Type()
)
sleAlarmFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmFallingThreshold.setStatus("current")


class _SleAlarmRisingEventIndex_Type(Integer32):
    """Custom type sleAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleAlarmRisingEventIndex_Type.__name__ = "Integer32"
_SleAlarmRisingEventIndex_Object = MibTableColumn
sleAlarmRisingEventIndex = _SleAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 9),
    _SleAlarmRisingEventIndex_Type()
)
sleAlarmRisingEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmRisingEventIndex.setStatus("current")


class _SleAlarmFallingEventIndex_Type(Integer32):
    """Custom type sleAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleAlarmFallingEventIndex_Type.__name__ = "Integer32"
_SleAlarmFallingEventIndex_Object = MibTableColumn
sleAlarmFallingEventIndex = _SleAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 10),
    _SleAlarmFallingEventIndex_Type()
)
sleAlarmFallingEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmFallingEventIndex.setStatus("current")
_SleAlarmOwner_Type = OwnerString
_SleAlarmOwner_Object = MibTableColumn
sleAlarmOwner = _SleAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 11),
    _SleAlarmOwner_Type()
)
sleAlarmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmOwner.setStatus("current")
_SleAlarmStatus_Type = SleEntryStatus
_SleAlarmStatus_Object = MibTableColumn
sleAlarmStatus = _SleAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 1, 1, 12),
    _SleAlarmStatus_Type()
)
sleAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmStatus.setStatus("current")
_SleAlarmControl_ObjectIdentity = ObjectIdentity
sleAlarmControl = _SleAlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2)
)


class _SleAlarmControlRequest_Type(Integer32):
    """Custom type sleAlarmControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createAlarm", 1),
          ("destroyAlarm", 2),
          ("setAlarmProfile", 3))
    )


_SleAlarmControlRequest_Type.__name__ = "Integer32"
_SleAlarmControlRequest_Object = MibScalar
sleAlarmControlRequest = _SleAlarmControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 1),
    _SleAlarmControlRequest_Type()
)
sleAlarmControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlRequest.setStatus("current")
_SleAlarmControlStatus_Type = SleControlStatusType
_SleAlarmControlStatus_Object = MibScalar
sleAlarmControlStatus = _SleAlarmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 2),
    _SleAlarmControlStatus_Type()
)
sleAlarmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmControlStatus.setStatus("current")
_SleAlarmControlTimer_Type = Gauge32
_SleAlarmControlTimer_Object = MibScalar
sleAlarmControlTimer = _SleAlarmControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 3),
    _SleAlarmControlTimer_Type()
)
sleAlarmControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlTimer.setStatus("current")
_SleAlarmControlTimeStamp_Type = TimeTicks
_SleAlarmControlTimeStamp_Object = MibScalar
sleAlarmControlTimeStamp = _SleAlarmControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 4),
    _SleAlarmControlTimeStamp_Type()
)
sleAlarmControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmControlTimeStamp.setStatus("current")
_SleAlarmControlReqResult_Type = SleControlRequestResultType
_SleAlarmControlReqResult_Object = MibScalar
sleAlarmControlReqResult = _SleAlarmControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 5),
    _SleAlarmControlReqResult_Type()
)
sleAlarmControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAlarmControlReqResult.setStatus("current")


class _SleAlarmControlIndex_Type(Integer32):
    """Custom type sleAlarmControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleAlarmControlIndex_Type.__name__ = "Integer32"
_SleAlarmControlIndex_Object = MibScalar
sleAlarmControlIndex = _SleAlarmControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 6),
    _SleAlarmControlIndex_Type()
)
sleAlarmControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlIndex.setStatus("current")
_SleAlarmControlInterval_Type = Integer32
_SleAlarmControlInterval_Object = MibScalar
sleAlarmControlInterval = _SleAlarmControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 7),
    _SleAlarmControlInterval_Type()
)
sleAlarmControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlInterval.setStatus("current")
_SleAlarmControlVariable_Type = ObjectIdentifier
_SleAlarmControlVariable_Object = MibScalar
sleAlarmControlVariable = _SleAlarmControlVariable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 8),
    _SleAlarmControlVariable_Type()
)
sleAlarmControlVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlVariable.setStatus("current")


class _SleAlarmControlSampleType_Type(Integer32):
    """Custom type sleAlarmControlSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_SleAlarmControlSampleType_Type.__name__ = "Integer32"
_SleAlarmControlSampleType_Object = MibScalar
sleAlarmControlSampleType = _SleAlarmControlSampleType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 9),
    _SleAlarmControlSampleType_Type()
)
sleAlarmControlSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlSampleType.setStatus("current")


class _SleAlarmControlStartupAlarm_Type(Integer32):
    """Custom type sleAlarmControlStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("risingAlarm", 1),
          ("fallingAlarm", 2),
          ("risingOrFallingAlarm", 3))
    )


_SleAlarmControlStartupAlarm_Type.__name__ = "Integer32"
_SleAlarmControlStartupAlarm_Object = MibScalar
sleAlarmControlStartupAlarm = _SleAlarmControlStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 10),
    _SleAlarmControlStartupAlarm_Type()
)
sleAlarmControlStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlStartupAlarm.setStatus("current")
_SleAlarmControlRisingThreshold_Type = Integer32
_SleAlarmControlRisingThreshold_Object = MibScalar
sleAlarmControlRisingThreshold = _SleAlarmControlRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 11),
    _SleAlarmControlRisingThreshold_Type()
)
sleAlarmControlRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlRisingThreshold.setStatus("current")
_SleAlarmControlFallingThreshold_Type = Integer32
_SleAlarmControlFallingThreshold_Object = MibScalar
sleAlarmControlFallingThreshold = _SleAlarmControlFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 12),
    _SleAlarmControlFallingThreshold_Type()
)
sleAlarmControlFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlFallingThreshold.setStatus("current")


class _SleAlarmControlRisingEventIndex_Type(Integer32):
    """Custom type sleAlarmControlRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleAlarmControlRisingEventIndex_Type.__name__ = "Integer32"
_SleAlarmControlRisingEventIndex_Object = MibScalar
sleAlarmControlRisingEventIndex = _SleAlarmControlRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 13),
    _SleAlarmControlRisingEventIndex_Type()
)
sleAlarmControlRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlRisingEventIndex.setStatus("current")


class _SleAlarmControlFallingEventIndex_Type(Integer32):
    """Custom type sleAlarmControlFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleAlarmControlFallingEventIndex_Type.__name__ = "Integer32"
_SleAlarmControlFallingEventIndex_Object = MibScalar
sleAlarmControlFallingEventIndex = _SleAlarmControlFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 14),
    _SleAlarmControlFallingEventIndex_Type()
)
sleAlarmControlFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlFallingEventIndex.setStatus("current")
_SleAlarmControlOwner_Type = OwnerString
_SleAlarmControlOwner_Object = MibScalar
sleAlarmControlOwner = _SleAlarmControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 15),
    _SleAlarmControlOwner_Type()
)
sleAlarmControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlOwner.setStatus("current")
_SleAlarmControlSts_Type = SleEntryStatus
_SleAlarmControlSts_Object = MibScalar
sleAlarmControlSts = _SleAlarmControlSts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 2, 16),
    _SleAlarmControlSts_Type()
)
sleAlarmControlSts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAlarmControlSts.setStatus("current")
_SleAlarmNotification_ObjectIdentity = ObjectIdentity
sleAlarmNotification = _SleAlarmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 3)
)
_SleEvent_ObjectIdentity = ObjectIdentity
sleEvent = _SleEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3)
)
_SleEventTable_Object = MibTable
sleEventTable = _SleEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1)
)
if mibBuilder.loadTexts:
    sleEventTable.setStatus("current")
_SleEventEntry_Object = MibTableRow
sleEventEntry = _SleEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1)
)
sleEventEntry.setIndexNames(
    (0, "SLE-RMON-MIB", "sleEventIndex"),
)
if mibBuilder.loadTexts:
    sleEventEntry.setStatus("current")


class _SleEventIndex_Type(Integer32):
    """Custom type sleEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleEventIndex_Type.__name__ = "Integer32"
_SleEventIndex_Object = MibTableColumn
sleEventIndex = _SleEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1, 1),
    _SleEventIndex_Type()
)
sleEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventIndex.setStatus("current")


class _SleEventDescription_Type(DisplayString):
    """Custom type sleEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SleEventDescription_Type.__name__ = "DisplayString"
_SleEventDescription_Object = MibTableColumn
sleEventDescription = _SleEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1, 2),
    _SleEventDescription_Type()
)
sleEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventDescription.setStatus("current")


class _SleEventType_Type(Integer32):
    """Custom type sleEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("log", 2),
          ("snmpTrap", 3),
          ("logAndTrap", 4))
    )


_SleEventType_Type.__name__ = "Integer32"
_SleEventType_Object = MibTableColumn
sleEventType = _SleEventType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1, 3),
    _SleEventType_Type()
)
sleEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventType.setStatus("current")


class _SleEventCommunity_Type(OctetString):
    """Custom type sleEventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SleEventCommunity_Type.__name__ = "OctetString"
_SleEventCommunity_Object = MibTableColumn
sleEventCommunity = _SleEventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1, 4),
    _SleEventCommunity_Type()
)
sleEventCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventCommunity.setStatus("current")
_SleEventLastTimeSent_Type = TimeTicks
_SleEventLastTimeSent_Object = MibTableColumn
sleEventLastTimeSent = _SleEventLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1, 5),
    _SleEventLastTimeSent_Type()
)
sleEventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventLastTimeSent.setStatus("current")
_SleEventOwner_Type = OwnerString
_SleEventOwner_Object = MibTableColumn
sleEventOwner = _SleEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1, 6),
    _SleEventOwner_Type()
)
sleEventOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventOwner.setStatus("current")
_SleEventStatus_Type = SleEntryStatus
_SleEventStatus_Object = MibTableColumn
sleEventStatus = _SleEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 1, 1, 7),
    _SleEventStatus_Type()
)
sleEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventStatus.setStatus("current")
_SleEventControl_ObjectIdentity = ObjectIdentity
sleEventControl = _SleEventControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2)
)


class _SleEventControlRequest_Type(Integer32):
    """Custom type sleEventControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createEvent", 1),
          ("destroyEvent", 2),
          ("setEventProfile", 3))
    )


_SleEventControlRequest_Type.__name__ = "Integer32"
_SleEventControlRequest_Object = MibScalar
sleEventControlRequest = _SleEventControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 1),
    _SleEventControlRequest_Type()
)
sleEventControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlRequest.setStatus("current")
_SleEventControlStatus_Type = SleControlStatusType
_SleEventControlStatus_Object = MibScalar
sleEventControlStatus = _SleEventControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 2),
    _SleEventControlStatus_Type()
)
sleEventControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventControlStatus.setStatus("current")
_SleEventControlTimer_Type = Gauge32
_SleEventControlTimer_Object = MibScalar
sleEventControlTimer = _SleEventControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 3),
    _SleEventControlTimer_Type()
)
sleEventControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlTimer.setStatus("current")
_SleEventControlTimeStamp_Type = TimeTicks
_SleEventControlTimeStamp_Object = MibScalar
sleEventControlTimeStamp = _SleEventControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 4),
    _SleEventControlTimeStamp_Type()
)
sleEventControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventControlTimeStamp.setStatus("current")
_SleEventControlReqResult_Type = SleControlRequestResultType
_SleEventControlReqResult_Object = MibScalar
sleEventControlReqResult = _SleEventControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 5),
    _SleEventControlReqResult_Type()
)
sleEventControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEventControlReqResult.setStatus("current")


class _SleEventControlIndex_Type(Integer32):
    """Custom type sleEventControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleEventControlIndex_Type.__name__ = "Integer32"
_SleEventControlIndex_Object = MibScalar
sleEventControlIndex = _SleEventControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 6),
    _SleEventControlIndex_Type()
)
sleEventControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlIndex.setStatus("current")


class _SleEventControlDescription_Type(DisplayString):
    """Custom type sleEventControlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SleEventControlDescription_Type.__name__ = "DisplayString"
_SleEventControlDescription_Object = MibScalar
sleEventControlDescription = _SleEventControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 7),
    _SleEventControlDescription_Type()
)
sleEventControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlDescription.setStatus("current")


class _SleEventControlType_Type(Integer32):
    """Custom type sleEventControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("log", 2),
          ("snmpTrap", 3),
          ("logAndTrap", 4))
    )


_SleEventControlType_Type.__name__ = "Integer32"
_SleEventControlType_Object = MibScalar
sleEventControlType = _SleEventControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 8),
    _SleEventControlType_Type()
)
sleEventControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlType.setStatus("current")


class _SleEventControlCommunity_Type(OctetString):
    """Custom type sleEventControlCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SleEventControlCommunity_Type.__name__ = "OctetString"
_SleEventControlCommunity_Object = MibScalar
sleEventControlCommunity = _SleEventControlCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 9),
    _SleEventControlCommunity_Type()
)
sleEventControlCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlCommunity.setStatus("current")
_SleEventControlOwner_Type = OwnerString
_SleEventControlOwner_Object = MibScalar
sleEventControlOwner = _SleEventControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 10),
    _SleEventControlOwner_Type()
)
sleEventControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlOwner.setStatus("current")
_SleEventControlSts_Type = SleEntryStatus
_SleEventControlSts_Object = MibScalar
sleEventControlSts = _SleEventControlSts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 2, 11),
    _SleEventControlSts_Type()
)
sleEventControlSts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEventControlSts.setStatus("current")
_SleEventNotification_ObjectIdentity = ObjectIdentity
sleEventNotification = _SleEventNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 3)
)
_SleStatistics_ObjectIdentity = ObjectIdentity
sleStatistics = _SleStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4)
)
_SleEtherStats_ObjectIdentity = ObjectIdentity
sleEtherStats = _SleEtherStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1)
)
_SleEtherStatsTable_Object = MibTable
sleEtherStatsTable = _SleEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleEtherStatsTable.setStatus("current")
_SleEtherStatsEntry_Object = MibTableRow
sleEtherStatsEntry = _SleEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1)
)
sleEtherStatsEntry.setIndexNames(
    (0, "SLE-RMON-MIB", "sleEtherStatsIndex"),
)
if mibBuilder.loadTexts:
    sleEtherStatsEntry.setStatus("current")


class _SleEtherStatsIndex_Type(Integer32):
    """Custom type sleEtherStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleEtherStatsIndex_Type.__name__ = "Integer32"
_SleEtherStatsIndex_Object = MibTableColumn
sleEtherStatsIndex = _SleEtherStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 1),
    _SleEtherStatsIndex_Type()
)
sleEtherStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsIndex.setStatus("current")
_SleEtherStatsDataSource_Type = ObjectIdentifier
_SleEtherStatsDataSource_Object = MibTableColumn
sleEtherStatsDataSource = _SleEtherStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 2),
    _SleEtherStatsDataSource_Type()
)
sleEtherStatsDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsDataSource.setStatus("current")
_SleEtherStatsDropEvents_Type = Counter32
_SleEtherStatsDropEvents_Object = MibTableColumn
sleEtherStatsDropEvents = _SleEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 3),
    _SleEtherStatsDropEvents_Type()
)
sleEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsDropEvents.setStatus("current")
_SleEtherStatsOctets_Type = Counter32
_SleEtherStatsOctets_Object = MibTableColumn
sleEtherStatsOctets = _SleEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 4),
    _SleEtherStatsOctets_Type()
)
sleEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsOctets.setStatus("current")
_SleEtherStatsPkts_Type = Counter32
_SleEtherStatsPkts_Object = MibTableColumn
sleEtherStatsPkts = _SleEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 5),
    _SleEtherStatsPkts_Type()
)
sleEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsPkts.setStatus("current")
_SleEtherStatsBroadcastPkts_Type = Counter32
_SleEtherStatsBroadcastPkts_Object = MibTableColumn
sleEtherStatsBroadcastPkts = _SleEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 6),
    _SleEtherStatsBroadcastPkts_Type()
)
sleEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsBroadcastPkts.setStatus("current")
_SleEtherStatsMulticastPkts_Type = Counter32
_SleEtherStatsMulticastPkts_Object = MibTableColumn
sleEtherStatsMulticastPkts = _SleEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 7),
    _SleEtherStatsMulticastPkts_Type()
)
sleEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsMulticastPkts.setStatus("current")
_SleEtherStatsCRCAlignErrors_Type = Counter32
_SleEtherStatsCRCAlignErrors_Object = MibTableColumn
sleEtherStatsCRCAlignErrors = _SleEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 8),
    _SleEtherStatsCRCAlignErrors_Type()
)
sleEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsCRCAlignErrors.setStatus("current")
_SleEtherStatsUndersizePkts_Type = Counter32
_SleEtherStatsUndersizePkts_Object = MibTableColumn
sleEtherStatsUndersizePkts = _SleEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 9),
    _SleEtherStatsUndersizePkts_Type()
)
sleEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsUndersizePkts.setStatus("current")
_SleEtherStatsOversizePkts_Type = Counter32
_SleEtherStatsOversizePkts_Object = MibTableColumn
sleEtherStatsOversizePkts = _SleEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 10),
    _SleEtherStatsOversizePkts_Type()
)
sleEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsOversizePkts.setStatus("current")
_SleEtherStatsFragments_Type = Counter32
_SleEtherStatsFragments_Object = MibTableColumn
sleEtherStatsFragments = _SleEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 11),
    _SleEtherStatsFragments_Type()
)
sleEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsFragments.setStatus("current")
_SleEtherStatsJabbers_Type = Counter32
_SleEtherStatsJabbers_Object = MibTableColumn
sleEtherStatsJabbers = _SleEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 12),
    _SleEtherStatsJabbers_Type()
)
sleEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsJabbers.setStatus("current")
_SleEtherStatsCollisions_Type = Counter32
_SleEtherStatsCollisions_Object = MibTableColumn
sleEtherStatsCollisions = _SleEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 13),
    _SleEtherStatsCollisions_Type()
)
sleEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsCollisions.setStatus("current")
_SleEtherStatsPkts64Octets_Type = Counter32
_SleEtherStatsPkts64Octets_Object = MibTableColumn
sleEtherStatsPkts64Octets = _SleEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 14),
    _SleEtherStatsPkts64Octets_Type()
)
sleEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsPkts64Octets.setStatus("current")
_SleEtherStatsPkts65to127Octets_Type = Counter32
_SleEtherStatsPkts65to127Octets_Object = MibTableColumn
sleEtherStatsPkts65to127Octets = _SleEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 15),
    _SleEtherStatsPkts65to127Octets_Type()
)
sleEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsPkts65to127Octets.setStatus("current")
_SleEtherStatsPkts128to255Octets_Type = Counter32
_SleEtherStatsPkts128to255Octets_Object = MibTableColumn
sleEtherStatsPkts128to255Octets = _SleEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 16),
    _SleEtherStatsPkts128to255Octets_Type()
)
sleEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsPkts128to255Octets.setStatus("current")
_SleEtherStatsPkts256to511Octets_Type = Counter32
_SleEtherStatsPkts256to511Octets_Object = MibTableColumn
sleEtherStatsPkts256to511Octets = _SleEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 17),
    _SleEtherStatsPkts256to511Octets_Type()
)
sleEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsPkts256to511Octets.setStatus("current")
_SleEtherStatsPkts512to1023Octets_Type = Counter32
_SleEtherStatsPkts512to1023Octets_Object = MibTableColumn
sleEtherStatsPkts512to1023Octets = _SleEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 18),
    _SleEtherStatsPkts512to1023Octets_Type()
)
sleEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsPkts512to1023Octets.setStatus("current")
_SleEtherStatsPkts1024to1518Octets_Type = Counter32
_SleEtherStatsPkts1024to1518Octets_Object = MibTableColumn
sleEtherStatsPkts1024to1518Octets = _SleEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 19),
    _SleEtherStatsPkts1024to1518Octets_Type()
)
sleEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsPkts1024to1518Octets.setStatus("current")
_SleEtherStatsOwner_Type = OctetString
_SleEtherStatsOwner_Object = MibTableColumn
sleEtherStatsOwner = _SleEtherStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 20),
    _SleEtherStatsOwner_Type()
)
sleEtherStatsOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsOwner.setStatus("current")
_SleEtherStatsStatus_Type = SleEntryStatus
_SleEtherStatsStatus_Object = MibTableColumn
sleEtherStatsStatus = _SleEtherStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 21),
    _SleEtherStatsStatus_Type()
)
sleEtherStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsStatus.setStatus("current")
_SleEtherStatsClearedTime_Type = TimeTicks
_SleEtherStatsClearedTime_Object = MibTableColumn
sleEtherStatsClearedTime = _SleEtherStatsClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 1, 1, 22),
    _SleEtherStatsClearedTime_Type()
)
sleEtherStatsClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsClearedTime.setStatus("current")
_SleEtherStatsControl_ObjectIdentity = ObjectIdentity
sleEtherStatsControl = _SleEtherStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 2)
)


class _SleEtherStatsControlRequest_Type(Integer32):
    """Custom type sleEtherStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearRmonStat", 1)
    )


_SleEtherStatsControlRequest_Type.__name__ = "Integer32"
_SleEtherStatsControlRequest_Object = MibScalar
sleEtherStatsControlRequest = _SleEtherStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 2, 1),
    _SleEtherStatsControlRequest_Type()
)
sleEtherStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEtherStatsControlRequest.setStatus("current")
_SleEtherStatsControlStatus_Type = SleControlStatusType
_SleEtherStatsControlStatus_Object = MibScalar
sleEtherStatsControlStatus = _SleEtherStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 2, 2),
    _SleEtherStatsControlStatus_Type()
)
sleEtherStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsControlStatus.setStatus("current")
_SleEtherStatsControlTimer_Type = Gauge32
_SleEtherStatsControlTimer_Object = MibScalar
sleEtherStatsControlTimer = _SleEtherStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 2, 3),
    _SleEtherStatsControlTimer_Type()
)
sleEtherStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEtherStatsControlTimer.setStatus("current")
_SleEtherStatsControlTimeStamp_Type = TimeTicks
_SleEtherStatsControlTimeStamp_Object = MibScalar
sleEtherStatsControlTimeStamp = _SleEtherStatsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 2, 4),
    _SleEtherStatsControlTimeStamp_Type()
)
sleEtherStatsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsControlTimeStamp.setStatus("current")
_SleEtherStatsControlReqResult_Type = SleControlRequestResultType
_SleEtherStatsControlReqResult_Object = MibScalar
sleEtherStatsControlReqResult = _SleEtherStatsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 2, 5),
    _SleEtherStatsControlReqResult_Type()
)
sleEtherStatsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEtherStatsControlReqResult.setStatus("current")


class _SleEtherStatsControlIfIndex_Type(Integer32):
    """Custom type sleEtherStatsControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleEtherStatsControlIfIndex_Type.__name__ = "Integer32"
_SleEtherStatsControlIfIndex_Object = MibScalar
sleEtherStatsControlIfIndex = _SleEtherStatsControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 4, 1, 2, 6),
    _SleEtherStatsControlIfIndex_Type()
)
sleEtherStatsControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleEtherStatsControlIfIndex.setStatus("current")
_SleRmonSimple_ObjectIdentity = ObjectIdentity
sleRmonSimple = _SleRmonSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5)
)
_SleRmonSimpleTable_Object = MibTable
sleRmonSimpleTable = _SleRmonSimpleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 1)
)
if mibBuilder.loadTexts:
    sleRmonSimpleTable.setStatus("current")
_SleRmonSimpleEntry_Object = MibTableRow
sleRmonSimpleEntry = _SleRmonSimpleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 1, 1)
)
sleRmonSimpleEntry.setIndexNames(
    (0, "SLE-RMON-MIB", "sleRmonSimplePortIndex"),
    (0, "SLE-RMON-MIB", "sleRmonSimpleSampleVariable"),
)
if mibBuilder.loadTexts:
    sleRmonSimpleEntry.setStatus("current")


class _SleRmonSimplePortIndex_Type(Integer32):
    """Custom type sleRmonSimplePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleRmonSimplePortIndex_Type.__name__ = "Integer32"
_SleRmonSimplePortIndex_Object = MibTableColumn
sleRmonSimplePortIndex = _SleRmonSimplePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 1, 1, 1),
    _SleRmonSimplePortIndex_Type()
)
sleRmonSimplePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimplePortIndex.setStatus("current")


class _SleRmonSimpleSampleVariable_Type(Integer32):
    """Custom type sleRmonSimpleSampleVariable based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("crcAlignError", 1),
          ("jabber", 2),
          ("oversizePackets", 3),
          ("undersizePackets", 4),
          ("fragments", 5),
          ("dropEvents", 6),
          ("collisions", 7),
          ("ifInDiscards", 8),
          ("ifInErrors", 9),
          ("ifOutDiscards", 10),
          ("ifOutErrors", 11),
          ("ifInPauseFrame", 12),
          ("ifOutPauseFrame", 13))
    )


_SleRmonSimpleSampleVariable_Type.__name__ = "Integer32"
_SleRmonSimpleSampleVariable_Object = MibTableColumn
sleRmonSimpleSampleVariable = _SleRmonSimpleSampleVariable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 1, 1, 2),
    _SleRmonSimpleSampleVariable_Type()
)
sleRmonSimpleSampleVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleSampleVariable.setStatus("current")
_SleRmonSimpleSampleInterval_Type = Integer32
_SleRmonSimpleSampleInterval_Object = MibTableColumn
sleRmonSimpleSampleInterval = _SleRmonSimpleSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 1, 1, 3),
    _SleRmonSimpleSampleInterval_Type()
)
sleRmonSimpleSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleSampleInterval.setStatus("current")
_SleRmonSimpleRisingThreshold_Type = Integer32
_SleRmonSimpleRisingThreshold_Object = MibTableColumn
sleRmonSimpleRisingThreshold = _SleRmonSimpleRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 1, 1, 4),
    _SleRmonSimpleRisingThreshold_Type()
)
sleRmonSimpleRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleRisingThreshold.setStatus("current")
_SleRmonSimpleFallingThreshold_Type = Integer32
_SleRmonSimpleFallingThreshold_Object = MibTableColumn
sleRmonSimpleFallingThreshold = _SleRmonSimpleFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 1, 1, 5),
    _SleRmonSimpleFallingThreshold_Type()
)
sleRmonSimpleFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleFallingThreshold.setStatus("current")
_SleRmonSimpleControl_ObjectIdentity = ObjectIdentity
sleRmonSimpleControl = _SleRmonSimpleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2)
)


class _SleRmonSimpleControlRequest_Type(Integer32):
    """Custom type sleRmonSimpleControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRmonSimple", 1),
          ("delRmonSimple", 2))
    )


_SleRmonSimpleControlRequest_Type.__name__ = "Integer32"
_SleRmonSimpleControlRequest_Object = MibScalar
sleRmonSimpleControlRequest = _SleRmonSimpleControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 1),
    _SleRmonSimpleControlRequest_Type()
)
sleRmonSimpleControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleControlRequest.setStatus("current")
_SleRmonSimpleControlStatus_Type = SleControlStatusType
_SleRmonSimpleControlStatus_Object = MibScalar
sleRmonSimpleControlStatus = _SleRmonSimpleControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 2),
    _SleRmonSimpleControlStatus_Type()
)
sleRmonSimpleControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleControlStatus.setStatus("current")
_SleRmonSimpleControlTimer_Type = Gauge32
_SleRmonSimpleControlTimer_Object = MibScalar
sleRmonSimpleControlTimer = _SleRmonSimpleControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 3),
    _SleRmonSimpleControlTimer_Type()
)
sleRmonSimpleControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleControlTimer.setStatus("current")
_SleRmonSimpleControlTimeStamp_Type = TimeTicks
_SleRmonSimpleControlTimeStamp_Object = MibScalar
sleRmonSimpleControlTimeStamp = _SleRmonSimpleControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 4),
    _SleRmonSimpleControlTimeStamp_Type()
)
sleRmonSimpleControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleControlTimeStamp.setStatus("current")
_SleRmonSimpleControlReqResult_Type = SleControlRequestResultType
_SleRmonSimpleControlReqResult_Object = MibScalar
sleRmonSimpleControlReqResult = _SleRmonSimpleControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 5),
    _SleRmonSimpleControlReqResult_Type()
)
sleRmonSimpleControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleControlReqResult.setStatus("current")


class _SleRmonSimpleControlPortIndex_Type(Integer32):
    """Custom type sleRmonSimpleControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleRmonSimpleControlPortIndex_Type.__name__ = "Integer32"
_SleRmonSimpleControlPortIndex_Object = MibScalar
sleRmonSimpleControlPortIndex = _SleRmonSimpleControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 6),
    _SleRmonSimpleControlPortIndex_Type()
)
sleRmonSimpleControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleControlPortIndex.setStatus("current")


class _SleRmonSimpleControlSampleVariable_Type(Integer32):
    """Custom type sleRmonSimpleControlSampleVariable based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("crcAlignError", 1),
          ("jabber", 2),
          ("oversizePackets", 3),
          ("undersizePackets", 4),
          ("fragments", 5),
          ("dropEvents", 6),
          ("collisions", 7),
          ("ifInDiscards", 8),
          ("ifInErrors", 9),
          ("ifOutDiscards", 10),
          ("ifOutErrors", 11),
          ("ifInPauseFrame", 12),
          ("ifOutPauseFrame", 13),
          ("allTypes", 255))
    )


_SleRmonSimpleControlSampleVariable_Type.__name__ = "Integer32"
_SleRmonSimpleControlSampleVariable_Object = MibScalar
sleRmonSimpleControlSampleVariable = _SleRmonSimpleControlSampleVariable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 7),
    _SleRmonSimpleControlSampleVariable_Type()
)
sleRmonSimpleControlSampleVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleControlSampleVariable.setStatus("current")


class _SleRmonSimpleControlSampleInterval_Type(Integer32):
    """Custom type sleRmonSimpleControlSampleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_SleRmonSimpleControlSampleInterval_Type.__name__ = "Integer32"
_SleRmonSimpleControlSampleInterval_Object = MibScalar
sleRmonSimpleControlSampleInterval = _SleRmonSimpleControlSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 8),
    _SleRmonSimpleControlSampleInterval_Type()
)
sleRmonSimpleControlSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleControlSampleInterval.setStatus("current")
_SleRmonSimpleControlRisingThreshold_Type = Integer32
_SleRmonSimpleControlRisingThreshold_Object = MibScalar
sleRmonSimpleControlRisingThreshold = _SleRmonSimpleControlRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 9),
    _SleRmonSimpleControlRisingThreshold_Type()
)
sleRmonSimpleControlRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleControlRisingThreshold.setStatus("current")
_SleRmonSimpleControlFallingThreshold_Type = Integer32
_SleRmonSimpleControlFallingThreshold_Object = MibScalar
sleRmonSimpleControlFallingThreshold = _SleRmonSimpleControlFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 2, 10),
    _SleRmonSimpleControlFallingThreshold_Type()
)
sleRmonSimpleControlFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleControlFallingThreshold.setStatus("current")
_SleRmonSimpleNotification_ObjectIdentity = ObjectIdentity
sleRmonSimpleNotification = _SleRmonSimpleNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 3)
)
_SleRmonSimpleQueue_ObjectIdentity = ObjectIdentity
sleRmonSimpleQueue = _SleRmonSimpleQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6)
)
_SleRmonSimpleQueueTable_Object = MibTable
sleRmonSimpleQueueTable = _SleRmonSimpleQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1)
)
if mibBuilder.loadTexts:
    sleRmonSimpleQueueTable.setStatus("current")
_SleRmonSimpleQueueEntry_Object = MibTableRow
sleRmonSimpleQueueEntry = _SleRmonSimpleQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1, 1)
)
sleRmonSimpleQueueEntry.setIndexNames(
    (0, "SLE-RMON-MIB", "sleRmonSimpleQueuePortIndex"),
    (0, "SLE-RMON-MIB", "sleRmonSimpleQueueSampleVariable"),
    (0, "SLE-RMON-MIB", "sleRmonSimpleQueueQueueNumber"),
)
if mibBuilder.loadTexts:
    sleRmonSimpleQueueEntry.setStatus("current")


class _SleRmonSimpleQueuePortIndex_Type(Integer32):
    """Custom type sleRmonSimpleQueuePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleRmonSimpleQueuePortIndex_Type.__name__ = "Integer32"
_SleRmonSimpleQueuePortIndex_Object = MibTableColumn
sleRmonSimpleQueuePortIndex = _SleRmonSimpleQueuePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1, 1, 1),
    _SleRmonSimpleQueuePortIndex_Type()
)
sleRmonSimpleQueuePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueuePortIndex.setStatus("current")


class _SleRmonSimpleQueueSampleVariable_Type(Integer32):
    """Custom type sleRmonSimpleQueueSampleVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmitCount", 1),
          ("dropCount", 2))
    )


_SleRmonSimpleQueueSampleVariable_Type.__name__ = "Integer32"
_SleRmonSimpleQueueSampleVariable_Object = MibTableColumn
sleRmonSimpleQueueSampleVariable = _SleRmonSimpleQueueSampleVariable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1, 1, 2),
    _SleRmonSimpleQueueSampleVariable_Type()
)
sleRmonSimpleQueueSampleVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueSampleVariable.setStatus("current")


class _SleRmonSimpleQueueQueueNumber_Type(Integer32):
    """Custom type sleRmonSimpleQueueQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleRmonSimpleQueueQueueNumber_Type.__name__ = "Integer32"
_SleRmonSimpleQueueQueueNumber_Object = MibTableColumn
sleRmonSimpleQueueQueueNumber = _SleRmonSimpleQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1, 1, 3),
    _SleRmonSimpleQueueQueueNumber_Type()
)
sleRmonSimpleQueueQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueQueueNumber.setStatus("current")
_SleRmonSimpleQueueSampleInterval_Type = Integer32
_SleRmonSimpleQueueSampleInterval_Object = MibTableColumn
sleRmonSimpleQueueSampleInterval = _SleRmonSimpleQueueSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1, 1, 4),
    _SleRmonSimpleQueueSampleInterval_Type()
)
sleRmonSimpleQueueSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueSampleInterval.setStatus("current")
_SleRmonSimpleQueueRisingThreshold_Type = Integer32
_SleRmonSimpleQueueRisingThreshold_Object = MibTableColumn
sleRmonSimpleQueueRisingThreshold = _SleRmonSimpleQueueRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1, 1, 5),
    _SleRmonSimpleQueueRisingThreshold_Type()
)
sleRmonSimpleQueueRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueRisingThreshold.setStatus("current")
_SleRmonSimpleQueueFallingThreshold_Type = Integer32
_SleRmonSimpleQueueFallingThreshold_Object = MibTableColumn
sleRmonSimpleQueueFallingThreshold = _SleRmonSimpleQueueFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 1, 1, 6),
    _SleRmonSimpleQueueFallingThreshold_Type()
)
sleRmonSimpleQueueFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueFallingThreshold.setStatus("current")
_SleRmonSimpleQueueControl_ObjectIdentity = ObjectIdentity
sleRmonSimpleQueueControl = _SleRmonSimpleQueueControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2)
)


class _SleRmonSimpleQueueControlRequest_Type(Integer32):
    """Custom type sleRmonSimpleQueueControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRmonSimpleQueue", 1),
          ("delRmonSimpleQueue", 2))
    )


_SleRmonSimpleQueueControlRequest_Type.__name__ = "Integer32"
_SleRmonSimpleQueueControlRequest_Object = MibScalar
sleRmonSimpleQueueControlRequest = _SleRmonSimpleQueueControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 1),
    _SleRmonSimpleQueueControlRequest_Type()
)
sleRmonSimpleQueueControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlRequest.setStatus("current")
_SleRmonSimpleQueueControlStatus_Type = SleControlStatusType
_SleRmonSimpleQueueControlStatus_Object = MibScalar
sleRmonSimpleQueueControlStatus = _SleRmonSimpleQueueControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 2),
    _SleRmonSimpleQueueControlStatus_Type()
)
sleRmonSimpleQueueControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlStatus.setStatus("current")
_SleRmonSimpleQueueControlTimer_Type = Gauge32
_SleRmonSimpleQueueControlTimer_Object = MibScalar
sleRmonSimpleQueueControlTimer = _SleRmonSimpleQueueControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 3),
    _SleRmonSimpleQueueControlTimer_Type()
)
sleRmonSimpleQueueControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlTimer.setStatus("current")
_SleRmonSimpleQueueControlTimeStamp_Type = TimeTicks
_SleRmonSimpleQueueControlTimeStamp_Object = MibScalar
sleRmonSimpleQueueControlTimeStamp = _SleRmonSimpleQueueControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 4),
    _SleRmonSimpleQueueControlTimeStamp_Type()
)
sleRmonSimpleQueueControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlTimeStamp.setStatus("current")
_SleRmonSimpleQueueControlReqResult_Type = SleControlRequestResultType
_SleRmonSimpleQueueControlReqResult_Object = MibScalar
sleRmonSimpleQueueControlReqResult = _SleRmonSimpleQueueControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 5),
    _SleRmonSimpleQueueControlReqResult_Type()
)
sleRmonSimpleQueueControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlReqResult.setStatus("current")


class _SleRmonSimpleQueueControlPortIndex_Type(Integer32):
    """Custom type sleRmonSimpleQueueControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleRmonSimpleQueueControlPortIndex_Type.__name__ = "Integer32"
_SleRmonSimpleQueueControlPortIndex_Object = MibScalar
sleRmonSimpleQueueControlPortIndex = _SleRmonSimpleQueueControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 6),
    _SleRmonSimpleQueueControlPortIndex_Type()
)
sleRmonSimpleQueueControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlPortIndex.setStatus("current")


class _SleRmonSimpleQueueControlSampleVariable_Type(Integer32):
    """Custom type sleRmonSimpleQueueControlSampleVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmitCount", 1),
          ("dropCount", 2))
    )


_SleRmonSimpleQueueControlSampleVariable_Type.__name__ = "Integer32"
_SleRmonSimpleQueueControlSampleVariable_Object = MibScalar
sleRmonSimpleQueueControlSampleVariable = _SleRmonSimpleQueueControlSampleVariable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 7),
    _SleRmonSimpleQueueControlSampleVariable_Type()
)
sleRmonSimpleQueueControlSampleVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlSampleVariable.setStatus("current")


class _SleRmonSimpleQueueControlQueueNumber_Type(Integer32):
    """Custom type sleRmonSimpleQueueControlQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleRmonSimpleQueueControlQueueNumber_Type.__name__ = "Integer32"
_SleRmonSimpleQueueControlQueueNumber_Object = MibScalar
sleRmonSimpleQueueControlQueueNumber = _SleRmonSimpleQueueControlQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 8),
    _SleRmonSimpleQueueControlQueueNumber_Type()
)
sleRmonSimpleQueueControlQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlQueueNumber.setStatus("current")


class _SleRmonSimpleQueueControlSampleInterval_Type(Integer32):
    """Custom type sleRmonSimpleQueueControlSampleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_SleRmonSimpleQueueControlSampleInterval_Type.__name__ = "Integer32"
_SleRmonSimpleQueueControlSampleInterval_Object = MibScalar
sleRmonSimpleQueueControlSampleInterval = _SleRmonSimpleQueueControlSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 9),
    _SleRmonSimpleQueueControlSampleInterval_Type()
)
sleRmonSimpleQueueControlSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlSampleInterval.setStatus("current")
_SleRmonSimpleQueueControlRisingThreshold_Type = Integer32
_SleRmonSimpleQueueControlRisingThreshold_Object = MibScalar
sleRmonSimpleQueueControlRisingThreshold = _SleRmonSimpleQueueControlRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 10),
    _SleRmonSimpleQueueControlRisingThreshold_Type()
)
sleRmonSimpleQueueControlRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlRisingThreshold.setStatus("current")
_SleRmonSimpleQueueControlFallingThreshold_Type = Integer32
_SleRmonSimpleQueueControlFallingThreshold_Object = MibScalar
sleRmonSimpleQueueControlFallingThreshold = _SleRmonSimpleQueueControlFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 2, 11),
    _SleRmonSimpleQueueControlFallingThreshold_Type()
)
sleRmonSimpleQueueControlFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRmonSimpleQueueControlFallingThreshold.setStatus("current")
_SleRmonSimpleQueueNotification_ObjectIdentity = ObjectIdentity
sleRmonSimpleQueueNotification = _SleRmonSimpleQueueNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 3)
)

# Managed Objects groups

sleRmonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 7)
)
sleRmonGroup.setObjects(
      *(("SLE-RMON-MIB", "sleHistoryIndex"),
        ("SLE-RMON-MIB", "sleHistoryDataSource"),
        ("SLE-RMON-MIB", "sleHistoryBucketsRequested"),
        ("SLE-RMON-MIB", "sleHistoryBucketsGranted"),
        ("SLE-RMON-MIB", "sleHistoryInterval"),
        ("SLE-RMON-MIB", "sleHistoryOwner"),
        ("SLE-RMON-MIB", "sleHistoryStatus"),
        ("SLE-RMON-MIB", "sleHistoryControlRequest"),
        ("SLE-RMON-MIB", "sleHistoryControlStatus"),
        ("SLE-RMON-MIB", "sleHistoryControlTimer"),
        ("SLE-RMON-MIB", "sleHistoryControlTimeStamp"),
        ("SLE-RMON-MIB", "sleHistoryControlReqResult"),
        ("SLE-RMON-MIB", "sleHistoryControlIndex"),
        ("SLE-RMON-MIB", "sleHistoryControlDataSource"),
        ("SLE-RMON-MIB", "sleHistoryControlBucketsRequested"),
        ("SLE-RMON-MIB", "sleHistoryControlInterval"),
        ("SLE-RMON-MIB", "sleHistoryControlOwner"),
        ("SLE-RMON-MIB", "sleHistoryControlSts"),
        ("SLE-RMON-MIB", "sleAlarmIndex"),
        ("SLE-RMON-MIB", "sleAlarmInterval"),
        ("SLE-RMON-MIB", "sleAlarmVariable"),
        ("SLE-RMON-MIB", "sleAlarmSampleType"),
        ("SLE-RMON-MIB", "sleAlarmValue"),
        ("SLE-RMON-MIB", "sleAlarmStartupAlarm"),
        ("SLE-RMON-MIB", "sleAlarmRisingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmFallingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmRisingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmFallingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmOwner"),
        ("SLE-RMON-MIB", "sleAlarmStatus"),
        ("SLE-RMON-MIB", "sleAlarmControlRequest"),
        ("SLE-RMON-MIB", "sleAlarmControlStatus"),
        ("SLE-RMON-MIB", "sleAlarmControlTimer"),
        ("SLE-RMON-MIB", "sleAlarmControlTimeStamp"),
        ("SLE-RMON-MIB", "sleAlarmControlReqResult"),
        ("SLE-RMON-MIB", "sleAlarmControlIndex"),
        ("SLE-RMON-MIB", "sleAlarmControlInterval"),
        ("SLE-RMON-MIB", "sleAlarmControlVariable"),
        ("SLE-RMON-MIB", "sleAlarmControlSampleType"),
        ("SLE-RMON-MIB", "sleAlarmControlStartupAlarm"),
        ("SLE-RMON-MIB", "sleAlarmControlRisingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmControlFallingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmControlRisingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmControlFallingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmControlOwner"),
        ("SLE-RMON-MIB", "sleAlarmControlSts"),
        ("SLE-RMON-MIB", "sleEventIndex"),
        ("SLE-RMON-MIB", "sleEventDescription"),
        ("SLE-RMON-MIB", "sleEventType"),
        ("SLE-RMON-MIB", "sleEventCommunity"),
        ("SLE-RMON-MIB", "sleEventLastTimeSent"),
        ("SLE-RMON-MIB", "sleEventOwner"),
        ("SLE-RMON-MIB", "sleEventStatus"),
        ("SLE-RMON-MIB", "sleEventControlRequest"),
        ("SLE-RMON-MIB", "sleEventControlStatus"),
        ("SLE-RMON-MIB", "sleEventControlTimer"),
        ("SLE-RMON-MIB", "sleEventControlTimeStamp"),
        ("SLE-RMON-MIB", "sleEventControlReqResult"),
        ("SLE-RMON-MIB", "sleEventControlIndex"),
        ("SLE-RMON-MIB", "sleEventControlDescription"),
        ("SLE-RMON-MIB", "sleEventControlType"),
        ("SLE-RMON-MIB", "sleEventControlCommunity"),
        ("SLE-RMON-MIB", "sleEventControlOwner"),
        ("SLE-RMON-MIB", "sleEventControlSts"),
        ("SLE-RMON-MIB", "sleEtherStatsIndex"),
        ("SLE-RMON-MIB", "sleEtherStatsDataSource"),
        ("SLE-RMON-MIB", "sleEtherStatsDropEvents"),
        ("SLE-RMON-MIB", "sleEtherStatsOctets"),
        ("SLE-RMON-MIB", "sleEtherStatsPkts"),
        ("SLE-RMON-MIB", "sleEtherStatsBroadcastPkts"),
        ("SLE-RMON-MIB", "sleEtherStatsMulticastPkts"),
        ("SLE-RMON-MIB", "sleEtherStatsCRCAlignErrors"),
        ("SLE-RMON-MIB", "sleEtherStatsUndersizePkts"),
        ("SLE-RMON-MIB", "sleEtherStatsOversizePkts"),
        ("SLE-RMON-MIB", "sleEtherStatsFragments"),
        ("SLE-RMON-MIB", "sleEtherStatsJabbers"),
        ("SLE-RMON-MIB", "sleEtherStatsCollisions"),
        ("SLE-RMON-MIB", "sleEtherStatsPkts64Octets"),
        ("SLE-RMON-MIB", "sleEtherStatsPkts65to127Octets"),
        ("SLE-RMON-MIB", "sleEtherStatsPkts128to255Octets"),
        ("SLE-RMON-MIB", "sleEtherStatsPkts256to511Octets"),
        ("SLE-RMON-MIB", "sleEtherStatsPkts512to1023Octets"),
        ("SLE-RMON-MIB", "sleEtherStatsPkts1024to1518Octets"),
        ("SLE-RMON-MIB", "sleEtherStatsOwner"),
        ("SLE-RMON-MIB", "sleEtherStatsStatus"),
        ("SLE-RMON-MIB", "sleEtherStatsClearedTime"),
        ("SLE-RMON-MIB", "sleRmonSimplePortIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleSampleVariable"),
        ("SLE-RMON-MIB", "sleRmonSimpleSampleInterval"),
        ("SLE-RMON-MIB", "sleRmonSimpleRisingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleFallingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlRequest"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlStatus"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlTimer"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlTimeStamp"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlReqResult"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlPortIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlSampleVariable"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlRisingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlFallingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlSampleInterval"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueuePortIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueQueueNumber"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueSampleVariable"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueSampleInterval"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueRisingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueFallingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlRequest"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlStatus"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlTimer"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlTimeStamp"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlReqResult"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlPortIndex"),
        ("SLE-RMON-MIB", "sleEtherStatsControlRequest"),
        ("SLE-RMON-MIB", "sleEtherStatsControlStatus"),
        ("SLE-RMON-MIB", "sleEtherStatsControlTimer"),
        ("SLE-RMON-MIB", "sleEtherStatsControlTimeStamp"),
        ("SLE-RMON-MIB", "sleEtherStatsControlReqResult"),
        ("SLE-RMON-MIB", "sleEtherStatsControlIfIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlQueueNumber"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlSampleVariable"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlSampleInterval"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlRisingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlFallingThreshold"))
)
if mibBuilder.loadTexts:
    sleRmonGroup.setStatus("current")


# Notification objects

sleHistoryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 3, 1)
)
sleHistoryCreated.setObjects(
      *(("SLE-RMON-MIB", "sleHistoryDataSource"),
        ("SLE-RMON-MIB", "sleHistoryBucketsRequested"),
        ("SLE-RMON-MIB", "sleHistoryInterval"),
        ("SLE-RMON-MIB", "sleHistoryOwner"),
        ("SLE-RMON-MIB", "sleHistoryStatus"),
        ("SLE-RMON-MIB", "sleHistoryControlRequest"),
        ("SLE-RMON-MIB", "sleHistoryControlTimeStamp"),
        ("SLE-RMON-MIB", "sleHistoryControlReqResult"))
)
if mibBuilder.loadTexts:
    sleHistoryCreated.setStatus(
        "current"
    )

sleHistoryDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 3, 2)
)
sleHistoryDestroyed.setObjects(
      *(("SLE-RMON-MIB", "sleHistoryIndex"),
        ("SLE-RMON-MIB", "sleHistoryControlRequest"),
        ("SLE-RMON-MIB", "sleHistoryControlTimeStamp"),
        ("SLE-RMON-MIB", "sleHistoryControlReqResult"))
)
if mibBuilder.loadTexts:
    sleHistoryDestroyed.setStatus(
        "current"
    )

sleHistoryProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 1, 3, 3)
)
sleHistoryProfileChanged.setObjects(
      *(("SLE-RMON-MIB", "sleHistoryDataSource"),
        ("SLE-RMON-MIB", "sleHistoryBucketsRequested"),
        ("SLE-RMON-MIB", "sleHistoryInterval"),
        ("SLE-RMON-MIB", "sleHistoryOwner"),
        ("SLE-RMON-MIB", "sleHistoryStatus"),
        ("SLE-RMON-MIB", "sleHistoryControlRequest"),
        ("SLE-RMON-MIB", "sleHistoryControlTimeStamp"),
        ("SLE-RMON-MIB", "sleHistoryControlReqResult"))
)
if mibBuilder.loadTexts:
    sleHistoryProfileChanged.setStatus(
        "current"
    )

sleAlarmCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 3, 1)
)
sleAlarmCreated.setObjects(
      *(("SLE-RMON-MIB", "sleAlarmInterval"),
        ("SLE-RMON-MIB", "sleAlarmVariable"),
        ("SLE-RMON-MIB", "sleAlarmSampleType"),
        ("SLE-RMON-MIB", "sleAlarmStartupAlarm"),
        ("SLE-RMON-MIB", "sleAlarmRisingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmFallingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmRisingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmFallingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmOwner"),
        ("SLE-RMON-MIB", "sleAlarmStatus"),
        ("SLE-RMON-MIB", "sleAlarmControlRequest"),
        ("SLE-RMON-MIB", "sleAlarmControlTimeStamp"),
        ("SLE-RMON-MIB", "sleAlarmControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAlarmCreated.setStatus(
        "current"
    )

sleAlarmDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 3, 2)
)
sleAlarmDestroyed.setObjects(
      *(("SLE-RMON-MIB", "sleAlarmIndex"),
        ("SLE-RMON-MIB", "sleAlarmControlRequest"),
        ("SLE-RMON-MIB", "sleAlarmControlTimeStamp"),
        ("SLE-RMON-MIB", "sleAlarmControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAlarmDestroyed.setStatus(
        "current"
    )

sleAlarmProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 2, 3, 3)
)
sleAlarmProfileChanged.setObjects(
      *(("SLE-RMON-MIB", "sleAlarmControlRequest"),
        ("SLE-RMON-MIB", "sleAlarmControlTimeStamp"),
        ("SLE-RMON-MIB", "sleAlarmControlReqResult"),
        ("SLE-RMON-MIB", "sleAlarmInterval"),
        ("SLE-RMON-MIB", "sleAlarmVariable"),
        ("SLE-RMON-MIB", "sleAlarmSampleType"),
        ("SLE-RMON-MIB", "sleAlarmStartupAlarm"),
        ("SLE-RMON-MIB", "sleAlarmRisingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmFallingThreshold"),
        ("SLE-RMON-MIB", "sleAlarmRisingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmFallingEventIndex"),
        ("SLE-RMON-MIB", "sleAlarmOwner"),
        ("SLE-RMON-MIB", "sleAlarmStatus"))
)
if mibBuilder.loadTexts:
    sleAlarmProfileChanged.setStatus(
        "current"
    )

sleEventCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 3, 1)
)
sleEventCreated.setObjects(
      *(("SLE-RMON-MIB", "sleEventDescription"),
        ("SLE-RMON-MIB", "sleEventType"),
        ("SLE-RMON-MIB", "sleEventCommunity"),
        ("SLE-RMON-MIB", "sleEventOwner"),
        ("SLE-RMON-MIB", "sleEventStatus"),
        ("SLE-RMON-MIB", "sleEventControlRequest"),
        ("SLE-RMON-MIB", "sleEventControlTimeStamp"),
        ("SLE-RMON-MIB", "sleEventControlReqResult"))
)
if mibBuilder.loadTexts:
    sleEventCreated.setStatus(
        "current"
    )

sleEventDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 3, 2)
)
sleEventDestroyed.setObjects(
      *(("SLE-RMON-MIB", "sleEventIndex"),
        ("SLE-RMON-MIB", "sleEventControlRequest"),
        ("SLE-RMON-MIB", "sleEventControlTimeStamp"),
        ("SLE-RMON-MIB", "sleEventControlReqResult"))
)
if mibBuilder.loadTexts:
    sleEventDestroyed.setStatus(
        "current"
    )

sleEventProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 3, 3, 3)
)
sleEventProfileChanged.setObjects(
      *(("SLE-RMON-MIB", "sleEventDescription"),
        ("SLE-RMON-MIB", "sleEventType"),
        ("SLE-RMON-MIB", "sleEventCommunity"),
        ("SLE-RMON-MIB", "sleEventOwner"),
        ("SLE-RMON-MIB", "sleEventStatus"),
        ("SLE-RMON-MIB", "sleEventControlRequest"),
        ("SLE-RMON-MIB", "sleEventControlTimeStamp"),
        ("SLE-RMON-MIB", "sleEventControlReqResult"))
)
if mibBuilder.loadTexts:
    sleEventProfileChanged.setStatus(
        "current"
    )

sleRmonSimpleCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 3, 1)
)
sleRmonSimpleCreated.setObjects(
      *(("SLE-RMON-MIB", "sleRmonSimpleControlRequest"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlTimeStamp"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlReqResult"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlPortIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlSampleVariable"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlSampleInterval"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlRisingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlFallingThreshold"))
)
if mibBuilder.loadTexts:
    sleRmonSimpleCreated.setStatus(
        "current"
    )

sleRmonSimpleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 5, 3, 2)
)
sleRmonSimpleDeleted.setObjects(
      *(("SLE-RMON-MIB", "sleRmonSimpleControlRequest"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlTimeStamp"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlReqResult"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlPortIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleControlSampleVariable"))
)
if mibBuilder.loadTexts:
    sleRmonSimpleDeleted.setStatus(
        "current"
    )

sleRmonSimpleQueueCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 3, 1)
)
sleRmonSimpleQueueCreated.setObjects(
      *(("SLE-RMON-MIB", "sleRmonSimpleQueueControlRequest"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlTimeStamp"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlReqResult"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlPortIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlSampleVariable"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlQueueNumber"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlSampleInterval"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlRisingThreshold"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlFallingThreshold"))
)
if mibBuilder.loadTexts:
    sleRmonSimpleQueueCreated.setStatus(
        "current"
    )

sleRmonSimpleQueueDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 6, 3, 2)
)
sleRmonSimpleQueueDeleted.setObjects(
      *(("SLE-RMON-MIB", "sleRmonSimpleQueueControlRequest"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlTimeStamp"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlReqResult"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlPortIndex"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlSampleVariable"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueControlQueueNumber"))
)
if mibBuilder.loadTexts:
    sleRmonSimpleQueueDeleted.setStatus(
        "current"
    )


# Notifications groups

sleRmonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 9, 8)
)
sleRmonNotificationGroup.setObjects(
      *(("SLE-RMON-MIB", "sleHistoryCreated"),
        ("SLE-RMON-MIB", "sleHistoryDestroyed"),
        ("SLE-RMON-MIB", "sleHistoryProfileChanged"),
        ("SLE-RMON-MIB", "sleAlarmCreated"),
        ("SLE-RMON-MIB", "sleAlarmDestroyed"),
        ("SLE-RMON-MIB", "sleAlarmProfileChanged"),
        ("SLE-RMON-MIB", "sleEventCreated"),
        ("SLE-RMON-MIB", "sleEventDestroyed"),
        ("SLE-RMON-MIB", "sleEventProfileChanged"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueCreated"),
        ("SLE-RMON-MIB", "sleRmonSimpleQueueDeleted"),
        ("SLE-RMON-MIB", "sleRmonSimpleDeleted"),
        ("SLE-RMON-MIB", "sleRmonSimpleCreated"))
)
if mibBuilder.loadTexts:
    sleRmonNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-RMON-MIB",
    **{"OwnerString": OwnerString,
       "SleEntryStatus": SleEntryStatus,
       "sleRmon": sleRmon,
       "sleHistory": sleHistory,
       "sleHistoryTable": sleHistoryTable,
       "sleHistoryEntry": sleHistoryEntry,
       "sleHistoryIndex": sleHistoryIndex,
       "sleHistoryDataSource": sleHistoryDataSource,
       "sleHistoryBucketsRequested": sleHistoryBucketsRequested,
       "sleHistoryBucketsGranted": sleHistoryBucketsGranted,
       "sleHistoryInterval": sleHistoryInterval,
       "sleHistoryOwner": sleHistoryOwner,
       "sleHistoryStatus": sleHistoryStatus,
       "sleHistoryControl": sleHistoryControl,
       "sleHistoryControlRequest": sleHistoryControlRequest,
       "sleHistoryControlStatus": sleHistoryControlStatus,
       "sleHistoryControlTimer": sleHistoryControlTimer,
       "sleHistoryControlTimeStamp": sleHistoryControlTimeStamp,
       "sleHistoryControlReqResult": sleHistoryControlReqResult,
       "sleHistoryControlIndex": sleHistoryControlIndex,
       "sleHistoryControlDataSource": sleHistoryControlDataSource,
       "sleHistoryControlBucketsRequested": sleHistoryControlBucketsRequested,
       "sleHistoryControlInterval": sleHistoryControlInterval,
       "sleHistoryControlOwner": sleHistoryControlOwner,
       "sleHistoryControlSts": sleHistoryControlSts,
       "sleHistoryNotification": sleHistoryNotification,
       "sleHistoryCreated": sleHistoryCreated,
       "sleHistoryDestroyed": sleHistoryDestroyed,
       "sleHistoryProfileChanged": sleHistoryProfileChanged,
       "sleAlarm": sleAlarm,
       "sleAlarmTable": sleAlarmTable,
       "sleAlarmEntry": sleAlarmEntry,
       "sleAlarmIndex": sleAlarmIndex,
       "sleAlarmInterval": sleAlarmInterval,
       "sleAlarmVariable": sleAlarmVariable,
       "sleAlarmSampleType": sleAlarmSampleType,
       "sleAlarmValue": sleAlarmValue,
       "sleAlarmStartupAlarm": sleAlarmStartupAlarm,
       "sleAlarmRisingThreshold": sleAlarmRisingThreshold,
       "sleAlarmFallingThreshold": sleAlarmFallingThreshold,
       "sleAlarmRisingEventIndex": sleAlarmRisingEventIndex,
       "sleAlarmFallingEventIndex": sleAlarmFallingEventIndex,
       "sleAlarmOwner": sleAlarmOwner,
       "sleAlarmStatus": sleAlarmStatus,
       "sleAlarmControl": sleAlarmControl,
       "sleAlarmControlRequest": sleAlarmControlRequest,
       "sleAlarmControlStatus": sleAlarmControlStatus,
       "sleAlarmControlTimer": sleAlarmControlTimer,
       "sleAlarmControlTimeStamp": sleAlarmControlTimeStamp,
       "sleAlarmControlReqResult": sleAlarmControlReqResult,
       "sleAlarmControlIndex": sleAlarmControlIndex,
       "sleAlarmControlInterval": sleAlarmControlInterval,
       "sleAlarmControlVariable": sleAlarmControlVariable,
       "sleAlarmControlSampleType": sleAlarmControlSampleType,
       "sleAlarmControlStartupAlarm": sleAlarmControlStartupAlarm,
       "sleAlarmControlRisingThreshold": sleAlarmControlRisingThreshold,
       "sleAlarmControlFallingThreshold": sleAlarmControlFallingThreshold,
       "sleAlarmControlRisingEventIndex": sleAlarmControlRisingEventIndex,
       "sleAlarmControlFallingEventIndex": sleAlarmControlFallingEventIndex,
       "sleAlarmControlOwner": sleAlarmControlOwner,
       "sleAlarmControlSts": sleAlarmControlSts,
       "sleAlarmNotification": sleAlarmNotification,
       "sleAlarmCreated": sleAlarmCreated,
       "sleAlarmDestroyed": sleAlarmDestroyed,
       "sleAlarmProfileChanged": sleAlarmProfileChanged,
       "sleEvent": sleEvent,
       "sleEventTable": sleEventTable,
       "sleEventEntry": sleEventEntry,
       "sleEventIndex": sleEventIndex,
       "sleEventDescription": sleEventDescription,
       "sleEventType": sleEventType,
       "sleEventCommunity": sleEventCommunity,
       "sleEventLastTimeSent": sleEventLastTimeSent,
       "sleEventOwner": sleEventOwner,
       "sleEventStatus": sleEventStatus,
       "sleEventControl": sleEventControl,
       "sleEventControlRequest": sleEventControlRequest,
       "sleEventControlStatus": sleEventControlStatus,
       "sleEventControlTimer": sleEventControlTimer,
       "sleEventControlTimeStamp": sleEventControlTimeStamp,
       "sleEventControlReqResult": sleEventControlReqResult,
       "sleEventControlIndex": sleEventControlIndex,
       "sleEventControlDescription": sleEventControlDescription,
       "sleEventControlType": sleEventControlType,
       "sleEventControlCommunity": sleEventControlCommunity,
       "sleEventControlOwner": sleEventControlOwner,
       "sleEventControlSts": sleEventControlSts,
       "sleEventNotification": sleEventNotification,
       "sleEventCreated": sleEventCreated,
       "sleEventDestroyed": sleEventDestroyed,
       "sleEventProfileChanged": sleEventProfileChanged,
       "sleStatistics": sleStatistics,
       "sleEtherStats": sleEtherStats,
       "sleEtherStatsTable": sleEtherStatsTable,
       "sleEtherStatsEntry": sleEtherStatsEntry,
       "sleEtherStatsIndex": sleEtherStatsIndex,
       "sleEtherStatsDataSource": sleEtherStatsDataSource,
       "sleEtherStatsDropEvents": sleEtherStatsDropEvents,
       "sleEtherStatsOctets": sleEtherStatsOctets,
       "sleEtherStatsPkts": sleEtherStatsPkts,
       "sleEtherStatsBroadcastPkts": sleEtherStatsBroadcastPkts,
       "sleEtherStatsMulticastPkts": sleEtherStatsMulticastPkts,
       "sleEtherStatsCRCAlignErrors": sleEtherStatsCRCAlignErrors,
       "sleEtherStatsUndersizePkts": sleEtherStatsUndersizePkts,
       "sleEtherStatsOversizePkts": sleEtherStatsOversizePkts,
       "sleEtherStatsFragments": sleEtherStatsFragments,
       "sleEtherStatsJabbers": sleEtherStatsJabbers,
       "sleEtherStatsCollisions": sleEtherStatsCollisions,
       "sleEtherStatsPkts64Octets": sleEtherStatsPkts64Octets,
       "sleEtherStatsPkts65to127Octets": sleEtherStatsPkts65to127Octets,
       "sleEtherStatsPkts128to255Octets": sleEtherStatsPkts128to255Octets,
       "sleEtherStatsPkts256to511Octets": sleEtherStatsPkts256to511Octets,
       "sleEtherStatsPkts512to1023Octets": sleEtherStatsPkts512to1023Octets,
       "sleEtherStatsPkts1024to1518Octets": sleEtherStatsPkts1024to1518Octets,
       "sleEtherStatsOwner": sleEtherStatsOwner,
       "sleEtherStatsStatus": sleEtherStatsStatus,
       "sleEtherStatsClearedTime": sleEtherStatsClearedTime,
       "sleEtherStatsControl": sleEtherStatsControl,
       "sleEtherStatsControlRequest": sleEtherStatsControlRequest,
       "sleEtherStatsControlStatus": sleEtherStatsControlStatus,
       "sleEtherStatsControlTimer": sleEtherStatsControlTimer,
       "sleEtherStatsControlTimeStamp": sleEtherStatsControlTimeStamp,
       "sleEtherStatsControlReqResult": sleEtherStatsControlReqResult,
       "sleEtherStatsControlIfIndex": sleEtherStatsControlIfIndex,
       "sleRmonSimple": sleRmonSimple,
       "sleRmonSimpleTable": sleRmonSimpleTable,
       "sleRmonSimpleEntry": sleRmonSimpleEntry,
       "sleRmonSimplePortIndex": sleRmonSimplePortIndex,
       "sleRmonSimpleSampleVariable": sleRmonSimpleSampleVariable,
       "sleRmonSimpleSampleInterval": sleRmonSimpleSampleInterval,
       "sleRmonSimpleRisingThreshold": sleRmonSimpleRisingThreshold,
       "sleRmonSimpleFallingThreshold": sleRmonSimpleFallingThreshold,
       "sleRmonSimpleControl": sleRmonSimpleControl,
       "sleRmonSimpleControlRequest": sleRmonSimpleControlRequest,
       "sleRmonSimpleControlStatus": sleRmonSimpleControlStatus,
       "sleRmonSimpleControlTimer": sleRmonSimpleControlTimer,
       "sleRmonSimpleControlTimeStamp": sleRmonSimpleControlTimeStamp,
       "sleRmonSimpleControlReqResult": sleRmonSimpleControlReqResult,
       "sleRmonSimpleControlPortIndex": sleRmonSimpleControlPortIndex,
       "sleRmonSimpleControlSampleVariable": sleRmonSimpleControlSampleVariable,
       "sleRmonSimpleControlSampleInterval": sleRmonSimpleControlSampleInterval,
       "sleRmonSimpleControlRisingThreshold": sleRmonSimpleControlRisingThreshold,
       "sleRmonSimpleControlFallingThreshold": sleRmonSimpleControlFallingThreshold,
       "sleRmonSimpleNotification": sleRmonSimpleNotification,
       "sleRmonSimpleCreated": sleRmonSimpleCreated,
       "sleRmonSimpleDeleted": sleRmonSimpleDeleted,
       "sleRmonSimpleQueue": sleRmonSimpleQueue,
       "sleRmonSimpleQueueTable": sleRmonSimpleQueueTable,
       "sleRmonSimpleQueueEntry": sleRmonSimpleQueueEntry,
       "sleRmonSimpleQueuePortIndex": sleRmonSimpleQueuePortIndex,
       "sleRmonSimpleQueueSampleVariable": sleRmonSimpleQueueSampleVariable,
       "sleRmonSimpleQueueQueueNumber": sleRmonSimpleQueueQueueNumber,
       "sleRmonSimpleQueueSampleInterval": sleRmonSimpleQueueSampleInterval,
       "sleRmonSimpleQueueRisingThreshold": sleRmonSimpleQueueRisingThreshold,
       "sleRmonSimpleQueueFallingThreshold": sleRmonSimpleQueueFallingThreshold,
       "sleRmonSimpleQueueControl": sleRmonSimpleQueueControl,
       "sleRmonSimpleQueueControlRequest": sleRmonSimpleQueueControlRequest,
       "sleRmonSimpleQueueControlStatus": sleRmonSimpleQueueControlStatus,
       "sleRmonSimpleQueueControlTimer": sleRmonSimpleQueueControlTimer,
       "sleRmonSimpleQueueControlTimeStamp": sleRmonSimpleQueueControlTimeStamp,
       "sleRmonSimpleQueueControlReqResult": sleRmonSimpleQueueControlReqResult,
       "sleRmonSimpleQueueControlPortIndex": sleRmonSimpleQueueControlPortIndex,
       "sleRmonSimpleQueueControlSampleVariable": sleRmonSimpleQueueControlSampleVariable,
       "sleRmonSimpleQueueControlQueueNumber": sleRmonSimpleQueueControlQueueNumber,
       "sleRmonSimpleQueueControlSampleInterval": sleRmonSimpleQueueControlSampleInterval,
       "sleRmonSimpleQueueControlRisingThreshold": sleRmonSimpleQueueControlRisingThreshold,
       "sleRmonSimpleQueueControlFallingThreshold": sleRmonSimpleQueueControlFallingThreshold,
       "sleRmonSimpleQueueNotification": sleRmonSimpleQueueNotification,
       "sleRmonSimpleQueueCreated": sleRmonSimpleQueueCreated,
       "sleRmonSimpleQueueDeleted": sleRmonSimpleQueueDeleted,
       "sleRmonGroup": sleRmonGroup,
       "sleRmonNotificationGroup": sleRmonNotificationGroup}
)
