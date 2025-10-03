# SNMP MIB module (CM-SAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-SAT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:31 2025
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
 MepDestinationType,
 OperationalState,
 SecondaryState,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "MepDestinationType",
    "OperationalState",
    "SecondaryState",
    "VlanId",
    "VlanPriority")

(neIndex,
 networkElementEntry,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "networkElementEntry",
    "shelfIndex",
    "slotIndex")

(PolicerColorMode,) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "PolicerColorMode")

(EsaProbePktIntervalType,) = mibBuilder.importSymbols(
    "CM-SA-MIB",
    "EsaProbePktIntervalType")

(Dot1agCfmMepIdOrZero,
 dot1agCfmMepEntry) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMepEntry")

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

cmServiceActivationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28)
)
if mibBuilder.loadTexts:
    cmServiceActivationMIB.setRevisions(
        ("2017-04-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ServiceActivationTestMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWay", 1),
          ("twoWay", 2))
    )



class SatProceduresType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("configTestCir", 2),
          ("configTestEir", 3),
          ("configTestCbs", 4),
          ("configTestEbs", 5),
          ("configTestPolicing", 6),
          ("performanceTest", 7))
    )



class SatProceduresList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("configTestCir", 1),
          ("configTestEir", 2),
          ("configTestCbs", 3),
          ("configTestEbs", 4),
          ("configTestPolicing", 5),
          ("performance", 6))
    )


class SatStatus(TextualConvention, Integer32):
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
        *(("completed", 1),
          ("notStarted", 2),
          ("inProgress", 3),
          ("failed", 4),
          ("aborted", 5))
    )



class SatDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("backward", 2))
    )



class SatFramePayloadType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prbs31", 1),
          ("custom", 2))
    )



class SatTestAction(TextualConvention, Integer32):
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
        *(("start", 1),
          ("stop", 2),
          ("notApplicable", 3))
    )



class SatResult(TextualConvention, Integer32):
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
        *(("none", 1),
          ("pass", 2),
          ("fail", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CmServActivationObjects_ObjectIdentity = ObjectIdentity
cmServActivationObjects = _CmServActivationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1)
)
_SatControlTable_Object = MibTable
satControlTable = _SatControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1)
)
if mibBuilder.loadTexts:
    satControlTable.setStatus("current")
_SatControlEntry_Object = MibTableRow
satControlEntry = _SatControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1)
)
satControlEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-SAT-MIB", "satControlIndex"),
)
if mibBuilder.loadTexts:
    satControlEntry.setStatus("current")
_SatControlIndex_Type = Integer32
_SatControlIndex_Object = MibTableColumn
satControlIndex = _SatControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 1),
    _SatControlIndex_Type()
)
satControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satControlIndex.setStatus("current")


class _SatControlName_Type(DisplayString):
    """Custom type satControlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SatControlName_Type.__name__ = "DisplayString"
_SatControlName_Object = MibTableColumn
satControlName = _SatControlName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 2),
    _SatControlName_Type()
)
satControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlName.setStatus("current")
_SatControlTestMode_Type = ServiceActivationTestMode
_SatControlTestMode_Object = MibTableColumn
satControlTestMode = _SatControlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 3),
    _SatControlTestMode_Type()
)
satControlTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlTestMode.setStatus("current")
_SatControlTestProcedures_Type = SatProceduresList
_SatControlTestProcedures_Object = MibTableColumn
satControlTestProcedures = _SatControlTestProcedures_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 4),
    _SatControlTestProcedures_Type()
)
satControlTestProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlTestProcedures.setStatus("current")
_SatControlConfigTestDuration_Type = Integer32
_SatControlConfigTestDuration_Object = MibTableColumn
satControlConfigTestDuration = _SatControlConfigTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 5),
    _SatControlConfigTestDuration_Type()
)
satControlConfigTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlConfigTestDuration.setStatus("current")


class _SatControlConfigCIRTestStepNum_Type(Integer32):
    """Custom type satControlConfigCIRTestStepNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SatControlConfigCIRTestStepNum_Type.__name__ = "Integer32"
_SatControlConfigCIRTestStepNum_Object = MibTableColumn
satControlConfigCIRTestStepNum = _SatControlConfigCIRTestStepNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 6),
    _SatControlConfigCIRTestStepNum_Type()
)
satControlConfigCIRTestStepNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlConfigCIRTestStepNum.setStatus("current")


class _SatControlConfigCIRTestStepDuration_Type(Integer32):
    """Custom type satControlConfigCIRTestStepDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SatControlConfigCIRTestStepDuration_Type.__name__ = "Integer32"
_SatControlConfigCIRTestStepDuration_Object = MibTableColumn
satControlConfigCIRTestStepDuration = _SatControlConfigCIRTestStepDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 7),
    _SatControlConfigCIRTestStepDuration_Type()
)
satControlConfigCIRTestStepDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlConfigCIRTestStepDuration.setStatus("current")
_SatControlPerfTestDuration_Type = Integer32
_SatControlPerfTestDuration_Object = MibTableColumn
satControlPerfTestDuration = _SatControlPerfTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 8),
    _SatControlPerfTestDuration_Type()
)
satControlPerfTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlPerfTestDuration.setStatus("current")
_SatControlStatus_Type = SatStatus
_SatControlStatus_Object = MibTableColumn
satControlStatus = _SatControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 9),
    _SatControlStatus_Type()
)
satControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satControlStatus.setStatus("current")
_SatControlAction_Type = SatTestAction
_SatControlAction_Object = MibTableColumn
satControlAction = _SatControlAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 10),
    _SatControlAction_Type()
)
satControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlAction.setStatus("current")
_SatControlStorageType_Type = StorageType
_SatControlStorageType_Object = MibTableColumn
satControlStorageType = _SatControlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 11),
    _SatControlStorageType_Type()
)
satControlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satControlStorageType.setStatus("current")
_SatControlRowStatus_Type = RowStatus
_SatControlRowStatus_Object = MibTableColumn
satControlRowStatus = _SatControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 12),
    _SatControlRowStatus_Type()
)
satControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satControlRowStatus.setStatus("current")
_SatControlFailCause_Type = DisplayString
_SatControlFailCause_Object = MibTableColumn
satControlFailCause = _SatControlFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 13),
    _SatControlFailCause_Type()
)
satControlFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satControlFailCause.setStatus("current")
_SatControlTestStartTime_Type = DateAndTime
_SatControlTestStartTime_Object = MibTableColumn
satControlTestStartTime = _SatControlTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 14),
    _SatControlTestStartTime_Type()
)
satControlTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satControlTestStartTime.setStatus("current")
_SatControlFlpduTagOverride_Type = TruthValue
_SatControlFlpduTagOverride_Object = MibTableColumn
satControlFlpduTagOverride = _SatControlFlpduTagOverride_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 1, 1, 15),
    _SatControlFlpduTagOverride_Type()
)
satControlFlpduTagOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satControlFlpduTagOverride.setStatus("current")
_SatStreamTable_Object = MibTable
satStreamTable = _SatStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2)
)
if mibBuilder.loadTexts:
    satStreamTable.setStatus("current")
_SatStreamEntry_Object = MibTableRow
satStreamEntry = _SatStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1)
)
satStreamEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-SAT-MIB", "satControlIndex"),
    (0, "CM-SAT-MIB", "satStreamIndex"),
)
if mibBuilder.loadTexts:
    satStreamEntry.setStatus("current")
_SatStreamIndex_Type = Integer32
_SatStreamIndex_Object = MibTableColumn
satStreamIndex = _SatStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 1),
    _SatStreamIndex_Type()
)
satStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satStreamIndex.setStatus("current")


class _SatStreamName_Type(DisplayString):
    """Custom type satStreamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SatStreamName_Type.__name__ = "DisplayString"
_SatStreamName_Object = MibTableColumn
satStreamName = _SatStreamName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 2),
    _SatStreamName_Type()
)
satStreamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamName.setStatus("current")
_SatStreamTestPort_Type = VariablePointer
_SatStreamTestPort_Object = MibTableColumn
satStreamTestPort = _SatStreamTestPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 3),
    _SatStreamTestPort_Type()
)
satStreamTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamTestPort.setStatus("current")
_SatStreamTestDirection_Type = SatDirection
_SatStreamTestDirection_Object = MibTableColumn
satStreamTestDirection = _SatStreamTestDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 4),
    _SatStreamTestDirection_Type()
)
satStreamTestDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamTestDirection.setStatus("current")
_SatStreamDestMacAddress_Type = MacAddress
_SatStreamDestMacAddress_Object = MibTableColumn
satStreamDestMacAddress = _SatStreamDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 5),
    _SatStreamDestMacAddress_Type()
)
satStreamDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDestMacAddress.setStatus("current")
_SatStreamFramePayloadType_Type = SatFramePayloadType
_SatStreamFramePayloadType_Object = MibTableColumn
satStreamFramePayloadType = _SatStreamFramePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 6),
    _SatStreamFramePayloadType_Type()
)
satStreamFramePayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamFramePayloadType.setStatus("current")


class _SatStreamCustomFramePayload_Type(DisplayString):
    """Custom type satStreamCustomFramePayload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SatStreamCustomFramePayload_Type.__name__ = "DisplayString"
_SatStreamCustomFramePayload_Object = MibTableColumn
satStreamCustomFramePayload = _SatStreamCustomFramePayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 7),
    _SatStreamCustomFramePayload_Type()
)
satStreamCustomFramePayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamCustomFramePayload.setStatus("current")
_SatStreamFrameSizeList_Type = DisplayString
_SatStreamFrameSizeList_Object = MibTableColumn
satStreamFrameSizeList = _SatStreamFrameSizeList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 8),
    _SatStreamFrameSizeList_Type()
)
satStreamFrameSizeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamFrameSizeList.setStatus("current")
_SatStreamSacProfileId_Type = VariablePointer
_SatStreamSacProfileId_Object = MibTableColumn
satStreamSacProfileId = _SatStreamSacProfileId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 9),
    _SatStreamSacProfileId_Type()
)
satStreamSacProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamSacProfileId.setStatus("current")
_SatStreamSrcMepId_Type = VariablePointer
_SatStreamSrcMepId_Object = MibTableColumn
satStreamSrcMepId = _SatStreamSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 10),
    _SatStreamSrcMepId_Type()
)
satStreamSrcMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamSrcMepId.setStatus("current")
_SatStreamDestMepType_Type = MepDestinationType
_SatStreamDestMepType_Object = MibTableColumn
satStreamDestMepType = _SatStreamDestMepType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 11),
    _SatStreamDestMepType_Type()
)
satStreamDestMepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDestMepType.setStatus("current")
_SatStreamDestMepId_Type = Integer32
_SatStreamDestMepId_Object = MibTableColumn
satStreamDestMepId = _SatStreamDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 12),
    _SatStreamDestMepId_Type()
)
satStreamDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDestMepId.setStatus("current")
_SatStreamDestMepMacAddr_Type = MacAddress
_SatStreamDestMepMacAddr_Object = MibTableColumn
satStreamDestMepMacAddr = _SatStreamDestMepMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 13),
    _SatStreamDestMepMacAddr_Type()
)
satStreamDestMepMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDestMepMacAddr.setStatus("current")
_SatStreamDmmPacketSize_Type = Integer32
_SatStreamDmmPacketSize_Object = MibTableColumn
satStreamDmmPacketSize = _SatStreamDmmPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 14),
    _SatStreamDmmPacketSize_Type()
)
satStreamDmmPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDmmPacketSize.setStatus("current")
_SatStreamDmmPacketInterval_Type = EsaProbePktIntervalType
_SatStreamDmmPacketInterval_Object = MibTableColumn
satStreamDmmPacketInterval = _SatStreamDmmPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 15),
    _SatStreamDmmPacketInterval_Type()
)
satStreamDmmPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDmmPacketInterval.setStatus("current")
_SatStreamOverallResult_Type = SatResult
_SatStreamOverallResult_Object = MibTableColumn
satStreamOverallResult = _SatStreamOverallResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 16),
    _SatStreamOverallResult_Type()
)
satStreamOverallResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satStreamOverallResult.setStatus("current")
_SatStreamAction_Type = SatTestAction
_SatStreamAction_Object = MibTableColumn
satStreamAction = _SatStreamAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 17),
    _SatStreamAction_Type()
)
satStreamAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamAction.setStatus("current")
_SatStreamStatus_Type = SatStatus
_SatStreamStatus_Object = MibTableColumn
satStreamStatus = _SatStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 18),
    _SatStreamStatus_Type()
)
satStreamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satStreamStatus.setStatus("current")
_SatStreamCurrentTestProcedure_Type = SatProceduresType
_SatStreamCurrentTestProcedure_Object = MibTableColumn
satStreamCurrentTestProcedure = _SatStreamCurrentTestProcedure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 19),
    _SatStreamCurrentTestProcedure_Type()
)
satStreamCurrentTestProcedure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satStreamCurrentTestProcedure.setStatus("current")
_SatStreamCurrentConfigCirTestStep_Type = Integer32
_SatStreamCurrentConfigCirTestStep_Object = MibTableColumn
satStreamCurrentConfigCirTestStep = _SatStreamCurrentConfigCirTestStep_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 20),
    _SatStreamCurrentConfigCirTestStep_Type()
)
satStreamCurrentConfigCirTestStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satStreamCurrentConfigCirTestStep.setStatus("current")
_SatStreamInner1VlanId_Type = VlanId
_SatStreamInner1VlanId_Object = MibTableColumn
satStreamInner1VlanId = _SatStreamInner1VlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 21),
    _SatStreamInner1VlanId_Type()
)
satStreamInner1VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner1VlanId.setStatus("current")
_SatStreamInner1VlanPri_Type = VlanPriority
_SatStreamInner1VlanPri_Object = MibTableColumn
satStreamInner1VlanPri = _SatStreamInner1VlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 22),
    _SatStreamInner1VlanPri_Type()
)
satStreamInner1VlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner1VlanPri.setStatus("current")
_SatStreamInner1VlanEnabled_Type = TruthValue
_SatStreamInner1VlanEnabled_Object = MibTableColumn
satStreamInner1VlanEnabled = _SatStreamInner1VlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 23),
    _SatStreamInner1VlanEnabled_Type()
)
satStreamInner1VlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner1VlanEnabled.setStatus("current")
_SatStreamInner1ValnEtherType_Type = Integer32
_SatStreamInner1ValnEtherType_Object = MibTableColumn
satStreamInner1ValnEtherType = _SatStreamInner1ValnEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 24),
    _SatStreamInner1ValnEtherType_Type()
)
satStreamInner1ValnEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner1ValnEtherType.setStatus("current")
_SatStreamInner2VlanId_Type = VlanId
_SatStreamInner2VlanId_Object = MibTableColumn
satStreamInner2VlanId = _SatStreamInner2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 25),
    _SatStreamInner2VlanId_Type()
)
satStreamInner2VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner2VlanId.setStatus("current")
_SatStreamInner2VlanPri_Type = VlanPriority
_SatStreamInner2VlanPri_Object = MibTableColumn
satStreamInner2VlanPri = _SatStreamInner2VlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 26),
    _SatStreamInner2VlanPri_Type()
)
satStreamInner2VlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner2VlanPri.setStatus("current")
_SatStreamInner2VlanEnabled_Type = TruthValue
_SatStreamInner2VlanEnabled_Object = MibTableColumn
satStreamInner2VlanEnabled = _SatStreamInner2VlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 27),
    _SatStreamInner2VlanEnabled_Type()
)
satStreamInner2VlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner2VlanEnabled.setStatus("current")
_SatStreamInner2VlanEtherType_Type = Integer32
_SatStreamInner2VlanEtherType_Object = MibTableColumn
satStreamInner2VlanEtherType = _SatStreamInner2VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 28),
    _SatStreamInner2VlanEtherType_Type()
)
satStreamInner2VlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamInner2VlanEtherType.setStatus("current")
_SatStreamOuterVlanId_Type = VlanId
_SatStreamOuterVlanId_Object = MibTableColumn
satStreamOuterVlanId = _SatStreamOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 29),
    _SatStreamOuterVlanId_Type()
)
satStreamOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamOuterVlanId.setStatus("current")
_SatStreamOuterVlanPri_Type = VlanPriority
_SatStreamOuterVlanPri_Object = MibTableColumn
satStreamOuterVlanPri = _SatStreamOuterVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 30),
    _SatStreamOuterVlanPri_Type()
)
satStreamOuterVlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamOuterVlanPri.setStatus("current")
_SatStreamOuterVlanEnabled_Type = TruthValue
_SatStreamOuterVlanEnabled_Object = MibTableColumn
satStreamOuterVlanEnabled = _SatStreamOuterVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 31),
    _SatStreamOuterVlanEnabled_Type()
)
satStreamOuterVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamOuterVlanEnabled.setStatus("current")
_SatStreamOuterVlanEtherType_Type = Integer32
_SatStreamOuterVlanEtherType_Object = MibTableColumn
satStreamOuterVlanEtherType = _SatStreamOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 32),
    _SatStreamOuterVlanEtherType_Type()
)
satStreamOuterVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamOuterVlanEtherType.setStatus("current")
_SatStreamDeiEnabled_Type = TruthValue
_SatStreamDeiEnabled_Object = MibTableColumn
satStreamDeiEnabled = _SatStreamDeiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 33),
    _SatStreamDeiEnabled_Type()
)
satStreamDeiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDeiEnabled.setStatus("current")
_SatStreamGreenPcp_Type = Integer32
_SatStreamGreenPcp_Object = MibTableColumn
satStreamGreenPcp = _SatStreamGreenPcp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 34),
    _SatStreamGreenPcp_Type()
)
satStreamGreenPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamGreenPcp.setStatus("current")
_SatStreamYellowPcp_Type = Integer32
_SatStreamYellowPcp_Object = MibTableColumn
satStreamYellowPcp = _SatStreamYellowPcp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 35),
    _SatStreamYellowPcp_Type()
)
satStreamYellowPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamYellowPcp.setStatus("current")
_SatStreamColorMode_Type = PolicerColorMode
_SatStreamColorMode_Object = MibTableColumn
satStreamColorMode = _SatStreamColorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 36),
    _SatStreamColorMode_Type()
)
satStreamColorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamColorMode.setStatus("current")
_SatStreamCirLo_Type = Unsigned32
_SatStreamCirLo_Object = MibTableColumn
satStreamCirLo = _SatStreamCirLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 37),
    _SatStreamCirLo_Type()
)
satStreamCirLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamCirLo.setStatus("current")
_SatStreamCirHi_Type = Unsigned32
_SatStreamCirHi_Object = MibTableColumn
satStreamCirHi = _SatStreamCirHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 38),
    _SatStreamCirHi_Type()
)
satStreamCirHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamCirHi.setStatus("current")
_SatStreamEirLo_Type = Unsigned32
_SatStreamEirLo_Object = MibTableColumn
satStreamEirLo = _SatStreamEirLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 39),
    _SatStreamEirLo_Type()
)
satStreamEirLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamEirLo.setStatus("current")
_SatStreamEirHi_Type = Unsigned32
_SatStreamEirHi_Object = MibTableColumn
satStreamEirHi = _SatStreamEirHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 40),
    _SatStreamEirHi_Type()
)
satStreamEirHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamEirHi.setStatus("current")
_SatStreamCbs_Type = Unsigned32
_SatStreamCbs_Object = MibTableColumn
satStreamCbs = _SatStreamCbs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 41),
    _SatStreamCbs_Type()
)
satStreamCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamCbs.setStatus("current")
_SatStreamEbs_Type = Unsigned32
_SatStreamEbs_Object = MibTableColumn
satStreamEbs = _SatStreamEbs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 42),
    _SatStreamEbs_Type()
)
satStreamEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamEbs.setStatus("current")
_SatStreamStorageType_Type = StorageType
_SatStreamStorageType_Object = MibTableColumn
satStreamStorageType = _SatStreamStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 43),
    _SatStreamStorageType_Type()
)
satStreamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satStreamStorageType.setStatus("current")
_SatStreamRowStatus_Type = RowStatus
_SatStreamRowStatus_Object = MibTableColumn
satStreamRowStatus = _SatStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 44),
    _SatStreamRowStatus_Type()
)
satStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satStreamRowStatus.setStatus("current")
_SatStreamDmmPktPriority_Type = VlanPriority
_SatStreamDmmPktPriority_Object = MibTableColumn
satStreamDmmPktPriority = _SatStreamDmmPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 45),
    _SatStreamDmmPktPriority_Type()
)
satStreamDmmPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDmmPktPriority.setStatus("current")
_SatStreamMFactor_Type = Unsigned32
_SatStreamMFactor_Object = MibTableColumn
satStreamMFactor = _SatStreamMFactor_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 46),
    _SatStreamMFactor_Type()
)
satStreamMFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamMFactor.setStatus("current")
_SatStreamDestMepEnabled_Type = TruthValue
_SatStreamDestMepEnabled_Object = MibTableColumn
satStreamDestMepEnabled = _SatStreamDestMepEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 47),
    _SatStreamDestMepEnabled_Type()
)
satStreamDestMepEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamDestMepEnabled.setStatus("current")
_SatStreamLlActivateEnabled_Type = TruthValue
_SatStreamLlActivateEnabled_Object = MibTableColumn
satStreamLlActivateEnabled = _SatStreamLlActivateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 2, 1, 48),
    _SatStreamLlActivateEnabled_Type()
)
satStreamLlActivateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satStreamLlActivateEnabled.setStatus("current")
_SatResultStatsTable_Object = MibTable
satResultStatsTable = _SatResultStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3)
)
if mibBuilder.loadTexts:
    satResultStatsTable.setStatus("current")
_SatResultStatsEntry_Object = MibTableRow
satResultStatsEntry = _SatResultStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1)
)
satResultStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-SAT-MIB", "satControlIndex"),
    (0, "CM-SAT-MIB", "satStreamIndex"),
    (0, "CM-SAT-MIB", "satResultStatsTestType"),
    (0, "CM-SAT-MIB", "satResultStatsStepNumber"),
)
if mibBuilder.loadTexts:
    satResultStatsEntry.setStatus("current")
_SatResultStatsTestType_Type = SatProceduresType
_SatResultStatsTestType_Object = MibTableColumn
satResultStatsTestType = _SatResultStatsTestType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 1),
    _SatResultStatsTestType_Type()
)
satResultStatsTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satResultStatsTestType.setStatus("current")
_SatResultStatsStepNumber_Type = Integer32
_SatResultStatsStepNumber_Object = MibTableColumn
satResultStatsStepNumber = _SatResultStatsStepNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 2),
    _SatResultStatsStepNumber_Type()
)
satResultStatsStepNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satResultStatsStepNumber.setStatus("current")
_SatResultStatsSessionId_Type = Unsigned32
_SatResultStatsSessionId_Object = MibTableColumn
satResultStatsSessionId = _SatResultStatsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 3),
    _SatResultStatsSessionId_Type()
)
satResultStatsSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsSessionId.setStatus("current")
_SatResultStatsStartTime_Type = DateAndTime
_SatResultStatsStartTime_Object = MibTableColumn
satResultStatsStartTime = _SatResultStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 4),
    _SatResultStatsStartTime_Type()
)
satResultStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsStartTime.setStatus("current")
_SatResultStatsEndTime_Type = DateAndTime
_SatResultStatsEndTime_Object = MibTableColumn
satResultStatsEndTime = _SatResultStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 5),
    _SatResultStatsEndTime_Type()
)
satResultStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsEndTime.setStatus("current")
_SatResultStatsStatus_Type = SatStatus
_SatResultStatsStatus_Object = MibTableColumn
satResultStatsStatus = _SatResultStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 6),
    _SatResultStatsStatus_Type()
)
satResultStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsStatus.setStatus("current")
_SatResultStatsResult_Type = SatResult
_SatResultStatsResult_Object = MibTableColumn
satResultStatsResult = _SatResultStatsResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 7),
    _SatResultStatsResult_Type()
)
satResultStatsResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsResult.setStatus("current")
_SatResultStatsMinIRGMeasured_Type = Counter64
_SatResultStatsMinIRGMeasured_Object = MibTableColumn
satResultStatsMinIRGMeasured = _SatResultStatsMinIRGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 8),
    _SatResultStatsMinIRGMeasured_Type()
)
satResultStatsMinIRGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsMinIRGMeasured.setStatus("current")
_SatResultStatsAvgIRGMeasured_Type = Counter64
_SatResultStatsAvgIRGMeasured_Object = MibTableColumn
satResultStatsAvgIRGMeasured = _SatResultStatsAvgIRGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 9),
    _SatResultStatsAvgIRGMeasured_Type()
)
satResultStatsAvgIRGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsAvgIRGMeasured.setStatus("current")
_SatResultStatsMaxIRGMeasured_Type = Counter64
_SatResultStatsMaxIRGMeasured_Object = MibTableColumn
satResultStatsMaxIRGMeasured = _SatResultStatsMaxIRGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 10),
    _SatResultStatsMaxIRGMeasured_Type()
)
satResultStatsMaxIRGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsMaxIRGMeasured.setStatus("current")
_SatResultStatsMinIRYMeasured_Type = Counter64
_SatResultStatsMinIRYMeasured_Object = MibTableColumn
satResultStatsMinIRYMeasured = _SatResultStatsMinIRYMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 11),
    _SatResultStatsMinIRYMeasured_Type()
)
satResultStatsMinIRYMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsMinIRYMeasured.setStatus("current")
_SatResultStatsAvgIRYMeasured_Type = Counter64
_SatResultStatsAvgIRYMeasured_Object = MibTableColumn
satResultStatsAvgIRYMeasured = _SatResultStatsAvgIRYMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 12),
    _SatResultStatsAvgIRYMeasured_Type()
)
satResultStatsAvgIRYMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsAvgIRYMeasured.setStatus("current")
_SatResultStatsMaxIRYMeasured_Type = Counter64
_SatResultStatsMaxIRYMeasured_Object = MibTableColumn
satResultStatsMaxIRYMeasured = _SatResultStatsMaxIRYMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 13),
    _SatResultStatsMaxIRYMeasured_Type()
)
satResultStatsMaxIRYMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsMaxIRYMeasured.setStatus("current")
_SatResultStatsFlrGMeasured_Type = Integer32
_SatResultStatsFlrGMeasured_Object = MibTableColumn
satResultStatsFlrGMeasured = _SatResultStatsFlrGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 14),
    _SatResultStatsFlrGMeasured_Type()
)
satResultStatsFlrGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsFlrGMeasured.setStatus("current")
_SatResultStatsFlrYMeasured_Type = Integer32
_SatResultStatsFlrYMeasured_Object = MibTableColumn
satResultStatsFlrYMeasured = _SatResultStatsFlrYMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 15),
    _SatResultStatsFlrYMeasured_Type()
)
satResultStatsFlrYMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsFlrYMeasured.setStatus("current")
_SatResultStatsFlrGCounts_Type = Counter64
_SatResultStatsFlrGCounts_Object = MibTableColumn
satResultStatsFlrGCounts = _SatResultStatsFlrGCounts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 16),
    _SatResultStatsFlrGCounts_Type()
)
satResultStatsFlrGCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsFlrGCounts.setStatus("current")
_SatResultStatsFlrYCounts_Type = Counter64
_SatResultStatsFlrYCounts_Object = MibTableColumn
satResultStatsFlrYCounts = _SatResultStatsFlrYCounts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 17),
    _SatResultStatsFlrYCounts_Type()
)
satResultStatsFlrYCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsFlrYCounts.setStatus("current")
_SatResultStatsMinFTDGMeasured_Type = Unsigned32
_SatResultStatsMinFTDGMeasured_Object = MibTableColumn
satResultStatsMinFTDGMeasured = _SatResultStatsMinFTDGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 18),
    _SatResultStatsMinFTDGMeasured_Type()
)
satResultStatsMinFTDGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsMinFTDGMeasured.setStatus("current")
_SatResultStatsAvgFTDGMeasured_Type = Unsigned32
_SatResultStatsAvgFTDGMeasured_Object = MibTableColumn
satResultStatsAvgFTDGMeasured = _SatResultStatsAvgFTDGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 19),
    _SatResultStatsAvgFTDGMeasured_Type()
)
satResultStatsAvgFTDGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsAvgFTDGMeasured.setStatus("current")
_SatResultStatsMaxFTDGMeasured_Type = Unsigned32
_SatResultStatsMaxFTDGMeasured_Object = MibTableColumn
satResultStatsMaxFTDGMeasured = _SatResultStatsMaxFTDGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 20),
    _SatResultStatsMaxFTDGMeasured_Type()
)
satResultStatsMaxFTDGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsMaxFTDGMeasured.setStatus("current")
_SatResultStatsIMinFDVGMeasured_Type = Unsigned32
_SatResultStatsIMinFDVGMeasured_Object = MibTableColumn
satResultStatsIMinFDVGMeasured = _SatResultStatsIMinFDVGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 21),
    _SatResultStatsIMinFDVGMeasured_Type()
)
satResultStatsIMinFDVGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsIMinFDVGMeasured.setStatus("current")
_SatResultStatsIAvgFDVGMeasured_Type = Unsigned32
_SatResultStatsIAvgFDVGMeasured_Object = MibTableColumn
satResultStatsIAvgFDVGMeasured = _SatResultStatsIAvgFDVGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 22),
    _SatResultStatsIAvgFDVGMeasured_Type()
)
satResultStatsIAvgFDVGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsIAvgFDVGMeasured.setStatus("current")
_SatResultStatsIMaxFDVGMeasured_Type = Unsigned32
_SatResultStatsIMaxFDVGMeasured_Object = MibTableColumn
satResultStatsIMaxFDVGMeasured = _SatResultStatsIMaxFDVGMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 23),
    _SatResultStatsIMaxFDVGMeasured_Type()
)
satResultStatsIMaxFDVGMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsIMaxFDVGMeasured.setStatus("current")
_SatResultStatsISyncErrorsNum_Type = Unsigned32
_SatResultStatsISyncErrorsNum_Object = MibTableColumn
satResultStatsISyncErrorsNum = _SatResultStatsISyncErrorsNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 24),
    _SatResultStatsISyncErrorsNum_Type()
)
satResultStatsISyncErrorsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsISyncErrorsNum.setStatus("current")
_SatResultStatsIfNegFLG_Type = TruthValue
_SatResultStatsIfNegFLG_Object = MibTableColumn
satResultStatsIfNegFLG = _SatResultStatsIfNegFLG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 25),
    _SatResultStatsIfNegFLG_Type()
)
satResultStatsIfNegFLG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsIfNegFLG.setStatus("current")
_SatResultStatsIfNegFLY_Type = TruthValue
_SatResultStatsIfNegFLY_Object = MibTableColumn
satResultStatsIfNegFLY = _SatResultStatsIfNegFLY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 26),
    _SatResultStatsIfNegFLY_Type()
)
satResultStatsIfNegFLY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsIfNegFLY.setStatus("current")
_SatResultStatsAvgIRT_Type = Counter64
_SatResultStatsAvgIRT_Object = MibTableColumn
satResultStatsAvgIRT = _SatResultStatsAvgIRT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 27),
    _SatResultStatsAvgIRT_Type()
)
satResultStatsAvgIRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsAvgIRT.setStatus("current")
_SatResultStatsFlrTMeasured_Type = Integer32
_SatResultStatsFlrTMeasured_Object = MibTableColumn
satResultStatsFlrTMeasured = _SatResultStatsFlrTMeasured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 28),
    _SatResultStatsFlrTMeasured_Type()
)
satResultStatsFlrTMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsFlrTMeasured.setStatus("current")
_SatResultStatsFlTCounts_Type = Counter64
_SatResultStatsFlTCounts_Object = MibTableColumn
satResultStatsFlTCounts = _SatResultStatsFlTCounts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 29),
    _SatResultStatsFlTCounts_Type()
)
satResultStatsFlTCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsFlTCounts.setStatus("current")
_SatResultStatsIfNegFLT_Type = TruthValue
_SatResultStatsIfNegFLT_Object = MibTableColumn
satResultStatsIfNegFLT = _SatResultStatsIfNegFLT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 3, 1, 30),
    _SatResultStatsIfNegFLT_Type()
)
satResultStatsIfNegFLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResultStatsIfNegFLT.setStatus("current")
_SatSacProfileTable_Object = MibTable
satSacProfileTable = _SatSacProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4)
)
if mibBuilder.loadTexts:
    satSacProfileTable.setStatus("current")
_SatSacProfileEntry_Object = MibTableRow
satSacProfileEntry = _SatSacProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1)
)
satSacProfileEntry.setIndexNames(
    (0, "CM-SAT-MIB", "satSacProfileIndex"),
)
if mibBuilder.loadTexts:
    satSacProfileEntry.setStatus("current")
_SatSacProfileIndex_Type = Integer32
_SatSacProfileIndex_Object = MibTableColumn
satSacProfileIndex = _SatSacProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1, 1),
    _SatSacProfileIndex_Type()
)
satSacProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satSacProfileIndex.setStatus("current")


class _SatSacProfileAlias_Type(DisplayString):
    """Custom type satSacProfileAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SatSacProfileAlias_Type.__name__ = "DisplayString"
_SatSacProfileAlias_Object = MibTableColumn
satSacProfileAlias = _SatSacProfileAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1, 2),
    _SatSacProfileAlias_Type()
)
satSacProfileAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satSacProfileAlias.setStatus("current")
_SatSacProfileFLR_Type = Integer32
_SatSacProfileFLR_Object = MibTableColumn
satSacProfileFLR = _SatSacProfileFLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1, 3),
    _SatSacProfileFLR_Type()
)
satSacProfileFLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satSacProfileFLR.setStatus("current")
_SatSacProfileFTD_Type = Unsigned32
_SatSacProfileFTD_Object = MibTableColumn
satSacProfileFTD = _SatSacProfileFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1, 4),
    _SatSacProfileFTD_Type()
)
satSacProfileFTD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satSacProfileFTD.setStatus("current")
_SatSacProfileFDV_Type = Unsigned32
_SatSacProfileFDV_Object = MibTableColumn
satSacProfileFDV = _SatSacProfileFDV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1, 5),
    _SatSacProfileFDV_Type()
)
satSacProfileFDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satSacProfileFDV.setStatus("current")
_SatSacProfileStorageType_Type = StorageType
_SatSacProfileStorageType_Object = MibTableColumn
satSacProfileStorageType = _SatSacProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1, 6),
    _SatSacProfileStorageType_Type()
)
satSacProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satSacProfileStorageType.setStatus("current")
_SatSacProfileRowStatus_Type = RowStatus
_SatSacProfileRowStatus_Object = MibTableColumn
satSacProfileRowStatus = _SatSacProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 4, 1, 7),
    _SatSacProfileRowStatus_Type()
)
satSacProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satSacProfileRowStatus.setStatus("current")
_SatResponderSessionTable_Object = MibTable
satResponderSessionTable = _SatResponderSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5)
)
if mibBuilder.loadTexts:
    satResponderSessionTable.setStatus("current")
_SatResponderSessionEntry_Object = MibTableRow
satResponderSessionEntry = _SatResponderSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5, 1)
)
satResponderSessionEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-SAT-MIB", "satResponderSessionIndex"),
)
if mibBuilder.loadTexts:
    satResponderSessionEntry.setStatus("current")
_SatResponderSessionIndex_Type = Unsigned32
_SatResponderSessionIndex_Object = MibTableColumn
satResponderSessionIndex = _SatResponderSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5, 1, 1),
    _SatResponderSessionIndex_Type()
)
satResponderSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satResponderSessionIndex.setStatus("current")
_SatResponderSessionId_Type = Unsigned32
_SatResponderSessionId_Object = MibTableColumn
satResponderSessionId = _SatResponderSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5, 1, 2),
    _SatResponderSessionId_Type()
)
satResponderSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResponderSessionId.setStatus("current")
_SatResponderSessionControlMepMacAddr_Type = MacAddress
_SatResponderSessionControlMepMacAddr_Object = MibTableColumn
satResponderSessionControlMepMacAddr = _SatResponderSessionControlMepMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5, 1, 3),
    _SatResponderSessionControlMepMacAddr_Type()
)
satResponderSessionControlMepMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResponderSessionControlMepMacAddr.setStatus("current")
_SatResponderSessionMepId_Type = VariablePointer
_SatResponderSessionMepId_Object = MibTableColumn
satResponderSessionMepId = _SatResponderSessionMepId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5, 1, 4),
    _SatResponderSessionMepId_Type()
)
satResponderSessionMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satResponderSessionMepId.setStatus("current")
_SatResponderSessionStorageType_Type = StorageType
_SatResponderSessionStorageType_Object = MibTableColumn
satResponderSessionStorageType = _SatResponderSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5, 1, 5),
    _SatResponderSessionStorageType_Type()
)
satResponderSessionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satResponderSessionStorageType.setStatus("current")
_SatResponderSessionRowStatus_Type = RowStatus
_SatResponderSessionRowStatus_Object = MibTableColumn
satResponderSessionRowStatus = _SatResponderSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 5, 1, 6),
    _SatResponderSessionRowStatus_Type()
)
satResponderSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    satResponderSessionRowStatus.setStatus("current")
_NetworkElementSatParamsTable_Object = MibTable
networkElementSatParamsTable = _NetworkElementSatParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 6)
)
if mibBuilder.loadTexts:
    networkElementSatParamsTable.setStatus("current")
_NetworkElementSatParamsEntry_Object = MibTableRow
networkElementSatParamsEntry = _NetworkElementSatParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 6, 1)
)
if mibBuilder.loadTexts:
    networkElementSatParamsEntry.setStatus("current")
_NeSatParamsEtherType_Type = Unsigned32
_NeSatParamsEtherType_Object = MibTableColumn
neSatParamsEtherType = _NeSatParamsEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 6, 1, 1),
    _NeSatParamsEtherType_Type()
)
neSatParamsEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neSatParamsEtherType.setStatus("current")
_SatCfmMepExtTable_Object = MibTable
satCfmMepExtTable = _SatCfmMepExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 7)
)
if mibBuilder.loadTexts:
    satCfmMepExtTable.setStatus("current")
_SatCfmMepExtEntry_Object = MibTableRow
satCfmMepExtEntry = _SatCfmMepExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 7, 1)
)
if mibBuilder.loadTexts:
    satCfmMepExtEntry.setStatus("current")
_SatCfmMepSatResponderEnabled_Type = TruthValue
_SatCfmMepSatResponderEnabled_Object = MibTableColumn
satCfmMepSatResponderEnabled = _SatCfmMepSatResponderEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 1, 7, 1, 1),
    _SatCfmMepSatResponderEnabled_Type()
)
satCfmMepSatResponderEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satCfmMepSatResponderEnabled.setStatus("current")
_CmServActivationNotifications_ObjectIdentity = ObjectIdentity
cmServActivationNotifications = _CmServActivationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 2)
)
_CmServActivationConformance_ObjectIdentity = ObjectIdentity
cmServActivationConformance = _CmServActivationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 3)
)
_CmServActivationCompliances_ObjectIdentity = ObjectIdentity
cmServActivationCompliances = _CmServActivationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 3, 1)
)
_CmServActivationGroups_ObjectIdentity = ObjectIdentity
cmServActivationGroups = _CmServActivationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 3, 2)
)
networkElementEntry.registerAugmentions(
    ("CM-SAT-MIB",
     "networkElementSatParamsEntry")
)
networkElementSatParamsEntry.setIndexNames(*networkElementEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("CM-SAT-MIB",
     "satCfmMepExtEntry")
)
satCfmMepExtEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

cmSatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 3, 2, 1)
)
cmSatGroup.setObjects(
      *(("CM-SAT-MIB", "satControlIndex"),
        ("CM-SAT-MIB", "satControlName"),
        ("CM-SAT-MIB", "satControlTestMode"),
        ("CM-SAT-MIB", "satControlTestProcedures"),
        ("CM-SAT-MIB", "satControlConfigTestDuration"),
        ("CM-SAT-MIB", "satControlConfigCIRTestStepNum"),
        ("CM-SAT-MIB", "satControlConfigCIRTestStepDuration"),
        ("CM-SAT-MIB", "satControlPerfTestDuration"),
        ("CM-SAT-MIB", "satControlStatus"),
        ("CM-SAT-MIB", "satControlAction"),
        ("CM-SAT-MIB", "satControlFailCause"),
        ("CM-SAT-MIB", "satControlTestStartTime"),
        ("CM-SAT-MIB", "satControlFlpduTagOverride"),
        ("CM-SAT-MIB", "satStreamIndex"),
        ("CM-SAT-MIB", "satStreamName"),
        ("CM-SAT-MIB", "satStreamTestPort"),
        ("CM-SAT-MIB", "satStreamTestDirection"),
        ("CM-SAT-MIB", "satStreamDestMacAddress"),
        ("CM-SAT-MIB", "satStreamFramePayloadType"),
        ("CM-SAT-MIB", "satStreamCustomFramePayload"),
        ("CM-SAT-MIB", "satStreamFrameSizeList"),
        ("CM-SAT-MIB", "satStreamSacProfileId"),
        ("CM-SAT-MIB", "satStreamSrcMepId"),
        ("CM-SAT-MIB", "satStreamDestMepType"),
        ("CM-SAT-MIB", "satStreamDestMepId"),
        ("CM-SAT-MIB", "satStreamDestMepMacAddr"),
        ("CM-SAT-MIB", "satStreamDmmPacketSize"),
        ("CM-SAT-MIB", "satStreamDmmPacketInterval"),
        ("CM-SAT-MIB", "satStreamOverallResult"),
        ("CM-SAT-MIB", "satStreamAction"),
        ("CM-SAT-MIB", "satStreamStatus"),
        ("CM-SAT-MIB", "satStreamCurrentTestProcedure"),
        ("CM-SAT-MIB", "satStreamCurrentConfigCirTestStep"),
        ("CM-SAT-MIB", "satStreamInner1VlanId"),
        ("CM-SAT-MIB", "satStreamInner1VlanPri"),
        ("CM-SAT-MIB", "satStreamInner1VlanEnabled"),
        ("CM-SAT-MIB", "satStreamInner1ValnEtherType"),
        ("CM-SAT-MIB", "satStreamInner2VlanId"),
        ("CM-SAT-MIB", "satStreamInner2VlanPri"),
        ("CM-SAT-MIB", "satStreamInner2VlanEnabled"),
        ("CM-SAT-MIB", "satStreamInner2VlanEtherType"),
        ("CM-SAT-MIB", "satStreamOuterVlanId"),
        ("CM-SAT-MIB", "satStreamOuterVlanPri"),
        ("CM-SAT-MIB", "satStreamOuterVlanEnabled"),
        ("CM-SAT-MIB", "satStreamOuterVlanEtherType"),
        ("CM-SAT-MIB", "satStreamDeiEnabled"),
        ("CM-SAT-MIB", "satStreamGreenPcp"),
        ("CM-SAT-MIB", "satStreamYellowPcp"),
        ("CM-SAT-MIB", "satStreamColorMode"),
        ("CM-SAT-MIB", "satStreamCirLo"),
        ("CM-SAT-MIB", "satStreamCirHi"),
        ("CM-SAT-MIB", "satStreamEirLo"),
        ("CM-SAT-MIB", "satStreamEirHi"),
        ("CM-SAT-MIB", "satStreamCbs"),
        ("CM-SAT-MIB", "satStreamEbs"),
        ("CM-SAT-MIB", "satStreamStorageType"),
        ("CM-SAT-MIB", "satStreamRowStatus"),
        ("CM-SAT-MIB", "satControlStorageType"),
        ("CM-SAT-MIB", "satControlRowStatus"),
        ("CM-SAT-MIB", "satStreamDmmPktPriority"),
        ("CM-SAT-MIB", "satStreamMFactor"),
        ("CM-SAT-MIB", "satStreamDestMepEnabled"),
        ("CM-SAT-MIB", "satStreamLlActivateEnabled"),
        ("CM-SAT-MIB", "satResultStatsSessionId"),
        ("CM-SAT-MIB", "satResultStatsTestType"),
        ("CM-SAT-MIB", "satResultStatsStepNumber"),
        ("CM-SAT-MIB", "satResultStatsStartTime"),
        ("CM-SAT-MIB", "satResultStatsEndTime"),
        ("CM-SAT-MIB", "satResultStatsStatus"),
        ("CM-SAT-MIB", "satResultStatsResult"),
        ("CM-SAT-MIB", "satResultStatsMinIRGMeasured"),
        ("CM-SAT-MIB", "satResultStatsAvgIRGMeasured"),
        ("CM-SAT-MIB", "satResultStatsMaxIRGMeasured"),
        ("CM-SAT-MIB", "satResultStatsMinIRYMeasured"),
        ("CM-SAT-MIB", "satResultStatsAvgIRYMeasured"),
        ("CM-SAT-MIB", "satResultStatsMaxIRYMeasured"),
        ("CM-SAT-MIB", "satResultStatsFlrGMeasured"),
        ("CM-SAT-MIB", "satResultStatsFlrYMeasured"),
        ("CM-SAT-MIB", "satResultStatsFlrGCounts"),
        ("CM-SAT-MIB", "satResultStatsFlrYCounts"),
        ("CM-SAT-MIB", "satResultStatsMinFTDGMeasured"),
        ("CM-SAT-MIB", "satResultStatsAvgFTDGMeasured"),
        ("CM-SAT-MIB", "satResultStatsMaxFTDGMeasured"),
        ("CM-SAT-MIB", "satResultStatsIMinFDVGMeasured"),
        ("CM-SAT-MIB", "satResultStatsIAvgFDVGMeasured"),
        ("CM-SAT-MIB", "satResultStatsIMaxFDVGMeasured"),
        ("CM-SAT-MIB", "satResultStatsISyncErrorsNum"),
        ("CM-SAT-MIB", "satResultStatsIfNegFLG"),
        ("CM-SAT-MIB", "satResultStatsIfNegFLY"),
        ("CM-SAT-MIB", "satResultStatsAvgIRT"),
        ("CM-SAT-MIB", "satResultStatsFlrTMeasured"),
        ("CM-SAT-MIB", "satResultStatsFlTCounts"),
        ("CM-SAT-MIB", "satResultStatsIfNegFLT"),
        ("CM-SAT-MIB", "satSacProfileIndex"),
        ("CM-SAT-MIB", "satSacProfileAlias"),
        ("CM-SAT-MIB", "satSacProfileFLR"),
        ("CM-SAT-MIB", "satSacProfileFTD"),
        ("CM-SAT-MIB", "satSacProfileFDV"),
        ("CM-SAT-MIB", "satSacProfileStorageType"),
        ("CM-SAT-MIB", "satSacProfileRowStatus"),
        ("CM-SAT-MIB", "satResponderSessionIndex"),
        ("CM-SAT-MIB", "satResponderSessionId"),
        ("CM-SAT-MIB", "satResponderSessionControlMepMacAddr"),
        ("CM-SAT-MIB", "satResponderSessionMepId"),
        ("CM-SAT-MIB", "satResponderSessionStorageType"),
        ("CM-SAT-MIB", "satResponderSessionRowStatus"),
        ("CM-SAT-MIB", "satCfmMepSatResponderEnabled"))
)
if mibBuilder.loadTexts:
    cmSatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmServActivationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 28, 3, 1, 1)
)
cmServActivationCompliance.setObjects(
    ("CM-SAT-MIB", "cmSatGroup")
)
if mibBuilder.loadTexts:
    cmServActivationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-SAT-MIB",
    **{"ServiceActivationTestMode": ServiceActivationTestMode,
       "SatProceduresType": SatProceduresType,
       "SatProceduresList": SatProceduresList,
       "SatStatus": SatStatus,
       "SatDirection": SatDirection,
       "SatFramePayloadType": SatFramePayloadType,
       "SatTestAction": SatTestAction,
       "SatResult": SatResult,
       "cmServiceActivationMIB": cmServiceActivationMIB,
       "cmServActivationObjects": cmServActivationObjects,
       "satControlTable": satControlTable,
       "satControlEntry": satControlEntry,
       "satControlIndex": satControlIndex,
       "satControlName": satControlName,
       "satControlTestMode": satControlTestMode,
       "satControlTestProcedures": satControlTestProcedures,
       "satControlConfigTestDuration": satControlConfigTestDuration,
       "satControlConfigCIRTestStepNum": satControlConfigCIRTestStepNum,
       "satControlConfigCIRTestStepDuration": satControlConfigCIRTestStepDuration,
       "satControlPerfTestDuration": satControlPerfTestDuration,
       "satControlStatus": satControlStatus,
       "satControlAction": satControlAction,
       "satControlStorageType": satControlStorageType,
       "satControlRowStatus": satControlRowStatus,
       "satControlFailCause": satControlFailCause,
       "satControlTestStartTime": satControlTestStartTime,
       "satControlFlpduTagOverride": satControlFlpduTagOverride,
       "satStreamTable": satStreamTable,
       "satStreamEntry": satStreamEntry,
       "satStreamIndex": satStreamIndex,
       "satStreamName": satStreamName,
       "satStreamTestPort": satStreamTestPort,
       "satStreamTestDirection": satStreamTestDirection,
       "satStreamDestMacAddress": satStreamDestMacAddress,
       "satStreamFramePayloadType": satStreamFramePayloadType,
       "satStreamCustomFramePayload": satStreamCustomFramePayload,
       "satStreamFrameSizeList": satStreamFrameSizeList,
       "satStreamSacProfileId": satStreamSacProfileId,
       "satStreamSrcMepId": satStreamSrcMepId,
       "satStreamDestMepType": satStreamDestMepType,
       "satStreamDestMepId": satStreamDestMepId,
       "satStreamDestMepMacAddr": satStreamDestMepMacAddr,
       "satStreamDmmPacketSize": satStreamDmmPacketSize,
       "satStreamDmmPacketInterval": satStreamDmmPacketInterval,
       "satStreamOverallResult": satStreamOverallResult,
       "satStreamAction": satStreamAction,
       "satStreamStatus": satStreamStatus,
       "satStreamCurrentTestProcedure": satStreamCurrentTestProcedure,
       "satStreamCurrentConfigCirTestStep": satStreamCurrentConfigCirTestStep,
       "satStreamInner1VlanId": satStreamInner1VlanId,
       "satStreamInner1VlanPri": satStreamInner1VlanPri,
       "satStreamInner1VlanEnabled": satStreamInner1VlanEnabled,
       "satStreamInner1ValnEtherType": satStreamInner1ValnEtherType,
       "satStreamInner2VlanId": satStreamInner2VlanId,
       "satStreamInner2VlanPri": satStreamInner2VlanPri,
       "satStreamInner2VlanEnabled": satStreamInner2VlanEnabled,
       "satStreamInner2VlanEtherType": satStreamInner2VlanEtherType,
       "satStreamOuterVlanId": satStreamOuterVlanId,
       "satStreamOuterVlanPri": satStreamOuterVlanPri,
       "satStreamOuterVlanEnabled": satStreamOuterVlanEnabled,
       "satStreamOuterVlanEtherType": satStreamOuterVlanEtherType,
       "satStreamDeiEnabled": satStreamDeiEnabled,
       "satStreamGreenPcp": satStreamGreenPcp,
       "satStreamYellowPcp": satStreamYellowPcp,
       "satStreamColorMode": satStreamColorMode,
       "satStreamCirLo": satStreamCirLo,
       "satStreamCirHi": satStreamCirHi,
       "satStreamEirLo": satStreamEirLo,
       "satStreamEirHi": satStreamEirHi,
       "satStreamCbs": satStreamCbs,
       "satStreamEbs": satStreamEbs,
       "satStreamStorageType": satStreamStorageType,
       "satStreamRowStatus": satStreamRowStatus,
       "satStreamDmmPktPriority": satStreamDmmPktPriority,
       "satStreamMFactor": satStreamMFactor,
       "satStreamDestMepEnabled": satStreamDestMepEnabled,
       "satStreamLlActivateEnabled": satStreamLlActivateEnabled,
       "satResultStatsTable": satResultStatsTable,
       "satResultStatsEntry": satResultStatsEntry,
       "satResultStatsTestType": satResultStatsTestType,
       "satResultStatsStepNumber": satResultStatsStepNumber,
       "satResultStatsSessionId": satResultStatsSessionId,
       "satResultStatsStartTime": satResultStatsStartTime,
       "satResultStatsEndTime": satResultStatsEndTime,
       "satResultStatsStatus": satResultStatsStatus,
       "satResultStatsResult": satResultStatsResult,
       "satResultStatsMinIRGMeasured": satResultStatsMinIRGMeasured,
       "satResultStatsAvgIRGMeasured": satResultStatsAvgIRGMeasured,
       "satResultStatsMaxIRGMeasured": satResultStatsMaxIRGMeasured,
       "satResultStatsMinIRYMeasured": satResultStatsMinIRYMeasured,
       "satResultStatsAvgIRYMeasured": satResultStatsAvgIRYMeasured,
       "satResultStatsMaxIRYMeasured": satResultStatsMaxIRYMeasured,
       "satResultStatsFlrGMeasured": satResultStatsFlrGMeasured,
       "satResultStatsFlrYMeasured": satResultStatsFlrYMeasured,
       "satResultStatsFlrGCounts": satResultStatsFlrGCounts,
       "satResultStatsFlrYCounts": satResultStatsFlrYCounts,
       "satResultStatsMinFTDGMeasured": satResultStatsMinFTDGMeasured,
       "satResultStatsAvgFTDGMeasured": satResultStatsAvgFTDGMeasured,
       "satResultStatsMaxFTDGMeasured": satResultStatsMaxFTDGMeasured,
       "satResultStatsIMinFDVGMeasured": satResultStatsIMinFDVGMeasured,
       "satResultStatsIAvgFDVGMeasured": satResultStatsIAvgFDVGMeasured,
       "satResultStatsIMaxFDVGMeasured": satResultStatsIMaxFDVGMeasured,
       "satResultStatsISyncErrorsNum": satResultStatsISyncErrorsNum,
       "satResultStatsIfNegFLG": satResultStatsIfNegFLG,
       "satResultStatsIfNegFLY": satResultStatsIfNegFLY,
       "satResultStatsAvgIRT": satResultStatsAvgIRT,
       "satResultStatsFlrTMeasured": satResultStatsFlrTMeasured,
       "satResultStatsFlTCounts": satResultStatsFlTCounts,
       "satResultStatsIfNegFLT": satResultStatsIfNegFLT,
       "satSacProfileTable": satSacProfileTable,
       "satSacProfileEntry": satSacProfileEntry,
       "satSacProfileIndex": satSacProfileIndex,
       "satSacProfileAlias": satSacProfileAlias,
       "satSacProfileFLR": satSacProfileFLR,
       "satSacProfileFTD": satSacProfileFTD,
       "satSacProfileFDV": satSacProfileFDV,
       "satSacProfileStorageType": satSacProfileStorageType,
       "satSacProfileRowStatus": satSacProfileRowStatus,
       "satResponderSessionTable": satResponderSessionTable,
       "satResponderSessionEntry": satResponderSessionEntry,
       "satResponderSessionIndex": satResponderSessionIndex,
       "satResponderSessionId": satResponderSessionId,
       "satResponderSessionControlMepMacAddr": satResponderSessionControlMepMacAddr,
       "satResponderSessionMepId": satResponderSessionMepId,
       "satResponderSessionStorageType": satResponderSessionStorageType,
       "satResponderSessionRowStatus": satResponderSessionRowStatus,
       "networkElementSatParamsTable": networkElementSatParamsTable,
       "networkElementSatParamsEntry": networkElementSatParamsEntry,
       "neSatParamsEtherType": neSatParamsEtherType,
       "satCfmMepExtTable": satCfmMepExtTable,
       "satCfmMepExtEntry": satCfmMepExtEntry,
       "satCfmMepSatResponderEnabled": satCfmMepSatResponderEnabled,
       "cmServActivationNotifications": cmServActivationNotifications,
       "cmServActivationConformance": cmServActivationConformance,
       "cmServActivationCompliances": cmServActivationCompliances,
       "cmServActivationCompliance": cmServActivationCompliance,
       "cmServActivationGroups": cmServActivationGroups,
       "cmSatGroup": cmSatGroup}
)
