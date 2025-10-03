# SNMP MIB module (SLE-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:57 2025
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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

slePmMgr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94)
)
if mibBuilder.loadTexts:
    slePmMgr.setRevisions(
        ("2015-11-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmClassId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class PmId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class PmSrc(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(68, 68),
    )
    fixed_length = 68



class PmTcaState(TextualConvention, Integer32):
    status = "current"
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



class PmDateTime(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs



class _SlePmNeId_Type(OctetString):
    """Custom type slePmNeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SlePmNeId_Type.__name__ = "OctetString"
_SlePmNeId_Object = MibScalar
slePmNeId = _SlePmNeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 1),
    _SlePmNeId_Type()
)
slePmNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmNeId.setStatus("current")
_SlePmConfigBase_ObjectIdentity = ObjectIdentity
slePmConfigBase = _SlePmConfigBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2)
)
_SlePmConfigTable_Object = MibTable
slePmConfigTable = _SlePmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1)
)
if mibBuilder.loadTexts:
    slePmConfigTable.setStatus("current")
_SlePmConfigEntry_Object = MibTableRow
slePmConfigEntry = _SlePmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1)
)
slePmConfigEntry.setIndexNames(
    (0, "SLE-PM-MIB", "slePmConfigSeqId"),
)
if mibBuilder.loadTexts:
    slePmConfigEntry.setStatus("current")


class _SlePmConfigSeqId_Type(Integer32):
    """Custom type slePmConfigSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlePmConfigSeqId_Type.__name__ = "Integer32"
_SlePmConfigSeqId_Object = MibTableColumn
slePmConfigSeqId = _SlePmConfigSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 1),
    _SlePmConfigSeqId_Type()
)
slePmConfigSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigSeqId.setStatus("current")
_SlePmConfigClassId_Type = PmClassId
_SlePmConfigClassId_Object = MibTableColumn
slePmConfigClassId = _SlePmConfigClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 2),
    _SlePmConfigClassId_Type()
)
slePmConfigClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigClassId.setStatus("current")
_SlePmConfigPmId_Type = PmId
_SlePmConfigPmId_Object = MibTableColumn
slePmConfigPmId = _SlePmConfigPmId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 3),
    _SlePmConfigPmId_Type()
)
slePmConfigPmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigPmId.setStatus("current")
_SlePmConfigSource_Type = PmSrc
_SlePmConfigSource_Object = MibTableColumn
slePmConfigSource = _SlePmConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 4),
    _SlePmConfigSource_Type()
)
slePmConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigSource.setStatus("current")


class _SlePmConfigTcaStat_Type(Integer32):
    """Custom type slePmConfigTcaStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcaNormal", 0),
          ("tcaOccur", 1))
    )


_SlePmConfigTcaStat_Type.__name__ = "Integer32"
_SlePmConfigTcaStat_Object = MibTableColumn
slePmConfigTcaStat = _SlePmConfigTcaStat_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 5),
    _SlePmConfigTcaStat_Type()
)
slePmConfigTcaStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigTcaStat.setStatus("current")
_SlePmConfigTcaEnable_Type = PmTcaState
_SlePmConfigTcaEnable_Object = MibTableColumn
slePmConfigTcaEnable = _SlePmConfigTcaEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 6),
    _SlePmConfigTcaEnable_Type()
)
slePmConfigTcaEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigTcaEnable.setStatus("current")
_SlePmConfigTh15Min_Type = Counter64
_SlePmConfigTh15Min_Object = MibTableColumn
slePmConfigTh15Min = _SlePmConfigTh15Min_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 7),
    _SlePmConfigTh15Min_Type()
)
slePmConfigTh15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigTh15Min.setStatus("current")
_SlePmConfigTh1Day_Type = Counter64
_SlePmConfigTh1Day_Object = MibTableColumn
slePmConfigTh1Day = _SlePmConfigTh1Day_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 1, 1, 8),
    _SlePmConfigTh1Day_Type()
)
slePmConfigTh1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmConfigTh1Day.setStatus("current")
_SlePmConfigControl_ObjectIdentity = ObjectIdentity
slePmConfigControl = _SlePmConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2)
)


class _SlePmConfigControlRequest_Type(Integer32):
    """Custom type slePmConfigControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setPmConfigTcaEnable", 1),
          ("setPmConfigTh15Min", 2),
          ("setPmConfigTh1Day", 3))
    )


_SlePmConfigControlRequest_Type.__name__ = "Integer32"
_SlePmConfigControlRequest_Object = MibScalar
slePmConfigControlRequest = _SlePmConfigControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 1),
    _SlePmConfigControlRequest_Type()
)
slePmConfigControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmConfigControlRequest.setStatus("current")
_SlePmConfigControlStatus_Type = SleControlStatusType
_SlePmConfigControlStatus_Object = MibScalar
slePmConfigControlStatus = _SlePmConfigControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 2),
    _SlePmConfigControlStatus_Type()
)
slePmConfigControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigControlStatus.setStatus("current")
_SlePmConfigControlTimer_Type = Gauge32
_SlePmConfigControlTimer_Object = MibScalar
slePmConfigControlTimer = _SlePmConfigControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 3),
    _SlePmConfigControlTimer_Type()
)
slePmConfigControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmConfigControlTimer.setStatus("current")
_SlePmConfigControlTimeStamp_Type = TimeTicks
_SlePmConfigControlTimeStamp_Object = MibScalar
slePmConfigControlTimeStamp = _SlePmConfigControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 4),
    _SlePmConfigControlTimeStamp_Type()
)
slePmConfigControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigControlTimeStamp.setStatus("current")
_SlePmConfigControlReqResult_Type = SleControlRequestResultType
_SlePmConfigControlReqResult_Object = MibScalar
slePmConfigControlReqResult = _SlePmConfigControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 5),
    _SlePmConfigControlReqResult_Type()
)
slePmConfigControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmConfigControlReqResult.setStatus("current")
_SlePmConfigControlSeqId_Type = Integer32
_SlePmConfigControlSeqId_Object = MibScalar
slePmConfigControlSeqId = _SlePmConfigControlSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 6),
    _SlePmConfigControlSeqId_Type()
)
slePmConfigControlSeqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmConfigControlSeqId.setStatus("current")
_SlePmConfigControlTcaEnable_Type = PmTcaState
_SlePmConfigControlTcaEnable_Object = MibScalar
slePmConfigControlTcaEnable = _SlePmConfigControlTcaEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 7),
    _SlePmConfigControlTcaEnable_Type()
)
slePmConfigControlTcaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmConfigControlTcaEnable.setStatus("current")
_SlePmConfigControlTh15Min_Type = Counter64
_SlePmConfigControlTh15Min_Object = MibScalar
slePmConfigControlTh15Min = _SlePmConfigControlTh15Min_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 8),
    _SlePmConfigControlTh15Min_Type()
)
slePmConfigControlTh15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmConfigControlTh15Min.setStatus("current")
_SlePmConfigControlTh1Day_Type = Counter64
_SlePmConfigControlTh1Day_Object = MibScalar
slePmConfigControlTh1Day = _SlePmConfigControlTh1Day_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 2, 9),
    _SlePmConfigControlTh1Day_Type()
)
slePmConfigControlTh1Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmConfigControlTh1Day.setStatus("current")
_SlePmConfigNotification_ObjectIdentity = ObjectIdentity
slePmConfigNotification = _SlePmConfigNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 3)
)
_SlePmCurrentBase_ObjectIdentity = ObjectIdentity
slePmCurrentBase = _SlePmCurrentBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3)
)
_SlePmCurrentTable_Object = MibTable
slePmCurrentTable = _SlePmCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1)
)
if mibBuilder.loadTexts:
    slePmCurrentTable.setStatus("current")
_SlePmCurrentEntry_Object = MibTableRow
slePmCurrentEntry = _SlePmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1)
)
slePmCurrentEntry.setIndexNames(
    (0, "SLE-PM-MIB", "slePmCurrentSeqId"),
    (0, "SLE-PM-MIB", "slePmCurrentTerm"),
)
if mibBuilder.loadTexts:
    slePmCurrentEntry.setStatus("current")


class _SlePmCurrentSeqId_Type(Integer32):
    """Custom type slePmCurrentSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlePmCurrentSeqId_Type.__name__ = "Integer32"
_SlePmCurrentSeqId_Object = MibTableColumn
slePmCurrentSeqId = _SlePmCurrentSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 1),
    _SlePmCurrentSeqId_Type()
)
slePmCurrentSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentSeqId.setStatus("current")
_SlePmCurrentClassId_Type = PmClassId
_SlePmCurrentClassId_Object = MibTableColumn
slePmCurrentClassId = _SlePmCurrentClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 2),
    _SlePmCurrentClassId_Type()
)
slePmCurrentClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentClassId.setStatus("current")
_SlePmCurrentPmId_Type = PmId
_SlePmCurrentPmId_Object = MibTableColumn
slePmCurrentPmId = _SlePmCurrentPmId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 3),
    _SlePmCurrentPmId_Type()
)
slePmCurrentPmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentPmId.setStatus("current")
_SlePmCurrentSource_Type = PmSrc
_SlePmCurrentSource_Object = MibTableColumn
slePmCurrentSource = _SlePmCurrentSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 4),
    _SlePmCurrentSource_Type()
)
slePmCurrentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentSource.setStatus("current")


class _SlePmCurrentTerm_Type(Integer32):
    """Custom type slePmCurrentTerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("min15", 1),
          ("day1", 2))
    )


_SlePmCurrentTerm_Type.__name__ = "Integer32"
_SlePmCurrentTerm_Object = MibTableColumn
slePmCurrentTerm = _SlePmCurrentTerm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 5),
    _SlePmCurrentTerm_Type()
)
slePmCurrentTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmCurrentTerm.setStatus("current")
_SlePmCurrentPmCount_Type = Counter64
_SlePmCurrentPmCount_Object = MibTableColumn
slePmCurrentPmCount = _SlePmCurrentPmCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 6),
    _SlePmCurrentPmCount_Type()
)
slePmCurrentPmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentPmCount.setStatus("current")
_SlePmCurrentAccSecond_Type = Counter32
_SlePmCurrentAccSecond_Object = MibTableColumn
slePmCurrentAccSecond = _SlePmCurrentAccSecond_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 7),
    _SlePmCurrentAccSecond_Type()
)
slePmCurrentAccSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentAccSecond.setStatus("current")


class _SlePmCurrentTcaStat_Type(Integer32):
    """Custom type slePmCurrentTcaStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcaNormal", 0),
          ("tcaOccur", 1))
    )


_SlePmCurrentTcaStat_Type.__name__ = "Integer32"
_SlePmCurrentTcaStat_Object = MibTableColumn
slePmCurrentTcaStat = _SlePmCurrentTcaStat_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 8),
    _SlePmCurrentTcaStat_Type()
)
slePmCurrentTcaStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentTcaStat.setStatus("current")
_SlePmCurrentTcaTime_Type = TimeTicks
_SlePmCurrentTcaTime_Object = MibTableColumn
slePmCurrentTcaTime = _SlePmCurrentTcaTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 1, 1, 9),
    _SlePmCurrentTcaTime_Type()
)
slePmCurrentTcaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentTcaTime.setStatus("current")
_SlePmCurrentControl_ObjectIdentity = ObjectIdentity
slePmCurrentControl = _SlePmCurrentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 2)
)


class _SlePmCurrentControlRequest_Type(Integer32):
    """Custom type slePmCurrentControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCurrentPm", 1),
          ("clearCurrentTca", 2))
    )


_SlePmCurrentControlRequest_Type.__name__ = "Integer32"
_SlePmCurrentControlRequest_Object = MibScalar
slePmCurrentControlRequest = _SlePmCurrentControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 2, 1),
    _SlePmCurrentControlRequest_Type()
)
slePmCurrentControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmCurrentControlRequest.setStatus("current")
_SlePmCurrentControlStatus_Type = SleControlStatusType
_SlePmCurrentControlStatus_Object = MibScalar
slePmCurrentControlStatus = _SlePmCurrentControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 2, 2),
    _SlePmCurrentControlStatus_Type()
)
slePmCurrentControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentControlStatus.setStatus("current")
_SlePmCurrentControlTimer_Type = Gauge32
_SlePmCurrentControlTimer_Object = MibScalar
slePmCurrentControlTimer = _SlePmCurrentControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 2, 3),
    _SlePmCurrentControlTimer_Type()
)
slePmCurrentControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmCurrentControlTimer.setStatus("current")
_SlePmCurrentControlTimeStamp_Type = TimeTicks
_SlePmCurrentControlTimeStamp_Object = MibScalar
slePmCurrentControlTimeStamp = _SlePmCurrentControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 2, 4),
    _SlePmCurrentControlTimeStamp_Type()
)
slePmCurrentControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentControlTimeStamp.setStatus("current")
_SlePmCurrentControlReqResult_Type = SleControlRequestResultType
_SlePmCurrentControlReqResult_Object = MibScalar
slePmCurrentControlReqResult = _SlePmCurrentControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 2, 5),
    _SlePmCurrentControlReqResult_Type()
)
slePmCurrentControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmCurrentControlReqResult.setStatus("current")
_SlePmCurrentNotification_ObjectIdentity = ObjectIdentity
slePmCurrentNotification = _SlePmCurrentNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 3)
)
_SlePMHistoryBase_ObjectIdentity = ObjectIdentity
slePMHistoryBase = _SlePMHistoryBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4)
)
_SlePmHistoryTable_Object = MibTable
slePmHistoryTable = _SlePmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1)
)
if mibBuilder.loadTexts:
    slePmHistoryTable.setStatus("current")
_SlePmHistoryEntry_Object = MibTableRow
slePmHistoryEntry = _SlePmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1)
)
slePmHistoryEntry.setIndexNames(
    (0, "SLE-PM-MIB", "slePmHistorySeqId"),
    (0, "SLE-PM-MIB", "slePmHistoryTerm"),
    (0, "SLE-PM-MIB", "slePmHistoryIndex"),
)
if mibBuilder.loadTexts:
    slePmHistoryEntry.setStatus("current")


class _SlePmHistorySeqId_Type(Integer32):
    """Custom type slePmHistorySeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlePmHistorySeqId_Type.__name__ = "Integer32"
_SlePmHistorySeqId_Object = MibTableColumn
slePmHistorySeqId = _SlePmHistorySeqId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 1),
    _SlePmHistorySeqId_Type()
)
slePmHistorySeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistorySeqId.setStatus("current")
_SlePmHistoryClassId_Type = PmClassId
_SlePmHistoryClassId_Object = MibTableColumn
slePmHistoryClassId = _SlePmHistoryClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 2),
    _SlePmHistoryClassId_Type()
)
slePmHistoryClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryClassId.setStatus("current")
_SlePmHistoryPmId_Type = PmId
_SlePmHistoryPmId_Object = MibTableColumn
slePmHistoryPmId = _SlePmHistoryPmId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 3),
    _SlePmHistoryPmId_Type()
)
slePmHistoryPmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryPmId.setStatus("current")
_SlePmHistoryPmSource_Type = PmSrc
_SlePmHistoryPmSource_Object = MibTableColumn
slePmHistoryPmSource = _SlePmHistoryPmSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 4),
    _SlePmHistoryPmSource_Type()
)
slePmHistoryPmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryPmSource.setStatus("current")


class _SlePmHistoryTerm_Type(Integer32):
    """Custom type slePmHistoryTerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("min15", 1),
          ("day1", 2))
    )


_SlePmHistoryTerm_Type.__name__ = "Integer32"
_SlePmHistoryTerm_Object = MibTableColumn
slePmHistoryTerm = _SlePmHistoryTerm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 5),
    _SlePmHistoryTerm_Type()
)
slePmHistoryTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryTerm.setStatus("current")


class _SlePmHistoryIndex_Type(Integer32):
    """Custom type slePmHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SlePmHistoryIndex_Type.__name__ = "Integer32"
_SlePmHistoryIndex_Object = MibTableColumn
slePmHistoryIndex = _SlePmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 6),
    _SlePmHistoryIndex_Type()
)
slePmHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryIndex.setStatus("current")
_SlePmHistoryPmCount_Type = Counter64
_SlePmHistoryPmCount_Object = MibTableColumn
slePmHistoryPmCount = _SlePmHistoryPmCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 7),
    _SlePmHistoryPmCount_Type()
)
slePmHistoryPmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryPmCount.setStatus("current")
_SlePmHistoryAccCount_Type = Counter32
_SlePmHistoryAccCount_Object = MibTableColumn
slePmHistoryAccCount = _SlePmHistoryAccCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 8),
    _SlePmHistoryAccCount_Type()
)
slePmHistoryAccCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmHistoryAccCount.setStatus("current")
_SlePmHistoryStartTime_Type = TimeTicks
_SlePmHistoryStartTime_Object = MibTableColumn
slePmHistoryStartTime = _SlePmHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 1, 1, 9),
    _SlePmHistoryStartTime_Type()
)
slePmHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryStartTime.setStatus("current")
_SlePmHistoryControl_ObjectIdentity = ObjectIdentity
slePmHistoryControl = _SlePmHistoryControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 2)
)


class _SlePmHistoryControlRequest_Type(Integer32):
    """Custom type slePmHistoryControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearPmHistory", 1)
    )


_SlePmHistoryControlRequest_Type.__name__ = "Integer32"
_SlePmHistoryControlRequest_Object = MibScalar
slePmHistoryControlRequest = _SlePmHistoryControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 2, 1),
    _SlePmHistoryControlRequest_Type()
)
slePmHistoryControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmHistoryControlRequest.setStatus("current")
_SlePmHistoryControlStatus_Type = SleControlStatusType
_SlePmHistoryControlStatus_Object = MibScalar
slePmHistoryControlStatus = _SlePmHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 2, 2),
    _SlePmHistoryControlStatus_Type()
)
slePmHistoryControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryControlStatus.setStatus("current")
_SlePmHistoryControlTimer_Type = Gauge32
_SlePmHistoryControlTimer_Object = MibScalar
slePmHistoryControlTimer = _SlePmHistoryControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 2, 3),
    _SlePmHistoryControlTimer_Type()
)
slePmHistoryControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePmHistoryControlTimer.setStatus("current")
_SlePmHistoryControlTimeStamp_Type = TimeTicks
_SlePmHistoryControlTimeStamp_Object = MibScalar
slePmHistoryControlTimeStamp = _SlePmHistoryControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 2, 4),
    _SlePmHistoryControlTimeStamp_Type()
)
slePmHistoryControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryControlTimeStamp.setStatus("current")
_SlePmHistoryControlReqResult_Type = SleControlRequestResultType
_SlePmHistoryControlReqResult_Object = MibScalar
slePmHistoryControlReqResult = _SlePmHistoryControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 2, 5),
    _SlePmHistoryControlReqResult_Type()
)
slePmHistoryControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePmHistoryControlReqResult.setStatus("current")
_SlePmHistoryNotification_ObjectIdentity = ObjectIdentity
slePmHistoryNotification = _SlePmHistoryNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 3)
)

# Managed Objects groups


# Notification objects

slePmConfigTcaEnableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 3, 1)
)
slePmConfigTcaEnableChanged.setObjects(
      *(("SLE-PM-MIB", "slePmNeId"),
        ("SLE-PM-MIB", "slePmConfigControlRequest"),
        ("SLE-PM-MIB", "slePmConfigControlTimeStamp"),
        ("SLE-PM-MIB", "slePmConfigControlReqResult"),
        ("SLE-PM-MIB", "slePmConfigControlSeqId"),
        ("SLE-PM-MIB", "slePmConfigControlTcaEnable"))
)
if mibBuilder.loadTexts:
    slePmConfigTcaEnableChanged.setStatus(
        "current"
    )

slePmConfigTh15MinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 3, 2)
)
slePmConfigTh15MinChanged.setObjects(
      *(("SLE-PM-MIB", "slePmNeId"),
        ("SLE-PM-MIB", "slePmConfigControlRequest"),
        ("SLE-PM-MIB", "slePmConfigControlTimeStamp"),
        ("SLE-PM-MIB", "slePmConfigControlReqResult"),
        ("SLE-PM-MIB", "slePmConfigControlSeqId"),
        ("SLE-PM-MIB", "slePmConfigControlTh15Min"))
)
if mibBuilder.loadTexts:
    slePmConfigTh15MinChanged.setStatus(
        "current"
    )

slePmConfigTh1DayChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 2, 3, 3)
)
slePmConfigTh1DayChanged.setObjects(
      *(("SLE-PM-MIB", "slePmNeId"),
        ("SLE-PM-MIB", "slePmConfigControlRequest"),
        ("SLE-PM-MIB", "slePmConfigControlTimeStamp"),
        ("SLE-PM-MIB", "slePmConfigControlReqResult"),
        ("SLE-PM-MIB", "slePmConfigControlSeqId"),
        ("SLE-PM-MIB", "slePmConfigControlTh1Day"))
)
if mibBuilder.loadTexts:
    slePmConfigTh1DayChanged.setStatus(
        "current"
    )

slePmCurrentPmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 3, 3, 1)
)
slePmCurrentPmCleared.setObjects(
      *(("SLE-PM-MIB", "slePmNeId"),
        ("SLE-PM-MIB", "slePmCurrentControlRequest"),
        ("SLE-PM-MIB", "slePmCurrentControlTimeStamp"),
        ("SLE-PM-MIB", "slePmCurrentControlReqResult"))
)
if mibBuilder.loadTexts:
    slePmCurrentPmCleared.setStatus(
        "current"
    )

slePmHistoryPmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 94, 4, 3, 1)
)
slePmHistoryPmCleared.setObjects(
      *(("SLE-PM-MIB", "slePmNeId"),
        ("SLE-PM-MIB", "slePmHistoryControlRequest"),
        ("SLE-PM-MIB", "slePmHistoryControlTimeStamp"),
        ("SLE-PM-MIB", "slePmHistoryControlReqResult"))
)
if mibBuilder.loadTexts:
    slePmHistoryPmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-PM-MIB",
    **{"PmClassId": PmClassId,
       "PmId": PmId,
       "PmSrc": PmSrc,
       "PmTcaState": PmTcaState,
       "PmDateTime": PmDateTime,
       "slePmMgr": slePmMgr,
       "slePmNeId": slePmNeId,
       "slePmConfigBase": slePmConfigBase,
       "slePmConfigTable": slePmConfigTable,
       "slePmConfigEntry": slePmConfigEntry,
       "slePmConfigSeqId": slePmConfigSeqId,
       "slePmConfigClassId": slePmConfigClassId,
       "slePmConfigPmId": slePmConfigPmId,
       "slePmConfigSource": slePmConfigSource,
       "slePmConfigTcaStat": slePmConfigTcaStat,
       "slePmConfigTcaEnable": slePmConfigTcaEnable,
       "slePmConfigTh15Min": slePmConfigTh15Min,
       "slePmConfigTh1Day": slePmConfigTh1Day,
       "slePmConfigControl": slePmConfigControl,
       "slePmConfigControlRequest": slePmConfigControlRequest,
       "slePmConfigControlStatus": slePmConfigControlStatus,
       "slePmConfigControlTimer": slePmConfigControlTimer,
       "slePmConfigControlTimeStamp": slePmConfigControlTimeStamp,
       "slePmConfigControlReqResult": slePmConfigControlReqResult,
       "slePmConfigControlSeqId": slePmConfigControlSeqId,
       "slePmConfigControlTcaEnable": slePmConfigControlTcaEnable,
       "slePmConfigControlTh15Min": slePmConfigControlTh15Min,
       "slePmConfigControlTh1Day": slePmConfigControlTh1Day,
       "slePmConfigNotification": slePmConfigNotification,
       "slePmConfigTcaEnableChanged": slePmConfigTcaEnableChanged,
       "slePmConfigTh15MinChanged": slePmConfigTh15MinChanged,
       "slePmConfigTh1DayChanged": slePmConfigTh1DayChanged,
       "slePmCurrentBase": slePmCurrentBase,
       "slePmCurrentTable": slePmCurrentTable,
       "slePmCurrentEntry": slePmCurrentEntry,
       "slePmCurrentSeqId": slePmCurrentSeqId,
       "slePmCurrentClassId": slePmCurrentClassId,
       "slePmCurrentPmId": slePmCurrentPmId,
       "slePmCurrentSource": slePmCurrentSource,
       "slePmCurrentTerm": slePmCurrentTerm,
       "slePmCurrentPmCount": slePmCurrentPmCount,
       "slePmCurrentAccSecond": slePmCurrentAccSecond,
       "slePmCurrentTcaStat": slePmCurrentTcaStat,
       "slePmCurrentTcaTime": slePmCurrentTcaTime,
       "slePmCurrentControl": slePmCurrentControl,
       "slePmCurrentControlRequest": slePmCurrentControlRequest,
       "slePmCurrentControlStatus": slePmCurrentControlStatus,
       "slePmCurrentControlTimer": slePmCurrentControlTimer,
       "slePmCurrentControlTimeStamp": slePmCurrentControlTimeStamp,
       "slePmCurrentControlReqResult": slePmCurrentControlReqResult,
       "slePmCurrentNotification": slePmCurrentNotification,
       "slePmCurrentPmCleared": slePmCurrentPmCleared,
       "slePMHistoryBase": slePMHistoryBase,
       "slePmHistoryTable": slePmHistoryTable,
       "slePmHistoryEntry": slePmHistoryEntry,
       "slePmHistorySeqId": slePmHistorySeqId,
       "slePmHistoryClassId": slePmHistoryClassId,
       "slePmHistoryPmId": slePmHistoryPmId,
       "slePmHistoryPmSource": slePmHistoryPmSource,
       "slePmHistoryTerm": slePmHistoryTerm,
       "slePmHistoryIndex": slePmHistoryIndex,
       "slePmHistoryPmCount": slePmHistoryPmCount,
       "slePmHistoryAccCount": slePmHistoryAccCount,
       "slePmHistoryStartTime": slePmHistoryStartTime,
       "slePmHistoryControl": slePmHistoryControl,
       "slePmHistoryControlRequest": slePmHistoryControlRequest,
       "slePmHistoryControlStatus": slePmHistoryControlStatus,
       "slePmHistoryControlTimer": slePmHistoryControlTimer,
       "slePmHistoryControlTimeStamp": slePmHistoryControlTimeStamp,
       "slePmHistoryControlReqResult": slePmHistoryControlReqResult,
       "slePmHistoryNotification": slePmHistoryNotification,
       "slePmHistoryPmCleared": slePmHistoryPmCleared}
)
