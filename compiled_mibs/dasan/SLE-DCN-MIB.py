# SNMP MIB module (SLE-DCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-DCN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:22 2025
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

sleDCN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleDcnNodeInfo_ObjectIdentity = ObjectIdentity
sleDcnNodeInfo = _SleDcnNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1)
)
_SleDcnNodeBaseInfo_ObjectIdentity = ObjectIdentity
sleDcnNodeBaseInfo = _SleDcnNodeBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1)
)


class _SleDcnNodeType_Type(Integer32):
    """Custom type sleDcnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ne", 0),
          ("gne", 1),
          ("l2ne", 2))
    )


_SleDcnNodeType_Type.__name__ = "Integer32"
_SleDcnNodeType_Object = MibScalar
sleDcnNodeType = _SleDcnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 1),
    _SleDcnNodeType_Type()
)
sleDcnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNodeType.setStatus("current")
_SleDcnMacAddress_Type = OctetString
_SleDcnMacAddress_Object = MibScalar
sleDcnMacAddress = _SleDcnMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 2),
    _SleDcnMacAddress_Type()
)
sleDcnMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnMacAddress.setStatus("current")
_SleDcnLoIp_Type = IpAddress
_SleDcnLoIp_Object = MibScalar
sleDcnLoIp = _SleDcnLoIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 3),
    _SleDcnLoIp_Type()
)
sleDcnLoIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnLoIp.setStatus("current")


class _SleDcnLoIpRegisterType_Type(Integer32):
    """Custom type sleDcnLoIpRegisterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_SleDcnLoIpRegisterType_Type.__name__ = "Integer32"
_SleDcnLoIpRegisterType_Object = MibScalar
sleDcnLoIpRegisterType = _SleDcnLoIpRegisterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 4),
    _SleDcnLoIpRegisterType_Type()
)
sleDcnLoIpRegisterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnLoIpRegisterType.setStatus("current")
_SleDcnIfNetwork_Type = IpAddress
_SleDcnIfNetwork_Object = MibScalar
sleDcnIfNetwork = _SleDcnIfNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 5),
    _SleDcnIfNetwork_Type()
)
sleDcnIfNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfNetwork.setStatus("current")


class _SleDcnIfNetworkRegisterType_Type(Integer32):
    """Custom type sleDcnIfNetworkRegisterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_SleDcnIfNetworkRegisterType_Type.__name__ = "Integer32"
_SleDcnIfNetworkRegisterType_Object = MibScalar
sleDcnIfNetworkRegisterType = _SleDcnIfNetworkRegisterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 6),
    _SleDcnIfNetworkRegisterType_Type()
)
sleDcnIfNetworkRegisterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfNetworkRegisterType.setStatus("current")
_SleNeDcnOspfArea_Type = IpAddress
_SleNeDcnOspfArea_Object = MibScalar
sleNeDcnOspfArea = _SleNeDcnOspfArea_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 7),
    _SleNeDcnOspfArea_Type()
)
sleNeDcnOspfArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNeDcnOspfArea.setStatus("current")


class _SleDcnGneState_Type(Integer32):
    """Custom type sleDcnGneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noneGne", 0),
          ("noCandidate", 1),
          ("waiting", 2),
          ("slave", 3),
          ("master", 4))
    )


_SleDcnGneState_Type.__name__ = "Integer32"
_SleDcnGneState_Object = MibScalar
sleDcnGneState = _SleDcnGneState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 8),
    _SleDcnGneState_Type()
)
sleDcnGneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnGneState.setStatus("current")


class _SleDcnMgneCandidate_Type(Integer32):
    """Custom type sleDcnMgneCandidate based on Integer32"""
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


_SleDcnMgneCandidate_Type.__name__ = "Integer32"
_SleDcnMgneCandidate_Object = MibScalar
sleDcnMgneCandidate = _SleDcnMgneCandidate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 9),
    _SleDcnMgneCandidate_Type()
)
sleDcnMgneCandidate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnMgneCandidate.setStatus("current")


class _SleDcnMgnePriority_Type(Integer32):
    """Custom type sleDcnMgnePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDcnMgnePriority_Type.__name__ = "Integer32"
_SleDcnMgnePriority_Object = MibScalar
sleDcnMgnePriority = _SleDcnMgnePriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 10),
    _SleDcnMgnePriority_Type()
)
sleDcnMgnePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnMgnePriority.setStatus("current")
_SleDcnLoIpBase_Type = IpAddress
_SleDcnLoIpBase_Object = MibScalar
sleDcnLoIpBase = _SleDcnLoIpBase_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 11),
    _SleDcnLoIpBase_Type()
)
sleDcnLoIpBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnLoIpBase.setStatus("current")


class _SleDcnLoIpBasePrefixlen_Type(Integer32):
    """Custom type sleDcnLoIpBasePrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleDcnLoIpBasePrefixlen_Type.__name__ = "Integer32"
_SleDcnLoIpBasePrefixlen_Object = MibScalar
sleDcnLoIpBasePrefixlen = _SleDcnLoIpBasePrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 12),
    _SleDcnLoIpBasePrefixlen_Type()
)
sleDcnLoIpBasePrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnLoIpBasePrefixlen.setStatus("current")
_SleDcnIfIpBase_Type = IpAddress
_SleDcnIfIpBase_Object = MibScalar
sleDcnIfIpBase = _SleDcnIfIpBase_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 13),
    _SleDcnIfIpBase_Type()
)
sleDcnIfIpBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfIpBase.setStatus("current")


class _SleDcnIfIpBasePrefixlen_Type(Integer32):
    """Custom type sleDcnIfIpBasePrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleDcnIfIpBasePrefixlen_Type.__name__ = "Integer32"
_SleDcnIfIpBasePrefixlen_Object = MibScalar
sleDcnIfIpBasePrefixlen = _SleDcnIfIpBasePrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 14),
    _SleDcnIfIpBasePrefixlen_Type()
)
sleDcnIfIpBasePrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfIpBasePrefixlen.setStatus("current")


class _SleDcnL2gwState_Type(Integer32):
    """Custom type sleDcnL2gwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noneL2gw", 0),
          ("noCandidate", 1),
          ("waiting", 2),
          ("slave", 3),
          ("master", 4))
    )


_SleDcnL2gwState_Type.__name__ = "Integer32"
_SleDcnL2gwState_Object = MibScalar
sleDcnL2gwState = _SleDcnL2gwState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 15),
    _SleDcnL2gwState_Type()
)
sleDcnL2gwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnL2gwState.setStatus("current")


class _SleDcnMl2gwCandidate_Type(Integer32):
    """Custom type sleDcnMl2gwCandidate based on Integer32"""
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


_SleDcnMl2gwCandidate_Type.__name__ = "Integer32"
_SleDcnMl2gwCandidate_Object = MibScalar
sleDcnMl2gwCandidate = _SleDcnMl2gwCandidate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 16),
    _SleDcnMl2gwCandidate_Type()
)
sleDcnMl2gwCandidate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnMl2gwCandidate.setStatus("current")


class _SleDcnMl2gwPriority_Type(Integer32):
    """Custom type sleDcnMl2gwPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDcnMl2gwPriority_Type.__name__ = "Integer32"
_SleDcnMl2gwPriority_Object = MibScalar
sleDcnMl2gwPriority = _SleDcnMl2gwPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 17),
    _SleDcnMl2gwPriority_Type()
)
sleDcnMl2gwPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnMl2gwPriority.setStatus("current")
_SleDcnVlanIp_Type = IpAddress
_SleDcnVlanIp_Object = MibScalar
sleDcnVlanIp = _SleDcnVlanIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 18),
    _SleDcnVlanIp_Type()
)
sleDcnVlanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnVlanIp.setStatus("current")


class _SleDcnVlanIpPrefixlen_Type(Integer32):
    """Custom type sleDcnVlanIpPrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleDcnVlanIpPrefixlen_Type.__name__ = "Integer32"
_SleDcnVlanIpPrefixlen_Object = MibScalar
sleDcnVlanIpPrefixlen = _SleDcnVlanIpPrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 19),
    _SleDcnVlanIpPrefixlen_Type()
)
sleDcnVlanIpPrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnVlanIpPrefixlen.setStatus("current")


class _SleDcnVlanIpRegisterType_Type(Integer32):
    """Custom type sleDcnVlanIpRegisterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_SleDcnVlanIpRegisterType_Type.__name__ = "Integer32"
_SleDcnVlanIpRegisterType_Object = MibScalar
sleDcnVlanIpRegisterType = _SleDcnVlanIpRegisterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 20),
    _SleDcnVlanIpRegisterType_Type()
)
sleDcnVlanIpRegisterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnVlanIpRegisterType.setStatus("current")
_SleDcnL2GatewayIp_Type = IpAddress
_SleDcnL2GatewayIp_Object = MibScalar
sleDcnL2GatewayIp = _SleDcnL2GatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 21),
    _SleDcnL2GatewayIp_Type()
)
sleDcnL2GatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnL2GatewayIp.setStatus("current")
_SleDcnMgmtIp_Type = IpAddress
_SleDcnMgmtIp_Object = MibScalar
sleDcnMgmtIp = _SleDcnMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 22),
    _SleDcnMgmtIp_Type()
)
sleDcnMgmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnMgmtIp.setStatus("current")


class _SleDcnMgmtIpPrefixlen_Type(Integer32):
    """Custom type sleDcnMgmtIpPrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleDcnMgmtIpPrefixlen_Type.__name__ = "Integer32"
_SleDcnMgmtIpPrefixlen_Object = MibScalar
sleDcnMgmtIpPrefixlen = _SleDcnMgmtIpPrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 1, 23),
    _SleDcnMgmtIpPrefixlen_Type()
)
sleDcnMgmtIpPrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnMgmtIpPrefixlen.setStatus("current")
_SleDcnNodeBaseControl_ObjectIdentity = ObjectIdentity
sleDcnNodeBaseControl = _SleDcnNodeBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2)
)


class _SleDcnControlRequest_Type(Integer32):
    """Custom type sleDcnControlRequest based on Integer32"""
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
        *(("setNodeType", 1),
          ("dcnLoip", 2),
          ("dcnLoIpBase", 3),
          ("dcnIfNetwork", 4),
          ("dcnIfIpBase", 5),
          ("mgneSwitchOver", 6),
          ("mgneCandidate", 7),
          ("mgnePriority", 8),
          ("l2GatewayEnable", 9),
          ("dcnVlanIp", 10),
          ("ml2gwSwitchOver", 11),
          ("ml2gwCandidate", 12),
          ("ml2gwPriority", 13),
          ("remoteLoip", 14),
          ("remoteIfNetwork", 15),
          ("mgmtIp", 16))
    )


_SleDcnControlRequest_Type.__name__ = "Integer32"
_SleDcnControlRequest_Object = MibScalar
sleDcnControlRequest = _SleDcnControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 1),
    _SleDcnControlRequest_Type()
)
sleDcnControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlRequest.setStatus("current")
_SleDcnControlStatus_Type = SleControlStatusType
_SleDcnControlStatus_Object = MibScalar
sleDcnControlStatus = _SleDcnControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 2),
    _SleDcnControlStatus_Type()
)
sleDcnControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlStatus.setStatus("current")
_SleDcnControlTimer_Type = Gauge32
_SleDcnControlTimer_Object = MibScalar
sleDcnControlTimer = _SleDcnControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 3),
    _SleDcnControlTimer_Type()
)
sleDcnControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlTimer.setStatus("current")
_SleDcnControlTimeStamp_Type = TimeTicks
_SleDcnControlTimeStamp_Object = MibScalar
sleDcnControlTimeStamp = _SleDcnControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 4),
    _SleDcnControlTimeStamp_Type()
)
sleDcnControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlTimeStamp.setStatus("current")
_SleDcnControlReqResult_Type = SleControlRequestResultType
_SleDcnControlReqResult_Object = MibScalar
sleDcnControlReqResult = _SleDcnControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 5),
    _SleDcnControlReqResult_Type()
)
sleDcnControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlReqResult.setStatus("current")


class _SleDcnControlNodeType_Type(Integer32):
    """Custom type sleDcnControlNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ne", 0),
          ("gne", 1),
          ("l2ne", 2))
    )


_SleDcnControlNodeType_Type.__name__ = "Integer32"
_SleDcnControlNodeType_Object = MibScalar
sleDcnControlNodeType = _SleDcnControlNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 6),
    _SleDcnControlNodeType_Type()
)
sleDcnControlNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlNodeType.setStatus("current")
_SleDcnControlDcnLoIp_Type = IpAddress
_SleDcnControlDcnLoIp_Object = MibScalar
sleDcnControlDcnLoIp = _SleDcnControlDcnLoIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 7),
    _SleDcnControlDcnLoIp_Type()
)
sleDcnControlDcnLoIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnLoIp.setStatus("current")
_SleDcnControlDcnLoIpBase_Type = IpAddress
_SleDcnControlDcnLoIpBase_Object = MibScalar
sleDcnControlDcnLoIpBase = _SleDcnControlDcnLoIpBase_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 8),
    _SleDcnControlDcnLoIpBase_Type()
)
sleDcnControlDcnLoIpBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnLoIpBase.setStatus("current")


class _SleDcnControlDcnLoIpBasePrefixlen_Type(Integer32):
    """Custom type sleDcnControlDcnLoIpBasePrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 24),
    )


_SleDcnControlDcnLoIpBasePrefixlen_Type.__name__ = "Integer32"
_SleDcnControlDcnLoIpBasePrefixlen_Object = MibScalar
sleDcnControlDcnLoIpBasePrefixlen = _SleDcnControlDcnLoIpBasePrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 9),
    _SleDcnControlDcnLoIpBasePrefixlen_Type()
)
sleDcnControlDcnLoIpBasePrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnLoIpBasePrefixlen.setStatus("current")
_SleDcnControlDcnIfIpBase_Type = IpAddress
_SleDcnControlDcnIfIpBase_Object = MibScalar
sleDcnControlDcnIfIpBase = _SleDcnControlDcnIfIpBase_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 10),
    _SleDcnControlDcnIfIpBase_Type()
)
sleDcnControlDcnIfIpBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnIfIpBase.setStatus("current")


class _SleDcnControlDcnIfIpBasePrefixlen_Type(Integer32):
    """Custom type sleDcnControlDcnIfIpBasePrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16),
    )


_SleDcnControlDcnIfIpBasePrefixlen_Type.__name__ = "Integer32"
_SleDcnControlDcnIfIpBasePrefixlen_Object = MibScalar
sleDcnControlDcnIfIpBasePrefixlen = _SleDcnControlDcnIfIpBasePrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 11),
    _SleDcnControlDcnIfIpBasePrefixlen_Type()
)
sleDcnControlDcnIfIpBasePrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnIfIpBasePrefixlen.setStatus("current")


class _SleDcnControlDcnMgneCandidate_Type(Integer32):
    """Custom type sleDcnControlDcnMgneCandidate based on Integer32"""
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


_SleDcnControlDcnMgneCandidate_Type.__name__ = "Integer32"
_SleDcnControlDcnMgneCandidate_Object = MibScalar
sleDcnControlDcnMgneCandidate = _SleDcnControlDcnMgneCandidate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 12),
    _SleDcnControlDcnMgneCandidate_Type()
)
sleDcnControlDcnMgneCandidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlDcnMgneCandidate.setStatus("current")


class _SleDcnControlDcnMgnePriority_Type(Integer32):
    """Custom type sleDcnControlDcnMgnePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDcnControlDcnMgnePriority_Type.__name__ = "Integer32"
_SleDcnControlDcnMgnePriority_Object = MibScalar
sleDcnControlDcnMgnePriority = _SleDcnControlDcnMgnePriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 13),
    _SleDcnControlDcnMgnePriority_Type()
)
sleDcnControlDcnMgnePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlDcnMgnePriority.setStatus("current")


class _SleDcnControlL2GatewayEnable_Type(Integer32):
    """Custom type sleDcnControlL2GatewayEnable based on Integer32"""
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


_SleDcnControlL2GatewayEnable_Type.__name__ = "Integer32"
_SleDcnControlL2GatewayEnable_Object = MibScalar
sleDcnControlL2GatewayEnable = _SleDcnControlL2GatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 14),
    _SleDcnControlL2GatewayEnable_Type()
)
sleDcnControlL2GatewayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlL2GatewayEnable.setStatus("current")
_SleDcnControlDcnVlanIp_Type = IpAddress
_SleDcnControlDcnVlanIp_Object = MibScalar
sleDcnControlDcnVlanIp = _SleDcnControlDcnVlanIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 15),
    _SleDcnControlDcnVlanIp_Type()
)
sleDcnControlDcnVlanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnVlanIp.setStatus("current")


class _SleDcnControlDcnVlanIpPrefixlen_Type(Integer32):
    """Custom type sleDcnControlDcnVlanIpPrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 24),
    )


_SleDcnControlDcnVlanIpPrefixlen_Type.__name__ = "Integer32"
_SleDcnControlDcnVlanIpPrefixlen_Object = MibScalar
sleDcnControlDcnVlanIpPrefixlen = _SleDcnControlDcnVlanIpPrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 16),
    _SleDcnControlDcnVlanIpPrefixlen_Type()
)
sleDcnControlDcnVlanIpPrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnVlanIpPrefixlen.setStatus("current")


class _SleDcnControlDcnMl2gwCandidate_Type(Integer32):
    """Custom type sleDcnControlDcnMl2gwCandidate based on Integer32"""
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


_SleDcnControlDcnMl2gwCandidate_Type.__name__ = "Integer32"
_SleDcnControlDcnMl2gwCandidate_Object = MibScalar
sleDcnControlDcnMl2gwCandidate = _SleDcnControlDcnMl2gwCandidate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 17),
    _SleDcnControlDcnMl2gwCandidate_Type()
)
sleDcnControlDcnMl2gwCandidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlDcnMl2gwCandidate.setStatus("current")


class _SleDcnControlDcnMl2gwPriority_Type(Integer32):
    """Custom type sleDcnControlDcnMl2gwPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDcnControlDcnMl2gwPriority_Type.__name__ = "Integer32"
_SleDcnControlDcnMl2gwPriority_Object = MibScalar
sleDcnControlDcnMl2gwPriority = _SleDcnControlDcnMl2gwPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 18),
    _SleDcnControlDcnMl2gwPriority_Type()
)
sleDcnControlDcnMl2gwPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnControlDcnMl2gwPriority.setStatus("current")
_SleDcnControlDcnMacAddr_Type = OctetString
_SleDcnControlDcnMacAddr_Object = MibScalar
sleDcnControlDcnMacAddr = _SleDcnControlDcnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 19),
    _SleDcnControlDcnMacAddr_Type()
)
sleDcnControlDcnMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnMacAddr.setStatus("current")
_SleDcnControlDcnIfNetwork_Type = IpAddress
_SleDcnControlDcnIfNetwork_Object = MibScalar
sleDcnControlDcnIfNetwork = _SleDcnControlDcnIfNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 20),
    _SleDcnControlDcnIfNetwork_Type()
)
sleDcnControlDcnIfNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnIfNetwork.setStatus("current")
_SleDcnControlDcnMgmtIp_Type = IpAddress
_SleDcnControlDcnMgmtIp_Object = MibScalar
sleDcnControlDcnMgmtIp = _SleDcnControlDcnMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 21),
    _SleDcnControlDcnMgmtIp_Type()
)
sleDcnControlDcnMgmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnMgmtIp.setStatus("current")


class _SleDcnControlDcnMgmtIpPrefixlen_Type(Integer32):
    """Custom type sleDcnControlDcnMgmtIpPrefixlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleDcnControlDcnMgmtIpPrefixlen_Type.__name__ = "Integer32"
_SleDcnControlDcnMgmtIpPrefixlen_Object = MibScalar
sleDcnControlDcnMgmtIpPrefixlen = _SleDcnControlDcnMgmtIpPrefixlen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 2, 22),
    _SleDcnControlDcnMgmtIpPrefixlen_Type()
)
sleDcnControlDcnMgmtIpPrefixlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnControlDcnMgmtIpPrefixlen.setStatus("current")
_SleDcnNodeBaseNotification_ObjectIdentity = ObjectIdentity
sleDcnNodeBaseNotification = _SleDcnNodeBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3)
)
_SleDcnGneInfo_ObjectIdentity = ObjectIdentity
sleDcnGneInfo = _SleDcnGneInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2)
)
_SleDcnNe_ObjectIdentity = ObjectIdentity
sleDcnNe = _SleDcnNe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1)
)
_SleDcnNeTable_Object = MibTable
sleDcnNeTable = _SleDcnNeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleDcnNeTable.setStatus("current")
_SleDcnNeEntry_Object = MibTableRow
sleDcnNeEntry = _SleDcnNeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1, 1)
)
sleDcnNeEntry.setIndexNames(
    (0, "SLE-DCN-MIB", "sleDcnNeMacAddress"),
)
if mibBuilder.loadTexts:
    sleDcnNeEntry.setStatus("current")
_SleDcnNeMacAddress_Type = OctetString
_SleDcnNeMacAddress_Object = MibTableColumn
sleDcnNeMacAddress = _SleDcnNeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1, 1, 1),
    _SleDcnNeMacAddress_Type()
)
sleDcnNeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeMacAddress.setStatus("current")
_SleDcnNeLoIpAddr_Type = IpAddress
_SleDcnNeLoIpAddr_Object = MibTableColumn
sleDcnNeLoIpAddr = _SleDcnNeLoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1, 1, 2),
    _SleDcnNeLoIpAddr_Type()
)
sleDcnNeLoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeLoIpAddr.setStatus("current")


class _SleDcnNeLoipRegsterType_Type(Integer32):
    """Custom type sleDcnNeLoipRegsterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_SleDcnNeLoipRegsterType_Type.__name__ = "Integer32"
_SleDcnNeLoipRegsterType_Object = MibTableColumn
sleDcnNeLoipRegsterType = _SleDcnNeLoipRegsterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1, 1, 3),
    _SleDcnNeLoipRegsterType_Type()
)
sleDcnNeLoipRegsterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeLoipRegsterType.setStatus("current")


class _SleDcnNeType_Type(Integer32):
    """Custom type sleDcnNeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ne", 0),
          ("gne", 1),
          ("l2ne", 2))
    )


_SleDcnNeType_Type.__name__ = "Integer32"
_SleDcnNeType_Object = MibTableColumn
sleDcnNeType = _SleDcnNeType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1, 1, 4),
    _SleDcnNeType_Type()
)
sleDcnNeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeType.setStatus("current")


class _SleDcnNeNodeRegisterType_Type(Integer32):
    """Custom type sleDcnNeNodeRegisterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_SleDcnNeNodeRegisterType_Type.__name__ = "Integer32"
_SleDcnNeNodeRegisterType_Object = MibTableColumn
sleDcnNeNodeRegisterType = _SleDcnNeNodeRegisterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1, 1, 5),
    _SleDcnNeNodeRegisterType_Type()
)
sleDcnNeNodeRegisterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeNodeRegisterType.setStatus("current")


class _SleDcnNodeFail_Type(Integer32):
    """Custom type sleDcnNodeFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("fail", 1))
    )


_SleDcnNodeFail_Type.__name__ = "Integer32"
_SleDcnNodeFail_Object = MibTableColumn
sleDcnNodeFail = _SleDcnNodeFail_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 1, 1, 6),
    _SleDcnNodeFail_Type()
)
sleDcnNodeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNodeFail.setStatus("current")
_SleDcnNeSetControl_ObjectIdentity = ObjectIdentity
sleDcnNeSetControl = _SleDcnNeSetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 2)
)


class _SleDcnNeControlRequest_Type(Integer32):
    """Custom type sleDcnNeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("register", 1),
          ("unregister", 2))
    )


_SleDcnNeControlRequest_Type.__name__ = "Integer32"
_SleDcnNeControlRequest_Object = MibScalar
sleDcnNeControlRequest = _SleDcnNeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 2, 1),
    _SleDcnNeControlRequest_Type()
)
sleDcnNeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnNeControlRequest.setStatus("current")
_SleDcnNeControlStatus_Type = SleControlStatusType
_SleDcnNeControlStatus_Object = MibScalar
sleDcnNeControlStatus = _SleDcnNeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 2, 2),
    _SleDcnNeControlStatus_Type()
)
sleDcnNeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeControlStatus.setStatus("current")
_SleDcnNeControlTimer_Type = Gauge32
_SleDcnNeControlTimer_Object = MibScalar
sleDcnNeControlTimer = _SleDcnNeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 2, 3),
    _SleDcnNeControlTimer_Type()
)
sleDcnNeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnNeControlTimer.setStatus("current")
_SleDcnNeControlTimeStamp_Type = TimeTicks
_SleDcnNeControlTimeStamp_Object = MibScalar
sleDcnNeControlTimeStamp = _SleDcnNeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 2, 4),
    _SleDcnNeControlTimeStamp_Type()
)
sleDcnNeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeControlTimeStamp.setStatus("current")
_SleDcnNeControlReqResult_Type = SleControlRequestResultType
_SleDcnNeControlReqResult_Object = MibScalar
sleDcnNeControlReqResult = _SleDcnNeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 2, 5),
    _SleDcnNeControlReqResult_Type()
)
sleDcnNeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNeControlReqResult.setStatus("current")
_SleDcnNeControlNeMacAddr_Type = OctetString
_SleDcnNeControlNeMacAddr_Object = MibScalar
sleDcnNeControlNeMacAddr = _SleDcnNeControlNeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 2, 6),
    _SleDcnNeControlNeMacAddr_Type()
)
sleDcnNeControlNeMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnNeControlNeMacAddr.setStatus("current")
_SleDcnProxySetNotification_ObjectIdentity = ObjectIdentity
sleDcnProxySetNotification = _SleDcnProxySetNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 3)
)
_SleDcnNeInfo_ObjectIdentity = ObjectIdentity
sleDcnNeInfo = _SleDcnNeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3)
)
_SleDcnGNE_ObjectIdentity = ObjectIdentity
sleDcnGNE = _SleDcnGNE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1)
)
_SleDcnGneTable_Object = MibTable
sleDcnGneTable = _SleDcnGneTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleDcnGneTable.setStatus("current")
_SleDcnGneEntry_Object = MibTableRow
sleDcnGneEntry = _SleDcnGneEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1, 1)
)
sleDcnGneEntry.setIndexNames(
    (0, "SLE-DCN-MIB", "sleDcnGneMasterType"),
    (0, "SLE-DCN-MIB", "sleDcnGneMacAddr"),
)
if mibBuilder.loadTexts:
    sleDcnGneEntry.setStatus("current")


class _SleDcnGneMasterType_Type(Integer32):
    """Custom type sleDcnGneMasterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gne", 1),
          ("l2gw", 2))
    )


_SleDcnGneMasterType_Type.__name__ = "Integer32"
_SleDcnGneMasterType_Object = MibTableColumn
sleDcnGneMasterType = _SleDcnGneMasterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1, 1, 1),
    _SleDcnGneMasterType_Type()
)
sleDcnGneMasterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnGneMasterType.setStatus("current")
_SleDcnGneMacAddr_Type = OctetString
_SleDcnGneMacAddr_Object = MibTableColumn
sleDcnGneMacAddr = _SleDcnGneMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1, 1, 2),
    _SleDcnGneMacAddr_Type()
)
sleDcnGneMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnGneMacAddr.setStatus("current")
_SleDcnGneLoIpAddr_Type = IpAddress
_SleDcnGneLoIpAddr_Object = MibTableColumn
sleDcnGneLoIpAddr = _SleDcnGneLoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1, 1, 3),
    _SleDcnGneLoIpAddr_Type()
)
sleDcnGneLoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnGneLoIpAddr.setStatus("current")


class _SleDcnGneNodeType_Type(Integer32):
    """Custom type sleDcnGneNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ne", 0),
          ("gne", 1),
          ("l2ne", 2))
    )


_SleDcnGneNodeType_Type.__name__ = "Integer32"
_SleDcnGneNodeType_Object = MibTableColumn
sleDcnGneNodeType = _SleDcnGneNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1, 1, 4),
    _SleDcnGneNodeType_Type()
)
sleDcnGneNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnGneNodeType.setStatus("current")


class _SleDcnGNeGatewayState_Type(Integer32):
    """Custom type sleDcnGNeGatewayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("noCandidate", 1),
          ("waiting", 2),
          ("slave", 3),
          ("master", 4))
    )


_SleDcnGNeGatewayState_Type.__name__ = "Integer32"
_SleDcnGNeGatewayState_Object = MibTableColumn
sleDcnGNeGatewayState = _SleDcnGNeGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1, 1, 5),
    _SleDcnGNeGatewayState_Type()
)
sleDcnGNeGatewayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnGNeGatewayState.setStatus("current")


class _SleDcnGneNodeFail_Type(Integer32):
    """Custom type sleDcnGneNodeFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("fail", 1))
    )


_SleDcnGneNodeFail_Type.__name__ = "Integer32"
_SleDcnGneNodeFail_Object = MibTableColumn
sleDcnGneNodeFail = _SleDcnGneNodeFail_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 3, 1, 1, 1, 6),
    _SleDcnGneNodeFail_Type()
)
sleDcnGneNodeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnGneNodeFail.setStatus("current")
_SleDcnInterface_ObjectIdentity = ObjectIdentity
sleDcnInterface = _SleDcnInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4)
)
_SleDcnIf_ObjectIdentity = ObjectIdentity
sleDcnIf = _SleDcnIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1)
)
_SleDcnIfTable_Object = MibTable
sleDcnIfTable = _SleDcnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleDcnIfTable.setStatus("current")
_SleDcnIfEntry_Object = MibTableRow
sleDcnIfEntry = _SleDcnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1)
)
sleDcnIfEntry.setIndexNames(
    (0, "SLE-DCN-MIB", "sleDcnIfIndex"),
)
if mibBuilder.loadTexts:
    sleDcnIfEntry.setStatus("current")


class _SleDcnIfIndex_Type(Integer32):
    """Custom type sleDcnIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleDcnIfIndex_Type.__name__ = "Integer32"
_SleDcnIfIndex_Object = MibTableColumn
sleDcnIfIndex = _SleDcnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 1),
    _SleDcnIfIndex_Type()
)
sleDcnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfIndex.setStatus("current")


class _SleDcnIfName_Type(OctetString):
    """Custom type sleDcnIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleDcnIfName_Type.__name__ = "OctetString"
_SleDcnIfName_Object = MibTableColumn
sleDcnIfName = _SleDcnIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 2),
    _SleDcnIfName_Type()
)
sleDcnIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfName.setStatus("current")


class _SleDcnIfDcnMode_Type(Integer32):
    """Custom type sleDcnIfDcnMode based on Integer32"""
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
        *(("noDcnIf", 0),
          ("auto", 1),
          ("passive", 2),
          ("l2", 3))
    )


_SleDcnIfDcnMode_Type.__name__ = "Integer32"
_SleDcnIfDcnMode_Object = MibTableColumn
sleDcnIfDcnMode = _SleDcnIfDcnMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 3),
    _SleDcnIfDcnMode_Type()
)
sleDcnIfDcnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfDcnMode.setStatus("current")
_SleDcnIfAllocIpAddress_Type = IpAddress
_SleDcnIfAllocIpAddress_Object = MibTableColumn
sleDcnIfAllocIpAddress = _SleDcnIfAllocIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 4),
    _SleDcnIfAllocIpAddress_Type()
)
sleDcnIfAllocIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfAllocIpAddress.setStatus("current")
_SleDcnIfCurrentIpAddress_Type = IpAddress
_SleDcnIfCurrentIpAddress_Object = MibTableColumn
sleDcnIfCurrentIpAddress = _SleDcnIfCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 5),
    _SleDcnIfCurrentIpAddress_Type()
)
sleDcnIfCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfCurrentIpAddress.setStatus("current")
_SleDcnIfGneOspfArea_Type = IpAddress
_SleDcnIfGneOspfArea_Object = MibTableColumn
sleDcnIfGneOspfArea = _SleDcnIfGneOspfArea_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 6),
    _SleDcnIfGneOspfArea_Type()
)
sleDcnIfGneOspfArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfGneOspfArea.setStatus("current")
_SleDcnNearMacAddress_Type = OctetString
_SleDcnNearMacAddress_Object = MibTableColumn
sleDcnNearMacAddress = _SleDcnNearMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 7),
    _SleDcnNearMacAddress_Type()
)
sleDcnNearMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNearMacAddress.setStatus("current")
_SleDcnNearNodeLoIpAddr_Type = IpAddress
_SleDcnNearNodeLoIpAddr_Object = MibTableColumn
sleDcnNearNodeLoIpAddr = _SleDcnNearNodeLoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 8),
    _SleDcnNearNodeLoIpAddr_Type()
)
sleDcnNearNodeLoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNearNodeLoIpAddr.setStatus("current")


class _SleDcnNearNodeIfName_Type(OctetString):
    """Custom type sleDcnNearNodeIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleDcnNearNodeIfName_Type.__name__ = "OctetString"
_SleDcnNearNodeIfName_Object = MibTableColumn
sleDcnNearNodeIfName = _SleDcnNearNodeIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 9),
    _SleDcnNearNodeIfName_Type()
)
sleDcnNearNodeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNearNodeIfName.setStatus("current")


class _SleDcnNearIfFail_Type(Integer32):
    """Custom type sleDcnNearIfFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("fail", 1))
    )


_SleDcnNearIfFail_Type.__name__ = "Integer32"
_SleDcnNearIfFail_Object = MibTableColumn
sleDcnNearIfFail = _SleDcnNearIfFail_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 1, 1, 10),
    _SleDcnNearIfFail_Type()
)
sleDcnNearIfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnNearIfFail.setStatus("current")
_SleDcnIfControl_ObjectIdentity = ObjectIdentity
sleDcnIfControl = _SleDcnIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2)
)


class _SleDcnIfControlRequest_Type(Integer32):
    """Custom type sleDcnIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcnifDcnMode", 1),
          ("gneIfOspfArea", 2))
    )


_SleDcnIfControlRequest_Type.__name__ = "Integer32"
_SleDcnIfControlRequest_Object = MibScalar
sleDcnIfControlRequest = _SleDcnIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 1),
    _SleDcnIfControlRequest_Type()
)
sleDcnIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnIfControlRequest.setStatus("current")
_SleDcnIfControlStatus_Type = SleControlStatusType
_SleDcnIfControlStatus_Object = MibScalar
sleDcnIfControlStatus = _SleDcnIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 2),
    _SleDcnIfControlStatus_Type()
)
sleDcnIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfControlStatus.setStatus("current")
_SleDcnIfControlTimer_Type = Gauge32
_SleDcnIfControlTimer_Object = MibScalar
sleDcnIfControlTimer = _SleDcnIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 3),
    _SleDcnIfControlTimer_Type()
)
sleDcnIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnIfControlTimer.setStatus("current")
_SleDcnIfControlTimeStamp_Type = TimeTicks
_SleDcnIfControlTimeStamp_Object = MibScalar
sleDcnIfControlTimeStamp = _SleDcnIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 4),
    _SleDcnIfControlTimeStamp_Type()
)
sleDcnIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfControlTimeStamp.setStatus("current")
_SleDcnIfControlReqResult_Type = SleControlRequestResultType
_SleDcnIfControlReqResult_Object = MibScalar
sleDcnIfControlReqResult = _SleDcnIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 5),
    _SleDcnIfControlReqResult_Type()
)
sleDcnIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDcnIfControlReqResult.setStatus("current")
_SleDcnIfControlIfIndex_Type = Integer32
_SleDcnIfControlIfIndex_Object = MibScalar
sleDcnIfControlIfIndex = _SleDcnIfControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 6),
    _SleDcnIfControlIfIndex_Type()
)
sleDcnIfControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnIfControlIfIndex.setStatus("current")


class _SleDcnIfControlDcnMode_Type(Integer32):
    """Custom type sleDcnIfControlDcnMode based on Integer32"""
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
        *(("noDcnIf", 0),
          ("auto", 1),
          ("passive", 2),
          ("l2", 3))
    )


_SleDcnIfControlDcnMode_Type.__name__ = "Integer32"
_SleDcnIfControlDcnMode_Object = MibScalar
sleDcnIfControlDcnMode = _SleDcnIfControlDcnMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 7),
    _SleDcnIfControlDcnMode_Type()
)
sleDcnIfControlDcnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnIfControlDcnMode.setStatus("current")
_SleDcnIfControlGneOspfArea_Type = IpAddress
_SleDcnIfControlGneOspfArea_Object = MibScalar
sleDcnIfControlGneOspfArea = _SleDcnIfControlGneOspfArea_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 2, 8),
    _SleDcnIfControlGneOspfArea_Type()
)
sleDcnIfControlGneOspfArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDcnIfControlGneOspfArea.setStatus("current")
_SleDcnIfNotification_ObjectIdentity = ObjectIdentity
sleDcnIfNotification = _SleDcnIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 3)
)

# Managed Objects groups

sleDcnObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 13)
)
sleDcnObjectGroup.setObjects(
      *(("SLE-DCN-MIB", "sleDcnNodeType"),
        ("SLE-DCN-MIB", "sleDcnMacAddress"),
        ("SLE-DCN-MIB", "sleDcnMgneCandidate"),
        ("SLE-DCN-MIB", "sleDcnMgnePriority"),
        ("SLE-DCN-MIB", "sleDcnIfIpBase"),
        ("SLE-DCN-MIB", "sleDcnIfIpBasePrefixlen"),
        ("SLE-DCN-MIB", "sleDcnL2gwState"),
        ("SLE-DCN-MIB", "sleDcnMl2gwCandidate"),
        ("SLE-DCN-MIB", "sleDcnMl2gwPriority"),
        ("SLE-DCN-MIB", "sleDcnControlDcnIfIpBase"),
        ("SLE-DCN-MIB", "sleDcnControlDcnIfIpBasePrefixlen"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgneCandidate"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgnePriority"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMl2gwCandidate"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMl2gwPriority"),
        ("SLE-DCN-MIB", "sleDcnNeMacAddress"),
        ("SLE-DCN-MIB", "sleDcnNeLoIpAddr"),
        ("SLE-DCN-MIB", "sleDcnNeLoipRegsterType"),
        ("SLE-DCN-MIB", "sleDcnNeNodeRegisterType"),
        ("SLE-DCN-MIB", "sleDcnNeControlRequest"),
        ("SLE-DCN-MIB", "sleDcnNeControlStatus"),
        ("SLE-DCN-MIB", "sleDcnNeControlTimer"),
        ("SLE-DCN-MIB", "sleDcnNeControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnNeControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnNeControlNeMacAddr"),
        ("SLE-DCN-MIB", "sleDcnGneMacAddr"),
        ("SLE-DCN-MIB", "sleDcnGneNodeType"),
        ("SLE-DCN-MIB", "sleDcnGNeGatewayState"),
        ("SLE-DCN-MIB", "sleDcnIfName"),
        ("SLE-DCN-MIB", "sleDcnIfDcnMode"),
        ("SLE-DCN-MIB", "sleDcnIfAllocIpAddress"),
        ("SLE-DCN-MIB", "sleDcnIfCurrentIpAddress"),
        ("SLE-DCN-MIB", "sleDcnIfControlDcnMode"),
        ("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlStatus"),
        ("SLE-DCN-MIB", "sleDcnControlTimer"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlNodeType"),
        ("SLE-DCN-MIB", "sleDcnNodeFail"),
        ("SLE-DCN-MIB", "sleDcnGneLoIpAddr"),
        ("SLE-DCN-MIB", "sleDcnGneNodeFail"),
        ("SLE-DCN-MIB", "sleDcnIfIndex"),
        ("SLE-DCN-MIB", "sleDcnNearNodeLoIpAddr"),
        ("SLE-DCN-MIB", "sleDcnNearNodeIfName"),
        ("SLE-DCN-MIB", "sleDcnIfControlRequest"),
        ("SLE-DCN-MIB", "sleDcnIfControlStatus"),
        ("SLE-DCN-MIB", "sleDcnIfControlTimer"),
        ("SLE-DCN-MIB", "sleDcnIfControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnIfControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnIfControlIfIndex"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgmtIp"),
        ("SLE-DCN-MIB", "sleDcnMgmtIp"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgmtIpPrefixlen"),
        ("SLE-DCN-MIB", "sleDcnMgmtIpPrefixlen"),
        ("SLE-DCN-MIB", "sleDcnControlDcnVlanIpPrefixlen"),
        ("SLE-DCN-MIB", "sleDcnVlanIpPrefixlen"),
        ("SLE-DCN-MIB", "sleDcnNearIfFail"),
        ("SLE-DCN-MIB", "sleDcnGneState"),
        ("SLE-DCN-MIB", "sleDcnNeType"),
        ("SLE-DCN-MIB", "sleDcnLoIpBase"),
        ("SLE-DCN-MIB", "sleDcnLoIpBasePrefixlen"),
        ("SLE-DCN-MIB", "sleDcnLoIp"),
        ("SLE-DCN-MIB", "sleDcnVlanIp"),
        ("SLE-DCN-MIB", "sleNeDcnOspfArea"),
        ("SLE-DCN-MIB", "sleDcnControlL2GatewayEnable"),
        ("SLE-DCN-MIB", "sleDcnControlDcnLoIpBase"),
        ("SLE-DCN-MIB", "sleDcnControlDcnLoIpBasePrefixlen"),
        ("SLE-DCN-MIB", "sleDcnControlDcnLoIp"),
        ("SLE-DCN-MIB", "sleDcnControlDcnVlanIp"),
        ("SLE-DCN-MIB", "sleDcnIfGneOspfArea"),
        ("SLE-DCN-MIB", "sleDcnL2GatewayIp"),
        ("SLE-DCN-MIB", "sleDcnIfControlGneOspfArea"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMacAddr"),
        ("SLE-DCN-MIB", "sleDcnControlDcnIfNetwork"),
        ("SLE-DCN-MIB", "sleDcnNearMacAddress"),
        ("SLE-DCN-MIB", "sleDcnGneMasterType"),
        ("SLE-DCN-MIB", "sleDcnLoIpRegisterType"),
        ("SLE-DCN-MIB", "sleDcnIfNetwork"),
        ("SLE-DCN-MIB", "sleDcnIfNetworkRegisterType"),
        ("SLE-DCN-MIB", "sleDcnVlanIpRegisterType"))
)
if mibBuilder.loadTexts:
    sleDcnObjectGroup.setStatus("current")


# Notification objects

sleDcnNodeTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 1)
)
sleDcnNodeTypeChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlNodeType"))
)
if mibBuilder.loadTexts:
    sleDcnNodeTypeChanged.setStatus(
        "current"
    )

sleDcnLoIpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 2)
)
sleDcnLoIpChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnLoIp"))
)
if mibBuilder.loadTexts:
    sleDcnLoIpChanged.setStatus(
        "current"
    )

sleDcnLoIpBaseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 3)
)
sleDcnLoIpBaseChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnLoIpBase"),
        ("SLE-DCN-MIB", "sleDcnControlDcnLoIpBasePrefixlen"))
)
if mibBuilder.loadTexts:
    sleDcnLoIpBaseChanged.setStatus(
        "current"
    )

sleDcnIfNetworkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 4)
)
sleDcnIfNetworkChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnIfNetwork"))
)
if mibBuilder.loadTexts:
    sleDcnIfNetworkChanged.setStatus(
        "current"
    )

sleDcnIfIpBaseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 5)
)
sleDcnIfIpBaseChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnIfIpBase"),
        ("SLE-DCN-MIB", "sleDcnControlDcnIfIpBasePrefixlen"))
)
if mibBuilder.loadTexts:
    sleDcnIfIpBaseChanged.setStatus(
        "current"
    )

sleDcnMgneSwitchOverChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 6)
)
sleDcnMgneSwitchOverChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDcnMgneSwitchOverChanged.setStatus(
        "current"
    )

sleDcnMgneCandidateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 7)
)
sleDcnMgneCandidateChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgneCandidate"))
)
if mibBuilder.loadTexts:
    sleDcnMgneCandidateChanged.setStatus(
        "current"
    )

sleDcnMgnePriorityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 8)
)
sleDcnMgnePriorityChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgnePriority"))
)
if mibBuilder.loadTexts:
    sleDcnMgnePriorityChanged.setStatus(
        "current"
    )

sleDcnL2GatewayEnableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 9)
)
sleDcnL2GatewayEnableChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlL2GatewayEnable"))
)
if mibBuilder.loadTexts:
    sleDcnL2GatewayEnableChanged.setStatus(
        "current"
    )

sleDcnVlanIpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 10)
)
sleDcnVlanIpChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnVlanIp"),
        ("SLE-DCN-MIB", "sleDcnControlDcnVlanIpPrefixlen"))
)
if mibBuilder.loadTexts:
    sleDcnVlanIpChanged.setStatus(
        "current"
    )

sleDcnMl2gwSwitchOverChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 11)
)
sleDcnMl2gwSwitchOverChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDcnMl2gwSwitchOverChanged.setStatus(
        "current"
    )

sleDcnMl2gwCandidateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 12)
)
sleDcnMl2gwCandidateChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMl2gwCandidate"))
)
if mibBuilder.loadTexts:
    sleDcnMl2gwCandidateChanged.setStatus(
        "current"
    )

sleDcnMl2gwPriorityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 13)
)
sleDcnMl2gwPriorityChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMl2gwPriority"))
)
if mibBuilder.loadTexts:
    sleDcnMl2gwPriorityChanged.setStatus(
        "current"
    )

sleDcnRemoteLoIpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 14)
)
sleDcnRemoteLoIpChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMacAddr"),
        ("SLE-DCN-MIB", "sleDcnControlDcnLoIp"))
)
if mibBuilder.loadTexts:
    sleDcnRemoteLoIpChanged.setStatus(
        "current"
    )

sleDcnRemoteIfNetworkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 15)
)
sleDcnRemoteIfNetworkChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMacAddr"),
        ("SLE-DCN-MIB", "sleDcnControlDcnIfNetwork"))
)
if mibBuilder.loadTexts:
    sleDcnRemoteIfNetworkChanged.setStatus(
        "current"
    )

sleDcnMgmtIpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 1, 3, 16)
)
sleDcnMgmtIpChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnControlRequest"),
        ("SLE-DCN-MIB", "sleDcnControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgmtIp"),
        ("SLE-DCN-MIB", "sleDcnControlDcnMgmtIpPrefixlen"))
)
if mibBuilder.loadTexts:
    sleDcnMgmtIpChanged.setStatus(
        "current"
    )

sleDcnNeRegisterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 3, 1)
)
sleDcnNeRegisterChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnNeControlRequest"),
        ("SLE-DCN-MIB", "sleDcnNeControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnNeControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnNeControlNeMacAddr"))
)
if mibBuilder.loadTexts:
    sleDcnNeRegisterChanged.setStatus(
        "current"
    )

sleDcnNeUnegisterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 2, 1, 3, 2)
)
sleDcnNeUnegisterChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnNeControlRequest"),
        ("SLE-DCN-MIB", "sleDcnNeControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnNeControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnNeControlNeMacAddr"))
)
if mibBuilder.loadTexts:
    sleDcnNeUnegisterChanged.setStatus(
        "current"
    )

sleDcnIfModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 3, 1)
)
sleDcnIfModeChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnIfControlRequest"),
        ("SLE-DCN-MIB", "sleDcnIfControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnIfControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnIfControlIfIndex"),
        ("SLE-DCN-MIB", "sleDcnIfControlDcnMode"))
)
if mibBuilder.loadTexts:
    sleDcnIfModeChanged.setStatus(
        "current"
    )

sleDcnIfGneOspfAreaChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 4, 1, 3, 2)
)
sleDcnIfGneOspfAreaChanged.setObjects(
      *(("SLE-DCN-MIB", "sleDcnIfControlRequest"),
        ("SLE-DCN-MIB", "sleDcnIfControlTimeStamp"),
        ("SLE-DCN-MIB", "sleDcnIfControlReqResult"),
        ("SLE-DCN-MIB", "sleDcnIfControlIfIndex"),
        ("SLE-DCN-MIB", "sleDcnIfControlGneOspfArea"))
)
if mibBuilder.loadTexts:
    sleDcnIfGneOspfAreaChanged.setStatus(
        "current"
    )


# Notifications groups

sleDcnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 91, 14)
)
sleDcnNotificationGroup.setObjects(
      *(("SLE-DCN-MIB", "sleDcnIfIpBaseChanged"),
        ("SLE-DCN-MIB", "sleDcnMgneSwitchOverChanged"),
        ("SLE-DCN-MIB", "sleDcnMgneCandidateChanged"),
        ("SLE-DCN-MIB", "sleDcnMgnePriorityChanged"),
        ("SLE-DCN-MIB", "sleDcnMl2gwSwitchOverChanged"),
        ("SLE-DCN-MIB", "sleDcnMl2gwCandidateChanged"),
        ("SLE-DCN-MIB", "sleDcnMl2gwPriorityChanged"),
        ("SLE-DCN-MIB", "sleDcnNeRegisterChanged"),
        ("SLE-DCN-MIB", "sleDcnNeUnegisterChanged"),
        ("SLE-DCN-MIB", "sleDcnIfModeChanged"),
        ("SLE-DCN-MIB", "sleDcnNodeTypeChanged"),
        ("SLE-DCN-MIB", "sleDcnMgmtIpChanged"),
        ("SLE-DCN-MIB", "sleDcnL2GatewayEnableChanged"),
        ("SLE-DCN-MIB", "sleDcnIfNetworkChanged"),
        ("SLE-DCN-MIB", "sleDcnRemoteLoIpChanged"),
        ("SLE-DCN-MIB", "sleDcnRemoteIfNetworkChanged"),
        ("SLE-DCN-MIB", "sleDcnLoIpBaseChanged"),
        ("SLE-DCN-MIB", "sleDcnLoIpChanged"),
        ("SLE-DCN-MIB", "sleDcnVlanIpChanged"),
        ("SLE-DCN-MIB", "sleDcnIfGneOspfAreaChanged"))
)
if mibBuilder.loadTexts:
    sleDcnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-DCN-MIB",
    **{"sleDCN": sleDCN,
       "sleDcnNodeInfo": sleDcnNodeInfo,
       "sleDcnNodeBaseInfo": sleDcnNodeBaseInfo,
       "sleDcnNodeType": sleDcnNodeType,
       "sleDcnMacAddress": sleDcnMacAddress,
       "sleDcnLoIp": sleDcnLoIp,
       "sleDcnLoIpRegisterType": sleDcnLoIpRegisterType,
       "sleDcnIfNetwork": sleDcnIfNetwork,
       "sleDcnIfNetworkRegisterType": sleDcnIfNetworkRegisterType,
       "sleNeDcnOspfArea": sleNeDcnOspfArea,
       "sleDcnGneState": sleDcnGneState,
       "sleDcnMgneCandidate": sleDcnMgneCandidate,
       "sleDcnMgnePriority": sleDcnMgnePriority,
       "sleDcnLoIpBase": sleDcnLoIpBase,
       "sleDcnLoIpBasePrefixlen": sleDcnLoIpBasePrefixlen,
       "sleDcnIfIpBase": sleDcnIfIpBase,
       "sleDcnIfIpBasePrefixlen": sleDcnIfIpBasePrefixlen,
       "sleDcnL2gwState": sleDcnL2gwState,
       "sleDcnMl2gwCandidate": sleDcnMl2gwCandidate,
       "sleDcnMl2gwPriority": sleDcnMl2gwPriority,
       "sleDcnVlanIp": sleDcnVlanIp,
       "sleDcnVlanIpPrefixlen": sleDcnVlanIpPrefixlen,
       "sleDcnVlanIpRegisterType": sleDcnVlanIpRegisterType,
       "sleDcnL2GatewayIp": sleDcnL2GatewayIp,
       "sleDcnMgmtIp": sleDcnMgmtIp,
       "sleDcnMgmtIpPrefixlen": sleDcnMgmtIpPrefixlen,
       "sleDcnNodeBaseControl": sleDcnNodeBaseControl,
       "sleDcnControlRequest": sleDcnControlRequest,
       "sleDcnControlStatus": sleDcnControlStatus,
       "sleDcnControlTimer": sleDcnControlTimer,
       "sleDcnControlTimeStamp": sleDcnControlTimeStamp,
       "sleDcnControlReqResult": sleDcnControlReqResult,
       "sleDcnControlNodeType": sleDcnControlNodeType,
       "sleDcnControlDcnLoIp": sleDcnControlDcnLoIp,
       "sleDcnControlDcnLoIpBase": sleDcnControlDcnLoIpBase,
       "sleDcnControlDcnLoIpBasePrefixlen": sleDcnControlDcnLoIpBasePrefixlen,
       "sleDcnControlDcnIfIpBase": sleDcnControlDcnIfIpBase,
       "sleDcnControlDcnIfIpBasePrefixlen": sleDcnControlDcnIfIpBasePrefixlen,
       "sleDcnControlDcnMgneCandidate": sleDcnControlDcnMgneCandidate,
       "sleDcnControlDcnMgnePriority": sleDcnControlDcnMgnePriority,
       "sleDcnControlL2GatewayEnable": sleDcnControlL2GatewayEnable,
       "sleDcnControlDcnVlanIp": sleDcnControlDcnVlanIp,
       "sleDcnControlDcnVlanIpPrefixlen": sleDcnControlDcnVlanIpPrefixlen,
       "sleDcnControlDcnMl2gwCandidate": sleDcnControlDcnMl2gwCandidate,
       "sleDcnControlDcnMl2gwPriority": sleDcnControlDcnMl2gwPriority,
       "sleDcnControlDcnMacAddr": sleDcnControlDcnMacAddr,
       "sleDcnControlDcnIfNetwork": sleDcnControlDcnIfNetwork,
       "sleDcnControlDcnMgmtIp": sleDcnControlDcnMgmtIp,
       "sleDcnControlDcnMgmtIpPrefixlen": sleDcnControlDcnMgmtIpPrefixlen,
       "sleDcnNodeBaseNotification": sleDcnNodeBaseNotification,
       "sleDcnNodeTypeChanged": sleDcnNodeTypeChanged,
       "sleDcnLoIpChanged": sleDcnLoIpChanged,
       "sleDcnLoIpBaseChanged": sleDcnLoIpBaseChanged,
       "sleDcnIfNetworkChanged": sleDcnIfNetworkChanged,
       "sleDcnIfIpBaseChanged": sleDcnIfIpBaseChanged,
       "sleDcnMgneSwitchOverChanged": sleDcnMgneSwitchOverChanged,
       "sleDcnMgneCandidateChanged": sleDcnMgneCandidateChanged,
       "sleDcnMgnePriorityChanged": sleDcnMgnePriorityChanged,
       "sleDcnL2GatewayEnableChanged": sleDcnL2GatewayEnableChanged,
       "sleDcnVlanIpChanged": sleDcnVlanIpChanged,
       "sleDcnMl2gwSwitchOverChanged": sleDcnMl2gwSwitchOverChanged,
       "sleDcnMl2gwCandidateChanged": sleDcnMl2gwCandidateChanged,
       "sleDcnMl2gwPriorityChanged": sleDcnMl2gwPriorityChanged,
       "sleDcnRemoteLoIpChanged": sleDcnRemoteLoIpChanged,
       "sleDcnRemoteIfNetworkChanged": sleDcnRemoteIfNetworkChanged,
       "sleDcnMgmtIpChanged": sleDcnMgmtIpChanged,
       "sleDcnGneInfo": sleDcnGneInfo,
       "sleDcnNe": sleDcnNe,
       "sleDcnNeTable": sleDcnNeTable,
       "sleDcnNeEntry": sleDcnNeEntry,
       "sleDcnNeMacAddress": sleDcnNeMacAddress,
       "sleDcnNeLoIpAddr": sleDcnNeLoIpAddr,
       "sleDcnNeLoipRegsterType": sleDcnNeLoipRegsterType,
       "sleDcnNeType": sleDcnNeType,
       "sleDcnNeNodeRegisterType": sleDcnNeNodeRegisterType,
       "sleDcnNodeFail": sleDcnNodeFail,
       "sleDcnNeSetControl": sleDcnNeSetControl,
       "sleDcnNeControlRequest": sleDcnNeControlRequest,
       "sleDcnNeControlStatus": sleDcnNeControlStatus,
       "sleDcnNeControlTimer": sleDcnNeControlTimer,
       "sleDcnNeControlTimeStamp": sleDcnNeControlTimeStamp,
       "sleDcnNeControlReqResult": sleDcnNeControlReqResult,
       "sleDcnNeControlNeMacAddr": sleDcnNeControlNeMacAddr,
       "sleDcnProxySetNotification": sleDcnProxySetNotification,
       "sleDcnNeRegisterChanged": sleDcnNeRegisterChanged,
       "sleDcnNeUnegisterChanged": sleDcnNeUnegisterChanged,
       "sleDcnNeInfo": sleDcnNeInfo,
       "sleDcnGNE": sleDcnGNE,
       "sleDcnGneTable": sleDcnGneTable,
       "sleDcnGneEntry": sleDcnGneEntry,
       "sleDcnGneMasterType": sleDcnGneMasterType,
       "sleDcnGneMacAddr": sleDcnGneMacAddr,
       "sleDcnGneLoIpAddr": sleDcnGneLoIpAddr,
       "sleDcnGneNodeType": sleDcnGneNodeType,
       "sleDcnGNeGatewayState": sleDcnGNeGatewayState,
       "sleDcnGneNodeFail": sleDcnGneNodeFail,
       "sleDcnInterface": sleDcnInterface,
       "sleDcnIf": sleDcnIf,
       "sleDcnIfTable": sleDcnIfTable,
       "sleDcnIfEntry": sleDcnIfEntry,
       "sleDcnIfIndex": sleDcnIfIndex,
       "sleDcnIfName": sleDcnIfName,
       "sleDcnIfDcnMode": sleDcnIfDcnMode,
       "sleDcnIfAllocIpAddress": sleDcnIfAllocIpAddress,
       "sleDcnIfCurrentIpAddress": sleDcnIfCurrentIpAddress,
       "sleDcnIfGneOspfArea": sleDcnIfGneOspfArea,
       "sleDcnNearMacAddress": sleDcnNearMacAddress,
       "sleDcnNearNodeLoIpAddr": sleDcnNearNodeLoIpAddr,
       "sleDcnNearNodeIfName": sleDcnNearNodeIfName,
       "sleDcnNearIfFail": sleDcnNearIfFail,
       "sleDcnIfControl": sleDcnIfControl,
       "sleDcnIfControlRequest": sleDcnIfControlRequest,
       "sleDcnIfControlStatus": sleDcnIfControlStatus,
       "sleDcnIfControlTimer": sleDcnIfControlTimer,
       "sleDcnIfControlTimeStamp": sleDcnIfControlTimeStamp,
       "sleDcnIfControlReqResult": sleDcnIfControlReqResult,
       "sleDcnIfControlIfIndex": sleDcnIfControlIfIndex,
       "sleDcnIfControlDcnMode": sleDcnIfControlDcnMode,
       "sleDcnIfControlGneOspfArea": sleDcnIfControlGneOspfArea,
       "sleDcnIfNotification": sleDcnIfNotification,
       "sleDcnIfModeChanged": sleDcnIfModeChanged,
       "sleDcnIfGneOspfAreaChanged": sleDcnIfGneOspfAreaChanged,
       "sleDcnObjectGroup": sleDcnObjectGroup,
       "sleDcnNotificationGroup": sleDcnNotificationGroup}
)
