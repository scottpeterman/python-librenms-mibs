# SNMP MIB module (SLE-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-SFLOW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:03 2025
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

sleSFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleSFlowBase_ObjectIdentity = ObjectIdentity
sleSFlowBase = _SleSFlowBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1)
)
_SleSFlowInfo_ObjectIdentity = ObjectIdentity
sleSFlowInfo = _SleSFlowInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 1)
)


class _SleSFlowEnable_Type(Integer32):
    """Custom type sleSFlowEnable based on Integer32"""
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


_SleSFlowEnable_Type.__name__ = "Integer32"
_SleSFlowEnable_Object = MibScalar
sleSFlowEnable = _SleSFlowEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 1, 1),
    _SleSFlowEnable_Type()
)
sleSFlowEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowEnable.setStatus("current")
_SleSFlowVersion_Type = OctetString
_SleSFlowVersion_Object = MibScalar
sleSFlowVersion = _SleSFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 1, 2),
    _SleSFlowVersion_Type()
)
sleSFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowVersion.setStatus("current")
_SleSFlowAgentAddress_Type = IpAddress
_SleSFlowAgentAddress_Object = MibScalar
sleSFlowAgentAddress = _SleSFlowAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 1, 3),
    _SleSFlowAgentAddress_Type()
)
sleSFlowAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowAgentAddress.setStatus("current")


class _SleSFlowMaxInstance_Type(Integer32):
    """Custom type sleSFlowMaxInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowMaxInstance_Type.__name__ = "Integer32"
_SleSFlowMaxInstance_Object = MibScalar
sleSFlowMaxInstance = _SleSFlowMaxInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 1, 4),
    _SleSFlowMaxInstance_Type()
)
sleSFlowMaxInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowMaxInstance.setStatus("current")
_SleSFlowControl_ObjectIdentity = ObjectIdentity
sleSFlowControl = _SleSFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2)
)


class _SleSFlowControlRequest_Type(Integer32):
    """Custom type sleSFlowControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSFlowEnable", 1),
          ("setSFlowAgentAddress", 2))
    )


_SleSFlowControlRequest_Type.__name__ = "Integer32"
_SleSFlowControlRequest_Object = MibScalar
sleSFlowControlRequest = _SleSFlowControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2, 1),
    _SleSFlowControlRequest_Type()
)
sleSFlowControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowControlRequest.setStatus("current")
_SleSFlowControlStatus_Type = SleControlStatusType
_SleSFlowControlStatus_Object = MibScalar
sleSFlowControlStatus = _SleSFlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2, 2),
    _SleSFlowControlStatus_Type()
)
sleSFlowControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowControlStatus.setStatus("current")
_SleSFlowControlTimer_Type = Gauge32
_SleSFlowControlTimer_Object = MibScalar
sleSFlowControlTimer = _SleSFlowControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2, 3),
    _SleSFlowControlTimer_Type()
)
sleSFlowControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowControlTimer.setStatus("current")
_SleSFlowControlTimeStamp_Type = TimeTicks
_SleSFlowControlTimeStamp_Object = MibScalar
sleSFlowControlTimeStamp = _SleSFlowControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2, 4),
    _SleSFlowControlTimeStamp_Type()
)
sleSFlowControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowControlTimeStamp.setStatus("current")
_SleSFlowControlReqResult_Type = SleControlRequestResultType
_SleSFlowControlReqResult_Object = MibScalar
sleSFlowControlReqResult = _SleSFlowControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2, 5),
    _SleSFlowControlReqResult_Type()
)
sleSFlowControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowControlReqResult.setStatus("current")


class _SleSFlowControlEnable_Type(Integer32):
    """Custom type sleSFlowControlEnable based on Integer32"""
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


_SleSFlowControlEnable_Type.__name__ = "Integer32"
_SleSFlowControlEnable_Object = MibScalar
sleSFlowControlEnable = _SleSFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2, 6),
    _SleSFlowControlEnable_Type()
)
sleSFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowControlEnable.setStatus("current")
_SleSFlowControlAgentAddress_Type = IpAddress
_SleSFlowControlAgentAddress_Object = MibScalar
sleSFlowControlAgentAddress = _SleSFlowControlAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 2, 7),
    _SleSFlowControlAgentAddress_Type()
)
sleSFlowControlAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowControlAgentAddress.setStatus("current")
_SleSFlowNotification_ObjectIdentity = ObjectIdentity
sleSFlowNotification = _SleSFlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 3)
)
_SleSFlowRcvr_ObjectIdentity = ObjectIdentity
sleSFlowRcvr = _SleSFlowRcvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2)
)
_SleSFlowRcvrTable_Object = MibTable
sleSFlowRcvrTable = _SleSFlowRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1)
)
if mibBuilder.loadTexts:
    sleSFlowRcvrTable.setStatus("current")
_SleSFlowRcvrEntry_Object = MibTableRow
sleSFlowRcvrEntry = _SleSFlowRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1)
)
sleSFlowRcvrEntry.setIndexNames(
    (0, "SLE-SFLOW-MIB", "sleSFlowRcvrIndex"),
)
if mibBuilder.loadTexts:
    sleSFlowRcvrEntry.setStatus("current")


class _SleSFlowRcvrIndex_Type(Integer32):
    """Custom type sleSFlowRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowRcvrIndex_Type.__name__ = "Integer32"
_SleSFlowRcvrIndex_Object = MibTableColumn
sleSFlowRcvrIndex = _SleSFlowRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1, 1),
    _SleSFlowRcvrIndex_Type()
)
sleSFlowRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrIndex.setStatus("current")


class _SleSFlowRcvrOwner_Type(OctetString):
    """Custom type sleSFlowRcvrOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SleSFlowRcvrOwner_Type.__name__ = "OctetString"
_SleSFlowRcvrOwner_Object = MibTableColumn
sleSFlowRcvrOwner = _SleSFlowRcvrOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1, 2),
    _SleSFlowRcvrOwner_Type()
)
sleSFlowRcvrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrOwner.setStatus("current")


class _SleSFlowRcvrTimeout_Type(Integer32):
    """Custom type sleSFlowRcvrTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleSFlowRcvrTimeout_Type.__name__ = "Integer32"
_SleSFlowRcvrTimeout_Object = MibTableColumn
sleSFlowRcvrTimeout = _SleSFlowRcvrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1, 3),
    _SleSFlowRcvrTimeout_Type()
)
sleSFlowRcvrTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrTimeout.setStatus("current")


class _SleSFlowRcvrMaxDatagramSize_Type(Integer32):
    """Custom type sleSFlowRcvrMaxDatagramSize based on Integer32"""
    defaultValue = 1400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1400),
    )


_SleSFlowRcvrMaxDatagramSize_Type.__name__ = "Integer32"
_SleSFlowRcvrMaxDatagramSize_Object = MibTableColumn
sleSFlowRcvrMaxDatagramSize = _SleSFlowRcvrMaxDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1, 4),
    _SleSFlowRcvrMaxDatagramSize_Type()
)
sleSFlowRcvrMaxDatagramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrMaxDatagramSize.setStatus("current")
_SleSFlowRcvrAddress_Type = IpAddress
_SleSFlowRcvrAddress_Object = MibTableColumn
sleSFlowRcvrAddress = _SleSFlowRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1, 5),
    _SleSFlowRcvrAddress_Type()
)
sleSFlowRcvrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrAddress.setStatus("current")


class _SleSFlowRcvrPort_Type(Integer32):
    """Custom type sleSFlowRcvrPort based on Integer32"""
    defaultValue = 6343

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowRcvrPort_Type.__name__ = "Integer32"
_SleSFlowRcvrPort_Object = MibTableColumn
sleSFlowRcvrPort = _SleSFlowRcvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1, 6),
    _SleSFlowRcvrPort_Type()
)
sleSFlowRcvrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrPort.setStatus("current")


class _SleSFlowRcvrDatagramVersion_Type(Integer32):
    """Custom type sleSFlowRcvrDatagramVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("version5", 5)
    )


_SleSFlowRcvrDatagramVersion_Type.__name__ = "Integer32"
_SleSFlowRcvrDatagramVersion_Object = MibTableColumn
sleSFlowRcvrDatagramVersion = _SleSFlowRcvrDatagramVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 1, 1, 7),
    _SleSFlowRcvrDatagramVersion_Type()
)
sleSFlowRcvrDatagramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrDatagramVersion.setStatus("current")
_SleSFlowRcvrControl_ObjectIdentity = ObjectIdentity
sleSFlowRcvrControl = _SleSFlowRcvrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2)
)


class _SleSFlowRcvrControlRequest_Type(Integer32):
    """Custom type sleSFlowRcvrControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createSFlowRcvr", 1),
          ("setSFlowRcvr", 2),
          ("destroySFlowRcvr", 3))
    )


_SleSFlowRcvrControlRequest_Type.__name__ = "Integer32"
_SleSFlowRcvrControlRequest_Object = MibScalar
sleSFlowRcvrControlRequest = _SleSFlowRcvrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 1),
    _SleSFlowRcvrControlRequest_Type()
)
sleSFlowRcvrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlRequest.setStatus("current")
_SleSFlowRcvrControlStatus_Type = SleControlStatusType
_SleSFlowRcvrControlStatus_Object = MibScalar
sleSFlowRcvrControlStatus = _SleSFlowRcvrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 2),
    _SleSFlowRcvrControlStatus_Type()
)
sleSFlowRcvrControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlStatus.setStatus("current")
_SleSFlowRcvrControlTimer_Type = Gauge32
_SleSFlowRcvrControlTimer_Object = MibScalar
sleSFlowRcvrControlTimer = _SleSFlowRcvrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 3),
    _SleSFlowRcvrControlTimer_Type()
)
sleSFlowRcvrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlTimer.setStatus("current")
_SleSFlowRcvrControlTimeStamp_Type = TimeTicks
_SleSFlowRcvrControlTimeStamp_Object = MibScalar
sleSFlowRcvrControlTimeStamp = _SleSFlowRcvrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 4),
    _SleSFlowRcvrControlTimeStamp_Type()
)
sleSFlowRcvrControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlTimeStamp.setStatus("current")
_SleSFlowRcvrControlReqResult_Type = SleControlRequestResultType
_SleSFlowRcvrControlReqResult_Object = MibScalar
sleSFlowRcvrControlReqResult = _SleSFlowRcvrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 5),
    _SleSFlowRcvrControlReqResult_Type()
)
sleSFlowRcvrControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlReqResult.setStatus("current")


class _SleSFlowRcvrControlIndex_Type(Integer32):
    """Custom type sleSFlowRcvrControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowRcvrControlIndex_Type.__name__ = "Integer32"
_SleSFlowRcvrControlIndex_Object = MibScalar
sleSFlowRcvrControlIndex = _SleSFlowRcvrControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 6),
    _SleSFlowRcvrControlIndex_Type()
)
sleSFlowRcvrControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlIndex.setStatus("current")


class _SleSFlowRcvrControlOwner_Type(OctetString):
    """Custom type sleSFlowRcvrControlOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SleSFlowRcvrControlOwner_Type.__name__ = "OctetString"
_SleSFlowRcvrControlOwner_Object = MibScalar
sleSFlowRcvrControlOwner = _SleSFlowRcvrControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 7),
    _SleSFlowRcvrControlOwner_Type()
)
sleSFlowRcvrControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlOwner.setStatus("current")


class _SleSFlowRcvrControlTimeout_Type(Integer32):
    """Custom type sleSFlowRcvrControlTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleSFlowRcvrControlTimeout_Type.__name__ = "Integer32"
_SleSFlowRcvrControlTimeout_Object = MibScalar
sleSFlowRcvrControlTimeout = _SleSFlowRcvrControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 8),
    _SleSFlowRcvrControlTimeout_Type()
)
sleSFlowRcvrControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlTimeout.setStatus("current")


class _SleSFlowRcvrControlMaxDatagramSize_Type(Integer32):
    """Custom type sleSFlowRcvrControlMaxDatagramSize based on Integer32"""
    defaultValue = 1400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1400),
    )


_SleSFlowRcvrControlMaxDatagramSize_Type.__name__ = "Integer32"
_SleSFlowRcvrControlMaxDatagramSize_Object = MibScalar
sleSFlowRcvrControlMaxDatagramSize = _SleSFlowRcvrControlMaxDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 9),
    _SleSFlowRcvrControlMaxDatagramSize_Type()
)
sleSFlowRcvrControlMaxDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlMaxDatagramSize.setStatus("current")
_SleSFlowRcvrControlAddress_Type = IpAddress
_SleSFlowRcvrControlAddress_Object = MibScalar
sleSFlowRcvrControlAddress = _SleSFlowRcvrControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 10),
    _SleSFlowRcvrControlAddress_Type()
)
sleSFlowRcvrControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlAddress.setStatus("current")


class _SleSFlowRcvrControlPort_Type(Integer32):
    """Custom type sleSFlowRcvrControlPort based on Integer32"""
    defaultValue = 6343

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowRcvrControlPort_Type.__name__ = "Integer32"
_SleSFlowRcvrControlPort_Object = MibScalar
sleSFlowRcvrControlPort = _SleSFlowRcvrControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 2, 11),
    _SleSFlowRcvrControlPort_Type()
)
sleSFlowRcvrControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowRcvrControlPort.setStatus("current")
_SleSFlowRcvrNotification_ObjectIdentity = ObjectIdentity
sleSFlowRcvrNotification = _SleSFlowRcvrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 3)
)
_SleSFlowFs_ObjectIdentity = ObjectIdentity
sleSFlowFs = _SleSFlowFs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3)
)
_SleSFlowFsTable_Object = MibTable
sleSFlowFsTable = _SleSFlowFsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 1)
)
if mibBuilder.loadTexts:
    sleSFlowFsTable.setStatus("current")
_SleSFlowFsEntry_Object = MibTableRow
sleSFlowFsEntry = _SleSFlowFsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 1, 1)
)
sleSFlowFsEntry.setIndexNames(
    (0, "SLE-SFLOW-MIB", "sleSFlowFsDataSource"),
    (0, "SLE-SFLOW-MIB", "sleSFlowFsInstance"),
)
if mibBuilder.loadTexts:
    sleSFlowFsEntry.setStatus("current")
_SleSFlowFsDataSource_Type = InterfaceIndex
_SleSFlowFsDataSource_Object = MibTableColumn
sleSFlowFsDataSource = _SleSFlowFsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 1, 1, 1),
    _SleSFlowFsDataSource_Type()
)
sleSFlowFsDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowFsDataSource.setStatus("current")


class _SleSFlowFsInstance_Type(Integer32):
    """Custom type sleSFlowFsInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowFsInstance_Type.__name__ = "Integer32"
_SleSFlowFsInstance_Object = MibTableColumn
sleSFlowFsInstance = _SleSFlowFsInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 1, 1, 2),
    _SleSFlowFsInstance_Type()
)
sleSFlowFsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowFsInstance.setStatus("current")


class _SleSFlowFsReceiver_Type(Integer32):
    """Custom type sleSFlowFsReceiver based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSFlowFsReceiver_Type.__name__ = "Integer32"
_SleSFlowFsReceiver_Object = MibTableColumn
sleSFlowFsReceiver = _SleSFlowFsReceiver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 1, 1, 3),
    _SleSFlowFsReceiver_Type()
)
sleSFlowFsReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowFsReceiver.setStatus("current")


class _SleSFlowFsPacketSamplingRate_Type(Integer32):
    """Custom type sleSFlowFsPacketSamplingRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_SleSFlowFsPacketSamplingRate_Type.__name__ = "Integer32"
_SleSFlowFsPacketSamplingRate_Object = MibTableColumn
sleSFlowFsPacketSamplingRate = _SleSFlowFsPacketSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 1, 1, 4),
    _SleSFlowFsPacketSamplingRate_Type()
)
sleSFlowFsPacketSamplingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowFsPacketSamplingRate.setStatus("current")


class _SleSFlowFsMaxHeaderSize_Type(Integer32):
    """Custom type sleSFlowFsMaxHeaderSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 256),
    )


_SleSFlowFsMaxHeaderSize_Type.__name__ = "Integer32"
_SleSFlowFsMaxHeaderSize_Object = MibTableColumn
sleSFlowFsMaxHeaderSize = _SleSFlowFsMaxHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 1, 1, 5),
    _SleSFlowFsMaxHeaderSize_Type()
)
sleSFlowFsMaxHeaderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowFsMaxHeaderSize.setStatus("current")
_SleSFlowFsControl_ObjectIdentity = ObjectIdentity
sleSFlowFsControl = _SleSFlowFsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2)
)


class _SleSFlowFsControlRequest_Type(Integer32):
    """Custom type sleSFlowFsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createSFlowFs", 1),
          ("setSFlowFs", 2),
          ("destroySFlowFs", 3))
    )


_SleSFlowFsControlRequest_Type.__name__ = "Integer32"
_SleSFlowFsControlRequest_Object = MibScalar
sleSFlowFsControlRequest = _SleSFlowFsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 1),
    _SleSFlowFsControlRequest_Type()
)
sleSFlowFsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlRequest.setStatus("current")
_SleSFlowFsControlStatus_Type = SleControlStatusType
_SleSFlowFsControlStatus_Object = MibScalar
sleSFlowFsControlStatus = _SleSFlowFsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 2),
    _SleSFlowFsControlStatus_Type()
)
sleSFlowFsControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlStatus.setStatus("current")
_SleSFlowFsControlTimer_Type = Gauge32
_SleSFlowFsControlTimer_Object = MibScalar
sleSFlowFsControlTimer = _SleSFlowFsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 3),
    _SleSFlowFsControlTimer_Type()
)
sleSFlowFsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlTimer.setStatus("current")
_SleSFlowFsControlTimeStamp_Type = TimeTicks
_SleSFlowFsControlTimeStamp_Object = MibScalar
sleSFlowFsControlTimeStamp = _SleSFlowFsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 4),
    _SleSFlowFsControlTimeStamp_Type()
)
sleSFlowFsControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlTimeStamp.setStatus("current")
_SleSFlowFsControlReqResult_Type = SleControlRequestResultType
_SleSFlowFsControlReqResult_Object = MibScalar
sleSFlowFsControlReqResult = _SleSFlowFsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 5),
    _SleSFlowFsControlReqResult_Type()
)
sleSFlowFsControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlReqResult.setStatus("current")
_SleSFlowFsControlDataSource_Type = InterfaceIndex
_SleSFlowFsControlDataSource_Object = MibScalar
sleSFlowFsControlDataSource = _SleSFlowFsControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 6),
    _SleSFlowFsControlDataSource_Type()
)
sleSFlowFsControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlDataSource.setStatus("current")


class _SleSFlowFsControlInstance_Type(Integer32):
    """Custom type sleSFlowFsControlInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowFsControlInstance_Type.__name__ = "Integer32"
_SleSFlowFsControlInstance_Object = MibScalar
sleSFlowFsControlInstance = _SleSFlowFsControlInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 7),
    _SleSFlowFsControlInstance_Type()
)
sleSFlowFsControlInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlInstance.setStatus("current")


class _SleSFlowFsControlReceiver_Type(Integer32):
    """Custom type sleSFlowFsControlReceiver based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSFlowFsControlReceiver_Type.__name__ = "Integer32"
_SleSFlowFsControlReceiver_Object = MibScalar
sleSFlowFsControlReceiver = _SleSFlowFsControlReceiver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 8),
    _SleSFlowFsControlReceiver_Type()
)
sleSFlowFsControlReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlReceiver.setStatus("current")


class _SleSFlowFsControlPacketSamplingRate_Type(Integer32):
    """Custom type sleSFlowFsControlPacketSamplingRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_SleSFlowFsControlPacketSamplingRate_Type.__name__ = "Integer32"
_SleSFlowFsControlPacketSamplingRate_Object = MibScalar
sleSFlowFsControlPacketSamplingRate = _SleSFlowFsControlPacketSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 9),
    _SleSFlowFsControlPacketSamplingRate_Type()
)
sleSFlowFsControlPacketSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlPacketSamplingRate.setStatus("current")


class _SleSFlowFsControlMaxHeaderSize_Type(Integer32):
    """Custom type sleSFlowFsControlMaxHeaderSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 256),
    )


_SleSFlowFsControlMaxHeaderSize_Type.__name__ = "Integer32"
_SleSFlowFsControlMaxHeaderSize_Object = MibScalar
sleSFlowFsControlMaxHeaderSize = _SleSFlowFsControlMaxHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 2, 10),
    _SleSFlowFsControlMaxHeaderSize_Type()
)
sleSFlowFsControlMaxHeaderSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowFsControlMaxHeaderSize.setStatus("current")
_SleSFlowFsNotification_ObjectIdentity = ObjectIdentity
sleSFlowFsNotification = _SleSFlowFsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 3)
)
_SleSFlowCp_ObjectIdentity = ObjectIdentity
sleSFlowCp = _SleSFlowCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4)
)
_SleSFlowCpTable_Object = MibTable
sleSFlowCpTable = _SleSFlowCpTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 1)
)
if mibBuilder.loadTexts:
    sleSFlowCpTable.setStatus("current")
_SleSFlowCpEntry_Object = MibTableRow
sleSFlowCpEntry = _SleSFlowCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 1, 1)
)
sleSFlowCpEntry.setIndexNames(
    (0, "SLE-SFLOW-MIB", "sleSFlowCpDataSource"),
    (0, "SLE-SFLOW-MIB", "sleSFlowCpInstance"),
)
if mibBuilder.loadTexts:
    sleSFlowCpEntry.setStatus("current")
_SleSFlowCpDataSource_Type = InterfaceIndex
_SleSFlowCpDataSource_Object = MibTableColumn
sleSFlowCpDataSource = _SleSFlowCpDataSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 1, 1, 1),
    _SleSFlowCpDataSource_Type()
)
sleSFlowCpDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowCpDataSource.setStatus("current")


class _SleSFlowCpInstance_Type(Integer32):
    """Custom type sleSFlowCpInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowCpInstance_Type.__name__ = "Integer32"
_SleSFlowCpInstance_Object = MibTableColumn
sleSFlowCpInstance = _SleSFlowCpInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 1, 1, 2),
    _SleSFlowCpInstance_Type()
)
sleSFlowCpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowCpInstance.setStatus("current")


class _SleSFlowCpReceiver_Type(Integer32):
    """Custom type sleSFlowCpReceiver based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSFlowCpReceiver_Type.__name__ = "Integer32"
_SleSFlowCpReceiver_Object = MibTableColumn
sleSFlowCpReceiver = _SleSFlowCpReceiver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 1, 1, 3),
    _SleSFlowCpReceiver_Type()
)
sleSFlowCpReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowCpReceiver.setStatus("current")


class _SleSFlowCpInterval_Type(Integer32):
    """Custom type sleSFlowCpInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SleSFlowCpInterval_Type.__name__ = "Integer32"
_SleSFlowCpInterval_Object = MibTableColumn
sleSFlowCpInterval = _SleSFlowCpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 1, 1, 4),
    _SleSFlowCpInterval_Type()
)
sleSFlowCpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowCpInterval.setStatus("current")
_SleSFlowCpControl_ObjectIdentity = ObjectIdentity
sleSFlowCpControl = _SleSFlowCpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2)
)


class _SleSFlowCpControlRequest_Type(Integer32):
    """Custom type sleSFlowCpControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createSFlowCp", 1),
          ("setSFlowCp", 2),
          ("destroySFlowCp", 3))
    )


_SleSFlowCpControlRequest_Type.__name__ = "Integer32"
_SleSFlowCpControlRequest_Object = MibScalar
sleSFlowCpControlRequest = _SleSFlowCpControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 1),
    _SleSFlowCpControlRequest_Type()
)
sleSFlowCpControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlRequest.setStatus("current")
_SleSFlowCpControlStatus_Type = SleControlStatusType
_SleSFlowCpControlStatus_Object = MibScalar
sleSFlowCpControlStatus = _SleSFlowCpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 2),
    _SleSFlowCpControlStatus_Type()
)
sleSFlowCpControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlStatus.setStatus("current")
_SleSFlowCpControlTimer_Type = Gauge32
_SleSFlowCpControlTimer_Object = MibScalar
sleSFlowCpControlTimer = _SleSFlowCpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 3),
    _SleSFlowCpControlTimer_Type()
)
sleSFlowCpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlTimer.setStatus("current")
_SleSFlowCpControlTimeStamp_Type = TimeTicks
_SleSFlowCpControlTimeStamp_Object = MibScalar
sleSFlowCpControlTimeStamp = _SleSFlowCpControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 4),
    _SleSFlowCpControlTimeStamp_Type()
)
sleSFlowCpControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlTimeStamp.setStatus("current")
_SleSFlowCpControlReqResult_Type = SleControlRequestResultType
_SleSFlowCpControlReqResult_Object = MibScalar
sleSFlowCpControlReqResult = _SleSFlowCpControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 5),
    _SleSFlowCpControlReqResult_Type()
)
sleSFlowCpControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlReqResult.setStatus("current")
_SleSFlowCpControlDataSource_Type = InterfaceIndex
_SleSFlowCpControlDataSource_Object = MibScalar
sleSFlowCpControlDataSource = _SleSFlowCpControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 6),
    _SleSFlowCpControlDataSource_Type()
)
sleSFlowCpControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlDataSource.setStatus("current")


class _SleSFlowCpControlInstance_Type(Integer32):
    """Custom type sleSFlowCpControlInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSFlowCpControlInstance_Type.__name__ = "Integer32"
_SleSFlowCpControlInstance_Object = MibScalar
sleSFlowCpControlInstance = _SleSFlowCpControlInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 7),
    _SleSFlowCpControlInstance_Type()
)
sleSFlowCpControlInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlInstance.setStatus("current")


class _SleSFlowCpControlReceiver_Type(Integer32):
    """Custom type sleSFlowCpControlReceiver based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSFlowCpControlReceiver_Type.__name__ = "Integer32"
_SleSFlowCpControlReceiver_Object = MibScalar
sleSFlowCpControlReceiver = _SleSFlowCpControlReceiver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 8),
    _SleSFlowCpControlReceiver_Type()
)
sleSFlowCpControlReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlReceiver.setStatus("current")


class _SleSFlowCpControlInterval_Type(Integer32):
    """Custom type sleSFlowCpControlInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SleSFlowCpControlInterval_Type.__name__ = "Integer32"
_SleSFlowCpControlInterval_Object = MibScalar
sleSFlowCpControlInterval = _SleSFlowCpControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 2, 9),
    _SleSFlowCpControlInterval_Type()
)
sleSFlowCpControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSFlowCpControlInterval.setStatus("current")
_SleSFlowCpNotification_ObjectIdentity = ObjectIdentity
sleSFlowCpNotification = _SleSFlowCpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 3)
)

# Managed Objects groups

sleSFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 5)
)
sleSFlowGroup.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowEnable"),
        ("SLE-SFLOW-MIB", "sleSFlowVersion"),
        ("SLE-SFLOW-MIB", "sleSFlowAgentAddress"),
        ("SLE-SFLOW-MIB", "sleSFlowMaxInstance"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrIndex"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrOwner"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrTimeout"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrMaxDatagramSize"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrAddress"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrPort"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrDatagramVersion"),
        ("SLE-SFLOW-MIB", "sleSFlowFsDataSource"),
        ("SLE-SFLOW-MIB", "sleSFlowFsInstance"),
        ("SLE-SFLOW-MIB", "sleSFlowFsReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowFsPacketSamplingRate"),
        ("SLE-SFLOW-MIB", "sleSFlowFsMaxHeaderSize"),
        ("SLE-SFLOW-MIB", "sleSFlowCpDataSource"),
        ("SLE-SFLOW-MIB", "sleSFlowCpInstance"),
        ("SLE-SFLOW-MIB", "sleSFlowCpReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowCpInterval"))
)
if mibBuilder.loadTexts:
    sleSFlowGroup.setStatus("current")

sleSFlowControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 6)
)
sleSFlowControlGroup.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowControlStatus"),
        ("SLE-SFLOW-MIB", "sleSFlowControlTimer"),
        ("SLE-SFLOW-MIB", "sleSFlowControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowControlEnable"),
        ("SLE-SFLOW-MIB", "sleSFlowControlAgentAddress"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlStatus"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlTimer"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlIndex"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlOwner"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlTimeout"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlMaxDatagramSize"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlAddress"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlPort"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlStatus"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlTimer"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlDataSource"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlInstance"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlPacketSamplingRate"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlMaxHeaderSize"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlStatus"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlTimer"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlDataSource"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlInstance"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlInterval"))
)
if mibBuilder.loadTexts:
    sleSFlowControlGroup.setStatus("current")


# Notification objects

sleSFlowEnableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 3, 1)
)
sleSFlowEnableChanged.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowEnable"))
)
if mibBuilder.loadTexts:
    sleSFlowEnableChanged.setStatus(
        "current"
    )

sleSFlowAgentAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 1, 3, 2)
)
sleSFlowAgentAddressChanged.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowAgentAddress"))
)
if mibBuilder.loadTexts:
    sleSFlowAgentAddressChanged.setStatus(
        "current"
    )

sleSFlowRcvrCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 3, 1)
)
sleSFlowRcvrCreated.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowRcvrControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrOwner"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrTimeout"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrMaxDatagramSize"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrAddress"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrPort"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrDatagramVersion"))
)
if mibBuilder.loadTexts:
    sleSFlowRcvrCreated.setStatus(
        "current"
    )

sleSFlowRcvrChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 3, 2)
)
sleSFlowRcvrChanged.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowRcvrControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrOwner"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrTimeout"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrMaxDatagramSize"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrAddress"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrPort"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrDatagramVersion"))
)
if mibBuilder.loadTexts:
    sleSFlowRcvrChanged.setStatus(
        "current"
    )

sleSFlowRcvrDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 2, 3, 3)
)
sleSFlowRcvrDestroyed.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowRcvrControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrControlIndex"))
)
if mibBuilder.loadTexts:
    sleSFlowRcvrDestroyed.setStatus(
        "current"
    )

sleSFlowFsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 3, 1)
)
sleSFlowFsCreated.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowFsControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowFsReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowFsPacketSamplingRate"),
        ("SLE-SFLOW-MIB", "sleSFlowFsMaxHeaderSize"))
)
if mibBuilder.loadTexts:
    sleSFlowFsCreated.setStatus(
        "current"
    )

sleSFlowFsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 3, 2)
)
sleSFlowFsChanged.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowFsControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowFsReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowFsPacketSamplingRate"),
        ("SLE-SFLOW-MIB", "sleSFlowFsMaxHeaderSize"))
)
if mibBuilder.loadTexts:
    sleSFlowFsChanged.setStatus(
        "current"
    )

sleSFlowFsDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 3, 3, 3)
)
sleSFlowFsDestroyed.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowFsControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlDataSource"),
        ("SLE-SFLOW-MIB", "sleSFlowFsControlInstance"))
)
if mibBuilder.loadTexts:
    sleSFlowFsDestroyed.setStatus(
        "current"
    )

sleSFlowCpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 3, 1)
)
sleSFlowCpCreated.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowCpControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowCpReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowCpInterval"))
)
if mibBuilder.loadTexts:
    sleSFlowCpCreated.setStatus(
        "current"
    )

sleSFlowCpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 3, 2)
)
sleSFlowCpChanged.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowCpControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowCpReceiver"),
        ("SLE-SFLOW-MIB", "sleSFlowCpInterval"))
)
if mibBuilder.loadTexts:
    sleSFlowCpChanged.setStatus(
        "current"
    )

sleSFlowCpDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 4, 3, 3)
)
sleSFlowCpDestroyed.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowCpControlRequest"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlTimeStamp"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlReqResult"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlDataSource"),
        ("SLE-SFLOW-MIB", "sleSFlowCpControlInstance"))
)
if mibBuilder.loadTexts:
    sleSFlowCpDestroyed.setStatus(
        "current"
    )


# Notifications groups

sleSFlowNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 21, 7)
)
sleSFlowNotificationGroup.setObjects(
      *(("SLE-SFLOW-MIB", "sleSFlowEnableChanged"),
        ("SLE-SFLOW-MIB", "sleSFlowAgentAddressChanged"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrCreated"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrChanged"),
        ("SLE-SFLOW-MIB", "sleSFlowRcvrDestroyed"),
        ("SLE-SFLOW-MIB", "sleSFlowFsCreated"),
        ("SLE-SFLOW-MIB", "sleSFlowFsChanged"),
        ("SLE-SFLOW-MIB", "sleSFlowFsDestroyed"),
        ("SLE-SFLOW-MIB", "sleSFlowCpCreated"),
        ("SLE-SFLOW-MIB", "sleSFlowCpChanged"),
        ("SLE-SFLOW-MIB", "sleSFlowCpDestroyed"))
)
if mibBuilder.loadTexts:
    sleSFlowNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-SFLOW-MIB",
    **{"sleSFlow": sleSFlow,
       "sleSFlowBase": sleSFlowBase,
       "sleSFlowInfo": sleSFlowInfo,
       "sleSFlowEnable": sleSFlowEnable,
       "sleSFlowVersion": sleSFlowVersion,
       "sleSFlowAgentAddress": sleSFlowAgentAddress,
       "sleSFlowMaxInstance": sleSFlowMaxInstance,
       "sleSFlowControl": sleSFlowControl,
       "sleSFlowControlRequest": sleSFlowControlRequest,
       "sleSFlowControlStatus": sleSFlowControlStatus,
       "sleSFlowControlTimer": sleSFlowControlTimer,
       "sleSFlowControlTimeStamp": sleSFlowControlTimeStamp,
       "sleSFlowControlReqResult": sleSFlowControlReqResult,
       "sleSFlowControlEnable": sleSFlowControlEnable,
       "sleSFlowControlAgentAddress": sleSFlowControlAgentAddress,
       "sleSFlowNotification": sleSFlowNotification,
       "sleSFlowEnableChanged": sleSFlowEnableChanged,
       "sleSFlowAgentAddressChanged": sleSFlowAgentAddressChanged,
       "sleSFlowRcvr": sleSFlowRcvr,
       "sleSFlowRcvrTable": sleSFlowRcvrTable,
       "sleSFlowRcvrEntry": sleSFlowRcvrEntry,
       "sleSFlowRcvrIndex": sleSFlowRcvrIndex,
       "sleSFlowRcvrOwner": sleSFlowRcvrOwner,
       "sleSFlowRcvrTimeout": sleSFlowRcvrTimeout,
       "sleSFlowRcvrMaxDatagramSize": sleSFlowRcvrMaxDatagramSize,
       "sleSFlowRcvrAddress": sleSFlowRcvrAddress,
       "sleSFlowRcvrPort": sleSFlowRcvrPort,
       "sleSFlowRcvrDatagramVersion": sleSFlowRcvrDatagramVersion,
       "sleSFlowRcvrControl": sleSFlowRcvrControl,
       "sleSFlowRcvrControlRequest": sleSFlowRcvrControlRequest,
       "sleSFlowRcvrControlStatus": sleSFlowRcvrControlStatus,
       "sleSFlowRcvrControlTimer": sleSFlowRcvrControlTimer,
       "sleSFlowRcvrControlTimeStamp": sleSFlowRcvrControlTimeStamp,
       "sleSFlowRcvrControlReqResult": sleSFlowRcvrControlReqResult,
       "sleSFlowRcvrControlIndex": sleSFlowRcvrControlIndex,
       "sleSFlowRcvrControlOwner": sleSFlowRcvrControlOwner,
       "sleSFlowRcvrControlTimeout": sleSFlowRcvrControlTimeout,
       "sleSFlowRcvrControlMaxDatagramSize": sleSFlowRcvrControlMaxDatagramSize,
       "sleSFlowRcvrControlAddress": sleSFlowRcvrControlAddress,
       "sleSFlowRcvrControlPort": sleSFlowRcvrControlPort,
       "sleSFlowRcvrNotification": sleSFlowRcvrNotification,
       "sleSFlowRcvrCreated": sleSFlowRcvrCreated,
       "sleSFlowRcvrChanged": sleSFlowRcvrChanged,
       "sleSFlowRcvrDestroyed": sleSFlowRcvrDestroyed,
       "sleSFlowFs": sleSFlowFs,
       "sleSFlowFsTable": sleSFlowFsTable,
       "sleSFlowFsEntry": sleSFlowFsEntry,
       "sleSFlowFsDataSource": sleSFlowFsDataSource,
       "sleSFlowFsInstance": sleSFlowFsInstance,
       "sleSFlowFsReceiver": sleSFlowFsReceiver,
       "sleSFlowFsPacketSamplingRate": sleSFlowFsPacketSamplingRate,
       "sleSFlowFsMaxHeaderSize": sleSFlowFsMaxHeaderSize,
       "sleSFlowFsControl": sleSFlowFsControl,
       "sleSFlowFsControlRequest": sleSFlowFsControlRequest,
       "sleSFlowFsControlStatus": sleSFlowFsControlStatus,
       "sleSFlowFsControlTimer": sleSFlowFsControlTimer,
       "sleSFlowFsControlTimeStamp": sleSFlowFsControlTimeStamp,
       "sleSFlowFsControlReqResult": sleSFlowFsControlReqResult,
       "sleSFlowFsControlDataSource": sleSFlowFsControlDataSource,
       "sleSFlowFsControlInstance": sleSFlowFsControlInstance,
       "sleSFlowFsControlReceiver": sleSFlowFsControlReceiver,
       "sleSFlowFsControlPacketSamplingRate": sleSFlowFsControlPacketSamplingRate,
       "sleSFlowFsControlMaxHeaderSize": sleSFlowFsControlMaxHeaderSize,
       "sleSFlowFsNotification": sleSFlowFsNotification,
       "sleSFlowFsCreated": sleSFlowFsCreated,
       "sleSFlowFsChanged": sleSFlowFsChanged,
       "sleSFlowFsDestroyed": sleSFlowFsDestroyed,
       "sleSFlowCp": sleSFlowCp,
       "sleSFlowCpTable": sleSFlowCpTable,
       "sleSFlowCpEntry": sleSFlowCpEntry,
       "sleSFlowCpDataSource": sleSFlowCpDataSource,
       "sleSFlowCpInstance": sleSFlowCpInstance,
       "sleSFlowCpReceiver": sleSFlowCpReceiver,
       "sleSFlowCpInterval": sleSFlowCpInterval,
       "sleSFlowCpControl": sleSFlowCpControl,
       "sleSFlowCpControlRequest": sleSFlowCpControlRequest,
       "sleSFlowCpControlStatus": sleSFlowCpControlStatus,
       "sleSFlowCpControlTimer": sleSFlowCpControlTimer,
       "sleSFlowCpControlTimeStamp": sleSFlowCpControlTimeStamp,
       "sleSFlowCpControlReqResult": sleSFlowCpControlReqResult,
       "sleSFlowCpControlDataSource": sleSFlowCpControlDataSource,
       "sleSFlowCpControlInstance": sleSFlowCpControlInstance,
       "sleSFlowCpControlReceiver": sleSFlowCpControlReceiver,
       "sleSFlowCpControlInterval": sleSFlowCpControlInterval,
       "sleSFlowCpNotification": sleSFlowCpNotification,
       "sleSFlowCpCreated": sleSFlowCpCreated,
       "sleSFlowCpChanged": sleSFlowCpChanged,
       "sleSFlowCpDestroyed": sleSFlowCpDestroyed,
       "sleSFlowGroup": sleSFlowGroup,
       "sleSFlowControlGroup": sleSFlowControlGroup,
       "sleSFlowNotificationGroup": sleSFlowNotificationGroup}
)
