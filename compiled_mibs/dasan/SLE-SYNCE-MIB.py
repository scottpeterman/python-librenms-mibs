# SNMP MIB module (SLE-SYNCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-SYNCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:05 2025
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

sleSynce = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SynceClockQualityLevel(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prc", 1),
          ("ssua", 2),
          ("ssub", 3),
          ("sec", 4),
          ("dnu", 5),
          ("stu", 7),
          ("st2", 8),
          ("tnc", 9),
          ("st3e", 10),
          ("st3", 11),
          ("smc", 12),
          ("prov", 13),
          ("dus", 14))
    )



# MIB Managed Objects in the order of their OIDs

_SleSynceBaseMode_ObjectIdentity = ObjectIdentity
sleSynceBaseMode = _SleSynceBaseMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1)
)
_SleSynceBaseModeInfo_ObjectIdentity = ObjectIdentity
sleSynceBaseModeInfo = _SleSynceBaseModeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 1)
)


class _SleSynceSyncOption_Type(Integer32):
    """Custom type sleSynceSyncOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2gen1", 2),
          ("option2gen2", 3))
    )


_SleSynceSyncOption_Type.__name__ = "Integer32"
_SleSynceSyncOption_Object = MibScalar
sleSynceSyncOption = _SleSynceSyncOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 1, 1),
    _SleSynceSyncOption_Type()
)
sleSynceSyncOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceSyncOption.setStatus("current")


class _SleSynceSelectionMode_Type(Integer32):
    """Custom type sleSynceSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qlEnable", 1),
          ("qlDisable", 2))
    )


_SleSynceSelectionMode_Type.__name__ = "Integer32"
_SleSynceSelectionMode_Object = MibScalar
sleSynceSelectionMode = _SleSynceSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 1, 2),
    _SleSynceSelectionMode_Type()
)
sleSynceSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceSelectionMode.setStatus("current")
_SleSynceBaseModeControl_ObjectIdentity = ObjectIdentity
sleSynceBaseModeControl = _SleSynceBaseModeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2)
)


class _SleSynceModeControlRequest_Type(Integer32):
    """Custom type sleSynceModeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("setSelectionMode", 2)
    )


_SleSynceModeControlRequest_Type.__name__ = "Integer32"
_SleSynceModeControlRequest_Object = MibScalar
sleSynceModeControlRequest = _SleSynceModeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2, 1),
    _SleSynceModeControlRequest_Type()
)
sleSynceModeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceModeControlRequest.setStatus("current")
_SleSynceModeControlStatus_Type = SleControlStatusType
_SleSynceModeControlStatus_Object = MibScalar
sleSynceModeControlStatus = _SleSynceModeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2, 2),
    _SleSynceModeControlStatus_Type()
)
sleSynceModeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceModeControlStatus.setStatus("current")
_SleSynceModeControlTimer_Type = Gauge32
_SleSynceModeControlTimer_Object = MibScalar
sleSynceModeControlTimer = _SleSynceModeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2, 3),
    _SleSynceModeControlTimer_Type()
)
sleSynceModeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceModeControlTimer.setStatus("current")
_SleSynceModeControlTimeStamp_Type = TimeTicks
_SleSynceModeControlTimeStamp_Object = MibScalar
sleSynceModeControlTimeStamp = _SleSynceModeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2, 4),
    _SleSynceModeControlTimeStamp_Type()
)
sleSynceModeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceModeControlTimeStamp.setStatus("current")
_SleSynceModeControlReqResult_Type = SleControlRequestResultType
_SleSynceModeControlReqResult_Object = MibScalar
sleSynceModeControlReqResult = _SleSynceModeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2, 5),
    _SleSynceModeControlReqResult_Type()
)
sleSynceModeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceModeControlReqResult.setStatus("current")


class _SleSynceModeControlSyncOption_Type(Integer32):
    """Custom type sleSynceModeControlSyncOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2gen1", 2),
          ("option2gen2", 3))
    )


_SleSynceModeControlSyncOption_Type.__name__ = "Integer32"
_SleSynceModeControlSyncOption_Object = MibScalar
sleSynceModeControlSyncOption = _SleSynceModeControlSyncOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2, 6),
    _SleSynceModeControlSyncOption_Type()
)
sleSynceModeControlSyncOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceModeControlSyncOption.setStatus("current")


class _SleSynceModeControlSelectionMode_Type(Integer32):
    """Custom type sleSynceModeControlSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qlEnable", 1),
          ("qlDisable", 2))
    )


_SleSynceModeControlSelectionMode_Type.__name__ = "Integer32"
_SleSynceModeControlSelectionMode_Object = MibScalar
sleSynceModeControlSelectionMode = _SleSynceModeControlSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 2, 7),
    _SleSynceModeControlSelectionMode_Type()
)
sleSynceModeControlSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceModeControlSelectionMode.setStatus("current")
_SleSynceBaseModeNotification_ObjectIdentity = ObjectIdentity
sleSynceBaseModeNotification = _SleSynceBaseModeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 3)
)
_SleSynceIfEnable_ObjectIdentity = ObjectIdentity
sleSynceIfEnable = _SleSynceIfEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2)
)
_SleSynceIfEnableTable_Object = MibTable
sleSynceIfEnableTable = _SleSynceIfEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 1)
)
if mibBuilder.loadTexts:
    sleSynceIfEnableTable.setStatus("current")
_SleSynceIfEnableEntry_Object = MibTableRow
sleSynceIfEnableEntry = _SleSynceIfEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 1, 1)
)
sleSynceIfEnableEntry.setIndexNames(
    (0, "SLE-SYNCE-MIB", "sleSynceIfEnableIfIndex"),
)
if mibBuilder.loadTexts:
    sleSynceIfEnableEntry.setStatus("current")


class _SleSynceIfEnableIfIndex_Type(Integer32):
    """Custom type sleSynceIfEnableIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSynceIfEnableIfIndex_Type.__name__ = "Integer32"
_SleSynceIfEnableIfIndex_Object = MibTableColumn
sleSynceIfEnableIfIndex = _SleSynceIfEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 1, 1, 1),
    _SleSynceIfEnableIfIndex_Type()
)
sleSynceIfEnableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfEnableIfIndex.setStatus("current")


class _SleSynceIfEnableName_Type(OctetString):
    """Custom type sleSynceIfEnableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleSynceIfEnableName_Type.__name__ = "OctetString"
_SleSynceIfEnableName_Object = MibTableColumn
sleSynceIfEnableName = _SleSynceIfEnableName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 1, 1, 2),
    _SleSynceIfEnableName_Type()
)
sleSynceIfEnableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfEnableName.setStatus("current")


class _SleSynceIfEnableState_Type(Integer32):
    """Custom type sleSynceIfEnableState based on Integer32"""
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


_SleSynceIfEnableState_Type.__name__ = "Integer32"
_SleSynceIfEnableState_Object = MibTableColumn
sleSynceIfEnableState = _SleSynceIfEnableState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 1, 1, 3),
    _SleSynceIfEnableState_Type()
)
sleSynceIfEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfEnableState.setStatus("current")
_SleSynceIfEnableControl_ObjectIdentity = ObjectIdentity
sleSynceIfEnableControl = _SleSynceIfEnableControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2)
)


class _SleSynceIfEnableControlRequest_Type(Integer32):
    """Custom type sleSynceIfEnableControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setSynceEnable", 1)
    )


_SleSynceIfEnableControlRequest_Type.__name__ = "Integer32"
_SleSynceIfEnableControlRequest_Object = MibScalar
sleSynceIfEnableControlRequest = _SleSynceIfEnableControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2, 1),
    _SleSynceIfEnableControlRequest_Type()
)
sleSynceIfEnableControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfEnableControlRequest.setStatus("current")
_SleSynceIfEnableControlStatus_Type = SleControlStatusType
_SleSynceIfEnableControlStatus_Object = MibScalar
sleSynceIfEnableControlStatus = _SleSynceIfEnableControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2, 2),
    _SleSynceIfEnableControlStatus_Type()
)
sleSynceIfEnableControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfEnableControlStatus.setStatus("current")
_SleSynceIfEnableControlTimer_Type = Gauge32
_SleSynceIfEnableControlTimer_Object = MibScalar
sleSynceIfEnableControlTimer = _SleSynceIfEnableControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2, 3),
    _SleSynceIfEnableControlTimer_Type()
)
sleSynceIfEnableControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfEnableControlTimer.setStatus("current")
_SleSynceIfEnableControlTimeStamp_Type = TimeTicks
_SleSynceIfEnableControlTimeStamp_Object = MibScalar
sleSynceIfEnableControlTimeStamp = _SleSynceIfEnableControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2, 4),
    _SleSynceIfEnableControlTimeStamp_Type()
)
sleSynceIfEnableControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfEnableControlTimeStamp.setStatus("current")
_SleSynceIfEnableControlReqResult_Type = SleControlRequestResultType
_SleSynceIfEnableControlReqResult_Object = MibScalar
sleSynceIfEnableControlReqResult = _SleSynceIfEnableControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2, 5),
    _SleSynceIfEnableControlReqResult_Type()
)
sleSynceIfEnableControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfEnableControlReqResult.setStatus("current")


class _SleSynceIfEnableControlIfIndex_Type(Integer32):
    """Custom type sleSynceIfEnableControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSynceIfEnableControlIfIndex_Type.__name__ = "Integer32"
_SleSynceIfEnableControlIfIndex_Object = MibScalar
sleSynceIfEnableControlIfIndex = _SleSynceIfEnableControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2, 6),
    _SleSynceIfEnableControlIfIndex_Type()
)
sleSynceIfEnableControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfEnableControlIfIndex.setStatus("current")


class _SleSynceIfEnableControlState_Type(Integer32):
    """Custom type sleSynceIfEnableControlState based on Integer32"""
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


_SleSynceIfEnableControlState_Type.__name__ = "Integer32"
_SleSynceIfEnableControlState_Object = MibScalar
sleSynceIfEnableControlState = _SleSynceIfEnableControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 2, 7),
    _SleSynceIfEnableControlState_Type()
)
sleSynceIfEnableControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfEnableControlState.setStatus("current")
_SleSynceIfEnableNotification_ObjectIdentity = ObjectIdentity
sleSynceIfEnableNotification = _SleSynceIfEnableNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 3)
)
_SleSynceIf_ObjectIdentity = ObjectIdentity
sleSynceIf = _SleSynceIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3)
)
_SleSynceIfTable_Object = MibTable
sleSynceIfTable = _SleSynceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1)
)
if mibBuilder.loadTexts:
    sleSynceIfTable.setStatus("current")
_SleSynceIfEntry_Object = MibTableRow
sleSynceIfEntry = _SleSynceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1)
)
sleSynceIfEntry.setIndexNames(
    (0, "SLE-SYNCE-MIB", "sleSynceIfIfIndex"),
)
if mibBuilder.loadTexts:
    sleSynceIfEntry.setStatus("current")


class _SleSynceIfIfIndex_Type(Integer32):
    """Custom type sleSynceIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSynceIfIfIndex_Type.__name__ = "Integer32"
_SleSynceIfIfIndex_Object = MibTableColumn
sleSynceIfIfIndex = _SleSynceIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 1),
    _SleSynceIfIfIndex_Type()
)
sleSynceIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfIfIndex.setStatus("current")


class _SleSynceIfName_Type(OctetString):
    """Custom type sleSynceIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleSynceIfName_Type.__name__ = "OctetString"
_SleSynceIfName_Object = MibTableColumn
sleSynceIfName = _SleSynceIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 2),
    _SleSynceIfName_Type()
)
sleSynceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfName.setStatus("current")


class _SleSynceIfInputSource_Type(Integer32):
    """Custom type sleSynceIfInputSource based on Integer32"""
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


_SleSynceIfInputSource_Type.__name__ = "Integer32"
_SleSynceIfInputSource_Object = MibTableColumn
sleSynceIfInputSource = _SleSynceIfInputSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 3),
    _SleSynceIfInputSource_Type()
)
sleSynceIfInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfInputSource.setStatus("current")


class _SleSynceIfOoutputSource_Type(Integer32):
    """Custom type sleSynceIfOoutputSource based on Integer32"""
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


_SleSynceIfOoutputSource_Type.__name__ = "Integer32"
_SleSynceIfOoutputSource_Object = MibTableColumn
sleSynceIfOoutputSource = _SleSynceIfOoutputSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 4),
    _SleSynceIfOoutputSource_Type()
)
sleSynceIfOoutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfOoutputSource.setStatus("current")


class _SleSynceIfPriority_Type(Integer32):
    """Custom type sleSynceIfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleSynceIfPriority_Type.__name__ = "Integer32"
_SleSynceIfPriority_Object = MibTableColumn
sleSynceIfPriority = _SleSynceIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 5),
    _SleSynceIfPriority_Type()
)
sleSynceIfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfPriority.setStatus("current")
_SleSynceIfRecvQl_Type = SynceClockQualityLevel
_SleSynceIfRecvQl_Object = MibTableColumn
sleSynceIfRecvQl = _SleSynceIfRecvQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 6),
    _SleSynceIfRecvQl_Type()
)
sleSynceIfRecvQl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfRecvQl.setStatus("current")
_SleSynceIfSendQl_Type = SynceClockQualityLevel
_SleSynceIfSendQl_Object = MibTableColumn
sleSynceIfSendQl = _SleSynceIfSendQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 7),
    _SleSynceIfSendQl_Type()
)
sleSynceIfSendQl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfSendQl.setStatus("current")


class _SleSynceIfHoldOff_Type(Integer32):
    """Custom type sleSynceIfHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_SleSynceIfHoldOff_Type.__name__ = "Integer32"
_SleSynceIfHoldOff_Object = MibTableColumn
sleSynceIfHoldOff = _SleSynceIfHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 8),
    _SleSynceIfHoldOff_Type()
)
sleSynceIfHoldOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfHoldOff.setStatus("current")


class _SleSynceIfWaitToRestore_Type(Integer32):
    """Custom type sleSynceIfWaitToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SleSynceIfWaitToRestore_Type.__name__ = "Integer32"
_SleSynceIfWaitToRestore_Object = MibTableColumn
sleSynceIfWaitToRestore = _SleSynceIfWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 1, 1, 9),
    _SleSynceIfWaitToRestore_Type()
)
sleSynceIfWaitToRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfWaitToRestore.setStatus("current")
_SleSynceIfControl_ObjectIdentity = ObjectIdentity
sleSynceIfControl = _SleSynceIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2)
)


class _SleSynceIfControlRequest_Type(Integer32):
    """Custom type sleSynceIfControlRequest based on Integer32"""
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
        *(("setSynceIfAddInputSource", 1),
          ("setSynceIfDelInputSource", 2),
          ("setSynceIfAddOutputSource", 3),
          ("setSynceIfDelOutputSource", 4),
          ("setSynceIfRecvQl", 5),
          ("setSynceIfSendQl", 6),
          ("setSynceIfHoldOff", 7),
          ("setSynceIfWaitToRestore", 8))
    )


_SleSynceIfControlRequest_Type.__name__ = "Integer32"
_SleSynceIfControlRequest_Object = MibScalar
sleSynceIfControlRequest = _SleSynceIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 1),
    _SleSynceIfControlRequest_Type()
)
sleSynceIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlRequest.setStatus("current")
_SleSynceIfControlStatus_Type = SleControlStatusType
_SleSynceIfControlStatus_Object = MibScalar
sleSynceIfControlStatus = _SleSynceIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 2),
    _SleSynceIfControlStatus_Type()
)
sleSynceIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfControlStatus.setStatus("current")
_SleSynceIfControlTimer_Type = Gauge32
_SleSynceIfControlTimer_Object = MibScalar
sleSynceIfControlTimer = _SleSynceIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 3),
    _SleSynceIfControlTimer_Type()
)
sleSynceIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlTimer.setStatus("current")
_SleSynceIfControlTimeStamp_Type = TimeTicks
_SleSynceIfControlTimeStamp_Object = MibScalar
sleSynceIfControlTimeStamp = _SleSynceIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 4),
    _SleSynceIfControlTimeStamp_Type()
)
sleSynceIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfControlTimeStamp.setStatus("current")
_SleSynceIfControlReqResult_Type = SleControlRequestResultType
_SleSynceIfControlReqResult_Object = MibScalar
sleSynceIfControlReqResult = _SleSynceIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 5),
    _SleSynceIfControlReqResult_Type()
)
sleSynceIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceIfControlReqResult.setStatus("current")


class _SleSynceIfControlIfIndex_Type(Integer32):
    """Custom type sleSynceIfControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSynceIfControlIfIndex_Type.__name__ = "Integer32"
_SleSynceIfControlIfIndex_Object = MibScalar
sleSynceIfControlIfIndex = _SleSynceIfControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 6),
    _SleSynceIfControlIfIndex_Type()
)
sleSynceIfControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlIfIndex.setStatus("current")


class _SleSynceIfControlPriority_Type(Integer32):
    """Custom type sleSynceIfControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleSynceIfControlPriority_Type.__name__ = "Integer32"
_SleSynceIfControlPriority_Object = MibScalar
sleSynceIfControlPriority = _SleSynceIfControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 7),
    _SleSynceIfControlPriority_Type()
)
sleSynceIfControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlPriority.setStatus("current")
_SleSynceIfControlConfigRecvQl_Type = SynceClockQualityLevel
_SleSynceIfControlConfigRecvQl_Object = MibScalar
sleSynceIfControlConfigRecvQl = _SleSynceIfControlConfigRecvQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 8),
    _SleSynceIfControlConfigRecvQl_Type()
)
sleSynceIfControlConfigRecvQl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlConfigRecvQl.setStatus("current")
_SleSynceIfControlConfigSendQl_Type = SynceClockQualityLevel
_SleSynceIfControlConfigSendQl_Object = MibScalar
sleSynceIfControlConfigSendQl = _SleSynceIfControlConfigSendQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 9),
    _SleSynceIfControlConfigSendQl_Type()
)
sleSynceIfControlConfigSendQl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlConfigSendQl.setStatus("current")


class _SleSynceIfControlHoldOff_Type(Integer32):
    """Custom type sleSynceIfControlHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_SleSynceIfControlHoldOff_Type.__name__ = "Integer32"
_SleSynceIfControlHoldOff_Object = MibScalar
sleSynceIfControlHoldOff = _SleSynceIfControlHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 10),
    _SleSynceIfControlHoldOff_Type()
)
sleSynceIfControlHoldOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlHoldOff.setStatus("current")


class _SleSynceIfControlWaitToRestore_Type(Integer32):
    """Custom type sleSynceIfControlWaitToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SleSynceIfControlWaitToRestore_Type.__name__ = "Integer32"
_SleSynceIfControlWaitToRestore_Object = MibScalar
sleSynceIfControlWaitToRestore = _SleSynceIfControlWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 2, 11),
    _SleSynceIfControlWaitToRestore_Type()
)
sleSynceIfControlWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceIfControlWaitToRestore.setStatus("current")
_SleSynceIfNotification_ObjectIdentity = ObjectIdentity
sleSynceIfNotification = _SleSynceIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3)
)
_SleSynceInputSource_ObjectIdentity = ObjectIdentity
sleSynceInputSource = _SleSynceInputSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4)
)
_SleSynceInputSourceTable_Object = MibTable
sleSynceInputSourceTable = _SleSynceInputSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1)
)
if mibBuilder.loadTexts:
    sleSynceInputSourceTable.setStatus("current")
_SleSynceInputSourceEntry_Object = MibTableRow
sleSynceInputSourceEntry = _SleSynceInputSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1)
)
sleSynceInputSourceEntry.setIndexNames(
    (0, "SLE-SYNCE-MIB", "sleSynceInputSourceIfIndex"),
)
if mibBuilder.loadTexts:
    sleSynceInputSourceEntry.setStatus("current")


class _SleSynceInputSourceIfIndex_Type(Integer32):
    """Custom type sleSynceInputSourceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSynceInputSourceIfIndex_Type.__name__ = "Integer32"
_SleSynceInputSourceIfIndex_Object = MibTableColumn
sleSynceInputSourceIfIndex = _SleSynceInputSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 1),
    _SleSynceInputSourceIfIndex_Type()
)
sleSynceInputSourceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceIfIndex.setStatus("current")


class _SleSynceInputSourceName_Type(OctetString):
    """Custom type sleSynceInputSourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleSynceInputSourceName_Type.__name__ = "OctetString"
_SleSynceInputSourceName_Object = MibTableColumn
sleSynceInputSourceName = _SleSynceInputSourceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 2),
    _SleSynceInputSourceName_Type()
)
sleSynceInputSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceName.setStatus("current")


class _SleSynceInputSourcePriority_Type(Integer32):
    """Custom type sleSynceInputSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleSynceInputSourcePriority_Type.__name__ = "Integer32"
_SleSynceInputSourcePriority_Object = MibTableColumn
sleSynceInputSourcePriority = _SleSynceInputSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 3),
    _SleSynceInputSourcePriority_Type()
)
sleSynceInputSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourcePriority.setStatus("current")


class _SleSynceInputSourceEsmcState_Type(Integer32):
    """Custom type sleSynceInputSourceEsmcState based on Integer32"""
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
        *(("idle", 0),
          ("start", 1),
          ("ok", 2),
          ("failed", 3))
    )


_SleSynceInputSourceEsmcState_Type.__name__ = "Integer32"
_SleSynceInputSourceEsmcState_Object = MibTableColumn
sleSynceInputSourceEsmcState = _SleSynceInputSourceEsmcState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 4),
    _SleSynceInputSourceEsmcState_Type()
)
sleSynceInputSourceEsmcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceEsmcState.setStatus("current")


class _SleSynceInputSourceSelected_Type(Integer32):
    """Custom type sleSynceInputSourceSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SleSynceInputSourceSelected_Type.__name__ = "Integer32"
_SleSynceInputSourceSelected_Object = MibTableColumn
sleSynceInputSourceSelected = _SleSynceInputSourceSelected_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 5),
    _SleSynceInputSourceSelected_Type()
)
sleSynceInputSourceSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceSelected.setStatus("current")
_SleSynceInputSourceConfigRecvQl_Type = SynceClockQualityLevel
_SleSynceInputSourceConfigRecvQl_Object = MibTableColumn
sleSynceInputSourceConfigRecvQl = _SleSynceInputSourceConfigRecvQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 6),
    _SleSynceInputSourceConfigRecvQl_Type()
)
sleSynceInputSourceConfigRecvQl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceConfigRecvQl.setStatus("current")
_SleSynceInputSourceRecvQl_Type = SynceClockQualityLevel
_SleSynceInputSourceRecvQl_Object = MibTableColumn
sleSynceInputSourceRecvQl = _SleSynceInputSourceRecvQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 7),
    _SleSynceInputSourceRecvQl_Type()
)
sleSynceInputSourceRecvQl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceRecvQl.setStatus("current")


class _SleSynceInputSourceSignalFail_Type(Integer32):
    """Custom type sleSynceInputSourceSignalFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SleSynceInputSourceSignalFail_Type.__name__ = "Integer32"
_SleSynceInputSourceSignalFail_Object = MibTableColumn
sleSynceInputSourceSignalFail = _SleSynceInputSourceSignalFail_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 8),
    _SleSynceInputSourceSignalFail_Type()
)
sleSynceInputSourceSignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceSignalFail.setStatus("current")


class _SleSynceInputSourceCmd_Type(Integer32):
    """Custom type sleSynceInputSourceCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockout", 1),
          ("manual", 2))
    )


_SleSynceInputSourceCmd_Type.__name__ = "Integer32"
_SleSynceInputSourceCmd_Object = MibTableColumn
sleSynceInputSourceCmd = _SleSynceInputSourceCmd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 1, 1, 9),
    _SleSynceInputSourceCmd_Type()
)
sleSynceInputSourceCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceCmd.setStatus("current")
_SleSynceInputSourceControl_ObjectIdentity = ObjectIdentity
sleSynceInputSourceControl = _SleSynceInputSourceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2)
)


class _SleSynceInputSourceControlRequest_Type(Integer32):
    """Custom type sleSynceInputSourceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSynceInputsourceSwitch", 1),
          ("setSynceInputsourceLockout", 2))
    )


_SleSynceInputSourceControlRequest_Type.__name__ = "Integer32"
_SleSynceInputSourceControlRequest_Object = MibScalar
sleSynceInputSourceControlRequest = _SleSynceInputSourceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 1),
    _SleSynceInputSourceControlRequest_Type()
)
sleSynceInputSourceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlRequest.setStatus("current")
_SleSynceInputSourceControlStatus_Type = SleControlStatusType
_SleSynceInputSourceControlStatus_Object = MibScalar
sleSynceInputSourceControlStatus = _SleSynceInputSourceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 2),
    _SleSynceInputSourceControlStatus_Type()
)
sleSynceInputSourceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlStatus.setStatus("current")
_SleSynceInputSourceControlTimer_Type = Gauge32
_SleSynceInputSourceControlTimer_Object = MibScalar
sleSynceInputSourceControlTimer = _SleSynceInputSourceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 3),
    _SleSynceInputSourceControlTimer_Type()
)
sleSynceInputSourceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlTimer.setStatus("current")
_SleSynceInputSourceControlTimeStamp_Type = TimeTicks
_SleSynceInputSourceControlTimeStamp_Object = MibScalar
sleSynceInputSourceControlTimeStamp = _SleSynceInputSourceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 4),
    _SleSynceInputSourceControlTimeStamp_Type()
)
sleSynceInputSourceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlTimeStamp.setStatus("current")
_SleSynceInputSourceControlReqResult_Type = SleControlRequestResultType
_SleSynceInputSourceControlReqResult_Object = MibScalar
sleSynceInputSourceControlReqResult = _SleSynceInputSourceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 5),
    _SleSynceInputSourceControlReqResult_Type()
)
sleSynceInputSourceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlReqResult.setStatus("current")


class _SleSynceInputSourceControlIfIndex_Type(Integer32):
    """Custom type sleSynceInputSourceControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSynceInputSourceControlIfIndex_Type.__name__ = "Integer32"
_SleSynceInputSourceControlIfIndex_Object = MibScalar
sleSynceInputSourceControlIfIndex = _SleSynceInputSourceControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 6),
    _SleSynceInputSourceControlIfIndex_Type()
)
sleSynceInputSourceControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlIfIndex.setStatus("current")


class _SleSynceInputSourceControlSwitchType_Type(Integer32):
    """Custom type sleSynceInputSourceControlSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("manual", 2))
    )


_SleSynceInputSourceControlSwitchType_Type.__name__ = "Integer32"
_SleSynceInputSourceControlSwitchType_Object = MibScalar
sleSynceInputSourceControlSwitchType = _SleSynceInputSourceControlSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 7),
    _SleSynceInputSourceControlSwitchType_Type()
)
sleSynceInputSourceControlSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlSwitchType.setStatus("current")


class _SleSynceInputSourceControlLockoutState_Type(Integer32):
    """Custom type sleSynceInputSourceControlLockoutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_SleSynceInputSourceControlLockoutState_Type.__name__ = "Integer32"
_SleSynceInputSourceControlLockoutState_Object = MibScalar
sleSynceInputSourceControlLockoutState = _SleSynceInputSourceControlLockoutState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 2, 8),
    _SleSynceInputSourceControlLockoutState_Type()
)
sleSynceInputSourceControlLockoutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSynceInputSourceControlLockoutState.setStatus("current")
_SleSynceInputSourceNotification_ObjectIdentity = ObjectIdentity
sleSynceInputSourceNotification = _SleSynceInputSourceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 3)
)
_SleSynceOutputSource_ObjectIdentity = ObjectIdentity
sleSynceOutputSource = _SleSynceOutputSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5)
)
_SleSynceOutputSourceTable_Object = MibTable
sleSynceOutputSourceTable = _SleSynceOutputSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5, 1)
)
if mibBuilder.loadTexts:
    sleSynceOutputSourceTable.setStatus("current")
_SleSynceOutputSourceEntry_Object = MibTableRow
sleSynceOutputSourceEntry = _SleSynceOutputSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5, 1, 1)
)
sleSynceOutputSourceEntry.setIndexNames(
    (0, "SLE-SYNCE-MIB", "sleSynceOutputSourceIfIndex"),
)
if mibBuilder.loadTexts:
    sleSynceOutputSourceEntry.setStatus("current")


class _SleSynceOutputSourceIfIndex_Type(Integer32):
    """Custom type sleSynceOutputSourceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSynceOutputSourceIfIndex_Type.__name__ = "Integer32"
_SleSynceOutputSourceIfIndex_Object = MibTableColumn
sleSynceOutputSourceIfIndex = _SleSynceOutputSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5, 1, 1, 1),
    _SleSynceOutputSourceIfIndex_Type()
)
sleSynceOutputSourceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceOutputSourceIfIndex.setStatus("current")


class _SleSynceOutputSourceName_Type(OctetString):
    """Custom type sleSynceOutputSourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleSynceOutputSourceName_Type.__name__ = "OctetString"
_SleSynceOutputSourceName_Object = MibTableColumn
sleSynceOutputSourceName = _SleSynceOutputSourceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5, 1, 1, 2),
    _SleSynceOutputSourceName_Type()
)
sleSynceOutputSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceOutputSourceName.setStatus("current")
_SleSynceOutputSourceConfigSendQl_Type = SynceClockQualityLevel
_SleSynceOutputSourceConfigSendQl_Object = MibTableColumn
sleSynceOutputSourceConfigSendQl = _SleSynceOutputSourceConfigSendQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5, 1, 1, 3),
    _SleSynceOutputSourceConfigSendQl_Type()
)
sleSynceOutputSourceConfigSendQl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceOutputSourceConfigSendQl.setStatus("current")
_SleSynceOutputSourceSystemQl_Type = SynceClockQualityLevel
_SleSynceOutputSourceSystemQl_Object = MibTableColumn
sleSynceOutputSourceSystemQl = _SleSynceOutputSourceSystemQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5, 1, 1, 4),
    _SleSynceOutputSourceSystemQl_Type()
)
sleSynceOutputSourceSystemQl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceOutputSourceSystemQl.setStatus("current")
_SleSynceOutputSourceSendQl_Type = SynceClockQualityLevel
_SleSynceOutputSourceSendQl_Object = MibTableColumn
sleSynceOutputSourceSendQl = _SleSynceOutputSourceSendQl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 5, 1, 1, 5),
    _SleSynceOutputSourceSendQl_Type()
)
sleSynceOutputSourceSendQl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSynceOutputSourceSendQl.setStatus("current")

# Managed Objects groups

sleSynceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 29)
)
sleSynceObjectGroup.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfEnableIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableName"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableState"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlTimer"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlState"),
        ("SLE-SYNCE-MIB", "sleSynceIfIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfName"),
        ("SLE-SYNCE-MIB", "sleSynceIfInputSource"),
        ("SLE-SYNCE-MIB", "sleSynceIfOoutputSource"),
        ("SLE-SYNCE-MIB", "sleSynceIfPriority"),
        ("SLE-SYNCE-MIB", "sleSynceIfRecvQl"),
        ("SLE-SYNCE-MIB", "sleSynceIfSendQl"),
        ("SLE-SYNCE-MIB", "sleSynceIfHoldOff"),
        ("SLE-SYNCE-MIB", "sleSynceIfWaitToRestore"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimer"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlPriority"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlConfigRecvQl"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlConfigSendQl"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlHoldOff"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlWaitToRestore"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceName"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceEsmcState"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceSelected"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceConfigRecvQl"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceRecvQl"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceSignalFail"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceCmd"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlSwitchType"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlLockoutState"),
        ("SLE-SYNCE-MIB", "sleSynceOutputSourceIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceOutputSourceName"),
        ("SLE-SYNCE-MIB", "sleSynceOutputSourceConfigSendQl"),
        ("SLE-SYNCE-MIB", "sleSynceOutputSourceSystemQl"),
        ("SLE-SYNCE-MIB", "sleSynceOutputSourceSendQl"),
        ("SLE-SYNCE-MIB", "sleSynceSyncOption"),
        ("SLE-SYNCE-MIB", "sleSynceSelectionMode"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlTimer"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlSyncOption"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlSelectionMode"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourcePriority"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlTimer"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSynceObjectGroup.setStatus("current")


# Notification objects

sleSynceSyncOptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 3, 1)
)
sleSynceSyncOptionChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceModeControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlSyncOption"))
)
if mibBuilder.loadTexts:
    sleSynceSyncOptionChanged.setStatus(
        "current"
    )

sleSynceSelectionModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 1, 3, 2)
)
sleSynceSelectionModeChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceModeControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceModeControlSelectionMode"))
)
if mibBuilder.loadTexts:
    sleSynceSelectionModeChanged.setStatus(
        "current"
    )

sleSynceIfEnableStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 2, 3, 1)
)
sleSynceIfEnableStateChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfEnableControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfEnableControlState"))
)
if mibBuilder.loadTexts:
    sleSynceIfEnableStateChanged.setStatus(
        "current"
    )

sleSynceIfAddInputSourceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 1)
)
sleSynceIfAddInputSourceChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlPriority"))
)
if mibBuilder.loadTexts:
    sleSynceIfAddInputSourceChanged.setStatus(
        "current"
    )

sleSynceIfDelInputSourceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 2)
)
sleSynceIfDelInputSourceChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"))
)
if mibBuilder.loadTexts:
    sleSynceIfDelInputSourceChanged.setStatus(
        "current"
    )

sleSynceIfAddOutputSourceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 3)
)
sleSynceIfAddOutputSourceChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"))
)
if mibBuilder.loadTexts:
    sleSynceIfAddOutputSourceChanged.setStatus(
        "current"
    )

sleSynceIfDelOutputSourceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 4)
)
sleSynceIfDelOutputSourceChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"))
)
if mibBuilder.loadTexts:
    sleSynceIfDelOutputSourceChanged.setStatus(
        "current"
    )

sleSynceIfRecvQlChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 5)
)
sleSynceIfRecvQlChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlConfigRecvQl"))
)
if mibBuilder.loadTexts:
    sleSynceIfRecvQlChanged.setStatus(
        "current"
    )

sleSynceIfSendQlChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 6)
)
sleSynceIfSendQlChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlConfigSendQl"))
)
if mibBuilder.loadTexts:
    sleSynceIfSendQlChanged.setStatus(
        "current"
    )

sleSynceIfHoldOffChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 7)
)
sleSynceIfHoldOffChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlHoldOff"))
)
if mibBuilder.loadTexts:
    sleSynceIfHoldOffChanged.setStatus(
        "current"
    )

sleSynceIfWaitToRestoreChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 3, 3, 8)
)
sleSynceIfWaitToRestoreChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceIfControlWaitToRestore"))
)
if mibBuilder.loadTexts:
    sleSynceIfWaitToRestoreChanged.setStatus(
        "current"
    )

sleSynceInputSourceSwitchChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 3, 1)
)
sleSynceInputSourceSwitchChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceInputSourceControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlSwitchType"))
)
if mibBuilder.loadTexts:
    sleSynceInputSourceSwitchChanged.setStatus(
        "current"
    )

sleSynceInputSourceLockoutChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 4, 3, 2)
)
sleSynceInputSourceLockoutChanged.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceInputSourceControlRequest"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlStatus"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlTimeStamp"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlReqResult"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlIfIndex"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceControlLockoutState"))
)
if mibBuilder.loadTexts:
    sleSynceInputSourceLockoutChanged.setStatus(
        "current"
    )


# Notifications groups

sleSynceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 93, 30)
)
sleSynceNotificationGroup.setObjects(
      *(("SLE-SYNCE-MIB", "sleSynceIfEnableStateChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfAddInputSourceChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfDelInputSourceChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfAddOutputSourceChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfDelOutputSourceChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfRecvQlChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfSendQlChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfHoldOffChanged"),
        ("SLE-SYNCE-MIB", "sleSynceIfWaitToRestoreChanged"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceSwitchChanged"),
        ("SLE-SYNCE-MIB", "sleSynceInputSourceLockoutChanged"),
        ("SLE-SYNCE-MIB", "sleSynceSyncOptionChanged"),
        ("SLE-SYNCE-MIB", "sleSynceSelectionModeChanged"))
)
if mibBuilder.loadTexts:
    sleSynceNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-SYNCE-MIB",
    **{"SynceClockQualityLevel": SynceClockQualityLevel,
       "sleSynce": sleSynce,
       "sleSynceBaseMode": sleSynceBaseMode,
       "sleSynceBaseModeInfo": sleSynceBaseModeInfo,
       "sleSynceSyncOption": sleSynceSyncOption,
       "sleSynceSelectionMode": sleSynceSelectionMode,
       "sleSynceBaseModeControl": sleSynceBaseModeControl,
       "sleSynceModeControlRequest": sleSynceModeControlRequest,
       "sleSynceModeControlStatus": sleSynceModeControlStatus,
       "sleSynceModeControlTimer": sleSynceModeControlTimer,
       "sleSynceModeControlTimeStamp": sleSynceModeControlTimeStamp,
       "sleSynceModeControlReqResult": sleSynceModeControlReqResult,
       "sleSynceModeControlSyncOption": sleSynceModeControlSyncOption,
       "sleSynceModeControlSelectionMode": sleSynceModeControlSelectionMode,
       "sleSynceBaseModeNotification": sleSynceBaseModeNotification,
       "sleSynceSyncOptionChanged": sleSynceSyncOptionChanged,
       "sleSynceSelectionModeChanged": sleSynceSelectionModeChanged,
       "sleSynceIfEnable": sleSynceIfEnable,
       "sleSynceIfEnableTable": sleSynceIfEnableTable,
       "sleSynceIfEnableEntry": sleSynceIfEnableEntry,
       "sleSynceIfEnableIfIndex": sleSynceIfEnableIfIndex,
       "sleSynceIfEnableName": sleSynceIfEnableName,
       "sleSynceIfEnableState": sleSynceIfEnableState,
       "sleSynceIfEnableControl": sleSynceIfEnableControl,
       "sleSynceIfEnableControlRequest": sleSynceIfEnableControlRequest,
       "sleSynceIfEnableControlStatus": sleSynceIfEnableControlStatus,
       "sleSynceIfEnableControlTimer": sleSynceIfEnableControlTimer,
       "sleSynceIfEnableControlTimeStamp": sleSynceIfEnableControlTimeStamp,
       "sleSynceIfEnableControlReqResult": sleSynceIfEnableControlReqResult,
       "sleSynceIfEnableControlIfIndex": sleSynceIfEnableControlIfIndex,
       "sleSynceIfEnableControlState": sleSynceIfEnableControlState,
       "sleSynceIfEnableNotification": sleSynceIfEnableNotification,
       "sleSynceIfEnableStateChanged": sleSynceIfEnableStateChanged,
       "sleSynceIf": sleSynceIf,
       "sleSynceIfTable": sleSynceIfTable,
       "sleSynceIfEntry": sleSynceIfEntry,
       "sleSynceIfIfIndex": sleSynceIfIfIndex,
       "sleSynceIfName": sleSynceIfName,
       "sleSynceIfInputSource": sleSynceIfInputSource,
       "sleSynceIfOoutputSource": sleSynceIfOoutputSource,
       "sleSynceIfPriority": sleSynceIfPriority,
       "sleSynceIfRecvQl": sleSynceIfRecvQl,
       "sleSynceIfSendQl": sleSynceIfSendQl,
       "sleSynceIfHoldOff": sleSynceIfHoldOff,
       "sleSynceIfWaitToRestore": sleSynceIfWaitToRestore,
       "sleSynceIfControl": sleSynceIfControl,
       "sleSynceIfControlRequest": sleSynceIfControlRequest,
       "sleSynceIfControlStatus": sleSynceIfControlStatus,
       "sleSynceIfControlTimer": sleSynceIfControlTimer,
       "sleSynceIfControlTimeStamp": sleSynceIfControlTimeStamp,
       "sleSynceIfControlReqResult": sleSynceIfControlReqResult,
       "sleSynceIfControlIfIndex": sleSynceIfControlIfIndex,
       "sleSynceIfControlPriority": sleSynceIfControlPriority,
       "sleSynceIfControlConfigRecvQl": sleSynceIfControlConfigRecvQl,
       "sleSynceIfControlConfigSendQl": sleSynceIfControlConfigSendQl,
       "sleSynceIfControlHoldOff": sleSynceIfControlHoldOff,
       "sleSynceIfControlWaitToRestore": sleSynceIfControlWaitToRestore,
       "sleSynceIfNotification": sleSynceIfNotification,
       "sleSynceIfAddInputSourceChanged": sleSynceIfAddInputSourceChanged,
       "sleSynceIfDelInputSourceChanged": sleSynceIfDelInputSourceChanged,
       "sleSynceIfAddOutputSourceChanged": sleSynceIfAddOutputSourceChanged,
       "sleSynceIfDelOutputSourceChanged": sleSynceIfDelOutputSourceChanged,
       "sleSynceIfRecvQlChanged": sleSynceIfRecvQlChanged,
       "sleSynceIfSendQlChanged": sleSynceIfSendQlChanged,
       "sleSynceIfHoldOffChanged": sleSynceIfHoldOffChanged,
       "sleSynceIfWaitToRestoreChanged": sleSynceIfWaitToRestoreChanged,
       "sleSynceInputSource": sleSynceInputSource,
       "sleSynceInputSourceTable": sleSynceInputSourceTable,
       "sleSynceInputSourceEntry": sleSynceInputSourceEntry,
       "sleSynceInputSourceIfIndex": sleSynceInputSourceIfIndex,
       "sleSynceInputSourceName": sleSynceInputSourceName,
       "sleSynceInputSourcePriority": sleSynceInputSourcePriority,
       "sleSynceInputSourceEsmcState": sleSynceInputSourceEsmcState,
       "sleSynceInputSourceSelected": sleSynceInputSourceSelected,
       "sleSynceInputSourceConfigRecvQl": sleSynceInputSourceConfigRecvQl,
       "sleSynceInputSourceRecvQl": sleSynceInputSourceRecvQl,
       "sleSynceInputSourceSignalFail": sleSynceInputSourceSignalFail,
       "sleSynceInputSourceCmd": sleSynceInputSourceCmd,
       "sleSynceInputSourceControl": sleSynceInputSourceControl,
       "sleSynceInputSourceControlRequest": sleSynceInputSourceControlRequest,
       "sleSynceInputSourceControlStatus": sleSynceInputSourceControlStatus,
       "sleSynceInputSourceControlTimer": sleSynceInputSourceControlTimer,
       "sleSynceInputSourceControlTimeStamp": sleSynceInputSourceControlTimeStamp,
       "sleSynceInputSourceControlReqResult": sleSynceInputSourceControlReqResult,
       "sleSynceInputSourceControlIfIndex": sleSynceInputSourceControlIfIndex,
       "sleSynceInputSourceControlSwitchType": sleSynceInputSourceControlSwitchType,
       "sleSynceInputSourceControlLockoutState": sleSynceInputSourceControlLockoutState,
       "sleSynceInputSourceNotification": sleSynceInputSourceNotification,
       "sleSynceInputSourceSwitchChanged": sleSynceInputSourceSwitchChanged,
       "sleSynceInputSourceLockoutChanged": sleSynceInputSourceLockoutChanged,
       "sleSynceOutputSource": sleSynceOutputSource,
       "sleSynceOutputSourceTable": sleSynceOutputSourceTable,
       "sleSynceOutputSourceEntry": sleSynceOutputSourceEntry,
       "sleSynceOutputSourceIfIndex": sleSynceOutputSourceIfIndex,
       "sleSynceOutputSourceName": sleSynceOutputSourceName,
       "sleSynceOutputSourceConfigSendQl": sleSynceOutputSourceConfigSendQl,
       "sleSynceOutputSourceSystemQl": sleSynceOutputSourceSystemQl,
       "sleSynceOutputSourceSendQl": sleSynceOutputSourceSendQl,
       "sleSynceObjectGroup": sleSynceObjectGroup,
       "sleSynceNotificationGroup": sleSynceNotificationGroup}
)
