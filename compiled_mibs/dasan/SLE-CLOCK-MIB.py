# SNMP MIB module (SLE-CLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-CLOCK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:21 2025
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

sleClock = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClockSourceAll(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bitsa", 1),
          ("bitsb", 2),
          ("synce", 3),
          ("ieee1588", 7),
          ("gps10m", 11),
          ("int", 12))
    )



class ClockQualityLevel(TextualConvention, Integer32):
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



class ClockSourceSystem(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bitsa", 1),
          ("bitsb", 2),
          ("synce", 3),
          ("ieee1588", 7),
          ("gps10m", 11),
          ("int", 12))
    )



class ClockQualityLevelValid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("prc", 1),
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

_SleClockBaseMode_ObjectIdentity = ObjectIdentity
sleClockBaseMode = _SleClockBaseMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1)
)
_SleClockBaseModeInfo_ObjectIdentity = ObjectIdentity
sleClockBaseModeInfo = _SleClockBaseModeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 1)
)


class _SleClockSyncOption_Type(Integer32):
    """Custom type sleClockSyncOption based on Integer32"""
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


_SleClockSyncOption_Type.__name__ = "Integer32"
_SleClockSyncOption_Object = MibScalar
sleClockSyncOption = _SleClockSyncOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 1, 1),
    _SleClockSyncOption_Type()
)
sleClockSyncOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSyncOption.setStatus("current")


class _SleClockSelectionMode_Type(Integer32):
    """Custom type sleClockSelectionMode based on Integer32"""
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


_SleClockSelectionMode_Type.__name__ = "Integer32"
_SleClockSelectionMode_Object = MibScalar
sleClockSelectionMode = _SleClockSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 1, 2),
    _SleClockSelectionMode_Type()
)
sleClockSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectionMode.setStatus("current")
_SleClockBaseModeControl_ObjectIdentity = ObjectIdentity
sleClockBaseModeControl = _SleClockBaseModeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2)
)


class _SleClockModeControlRequest_Type(Integer32):
    """Custom type sleClockModeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSyncOption", 1),
          ("setSelectionMode", 2))
    )


_SleClockModeControlRequest_Type.__name__ = "Integer32"
_SleClockModeControlRequest_Object = MibScalar
sleClockModeControlRequest = _SleClockModeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2, 1),
    _SleClockModeControlRequest_Type()
)
sleClockModeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockModeControlRequest.setStatus("current")
_SleClockModeControlStatus_Type = SleControlStatusType
_SleClockModeControlStatus_Object = MibScalar
sleClockModeControlStatus = _SleClockModeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2, 2),
    _SleClockModeControlStatus_Type()
)
sleClockModeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockModeControlStatus.setStatus("current")
_SleClockModeControlTimer_Type = Gauge32
_SleClockModeControlTimer_Object = MibScalar
sleClockModeControlTimer = _SleClockModeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2, 3),
    _SleClockModeControlTimer_Type()
)
sleClockModeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockModeControlTimer.setStatus("current")
_SleClockModeControlTimeStamp_Type = TimeTicks
_SleClockModeControlTimeStamp_Object = MibScalar
sleClockModeControlTimeStamp = _SleClockModeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2, 4),
    _SleClockModeControlTimeStamp_Type()
)
sleClockModeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockModeControlTimeStamp.setStatus("current")
_SleClockModeControlReqResult_Type = SleControlRequestResultType
_SleClockModeControlReqResult_Object = MibScalar
sleClockModeControlReqResult = _SleClockModeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2, 5),
    _SleClockModeControlReqResult_Type()
)
sleClockModeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockModeControlReqResult.setStatus("current")


class _SleClockModeControlSyncOption_Type(Integer32):
    """Custom type sleClockModeControlSyncOption based on Integer32"""
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


_SleClockModeControlSyncOption_Type.__name__ = "Integer32"
_SleClockModeControlSyncOption_Object = MibScalar
sleClockModeControlSyncOption = _SleClockModeControlSyncOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2, 6),
    _SleClockModeControlSyncOption_Type()
)
sleClockModeControlSyncOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockModeControlSyncOption.setStatus("current")


class _SleClockModeControlSelectionMode_Type(Integer32):
    """Custom type sleClockModeControlSelectionMode based on Integer32"""
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


_SleClockModeControlSelectionMode_Type.__name__ = "Integer32"
_SleClockModeControlSelectionMode_Object = MibScalar
sleClockModeControlSelectionMode = _SleClockModeControlSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 2, 7),
    _SleClockModeControlSelectionMode_Type()
)
sleClockModeControlSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockModeControlSelectionMode.setStatus("current")
_SleClockBaseModeNotification_ObjectIdentity = ObjectIdentity
sleClockBaseModeNotification = _SleClockBaseModeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 3)
)
_SleClockBits_ObjectIdentity = ObjectIdentity
sleClockBits = _SleClockBits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2)
)
_SleClockBitsInfo_ObjectIdentity = ObjectIdentity
sleClockBitsInfo = _SleClockBitsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 1)
)


class _SleClockBitsType_Type(Integer32):
    """Custom type sleClockBitsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1", 1),
          ("e1", 2))
    )


_SleClockBitsType_Type.__name__ = "Integer32"
_SleClockBitsType_Object = MibScalar
sleClockBitsType = _SleClockBitsType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 1, 1),
    _SleClockBitsType_Type()
)
sleClockBitsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockBitsType.setStatus("current")


class _SleClockBitsFrameMode_Type(Integer32):
    """Custom type sleClockBitsFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sf", 1),
          ("esf", 2),
          ("g704", 3))
    )


_SleClockBitsFrameMode_Type.__name__ = "Integer32"
_SleClockBitsFrameMode_Object = MibScalar
sleClockBitsFrameMode = _SleClockBitsFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 1, 2),
    _SleClockBitsFrameMode_Type()
)
sleClockBitsFrameMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockBitsFrameMode.setStatus("current")


class _SleClockBitsLineEncoding_Type(Integer32):
    """Custom type sleClockBitsLineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b8zs", 1),
          ("ami", 2),
          ("hdb3", 3))
    )


_SleClockBitsLineEncoding_Type.__name__ = "Integer32"
_SleClockBitsLineEncoding_Object = MibScalar
sleClockBitsLineEncoding = _SleClockBitsLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 1, 3),
    _SleClockBitsLineEncoding_Type()
)
sleClockBitsLineEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockBitsLineEncoding.setStatus("current")
_SleClockBitsControl_ObjectIdentity = ObjectIdentity
sleClockBitsControl = _SleClockBitsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2)
)


class _SleClockBitsControlRequest_Type(Integer32):
    """Custom type sleClockBitsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setBitsMode", 1),
          ("setBitsLineEncoding", 2))
    )


_SleClockBitsControlRequest_Type.__name__ = "Integer32"
_SleClockBitsControlRequest_Object = MibScalar
sleClockBitsControlRequest = _SleClockBitsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 1),
    _SleClockBitsControlRequest_Type()
)
sleClockBitsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockBitsControlRequest.setStatus("current")
_SleClockBitsControlStatus_Type = SleControlStatusType
_SleClockBitsControlStatus_Object = MibScalar
sleClockBitsControlStatus = _SleClockBitsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 2),
    _SleClockBitsControlStatus_Type()
)
sleClockBitsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockBitsControlStatus.setStatus("current")
_SleClockBitsControlTimer_Type = Gauge32
_SleClockBitsControlTimer_Object = MibScalar
sleClockBitsControlTimer = _SleClockBitsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 3),
    _SleClockBitsControlTimer_Type()
)
sleClockBitsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockBitsControlTimer.setStatus("current")
_SleClockBitsControlTimeStamp_Type = TimeTicks
_SleClockBitsControlTimeStamp_Object = MibScalar
sleClockBitsControlTimeStamp = _SleClockBitsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 4),
    _SleClockBitsControlTimeStamp_Type()
)
sleClockBitsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockBitsControlTimeStamp.setStatus("current")
_SleClockBitsControlReqResult_Type = SleControlRequestResultType
_SleClockBitsControlReqResult_Object = MibScalar
sleClockBitsControlReqResult = _SleClockBitsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 5),
    _SleClockBitsControlReqResult_Type()
)
sleClockBitsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockBitsControlReqResult.setStatus("current")


class _SleClockBitsControlType_Type(Integer32):
    """Custom type sleClockBitsControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1", 1),
          ("e1", 2))
    )


_SleClockBitsControlType_Type.__name__ = "Integer32"
_SleClockBitsControlType_Object = MibScalar
sleClockBitsControlType = _SleClockBitsControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 6),
    _SleClockBitsControlType_Type()
)
sleClockBitsControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockBitsControlType.setStatus("current")


class _SleClockBitsControlFrameMode_Type(Integer32):
    """Custom type sleClockBitsControlFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sf", 1),
          ("esf", 2),
          ("g704", 3))
    )


_SleClockBitsControlFrameMode_Type.__name__ = "Integer32"
_SleClockBitsControlFrameMode_Object = MibScalar
sleClockBitsControlFrameMode = _SleClockBitsControlFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 7),
    _SleClockBitsControlFrameMode_Type()
)
sleClockBitsControlFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockBitsControlFrameMode.setStatus("current")


class _SleClockBitsControlLineEncoding_Type(Integer32):
    """Custom type sleClockBitsControlLineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b8zs", 1),
          ("ami", 2),
          ("hdb3", 3))
    )


_SleClockBitsControlLineEncoding_Type.__name__ = "Integer32"
_SleClockBitsControlLineEncoding_Object = MibScalar
sleClockBitsControlLineEncoding = _SleClockBitsControlLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 2, 8),
    _SleClockBitsControlLineEncoding_Type()
)
sleClockBitsControlLineEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockBitsControlLineEncoding.setStatus("current")
_SleClockBitsNotification_ObjectIdentity = ObjectIdentity
sleClockBitsNotification = _SleClockBitsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 3)
)
_SleClockQlSet_ObjectIdentity = ObjectIdentity
sleClockQlSet = _SleClockQlSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3)
)
_SleClockQlSetTable_Object = MibTable
sleClockQlSetTable = _SleClockQlSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 1)
)
if mibBuilder.loadTexts:
    sleClockQlSetTable.setStatus("current")
_SleClockQlSetEntry_Object = MibTableRow
sleClockQlSetEntry = _SleClockQlSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 1, 1)
)
sleClockQlSetEntry.setIndexNames(
    (0, "SLE-CLOCK-MIB", "sleClockQlSetSource"),
)
if mibBuilder.loadTexts:
    sleClockQlSetEntry.setStatus("current")
_SleClockQlSetSource_Type = ClockSourceAll
_SleClockQlSetSource_Object = MibTableColumn
sleClockQlSetSource = _SleClockQlSetSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 1, 1, 1),
    _SleClockQlSetSource_Type()
)
sleClockQlSetSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockQlSetSource.setStatus("current")
_SleClockQlSetQulatyLevel_Type = ClockQualityLevel
_SleClockQlSetQulatyLevel_Object = MibTableColumn
sleClockQlSetQulatyLevel = _SleClockQlSetQulatyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 1, 1, 2),
    _SleClockQlSetQulatyLevel_Type()
)
sleClockQlSetQulatyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockQlSetQulatyLevel.setStatus("current")
_SleClockQlSetControl_ObjectIdentity = ObjectIdentity
sleClockQlSetControl = _SleClockQlSetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2)
)


class _SleClockQlSetControlRequest_Type(Integer32):
    """Custom type sleClockQlSetControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setQualityLevel", 1)
    )


_SleClockQlSetControlRequest_Type.__name__ = "Integer32"
_SleClockQlSetControlRequest_Object = MibScalar
sleClockQlSetControlRequest = _SleClockQlSetControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2, 1),
    _SleClockQlSetControlRequest_Type()
)
sleClockQlSetControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockQlSetControlRequest.setStatus("current")
_SleClockQlSetControlStatus_Type = SleControlStatusType
_SleClockQlSetControlStatus_Object = MibScalar
sleClockQlSetControlStatus = _SleClockQlSetControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2, 2),
    _SleClockQlSetControlStatus_Type()
)
sleClockQlSetControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockQlSetControlStatus.setStatus("current")
_SleClockQlSetControlTimer_Type = Gauge32
_SleClockQlSetControlTimer_Object = MibScalar
sleClockQlSetControlTimer = _SleClockQlSetControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2, 3),
    _SleClockQlSetControlTimer_Type()
)
sleClockQlSetControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockQlSetControlTimer.setStatus("current")
_SleClockQlSetControlTimeStamp_Type = TimeTicks
_SleClockQlSetControlTimeStamp_Object = MibScalar
sleClockQlSetControlTimeStamp = _SleClockQlSetControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2, 4),
    _SleClockQlSetControlTimeStamp_Type()
)
sleClockQlSetControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockQlSetControlTimeStamp.setStatus("current")
_SleClockQlSetControlReqResult_Type = SleControlRequestResultType
_SleClockQlSetControlReqResult_Object = MibScalar
sleClockQlSetControlReqResult = _SleClockQlSetControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2, 5),
    _SleClockQlSetControlReqResult_Type()
)
sleClockQlSetControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockQlSetControlReqResult.setStatus("current")
_SleClockQlSetControlSoruce_Type = ClockSourceAll
_SleClockQlSetControlSoruce_Object = MibScalar
sleClockQlSetControlSoruce = _SleClockQlSetControlSoruce_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2, 6),
    _SleClockQlSetControlSoruce_Type()
)
sleClockQlSetControlSoruce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockQlSetControlSoruce.setStatus("current")
_SleClockQlSetControlQualityLevel_Type = ClockQualityLevel
_SleClockQlSetControlQualityLevel_Object = MibScalar
sleClockQlSetControlQualityLevel = _SleClockQlSetControlQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 2, 7),
    _SleClockQlSetControlQualityLevel_Type()
)
sleClockQlSetControlQualityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockQlSetControlQualityLevel.setStatus("current")
_SleClockQlNotification_ObjectIdentity = ObjectIdentity
sleClockQlNotification = _SleClockQlNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 3)
)
_SleClockSelected_ObjectIdentity = ObjectIdentity
sleClockSelected = _SleClockSelected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4)
)
_SleClockSelectedInfo_ObjectIdentity = ObjectIdentity
sleClockSelectedInfo = _SleClockSelectedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 1)
)
_SleClockSelectedSource_Type = ClockSourceSystem
_SleClockSelectedSource_Object = MibScalar
sleClockSelectedSource = _SleClockSelectedSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 1, 1),
    _SleClockSelectedSource_Type()
)
sleClockSelectedSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectedSource.setStatus("current")


class _SleClockSelectedState_Type(Integer32):
    """Custom type sleClockSelectedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 1),
          ("holdover", 2),
          ("locked", 3))
    )


_SleClockSelectedState_Type.__name__ = "Integer32"
_SleClockSelectedState_Object = MibScalar
sleClockSelectedState = _SleClockSelectedState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 1, 2),
    _SleClockSelectedState_Type()
)
sleClockSelectedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectedState.setStatus("current")
_SleClockSelectedQualityLevel_Type = ClockQualityLevel
_SleClockSelectedQualityLevel_Object = MibScalar
sleClockSelectedQualityLevel = _SleClockSelectedQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 1, 3),
    _SleClockSelectedQualityLevel_Type()
)
sleClockSelectedQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectedQualityLevel.setStatus("current")


class _SleClockSelectedSwitchType_Type(Integer32):
    """Custom type sleClockSelectedSwitchType based on Integer32"""
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
        *(("clear", 0),
          ("force", 1),
          ("man", 2),
          ("auto", 3))
    )


_SleClockSelectedSwitchType_Type.__name__ = "Integer32"
_SleClockSelectedSwitchType_Object = MibScalar
sleClockSelectedSwitchType = _SleClockSelectedSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 1, 4),
    _SleClockSelectedSwitchType_Type()
)
sleClockSelectedSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectedSwitchType.setStatus("current")
_SleClockSelectedControl_ObjectIdentity = ObjectIdentity
sleClockSelectedControl = _SleClockSelectedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 2)
)


class _SleClockSelectedControlRequest_Type(Integer32):
    """Custom type sleClockSelectedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSwitchClear", 1),
          ("setSwitchMan", 2))
    )


_SleClockSelectedControlRequest_Type.__name__ = "Integer32"
_SleClockSelectedControlRequest_Object = MibScalar
sleClockSelectedControlRequest = _SleClockSelectedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 2, 1),
    _SleClockSelectedControlRequest_Type()
)
sleClockSelectedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockSelectedControlRequest.setStatus("current")
_SleClockSelectedControlStatus_Type = SleControlStatusType
_SleClockSelectedControlStatus_Object = MibScalar
sleClockSelectedControlStatus = _SleClockSelectedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 2, 2),
    _SleClockSelectedControlStatus_Type()
)
sleClockSelectedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectedControlStatus.setStatus("current")
_SleClockSelectedControlTimer_Type = Gauge32
_SleClockSelectedControlTimer_Object = MibScalar
sleClockSelectedControlTimer = _SleClockSelectedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 2, 3),
    _SleClockSelectedControlTimer_Type()
)
sleClockSelectedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockSelectedControlTimer.setStatus("current")
_SleClockSelectedControlTimeStamp_Type = TimeTicks
_SleClockSelectedControlTimeStamp_Object = MibScalar
sleClockSelectedControlTimeStamp = _SleClockSelectedControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 2, 4),
    _SleClockSelectedControlTimeStamp_Type()
)
sleClockSelectedControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectedControlTimeStamp.setStatus("current")
_SleClockSelectedControlReqResult_Type = SleControlRequestResultType
_SleClockSelectedControlReqResult_Object = MibScalar
sleClockSelectedControlReqResult = _SleClockSelectedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 2, 5),
    _SleClockSelectedControlReqResult_Type()
)
sleClockSelectedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockSelectedControlReqResult.setStatus("current")
_SleClockSelectedControlDestSource_Type = ClockSourceSystem
_SleClockSelectedControlDestSource_Object = MibScalar
sleClockSelectedControlDestSource = _SleClockSelectedControlDestSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 2, 6),
    _SleClockSelectedControlDestSource_Type()
)
sleClockSelectedControlDestSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockSelectedControlDestSource.setStatus("current")
_SleClockSelectedNotification_ObjectIdentity = ObjectIdentity
sleClockSelectedNotification = _SleClockSelectedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 3)
)
_SleClockInputSource_ObjectIdentity = ObjectIdentity
sleClockInputSource = _SleClockInputSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5)
)
_SleClockInputSourceTable_Object = MibTable
sleClockInputSourceTable = _SleClockInputSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1)
)
if mibBuilder.loadTexts:
    sleClockInputSourceTable.setStatus("current")
_SleClockInputSourceEntry_Object = MibTableRow
sleClockInputSourceEntry = _SleClockInputSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1)
)
sleClockInputSourceEntry.setIndexNames(
    (0, "SLE-CLOCK-MIB", "sleClockInputSourceSource"),
)
if mibBuilder.loadTexts:
    sleClockInputSourceEntry.setStatus("current")
_SleClockInputSourceSource_Type = ClockSourceSystem
_SleClockInputSourceSource_Object = MibTableColumn
sleClockInputSourceSource = _SleClockInputSourceSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1, 1),
    _SleClockInputSourceSource_Type()
)
sleClockInputSourceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceSource.setStatus("current")


class _SleClockInputSourceUse_Type(Integer32):
    """Custom type sleClockInputSourceUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleClockInputSourceUse_Type.__name__ = "Integer32"
_SleClockInputSourceUse_Object = MibTableColumn
sleClockInputSourceUse = _SleClockInputSourceUse_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1, 2),
    _SleClockInputSourceUse_Type()
)
sleClockInputSourceUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceUse.setStatus("current")


class _SleClockInputSourcePriority_Type(Integer32):
    """Custom type sleClockInputSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleClockInputSourcePriority_Type.__name__ = "Integer32"
_SleClockInputSourcePriority_Object = MibTableColumn
sleClockInputSourcePriority = _SleClockInputSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1, 3),
    _SleClockInputSourcePriority_Type()
)
sleClockInputSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourcePriority.setStatus("current")


class _SleClockInputSourceIfName_Type(OctetString):
    """Custom type sleClockInputSourceIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleClockInputSourceIfName_Type.__name__ = "OctetString"
_SleClockInputSourceIfName_Object = MibTableColumn
sleClockInputSourceIfName = _SleClockInputSourceIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1, 4),
    _SleClockInputSourceIfName_Type()
)
sleClockInputSourceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceIfName.setStatus("current")
_SleClockInputSourceConfQulatyLevel_Type = ClockQualityLevel
_SleClockInputSourceConfQulatyLevel_Object = MibTableColumn
sleClockInputSourceConfQulatyLevel = _SleClockInputSourceConfQulatyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1, 5),
    _SleClockInputSourceConfQulatyLevel_Type()
)
sleClockInputSourceConfQulatyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceConfQulatyLevel.setStatus("current")
_SleClockInputSourceRecvQulatyLevel_Type = ClockQualityLevel
_SleClockInputSourceRecvQulatyLevel_Object = MibTableColumn
sleClockInputSourceRecvQulatyLevel = _SleClockInputSourceRecvQulatyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1, 6),
    _SleClockInputSourceRecvQulatyLevel_Type()
)
sleClockInputSourceRecvQulatyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceRecvQulatyLevel.setStatus("current")


class _SleClockInputSourceValid_Type(Integer32):
    """Custom type sleClockInputSourceValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_SleClockInputSourceValid_Type.__name__ = "Integer32"
_SleClockInputSourceValid_Object = MibTableColumn
sleClockInputSourceValid = _SleClockInputSourceValid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 1, 1, 7),
    _SleClockInputSourceValid_Type()
)
sleClockInputSourceValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceValid.setStatus("current")
_SleClockInputSourceControl_ObjectIdentity = ObjectIdentity
sleClockInputSourceControl = _SleClockInputSourceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2)
)


class _SleClockInputSourceControlRequest_Type(Integer32):
    """Custom type sleClockInputSourceControlRequest based on Integer32"""
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
        *(("setUseOn", 1),
          ("setUseOff", 2),
          ("setPriority", 3),
          ("setIfName", 4))
    )


_SleClockInputSourceControlRequest_Type.__name__ = "Integer32"
_SleClockInputSourceControlRequest_Object = MibScalar
sleClockInputSourceControlRequest = _SleClockInputSourceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 1),
    _SleClockInputSourceControlRequest_Type()
)
sleClockInputSourceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockInputSourceControlRequest.setStatus("current")
_SleClockInputSourceControlStatus_Type = SleControlStatusType
_SleClockInputSourceControlStatus_Object = MibScalar
sleClockInputSourceControlStatus = _SleClockInputSourceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 2),
    _SleClockInputSourceControlStatus_Type()
)
sleClockInputSourceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceControlStatus.setStatus("current")
_SleClockInputSourceControlTimer_Type = Gauge32
_SleClockInputSourceControlTimer_Object = MibScalar
sleClockInputSourceControlTimer = _SleClockInputSourceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 3),
    _SleClockInputSourceControlTimer_Type()
)
sleClockInputSourceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockInputSourceControlTimer.setStatus("current")
_SleClockInputSourceControlTimeStamp_Type = TimeTicks
_SleClockInputSourceControlTimeStamp_Object = MibScalar
sleClockInputSourceControlTimeStamp = _SleClockInputSourceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 4),
    _SleClockInputSourceControlTimeStamp_Type()
)
sleClockInputSourceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceControlTimeStamp.setStatus("current")
_SleClockInputSourceControlReqResult_Type = SleControlRequestResultType
_SleClockInputSourceControlReqResult_Object = MibScalar
sleClockInputSourceControlReqResult = _SleClockInputSourceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 5),
    _SleClockInputSourceControlReqResult_Type()
)
sleClockInputSourceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleClockInputSourceControlReqResult.setStatus("current")
_SleClockInputSourceControlSource_Type = ClockSourceSystem
_SleClockInputSourceControlSource_Object = MibScalar
sleClockInputSourceControlSource = _SleClockInputSourceControlSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 6),
    _SleClockInputSourceControlSource_Type()
)
sleClockInputSourceControlSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockInputSourceControlSource.setStatus("current")


class _SleClockInputSourceControlPriority_Type(Integer32):
    """Custom type sleClockInputSourceControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleClockInputSourceControlPriority_Type.__name__ = "Integer32"
_SleClockInputSourceControlPriority_Object = MibScalar
sleClockInputSourceControlPriority = _SleClockInputSourceControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 7),
    _SleClockInputSourceControlPriority_Type()
)
sleClockInputSourceControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockInputSourceControlPriority.setStatus("current")


class _SleClockInputSourceControlIfName_Type(OctetString):
    """Custom type sleClockInputSourceControlIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleClockInputSourceControlIfName_Type.__name__ = "OctetString"
_SleClockInputSourceControlIfName_Object = MibScalar
sleClockInputSourceControlIfName = _SleClockInputSourceControlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 2, 8),
    _SleClockInputSourceControlIfName_Type()
)
sleClockInputSourceControlIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleClockInputSourceControlIfName.setStatus("current")
_SleClockInputSourceNotification_ObjectIdentity = ObjectIdentity
sleClockInputSourceNotification = _SleClockInputSourceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 3)
)

# Managed Objects groups

sleClockObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 29)
)
sleClockObjectGroup.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockSyncOption"),
        ("SLE-CLOCK-MIB", "sleClockSelectionMode"),
        ("SLE-CLOCK-MIB", "sleClockModeControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockModeControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockModeControlTimer"),
        ("SLE-CLOCK-MIB", "sleClockModeControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockModeControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockModeControlSyncOption"),
        ("SLE-CLOCK-MIB", "sleClockModeControlSelectionMode"),
        ("SLE-CLOCK-MIB", "sleClockBitsType"),
        ("SLE-CLOCK-MIB", "sleClockBitsFrameMode"),
        ("SLE-CLOCK-MIB", "sleClockBitsLineEncoding"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlTimer"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlType"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlFrameMode"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlLineEncoding"),
        ("SLE-CLOCK-MIB", "sleClockQlSetSource"),
        ("SLE-CLOCK-MIB", "sleClockQlSetQulatyLevel"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlTimer"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlSoruce"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlQualityLevel"),
        ("SLE-CLOCK-MIB", "sleClockSelectedSource"),
        ("SLE-CLOCK-MIB", "sleClockSelectedState"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlTimer"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlDestSource"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceSource"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceUse"),
        ("SLE-CLOCK-MIB", "sleClockInputSourcePriority"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceIfName"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceConfQulatyLevel"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceRecvQulatyLevel"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceValid"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlTimer"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlSource"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlPriority"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlIfName"),
        ("SLE-CLOCK-MIB", "sleClockSelectedQualityLevel"),
        ("SLE-CLOCK-MIB", "sleClockSelectedSwitchType"))
)
if mibBuilder.loadTexts:
    sleClockObjectGroup.setStatus("current")


# Notification objects

sleClockSyncOptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 3, 1)
)
sleClockSyncOptionChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockModeControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockModeControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockModeControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockModeControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockModeControlSyncOption"))
)
if mibBuilder.loadTexts:
    sleClockSyncOptionChanged.setStatus(
        "current"
    )

sleClockSelectionModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 1, 3, 2)
)
sleClockSelectionModeChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockModeControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockModeControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockModeControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockModeControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockModeControlSelectionMode"))
)
if mibBuilder.loadTexts:
    sleClockSelectionModeChanged.setStatus(
        "current"
    )

sleClockBitsTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 3, 1)
)
sleClockBitsTypeChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockBitsControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlType"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlFrameMode"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlLineEncoding"))
)
if mibBuilder.loadTexts:
    sleClockBitsTypeChanged.setStatus(
        "current"
    )

sleClockBitsLineEncodingChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 2, 3, 2)
)
sleClockBitsLineEncodingChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockBitsControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockBitsControlLineEncoding"))
)
if mibBuilder.loadTexts:
    sleClockBitsLineEncodingChanged.setStatus(
        "current"
    )

sleClockQlSetQualityLevelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 3, 3, 1)
)
sleClockQlSetQualityLevelChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockQlSetControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlSoruce"),
        ("SLE-CLOCK-MIB", "sleClockQlSetControlQualityLevel"))
)
if mibBuilder.loadTexts:
    sleClockQlSetQualityLevelChanged.setStatus(
        "current"
    )

sleClockSwitchManChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 3, 1)
)
sleClockSwitchManChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockSelectedControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlDestSource"))
)
if mibBuilder.loadTexts:
    sleClockSwitchManChanged.setStatus(
        "current"
    )

sleClockSwitchClearChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 4, 3, 2)
)
sleClockSwitchClearChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockSelectedControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockSelectedControlReqResult"))
)
if mibBuilder.loadTexts:
    sleClockSwitchClearChanged.setStatus(
        "current"
    )

sleClockInputSourceUseOnChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 3, 1)
)
sleClockInputSourceUseOnChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockInputSourceControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlSource"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlPriority"))
)
if mibBuilder.loadTexts:
    sleClockInputSourceUseOnChanged.setStatus(
        "current"
    )

sleClockInputSourceUseOffChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 3, 2)
)
sleClockInputSourceUseOffChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockInputSourceControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlSource"))
)
if mibBuilder.loadTexts:
    sleClockInputSourceUseOffChanged.setStatus(
        "current"
    )

sleClockInputSourcePriorityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 3, 3)
)
sleClockInputSourcePriorityChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockInputSourceControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlSource"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlPriority"))
)
if mibBuilder.loadTexts:
    sleClockInputSourcePriorityChanged.setStatus(
        "current"
    )

sleClockInputSourceIfNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 5, 3, 4)
)
sleClockInputSourceIfNameChanged.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockInputSourceControlRequest"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlStatus"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlTimeStamp"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlReqResult"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlSource"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceControlIfName"))
)
if mibBuilder.loadTexts:
    sleClockInputSourceIfNameChanged.setStatus(
        "current"
    )


# Notifications groups

sleClockNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 92, 30)
)
sleClockNotificationGroup.setObjects(
      *(("SLE-CLOCK-MIB", "sleClockSyncOptionChanged"),
        ("SLE-CLOCK-MIB", "sleClockSelectionModeChanged"),
        ("SLE-CLOCK-MIB", "sleClockBitsTypeChanged"),
        ("SLE-CLOCK-MIB", "sleClockBitsLineEncodingChanged"),
        ("SLE-CLOCK-MIB", "sleClockQlSetQualityLevelChanged"),
        ("SLE-CLOCK-MIB", "sleClockSwitchManChanged"),
        ("SLE-CLOCK-MIB", "sleClockInputSourcePriorityChanged"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceIfNameChanged"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceUseOnChanged"),
        ("SLE-CLOCK-MIB", "sleClockInputSourceUseOffChanged"),
        ("SLE-CLOCK-MIB", "sleClockSwitchClearChanged"))
)
if mibBuilder.loadTexts:
    sleClockNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-CLOCK-MIB",
    **{"ClockSourceAll": ClockSourceAll,
       "ClockQualityLevel": ClockQualityLevel,
       "ClockSourceSystem": ClockSourceSystem,
       "ClockQualityLevelValid": ClockQualityLevelValid,
       "sleClock": sleClock,
       "sleClockBaseMode": sleClockBaseMode,
       "sleClockBaseModeInfo": sleClockBaseModeInfo,
       "sleClockSyncOption": sleClockSyncOption,
       "sleClockSelectionMode": sleClockSelectionMode,
       "sleClockBaseModeControl": sleClockBaseModeControl,
       "sleClockModeControlRequest": sleClockModeControlRequest,
       "sleClockModeControlStatus": sleClockModeControlStatus,
       "sleClockModeControlTimer": sleClockModeControlTimer,
       "sleClockModeControlTimeStamp": sleClockModeControlTimeStamp,
       "sleClockModeControlReqResult": sleClockModeControlReqResult,
       "sleClockModeControlSyncOption": sleClockModeControlSyncOption,
       "sleClockModeControlSelectionMode": sleClockModeControlSelectionMode,
       "sleClockBaseModeNotification": sleClockBaseModeNotification,
       "sleClockSyncOptionChanged": sleClockSyncOptionChanged,
       "sleClockSelectionModeChanged": sleClockSelectionModeChanged,
       "sleClockBits": sleClockBits,
       "sleClockBitsInfo": sleClockBitsInfo,
       "sleClockBitsType": sleClockBitsType,
       "sleClockBitsFrameMode": sleClockBitsFrameMode,
       "sleClockBitsLineEncoding": sleClockBitsLineEncoding,
       "sleClockBitsControl": sleClockBitsControl,
       "sleClockBitsControlRequest": sleClockBitsControlRequest,
       "sleClockBitsControlStatus": sleClockBitsControlStatus,
       "sleClockBitsControlTimer": sleClockBitsControlTimer,
       "sleClockBitsControlTimeStamp": sleClockBitsControlTimeStamp,
       "sleClockBitsControlReqResult": sleClockBitsControlReqResult,
       "sleClockBitsControlType": sleClockBitsControlType,
       "sleClockBitsControlFrameMode": sleClockBitsControlFrameMode,
       "sleClockBitsControlLineEncoding": sleClockBitsControlLineEncoding,
       "sleClockBitsNotification": sleClockBitsNotification,
       "sleClockBitsTypeChanged": sleClockBitsTypeChanged,
       "sleClockBitsLineEncodingChanged": sleClockBitsLineEncodingChanged,
       "sleClockQlSet": sleClockQlSet,
       "sleClockQlSetTable": sleClockQlSetTable,
       "sleClockQlSetEntry": sleClockQlSetEntry,
       "sleClockQlSetSource": sleClockQlSetSource,
       "sleClockQlSetQulatyLevel": sleClockQlSetQulatyLevel,
       "sleClockQlSetControl": sleClockQlSetControl,
       "sleClockQlSetControlRequest": sleClockQlSetControlRequest,
       "sleClockQlSetControlStatus": sleClockQlSetControlStatus,
       "sleClockQlSetControlTimer": sleClockQlSetControlTimer,
       "sleClockQlSetControlTimeStamp": sleClockQlSetControlTimeStamp,
       "sleClockQlSetControlReqResult": sleClockQlSetControlReqResult,
       "sleClockQlSetControlSoruce": sleClockQlSetControlSoruce,
       "sleClockQlSetControlQualityLevel": sleClockQlSetControlQualityLevel,
       "sleClockQlNotification": sleClockQlNotification,
       "sleClockQlSetQualityLevelChanged": sleClockQlSetQualityLevelChanged,
       "sleClockSelected": sleClockSelected,
       "sleClockSelectedInfo": sleClockSelectedInfo,
       "sleClockSelectedSource": sleClockSelectedSource,
       "sleClockSelectedState": sleClockSelectedState,
       "sleClockSelectedQualityLevel": sleClockSelectedQualityLevel,
       "sleClockSelectedSwitchType": sleClockSelectedSwitchType,
       "sleClockSelectedControl": sleClockSelectedControl,
       "sleClockSelectedControlRequest": sleClockSelectedControlRequest,
       "sleClockSelectedControlStatus": sleClockSelectedControlStatus,
       "sleClockSelectedControlTimer": sleClockSelectedControlTimer,
       "sleClockSelectedControlTimeStamp": sleClockSelectedControlTimeStamp,
       "sleClockSelectedControlReqResult": sleClockSelectedControlReqResult,
       "sleClockSelectedControlDestSource": sleClockSelectedControlDestSource,
       "sleClockSelectedNotification": sleClockSelectedNotification,
       "sleClockSwitchManChanged": sleClockSwitchManChanged,
       "sleClockSwitchClearChanged": sleClockSwitchClearChanged,
       "sleClockInputSource": sleClockInputSource,
       "sleClockInputSourceTable": sleClockInputSourceTable,
       "sleClockInputSourceEntry": sleClockInputSourceEntry,
       "sleClockInputSourceSource": sleClockInputSourceSource,
       "sleClockInputSourceUse": sleClockInputSourceUse,
       "sleClockInputSourcePriority": sleClockInputSourcePriority,
       "sleClockInputSourceIfName": sleClockInputSourceIfName,
       "sleClockInputSourceConfQulatyLevel": sleClockInputSourceConfQulatyLevel,
       "sleClockInputSourceRecvQulatyLevel": sleClockInputSourceRecvQulatyLevel,
       "sleClockInputSourceValid": sleClockInputSourceValid,
       "sleClockInputSourceControl": sleClockInputSourceControl,
       "sleClockInputSourceControlRequest": sleClockInputSourceControlRequest,
       "sleClockInputSourceControlStatus": sleClockInputSourceControlStatus,
       "sleClockInputSourceControlTimer": sleClockInputSourceControlTimer,
       "sleClockInputSourceControlTimeStamp": sleClockInputSourceControlTimeStamp,
       "sleClockInputSourceControlReqResult": sleClockInputSourceControlReqResult,
       "sleClockInputSourceControlSource": sleClockInputSourceControlSource,
       "sleClockInputSourceControlPriority": sleClockInputSourceControlPriority,
       "sleClockInputSourceControlIfName": sleClockInputSourceControlIfName,
       "sleClockInputSourceNotification": sleClockInputSourceNotification,
       "sleClockInputSourceUseOnChanged": sleClockInputSourceUseOnChanged,
       "sleClockInputSourceUseOffChanged": sleClockInputSourceUseOffChanged,
       "sleClockInputSourcePriorityChanged": sleClockInputSourcePriorityChanged,
       "sleClockInputSourceIfNameChanged": sleClockInputSourceIfNameChanged,
       "sleClockObjectGroup": sleClockObjectGroup,
       "sleClockNotificationGroup": sleClockNotificationGroup}
)
