# SNMP MIB module (SLE-MVQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-MVQOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:52 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

sleMVQoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14)
)


# Types definitions



class IntQueue(Integer32):
    """Custom type IntQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )





class IntQueueIndex(Integer32):
    """Custom type IntQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )





class IntEtherType(Integer32):
    """Custom type IntEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )





class IntEtherTypeIndex(Integer32):
    """Custom type IntEtherTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class IntIpAddressMask(Integer32):
    """Custom type IntIpAddressMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )





class IntQueueDirection(Integer32):
    """Custom type IntQueueDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("source", 1),
          ("destination", 2))
    )





class IntCoS(Integer32):
    """Custom type IntCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )





class IntCoSIndex(Integer32):
    """Custom type IntCoSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )





class IntDp(Integer32):
    """Custom type IntDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2),
    )





class IntDSCP(Integer32):
    """Custom type IntDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMVQoSBase_ObjectIdentity = ObjectIdentity
sleMVQoSBase = _SleMVQoSBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 1)
)
_SleMVQoS4_ObjectIdentity = ObjectIdentity
sleMVQoS4 = _SleMVQoS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2)
)
_SleMVQoS4Base_ObjectIdentity = ObjectIdentity
sleMVQoS4Base = _SleMVQoS4Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 1)
)
_SleMVQoS4BridgeBase_ObjectIdentity = ObjectIdentity
sleMVQoS4BridgeBase = _SleMVQoS4BridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2)
)
_SleMVQoS4BridgePort2TCMark_ObjectIdentity = ObjectIdentity
sleMVQoS4BridgePort2TCMark = _SleMVQoS4BridgePort2TCMark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1)
)
_SleMVQoS4BridgePort2TCMarkTable_Object = MibTable
sleMVQoS4BridgePort2TCMarkTable = _SleMVQoS4BridgePort2TCMarkTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkTable.setStatus("current")
_SleMVQoS4BridgePort2TCMarkEntry_Object = MibTableRow
sleMVQoS4BridgePort2TCMarkEntry = _SleMVQoS4BridgePort2TCMarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 1, 1)
)
sleMVQoS4BridgePort2TCMarkEntry.setIndexNames(
    (0, "SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkPortIndex"),
)
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkEntry.setStatus("current")
_SleMVQoS4BridgePort2TCMarkPortIndex_Type = InterfaceIndex
_SleMVQoS4BridgePort2TCMarkPortIndex_Object = MibTableColumn
sleMVQoS4BridgePort2TCMarkPortIndex = _SleMVQoS4BridgePort2TCMarkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 1, 1, 1),
    _SleMVQoS4BridgePort2TCMarkPortIndex_Type()
)
sleMVQoS4BridgePort2TCMarkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkPortIndex.setStatus("current")
_SleMVQoS4BridgePort2TCMarkQueue_Type = IntQueue
_SleMVQoS4BridgePort2TCMarkQueue_Object = MibTableColumn
sleMVQoS4BridgePort2TCMarkQueue = _SleMVQoS4BridgePort2TCMarkQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 1, 1, 2),
    _SleMVQoS4BridgePort2TCMarkQueue_Type()
)
sleMVQoS4BridgePort2TCMarkQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkQueue.setStatus("current")
_SleMVQoS4BridgePort2TCMarkControl_ObjectIdentity = ObjectIdentity
sleMVQoS4BridgePort2TCMarkControl = _SleMVQoS4BridgePort2TCMarkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2)
)


class _SleMVQoS4BridgePort2TCMarkControlRequest_Type(Integer32):
    """Custom type sleMVQoS4BridgePort2TCMarkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setBridgePort2TCMark", 1)
    )


_SleMVQoS4BridgePort2TCMarkControlRequest_Type.__name__ = "Integer32"
_SleMVQoS4BridgePort2TCMarkControlRequest_Object = MibScalar
sleMVQoS4BridgePort2TCMarkControlRequest = _SleMVQoS4BridgePort2TCMarkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2, 1),
    _SleMVQoS4BridgePort2TCMarkControlRequest_Type()
)
sleMVQoS4BridgePort2TCMarkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkControlRequest.setStatus("current")
_SleMVQoS4BridgePort2TCMarkControlStatus_Type = SleControlStatusType
_SleMVQoS4BridgePort2TCMarkControlStatus_Object = MibScalar
sleMVQoS4BridgePort2TCMarkControlStatus = _SleMVQoS4BridgePort2TCMarkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2, 2),
    _SleMVQoS4BridgePort2TCMarkControlStatus_Type()
)
sleMVQoS4BridgePort2TCMarkControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkControlStatus.setStatus("current")
_SleMVQoS4BridgePort2TCMarkControlTimer_Type = Gauge32
_SleMVQoS4BridgePort2TCMarkControlTimer_Object = MibScalar
sleMVQoS4BridgePort2TCMarkControlTimer = _SleMVQoS4BridgePort2TCMarkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2, 3),
    _SleMVQoS4BridgePort2TCMarkControlTimer_Type()
)
sleMVQoS4BridgePort2TCMarkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkControlTimer.setStatus("current")
_SleMVQoS4BridgePort2TCMarkControlTmeStamp_Type = TimeTicks
_SleMVQoS4BridgePort2TCMarkControlTmeStamp_Object = MibScalar
sleMVQoS4BridgePort2TCMarkControlTmeStamp = _SleMVQoS4BridgePort2TCMarkControlTmeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2, 4),
    _SleMVQoS4BridgePort2TCMarkControlTmeStamp_Type()
)
sleMVQoS4BridgePort2TCMarkControlTmeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkControlTmeStamp.setStatus("current")
_SleMVQoS4BridgePort2TCMarkControlReqResult_Type = SleControlRequestResultType
_SleMVQoS4BridgePort2TCMarkControlReqResult_Object = MibScalar
sleMVQoS4BridgePort2TCMarkControlReqResult = _SleMVQoS4BridgePort2TCMarkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2, 5),
    _SleMVQoS4BridgePort2TCMarkControlReqResult_Type()
)
sleMVQoS4BridgePort2TCMarkControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkControlReqResult.setStatus("current")
_SleMVQoS4BridgePort2TCMarkControlPortIndex_Type = InterfaceIndex
_SleMVQoS4BridgePort2TCMarkControlPortIndex_Object = MibScalar
sleMVQoS4BridgePort2TCMarkControlPortIndex = _SleMVQoS4BridgePort2TCMarkControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2, 6),
    _SleMVQoS4BridgePort2TCMarkControlPortIndex_Type()
)
sleMVQoS4BridgePort2TCMarkControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkControlPortIndex.setStatus("current")
_SleMVQoS4BridgePort2TCMarkControlQueue_Type = IntQueue
_SleMVQoS4BridgePort2TCMarkControlQueue_Object = MibScalar
sleMVQoS4BridgePort2TCMarkControlQueue = _SleMVQoS4BridgePort2TCMarkControlQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 2, 7),
    _SleMVQoS4BridgePort2TCMarkControlQueue_Type()
)
sleMVQoS4BridgePort2TCMarkControlQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4BridgePort2TCMarkControlQueue.setStatus("current")
_SleMVQoS4BridgePort2TCMarkNotification_ObjectIdentity = ObjectIdentity
sleMVQoS4BridgePort2TCMarkNotification = _SleMVQoS4BridgePort2TCMarkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 3)
)
_SleMVQoS4InLIF_ObjectIdentity = ObjectIdentity
sleMVQoS4InLIF = _SleMVQoS4InLIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3)
)
_SleMVQoS4InLIFMark_ObjectIdentity = ObjectIdentity
sleMVQoS4InLIFMark = _SleMVQoS4InLIFMark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1)
)
_SleMVQoS4InLIFMarkTable_Object = MibTable
sleMVQoS4InLIFMarkTable = _SleMVQoS4InLIFMarkTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkTable.setStatus("current")
_SleMVQoS4InLIFMarkEntry_Object = MibTableRow
sleMVQoS4InLIFMarkEntry = _SleMVQoS4InLIFMarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 1, 1)
)
sleMVQoS4InLIFMarkEntry.setIndexNames(
    (0, "SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkPortIndex"),
)
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkEntry.setStatus("current")
_SleMVQoS4InLIFMarkPortIndex_Type = InterfaceIndex
_SleMVQoS4InLIFMarkPortIndex_Object = MibTableColumn
sleMVQoS4InLIFMarkPortIndex = _SleMVQoS4InLIFMarkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 1, 1, 1),
    _SleMVQoS4InLIFMarkPortIndex_Type()
)
sleMVQoS4InLIFMarkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkPortIndex.setStatus("current")
_SleMVQoS4InLIFMarkCoS_Type = IntCoS
_SleMVQoS4InLIFMarkCoS_Object = MibTableColumn
sleMVQoS4InLIFMarkCoS = _SleMVQoS4InLIFMarkCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 1, 1, 2),
    _SleMVQoS4InLIFMarkCoS_Type()
)
sleMVQoS4InLIFMarkCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkCoS.setStatus("current")
_SleMVQoS4InLIFMarkDSCP_Type = IntDSCP
_SleMVQoS4InLIFMarkDSCP_Object = MibTableColumn
sleMVQoS4InLIFMarkDSCP = _SleMVQoS4InLIFMarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 1, 1, 3),
    _SleMVQoS4InLIFMarkDSCP_Type()
)
sleMVQoS4InLIFMarkDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkDSCP.setStatus("current")
_SleMVQoS4InLIFMarkControl_ObjectIdentity = ObjectIdentity
sleMVQoS4InLIFMarkControl = _SleMVQoS4InLIFMarkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2)
)


class _SleMVQoS4InLIFMarkControlRequest_Type(Integer32):
    """Custom type sleMVQoS4InLIFMarkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setInLIFUp", 1),
          ("setInLIFDscp", 2))
    )


_SleMVQoS4InLIFMarkControlRequest_Type.__name__ = "Integer32"
_SleMVQoS4InLIFMarkControlRequest_Object = MibScalar
sleMVQoS4InLIFMarkControlRequest = _SleMVQoS4InLIFMarkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 1),
    _SleMVQoS4InLIFMarkControlRequest_Type()
)
sleMVQoS4InLIFMarkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlRequest.setStatus("current")
_SleMVQoS4InLIFMarkControlStatus_Type = SleControlStatusType
_SleMVQoS4InLIFMarkControlStatus_Object = MibScalar
sleMVQoS4InLIFMarkControlStatus = _SleMVQoS4InLIFMarkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 2),
    _SleMVQoS4InLIFMarkControlStatus_Type()
)
sleMVQoS4InLIFMarkControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlStatus.setStatus("current")
_SleMVQoS4InLIFMarkControlTimer_Type = Gauge32
_SleMVQoS4InLIFMarkControlTimer_Object = MibScalar
sleMVQoS4InLIFMarkControlTimer = _SleMVQoS4InLIFMarkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 3),
    _SleMVQoS4InLIFMarkControlTimer_Type()
)
sleMVQoS4InLIFMarkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlTimer.setStatus("current")
_SleMVQoS4InLIFMarkControlTimeStamp_Type = TimeTicks
_SleMVQoS4InLIFMarkControlTimeStamp_Object = MibScalar
sleMVQoS4InLIFMarkControlTimeStamp = _SleMVQoS4InLIFMarkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 4),
    _SleMVQoS4InLIFMarkControlTimeStamp_Type()
)
sleMVQoS4InLIFMarkControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlTimeStamp.setStatus("current")
_SleMVQoS4InLIFMarkControlReqResult_Type = SleControlRequestResultType
_SleMVQoS4InLIFMarkControlReqResult_Object = MibScalar
sleMVQoS4InLIFMarkControlReqResult = _SleMVQoS4InLIFMarkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 5),
    _SleMVQoS4InLIFMarkControlReqResult_Type()
)
sleMVQoS4InLIFMarkControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlReqResult.setStatus("current")
_SleMVQoS4InLIFMarkControlPortIndex_Type = InterfaceIndex
_SleMVQoS4InLIFMarkControlPortIndex_Object = MibScalar
sleMVQoS4InLIFMarkControlPortIndex = _SleMVQoS4InLIFMarkControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 6),
    _SleMVQoS4InLIFMarkControlPortIndex_Type()
)
sleMVQoS4InLIFMarkControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlPortIndex.setStatus("current")
_SleMVQoS4InLIFMarkControlCoS_Type = IntCoS
_SleMVQoS4InLIFMarkControlCoS_Object = MibScalar
sleMVQoS4InLIFMarkControlCoS = _SleMVQoS4InLIFMarkControlCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 7),
    _SleMVQoS4InLIFMarkControlCoS_Type()
)
sleMVQoS4InLIFMarkControlCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlCoS.setStatus("current")
_SleMVQoS4InLIFMarkControlDSCP_Type = IntDSCP
_SleMVQoS4InLIFMarkControlDSCP_Object = MibScalar
sleMVQoS4InLIFMarkControlDSCP = _SleMVQoS4InLIFMarkControlDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 2, 8),
    _SleMVQoS4InLIFMarkControlDSCP_Type()
)
sleMVQoS4InLIFMarkControlDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4InLIFMarkControlDSCP.setStatus("current")
_SleMVQoS4InLIFMarkNotification_ObjectIdentity = ObjectIdentity
sleMVQoS4InLIFMarkNotification = _SleMVQoS4InLIFMarkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 3)
)
_SleMVQoS4Router_ObjectIdentity = ObjectIdentity
sleMVQoS4Router = _SleMVQoS4Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4)
)
_SleMVQoS4RouterMark_ObjectIdentity = ObjectIdentity
sleMVQoS4RouterMark = _SleMVQoS4RouterMark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1)
)
_SleMVQoS4RouterMarkTable_Object = MibTable
sleMVQoS4RouterMarkTable = _SleMVQoS4RouterMarkTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkTable.setStatus("current")
_SleMVQoS4RouterMarkEntry_Object = MibTableRow
sleMVQoS4RouterMarkEntry = _SleMVQoS4RouterMarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 1, 1)
)
sleMVQoS4RouterMarkEntry.setIndexNames(
    (0, "SLE-MVQOS-MIB", "sleMVQoS4RouterMarkNextHop"),
)
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkEntry.setStatus("current")
_SleMVQoS4RouterMarkNextHop_Type = IpAddress
_SleMVQoS4RouterMarkNextHop_Object = MibTableColumn
sleMVQoS4RouterMarkNextHop = _SleMVQoS4RouterMarkNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 1, 1, 1),
    _SleMVQoS4RouterMarkNextHop_Type()
)
sleMVQoS4RouterMarkNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkNextHop.setStatus("current")
_SleMVQoS4RouterMarkQueue_Type = IntQueue
_SleMVQoS4RouterMarkQueue_Object = MibTableColumn
sleMVQoS4RouterMarkQueue = _SleMVQoS4RouterMarkQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 1, 1, 2),
    _SleMVQoS4RouterMarkQueue_Type()
)
sleMVQoS4RouterMarkQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkQueue.setStatus("current")
_SleMVQoS4RouterMarkDp_Type = IntDp
_SleMVQoS4RouterMarkDp_Object = MibTableColumn
sleMVQoS4RouterMarkDp = _SleMVQoS4RouterMarkDp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 1, 1, 3),
    _SleMVQoS4RouterMarkDp_Type()
)
sleMVQoS4RouterMarkDp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkDp.setStatus("current")
_SleMVQoS4RouterMarkCoS_Type = IntCoS
_SleMVQoS4RouterMarkCoS_Object = MibTableColumn
sleMVQoS4RouterMarkCoS = _SleMVQoS4RouterMarkCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 1, 1, 4),
    _SleMVQoS4RouterMarkCoS_Type()
)
sleMVQoS4RouterMarkCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkCoS.setStatus("current")
_SleMVQoS4RouterMarkControl_ObjectIdentity = ObjectIdentity
sleMVQoS4RouterMarkControl = _SleMVQoS4RouterMarkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2)
)


class _SleMVQoS4RouterMarkControlRequest_Type(Integer32):
    """Custom type sleMVQoS4RouterMarkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createRouterMarkEntry", 1),
          ("setRouterMarkEntry", 2),
          ("destroyRouterMarkEntry", 3))
    )


_SleMVQoS4RouterMarkControlRequest_Type.__name__ = "Integer32"
_SleMVQoS4RouterMarkControlRequest_Object = MibScalar
sleMVQoS4RouterMarkControlRequest = _SleMVQoS4RouterMarkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 1),
    _SleMVQoS4RouterMarkControlRequest_Type()
)
sleMVQoS4RouterMarkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlRequest.setStatus("current")
_SleMVQoS4RouterMarkControlStatus_Type = SleControlStatusType
_SleMVQoS4RouterMarkControlStatus_Object = MibScalar
sleMVQoS4RouterMarkControlStatus = _SleMVQoS4RouterMarkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 2),
    _SleMVQoS4RouterMarkControlStatus_Type()
)
sleMVQoS4RouterMarkControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlStatus.setStatus("current")
_SleMVQoS4RouterMarkControlTimer_Type = Gauge32
_SleMVQoS4RouterMarkControlTimer_Object = MibScalar
sleMVQoS4RouterMarkControlTimer = _SleMVQoS4RouterMarkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 3),
    _SleMVQoS4RouterMarkControlTimer_Type()
)
sleMVQoS4RouterMarkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlTimer.setStatus("current")
_SleMVQoS4RouterMarkControlTimeStamp_Type = TimeTicks
_SleMVQoS4RouterMarkControlTimeStamp_Object = MibScalar
sleMVQoS4RouterMarkControlTimeStamp = _SleMVQoS4RouterMarkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 4),
    _SleMVQoS4RouterMarkControlTimeStamp_Type()
)
sleMVQoS4RouterMarkControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlTimeStamp.setStatus("current")
_SleMVQoS4RouterMarkControlReqResult_Type = SleControlRequestResultType
_SleMVQoS4RouterMarkControlReqResult_Object = MibScalar
sleMVQoS4RouterMarkControlReqResult = _SleMVQoS4RouterMarkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 5),
    _SleMVQoS4RouterMarkControlReqResult_Type()
)
sleMVQoS4RouterMarkControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlReqResult.setStatus("current")
_SleMVQoS4RouterMarkControlNextHop_Type = IpAddress
_SleMVQoS4RouterMarkControlNextHop_Object = MibScalar
sleMVQoS4RouterMarkControlNextHop = _SleMVQoS4RouterMarkControlNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 6),
    _SleMVQoS4RouterMarkControlNextHop_Type()
)
sleMVQoS4RouterMarkControlNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlNextHop.setStatus("current")
_SleMVQoS4RouterMarkControlQueue_Type = IntQueue
_SleMVQoS4RouterMarkControlQueue_Object = MibScalar
sleMVQoS4RouterMarkControlQueue = _SleMVQoS4RouterMarkControlQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 7),
    _SleMVQoS4RouterMarkControlQueue_Type()
)
sleMVQoS4RouterMarkControlQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlQueue.setStatus("current")
_SleMVQoS4RouterMarkControlDp_Type = IntDp
_SleMVQoS4RouterMarkControlDp_Object = MibScalar
sleMVQoS4RouterMarkControlDp = _SleMVQoS4RouterMarkControlDp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 8),
    _SleMVQoS4RouterMarkControlDp_Type()
)
sleMVQoS4RouterMarkControlDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlDp.setStatus("current")
_SleMVQoS4RouterMarkControlCoS_Type = IntCoS
_SleMVQoS4RouterMarkControlCoS_Object = MibScalar
sleMVQoS4RouterMarkControlCoS = _SleMVQoS4RouterMarkControlCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 2, 9),
    _SleMVQoS4RouterMarkControlCoS_Type()
)
sleMVQoS4RouterMarkControlCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMVQoS4RouterMarkControlCoS.setStatus("current")
_SleMVQoS4RouterMarkNotification_ObjectIdentity = ObjectIdentity
sleMVQoS4RouterMarkNotification = _SleMVQoS4RouterMarkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 3)
)
_SleMVQoS6_ObjectIdentity = ObjectIdentity
sleMVQoS6 = _SleMVQoS6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 3)
)

# Managed Objects groups

sleMVQoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 4)
)
sleMVQoSGroup.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkPortIndex"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkQueue"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkPortIndex"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkCoS"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkDSCP"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkNextHop"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkQueue"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkDp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkCoS"))
)
if mibBuilder.loadTexts:
    sleMVQoSGroup.setStatus("current")

sleMVQoSControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 5)
)
sleMVQoSControlGroup.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlStatus"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlTimer"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlTmeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlPortIndex"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlQueue"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlStatus"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlTimer"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlTimeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlNextHop"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlQueue"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlDp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlCoS"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlStatus"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlTimer"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlTimeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlPortIndex"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlCoS"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlDSCP"))
)
if mibBuilder.loadTexts:
    sleMVQoSControlGroup.setStatus("current")


# Notification objects

sleBridgePort2TCMarkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 2, 1, 3, 1)
)
sleBridgePort2TCMarkChanged.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlTmeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4BridgePort2TCMarkQueue"))
)
if mibBuilder.loadTexts:
    sleBridgePort2TCMarkChanged.setStatus(
        "current"
    )

sleInLIFMarkUpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 3, 1)
)
sleInLIFMarkUpChanged.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlTimeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkCoS"))
)
if mibBuilder.loadTexts:
    sleInLIFMarkUpChanged.setStatus(
        "current"
    )

sleInLIFMarkDscpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 3, 1, 3, 2)
)
sleInLIFMarkDscpChanged.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlTimeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4InLIFMarkDSCP"))
)
if mibBuilder.loadTexts:
    sleInLIFMarkDscpChanged.setStatus(
        "current"
    )

sleRouterMarkEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 3, 1)
)
sleRouterMarkEntryCreated.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlTimeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkQueue"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkDp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkCoS"))
)
if mibBuilder.loadTexts:
    sleRouterMarkEntryCreated.setStatus(
        "current"
    )

sleRouterMarkEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 3, 2)
)
sleRouterMarkEntryChanged.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlTimeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkQueue"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkDp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkCoS"))
)
if mibBuilder.loadTexts:
    sleRouterMarkEntryChanged.setStatus(
        "current"
    )

sleRouterMarkEntryDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 2, 4, 1, 3, 3)
)
sleRouterMarkEntryDestroyed.setObjects(
      *(("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlRequest"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlTimeStamp"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlReqResult"),
        ("SLE-MVQOS-MIB", "sleMVQoS4RouterMarkControlNextHop"))
)
if mibBuilder.loadTexts:
    sleRouterMarkEntryDestroyed.setStatus(
        "current"
    )


# Notifications groups

sleMVQoSNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 14, 6)
)
sleMVQoSNotificationGroup.setObjects(
      *(("SLE-MVQOS-MIB", "sleBridgePort2TCMarkChanged"),
        ("SLE-MVQOS-MIB", "sleInLIFMarkUpChanged"),
        ("SLE-MVQOS-MIB", "sleInLIFMarkDscpChanged"),
        ("SLE-MVQOS-MIB", "sleRouterMarkEntryDestroyed"),
        ("SLE-MVQOS-MIB", "sleRouterMarkEntryCreated"),
        ("SLE-MVQOS-MIB", "sleRouterMarkEntryChanged"))
)
if mibBuilder.loadTexts:
    sleMVQoSNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MVQOS-MIB",
    **{"IntQueue": IntQueue,
       "IntQueueIndex": IntQueueIndex,
       "IntEtherType": IntEtherType,
       "IntEtherTypeIndex": IntEtherTypeIndex,
       "IntIpAddressMask": IntIpAddressMask,
       "IntQueueDirection": IntQueueDirection,
       "IntCoS": IntCoS,
       "IntCoSIndex": IntCoSIndex,
       "IntDp": IntDp,
       "IntDSCP": IntDSCP,
       "sleMVQoS": sleMVQoS,
       "sleMVQoSBase": sleMVQoSBase,
       "sleMVQoS4": sleMVQoS4,
       "sleMVQoS4Base": sleMVQoS4Base,
       "sleMVQoS4BridgeBase": sleMVQoS4BridgeBase,
       "sleMVQoS4BridgePort2TCMark": sleMVQoS4BridgePort2TCMark,
       "sleMVQoS4BridgePort2TCMarkTable": sleMVQoS4BridgePort2TCMarkTable,
       "sleMVQoS4BridgePort2TCMarkEntry": sleMVQoS4BridgePort2TCMarkEntry,
       "sleMVQoS4BridgePort2TCMarkPortIndex": sleMVQoS4BridgePort2TCMarkPortIndex,
       "sleMVQoS4BridgePort2TCMarkQueue": sleMVQoS4BridgePort2TCMarkQueue,
       "sleMVQoS4BridgePort2TCMarkControl": sleMVQoS4BridgePort2TCMarkControl,
       "sleMVQoS4BridgePort2TCMarkControlRequest": sleMVQoS4BridgePort2TCMarkControlRequest,
       "sleMVQoS4BridgePort2TCMarkControlStatus": sleMVQoS4BridgePort2TCMarkControlStatus,
       "sleMVQoS4BridgePort2TCMarkControlTimer": sleMVQoS4BridgePort2TCMarkControlTimer,
       "sleMVQoS4BridgePort2TCMarkControlTmeStamp": sleMVQoS4BridgePort2TCMarkControlTmeStamp,
       "sleMVQoS4BridgePort2TCMarkControlReqResult": sleMVQoS4BridgePort2TCMarkControlReqResult,
       "sleMVQoS4BridgePort2TCMarkControlPortIndex": sleMVQoS4BridgePort2TCMarkControlPortIndex,
       "sleMVQoS4BridgePort2TCMarkControlQueue": sleMVQoS4BridgePort2TCMarkControlQueue,
       "sleMVQoS4BridgePort2TCMarkNotification": sleMVQoS4BridgePort2TCMarkNotification,
       "sleBridgePort2TCMarkChanged": sleBridgePort2TCMarkChanged,
       "sleMVQoS4InLIF": sleMVQoS4InLIF,
       "sleMVQoS4InLIFMark": sleMVQoS4InLIFMark,
       "sleMVQoS4InLIFMarkTable": sleMVQoS4InLIFMarkTable,
       "sleMVQoS4InLIFMarkEntry": sleMVQoS4InLIFMarkEntry,
       "sleMVQoS4InLIFMarkPortIndex": sleMVQoS4InLIFMarkPortIndex,
       "sleMVQoS4InLIFMarkCoS": sleMVQoS4InLIFMarkCoS,
       "sleMVQoS4InLIFMarkDSCP": sleMVQoS4InLIFMarkDSCP,
       "sleMVQoS4InLIFMarkControl": sleMVQoS4InLIFMarkControl,
       "sleMVQoS4InLIFMarkControlRequest": sleMVQoS4InLIFMarkControlRequest,
       "sleMVQoS4InLIFMarkControlStatus": sleMVQoS4InLIFMarkControlStatus,
       "sleMVQoS4InLIFMarkControlTimer": sleMVQoS4InLIFMarkControlTimer,
       "sleMVQoS4InLIFMarkControlTimeStamp": sleMVQoS4InLIFMarkControlTimeStamp,
       "sleMVQoS4InLIFMarkControlReqResult": sleMVQoS4InLIFMarkControlReqResult,
       "sleMVQoS4InLIFMarkControlPortIndex": sleMVQoS4InLIFMarkControlPortIndex,
       "sleMVQoS4InLIFMarkControlCoS": sleMVQoS4InLIFMarkControlCoS,
       "sleMVQoS4InLIFMarkControlDSCP": sleMVQoS4InLIFMarkControlDSCP,
       "sleMVQoS4InLIFMarkNotification": sleMVQoS4InLIFMarkNotification,
       "sleInLIFMarkUpChanged": sleInLIFMarkUpChanged,
       "sleInLIFMarkDscpChanged": sleInLIFMarkDscpChanged,
       "sleMVQoS4Router": sleMVQoS4Router,
       "sleMVQoS4RouterMark": sleMVQoS4RouterMark,
       "sleMVQoS4RouterMarkTable": sleMVQoS4RouterMarkTable,
       "sleMVQoS4RouterMarkEntry": sleMVQoS4RouterMarkEntry,
       "sleMVQoS4RouterMarkNextHop": sleMVQoS4RouterMarkNextHop,
       "sleMVQoS4RouterMarkQueue": sleMVQoS4RouterMarkQueue,
       "sleMVQoS4RouterMarkDp": sleMVQoS4RouterMarkDp,
       "sleMVQoS4RouterMarkCoS": sleMVQoS4RouterMarkCoS,
       "sleMVQoS4RouterMarkControl": sleMVQoS4RouterMarkControl,
       "sleMVQoS4RouterMarkControlRequest": sleMVQoS4RouterMarkControlRequest,
       "sleMVQoS4RouterMarkControlStatus": sleMVQoS4RouterMarkControlStatus,
       "sleMVQoS4RouterMarkControlTimer": sleMVQoS4RouterMarkControlTimer,
       "sleMVQoS4RouterMarkControlTimeStamp": sleMVQoS4RouterMarkControlTimeStamp,
       "sleMVQoS4RouterMarkControlReqResult": sleMVQoS4RouterMarkControlReqResult,
       "sleMVQoS4RouterMarkControlNextHop": sleMVQoS4RouterMarkControlNextHop,
       "sleMVQoS4RouterMarkControlQueue": sleMVQoS4RouterMarkControlQueue,
       "sleMVQoS4RouterMarkControlDp": sleMVQoS4RouterMarkControlDp,
       "sleMVQoS4RouterMarkControlCoS": sleMVQoS4RouterMarkControlCoS,
       "sleMVQoS4RouterMarkNotification": sleMVQoS4RouterMarkNotification,
       "sleRouterMarkEntryCreated": sleRouterMarkEntryCreated,
       "sleRouterMarkEntryChanged": sleRouterMarkEntryChanged,
       "sleRouterMarkEntryDestroyed": sleRouterMarkEntryDestroyed,
       "sleMVQoS6": sleMVQoS6,
       "sleMVQoSGroup": sleMVQoSGroup,
       "sleMVQoSControlGroup": sleMVQoSControlGroup,
       "sleMVQoSNotificationGroup": sleMVQoSNotificationGroup}
)
