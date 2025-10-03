# SNMP MIB module (CISCOSB-IP-SLA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-IP-SLA
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:50 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

rlSLA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231)
)
if mibBuilder.loadTexts:
    rlSLA.setRevisions(
        ("2016-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlSLAOperTable_Object = MibTable
rlSLAOperTable = _RlSLAOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1)
)
if mibBuilder.loadTexts:
    rlSLAOperTable.setStatus("current")
_RlSLAOperEntry_Object = MibTableRow
rlSLAOperEntry = _RlSLAOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1)
)
rlSLAOperEntry.setIndexNames(
    (0, "CISCOSB-IP-SLA", "rlSLAOperId"),
)
if mibBuilder.loadTexts:
    rlSLAOperEntry.setStatus("current")
_RlSLAOperId_Type = Unsigned32
_RlSLAOperId_Object = MibTableColumn
rlSLAOperId = _RlSLAOperId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 1),
    _RlSLAOperId_Type()
)
rlSLAOperId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSLAOperId.setStatus("current")


class _RlSLAOperType_Type(Integer32):
    """Custom type rlSLAOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("icmp-echo", 1)
    )


_RlSLAOperType_Type.__name__ = "Integer32"
_RlSLAOperType_Object = MibTableColumn
rlSLAOperType = _RlSLAOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 2),
    _RlSLAOperType_Type()
)
rlSLAOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperType.setStatus("current")


class _RlSLAOperState_Type(Integer32):
    """Custom type rlSLAOperState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pending", 0),
          ("scheduled", 1))
    )


_RlSLAOperState_Type.__name__ = "Integer32"
_RlSLAOperState_Object = MibTableColumn
rlSLAOperState = _RlSLAOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 3),
    _RlSLAOperState_Type()
)
rlSLAOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperState.setStatus("current")
_RlSLAOperTimeout_Type = Unsigned32
_RlSLAOperTimeout_Object = MibTableColumn
rlSLAOperTimeout = _RlSLAOperTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 4),
    _RlSLAOperTimeout_Type()
)
rlSLAOperTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperTimeout.setStatus("current")
_RlSLAOperFrequency_Type = Unsigned32
_RlSLAOperFrequency_Object = MibTableColumn
rlSLAOperFrequency = _RlSLAOperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 5),
    _RlSLAOperFrequency_Type()
)
rlSLAOperFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperFrequency.setStatus("current")


class _RlSLAOperReqDataSize_Type(Unsigned32):
    """Custom type rlSLAOperReqDataSize based on Unsigned32"""
    defaultValue = 28

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(28, 1472),
    )


_RlSLAOperReqDataSize_Type.__name__ = "Unsigned32"
_RlSLAOperReqDataSize_Object = MibTableColumn
rlSLAOperReqDataSize = _RlSLAOperReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 6),
    _RlSLAOperReqDataSize_Type()
)
rlSLAOperReqDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperReqDataSize.setStatus("current")


class _RlSLAOperReturnCode_Type(Integer32):
    """Custom type rlSLAOperReturnCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("error", 1))
    )


_RlSLAOperReturnCode_Type.__name__ = "Integer32"
_RlSLAOperReturnCode_Object = MibTableColumn
rlSLAOperReturnCode = _RlSLAOperReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 7),
    _RlSLAOperReturnCode_Type()
)
rlSLAOperReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAOperReturnCode.setStatus("current")
_RlSLAOperDestAddrType_Type = InetAddressType
_RlSLAOperDestAddrType_Object = MibTableColumn
rlSLAOperDestAddrType = _RlSLAOperDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 8),
    _RlSLAOperDestAddrType_Type()
)
rlSLAOperDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperDestAddrType.setStatus("current")
_RlSLAOperDestAddr_Type = InetAddress
_RlSLAOperDestAddr_Object = MibTableColumn
rlSLAOperDestAddr = _RlSLAOperDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 9),
    _RlSLAOperDestAddr_Type()
)
rlSLAOperDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperDestAddr.setStatus("current")


class _RlSLAOperSrcAddr_Type(IpAddress):
    """Custom type rlSLAOperSrcAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RlSLAOperSrcAddr_Type.__name__ = "IpAddress"
_RlSLAOperSrcAddr_Object = MibTableColumn
rlSLAOperSrcAddr = _RlSLAOperSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 10),
    _RlSLAOperSrcAddr_Type()
)
rlSLAOperSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperSrcAddr.setStatus("current")
_RlSLAOperSuccessCounter_Type = Unsigned32
_RlSLAOperSuccessCounter_Object = MibTableColumn
rlSLAOperSuccessCounter = _RlSLAOperSuccessCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 11),
    _RlSLAOperSuccessCounter_Type()
)
rlSLAOperSuccessCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAOperSuccessCounter.setStatus("current")
_RlSLAOperFailureCounter_Type = Unsigned32
_RlSLAOperFailureCounter_Object = MibTableColumn
rlSLAOperFailureCounter = _RlSLAOperFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 12),
    _RlSLAOperFailureCounter_Type()
)
rlSLAOperFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAOperFailureCounter.setStatus("current")
_RlSLAICMPEchoRequestCounter_Type = Unsigned32
_RlSLAICMPEchoRequestCounter_Object = MibTableColumn
rlSLAICMPEchoRequestCounter = _RlSLAICMPEchoRequestCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 13),
    _RlSLAICMPEchoRequestCounter_Type()
)
rlSLAICMPEchoRequestCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAICMPEchoRequestCounter.setStatus("current")
_RlSLAICMPEchoReplyCounter_Type = Unsigned32
_RlSLAICMPEchoReplyCounter_Object = MibTableColumn
rlSLAICMPEchoReplyCounter = _RlSLAICMPEchoReplyCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 14),
    _RlSLAICMPEchoReplyCounter_Type()
)
rlSLAICMPEchoReplyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAICMPEchoReplyCounter.setStatus("current")
_RlSLAICMPErrorCounter_Type = Unsigned32
_RlSLAICMPErrorCounter_Object = MibTableColumn
rlSLAICMPErrorCounter = _RlSLAICMPErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 15),
    _RlSLAICMPErrorCounter_Type()
)
rlSLAICMPErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAICMPErrorCounter.setStatus("current")
_RlSLARowStatus_Type = RowStatus
_RlSLARowStatus_Object = MibTableColumn
rlSLARowStatus = _RlSLARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 16),
    _RlSLARowStatus_Type()
)
rlSLARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSLARowStatus.setStatus("current")


class _RlSLAOperNextHopAddr_Type(IpAddress):
    """Custom type rlSLAOperNextHopAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RlSLAOperNextHopAddr_Type.__name__ = "IpAddress"
_RlSLAOperNextHopAddr_Object = MibTableColumn
rlSLAOperNextHopAddr = _RlSLAOperNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 17),
    _RlSLAOperNextHopAddr_Type()
)
rlSLAOperNextHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAOperNextHopAddr.setStatus("current")
_RlSLAICMPEchoHostUnreachCounter_Type = Unsigned32
_RlSLAICMPEchoHostUnreachCounter_Object = MibTableColumn
rlSLAICMPEchoHostUnreachCounter = _RlSLAICMPEchoHostUnreachCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 18),
    _RlSLAICMPEchoHostUnreachCounter_Type()
)
rlSLAICMPEchoHostUnreachCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAICMPEchoHostUnreachCounter.setStatus("current")
_RlSLAICMPEchoNonHostUnreachCounter_Type = Unsigned32
_RlSLAICMPEchoNonHostUnreachCounter_Object = MibTableColumn
rlSLAICMPEchoNonHostUnreachCounter = _RlSLAICMPEchoNonHostUnreachCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 1, 1, 19),
    _RlSLAICMPEchoNonHostUnreachCounter_Type()
)
rlSLAICMPEchoNonHostUnreachCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLAICMPEchoNonHostUnreachCounter.setStatus("current")
_RlSLATrackTable_Object = MibTable
rlSLATrackTable = _RlSLATrackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2)
)
if mibBuilder.loadTexts:
    rlSLATrackTable.setStatus("current")
_RlSLATrackEntry_Object = MibTableRow
rlSLATrackEntry = _RlSLATrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1)
)
rlSLATrackEntry.setIndexNames(
    (0, "CISCOSB-IP-SLA", "rlSLATrackObj"),
)
if mibBuilder.loadTexts:
    rlSLATrackEntry.setStatus("current")
_RlSLATrackObj_Type = Unsigned32
_RlSLATrackObj_Object = MibTableColumn
rlSLATrackObj = _RlSLATrackObj_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1, 1),
    _RlSLATrackObj_Type()
)
rlSLATrackObj.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSLATrackObj.setStatus("current")
_RlSLATrackOperId_Type = Unsigned32
_RlSLATrackOperId_Object = MibTableColumn
rlSLATrackOperId = _RlSLATrackOperId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1, 2),
    _RlSLATrackOperId_Type()
)
rlSLATrackOperId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLATrackOperId.setStatus("current")


class _RlSLAUpDelay_Type(Unsigned32):
    """Custom type rlSLAUpDelay based on Unsigned32"""
    defaultValue = 0


_RlSLAUpDelay_Type.__name__ = "Unsigned32"
_RlSLAUpDelay_Object = MibTableColumn
rlSLAUpDelay = _RlSLAUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1, 3),
    _RlSLAUpDelay_Type()
)
rlSLAUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAUpDelay.setStatus("current")


class _RlSLADownDelay_Type(Unsigned32):
    """Custom type rlSLADownDelay based on Unsigned32"""
    defaultValue = 0


_RlSLADownDelay_Type.__name__ = "Unsigned32"
_RlSLADownDelay_Object = MibTableColumn
rlSLADownDelay = _RlSLADownDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1, 4),
    _RlSLADownDelay_Type()
)
rlSLADownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLADownDelay.setStatus("current")
_RlSLADelayReminder_Type = Unsigned32
_RlSLADelayReminder_Object = MibTableColumn
rlSLADelayReminder = _RlSLADelayReminder_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1, 5),
    _RlSLADelayReminder_Type()
)
rlSLADelayReminder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLADelayReminder.setStatus("current")


class _RlSLATrackObjState_Type(Integer32):
    """Custom type rlSLATrackObjState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_RlSLATrackObjState_Type.__name__ = "Integer32"
_RlSLATrackObjState_Object = MibTableColumn
rlSLATrackObjState = _RlSLATrackObjState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1, 6),
    _RlSLATrackObjState_Type()
)
rlSLATrackObjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSLATrackObjState.setStatus("current")
_RlSLATrackRowStatus_Type = RowStatus
_RlSLATrackRowStatus_Object = MibTableColumn
rlSLATrackRowStatus = _RlSLATrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 2, 1, 7),
    _RlSLATrackRowStatus_Type()
)
rlSLATrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSLATrackRowStatus.setStatus("current")


class _RlSLAClearCounters_Type(Integer32):
    """Custom type rlSLAClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 64),
    )


_RlSLAClearCounters_Type.__name__ = "Integer32"
_RlSLAClearCounters_Object = MibScalar
rlSLAClearCounters = _RlSLAClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 231, 3),
    _RlSLAClearCounters_Type()
)
rlSLAClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSLAClearCounters.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-IP-SLA",
    **{"rlSLA": rlSLA,
       "rlSLAOperTable": rlSLAOperTable,
       "rlSLAOperEntry": rlSLAOperEntry,
       "rlSLAOperId": rlSLAOperId,
       "rlSLAOperType": rlSLAOperType,
       "rlSLAOperState": rlSLAOperState,
       "rlSLAOperTimeout": rlSLAOperTimeout,
       "rlSLAOperFrequency": rlSLAOperFrequency,
       "rlSLAOperReqDataSize": rlSLAOperReqDataSize,
       "rlSLAOperReturnCode": rlSLAOperReturnCode,
       "rlSLAOperDestAddrType": rlSLAOperDestAddrType,
       "rlSLAOperDestAddr": rlSLAOperDestAddr,
       "rlSLAOperSrcAddr": rlSLAOperSrcAddr,
       "rlSLAOperSuccessCounter": rlSLAOperSuccessCounter,
       "rlSLAOperFailureCounter": rlSLAOperFailureCounter,
       "rlSLAICMPEchoRequestCounter": rlSLAICMPEchoRequestCounter,
       "rlSLAICMPEchoReplyCounter": rlSLAICMPEchoReplyCounter,
       "rlSLAICMPErrorCounter": rlSLAICMPErrorCounter,
       "rlSLARowStatus": rlSLARowStatus,
       "rlSLAOperNextHopAddr": rlSLAOperNextHopAddr,
       "rlSLAICMPEchoHostUnreachCounter": rlSLAICMPEchoHostUnreachCounter,
       "rlSLAICMPEchoNonHostUnreachCounter": rlSLAICMPEchoNonHostUnreachCounter,
       "rlSLATrackTable": rlSLATrackTable,
       "rlSLATrackEntry": rlSLATrackEntry,
       "rlSLATrackObj": rlSLATrackObj,
       "rlSLATrackOperId": rlSLATrackOperId,
       "rlSLAUpDelay": rlSLAUpDelay,
       "rlSLADownDelay": rlSLADownDelay,
       "rlSLADelayReminder": rlSLADelayReminder,
       "rlSLATrackObjState": rlSLATrackObjState,
       "rlSLATrackRowStatus": rlSLATrackRowStatus,
       "rlSLAClearCounters": rlSLAClearCounters}
)
