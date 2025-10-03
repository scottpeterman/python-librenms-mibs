# SNMP MIB module (TN-ELPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ELPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:20 2025
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

(Dot1agCfmMepId,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProtectionMIB,) = mibBuilder.importSymbols(
    "TN-PROTECTION-MIB",
    "tnProtectionMIB")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class TnElpsProtSwitchState(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("noRequestW", 2),
          ("noRequestP", 3),
          ("lockout", 4),
          ("forcedSwitch", 5),
          ("signalFailW", 6),
          ("signalFailP", 7),
          ("manualSwitchW", 8),
          ("manualSwitchP", 9),
          ("waitToRestore", 10),
          ("exerciseW", 11),
          ("exerciseP", 12),
          ("reverseRequestW", 13),
          ("reverseRequestP", 14),
          ("doNotRevert", 15))
    )



class TnElpsDefectState(TextualConvention, Integer32):
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
        *(("signalOk", 1),
          ("signalFail", 2),
          ("signalDegrade", 3))
    )



class TnElpsRequestType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 1),
          ("doNotRevert", 2),
          ("reverseRequest", 3),
          ("exercise", 4),
          ("wait2Restore", 5),
          ("manualSwitch", 6),
          ("signalDegrade", 7),
          ("signalFailForWorking", 8),
          ("forcedWwitch", 9),
          ("signalFailForProtection", 10),
          ("lockoutOfProtection", 11))
    )



# MIB Managed Objects in the order of their OIDs

_TnElpsMib_ObjectIdentity = ObjectIdentity
tnElpsMib = _TnElpsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2)
)
_TnElpsMibNotifications_ObjectIdentity = ObjectIdentity
tnElpsMibNotifications = _TnElpsMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 0)
)
_TnElpsMibObjects_ObjectIdentity = ObjectIdentity
tnElpsMibObjects = _TnElpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1)
)
_TnElpsCfgMgmt_ObjectIdentity = ObjectIdentity
tnElpsCfgMgmt = _TnElpsCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1)
)
_TnElpsCfgTable_Object = MibTable
tnElpsCfgTable = _TnElpsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnElpsCfgTable.setStatus("current")
_TnElpsCfgEntry_Object = MibTableRow
tnElpsCfgEntry = _TnElpsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1)
)
tnElpsCfgEntry.setIndexNames(
    (0, "TN-ELPS-MIB", "tnElpsInstance"),
)
if mibBuilder.loadTexts:
    tnElpsCfgEntry.setStatus("current")
_TnElpsInstance_Type = Unsigned32
_TnElpsInstance_Object = MibTableColumn
tnElpsInstance = _TnElpsInstance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 1),
    _TnElpsInstance_Type()
)
tnElpsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnElpsInstance.setStatus("current")


class _TnElpsDomain_Type(Integer32):
    """Custom type tnElpsDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port", 1)
    )


_TnElpsDomain_Type.__name__ = "Integer32"
_TnElpsDomain_Object = MibTableColumn
tnElpsDomain = _TnElpsDomain_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 2),
    _TnElpsDomain_Type()
)
tnElpsDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsDomain.setStatus("current")


class _TnElpsArchitecture_Type(Integer32):
    """Custom type tnElpsArchitecture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 1),
          ("oneForOne", 2))
    )


_TnElpsArchitecture_Type.__name__ = "Integer32"
_TnElpsArchitecture_Object = MibTableColumn
tnElpsArchitecture = _TnElpsArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 3),
    _TnElpsArchitecture_Type()
)
tnElpsArchitecture.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsArchitecture.setStatus("current")
_TnElpsWFlowPortId_Type = InterfaceIndex
_TnElpsWFlowPortId_Object = MibTableColumn
tnElpsWFlowPortId = _TnElpsWFlowPortId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 4),
    _TnElpsWFlowPortId_Type()
)
tnElpsWFlowPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsWFlowPortId.setStatus("current")
_TnElpsPFlowPortId_Type = InterfaceIndex
_TnElpsPFlowPortId_Object = MibTableColumn
tnElpsPFlowPortId = _TnElpsPFlowPortId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 5),
    _TnElpsPFlowPortId_Type()
)
tnElpsPFlowPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsPFlowPortId.setStatus("current")
_TnElpsWSfMepId_Type = Dot1agCfmMepId
_TnElpsWSfMepId_Object = MibTableColumn
tnElpsWSfMepId = _TnElpsWSfMepId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 6),
    _TnElpsWSfMepId_Type()
)
tnElpsWSfMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsWSfMepId.setStatus("current")
_TnElpsPSfMepId_Type = Dot1agCfmMepId
_TnElpsPSfMepId_Object = MibTableColumn
tnElpsPSfMepId = _TnElpsPSfMepId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 7),
    _TnElpsPSfMepId_Type()
)
tnElpsPSfMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsPSfMepId.setStatus("current")
_TnElpsApsMepId_Type = Dot1agCfmMepId
_TnElpsApsMepId_Object = MibTableColumn
tnElpsApsMepId = _TnElpsApsMepId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 8),
    _TnElpsApsMepId_Type()
)
tnElpsApsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsApsMepId.setStatus("current")
_TnElpsConfigured_Type = TruthValue
_TnElpsConfigured_Object = MibTableColumn
tnElpsConfigured = _TnElpsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 9),
    _TnElpsConfigured_Type()
)
tnElpsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsConfigured.setStatus("current")


class _TnElpsDirection_Type(Integer32):
    """Custom type tnElpsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_TnElpsDirection_Type.__name__ = "Integer32"
_TnElpsDirection_Object = MibTableColumn
tnElpsDirection = _TnElpsDirection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 10),
    _TnElpsDirection_Type()
)
tnElpsDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsDirection.setStatus("current")
_TnElpsApsEnable_Type = TruthValue
_TnElpsApsEnable_Object = MibTableColumn
tnElpsApsEnable = _TnElpsApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 11),
    _TnElpsApsEnable_Type()
)
tnElpsApsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsApsEnable.setStatus("current")
_TnElpsRevertiveEnable_Type = TruthValue
_TnElpsRevertiveEnable_Object = MibTableColumn
tnElpsRevertiveEnable = _TnElpsRevertiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 12),
    _TnElpsRevertiveEnable_Type()
)
tnElpsRevertiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsRevertiveEnable.setStatus("current")


class _TnElpsWTRTime_Type(Integer32):
    """Custom type tnElpsWTRTime based on Integer32"""
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
        *(("disabled", 0),
          ("t10sec", 1),
          ("t30sec", 2),
          ("t5min", 3),
          ("t6min", 4),
          ("t7min", 5),
          ("t8min", 6),
          ("t9min", 7),
          ("t10min", 8),
          ("t11min", 9),
          ("t12min", 10))
    )


_TnElpsWTRTime_Type.__name__ = "Integer32"
_TnElpsWTRTime_Object = MibTableColumn
tnElpsWTRTime = _TnElpsWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 13),
    _TnElpsWTRTime_Type()
)
tnElpsWTRTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsWTRTime.setStatus("current")


class _TnElpsHoldOffTime_Type(Integer32):
    """Custom type tnElpsHoldOffTime based on Integer32"""
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
        *(("disabled", 0),
          ("t100ms", 1),
          ("t200ms", 2),
          ("t300ms", 3),
          ("t400ms", 4),
          ("t500ms", 5),
          ("t600ms", 6),
          ("t700ms", 7),
          ("t800ms", 8),
          ("t900ms", 9),
          ("t1s", 10),
          ("t2s", 11),
          ("t3s", 12),
          ("t4s", 13),
          ("t5s", 14),
          ("t6s", 15),
          ("t7s", 16),
          ("t8s", 17),
          ("t9s", 18),
          ("t10s", 19))
    )


_TnElpsHoldOffTime_Type.__name__ = "Integer32"
_TnElpsHoldOffTime_Object = MibTableColumn
tnElpsHoldOffTime = _TnElpsHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 14),
    _TnElpsHoldOffTime_Type()
)
tnElpsHoldOffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsHoldOffTime.setStatus("current")


class _TnElpsCmd_Type(Integer32):
    """Custom type tnElpsCmd based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1),
          ("lockOut", 2),
          ("forcedSwitch", 3),
          ("manualSwitchP", 4),
          ("manualSwitchW", 5),
          ("exercise", 6),
          ("freeze", 7),
          ("lockOutLocal", 8))
    )


_TnElpsCmd_Type.__name__ = "Integer32"
_TnElpsCmd_Object = MibTableColumn
tnElpsCmd = _TnElpsCmd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 15),
    _TnElpsCmd_Type()
)
tnElpsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsCmd.setStatus("current")
_TnElpsStatus_Type = RowStatus
_TnElpsStatus_Object = MibTableColumn
tnElpsStatus = _TnElpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 1, 1, 1, 16),
    _TnElpsStatus_Type()
)
tnElpsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnElpsStatus.setStatus("current")
_TnElpsStateMgmt_ObjectIdentity = ObjectIdentity
tnElpsStateMgmt = _TnElpsStateMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2)
)
_TnElpsStateTable_Object = MibTable
tnElpsStateTable = _TnElpsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnElpsStateTable.setStatus("current")
_TnElpsStateEntry_Object = MibTableRow
tnElpsStateEntry = _TnElpsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1)
)
tnElpsStateEntry.setIndexNames(
    (0, "TN-ELPS-MIB", "tnElpsInstance"),
)
if mibBuilder.loadTexts:
    tnElpsStateEntry.setStatus("current")
_TnElpsProtectionState_Type = TnElpsProtSwitchState
_TnElpsProtectionState_Object = MibTableColumn
tnElpsProtectionState = _TnElpsProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 1),
    _TnElpsProtectionState_Type()
)
tnElpsProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsProtectionState.setStatus("current")
_TnElpsWFlowState_Type = TnElpsDefectState
_TnElpsWFlowState_Object = MibTableColumn
tnElpsWFlowState = _TnElpsWFlowState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 2),
    _TnElpsWFlowState_Type()
)
tnElpsWFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsWFlowState.setStatus("current")
_TnElpsPFlowState_Type = TnElpsDefectState
_TnElpsPFlowState_Object = MibTableColumn
tnElpsPFlowState = _TnElpsPFlowState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 3),
    _TnElpsPFlowState_Type()
)
tnElpsPFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsPFlowState.setStatus("current")
_TnElpsTransmitRequestType_Type = TnElpsRequestType
_TnElpsTransmitRequestType_Object = MibTableColumn
tnElpsTransmitRequestType = _TnElpsTransmitRequestType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 4),
    _TnElpsTransmitRequestType_Type()
)
tnElpsTransmitRequestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsTransmitRequestType.setStatus("current")
_TnElpsTransmitRequestedSignal_Type = Unsigned32
_TnElpsTransmitRequestedSignal_Object = MibTableColumn
tnElpsTransmitRequestedSignal = _TnElpsTransmitRequestedSignal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 5),
    _TnElpsTransmitRequestedSignal_Type()
)
tnElpsTransmitRequestedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsTransmitRequestedSignal.setStatus("current")
_TnElpsTransmitBridgedSignal_Type = Unsigned32
_TnElpsTransmitBridgedSignal_Object = MibTableColumn
tnElpsTransmitBridgedSignal = _TnElpsTransmitBridgedSignal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 6),
    _TnElpsTransmitBridgedSignal_Type()
)
tnElpsTransmitBridgedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsTransmitBridgedSignal.setStatus("current")
_TnElpsReceiveRequestType_Type = TnElpsRequestType
_TnElpsReceiveRequestType_Object = MibTableColumn
tnElpsReceiveRequestType = _TnElpsReceiveRequestType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 7),
    _TnElpsReceiveRequestType_Type()
)
tnElpsReceiveRequestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsReceiveRequestType.setStatus("current")
_TnElpsReceiveRequestedSignal_Type = Unsigned32
_TnElpsReceiveRequestedSignal_Object = MibTableColumn
tnElpsReceiveRequestedSignal = _TnElpsReceiveRequestedSignal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 8),
    _TnElpsReceiveRequestedSignal_Type()
)
tnElpsReceiveRequestedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsReceiveRequestedSignal.setStatus("current")
_TnElpsReceiveBridgedSignal_Type = Unsigned32
_TnElpsReceiveBridgedSignal_Object = MibTableColumn
tnElpsReceiveBridgedSignal = _TnElpsReceiveBridgedSignal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 9),
    _TnElpsReceiveBridgedSignal_Type()
)
tnElpsReceiveBridgedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsReceiveBridgedSignal.setStatus("current")
_TnElpsArchitectureMismatch_Type = TruthValue
_TnElpsArchitectureMismatch_Object = MibTableColumn
tnElpsArchitectureMismatch = _TnElpsArchitectureMismatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 10),
    _TnElpsArchitectureMismatch_Type()
)
tnElpsArchitectureMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsArchitectureMismatch.setStatus("current")
_TnElpsAPSOnWorking_Type = TruthValue
_TnElpsAPSOnWorking_Object = MibTableColumn
tnElpsAPSOnWorking = _TnElpsAPSOnWorking_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 11),
    _TnElpsAPSOnWorking_Type()
)
tnElpsAPSOnWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsAPSOnWorking.setStatus("current")
_TnElpsSwitchingIncomplete_Type = TruthValue
_TnElpsSwitchingIncomplete_Object = MibTableColumn
tnElpsSwitchingIncomplete = _TnElpsSwitchingIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 12),
    _TnElpsSwitchingIncomplete_Type()
)
tnElpsSwitchingIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsSwitchingIncomplete.setStatus("current")
_TnElpsNoApsReceived_Type = TruthValue
_TnElpsNoApsReceived_Object = MibTableColumn
tnElpsNoApsReceived = _TnElpsNoApsReceived_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 2, 1, 1, 13),
    _TnElpsNoApsReceived_Type()
)
tnElpsNoApsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnElpsNoApsReceived.setStatus("current")
_TnElpsLinkOverMgmt_ObjectIdentity = ObjectIdentity
tnElpsLinkOverMgmt = _TnElpsLinkOverMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 3)
)
_TnElpsLinkOverTable_Object = MibTable
tnElpsLinkOverTable = _TnElpsLinkOverTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnElpsLinkOverTable.setStatus("current")
_TnElpsLinkOverEntry_Object = MibTableRow
tnElpsLinkOverEntry = _TnElpsLinkOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 3, 1, 1)
)
tnElpsLinkOverEntry.setIndexNames(
    (0, "TN-ELPS-MIB", "tnElpsInstance"),
)
if mibBuilder.loadTexts:
    tnElpsLinkOverEntry.setStatus("current")
_TnElpsLinkOverEnabled_Type = TruthValue
_TnElpsLinkOverEnabled_Object = MibTableColumn
tnElpsLinkOverEnabled = _TnElpsLinkOverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 3, 1, 1, 1),
    _TnElpsLinkOverEnabled_Type()
)
tnElpsLinkOverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnElpsLinkOverEnabled.setStatus("current")
_TnElpsLinkOverDeltaValue_Type = Unsigned32
_TnElpsLinkOverDeltaValue_Object = MibTableColumn
tnElpsLinkOverDeltaValue = _TnElpsLinkOverDeltaValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 1, 3, 1, 1, 2),
    _TnElpsLinkOverDeltaValue_Type()
)
tnElpsLinkOverDeltaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnElpsLinkOverDeltaValue.setStatus("current")
_TnElpsMibConformance_ObjectIdentity = ObjectIdentity
tnElpsMibConformance = _TnElpsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 2)
)

# Managed Objects groups


# Notification objects

tnElpsAlarmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 0, 1)
)
tnElpsAlarmUp.setObjects(
      *(("TN-ELPS-MIB", "tnElpsProtectionState"),
        ("TN-ELPS-MIB", "tnElpsWFlowState"),
        ("TN-ELPS-MIB", "tnElpsPFlowState"),
        ("TN-ELPS-MIB", "tnElpsArchitectureMismatch"),
        ("TN-ELPS-MIB", "tnElpsAPSOnWorking"),
        ("TN-ELPS-MIB", "tnElpsSwitchingIncomplete"))
)
if mibBuilder.loadTexts:
    tnElpsAlarmUp.setStatus(
        "current"
    )

tnElpsAlarmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 2, 0, 2)
)
tnElpsAlarmDown.setObjects(
      *(("TN-ELPS-MIB", "tnElpsProtectionState"),
        ("TN-ELPS-MIB", "tnElpsWFlowState"),
        ("TN-ELPS-MIB", "tnElpsPFlowState"),
        ("TN-ELPS-MIB", "tnElpsArchitectureMismatch"),
        ("TN-ELPS-MIB", "tnElpsAPSOnWorking"),
        ("TN-ELPS-MIB", "tnElpsSwitchingIncomplete"))
)
if mibBuilder.loadTexts:
    tnElpsAlarmDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ELPS-MIB",
    **{"TnElpsProtSwitchState": TnElpsProtSwitchState,
       "TnElpsDefectState": TnElpsDefectState,
       "TnElpsRequestType": TnElpsRequestType,
       "tnElpsMib": tnElpsMib,
       "tnElpsMibNotifications": tnElpsMibNotifications,
       "tnElpsAlarmUp": tnElpsAlarmUp,
       "tnElpsAlarmDown": tnElpsAlarmDown,
       "tnElpsMibObjects": tnElpsMibObjects,
       "tnElpsCfgMgmt": tnElpsCfgMgmt,
       "tnElpsCfgTable": tnElpsCfgTable,
       "tnElpsCfgEntry": tnElpsCfgEntry,
       "tnElpsInstance": tnElpsInstance,
       "tnElpsDomain": tnElpsDomain,
       "tnElpsArchitecture": tnElpsArchitecture,
       "tnElpsWFlowPortId": tnElpsWFlowPortId,
       "tnElpsPFlowPortId": tnElpsPFlowPortId,
       "tnElpsWSfMepId": tnElpsWSfMepId,
       "tnElpsPSfMepId": tnElpsPSfMepId,
       "tnElpsApsMepId": tnElpsApsMepId,
       "tnElpsConfigured": tnElpsConfigured,
       "tnElpsDirection": tnElpsDirection,
       "tnElpsApsEnable": tnElpsApsEnable,
       "tnElpsRevertiveEnable": tnElpsRevertiveEnable,
       "tnElpsWTRTime": tnElpsWTRTime,
       "tnElpsHoldOffTime": tnElpsHoldOffTime,
       "tnElpsCmd": tnElpsCmd,
       "tnElpsStatus": tnElpsStatus,
       "tnElpsStateMgmt": tnElpsStateMgmt,
       "tnElpsStateTable": tnElpsStateTable,
       "tnElpsStateEntry": tnElpsStateEntry,
       "tnElpsProtectionState": tnElpsProtectionState,
       "tnElpsWFlowState": tnElpsWFlowState,
       "tnElpsPFlowState": tnElpsPFlowState,
       "tnElpsTransmitRequestType": tnElpsTransmitRequestType,
       "tnElpsTransmitRequestedSignal": tnElpsTransmitRequestedSignal,
       "tnElpsTransmitBridgedSignal": tnElpsTransmitBridgedSignal,
       "tnElpsReceiveRequestType": tnElpsReceiveRequestType,
       "tnElpsReceiveRequestedSignal": tnElpsReceiveRequestedSignal,
       "tnElpsReceiveBridgedSignal": tnElpsReceiveBridgedSignal,
       "tnElpsArchitectureMismatch": tnElpsArchitectureMismatch,
       "tnElpsAPSOnWorking": tnElpsAPSOnWorking,
       "tnElpsSwitchingIncomplete": tnElpsSwitchingIncomplete,
       "tnElpsNoApsReceived": tnElpsNoApsReceived,
       "tnElpsLinkOverMgmt": tnElpsLinkOverMgmt,
       "tnElpsLinkOverTable": tnElpsLinkOverTable,
       "tnElpsLinkOverEntry": tnElpsLinkOverEntry,
       "tnElpsLinkOverEnabled": tnElpsLinkOverEnabled,
       "tnElpsLinkOverDeltaValue": tnElpsLinkOverDeltaValue,
       "tnElpsMibConformance": tnElpsMibConformance}
)
