# SNMP MIB module (F3-SYNCJACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-SYNCJACK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:56 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmBinAction,
 CmPmIntervalType,
 IpPriorityMapMode,
 IpVersion,
 OperationalState,
 PerfCounter32,
 PerfCounter64,
 SchedActivityStatus,
 ScheduleType,
 SecondaryState) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "IpPriorityMapMode",
    "IpVersion",
    "OperationalState",
    "PerfCounter32",
    "PerfCounter64",
    "SchedActivityStatus",
    "ScheduleType",
    "SecondaryState")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(ScaledNanoseconds,) = mibBuilder.importSymbols(
    "F3-PTP-MIB",
    "ScaledNanoseconds")

(SSMQualityLevel,) = mibBuilder.importSymbols(
    "F3-SYNC-MIB",
    "SSMQualityLevel")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3SyncJMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22)
)
if mibBuilder.loadTexts:
    f3SyncJMIB.setRevisions(
        ("2012-05-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SyncJackTestState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("waiting", 1),
          ("running", 2),
          ("completed", 3),
          ("failed", 4),
          ("suspended", 5),
          ("notscheduled", 6))
    )



class MTIEMaskType(TextualConvention, Integer32):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("g823-e1-ssu", 1),
          ("g823-e1-sec", 2),
          ("g823-e1-traffic", 3),
          ("g823-pdh", 4),
          ("g824-t1-sync", 5),
          ("g824-t1-traffic", 6),
          ("g8261-e1-case1", 7),
          ("g8261-t1-case1", 8),
          ("g8261-e1-case2", 9),
          ("g8261-eec-opt1", 10),
          ("g8263-const-temp", 11),
          ("g8272-prtc", 12),
          ("g8261-1", 13),
          ("g8262-eec-opt1", 14),
          ("g8262-eec-opt1-temp", 15),
          ("g8262-eec-opt2", 16),
          ("g8262-eec-opt1-tolerrance", 17),
          ("g8263-var-temp", 18),
          ("g8273-2", 19),
          ("g8271-1", 20),
          ("user-defined", 21))
    )



class TIESourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phase", 1),
          ("frequency", 2))
    )



class TIEMeasurementRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("meas-10per1sec", 1),
          ("meas-1per1sec", 2),
          ("meas-1per2sec", 3))
    )



class PTPMeasurementDirection(TextualConvention, Integer32):
    status = "current"
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
        *(("master2slave", 1),
          ("slave2master", 2),
          ("twoways", 3),
          ("master2slave-t4", 4))
    )



class MeasurementType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phase", 1),
          ("frequency", 2))
    )



class FFOObserWindow(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("window-100s", 1),
          ("window-200s", 2),
          ("window-500s", 3),
          ("window-1000s", 4),
          ("window-2000s", 5),
          ("window-5000s", 6),
          ("window-10000s", 7))
    )



# MIB Managed Objects in the order of their OIDs

_F3SyncJConfigObjects_ObjectIdentity = ObjectIdentity
f3SyncJConfigObjects = _F3SyncJConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1)
)
_F3SyncJClockProbeTable_Object = MibTable
f3SyncJClockProbeTable = _F3SyncJClockProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1)
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeTable.setStatus("current")
_F3SyncJClockProbeEntry_Object = MibTableRow
f3SyncJClockProbeEntry = _F3SyncJClockProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1)
)
f3SyncJClockProbeEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeEntry.setStatus("current")
_F3SyncJClockProbeIndex_Type = Integer32
_F3SyncJClockProbeIndex_Object = MibTableColumn
f3SyncJClockProbeIndex = _F3SyncJClockProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 1),
    _F3SyncJClockProbeIndex_Type()
)
f3SyncJClockProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJClockProbeIndex.setStatus("current")


class _F3SyncJClockProbeName_Type(DisplayString):
    """Custom type f3SyncJClockProbeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_F3SyncJClockProbeName_Type.__name__ = "DisplayString"
_F3SyncJClockProbeName_Object = MibTableColumn
f3SyncJClockProbeName = _F3SyncJClockProbeName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 2),
    _F3SyncJClockProbeName_Type()
)
f3SyncJClockProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJClockProbeName.setStatus("current")
_F3SyncJClockProbeSource_Type = VariablePointer
_F3SyncJClockProbeSource_Object = MibTableColumn
f3SyncJClockProbeSource = _F3SyncJClockProbeSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 3),
    _F3SyncJClockProbeSource_Type()
)
f3SyncJClockProbeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeSource.setStatus("current")
_F3SyncJClockProbeReference_Type = VariablePointer
_F3SyncJClockProbeReference_Object = MibTableColumn
f3SyncJClockProbeReference = _F3SyncJClockProbeReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 4),
    _F3SyncJClockProbeReference_Type()
)
f3SyncJClockProbeReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeReference.setStatus("current")
_F3SyncJClockProbeExpectedQL_Type = SSMQualityLevel
_F3SyncJClockProbeExpectedQL_Object = MibTableColumn
f3SyncJClockProbeExpectedQL = _F3SyncJClockProbeExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 5),
    _F3SyncJClockProbeExpectedQL_Type()
)
f3SyncJClockProbeExpectedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeExpectedQL.setStatus("current")
_F3SyncJClockProbeSourceType_Type = TIESourceType
_F3SyncJClockProbeSourceType_Object = MibTableColumn
f3SyncJClockProbeSourceType = _F3SyncJClockProbeSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 6),
    _F3SyncJClockProbeSourceType_Type()
)
f3SyncJClockProbeSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJClockProbeSourceType.setStatus("current")
_F3SyncJClockProbeMeasurementRate_Type = TIEMeasurementRate
_F3SyncJClockProbeMeasurementRate_Object = MibTableColumn
f3SyncJClockProbeMeasurementRate = _F3SyncJClockProbeMeasurementRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 7),
    _F3SyncJClockProbeMeasurementRate_Type()
)
f3SyncJClockProbeMeasurementRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMeasurementRate.setStatus("current")
_F3SyncJClockProbeMTIEMaskType_Type = MTIEMaskType
_F3SyncJClockProbeMTIEMaskType_Object = MibTableColumn
f3SyncJClockProbeMTIEMaskType = _F3SyncJClockProbeMTIEMaskType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 8),
    _F3SyncJClockProbeMTIEMaskType_Type()
)
f3SyncJClockProbeMTIEMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEMaskType.setStatus("current")
_F3SyncJClockProbeMTIEMaskMargin_Type = Unsigned32
_F3SyncJClockProbeMTIEMaskMargin_Object = MibTableColumn
f3SyncJClockProbeMTIEMaskMargin = _F3SyncJClockProbeMTIEMaskMargin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 9),
    _F3SyncJClockProbeMTIEMaskMargin_Type()
)
f3SyncJClockProbeMTIEMaskMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEMaskMargin.setStatus("current")
_F3SyncJClockProbeScheduler_Type = VariablePointer
_F3SyncJClockProbeScheduler_Object = MibTableColumn
f3SyncJClockProbeScheduler = _F3SyncJClockProbeScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 10),
    _F3SyncJClockProbeScheduler_Type()
)
f3SyncJClockProbeScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeScheduler.setStatus("current")
_F3SyncJClockProbeTestState_Type = SyncJackTestState
_F3SyncJClockProbeTestState_Object = MibTableColumn
f3SyncJClockProbeTestState = _F3SyncJClockProbeTestState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 11),
    _F3SyncJClockProbeTestState_Type()
)
f3SyncJClockProbeTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeTestState.setStatus("current")
_F3SyncJClockProbeLastTIEResult_Type = Integer32
_F3SyncJClockProbeLastTIEResult_Object = MibTableColumn
f3SyncJClockProbeLastTIEResult = _F3SyncJClockProbeLastTIEResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 12),
    _F3SyncJClockProbeLastTIEResult_Type()
)
f3SyncJClockProbeLastTIEResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeLastTIEResult.setStatus("current")
_F3SyncJClockProbeLastTIEResultTime_Type = DateAndTime
_F3SyncJClockProbeLastTIEResultTime_Object = MibTableColumn
f3SyncJClockProbeLastTIEResultTime = _F3SyncJClockProbeLastTIEResultTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 13),
    _F3SyncJClockProbeLastTIEResultTime_Type()
)
f3SyncJClockProbeLastTIEResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeLastTIEResultTime.setStatus("current")
_F3SyncJClockProbeSourceFailure_Type = TruthValue
_F3SyncJClockProbeSourceFailure_Object = MibTableColumn
f3SyncJClockProbeSourceFailure = _F3SyncJClockProbeSourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 14),
    _F3SyncJClockProbeSourceFailure_Type()
)
f3SyncJClockProbeSourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeSourceFailure.setStatus("current")
_F3SyncJClockProbeReferenceFailure_Type = TruthValue
_F3SyncJClockProbeReferenceFailure_Object = MibTableColumn
f3SyncJClockProbeReferenceFailure = _F3SyncJClockProbeReferenceFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 15),
    _F3SyncJClockProbeReferenceFailure_Type()
)
f3SyncJClockProbeReferenceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeReferenceFailure.setStatus("current")
_F3SyncJClockProbeActualTestStartTime_Type = DateAndTime
_F3SyncJClockProbeActualTestStartTime_Object = MibTableColumn
f3SyncJClockProbeActualTestStartTime = _F3SyncJClockProbeActualTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 16),
    _F3SyncJClockProbeActualTestStartTime_Type()
)
f3SyncJClockProbeActualTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeActualTestStartTime.setStatus("current")
_F3SyncJClockProbeActualTestDuration_Type = Unsigned32
_F3SyncJClockProbeActualTestDuration_Object = MibTableColumn
f3SyncJClockProbeActualTestDuration = _F3SyncJClockProbeActualTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 17),
    _F3SyncJClockProbeActualTestDuration_Type()
)
f3SyncJClockProbeActualTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeActualTestDuration.setStatus("current")
_F3SyncJClockProbeMTIEMaskCrossedTime_Type = DateAndTime
_F3SyncJClockProbeMTIEMaskCrossedTime_Object = MibTableColumn
f3SyncJClockProbeMTIEMaskCrossedTime = _F3SyncJClockProbeMTIEMaskCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 18),
    _F3SyncJClockProbeMTIEMaskCrossedTime_Type()
)
f3SyncJClockProbeMTIEMaskCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEMaskCrossedTime.setStatus("current")
_F3SyncJClockProbeMTIEMaskMarginCrossedTime_Type = DateAndTime
_F3SyncJClockProbeMTIEMaskMarginCrossedTime_Object = MibTableColumn
f3SyncJClockProbeMTIEMaskMarginCrossedTime = _F3SyncJClockProbeMTIEMaskMarginCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 19),
    _F3SyncJClockProbeMTIEMaskMarginCrossedTime_Type()
)
f3SyncJClockProbeMTIEMaskMarginCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEMaskMarginCrossedTime.setStatus("current")
_F3SyncJClockProbeStatusMTIEMaskFailed_Type = TruthValue
_F3SyncJClockProbeStatusMTIEMaskFailed_Object = MibTableColumn
f3SyncJClockProbeStatusMTIEMaskFailed = _F3SyncJClockProbeStatusMTIEMaskFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 20),
    _F3SyncJClockProbeStatusMTIEMaskFailed_Type()
)
f3SyncJClockProbeStatusMTIEMaskFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatusMTIEMaskFailed.setStatus("current")
_F3SyncJClockProbeStatusMTIEMarginFailed_Type = TruthValue
_F3SyncJClockProbeStatusMTIEMarginFailed_Object = MibTableColumn
f3SyncJClockProbeStatusMTIEMarginFailed = _F3SyncJClockProbeStatusMTIEMarginFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 21),
    _F3SyncJClockProbeStatusMTIEMarginFailed_Type()
)
f3SyncJClockProbeStatusMTIEMarginFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatusMTIEMarginFailed.setStatus("current")
_F3SyncJClockProbeStorageType_Type = StorageType
_F3SyncJClockProbeStorageType_Object = MibTableColumn
f3SyncJClockProbeStorageType = _F3SyncJClockProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 22),
    _F3SyncJClockProbeStorageType_Type()
)
f3SyncJClockProbeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStorageType.setStatus("current")
_F3SyncJClockProbeRowStatus_Type = RowStatus
_F3SyncJClockProbeRowStatus_Object = MibTableColumn
f3SyncJClockProbeRowStatus = _F3SyncJClockProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 23),
    _F3SyncJClockProbeRowStatus_Type()
)
f3SyncJClockProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJClockProbeRowStatus.setStatus("current")
_F3SyncJClockProbeFfoTarget_Type = Integer32
_F3SyncJClockProbeFfoTarget_Object = MibTableColumn
f3SyncJClockProbeFfoTarget = _F3SyncJClockProbeFfoTarget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 24),
    _F3SyncJClockProbeFfoTarget_Type()
)
f3SyncJClockProbeFfoTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeFfoTarget.setStatus("current")
_F3SyncJClockProbeFfoObserWindow_Type = FFOObserWindow
_F3SyncJClockProbeFfoObserWindow_Object = MibTableColumn
f3SyncJClockProbeFfoObserWindow = _F3SyncJClockProbeFfoObserWindow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 25),
    _F3SyncJClockProbeFfoObserWindow_Type()
)
f3SyncJClockProbeFfoObserWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeFfoObserWindow.setStatus("current")
_F3SyncJClockProbeLastFFOResult_Type = Integer32
_F3SyncJClockProbeLastFFOResult_Object = MibTableColumn
f3SyncJClockProbeLastFFOResult = _F3SyncJClockProbeLastFFOResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 26),
    _F3SyncJClockProbeLastFFOResult_Type()
)
f3SyncJClockProbeLastFFOResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeLastFFOResult.setStatus("current")
_F3SyncJClockProbeTimeOfLastFFOResult_Type = DateAndTime
_F3SyncJClockProbeTimeOfLastFFOResult_Object = MibTableColumn
f3SyncJClockProbeTimeOfLastFFOResult = _F3SyncJClockProbeTimeOfLastFFOResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 27),
    _F3SyncJClockProbeTimeOfLastFFOResult_Type()
)
f3SyncJClockProbeTimeOfLastFFOResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeTimeOfLastFFOResult.setStatus("current")
_F3SyncJClockProbeRawDataCollectionEnabled_Type = TruthValue
_F3SyncJClockProbeRawDataCollectionEnabled_Object = MibTableColumn
f3SyncJClockProbeRawDataCollectionEnabled = _F3SyncJClockProbeRawDataCollectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 28),
    _F3SyncJClockProbeRawDataCollectionEnabled_Type()
)
f3SyncJClockProbeRawDataCollectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeRawDataCollectionEnabled.setStatus("current")
_F3SyncJClockProbeTeAlertThreshold_Type = Integer32
_F3SyncJClockProbeTeAlertThreshold_Object = MibTableColumn
f3SyncJClockProbeTeAlertThreshold = _F3SyncJClockProbeTeAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 29),
    _F3SyncJClockProbeTeAlertThreshold_Type()
)
f3SyncJClockProbeTeAlertThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeTeAlertThreshold.setStatus("deprecated")
_F3SyncJClockProbeTeAlertClearThreshold_Type = Integer32
_F3SyncJClockProbeTeAlertClearThreshold_Object = MibTableColumn
f3SyncJClockProbeTeAlertClearThreshold = _F3SyncJClockProbeTeAlertClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 30),
    _F3SyncJClockProbeTeAlertClearThreshold_Type()
)
f3SyncJClockProbeTeAlertClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeTeAlertClearThreshold.setStatus("deprecated")
_F3SyncJClockProbeLastTEAlertTime_Type = DateAndTime
_F3SyncJClockProbeLastTEAlertTime_Object = MibTableColumn
f3SyncJClockProbeLastTEAlertTime = _F3SyncJClockProbeLastTEAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 31),
    _F3SyncJClockProbeLastTEAlertTime_Type()
)
f3SyncJClockProbeLastTEAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeLastTEAlertTime.setStatus("deprecated")
_F3SyncJClockProbeLastTEAlertClearTime_Type = DateAndTime
_F3SyncJClockProbeLastTEAlertClearTime_Object = MibTableColumn
f3SyncJClockProbeLastTEAlertClearTime = _F3SyncJClockProbeLastTEAlertClearTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 32),
    _F3SyncJClockProbeLastTEAlertClearTime_Type()
)
f3SyncJClockProbeLastTEAlertClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeLastTEAlertClearTime.setStatus("deprecated")
_F3SyncJClockProbeRunningFailedCount_Type = Integer32
_F3SyncJClockProbeRunningFailedCount_Object = MibTableColumn
f3SyncJClockProbeRunningFailedCount = _F3SyncJClockProbeRunningFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 33),
    _F3SyncJClockProbeRunningFailedCount_Type()
)
f3SyncJClockProbeRunningFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeRunningFailedCount.setStatus("current")
_F3SyncJClockProbeMeasurementType_Type = MeasurementType
_F3SyncJClockProbeMeasurementType_Object = MibTableColumn
f3SyncJClockProbeMeasurementType = _F3SyncJClockProbeMeasurementType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 34),
    _F3SyncJClockProbeMeasurementType_Type()
)
f3SyncJClockProbeMeasurementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMeasurementType.setStatus("current")
_F3SyncJClockProbeConstTEThreshold_Type = Unsigned32
_F3SyncJClockProbeConstTEThreshold_Object = MibTableColumn
f3SyncJClockProbeConstTEThreshold = _F3SyncJClockProbeConstTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 35),
    _F3SyncJClockProbeConstTEThreshold_Type()
)
f3SyncJClockProbeConstTEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeConstTEThreshold.setStatus("current")
_F3SyncJClockProbeConstTEClrThreshold_Type = Unsigned32
_F3SyncJClockProbeConstTEClrThreshold_Object = MibTableColumn
f3SyncJClockProbeConstTEClrThreshold = _F3SyncJClockProbeConstTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 36),
    _F3SyncJClockProbeConstTEClrThreshold_Type()
)
f3SyncJClockProbeConstTEClrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeConstTEClrThreshold.setStatus("current")
_F3SyncJClockProbeConstTEWindow_Type = Unsigned32
_F3SyncJClockProbeConstTEWindow_Object = MibTableColumn
f3SyncJClockProbeConstTEWindow = _F3SyncJClockProbeConstTEWindow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 37),
    _F3SyncJClockProbeConstTEWindow_Type()
)
f3SyncJClockProbeConstTEWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeConstTEWindow.setStatus("current")
_F3SyncJClockProbeMaxTETotAlarmTime_Type = Unsigned32
_F3SyncJClockProbeMaxTETotAlarmTime_Object = MibTableColumn
f3SyncJClockProbeMaxTETotAlarmTime = _F3SyncJClockProbeMaxTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 38),
    _F3SyncJClockProbeMaxTETotAlarmTime_Type()
)
f3SyncJClockProbeMaxTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMaxTETotAlarmTime.setStatus("current")
_F3SyncJClockProbeConstTETotAlarmTime_Type = Unsigned32
_F3SyncJClockProbeConstTETotAlarmTime_Object = MibTableColumn
f3SyncJClockProbeConstTETotAlarmTime = _F3SyncJClockProbeConstTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 39),
    _F3SyncJClockProbeConstTETotAlarmTime_Type()
)
f3SyncJClockProbeConstTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeConstTETotAlarmTime.setStatus("current")
_F3SyncJClockProbeConstTEMeasurementTime_Type = Unsigned32
_F3SyncJClockProbeConstTEMeasurementTime_Object = MibTableColumn
f3SyncJClockProbeConstTEMeasurementTime = _F3SyncJClockProbeConstTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 40),
    _F3SyncJClockProbeConstTEMeasurementTime_Type()
)
f3SyncJClockProbeConstTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeConstTEMeasurementTime.setStatus("current")
_F3SyncJClockProbeMaxTEMeasurementTime_Type = Unsigned32
_F3SyncJClockProbeMaxTEMeasurementTime_Object = MibTableColumn
f3SyncJClockProbeMaxTEMeasurementTime = _F3SyncJClockProbeMaxTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 41),
    _F3SyncJClockProbeMaxTEMeasurementTime_Type()
)
f3SyncJClockProbeMaxTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMaxTEMeasurementTime.setStatus("current")
_F3SyncJClockProbeMaxTEThreshold_Type = Integer32
_F3SyncJClockProbeMaxTEThreshold_Object = MibTableColumn
f3SyncJClockProbeMaxTEThreshold = _F3SyncJClockProbeMaxTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 42),
    _F3SyncJClockProbeMaxTEThreshold_Type()
)
f3SyncJClockProbeMaxTEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMaxTEThreshold.setStatus("current")
_F3SyncJClockProbeMaxTEClrThreshold_Type = Integer32
_F3SyncJClockProbeMaxTEClrThreshold_Object = MibTableColumn
f3SyncJClockProbeMaxTEClrThreshold = _F3SyncJClockProbeMaxTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 43),
    _F3SyncJClockProbeMaxTEClrThreshold_Type()
)
f3SyncJClockProbeMaxTEClrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMaxTEClrThreshold.setStatus("current")
_F3SyncJClockProbeMTIERestart_Type = TruthValue
_F3SyncJClockProbeMTIERestart_Object = MibTableColumn
f3SyncJClockProbeMTIERestart = _F3SyncJClockProbeMTIERestart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 1, 1, 44),
    _F3SyncJClockProbeMTIERestart_Type()
)
f3SyncJClockProbeMTIERestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIERestart.setStatus("current")
_F3SyncJClockProbeMTIEValueTable_Object = MibTable
f3SyncJClockProbeMTIEValueTable = _F3SyncJClockProbeMTIEValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 2)
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEValueTable.setStatus("current")
_F3SyncJClockProbeMTIEValueEntry_Object = MibTableRow
f3SyncJClockProbeMTIEValueEntry = _F3SyncJClockProbeMTIEValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 2, 1)
)
f3SyncJClockProbeMTIEValueEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeMTIEValueIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEValueEntry.setStatus("current")
_F3SyncJClockProbeMTIEValueIndex_Type = Integer32
_F3SyncJClockProbeMTIEValueIndex_Object = MibTableColumn
f3SyncJClockProbeMTIEValueIndex = _F3SyncJClockProbeMTIEValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 2, 1, 1),
    _F3SyncJClockProbeMTIEValueIndex_Type()
)
f3SyncJClockProbeMTIEValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEValueIndex.setStatus("current")
_F3SyncJClockProbeMTIEValue_Type = Integer32
_F3SyncJClockProbeMTIEValue_Object = MibTableColumn
f3SyncJClockProbeMTIEValue = _F3SyncJClockProbeMTIEValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 2, 1, 2),
    _F3SyncJClockProbeMTIEValue_Type()
)
f3SyncJClockProbeMTIEValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeMTIEValue.setStatus("current")
_F3SyncJClockProbeResHistoryTable_Object = MibTable
f3SyncJClockProbeResHistoryTable = _F3SyncJClockProbeResHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3)
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryTable.setStatus("current")
_F3SyncJClockProbeResHistoryEntry_Object = MibTableRow
f3SyncJClockProbeResHistoryEntry = _F3SyncJClockProbeResHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1)
)
f3SyncJClockProbeResHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryEntry.setStatus("current")
_F3SyncJClockProbeResHistoryIndex_Type = Integer32
_F3SyncJClockProbeResHistoryIndex_Object = MibTableColumn
f3SyncJClockProbeResHistoryIndex = _F3SyncJClockProbeResHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 1),
    _F3SyncJClockProbeResHistoryIndex_Type()
)
f3SyncJClockProbeResHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryIndex.setStatus("current")


class _F3SyncJClockProbeResHistoryAlias_Type(DisplayString):
    """Custom type f3SyncJClockProbeResHistoryAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3SyncJClockProbeResHistoryAlias_Type.__name__ = "DisplayString"
_F3SyncJClockProbeResHistoryAlias_Object = MibTableColumn
f3SyncJClockProbeResHistoryAlias = _F3SyncJClockProbeResHistoryAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 2),
    _F3SyncJClockProbeResHistoryAlias_Type()
)
f3SyncJClockProbeResHistoryAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryAlias.setStatus("current")
_F3SyncJClockProbeResHistorySource_Type = VariablePointer
_F3SyncJClockProbeResHistorySource_Object = MibTableColumn
f3SyncJClockProbeResHistorySource = _F3SyncJClockProbeResHistorySource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 3),
    _F3SyncJClockProbeResHistorySource_Type()
)
f3SyncJClockProbeResHistorySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistorySource.setStatus("current")
_F3SyncJClockProbeResHistoryReference_Type = VariablePointer
_F3SyncJClockProbeResHistoryReference_Object = MibTableColumn
f3SyncJClockProbeResHistoryReference = _F3SyncJClockProbeResHistoryReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 4),
    _F3SyncJClockProbeResHistoryReference_Type()
)
f3SyncJClockProbeResHistoryReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryReference.setStatus("current")
_F3SyncJClockProbeResHistoryExpectedQL_Type = SSMQualityLevel
_F3SyncJClockProbeResHistoryExpectedQL_Object = MibTableColumn
f3SyncJClockProbeResHistoryExpectedQL = _F3SyncJClockProbeResHistoryExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 5),
    _F3SyncJClockProbeResHistoryExpectedQL_Type()
)
f3SyncJClockProbeResHistoryExpectedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryExpectedQL.setStatus("current")
_F3SyncJClockProbeResHistorySourceType_Type = TIESourceType
_F3SyncJClockProbeResHistorySourceType_Object = MibTableColumn
f3SyncJClockProbeResHistorySourceType = _F3SyncJClockProbeResHistorySourceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 6),
    _F3SyncJClockProbeResHistorySourceType_Type()
)
f3SyncJClockProbeResHistorySourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistorySourceType.setStatus("current")
_F3SyncJClockProbeResHistoryMeasurementRate_Type = TIEMeasurementRate
_F3SyncJClockProbeResHistoryMeasurementRate_Object = MibTableColumn
f3SyncJClockProbeResHistoryMeasurementRate = _F3SyncJClockProbeResHistoryMeasurementRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 7),
    _F3SyncJClockProbeResHistoryMeasurementRate_Type()
)
f3SyncJClockProbeResHistoryMeasurementRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMeasurementRate.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEMaskType_Type = MTIEMaskType
_F3SyncJClockProbeResHistoryMTIEMaskType_Object = MibTableColumn
f3SyncJClockProbeResHistoryMTIEMaskType = _F3SyncJClockProbeResHistoryMTIEMaskType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 8),
    _F3SyncJClockProbeResHistoryMTIEMaskType_Type()
)
f3SyncJClockProbeResHistoryMTIEMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEMaskType.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEMaskMargin_Type = Unsigned32
_F3SyncJClockProbeResHistoryMTIEMaskMargin_Object = MibTableColumn
f3SyncJClockProbeResHistoryMTIEMaskMargin = _F3SyncJClockProbeResHistoryMTIEMaskMargin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 9),
    _F3SyncJClockProbeResHistoryMTIEMaskMargin_Type()
)
f3SyncJClockProbeResHistoryMTIEMaskMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEMaskMargin.setStatus("current")
_F3SyncJClockProbeResHistorySourceFailure_Type = TruthValue
_F3SyncJClockProbeResHistorySourceFailure_Object = MibTableColumn
f3SyncJClockProbeResHistorySourceFailure = _F3SyncJClockProbeResHistorySourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 10),
    _F3SyncJClockProbeResHistorySourceFailure_Type()
)
f3SyncJClockProbeResHistorySourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistorySourceFailure.setStatus("current")
_F3SyncJClockProbeResHistoryReferenceFailure_Type = TruthValue
_F3SyncJClockProbeResHistoryReferenceFailure_Object = MibTableColumn
f3SyncJClockProbeResHistoryReferenceFailure = _F3SyncJClockProbeResHistoryReferenceFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 11),
    _F3SyncJClockProbeResHistoryReferenceFailure_Type()
)
f3SyncJClockProbeResHistoryReferenceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryReferenceFailure.setStatus("current")
_F3SyncJClockProbeResHistoryActualTestStartTime_Type = DateAndTime
_F3SyncJClockProbeResHistoryActualTestStartTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryActualTestStartTime = _F3SyncJClockProbeResHistoryActualTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 12),
    _F3SyncJClockProbeResHistoryActualTestStartTime_Type()
)
f3SyncJClockProbeResHistoryActualTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryActualTestStartTime.setStatus("current")
_F3SyncJClockProbeResHistoryActualTestDuration_Type = Unsigned32
_F3SyncJClockProbeResHistoryActualTestDuration_Object = MibTableColumn
f3SyncJClockProbeResHistoryActualTestDuration = _F3SyncJClockProbeResHistoryActualTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 13),
    _F3SyncJClockProbeResHistoryActualTestDuration_Type()
)
f3SyncJClockProbeResHistoryActualTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryActualTestDuration.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEMaskCrossedTime_Type = DateAndTime
_F3SyncJClockProbeResHistoryMTIEMaskCrossedTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryMTIEMaskCrossedTime = _F3SyncJClockProbeResHistoryMTIEMaskCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 14),
    _F3SyncJClockProbeResHistoryMTIEMaskCrossedTime_Type()
)
f3SyncJClockProbeResHistoryMTIEMaskCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEMaskCrossedTime.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime_Type = DateAndTime
_F3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime = _F3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 15),
    _F3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime_Type()
)
f3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime.setStatus("current")
_F3SyncJClockProbeResHistoryStatusMTIEMaskFailed_Type = TruthValue
_F3SyncJClockProbeResHistoryStatusMTIEMaskFailed_Object = MibTableColumn
f3SyncJClockProbeResHistoryStatusMTIEMaskFailed = _F3SyncJClockProbeResHistoryStatusMTIEMaskFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 16),
    _F3SyncJClockProbeResHistoryStatusMTIEMaskFailed_Type()
)
f3SyncJClockProbeResHistoryStatusMTIEMaskFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryStatusMTIEMaskFailed.setStatus("current")
_F3SyncJClockProbeResHistoryStatusMTIEMarginFailed_Type = TruthValue
_F3SyncJClockProbeResHistoryStatusMTIEMarginFailed_Object = MibTableColumn
f3SyncJClockProbeResHistoryStatusMTIEMarginFailed = _F3SyncJClockProbeResHistoryStatusMTIEMarginFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 17),
    _F3SyncJClockProbeResHistoryStatusMTIEMarginFailed_Type()
)
f3SyncJClockProbeResHistoryStatusMTIEMarginFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryStatusMTIEMarginFailed.setStatus("current")
_F3SyncJClockProbeResHistoryStorageType_Type = StorageType
_F3SyncJClockProbeResHistoryStorageType_Object = MibTableColumn
f3SyncJClockProbeResHistoryStorageType = _F3SyncJClockProbeResHistoryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 18),
    _F3SyncJClockProbeResHistoryStorageType_Type()
)
f3SyncJClockProbeResHistoryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryStorageType.setStatus("current")
_F3SyncJClockProbeResHistoryRowStatus_Type = RowStatus
_F3SyncJClockProbeResHistoryRowStatus_Object = MibTableColumn
f3SyncJClockProbeResHistoryRowStatus = _F3SyncJClockProbeResHistoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 19),
    _F3SyncJClockProbeResHistoryRowStatus_Type()
)
f3SyncJClockProbeResHistoryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryRowStatus.setStatus("current")
_F3SyncJClockProbeResHistoryMinFFO_Type = Integer32
_F3SyncJClockProbeResHistoryMinFFO_Object = MibTableColumn
f3SyncJClockProbeResHistoryMinFFO = _F3SyncJClockProbeResHistoryMinFFO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 20),
    _F3SyncJClockProbeResHistoryMinFFO_Type()
)
f3SyncJClockProbeResHistoryMinFFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMinFFO.setStatus("current")
_F3SyncJClockProbeResHistoryMaxFFO_Type = Integer32
_F3SyncJClockProbeResHistoryMaxFFO_Object = MibTableColumn
f3SyncJClockProbeResHistoryMaxFFO = _F3SyncJClockProbeResHistoryMaxFFO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 21),
    _F3SyncJClockProbeResHistoryMaxFFO_Type()
)
f3SyncJClockProbeResHistoryMaxFFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMaxFFO.setStatus("current")
_F3SyncJClockProbeResHistoryAvgFFO_Type = Integer32
_F3SyncJClockProbeResHistoryAvgFFO_Object = MibTableColumn
f3SyncJClockProbeResHistoryAvgFFO = _F3SyncJClockProbeResHistoryAvgFFO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 22),
    _F3SyncJClockProbeResHistoryAvgFFO_Type()
)
f3SyncJClockProbeResHistoryAvgFFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryAvgFFO.setStatus("current")
_F3SyncJClockProbeResHistoryOutOfTargetFFOTime_Type = Integer32
_F3SyncJClockProbeResHistoryOutOfTargetFFOTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryOutOfTargetFFOTime = _F3SyncJClockProbeResHistoryOutOfTargetFFOTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 23),
    _F3SyncJClockProbeResHistoryOutOfTargetFFOTime_Type()
)
f3SyncJClockProbeResHistoryOutOfTargetFFOTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryOutOfTargetFFOTime.setStatus("current")
_F3SyncJClockProbeResHistoryTotalFFOTime_Type = Integer32
_F3SyncJClockProbeResHistoryTotalFFOTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryTotalFFOTime = _F3SyncJClockProbeResHistoryTotalFFOTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 24),
    _F3SyncJClockProbeResHistoryTotalFFOTime_Type()
)
f3SyncJClockProbeResHistoryTotalFFOTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryTotalFFOTime.setStatus("current")
_F3SyncJClockProbeResHistoryMinPhaseOffset_Type = Integer32
_F3SyncJClockProbeResHistoryMinPhaseOffset_Object = MibTableColumn
f3SyncJClockProbeResHistoryMinPhaseOffset = _F3SyncJClockProbeResHistoryMinPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 25),
    _F3SyncJClockProbeResHistoryMinPhaseOffset_Type()
)
f3SyncJClockProbeResHistoryMinPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMinPhaseOffset.setStatus("current")
_F3SyncJClockProbeResHistoryMaxPhaseOffset_Type = Integer32
_F3SyncJClockProbeResHistoryMaxPhaseOffset_Object = MibTableColumn
f3SyncJClockProbeResHistoryMaxPhaseOffset = _F3SyncJClockProbeResHistoryMaxPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 26),
    _F3SyncJClockProbeResHistoryMaxPhaseOffset_Type()
)
f3SyncJClockProbeResHistoryMaxPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMaxPhaseOffset.setStatus("current")
_F3SyncJClockProbeResHistoryAvgPhaseOffset_Type = Integer32
_F3SyncJClockProbeResHistoryAvgPhaseOffset_Object = MibTableColumn
f3SyncJClockProbeResHistoryAvgPhaseOffset = _F3SyncJClockProbeResHistoryAvgPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 27),
    _F3SyncJClockProbeResHistoryAvgPhaseOffset_Type()
)
f3SyncJClockProbeResHistoryAvgPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryAvgPhaseOffset.setStatus("current")
_F3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime_Type = Integer32
_F3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime = _F3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 28),
    _F3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime_Type()
)
f3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime.setStatus("current")
_F3SyncJClockProbeResHistoryTotalPhaseOffsetTime_Type = Integer32
_F3SyncJClockProbeResHistoryTotalPhaseOffsetTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryTotalPhaseOffsetTime = _F3SyncJClockProbeResHistoryTotalPhaseOffsetTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 29),
    _F3SyncJClockProbeResHistoryTotalPhaseOffsetTime_Type()
)
f3SyncJClockProbeResHistoryTotalPhaseOffsetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryTotalPhaseOffsetTime.setStatus("current")
_F3SyncJClockProbeResHistoryMeasurementType_Type = MeasurementType
_F3SyncJClockProbeResHistoryMeasurementType_Object = MibTableColumn
f3SyncJClockProbeResHistoryMeasurementType = _F3SyncJClockProbeResHistoryMeasurementType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 30),
    _F3SyncJClockProbeResHistoryMeasurementType_Type()
)
f3SyncJClockProbeResHistoryMeasurementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMeasurementType.setStatus("current")
_F3SyncJClockProbeResHistoryTeAlertThreshold_Type = Integer32
_F3SyncJClockProbeResHistoryTeAlertThreshold_Object = MibTableColumn
f3SyncJClockProbeResHistoryTeAlertThreshold = _F3SyncJClockProbeResHistoryTeAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 31),
    _F3SyncJClockProbeResHistoryTeAlertThreshold_Type()
)
f3SyncJClockProbeResHistoryTeAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryTeAlertThreshold.setStatus("deprecated")
_F3SyncJClockProbeResHistoryTeAlertClearThreshold_Type = Integer32
_F3SyncJClockProbeResHistoryTeAlertClearThreshold_Object = MibTableColumn
f3SyncJClockProbeResHistoryTeAlertClearThreshold = _F3SyncJClockProbeResHistoryTeAlertClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 32),
    _F3SyncJClockProbeResHistoryTeAlertClearThreshold_Type()
)
f3SyncJClockProbeResHistoryTeAlertClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryTeAlertClearThreshold.setStatus("deprecated")
_F3SyncJClockProbeResHistoryLastTEAlertTime_Type = DateAndTime
_F3SyncJClockProbeResHistoryLastTEAlertTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryLastTEAlertTime = _F3SyncJClockProbeResHistoryLastTEAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 33),
    _F3SyncJClockProbeResHistoryLastTEAlertTime_Type()
)
f3SyncJClockProbeResHistoryLastTEAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryLastTEAlertTime.setStatus("deprecated")
_F3SyncJClockProbeResHistoryLastTEAlertClearTime_Type = DateAndTime
_F3SyncJClockProbeResHistoryLastTEAlertClearTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryLastTEAlertClearTime = _F3SyncJClockProbeResHistoryLastTEAlertClearTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 34),
    _F3SyncJClockProbeResHistoryLastTEAlertClearTime_Type()
)
f3SyncJClockProbeResHistoryLastTEAlertClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryLastTEAlertClearTime.setStatus("deprecated")
_F3SyncJClockProbeResHistoryRunningFailedCount_Type = Integer32
_F3SyncJClockProbeResHistoryRunningFailedCount_Object = MibTableColumn
f3SyncJClockProbeResHistoryRunningFailedCount = _F3SyncJClockProbeResHistoryRunningFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 35),
    _F3SyncJClockProbeResHistoryRunningFailedCount_Type()
)
f3SyncJClockProbeResHistoryRunningFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryRunningFailedCount.setStatus("current")
_F3SyncJClockProbeResHistoryConstTEThreshold_Type = Unsigned32
_F3SyncJClockProbeResHistoryConstTEThreshold_Object = MibTableColumn
f3SyncJClockProbeResHistoryConstTEThreshold = _F3SyncJClockProbeResHistoryConstTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 36),
    _F3SyncJClockProbeResHistoryConstTEThreshold_Type()
)
f3SyncJClockProbeResHistoryConstTEThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryConstTEThreshold.setStatus("current")
_F3SyncJClockProbeResHistoryConstTEClrThreshold_Type = Unsigned32
_F3SyncJClockProbeResHistoryConstTEClrThreshold_Object = MibTableColumn
f3SyncJClockProbeResHistoryConstTEClrThreshold = _F3SyncJClockProbeResHistoryConstTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 37),
    _F3SyncJClockProbeResHistoryConstTEClrThreshold_Type()
)
f3SyncJClockProbeResHistoryConstTEClrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryConstTEClrThreshold.setStatus("current")
_F3SyncJClockProbeResHistoryConstTEWindow_Type = Unsigned32
_F3SyncJClockProbeResHistoryConstTEWindow_Object = MibTableColumn
f3SyncJClockProbeResHistoryConstTEWindow = _F3SyncJClockProbeResHistoryConstTEWindow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 38),
    _F3SyncJClockProbeResHistoryConstTEWindow_Type()
)
f3SyncJClockProbeResHistoryConstTEWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryConstTEWindow.setStatus("current")
_F3SyncJClockProbeResHistoryMaxTETotAlarmTime_Type = Unsigned32
_F3SyncJClockProbeResHistoryMaxTETotAlarmTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryMaxTETotAlarmTime = _F3SyncJClockProbeResHistoryMaxTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 39),
    _F3SyncJClockProbeResHistoryMaxTETotAlarmTime_Type()
)
f3SyncJClockProbeResHistoryMaxTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMaxTETotAlarmTime.setStatus("current")
_F3SyncJClockProbeResHistoryConstTETotAlarmTime_Type = Unsigned32
_F3SyncJClockProbeResHistoryConstTETotAlarmTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryConstTETotAlarmTime = _F3SyncJClockProbeResHistoryConstTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 40),
    _F3SyncJClockProbeResHistoryConstTETotAlarmTime_Type()
)
f3SyncJClockProbeResHistoryConstTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryConstTETotAlarmTime.setStatus("current")
_F3SyncJClockProbeResHistoryConstTEMeasurementTime_Type = Unsigned32
_F3SyncJClockProbeResHistoryConstTEMeasurementTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryConstTEMeasurementTime = _F3SyncJClockProbeResHistoryConstTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 41),
    _F3SyncJClockProbeResHistoryConstTEMeasurementTime_Type()
)
f3SyncJClockProbeResHistoryConstTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryConstTEMeasurementTime.setStatus("current")
_F3SyncJClockProbeResHistoryMaxTEMeasurementTime_Type = Unsigned32
_F3SyncJClockProbeResHistoryMaxTEMeasurementTime_Object = MibTableColumn
f3SyncJClockProbeResHistoryMaxTEMeasurementTime = _F3SyncJClockProbeResHistoryMaxTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 42),
    _F3SyncJClockProbeResHistoryMaxTEMeasurementTime_Type()
)
f3SyncJClockProbeResHistoryMaxTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMaxTEMeasurementTime.setStatus("current")
_F3SyncJClockProbeResHistoryMaxTEThreshold_Type = Integer32
_F3SyncJClockProbeResHistoryMaxTEThreshold_Object = MibTableColumn
f3SyncJClockProbeResHistoryMaxTEThreshold = _F3SyncJClockProbeResHistoryMaxTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 43),
    _F3SyncJClockProbeResHistoryMaxTEThreshold_Type()
)
f3SyncJClockProbeResHistoryMaxTEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMaxTEThreshold.setStatus("current")
_F3SyncJClockProbeResHistoryMaxTEClrThreshold_Type = Integer32
_F3SyncJClockProbeResHistoryMaxTEClrThreshold_Object = MibTableColumn
f3SyncJClockProbeResHistoryMaxTEClrThreshold = _F3SyncJClockProbeResHistoryMaxTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 3, 1, 44),
    _F3SyncJClockProbeResHistoryMaxTEClrThreshold_Type()
)
f3SyncJClockProbeResHistoryMaxTEClrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMaxTEClrThreshold.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEValueTable_Object = MibTable
f3SyncJClockProbeResHistoryMTIEValueTable = _F3SyncJClockProbeResHistoryMTIEValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 4)
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEValueTable.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEValueEntry_Object = MibTableRow
f3SyncJClockProbeResHistoryMTIEValueEntry = _F3SyncJClockProbeResHistoryMTIEValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 4, 1)
)
f3SyncJClockProbeResHistoryMTIEValueEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMTIEValueIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEValueEntry.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEValueIndex_Type = Integer32
_F3SyncJClockProbeResHistoryMTIEValueIndex_Object = MibTableColumn
f3SyncJClockProbeResHistoryMTIEValueIndex = _F3SyncJClockProbeResHistoryMTIEValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 4, 1, 1),
    _F3SyncJClockProbeResHistoryMTIEValueIndex_Type()
)
f3SyncJClockProbeResHistoryMTIEValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEValueIndex.setStatus("current")
_F3SyncJClockProbeResHistoryMTIEValue_Type = Integer32
_F3SyncJClockProbeResHistoryMTIEValue_Object = MibTableColumn
f3SyncJClockProbeResHistoryMTIEValue = _F3SyncJClockProbeResHistoryMTIEValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 4, 1, 2),
    _F3SyncJClockProbeResHistoryMTIEValue_Type()
)
f3SyncJClockProbeResHistoryMTIEValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeResHistoryMTIEValue.setStatus("current")
_F3SyncJPTPClockProbeTable_Object = MibTable
f3SyncJPTPClockProbeTable = _F3SyncJPTPClockProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5)
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeTable.setStatus("current")
_F3SyncJPTPClockProbeEntry_Object = MibTableRow
f3SyncJPTPClockProbeEntry = _F3SyncJPTPClockProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1)
)
f3SyncJPTPClockProbeEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeEntry.setStatus("current")
_F3SyncJPTPClockProbeIndex_Type = Integer32
_F3SyncJPTPClockProbeIndex_Object = MibTableColumn
f3SyncJPTPClockProbeIndex = _F3SyncJPTPClockProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 1),
    _F3SyncJPTPClockProbeIndex_Type()
)
f3SyncJPTPClockProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeIndex.setStatus("current")


class _F3SyncJPTPClockProbeName_Type(DisplayString):
    """Custom type f3SyncJPTPClockProbeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_F3SyncJPTPClockProbeName_Type.__name__ = "DisplayString"
_F3SyncJPTPClockProbeName_Object = MibTableColumn
f3SyncJPTPClockProbeName = _F3SyncJPTPClockProbeName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 2),
    _F3SyncJPTPClockProbeName_Type()
)
f3SyncJPTPClockProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeName.setStatus("current")
_F3SyncJPTPClockProbeMeasurementDirection_Type = PTPMeasurementDirection
_F3SyncJPTPClockProbeMeasurementDirection_Object = MibTableColumn
f3SyncJPTPClockProbeMeasurementDirection = _F3SyncJPTPClockProbeMeasurementDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 3),
    _F3SyncJPTPClockProbeMeasurementDirection_Type()
)
f3SyncJPTPClockProbeMeasurementDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMeasurementDirection.setStatus("current")
_F3SyncJPTPClockProbePTPFlowPoint_Type = VariablePointer
_F3SyncJPTPClockProbePTPFlowPoint_Object = MibTableColumn
f3SyncJPTPClockProbePTPFlowPoint = _F3SyncJPTPClockProbePTPFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 4),
    _F3SyncJPTPClockProbePTPFlowPoint_Type()
)
f3SyncJPTPClockProbePTPFlowPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbePTPFlowPoint.setStatus("current")
_F3SyncJPTPClockProbeIpPrototocol_Type = IpVersion
_F3SyncJPTPClockProbeIpPrototocol_Object = MibTableColumn
f3SyncJPTPClockProbeIpPrototocol = _F3SyncJPTPClockProbeIpPrototocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 5),
    _F3SyncJPTPClockProbeIpPrototocol_Type()
)
f3SyncJPTPClockProbeIpPrototocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeIpPrototocol.setStatus("current")
_F3SyncJPTPClockProbeSlaveIpV4Address_Type = IpAddress
_F3SyncJPTPClockProbeSlaveIpV4Address_Object = MibTableColumn
f3SyncJPTPClockProbeSlaveIpV4Address = _F3SyncJPTPClockProbeSlaveIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 6),
    _F3SyncJPTPClockProbeSlaveIpV4Address_Type()
)
f3SyncJPTPClockProbeSlaveIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeSlaveIpV4Address.setStatus("current")
_F3SyncJPTPClockProbeMasterIpV4Address_Type = IpAddress
_F3SyncJPTPClockProbeMasterIpV4Address_Object = MibTableColumn
f3SyncJPTPClockProbeMasterIpV4Address = _F3SyncJPTPClockProbeMasterIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 7),
    _F3SyncJPTPClockProbeMasterIpV4Address_Type()
)
f3SyncJPTPClockProbeMasterIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMasterIpV4Address.setStatus("current")
_F3SyncJPTPClockProbeReference_Type = VariablePointer
_F3SyncJPTPClockProbeReference_Object = MibTableColumn
f3SyncJPTPClockProbeReference = _F3SyncJPTPClockProbeReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 8),
    _F3SyncJPTPClockProbeReference_Type()
)
f3SyncJPTPClockProbeReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeReference.setStatus("current")
_F3SyncJPTPClockProbeExpectedQL_Type = SSMQualityLevel
_F3SyncJPTPClockProbeExpectedQL_Object = MibTableColumn
f3SyncJPTPClockProbeExpectedQL = _F3SyncJPTPClockProbeExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 9),
    _F3SyncJPTPClockProbeExpectedQL_Type()
)
f3SyncJPTPClockProbeExpectedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeExpectedQL.setStatus("current")
_F3SyncJPTPClockProbeMTIEMaskType_Type = MTIEMaskType
_F3SyncJPTPClockProbeMTIEMaskType_Object = MibTableColumn
f3SyncJPTPClockProbeMTIEMaskType = _F3SyncJPTPClockProbeMTIEMaskType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 10),
    _F3SyncJPTPClockProbeMTIEMaskType_Type()
)
f3SyncJPTPClockProbeMTIEMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEMaskType.setStatus("current")
_F3SyncJPTPClockProbeMTIEMaskMargin_Type = Unsigned32
_F3SyncJPTPClockProbeMTIEMaskMargin_Object = MibTableColumn
f3SyncJPTPClockProbeMTIEMaskMargin = _F3SyncJPTPClockProbeMTIEMaskMargin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 11),
    _F3SyncJPTPClockProbeMTIEMaskMargin_Type()
)
f3SyncJPTPClockProbeMTIEMaskMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEMaskMargin.setStatus("current")
_F3SyncJPTPClockProbeScheduler_Type = VariablePointer
_F3SyncJPTPClockProbeScheduler_Object = MibTableColumn
f3SyncJPTPClockProbeScheduler = _F3SyncJPTPClockProbeScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 12),
    _F3SyncJPTPClockProbeScheduler_Type()
)
f3SyncJPTPClockProbeScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeScheduler.setStatus("current")
_F3SyncJPTPClockProbeTestState_Type = SyncJackTestState
_F3SyncJPTPClockProbeTestState_Object = MibTableColumn
f3SyncJPTPClockProbeTestState = _F3SyncJPTPClockProbeTestState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 13),
    _F3SyncJPTPClockProbeTestState_Type()
)
f3SyncJPTPClockProbeTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeTestState.setStatus("current")
_F3SyncJPTPClockProbeLastTIEResult_Type = Integer32
_F3SyncJPTPClockProbeLastTIEResult_Object = MibTableColumn
f3SyncJPTPClockProbeLastTIEResult = _F3SyncJPTPClockProbeLastTIEResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 14),
    _F3SyncJPTPClockProbeLastTIEResult_Type()
)
f3SyncJPTPClockProbeLastTIEResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeLastTIEResult.setStatus("current")
_F3SyncJPTPClockProbeLastTIEResultTime_Type = DateAndTime
_F3SyncJPTPClockProbeLastTIEResultTime_Object = MibTableColumn
f3SyncJPTPClockProbeLastTIEResultTime = _F3SyncJPTPClockProbeLastTIEResultTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 15),
    _F3SyncJPTPClockProbeLastTIEResultTime_Type()
)
f3SyncJPTPClockProbeLastTIEResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeLastTIEResultTime.setStatus("current")
_F3SyncJPTPClockProbeNoTimestampFailure_Type = TruthValue
_F3SyncJPTPClockProbeNoTimestampFailure_Object = MibTableColumn
f3SyncJPTPClockProbeNoTimestampFailure = _F3SyncJPTPClockProbeNoTimestampFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 16),
    _F3SyncJPTPClockProbeNoTimestampFailure_Type()
)
f3SyncJPTPClockProbeNoTimestampFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeNoTimestampFailure.setStatus("current")
_F3SyncJPTPClockProbeNoEventMessageFailure_Type = TruthValue
_F3SyncJPTPClockProbeNoEventMessageFailure_Object = MibTableColumn
f3SyncJPTPClockProbeNoEventMessageFailure = _F3SyncJPTPClockProbeNoEventMessageFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 17),
    _F3SyncJPTPClockProbeNoEventMessageFailure_Type()
)
f3SyncJPTPClockProbeNoEventMessageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeNoEventMessageFailure.setStatus("current")
_F3SyncJPTPClockProbeReferenceFailure_Type = TruthValue
_F3SyncJPTPClockProbeReferenceFailure_Object = MibTableColumn
f3SyncJPTPClockProbeReferenceFailure = _F3SyncJPTPClockProbeReferenceFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 18),
    _F3SyncJPTPClockProbeReferenceFailure_Type()
)
f3SyncJPTPClockProbeReferenceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeReferenceFailure.setStatus("current")
_F3SyncJPTPClockProbeActualTestStartTime_Type = DateAndTime
_F3SyncJPTPClockProbeActualTestStartTime_Object = MibTableColumn
f3SyncJPTPClockProbeActualTestStartTime = _F3SyncJPTPClockProbeActualTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 19),
    _F3SyncJPTPClockProbeActualTestStartTime_Type()
)
f3SyncJPTPClockProbeActualTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeActualTestStartTime.setStatus("current")
_F3SyncJPTPClockProbeActualTestDuration_Type = Unsigned32
_F3SyncJPTPClockProbeActualTestDuration_Object = MibTableColumn
f3SyncJPTPClockProbeActualTestDuration = _F3SyncJPTPClockProbeActualTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 20),
    _F3SyncJPTPClockProbeActualTestDuration_Type()
)
f3SyncJPTPClockProbeActualTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeActualTestDuration.setStatus("current")
_F3SyncJPTPClockProbeMTIEMaskCrossedTime_Type = DateAndTime
_F3SyncJPTPClockProbeMTIEMaskCrossedTime_Object = MibTableColumn
f3SyncJPTPClockProbeMTIEMaskCrossedTime = _F3SyncJPTPClockProbeMTIEMaskCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 21),
    _F3SyncJPTPClockProbeMTIEMaskCrossedTime_Type()
)
f3SyncJPTPClockProbeMTIEMaskCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEMaskCrossedTime.setStatus("current")
_F3SyncJPTPClockProbeMTIEMaskMarginCrossedTime_Type = DateAndTime
_F3SyncJPTPClockProbeMTIEMaskMarginCrossedTime_Object = MibTableColumn
f3SyncJPTPClockProbeMTIEMaskMarginCrossedTime = _F3SyncJPTPClockProbeMTIEMaskMarginCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 22),
    _F3SyncJPTPClockProbeMTIEMaskMarginCrossedTime_Type()
)
f3SyncJPTPClockProbeMTIEMaskMarginCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEMaskMarginCrossedTime.setStatus("current")
_F3SyncJPTPClockProbeStatusMTIEMaskFailed_Type = TruthValue
_F3SyncJPTPClockProbeStatusMTIEMaskFailed_Object = MibTableColumn
f3SyncJPTPClockProbeStatusMTIEMaskFailed = _F3SyncJPTPClockProbeStatusMTIEMaskFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 23),
    _F3SyncJPTPClockProbeStatusMTIEMaskFailed_Type()
)
f3SyncJPTPClockProbeStatusMTIEMaskFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatusMTIEMaskFailed.setStatus("current")
_F3SyncJPTPClockProbeStatusMTIEMarginFailed_Type = TruthValue
_F3SyncJPTPClockProbeStatusMTIEMarginFailed_Object = MibTableColumn
f3SyncJPTPClockProbeStatusMTIEMarginFailed = _F3SyncJPTPClockProbeStatusMTIEMarginFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 24),
    _F3SyncJPTPClockProbeStatusMTIEMarginFailed_Type()
)
f3SyncJPTPClockProbeStatusMTIEMarginFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatusMTIEMarginFailed.setStatus("current")
_F3SyncJPTPClockProbeStorageType_Type = StorageType
_F3SyncJPTPClockProbeStorageType_Object = MibTableColumn
f3SyncJPTPClockProbeStorageType = _F3SyncJPTPClockProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 25),
    _F3SyncJPTPClockProbeStorageType_Type()
)
f3SyncJPTPClockProbeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStorageType.setStatus("current")
_F3SyncJPTPClockProbeRowStatus_Type = RowStatus
_F3SyncJPTPClockProbeRowStatus_Object = MibTableColumn
f3SyncJPTPClockProbeRowStatus = _F3SyncJPTPClockProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 26),
    _F3SyncJPTPClockProbeRowStatus_Type()
)
f3SyncJPTPClockProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeRowStatus.setStatus("current")
_F3SyncJPTPClockProbeFfoTarget_Type = Integer32
_F3SyncJPTPClockProbeFfoTarget_Object = MibTableColumn
f3SyncJPTPClockProbeFfoTarget = _F3SyncJPTPClockProbeFfoTarget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 27),
    _F3SyncJPTPClockProbeFfoTarget_Type()
)
f3SyncJPTPClockProbeFfoTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeFfoTarget.setStatus("current")
_F3SyncJPTPClockProbeFfoObserWindow_Type = FFOObserWindow
_F3SyncJPTPClockProbeFfoObserWindow_Object = MibTableColumn
f3SyncJPTPClockProbeFfoObserWindow = _F3SyncJPTPClockProbeFfoObserWindow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 28),
    _F3SyncJPTPClockProbeFfoObserWindow_Type()
)
f3SyncJPTPClockProbeFfoObserWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeFfoObserWindow.setStatus("current")
_F3SyncJPTPClockProbeLastFFOResult_Type = Integer32
_F3SyncJPTPClockProbeLastFFOResult_Object = MibTableColumn
f3SyncJPTPClockProbeLastFFOResult = _F3SyncJPTPClockProbeLastFFOResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 29),
    _F3SyncJPTPClockProbeLastFFOResult_Type()
)
f3SyncJPTPClockProbeLastFFOResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeLastFFOResult.setStatus("current")
_F3SyncJPTPClockProbeTimeOfLastFFOResult_Type = DateAndTime
_F3SyncJPTPClockProbeTimeOfLastFFOResult_Object = MibTableColumn
f3SyncJPTPClockProbeTimeOfLastFFOResult = _F3SyncJPTPClockProbeTimeOfLastFFOResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 30),
    _F3SyncJPTPClockProbeTimeOfLastFFOResult_Type()
)
f3SyncJPTPClockProbeTimeOfLastFFOResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeTimeOfLastFFOResult.setStatus("current")
_F3SyncJPTPClockProbeRawDataCollectionEnabled_Type = TruthValue
_F3SyncJPTPClockProbeRawDataCollectionEnabled_Object = MibTableColumn
f3SyncJPTPClockProbeRawDataCollectionEnabled = _F3SyncJPTPClockProbeRawDataCollectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 31),
    _F3SyncJPTPClockProbeRawDataCollectionEnabled_Type()
)
f3SyncJPTPClockProbeRawDataCollectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeRawDataCollectionEnabled.setStatus("current")
_F3SyncJPTPClockProbeTeAlertThreshold_Type = Integer32
_F3SyncJPTPClockProbeTeAlertThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeTeAlertThreshold = _F3SyncJPTPClockProbeTeAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 32),
    _F3SyncJPTPClockProbeTeAlertThreshold_Type()
)
f3SyncJPTPClockProbeTeAlertThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeTeAlertThreshold.setStatus("deprecated")
_F3SyncJPTPClockProbeTeAlertClearThreshold_Type = Integer32
_F3SyncJPTPClockProbeTeAlertClearThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeTeAlertClearThreshold = _F3SyncJPTPClockProbeTeAlertClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 33),
    _F3SyncJPTPClockProbeTeAlertClearThreshold_Type()
)
f3SyncJPTPClockProbeTeAlertClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeTeAlertClearThreshold.setStatus("deprecated")
_F3SyncJPTPClockProbeLastTEAlertTime_Type = DateAndTime
_F3SyncJPTPClockProbeLastTEAlertTime_Object = MibTableColumn
f3SyncJPTPClockProbeLastTEAlertTime = _F3SyncJPTPClockProbeLastTEAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 34),
    _F3SyncJPTPClockProbeLastTEAlertTime_Type()
)
f3SyncJPTPClockProbeLastTEAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeLastTEAlertTime.setStatus("deprecated")
_F3SyncJPTPClockProbeLastTEAlertClearTime_Type = DateAndTime
_F3SyncJPTPClockProbeLastTEAlertClearTime_Object = MibTableColumn
f3SyncJPTPClockProbeLastTEAlertClearTime = _F3SyncJPTPClockProbeLastTEAlertClearTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 35),
    _F3SyncJPTPClockProbeLastTEAlertClearTime_Type()
)
f3SyncJPTPClockProbeLastTEAlertClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeLastTEAlertClearTime.setStatus("deprecated")
_F3SyncJPTPClockProbeRunningFailedCount_Type = Integer32
_F3SyncJPTPClockProbeRunningFailedCount_Object = MibTableColumn
f3SyncJPTPClockProbeRunningFailedCount = _F3SyncJPTPClockProbeRunningFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 36),
    _F3SyncJPTPClockProbeRunningFailedCount_Type()
)
f3SyncJPTPClockProbeRunningFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeRunningFailedCount.setStatus("current")
_F3SyncJPTPClockProbeMeasurementType_Type = MeasurementType
_F3SyncJPTPClockProbeMeasurementType_Object = MibTableColumn
f3SyncJPTPClockProbeMeasurementType = _F3SyncJPTPClockProbeMeasurementType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 37),
    _F3SyncJPTPClockProbeMeasurementType_Type()
)
f3SyncJPTPClockProbeMeasurementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMeasurementType.setStatus("current")
_F3SyncJPTPClockProbeDelayMS_Type = Integer32
_F3SyncJPTPClockProbeDelayMS_Object = MibTableColumn
f3SyncJPTPClockProbeDelayMS = _F3SyncJPTPClockProbeDelayMS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 38),
    _F3SyncJPTPClockProbeDelayMS_Type()
)
f3SyncJPTPClockProbeDelayMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeDelayMS.setStatus("deprecated")
_F3SyncJPTPClockProbeDelaySM_Type = Integer32
_F3SyncJPTPClockProbeDelaySM_Object = MibTableColumn
f3SyncJPTPClockProbeDelaySM = _F3SyncJPTPClockProbeDelaySM_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 39),
    _F3SyncJPTPClockProbeDelaySM_Type()
)
f3SyncJPTPClockProbeDelaySM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeDelaySM.setStatus("deprecated")
_F3SyncJPTPClockProbeTAsymmetry_Type = Integer32
_F3SyncJPTPClockProbeTAsymmetry_Object = MibTableColumn
f3SyncJPTPClockProbeTAsymmetry = _F3SyncJPTPClockProbeTAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 40),
    _F3SyncJPTPClockProbeTAsymmetry_Type()
)
f3SyncJPTPClockProbeTAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeTAsymmetry.setStatus("deprecated")
_F3SyncJPTPClockProbeDelayCompensation_Type = Integer32
_F3SyncJPTPClockProbeDelayCompensation_Object = MibTableColumn
f3SyncJPTPClockProbeDelayCompensation = _F3SyncJPTPClockProbeDelayCompensation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 41),
    _F3SyncJPTPClockProbeDelayCompensation_Type()
)
f3SyncJPTPClockProbeDelayCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeDelayCompensation.setStatus("current")
_F3SyncJPTPClockProbeConstTEThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeConstTEThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeConstTEThreshold = _F3SyncJPTPClockProbeConstTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 42),
    _F3SyncJPTPClockProbeConstTEThreshold_Type()
)
f3SyncJPTPClockProbeConstTEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeConstTEThreshold.setStatus("current")
_F3SyncJPTPClockProbeConstTEClrThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeConstTEClrThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeConstTEClrThreshold = _F3SyncJPTPClockProbeConstTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 43),
    _F3SyncJPTPClockProbeConstTEClrThreshold_Type()
)
f3SyncJPTPClockProbeConstTEClrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeConstTEClrThreshold.setStatus("current")
_F3SyncJPTPClockProbeConstTEWindow_Type = Unsigned32
_F3SyncJPTPClockProbeConstTEWindow_Object = MibTableColumn
f3SyncJPTPClockProbeConstTEWindow = _F3SyncJPTPClockProbeConstTEWindow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 44),
    _F3SyncJPTPClockProbeConstTEWindow_Type()
)
f3SyncJPTPClockProbeConstTEWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeConstTEWindow.setStatus("current")
_F3SyncJPTPClockProbeInstTEThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeInstTEThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeInstTEThreshold = _F3SyncJPTPClockProbeInstTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 45),
    _F3SyncJPTPClockProbeInstTEThreshold_Type()
)
f3SyncJPTPClockProbeInstTEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeInstTEThreshold.setStatus("current")
_F3SyncJPTPClockProbeInstTEClrThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeInstTEClrThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeInstTEClrThreshold = _F3SyncJPTPClockProbeInstTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 46),
    _F3SyncJPTPClockProbeInstTEClrThreshold_Type()
)
f3SyncJPTPClockProbeInstTEClrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeInstTEClrThreshold.setStatus("current")
_F3SyncJPTPClockProbeMaxTETotAlarmTime_Type = Unsigned32
_F3SyncJPTPClockProbeMaxTETotAlarmTime_Object = MibTableColumn
f3SyncJPTPClockProbeMaxTETotAlarmTime = _F3SyncJPTPClockProbeMaxTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 47),
    _F3SyncJPTPClockProbeMaxTETotAlarmTime_Type()
)
f3SyncJPTPClockProbeMaxTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMaxTETotAlarmTime.setStatus("current")
_F3SyncJPTPClockProbeConstTETotAlarmTime_Type = Unsigned32
_F3SyncJPTPClockProbeConstTETotAlarmTime_Object = MibTableColumn
f3SyncJPTPClockProbeConstTETotAlarmTime = _F3SyncJPTPClockProbeConstTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 48),
    _F3SyncJPTPClockProbeConstTETotAlarmTime_Type()
)
f3SyncJPTPClockProbeConstTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeConstTETotAlarmTime.setStatus("current")
_F3SyncJPTPClockProbeInstTETotAlarmTime_Type = Unsigned32
_F3SyncJPTPClockProbeInstTETotAlarmTime_Object = MibTableColumn
f3SyncJPTPClockProbeInstTETotAlarmTime = _F3SyncJPTPClockProbeInstTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 49),
    _F3SyncJPTPClockProbeInstTETotAlarmTime_Type()
)
f3SyncJPTPClockProbeInstTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeInstTETotAlarmTime.setStatus("current")


class _F3SyncJPTPClockProbeSlavePortIdentity_Type(DisplayString):
    """Custom type f3SyncJPTPClockProbeSlavePortIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_F3SyncJPTPClockProbeSlavePortIdentity_Type.__name__ = "DisplayString"
_F3SyncJPTPClockProbeSlavePortIdentity_Object = MibTableColumn
f3SyncJPTPClockProbeSlavePortIdentity = _F3SyncJPTPClockProbeSlavePortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 50),
    _F3SyncJPTPClockProbeSlavePortIdentity_Type()
)
f3SyncJPTPClockProbeSlavePortIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeSlavePortIdentity.setStatus("current")


class _F3SyncJPTPClockProbeMasterPortIdentity_Type(DisplayString):
    """Custom type f3SyncJPTPClockProbeMasterPortIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_F3SyncJPTPClockProbeMasterPortIdentity_Type.__name__ = "DisplayString"
_F3SyncJPTPClockProbeMasterPortIdentity_Object = MibTableColumn
f3SyncJPTPClockProbeMasterPortIdentity = _F3SyncJPTPClockProbeMasterPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 51),
    _F3SyncJPTPClockProbeMasterPortIdentity_Type()
)
f3SyncJPTPClockProbeMasterPortIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMasterPortIdentity.setStatus("current")
_F3SyncJPTPClockProbeConstTEMeasurementTime_Type = Unsigned32
_F3SyncJPTPClockProbeConstTEMeasurementTime_Object = MibTableColumn
f3SyncJPTPClockProbeConstTEMeasurementTime = _F3SyncJPTPClockProbeConstTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 52),
    _F3SyncJPTPClockProbeConstTEMeasurementTime_Type()
)
f3SyncJPTPClockProbeConstTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeConstTEMeasurementTime.setStatus("current")
_F3SyncJPTPClockProbeMaxTEMeasurementTime_Type = Unsigned32
_F3SyncJPTPClockProbeMaxTEMeasurementTime_Object = MibTableColumn
f3SyncJPTPClockProbeMaxTEMeasurementTime = _F3SyncJPTPClockProbeMaxTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 53),
    _F3SyncJPTPClockProbeMaxTEMeasurementTime_Type()
)
f3SyncJPTPClockProbeMaxTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMaxTEMeasurementTime.setStatus("current")
_F3SyncJPTPClockProbeInstTEMeasurementTime_Type = Unsigned32
_F3SyncJPTPClockProbeInstTEMeasurementTime_Object = MibTableColumn
f3SyncJPTPClockProbeInstTEMeasurementTime = _F3SyncJPTPClockProbeInstTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 54),
    _F3SyncJPTPClockProbeInstTEMeasurementTime_Type()
)
f3SyncJPTPClockProbeInstTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeInstTEMeasurementTime.setStatus("current")
_F3SyncJPTPClockProbeMaxTEThreshold_Type = Integer32
_F3SyncJPTPClockProbeMaxTEThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeMaxTEThreshold = _F3SyncJPTPClockProbeMaxTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 55),
    _F3SyncJPTPClockProbeMaxTEThreshold_Type()
)
f3SyncJPTPClockProbeMaxTEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMaxTEThreshold.setStatus("current")
_F3SyncJPTPClockProbeMaxTEClrThreshold_Type = Integer32
_F3SyncJPTPClockProbeMaxTEClrThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeMaxTEClrThreshold = _F3SyncJPTPClockProbeMaxTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 56),
    _F3SyncJPTPClockProbeMaxTEClrThreshold_Type()
)
f3SyncJPTPClockProbeMaxTEClrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMaxTEClrThreshold.setStatus("current")
_F3SyncJPTPClockProbeMTIERestart_Type = TruthValue
_F3SyncJPTPClockProbeMTIERestart_Object = MibTableColumn
f3SyncJPTPClockProbeMTIERestart = _F3SyncJPTPClockProbeMTIERestart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 5, 1, 57),
    _F3SyncJPTPClockProbeMTIERestart_Type()
)
f3SyncJPTPClockProbeMTIERestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIERestart.setStatus("current")
_F3SyncJPTPClockProbeMTIEValueTable_Object = MibTable
f3SyncJPTPClockProbeMTIEValueTable = _F3SyncJPTPClockProbeMTIEValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 6)
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEValueTable.setStatus("current")
_F3SyncJPTPClockProbeMTIEValueEntry_Object = MibTableRow
f3SyncJPTPClockProbeMTIEValueEntry = _F3SyncJPTPClockProbeMTIEValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 6, 1)
)
f3SyncJPTPClockProbeMTIEValueEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMTIEValueIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEValueEntry.setStatus("current")
_F3SyncJPTPClockProbeMTIEValueIndex_Type = Integer32
_F3SyncJPTPClockProbeMTIEValueIndex_Object = MibTableColumn
f3SyncJPTPClockProbeMTIEValueIndex = _F3SyncJPTPClockProbeMTIEValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 6, 1, 1),
    _F3SyncJPTPClockProbeMTIEValueIndex_Type()
)
f3SyncJPTPClockProbeMTIEValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEValueIndex.setStatus("current")
_F3SyncJPTPClockProbeMTIEValue_Type = Integer32
_F3SyncJPTPClockProbeMTIEValue_Object = MibTableColumn
f3SyncJPTPClockProbeMTIEValue = _F3SyncJPTPClockProbeMTIEValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 6, 1, 2),
    _F3SyncJPTPClockProbeMTIEValue_Type()
)
f3SyncJPTPClockProbeMTIEValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeMTIEValue.setStatus("current")
_F3SyncJPTPClockProbeResHistoryTable_Object = MibTable
f3SyncJPTPClockProbeResHistoryTable = _F3SyncJPTPClockProbeResHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7)
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryTable.setStatus("current")
_F3SyncJPTPClockProbeResHistoryEntry_Object = MibTableRow
f3SyncJPTPClockProbeResHistoryEntry = _F3SyncJPTPClockProbeResHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1)
)
f3SyncJPTPClockProbeResHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryEntry.setStatus("current")
_F3SyncJPTPClockProbeResHistoryIndex_Type = Integer32
_F3SyncJPTPClockProbeResHistoryIndex_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryIndex = _F3SyncJPTPClockProbeResHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 1),
    _F3SyncJPTPClockProbeResHistoryIndex_Type()
)
f3SyncJPTPClockProbeResHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryIndex.setStatus("current")


class _F3SyncJPTPClockProbeResHistoryAlias_Type(DisplayString):
    """Custom type f3SyncJPTPClockProbeResHistoryAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3SyncJPTPClockProbeResHistoryAlias_Type.__name__ = "DisplayString"
_F3SyncJPTPClockProbeResHistoryAlias_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryAlias = _F3SyncJPTPClockProbeResHistoryAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 2),
    _F3SyncJPTPClockProbeResHistoryAlias_Type()
)
f3SyncJPTPClockProbeResHistoryAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryAlias.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMeasurementDirection_Type = PTPMeasurementDirection
_F3SyncJPTPClockProbeResHistoryMeasurementDirection_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMeasurementDirection = _F3SyncJPTPClockProbeResHistoryMeasurementDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 3),
    _F3SyncJPTPClockProbeResHistoryMeasurementDirection_Type()
)
f3SyncJPTPClockProbeResHistoryMeasurementDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMeasurementDirection.setStatus("current")
_F3SyncJPTPClockProbeResHistoryPTPFlowPoint_Type = VariablePointer
_F3SyncJPTPClockProbeResHistoryPTPFlowPoint_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryPTPFlowPoint = _F3SyncJPTPClockProbeResHistoryPTPFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 4),
    _F3SyncJPTPClockProbeResHistoryPTPFlowPoint_Type()
)
f3SyncJPTPClockProbeResHistoryPTPFlowPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryPTPFlowPoint.setStatus("current")
_F3SyncJPTPClockProbeResHistoryIpPrototocol_Type = IpVersion
_F3SyncJPTPClockProbeResHistoryIpPrototocol_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryIpPrototocol = _F3SyncJPTPClockProbeResHistoryIpPrototocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 5),
    _F3SyncJPTPClockProbeResHistoryIpPrototocol_Type()
)
f3SyncJPTPClockProbeResHistoryIpPrototocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryIpPrototocol.setStatus("current")
_F3SyncJPTPClockProbeResHistorySlaveIpV4Address_Type = IpAddress
_F3SyncJPTPClockProbeResHistorySlaveIpV4Address_Object = MibTableColumn
f3SyncJPTPClockProbeResHistorySlaveIpV4Address = _F3SyncJPTPClockProbeResHistorySlaveIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 6),
    _F3SyncJPTPClockProbeResHistorySlaveIpV4Address_Type()
)
f3SyncJPTPClockProbeResHistorySlaveIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistorySlaveIpV4Address.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMasterIpV4Address_Type = IpAddress
_F3SyncJPTPClockProbeResHistoryMasterIpV4Address_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMasterIpV4Address = _F3SyncJPTPClockProbeResHistoryMasterIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 7),
    _F3SyncJPTPClockProbeResHistoryMasterIpV4Address_Type()
)
f3SyncJPTPClockProbeResHistoryMasterIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMasterIpV4Address.setStatus("current")
_F3SyncJPTPClockProbeResHistoryReference_Type = VariablePointer
_F3SyncJPTPClockProbeResHistoryReference_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryReference = _F3SyncJPTPClockProbeResHistoryReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 8),
    _F3SyncJPTPClockProbeResHistoryReference_Type()
)
f3SyncJPTPClockProbeResHistoryReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryReference.setStatus("current")
_F3SyncJPTPClockProbeResHistoryExpectedQL_Type = SSMQualityLevel
_F3SyncJPTPClockProbeResHistoryExpectedQL_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryExpectedQL = _F3SyncJPTPClockProbeResHistoryExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 9),
    _F3SyncJPTPClockProbeResHistoryExpectedQL_Type()
)
f3SyncJPTPClockProbeResHistoryExpectedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryExpectedQL.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEMaskType_Type = MTIEMaskType
_F3SyncJPTPClockProbeResHistoryMTIEMaskType_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMTIEMaskType = _F3SyncJPTPClockProbeResHistoryMTIEMaskType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 10),
    _F3SyncJPTPClockProbeResHistoryMTIEMaskType_Type()
)
f3SyncJPTPClockProbeResHistoryMTIEMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEMaskType.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEMaskMargin_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryMTIEMaskMargin_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMTIEMaskMargin = _F3SyncJPTPClockProbeResHistoryMTIEMaskMargin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 11),
    _F3SyncJPTPClockProbeResHistoryMTIEMaskMargin_Type()
)
f3SyncJPTPClockProbeResHistoryMTIEMaskMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEMaskMargin.setStatus("current")
_F3SyncJPTPClockProbeResHistoryNoTimestampFailure_Type = TruthValue
_F3SyncJPTPClockProbeResHistoryNoTimestampFailure_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryNoTimestampFailure = _F3SyncJPTPClockProbeResHistoryNoTimestampFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 12),
    _F3SyncJPTPClockProbeResHistoryNoTimestampFailure_Type()
)
f3SyncJPTPClockProbeResHistoryNoTimestampFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryNoTimestampFailure.setStatus("current")
_F3SyncJPTPClockProbeResHistoryNoEventMessageFailure_Type = TruthValue
_F3SyncJPTPClockProbeResHistoryNoEventMessageFailure_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryNoEventMessageFailure = _F3SyncJPTPClockProbeResHistoryNoEventMessageFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 13),
    _F3SyncJPTPClockProbeResHistoryNoEventMessageFailure_Type()
)
f3SyncJPTPClockProbeResHistoryNoEventMessageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryNoEventMessageFailure.setStatus("current")
_F3SyncJPTPClockProbeResHistoryReferenceFailure_Type = TruthValue
_F3SyncJPTPClockProbeResHistoryReferenceFailure_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryReferenceFailure = _F3SyncJPTPClockProbeResHistoryReferenceFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 14),
    _F3SyncJPTPClockProbeResHistoryReferenceFailure_Type()
)
f3SyncJPTPClockProbeResHistoryReferenceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryReferenceFailure.setStatus("current")
_F3SyncJPTPClockProbeResHistoryActualTestStartTime_Type = DateAndTime
_F3SyncJPTPClockProbeResHistoryActualTestStartTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryActualTestStartTime = _F3SyncJPTPClockProbeResHistoryActualTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 15),
    _F3SyncJPTPClockProbeResHistoryActualTestStartTime_Type()
)
f3SyncJPTPClockProbeResHistoryActualTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryActualTestStartTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryActualTestDuration_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryActualTestDuration_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryActualTestDuration = _F3SyncJPTPClockProbeResHistoryActualTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 16),
    _F3SyncJPTPClockProbeResHistoryActualTestDuration_Type()
)
f3SyncJPTPClockProbeResHistoryActualTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryActualTestDuration.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime_Type = DateAndTime
_F3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime = _F3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 17),
    _F3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime_Type()
)
f3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime_Type = DateAndTime
_F3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime = _F3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 18),
    _F3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime_Type()
)
f3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed_Type = TruthValue
_F3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed = _F3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 19),
    _F3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed_Type()
)
f3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed.setStatus("current")
_F3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed_Type = TruthValue
_F3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed = _F3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 20),
    _F3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed_Type()
)
f3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed.setStatus("current")
_F3SyncJPTPClockProbeResHistoryStorageType_Type = StorageType
_F3SyncJPTPClockProbeResHistoryStorageType_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryStorageType = _F3SyncJPTPClockProbeResHistoryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 21),
    _F3SyncJPTPClockProbeResHistoryStorageType_Type()
)
f3SyncJPTPClockProbeResHistoryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryStorageType.setStatus("current")
_F3SyncJPTPClockProbeResHistoryRowStatus_Type = RowStatus
_F3SyncJPTPClockProbeResHistoryRowStatus_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryRowStatus = _F3SyncJPTPClockProbeResHistoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 22),
    _F3SyncJPTPClockProbeResHistoryRowStatus_Type()
)
f3SyncJPTPClockProbeResHistoryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryRowStatus.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMinFFO_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMinFFO_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMinFFO = _F3SyncJPTPClockProbeResHistoryMinFFO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 23),
    _F3SyncJPTPClockProbeResHistoryMinFFO_Type()
)
f3SyncJPTPClockProbeResHistoryMinFFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMinFFO.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMaxFFO_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMaxFFO_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMaxFFO = _F3SyncJPTPClockProbeResHistoryMaxFFO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 24),
    _F3SyncJPTPClockProbeResHistoryMaxFFO_Type()
)
f3SyncJPTPClockProbeResHistoryMaxFFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMaxFFO.setStatus("current")
_F3SyncJPTPClockProbeResHistoryAvgFFO_Type = Integer32
_F3SyncJPTPClockProbeResHistoryAvgFFO_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryAvgFFO = _F3SyncJPTPClockProbeResHistoryAvgFFO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 25),
    _F3SyncJPTPClockProbeResHistoryAvgFFO_Type()
)
f3SyncJPTPClockProbeResHistoryAvgFFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryAvgFFO.setStatus("current")
_F3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime_Type = Integer32
_F3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime = _F3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 26),
    _F3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime_Type()
)
f3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryTotalFFOTime_Type = Integer32
_F3SyncJPTPClockProbeResHistoryTotalFFOTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryTotalFFOTime = _F3SyncJPTPClockProbeResHistoryTotalFFOTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 27),
    _F3SyncJPTPClockProbeResHistoryTotalFFOTime_Type()
)
f3SyncJPTPClockProbeResHistoryTotalFFOTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryTotalFFOTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMinPhaseOffset_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMinPhaseOffset_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMinPhaseOffset = _F3SyncJPTPClockProbeResHistoryMinPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 28),
    _F3SyncJPTPClockProbeResHistoryMinPhaseOffset_Type()
)
f3SyncJPTPClockProbeResHistoryMinPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMinPhaseOffset.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMaxPhaseOffset_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMaxPhaseOffset_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMaxPhaseOffset = _F3SyncJPTPClockProbeResHistoryMaxPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 29),
    _F3SyncJPTPClockProbeResHistoryMaxPhaseOffset_Type()
)
f3SyncJPTPClockProbeResHistoryMaxPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMaxPhaseOffset.setStatus("current")
_F3SyncJPTPClockProbeResHistoryAvgPhaseOffset_Type = Integer32
_F3SyncJPTPClockProbeResHistoryAvgPhaseOffset_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryAvgPhaseOffset = _F3SyncJPTPClockProbeResHistoryAvgPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 30),
    _F3SyncJPTPClockProbeResHistoryAvgPhaseOffset_Type()
)
f3SyncJPTPClockProbeResHistoryAvgPhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryAvgPhaseOffset.setStatus("current")
_F3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime_Type = Integer32
_F3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime = _F3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 31),
    _F3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime_Type()
)
f3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime_Type = Integer32
_F3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime = _F3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 32),
    _F3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime_Type()
)
f3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryTeAlertThreshold_Type = Integer32
_F3SyncJPTPClockProbeResHistoryTeAlertThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryTeAlertThreshold = _F3SyncJPTPClockProbeResHistoryTeAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 33),
    _F3SyncJPTPClockProbeResHistoryTeAlertThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryTeAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryTeAlertThreshold.setStatus("deprecated")
_F3SyncJPTPClockProbeResHistoryTeAlertClearThreshold_Type = Integer32
_F3SyncJPTPClockProbeResHistoryTeAlertClearThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryTeAlertClearThreshold = _F3SyncJPTPClockProbeResHistoryTeAlertClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 34),
    _F3SyncJPTPClockProbeResHistoryTeAlertClearThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryTeAlertClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryTeAlertClearThreshold.setStatus("deprecated")
_F3SyncJPTPClockProbeResHistoryLastTEAlertTime_Type = DateAndTime
_F3SyncJPTPClockProbeResHistoryLastTEAlertTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryLastTEAlertTime = _F3SyncJPTPClockProbeResHistoryLastTEAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 35),
    _F3SyncJPTPClockProbeResHistoryLastTEAlertTime_Type()
)
f3SyncJPTPClockProbeResHistoryLastTEAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryLastTEAlertTime.setStatus("deprecated")
_F3SyncJPTPClockProbeResHistoryLastTEAlertClearTime_Type = DateAndTime
_F3SyncJPTPClockProbeResHistoryLastTEAlertClearTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryLastTEAlertClearTime = _F3SyncJPTPClockProbeResHistoryLastTEAlertClearTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 36),
    _F3SyncJPTPClockProbeResHistoryLastTEAlertClearTime_Type()
)
f3SyncJPTPClockProbeResHistoryLastTEAlertClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryLastTEAlertClearTime.setStatus("deprecated")
_F3SyncJPTPClockProbeResHistoryRunningFailedCount_Type = Integer32
_F3SyncJPTPClockProbeResHistoryRunningFailedCount_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryRunningFailedCount = _F3SyncJPTPClockProbeResHistoryRunningFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 37),
    _F3SyncJPTPClockProbeResHistoryRunningFailedCount_Type()
)
f3SyncJPTPClockProbeResHistoryRunningFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryRunningFailedCount.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMeasurementType_Type = MeasurementType
_F3SyncJPTPClockProbeResHistoryMeasurementType_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMeasurementType = _F3SyncJPTPClockProbeResHistoryMeasurementType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 38),
    _F3SyncJPTPClockProbeResHistoryMeasurementType_Type()
)
f3SyncJPTPClockProbeResHistoryMeasurementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMeasurementType.setStatus("current")
_F3SyncJPTPClockProbeResHistoryConstTEThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryConstTEThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryConstTEThreshold = _F3SyncJPTPClockProbeResHistoryConstTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 39),
    _F3SyncJPTPClockProbeResHistoryConstTEThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryConstTEThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryConstTEThreshold.setStatus("current")
_F3SyncJPTPClockProbeResHistoryConstTEClrThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryConstTEClrThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryConstTEClrThreshold = _F3SyncJPTPClockProbeResHistoryConstTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 40),
    _F3SyncJPTPClockProbeResHistoryConstTEClrThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryConstTEClrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryConstTEClrThreshold.setStatus("current")
_F3SyncJPTPClockProbeResHistoryConstTEWindow_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryConstTEWindow_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryConstTEWindow = _F3SyncJPTPClockProbeResHistoryConstTEWindow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 41),
    _F3SyncJPTPClockProbeResHistoryConstTEWindow_Type()
)
f3SyncJPTPClockProbeResHistoryConstTEWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryConstTEWindow.setStatus("current")
_F3SyncJPTPClockProbeResHistoryInstTEThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryInstTEThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryInstTEThreshold = _F3SyncJPTPClockProbeResHistoryInstTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 42),
    _F3SyncJPTPClockProbeResHistoryInstTEThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryInstTEThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryInstTEThreshold.setStatus("current")
_F3SyncJPTPClockProbeResHistoryInstTEClrThreshold_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryInstTEClrThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryInstTEClrThreshold = _F3SyncJPTPClockProbeResHistoryInstTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 43),
    _F3SyncJPTPClockProbeResHistoryInstTEClrThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryInstTEClrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryInstTEClrThreshold.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime = _F3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 44),
    _F3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime_Type()
)
f3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryConstTETotAlarmTime_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryConstTETotAlarmTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryConstTETotAlarmTime = _F3SyncJPTPClockProbeResHistoryConstTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 45),
    _F3SyncJPTPClockProbeResHistoryConstTETotAlarmTime_Type()
)
f3SyncJPTPClockProbeResHistoryConstTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryConstTETotAlarmTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryInstTETotAlarmTime_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryInstTETotAlarmTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryInstTETotAlarmTime = _F3SyncJPTPClockProbeResHistoryInstTETotAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 46),
    _F3SyncJPTPClockProbeResHistoryInstTETotAlarmTime_Type()
)
f3SyncJPTPClockProbeResHistoryInstTETotAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryInstTETotAlarmTime.setStatus("current")


class _F3SyncJPTPClockProbeResHistorySlavePortIdentity_Type(DisplayString):
    """Custom type f3SyncJPTPClockProbeResHistorySlavePortIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_F3SyncJPTPClockProbeResHistorySlavePortIdentity_Type.__name__ = "DisplayString"
_F3SyncJPTPClockProbeResHistorySlavePortIdentity_Object = MibTableColumn
f3SyncJPTPClockProbeResHistorySlavePortIdentity = _F3SyncJPTPClockProbeResHistorySlavePortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 47),
    _F3SyncJPTPClockProbeResHistorySlavePortIdentity_Type()
)
f3SyncJPTPClockProbeResHistorySlavePortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistorySlavePortIdentity.setStatus("current")


class _F3SyncJPTPClockProbeResHistoryMasterPortIdentity_Type(DisplayString):
    """Custom type f3SyncJPTPClockProbeResHistoryMasterPortIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_F3SyncJPTPClockProbeResHistoryMasterPortIdentity_Type.__name__ = "DisplayString"
_F3SyncJPTPClockProbeResHistoryMasterPortIdentity_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMasterPortIdentity = _F3SyncJPTPClockProbeResHistoryMasterPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 48),
    _F3SyncJPTPClockProbeResHistoryMasterPortIdentity_Type()
)
f3SyncJPTPClockProbeResHistoryMasterPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMasterPortIdentity.setStatus("current")
_F3SyncJPTPClockProbeResHistoryConstTEMeasurementTime_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryConstTEMeasurementTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryConstTEMeasurementTime = _F3SyncJPTPClockProbeResHistoryConstTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 49),
    _F3SyncJPTPClockProbeResHistoryConstTEMeasurementTime_Type()
)
f3SyncJPTPClockProbeResHistoryConstTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryConstTEMeasurementTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime = _F3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 50),
    _F3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime_Type()
)
f3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryInstTEMeasurementTime_Type = Unsigned32
_F3SyncJPTPClockProbeResHistoryInstTEMeasurementTime_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryInstTEMeasurementTime = _F3SyncJPTPClockProbeResHistoryInstTEMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 51),
    _F3SyncJPTPClockProbeResHistoryInstTEMeasurementTime_Type()
)
f3SyncJPTPClockProbeResHistoryInstTEMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryInstTEMeasurementTime.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMaxTEThreshold_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMaxTEThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMaxTEThreshold = _F3SyncJPTPClockProbeResHistoryMaxTEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 52),
    _F3SyncJPTPClockProbeResHistoryMaxTEThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryMaxTEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMaxTEThreshold.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMaxTEClrThreshold_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMaxTEClrThreshold_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMaxTEClrThreshold = _F3SyncJPTPClockProbeResHistoryMaxTEClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 7, 1, 53),
    _F3SyncJPTPClockProbeResHistoryMaxTEClrThreshold_Type()
)
f3SyncJPTPClockProbeResHistoryMaxTEClrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMaxTEClrThreshold.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEValueTable_Object = MibTable
f3SyncJPTPClockProbeResHistoryMTIEValueTable = _F3SyncJPTPClockProbeResHistoryMTIEValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 8)
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEValueTable.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEValueEntry_Object = MibTableRow
f3SyncJPTPClockProbeResHistoryMTIEValueEntry = _F3SyncJPTPClockProbeResHistoryMTIEValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 8, 1)
)
f3SyncJPTPClockProbeResHistoryMTIEValueEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMTIEValueIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEValueEntry.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEValueIndex_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMTIEValueIndex_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMTIEValueIndex = _F3SyncJPTPClockProbeResHistoryMTIEValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 8, 1, 1),
    _F3SyncJPTPClockProbeResHistoryMTIEValueIndex_Type()
)
f3SyncJPTPClockProbeResHistoryMTIEValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEValueIndex.setStatus("current")
_F3SyncJPTPClockProbeResHistoryMTIEValue_Type = Integer32
_F3SyncJPTPClockProbeResHistoryMTIEValue_Object = MibTableColumn
f3SyncJPTPClockProbeResHistoryMTIEValue = _F3SyncJPTPClockProbeResHistoryMTIEValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 8, 1, 2),
    _F3SyncJPTPClockProbeResHistoryMTIEValue_Type()
)
f3SyncJPTPClockProbeResHistoryMTIEValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeResHistoryMTIEValue.setStatus("current")
_F3SyncJPTPNetworkProbeTable_Object = MibTable
f3SyncJPTPNetworkProbeTable = _F3SyncJPTPNetworkProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9)
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeTable.setStatus("current")
_F3SyncJPTPNetworkProbeEntry_Object = MibTableRow
f3SyncJPTPNetworkProbeEntry = _F3SyncJPTPNetworkProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1)
)
f3SyncJPTPNetworkProbeEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeEntry.setStatus("current")
_F3SyncJPTPNetworkProbeIndex_Type = Integer32
_F3SyncJPTPNetworkProbeIndex_Object = MibTableColumn
f3SyncJPTPNetworkProbeIndex = _F3SyncJPTPNetworkProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 1),
    _F3SyncJPTPNetworkProbeIndex_Type()
)
f3SyncJPTPNetworkProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeIndex.setStatus("current")


class _F3SyncJPTPNetworkProbeName_Type(DisplayString):
    """Custom type f3SyncJPTPNetworkProbeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_F3SyncJPTPNetworkProbeName_Type.__name__ = "DisplayString"
_F3SyncJPTPNetworkProbeName_Object = MibTableColumn
f3SyncJPTPNetworkProbeName = _F3SyncJPTPNetworkProbeName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 2),
    _F3SyncJPTPNetworkProbeName_Type()
)
f3SyncJPTPNetworkProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeName.setStatus("current")
_F3SyncJPTPNetworkProbeAdminState_Type = AdminState
_F3SyncJPTPNetworkProbeAdminState_Object = MibTableColumn
f3SyncJPTPNetworkProbeAdminState = _F3SyncJPTPNetworkProbeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 3),
    _F3SyncJPTPNetworkProbeAdminState_Type()
)
f3SyncJPTPNetworkProbeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeAdminState.setStatus("current")
_F3SyncJPTPNetworkProbeOperationalState_Type = OperationalState
_F3SyncJPTPNetworkProbeOperationalState_Object = MibTableColumn
f3SyncJPTPNetworkProbeOperationalState = _F3SyncJPTPNetworkProbeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 4),
    _F3SyncJPTPNetworkProbeOperationalState_Type()
)
f3SyncJPTPNetworkProbeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeOperationalState.setStatus("current")
_F3SyncJPTPNetworkProbeSecondaryState_Type = SecondaryState
_F3SyncJPTPNetworkProbeSecondaryState_Object = MibTableColumn
f3SyncJPTPNetworkProbeSecondaryState = _F3SyncJPTPNetworkProbeSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 5),
    _F3SyncJPTPNetworkProbeSecondaryState_Type()
)
f3SyncJPTPNetworkProbeSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeSecondaryState.setStatus("current")
_F3SyncJPTPNetworkProbePTPFlowPoint_Type = VariablePointer
_F3SyncJPTPNetworkProbePTPFlowPoint_Object = MibTableColumn
f3SyncJPTPNetworkProbePTPFlowPoint = _F3SyncJPTPNetworkProbePTPFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 6),
    _F3SyncJPTPNetworkProbePTPFlowPoint_Type()
)
f3SyncJPTPNetworkProbePTPFlowPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbePTPFlowPoint.setStatus("current")
_F3SyncJPTPNetworkProbeIpPrototocol_Type = IpVersion
_F3SyncJPTPNetworkProbeIpPrototocol_Object = MibTableColumn
f3SyncJPTPNetworkProbeIpPrototocol = _F3SyncJPTPNetworkProbeIpPrototocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 7),
    _F3SyncJPTPNetworkProbeIpPrototocol_Type()
)
f3SyncJPTPNetworkProbeIpPrototocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeIpPrototocol.setStatus("current")
_F3SyncJPTPNetworkProbeSlaveIpV4Address_Type = IpAddress
_F3SyncJPTPNetworkProbeSlaveIpV4Address_Object = MibTableColumn
f3SyncJPTPNetworkProbeSlaveIpV4Address = _F3SyncJPTPNetworkProbeSlaveIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 8),
    _F3SyncJPTPNetworkProbeSlaveIpV4Address_Type()
)
f3SyncJPTPNetworkProbeSlaveIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeSlaveIpV4Address.setStatus("current")
_F3SyncJPTPNetworkProbeMasterIpV4Address_Type = IpAddress
_F3SyncJPTPNetworkProbeMasterIpV4Address_Object = MibTableColumn
f3SyncJPTPNetworkProbeMasterIpV4Address = _F3SyncJPTPNetworkProbeMasterIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 9),
    _F3SyncJPTPNetworkProbeMasterIpV4Address_Type()
)
f3SyncJPTPNetworkProbeMasterIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeMasterIpV4Address.setStatus("current")
_F3SyncJPTPNetworkProbeReference_Type = VariablePointer
_F3SyncJPTPNetworkProbeReference_Object = MibTableColumn
f3SyncJPTPNetworkProbeReference = _F3SyncJPTPNetworkProbeReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 10),
    _F3SyncJPTPNetworkProbeReference_Type()
)
f3SyncJPTPNetworkProbeReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeReference.setStatus("current")
_F3SyncJPTPNetworkProbeExpectedQL_Type = SSMQualityLevel
_F3SyncJPTPNetworkProbeExpectedQL_Object = MibTableColumn
f3SyncJPTPNetworkProbeExpectedQL = _F3SyncJPTPNetworkProbeExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 11),
    _F3SyncJPTPNetworkProbeExpectedQL_Type()
)
f3SyncJPTPNetworkProbeExpectedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeExpectedQL.setStatus("current")
_F3SyncJPTPNetworkProbeActualTestStartTime_Type = DateAndTime
_F3SyncJPTPNetworkProbeActualTestStartTime_Object = MibTableColumn
f3SyncJPTPNetworkProbeActualTestStartTime = _F3SyncJPTPNetworkProbeActualTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 12),
    _F3SyncJPTPNetworkProbeActualTestStartTime_Type()
)
f3SyncJPTPNetworkProbeActualTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeActualTestStartTime.setStatus("current")
_F3SyncJPTPNetworkProbeActualTestDuration_Type = Unsigned32
_F3SyncJPTPNetworkProbeActualTestDuration_Object = MibTableColumn
f3SyncJPTPNetworkProbeActualTestDuration = _F3SyncJPTPNetworkProbeActualTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 13),
    _F3SyncJPTPNetworkProbeActualTestDuration_Type()
)
f3SyncJPTPNetworkProbeActualTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeActualTestDuration.setStatus("current")
_F3SyncJPTPNetworkProbePDVAssuredHi_Type = Unsigned32
_F3SyncJPTPNetworkProbePDVAssuredHi_Object = MibTableColumn
f3SyncJPTPNetworkProbePDVAssuredHi = _F3SyncJPTPNetworkProbePDVAssuredHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 14),
    _F3SyncJPTPNetworkProbePDVAssuredHi_Type()
)
f3SyncJPTPNetworkProbePDVAssuredHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbePDVAssuredHi.setStatus("current")
_F3SyncJPTPNetworkProbePDVAssuredLo_Type = Unsigned32
_F3SyncJPTPNetworkProbePDVAssuredLo_Object = MibTableColumn
f3SyncJPTPNetworkProbePDVAssuredLo = _F3SyncJPTPNetworkProbePDVAssuredLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 15),
    _F3SyncJPTPNetworkProbePDVAssuredLo_Type()
)
f3SyncJPTPNetworkProbePDVAssuredLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbePDVAssuredLo.setStatus("current")
_F3SyncJPTPNetworkProbePDVSatisfiedHi_Type = Unsigned32
_F3SyncJPTPNetworkProbePDVSatisfiedHi_Object = MibTableColumn
f3SyncJPTPNetworkProbePDVSatisfiedHi = _F3SyncJPTPNetworkProbePDVSatisfiedHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 16),
    _F3SyncJPTPNetworkProbePDVSatisfiedHi_Type()
)
f3SyncJPTPNetworkProbePDVSatisfiedHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbePDVSatisfiedHi.setStatus("current")
_F3SyncJPTPNetworkProbePDVSatisfiedLo_Type = Unsigned32
_F3SyncJPTPNetworkProbePDVSatisfiedLo_Object = MibTableColumn
f3SyncJPTPNetworkProbePDVSatisfiedLo = _F3SyncJPTPNetworkProbePDVSatisfiedLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 17),
    _F3SyncJPTPNetworkProbePDVSatisfiedLo_Type()
)
f3SyncJPTPNetworkProbePDVSatisfiedLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbePDVSatisfiedLo.setStatus("current")
_F3SyncJPTPNetworkProbeResPDVFwdLowRange_Type = Unsigned32
_F3SyncJPTPNetworkProbeResPDVFwdLowRange_Object = MibTableColumn
f3SyncJPTPNetworkProbeResPDVFwdLowRange = _F3SyncJPTPNetworkProbeResPDVFwdLowRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 18),
    _F3SyncJPTPNetworkProbeResPDVFwdLowRange_Type()
)
f3SyncJPTPNetworkProbeResPDVFwdLowRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeResPDVFwdLowRange.setStatus("current")
_F3SyncJPTPNetworkProbeResPDVFwdMediumRange_Type = Unsigned32
_F3SyncJPTPNetworkProbeResPDVFwdMediumRange_Object = MibTableColumn
f3SyncJPTPNetworkProbeResPDVFwdMediumRange = _F3SyncJPTPNetworkProbeResPDVFwdMediumRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 19),
    _F3SyncJPTPNetworkProbeResPDVFwdMediumRange_Type()
)
f3SyncJPTPNetworkProbeResPDVFwdMediumRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeResPDVFwdMediumRange.setStatus("current")
_F3SyncJPTPNetworkProbeResPDVFwdHighRange_Type = Unsigned32
_F3SyncJPTPNetworkProbeResPDVFwdHighRange_Object = MibTableColumn
f3SyncJPTPNetworkProbeResPDVFwdHighRange = _F3SyncJPTPNetworkProbeResPDVFwdHighRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 20),
    _F3SyncJPTPNetworkProbeResPDVFwdHighRange_Type()
)
f3SyncJPTPNetworkProbeResPDVFwdHighRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeResPDVFwdHighRange.setStatus("current")
_F3SyncJPTPNetworkProbeResPDVRevLowRange_Type = Unsigned32
_F3SyncJPTPNetworkProbeResPDVRevLowRange_Object = MibTableColumn
f3SyncJPTPNetworkProbeResPDVRevLowRange = _F3SyncJPTPNetworkProbeResPDVRevLowRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 21),
    _F3SyncJPTPNetworkProbeResPDVRevLowRange_Type()
)
f3SyncJPTPNetworkProbeResPDVRevLowRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeResPDVRevLowRange.setStatus("current")
_F3SyncJPTPNetworkProbeResPDVRevMediumRange_Type = Unsigned32
_F3SyncJPTPNetworkProbeResPDVRevMediumRange_Object = MibTableColumn
f3SyncJPTPNetworkProbeResPDVRevMediumRange = _F3SyncJPTPNetworkProbeResPDVRevMediumRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 22),
    _F3SyncJPTPNetworkProbeResPDVRevMediumRange_Type()
)
f3SyncJPTPNetworkProbeResPDVRevMediumRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeResPDVRevMediumRange.setStatus("current")
_F3SyncJPTPNetworkProbeResPDVRevHighRange_Type = Unsigned32
_F3SyncJPTPNetworkProbeResPDVRevHighRange_Object = MibTableColumn
f3SyncJPTPNetworkProbeResPDVRevHighRange = _F3SyncJPTPNetworkProbeResPDVRevHighRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 23),
    _F3SyncJPTPNetworkProbeResPDVRevHighRange_Type()
)
f3SyncJPTPNetworkProbeResPDVRevHighRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeResPDVRevHighRange.setStatus("current")
_F3SyncJPTPNetworkProbeScheduler_Type = VariablePointer
_F3SyncJPTPNetworkProbeScheduler_Object = MibTableColumn
f3SyncJPTPNetworkProbeScheduler = _F3SyncJPTPNetworkProbeScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 24),
    _F3SyncJPTPNetworkProbeScheduler_Type()
)
f3SyncJPTPNetworkProbeScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeScheduler.setStatus("current")
_F3SyncJPTPNetworkProbeTestState_Type = SyncJackTestState
_F3SyncJPTPNetworkProbeTestState_Object = MibTableColumn
f3SyncJPTPNetworkProbeTestState = _F3SyncJPTPNetworkProbeTestState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 25),
    _F3SyncJPTPNetworkProbeTestState_Type()
)
f3SyncJPTPNetworkProbeTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeTestState.setStatus("current")
_F3SyncJPTPNetworkProbeNoTimestampFailure_Type = TruthValue
_F3SyncJPTPNetworkProbeNoTimestampFailure_Object = MibTableColumn
f3SyncJPTPNetworkProbeNoTimestampFailure = _F3SyncJPTPNetworkProbeNoTimestampFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 26),
    _F3SyncJPTPNetworkProbeNoTimestampFailure_Type()
)
f3SyncJPTPNetworkProbeNoTimestampFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeNoTimestampFailure.setStatus("current")
_F3SyncJPTPNetworkProbeNoEventMessageFailure_Type = TruthValue
_F3SyncJPTPNetworkProbeNoEventMessageFailure_Object = MibTableColumn
f3SyncJPTPNetworkProbeNoEventMessageFailure = _F3SyncJPTPNetworkProbeNoEventMessageFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 27),
    _F3SyncJPTPNetworkProbeNoEventMessageFailure_Type()
)
f3SyncJPTPNetworkProbeNoEventMessageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeNoEventMessageFailure.setStatus("current")
_F3SyncJPTPNetworkProbeFwdScore_Type = Unsigned32
_F3SyncJPTPNetworkProbeFwdScore_Object = MibTableColumn
f3SyncJPTPNetworkProbeFwdScore = _F3SyncJPTPNetworkProbeFwdScore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 28),
    _F3SyncJPTPNetworkProbeFwdScore_Type()
)
f3SyncJPTPNetworkProbeFwdScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeFwdScore.setStatus("current")
_F3SyncJPTPNetworkProbeRevScore_Type = Unsigned32
_F3SyncJPTPNetworkProbeRevScore_Object = MibTableColumn
f3SyncJPTPNetworkProbeRevScore = _F3SyncJPTPNetworkProbeRevScore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 29),
    _F3SyncJPTPNetworkProbeRevScore_Type()
)
f3SyncJPTPNetworkProbeRevScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeRevScore.setStatus("current")
_F3SyncJPTPNetworkProbeReferenceFailure_Type = TruthValue
_F3SyncJPTPNetworkProbeReferenceFailure_Object = MibTableColumn
f3SyncJPTPNetworkProbeReferenceFailure = _F3SyncJPTPNetworkProbeReferenceFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 30),
    _F3SyncJPTPNetworkProbeReferenceFailure_Type()
)
f3SyncJPTPNetworkProbeReferenceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeReferenceFailure.setStatus("current")
_F3SyncJPTPNetworkProbeStorageType_Type = StorageType
_F3SyncJPTPNetworkProbeStorageType_Object = MibTableColumn
f3SyncJPTPNetworkProbeStorageType = _F3SyncJPTPNetworkProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 31),
    _F3SyncJPTPNetworkProbeStorageType_Type()
)
f3SyncJPTPNetworkProbeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStorageType.setStatus("current")
_F3SyncJPTPNetworkProbeRowStatus_Type = RowStatus
_F3SyncJPTPNetworkProbeRowStatus_Object = MibTableColumn
f3SyncJPTPNetworkProbeRowStatus = _F3SyncJPTPNetworkProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 32),
    _F3SyncJPTPNetworkProbeRowStatus_Type()
)
f3SyncJPTPNetworkProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeRowStatus.setStatus("current")
_F3SyncJPTPNetworkProbeResultsAvailable_Type = TruthValue
_F3SyncJPTPNetworkProbeResultsAvailable_Object = MibTableColumn
f3SyncJPTPNetworkProbeResultsAvailable = _F3SyncJPTPNetworkProbeResultsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 9, 1, 33),
    _F3SyncJPTPNetworkProbeResultsAvailable_Type()
)
f3SyncJPTPNetworkProbeResultsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeResultsAvailable.setStatus("current")
_F3SyncJScheduleGroupTable_Object = MibTable
f3SyncJScheduleGroupTable = _F3SyncJScheduleGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10)
)
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupTable.setStatus("current")
_F3SyncJScheduleGroupEntry_Object = MibTableRow
f3SyncJScheduleGroupEntry = _F3SyncJScheduleGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1)
)
f3SyncJScheduleGroupEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJScheduleGroupIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupEntry.setStatus("current")
_F3SyncJScheduleGroupIndex_Type = Integer32
_F3SyncJScheduleGroupIndex_Object = MibTableColumn
f3SyncJScheduleGroupIndex = _F3SyncJScheduleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 1),
    _F3SyncJScheduleGroupIndex_Type()
)
f3SyncJScheduleGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupIndex.setStatus("current")


class _F3SyncJScheduleGroupDescr_Type(DisplayString):
    """Custom type f3SyncJScheduleGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_F3SyncJScheduleGroupDescr_Type.__name__ = "DisplayString"
_F3SyncJScheduleGroupDescr_Object = MibTableColumn
f3SyncJScheduleGroupDescr = _F3SyncJScheduleGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 2),
    _F3SyncJScheduleGroupDescr_Type()
)
f3SyncJScheduleGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupDescr.setStatus("current")


class _F3SyncJScheduleGroupEntityList_Type(DisplayString):
    """Custom type f3SyncJScheduleGroupEntityList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_F3SyncJScheduleGroupEntityList_Type.__name__ = "DisplayString"
_F3SyncJScheduleGroupEntityList_Object = MibTableColumn
f3SyncJScheduleGroupEntityList = _F3SyncJScheduleGroupEntityList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 3),
    _F3SyncJScheduleGroupEntityList_Type()
)
f3SyncJScheduleGroupEntityList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupEntityList.setStatus("current")
_F3SyncJScheduleGroupType_Type = ScheduleType
_F3SyncJScheduleGroupType_Object = MibTableColumn
f3SyncJScheduleGroupType = _F3SyncJScheduleGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 4),
    _F3SyncJScheduleGroupType_Type()
)
f3SyncJScheduleGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupType.setStatus("current")
_F3SyncJScheduleGroupStartTime_Type = DateAndTime
_F3SyncJScheduleGroupStartTime_Object = MibTableColumn
f3SyncJScheduleGroupStartTime = _F3SyncJScheduleGroupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 5),
    _F3SyncJScheduleGroupStartTime_Type()
)
f3SyncJScheduleGroupStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupStartTime.setStatus("current")
_F3SyncJScheduleGroupDuration_Type = Unsigned32
_F3SyncJScheduleGroupDuration_Object = MibTableColumn
f3SyncJScheduleGroupDuration = _F3SyncJScheduleGroupDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 6),
    _F3SyncJScheduleGroupDuration_Type()
)
f3SyncJScheduleGroupDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupDuration.setStatus("current")
_F3SyncJScheduleGroupStatus_Type = SchedActivityStatus
_F3SyncJScheduleGroupStatus_Object = MibTableColumn
f3SyncJScheduleGroupStatus = _F3SyncJScheduleGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 7),
    _F3SyncJScheduleGroupStatus_Type()
)
f3SyncJScheduleGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupStatus.setStatus("current")
_F3SyncJScheduleGroupStorageType_Type = StorageType
_F3SyncJScheduleGroupStorageType_Object = MibTableColumn
f3SyncJScheduleGroupStorageType = _F3SyncJScheduleGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 8),
    _F3SyncJScheduleGroupStorageType_Type()
)
f3SyncJScheduleGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupStorageType.setStatus("current")
_F3SyncJScheduleGroupRowStatus_Type = RowStatus
_F3SyncJScheduleGroupRowStatus_Object = MibTableColumn
f3SyncJScheduleGroupRowStatus = _F3SyncJScheduleGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 10, 1, 9),
    _F3SyncJScheduleGroupRowStatus_Type()
)
f3SyncJScheduleGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncJScheduleGroupRowStatus.setStatus("current")
_F3UserDefinedMTIEMaskTable_Object = MibTable
f3UserDefinedMTIEMaskTable = _F3UserDefinedMTIEMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11)
)
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskTable.setStatus("current")
_F3UserDefinedMTIEMaskEntry_Object = MibTableRow
f3UserDefinedMTIEMaskEntry = _F3UserDefinedMTIEMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11, 1)
)
f3UserDefinedMTIEMaskEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3UserDefinedMTIEMaskIndex"),
)
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskEntry.setStatus("current")
_F3UserDefinedMTIEMaskIndex_Type = Integer32
_F3UserDefinedMTIEMaskIndex_Object = MibTableColumn
f3UserDefinedMTIEMaskIndex = _F3UserDefinedMTIEMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11, 1, 1),
    _F3UserDefinedMTIEMaskIndex_Type()
)
f3UserDefinedMTIEMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskIndex.setStatus("current")


class _F3UserDefinedMTIEMaskName_Type(DisplayString):
    """Custom type f3UserDefinedMTIEMaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_F3UserDefinedMTIEMaskName_Type.__name__ = "DisplayString"
_F3UserDefinedMTIEMaskName_Object = MibTableColumn
f3UserDefinedMTIEMaskName = _F3UserDefinedMTIEMaskName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11, 1, 2),
    _F3UserDefinedMTIEMaskName_Type()
)
f3UserDefinedMTIEMaskName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskName.setStatus("current")


class _F3UserDefinedMTIEMaskDisplayPoints_Type(DisplayString):
    """Custom type f3UserDefinedMTIEMaskDisplayPoints based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_F3UserDefinedMTIEMaskDisplayPoints_Type.__name__ = "DisplayString"
_F3UserDefinedMTIEMaskDisplayPoints_Object = MibTableColumn
f3UserDefinedMTIEMaskDisplayPoints = _F3UserDefinedMTIEMaskDisplayPoints_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11, 1, 3),
    _F3UserDefinedMTIEMaskDisplayPoints_Type()
)
f3UserDefinedMTIEMaskDisplayPoints.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskDisplayPoints.setStatus("current")


class _F3UserDefinedMTIEMaskMeasurmentPoints_Type(DisplayString):
    """Custom type f3UserDefinedMTIEMaskMeasurmentPoints based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_F3UserDefinedMTIEMaskMeasurmentPoints_Type.__name__ = "DisplayString"
_F3UserDefinedMTIEMaskMeasurmentPoints_Object = MibTableColumn
f3UserDefinedMTIEMaskMeasurmentPoints = _F3UserDefinedMTIEMaskMeasurmentPoints_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11, 1, 4),
    _F3UserDefinedMTIEMaskMeasurmentPoints_Type()
)
f3UserDefinedMTIEMaskMeasurmentPoints.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskMeasurmentPoints.setStatus("current")
_F3UserDefinedMTIEMaskStorageType_Type = StorageType
_F3UserDefinedMTIEMaskStorageType_Object = MibTableColumn
f3UserDefinedMTIEMaskStorageType = _F3UserDefinedMTIEMaskStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11, 1, 5),
    _F3UserDefinedMTIEMaskStorageType_Type()
)
f3UserDefinedMTIEMaskStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskStorageType.setStatus("current")
_F3UserDefinedMTIEMaskRowStatus_Type = RowStatus
_F3UserDefinedMTIEMaskRowStatus_Object = MibTableColumn
f3UserDefinedMTIEMaskRowStatus = _F3UserDefinedMTIEMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 1, 11, 1, 6),
    _F3UserDefinedMTIEMaskRowStatus_Type()
)
f3UserDefinedMTIEMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3UserDefinedMTIEMaskRowStatus.setStatus("current")
_F3SyncJPerformanceObjects_ObjectIdentity = ObjectIdentity
f3SyncJPerformanceObjects = _F3SyncJPerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2)
)
_F3SyncJPTPNetworkProbeStatsTable_Object = MibTable
f3SyncJPTPNetworkProbeStatsTable = _F3SyncJPTPNetworkProbeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1)
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsTable.setStatus("current")
_F3SyncJPTPNetworkProbeStatsEntry_Object = MibTableRow
f3SyncJPTPNetworkProbeStatsEntry = _F3SyncJPTPNetworkProbeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1)
)
f3SyncJPTPNetworkProbeStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsEntry.setStatus("current")


class _F3SyncJPTPNetworkProbeStatsIndex_Type(Integer32):
    """Custom type f3SyncJPTPNetworkProbeStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_F3SyncJPTPNetworkProbeStatsIndex_Type.__name__ = "Integer32"
_F3SyncJPTPNetworkProbeStatsIndex_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsIndex = _F3SyncJPTPNetworkProbeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 1),
    _F3SyncJPTPNetworkProbeStatsIndex_Type()
)
f3SyncJPTPNetworkProbeStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsIndex.setStatus("current")
_F3SyncJPTPNetworkProbeStatsIntervalType_Type = CmPmIntervalType
_F3SyncJPTPNetworkProbeStatsIntervalType_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsIntervalType = _F3SyncJPTPNetworkProbeStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 2),
    _F3SyncJPTPNetworkProbeStatsIntervalType_Type()
)
f3SyncJPTPNetworkProbeStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsIntervalType.setStatus("current")
_F3SyncJPTPNetworkProbeStatsValid_Type = TruthValue
_F3SyncJPTPNetworkProbeStatsValid_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsValid = _F3SyncJPTPNetworkProbeStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 3),
    _F3SyncJPTPNetworkProbeStatsValid_Type()
)
f3SyncJPTPNetworkProbeStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsValid.setStatus("current")
_F3SyncJPTPNetworkProbeStatsAction_Type = CmPmBinAction
_F3SyncJPTPNetworkProbeStatsAction_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsAction = _F3SyncJPTPNetworkProbeStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 4),
    _F3SyncJPTPNetworkProbeStatsAction_Type()
)
f3SyncJPTPNetworkProbeStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsAction.setStatus("current")
_F3SyncJPTPNetworkProbeStatsSyncMsgsRx_Type = PerfCounter32
_F3SyncJPTPNetworkProbeStatsSyncMsgsRx_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsSyncMsgsRx = _F3SyncJPTPNetworkProbeStatsSyncMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 5),
    _F3SyncJPTPNetworkProbeStatsSyncMsgsRx_Type()
)
f3SyncJPTPNetworkProbeStatsSyncMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsSyncMsgsRx.setStatus("current")
_F3SyncJPTPNetworkProbeStatsDelayRspMsgsRx_Type = PerfCounter32
_F3SyncJPTPNetworkProbeStatsDelayRspMsgsRx_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsDelayRspMsgsRx = _F3SyncJPTPNetworkProbeStatsDelayRspMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 6),
    _F3SyncJPTPNetworkProbeStatsDelayRspMsgsRx_Type()
)
f3SyncJPTPNetworkProbeStatsDelayRspMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsDelayRspMsgsRx.setStatus("current")
_F3SyncJPTPNetworkProbeStatsLostSyncMsgs_Type = PerfCounter32
_F3SyncJPTPNetworkProbeStatsLostSyncMsgs_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsLostSyncMsgs = _F3SyncJPTPNetworkProbeStatsLostSyncMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 7),
    _F3SyncJPTPNetworkProbeStatsLostSyncMsgs_Type()
)
f3SyncJPTPNetworkProbeStatsLostSyncMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsLostSyncMsgs.setStatus("current")
_F3SyncJPTPNetworkProbeStatsLostDelayRspMsgs_Type = PerfCounter32
_F3SyncJPTPNetworkProbeStatsLostDelayRspMsgs_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsLostDelayRspMsgs = _F3SyncJPTPNetworkProbeStatsLostDelayRspMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 8),
    _F3SyncJPTPNetworkProbeStatsLostDelayRspMsgs_Type()
)
f3SyncJPTPNetworkProbeStatsLostDelayRspMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsLostDelayRspMsgs.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMinMeanPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMinMeanPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMinMeanPathDelay = _F3SyncJPTPNetworkProbeStatsMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 9),
    _F3SyncJPTPNetworkProbeStatsMinMeanPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMinMeanPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMaxMeanPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMaxMeanPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMaxMeanPathDelay = _F3SyncJPTPNetworkProbeStatsMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 10),
    _F3SyncJPTPNetworkProbeStatsMaxMeanPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMaxMeanPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsAvgMeanPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsAvgMeanPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsAvgMeanPathDelay = _F3SyncJPTPNetworkProbeStatsAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 11),
    _F3SyncJPTPNetworkProbeStatsAvgMeanPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsAvgMeanPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMinSyncPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMinSyncPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMinSyncPathDelay = _F3SyncJPTPNetworkProbeStatsMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 12),
    _F3SyncJPTPNetworkProbeStatsMinSyncPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMinSyncPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMaxSyncPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMaxSyncPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMaxSyncPathDelay = _F3SyncJPTPNetworkProbeStatsMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 13),
    _F3SyncJPTPNetworkProbeStatsMaxSyncPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMaxSyncPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsAvgSyncPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsAvgSyncPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsAvgSyncPathDelay = _F3SyncJPTPNetworkProbeStatsAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 14),
    _F3SyncJPTPNetworkProbeStatsAvgSyncPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsAvgSyncPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsAvgResPDVFwd_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsAvgResPDVFwd_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsAvgResPDVFwd = _F3SyncJPTPNetworkProbeStatsAvgResPDVFwd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 15),
    _F3SyncJPTPNetworkProbeStatsAvgResPDVFwd_Type()
)
f3SyncJPTPNetworkProbeStatsAvgResPDVFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsAvgResPDVFwd.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVFwdLow_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVFwdLow_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVFwdLow = _F3SyncJPTPNetworkProbeStatsResPDVFwdLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 16),
    _F3SyncJPTPNetworkProbeStatsResPDVFwdLow_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVFwdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVFwdLow.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVFwdMedium_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVFwdMedium_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVFwdMedium = _F3SyncJPTPNetworkProbeStatsResPDVFwdMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 17),
    _F3SyncJPTPNetworkProbeStatsResPDVFwdMedium_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVFwdMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVFwdMedium.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVFwdHigh_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVFwdHigh_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVFwdHigh = _F3SyncJPTPNetworkProbeStatsResPDVFwdHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 18),
    _F3SyncJPTPNetworkProbeStatsResPDVFwdHigh_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVFwdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVFwdHigh.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVFwdTotal_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVFwdTotal_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVFwdTotal = _F3SyncJPTPNetworkProbeStatsResPDVFwdTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 19),
    _F3SyncJPTPNetworkProbeStatsResPDVFwdTotal_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVFwdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVFwdTotal.setStatus("current")
_F3SyncJPTPNetworkProbeStatsFwdScore5_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsFwdScore5_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsFwdScore5 = _F3SyncJPTPNetworkProbeStatsFwdScore5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 20),
    _F3SyncJPTPNetworkProbeStatsFwdScore5_Type()
)
f3SyncJPTPNetworkProbeStatsFwdScore5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsFwdScore5.setStatus("current")
_F3SyncJPTPNetworkProbeStatsFwdScore4_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsFwdScore4_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsFwdScore4 = _F3SyncJPTPNetworkProbeStatsFwdScore4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 21),
    _F3SyncJPTPNetworkProbeStatsFwdScore4_Type()
)
f3SyncJPTPNetworkProbeStatsFwdScore4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsFwdScore4.setStatus("current")
_F3SyncJPTPNetworkProbeStatsFwdScore3_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsFwdScore3_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsFwdScore3 = _F3SyncJPTPNetworkProbeStatsFwdScore3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 22),
    _F3SyncJPTPNetworkProbeStatsFwdScore3_Type()
)
f3SyncJPTPNetworkProbeStatsFwdScore3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsFwdScore3.setStatus("current")
_F3SyncJPTPNetworkProbeStatsAvgResPDVRev_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsAvgResPDVRev_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsAvgResPDVRev = _F3SyncJPTPNetworkProbeStatsAvgResPDVRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 23),
    _F3SyncJPTPNetworkProbeStatsAvgResPDVRev_Type()
)
f3SyncJPTPNetworkProbeStatsAvgResPDVRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsAvgResPDVRev.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVRevLow_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVRevLow_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVRevLow = _F3SyncJPTPNetworkProbeStatsResPDVRevLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 24),
    _F3SyncJPTPNetworkProbeStatsResPDVRevLow_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVRevLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVRevLow.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVRevMedium_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVRevMedium_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVRevMedium = _F3SyncJPTPNetworkProbeStatsResPDVRevMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 25),
    _F3SyncJPTPNetworkProbeStatsResPDVRevMedium_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVRevMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVRevMedium.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVRevHigh_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVRevHigh_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVRevHigh = _F3SyncJPTPNetworkProbeStatsResPDVRevHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 26),
    _F3SyncJPTPNetworkProbeStatsResPDVRevHigh_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVRevHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVRevHigh.setStatus("current")
_F3SyncJPTPNetworkProbeStatsResPDVRevTotal_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsResPDVRevTotal_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsResPDVRevTotal = _F3SyncJPTPNetworkProbeStatsResPDVRevTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 27),
    _F3SyncJPTPNetworkProbeStatsResPDVRevTotal_Type()
)
f3SyncJPTPNetworkProbeStatsResPDVRevTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsResPDVRevTotal.setStatus("current")
_F3SyncJPTPNetworkProbeStatsRevScore5_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsRevScore5_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsRevScore5 = _F3SyncJPTPNetworkProbeStatsRevScore5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 28),
    _F3SyncJPTPNetworkProbeStatsRevScore5_Type()
)
f3SyncJPTPNetworkProbeStatsRevScore5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsRevScore5.setStatus("current")
_F3SyncJPTPNetworkProbeStatsRevScore4_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsRevScore4_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsRevScore4 = _F3SyncJPTPNetworkProbeStatsRevScore4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 29),
    _F3SyncJPTPNetworkProbeStatsRevScore4_Type()
)
f3SyncJPTPNetworkProbeStatsRevScore4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsRevScore4.setStatus("current")
_F3SyncJPTPNetworkProbeStatsRevScore3_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsRevScore3_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsRevScore3 = _F3SyncJPTPNetworkProbeStatsRevScore3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 30),
    _F3SyncJPTPNetworkProbeStatsRevScore3_Type()
)
f3SyncJPTPNetworkProbeStatsRevScore3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsRevScore3.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMinRPDVFwd_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMinRPDVFwd_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMinRPDVFwd = _F3SyncJPTPNetworkProbeStatsMinRPDVFwd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 31),
    _F3SyncJPTPNetworkProbeStatsMinRPDVFwd_Type()
)
f3SyncJPTPNetworkProbeStatsMinRPDVFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMinRPDVFwd.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMinRPDVRev_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMinRPDVRev_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMinRPDVRev = _F3SyncJPTPNetworkProbeStatsMinRPDVRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 32),
    _F3SyncJPTPNetworkProbeStatsMinRPDVRev_Type()
)
f3SyncJPTPNetworkProbeStatsMinRPDVRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMinRPDVRev.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMinPathAsymmetry_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsMinPathAsymmetry_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMinPathAsymmetry = _F3SyncJPTPNetworkProbeStatsMinPathAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 33),
    _F3SyncJPTPNetworkProbeStatsMinPathAsymmetry_Type()
)
f3SyncJPTPNetworkProbeStatsMinPathAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMinPathAsymmetry.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMaxPathAsymmetry_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsMaxPathAsymmetry_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMaxPathAsymmetry = _F3SyncJPTPNetworkProbeStatsMaxPathAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 34),
    _F3SyncJPTPNetworkProbeStatsMaxPathAsymmetry_Type()
)
f3SyncJPTPNetworkProbeStatsMaxPathAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMaxPathAsymmetry.setStatus("current")
_F3SyncJPTPNetworkProbeStatsAvgPathAsymmetry_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsAvgPathAsymmetry_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsAvgPathAsymmetry = _F3SyncJPTPNetworkProbeStatsAvgPathAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 35),
    _F3SyncJPTPNetworkProbeStatsAvgPathAsymmetry_Type()
)
f3SyncJPTPNetworkProbeStatsAvgPathAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsAvgPathAsymmetry.setStatus("current")
_F3SyncJPTPNetworkProbeStatsPathLossSecondsFwd_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsPathLossSecondsFwd_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsPathLossSecondsFwd = _F3SyncJPTPNetworkProbeStatsPathLossSecondsFwd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 36),
    _F3SyncJPTPNetworkProbeStatsPathLossSecondsFwd_Type()
)
f3SyncJPTPNetworkProbeStatsPathLossSecondsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsPathLossSecondsFwd.setStatus("current")
_F3SyncJPTPNetworkProbeStatsPathLossSecondsRev_Type = Unsigned32
_F3SyncJPTPNetworkProbeStatsPathLossSecondsRev_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsPathLossSecondsRev = _F3SyncJPTPNetworkProbeStatsPathLossSecondsRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 37),
    _F3SyncJPTPNetworkProbeStatsPathLossSecondsRev_Type()
)
f3SyncJPTPNetworkProbeStatsPathLossSecondsRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsPathLossSecondsRev.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay = _F3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 38),
    _F3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay = _F3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 39),
    _F3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay = _F3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 1, 1, 40),
    _F3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay_Type()
)
f3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryTable_Object = MibTable
f3SyncJPTPNetworkProbeHistoryTable = _F3SyncJPTPNetworkProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2)
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryTable.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryEntry_Object = MibTableRow
f3SyncJPTPNetworkProbeHistoryEntry = _F3SyncJPTPNetworkProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1)
)
f3SyncJPTPNetworkProbeHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryEntry.setStatus("current")


class _F3SyncJPTPNetworkProbeHistoryIndex_Type(Integer32):
    """Custom type f3SyncJPTPNetworkProbeHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3SyncJPTPNetworkProbeHistoryIndex_Type.__name__ = "Integer32"
_F3SyncJPTPNetworkProbeHistoryIndex_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryIndex = _F3SyncJPTPNetworkProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 1),
    _F3SyncJPTPNetworkProbeHistoryIndex_Type()
)
f3SyncJPTPNetworkProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryIndex.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryTime_Type = DateAndTime
_F3SyncJPTPNetworkProbeHistoryTime_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryTime = _F3SyncJPTPNetworkProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 2),
    _F3SyncJPTPNetworkProbeHistoryTime_Type()
)
f3SyncJPTPNetworkProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryTime.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryValid_Type = TruthValue
_F3SyncJPTPNetworkProbeHistoryValid_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryValid = _F3SyncJPTPNetworkProbeHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 3),
    _F3SyncJPTPNetworkProbeHistoryValid_Type()
)
f3SyncJPTPNetworkProbeHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryValid.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryAction_Type = CmPmBinAction
_F3SyncJPTPNetworkProbeHistoryAction_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryAction = _F3SyncJPTPNetworkProbeHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 4),
    _F3SyncJPTPNetworkProbeHistoryAction_Type()
)
f3SyncJPTPNetworkProbeHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryAction.setStatus("current")
_F3SyncJPTPNetworkProbeHistorySyncMsgsRx_Type = PerfCounter32
_F3SyncJPTPNetworkProbeHistorySyncMsgsRx_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistorySyncMsgsRx = _F3SyncJPTPNetworkProbeHistorySyncMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 5),
    _F3SyncJPTPNetworkProbeHistorySyncMsgsRx_Type()
)
f3SyncJPTPNetworkProbeHistorySyncMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistorySyncMsgsRx.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx_Type = PerfCounter32
_F3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx = _F3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 6),
    _F3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx_Type()
)
f3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryLostSyncMsgs_Type = PerfCounter32
_F3SyncJPTPNetworkProbeHistoryLostSyncMsgs_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryLostSyncMsgs = _F3SyncJPTPNetworkProbeHistoryLostSyncMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 7),
    _F3SyncJPTPNetworkProbeHistoryLostSyncMsgs_Type()
)
f3SyncJPTPNetworkProbeHistoryLostSyncMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryLostSyncMsgs.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs_Type = PerfCounter32
_F3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs = _F3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 8),
    _F3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs_Type()
)
f3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMinMeanPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMinMeanPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMinMeanPathDelay = _F3SyncJPTPNetworkProbeHistoryMinMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 9),
    _F3SyncJPTPNetworkProbeHistoryMinMeanPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryMinMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMinMeanPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay = _F3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 10),
    _F3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay = _F3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 11),
    _F3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMinSyncPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMinSyncPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMinSyncPathDelay = _F3SyncJPTPNetworkProbeHistoryMinSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 12),
    _F3SyncJPTPNetworkProbeHistoryMinSyncPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryMinSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMinSyncPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay = _F3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 13),
    _F3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay = _F3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 14),
    _F3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryAvgResPDVFwd_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryAvgResPDVFwd_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryAvgResPDVFwd = _F3SyncJPTPNetworkProbeHistoryAvgResPDVFwd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 15),
    _F3SyncJPTPNetworkProbeHistoryAvgResPDVFwd_Type()
)
f3SyncJPTPNetworkProbeHistoryAvgResPDVFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryAvgResPDVFwd.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVFwdLow_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVFwdLow_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVFwdLow = _F3SyncJPTPNetworkProbeHistoryResPDVFwdLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 16),
    _F3SyncJPTPNetworkProbeHistoryResPDVFwdLow_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVFwdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVFwdLow.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVFwdMedium_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVFwdMedium_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVFwdMedium = _F3SyncJPTPNetworkProbeHistoryResPDVFwdMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 17),
    _F3SyncJPTPNetworkProbeHistoryResPDVFwdMedium_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVFwdMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVFwdMedium.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVFwdHigh_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVFwdHigh_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVFwdHigh = _F3SyncJPTPNetworkProbeHistoryResPDVFwdHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 18),
    _F3SyncJPTPNetworkProbeHistoryResPDVFwdHigh_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVFwdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVFwdHigh.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVFwdTotal_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVFwdTotal_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVFwdTotal = _F3SyncJPTPNetworkProbeHistoryResPDVFwdTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 19),
    _F3SyncJPTPNetworkProbeHistoryResPDVFwdTotal_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVFwdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVFwdTotal.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryFwdScore5_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryFwdScore5_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryFwdScore5 = _F3SyncJPTPNetworkProbeHistoryFwdScore5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 20),
    _F3SyncJPTPNetworkProbeHistoryFwdScore5_Type()
)
f3SyncJPTPNetworkProbeHistoryFwdScore5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryFwdScore5.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryFwdScore4_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryFwdScore4_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryFwdScore4 = _F3SyncJPTPNetworkProbeHistoryFwdScore4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 21),
    _F3SyncJPTPNetworkProbeHistoryFwdScore4_Type()
)
f3SyncJPTPNetworkProbeHistoryFwdScore4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryFwdScore4.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryFwdScore3_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryFwdScore3_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryFwdScore3 = _F3SyncJPTPNetworkProbeHistoryFwdScore3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 22),
    _F3SyncJPTPNetworkProbeHistoryFwdScore3_Type()
)
f3SyncJPTPNetworkProbeHistoryFwdScore3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryFwdScore3.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryAvgResPDVRev_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryAvgResPDVRev_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryAvgResPDVRev = _F3SyncJPTPNetworkProbeHistoryAvgResPDVRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 23),
    _F3SyncJPTPNetworkProbeHistoryAvgResPDVRev_Type()
)
f3SyncJPTPNetworkProbeHistoryAvgResPDVRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryAvgResPDVRev.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVRevLow_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVRevLow_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVRevLow = _F3SyncJPTPNetworkProbeHistoryResPDVRevLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 24),
    _F3SyncJPTPNetworkProbeHistoryResPDVRevLow_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVRevLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVRevLow.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVRevMedium_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVRevMedium_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVRevMedium = _F3SyncJPTPNetworkProbeHistoryResPDVRevMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 25),
    _F3SyncJPTPNetworkProbeHistoryResPDVRevMedium_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVRevMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVRevMedium.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVRevHigh_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVRevHigh_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVRevHigh = _F3SyncJPTPNetworkProbeHistoryResPDVRevHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 26),
    _F3SyncJPTPNetworkProbeHistoryResPDVRevHigh_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVRevHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVRevHigh.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryResPDVRevTotal_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryResPDVRevTotal_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryResPDVRevTotal = _F3SyncJPTPNetworkProbeHistoryResPDVRevTotal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 27),
    _F3SyncJPTPNetworkProbeHistoryResPDVRevTotal_Type()
)
f3SyncJPTPNetworkProbeHistoryResPDVRevTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryResPDVRevTotal.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryRevScore5_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryRevScore5_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryRevScore5 = _F3SyncJPTPNetworkProbeHistoryRevScore5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 28),
    _F3SyncJPTPNetworkProbeHistoryRevScore5_Type()
)
f3SyncJPTPNetworkProbeHistoryRevScore5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryRevScore5.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryRevScore4_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryRevScore4_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryRevScore4 = _F3SyncJPTPNetworkProbeHistoryRevScore4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 29),
    _F3SyncJPTPNetworkProbeHistoryRevScore4_Type()
)
f3SyncJPTPNetworkProbeHistoryRevScore4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryRevScore4.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryRevScore3_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryRevScore3_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryRevScore3 = _F3SyncJPTPNetworkProbeHistoryRevScore3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 30),
    _F3SyncJPTPNetworkProbeHistoryRevScore3_Type()
)
f3SyncJPTPNetworkProbeHistoryRevScore3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryRevScore3.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMinRPDVFwd_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMinRPDVFwd_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMinRPDVFwd = _F3SyncJPTPNetworkProbeHistoryMinRPDVFwd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 31),
    _F3SyncJPTPNetworkProbeHistoryMinRPDVFwd_Type()
)
f3SyncJPTPNetworkProbeHistoryMinRPDVFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMinRPDVFwd.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMinRPDVRev_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMinRPDVRev_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMinRPDVRev = _F3SyncJPTPNetworkProbeHistoryMinRPDVRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 32),
    _F3SyncJPTPNetworkProbeHistoryMinRPDVRev_Type()
)
f3SyncJPTPNetworkProbeHistoryMinRPDVRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMinRPDVRev.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMinPathAsymmetry_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryMinPathAsymmetry_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMinPathAsymmetry = _F3SyncJPTPNetworkProbeHistoryMinPathAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 33),
    _F3SyncJPTPNetworkProbeHistoryMinPathAsymmetry_Type()
)
f3SyncJPTPNetworkProbeHistoryMinPathAsymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMinPathAsymmetry.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry = _F3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 34),
    _F3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry_Type()
)
f3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry_Type = Unsigned32
_F3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry = _F3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 35),
    _F3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry_Type()
)
f3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay = _F3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 36),
    _F3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay = _F3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 37),
    _F3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay_Type = ScaledNanoseconds
_F3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay_Object = MibTableColumn
f3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay = _F3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 2, 1, 38),
    _F3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay_Type()
)
f3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay.setStatus("current")
_F3SyncJPTPNetworkProbeThresholdTable_Object = MibTable
f3SyncJPTPNetworkProbeThresholdTable = _F3SyncJPTPNetworkProbeThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3)
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdTable.setStatus("current")
_F3SyncJPTPNetworkProbeThresholdEntry_Object = MibTableRow
f3SyncJPTPNetworkProbeThresholdEntry = _F3SyncJPTPNetworkProbeThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3, 1)
)
f3SyncJPTPNetworkProbeThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdEntry.setStatus("current")


class _F3SyncJPTPNetworkProbeThresholdIndex_Type(Integer32):
    """Custom type f3SyncJPTPNetworkProbeThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3SyncJPTPNetworkProbeThresholdIndex_Type.__name__ = "Integer32"
_F3SyncJPTPNetworkProbeThresholdIndex_Object = MibTableColumn
f3SyncJPTPNetworkProbeThresholdIndex = _F3SyncJPTPNetworkProbeThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3, 1, 1),
    _F3SyncJPTPNetworkProbeThresholdIndex_Type()
)
f3SyncJPTPNetworkProbeThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdIndex.setStatus("current")
_F3SyncJPTPNetworkProbeThresholdInterval_Type = CmPmIntervalType
_F3SyncJPTPNetworkProbeThresholdInterval_Object = MibTableColumn
f3SyncJPTPNetworkProbeThresholdInterval = _F3SyncJPTPNetworkProbeThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3, 1, 2),
    _F3SyncJPTPNetworkProbeThresholdInterval_Type()
)
f3SyncJPTPNetworkProbeThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdInterval.setStatus("current")
_F3SyncJPTPNetworkProbeThresholdVariable_Type = VariablePointer
_F3SyncJPTPNetworkProbeThresholdVariable_Object = MibTableColumn
f3SyncJPTPNetworkProbeThresholdVariable = _F3SyncJPTPNetworkProbeThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3, 1, 3),
    _F3SyncJPTPNetworkProbeThresholdVariable_Type()
)
f3SyncJPTPNetworkProbeThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdVariable.setStatus("current")
_F3SyncJPTPNetworkProbeThresholdValueLo_Type = Unsigned32
_F3SyncJPTPNetworkProbeThresholdValueLo_Object = MibTableColumn
f3SyncJPTPNetworkProbeThresholdValueLo = _F3SyncJPTPNetworkProbeThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3, 1, 4),
    _F3SyncJPTPNetworkProbeThresholdValueLo_Type()
)
f3SyncJPTPNetworkProbeThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdValueLo.setStatus("current")
_F3SyncJPTPNetworkProbeThresholdValueHi_Type = Unsigned32
_F3SyncJPTPNetworkProbeThresholdValueHi_Object = MibTableColumn
f3SyncJPTPNetworkProbeThresholdValueHi = _F3SyncJPTPNetworkProbeThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3, 1, 5),
    _F3SyncJPTPNetworkProbeThresholdValueHi_Type()
)
f3SyncJPTPNetworkProbeThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdValueHi.setStatus("current")
_F3SyncJPTPNetworkProbeThresholdMonValue_Type = PerfCounter64
_F3SyncJPTPNetworkProbeThresholdMonValue_Object = MibTableColumn
f3SyncJPTPNetworkProbeThresholdMonValue = _F3SyncJPTPNetworkProbeThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 3, 1, 6),
    _F3SyncJPTPNetworkProbeThresholdMonValue_Type()
)
f3SyncJPTPNetworkProbeThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdMonValue.setStatus("current")
_F3SyncJClockProbeStatsTable_Object = MibTable
f3SyncJClockProbeStatsTable = _F3SyncJClockProbeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4)
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsTable.setStatus("current")
_F3SyncJClockProbeStatsEntry_Object = MibTableRow
f3SyncJClockProbeStatsEntry = _F3SyncJClockProbeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1)
)
f3SyncJClockProbeStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsEntry.setStatus("current")


class _F3SyncJClockProbeStatsIndex_Type(Integer32):
    """Custom type f3SyncJClockProbeStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_F3SyncJClockProbeStatsIndex_Type.__name__ = "Integer32"
_F3SyncJClockProbeStatsIndex_Object = MibTableColumn
f3SyncJClockProbeStatsIndex = _F3SyncJClockProbeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 1),
    _F3SyncJClockProbeStatsIndex_Type()
)
f3SyncJClockProbeStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsIndex.setStatus("current")
_F3SyncJClockProbeStatsIntervalType_Type = CmPmIntervalType
_F3SyncJClockProbeStatsIntervalType_Object = MibTableColumn
f3SyncJClockProbeStatsIntervalType = _F3SyncJClockProbeStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 2),
    _F3SyncJClockProbeStatsIntervalType_Type()
)
f3SyncJClockProbeStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsIntervalType.setStatus("current")
_F3SyncJClockProbeStatsValid_Type = TruthValue
_F3SyncJClockProbeStatsValid_Object = MibTableColumn
f3SyncJClockProbeStatsValid = _F3SyncJClockProbeStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 3),
    _F3SyncJClockProbeStatsValid_Type()
)
f3SyncJClockProbeStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsValid.setStatus("current")
_F3SyncJClockProbeStatsAction_Type = CmPmBinAction
_F3SyncJClockProbeStatsAction_Object = MibTableColumn
f3SyncJClockProbeStatsAction = _F3SyncJClockProbeStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 4),
    _F3SyncJClockProbeStatsAction_Type()
)
f3SyncJClockProbeStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsAction.setStatus("current")
_F3SyncJClockProbeStatsMTIE1s_Type = Unsigned32
_F3SyncJClockProbeStatsMTIE1s_Object = MibTableColumn
f3SyncJClockProbeStatsMTIE1s = _F3SyncJClockProbeStatsMTIE1s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 5),
    _F3SyncJClockProbeStatsMTIE1s_Type()
)
f3SyncJClockProbeStatsMTIE1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMTIE1s.setStatus("current")
_F3SyncJClockProbeStatsMTIE10s_Type = Unsigned32
_F3SyncJClockProbeStatsMTIE10s_Object = MibTableColumn
f3SyncJClockProbeStatsMTIE10s = _F3SyncJClockProbeStatsMTIE10s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 6),
    _F3SyncJClockProbeStatsMTIE10s_Type()
)
f3SyncJClockProbeStatsMTIE10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMTIE10s.setStatus("current")
_F3SyncJClockProbeStatsMTIE100s_Type = Unsigned32
_F3SyncJClockProbeStatsMTIE100s_Object = MibTableColumn
f3SyncJClockProbeStatsMTIE100s = _F3SyncJClockProbeStatsMTIE100s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 7),
    _F3SyncJClockProbeStatsMTIE100s_Type()
)
f3SyncJClockProbeStatsMTIE100s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMTIE100s.setStatus("current")
_F3SyncJClockProbeStatsMTIE1000s_Type = Unsigned32
_F3SyncJClockProbeStatsMTIE1000s_Object = MibTableColumn
f3SyncJClockProbeStatsMTIE1000s = _F3SyncJClockProbeStatsMTIE1000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 8),
    _F3SyncJClockProbeStatsMTIE1000s_Type()
)
f3SyncJClockProbeStatsMTIE1000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMTIE1000s.setStatus("current")
_F3SyncJClockProbeStatsMTIE10000s_Type = Unsigned32
_F3SyncJClockProbeStatsMTIE10000s_Object = MibTableColumn
f3SyncJClockProbeStatsMTIE10000s = _F3SyncJClockProbeStatsMTIE10000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 9),
    _F3SyncJClockProbeStatsMTIE10000s_Type()
)
f3SyncJClockProbeStatsMTIE10000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMTIE10000s.setStatus("current")
_F3SyncJClockProbeStatsMTIE50000s_Type = Unsigned32
_F3SyncJClockProbeStatsMTIE50000s_Object = MibTableColumn
f3SyncJClockProbeStatsMTIE50000s = _F3SyncJClockProbeStatsMTIE50000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 10),
    _F3SyncJClockProbeStatsMTIE50000s_Type()
)
f3SyncJClockProbeStatsMTIE50000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMTIE50000s.setStatus("current")
_F3SyncJClockProbeStatsMaxTE_Type = Integer32
_F3SyncJClockProbeStatsMaxTE_Object = MibTableColumn
f3SyncJClockProbeStatsMaxTE = _F3SyncJClockProbeStatsMaxTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 11),
    _F3SyncJClockProbeStatsMaxTE_Type()
)
f3SyncJClockProbeStatsMaxTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMaxTE.setStatus("current")
_F3SyncJClockProbeStatsMaxConstTE_Type = Integer32
_F3SyncJClockProbeStatsMaxConstTE_Object = MibTableColumn
f3SyncJClockProbeStatsMaxConstTE = _F3SyncJClockProbeStatsMaxConstTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 4, 1, 12),
    _F3SyncJClockProbeStatsMaxConstTE_Type()
)
f3SyncJClockProbeStatsMaxConstTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatsMaxConstTE.setStatus("current")
_F3SyncJClockProbeHistoryTable_Object = MibTable
f3SyncJClockProbeHistoryTable = _F3SyncJClockProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5)
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryTable.setStatus("current")
_F3SyncJClockProbeHistoryEntry_Object = MibTableRow
f3SyncJClockProbeHistoryEntry = _F3SyncJClockProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1)
)
f3SyncJClockProbeHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryEntry.setStatus("current")


class _F3SyncJClockProbeHistoryIndex_Type(Integer32):
    """Custom type f3SyncJClockProbeHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3SyncJClockProbeHistoryIndex_Type.__name__ = "Integer32"
_F3SyncJClockProbeHistoryIndex_Object = MibTableColumn
f3SyncJClockProbeHistoryIndex = _F3SyncJClockProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 1),
    _F3SyncJClockProbeHistoryIndex_Type()
)
f3SyncJClockProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryIndex.setStatus("current")
_F3SyncJClockProbeHistoryTime_Type = DateAndTime
_F3SyncJClockProbeHistoryTime_Object = MibTableColumn
f3SyncJClockProbeHistoryTime = _F3SyncJClockProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 2),
    _F3SyncJClockProbeHistoryTime_Type()
)
f3SyncJClockProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryTime.setStatus("current")
_F3SyncJClockProbeHistoryValid_Type = TruthValue
_F3SyncJClockProbeHistoryValid_Object = MibTableColumn
f3SyncJClockProbeHistoryValid = _F3SyncJClockProbeHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 3),
    _F3SyncJClockProbeHistoryValid_Type()
)
f3SyncJClockProbeHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryValid.setStatus("current")
_F3SyncJClockProbeHistoryAction_Type = CmPmBinAction
_F3SyncJClockProbeHistoryAction_Object = MibTableColumn
f3SyncJClockProbeHistoryAction = _F3SyncJClockProbeHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 4),
    _F3SyncJClockProbeHistoryAction_Type()
)
f3SyncJClockProbeHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryAction.setStatus("current")
_F3SyncJClockProbeHistoryMTIE1s_Type = Unsigned32
_F3SyncJClockProbeHistoryMTIE1s_Object = MibTableColumn
f3SyncJClockProbeHistoryMTIE1s = _F3SyncJClockProbeHistoryMTIE1s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 5),
    _F3SyncJClockProbeHistoryMTIE1s_Type()
)
f3SyncJClockProbeHistoryMTIE1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMTIE1s.setStatus("current")
_F3SyncJClockProbeHistoryMTIE10s_Type = Unsigned32
_F3SyncJClockProbeHistoryMTIE10s_Object = MibTableColumn
f3SyncJClockProbeHistoryMTIE10s = _F3SyncJClockProbeHistoryMTIE10s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 6),
    _F3SyncJClockProbeHistoryMTIE10s_Type()
)
f3SyncJClockProbeHistoryMTIE10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMTIE10s.setStatus("current")
_F3SyncJClockProbeHistoryMTIE100s_Type = Unsigned32
_F3SyncJClockProbeHistoryMTIE100s_Object = MibTableColumn
f3SyncJClockProbeHistoryMTIE100s = _F3SyncJClockProbeHistoryMTIE100s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 7),
    _F3SyncJClockProbeHistoryMTIE100s_Type()
)
f3SyncJClockProbeHistoryMTIE100s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMTIE100s.setStatus("current")
_F3SyncJClockProbeHistoryMTIE1000s_Type = Unsigned32
_F3SyncJClockProbeHistoryMTIE1000s_Object = MibTableColumn
f3SyncJClockProbeHistoryMTIE1000s = _F3SyncJClockProbeHistoryMTIE1000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 8),
    _F3SyncJClockProbeHistoryMTIE1000s_Type()
)
f3SyncJClockProbeHistoryMTIE1000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMTIE1000s.setStatus("current")
_F3SyncJClockProbeHistoryMTIE10000s_Type = Unsigned32
_F3SyncJClockProbeHistoryMTIE10000s_Object = MibTableColumn
f3SyncJClockProbeHistoryMTIE10000s = _F3SyncJClockProbeHistoryMTIE10000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 9),
    _F3SyncJClockProbeHistoryMTIE10000s_Type()
)
f3SyncJClockProbeHistoryMTIE10000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMTIE10000s.setStatus("current")
_F3SyncJClockProbeHistoryMTIE50000s_Type = Unsigned32
_F3SyncJClockProbeHistoryMTIE50000s_Object = MibTableColumn
f3SyncJClockProbeHistoryMTIE50000s = _F3SyncJClockProbeHistoryMTIE50000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 10),
    _F3SyncJClockProbeHistoryMTIE50000s_Type()
)
f3SyncJClockProbeHistoryMTIE50000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMTIE50000s.setStatus("current")
_F3SyncJClockProbeHistoryMaxTE_Type = Integer32
_F3SyncJClockProbeHistoryMaxTE_Object = MibTableColumn
f3SyncJClockProbeHistoryMaxTE = _F3SyncJClockProbeHistoryMaxTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 11),
    _F3SyncJClockProbeHistoryMaxTE_Type()
)
f3SyncJClockProbeHistoryMaxTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMaxTE.setStatus("current")
_F3SyncJClockProbeHistoryMaxConstTE_Type = Integer32
_F3SyncJClockProbeHistoryMaxConstTE_Object = MibTableColumn
f3SyncJClockProbeHistoryMaxConstTE = _F3SyncJClockProbeHistoryMaxConstTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 5, 1, 12),
    _F3SyncJClockProbeHistoryMaxConstTE_Type()
)
f3SyncJClockProbeHistoryMaxConstTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeHistoryMaxConstTE.setStatus("current")
_F3SyncJClockProbeThresholdTable_Object = MibTable
f3SyncJClockProbeThresholdTable = _F3SyncJClockProbeThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6)
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdTable.setStatus("current")
_F3SyncJClockProbeThresholdEntry_Object = MibTableRow
f3SyncJClockProbeThresholdEntry = _F3SyncJClockProbeThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6, 1)
)
f3SyncJClockProbeThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdEntry.setStatus("current")


class _F3SyncJClockProbeThresholdIndex_Type(Integer32):
    """Custom type f3SyncJClockProbeThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3SyncJClockProbeThresholdIndex_Type.__name__ = "Integer32"
_F3SyncJClockProbeThresholdIndex_Object = MibTableColumn
f3SyncJClockProbeThresholdIndex = _F3SyncJClockProbeThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6, 1, 1),
    _F3SyncJClockProbeThresholdIndex_Type()
)
f3SyncJClockProbeThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdIndex.setStatus("current")
_F3SyncJClockProbeThresholdInterval_Type = CmPmIntervalType
_F3SyncJClockProbeThresholdInterval_Object = MibTableColumn
f3SyncJClockProbeThresholdInterval = _F3SyncJClockProbeThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6, 1, 2),
    _F3SyncJClockProbeThresholdInterval_Type()
)
f3SyncJClockProbeThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdInterval.setStatus("current")
_F3SyncJClockProbeThresholdVariable_Type = VariablePointer
_F3SyncJClockProbeThresholdVariable_Object = MibTableColumn
f3SyncJClockProbeThresholdVariable = _F3SyncJClockProbeThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6, 1, 3),
    _F3SyncJClockProbeThresholdVariable_Type()
)
f3SyncJClockProbeThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdVariable.setStatus("current")
_F3SyncJClockProbeThresholdValueLo_Type = Unsigned32
_F3SyncJClockProbeThresholdValueLo_Object = MibTableColumn
f3SyncJClockProbeThresholdValueLo = _F3SyncJClockProbeThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6, 1, 4),
    _F3SyncJClockProbeThresholdValueLo_Type()
)
f3SyncJClockProbeThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdValueLo.setStatus("current")
_F3SyncJClockProbeThresholdValueHi_Type = Unsigned32
_F3SyncJClockProbeThresholdValueHi_Object = MibTableColumn
f3SyncJClockProbeThresholdValueHi = _F3SyncJClockProbeThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6, 1, 5),
    _F3SyncJClockProbeThresholdValueHi_Type()
)
f3SyncJClockProbeThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdValueHi.setStatus("current")
_F3SyncJClockProbeThresholdMonValue_Type = PerfCounter64
_F3SyncJClockProbeThresholdMonValue_Object = MibTableColumn
f3SyncJClockProbeThresholdMonValue = _F3SyncJClockProbeThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 6, 1, 6),
    _F3SyncJClockProbeThresholdMonValue_Type()
)
f3SyncJClockProbeThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdMonValue.setStatus("current")
_F3SyncJPTPClockProbeStatsTable_Object = MibTable
f3SyncJPTPClockProbeStatsTable = _F3SyncJPTPClockProbeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7)
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsTable.setStatus("current")
_F3SyncJPTPClockProbeStatsEntry_Object = MibTableRow
f3SyncJPTPClockProbeStatsEntry = _F3SyncJPTPClockProbeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1)
)
f3SyncJPTPClockProbeStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsEntry.setStatus("current")


class _F3SyncJPTPClockProbeStatsIndex_Type(Integer32):
    """Custom type f3SyncJPTPClockProbeStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_F3SyncJPTPClockProbeStatsIndex_Type.__name__ = "Integer32"
_F3SyncJPTPClockProbeStatsIndex_Object = MibTableColumn
f3SyncJPTPClockProbeStatsIndex = _F3SyncJPTPClockProbeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 1),
    _F3SyncJPTPClockProbeStatsIndex_Type()
)
f3SyncJPTPClockProbeStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsIndex.setStatus("current")
_F3SyncJPTPClockProbeStatsIntervalType_Type = CmPmIntervalType
_F3SyncJPTPClockProbeStatsIntervalType_Object = MibTableColumn
f3SyncJPTPClockProbeStatsIntervalType = _F3SyncJPTPClockProbeStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 2),
    _F3SyncJPTPClockProbeStatsIntervalType_Type()
)
f3SyncJPTPClockProbeStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsIntervalType.setStatus("current")
_F3SyncJPTPClockProbeStatsValid_Type = TruthValue
_F3SyncJPTPClockProbeStatsValid_Object = MibTableColumn
f3SyncJPTPClockProbeStatsValid = _F3SyncJPTPClockProbeStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 3),
    _F3SyncJPTPClockProbeStatsValid_Type()
)
f3SyncJPTPClockProbeStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsValid.setStatus("current")
_F3SyncJPTPClockProbeStatsAction_Type = CmPmBinAction
_F3SyncJPTPClockProbeStatsAction_Object = MibTableColumn
f3SyncJPTPClockProbeStatsAction = _F3SyncJPTPClockProbeStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 4),
    _F3SyncJPTPClockProbeStatsAction_Type()
)
f3SyncJPTPClockProbeStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsAction.setStatus("current")
_F3SyncJPTPClockProbeStatsMTIE1s_Type = Unsigned32
_F3SyncJPTPClockProbeStatsMTIE1s_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMTIE1s = _F3SyncJPTPClockProbeStatsMTIE1s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 5),
    _F3SyncJPTPClockProbeStatsMTIE1s_Type()
)
f3SyncJPTPClockProbeStatsMTIE1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMTIE1s.setStatus("current")
_F3SyncJPTPClockProbeStatsMTIE10s_Type = Unsigned32
_F3SyncJPTPClockProbeStatsMTIE10s_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMTIE10s = _F3SyncJPTPClockProbeStatsMTIE10s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 6),
    _F3SyncJPTPClockProbeStatsMTIE10s_Type()
)
f3SyncJPTPClockProbeStatsMTIE10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMTIE10s.setStatus("current")
_F3SyncJPTPClockProbeStatsMTIE100s_Type = Unsigned32
_F3SyncJPTPClockProbeStatsMTIE100s_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMTIE100s = _F3SyncJPTPClockProbeStatsMTIE100s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 7),
    _F3SyncJPTPClockProbeStatsMTIE100s_Type()
)
f3SyncJPTPClockProbeStatsMTIE100s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMTIE100s.setStatus("current")
_F3SyncJPTPClockProbeStatsMTIE1000s_Type = Unsigned32
_F3SyncJPTPClockProbeStatsMTIE1000s_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMTIE1000s = _F3SyncJPTPClockProbeStatsMTIE1000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 8),
    _F3SyncJPTPClockProbeStatsMTIE1000s_Type()
)
f3SyncJPTPClockProbeStatsMTIE1000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMTIE1000s.setStatus("current")
_F3SyncJPTPClockProbeStatsMTIE10000s_Type = Unsigned32
_F3SyncJPTPClockProbeStatsMTIE10000s_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMTIE10000s = _F3SyncJPTPClockProbeStatsMTIE10000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 9),
    _F3SyncJPTPClockProbeStatsMTIE10000s_Type()
)
f3SyncJPTPClockProbeStatsMTIE10000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMTIE10000s.setStatus("current")
_F3SyncJPTPClockProbeStatsMTIE50000s_Type = Unsigned32
_F3SyncJPTPClockProbeStatsMTIE50000s_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMTIE50000s = _F3SyncJPTPClockProbeStatsMTIE50000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 10),
    _F3SyncJPTPClockProbeStatsMTIE50000s_Type()
)
f3SyncJPTPClockProbeStatsMTIE50000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMTIE50000s.setStatus("current")
_F3SyncJPTPClockProbeStatsMaxTE_Type = Integer32
_F3SyncJPTPClockProbeStatsMaxTE_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMaxTE = _F3SyncJPTPClockProbeStatsMaxTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 11),
    _F3SyncJPTPClockProbeStatsMaxTE_Type()
)
f3SyncJPTPClockProbeStatsMaxTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMaxTE.setStatus("current")
_F3SyncJPTPClockProbeStatsMaxConstTE_Type = Integer32
_F3SyncJPTPClockProbeStatsMaxConstTE_Object = MibTableColumn
f3SyncJPTPClockProbeStatsMaxConstTE = _F3SyncJPTPClockProbeStatsMaxConstTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 7, 1, 12),
    _F3SyncJPTPClockProbeStatsMaxConstTE_Type()
)
f3SyncJPTPClockProbeStatsMaxConstTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatsMaxConstTE.setStatus("current")
_F3SyncJPTPClockProbeHistoryTable_Object = MibTable
f3SyncJPTPClockProbeHistoryTable = _F3SyncJPTPClockProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8)
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryTable.setStatus("current")
_F3SyncJPTPClockProbeHistoryEntry_Object = MibTableRow
f3SyncJPTPClockProbeHistoryEntry = _F3SyncJPTPClockProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1)
)
f3SyncJPTPClockProbeHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryEntry.setStatus("current")


class _F3SyncJPTPClockProbeHistoryIndex_Type(Integer32):
    """Custom type f3SyncJPTPClockProbeHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3SyncJPTPClockProbeHistoryIndex_Type.__name__ = "Integer32"
_F3SyncJPTPClockProbeHistoryIndex_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryIndex = _F3SyncJPTPClockProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 1),
    _F3SyncJPTPClockProbeHistoryIndex_Type()
)
f3SyncJPTPClockProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryIndex.setStatus("current")
_F3SyncJPTPClockProbeHistoryTime_Type = DateAndTime
_F3SyncJPTPClockProbeHistoryTime_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryTime = _F3SyncJPTPClockProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 2),
    _F3SyncJPTPClockProbeHistoryTime_Type()
)
f3SyncJPTPClockProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryTime.setStatus("current")
_F3SyncJPTPClockProbeHistoryValid_Type = TruthValue
_F3SyncJPTPClockProbeHistoryValid_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryValid = _F3SyncJPTPClockProbeHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 3),
    _F3SyncJPTPClockProbeHistoryValid_Type()
)
f3SyncJPTPClockProbeHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryValid.setStatus("current")
_F3SyncJPTPClockProbeHistoryAction_Type = CmPmBinAction
_F3SyncJPTPClockProbeHistoryAction_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryAction = _F3SyncJPTPClockProbeHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 4),
    _F3SyncJPTPClockProbeHistoryAction_Type()
)
f3SyncJPTPClockProbeHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryAction.setStatus("current")
_F3SyncJPTPClockProbeHistoryMTIE1s_Type = Unsigned32
_F3SyncJPTPClockProbeHistoryMTIE1s_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMTIE1s = _F3SyncJPTPClockProbeHistoryMTIE1s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 5),
    _F3SyncJPTPClockProbeHistoryMTIE1s_Type()
)
f3SyncJPTPClockProbeHistoryMTIE1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMTIE1s.setStatus("current")
_F3SyncJPTPClockProbeHistoryMTIE10s_Type = Unsigned32
_F3SyncJPTPClockProbeHistoryMTIE10s_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMTIE10s = _F3SyncJPTPClockProbeHistoryMTIE10s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 6),
    _F3SyncJPTPClockProbeHistoryMTIE10s_Type()
)
f3SyncJPTPClockProbeHistoryMTIE10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMTIE10s.setStatus("current")
_F3SyncJPTPClockProbeHistoryMTIE100s_Type = Unsigned32
_F3SyncJPTPClockProbeHistoryMTIE100s_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMTIE100s = _F3SyncJPTPClockProbeHistoryMTIE100s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 7),
    _F3SyncJPTPClockProbeHistoryMTIE100s_Type()
)
f3SyncJPTPClockProbeHistoryMTIE100s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMTIE100s.setStatus("current")
_F3SyncJPTPClockProbeHistoryMTIE1000s_Type = Unsigned32
_F3SyncJPTPClockProbeHistoryMTIE1000s_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMTIE1000s = _F3SyncJPTPClockProbeHistoryMTIE1000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 8),
    _F3SyncJPTPClockProbeHistoryMTIE1000s_Type()
)
f3SyncJPTPClockProbeHistoryMTIE1000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMTIE1000s.setStatus("current")
_F3SyncJPTPClockProbeHistoryMTIE10000s_Type = Unsigned32
_F3SyncJPTPClockProbeHistoryMTIE10000s_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMTIE10000s = _F3SyncJPTPClockProbeHistoryMTIE10000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 9),
    _F3SyncJPTPClockProbeHistoryMTIE10000s_Type()
)
f3SyncJPTPClockProbeHistoryMTIE10000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMTIE10000s.setStatus("current")
_F3SyncJPTPClockProbeHistoryMTIE50000s_Type = Unsigned32
_F3SyncJPTPClockProbeHistoryMTIE50000s_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMTIE50000s = _F3SyncJPTPClockProbeHistoryMTIE50000s_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 10),
    _F3SyncJPTPClockProbeHistoryMTIE50000s_Type()
)
f3SyncJPTPClockProbeHistoryMTIE50000s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMTIE50000s.setStatus("current")
_F3SyncJPTPClockProbeHistoryMaxTE_Type = Integer32
_F3SyncJPTPClockProbeHistoryMaxTE_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMaxTE = _F3SyncJPTPClockProbeHistoryMaxTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 11),
    _F3SyncJPTPClockProbeHistoryMaxTE_Type()
)
f3SyncJPTPClockProbeHistoryMaxTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMaxTE.setStatus("current")
_F3SyncJPTPClockProbeHistoryMaxConstTE_Type = Integer32
_F3SyncJPTPClockProbeHistoryMaxConstTE_Object = MibTableColumn
f3SyncJPTPClockProbeHistoryMaxConstTE = _F3SyncJPTPClockProbeHistoryMaxConstTE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 8, 1, 12),
    _F3SyncJPTPClockProbeHistoryMaxConstTE_Type()
)
f3SyncJPTPClockProbeHistoryMaxConstTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeHistoryMaxConstTE.setStatus("current")
_F3SyncJPTPClockProbeThresholdTable_Object = MibTable
f3SyncJPTPClockProbeThresholdTable = _F3SyncJPTPClockProbeThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9)
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdTable.setStatus("current")
_F3SyncJPTPClockProbeThresholdEntry_Object = MibTableRow
f3SyncJPTPClockProbeThresholdEntry = _F3SyncJPTPClockProbeThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9, 1)
)
f3SyncJPTPClockProbeThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsIndex"),
    (0, "F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdEntry.setStatus("current")


class _F3SyncJPTPClockProbeThresholdIndex_Type(Integer32):
    """Custom type f3SyncJPTPClockProbeThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3SyncJPTPClockProbeThresholdIndex_Type.__name__ = "Integer32"
_F3SyncJPTPClockProbeThresholdIndex_Object = MibTableColumn
f3SyncJPTPClockProbeThresholdIndex = _F3SyncJPTPClockProbeThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9, 1, 1),
    _F3SyncJPTPClockProbeThresholdIndex_Type()
)
f3SyncJPTPClockProbeThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdIndex.setStatus("current")
_F3SyncJPTPClockProbeThresholdInterval_Type = CmPmIntervalType
_F3SyncJPTPClockProbeThresholdInterval_Object = MibTableColumn
f3SyncJPTPClockProbeThresholdInterval = _F3SyncJPTPClockProbeThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9, 1, 2),
    _F3SyncJPTPClockProbeThresholdInterval_Type()
)
f3SyncJPTPClockProbeThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdInterval.setStatus("current")
_F3SyncJPTPClockProbeThresholdVariable_Type = VariablePointer
_F3SyncJPTPClockProbeThresholdVariable_Object = MibTableColumn
f3SyncJPTPClockProbeThresholdVariable = _F3SyncJPTPClockProbeThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9, 1, 3),
    _F3SyncJPTPClockProbeThresholdVariable_Type()
)
f3SyncJPTPClockProbeThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdVariable.setStatus("current")
_F3SyncJPTPClockProbeThresholdValueLo_Type = Unsigned32
_F3SyncJPTPClockProbeThresholdValueLo_Object = MibTableColumn
f3SyncJPTPClockProbeThresholdValueLo = _F3SyncJPTPClockProbeThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9, 1, 4),
    _F3SyncJPTPClockProbeThresholdValueLo_Type()
)
f3SyncJPTPClockProbeThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdValueLo.setStatus("current")
_F3SyncJPTPClockProbeThresholdValueHi_Type = Unsigned32
_F3SyncJPTPClockProbeThresholdValueHi_Object = MibTableColumn
f3SyncJPTPClockProbeThresholdValueHi = _F3SyncJPTPClockProbeThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9, 1, 5),
    _F3SyncJPTPClockProbeThresholdValueHi_Type()
)
f3SyncJPTPClockProbeThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdValueHi.setStatus("current")
_F3SyncJPTPClockProbeThresholdMonValue_Type = PerfCounter64
_F3SyncJPTPClockProbeThresholdMonValue_Object = MibTableColumn
f3SyncJPTPClockProbeThresholdMonValue = _F3SyncJPTPClockProbeThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 2, 9, 1, 6),
    _F3SyncJPTPClockProbeThresholdMonValue_Type()
)
f3SyncJPTPClockProbeThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdMonValue.setStatus("current")
_F3SyncJNotifications_ObjectIdentity = ObjectIdentity
f3SyncJNotifications = _F3SyncJNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 3)
)
_F3SyncJConformance_ObjectIdentity = ObjectIdentity
f3SyncJConformance = _F3SyncJConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 4)
)
_F3SyncJCompliances_ObjectIdentity = ObjectIdentity
f3SyncJCompliances = _F3SyncJCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 4, 1)
)
_F3SyncJGroups_ObjectIdentity = ObjectIdentity
f3SyncJGroups = _F3SyncJGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 4, 2)
)

# Managed Objects groups

f3SyncJObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 4, 2, 1)
)
f3SyncJObjectGroup.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJClockProbeIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeName"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeSource"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeReference"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeExpectedQL"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeSourceType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMeasurementRate"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMTIEMaskType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMTIEMaskMargin"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeScheduler"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeTestState"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeLastTIEResult"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeLastTIEResultTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeSourceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeActualTestStartTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeActualTestDuration"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMTIEMaskCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMTIEMaskMarginCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStorageType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeRowStatus"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeFfoTarget"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeFfoObserWindow"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeLastFFOResult"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeTimeOfLastFFOResult"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeRawDataCollectionEnabled"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeTeAlertThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeTeAlertClearThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeLastTEAlertTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeLastTEAlertClearTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeRunningFailedCount"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMeasurementType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeConstTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeConstTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeConstTEWindow"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMaxTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeConstTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeConstTEMeasurementTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMaxTEMeasurementTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMaxTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMaxTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeMTIERestart"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryAlias"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistorySource"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryReference"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryExpectedQL"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistorySourceType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMeasurementRate"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMTIEMaskType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMTIEMaskMargin"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistorySourceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryActualTestStartTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryActualTestDuration"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMTIEMaskCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryStatusMTIEMaskFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryStatusMTIEMarginFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryStorageType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryRowStatus"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMinFFO"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMaxFFO"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryAvgFFO"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryOutOfTargetFFOTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryTotalFFOTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMinPhaseOffset"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMaxPhaseOffset"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryAvgPhaseOffset"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryTotalPhaseOffsetTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMeasurementType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryTeAlertThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryTeAlertClearThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryLastTEAlertTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryLastTEAlertClearTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryRunningFailedCount"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryConstTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryConstTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryConstTEWindow"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMaxTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryConstTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMTIEValueIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMTIEValue"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryConstTEMeasurementTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMaxTEMeasurementTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMaxTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeResHistoryMaxTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeName"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMeasurementDirection"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbePTPFlowPoint"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeIpPrototocol"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeSlaveIpV4Address"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMasterIpV4Address"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeReference"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeExpectedQL"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMTIEMaskType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMTIEMaskMargin"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeScheduler"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeTestState"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeLastTIEResult"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeLastTIEResultTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeNoTimestampFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeNoEventMessageFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeActualTestStartTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeActualTestDuration"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMTIEMaskCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMTIEMaskMarginCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatusMTIEMaskFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatusMTIEMarginFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStorageType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeRowStatus"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeFfoTarget"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeFfoObserWindow"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeLastFFOResult"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeTimeOfLastFFOResult"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeRawDataCollectionEnabled"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeTeAlertThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeTeAlertClearThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeLastTEAlertTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeLastTEAlertClearTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeRunningFailedCount"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMeasurementType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeDelayMS"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeDelaySM"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeTAsymmetry"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeDelayCompensation"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeConstTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeConstTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeConstTEWindow"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeInstTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeInstTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMaxTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeConstTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeInstTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeSlavePortIdentity"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMasterPortIdentity"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeMTIERestart"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryAlias"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMeasurementDirection"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryPTPFlowPoint"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryIpPrototocol"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistorySlaveIpV4Address"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMasterIpV4Address"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryReference"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryExpectedQL"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMTIEMaskType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMTIEMaskMargin"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryNoTimestampFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryNoEventMessageFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryActualTestStartTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryActualTestDuration"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryStorageType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryRowStatus"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMinFFO"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMaxFFO"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryAvgFFO"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryTotalFFOTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMinPhaseOffset"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMaxPhaseOffset"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryAvgPhaseOffset"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryTeAlertThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryTeAlertClearThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryLastTEAlertTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryLastTEAlertClearTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryRunningFailedCount"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMeasurementType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryConstTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryConstTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryConstTEWindow"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryInstTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryInstTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryConstTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryInstTETotAlarmTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistorySlavePortIdentity"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMasterPortIdentity"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMTIEValueIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMTIEValue"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryConstTEMeasurementTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryInstTEMeasurementTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMaxTEThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeResHistoryMaxTEClrThreshold"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeName"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeAdminState"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeOperationalState"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeSecondaryState"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbePTPFlowPoint"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeIpPrototocol"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeSlaveIpV4Address"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeMasterIpV4Address"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeReference"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeExpectedQL"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeActualTestStartTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeActualTestDuration"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbePDVAssuredHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbePDVAssuredLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbePDVSatisfiedHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbePDVSatisfiedLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeResPDVFwdLowRange"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeResPDVFwdMediumRange"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeResPDVFwdHighRange"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeResPDVRevLowRange"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeResPDVRevMediumRange"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeResPDVRevHighRange"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeScheduler"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeTestState"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeNoTimestampFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeNoEventMessageFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeFwdScore"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeRevScore"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStorageType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeRowStatus"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeResultsAvailable"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupDescr"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupEntityList"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupType"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupStartTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupDuration"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupStatus"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupStorageType"),
        ("F3-SYNCJACK-MIB", "f3SyncJScheduleGroupRowStatus"),
        ("F3-SYNCJACK-MIB", "f3UserDefinedMTIEMaskIndex"),
        ("F3-SYNCJACK-MIB", "f3UserDefinedMTIEMaskName"),
        ("F3-SYNCJACK-MIB", "f3UserDefinedMTIEMaskDisplayPoints"),
        ("F3-SYNCJACK-MIB", "f3UserDefinedMTIEMaskMeasurmentPoints"),
        ("F3-SYNCJACK-MIB", "f3UserDefinedMTIEMaskStorageType"),
        ("F3-SYNCJACK-MIB", "f3UserDefinedMTIEMaskRowStatus"))
)
if mibBuilder.loadTexts:
    f3SyncJObjectGroup.setStatus("current")

f3SyncJPerfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 4, 2, 2)
)
f3SyncJPerfObjectGroup.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsIntervalType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsValid"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsAction"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsSyncMsgsRx"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsDelayRspMsgsRx"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsLostSyncMsgs"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsLostDelayRspMsgs"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMinMeanPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMaxMeanPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsAvgMeanPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMinSyncPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMaxSyncPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsAvgSyncPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsAvgResPDVFwd"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVFwdLow"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVFwdMedium"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVFwdHigh"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVFwdTotal"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsFwdScore5"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsFwdScore4"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsFwdScore3"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsAvgResPDVRev"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVRevLow"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVRevMedium"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVRevHigh"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsResPDVRevTotal"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsRevScore5"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsRevScore4"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsRevScore3"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMinRPDVFwd"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMinRPDVRev"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMinPathAsymmetry"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMaxPathAsymmetry"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsAvgPathAsymmetry"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsPathLossSecondsFwd"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsPathLossSecondsRev"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryValid"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryAction"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistorySyncMsgsRx"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryLostSyncMsgs"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMinMeanPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMinSyncPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryAvgResPDVFwd"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVFwdLow"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVFwdMedium"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVFwdHigh"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVFwdTotal"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryFwdScore5"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryFwdScore4"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryFwdScore3"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryAvgResPDVRev"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVRevLow"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVRevMedium"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVRevHigh"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryResPDVRevTotal"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryRevScore5"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryRevScore4"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryRevScore3"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMinRPDVFwd"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMinRPDVRev"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMinPathAsymmetry"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdInterval"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdVariable"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdValueLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdValueHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdMonValue"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsIntervalType"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsValid"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsAction"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMTIE1s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMTIE10s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMTIE100s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMTIE1000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMTIE10000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMTIE50000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMaxTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatsMaxConstTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryValid"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryAction"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMTIE1s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMTIE10s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMTIE100s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMTIE1000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMTIE10000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMTIE50000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMaxTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeHistoryMaxConstTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdInterval"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdVariable"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdValueLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdValueHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdMonValue"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsIntervalType"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsValid"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsAction"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMTIE1s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMTIE10s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMTIE100s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMTIE1000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMTIE10000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMTIE50000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMaxTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatsMaxConstTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryTime"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryValid"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryAction"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMTIE1s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMTIE10s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMTIE100s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMTIE1000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMTIE10000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMTIE50000s"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMaxTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeHistoryMaxConstTE"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdInterval"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdVariable"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdValueLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdValueHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3SyncJPerfObjectGroup.setStatus("current")


# Notification objects

f3SyncJPTPNetworkProbeThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 3, 1)
)
f3SyncJPTPNetworkProbeThresholdCrossingAlert.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdInterval"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdVariable"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdValueLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdValueHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeThresholdCrossingAlert.setStatus(
        "current"
    )

f3SyncJClockProbeStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 3, 2)
)
f3SyncJClockProbeStatusChangeTrap.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJClockProbeTestState"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeSourceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatusMTIEMaskFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatusMTIEMarginFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeActualTestStartTime"))
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeStatusChangeTrap.setStatus(
        "current"
    )

f3SyncJPTPClockProbeStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 3, 3)
)
f3SyncJPTPClockProbeStatusChangeTrap.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeTestState"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeNoTimestampFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeNoEventMessageFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatusMTIEMaskFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatusMTIEMarginFailed"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeActualTestStartTime"))
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeStatusChangeTrap.setStatus(
        "current"
    )

f3SyncJPTPNetworkProbeStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 3, 4)
)
f3SyncJPTPNetworkProbeStatusChangeTrap.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeTestState"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeNoTimestampFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeNoEventMessageFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeReferenceFailure"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeFwdScore"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeRevScore"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeActualTestStartTime"))
)
if mibBuilder.loadTexts:
    f3SyncJPTPNetworkProbeStatusChangeTrap.setStatus(
        "current"
    )

f3SyncJClockProbeThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 3, 5)
)
f3SyncJClockProbeThresholdCrossingAlert.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdInterval"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdVariable"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdValueLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdValueHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3SyncJClockProbeThresholdCrossingAlert.setStatus(
        "current"
    )

f3SyncJPTPClockProbeThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 3, 6)
)
f3SyncJPTPClockProbeThresholdCrossingAlert.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdIndex"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdInterval"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdVariable"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdValueLo"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdValueHi"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3SyncJPTPClockProbeThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups

f3SyncJNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 4, 2, 3)
)
f3SyncJNotifGroup.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeThresholdCrossingAlert"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeThresholdCrossingAlert"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeThresholdCrossingAlert"),
        ("F3-SYNCJACK-MIB", "f3SyncJClockProbeStatusChangeTrap"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPClockProbeStatusChangeTrap"),
        ("F3-SYNCJACK-MIB", "f3SyncJPTPNetworkProbeStatusChangeTrap"))
)
if mibBuilder.loadTexts:
    f3SyncJNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f3SyncJCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 22, 4, 1, 1)
)
f3SyncJCompliance.setObjects(
      *(("F3-SYNCJACK-MIB", "f3SyncJObjectGroup"),
        ("F3-SYNCJACK-MIB", "f3SyncJPerfObjectGroup"),
        ("F3-SYNCJACK-MIB", "f3SyncJNotifGroup"))
)
if mibBuilder.loadTexts:
    f3SyncJCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-SYNCJACK-MIB",
    **{"SyncJackTestState": SyncJackTestState,
       "MTIEMaskType": MTIEMaskType,
       "TIESourceType": TIESourceType,
       "TIEMeasurementRate": TIEMeasurementRate,
       "PTPMeasurementDirection": PTPMeasurementDirection,
       "MeasurementType": MeasurementType,
       "FFOObserWindow": FFOObserWindow,
       "f3SyncJMIB": f3SyncJMIB,
       "f3SyncJConfigObjects": f3SyncJConfigObjects,
       "f3SyncJClockProbeTable": f3SyncJClockProbeTable,
       "f3SyncJClockProbeEntry": f3SyncJClockProbeEntry,
       "f3SyncJClockProbeIndex": f3SyncJClockProbeIndex,
       "f3SyncJClockProbeName": f3SyncJClockProbeName,
       "f3SyncJClockProbeSource": f3SyncJClockProbeSource,
       "f3SyncJClockProbeReference": f3SyncJClockProbeReference,
       "f3SyncJClockProbeExpectedQL": f3SyncJClockProbeExpectedQL,
       "f3SyncJClockProbeSourceType": f3SyncJClockProbeSourceType,
       "f3SyncJClockProbeMeasurementRate": f3SyncJClockProbeMeasurementRate,
       "f3SyncJClockProbeMTIEMaskType": f3SyncJClockProbeMTIEMaskType,
       "f3SyncJClockProbeMTIEMaskMargin": f3SyncJClockProbeMTIEMaskMargin,
       "f3SyncJClockProbeScheduler": f3SyncJClockProbeScheduler,
       "f3SyncJClockProbeTestState": f3SyncJClockProbeTestState,
       "f3SyncJClockProbeLastTIEResult": f3SyncJClockProbeLastTIEResult,
       "f3SyncJClockProbeLastTIEResultTime": f3SyncJClockProbeLastTIEResultTime,
       "f3SyncJClockProbeSourceFailure": f3SyncJClockProbeSourceFailure,
       "f3SyncJClockProbeReferenceFailure": f3SyncJClockProbeReferenceFailure,
       "f3SyncJClockProbeActualTestStartTime": f3SyncJClockProbeActualTestStartTime,
       "f3SyncJClockProbeActualTestDuration": f3SyncJClockProbeActualTestDuration,
       "f3SyncJClockProbeMTIEMaskCrossedTime": f3SyncJClockProbeMTIEMaskCrossedTime,
       "f3SyncJClockProbeMTIEMaskMarginCrossedTime": f3SyncJClockProbeMTIEMaskMarginCrossedTime,
       "f3SyncJClockProbeStatusMTIEMaskFailed": f3SyncJClockProbeStatusMTIEMaskFailed,
       "f3SyncJClockProbeStatusMTIEMarginFailed": f3SyncJClockProbeStatusMTIEMarginFailed,
       "f3SyncJClockProbeStorageType": f3SyncJClockProbeStorageType,
       "f3SyncJClockProbeRowStatus": f3SyncJClockProbeRowStatus,
       "f3SyncJClockProbeFfoTarget": f3SyncJClockProbeFfoTarget,
       "f3SyncJClockProbeFfoObserWindow": f3SyncJClockProbeFfoObserWindow,
       "f3SyncJClockProbeLastFFOResult": f3SyncJClockProbeLastFFOResult,
       "f3SyncJClockProbeTimeOfLastFFOResult": f3SyncJClockProbeTimeOfLastFFOResult,
       "f3SyncJClockProbeRawDataCollectionEnabled": f3SyncJClockProbeRawDataCollectionEnabled,
       "f3SyncJClockProbeTeAlertThreshold": f3SyncJClockProbeTeAlertThreshold,
       "f3SyncJClockProbeTeAlertClearThreshold": f3SyncJClockProbeTeAlertClearThreshold,
       "f3SyncJClockProbeLastTEAlertTime": f3SyncJClockProbeLastTEAlertTime,
       "f3SyncJClockProbeLastTEAlertClearTime": f3SyncJClockProbeLastTEAlertClearTime,
       "f3SyncJClockProbeRunningFailedCount": f3SyncJClockProbeRunningFailedCount,
       "f3SyncJClockProbeMeasurementType": f3SyncJClockProbeMeasurementType,
       "f3SyncJClockProbeConstTEThreshold": f3SyncJClockProbeConstTEThreshold,
       "f3SyncJClockProbeConstTEClrThreshold": f3SyncJClockProbeConstTEClrThreshold,
       "f3SyncJClockProbeConstTEWindow": f3SyncJClockProbeConstTEWindow,
       "f3SyncJClockProbeMaxTETotAlarmTime": f3SyncJClockProbeMaxTETotAlarmTime,
       "f3SyncJClockProbeConstTETotAlarmTime": f3SyncJClockProbeConstTETotAlarmTime,
       "f3SyncJClockProbeConstTEMeasurementTime": f3SyncJClockProbeConstTEMeasurementTime,
       "f3SyncJClockProbeMaxTEMeasurementTime": f3SyncJClockProbeMaxTEMeasurementTime,
       "f3SyncJClockProbeMaxTEThreshold": f3SyncJClockProbeMaxTEThreshold,
       "f3SyncJClockProbeMaxTEClrThreshold": f3SyncJClockProbeMaxTEClrThreshold,
       "f3SyncJClockProbeMTIERestart": f3SyncJClockProbeMTIERestart,
       "f3SyncJClockProbeMTIEValueTable": f3SyncJClockProbeMTIEValueTable,
       "f3SyncJClockProbeMTIEValueEntry": f3SyncJClockProbeMTIEValueEntry,
       "f3SyncJClockProbeMTIEValueIndex": f3SyncJClockProbeMTIEValueIndex,
       "f3SyncJClockProbeMTIEValue": f3SyncJClockProbeMTIEValue,
       "f3SyncJClockProbeResHistoryTable": f3SyncJClockProbeResHistoryTable,
       "f3SyncJClockProbeResHistoryEntry": f3SyncJClockProbeResHistoryEntry,
       "f3SyncJClockProbeResHistoryIndex": f3SyncJClockProbeResHistoryIndex,
       "f3SyncJClockProbeResHistoryAlias": f3SyncJClockProbeResHistoryAlias,
       "f3SyncJClockProbeResHistorySource": f3SyncJClockProbeResHistorySource,
       "f3SyncJClockProbeResHistoryReference": f3SyncJClockProbeResHistoryReference,
       "f3SyncJClockProbeResHistoryExpectedQL": f3SyncJClockProbeResHistoryExpectedQL,
       "f3SyncJClockProbeResHistorySourceType": f3SyncJClockProbeResHistorySourceType,
       "f3SyncJClockProbeResHistoryMeasurementRate": f3SyncJClockProbeResHistoryMeasurementRate,
       "f3SyncJClockProbeResHistoryMTIEMaskType": f3SyncJClockProbeResHistoryMTIEMaskType,
       "f3SyncJClockProbeResHistoryMTIEMaskMargin": f3SyncJClockProbeResHistoryMTIEMaskMargin,
       "f3SyncJClockProbeResHistorySourceFailure": f3SyncJClockProbeResHistorySourceFailure,
       "f3SyncJClockProbeResHistoryReferenceFailure": f3SyncJClockProbeResHistoryReferenceFailure,
       "f3SyncJClockProbeResHistoryActualTestStartTime": f3SyncJClockProbeResHistoryActualTestStartTime,
       "f3SyncJClockProbeResHistoryActualTestDuration": f3SyncJClockProbeResHistoryActualTestDuration,
       "f3SyncJClockProbeResHistoryMTIEMaskCrossedTime": f3SyncJClockProbeResHistoryMTIEMaskCrossedTime,
       "f3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime": f3SyncJClockProbeResHistoryMTIEMaskMarginCrossedTime,
       "f3SyncJClockProbeResHistoryStatusMTIEMaskFailed": f3SyncJClockProbeResHistoryStatusMTIEMaskFailed,
       "f3SyncJClockProbeResHistoryStatusMTIEMarginFailed": f3SyncJClockProbeResHistoryStatusMTIEMarginFailed,
       "f3SyncJClockProbeResHistoryStorageType": f3SyncJClockProbeResHistoryStorageType,
       "f3SyncJClockProbeResHistoryRowStatus": f3SyncJClockProbeResHistoryRowStatus,
       "f3SyncJClockProbeResHistoryMinFFO": f3SyncJClockProbeResHistoryMinFFO,
       "f3SyncJClockProbeResHistoryMaxFFO": f3SyncJClockProbeResHistoryMaxFFO,
       "f3SyncJClockProbeResHistoryAvgFFO": f3SyncJClockProbeResHistoryAvgFFO,
       "f3SyncJClockProbeResHistoryOutOfTargetFFOTime": f3SyncJClockProbeResHistoryOutOfTargetFFOTime,
       "f3SyncJClockProbeResHistoryTotalFFOTime": f3SyncJClockProbeResHistoryTotalFFOTime,
       "f3SyncJClockProbeResHistoryMinPhaseOffset": f3SyncJClockProbeResHistoryMinPhaseOffset,
       "f3SyncJClockProbeResHistoryMaxPhaseOffset": f3SyncJClockProbeResHistoryMaxPhaseOffset,
       "f3SyncJClockProbeResHistoryAvgPhaseOffset": f3SyncJClockProbeResHistoryAvgPhaseOffset,
       "f3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime": f3SyncJClockProbeResHistoryOutOfTargetPhaseOffsetTime,
       "f3SyncJClockProbeResHistoryTotalPhaseOffsetTime": f3SyncJClockProbeResHistoryTotalPhaseOffsetTime,
       "f3SyncJClockProbeResHistoryMeasurementType": f3SyncJClockProbeResHistoryMeasurementType,
       "f3SyncJClockProbeResHistoryTeAlertThreshold": f3SyncJClockProbeResHistoryTeAlertThreshold,
       "f3SyncJClockProbeResHistoryTeAlertClearThreshold": f3SyncJClockProbeResHistoryTeAlertClearThreshold,
       "f3SyncJClockProbeResHistoryLastTEAlertTime": f3SyncJClockProbeResHistoryLastTEAlertTime,
       "f3SyncJClockProbeResHistoryLastTEAlertClearTime": f3SyncJClockProbeResHistoryLastTEAlertClearTime,
       "f3SyncJClockProbeResHistoryRunningFailedCount": f3SyncJClockProbeResHistoryRunningFailedCount,
       "f3SyncJClockProbeResHistoryConstTEThreshold": f3SyncJClockProbeResHistoryConstTEThreshold,
       "f3SyncJClockProbeResHistoryConstTEClrThreshold": f3SyncJClockProbeResHistoryConstTEClrThreshold,
       "f3SyncJClockProbeResHistoryConstTEWindow": f3SyncJClockProbeResHistoryConstTEWindow,
       "f3SyncJClockProbeResHistoryMaxTETotAlarmTime": f3SyncJClockProbeResHistoryMaxTETotAlarmTime,
       "f3SyncJClockProbeResHistoryConstTETotAlarmTime": f3SyncJClockProbeResHistoryConstTETotAlarmTime,
       "f3SyncJClockProbeResHistoryConstTEMeasurementTime": f3SyncJClockProbeResHistoryConstTEMeasurementTime,
       "f3SyncJClockProbeResHistoryMaxTEMeasurementTime": f3SyncJClockProbeResHistoryMaxTEMeasurementTime,
       "f3SyncJClockProbeResHistoryMaxTEThreshold": f3SyncJClockProbeResHistoryMaxTEThreshold,
       "f3SyncJClockProbeResHistoryMaxTEClrThreshold": f3SyncJClockProbeResHistoryMaxTEClrThreshold,
       "f3SyncJClockProbeResHistoryMTIEValueTable": f3SyncJClockProbeResHistoryMTIEValueTable,
       "f3SyncJClockProbeResHistoryMTIEValueEntry": f3SyncJClockProbeResHistoryMTIEValueEntry,
       "f3SyncJClockProbeResHistoryMTIEValueIndex": f3SyncJClockProbeResHistoryMTIEValueIndex,
       "f3SyncJClockProbeResHistoryMTIEValue": f3SyncJClockProbeResHistoryMTIEValue,
       "f3SyncJPTPClockProbeTable": f3SyncJPTPClockProbeTable,
       "f3SyncJPTPClockProbeEntry": f3SyncJPTPClockProbeEntry,
       "f3SyncJPTPClockProbeIndex": f3SyncJPTPClockProbeIndex,
       "f3SyncJPTPClockProbeName": f3SyncJPTPClockProbeName,
       "f3SyncJPTPClockProbeMeasurementDirection": f3SyncJPTPClockProbeMeasurementDirection,
       "f3SyncJPTPClockProbePTPFlowPoint": f3SyncJPTPClockProbePTPFlowPoint,
       "f3SyncJPTPClockProbeIpPrototocol": f3SyncJPTPClockProbeIpPrototocol,
       "f3SyncJPTPClockProbeSlaveIpV4Address": f3SyncJPTPClockProbeSlaveIpV4Address,
       "f3SyncJPTPClockProbeMasterIpV4Address": f3SyncJPTPClockProbeMasterIpV4Address,
       "f3SyncJPTPClockProbeReference": f3SyncJPTPClockProbeReference,
       "f3SyncJPTPClockProbeExpectedQL": f3SyncJPTPClockProbeExpectedQL,
       "f3SyncJPTPClockProbeMTIEMaskType": f3SyncJPTPClockProbeMTIEMaskType,
       "f3SyncJPTPClockProbeMTIEMaskMargin": f3SyncJPTPClockProbeMTIEMaskMargin,
       "f3SyncJPTPClockProbeScheduler": f3SyncJPTPClockProbeScheduler,
       "f3SyncJPTPClockProbeTestState": f3SyncJPTPClockProbeTestState,
       "f3SyncJPTPClockProbeLastTIEResult": f3SyncJPTPClockProbeLastTIEResult,
       "f3SyncJPTPClockProbeLastTIEResultTime": f3SyncJPTPClockProbeLastTIEResultTime,
       "f3SyncJPTPClockProbeNoTimestampFailure": f3SyncJPTPClockProbeNoTimestampFailure,
       "f3SyncJPTPClockProbeNoEventMessageFailure": f3SyncJPTPClockProbeNoEventMessageFailure,
       "f3SyncJPTPClockProbeReferenceFailure": f3SyncJPTPClockProbeReferenceFailure,
       "f3SyncJPTPClockProbeActualTestStartTime": f3SyncJPTPClockProbeActualTestStartTime,
       "f3SyncJPTPClockProbeActualTestDuration": f3SyncJPTPClockProbeActualTestDuration,
       "f3SyncJPTPClockProbeMTIEMaskCrossedTime": f3SyncJPTPClockProbeMTIEMaskCrossedTime,
       "f3SyncJPTPClockProbeMTIEMaskMarginCrossedTime": f3SyncJPTPClockProbeMTIEMaskMarginCrossedTime,
       "f3SyncJPTPClockProbeStatusMTIEMaskFailed": f3SyncJPTPClockProbeStatusMTIEMaskFailed,
       "f3SyncJPTPClockProbeStatusMTIEMarginFailed": f3SyncJPTPClockProbeStatusMTIEMarginFailed,
       "f3SyncJPTPClockProbeStorageType": f3SyncJPTPClockProbeStorageType,
       "f3SyncJPTPClockProbeRowStatus": f3SyncJPTPClockProbeRowStatus,
       "f3SyncJPTPClockProbeFfoTarget": f3SyncJPTPClockProbeFfoTarget,
       "f3SyncJPTPClockProbeFfoObserWindow": f3SyncJPTPClockProbeFfoObserWindow,
       "f3SyncJPTPClockProbeLastFFOResult": f3SyncJPTPClockProbeLastFFOResult,
       "f3SyncJPTPClockProbeTimeOfLastFFOResult": f3SyncJPTPClockProbeTimeOfLastFFOResult,
       "f3SyncJPTPClockProbeRawDataCollectionEnabled": f3SyncJPTPClockProbeRawDataCollectionEnabled,
       "f3SyncJPTPClockProbeTeAlertThreshold": f3SyncJPTPClockProbeTeAlertThreshold,
       "f3SyncJPTPClockProbeTeAlertClearThreshold": f3SyncJPTPClockProbeTeAlertClearThreshold,
       "f3SyncJPTPClockProbeLastTEAlertTime": f3SyncJPTPClockProbeLastTEAlertTime,
       "f3SyncJPTPClockProbeLastTEAlertClearTime": f3SyncJPTPClockProbeLastTEAlertClearTime,
       "f3SyncJPTPClockProbeRunningFailedCount": f3SyncJPTPClockProbeRunningFailedCount,
       "f3SyncJPTPClockProbeMeasurementType": f3SyncJPTPClockProbeMeasurementType,
       "f3SyncJPTPClockProbeDelayMS": f3SyncJPTPClockProbeDelayMS,
       "f3SyncJPTPClockProbeDelaySM": f3SyncJPTPClockProbeDelaySM,
       "f3SyncJPTPClockProbeTAsymmetry": f3SyncJPTPClockProbeTAsymmetry,
       "f3SyncJPTPClockProbeDelayCompensation": f3SyncJPTPClockProbeDelayCompensation,
       "f3SyncJPTPClockProbeConstTEThreshold": f3SyncJPTPClockProbeConstTEThreshold,
       "f3SyncJPTPClockProbeConstTEClrThreshold": f3SyncJPTPClockProbeConstTEClrThreshold,
       "f3SyncJPTPClockProbeConstTEWindow": f3SyncJPTPClockProbeConstTEWindow,
       "f3SyncJPTPClockProbeInstTEThreshold": f3SyncJPTPClockProbeInstTEThreshold,
       "f3SyncJPTPClockProbeInstTEClrThreshold": f3SyncJPTPClockProbeInstTEClrThreshold,
       "f3SyncJPTPClockProbeMaxTETotAlarmTime": f3SyncJPTPClockProbeMaxTETotAlarmTime,
       "f3SyncJPTPClockProbeConstTETotAlarmTime": f3SyncJPTPClockProbeConstTETotAlarmTime,
       "f3SyncJPTPClockProbeInstTETotAlarmTime": f3SyncJPTPClockProbeInstTETotAlarmTime,
       "f3SyncJPTPClockProbeSlavePortIdentity": f3SyncJPTPClockProbeSlavePortIdentity,
       "f3SyncJPTPClockProbeMasterPortIdentity": f3SyncJPTPClockProbeMasterPortIdentity,
       "f3SyncJPTPClockProbeConstTEMeasurementTime": f3SyncJPTPClockProbeConstTEMeasurementTime,
       "f3SyncJPTPClockProbeMaxTEMeasurementTime": f3SyncJPTPClockProbeMaxTEMeasurementTime,
       "f3SyncJPTPClockProbeInstTEMeasurementTime": f3SyncJPTPClockProbeInstTEMeasurementTime,
       "f3SyncJPTPClockProbeMaxTEThreshold": f3SyncJPTPClockProbeMaxTEThreshold,
       "f3SyncJPTPClockProbeMaxTEClrThreshold": f3SyncJPTPClockProbeMaxTEClrThreshold,
       "f3SyncJPTPClockProbeMTIERestart": f3SyncJPTPClockProbeMTIERestart,
       "f3SyncJPTPClockProbeMTIEValueTable": f3SyncJPTPClockProbeMTIEValueTable,
       "f3SyncJPTPClockProbeMTIEValueEntry": f3SyncJPTPClockProbeMTIEValueEntry,
       "f3SyncJPTPClockProbeMTIEValueIndex": f3SyncJPTPClockProbeMTIEValueIndex,
       "f3SyncJPTPClockProbeMTIEValue": f3SyncJPTPClockProbeMTIEValue,
       "f3SyncJPTPClockProbeResHistoryTable": f3SyncJPTPClockProbeResHistoryTable,
       "f3SyncJPTPClockProbeResHistoryEntry": f3SyncJPTPClockProbeResHistoryEntry,
       "f3SyncJPTPClockProbeResHistoryIndex": f3SyncJPTPClockProbeResHistoryIndex,
       "f3SyncJPTPClockProbeResHistoryAlias": f3SyncJPTPClockProbeResHistoryAlias,
       "f3SyncJPTPClockProbeResHistoryMeasurementDirection": f3SyncJPTPClockProbeResHistoryMeasurementDirection,
       "f3SyncJPTPClockProbeResHistoryPTPFlowPoint": f3SyncJPTPClockProbeResHistoryPTPFlowPoint,
       "f3SyncJPTPClockProbeResHistoryIpPrototocol": f3SyncJPTPClockProbeResHistoryIpPrototocol,
       "f3SyncJPTPClockProbeResHistorySlaveIpV4Address": f3SyncJPTPClockProbeResHistorySlaveIpV4Address,
       "f3SyncJPTPClockProbeResHistoryMasterIpV4Address": f3SyncJPTPClockProbeResHistoryMasterIpV4Address,
       "f3SyncJPTPClockProbeResHistoryReference": f3SyncJPTPClockProbeResHistoryReference,
       "f3SyncJPTPClockProbeResHistoryExpectedQL": f3SyncJPTPClockProbeResHistoryExpectedQL,
       "f3SyncJPTPClockProbeResHistoryMTIEMaskType": f3SyncJPTPClockProbeResHistoryMTIEMaskType,
       "f3SyncJPTPClockProbeResHistoryMTIEMaskMargin": f3SyncJPTPClockProbeResHistoryMTIEMaskMargin,
       "f3SyncJPTPClockProbeResHistoryNoTimestampFailure": f3SyncJPTPClockProbeResHistoryNoTimestampFailure,
       "f3SyncJPTPClockProbeResHistoryNoEventMessageFailure": f3SyncJPTPClockProbeResHistoryNoEventMessageFailure,
       "f3SyncJPTPClockProbeResHistoryReferenceFailure": f3SyncJPTPClockProbeResHistoryReferenceFailure,
       "f3SyncJPTPClockProbeResHistoryActualTestStartTime": f3SyncJPTPClockProbeResHistoryActualTestStartTime,
       "f3SyncJPTPClockProbeResHistoryActualTestDuration": f3SyncJPTPClockProbeResHistoryActualTestDuration,
       "f3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime": f3SyncJPTPClockProbeResHistoryMTIEMaskCrossedTime,
       "f3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime": f3SyncJPTPClockProbeResHistoryMTIEMaskMarginCrossedTime,
       "f3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed": f3SyncJPTPClockProbeResHistoryStatusMTIEMaskFailed,
       "f3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed": f3SyncJPTPClockProbeResHistoryStatusMTIEMarginFailed,
       "f3SyncJPTPClockProbeResHistoryStorageType": f3SyncJPTPClockProbeResHistoryStorageType,
       "f3SyncJPTPClockProbeResHistoryRowStatus": f3SyncJPTPClockProbeResHistoryRowStatus,
       "f3SyncJPTPClockProbeResHistoryMinFFO": f3SyncJPTPClockProbeResHistoryMinFFO,
       "f3SyncJPTPClockProbeResHistoryMaxFFO": f3SyncJPTPClockProbeResHistoryMaxFFO,
       "f3SyncJPTPClockProbeResHistoryAvgFFO": f3SyncJPTPClockProbeResHistoryAvgFFO,
       "f3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime": f3SyncJPTPClockProbeResHistoryOutOfTargetFFOTime,
       "f3SyncJPTPClockProbeResHistoryTotalFFOTime": f3SyncJPTPClockProbeResHistoryTotalFFOTime,
       "f3SyncJPTPClockProbeResHistoryMinPhaseOffset": f3SyncJPTPClockProbeResHistoryMinPhaseOffset,
       "f3SyncJPTPClockProbeResHistoryMaxPhaseOffset": f3SyncJPTPClockProbeResHistoryMaxPhaseOffset,
       "f3SyncJPTPClockProbeResHistoryAvgPhaseOffset": f3SyncJPTPClockProbeResHistoryAvgPhaseOffset,
       "f3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime": f3SyncJPTPClockProbeResHistoryOutOfTargetPhaseOffsetTime,
       "f3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime": f3SyncJPTPClockProbeResHistoryTotalPhaseOffsetTime,
       "f3SyncJPTPClockProbeResHistoryTeAlertThreshold": f3SyncJPTPClockProbeResHistoryTeAlertThreshold,
       "f3SyncJPTPClockProbeResHistoryTeAlertClearThreshold": f3SyncJPTPClockProbeResHistoryTeAlertClearThreshold,
       "f3SyncJPTPClockProbeResHistoryLastTEAlertTime": f3SyncJPTPClockProbeResHistoryLastTEAlertTime,
       "f3SyncJPTPClockProbeResHistoryLastTEAlertClearTime": f3SyncJPTPClockProbeResHistoryLastTEAlertClearTime,
       "f3SyncJPTPClockProbeResHistoryRunningFailedCount": f3SyncJPTPClockProbeResHistoryRunningFailedCount,
       "f3SyncJPTPClockProbeResHistoryMeasurementType": f3SyncJPTPClockProbeResHistoryMeasurementType,
       "f3SyncJPTPClockProbeResHistoryConstTEThreshold": f3SyncJPTPClockProbeResHistoryConstTEThreshold,
       "f3SyncJPTPClockProbeResHistoryConstTEClrThreshold": f3SyncJPTPClockProbeResHistoryConstTEClrThreshold,
       "f3SyncJPTPClockProbeResHistoryConstTEWindow": f3SyncJPTPClockProbeResHistoryConstTEWindow,
       "f3SyncJPTPClockProbeResHistoryInstTEThreshold": f3SyncJPTPClockProbeResHistoryInstTEThreshold,
       "f3SyncJPTPClockProbeResHistoryInstTEClrThreshold": f3SyncJPTPClockProbeResHistoryInstTEClrThreshold,
       "f3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime": f3SyncJPTPClockProbeResHistoryMaxTETotAlarmTime,
       "f3SyncJPTPClockProbeResHistoryConstTETotAlarmTime": f3SyncJPTPClockProbeResHistoryConstTETotAlarmTime,
       "f3SyncJPTPClockProbeResHistoryInstTETotAlarmTime": f3SyncJPTPClockProbeResHistoryInstTETotAlarmTime,
       "f3SyncJPTPClockProbeResHistorySlavePortIdentity": f3SyncJPTPClockProbeResHistorySlavePortIdentity,
       "f3SyncJPTPClockProbeResHistoryMasterPortIdentity": f3SyncJPTPClockProbeResHistoryMasterPortIdentity,
       "f3SyncJPTPClockProbeResHistoryConstTEMeasurementTime": f3SyncJPTPClockProbeResHistoryConstTEMeasurementTime,
       "f3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime": f3SyncJPTPClockProbeResHistoryMaxTEMeasurementTime,
       "f3SyncJPTPClockProbeResHistoryInstTEMeasurementTime": f3SyncJPTPClockProbeResHistoryInstTEMeasurementTime,
       "f3SyncJPTPClockProbeResHistoryMaxTEThreshold": f3SyncJPTPClockProbeResHistoryMaxTEThreshold,
       "f3SyncJPTPClockProbeResHistoryMaxTEClrThreshold": f3SyncJPTPClockProbeResHistoryMaxTEClrThreshold,
       "f3SyncJPTPClockProbeResHistoryMTIEValueTable": f3SyncJPTPClockProbeResHistoryMTIEValueTable,
       "f3SyncJPTPClockProbeResHistoryMTIEValueEntry": f3SyncJPTPClockProbeResHistoryMTIEValueEntry,
       "f3SyncJPTPClockProbeResHistoryMTIEValueIndex": f3SyncJPTPClockProbeResHistoryMTIEValueIndex,
       "f3SyncJPTPClockProbeResHistoryMTIEValue": f3SyncJPTPClockProbeResHistoryMTIEValue,
       "f3SyncJPTPNetworkProbeTable": f3SyncJPTPNetworkProbeTable,
       "f3SyncJPTPNetworkProbeEntry": f3SyncJPTPNetworkProbeEntry,
       "f3SyncJPTPNetworkProbeIndex": f3SyncJPTPNetworkProbeIndex,
       "f3SyncJPTPNetworkProbeName": f3SyncJPTPNetworkProbeName,
       "f3SyncJPTPNetworkProbeAdminState": f3SyncJPTPNetworkProbeAdminState,
       "f3SyncJPTPNetworkProbeOperationalState": f3SyncJPTPNetworkProbeOperationalState,
       "f3SyncJPTPNetworkProbeSecondaryState": f3SyncJPTPNetworkProbeSecondaryState,
       "f3SyncJPTPNetworkProbePTPFlowPoint": f3SyncJPTPNetworkProbePTPFlowPoint,
       "f3SyncJPTPNetworkProbeIpPrototocol": f3SyncJPTPNetworkProbeIpPrototocol,
       "f3SyncJPTPNetworkProbeSlaveIpV4Address": f3SyncJPTPNetworkProbeSlaveIpV4Address,
       "f3SyncJPTPNetworkProbeMasterIpV4Address": f3SyncJPTPNetworkProbeMasterIpV4Address,
       "f3SyncJPTPNetworkProbeReference": f3SyncJPTPNetworkProbeReference,
       "f3SyncJPTPNetworkProbeExpectedQL": f3SyncJPTPNetworkProbeExpectedQL,
       "f3SyncJPTPNetworkProbeActualTestStartTime": f3SyncJPTPNetworkProbeActualTestStartTime,
       "f3SyncJPTPNetworkProbeActualTestDuration": f3SyncJPTPNetworkProbeActualTestDuration,
       "f3SyncJPTPNetworkProbePDVAssuredHi": f3SyncJPTPNetworkProbePDVAssuredHi,
       "f3SyncJPTPNetworkProbePDVAssuredLo": f3SyncJPTPNetworkProbePDVAssuredLo,
       "f3SyncJPTPNetworkProbePDVSatisfiedHi": f3SyncJPTPNetworkProbePDVSatisfiedHi,
       "f3SyncJPTPNetworkProbePDVSatisfiedLo": f3SyncJPTPNetworkProbePDVSatisfiedLo,
       "f3SyncJPTPNetworkProbeResPDVFwdLowRange": f3SyncJPTPNetworkProbeResPDVFwdLowRange,
       "f3SyncJPTPNetworkProbeResPDVFwdMediumRange": f3SyncJPTPNetworkProbeResPDVFwdMediumRange,
       "f3SyncJPTPNetworkProbeResPDVFwdHighRange": f3SyncJPTPNetworkProbeResPDVFwdHighRange,
       "f3SyncJPTPNetworkProbeResPDVRevLowRange": f3SyncJPTPNetworkProbeResPDVRevLowRange,
       "f3SyncJPTPNetworkProbeResPDVRevMediumRange": f3SyncJPTPNetworkProbeResPDVRevMediumRange,
       "f3SyncJPTPNetworkProbeResPDVRevHighRange": f3SyncJPTPNetworkProbeResPDVRevHighRange,
       "f3SyncJPTPNetworkProbeScheduler": f3SyncJPTPNetworkProbeScheduler,
       "f3SyncJPTPNetworkProbeTestState": f3SyncJPTPNetworkProbeTestState,
       "f3SyncJPTPNetworkProbeNoTimestampFailure": f3SyncJPTPNetworkProbeNoTimestampFailure,
       "f3SyncJPTPNetworkProbeNoEventMessageFailure": f3SyncJPTPNetworkProbeNoEventMessageFailure,
       "f3SyncJPTPNetworkProbeFwdScore": f3SyncJPTPNetworkProbeFwdScore,
       "f3SyncJPTPNetworkProbeRevScore": f3SyncJPTPNetworkProbeRevScore,
       "f3SyncJPTPNetworkProbeReferenceFailure": f3SyncJPTPNetworkProbeReferenceFailure,
       "f3SyncJPTPNetworkProbeStorageType": f3SyncJPTPNetworkProbeStorageType,
       "f3SyncJPTPNetworkProbeRowStatus": f3SyncJPTPNetworkProbeRowStatus,
       "f3SyncJPTPNetworkProbeResultsAvailable": f3SyncJPTPNetworkProbeResultsAvailable,
       "f3SyncJScheduleGroupTable": f3SyncJScheduleGroupTable,
       "f3SyncJScheduleGroupEntry": f3SyncJScheduleGroupEntry,
       "f3SyncJScheduleGroupIndex": f3SyncJScheduleGroupIndex,
       "f3SyncJScheduleGroupDescr": f3SyncJScheduleGroupDescr,
       "f3SyncJScheduleGroupEntityList": f3SyncJScheduleGroupEntityList,
       "f3SyncJScheduleGroupType": f3SyncJScheduleGroupType,
       "f3SyncJScheduleGroupStartTime": f3SyncJScheduleGroupStartTime,
       "f3SyncJScheduleGroupDuration": f3SyncJScheduleGroupDuration,
       "f3SyncJScheduleGroupStatus": f3SyncJScheduleGroupStatus,
       "f3SyncJScheduleGroupStorageType": f3SyncJScheduleGroupStorageType,
       "f3SyncJScheduleGroupRowStatus": f3SyncJScheduleGroupRowStatus,
       "f3UserDefinedMTIEMaskTable": f3UserDefinedMTIEMaskTable,
       "f3UserDefinedMTIEMaskEntry": f3UserDefinedMTIEMaskEntry,
       "f3UserDefinedMTIEMaskIndex": f3UserDefinedMTIEMaskIndex,
       "f3UserDefinedMTIEMaskName": f3UserDefinedMTIEMaskName,
       "f3UserDefinedMTIEMaskDisplayPoints": f3UserDefinedMTIEMaskDisplayPoints,
       "f3UserDefinedMTIEMaskMeasurmentPoints": f3UserDefinedMTIEMaskMeasurmentPoints,
       "f3UserDefinedMTIEMaskStorageType": f3UserDefinedMTIEMaskStorageType,
       "f3UserDefinedMTIEMaskRowStatus": f3UserDefinedMTIEMaskRowStatus,
       "f3SyncJPerformanceObjects": f3SyncJPerformanceObjects,
       "f3SyncJPTPNetworkProbeStatsTable": f3SyncJPTPNetworkProbeStatsTable,
       "f3SyncJPTPNetworkProbeStatsEntry": f3SyncJPTPNetworkProbeStatsEntry,
       "f3SyncJPTPNetworkProbeStatsIndex": f3SyncJPTPNetworkProbeStatsIndex,
       "f3SyncJPTPNetworkProbeStatsIntervalType": f3SyncJPTPNetworkProbeStatsIntervalType,
       "f3SyncJPTPNetworkProbeStatsValid": f3SyncJPTPNetworkProbeStatsValid,
       "f3SyncJPTPNetworkProbeStatsAction": f3SyncJPTPNetworkProbeStatsAction,
       "f3SyncJPTPNetworkProbeStatsSyncMsgsRx": f3SyncJPTPNetworkProbeStatsSyncMsgsRx,
       "f3SyncJPTPNetworkProbeStatsDelayRspMsgsRx": f3SyncJPTPNetworkProbeStatsDelayRspMsgsRx,
       "f3SyncJPTPNetworkProbeStatsLostSyncMsgs": f3SyncJPTPNetworkProbeStatsLostSyncMsgs,
       "f3SyncJPTPNetworkProbeStatsLostDelayRspMsgs": f3SyncJPTPNetworkProbeStatsLostDelayRspMsgs,
       "f3SyncJPTPNetworkProbeStatsMinMeanPathDelay": f3SyncJPTPNetworkProbeStatsMinMeanPathDelay,
       "f3SyncJPTPNetworkProbeStatsMaxMeanPathDelay": f3SyncJPTPNetworkProbeStatsMaxMeanPathDelay,
       "f3SyncJPTPNetworkProbeStatsAvgMeanPathDelay": f3SyncJPTPNetworkProbeStatsAvgMeanPathDelay,
       "f3SyncJPTPNetworkProbeStatsMinSyncPathDelay": f3SyncJPTPNetworkProbeStatsMinSyncPathDelay,
       "f3SyncJPTPNetworkProbeStatsMaxSyncPathDelay": f3SyncJPTPNetworkProbeStatsMaxSyncPathDelay,
       "f3SyncJPTPNetworkProbeStatsAvgSyncPathDelay": f3SyncJPTPNetworkProbeStatsAvgSyncPathDelay,
       "f3SyncJPTPNetworkProbeStatsAvgResPDVFwd": f3SyncJPTPNetworkProbeStatsAvgResPDVFwd,
       "f3SyncJPTPNetworkProbeStatsResPDVFwdLow": f3SyncJPTPNetworkProbeStatsResPDVFwdLow,
       "f3SyncJPTPNetworkProbeStatsResPDVFwdMedium": f3SyncJPTPNetworkProbeStatsResPDVFwdMedium,
       "f3SyncJPTPNetworkProbeStatsResPDVFwdHigh": f3SyncJPTPNetworkProbeStatsResPDVFwdHigh,
       "f3SyncJPTPNetworkProbeStatsResPDVFwdTotal": f3SyncJPTPNetworkProbeStatsResPDVFwdTotal,
       "f3SyncJPTPNetworkProbeStatsFwdScore5": f3SyncJPTPNetworkProbeStatsFwdScore5,
       "f3SyncJPTPNetworkProbeStatsFwdScore4": f3SyncJPTPNetworkProbeStatsFwdScore4,
       "f3SyncJPTPNetworkProbeStatsFwdScore3": f3SyncJPTPNetworkProbeStatsFwdScore3,
       "f3SyncJPTPNetworkProbeStatsAvgResPDVRev": f3SyncJPTPNetworkProbeStatsAvgResPDVRev,
       "f3SyncJPTPNetworkProbeStatsResPDVRevLow": f3SyncJPTPNetworkProbeStatsResPDVRevLow,
       "f3SyncJPTPNetworkProbeStatsResPDVRevMedium": f3SyncJPTPNetworkProbeStatsResPDVRevMedium,
       "f3SyncJPTPNetworkProbeStatsResPDVRevHigh": f3SyncJPTPNetworkProbeStatsResPDVRevHigh,
       "f3SyncJPTPNetworkProbeStatsResPDVRevTotal": f3SyncJPTPNetworkProbeStatsResPDVRevTotal,
       "f3SyncJPTPNetworkProbeStatsRevScore5": f3SyncJPTPNetworkProbeStatsRevScore5,
       "f3SyncJPTPNetworkProbeStatsRevScore4": f3SyncJPTPNetworkProbeStatsRevScore4,
       "f3SyncJPTPNetworkProbeStatsRevScore3": f3SyncJPTPNetworkProbeStatsRevScore3,
       "f3SyncJPTPNetworkProbeStatsMinRPDVFwd": f3SyncJPTPNetworkProbeStatsMinRPDVFwd,
       "f3SyncJPTPNetworkProbeStatsMinRPDVRev": f3SyncJPTPNetworkProbeStatsMinRPDVRev,
       "f3SyncJPTPNetworkProbeStatsMinPathAsymmetry": f3SyncJPTPNetworkProbeStatsMinPathAsymmetry,
       "f3SyncJPTPNetworkProbeStatsMaxPathAsymmetry": f3SyncJPTPNetworkProbeStatsMaxPathAsymmetry,
       "f3SyncJPTPNetworkProbeStatsAvgPathAsymmetry": f3SyncJPTPNetworkProbeStatsAvgPathAsymmetry,
       "f3SyncJPTPNetworkProbeStatsPathLossSecondsFwd": f3SyncJPTPNetworkProbeStatsPathLossSecondsFwd,
       "f3SyncJPTPNetworkProbeStatsPathLossSecondsRev": f3SyncJPTPNetworkProbeStatsPathLossSecondsRev,
       "f3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay": f3SyncJPTPNetworkProbeStatsMinDelayReqPathDelay,
       "f3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay": f3SyncJPTPNetworkProbeStatsMaxDelayReqPathDelay,
       "f3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay": f3SyncJPTPNetworkProbeStatsAvgDelayReqPathDelay,
       "f3SyncJPTPNetworkProbeHistoryTable": f3SyncJPTPNetworkProbeHistoryTable,
       "f3SyncJPTPNetworkProbeHistoryEntry": f3SyncJPTPNetworkProbeHistoryEntry,
       "f3SyncJPTPNetworkProbeHistoryIndex": f3SyncJPTPNetworkProbeHistoryIndex,
       "f3SyncJPTPNetworkProbeHistoryTime": f3SyncJPTPNetworkProbeHistoryTime,
       "f3SyncJPTPNetworkProbeHistoryValid": f3SyncJPTPNetworkProbeHistoryValid,
       "f3SyncJPTPNetworkProbeHistoryAction": f3SyncJPTPNetworkProbeHistoryAction,
       "f3SyncJPTPNetworkProbeHistorySyncMsgsRx": f3SyncJPTPNetworkProbeHistorySyncMsgsRx,
       "f3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx": f3SyncJPTPNetworkProbeHistoryDelayRspMsgsRx,
       "f3SyncJPTPNetworkProbeHistoryLostSyncMsgs": f3SyncJPTPNetworkProbeHistoryLostSyncMsgs,
       "f3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs": f3SyncJPTPNetworkProbeHistoryLostDelayRspMsgs,
       "f3SyncJPTPNetworkProbeHistoryMinMeanPathDelay": f3SyncJPTPNetworkProbeHistoryMinMeanPathDelay,
       "f3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay": f3SyncJPTPNetworkProbeHistoryMaxMeanPathDelay,
       "f3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay": f3SyncJPTPNetworkProbeHistoryAvgMeanPathDelay,
       "f3SyncJPTPNetworkProbeHistoryMinSyncPathDelay": f3SyncJPTPNetworkProbeHistoryMinSyncPathDelay,
       "f3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay": f3SyncJPTPNetworkProbeHistoryMaxSyncPathDelay,
       "f3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay": f3SyncJPTPNetworkProbeHistoryAvgSyncPathDelay,
       "f3SyncJPTPNetworkProbeHistoryAvgResPDVFwd": f3SyncJPTPNetworkProbeHistoryAvgResPDVFwd,
       "f3SyncJPTPNetworkProbeHistoryResPDVFwdLow": f3SyncJPTPNetworkProbeHistoryResPDVFwdLow,
       "f3SyncJPTPNetworkProbeHistoryResPDVFwdMedium": f3SyncJPTPNetworkProbeHistoryResPDVFwdMedium,
       "f3SyncJPTPNetworkProbeHistoryResPDVFwdHigh": f3SyncJPTPNetworkProbeHistoryResPDVFwdHigh,
       "f3SyncJPTPNetworkProbeHistoryResPDVFwdTotal": f3SyncJPTPNetworkProbeHistoryResPDVFwdTotal,
       "f3SyncJPTPNetworkProbeHistoryFwdScore5": f3SyncJPTPNetworkProbeHistoryFwdScore5,
       "f3SyncJPTPNetworkProbeHistoryFwdScore4": f3SyncJPTPNetworkProbeHistoryFwdScore4,
       "f3SyncJPTPNetworkProbeHistoryFwdScore3": f3SyncJPTPNetworkProbeHistoryFwdScore3,
       "f3SyncJPTPNetworkProbeHistoryAvgResPDVRev": f3SyncJPTPNetworkProbeHistoryAvgResPDVRev,
       "f3SyncJPTPNetworkProbeHistoryResPDVRevLow": f3SyncJPTPNetworkProbeHistoryResPDVRevLow,
       "f3SyncJPTPNetworkProbeHistoryResPDVRevMedium": f3SyncJPTPNetworkProbeHistoryResPDVRevMedium,
       "f3SyncJPTPNetworkProbeHistoryResPDVRevHigh": f3SyncJPTPNetworkProbeHistoryResPDVRevHigh,
       "f3SyncJPTPNetworkProbeHistoryResPDVRevTotal": f3SyncJPTPNetworkProbeHistoryResPDVRevTotal,
       "f3SyncJPTPNetworkProbeHistoryRevScore5": f3SyncJPTPNetworkProbeHistoryRevScore5,
       "f3SyncJPTPNetworkProbeHistoryRevScore4": f3SyncJPTPNetworkProbeHistoryRevScore4,
       "f3SyncJPTPNetworkProbeHistoryRevScore3": f3SyncJPTPNetworkProbeHistoryRevScore3,
       "f3SyncJPTPNetworkProbeHistoryMinRPDVFwd": f3SyncJPTPNetworkProbeHistoryMinRPDVFwd,
       "f3SyncJPTPNetworkProbeHistoryMinRPDVRev": f3SyncJPTPNetworkProbeHistoryMinRPDVRev,
       "f3SyncJPTPNetworkProbeHistoryMinPathAsymmetry": f3SyncJPTPNetworkProbeHistoryMinPathAsymmetry,
       "f3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry": f3SyncJPTPNetworkProbeHistoryMaxPathAsymmetry,
       "f3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry": f3SyncJPTPNetworkProbeHistoryAvgPathAsymmetry,
       "f3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay": f3SyncJPTPNetworkProbeHistoryMinDelayReqPathDelay,
       "f3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay": f3SyncJPTPNetworkProbeHistoryMaxDelayReqPathDelay,
       "f3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay": f3SyncJPTPNetworkProbeHistoryAvgDelayReqPathDelay,
       "f3SyncJPTPNetworkProbeThresholdTable": f3SyncJPTPNetworkProbeThresholdTable,
       "f3SyncJPTPNetworkProbeThresholdEntry": f3SyncJPTPNetworkProbeThresholdEntry,
       "f3SyncJPTPNetworkProbeThresholdIndex": f3SyncJPTPNetworkProbeThresholdIndex,
       "f3SyncJPTPNetworkProbeThresholdInterval": f3SyncJPTPNetworkProbeThresholdInterval,
       "f3SyncJPTPNetworkProbeThresholdVariable": f3SyncJPTPNetworkProbeThresholdVariable,
       "f3SyncJPTPNetworkProbeThresholdValueLo": f3SyncJPTPNetworkProbeThresholdValueLo,
       "f3SyncJPTPNetworkProbeThresholdValueHi": f3SyncJPTPNetworkProbeThresholdValueHi,
       "f3SyncJPTPNetworkProbeThresholdMonValue": f3SyncJPTPNetworkProbeThresholdMonValue,
       "f3SyncJClockProbeStatsTable": f3SyncJClockProbeStatsTable,
       "f3SyncJClockProbeStatsEntry": f3SyncJClockProbeStatsEntry,
       "f3SyncJClockProbeStatsIndex": f3SyncJClockProbeStatsIndex,
       "f3SyncJClockProbeStatsIntervalType": f3SyncJClockProbeStatsIntervalType,
       "f3SyncJClockProbeStatsValid": f3SyncJClockProbeStatsValid,
       "f3SyncJClockProbeStatsAction": f3SyncJClockProbeStatsAction,
       "f3SyncJClockProbeStatsMTIE1s": f3SyncJClockProbeStatsMTIE1s,
       "f3SyncJClockProbeStatsMTIE10s": f3SyncJClockProbeStatsMTIE10s,
       "f3SyncJClockProbeStatsMTIE100s": f3SyncJClockProbeStatsMTIE100s,
       "f3SyncJClockProbeStatsMTIE1000s": f3SyncJClockProbeStatsMTIE1000s,
       "f3SyncJClockProbeStatsMTIE10000s": f3SyncJClockProbeStatsMTIE10000s,
       "f3SyncJClockProbeStatsMTIE50000s": f3SyncJClockProbeStatsMTIE50000s,
       "f3SyncJClockProbeStatsMaxTE": f3SyncJClockProbeStatsMaxTE,
       "f3SyncJClockProbeStatsMaxConstTE": f3SyncJClockProbeStatsMaxConstTE,
       "f3SyncJClockProbeHistoryTable": f3SyncJClockProbeHistoryTable,
       "f3SyncJClockProbeHistoryEntry": f3SyncJClockProbeHistoryEntry,
       "f3SyncJClockProbeHistoryIndex": f3SyncJClockProbeHistoryIndex,
       "f3SyncJClockProbeHistoryTime": f3SyncJClockProbeHistoryTime,
       "f3SyncJClockProbeHistoryValid": f3SyncJClockProbeHistoryValid,
       "f3SyncJClockProbeHistoryAction": f3SyncJClockProbeHistoryAction,
       "f3SyncJClockProbeHistoryMTIE1s": f3SyncJClockProbeHistoryMTIE1s,
       "f3SyncJClockProbeHistoryMTIE10s": f3SyncJClockProbeHistoryMTIE10s,
       "f3SyncJClockProbeHistoryMTIE100s": f3SyncJClockProbeHistoryMTIE100s,
       "f3SyncJClockProbeHistoryMTIE1000s": f3SyncJClockProbeHistoryMTIE1000s,
       "f3SyncJClockProbeHistoryMTIE10000s": f3SyncJClockProbeHistoryMTIE10000s,
       "f3SyncJClockProbeHistoryMTIE50000s": f3SyncJClockProbeHistoryMTIE50000s,
       "f3SyncJClockProbeHistoryMaxTE": f3SyncJClockProbeHistoryMaxTE,
       "f3SyncJClockProbeHistoryMaxConstTE": f3SyncJClockProbeHistoryMaxConstTE,
       "f3SyncJClockProbeThresholdTable": f3SyncJClockProbeThresholdTable,
       "f3SyncJClockProbeThresholdEntry": f3SyncJClockProbeThresholdEntry,
       "f3SyncJClockProbeThresholdIndex": f3SyncJClockProbeThresholdIndex,
       "f3SyncJClockProbeThresholdInterval": f3SyncJClockProbeThresholdInterval,
       "f3SyncJClockProbeThresholdVariable": f3SyncJClockProbeThresholdVariable,
       "f3SyncJClockProbeThresholdValueLo": f3SyncJClockProbeThresholdValueLo,
       "f3SyncJClockProbeThresholdValueHi": f3SyncJClockProbeThresholdValueHi,
       "f3SyncJClockProbeThresholdMonValue": f3SyncJClockProbeThresholdMonValue,
       "f3SyncJPTPClockProbeStatsTable": f3SyncJPTPClockProbeStatsTable,
       "f3SyncJPTPClockProbeStatsEntry": f3SyncJPTPClockProbeStatsEntry,
       "f3SyncJPTPClockProbeStatsIndex": f3SyncJPTPClockProbeStatsIndex,
       "f3SyncJPTPClockProbeStatsIntervalType": f3SyncJPTPClockProbeStatsIntervalType,
       "f3SyncJPTPClockProbeStatsValid": f3SyncJPTPClockProbeStatsValid,
       "f3SyncJPTPClockProbeStatsAction": f3SyncJPTPClockProbeStatsAction,
       "f3SyncJPTPClockProbeStatsMTIE1s": f3SyncJPTPClockProbeStatsMTIE1s,
       "f3SyncJPTPClockProbeStatsMTIE10s": f3SyncJPTPClockProbeStatsMTIE10s,
       "f3SyncJPTPClockProbeStatsMTIE100s": f3SyncJPTPClockProbeStatsMTIE100s,
       "f3SyncJPTPClockProbeStatsMTIE1000s": f3SyncJPTPClockProbeStatsMTIE1000s,
       "f3SyncJPTPClockProbeStatsMTIE10000s": f3SyncJPTPClockProbeStatsMTIE10000s,
       "f3SyncJPTPClockProbeStatsMTIE50000s": f3SyncJPTPClockProbeStatsMTIE50000s,
       "f3SyncJPTPClockProbeStatsMaxTE": f3SyncJPTPClockProbeStatsMaxTE,
       "f3SyncJPTPClockProbeStatsMaxConstTE": f3SyncJPTPClockProbeStatsMaxConstTE,
       "f3SyncJPTPClockProbeHistoryTable": f3SyncJPTPClockProbeHistoryTable,
       "f3SyncJPTPClockProbeHistoryEntry": f3SyncJPTPClockProbeHistoryEntry,
       "f3SyncJPTPClockProbeHistoryIndex": f3SyncJPTPClockProbeHistoryIndex,
       "f3SyncJPTPClockProbeHistoryTime": f3SyncJPTPClockProbeHistoryTime,
       "f3SyncJPTPClockProbeHistoryValid": f3SyncJPTPClockProbeHistoryValid,
       "f3SyncJPTPClockProbeHistoryAction": f3SyncJPTPClockProbeHistoryAction,
       "f3SyncJPTPClockProbeHistoryMTIE1s": f3SyncJPTPClockProbeHistoryMTIE1s,
       "f3SyncJPTPClockProbeHistoryMTIE10s": f3SyncJPTPClockProbeHistoryMTIE10s,
       "f3SyncJPTPClockProbeHistoryMTIE100s": f3SyncJPTPClockProbeHistoryMTIE100s,
       "f3SyncJPTPClockProbeHistoryMTIE1000s": f3SyncJPTPClockProbeHistoryMTIE1000s,
       "f3SyncJPTPClockProbeHistoryMTIE10000s": f3SyncJPTPClockProbeHistoryMTIE10000s,
       "f3SyncJPTPClockProbeHistoryMTIE50000s": f3SyncJPTPClockProbeHistoryMTIE50000s,
       "f3SyncJPTPClockProbeHistoryMaxTE": f3SyncJPTPClockProbeHistoryMaxTE,
       "f3SyncJPTPClockProbeHistoryMaxConstTE": f3SyncJPTPClockProbeHistoryMaxConstTE,
       "f3SyncJPTPClockProbeThresholdTable": f3SyncJPTPClockProbeThresholdTable,
       "f3SyncJPTPClockProbeThresholdEntry": f3SyncJPTPClockProbeThresholdEntry,
       "f3SyncJPTPClockProbeThresholdIndex": f3SyncJPTPClockProbeThresholdIndex,
       "f3SyncJPTPClockProbeThresholdInterval": f3SyncJPTPClockProbeThresholdInterval,
       "f3SyncJPTPClockProbeThresholdVariable": f3SyncJPTPClockProbeThresholdVariable,
       "f3SyncJPTPClockProbeThresholdValueLo": f3SyncJPTPClockProbeThresholdValueLo,
       "f3SyncJPTPClockProbeThresholdValueHi": f3SyncJPTPClockProbeThresholdValueHi,
       "f3SyncJPTPClockProbeThresholdMonValue": f3SyncJPTPClockProbeThresholdMonValue,
       "f3SyncJNotifications": f3SyncJNotifications,
       "f3SyncJPTPNetworkProbeThresholdCrossingAlert": f3SyncJPTPNetworkProbeThresholdCrossingAlert,
       "f3SyncJClockProbeStatusChangeTrap": f3SyncJClockProbeStatusChangeTrap,
       "f3SyncJPTPClockProbeStatusChangeTrap": f3SyncJPTPClockProbeStatusChangeTrap,
       "f3SyncJPTPNetworkProbeStatusChangeTrap": f3SyncJPTPNetworkProbeStatusChangeTrap,
       "f3SyncJClockProbeThresholdCrossingAlert": f3SyncJClockProbeThresholdCrossingAlert,
       "f3SyncJPTPClockProbeThresholdCrossingAlert": f3SyncJPTPClockProbeThresholdCrossingAlert,
       "f3SyncJConformance": f3SyncJConformance,
       "f3SyncJCompliances": f3SyncJCompliances,
       "f3SyncJCompliance": f3SyncJCompliance,
       "f3SyncJGroups": f3SyncJGroups,
       "f3SyncJObjectGroup": f3SyncJObjectGroup,
       "f3SyncJPerfObjectGroup": f3SyncJPerfObjectGroup,
       "f3SyncJNotifGroup": f3SyncJNotifGroup}
)
