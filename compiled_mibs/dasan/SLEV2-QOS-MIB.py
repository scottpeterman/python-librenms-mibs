# SNMP MIB module (SLEV2-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLEV2-QOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:13 2025
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

(sleV2Mgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleV2Mgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 Bits,
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleV2QoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10)
)


# Types definitions



class IntFlowIndex(Integer32):
    """Custom type IntFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )





class IntClassIndex(Integer32):
    """Custom type IntClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )





class IntPolicerIndex(Integer32):
    """Custom type IntPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )





class IntPolicyIndex(Integer32):
    """Custom type IntPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )





class OctetName(OctetString):
    """Custom type OctetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )





class IntEthernetType(Integer32):
    """Custom type IntEthernetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )





class Int8021p(Integer32):
    """Custom type Int8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )





class IntIpAddrMask(Integer32):
    """Custom type IntIpAddrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )





class IntToS(Integer32):
    """Custom type IntToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )





class IntPktLen(Integer32):
    """Custom type IntPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(21, 65535),
    )





class IntProtocolType(Integer32):
    """Custom type IntProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )





class IntL4Port(Integer32):
    """Custom type IntL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )





class IntIcmpType(Integer32):
    """Custom type IntIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )





class IntIcmpCode(Integer32):
    """Custom type IntIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )





class IntInternetProtocolFlag(Integer32):
    """Custom type IntInternetProtocolFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("tcp", 1),
          ("ucp", 2),
          ("icmp", 3))
    )





class IntRulePriority(Integer32):
    """Custom type IntRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4),
          ("lowest", 5),
          ("highMiddle", 6))
    )





class IntFlowClass(Integer32):
    """Custom type IntFlowClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("flow", 1),
          ("class", 2),
          ("both", 4))
    )





class IntVlanID(Integer32):
    """Custom type IntVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )





class IntQueue(Integer32):
    """Custom type IntQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )





class IntDP(Integer32):
    """Custom type IntDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2),
    )





class IntCoS(Integer32):
    """Custom type IntCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )





class IntDscp(Integer32):
    """Custom type IntDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )





class IntIpPrecedence(Integer32):
    """Custom type IntIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )





class IntDstMacOrEgressPorts(Integer32):
    """Custom type IntDstMacOrEgressPorts based on Integer32"""
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
          ("dstMac", 1),
          ("egressPorts", 2))
    )





class IntMarkMode(Integer32):
    """Custom type IntMarkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("markByEntry", 1),
          ("dSCPAttribute", 2),
          ("entryDSCP", 3))
    )





class IntMeterMode(Integer32):
    """Custom type IntMeterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("rateLimit", 1),
          ("color", 2),
          ("minmaxbandwidth", 3))
    )





class IntColorType(Integer32):
    """Custom type IntColorType based on Integer32"""
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
          ("srTCM", 1),
          ("trTCM", 2))
    )





class IntColorMode(Integer32):
    """Custom type IntColorMode based on Integer32"""
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
          ("blind", 1),
          ("aware", 2))
    )





class IntColorAwareMode(Integer32):
    """Custom type IntColorAwareMode based on Integer32"""
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
          ("unprotected", 1),
          ("protected", 2))
    )





class IntColorCIR(Integer32):
    """Custom type IntColorCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1000000),
    )





class IntColorCBS(Integer32):
    """Custom type IntColorCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4000),
    )





class IntColorPIR(Integer32):
    """Custom type IntColorPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1000000),
    )





class IntColorPBS(Integer32):
    """Custom type IntColorPBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4000),
    )





class IntColorEBS(Integer32):
    """Custom type IntColorEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4000),
    )





class IntColorAction(Integer32):
    """Custom type IntColorAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("drop", 1),
          ("marking", 2),
          ("dropPrecedence", 3),
          ("dropPrecedenceRed", 4),
          ("dropPrecedenceYellow", 5),
          ("dropPrecedenceGreen", 6))
    )





class IntCounterMode(Integer32):
    """Custom type IntCounterMode based on Integer32"""
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
          ("byte", 1),
          ("packet", 2))
    )





class IntInterfaceIndex(Integer32):
    """Custom type IntInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 512),
    )





class IntFlowOrClass(Integer32):
    """Custom type IntFlowOrClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flow", 1),
          ("class", 2))
    )





class IntL2BaseRemarkMode(Integer32):
    """Custom type IntL2BaseRemarkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remarkByQueue", 1),
          ("remarkByPriority", 2))
    )





class IntColorIndex(Integer32):
    """Custom type IntColorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )





class IntDSCPIndex(Integer32):
    """Custom type IntDSCPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )





class IntQueueCoSIndex(Integer32):
    """Custom type IntQueueCoSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )





class IntIpPktPriorityType(Integer32):
    """Custom type IntIpPktPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("iPPrecedence", 1),
          ("diffServ", 2),
          ("ipToS", 3))
    )





class IntEnableFlag(Integer32):
    """Custom type IntEnableFlag based on Integer32"""
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





class IntAvrgCounterMode(Integer32):
    """Custom type IntAvrgCounterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("byte", 1))
    )




# TEXTUAL-CONVENTIONS



class MacAddressMask(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



# MIB Managed Objects in the order of their OIDs

_SleV2QoSBase_ObjectIdentity = ObjectIdentity
sleV2QoSBase = _SleV2QoSBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 1)
)
_SleV2QoS4_ObjectIdentity = ObjectIdentity
sleV2QoS4 = _SleV2QoS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2)
)
_SleV2QoS4Base_ObjectIdentity = ObjectIdentity
sleV2QoS4Base = _SleV2QoS4Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1)
)
_SleV2QoS4BaseInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4BaseInfo = _SleV2QoS4BaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 1)
)


class _SleV2QoS4BaseFlowMode_Type(Integer32):
    """Custom type sleV2QoS4BaseFlowMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("extension", 2))
    )


_SleV2QoS4BaseFlowMode_Type.__name__ = "Integer32"
_SleV2QoS4BaseFlowMode_Object = MibScalar
sleV2QoS4BaseFlowMode = _SleV2QoS4BaseFlowMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 1, 1),
    _SleV2QoS4BaseFlowMode_Type()
)
sleV2QoS4BaseFlowMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4BaseFlowMode.setStatus("current")
_SleV2QoS4BaseControl_ObjectIdentity = ObjectIdentity
sleV2QoS4BaseControl = _SleV2QoS4BaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 2)
)


class _SleV2QoS4BaseControlRequest_Type(Integer32):
    """Custom type sleV2QoS4BaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setFlowMode", 1)
    )


_SleV2QoS4BaseControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4BaseControlRequest_Object = MibScalar
sleV2QoS4BaseControlRequest = _SleV2QoS4BaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 2, 1),
    _SleV2QoS4BaseControlRequest_Type()
)
sleV2QoS4BaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4BaseControlRequest.setStatus("current")
_SleV2QoS4BaseControlStatus_Type = SleControlStatusType
_SleV2QoS4BaseControlStatus_Object = MibScalar
sleV2QoS4BaseControlStatus = _SleV2QoS4BaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 2, 2),
    _SleV2QoS4BaseControlStatus_Type()
)
sleV2QoS4BaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4BaseControlStatus.setStatus("current")
_SleV2QoS4BaseControlTimer_Type = Gauge32
_SleV2QoS4BaseControlTimer_Object = MibScalar
sleV2QoS4BaseControlTimer = _SleV2QoS4BaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 2, 3),
    _SleV2QoS4BaseControlTimer_Type()
)
sleV2QoS4BaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4BaseControlTimer.setStatus("current")
_SleV2QoS4BaseControlTimeStamp_Type = TimeTicks
_SleV2QoS4BaseControlTimeStamp_Object = MibScalar
sleV2QoS4BaseControlTimeStamp = _SleV2QoS4BaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 2, 4),
    _SleV2QoS4BaseControlTimeStamp_Type()
)
sleV2QoS4BaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4BaseControlTimeStamp.setStatus("current")
_SleV2QoS4BaseControlResult_Type = SleControlRequestResultType
_SleV2QoS4BaseControlResult_Object = MibScalar
sleV2QoS4BaseControlResult = _SleV2QoS4BaseControlResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 2, 5),
    _SleV2QoS4BaseControlResult_Type()
)
sleV2QoS4BaseControlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4BaseControlResult.setStatus("current")


class _SleV2QoS4BaseControlFlowMode_Type(Integer32):
    """Custom type sleV2QoS4BaseControlFlowMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("extension", 2))
    )


_SleV2QoS4BaseControlFlowMode_Type.__name__ = "Integer32"
_SleV2QoS4BaseControlFlowMode_Object = MibScalar
sleV2QoS4BaseControlFlowMode = _SleV2QoS4BaseControlFlowMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 2, 6),
    _SleV2QoS4BaseControlFlowMode_Type()
)
sleV2QoS4BaseControlFlowMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4BaseControlFlowMode.setStatus("current")
_SleV2QoS4BaseNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4BaseNotification = _SleV2QoS4BaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 3)
)
_SleV2QoS4Flow_ObjectIdentity = ObjectIdentity
sleV2QoS4Flow = _SleV2QoS4Flow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2)
)
_SleV2QoS4FlowInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4FlowInfo = _SleV2QoS4FlowInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1)
)
_SleV2QoS4FlowTable_Object = MibTable
sleV2QoS4FlowTable = _SleV2QoS4FlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4FlowTable.setStatus("current")
_SleV2QoS4FlowEntry_Object = MibTableRow
sleV2QoS4FlowEntry = _SleV2QoS4FlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1)
)
sleV2QoS4FlowEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4FlowIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4FlowEntry.setStatus("current")


class _SleV2QoS4FlowIndex_Type(Integer32):
    """Custom type sleV2QoS4FlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SleV2QoS4FlowIndex_Type.__name__ = "Integer32"
_SleV2QoS4FlowIndex_Object = MibTableColumn
sleV2QoS4FlowIndex = _SleV2QoS4FlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 1),
    _SleV2QoS4FlowIndex_Type()
)
sleV2QoS4FlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowIndex.setStatus("current")
_SleV2QoS4FlowName_Type = OctetName
_SleV2QoS4FlowName_Object = MibTableColumn
sleV2QoS4FlowName = _SleV2QoS4FlowName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 2),
    _SleV2QoS4FlowName_Type()
)
sleV2QoS4FlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowName.setStatus("current")
_SleV2QoS4FlowEthernetType_Type = IntEthernetType
_SleV2QoS4FlowEthernetType_Object = MibTableColumn
sleV2QoS4FlowEthernetType = _SleV2QoS4FlowEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 3),
    _SleV2QoS4FlowEthernetType_Type()
)
sleV2QoS4FlowEthernetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowEthernetType.setStatus("current")
_SleV2QoS4FlowSrcMacAddr_Type = MacAddress
_SleV2QoS4FlowSrcMacAddr_Object = MibTableColumn
sleV2QoS4FlowSrcMacAddr = _SleV2QoS4FlowSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 4),
    _SleV2QoS4FlowSrcMacAddr_Type()
)
sleV2QoS4FlowSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowSrcMacAddr.setStatus("current")
_SleV2QoS4FlowSrcMacAddrMask_Type = MacAddressMask
_SleV2QoS4FlowSrcMacAddrMask_Object = MibTableColumn
sleV2QoS4FlowSrcMacAddrMask = _SleV2QoS4FlowSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 5),
    _SleV2QoS4FlowSrcMacAddrMask_Type()
)
sleV2QoS4FlowSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowSrcMacAddrMask.setStatus("current")
_SleV2QoS4FlowDstMacAddr_Type = MacAddress
_SleV2QoS4FlowDstMacAddr_Object = MibTableColumn
sleV2QoS4FlowDstMacAddr = _SleV2QoS4FlowDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 6),
    _SleV2QoS4FlowDstMacAddr_Type()
)
sleV2QoS4FlowDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowDstMacAddr.setStatus("current")
_SleV2QoS4FlowDstMacAddrMask_Type = MacAddressMask
_SleV2QoS4FlowDstMacAddrMask_Object = MibTableColumn
sleV2QoS4FlowDstMacAddrMask = _SleV2QoS4FlowDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 7),
    _SleV2QoS4FlowDstMacAddrMask_Type()
)
sleV2QoS4FlowDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowDstMacAddrMask.setStatus("current")
_SleV2QoS4Flow8021p_Type = Int8021p
_SleV2QoS4Flow8021p_Object = MibTableColumn
sleV2QoS4Flow8021p = _SleV2QoS4Flow8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 8),
    _SleV2QoS4Flow8021p_Type()
)
sleV2QoS4Flow8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4Flow8021p.setStatus("current")
_SleV2QoS4FlowSrcIpAddr_Type = IpAddress
_SleV2QoS4FlowSrcIpAddr_Object = MibTableColumn
sleV2QoS4FlowSrcIpAddr = _SleV2QoS4FlowSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 9),
    _SleV2QoS4FlowSrcIpAddr_Type()
)
sleV2QoS4FlowSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowSrcIpAddr.setStatus("current")
_SleV2QoS4FlowSrcIpAddrMask_Type = IntIpAddrMask
_SleV2QoS4FlowSrcIpAddrMask_Object = MibTableColumn
sleV2QoS4FlowSrcIpAddrMask = _SleV2QoS4FlowSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 10),
    _SleV2QoS4FlowSrcIpAddrMask_Type()
)
sleV2QoS4FlowSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowSrcIpAddrMask.setStatus("current")
_SleV2QoS4FlowDstIpAddr_Type = IpAddress
_SleV2QoS4FlowDstIpAddr_Object = MibTableColumn
sleV2QoS4FlowDstIpAddr = _SleV2QoS4FlowDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 11),
    _SleV2QoS4FlowDstIpAddr_Type()
)
sleV2QoS4FlowDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowDstIpAddr.setStatus("current")
_SleV2QoS4FlowDstIpAddrMask_Type = IntIpAddrMask
_SleV2QoS4FlowDstIpAddrMask_Object = MibTableColumn
sleV2QoS4FlowDstIpAddrMask = _SleV2QoS4FlowDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 12),
    _SleV2QoS4FlowDstIpAddrMask_Type()
)
sleV2QoS4FlowDstIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowDstIpAddrMask.setStatus("current")
_SleV2QoS4FlowIpPktPriorityType_Type = IntIpPktPriorityType
_SleV2QoS4FlowIpPktPriorityType_Object = MibTableColumn
sleV2QoS4FlowIpPktPriorityType = _SleV2QoS4FlowIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 13),
    _SleV2QoS4FlowIpPktPriorityType_Type()
)
sleV2QoS4FlowIpPktPriorityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowIpPktPriorityType.setStatus("current")
_SleV2QoS4FlowIpPktPriority_Type = Integer32
_SleV2QoS4FlowIpPktPriority_Object = MibTableColumn
sleV2QoS4FlowIpPktPriority = _SleV2QoS4FlowIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 14),
    _SleV2QoS4FlowIpPktPriority_Type()
)
sleV2QoS4FlowIpPktPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowIpPktPriority.setStatus("current")
_SleV2QoS4FlowPktLen_Type = IntPktLen
_SleV2QoS4FlowPktLen_Object = MibTableColumn
sleV2QoS4FlowPktLen = _SleV2QoS4FlowPktLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 15),
    _SleV2QoS4FlowPktLen_Type()
)
sleV2QoS4FlowPktLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowPktLen.setStatus("current")
_SleV2QoS4FlowProtocolType_Type = IntProtocolType
_SleV2QoS4FlowProtocolType_Object = MibTableColumn
sleV2QoS4FlowProtocolType = _SleV2QoS4FlowProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 16),
    _SleV2QoS4FlowProtocolType_Type()
)
sleV2QoS4FlowProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowProtocolType.setStatus("current")
_SleV2QoS4FlowTcpSrcStartPort_Type = IntL4Port
_SleV2QoS4FlowTcpSrcStartPort_Object = MibTableColumn
sleV2QoS4FlowTcpSrcStartPort = _SleV2QoS4FlowTcpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 17),
    _SleV2QoS4FlowTcpSrcStartPort_Type()
)
sleV2QoS4FlowTcpSrcStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowTcpSrcStartPort.setStatus("current")
_SleV2QoS4FlowTcpSrcEndPort_Type = IntL4Port
_SleV2QoS4FlowTcpSrcEndPort_Object = MibTableColumn
sleV2QoS4FlowTcpSrcEndPort = _SleV2QoS4FlowTcpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 18),
    _SleV2QoS4FlowTcpSrcEndPort_Type()
)
sleV2QoS4FlowTcpSrcEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowTcpSrcEndPort.setStatus("current")
_SleV2QoS4FlowTcpDstStartPort_Type = IntL4Port
_SleV2QoS4FlowTcpDstStartPort_Object = MibTableColumn
sleV2QoS4FlowTcpDstStartPort = _SleV2QoS4FlowTcpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 19),
    _SleV2QoS4FlowTcpDstStartPort_Type()
)
sleV2QoS4FlowTcpDstStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowTcpDstStartPort.setStatus("current")
_SleV2QoS4FlowTcpDstEndPort_Type = IntL4Port
_SleV2QoS4FlowTcpDstEndPort_Object = MibTableColumn
sleV2QoS4FlowTcpDstEndPort = _SleV2QoS4FlowTcpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 20),
    _SleV2QoS4FlowTcpDstEndPort_Type()
)
sleV2QoS4FlowTcpDstEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowTcpDstEndPort.setStatus("current")


class _SleV2QoS4FlowTcpFlag_Type(Bits):
    """Custom type sleV2QoS4FlowTcpFlag based on Bits"""
    namedValues = NamedValues(
        *(("reserv0", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleV2QoS4FlowTcpFlag_Type.__name__ = "Bits"
_SleV2QoS4FlowTcpFlag_Object = MibTableColumn
sleV2QoS4FlowTcpFlag = _SleV2QoS4FlowTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 21),
    _SleV2QoS4FlowTcpFlag_Type()
)
sleV2QoS4FlowTcpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowTcpFlag.setStatus("current")
_SleV2QoS4FlowUdpSrcStartPort_Type = IntL4Port
_SleV2QoS4FlowUdpSrcStartPort_Object = MibTableColumn
sleV2QoS4FlowUdpSrcStartPort = _SleV2QoS4FlowUdpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 22),
    _SleV2QoS4FlowUdpSrcStartPort_Type()
)
sleV2QoS4FlowUdpSrcStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowUdpSrcStartPort.setStatus("current")
_SleV2QoS4FlowUdpSrcEndPort_Type = IntL4Port
_SleV2QoS4FlowUdpSrcEndPort_Object = MibTableColumn
sleV2QoS4FlowUdpSrcEndPort = _SleV2QoS4FlowUdpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 23),
    _SleV2QoS4FlowUdpSrcEndPort_Type()
)
sleV2QoS4FlowUdpSrcEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowUdpSrcEndPort.setStatus("current")
_SleV2QoS4FlowUdpDstStartPort_Type = IntL4Port
_SleV2QoS4FlowUdpDstStartPort_Object = MibTableColumn
sleV2QoS4FlowUdpDstStartPort = _SleV2QoS4FlowUdpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 24),
    _SleV2QoS4FlowUdpDstStartPort_Type()
)
sleV2QoS4FlowUdpDstStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowUdpDstStartPort.setStatus("current")
_SleV2QoS4FlowUdpDstEndPort_Type = IntL4Port
_SleV2QoS4FlowUdpDstEndPort_Object = MibTableColumn
sleV2QoS4FlowUdpDstEndPort = _SleV2QoS4FlowUdpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 25),
    _SleV2QoS4FlowUdpDstEndPort_Type()
)
sleV2QoS4FlowUdpDstEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowUdpDstEndPort.setStatus("current")
_SleV2QoS4FlowIcmpType_Type = IntIcmpType
_SleV2QoS4FlowIcmpType_Object = MibTableColumn
sleV2QoS4FlowIcmpType = _SleV2QoS4FlowIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 26),
    _SleV2QoS4FlowIcmpType_Type()
)
sleV2QoS4FlowIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowIcmpType.setStatus("current")
_SleV2QoS4FlowIcmpCode_Type = IntIcmpCode
_SleV2QoS4FlowIcmpCode_Object = MibTableColumn
sleV2QoS4FlowIcmpCode = _SleV2QoS4FlowIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 27),
    _SleV2QoS4FlowIcmpCode_Type()
)
sleV2QoS4FlowIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowIcmpCode.setStatus("current")


class _SleV2QoS4FlowHdrlen_Type(Integer32):
    """Custom type sleV2QoS4FlowHdrlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4FlowHdrlen_Type.__name__ = "Integer32"
_SleV2QoS4FlowHdrlen_Object = MibTableColumn
sleV2QoS4FlowHdrlen = _SleV2QoS4FlowHdrlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 28),
    _SleV2QoS4FlowHdrlen_Type()
)
sleV2QoS4FlowHdrlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowHdrlen.setStatus("current")
_SleV2QoS4FlowHdrError_Type = IntEnableFlag
_SleV2QoS4FlowHdrError_Object = MibTableColumn
sleV2QoS4FlowHdrError = _SleV2QoS4FlowHdrError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 29),
    _SleV2QoS4FlowHdrError_Type()
)
sleV2QoS4FlowHdrError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowHdrError.setStatus("current")


class _SleV2QoS4FlowInnerVlan_Type(Integer32):
    """Custom type sleV2QoS4FlowInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2QoS4FlowInnerVlan_Type.__name__ = "Integer32"
_SleV2QoS4FlowInnerVlan_Object = MibTableColumn
sleV2QoS4FlowInnerVlan = _SleV2QoS4FlowInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 30),
    _SleV2QoS4FlowInnerVlan_Type()
)
sleV2QoS4FlowInnerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowInnerVlan.setStatus("current")


class _SleV2QoS4FlowInner8021p_Type(Integer32):
    """Custom type sleV2QoS4FlowInner8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4FlowInner8021p_Type.__name__ = "Integer32"
_SleV2QoS4FlowInner8021p_Object = MibTableColumn
sleV2QoS4FlowInner8021p = _SleV2QoS4FlowInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 31),
    _SleV2QoS4FlowInner8021p_Type()
)
sleV2QoS4FlowInner8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowInner8021p.setStatus("current")


class _SleV2QoS4FlowMacFlag_Type(Integer32):
    """Custom type sleV2QoS4FlowMacFlag based on Integer32"""
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
        *(("none", 0),
          ("srcAny", 1),
          ("dstAny", 2),
          ("srcDstAny", 3))
    )


_SleV2QoS4FlowMacFlag_Type.__name__ = "Integer32"
_SleV2QoS4FlowMacFlag_Object = MibTableColumn
sleV2QoS4FlowMacFlag = _SleV2QoS4FlowMacFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 32),
    _SleV2QoS4FlowMacFlag_Type()
)
sleV2QoS4FlowMacFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowMacFlag.setStatus("current")


class _SleV2QoS4FlowIpFlag_Type(Integer32):
    """Custom type sleV2QoS4FlowIpFlag based on Integer32"""
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
        *(("none", 0),
          ("srcAny", 1),
          ("dstAny", 2),
          ("srcDstAny", 3))
    )


_SleV2QoS4FlowIpFlag_Type.__name__ = "Integer32"
_SleV2QoS4FlowIpFlag_Object = MibTableColumn
sleV2QoS4FlowIpFlag = _SleV2QoS4FlowIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 33),
    _SleV2QoS4FlowIpFlag_Type()
)
sleV2QoS4FlowIpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowIpFlag.setStatus("current")


class _SleV2QoS4FlowMacDlf_Type(Integer32):
    """Custom type sleV2QoS4FlowMacDlf based on Integer32"""
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
          ("dstFound", 1),
          ("dstNotFound", 2))
    )


_SleV2QoS4FlowMacDlf_Type.__name__ = "Integer32"
_SleV2QoS4FlowMacDlf_Object = MibTableColumn
sleV2QoS4FlowMacDlf = _SleV2QoS4FlowMacDlf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 34),
    _SleV2QoS4FlowMacDlf_Type()
)
sleV2QoS4FlowMacDlf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowMacDlf.setStatus("current")


class _SleV2QoS4FlowTagType_Type(Integer32):
    """Custom type sleV2QoS4FlowTagType based on Integer32"""
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
        *(("untag", 1),
          ("custom", 2),
          ("service", 3),
          ("both", 4))
    )


_SleV2QoS4FlowTagType_Type.__name__ = "Integer32"
_SleV2QoS4FlowTagType_Object = MibTableColumn
sleV2QoS4FlowTagType = _SleV2QoS4FlowTagType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 35),
    _SleV2QoS4FlowTagType_Type()
)
sleV2QoS4FlowTagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowTagType.setStatus("current")


class _SleV2QoS4FlowInPktTagVid_Type(Integer32):
    """Custom type sleV2QoS4FlowInPktTagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_SleV2QoS4FlowInPktTagVid_Type.__name__ = "Integer32"
_SleV2QoS4FlowInPktTagVid_Object = MibTableColumn
sleV2QoS4FlowInPktTagVid = _SleV2QoS4FlowInPktTagVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 36),
    _SleV2QoS4FlowInPktTagVid_Type()
)
sleV2QoS4FlowInPktTagVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowInPktTagVid.setStatus("current")


class _SleV2QoS4FlowInPktTagCfi_Type(Integer32):
    """Custom type sleV2QoS4FlowInPktTagCfi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(255, 255),
    )


_SleV2QoS4FlowInPktTagCfi_Type.__name__ = "Integer32"
_SleV2QoS4FlowInPktTagCfi_Object = MibTableColumn
sleV2QoS4FlowInPktTagCfi = _SleV2QoS4FlowInPktTagCfi_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 37),
    _SleV2QoS4FlowInPktTagCfi_Type()
)
sleV2QoS4FlowInPktTagCfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowInPktTagCfi.setStatus("current")


class _SleV2QoS4FlowInPktTagCoS_Type(Integer32):
    """Custom type sleV2QoS4FlowInPktTagCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_SleV2QoS4FlowInPktTagCoS_Type.__name__ = "Integer32"
_SleV2QoS4FlowInPktTagCoS_Object = MibTableColumn
sleV2QoS4FlowInPktTagCoS = _SleV2QoS4FlowInPktTagCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 38),
    _SleV2QoS4FlowInPktTagCoS_Type()
)
sleV2QoS4FlowInPktTagCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowInPktTagCoS.setStatus("current")


class _SleV2QoS4FlowOutPktTagVid_Type(Integer32):
    """Custom type sleV2QoS4FlowOutPktTagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_SleV2QoS4FlowOutPktTagVid_Type.__name__ = "Integer32"
_SleV2QoS4FlowOutPktTagVid_Object = MibTableColumn
sleV2QoS4FlowOutPktTagVid = _SleV2QoS4FlowOutPktTagVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 39),
    _SleV2QoS4FlowOutPktTagVid_Type()
)
sleV2QoS4FlowOutPktTagVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowOutPktTagVid.setStatus("current")


class _SleV2QoS4FlowOutPktTagCfi_Type(Integer32):
    """Custom type sleV2QoS4FlowOutPktTagCfi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(255, 255),
    )


_SleV2QoS4FlowOutPktTagCfi_Type.__name__ = "Integer32"
_SleV2QoS4FlowOutPktTagCfi_Object = MibTableColumn
sleV2QoS4FlowOutPktTagCfi = _SleV2QoS4FlowOutPktTagCfi_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 40),
    _SleV2QoS4FlowOutPktTagCfi_Type()
)
sleV2QoS4FlowOutPktTagCfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowOutPktTagCfi.setStatus("current")


class _SleV2QoS4FlowOutPktTagCoS_Type(Integer32):
    """Custom type sleV2QoS4FlowOutPktTagCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_SleV2QoS4FlowOutPktTagCoS_Type.__name__ = "Integer32"
_SleV2QoS4FlowOutPktTagCoS_Object = MibTableColumn
sleV2QoS4FlowOutPktTagCoS = _SleV2QoS4FlowOutPktTagCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 41),
    _SleV2QoS4FlowOutPktTagCoS_Type()
)
sleV2QoS4FlowOutPktTagCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowOutPktTagCoS.setStatus("current")
_SleV2QoS4FlowFlowAlias_Type = OctetString
_SleV2QoS4FlowFlowAlias_Object = MibTableColumn
sleV2QoS4FlowFlowAlias = _SleV2QoS4FlowFlowAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 42),
    _SleV2QoS4FlowFlowAlias_Type()
)
sleV2QoS4FlowFlowAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowFlowAlias.setStatus("current")
_SleV2QoSFlowInetAddrType_Type = InetAddressType
_SleV2QoSFlowInetAddrType_Object = MibTableColumn
sleV2QoSFlowInetAddrType = _SleV2QoSFlowInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 43),
    _SleV2QoSFlowInetAddrType_Type()
)
sleV2QoSFlowInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowInetAddrType.setStatus("current")
_SleV2QoSFlowSrcInetAddr_Type = InetAddress
_SleV2QoSFlowSrcInetAddr_Object = MibTableColumn
sleV2QoSFlowSrcInetAddr = _SleV2QoSFlowSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 44),
    _SleV2QoSFlowSrcInetAddr_Type()
)
sleV2QoSFlowSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowSrcInetAddr.setStatus("current")
_SleV2QoSFlowDstInetAddr_Type = InetAddress
_SleV2QoSFlowDstInetAddr_Object = MibTableColumn
sleV2QoSFlowDstInetAddr = _SleV2QoSFlowDstInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 45),
    _SleV2QoSFlowDstInetAddr_Type()
)
sleV2QoSFlowDstInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowDstInetAddr.setStatus("current")
_SleV2QoSFlowSrcInetAddrLen_Type = InetAddressPrefixLength
_SleV2QoSFlowSrcInetAddrLen_Object = MibTableColumn
sleV2QoSFlowSrcInetAddrLen = _SleV2QoSFlowSrcInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 46),
    _SleV2QoSFlowSrcInetAddrLen_Type()
)
sleV2QoSFlowSrcInetAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowSrcInetAddrLen.setStatus("current")
_SleV2QoSFlowDstInetAddrLen_Type = InetAddressPrefixLength
_SleV2QoSFlowDstInetAddrLen_Object = MibTableColumn
sleV2QoSFlowDstInetAddrLen = _SleV2QoSFlowDstInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 47),
    _SleV2QoSFlowDstInetAddrLen_Type()
)
sleV2QoSFlowDstInetAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowDstInetAddrLen.setStatus("current")


class _SleV2QoSFlowTrafficClass_Type(Integer32):
    """Custom type sleV2QoSFlowTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_SleV2QoSFlowTrafficClass_Type.__name__ = "Integer32"
_SleV2QoSFlowTrafficClass_Object = MibTableColumn
sleV2QoSFlowTrafficClass = _SleV2QoSFlowTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 48),
    _SleV2QoSFlowTrafficClass_Type()
)
sleV2QoSFlowTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowTrafficClass.setStatus("current")


class _SleV2QoSFlowFlowLabel_Type(Integer32):
    """Custom type sleV2QoSFlowFlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoSFlowFlowLabel_Type.__name__ = "Integer32"
_SleV2QoSFlowFlowLabel_Object = MibTableColumn
sleV2QoSFlowFlowLabel = _SleV2QoSFlowFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 49),
    _SleV2QoSFlowFlowLabel_Type()
)
sleV2QoSFlowFlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowFlowLabel.setStatus("current")


class _SleV2QoS4FlowOuterVlan_Type(Integer32):
    """Custom type sleV2QoS4FlowOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4094),
    )


_SleV2QoS4FlowOuterVlan_Type.__name__ = "Integer32"
_SleV2QoS4FlowOuterVlan_Object = MibTableColumn
sleV2QoS4FlowOuterVlan = _SleV2QoS4FlowOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 50),
    _SleV2QoS4FlowOuterVlan_Type()
)
sleV2QoS4FlowOuterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowOuterVlan.setStatus("current")


class _SleV2QoS4FlowOuter8021p_Type(Integer32):
    """Custom type sleV2QoS4FlowOuter8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4FlowOuter8021p_Type.__name__ = "Integer32"
_SleV2QoS4FlowOuter8021p_Object = MibTableColumn
sleV2QoS4FlowOuter8021p = _SleV2QoS4FlowOuter8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 51),
    _SleV2QoS4FlowOuter8021p_Type()
)
sleV2QoS4FlowOuter8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowOuter8021p.setStatus("current")


class _SleV2QoS4FlowOnuCircuitId_Type(Integer32):
    """Custom type sleV2QoS4FlowOnuCircuitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 50000),
        ValueRangeConstraint(50002, 50002),
        ValueRangeConstraint(50003, 50003),
        ValueRangeConstraint(50004, 50004),
        ValueRangeConstraint(51002, 51002),
    )


_SleV2QoS4FlowOnuCircuitId_Type.__name__ = "Integer32"
_SleV2QoS4FlowOnuCircuitId_Object = MibTableColumn
sleV2QoS4FlowOnuCircuitId = _SleV2QoS4FlowOnuCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 1, 1, 52),
    _SleV2QoS4FlowOnuCircuitId_Type()
)
sleV2QoS4FlowOnuCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowOnuCircuitId.setStatus("current")
_SleV2QoS4FlowControl_ObjectIdentity = ObjectIdentity
sleV2QoS4FlowControl = _SleV2QoS4FlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2)
)


class _SleV2QoS4FlowControlRequest_Type(Integer32):
    """Custom type sleV2QoS4FlowControlRequest based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("createFlow", 1),
          ("modifyFlow", 2),
          ("destroyFlow", 3),
          ("destroyAllFlow", 4),
          ("setInPktTag", 5),
          ("setOutPktTag", 6),
          ("setFlowAlias", 7),
          ("createFlowEx", 8),
          ("setFlowEx", 9))
    )


_SleV2QoS4FlowControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlRequest_Object = MibScalar
sleV2QoS4FlowControlRequest = _SleV2QoS4FlowControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 1),
    _SleV2QoS4FlowControlRequest_Type()
)
sleV2QoS4FlowControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlRequest.setStatus("current")
_SleV2QoS4FlowControlStatus_Type = SleControlStatusType
_SleV2QoS4FlowControlStatus_Object = MibScalar
sleV2QoS4FlowControlStatus = _SleV2QoS4FlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 2),
    _SleV2QoS4FlowControlStatus_Type()
)
sleV2QoS4FlowControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlStatus.setStatus("current")
_SleV2QoS4FlowControlTimer_Type = Gauge32
_SleV2QoS4FlowControlTimer_Object = MibScalar
sleV2QoS4FlowControlTimer = _SleV2QoS4FlowControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 3),
    _SleV2QoS4FlowControlTimer_Type()
)
sleV2QoS4FlowControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTimer.setStatus("current")
_SleV2QoS4FlowControlTimeStamp_Type = TimeTicks
_SleV2QoS4FlowControlTimeStamp_Object = MibScalar
sleV2QoS4FlowControlTimeStamp = _SleV2QoS4FlowControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 4),
    _SleV2QoS4FlowControlTimeStamp_Type()
)
sleV2QoS4FlowControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTimeStamp.setStatus("current")
_SleV2QoS4FlowControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4FlowControlReqResult_Object = MibScalar
sleV2QoS4FlowControlReqResult = _SleV2QoS4FlowControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 5),
    _SleV2QoS4FlowControlReqResult_Type()
)
sleV2QoS4FlowControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlReqResult.setStatus("current")
_SleV2QoS4FlowControlIndex_Type = IntFlowIndex
_SleV2QoS4FlowControlIndex_Object = MibScalar
sleV2QoS4FlowControlIndex = _SleV2QoS4FlowControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 6),
    _SleV2QoS4FlowControlIndex_Type()
)
sleV2QoS4FlowControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlIndex.setStatus("current")
_SleV2QoS4FlowControlName_Type = OctetName
_SleV2QoS4FlowControlName_Object = MibScalar
sleV2QoS4FlowControlName = _SleV2QoS4FlowControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 7),
    _SleV2QoS4FlowControlName_Type()
)
sleV2QoS4FlowControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlName.setStatus("current")
_SleV2QoS4FlowControlEthernetType_Type = IntEthernetType
_SleV2QoS4FlowControlEthernetType_Object = MibScalar
sleV2QoS4FlowControlEthernetType = _SleV2QoS4FlowControlEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 8),
    _SleV2QoS4FlowControlEthernetType_Type()
)
sleV2QoS4FlowControlEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlEthernetType.setStatus("current")
_SleV2QoS4FlowControlSrcMacAddr_Type = MacAddress
_SleV2QoS4FlowControlSrcMacAddr_Object = MibScalar
sleV2QoS4FlowControlSrcMacAddr = _SleV2QoS4FlowControlSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 9),
    _SleV2QoS4FlowControlSrcMacAddr_Type()
)
sleV2QoS4FlowControlSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlSrcMacAddr.setStatus("current")
_SleV2QoS4FlowControlSrcMacAddrMask_Type = MacAddressMask
_SleV2QoS4FlowControlSrcMacAddrMask_Object = MibScalar
sleV2QoS4FlowControlSrcMacAddrMask = _SleV2QoS4FlowControlSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 10),
    _SleV2QoS4FlowControlSrcMacAddrMask_Type()
)
sleV2QoS4FlowControlSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlSrcMacAddrMask.setStatus("current")
_SleV2QoS4FlowControlDstMacAddr_Type = MacAddress
_SleV2QoS4FlowControlDstMacAddr_Object = MibScalar
sleV2QoS4FlowControlDstMacAddr = _SleV2QoS4FlowControlDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 11),
    _SleV2QoS4FlowControlDstMacAddr_Type()
)
sleV2QoS4FlowControlDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlDstMacAddr.setStatus("current")
_SleV2QoS4FlowControlDstMacAddrMask_Type = MacAddressMask
_SleV2QoS4FlowControlDstMacAddrMask_Object = MibScalar
sleV2QoS4FlowControlDstMacAddrMask = _SleV2QoS4FlowControlDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 12),
    _SleV2QoS4FlowControlDstMacAddrMask_Type()
)
sleV2QoS4FlowControlDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlDstMacAddrMask.setStatus("current")
_SleV2QoS4FlowControl8021p_Type = Int8021p
_SleV2QoS4FlowControl8021p_Object = MibScalar
sleV2QoS4FlowControl8021p = _SleV2QoS4FlowControl8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 13),
    _SleV2QoS4FlowControl8021p_Type()
)
sleV2QoS4FlowControl8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControl8021p.setStatus("current")
_SleV2QoS4FlowControlSrcIpAddr_Type = IpAddress
_SleV2QoS4FlowControlSrcIpAddr_Object = MibScalar
sleV2QoS4FlowControlSrcIpAddr = _SleV2QoS4FlowControlSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 14),
    _SleV2QoS4FlowControlSrcIpAddr_Type()
)
sleV2QoS4FlowControlSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlSrcIpAddr.setStatus("current")
_SleV2QoS4FlowControlSrcIpAddrMask_Type = IntIpAddrMask
_SleV2QoS4FlowControlSrcIpAddrMask_Object = MibScalar
sleV2QoS4FlowControlSrcIpAddrMask = _SleV2QoS4FlowControlSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 15),
    _SleV2QoS4FlowControlSrcIpAddrMask_Type()
)
sleV2QoS4FlowControlSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlSrcIpAddrMask.setStatus("current")
_SleV2QoS4FlowControlDstIpAddr_Type = IpAddress
_SleV2QoS4FlowControlDstIpAddr_Object = MibScalar
sleV2QoS4FlowControlDstIpAddr = _SleV2QoS4FlowControlDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 16),
    _SleV2QoS4FlowControlDstIpAddr_Type()
)
sleV2QoS4FlowControlDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlDstIpAddr.setStatus("current")
_SleV2QoS4FlowControlDstIpAddrMask_Type = IntIpAddrMask
_SleV2QoS4FlowControlDstIpAddrMask_Object = MibScalar
sleV2QoS4FlowControlDstIpAddrMask = _SleV2QoS4FlowControlDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 17),
    _SleV2QoS4FlowControlDstIpAddrMask_Type()
)
sleV2QoS4FlowControlDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlDstIpAddrMask.setStatus("current")
_SleV2QoS4FlowControlIpPktPriorityType_Type = IntIpPktPriorityType
_SleV2QoS4FlowControlIpPktPriorityType_Object = MibScalar
sleV2QoS4FlowControlIpPktPriorityType = _SleV2QoS4FlowControlIpPktPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 18),
    _SleV2QoS4FlowControlIpPktPriorityType_Type()
)
sleV2QoS4FlowControlIpPktPriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlIpPktPriorityType.setStatus("current")
_SleV2QoS4FlowControlIpPktPriority_Type = Integer32
_SleV2QoS4FlowControlIpPktPriority_Object = MibScalar
sleV2QoS4FlowControlIpPktPriority = _SleV2QoS4FlowControlIpPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 19),
    _SleV2QoS4FlowControlIpPktPriority_Type()
)
sleV2QoS4FlowControlIpPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlIpPktPriority.setStatus("current")
_SleV2QoS4FlowControlPktLen_Type = IntPktLen
_SleV2QoS4FlowControlPktLen_Object = MibScalar
sleV2QoS4FlowControlPktLen = _SleV2QoS4FlowControlPktLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 20),
    _SleV2QoS4FlowControlPktLen_Type()
)
sleV2QoS4FlowControlPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlPktLen.setStatus("current")
_SleV2QoS4FlowControlProtocolType_Type = IntProtocolType
_SleV2QoS4FlowControlProtocolType_Object = MibScalar
sleV2QoS4FlowControlProtocolType = _SleV2QoS4FlowControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 21),
    _SleV2QoS4FlowControlProtocolType_Type()
)
sleV2QoS4FlowControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlProtocolType.setStatus("current")
_SleV2QoS4FlowControlTcpSrcStartPort_Type = IntL4Port
_SleV2QoS4FlowControlTcpSrcStartPort_Object = MibScalar
sleV2QoS4FlowControlTcpSrcStartPort = _SleV2QoS4FlowControlTcpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 22),
    _SleV2QoS4FlowControlTcpSrcStartPort_Type()
)
sleV2QoS4FlowControlTcpSrcStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTcpSrcStartPort.setStatus("current")
_SleV2QoS4FlowControlTcpSrcEndPort_Type = IntL4Port
_SleV2QoS4FlowControlTcpSrcEndPort_Object = MibScalar
sleV2QoS4FlowControlTcpSrcEndPort = _SleV2QoS4FlowControlTcpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 23),
    _SleV2QoS4FlowControlTcpSrcEndPort_Type()
)
sleV2QoS4FlowControlTcpSrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTcpSrcEndPort.setStatus("current")
_SleV2QoS4FlowControlTcpDstStartPort_Type = IntL4Port
_SleV2QoS4FlowControlTcpDstStartPort_Object = MibScalar
sleV2QoS4FlowControlTcpDstStartPort = _SleV2QoS4FlowControlTcpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 24),
    _SleV2QoS4FlowControlTcpDstStartPort_Type()
)
sleV2QoS4FlowControlTcpDstStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTcpDstStartPort.setStatus("current")
_SleV2QoS4FlowControlTcpDstEndPort_Type = IntL4Port
_SleV2QoS4FlowControlTcpDstEndPort_Object = MibScalar
sleV2QoS4FlowControlTcpDstEndPort = _SleV2QoS4FlowControlTcpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 25),
    _SleV2QoS4FlowControlTcpDstEndPort_Type()
)
sleV2QoS4FlowControlTcpDstEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTcpDstEndPort.setStatus("current")


class _SleV2QoS4FlowControlTcpFlag_Type(Bits):
    """Custom type sleV2QoS4FlowControlTcpFlag based on Bits"""
    namedValues = NamedValues(
        *(("reserv0", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleV2QoS4FlowControlTcpFlag_Type.__name__ = "Bits"
_SleV2QoS4FlowControlTcpFlag_Object = MibScalar
sleV2QoS4FlowControlTcpFlag = _SleV2QoS4FlowControlTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 26),
    _SleV2QoS4FlowControlTcpFlag_Type()
)
sleV2QoS4FlowControlTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTcpFlag.setStatus("current")
_SleV2QoS4FlowControlUdpSrcStartPort_Type = IntL4Port
_SleV2QoS4FlowControlUdpSrcStartPort_Object = MibScalar
sleV2QoS4FlowControlUdpSrcStartPort = _SleV2QoS4FlowControlUdpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 27),
    _SleV2QoS4FlowControlUdpSrcStartPort_Type()
)
sleV2QoS4FlowControlUdpSrcStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlUdpSrcStartPort.setStatus("current")
_SleV2QoS4FlowControlUdpSrcEndPort_Type = IntL4Port
_SleV2QoS4FlowControlUdpSrcEndPort_Object = MibScalar
sleV2QoS4FlowControlUdpSrcEndPort = _SleV2QoS4FlowControlUdpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 28),
    _SleV2QoS4FlowControlUdpSrcEndPort_Type()
)
sleV2QoS4FlowControlUdpSrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlUdpSrcEndPort.setStatus("current")
_SleV2QoS4FlowControlUdpDstStartPort_Type = IntL4Port
_SleV2QoS4FlowControlUdpDstStartPort_Object = MibScalar
sleV2QoS4FlowControlUdpDstStartPort = _SleV2QoS4FlowControlUdpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 29),
    _SleV2QoS4FlowControlUdpDstStartPort_Type()
)
sleV2QoS4FlowControlUdpDstStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlUdpDstStartPort.setStatus("current")
_SleV2QoS4FlowControlUdpDstEndPort_Type = IntL4Port
_SleV2QoS4FlowControlUdpDstEndPort_Object = MibScalar
sleV2QoS4FlowControlUdpDstEndPort = _SleV2QoS4FlowControlUdpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 30),
    _SleV2QoS4FlowControlUdpDstEndPort_Type()
)
sleV2QoS4FlowControlUdpDstEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlUdpDstEndPort.setStatus("current")
_SleV2QoS4FlowControlIcmpType_Type = IntIcmpType
_SleV2QoS4FlowControlIcmpType_Object = MibScalar
sleV2QoS4FlowControlIcmpType = _SleV2QoS4FlowControlIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 31),
    _SleV2QoS4FlowControlIcmpType_Type()
)
sleV2QoS4FlowControlIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlIcmpType.setStatus("current")
_SleV2QoS4FlowControlIcmpCode_Type = IntIcmpCode
_SleV2QoS4FlowControlIcmpCode_Object = MibScalar
sleV2QoS4FlowControlIcmpCode = _SleV2QoS4FlowControlIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 32),
    _SleV2QoS4FlowControlIcmpCode_Type()
)
sleV2QoS4FlowControlIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlIcmpCode.setStatus("current")


class _SleV2QoS4FlowControlHdrlen_Type(Integer32):
    """Custom type sleV2QoS4FlowControlHdrlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4FlowControlHdrlen_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlHdrlen_Object = MibScalar
sleV2QoS4FlowControlHdrlen = _SleV2QoS4FlowControlHdrlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 33),
    _SleV2QoS4FlowControlHdrlen_Type()
)
sleV2QoS4FlowControlHdrlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlHdrlen.setStatus("current")
_SleV2QoS4FlowControlHdrError_Type = IntEnableFlag
_SleV2QoS4FlowControlHdrError_Object = MibScalar
sleV2QoS4FlowControlHdrError = _SleV2QoS4FlowControlHdrError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 34),
    _SleV2QoS4FlowControlHdrError_Type()
)
sleV2QoS4FlowControlHdrError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlHdrError.setStatus("current")


class _SleV2QoS4FlowControlInnerVlan_Type(Integer32):
    """Custom type sleV2QoS4FlowControlInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2QoS4FlowControlInnerVlan_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlInnerVlan_Object = MibScalar
sleV2QoS4FlowControlInnerVlan = _SleV2QoS4FlowControlInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 35),
    _SleV2QoS4FlowControlInnerVlan_Type()
)
sleV2QoS4FlowControlInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlInnerVlan.setStatus("current")


class _SleV2QoS4FlowControlInner8021p_Type(Integer32):
    """Custom type sleV2QoS4FlowControlInner8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4FlowControlInner8021p_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlInner8021p_Object = MibScalar
sleV2QoS4FlowControlInner8021p = _SleV2QoS4FlowControlInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 36),
    _SleV2QoS4FlowControlInner8021p_Type()
)
sleV2QoS4FlowControlInner8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlInner8021p.setStatus("current")


class _SleV2QoS4FlowControlMacFlag_Type(Integer32):
    """Custom type sleV2QoS4FlowControlMacFlag based on Integer32"""
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
        *(("none", 0),
          ("srcAny", 1),
          ("dstAny", 2),
          ("srcDstAny", 3))
    )


_SleV2QoS4FlowControlMacFlag_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlMacFlag_Object = MibScalar
sleV2QoS4FlowControlMacFlag = _SleV2QoS4FlowControlMacFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 37),
    _SleV2QoS4FlowControlMacFlag_Type()
)
sleV2QoS4FlowControlMacFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlMacFlag.setStatus("current")


class _SleV2QoS4FlowControlIpFlag_Type(Integer32):
    """Custom type sleV2QoS4FlowControlIpFlag based on Integer32"""
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
        *(("none", 0),
          ("srcAny", 1),
          ("dstAny", 2),
          ("srcDstAny", 3))
    )


_SleV2QoS4FlowControlIpFlag_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlIpFlag_Object = MibScalar
sleV2QoS4FlowControlIpFlag = _SleV2QoS4FlowControlIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 38),
    _SleV2QoS4FlowControlIpFlag_Type()
)
sleV2QoS4FlowControlIpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlIpFlag.setStatus("current")


class _SleV2QoS4FlowControlMacDlf_Type(Integer32):
    """Custom type sleV2QoS4FlowControlMacDlf based on Integer32"""
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
          ("dstFound", 1),
          ("dstNotFound", 2))
    )


_SleV2QoS4FlowControlMacDlf_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlMacDlf_Object = MibScalar
sleV2QoS4FlowControlMacDlf = _SleV2QoS4FlowControlMacDlf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 39),
    _SleV2QoS4FlowControlMacDlf_Type()
)
sleV2QoS4FlowControlMacDlf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlMacDlf.setStatus("current")


class _SleV2QoS4FlowControlTagType_Type(Integer32):
    """Custom type sleV2QoS4FlowControlTagType based on Integer32"""
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
        *(("untag", 1),
          ("custom", 2),
          ("service", 3),
          ("both", 4))
    )


_SleV2QoS4FlowControlTagType_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlTagType_Object = MibScalar
sleV2QoS4FlowControlTagType = _SleV2QoS4FlowControlTagType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 40),
    _SleV2QoS4FlowControlTagType_Type()
)
sleV2QoS4FlowControlTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlTagType.setStatus("current")


class _SleV2QoS4FlowControlPktTagVid_Type(Integer32):
    """Custom type sleV2QoS4FlowControlPktTagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_SleV2QoS4FlowControlPktTagVid_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlPktTagVid_Object = MibScalar
sleV2QoS4FlowControlPktTagVid = _SleV2QoS4FlowControlPktTagVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 41),
    _SleV2QoS4FlowControlPktTagVid_Type()
)
sleV2QoS4FlowControlPktTagVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlPktTagVid.setStatus("current")


class _SleV2QoS4FlowControlPktTagCfi_Type(Integer32):
    """Custom type sleV2QoS4FlowControlPktTagCfi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(255, 255),
    )


_SleV2QoS4FlowControlPktTagCfi_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlPktTagCfi_Object = MibScalar
sleV2QoS4FlowControlPktTagCfi = _SleV2QoS4FlowControlPktTagCfi_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 42),
    _SleV2QoS4FlowControlPktTagCfi_Type()
)
sleV2QoS4FlowControlPktTagCfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlPktTagCfi.setStatus("current")


class _SleV2QoS4FlowControlPktTagCoS_Type(Integer32):
    """Custom type sleV2QoS4FlowControlPktTagCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_SleV2QoS4FlowControlPktTagCoS_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlPktTagCoS_Object = MibScalar
sleV2QoS4FlowControlPktTagCoS = _SleV2QoS4FlowControlPktTagCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 43),
    _SleV2QoS4FlowControlPktTagCoS_Type()
)
sleV2QoS4FlowControlPktTagCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlPktTagCoS.setStatus("current")
_SleV2QoS4FlowControlFlowAlias_Type = OctetString
_SleV2QoS4FlowControlFlowAlias_Object = MibScalar
sleV2QoS4FlowControlFlowAlias = _SleV2QoS4FlowControlFlowAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 44),
    _SleV2QoS4FlowControlFlowAlias_Type()
)
sleV2QoS4FlowControlFlowAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlFlowAlias.setStatus("current")
_SleV2QoSFlowControlInetAddrType_Type = InetAddressType
_SleV2QoSFlowControlInetAddrType_Object = MibScalar
sleV2QoSFlowControlInetAddrType = _SleV2QoSFlowControlInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 45),
    _SleV2QoSFlowControlInetAddrType_Type()
)
sleV2QoSFlowControlInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowControlInetAddrType.setStatus("current")
_SleV2QoSFlowControlSrcInetAddr_Type = InetAddress
_SleV2QoSFlowControlSrcInetAddr_Object = MibScalar
sleV2QoSFlowControlSrcInetAddr = _SleV2QoSFlowControlSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 46),
    _SleV2QoSFlowControlSrcInetAddr_Type()
)
sleV2QoSFlowControlSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowControlSrcInetAddr.setStatus("current")
_SleV2QoSFlowControlDstInetAddr_Type = InetAddress
_SleV2QoSFlowControlDstInetAddr_Object = MibScalar
sleV2QoSFlowControlDstInetAddr = _SleV2QoSFlowControlDstInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 47),
    _SleV2QoSFlowControlDstInetAddr_Type()
)
sleV2QoSFlowControlDstInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowControlDstInetAddr.setStatus("current")
_SleV2QoSFlowControlSrcInetAddrLen_Type = InetAddressPrefixLength
_SleV2QoSFlowControlSrcInetAddrLen_Object = MibScalar
sleV2QoSFlowControlSrcInetAddrLen = _SleV2QoSFlowControlSrcInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 48),
    _SleV2QoSFlowControlSrcInetAddrLen_Type()
)
sleV2QoSFlowControlSrcInetAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowControlSrcInetAddrLen.setStatus("current")
_SleV2QoSFlowControlDstInetAddrLen_Type = InetAddressPrefixLength
_SleV2QoSFlowControlDstInetAddrLen_Object = MibScalar
sleV2QoSFlowControlDstInetAddrLen = _SleV2QoSFlowControlDstInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 49),
    _SleV2QoSFlowControlDstInetAddrLen_Type()
)
sleV2QoSFlowControlDstInetAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoSFlowControlDstInetAddrLen.setStatus("current")


class _SleV2QoSFlowControlTrafficClass_Type(Integer32):
    """Custom type sleV2QoSFlowControlTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_SleV2QoSFlowControlTrafficClass_Type.__name__ = "Integer32"
_SleV2QoSFlowControlTrafficClass_Object = MibScalar
sleV2QoSFlowControlTrafficClass = _SleV2QoSFlowControlTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 50),
    _SleV2QoSFlowControlTrafficClass_Type()
)
sleV2QoSFlowControlTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoSFlowControlTrafficClass.setStatus("current")


class _SleV2QoSFlowControlFlowLabel_Type(Integer32):
    """Custom type sleV2QoSFlowControlFlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoSFlowControlFlowLabel_Type.__name__ = "Integer32"
_SleV2QoSFlowControlFlowLabel_Object = MibScalar
sleV2QoSFlowControlFlowLabel = _SleV2QoSFlowControlFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 51),
    _SleV2QoSFlowControlFlowLabel_Type()
)
sleV2QoSFlowControlFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoSFlowControlFlowLabel.setStatus("current")


class _SleV2QoS4FlowControlOuterVlan_Type(Integer32):
    """Custom type sleV2QoS4FlowControlOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_SleV2QoS4FlowControlOuterVlan_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlOuterVlan_Object = MibScalar
sleV2QoS4FlowControlOuterVlan = _SleV2QoS4FlowControlOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 52),
    _SleV2QoS4FlowControlOuterVlan_Type()
)
sleV2QoS4FlowControlOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlOuterVlan.setStatus("current")


class _SleV2QoS4FlowControlOuter8021p_Type(Integer32):
    """Custom type sleV2QoS4FlowControlOuter8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4FlowControlOuter8021p_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlOuter8021p_Object = MibScalar
sleV2QoS4FlowControlOuter8021p = _SleV2QoS4FlowControlOuter8021p_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 53),
    _SleV2QoS4FlowControlOuter8021p_Type()
)
sleV2QoS4FlowControlOuter8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlOuter8021p.setStatus("current")


class _SleV2QoS4FlowControlOnuCircuitId_Type(Integer32):
    """Custom type sleV2QoS4FlowControlOnuCircuitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 5000),
        ValueRangeConstraint(50002, 50002),
        ValueRangeConstraint(50003, 50003),
        ValueRangeConstraint(50004, 50004),
        ValueRangeConstraint(51002, 51002),
    )


_SleV2QoS4FlowControlOnuCircuitId_Type.__name__ = "Integer32"
_SleV2QoS4FlowControlOnuCircuitId_Object = MibScalar
sleV2QoS4FlowControlOnuCircuitId = _SleV2QoS4FlowControlOnuCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 2, 54),
    _SleV2QoS4FlowControlOnuCircuitId_Type()
)
sleV2QoS4FlowControlOnuCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4FlowControlOnuCircuitId.setStatus("current")
_SleV2QoS4FlowNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4FlowNotification = _SleV2QoS4FlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3)
)
_SleV2QoS4FlowClass_ObjectIdentity = ObjectIdentity
sleV2QoS4FlowClass = _SleV2QoS4FlowClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 2)
)
_SleV2QoS4FlowClassTable_Object = MibTable
sleV2QoS4FlowClassTable = _SleV2QoS4FlowClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4FlowClassTable.setStatus("current")
_SleV2QoS4FlowClassEntry_Object = MibTableRow
sleV2QoS4FlowClassEntry = _SleV2QoS4FlowClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 2, 1, 1)
)
sleV2QoS4FlowClassEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4FlowIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4FlowClassIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4FlowClassEntry.setStatus("current")
_SleV2QoS4FlowClassIndex_Type = IntClassIndex
_SleV2QoS4FlowClassIndex_Object = MibTableColumn
sleV2QoS4FlowClassIndex = _SleV2QoS4FlowClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 2, 1, 1, 1),
    _SleV2QoS4FlowClassIndex_Type()
)
sleV2QoS4FlowClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowClassIndex.setStatus("current")
_SleV2QoS4FlowClassID_Type = IntClassIndex
_SleV2QoS4FlowClassID_Object = MibTableColumn
sleV2QoS4FlowClassID = _SleV2QoS4FlowClassID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 2, 1, 1, 2),
    _SleV2QoS4FlowClassID_Type()
)
sleV2QoS4FlowClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowClassID.setStatus("current")
_SleV2QoS4FlowClassName_Type = OctetName
_SleV2QoS4FlowClassName_Object = MibTableColumn
sleV2QoS4FlowClassName = _SleV2QoS4FlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 2, 1, 1, 3),
    _SleV2QoS4FlowClassName_Type()
)
sleV2QoS4FlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowClassName.setStatus("current")
_SleV2QoS4FlowPolicy_ObjectIdentity = ObjectIdentity
sleV2QoS4FlowPolicy = _SleV2QoS4FlowPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 3)
)
_SleV2QoS4FlowPolicyTable_Object = MibTable
sleV2QoS4FlowPolicyTable = _SleV2QoS4FlowPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4FlowPolicyTable.setStatus("current")
_SleV2QoS4FlowPolicyEntry_Object = MibTableRow
sleV2QoS4FlowPolicyEntry = _SleV2QoS4FlowPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 3, 1, 1)
)
sleV2QoS4FlowPolicyEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4FlowIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4FlowPolicyIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4FlowPolicyEntry.setStatus("current")
_SleV2QoS4FlowPolicyIndex_Type = IntPolicyIndex
_SleV2QoS4FlowPolicyIndex_Object = MibTableColumn
sleV2QoS4FlowPolicyIndex = _SleV2QoS4FlowPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 3, 1, 1, 1),
    _SleV2QoS4FlowPolicyIndex_Type()
)
sleV2QoS4FlowPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowPolicyIndex.setStatus("current")
_SleV2QoS4FlowPolicyID_Type = IntPolicyIndex
_SleV2QoS4FlowPolicyID_Object = MibTableColumn
sleV2QoS4FlowPolicyID = _SleV2QoS4FlowPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 3, 1, 1, 2),
    _SleV2QoS4FlowPolicyID_Type()
)
sleV2QoS4FlowPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowPolicyID.setStatus("current")
_SleV2QoS4FlowPolicyName_Type = OctetName
_SleV2QoS4FlowPolicyName_Object = MibTableColumn
sleV2QoS4FlowPolicyName = _SleV2QoS4FlowPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 3, 1, 1, 3),
    _SleV2QoS4FlowPolicyName_Type()
)
sleV2QoS4FlowPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4FlowPolicyName.setStatus("current")
_SleV2QoS4Class_ObjectIdentity = ObjectIdentity
sleV2QoS4Class = _SleV2QoS4Class_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3)
)
_SleV2QoS4ClassInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4ClassInfo = _SleV2QoS4ClassInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1)
)
_SleV2QoS4ClassTable_Object = MibTable
sleV2QoS4ClassTable = _SleV2QoS4ClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4ClassTable.setStatus("current")
_SleV2QoS4ClassEntry_Object = MibTableRow
sleV2QoS4ClassEntry = _SleV2QoS4ClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 1, 1)
)
sleV2QoS4ClassEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4ClassIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4ClassEntry.setStatus("current")
_SleV2QoS4ClassIndex_Type = IntClassIndex
_SleV2QoS4ClassIndex_Object = MibTableColumn
sleV2QoS4ClassIndex = _SleV2QoS4ClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 1, 1, 1),
    _SleV2QoS4ClassIndex_Type()
)
sleV2QoS4ClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassIndex.setStatus("current")
_SleV2QoS4ClassName_Type = OctetName
_SleV2QoS4ClassName_Object = MibTableColumn
sleV2QoS4ClassName = _SleV2QoS4ClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 1, 1, 2),
    _SleV2QoS4ClassName_Type()
)
sleV2QoS4ClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassName.setStatus("current")
_SleV2QoS4ClassFlowCnt_Type = Counter32
_SleV2QoS4ClassFlowCnt_Object = MibTableColumn
sleV2QoS4ClassFlowCnt = _SleV2QoS4ClassFlowCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 1, 1, 3),
    _SleV2QoS4ClassFlowCnt_Type()
)
sleV2QoS4ClassFlowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowCnt.setStatus("current")
_SleV2QoS4ClassControl_ObjectIdentity = ObjectIdentity
sleV2QoS4ClassControl = _SleV2QoS4ClassControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2)
)


class _SleV2QoS4ClassControlRequest_Type(Integer32):
    """Custom type sleV2QoS4ClassControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createClass", 1),
          ("destroyClass", 2),
          ("destroyAllClass", 3))
    )


_SleV2QoS4ClassControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4ClassControlRequest_Object = MibScalar
sleV2QoS4ClassControlRequest = _SleV2QoS4ClassControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2, 1),
    _SleV2QoS4ClassControlRequest_Type()
)
sleV2QoS4ClassControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassControlRequest.setStatus("current")
_SleV2QoS4ClassControlStatus_Type = SleControlStatusType
_SleV2QoS4ClassControlStatus_Object = MibScalar
sleV2QoS4ClassControlStatus = _SleV2QoS4ClassControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2, 2),
    _SleV2QoS4ClassControlStatus_Type()
)
sleV2QoS4ClassControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassControlStatus.setStatus("current")
_SleV2QoS4ClassControlTimer_Type = Gauge32
_SleV2QoS4ClassControlTimer_Object = MibScalar
sleV2QoS4ClassControlTimer = _SleV2QoS4ClassControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2, 3),
    _SleV2QoS4ClassControlTimer_Type()
)
sleV2QoS4ClassControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassControlTimer.setStatus("current")
_SleV2QoS4ClassControlTimeStamp_Type = TimeTicks
_SleV2QoS4ClassControlTimeStamp_Object = MibScalar
sleV2QoS4ClassControlTimeStamp = _SleV2QoS4ClassControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2, 4),
    _SleV2QoS4ClassControlTimeStamp_Type()
)
sleV2QoS4ClassControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassControlTimeStamp.setStatus("current")
_SleV2QoS4ClassControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4ClassControlReqResult_Object = MibScalar
sleV2QoS4ClassControlReqResult = _SleV2QoS4ClassControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2, 5),
    _SleV2QoS4ClassControlReqResult_Type()
)
sleV2QoS4ClassControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassControlReqResult.setStatus("current")
_SleV2QoS4ClassControlIndex_Type = IntClassIndex
_SleV2QoS4ClassControlIndex_Object = MibScalar
sleV2QoS4ClassControlIndex = _SleV2QoS4ClassControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2, 6),
    _SleV2QoS4ClassControlIndex_Type()
)
sleV2QoS4ClassControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassControlIndex.setStatus("current")
_SleV2QoS4ClassControlName_Type = OctetName
_SleV2QoS4ClassControlName_Object = MibScalar
sleV2QoS4ClassControlName = _SleV2QoS4ClassControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 2, 7),
    _SleV2QoS4ClassControlName_Type()
)
sleV2QoS4ClassControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassControlName.setStatus("current")
_SleV2QoS4ClassNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4ClassNotification = _SleV2QoS4ClassNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 3)
)
_SleV2QoS4ClassFlow_ObjectIdentity = ObjectIdentity
sleV2QoS4ClassFlow = _SleV2QoS4ClassFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2)
)
_SleV2QoS4ClassFlowTable_Object = MibTable
sleV2QoS4ClassFlowTable = _SleV2QoS4ClassFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowTable.setStatus("current")
_SleV2QoS4ClassFlowEntry_Object = MibTableRow
sleV2QoS4ClassFlowEntry = _SleV2QoS4ClassFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 1, 1)
)
sleV2QoS4ClassFlowEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4ClassIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4ClassFlowIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowEntry.setStatus("current")
_SleV2QoS4ClassFlowIndex_Type = IntFlowIndex
_SleV2QoS4ClassFlowIndex_Object = MibTableColumn
sleV2QoS4ClassFlowIndex = _SleV2QoS4ClassFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 1, 1, 1),
    _SleV2QoS4ClassFlowIndex_Type()
)
sleV2QoS4ClassFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowIndex.setStatus("current")
_SleV2QoS4ClassFlowID_Type = IntFlowIndex
_SleV2QoS4ClassFlowID_Object = MibTableColumn
sleV2QoS4ClassFlowID = _SleV2QoS4ClassFlowID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 1, 1, 2),
    _SleV2QoS4ClassFlowID_Type()
)
sleV2QoS4ClassFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowID.setStatus("current")
_SleV2QoS4ClassFlowName_Type = OctetName
_SleV2QoS4ClassFlowName_Object = MibTableColumn
sleV2QoS4ClassFlowName = _SleV2QoS4ClassFlowName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 1, 1, 3),
    _SleV2QoS4ClassFlowName_Type()
)
sleV2QoS4ClassFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowName.setStatus("current")
_SleV2QoS4ClassFlowClassName_Type = OctetName
_SleV2QoS4ClassFlowClassName_Object = MibTableColumn
sleV2QoS4ClassFlowClassName = _SleV2QoS4ClassFlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 1, 1, 4),
    _SleV2QoS4ClassFlowClassName_Type()
)
sleV2QoS4ClassFlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowClassName.setStatus("current")
_SleV2QoS4ClassFlowControl_ObjectIdentity = ObjectIdentity
sleV2QoS4ClassFlowControl = _SleV2QoS4ClassFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2)
)


class _SleV2QoS4ClassFlowControlRequest_Type(Integer32):
    """Custom type sleV2QoS4ClassFlowControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addFlow", 1),
          ("deleteFlow", 2),
          ("deleteAllFlow", 3))
    )


_SleV2QoS4ClassFlowControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4ClassFlowControlRequest_Object = MibScalar
sleV2QoS4ClassFlowControlRequest = _SleV2QoS4ClassFlowControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 1),
    _SleV2QoS4ClassFlowControlRequest_Type()
)
sleV2QoS4ClassFlowControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlRequest.setStatus("current")
_SleV2QoS4ClassFlowControlStatus_Type = SleControlStatusType
_SleV2QoS4ClassFlowControlStatus_Object = MibScalar
sleV2QoS4ClassFlowControlStatus = _SleV2QoS4ClassFlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 2),
    _SleV2QoS4ClassFlowControlStatus_Type()
)
sleV2QoS4ClassFlowControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlStatus.setStatus("current")
_SleV2QoS4ClassFlowControlTimer_Type = Gauge32
_SleV2QoS4ClassFlowControlTimer_Object = MibScalar
sleV2QoS4ClassFlowControlTimer = _SleV2QoS4ClassFlowControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 3),
    _SleV2QoS4ClassFlowControlTimer_Type()
)
sleV2QoS4ClassFlowControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlTimer.setStatus("current")
_SleV2QoS4ClassFlowControlTimeStamp_Type = TimeTicks
_SleV2QoS4ClassFlowControlTimeStamp_Object = MibScalar
sleV2QoS4ClassFlowControlTimeStamp = _SleV2QoS4ClassFlowControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 4),
    _SleV2QoS4ClassFlowControlTimeStamp_Type()
)
sleV2QoS4ClassFlowControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlTimeStamp.setStatus("current")
_SleV2QoS4ClassFlowControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4ClassFlowControlReqResult_Object = MibScalar
sleV2QoS4ClassFlowControlReqResult = _SleV2QoS4ClassFlowControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 5),
    _SleV2QoS4ClassFlowControlReqResult_Type()
)
sleV2QoS4ClassFlowControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlReqResult.setStatus("current")
_SleV2QoS4ClassFlowControlClassIndex_Type = IntClassIndex
_SleV2QoS4ClassFlowControlClassIndex_Object = MibScalar
sleV2QoS4ClassFlowControlClassIndex = _SleV2QoS4ClassFlowControlClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 6),
    _SleV2QoS4ClassFlowControlClassIndex_Type()
)
sleV2QoS4ClassFlowControlClassIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlClassIndex.setStatus("current")
_SleV2QoS4ClassFlowControlFlowIndex_Type = IntFlowIndex
_SleV2QoS4ClassFlowControlFlowIndex_Object = MibScalar
sleV2QoS4ClassFlowControlFlowIndex = _SleV2QoS4ClassFlowControlFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 7),
    _SleV2QoS4ClassFlowControlFlowIndex_Type()
)
sleV2QoS4ClassFlowControlFlowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlFlowIndex.setStatus("current")
_SleV2QoS4ClassFlowControlFlowID_Type = IntFlowIndex
_SleV2QoS4ClassFlowControlFlowID_Object = MibScalar
sleV2QoS4ClassFlowControlFlowID = _SleV2QoS4ClassFlowControlFlowID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 8),
    _SleV2QoS4ClassFlowControlFlowID_Type()
)
sleV2QoS4ClassFlowControlFlowID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlFlowID.setStatus("current")
_SleV2QoS4ClassFlowControlClassName_Type = OctetName
_SleV2QoS4ClassFlowControlClassName_Object = MibScalar
sleV2QoS4ClassFlowControlClassName = _SleV2QoS4ClassFlowControlClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 2, 9),
    _SleV2QoS4ClassFlowControlClassName_Type()
)
sleV2QoS4ClassFlowControlClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4ClassFlowControlClassName.setStatus("current")
_SleV2QoS4ClassFlowNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4ClassFlowNotification = _SleV2QoS4ClassFlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 3)
)
_SleV2QoS4ClassPolicy_ObjectIdentity = ObjectIdentity
sleV2QoS4ClassPolicy = _SleV2QoS4ClassPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 3)
)
_SleV2QoS4ClassPolicyTable_Object = MibTable
sleV2QoS4ClassPolicyTable = _SleV2QoS4ClassPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4ClassPolicyTable.setStatus("current")
_SleV2QoS4ClassPolicyEntry_Object = MibTableRow
sleV2QoS4ClassPolicyEntry = _SleV2QoS4ClassPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 3, 1, 1)
)
sleV2QoS4ClassPolicyEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4ClassIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4ClassPolicyIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4ClassPolicyEntry.setStatus("current")
_SleV2QoS4ClassPolicyIndex_Type = IntPolicyIndex
_SleV2QoS4ClassPolicyIndex_Object = MibTableColumn
sleV2QoS4ClassPolicyIndex = _SleV2QoS4ClassPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 3, 1, 1, 1),
    _SleV2QoS4ClassPolicyIndex_Type()
)
sleV2QoS4ClassPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassPolicyIndex.setStatus("current")
_SleV2QoS4ClassPolicyID_Type = IntPolicyIndex
_SleV2QoS4ClassPolicyID_Object = MibTableColumn
sleV2QoS4ClassPolicyID = _SleV2QoS4ClassPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 3, 1, 1, 2),
    _SleV2QoS4ClassPolicyID_Type()
)
sleV2QoS4ClassPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassPolicyID.setStatus("current")
_SleV2QoS4ClassPolicyName_Type = OctetName
_SleV2QoS4ClassPolicyName_Object = MibTableColumn
sleV2QoS4ClassPolicyName = _SleV2QoS4ClassPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 3, 1, 1, 3),
    _SleV2QoS4ClassPolicyName_Type()
)
sleV2QoS4ClassPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4ClassPolicyName.setStatus("current")
_SleV2QoS4Policer_ObjectIdentity = ObjectIdentity
sleV2QoS4Policer = _SleV2QoS4Policer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4)
)
_SleV2QoS4PolicerInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicerInfo = _SleV2QoS4PolicerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1)
)
_SleV2QoS4PolicerTable_Object = MibTable
sleV2QoS4PolicerTable = _SleV2QoS4PolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicerTable.setStatus("current")
_SleV2QoS4PolicerEntry_Object = MibTableRow
sleV2QoS4PolicerEntry = _SleV2QoS4PolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1)
)
sleV2QoS4PolicerEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PolicerIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicerEntry.setStatus("current")
_SleV2QoS4PolicerIndex_Type = IntPolicerIndex
_SleV2QoS4PolicerIndex_Object = MibTableColumn
sleV2QoS4PolicerIndex = _SleV2QoS4PolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 1),
    _SleV2QoS4PolicerIndex_Type()
)
sleV2QoS4PolicerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerIndex.setStatus("current")
_SleV2QoS4PolicerName_Type = OctetName
_SleV2QoS4PolicerName_Object = MibTableColumn
sleV2QoS4PolicerName = _SleV2QoS4PolicerName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 2),
    _SleV2QoS4PolicerName_Type()
)
sleV2QoS4PolicerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerName.setStatus("current")
_SleV2QoS4PolicerMeterMode_Type = IntMeterMode
_SleV2QoS4PolicerMeterMode_Object = MibTableColumn
sleV2QoS4PolicerMeterMode = _SleV2QoS4PolicerMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 3),
    _SleV2QoS4PolicerMeterMode_Type()
)
sleV2QoS4PolicerMeterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMeterMode.setStatus("current")
_SleV2QoS4PolicerRateLimit_Type = Integer32
_SleV2QoS4PolicerRateLimit_Object = MibTableColumn
sleV2QoS4PolicerRateLimit = _SleV2QoS4PolicerRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 4),
    _SleV2QoS4PolicerRateLimit_Type()
)
sleV2QoS4PolicerRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerRateLimit.setStatus("current")
_SleV2QoS4PolicerColorType_Type = IntColorType
_SleV2QoS4PolicerColorType_Object = MibTableColumn
sleV2QoS4PolicerColorType = _SleV2QoS4PolicerColorType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 5),
    _SleV2QoS4PolicerColorType_Type()
)
sleV2QoS4PolicerColorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorType.setStatus("current")
_SleV2QoS4PolicerColorMode_Type = IntColorMode
_SleV2QoS4PolicerColorMode_Object = MibTableColumn
sleV2QoS4PolicerColorMode = _SleV2QoS4PolicerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 6),
    _SleV2QoS4PolicerColorMode_Type()
)
sleV2QoS4PolicerColorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorMode.setStatus("current")
_SleV2QoS4PolicerColorAwareMode_Type = IntColorAwareMode
_SleV2QoS4PolicerColorAwareMode_Object = MibTableColumn
sleV2QoS4PolicerColorAwareMode = _SleV2QoS4PolicerColorAwareMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 7),
    _SleV2QoS4PolicerColorAwareMode_Type()
)
sleV2QoS4PolicerColorAwareMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorAwareMode.setStatus("current")
_SleV2QoS4PolicerColorCIR_Type = IntColorCIR
_SleV2QoS4PolicerColorCIR_Object = MibTableColumn
sleV2QoS4PolicerColorCIR = _SleV2QoS4PolicerColorCIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 8),
    _SleV2QoS4PolicerColorCIR_Type()
)
sleV2QoS4PolicerColorCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorCIR.setStatus("current")
_SleV2QoS4PolicerColorCBS_Type = IntColorCBS
_SleV2QoS4PolicerColorCBS_Object = MibTableColumn
sleV2QoS4PolicerColorCBS = _SleV2QoS4PolicerColorCBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 9),
    _SleV2QoS4PolicerColorCBS_Type()
)
sleV2QoS4PolicerColorCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorCBS.setStatus("current")
_SleV2QoS4PolicerColorPIR_Type = IntColorPIR
_SleV2QoS4PolicerColorPIR_Object = MibTableColumn
sleV2QoS4PolicerColorPIR = _SleV2QoS4PolicerColorPIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 10),
    _SleV2QoS4PolicerColorPIR_Type()
)
sleV2QoS4PolicerColorPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorPIR.setStatus("current")
_SleV2QoS4PolicerColorPBS_Type = IntColorPBS
_SleV2QoS4PolicerColorPBS_Object = MibTableColumn
sleV2QoS4PolicerColorPBS = _SleV2QoS4PolicerColorPBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 11),
    _SleV2QoS4PolicerColorPBS_Type()
)
sleV2QoS4PolicerColorPBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorPBS.setStatus("current")
_SleV2QoS4PolicerColorEBS_Type = IntColorEBS
_SleV2QoS4PolicerColorEBS_Object = MibTableColumn
sleV2QoS4PolicerColorEBS = _SleV2QoS4PolicerColorEBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 12),
    _SleV2QoS4PolicerColorEBS_Type()
)
sleV2QoS4PolicerColorEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorEBS.setStatus("current")
_SleV2QoS4PolicerColorRedAction_Type = IntColorAction
_SleV2QoS4PolicerColorRedAction_Object = MibTableColumn
sleV2QoS4PolicerColorRedAction = _SleV2QoS4PolicerColorRedAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 13),
    _SleV2QoS4PolicerColorRedAction_Type()
)
sleV2QoS4PolicerColorRedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorRedAction.setStatus("current")
_SleV2QoS4PolicerColorYellowAction_Type = IntColorAction
_SleV2QoS4PolicerColorYellowAction_Object = MibTableColumn
sleV2QoS4PolicerColorYellowAction = _SleV2QoS4PolicerColorYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 14),
    _SleV2QoS4PolicerColorYellowAction_Type()
)
sleV2QoS4PolicerColorYellowAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorYellowAction.setStatus("current")
_SleV2QoS4PolicerColorGreenAction_Type = IntColorAction
_SleV2QoS4PolicerColorGreenAction_Object = MibTableColumn
sleV2QoS4PolicerColorGreenAction = _SleV2QoS4PolicerColorGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 15),
    _SleV2QoS4PolicerColorGreenAction_Type()
)
sleV2QoS4PolicerColorGreenAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorGreenAction.setStatus("current")


class _SleV2QoS4PolicerRemarkLayerMode_Type(Bits):
    """Custom type sleV2QoS4PolicerRemarkLayerMode based on Bits"""
    namedValues = NamedValues(
        *(("remarkByDSCP", 0),
          ("remarkByQueueOrCoS", 1))
    )

_SleV2QoS4PolicerRemarkLayerMode_Type.__name__ = "Bits"
_SleV2QoS4PolicerRemarkLayerMode_Object = MibTableColumn
sleV2QoS4PolicerRemarkLayerMode = _SleV2QoS4PolicerRemarkLayerMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 16),
    _SleV2QoS4PolicerRemarkLayerMode_Type()
)
sleV2QoS4PolicerRemarkLayerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerRemarkLayerMode.setStatus("current")


class _SleV2QoS4PolicerRemarkMode_Type(Bits):
    """Custom type sleV2QoS4PolicerRemarkMode based on Bits"""
    namedValues = NamedValues(
        *(("remarkQueue", 0),
          ("remarkExtCoS", 1))
    )

_SleV2QoS4PolicerRemarkMode_Type.__name__ = "Bits"
_SleV2QoS4PolicerRemarkMode_Object = MibTableColumn
sleV2QoS4PolicerRemarkMode = _SleV2QoS4PolicerRemarkMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 17),
    _SleV2QoS4PolicerRemarkMode_Type()
)
sleV2QoS4PolicerRemarkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerRemarkMode.setStatus("current")
_SleV2QoS4PolicerCounterMode_Type = IntCounterMode
_SleV2QoS4PolicerCounterMode_Object = MibTableColumn
sleV2QoS4PolicerCounterMode = _SleV2QoS4PolicerCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 18),
    _SleV2QoS4PolicerCounterMode_Type()
)
sleV2QoS4PolicerCounterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerCounterMode.setStatus("current")
_SleV2QoS4PolicerAvrgCounterMode_Type = IntAvrgCounterMode
_SleV2QoS4PolicerAvrgCounterMode_Object = MibTableColumn
sleV2QoS4PolicerAvrgCounterMode = _SleV2QoS4PolicerAvrgCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 19),
    _SleV2QoS4PolicerAvrgCounterMode_Type()
)
sleV2QoS4PolicerAvrgCounterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerAvrgCounterMode.setStatus("current")
_SleV2QoS4PolicerMinBandwidth_Type = Integer32
_SleV2QoS4PolicerMinBandwidth_Object = MibTableColumn
sleV2QoS4PolicerMinBandwidth = _SleV2QoS4PolicerMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 20),
    _SleV2QoS4PolicerMinBandwidth_Type()
)
sleV2QoS4PolicerMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMinBandwidth.setStatus("current")
_SleV2QoS4PolicerMaxBandwidth_Type = Integer32
_SleV2QoS4PolicerMaxBandwidth_Object = MibTableColumn
sleV2QoS4PolicerMaxBandwidth = _SleV2QoS4PolicerMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 21),
    _SleV2QoS4PolicerMaxBandwidth_Type()
)
sleV2QoS4PolicerMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMaxBandwidth.setStatus("current")


class _SleV2QoS4PolicerColorRedDscp_Type(IntDscp):
    """Custom type sleV2QoS4PolicerColorRedDscp based on IntDscp"""
    defaultValue = 30


_SleV2QoS4PolicerColorRedDscp_Type.__name__ = "IntDscp"
_SleV2QoS4PolicerColorRedDscp_Object = MibTableColumn
sleV2QoS4PolicerColorRedDscp = _SleV2QoS4PolicerColorRedDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 22),
    _SleV2QoS4PolicerColorRedDscp_Type()
)
sleV2QoS4PolicerColorRedDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorRedDscp.setStatus("current")


class _SleV2QoS4PolicerColorYellowDscp_Type(IntDscp):
    """Custom type sleV2QoS4PolicerColorYellowDscp based on IntDscp"""
    defaultValue = 28


_SleV2QoS4PolicerColorYellowDscp_Type.__name__ = "IntDscp"
_SleV2QoS4PolicerColorYellowDscp_Object = MibTableColumn
sleV2QoS4PolicerColorYellowDscp = _SleV2QoS4PolicerColorYellowDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 23),
    _SleV2QoS4PolicerColorYellowDscp_Type()
)
sleV2QoS4PolicerColorYellowDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorYellowDscp.setStatus("current")


class _SleV2QoS4PolicerColorGreenDscp_Type(IntDscp):
    """Custom type sleV2QoS4PolicerColorGreenDscp based on IntDscp"""
    defaultValue = 26


_SleV2QoS4PolicerColorGreenDscp_Type.__name__ = "IntDscp"
_SleV2QoS4PolicerColorGreenDscp_Object = MibTableColumn
sleV2QoS4PolicerColorGreenDscp = _SleV2QoS4PolicerColorGreenDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 24),
    _SleV2QoS4PolicerColorGreenDscp_Type()
)
sleV2QoS4PolicerColorGreenDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorGreenDscp.setStatus("current")


class _SleV2QoS4PolicerColorRedCosType_Type(Integer32):
    """Custom type sleV2QoS4PolicerColorRedCosType based on Integer32"""
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
          ("mark", 1),
          ("overwrite", 2))
    )


_SleV2QoS4PolicerColorRedCosType_Type.__name__ = "Integer32"
_SleV2QoS4PolicerColorRedCosType_Object = MibTableColumn
sleV2QoS4PolicerColorRedCosType = _SleV2QoS4PolicerColorRedCosType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 25),
    _SleV2QoS4PolicerColorRedCosType_Type()
)
sleV2QoS4PolicerColorRedCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorRedCosType.setStatus("current")
_SleV2QoS4PolicerColorRedCos_Type = IntCoS
_SleV2QoS4PolicerColorRedCos_Object = MibTableColumn
sleV2QoS4PolicerColorRedCos = _SleV2QoS4PolicerColorRedCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 26),
    _SleV2QoS4PolicerColorRedCos_Type()
)
sleV2QoS4PolicerColorRedCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorRedCos.setStatus("current")


class _SleV2QoS4PolicerColorYellowCosType_Type(Integer32):
    """Custom type sleV2QoS4PolicerColorYellowCosType based on Integer32"""
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
          ("mark", 1),
          ("overwrite", 2))
    )


_SleV2QoS4PolicerColorYellowCosType_Type.__name__ = "Integer32"
_SleV2QoS4PolicerColorYellowCosType_Object = MibTableColumn
sleV2QoS4PolicerColorYellowCosType = _SleV2QoS4PolicerColorYellowCosType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 27),
    _SleV2QoS4PolicerColorYellowCosType_Type()
)
sleV2QoS4PolicerColorYellowCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorYellowCosType.setStatus("current")
_SleV2QoS4PolicerColorYellowCos_Type = IntToS
_SleV2QoS4PolicerColorYellowCos_Object = MibTableColumn
sleV2QoS4PolicerColorYellowCos = _SleV2QoS4PolicerColorYellowCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 28),
    _SleV2QoS4PolicerColorYellowCos_Type()
)
sleV2QoS4PolicerColorYellowCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorYellowCos.setStatus("current")


class _SleV2QoS4PolicerColorGreenCosType_Type(Integer32):
    """Custom type sleV2QoS4PolicerColorGreenCosType based on Integer32"""
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
          ("mark", 1),
          ("overwrite", 2))
    )


_SleV2QoS4PolicerColorGreenCosType_Type.__name__ = "Integer32"
_SleV2QoS4PolicerColorGreenCosType_Object = MibTableColumn
sleV2QoS4PolicerColorGreenCosType = _SleV2QoS4PolicerColorGreenCosType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 29),
    _SleV2QoS4PolicerColorGreenCosType_Type()
)
sleV2QoS4PolicerColorGreenCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorGreenCosType.setStatus("current")
_SleV2QoS4PolicerColorGreenCos_Type = IntToS
_SleV2QoS4PolicerColorGreenCos_Object = MibTableColumn
sleV2QoS4PolicerColorGreenCos = _SleV2QoS4PolicerColorGreenCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 1, 1, 30),
    _SleV2QoS4PolicerColorGreenCos_Type()
)
sleV2QoS4PolicerColorGreenCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerColorGreenCos.setStatus("current")
_SleV2QoS4PolicerControl_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicerControl = _SleV2QoS4PolicerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2)
)


class _SleV2QoS4PolicerControlRequest_Type(Integer32):
    """Custom type sleV2QoS4PolicerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createPolicer", 1),
          ("modifyPolicer", 2),
          ("destroyPolicer", 3))
    )


_SleV2QoS4PolicerControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4PolicerControlRequest_Object = MibScalar
sleV2QoS4PolicerControlRequest = _SleV2QoS4PolicerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 1),
    _SleV2QoS4PolicerControlRequest_Type()
)
sleV2QoS4PolicerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlRequest.setStatus("current")
_SleV2QoS4PolicerControlStatus_Type = SleControlStatusType
_SleV2QoS4PolicerControlStatus_Object = MibScalar
sleV2QoS4PolicerControlStatus = _SleV2QoS4PolicerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 2),
    _SleV2QoS4PolicerControlStatus_Type()
)
sleV2QoS4PolicerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlStatus.setStatus("current")
_SleV2QoS4PolicerControlTimer_Type = Gauge32
_SleV2QoS4PolicerControlTimer_Object = MibScalar
sleV2QoS4PolicerControlTimer = _SleV2QoS4PolicerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 3),
    _SleV2QoS4PolicerControlTimer_Type()
)
sleV2QoS4PolicerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlTimer.setStatus("current")
_SleV2QoS4PolicerControlTimeStamp_Type = TimeTicks
_SleV2QoS4PolicerControlTimeStamp_Object = MibScalar
sleV2QoS4PolicerControlTimeStamp = _SleV2QoS4PolicerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 4),
    _SleV2QoS4PolicerControlTimeStamp_Type()
)
sleV2QoS4PolicerControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlTimeStamp.setStatus("current")
_SleV2QoS4PolicerControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4PolicerControlReqResult_Object = MibScalar
sleV2QoS4PolicerControlReqResult = _SleV2QoS4PolicerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 5),
    _SleV2QoS4PolicerControlReqResult_Type()
)
sleV2QoS4PolicerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlReqResult.setStatus("current")
_SleV2QoS4PolicerControlIndex_Type = IntPolicerIndex
_SleV2QoS4PolicerControlIndex_Object = MibScalar
sleV2QoS4PolicerControlIndex = _SleV2QoS4PolicerControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 6),
    _SleV2QoS4PolicerControlIndex_Type()
)
sleV2QoS4PolicerControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlIndex.setStatus("current")
_SleV2QoS4PolicerControlName_Type = OctetName
_SleV2QoS4PolicerControlName_Object = MibScalar
sleV2QoS4PolicerControlName = _SleV2QoS4PolicerControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 7),
    _SleV2QoS4PolicerControlName_Type()
)
sleV2QoS4PolicerControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlName.setStatus("current")
_SleV2QoS4PolicerControlMeterMode_Type = IntMeterMode
_SleV2QoS4PolicerControlMeterMode_Object = MibScalar
sleV2QoS4PolicerControlMeterMode = _SleV2QoS4PolicerControlMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 8),
    _SleV2QoS4PolicerControlMeterMode_Type()
)
sleV2QoS4PolicerControlMeterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlMeterMode.setStatus("current")
_SleV2QoS4PolicerControlRateLimit_Type = Integer32
_SleV2QoS4PolicerControlRateLimit_Object = MibScalar
sleV2QoS4PolicerControlRateLimit = _SleV2QoS4PolicerControlRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 9),
    _SleV2QoS4PolicerControlRateLimit_Type()
)
sleV2QoS4PolicerControlRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlRateLimit.setStatus("current")
_SleV2QoS4PolicerControlColorType_Type = IntColorType
_SleV2QoS4PolicerControlColorType_Object = MibScalar
sleV2QoS4PolicerControlColorType = _SleV2QoS4PolicerControlColorType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 10),
    _SleV2QoS4PolicerControlColorType_Type()
)
sleV2QoS4PolicerControlColorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorType.setStatus("current")
_SleV2QoS4PolicerControlColorMode_Type = IntColorMode
_SleV2QoS4PolicerControlColorMode_Object = MibScalar
sleV2QoS4PolicerControlColorMode = _SleV2QoS4PolicerControlColorMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 11),
    _SleV2QoS4PolicerControlColorMode_Type()
)
sleV2QoS4PolicerControlColorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorMode.setStatus("current")
_SleV2QoS4PolicerControlColorAwareMode_Type = IntColorAwareMode
_SleV2QoS4PolicerControlColorAwareMode_Object = MibScalar
sleV2QoS4PolicerControlColorAwareMode = _SleV2QoS4PolicerControlColorAwareMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 12),
    _SleV2QoS4PolicerControlColorAwareMode_Type()
)
sleV2QoS4PolicerControlColorAwareMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorAwareMode.setStatus("current")
_SleV2QoS4PolicerControlColorCIR_Type = IntColorCIR
_SleV2QoS4PolicerControlColorCIR_Object = MibScalar
sleV2QoS4PolicerControlColorCIR = _SleV2QoS4PolicerControlColorCIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 13),
    _SleV2QoS4PolicerControlColorCIR_Type()
)
sleV2QoS4PolicerControlColorCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorCIR.setStatus("current")
_SleV2QoS4PolicerControlColorCBS_Type = IntColorCBS
_SleV2QoS4PolicerControlColorCBS_Object = MibScalar
sleV2QoS4PolicerControlColorCBS = _SleV2QoS4PolicerControlColorCBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 14),
    _SleV2QoS4PolicerControlColorCBS_Type()
)
sleV2QoS4PolicerControlColorCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorCBS.setStatus("current")
_SleV2QoS4PolicerControlColorPIR_Type = IntColorPIR
_SleV2QoS4PolicerControlColorPIR_Object = MibScalar
sleV2QoS4PolicerControlColorPIR = _SleV2QoS4PolicerControlColorPIR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 15),
    _SleV2QoS4PolicerControlColorPIR_Type()
)
sleV2QoS4PolicerControlColorPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorPIR.setStatus("current")
_SleV2QoS4PolicerControlColorPBS_Type = IntColorPBS
_SleV2QoS4PolicerControlColorPBS_Object = MibScalar
sleV2QoS4PolicerControlColorPBS = _SleV2QoS4PolicerControlColorPBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 16),
    _SleV2QoS4PolicerControlColorPBS_Type()
)
sleV2QoS4PolicerControlColorPBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorPBS.setStatus("current")
_SleV2QoS4PolicerControlColorEBS_Type = IntColorEBS
_SleV2QoS4PolicerControlColorEBS_Object = MibScalar
sleV2QoS4PolicerControlColorEBS = _SleV2QoS4PolicerControlColorEBS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 17),
    _SleV2QoS4PolicerControlColorEBS_Type()
)
sleV2QoS4PolicerControlColorEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorEBS.setStatus("current")
_SleV2QoS4PolicerControlColorRedAction_Type = IntColorAction
_SleV2QoS4PolicerControlColorRedAction_Object = MibScalar
sleV2QoS4PolicerControlColorRedAction = _SleV2QoS4PolicerControlColorRedAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 18),
    _SleV2QoS4PolicerControlColorRedAction_Type()
)
sleV2QoS4PolicerControlColorRedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorRedAction.setStatus("current")
_SleV2QoS4PolicerControlColorYellowAction_Type = IntColorAction
_SleV2QoS4PolicerControlColorYellowAction_Object = MibScalar
sleV2QoS4PolicerControlColorYellowAction = _SleV2QoS4PolicerControlColorYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 19),
    _SleV2QoS4PolicerControlColorYellowAction_Type()
)
sleV2QoS4PolicerControlColorYellowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorYellowAction.setStatus("current")
_SleV2QoS4PolicerControlColorGreenAction_Type = IntColorAction
_SleV2QoS4PolicerControlColorGreenAction_Object = MibScalar
sleV2QoS4PolicerControlColorGreenAction = _SleV2QoS4PolicerControlColorGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 20),
    _SleV2QoS4PolicerControlColorGreenAction_Type()
)
sleV2QoS4PolicerControlColorGreenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorGreenAction.setStatus("current")


class _SleV2QoS4PolicerControlRemarkLayerMode_Type(Bits):
    """Custom type sleV2QoS4PolicerControlRemarkLayerMode based on Bits"""
    namedValues = NamedValues(
        *(("remarkByDSCP", 0),
          ("remarkByQueueOrCoS", 1))
    )

_SleV2QoS4PolicerControlRemarkLayerMode_Type.__name__ = "Bits"
_SleV2QoS4PolicerControlRemarkLayerMode_Object = MibScalar
sleV2QoS4PolicerControlRemarkLayerMode = _SleV2QoS4PolicerControlRemarkLayerMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 21),
    _SleV2QoS4PolicerControlRemarkLayerMode_Type()
)
sleV2QoS4PolicerControlRemarkLayerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlRemarkLayerMode.setStatus("current")


class _SleV2QoS4PolicerControlRemarkMode_Type(Bits):
    """Custom type sleV2QoS4PolicerControlRemarkMode based on Bits"""
    namedValues = NamedValues(
        *(("remarkQueue", 0),
          ("remarkExtCoS", 1))
    )

_SleV2QoS4PolicerControlRemarkMode_Type.__name__ = "Bits"
_SleV2QoS4PolicerControlRemarkMode_Object = MibScalar
sleV2QoS4PolicerControlRemarkMode = _SleV2QoS4PolicerControlRemarkMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 22),
    _SleV2QoS4PolicerControlRemarkMode_Type()
)
sleV2QoS4PolicerControlRemarkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlRemarkMode.setStatus("current")
_SleV2QoS4PolicerControlCounterMode_Type = IntCounterMode
_SleV2QoS4PolicerControlCounterMode_Object = MibScalar
sleV2QoS4PolicerControlCounterMode = _SleV2QoS4PolicerControlCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 23),
    _SleV2QoS4PolicerControlCounterMode_Type()
)
sleV2QoS4PolicerControlCounterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlCounterMode.setStatus("current")
_SleV2QoS4PolicerControlAvrgCounterMode_Type = IntAvrgCounterMode
_SleV2QoS4PolicerControlAvrgCounterMode_Object = MibScalar
sleV2QoS4PolicerControlAvrgCounterMode = _SleV2QoS4PolicerControlAvrgCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 24),
    _SleV2QoS4PolicerControlAvrgCounterMode_Type()
)
sleV2QoS4PolicerControlAvrgCounterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlAvrgCounterMode.setStatus("current")
_SleV2QoS4PolicerControlMinBandwidth_Type = Integer32
_SleV2QoS4PolicerControlMinBandwidth_Object = MibScalar
sleV2QoS4PolicerControlMinBandwidth = _SleV2QoS4PolicerControlMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 25),
    _SleV2QoS4PolicerControlMinBandwidth_Type()
)
sleV2QoS4PolicerControlMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlMinBandwidth.setStatus("current")
_SleV2QoS4PolicerControlMaxBandwidth_Type = Integer32
_SleV2QoS4PolicerControlMaxBandwidth_Object = MibScalar
sleV2QoS4PolicerControlMaxBandwidth = _SleV2QoS4PolicerControlMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 26),
    _SleV2QoS4PolicerControlMaxBandwidth_Type()
)
sleV2QoS4PolicerControlMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlMaxBandwidth.setStatus("current")
_SleV2QoS4PolicerControlColorRedDscp_Type = IntDscp
_SleV2QoS4PolicerControlColorRedDscp_Object = MibScalar
sleV2QoS4PolicerControlColorRedDscp = _SleV2QoS4PolicerControlColorRedDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 27),
    _SleV2QoS4PolicerControlColorRedDscp_Type()
)
sleV2QoS4PolicerControlColorRedDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorRedDscp.setStatus("current")
_SleV2QoS4PolicerControlColorYellowDscp_Type = IntDscp
_SleV2QoS4PolicerControlColorYellowDscp_Object = MibScalar
sleV2QoS4PolicerControlColorYellowDscp = _SleV2QoS4PolicerControlColorYellowDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 28),
    _SleV2QoS4PolicerControlColorYellowDscp_Type()
)
sleV2QoS4PolicerControlColorYellowDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorYellowDscp.setStatus("current")
_SleV2QoS4PolicerControlColorGreenDscp_Type = IntDscp
_SleV2QoS4PolicerControlColorGreenDscp_Object = MibScalar
sleV2QoS4PolicerControlColorGreenDscp = _SleV2QoS4PolicerControlColorGreenDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 29),
    _SleV2QoS4PolicerControlColorGreenDscp_Type()
)
sleV2QoS4PolicerControlColorGreenDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorGreenDscp.setStatus("current")


class _SleV2QoS4PolicerControlColorRedCosType_Type(Integer32):
    """Custom type sleV2QoS4PolicerControlColorRedCosType based on Integer32"""
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
          ("mark", 1),
          ("overwrite", 2))
    )


_SleV2QoS4PolicerControlColorRedCosType_Type.__name__ = "Integer32"
_SleV2QoS4PolicerControlColorRedCosType_Object = MibScalar
sleV2QoS4PolicerControlColorRedCosType = _SleV2QoS4PolicerControlColorRedCosType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 30),
    _SleV2QoS4PolicerControlColorRedCosType_Type()
)
sleV2QoS4PolicerControlColorRedCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorRedCosType.setStatus("current")
_SleV2QoS4PolicerControlColorRedCos_Type = IntCoS
_SleV2QoS4PolicerControlColorRedCos_Object = MibScalar
sleV2QoS4PolicerControlColorRedCos = _SleV2QoS4PolicerControlColorRedCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 31),
    _SleV2QoS4PolicerControlColorRedCos_Type()
)
sleV2QoS4PolicerControlColorRedCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorRedCos.setStatus("current")


class _SleV2QoS4PolicerControlColorYellowCosType_Type(Integer32):
    """Custom type sleV2QoS4PolicerControlColorYellowCosType based on Integer32"""
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
          ("mark", 1),
          ("overwrite", 2))
    )


_SleV2QoS4PolicerControlColorYellowCosType_Type.__name__ = "Integer32"
_SleV2QoS4PolicerControlColorYellowCosType_Object = MibScalar
sleV2QoS4PolicerControlColorYellowCosType = _SleV2QoS4PolicerControlColorYellowCosType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 32),
    _SleV2QoS4PolicerControlColorYellowCosType_Type()
)
sleV2QoS4PolicerControlColorYellowCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorYellowCosType.setStatus("current")
_SleV2QoS4PolicerControlColorYellowCos_Type = IntToS
_SleV2QoS4PolicerControlColorYellowCos_Object = MibScalar
sleV2QoS4PolicerControlColorYellowCos = _SleV2QoS4PolicerControlColorYellowCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 33),
    _SleV2QoS4PolicerControlColorYellowCos_Type()
)
sleV2QoS4PolicerControlColorYellowCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorYellowCos.setStatus("current")


class _SleV2QoS4PolicerControlColorGreenCosType_Type(Integer32):
    """Custom type sleV2QoS4PolicerControlColorGreenCosType based on Integer32"""
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
          ("mark", 1),
          ("overwrite", 2))
    )


_SleV2QoS4PolicerControlColorGreenCosType_Type.__name__ = "Integer32"
_SleV2QoS4PolicerControlColorGreenCosType_Object = MibScalar
sleV2QoS4PolicerControlColorGreenCosType = _SleV2QoS4PolicerControlColorGreenCosType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 34),
    _SleV2QoS4PolicerControlColorGreenCosType_Type()
)
sleV2QoS4PolicerControlColorGreenCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorGreenCosType.setStatus("current")
_SleV2QoS4PolicerControlColorGreenCos_Type = IntToS
_SleV2QoS4PolicerControlColorGreenCos_Object = MibScalar
sleV2QoS4PolicerControlColorGreenCos = _SleV2QoS4PolicerControlColorGreenCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 2, 35),
    _SleV2QoS4PolicerControlColorGreenCos_Type()
)
sleV2QoS4PolicerControlColorGreenCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerControlColorGreenCos.setStatus("current")
_SleV2QoS4PolicerNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicerNotification = _SleV2QoS4PolicerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 3)
)
_SleV2QoS4PolicerMatchCounter_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicerMatchCounter = _SleV2QoS4PolicerMatchCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 2)
)
_SleV2QoS4PolicerMatchCounterTable_Object = MibTable
sleV2QoS4PolicerMatchCounterTable = _SleV2QoS4PolicerMatchCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMatchCounterTable.setStatus("current")
_SleV2QoS4PolicerMatchCounterEntry_Object = MibTableRow
sleV2QoS4PolicerMatchCounterEntry = _SleV2QoS4PolicerMatchCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 2, 1, 1)
)
sleV2QoS4PolicerMatchCounterEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PolicerMatchCounterName"),
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMatchCounterEntry.setStatus("current")


class _SleV2QoS4PolicerMatchCounterName_Type(OctetString):
    """Custom type sleV2QoS4PolicerMatchCounterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_SleV2QoS4PolicerMatchCounterName_Type.__name__ = "OctetString"
_SleV2QoS4PolicerMatchCounterName_Object = MibTableColumn
sleV2QoS4PolicerMatchCounterName = _SleV2QoS4PolicerMatchCounterName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 2, 1, 1, 1),
    _SleV2QoS4PolicerMatchCounterName_Type()
)
sleV2QoS4PolicerMatchCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMatchCounterName.setStatus("current")


class _SleV2QoS4PolicerMatchCounterDesc_Type(OctetString):
    """Custom type sleV2QoS4PolicerMatchCounterDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_SleV2QoS4PolicerMatchCounterDesc_Type.__name__ = "OctetString"
_SleV2QoS4PolicerMatchCounterDesc_Object = MibTableColumn
sleV2QoS4PolicerMatchCounterDesc = _SleV2QoS4PolicerMatchCounterDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 2, 1, 1, 2),
    _SleV2QoS4PolicerMatchCounterDesc_Type()
)
sleV2QoS4PolicerMatchCounterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMatchCounterDesc.setStatus("current")
_SleV2QoS4PolicerMatchCounterValue_Type = Counter64
_SleV2QoS4PolicerMatchCounterValue_Object = MibTableColumn
sleV2QoS4PolicerMatchCounterValue = _SleV2QoS4PolicerMatchCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 2, 1, 1, 3),
    _SleV2QoS4PolicerMatchCounterValue_Type()
)
sleV2QoS4PolicerMatchCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicerMatchCounterValue.setStatus("current")
_SleV2QoS4Policy_ObjectIdentity = ObjectIdentity
sleV2QoS4Policy = _SleV2QoS4Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5)
)
_SleV2QoS4PolicyInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyInfo = _SleV2QoS4PolicyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1)
)
_SleV2QoS4PolicyTable_Object = MibTable
sleV2QoS4PolicyTable = _SleV2QoS4PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicyTable.setStatus("current")
_SleV2QoS4PolicyEntry_Object = MibTableRow
sleV2QoS4PolicyEntry = _SleV2QoS4PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1)
)
sleV2QoS4PolicyEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PolicyIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicyEntry.setStatus("current")
_SleV2QoS4PolicyIndex_Type = IntPolicyIndex
_SleV2QoS4PolicyIndex_Object = MibTableColumn
sleV2QoS4PolicyIndex = _SleV2QoS4PolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 1),
    _SleV2QoS4PolicyIndex_Type()
)
sleV2QoS4PolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIndex.setStatus("current")
_SleV2QoS4PolicyName_Type = OctetName
_SleV2QoS4PolicyName_Object = MibTableColumn
sleV2QoS4PolicyName = _SleV2QoS4PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 2),
    _SleV2QoS4PolicyName_Type()
)
sleV2QoS4PolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyName.setStatus("current")
_SleV2QoS4PolicyFlowCnt_Type = Integer32
_SleV2QoS4PolicyFlowCnt_Object = MibTableColumn
sleV2QoS4PolicyFlowCnt = _SleV2QoS4PolicyFlowCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 3),
    _SleV2QoS4PolicyFlowCnt_Type()
)
sleV2QoS4PolicyFlowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowCnt.setStatus("current")
_SleV2QoS4PolicyClassCnt_Type = Integer32
_SleV2QoS4PolicyClassCnt_Object = MibTableColumn
sleV2QoS4PolicyClassCnt = _SleV2QoS4PolicyClassCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 4),
    _SleV2QoS4PolicyClassCnt_Type()
)
sleV2QoS4PolicyClassCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyClassCnt.setStatus("current")


class _SleV2QoS4PolicyPolicerIndex_Type(Integer32):
    """Custom type sleV2QoS4PolicyPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1024),
    )


_SleV2QoS4PolicyPolicerIndex_Type.__name__ = "Integer32"
_SleV2QoS4PolicyPolicerIndex_Object = MibTableColumn
sleV2QoS4PolicyPolicerIndex = _SleV2QoS4PolicyPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 5),
    _SleV2QoS4PolicyPolicerIndex_Type()
)
sleV2QoS4PolicyPolicerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyPolicerIndex.setStatus("current")
_SleV2QoS4PolicyPriority_Type = IntRulePriority
_SleV2QoS4PolicyPriority_Object = MibTableColumn
sleV2QoS4PolicyPriority = _SleV2QoS4PolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 6),
    _SleV2QoS4PolicyPriority_Type()
)
sleV2QoS4PolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyPriority.setStatus("current")
_SleV2QoS4PolicyIngressPorts_Type = OctetString
_SleV2QoS4PolicyIngressPorts_Object = MibTableColumn
sleV2QoS4PolicyIngressPorts = _SleV2QoS4PolicyIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 7),
    _SleV2QoS4PolicyIngressPorts_Type()
)
sleV2QoS4PolicyIngressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIngressPorts.setStatus("current")
_SleV2QoS4PolicyEgressPorts_Type = OctetString
_SleV2QoS4PolicyEgressPorts_Object = MibTableColumn
sleV2QoS4PolicyEgressPorts = _SleV2QoS4PolicyEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 8),
    _SleV2QoS4PolicyEgressPorts_Type()
)
sleV2QoS4PolicyEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyEgressPorts.setStatus("current")
_SleV2QoS4PolicyVlan_Type = IntVlanID
_SleV2QoS4PolicyVlan_Object = MibTableColumn
sleV2QoS4PolicyVlan = _SleV2QoS4PolicyVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 9),
    _SleV2QoS4PolicyVlan_Type()
)
sleV2QoS4PolicyVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyVlan.setStatus("current")


class _SleV2QoS4PolicyMatchFlag_Type(Bits):
    """Custom type sleV2QoS4PolicyMatchFlag based on Bits"""
    namedValues = NamedValues(
        *(("deny", 0),
          ("mirror", 1),
          ("copyToCPU", 2),
          ("sameAsTos", 3),
          ("sameAsCos", 4),
          ("cos", 5),
          ("tos", 6),
          ("permit", 7))
    )

_SleV2QoS4PolicyMatchFlag_Type.__name__ = "Bits"
_SleV2QoS4PolicyMatchFlag_Object = MibTableColumn
sleV2QoS4PolicyMatchFlag = _SleV2QoS4PolicyMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 10),
    _SleV2QoS4PolicyMatchFlag_Type()
)
sleV2QoS4PolicyMatchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchFlag.setStatus("current")
_SleV2QoS4PolicyMatchVlan_Type = IntVlanID
_SleV2QoS4PolicyMatchVlan_Object = MibTableColumn
sleV2QoS4PolicyMatchVlan = _SleV2QoS4PolicyMatchVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 11),
    _SleV2QoS4PolicyMatchVlan_Type()
)
sleV2QoS4PolicyMatchVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchVlan.setStatus("current")
_SleV2QoS4PolicyMatchRedirectVlan_Type = IntVlanID
_SleV2QoS4PolicyMatchRedirectVlan_Object = MibTableColumn
sleV2QoS4PolicyMatchRedirectVlan = _SleV2QoS4PolicyMatchRedirectVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 12),
    _SleV2QoS4PolicyMatchRedirectVlan_Type()
)
sleV2QoS4PolicyMatchRedirectVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchRedirectVlan.setStatus("current")
_SleV2QoS4PolicyMatchRedirectPort_Type = IntInterfaceIndex
_SleV2QoS4PolicyMatchRedirectPort_Object = MibTableColumn
sleV2QoS4PolicyMatchRedirectPort = _SleV2QoS4PolicyMatchRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 13),
    _SleV2QoS4PolicyMatchRedirectPort_Type()
)
sleV2QoS4PolicyMatchRedirectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchRedirectPort.setStatus("current")
_SleV2QoS4PolicyMatchMarkMode_Type = IntMarkMode
_SleV2QoS4PolicyMatchMarkMode_Object = MibTableColumn
sleV2QoS4PolicyMatchMarkMode = _SleV2QoS4PolicyMatchMarkMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 14),
    _SleV2QoS4PolicyMatchMarkMode_Type()
)
sleV2QoS4PolicyMatchMarkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchMarkMode.setStatus("current")
_SleV2QoS4PolicyMatchQueue_Type = IntQueue
_SleV2QoS4PolicyMatchQueue_Object = MibTableColumn
sleV2QoS4PolicyMatchQueue = _SleV2QoS4PolicyMatchQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 15),
    _SleV2QoS4PolicyMatchQueue_Type()
)
sleV2QoS4PolicyMatchQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchQueue.setStatus("current")
_SleV2QoS4PolicyMatchDp_Type = IntDP
_SleV2QoS4PolicyMatchDp_Object = MibTableColumn
sleV2QoS4PolicyMatchDp = _SleV2QoS4PolicyMatchDp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 16),
    _SleV2QoS4PolicyMatchDp_Type()
)
sleV2QoS4PolicyMatchDp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchDp.setStatus("current")
_SleV2QoS4PolicyMatchCoS_Type = IntCoS
_SleV2QoS4PolicyMatchCoS_Object = MibTableColumn
sleV2QoS4PolicyMatchCoS = _SleV2QoS4PolicyMatchCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 17),
    _SleV2QoS4PolicyMatchCoS_Type()
)
sleV2QoS4PolicyMatchCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchCoS.setStatus("current")
_SleV2QoS4PolicyMatchDscp_Type = IntDscp
_SleV2QoS4PolicyMatchDscp_Object = MibTableColumn
sleV2QoS4PolicyMatchDscp = _SleV2QoS4PolicyMatchDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 18),
    _SleV2QoS4PolicyMatchDscp_Type()
)
sleV2QoS4PolicyMatchDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchDscp.setStatus("current")
_SleV2QoS4PolicyMatchIpPrecedence_Type = IntIpPrecedence
_SleV2QoS4PolicyMatchIpPrecedence_Object = MibTableColumn
sleV2QoS4PolicyMatchIpPrecedence = _SleV2QoS4PolicyMatchIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 19),
    _SleV2QoS4PolicyMatchIpPrecedence_Type()
)
sleV2QoS4PolicyMatchIpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchIpPrecedence.setStatus("current")
_SleV2QoS4PolicyMatchDstMacOrEgressPorts_Type = IntDstMacOrEgressPorts
_SleV2QoS4PolicyMatchDstMacOrEgressPorts_Object = MibTableColumn
sleV2QoS4PolicyMatchDstMacOrEgressPorts = _SleV2QoS4PolicyMatchDstMacOrEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 20),
    _SleV2QoS4PolicyMatchDstMacOrEgressPorts_Type()
)
sleV2QoS4PolicyMatchDstMacOrEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchDstMacOrEgressPorts.setStatus("current")
_SleV2QoS4PolicyMatchDstMac_Type = MacAddress
_SleV2QoS4PolicyMatchDstMac_Object = MibTableColumn
sleV2QoS4PolicyMatchDstMac = _SleV2QoS4PolicyMatchDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 21),
    _SleV2QoS4PolicyMatchDstMac_Type()
)
sleV2QoS4PolicyMatchDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchDstMac.setStatus("current")
_SleV2QoS4PolicyMatchEgressPorts_Type = OctetString
_SleV2QoS4PolicyMatchEgressPorts_Object = MibTableColumn
sleV2QoS4PolicyMatchEgressPorts = _SleV2QoS4PolicyMatchEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 22),
    _SleV2QoS4PolicyMatchEgressPorts_Type()
)
sleV2QoS4PolicyMatchEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchEgressPorts.setStatus("current")


class _SleV2QoS4PolicyNomatchFlag_Type(Bits):
    """Custom type sleV2QoS4PolicyNomatchFlag based on Bits"""
    namedValues = NamedValues(
        *(("deny", 0),
          ("mirror", 1),
          ("copyToCPU", 2),
          ("sameAsTos", 3),
          ("sameAsCos", 4),
          ("cos", 5),
          ("tos", 6),
          ("permit", 7))
    )

_SleV2QoS4PolicyNomatchFlag_Type.__name__ = "Bits"
_SleV2QoS4PolicyNomatchFlag_Object = MibTableColumn
sleV2QoS4PolicyNomatchFlag = _SleV2QoS4PolicyNomatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 23),
    _SleV2QoS4PolicyNomatchFlag_Type()
)
sleV2QoS4PolicyNomatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyNomatchFlag.setStatus("current")
_SleV2QoS4PolicyNomatchRedirectPort_Type = IntInterfaceIndex
_SleV2QoS4PolicyNomatchRedirectPort_Object = MibTableColumn
sleV2QoS4PolicyNomatchRedirectPort = _SleV2QoS4PolicyNomatchRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 24),
    _SleV2QoS4PolicyNomatchRedirectPort_Type()
)
sleV2QoS4PolicyNomatchRedirectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyNomatchRedirectPort.setStatus("current")
_SleV2QoS4PolicyNomatchCoS_Type = IntCoS
_SleV2QoS4PolicyNomatchCoS_Object = MibTableColumn
sleV2QoS4PolicyNomatchCoS = _SleV2QoS4PolicyNomatchCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 25),
    _SleV2QoS4PolicyNomatchCoS_Type()
)
sleV2QoS4PolicyNomatchCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyNomatchCoS.setStatus("current")
_SleV2QoS4PolicyNomatchDscp_Type = IntDscp
_SleV2QoS4PolicyNomatchDscp_Object = MibTableColumn
sleV2QoS4PolicyNomatchDscp = _SleV2QoS4PolicyNomatchDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 26),
    _SleV2QoS4PolicyNomatchDscp_Type()
)
sleV2QoS4PolicyNomatchDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyNomatchDscp.setStatus("current")
_SleV2QoS4PolicyNomatchIpPrecedence_Type = IntIpPrecedence
_SleV2QoS4PolicyNomatchIpPrecedence_Object = MibTableColumn
sleV2QoS4PolicyNomatchIpPrecedence = _SleV2QoS4PolicyNomatchIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 27),
    _SleV2QoS4PolicyNomatchIpPrecedence_Type()
)
sleV2QoS4PolicyNomatchIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyNomatchIpPrecedence.setStatus("current")
_SleV2QoS4PolicyCounterValue_Type = Counter64
_SleV2QoS4PolicyCounterValue_Object = MibTableColumn
sleV2QoS4PolicyCounterValue = _SleV2QoS4PolicyCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 28),
    _SleV2QoS4PolicyCounterValue_Type()
)
sleV2QoS4PolicyCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyCounterValue.setStatus("current")
_SleV2QoS4PolicyCounterGreenBytes_Type = Counter64
_SleV2QoS4PolicyCounterGreenBytes_Object = MibTableColumn
sleV2QoS4PolicyCounterGreenBytes = _SleV2QoS4PolicyCounterGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 29),
    _SleV2QoS4PolicyCounterGreenBytes_Type()
)
sleV2QoS4PolicyCounterGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyCounterGreenBytes.setStatus("current")
_SleV2QoS4PolicyCounterYellowBytes_Type = Counter64
_SleV2QoS4PolicyCounterYellowBytes_Object = MibTableColumn
sleV2QoS4PolicyCounterYellowBytes = _SleV2QoS4PolicyCounterYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 30),
    _SleV2QoS4PolicyCounterYellowBytes_Type()
)
sleV2QoS4PolicyCounterYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyCounterYellowBytes.setStatus("current")
_SleV2QoS4PolicyCounterRedBytes_Type = Counter64
_SleV2QoS4PolicyCounterRedBytes_Object = MibTableColumn
sleV2QoS4PolicyCounterRedBytes = _SleV2QoS4PolicyCounterRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 31),
    _SleV2QoS4PolicyCounterRedBytes_Type()
)
sleV2QoS4PolicyCounterRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyCounterRedBytes.setStatus("current")
_SleV2QoS4PolicyRedirBlackhole_Type = IntEnableFlag
_SleV2QoS4PolicyRedirBlackhole_Object = MibTableColumn
sleV2QoS4PolicyRedirBlackhole = _SleV2QoS4PolicyRedirBlackhole_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 32),
    _SleV2QoS4PolicyRedirBlackhole_Type()
)
sleV2QoS4PolicyRedirBlackhole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyRedirBlackhole.setStatus("current")
_SleV2QoS4PolicyAvrg5SecCounterValue_Type = Counter64
_SleV2QoS4PolicyAvrg5SecCounterValue_Object = MibTableColumn
sleV2QoS4PolicyAvrg5SecCounterValue = _SleV2QoS4PolicyAvrg5SecCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 33),
    _SleV2QoS4PolicyAvrg5SecCounterValue_Type()
)
sleV2QoS4PolicyAvrg5SecCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyAvrg5SecCounterValue.setStatus("current")
_SleV2QoS4PolicyAvrg1minCounterValue_Type = Counter64
_SleV2QoS4PolicyAvrg1minCounterValue_Object = MibTableColumn
sleV2QoS4PolicyAvrg1minCounterValue = _SleV2QoS4PolicyAvrg1minCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 34),
    _SleV2QoS4PolicyAvrg1minCounterValue_Type()
)
sleV2QoS4PolicyAvrg1minCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyAvrg1minCounterValue.setStatus("current")
_SleV2QoS4PolicyAvrg10minCounterValue_Type = Counter64
_SleV2QoS4PolicyAvrg10minCounterValue_Object = MibTableColumn
sleV2QoS4PolicyAvrg10minCounterValue = _SleV2QoS4PolicyAvrg10minCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 35),
    _SleV2QoS4PolicyAvrg10minCounterValue_Type()
)
sleV2QoS4PolicyAvrg10minCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyAvrg10minCounterValue.setStatus("current")


class _SleV2QoS4PolicyIngressTunnelIfIndex_Type(Integer32):
    """Custom type sleV2QoS4PolicyIngressTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 11023),
    )


_SleV2QoS4PolicyIngressTunnelIfIndex_Type.__name__ = "Integer32"
_SleV2QoS4PolicyIngressTunnelIfIndex_Object = MibTableColumn
sleV2QoS4PolicyIngressTunnelIfIndex = _SleV2QoS4PolicyIngressTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 36),
    _SleV2QoS4PolicyIngressTunnelIfIndex_Type()
)
sleV2QoS4PolicyIngressTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIngressTunnelIfIndex.setStatus("current")


class _SleV2QoS4PolicyEgressTunnelIfIndex_Type(Integer32):
    """Custom type sleV2QoS4PolicyEgressTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 11023),
    )


_SleV2QoS4PolicyEgressTunnelIfIndex_Type.__name__ = "Integer32"
_SleV2QoS4PolicyEgressTunnelIfIndex_Object = MibTableColumn
sleV2QoS4PolicyEgressTunnelIfIndex = _SleV2QoS4PolicyEgressTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 37),
    _SleV2QoS4PolicyEgressTunnelIfIndex_Type()
)
sleV2QoS4PolicyEgressTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyEgressTunnelIfIndex.setStatus("current")
_SleV2QoS4PolicyCounterElapsedTimeAfterClear_Type = TimeTicks
_SleV2QoS4PolicyCounterElapsedTimeAfterClear_Object = MibTableColumn
sleV2QoS4PolicyCounterElapsedTimeAfterClear = _SleV2QoS4PolicyCounterElapsedTimeAfterClear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 38),
    _SleV2QoS4PolicyCounterElapsedTimeAfterClear_Type()
)
sleV2QoS4PolicyCounterElapsedTimeAfterClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyCounterElapsedTimeAfterClear.setStatus("current")
_SleV2QoS4PolicyMatchPbrNextHop_Type = IpAddress
_SleV2QoS4PolicyMatchPbrNextHop_Object = MibTableColumn
sleV2QoS4PolicyMatchPbrNextHop = _SleV2QoS4PolicyMatchPbrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 39),
    _SleV2QoS4PolicyMatchPbrNextHop_Type()
)
sleV2QoS4PolicyMatchPbrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchPbrNextHop.setStatus("current")


class _SleV2QoS4PolicyStage_Type(Integer32):
    """Custom type sleV2QoS4PolicyStage based on Integer32"""
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
        *(("ingress", 1),
          ("prio", 2),
          ("egress", 3),
          ("external", 4))
    )


_SleV2QoS4PolicyStage_Type.__name__ = "Integer32"
_SleV2QoS4PolicyStage_Object = MibTableColumn
sleV2QoS4PolicyStage = _SleV2QoS4PolicyStage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 40),
    _SleV2QoS4PolicyStage_Type()
)
sleV2QoS4PolicyStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyStage.setStatus("current")


class _SleV2QoS4PolicyIngressPortsFlag_Type(Integer32):
    """Custom type sleV2QoS4PolicyIngressPortsFlag based on Integer32"""
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
          ("any", 1),
          ("cpu", 2))
    )


_SleV2QoS4PolicyIngressPortsFlag_Type.__name__ = "Integer32"
_SleV2QoS4PolicyIngressPortsFlag_Object = MibTableColumn
sleV2QoS4PolicyIngressPortsFlag = _SleV2QoS4PolicyIngressPortsFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 41),
    _SleV2QoS4PolicyIngressPortsFlag_Type()
)
sleV2QoS4PolicyIngressPortsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIngressPortsFlag.setStatus("current")


class _SleV2QoS4PolicyEgressPortsFlag_Type(Integer32):
    """Custom type sleV2QoS4PolicyEgressPortsFlag based on Integer32"""
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
          ("any", 1),
          ("cpu", 2))
    )


_SleV2QoS4PolicyEgressPortsFlag_Type.__name__ = "Integer32"
_SleV2QoS4PolicyEgressPortsFlag_Object = MibTableColumn
sleV2QoS4PolicyEgressPortsFlag = _SleV2QoS4PolicyEgressPortsFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 42),
    _SleV2QoS4PolicyEgressPortsFlag_Type()
)
sleV2QoS4PolicyEgressPortsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyEgressPortsFlag.setStatus("current")


class _SleV2QoS4PolicyInnerVlanAction_Type(Integer32):
    """Custom type sleV2QoS4PolicyInnerVlanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("add", 1),
          ("replace", 2),
          ("del", 3))
    )


_SleV2QoS4PolicyInnerVlanAction_Type.__name__ = "Integer32"
_SleV2QoS4PolicyInnerVlanAction_Object = MibTableColumn
sleV2QoS4PolicyInnerVlanAction = _SleV2QoS4PolicyInnerVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 43),
    _SleV2QoS4PolicyInnerVlanAction_Type()
)
sleV2QoS4PolicyInnerVlanAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyInnerVlanAction.setStatus("current")


class _SleV2QoS4PolicyOuterVlanAction_Type(Integer32):
    """Custom type sleV2QoS4PolicyOuterVlanAction based on Integer32"""
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
          ("add", 1),
          ("replace", 2))
    )


_SleV2QoS4PolicyOuterVlanAction_Type.__name__ = "Integer32"
_SleV2QoS4PolicyOuterVlanAction_Object = MibTableColumn
sleV2QoS4PolicyOuterVlanAction = _SleV2QoS4PolicyOuterVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 44),
    _SleV2QoS4PolicyOuterVlanAction_Type()
)
sleV2QoS4PolicyOuterVlanAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyOuterVlanAction.setStatus("current")


class _SleV2QoS4PolicyInnerVlan_Type(Integer32):
    """Custom type sleV2QoS4PolicyInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_SleV2QoS4PolicyInnerVlan_Type.__name__ = "Integer32"
_SleV2QoS4PolicyInnerVlan_Object = MibTableColumn
sleV2QoS4PolicyInnerVlan = _SleV2QoS4PolicyInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 45),
    _SleV2QoS4PolicyInnerVlan_Type()
)
sleV2QoS4PolicyInnerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyInnerVlan.setStatus("current")


class _SleV2QoS4PolicyOuterVlan_Type(Integer32):
    """Custom type sleV2QoS4PolicyOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_SleV2QoS4PolicyOuterVlan_Type.__name__ = "Integer32"
_SleV2QoS4PolicyOuterVlan_Object = MibTableColumn
sleV2QoS4PolicyOuterVlan = _SleV2QoS4PolicyOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 46),
    _SleV2QoS4PolicyOuterVlan_Type()
)
sleV2QoS4PolicyOuterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyOuterVlan.setStatus("current")
_SleV2QoS4PolicyMatchPbrNextHopSecondary_Type = IpAddress
_SleV2QoS4PolicyMatchPbrNextHopSecondary_Object = MibTableColumn
sleV2QoS4PolicyMatchPbrNextHopSecondary = _SleV2QoS4PolicyMatchPbrNextHopSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 47),
    _SleV2QoS4PolicyMatchPbrNextHopSecondary_Type()
)
sleV2QoS4PolicyMatchPbrNextHopSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchPbrNextHopSecondary.setStatus("current")


class _SleV2QoS4PolicyMatchPbrNextHopVerifyReach_Type(Integer32):
    """Custom type sleV2QoS4PolicyMatchPbrNextHopVerifyReach based on Integer32"""
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


_SleV2QoS4PolicyMatchPbrNextHopVerifyReach_Type.__name__ = "Integer32"
_SleV2QoS4PolicyMatchPbrNextHopVerifyReach_Object = MibTableColumn
sleV2QoS4PolicyMatchPbrNextHopVerifyReach = _SleV2QoS4PolicyMatchPbrNextHopVerifyReach_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 48),
    _SleV2QoS4PolicyMatchPbrNextHopVerifyReach_Type()
)
sleV2QoS4PolicyMatchPbrNextHopVerifyReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchPbrNextHopVerifyReach.setStatus("current")
_SleV2QoS4PolicyMatchFlowAlias_Type = OctetString
_SleV2QoS4PolicyMatchFlowAlias_Object = MibTableColumn
sleV2QoS4PolicyMatchFlowAlias = _SleV2QoS4PolicyMatchFlowAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 49),
    _SleV2QoS4PolicyMatchFlowAlias_Type()
)
sleV2QoS4PolicyMatchFlowAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchFlowAlias.setStatus("current")


class _SleV2QoS4PolicyMatchInnerVlanCosReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyMatchInnerVlanCosReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4PolicyMatchInnerVlanCosReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyMatchInnerVlanCosReplace_Object = MibTableColumn
sleV2QoS4PolicyMatchInnerVlanCosReplace = _SleV2QoS4PolicyMatchInnerVlanCosReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 50),
    _SleV2QoS4PolicyMatchInnerVlanCosReplace_Type()
)
sleV2QoS4PolicyMatchInnerVlanCosReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchInnerVlanCosReplace.setStatus("current")


class _SleV2QoS4PolicyMatchInnerVlanCfiReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyMatchInnerVlanCfiReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
    )


_SleV2QoS4PolicyMatchInnerVlanCfiReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyMatchInnerVlanCfiReplace_Object = MibTableColumn
sleV2QoS4PolicyMatchInnerVlanCfiReplace = _SleV2QoS4PolicyMatchInnerVlanCfiReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 51),
    _SleV2QoS4PolicyMatchInnerVlanCfiReplace_Type()
)
sleV2QoS4PolicyMatchInnerVlanCfiReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchInnerVlanCfiReplace.setStatus("current")


class _SleV2QoS4PolicyMatchOuterVlanCosReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyMatchOuterVlanCosReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4PolicyMatchOuterVlanCosReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyMatchOuterVlanCosReplace_Object = MibTableColumn
sleV2QoS4PolicyMatchOuterVlanCosReplace = _SleV2QoS4PolicyMatchOuterVlanCosReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 52),
    _SleV2QoS4PolicyMatchOuterVlanCosReplace_Type()
)
sleV2QoS4PolicyMatchOuterVlanCosReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchOuterVlanCosReplace.setStatus("current")


class _SleV2QoS4PolicyMatchOuterVlanCfiReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyMatchOuterVlanCfiReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
    )


_SleV2QoS4PolicyMatchOuterVlanCfiReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyMatchOuterVlanCfiReplace_Object = MibTableColumn
sleV2QoS4PolicyMatchOuterVlanCfiReplace = _SleV2QoS4PolicyMatchOuterVlanCfiReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 1, 1, 53),
    _SleV2QoS4PolicyMatchOuterVlanCfiReplace_Type()
)
sleV2QoS4PolicyMatchOuterVlanCfiReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyMatchOuterVlanCfiReplace.setStatus("current")
_SleV2QoS4PolicyControl_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyControl = _SleV2QoS4PolicyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2)
)


class _SleV2QoS4PolicyControlRequest_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlRequest based on Integer32"""
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
        *(("createPolicy", 1),
          ("setPolicyInfo", 2),
          ("setMatchAction", 3),
          ("setNomatchAction", 4),
          ("destroyPolicy", 5),
          ("clearCounter", 6),
          ("createEmptyPolicy", 7),
          ("setPolicyIngressTunnel", 8),
          ("unsetPolicyIngressTunnel", 9),
          ("setPolicyEgressTunnel", 10),
          ("unsetPolicyEgressTunnel", 11),
          ("setMatchActionFlowAlias", 12),
          ("setMatchInnerVlanCosReplace", 13),
          ("setMatchInnerVlanCfiReplace", 14),
          ("setMatchOuterVlanCosReplace", 15),
          ("setMatchOuterVlanCfiReplace", 16))
    )


_SleV2QoS4PolicyControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlRequest_Object = MibScalar
sleV2QoS4PolicyControlRequest = _SleV2QoS4PolicyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 1),
    _SleV2QoS4PolicyControlRequest_Type()
)
sleV2QoS4PolicyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlRequest.setStatus("current")
_SleV2QoS4PolicyControlStatus_Type = SleControlStatusType
_SleV2QoS4PolicyControlStatus_Object = MibScalar
sleV2QoS4PolicyControlStatus = _SleV2QoS4PolicyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 2),
    _SleV2QoS4PolicyControlStatus_Type()
)
sleV2QoS4PolicyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlStatus.setStatus("current")
_SleV2QoS4PolicyControlTimer_Type = Gauge32
_SleV2QoS4PolicyControlTimer_Object = MibScalar
sleV2QoS4PolicyControlTimer = _SleV2QoS4PolicyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 3),
    _SleV2QoS4PolicyControlTimer_Type()
)
sleV2QoS4PolicyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlTimer.setStatus("current")
_SleV2QoS4PolicyControlTimeStamp_Type = TimeTicks
_SleV2QoS4PolicyControlTimeStamp_Object = MibScalar
sleV2QoS4PolicyControlTimeStamp = _SleV2QoS4PolicyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 4),
    _SleV2QoS4PolicyControlTimeStamp_Type()
)
sleV2QoS4PolicyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlTimeStamp.setStatus("current")
_SleV2QoS4PolicyControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4PolicyControlReqResult_Object = MibScalar
sleV2QoS4PolicyControlReqResult = _SleV2QoS4PolicyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 5),
    _SleV2QoS4PolicyControlReqResult_Type()
)
sleV2QoS4PolicyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlReqResult.setStatus("current")
_SleV2QoS4PolicyControlIndex_Type = IntPolicyIndex
_SleV2QoS4PolicyControlIndex_Object = MibScalar
sleV2QoS4PolicyControlIndex = _SleV2QoS4PolicyControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 6),
    _SleV2QoS4PolicyControlIndex_Type()
)
sleV2QoS4PolicyControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlIndex.setStatus("current")
_SleV2QoS4PolicyControlName_Type = OctetName
_SleV2QoS4PolicyControlName_Object = MibScalar
sleV2QoS4PolicyControlName = _SleV2QoS4PolicyControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 7),
    _SleV2QoS4PolicyControlName_Type()
)
sleV2QoS4PolicyControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlName.setStatus("current")


class _SleV2QoS4PolicyControlPolicerIndex_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1024),
    )


_SleV2QoS4PolicyControlPolicerIndex_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlPolicerIndex_Object = MibScalar
sleV2QoS4PolicyControlPolicerIndex = _SleV2QoS4PolicyControlPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 8),
    _SleV2QoS4PolicyControlPolicerIndex_Type()
)
sleV2QoS4PolicyControlPolicerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlPolicerIndex.setStatus("current")
_SleV2QoS4PolicyControlPriority_Type = IntRulePriority
_SleV2QoS4PolicyControlPriority_Object = MibScalar
sleV2QoS4PolicyControlPriority = _SleV2QoS4PolicyControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 9),
    _SleV2QoS4PolicyControlPriority_Type()
)
sleV2QoS4PolicyControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlPriority.setStatus("current")
_SleV2QoS4PolicyControlIngressPorts_Type = OctetString
_SleV2QoS4PolicyControlIngressPorts_Object = MibScalar
sleV2QoS4PolicyControlIngressPorts = _SleV2QoS4PolicyControlIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 10),
    _SleV2QoS4PolicyControlIngressPorts_Type()
)
sleV2QoS4PolicyControlIngressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlIngressPorts.setStatus("current")
_SleV2QoS4PolicyControlEgressPorts_Type = OctetString
_SleV2QoS4PolicyControlEgressPorts_Object = MibScalar
sleV2QoS4PolicyControlEgressPorts = _SleV2QoS4PolicyControlEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 11),
    _SleV2QoS4PolicyControlEgressPorts_Type()
)
sleV2QoS4PolicyControlEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlEgressPorts.setStatus("current")
_SleV2QoS4PolicyControlVlan_Type = IntVlanID
_SleV2QoS4PolicyControlVlan_Object = MibScalar
sleV2QoS4PolicyControlVlan = _SleV2QoS4PolicyControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 12),
    _SleV2QoS4PolicyControlVlan_Type()
)
sleV2QoS4PolicyControlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlVlan.setStatus("current")


class _SleV2QoS4PolicyControlMatchFlag_Type(Bits):
    """Custom type sleV2QoS4PolicyControlMatchFlag based on Bits"""
    namedValues = NamedValues(
        *(("deny", 0),
          ("mirror", 1),
          ("copyToCPU", 2),
          ("sameAsTos", 3),
          ("sameAsCos", 4),
          ("cos", 5),
          ("tos", 6),
          ("permit", 7))
    )

_SleV2QoS4PolicyControlMatchFlag_Type.__name__ = "Bits"
_SleV2QoS4PolicyControlMatchFlag_Object = MibScalar
sleV2QoS4PolicyControlMatchFlag = _SleV2QoS4PolicyControlMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 13),
    _SleV2QoS4PolicyControlMatchFlag_Type()
)
sleV2QoS4PolicyControlMatchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchFlag.setStatus("current")
_SleV2QoS4PolicyControlMatchVlan_Type = IntVlanID
_SleV2QoS4PolicyControlMatchVlan_Object = MibScalar
sleV2QoS4PolicyControlMatchVlan = _SleV2QoS4PolicyControlMatchVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 14),
    _SleV2QoS4PolicyControlMatchVlan_Type()
)
sleV2QoS4PolicyControlMatchVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchVlan.setStatus("current")
_SleV2QoS4PolicyControlMatchRedirectVlan_Type = IntVlanID
_SleV2QoS4PolicyControlMatchRedirectVlan_Object = MibScalar
sleV2QoS4PolicyControlMatchRedirectVlan = _SleV2QoS4PolicyControlMatchRedirectVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 15),
    _SleV2QoS4PolicyControlMatchRedirectVlan_Type()
)
sleV2QoS4PolicyControlMatchRedirectVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchRedirectVlan.setStatus("current")
_SleV2QoS4PolicyControlMatchRedirectPort_Type = IntInterfaceIndex
_SleV2QoS4PolicyControlMatchRedirectPort_Object = MibScalar
sleV2QoS4PolicyControlMatchRedirectPort = _SleV2QoS4PolicyControlMatchRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 16),
    _SleV2QoS4PolicyControlMatchRedirectPort_Type()
)
sleV2QoS4PolicyControlMatchRedirectPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchRedirectPort.setStatus("current")
_SleV2QoS4PolicyControlMatchMarkMode_Type = IntMarkMode
_SleV2QoS4PolicyControlMatchMarkMode_Object = MibScalar
sleV2QoS4PolicyControlMatchMarkMode = _SleV2QoS4PolicyControlMatchMarkMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 17),
    _SleV2QoS4PolicyControlMatchMarkMode_Type()
)
sleV2QoS4PolicyControlMatchMarkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchMarkMode.setStatus("current")
_SleV2QoS4PolicyControlMatchQueue_Type = IntQueue
_SleV2QoS4PolicyControlMatchQueue_Object = MibScalar
sleV2QoS4PolicyControlMatchQueue = _SleV2QoS4PolicyControlMatchQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 18),
    _SleV2QoS4PolicyControlMatchQueue_Type()
)
sleV2QoS4PolicyControlMatchQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchQueue.setStatus("current")
_SleV2QoS4PolicyControlMatchDp_Type = IntDP
_SleV2QoS4PolicyControlMatchDp_Object = MibScalar
sleV2QoS4PolicyControlMatchDp = _SleV2QoS4PolicyControlMatchDp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 19),
    _SleV2QoS4PolicyControlMatchDp_Type()
)
sleV2QoS4PolicyControlMatchDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchDp.setStatus("current")
_SleV2QoS4PolicyControlMatchCoS_Type = Integer32
_SleV2QoS4PolicyControlMatchCoS_Object = MibScalar
sleV2QoS4PolicyControlMatchCoS = _SleV2QoS4PolicyControlMatchCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 20),
    _SleV2QoS4PolicyControlMatchCoS_Type()
)
sleV2QoS4PolicyControlMatchCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchCoS.setStatus("current")
_SleV2QoS4PolicyControlMatchDscp_Type = IntDscp
_SleV2QoS4PolicyControlMatchDscp_Object = MibScalar
sleV2QoS4PolicyControlMatchDscp = _SleV2QoS4PolicyControlMatchDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 21),
    _SleV2QoS4PolicyControlMatchDscp_Type()
)
sleV2QoS4PolicyControlMatchDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchDscp.setStatus("current")
_SleV2QoS4PolicyControlMatchIpPrecedence_Type = IntIpPrecedence
_SleV2QoS4PolicyControlMatchIpPrecedence_Object = MibScalar
sleV2QoS4PolicyControlMatchIpPrecedence = _SleV2QoS4PolicyControlMatchIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 22),
    _SleV2QoS4PolicyControlMatchIpPrecedence_Type()
)
sleV2QoS4PolicyControlMatchIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchIpPrecedence.setStatus("current")
_SleV2QoS4PolicyControlMatchDstMacOrEgressPorts_Type = IntDstMacOrEgressPorts
_SleV2QoS4PolicyControlMatchDstMacOrEgressPorts_Object = MibScalar
sleV2QoS4PolicyControlMatchDstMacOrEgressPorts = _SleV2QoS4PolicyControlMatchDstMacOrEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 23),
    _SleV2QoS4PolicyControlMatchDstMacOrEgressPorts_Type()
)
sleV2QoS4PolicyControlMatchDstMacOrEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchDstMacOrEgressPorts.setStatus("current")
_SleV2QoS4PolicyControlMatchDstMac_Type = MacAddress
_SleV2QoS4PolicyControlMatchDstMac_Object = MibScalar
sleV2QoS4PolicyControlMatchDstMac = _SleV2QoS4PolicyControlMatchDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 24),
    _SleV2QoS4PolicyControlMatchDstMac_Type()
)
sleV2QoS4PolicyControlMatchDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchDstMac.setStatus("current")
_SleV2QoS4PolicyControlMatchEgressPorts_Type = OctetString
_SleV2QoS4PolicyControlMatchEgressPorts_Object = MibScalar
sleV2QoS4PolicyControlMatchEgressPorts = _SleV2QoS4PolicyControlMatchEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 25),
    _SleV2QoS4PolicyControlMatchEgressPorts_Type()
)
sleV2QoS4PolicyControlMatchEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchEgressPorts.setStatus("current")


class _SleV2QoS4PolicyControlNomatchFlag_Type(Bits):
    """Custom type sleV2QoS4PolicyControlNomatchFlag based on Bits"""
    namedValues = NamedValues(
        *(("deny", 0),
          ("mirror", 1),
          ("copyToCPU", 2),
          ("sameAsTos", 3),
          ("sameAsCos", 4),
          ("cos", 5),
          ("tos", 6),
          ("permit", 7))
    )

_SleV2QoS4PolicyControlNomatchFlag_Type.__name__ = "Bits"
_SleV2QoS4PolicyControlNomatchFlag_Object = MibScalar
sleV2QoS4PolicyControlNomatchFlag = _SleV2QoS4PolicyControlNomatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 26),
    _SleV2QoS4PolicyControlNomatchFlag_Type()
)
sleV2QoS4PolicyControlNomatchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlNomatchFlag.setStatus("current")
_SleV2QoS4PolicyControlNomatchRedirectPort_Type = IntInterfaceIndex
_SleV2QoS4PolicyControlNomatchRedirectPort_Object = MibScalar
sleV2QoS4PolicyControlNomatchRedirectPort = _SleV2QoS4PolicyControlNomatchRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 27),
    _SleV2QoS4PolicyControlNomatchRedirectPort_Type()
)
sleV2QoS4PolicyControlNomatchRedirectPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlNomatchRedirectPort.setStatus("current")
_SleV2QoS4PolicyControlNomatchCoS_Type = IntCoS
_SleV2QoS4PolicyControlNomatchCoS_Object = MibScalar
sleV2QoS4PolicyControlNomatchCoS = _SleV2QoS4PolicyControlNomatchCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 28),
    _SleV2QoS4PolicyControlNomatchCoS_Type()
)
sleV2QoS4PolicyControlNomatchCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlNomatchCoS.setStatus("current")
_SleV2QoS4PolicyControlNomatchDscp_Type = IntDscp
_SleV2QoS4PolicyControlNomatchDscp_Object = MibScalar
sleV2QoS4PolicyControlNomatchDscp = _SleV2QoS4PolicyControlNomatchDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 29),
    _SleV2QoS4PolicyControlNomatchDscp_Type()
)
sleV2QoS4PolicyControlNomatchDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlNomatchDscp.setStatus("current")
_SleV2QoS4PolicyControlNomatchIpPrecedence_Type = IntIpPrecedence
_SleV2QoS4PolicyControlNomatchIpPrecedence_Object = MibScalar
sleV2QoS4PolicyControlNomatchIpPrecedence = _SleV2QoS4PolicyControlNomatchIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 30),
    _SleV2QoS4PolicyControlNomatchIpPrecedence_Type()
)
sleV2QoS4PolicyControlNomatchIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlNomatchIpPrecedence.setStatus("current")
_SleV2QoS4PolicyControlMatchRedirBlackhole_Type = IntEnableFlag
_SleV2QoS4PolicyControlMatchRedirBlackhole_Object = MibScalar
sleV2QoS4PolicyControlMatchRedirBlackhole = _SleV2QoS4PolicyControlMatchRedirBlackhole_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 31),
    _SleV2QoS4PolicyControlMatchRedirBlackhole_Type()
)
sleV2QoS4PolicyControlMatchRedirBlackhole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchRedirBlackhole.setStatus("current")


class _SleV2QoS4PolicyControlIngressTunnelIfIndex_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlIngressTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 11023),
    )


_SleV2QoS4PolicyControlIngressTunnelIfIndex_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlIngressTunnelIfIndex_Object = MibScalar
sleV2QoS4PolicyControlIngressTunnelIfIndex = _SleV2QoS4PolicyControlIngressTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 32),
    _SleV2QoS4PolicyControlIngressTunnelIfIndex_Type()
)
sleV2QoS4PolicyControlIngressTunnelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlIngressTunnelIfIndex.setStatus("current")


class _SleV2Qo4SPolicyControlEgressTunnelIfIndex_Type(Integer32):
    """Custom type sleV2Qo4SPolicyControlEgressTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 11023),
    )


_SleV2Qo4SPolicyControlEgressTunnelIfIndex_Type.__name__ = "Integer32"
_SleV2Qo4SPolicyControlEgressTunnelIfIndex_Object = MibScalar
sleV2Qo4SPolicyControlEgressTunnelIfIndex = _SleV2Qo4SPolicyControlEgressTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 33),
    _SleV2Qo4SPolicyControlEgressTunnelIfIndex_Type()
)
sleV2Qo4SPolicyControlEgressTunnelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Qo4SPolicyControlEgressTunnelIfIndex.setStatus("current")
_SleV2QoS4PolicyControlMatchPbrNextHop_Type = IpAddress
_SleV2QoS4PolicyControlMatchPbrNextHop_Object = MibScalar
sleV2QoS4PolicyControlMatchPbrNextHop = _SleV2QoS4PolicyControlMatchPbrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 34),
    _SleV2QoS4PolicyControlMatchPbrNextHop_Type()
)
sleV2QoS4PolicyControlMatchPbrNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchPbrNextHop.setStatus("current")


class _SleV2QoS4PolicyControlStage_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlStage based on Integer32"""
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
        *(("ingress", 1),
          ("prio", 2),
          ("egress", 3),
          ("external", 4))
    )


_SleV2QoS4PolicyControlStage_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlStage_Object = MibScalar
sleV2QoS4PolicyControlStage = _SleV2QoS4PolicyControlStage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 35),
    _SleV2QoS4PolicyControlStage_Type()
)
sleV2QoS4PolicyControlStage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlStage.setStatus("current")


class _SleV2QoS4PolicyControlIngressPortsFlag_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlIngressPortsFlag based on Integer32"""
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
          ("any", 1),
          ("cpu", 2))
    )


_SleV2QoS4PolicyControlIngressPortsFlag_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlIngressPortsFlag_Object = MibScalar
sleV2QoS4PolicyControlIngressPortsFlag = _SleV2QoS4PolicyControlIngressPortsFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 36),
    _SleV2QoS4PolicyControlIngressPortsFlag_Type()
)
sleV2QoS4PolicyControlIngressPortsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlIngressPortsFlag.setStatus("current")


class _SleV2QoS4PolicyControlEgressPortsFlag_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlEgressPortsFlag based on Integer32"""
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
          ("any", 1),
          ("cpu", 2))
    )


_SleV2QoS4PolicyControlEgressPortsFlag_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlEgressPortsFlag_Object = MibScalar
sleV2QoS4PolicyControlEgressPortsFlag = _SleV2QoS4PolicyControlEgressPortsFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 37),
    _SleV2QoS4PolicyControlEgressPortsFlag_Type()
)
sleV2QoS4PolicyControlEgressPortsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlEgressPortsFlag.setStatus("current")


class _SleV2QoS4PolicyControlInnerVlanAction_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlInnerVlanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("add", 1),
          ("replace", 2),
          ("del", 3))
    )


_SleV2QoS4PolicyControlInnerVlanAction_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlInnerVlanAction_Object = MibScalar
sleV2QoS4PolicyControlInnerVlanAction = _SleV2QoS4PolicyControlInnerVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 38),
    _SleV2QoS4PolicyControlInnerVlanAction_Type()
)
sleV2QoS4PolicyControlInnerVlanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlInnerVlanAction.setStatus("current")


class _SleV2QoS4PolicyControlOuterVlanAction_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlOuterVlanAction based on Integer32"""
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
          ("add", 1),
          ("replace", 2))
    )


_SleV2QoS4PolicyControlOuterVlanAction_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlOuterVlanAction_Object = MibScalar
sleV2QoS4PolicyControlOuterVlanAction = _SleV2QoS4PolicyControlOuterVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 39),
    _SleV2QoS4PolicyControlOuterVlanAction_Type()
)
sleV2QoS4PolicyControlOuterVlanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlOuterVlanAction.setStatus("current")


class _SleV2QoS4PolicyControlInnerVlan_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_SleV2QoS4PolicyControlInnerVlan_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlInnerVlan_Object = MibScalar
sleV2QoS4PolicyControlInnerVlan = _SleV2QoS4PolicyControlInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 40),
    _SleV2QoS4PolicyControlInnerVlan_Type()
)
sleV2QoS4PolicyControlInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlInnerVlan.setStatus("current")


class _SleV2QoS4PolicyControlOuterVlan_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_SleV2QoS4PolicyControlOuterVlan_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlOuterVlan_Object = MibScalar
sleV2QoS4PolicyControlOuterVlan = _SleV2QoS4PolicyControlOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 41),
    _SleV2QoS4PolicyControlOuterVlan_Type()
)
sleV2QoS4PolicyControlOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlOuterVlan.setStatus("current")
_SleV2QoS4PolicyControlMatchPbrNextHopSecondary_Type = IpAddress
_SleV2QoS4PolicyControlMatchPbrNextHopSecondary_Object = MibScalar
sleV2QoS4PolicyControlMatchPbrNextHopSecondary = _SleV2QoS4PolicyControlMatchPbrNextHopSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 42),
    _SleV2QoS4PolicyControlMatchPbrNextHopSecondary_Type()
)
sleV2QoS4PolicyControlMatchPbrNextHopSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchPbrNextHopSecondary.setStatus("current")


class _SleV2QoS4PolicyControlMatchPbrNextHopVerifyReach_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlMatchPbrNextHopVerifyReach based on Integer32"""
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


_SleV2QoS4PolicyControlMatchPbrNextHopVerifyReach_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlMatchPbrNextHopVerifyReach_Object = MibScalar
sleV2QoS4PolicyControlMatchPbrNextHopVerifyReach = _SleV2QoS4PolicyControlMatchPbrNextHopVerifyReach_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 43),
    _SleV2QoS4PolicyControlMatchPbrNextHopVerifyReach_Type()
)
sleV2QoS4PolicyControlMatchPbrNextHopVerifyReach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchPbrNextHopVerifyReach.setStatus("current")
_SleV2QoS4PolicyControlMatchFlowAlias_Type = OctetString
_SleV2QoS4PolicyControlMatchFlowAlias_Object = MibScalar
sleV2QoS4PolicyControlMatchFlowAlias = _SleV2QoS4PolicyControlMatchFlowAlias_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 44),
    _SleV2QoS4PolicyControlMatchFlowAlias_Type()
)
sleV2QoS4PolicyControlMatchFlowAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchFlowAlias.setStatus("current")


class _SleV2QoS4PolicyControlMatchInnerVlanCosReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlMatchInnerVlanCosReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4PolicyControlMatchInnerVlanCosReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlMatchInnerVlanCosReplace_Object = MibScalar
sleV2QoS4PolicyControlMatchInnerVlanCosReplace = _SleV2QoS4PolicyControlMatchInnerVlanCosReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 45),
    _SleV2QoS4PolicyControlMatchInnerVlanCosReplace_Type()
)
sleV2QoS4PolicyControlMatchInnerVlanCosReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchInnerVlanCosReplace.setStatus("current")


class _SleV2QoS4PolicyControlMatchInnerVlanCfiReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlMatchInnerVlanCfiReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
    )


_SleV2QoS4PolicyControlMatchInnerVlanCfiReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlMatchInnerVlanCfiReplace_Object = MibScalar
sleV2QoS4PolicyControlMatchInnerVlanCfiReplace = _SleV2QoS4PolicyControlMatchInnerVlanCfiReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 46),
    _SleV2QoS4PolicyControlMatchInnerVlanCfiReplace_Type()
)
sleV2QoS4PolicyControlMatchInnerVlanCfiReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchInnerVlanCfiReplace.setStatus("current")


class _SleV2QoS4PolicyControlMatchOuterVlanCosReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlMatchOuterVlanCosReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4PolicyControlMatchOuterVlanCosReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlMatchOuterVlanCosReplace_Object = MibScalar
sleV2QoS4PolicyControlMatchOuterVlanCosReplace = _SleV2QoS4PolicyControlMatchOuterVlanCosReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 47),
    _SleV2QoS4PolicyControlMatchOuterVlanCosReplace_Type()
)
sleV2QoS4PolicyControlMatchOuterVlanCosReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchOuterVlanCosReplace.setStatus("current")


class _SleV2QoS4PolicyControlMatchOuterVlanCfiReplace_Type(Integer32):
    """Custom type sleV2QoS4PolicyControlMatchOuterVlanCfiReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
    )


_SleV2QoS4PolicyControlMatchOuterVlanCfiReplace_Type.__name__ = "Integer32"
_SleV2QoS4PolicyControlMatchOuterVlanCfiReplace_Object = MibScalar
sleV2QoS4PolicyControlMatchOuterVlanCfiReplace = _SleV2QoS4PolicyControlMatchOuterVlanCfiReplace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 2, 48),
    _SleV2QoS4PolicyControlMatchOuterVlanCfiReplace_Type()
)
sleV2QoS4PolicyControlMatchOuterVlanCfiReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyControlMatchOuterVlanCfiReplace.setStatus("current")
_SleV2QoSPolicyNotification_ObjectIdentity = ObjectIdentity
sleV2QoSPolicyNotification = _SleV2QoSPolicyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3)
)
_SleV2QoS4PolicyFlowClass_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyFlowClass = _SleV2QoS4PolicyFlowClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2)
)
_SleV2QoS4PolicyFlowClassTable_Object = MibTable
sleV2QoS4PolicyFlowClassTable = _SleV2QoS4PolicyFlowClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassTable.setStatus("current")
_SleV2QoS4PolicyFlowClassEntry_Object = MibTableRow
sleV2QoS4PolicyFlowClassEntry = _SleV2QoS4PolicyFlowClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 1, 1)
)
sleV2QoS4PolicyFlowClassEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PolicyIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassEntry.setStatus("current")
_SleV2QoS4PolicyFlowClassIndex_Type = IntFlowIndex
_SleV2QoS4PolicyFlowClassIndex_Object = MibTableColumn
sleV2QoS4PolicyFlowClassIndex = _SleV2QoS4PolicyFlowClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 1, 1, 1),
    _SleV2QoS4PolicyFlowClassIndex_Type()
)
sleV2QoS4PolicyFlowClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassIndex.setStatus("current")
_SleV2QoS4PolicyFlowClassType_Type = IntFlowOrClass
_SleV2QoS4PolicyFlowClassType_Object = MibTableColumn
sleV2QoS4PolicyFlowClassType = _SleV2QoS4PolicyFlowClassType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 1, 1, 2),
    _SleV2QoS4PolicyFlowClassType_Type()
)
sleV2QoS4PolicyFlowClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassType.setStatus("current")
_SleV2QoS4PolicyFlowClassID_Type = IntFlowIndex
_SleV2QoS4PolicyFlowClassID_Object = MibTableColumn
sleV2QoS4PolicyFlowClassID = _SleV2QoS4PolicyFlowClassID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 1, 1, 3),
    _SleV2QoS4PolicyFlowClassID_Type()
)
sleV2QoS4PolicyFlowClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassID.setStatus("current")
_SleV2QoS4PolicyFlowClassName_Type = OctetName
_SleV2QoS4PolicyFlowClassName_Object = MibTableColumn
sleV2QoS4PolicyFlowClassName = _SleV2QoS4PolicyFlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 1, 1, 4),
    _SleV2QoS4PolicyFlowClassName_Type()
)
sleV2QoS4PolicyFlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassName.setStatus("current")
_SleV2QoS4PolicyFlowClassControl_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyFlowClassControl = _SleV2QoS4PolicyFlowClassControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2)
)


class _SleV2QoS4PolicyFlowClassControlRequest_Type(Integer32):
    """Custom type sleV2QoS4PolicyFlowClassControlRequest based on Integer32"""
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
        *(("addFlowClass", 1),
          ("deleteFlowClass", 2),
          ("deleteAllFlow", 3),
          ("deleteAllClass", 4),
          ("deleteAllFlowClass", 5))
    )


_SleV2QoS4PolicyFlowClassControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4PolicyFlowClassControlRequest_Object = MibScalar
sleV2QoS4PolicyFlowClassControlRequest = _SleV2QoS4PolicyFlowClassControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 1),
    _SleV2QoS4PolicyFlowClassControlRequest_Type()
)
sleV2QoS4PolicyFlowClassControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlRequest.setStatus("current")
_SleV2QoS4PolicyFlowClassControlStatus_Type = SleControlStatusType
_SleV2QoS4PolicyFlowClassControlStatus_Object = MibScalar
sleV2QoS4PolicyFlowClassControlStatus = _SleV2QoS4PolicyFlowClassControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 2),
    _SleV2QoS4PolicyFlowClassControlStatus_Type()
)
sleV2QoS4PolicyFlowClassControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlStatus.setStatus("current")
_SleV2QoS4PolicyFlowClassControlTimer_Type = Gauge32
_SleV2QoS4PolicyFlowClassControlTimer_Object = MibScalar
sleV2QoS4PolicyFlowClassControlTimer = _SleV2QoS4PolicyFlowClassControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 3),
    _SleV2QoS4PolicyFlowClassControlTimer_Type()
)
sleV2QoS4PolicyFlowClassControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlTimer.setStatus("current")
_SleV2QoS4PolicyFlowClassControlTimeStamp_Type = TimeTicks
_SleV2QoS4PolicyFlowClassControlTimeStamp_Object = MibScalar
sleV2QoS4PolicyFlowClassControlTimeStamp = _SleV2QoS4PolicyFlowClassControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 4),
    _SleV2QoS4PolicyFlowClassControlTimeStamp_Type()
)
sleV2QoS4PolicyFlowClassControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlTimeStamp.setStatus("current")
_SleV2QoS4PolicyFlowClassControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4PolicyFlowClassControlReqResult_Object = MibScalar
sleV2QoS4PolicyFlowClassControlReqResult = _SleV2QoS4PolicyFlowClassControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 5),
    _SleV2QoS4PolicyFlowClassControlReqResult_Type()
)
sleV2QoS4PolicyFlowClassControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlReqResult.setStatus("current")
_SleV2QoS4PolicyFlowClassControlPolicyIndex_Type = IntPolicyIndex
_SleV2QoS4PolicyFlowClassControlPolicyIndex_Object = MibScalar
sleV2QoS4PolicyFlowClassControlPolicyIndex = _SleV2QoS4PolicyFlowClassControlPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 6),
    _SleV2QoS4PolicyFlowClassControlPolicyIndex_Type()
)
sleV2QoS4PolicyFlowClassControlPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlPolicyIndex.setStatus("current")
_SleV2QoS4PolicyFlowClassControlIndex_Type = IntFlowIndex
_SleV2QoS4PolicyFlowClassControlIndex_Object = MibScalar
sleV2QoS4PolicyFlowClassControlIndex = _SleV2QoS4PolicyFlowClassControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 7),
    _SleV2QoS4PolicyFlowClassControlIndex_Type()
)
sleV2QoS4PolicyFlowClassControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlIndex.setStatus("current")
_SleV2QoS4PolicyFlowClassControlType_Type = IntFlowOrClass
_SleV2QoS4PolicyFlowClassControlType_Object = MibScalar
sleV2QoS4PolicyFlowClassControlType = _SleV2QoS4PolicyFlowClassControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 8),
    _SleV2QoS4PolicyFlowClassControlType_Type()
)
sleV2QoS4PolicyFlowClassControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlType.setStatus("current")
_SleV2QoS4PolicyFlowClassControlFlowID_Type = IntFlowIndex
_SleV2QoS4PolicyFlowClassControlFlowID_Object = MibScalar
sleV2QoS4PolicyFlowClassControlFlowID = _SleV2QoS4PolicyFlowClassControlFlowID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 9),
    _SleV2QoS4PolicyFlowClassControlFlowID_Type()
)
sleV2QoS4PolicyFlowClassControlFlowID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlFlowID.setStatus("current")
_SleV2QoS4PolicyFlowClassControlClassID_Type = IntClassIndex
_SleV2QoS4PolicyFlowClassControlClassID_Object = MibScalar
sleV2QoS4PolicyFlowClassControlClassID = _SleV2QoS4PolicyFlowClassControlClassID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 2, 10),
    _SleV2QoS4PolicyFlowClassControlClassID_Type()
)
sleV2QoS4PolicyFlowClassControlClassID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyFlowClassControlClassID.setStatus("current")
_SleV2QoS4PolicyFlowClassNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyFlowClassNotification = _SleV2QoS4PolicyFlowClassNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 3)
)
_SleV2QoS4PolicyIF_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyIF = _SleV2QoS4PolicyIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3)
)
_SleV2QoS4PolicyIFTable_Object = MibTable
sleV2QoS4PolicyIFTable = _SleV2QoS4PolicyIFTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFTable.setStatus("current")
_SleV2QoS4PolicyIFEntry_Object = MibTableRow
sleV2QoS4PolicyIFEntry = _SleV2QoS4PolicyIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 1, 1)
)
sleV2QoS4PolicyIFEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "ifindex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PolicyIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PolicyIFDirection"),
)
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFEntry.setStatus("current")


class _SleV2QoS4PolicyIFDirection_Type(Integer32):
    """Custom type sleV2QoS4PolicyIFDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_SleV2QoS4PolicyIFDirection_Type.__name__ = "Integer32"
_SleV2QoS4PolicyIFDirection_Object = MibTableColumn
sleV2QoS4PolicyIFDirection = _SleV2QoS4PolicyIFDirection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 1, 1, 1),
    _SleV2QoS4PolicyIFDirection_Type()
)
sleV2QoS4PolicyIFDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFDirection.setStatus("current")
_SleV2QoS4PolicyIFControl_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyIFControl = _SleV2QoS4PolicyIFControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2)
)


class _SleV2QoS4PolicyIFControlRequest_Type(Integer32):
    """Custom type sleV2QoS4PolicyIFControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setServicePolicy", 1),
          ("clearServicePolicy", 2))
    )


_SleV2QoS4PolicyIFControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4PolicyIFControlRequest_Object = MibScalar
sleV2QoS4PolicyIFControlRequest = _SleV2QoS4PolicyIFControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 1),
    _SleV2QoS4PolicyIFControlRequest_Type()
)
sleV2QoS4PolicyIFControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlRequest.setStatus("current")
_SleV2QoS4PolicyIFControlStatus_Type = SleControlStatusType
_SleV2QoS4PolicyIFControlStatus_Object = MibScalar
sleV2QoS4PolicyIFControlStatus = _SleV2QoS4PolicyIFControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 2),
    _SleV2QoS4PolicyIFControlStatus_Type()
)
sleV2QoS4PolicyIFControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlStatus.setStatus("current")
_SleV2QoS4PolicyIFControlTimer_Type = Gauge32
_SleV2QoS4PolicyIFControlTimer_Object = MibScalar
sleV2QoS4PolicyIFControlTimer = _SleV2QoS4PolicyIFControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 3),
    _SleV2QoS4PolicyIFControlTimer_Type()
)
sleV2QoS4PolicyIFControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlTimer.setStatus("current")
_SleV2QoS4PolicyIFControlTimeStamp_Type = TimeTicks
_SleV2QoS4PolicyIFControlTimeStamp_Object = MibScalar
sleV2QoS4PolicyIFControlTimeStamp = _SleV2QoS4PolicyIFControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 4),
    _SleV2QoS4PolicyIFControlTimeStamp_Type()
)
sleV2QoS4PolicyIFControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlTimeStamp.setStatus("current")
_SleV2QoS4PolicyIFControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4PolicyIFControlReqResult_Object = MibScalar
sleV2QoS4PolicyIFControlReqResult = _SleV2QoS4PolicyIFControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 5),
    _SleV2QoS4PolicyIFControlReqResult_Type()
)
sleV2QoS4PolicyIFControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlReqResult.setStatus("current")
_SleV2QoS4PolicyIFControlIfindex_Type = Integer32
_SleV2QoS4PolicyIFControlIfindex_Object = MibScalar
sleV2QoS4PolicyIFControlIfindex = _SleV2QoS4PolicyIFControlIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 6),
    _SleV2QoS4PolicyIFControlIfindex_Type()
)
sleV2QoS4PolicyIFControlIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlIfindex.setStatus("current")
_SleV2QoS4PolicyIFControlPolicyIndex_Type = IntPolicerIndex
_SleV2QoS4PolicyIFControlPolicyIndex_Object = MibScalar
sleV2QoS4PolicyIFControlPolicyIndex = _SleV2QoS4PolicyIFControlPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 7),
    _SleV2QoS4PolicyIFControlPolicyIndex_Type()
)
sleV2QoS4PolicyIFControlPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlPolicyIndex.setStatus("current")


class _SleV2QoS4PolicyIFControlDirection_Type(Integer32):
    """Custom type sleV2QoS4PolicyIFControlDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_SleV2QoS4PolicyIFControlDirection_Type.__name__ = "Integer32"
_SleV2QoS4PolicyIFControlDirection_Object = MibScalar
sleV2QoS4PolicyIFControlDirection = _SleV2QoS4PolicyIFControlDirection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 2, 8),
    _SleV2QoS4PolicyIFControlDirection_Type()
)
sleV2QoS4PolicyIFControlDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PolicyIFControlDirection.setStatus("current")
_SleV2QoS4PolicyIFNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4PolicyIFNotification = _SleV2QoS4PolicyIFNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 3)
)
_SleV2QoS4Remark_ObjectIdentity = ObjectIdentity
sleV2QoS4Remark = _SleV2QoS4Remark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6)
)
_SleV2QoS4RemarkBase_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkBase = _SleV2QoS4RemarkBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1)
)
_SleV2QoS4RemarkInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkInfo = _SleV2QoS4RemarkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 1)
)
_SleV2QoS4RemarkLayer2Mode_Type = IntL2BaseRemarkMode
_SleV2QoS4RemarkLayer2Mode_Object = MibScalar
sleV2QoS4RemarkLayer2Mode = _SleV2QoS4RemarkLayer2Mode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 1, 1),
    _SleV2QoS4RemarkLayer2Mode_Type()
)
sleV2QoS4RemarkLayer2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkLayer2Mode.setStatus("current")


class _SleV2QoS4RemarkMode_Type(Bits):
    """Custom type sleV2QoS4RemarkMode based on Bits"""
    namedValues = NamedValues(
        *(("remarkPriorityIP", 0),
          ("remarkByQueueOrCoS", 1))
    )

_SleV2QoS4RemarkMode_Type.__name__ = "Bits"
_SleV2QoS4RemarkMode_Object = MibScalar
sleV2QoS4RemarkMode = _SleV2QoS4RemarkMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 1, 2),
    _SleV2QoS4RemarkMode_Type()
)
sleV2QoS4RemarkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkMode.setStatus("current")
_SleV2QoS4RemarkControl_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkControl = _SleV2QoS4RemarkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2)
)


class _SleV2QoS4RemarkControlRequest_Type(Integer32):
    """Custom type sleV2QoS4RemarkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setRemarkMode", 1)
    )


_SleV2QoS4RemarkControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4RemarkControlRequest_Object = MibScalar
sleV2QoS4RemarkControlRequest = _SleV2QoS4RemarkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2, 1),
    _SleV2QoS4RemarkControlRequest_Type()
)
sleV2QoS4RemarkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkControlRequest.setStatus("current")
_SleV2QoS4RemarkControlStatus_Type = SleControlStatusType
_SleV2QoS4RemarkControlStatus_Object = MibScalar
sleV2QoS4RemarkControlStatus = _SleV2QoS4RemarkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2, 2),
    _SleV2QoS4RemarkControlStatus_Type()
)
sleV2QoS4RemarkControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkControlStatus.setStatus("current")
_SleV2QoS4RemarkControlTimer_Type = Gauge32
_SleV2QoS4RemarkControlTimer_Object = MibScalar
sleV2QoS4RemarkControlTimer = _SleV2QoS4RemarkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2, 3),
    _SleV2QoS4RemarkControlTimer_Type()
)
sleV2QoS4RemarkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkControlTimer.setStatus("current")
_SleV2QoS4RemarkControlTimStamp_Type = TimeTicks
_SleV2QoS4RemarkControlTimStamp_Object = MibScalar
sleV2QoS4RemarkControlTimStamp = _SleV2QoS4RemarkControlTimStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2, 4),
    _SleV2QoS4RemarkControlTimStamp_Type()
)
sleV2QoS4RemarkControlTimStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkControlTimStamp.setStatus("current")
_SleV2QoS4RemarkControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4RemarkControlReqResult_Object = MibScalar
sleV2QoS4RemarkControlReqResult = _SleV2QoS4RemarkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2, 5),
    _SleV2QoS4RemarkControlReqResult_Type()
)
sleV2QoS4RemarkControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkControlReqResult.setStatus("current")
_SleV2QoS4RemarkControlLayer2Mode_Type = IntL2BaseRemarkMode
_SleV2QoS4RemarkControlLayer2Mode_Object = MibScalar
sleV2QoS4RemarkControlLayer2Mode = _SleV2QoS4RemarkControlLayer2Mode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2, 6),
    _SleV2QoS4RemarkControlLayer2Mode_Type()
)
sleV2QoS4RemarkControlLayer2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkControlLayer2Mode.setStatus("current")


class _SleV2QoS4RemarkControlMode_Type(Bits):
    """Custom type sleV2QoS4RemarkControlMode based on Bits"""
    namedValues = NamedValues(
        *(("remarkByDSCP", 0),
          ("remarkByQueueOrCoS", 1))
    )

_SleV2QoS4RemarkControlMode_Type.__name__ = "Bits"
_SleV2QoS4RemarkControlMode_Object = MibScalar
sleV2QoS4RemarkControlMode = _SleV2QoS4RemarkControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 2, 7),
    _SleV2QoS4RemarkControlMode_Type()
)
sleV2QoS4RemarkControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkControlMode.setStatus("current")
_SleV2QoS4RemarkNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkNotification = _SleV2QoS4RemarkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 3)
)
_SleV2QoS4RemarkL3_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkL3 = _SleV2QoS4RemarkL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2)
)
_SleV2QoS4RemarkL3Table_Object = MibTable
sleV2QoS4RemarkL3Table = _SleV2QoS4RemarkL3Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3Table.setStatus("current")
_SleV2QoS4RemarkL3Entry_Object = MibTableRow
sleV2QoS4RemarkL3Entry = _SleV2QoS4RemarkL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1, 1)
)
sleV2QoS4RemarkL3Entry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ColorIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4RemarkL3DSCPIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3Entry.setStatus("current")
_SleV2QoS4RemarkL3ColorIndex_Type = IntColorIndex
_SleV2QoS4RemarkL3ColorIndex_Object = MibTableColumn
sleV2QoS4RemarkL3ColorIndex = _SleV2QoS4RemarkL3ColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1, 1, 1),
    _SleV2QoS4RemarkL3ColorIndex_Type()
)
sleV2QoS4RemarkL3ColorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ColorIndex.setStatus("current")
_SleV2QoS4RemarkL3DSCPIndex_Type = IntDSCPIndex
_SleV2QoS4RemarkL3DSCPIndex_Object = MibTableColumn
sleV2QoS4RemarkL3DSCPIndex = _SleV2QoS4RemarkL3DSCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1, 1, 2),
    _SleV2QoS4RemarkL3DSCPIndex_Type()
)
sleV2QoS4RemarkL3DSCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3DSCPIndex.setStatus("current")
_SleV2QoS4RemarkL3Queue_Type = IntQueue
_SleV2QoS4RemarkL3Queue_Object = MibTableColumn
sleV2QoS4RemarkL3Queue = _SleV2QoS4RemarkL3Queue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1, 1, 3),
    _SleV2QoS4RemarkL3Queue_Type()
)
sleV2QoS4RemarkL3Queue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3Queue.setStatus("current")
_SleV2QoS4RemarkL3Dp_Type = IntDP
_SleV2QoS4RemarkL3Dp_Object = MibTableColumn
sleV2QoS4RemarkL3Dp = _SleV2QoS4RemarkL3Dp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1, 1, 4),
    _SleV2QoS4RemarkL3Dp_Type()
)
sleV2QoS4RemarkL3Dp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3Dp.setStatus("current")
_SleV2QoS4RemarkL3CoS_Type = IntCoS
_SleV2QoS4RemarkL3CoS_Object = MibTableColumn
sleV2QoS4RemarkL3CoS = _SleV2QoS4RemarkL3CoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1, 1, 5),
    _SleV2QoS4RemarkL3CoS_Type()
)
sleV2QoS4RemarkL3CoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3CoS.setStatus("current")
_SleV2QoS4RemarkL3Dscp_Type = IntDscp
_SleV2QoS4RemarkL3Dscp_Object = MibTableColumn
sleV2QoS4RemarkL3Dscp = _SleV2QoS4RemarkL3Dscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 1, 1, 6),
    _SleV2QoS4RemarkL3Dscp_Type()
)
sleV2QoS4RemarkL3Dscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3Dscp.setStatus("current")
_SleV2QoS4RemarkL3Control_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkL3Control = _SleV2QoS4RemarkL3Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2)
)


class _SleV2QoS4RemarkL3ControlRequest_Type(Integer32):
    """Custom type sleV2QoS4RemarkL3ControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setL3Remark", 1)
    )


_SleV2QoS4RemarkL3ControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4RemarkL3ControlRequest_Object = MibScalar
sleV2QoS4RemarkL3ControlRequest = _SleV2QoS4RemarkL3ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 1),
    _SleV2QoS4RemarkL3ControlRequest_Type()
)
sleV2QoS4RemarkL3ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlRequest.setStatus("current")
_SleV2QoS4RemarkL3ControlStatus_Type = SleControlStatusType
_SleV2QoS4RemarkL3ControlStatus_Object = MibScalar
sleV2QoS4RemarkL3ControlStatus = _SleV2QoS4RemarkL3ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 2),
    _SleV2QoS4RemarkL3ControlStatus_Type()
)
sleV2QoS4RemarkL3ControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlStatus.setStatus("current")
_SleV2QoS4RemarkL3ControlTimer_Type = Gauge32
_SleV2QoS4RemarkL3ControlTimer_Object = MibScalar
sleV2QoS4RemarkL3ControlTimer = _SleV2QoS4RemarkL3ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 3),
    _SleV2QoS4RemarkL3ControlTimer_Type()
)
sleV2QoS4RemarkL3ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlTimer.setStatus("current")
_SleV2QoS4RemarkL3ControlTimeStamp_Type = TimeTicks
_SleV2QoS4RemarkL3ControlTimeStamp_Object = MibScalar
sleV2QoS4RemarkL3ControlTimeStamp = _SleV2QoS4RemarkL3ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 4),
    _SleV2QoS4RemarkL3ControlTimeStamp_Type()
)
sleV2QoS4RemarkL3ControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlTimeStamp.setStatus("current")
_SleV2QoS4RemarkL3ControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4RemarkL3ControlReqResult_Object = MibScalar
sleV2QoS4RemarkL3ControlReqResult = _SleV2QoS4RemarkL3ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 5),
    _SleV2QoS4RemarkL3ControlReqResult_Type()
)
sleV2QoS4RemarkL3ControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlReqResult.setStatus("current")
_SleV2QoS4RemarkL3ControlColorIndex_Type = IntColorIndex
_SleV2QoS4RemarkL3ControlColorIndex_Object = MibScalar
sleV2QoS4RemarkL3ControlColorIndex = _SleV2QoS4RemarkL3ControlColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 6),
    _SleV2QoS4RemarkL3ControlColorIndex_Type()
)
sleV2QoS4RemarkL3ControlColorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlColorIndex.setStatus("current")
_SleV2QoS4RemarkL3ControlDSCPIndex_Type = IntDSCPIndex
_SleV2QoS4RemarkL3ControlDSCPIndex_Object = MibScalar
sleV2QoS4RemarkL3ControlDSCPIndex = _SleV2QoS4RemarkL3ControlDSCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 7),
    _SleV2QoS4RemarkL3ControlDSCPIndex_Type()
)
sleV2QoS4RemarkL3ControlDSCPIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlDSCPIndex.setStatus("current")
_SleV2QoS4RemarkL3ControlQueue_Type = IntQueue
_SleV2QoS4RemarkL3ControlQueue_Object = MibScalar
sleV2QoS4RemarkL3ControlQueue = _SleV2QoS4RemarkL3ControlQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 8),
    _SleV2QoS4RemarkL3ControlQueue_Type()
)
sleV2QoS4RemarkL3ControlQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlQueue.setStatus("current")
_SleV2QoS4RemarkL3ControlDp_Type = IntDP
_SleV2QoS4RemarkL3ControlDp_Object = MibScalar
sleV2QoS4RemarkL3ControlDp = _SleV2QoS4RemarkL3ControlDp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 9),
    _SleV2QoS4RemarkL3ControlDp_Type()
)
sleV2QoS4RemarkL3ControlDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlDp.setStatus("current")
_SleV2QoS4RemarkL3ControlCoS_Type = IntCoS
_SleV2QoS4RemarkL3ControlCoS_Object = MibScalar
sleV2QoS4RemarkL3ControlCoS = _SleV2QoS4RemarkL3ControlCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 10),
    _SleV2QoS4RemarkL3ControlCoS_Type()
)
sleV2QoS4RemarkL3ControlCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlCoS.setStatus("current")
_SleV2QoS4RemarkL3ControlDscp_Type = IntDscp
_SleV2QoS4RemarkL3ControlDscp_Object = MibScalar
sleV2QoS4RemarkL3ControlDscp = _SleV2QoS4RemarkL3ControlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 2, 11),
    _SleV2QoS4RemarkL3ControlDscp_Type()
)
sleV2QoS4RemarkL3ControlDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL3ControlDscp.setStatus("current")
_SleV2QoS4RemarkL3Notification_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkL3Notification = _SleV2QoS4RemarkL3Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 3)
)
_SleV2QoS4RemarkL2_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkL2 = _SleV2QoS4RemarkL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3)
)
_SleV2QoS4RemarkL2Table_Object = MibTable
sleV2QoS4RemarkL2Table = _SleV2QoS4RemarkL2Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2Table.setStatus("current")
_SleV2QoS4RemarkL2Entry_Object = MibTableRow
sleV2QoS4RemarkL2Entry = _SleV2QoS4RemarkL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1, 1)
)
sleV2QoS4RemarkL2Entry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ColorIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4RemarkL2QueueCoSIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2Entry.setStatus("current")
_SleV2QoS4RemarkL2ColorIndex_Type = IntColorIndex
_SleV2QoS4RemarkL2ColorIndex_Object = MibTableColumn
sleV2QoS4RemarkL2ColorIndex = _SleV2QoS4RemarkL2ColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1, 1, 1),
    _SleV2QoS4RemarkL2ColorIndex_Type()
)
sleV2QoS4RemarkL2ColorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ColorIndex.setStatus("current")
_SleV2QoS4RemarkL2QueueCoSIndex_Type = IntQueueCoSIndex
_SleV2QoS4RemarkL2QueueCoSIndex_Object = MibTableColumn
sleV2QoS4RemarkL2QueueCoSIndex = _SleV2QoS4RemarkL2QueueCoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1, 1, 2),
    _SleV2QoS4RemarkL2QueueCoSIndex_Type()
)
sleV2QoS4RemarkL2QueueCoSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2QueueCoSIndex.setStatus("current")
_SleV2QoS4RemarkL2Queue_Type = IntQueue
_SleV2QoS4RemarkL2Queue_Object = MibTableColumn
sleV2QoS4RemarkL2Queue = _SleV2QoS4RemarkL2Queue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1, 1, 3),
    _SleV2QoS4RemarkL2Queue_Type()
)
sleV2QoS4RemarkL2Queue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2Queue.setStatus("current")
_SleV2QoS4RemarkL2Dp_Type = IntDP
_SleV2QoS4RemarkL2Dp_Object = MibTableColumn
sleV2QoS4RemarkL2Dp = _SleV2QoS4RemarkL2Dp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1, 1, 4),
    _SleV2QoS4RemarkL2Dp_Type()
)
sleV2QoS4RemarkL2Dp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2Dp.setStatus("current")
_SleV2QoS4RemarkL2CoS_Type = IntCoS
_SleV2QoS4RemarkL2CoS_Object = MibTableColumn
sleV2QoS4RemarkL2CoS = _SleV2QoS4RemarkL2CoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1, 1, 5),
    _SleV2QoS4RemarkL2CoS_Type()
)
sleV2QoS4RemarkL2CoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2CoS.setStatus("current")
_SleV2QoS4RemarkL2Dscp_Type = IntDscp
_SleV2QoS4RemarkL2Dscp_Object = MibTableColumn
sleV2QoS4RemarkL2Dscp = _SleV2QoS4RemarkL2Dscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 1, 1, 6),
    _SleV2QoS4RemarkL2Dscp_Type()
)
sleV2QoS4RemarkL2Dscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2Dscp.setStatus("current")
_SleV2QoS4RemarkL2Control_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkL2Control = _SleV2QoS4RemarkL2Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2)
)


class _SleV2QoS4RemarkL2ControlRequest_Type(Integer32):
    """Custom type sleV2QoS4RemarkL2ControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setL2Remark", 1)
    )


_SleV2QoS4RemarkL2ControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4RemarkL2ControlRequest_Object = MibScalar
sleV2QoS4RemarkL2ControlRequest = _SleV2QoS4RemarkL2ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 1),
    _SleV2QoS4RemarkL2ControlRequest_Type()
)
sleV2QoS4RemarkL2ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlRequest.setStatus("current")
_SleV2QoS4RemarkL2ControlStatus_Type = SleControlStatusType
_SleV2QoS4RemarkL2ControlStatus_Object = MibScalar
sleV2QoS4RemarkL2ControlStatus = _SleV2QoS4RemarkL2ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 2),
    _SleV2QoS4RemarkL2ControlStatus_Type()
)
sleV2QoS4RemarkL2ControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlStatus.setStatus("current")
_SleV2QoS4RemarkL2ControlTimer_Type = Gauge32
_SleV2QoS4RemarkL2ControlTimer_Object = MibScalar
sleV2QoS4RemarkL2ControlTimer = _SleV2QoS4RemarkL2ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 3),
    _SleV2QoS4RemarkL2ControlTimer_Type()
)
sleV2QoS4RemarkL2ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlTimer.setStatus("current")
_SleV2QoS4RemarkL2ControlTimeStamp_Type = TimeTicks
_SleV2QoS4RemarkL2ControlTimeStamp_Object = MibScalar
sleV2QoS4RemarkL2ControlTimeStamp = _SleV2QoS4RemarkL2ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 4),
    _SleV2QoS4RemarkL2ControlTimeStamp_Type()
)
sleV2QoS4RemarkL2ControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlTimeStamp.setStatus("current")
_SleV2QoS4RemarkL2ControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4RemarkL2ControlReqResult_Object = MibScalar
sleV2QoS4RemarkL2ControlReqResult = _SleV2QoS4RemarkL2ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 5),
    _SleV2QoS4RemarkL2ControlReqResult_Type()
)
sleV2QoS4RemarkL2ControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlReqResult.setStatus("current")
_SleV2QoS4RemarkL2ControlColorIndex_Type = IntColorIndex
_SleV2QoS4RemarkL2ControlColorIndex_Object = MibScalar
sleV2QoS4RemarkL2ControlColorIndex = _SleV2QoS4RemarkL2ControlColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 6),
    _SleV2QoS4RemarkL2ControlColorIndex_Type()
)
sleV2QoS4RemarkL2ControlColorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlColorIndex.setStatus("current")
_SleV2QoS4RemarkL2ControlQueueCoSIndex_Type = IntQueueCoSIndex
_SleV2QoS4RemarkL2ControlQueueCoSIndex_Object = MibScalar
sleV2QoS4RemarkL2ControlQueueCoSIndex = _SleV2QoS4RemarkL2ControlQueueCoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 7),
    _SleV2QoS4RemarkL2ControlQueueCoSIndex_Type()
)
sleV2QoS4RemarkL2ControlQueueCoSIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlQueueCoSIndex.setStatus("current")
_SleV2QoS4RemarkL2ControlQueue_Type = IntQueue
_SleV2QoS4RemarkL2ControlQueue_Object = MibScalar
sleV2QoS4RemarkL2ControlQueue = _SleV2QoS4RemarkL2ControlQueue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 8),
    _SleV2QoS4RemarkL2ControlQueue_Type()
)
sleV2QoS4RemarkL2ControlQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlQueue.setStatus("current")
_SleV2QoS4RemarkL2ControlDp_Type = IntDP
_SleV2QoS4RemarkL2ControlDp_Object = MibScalar
sleV2QoS4RemarkL2ControlDp = _SleV2QoS4RemarkL2ControlDp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 9),
    _SleV2QoS4RemarkL2ControlDp_Type()
)
sleV2QoS4RemarkL2ControlDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlDp.setStatus("current")
_SleV2QoS4RemarkL2ControlCoS_Type = IntCoS
_SleV2QoS4RemarkL2ControlCoS_Object = MibScalar
sleV2QoS4RemarkL2ControlCoS = _SleV2QoS4RemarkL2ControlCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 10),
    _SleV2QoS4RemarkL2ControlCoS_Type()
)
sleV2QoS4RemarkL2ControlCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlCoS.setStatus("current")
_SleV2QoS4RemarkL2ControlDscp_Type = IntDscp
_SleV2QoS4RemarkL2ControlDscp_Object = MibScalar
sleV2QoS4RemarkL2ControlDscp = _SleV2QoS4RemarkL2ControlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 2, 11),
    _SleV2QoS4RemarkL2ControlDscp_Type()
)
sleV2QoS4RemarkL2ControlDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4RemarkL2ControlDscp.setStatus("current")
_SleV2QoS4RemarkL2Notification_ObjectIdentity = ObjectIdentity
sleV2QoS4RemarkL2Notification = _SleV2QoS4RemarkL2Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 3)
)
_SleV2QoS4RED_ObjectIdentity = ObjectIdentity
sleV2QoS4RED = _SleV2QoS4RED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7)
)
_SleV2QoS4REDProfile_ObjectIdentity = ObjectIdentity
sleV2QoS4REDProfile = _SleV2QoS4REDProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1)
)
_SleV2QoS4REDProfileTable_Object = MibTable
sleV2QoS4REDProfileTable = _SleV2QoS4REDProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileTable.setStatus("current")
_SleV2QoS4REDProfileEntry_Object = MibTableRow
sleV2QoS4REDProfileEntry = _SleV2QoS4REDProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1)
)
sleV2QoS4REDProfileEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4REDProfileId"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4REDProfileQueueId"),
)
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileEntry.setStatus("current")


class _SleV2QoS4REDProfileId_Type(Integer32):
    """Custom type sleV2QoS4REDProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2QoS4REDProfileId_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileId_Object = MibTableColumn
sleV2QoS4REDProfileId = _SleV2QoS4REDProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 1),
    _SleV2QoS4REDProfileId_Type()
)
sleV2QoS4REDProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileId.setStatus("current")


class _SleV2QoS4REDProfileQueueId_Type(Integer32):
    """Custom type sleV2QoS4REDProfileQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2QoS4REDProfileQueueId_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileQueueId_Object = MibTableColumn
sleV2QoS4REDProfileQueueId = _SleV2QoS4REDProfileQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 2),
    _SleV2QoS4REDProfileQueueId_Type()
)
sleV2QoS4REDProfileQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileQueueId.setStatus("current")


class _SleV2QoS4REDProfileDp0MinThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp0MinThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileDp0MinThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp0MinThres_Object = MibTableColumn
sleV2QoS4REDProfileDp0MinThres = _SleV2QoS4REDProfileDp0MinThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 3),
    _SleV2QoS4REDProfileDp0MinThres_Type()
)
sleV2QoS4REDProfileDp0MinThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp0MinThres.setStatus("current")


class _SleV2QoS4REDProfileDp0MaxThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp0MaxThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileDp0MaxThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp0MaxThres_Object = MibTableColumn
sleV2QoS4REDProfileDp0MaxThres = _SleV2QoS4REDProfileDp0MaxThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 4),
    _SleV2QoS4REDProfileDp0MaxThres_Type()
)
sleV2QoS4REDProfileDp0MaxThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp0MaxThres.setStatus("current")


class _SleV2QoS4REDProfileDp0Prob_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp0Prob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileDp0Prob_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp0Prob_Object = MibTableColumn
sleV2QoS4REDProfileDp0Prob = _SleV2QoS4REDProfileDp0Prob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 5),
    _SleV2QoS4REDProfileDp0Prob_Type()
)
sleV2QoS4REDProfileDp0Prob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp0Prob.setStatus("current")


class _SleV2QoS4REDProfileDp1MinThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp1MinThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileDp1MinThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp1MinThres_Object = MibTableColumn
sleV2QoS4REDProfileDp1MinThres = _SleV2QoS4REDProfileDp1MinThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 6),
    _SleV2QoS4REDProfileDp1MinThres_Type()
)
sleV2QoS4REDProfileDp1MinThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp1MinThres.setStatus("current")


class _SleV2QoS4REDProfileDp1MaxThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp1MaxThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileDp1MaxThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp1MaxThres_Object = MibTableColumn
sleV2QoS4REDProfileDp1MaxThres = _SleV2QoS4REDProfileDp1MaxThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 7),
    _SleV2QoS4REDProfileDp1MaxThres_Type()
)
sleV2QoS4REDProfileDp1MaxThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp1MaxThres.setStatus("current")


class _SleV2QoS4REDProfileDp1Prob_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp1Prob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileDp1Prob_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp1Prob_Object = MibTableColumn
sleV2QoS4REDProfileDp1Prob = _SleV2QoS4REDProfileDp1Prob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 8),
    _SleV2QoS4REDProfileDp1Prob_Type()
)
sleV2QoS4REDProfileDp1Prob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp1Prob.setStatus("current")


class _SleV2QoS4REDProfileDp2MinThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp2MinThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileDp2MinThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp2MinThres_Object = MibTableColumn
sleV2QoS4REDProfileDp2MinThres = _SleV2QoS4REDProfileDp2MinThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 9),
    _SleV2QoS4REDProfileDp2MinThres_Type()
)
sleV2QoS4REDProfileDp2MinThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp2MinThres.setStatus("current")


class _SleV2QoS4REDProfileDp2MaxThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp2MaxThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileDp2MaxThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp2MaxThres_Object = MibTableColumn
sleV2QoS4REDProfileDp2MaxThres = _SleV2QoS4REDProfileDp2MaxThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 10),
    _SleV2QoS4REDProfileDp2MaxThres_Type()
)
sleV2QoS4REDProfileDp2MaxThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp2MaxThres.setStatus("current")


class _SleV2QoS4REDProfileDp2Prob_Type(Integer32):
    """Custom type sleV2QoS4REDProfileDp2Prob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileDp2Prob_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileDp2Prob_Object = MibTableColumn
sleV2QoS4REDProfileDp2Prob = _SleV2QoS4REDProfileDp2Prob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 11),
    _SleV2QoS4REDProfileDp2Prob_Type()
)
sleV2QoS4REDProfileDp2Prob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileDp2Prob.setStatus("current")


class _SleV2QoS4REDProfileWeight_Type(Integer32):
    """Custom type sleV2QoS4REDProfileWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileWeight_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileWeight_Object = MibTableColumn
sleV2QoS4REDProfileWeight = _SleV2QoS4REDProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 1, 1, 12),
    _SleV2QoS4REDProfileWeight_Type()
)
sleV2QoS4REDProfileWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileWeight.setStatus("current")
_SleV2QoS4REDProfileControl_ObjectIdentity = ObjectIdentity
sleV2QoS4REDProfileControl = _SleV2QoS4REDProfileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2)
)


class _SleV2QoS4REDProfileControlRequest_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setREDProfile", 1),
          ("clearREDProfile", 2))
    )


_SleV2QoS4REDProfileControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlRequest_Object = MibScalar
sleV2QoS4REDProfileControlRequest = _SleV2QoS4REDProfileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 1),
    _SleV2QoS4REDProfileControlRequest_Type()
)
sleV2QoS4REDProfileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlRequest.setStatus("current")
_SleV2QoS4REDProfileControlStatus_Type = SleControlStatusType
_SleV2QoS4REDProfileControlStatus_Object = MibScalar
sleV2QoS4REDProfileControlStatus = _SleV2QoS4REDProfileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 2),
    _SleV2QoS4REDProfileControlStatus_Type()
)
sleV2QoS4REDProfileControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlStatus.setStatus("current")
_SleV2QoS4REDProfileControlTimer_Type = Gauge32
_SleV2QoS4REDProfileControlTimer_Object = MibScalar
sleV2QoS4REDProfileControlTimer = _SleV2QoS4REDProfileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 3),
    _SleV2QoS4REDProfileControlTimer_Type()
)
sleV2QoS4REDProfileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlTimer.setStatus("current")
_SleV2QoS4REDProfileControlTimeStamp_Type = TimeTicks
_SleV2QoS4REDProfileControlTimeStamp_Object = MibScalar
sleV2QoS4REDProfileControlTimeStamp = _SleV2QoS4REDProfileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 4),
    _SleV2QoS4REDProfileControlTimeStamp_Type()
)
sleV2QoS4REDProfileControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlTimeStamp.setStatus("current")
_SleV2QoS4REDProfileControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4REDProfileControlReqResult_Object = MibScalar
sleV2QoS4REDProfileControlReqResult = _SleV2QoS4REDProfileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 5),
    _SleV2QoS4REDProfileControlReqResult_Type()
)
sleV2QoS4REDProfileControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlReqResult.setStatus("current")


class _SleV2QoS4REDProfileControlId_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2QoS4REDProfileControlId_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlId_Object = MibScalar
sleV2QoS4REDProfileControlId = _SleV2QoS4REDProfileControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 6),
    _SleV2QoS4REDProfileControlId_Type()
)
sleV2QoS4REDProfileControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlId.setStatus("current")


class _SleV2QoS4REDProfileControlQueueId_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2QoS4REDProfileControlQueueId_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlQueueId_Object = MibScalar
sleV2QoS4REDProfileControlQueueId = _SleV2QoS4REDProfileControlQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 7),
    _SleV2QoS4REDProfileControlQueueId_Type()
)
sleV2QoS4REDProfileControlQueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlQueueId.setStatus("current")


class _SleV2QoS4REDProfileControlDp0MinThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp0MinThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileControlDp0MinThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp0MinThres_Object = MibScalar
sleV2QoS4REDProfileControlDp0MinThres = _SleV2QoS4REDProfileControlDp0MinThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 8),
    _SleV2QoS4REDProfileControlDp0MinThres_Type()
)
sleV2QoS4REDProfileControlDp0MinThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp0MinThres.setStatus("current")


class _SleV2QoS4REDProfileControlDp0MaxThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp0MaxThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileControlDp0MaxThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp0MaxThres_Object = MibScalar
sleV2QoS4REDProfileControlDp0MaxThres = _SleV2QoS4REDProfileControlDp0MaxThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 9),
    _SleV2QoS4REDProfileControlDp0MaxThres_Type()
)
sleV2QoS4REDProfileControlDp0MaxThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp0MaxThres.setStatus("current")


class _SleV2QoS4REDProfileControlDp0Prob_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp0Prob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileControlDp0Prob_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp0Prob_Object = MibScalar
sleV2QoS4REDProfileControlDp0Prob = _SleV2QoS4REDProfileControlDp0Prob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 10),
    _SleV2QoS4REDProfileControlDp0Prob_Type()
)
sleV2QoS4REDProfileControlDp0Prob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp0Prob.setStatus("current")


class _SleV2QoS4REDProfileControlDp1MinThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp1MinThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileControlDp1MinThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp1MinThres_Object = MibScalar
sleV2QoS4REDProfileControlDp1MinThres = _SleV2QoS4REDProfileControlDp1MinThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 11),
    _SleV2QoS4REDProfileControlDp1MinThres_Type()
)
sleV2QoS4REDProfileControlDp1MinThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp1MinThres.setStatus("current")


class _SleV2QoS4REDProfileControlDp1MaxThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp1MaxThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileControlDp1MaxThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp1MaxThres_Object = MibScalar
sleV2QoS4REDProfileControlDp1MaxThres = _SleV2QoS4REDProfileControlDp1MaxThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 12),
    _SleV2QoS4REDProfileControlDp1MaxThres_Type()
)
sleV2QoS4REDProfileControlDp1MaxThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp1MaxThres.setStatus("current")


class _SleV2QoS4REDProfileControlDp1Prob_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp1Prob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileControlDp1Prob_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp1Prob_Object = MibScalar
sleV2QoS4REDProfileControlDp1Prob = _SleV2QoS4REDProfileControlDp1Prob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 13),
    _SleV2QoS4REDProfileControlDp1Prob_Type()
)
sleV2QoS4REDProfileControlDp1Prob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp1Prob.setStatus("current")


class _SleV2QoS4REDProfileControlDp2MinThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp2MinThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileControlDp2MinThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp2MinThres_Object = MibScalar
sleV2QoS4REDProfileControlDp2MinThres = _SleV2QoS4REDProfileControlDp2MinThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 14),
    _SleV2QoS4REDProfileControlDp2MinThres_Type()
)
sleV2QoS4REDProfileControlDp2MinThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp2MinThres.setStatus("current")


class _SleV2QoS4REDProfileControlDp2MaxThres_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp2MaxThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleV2QoS4REDProfileControlDp2MaxThres_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp2MaxThres_Object = MibScalar
sleV2QoS4REDProfileControlDp2MaxThres = _SleV2QoS4REDProfileControlDp2MaxThres_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 15),
    _SleV2QoS4REDProfileControlDp2MaxThres_Type()
)
sleV2QoS4REDProfileControlDp2MaxThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp2MaxThres.setStatus("current")


class _SleV2QoS4REDProfileControlDp2Prob_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlDp2Prob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileControlDp2Prob_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlDp2Prob_Object = MibScalar
sleV2QoS4REDProfileControlDp2Prob = _SleV2QoS4REDProfileControlDp2Prob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 16),
    _SleV2QoS4REDProfileControlDp2Prob_Type()
)
sleV2QoS4REDProfileControlDp2Prob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlDp2Prob.setStatus("current")


class _SleV2QoS4REDProfileControlWeight_Type(Integer32):
    """Custom type sleV2QoS4REDProfileControlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 15),
    )


_SleV2QoS4REDProfileControlWeight_Type.__name__ = "Integer32"
_SleV2QoS4REDProfileControlWeight_Object = MibScalar
sleV2QoS4REDProfileControlWeight = _SleV2QoS4REDProfileControlWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 2, 17),
    _SleV2QoS4REDProfileControlWeight_Type()
)
sleV2QoS4REDProfileControlWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4REDProfileControlWeight.setStatus("current")
_SleV2QoS4REDProfileNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4REDProfileNotification = _SleV2QoS4REDProfileNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 3)
)
_SleV2QoS4PortREDInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4PortREDInfo = _SleV2QoS4PortREDInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2)
)
_SleV2QoS4PortREDInfoTable_Object = MibTable
sleV2QoS4PortREDInfoTable = _SleV2QoS4PortREDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoTable.setStatus("current")
_SleV2QoS4PortREDInfoEntry_Object = MibTableRow
sleV2QoS4PortREDInfoEntry = _SleV2QoS4PortREDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 1, 1)
)
sleV2QoS4PortREDInfoEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoEntry.setStatus("current")
_SleV2QoS4PortREDInfoInterfaceIndex_Type = InterfaceIndex
_SleV2QoS4PortREDInfoInterfaceIndex_Object = MibTableColumn
sleV2QoS4PortREDInfoInterfaceIndex = _SleV2QoS4PortREDInfoInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 1, 1, 1),
    _SleV2QoS4PortREDInfoInterfaceIndex_Type()
)
sleV2QoS4PortREDInfoInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoInterfaceIndex.setStatus("current")


class _SleV2QoS4PortREDInfoEnable_Type(Integer32):
    """Custom type sleV2QoS4PortREDInfoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("red", 1),
          ("wred", 2))
    )


_SleV2QoS4PortREDInfoEnable_Type.__name__ = "Integer32"
_SleV2QoS4PortREDInfoEnable_Object = MibTableColumn
sleV2QoS4PortREDInfoEnable = _SleV2QoS4PortREDInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 1, 1, 2),
    _SleV2QoS4PortREDInfoEnable_Type()
)
sleV2QoS4PortREDInfoEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoEnable.setStatus("current")


class _SleV2QoS4PortREDInfoProfileId_Type(Integer32):
    """Custom type sleV2QoS4PortREDInfoProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_SleV2QoS4PortREDInfoProfileId_Type.__name__ = "Integer32"
_SleV2QoS4PortREDInfoProfileId_Object = MibTableColumn
sleV2QoS4PortREDInfoProfileId = _SleV2QoS4PortREDInfoProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 1, 1, 3),
    _SleV2QoS4PortREDInfoProfileId_Type()
)
sleV2QoS4PortREDInfoProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoProfileId.setStatus("current")
_SleV2QoS4PortREDInfoControl_ObjectIdentity = ObjectIdentity
sleV2QoS4PortREDInfoControl = _SleV2QoS4PortREDInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2)
)


class _SleV2QoS4PortREDInfoControlRequest_Type(Integer32):
    """Custom type sleV2QoS4PortREDInfoControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setPortREDInfo", 1)
    )


_SleV2QoS4PortREDInfoControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4PortREDInfoControlRequest_Object = MibScalar
sleV2QoS4PortREDInfoControlRequest = _SleV2QoS4PortREDInfoControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 1),
    _SleV2QoS4PortREDInfoControlRequest_Type()
)
sleV2QoS4PortREDInfoControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlRequest.setStatus("current")
_SleV2QoS4PortREDInfoControlStatus_Type = SleControlStatusType
_SleV2QoS4PortREDInfoControlStatus_Object = MibScalar
sleV2QoS4PortREDInfoControlStatus = _SleV2QoS4PortREDInfoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 2),
    _SleV2QoS4PortREDInfoControlStatus_Type()
)
sleV2QoS4PortREDInfoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlStatus.setStatus("current")
_SleV2QoS4PortREDInfoControlTimer_Type = Gauge32
_SleV2QoS4PortREDInfoControlTimer_Object = MibScalar
sleV2QoS4PortREDInfoControlTimer = _SleV2QoS4PortREDInfoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 3),
    _SleV2QoS4PortREDInfoControlTimer_Type()
)
sleV2QoS4PortREDInfoControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlTimer.setStatus("current")
_SleV2QoS4PortREDInfoControlTimeStamp_Type = TimeTicks
_SleV2QoS4PortREDInfoControlTimeStamp_Object = MibScalar
sleV2QoS4PortREDInfoControlTimeStamp = _SleV2QoS4PortREDInfoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 4),
    _SleV2QoS4PortREDInfoControlTimeStamp_Type()
)
sleV2QoS4PortREDInfoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlTimeStamp.setStatus("current")
_SleV2QoS4PortREDInfoControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4PortREDInfoControlReqResult_Object = MibScalar
sleV2QoS4PortREDInfoControlReqResult = _SleV2QoS4PortREDInfoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 5),
    _SleV2QoS4PortREDInfoControlReqResult_Type()
)
sleV2QoS4PortREDInfoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlReqResult.setStatus("current")
_SleV2QoS4PortREDInfoControlInterfaceIndex_Type = InterfaceIndex
_SleV2QoS4PortREDInfoControlInterfaceIndex_Object = MibScalar
sleV2QoS4PortREDInfoControlInterfaceIndex = _SleV2QoS4PortREDInfoControlInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 6),
    _SleV2QoS4PortREDInfoControlInterfaceIndex_Type()
)
sleV2QoS4PortREDInfoControlInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlInterfaceIndex.setStatus("current")


class _SleV2QoS4PortREDInfoControlEnable_Type(Integer32):
    """Custom type sleV2QoS4PortREDInfoControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("red", 1),
          ("wred", 2))
    )


_SleV2QoS4PortREDInfoControlEnable_Type.__name__ = "Integer32"
_SleV2QoS4PortREDInfoControlEnable_Object = MibScalar
sleV2QoS4PortREDInfoControlEnable = _SleV2QoS4PortREDInfoControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 7),
    _SleV2QoS4PortREDInfoControlEnable_Type()
)
sleV2QoS4PortREDInfoControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlEnable.setStatus("current")


class _SleV2QoS4PortREDInfoControlProfileId_Type(Integer32):
    """Custom type sleV2QoS4PortREDInfoControlProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_SleV2QoS4PortREDInfoControlProfileId_Type.__name__ = "Integer32"
_SleV2QoS4PortREDInfoControlProfileId_Object = MibScalar
sleV2QoS4PortREDInfoControlProfileId = _SleV2QoS4PortREDInfoControlProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 2, 8),
    _SleV2QoS4PortREDInfoControlProfileId_Type()
)
sleV2QoS4PortREDInfoControlProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoControlProfileId.setStatus("current")
_SleV2QoS4PortREDInfoNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4PortREDInfoNotification = _SleV2QoS4PortREDInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 3)
)
_SleV2QoS4Queue_ObjectIdentity = ObjectIdentity
sleV2QoS4Queue = _SleV2QoS4Queue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8)
)
_SleV2QoS4QueueInfo_ObjectIdentity = ObjectIdentity
sleV2QoS4QueueInfo = _SleV2QoS4QueueInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1)
)
_SleV2QoS4QueueInfoTable_Object = MibTable
sleV2QoS4QueueInfoTable = _SleV2QoS4QueueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoTable.setStatus("current")
_SleV2QoS4QueueInfoEntry_Object = MibTableRow
sleV2QoS4QueueInfoEntry = _SleV2QoS4QueueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1)
)
sleV2QoS4QueueInfoEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4QueueInfoInterfaceIndex"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4QueueInfoId"),
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoEntry.setStatus("current")
_SleV2QoS4QueueInfoInterfaceIndex_Type = InterfaceIndex
_SleV2QoS4QueueInfoInterfaceIndex_Object = MibTableColumn
sleV2QoS4QueueInfoInterfaceIndex = _SleV2QoS4QueueInfoInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 1),
    _SleV2QoS4QueueInfoInterfaceIndex_Type()
)
sleV2QoS4QueueInfoInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoInterfaceIndex.setStatus("current")


class _SleV2QoS4QueueInfoId_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2QoS4QueueInfoId_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoId_Object = MibTableColumn
sleV2QoS4QueueInfoId = _SleV2QoS4QueueInfoId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 2),
    _SleV2QoS4QueueInfoId_Type()
)
sleV2QoS4QueueInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoId.setStatus("current")


class _SleV2QoS4QueueInfoScheduleMode_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoScheduleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("rr", 2),
          ("wrr", 3),
          ("wfq", 4),
          ("drr", 5),
          ("bd", 6))
    )


_SleV2QoS4QueueInfoScheduleMode_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoScheduleMode_Object = MibTableColumn
sleV2QoS4QueueInfoScheduleMode = _SleV2QoS4QueueInfoScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 3),
    _SleV2QoS4QueueInfoScheduleMode_Type()
)
sleV2QoS4QueueInfoScheduleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoScheduleMode.setStatus("current")


class _SleV2QoS4QueueInfoDWRRGroup_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoDWRRGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("group0", 1),
          ("group1", 2))
    )


_SleV2QoS4QueueInfoDWRRGroup_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoDWRRGroup_Object = MibTableColumn
sleV2QoS4QueueInfoDWRRGroup = _SleV2QoS4QueueInfoDWRRGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 4),
    _SleV2QoS4QueueInfoDWRRGroup_Type()
)
sleV2QoS4QueueInfoDWRRGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoDWRRGroup.setStatus("current")
_SleV2QoS4QueueInfoMinBandwidth_Type = Integer32
_SleV2QoS4QueueInfoMinBandwidth_Object = MibTableColumn
sleV2QoS4QueueInfoMinBandwidth = _SleV2QoS4QueueInfoMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 5),
    _SleV2QoS4QueueInfoMinBandwidth_Type()
)
sleV2QoS4QueueInfoMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoMinBandwidth.setStatus("current")
_SleV2QoS4QueueInfoMaxBandwidth_Type = Integer32
_SleV2QoS4QueueInfoMaxBandwidth_Object = MibTableColumn
sleV2QoS4QueueInfoMaxBandwidth = _SleV2QoS4QueueInfoMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 6),
    _SleV2QoS4QueueInfoMaxBandwidth_Type()
)
sleV2QoS4QueueInfoMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoMaxBandwidth.setStatus("current")


class _SleV2QoS4QueueInfoWeight_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_SleV2QoS4QueueInfoWeight_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoWeight_Object = MibTableColumn
sleV2QoS4QueueInfoWeight = _SleV2QoS4QueueInfoWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 7),
    _SleV2QoS4QueueInfoWeight_Type()
)
sleV2QoS4QueueInfoWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoWeight.setStatus("current")


class _SleV2QoS4QueueMappedCoS_Type(Integer32):
    """Custom type sleV2QoS4QueueMappedCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4QueueMappedCoS_Type.__name__ = "Integer32"
_SleV2QoS4QueueMappedCoS_Object = MibTableColumn
sleV2QoS4QueueMappedCoS = _SleV2QoS4QueueMappedCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 8),
    _SleV2QoS4QueueMappedCoS_Type()
)
sleV2QoS4QueueMappedCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueMappedCoS.setStatus("current")
_SleV2QoS4QueueInfoBufferEgressMinLimitUnicast_Type = Integer32
_SleV2QoS4QueueInfoBufferEgressMinLimitUnicast_Object = MibTableColumn
sleV2QoS4QueueInfoBufferEgressMinLimitUnicast = _SleV2QoS4QueueInfoBufferEgressMinLimitUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 9),
    _SleV2QoS4QueueInfoBufferEgressMinLimitUnicast_Type()
)
sleV2QoS4QueueInfoBufferEgressMinLimitUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMinLimitUnicast.setStatus("current")


class _SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast_Object = MibTableColumn
sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast = _SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 10),
    _SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast_Type()
)
sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast.setStatus("current")
_SleV2QoS4QueueInfoBufferEgressMaxLimitUnicast_Type = Integer32
_SleV2QoS4QueueInfoBufferEgressMaxLimitUnicast_Object = MibTableColumn
sleV2QoS4QueueInfoBufferEgressMaxLimitUnicast = _SleV2QoS4QueueInfoBufferEgressMaxLimitUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 11),
    _SleV2QoS4QueueInfoBufferEgressMaxLimitUnicast_Type()
)
sleV2QoS4QueueInfoBufferEgressMaxLimitUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitUnicast.setStatus("current")
_SleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast_Type = Integer32
_SleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast_Object = MibTableColumn
sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast = _SleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 12),
    _SleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast_Type()
)
sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast.setStatus("current")


class _SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast_Object = MibTableColumn
sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast = _SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 13),
    _SleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast_Type()
)
sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast.setStatus("current")
_SleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast_Type = Integer32
_SleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast_Object = MibTableColumn
sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast = _SleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 1, 1, 14),
    _SleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast_Type()
)
sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast.setStatus("current")
_SleV2QoS4QueueInfoControl_ObjectIdentity = ObjectIdentity
sleV2QoS4QueueInfoControl = _SleV2QoS4QueueInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2)
)


class _SleV2QoS4QueueInfoControlRequest_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlRequest based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("setQueueInfo", 1),
          ("setScheduleMode", 2),
          ("setMaxBandwidth", 3),
          ("setMinBandwidth", 4),
          ("setWeight", 5),
          ("setBufferEgressMinLimitUnicast", 6),
          ("clearBufferEgressMinLimitUnicast", 7),
          ("setBufferEgressMaxLimitUnicast", 8),
          ("clearBufferEgressMaxLimitUnicast", 9),
          ("setBufferEgressMinLimitNonUnicast", 10),
          ("clearBufferEgressMinLimitNonUnicast", 11),
          ("setBufferEgressMaxLimitNonUnicast", 12),
          ("clearBufferEgressMaxLimitNonUnicast", 13))
    )


_SleV2QoS4QueueInfoControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlRequest_Object = MibScalar
sleV2QoS4QueueInfoControlRequest = _SleV2QoS4QueueInfoControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 1),
    _SleV2QoS4QueueInfoControlRequest_Type()
)
sleV2QoS4QueueInfoControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlRequest.setStatus("current")
_SleV2QoS4QueueInfoControlStatus_Type = SleControlStatusType
_SleV2QoS4QueueInfoControlStatus_Object = MibScalar
sleV2QoS4QueueInfoControlStatus = _SleV2QoS4QueueInfoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 2),
    _SleV2QoS4QueueInfoControlStatus_Type()
)
sleV2QoS4QueueInfoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlStatus.setStatus("current")
_SleV2QoS4QueueInfoControlTimer_Type = Gauge32
_SleV2QoS4QueueInfoControlTimer_Object = MibScalar
sleV2QoS4QueueInfoControlTimer = _SleV2QoS4QueueInfoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 3),
    _SleV2QoS4QueueInfoControlTimer_Type()
)
sleV2QoS4QueueInfoControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlTimer.setStatus("current")
_SleV2QoS4QueueInfoControlTimeStamp_Type = TimeTicks
_SleV2QoS4QueueInfoControlTimeStamp_Object = MibScalar
sleV2QoS4QueueInfoControlTimeStamp = _SleV2QoS4QueueInfoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 4),
    _SleV2QoS4QueueInfoControlTimeStamp_Type()
)
sleV2QoS4QueueInfoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlTimeStamp.setStatus("current")
_SleV2QoS4QueueInfoControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4QueueInfoControlReqResult_Object = MibScalar
sleV2QoS4QueueInfoControlReqResult = _SleV2QoS4QueueInfoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 5),
    _SleV2QoS4QueueInfoControlReqResult_Type()
)
sleV2QoS4QueueInfoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlReqResult.setStatus("current")
_SleV2QoS4QueueInfoControlInterfaceIndex_Type = InterfaceIndex
_SleV2QoS4QueueInfoControlInterfaceIndex_Object = MibScalar
sleV2QoS4QueueInfoControlInterfaceIndex = _SleV2QoS4QueueInfoControlInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 6),
    _SleV2QoS4QueueInfoControlInterfaceIndex_Type()
)
sleV2QoS4QueueInfoControlInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlInterfaceIndex.setStatus("current")


class _SleV2QoS4QueueInfoControlId_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2QoS4QueueInfoControlId_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlId_Object = MibScalar
sleV2QoS4QueueInfoControlId = _SleV2QoS4QueueInfoControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 7),
    _SleV2QoS4QueueInfoControlId_Type()
)
sleV2QoS4QueueInfoControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlId.setStatus("current")


class _SleV2QoS4QueueInfoControlScheduleMode_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlScheduleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("rr", 2),
          ("wrr", 3),
          ("wfq", 4),
          ("drr", 5),
          ("bd", 6))
    )


_SleV2QoS4QueueInfoControlScheduleMode_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlScheduleMode_Object = MibScalar
sleV2QoS4QueueInfoControlScheduleMode = _SleV2QoS4QueueInfoControlScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 8),
    _SleV2QoS4QueueInfoControlScheduleMode_Type()
)
sleV2QoS4QueueInfoControlScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlScheduleMode.setStatus("current")


class _SleV2QoS4QueueInfoControlDWRRGroup_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlDWRRGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("group0", 1),
          ("group1", 2))
    )


_SleV2QoS4QueueInfoControlDWRRGroup_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlDWRRGroup_Object = MibScalar
sleV2QoS4QueueInfoControlDWRRGroup = _SleV2QoS4QueueInfoControlDWRRGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 9),
    _SleV2QoS4QueueInfoControlDWRRGroup_Type()
)
sleV2QoS4QueueInfoControlDWRRGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlDWRRGroup.setStatus("current")
_SleV2QoS4QueueInfoControlMinBandwidth_Type = Integer32
_SleV2QoS4QueueInfoControlMinBandwidth_Object = MibScalar
sleV2QoS4QueueInfoControlMinBandwidth = _SleV2QoS4QueueInfoControlMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 10),
    _SleV2QoS4QueueInfoControlMinBandwidth_Type()
)
sleV2QoS4QueueInfoControlMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlMinBandwidth.setStatus("current")
_SleV2QoS4QueueInfoControlMaxBandwidth_Type = Integer32
_SleV2QoS4QueueInfoControlMaxBandwidth_Object = MibScalar
sleV2QoS4QueueInfoControlMaxBandwidth = _SleV2QoS4QueueInfoControlMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 11),
    _SleV2QoS4QueueInfoControlMaxBandwidth_Type()
)
sleV2QoS4QueueInfoControlMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlMaxBandwidth.setStatus("current")


class _SleV2QoS4QueueInfoControlWeight_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2QoS4QueueInfoControlWeight_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlWeight_Object = MibScalar
sleV2QoS4QueueInfoControlWeight = _SleV2QoS4QueueInfoControlWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 12),
    _SleV2QoS4QueueInfoControlWeight_Type()
)
sleV2QoS4QueueInfoControlWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlWeight.setStatus("current")


class _SleV2QoS4QueueInfoControlMappedCoS_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlMappedCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4QueueInfoControlMappedCoS_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlMappedCoS_Object = MibScalar
sleV2QoS4QueueInfoControlMappedCoS = _SleV2QoS4QueueInfoControlMappedCoS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 13),
    _SleV2QoS4QueueInfoControlMappedCoS_Type()
)
sleV2QoS4QueueInfoControlMappedCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlMappedCoS.setStatus("current")
_SleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast_Type = Integer32
_SleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast_Object = MibScalar
sleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast = _SleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 14),
    _SleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast_Type()
)
sleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast.setStatus("current")


class _SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast_Object = MibScalar
sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast = _SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 15),
    _SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast_Type()
)
sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast.setStatus("current")
_SleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast_Type = Integer32
_SleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast_Object = MibScalar
sleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast = _SleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 16),
    _SleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast_Type()
)
sleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast.setStatus("current")
_SleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast_Type = Integer32
_SleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast_Object = MibScalar
sleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast = _SleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 17),
    _SleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast_Type()
)
sleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast.setStatus("current")


class _SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast_Type(Integer32):
    """Custom type sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast_Type.__name__ = "Integer32"
_SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast_Object = MibScalar
sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast = _SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 18),
    _SleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast_Type()
)
sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast.setStatus("current")
_SleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast_Type = Integer32
_SleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast_Object = MibScalar
sleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast = _SleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 2, 19),
    _SleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast_Type()
)
sleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast.setStatus("current")
_SleV2QoS4QueueInfoNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4QueueInfoNotification = _SleV2QoS4QueueInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3)
)
_SleV2QoS4DscpMap_ObjectIdentity = ObjectIdentity
sleV2QoS4DscpMap = _SleV2QoS4DscpMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9)
)
_SleV2QoS4DscpMapIngress_ObjectIdentity = ObjectIdentity
sleV2QoS4DscpMapIngress = _SleV2QoS4DscpMapIngress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1)
)
_SleV2QoS4DscpMapIngressTable_Object = MibTable
sleV2QoS4DscpMapIngressTable = _SleV2QoS4DscpMapIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressTable.setStatus("current")
_SleV2QoS4DscpMapIngressEntry_Object = MibTableRow
sleV2QoS4DscpMapIngressEntry = _SleV2QoS4DscpMapIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 1, 1)
)
sleV2QoS4DscpMapIngressEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressDscpIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressEntry.setStatus("current")


class _SleV2QoS4DscpMapIngressDscpIndex_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SleV2QoS4DscpMapIngressDscpIndex_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressDscpIndex_Object = MibTableColumn
sleV2QoS4DscpMapIngressDscpIndex = _SleV2QoS4DscpMapIngressDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 1, 1, 1),
    _SleV2QoS4DscpMapIngressDscpIndex_Type()
)
sleV2QoS4DscpMapIngressDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressDscpIndex.setStatus("current")


class _SleV2QoS4DscpMapIngressDscp_Type(OctetString):
    """Custom type sleV2QoS4DscpMapIngressDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleV2QoS4DscpMapIngressDscp_Type.__name__ = "OctetString"
_SleV2QoS4DscpMapIngressDscp_Object = MibTableColumn
sleV2QoS4DscpMapIngressDscp = _SleV2QoS4DscpMapIngressDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 1, 1, 2),
    _SleV2QoS4DscpMapIngressDscp_Type()
)
sleV2QoS4DscpMapIngressDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressDscp.setStatus("current")


class _SleV2QoS4DscpMapIngressCos_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4DscpMapIngressCos_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressCos_Object = MibTableColumn
sleV2QoS4DscpMapIngressCos = _SleV2QoS4DscpMapIngressCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 1, 1, 3),
    _SleV2QoS4DscpMapIngressCos_Type()
)
sleV2QoS4DscpMapIngressCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressCos.setStatus("current")


class _SleV2QoS4DscpMapIngressColor_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_SleV2QoS4DscpMapIngressColor_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressColor_Object = MibTableColumn
sleV2QoS4DscpMapIngressColor = _SleV2QoS4DscpMapIngressColor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 1, 1, 4),
    _SleV2QoS4DscpMapIngressColor_Type()
)
sleV2QoS4DscpMapIngressColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressColor.setStatus("current")
_SleV2QoS4DscpMapIngressControl_ObjectIdentity = ObjectIdentity
sleV2QoS4DscpMapIngressControl = _SleV2QoS4DscpMapIngressControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2)
)


class _SleV2QoS4DscpMapIngressControlRequest_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDscpMapIngress", 1)
    )


_SleV2QoS4DscpMapIngressControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressControlRequest_Object = MibScalar
sleV2QoS4DscpMapIngressControlRequest = _SleV2QoS4DscpMapIngressControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 1),
    _SleV2QoS4DscpMapIngressControlRequest_Type()
)
sleV2QoS4DscpMapIngressControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlRequest.setStatus("current")
_SleV2QoS4DscpMapIngressControlStatus_Type = SleControlStatusType
_SleV2QoS4DscpMapIngressControlStatus_Object = MibScalar
sleV2QoS4DscpMapIngressControlStatus = _SleV2QoS4DscpMapIngressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 2),
    _SleV2QoS4DscpMapIngressControlStatus_Type()
)
sleV2QoS4DscpMapIngressControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlStatus.setStatus("current")
_SleV2QoS4DscpMapIngressControlTimer_Type = Gauge32
_SleV2QoS4DscpMapIngressControlTimer_Object = MibScalar
sleV2QoS4DscpMapIngressControlTimer = _SleV2QoS4DscpMapIngressControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 3),
    _SleV2QoS4DscpMapIngressControlTimer_Type()
)
sleV2QoS4DscpMapIngressControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlTimer.setStatus("current")
_SleV2QoS4DscpMapIngressControlTimeStamp_Type = TimeTicks
_SleV2QoS4DscpMapIngressControlTimeStamp_Object = MibScalar
sleV2QoS4DscpMapIngressControlTimeStamp = _SleV2QoS4DscpMapIngressControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 4),
    _SleV2QoS4DscpMapIngressControlTimeStamp_Type()
)
sleV2QoS4DscpMapIngressControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlTimeStamp.setStatus("current")
_SleV2QoS4DscpMapIngressControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4DscpMapIngressControlReqResult_Object = MibScalar
sleV2QoS4DscpMapIngressControlReqResult = _SleV2QoS4DscpMapIngressControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 5),
    _SleV2QoS4DscpMapIngressControlReqResult_Type()
)
sleV2QoS4DscpMapIngressControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlReqResult.setStatus("current")


class _SleV2QoS4DscpMapIngressControlDscpIndex_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressControlDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SleV2QoS4DscpMapIngressControlDscpIndex_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressControlDscpIndex_Object = MibScalar
sleV2QoS4DscpMapIngressControlDscpIndex = _SleV2QoS4DscpMapIngressControlDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 6),
    _SleV2QoS4DscpMapIngressControlDscpIndex_Type()
)
sleV2QoS4DscpMapIngressControlDscpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlDscpIndex.setStatus("current")


class _SleV2QoS4DscpMapIngressControlDscp_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressControlDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleV2QoS4DscpMapIngressControlDscp_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressControlDscp_Object = MibScalar
sleV2QoS4DscpMapIngressControlDscp = _SleV2QoS4DscpMapIngressControlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 7),
    _SleV2QoS4DscpMapIngressControlDscp_Type()
)
sleV2QoS4DscpMapIngressControlDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlDscp.setStatus("current")


class _SleV2QoS4DscpMapIngressControlCos_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressControlCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleV2QoS4DscpMapIngressControlCos_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressControlCos_Object = MibScalar
sleV2QoS4DscpMapIngressControlCos = _SleV2QoS4DscpMapIngressControlCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 8),
    _SleV2QoS4DscpMapIngressControlCos_Type()
)
sleV2QoS4DscpMapIngressControlCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlCos.setStatus("current")


class _SleV2QoS4DscpMapIngressControlColor_Type(Integer32):
    """Custom type sleV2QoS4DscpMapIngressControlColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_SleV2QoS4DscpMapIngressControlColor_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapIngressControlColor_Object = MibScalar
sleV2QoS4DscpMapIngressControlColor = _SleV2QoS4DscpMapIngressControlColor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 2, 9),
    _SleV2QoS4DscpMapIngressControlColor_Type()
)
sleV2QoS4DscpMapIngressControlColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressControlColor.setStatus("current")
_SleV2QoS4DscpMapIngressNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4DscpMapIngressNotification = _SleV2QoS4DscpMapIngressNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 3)
)
_SleV2QoS4DscpMapTunnel_ObjectIdentity = ObjectIdentity
sleV2QoS4DscpMapTunnel = _SleV2QoS4DscpMapTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2)
)
_SleV2QoS4DscpMapTunnelTable_Object = MibTable
sleV2QoS4DscpMapTunnelTable = _SleV2QoS4DscpMapTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelTable.setStatus("current")
_SleV2QoS4DscpMapTunnelEntry_Object = MibTableRow
sleV2QoS4DscpMapTunnelEntry = _SleV2QoS4DscpMapTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 1, 1)
)
sleV2QoS4DscpMapTunnelEntry.setIndexNames(
    (0, "SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelPriority"),
    (0, "SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelColor"),
)
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelEntry.setStatus("current")


class _SleV2QoS4DscpMapTunnelPriority_Type(Integer32):
    """Custom type sleV2QoS4DscpMapTunnelPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2QoS4DscpMapTunnelPriority_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapTunnelPriority_Object = MibTableColumn
sleV2QoS4DscpMapTunnelPriority = _SleV2QoS4DscpMapTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 1, 1, 1),
    _SleV2QoS4DscpMapTunnelPriority_Type()
)
sleV2QoS4DscpMapTunnelPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelPriority.setStatus("current")


class _SleV2QoS4DscpMapTunnelColor_Type(Integer32):
    """Custom type sleV2QoS4DscpMapTunnelColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_SleV2QoS4DscpMapTunnelColor_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapTunnelColor_Object = MibTableColumn
sleV2QoS4DscpMapTunnelColor = _SleV2QoS4DscpMapTunnelColor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 1, 1, 2),
    _SleV2QoS4DscpMapTunnelColor_Type()
)
sleV2QoS4DscpMapTunnelColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelColor.setStatus("current")


class _SleV2QoS4DscpMapTunnelDscp_Type(Integer32):
    """Custom type sleV2QoS4DscpMapTunnelDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleV2QoS4DscpMapTunnelDscp_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapTunnelDscp_Object = MibTableColumn
sleV2QoS4DscpMapTunnelDscp = _SleV2QoS4DscpMapTunnelDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 1, 1, 3),
    _SleV2QoS4DscpMapTunnelDscp_Type()
)
sleV2QoS4DscpMapTunnelDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelDscp.setStatus("current")
_SleV2QoS4DscpMapTunnelControl_ObjectIdentity = ObjectIdentity
sleV2QoS4DscpMapTunnelControl = _SleV2QoS4DscpMapTunnelControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2)
)


class _SleV2QoS4DscpMapTunnelControlRequest_Type(Integer32):
    """Custom type sleV2QoS4DscpMapTunnelControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDscpMapTunnel", 1)
    )


_SleV2QoS4DscpMapTunnelControlRequest_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapTunnelControlRequest_Object = MibScalar
sleV2QoS4DscpMapTunnelControlRequest = _SleV2QoS4DscpMapTunnelControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 1),
    _SleV2QoS4DscpMapTunnelControlRequest_Type()
)
sleV2QoS4DscpMapTunnelControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlRequest.setStatus("current")
_SleV2QoS4DscpMapTunnelControlStatus_Type = SleControlStatusType
_SleV2QoS4DscpMapTunnelControlStatus_Object = MibScalar
sleV2QoS4DscpMapTunnelControlStatus = _SleV2QoS4DscpMapTunnelControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 2),
    _SleV2QoS4DscpMapTunnelControlStatus_Type()
)
sleV2QoS4DscpMapTunnelControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlStatus.setStatus("current")
_SleV2QoS4DscpMapTunnelControlTimer_Type = Gauge32
_SleV2QoS4DscpMapTunnelControlTimer_Object = MibScalar
sleV2QoS4DscpMapTunnelControlTimer = _SleV2QoS4DscpMapTunnelControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 3),
    _SleV2QoS4DscpMapTunnelControlTimer_Type()
)
sleV2QoS4DscpMapTunnelControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlTimer.setStatus("current")
_SleV2QoS4DscpMapTunnelControlTimeStamp_Type = TimeTicks
_SleV2QoS4DscpMapTunnelControlTimeStamp_Object = MibScalar
sleV2QoS4DscpMapTunnelControlTimeStamp = _SleV2QoS4DscpMapTunnelControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 4),
    _SleV2QoS4DscpMapTunnelControlTimeStamp_Type()
)
sleV2QoS4DscpMapTunnelControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlTimeStamp.setStatus("current")
_SleV2QoS4DscpMapTunnelControlReqResult_Type = SleControlRequestResultType
_SleV2QoS4DscpMapTunnelControlReqResult_Object = MibScalar
sleV2QoS4DscpMapTunnelControlReqResult = _SleV2QoS4DscpMapTunnelControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 5),
    _SleV2QoS4DscpMapTunnelControlReqResult_Type()
)
sleV2QoS4DscpMapTunnelControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlReqResult.setStatus("current")


class _SleV2QoS4DscpMapTunnelControlPriority_Type(Integer32):
    """Custom type sleV2QoS4DscpMapTunnelControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2QoS4DscpMapTunnelControlPriority_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapTunnelControlPriority_Object = MibScalar
sleV2QoS4DscpMapTunnelControlPriority = _SleV2QoS4DscpMapTunnelControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 6),
    _SleV2QoS4DscpMapTunnelControlPriority_Type()
)
sleV2QoS4DscpMapTunnelControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlPriority.setStatus("current")


class _SleV2QoS4DscpMapTunnelControlColor_Type(Integer32):
    """Custom type sleV2QoS4DscpMapTunnelControlColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_SleV2QoS4DscpMapTunnelControlColor_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapTunnelControlColor_Object = MibScalar
sleV2QoS4DscpMapTunnelControlColor = _SleV2QoS4DscpMapTunnelControlColor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 7),
    _SleV2QoS4DscpMapTunnelControlColor_Type()
)
sleV2QoS4DscpMapTunnelControlColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlColor.setStatus("current")


class _SleV2QoS4DscpMapTunnelControlDscp_Type(Integer32):
    """Custom type sleV2QoS4DscpMapTunnelControlDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleV2QoS4DscpMapTunnelControlDscp_Type.__name__ = "Integer32"
_SleV2QoS4DscpMapTunnelControlDscp_Object = MibScalar
sleV2QoS4DscpMapTunnelControlDscp = _SleV2QoS4DscpMapTunnelControlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 2, 8),
    _SleV2QoS4DscpMapTunnelControlDscp_Type()
)
sleV2QoS4DscpMapTunnelControlDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelControlDscp.setStatus("current")
_SleV2QoS4DscpMapTunnelNotification_ObjectIdentity = ObjectIdentity
sleV2QoS4DscpMapTunnelNotification = _SleV2QoS4DscpMapTunnelNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 3)
)
_SleV2QoS6_ObjectIdentity = ObjectIdentity
sleV2QoS6 = _SleV2QoS6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 3)
)

# Managed Objects groups

sleV2QoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 4)
)
sleV2QoSGroup.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowEthernetType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4Flow8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowPktLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowProtocolType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpCode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowCnt"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRateLimit"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorAwareMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorCIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorCBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorPIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorPBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorEBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerCounterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIngressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchRedirectVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchMarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchQueue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchIpPrecedence"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDstMacOrEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDstMac"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchIpPrecedence"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowCnt"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyClassCnt"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyPolicerIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ColorIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2QueueCoSIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2Queue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2Dp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2CoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2Dscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ColorIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3DSCPIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3Queue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3Dp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3CoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3Dscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMeterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterRedBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterYellowBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterGreenBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterValue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlFlowIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassPolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassPolicyID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassPolicyName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowPolicyName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowPolicyID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowPolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowClassName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowClassID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowClassIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp1MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp1MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp1Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp2MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp2MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp2Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileWeight"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp0Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp0MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp0MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileQueueId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoEnable"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoProfileId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoScheduleMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoDWRRGroup"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoMinBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoMaxBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoWeight"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueMappedCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrlen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyRedirBlackhole"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrError"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerAvrgCounterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyAvrg5SecCounterValue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyAvrg1minCounterValue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyAvrg10minCounterValue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMaxBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMinBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInner8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlEthernetType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControl8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIpPktPriorityType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIpPktPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlProtocolType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIcmpType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIcmpCode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlHdrlen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlHdrError"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlInner8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlClassIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlFlowID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlMeterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlRateLimit"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorAwareMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorCIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorCBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorPIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorPBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorEBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorRedAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorYellowAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorGreenAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlRemarkLayerMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlRemarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlCounterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlAvrgCounterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlMinBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlMaxBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorRedDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorYellowDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorGreenDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlPolicerIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIngressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchRedirectVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchMarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchQueue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchDp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchIpPrecedence"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchDstMacOrEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchDstMac"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlNomatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlNomatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlNomatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlNomatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlNomatchIpPrecedence"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchRedirBlackhole"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlPolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlFlowID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlClassID"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkLayer2Mode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlTimStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlLayer2Mode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlColorIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlDSCPIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlQueue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlDp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlColorIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlQueueCoSIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlQueue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlDp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlQueueId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp0MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp0MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp0Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp1MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp1MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp1Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp2MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp2MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlDp2Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlWeight"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlEnable"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlProfileId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlScheduleMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlDWRRGroup"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlMinBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlMaxBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlWeight"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlMappedCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIngressTunnelIfIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyEgressTunnelIfIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIngressTunnelIfIndex"),
        ("SLEV2-QOS-MIB", "sleV2Qo4SPolicyControlEgressTunnelIfIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressDscpIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressColor"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlDscpIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlColor"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelColor"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlColor"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseFlowMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlFlowMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterElapsedTimeAfterClear"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMatchCounterName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMatchCounterDesc"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMatchCounterValue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlMacFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorRedCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorYellowCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorGreenCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedCosType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowCosType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorRedCosType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorYellowCosType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlColorGreenCosType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacDlf"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlMacDlf"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyStage"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlStage"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIngressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyEgressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIngressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlEgressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyInnerVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyOuterVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlInnerVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlOuterVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFDirection"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlStatus"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlTimer"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlIfindex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlPolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlDirection"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHopSecondary"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHopVerifyReach"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchPbrNextHopSecondary"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchPbrNextHopVerifyReach"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTagType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTagType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInPktTagVid"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInPktTagCfi"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInPktTagCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOutPktTagVid"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOutPktTagCfi"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOutPktTagCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowFlowAlias"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagVid"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagCfi"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlFlowAlias"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchFlowAlias"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchFlowAlias"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchInnerVlanCosReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchInnerVlanCfiReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchOuterVlanCosReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchOuterVlanCfiReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchInnerVlanCosReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchInnerVlanCfiReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchOuterVlanCosReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchOuterVlanCfiReplace"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowClassName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlClassName"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowInetAddrType"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowSrcInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowDstInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowSrcInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowDstInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowTrafficClass"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowFlowLabel"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowControlInetAddrType"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowControlSrcInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowControlDstInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowControlSrcInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowControlDstInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowControlTrafficClass"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowControlFlowLabel"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuter8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOnuCircuitId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlOuter8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlOnuCircuitId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMinLimitUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriorityType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRemarkLayerMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRemarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenCosType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHop"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchPbrNextHop"))
)
if mibBuilder.loadTexts:
    sleV2QoSGroup.setStatus("current")


# Notification objects

sleV2QoS4BaseFlowModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 1, 3, 1)
)
sleV2QoS4BaseFlowModeChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4BaseControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlFlowMode"))
)
if mibBuilder.loadTexts:
    sleV2QoS4BaseFlowModeChanged.setStatus(
        "current"
    )

sleFlowCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 1)
)
sleFlowCreated.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrError"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInner8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacDlf"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTagType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuter8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOnuCircuitId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowEthernetType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4Flow8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriorityType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowPktLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowProtocolType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpCode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrlen"))
)
if mibBuilder.loadTexts:
    sleFlowCreated.setStatus(
        "current"
    )

sleFlowChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 2)
)
sleFlowChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlFlowMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlEthernetType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControl8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlSrcIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlDstIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIpPktPriorityType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIpPktPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlProtocolType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTcpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlUdpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIcmpType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIcmpCode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlHdrlen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlHdrError"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlInner8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlMacFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTagType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlOuter8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlOnuCircuitId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlMacDlf"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFlowChanged.setStatus(
        "current"
    )

sleFlowDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 3)
)
sleFlowDestroyed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIndex"))
)
if mibBuilder.loadTexts:
    sleFlowDestroyed.setStatus(
        "current"
    )

sleFlowAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 4)
)
sleFlowAllDestroyed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFlowAllDestroyed.setStatus(
        "current"
    )

sleFlowInPktTagChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 5)
)
sleFlowInPktTagChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagVid"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagCfi"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagCoS"))
)
if mibBuilder.loadTexts:
    sleFlowInPktTagChanged.setStatus(
        "current"
    )

sleFlowOutPktTagChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 6)
)
sleFlowOutPktTagChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagVid"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagCfi"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlPktTagCoS"))
)
if mibBuilder.loadTexts:
    sleFlowOutPktTagChanged.setStatus(
        "current"
    )

sleFlowAliasChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 7)
)
sleFlowAliasChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlFlowAlias"))
)
if mibBuilder.loadTexts:
    sleFlowAliasChanged.setStatus(
        "current"
    )

sleFlowExCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 8)
)
sleFlowExCreated.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowEthernetType"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowInetAddrType"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowSrcInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowDstInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowSrcInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowDstInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4Flow8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstIpAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstIpAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriorityType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowPktLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowProtocolType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpCode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrlen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrError"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInner8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacDlf"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTagType"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowTrafficClass"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowFlowLabel"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuter8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOnuCircuitId"))
)
if mibBuilder.loadTexts:
    sleFlowExCreated.setStatus(
        "current"
    )

sleFlowExChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 2, 1, 3, 9)
)
sleFlowExChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4FlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseControlFlowMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowEthernetType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowSrcMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstMacAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowDstMacAddrMask"),
        ("SLEV2-QOS-MIB", "sleV2QoS4Flow8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowInetAddrType"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowSrcInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowDstInetAddr"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowSrcInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowDstInetAddrLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriorityType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpPktPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowPktLen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowProtocolType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTcpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpSrcEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstStartPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowUdpDstEndPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIcmpCode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrlen"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowHdrError"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowInner8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowIpFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowTagType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowMacDlf"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOuter8021p"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowOnuCircuitId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4FlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowTrafficClass"),
        ("SLEV2-QOS-MIB", "sleV2QoSFlowFlowLabel"))
)
if mibBuilder.loadTexts:
    sleFlowExChanged.setStatus(
        "current"
    )

sleClassCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 3, 1)
)
sleClassCreated.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4ClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlReqResult"))
)
if mibBuilder.loadTexts:
    sleClassCreated.setStatus(
        "current"
    )

sleClassDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 3, 2)
)
sleClassDestroyed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4ClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlIndex"))
)
if mibBuilder.loadTexts:
    sleClassDestroyed.setStatus(
        "current"
    )

sleClassAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 1, 3, 3)
)
sleClassAllDestroyed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4ClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassControlReqResult"))
)
if mibBuilder.loadTexts:
    sleClassAllDestroyed.setStatus(
        "current"
    )

sleClassFlowAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 3, 1)
)
sleClassFlowAdded.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlClassName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowID"))
)
if mibBuilder.loadTexts:
    sleClassFlowAdded.setStatus(
        "current"
    )

sleClassFlowDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 3, 2)
)
sleClassFlowDeleted.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlClassIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlFlowIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlClassName"))
)
if mibBuilder.loadTexts:
    sleClassFlowDeleted.setStatus(
        "current"
    )

sleClassFlowAllDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 3, 2, 3, 3)
)
sleClassFlowAllDeleted.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4ClassFlowControlClassIndex"))
)
if mibBuilder.loadTexts:
    sleClassFlowAllDeleted.setStatus(
        "current"
    )

slePolicerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 3, 1)
)
slePolicerCreated.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMaxBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMinBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerAvrgCounterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMeterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRateLimit"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorAwareMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorCIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorCBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorPIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorPBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorEBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRemarkLayerMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRemarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerCounterMode"))
)
if mibBuilder.loadTexts:
    slePolicerCreated.setStatus(
        "current"
    )

slePolicerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 3, 2)
)
slePolicerChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerAvrgCounterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMeterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRateLimit"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorAwareMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorCIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorCBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorPIR"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorPBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorEBS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRemarkLayerMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerRemarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerCounterMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMinBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerMaxBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorRedDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorYellowDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerColorGreenDscp"))
)
if mibBuilder.loadTexts:
    slePolicerChanged.setStatus(
        "current"
    )

slePolicerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 4, 1, 3, 3)
)
slePolicerDestroyed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicerControlIndex"))
)
if mibBuilder.loadTexts:
    slePolicerDestroyed.setStatus(
        "current"
    )

slePolicyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 1)
)
slePolicyCreated.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyRedirBlackhole"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHop"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyStage"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIngressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyEgressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyInnerVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyOuterVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyName"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowCnt"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyClassCnt"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyPolicerIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIngressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchRedirectVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchMarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchQueue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchIpPrecedence"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDstMacOrEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDstMac"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchIpPrecedence"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterValue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterGreenBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterYellowBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterRedBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHopSecondary"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHopVerifyReach"))
)
if mibBuilder.loadTexts:
    slePolicyCreated.setStatus(
        "current"
    )

slePolicyInfoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 2)
)
slePolicyInfoChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyStage"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyPolicerIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIngressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIngressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyEgressPortsFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyPriority"))
)
if mibBuilder.loadTexts:
    slePolicyInfoChanged.setStatus(
        "current"
    )

slePolicyMatchActionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 3)
)
slePolicyMatchActionChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyRedirBlackhole"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyInnerVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyOuterVlanAction"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyInnerVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyOuterVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchRedirectVlan"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchMarkMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchQueue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchIpPrecedence"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDstMacOrEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchDstMac"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchEgressPorts"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHop"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHopSecondary"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyMatchPbrNextHopVerifyReach"))
)
if mibBuilder.loadTexts:
    slePolicyMatchActionChanged.setStatus(
        "current"
    )

slePolicyNomatchActionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 4)
)
slePolicyNomatchActionChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchFlag"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchRedirectPort"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchCoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyNomatchIpPrecedence"))
)
if mibBuilder.loadTexts:
    slePolicyNomatchActionChanged.setStatus(
        "current"
    )

slePolicyDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 5)
)
slePolicyDestroyed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"))
)
if mibBuilder.loadTexts:
    slePolicyDestroyed.setStatus(
        "current"
    )

slePolicyCounterCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 6)
)
slePolicyCounterCleared.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterValue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterGreenBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterYellowBytes"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyCounterRedBytes"))
)
if mibBuilder.loadTexts:
    slePolicyCounterCleared.setStatus(
        "current"
    )

slePolicyEmptyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 7)
)
slePolicyEmptyCreated.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyName"))
)
if mibBuilder.loadTexts:
    slePolicyEmptyCreated.setStatus(
        "current"
    )

slePolicyIngressTunnelSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 8)
)
slePolicyIngressTunnelSet.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIngressTunnelIfIndex"))
)
if mibBuilder.loadTexts:
    slePolicyIngressTunnelSet.setStatus(
        "current"
    )

slePolicyIngressTunnelUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 9)
)
slePolicyIngressTunnelUnset.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIngressTunnelIfIndex"))
)
if mibBuilder.loadTexts:
    slePolicyIngressTunnelUnset.setStatus(
        "current"
    )

slePolicyEgressTunnelSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 10)
)
slePolicyEgressTunnelSet.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2Qo4SPolicyControlEgressTunnelIfIndex"))
)
if mibBuilder.loadTexts:
    slePolicyEgressTunnelSet.setStatus(
        "current"
    )

slePolicyEgressTunnelUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 11)
)
slePolicyEgressTunnelUnset.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2Qo4SPolicyControlEgressTunnelIfIndex"))
)
if mibBuilder.loadTexts:
    slePolicyEgressTunnelUnset.setStatus(
        "current"
    )

slePolicyActionMatchFlowAliasChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 12)
)
slePolicyActionMatchFlowAliasChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchFlowAlias"))
)
if mibBuilder.loadTexts:
    slePolicyActionMatchFlowAliasChanged.setStatus(
        "current"
    )

slePolicyMatchInnerVlanCosReplaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 13)
)
slePolicyMatchInnerVlanCosReplaceChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchInnerVlanCosReplace"))
)
if mibBuilder.loadTexts:
    slePolicyMatchInnerVlanCosReplaceChanged.setStatus(
        "current"
    )

slePolicyMatchInnerVlanCfiReplaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 14)
)
slePolicyMatchInnerVlanCfiReplaceChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchInnerVlanCfiReplace"))
)
if mibBuilder.loadTexts:
    slePolicyMatchInnerVlanCfiReplaceChanged.setStatus(
        "current"
    )

slePolicyMatchOuterVlanCosReplaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 15)
)
slePolicyMatchOuterVlanCosReplaceChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchOuterVlanCosReplace"))
)
if mibBuilder.loadTexts:
    slePolicyMatchOuterVlanCosReplaceChanged.setStatus(
        "current"
    )

slePolicyMatchOuterVlanCfiReplaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 1, 3, 16)
)
slePolicyMatchOuterVlanCfiReplaceChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyControlMatchOuterVlanCfiReplace"))
)
if mibBuilder.loadTexts:
    slePolicyMatchOuterVlanCfiReplaceChanged.setStatus(
        "current"
    )

slePolicyFlowAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 3, 1)
)
slePolicyFlowAdded.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassType"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassID"))
)
if mibBuilder.loadTexts:
    slePolicyFlowAdded.setStatus(
        "current"
    )

slePolicyFlowDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 3, 2)
)
slePolicyFlowDeleted.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlPolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlIndex"))
)
if mibBuilder.loadTexts:
    slePolicyFlowDeleted.setStatus(
        "current"
    )

slePolicyAllFlowDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 3, 3)
)
slePolicyAllFlowDeleted.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlPolicyIndex"))
)
if mibBuilder.loadTexts:
    slePolicyAllFlowDeleted.setStatus(
        "current"
    )

slePolicyAllClassDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 3, 4)
)
slePolicyAllClassDeleted.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlPolicyIndex"))
)
if mibBuilder.loadTexts:
    slePolicyAllClassDeleted.setStatus(
        "current"
    )

slePolicyAllFlowClassDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 2, 3, 5)
)
slePolicyAllFlowClassDeleted.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyFlowClassControlPolicyIndex"))
)
if mibBuilder.loadTexts:
    slePolicyAllFlowClassDeleted.setStatus(
        "current"
    )

sleV2QosPolicyIFServicePolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 3, 1)
)
sleV2QosPolicyIFServicePolicyChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlIfindex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlPolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlDirection"))
)
if mibBuilder.loadTexts:
    sleV2QosPolicyIFServicePolicyChanged.setStatus(
        "current"
    )

sleV2QosPolicyIFServicePolicyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 5, 3, 3, 2)
)
sleV2QosPolicyIFServicePolicyCleared.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlIfindex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlPolicyIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PolicyIFControlDirection"))
)
if mibBuilder.loadTexts:
    sleV2QosPolicyIFServicePolicyCleared.setStatus(
        "current"
    )

sleRemarkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 1, 3, 1)
)
sleRemarkChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlTimStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkLayer2Mode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkMode"))
)
if mibBuilder.loadTexts:
    sleRemarkChanged.setStatus(
        "current"
    )

sleRemarkL3Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 2, 3, 1)
)
sleRemarkL3Changed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3ControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3Queue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3Dp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3CoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL3Dscp"))
)
if mibBuilder.loadTexts:
    sleRemarkL3Changed.setStatus(
        "current"
    )

sleRemarkL2Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 6, 3, 3, 1)
)
sleRemarkL2Changed.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2ControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2Queue"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2Dp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2CoS"),
        ("SLEV2-QOS-MIB", "sleV2QoS4RemarkL2Dscp"))
)
if mibBuilder.loadTexts:
    sleRemarkL2Changed.setStatus(
        "current"
    )

sleV2QS4REDProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 3, 1)
)
sleV2QS4REDProfileChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp0MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp0MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp0Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp1MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp1MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp1Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp2MinThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp2MaxThres"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileDp2Prob"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileWeight"))
)
if mibBuilder.loadTexts:
    sleV2QS4REDProfileChanged.setStatus(
        "current"
    )

sleV2QS4REDProfileCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 1, 3, 2)
)
sleV2QS4REDProfileCleared.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4REDProfileControlId"))
)
if mibBuilder.loadTexts:
    sleV2QS4REDProfileCleared.setStatus(
        "current"
    )

sleV2QoS4PortREDInfoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 7, 2, 3, 1)
)
sleV2QoS4PortREDInfoChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoEnable"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoProfileId"))
)
if mibBuilder.loadTexts:
    sleV2QoS4PortREDInfoChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 1)
)
sleV2QoS4QueueInfoChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoScheduleMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoDWRRGroup"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoMinBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoMaxBandwidth"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoWeight"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueMappedCoS"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoScheduleModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 2)
)
sleV2QoS4QueueInfoScheduleModeChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoScheduleMode"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoDWRRGroup"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoScheduleModeChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoMaxBandwidthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 3)
)
sleV2QoS4QueueInfoMaxBandwidthChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlMaxBandwidth"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoMaxBandwidthChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoMinBandwidthChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 4)
)
sleV2QoS4QueueInfoMinBandwidthChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlMinBandwidth"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoMinBandwidthChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoWeightChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 5)
)
sleV2QoS4QueueInfoWeightChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoWeight"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoWeightChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMinLimitUnicastChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 6)
)
sleV2QoS4QueueInfoBufferEgressMinLimitUnicastChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMinLimitUnicastChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMinLimitUnicastCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 7)
)
sleV2QoS4QueueInfoBufferEgressMinLimitUnicastCleared.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMinLimitUnicastCleared.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 8)
)
sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 9)
)
sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastCleared.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastCleared.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 10)
)
sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 11)
)
sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastCleared.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastCleared.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 12)
)
sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastChanged.setStatus(
        "current"
    )

sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 8, 1, 3, 13)
)
sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastCleared.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlInterfaceIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoControlId"))
)
if mibBuilder.loadTexts:
    sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastCleared.setStatus(
        "current"
    )

sleV2QoS4DscpMapIngressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 1, 3, 1)
)
sleV2QoS4DscpMapIngressChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlDscpIndex"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlDscp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlCos"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressControlColor"))
)
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapIngressChanged.setStatus(
        "current"
    )

sleV2QoS4DscpMapTunnelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 2, 9, 2, 3, 1)
)
sleV2QoS4DscpMapTunnelChanged.setObjects(
      *(("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlRequest"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlTimeStamp"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlReqResult"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlPriority"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlColor"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelControlDscp"))
)
if mibBuilder.loadTexts:
    sleV2QoS4DscpMapTunnelChanged.setStatus(
        "current"
    )


# Notifications groups

sleV2QoSNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 10, 5)
)
sleV2QoSNotificationGroup.setObjects(
      *(("SLEV2-QOS-MIB", "sleFlowCreated"),
        ("SLEV2-QOS-MIB", "sleFlowChanged"),
        ("SLEV2-QOS-MIB", "sleFlowDestroyed"),
        ("SLEV2-QOS-MIB", "sleFlowAllDestroyed"),
        ("SLEV2-QOS-MIB", "sleClassCreated"),
        ("SLEV2-QOS-MIB", "sleClassDestroyed"),
        ("SLEV2-QOS-MIB", "sleClassAllDestroyed"),
        ("SLEV2-QOS-MIB", "sleClassFlowAdded"),
        ("SLEV2-QOS-MIB", "sleClassFlowDeleted"),
        ("SLEV2-QOS-MIB", "sleClassFlowAllDeleted"),
        ("SLEV2-QOS-MIB", "slePolicerCreated"),
        ("SLEV2-QOS-MIB", "slePolicerChanged"),
        ("SLEV2-QOS-MIB", "slePolicerDestroyed"),
        ("SLEV2-QOS-MIB", "slePolicyCreated"),
        ("SLEV2-QOS-MIB", "slePolicyDestroyed"),
        ("SLEV2-QOS-MIB", "sleRemarkChanged"),
        ("SLEV2-QOS-MIB", "sleRemarkL3Changed"),
        ("SLEV2-QOS-MIB", "sleV2QS4REDProfileChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4PortREDInfoChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoChanged"),
        ("SLEV2-QOS-MIB", "sleV2QS4REDProfileCleared"),
        ("SLEV2-QOS-MIB", "slePolicyEmptyCreated"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapIngressChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4DscpMapTunnelChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4BaseFlowModeChanged"),
        ("SLEV2-QOS-MIB", "sleRemarkL2Changed"),
        ("SLEV2-QOS-MIB", "slePolicyInfoChanged"),
        ("SLEV2-QOS-MIB", "slePolicyMatchActionChanged"),
        ("SLEV2-QOS-MIB", "slePolicyNomatchActionChanged"),
        ("SLEV2-QOS-MIB", "slePolicyCounterCleared"),
        ("SLEV2-QOS-MIB", "slePolicyFlowAdded"),
        ("SLEV2-QOS-MIB", "slePolicyFlowDeleted"),
        ("SLEV2-QOS-MIB", "slePolicyAllFlowDeleted"),
        ("SLEV2-QOS-MIB", "slePolicyAllClassDeleted"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoScheduleModeChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoWeightChanged"),
        ("SLEV2-QOS-MIB", "sleV2QosPolicyIFServicePolicyChanged"),
        ("SLEV2-QOS-MIB", "sleV2QosPolicyIFServicePolicyCleared"),
        ("SLEV2-QOS-MIB", "slePolicyAllFlowClassDeleted"),
        ("SLEV2-QOS-MIB", "slePolicyIngressTunnelSet"),
        ("SLEV2-QOS-MIB", "slePolicyIngressTunnelUnset"),
        ("SLEV2-QOS-MIB", "slePolicyEgressTunnelSet"),
        ("SLEV2-QOS-MIB", "slePolicyEgressTunnelUnset"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoMaxBandwidthChanged"),
        ("SLEV2-QOS-MIB", "slePolicyMatchInnerVlanCosReplaceChanged"),
        ("SLEV2-QOS-MIB", "slePolicyMatchInnerVlanCfiReplaceChanged"),
        ("SLEV2-QOS-MIB", "slePolicyMatchOuterVlanCosReplaceChanged"),
        ("SLEV2-QOS-MIB", "slePolicyMatchOuterVlanCfiReplaceChanged"),
        ("SLEV2-QOS-MIB", "sleFlowExCreated"),
        ("SLEV2-QOS-MIB", "sleFlowExChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMinLimitUnicastChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMinLimitUnicastCleared"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastCleared"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastCleared"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastChanged"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastCleared"),
        ("SLEV2-QOS-MIB", "sleV2QoS4QueueInfoMinBandwidthChanged"),
        ("SLEV2-QOS-MIB", "sleFlowInPktTagChanged"),
        ("SLEV2-QOS-MIB", "sleFlowOutPktTagChanged"),
        ("SLEV2-QOS-MIB", "sleFlowAliasChanged"),
        ("SLEV2-QOS-MIB", "slePolicyActionMatchFlowAliasChanged"))
)
if mibBuilder.loadTexts:
    sleV2QoSNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLEV2-QOS-MIB",
    **{"IntFlowIndex": IntFlowIndex,
       "IntClassIndex": IntClassIndex,
       "IntPolicerIndex": IntPolicerIndex,
       "IntPolicyIndex": IntPolicyIndex,
       "OctetName": OctetName,
       "IntEthernetType": IntEthernetType,
       "Int8021p": Int8021p,
       "IntIpAddrMask": IntIpAddrMask,
       "IntToS": IntToS,
       "IntPktLen": IntPktLen,
       "IntProtocolType": IntProtocolType,
       "IntL4Port": IntL4Port,
       "IntIcmpType": IntIcmpType,
       "IntIcmpCode": IntIcmpCode,
       "IntInternetProtocolFlag": IntInternetProtocolFlag,
       "IntRulePriority": IntRulePriority,
       "IntFlowClass": IntFlowClass,
       "IntVlanID": IntVlanID,
       "IntQueue": IntQueue,
       "IntDP": IntDP,
       "IntCoS": IntCoS,
       "IntDscp": IntDscp,
       "IntIpPrecedence": IntIpPrecedence,
       "IntDstMacOrEgressPorts": IntDstMacOrEgressPorts,
       "IntMarkMode": IntMarkMode,
       "IntMeterMode": IntMeterMode,
       "IntColorType": IntColorType,
       "IntColorMode": IntColorMode,
       "IntColorAwareMode": IntColorAwareMode,
       "IntColorCIR": IntColorCIR,
       "IntColorCBS": IntColorCBS,
       "IntColorPIR": IntColorPIR,
       "IntColorPBS": IntColorPBS,
       "IntColorEBS": IntColorEBS,
       "IntColorAction": IntColorAction,
       "IntCounterMode": IntCounterMode,
       "IntInterfaceIndex": IntInterfaceIndex,
       "IntFlowOrClass": IntFlowOrClass,
       "IntL2BaseRemarkMode": IntL2BaseRemarkMode,
       "IntColorIndex": IntColorIndex,
       "IntDSCPIndex": IntDSCPIndex,
       "IntQueueCoSIndex": IntQueueCoSIndex,
       "IntIpPktPriorityType": IntIpPktPriorityType,
       "IntEnableFlag": IntEnableFlag,
       "IntAvrgCounterMode": IntAvrgCounterMode,
       "MacAddressMask": MacAddressMask,
       "sleV2QoS": sleV2QoS,
       "sleV2QoSBase": sleV2QoSBase,
       "sleV2QoS4": sleV2QoS4,
       "sleV2QoS4Base": sleV2QoS4Base,
       "sleV2QoS4BaseInfo": sleV2QoS4BaseInfo,
       "sleV2QoS4BaseFlowMode": sleV2QoS4BaseFlowMode,
       "sleV2QoS4BaseControl": sleV2QoS4BaseControl,
       "sleV2QoS4BaseControlRequest": sleV2QoS4BaseControlRequest,
       "sleV2QoS4BaseControlStatus": sleV2QoS4BaseControlStatus,
       "sleV2QoS4BaseControlTimer": sleV2QoS4BaseControlTimer,
       "sleV2QoS4BaseControlTimeStamp": sleV2QoS4BaseControlTimeStamp,
       "sleV2QoS4BaseControlResult": sleV2QoS4BaseControlResult,
       "sleV2QoS4BaseControlFlowMode": sleV2QoS4BaseControlFlowMode,
       "sleV2QoS4BaseNotification": sleV2QoS4BaseNotification,
       "sleV2QoS4BaseFlowModeChanged": sleV2QoS4BaseFlowModeChanged,
       "sleV2QoS4Flow": sleV2QoS4Flow,
       "sleV2QoS4FlowInfo": sleV2QoS4FlowInfo,
       "sleV2QoS4FlowTable": sleV2QoS4FlowTable,
       "sleV2QoS4FlowEntry": sleV2QoS4FlowEntry,
       "sleV2QoS4FlowIndex": sleV2QoS4FlowIndex,
       "sleV2QoS4FlowName": sleV2QoS4FlowName,
       "sleV2QoS4FlowEthernetType": sleV2QoS4FlowEthernetType,
       "sleV2QoS4FlowSrcMacAddr": sleV2QoS4FlowSrcMacAddr,
       "sleV2QoS4FlowSrcMacAddrMask": sleV2QoS4FlowSrcMacAddrMask,
       "sleV2QoS4FlowDstMacAddr": sleV2QoS4FlowDstMacAddr,
       "sleV2QoS4FlowDstMacAddrMask": sleV2QoS4FlowDstMacAddrMask,
       "sleV2QoS4Flow8021p": sleV2QoS4Flow8021p,
       "sleV2QoS4FlowSrcIpAddr": sleV2QoS4FlowSrcIpAddr,
       "sleV2QoS4FlowSrcIpAddrMask": sleV2QoS4FlowSrcIpAddrMask,
       "sleV2QoS4FlowDstIpAddr": sleV2QoS4FlowDstIpAddr,
       "sleV2QoS4FlowDstIpAddrMask": sleV2QoS4FlowDstIpAddrMask,
       "sleV2QoS4FlowIpPktPriorityType": sleV2QoS4FlowIpPktPriorityType,
       "sleV2QoS4FlowIpPktPriority": sleV2QoS4FlowIpPktPriority,
       "sleV2QoS4FlowPktLen": sleV2QoS4FlowPktLen,
       "sleV2QoS4FlowProtocolType": sleV2QoS4FlowProtocolType,
       "sleV2QoS4FlowTcpSrcStartPort": sleV2QoS4FlowTcpSrcStartPort,
       "sleV2QoS4FlowTcpSrcEndPort": sleV2QoS4FlowTcpSrcEndPort,
       "sleV2QoS4FlowTcpDstStartPort": sleV2QoS4FlowTcpDstStartPort,
       "sleV2QoS4FlowTcpDstEndPort": sleV2QoS4FlowTcpDstEndPort,
       "sleV2QoS4FlowTcpFlag": sleV2QoS4FlowTcpFlag,
       "sleV2QoS4FlowUdpSrcStartPort": sleV2QoS4FlowUdpSrcStartPort,
       "sleV2QoS4FlowUdpSrcEndPort": sleV2QoS4FlowUdpSrcEndPort,
       "sleV2QoS4FlowUdpDstStartPort": sleV2QoS4FlowUdpDstStartPort,
       "sleV2QoS4FlowUdpDstEndPort": sleV2QoS4FlowUdpDstEndPort,
       "sleV2QoS4FlowIcmpType": sleV2QoS4FlowIcmpType,
       "sleV2QoS4FlowIcmpCode": sleV2QoS4FlowIcmpCode,
       "sleV2QoS4FlowHdrlen": sleV2QoS4FlowHdrlen,
       "sleV2QoS4FlowHdrError": sleV2QoS4FlowHdrError,
       "sleV2QoS4FlowInnerVlan": sleV2QoS4FlowInnerVlan,
       "sleV2QoS4FlowInner8021p": sleV2QoS4FlowInner8021p,
       "sleV2QoS4FlowMacFlag": sleV2QoS4FlowMacFlag,
       "sleV2QoS4FlowIpFlag": sleV2QoS4FlowIpFlag,
       "sleV2QoS4FlowMacDlf": sleV2QoS4FlowMacDlf,
       "sleV2QoS4FlowTagType": sleV2QoS4FlowTagType,
       "sleV2QoS4FlowInPktTagVid": sleV2QoS4FlowInPktTagVid,
       "sleV2QoS4FlowInPktTagCfi": sleV2QoS4FlowInPktTagCfi,
       "sleV2QoS4FlowInPktTagCoS": sleV2QoS4FlowInPktTagCoS,
       "sleV2QoS4FlowOutPktTagVid": sleV2QoS4FlowOutPktTagVid,
       "sleV2QoS4FlowOutPktTagCfi": sleV2QoS4FlowOutPktTagCfi,
       "sleV2QoS4FlowOutPktTagCoS": sleV2QoS4FlowOutPktTagCoS,
       "sleV2QoS4FlowFlowAlias": sleV2QoS4FlowFlowAlias,
       "sleV2QoSFlowInetAddrType": sleV2QoSFlowInetAddrType,
       "sleV2QoSFlowSrcInetAddr": sleV2QoSFlowSrcInetAddr,
       "sleV2QoSFlowDstInetAddr": sleV2QoSFlowDstInetAddr,
       "sleV2QoSFlowSrcInetAddrLen": sleV2QoSFlowSrcInetAddrLen,
       "sleV2QoSFlowDstInetAddrLen": sleV2QoSFlowDstInetAddrLen,
       "sleV2QoSFlowTrafficClass": sleV2QoSFlowTrafficClass,
       "sleV2QoSFlowFlowLabel": sleV2QoSFlowFlowLabel,
       "sleV2QoS4FlowOuterVlan": sleV2QoS4FlowOuterVlan,
       "sleV2QoS4FlowOuter8021p": sleV2QoS4FlowOuter8021p,
       "sleV2QoS4FlowOnuCircuitId": sleV2QoS4FlowOnuCircuitId,
       "sleV2QoS4FlowControl": sleV2QoS4FlowControl,
       "sleV2QoS4FlowControlRequest": sleV2QoS4FlowControlRequest,
       "sleV2QoS4FlowControlStatus": sleV2QoS4FlowControlStatus,
       "sleV2QoS4FlowControlTimer": sleV2QoS4FlowControlTimer,
       "sleV2QoS4FlowControlTimeStamp": sleV2QoS4FlowControlTimeStamp,
       "sleV2QoS4FlowControlReqResult": sleV2QoS4FlowControlReqResult,
       "sleV2QoS4FlowControlIndex": sleV2QoS4FlowControlIndex,
       "sleV2QoS4FlowControlName": sleV2QoS4FlowControlName,
       "sleV2QoS4FlowControlEthernetType": sleV2QoS4FlowControlEthernetType,
       "sleV2QoS4FlowControlSrcMacAddr": sleV2QoS4FlowControlSrcMacAddr,
       "sleV2QoS4FlowControlSrcMacAddrMask": sleV2QoS4FlowControlSrcMacAddrMask,
       "sleV2QoS4FlowControlDstMacAddr": sleV2QoS4FlowControlDstMacAddr,
       "sleV2QoS4FlowControlDstMacAddrMask": sleV2QoS4FlowControlDstMacAddrMask,
       "sleV2QoS4FlowControl8021p": sleV2QoS4FlowControl8021p,
       "sleV2QoS4FlowControlSrcIpAddr": sleV2QoS4FlowControlSrcIpAddr,
       "sleV2QoS4FlowControlSrcIpAddrMask": sleV2QoS4FlowControlSrcIpAddrMask,
       "sleV2QoS4FlowControlDstIpAddr": sleV2QoS4FlowControlDstIpAddr,
       "sleV2QoS4FlowControlDstIpAddrMask": sleV2QoS4FlowControlDstIpAddrMask,
       "sleV2QoS4FlowControlIpPktPriorityType": sleV2QoS4FlowControlIpPktPriorityType,
       "sleV2QoS4FlowControlIpPktPriority": sleV2QoS4FlowControlIpPktPriority,
       "sleV2QoS4FlowControlPktLen": sleV2QoS4FlowControlPktLen,
       "sleV2QoS4FlowControlProtocolType": sleV2QoS4FlowControlProtocolType,
       "sleV2QoS4FlowControlTcpSrcStartPort": sleV2QoS4FlowControlTcpSrcStartPort,
       "sleV2QoS4FlowControlTcpSrcEndPort": sleV2QoS4FlowControlTcpSrcEndPort,
       "sleV2QoS4FlowControlTcpDstStartPort": sleV2QoS4FlowControlTcpDstStartPort,
       "sleV2QoS4FlowControlTcpDstEndPort": sleV2QoS4FlowControlTcpDstEndPort,
       "sleV2QoS4FlowControlTcpFlag": sleV2QoS4FlowControlTcpFlag,
       "sleV2QoS4FlowControlUdpSrcStartPort": sleV2QoS4FlowControlUdpSrcStartPort,
       "sleV2QoS4FlowControlUdpSrcEndPort": sleV2QoS4FlowControlUdpSrcEndPort,
       "sleV2QoS4FlowControlUdpDstStartPort": sleV2QoS4FlowControlUdpDstStartPort,
       "sleV2QoS4FlowControlUdpDstEndPort": sleV2QoS4FlowControlUdpDstEndPort,
       "sleV2QoS4FlowControlIcmpType": sleV2QoS4FlowControlIcmpType,
       "sleV2QoS4FlowControlIcmpCode": sleV2QoS4FlowControlIcmpCode,
       "sleV2QoS4FlowControlHdrlen": sleV2QoS4FlowControlHdrlen,
       "sleV2QoS4FlowControlHdrError": sleV2QoS4FlowControlHdrError,
       "sleV2QoS4FlowControlInnerVlan": sleV2QoS4FlowControlInnerVlan,
       "sleV2QoS4FlowControlInner8021p": sleV2QoS4FlowControlInner8021p,
       "sleV2QoS4FlowControlMacFlag": sleV2QoS4FlowControlMacFlag,
       "sleV2QoS4FlowControlIpFlag": sleV2QoS4FlowControlIpFlag,
       "sleV2QoS4FlowControlMacDlf": sleV2QoS4FlowControlMacDlf,
       "sleV2QoS4FlowControlTagType": sleV2QoS4FlowControlTagType,
       "sleV2QoS4FlowControlPktTagVid": sleV2QoS4FlowControlPktTagVid,
       "sleV2QoS4FlowControlPktTagCfi": sleV2QoS4FlowControlPktTagCfi,
       "sleV2QoS4FlowControlPktTagCoS": sleV2QoS4FlowControlPktTagCoS,
       "sleV2QoS4FlowControlFlowAlias": sleV2QoS4FlowControlFlowAlias,
       "sleV2QoSFlowControlInetAddrType": sleV2QoSFlowControlInetAddrType,
       "sleV2QoSFlowControlSrcInetAddr": sleV2QoSFlowControlSrcInetAddr,
       "sleV2QoSFlowControlDstInetAddr": sleV2QoSFlowControlDstInetAddr,
       "sleV2QoSFlowControlSrcInetAddrLen": sleV2QoSFlowControlSrcInetAddrLen,
       "sleV2QoSFlowControlDstInetAddrLen": sleV2QoSFlowControlDstInetAddrLen,
       "sleV2QoSFlowControlTrafficClass": sleV2QoSFlowControlTrafficClass,
       "sleV2QoSFlowControlFlowLabel": sleV2QoSFlowControlFlowLabel,
       "sleV2QoS4FlowControlOuterVlan": sleV2QoS4FlowControlOuterVlan,
       "sleV2QoS4FlowControlOuter8021p": sleV2QoS4FlowControlOuter8021p,
       "sleV2QoS4FlowControlOnuCircuitId": sleV2QoS4FlowControlOnuCircuitId,
       "sleV2QoS4FlowNotification": sleV2QoS4FlowNotification,
       "sleFlowCreated": sleFlowCreated,
       "sleFlowChanged": sleFlowChanged,
       "sleFlowDestroyed": sleFlowDestroyed,
       "sleFlowAllDestroyed": sleFlowAllDestroyed,
       "sleFlowInPktTagChanged": sleFlowInPktTagChanged,
       "sleFlowOutPktTagChanged": sleFlowOutPktTagChanged,
       "sleFlowAliasChanged": sleFlowAliasChanged,
       "sleFlowExCreated": sleFlowExCreated,
       "sleFlowExChanged": sleFlowExChanged,
       "sleV2QoS4FlowClass": sleV2QoS4FlowClass,
       "sleV2QoS4FlowClassTable": sleV2QoS4FlowClassTable,
       "sleV2QoS4FlowClassEntry": sleV2QoS4FlowClassEntry,
       "sleV2QoS4FlowClassIndex": sleV2QoS4FlowClassIndex,
       "sleV2QoS4FlowClassID": sleV2QoS4FlowClassID,
       "sleV2QoS4FlowClassName": sleV2QoS4FlowClassName,
       "sleV2QoS4FlowPolicy": sleV2QoS4FlowPolicy,
       "sleV2QoS4FlowPolicyTable": sleV2QoS4FlowPolicyTable,
       "sleV2QoS4FlowPolicyEntry": sleV2QoS4FlowPolicyEntry,
       "sleV2QoS4FlowPolicyIndex": sleV2QoS4FlowPolicyIndex,
       "sleV2QoS4FlowPolicyID": sleV2QoS4FlowPolicyID,
       "sleV2QoS4FlowPolicyName": sleV2QoS4FlowPolicyName,
       "sleV2QoS4Class": sleV2QoS4Class,
       "sleV2QoS4ClassInfo": sleV2QoS4ClassInfo,
       "sleV2QoS4ClassTable": sleV2QoS4ClassTable,
       "sleV2QoS4ClassEntry": sleV2QoS4ClassEntry,
       "sleV2QoS4ClassIndex": sleV2QoS4ClassIndex,
       "sleV2QoS4ClassName": sleV2QoS4ClassName,
       "sleV2QoS4ClassFlowCnt": sleV2QoS4ClassFlowCnt,
       "sleV2QoS4ClassControl": sleV2QoS4ClassControl,
       "sleV2QoS4ClassControlRequest": sleV2QoS4ClassControlRequest,
       "sleV2QoS4ClassControlStatus": sleV2QoS4ClassControlStatus,
       "sleV2QoS4ClassControlTimer": sleV2QoS4ClassControlTimer,
       "sleV2QoS4ClassControlTimeStamp": sleV2QoS4ClassControlTimeStamp,
       "sleV2QoS4ClassControlReqResult": sleV2QoS4ClassControlReqResult,
       "sleV2QoS4ClassControlIndex": sleV2QoS4ClassControlIndex,
       "sleV2QoS4ClassControlName": sleV2QoS4ClassControlName,
       "sleV2QoS4ClassNotification": sleV2QoS4ClassNotification,
       "sleClassCreated": sleClassCreated,
       "sleClassDestroyed": sleClassDestroyed,
       "sleClassAllDestroyed": sleClassAllDestroyed,
       "sleV2QoS4ClassFlow": sleV2QoS4ClassFlow,
       "sleV2QoS4ClassFlowTable": sleV2QoS4ClassFlowTable,
       "sleV2QoS4ClassFlowEntry": sleV2QoS4ClassFlowEntry,
       "sleV2QoS4ClassFlowIndex": sleV2QoS4ClassFlowIndex,
       "sleV2QoS4ClassFlowID": sleV2QoS4ClassFlowID,
       "sleV2QoS4ClassFlowName": sleV2QoS4ClassFlowName,
       "sleV2QoS4ClassFlowClassName": sleV2QoS4ClassFlowClassName,
       "sleV2QoS4ClassFlowControl": sleV2QoS4ClassFlowControl,
       "sleV2QoS4ClassFlowControlRequest": sleV2QoS4ClassFlowControlRequest,
       "sleV2QoS4ClassFlowControlStatus": sleV2QoS4ClassFlowControlStatus,
       "sleV2QoS4ClassFlowControlTimer": sleV2QoS4ClassFlowControlTimer,
       "sleV2QoS4ClassFlowControlTimeStamp": sleV2QoS4ClassFlowControlTimeStamp,
       "sleV2QoS4ClassFlowControlReqResult": sleV2QoS4ClassFlowControlReqResult,
       "sleV2QoS4ClassFlowControlClassIndex": sleV2QoS4ClassFlowControlClassIndex,
       "sleV2QoS4ClassFlowControlFlowIndex": sleV2QoS4ClassFlowControlFlowIndex,
       "sleV2QoS4ClassFlowControlFlowID": sleV2QoS4ClassFlowControlFlowID,
       "sleV2QoS4ClassFlowControlClassName": sleV2QoS4ClassFlowControlClassName,
       "sleV2QoS4ClassFlowNotification": sleV2QoS4ClassFlowNotification,
       "sleClassFlowAdded": sleClassFlowAdded,
       "sleClassFlowDeleted": sleClassFlowDeleted,
       "sleClassFlowAllDeleted": sleClassFlowAllDeleted,
       "sleV2QoS4ClassPolicy": sleV2QoS4ClassPolicy,
       "sleV2QoS4ClassPolicyTable": sleV2QoS4ClassPolicyTable,
       "sleV2QoS4ClassPolicyEntry": sleV2QoS4ClassPolicyEntry,
       "sleV2QoS4ClassPolicyIndex": sleV2QoS4ClassPolicyIndex,
       "sleV2QoS4ClassPolicyID": sleV2QoS4ClassPolicyID,
       "sleV2QoS4ClassPolicyName": sleV2QoS4ClassPolicyName,
       "sleV2QoS4Policer": sleV2QoS4Policer,
       "sleV2QoS4PolicerInfo": sleV2QoS4PolicerInfo,
       "sleV2QoS4PolicerTable": sleV2QoS4PolicerTable,
       "sleV2QoS4PolicerEntry": sleV2QoS4PolicerEntry,
       "sleV2QoS4PolicerIndex": sleV2QoS4PolicerIndex,
       "sleV2QoS4PolicerName": sleV2QoS4PolicerName,
       "sleV2QoS4PolicerMeterMode": sleV2QoS4PolicerMeterMode,
       "sleV2QoS4PolicerRateLimit": sleV2QoS4PolicerRateLimit,
       "sleV2QoS4PolicerColorType": sleV2QoS4PolicerColorType,
       "sleV2QoS4PolicerColorMode": sleV2QoS4PolicerColorMode,
       "sleV2QoS4PolicerColorAwareMode": sleV2QoS4PolicerColorAwareMode,
       "sleV2QoS4PolicerColorCIR": sleV2QoS4PolicerColorCIR,
       "sleV2QoS4PolicerColorCBS": sleV2QoS4PolicerColorCBS,
       "sleV2QoS4PolicerColorPIR": sleV2QoS4PolicerColorPIR,
       "sleV2QoS4PolicerColorPBS": sleV2QoS4PolicerColorPBS,
       "sleV2QoS4PolicerColorEBS": sleV2QoS4PolicerColorEBS,
       "sleV2QoS4PolicerColorRedAction": sleV2QoS4PolicerColorRedAction,
       "sleV2QoS4PolicerColorYellowAction": sleV2QoS4PolicerColorYellowAction,
       "sleV2QoS4PolicerColorGreenAction": sleV2QoS4PolicerColorGreenAction,
       "sleV2QoS4PolicerRemarkLayerMode": sleV2QoS4PolicerRemarkLayerMode,
       "sleV2QoS4PolicerRemarkMode": sleV2QoS4PolicerRemarkMode,
       "sleV2QoS4PolicerCounterMode": sleV2QoS4PolicerCounterMode,
       "sleV2QoS4PolicerAvrgCounterMode": sleV2QoS4PolicerAvrgCounterMode,
       "sleV2QoS4PolicerMinBandwidth": sleV2QoS4PolicerMinBandwidth,
       "sleV2QoS4PolicerMaxBandwidth": sleV2QoS4PolicerMaxBandwidth,
       "sleV2QoS4PolicerColorRedDscp": sleV2QoS4PolicerColorRedDscp,
       "sleV2QoS4PolicerColorYellowDscp": sleV2QoS4PolicerColorYellowDscp,
       "sleV2QoS4PolicerColorGreenDscp": sleV2QoS4PolicerColorGreenDscp,
       "sleV2QoS4PolicerColorRedCosType": sleV2QoS4PolicerColorRedCosType,
       "sleV2QoS4PolicerColorRedCos": sleV2QoS4PolicerColorRedCos,
       "sleV2QoS4PolicerColorYellowCosType": sleV2QoS4PolicerColorYellowCosType,
       "sleV2QoS4PolicerColorYellowCos": sleV2QoS4PolicerColorYellowCos,
       "sleV2QoS4PolicerColorGreenCosType": sleV2QoS4PolicerColorGreenCosType,
       "sleV2QoS4PolicerColorGreenCos": sleV2QoS4PolicerColorGreenCos,
       "sleV2QoS4PolicerControl": sleV2QoS4PolicerControl,
       "sleV2QoS4PolicerControlRequest": sleV2QoS4PolicerControlRequest,
       "sleV2QoS4PolicerControlStatus": sleV2QoS4PolicerControlStatus,
       "sleV2QoS4PolicerControlTimer": sleV2QoS4PolicerControlTimer,
       "sleV2QoS4PolicerControlTimeStamp": sleV2QoS4PolicerControlTimeStamp,
       "sleV2QoS4PolicerControlReqResult": sleV2QoS4PolicerControlReqResult,
       "sleV2QoS4PolicerControlIndex": sleV2QoS4PolicerControlIndex,
       "sleV2QoS4PolicerControlName": sleV2QoS4PolicerControlName,
       "sleV2QoS4PolicerControlMeterMode": sleV2QoS4PolicerControlMeterMode,
       "sleV2QoS4PolicerControlRateLimit": sleV2QoS4PolicerControlRateLimit,
       "sleV2QoS4PolicerControlColorType": sleV2QoS4PolicerControlColorType,
       "sleV2QoS4PolicerControlColorMode": sleV2QoS4PolicerControlColorMode,
       "sleV2QoS4PolicerControlColorAwareMode": sleV2QoS4PolicerControlColorAwareMode,
       "sleV2QoS4PolicerControlColorCIR": sleV2QoS4PolicerControlColorCIR,
       "sleV2QoS4PolicerControlColorCBS": sleV2QoS4PolicerControlColorCBS,
       "sleV2QoS4PolicerControlColorPIR": sleV2QoS4PolicerControlColorPIR,
       "sleV2QoS4PolicerControlColorPBS": sleV2QoS4PolicerControlColorPBS,
       "sleV2QoS4PolicerControlColorEBS": sleV2QoS4PolicerControlColorEBS,
       "sleV2QoS4PolicerControlColorRedAction": sleV2QoS4PolicerControlColorRedAction,
       "sleV2QoS4PolicerControlColorYellowAction": sleV2QoS4PolicerControlColorYellowAction,
       "sleV2QoS4PolicerControlColorGreenAction": sleV2QoS4PolicerControlColorGreenAction,
       "sleV2QoS4PolicerControlRemarkLayerMode": sleV2QoS4PolicerControlRemarkLayerMode,
       "sleV2QoS4PolicerControlRemarkMode": sleV2QoS4PolicerControlRemarkMode,
       "sleV2QoS4PolicerControlCounterMode": sleV2QoS4PolicerControlCounterMode,
       "sleV2QoS4PolicerControlAvrgCounterMode": sleV2QoS4PolicerControlAvrgCounterMode,
       "sleV2QoS4PolicerControlMinBandwidth": sleV2QoS4PolicerControlMinBandwidth,
       "sleV2QoS4PolicerControlMaxBandwidth": sleV2QoS4PolicerControlMaxBandwidth,
       "sleV2QoS4PolicerControlColorRedDscp": sleV2QoS4PolicerControlColorRedDscp,
       "sleV2QoS4PolicerControlColorYellowDscp": sleV2QoS4PolicerControlColorYellowDscp,
       "sleV2QoS4PolicerControlColorGreenDscp": sleV2QoS4PolicerControlColorGreenDscp,
       "sleV2QoS4PolicerControlColorRedCosType": sleV2QoS4PolicerControlColorRedCosType,
       "sleV2QoS4PolicerControlColorRedCos": sleV2QoS4PolicerControlColorRedCos,
       "sleV2QoS4PolicerControlColorYellowCosType": sleV2QoS4PolicerControlColorYellowCosType,
       "sleV2QoS4PolicerControlColorYellowCos": sleV2QoS4PolicerControlColorYellowCos,
       "sleV2QoS4PolicerControlColorGreenCosType": sleV2QoS4PolicerControlColorGreenCosType,
       "sleV2QoS4PolicerControlColorGreenCos": sleV2QoS4PolicerControlColorGreenCos,
       "sleV2QoS4PolicerNotification": sleV2QoS4PolicerNotification,
       "slePolicerCreated": slePolicerCreated,
       "slePolicerChanged": slePolicerChanged,
       "slePolicerDestroyed": slePolicerDestroyed,
       "sleV2QoS4PolicerMatchCounter": sleV2QoS4PolicerMatchCounter,
       "sleV2QoS4PolicerMatchCounterTable": sleV2QoS4PolicerMatchCounterTable,
       "sleV2QoS4PolicerMatchCounterEntry": sleV2QoS4PolicerMatchCounterEntry,
       "sleV2QoS4PolicerMatchCounterName": sleV2QoS4PolicerMatchCounterName,
       "sleV2QoS4PolicerMatchCounterDesc": sleV2QoS4PolicerMatchCounterDesc,
       "sleV2QoS4PolicerMatchCounterValue": sleV2QoS4PolicerMatchCounterValue,
       "sleV2QoS4Policy": sleV2QoS4Policy,
       "sleV2QoS4PolicyInfo": sleV2QoS4PolicyInfo,
       "sleV2QoS4PolicyTable": sleV2QoS4PolicyTable,
       "sleV2QoS4PolicyEntry": sleV2QoS4PolicyEntry,
       "sleV2QoS4PolicyIndex": sleV2QoS4PolicyIndex,
       "sleV2QoS4PolicyName": sleV2QoS4PolicyName,
       "sleV2QoS4PolicyFlowCnt": sleV2QoS4PolicyFlowCnt,
       "sleV2QoS4PolicyClassCnt": sleV2QoS4PolicyClassCnt,
       "sleV2QoS4PolicyPolicerIndex": sleV2QoS4PolicyPolicerIndex,
       "sleV2QoS4PolicyPriority": sleV2QoS4PolicyPriority,
       "sleV2QoS4PolicyIngressPorts": sleV2QoS4PolicyIngressPorts,
       "sleV2QoS4PolicyEgressPorts": sleV2QoS4PolicyEgressPorts,
       "sleV2QoS4PolicyVlan": sleV2QoS4PolicyVlan,
       "sleV2QoS4PolicyMatchFlag": sleV2QoS4PolicyMatchFlag,
       "sleV2QoS4PolicyMatchVlan": sleV2QoS4PolicyMatchVlan,
       "sleV2QoS4PolicyMatchRedirectVlan": sleV2QoS4PolicyMatchRedirectVlan,
       "sleV2QoS4PolicyMatchRedirectPort": sleV2QoS4PolicyMatchRedirectPort,
       "sleV2QoS4PolicyMatchMarkMode": sleV2QoS4PolicyMatchMarkMode,
       "sleV2QoS4PolicyMatchQueue": sleV2QoS4PolicyMatchQueue,
       "sleV2QoS4PolicyMatchDp": sleV2QoS4PolicyMatchDp,
       "sleV2QoS4PolicyMatchCoS": sleV2QoS4PolicyMatchCoS,
       "sleV2QoS4PolicyMatchDscp": sleV2QoS4PolicyMatchDscp,
       "sleV2QoS4PolicyMatchIpPrecedence": sleV2QoS4PolicyMatchIpPrecedence,
       "sleV2QoS4PolicyMatchDstMacOrEgressPorts": sleV2QoS4PolicyMatchDstMacOrEgressPorts,
       "sleV2QoS4PolicyMatchDstMac": sleV2QoS4PolicyMatchDstMac,
       "sleV2QoS4PolicyMatchEgressPorts": sleV2QoS4PolicyMatchEgressPorts,
       "sleV2QoS4PolicyNomatchFlag": sleV2QoS4PolicyNomatchFlag,
       "sleV2QoS4PolicyNomatchRedirectPort": sleV2QoS4PolicyNomatchRedirectPort,
       "sleV2QoS4PolicyNomatchCoS": sleV2QoS4PolicyNomatchCoS,
       "sleV2QoS4PolicyNomatchDscp": sleV2QoS4PolicyNomatchDscp,
       "sleV2QoS4PolicyNomatchIpPrecedence": sleV2QoS4PolicyNomatchIpPrecedence,
       "sleV2QoS4PolicyCounterValue": sleV2QoS4PolicyCounterValue,
       "sleV2QoS4PolicyCounterGreenBytes": sleV2QoS4PolicyCounterGreenBytes,
       "sleV2QoS4PolicyCounterYellowBytes": sleV2QoS4PolicyCounterYellowBytes,
       "sleV2QoS4PolicyCounterRedBytes": sleV2QoS4PolicyCounterRedBytes,
       "sleV2QoS4PolicyRedirBlackhole": sleV2QoS4PolicyRedirBlackhole,
       "sleV2QoS4PolicyAvrg5SecCounterValue": sleV2QoS4PolicyAvrg5SecCounterValue,
       "sleV2QoS4PolicyAvrg1minCounterValue": sleV2QoS4PolicyAvrg1minCounterValue,
       "sleV2QoS4PolicyAvrg10minCounterValue": sleV2QoS4PolicyAvrg10minCounterValue,
       "sleV2QoS4PolicyIngressTunnelIfIndex": sleV2QoS4PolicyIngressTunnelIfIndex,
       "sleV2QoS4PolicyEgressTunnelIfIndex": sleV2QoS4PolicyEgressTunnelIfIndex,
       "sleV2QoS4PolicyCounterElapsedTimeAfterClear": sleV2QoS4PolicyCounterElapsedTimeAfterClear,
       "sleV2QoS4PolicyMatchPbrNextHop": sleV2QoS4PolicyMatchPbrNextHop,
       "sleV2QoS4PolicyStage": sleV2QoS4PolicyStage,
       "sleV2QoS4PolicyIngressPortsFlag": sleV2QoS4PolicyIngressPortsFlag,
       "sleV2QoS4PolicyEgressPortsFlag": sleV2QoS4PolicyEgressPortsFlag,
       "sleV2QoS4PolicyInnerVlanAction": sleV2QoS4PolicyInnerVlanAction,
       "sleV2QoS4PolicyOuterVlanAction": sleV2QoS4PolicyOuterVlanAction,
       "sleV2QoS4PolicyInnerVlan": sleV2QoS4PolicyInnerVlan,
       "sleV2QoS4PolicyOuterVlan": sleV2QoS4PolicyOuterVlan,
       "sleV2QoS4PolicyMatchPbrNextHopSecondary": sleV2QoS4PolicyMatchPbrNextHopSecondary,
       "sleV2QoS4PolicyMatchPbrNextHopVerifyReach": sleV2QoS4PolicyMatchPbrNextHopVerifyReach,
       "sleV2QoS4PolicyMatchFlowAlias": sleV2QoS4PolicyMatchFlowAlias,
       "sleV2QoS4PolicyMatchInnerVlanCosReplace": sleV2QoS4PolicyMatchInnerVlanCosReplace,
       "sleV2QoS4PolicyMatchInnerVlanCfiReplace": sleV2QoS4PolicyMatchInnerVlanCfiReplace,
       "sleV2QoS4PolicyMatchOuterVlanCosReplace": sleV2QoS4PolicyMatchOuterVlanCosReplace,
       "sleV2QoS4PolicyMatchOuterVlanCfiReplace": sleV2QoS4PolicyMatchOuterVlanCfiReplace,
       "sleV2QoS4PolicyControl": sleV2QoS4PolicyControl,
       "sleV2QoS4PolicyControlRequest": sleV2QoS4PolicyControlRequest,
       "sleV2QoS4PolicyControlStatus": sleV2QoS4PolicyControlStatus,
       "sleV2QoS4PolicyControlTimer": sleV2QoS4PolicyControlTimer,
       "sleV2QoS4PolicyControlTimeStamp": sleV2QoS4PolicyControlTimeStamp,
       "sleV2QoS4PolicyControlReqResult": sleV2QoS4PolicyControlReqResult,
       "sleV2QoS4PolicyControlIndex": sleV2QoS4PolicyControlIndex,
       "sleV2QoS4PolicyControlName": sleV2QoS4PolicyControlName,
       "sleV2QoS4PolicyControlPolicerIndex": sleV2QoS4PolicyControlPolicerIndex,
       "sleV2QoS4PolicyControlPriority": sleV2QoS4PolicyControlPriority,
       "sleV2QoS4PolicyControlIngressPorts": sleV2QoS4PolicyControlIngressPorts,
       "sleV2QoS4PolicyControlEgressPorts": sleV2QoS4PolicyControlEgressPorts,
       "sleV2QoS4PolicyControlVlan": sleV2QoS4PolicyControlVlan,
       "sleV2QoS4PolicyControlMatchFlag": sleV2QoS4PolicyControlMatchFlag,
       "sleV2QoS4PolicyControlMatchVlan": sleV2QoS4PolicyControlMatchVlan,
       "sleV2QoS4PolicyControlMatchRedirectVlan": sleV2QoS4PolicyControlMatchRedirectVlan,
       "sleV2QoS4PolicyControlMatchRedirectPort": sleV2QoS4PolicyControlMatchRedirectPort,
       "sleV2QoS4PolicyControlMatchMarkMode": sleV2QoS4PolicyControlMatchMarkMode,
       "sleV2QoS4PolicyControlMatchQueue": sleV2QoS4PolicyControlMatchQueue,
       "sleV2QoS4PolicyControlMatchDp": sleV2QoS4PolicyControlMatchDp,
       "sleV2QoS4PolicyControlMatchCoS": sleV2QoS4PolicyControlMatchCoS,
       "sleV2QoS4PolicyControlMatchDscp": sleV2QoS4PolicyControlMatchDscp,
       "sleV2QoS4PolicyControlMatchIpPrecedence": sleV2QoS4PolicyControlMatchIpPrecedence,
       "sleV2QoS4PolicyControlMatchDstMacOrEgressPorts": sleV2QoS4PolicyControlMatchDstMacOrEgressPorts,
       "sleV2QoS4PolicyControlMatchDstMac": sleV2QoS4PolicyControlMatchDstMac,
       "sleV2QoS4PolicyControlMatchEgressPorts": sleV2QoS4PolicyControlMatchEgressPorts,
       "sleV2QoS4PolicyControlNomatchFlag": sleV2QoS4PolicyControlNomatchFlag,
       "sleV2QoS4PolicyControlNomatchRedirectPort": sleV2QoS4PolicyControlNomatchRedirectPort,
       "sleV2QoS4PolicyControlNomatchCoS": sleV2QoS4PolicyControlNomatchCoS,
       "sleV2QoS4PolicyControlNomatchDscp": sleV2QoS4PolicyControlNomatchDscp,
       "sleV2QoS4PolicyControlNomatchIpPrecedence": sleV2QoS4PolicyControlNomatchIpPrecedence,
       "sleV2QoS4PolicyControlMatchRedirBlackhole": sleV2QoS4PolicyControlMatchRedirBlackhole,
       "sleV2QoS4PolicyControlIngressTunnelIfIndex": sleV2QoS4PolicyControlIngressTunnelIfIndex,
       "sleV2Qo4SPolicyControlEgressTunnelIfIndex": sleV2Qo4SPolicyControlEgressTunnelIfIndex,
       "sleV2QoS4PolicyControlMatchPbrNextHop": sleV2QoS4PolicyControlMatchPbrNextHop,
       "sleV2QoS4PolicyControlStage": sleV2QoS4PolicyControlStage,
       "sleV2QoS4PolicyControlIngressPortsFlag": sleV2QoS4PolicyControlIngressPortsFlag,
       "sleV2QoS4PolicyControlEgressPortsFlag": sleV2QoS4PolicyControlEgressPortsFlag,
       "sleV2QoS4PolicyControlInnerVlanAction": sleV2QoS4PolicyControlInnerVlanAction,
       "sleV2QoS4PolicyControlOuterVlanAction": sleV2QoS4PolicyControlOuterVlanAction,
       "sleV2QoS4PolicyControlInnerVlan": sleV2QoS4PolicyControlInnerVlan,
       "sleV2QoS4PolicyControlOuterVlan": sleV2QoS4PolicyControlOuterVlan,
       "sleV2QoS4PolicyControlMatchPbrNextHopSecondary": sleV2QoS4PolicyControlMatchPbrNextHopSecondary,
       "sleV2QoS4PolicyControlMatchPbrNextHopVerifyReach": sleV2QoS4PolicyControlMatchPbrNextHopVerifyReach,
       "sleV2QoS4PolicyControlMatchFlowAlias": sleV2QoS4PolicyControlMatchFlowAlias,
       "sleV2QoS4PolicyControlMatchInnerVlanCosReplace": sleV2QoS4PolicyControlMatchInnerVlanCosReplace,
       "sleV2QoS4PolicyControlMatchInnerVlanCfiReplace": sleV2QoS4PolicyControlMatchInnerVlanCfiReplace,
       "sleV2QoS4PolicyControlMatchOuterVlanCosReplace": sleV2QoS4PolicyControlMatchOuterVlanCosReplace,
       "sleV2QoS4PolicyControlMatchOuterVlanCfiReplace": sleV2QoS4PolicyControlMatchOuterVlanCfiReplace,
       "sleV2QoSPolicyNotification": sleV2QoSPolicyNotification,
       "slePolicyCreated": slePolicyCreated,
       "slePolicyInfoChanged": slePolicyInfoChanged,
       "slePolicyMatchActionChanged": slePolicyMatchActionChanged,
       "slePolicyNomatchActionChanged": slePolicyNomatchActionChanged,
       "slePolicyDestroyed": slePolicyDestroyed,
       "slePolicyCounterCleared": slePolicyCounterCleared,
       "slePolicyEmptyCreated": slePolicyEmptyCreated,
       "slePolicyIngressTunnelSet": slePolicyIngressTunnelSet,
       "slePolicyIngressTunnelUnset": slePolicyIngressTunnelUnset,
       "slePolicyEgressTunnelSet": slePolicyEgressTunnelSet,
       "slePolicyEgressTunnelUnset": slePolicyEgressTunnelUnset,
       "slePolicyActionMatchFlowAliasChanged": slePolicyActionMatchFlowAliasChanged,
       "slePolicyMatchInnerVlanCosReplaceChanged": slePolicyMatchInnerVlanCosReplaceChanged,
       "slePolicyMatchInnerVlanCfiReplaceChanged": slePolicyMatchInnerVlanCfiReplaceChanged,
       "slePolicyMatchOuterVlanCosReplaceChanged": slePolicyMatchOuterVlanCosReplaceChanged,
       "slePolicyMatchOuterVlanCfiReplaceChanged": slePolicyMatchOuterVlanCfiReplaceChanged,
       "sleV2QoS4PolicyFlowClass": sleV2QoS4PolicyFlowClass,
       "sleV2QoS4PolicyFlowClassTable": sleV2QoS4PolicyFlowClassTable,
       "sleV2QoS4PolicyFlowClassEntry": sleV2QoS4PolicyFlowClassEntry,
       "sleV2QoS4PolicyFlowClassIndex": sleV2QoS4PolicyFlowClassIndex,
       "sleV2QoS4PolicyFlowClassType": sleV2QoS4PolicyFlowClassType,
       "sleV2QoS4PolicyFlowClassID": sleV2QoS4PolicyFlowClassID,
       "sleV2QoS4PolicyFlowClassName": sleV2QoS4PolicyFlowClassName,
       "sleV2QoS4PolicyFlowClassControl": sleV2QoS4PolicyFlowClassControl,
       "sleV2QoS4PolicyFlowClassControlRequest": sleV2QoS4PolicyFlowClassControlRequest,
       "sleV2QoS4PolicyFlowClassControlStatus": sleV2QoS4PolicyFlowClassControlStatus,
       "sleV2QoS4PolicyFlowClassControlTimer": sleV2QoS4PolicyFlowClassControlTimer,
       "sleV2QoS4PolicyFlowClassControlTimeStamp": sleV2QoS4PolicyFlowClassControlTimeStamp,
       "sleV2QoS4PolicyFlowClassControlReqResult": sleV2QoS4PolicyFlowClassControlReqResult,
       "sleV2QoS4PolicyFlowClassControlPolicyIndex": sleV2QoS4PolicyFlowClassControlPolicyIndex,
       "sleV2QoS4PolicyFlowClassControlIndex": sleV2QoS4PolicyFlowClassControlIndex,
       "sleV2QoS4PolicyFlowClassControlType": sleV2QoS4PolicyFlowClassControlType,
       "sleV2QoS4PolicyFlowClassControlFlowID": sleV2QoS4PolicyFlowClassControlFlowID,
       "sleV2QoS4PolicyFlowClassControlClassID": sleV2QoS4PolicyFlowClassControlClassID,
       "sleV2QoS4PolicyFlowClassNotification": sleV2QoS4PolicyFlowClassNotification,
       "slePolicyFlowAdded": slePolicyFlowAdded,
       "slePolicyFlowDeleted": slePolicyFlowDeleted,
       "slePolicyAllFlowDeleted": slePolicyAllFlowDeleted,
       "slePolicyAllClassDeleted": slePolicyAllClassDeleted,
       "slePolicyAllFlowClassDeleted": slePolicyAllFlowClassDeleted,
       "sleV2QoS4PolicyIF": sleV2QoS4PolicyIF,
       "sleV2QoS4PolicyIFTable": sleV2QoS4PolicyIFTable,
       "sleV2QoS4PolicyIFEntry": sleV2QoS4PolicyIFEntry,
       "sleV2QoS4PolicyIFDirection": sleV2QoS4PolicyIFDirection,
       "sleV2QoS4PolicyIFControl": sleV2QoS4PolicyIFControl,
       "sleV2QoS4PolicyIFControlRequest": sleV2QoS4PolicyIFControlRequest,
       "sleV2QoS4PolicyIFControlStatus": sleV2QoS4PolicyIFControlStatus,
       "sleV2QoS4PolicyIFControlTimer": sleV2QoS4PolicyIFControlTimer,
       "sleV2QoS4PolicyIFControlTimeStamp": sleV2QoS4PolicyIFControlTimeStamp,
       "sleV2QoS4PolicyIFControlReqResult": sleV2QoS4PolicyIFControlReqResult,
       "sleV2QoS4PolicyIFControlIfindex": sleV2QoS4PolicyIFControlIfindex,
       "sleV2QoS4PolicyIFControlPolicyIndex": sleV2QoS4PolicyIFControlPolicyIndex,
       "sleV2QoS4PolicyIFControlDirection": sleV2QoS4PolicyIFControlDirection,
       "sleV2QoS4PolicyIFNotification": sleV2QoS4PolicyIFNotification,
       "sleV2QosPolicyIFServicePolicyChanged": sleV2QosPolicyIFServicePolicyChanged,
       "sleV2QosPolicyIFServicePolicyCleared": sleV2QosPolicyIFServicePolicyCleared,
       "sleV2QoS4Remark": sleV2QoS4Remark,
       "sleV2QoS4RemarkBase": sleV2QoS4RemarkBase,
       "sleV2QoS4RemarkInfo": sleV2QoS4RemarkInfo,
       "sleV2QoS4RemarkLayer2Mode": sleV2QoS4RemarkLayer2Mode,
       "sleV2QoS4RemarkMode": sleV2QoS4RemarkMode,
       "sleV2QoS4RemarkControl": sleV2QoS4RemarkControl,
       "sleV2QoS4RemarkControlRequest": sleV2QoS4RemarkControlRequest,
       "sleV2QoS4RemarkControlStatus": sleV2QoS4RemarkControlStatus,
       "sleV2QoS4RemarkControlTimer": sleV2QoS4RemarkControlTimer,
       "sleV2QoS4RemarkControlTimStamp": sleV2QoS4RemarkControlTimStamp,
       "sleV2QoS4RemarkControlReqResult": sleV2QoS4RemarkControlReqResult,
       "sleV2QoS4RemarkControlLayer2Mode": sleV2QoS4RemarkControlLayer2Mode,
       "sleV2QoS4RemarkControlMode": sleV2QoS4RemarkControlMode,
       "sleV2QoS4RemarkNotification": sleV2QoS4RemarkNotification,
       "sleRemarkChanged": sleRemarkChanged,
       "sleV2QoS4RemarkL3": sleV2QoS4RemarkL3,
       "sleV2QoS4RemarkL3Table": sleV2QoS4RemarkL3Table,
       "sleV2QoS4RemarkL3Entry": sleV2QoS4RemarkL3Entry,
       "sleV2QoS4RemarkL3ColorIndex": sleV2QoS4RemarkL3ColorIndex,
       "sleV2QoS4RemarkL3DSCPIndex": sleV2QoS4RemarkL3DSCPIndex,
       "sleV2QoS4RemarkL3Queue": sleV2QoS4RemarkL3Queue,
       "sleV2QoS4RemarkL3Dp": sleV2QoS4RemarkL3Dp,
       "sleV2QoS4RemarkL3CoS": sleV2QoS4RemarkL3CoS,
       "sleV2QoS4RemarkL3Dscp": sleV2QoS4RemarkL3Dscp,
       "sleV2QoS4RemarkL3Control": sleV2QoS4RemarkL3Control,
       "sleV2QoS4RemarkL3ControlRequest": sleV2QoS4RemarkL3ControlRequest,
       "sleV2QoS4RemarkL3ControlStatus": sleV2QoS4RemarkL3ControlStatus,
       "sleV2QoS4RemarkL3ControlTimer": sleV2QoS4RemarkL3ControlTimer,
       "sleV2QoS4RemarkL3ControlTimeStamp": sleV2QoS4RemarkL3ControlTimeStamp,
       "sleV2QoS4RemarkL3ControlReqResult": sleV2QoS4RemarkL3ControlReqResult,
       "sleV2QoS4RemarkL3ControlColorIndex": sleV2QoS4RemarkL3ControlColorIndex,
       "sleV2QoS4RemarkL3ControlDSCPIndex": sleV2QoS4RemarkL3ControlDSCPIndex,
       "sleV2QoS4RemarkL3ControlQueue": sleV2QoS4RemarkL3ControlQueue,
       "sleV2QoS4RemarkL3ControlDp": sleV2QoS4RemarkL3ControlDp,
       "sleV2QoS4RemarkL3ControlCoS": sleV2QoS4RemarkL3ControlCoS,
       "sleV2QoS4RemarkL3ControlDscp": sleV2QoS4RemarkL3ControlDscp,
       "sleV2QoS4RemarkL3Notification": sleV2QoS4RemarkL3Notification,
       "sleRemarkL3Changed": sleRemarkL3Changed,
       "sleV2QoS4RemarkL2": sleV2QoS4RemarkL2,
       "sleV2QoS4RemarkL2Table": sleV2QoS4RemarkL2Table,
       "sleV2QoS4RemarkL2Entry": sleV2QoS4RemarkL2Entry,
       "sleV2QoS4RemarkL2ColorIndex": sleV2QoS4RemarkL2ColorIndex,
       "sleV2QoS4RemarkL2QueueCoSIndex": sleV2QoS4RemarkL2QueueCoSIndex,
       "sleV2QoS4RemarkL2Queue": sleV2QoS4RemarkL2Queue,
       "sleV2QoS4RemarkL2Dp": sleV2QoS4RemarkL2Dp,
       "sleV2QoS4RemarkL2CoS": sleV2QoS4RemarkL2CoS,
       "sleV2QoS4RemarkL2Dscp": sleV2QoS4RemarkL2Dscp,
       "sleV2QoS4RemarkL2Control": sleV2QoS4RemarkL2Control,
       "sleV2QoS4RemarkL2ControlRequest": sleV2QoS4RemarkL2ControlRequest,
       "sleV2QoS4RemarkL2ControlStatus": sleV2QoS4RemarkL2ControlStatus,
       "sleV2QoS4RemarkL2ControlTimer": sleV2QoS4RemarkL2ControlTimer,
       "sleV2QoS4RemarkL2ControlTimeStamp": sleV2QoS4RemarkL2ControlTimeStamp,
       "sleV2QoS4RemarkL2ControlReqResult": sleV2QoS4RemarkL2ControlReqResult,
       "sleV2QoS4RemarkL2ControlColorIndex": sleV2QoS4RemarkL2ControlColorIndex,
       "sleV2QoS4RemarkL2ControlQueueCoSIndex": sleV2QoS4RemarkL2ControlQueueCoSIndex,
       "sleV2QoS4RemarkL2ControlQueue": sleV2QoS4RemarkL2ControlQueue,
       "sleV2QoS4RemarkL2ControlDp": sleV2QoS4RemarkL2ControlDp,
       "sleV2QoS4RemarkL2ControlCoS": sleV2QoS4RemarkL2ControlCoS,
       "sleV2QoS4RemarkL2ControlDscp": sleV2QoS4RemarkL2ControlDscp,
       "sleV2QoS4RemarkL2Notification": sleV2QoS4RemarkL2Notification,
       "sleRemarkL2Changed": sleRemarkL2Changed,
       "sleV2QoS4RED": sleV2QoS4RED,
       "sleV2QoS4REDProfile": sleV2QoS4REDProfile,
       "sleV2QoS4REDProfileTable": sleV2QoS4REDProfileTable,
       "sleV2QoS4REDProfileEntry": sleV2QoS4REDProfileEntry,
       "sleV2QoS4REDProfileId": sleV2QoS4REDProfileId,
       "sleV2QoS4REDProfileQueueId": sleV2QoS4REDProfileQueueId,
       "sleV2QoS4REDProfileDp0MinThres": sleV2QoS4REDProfileDp0MinThres,
       "sleV2QoS4REDProfileDp0MaxThres": sleV2QoS4REDProfileDp0MaxThres,
       "sleV2QoS4REDProfileDp0Prob": sleV2QoS4REDProfileDp0Prob,
       "sleV2QoS4REDProfileDp1MinThres": sleV2QoS4REDProfileDp1MinThres,
       "sleV2QoS4REDProfileDp1MaxThres": sleV2QoS4REDProfileDp1MaxThres,
       "sleV2QoS4REDProfileDp1Prob": sleV2QoS4REDProfileDp1Prob,
       "sleV2QoS4REDProfileDp2MinThres": sleV2QoS4REDProfileDp2MinThres,
       "sleV2QoS4REDProfileDp2MaxThres": sleV2QoS4REDProfileDp2MaxThres,
       "sleV2QoS4REDProfileDp2Prob": sleV2QoS4REDProfileDp2Prob,
       "sleV2QoS4REDProfileWeight": sleV2QoS4REDProfileWeight,
       "sleV2QoS4REDProfileControl": sleV2QoS4REDProfileControl,
       "sleV2QoS4REDProfileControlRequest": sleV2QoS4REDProfileControlRequest,
       "sleV2QoS4REDProfileControlStatus": sleV2QoS4REDProfileControlStatus,
       "sleV2QoS4REDProfileControlTimer": sleV2QoS4REDProfileControlTimer,
       "sleV2QoS4REDProfileControlTimeStamp": sleV2QoS4REDProfileControlTimeStamp,
       "sleV2QoS4REDProfileControlReqResult": sleV2QoS4REDProfileControlReqResult,
       "sleV2QoS4REDProfileControlId": sleV2QoS4REDProfileControlId,
       "sleV2QoS4REDProfileControlQueueId": sleV2QoS4REDProfileControlQueueId,
       "sleV2QoS4REDProfileControlDp0MinThres": sleV2QoS4REDProfileControlDp0MinThres,
       "sleV2QoS4REDProfileControlDp0MaxThres": sleV2QoS4REDProfileControlDp0MaxThres,
       "sleV2QoS4REDProfileControlDp0Prob": sleV2QoS4REDProfileControlDp0Prob,
       "sleV2QoS4REDProfileControlDp1MinThres": sleV2QoS4REDProfileControlDp1MinThres,
       "sleV2QoS4REDProfileControlDp1MaxThres": sleV2QoS4REDProfileControlDp1MaxThres,
       "sleV2QoS4REDProfileControlDp1Prob": sleV2QoS4REDProfileControlDp1Prob,
       "sleV2QoS4REDProfileControlDp2MinThres": sleV2QoS4REDProfileControlDp2MinThres,
       "sleV2QoS4REDProfileControlDp2MaxThres": sleV2QoS4REDProfileControlDp2MaxThres,
       "sleV2QoS4REDProfileControlDp2Prob": sleV2QoS4REDProfileControlDp2Prob,
       "sleV2QoS4REDProfileControlWeight": sleV2QoS4REDProfileControlWeight,
       "sleV2QoS4REDProfileNotification": sleV2QoS4REDProfileNotification,
       "sleV2QS4REDProfileChanged": sleV2QS4REDProfileChanged,
       "sleV2QS4REDProfileCleared": sleV2QS4REDProfileCleared,
       "sleV2QoS4PortREDInfo": sleV2QoS4PortREDInfo,
       "sleV2QoS4PortREDInfoTable": sleV2QoS4PortREDInfoTable,
       "sleV2QoS4PortREDInfoEntry": sleV2QoS4PortREDInfoEntry,
       "sleV2QoS4PortREDInfoInterfaceIndex": sleV2QoS4PortREDInfoInterfaceIndex,
       "sleV2QoS4PortREDInfoEnable": sleV2QoS4PortREDInfoEnable,
       "sleV2QoS4PortREDInfoProfileId": sleV2QoS4PortREDInfoProfileId,
       "sleV2QoS4PortREDInfoControl": sleV2QoS4PortREDInfoControl,
       "sleV2QoS4PortREDInfoControlRequest": sleV2QoS4PortREDInfoControlRequest,
       "sleV2QoS4PortREDInfoControlStatus": sleV2QoS4PortREDInfoControlStatus,
       "sleV2QoS4PortREDInfoControlTimer": sleV2QoS4PortREDInfoControlTimer,
       "sleV2QoS4PortREDInfoControlTimeStamp": sleV2QoS4PortREDInfoControlTimeStamp,
       "sleV2QoS4PortREDInfoControlReqResult": sleV2QoS4PortREDInfoControlReqResult,
       "sleV2QoS4PortREDInfoControlInterfaceIndex": sleV2QoS4PortREDInfoControlInterfaceIndex,
       "sleV2QoS4PortREDInfoControlEnable": sleV2QoS4PortREDInfoControlEnable,
       "sleV2QoS4PortREDInfoControlProfileId": sleV2QoS4PortREDInfoControlProfileId,
       "sleV2QoS4PortREDInfoNotification": sleV2QoS4PortREDInfoNotification,
       "sleV2QoS4PortREDInfoChanged": sleV2QoS4PortREDInfoChanged,
       "sleV2QoS4Queue": sleV2QoS4Queue,
       "sleV2QoS4QueueInfo": sleV2QoS4QueueInfo,
       "sleV2QoS4QueueInfoTable": sleV2QoS4QueueInfoTable,
       "sleV2QoS4QueueInfoEntry": sleV2QoS4QueueInfoEntry,
       "sleV2QoS4QueueInfoInterfaceIndex": sleV2QoS4QueueInfoInterfaceIndex,
       "sleV2QoS4QueueInfoId": sleV2QoS4QueueInfoId,
       "sleV2QoS4QueueInfoScheduleMode": sleV2QoS4QueueInfoScheduleMode,
       "sleV2QoS4QueueInfoDWRRGroup": sleV2QoS4QueueInfoDWRRGroup,
       "sleV2QoS4QueueInfoMinBandwidth": sleV2QoS4QueueInfoMinBandwidth,
       "sleV2QoS4QueueInfoMaxBandwidth": sleV2QoS4QueueInfoMaxBandwidth,
       "sleV2QoS4QueueInfoWeight": sleV2QoS4QueueInfoWeight,
       "sleV2QoS4QueueMappedCoS": sleV2QoS4QueueMappedCoS,
       "sleV2QoS4QueueInfoBufferEgressMinLimitUnicast": sleV2QoS4QueueInfoBufferEgressMinLimitUnicast,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast": sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyUnicast,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitUnicast": sleV2QoS4QueueInfoBufferEgressMaxLimitUnicast,
       "sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast": sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicast,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast": sleV2QoS4QueueInfoBufferEgressMaxLimitPolicyNonUnicast,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast": sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicast,
       "sleV2QoS4QueueInfoControl": sleV2QoS4QueueInfoControl,
       "sleV2QoS4QueueInfoControlRequest": sleV2QoS4QueueInfoControlRequest,
       "sleV2QoS4QueueInfoControlStatus": sleV2QoS4QueueInfoControlStatus,
       "sleV2QoS4QueueInfoControlTimer": sleV2QoS4QueueInfoControlTimer,
       "sleV2QoS4QueueInfoControlTimeStamp": sleV2QoS4QueueInfoControlTimeStamp,
       "sleV2QoS4QueueInfoControlReqResult": sleV2QoS4QueueInfoControlReqResult,
       "sleV2QoS4QueueInfoControlInterfaceIndex": sleV2QoS4QueueInfoControlInterfaceIndex,
       "sleV2QoS4QueueInfoControlId": sleV2QoS4QueueInfoControlId,
       "sleV2QoS4QueueInfoControlScheduleMode": sleV2QoS4QueueInfoControlScheduleMode,
       "sleV2QoS4QueueInfoControlDWRRGroup": sleV2QoS4QueueInfoControlDWRRGroup,
       "sleV2QoS4QueueInfoControlMinBandwidth": sleV2QoS4QueueInfoControlMinBandwidth,
       "sleV2QoS4QueueInfoControlMaxBandwidth": sleV2QoS4QueueInfoControlMaxBandwidth,
       "sleV2QoS4QueueInfoControlWeight": sleV2QoS4QueueInfoControlWeight,
       "sleV2QoS4QueueInfoControlMappedCoS": sleV2QoS4QueueInfoControlMappedCoS,
       "sleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast": sleV2QoS4QueueInfoControlBufferEgressMinLimitUnicast,
       "sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast": sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyUnicast,
       "sleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast": sleV2QoS4QueueInfoControlBufferEgressMaxLimitUnicast,
       "sleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast": sleV2QoS4QueueInfoControlBufferEgressMinLimitNonUnicast,
       "sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast": sleV2QoS4QueueInfoControlBufferEgressMaxLimitPolicyNonUnicast,
       "sleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast": sleV2QoS4QueueInfoControlBufferEgressMaxLimitNonUnicast,
       "sleV2QoS4QueueInfoNotification": sleV2QoS4QueueInfoNotification,
       "sleV2QoS4QueueInfoChanged": sleV2QoS4QueueInfoChanged,
       "sleV2QoS4QueueInfoScheduleModeChanged": sleV2QoS4QueueInfoScheduleModeChanged,
       "sleV2QoS4QueueInfoMaxBandwidthChanged": sleV2QoS4QueueInfoMaxBandwidthChanged,
       "sleV2QoS4QueueInfoMinBandwidthChanged": sleV2QoS4QueueInfoMinBandwidthChanged,
       "sleV2QoS4QueueInfoWeightChanged": sleV2QoS4QueueInfoWeightChanged,
       "sleV2QoS4QueueInfoBufferEgressMinLimitUnicastChanged": sleV2QoS4QueueInfoBufferEgressMinLimitUnicastChanged,
       "sleV2QoS4QueueInfoBufferEgressMinLimitUnicastCleared": sleV2QoS4QueueInfoBufferEgressMinLimitUnicastCleared,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastChanged": sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastChanged,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastCleared": sleV2QoS4QueueInfoBufferEgressMaxLimitUnicastCleared,
       "sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastChanged": sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastChanged,
       "sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastCleared": sleV2QoS4QueueInfoBufferEgressMinLimitNonUnicastCleared,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastChanged": sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastChanged,
       "sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastCleared": sleV2QoS4QueueInfoBufferEgressMaxLimitNonUnicastCleared,
       "sleV2QoS4DscpMap": sleV2QoS4DscpMap,
       "sleV2QoS4DscpMapIngress": sleV2QoS4DscpMapIngress,
       "sleV2QoS4DscpMapIngressTable": sleV2QoS4DscpMapIngressTable,
       "sleV2QoS4DscpMapIngressEntry": sleV2QoS4DscpMapIngressEntry,
       "sleV2QoS4DscpMapIngressDscpIndex": sleV2QoS4DscpMapIngressDscpIndex,
       "sleV2QoS4DscpMapIngressDscp": sleV2QoS4DscpMapIngressDscp,
       "sleV2QoS4DscpMapIngressCos": sleV2QoS4DscpMapIngressCos,
       "sleV2QoS4DscpMapIngressColor": sleV2QoS4DscpMapIngressColor,
       "sleV2QoS4DscpMapIngressControl": sleV2QoS4DscpMapIngressControl,
       "sleV2QoS4DscpMapIngressControlRequest": sleV2QoS4DscpMapIngressControlRequest,
       "sleV2QoS4DscpMapIngressControlStatus": sleV2QoS4DscpMapIngressControlStatus,
       "sleV2QoS4DscpMapIngressControlTimer": sleV2QoS4DscpMapIngressControlTimer,
       "sleV2QoS4DscpMapIngressControlTimeStamp": sleV2QoS4DscpMapIngressControlTimeStamp,
       "sleV2QoS4DscpMapIngressControlReqResult": sleV2QoS4DscpMapIngressControlReqResult,
       "sleV2QoS4DscpMapIngressControlDscpIndex": sleV2QoS4DscpMapIngressControlDscpIndex,
       "sleV2QoS4DscpMapIngressControlDscp": sleV2QoS4DscpMapIngressControlDscp,
       "sleV2QoS4DscpMapIngressControlCos": sleV2QoS4DscpMapIngressControlCos,
       "sleV2QoS4DscpMapIngressControlColor": sleV2QoS4DscpMapIngressControlColor,
       "sleV2QoS4DscpMapIngressNotification": sleV2QoS4DscpMapIngressNotification,
       "sleV2QoS4DscpMapIngressChanged": sleV2QoS4DscpMapIngressChanged,
       "sleV2QoS4DscpMapTunnel": sleV2QoS4DscpMapTunnel,
       "sleV2QoS4DscpMapTunnelTable": sleV2QoS4DscpMapTunnelTable,
       "sleV2QoS4DscpMapTunnelEntry": sleV2QoS4DscpMapTunnelEntry,
       "sleV2QoS4DscpMapTunnelPriority": sleV2QoS4DscpMapTunnelPriority,
       "sleV2QoS4DscpMapTunnelColor": sleV2QoS4DscpMapTunnelColor,
       "sleV2QoS4DscpMapTunnelDscp": sleV2QoS4DscpMapTunnelDscp,
       "sleV2QoS4DscpMapTunnelControl": sleV2QoS4DscpMapTunnelControl,
       "sleV2QoS4DscpMapTunnelControlRequest": sleV2QoS4DscpMapTunnelControlRequest,
       "sleV2QoS4DscpMapTunnelControlStatus": sleV2QoS4DscpMapTunnelControlStatus,
       "sleV2QoS4DscpMapTunnelControlTimer": sleV2QoS4DscpMapTunnelControlTimer,
       "sleV2QoS4DscpMapTunnelControlTimeStamp": sleV2QoS4DscpMapTunnelControlTimeStamp,
       "sleV2QoS4DscpMapTunnelControlReqResult": sleV2QoS4DscpMapTunnelControlReqResult,
       "sleV2QoS4DscpMapTunnelControlPriority": sleV2QoS4DscpMapTunnelControlPriority,
       "sleV2QoS4DscpMapTunnelControlColor": sleV2QoS4DscpMapTunnelControlColor,
       "sleV2QoS4DscpMapTunnelControlDscp": sleV2QoS4DscpMapTunnelControlDscp,
       "sleV2QoS4DscpMapTunnelNotification": sleV2QoS4DscpMapTunnelNotification,
       "sleV2QoS4DscpMapTunnelChanged": sleV2QoS4DscpMapTunnelChanged,
       "sleV2QoS6": sleV2QoS6,
       "sleV2QoSGroup": sleV2QoSGroup,
       "sleV2QoSNotificationGroup": sleV2QoSNotificationGroup}
)
