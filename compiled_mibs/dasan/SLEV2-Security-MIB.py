# SNMP MIB module (SLEV2-Security-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLEV2-Security-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:14 2025
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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

sleV2Security = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7)
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





class IntIpAddrMask(Integer32):
    """Custom type IntIpAddrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("nothing", -1),
          ("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
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





class IntPermit(Integer32):
    """Custom type IntPermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2),
          ("none", 3))
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

_SleV2SecurityBase_ObjectIdentity = ObjectIdentity
sleV2SecurityBase = _SleV2SecurityBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 1)
)
_SleVSecurity4_ObjectIdentity = ObjectIdentity
sleVSecurity4 = _SleVSecurity4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2)
)
_SleV2SecurityACL_ObjectIdentity = ObjectIdentity
sleV2SecurityACL = _SleV2SecurityACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5)
)
_SleV2Security4ACLBase_ObjectIdentity = ObjectIdentity
sleV2Security4ACLBase = _SleV2Security4ACLBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 1)
)
_SleV2Security4ACLFlow_ObjectIdentity = ObjectIdentity
sleV2Security4ACLFlow = _SleV2Security4ACLFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2)
)
_SleV2Security4ACLFlowInfo_ObjectIdentity = ObjectIdentity
sleV2Security4ACLFlowInfo = _SleV2Security4ACLFlowInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1)
)
_SleV2Security4ACLFlowTable_Object = MibTable
sleV2Security4ACLFlowTable = _SleV2Security4ACLFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowTable.setStatus("current")
_SleV2Security4ACLFlowEntry_Object = MibTableRow
sleV2Security4ACLFlowEntry = _SleV2Security4ACLFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1)
)
sleV2Security4ACLFlowEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLFlowIndex"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowEntry.setStatus("current")


class _SleV2Security4ACLFlowIndex_Type(Integer32):
    """Custom type sleV2Security4ACLFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SleV2Security4ACLFlowIndex_Type.__name__ = "Integer32"
_SleV2Security4ACLFlowIndex_Object = MibTableColumn
sleV2Security4ACLFlowIndex = _SleV2Security4ACLFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 1),
    _SleV2Security4ACLFlowIndex_Type()
)
sleV2Security4ACLFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowIndex.setStatus("current")
_SleV2Security4ACLFlowName_Type = OctetName
_SleV2Security4ACLFlowName_Object = MibTableColumn
sleV2Security4ACLFlowName = _SleV2Security4ACLFlowName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 2),
    _SleV2Security4ACLFlowName_Type()
)
sleV2Security4ACLFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowName.setStatus("current")
_SleV2Security4ACLFlowSrcIpAddr_Type = IpAddress
_SleV2Security4ACLFlowSrcIpAddr_Object = MibTableColumn
sleV2Security4ACLFlowSrcIpAddr = _SleV2Security4ACLFlowSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 3),
    _SleV2Security4ACLFlowSrcIpAddr_Type()
)
sleV2Security4ACLFlowSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowSrcIpAddr.setStatus("current")
_SleV2Security4ACLFlowSrcIpAddrMask_Type = IntIpAddrMask
_SleV2Security4ACLFlowSrcIpAddrMask_Object = MibTableColumn
sleV2Security4ACLFlowSrcIpAddrMask = _SleV2Security4ACLFlowSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 4),
    _SleV2Security4ACLFlowSrcIpAddrMask_Type()
)
sleV2Security4ACLFlowSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowSrcIpAddrMask.setStatus("current")
_SleV2Security4ACLFlowDstIpAddr_Type = IpAddress
_SleV2Security4ACLFlowDstIpAddr_Object = MibTableColumn
sleV2Security4ACLFlowDstIpAddr = _SleV2Security4ACLFlowDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 5),
    _SleV2Security4ACLFlowDstIpAddr_Type()
)
sleV2Security4ACLFlowDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowDstIpAddr.setStatus("current")
_SleV2Security4ACLFlowDstIpAddrMask_Type = IntIpAddrMask
_SleV2Security4ACLFlowDstIpAddrMask_Object = MibTableColumn
sleV2Security4ACLFlowDstIpAddrMask = _SleV2Security4ACLFlowDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 6),
    _SleV2Security4ACLFlowDstIpAddrMask_Type()
)
sleV2Security4ACLFlowDstIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowDstIpAddrMask.setStatus("current")
_SleV2Security4ACLFlowProtocolType_Type = IntProtocolType
_SleV2Security4ACLFlowProtocolType_Object = MibTableColumn
sleV2Security4ACLFlowProtocolType = _SleV2Security4ACLFlowProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 7),
    _SleV2Security4ACLFlowProtocolType_Type()
)
sleV2Security4ACLFlowProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowProtocolType.setStatus("current")
_SleV2Security4ACLFlowTcpSrcStartPort_Type = IntL4Port
_SleV2Security4ACLFlowTcpSrcStartPort_Object = MibTableColumn
sleV2Security4ACLFlowTcpSrcStartPort = _SleV2Security4ACLFlowTcpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 8),
    _SleV2Security4ACLFlowTcpSrcStartPort_Type()
)
sleV2Security4ACLFlowTcpSrcStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowTcpSrcStartPort.setStatus("current")
_SleV2Security4ACLFlowTcpSrcEndPort_Type = IntL4Port
_SleV2Security4ACLFlowTcpSrcEndPort_Object = MibTableColumn
sleV2Security4ACLFlowTcpSrcEndPort = _SleV2Security4ACLFlowTcpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 9),
    _SleV2Security4ACLFlowTcpSrcEndPort_Type()
)
sleV2Security4ACLFlowTcpSrcEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowTcpSrcEndPort.setStatus("current")
_SleV2Security4ACLFlowTcpDstStartPort_Type = IntL4Port
_SleV2Security4ACLFlowTcpDstStartPort_Object = MibTableColumn
sleV2Security4ACLFlowTcpDstStartPort = _SleV2Security4ACLFlowTcpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 10),
    _SleV2Security4ACLFlowTcpDstStartPort_Type()
)
sleV2Security4ACLFlowTcpDstStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowTcpDstStartPort.setStatus("current")
_SleV2Security4ACLFlowTcpDstEndPort_Type = IntL4Port
_SleV2Security4ACLFlowTcpDstEndPort_Object = MibTableColumn
sleV2Security4ACLFlowTcpDstEndPort = _SleV2Security4ACLFlowTcpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 11),
    _SleV2Security4ACLFlowTcpDstEndPort_Type()
)
sleV2Security4ACLFlowTcpDstEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowTcpDstEndPort.setStatus("current")


class _SleV2Security4ACLFlowTcpFlag_Type(Bits):
    """Custom type sleV2Security4ACLFlowTcpFlag based on Bits"""
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

_SleV2Security4ACLFlowTcpFlag_Type.__name__ = "Bits"
_SleV2Security4ACLFlowTcpFlag_Object = MibTableColumn
sleV2Security4ACLFlowTcpFlag = _SleV2Security4ACLFlowTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 12),
    _SleV2Security4ACLFlowTcpFlag_Type()
)
sleV2Security4ACLFlowTcpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowTcpFlag.setStatus("current")
_SleV2Security4ACLFlowUdpSrcStartPort_Type = IntL4Port
_SleV2Security4ACLFlowUdpSrcStartPort_Object = MibTableColumn
sleV2Security4ACLFlowUdpSrcStartPort = _SleV2Security4ACLFlowUdpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 13),
    _SleV2Security4ACLFlowUdpSrcStartPort_Type()
)
sleV2Security4ACLFlowUdpSrcStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowUdpSrcStartPort.setStatus("current")
_SleV2Security4ACLFlowUdpSrcEndPort_Type = IntL4Port
_SleV2Security4ACLFlowUdpSrcEndPort_Object = MibTableColumn
sleV2Security4ACLFlowUdpSrcEndPort = _SleV2Security4ACLFlowUdpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 14),
    _SleV2Security4ACLFlowUdpSrcEndPort_Type()
)
sleV2Security4ACLFlowUdpSrcEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowUdpSrcEndPort.setStatus("current")
_SleV2Security4ACLFlowUdpDstStartPort_Type = IntL4Port
_SleV2Security4ACLFlowUdpDstStartPort_Object = MibTableColumn
sleV2Security4ACLFlowUdpDstStartPort = _SleV2Security4ACLFlowUdpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 15),
    _SleV2Security4ACLFlowUdpDstStartPort_Type()
)
sleV2Security4ACLFlowUdpDstStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowUdpDstStartPort.setStatus("current")
_SleV2Security4ACLFlowUdpDstEndPort_Type = IntL4Port
_SleV2Security4ACLFlowUdpDstEndPort_Object = MibTableColumn
sleV2Security4ACLFlowUdpDstEndPort = _SleV2Security4ACLFlowUdpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 16),
    _SleV2Security4ACLFlowUdpDstEndPort_Type()
)
sleV2Security4ACLFlowUdpDstEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowUdpDstEndPort.setStatus("current")
_SleV2Security4ACLFlowIcmpType_Type = IntIcmpType
_SleV2Security4ACLFlowIcmpType_Object = MibTableColumn
sleV2Security4ACLFlowIcmpType = _SleV2Security4ACLFlowIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 17),
    _SleV2Security4ACLFlowIcmpType_Type()
)
sleV2Security4ACLFlowIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowIcmpType.setStatus("current")
_SleV2Security4ACLFlowIcmpCode_Type = IntIcmpCode
_SleV2Security4ACLFlowIcmpCode_Object = MibTableColumn
sleV2Security4ACLFlowIcmpCode = _SleV2Security4ACLFlowIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 18),
    _SleV2Security4ACLFlowIcmpCode_Type()
)
sleV2Security4ACLFlowIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowIcmpCode.setStatus("current")


class _SleV2Security4ACLFlowHdrlen_Type(Integer32):
    """Custom type sleV2Security4ACLFlowHdrlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_SleV2Security4ACLFlowHdrlen_Type.__name__ = "Integer32"
_SleV2Security4ACLFlowHdrlen_Object = MibTableColumn
sleV2Security4ACLFlowHdrlen = _SleV2Security4ACLFlowHdrlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 19),
    _SleV2Security4ACLFlowHdrlen_Type()
)
sleV2Security4ACLFlowHdrlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowHdrlen.setStatus("current")


class _SleV2Security4ACLFlowIpFlag_Type(Integer32):
    """Custom type sleV2Security4ACLFlowIpFlag based on Integer32"""
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


_SleV2Security4ACLFlowIpFlag_Type.__name__ = "Integer32"
_SleV2Security4ACLFlowIpFlag_Object = MibTableColumn
sleV2Security4ACLFlowIpFlag = _SleV2Security4ACLFlowIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 20),
    _SleV2Security4ACLFlowIpFlag_Type()
)
sleV2Security4ACLFlowIpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowIpFlag.setStatus("current")
_SleV2SecurityACLFlowInetAddrType_Type = InetAddressType
_SleV2SecurityACLFlowInetAddrType_Object = MibTableColumn
sleV2SecurityACLFlowInetAddrType = _SleV2SecurityACLFlowInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 21),
    _SleV2SecurityACLFlowInetAddrType_Type()
)
sleV2SecurityACLFlowInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowInetAddrType.setStatus("current")
_SleV2SecurityACLFlowSrcInetAddr_Type = InetAddress
_SleV2SecurityACLFlowSrcInetAddr_Object = MibTableColumn
sleV2SecurityACLFlowSrcInetAddr = _SleV2SecurityACLFlowSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 22),
    _SleV2SecurityACLFlowSrcInetAddr_Type()
)
sleV2SecurityACLFlowSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowSrcInetAddr.setStatus("current")
_SleV2SecurityACLFlowDstInetAddr_Type = InetAddress
_SleV2SecurityACLFlowDstInetAddr_Object = MibTableColumn
sleV2SecurityACLFlowDstInetAddr = _SleV2SecurityACLFlowDstInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 23),
    _SleV2SecurityACLFlowDstInetAddr_Type()
)
sleV2SecurityACLFlowDstInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowDstInetAddr.setStatus("current")
_SleV2SecurityACLFlowSrcInetAddrLen_Type = InetAddressPrefixLength
_SleV2SecurityACLFlowSrcInetAddrLen_Object = MibTableColumn
sleV2SecurityACLFlowSrcInetAddrLen = _SleV2SecurityACLFlowSrcInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 24),
    _SleV2SecurityACLFlowSrcInetAddrLen_Type()
)
sleV2SecurityACLFlowSrcInetAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowSrcInetAddrLen.setStatus("current")
_SleV2SecurityACLFlowDstInetAddrLen_Type = InetAddressPrefixLength
_SleV2SecurityACLFlowDstInetAddrLen_Object = MibTableColumn
sleV2SecurityACLFlowDstInetAddrLen = _SleV2SecurityACLFlowDstInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 1, 1, 25),
    _SleV2SecurityACLFlowDstInetAddrLen_Type()
)
sleV2SecurityACLFlowDstInetAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowDstInetAddrLen.setStatus("current")
_SleV2Security4ACLFlowControl_ObjectIdentity = ObjectIdentity
sleV2Security4ACLFlowControl = _SleV2Security4ACLFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2)
)


class _SleV2Security4ACLFlowControlRequest_Type(Integer32):
    """Custom type sleV2Security4ACLFlowControlRequest based on Integer32"""
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
        *(("createFlow", 1),
          ("modifyFlow", 2),
          ("destroyFlow", 3),
          ("destroyAllFlow", 4),
          ("createFlowEx", 5),
          ("setFlowEx", 6))
    )


_SleV2Security4ACLFlowControlRequest_Type.__name__ = "Integer32"
_SleV2Security4ACLFlowControlRequest_Object = MibScalar
sleV2Security4ACLFlowControlRequest = _SleV2Security4ACLFlowControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 1),
    _SleV2Security4ACLFlowControlRequest_Type()
)
sleV2Security4ACLFlowControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlRequest.setStatus("current")
_SleV2Security4ACLFlowControlStatus_Type = SleControlStatusType
_SleV2Security4ACLFlowControlStatus_Object = MibScalar
sleV2Security4ACLFlowControlStatus = _SleV2Security4ACLFlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 2),
    _SleV2Security4ACLFlowControlStatus_Type()
)
sleV2Security4ACLFlowControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlStatus.setStatus("current")
_SleV2Security4ACLFlowControlTimer_Type = Gauge32
_SleV2Security4ACLFlowControlTimer_Object = MibScalar
sleV2Security4ACLFlowControlTimer = _SleV2Security4ACLFlowControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 3),
    _SleV2Security4ACLFlowControlTimer_Type()
)
sleV2Security4ACLFlowControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlTimer.setStatus("current")
_SleV2Security4ACLFlowControlTimeStamp_Type = TimeTicks
_SleV2Security4ACLFlowControlTimeStamp_Object = MibScalar
sleV2Security4ACLFlowControlTimeStamp = _SleV2Security4ACLFlowControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 4),
    _SleV2Security4ACLFlowControlTimeStamp_Type()
)
sleV2Security4ACLFlowControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlTimeStamp.setStatus("current")
_SleV2Security4ACLFlowControlReqResult_Type = SleControlRequestResultType
_SleV2Security4ACLFlowControlReqResult_Object = MibScalar
sleV2Security4ACLFlowControlReqResult = _SleV2Security4ACLFlowControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 5),
    _SleV2Security4ACLFlowControlReqResult_Type()
)
sleV2Security4ACLFlowControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlReqResult.setStatus("current")
_SleV2Security4ACLFlowControlIndex_Type = IntFlowIndex
_SleV2Security4ACLFlowControlIndex_Object = MibScalar
sleV2Security4ACLFlowControlIndex = _SleV2Security4ACLFlowControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 6),
    _SleV2Security4ACLFlowControlIndex_Type()
)
sleV2Security4ACLFlowControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlIndex.setStatus("current")
_SleV2Security4ACLFlowControlName_Type = OctetName
_SleV2Security4ACLFlowControlName_Object = MibScalar
sleV2Security4ACLFlowControlName = _SleV2Security4ACLFlowControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 7),
    _SleV2Security4ACLFlowControlName_Type()
)
sleV2Security4ACLFlowControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlName.setStatus("current")
_SleV2Security4ACLFlowControlSrcIpAddr_Type = IpAddress
_SleV2Security4ACLFlowControlSrcIpAddr_Object = MibScalar
sleV2Security4ACLFlowControlSrcIpAddr = _SleV2Security4ACLFlowControlSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 8),
    _SleV2Security4ACLFlowControlSrcIpAddr_Type()
)
sleV2Security4ACLFlowControlSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlSrcIpAddr.setStatus("current")
_SleV2Security4ACLFlowControlSrcIpAddrMask_Type = IntIpAddrMask
_SleV2Security4ACLFlowControlSrcIpAddrMask_Object = MibScalar
sleV2Security4ACLFlowControlSrcIpAddrMask = _SleV2Security4ACLFlowControlSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 9),
    _SleV2Security4ACLFlowControlSrcIpAddrMask_Type()
)
sleV2Security4ACLFlowControlSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlSrcIpAddrMask.setStatus("current")
_SleV2Security4ACLFlowControlDstIpAddr_Type = IpAddress
_SleV2Security4ACLFlowControlDstIpAddr_Object = MibScalar
sleV2Security4ACLFlowControlDstIpAddr = _SleV2Security4ACLFlowControlDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 10),
    _SleV2Security4ACLFlowControlDstIpAddr_Type()
)
sleV2Security4ACLFlowControlDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlDstIpAddr.setStatus("current")
_SleV2Security4ACLFlowControlDstIpAddrMask_Type = IntIpAddrMask
_SleV2Security4ACLFlowControlDstIpAddrMask_Object = MibScalar
sleV2Security4ACLFlowControlDstIpAddrMask = _SleV2Security4ACLFlowControlDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 11),
    _SleV2Security4ACLFlowControlDstIpAddrMask_Type()
)
sleV2Security4ACLFlowControlDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlDstIpAddrMask.setStatus("current")
_SleV2Security4ACLFlowControlProtocolType_Type = IntProtocolType
_SleV2Security4ACLFlowControlProtocolType_Object = MibScalar
sleV2Security4ACLFlowControlProtocolType = _SleV2Security4ACLFlowControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 12),
    _SleV2Security4ACLFlowControlProtocolType_Type()
)
sleV2Security4ACLFlowControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlProtocolType.setStatus("current")
_SleV2Security4ACLFlowControlTcpSrcStartPort_Type = IntL4Port
_SleV2Security4ACLFlowControlTcpSrcStartPort_Object = MibScalar
sleV2Security4ACLFlowControlTcpSrcStartPort = _SleV2Security4ACLFlowControlTcpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 13),
    _SleV2Security4ACLFlowControlTcpSrcStartPort_Type()
)
sleV2Security4ACLFlowControlTcpSrcStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlTcpSrcStartPort.setStatus("current")
_SleV2Security4ACLFlowControlTcpSrcEndPort_Type = IntL4Port
_SleV2Security4ACLFlowControlTcpSrcEndPort_Object = MibScalar
sleV2Security4ACLFlowControlTcpSrcEndPort = _SleV2Security4ACLFlowControlTcpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 14),
    _SleV2Security4ACLFlowControlTcpSrcEndPort_Type()
)
sleV2Security4ACLFlowControlTcpSrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlTcpSrcEndPort.setStatus("current")
_SleV2Security4ACLFlowControlTcpDstStartPort_Type = IntL4Port
_SleV2Security4ACLFlowControlTcpDstStartPort_Object = MibScalar
sleV2Security4ACLFlowControlTcpDstStartPort = _SleV2Security4ACLFlowControlTcpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 15),
    _SleV2Security4ACLFlowControlTcpDstStartPort_Type()
)
sleV2Security4ACLFlowControlTcpDstStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlTcpDstStartPort.setStatus("current")
_SleV2Security4ACLFlowControlTcpDstEndPort_Type = IntL4Port
_SleV2Security4ACLFlowControlTcpDstEndPort_Object = MibScalar
sleV2Security4ACLFlowControlTcpDstEndPort = _SleV2Security4ACLFlowControlTcpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 16),
    _SleV2Security4ACLFlowControlTcpDstEndPort_Type()
)
sleV2Security4ACLFlowControlTcpDstEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlTcpDstEndPort.setStatus("current")


class _SleV2Security4ACLFlowControlTcpFlag_Type(Bits):
    """Custom type sleV2Security4ACLFlowControlTcpFlag based on Bits"""
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

_SleV2Security4ACLFlowControlTcpFlag_Type.__name__ = "Bits"
_SleV2Security4ACLFlowControlTcpFlag_Object = MibScalar
sleV2Security4ACLFlowControlTcpFlag = _SleV2Security4ACLFlowControlTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 17),
    _SleV2Security4ACLFlowControlTcpFlag_Type()
)
sleV2Security4ACLFlowControlTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlTcpFlag.setStatus("current")
_SleV2Security4ACLFlowControlUdpSrcStartPort_Type = IntL4Port
_SleV2Security4ACLFlowControlUdpSrcStartPort_Object = MibScalar
sleV2Security4ACLFlowControlUdpSrcStartPort = _SleV2Security4ACLFlowControlUdpSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 18),
    _SleV2Security4ACLFlowControlUdpSrcStartPort_Type()
)
sleV2Security4ACLFlowControlUdpSrcStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlUdpSrcStartPort.setStatus("current")
_SleV2Security4ACLFlowControlUdpSrcEndPort_Type = IntL4Port
_SleV2Security4ACLFlowControlUdpSrcEndPort_Object = MibScalar
sleV2Security4ACLFlowControlUdpSrcEndPort = _SleV2Security4ACLFlowControlUdpSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 19),
    _SleV2Security4ACLFlowControlUdpSrcEndPort_Type()
)
sleV2Security4ACLFlowControlUdpSrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlUdpSrcEndPort.setStatus("current")
_SleV2Security4ACLFlowControlUdpDstStartPort_Type = IntL4Port
_SleV2Security4ACLFlowControlUdpDstStartPort_Object = MibScalar
sleV2Security4ACLFlowControlUdpDstStartPort = _SleV2Security4ACLFlowControlUdpDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 20),
    _SleV2Security4ACLFlowControlUdpDstStartPort_Type()
)
sleV2Security4ACLFlowControlUdpDstStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlUdpDstStartPort.setStatus("current")
_SleV2Security4ACLFlowControlUdpDstEndPort_Type = IntL4Port
_SleV2Security4ACLFlowControlUdpDstEndPort_Object = MibScalar
sleV2Security4ACLFlowControlUdpDstEndPort = _SleV2Security4ACLFlowControlUdpDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 21),
    _SleV2Security4ACLFlowControlUdpDstEndPort_Type()
)
sleV2Security4ACLFlowControlUdpDstEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlUdpDstEndPort.setStatus("current")
_SleV2Security4ACLFlowControlIcmpType_Type = IntIcmpType
_SleV2Security4ACLFlowControlIcmpType_Object = MibScalar
sleV2Security4ACLFlowControlIcmpType = _SleV2Security4ACLFlowControlIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 22),
    _SleV2Security4ACLFlowControlIcmpType_Type()
)
sleV2Security4ACLFlowControlIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlIcmpType.setStatus("current")
_SleV2Security4ACLFlowControlIcmpCode_Type = IntIcmpCode
_SleV2Security4ACLFlowControlIcmpCode_Object = MibScalar
sleV2Security4ACLFlowControlIcmpCode = _SleV2Security4ACLFlowControlIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 23),
    _SleV2Security4ACLFlowControlIcmpCode_Type()
)
sleV2Security4ACLFlowControlIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlIcmpCode.setStatus("current")


class _SleV2Security4ACLFlowControlHdrlen_Type(Integer32):
    """Custom type sleV2Security4ACLFlowControlHdrlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_SleV2Security4ACLFlowControlHdrlen_Type.__name__ = "Integer32"
_SleV2Security4ACLFlowControlHdrlen_Object = MibScalar
sleV2Security4ACLFlowControlHdrlen = _SleV2Security4ACLFlowControlHdrlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 24),
    _SleV2Security4ACLFlowControlHdrlen_Type()
)
sleV2Security4ACLFlowControlHdrlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlHdrlen.setStatus("current")


class _SleV2Security4ACLFlowControlIpFlag_Type(Integer32):
    """Custom type sleV2Security4ACLFlowControlIpFlag based on Integer32"""
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


_SleV2Security4ACLFlowControlIpFlag_Type.__name__ = "Integer32"
_SleV2Security4ACLFlowControlIpFlag_Object = MibScalar
sleV2Security4ACLFlowControlIpFlag = _SleV2Security4ACLFlowControlIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 25),
    _SleV2Security4ACLFlowControlIpFlag_Type()
)
sleV2Security4ACLFlowControlIpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowControlIpFlag.setStatus("current")
_SleV2SecurityACLFlowControlInetAddrType_Type = InetAddressType
_SleV2SecurityACLFlowControlInetAddrType_Object = MibScalar
sleV2SecurityACLFlowControlInetAddrType = _SleV2SecurityACLFlowControlInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 26),
    _SleV2SecurityACLFlowControlInetAddrType_Type()
)
sleV2SecurityACLFlowControlInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowControlInetAddrType.setStatus("current")
_SleV2SecurityACLFlowControlSrcInetAddr_Type = InetAddress
_SleV2SecurityACLFlowControlSrcInetAddr_Object = MibScalar
sleV2SecurityACLFlowControlSrcInetAddr = _SleV2SecurityACLFlowControlSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 27),
    _SleV2SecurityACLFlowControlSrcInetAddr_Type()
)
sleV2SecurityACLFlowControlSrcInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowControlSrcInetAddr.setStatus("current")
_SleV2SecurityACLFlowControlDstInetAddr_Type = InetAddress
_SleV2SecurityACLFlowControlDstInetAddr_Object = MibScalar
sleV2SecurityACLFlowControlDstInetAddr = _SleV2SecurityACLFlowControlDstInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 28),
    _SleV2SecurityACLFlowControlDstInetAddr_Type()
)
sleV2SecurityACLFlowControlDstInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowControlDstInetAddr.setStatus("current")
_SleV2SecurityACLFlowControlSrcInetAddrLen_Type = InetAddressPrefixLength
_SleV2SecurityACLFlowControlSrcInetAddrLen_Object = MibScalar
sleV2SecurityACLFlowControlSrcInetAddrLen = _SleV2SecurityACLFlowControlSrcInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 29),
    _SleV2SecurityACLFlowControlSrcInetAddrLen_Type()
)
sleV2SecurityACLFlowControlSrcInetAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowControlSrcInetAddrLen.setStatus("current")
_SleV2SecurityACLFlowControlDstInetAddrLen_Type = InetAddressPrefixLength
_SleV2SecurityACLFlowControlDstInetAddrLen_Object = MibScalar
sleV2SecurityACLFlowControlDstInetAddrLen = _SleV2SecurityACLFlowControlDstInetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 2, 30),
    _SleV2SecurityACLFlowControlDstInetAddrLen_Type()
)
sleV2SecurityACLFlowControlDstInetAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLFlowControlDstInetAddrLen.setStatus("current")
_SleV2Security4ACLFlowNotification_ObjectIdentity = ObjectIdentity
sleV2Security4ACLFlowNotification = _SleV2Security4ACLFlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 3)
)
_SleV2Security4ACLFlowClass_ObjectIdentity = ObjectIdentity
sleV2Security4ACLFlowClass = _SleV2Security4ACLFlowClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 2)
)
_SleV2Security4ACLFlowClassTable_Object = MibTable
sleV2Security4ACLFlowClassTable = _SleV2Security4ACLFlowClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowClassTable.setStatus("current")
_SleV2Security4ACLFlowClassEntry_Object = MibTableRow
sleV2Security4ACLFlowClassEntry = _SleV2Security4ACLFlowClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 2, 1, 1)
)
sleV2Security4ACLFlowClassEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLFlowIndex"),
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLFlowClassIndex"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowClassEntry.setStatus("current")
_SleV2Security4ACLFlowClassIndex_Type = IntClassIndex
_SleV2Security4ACLFlowClassIndex_Object = MibTableColumn
sleV2Security4ACLFlowClassIndex = _SleV2Security4ACLFlowClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 2, 1, 1, 1),
    _SleV2Security4ACLFlowClassIndex_Type()
)
sleV2Security4ACLFlowClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowClassIndex.setStatus("current")
_SleV2Security4ACLFlowClassID_Type = IntClassIndex
_SleV2Security4ACLFlowClassID_Object = MibTableColumn
sleV2Security4ACLFlowClassID = _SleV2Security4ACLFlowClassID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 2, 1, 1, 2),
    _SleV2Security4ACLFlowClassID_Type()
)
sleV2Security4ACLFlowClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowClassID.setStatus("current")
_SleV2Security4ACLFlowClassName_Type = OctetName
_SleV2Security4ACLFlowClassName_Object = MibTableColumn
sleV2Security4ACLFlowClassName = _SleV2Security4ACLFlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 2, 1, 1, 3),
    _SleV2Security4ACLFlowClassName_Type()
)
sleV2Security4ACLFlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowClassName.setStatus("current")
_SleV2Security4ACLFlowPolicy_ObjectIdentity = ObjectIdentity
sleV2Security4ACLFlowPolicy = _SleV2Security4ACLFlowPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 3)
)
_SleV2QoS4ACLFlowPolicyTable_Object = MibTable
sleV2QoS4ACLFlowPolicyTable = _SleV2QoS4ACLFlowPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2QoS4ACLFlowPolicyTable.setStatus("current")
_SleV2QoS4ACLFlowPolicyEntry_Object = MibTableRow
sleV2QoS4ACLFlowPolicyEntry = _SleV2QoS4ACLFlowPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 3, 1, 1)
)
sleV2QoS4ACLFlowPolicyEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLFlowIndex"),
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLFlowPolicyIndex"),
)
if mibBuilder.loadTexts:
    sleV2QoS4ACLFlowPolicyEntry.setStatus("current")
_SleV2Security4ACLFlowPolicyIndex_Type = IntPolicyIndex
_SleV2Security4ACLFlowPolicyIndex_Object = MibTableColumn
sleV2Security4ACLFlowPolicyIndex = _SleV2Security4ACLFlowPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 3, 1, 1, 1),
    _SleV2Security4ACLFlowPolicyIndex_Type()
)
sleV2Security4ACLFlowPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowPolicyIndex.setStatus("current")
_SleV2Security4ACLFlowPolicyID_Type = IntPolicyIndex
_SleV2Security4ACLFlowPolicyID_Object = MibTableColumn
sleV2Security4ACLFlowPolicyID = _SleV2Security4ACLFlowPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 3, 1, 1, 2),
    _SleV2Security4ACLFlowPolicyID_Type()
)
sleV2Security4ACLFlowPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowPolicyID.setStatus("current")
_SleV2Security4ACLFlowPolicyName_Type = OctetName
_SleV2Security4ACLFlowPolicyName_Object = MibTableColumn
sleV2Security4ACLFlowPolicyName = _SleV2Security4ACLFlowPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 3, 1, 1, 3),
    _SleV2Security4ACLFlowPolicyName_Type()
)
sleV2Security4ACLFlowPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLFlowPolicyName.setStatus("current")
_SleV2Security4ACLClass_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClass = _SleV2Security4ACLClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3)
)
_SleV2Security4ACLClassInfo_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClassInfo = _SleV2Security4ACLClassInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1)
)
_SleV2Security4ACLClassTable_Object = MibTable
sleV2Security4ACLClassTable = _SleV2Security4ACLClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLClassTable.setStatus("current")
_SleV2Security4ACLClassEntry_Object = MibTableRow
sleV2Security4ACLClassEntry = _SleV2Security4ACLClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 1, 1)
)
sleV2Security4ACLClassEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLClassIndex"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLClassEntry.setStatus("current")
_SleV2Security4ACLClassIndex_Type = IntClassIndex
_SleV2Security4ACLClassIndex_Object = MibTableColumn
sleV2Security4ACLClassIndex = _SleV2Security4ACLClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 1, 1, 1),
    _SleV2Security4ACLClassIndex_Type()
)
sleV2Security4ACLClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassIndex.setStatus("current")
_SleV2Security4ACLClassName_Type = OctetName
_SleV2Security4ACLClassName_Object = MibTableColumn
sleV2Security4ACLClassName = _SleV2Security4ACLClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 1, 1, 2),
    _SleV2Security4ACLClassName_Type()
)
sleV2Security4ACLClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassName.setStatus("current")
_SleV2Security4ACLClassFlowCnt_Type = Counter32
_SleV2Security4ACLClassFlowCnt_Object = MibTableColumn
sleV2Security4ACLClassFlowCnt = _SleV2Security4ACLClassFlowCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 1, 1, 3),
    _SleV2Security4ACLClassFlowCnt_Type()
)
sleV2Security4ACLClassFlowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowCnt.setStatus("current")
_SleV2Security4ACLClassControl_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClassControl = _SleV2Security4ACLClassControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2)
)


class _SleV2Security4ACLClassControlRequest_Type(Integer32):
    """Custom type sleV2Security4ACLClassControlRequest based on Integer32"""
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


_SleV2Security4ACLClassControlRequest_Type.__name__ = "Integer32"
_SleV2Security4ACLClassControlRequest_Object = MibScalar
sleV2Security4ACLClassControlRequest = _SleV2Security4ACLClassControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2, 1),
    _SleV2Security4ACLClassControlRequest_Type()
)
sleV2Security4ACLClassControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassControlRequest.setStatus("current")
_SleV2Security4ACLClassControlStatus_Type = SleControlStatusType
_SleV2Security4ACLClassControlStatus_Object = MibScalar
sleV2Security4ACLClassControlStatus = _SleV2Security4ACLClassControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2, 2),
    _SleV2Security4ACLClassControlStatus_Type()
)
sleV2Security4ACLClassControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassControlStatus.setStatus("current")
_SleV2Security4ACLClassControlTimer_Type = Gauge32
_SleV2Security4ACLClassControlTimer_Object = MibScalar
sleV2Security4ACLClassControlTimer = _SleV2Security4ACLClassControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2, 3),
    _SleV2Security4ACLClassControlTimer_Type()
)
sleV2Security4ACLClassControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassControlTimer.setStatus("current")
_SleV2Security4ACLClassControlTimeStamp_Type = TimeTicks
_SleV2Security4ACLClassControlTimeStamp_Object = MibScalar
sleV2Security4ACLClassControlTimeStamp = _SleV2Security4ACLClassControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2, 4),
    _SleV2Security4ACLClassControlTimeStamp_Type()
)
sleV2Security4ACLClassControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassControlTimeStamp.setStatus("current")
_SleV2Security4ACLClassControlReqResult_Type = SleControlRequestResultType
_SleV2Security4ACLClassControlReqResult_Object = MibScalar
sleV2Security4ACLClassControlReqResult = _SleV2Security4ACLClassControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2, 5),
    _SleV2Security4ACLClassControlReqResult_Type()
)
sleV2Security4ACLClassControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassControlReqResult.setStatus("current")
_SleV2Security4ACLClassControlIndex_Type = IntClassIndex
_SleV2Security4ACLClassControlIndex_Object = MibScalar
sleV2Security4ACLClassControlIndex = _SleV2Security4ACLClassControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2, 6),
    _SleV2Security4ACLClassControlIndex_Type()
)
sleV2Security4ACLClassControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassControlIndex.setStatus("current")
_SleV2Security4ACLClassControlName_Type = OctetName
_SleV2Security4ACLClassControlName_Object = MibScalar
sleV2Security4ACLClassControlName = _SleV2Security4ACLClassControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 2, 7),
    _SleV2Security4ACLClassControlName_Type()
)
sleV2Security4ACLClassControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassControlName.setStatus("current")
_SleV2Security4ACLClassNotification_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClassNotification = _SleV2Security4ACLClassNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 3)
)
_SleV2Security4ACLClassFlow_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClassFlow = _SleV2Security4ACLClassFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2)
)
_SleV2Security4ACLClassFlowTable_Object = MibTable
sleV2Security4ACLClassFlowTable = _SleV2Security4ACLClassFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowTable.setStatus("current")
_SleV2Security4ACLClassFlowEntry_Object = MibTableRow
sleV2Security4ACLClassFlowEntry = _SleV2Security4ACLClassFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 1, 1)
)
sleV2Security4ACLClassFlowEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLClassIndex"),
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLClassFlowIndex"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowEntry.setStatus("current")
_SleV2Security4ACLClassFlowIndex_Type = IntFlowIndex
_SleV2Security4ACLClassFlowIndex_Object = MibTableColumn
sleV2Security4ACLClassFlowIndex = _SleV2Security4ACLClassFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 1, 1, 1),
    _SleV2Security4ACLClassFlowIndex_Type()
)
sleV2Security4ACLClassFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowIndex.setStatus("current")
_SleV2Security4ACLClassFlowID_Type = IntFlowIndex
_SleV2Security4ACLClassFlowID_Object = MibTableColumn
sleV2Security4ACLClassFlowID = _SleV2Security4ACLClassFlowID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 1, 1, 2),
    _SleV2Security4ACLClassFlowID_Type()
)
sleV2Security4ACLClassFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowID.setStatus("current")
_SleV2Security4ACLClassFlowName_Type = OctetName
_SleV2Security4ACLClassFlowName_Object = MibTableColumn
sleV2Security4ACLClassFlowName = _SleV2Security4ACLClassFlowName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 1, 1, 3),
    _SleV2Security4ACLClassFlowName_Type()
)
sleV2Security4ACLClassFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowName.setStatus("current")
_SleV2Security4ACLClassFlowClassName_Type = OctetName
_SleV2Security4ACLClassFlowClassName_Object = MibTableColumn
sleV2Security4ACLClassFlowClassName = _SleV2Security4ACLClassFlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 1, 1, 4),
    _SleV2Security4ACLClassFlowClassName_Type()
)
sleV2Security4ACLClassFlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowClassName.setStatus("current")
_SleV2Security4ACLClassFlowControl_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClassFlowControl = _SleV2Security4ACLClassFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2)
)


class _SleV2Security4ACLClassFlowControlRequest_Type(Integer32):
    """Custom type sleV2Security4ACLClassFlowControlRequest based on Integer32"""
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


_SleV2Security4ACLClassFlowControlRequest_Type.__name__ = "Integer32"
_SleV2Security4ACLClassFlowControlRequest_Object = MibScalar
sleV2Security4ACLClassFlowControlRequest = _SleV2Security4ACLClassFlowControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 1),
    _SleV2Security4ACLClassFlowControlRequest_Type()
)
sleV2Security4ACLClassFlowControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlRequest.setStatus("current")
_SleV2Security4ACLClassFlowControlStatus_Type = SleControlStatusType
_SleV2Security4ACLClassFlowControlStatus_Object = MibScalar
sleV2Security4ACLClassFlowControlStatus = _SleV2Security4ACLClassFlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 2),
    _SleV2Security4ACLClassFlowControlStatus_Type()
)
sleV2Security4ACLClassFlowControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlStatus.setStatus("current")
_SleV2Security4ACLClassFlowControlTimer_Type = Gauge32
_SleV2Security4ACLClassFlowControlTimer_Object = MibScalar
sleV2Security4ACLClassFlowControlTimer = _SleV2Security4ACLClassFlowControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 3),
    _SleV2Security4ACLClassFlowControlTimer_Type()
)
sleV2Security4ACLClassFlowControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlTimer.setStatus("current")
_SleV2Security4ACLClassFlowControlTimeStamp_Type = TimeTicks
_SleV2Security4ACLClassFlowControlTimeStamp_Object = MibScalar
sleV2Security4ACLClassFlowControlTimeStamp = _SleV2Security4ACLClassFlowControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 4),
    _SleV2Security4ACLClassFlowControlTimeStamp_Type()
)
sleV2Security4ACLClassFlowControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlTimeStamp.setStatus("current")
_SleV2Security4ACLClassFlowControlReqResult_Type = SleControlRequestResultType
_SleV2Security4ACLClassFlowControlReqResult_Object = MibScalar
sleV2Security4ACLClassFlowControlReqResult = _SleV2Security4ACLClassFlowControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 5),
    _SleV2Security4ACLClassFlowControlReqResult_Type()
)
sleV2Security4ACLClassFlowControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlReqResult.setStatus("current")
_SleV2Security4ACLClassFlowControlClassIndex_Type = IntClassIndex
_SleV2Security4ACLClassFlowControlClassIndex_Object = MibScalar
sleV2Security4ACLClassFlowControlClassIndex = _SleV2Security4ACLClassFlowControlClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 6),
    _SleV2Security4ACLClassFlowControlClassIndex_Type()
)
sleV2Security4ACLClassFlowControlClassIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlClassIndex.setStatus("current")
_SleV2Security4ACLClassFlowControlFlowIndex_Type = IntFlowIndex
_SleV2Security4ACLClassFlowControlFlowIndex_Object = MibScalar
sleV2Security4ACLClassFlowControlFlowIndex = _SleV2Security4ACLClassFlowControlFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 7),
    _SleV2Security4ACLClassFlowControlFlowIndex_Type()
)
sleV2Security4ACLClassFlowControlFlowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlFlowIndex.setStatus("current")
_SleV2Security4ACLClassFlowControlFlowID_Type = IntFlowIndex
_SleV2Security4ACLClassFlowControlFlowID_Object = MibScalar
sleV2Security4ACLClassFlowControlFlowID = _SleV2Security4ACLClassFlowControlFlowID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 8),
    _SleV2Security4ACLClassFlowControlFlowID_Type()
)
sleV2Security4ACLClassFlowControlFlowID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlFlowID.setStatus("current")
_SleV2Security4ACLClassFlowControlClassName_Type = OctetString
_SleV2Security4ACLClassFlowControlClassName_Object = MibScalar
sleV2Security4ACLClassFlowControlClassName = _SleV2Security4ACLClassFlowControlClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 2, 9),
    _SleV2Security4ACLClassFlowControlClassName_Type()
)
sleV2Security4ACLClassFlowControlClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassFlowControlClassName.setStatus("current")
_SleV2Security4ACLClassFlowNotification_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClassFlowNotification = _SleV2Security4ACLClassFlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 3)
)
_SleV2Security4ACLClassPolicy_ObjectIdentity = ObjectIdentity
sleV2Security4ACLClassPolicy = _SleV2Security4ACLClassPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 3)
)
_SleV2Security4ACLClassPolicyTable_Object = MibTable
sleV2Security4ACLClassPolicyTable = _SleV2Security4ACLClassPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLClassPolicyTable.setStatus("current")
_SleV2Security4ACLClassPolicyEntry_Object = MibTableRow
sleV2Security4ACLClassPolicyEntry = _SleV2Security4ACLClassPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 3, 1, 1)
)
sleV2Security4ACLClassPolicyEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLClassIndex"),
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLClassPolicyIndex"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLClassPolicyEntry.setStatus("current")
_SleV2Security4ACLClassPolicyIndex_Type = IntPolicyIndex
_SleV2Security4ACLClassPolicyIndex_Object = MibTableColumn
sleV2Security4ACLClassPolicyIndex = _SleV2Security4ACLClassPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 3, 1, 1, 1),
    _SleV2Security4ACLClassPolicyIndex_Type()
)
sleV2Security4ACLClassPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassPolicyIndex.setStatus("current")
_SleV2Security4ACLClassPolicyID_Type = IntPolicyIndex
_SleV2Security4ACLClassPolicyID_Object = MibTableColumn
sleV2Security4ACLClassPolicyID = _SleV2Security4ACLClassPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 3, 1, 1, 2),
    _SleV2Security4ACLClassPolicyID_Type()
)
sleV2Security4ACLClassPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassPolicyID.setStatus("current")
_SleV2Security4ACLClassPolicyName_Type = OctetName
_SleV2Security4ACLClassPolicyName_Object = MibTableColumn
sleV2Security4ACLClassPolicyName = _SleV2Security4ACLClassPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 3, 1, 1, 3),
    _SleV2Security4ACLClassPolicyName_Type()
)
sleV2Security4ACLClassPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLClassPolicyName.setStatus("current")
_SleV2Security4ACLPolicy_ObjectIdentity = ObjectIdentity
sleV2Security4ACLPolicy = _SleV2Security4ACLPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4)
)
_SleV2Security4ACLPolicyInfo_ObjectIdentity = ObjectIdentity
sleV2Security4ACLPolicyInfo = _SleV2Security4ACLPolicyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1)
)
_SleV2Security4ACLPolicyTable_Object = MibTable
sleV2Security4ACLPolicyTable = _SleV2Security4ACLPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyTable.setStatus("current")
_SleV2Security4ACLPolicyEntry_Object = MibTableRow
sleV2Security4ACLPolicyEntry = _SleV2Security4ACLPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1)
)
sleV2Security4ACLPolicyEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLPolicyIndex"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyEntry.setStatus("current")
_SleV2Security4ACLPolicyIndex_Type = IntPolicyIndex
_SleV2Security4ACLPolicyIndex_Object = MibTableColumn
sleV2Security4ACLPolicyIndex = _SleV2Security4ACLPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1, 1),
    _SleV2Security4ACLPolicyIndex_Type()
)
sleV2Security4ACLPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyIndex.setStatus("current")
_SleV2Security4ACLPolicyName_Type = OctetName
_SleV2Security4ACLPolicyName_Object = MibTableColumn
sleV2Security4ACLPolicyName = _SleV2Security4ACLPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1, 2),
    _SleV2Security4ACLPolicyName_Type()
)
sleV2Security4ACLPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyName.setStatus("current")
_SleV2Security4ACLPolicyFlowCnt_Type = Integer32
_SleV2Security4ACLPolicyFlowCnt_Object = MibTableColumn
sleV2Security4ACLPolicyFlowCnt = _SleV2Security4ACLPolicyFlowCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1, 3),
    _SleV2Security4ACLPolicyFlowCnt_Type()
)
sleV2Security4ACLPolicyFlowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowCnt.setStatus("current")
_SleV2Security4ACLPolicyClassCnt_Type = Integer32
_SleV2Security4ACLPolicyClassCnt_Object = MibTableColumn
sleV2Security4ACLPolicyClassCnt = _SleV2Security4ACLPolicyClassCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1, 4),
    _SleV2Security4ACLPolicyClassCnt_Type()
)
sleV2Security4ACLPolicyClassCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyClassCnt.setStatus("current")


class _SleV2Security4ACLPolicyPriority_Type(Integer32):
    """Custom type sleV2Security4ACLPolicyPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_SleV2Security4ACLPolicyPriority_Type.__name__ = "Integer32"
_SleV2Security4ACLPolicyPriority_Object = MibTableColumn
sleV2Security4ACLPolicyPriority = _SleV2Security4ACLPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1, 5),
    _SleV2Security4ACLPolicyPriority_Type()
)
sleV2Security4ACLPolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyPriority.setStatus("current")
_SleV2Security4ACLPolicyMatchFlag_Type = IntPermit
_SleV2Security4ACLPolicyMatchFlag_Object = MibTableColumn
sleV2Security4ACLPolicyMatchFlag = _SleV2Security4ACLPolicyMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1, 6),
    _SleV2Security4ACLPolicyMatchFlag_Type()
)
sleV2Security4ACLPolicyMatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyMatchFlag.setStatus("current")
_SleV2Security4ACLPolicyNomatchFlag_Type = IntPermit
_SleV2Security4ACLPolicyNomatchFlag_Object = MibTableColumn
sleV2Security4ACLPolicyNomatchFlag = _SleV2Security4ACLPolicyNomatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 1, 1, 7),
    _SleV2Security4ACLPolicyNomatchFlag_Type()
)
sleV2Security4ACLPolicyNomatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyNomatchFlag.setStatus("current")
_SleV2Security4ACLPolicyControl_ObjectIdentity = ObjectIdentity
sleV2Security4ACLPolicyControl = _SleV2Security4ACLPolicyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2)
)


class _SleV2Security4ACLPolicyControlRequest_Type(Integer32):
    """Custom type sleV2Security4ACLPolicyControlRequest based on Integer32"""
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
        *(("createPolicy", 1),
          ("setPolicyInfo", 2),
          ("setMatchAction", 3),
          ("setNomatchAction", 4),
          ("destroyPolicy", 5))
    )


_SleV2Security4ACLPolicyControlRequest_Type.__name__ = "Integer32"
_SleV2Security4ACLPolicyControlRequest_Object = MibScalar
sleV2Security4ACLPolicyControlRequest = _SleV2Security4ACLPolicyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 1),
    _SleV2Security4ACLPolicyControlRequest_Type()
)
sleV2Security4ACLPolicyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlRequest.setStatus("current")
_SleV2Security4ACLPolicyControlStatus_Type = SleControlStatusType
_SleV2Security4ACLPolicyControlStatus_Object = MibScalar
sleV2Security4ACLPolicyControlStatus = _SleV2Security4ACLPolicyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 2),
    _SleV2Security4ACLPolicyControlStatus_Type()
)
sleV2Security4ACLPolicyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlStatus.setStatus("current")
_SleV2Security4ACLPolicyControlTimer_Type = Gauge32
_SleV2Security4ACLPolicyControlTimer_Object = MibScalar
sleV2Security4ACLPolicyControlTimer = _SleV2Security4ACLPolicyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 3),
    _SleV2Security4ACLPolicyControlTimer_Type()
)
sleV2Security4ACLPolicyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlTimer.setStatus("current")
_SleV2Security4ACLPolicyControlTimeStamp_Type = TimeTicks
_SleV2Security4ACLPolicyControlTimeStamp_Object = MibScalar
sleV2Security4ACLPolicyControlTimeStamp = _SleV2Security4ACLPolicyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 4),
    _SleV2Security4ACLPolicyControlTimeStamp_Type()
)
sleV2Security4ACLPolicyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlTimeStamp.setStatus("current")
_SleV2Security4ACLPolicyControlReqResult_Type = SleControlRequestResultType
_SleV2Security4ACLPolicyControlReqResult_Object = MibScalar
sleV2Security4ACLPolicyControlReqResult = _SleV2Security4ACLPolicyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 5),
    _SleV2Security4ACLPolicyControlReqResult_Type()
)
sleV2Security4ACLPolicyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlReqResult.setStatus("current")
_SleV2Security4ACLPolicyControlIndex_Type = IntPolicyIndex
_SleV2Security4ACLPolicyControlIndex_Object = MibScalar
sleV2Security4ACLPolicyControlIndex = _SleV2Security4ACLPolicyControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 6),
    _SleV2Security4ACLPolicyControlIndex_Type()
)
sleV2Security4ACLPolicyControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlIndex.setStatus("current")
_SleV2Security4ACLPolicyControlName_Type = OctetName
_SleV2Security4ACLPolicyControlName_Object = MibScalar
sleV2Security4ACLPolicyControlName = _SleV2Security4ACLPolicyControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 7),
    _SleV2Security4ACLPolicyControlName_Type()
)
sleV2Security4ACLPolicyControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlName.setStatus("current")
_SleV2Security4ACLPolicyControlPriority_Type = IntRulePriority
_SleV2Security4ACLPolicyControlPriority_Object = MibScalar
sleV2Security4ACLPolicyControlPriority = _SleV2Security4ACLPolicyControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 8),
    _SleV2Security4ACLPolicyControlPriority_Type()
)
sleV2Security4ACLPolicyControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlPriority.setStatus("current")
_SleV2Security4ACLPolicyControlMatchFlag_Type = IntPermit
_SleV2Security4ACLPolicyControlMatchFlag_Object = MibScalar
sleV2Security4ACLPolicyControlMatchFlag = _SleV2Security4ACLPolicyControlMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 9),
    _SleV2Security4ACLPolicyControlMatchFlag_Type()
)
sleV2Security4ACLPolicyControlMatchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlMatchFlag.setStatus("current")
_SleV2Security4ACLPolicyControlNomatchFlag_Type = IntPermit
_SleV2Security4ACLPolicyControlNomatchFlag_Object = MibScalar
sleV2Security4ACLPolicyControlNomatchFlag = _SleV2Security4ACLPolicyControlNomatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 10),
    _SleV2Security4ACLPolicyControlNomatchFlag_Type()
)
sleV2Security4ACLPolicyControlNomatchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlNomatchFlag.setStatus("current")
_SleV2Security4ACLPolicyControlFlowID_Type = Integer32
_SleV2Security4ACLPolicyControlFlowID_Object = MibScalar
sleV2Security4ACLPolicyControlFlowID = _SleV2Security4ACLPolicyControlFlowID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 11),
    _SleV2Security4ACLPolicyControlFlowID_Type()
)
sleV2Security4ACLPolicyControlFlowID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlFlowID.setStatus("current")
_SleV2Security4ACLPolicyControlClassID_Type = Integer32
_SleV2Security4ACLPolicyControlClassID_Object = MibScalar
sleV2Security4ACLPolicyControlClassID = _SleV2Security4ACLPolicyControlClassID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 2, 12),
    _SleV2Security4ACLPolicyControlClassID_Type()
)
sleV2Security4ACLPolicyControlClassID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyControlClassID.setStatus("current")
_SleV2Security4ACLPolicyNotification_ObjectIdentity = ObjectIdentity
sleV2Security4ACLPolicyNotification = _SleV2Security4ACLPolicyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 3)
)
_SleV2Security4ACLPolicyFlowClass_ObjectIdentity = ObjectIdentity
sleV2Security4ACLPolicyFlowClass = _SleV2Security4ACLPolicyFlowClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2)
)
_SleV2Security4ACLPolicyFlowClassTable_Object = MibTable
sleV2Security4ACLPolicyFlowClassTable = _SleV2Security4ACLPolicyFlowClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassTable.setStatus("current")
_SleV2Security4ACLPolicyFlowClassEntry_Object = MibTableRow
sleV2Security4ACLPolicyFlowClassEntry = _SleV2Security4ACLPolicyFlowClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 1, 1)
)
sleV2Security4ACLPolicyFlowClassEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLPolicyIndex"),
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassIndex"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassEntry.setStatus("current")
_SleV2Security4ACLPolicyFlowClassIndex_Type = IntFlowIndex
_SleV2Security4ACLPolicyFlowClassIndex_Object = MibTableColumn
sleV2Security4ACLPolicyFlowClassIndex = _SleV2Security4ACLPolicyFlowClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 1, 1, 1),
    _SleV2Security4ACLPolicyFlowClassIndex_Type()
)
sleV2Security4ACLPolicyFlowClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassIndex.setStatus("current")
_SleV2Security4ACLPolicyFlowClassType_Type = IntFlowOrClass
_SleV2Security4ACLPolicyFlowClassType_Object = MibTableColumn
sleV2Security4ACLPolicyFlowClassType = _SleV2Security4ACLPolicyFlowClassType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 1, 1, 2),
    _SleV2Security4ACLPolicyFlowClassType_Type()
)
sleV2Security4ACLPolicyFlowClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassType.setStatus("current")
_SleV2Security4ACLPolicyFlowClassID_Type = IntFlowIndex
_SleV2Security4ACLPolicyFlowClassID_Object = MibTableColumn
sleV2Security4ACLPolicyFlowClassID = _SleV2Security4ACLPolicyFlowClassID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 1, 1, 3),
    _SleV2Security4ACLPolicyFlowClassID_Type()
)
sleV2Security4ACLPolicyFlowClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassID.setStatus("current")
_SleV2Security4ACLPolicyFlowClassName_Type = OctetName
_SleV2Security4ACLPolicyFlowClassName_Object = MibTableColumn
sleV2Security4ACLPolicyFlowClassName = _SleV2Security4ACLPolicyFlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 1, 1, 4),
    _SleV2Security4ACLPolicyFlowClassName_Type()
)
sleV2Security4ACLPolicyFlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassName.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControl_ObjectIdentity = ObjectIdentity
sleV2Security4ACLPolicyFlowClassControl = _SleV2Security4ACLPolicyFlowClassControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2)
)


class _SleV2Security4ACLPolicyFlowClassControlRequest_Type(Integer32):
    """Custom type sleV2Security4ACLPolicyFlowClassControlRequest based on Integer32"""
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


_SleV2Security4ACLPolicyFlowClassControlRequest_Type.__name__ = "Integer32"
_SleV2Security4ACLPolicyFlowClassControlRequest_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlRequest = _SleV2Security4ACLPolicyFlowClassControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 1),
    _SleV2Security4ACLPolicyFlowClassControlRequest_Type()
)
sleV2Security4ACLPolicyFlowClassControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlRequest.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlStatus_Type = SleControlStatusType
_SleV2Security4ACLPolicyFlowClassControlStatus_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlStatus = _SleV2Security4ACLPolicyFlowClassControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 2),
    _SleV2Security4ACLPolicyFlowClassControlStatus_Type()
)
sleV2Security4ACLPolicyFlowClassControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlStatus.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlTimer_Type = Gauge32
_SleV2Security4ACLPolicyFlowClassControlTimer_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlTimer = _SleV2Security4ACLPolicyFlowClassControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 3),
    _SleV2Security4ACLPolicyFlowClassControlTimer_Type()
)
sleV2Security4ACLPolicyFlowClassControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlTimer.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlTimeStamp_Type = TimeTicks
_SleV2Security4ACLPolicyFlowClassControlTimeStamp_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlTimeStamp = _SleV2Security4ACLPolicyFlowClassControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 4),
    _SleV2Security4ACLPolicyFlowClassControlTimeStamp_Type()
)
sleV2Security4ACLPolicyFlowClassControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlTimeStamp.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlReqResult_Type = SleControlRequestResultType
_SleV2Security4ACLPolicyFlowClassControlReqResult_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlReqResult = _SleV2Security4ACLPolicyFlowClassControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 5),
    _SleV2Security4ACLPolicyFlowClassControlReqResult_Type()
)
sleV2Security4ACLPolicyFlowClassControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlReqResult.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlPolicyIndex_Type = IntPolicyIndex
_SleV2Security4ACLPolicyFlowClassControlPolicyIndex_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlPolicyIndex = _SleV2Security4ACLPolicyFlowClassControlPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 6),
    _SleV2Security4ACLPolicyFlowClassControlPolicyIndex_Type()
)
sleV2Security4ACLPolicyFlowClassControlPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlPolicyIndex.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlIndex_Type = IntFlowIndex
_SleV2Security4ACLPolicyFlowClassControlIndex_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlIndex = _SleV2Security4ACLPolicyFlowClassControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 7),
    _SleV2Security4ACLPolicyFlowClassControlIndex_Type()
)
sleV2Security4ACLPolicyFlowClassControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlIndex.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlType_Type = IntFlowOrClass
_SleV2Security4ACLPolicyFlowClassControlType_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlType = _SleV2Security4ACLPolicyFlowClassControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 8),
    _SleV2Security4ACLPolicyFlowClassControlType_Type()
)
sleV2Security4ACLPolicyFlowClassControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlType.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlFlowID_Type = IntFlowIndex
_SleV2Security4ACLPolicyFlowClassControlFlowID_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlFlowID = _SleV2Security4ACLPolicyFlowClassControlFlowID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 9),
    _SleV2Security4ACLPolicyFlowClassControlFlowID_Type()
)
sleV2Security4ACLPolicyFlowClassControlFlowID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlFlowID.setStatus("current")
_SleV2Security4ACLPolicyFlowClassControlClassID_Type = IntClassIndex
_SleV2Security4ACLPolicyFlowClassControlClassID_Object = MibScalar
sleV2Security4ACLPolicyFlowClassControlClassID = _SleV2Security4ACLPolicyFlowClassControlClassID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 2, 10),
    _SleV2Security4ACLPolicyFlowClassControlClassID_Type()
)
sleV2Security4ACLPolicyFlowClassControlClassID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLPolicyFlowClassControlClassID.setStatus("current")
_SleV2Security4ACLPolicyFlowClassNotification_ObjectIdentity = ObjectIdentity
sleV2Security4ACLPolicyFlowClassNotification = _SleV2Security4ACLPolicyFlowClassNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 3)
)
_SleV2Security4ACLGroup_ObjectIdentity = ObjectIdentity
sleV2Security4ACLGroup = _SleV2Security4ACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5)
)
_SleV2Security4ACLGroupIf_ObjectIdentity = ObjectIdentity
sleV2Security4ACLGroupIf = _SleV2Security4ACLGroupIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1)
)
_SleV2Security4ACLGroupIfTable_Object = MibTable
sleV2Security4ACLGroupIfTable = _SleV2Security4ACLGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfTable.setStatus("current")
_SleV2Security4ACLGroupIfEntry_Object = MibTableRow
sleV2Security4ACLGroupIfEntry = _SleV2Security4ACLGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 1, 1)
)
sleV2Security4ACLGroupIfEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLGroupIfindex"),
    (0, "SLEV2-Security-MIB", "sleV2Security4ACLGroupIfType"),
)
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfEntry.setStatus("current")


class _SleV2Security4ACLGroupIfindex_Type(Integer32):
    """Custom type sleV2Security4ACLGroupIfindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2Security4ACLGroupIfindex_Type.__name__ = "Integer32"
_SleV2Security4ACLGroupIfindex_Object = MibTableColumn
sleV2Security4ACLGroupIfindex = _SleV2Security4ACLGroupIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 1, 1, 1),
    _SleV2Security4ACLGroupIfindex_Type()
)
sleV2Security4ACLGroupIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfindex.setStatus("current")


class _SleV2Security4ACLGroupIfType_Type(Integer32):
    """Custom type sleV2Security4ACLGroupIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("mac", 4))
    )


_SleV2Security4ACLGroupIfType_Type.__name__ = "Integer32"
_SleV2Security4ACLGroupIfType_Object = MibTableColumn
sleV2Security4ACLGroupIfType = _SleV2Security4ACLGroupIfType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 1, 1, 2),
    _SleV2Security4ACLGroupIfType_Type()
)
sleV2Security4ACLGroupIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfType.setStatus("current")
_SleV2Security4ACLGroupIfName_Type = OctetString
_SleV2Security4ACLGroupIfName_Object = MibTableColumn
sleV2Security4ACLGroupIfName = _SleV2Security4ACLGroupIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 1, 1, 3),
    _SleV2Security4ACLGroupIfName_Type()
)
sleV2Security4ACLGroupIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfName.setStatus("current")


class _SleV2Security4ACLGroupIfPriority_Type(Integer32):
    """Custom type sleV2Security4ACLGroupIfPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_SleV2Security4ACLGroupIfPriority_Type.__name__ = "Integer32"
_SleV2Security4ACLGroupIfPriority_Object = MibTableColumn
sleV2Security4ACLGroupIfPriority = _SleV2Security4ACLGroupIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 1, 1, 4),
    _SleV2Security4ACLGroupIfPriority_Type()
)
sleV2Security4ACLGroupIfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfPriority.setStatus("current")
_SleV2Security4ACLGroupIfControl_ObjectIdentity = ObjectIdentity
sleV2Security4ACLGroupIfControl = _SleV2Security4ACLGroupIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2)
)


class _SleV2Security4ACLGroupIfControlRequest_Type(Integer32):
    """Custom type sleV2Security4ACLGroupIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSecurityAclGroupIfProfile", 1),
          ("delSecurityAclGroupIfProfile", 2))
    )


_SleV2Security4ACLGroupIfControlRequest_Type.__name__ = "Integer32"
_SleV2Security4ACLGroupIfControlRequest_Object = MibScalar
sleV2Security4ACLGroupIfControlRequest = _SleV2Security4ACLGroupIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 1),
    _SleV2Security4ACLGroupIfControlRequest_Type()
)
sleV2Security4ACLGroupIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlRequest.setStatus("current")
_SleV2Security4ACLGroupIfControlStatus_Type = SleControlStatusType
_SleV2Security4ACLGroupIfControlStatus_Object = MibScalar
sleV2Security4ACLGroupIfControlStatus = _SleV2Security4ACLGroupIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 2),
    _SleV2Security4ACLGroupIfControlStatus_Type()
)
sleV2Security4ACLGroupIfControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlStatus.setStatus("current")
_SleV2Security4ACLGroupIfControlTimer_Type = Gauge32
_SleV2Security4ACLGroupIfControlTimer_Object = MibScalar
sleV2Security4ACLGroupIfControlTimer = _SleV2Security4ACLGroupIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 3),
    _SleV2Security4ACLGroupIfControlTimer_Type()
)
sleV2Security4ACLGroupIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlTimer.setStatus("current")
_SleV2Security4ACLGroupIfControlReqResult_Type = TimeTicks
_SleV2Security4ACLGroupIfControlReqResult_Object = MibScalar
sleV2Security4ACLGroupIfControlReqResult = _SleV2Security4ACLGroupIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 4),
    _SleV2Security4ACLGroupIfControlReqResult_Type()
)
sleV2Security4ACLGroupIfControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlReqResult.setStatus("current")
_SleV2Security4ACLGroupIfControlTimeStamp_Type = SleControlRequestResultType
_SleV2Security4ACLGroupIfControlTimeStamp_Object = MibScalar
sleV2Security4ACLGroupIfControlTimeStamp = _SleV2Security4ACLGroupIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 5),
    _SleV2Security4ACLGroupIfControlTimeStamp_Type()
)
sleV2Security4ACLGroupIfControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlTimeStamp.setStatus("current")
_SleV2Security4ACLGroupIfConrolIndex_Type = Integer32
_SleV2Security4ACLGroupIfConrolIndex_Object = MibScalar
sleV2Security4ACLGroupIfConrolIndex = _SleV2Security4ACLGroupIfConrolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 6),
    _SleV2Security4ACLGroupIfConrolIndex_Type()
)
sleV2Security4ACLGroupIfConrolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfConrolIndex.setStatus("current")


class _SleV2Security4ACLGroupIfControlType_Type(Integer32):
    """Custom type sleV2Security4ACLGroupIfControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ip", 3),
          ("mac", 4))
    )


_SleV2Security4ACLGroupIfControlType_Type.__name__ = "Integer32"
_SleV2Security4ACLGroupIfControlType_Object = MibScalar
sleV2Security4ACLGroupIfControlType = _SleV2Security4ACLGroupIfControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 7),
    _SleV2Security4ACLGroupIfControlType_Type()
)
sleV2Security4ACLGroupIfControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlType.setStatus("current")
_SleV2Security4ACLGroupIfControlName_Type = OctetString
_SleV2Security4ACLGroupIfControlName_Object = MibScalar
sleV2Security4ACLGroupIfControlName = _SleV2Security4ACLGroupIfControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 8),
    _SleV2Security4ACLGroupIfControlName_Type()
)
sleV2Security4ACLGroupIfControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlName.setStatus("current")


class _SleV2Security4ACLGroupIfControlPriority_Type(Integer32):
    """Custom type sleV2Security4ACLGroupIfControlPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_SleV2Security4ACLGroupIfControlPriority_Type.__name__ = "Integer32"
_SleV2Security4ACLGroupIfControlPriority_Object = MibScalar
sleV2Security4ACLGroupIfControlPriority = _SleV2Security4ACLGroupIfControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 2, 9),
    _SleV2Security4ACLGroupIfControlPriority_Type()
)
sleV2Security4ACLGroupIfControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfControlPriority.setStatus("current")
_SleV2SecurityACLGroupIfNotification_ObjectIdentity = ObjectIdentity
sleV2SecurityACLGroupIfNotification = _SleV2SecurityACLGroupIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 3)
)
_SleV2SecuritySACL_ObjectIdentity = ObjectIdentity
sleV2SecuritySACL = _SleV2SecuritySACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6)
)
_SleV2SecuritySACLTable_Object = MibTable
sleV2SecuritySACLTable = _SleV2SecuritySACLTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sleV2SecuritySACLTable.setStatus("current")
_SleV2SecuritySACLEntry_Object = MibTableRow
sleV2SecuritySACLEntry = _SleV2SecuritySACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1)
)
sleV2SecuritySACLEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2SecuritySACLName"),
)
if mibBuilder.loadTexts:
    sleV2SecuritySACLEntry.setStatus("current")
_SleV2SecuritySACLName_Type = OctetName
_SleV2SecuritySACLName_Object = MibTableColumn
sleV2SecuritySACLName = _SleV2SecuritySACLName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 1),
    _SleV2SecuritySACLName_Type()
)
sleV2SecuritySACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLName.setStatus("current")
_SleV2SecuritySACLSrcIpaddr_Type = IpAddress
_SleV2SecuritySACLSrcIpaddr_Object = MibTableColumn
sleV2SecuritySACLSrcIpaddr = _SleV2SecuritySACLSrcIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 2),
    _SleV2SecuritySACLSrcIpaddr_Type()
)
sleV2SecuritySACLSrcIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLSrcIpaddr.setStatus("current")


class _SleV2SecuritySACLSrcPrefixLength_Type(Integer32):
    """Custom type sleV2SecuritySACLSrcPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleV2SecuritySACLSrcPrefixLength_Type.__name__ = "Integer32"
_SleV2SecuritySACLSrcPrefixLength_Object = MibTableColumn
sleV2SecuritySACLSrcPrefixLength = _SleV2SecuritySACLSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 3),
    _SleV2SecuritySACLSrcPrefixLength_Type()
)
sleV2SecuritySACLSrcPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLSrcPrefixLength.setStatus("current")
_SleV2SecuritySACLDstIpAddr_Type = IpAddress
_SleV2SecuritySACLDstIpAddr_Object = MibTableColumn
sleV2SecuritySACLDstIpAddr = _SleV2SecuritySACLDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 4),
    _SleV2SecuritySACLDstIpAddr_Type()
)
sleV2SecuritySACLDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLDstIpAddr.setStatus("current")


class _SleV2SecuritySACLDstPrefixLength_Type(Integer32):
    """Custom type sleV2SecuritySACLDstPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleV2SecuritySACLDstPrefixLength_Type.__name__ = "Integer32"
_SleV2SecuritySACLDstPrefixLength_Object = MibTableColumn
sleV2SecuritySACLDstPrefixLength = _SleV2SecuritySACLDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 5),
    _SleV2SecuritySACLDstPrefixLength_Type()
)
sleV2SecuritySACLDstPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLDstPrefixLength.setStatus("current")
_SleV2SecuritySACLProtocolType_Type = IntProtocolType
_SleV2SecuritySACLProtocolType_Object = MibTableColumn
sleV2SecuritySACLProtocolType = _SleV2SecuritySACLProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 6),
    _SleV2SecuritySACLProtocolType_Type()
)
sleV2SecuritySACLProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLProtocolType.setStatus("current")


class _SleV2SecuritySACLTcpflag_Type(Bits):
    """Custom type sleV2SecuritySACLTcpflag based on Bits"""
    namedValues = NamedValues(
        *(("reserv", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleV2SecuritySACLTcpflag_Type.__name__ = "Bits"
_SleV2SecuritySACLTcpflag_Object = MibTableColumn
sleV2SecuritySACLTcpflag = _SleV2SecuritySACLTcpflag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 7),
    _SleV2SecuritySACLTcpflag_Type()
)
sleV2SecuritySACLTcpflag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLTcpflag.setStatus("current")
_SleV2SecuritySACLSrcL4Port_Type = IntL4Port
_SleV2SecuritySACLSrcL4Port_Object = MibTableColumn
sleV2SecuritySACLSrcL4Port = _SleV2SecuritySACLSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 8),
    _SleV2SecuritySACLSrcL4Port_Type()
)
sleV2SecuritySACLSrcL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLSrcL4Port.setStatus("current")
_SleV2SecuritySACLDstL4Port_Type = IntL4Port
_SleV2SecuritySACLDstL4Port_Object = MibTableColumn
sleV2SecuritySACLDstL4Port = _SleV2SecuritySACLDstL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 9),
    _SleV2SecuritySACLDstL4Port_Type()
)
sleV2SecuritySACLDstL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLDstL4Port.setStatus("current")
_SleV2SecuritySACLIcmpType_Type = IntProtocolType
_SleV2SecuritySACLIcmpType_Object = MibTableColumn
sleV2SecuritySACLIcmpType = _SleV2SecuritySACLIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 10),
    _SleV2SecuritySACLIcmpType_Type()
)
sleV2SecuritySACLIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLIcmpType.setStatus("current")
_SleV2SecuritySACLIcmpCode_Type = IntProtocolType
_SleV2SecuritySACLIcmpCode_Object = MibTableColumn
sleV2SecuritySACLIcmpCode = _SleV2SecuritySACLIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 11),
    _SleV2SecuritySACLIcmpCode_Type()
)
sleV2SecuritySACLIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLIcmpCode.setStatus("current")


class _SleV2SecuritySACLPriority_Type(Integer32):
    """Custom type sleV2SecuritySACLPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_SleV2SecuritySACLPriority_Type.__name__ = "Integer32"
_SleV2SecuritySACLPriority_Object = MibTableColumn
sleV2SecuritySACLPriority = _SleV2SecuritySACLPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 12),
    _SleV2SecuritySACLPriority_Type()
)
sleV2SecuritySACLPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLPriority.setStatus("current")


class _SleV2SecuritySACLMatchAction_Type(Integer32):
    """Custom type sleV2SecuritySACLMatchAction based on Integer32"""
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
          ("permit", 1),
          ("deny", 2))
    )


_SleV2SecuritySACLMatchAction_Type.__name__ = "Integer32"
_SleV2SecuritySACLMatchAction_Object = MibTableColumn
sleV2SecuritySACLMatchAction = _SleV2SecuritySACLMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 13),
    _SleV2SecuritySACLMatchAction_Type()
)
sleV2SecuritySACLMatchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLMatchAction.setStatus("current")


class _SleV2SecuritySACLNomatchAction_Type(Integer32):
    """Custom type sleV2SecuritySACLNomatchAction based on Integer32"""
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
          ("permit", 1),
          ("deny", 2))
    )


_SleV2SecuritySACLNomatchAction_Type.__name__ = "Integer32"
_SleV2SecuritySACLNomatchAction_Object = MibTableColumn
sleV2SecuritySACLNomatchAction = _SleV2SecuritySACLNomatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 1, 1, 14),
    _SleV2SecuritySACLNomatchAction_Type()
)
sleV2SecuritySACLNomatchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLNomatchAction.setStatus("current")
_SleV2SecuritySACLControl_ObjectIdentity = ObjectIdentity
sleV2SecuritySACLControl = _SleV2SecuritySACLControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2)
)


class _SleV2SecuritySACLControlRequest_Type(Integer32):
    """Custom type sleV2SecuritySACLControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createSAclRule", 1),
          ("destroySAclRule", 2),
          ("destroyAllSAclRule", 3))
    )


_SleV2SecuritySACLControlRequest_Type.__name__ = "Integer32"
_SleV2SecuritySACLControlRequest_Object = MibScalar
sleV2SecuritySACLControlRequest = _SleV2SecuritySACLControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 1),
    _SleV2SecuritySACLControlRequest_Type()
)
sleV2SecuritySACLControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlRequest.setStatus("current")
_SleV2SecuritySACLControlStatus_Type = SleControlStatusType
_SleV2SecuritySACLControlStatus_Object = MibScalar
sleV2SecuritySACLControlStatus = _SleV2SecuritySACLControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 2),
    _SleV2SecuritySACLControlStatus_Type()
)
sleV2SecuritySACLControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlStatus.setStatus("current")
_SleV2SecuritySACLControlTimer_Type = Gauge32
_SleV2SecuritySACLControlTimer_Object = MibScalar
sleV2SecuritySACLControlTimer = _SleV2SecuritySACLControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 3),
    _SleV2SecuritySACLControlTimer_Type()
)
sleV2SecuritySACLControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlTimer.setStatus("current")
_SleV2SecuritySACLControlTimeStamp_Type = TimeStamp
_SleV2SecuritySACLControlTimeStamp_Object = MibScalar
sleV2SecuritySACLControlTimeStamp = _SleV2SecuritySACLControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 4),
    _SleV2SecuritySACLControlTimeStamp_Type()
)
sleV2SecuritySACLControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlTimeStamp.setStatus("current")
_SleV2SecuritySACLControlReqResult_Type = SleControlRequestResultType
_SleV2SecuritySACLControlReqResult_Object = MibScalar
sleV2SecuritySACLControlReqResult = _SleV2SecuritySACLControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 5),
    _SleV2SecuritySACLControlReqResult_Type()
)
sleV2SecuritySACLControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlReqResult.setStatus("current")
_SleV2SecuritySACLControlName_Type = OctetName
_SleV2SecuritySACLControlName_Object = MibScalar
sleV2SecuritySACLControlName = _SleV2SecuritySACLControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 6),
    _SleV2SecuritySACLControlName_Type()
)
sleV2SecuritySACLControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlName.setStatus("current")
_SleV2SecuritySACLControlSrcIpaddr_Type = IpAddress
_SleV2SecuritySACLControlSrcIpaddr_Object = MibScalar
sleV2SecuritySACLControlSrcIpaddr = _SleV2SecuritySACLControlSrcIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 7),
    _SleV2SecuritySACLControlSrcIpaddr_Type()
)
sleV2SecuritySACLControlSrcIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlSrcIpaddr.setStatus("current")
_SleV2SecuritySACLControlSrcPrefixLength_Type = IntIpAddrMask
_SleV2SecuritySACLControlSrcPrefixLength_Object = MibScalar
sleV2SecuritySACLControlSrcPrefixLength = _SleV2SecuritySACLControlSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 8),
    _SleV2SecuritySACLControlSrcPrefixLength_Type()
)
sleV2SecuritySACLControlSrcPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlSrcPrefixLength.setStatus("current")
_SleV2SecuritySACLControlDstIpaddr_Type = IpAddress
_SleV2SecuritySACLControlDstIpaddr_Object = MibScalar
sleV2SecuritySACLControlDstIpaddr = _SleV2SecuritySACLControlDstIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 9),
    _SleV2SecuritySACLControlDstIpaddr_Type()
)
sleV2SecuritySACLControlDstIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlDstIpaddr.setStatus("current")
_SleV2SecuritySACLControlDstPrefixLength_Type = IntIpAddrMask
_SleV2SecuritySACLControlDstPrefixLength_Object = MibScalar
sleV2SecuritySACLControlDstPrefixLength = _SleV2SecuritySACLControlDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 10),
    _SleV2SecuritySACLControlDstPrefixLength_Type()
)
sleV2SecuritySACLControlDstPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlDstPrefixLength.setStatus("current")
_SleV2SecuritySACLControlProtocolType_Type = IntProtocolType
_SleV2SecuritySACLControlProtocolType_Object = MibScalar
sleV2SecuritySACLControlProtocolType = _SleV2SecuritySACLControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 11),
    _SleV2SecuritySACLControlProtocolType_Type()
)
sleV2SecuritySACLControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlProtocolType.setStatus("current")


class _SleV2SecuritySACLControlTcpflag_Type(Bits):
    """Custom type sleV2SecuritySACLControlTcpflag based on Bits"""
    namedValues = NamedValues(
        *(("reserv", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleV2SecuritySACLControlTcpflag_Type.__name__ = "Bits"
_SleV2SecuritySACLControlTcpflag_Object = MibScalar
sleV2SecuritySACLControlTcpflag = _SleV2SecuritySACLControlTcpflag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 12),
    _SleV2SecuritySACLControlTcpflag_Type()
)
sleV2SecuritySACLControlTcpflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlTcpflag.setStatus("current")
_SleV2SecuritySACLControlSrcL4Port_Type = IntL4Port
_SleV2SecuritySACLControlSrcL4Port_Object = MibScalar
sleV2SecuritySACLControlSrcL4Port = _SleV2SecuritySACLControlSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 13),
    _SleV2SecuritySACLControlSrcL4Port_Type()
)
sleV2SecuritySACLControlSrcL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlSrcL4Port.setStatus("current")
_SleV2SecuritySACLControlDstL4Port_Type = IntL4Port
_SleV2SecuritySACLControlDstL4Port_Object = MibScalar
sleV2SecuritySACLControlDstL4Port = _SleV2SecuritySACLControlDstL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 14),
    _SleV2SecuritySACLControlDstL4Port_Type()
)
sleV2SecuritySACLControlDstL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlDstL4Port.setStatus("current")
_SleV2SecuritySACLControlIcmpType_Type = IntProtocolType
_SleV2SecuritySACLControlIcmpType_Object = MibScalar
sleV2SecuritySACLControlIcmpType = _SleV2SecuritySACLControlIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 15),
    _SleV2SecuritySACLControlIcmpType_Type()
)
sleV2SecuritySACLControlIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlIcmpType.setStatus("current")
_SleV2SecuritySACLControlIcmpCode_Type = IntProtocolType
_SleV2SecuritySACLControlIcmpCode_Object = MibScalar
sleV2SecuritySACLControlIcmpCode = _SleV2SecuritySACLControlIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 16),
    _SleV2SecuritySACLControlIcmpCode_Type()
)
sleV2SecuritySACLControlIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlIcmpCode.setStatus("current")


class _SleV2SecuritySACLControlPriority_Type(Integer32):
    """Custom type sleV2SecuritySACLControlPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_SleV2SecuritySACLControlPriority_Type.__name__ = "Integer32"
_SleV2SecuritySACLControlPriority_Object = MibScalar
sleV2SecuritySACLControlPriority = _SleV2SecuritySACLControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 17),
    _SleV2SecuritySACLControlPriority_Type()
)
sleV2SecuritySACLControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlPriority.setStatus("current")


class _SleV2SecuritySACLControlMatchAction_Type(Integer32):
    """Custom type sleV2SecuritySACLControlMatchAction based on Integer32"""
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
          ("permit", 1),
          ("deny", 2))
    )


_SleV2SecuritySACLControlMatchAction_Type.__name__ = "Integer32"
_SleV2SecuritySACLControlMatchAction_Object = MibScalar
sleV2SecuritySACLControlMatchAction = _SleV2SecuritySACLControlMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 18),
    _SleV2SecuritySACLControlMatchAction_Type()
)
sleV2SecuritySACLControlMatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlMatchAction.setStatus("current")


class _SleV2SecuritySACLControlNomatchAction_Type(Integer32):
    """Custom type sleV2SecuritySACLControlNomatchAction based on Integer32"""
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
          ("permit", 1),
          ("deny", 2))
    )


_SleV2SecuritySACLControlNomatchAction_Type.__name__ = "Integer32"
_SleV2SecuritySACLControlNomatchAction_Object = MibScalar
sleV2SecuritySACLControlNomatchAction = _SleV2SecuritySACLControlNomatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 2, 19),
    _SleV2SecuritySACLControlNomatchAction_Type()
)
sleV2SecuritySACLControlNomatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecuritySACLControlNomatchAction.setStatus("current")
_SleV2SecuritySACLNotification_ObjectIdentity = ObjectIdentity
sleV2SecuritySACLNotification = _SleV2SecuritySACLNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 3)
)
_SleV2SecurityACLStatistics_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatistics = _SleV2SecurityACLStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7)
)
_SleV2SecurityACLStatisticsBase_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatisticsBase = _SleV2SecurityACLStatisticsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1)
)
_SleV2SecurityACLStatisticsBaseInfo_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatisticsBaseInfo = _SleV2SecurityACLStatisticsBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 1)
)


class _SleV2SecurityACLStatisticsSyslogStatus_Type(Integer32):
    """Custom type sleV2SecurityACLStatisticsSyslogStatus based on Integer32"""
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


_SleV2SecurityACLStatisticsSyslogStatus_Type.__name__ = "Integer32"
_SleV2SecurityACLStatisticsSyslogStatus_Object = MibScalar
sleV2SecurityACLStatisticsSyslogStatus = _SleV2SecurityACLStatisticsSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 1, 1),
    _SleV2SecurityACLStatisticsSyslogStatus_Type()
)
sleV2SecurityACLStatisticsSyslogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsSyslogStatus.setStatus("current")
_SleV2SecurityACLStatisticsBaseControl_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatisticsBaseControl = _SleV2SecurityACLStatisticsBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 2)
)


class _SleV2SecurityACLStatisticsBaseControlRequest_Type(Integer32):
    """Custom type sleV2SecurityACLStatisticsBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("aclSyslogModeChange", 1)
    )


_SleV2SecurityACLStatisticsBaseControlRequest_Type.__name__ = "Integer32"
_SleV2SecurityACLStatisticsBaseControlRequest_Object = MibScalar
sleV2SecurityACLStatisticsBaseControlRequest = _SleV2SecurityACLStatisticsBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 2, 1),
    _SleV2SecurityACLStatisticsBaseControlRequest_Type()
)
sleV2SecurityACLStatisticsBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsBaseControlRequest.setStatus("current")
_SleV2SecurityACLStatisticsBaseControlStatus_Type = SleControlStatusType
_SleV2SecurityACLStatisticsBaseControlStatus_Object = MibScalar
sleV2SecurityACLStatisticsBaseControlStatus = _SleV2SecurityACLStatisticsBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 2, 2),
    _SleV2SecurityACLStatisticsBaseControlStatus_Type()
)
sleV2SecurityACLStatisticsBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsBaseControlStatus.setStatus("current")
_SleV2SecurityACLStatisticsBaseControlTimer_Type = Gauge32
_SleV2SecurityACLStatisticsBaseControlTimer_Object = MibScalar
sleV2SecurityACLStatisticsBaseControlTimer = _SleV2SecurityACLStatisticsBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 2, 3),
    _SleV2SecurityACLStatisticsBaseControlTimer_Type()
)
sleV2SecurityACLStatisticsBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsBaseControlTimer.setStatus("current")
_SleV2SecurityACLStatisticsBaseControlTimeStamp_Type = TimeStamp
_SleV2SecurityACLStatisticsBaseControlTimeStamp_Object = MibScalar
sleV2SecurityACLStatisticsBaseControlTimeStamp = _SleV2SecurityACLStatisticsBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 2, 4),
    _SleV2SecurityACLStatisticsBaseControlTimeStamp_Type()
)
sleV2SecurityACLStatisticsBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsBaseControlTimeStamp.setStatus("current")
_SleV2SecurityACLStatisticsBaseControlReqResult_Type = SleControlRequestResultType
_SleV2SecurityACLStatisticsBaseControlReqResult_Object = MibScalar
sleV2SecurityACLStatisticsBaseControlReqResult = _SleV2SecurityACLStatisticsBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 2, 5),
    _SleV2SecurityACLStatisticsBaseControlReqResult_Type()
)
sleV2SecurityACLStatisticsBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsBaseControlReqResult.setStatus("current")


class _SleV2SecurityACLStatisticsBaseControlSyslogMode_Type(Integer32):
    """Custom type sleV2SecurityACLStatisticsBaseControlSyslogMode based on Integer32"""
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


_SleV2SecurityACLStatisticsBaseControlSyslogMode_Type.__name__ = "Integer32"
_SleV2SecurityACLStatisticsBaseControlSyslogMode_Object = MibScalar
sleV2SecurityACLStatisticsBaseControlSyslogMode = _SleV2SecurityACLStatisticsBaseControlSyslogMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 2, 6),
    _SleV2SecurityACLStatisticsBaseControlSyslogMode_Type()
)
sleV2SecurityACLStatisticsBaseControlSyslogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsBaseControlSyslogMode.setStatus("current")
_SleV2SecurityACLStatisticsBaseNotification_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatisticsBaseNotification = _SleV2SecurityACLStatisticsBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 3)
)
_SleV2SecurityACLStatisticsPacketHistory_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatisticsPacketHistory = _SleV2SecurityACLStatisticsPacketHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2)
)
_SleV2SecurityACLPacketCountTable_Object = MibTable
sleV2SecurityACLPacketCountTable = _SleV2SecurityACLPacketCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2SecurityACLPacketCountTable.setStatus("current")
_SleV2SecurityACLPacketCountEntry_Object = MibTableRow
sleV2SecurityACLPacketCountEntry = _SleV2SecurityACLPacketCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 1, 1)
)
sleV2SecurityACLPacketCountEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2SecuritySACLName"),
)
if mibBuilder.loadTexts:
    sleV2SecurityACLPacketCountEntry.setStatus("current")
_SleV2SecurityACLTotalPacket_Type = Counter64
_SleV2SecurityACLTotalPacket_Object = MibTableColumn
sleV2SecurityACLTotalPacket = _SleV2SecurityACLTotalPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 1, 1, 1),
    _SleV2SecurityACLTotalPacket_Type()
)
sleV2SecurityACLTotalPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLTotalPacket.setStatus("current")
_SleV2SecurityACLSrcHistoryTable_Object = MibTable
sleV2SecurityACLSrcHistoryTable = _SleV2SecurityACLSrcHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 2)
)
if mibBuilder.loadTexts:
    sleV2SecurityACLSrcHistoryTable.setStatus("current")
_SleV2SecurityACLSrcHistoryEntry_Object = MibTableRow
sleV2SecurityACLSrcHistoryEntry = _SleV2SecurityACLSrcHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 2, 1)
)
sleV2SecurityACLSrcHistoryEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2SecuritySACLName"),
    (0, "SLEV2-Security-MIB", "sleV2SecurityACLSrcHistoryIndex"),
)
if mibBuilder.loadTexts:
    sleV2SecurityACLSrcHistoryEntry.setStatus("current")


class _SleV2SecurityACLSrcHistoryIndex_Type(Integer32):
    """Custom type sleV2SecurityACLSrcHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SleV2SecurityACLSrcHistoryIndex_Type.__name__ = "Integer32"
_SleV2SecurityACLSrcHistoryIndex_Object = MibTableColumn
sleV2SecurityACLSrcHistoryIndex = _SleV2SecurityACLSrcHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 2, 1, 1),
    _SleV2SecurityACLSrcHistoryIndex_Type()
)
sleV2SecurityACLSrcHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLSrcHistoryIndex.setStatus("current")
_SleV2SecurityACLSrcHistoryIpAddr_Type = IpAddress
_SleV2SecurityACLSrcHistoryIpAddr_Object = MibTableColumn
sleV2SecurityACLSrcHistoryIpAddr = _SleV2SecurityACLSrcHistoryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 2, 1, 2),
    _SleV2SecurityACLSrcHistoryIpAddr_Type()
)
sleV2SecurityACLSrcHistoryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLSrcHistoryIpAddr.setStatus("current")
_SleV2SecurityACLStatisticsControl_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatisticsControl = _SleV2SecurityACLStatisticsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 3)
)


class _SleV2SecurityACLStatisticsControlRequest_Type(Integer32):
    """Custom type sleV2SecurityACLStatisticsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearAruleStatus", 1)
    )


_SleV2SecurityACLStatisticsControlRequest_Type.__name__ = "Integer32"
_SleV2SecurityACLStatisticsControlRequest_Object = MibScalar
sleV2SecurityACLStatisticsControlRequest = _SleV2SecurityACLStatisticsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 3, 1),
    _SleV2SecurityACLStatisticsControlRequest_Type()
)
sleV2SecurityACLStatisticsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsControlRequest.setStatus("current")
_SleV2SecurityACLStatisticsControlStatus_Type = SleControlStatusType
_SleV2SecurityACLStatisticsControlStatus_Object = MibScalar
sleV2SecurityACLStatisticsControlStatus = _SleV2SecurityACLStatisticsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 3, 2),
    _SleV2SecurityACLStatisticsControlStatus_Type()
)
sleV2SecurityACLStatisticsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsControlStatus.setStatus("current")
_SleV2SecurityACLStatisticsControlTimer_Type = Gauge32
_SleV2SecurityACLStatisticsControlTimer_Object = MibScalar
sleV2SecurityACLStatisticsControlTimer = _SleV2SecurityACLStatisticsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 3, 3),
    _SleV2SecurityACLStatisticsControlTimer_Type()
)
sleV2SecurityACLStatisticsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsControlTimer.setStatus("current")
_SleV2SecurityACLStatisticsControlTimeStamp_Type = TimeStamp
_SleV2SecurityACLStatisticsControlTimeStamp_Object = MibScalar
sleV2SecurityACLStatisticsControlTimeStamp = _SleV2SecurityACLStatisticsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 3, 4),
    _SleV2SecurityACLStatisticsControlTimeStamp_Type()
)
sleV2SecurityACLStatisticsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsControlTimeStamp.setStatus("current")
_SleV2SecurityACLStatisticsControlReqResult_Type = SleControlRequestResultType
_SleV2SecurityACLStatisticsControlReqResult_Object = MibScalar
sleV2SecurityACLStatisticsControlReqResult = _SleV2SecurityACLStatisticsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 3, 5),
    _SleV2SecurityACLStatisticsControlReqResult_Type()
)
sleV2SecurityACLStatisticsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsControlReqResult.setStatus("current")
_SleV2SecurityACLStatisticsControlName_Type = OctetName
_SleV2SecurityACLStatisticsControlName_Object = MibScalar
sleV2SecurityACLStatisticsControlName = _SleV2SecurityACLStatisticsControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 3, 6),
    _SleV2SecurityACLStatisticsControlName_Type()
)
sleV2SecurityACLStatisticsControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsControlName.setStatus("current")
_SleV2SecurityACLStatisticsNotification_ObjectIdentity = ObjectIdentity
sleV2SecurityACLStatisticsNotification = _SleV2SecurityACLStatisticsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 4)
)
_SleV2CpuPacketFilter_ObjectIdentity = ObjectIdentity
sleV2CpuPacketFilter = _SleV2CpuPacketFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8)
)
_SleV2CpuPacketFilterTable_Object = MibTable
sleV2CpuPacketFilterTable = _SleV2CpuPacketFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1)
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterTable.setStatus("current")
_SleV2CpuPacketFilterEntry_Object = MibTableRow
sleV2CpuPacketFilterEntry = _SleV2CpuPacketFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1)
)
sleV2CpuPacketFilterEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2CpuPacketFilterIndex"),
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterEntry.setStatus("current")


class _SleV2CpuPacketFilterIndex_Type(Integer32):
    """Custom type sleV2CpuPacketFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleV2CpuPacketFilterIndex_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterIndex_Object = MibTableColumn
sleV2CpuPacketFilterIndex = _SleV2CpuPacketFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 1),
    _SleV2CpuPacketFilterIndex_Type()
)
sleV2CpuPacketFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterIndex.setStatus("current")
_SleV2CpuPacketFilterName_Type = OctetString
_SleV2CpuPacketFilterName_Object = MibTableColumn
sleV2CpuPacketFilterName = _SleV2CpuPacketFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 2),
    _SleV2CpuPacketFilterName_Type()
)
sleV2CpuPacketFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterName.setStatus("current")
_SleV2CpuPacketFilterCreationTime_Type = Counter32
_SleV2CpuPacketFilterCreationTime_Object = MibTableColumn
sleV2CpuPacketFilterCreationTime = _SleV2CpuPacketFilterCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 3),
    _SleV2CpuPacketFilterCreationTime_Type()
)
sleV2CpuPacketFilterCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterCreationTime.setStatus("current")
_SleV2CpuPacketFilterElapsedtimeAfterClear_Type = Counter32
_SleV2CpuPacketFilterElapsedtimeAfterClear_Object = MibTableColumn
sleV2CpuPacketFilterElapsedtimeAfterClear = _SleV2CpuPacketFilterElapsedtimeAfterClear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 4),
    _SleV2CpuPacketFilterElapsedtimeAfterClear_Type()
)
sleV2CpuPacketFilterElapsedtimeAfterClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterElapsedtimeAfterClear.setStatus("current")


class _SleV2CpuPacketFilterStage_Type(Integer32):
    """Custom type sleV2CpuPacketFilterStage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cpuingress", 1),
          ("cpuegress", 2),
          ("portrx", 3),
          ("porttx", 4),
          ("vlanAssigned", 5),
          ("unknown", 255))
    )


_SleV2CpuPacketFilterStage_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterStage_Object = MibTableColumn
sleV2CpuPacketFilterStage = _SleV2CpuPacketFilterStage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 5),
    _SleV2CpuPacketFilterStage_Type()
)
sleV2CpuPacketFilterStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterStage.setStatus("current")


class _SleV2CpuPacketFilterPriority_Type(Integer32):
    """Custom type sleV2CpuPacketFilterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2CpuPacketFilterPriority_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterPriority_Object = MibTableColumn
sleV2CpuPacketFilterPriority = _SleV2CpuPacketFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 6),
    _SleV2CpuPacketFilterPriority_Type()
)
sleV2CpuPacketFilterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterPriority.setStatus("current")


class _SleV2CpuPacketFilterAction_Type(Integer32):
    """Custom type sleV2CpuPacketFilterAction based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("permit", 2),
          ("rateLimit", 3),
          ("pass", 4),
          ("dot1q", 5),
          ("dot1qAttach", 6),
          ("dot1qDetach", 7),
          ("unknown", 255))
    )


_SleV2CpuPacketFilterAction_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterAction_Object = MibTableColumn
sleV2CpuPacketFilterAction = _SleV2CpuPacketFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 7),
    _SleV2CpuPacketFilterAction_Type()
)
sleV2CpuPacketFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterAction.setStatus("current")


class _SleV2CpuPacketFilterActionRateLimit_Type(Integer32):
    """Custom type sleV2CpuPacketFilterActionRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleV2CpuPacketFilterActionRateLimit_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterActionRateLimit_Object = MibTableColumn
sleV2CpuPacketFilterActionRateLimit = _SleV2CpuPacketFilterActionRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 8),
    _SleV2CpuPacketFilterActionRateLimit_Type()
)
sleV2CpuPacketFilterActionRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterActionRateLimit.setStatus("current")


class _SleV2CpuPacketFilterActionBurstSize_Type(Integer32):
    """Custom type sleV2CpuPacketFilterActionBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleV2CpuPacketFilterActionBurstSize_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterActionBurstSize_Object = MibTableColumn
sleV2CpuPacketFilterActionBurstSize = _SleV2CpuPacketFilterActionBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 9),
    _SleV2CpuPacketFilterActionBurstSize_Type()
)
sleV2CpuPacketFilterActionBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterActionBurstSize.setStatus("current")


class _SleV2CpuPacketFilterActionTpid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterActionTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleV2CpuPacketFilterActionTpid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterActionTpid_Object = MibTableColumn
sleV2CpuPacketFilterActionTpid = _SleV2CpuPacketFilterActionTpid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 10),
    _SleV2CpuPacketFilterActionTpid_Type()
)
sleV2CpuPacketFilterActionTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterActionTpid.setStatus("current")


class _SleV2CpuPacketFilterActionPcp_Type(Integer32):
    """Custom type sleV2CpuPacketFilterActionPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_SleV2CpuPacketFilterActionPcp_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterActionPcp_Object = MibTableColumn
sleV2CpuPacketFilterActionPcp = _SleV2CpuPacketFilterActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 11),
    _SleV2CpuPacketFilterActionPcp_Type()
)
sleV2CpuPacketFilterActionPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterActionPcp.setStatus("current")


class _SleV2CpuPacketFilterActionVid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterActionVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_SleV2CpuPacketFilterActionVid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterActionVid_Object = MibTableColumn
sleV2CpuPacketFilterActionVid = _SleV2CpuPacketFilterActionVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 12),
    _SleV2CpuPacketFilterActionVid_Type()
)
sleV2CpuPacketFilterActionVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterActionVid.setStatus("current")


class _SleV2CpuPacketFilterActionTagPosition_Type(Integer32):
    """Custom type sleV2CpuPacketFilterActionTagPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_SleV2CpuPacketFilterActionTagPosition_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterActionTagPosition_Object = MibTableColumn
sleV2CpuPacketFilterActionTagPosition = _SleV2CpuPacketFilterActionTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 1, 1, 13),
    _SleV2CpuPacketFilterActionTagPosition_Type()
)
sleV2CpuPacketFilterActionTagPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterActionTagPosition.setStatus("current")
_SleV2CpuPacketFilterMatchTable_Object = MibTable
sleV2CpuPacketFilterMatchTable = _SleV2CpuPacketFilterMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2)
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchTable.setStatus("current")
_SleV2CpuPacketFilterMatchEntry_Object = MibTableRow
sleV2CpuPacketFilterMatchEntry = _SleV2CpuPacketFilterMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1)
)
sleV2CpuPacketFilterMatchEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2CpuPacketFilterIndex"),
    (0, "SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchIndex"),
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchEntry.setStatus("current")


class _SleV2CpuPacketFilterMatchIndex_Type(Integer32):
    """Custom type sleV2CpuPacketFilterMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2CpuPacketFilterMatchIndex_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterMatchIndex_Object = MibTableColumn
sleV2CpuPacketFilterMatchIndex = _SleV2CpuPacketFilterMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 1),
    _SleV2CpuPacketFilterMatchIndex_Type()
)
sleV2CpuPacketFilterMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchIndex.setStatus("current")


class _SleV2CpuPacketFilterMatchType_Type(Bits):
    """Custom type sleV2CpuPacketFilterMatchType based on Bits"""
    namedValues = NamedValues(
        *(("vid", 0),
          ("cos", 1),
          ("port", 2),
          ("offset", 3),
          ("dot1q", 4))
    )

_SleV2CpuPacketFilterMatchType_Type.__name__ = "Bits"
_SleV2CpuPacketFilterMatchType_Object = MibTableColumn
sleV2CpuPacketFilterMatchType = _SleV2CpuPacketFilterMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 2),
    _SleV2CpuPacketFilterMatchType_Type()
)
sleV2CpuPacketFilterMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchType.setStatus("current")
_SleV2CpuPacketFilterMatchCos_Type = OctetString
_SleV2CpuPacketFilterMatchCos_Object = MibTableColumn
sleV2CpuPacketFilterMatchCos = _SleV2CpuPacketFilterMatchCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 3),
    _SleV2CpuPacketFilterMatchCos_Type()
)
sleV2CpuPacketFilterMatchCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchCos.setStatus("current")
_SleV2CpuPacketFilterMatchPort_Type = OctetString
_SleV2CpuPacketFilterMatchPort_Object = MibTableColumn
sleV2CpuPacketFilterMatchPort = _SleV2CpuPacketFilterMatchPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 4),
    _SleV2CpuPacketFilterMatchPort_Type()
)
sleV2CpuPacketFilterMatchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchPort.setStatus("current")
_SleV2CpuPacketFilterMatchVidmap_Type = OctetString
_SleV2CpuPacketFilterMatchVidmap_Object = MibTableColumn
sleV2CpuPacketFilterMatchVidmap = _SleV2CpuPacketFilterMatchVidmap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 5),
    _SleV2CpuPacketFilterMatchVidmap_Type()
)
sleV2CpuPacketFilterMatchVidmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchVidmap.setStatus("current")


class _SleV2CpuPacketFilterMatchTagPosition_Type(Integer32):
    """Custom type sleV2CpuPacketFilterMatchTagPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_SleV2CpuPacketFilterMatchTagPosition_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterMatchTagPosition_Object = MibTableColumn
sleV2CpuPacketFilterMatchTagPosition = _SleV2CpuPacketFilterMatchTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 6),
    _SleV2CpuPacketFilterMatchTagPosition_Type()
)
sleV2CpuPacketFilterMatchTagPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchTagPosition.setStatus("current")


class _SleV2CpuPacketFilterMatchTpid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterMatchTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleV2CpuPacketFilterMatchTpid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterMatchTpid_Object = MibTableColumn
sleV2CpuPacketFilterMatchTpid = _SleV2CpuPacketFilterMatchTpid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 7),
    _SleV2CpuPacketFilterMatchTpid_Type()
)
sleV2CpuPacketFilterMatchTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchTpid.setStatus("current")


class _SleV2CpuPacketFilterMatchPcp_Type(Integer32):
    """Custom type sleV2CpuPacketFilterMatchPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_SleV2CpuPacketFilterMatchPcp_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterMatchPcp_Object = MibTableColumn
sleV2CpuPacketFilterMatchPcp = _SleV2CpuPacketFilterMatchPcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 8),
    _SleV2CpuPacketFilterMatchPcp_Type()
)
sleV2CpuPacketFilterMatchPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchPcp.setStatus("current")


class _SleV2CpuPacketFilterMatchVid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterMatchVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_SleV2CpuPacketFilterMatchVid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterMatchVid_Object = MibTableColumn
sleV2CpuPacketFilterMatchVid = _SleV2CpuPacketFilterMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 9),
    _SleV2CpuPacketFilterMatchVid_Type()
)
sleV2CpuPacketFilterMatchVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchVid.setStatus("current")


class _SleV2CpuPacketFilterMatchOffset_Type(Integer32):
    """Custom type sleV2CpuPacketFilterMatchOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SleV2CpuPacketFilterMatchOffset_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterMatchOffset_Object = MibTableColumn
sleV2CpuPacketFilterMatchOffset = _SleV2CpuPacketFilterMatchOffset_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 10),
    _SleV2CpuPacketFilterMatchOffset_Type()
)
sleV2CpuPacketFilterMatchOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchOffset.setStatus("current")


class _SleV2CpuPacketFilterMatchLength_Type(Integer32):
    """Custom type sleV2CpuPacketFilterMatchLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleV2CpuPacketFilterMatchLength_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterMatchLength_Object = MibTableColumn
sleV2CpuPacketFilterMatchLength = _SleV2CpuPacketFilterMatchLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 11),
    _SleV2CpuPacketFilterMatchLength_Type()
)
sleV2CpuPacketFilterMatchLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchLength.setStatus("current")
_SleV2CpuPacketFilterMatchData_Type = OctetString
_SleV2CpuPacketFilterMatchData_Object = MibTableColumn
sleV2CpuPacketFilterMatchData = _SleV2CpuPacketFilterMatchData_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 12),
    _SleV2CpuPacketFilterMatchData_Type()
)
sleV2CpuPacketFilterMatchData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchData.setStatus("current")
_SleV2CpuPacketFilterMatchMask_Type = OctetString
_SleV2CpuPacketFilterMatchMask_Object = MibTableColumn
sleV2CpuPacketFilterMatchMask = _SleV2CpuPacketFilterMatchMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 13),
    _SleV2CpuPacketFilterMatchMask_Type()
)
sleV2CpuPacketFilterMatchMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchMask.setStatus("current")
_SleV2CpuPacketFilterMatchDesc_Type = OctetString
_SleV2CpuPacketFilterMatchDesc_Object = MibTableColumn
sleV2CpuPacketFilterMatchDesc = _SleV2CpuPacketFilterMatchDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 2, 1, 14),
    _SleV2CpuPacketFilterMatchDesc_Type()
)
sleV2CpuPacketFilterMatchDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchDesc.setStatus("current")
_SleV2CpuPacketFilterControl_ObjectIdentity = ObjectIdentity
sleV2CpuPacketFilterControl = _SleV2CpuPacketFilterControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3)
)


class _SleV2CpuPacketFilterControlRequest_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlRequest based on Integer32"""
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
        *(("addCpuPktFilter", 1),
          ("delCpuPktfilter", 2),
          ("setAction", 3),
          ("addMatch", 4),
          ("delMatch", 5))
    )


_SleV2CpuPacketFilterControlRequest_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlRequest_Object = MibScalar
sleV2CpuPacketFilterControlRequest = _SleV2CpuPacketFilterControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 1),
    _SleV2CpuPacketFilterControlRequest_Type()
)
sleV2CpuPacketFilterControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlRequest.setStatus("current")
_SleV2CpuPacketFilterControlStatus_Type = SleControlStatusType
_SleV2CpuPacketFilterControlStatus_Object = MibScalar
sleV2CpuPacketFilterControlStatus = _SleV2CpuPacketFilterControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 2),
    _SleV2CpuPacketFilterControlStatus_Type()
)
sleV2CpuPacketFilterControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlStatus.setStatus("current")
_SleV2CpuPacketFilterControlTimer_Type = Gauge32
_SleV2CpuPacketFilterControlTimer_Object = MibScalar
sleV2CpuPacketFilterControlTimer = _SleV2CpuPacketFilterControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 3),
    _SleV2CpuPacketFilterControlTimer_Type()
)
sleV2CpuPacketFilterControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlTimer.setStatus("current")
_SleV2CpuPacketFilterControlTimeStamp_Type = TimeStamp
_SleV2CpuPacketFilterControlTimeStamp_Object = MibScalar
sleV2CpuPacketFilterControlTimeStamp = _SleV2CpuPacketFilterControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 4),
    _SleV2CpuPacketFilterControlTimeStamp_Type()
)
sleV2CpuPacketFilterControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlTimeStamp.setStatus("current")
_SleV2CpuPacketFilterControlReqResult_Type = SleControlRequestResultType
_SleV2CpuPacketFilterControlReqResult_Object = MibScalar
sleV2CpuPacketFilterControlReqResult = _SleV2CpuPacketFilterControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 5),
    _SleV2CpuPacketFilterControlReqResult_Type()
)
sleV2CpuPacketFilterControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlReqResult.setStatus("current")


class _SleV2CpuPacketFilterControlIndex_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleV2CpuPacketFilterControlIndex_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlIndex_Object = MibScalar
sleV2CpuPacketFilterControlIndex = _SleV2CpuPacketFilterControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 6),
    _SleV2CpuPacketFilterControlIndex_Type()
)
sleV2CpuPacketFilterControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlIndex.setStatus("current")
_SleV2CpuPacketFilterControlName_Type = OctetString
_SleV2CpuPacketFilterControlName_Object = MibScalar
sleV2CpuPacketFilterControlName = _SleV2CpuPacketFilterControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 7),
    _SleV2CpuPacketFilterControlName_Type()
)
sleV2CpuPacketFilterControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlName.setStatus("current")


class _SleV2CpuPacketFilterControlStage_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlStage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cpuingress", 1),
          ("cpuegress", 2),
          ("portrx", 3),
          ("porttx", 4),
          ("vlanAssigned", 5),
          ("unknown", 255))
    )


_SleV2CpuPacketFilterControlStage_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlStage_Object = MibScalar
sleV2CpuPacketFilterControlStage = _SleV2CpuPacketFilterControlStage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 8),
    _SleV2CpuPacketFilterControlStage_Type()
)
sleV2CpuPacketFilterControlStage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlStage.setStatus("current")


class _SleV2CpuPacketFilterControlPriority_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2CpuPacketFilterControlPriority_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlPriority_Object = MibScalar
sleV2CpuPacketFilterControlPriority = _SleV2CpuPacketFilterControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 9),
    _SleV2CpuPacketFilterControlPriority_Type()
)
sleV2CpuPacketFilterControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlPriority.setStatus("current")


class _SleV2CpuPacketFilterControlAction_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlAction based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("permit", 2),
          ("rateLimit", 3),
          ("pass", 4),
          ("dot1q", 5),
          ("dot1qAttach", 6),
          ("dot1qDetach", 7),
          ("unknown", 255))
    )


_SleV2CpuPacketFilterControlAction_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlAction_Object = MibScalar
sleV2CpuPacketFilterControlAction = _SleV2CpuPacketFilterControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 10),
    _SleV2CpuPacketFilterControlAction_Type()
)
sleV2CpuPacketFilterControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlAction.setStatus("current")


class _SleV2CpuPacketFilterControlActionRateLimit_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlActionRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleV2CpuPacketFilterControlActionRateLimit_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlActionRateLimit_Object = MibScalar
sleV2CpuPacketFilterControlActionRateLimit = _SleV2CpuPacketFilterControlActionRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 11),
    _SleV2CpuPacketFilterControlActionRateLimit_Type()
)
sleV2CpuPacketFilterControlActionRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlActionRateLimit.setStatus("current")


class _SleV2CpuPacketFilterControlActionBurstSize_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlActionBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleV2CpuPacketFilterControlActionBurstSize_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlActionBurstSize_Object = MibScalar
sleV2CpuPacketFilterControlActionBurstSize = _SleV2CpuPacketFilterControlActionBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 12),
    _SleV2CpuPacketFilterControlActionBurstSize_Type()
)
sleV2CpuPacketFilterControlActionBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlActionBurstSize.setStatus("current")


class _SleV2CpuPacketFilterControlActionTpid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlActionTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleV2CpuPacketFilterControlActionTpid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlActionTpid_Object = MibScalar
sleV2CpuPacketFilterControlActionTpid = _SleV2CpuPacketFilterControlActionTpid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 13),
    _SleV2CpuPacketFilterControlActionTpid_Type()
)
sleV2CpuPacketFilterControlActionTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlActionTpid.setStatus("current")


class _SleV2CpuPacketFilterControlActionPcp_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlActionPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_SleV2CpuPacketFilterControlActionPcp_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlActionPcp_Object = MibScalar
sleV2CpuPacketFilterControlActionPcp = _SleV2CpuPacketFilterControlActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 14),
    _SleV2CpuPacketFilterControlActionPcp_Type()
)
sleV2CpuPacketFilterControlActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlActionPcp.setStatus("current")


class _SleV2CpuPacketFilterControlActionVid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlActionVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_SleV2CpuPacketFilterControlActionVid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlActionVid_Object = MibScalar
sleV2CpuPacketFilterControlActionVid = _SleV2CpuPacketFilterControlActionVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 15),
    _SleV2CpuPacketFilterControlActionVid_Type()
)
sleV2CpuPacketFilterControlActionVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlActionVid.setStatus("current")


class _SleV2CpuPacketFilterControlActionTagPosition_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlActionTagPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_SleV2CpuPacketFilterControlActionTagPosition_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlActionTagPosition_Object = MibScalar
sleV2CpuPacketFilterControlActionTagPosition = _SleV2CpuPacketFilterControlActionTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 16),
    _SleV2CpuPacketFilterControlActionTagPosition_Type()
)
sleV2CpuPacketFilterControlActionTagPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlActionTagPosition.setStatus("current")


class _SleV2CpuPacketFilterControlMatchType_Type(Bits):
    """Custom type sleV2CpuPacketFilterControlMatchType based on Bits"""
    namedValues = NamedValues(
        *(("vid", 0),
          ("cos", 1),
          ("port", 2),
          ("offset", 3),
          ("dot1q", 4))
    )

_SleV2CpuPacketFilterControlMatchType_Type.__name__ = "Bits"
_SleV2CpuPacketFilterControlMatchType_Object = MibScalar
sleV2CpuPacketFilterControlMatchType = _SleV2CpuPacketFilterControlMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 17),
    _SleV2CpuPacketFilterControlMatchType_Type()
)
sleV2CpuPacketFilterControlMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchType.setStatus("current")
_SleV2CpuPacketFilterControlMatchCos_Type = OctetString
_SleV2CpuPacketFilterControlMatchCos_Object = MibScalar
sleV2CpuPacketFilterControlMatchCos = _SleV2CpuPacketFilterControlMatchCos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 18),
    _SleV2CpuPacketFilterControlMatchCos_Type()
)
sleV2CpuPacketFilterControlMatchCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchCos.setStatus("current")
_SleV2CpuPacketFilterControlMatchPort_Type = OctetString
_SleV2CpuPacketFilterControlMatchPort_Object = MibScalar
sleV2CpuPacketFilterControlMatchPort = _SleV2CpuPacketFilterControlMatchPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 19),
    _SleV2CpuPacketFilterControlMatchPort_Type()
)
sleV2CpuPacketFilterControlMatchPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchPort.setStatus("current")
_SleV2CpuPacketFilterControlMatchVidmap_Type = OctetString
_SleV2CpuPacketFilterControlMatchVidmap_Object = MibScalar
sleV2CpuPacketFilterControlMatchVidmap = _SleV2CpuPacketFilterControlMatchVidmap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 20),
    _SleV2CpuPacketFilterControlMatchVidmap_Type()
)
sleV2CpuPacketFilterControlMatchVidmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchVidmap.setStatus("current")


class _SleV2CpuPacketFilterControlMatchTagPosition_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlMatchTagPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_SleV2CpuPacketFilterControlMatchTagPosition_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlMatchTagPosition_Object = MibScalar
sleV2CpuPacketFilterControlMatchTagPosition = _SleV2CpuPacketFilterControlMatchTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 21),
    _SleV2CpuPacketFilterControlMatchTagPosition_Type()
)
sleV2CpuPacketFilterControlMatchTagPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchTagPosition.setStatus("current")


class _SleV2CpuPacketFilterControlMatchTpid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlMatchTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleV2CpuPacketFilterControlMatchTpid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlMatchTpid_Object = MibScalar
sleV2CpuPacketFilterControlMatchTpid = _SleV2CpuPacketFilterControlMatchTpid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 22),
    _SleV2CpuPacketFilterControlMatchTpid_Type()
)
sleV2CpuPacketFilterControlMatchTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchTpid.setStatus("current")


class _SleV2CpuPacketFilterControlMatchPcp_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlMatchPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_SleV2CpuPacketFilterControlMatchPcp_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlMatchPcp_Object = MibScalar
sleV2CpuPacketFilterControlMatchPcp = _SleV2CpuPacketFilterControlMatchPcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 23),
    _SleV2CpuPacketFilterControlMatchPcp_Type()
)
sleV2CpuPacketFilterControlMatchPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchPcp.setStatus("current")


class _SleV2CpuPacketFilterControlMatchVid_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlMatchVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_SleV2CpuPacketFilterControlMatchVid_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlMatchVid_Object = MibScalar
sleV2CpuPacketFilterControlMatchVid = _SleV2CpuPacketFilterControlMatchVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 24),
    _SleV2CpuPacketFilterControlMatchVid_Type()
)
sleV2CpuPacketFilterControlMatchVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchVid.setStatus("current")


class _SleV2CpuPacketFilterControlMatchOffset_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlMatchOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SleV2CpuPacketFilterControlMatchOffset_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlMatchOffset_Object = MibScalar
sleV2CpuPacketFilterControlMatchOffset = _SleV2CpuPacketFilterControlMatchOffset_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 25),
    _SleV2CpuPacketFilterControlMatchOffset_Type()
)
sleV2CpuPacketFilterControlMatchOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchOffset.setStatus("current")


class _SleV2CpuPacketFilterControlMatchLength_Type(Integer32):
    """Custom type sleV2CpuPacketFilterControlMatchLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleV2CpuPacketFilterControlMatchLength_Type.__name__ = "Integer32"
_SleV2CpuPacketFilterControlMatchLength_Object = MibScalar
sleV2CpuPacketFilterControlMatchLength = _SleV2CpuPacketFilterControlMatchLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 26),
    _SleV2CpuPacketFilterControlMatchLength_Type()
)
sleV2CpuPacketFilterControlMatchLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchLength.setStatus("current")
_SleV2CpuPacketFilterControlMatchData_Type = OctetString
_SleV2CpuPacketFilterControlMatchData_Object = MibScalar
sleV2CpuPacketFilterControlMatchData = _SleV2CpuPacketFilterControlMatchData_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 27),
    _SleV2CpuPacketFilterControlMatchData_Type()
)
sleV2CpuPacketFilterControlMatchData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchData.setStatus("current")
_SleV2CpuPacketFilterControlMatchMask_Type = OctetString
_SleV2CpuPacketFilterControlMatchMask_Object = MibScalar
sleV2CpuPacketFilterControlMatchMask = _SleV2CpuPacketFilterControlMatchMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 28),
    _SleV2CpuPacketFilterControlMatchMask_Type()
)
sleV2CpuPacketFilterControlMatchMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchMask.setStatus("current")
_SleV2CpuPacketFilterControlMatchDesc_Type = OctetString
_SleV2CpuPacketFilterControlMatchDesc_Object = MibScalar
sleV2CpuPacketFilterControlMatchDesc = _SleV2CpuPacketFilterControlMatchDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 3, 29),
    _SleV2CpuPacketFilterControlMatchDesc_Type()
)
sleV2CpuPacketFilterControlMatchDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterControlMatchDesc.setStatus("current")
_SleV2CpuPacketFilterNotification_ObjectIdentity = ObjectIdentity
sleV2CpuPacketFilterNotification = _SleV2CpuPacketFilterNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 4)
)
_SleV2VlanOperation_ObjectIdentity = ObjectIdentity
sleV2VlanOperation = _SleV2VlanOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9)
)
_SleV2VlanOperationTable_Object = MibTable
sleV2VlanOperationTable = _SleV2VlanOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1)
)
if mibBuilder.loadTexts:
    sleV2VlanOperationTable.setStatus("current")
_SleV2VlanOperationEntry_Object = MibTableRow
sleV2VlanOperationEntry = _SleV2VlanOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1)
)
sleV2VlanOperationEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2VlanOperationIndex"),
    (0, "SLEV2-Security-MIB", "sleV2VlanOperationName"),
)
if mibBuilder.loadTexts:
    sleV2VlanOperationEntry.setStatus("current")


class _SleV2VlanOperationIndex_Type(Integer32):
    """Custom type sleV2VlanOperationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65565),
    )


_SleV2VlanOperationIndex_Type.__name__ = "Integer32"
_SleV2VlanOperationIndex_Object = MibTableColumn
sleV2VlanOperationIndex = _SleV2VlanOperationIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 1),
    _SleV2VlanOperationIndex_Type()
)
sleV2VlanOperationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationIndex.setStatus("current")
_SleV2VlanOperationName_Type = OctetString
_SleV2VlanOperationName_Object = MibTableColumn
sleV2VlanOperationName = _SleV2VlanOperationName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 2),
    _SleV2VlanOperationName_Type()
)
sleV2VlanOperationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationName.setStatus("current")


class _SleV2VlanOperationStage_Type(Integer32):
    """Custom type sleV2VlanOperationStage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingressSlowPath", 1),
          ("egressSlowPath", 2))
    )


_SleV2VlanOperationStage_Type.__name__ = "Integer32"
_SleV2VlanOperationStage_Object = MibTableColumn
sleV2VlanOperationStage = _SleV2VlanOperationStage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 3),
    _SleV2VlanOperationStage_Type()
)
sleV2VlanOperationStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationStage.setStatus("current")


class _SleV2VlanOperationProiroty_Type(Integer32):
    """Custom type sleV2VlanOperationProiroty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2VlanOperationProiroty_Type.__name__ = "Integer32"
_SleV2VlanOperationProiroty_Object = MibTableColumn
sleV2VlanOperationProiroty = _SleV2VlanOperationProiroty_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 4),
    _SleV2VlanOperationProiroty_Type()
)
sleV2VlanOperationProiroty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationProiroty.setStatus("current")
_SleV2VlanOperationPort_Type = OctetString
_SleV2VlanOperationPort_Object = MibTableColumn
sleV2VlanOperationPort = _SleV2VlanOperationPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 5),
    _SleV2VlanOperationPort_Type()
)
sleV2VlanOperationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationPort.setStatus("current")
_SleV2VlanOperationOuterVlan_Type = OctetString
_SleV2VlanOperationOuterVlan_Object = MibTableColumn
sleV2VlanOperationOuterVlan = _SleV2VlanOperationOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 6),
    _SleV2VlanOperationOuterVlan_Type()
)
sleV2VlanOperationOuterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationOuterVlan.setStatus("current")
_SleV2VlanOperationInnerVlan_Type = OctetString
_SleV2VlanOperationInnerVlan_Object = MibTableColumn
sleV2VlanOperationInnerVlan = _SleV2VlanOperationInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 7),
    _SleV2VlanOperationInnerVlan_Type()
)
sleV2VlanOperationInnerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationInnerVlan.setStatus("current")
_SleV2VlanOperationEtherType_Type = Integer32
_SleV2VlanOperationEtherType_Object = MibTableColumn
sleV2VlanOperationEtherType = _SleV2VlanOperationEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 8),
    _SleV2VlanOperationEtherType_Type()
)
sleV2VlanOperationEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationEtherType.setStatus("current")
_SleV2VlanOperationIpProtocol_Type = Integer32
_SleV2VlanOperationIpProtocol_Object = MibTableColumn
sleV2VlanOperationIpProtocol = _SleV2VlanOperationIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 9),
    _SleV2VlanOperationIpProtocol_Type()
)
sleV2VlanOperationIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationIpProtocol.setStatus("current")
_SleV2VlanOperationArpSip_Type = OctetString
_SleV2VlanOperationArpSip_Object = MibTableColumn
sleV2VlanOperationArpSip = _SleV2VlanOperationArpSip_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 10),
    _SleV2VlanOperationArpSip_Type()
)
sleV2VlanOperationArpSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationArpSip.setStatus("current")
_SleV2VlanOperationArpSipPfxLen_Type = Integer32
_SleV2VlanOperationArpSipPfxLen_Object = MibTableColumn
sleV2VlanOperationArpSipPfxLen = _SleV2VlanOperationArpSipPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 11),
    _SleV2VlanOperationArpSipPfxLen_Type()
)
sleV2VlanOperationArpSipPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationArpSipPfxLen.setStatus("current")
_SleV2VlanOperationSip_Type = OctetString
_SleV2VlanOperationSip_Object = MibTableColumn
sleV2VlanOperationSip = _SleV2VlanOperationSip_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 12),
    _SleV2VlanOperationSip_Type()
)
sleV2VlanOperationSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationSip.setStatus("current")
_SleV2VlanOperationSipPfxLen_Type = Integer32
_SleV2VlanOperationSipPfxLen_Object = MibTableColumn
sleV2VlanOperationSipPfxLen = _SleV2VlanOperationSipPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 13),
    _SleV2VlanOperationSipPfxLen_Type()
)
sleV2VlanOperationSipPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationSipPfxLen.setStatus("current")
_SleV2VlanOperationDip_Type = OctetString
_SleV2VlanOperationDip_Object = MibTableColumn
sleV2VlanOperationDip = _SleV2VlanOperationDip_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 14),
    _SleV2VlanOperationDip_Type()
)
sleV2VlanOperationDip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationDip.setStatus("current")
_SleV2VlanOperationDipPfxLen_Type = Integer32
_SleV2VlanOperationDipPfxLen_Object = MibTableColumn
sleV2VlanOperationDipPfxLen = _SleV2VlanOperationDipPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 15),
    _SleV2VlanOperationDipPfxLen_Type()
)
sleV2VlanOperationDipPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationDipPfxLen.setStatus("current")


class _SleV2VlanOperationAction_Type(Integer32):
    """Custom type sleV2VlanOperationAction based on Integer32"""
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
        *(("addServiceVlanTag", 1),
          ("replaceServiceVlanID", 2),
          ("removeServiceVlanTag", 3),
          ("addCustomerVlanTag", 4),
          ("replaceCustomerVlanID", 5),
          ("removeCustomerVlanTag", 6))
    )


_SleV2VlanOperationAction_Type.__name__ = "Integer32"
_SleV2VlanOperationAction_Object = MibTableColumn
sleV2VlanOperationAction = _SleV2VlanOperationAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 16),
    _SleV2VlanOperationAction_Type()
)
sleV2VlanOperationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationAction.setStatus("current")


class _SleV2VlanOperationActionVid_Type(Integer32):
    """Custom type sleV2VlanOperationActionVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SleV2VlanOperationActionVid_Type.__name__ = "Integer32"
_SleV2VlanOperationActionVid_Object = MibTableColumn
sleV2VlanOperationActionVid = _SleV2VlanOperationActionVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 1, 1, 17),
    _SleV2VlanOperationActionVid_Type()
)
sleV2VlanOperationActionVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationActionVid.setStatus("current")
_SleV2VlanOperationControl_ObjectIdentity = ObjectIdentity
sleV2VlanOperationControl = _SleV2VlanOperationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2)
)


class _SleV2VlanOperationControlRequest_Type(Integer32):
    """Custom type sleV2VlanOperationControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addVlanOperation", 1),
          ("delVlanOperation", 2))
    )


_SleV2VlanOperationControlRequest_Type.__name__ = "Integer32"
_SleV2VlanOperationControlRequest_Object = MibScalar
sleV2VlanOperationControlRequest = _SleV2VlanOperationControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 1),
    _SleV2VlanOperationControlRequest_Type()
)
sleV2VlanOperationControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlRequest.setStatus("current")
_SleV2VlanOperationControlStatus_Type = SleControlStatusType
_SleV2VlanOperationControlStatus_Object = MibScalar
sleV2VlanOperationControlStatus = _SleV2VlanOperationControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 2),
    _SleV2VlanOperationControlStatus_Type()
)
sleV2VlanOperationControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlStatus.setStatus("current")
_SleV2VlanOperationControlTimer_Type = Gauge32
_SleV2VlanOperationControlTimer_Object = MibScalar
sleV2VlanOperationControlTimer = _SleV2VlanOperationControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 3),
    _SleV2VlanOperationControlTimer_Type()
)
sleV2VlanOperationControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlTimer.setStatus("current")
_SleV2VlanOperationControlTimeStamp_Type = TimeTicks
_SleV2VlanOperationControlTimeStamp_Object = MibScalar
sleV2VlanOperationControlTimeStamp = _SleV2VlanOperationControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 4),
    _SleV2VlanOperationControlTimeStamp_Type()
)
sleV2VlanOperationControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlTimeStamp.setStatus("current")
_SleV2VlanOperationControlReqResult_Type = SleControlRequestResultType
_SleV2VlanOperationControlReqResult_Object = MibScalar
sleV2VlanOperationControlReqResult = _SleV2VlanOperationControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 5),
    _SleV2VlanOperationControlReqResult_Type()
)
sleV2VlanOperationControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlReqResult.setStatus("current")


class _SleV2VlanOperationControlIndex_Type(Integer32):
    """Custom type sleV2VlanOperationControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2VlanOperationControlIndex_Type.__name__ = "Integer32"
_SleV2VlanOperationControlIndex_Object = MibScalar
sleV2VlanOperationControlIndex = _SleV2VlanOperationControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 6),
    _SleV2VlanOperationControlIndex_Type()
)
sleV2VlanOperationControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlIndex.setStatus("current")
_SleV2VlanOperationControlName_Type = OctetString
_SleV2VlanOperationControlName_Object = MibScalar
sleV2VlanOperationControlName = _SleV2VlanOperationControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 7),
    _SleV2VlanOperationControlName_Type()
)
sleV2VlanOperationControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlName.setStatus("current")


class _SleV2VlanOperationControlStage_Type(Integer32):
    """Custom type sleV2VlanOperationControlStage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingressSlowPath", 1),
          ("egressSlowPath", 2))
    )


_SleV2VlanOperationControlStage_Type.__name__ = "Integer32"
_SleV2VlanOperationControlStage_Object = MibScalar
sleV2VlanOperationControlStage = _SleV2VlanOperationControlStage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 8),
    _SleV2VlanOperationControlStage_Type()
)
sleV2VlanOperationControlStage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlStage.setStatus("current")


class _SleV2VlanOperationControlProiroty_Type(Integer32):
    """Custom type sleV2VlanOperationControlProiroty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2VlanOperationControlProiroty_Type.__name__ = "Integer32"
_SleV2VlanOperationControlProiroty_Object = MibScalar
sleV2VlanOperationControlProiroty = _SleV2VlanOperationControlProiroty_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 9),
    _SleV2VlanOperationControlProiroty_Type()
)
sleV2VlanOperationControlProiroty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlProiroty.setStatus("current")
_SleV2VlanOperationControlPort_Type = OctetString
_SleV2VlanOperationControlPort_Object = MibScalar
sleV2VlanOperationControlPort = _SleV2VlanOperationControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 10),
    _SleV2VlanOperationControlPort_Type()
)
sleV2VlanOperationControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlPort.setStatus("current")
_SleV2VlanOperationControlOuterVlan_Type = OctetString
_SleV2VlanOperationControlOuterVlan_Object = MibScalar
sleV2VlanOperationControlOuterVlan = _SleV2VlanOperationControlOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 11),
    _SleV2VlanOperationControlOuterVlan_Type()
)
sleV2VlanOperationControlOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlOuterVlan.setStatus("current")
_SleV2VlanOperationControlInnerVlan_Type = OctetString
_SleV2VlanOperationControlInnerVlan_Object = MibScalar
sleV2VlanOperationControlInnerVlan = _SleV2VlanOperationControlInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 12),
    _SleV2VlanOperationControlInnerVlan_Type()
)
sleV2VlanOperationControlInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlInnerVlan.setStatus("current")
_SleV2VlanOperationControlEtherType_Type = Integer32
_SleV2VlanOperationControlEtherType_Object = MibScalar
sleV2VlanOperationControlEtherType = _SleV2VlanOperationControlEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 13),
    _SleV2VlanOperationControlEtherType_Type()
)
sleV2VlanOperationControlEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlEtherType.setStatus("current")
_SleV2VlanOperationControlIpProtocol_Type = Integer32
_SleV2VlanOperationControlIpProtocol_Object = MibScalar
sleV2VlanOperationControlIpProtocol = _SleV2VlanOperationControlIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 14),
    _SleV2VlanOperationControlIpProtocol_Type()
)
sleV2VlanOperationControlIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlIpProtocol.setStatus("current")
_SleV2VlanOperationControlArpSip_Type = OctetString
_SleV2VlanOperationControlArpSip_Object = MibScalar
sleV2VlanOperationControlArpSip = _SleV2VlanOperationControlArpSip_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 15),
    _SleV2VlanOperationControlArpSip_Type()
)
sleV2VlanOperationControlArpSip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlArpSip.setStatus("current")
_SleV2VlanOperationControlArpSipPfxLen_Type = Integer32
_SleV2VlanOperationControlArpSipPfxLen_Object = MibScalar
sleV2VlanOperationControlArpSipPfxLen = _SleV2VlanOperationControlArpSipPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 16),
    _SleV2VlanOperationControlArpSipPfxLen_Type()
)
sleV2VlanOperationControlArpSipPfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlArpSipPfxLen.setStatus("current")
_SleV2VlanOperationControlSip_Type = OctetString
_SleV2VlanOperationControlSip_Object = MibScalar
sleV2VlanOperationControlSip = _SleV2VlanOperationControlSip_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 17),
    _SleV2VlanOperationControlSip_Type()
)
sleV2VlanOperationControlSip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlSip.setStatus("current")
_SleV2VlanOperationControlSipPfxLen_Type = Integer32
_SleV2VlanOperationControlSipPfxLen_Object = MibScalar
sleV2VlanOperationControlSipPfxLen = _SleV2VlanOperationControlSipPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 18),
    _SleV2VlanOperationControlSipPfxLen_Type()
)
sleV2VlanOperationControlSipPfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlSipPfxLen.setStatus("current")
_SleV2VlanOperationControlDip_Type = OctetString
_SleV2VlanOperationControlDip_Object = MibScalar
sleV2VlanOperationControlDip = _SleV2VlanOperationControlDip_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 19),
    _SleV2VlanOperationControlDip_Type()
)
sleV2VlanOperationControlDip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlDip.setStatus("current")
_SleV2VlanOperationControlDipPfxLen_Type = Integer32
_SleV2VlanOperationControlDipPfxLen_Object = MibScalar
sleV2VlanOperationControlDipPfxLen = _SleV2VlanOperationControlDipPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 20),
    _SleV2VlanOperationControlDipPfxLen_Type()
)
sleV2VlanOperationControlDipPfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlDipPfxLen.setStatus("current")


class _SleV2VlanOperationControlAction_Type(Integer32):
    """Custom type sleV2VlanOperationControlAction based on Integer32"""
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
        *(("addServiceVlanTag", 1),
          ("replaceServiceVlanID", 2),
          ("removeServiceVlanTag", 3),
          ("addCustomerVlanTag", 4),
          ("replaceCustomerVlanID", 5),
          ("removeCustomerVlanTag", 6))
    )


_SleV2VlanOperationControlAction_Type.__name__ = "Integer32"
_SleV2VlanOperationControlAction_Object = MibScalar
sleV2VlanOperationControlAction = _SleV2VlanOperationControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 21),
    _SleV2VlanOperationControlAction_Type()
)
sleV2VlanOperationControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlAction.setStatus("current")


class _SleV2VlanOperationControlActionVid_Type(Integer32):
    """Custom type sleV2VlanOperationControlActionVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SleV2VlanOperationControlActionVid_Type.__name__ = "Integer32"
_SleV2VlanOperationControlActionVid_Object = MibScalar
sleV2VlanOperationControlActionVid = _SleV2VlanOperationControlActionVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 2, 22),
    _SleV2VlanOperationControlActionVid_Type()
)
sleV2VlanOperationControlActionVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2VlanOperationControlActionVid.setStatus("current")
_SleV2VlanOperationNotification_ObjectIdentity = ObjectIdentity
sleV2VlanOperationNotification = _SleV2VlanOperationNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 3)
)
_SleV2EthernetService_ObjectIdentity = ObjectIdentity
sleV2EthernetService = _SleV2EthernetService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10)
)
_SleV2EthernetServiceBase_ObjectIdentity = ObjectIdentity
sleV2EthernetServiceBase = _SleV2EthernetServiceBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 1)
)


class _SleV2EthernetServiceEnableStatus_Type(Integer32):
    """Custom type sleV2EthernetServiceEnableStatus based on Integer32"""
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
          ("rt", 1),
          ("cot", 2))
    )


_SleV2EthernetServiceEnableStatus_Type.__name__ = "Integer32"
_SleV2EthernetServiceEnableStatus_Object = MibScalar
sleV2EthernetServiceEnableStatus = _SleV2EthernetServiceEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 1, 1),
    _SleV2EthernetServiceEnableStatus_Type()
)
sleV2EthernetServiceEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceEnableStatus.setStatus("current")


class _SleV2EthernetServiceEnableManagement_Type(Integer32):
    """Custom type sleV2EthernetServiceEnableManagement based on Integer32"""
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


_SleV2EthernetServiceEnableManagement_Type.__name__ = "Integer32"
_SleV2EthernetServiceEnableManagement_Object = MibScalar
sleV2EthernetServiceEnableManagement = _SleV2EthernetServiceEnableManagement_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 1, 2),
    _SleV2EthernetServiceEnableManagement_Type()
)
sleV2EthernetServiceEnableManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceEnableManagement.setStatus("current")
_SleV2EthernetServiceHealthCheckPort_Type = OctetString
_SleV2EthernetServiceHealthCheckPort_Object = MibScalar
sleV2EthernetServiceHealthCheckPort = _SleV2EthernetServiceHealthCheckPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 1, 3),
    _SleV2EthernetServiceHealthCheckPort_Type()
)
sleV2EthernetServiceHealthCheckPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceHealthCheckPort.setStatus("current")
_SleV2EthernetServiceHealthCheckVid_Type = OctetString
_SleV2EthernetServiceHealthCheckVid_Object = MibScalar
sleV2EthernetServiceHealthCheckVid = _SleV2EthernetServiceHealthCheckVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 1, 4),
    _SleV2EthernetServiceHealthCheckVid_Type()
)
sleV2EthernetServiceHealthCheckVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceHealthCheckVid.setStatus("current")
_SleV2EthernetServiceTable_Object = MibTable
sleV2EthernetServiceTable = _SleV2EthernetServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2)
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceTable.setStatus("current")
_SleV2EthernetServiceEntry_Object = MibTableRow
sleV2EthernetServiceEntry = _SleV2EthernetServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1)
)
sleV2EthernetServiceEntry.setIndexNames(
    (0, "SLEV2-Security-MIB", "sleV2EthernetServiceSid"),
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceEntry.setStatus("current")


class _SleV2EthernetServiceSid_Type(Integer32):
    """Custom type sleV2EthernetServiceSid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2EthernetServiceSid_Type.__name__ = "Integer32"
_SleV2EthernetServiceSid_Object = MibTableColumn
sleV2EthernetServiceSid = _SleV2EthernetServiceSid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 1),
    _SleV2EthernetServiceSid_Type()
)
sleV2EthernetServiceSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceSid.setStatus("current")


class _SleV2EthernetServiceType_Type(Integer32):
    """Custom type sleV2EthernetServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_SleV2EthernetServiceType_Type.__name__ = "Integer32"
_SleV2EthernetServiceType_Object = MibTableColumn
sleV2EthernetServiceType = _SleV2EthernetServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 2),
    _SleV2EthernetServiceType_Type()
)
sleV2EthernetServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceType.setStatus("current")
_SleV2EthernetServiceRtCustomerPort_Type = OctetString
_SleV2EthernetServiceRtCustomerPort_Object = MibTableColumn
sleV2EthernetServiceRtCustomerPort = _SleV2EthernetServiceRtCustomerPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 3),
    _SleV2EthernetServiceRtCustomerPort_Type()
)
sleV2EthernetServiceRtCustomerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceRtCustomerPort.setStatus("current")
_SleV2EthernetServiceRtCustomerVid_Type = OctetString
_SleV2EthernetServiceRtCustomerVid_Object = MibTableColumn
sleV2EthernetServiceRtCustomerVid = _SleV2EthernetServiceRtCustomerVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 4),
    _SleV2EthernetServiceRtCustomerVid_Type()
)
sleV2EthernetServiceRtCustomerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceRtCustomerVid.setStatus("current")
_SleV2EthernetServiceRtNetworkPort_Type = OctetString
_SleV2EthernetServiceRtNetworkPort_Object = MibTableColumn
sleV2EthernetServiceRtNetworkPort = _SleV2EthernetServiceRtNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 5),
    _SleV2EthernetServiceRtNetworkPort_Type()
)
sleV2EthernetServiceRtNetworkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceRtNetworkPort.setStatus("current")
_SleV2EthernetServiceRtNetworkVid_Type = OctetString
_SleV2EthernetServiceRtNetworkVid_Object = MibTableColumn
sleV2EthernetServiceRtNetworkVid = _SleV2EthernetServiceRtNetworkVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 6),
    _SleV2EthernetServiceRtNetworkVid_Type()
)
sleV2EthernetServiceRtNetworkVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceRtNetworkVid.setStatus("current")


class _SleV2EthernetServiceRtEnableManagement_Type(Integer32):
    """Custom type sleV2EthernetServiceRtEnableManagement based on Integer32"""
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


_SleV2EthernetServiceRtEnableManagement_Type.__name__ = "Integer32"
_SleV2EthernetServiceRtEnableManagement_Object = MibTableColumn
sleV2EthernetServiceRtEnableManagement = _SleV2EthernetServiceRtEnableManagement_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 7),
    _SleV2EthernetServiceRtEnableManagement_Type()
)
sleV2EthernetServiceRtEnableManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceRtEnableManagement.setStatus("current")
_SleV2EthernetServiceCotExternalPort_Type = OctetString
_SleV2EthernetServiceCotExternalPort_Object = MibTableColumn
sleV2EthernetServiceCotExternalPort = _SleV2EthernetServiceCotExternalPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 8),
    _SleV2EthernetServiceCotExternalPort_Type()
)
sleV2EthernetServiceCotExternalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceCotExternalPort.setStatus("current")
_SleV2EthernetServiceCotExternalVid_Type = OctetString
_SleV2EthernetServiceCotExternalVid_Object = MibTableColumn
sleV2EthernetServiceCotExternalVid = _SleV2EthernetServiceCotExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 9),
    _SleV2EthernetServiceCotExternalVid_Type()
)
sleV2EthernetServiceCotExternalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceCotExternalVid.setStatus("current")
_SleV2EthernetServiceCotInternalPort_Type = OctetString
_SleV2EthernetServiceCotInternalPort_Object = MibTableColumn
sleV2EthernetServiceCotInternalPort = _SleV2EthernetServiceCotInternalPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 10),
    _SleV2EthernetServiceCotInternalPort_Type()
)
sleV2EthernetServiceCotInternalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceCotInternalPort.setStatus("current")
_SleV2EthernetServiceCotInternalVid_Type = OctetString
_SleV2EthernetServiceCotInternalVid_Object = MibTableColumn
sleV2EthernetServiceCotInternalVid = _SleV2EthernetServiceCotInternalVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 2, 1, 11),
    _SleV2EthernetServiceCotInternalVid_Type()
)
sleV2EthernetServiceCotInternalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceCotInternalVid.setStatus("current")
_SleV2EthernetServiceControl_ObjectIdentity = ObjectIdentity
sleV2EthernetServiceControl = _SleV2EthernetServiceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3)
)


class _SleV2EthernetServiceControlRequest_Type(Integer32):
    """Custom type sleV2EthernetServiceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("setEnableStatus", 1),
          ("setEnableManagement", 2),
          ("setHealthCheck", 3),
          ("delHealthCheck", 4),
          ("setSidForRT", 5),
          ("setSidForCOT", 6),
          ("delService", 7))
    )


_SleV2EthernetServiceControlRequest_Type.__name__ = "Integer32"
_SleV2EthernetServiceControlRequest_Object = MibScalar
sleV2EthernetServiceControlRequest = _SleV2EthernetServiceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 1),
    _SleV2EthernetServiceControlRequest_Type()
)
sleV2EthernetServiceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlRequest.setStatus("current")
_SleV2EthernetServiceControlStatus_Type = SleControlStatusType
_SleV2EthernetServiceControlStatus_Object = MibScalar
sleV2EthernetServiceControlStatus = _SleV2EthernetServiceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 2),
    _SleV2EthernetServiceControlStatus_Type()
)
sleV2EthernetServiceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlStatus.setStatus("current")
_SleV2EthernetServiceControlTimer_Type = Gauge32
_SleV2EthernetServiceControlTimer_Object = MibScalar
sleV2EthernetServiceControlTimer = _SleV2EthernetServiceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 3),
    _SleV2EthernetServiceControlTimer_Type()
)
sleV2EthernetServiceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlTimer.setStatus("current")
_SleV2EthernetServiceControlTimeStamp_Type = TimeTicks
_SleV2EthernetServiceControlTimeStamp_Object = MibScalar
sleV2EthernetServiceControlTimeStamp = _SleV2EthernetServiceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 4),
    _SleV2EthernetServiceControlTimeStamp_Type()
)
sleV2EthernetServiceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlTimeStamp.setStatus("current")
_SleV2EthernetServiceControlReqResult_Type = SleControlRequestResultType
_SleV2EthernetServiceControlReqResult_Object = MibScalar
sleV2EthernetServiceControlReqResult = _SleV2EthernetServiceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 5),
    _SleV2EthernetServiceControlReqResult_Type()
)
sleV2EthernetServiceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlReqResult.setStatus("current")


class _SleV2EthernetServiceControlEnableStatus_Type(Integer32):
    """Custom type sleV2EthernetServiceControlEnableStatus based on Integer32"""
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
          ("rt", 1),
          ("cot", 2))
    )


_SleV2EthernetServiceControlEnableStatus_Type.__name__ = "Integer32"
_SleV2EthernetServiceControlEnableStatus_Object = MibScalar
sleV2EthernetServiceControlEnableStatus = _SleV2EthernetServiceControlEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 6),
    _SleV2EthernetServiceControlEnableStatus_Type()
)
sleV2EthernetServiceControlEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlEnableStatus.setStatus("current")


class _SleV2EthernetServiceControlEnableManagement_Type(Integer32):
    """Custom type sleV2EthernetServiceControlEnableManagement based on Integer32"""
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


_SleV2EthernetServiceControlEnableManagement_Type.__name__ = "Integer32"
_SleV2EthernetServiceControlEnableManagement_Object = MibScalar
sleV2EthernetServiceControlEnableManagement = _SleV2EthernetServiceControlEnableManagement_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 7),
    _SleV2EthernetServiceControlEnableManagement_Type()
)
sleV2EthernetServiceControlEnableManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlEnableManagement.setStatus("current")
_SleV2EthernetServiceControlHealthCheckPort_Type = OctetString
_SleV2EthernetServiceControlHealthCheckPort_Object = MibScalar
sleV2EthernetServiceControlHealthCheckPort = _SleV2EthernetServiceControlHealthCheckPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 8),
    _SleV2EthernetServiceControlHealthCheckPort_Type()
)
sleV2EthernetServiceControlHealthCheckPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlHealthCheckPort.setStatus("current")
_SleV2EthernetServiceControlHealthCheckVid_Type = OctetString
_SleV2EthernetServiceControlHealthCheckVid_Object = MibScalar
sleV2EthernetServiceControlHealthCheckVid = _SleV2EthernetServiceControlHealthCheckVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 9),
    _SleV2EthernetServiceControlHealthCheckVid_Type()
)
sleV2EthernetServiceControlHealthCheckVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlHealthCheckVid.setStatus("current")


class _SleV2EthernetServiceControlSid_Type(Integer32):
    """Custom type sleV2EthernetServiceControlSid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2EthernetServiceControlSid_Type.__name__ = "Integer32"
_SleV2EthernetServiceControlSid_Object = MibScalar
sleV2EthernetServiceControlSid = _SleV2EthernetServiceControlSid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 10),
    _SleV2EthernetServiceControlSid_Type()
)
sleV2EthernetServiceControlSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlSid.setStatus("current")


class _SleV2EthernetServiceControlType_Type(Integer32):
    """Custom type sleV2EthernetServiceControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_SleV2EthernetServiceControlType_Type.__name__ = "Integer32"
_SleV2EthernetServiceControlType_Object = MibScalar
sleV2EthernetServiceControlType = _SleV2EthernetServiceControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 11),
    _SleV2EthernetServiceControlType_Type()
)
sleV2EthernetServiceControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlType.setStatus("current")
_SleV2EthernetServiceControlRtCustomerPort_Type = OctetString
_SleV2EthernetServiceControlRtCustomerPort_Object = MibScalar
sleV2EthernetServiceControlRtCustomerPort = _SleV2EthernetServiceControlRtCustomerPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 12),
    _SleV2EthernetServiceControlRtCustomerPort_Type()
)
sleV2EthernetServiceControlRtCustomerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlRtCustomerPort.setStatus("current")
_SleV2EthernetServiceControlRtCustomerVid_Type = OctetString
_SleV2EthernetServiceControlRtCustomerVid_Object = MibScalar
sleV2EthernetServiceControlRtCustomerVid = _SleV2EthernetServiceControlRtCustomerVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 13),
    _SleV2EthernetServiceControlRtCustomerVid_Type()
)
sleV2EthernetServiceControlRtCustomerVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlRtCustomerVid.setStatus("current")
_SleV2EthernetServiceControlRtNetworkPort_Type = OctetString
_SleV2EthernetServiceControlRtNetworkPort_Object = MibScalar
sleV2EthernetServiceControlRtNetworkPort = _SleV2EthernetServiceControlRtNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 14),
    _SleV2EthernetServiceControlRtNetworkPort_Type()
)
sleV2EthernetServiceControlRtNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlRtNetworkPort.setStatus("current")
_SleV2EthernetServiceControlRtNetworkVid_Type = OctetString
_SleV2EthernetServiceControlRtNetworkVid_Object = MibScalar
sleV2EthernetServiceControlRtNetworkVid = _SleV2EthernetServiceControlRtNetworkVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 15),
    _SleV2EthernetServiceControlRtNetworkVid_Type()
)
sleV2EthernetServiceControlRtNetworkVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlRtNetworkVid.setStatus("current")


class _SleV2EthernetServiceControlRtEnableManagement_Type(Integer32):
    """Custom type sleV2EthernetServiceControlRtEnableManagement based on Integer32"""
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


_SleV2EthernetServiceControlRtEnableManagement_Type.__name__ = "Integer32"
_SleV2EthernetServiceControlRtEnableManagement_Object = MibScalar
sleV2EthernetServiceControlRtEnableManagement = _SleV2EthernetServiceControlRtEnableManagement_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 16),
    _SleV2EthernetServiceControlRtEnableManagement_Type()
)
sleV2EthernetServiceControlRtEnableManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlRtEnableManagement.setStatus("current")
_SleV2EthernetServiceControlCotExternalPort_Type = OctetString
_SleV2EthernetServiceControlCotExternalPort_Object = MibScalar
sleV2EthernetServiceControlCotExternalPort = _SleV2EthernetServiceControlCotExternalPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 17),
    _SleV2EthernetServiceControlCotExternalPort_Type()
)
sleV2EthernetServiceControlCotExternalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlCotExternalPort.setStatus("current")
_SleV2EthernetServiceControlCotExternalVid_Type = OctetString
_SleV2EthernetServiceControlCotExternalVid_Object = MibScalar
sleV2EthernetServiceControlCotExternalVid = _SleV2EthernetServiceControlCotExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 18),
    _SleV2EthernetServiceControlCotExternalVid_Type()
)
sleV2EthernetServiceControlCotExternalVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlCotExternalVid.setStatus("current")
_SleV2EthernetServiceControlCotInternalPort_Type = OctetString
_SleV2EthernetServiceControlCotInternalPort_Object = MibScalar
sleV2EthernetServiceControlCotInternalPort = _SleV2EthernetServiceControlCotInternalPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 19),
    _SleV2EthernetServiceControlCotInternalPort_Type()
)
sleV2EthernetServiceControlCotInternalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlCotInternalPort.setStatus("current")
_SleV2EthernetServiceControlCotInternalVid_Type = OctetString
_SleV2EthernetServiceControlCotInternalVid_Object = MibScalar
sleV2EthernetServiceControlCotInternalVid = _SleV2EthernetServiceControlCotInternalVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 3, 20),
    _SleV2EthernetServiceControlCotInternalVid_Type()
)
sleV2EthernetServiceControlCotInternalVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EthernetServiceControlCotInternalVid.setStatus("current")
_SleV2EthernetServiceNotification_ObjectIdentity = ObjectIdentity
sleV2EthernetServiceNotification = _SleV2EthernetServiceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4)
)
_SleV2Security6_ObjectIdentity = ObjectIdentity
sleV2Security6 = _SleV2Security6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 3)
)

# Managed Objects groups

sleV2SecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 4)
)
sleV2SecurityGroup.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLFlowIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowSrcIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowSrcIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowDstIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowDstIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowProtocolType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTcpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowClassIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowClassID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowClassName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowPolicyIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowPolicyID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowPolicyName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowCnt"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassPolicyIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassPolicyID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassPolicyName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowCnt"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyClassCnt"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyPriority"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyMatchFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyNomatchFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlStatus"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimer"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlSrcIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlSrcIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlDstIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlDstIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlProtocolType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTcpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTcpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTcpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTcpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlUdpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlUdpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlUdpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlUdpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIcmpType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlHdrlen"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlStatus"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlTimer"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlStatus"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlTimer"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlClassIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlFlowIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlFlowID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlStatus"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlTimer"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlPriority"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlMatchFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlNomatchFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlStatus"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlTimer"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlPolicyIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlFlowID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlClassID"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLName"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLSrcIpaddr"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLSrcPrefixLength"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLDstIpAddr"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLDstPrefixLength"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLProtocolType"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLTcpflag"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLIcmpType"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLPriority"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLMatchAction"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLNomatchAction"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlStatus"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlTimer"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlName"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlSrcIpaddr"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlSrcPrefixLength"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlDstIpaddr"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlDstPrefixLength"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlProtocolType"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlTcpflag"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlIcmpType"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlPriority"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlMatchAction"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlNomatchAction"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowHdrlen"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLDstL4Port"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLSrcL4Port"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlSrcL4Port"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlDstL4Port"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLTotalPacket"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLSrcHistoryIpAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlStatus"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlTimer"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlTimer"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlStatus"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlName"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLSrcHistoryIndex"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterIndex"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterName"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterCreationTime"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterElapsedtimeAfterClear"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterStage"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterPriority"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterAction"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterActionRateLimit"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterActionBurstSize"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterActionTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterActionPcp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterActionVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterActionTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchType"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchCos"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchPort"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchOffset"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchLength"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchData"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchMask"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchDesc"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlRequest"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlStatus"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlTimer"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlIndex"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlName"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlStage"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlPriority"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlAction"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionRateLimit"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionBurstSize"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionPcp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchType"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchCos"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchPort"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchOffset"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchLength"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchData"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchMask"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchDesc"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchIndex"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchVidmap"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchPcp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchVidmap"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchPcp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIpFlag"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationIndex"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationName"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationStage"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationPort"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationEtherType"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationIpProtocol"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationArpSip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationArpSipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationDip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationDipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationAction"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationActionVid"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationProiroty"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlIndex"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlName"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlStage"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlProiroty"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlPort"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlEtherType"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlIpProtocol"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlArpSip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlArpSipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlDip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlDipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlAction"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlActionVid"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationSip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationSipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlSip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlSipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationOuterVlan"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationInnerVlan"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlOuterVlan"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlInnerVlan"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceEnableStatus"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceEnableManagement"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceHealthCheckPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceHealthCheckVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceSid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceType"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceRtCustomerPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceRtCustomerVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceRtNetworkPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceRtNetworkVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceRtEnableManagement"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceCotExternalPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceCotExternalVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceCotInternalPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceCotInternalVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlStatus"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimer"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlEnableStatus"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlEnableManagement"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlHealthCheckPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlHealthCheckVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlSid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlType"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtCustomerPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtCustomerVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtNetworkPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtNetworkVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtEnableManagement"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotExternalPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotExternalVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotInternalPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotInternalVid"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowClassName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlClassName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlFlowID"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlClassID"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowInetAddrType"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowSrcInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowDstInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowSrcInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowDstInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowControlInetAddrType"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowControlSrcInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowControlDstInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowControlSrcInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowControlDstInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfindex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfPriority"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlStatus"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlTimer"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfConrolIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlPriority"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlSyslogMode"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsSyslogStatus"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlRequest"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlStatus"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlTimer"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SecurityGroup.setStatus("current")


# Notification objects

sleACLFlowCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 3, 1)
)
sleACLFlowCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowSrcIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowSrcIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowDstIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowDstIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowProtocolType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowHdrlen"))
)
if mibBuilder.loadTexts:
    sleACLFlowCreated.setStatus(
        "current"
    )

sleACLFlowChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 3, 2)
)
sleACLFlowChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowSrcIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowSrcIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowDstIpAddr"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowDstIpAddrMask"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowProtocolType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowHdrlen"))
)
if mibBuilder.loadTexts:
    sleACLFlowChanged.setStatus(
        "current"
    )

sleACLFlowDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 3, 3)
)
sleACLFlowDestroyed.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlIndex"))
)
if mibBuilder.loadTexts:
    sleACLFlowDestroyed.setStatus(
        "current"
    )

sleACLFlowAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 3, 4)
)
sleACLFlowAllDestroyed.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlReqResult"))
)
if mibBuilder.loadTexts:
    sleACLFlowAllDestroyed.setStatus(
        "current"
    )

sleACLFlowExCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 3, 5)
)
sleACLFlowExCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowName"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowInetAddrType"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowSrcInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowDstInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowSrcInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowDstInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowProtocolType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowHdrlen"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIpFlag"))
)
if mibBuilder.loadTexts:
    sleACLFlowExCreated.setStatus(
        "current"
    )

sleACLFlowExChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 2, 1, 3, 6)
)
sleACLFlowExChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIndex"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowInetAddrType"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowSrcInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowDstInetAddr"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowSrcInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLFlowDstInetAddrLen"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowProtocolType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowTcpFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpSrcEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstStartPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowUdpDstEndPort"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowHdrlen"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowIpFlag"))
)
if mibBuilder.loadTexts:
    sleACLFlowExChanged.setStatus(
        "current"
    )

sleACLClassCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 3, 1)
)
sleACLClassCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLFlowClassName"))
)
if mibBuilder.loadTexts:
    sleACLClassCreated.setStatus(
        "current"
    )

sleACLClassDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 3, 2)
)
sleACLClassDestroyed.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlIndex"))
)
if mibBuilder.loadTexts:
    sleACLClassDestroyed.setStatus(
        "current"
    )

sleACLClassAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 1, 3, 3)
)
sleACLClassAllDestroyed.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassControlReqResult"))
)
if mibBuilder.loadTexts:
    sleACLClassAllDestroyed.setStatus(
        "current"
    )

sleACLClassFlowAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 3, 1)
)
sleACLClassFlowAdded.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlClassName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlClassIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowID"))
)
if mibBuilder.loadTexts:
    sleACLClassFlowAdded.setStatus(
        "current"
    )

sleACLClassFlowDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 3, 2)
)
sleACLClassFlowDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlClassIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlFlowIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlClassName"))
)
if mibBuilder.loadTexts:
    sleACLClassFlowDeleted.setStatus(
        "current"
    )

sleACLClassFlowAllDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 3, 2, 3, 3)
)
sleACLClassFlowAllDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassFlowControlClassIndex"))
)
if mibBuilder.loadTexts:
    sleACLClassFlowAllDeleted.setStatus(
        "current"
    )

sleACLPolicyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 3, 1)
)
sleACLPolicyCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLClassPolicyName"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyPriority"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyMatchFlag"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyNomatchFlag"))
)
if mibBuilder.loadTexts:
    sleACLPolicyCreated.setStatus(
        "current"
    )

sleACLPolicyInfoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 3, 2)
)
sleACLPolicyInfoChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyPriority"))
)
if mibBuilder.loadTexts:
    sleACLPolicyInfoChanged.setStatus(
        "current"
    )

sleACLPolicyMatchActionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 3, 3)
)
sleACLPolicyMatchActionChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyMatchFlag"))
)
if mibBuilder.loadTexts:
    sleACLPolicyMatchActionChanged.setStatus(
        "current"
    )

sleACLPolicyNomatchActionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 3, 4)
)
sleACLPolicyNomatchActionChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyNomatchFlag"))
)
if mibBuilder.loadTexts:
    sleACLPolicyNomatchActionChanged.setStatus(
        "current"
    )

sleACLPolicyDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 1, 3, 5)
)
sleACLPolicyDestroyed.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyControlIndex"))
)
if mibBuilder.loadTexts:
    sleACLPolicyDestroyed.setStatus(
        "current"
    )

sleACLPolicyFlowAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 3, 1)
)
sleACLPolicyFlowAdded.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassType"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassID"))
)
if mibBuilder.loadTexts:
    sleACLPolicyFlowAdded.setStatus(
        "current"
    )

sleACLPolicyFlowDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 3, 2)
)
sleACLPolicyFlowDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlPolicyIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlIndex"))
)
if mibBuilder.loadTexts:
    sleACLPolicyFlowDeleted.setStatus(
        "current"
    )

sleACLPolicyAllFlowDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 3, 3)
)
sleACLPolicyAllFlowDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlPolicyIndex"))
)
if mibBuilder.loadTexts:
    sleACLPolicyAllFlowDeleted.setStatus(
        "current"
    )

sleACLPolicyAllClassDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 3, 4)
)
sleACLPolicyAllClassDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlPolicyIndex"))
)
if mibBuilder.loadTexts:
    sleACLPolicyAllClassDeleted.setStatus(
        "current"
    )

sleACLPolicyAllFlowClassDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 4, 2, 3, 5)
)
sleACLPolicyAllFlowClassDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLPolicyFlowClassControlPolicyIndex"))
)
if mibBuilder.loadTexts:
    sleACLPolicyAllFlowClassDeleted.setStatus(
        "current"
    )

sleV2Security4ACLGroupIfProfileAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 3, 1)
)
sleV2Security4ACLGroupIfProfileAdd.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlName"))
)
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfProfileAdd.setStatus(
        "current"
    )

sleV2Security4ACLGroupIfProfileDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 5, 5, 1, 3, 2)
)
sleV2Security4ACLGroupIfProfileDelete.setObjects(
      *(("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlRequest"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfConrolIndex"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfControlType"))
)
if mibBuilder.loadTexts:
    sleV2Security4ACLGroupIfProfileDelete.setStatus(
        "current"
    )

sleSACLCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 3, 1)
)
sleSACLCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2SecuritySACLControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLSrcIpaddr"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLSrcPrefixLength"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLDstIpAddr"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLDstPrefixLength"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLProtocolType"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLTcpflag"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLIcmpType"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLIcmpCode"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLPriority"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLMatchAction"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLNomatchAction"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLSrcL4Port"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLDstL4Port"))
)
if mibBuilder.loadTexts:
    sleSACLCreated.setStatus(
        "current"
    )

sleSACLDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 3, 2)
)
sleSACLDestroyed.setObjects(
      *(("SLEV2-Security-MIB", "sleV2SecuritySACLControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlName"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSACLDestroyed.setStatus(
        "current"
    )

sleSACLAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 6, 3, 3)
)
sleSACLAllDestroyed.setObjects(
      *(("SLEV2-Security-MIB", "sleV2SecuritySACLControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecuritySACLControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSACLAllDestroyed.setStatus(
        "current"
    )

sleV2SecurityACLStatisticsSyslogModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 1, 3, 1)
)
sleV2SecurityACLStatisticsSyslogModeChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsBaseControlSyslogMode"))
)
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsSyslogModeChanged.setStatus(
        "current"
    )

sleV2SecurityACLStatisticsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 7, 2, 4, 1)
)
sleV2SecurityACLStatisticsCleared.setObjects(
      *(("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlRequest"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsControlName"))
)
if mibBuilder.loadTexts:
    sleV2SecurityACLStatisticsCleared.setStatus(
        "current"
    )

sleV2CpuPacketFilterAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 4, 1)
)
sleV2CpuPacketFilterAdded.setObjects(
      *(("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlRequest"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlName"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlStage"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlPriority"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlAction"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionRateLimit"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionBurstSize"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionPcp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchType"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchCos"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchPort"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchOffset"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchLength"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchData"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchMask"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlStatus"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlTimer"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchVidmap"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchPcp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchDesc"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterAdded.setStatus(
        "current"
    )

sleV2CpuPacketFilterDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 4, 2)
)
sleV2CpuPacketFilterDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlRequest"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterDeleted.setStatus(
        "current"
    )

sleV2CpuPacketFilterActionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 4, 3)
)
sleV2CpuPacketFilterActionChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlRequest"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlIndex"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlAction"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionRateLimit"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionBurstSize"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionPcp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlActionTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchType"))
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterActionChanged.setStatus(
        "current"
    )

sleV2CpuPacketFilterMatchChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 8, 4, 4)
)
sleV2CpuPacketFilterMatchChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlRequest"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlIndex"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchType"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchCos"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchPort"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchVidmap"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchTagPosition"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchTpid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchPcp"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchVid"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchOffset"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchLength"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchData"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchMask"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterControlMatchDesc"))
)
if mibBuilder.loadTexts:
    sleV2CpuPacketFilterMatchChanged.setStatus(
        "current"
    )

sleV2VlanOperationCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 3, 1)
)
sleV2VlanOperationCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2VlanOperationControlRequest"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlName"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlStage"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlProiroty"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlPort"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlOuterVlan"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlInnerVlan"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlEtherType"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlIpProtocol"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlArpSip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlArpSipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlSip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlSipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlDip"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlDipPfxLen"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlAction"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlActionVid"))
)
if mibBuilder.loadTexts:
    sleV2VlanOperationCreated.setStatus(
        "current"
    )

sleV2VlanOperationDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 9, 3, 2)
)
sleV2VlanOperationDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2VlanOperationControlRequest"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationControlName"))
)
if mibBuilder.loadTexts:
    sleV2VlanOperationDeleted.setStatus(
        "current"
    )

sleV2EthernetServiceEnableStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4, 1)
)
sleV2EthernetServiceEnableStatusChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlEnableStatus"))
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceEnableStatusChanged.setStatus(
        "current"
    )

sleV2EthernetServiceEnableManagementChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4, 2)
)
sleV2EthernetServiceEnableManagementChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlEnableManagement"))
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceEnableManagementChanged.setStatus(
        "current"
    )

sleV2EthernetServiceHealthCheckChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4, 3)
)
sleV2EthernetServiceHealthCheckChanged.setObjects(
      *(("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlHealthCheckPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlHealthCheckVid"))
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceHealthCheckChanged.setStatus(
        "current"
    )

sleV2EthernetServiceHealthCheckDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4, 4)
)
sleV2EthernetServiceHealthCheckDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceHealthCheckDeleted.setStatus(
        "current"
    )

sleV2EthernetServiceSidForRtModeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4, 5)
)
sleV2EthernetServiceSidForRtModeCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlSid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlType"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtCustomerPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtCustomerVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtNetworkPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtNetworkVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlRtEnableManagement"))
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceSidForRtModeCreated.setStatus(
        "current"
    )

sleV2EthernetServiceSidForCotModeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4, 6)
)
sleV2EthernetServiceSidForCotModeCreated.setObjects(
      *(("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlSid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlType"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotExternalPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotExternalVid"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotInternalPort"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlCotInternalVid"))
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceSidForCotModeCreated.setStatus(
        "current"
    )

sleV2EthernetServiceSidDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 2, 10, 4, 7)
)
sleV2EthernetServiceSidDeleted.setObjects(
      *(("SLEV2-Security-MIB", "sleV2EthernetServiceControlRequest"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlTimeStamp"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlReqResult"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceControlSid"))
)
if mibBuilder.loadTexts:
    sleV2EthernetServiceSidDeleted.setStatus(
        "current"
    )


# Notifications groups

sleV2SecurityNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 7, 5)
)
sleV2SecurityNotificationGroup.setObjects(
      *(("SLEV2-Security-MIB", "sleACLFlowCreated"),
        ("SLEV2-Security-MIB", "sleACLFlowChanged"),
        ("SLEV2-Security-MIB", "sleACLFlowDestroyed"),
        ("SLEV2-Security-MIB", "sleACLFlowAllDestroyed"),
        ("SLEV2-Security-MIB", "sleACLClassCreated"),
        ("SLEV2-Security-MIB", "sleACLClassDestroyed"),
        ("SLEV2-Security-MIB", "sleACLClassAllDestroyed"),
        ("SLEV2-Security-MIB", "sleACLClassFlowAdded"),
        ("SLEV2-Security-MIB", "sleACLClassFlowDeleted"),
        ("SLEV2-Security-MIB", "sleACLClassFlowAllDeleted"),
        ("SLEV2-Security-MIB", "sleACLPolicyCreated"),
        ("SLEV2-Security-MIB", "sleACLPolicyInfoChanged"),
        ("SLEV2-Security-MIB", "sleACLPolicyMatchActionChanged"),
        ("SLEV2-Security-MIB", "sleACLPolicyNomatchActionChanged"),
        ("SLEV2-Security-MIB", "sleACLPolicyDestroyed"),
        ("SLEV2-Security-MIB", "sleACLPolicyFlowAdded"),
        ("SLEV2-Security-MIB", "sleACLPolicyFlowDeleted"),
        ("SLEV2-Security-MIB", "sleACLPolicyAllFlowDeleted"),
        ("SLEV2-Security-MIB", "sleACLPolicyAllClassDeleted"),
        ("SLEV2-Security-MIB", "sleACLPolicyAllFlowClassDeleted"),
        ("SLEV2-Security-MIB", "sleSACLCreated"),
        ("SLEV2-Security-MIB", "sleSACLDestroyed"),
        ("SLEV2-Security-MIB", "sleSACLAllDestroyed"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsSyslogModeChanged"),
        ("SLEV2-Security-MIB", "sleV2SecurityACLStatisticsCleared"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterAdded"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterDeleted"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterActionChanged"),
        ("SLEV2-Security-MIB", "sleV2CpuPacketFilterMatchChanged"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationCreated"),
        ("SLEV2-Security-MIB", "sleV2VlanOperationDeleted"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceEnableStatusChanged"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceEnableManagementChanged"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceHealthCheckChanged"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceHealthCheckDeleted"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceSidForRtModeCreated"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceSidForCotModeCreated"),
        ("SLEV2-Security-MIB", "sleV2EthernetServiceSidDeleted"),
        ("SLEV2-Security-MIB", "sleACLFlowExCreated"),
        ("SLEV2-Security-MIB", "sleACLFlowExChanged"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfProfileAdd"),
        ("SLEV2-Security-MIB", "sleV2Security4ACLGroupIfProfileDelete"))
)
if mibBuilder.loadTexts:
    sleV2SecurityNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLEV2-Security-MIB",
    **{"IntFlowIndex": IntFlowIndex,
       "IntClassIndex": IntClassIndex,
       "IntPolicyIndex": IntPolicyIndex,
       "OctetName": OctetName,
       "IntIpAddrMask": IntIpAddrMask,
       "IntProtocolType": IntProtocolType,
       "IntL4Port": IntL4Port,
       "IntIcmpType": IntIcmpType,
       "IntIcmpCode": IntIcmpCode,
       "IntInternetProtocolFlag": IntInternetProtocolFlag,
       "IntRulePriority": IntRulePriority,
       "IntFlowClass": IntFlowClass,
       "IntInterfaceIndex": IntInterfaceIndex,
       "IntFlowOrClass": IntFlowOrClass,
       "IntPermit": IntPermit,
       "MacAddressMask": MacAddressMask,
       "sleV2Security": sleV2Security,
       "sleV2SecurityBase": sleV2SecurityBase,
       "sleVSecurity4": sleVSecurity4,
       "sleV2SecurityACL": sleV2SecurityACL,
       "sleV2Security4ACLBase": sleV2Security4ACLBase,
       "sleV2Security4ACLFlow": sleV2Security4ACLFlow,
       "sleV2Security4ACLFlowInfo": sleV2Security4ACLFlowInfo,
       "sleV2Security4ACLFlowTable": sleV2Security4ACLFlowTable,
       "sleV2Security4ACLFlowEntry": sleV2Security4ACLFlowEntry,
       "sleV2Security4ACLFlowIndex": sleV2Security4ACLFlowIndex,
       "sleV2Security4ACLFlowName": sleV2Security4ACLFlowName,
       "sleV2Security4ACLFlowSrcIpAddr": sleV2Security4ACLFlowSrcIpAddr,
       "sleV2Security4ACLFlowSrcIpAddrMask": sleV2Security4ACLFlowSrcIpAddrMask,
       "sleV2Security4ACLFlowDstIpAddr": sleV2Security4ACLFlowDstIpAddr,
       "sleV2Security4ACLFlowDstIpAddrMask": sleV2Security4ACLFlowDstIpAddrMask,
       "sleV2Security4ACLFlowProtocolType": sleV2Security4ACLFlowProtocolType,
       "sleV2Security4ACLFlowTcpSrcStartPort": sleV2Security4ACLFlowTcpSrcStartPort,
       "sleV2Security4ACLFlowTcpSrcEndPort": sleV2Security4ACLFlowTcpSrcEndPort,
       "sleV2Security4ACLFlowTcpDstStartPort": sleV2Security4ACLFlowTcpDstStartPort,
       "sleV2Security4ACLFlowTcpDstEndPort": sleV2Security4ACLFlowTcpDstEndPort,
       "sleV2Security4ACLFlowTcpFlag": sleV2Security4ACLFlowTcpFlag,
       "sleV2Security4ACLFlowUdpSrcStartPort": sleV2Security4ACLFlowUdpSrcStartPort,
       "sleV2Security4ACLFlowUdpSrcEndPort": sleV2Security4ACLFlowUdpSrcEndPort,
       "sleV2Security4ACLFlowUdpDstStartPort": sleV2Security4ACLFlowUdpDstStartPort,
       "sleV2Security4ACLFlowUdpDstEndPort": sleV2Security4ACLFlowUdpDstEndPort,
       "sleV2Security4ACLFlowIcmpType": sleV2Security4ACLFlowIcmpType,
       "sleV2Security4ACLFlowIcmpCode": sleV2Security4ACLFlowIcmpCode,
       "sleV2Security4ACLFlowHdrlen": sleV2Security4ACLFlowHdrlen,
       "sleV2Security4ACLFlowIpFlag": sleV2Security4ACLFlowIpFlag,
       "sleV2SecurityACLFlowInetAddrType": sleV2SecurityACLFlowInetAddrType,
       "sleV2SecurityACLFlowSrcInetAddr": sleV2SecurityACLFlowSrcInetAddr,
       "sleV2SecurityACLFlowDstInetAddr": sleV2SecurityACLFlowDstInetAddr,
       "sleV2SecurityACLFlowSrcInetAddrLen": sleV2SecurityACLFlowSrcInetAddrLen,
       "sleV2SecurityACLFlowDstInetAddrLen": sleV2SecurityACLFlowDstInetAddrLen,
       "sleV2Security4ACLFlowControl": sleV2Security4ACLFlowControl,
       "sleV2Security4ACLFlowControlRequest": sleV2Security4ACLFlowControlRequest,
       "sleV2Security4ACLFlowControlStatus": sleV2Security4ACLFlowControlStatus,
       "sleV2Security4ACLFlowControlTimer": sleV2Security4ACLFlowControlTimer,
       "sleV2Security4ACLFlowControlTimeStamp": sleV2Security4ACLFlowControlTimeStamp,
       "sleV2Security4ACLFlowControlReqResult": sleV2Security4ACLFlowControlReqResult,
       "sleV2Security4ACLFlowControlIndex": sleV2Security4ACLFlowControlIndex,
       "sleV2Security4ACLFlowControlName": sleV2Security4ACLFlowControlName,
       "sleV2Security4ACLFlowControlSrcIpAddr": sleV2Security4ACLFlowControlSrcIpAddr,
       "sleV2Security4ACLFlowControlSrcIpAddrMask": sleV2Security4ACLFlowControlSrcIpAddrMask,
       "sleV2Security4ACLFlowControlDstIpAddr": sleV2Security4ACLFlowControlDstIpAddr,
       "sleV2Security4ACLFlowControlDstIpAddrMask": sleV2Security4ACLFlowControlDstIpAddrMask,
       "sleV2Security4ACLFlowControlProtocolType": sleV2Security4ACLFlowControlProtocolType,
       "sleV2Security4ACLFlowControlTcpSrcStartPort": sleV2Security4ACLFlowControlTcpSrcStartPort,
       "sleV2Security4ACLFlowControlTcpSrcEndPort": sleV2Security4ACLFlowControlTcpSrcEndPort,
       "sleV2Security4ACLFlowControlTcpDstStartPort": sleV2Security4ACLFlowControlTcpDstStartPort,
       "sleV2Security4ACLFlowControlTcpDstEndPort": sleV2Security4ACLFlowControlTcpDstEndPort,
       "sleV2Security4ACLFlowControlTcpFlag": sleV2Security4ACLFlowControlTcpFlag,
       "sleV2Security4ACLFlowControlUdpSrcStartPort": sleV2Security4ACLFlowControlUdpSrcStartPort,
       "sleV2Security4ACLFlowControlUdpSrcEndPort": sleV2Security4ACLFlowControlUdpSrcEndPort,
       "sleV2Security4ACLFlowControlUdpDstStartPort": sleV2Security4ACLFlowControlUdpDstStartPort,
       "sleV2Security4ACLFlowControlUdpDstEndPort": sleV2Security4ACLFlowControlUdpDstEndPort,
       "sleV2Security4ACLFlowControlIcmpType": sleV2Security4ACLFlowControlIcmpType,
       "sleV2Security4ACLFlowControlIcmpCode": sleV2Security4ACLFlowControlIcmpCode,
       "sleV2Security4ACLFlowControlHdrlen": sleV2Security4ACLFlowControlHdrlen,
       "sleV2Security4ACLFlowControlIpFlag": sleV2Security4ACLFlowControlIpFlag,
       "sleV2SecurityACLFlowControlInetAddrType": sleV2SecurityACLFlowControlInetAddrType,
       "sleV2SecurityACLFlowControlSrcInetAddr": sleV2SecurityACLFlowControlSrcInetAddr,
       "sleV2SecurityACLFlowControlDstInetAddr": sleV2SecurityACLFlowControlDstInetAddr,
       "sleV2SecurityACLFlowControlSrcInetAddrLen": sleV2SecurityACLFlowControlSrcInetAddrLen,
       "sleV2SecurityACLFlowControlDstInetAddrLen": sleV2SecurityACLFlowControlDstInetAddrLen,
       "sleV2Security4ACLFlowNotification": sleV2Security4ACLFlowNotification,
       "sleACLFlowCreated": sleACLFlowCreated,
       "sleACLFlowChanged": sleACLFlowChanged,
       "sleACLFlowDestroyed": sleACLFlowDestroyed,
       "sleACLFlowAllDestroyed": sleACLFlowAllDestroyed,
       "sleACLFlowExCreated": sleACLFlowExCreated,
       "sleACLFlowExChanged": sleACLFlowExChanged,
       "sleV2Security4ACLFlowClass": sleV2Security4ACLFlowClass,
       "sleV2Security4ACLFlowClassTable": sleV2Security4ACLFlowClassTable,
       "sleV2Security4ACLFlowClassEntry": sleV2Security4ACLFlowClassEntry,
       "sleV2Security4ACLFlowClassIndex": sleV2Security4ACLFlowClassIndex,
       "sleV2Security4ACLFlowClassID": sleV2Security4ACLFlowClassID,
       "sleV2Security4ACLFlowClassName": sleV2Security4ACLFlowClassName,
       "sleV2Security4ACLFlowPolicy": sleV2Security4ACLFlowPolicy,
       "sleV2QoS4ACLFlowPolicyTable": sleV2QoS4ACLFlowPolicyTable,
       "sleV2QoS4ACLFlowPolicyEntry": sleV2QoS4ACLFlowPolicyEntry,
       "sleV2Security4ACLFlowPolicyIndex": sleV2Security4ACLFlowPolicyIndex,
       "sleV2Security4ACLFlowPolicyID": sleV2Security4ACLFlowPolicyID,
       "sleV2Security4ACLFlowPolicyName": sleV2Security4ACLFlowPolicyName,
       "sleV2Security4ACLClass": sleV2Security4ACLClass,
       "sleV2Security4ACLClassInfo": sleV2Security4ACLClassInfo,
       "sleV2Security4ACLClassTable": sleV2Security4ACLClassTable,
       "sleV2Security4ACLClassEntry": sleV2Security4ACLClassEntry,
       "sleV2Security4ACLClassIndex": sleV2Security4ACLClassIndex,
       "sleV2Security4ACLClassName": sleV2Security4ACLClassName,
       "sleV2Security4ACLClassFlowCnt": sleV2Security4ACLClassFlowCnt,
       "sleV2Security4ACLClassControl": sleV2Security4ACLClassControl,
       "sleV2Security4ACLClassControlRequest": sleV2Security4ACLClassControlRequest,
       "sleV2Security4ACLClassControlStatus": sleV2Security4ACLClassControlStatus,
       "sleV2Security4ACLClassControlTimer": sleV2Security4ACLClassControlTimer,
       "sleV2Security4ACLClassControlTimeStamp": sleV2Security4ACLClassControlTimeStamp,
       "sleV2Security4ACLClassControlReqResult": sleV2Security4ACLClassControlReqResult,
       "sleV2Security4ACLClassControlIndex": sleV2Security4ACLClassControlIndex,
       "sleV2Security4ACLClassControlName": sleV2Security4ACLClassControlName,
       "sleV2Security4ACLClassNotification": sleV2Security4ACLClassNotification,
       "sleACLClassCreated": sleACLClassCreated,
       "sleACLClassDestroyed": sleACLClassDestroyed,
       "sleACLClassAllDestroyed": sleACLClassAllDestroyed,
       "sleV2Security4ACLClassFlow": sleV2Security4ACLClassFlow,
       "sleV2Security4ACLClassFlowTable": sleV2Security4ACLClassFlowTable,
       "sleV2Security4ACLClassFlowEntry": sleV2Security4ACLClassFlowEntry,
       "sleV2Security4ACLClassFlowIndex": sleV2Security4ACLClassFlowIndex,
       "sleV2Security4ACLClassFlowID": sleV2Security4ACLClassFlowID,
       "sleV2Security4ACLClassFlowName": sleV2Security4ACLClassFlowName,
       "sleV2Security4ACLClassFlowClassName": sleV2Security4ACLClassFlowClassName,
       "sleV2Security4ACLClassFlowControl": sleV2Security4ACLClassFlowControl,
       "sleV2Security4ACLClassFlowControlRequest": sleV2Security4ACLClassFlowControlRequest,
       "sleV2Security4ACLClassFlowControlStatus": sleV2Security4ACLClassFlowControlStatus,
       "sleV2Security4ACLClassFlowControlTimer": sleV2Security4ACLClassFlowControlTimer,
       "sleV2Security4ACLClassFlowControlTimeStamp": sleV2Security4ACLClassFlowControlTimeStamp,
       "sleV2Security4ACLClassFlowControlReqResult": sleV2Security4ACLClassFlowControlReqResult,
       "sleV2Security4ACLClassFlowControlClassIndex": sleV2Security4ACLClassFlowControlClassIndex,
       "sleV2Security4ACLClassFlowControlFlowIndex": sleV2Security4ACLClassFlowControlFlowIndex,
       "sleV2Security4ACLClassFlowControlFlowID": sleV2Security4ACLClassFlowControlFlowID,
       "sleV2Security4ACLClassFlowControlClassName": sleV2Security4ACLClassFlowControlClassName,
       "sleV2Security4ACLClassFlowNotification": sleV2Security4ACLClassFlowNotification,
       "sleACLClassFlowAdded": sleACLClassFlowAdded,
       "sleACLClassFlowDeleted": sleACLClassFlowDeleted,
       "sleACLClassFlowAllDeleted": sleACLClassFlowAllDeleted,
       "sleV2Security4ACLClassPolicy": sleV2Security4ACLClassPolicy,
       "sleV2Security4ACLClassPolicyTable": sleV2Security4ACLClassPolicyTable,
       "sleV2Security4ACLClassPolicyEntry": sleV2Security4ACLClassPolicyEntry,
       "sleV2Security4ACLClassPolicyIndex": sleV2Security4ACLClassPolicyIndex,
       "sleV2Security4ACLClassPolicyID": sleV2Security4ACLClassPolicyID,
       "sleV2Security4ACLClassPolicyName": sleV2Security4ACLClassPolicyName,
       "sleV2Security4ACLPolicy": sleV2Security4ACLPolicy,
       "sleV2Security4ACLPolicyInfo": sleV2Security4ACLPolicyInfo,
       "sleV2Security4ACLPolicyTable": sleV2Security4ACLPolicyTable,
       "sleV2Security4ACLPolicyEntry": sleV2Security4ACLPolicyEntry,
       "sleV2Security4ACLPolicyIndex": sleV2Security4ACLPolicyIndex,
       "sleV2Security4ACLPolicyName": sleV2Security4ACLPolicyName,
       "sleV2Security4ACLPolicyFlowCnt": sleV2Security4ACLPolicyFlowCnt,
       "sleV2Security4ACLPolicyClassCnt": sleV2Security4ACLPolicyClassCnt,
       "sleV2Security4ACLPolicyPriority": sleV2Security4ACLPolicyPriority,
       "sleV2Security4ACLPolicyMatchFlag": sleV2Security4ACLPolicyMatchFlag,
       "sleV2Security4ACLPolicyNomatchFlag": sleV2Security4ACLPolicyNomatchFlag,
       "sleV2Security4ACLPolicyControl": sleV2Security4ACLPolicyControl,
       "sleV2Security4ACLPolicyControlRequest": sleV2Security4ACLPolicyControlRequest,
       "sleV2Security4ACLPolicyControlStatus": sleV2Security4ACLPolicyControlStatus,
       "sleV2Security4ACLPolicyControlTimer": sleV2Security4ACLPolicyControlTimer,
       "sleV2Security4ACLPolicyControlTimeStamp": sleV2Security4ACLPolicyControlTimeStamp,
       "sleV2Security4ACLPolicyControlReqResult": sleV2Security4ACLPolicyControlReqResult,
       "sleV2Security4ACLPolicyControlIndex": sleV2Security4ACLPolicyControlIndex,
       "sleV2Security4ACLPolicyControlName": sleV2Security4ACLPolicyControlName,
       "sleV2Security4ACLPolicyControlPriority": sleV2Security4ACLPolicyControlPriority,
       "sleV2Security4ACLPolicyControlMatchFlag": sleV2Security4ACLPolicyControlMatchFlag,
       "sleV2Security4ACLPolicyControlNomatchFlag": sleV2Security4ACLPolicyControlNomatchFlag,
       "sleV2Security4ACLPolicyControlFlowID": sleV2Security4ACLPolicyControlFlowID,
       "sleV2Security4ACLPolicyControlClassID": sleV2Security4ACLPolicyControlClassID,
       "sleV2Security4ACLPolicyNotification": sleV2Security4ACLPolicyNotification,
       "sleACLPolicyCreated": sleACLPolicyCreated,
       "sleACLPolicyInfoChanged": sleACLPolicyInfoChanged,
       "sleACLPolicyMatchActionChanged": sleACLPolicyMatchActionChanged,
       "sleACLPolicyNomatchActionChanged": sleACLPolicyNomatchActionChanged,
       "sleACLPolicyDestroyed": sleACLPolicyDestroyed,
       "sleV2Security4ACLPolicyFlowClass": sleV2Security4ACLPolicyFlowClass,
       "sleV2Security4ACLPolicyFlowClassTable": sleV2Security4ACLPolicyFlowClassTable,
       "sleV2Security4ACLPolicyFlowClassEntry": sleV2Security4ACLPolicyFlowClassEntry,
       "sleV2Security4ACLPolicyFlowClassIndex": sleV2Security4ACLPolicyFlowClassIndex,
       "sleV2Security4ACLPolicyFlowClassType": sleV2Security4ACLPolicyFlowClassType,
       "sleV2Security4ACLPolicyFlowClassID": sleV2Security4ACLPolicyFlowClassID,
       "sleV2Security4ACLPolicyFlowClassName": sleV2Security4ACLPolicyFlowClassName,
       "sleV2Security4ACLPolicyFlowClassControl": sleV2Security4ACLPolicyFlowClassControl,
       "sleV2Security4ACLPolicyFlowClassControlRequest": sleV2Security4ACLPolicyFlowClassControlRequest,
       "sleV2Security4ACLPolicyFlowClassControlStatus": sleV2Security4ACLPolicyFlowClassControlStatus,
       "sleV2Security4ACLPolicyFlowClassControlTimer": sleV2Security4ACLPolicyFlowClassControlTimer,
       "sleV2Security4ACLPolicyFlowClassControlTimeStamp": sleV2Security4ACLPolicyFlowClassControlTimeStamp,
       "sleV2Security4ACLPolicyFlowClassControlReqResult": sleV2Security4ACLPolicyFlowClassControlReqResult,
       "sleV2Security4ACLPolicyFlowClassControlPolicyIndex": sleV2Security4ACLPolicyFlowClassControlPolicyIndex,
       "sleV2Security4ACLPolicyFlowClassControlIndex": sleV2Security4ACLPolicyFlowClassControlIndex,
       "sleV2Security4ACLPolicyFlowClassControlType": sleV2Security4ACLPolicyFlowClassControlType,
       "sleV2Security4ACLPolicyFlowClassControlFlowID": sleV2Security4ACLPolicyFlowClassControlFlowID,
       "sleV2Security4ACLPolicyFlowClassControlClassID": sleV2Security4ACLPolicyFlowClassControlClassID,
       "sleV2Security4ACLPolicyFlowClassNotification": sleV2Security4ACLPolicyFlowClassNotification,
       "sleACLPolicyFlowAdded": sleACLPolicyFlowAdded,
       "sleACLPolicyFlowDeleted": sleACLPolicyFlowDeleted,
       "sleACLPolicyAllFlowDeleted": sleACLPolicyAllFlowDeleted,
       "sleACLPolicyAllClassDeleted": sleACLPolicyAllClassDeleted,
       "sleACLPolicyAllFlowClassDeleted": sleACLPolicyAllFlowClassDeleted,
       "sleV2Security4ACLGroup": sleV2Security4ACLGroup,
       "sleV2Security4ACLGroupIf": sleV2Security4ACLGroupIf,
       "sleV2Security4ACLGroupIfTable": sleV2Security4ACLGroupIfTable,
       "sleV2Security4ACLGroupIfEntry": sleV2Security4ACLGroupIfEntry,
       "sleV2Security4ACLGroupIfindex": sleV2Security4ACLGroupIfindex,
       "sleV2Security4ACLGroupIfType": sleV2Security4ACLGroupIfType,
       "sleV2Security4ACLGroupIfName": sleV2Security4ACLGroupIfName,
       "sleV2Security4ACLGroupIfPriority": sleV2Security4ACLGroupIfPriority,
       "sleV2Security4ACLGroupIfControl": sleV2Security4ACLGroupIfControl,
       "sleV2Security4ACLGroupIfControlRequest": sleV2Security4ACLGroupIfControlRequest,
       "sleV2Security4ACLGroupIfControlStatus": sleV2Security4ACLGroupIfControlStatus,
       "sleV2Security4ACLGroupIfControlTimer": sleV2Security4ACLGroupIfControlTimer,
       "sleV2Security4ACLGroupIfControlReqResult": sleV2Security4ACLGroupIfControlReqResult,
       "sleV2Security4ACLGroupIfControlTimeStamp": sleV2Security4ACLGroupIfControlTimeStamp,
       "sleV2Security4ACLGroupIfConrolIndex": sleV2Security4ACLGroupIfConrolIndex,
       "sleV2Security4ACLGroupIfControlType": sleV2Security4ACLGroupIfControlType,
       "sleV2Security4ACLGroupIfControlName": sleV2Security4ACLGroupIfControlName,
       "sleV2Security4ACLGroupIfControlPriority": sleV2Security4ACLGroupIfControlPriority,
       "sleV2SecurityACLGroupIfNotification": sleV2SecurityACLGroupIfNotification,
       "sleV2Security4ACLGroupIfProfileAdd": sleV2Security4ACLGroupIfProfileAdd,
       "sleV2Security4ACLGroupIfProfileDelete": sleV2Security4ACLGroupIfProfileDelete,
       "sleV2SecuritySACL": sleV2SecuritySACL,
       "sleV2SecuritySACLTable": sleV2SecuritySACLTable,
       "sleV2SecuritySACLEntry": sleV2SecuritySACLEntry,
       "sleV2SecuritySACLName": sleV2SecuritySACLName,
       "sleV2SecuritySACLSrcIpaddr": sleV2SecuritySACLSrcIpaddr,
       "sleV2SecuritySACLSrcPrefixLength": sleV2SecuritySACLSrcPrefixLength,
       "sleV2SecuritySACLDstIpAddr": sleV2SecuritySACLDstIpAddr,
       "sleV2SecuritySACLDstPrefixLength": sleV2SecuritySACLDstPrefixLength,
       "sleV2SecuritySACLProtocolType": sleV2SecuritySACLProtocolType,
       "sleV2SecuritySACLTcpflag": sleV2SecuritySACLTcpflag,
       "sleV2SecuritySACLSrcL4Port": sleV2SecuritySACLSrcL4Port,
       "sleV2SecuritySACLDstL4Port": sleV2SecuritySACLDstL4Port,
       "sleV2SecuritySACLIcmpType": sleV2SecuritySACLIcmpType,
       "sleV2SecuritySACLIcmpCode": sleV2SecuritySACLIcmpCode,
       "sleV2SecuritySACLPriority": sleV2SecuritySACLPriority,
       "sleV2SecuritySACLMatchAction": sleV2SecuritySACLMatchAction,
       "sleV2SecuritySACLNomatchAction": sleV2SecuritySACLNomatchAction,
       "sleV2SecuritySACLControl": sleV2SecuritySACLControl,
       "sleV2SecuritySACLControlRequest": sleV2SecuritySACLControlRequest,
       "sleV2SecuritySACLControlStatus": sleV2SecuritySACLControlStatus,
       "sleV2SecuritySACLControlTimer": sleV2SecuritySACLControlTimer,
       "sleV2SecuritySACLControlTimeStamp": sleV2SecuritySACLControlTimeStamp,
       "sleV2SecuritySACLControlReqResult": sleV2SecuritySACLControlReqResult,
       "sleV2SecuritySACLControlName": sleV2SecuritySACLControlName,
       "sleV2SecuritySACLControlSrcIpaddr": sleV2SecuritySACLControlSrcIpaddr,
       "sleV2SecuritySACLControlSrcPrefixLength": sleV2SecuritySACLControlSrcPrefixLength,
       "sleV2SecuritySACLControlDstIpaddr": sleV2SecuritySACLControlDstIpaddr,
       "sleV2SecuritySACLControlDstPrefixLength": sleV2SecuritySACLControlDstPrefixLength,
       "sleV2SecuritySACLControlProtocolType": sleV2SecuritySACLControlProtocolType,
       "sleV2SecuritySACLControlTcpflag": sleV2SecuritySACLControlTcpflag,
       "sleV2SecuritySACLControlSrcL4Port": sleV2SecuritySACLControlSrcL4Port,
       "sleV2SecuritySACLControlDstL4Port": sleV2SecuritySACLControlDstL4Port,
       "sleV2SecuritySACLControlIcmpType": sleV2SecuritySACLControlIcmpType,
       "sleV2SecuritySACLControlIcmpCode": sleV2SecuritySACLControlIcmpCode,
       "sleV2SecuritySACLControlPriority": sleV2SecuritySACLControlPriority,
       "sleV2SecuritySACLControlMatchAction": sleV2SecuritySACLControlMatchAction,
       "sleV2SecuritySACLControlNomatchAction": sleV2SecuritySACLControlNomatchAction,
       "sleV2SecuritySACLNotification": sleV2SecuritySACLNotification,
       "sleSACLCreated": sleSACLCreated,
       "sleSACLDestroyed": sleSACLDestroyed,
       "sleSACLAllDestroyed": sleSACLAllDestroyed,
       "sleV2SecurityACLStatistics": sleV2SecurityACLStatistics,
       "sleV2SecurityACLStatisticsBase": sleV2SecurityACLStatisticsBase,
       "sleV2SecurityACLStatisticsBaseInfo": sleV2SecurityACLStatisticsBaseInfo,
       "sleV2SecurityACLStatisticsSyslogStatus": sleV2SecurityACLStatisticsSyslogStatus,
       "sleV2SecurityACLStatisticsBaseControl": sleV2SecurityACLStatisticsBaseControl,
       "sleV2SecurityACLStatisticsBaseControlRequest": sleV2SecurityACLStatisticsBaseControlRequest,
       "sleV2SecurityACLStatisticsBaseControlStatus": sleV2SecurityACLStatisticsBaseControlStatus,
       "sleV2SecurityACLStatisticsBaseControlTimer": sleV2SecurityACLStatisticsBaseControlTimer,
       "sleV2SecurityACLStatisticsBaseControlTimeStamp": sleV2SecurityACLStatisticsBaseControlTimeStamp,
       "sleV2SecurityACLStatisticsBaseControlReqResult": sleV2SecurityACLStatisticsBaseControlReqResult,
       "sleV2SecurityACLStatisticsBaseControlSyslogMode": sleV2SecurityACLStatisticsBaseControlSyslogMode,
       "sleV2SecurityACLStatisticsBaseNotification": sleV2SecurityACLStatisticsBaseNotification,
       "sleV2SecurityACLStatisticsSyslogModeChanged": sleV2SecurityACLStatisticsSyslogModeChanged,
       "sleV2SecurityACLStatisticsPacketHistory": sleV2SecurityACLStatisticsPacketHistory,
       "sleV2SecurityACLPacketCountTable": sleV2SecurityACLPacketCountTable,
       "sleV2SecurityACLPacketCountEntry": sleV2SecurityACLPacketCountEntry,
       "sleV2SecurityACLTotalPacket": sleV2SecurityACLTotalPacket,
       "sleV2SecurityACLSrcHistoryTable": sleV2SecurityACLSrcHistoryTable,
       "sleV2SecurityACLSrcHistoryEntry": sleV2SecurityACLSrcHistoryEntry,
       "sleV2SecurityACLSrcHistoryIndex": sleV2SecurityACLSrcHistoryIndex,
       "sleV2SecurityACLSrcHistoryIpAddr": sleV2SecurityACLSrcHistoryIpAddr,
       "sleV2SecurityACLStatisticsControl": sleV2SecurityACLStatisticsControl,
       "sleV2SecurityACLStatisticsControlRequest": sleV2SecurityACLStatisticsControlRequest,
       "sleV2SecurityACLStatisticsControlStatus": sleV2SecurityACLStatisticsControlStatus,
       "sleV2SecurityACLStatisticsControlTimer": sleV2SecurityACLStatisticsControlTimer,
       "sleV2SecurityACLStatisticsControlTimeStamp": sleV2SecurityACLStatisticsControlTimeStamp,
       "sleV2SecurityACLStatisticsControlReqResult": sleV2SecurityACLStatisticsControlReqResult,
       "sleV2SecurityACLStatisticsControlName": sleV2SecurityACLStatisticsControlName,
       "sleV2SecurityACLStatisticsNotification": sleV2SecurityACLStatisticsNotification,
       "sleV2SecurityACLStatisticsCleared": sleV2SecurityACLStatisticsCleared,
       "sleV2CpuPacketFilter": sleV2CpuPacketFilter,
       "sleV2CpuPacketFilterTable": sleV2CpuPacketFilterTable,
       "sleV2CpuPacketFilterEntry": sleV2CpuPacketFilterEntry,
       "sleV2CpuPacketFilterIndex": sleV2CpuPacketFilterIndex,
       "sleV2CpuPacketFilterName": sleV2CpuPacketFilterName,
       "sleV2CpuPacketFilterCreationTime": sleV2CpuPacketFilterCreationTime,
       "sleV2CpuPacketFilterElapsedtimeAfterClear": sleV2CpuPacketFilterElapsedtimeAfterClear,
       "sleV2CpuPacketFilterStage": sleV2CpuPacketFilterStage,
       "sleV2CpuPacketFilterPriority": sleV2CpuPacketFilterPriority,
       "sleV2CpuPacketFilterAction": sleV2CpuPacketFilterAction,
       "sleV2CpuPacketFilterActionRateLimit": sleV2CpuPacketFilterActionRateLimit,
       "sleV2CpuPacketFilterActionBurstSize": sleV2CpuPacketFilterActionBurstSize,
       "sleV2CpuPacketFilterActionTpid": sleV2CpuPacketFilterActionTpid,
       "sleV2CpuPacketFilterActionPcp": sleV2CpuPacketFilterActionPcp,
       "sleV2CpuPacketFilterActionVid": sleV2CpuPacketFilterActionVid,
       "sleV2CpuPacketFilterActionTagPosition": sleV2CpuPacketFilterActionTagPosition,
       "sleV2CpuPacketFilterMatchTable": sleV2CpuPacketFilterMatchTable,
       "sleV2CpuPacketFilterMatchEntry": sleV2CpuPacketFilterMatchEntry,
       "sleV2CpuPacketFilterMatchIndex": sleV2CpuPacketFilterMatchIndex,
       "sleV2CpuPacketFilterMatchType": sleV2CpuPacketFilterMatchType,
       "sleV2CpuPacketFilterMatchCos": sleV2CpuPacketFilterMatchCos,
       "sleV2CpuPacketFilterMatchPort": sleV2CpuPacketFilterMatchPort,
       "sleV2CpuPacketFilterMatchVidmap": sleV2CpuPacketFilterMatchVidmap,
       "sleV2CpuPacketFilterMatchTagPosition": sleV2CpuPacketFilterMatchTagPosition,
       "sleV2CpuPacketFilterMatchTpid": sleV2CpuPacketFilterMatchTpid,
       "sleV2CpuPacketFilterMatchPcp": sleV2CpuPacketFilterMatchPcp,
       "sleV2CpuPacketFilterMatchVid": sleV2CpuPacketFilterMatchVid,
       "sleV2CpuPacketFilterMatchOffset": sleV2CpuPacketFilterMatchOffset,
       "sleV2CpuPacketFilterMatchLength": sleV2CpuPacketFilterMatchLength,
       "sleV2CpuPacketFilterMatchData": sleV2CpuPacketFilterMatchData,
       "sleV2CpuPacketFilterMatchMask": sleV2CpuPacketFilterMatchMask,
       "sleV2CpuPacketFilterMatchDesc": sleV2CpuPacketFilterMatchDesc,
       "sleV2CpuPacketFilterControl": sleV2CpuPacketFilterControl,
       "sleV2CpuPacketFilterControlRequest": sleV2CpuPacketFilterControlRequest,
       "sleV2CpuPacketFilterControlStatus": sleV2CpuPacketFilterControlStatus,
       "sleV2CpuPacketFilterControlTimer": sleV2CpuPacketFilterControlTimer,
       "sleV2CpuPacketFilterControlTimeStamp": sleV2CpuPacketFilterControlTimeStamp,
       "sleV2CpuPacketFilterControlReqResult": sleV2CpuPacketFilterControlReqResult,
       "sleV2CpuPacketFilterControlIndex": sleV2CpuPacketFilterControlIndex,
       "sleV2CpuPacketFilterControlName": sleV2CpuPacketFilterControlName,
       "sleV2CpuPacketFilterControlStage": sleV2CpuPacketFilterControlStage,
       "sleV2CpuPacketFilterControlPriority": sleV2CpuPacketFilterControlPriority,
       "sleV2CpuPacketFilterControlAction": sleV2CpuPacketFilterControlAction,
       "sleV2CpuPacketFilterControlActionRateLimit": sleV2CpuPacketFilterControlActionRateLimit,
       "sleV2CpuPacketFilterControlActionBurstSize": sleV2CpuPacketFilterControlActionBurstSize,
       "sleV2CpuPacketFilterControlActionTpid": sleV2CpuPacketFilterControlActionTpid,
       "sleV2CpuPacketFilterControlActionPcp": sleV2CpuPacketFilterControlActionPcp,
       "sleV2CpuPacketFilterControlActionVid": sleV2CpuPacketFilterControlActionVid,
       "sleV2CpuPacketFilterControlActionTagPosition": sleV2CpuPacketFilterControlActionTagPosition,
       "sleV2CpuPacketFilterControlMatchType": sleV2CpuPacketFilterControlMatchType,
       "sleV2CpuPacketFilterControlMatchCos": sleV2CpuPacketFilterControlMatchCos,
       "sleV2CpuPacketFilterControlMatchPort": sleV2CpuPacketFilterControlMatchPort,
       "sleV2CpuPacketFilterControlMatchVidmap": sleV2CpuPacketFilterControlMatchVidmap,
       "sleV2CpuPacketFilterControlMatchTagPosition": sleV2CpuPacketFilterControlMatchTagPosition,
       "sleV2CpuPacketFilterControlMatchTpid": sleV2CpuPacketFilterControlMatchTpid,
       "sleV2CpuPacketFilterControlMatchPcp": sleV2CpuPacketFilterControlMatchPcp,
       "sleV2CpuPacketFilterControlMatchVid": sleV2CpuPacketFilterControlMatchVid,
       "sleV2CpuPacketFilterControlMatchOffset": sleV2CpuPacketFilterControlMatchOffset,
       "sleV2CpuPacketFilterControlMatchLength": sleV2CpuPacketFilterControlMatchLength,
       "sleV2CpuPacketFilterControlMatchData": sleV2CpuPacketFilterControlMatchData,
       "sleV2CpuPacketFilterControlMatchMask": sleV2CpuPacketFilterControlMatchMask,
       "sleV2CpuPacketFilterControlMatchDesc": sleV2CpuPacketFilterControlMatchDesc,
       "sleV2CpuPacketFilterNotification": sleV2CpuPacketFilterNotification,
       "sleV2CpuPacketFilterAdded": sleV2CpuPacketFilterAdded,
       "sleV2CpuPacketFilterDeleted": sleV2CpuPacketFilterDeleted,
       "sleV2CpuPacketFilterActionChanged": sleV2CpuPacketFilterActionChanged,
       "sleV2CpuPacketFilterMatchChanged": sleV2CpuPacketFilterMatchChanged,
       "sleV2VlanOperation": sleV2VlanOperation,
       "sleV2VlanOperationTable": sleV2VlanOperationTable,
       "sleV2VlanOperationEntry": sleV2VlanOperationEntry,
       "sleV2VlanOperationIndex": sleV2VlanOperationIndex,
       "sleV2VlanOperationName": sleV2VlanOperationName,
       "sleV2VlanOperationStage": sleV2VlanOperationStage,
       "sleV2VlanOperationProiroty": sleV2VlanOperationProiroty,
       "sleV2VlanOperationPort": sleV2VlanOperationPort,
       "sleV2VlanOperationOuterVlan": sleV2VlanOperationOuterVlan,
       "sleV2VlanOperationInnerVlan": sleV2VlanOperationInnerVlan,
       "sleV2VlanOperationEtherType": sleV2VlanOperationEtherType,
       "sleV2VlanOperationIpProtocol": sleV2VlanOperationIpProtocol,
       "sleV2VlanOperationArpSip": sleV2VlanOperationArpSip,
       "sleV2VlanOperationArpSipPfxLen": sleV2VlanOperationArpSipPfxLen,
       "sleV2VlanOperationSip": sleV2VlanOperationSip,
       "sleV2VlanOperationSipPfxLen": sleV2VlanOperationSipPfxLen,
       "sleV2VlanOperationDip": sleV2VlanOperationDip,
       "sleV2VlanOperationDipPfxLen": sleV2VlanOperationDipPfxLen,
       "sleV2VlanOperationAction": sleV2VlanOperationAction,
       "sleV2VlanOperationActionVid": sleV2VlanOperationActionVid,
       "sleV2VlanOperationControl": sleV2VlanOperationControl,
       "sleV2VlanOperationControlRequest": sleV2VlanOperationControlRequest,
       "sleV2VlanOperationControlStatus": sleV2VlanOperationControlStatus,
       "sleV2VlanOperationControlTimer": sleV2VlanOperationControlTimer,
       "sleV2VlanOperationControlTimeStamp": sleV2VlanOperationControlTimeStamp,
       "sleV2VlanOperationControlReqResult": sleV2VlanOperationControlReqResult,
       "sleV2VlanOperationControlIndex": sleV2VlanOperationControlIndex,
       "sleV2VlanOperationControlName": sleV2VlanOperationControlName,
       "sleV2VlanOperationControlStage": sleV2VlanOperationControlStage,
       "sleV2VlanOperationControlProiroty": sleV2VlanOperationControlProiroty,
       "sleV2VlanOperationControlPort": sleV2VlanOperationControlPort,
       "sleV2VlanOperationControlOuterVlan": sleV2VlanOperationControlOuterVlan,
       "sleV2VlanOperationControlInnerVlan": sleV2VlanOperationControlInnerVlan,
       "sleV2VlanOperationControlEtherType": sleV2VlanOperationControlEtherType,
       "sleV2VlanOperationControlIpProtocol": sleV2VlanOperationControlIpProtocol,
       "sleV2VlanOperationControlArpSip": sleV2VlanOperationControlArpSip,
       "sleV2VlanOperationControlArpSipPfxLen": sleV2VlanOperationControlArpSipPfxLen,
       "sleV2VlanOperationControlSip": sleV2VlanOperationControlSip,
       "sleV2VlanOperationControlSipPfxLen": sleV2VlanOperationControlSipPfxLen,
       "sleV2VlanOperationControlDip": sleV2VlanOperationControlDip,
       "sleV2VlanOperationControlDipPfxLen": sleV2VlanOperationControlDipPfxLen,
       "sleV2VlanOperationControlAction": sleV2VlanOperationControlAction,
       "sleV2VlanOperationControlActionVid": sleV2VlanOperationControlActionVid,
       "sleV2VlanOperationNotification": sleV2VlanOperationNotification,
       "sleV2VlanOperationCreated": sleV2VlanOperationCreated,
       "sleV2VlanOperationDeleted": sleV2VlanOperationDeleted,
       "sleV2EthernetService": sleV2EthernetService,
       "sleV2EthernetServiceBase": sleV2EthernetServiceBase,
       "sleV2EthernetServiceEnableStatus": sleV2EthernetServiceEnableStatus,
       "sleV2EthernetServiceEnableManagement": sleV2EthernetServiceEnableManagement,
       "sleV2EthernetServiceHealthCheckPort": sleV2EthernetServiceHealthCheckPort,
       "sleV2EthernetServiceHealthCheckVid": sleV2EthernetServiceHealthCheckVid,
       "sleV2EthernetServiceTable": sleV2EthernetServiceTable,
       "sleV2EthernetServiceEntry": sleV2EthernetServiceEntry,
       "sleV2EthernetServiceSid": sleV2EthernetServiceSid,
       "sleV2EthernetServiceType": sleV2EthernetServiceType,
       "sleV2EthernetServiceRtCustomerPort": sleV2EthernetServiceRtCustomerPort,
       "sleV2EthernetServiceRtCustomerVid": sleV2EthernetServiceRtCustomerVid,
       "sleV2EthernetServiceRtNetworkPort": sleV2EthernetServiceRtNetworkPort,
       "sleV2EthernetServiceRtNetworkVid": sleV2EthernetServiceRtNetworkVid,
       "sleV2EthernetServiceRtEnableManagement": sleV2EthernetServiceRtEnableManagement,
       "sleV2EthernetServiceCotExternalPort": sleV2EthernetServiceCotExternalPort,
       "sleV2EthernetServiceCotExternalVid": sleV2EthernetServiceCotExternalVid,
       "sleV2EthernetServiceCotInternalPort": sleV2EthernetServiceCotInternalPort,
       "sleV2EthernetServiceCotInternalVid": sleV2EthernetServiceCotInternalVid,
       "sleV2EthernetServiceControl": sleV2EthernetServiceControl,
       "sleV2EthernetServiceControlRequest": sleV2EthernetServiceControlRequest,
       "sleV2EthernetServiceControlStatus": sleV2EthernetServiceControlStatus,
       "sleV2EthernetServiceControlTimer": sleV2EthernetServiceControlTimer,
       "sleV2EthernetServiceControlTimeStamp": sleV2EthernetServiceControlTimeStamp,
       "sleV2EthernetServiceControlReqResult": sleV2EthernetServiceControlReqResult,
       "sleV2EthernetServiceControlEnableStatus": sleV2EthernetServiceControlEnableStatus,
       "sleV2EthernetServiceControlEnableManagement": sleV2EthernetServiceControlEnableManagement,
       "sleV2EthernetServiceControlHealthCheckPort": sleV2EthernetServiceControlHealthCheckPort,
       "sleV2EthernetServiceControlHealthCheckVid": sleV2EthernetServiceControlHealthCheckVid,
       "sleV2EthernetServiceControlSid": sleV2EthernetServiceControlSid,
       "sleV2EthernetServiceControlType": sleV2EthernetServiceControlType,
       "sleV2EthernetServiceControlRtCustomerPort": sleV2EthernetServiceControlRtCustomerPort,
       "sleV2EthernetServiceControlRtCustomerVid": sleV2EthernetServiceControlRtCustomerVid,
       "sleV2EthernetServiceControlRtNetworkPort": sleV2EthernetServiceControlRtNetworkPort,
       "sleV2EthernetServiceControlRtNetworkVid": sleV2EthernetServiceControlRtNetworkVid,
       "sleV2EthernetServiceControlRtEnableManagement": sleV2EthernetServiceControlRtEnableManagement,
       "sleV2EthernetServiceControlCotExternalPort": sleV2EthernetServiceControlCotExternalPort,
       "sleV2EthernetServiceControlCotExternalVid": sleV2EthernetServiceControlCotExternalVid,
       "sleV2EthernetServiceControlCotInternalPort": sleV2EthernetServiceControlCotInternalPort,
       "sleV2EthernetServiceControlCotInternalVid": sleV2EthernetServiceControlCotInternalVid,
       "sleV2EthernetServiceNotification": sleV2EthernetServiceNotification,
       "sleV2EthernetServiceEnableStatusChanged": sleV2EthernetServiceEnableStatusChanged,
       "sleV2EthernetServiceEnableManagementChanged": sleV2EthernetServiceEnableManagementChanged,
       "sleV2EthernetServiceHealthCheckChanged": sleV2EthernetServiceHealthCheckChanged,
       "sleV2EthernetServiceHealthCheckDeleted": sleV2EthernetServiceHealthCheckDeleted,
       "sleV2EthernetServiceSidForRtModeCreated": sleV2EthernetServiceSidForRtModeCreated,
       "sleV2EthernetServiceSidForCotModeCreated": sleV2EthernetServiceSidForCotModeCreated,
       "sleV2EthernetServiceSidDeleted": sleV2EthernetServiceSidDeleted,
       "sleV2Security6": sleV2Security6,
       "sleV2SecurityGroup": sleV2SecurityGroup,
       "sleV2SecurityNotificationGroup": sleV2SecurityNotificationGroup}
)
