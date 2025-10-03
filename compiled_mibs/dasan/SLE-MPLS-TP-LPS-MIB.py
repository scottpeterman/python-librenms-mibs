# SNMP MIB module (SLE-MPLS-TP-LPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-MPLS-TP-LPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:36 2025
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

sleMplsTpLps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18)
)
if mibBuilder.loadTexts:
    sleMplsTpLps.setRevisions(
        ("2012-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
if mibBuilder.loadTexts:
    sleMpls.setStatus("current")
_SleMplsTpLpsCfg_ObjectIdentity = ObjectIdentity
sleMplsTpLpsCfg = _SleMplsTpLpsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1)
)
_SleMplsTpLpsCfgInfoTable_Object = MibTable
sleMplsTpLpsCfgInfoTable = _SleMplsTpLpsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoTable.setStatus("current")
_SleMplsTpLpsCfgInfoEntry_Object = MibTableRow
sleMplsTpLpsCfgInfoEntry = _SleMplsTpLpsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1)
)
sleMplsTpLpsCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-LPS-MIB", "sleMplsTpLpsCfgInfoGroupIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoEntry.setStatus("current")


class _SleMplsTpLpsCfgInfoGroupIndex_Type(Unsigned32):
    """Custom type sleMplsTpLpsCfgInfoGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpLpsCfgInfoGroupIndex_Type.__name__ = "Unsigned32"
_SleMplsTpLpsCfgInfoGroupIndex_Object = MibTableColumn
sleMplsTpLpsCfgInfoGroupIndex = _SleMplsTpLpsCfgInfoGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 1),
    _SleMplsTpLpsCfgInfoGroupIndex_Type()
)
sleMplsTpLpsCfgInfoGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoGroupIndex.setStatus("current")


class _SleMplsTpLpsCfgInfoGroupName_Type(OctetString):
    """Custom type sleMplsTpLpsCfgInfoGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SleMplsTpLpsCfgInfoGroupName_Type.__name__ = "OctetString"
_SleMplsTpLpsCfgInfoGroupName_Object = MibTableColumn
sleMplsTpLpsCfgInfoGroupName = _SleMplsTpLpsCfgInfoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 2),
    _SleMplsTpLpsCfgInfoGroupName_Type()
)
sleMplsTpLpsCfgInfoGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoGroupName.setStatus("current")


class _SleMplsTpLpsCfgInfoMode_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 1),
          ("oneColonOne", 2),
          ("oneColonN", 3))
    )


_SleMplsTpLpsCfgInfoMode_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoMode_Object = MibTableColumn
sleMplsTpLpsCfgInfoMode = _SleMplsTpLpsCfgInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 3),
    _SleMplsTpLpsCfgInfoMode_Type()
)
sleMplsTpLpsCfgInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoMode.setStatus("current")


class _SleMplsTpLpsCfgInfoProtectionScheme_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoProtectionScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_SleMplsTpLpsCfgInfoProtectionScheme_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoProtectionScheme_Object = MibTableColumn
sleMplsTpLpsCfgInfoProtectionScheme = _SleMplsTpLpsCfgInfoProtectionScheme_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 4),
    _SleMplsTpLpsCfgInfoProtectionScheme_Type()
)
sleMplsTpLpsCfgInfoProtectionScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoProtectionScheme.setStatus("current")


class _SleMplsTpLpsCfgInfoRevertive_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoRevertive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_SleMplsTpLpsCfgInfoRevertive_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoRevertive_Object = MibTableColumn
sleMplsTpLpsCfgInfoRevertive = _SleMplsTpLpsCfgInfoRevertive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 5),
    _SleMplsTpLpsCfgInfoRevertive_Type()
)
sleMplsTpLpsCfgInfoRevertive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoRevertive.setStatus("current")


class _SleMplsTpLpsCfgInfoWtr_Type(Unsigned32):
    """Custom type sleMplsTpLpsCfgInfoWtr based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_SleMplsTpLpsCfgInfoWtr_Type.__name__ = "Unsigned32"
_SleMplsTpLpsCfgInfoWtr_Object = MibTableColumn
sleMplsTpLpsCfgInfoWtr = _SleMplsTpLpsCfgInfoWtr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 6),
    _SleMplsTpLpsCfgInfoWtr_Type()
)
sleMplsTpLpsCfgInfoWtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoWtr.setStatus("current")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoWtr.setUnits("seconds")


class _SleMplsTpLpsCfgInfoContinualTxInterval_Type(Unsigned32):
    """Custom type sleMplsTpLpsCfgInfoContinualTxInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SleMplsTpLpsCfgInfoContinualTxInterval_Type.__name__ = "Unsigned32"
_SleMplsTpLpsCfgInfoContinualTxInterval_Object = MibTableColumn
sleMplsTpLpsCfgInfoContinualTxInterval = _SleMplsTpLpsCfgInfoContinualTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 7),
    _SleMplsTpLpsCfgInfoContinualTxInterval_Type()
)
sleMplsTpLpsCfgInfoContinualTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoContinualTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoContinualTxInterval.setUnits("seconds")


class _SleMplsTpLpsCfgInfoRapidTxInterval_Type(Unsigned32):
    """Custom type sleMplsTpLpsCfgInfoRapidTxInterval based on Unsigned32"""
    defaultValue = 3300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_SleMplsTpLpsCfgInfoRapidTxInterval_Type.__name__ = "Unsigned32"
_SleMplsTpLpsCfgInfoRapidTxInterval_Object = MibTableColumn
sleMplsTpLpsCfgInfoRapidTxInterval = _SleMplsTpLpsCfgInfoRapidTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 8),
    _SleMplsTpLpsCfgInfoRapidTxInterval_Type()
)
sleMplsTpLpsCfgInfoRapidTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoRapidTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoRapidTxInterval.setUnits("micro-seconds")


class _SleMplsTpLpsCfgInfoSwitchOver_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("forced", 1),
          ("manual", 2))
    )


_SleMplsTpLpsCfgInfoSwitchOver_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoSwitchOver_Object = MibTableColumn
sleMplsTpLpsCfgInfoSwitchOver = _SleMplsTpLpsCfgInfoSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 9),
    _SleMplsTpLpsCfgInfoSwitchOver_Type()
)
sleMplsTpLpsCfgInfoSwitchOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoSwitchOver.setStatus("current")


class _SleMplsTpLpsCfgInfoLockOut_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoLockOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleMplsTpLpsCfgInfoLockOut_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoLockOut_Object = MibTableColumn
sleMplsTpLpsCfgInfoLockOut = _SleMplsTpLpsCfgInfoLockOut_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 10),
    _SleMplsTpLpsCfgInfoLockOut_Type()
)
sleMplsTpLpsCfgInfoLockOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoLockOut.setStatus("current")
_SleMplsTpLpsCfgInfoHoldOffTimer_Type = Unsigned32
_SleMplsTpLpsCfgInfoHoldOffTimer_Object = MibTableColumn
sleMplsTpLpsCfgInfoHoldOffTimer = _SleMplsTpLpsCfgInfoHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 11),
    _SleMplsTpLpsCfgInfoHoldOffTimer_Type()
)
sleMplsTpLpsCfgInfoHoldOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoHoldOffTimer.setStatus("current")


class _SleMplsTpLpsCfgInfoActivePath_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoActivePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_SleMplsTpLpsCfgInfoActivePath_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoActivePath_Object = MibTableColumn
sleMplsTpLpsCfgInfoActivePath = _SleMplsTpLpsCfgInfoActivePath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 12),
    _SleMplsTpLpsCfgInfoActivePath_Type()
)
sleMplsTpLpsCfgInfoActivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoActivePath.setStatus("current")


class _SleMplsTpLpsCfgInfoOperationState_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoOperationState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_SleMplsTpLpsCfgInfoOperationState_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoOperationState_Object = MibTableColumn
sleMplsTpLpsCfgInfoOperationState = _SleMplsTpLpsCfgInfoOperationState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 13),
    _SleMplsTpLpsCfgInfoOperationState_Type()
)
sleMplsTpLpsCfgInfoOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoOperationState.setStatus("current")


class _SleMplsTpLpsCfgInfoEventStatus_Type(Integer32):
    """Custom type sleMplsTpLpsCfgInfoEventStatus based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("protection", 2),
          ("localForce", 3),
          ("localManual", 4),
          ("localSgfProtection", 5),
          ("localSgfWorking", 6),
          ("localWtr", 7),
          ("localLock", 8),
          ("localClrSfProtection", 9),
          ("localClrSfWorking", 10),
          ("localClrEvent", 11),
          ("remoteLock", 12),
          ("remoteForce", 13),
          ("remoteManual", 14),
          ("remoteSfProtect", 15),
          ("remoteSfWork", 16),
          ("remoteWtr", 17),
          ("remoteNoReq", 18),
          ("remoteNotRevert", 19),
          ("noRequest", 20),
          ("remoteSdWork", 21),
          ("remoteSdProtection", 22),
          ("remoteExesWork", 23),
          ("remoteExesProtect", 24),
          ("remoteRrReqWork", 25),
          ("remoteRrReqProtec", 26),
          ("remoteNoReqWork", 27),
          ("remoteNoReqProtection", 28),
          ("localSdProtection", 29),
          ("localClearSdProtection", 30),
          ("localSdWorking", 31),
          ("localClearSdWorking", 32),
          ("localExercise", 33))
    )


_SleMplsTpLpsCfgInfoEventStatus_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgInfoEventStatus_Object = MibTableColumn
sleMplsTpLpsCfgInfoEventStatus = _SleMplsTpLpsCfgInfoEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 1, 1, 14),
    _SleMplsTpLpsCfgInfoEventStatus_Type()
)
sleMplsTpLpsCfgInfoEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgInfoEventStatus.setStatus("current")
_SleMplsTpLpsCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpLpsCfgControl = _SleMplsTpLpsCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2)
)


class _SleMplsTpLpsCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpLpsCfgControlRequest based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("createSleMplsTpLpsCfgEntry", 1),
          ("deleteSleMplsTpLpsCfgEntry", 2),
          ("setSleMplsTpLpsCfgControProtectionScheme", 3),
          ("unsetSleMplsTpLpsCfgControProtectionScheme", 4),
          ("setSleMplsLpsTpCfgControlRevertive", 5),
          ("setSleMplsLpsTpCfgControlWaitToRestoreset", 6),
          ("unsetSleMplsTpLpsCfgControlWaitToRestoreset", 7),
          ("setSleMplsLpsTpCfgControlContinualTxInterval", 8),
          ("unsetSleMplsTpLpsCfgControlContinualTxInterval", 9),
          ("setSleMplsLpsTpCfgControlRapidTxInterval", 10),
          ("unsetSleMplsTpLpsCfgControlRapidTxInterval", 11),
          ("setSleMplsLpsTpCfgControlSwitchover", 12),
          ("unsetSleMplsTpLpsCfgControlSwitchover", 13),
          ("setSleMplsTpLpsCfgControlLockOut", 14),
          ("unsetSleMplsTpLpsTpCfgControlLockOut", 15),
          ("setSleMplsTpLpsCfgControlHoldOffTimer", 16),
          ("unSetSleMplsTpLpsCfgControlHoldOffTimer", 17))
    )


_SleMplsTpLpsCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgControlRequest_Object = MibScalar
sleMplsTpLpsCfgControlRequest = _SleMplsTpLpsCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 1),
    _SleMplsTpLpsCfgControlRequest_Type()
)
sleMplsTpLpsCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlRequest.setStatus("current")
_SleMplsTpLpsCfgControlStatus_Type = SleControlStatusType
_SleMplsTpLpsCfgControlStatus_Object = MibScalar
sleMplsTpLpsCfgControlStatus = _SleMplsTpLpsCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 2),
    _SleMplsTpLpsCfgControlStatus_Type()
)
sleMplsTpLpsCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlStatus.setStatus("current")
_SleMplsTpLpsCfgControlTimer_Type = Gauge32
_SleMplsTpLpsCfgControlTimer_Object = MibScalar
sleMplsTpLpsCfgControlTimer = _SleMplsTpLpsCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 3),
    _SleMplsTpLpsCfgControlTimer_Type()
)
sleMplsTpLpsCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlTimer.setStatus("current")
_SleMplsTpLpsCfgControlTimeStamp_Type = TimeTicks
_SleMplsTpLpsCfgControlTimeStamp_Object = MibScalar
sleMplsTpLpsCfgControlTimeStamp = _SleMplsTpLpsCfgControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 4),
    _SleMplsTpLpsCfgControlTimeStamp_Type()
)
sleMplsTpLpsCfgControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlTimeStamp.setStatus("current")
_SleMplsTpLpsCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpLpsCfgControlReqResult_Object = MibScalar
sleMplsTpLpsCfgControlReqResult = _SleMplsTpLpsCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 5),
    _SleMplsTpLpsCfgControlReqResult_Type()
)
sleMplsTpLpsCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlReqResult.setStatus("current")


class _SleMplsTpLpsCfgControlGroupName_Type(OctetString):
    """Custom type sleMplsTpLpsCfgControlGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleMplsTpLpsCfgControlGroupName_Type.__name__ = "OctetString"
_SleMplsTpLpsCfgControlGroupName_Object = MibScalar
sleMplsTpLpsCfgControlGroupName = _SleMplsTpLpsCfgControlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 6),
    _SleMplsTpLpsCfgControlGroupName_Type()
)
sleMplsTpLpsCfgControlGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlGroupName.setStatus("current")


class _SleMplsTpLpsCfgControlMode_Type(Integer32):
    """Custom type sleMplsTpLpsCfgControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 1),
          ("oneColonOne", 2),
          ("oneColonN", 3))
    )


_SleMplsTpLpsCfgControlMode_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgControlMode_Object = MibScalar
sleMplsTpLpsCfgControlMode = _SleMplsTpLpsCfgControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 7),
    _SleMplsTpLpsCfgControlMode_Type()
)
sleMplsTpLpsCfgControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlMode.setStatus("current")


class _SleMplsTpLpsCfgControlProtectionScheme_Type(Integer32):
    """Custom type sleMplsTpLpsCfgControlProtectionScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_SleMplsTpLpsCfgControlProtectionScheme_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgControlProtectionScheme_Object = MibScalar
sleMplsTpLpsCfgControlProtectionScheme = _SleMplsTpLpsCfgControlProtectionScheme_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 8),
    _SleMplsTpLpsCfgControlProtectionScheme_Type()
)
sleMplsTpLpsCfgControlProtectionScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlProtectionScheme.setStatus("current")


class _SleMplsTpLpsCfgControlRevertive_Type(Integer32):
    """Custom type sleMplsTpLpsCfgControlRevertive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_SleMplsTpLpsCfgControlRevertive_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgControlRevertive_Object = MibScalar
sleMplsTpLpsCfgControlRevertive = _SleMplsTpLpsCfgControlRevertive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 9),
    _SleMplsTpLpsCfgControlRevertive_Type()
)
sleMplsTpLpsCfgControlRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlRevertive.setStatus("current")


class _SleMplsTpLpsCfgControlWtr_Type(Unsigned32):
    """Custom type sleMplsTpLpsCfgControlWtr based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_SleMplsTpLpsCfgControlWtr_Type.__name__ = "Unsigned32"
_SleMplsTpLpsCfgControlWtr_Object = MibScalar
sleMplsTpLpsCfgControlWtr = _SleMplsTpLpsCfgControlWtr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 10),
    _SleMplsTpLpsCfgControlWtr_Type()
)
sleMplsTpLpsCfgControlWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlWtr.setStatus("current")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlWtr.setUnits("seconds")


class _SleMplsTpLpsCfgControlContinualTxInterval_Type(Unsigned32):
    """Custom type sleMplsTpLpsCfgControlContinualTxInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SleMplsTpLpsCfgControlContinualTxInterval_Type.__name__ = "Unsigned32"
_SleMplsTpLpsCfgControlContinualTxInterval_Object = MibScalar
sleMplsTpLpsCfgControlContinualTxInterval = _SleMplsTpLpsCfgControlContinualTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 11),
    _SleMplsTpLpsCfgControlContinualTxInterval_Type()
)
sleMplsTpLpsCfgControlContinualTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlContinualTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlContinualTxInterval.setUnits("seconds")


class _SleMplsTpLpsCfgControlRapidTxInterval_Type(Unsigned32):
    """Custom type sleMplsTpLpsCfgControlRapidTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000),
    )


_SleMplsTpLpsCfgControlRapidTxInterval_Type.__name__ = "Unsigned32"
_SleMplsTpLpsCfgControlRapidTxInterval_Object = MibScalar
sleMplsTpLpsCfgControlRapidTxInterval = _SleMplsTpLpsCfgControlRapidTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 12),
    _SleMplsTpLpsCfgControlRapidTxInterval_Type()
)
sleMplsTpLpsCfgControlRapidTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlRapidTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlRapidTxInterval.setUnits("micro-seconds")


class _SleMplsTpLpsCfgControlswitchOver_Type(Integer32):
    """Custom type sleMplsTpLpsCfgControlswitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("manual", 2))
    )


_SleMplsTpLpsCfgControlswitchOver_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgControlswitchOver_Object = MibScalar
sleMplsTpLpsCfgControlswitchOver = _SleMplsTpLpsCfgControlswitchOver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 13),
    _SleMplsTpLpsCfgControlswitchOver_Type()
)
sleMplsTpLpsCfgControlswitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlswitchOver.setStatus("current")


class _SleMplsTpLpsCfgControlLockOut_Type(Integer32):
    """Custom type sleMplsTpLpsCfgControlLockOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleMplsTpLpsCfgControlLockOut_Type.__name__ = "Integer32"
_SleMplsTpLpsCfgControlLockOut_Object = MibScalar
sleMplsTpLpsCfgControlLockOut = _SleMplsTpLpsCfgControlLockOut_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 14),
    _SleMplsTpLpsCfgControlLockOut_Type()
)
sleMplsTpLpsCfgControlLockOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlLockOut.setStatus("current")
_SleMplsTpLpsCfgControlHoldOffTimer_Type = Unsigned32
_SleMplsTpLpsCfgControlHoldOffTimer_Object = MibScalar
sleMplsTpLpsCfgControlHoldOffTimer = _SleMplsTpLpsCfgControlHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 1, 2, 15),
    _SleMplsTpLpsCfgControlHoldOffTimer_Type()
)
sleMplsTpLpsCfgControlHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsCfgControlHoldOffTimer.setStatus("current")
_SleMplsTpLpsMeCfg_ObjectIdentity = ObjectIdentity
sleMplsTpLpsMeCfg = _SleMplsTpLpsMeCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2)
)
_SleMplsTpLpsMeCfgInfoTable_Object = MibTable
sleMplsTpLpsMeCfgInfoTable = _SleMplsTpLpsMeCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgInfoTable.setStatus("current")
_SleMplsTpLpsMeCfgInfoEntry_Object = MibTableRow
sleMplsTpLpsMeCfgInfoEntry = _SleMplsTpLpsMeCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 1, 1)
)
sleMplsTpLpsMeCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-LPS-MIB", "sleMplsTpLpsMeCfgInfoMeIndex"),
    (0, "SLE-MPLS-TP-LPS-MIB", "sleMplsTpLpsMeCfgInfoMPId"),
    (0, "SLE-MPLS-TP-LPS-MIB", "sleMplsTpLspMeCfgInfoGroupIndex"),
    (0, "SLE-MPLS-TP-LPS-MIB", "sleMplsTpLpsMeCfgInfoMegIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgInfoEntry.setStatus("current")


class _SleMplsTpLpsMeCfgInfoMegIndex_Type(Unsigned32):
    """Custom type sleMplsTpLpsMeCfgInfoMegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpLpsMeCfgInfoMegIndex_Type.__name__ = "Unsigned32"
_SleMplsTpLpsMeCfgInfoMegIndex_Object = MibTableColumn
sleMplsTpLpsMeCfgInfoMegIndex = _SleMplsTpLpsMeCfgInfoMegIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 1, 1, 1),
    _SleMplsTpLpsMeCfgInfoMegIndex_Type()
)
sleMplsTpLpsMeCfgInfoMegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgInfoMegIndex.setStatus("current")


class _SleMplsTpLpsMeCfgInfoMeIndex_Type(Unsigned32):
    """Custom type sleMplsTpLpsMeCfgInfoMeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpLpsMeCfgInfoMeIndex_Type.__name__ = "Unsigned32"
_SleMplsTpLpsMeCfgInfoMeIndex_Object = MibTableColumn
sleMplsTpLpsMeCfgInfoMeIndex = _SleMplsTpLpsMeCfgInfoMeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 1, 1, 2),
    _SleMplsTpLpsMeCfgInfoMeIndex_Type()
)
sleMplsTpLpsMeCfgInfoMeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgInfoMeIndex.setStatus("current")


class _SleMplsTpLpsMeCfgInfoMPId_Type(Unsigned32):
    """Custom type sleMplsTpLpsMeCfgInfoMPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SleMplsTpLpsMeCfgInfoMPId_Type.__name__ = "Unsigned32"
_SleMplsTpLpsMeCfgInfoMPId_Object = MibTableColumn
sleMplsTpLpsMeCfgInfoMPId = _SleMplsTpLpsMeCfgInfoMPId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 1, 1, 3),
    _SleMplsTpLpsMeCfgInfoMPId_Type()
)
sleMplsTpLpsMeCfgInfoMPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgInfoMPId.setStatus("current")


class _SleMplsTpLspMeCfgInfoGroupIndex_Type(Unsigned32):
    """Custom type sleMplsTpLspMeCfgInfoGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpLspMeCfgInfoGroupIndex_Type.__name__ = "Unsigned32"
_SleMplsTpLspMeCfgInfoGroupIndex_Object = MibTableColumn
sleMplsTpLspMeCfgInfoGroupIndex = _SleMplsTpLspMeCfgInfoGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 1, 1, 4),
    _SleMplsTpLspMeCfgInfoGroupIndex_Type()
)
sleMplsTpLspMeCfgInfoGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLspMeCfgInfoGroupIndex.setStatus("current")


class _SleMplsTpLpsMeCfgInfoState_Type(Integer32):
    """Custom type sleMplsTpLpsMeCfgInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_SleMplsTpLpsMeCfgInfoState_Type.__name__ = "Integer32"
_SleMplsTpLpsMeCfgInfoState_Object = MibTableColumn
sleMplsTpLpsMeCfgInfoState = _SleMplsTpLpsMeCfgInfoState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 1, 1, 5),
    _SleMplsTpLpsMeCfgInfoState_Type()
)
sleMplsTpLpsMeCfgInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgInfoState.setStatus("current")
_SleMplsTpLpsMeCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpLpsMeCfgControl = _SleMplsTpLpsMeCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2)
)


class _SleMplsTpLpsMeCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpLpsMeCfgControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createSleMplsTpLpsMeConfigEntry", 1),
          ("deleteSleMplsTpLpsMeConfigEntry", 2))
    )


_SleMplsTpLpsMeCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpLpsMeCfgControlRequest_Object = MibScalar
sleMplsTpLpsMeCfgControlRequest = _SleMplsTpLpsMeCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 1),
    _SleMplsTpLpsMeCfgControlRequest_Type()
)
sleMplsTpLpsMeCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlRequest.setStatus("current")
_SleMplsTpLpsMeCfgControlStatus_Type = SleControlStatusType
_SleMplsTpLpsMeCfgControlStatus_Object = MibScalar
sleMplsTpLpsMeCfgControlStatus = _SleMplsTpLpsMeCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 2),
    _SleMplsTpLpsMeCfgControlStatus_Type()
)
sleMplsTpLpsMeCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlStatus.setStatus("current")
_SleMplsTpLpsMeCfgControlTimer_Type = Gauge32
_SleMplsTpLpsMeCfgControlTimer_Object = MibScalar
sleMplsTpLpsMeCfgControlTimer = _SleMplsTpLpsMeCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 3),
    _SleMplsTpLpsMeCfgControlTimer_Type()
)
sleMplsTpLpsMeCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlTimer.setStatus("current")
_SleMplsTpLpsMeCfgControlTimeStamp_Type = TimeTicks
_SleMplsTpLpsMeCfgControlTimeStamp_Object = MibScalar
sleMplsTpLpsMeCfgControlTimeStamp = _SleMplsTpLpsMeCfgControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 4),
    _SleMplsTpLpsMeCfgControlTimeStamp_Type()
)
sleMplsTpLpsMeCfgControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlTimeStamp.setStatus("current")
_SleMplsTpLpsMeCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpLpsMeCfgControlReqResult_Object = MibScalar
sleMplsTpLpsMeCfgControlReqResult = _SleMplsTpLpsMeCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 5),
    _SleMplsTpLpsMeCfgControlReqResult_Type()
)
sleMplsTpLpsMeCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlReqResult.setStatus("current")
_SleMplsTpLpsMeCfgControlMegName_Type = OctetString
_SleMplsTpLpsMeCfgControlMegName_Object = MibScalar
sleMplsTpLpsMeCfgControlMegName = _SleMplsTpLpsMeCfgControlMegName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 6),
    _SleMplsTpLpsMeCfgControlMegName_Type()
)
sleMplsTpLpsMeCfgControlMegName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlMegName.setStatus("current")
_SleMplsTpLpsMeCfgControlMeName_Type = OctetString
_SleMplsTpLpsMeCfgControlMeName_Object = MibScalar
sleMplsTpLpsMeCfgControlMeName = _SleMplsTpLpsMeCfgControlMeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 7),
    _SleMplsTpLpsMeCfgControlMeName_Type()
)
sleMplsTpLpsMeCfgControlMeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlMeName.setStatus("current")
_SleMplsTpLpsMeCfgControlMpId_Type = Unsigned32
_SleMplsTpLpsMeCfgControlMpId_Object = MibScalar
sleMplsTpLpsMeCfgControlMpId = _SleMplsTpLpsMeCfgControlMpId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 8),
    _SleMplsTpLpsMeCfgControlMpId_Type()
)
sleMplsTpLpsMeCfgControlMpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlMpId.setStatus("current")
_SleMplsTpLpsMeCfgControlGroupName_Type = OctetString
_SleMplsTpLpsMeCfgControlGroupName_Object = MibScalar
sleMplsTpLpsMeCfgControlGroupName = _SleMplsTpLpsMeCfgControlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 9),
    _SleMplsTpLpsMeCfgControlGroupName_Type()
)
sleMplsTpLpsMeCfgControlGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlGroupName.setStatus("current")


class _SleMplsTpLpsMeCfgControlState_Type(Integer32):
    """Custom type sleMplsTpLpsMeCfgControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_SleMplsTpLpsMeCfgControlState_Type.__name__ = "Integer32"
_SleMplsTpLpsMeCfgControlState_Object = MibScalar
sleMplsTpLpsMeCfgControlState = _SleMplsTpLpsMeCfgControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 18, 2, 2, 10),
    _SleMplsTpLpsMeCfgControlState_Type()
)
sleMplsTpLpsMeCfgControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpLpsMeCfgControlState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-LPS-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpLps": sleMplsTpLps,
       "sleMplsTpLpsCfg": sleMplsTpLpsCfg,
       "sleMplsTpLpsCfgInfoTable": sleMplsTpLpsCfgInfoTable,
       "sleMplsTpLpsCfgInfoEntry": sleMplsTpLpsCfgInfoEntry,
       "sleMplsTpLpsCfgInfoGroupIndex": sleMplsTpLpsCfgInfoGroupIndex,
       "sleMplsTpLpsCfgInfoGroupName": sleMplsTpLpsCfgInfoGroupName,
       "sleMplsTpLpsCfgInfoMode": sleMplsTpLpsCfgInfoMode,
       "sleMplsTpLpsCfgInfoProtectionScheme": sleMplsTpLpsCfgInfoProtectionScheme,
       "sleMplsTpLpsCfgInfoRevertive": sleMplsTpLpsCfgInfoRevertive,
       "sleMplsTpLpsCfgInfoWtr": sleMplsTpLpsCfgInfoWtr,
       "sleMplsTpLpsCfgInfoContinualTxInterval": sleMplsTpLpsCfgInfoContinualTxInterval,
       "sleMplsTpLpsCfgInfoRapidTxInterval": sleMplsTpLpsCfgInfoRapidTxInterval,
       "sleMplsTpLpsCfgInfoSwitchOver": sleMplsTpLpsCfgInfoSwitchOver,
       "sleMplsTpLpsCfgInfoLockOut": sleMplsTpLpsCfgInfoLockOut,
       "sleMplsTpLpsCfgInfoHoldOffTimer": sleMplsTpLpsCfgInfoHoldOffTimer,
       "sleMplsTpLpsCfgInfoActivePath": sleMplsTpLpsCfgInfoActivePath,
       "sleMplsTpLpsCfgInfoOperationState": sleMplsTpLpsCfgInfoOperationState,
       "sleMplsTpLpsCfgInfoEventStatus": sleMplsTpLpsCfgInfoEventStatus,
       "sleMplsTpLpsCfgControl": sleMplsTpLpsCfgControl,
       "sleMplsTpLpsCfgControlRequest": sleMplsTpLpsCfgControlRequest,
       "sleMplsTpLpsCfgControlStatus": sleMplsTpLpsCfgControlStatus,
       "sleMplsTpLpsCfgControlTimer": sleMplsTpLpsCfgControlTimer,
       "sleMplsTpLpsCfgControlTimeStamp": sleMplsTpLpsCfgControlTimeStamp,
       "sleMplsTpLpsCfgControlReqResult": sleMplsTpLpsCfgControlReqResult,
       "sleMplsTpLpsCfgControlGroupName": sleMplsTpLpsCfgControlGroupName,
       "sleMplsTpLpsCfgControlMode": sleMplsTpLpsCfgControlMode,
       "sleMplsTpLpsCfgControlProtectionScheme": sleMplsTpLpsCfgControlProtectionScheme,
       "sleMplsTpLpsCfgControlRevertive": sleMplsTpLpsCfgControlRevertive,
       "sleMplsTpLpsCfgControlWtr": sleMplsTpLpsCfgControlWtr,
       "sleMplsTpLpsCfgControlContinualTxInterval": sleMplsTpLpsCfgControlContinualTxInterval,
       "sleMplsTpLpsCfgControlRapidTxInterval": sleMplsTpLpsCfgControlRapidTxInterval,
       "sleMplsTpLpsCfgControlswitchOver": sleMplsTpLpsCfgControlswitchOver,
       "sleMplsTpLpsCfgControlLockOut": sleMplsTpLpsCfgControlLockOut,
       "sleMplsTpLpsCfgControlHoldOffTimer": sleMplsTpLpsCfgControlHoldOffTimer,
       "sleMplsTpLpsMeCfg": sleMplsTpLpsMeCfg,
       "sleMplsTpLpsMeCfgInfoTable": sleMplsTpLpsMeCfgInfoTable,
       "sleMplsTpLpsMeCfgInfoEntry": sleMplsTpLpsMeCfgInfoEntry,
       "sleMplsTpLpsMeCfgInfoMegIndex": sleMplsTpLpsMeCfgInfoMegIndex,
       "sleMplsTpLpsMeCfgInfoMeIndex": sleMplsTpLpsMeCfgInfoMeIndex,
       "sleMplsTpLpsMeCfgInfoMPId": sleMplsTpLpsMeCfgInfoMPId,
       "sleMplsTpLspMeCfgInfoGroupIndex": sleMplsTpLspMeCfgInfoGroupIndex,
       "sleMplsTpLpsMeCfgInfoState": sleMplsTpLpsMeCfgInfoState,
       "sleMplsTpLpsMeCfgControl": sleMplsTpLpsMeCfgControl,
       "sleMplsTpLpsMeCfgControlRequest": sleMplsTpLpsMeCfgControlRequest,
       "sleMplsTpLpsMeCfgControlStatus": sleMplsTpLpsMeCfgControlStatus,
       "sleMplsTpLpsMeCfgControlTimer": sleMplsTpLpsMeCfgControlTimer,
       "sleMplsTpLpsMeCfgControlTimeStamp": sleMplsTpLpsMeCfgControlTimeStamp,
       "sleMplsTpLpsMeCfgControlReqResult": sleMplsTpLpsMeCfgControlReqResult,
       "sleMplsTpLpsMeCfgControlMegName": sleMplsTpLpsMeCfgControlMegName,
       "sleMplsTpLpsMeCfgControlMeName": sleMplsTpLpsMeCfgControlMeName,
       "sleMplsTpLpsMeCfgControlMpId": sleMplsTpLpsMeCfgControlMpId,
       "sleMplsTpLpsMeCfgControlGroupName": sleMplsTpLpsMeCfgControlGroupName,
       "sleMplsTpLpsMeCfgControlState": sleMplsTpLpsMeCfgControlState}
)
