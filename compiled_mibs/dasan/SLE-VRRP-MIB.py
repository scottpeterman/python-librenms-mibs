# SNMP MIB module (SLE-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-VRRP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:08 2025
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

sleVRRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57)
)
if mibBuilder.loadTexts:
    sleVRRP.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleVrrpBase_ObjectIdentity = ObjectIdentity
sleVrrpBase = _SleVrrpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1)
)
_SleVrrpBaseInfo_ObjectIdentity = ObjectIdentity
sleVrrpBaseInfo = _SleVrrpBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 1)
)


class _SleVrrpBaseInfoCompatibleV2_Type(Integer32):
    """Custom type sleVrrpBaseInfoCompatibleV2 based on Integer32"""
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


_SleVrrpBaseInfoCompatibleV2_Type.__name__ = "Integer32"
_SleVrrpBaseInfoCompatibleV2_Object = MibScalar
sleVrrpBaseInfoCompatibleV2 = _SleVrrpBaseInfoCompatibleV2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 1, 1),
    _SleVrrpBaseInfoCompatibleV2_Type()
)
sleVrrpBaseInfoCompatibleV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrpBaseInfoCompatibleV2.setStatus("current")


class _SleVrrpBaseInfoVMac_Type(Integer32):
    """Custom type sleVrrpBaseInfoVMac based on Integer32"""
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


_SleVrrpBaseInfoVMac_Type.__name__ = "Integer32"
_SleVrrpBaseInfoVMac_Object = MibScalar
sleVrrpBaseInfoVMac = _SleVrrpBaseInfoVMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 1, 2),
    _SleVrrpBaseInfoVMac_Type()
)
sleVrrpBaseInfoVMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrpBaseInfoVMac.setStatus("current")


class _SleVrrpBaseInfoDelegate_Type(Integer32):
    """Custom type sleVrrpBaseInfoDelegate based on Integer32"""
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


_SleVrrpBaseInfoDelegate_Type.__name__ = "Integer32"
_SleVrrpBaseInfoDelegate_Object = MibScalar
sleVrrpBaseInfoDelegate = _SleVrrpBaseInfoDelegate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 1, 3),
    _SleVrrpBaseInfoDelegate_Type()
)
sleVrrpBaseInfoDelegate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrpBaseInfoDelegate.setStatus("current")
_SleVrrpBaseControl_ObjectIdentity = ObjectIdentity
sleVrrpBaseControl = _SleVrrpBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2)
)


class _SleVrrpBaseControlRequest_Type(Integer32):
    """Custom type sleVrrpBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setVrrpBaseCompatibleV2", 1),
          ("setVrrpBaseVmacStatus", 2),
          ("setVrrpBaseDelegate", 3))
    )


_SleVrrpBaseControlRequest_Type.__name__ = "Integer32"
_SleVrrpBaseControlRequest_Object = MibScalar
sleVrrpBaseControlRequest = _SleVrrpBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 1),
    _SleVrrpBaseControlRequest_Type()
)
sleVrrpBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrpBaseControlRequest.setStatus("current")
_SleVrrpBaseControlStatus_Type = SleControlStatusType
_SleVrrpBaseControlStatus_Object = MibScalar
sleVrrpBaseControlStatus = _SleVrrpBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 2),
    _SleVrrpBaseControlStatus_Type()
)
sleVrrpBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrpBaseControlStatus.setStatus("current")
_SleVrrpBaseControlTimer_Type = Gauge32
_SleVrrpBaseControlTimer_Object = MibScalar
sleVrrpBaseControlTimer = _SleVrrpBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 3),
    _SleVrrpBaseControlTimer_Type()
)
sleVrrpBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrpBaseControlTimer.setStatus("current")
_SleVrrpBaseControlTimeStamp_Type = TimeTicks
_SleVrrpBaseControlTimeStamp_Object = MibScalar
sleVrrpBaseControlTimeStamp = _SleVrrpBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 4),
    _SleVrrpBaseControlTimeStamp_Type()
)
sleVrrpBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrpBaseControlTimeStamp.setStatus("current")
_SleVrrpBaseControlReqResult_Type = SleControlRequestResultType
_SleVrrpBaseControlReqResult_Object = MibScalar
sleVrrpBaseControlReqResult = _SleVrrpBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 5),
    _SleVrrpBaseControlReqResult_Type()
)
sleVrrpBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrpBaseControlReqResult.setStatus("current")


class _SleVrrpBaseControlCompatibleV2_Type(Integer32):
    """Custom type sleVrrpBaseControlCompatibleV2 based on Integer32"""
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


_SleVrrpBaseControlCompatibleV2_Type.__name__ = "Integer32"
_SleVrrpBaseControlCompatibleV2_Object = MibScalar
sleVrrpBaseControlCompatibleV2 = _SleVrrpBaseControlCompatibleV2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 6),
    _SleVrrpBaseControlCompatibleV2_Type()
)
sleVrrpBaseControlCompatibleV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrpBaseControlCompatibleV2.setStatus("current")


class _SleVrrpBaseControlVMac_Type(Integer32):
    """Custom type sleVrrpBaseControlVMac based on Integer32"""
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


_SleVrrpBaseControlVMac_Type.__name__ = "Integer32"
_SleVrrpBaseControlVMac_Object = MibScalar
sleVrrpBaseControlVMac = _SleVrrpBaseControlVMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 7),
    _SleVrrpBaseControlVMac_Type()
)
sleVrrpBaseControlVMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrpBaseControlVMac.setStatus("current")


class _SleVrrpBaseControlDelegate_Type(Integer32):
    """Custom type sleVrrpBaseControlDelegate based on Integer32"""
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


_SleVrrpBaseControlDelegate_Type.__name__ = "Integer32"
_SleVrrpBaseControlDelegate_Object = MibScalar
sleVrrpBaseControlDelegate = _SleVrrpBaseControlDelegate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 1, 2, 8),
    _SleVrrpBaseControlDelegate_Type()
)
sleVrrpBaseControlDelegate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrpBaseControlDelegate.setStatus("current")
_SleVrrpSess_ObjectIdentity = ObjectIdentity
sleVrrpSess = _SleVrrpSess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2)
)
_SleVrrp4Session_ObjectIdentity = ObjectIdentity
sleVrrp4Session = _SleVrrp4Session_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1)
)
_SleVrrp4SessionTable_Object = MibTable
sleVrrp4SessionTable = _SleVrrp4SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleVrrp4SessionTable.setStatus("current")
_SleVrrp4SessionEntry_Object = MibTableRow
sleVrrp4SessionEntry = _SleVrrp4SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1)
)
sleVrrp4SessionEntry.setIndexNames(
    (0, "SLE-VRRP-MIB", "sleVrrp4SessionVrId"),
    (0, "SLE-VRRP-MIB", "sleVrrp4SessionIfIndex"),
)
if mibBuilder.loadTexts:
    sleVrrp4SessionEntry.setStatus("current")


class _SleVrrp4SessionVrId_Type(Integer32):
    """Custom type sleVrrp4SessionVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessionVrId_Type.__name__ = "Integer32"
_SleVrrp4SessionVrId_Object = MibTableColumn
sleVrrp4SessionVrId = _SleVrrp4SessionVrId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 1),
    _SleVrrp4SessionVrId_Type()
)
sleVrrp4SessionVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionVrId.setStatus("current")


class _SleVrrp4SessionIfIndex_Type(Integer32):
    """Custom type sleVrrp4SessionIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessionIfIndex_Type.__name__ = "Integer32"
_SleVrrp4SessionIfIndex_Object = MibTableColumn
sleVrrp4SessionIfIndex = _SleVrrp4SessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 2),
    _SleVrrp4SessionIfIndex_Type()
)
sleVrrp4SessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionIfIndex.setStatus("current")


class _SleVrrp4SessionStatus_Type(Integer32):
    """Custom type sleVrrp4SessionStatus based on Integer32"""
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


_SleVrrp4SessionStatus_Type.__name__ = "Integer32"
_SleVrrp4SessionStatus_Object = MibTableColumn
sleVrrp4SessionStatus = _SleVrrp4SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 3),
    _SleVrrp4SessionStatus_Type()
)
sleVrrp4SessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionStatus.setStatus("current")


class _SleVrrp4SessionAcceptMode_Type(Integer32):
    """Custom type sleVrrp4SessionAcceptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SleVrrp4SessionAcceptMode_Type.__name__ = "Integer32"
_SleVrrp4SessionAcceptMode_Object = MibTableColumn
sleVrrp4SessionAcceptMode = _SleVrrp4SessionAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 4),
    _SleVrrp4SessionAcceptMode_Type()
)
sleVrrp4SessionAcceptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionAcceptMode.setStatus("current")


class _SleVrrp4SessionAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp4SessionAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000),
    )


_SleVrrp4SessionAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp4SessionAdvertisementInterval_Object = MibTableColumn
sleVrrp4SessionAdvertisementInterval = _SleVrrp4SessionAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 5),
    _SleVrrp4SessionAdvertisementInterval_Type()
)
sleVrrp4SessionAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionAdvertisementInterval.setStatus("current")
_SleVrrp4SessionCircuitFailOverIfIndex_Type = Integer32
_SleVrrp4SessionCircuitFailOverIfIndex_Object = MibTableColumn
sleVrrp4SessionCircuitFailOverIfIndex = _SleVrrp4SessionCircuitFailOverIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 6),
    _SleVrrp4SessionCircuitFailOverIfIndex_Type()
)
sleVrrp4SessionCircuitFailOverIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionCircuitFailOverIfIndex.setStatus("current")


class _SleVrrp4SessionCircuitFailOverPriorityDelta_Type(Integer32):
    """Custom type sleVrrp4SessionCircuitFailOverPriorityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 253),
    )


_SleVrrp4SessionCircuitFailOverPriorityDelta_Type.__name__ = "Integer32"
_SleVrrp4SessionCircuitFailOverPriorityDelta_Object = MibTableColumn
sleVrrp4SessionCircuitFailOverPriorityDelta = _SleVrrp4SessionCircuitFailOverPriorityDelta_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 7),
    _SleVrrp4SessionCircuitFailOverPriorityDelta_Type()
)
sleVrrp4SessionCircuitFailOverPriorityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionCircuitFailOverPriorityDelta.setStatus("current")


class _SleVrrp4SessionPreemptMode_Type(Integer32):
    """Custom type sleVrrp4SessionPreemptMode based on Integer32"""
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


_SleVrrp4SessionPreemptMode_Type.__name__ = "Integer32"
_SleVrrp4SessionPreemptMode_Object = MibTableColumn
sleVrrp4SessionPreemptMode = _SleVrrp4SessionPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 8),
    _SleVrrp4SessionPreemptMode_Type()
)
sleVrrp4SessionPreemptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionPreemptMode.setStatus("current")


class _SleVrrp4SessionPriority_Type(Integer32):
    """Custom type sleVrrp4SessionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessionPriority_Type.__name__ = "Integer32"
_SleVrrp4SessionPriority_Object = MibTableColumn
sleVrrp4SessionPriority = _SleVrrp4SessionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 9),
    _SleVrrp4SessionPriority_Type()
)
sleVrrp4SessionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionPriority.setStatus("current")


class _SleVrrp4SessionSwitchBackDelay_Type(Integer32):
    """Custom type sleVrrp4SessionSwitchBackDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 500000),
    )


_SleVrrp4SessionSwitchBackDelay_Type.__name__ = "Integer32"
_SleVrrp4SessionSwitchBackDelay_Object = MibTableColumn
sleVrrp4SessionSwitchBackDelay = _SleVrrp4SessionSwitchBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 10),
    _SleVrrp4SessionSwitchBackDelay_Type()
)
sleVrrp4SessionSwitchBackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionSwitchBackDelay.setStatus("current")
_SleVrrp4SessionVirtualIpVal_Type = OctetString
_SleVrrp4SessionVirtualIpVal_Object = MibTableColumn
sleVrrp4SessionVirtualIpVal = _SleVrrp4SessionVirtualIpVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 11),
    _SleVrrp4SessionVirtualIpVal_Type()
)
sleVrrp4SessionVirtualIpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionVirtualIpVal.setStatus("current")


class _SleVrrp4SessionVirtualIpOwner_Type(Integer32):
    """Custom type sleVrrp4SessionVirtualIpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unSet", 0),
          ("set", 1))
    )


_SleVrrp4SessionVirtualIpOwner_Type.__name__ = "Integer32"
_SleVrrp4SessionVirtualIpOwner_Object = MibTableColumn
sleVrrp4SessionVirtualIpOwner = _SleVrrp4SessionVirtualIpOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 12),
    _SleVrrp4SessionVirtualIpOwner_Type()
)
sleVrrp4SessionVirtualIpOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionVirtualIpOwner.setStatus("current")


class _SleVrrp4SessionCompatibleV2_Type(Integer32):
    """Custom type sleVrrp4SessionCompatibleV2 based on Integer32"""
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


_SleVrrp4SessionCompatibleV2_Type.__name__ = "Integer32"
_SleVrrp4SessionCompatibleV2_Object = MibTableColumn
sleVrrp4SessionCompatibleV2 = _SleVrrp4SessionCompatibleV2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 1, 1, 13),
    _SleVrrp4SessionCompatibleV2_Type()
)
sleVrrp4SessionCompatibleV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionCompatibleV2.setStatus("current")
_SleVrrp4SessionControl_ObjectIdentity = ObjectIdentity
sleVrrp4SessionControl = _SleVrrp4SessionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2)
)


class _SleVrrp4SessionControlRequest_Type(Integer32):
    """Custom type sleVrrp4SessionControlRequest based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("createVrrp4Sess", 1),
          ("delVrrp4Sess", 2),
          ("setVrrp4SessStatus", 3),
          ("setVrrp4SessAcceptMode", 4),
          ("setVrrp4SessAdvInterval", 5),
          ("delVrrp4SessAdvInterval", 6),
          ("setVrrp4SessCircuitFailOver", 7),
          ("delVrrp4SessCircuitFailOver", 8),
          ("setVrrp4SessPreemptMode", 9),
          ("setVrrp4SessPriority", 10),
          ("delVrrp4SessPriority", 11),
          ("setVrrp4SessSwitchBackDelay", 12),
          ("delVrrp4SessSwitchBackDelay", 13),
          ("setVrrp4SessVirtualIp", 14),
          ("delVrrp4SessVirtualIp", 15),
          ("setVrrp4SessCompatibleV2", 16))
    )


_SleVrrp4SessionControlRequest_Type.__name__ = "Integer32"
_SleVrrp4SessionControlRequest_Object = MibScalar
sleVrrp4SessionControlRequest = _SleVrrp4SessionControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 1),
    _SleVrrp4SessionControlRequest_Type()
)
sleVrrp4SessionControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlRequest.setStatus("current")
_SleVrrp4SessionControlStatus_Type = SleControlStatusType
_SleVrrp4SessionControlStatus_Object = MibScalar
sleVrrp4SessionControlStatus = _SleVrrp4SessionControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 2),
    _SleVrrp4SessionControlStatus_Type()
)
sleVrrp4SessionControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlStatus.setStatus("current")
_SleVrrp4SessionControlTimer_Type = Gauge32
_SleVrrp4SessionControlTimer_Object = MibScalar
sleVrrp4SessionControlTimer = _SleVrrp4SessionControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 3),
    _SleVrrp4SessionControlTimer_Type()
)
sleVrrp4SessionControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlTimer.setStatus("current")
_SleVrrp4SessionControlTimeStamp_Type = TimeTicks
_SleVrrp4SessionControlTimeStamp_Object = MibScalar
sleVrrp4SessionControlTimeStamp = _SleVrrp4SessionControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 4),
    _SleVrrp4SessionControlTimeStamp_Type()
)
sleVrrp4SessionControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlTimeStamp.setStatus("current")
_SleVrrp4SessionControlReqResult_Type = SleControlRequestResultType
_SleVrrp4SessionControlReqResult_Object = MibScalar
sleVrrp4SessionControlReqResult = _SleVrrp4SessionControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 5),
    _SleVrrp4SessionControlReqResult_Type()
)
sleVrrp4SessionControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlReqResult.setStatus("current")


class _SleVrrp4SessionControlVrId_Type(Integer32):
    """Custom type sleVrrp4SessionControlVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessionControlVrId_Type.__name__ = "Integer32"
_SleVrrp4SessionControlVrId_Object = MibScalar
sleVrrp4SessionControlVrId = _SleVrrp4SessionControlVrId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 6),
    _SleVrrp4SessionControlVrId_Type()
)
sleVrrp4SessionControlVrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlVrId.setStatus("current")
_SleVrrp4SessionControlIfIndex_Type = Integer32
_SleVrrp4SessionControlIfIndex_Object = MibScalar
sleVrrp4SessionControlIfIndex = _SleVrrp4SessionControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 7),
    _SleVrrp4SessionControlIfIndex_Type()
)
sleVrrp4SessionControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlIfIndex.setStatus("current")


class _SleVrrp4SessionControlSessionStatus_Type(Integer32):
    """Custom type sleVrrp4SessionControlSessionStatus based on Integer32"""
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


_SleVrrp4SessionControlSessionStatus_Type.__name__ = "Integer32"
_SleVrrp4SessionControlSessionStatus_Object = MibScalar
sleVrrp4SessionControlSessionStatus = _SleVrrp4SessionControlSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 8),
    _SleVrrp4SessionControlSessionStatus_Type()
)
sleVrrp4SessionControlSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlSessionStatus.setStatus("current")


class _SleVrrp4SessionControlAcceptMode_Type(Integer32):
    """Custom type sleVrrp4SessionControlAcceptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SleVrrp4SessionControlAcceptMode_Type.__name__ = "Integer32"
_SleVrrp4SessionControlAcceptMode_Object = MibScalar
sleVrrp4SessionControlAcceptMode = _SleVrrp4SessionControlAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 9),
    _SleVrrp4SessionControlAcceptMode_Type()
)
sleVrrp4SessionControlAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlAcceptMode.setStatus("current")


class _SleVrrp4SessionControlAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp4SessionControlAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SleVrrp4SessionControlAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp4SessionControlAdvertisementInterval_Object = MibScalar
sleVrrp4SessionControlAdvertisementInterval = _SleVrrp4SessionControlAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 10),
    _SleVrrp4SessionControlAdvertisementInterval_Type()
)
sleVrrp4SessionControlAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlAdvertisementInterval.setStatus("current")
_SleVrrp4SessionControlCircuitFailOverIfIndex_Type = Integer32
_SleVrrp4SessionControlCircuitFailOverIfIndex_Object = MibScalar
sleVrrp4SessionControlCircuitFailOverIfIndex = _SleVrrp4SessionControlCircuitFailOverIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 11),
    _SleVrrp4SessionControlCircuitFailOverIfIndex_Type()
)
sleVrrp4SessionControlCircuitFailOverIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlCircuitFailOverIfIndex.setStatus("current")


class _SleVrrp4SessionControlCircuitFailOverPriorityDelta_Type(Integer32):
    """Custom type sleVrrp4SessionControlCircuitFailOverPriorityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 253),
    )


_SleVrrp4SessionControlCircuitFailOverPriorityDelta_Type.__name__ = "Integer32"
_SleVrrp4SessionControlCircuitFailOverPriorityDelta_Object = MibScalar
sleVrrp4SessionControlCircuitFailOverPriorityDelta = _SleVrrp4SessionControlCircuitFailOverPriorityDelta_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 12),
    _SleVrrp4SessionControlCircuitFailOverPriorityDelta_Type()
)
sleVrrp4SessionControlCircuitFailOverPriorityDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlCircuitFailOverPriorityDelta.setStatus("current")


class _SleVrrp4SessionControlPreemptMode_Type(Integer32):
    """Custom type sleVrrp4SessionControlPreemptMode based on Integer32"""
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


_SleVrrp4SessionControlPreemptMode_Type.__name__ = "Integer32"
_SleVrrp4SessionControlPreemptMode_Object = MibScalar
sleVrrp4SessionControlPreemptMode = _SleVrrp4SessionControlPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 13),
    _SleVrrp4SessionControlPreemptMode_Type()
)
sleVrrp4SessionControlPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlPreemptMode.setStatus("current")


class _SleVrrp4SessionControlPriority_Type(Integer32):
    """Custom type sleVrrp4SessionControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessionControlPriority_Type.__name__ = "Integer32"
_SleVrrp4SessionControlPriority_Object = MibScalar
sleVrrp4SessionControlPriority = _SleVrrp4SessionControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 14),
    _SleVrrp4SessionControlPriority_Type()
)
sleVrrp4SessionControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlPriority.setStatus("current")


class _SleVrrp4SessionControlSwitchBackDelay_Type(Integer32):
    """Custom type sleVrrp4SessionControlSwitchBackDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_SleVrrp4SessionControlSwitchBackDelay_Type.__name__ = "Integer32"
_SleVrrp4SessionControlSwitchBackDelay_Object = MibScalar
sleVrrp4SessionControlSwitchBackDelay = _SleVrrp4SessionControlSwitchBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 15),
    _SleVrrp4SessionControlSwitchBackDelay_Type()
)
sleVrrp4SessionControlSwitchBackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlSwitchBackDelay.setStatus("current")
_SleVrrp4SessionControlVirtualIpVal_Type = OctetString
_SleVrrp4SessionControlVirtualIpVal_Object = MibScalar
sleVrrp4SessionControlVirtualIpVal = _SleVrrp4SessionControlVirtualIpVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 16),
    _SleVrrp4SessionControlVirtualIpVal_Type()
)
sleVrrp4SessionControlVirtualIpVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlVirtualIpVal.setStatus("current")


class _SleVrrp4SessionControlVirtualIpOwner_Type(Integer32):
    """Custom type sleVrrp4SessionControlVirtualIpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("set", 1))
    )


_SleVrrp4SessionControlVirtualIpOwner_Type.__name__ = "Integer32"
_SleVrrp4SessionControlVirtualIpOwner_Object = MibScalar
sleVrrp4SessionControlVirtualIpOwner = _SleVrrp4SessionControlVirtualIpOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 17),
    _SleVrrp4SessionControlVirtualIpOwner_Type()
)
sleVrrp4SessionControlVirtualIpOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlVirtualIpOwner.setStatus("current")


class _SleVrrp4SessionControlCompatibleV2_Type(Integer32):
    """Custom type sleVrrp4SessionControlCompatibleV2 based on Integer32"""
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


_SleVrrp4SessionControlCompatibleV2_Type.__name__ = "Integer32"
_SleVrrp4SessionControlCompatibleV2_Object = MibScalar
sleVrrp4SessionControlCompatibleV2 = _SleVrrp4SessionControlCompatibleV2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 2, 18),
    _SleVrrp4SessionControlCompatibleV2_Type()
)
sleVrrp4SessionControlCompatibleV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessionControlCompatibleV2.setStatus("current")
_SleVrrp4SessionNotification_ObjectIdentity = ObjectIdentity
sleVrrp4SessionNotification = _SleVrrp4SessionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 3)
)
_SleVrrp4SessInfoTable_Object = MibTable
sleVrrp4SessInfoTable = _SleVrrp4SessInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sleVrrp4SessInfoTable.setStatus("current")
_SleVrrp4SessInfoEntry_Object = MibTableRow
sleVrrp4SessInfoEntry = _SleVrrp4SessInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1)
)
sleVrrp4SessInfoEntry.setIndexNames(
    (0, "SLE-VRRP-MIB", "sleVrrp4SessInfoVrId"),
    (0, "SLE-VRRP-MIB", "sleVrrp4SessInfoIfIndex"),
)
if mibBuilder.loadTexts:
    sleVrrp4SessInfoEntry.setStatus("current")


class _SleVrrp4SessInfoVrId_Type(Integer32):
    """Custom type sleVrrp4SessInfoVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessInfoVrId_Type.__name__ = "Integer32"
_SleVrrp4SessInfoVrId_Object = MibTableColumn
sleVrrp4SessInfoVrId = _SleVrrp4SessInfoVrId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 1),
    _SleVrrp4SessInfoVrId_Type()
)
sleVrrp4SessInfoVrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoVrId.setStatus("current")


class _SleVrrp4SessInfoIfIndex_Type(Integer32):
    """Custom type sleVrrp4SessInfoIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessInfoIfIndex_Type.__name__ = "Integer32"
_SleVrrp4SessInfoIfIndex_Object = MibTableColumn
sleVrrp4SessInfoIfIndex = _SleVrrp4SessInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 2),
    _SleVrrp4SessInfoIfIndex_Type()
)
sleVrrp4SessInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoIfIndex.setStatus("current")
_SleVrrp4SessInfoVrfName_Type = OctetString
_SleVrrp4SessInfoVrfName_Object = MibTableColumn
sleVrrp4SessInfoVrfName = _SleVrrp4SessInfoVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 3),
    _SleVrrp4SessInfoVrfName_Type()
)
sleVrrp4SessInfoVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoVrfName.setStatus("current")
_SleVrrp4SessInfoVrfFibId_Type = Integer32
_SleVrrp4SessInfoVrfFibId_Object = MibTableColumn
sleVrrp4SessInfoVrfFibId = _SleVrrp4SessInfoVrfFibId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 4),
    _SleVrrp4SessInfoVrfFibId_Type()
)
sleVrrp4SessInfoVrfFibId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoVrfFibId.setStatus("current")


class _SleVrrp4SessInfoSessionAdminState_Type(Integer32):
    """Custom type sleVrrp4SessInfoSessionAdminState based on Integer32"""
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


_SleVrrp4SessInfoSessionAdminState_Type.__name__ = "Integer32"
_SleVrrp4SessInfoSessionAdminState_Object = MibTableColumn
sleVrrp4SessInfoSessionAdminState = _SleVrrp4SessInfoSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 5),
    _SleVrrp4SessInfoSessionAdminState_Type()
)
sleVrrp4SessInfoSessionAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoSessionAdminState.setStatus("current")


class _SleVrrp4SessInfoSessionState_Type(Integer32):
    """Custom type sleVrrp4SessInfoSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("backup", 2),
          ("master", 3))
    )


_SleVrrp4SessInfoSessionState_Type.__name__ = "Integer32"
_SleVrrp4SessInfoSessionState_Object = MibTableColumn
sleVrrp4SessInfoSessionState = _SleVrrp4SessInfoSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 6),
    _SleVrrp4SessInfoSessionState_Type()
)
sleVrrp4SessInfoSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoSessionState.setStatus("current")


class _SleVrrp4SessInfoSessionStateInitMsg_Type(Integer32):
    """Custom type sleVrrp4SessInfoSessionStateInitMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("adminDown", 0),
          ("interfaceNotRunning", 1),
          ("circuitDown", 2),
          ("noSubnet", 3),
          ("virtualIpUnset", 4),
          ("inSwitchBackDelay", 5))
    )


_SleVrrp4SessInfoSessionStateInitMsg_Type.__name__ = "Integer32"
_SleVrrp4SessInfoSessionStateInitMsg_Object = MibTableColumn
sleVrrp4SessInfoSessionStateInitMsg = _SleVrrp4SessInfoSessionStateInitMsg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 7),
    _SleVrrp4SessInfoSessionStateInitMsg_Type()
)
sleVrrp4SessInfoSessionStateInitMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoSessionStateInitMsg.setStatus("current")
_SleVrrp4SessInfoVirtualIp_Type = OctetString
_SleVrrp4SessInfoVirtualIp_Object = MibTableColumn
sleVrrp4SessInfoVirtualIp = _SleVrrp4SessInfoVirtualIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 8),
    _SleVrrp4SessInfoVirtualIp_Type()
)
sleVrrp4SessInfoVirtualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoVirtualIp.setStatus("current")


class _SleVrrp4SessInfoVirtualIpOwner_Type(Integer32):
    """Custom type sleVrrp4SessInfoVirtualIpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("set", 1))
    )


_SleVrrp4SessInfoVirtualIpOwner_Type.__name__ = "Integer32"
_SleVrrp4SessInfoVirtualIpOwner_Object = MibTableColumn
sleVrrp4SessInfoVirtualIpOwner = _SleVrrp4SessInfoVirtualIpOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 9),
    _SleVrrp4SessInfoVirtualIpOwner_Type()
)
sleVrrp4SessInfoVirtualIpOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoVirtualIpOwner.setStatus("current")
_SleVrrp4SessInfoConfiguredPriority_Type = Integer32
_SleVrrp4SessInfoConfiguredPriority_Object = MibTableColumn
sleVrrp4SessInfoConfiguredPriority = _SleVrrp4SessInfoConfiguredPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 10),
    _SleVrrp4SessInfoConfiguredPriority_Type()
)
sleVrrp4SessInfoConfiguredPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoConfiguredPriority.setStatus("current")
_SleVrrp4SessInfoCurrentPriority_Type = Integer32
_SleVrrp4SessInfoCurrentPriority_Object = MibTableColumn
sleVrrp4SessInfoCurrentPriority = _SleVrrp4SessInfoCurrentPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 11),
    _SleVrrp4SessInfoCurrentPriority_Type()
)
sleVrrp4SessInfoCurrentPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoCurrentPriority.setStatus("current")
_SleVrrp4SessInfoSwitchBackDelay_Type = Integer32
_SleVrrp4SessInfoSwitchBackDelay_Object = MibTableColumn
sleVrrp4SessInfoSwitchBackDelay = _SleVrrp4SessInfoSwitchBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 12),
    _SleVrrp4SessInfoSwitchBackDelay_Type()
)
sleVrrp4SessInfoSwitchBackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoSwitchBackDelay.setStatus("current")


class _SleVrrp4SessInfoAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp4SessInfoAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SleVrrp4SessInfoAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp4SessInfoAdvertisementInterval_Object = MibTableColumn
sleVrrp4SessInfoAdvertisementInterval = _SleVrrp4SessInfoAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 13),
    _SleVrrp4SessInfoAdvertisementInterval_Type()
)
sleVrrp4SessInfoAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoAdvertisementInterval.setStatus("current")


class _SleVrrp4SessInfoMasterAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp4SessInfoMasterAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SleVrrp4SessInfoMasterAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp4SessInfoMasterAdvertisementInterval_Object = MibTableColumn
sleVrrp4SessInfoMasterAdvertisementInterval = _SleVrrp4SessInfoMasterAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 14),
    _SleVrrp4SessInfoMasterAdvertisementInterval_Type()
)
sleVrrp4SessInfoMasterAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoMasterAdvertisementInterval.setStatus("current")
_SleVrrp4SessInfoSkewTime_Type = Integer32
_SleVrrp4SessInfoSkewTime_Object = MibTableColumn
sleVrrp4SessInfoSkewTime = _SleVrrp4SessInfoSkewTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 15),
    _SleVrrp4SessInfoSkewTime_Type()
)
sleVrrp4SessInfoSkewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoSkewTime.setStatus("current")


class _SleVrrp4SessInfoAcceptMode_Type(Integer32):
    """Custom type sleVrrp4SessInfoAcceptMode based on Integer32"""
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


_SleVrrp4SessInfoAcceptMode_Type.__name__ = "Integer32"
_SleVrrp4SessInfoAcceptMode_Object = MibTableColumn
sleVrrp4SessInfoAcceptMode = _SleVrrp4SessInfoAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 16),
    _SleVrrp4SessInfoAcceptMode_Type()
)
sleVrrp4SessInfoAcceptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoAcceptMode.setStatus("current")


class _SleVrrp4SessInfoPreemptMode_Type(Integer32):
    """Custom type sleVrrp4SessInfoPreemptMode based on Integer32"""
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


_SleVrrp4SessInfoPreemptMode_Type.__name__ = "Integer32"
_SleVrrp4SessInfoPreemptMode_Object = MibTableColumn
sleVrrp4SessInfoPreemptMode = _SleVrrp4SessInfoPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 17),
    _SleVrrp4SessInfoPreemptMode_Type()
)
sleVrrp4SessInfoPreemptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoPreemptMode.setStatus("current")
_SleVrrp4SessInfoMonitorCircuitIfIndex_Type = Integer32
_SleVrrp4SessInfoMonitorCircuitIfIndex_Object = MibTableColumn
sleVrrp4SessInfoMonitorCircuitIfIndex = _SleVrrp4SessInfoMonitorCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 18),
    _SleVrrp4SessInfoMonitorCircuitIfIndex_Type()
)
sleVrrp4SessInfoMonitorCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoMonitorCircuitIfIndex.setStatus("current")


class _SleVrrp4SessInfoMonitorCircuitPrioDelta_Type(Integer32):
    """Custom type sleVrrp4SessInfoMonitorCircuitPrioDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 253),
    )


_SleVrrp4SessInfoMonitorCircuitPrioDelta_Type.__name__ = "Integer32"
_SleVrrp4SessInfoMonitorCircuitPrioDelta_Object = MibTableColumn
sleVrrp4SessInfoMonitorCircuitPrioDelta = _SleVrrp4SessInfoMonitorCircuitPrioDelta_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 19),
    _SleVrrp4SessInfoMonitorCircuitPrioDelta_Type()
)
sleVrrp4SessInfoMonitorCircuitPrioDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoMonitorCircuitPrioDelta.setStatus("current")


class _SleVrrp4SessInfoMonitorCircuitState_Type(Integer32):
    """Custom type sleVrrp4SessInfoMonitorCircuitState based on Integer32"""
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


_SleVrrp4SessInfoMonitorCircuitState_Type.__name__ = "Integer32"
_SleVrrp4SessInfoMonitorCircuitState_Object = MibTableColumn
sleVrrp4SessInfoMonitorCircuitState = _SleVrrp4SessInfoMonitorCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 20),
    _SleVrrp4SessInfoMonitorCircuitState_Type()
)
sleVrrp4SessInfoMonitorCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoMonitorCircuitState.setStatus("current")


class _SleVrrp4SessInfoMulticastMembershipOn_Type(Integer32):
    """Custom type sleVrrp4SessInfoMulticastMembershipOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joined", 1),
          ("left", 2))
    )


_SleVrrp4SessInfoMulticastMembershipOn_Type.__name__ = "Integer32"
_SleVrrp4SessInfoMulticastMembershipOn_Object = MibTableColumn
sleVrrp4SessInfoMulticastMembershipOn = _SleVrrp4SessInfoMulticastMembershipOn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 21),
    _SleVrrp4SessInfoMulticastMembershipOn_Type()
)
sleVrrp4SessInfoMulticastMembershipOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoMulticastMembershipOn.setStatus("current")


class _SleVrrp4SessInfoCompatibleV2_Type(Integer32):
    """Custom type sleVrrp4SessInfoCompatibleV2 based on Integer32"""
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


_SleVrrp4SessInfoCompatibleV2_Type.__name__ = "Integer32"
_SleVrrp4SessInfoCompatibleV2_Object = MibTableColumn
sleVrrp4SessInfoCompatibleV2 = _SleVrrp4SessInfoCompatibleV2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 4, 1, 22),
    _SleVrrp4SessInfoCompatibleV2_Type()
)
sleVrrp4SessInfoCompatibleV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessInfoCompatibleV2.setStatus("current")
_SleVrrp4SessStatTable_Object = MibTable
sleVrrp4SessStatTable = _SleVrrp4SessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5)
)
if mibBuilder.loadTexts:
    sleVrrp4SessStatTable.setStatus("current")
_SleVrrp4SessStatEntry_Object = MibTableRow
sleVrrp4SessStatEntry = _SleVrrp4SessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1)
)
sleVrrp4SessStatEntry.setIndexNames(
    (0, "SLE-VRRP-MIB", "sleVrrp4SessStatVrid"),
    (0, "SLE-VRRP-MIB", "sleVrrp4SessStatIfIndex"),
)
if mibBuilder.loadTexts:
    sleVrrp4SessStatEntry.setStatus("current")


class _SleVrrp4SessStatVrid_Type(Integer32):
    """Custom type sleVrrp4SessStatVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessStatVrid_Type.__name__ = "Integer32"
_SleVrrp4SessStatVrid_Object = MibTableColumn
sleVrrp4SessStatVrid = _SleVrrp4SessStatVrid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 1),
    _SleVrrp4SessStatVrid_Type()
)
sleVrrp4SessStatVrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp4SessStatVrid.setStatus("current")


class _SleVrrp4SessStatIfIndex_Type(Integer32):
    """Custom type sleVrrp4SessStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp4SessStatIfIndex_Type.__name__ = "Integer32"
_SleVrrp4SessStatIfIndex_Object = MibTableColumn
sleVrrp4SessStatIfIndex = _SleVrrp4SessStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 2),
    _SleVrrp4SessStatIfIndex_Type()
)
sleVrrp4SessStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatIfIndex.setStatus("current")
_SleVrrp4SessStatChecksumErrors_Type = Counter32
_SleVrrp4SessStatChecksumErrors_Object = MibTableColumn
sleVrrp4SessStatChecksumErrors = _SleVrrp4SessStatChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 3),
    _SleVrrp4SessStatChecksumErrors_Type()
)
sleVrrp4SessStatChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatChecksumErrors.setStatus("current")
_SleVrrp4SessStatVersionErrors_Type = Counter32
_SleVrrp4SessStatVersionErrors_Object = MibTableColumn
sleVrrp4SessStatVersionErrors = _SleVrrp4SessStatVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 4),
    _SleVrrp4SessStatVersionErrors_Type()
)
sleVrrp4SessStatVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatVersionErrors.setStatus("current")
_SleVrrp4SessStatVridErrors_Type = Counter32
_SleVrrp4SessStatVridErrors_Object = MibTableColumn
sleVrrp4SessStatVridErrors = _SleVrrp4SessStatVridErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 5),
    _SleVrrp4SessStatVridErrors_Type()
)
sleVrrp4SessStatVridErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatVridErrors.setStatus("current")
_SleVrrp4SessStatMasterTransitions_Type = Counter32
_SleVrrp4SessStatMasterTransitions_Object = MibTableColumn
sleVrrp4SessStatMasterTransitions = _SleVrrp4SessStatMasterTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 6),
    _SleVrrp4SessStatMasterTransitions_Type()
)
sleVrrp4SessStatMasterTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatMasterTransitions.setStatus("current")
_SleVrrp4SessStatAdvertisementsRcvd_Type = Counter32
_SleVrrp4SessStatAdvertisementsRcvd_Object = MibTableColumn
sleVrrp4SessStatAdvertisementsRcvd = _SleVrrp4SessStatAdvertisementsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 7),
    _SleVrrp4SessStatAdvertisementsRcvd_Type()
)
sleVrrp4SessStatAdvertisementsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatAdvertisementsRcvd.setStatus("current")
_SleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors_Type = Counter32
_SleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors = _SleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 8),
    _SleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors_Type()
)
sleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors.setStatus("current")
_SleVrrp4SessStatPktsRcvdIpTtlErros_Type = Counter32
_SleVrrp4SessStatPktsRcvdIpTtlErros_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdIpTtlErros = _SleVrrp4SessStatPktsRcvdIpTtlErros_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 9),
    _SleVrrp4SessStatPktsRcvdIpTtlErros_Type()
)
sleVrrp4SessStatPktsRcvdIpTtlErros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdIpTtlErros.setStatus("current")
_SleVrrp4SessStatPktsRcvdZeroPriority_Type = Counter32
_SleVrrp4SessStatPktsRcvdZeroPriority_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdZeroPriority = _SleVrrp4SessStatPktsRcvdZeroPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 10),
    _SleVrrp4SessStatPktsRcvdZeroPriority_Type()
)
sleVrrp4SessStatPktsRcvdZeroPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdZeroPriority.setStatus("current")
_SleVrrp4SessStatPktsSentZeroPriority_Type = Counter32
_SleVrrp4SessStatPktsSentZeroPriority_Object = MibTableColumn
sleVrrp4SessStatPktsSentZeroPriority = _SleVrrp4SessStatPktsSentZeroPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 11),
    _SleVrrp4SessStatPktsSentZeroPriority_Type()
)
sleVrrp4SessStatPktsSentZeroPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsSentZeroPriority.setStatus("current")
_SleVrrp4SessStatPktsRcvdInvalidType_Type = Counter32
_SleVrrp4SessStatPktsRcvdInvalidType_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdInvalidType = _SleVrrp4SessStatPktsRcvdInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 12),
    _SleVrrp4SessStatPktsRcvdInvalidType_Type()
)
sleVrrp4SessStatPktsRcvdInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdInvalidType.setStatus("current")
_SleVrrp4SessStatPktsRcvdAddressListErrors_Type = Counter32
_SleVrrp4SessStatPktsRcvdAddressListErrors_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdAddressListErrors = _SleVrrp4SessStatPktsRcvdAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 13),
    _SleVrrp4SessStatPktsRcvdAddressListErrors_Type()
)
sleVrrp4SessStatPktsRcvdAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdAddressListErrors.setStatus("current")
_SleVrrp4SessStatPktsRcvdPacketLengthErrors_Type = Counter32
_SleVrrp4SessStatPktsRcvdPacketLengthErrors_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdPacketLengthErrors = _SleVrrp4SessStatPktsRcvdPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 14),
    _SleVrrp4SessStatPktsRcvdPacketLengthErrors_Type()
)
sleVrrp4SessStatPktsRcvdPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdPacketLengthErrors.setStatus("current")
_SleVrrp4SessStatPktsRcvdUnknownAuthenticationType_Type = Counter32
_SleVrrp4SessStatPktsRcvdUnknownAuthenticationType_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdUnknownAuthenticationType = _SleVrrp4SessStatPktsRcvdUnknownAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 15),
    _SleVrrp4SessStatPktsRcvdUnknownAuthenticationType_Type()
)
sleVrrp4SessStatPktsRcvdUnknownAuthenticationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdUnknownAuthenticationType.setStatus("current")
_SleVrrp4SessStatPktsRcvdIpCountMismatch_Type = Counter32
_SleVrrp4SessStatPktsRcvdIpCountMismatch_Object = MibTableColumn
sleVrrp4SessStatPktsRcvdIpCountMismatch = _SleVrrp4SessStatPktsRcvdIpCountMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 16),
    _SleVrrp4SessStatPktsRcvdIpCountMismatch_Type()
)
sleVrrp4SessStatPktsRcvdIpCountMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatPktsRcvdIpCountMismatch.setStatus("current")
_SleVrrp4SessStatDiscontinuityTime_Type = OctetString
_SleVrrp4SessStatDiscontinuityTime_Object = MibTableColumn
sleVrrp4SessStatDiscontinuityTime = _SleVrrp4SessStatDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 17),
    _SleVrrp4SessStatDiscontinuityTime_Type()
)
sleVrrp4SessStatDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatDiscontinuityTime.setStatus("current")
_SleVrrp4SessStatRefreshRate_Type = Integer32
_SleVrrp4SessStatRefreshRate_Object = MibTableColumn
sleVrrp4SessStatRefreshRate = _SleVrrp4SessStatRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 1, 5, 1, 18),
    _SleVrrp4SessStatRefreshRate_Type()
)
sleVrrp4SessStatRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp4SessStatRefreshRate.setStatus("current")
_SleVrrp6Session_ObjectIdentity = ObjectIdentity
sleVrrp6Session = _SleVrrp6Session_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2)
)
_SleVrrp6SessionTable_Object = MibTable
sleVrrp6SessionTable = _SleVrrp6SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleVrrp6SessionTable.setStatus("current")
_SleVrrp6SessionEntry_Object = MibTableRow
sleVrrp6SessionEntry = _SleVrrp6SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1)
)
sleVrrp6SessionEntry.setIndexNames(
    (0, "SLE-VRRP-MIB", "sleVrrp6SessionVrId"),
    (0, "SLE-VRRP-MIB", "sleVrrp6SessionIfIndex"),
)
if mibBuilder.loadTexts:
    sleVrrp6SessionEntry.setStatus("current")


class _SleVrrp6SessionVrId_Type(Integer32):
    """Custom type sleVrrp6SessionVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessionVrId_Type.__name__ = "Integer32"
_SleVrrp6SessionVrId_Object = MibTableColumn
sleVrrp6SessionVrId = _SleVrrp6SessionVrId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 1),
    _SleVrrp6SessionVrId_Type()
)
sleVrrp6SessionVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionVrId.setStatus("current")


class _SleVrrp6SessionIfIndex_Type(Integer32):
    """Custom type sleVrrp6SessionIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessionIfIndex_Type.__name__ = "Integer32"
_SleVrrp6SessionIfIndex_Object = MibTableColumn
sleVrrp6SessionIfIndex = _SleVrrp6SessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 2),
    _SleVrrp6SessionIfIndex_Type()
)
sleVrrp6SessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionIfIndex.setStatus("current")


class _SleVrrp6SessionStatus_Type(Integer32):
    """Custom type sleVrrp6SessionStatus based on Integer32"""
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


_SleVrrp6SessionStatus_Type.__name__ = "Integer32"
_SleVrrp6SessionStatus_Object = MibTableColumn
sleVrrp6SessionStatus = _SleVrrp6SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 3),
    _SleVrrp6SessionStatus_Type()
)
sleVrrp6SessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionStatus.setStatus("current")


class _SleVrrp6SessionAcceptMode_Type(Integer32):
    """Custom type sleVrrp6SessionAcceptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SleVrrp6SessionAcceptMode_Type.__name__ = "Integer32"
_SleVrrp6SessionAcceptMode_Object = MibTableColumn
sleVrrp6SessionAcceptMode = _SleVrrp6SessionAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 4),
    _SleVrrp6SessionAcceptMode_Type()
)
sleVrrp6SessionAcceptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionAcceptMode.setStatus("current")


class _SleVrrp6SessionAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp6SessionAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000),
    )


_SleVrrp6SessionAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp6SessionAdvertisementInterval_Object = MibTableColumn
sleVrrp6SessionAdvertisementInterval = _SleVrrp6SessionAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 5),
    _SleVrrp6SessionAdvertisementInterval_Type()
)
sleVrrp6SessionAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionAdvertisementInterval.setStatus("current")
_SleVrrp6SessionCircuitFailOverIfIndex_Type = Integer32
_SleVrrp6SessionCircuitFailOverIfIndex_Object = MibTableColumn
sleVrrp6SessionCircuitFailOverIfIndex = _SleVrrp6SessionCircuitFailOverIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 6),
    _SleVrrp6SessionCircuitFailOverIfIndex_Type()
)
sleVrrp6SessionCircuitFailOverIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionCircuitFailOverIfIndex.setStatus("current")


class _SleVrrp6SessionCircuitFailOverPriorityDelta_Type(Integer32):
    """Custom type sleVrrp6SessionCircuitFailOverPriorityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 253),
    )


_SleVrrp6SessionCircuitFailOverPriorityDelta_Type.__name__ = "Integer32"
_SleVrrp6SessionCircuitFailOverPriorityDelta_Object = MibTableColumn
sleVrrp6SessionCircuitFailOverPriorityDelta = _SleVrrp6SessionCircuitFailOverPriorityDelta_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 7),
    _SleVrrp6SessionCircuitFailOverPriorityDelta_Type()
)
sleVrrp6SessionCircuitFailOverPriorityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionCircuitFailOverPriorityDelta.setStatus("current")


class _SleVrrp6SessionPreemptMode_Type(Integer32):
    """Custom type sleVrrp6SessionPreemptMode based on Integer32"""
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


_SleVrrp6SessionPreemptMode_Type.__name__ = "Integer32"
_SleVrrp6SessionPreemptMode_Object = MibTableColumn
sleVrrp6SessionPreemptMode = _SleVrrp6SessionPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 8),
    _SleVrrp6SessionPreemptMode_Type()
)
sleVrrp6SessionPreemptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionPreemptMode.setStatus("current")


class _SleVrrp6SessionPriority_Type(Integer32):
    """Custom type sleVrrp6SessionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessionPriority_Type.__name__ = "Integer32"
_SleVrrp6SessionPriority_Object = MibTableColumn
sleVrrp6SessionPriority = _SleVrrp6SessionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 9),
    _SleVrrp6SessionPriority_Type()
)
sleVrrp6SessionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionPriority.setStatus("current")


class _SleVrrp6SessionSwitchBackDelay_Type(Integer32):
    """Custom type sleVrrp6SessionSwitchBackDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 500000),
    )


_SleVrrp6SessionSwitchBackDelay_Type.__name__ = "Integer32"
_SleVrrp6SessionSwitchBackDelay_Object = MibTableColumn
sleVrrp6SessionSwitchBackDelay = _SleVrrp6SessionSwitchBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 10),
    _SleVrrp6SessionSwitchBackDelay_Type()
)
sleVrrp6SessionSwitchBackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionSwitchBackDelay.setStatus("current")
_SleVrrp6SessionVirtualIpVal_Type = OctetString
_SleVrrp6SessionVirtualIpVal_Object = MibTableColumn
sleVrrp6SessionVirtualIpVal = _SleVrrp6SessionVirtualIpVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 11),
    _SleVrrp6SessionVirtualIpVal_Type()
)
sleVrrp6SessionVirtualIpVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionVirtualIpVal.setStatus("current")


class _SleVrrp6SessionVirtualIpOwner_Type(Integer32):
    """Custom type sleVrrp6SessionVirtualIpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unSet", 0),
          ("set", 1))
    )


_SleVrrp6SessionVirtualIpOwner_Type.__name__ = "Integer32"
_SleVrrp6SessionVirtualIpOwner_Object = MibTableColumn
sleVrrp6SessionVirtualIpOwner = _SleVrrp6SessionVirtualIpOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 1, 1, 12),
    _SleVrrp6SessionVirtualIpOwner_Type()
)
sleVrrp6SessionVirtualIpOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionVirtualIpOwner.setStatus("current")
_SleVrrp6SessionControl_ObjectIdentity = ObjectIdentity
sleVrrp6SessionControl = _SleVrrp6SessionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2)
)


class _SleVrrp6SessionControlRequest_Type(Integer32):
    """Custom type sleVrrp6SessionControlRequest based on Integer32"""
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
        *(("createVrrp6Sess", 1),
          ("delVrrp6Sess", 2),
          ("setVrrp6SessStatus", 3),
          ("setVrrp6SessAcceptMode", 4),
          ("setVrrp6SessAdvInterval", 5),
          ("delVrrp6SessAdvInterval", 6),
          ("setVrrp6SessCircuitFailOver", 7),
          ("delVrrp6SessCircuitFailOver", 8),
          ("setVrrp6SessPreemptMode", 9),
          ("setVrrp6SessPriority", 10),
          ("delVrrp6SessPriority", 11),
          ("setVrrp6SessSwitchBackDelay", 12),
          ("delVrrp6SessSwitchBackDelay", 13),
          ("setVrrp6SessVirtualIp", 14),
          ("delVrrp6SessVirtualIp", 15))
    )


_SleVrrp6SessionControlRequest_Type.__name__ = "Integer32"
_SleVrrp6SessionControlRequest_Object = MibScalar
sleVrrp6SessionControlRequest = _SleVrrp6SessionControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 1),
    _SleVrrp6SessionControlRequest_Type()
)
sleVrrp6SessionControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlRequest.setStatus("current")
_SleVrrp6SessionControlStatus_Type = SleControlStatusType
_SleVrrp6SessionControlStatus_Object = MibScalar
sleVrrp6SessionControlStatus = _SleVrrp6SessionControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 2),
    _SleVrrp6SessionControlStatus_Type()
)
sleVrrp6SessionControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlStatus.setStatus("current")
_SleVrrp6SessionControlTimer_Type = Gauge32
_SleVrrp6SessionControlTimer_Object = MibScalar
sleVrrp6SessionControlTimer = _SleVrrp6SessionControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 3),
    _SleVrrp6SessionControlTimer_Type()
)
sleVrrp6SessionControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlTimer.setStatus("current")
_SleVrrp6SessionControlTimeStamp_Type = TimeTicks
_SleVrrp6SessionControlTimeStamp_Object = MibScalar
sleVrrp6SessionControlTimeStamp = _SleVrrp6SessionControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 4),
    _SleVrrp6SessionControlTimeStamp_Type()
)
sleVrrp6SessionControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlTimeStamp.setStatus("current")
_SleVrrp6SessionControlReqResult_Type = SleControlRequestResultType
_SleVrrp6SessionControlReqResult_Object = MibScalar
sleVrrp6SessionControlReqResult = _SleVrrp6SessionControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 5),
    _SleVrrp6SessionControlReqResult_Type()
)
sleVrrp6SessionControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlReqResult.setStatus("current")


class _SleVrrp6SessionControlVrId_Type(Integer32):
    """Custom type sleVrrp6SessionControlVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessionControlVrId_Type.__name__ = "Integer32"
_SleVrrp6SessionControlVrId_Object = MibScalar
sleVrrp6SessionControlVrId = _SleVrrp6SessionControlVrId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 6),
    _SleVrrp6SessionControlVrId_Type()
)
sleVrrp6SessionControlVrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlVrId.setStatus("current")
_SleVrrp6SessionControlIfIndex_Type = Integer32
_SleVrrp6SessionControlIfIndex_Object = MibScalar
sleVrrp6SessionControlIfIndex = _SleVrrp6SessionControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 7),
    _SleVrrp6SessionControlIfIndex_Type()
)
sleVrrp6SessionControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlIfIndex.setStatus("current")


class _SleVrrp6SessionControlSessionStatus_Type(Integer32):
    """Custom type sleVrrp6SessionControlSessionStatus based on Integer32"""
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


_SleVrrp6SessionControlSessionStatus_Type.__name__ = "Integer32"
_SleVrrp6SessionControlSessionStatus_Object = MibScalar
sleVrrp6SessionControlSessionStatus = _SleVrrp6SessionControlSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 8),
    _SleVrrp6SessionControlSessionStatus_Type()
)
sleVrrp6SessionControlSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlSessionStatus.setStatus("current")


class _SleVrrp6SessionControlAcceptMode_Type(Integer32):
    """Custom type sleVrrp6SessionControlAcceptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SleVrrp6SessionControlAcceptMode_Type.__name__ = "Integer32"
_SleVrrp6SessionControlAcceptMode_Object = MibScalar
sleVrrp6SessionControlAcceptMode = _SleVrrp6SessionControlAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 9),
    _SleVrrp6SessionControlAcceptMode_Type()
)
sleVrrp6SessionControlAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlAcceptMode.setStatus("current")


class _SleVrrp6SessionControlAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp6SessionControlAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SleVrrp6SessionControlAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp6SessionControlAdvertisementInterval_Object = MibScalar
sleVrrp6SessionControlAdvertisementInterval = _SleVrrp6SessionControlAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 10),
    _SleVrrp6SessionControlAdvertisementInterval_Type()
)
sleVrrp6SessionControlAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlAdvertisementInterval.setStatus("current")
_SleVrrp6SessionControlCircuitFailOverIfIndex_Type = Integer32
_SleVrrp6SessionControlCircuitFailOverIfIndex_Object = MibScalar
sleVrrp6SessionControlCircuitFailOverIfIndex = _SleVrrp6SessionControlCircuitFailOverIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 11),
    _SleVrrp6SessionControlCircuitFailOverIfIndex_Type()
)
sleVrrp6SessionControlCircuitFailOverIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlCircuitFailOverIfIndex.setStatus("current")


class _SleVrrp6SessionControlCircuitFailOverPriorityDelta_Type(Integer32):
    """Custom type sleVrrp6SessionControlCircuitFailOverPriorityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 253),
    )


_SleVrrp6SessionControlCircuitFailOverPriorityDelta_Type.__name__ = "Integer32"
_SleVrrp6SessionControlCircuitFailOverPriorityDelta_Object = MibScalar
sleVrrp6SessionControlCircuitFailOverPriorityDelta = _SleVrrp6SessionControlCircuitFailOverPriorityDelta_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 12),
    _SleVrrp6SessionControlCircuitFailOverPriorityDelta_Type()
)
sleVrrp6SessionControlCircuitFailOverPriorityDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlCircuitFailOverPriorityDelta.setStatus("current")


class _SleVrrp6SessionControlPreemptMode_Type(Integer32):
    """Custom type sleVrrp6SessionControlPreemptMode based on Integer32"""
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


_SleVrrp6SessionControlPreemptMode_Type.__name__ = "Integer32"
_SleVrrp6SessionControlPreemptMode_Object = MibScalar
sleVrrp6SessionControlPreemptMode = _SleVrrp6SessionControlPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 13),
    _SleVrrp6SessionControlPreemptMode_Type()
)
sleVrrp6SessionControlPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlPreemptMode.setStatus("current")


class _SleVrrp6SessionControlPriority_Type(Integer32):
    """Custom type sleVrrp6SessionControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessionControlPriority_Type.__name__ = "Integer32"
_SleVrrp6SessionControlPriority_Object = MibScalar
sleVrrp6SessionControlPriority = _SleVrrp6SessionControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 14),
    _SleVrrp6SessionControlPriority_Type()
)
sleVrrp6SessionControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlPriority.setStatus("current")


class _SleVrrp6SessionControlSwitchBackDelay_Type(Integer32):
    """Custom type sleVrrp6SessionControlSwitchBackDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_SleVrrp6SessionControlSwitchBackDelay_Type.__name__ = "Integer32"
_SleVrrp6SessionControlSwitchBackDelay_Object = MibScalar
sleVrrp6SessionControlSwitchBackDelay = _SleVrrp6SessionControlSwitchBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 15),
    _SleVrrp6SessionControlSwitchBackDelay_Type()
)
sleVrrp6SessionControlSwitchBackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlSwitchBackDelay.setStatus("current")
_SleVrrp6SessionControlVirtualIpVal_Type = OctetString
_SleVrrp6SessionControlVirtualIpVal_Object = MibScalar
sleVrrp6SessionControlVirtualIpVal = _SleVrrp6SessionControlVirtualIpVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 16),
    _SleVrrp6SessionControlVirtualIpVal_Type()
)
sleVrrp6SessionControlVirtualIpVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlVirtualIpVal.setStatus("current")


class _SleVrrp6SessionControlVirtualIpOwner_Type(Integer32):
    """Custom type sleVrrp6SessionControlVirtualIpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("set", 1))
    )


_SleVrrp6SessionControlVirtualIpOwner_Type.__name__ = "Integer32"
_SleVrrp6SessionControlVirtualIpOwner_Object = MibScalar
sleVrrp6SessionControlVirtualIpOwner = _SleVrrp6SessionControlVirtualIpOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 2, 17),
    _SleVrrp6SessionControlVirtualIpOwner_Type()
)
sleVrrp6SessionControlVirtualIpOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessionControlVirtualIpOwner.setStatus("current")
_SleVrrp6SessionNotification_ObjectIdentity = ObjectIdentity
sleVrrp6SessionNotification = _SleVrrp6SessionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 3)
)
_SleVrrp6SessInfoTable_Object = MibTable
sleVrrp6SessInfoTable = _SleVrrp6SessInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4)
)
if mibBuilder.loadTexts:
    sleVrrp6SessInfoTable.setStatus("current")
_SleVrrp6SessInfoEntry_Object = MibTableRow
sleVrrp6SessInfoEntry = _SleVrrp6SessInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1)
)
sleVrrp6SessInfoEntry.setIndexNames(
    (0, "SLE-VRRP-MIB", "sleVrrp6SessInfoVrId"),
    (0, "SLE-VRRP-MIB", "sleVrrp6SessInfoIfIndex"),
)
if mibBuilder.loadTexts:
    sleVrrp6SessInfoEntry.setStatus("current")


class _SleVrrp6SessInfoVrId_Type(Integer32):
    """Custom type sleVrrp6SessInfoVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessInfoVrId_Type.__name__ = "Integer32"
_SleVrrp6SessInfoVrId_Object = MibTableColumn
sleVrrp6SessInfoVrId = _SleVrrp6SessInfoVrId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 1),
    _SleVrrp6SessInfoVrId_Type()
)
sleVrrp6SessInfoVrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoVrId.setStatus("current")


class _SleVrrp6SessInfoIfIndex_Type(Integer32):
    """Custom type sleVrrp6SessInfoIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessInfoIfIndex_Type.__name__ = "Integer32"
_SleVrrp6SessInfoIfIndex_Object = MibTableColumn
sleVrrp6SessInfoIfIndex = _SleVrrp6SessInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 2),
    _SleVrrp6SessInfoIfIndex_Type()
)
sleVrrp6SessInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoIfIndex.setStatus("current")
_SleVrrp6SessInfoVrfName_Type = OctetString
_SleVrrp6SessInfoVrfName_Object = MibTableColumn
sleVrrp6SessInfoVrfName = _SleVrrp6SessInfoVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 3),
    _SleVrrp6SessInfoVrfName_Type()
)
sleVrrp6SessInfoVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoVrfName.setStatus("current")
_SleVrrp6SessInfoVrfFibId_Type = Integer32
_SleVrrp6SessInfoVrfFibId_Object = MibTableColumn
sleVrrp6SessInfoVrfFibId = _SleVrrp6SessInfoVrfFibId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 4),
    _SleVrrp6SessInfoVrfFibId_Type()
)
sleVrrp6SessInfoVrfFibId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoVrfFibId.setStatus("current")


class _SleVrrp6SessInfoSessionAdminState_Type(Integer32):
    """Custom type sleVrrp6SessInfoSessionAdminState based on Integer32"""
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


_SleVrrp6SessInfoSessionAdminState_Type.__name__ = "Integer32"
_SleVrrp6SessInfoSessionAdminState_Object = MibTableColumn
sleVrrp6SessInfoSessionAdminState = _SleVrrp6SessInfoSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 5),
    _SleVrrp6SessInfoSessionAdminState_Type()
)
sleVrrp6SessInfoSessionAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoSessionAdminState.setStatus("current")


class _SleVrrp6SessInfoSessionState_Type(Integer32):
    """Custom type sleVrrp6SessInfoSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("backup", 2),
          ("master", 3))
    )


_SleVrrp6SessInfoSessionState_Type.__name__ = "Integer32"
_SleVrrp6SessInfoSessionState_Object = MibTableColumn
sleVrrp6SessInfoSessionState = _SleVrrp6SessInfoSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 6),
    _SleVrrp6SessInfoSessionState_Type()
)
sleVrrp6SessInfoSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoSessionState.setStatus("current")


class _SleVrrp6SessInfoSessionStateInitMsg_Type(Integer32):
    """Custom type sleVrrp6SessInfoSessionStateInitMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("adminDown", 0),
          ("interfaceNotRunning", 1),
          ("circuitDown", 2),
          ("noSubnet", 3),
          ("virtualIpUnset", 4),
          ("inSwitchBackDelay", 5))
    )


_SleVrrp6SessInfoSessionStateInitMsg_Type.__name__ = "Integer32"
_SleVrrp6SessInfoSessionStateInitMsg_Object = MibTableColumn
sleVrrp6SessInfoSessionStateInitMsg = _SleVrrp6SessInfoSessionStateInitMsg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 7),
    _SleVrrp6SessInfoSessionStateInitMsg_Type()
)
sleVrrp6SessInfoSessionStateInitMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoSessionStateInitMsg.setStatus("current")
_SleVrrp6SessInfoVirtualIp_Type = OctetString
_SleVrrp6SessInfoVirtualIp_Object = MibTableColumn
sleVrrp6SessInfoVirtualIp = _SleVrrp6SessInfoVirtualIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 8),
    _SleVrrp6SessInfoVirtualIp_Type()
)
sleVrrp6SessInfoVirtualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoVirtualIp.setStatus("current")


class _SleVrrp6SessInfoVirtualIpOwner_Type(Integer32):
    """Custom type sleVrrp6SessInfoVirtualIpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("set", 1))
    )


_SleVrrp6SessInfoVirtualIpOwner_Type.__name__ = "Integer32"
_SleVrrp6SessInfoVirtualIpOwner_Object = MibTableColumn
sleVrrp6SessInfoVirtualIpOwner = _SleVrrp6SessInfoVirtualIpOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 9),
    _SleVrrp6SessInfoVirtualIpOwner_Type()
)
sleVrrp6SessInfoVirtualIpOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoVirtualIpOwner.setStatus("current")
_SleVrrp6SessInfoConfiguredPriority_Type = Integer32
_SleVrrp6SessInfoConfiguredPriority_Object = MibTableColumn
sleVrrp6SessInfoConfiguredPriority = _SleVrrp6SessInfoConfiguredPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 10),
    _SleVrrp6SessInfoConfiguredPriority_Type()
)
sleVrrp6SessInfoConfiguredPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoConfiguredPriority.setStatus("current")
_SleVrrp6SessInfoCurrentPriority_Type = Integer32
_SleVrrp6SessInfoCurrentPriority_Object = MibTableColumn
sleVrrp6SessInfoCurrentPriority = _SleVrrp6SessInfoCurrentPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 11),
    _SleVrrp6SessInfoCurrentPriority_Type()
)
sleVrrp6SessInfoCurrentPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoCurrentPriority.setStatus("current")
_SleVrrp6SessInfoSwitchBackDelay_Type = Integer32
_SleVrrp6SessInfoSwitchBackDelay_Object = MibTableColumn
sleVrrp6SessInfoSwitchBackDelay = _SleVrrp6SessInfoSwitchBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 12),
    _SleVrrp6SessInfoSwitchBackDelay_Type()
)
sleVrrp6SessInfoSwitchBackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoSwitchBackDelay.setStatus("current")


class _SleVrrp6SessInfoAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp6SessInfoAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SleVrrp6SessInfoAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp6SessInfoAdvertisementInterval_Object = MibTableColumn
sleVrrp6SessInfoAdvertisementInterval = _SleVrrp6SessInfoAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 13),
    _SleVrrp6SessInfoAdvertisementInterval_Type()
)
sleVrrp6SessInfoAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoAdvertisementInterval.setStatus("current")


class _SleVrrp6SessInfoMasterAdvertisementInterval_Type(Integer32):
    """Custom type sleVrrp6SessInfoMasterAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SleVrrp6SessInfoMasterAdvertisementInterval_Type.__name__ = "Integer32"
_SleVrrp6SessInfoMasterAdvertisementInterval_Object = MibTableColumn
sleVrrp6SessInfoMasterAdvertisementInterval = _SleVrrp6SessInfoMasterAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 14),
    _SleVrrp6SessInfoMasterAdvertisementInterval_Type()
)
sleVrrp6SessInfoMasterAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoMasterAdvertisementInterval.setStatus("current")
_SleVrrp6SessInfoSkewTime_Type = Integer32
_SleVrrp6SessInfoSkewTime_Object = MibTableColumn
sleVrrp6SessInfoSkewTime = _SleVrrp6SessInfoSkewTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 15),
    _SleVrrp6SessInfoSkewTime_Type()
)
sleVrrp6SessInfoSkewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoSkewTime.setStatus("current")


class _SleVrrp6SessInfoAcceptMode_Type(Integer32):
    """Custom type sleVrrp6SessInfoAcceptMode based on Integer32"""
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


_SleVrrp6SessInfoAcceptMode_Type.__name__ = "Integer32"
_SleVrrp6SessInfoAcceptMode_Object = MibTableColumn
sleVrrp6SessInfoAcceptMode = _SleVrrp6SessInfoAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 16),
    _SleVrrp6SessInfoAcceptMode_Type()
)
sleVrrp6SessInfoAcceptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoAcceptMode.setStatus("current")


class _SleVrrp6SessInfoPreemptMode_Type(Integer32):
    """Custom type sleVrrp6SessInfoPreemptMode based on Integer32"""
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


_SleVrrp6SessInfoPreemptMode_Type.__name__ = "Integer32"
_SleVrrp6SessInfoPreemptMode_Object = MibTableColumn
sleVrrp6SessInfoPreemptMode = _SleVrrp6SessInfoPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 17),
    _SleVrrp6SessInfoPreemptMode_Type()
)
sleVrrp6SessInfoPreemptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoPreemptMode.setStatus("current")
_SleVrrp6SessInfoMonitorCircuitIfIndex_Type = Integer32
_SleVrrp6SessInfoMonitorCircuitIfIndex_Object = MibTableColumn
sleVrrp6SessInfoMonitorCircuitIfIndex = _SleVrrp6SessInfoMonitorCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 18),
    _SleVrrp6SessInfoMonitorCircuitIfIndex_Type()
)
sleVrrp6SessInfoMonitorCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoMonitorCircuitIfIndex.setStatus("current")


class _SleVrrp6SessInfoMonitorCircuitPrioDelta_Type(Integer32):
    """Custom type sleVrrp6SessInfoMonitorCircuitPrioDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 253),
    )


_SleVrrp6SessInfoMonitorCircuitPrioDelta_Type.__name__ = "Integer32"
_SleVrrp6SessInfoMonitorCircuitPrioDelta_Object = MibTableColumn
sleVrrp6SessInfoMonitorCircuitPrioDelta = _SleVrrp6SessInfoMonitorCircuitPrioDelta_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 19),
    _SleVrrp6SessInfoMonitorCircuitPrioDelta_Type()
)
sleVrrp6SessInfoMonitorCircuitPrioDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoMonitorCircuitPrioDelta.setStatus("current")


class _SleVrrp6SessInfoMonitorCircuitState_Type(Integer32):
    """Custom type sleVrrp6SessInfoMonitorCircuitState based on Integer32"""
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


_SleVrrp6SessInfoMonitorCircuitState_Type.__name__ = "Integer32"
_SleVrrp6SessInfoMonitorCircuitState_Object = MibTableColumn
sleVrrp6SessInfoMonitorCircuitState = _SleVrrp6SessInfoMonitorCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 20),
    _SleVrrp6SessInfoMonitorCircuitState_Type()
)
sleVrrp6SessInfoMonitorCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoMonitorCircuitState.setStatus("current")


class _SleVrrp6SessInfoMulticastMembershipOn_Type(Integer32):
    """Custom type sleVrrp6SessInfoMulticastMembershipOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joined", 1),
          ("left", 2))
    )


_SleVrrp6SessInfoMulticastMembershipOn_Type.__name__ = "Integer32"
_SleVrrp6SessInfoMulticastMembershipOn_Object = MibTableColumn
sleVrrp6SessInfoMulticastMembershipOn = _SleVrrp6SessInfoMulticastMembershipOn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 21),
    _SleVrrp6SessInfoMulticastMembershipOn_Type()
)
sleVrrp6SessInfoMulticastMembershipOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoMulticastMembershipOn.setStatus("current")


class _SleVrrp6SessInfoCompatibleV2_Type(Integer32):
    """Custom type sleVrrp6SessInfoCompatibleV2 based on Integer32"""
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


_SleVrrp6SessInfoCompatibleV2_Type.__name__ = "Integer32"
_SleVrrp6SessInfoCompatibleV2_Object = MibTableColumn
sleVrrp6SessInfoCompatibleV2 = _SleVrrp6SessInfoCompatibleV2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 4, 1, 22),
    _SleVrrp6SessInfoCompatibleV2_Type()
)
sleVrrp6SessInfoCompatibleV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessInfoCompatibleV2.setStatus("current")
_SleVrrp6SessStatTable_Object = MibTable
sleVrrp6SessStatTable = _SleVrrp6SessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5)
)
if mibBuilder.loadTexts:
    sleVrrp6SessStatTable.setStatus("current")
_SleVrrp6SessStatEntry_Object = MibTableRow
sleVrrp6SessStatEntry = _SleVrrp6SessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1)
)
sleVrrp6SessStatEntry.setIndexNames(
    (0, "SLE-VRRP-MIB", "sleVrrp6SessStatVrid"),
    (0, "SLE-VRRP-MIB", "sleVrrp6SessStatIfIndex"),
)
if mibBuilder.loadTexts:
    sleVrrp6SessStatEntry.setStatus("current")


class _SleVrrp6SessStatVrid_Type(Integer32):
    """Custom type sleVrrp6SessStatVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessStatVrid_Type.__name__ = "Integer32"
_SleVrrp6SessStatVrid_Object = MibTableColumn
sleVrrp6SessStatVrid = _SleVrrp6SessStatVrid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 1),
    _SleVrrp6SessStatVrid_Type()
)
sleVrrp6SessStatVrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVrrp6SessStatVrid.setStatus("current")


class _SleVrrp6SessStatIfIndex_Type(Integer32):
    """Custom type sleVrrp6SessStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleVrrp6SessStatIfIndex_Type.__name__ = "Integer32"
_SleVrrp6SessStatIfIndex_Object = MibTableColumn
sleVrrp6SessStatIfIndex = _SleVrrp6SessStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 2),
    _SleVrrp6SessStatIfIndex_Type()
)
sleVrrp6SessStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatIfIndex.setStatus("current")
_SleVrrp6SessStatChecksumErrors_Type = Counter32
_SleVrrp6SessStatChecksumErrors_Object = MibTableColumn
sleVrrp6SessStatChecksumErrors = _SleVrrp6SessStatChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 3),
    _SleVrrp6SessStatChecksumErrors_Type()
)
sleVrrp6SessStatChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatChecksumErrors.setStatus("current")
_SleVrrp6SessStatVersionErrors_Type = Counter32
_SleVrrp6SessStatVersionErrors_Object = MibTableColumn
sleVrrp6SessStatVersionErrors = _SleVrrp6SessStatVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 4),
    _SleVrrp6SessStatVersionErrors_Type()
)
sleVrrp6SessStatVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatVersionErrors.setStatus("current")
_SleVrrp6SessStatVridErrors_Type = Counter32
_SleVrrp6SessStatVridErrors_Object = MibTableColumn
sleVrrp6SessStatVridErrors = _SleVrrp6SessStatVridErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 5),
    _SleVrrp6SessStatVridErrors_Type()
)
sleVrrp6SessStatVridErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatVridErrors.setStatus("current")
_SleVrrp6SessStatMasterTransitions_Type = Counter32
_SleVrrp6SessStatMasterTransitions_Object = MibTableColumn
sleVrrp6SessStatMasterTransitions = _SleVrrp6SessStatMasterTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 6),
    _SleVrrp6SessStatMasterTransitions_Type()
)
sleVrrp6SessStatMasterTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatMasterTransitions.setStatus("current")
_SleVrrp6SessStatAdvertisementsRcvd_Type = Counter32
_SleVrrp6SessStatAdvertisementsRcvd_Object = MibTableColumn
sleVrrp6SessStatAdvertisementsRcvd = _SleVrrp6SessStatAdvertisementsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 7),
    _SleVrrp6SessStatAdvertisementsRcvd_Type()
)
sleVrrp6SessStatAdvertisementsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatAdvertisementsRcvd.setStatus("current")
_SleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors_Type = Counter32
_SleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors = _SleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 8),
    _SleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors_Type()
)
sleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors.setStatus("current")
_SleVrrp6SessStatPktsRcvdIpTtlErros_Type = Counter32
_SleVrrp6SessStatPktsRcvdIpTtlErros_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdIpTtlErros = _SleVrrp6SessStatPktsRcvdIpTtlErros_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 9),
    _SleVrrp6SessStatPktsRcvdIpTtlErros_Type()
)
sleVrrp6SessStatPktsRcvdIpTtlErros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdIpTtlErros.setStatus("current")
_SleVrrp6SessStatPktsRcvdZeroPriority_Type = Counter32
_SleVrrp6SessStatPktsRcvdZeroPriority_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdZeroPriority = _SleVrrp6SessStatPktsRcvdZeroPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 10),
    _SleVrrp6SessStatPktsRcvdZeroPriority_Type()
)
sleVrrp6SessStatPktsRcvdZeroPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdZeroPriority.setStatus("current")
_SleVrrp6SessStatPktsSentZeroPriority_Type = Counter32
_SleVrrp6SessStatPktsSentZeroPriority_Object = MibTableColumn
sleVrrp6SessStatPktsSentZeroPriority = _SleVrrp6SessStatPktsSentZeroPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 11),
    _SleVrrp6SessStatPktsSentZeroPriority_Type()
)
sleVrrp6SessStatPktsSentZeroPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsSentZeroPriority.setStatus("current")
_SleVrrp6SessStatPktsRcvdInvalidType_Type = Counter32
_SleVrrp6SessStatPktsRcvdInvalidType_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdInvalidType = _SleVrrp6SessStatPktsRcvdInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 12),
    _SleVrrp6SessStatPktsRcvdInvalidType_Type()
)
sleVrrp6SessStatPktsRcvdInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdInvalidType.setStatus("current")
_SleVrrp6SessStatPktsRcvdAddressListErrors_Type = Counter32
_SleVrrp6SessStatPktsRcvdAddressListErrors_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdAddressListErrors = _SleVrrp6SessStatPktsRcvdAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 13),
    _SleVrrp6SessStatPktsRcvdAddressListErrors_Type()
)
sleVrrp6SessStatPktsRcvdAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdAddressListErrors.setStatus("current")
_SleVrrp6SessStatPktsRcvdPacketLengthErrors_Type = Counter32
_SleVrrp6SessStatPktsRcvdPacketLengthErrors_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdPacketLengthErrors = _SleVrrp6SessStatPktsRcvdPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 14),
    _SleVrrp6SessStatPktsRcvdPacketLengthErrors_Type()
)
sleVrrp6SessStatPktsRcvdPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdPacketLengthErrors.setStatus("current")
_SleVrrp6SessStatPktsRcvdUnknownAuthenticationType_Type = Counter32
_SleVrrp6SessStatPktsRcvdUnknownAuthenticationType_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdUnknownAuthenticationType = _SleVrrp6SessStatPktsRcvdUnknownAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 15),
    _SleVrrp6SessStatPktsRcvdUnknownAuthenticationType_Type()
)
sleVrrp6SessStatPktsRcvdUnknownAuthenticationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdUnknownAuthenticationType.setStatus("current")
_SleVrrp6SessStatPktsRcvdIpCountMismatch_Type = Counter32
_SleVrrp6SessStatPktsRcvdIpCountMismatch_Object = MibTableColumn
sleVrrp6SessStatPktsRcvdIpCountMismatch = _SleVrrp6SessStatPktsRcvdIpCountMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 16),
    _SleVrrp6SessStatPktsRcvdIpCountMismatch_Type()
)
sleVrrp6SessStatPktsRcvdIpCountMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatPktsRcvdIpCountMismatch.setStatus("current")
_SleVrrp6SessStatDiscontinuityTime_Type = OctetString
_SleVrrp6SessStatDiscontinuityTime_Object = MibTableColumn
sleVrrp6SessStatDiscontinuityTime = _SleVrrp6SessStatDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 17),
    _SleVrrp6SessStatDiscontinuityTime_Type()
)
sleVrrp6SessStatDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatDiscontinuityTime.setStatus("current")
_SleVrrp6SessStatRefreshRate_Type = Integer32
_SleVrrp6SessStatRefreshRate_Object = MibTableColumn
sleVrrp6SessStatRefreshRate = _SleVrrp6SessStatRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 2, 2, 5, 1, 18),
    _SleVrrp6SessStatRefreshRate_Type()
)
sleVrrp6SessStatRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVrrp6SessStatRefreshRate.setStatus("current")

# Managed Objects groups

sleISISGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 57, 5)
)
sleISISGroup.setObjects(
      *(("SLE-VRRP-MIB", "sleVrrpBaseInfoCompatibleV2"),
        ("SLE-VRRP-MIB", "sleVrrpBaseInfoVMac"),
        ("SLE-VRRP-MIB", "sleVrrpBaseInfoDelegate"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlRequest"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlStatus"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlTimer"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlTimeStamp"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlReqResult"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlCompatibleV2"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlVMac"),
        ("SLE-VRRP-MIB", "sleVrrpBaseControlDelegate"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionVrId"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionStatus"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionAcceptMode"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionCircuitFailOverIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionCircuitFailOverPriorityDelta"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionPreemptMode"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionPriority"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionSwitchBackDelay"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionVirtualIpVal"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionVirtualIpOwner"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionCompatibleV2"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlRequest"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlStatus"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlTimer"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlTimeStamp"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlReqResult"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlVrId"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlSessionStatus"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlAcceptMode"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlCircuitFailOverIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlCircuitFailOverPriorityDelta"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlPreemptMode"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlPriority"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlSwitchBackDelay"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlVirtualIpVal"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlVirtualIpOwner"),
        ("SLE-VRRP-MIB", "sleVrrp4SessionControlCompatibleV2"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionVrId"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionStatus"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionAcceptMode"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionCircuitFailOverIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionCircuitFailOverPriorityDelta"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionPreemptMode"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionPriority"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionSwitchBackDelay"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionVirtualIpVal"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionVirtualIpOwner"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlRequest"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlStatus"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlTimer"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlTimeStamp"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlReqResult"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlVrId"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlSessionStatus"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlAcceptMode"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlCircuitFailOverIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlCircuitFailOverPriorityDelta"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlPreemptMode"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlPriority"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlSwitchBackDelay"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlVirtualIpVal"),
        ("SLE-VRRP-MIB", "sleVrrp6SessionControlVirtualIpOwner"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoVrId"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoVrfName"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoVrfFibId"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoSessionAdminState"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoSessionState"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoVirtualIp"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoVirtualIpOwner"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoConfiguredPriority"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoCurrentPriority"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoSwitchBackDelay"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoMasterAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoSkewTime"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoAcceptMode"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoPreemptMode"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoMonitorCircuitIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoMonitorCircuitPrioDelta"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoMonitorCircuitState"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoMulticastMembershipOn"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatVrid"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatChecksumErrors"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatVersionErrors"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatVridErrors"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatMasterTransitions"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatAdvertisementsRcvd"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdIpTtlErros"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdZeroPriority"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsSentZeroPriority"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdInvalidType"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdAddressListErrors"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdPacketLengthErrors"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdUnknownAuthenticationType"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatPktsRcvdIpCountMismatch"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatDiscontinuityTime"),
        ("SLE-VRRP-MIB", "sleVrrp4SessStatRefreshRate"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatVrid"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatChecksumErrors"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatVersionErrors"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatVridErrors"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatMasterTransitions"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatAdvertisementsRcvd"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdIpTtlErros"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdZeroPriority"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsSentZeroPriority"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdInvalidType"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdAddressListErrors"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdPacketLengthErrors"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdUnknownAuthenticationType"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatPktsRcvdIpCountMismatch"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatDiscontinuityTime"),
        ("SLE-VRRP-MIB", "sleVrrp6SessStatRefreshRate"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoCompatibleV2"),
        ("SLE-VRRP-MIB", "sleVrrp4SessInfoSessionStateInitMsg"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoVrId"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoVrfName"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoVrfFibId"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoSessionAdminState"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoSessionState"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoSessionStateInitMsg"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoVirtualIp"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoVirtualIpOwner"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoConfiguredPriority"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoCurrentPriority"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoSwitchBackDelay"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoMasterAdvertisementInterval"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoSkewTime"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoAcceptMode"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoPreemptMode"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoMonitorCircuitIfIndex"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoMonitorCircuitPrioDelta"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoMonitorCircuitState"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoMulticastMembershipOn"),
        ("SLE-VRRP-MIB", "sleVrrp6SessInfoCompatibleV2"))
)
if mibBuilder.loadTexts:
    sleISISGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-VRRP-MIB",
    **{"sleVRRP": sleVRRP,
       "sleVrrpBase": sleVrrpBase,
       "sleVrrpBaseInfo": sleVrrpBaseInfo,
       "sleVrrpBaseInfoCompatibleV2": sleVrrpBaseInfoCompatibleV2,
       "sleVrrpBaseInfoVMac": sleVrrpBaseInfoVMac,
       "sleVrrpBaseInfoDelegate": sleVrrpBaseInfoDelegate,
       "sleVrrpBaseControl": sleVrrpBaseControl,
       "sleVrrpBaseControlRequest": sleVrrpBaseControlRequest,
       "sleVrrpBaseControlStatus": sleVrrpBaseControlStatus,
       "sleVrrpBaseControlTimer": sleVrrpBaseControlTimer,
       "sleVrrpBaseControlTimeStamp": sleVrrpBaseControlTimeStamp,
       "sleVrrpBaseControlReqResult": sleVrrpBaseControlReqResult,
       "sleVrrpBaseControlCompatibleV2": sleVrrpBaseControlCompatibleV2,
       "sleVrrpBaseControlVMac": sleVrrpBaseControlVMac,
       "sleVrrpBaseControlDelegate": sleVrrpBaseControlDelegate,
       "sleVrrpSess": sleVrrpSess,
       "sleVrrp4Session": sleVrrp4Session,
       "sleVrrp4SessionTable": sleVrrp4SessionTable,
       "sleVrrp4SessionEntry": sleVrrp4SessionEntry,
       "sleVrrp4SessionVrId": sleVrrp4SessionVrId,
       "sleVrrp4SessionIfIndex": sleVrrp4SessionIfIndex,
       "sleVrrp4SessionStatus": sleVrrp4SessionStatus,
       "sleVrrp4SessionAcceptMode": sleVrrp4SessionAcceptMode,
       "sleVrrp4SessionAdvertisementInterval": sleVrrp4SessionAdvertisementInterval,
       "sleVrrp4SessionCircuitFailOverIfIndex": sleVrrp4SessionCircuitFailOverIfIndex,
       "sleVrrp4SessionCircuitFailOverPriorityDelta": sleVrrp4SessionCircuitFailOverPriorityDelta,
       "sleVrrp4SessionPreemptMode": sleVrrp4SessionPreemptMode,
       "sleVrrp4SessionPriority": sleVrrp4SessionPriority,
       "sleVrrp4SessionSwitchBackDelay": sleVrrp4SessionSwitchBackDelay,
       "sleVrrp4SessionVirtualIpVal": sleVrrp4SessionVirtualIpVal,
       "sleVrrp4SessionVirtualIpOwner": sleVrrp4SessionVirtualIpOwner,
       "sleVrrp4SessionCompatibleV2": sleVrrp4SessionCompatibleV2,
       "sleVrrp4SessionControl": sleVrrp4SessionControl,
       "sleVrrp4SessionControlRequest": sleVrrp4SessionControlRequest,
       "sleVrrp4SessionControlStatus": sleVrrp4SessionControlStatus,
       "sleVrrp4SessionControlTimer": sleVrrp4SessionControlTimer,
       "sleVrrp4SessionControlTimeStamp": sleVrrp4SessionControlTimeStamp,
       "sleVrrp4SessionControlReqResult": sleVrrp4SessionControlReqResult,
       "sleVrrp4SessionControlVrId": sleVrrp4SessionControlVrId,
       "sleVrrp4SessionControlIfIndex": sleVrrp4SessionControlIfIndex,
       "sleVrrp4SessionControlSessionStatus": sleVrrp4SessionControlSessionStatus,
       "sleVrrp4SessionControlAcceptMode": sleVrrp4SessionControlAcceptMode,
       "sleVrrp4SessionControlAdvertisementInterval": sleVrrp4SessionControlAdvertisementInterval,
       "sleVrrp4SessionControlCircuitFailOverIfIndex": sleVrrp4SessionControlCircuitFailOverIfIndex,
       "sleVrrp4SessionControlCircuitFailOverPriorityDelta": sleVrrp4SessionControlCircuitFailOverPriorityDelta,
       "sleVrrp4SessionControlPreemptMode": sleVrrp4SessionControlPreemptMode,
       "sleVrrp4SessionControlPriority": sleVrrp4SessionControlPriority,
       "sleVrrp4SessionControlSwitchBackDelay": sleVrrp4SessionControlSwitchBackDelay,
       "sleVrrp4SessionControlVirtualIpVal": sleVrrp4SessionControlVirtualIpVal,
       "sleVrrp4SessionControlVirtualIpOwner": sleVrrp4SessionControlVirtualIpOwner,
       "sleVrrp4SessionControlCompatibleV2": sleVrrp4SessionControlCompatibleV2,
       "sleVrrp4SessionNotification": sleVrrp4SessionNotification,
       "sleVrrp4SessInfoTable": sleVrrp4SessInfoTable,
       "sleVrrp4SessInfoEntry": sleVrrp4SessInfoEntry,
       "sleVrrp4SessInfoVrId": sleVrrp4SessInfoVrId,
       "sleVrrp4SessInfoIfIndex": sleVrrp4SessInfoIfIndex,
       "sleVrrp4SessInfoVrfName": sleVrrp4SessInfoVrfName,
       "sleVrrp4SessInfoVrfFibId": sleVrrp4SessInfoVrfFibId,
       "sleVrrp4SessInfoSessionAdminState": sleVrrp4SessInfoSessionAdminState,
       "sleVrrp4SessInfoSessionState": sleVrrp4SessInfoSessionState,
       "sleVrrp4SessInfoSessionStateInitMsg": sleVrrp4SessInfoSessionStateInitMsg,
       "sleVrrp4SessInfoVirtualIp": sleVrrp4SessInfoVirtualIp,
       "sleVrrp4SessInfoVirtualIpOwner": sleVrrp4SessInfoVirtualIpOwner,
       "sleVrrp4SessInfoConfiguredPriority": sleVrrp4SessInfoConfiguredPriority,
       "sleVrrp4SessInfoCurrentPriority": sleVrrp4SessInfoCurrentPriority,
       "sleVrrp4SessInfoSwitchBackDelay": sleVrrp4SessInfoSwitchBackDelay,
       "sleVrrp4SessInfoAdvertisementInterval": sleVrrp4SessInfoAdvertisementInterval,
       "sleVrrp4SessInfoMasterAdvertisementInterval": sleVrrp4SessInfoMasterAdvertisementInterval,
       "sleVrrp4SessInfoSkewTime": sleVrrp4SessInfoSkewTime,
       "sleVrrp4SessInfoAcceptMode": sleVrrp4SessInfoAcceptMode,
       "sleVrrp4SessInfoPreemptMode": sleVrrp4SessInfoPreemptMode,
       "sleVrrp4SessInfoMonitorCircuitIfIndex": sleVrrp4SessInfoMonitorCircuitIfIndex,
       "sleVrrp4SessInfoMonitorCircuitPrioDelta": sleVrrp4SessInfoMonitorCircuitPrioDelta,
       "sleVrrp4SessInfoMonitorCircuitState": sleVrrp4SessInfoMonitorCircuitState,
       "sleVrrp4SessInfoMulticastMembershipOn": sleVrrp4SessInfoMulticastMembershipOn,
       "sleVrrp4SessInfoCompatibleV2": sleVrrp4SessInfoCompatibleV2,
       "sleVrrp4SessStatTable": sleVrrp4SessStatTable,
       "sleVrrp4SessStatEntry": sleVrrp4SessStatEntry,
       "sleVrrp4SessStatVrid": sleVrrp4SessStatVrid,
       "sleVrrp4SessStatIfIndex": sleVrrp4SessStatIfIndex,
       "sleVrrp4SessStatChecksumErrors": sleVrrp4SessStatChecksumErrors,
       "sleVrrp4SessStatVersionErrors": sleVrrp4SessStatVersionErrors,
       "sleVrrp4SessStatVridErrors": sleVrrp4SessStatVridErrors,
       "sleVrrp4SessStatMasterTransitions": sleVrrp4SessStatMasterTransitions,
       "sleVrrp4SessStatAdvertisementsRcvd": sleVrrp4SessStatAdvertisementsRcvd,
       "sleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors": sleVrrp4SessStatPktsRcvdAdvertisementIntervalErrors,
       "sleVrrp4SessStatPktsRcvdIpTtlErros": sleVrrp4SessStatPktsRcvdIpTtlErros,
       "sleVrrp4SessStatPktsRcvdZeroPriority": sleVrrp4SessStatPktsRcvdZeroPriority,
       "sleVrrp4SessStatPktsSentZeroPriority": sleVrrp4SessStatPktsSentZeroPriority,
       "sleVrrp4SessStatPktsRcvdInvalidType": sleVrrp4SessStatPktsRcvdInvalidType,
       "sleVrrp4SessStatPktsRcvdAddressListErrors": sleVrrp4SessStatPktsRcvdAddressListErrors,
       "sleVrrp4SessStatPktsRcvdPacketLengthErrors": sleVrrp4SessStatPktsRcvdPacketLengthErrors,
       "sleVrrp4SessStatPktsRcvdUnknownAuthenticationType": sleVrrp4SessStatPktsRcvdUnknownAuthenticationType,
       "sleVrrp4SessStatPktsRcvdIpCountMismatch": sleVrrp4SessStatPktsRcvdIpCountMismatch,
       "sleVrrp4SessStatDiscontinuityTime": sleVrrp4SessStatDiscontinuityTime,
       "sleVrrp4SessStatRefreshRate": sleVrrp4SessStatRefreshRate,
       "sleVrrp6Session": sleVrrp6Session,
       "sleVrrp6SessionTable": sleVrrp6SessionTable,
       "sleVrrp6SessionEntry": sleVrrp6SessionEntry,
       "sleVrrp6SessionVrId": sleVrrp6SessionVrId,
       "sleVrrp6SessionIfIndex": sleVrrp6SessionIfIndex,
       "sleVrrp6SessionStatus": sleVrrp6SessionStatus,
       "sleVrrp6SessionAcceptMode": sleVrrp6SessionAcceptMode,
       "sleVrrp6SessionAdvertisementInterval": sleVrrp6SessionAdvertisementInterval,
       "sleVrrp6SessionCircuitFailOverIfIndex": sleVrrp6SessionCircuitFailOverIfIndex,
       "sleVrrp6SessionCircuitFailOverPriorityDelta": sleVrrp6SessionCircuitFailOverPriorityDelta,
       "sleVrrp6SessionPreemptMode": sleVrrp6SessionPreemptMode,
       "sleVrrp6SessionPriority": sleVrrp6SessionPriority,
       "sleVrrp6SessionSwitchBackDelay": sleVrrp6SessionSwitchBackDelay,
       "sleVrrp6SessionVirtualIpVal": sleVrrp6SessionVirtualIpVal,
       "sleVrrp6SessionVirtualIpOwner": sleVrrp6SessionVirtualIpOwner,
       "sleVrrp6SessionControl": sleVrrp6SessionControl,
       "sleVrrp6SessionControlRequest": sleVrrp6SessionControlRequest,
       "sleVrrp6SessionControlStatus": sleVrrp6SessionControlStatus,
       "sleVrrp6SessionControlTimer": sleVrrp6SessionControlTimer,
       "sleVrrp6SessionControlTimeStamp": sleVrrp6SessionControlTimeStamp,
       "sleVrrp6SessionControlReqResult": sleVrrp6SessionControlReqResult,
       "sleVrrp6SessionControlVrId": sleVrrp6SessionControlVrId,
       "sleVrrp6SessionControlIfIndex": sleVrrp6SessionControlIfIndex,
       "sleVrrp6SessionControlSessionStatus": sleVrrp6SessionControlSessionStatus,
       "sleVrrp6SessionControlAcceptMode": sleVrrp6SessionControlAcceptMode,
       "sleVrrp6SessionControlAdvertisementInterval": sleVrrp6SessionControlAdvertisementInterval,
       "sleVrrp6SessionControlCircuitFailOverIfIndex": sleVrrp6SessionControlCircuitFailOverIfIndex,
       "sleVrrp6SessionControlCircuitFailOverPriorityDelta": sleVrrp6SessionControlCircuitFailOverPriorityDelta,
       "sleVrrp6SessionControlPreemptMode": sleVrrp6SessionControlPreemptMode,
       "sleVrrp6SessionControlPriority": sleVrrp6SessionControlPriority,
       "sleVrrp6SessionControlSwitchBackDelay": sleVrrp6SessionControlSwitchBackDelay,
       "sleVrrp6SessionControlVirtualIpVal": sleVrrp6SessionControlVirtualIpVal,
       "sleVrrp6SessionControlVirtualIpOwner": sleVrrp6SessionControlVirtualIpOwner,
       "sleVrrp6SessionNotification": sleVrrp6SessionNotification,
       "sleVrrp6SessInfoTable": sleVrrp6SessInfoTable,
       "sleVrrp6SessInfoEntry": sleVrrp6SessInfoEntry,
       "sleVrrp6SessInfoVrId": sleVrrp6SessInfoVrId,
       "sleVrrp6SessInfoIfIndex": sleVrrp6SessInfoIfIndex,
       "sleVrrp6SessInfoVrfName": sleVrrp6SessInfoVrfName,
       "sleVrrp6SessInfoVrfFibId": sleVrrp6SessInfoVrfFibId,
       "sleVrrp6SessInfoSessionAdminState": sleVrrp6SessInfoSessionAdminState,
       "sleVrrp6SessInfoSessionState": sleVrrp6SessInfoSessionState,
       "sleVrrp6SessInfoSessionStateInitMsg": sleVrrp6SessInfoSessionStateInitMsg,
       "sleVrrp6SessInfoVirtualIp": sleVrrp6SessInfoVirtualIp,
       "sleVrrp6SessInfoVirtualIpOwner": sleVrrp6SessInfoVirtualIpOwner,
       "sleVrrp6SessInfoConfiguredPriority": sleVrrp6SessInfoConfiguredPriority,
       "sleVrrp6SessInfoCurrentPriority": sleVrrp6SessInfoCurrentPriority,
       "sleVrrp6SessInfoSwitchBackDelay": sleVrrp6SessInfoSwitchBackDelay,
       "sleVrrp6SessInfoAdvertisementInterval": sleVrrp6SessInfoAdvertisementInterval,
       "sleVrrp6SessInfoMasterAdvertisementInterval": sleVrrp6SessInfoMasterAdvertisementInterval,
       "sleVrrp6SessInfoSkewTime": sleVrrp6SessInfoSkewTime,
       "sleVrrp6SessInfoAcceptMode": sleVrrp6SessInfoAcceptMode,
       "sleVrrp6SessInfoPreemptMode": sleVrrp6SessInfoPreemptMode,
       "sleVrrp6SessInfoMonitorCircuitIfIndex": sleVrrp6SessInfoMonitorCircuitIfIndex,
       "sleVrrp6SessInfoMonitorCircuitPrioDelta": sleVrrp6SessInfoMonitorCircuitPrioDelta,
       "sleVrrp6SessInfoMonitorCircuitState": sleVrrp6SessInfoMonitorCircuitState,
       "sleVrrp6SessInfoMulticastMembershipOn": sleVrrp6SessInfoMulticastMembershipOn,
       "sleVrrp6SessInfoCompatibleV2": sleVrrp6SessInfoCompatibleV2,
       "sleVrrp6SessStatTable": sleVrrp6SessStatTable,
       "sleVrrp6SessStatEntry": sleVrrp6SessStatEntry,
       "sleVrrp6SessStatVrid": sleVrrp6SessStatVrid,
       "sleVrrp6SessStatIfIndex": sleVrrp6SessStatIfIndex,
       "sleVrrp6SessStatChecksumErrors": sleVrrp6SessStatChecksumErrors,
       "sleVrrp6SessStatVersionErrors": sleVrrp6SessStatVersionErrors,
       "sleVrrp6SessStatVridErrors": sleVrrp6SessStatVridErrors,
       "sleVrrp6SessStatMasterTransitions": sleVrrp6SessStatMasterTransitions,
       "sleVrrp6SessStatAdvertisementsRcvd": sleVrrp6SessStatAdvertisementsRcvd,
       "sleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors": sleVrrp6SessStatPktsRcvdAdvertisementIntervalErrors,
       "sleVrrp6SessStatPktsRcvdIpTtlErros": sleVrrp6SessStatPktsRcvdIpTtlErros,
       "sleVrrp6SessStatPktsRcvdZeroPriority": sleVrrp6SessStatPktsRcvdZeroPriority,
       "sleVrrp6SessStatPktsSentZeroPriority": sleVrrp6SessStatPktsSentZeroPriority,
       "sleVrrp6SessStatPktsRcvdInvalidType": sleVrrp6SessStatPktsRcvdInvalidType,
       "sleVrrp6SessStatPktsRcvdAddressListErrors": sleVrrp6SessStatPktsRcvdAddressListErrors,
       "sleVrrp6SessStatPktsRcvdPacketLengthErrors": sleVrrp6SessStatPktsRcvdPacketLengthErrors,
       "sleVrrp6SessStatPktsRcvdUnknownAuthenticationType": sleVrrp6SessStatPktsRcvdUnknownAuthenticationType,
       "sleVrrp6SessStatPktsRcvdIpCountMismatch": sleVrrp6SessStatPktsRcvdIpCountMismatch,
       "sleVrrp6SessStatDiscontinuityTime": sleVrrp6SessStatDiscontinuityTime,
       "sleVrrp6SessStatRefreshRate": sleVrrp6SessStatRefreshRate,
       "sleISISGroup": sleISISGroup}
)
