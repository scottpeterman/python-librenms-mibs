# SNMP MIB module (SLE-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-BGP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:18 2025
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

sleBGP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53)
)
if mibBuilder.loadTexts:
    sleBGP.setRevisions(
        ("2010-03-21 19:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleBGPBase_ObjectIdentity = ObjectIdentity
sleBGPBase = _SleBGPBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1)
)
_SleBGPBaseInfo_ObjectIdentity = ObjectIdentity
sleBGPBaseInfo = _SleBGPBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 1)
)


class _SleBGPBaseAsNumber_Type(Gauge32):
    """Custom type sleBGPBaseAsNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleBGPBaseAsNumber_Type.__name__ = "Gauge32"
_SleBGPBaseAsNumber_Object = MibScalar
sleBGPBaseAsNumber = _SleBGPBaseAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 1, 1),
    _SleBGPBaseAsNumber_Type()
)
sleBGPBaseAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseAsNumber.setStatus("current")


class _SleBGPBaseConfigType_Type(Integer32):
    """Custom type sleBGPBaseConfigType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("zebos", 0),
          ("standard", 1))
    )


_SleBGPBaseConfigType_Type.__name__ = "Integer32"
_SleBGPBaseConfigType_Object = MibScalar
sleBGPBaseConfigType = _SleBGPBaseConfigType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 1, 2),
    _SleBGPBaseConfigType_Type()
)
sleBGPBaseConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseConfigType.setStatus("current")


class _SleBGPBaseRfc1771PathSelect_Type(Integer32):
    """Custom type sleBGPBaseRfc1771PathSelect based on Integer32"""
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


_SleBGPBaseRfc1771PathSelect_Type.__name__ = "Integer32"
_SleBGPBaseRfc1771PathSelect_Object = MibScalar
sleBGPBaseRfc1771PathSelect = _SleBGPBaseRfc1771PathSelect_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 1, 3),
    _SleBGPBaseRfc1771PathSelect_Type()
)
sleBGPBaseRfc1771PathSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseRfc1771PathSelect.setStatus("current")


class _SleBGPBaseRfc1771Strict_Type(Integer32):
    """Custom type sleBGPBaseRfc1771Strict based on Integer32"""
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


_SleBGPBaseRfc1771Strict_Type.__name__ = "Integer32"
_SleBGPBaseRfc1771Strict_Object = MibScalar
sleBGPBaseRfc1771Strict = _SleBGPBaseRfc1771Strict_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 1, 4),
    _SleBGPBaseRfc1771Strict_Type()
)
sleBGPBaseRfc1771Strict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseRfc1771Strict.setStatus("current")


class _SleBGPBaseAggregateNextHop_Type(Integer32):
    """Custom type sleBGPBaseAggregateNextHop based on Integer32"""
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


_SleBGPBaseAggregateNextHop_Type.__name__ = "Integer32"
_SleBGPBaseAggregateNextHop_Object = MibScalar
sleBGPBaseAggregateNextHop = _SleBGPBaseAggregateNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 1, 5),
    _SleBGPBaseAggregateNextHop_Type()
)
sleBGPBaseAggregateNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseAggregateNextHop.setStatus("current")


class _SleBGPBaseExtendAsnCap_Type(Integer32):
    """Custom type sleBGPBaseExtendAsnCap based on Integer32"""
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


_SleBGPBaseExtendAsnCap_Type.__name__ = "Integer32"
_SleBGPBaseExtendAsnCap_Object = MibScalar
sleBGPBaseExtendAsnCap = _SleBGPBaseExtendAsnCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 1, 6),
    _SleBGPBaseExtendAsnCap_Type()
)
sleBGPBaseExtendAsnCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseExtendAsnCap.setStatus("current")
_SleBGPBaseControl_ObjectIdentity = ObjectIdentity
sleBGPBaseControl = _SleBGPBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2)
)


class _SleBGPBaseControlRequest_Type(Integer32):
    """Custom type sleBGPBaseControlRequest based on Integer32"""
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
        *(("createBGPAsNumber", 1),
          ("deleteBGPAsNumber", 2),
          ("setBGPConfigType", 3),
          ("setBGPRfc1771PathSelect", 4),
          ("setBGPRfc1771Strict", 5),
          ("setAggregateNextHop", 6),
          ("setBGPExtendAsnCap", 7),
          ("clearBGPAll", 8),
          ("clearBGPAsNumber", 9),
          ("clearBGPPeer", 10),
          ("clearBGPDamp", 11),
          ("clearBGPExternal", 12),
          ("clearBGPView", 13))
    )


_SleBGPBaseControlRequest_Type.__name__ = "Integer32"
_SleBGPBaseControlRequest_Object = MibScalar
sleBGPBaseControlRequest = _SleBGPBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 1),
    _SleBGPBaseControlRequest_Type()
)
sleBGPBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPBaseControlRequest.setStatus("current")
_SleBGPBaseControlStatus_Type = SleControlStatusType
_SleBGPBaseControlStatus_Object = MibScalar
sleBGPBaseControlStatus = _SleBGPBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 2),
    _SleBGPBaseControlStatus_Type()
)
sleBGPBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlStatus.setStatus("current")
_SleBGPBaseControlTimer_Type = Gauge32
_SleBGPBaseControlTimer_Object = MibScalar
sleBGPBaseControlTimer = _SleBGPBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 3),
    _SleBGPBaseControlTimer_Type()
)
sleBGPBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPBaseControlTimer.setStatus("current")
_SleBGPBaseControlTimeStamp_Type = TimeTicks
_SleBGPBaseControlTimeStamp_Object = MibScalar
sleBGPBaseControlTimeStamp = _SleBGPBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 4),
    _SleBGPBaseControlTimeStamp_Type()
)
sleBGPBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlTimeStamp.setStatus("current")
_SleBGPBaseControlReqResult_Type = SleControlRequestResultType
_SleBGPBaseControlReqResult_Object = MibScalar
sleBGPBaseControlReqResult = _SleBGPBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 5),
    _SleBGPBaseControlReqResult_Type()
)
sleBGPBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlReqResult.setStatus("current")


class _SleBGPBaseControlAsNumber_Type(Gauge32):
    """Custom type sleBGPBaseControlAsNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPBaseControlAsNumber_Type.__name__ = "Gauge32"
_SleBGPBaseControlAsNumber_Object = MibScalar
sleBGPBaseControlAsNumber = _SleBGPBaseControlAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 6),
    _SleBGPBaseControlAsNumber_Type()
)
sleBGPBaseControlAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlAsNumber.setStatus("current")


class _SleBGPBaseControlConfigType_Type(Integer32):
    """Custom type sleBGPBaseControlConfigType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("zebos", 0),
          ("standard", 1))
    )


_SleBGPBaseControlConfigType_Type.__name__ = "Integer32"
_SleBGPBaseControlConfigType_Object = MibScalar
sleBGPBaseControlConfigType = _SleBGPBaseControlConfigType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 7),
    _SleBGPBaseControlConfigType_Type()
)
sleBGPBaseControlConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlConfigType.setStatus("current")


class _SleBGPBaseControlRfc1771PathSelect_Type(Integer32):
    """Custom type sleBGPBaseControlRfc1771PathSelect based on Integer32"""
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


_SleBGPBaseControlRfc1771PathSelect_Type.__name__ = "Integer32"
_SleBGPBaseControlRfc1771PathSelect_Object = MibScalar
sleBGPBaseControlRfc1771PathSelect = _SleBGPBaseControlRfc1771PathSelect_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 8),
    _SleBGPBaseControlRfc1771PathSelect_Type()
)
sleBGPBaseControlRfc1771PathSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlRfc1771PathSelect.setStatus("current")


class _SleBGPBaseControlRfc1771Strict_Type(Integer32):
    """Custom type sleBGPBaseControlRfc1771Strict based on Integer32"""
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


_SleBGPBaseControlRfc1771Strict_Type.__name__ = "Integer32"
_SleBGPBaseControlRfc1771Strict_Object = MibScalar
sleBGPBaseControlRfc1771Strict = _SleBGPBaseControlRfc1771Strict_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 9),
    _SleBGPBaseControlRfc1771Strict_Type()
)
sleBGPBaseControlRfc1771Strict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlRfc1771Strict.setStatus("current")


class _SleBGPBaseControlAggregateNextHop_Type(Integer32):
    """Custom type sleBGPBaseControlAggregateNextHop based on Integer32"""
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


_SleBGPBaseControlAggregateNextHop_Type.__name__ = "Integer32"
_SleBGPBaseControlAggregateNextHop_Object = MibScalar
sleBGPBaseControlAggregateNextHop = _SleBGPBaseControlAggregateNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 10),
    _SleBGPBaseControlAggregateNextHop_Type()
)
sleBGPBaseControlAggregateNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlAggregateNextHop.setStatus("current")


class _SleBGPBaseControlExtendAsnCap_Type(Integer32):
    """Custom type sleBGPBaseControlExtendAsnCap based on Integer32"""
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


_SleBGPBaseControlExtendAsnCap_Type.__name__ = "Integer32"
_SleBGPBaseControlExtendAsnCap_Object = MibScalar
sleBGPBaseControlExtendAsnCap = _SleBGPBaseControlExtendAsnCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 11),
    _SleBGPBaseControlExtendAsnCap_Type()
)
sleBGPBaseControlExtendAsnCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlExtendAsnCap.setStatus("current")


class _SleBGPBaseControlClearFamilyMode_Type(Integer32):
    """Custom type sleBGPBaseControlClearFamilyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPBaseControlClearFamilyMode_Type.__name__ = "Integer32"
_SleBGPBaseControlClearFamilyMode_Object = MibScalar
sleBGPBaseControlClearFamilyMode = _SleBGPBaseControlClearFamilyMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 12),
    _SleBGPBaseControlClearFamilyMode_Type()
)
sleBGPBaseControlClearFamilyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearFamilyMode.setStatus("current")


class _SleBGPBaseControlClearFamilyType_Type(Integer32):
    """Custom type sleBGPBaseControlClearFamilyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("vpnv4", 3))
    )


_SleBGPBaseControlClearFamilyType_Type.__name__ = "Integer32"
_SleBGPBaseControlClearFamilyType_Object = MibScalar
sleBGPBaseControlClearFamilyType = _SleBGPBaseControlClearFamilyType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 13),
    _SleBGPBaseControlClearFamilyType_Type()
)
sleBGPBaseControlClearFamilyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearFamilyType.setStatus("current")


class _SleBGPBaseControlClearDirection_Type(Integer32):
    """Custom type sleBGPBaseControlClearDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("in", 1),
          ("out", 2))
    )


_SleBGPBaseControlClearDirection_Type.__name__ = "Integer32"
_SleBGPBaseControlClearDirection_Object = MibScalar
sleBGPBaseControlClearDirection = _SleBGPBaseControlClearDirection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 14),
    _SleBGPBaseControlClearDirection_Type()
)
sleBGPBaseControlClearDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearDirection.setStatus("current")


class _SleBGPBaseControlClearSoft_Type(Integer32):
    """Custom type sleBGPBaseControlClearSoft based on Integer32"""
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


_SleBGPBaseControlClearSoft_Type.__name__ = "Integer32"
_SleBGPBaseControlClearSoft_Object = MibScalar
sleBGPBaseControlClearSoft = _SleBGPBaseControlClearSoft_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 15),
    _SleBGPBaseControlClearSoft_Type()
)
sleBGPBaseControlClearSoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearSoft.setStatus("current")


class _SleBGPBaseControlClearPrefixFilter_Type(Integer32):
    """Custom type sleBGPBaseControlClearPrefixFilter based on Integer32"""
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


_SleBGPBaseControlClearPrefixFilter_Type.__name__ = "Integer32"
_SleBGPBaseControlClearPrefixFilter_Object = MibScalar
sleBGPBaseControlClearPrefixFilter = _SleBGPBaseControlClearPrefixFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 16),
    _SleBGPBaseControlClearPrefixFilter_Type()
)
sleBGPBaseControlClearPrefixFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearPrefixFilter.setStatus("current")
_SleBGPBaseControlClearPeerName_Type = OctetString
_SleBGPBaseControlClearPeerName_Object = MibScalar
sleBGPBaseControlClearPeerName = _SleBGPBaseControlClearPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 17),
    _SleBGPBaseControlClearPeerName_Type()
)
sleBGPBaseControlClearPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearPeerName.setStatus("current")
_SleBGPBaseControlClearAddr_Type = OctetString
_SleBGPBaseControlClearAddr_Object = MibScalar
sleBGPBaseControlClearAddr = _SleBGPBaseControlClearAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 18),
    _SleBGPBaseControlClearAddr_Type()
)
sleBGPBaseControlClearAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearAddr.setStatus("current")
_SleBGPBaseControlClearViewName_Type = OctetString
_SleBGPBaseControlClearViewName_Object = MibScalar
sleBGPBaseControlClearViewName = _SleBGPBaseControlClearViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 19),
    _SleBGPBaseControlClearViewName_Type()
)
sleBGPBaseControlClearViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearViewName.setStatus("current")


class _SleBGPBaseControlClearDampFlag_Type(Integer32):
    """Custom type sleBGPBaseControlClearDampFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("damp", 1),
          ("flap", 2))
    )


_SleBGPBaseControlClearDampFlag_Type.__name__ = "Integer32"
_SleBGPBaseControlClearDampFlag_Object = MibScalar
sleBGPBaseControlClearDampFlag = _SleBGPBaseControlClearDampFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 2, 20),
    _SleBGPBaseControlClearDampFlag_Type()
)
sleBGPBaseControlClearDampFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPBaseControlClearDampFlag.setStatus("current")
_SleBGPBaseNotification_ObjectIdentity = ObjectIdentity
sleBGPBaseNotification = _SleBGPBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3)
)
_SleBGPInfo_ObjectIdentity = ObjectIdentity
sleBGPInfo = _SleBGPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2)
)
_SleBGPInfoValue_ObjectIdentity = ObjectIdentity
sleBGPInfoValue = _SleBGPInfoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1)
)
_SleBGPInfoRouterID_Type = IpAddress
_SleBGPInfoRouterID_Object = MibScalar
sleBGPInfoRouterID = _SleBGPInfoRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 1),
    _SleBGPInfoRouterID_Type()
)
sleBGPInfoRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoRouterID.setStatus("current")


class _SleBGPInfoLogNeighborChange_Type(Integer32):
    """Custom type sleBGPInfoLogNeighborChange based on Integer32"""
    defaultValue = 0

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


_SleBGPInfoLogNeighborChange_Type.__name__ = "Integer32"
_SleBGPInfoLogNeighborChange_Object = MibScalar
sleBGPInfoLogNeighborChange = _SleBGPInfoLogNeighborChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 2),
    _SleBGPInfoLogNeighborChange_Type()
)
sleBGPInfoLogNeighborChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoLogNeighborChange.setStatus("current")


class _SleBGPInfoAlwaysCompareMed_Type(Integer32):
    """Custom type sleBGPInfoAlwaysCompareMed based on Integer32"""
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


_SleBGPInfoAlwaysCompareMed_Type.__name__ = "Integer32"
_SleBGPInfoAlwaysCompareMed_Object = MibScalar
sleBGPInfoAlwaysCompareMed = _SleBGPInfoAlwaysCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 3),
    _SleBGPInfoAlwaysCompareMed_Type()
)
sleBGPInfoAlwaysCompareMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoAlwaysCompareMed.setStatus("current")


class _SleBGPInfoBestPathAsPathIgnore_Type(Integer32):
    """Custom type sleBGPInfoBestPathAsPathIgnore based on Integer32"""
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


_SleBGPInfoBestPathAsPathIgnore_Type.__name__ = "Integer32"
_SleBGPInfoBestPathAsPathIgnore_Object = MibScalar
sleBGPInfoBestPathAsPathIgnore = _SleBGPInfoBestPathAsPathIgnore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 4),
    _SleBGPInfoBestPathAsPathIgnore_Type()
)
sleBGPInfoBestPathAsPathIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoBestPathAsPathIgnore.setStatus("current")


class _SleBGPInfoBestPathCompareConfedAsPath_Type(Integer32):
    """Custom type sleBGPInfoBestPathCompareConfedAsPath based on Integer32"""
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


_SleBGPInfoBestPathCompareConfedAsPath_Type.__name__ = "Integer32"
_SleBGPInfoBestPathCompareConfedAsPath_Object = MibScalar
sleBGPInfoBestPathCompareConfedAsPath = _SleBGPInfoBestPathCompareConfedAsPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 5),
    _SleBGPInfoBestPathCompareConfedAsPath_Type()
)
sleBGPInfoBestPathCompareConfedAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareConfedAsPath.setStatus("current")


class _SleBGPInfoBestPathCompareRouterID_Type(Integer32):
    """Custom type sleBGPInfoBestPathCompareRouterID based on Integer32"""
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


_SleBGPInfoBestPathCompareRouterID_Type.__name__ = "Integer32"
_SleBGPInfoBestPathCompareRouterID_Object = MibScalar
sleBGPInfoBestPathCompareRouterID = _SleBGPInfoBestPathCompareRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 6),
    _SleBGPInfoBestPathCompareRouterID_Type()
)
sleBGPInfoBestPathCompareRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareRouterID.setStatus("current")


class _SleBGPInfoBestPathCompareMedConfed_Type(Integer32):
    """Custom type sleBGPInfoBestPathCompareMedConfed based on Integer32"""
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


_SleBGPInfoBestPathCompareMedConfed_Type.__name__ = "Integer32"
_SleBGPInfoBestPathCompareMedConfed_Object = MibScalar
sleBGPInfoBestPathCompareMedConfed = _SleBGPInfoBestPathCompareMedConfed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 7),
    _SleBGPInfoBestPathCompareMedConfed_Type()
)
sleBGPInfoBestPathCompareMedConfed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareMedConfed.setStatus("current")


class _SleBGPInfoBestPathCompareMedMisAsWorst_Type(Integer32):
    """Custom type sleBGPInfoBestPathCompareMedMisAsWorst based on Integer32"""
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


_SleBGPInfoBestPathCompareMedMisAsWorst_Type.__name__ = "Integer32"
_SleBGPInfoBestPathCompareMedMisAsWorst_Object = MibScalar
sleBGPInfoBestPathCompareMedMisAsWorst = _SleBGPInfoBestPathCompareMedMisAsWorst_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 8),
    _SleBGPInfoBestPathCompareMedMisAsWorst_Type()
)
sleBGPInfoBestPathCompareMedMisAsWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareMedMisAsWorst.setStatus("current")


class _SleBGPInfoClientToClient_Type(Integer32):
    """Custom type sleBGPInfoClientToClient based on Integer32"""
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


_SleBGPInfoClientToClient_Type.__name__ = "Integer32"
_SleBGPInfoClientToClient_Object = MibScalar
sleBGPInfoClientToClient = _SleBGPInfoClientToClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 9),
    _SleBGPInfoClientToClient_Type()
)
sleBGPInfoClientToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoClientToClient.setStatus("current")
_SleBGPInfoClusterID_Type = IpAddress
_SleBGPInfoClusterID_Object = MibScalar
sleBGPInfoClusterID = _SleBGPInfoClusterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 10),
    _SleBGPInfoClusterID_Type()
)
sleBGPInfoClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoClusterID.setStatus("current")


class _SleBGPInfoConfederationID_Type(Integer32):
    """Custom type sleBGPInfoConfederationID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPInfoConfederationID_Type.__name__ = "Integer32"
_SleBGPInfoConfederationID_Object = MibScalar
sleBGPInfoConfederationID = _SleBGPInfoConfederationID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 11),
    _SleBGPInfoConfederationID_Type()
)
sleBGPInfoConfederationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoConfederationID.setStatus("current")


class _SleBGPInfoDeterministicMed_Type(Integer32):
    """Custom type sleBGPInfoDeterministicMed based on Integer32"""
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


_SleBGPInfoDeterministicMed_Type.__name__ = "Integer32"
_SleBGPInfoDeterministicMed_Object = MibScalar
sleBGPInfoDeterministicMed = _SleBGPInfoDeterministicMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 12),
    _SleBGPInfoDeterministicMed_Type()
)
sleBGPInfoDeterministicMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoDeterministicMed.setStatus("current")


class _SleBGPInfoEnforceFirstAs_Type(Integer32):
    """Custom type sleBGPInfoEnforceFirstAs based on Integer32"""
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


_SleBGPInfoEnforceFirstAs_Type.__name__ = "Integer32"
_SleBGPInfoEnforceFirstAs_Object = MibScalar
sleBGPInfoEnforceFirstAs = _SleBGPInfoEnforceFirstAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 13),
    _SleBGPInfoEnforceFirstAs_Type()
)
sleBGPInfoEnforceFirstAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoEnforceFirstAs.setStatus("current")


class _SleBGPInfoFastExternalFailOver_Type(Integer32):
    """Custom type sleBGPInfoFastExternalFailOver based on Integer32"""
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


_SleBGPInfoFastExternalFailOver_Type.__name__ = "Integer32"
_SleBGPInfoFastExternalFailOver_Object = MibScalar
sleBGPInfoFastExternalFailOver = _SleBGPInfoFastExternalFailOver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 14),
    _SleBGPInfoFastExternalFailOver_Type()
)
sleBGPInfoFastExternalFailOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoFastExternalFailOver.setStatus("current")


class _SleBGPInfoGracefulRestartTime_Type(Integer32):
    """Custom type sleBGPInfoGracefulRestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SleBGPInfoGracefulRestartTime_Type.__name__ = "Integer32"
_SleBGPInfoGracefulRestartTime_Object = MibScalar
sleBGPInfoGracefulRestartTime = _SleBGPInfoGracefulRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 15),
    _SleBGPInfoGracefulRestartTime_Type()
)
sleBGPInfoGracefulRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoGracefulRestartTime.setStatus("current")


class _SleBGPInfoGracefulStalepathTime_Type(Integer32):
    """Custom type sleBGPInfoGracefulStalepathTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SleBGPInfoGracefulStalepathTime_Type.__name__ = "Integer32"
_SleBGPInfoGracefulStalepathTime_Object = MibScalar
sleBGPInfoGracefulStalepathTime = _SleBGPInfoGracefulStalepathTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 16),
    _SleBGPInfoGracefulStalepathTime_Type()
)
sleBGPInfoGracefulStalepathTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoGracefulStalepathTime.setStatus("current")


class _SleBGPInfoScanTime_Type(Integer32):
    """Custom type sleBGPInfoScanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SleBGPInfoScanTime_Type.__name__ = "Integer32"
_SleBGPInfoScanTime_Object = MibScalar
sleBGPInfoScanTime = _SleBGPInfoScanTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 17),
    _SleBGPInfoScanTime_Type()
)
sleBGPInfoScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoScanTime.setStatus("current")


class _SleBGPInfoNexthopTriggerStatus_Type(Integer32):
    """Custom type sleBGPInfoNexthopTriggerStatus based on Integer32"""
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


_SleBGPInfoNexthopTriggerStatus_Type.__name__ = "Integer32"
_SleBGPInfoNexthopTriggerStatus_Object = MibScalar
sleBGPInfoNexthopTriggerStatus = _SleBGPInfoNexthopTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 18),
    _SleBGPInfoNexthopTriggerStatus_Type()
)
sleBGPInfoNexthopTriggerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoNexthopTriggerStatus.setStatus("current")


class _SleBGPInfoNexthopTriggerDelay_Type(Integer32):
    """Custom type sleBGPInfoNexthopTriggerDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_SleBGPInfoNexthopTriggerDelay_Type.__name__ = "Integer32"
_SleBGPInfoNexthopTriggerDelay_Object = MibScalar
sleBGPInfoNexthopTriggerDelay = _SleBGPInfoNexthopTriggerDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 19),
    _SleBGPInfoNexthopTriggerDelay_Type()
)
sleBGPInfoNexthopTriggerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoNexthopTriggerDelay.setStatus("current")


class _SleBGPInfoSnmpNotification_Type(Integer32):
    """Custom type sleBGPInfoSnmpNotification based on Integer32"""
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


_SleBGPInfoSnmpNotification_Type.__name__ = "Integer32"
_SleBGPInfoSnmpNotification_Object = MibScalar
sleBGPInfoSnmpNotification = _SleBGPInfoSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 20),
    _SleBGPInfoSnmpNotification_Type()
)
sleBGPInfoSnmpNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoSnmpNotification.setStatus("current")


class _SleBGPInfoUpdateDelay_Type(Integer32):
    """Custom type sleBGPInfoUpdateDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SleBGPInfoUpdateDelay_Type.__name__ = "Integer32"
_SleBGPInfoUpdateDelay_Object = MibScalar
sleBGPInfoUpdateDelay = _SleBGPInfoUpdateDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 21),
    _SleBGPInfoUpdateDelay_Type()
)
sleBGPInfoUpdateDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoUpdateDelay.setStatus("current")


class _SleBGPInfoExternalRouteDistance_Type(Integer32):
    """Custom type sleBGPInfoExternalRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPInfoExternalRouteDistance_Type.__name__ = "Integer32"
_SleBGPInfoExternalRouteDistance_Object = MibScalar
sleBGPInfoExternalRouteDistance = _SleBGPInfoExternalRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 22),
    _SleBGPInfoExternalRouteDistance_Type()
)
sleBGPInfoExternalRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoExternalRouteDistance.setStatus("current")


class _SleBGPInfoInternalRouteDistance_Type(Integer32):
    """Custom type sleBGPInfoInternalRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPInfoInternalRouteDistance_Type.__name__ = "Integer32"
_SleBGPInfoInternalRouteDistance_Object = MibScalar
sleBGPInfoInternalRouteDistance = _SleBGPInfoInternalRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 23),
    _SleBGPInfoInternalRouteDistance_Type()
)
sleBGPInfoInternalRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoInternalRouteDistance.setStatus("current")


class _SleBGPInfoLocalRouteDistance_Type(Integer32):
    """Custom type sleBGPInfoLocalRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPInfoLocalRouteDistance_Type.__name__ = "Integer32"
_SleBGPInfoLocalRouteDistance_Object = MibScalar
sleBGPInfoLocalRouteDistance = _SleBGPInfoLocalRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 24),
    _SleBGPInfoLocalRouteDistance_Type()
)
sleBGPInfoLocalRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoLocalRouteDistance.setStatus("current")


class _SleBGPInfoMaximumPath_Type(Integer32):
    """Custom type sleBGPInfoMaximumPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleBGPInfoMaximumPath_Type.__name__ = "Integer32"
_SleBGPInfoMaximumPath_Object = MibScalar
sleBGPInfoMaximumPath = _SleBGPInfoMaximumPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 25),
    _SleBGPInfoMaximumPath_Type()
)
sleBGPInfoMaximumPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoMaximumPath.setStatus("current")


class _SleBGPInfoMaximumPathIBGP_Type(Integer32):
    """Custom type sleBGPInfoMaximumPathIBGP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleBGPInfoMaximumPathIBGP_Type.__name__ = "Integer32"
_SleBGPInfoMaximumPathIBGP_Object = MibScalar
sleBGPInfoMaximumPathIBGP = _SleBGPInfoMaximumPathIBGP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 26),
    _SleBGPInfoMaximumPathIBGP_Type()
)
sleBGPInfoMaximumPathIBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoMaximumPathIBGP.setStatus("current")


class _SleBGPInfoKeepAliveInterval_Type(Integer32):
    """Custom type sleBGPInfoKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPInfoKeepAliveInterval_Type.__name__ = "Integer32"
_SleBGPInfoKeepAliveInterval_Object = MibScalar
sleBGPInfoKeepAliveInterval = _SleBGPInfoKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 27),
    _SleBGPInfoKeepAliveInterval_Type()
)
sleBGPInfoKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoKeepAliveInterval.setStatus("current")


class _SleBGPInfoHoldTime_Type(Integer32):
    """Custom type sleBGPInfoHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPInfoHoldTime_Type.__name__ = "Integer32"
_SleBGPInfoHoldTime_Object = MibScalar
sleBGPInfoHoldTime = _SleBGPInfoHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 1, 28),
    _SleBGPInfoHoldTime_Type()
)
sleBGPInfoHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoHoldTime.setStatus("current")
_SleBGPInfoControl_ObjectIdentity = ObjectIdentity
sleBGPInfoControl = _SleBGPInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2)
)


class _SleBGPInfoControlRequest_Type(Integer32):
    """Custom type sleBGPInfoControlRequest based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("createBGPRouterID", 1),
          ("deleteBGPRouterID", 2),
          ("setBGPLogNeighbor", 3),
          ("setBGPAlwaysCompareMed", 4),
          ("setBGPBestPathAsPathIgnore", 5),
          ("setBGPBestPathCompareConfedAsPath", 6),
          ("setBGPBestPathCompareRouterID", 7),
          ("setBGPBestPathCompareMedConfed", 8),
          ("setBGPBestPathCompareMedMisAsWorst", 9),
          ("setBGPClientToClient", 10),
          ("createBGPClusterID", 11),
          ("deleteBGPClusterID", 12),
          ("setBGPConfederationID", 13),
          ("setBGPDeterministicMed", 14),
          ("setBGPEnforceFirstAs", 15),
          ("setBGPFastExternalFailOver", 16),
          ("setBGPGracefulRestartProfile", 17),
          ("setBGPScanTime", 18),
          ("setBGPNexthopTriggerStatus", 19),
          ("setBGPNexthopTriggerInterval", 20),
          ("setBGPSnmpNotification", 21),
          ("setBGPUpdateDelay", 22),
          ("createBGPDistanceProfile", 23),
          ("deleteBGPDistanceProfile", 24),
          ("setBGPMaximumPath", 25),
          ("setBGPMaximumPathIBGP", 26),
          ("setBGPTimersProfile", 27))
    )


_SleBGPInfoControlRequest_Type.__name__ = "Integer32"
_SleBGPInfoControlRequest_Object = MibScalar
sleBGPInfoControlRequest = _SleBGPInfoControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 1),
    _SleBGPInfoControlRequest_Type()
)
sleBGPInfoControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPInfoControlRequest.setStatus("current")
_SleBGPInfoControlStatus_Type = SleControlStatusType
_SleBGPInfoControlStatus_Object = MibScalar
sleBGPInfoControlStatus = _SleBGPInfoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 2),
    _SleBGPInfoControlStatus_Type()
)
sleBGPInfoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlStatus.setStatus("current")
_SleBGPInfoControlTimer_Type = Gauge32
_SleBGPInfoControlTimer_Object = MibScalar
sleBGPInfoControlTimer = _SleBGPInfoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 3),
    _SleBGPInfoControlTimer_Type()
)
sleBGPInfoControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPInfoControlTimer.setStatus("current")
_SleBGPInfoControlTimeStamp_Type = TimeTicks
_SleBGPInfoControlTimeStamp_Object = MibScalar
sleBGPInfoControlTimeStamp = _SleBGPInfoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 4),
    _SleBGPInfoControlTimeStamp_Type()
)
sleBGPInfoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlTimeStamp.setStatus("current")
_SleBGPInfoControlReqResult_Type = SleControlRequestResultType
_SleBGPInfoControlReqResult_Object = MibScalar
sleBGPInfoControlReqResult = _SleBGPInfoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 5),
    _SleBGPInfoControlReqResult_Type()
)
sleBGPInfoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlReqResult.setStatus("current")
_SleBGPInfoControlRouterID_Type = IpAddress
_SleBGPInfoControlRouterID_Object = MibScalar
sleBGPInfoControlRouterID = _SleBGPInfoControlRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 6),
    _SleBGPInfoControlRouterID_Type()
)
sleBGPInfoControlRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlRouterID.setStatus("current")


class _SleBGPInfoControlLogNeighborChange_Type(Integer32):
    """Custom type sleBGPInfoControlLogNeighborChange based on Integer32"""
    defaultValue = 0

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


_SleBGPInfoControlLogNeighborChange_Type.__name__ = "Integer32"
_SleBGPInfoControlLogNeighborChange_Object = MibScalar
sleBGPInfoControlLogNeighborChange = _SleBGPInfoControlLogNeighborChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 7),
    _SleBGPInfoControlLogNeighborChange_Type()
)
sleBGPInfoControlLogNeighborChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlLogNeighborChange.setStatus("current")


class _SleBGPInfoControlAlwaysCompareMed_Type(Integer32):
    """Custom type sleBGPInfoControlAlwaysCompareMed based on Integer32"""
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


_SleBGPInfoControlAlwaysCompareMed_Type.__name__ = "Integer32"
_SleBGPInfoControlAlwaysCompareMed_Object = MibScalar
sleBGPInfoControlAlwaysCompareMed = _SleBGPInfoControlAlwaysCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 8),
    _SleBGPInfoControlAlwaysCompareMed_Type()
)
sleBGPInfoControlAlwaysCompareMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlAlwaysCompareMed.setStatus("current")


class _SleBGPInfoControlBestPathAsPathIgnore_Type(Integer32):
    """Custom type sleBGPInfoControlBestPathAsPathIgnore based on Integer32"""
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


_SleBGPInfoControlBestPathAsPathIgnore_Type.__name__ = "Integer32"
_SleBGPInfoControlBestPathAsPathIgnore_Object = MibScalar
sleBGPInfoControlBestPathAsPathIgnore = _SleBGPInfoControlBestPathAsPathIgnore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 9),
    _SleBGPInfoControlBestPathAsPathIgnore_Type()
)
sleBGPInfoControlBestPathAsPathIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlBestPathAsPathIgnore.setStatus("current")


class _SleBGPInfoControlBestPathCompareConfedAsPath_Type(Integer32):
    """Custom type sleBGPInfoControlBestPathCompareConfedAsPath based on Integer32"""
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


_SleBGPInfoControlBestPathCompareConfedAsPath_Type.__name__ = "Integer32"
_SleBGPInfoControlBestPathCompareConfedAsPath_Object = MibScalar
sleBGPInfoControlBestPathCompareConfedAsPath = _SleBGPInfoControlBestPathCompareConfedAsPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 10),
    _SleBGPInfoControlBestPathCompareConfedAsPath_Type()
)
sleBGPInfoControlBestPathCompareConfedAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlBestPathCompareConfedAsPath.setStatus("current")


class _SleBGPInfoControlBestPathCompareRouterID_Type(Integer32):
    """Custom type sleBGPInfoControlBestPathCompareRouterID based on Integer32"""
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


_SleBGPInfoControlBestPathCompareRouterID_Type.__name__ = "Integer32"
_SleBGPInfoControlBestPathCompareRouterID_Object = MibScalar
sleBGPInfoControlBestPathCompareRouterID = _SleBGPInfoControlBestPathCompareRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 11),
    _SleBGPInfoControlBestPathCompareRouterID_Type()
)
sleBGPInfoControlBestPathCompareRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlBestPathCompareRouterID.setStatus("current")


class _SleBGPInfoControlBestPathCompareMedConfed_Type(Integer32):
    """Custom type sleBGPInfoControlBestPathCompareMedConfed based on Integer32"""
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


_SleBGPInfoControlBestPathCompareMedConfed_Type.__name__ = "Integer32"
_SleBGPInfoControlBestPathCompareMedConfed_Object = MibScalar
sleBGPInfoControlBestPathCompareMedConfed = _SleBGPInfoControlBestPathCompareMedConfed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 12),
    _SleBGPInfoControlBestPathCompareMedConfed_Type()
)
sleBGPInfoControlBestPathCompareMedConfed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlBestPathCompareMedConfed.setStatus("current")


class _SleBGPInfoControlBestPathCompareMedMisAsWorst_Type(Integer32):
    """Custom type sleBGPInfoControlBestPathCompareMedMisAsWorst based on Integer32"""
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


_SleBGPInfoControlBestPathCompareMedMisAsWorst_Type.__name__ = "Integer32"
_SleBGPInfoControlBestPathCompareMedMisAsWorst_Object = MibScalar
sleBGPInfoControlBestPathCompareMedMisAsWorst = _SleBGPInfoControlBestPathCompareMedMisAsWorst_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 13),
    _SleBGPInfoControlBestPathCompareMedMisAsWorst_Type()
)
sleBGPInfoControlBestPathCompareMedMisAsWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlBestPathCompareMedMisAsWorst.setStatus("current")


class _SleBGPInfoControlClientToClient_Type(Integer32):
    """Custom type sleBGPInfoControlClientToClient based on Integer32"""
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


_SleBGPInfoControlClientToClient_Type.__name__ = "Integer32"
_SleBGPInfoControlClientToClient_Object = MibScalar
sleBGPInfoControlClientToClient = _SleBGPInfoControlClientToClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 14),
    _SleBGPInfoControlClientToClient_Type()
)
sleBGPInfoControlClientToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlClientToClient.setStatus("current")
_SleBGPInfoControlClusterID_Type = IpAddress
_SleBGPInfoControlClusterID_Object = MibScalar
sleBGPInfoControlClusterID = _SleBGPInfoControlClusterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 15),
    _SleBGPInfoControlClusterID_Type()
)
sleBGPInfoControlClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlClusterID.setStatus("current")


class _SleBGPInfoControlConfederationID_Type(Integer32):
    """Custom type sleBGPInfoControlConfederationID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPInfoControlConfederationID_Type.__name__ = "Integer32"
_SleBGPInfoControlConfederationID_Object = MibScalar
sleBGPInfoControlConfederationID = _SleBGPInfoControlConfederationID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 16),
    _SleBGPInfoControlConfederationID_Type()
)
sleBGPInfoControlConfederationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlConfederationID.setStatus("current")


class _SleBGPInfoControlDeterministicMed_Type(Integer32):
    """Custom type sleBGPInfoControlDeterministicMed based on Integer32"""
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


_SleBGPInfoControlDeterministicMed_Type.__name__ = "Integer32"
_SleBGPInfoControlDeterministicMed_Object = MibScalar
sleBGPInfoControlDeterministicMed = _SleBGPInfoControlDeterministicMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 17),
    _SleBGPInfoControlDeterministicMed_Type()
)
sleBGPInfoControlDeterministicMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlDeterministicMed.setStatus("current")


class _SleBGPInfoControlEnforceFirstAs_Type(Integer32):
    """Custom type sleBGPInfoControlEnforceFirstAs based on Integer32"""
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


_SleBGPInfoControlEnforceFirstAs_Type.__name__ = "Integer32"
_SleBGPInfoControlEnforceFirstAs_Object = MibScalar
sleBGPInfoControlEnforceFirstAs = _SleBGPInfoControlEnforceFirstAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 18),
    _SleBGPInfoControlEnforceFirstAs_Type()
)
sleBGPInfoControlEnforceFirstAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlEnforceFirstAs.setStatus("current")


class _SleBGPInfoControlFastExternalFailOver_Type(Integer32):
    """Custom type sleBGPInfoControlFastExternalFailOver based on Integer32"""
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


_SleBGPInfoControlFastExternalFailOver_Type.__name__ = "Integer32"
_SleBGPInfoControlFastExternalFailOver_Object = MibScalar
sleBGPInfoControlFastExternalFailOver = _SleBGPInfoControlFastExternalFailOver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 19),
    _SleBGPInfoControlFastExternalFailOver_Type()
)
sleBGPInfoControlFastExternalFailOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlFastExternalFailOver.setStatus("current")


class _SleBGPInfoControlGracefulRestartTime_Type(Integer32):
    """Custom type sleBGPInfoControlGracefulRestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SleBGPInfoControlGracefulRestartTime_Type.__name__ = "Integer32"
_SleBGPInfoControlGracefulRestartTime_Object = MibScalar
sleBGPInfoControlGracefulRestartTime = _SleBGPInfoControlGracefulRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 20),
    _SleBGPInfoControlGracefulRestartTime_Type()
)
sleBGPInfoControlGracefulRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlGracefulRestartTime.setStatus("current")


class _SleBGPInfoControlGracefulStalepathTime_Type(Integer32):
    """Custom type sleBGPInfoControlGracefulStalepathTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SleBGPInfoControlGracefulStalepathTime_Type.__name__ = "Integer32"
_SleBGPInfoControlGracefulStalepathTime_Object = MibScalar
sleBGPInfoControlGracefulStalepathTime = _SleBGPInfoControlGracefulStalepathTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 21),
    _SleBGPInfoControlGracefulStalepathTime_Type()
)
sleBGPInfoControlGracefulStalepathTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlGracefulStalepathTime.setStatus("current")


class _SleBGPInfoControlScanTime_Type(Integer32):
    """Custom type sleBGPInfoControlScanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SleBGPInfoControlScanTime_Type.__name__ = "Integer32"
_SleBGPInfoControlScanTime_Object = MibScalar
sleBGPInfoControlScanTime = _SleBGPInfoControlScanTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 22),
    _SleBGPInfoControlScanTime_Type()
)
sleBGPInfoControlScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlScanTime.setStatus("current")


class _SleBGPInfoControlNexthopTriggerStatus_Type(Integer32):
    """Custom type sleBGPInfoControlNexthopTriggerStatus based on Integer32"""
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


_SleBGPInfoControlNexthopTriggerStatus_Type.__name__ = "Integer32"
_SleBGPInfoControlNexthopTriggerStatus_Object = MibScalar
sleBGPInfoControlNexthopTriggerStatus = _SleBGPInfoControlNexthopTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 23),
    _SleBGPInfoControlNexthopTriggerStatus_Type()
)
sleBGPInfoControlNexthopTriggerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlNexthopTriggerStatus.setStatus("current")


class _SleBGPInfoControlNexthopTriggerDelay_Type(Integer32):
    """Custom type sleBGPInfoControlNexthopTriggerDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_SleBGPInfoControlNexthopTriggerDelay_Type.__name__ = "Integer32"
_SleBGPInfoControlNexthopTriggerDelay_Object = MibScalar
sleBGPInfoControlNexthopTriggerDelay = _SleBGPInfoControlNexthopTriggerDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 24),
    _SleBGPInfoControlNexthopTriggerDelay_Type()
)
sleBGPInfoControlNexthopTriggerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlNexthopTriggerDelay.setStatus("current")


class _SleBGPInfoControlSnmpNotification_Type(Integer32):
    """Custom type sleBGPInfoControlSnmpNotification based on Integer32"""
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


_SleBGPInfoControlSnmpNotification_Type.__name__ = "Integer32"
_SleBGPInfoControlSnmpNotification_Object = MibScalar
sleBGPInfoControlSnmpNotification = _SleBGPInfoControlSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 25),
    _SleBGPInfoControlSnmpNotification_Type()
)
sleBGPInfoControlSnmpNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlSnmpNotification.setStatus("current")


class _SleBGPInfoControlUpdateDelay_Type(Integer32):
    """Custom type sleBGPInfoControlUpdateDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SleBGPInfoControlUpdateDelay_Type.__name__ = "Integer32"
_SleBGPInfoControlUpdateDelay_Object = MibScalar
sleBGPInfoControlUpdateDelay = _SleBGPInfoControlUpdateDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 26),
    _SleBGPInfoControlUpdateDelay_Type()
)
sleBGPInfoControlUpdateDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlUpdateDelay.setStatus("current")


class _SleBGPInfoControlExternalRouteDistance_Type(Integer32):
    """Custom type sleBGPInfoControlExternalRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPInfoControlExternalRouteDistance_Type.__name__ = "Integer32"
_SleBGPInfoControlExternalRouteDistance_Object = MibScalar
sleBGPInfoControlExternalRouteDistance = _SleBGPInfoControlExternalRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 27),
    _SleBGPInfoControlExternalRouteDistance_Type()
)
sleBGPInfoControlExternalRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlExternalRouteDistance.setStatus("current")


class _SleBGPInfoControlInternalRouteDistance_Type(Integer32):
    """Custom type sleBGPInfoControlInternalRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPInfoControlInternalRouteDistance_Type.__name__ = "Integer32"
_SleBGPInfoControlInternalRouteDistance_Object = MibScalar
sleBGPInfoControlInternalRouteDistance = _SleBGPInfoControlInternalRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 28),
    _SleBGPInfoControlInternalRouteDistance_Type()
)
sleBGPInfoControlInternalRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlInternalRouteDistance.setStatus("current")


class _SleBGPInfoControlLocalRouteDistance_Type(Integer32):
    """Custom type sleBGPInfoControlLocalRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPInfoControlLocalRouteDistance_Type.__name__ = "Integer32"
_SleBGPInfoControlLocalRouteDistance_Object = MibScalar
sleBGPInfoControlLocalRouteDistance = _SleBGPInfoControlLocalRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 29),
    _SleBGPInfoControlLocalRouteDistance_Type()
)
sleBGPInfoControlLocalRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlLocalRouteDistance.setStatus("current")


class _SleBGPInfoControlMaximumPath_Type(Integer32):
    """Custom type sleBGPInfoControlMaximumPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleBGPInfoControlMaximumPath_Type.__name__ = "Integer32"
_SleBGPInfoControlMaximumPath_Object = MibScalar
sleBGPInfoControlMaximumPath = _SleBGPInfoControlMaximumPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 30),
    _SleBGPInfoControlMaximumPath_Type()
)
sleBGPInfoControlMaximumPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlMaximumPath.setStatus("current")


class _SleBGPInfoControlMaximumPathIBGP_Type(Integer32):
    """Custom type sleBGPInfoControlMaximumPathIBGP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleBGPInfoControlMaximumPathIBGP_Type.__name__ = "Integer32"
_SleBGPInfoControlMaximumPathIBGP_Object = MibScalar
sleBGPInfoControlMaximumPathIBGP = _SleBGPInfoControlMaximumPathIBGP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 31),
    _SleBGPInfoControlMaximumPathIBGP_Type()
)
sleBGPInfoControlMaximumPathIBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlMaximumPathIBGP.setStatus("current")


class _SleBGPInfoControlKeepAliveInterval_Type(Integer32):
    """Custom type sleBGPInfoControlKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPInfoControlKeepAliveInterval_Type.__name__ = "Integer32"
_SleBGPInfoControlKeepAliveInterval_Object = MibScalar
sleBGPInfoControlKeepAliveInterval = _SleBGPInfoControlKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 32),
    _SleBGPInfoControlKeepAliveInterval_Type()
)
sleBGPInfoControlKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlKeepAliveInterval.setStatus("current")


class _SleBGPInfoControlHoldTime_Type(Integer32):
    """Custom type sleBGPInfoControlHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPInfoControlHoldTime_Type.__name__ = "Integer32"
_SleBGPInfoControlHoldTime_Object = MibScalar
sleBGPInfoControlHoldTime = _SleBGPInfoControlHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 2, 33),
    _SleBGPInfoControlHoldTime_Type()
)
sleBGPInfoControlHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPInfoControlHoldTime.setStatus("current")
_SleBGPInfoNotification_ObjectIdentity = ObjectIdentity
sleBGPInfoNotification = _SleBGPInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3)
)
_SleBGPAdminDistance_ObjectIdentity = ObjectIdentity
sleBGPAdminDistance = _SleBGPAdminDistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3)
)
_SleBGPAdminDistanceTable_Object = MibTable
sleBGPAdminDistanceTable = _SleBGPAdminDistanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 1)
)
if mibBuilder.loadTexts:
    sleBGPAdminDistanceTable.setStatus("current")
_SleBGPAdminDistanceEntry_Object = MibTableRow
sleBGPAdminDistanceEntry = _SleBGPAdminDistanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 1, 1)
)
sleBGPAdminDistanceEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPAdminDistanceAddrPrefix"),
)
if mibBuilder.loadTexts:
    sleBGPAdminDistanceEntry.setStatus("current")
_SleBGPAdminDistanceAddrPrefix_Type = OctetString
_SleBGPAdminDistanceAddrPrefix_Object = MibTableColumn
sleBGPAdminDistanceAddrPrefix = _SleBGPAdminDistanceAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 1, 1, 1),
    _SleBGPAdminDistanceAddrPrefix_Type()
)
sleBGPAdminDistanceAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceAddrPrefix.setStatus("current")


class _SleBGPAdminDistanceValue_Type(Integer32):
    """Custom type sleBGPAdminDistanceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleBGPAdminDistanceValue_Type.__name__ = "Integer32"
_SleBGPAdminDistanceValue_Object = MibTableColumn
sleBGPAdminDistanceValue = _SleBGPAdminDistanceValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 1, 1, 2),
    _SleBGPAdminDistanceValue_Type()
)
sleBGPAdminDistanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceValue.setStatus("current")


class _SleBGPAdminDistanceAccName_Type(OctetString):
    """Custom type sleBGPAdminDistanceAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAdminDistanceAccName_Type.__name__ = "OctetString"
_SleBGPAdminDistanceAccName_Object = MibTableColumn
sleBGPAdminDistanceAccName = _SleBGPAdminDistanceAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 1, 1, 3),
    _SleBGPAdminDistanceAccName_Type()
)
sleBGPAdminDistanceAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceAccName.setStatus("current")
_SleBGPAdminDistanceControl_ObjectIdentity = ObjectIdentity
sleBGPAdminDistanceControl = _SleBGPAdminDistanceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2)
)


class _SleBGPAdminDistanceControlRequest_Type(Integer32):
    """Custom type sleBGPAdminDistanceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createBGPAdminDistance", 1),
          ("deleteBGPAdminDistance", 2))
    )


_SleBGPAdminDistanceControlRequest_Type.__name__ = "Integer32"
_SleBGPAdminDistanceControlRequest_Object = MibScalar
sleBGPAdminDistanceControlRequest = _SleBGPAdminDistanceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 1),
    _SleBGPAdminDistanceControlRequest_Type()
)
sleBGPAdminDistanceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlRequest.setStatus("current")
_SleBGPAdminDistanceControlStatus_Type = SleControlStatusType
_SleBGPAdminDistanceControlStatus_Object = MibScalar
sleBGPAdminDistanceControlStatus = _SleBGPAdminDistanceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 2),
    _SleBGPAdminDistanceControlStatus_Type()
)
sleBGPAdminDistanceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlStatus.setStatus("current")
_SleBGPAdminDistanceControlTimer_Type = Gauge32
_SleBGPAdminDistanceControlTimer_Object = MibScalar
sleBGPAdminDistanceControlTimer = _SleBGPAdminDistanceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 3),
    _SleBGPAdminDistanceControlTimer_Type()
)
sleBGPAdminDistanceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlTimer.setStatus("current")
_SleBGPAdminDistanceControlTimeStamp_Type = TimeTicks
_SleBGPAdminDistanceControlTimeStamp_Object = MibScalar
sleBGPAdminDistanceControlTimeStamp = _SleBGPAdminDistanceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 4),
    _SleBGPAdminDistanceControlTimeStamp_Type()
)
sleBGPAdminDistanceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlTimeStamp.setStatus("current")
_SleBGPAdminDistanceControlReqResult_Type = SleControlRequestResultType
_SleBGPAdminDistanceControlReqResult_Object = MibScalar
sleBGPAdminDistanceControlReqResult = _SleBGPAdminDistanceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 5),
    _SleBGPAdminDistanceControlReqResult_Type()
)
sleBGPAdminDistanceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlReqResult.setStatus("current")
_SleBGPAdminDistanceControlAddrPrefix_Type = OctetString
_SleBGPAdminDistanceControlAddrPrefix_Object = MibScalar
sleBGPAdminDistanceControlAddrPrefix = _SleBGPAdminDistanceControlAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 6),
    _SleBGPAdminDistanceControlAddrPrefix_Type()
)
sleBGPAdminDistanceControlAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlAddrPrefix.setStatus("current")


class _SleBGPAdminDistanceControlValue_Type(Integer32):
    """Custom type sleBGPAdminDistanceControlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleBGPAdminDistanceControlValue_Type.__name__ = "Integer32"
_SleBGPAdminDistanceControlValue_Object = MibScalar
sleBGPAdminDistanceControlValue = _SleBGPAdminDistanceControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 7),
    _SleBGPAdminDistanceControlValue_Type()
)
sleBGPAdminDistanceControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlValue.setStatus("current")


class _SleBGPAdminDistanceControlAccName_Type(OctetString):
    """Custom type sleBGPAdminDistanceControlAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAdminDistanceControlAccName_Type.__name__ = "OctetString"
_SleBGPAdminDistanceControlAccName_Object = MibScalar
sleBGPAdminDistanceControlAccName = _SleBGPAdminDistanceControlAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 2, 8),
    _SleBGPAdminDistanceControlAccName_Type()
)
sleBGPAdminDistanceControlAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAdminDistanceControlAccName.setStatus("current")
_SleBGPAdminDistanceNotification_ObjectIdentity = ObjectIdentity
sleBGPAdminDistanceNotification = _SleBGPAdminDistanceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 3)
)
_SleBGPPeerInfo_ObjectIdentity = ObjectIdentity
sleBGPPeerInfo = _SleBGPPeerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4)
)
_SleBGPPeer_ObjectIdentity = ObjectIdentity
sleBGPPeer = _SleBGPPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1)
)
_SleBGPPeerTable_Object = MibTable
sleBGPPeerTable = _SleBGPPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleBGPPeerTable.setStatus("current")
_SleBGPPeerEntry_Object = MibTableRow
sleBGPPeerEntry = _SleBGPPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1)
)
sleBGPPeerEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPPeerName"),
)
if mibBuilder.loadTexts:
    sleBGPPeerEntry.setStatus("current")


class _SleBGPPeerName_Type(OctetString):
    """Custom type sleBGPPeerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPPeerName_Type.__name__ = "OctetString"
_SleBGPPeerName_Object = MibTableColumn
sleBGPPeerName = _SleBGPPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 1),
    _SleBGPPeerName_Type()
)
sleBGPPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerName.setStatus("current")


class _SleBGPPeerAsNum_Type(Gauge32):
    """Custom type sleBGPPeerAsNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPPeerAsNum_Type.__name__ = "Gauge32"
_SleBGPPeerAsNum_Object = MibTableColumn
sleBGPPeerAsNum = _SleBGPPeerAsNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 2),
    _SleBGPPeerAsNum_Type()
)
sleBGPPeerAsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerAsNum.setStatus("current")


class _SleBGPPeerGroupName_Type(OctetString):
    """Custom type sleBGPPeerGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerGroupName_Type.__name__ = "OctetString"
_SleBGPPeerGroupName_Object = MibTableColumn
sleBGPPeerGroupName = _SleBGPPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 3),
    _SleBGPPeerGroupName_Type()
)
sleBGPPeerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupName.setStatus("current")


class _SleBGPPeerAdvInterval_Type(Integer32):
    """Custom type sleBGPPeerAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerAdvInterval_Type.__name__ = "Integer32"
_SleBGPPeerAdvInterval_Object = MibTableColumn
sleBGPPeerAdvInterval = _SleBGPPeerAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 4),
    _SleBGPPeerAdvInterval_Type()
)
sleBGPPeerAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerAdvInterval.setStatus("current")


class _SleBGPPeerAsOriInterval_Type(Integer32):
    """Custom type sleBGPPeerAsOriInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerAsOriInterval_Type.__name__ = "Integer32"
_SleBGPPeerAsOriInterval_Object = MibTableColumn
sleBGPPeerAsOriInterval = _SleBGPPeerAsOriInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 5),
    _SleBGPPeerAsOriInterval_Type()
)
sleBGPPeerAsOriInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerAsOriInterval.setStatus("current")


class _SleBGPPeerDesc_Type(OctetString):
    """Custom type sleBGPPeerDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerDesc_Type.__name__ = "OctetString"
_SleBGPPeerDesc_Object = MibTableColumn
sleBGPPeerDesc = _SleBGPPeerDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 6),
    _SleBGPPeerDesc_Type()
)
sleBGPPeerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerDesc.setStatus("current")


class _SleBGPPeerDontCapNego_Type(Integer32):
    """Custom type sleBGPPeerDontCapNego based on Integer32"""
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


_SleBGPPeerDontCapNego_Type.__name__ = "Integer32"
_SleBGPPeerDontCapNego_Object = MibTableColumn
sleBGPPeerDontCapNego = _SleBGPPeerDontCapNego_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 7),
    _SleBGPPeerDontCapNego_Type()
)
sleBGPPeerDontCapNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerDontCapNego.setStatus("current")


class _SleBGPPeerWeight_Type(Integer32):
    """Custom type sleBGPPeerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerWeight_Type.__name__ = "Integer32"
_SleBGPPeerWeight_Object = MibTableColumn
sleBGPPeerWeight = _SleBGPPeerWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 8),
    _SleBGPPeerWeight_Type()
)
sleBGPPeerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerWeight.setStatus("current")


class _SleBGPPeerEnforcMultiHop_Type(Integer32):
    """Custom type sleBGPPeerEnforcMultiHop based on Integer32"""
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


_SleBGPPeerEnforcMultiHop_Type.__name__ = "Integer32"
_SleBGPPeerEnforcMultiHop_Object = MibTableColumn
sleBGPPeerEnforcMultiHop = _SleBGPPeerEnforcMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 9),
    _SleBGPPeerEnforcMultiHop_Type()
)
sleBGPPeerEnforcMultiHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerEnforcMultiHop.setStatus("current")


class _SleBGPPeerPassive_Type(Integer32):
    """Custom type sleBGPPeerPassive based on Integer32"""
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


_SleBGPPeerPassive_Type.__name__ = "Integer32"
_SleBGPPeerPassive_Object = MibTableColumn
sleBGPPeerPassive = _SleBGPPeerPassive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 10),
    _SleBGPPeerPassive_Type()
)
sleBGPPeerPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerPassive.setStatus("current")
_SleBGPPeerUpSourceName_Type = OctetString
_SleBGPPeerUpSourceName_Object = MibTableColumn
sleBGPPeerUpSourceName = _SleBGPPeerUpSourceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 11),
    _SleBGPPeerUpSourceName_Type()
)
sleBGPPeerUpSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerUpSourceName.setStatus("current")


class _SleBGPPeerPort_Type(Integer32):
    """Custom type sleBGPPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerPort_Type.__name__ = "Integer32"
_SleBGPPeerPort_Object = MibTableColumn
sleBGPPeerPort = _SleBGPPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 12),
    _SleBGPPeerPort_Type()
)
sleBGPPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerPort.setStatus("current")


class _SleBGPPeerRetstartTime_Type(Integer32):
    """Custom type sleBGPPeerRetstartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPPeerRetstartTime_Type.__name__ = "Integer32"
_SleBGPPeerRetstartTime_Object = MibTableColumn
sleBGPPeerRetstartTime = _SleBGPPeerRetstartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 13),
    _SleBGPPeerRetstartTime_Type()
)
sleBGPPeerRetstartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerRetstartTime.setStatus("current")


class _SleBGPPeerShutDown_Type(Integer32):
    """Custom type sleBGPPeerShutDown based on Integer32"""
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


_SleBGPPeerShutDown_Type.__name__ = "Integer32"
_SleBGPPeerShutDown_Object = MibTableColumn
sleBGPPeerShutDown = _SleBGPPeerShutDown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 14),
    _SleBGPPeerShutDown_Type()
)
sleBGPPeerShutDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerShutDown.setStatus("current")


class _SleBGPPeerKeepInterval_Type(Integer32):
    """Custom type sleBGPPeerKeepInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerKeepInterval_Type.__name__ = "Integer32"
_SleBGPPeerKeepInterval_Object = MibTableColumn
sleBGPPeerKeepInterval = _SleBGPPeerKeepInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 15),
    _SleBGPPeerKeepInterval_Type()
)
sleBGPPeerKeepInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerKeepInterval.setStatus("current")


class _SleBGPPeerHoldInterval_Type(Integer32):
    """Custom type sleBGPPeerHoldInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerHoldInterval_Type.__name__ = "Integer32"
_SleBGPPeerHoldInterval_Object = MibTableColumn
sleBGPPeerHoldInterval = _SleBGPPeerHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 16),
    _SleBGPPeerHoldInterval_Type()
)
sleBGPPeerHoldInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerHoldInterval.setStatus("current")


class _SleBGPPeerConnInterval_Type(Integer32):
    """Custom type sleBGPPeerConnInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerConnInterval_Type.__name__ = "Integer32"
_SleBGPPeerConnInterval_Object = MibTableColumn
sleBGPPeerConnInterval = _SleBGPPeerConnInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 17),
    _SleBGPPeerConnInterval_Type()
)
sleBGPPeerConnInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerConnInterval.setStatus("current")


class _SleBGPPeerOverCap_Type(Integer32):
    """Custom type sleBGPPeerOverCap based on Integer32"""
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


_SleBGPPeerOverCap_Type.__name__ = "Integer32"
_SleBGPPeerOverCap_Object = MibTableColumn
sleBGPPeerOverCap = _SleBGPPeerOverCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 18),
    _SleBGPPeerOverCap_Type()
)
sleBGPPeerOverCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerOverCap.setStatus("current")


class _SleBGPPeerStrictCapMatch_Type(Integer32):
    """Custom type sleBGPPeerStrictCapMatch based on Integer32"""
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


_SleBGPPeerStrictCapMatch_Type.__name__ = "Integer32"
_SleBGPPeerStrictCapMatch_Object = MibTableColumn
sleBGPPeerStrictCapMatch = _SleBGPPeerStrictCapMatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 19),
    _SleBGPPeerStrictCapMatch_Type()
)
sleBGPPeerStrictCapMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerStrictCapMatch.setStatus("current")
_SleBGPPeerIfname_Type = OctetString
_SleBGPPeerIfname_Object = MibTableColumn
sleBGPPeerIfname = _SleBGPPeerIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 20),
    _SleBGPPeerIfname_Type()
)
sleBGPPeerIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerIfname.setStatus("current")


class _SleBGPPeerCapRouteRefresh_Type(Integer32):
    """Custom type sleBGPPeerCapRouteRefresh based on Integer32"""
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


_SleBGPPeerCapRouteRefresh_Type.__name__ = "Integer32"
_SleBGPPeerCapRouteRefresh_Object = MibTableColumn
sleBGPPeerCapRouteRefresh = _SleBGPPeerCapRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 21),
    _SleBGPPeerCapRouteRefresh_Type()
)
sleBGPPeerCapRouteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerCapRouteRefresh.setStatus("current")


class _SleBGPPeerCapDynamic_Type(Integer32):
    """Custom type sleBGPPeerCapDynamic based on Integer32"""
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


_SleBGPPeerCapDynamic_Type.__name__ = "Integer32"
_SleBGPPeerCapDynamic_Object = MibTableColumn
sleBGPPeerCapDynamic = _SleBGPPeerCapDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 22),
    _SleBGPPeerCapDynamic_Type()
)
sleBGPPeerCapDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerCapDynamic.setStatus("current")


class _SleBGPPeerEBGPMulthopCount_Type(Integer32):
    """Custom type sleBGPPeerEBGPMulthopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPPeerEBGPMulthopCount_Type.__name__ = "Integer32"
_SleBGPPeerEBGPMulthopCount_Object = MibTableColumn
sleBGPPeerEBGPMulthopCount = _SleBGPPeerEBGPMulthopCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 23),
    _SleBGPPeerEBGPMulthopCount_Type()
)
sleBGPPeerEBGPMulthopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerEBGPMulthopCount.setStatus("current")


class _SleBGPPeerPassword_Type(OctetString):
    """Custom type sleBGPPeerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPPeerPassword_Type.__name__ = "OctetString"
_SleBGPPeerPassword_Object = MibTableColumn
sleBGPPeerPassword = _SleBGPPeerPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 1, 1, 24),
    _SleBGPPeerPassword_Type()
)
sleBGPPeerPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerPassword.setStatus("current")
_SleBGPPeerControl_ObjectIdentity = ObjectIdentity
sleBGPPeerControl = _SleBGPPeerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2)
)


class _SleBGPPeerControlRequest_Type(Integer32):
    """Custom type sleBGPPeerControlRequest based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("createBGPPeer", 1),
          ("deleteBGPPeer", 2),
          ("createPeerGroupName", 3),
          ("deletePeerGroupName", 4),
          ("setBGPPeerAdvInterval", 5),
          ("setBGPPeerAsOriInterval", 6),
          ("createBGPPeerDescription", 7),
          ("deleteBGPPeerDescription", 8),
          ("setBGPPeerDontCapNego", 9),
          ("setBGPPeerWeight", 10),
          ("setBGPPeerEnforceMultihop", 11),
          ("setBGPPeerPassive", 12),
          ("createBGPPeerUpSourceName", 13),
          ("deleteBGPPeerUpSourceName", 14),
          ("setBGPPeerPort", 15),
          ("setBGPPeerRestartTime", 16),
          ("setBGPPeerShutDown", 17),
          ("setBGPPeerTimersProfile", 18),
          ("setBGPPeerConnectInterval", 19),
          ("setBGPPeerOverCap", 20),
          ("setBGPPeerStrictCapMatch", 21),
          ("createBGPPeerIfname", 22),
          ("deleteBGPPeerIfname", 23),
          ("setBGPPeerCapRouteRefresh", 24),
          ("setBGPPeerCapDynamic", 25),
          ("setBGPPeerEBGPMulthopCount", 26),
          ("createBGPPeerPassword", 27),
          ("deleteBGPPeerPassword", 28))
    )


_SleBGPPeerControlRequest_Type.__name__ = "Integer32"
_SleBGPPeerControlRequest_Object = MibScalar
sleBGPPeerControlRequest = _SleBGPPeerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 1),
    _SleBGPPeerControlRequest_Type()
)
sleBGPPeerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlRequest.setStatus("current")
_SleBGPPeerControlStatus_Type = SleControlStatusType
_SleBGPPeerControlStatus_Object = MibScalar
sleBGPPeerControlStatus = _SleBGPPeerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 2),
    _SleBGPPeerControlStatus_Type()
)
sleBGPPeerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerControlStatus.setStatus("current")
_SleBGPPeerControlTimer_Type = Gauge32
_SleBGPPeerControlTimer_Object = MibScalar
sleBGPPeerControlTimer = _SleBGPPeerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 3),
    _SleBGPPeerControlTimer_Type()
)
sleBGPPeerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlTimer.setStatus("current")
_SleBGPPeerControlTimeStamp_Type = TimeTicks
_SleBGPPeerControlTimeStamp_Object = MibScalar
sleBGPPeerControlTimeStamp = _SleBGPPeerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 4),
    _SleBGPPeerControlTimeStamp_Type()
)
sleBGPPeerControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerControlTimeStamp.setStatus("current")
_SleBGPPeerControlReqResult_Type = SleControlRequestResultType
_SleBGPPeerControlReqResult_Object = MibScalar
sleBGPPeerControlReqResult = _SleBGPPeerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 5),
    _SleBGPPeerControlReqResult_Type()
)
sleBGPPeerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerControlReqResult.setStatus("current")


class _SleBGPPeerControlName_Type(OctetString):
    """Custom type sleBGPPeerControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPPeerControlName_Type.__name__ = "OctetString"
_SleBGPPeerControlName_Object = MibScalar
sleBGPPeerControlName = _SleBGPPeerControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 6),
    _SleBGPPeerControlName_Type()
)
sleBGPPeerControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlName.setStatus("current")


class _SleBGPPeerControlAsNum_Type(Gauge32):
    """Custom type sleBGPPeerControlAsNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPPeerControlAsNum_Type.__name__ = "Gauge32"
_SleBGPPeerControlAsNum_Object = MibScalar
sleBGPPeerControlAsNum = _SleBGPPeerControlAsNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 7),
    _SleBGPPeerControlAsNum_Type()
)
sleBGPPeerControlAsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlAsNum.setStatus("current")


class _SleBGPPeerControlGroupName_Type(OctetString):
    """Custom type sleBGPPeerControlGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerControlGroupName_Type.__name__ = "OctetString"
_SleBGPPeerControlGroupName_Object = MibScalar
sleBGPPeerControlGroupName = _SleBGPPeerControlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 8),
    _SleBGPPeerControlGroupName_Type()
)
sleBGPPeerControlGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlGroupName.setStatus("current")


class _SleBGPPeerControlAdvInterval_Type(Integer32):
    """Custom type sleBGPPeerControlAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerControlAdvInterval_Type.__name__ = "Integer32"
_SleBGPPeerControlAdvInterval_Object = MibScalar
sleBGPPeerControlAdvInterval = _SleBGPPeerControlAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 9),
    _SleBGPPeerControlAdvInterval_Type()
)
sleBGPPeerControlAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlAdvInterval.setStatus("current")


class _SleBGPPeerControlAsOriInterval_Type(Integer32):
    """Custom type sleBGPPeerControlAsOriInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerControlAsOriInterval_Type.__name__ = "Integer32"
_SleBGPPeerControlAsOriInterval_Object = MibScalar
sleBGPPeerControlAsOriInterval = _SleBGPPeerControlAsOriInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 10),
    _SleBGPPeerControlAsOriInterval_Type()
)
sleBGPPeerControlAsOriInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlAsOriInterval.setStatus("current")


class _SleBGPPeerControlDesc_Type(OctetString):
    """Custom type sleBGPPeerControlDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerControlDesc_Type.__name__ = "OctetString"
_SleBGPPeerControlDesc_Object = MibScalar
sleBGPPeerControlDesc = _SleBGPPeerControlDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 11),
    _SleBGPPeerControlDesc_Type()
)
sleBGPPeerControlDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlDesc.setStatus("current")


class _SleBGPPeerControlDontCapNego_Type(Integer32):
    """Custom type sleBGPPeerControlDontCapNego based on Integer32"""
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


_SleBGPPeerControlDontCapNego_Type.__name__ = "Integer32"
_SleBGPPeerControlDontCapNego_Object = MibScalar
sleBGPPeerControlDontCapNego = _SleBGPPeerControlDontCapNego_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 12),
    _SleBGPPeerControlDontCapNego_Type()
)
sleBGPPeerControlDontCapNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlDontCapNego.setStatus("current")


class _SleBGPPeerControlWeight_Type(Integer32):
    """Custom type sleBGPPeerControlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerControlWeight_Type.__name__ = "Integer32"
_SleBGPPeerControlWeight_Object = MibScalar
sleBGPPeerControlWeight = _SleBGPPeerControlWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 13),
    _SleBGPPeerControlWeight_Type()
)
sleBGPPeerControlWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlWeight.setStatus("current")


class _SleBGPPeerControlEnforcMultiHop_Type(Integer32):
    """Custom type sleBGPPeerControlEnforcMultiHop based on Integer32"""
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


_SleBGPPeerControlEnforcMultiHop_Type.__name__ = "Integer32"
_SleBGPPeerControlEnforcMultiHop_Object = MibScalar
sleBGPPeerControlEnforcMultiHop = _SleBGPPeerControlEnforcMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 14),
    _SleBGPPeerControlEnforcMultiHop_Type()
)
sleBGPPeerControlEnforcMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlEnforcMultiHop.setStatus("current")


class _SleBGPPeerControlPassive_Type(Integer32):
    """Custom type sleBGPPeerControlPassive based on Integer32"""
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


_SleBGPPeerControlPassive_Type.__name__ = "Integer32"
_SleBGPPeerControlPassive_Object = MibScalar
sleBGPPeerControlPassive = _SleBGPPeerControlPassive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 15),
    _SleBGPPeerControlPassive_Type()
)
sleBGPPeerControlPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlPassive.setStatus("current")
_SleBGPPeerControlUpSourceName_Type = OctetString
_SleBGPPeerControlUpSourceName_Object = MibScalar
sleBGPPeerControlUpSourceName = _SleBGPPeerControlUpSourceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 16),
    _SleBGPPeerControlUpSourceName_Type()
)
sleBGPPeerControlUpSourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlUpSourceName.setStatus("current")


class _SleBGPPeerControlPort_Type(Integer32):
    """Custom type sleBGPPeerControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerControlPort_Type.__name__ = "Integer32"
_SleBGPPeerControlPort_Object = MibScalar
sleBGPPeerControlPort = _SleBGPPeerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 17),
    _SleBGPPeerControlPort_Type()
)
sleBGPPeerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlPort.setStatus("current")


class _SleBGPPeerControlRetstartTime_Type(Integer32):
    """Custom type sleBGPPeerControlRetstartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPPeerControlRetstartTime_Type.__name__ = "Integer32"
_SleBGPPeerControlRetstartTime_Object = MibScalar
sleBGPPeerControlRetstartTime = _SleBGPPeerControlRetstartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 18),
    _SleBGPPeerControlRetstartTime_Type()
)
sleBGPPeerControlRetstartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlRetstartTime.setStatus("current")


class _SleBGPPeerControlShutDown_Type(Integer32):
    """Custom type sleBGPPeerControlShutDown based on Integer32"""
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


_SleBGPPeerControlShutDown_Type.__name__ = "Integer32"
_SleBGPPeerControlShutDown_Object = MibScalar
sleBGPPeerControlShutDown = _SleBGPPeerControlShutDown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 19),
    _SleBGPPeerControlShutDown_Type()
)
sleBGPPeerControlShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlShutDown.setStatus("current")


class _SleBGPPeerControlKeepInterval_Type(Integer32):
    """Custom type sleBGPPeerControlKeepInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerControlKeepInterval_Type.__name__ = "Integer32"
_SleBGPPeerControlKeepInterval_Object = MibScalar
sleBGPPeerControlKeepInterval = _SleBGPPeerControlKeepInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 20),
    _SleBGPPeerControlKeepInterval_Type()
)
sleBGPPeerControlKeepInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlKeepInterval.setStatus("current")


class _SleBGPPeerControlHoldInterval_Type(Integer32):
    """Custom type sleBGPPeerControlHoldInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerControlHoldInterval_Type.__name__ = "Integer32"
_SleBGPPeerControlHoldInterval_Object = MibScalar
sleBGPPeerControlHoldInterval = _SleBGPPeerControlHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 21),
    _SleBGPPeerControlHoldInterval_Type()
)
sleBGPPeerControlHoldInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlHoldInterval.setStatus("current")


class _SleBGPPeerControlConnInterval_Type(Integer32):
    """Custom type sleBGPPeerControlConnInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerControlConnInterval_Type.__name__ = "Integer32"
_SleBGPPeerControlConnInterval_Object = MibScalar
sleBGPPeerControlConnInterval = _SleBGPPeerControlConnInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 22),
    _SleBGPPeerControlConnInterval_Type()
)
sleBGPPeerControlConnInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlConnInterval.setStatus("current")


class _SleBGPPeerControlOverCap_Type(Integer32):
    """Custom type sleBGPPeerControlOverCap based on Integer32"""
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


_SleBGPPeerControlOverCap_Type.__name__ = "Integer32"
_SleBGPPeerControlOverCap_Object = MibScalar
sleBGPPeerControlOverCap = _SleBGPPeerControlOverCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 23),
    _SleBGPPeerControlOverCap_Type()
)
sleBGPPeerControlOverCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlOverCap.setStatus("current")


class _SleBGPPeerControlStrictCapMatch_Type(Integer32):
    """Custom type sleBGPPeerControlStrictCapMatch based on Integer32"""
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


_SleBGPPeerControlStrictCapMatch_Type.__name__ = "Integer32"
_SleBGPPeerControlStrictCapMatch_Object = MibScalar
sleBGPPeerControlStrictCapMatch = _SleBGPPeerControlStrictCapMatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 24),
    _SleBGPPeerControlStrictCapMatch_Type()
)
sleBGPPeerControlStrictCapMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlStrictCapMatch.setStatus("current")


class _SleBGPPeerControlIfname_Type(OctetString):
    """Custom type sleBGPPeerControlIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerControlIfname_Type.__name__ = "OctetString"
_SleBGPPeerControlIfname_Object = MibScalar
sleBGPPeerControlIfname = _SleBGPPeerControlIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 25),
    _SleBGPPeerControlIfname_Type()
)
sleBGPPeerControlIfname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlIfname.setStatus("current")


class _SleBGPPeerControlCapRouteRefresh_Type(Integer32):
    """Custom type sleBGPPeerControlCapRouteRefresh based on Integer32"""
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


_SleBGPPeerControlCapRouteRefresh_Type.__name__ = "Integer32"
_SleBGPPeerControlCapRouteRefresh_Object = MibScalar
sleBGPPeerControlCapRouteRefresh = _SleBGPPeerControlCapRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 26),
    _SleBGPPeerControlCapRouteRefresh_Type()
)
sleBGPPeerControlCapRouteRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlCapRouteRefresh.setStatus("current")


class _SleBGPPeerControlCapDynamic_Type(Integer32):
    """Custom type sleBGPPeerControlCapDynamic based on Integer32"""
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


_SleBGPPeerControlCapDynamic_Type.__name__ = "Integer32"
_SleBGPPeerControlCapDynamic_Object = MibScalar
sleBGPPeerControlCapDynamic = _SleBGPPeerControlCapDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 27),
    _SleBGPPeerControlCapDynamic_Type()
)
sleBGPPeerControlCapDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlCapDynamic.setStatus("current")


class _SleBGPPeerControlEBGPMulthopCount_Type(Integer32):
    """Custom type sleBGPPeerControlEBGPMulthopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPPeerControlEBGPMulthopCount_Type.__name__ = "Integer32"
_SleBGPPeerControlEBGPMulthopCount_Object = MibScalar
sleBGPPeerControlEBGPMulthopCount = _SleBGPPeerControlEBGPMulthopCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 28),
    _SleBGPPeerControlEBGPMulthopCount_Type()
)
sleBGPPeerControlEBGPMulthopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlEBGPMulthopCount.setStatus("current")


class _SleBGPPeerControlPassword_Type(OctetString):
    """Custom type sleBGPPeerControlPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerControlPassword_Type.__name__ = "OctetString"
_SleBGPPeerControlPassword_Object = MibScalar
sleBGPPeerControlPassword = _SleBGPPeerControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 2, 29),
    _SleBGPPeerControlPassword_Type()
)
sleBGPPeerControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerControlPassword.setStatus("current")
_SleBGPPeerNotification_ObjectIdentity = ObjectIdentity
sleBGPPeerNotification = _SleBGPPeerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3)
)
_SleBGPPeerGroup_ObjectIdentity = ObjectIdentity
sleBGPPeerGroup = _SleBGPPeerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2)
)
_SleBGPPeerGroupTable_Object = MibTable
sleBGPPeerGroupTable = _SleBGPPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupTable.setStatus("current")
_SleBGPPeerGroupEntry_Object = MibTableRow
sleBGPPeerGroupEntry = _SleBGPPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1)
)
sleBGPPeerGroupEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPPeerGroupStr"),
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupEntry.setStatus("current")


class _SleBGPPeerGroupStr_Type(OctetString):
    """Custom type sleBGPPeerGroupStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPPeerGroupStr_Type.__name__ = "OctetString"
_SleBGPPeerGroupStr_Object = MibTableColumn
sleBGPPeerGroupStr = _SleBGPPeerGroupStr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 1),
    _SleBGPPeerGroupStr_Type()
)
sleBGPPeerGroupStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupStr.setStatus("current")


class _SleBGPPeerGroupAsNum_Type(Gauge32):
    """Custom type sleBGPPeerGroupAsNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPPeerGroupAsNum_Type.__name__ = "Gauge32"
_SleBGPPeerGroupAsNum_Object = MibTableColumn
sleBGPPeerGroupAsNum = _SleBGPPeerGroupAsNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 2),
    _SleBGPPeerGroupAsNum_Type()
)
sleBGPPeerGroupAsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupAsNum.setStatus("current")


class _SleBGPPeerGroupAdvInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerGroupAdvInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupAdvInterval_Object = MibTableColumn
sleBGPPeerGroupAdvInterval = _SleBGPPeerGroupAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 3),
    _SleBGPPeerGroupAdvInterval_Type()
)
sleBGPPeerGroupAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupAdvInterval.setStatus("current")


class _SleBGPPeerGroupAsOriInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupAsOriInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerGroupAsOriInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupAsOriInterval_Object = MibTableColumn
sleBGPPeerGroupAsOriInterval = _SleBGPPeerGroupAsOriInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 4),
    _SleBGPPeerGroupAsOriInterval_Type()
)
sleBGPPeerGroupAsOriInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupAsOriInterval.setStatus("current")


class _SleBGPPeerGroupDesc_Type(OctetString):
    """Custom type sleBGPPeerGroupDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerGroupDesc_Type.__name__ = "OctetString"
_SleBGPPeerGroupDesc_Object = MibTableColumn
sleBGPPeerGroupDesc = _SleBGPPeerGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 5),
    _SleBGPPeerGroupDesc_Type()
)
sleBGPPeerGroupDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupDesc.setStatus("current")


class _SleBGPPeerGroupDontCapNego_Type(Integer32):
    """Custom type sleBGPPeerGroupDontCapNego based on Integer32"""
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


_SleBGPPeerGroupDontCapNego_Type.__name__ = "Integer32"
_SleBGPPeerGroupDontCapNego_Object = MibTableColumn
sleBGPPeerGroupDontCapNego = _SleBGPPeerGroupDontCapNego_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 6),
    _SleBGPPeerGroupDontCapNego_Type()
)
sleBGPPeerGroupDontCapNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupDontCapNego.setStatus("current")


class _SleBGPPeerGroupWeight_Type(Integer32):
    """Custom type sleBGPPeerGroupWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupWeight_Type.__name__ = "Integer32"
_SleBGPPeerGroupWeight_Object = MibTableColumn
sleBGPPeerGroupWeight = _SleBGPPeerGroupWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 7),
    _SleBGPPeerGroupWeight_Type()
)
sleBGPPeerGroupWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupWeight.setStatus("current")


class _SleBGPPeerGroupEnforcMultiHop_Type(Integer32):
    """Custom type sleBGPPeerGroupEnforcMultiHop based on Integer32"""
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


_SleBGPPeerGroupEnforcMultiHop_Type.__name__ = "Integer32"
_SleBGPPeerGroupEnforcMultiHop_Object = MibTableColumn
sleBGPPeerGroupEnforcMultiHop = _SleBGPPeerGroupEnforcMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 8),
    _SleBGPPeerGroupEnforcMultiHop_Type()
)
sleBGPPeerGroupEnforcMultiHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupEnforcMultiHop.setStatus("current")


class _SleBGPPeerGroupPassive_Type(Integer32):
    """Custom type sleBGPPeerGroupPassive based on Integer32"""
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


_SleBGPPeerGroupPassive_Type.__name__ = "Integer32"
_SleBGPPeerGroupPassive_Object = MibTableColumn
sleBGPPeerGroupPassive = _SleBGPPeerGroupPassive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 9),
    _SleBGPPeerGroupPassive_Type()
)
sleBGPPeerGroupPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupPassive.setStatus("current")
_SleBGPPeerGroupUpSourceName_Type = OctetString
_SleBGPPeerGroupUpSourceName_Object = MibTableColumn
sleBGPPeerGroupUpSourceName = _SleBGPPeerGroupUpSourceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 10),
    _SleBGPPeerGroupUpSourceName_Type()
)
sleBGPPeerGroupUpSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupUpSourceName.setStatus("current")


class _SleBGPPeerGroupPort_Type(Integer32):
    """Custom type sleBGPPeerGroupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupPort_Type.__name__ = "Integer32"
_SleBGPPeerGroupPort_Object = MibTableColumn
sleBGPPeerGroupPort = _SleBGPPeerGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 11),
    _SleBGPPeerGroupPort_Type()
)
sleBGPPeerGroupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupPort.setStatus("current")


class _SleBGPPeerGroupRetstartTime_Type(Integer32):
    """Custom type sleBGPPeerGroupRetstartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPPeerGroupRetstartTime_Type.__name__ = "Integer32"
_SleBGPPeerGroupRetstartTime_Object = MibTableColumn
sleBGPPeerGroupRetstartTime = _SleBGPPeerGroupRetstartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 12),
    _SleBGPPeerGroupRetstartTime_Type()
)
sleBGPPeerGroupRetstartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupRetstartTime.setStatus("current")


class _SleBGPPeerGroupShutDown_Type(Integer32):
    """Custom type sleBGPPeerGroupShutDown based on Integer32"""
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


_SleBGPPeerGroupShutDown_Type.__name__ = "Integer32"
_SleBGPPeerGroupShutDown_Object = MibTableColumn
sleBGPPeerGroupShutDown = _SleBGPPeerGroupShutDown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 13),
    _SleBGPPeerGroupShutDown_Type()
)
sleBGPPeerGroupShutDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupShutDown.setStatus("current")


class _SleBGPPeerGroupKeepInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupKeepInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupKeepInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupKeepInterval_Object = MibTableColumn
sleBGPPeerGroupKeepInterval = _SleBGPPeerGroupKeepInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 14),
    _SleBGPPeerGroupKeepInterval_Type()
)
sleBGPPeerGroupKeepInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupKeepInterval.setStatus("current")


class _SleBGPPeerGroupHoldInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupHoldInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupHoldInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupHoldInterval_Object = MibTableColumn
sleBGPPeerGroupHoldInterval = _SleBGPPeerGroupHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 15),
    _SleBGPPeerGroupHoldInterval_Type()
)
sleBGPPeerGroupHoldInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupHoldInterval.setStatus("current")


class _SleBGPPeerGroupConnInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupConnInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupConnInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupConnInterval_Object = MibTableColumn
sleBGPPeerGroupConnInterval = _SleBGPPeerGroupConnInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 16),
    _SleBGPPeerGroupConnInterval_Type()
)
sleBGPPeerGroupConnInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupConnInterval.setStatus("current")


class _SleBGPPeerGroupOverCap_Type(Integer32):
    """Custom type sleBGPPeerGroupOverCap based on Integer32"""
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


_SleBGPPeerGroupOverCap_Type.__name__ = "Integer32"
_SleBGPPeerGroupOverCap_Object = MibTableColumn
sleBGPPeerGroupOverCap = _SleBGPPeerGroupOverCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 17),
    _SleBGPPeerGroupOverCap_Type()
)
sleBGPPeerGroupOverCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupOverCap.setStatus("current")


class _SleBGPPeerGroupStrictCapMatch_Type(Integer32):
    """Custom type sleBGPPeerGroupStrictCapMatch based on Integer32"""
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


_SleBGPPeerGroupStrictCapMatch_Type.__name__ = "Integer32"
_SleBGPPeerGroupStrictCapMatch_Object = MibTableColumn
sleBGPPeerGroupStrictCapMatch = _SleBGPPeerGroupStrictCapMatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 18),
    _SleBGPPeerGroupStrictCapMatch_Type()
)
sleBGPPeerGroupStrictCapMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupStrictCapMatch.setStatus("current")


class _SleBGPPeerGroupCapRouteRefresh_Type(Integer32):
    """Custom type sleBGPPeerGroupCapRouteRefresh based on Integer32"""
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


_SleBGPPeerGroupCapRouteRefresh_Type.__name__ = "Integer32"
_SleBGPPeerGroupCapRouteRefresh_Object = MibTableColumn
sleBGPPeerGroupCapRouteRefresh = _SleBGPPeerGroupCapRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 19),
    _SleBGPPeerGroupCapRouteRefresh_Type()
)
sleBGPPeerGroupCapRouteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupCapRouteRefresh.setStatus("current")


class _SleBGPPeerGroupCapDynamic_Type(Integer32):
    """Custom type sleBGPPeerGroupCapDynamic based on Integer32"""
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


_SleBGPPeerGroupCapDynamic_Type.__name__ = "Integer32"
_SleBGPPeerGroupCapDynamic_Object = MibTableColumn
sleBGPPeerGroupCapDynamic = _SleBGPPeerGroupCapDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 20),
    _SleBGPPeerGroupCapDynamic_Type()
)
sleBGPPeerGroupCapDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupCapDynamic.setStatus("current")


class _SleBGPPeerGroupEBGPMulthopCount_Type(Integer32):
    """Custom type sleBGPPeerGroupEBGPMulthopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPPeerGroupEBGPMulthopCount_Type.__name__ = "Integer32"
_SleBGPPeerGroupEBGPMulthopCount_Object = MibTableColumn
sleBGPPeerGroupEBGPMulthopCount = _SleBGPPeerGroupEBGPMulthopCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 21),
    _SleBGPPeerGroupEBGPMulthopCount_Type()
)
sleBGPPeerGroupEBGPMulthopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupEBGPMulthopCount.setStatus("current")


class _SleBGPPeerGroupPassword_Type(OctetString):
    """Custom type sleBGPPeerGroupPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPPeerGroupPassword_Type.__name__ = "OctetString"
_SleBGPPeerGroupPassword_Object = MibTableColumn
sleBGPPeerGroupPassword = _SleBGPPeerGroupPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 1, 1, 22),
    _SleBGPPeerGroupPassword_Type()
)
sleBGPPeerGroupPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupPassword.setStatus("current")
_SleBGPPeerGroupControl_ObjectIdentity = ObjectIdentity
sleBGPPeerGroupControl = _SleBGPPeerGroupControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2)
)


class _SleBGPPeerGroupControlRequest_Type(Integer32):
    """Custom type sleBGPPeerGroupControlRequest based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("createBGPPeerGroup", 1),
          ("deleteBGPPeerGroup", 2),
          ("setBGPPeerGroupRemoteAs", 3),
          ("setBGPPeerGroupAdvInterval", 4),
          ("setBGPPeerGroupAsOriInterval", 5),
          ("createBGPPeerGroupDescription", 6),
          ("deleteBGPPeerGroupDescription", 7),
          ("setBGPPeerGroupDontCapNego", 8),
          ("setBGPPeerGroupWeight", 9),
          ("setBGPPeerGroupEnforceMultihop", 10),
          ("setBGPPeerGroupPassive", 11),
          ("createBGPPeerGroupUpSourceName", 12),
          ("deleteBGPPeerGroupUpSourceName", 13),
          ("setBGPPeerGroupPort", 14),
          ("setBGPPeerGroupRestartTime", 15),
          ("setBGPPeerGroupShutDown", 16),
          ("setBGPPeerGroupTimersProfile", 17),
          ("setBGPPeerGroupConnInterval", 18),
          ("setBGPPeerGroupOverCap", 19),
          ("setBGPPeerGroupStrictCapMatch", 20),
          ("setBGPPeerGroupCapRouteRefresh", 21),
          ("setBGPPeerGroupCapDynamic", 22),
          ("setBGPPeerGroupEBGPMulthopCount", 23),
          ("createBGPPeerGroupPassword", 24),
          ("deleteBGPPeerGroupPassword", 25))
    )


_SleBGPPeerGroupControlRequest_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlRequest_Object = MibScalar
sleBGPPeerGroupControlRequest = _SleBGPPeerGroupControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 1),
    _SleBGPPeerGroupControlRequest_Type()
)
sleBGPPeerGroupControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlRequest.setStatus("current")
_SleBGPPeerGroupControlStatus_Type = SleControlStatusType
_SleBGPPeerGroupControlStatus_Object = MibScalar
sleBGPPeerGroupControlStatus = _SleBGPPeerGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 2),
    _SleBGPPeerGroupControlStatus_Type()
)
sleBGPPeerGroupControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlStatus.setStatus("current")
_SleBGPPeerGroupControlTimer_Type = Gauge32
_SleBGPPeerGroupControlTimer_Object = MibScalar
sleBGPPeerGroupControlTimer = _SleBGPPeerGroupControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 3),
    _SleBGPPeerGroupControlTimer_Type()
)
sleBGPPeerGroupControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlTimer.setStatus("current")
_SleBGPPeerGroupControlTimeStamp_Type = TimeTicks
_SleBGPPeerGroupControlTimeStamp_Object = MibScalar
sleBGPPeerGroupControlTimeStamp = _SleBGPPeerGroupControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 4),
    _SleBGPPeerGroupControlTimeStamp_Type()
)
sleBGPPeerGroupControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlTimeStamp.setStatus("current")
_SleBGPPeerGroupControlReqResult_Type = SleControlRequestResultType
_SleBGPPeerGroupControlReqResult_Object = MibScalar
sleBGPPeerGroupControlReqResult = _SleBGPPeerGroupControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 5),
    _SleBGPPeerGroupControlReqResult_Type()
)
sleBGPPeerGroupControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlReqResult.setStatus("current")


class _SleBGPPeerGroupControlStr_Type(OctetString):
    """Custom type sleBGPPeerGroupControlStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPPeerGroupControlStr_Type.__name__ = "OctetString"
_SleBGPPeerGroupControlStr_Object = MibScalar
sleBGPPeerGroupControlStr = _SleBGPPeerGroupControlStr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 6),
    _SleBGPPeerGroupControlStr_Type()
)
sleBGPPeerGroupControlStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlStr.setStatus("current")


class _SleBGPPeerGroupControlAsNum_Type(Gauge32):
    """Custom type sleBGPPeerGroupControlAsNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPPeerGroupControlAsNum_Type.__name__ = "Gauge32"
_SleBGPPeerGroupControlAsNum_Object = MibScalar
sleBGPPeerGroupControlAsNum = _SleBGPPeerGroupControlAsNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 7),
    _SleBGPPeerGroupControlAsNum_Type()
)
sleBGPPeerGroupControlAsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlAsNum.setStatus("current")


class _SleBGPPeerGroupControlAdvInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupControlAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerGroupControlAdvInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlAdvInterval_Object = MibScalar
sleBGPPeerGroupControlAdvInterval = _SleBGPPeerGroupControlAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 8),
    _SleBGPPeerGroupControlAdvInterval_Type()
)
sleBGPPeerGroupControlAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlAdvInterval.setStatus("current")


class _SleBGPPeerGroupControlAsOriInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupControlAsOriInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleBGPPeerGroupControlAsOriInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlAsOriInterval_Object = MibScalar
sleBGPPeerGroupControlAsOriInterval = _SleBGPPeerGroupControlAsOriInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 9),
    _SleBGPPeerGroupControlAsOriInterval_Type()
)
sleBGPPeerGroupControlAsOriInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlAsOriInterval.setStatus("current")


class _SleBGPPeerGroupControlDesc_Type(OctetString):
    """Custom type sleBGPPeerGroupControlDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerGroupControlDesc_Type.__name__ = "OctetString"
_SleBGPPeerGroupControlDesc_Object = MibScalar
sleBGPPeerGroupControlDesc = _SleBGPPeerGroupControlDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 10),
    _SleBGPPeerGroupControlDesc_Type()
)
sleBGPPeerGroupControlDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlDesc.setStatus("current")


class _SleBGPPeerGroupControlDontCapNego_Type(Integer32):
    """Custom type sleBGPPeerGroupControlDontCapNego based on Integer32"""
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


_SleBGPPeerGroupControlDontCapNego_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlDontCapNego_Object = MibScalar
sleBGPPeerGroupControlDontCapNego = _SleBGPPeerGroupControlDontCapNego_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 11),
    _SleBGPPeerGroupControlDontCapNego_Type()
)
sleBGPPeerGroupControlDontCapNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlDontCapNego.setStatus("current")


class _SleBGPPeerGroupControlWeight_Type(Integer32):
    """Custom type sleBGPPeerGroupControlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupControlWeight_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlWeight_Object = MibScalar
sleBGPPeerGroupControlWeight = _SleBGPPeerGroupControlWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 12),
    _SleBGPPeerGroupControlWeight_Type()
)
sleBGPPeerGroupControlWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlWeight.setStatus("current")


class _SleBGPPeerGroupControlEnforcMultiHop_Type(Integer32):
    """Custom type sleBGPPeerGroupControlEnforcMultiHop based on Integer32"""
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


_SleBGPPeerGroupControlEnforcMultiHop_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlEnforcMultiHop_Object = MibScalar
sleBGPPeerGroupControlEnforcMultiHop = _SleBGPPeerGroupControlEnforcMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 13),
    _SleBGPPeerGroupControlEnforcMultiHop_Type()
)
sleBGPPeerGroupControlEnforcMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlEnforcMultiHop.setStatus("current")


class _SleBGPPeerGroupControlPassive_Type(Integer32):
    """Custom type sleBGPPeerGroupControlPassive based on Integer32"""
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


_SleBGPPeerGroupControlPassive_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlPassive_Object = MibScalar
sleBGPPeerGroupControlPassive = _SleBGPPeerGroupControlPassive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 14),
    _SleBGPPeerGroupControlPassive_Type()
)
sleBGPPeerGroupControlPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlPassive.setStatus("current")
_SleBGPPeerGroupControlUpSourceName_Type = OctetString
_SleBGPPeerGroupControlUpSourceName_Object = MibScalar
sleBGPPeerGroupControlUpSourceName = _SleBGPPeerGroupControlUpSourceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 15),
    _SleBGPPeerGroupControlUpSourceName_Type()
)
sleBGPPeerGroupControlUpSourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlUpSourceName.setStatus("current")


class _SleBGPPeerGroupControlPort_Type(Integer32):
    """Custom type sleBGPPeerGroupControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupControlPort_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlPort_Object = MibScalar
sleBGPPeerGroupControlPort = _SleBGPPeerGroupControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 16),
    _SleBGPPeerGroupControlPort_Type()
)
sleBGPPeerGroupControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlPort.setStatus("current")


class _SleBGPPeerGroupControlRetstartTime_Type(Integer32):
    """Custom type sleBGPPeerGroupControlRetstartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPPeerGroupControlRetstartTime_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlRetstartTime_Object = MibScalar
sleBGPPeerGroupControlRetstartTime = _SleBGPPeerGroupControlRetstartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 17),
    _SleBGPPeerGroupControlRetstartTime_Type()
)
sleBGPPeerGroupControlRetstartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlRetstartTime.setStatus("current")


class _SleBGPPeerGroupControlShutDown_Type(Integer32):
    """Custom type sleBGPPeerGroupControlShutDown based on Integer32"""
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


_SleBGPPeerGroupControlShutDown_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlShutDown_Object = MibScalar
sleBGPPeerGroupControlShutDown = _SleBGPPeerGroupControlShutDown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 18),
    _SleBGPPeerGroupControlShutDown_Type()
)
sleBGPPeerGroupControlShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlShutDown.setStatus("current")


class _SleBGPPeerGroupControlKeepInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupControlKeepInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupControlKeepInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlKeepInterval_Object = MibScalar
sleBGPPeerGroupControlKeepInterval = _SleBGPPeerGroupControlKeepInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 19),
    _SleBGPPeerGroupControlKeepInterval_Type()
)
sleBGPPeerGroupControlKeepInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlKeepInterval.setStatus("current")


class _SleBGPPeerGroupControlHoldInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupControlHoldInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupControlHoldInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlHoldInterval_Object = MibScalar
sleBGPPeerGroupControlHoldInterval = _SleBGPPeerGroupControlHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 20),
    _SleBGPPeerGroupControlHoldInterval_Type()
)
sleBGPPeerGroupControlHoldInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlHoldInterval.setStatus("current")


class _SleBGPPeerGroupControlConnInterval_Type(Integer32):
    """Custom type sleBGPPeerGroupControlConnInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleBGPPeerGroupControlConnInterval_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlConnInterval_Object = MibScalar
sleBGPPeerGroupControlConnInterval = _SleBGPPeerGroupControlConnInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 21),
    _SleBGPPeerGroupControlConnInterval_Type()
)
sleBGPPeerGroupControlConnInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlConnInterval.setStatus("current")


class _SleBGPPeerGroupControlOverCap_Type(Integer32):
    """Custom type sleBGPPeerGroupControlOverCap based on Integer32"""
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


_SleBGPPeerGroupControlOverCap_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlOverCap_Object = MibScalar
sleBGPPeerGroupControlOverCap = _SleBGPPeerGroupControlOverCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 22),
    _SleBGPPeerGroupControlOverCap_Type()
)
sleBGPPeerGroupControlOverCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlOverCap.setStatus("current")


class _SleBGPPeerGroupControlStrictCapMatch_Type(Integer32):
    """Custom type sleBGPPeerGroupControlStrictCapMatch based on Integer32"""
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


_SleBGPPeerGroupControlStrictCapMatch_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlStrictCapMatch_Object = MibScalar
sleBGPPeerGroupControlStrictCapMatch = _SleBGPPeerGroupControlStrictCapMatch_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 23),
    _SleBGPPeerGroupControlStrictCapMatch_Type()
)
sleBGPPeerGroupControlStrictCapMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlStrictCapMatch.setStatus("current")


class _SleBGPPeerGroupControlCapRouteRefresh_Type(Integer32):
    """Custom type sleBGPPeerGroupControlCapRouteRefresh based on Integer32"""
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


_SleBGPPeerGroupControlCapRouteRefresh_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlCapRouteRefresh_Object = MibScalar
sleBGPPeerGroupControlCapRouteRefresh = _SleBGPPeerGroupControlCapRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 24),
    _SleBGPPeerGroupControlCapRouteRefresh_Type()
)
sleBGPPeerGroupControlCapRouteRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlCapRouteRefresh.setStatus("current")


class _SleBGPPeerGroupControlCapDynamic_Type(Integer32):
    """Custom type sleBGPPeerGroupControlCapDynamic based on Integer32"""
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


_SleBGPPeerGroupControlCapDynamic_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlCapDynamic_Object = MibScalar
sleBGPPeerGroupControlCapDynamic = _SleBGPPeerGroupControlCapDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 25),
    _SleBGPPeerGroupControlCapDynamic_Type()
)
sleBGPPeerGroupControlCapDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlCapDynamic.setStatus("current")


class _SleBGPPeerGroupControlEBGPMulthopCount_Type(Integer32):
    """Custom type sleBGPPeerGroupControlEBGPMulthopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPPeerGroupControlEBGPMulthopCount_Type.__name__ = "Integer32"
_SleBGPPeerGroupControlEBGPMulthopCount_Object = MibScalar
sleBGPPeerGroupControlEBGPMulthopCount = _SleBGPPeerGroupControlEBGPMulthopCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 26),
    _SleBGPPeerGroupControlEBGPMulthopCount_Type()
)
sleBGPPeerGroupControlEBGPMulthopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlEBGPMulthopCount.setStatus("current")


class _SleBGPPeerGroupControlPassword_Type(OctetString):
    """Custom type sleBGPPeerGroupControlPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleBGPPeerGroupControlPassword_Type.__name__ = "OctetString"
_SleBGPPeerGroupControlPassword_Object = MibScalar
sleBGPPeerGroupControlPassword = _SleBGPPeerGroupControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 2, 27),
    _SleBGPPeerGroupControlPassword_Type()
)
sleBGPPeerGroupControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPPeerGroupControlPassword.setStatus("current")
_SleBGPPeerGroupNotification_ObjectIdentity = ObjectIdentity
sleBGPPeerGroupNotification = _SleBGPPeerGroupNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3)
)
_SleBGPAFInfo_ObjectIdentity = ObjectIdentity
sleBGPAFInfo = _SleBGPAFInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5)
)
_SleBGPAFBase_ObjectIdentity = ObjectIdentity
sleBGPAFBase = _SleBGPAFBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1)
)
_SleBGPAFBaseTable_Object = MibTable
sleBGPAFBaseTable = _SleBGPAFBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sleBGPAFBaseTable.setStatus("current")
_SleBGPAFBaseEntry_Object = MibTableRow
sleBGPAFBaseEntry = _SleBGPAFBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1)
)
sleBGPAFBaseEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPAFBaseMode"),
    (0, "SLE-BGP-MIB", "sleBGPAFBaseType"),
)
if mibBuilder.loadTexts:
    sleBGPAFBaseEntry.setStatus("current")


class _SleBGPAFBaseMode_Type(Integer32):
    """Custom type sleBGPAFBaseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFBaseMode_Type.__name__ = "Integer32"
_SleBGPAFBaseMode_Object = MibTableColumn
sleBGPAFBaseMode = _SleBGPAFBaseMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 1),
    _SleBGPAFBaseMode_Type()
)
sleBGPAFBaseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseMode.setStatus("current")


class _SleBGPAFBaseType_Type(Integer32):
    """Custom type sleBGPAFBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("vpn4", 3))
    )


_SleBGPAFBaseType_Type.__name__ = "Integer32"
_SleBGPAFBaseType_Object = MibTableColumn
sleBGPAFBaseType = _SleBGPAFBaseType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 2),
    _SleBGPAFBaseType_Type()
)
sleBGPAFBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseType.setStatus("current")


class _SleBGPAFBaseNetworkCheck_Type(Integer32):
    """Custom type sleBGPAFBaseNetworkCheck based on Integer32"""
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


_SleBGPAFBaseNetworkCheck_Type.__name__ = "Integer32"
_SleBGPAFBaseNetworkCheck_Object = MibTableColumn
sleBGPAFBaseNetworkCheck = _SleBGPAFBaseNetworkCheck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 3),
    _SleBGPAFBaseNetworkCheck_Type()
)
sleBGPAFBaseNetworkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseNetworkCheck.setStatus("current")


class _SleBGPAFBaseSync_Type(Integer32):
    """Custom type sleBGPAFBaseSync based on Integer32"""
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


_SleBGPAFBaseSync_Type.__name__ = "Integer32"
_SleBGPAFBaseSync_Object = MibTableColumn
sleBGPAFBaseSync = _SleBGPAFBaseSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 4),
    _SleBGPAFBaseSync_Type()
)
sleBGPAFBaseSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseSync.setStatus("current")


class _SleBGPAFBaseDefOrg_Type(Integer32):
    """Custom type sleBGPAFBaseDefOrg based on Integer32"""
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


_SleBGPAFBaseDefOrg_Type.__name__ = "Integer32"
_SleBGPAFBaseDefOrg_Object = MibTableColumn
sleBGPAFBaseDefOrg = _SleBGPAFBaseDefOrg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 5),
    _SleBGPAFBaseDefOrg_Type()
)
sleBGPAFBaseDefOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseDefOrg.setStatus("current")


class _SleBGPAFBaseDampRoutemapName_Type(OctetString):
    """Custom type sleBGPAFBaseDampRoutemapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFBaseDampRoutemapName_Type.__name__ = "OctetString"
_SleBGPAFBaseDampRoutemapName_Object = MibTableColumn
sleBGPAFBaseDampRoutemapName = _SleBGPAFBaseDampRoutemapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 6),
    _SleBGPAFBaseDampRoutemapName_Type()
)
sleBGPAFBaseDampRoutemapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseDampRoutemapName.setStatus("current")


class _SleBGPAFBaseDampReachHlife_Type(Integer32):
    """Custom type sleBGPAFBaseDampReachHlife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_SleBGPAFBaseDampReachHlife_Type.__name__ = "Integer32"
_SleBGPAFBaseDampReachHlife_Object = MibTableColumn
sleBGPAFBaseDampReachHlife = _SleBGPAFBaseDampReachHlife_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 7),
    _SleBGPAFBaseDampReachHlife_Type()
)
sleBGPAFBaseDampReachHlife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseDampReachHlife.setStatus("current")


class _SleBGPAFBaseDampReuse_Type(Integer32):
    """Custom type sleBGPAFBaseDampReuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_SleBGPAFBaseDampReuse_Type.__name__ = "Integer32"
_SleBGPAFBaseDampReuse_Object = MibTableColumn
sleBGPAFBaseDampReuse = _SleBGPAFBaseDampReuse_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 8),
    _SleBGPAFBaseDampReuse_Type()
)
sleBGPAFBaseDampReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseDampReuse.setStatus("current")


class _SleBGPAFBaseDampSuppress_Type(Integer32):
    """Custom type sleBGPAFBaseDampSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_SleBGPAFBaseDampSuppress_Type.__name__ = "Integer32"
_SleBGPAFBaseDampSuppress_Object = MibTableColumn
sleBGPAFBaseDampSuppress = _SleBGPAFBaseDampSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 9),
    _SleBGPAFBaseDampSuppress_Type()
)
sleBGPAFBaseDampSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseDampSuppress.setStatus("current")


class _SleBGPAFBaseDampMaxSuppress_Type(Integer32):
    """Custom type sleBGPAFBaseDampMaxSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPAFBaseDampMaxSuppress_Type.__name__ = "Integer32"
_SleBGPAFBaseDampMaxSuppress_Object = MibTableColumn
sleBGPAFBaseDampMaxSuppress = _SleBGPAFBaseDampMaxSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 10),
    _SleBGPAFBaseDampMaxSuppress_Type()
)
sleBGPAFBaseDampMaxSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseDampMaxSuppress.setStatus("current")


class _SleBGPAFBaseDampUnReachHlife_Type(Integer32):
    """Custom type sleBGPAFBaseDampUnReachHlife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_SleBGPAFBaseDampUnReachHlife_Type.__name__ = "Integer32"
_SleBGPAFBaseDampUnReachHlife_Object = MibTableColumn
sleBGPAFBaseDampUnReachHlife = _SleBGPAFBaseDampUnReachHlife_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 1, 1, 11),
    _SleBGPAFBaseDampUnReachHlife_Type()
)
sleBGPAFBaseDampUnReachHlife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseDampUnReachHlife.setStatus("current")
_SleBGPAFBaseControl_ObjectIdentity = ObjectIdentity
sleBGPAFBaseControl = _SleBGPAFBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2)
)


class _SleBGPAFBaseControlRequest_Type(Integer32):
    """Custom type sleBGPAFBaseControlRequest based on Integer32"""
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
        *(("setBGPAFBaseNetworkCheck", 1),
          ("setBGPAFBaseSync", 2),
          ("setBGPAFBaseDefOrg", 3),
          ("setBGPAFBaseDampRoutemap", 4),
          ("setBGPAFBaseDampTimeProfile", 5),
          ("deleteBGPAFBaseDamp", 6))
    )


_SleBGPAFBaseControlRequest_Type.__name__ = "Integer32"
_SleBGPAFBaseControlRequest_Object = MibScalar
sleBGPAFBaseControlRequest = _SleBGPAFBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 1),
    _SleBGPAFBaseControlRequest_Type()
)
sleBGPAFBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlRequest.setStatus("current")
_SleBGPAFBaseControlStatus_Type = SleControlStatusType
_SleBGPAFBaseControlStatus_Object = MibScalar
sleBGPAFBaseControlStatus = _SleBGPAFBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 2),
    _SleBGPAFBaseControlStatus_Type()
)
sleBGPAFBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlStatus.setStatus("current")
_SleBGPAFBaseControlTimer_Type = Gauge32
_SleBGPAFBaseControlTimer_Object = MibScalar
sleBGPAFBaseControlTimer = _SleBGPAFBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 3),
    _SleBGPAFBaseControlTimer_Type()
)
sleBGPAFBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlTimer.setStatus("current")
_SleBGPAFBaseControlTimeStamp_Type = TimeTicks
_SleBGPAFBaseControlTimeStamp_Object = MibScalar
sleBGPAFBaseControlTimeStamp = _SleBGPAFBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 4),
    _SleBGPAFBaseControlTimeStamp_Type()
)
sleBGPAFBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlTimeStamp.setStatus("current")
_SleBGPAFBaseControlReqResult_Type = SleControlRequestResultType
_SleBGPAFBaseControlReqResult_Object = MibScalar
sleBGPAFBaseControlReqResult = _SleBGPAFBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 5),
    _SleBGPAFBaseControlReqResult_Type()
)
sleBGPAFBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlReqResult.setStatus("current")


class _SleBGPAFBaseControlMode_Type(Integer32):
    """Custom type sleBGPAFBaseControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFBaseControlMode_Type.__name__ = "Integer32"
_SleBGPAFBaseControlMode_Object = MibScalar
sleBGPAFBaseControlMode = _SleBGPAFBaseControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 6),
    _SleBGPAFBaseControlMode_Type()
)
sleBGPAFBaseControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlMode.setStatus("current")


class _SleBGPAFBaseControlType_Type(Integer32):
    """Custom type sleBGPAFBaseControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("vpn4", 3))
    )


_SleBGPAFBaseControlType_Type.__name__ = "Integer32"
_SleBGPAFBaseControlType_Object = MibScalar
sleBGPAFBaseControlType = _SleBGPAFBaseControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 7),
    _SleBGPAFBaseControlType_Type()
)
sleBGPAFBaseControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlType.setStatus("current")


class _SleBGPAFBaseControlNetworkCheck_Type(Integer32):
    """Custom type sleBGPAFBaseControlNetworkCheck based on Integer32"""
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


_SleBGPAFBaseControlNetworkCheck_Type.__name__ = "Integer32"
_SleBGPAFBaseControlNetworkCheck_Object = MibScalar
sleBGPAFBaseControlNetworkCheck = _SleBGPAFBaseControlNetworkCheck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 8),
    _SleBGPAFBaseControlNetworkCheck_Type()
)
sleBGPAFBaseControlNetworkCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlNetworkCheck.setStatus("current")


class _SleBGPAFBaseControlSync_Type(Integer32):
    """Custom type sleBGPAFBaseControlSync based on Integer32"""
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


_SleBGPAFBaseControlSync_Type.__name__ = "Integer32"
_SleBGPAFBaseControlSync_Object = MibScalar
sleBGPAFBaseControlSync = _SleBGPAFBaseControlSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 9),
    _SleBGPAFBaseControlSync_Type()
)
sleBGPAFBaseControlSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlSync.setStatus("current")


class _SleBGPAFBaseControlDefOrg_Type(Integer32):
    """Custom type sleBGPAFBaseControlDefOrg based on Integer32"""
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


_SleBGPAFBaseControlDefOrg_Type.__name__ = "Integer32"
_SleBGPAFBaseControlDefOrg_Object = MibScalar
sleBGPAFBaseControlDefOrg = _SleBGPAFBaseControlDefOrg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 10),
    _SleBGPAFBaseControlDefOrg_Type()
)
sleBGPAFBaseControlDefOrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlDefOrg.setStatus("current")


class _SleBGPAFBaseControlDampRoutemapName_Type(OctetString):
    """Custom type sleBGPAFBaseControlDampRoutemapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFBaseControlDampRoutemapName_Type.__name__ = "OctetString"
_SleBGPAFBaseControlDampRoutemapName_Object = MibScalar
sleBGPAFBaseControlDampRoutemapName = _SleBGPAFBaseControlDampRoutemapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 11),
    _SleBGPAFBaseControlDampRoutemapName_Type()
)
sleBGPAFBaseControlDampRoutemapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlDampRoutemapName.setStatus("current")


class _SleBGPAFBaseControlDampReachHlife_Type(Integer32):
    """Custom type sleBGPAFBaseControlDampReachHlife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_SleBGPAFBaseControlDampReachHlife_Type.__name__ = "Integer32"
_SleBGPAFBaseControlDampReachHlife_Object = MibScalar
sleBGPAFBaseControlDampReachHlife = _SleBGPAFBaseControlDampReachHlife_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 12),
    _SleBGPAFBaseControlDampReachHlife_Type()
)
sleBGPAFBaseControlDampReachHlife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlDampReachHlife.setStatus("current")


class _SleBGPAFBaseControlDampReuse_Type(Integer32):
    """Custom type sleBGPAFBaseControlDampReuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_SleBGPAFBaseControlDampReuse_Type.__name__ = "Integer32"
_SleBGPAFBaseControlDampReuse_Object = MibScalar
sleBGPAFBaseControlDampReuse = _SleBGPAFBaseControlDampReuse_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 13),
    _SleBGPAFBaseControlDampReuse_Type()
)
sleBGPAFBaseControlDampReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlDampReuse.setStatus("current")


class _SleBGPAFBaseControlDampSuppress_Type(Integer32):
    """Custom type sleBGPAFBaseControlDampSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_SleBGPAFBaseControlDampSuppress_Type.__name__ = "Integer32"
_SleBGPAFBaseControlDampSuppress_Object = MibScalar
sleBGPAFBaseControlDampSuppress = _SleBGPAFBaseControlDampSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 14),
    _SleBGPAFBaseControlDampSuppress_Type()
)
sleBGPAFBaseControlDampSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlDampSuppress.setStatus("current")


class _SleBGPAFBaseControlDampMaxSuppress_Type(Integer32):
    """Custom type sleBGPAFBaseControlDampMaxSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleBGPAFBaseControlDampMaxSuppress_Type.__name__ = "Integer32"
_SleBGPAFBaseControlDampMaxSuppress_Object = MibScalar
sleBGPAFBaseControlDampMaxSuppress = _SleBGPAFBaseControlDampMaxSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 15),
    _SleBGPAFBaseControlDampMaxSuppress_Type()
)
sleBGPAFBaseControlDampMaxSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlDampMaxSuppress.setStatus("current")


class _SleBGPAFBaseControlDampUnReachHlife_Type(Integer32):
    """Custom type sleBGPAFBaseControlDampUnReachHlife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_SleBGPAFBaseControlDampUnReachHlife_Type.__name__ = "Integer32"
_SleBGPAFBaseControlDampUnReachHlife_Object = MibScalar
sleBGPAFBaseControlDampUnReachHlife = _SleBGPAFBaseControlDampUnReachHlife_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 2, 16),
    _SleBGPAFBaseControlDampUnReachHlife_Type()
)
sleBGPAFBaseControlDampUnReachHlife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFBaseControlDampUnReachHlife.setStatus("current")
_SleBGPAFBaseNotification_ObjectIdentity = ObjectIdentity
sleBGPAFBaseNotification = _SleBGPAFBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 3)
)
_SleBGPAFRedist_ObjectIdentity = ObjectIdentity
sleBGPAFRedist = _SleBGPAFRedist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2)
)
_SleBGPAFRedistTable_Object = MibTable
sleBGPAFRedistTable = _SleBGPAFRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sleBGPAFRedistTable.setStatus("current")
_SleBGPAFRedistEntry_Object = MibTableRow
sleBGPAFRedistEntry = _SleBGPAFRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 1, 1)
)
sleBGPAFRedistEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPAFRedistMode"),
    (0, "SLE-BGP-MIB", "sleBGPAFRedistType"),
    (0, "SLE-BGP-MIB", "sleBGPAFRedistProtoType"),
)
if mibBuilder.loadTexts:
    sleBGPAFRedistEntry.setStatus("current")


class _SleBGPAFRedistMode_Type(Integer32):
    """Custom type sleBGPAFRedistMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFRedistMode_Type.__name__ = "Integer32"
_SleBGPAFRedistMode_Object = MibTableColumn
sleBGPAFRedistMode = _SleBGPAFRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 1, 1, 1),
    _SleBGPAFRedistMode_Type()
)
sleBGPAFRedistMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFRedistMode.setStatus("current")


class _SleBGPAFRedistType_Type(Integer32):
    """Custom type sleBGPAFRedistType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SleBGPAFRedistType_Type.__name__ = "Integer32"
_SleBGPAFRedistType_Object = MibTableColumn
sleBGPAFRedistType = _SleBGPAFRedistType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 1, 1, 2),
    _SleBGPAFRedistType_Type()
)
sleBGPAFRedistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFRedistType.setStatus("current")


class _SleBGPAFRedistProtoType_Type(Integer32):
    """Custom type sleBGPAFRedistProtoType based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("ospf", 5))
    )


_SleBGPAFRedistProtoType_Type.__name__ = "Integer32"
_SleBGPAFRedistProtoType_Object = MibTableColumn
sleBGPAFRedistProtoType = _SleBGPAFRedistProtoType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 1, 1, 3),
    _SleBGPAFRedistProtoType_Type()
)
sleBGPAFRedistProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFRedistProtoType.setStatus("current")


class _SleBGPAFRedistRoutemapName_Type(OctetString):
    """Custom type sleBGPAFRedistRoutemapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFRedistRoutemapName_Type.__name__ = "OctetString"
_SleBGPAFRedistRoutemapName_Object = MibTableColumn
sleBGPAFRedistRoutemapName = _SleBGPAFRedistRoutemapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 1, 1, 4),
    _SleBGPAFRedistRoutemapName_Type()
)
sleBGPAFRedistRoutemapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFRedistRoutemapName.setStatus("current")
_SleBGPAFRedistControl_ObjectIdentity = ObjectIdentity
sleBGPAFRedistControl = _SleBGPAFRedistControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2)
)


class _SleBGPAFRedistControlRequest_Type(Integer32):
    """Custom type sleBGPAFRedistControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createBGPAFRedistribute", 1),
          ("deleteBGPAFRedistribute", 2),
          ("setBGPAFRedistribute", 3))
    )


_SleBGPAFRedistControlRequest_Type.__name__ = "Integer32"
_SleBGPAFRedistControlRequest_Object = MibScalar
sleBGPAFRedistControlRequest = _SleBGPAFRedistControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 1),
    _SleBGPAFRedistControlRequest_Type()
)
sleBGPAFRedistControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlRequest.setStatus("current")
_SleBGPAFRedistControlStatus_Type = SleControlStatusType
_SleBGPAFRedistControlStatus_Object = MibScalar
sleBGPAFRedistControlStatus = _SleBGPAFRedistControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 2),
    _SleBGPAFRedistControlStatus_Type()
)
sleBGPAFRedistControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlStatus.setStatus("current")
_SleBGPAFRedistControlTimer_Type = Gauge32
_SleBGPAFRedistControlTimer_Object = MibScalar
sleBGPAFRedistControlTimer = _SleBGPAFRedistControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 3),
    _SleBGPAFRedistControlTimer_Type()
)
sleBGPAFRedistControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlTimer.setStatus("current")
_SleBGPAFRedistControlTimeStamp_Type = TimeTicks
_SleBGPAFRedistControlTimeStamp_Object = MibScalar
sleBGPAFRedistControlTimeStamp = _SleBGPAFRedistControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 4),
    _SleBGPAFRedistControlTimeStamp_Type()
)
sleBGPAFRedistControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlTimeStamp.setStatus("current")
_SleBGPAFRedistControlReqResult_Type = SleControlRequestResultType
_SleBGPAFRedistControlReqResult_Object = MibScalar
sleBGPAFRedistControlReqResult = _SleBGPAFRedistControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 5),
    _SleBGPAFRedistControlReqResult_Type()
)
sleBGPAFRedistControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlReqResult.setStatus("current")


class _SleBGPAFRedistControlMode_Type(Integer32):
    """Custom type sleBGPAFRedistControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFRedistControlMode_Type.__name__ = "Integer32"
_SleBGPAFRedistControlMode_Object = MibScalar
sleBGPAFRedistControlMode = _SleBGPAFRedistControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 6),
    _SleBGPAFRedistControlMode_Type()
)
sleBGPAFRedistControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlMode.setStatus("current")


class _SleBGPAFRedistControlType_Type(Integer32):
    """Custom type sleBGPAFRedistControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SleBGPAFRedistControlType_Type.__name__ = "Integer32"
_SleBGPAFRedistControlType_Object = MibScalar
sleBGPAFRedistControlType = _SleBGPAFRedistControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 7),
    _SleBGPAFRedistControlType_Type()
)
sleBGPAFRedistControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlType.setStatus("current")


class _SleBGPAFRedistControlProtoType_Type(Integer32):
    """Custom type sleBGPAFRedistControlProtoType based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("ospf", 5))
    )


_SleBGPAFRedistControlProtoType_Type.__name__ = "Integer32"
_SleBGPAFRedistControlProtoType_Object = MibScalar
sleBGPAFRedistControlProtoType = _SleBGPAFRedistControlProtoType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 8),
    _SleBGPAFRedistControlProtoType_Type()
)
sleBGPAFRedistControlProtoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlProtoType.setStatus("current")


class _SleBGPAFRedistControlRoutemapName_Type(OctetString):
    """Custom type sleBGPAFRedistControlRoutemapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFRedistControlRoutemapName_Type.__name__ = "OctetString"
_SleBGPAFRedistControlRoutemapName_Object = MibScalar
sleBGPAFRedistControlRoutemapName = _SleBGPAFRedistControlRoutemapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 2, 9),
    _SleBGPAFRedistControlRoutemapName_Type()
)
sleBGPAFRedistControlRoutemapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFRedistControlRoutemapName.setStatus("current")
_SleBGPAFRedistNotification_ObjectIdentity = ObjectIdentity
sleBGPAFRedistNotification = _SleBGPAFRedistNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 3)
)
_SleBGPAFAggreAddr_ObjectIdentity = ObjectIdentity
sleBGPAFAggreAddr = _SleBGPAFAggreAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3)
)
_SleBGPAFAggreAddrTable_Object = MibTable
sleBGPAFAggreAddrTable = _SleBGPAFAggreAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 1)
)
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrTable.setStatus("current")
_SleBGPAFAggreAddrEntry_Object = MibTableRow
sleBGPAFAggreAddrEntry = _SleBGPAFAggreAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 1, 1)
)
sleBGPAFAggreAddrEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPAFAggreAddrMode"),
    (0, "SLE-BGP-MIB", "sleBGPAFAggreAddrType"),
    (0, "SLE-BGP-MIB", "sleBGPAFAggreAddrPrefix"),
)
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrEntry.setStatus("current")


class _SleBGPAFAggreAddrMode_Type(Integer32):
    """Custom type sleBGPAFAggreAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFAggreAddrMode_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrMode_Object = MibTableColumn
sleBGPAFAggreAddrMode = _SleBGPAFAggreAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 1, 1, 1),
    _SleBGPAFAggreAddrMode_Type()
)
sleBGPAFAggreAddrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrMode.setStatus("current")


class _SleBGPAFAggreAddrType_Type(Integer32):
    """Custom type sleBGPAFAggreAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SleBGPAFAggreAddrType_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrType_Object = MibTableColumn
sleBGPAFAggreAddrType = _SleBGPAFAggreAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 1, 1, 2),
    _SleBGPAFAggreAddrType_Type()
)
sleBGPAFAggreAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrType.setStatus("current")
_SleBGPAFAggreAddrPrefix_Type = OctetString
_SleBGPAFAggreAddrPrefix_Object = MibTableColumn
sleBGPAFAggreAddrPrefix = _SleBGPAFAggreAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 1, 1, 3),
    _SleBGPAFAggreAddrPrefix_Type()
)
sleBGPAFAggreAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrPrefix.setStatus("current")


class _SleBGPAFAggreAddrAsSet_Type(Integer32):
    """Custom type sleBGPAFAggreAddrAsSet based on Integer32"""
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


_SleBGPAFAggreAddrAsSet_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrAsSet_Object = MibTableColumn
sleBGPAFAggreAddrAsSet = _SleBGPAFAggreAddrAsSet_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 1, 1, 4),
    _SleBGPAFAggreAddrAsSet_Type()
)
sleBGPAFAggreAddrAsSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrAsSet.setStatus("current")


class _SleBGPAFAggreAddrSummOnly_Type(Integer32):
    """Custom type sleBGPAFAggreAddrSummOnly based on Integer32"""
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


_SleBGPAFAggreAddrSummOnly_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrSummOnly_Object = MibTableColumn
sleBGPAFAggreAddrSummOnly = _SleBGPAFAggreAddrSummOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 1, 1, 5),
    _SleBGPAFAggreAddrSummOnly_Type()
)
sleBGPAFAggreAddrSummOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrSummOnly.setStatus("current")
_SleBGPAFAggreAddrControl_ObjectIdentity = ObjectIdentity
sleBGPAFAggreAddrControl = _SleBGPAFAggreAddrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2)
)


class _SleBGPAFAggreAddrControlRequest_Type(Integer32):
    """Custom type sleBGPAFAggreAddrControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createBGPAFAggreAddress", 1),
          ("deleteBGPAFAggreAddress", 2))
    )


_SleBGPAFAggreAddrControlRequest_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrControlRequest_Object = MibScalar
sleBGPAFAggreAddrControlRequest = _SleBGPAFAggreAddrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 1),
    _SleBGPAFAggreAddrControlRequest_Type()
)
sleBGPAFAggreAddrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlRequest.setStatus("current")
_SleBGPAFAggreAddrControlStatus_Type = SleControlStatusType
_SleBGPAFAggreAddrControlStatus_Object = MibScalar
sleBGPAFAggreAddrControlStatus = _SleBGPAFAggreAddrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 2),
    _SleBGPAFAggreAddrControlStatus_Type()
)
sleBGPAFAggreAddrControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlStatus.setStatus("current")
_SleBGPAFAggreAddrControlTimer_Type = Gauge32
_SleBGPAFAggreAddrControlTimer_Object = MibScalar
sleBGPAFAggreAddrControlTimer = _SleBGPAFAggreAddrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 3),
    _SleBGPAFAggreAddrControlTimer_Type()
)
sleBGPAFAggreAddrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlTimer.setStatus("current")
_SleBGPAFAggreAddrControlTimeStamp_Type = TimeTicks
_SleBGPAFAggreAddrControlTimeStamp_Object = MibScalar
sleBGPAFAggreAddrControlTimeStamp = _SleBGPAFAggreAddrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 4),
    _SleBGPAFAggreAddrControlTimeStamp_Type()
)
sleBGPAFAggreAddrControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlTimeStamp.setStatus("current")
_SleBGPAFAggreAddrControlReqResult_Type = SleControlRequestResultType
_SleBGPAFAggreAddrControlReqResult_Object = MibScalar
sleBGPAFAggreAddrControlReqResult = _SleBGPAFAggreAddrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 5),
    _SleBGPAFAggreAddrControlReqResult_Type()
)
sleBGPAFAggreAddrControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlReqResult.setStatus("current")


class _SleBGPAFAggreAddrControlMode_Type(Integer32):
    """Custom type sleBGPAFAggreAddrControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFAggreAddrControlMode_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrControlMode_Object = MibScalar
sleBGPAFAggreAddrControlMode = _SleBGPAFAggreAddrControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 6),
    _SleBGPAFAggreAddrControlMode_Type()
)
sleBGPAFAggreAddrControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlMode.setStatus("current")


class _SleBGPAFAggreAddrControlType_Type(Integer32):
    """Custom type sleBGPAFAggreAddrControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SleBGPAFAggreAddrControlType_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrControlType_Object = MibScalar
sleBGPAFAggreAddrControlType = _SleBGPAFAggreAddrControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 7),
    _SleBGPAFAggreAddrControlType_Type()
)
sleBGPAFAggreAddrControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlType.setStatus("current")
_SleBGPAFAggreAddrControlAddrPrefix_Type = OctetString
_SleBGPAFAggreAddrControlAddrPrefix_Object = MibScalar
sleBGPAFAggreAddrControlAddrPrefix = _SleBGPAFAggreAddrControlAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 8),
    _SleBGPAFAggreAddrControlAddrPrefix_Type()
)
sleBGPAFAggreAddrControlAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlAddrPrefix.setStatus("current")


class _SleBGPAFAggreAddrControlAsSet_Type(Integer32):
    """Custom type sleBGPAFAggreAddrControlAsSet based on Integer32"""
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


_SleBGPAFAggreAddrControlAsSet_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrControlAsSet_Object = MibScalar
sleBGPAFAggreAddrControlAsSet = _SleBGPAFAggreAddrControlAsSet_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 9),
    _SleBGPAFAggreAddrControlAsSet_Type()
)
sleBGPAFAggreAddrControlAsSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlAsSet.setStatus("current")


class _SleBGPAFAggreAddrControlSummOnly_Type(Integer32):
    """Custom type sleBGPAFAggreAddrControlSummOnly based on Integer32"""
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


_SleBGPAFAggreAddrControlSummOnly_Type.__name__ = "Integer32"
_SleBGPAFAggreAddrControlSummOnly_Object = MibScalar
sleBGPAFAggreAddrControlSummOnly = _SleBGPAFAggreAddrControlSummOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 2, 10),
    _SleBGPAFAggreAddrControlSummOnly_Type()
)
sleBGPAFAggreAddrControlSummOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFAggreAddrControlSummOnly.setStatus("current")
_SleBGPAFAggreAddrNotification_ObjectIdentity = ObjectIdentity
sleBGPAFAggreAddrNotification = _SleBGPAFAggreAddrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 3)
)
_SleBGPAFPeerInfo_ObjectIdentity = ObjectIdentity
sleBGPAFPeerInfo = _SleBGPAFPeerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4)
)
_SleBGPAFPeer_ObjectIdentity = ObjectIdentity
sleBGPAFPeer = _SleBGPAFPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1)
)
_SleBGPAFPeerTable_Object = MibTable
sleBGPAFPeerTable = _SleBGPAFPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleBGPAFPeerTable.setStatus("current")
_SleBGPAFPeerEntry_Object = MibTableRow
sleBGPAFPeerEntry = _SleBGPAFPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1)
)
sleBGPAFPeerEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPAFPeerMode"),
    (0, "SLE-BGP-MIB", "sleBGPAFPeerType"),
    (0, "SLE-BGP-MIB", "sleBGPAFPeerName"),
)
if mibBuilder.loadTexts:
    sleBGPAFPeerEntry.setStatus("current")


class _SleBGPAFPeerMode_Type(Integer32):
    """Custom type sleBGPAFPeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("vpn4", 3))
    )


_SleBGPAFPeerMode_Type.__name__ = "Integer32"
_SleBGPAFPeerMode_Object = MibTableColumn
sleBGPAFPeerMode = _SleBGPAFPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 1),
    _SleBGPAFPeerMode_Type()
)
sleBGPAFPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerMode.setStatus("current")


class _SleBGPAFPeerType_Type(Integer32):
    """Custom type sleBGPAFPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("vrf", 3))
    )


_SleBGPAFPeerType_Type.__name__ = "Integer32"
_SleBGPAFPeerType_Object = MibTableColumn
sleBGPAFPeerType = _SleBGPAFPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 2),
    _SleBGPAFPeerType_Type()
)
sleBGPAFPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerType.setStatus("current")
_SleBGPAFPeerName_Type = OctetString
_SleBGPAFPeerName_Object = MibTableColumn
sleBGPAFPeerName = _SleBGPAFPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 3),
    _SleBGPAFPeerName_Type()
)
sleBGPAFPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerName.setStatus("current")


class _SleBGPAFPeerActviate_Type(Integer32):
    """Custom type sleBGPAFPeerActviate based on Integer32"""
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


_SleBGPAFPeerActviate_Type.__name__ = "Integer32"
_SleBGPAFPeerActviate_Object = MibTableColumn
sleBGPAFPeerActviate = _SleBGPAFPeerActviate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 4),
    _SleBGPAFPeerActviate_Type()
)
sleBGPAFPeerActviate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerActviate.setStatus("current")


class _SleBGPAFPeerAllowAsIn_Type(Integer32):
    """Custom type sleBGPAFPeerAllowAsIn based on Integer32"""
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


_SleBGPAFPeerAllowAsIn_Type.__name__ = "Integer32"
_SleBGPAFPeerAllowAsIn_Object = MibTableColumn
sleBGPAFPeerAllowAsIn = _SleBGPAFPeerAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 5),
    _SleBGPAFPeerAllowAsIn_Type()
)
sleBGPAFPeerAllowAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerAllowAsIn.setStatus("current")


class _SleBGPAFPeerAllowAsInNum_Type(Integer32):
    """Custom type sleBGPAFPeerAllowAsInNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SleBGPAFPeerAllowAsInNum_Type.__name__ = "Integer32"
_SleBGPAFPeerAllowAsInNum_Object = MibTableColumn
sleBGPAFPeerAllowAsInNum = _SleBGPAFPeerAllowAsInNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 6),
    _SleBGPAFPeerAllowAsInNum_Type()
)
sleBGPAFPeerAllowAsInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerAllowAsInNum.setStatus("current")


class _SleBGPAFPeerAttrUnchangedAsPath_Type(Integer32):
    """Custom type sleBGPAFPeerAttrUnchangedAsPath based on Integer32"""
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


_SleBGPAFPeerAttrUnchangedAsPath_Type.__name__ = "Integer32"
_SleBGPAFPeerAttrUnchangedAsPath_Object = MibTableColumn
sleBGPAFPeerAttrUnchangedAsPath = _SleBGPAFPeerAttrUnchangedAsPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 7),
    _SleBGPAFPeerAttrUnchangedAsPath_Type()
)
sleBGPAFPeerAttrUnchangedAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerAttrUnchangedAsPath.setStatus("current")


class _SleBGPAFPeerAttrUnchangedMed_Type(Integer32):
    """Custom type sleBGPAFPeerAttrUnchangedMed based on Integer32"""
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


_SleBGPAFPeerAttrUnchangedMed_Type.__name__ = "Integer32"
_SleBGPAFPeerAttrUnchangedMed_Object = MibTableColumn
sleBGPAFPeerAttrUnchangedMed = _SleBGPAFPeerAttrUnchangedMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 8),
    _SleBGPAFPeerAttrUnchangedMed_Type()
)
sleBGPAFPeerAttrUnchangedMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerAttrUnchangedMed.setStatus("current")


class _SleBGPAFPeerAttrUnchangedNexthop_Type(Integer32):
    """Custom type sleBGPAFPeerAttrUnchangedNexthop based on Integer32"""
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


_SleBGPAFPeerAttrUnchangedNexthop_Type.__name__ = "Integer32"
_SleBGPAFPeerAttrUnchangedNexthop_Object = MibTableColumn
sleBGPAFPeerAttrUnchangedNexthop = _SleBGPAFPeerAttrUnchangedNexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 9),
    _SleBGPAFPeerAttrUnchangedNexthop_Type()
)
sleBGPAFPeerAttrUnchangedNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerAttrUnchangedNexthop.setStatus("current")


class _SleBGPAFPeerCapGracefulRestart_Type(Integer32):
    """Custom type sleBGPAFPeerCapGracefulRestart based on Integer32"""
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


_SleBGPAFPeerCapGracefulRestart_Type.__name__ = "Integer32"
_SleBGPAFPeerCapGracefulRestart_Object = MibTableColumn
sleBGPAFPeerCapGracefulRestart = _SleBGPAFPeerCapGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 10),
    _SleBGPAFPeerCapGracefulRestart_Type()
)
sleBGPAFPeerCapGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerCapGracefulRestart.setStatus("current")


class _SleBGPAFPeerCapOrfMode_Type(Integer32):
    """Custom type sleBGPAFPeerCapOrfMode based on Integer32"""
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
        *(("disable", 0),
          ("send", 1),
          ("recevie", 2),
          ("both", 3))
    )


_SleBGPAFPeerCapOrfMode_Type.__name__ = "Integer32"
_SleBGPAFPeerCapOrfMode_Object = MibTableColumn
sleBGPAFPeerCapOrfMode = _SleBGPAFPeerCapOrfMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 11),
    _SleBGPAFPeerCapOrfMode_Type()
)
sleBGPAFPeerCapOrfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerCapOrfMode.setStatus("current")


class _SleBGPAFPeerDefOriginate_Type(Integer32):
    """Custom type sleBGPAFPeerDefOriginate based on Integer32"""
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


_SleBGPAFPeerDefOriginate_Type.__name__ = "Integer32"
_SleBGPAFPeerDefOriginate_Object = MibTableColumn
sleBGPAFPeerDefOriginate = _SleBGPAFPeerDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 12),
    _SleBGPAFPeerDefOriginate_Type()
)
sleBGPAFPeerDefOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerDefOriginate.setStatus("current")


class _SleBGPAFPeerDefOriginateRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerDefOriginateRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerDefOriginateRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerDefOriginateRoutemap_Object = MibTableColumn
sleBGPAFPeerDefOriginateRoutemap = _SleBGPAFPeerDefOriginateRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 13),
    _SleBGPAFPeerDefOriginateRoutemap_Type()
)
sleBGPAFPeerDefOriginateRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerDefOriginateRoutemap.setStatus("current")


class _SleBGPAFPeerFLInAccName_Type(OctetString):
    """Custom type sleBGPAFPeerFLInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerFLInAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerFLInAccName_Object = MibTableColumn
sleBGPAFPeerFLInAccName = _SleBGPAFPeerFLInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 14),
    _SleBGPAFPeerFLInAccName_Type()
)
sleBGPAFPeerFLInAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerFLInAccName.setStatus("current")


class _SleBGPAFPeerFLOutAccName_Type(OctetString):
    """Custom type sleBGPAFPeerFLOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerFLOutAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerFLOutAccName_Object = MibTableColumn
sleBGPAFPeerFLOutAccName = _SleBGPAFPeerFLOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 15),
    _SleBGPAFPeerFLOutAccName_Type()
)
sleBGPAFPeerFLOutAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerFLOutAccName.setStatus("current")


class _SleBGPAFPeerMaxPrefixNum_Type(Gauge32):
    """Custom type sleBGPAFPeerMaxPrefixNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleBGPAFPeerMaxPrefixNum_Type.__name__ = "Gauge32"
_SleBGPAFPeerMaxPrefixNum_Object = MibTableColumn
sleBGPAFPeerMaxPrefixNum = _SleBGPAFPeerMaxPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 16),
    _SleBGPAFPeerMaxPrefixNum_Type()
)
sleBGPAFPeerMaxPrefixNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerMaxPrefixNum.setStatus("current")


class _SleBGPAFPeerMaxPrefixThreshold_Type(Integer32):
    """Custom type sleBGPAFPeerMaxPrefixThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleBGPAFPeerMaxPrefixThreshold_Type.__name__ = "Integer32"
_SleBGPAFPeerMaxPrefixThreshold_Object = MibTableColumn
sleBGPAFPeerMaxPrefixThreshold = _SleBGPAFPeerMaxPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 17),
    _SleBGPAFPeerMaxPrefixThreshold_Type()
)
sleBGPAFPeerMaxPrefixThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerMaxPrefixThreshold.setStatus("current")


class _SleBGPAFPeerMaxPrefixWarnOnly_Type(Integer32):
    """Custom type sleBGPAFPeerMaxPrefixWarnOnly based on Integer32"""
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


_SleBGPAFPeerMaxPrefixWarnOnly_Type.__name__ = "Integer32"
_SleBGPAFPeerMaxPrefixWarnOnly_Object = MibTableColumn
sleBGPAFPeerMaxPrefixWarnOnly = _SleBGPAFPeerMaxPrefixWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 18),
    _SleBGPAFPeerMaxPrefixWarnOnly_Type()
)
sleBGPAFPeerMaxPrefixWarnOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerMaxPrefixWarnOnly.setStatus("current")


class _SleBGPAFPeerRemotePrivateAs_Type(Integer32):
    """Custom type sleBGPAFPeerRemotePrivateAs based on Integer32"""
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


_SleBGPAFPeerRemotePrivateAs_Type.__name__ = "Integer32"
_SleBGPAFPeerRemotePrivateAs_Object = MibTableColumn
sleBGPAFPeerRemotePrivateAs = _SleBGPAFPeerRemotePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 19),
    _SleBGPAFPeerRemotePrivateAs_Type()
)
sleBGPAFPeerRemotePrivateAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerRemotePrivateAs.setStatus("current")


class _SleBGPAFPeerInRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerInRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerInRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerInRoutemap_Object = MibTableColumn
sleBGPAFPeerInRoutemap = _SleBGPAFPeerInRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 20),
    _SleBGPAFPeerInRoutemap_Type()
)
sleBGPAFPeerInRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerInRoutemap.setStatus("current")


class _SleBGPAFPeerOutRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerOutRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerOutRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerOutRoutemap_Object = MibTableColumn
sleBGPAFPeerOutRoutemap = _SleBGPAFPeerOutRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 21),
    _SleBGPAFPeerOutRoutemap_Type()
)
sleBGPAFPeerOutRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerOutRoutemap.setStatus("current")


class _SleBGPAFPeerRouteReflectClient_Type(Integer32):
    """Custom type sleBGPAFPeerRouteReflectClient based on Integer32"""
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


_SleBGPAFPeerRouteReflectClient_Type.__name__ = "Integer32"
_SleBGPAFPeerRouteReflectClient_Object = MibTableColumn
sleBGPAFPeerRouteReflectClient = _SleBGPAFPeerRouteReflectClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 22),
    _SleBGPAFPeerRouteReflectClient_Type()
)
sleBGPAFPeerRouteReflectClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerRouteReflectClient.setStatus("current")


class _SleBGPAFPeerRouteServerClient_Type(Integer32):
    """Custom type sleBGPAFPeerRouteServerClient based on Integer32"""
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


_SleBGPAFPeerRouteServerClient_Type.__name__ = "Integer32"
_SleBGPAFPeerRouteServerClient_Object = MibTableColumn
sleBGPAFPeerRouteServerClient = _SleBGPAFPeerRouteServerClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 23),
    _SleBGPAFPeerRouteServerClient_Type()
)
sleBGPAFPeerRouteServerClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerRouteServerClient.setStatus("current")


class _SleBGPAFPeerInDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerInDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerInDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerInDistListName_Object = MibTableColumn
sleBGPAFPeerInDistListName = _SleBGPAFPeerInDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 24),
    _SleBGPAFPeerInDistListName_Type()
)
sleBGPAFPeerInDistListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerInDistListName.setStatus("current")


class _SleBGPAFPeerOutDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerOutDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerOutDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerOutDistListName_Object = MibTableColumn
sleBGPAFPeerOutDistListName = _SleBGPAFPeerOutDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 25),
    _SleBGPAFPeerOutDistListName_Type()
)
sleBGPAFPeerOutDistListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerOutDistListName.setStatus("current")


class _SleBGPAFPeerInPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerInPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerInPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerInPrefixListName_Object = MibTableColumn
sleBGPAFPeerInPrefixListName = _SleBGPAFPeerInPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 26),
    _SleBGPAFPeerInPrefixListName_Type()
)
sleBGPAFPeerInPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerInPrefixListName.setStatus("current")


class _SleBGPAFPeerOutPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerOutPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerOutPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerOutPrefixListName_Object = MibTableColumn
sleBGPAFPeerOutPrefixListName = _SleBGPAFPeerOutPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 27),
    _SleBGPAFPeerOutPrefixListName_Type()
)
sleBGPAFPeerOutPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerOutPrefixListName.setStatus("current")


class _SleBGPAFPeerSendCommunity_Type(Integer32):
    """Custom type sleBGPAFPeerSendCommunity based on Integer32"""
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
        *(("disable", 0),
          ("standard", 1),
          ("extended", 2),
          ("both", 3))
    )


_SleBGPAFPeerSendCommunity_Type.__name__ = "Integer32"
_SleBGPAFPeerSendCommunity_Object = MibTableColumn
sleBGPAFPeerSendCommunity = _SleBGPAFPeerSendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 28),
    _SleBGPAFPeerSendCommunity_Type()
)
sleBGPAFPeerSendCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerSendCommunity.setStatus("current")


class _SleBGPAFPeerNexthopSelf_Type(Integer32):
    """Custom type sleBGPAFPeerNexthopSelf based on Integer32"""
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


_SleBGPAFPeerNexthopSelf_Type.__name__ = "Integer32"
_SleBGPAFPeerNexthopSelf_Object = MibTableColumn
sleBGPAFPeerNexthopSelf = _SleBGPAFPeerNexthopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 29),
    _SleBGPAFPeerNexthopSelf_Type()
)
sleBGPAFPeerNexthopSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerNexthopSelf.setStatus("current")


class _SleBGPAFPeerSoftReconfig_Type(Integer32):
    """Custom type sleBGPAFPeerSoftReconfig based on Integer32"""
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


_SleBGPAFPeerSoftReconfig_Type.__name__ = "Integer32"
_SleBGPAFPeerSoftReconfig_Object = MibTableColumn
sleBGPAFPeerSoftReconfig = _SleBGPAFPeerSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 30),
    _SleBGPAFPeerSoftReconfig_Type()
)
sleBGPAFPeerSoftReconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerSoftReconfig.setStatus("current")


class _SleBGPAFPeerUnsuppressMapName_Type(OctetString):
    """Custom type sleBGPAFPeerUnsuppressMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerUnsuppressMapName_Type.__name__ = "OctetString"
_SleBGPAFPeerUnsuppressMapName_Object = MibTableColumn
sleBGPAFPeerUnsuppressMapName = _SleBGPAFPeerUnsuppressMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 1, 1, 31),
    _SleBGPAFPeerUnsuppressMapName_Type()
)
sleBGPAFPeerUnsuppressMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerUnsuppressMapName.setStatus("current")
_SleBGPAFPeerControl_ObjectIdentity = ObjectIdentity
sleBGPAFPeerControl = _SleBGPAFPeerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2)
)


class _SleBGPAFPeerControlRequest_Type(Integer32):
    """Custom type sleBGPAFPeerControlRequest based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("setBGPAFPeerActivate", 1),
          ("setBGPAFPeerAllowAsInProfile", 2),
          ("setBGPAFPeerAttrUnchangedProfile", 3),
          ("setBGPAFPeerCapGracefulRestart", 4),
          ("setBGPAFPeerCapOrfMode", 5),
          ("setBGPAFPeerDefaultOriginate", 6),
          ("setBGPAFPeerFLInAccName", 7),
          ("unsetBGPAFPeerFLInAccName", 8),
          ("setBGPAFPeerFLOutAccName", 9),
          ("unsetBGPAFPeerFLOutAccName", 10),
          ("setBGPAFPeerMaxPrefixProfile", 11),
          ("setBGPAFPeerRemotePrivateAs", 12),
          ("setBGPAFPeerInRoutemap", 13),
          ("unsetBGPAFPeerInRoutemap", 14),
          ("setBGPAFPeerOutRoutemap", 15),
          ("unsetBGPAFPeerOutRoutemap", 16),
          ("setBGPAFPeerRouteReflectClient", 17),
          ("setBGPAFPeerRouteServerClient", 18),
          ("setBGPAFPeerSendCommunity", 19),
          ("setBGPAFPeerNexthopSelf", 20),
          ("setBGPAFPeerSoftReconfig", 21),
          ("setBGPAFPeerUnsupressMapName", 22),
          ("unsetBGPAFPeerUnsupressMapName", 23),
          ("setBGPAFPeerInDistListName", 24),
          ("unsetBGPAFPeerInDistListName", 25),
          ("setBGPAFPeerOutDistListName", 26),
          ("unsetBGPAFPeerOutDistListName", 27),
          ("setBGPAFPeerInPrefixListName", 28),
          ("unsetBGPAFPeerInPrefixListName", 29),
          ("setBGPAFPeerOutPrefixListName", 30),
          ("unsetBGPAFPeerOutPrefixListName", 31))
    )


_SleBGPAFPeerControlRequest_Type.__name__ = "Integer32"
_SleBGPAFPeerControlRequest_Object = MibScalar
sleBGPAFPeerControlRequest = _SleBGPAFPeerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 1),
    _SleBGPAFPeerControlRequest_Type()
)
sleBGPAFPeerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlRequest.setStatus("current")
_SleBGPAFPeerControlStatus_Type = SleControlStatusType
_SleBGPAFPeerControlStatus_Object = MibScalar
sleBGPAFPeerControlStatus = _SleBGPAFPeerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 2),
    _SleBGPAFPeerControlStatus_Type()
)
sleBGPAFPeerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlStatus.setStatus("current")
_SleBGPAFPeerControlTimer_Type = Gauge32
_SleBGPAFPeerControlTimer_Object = MibScalar
sleBGPAFPeerControlTimer = _SleBGPAFPeerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 3),
    _SleBGPAFPeerControlTimer_Type()
)
sleBGPAFPeerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlTimer.setStatus("current")
_SleBGPAFPeerControlTimeStamp_Type = TimeTicks
_SleBGPAFPeerControlTimeStamp_Object = MibScalar
sleBGPAFPeerControlTimeStamp = _SleBGPAFPeerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 4),
    _SleBGPAFPeerControlTimeStamp_Type()
)
sleBGPAFPeerControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlTimeStamp.setStatus("current")
_SleBGPAFPeerControlReqResult_Type = SleControlRequestResultType
_SleBGPAFPeerControlReqResult_Object = MibScalar
sleBGPAFPeerControlReqResult = _SleBGPAFPeerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 5),
    _SleBGPAFPeerControlReqResult_Type()
)
sleBGPAFPeerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlReqResult.setStatus("current")


class _SleBGPAFPeerControlMode_Type(Integer32):
    """Custom type sleBGPAFPeerControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("vpn4", 3))
    )


_SleBGPAFPeerControlMode_Type.__name__ = "Integer32"
_SleBGPAFPeerControlMode_Object = MibScalar
sleBGPAFPeerControlMode = _SleBGPAFPeerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 6),
    _SleBGPAFPeerControlMode_Type()
)
sleBGPAFPeerControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlMode.setStatus("current")


class _SleBGPAFPeerControlType_Type(Integer32):
    """Custom type sleBGPAFPeerControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("vrf", 3))
    )


_SleBGPAFPeerControlType_Type.__name__ = "Integer32"
_SleBGPAFPeerControlType_Object = MibScalar
sleBGPAFPeerControlType = _SleBGPAFPeerControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 7),
    _SleBGPAFPeerControlType_Type()
)
sleBGPAFPeerControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlType.setStatus("current")
_SleBGPAFPeerControlName_Type = OctetString
_SleBGPAFPeerControlName_Object = MibScalar
sleBGPAFPeerControlName = _SleBGPAFPeerControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 8),
    _SleBGPAFPeerControlName_Type()
)
sleBGPAFPeerControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlName.setStatus("current")


class _SleBGPAFPeerControlActviate_Type(Integer32):
    """Custom type sleBGPAFPeerControlActviate based on Integer32"""
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


_SleBGPAFPeerControlActviate_Type.__name__ = "Integer32"
_SleBGPAFPeerControlActviate_Object = MibScalar
sleBGPAFPeerControlActviate = _SleBGPAFPeerControlActviate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 9),
    _SleBGPAFPeerControlActviate_Type()
)
sleBGPAFPeerControlActviate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlActviate.setStatus("current")


class _SleBGPAFPeerControlAllowAsIn_Type(Integer32):
    """Custom type sleBGPAFPeerControlAllowAsIn based on Integer32"""
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


_SleBGPAFPeerControlAllowAsIn_Type.__name__ = "Integer32"
_SleBGPAFPeerControlAllowAsIn_Object = MibScalar
sleBGPAFPeerControlAllowAsIn = _SleBGPAFPeerControlAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 10),
    _SleBGPAFPeerControlAllowAsIn_Type()
)
sleBGPAFPeerControlAllowAsIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlAllowAsIn.setStatus("current")


class _SleBGPAFPeerControlAllowAsInNum_Type(Integer32):
    """Custom type sleBGPAFPeerControlAllowAsInNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SleBGPAFPeerControlAllowAsInNum_Type.__name__ = "Integer32"
_SleBGPAFPeerControlAllowAsInNum_Object = MibScalar
sleBGPAFPeerControlAllowAsInNum = _SleBGPAFPeerControlAllowAsInNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 11),
    _SleBGPAFPeerControlAllowAsInNum_Type()
)
sleBGPAFPeerControlAllowAsInNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlAllowAsInNum.setStatus("current")


class _SleBGPAFPeerControlAttrUnchangedAsPath_Type(Integer32):
    """Custom type sleBGPAFPeerControlAttrUnchangedAsPath based on Integer32"""
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


_SleBGPAFPeerControlAttrUnchangedAsPath_Type.__name__ = "Integer32"
_SleBGPAFPeerControlAttrUnchangedAsPath_Object = MibScalar
sleBGPAFPeerControlAttrUnchangedAsPath = _SleBGPAFPeerControlAttrUnchangedAsPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 12),
    _SleBGPAFPeerControlAttrUnchangedAsPath_Type()
)
sleBGPAFPeerControlAttrUnchangedAsPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlAttrUnchangedAsPath.setStatus("current")


class _SleBGPAFPeerControlAttrUnchangedMed_Type(Integer32):
    """Custom type sleBGPAFPeerControlAttrUnchangedMed based on Integer32"""
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


_SleBGPAFPeerControlAttrUnchangedMed_Type.__name__ = "Integer32"
_SleBGPAFPeerControlAttrUnchangedMed_Object = MibScalar
sleBGPAFPeerControlAttrUnchangedMed = _SleBGPAFPeerControlAttrUnchangedMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 13),
    _SleBGPAFPeerControlAttrUnchangedMed_Type()
)
sleBGPAFPeerControlAttrUnchangedMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlAttrUnchangedMed.setStatus("current")


class _SleBGPAFPeerControlAttrUnchangedNexthop_Type(Integer32):
    """Custom type sleBGPAFPeerControlAttrUnchangedNexthop based on Integer32"""
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


_SleBGPAFPeerControlAttrUnchangedNexthop_Type.__name__ = "Integer32"
_SleBGPAFPeerControlAttrUnchangedNexthop_Object = MibScalar
sleBGPAFPeerControlAttrUnchangedNexthop = _SleBGPAFPeerControlAttrUnchangedNexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 14),
    _SleBGPAFPeerControlAttrUnchangedNexthop_Type()
)
sleBGPAFPeerControlAttrUnchangedNexthop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlAttrUnchangedNexthop.setStatus("current")


class _SleBGPAFPeerControlCapGracefulRestart_Type(Integer32):
    """Custom type sleBGPAFPeerControlCapGracefulRestart based on Integer32"""
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


_SleBGPAFPeerControlCapGracefulRestart_Type.__name__ = "Integer32"
_SleBGPAFPeerControlCapGracefulRestart_Object = MibScalar
sleBGPAFPeerControlCapGracefulRestart = _SleBGPAFPeerControlCapGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 15),
    _SleBGPAFPeerControlCapGracefulRestart_Type()
)
sleBGPAFPeerControlCapGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlCapGracefulRestart.setStatus("current")


class _SleBGPAFPeerControlCapOrfMode_Type(Integer32):
    """Custom type sleBGPAFPeerControlCapOrfMode based on Integer32"""
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
        *(("disable", 0),
          ("send", 1),
          ("receive", 2),
          ("both", 3))
    )


_SleBGPAFPeerControlCapOrfMode_Type.__name__ = "Integer32"
_SleBGPAFPeerControlCapOrfMode_Object = MibScalar
sleBGPAFPeerControlCapOrfMode = _SleBGPAFPeerControlCapOrfMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 16),
    _SleBGPAFPeerControlCapOrfMode_Type()
)
sleBGPAFPeerControlCapOrfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlCapOrfMode.setStatus("current")


class _SleBGPAFPeerControlDefOriginate_Type(Integer32):
    """Custom type sleBGPAFPeerControlDefOriginate based on Integer32"""
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


_SleBGPAFPeerControlDefOriginate_Type.__name__ = "Integer32"
_SleBGPAFPeerControlDefOriginate_Object = MibScalar
sleBGPAFPeerControlDefOriginate = _SleBGPAFPeerControlDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 17),
    _SleBGPAFPeerControlDefOriginate_Type()
)
sleBGPAFPeerControlDefOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlDefOriginate.setStatus("current")


class _SleBGPAFPeerControlDefOriginateRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerControlDefOriginateRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlDefOriginateRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerControlDefOriginateRoutemap_Object = MibScalar
sleBGPAFPeerControlDefOriginateRoutemap = _SleBGPAFPeerControlDefOriginateRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 18),
    _SleBGPAFPeerControlDefOriginateRoutemap_Type()
)
sleBGPAFPeerControlDefOriginateRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlDefOriginateRoutemap.setStatus("current")


class _SleBGPAFPeerControlFLInAccName_Type(OctetString):
    """Custom type sleBGPAFPeerControlFLInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlFLInAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerControlFLInAccName_Object = MibScalar
sleBGPAFPeerControlFLInAccName = _SleBGPAFPeerControlFLInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 19),
    _SleBGPAFPeerControlFLInAccName_Type()
)
sleBGPAFPeerControlFLInAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlFLInAccName.setStatus("current")


class _SleBGPAFPeerControlFLOutAccName_Type(OctetString):
    """Custom type sleBGPAFPeerControlFLOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlFLOutAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerControlFLOutAccName_Object = MibScalar
sleBGPAFPeerControlFLOutAccName = _SleBGPAFPeerControlFLOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 20),
    _SleBGPAFPeerControlFLOutAccName_Type()
)
sleBGPAFPeerControlFLOutAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlFLOutAccName.setStatus("current")


class _SleBGPAFPeerControlMaxPrefixNum_Type(Gauge32):
    """Custom type sleBGPAFPeerControlMaxPrefixNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPAFPeerControlMaxPrefixNum_Type.__name__ = "Gauge32"
_SleBGPAFPeerControlMaxPrefixNum_Object = MibScalar
sleBGPAFPeerControlMaxPrefixNum = _SleBGPAFPeerControlMaxPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 21),
    _SleBGPAFPeerControlMaxPrefixNum_Type()
)
sleBGPAFPeerControlMaxPrefixNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlMaxPrefixNum.setStatus("current")


class _SleBGPAFPeerControlMaxPrefixThreshold_Type(Integer32):
    """Custom type sleBGPAFPeerControlMaxPrefixThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleBGPAFPeerControlMaxPrefixThreshold_Type.__name__ = "Integer32"
_SleBGPAFPeerControlMaxPrefixThreshold_Object = MibScalar
sleBGPAFPeerControlMaxPrefixThreshold = _SleBGPAFPeerControlMaxPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 22),
    _SleBGPAFPeerControlMaxPrefixThreshold_Type()
)
sleBGPAFPeerControlMaxPrefixThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlMaxPrefixThreshold.setStatus("current")


class _SleBGPAFPeerControlMaxPrefixWarnOnly_Type(Integer32):
    """Custom type sleBGPAFPeerControlMaxPrefixWarnOnly based on Integer32"""
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


_SleBGPAFPeerControlMaxPrefixWarnOnly_Type.__name__ = "Integer32"
_SleBGPAFPeerControlMaxPrefixWarnOnly_Object = MibScalar
sleBGPAFPeerControlMaxPrefixWarnOnly = _SleBGPAFPeerControlMaxPrefixWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 23),
    _SleBGPAFPeerControlMaxPrefixWarnOnly_Type()
)
sleBGPAFPeerControlMaxPrefixWarnOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlMaxPrefixWarnOnly.setStatus("current")


class _SleBGPAFPeerControlRemotePrivateAs_Type(Integer32):
    """Custom type sleBGPAFPeerControlRemotePrivateAs based on Integer32"""
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


_SleBGPAFPeerControlRemotePrivateAs_Type.__name__ = "Integer32"
_SleBGPAFPeerControlRemotePrivateAs_Object = MibScalar
sleBGPAFPeerControlRemotePrivateAs = _SleBGPAFPeerControlRemotePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 24),
    _SleBGPAFPeerControlRemotePrivateAs_Type()
)
sleBGPAFPeerControlRemotePrivateAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlRemotePrivateAs.setStatus("current")


class _SleBGPAFPeerControlInRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerControlInRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlInRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerControlInRoutemap_Object = MibScalar
sleBGPAFPeerControlInRoutemap = _SleBGPAFPeerControlInRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 25),
    _SleBGPAFPeerControlInRoutemap_Type()
)
sleBGPAFPeerControlInRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlInRoutemap.setStatus("current")


class _SleBGPAFPeerControlOutRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerControlOutRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlOutRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerControlOutRoutemap_Object = MibScalar
sleBGPAFPeerControlOutRoutemap = _SleBGPAFPeerControlOutRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 26),
    _SleBGPAFPeerControlOutRoutemap_Type()
)
sleBGPAFPeerControlOutRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlOutRoutemap.setStatus("current")


class _SleBGPAFPeerControlRouteReflectClient_Type(Integer32):
    """Custom type sleBGPAFPeerControlRouteReflectClient based on Integer32"""
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


_SleBGPAFPeerControlRouteReflectClient_Type.__name__ = "Integer32"
_SleBGPAFPeerControlRouteReflectClient_Object = MibScalar
sleBGPAFPeerControlRouteReflectClient = _SleBGPAFPeerControlRouteReflectClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 27),
    _SleBGPAFPeerControlRouteReflectClient_Type()
)
sleBGPAFPeerControlRouteReflectClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlRouteReflectClient.setStatus("current")


class _SleBGPAFPeerControlRouteServerClient_Type(Integer32):
    """Custom type sleBGPAFPeerControlRouteServerClient based on Integer32"""
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


_SleBGPAFPeerControlRouteServerClient_Type.__name__ = "Integer32"
_SleBGPAFPeerControlRouteServerClient_Object = MibScalar
sleBGPAFPeerControlRouteServerClient = _SleBGPAFPeerControlRouteServerClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 28),
    _SleBGPAFPeerControlRouteServerClient_Type()
)
sleBGPAFPeerControlRouteServerClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlRouteServerClient.setStatus("current")


class _SleBGPAFPeerControlInDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerControlInDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlInDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerControlInDistListName_Object = MibScalar
sleBGPAFPeerControlInDistListName = _SleBGPAFPeerControlInDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 29),
    _SleBGPAFPeerControlInDistListName_Type()
)
sleBGPAFPeerControlInDistListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlInDistListName.setStatus("current")


class _SleBGPAFPeerControlOutDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerControlOutDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlOutDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerControlOutDistListName_Object = MibScalar
sleBGPAFPeerControlOutDistListName = _SleBGPAFPeerControlOutDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 30),
    _SleBGPAFPeerControlOutDistListName_Type()
)
sleBGPAFPeerControlOutDistListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlOutDistListName.setStatus("current")


class _SleBGPAFPeerControlInPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerControlInPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlInPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerControlInPrefixListName_Object = MibScalar
sleBGPAFPeerControlInPrefixListName = _SleBGPAFPeerControlInPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 31),
    _SleBGPAFPeerControlInPrefixListName_Type()
)
sleBGPAFPeerControlInPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlInPrefixListName.setStatus("current")


class _SleBGPAFPeerControlOutPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerControlOutPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlOutPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerControlOutPrefixListName_Object = MibScalar
sleBGPAFPeerControlOutPrefixListName = _SleBGPAFPeerControlOutPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 32),
    _SleBGPAFPeerControlOutPrefixListName_Type()
)
sleBGPAFPeerControlOutPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlOutPrefixListName.setStatus("current")


class _SleBGPAFPeerControlSendCommunity_Type(Integer32):
    """Custom type sleBGPAFPeerControlSendCommunity based on Integer32"""
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
        *(("disable", 0),
          ("standard", 1),
          ("extended", 2),
          ("both", 3))
    )


_SleBGPAFPeerControlSendCommunity_Type.__name__ = "Integer32"
_SleBGPAFPeerControlSendCommunity_Object = MibScalar
sleBGPAFPeerControlSendCommunity = _SleBGPAFPeerControlSendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 33),
    _SleBGPAFPeerControlSendCommunity_Type()
)
sleBGPAFPeerControlSendCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlSendCommunity.setStatus("current")


class _SleBGPAFPeerControlNexthopSelf_Type(Integer32):
    """Custom type sleBGPAFPeerControlNexthopSelf based on Integer32"""
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


_SleBGPAFPeerControlNexthopSelf_Type.__name__ = "Integer32"
_SleBGPAFPeerControlNexthopSelf_Object = MibScalar
sleBGPAFPeerControlNexthopSelf = _SleBGPAFPeerControlNexthopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 34),
    _SleBGPAFPeerControlNexthopSelf_Type()
)
sleBGPAFPeerControlNexthopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlNexthopSelf.setStatus("current")


class _SleBGPAFPeerControlSoftReconfig_Type(Integer32):
    """Custom type sleBGPAFPeerControlSoftReconfig based on Integer32"""
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


_SleBGPAFPeerControlSoftReconfig_Type.__name__ = "Integer32"
_SleBGPAFPeerControlSoftReconfig_Object = MibScalar
sleBGPAFPeerControlSoftReconfig = _SleBGPAFPeerControlSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 35),
    _SleBGPAFPeerControlSoftReconfig_Type()
)
sleBGPAFPeerControlSoftReconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlSoftReconfig.setStatus("current")


class _SleBGPAFPeerControlUnsuppressMapName_Type(OctetString):
    """Custom type sleBGPAFPeerControlUnsuppressMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerControlUnsuppressMapName_Type.__name__ = "OctetString"
_SleBGPAFPeerControlUnsuppressMapName_Object = MibScalar
sleBGPAFPeerControlUnsuppressMapName = _SleBGPAFPeerControlUnsuppressMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 2, 36),
    _SleBGPAFPeerControlUnsuppressMapName_Type()
)
sleBGPAFPeerControlUnsuppressMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerControlUnsuppressMapName.setStatus("current")
_SleBGPAFPeerNotification_ObjectIdentity = ObjectIdentity
sleBGPAFPeerNotification = _SleBGPAFPeerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3)
)
_SleBGPAFPeerGroup_ObjectIdentity = ObjectIdentity
sleBGPAFPeerGroup = _SleBGPAFPeerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2)
)
_SleBGPAFPeerGroupTable_Object = MibTable
sleBGPAFPeerGroupTable = _SleBGPAFPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupTable.setStatus("current")
_SleBGPAFPeerGroupEntry_Object = MibTableRow
sleBGPAFPeerGroupEntry = _SleBGPAFPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1)
)
sleBGPAFPeerGroupEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPAFPeerMode"),
    (0, "SLE-BGP-MIB", "sleBGPAFPeerType"),
    (0, "SLE-BGP-MIB", "sleBGPAFPeerName"),
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupEntry.setStatus("current")


class _SleBGPAFPeerGroupMode_Type(Integer32):
    """Custom type sleBGPAFPeerGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("vpn4", 3))
    )


_SleBGPAFPeerGroupMode_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupMode_Object = MibTableColumn
sleBGPAFPeerGroupMode = _SleBGPAFPeerGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 1),
    _SleBGPAFPeerGroupMode_Type()
)
sleBGPAFPeerGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupMode.setStatus("current")


class _SleBGPAFPeerGroupType_Type(Integer32):
    """Custom type sleBGPAFPeerGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("vrf", 3))
    )


_SleBGPAFPeerGroupType_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupType_Object = MibTableColumn
sleBGPAFPeerGroupType = _SleBGPAFPeerGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 2),
    _SleBGPAFPeerGroupType_Type()
)
sleBGPAFPeerGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupType.setStatus("current")
_SleBGPAFPeerGroupName_Type = OctetString
_SleBGPAFPeerGroupName_Object = MibTableColumn
sleBGPAFPeerGroupName = _SleBGPAFPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 3),
    _SleBGPAFPeerGroupName_Type()
)
sleBGPAFPeerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupName.setStatus("current")


class _SleBGPAFPeerGroupActviate_Type(Integer32):
    """Custom type sleBGPAFPeerGroupActviate based on Integer32"""
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


_SleBGPAFPeerGroupActviate_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupActviate_Object = MibTableColumn
sleBGPAFPeerGroupActviate = _SleBGPAFPeerGroupActviate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 4),
    _SleBGPAFPeerGroupActviate_Type()
)
sleBGPAFPeerGroupActviate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupActviate.setStatus("current")


class _SleBGPAFPeerGroupAllowAsIn_Type(Integer32):
    """Custom type sleBGPAFPeerGroupAllowAsIn based on Integer32"""
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


_SleBGPAFPeerGroupAllowAsIn_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupAllowAsIn_Object = MibTableColumn
sleBGPAFPeerGroupAllowAsIn = _SleBGPAFPeerGroupAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 5),
    _SleBGPAFPeerGroupAllowAsIn_Type()
)
sleBGPAFPeerGroupAllowAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupAllowAsIn.setStatus("current")


class _SleBGPAFPeerGroupAllowAsInNum_Type(Integer32):
    """Custom type sleBGPAFPeerGroupAllowAsInNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SleBGPAFPeerGroupAllowAsInNum_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupAllowAsInNum_Object = MibTableColumn
sleBGPAFPeerGroupAllowAsInNum = _SleBGPAFPeerGroupAllowAsInNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 6),
    _SleBGPAFPeerGroupAllowAsInNum_Type()
)
sleBGPAFPeerGroupAllowAsInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupAllowAsInNum.setStatus("current")


class _SleBGPAFPeerGroupAttrUnchangedAsPath_Type(Integer32):
    """Custom type sleBGPAFPeerGroupAttrUnchangedAsPath based on Integer32"""
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


_SleBGPAFPeerGroupAttrUnchangedAsPath_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupAttrUnchangedAsPath_Object = MibTableColumn
sleBGPAFPeerGroupAttrUnchangedAsPath = _SleBGPAFPeerGroupAttrUnchangedAsPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 7),
    _SleBGPAFPeerGroupAttrUnchangedAsPath_Type()
)
sleBGPAFPeerGroupAttrUnchangedAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupAttrUnchangedAsPath.setStatus("current")


class _SleBGPAFPeerGroupAttrUnchangedMed_Type(Integer32):
    """Custom type sleBGPAFPeerGroupAttrUnchangedMed based on Integer32"""
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


_SleBGPAFPeerGroupAttrUnchangedMed_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupAttrUnchangedMed_Object = MibTableColumn
sleBGPAFPeerGroupAttrUnchangedMed = _SleBGPAFPeerGroupAttrUnchangedMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 8),
    _SleBGPAFPeerGroupAttrUnchangedMed_Type()
)
sleBGPAFPeerGroupAttrUnchangedMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupAttrUnchangedMed.setStatus("current")


class _SleBGPAFPeerGroupAttrUnchangedNexthop_Type(Integer32):
    """Custom type sleBGPAFPeerGroupAttrUnchangedNexthop based on Integer32"""
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


_SleBGPAFPeerGroupAttrUnchangedNexthop_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupAttrUnchangedNexthop_Object = MibTableColumn
sleBGPAFPeerGroupAttrUnchangedNexthop = _SleBGPAFPeerGroupAttrUnchangedNexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 9),
    _SleBGPAFPeerGroupAttrUnchangedNexthop_Type()
)
sleBGPAFPeerGroupAttrUnchangedNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupAttrUnchangedNexthop.setStatus("current")


class _SleBGPAFPeerGroupCapGracefulRestart_Type(Integer32):
    """Custom type sleBGPAFPeerGroupCapGracefulRestart based on Integer32"""
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


_SleBGPAFPeerGroupCapGracefulRestart_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupCapGracefulRestart_Object = MibTableColumn
sleBGPAFPeerGroupCapGracefulRestart = _SleBGPAFPeerGroupCapGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 10),
    _SleBGPAFPeerGroupCapGracefulRestart_Type()
)
sleBGPAFPeerGroupCapGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupCapGracefulRestart.setStatus("current")


class _SleBGPAFPeerGroupCapOrfMode_Type(Integer32):
    """Custom type sleBGPAFPeerGroupCapOrfMode based on Integer32"""
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
        *(("disable", 0),
          ("send", 1),
          ("receive", 2),
          ("both", 3))
    )


_SleBGPAFPeerGroupCapOrfMode_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupCapOrfMode_Object = MibTableColumn
sleBGPAFPeerGroupCapOrfMode = _SleBGPAFPeerGroupCapOrfMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 11),
    _SleBGPAFPeerGroupCapOrfMode_Type()
)
sleBGPAFPeerGroupCapOrfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupCapOrfMode.setStatus("current")


class _SleBGPAFPeerGroupDefOriginate_Type(Integer32):
    """Custom type sleBGPAFPeerGroupDefOriginate based on Integer32"""
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


_SleBGPAFPeerGroupDefOriginate_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupDefOriginate_Object = MibTableColumn
sleBGPAFPeerGroupDefOriginate = _SleBGPAFPeerGroupDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 12),
    _SleBGPAFPeerGroupDefOriginate_Type()
)
sleBGPAFPeerGroupDefOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupDefOriginate.setStatus("current")


class _SleBGPAFPeerGroupDefOriginateRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerGroupDefOriginateRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupDefOriginateRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupDefOriginateRoutemap_Object = MibTableColumn
sleBGPAFPeerGroupDefOriginateRoutemap = _SleBGPAFPeerGroupDefOriginateRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 13),
    _SleBGPAFPeerGroupDefOriginateRoutemap_Type()
)
sleBGPAFPeerGroupDefOriginateRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupDefOriginateRoutemap.setStatus("current")


class _SleBGPAFPeerGroupFLInAccName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupFLInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupFLInAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupFLInAccName_Object = MibTableColumn
sleBGPAFPeerGroupFLInAccName = _SleBGPAFPeerGroupFLInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 14),
    _SleBGPAFPeerGroupFLInAccName_Type()
)
sleBGPAFPeerGroupFLInAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupFLInAccName.setStatus("current")


class _SleBGPAFPeerGroupFLOutAccName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupFLOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupFLOutAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupFLOutAccName_Object = MibTableColumn
sleBGPAFPeerGroupFLOutAccName = _SleBGPAFPeerGroupFLOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 15),
    _SleBGPAFPeerGroupFLOutAccName_Type()
)
sleBGPAFPeerGroupFLOutAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupFLOutAccName.setStatus("current")


class _SleBGPAFPeerGroupMaxPrefixNum_Type(Gauge32):
    """Custom type sleBGPAFPeerGroupMaxPrefixNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPAFPeerGroupMaxPrefixNum_Type.__name__ = "Gauge32"
_SleBGPAFPeerGroupMaxPrefixNum_Object = MibTableColumn
sleBGPAFPeerGroupMaxPrefixNum = _SleBGPAFPeerGroupMaxPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 16),
    _SleBGPAFPeerGroupMaxPrefixNum_Type()
)
sleBGPAFPeerGroupMaxPrefixNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupMaxPrefixNum.setStatus("current")


class _SleBGPAFPeerGroupMaxPrefixThreshold_Type(Integer32):
    """Custom type sleBGPAFPeerGroupMaxPrefixThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleBGPAFPeerGroupMaxPrefixThreshold_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupMaxPrefixThreshold_Object = MibTableColumn
sleBGPAFPeerGroupMaxPrefixThreshold = _SleBGPAFPeerGroupMaxPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 17),
    _SleBGPAFPeerGroupMaxPrefixThreshold_Type()
)
sleBGPAFPeerGroupMaxPrefixThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupMaxPrefixThreshold.setStatus("current")


class _SleBGPAFPeerGroupMaxPrefixWarnOnly_Type(Integer32):
    """Custom type sleBGPAFPeerGroupMaxPrefixWarnOnly based on Integer32"""
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


_SleBGPAFPeerGroupMaxPrefixWarnOnly_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupMaxPrefixWarnOnly_Object = MibTableColumn
sleBGPAFPeerGroupMaxPrefixWarnOnly = _SleBGPAFPeerGroupMaxPrefixWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 18),
    _SleBGPAFPeerGroupMaxPrefixWarnOnly_Type()
)
sleBGPAFPeerGroupMaxPrefixWarnOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupMaxPrefixWarnOnly.setStatus("current")


class _SleBGPAFPeerGroupRemotePrivateAs_Type(Integer32):
    """Custom type sleBGPAFPeerGroupRemotePrivateAs based on Integer32"""
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


_SleBGPAFPeerGroupRemotePrivateAs_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupRemotePrivateAs_Object = MibTableColumn
sleBGPAFPeerGroupRemotePrivateAs = _SleBGPAFPeerGroupRemotePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 19),
    _SleBGPAFPeerGroupRemotePrivateAs_Type()
)
sleBGPAFPeerGroupRemotePrivateAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupRemotePrivateAs.setStatus("current")


class _SleBGPAFPeerGroupInRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerGroupInRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupInRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupInRoutemap_Object = MibTableColumn
sleBGPAFPeerGroupInRoutemap = _SleBGPAFPeerGroupInRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 20),
    _SleBGPAFPeerGroupInRoutemap_Type()
)
sleBGPAFPeerGroupInRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupInRoutemap.setStatus("current")


class _SleBGPAFPeerGroupOutRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerGroupOutRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupOutRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupOutRoutemap_Object = MibTableColumn
sleBGPAFPeerGroupOutRoutemap = _SleBGPAFPeerGroupOutRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 21),
    _SleBGPAFPeerGroupOutRoutemap_Type()
)
sleBGPAFPeerGroupOutRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupOutRoutemap.setStatus("current")


class _SleBGPAFPeerGroupRouteReflectClient_Type(Integer32):
    """Custom type sleBGPAFPeerGroupRouteReflectClient based on Integer32"""
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


_SleBGPAFPeerGroupRouteReflectClient_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupRouteReflectClient_Object = MibTableColumn
sleBGPAFPeerGroupRouteReflectClient = _SleBGPAFPeerGroupRouteReflectClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 22),
    _SleBGPAFPeerGroupRouteReflectClient_Type()
)
sleBGPAFPeerGroupRouteReflectClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupRouteReflectClient.setStatus("current")


class _SleBGPAFPeerGroupRouteServerClient_Type(Integer32):
    """Custom type sleBGPAFPeerGroupRouteServerClient based on Integer32"""
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


_SleBGPAFPeerGroupRouteServerClient_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupRouteServerClient_Object = MibTableColumn
sleBGPAFPeerGroupRouteServerClient = _SleBGPAFPeerGroupRouteServerClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 23),
    _SleBGPAFPeerGroupRouteServerClient_Type()
)
sleBGPAFPeerGroupRouteServerClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupRouteServerClient.setStatus("current")


class _SleBGPAFPeerGroupInDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupInDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupInDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupInDistListName_Object = MibTableColumn
sleBGPAFPeerGroupInDistListName = _SleBGPAFPeerGroupInDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 24),
    _SleBGPAFPeerGroupInDistListName_Type()
)
sleBGPAFPeerGroupInDistListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupInDistListName.setStatus("current")


class _SleBGPAFPeerGroupOutDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupOutDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupOutDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupOutDistListName_Object = MibTableColumn
sleBGPAFPeerGroupOutDistListName = _SleBGPAFPeerGroupOutDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 25),
    _SleBGPAFPeerGroupOutDistListName_Type()
)
sleBGPAFPeerGroupOutDistListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupOutDistListName.setStatus("current")


class _SleBGPAFPeerGroupInPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupInPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupInPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupInPrefixListName_Object = MibTableColumn
sleBGPAFPeerGroupInPrefixListName = _SleBGPAFPeerGroupInPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 26),
    _SleBGPAFPeerGroupInPrefixListName_Type()
)
sleBGPAFPeerGroupInPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupInPrefixListName.setStatus("current")


class _SleBGPAFPeerGroupOutPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupOutPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupOutPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupOutPrefixListName_Object = MibTableColumn
sleBGPAFPeerGroupOutPrefixListName = _SleBGPAFPeerGroupOutPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 27),
    _SleBGPAFPeerGroupOutPrefixListName_Type()
)
sleBGPAFPeerGroupOutPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupOutPrefixListName.setStatus("current")


class _SleBGPAFPeerGroupSendCommunity_Type(Integer32):
    """Custom type sleBGPAFPeerGroupSendCommunity based on Integer32"""
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
        *(("disable", 0),
          ("standard", 1),
          ("extended", 2),
          ("both", 3))
    )


_SleBGPAFPeerGroupSendCommunity_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupSendCommunity_Object = MibTableColumn
sleBGPAFPeerGroupSendCommunity = _SleBGPAFPeerGroupSendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 28),
    _SleBGPAFPeerGroupSendCommunity_Type()
)
sleBGPAFPeerGroupSendCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupSendCommunity.setStatus("current")


class _SleBGPAFPeerGroupNexthopSelf_Type(Integer32):
    """Custom type sleBGPAFPeerGroupNexthopSelf based on Integer32"""
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


_SleBGPAFPeerGroupNexthopSelf_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupNexthopSelf_Object = MibTableColumn
sleBGPAFPeerGroupNexthopSelf = _SleBGPAFPeerGroupNexthopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 29),
    _SleBGPAFPeerGroupNexthopSelf_Type()
)
sleBGPAFPeerGroupNexthopSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupNexthopSelf.setStatus("current")


class _SleBGPAFPeerGroupSoftReconfig_Type(Integer32):
    """Custom type sleBGPAFPeerGroupSoftReconfig based on Integer32"""
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


_SleBGPAFPeerGroupSoftReconfig_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupSoftReconfig_Object = MibTableColumn
sleBGPAFPeerGroupSoftReconfig = _SleBGPAFPeerGroupSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 30),
    _SleBGPAFPeerGroupSoftReconfig_Type()
)
sleBGPAFPeerGroupSoftReconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupSoftReconfig.setStatus("current")


class _SleBGPAFPeerGroupUnsuppressMapName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupUnsuppressMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupUnsuppressMapName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupUnsuppressMapName_Object = MibTableColumn
sleBGPAFPeerGroupUnsuppressMapName = _SleBGPAFPeerGroupUnsuppressMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 1, 1, 31),
    _SleBGPAFPeerGroupUnsuppressMapName_Type()
)
sleBGPAFPeerGroupUnsuppressMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupUnsuppressMapName.setStatus("current")
_SleBGPAFPeerGroupControl_ObjectIdentity = ObjectIdentity
sleBGPAFPeerGroupControl = _SleBGPAFPeerGroupControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2)
)


class _SleBGPAFPeerGroupControlRequest_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlRequest based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("setBGPAFPeerGroupActivate", 1),
          ("setBGPAFPeerGroupAllowAsInProfile", 2),
          ("setBGPAFPeerGroupAttrUnchangedProfile", 3),
          ("setBGPAFPeerGroupCapGracefulRestart", 4),
          ("setBGPAFPeerGroupCapOrfMode", 5),
          ("setBGPAFPeerGroupDefaultOriginate", 6),
          ("setBGPAFPeerGroupFLInAccName", 7),
          ("unsetBGPAFPeerGroupFLInAccName", 8),
          ("setBGPAFPeerGroupFLOutAccName", 9),
          ("unsetBGPAFPeerGroupFLOutAccName", 10),
          ("setBGPAFPeerGroupMaxPrefixProfile", 11),
          ("setBGPAFPeerGroupRemotePrivateAs", 12),
          ("setBGPAFPeerGroupInRoutemap", 13),
          ("unsetBGPAFPeerGroupInRoutemap", 14),
          ("setBGPAFPeerGroupOutRoutemap", 15),
          ("unsetBGPAFPeerGroupOutRoutemap", 16),
          ("setBGPAFPeerGroupRouteReflectClient", 17),
          ("setBGPAFPeerGroupRouteServerClient", 18),
          ("setBGPAFPeerGroupSendCommunity", 19),
          ("setBGPAFPeerGroupNexthopSelf", 20),
          ("setBGPAFPeerGroupSoftReconfig", 21),
          ("setBGPAFPeerGroupUnsupressMapName", 22),
          ("unsetBGPAFPeerGroupUnsupressMapName", 23),
          ("setBGPAFPeerGroupInDistListName", 24),
          ("unsetBGPAFPeerGroupInDistListName", 25),
          ("setBGPAFPeerGroupOutDistListName", 26),
          ("unsetBGPAFPeerGroupOutDistListName", 27),
          ("setBGPAFPeerGroupInPrefixListName", 28),
          ("unsetBGPAFPeerGroupInPrefixListName", 29),
          ("setBGPAFPeerGroupOutPrefixListName", 30),
          ("unsetBGPAFPeerGroupOutPrefixListName", 31))
    )


_SleBGPAFPeerGroupControlRequest_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlRequest_Object = MibScalar
sleBGPAFPeerGroupControlRequest = _SleBGPAFPeerGroupControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 1),
    _SleBGPAFPeerGroupControlRequest_Type()
)
sleBGPAFPeerGroupControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlRequest.setStatus("current")
_SleBGPAFPeerGroupControlStatus_Type = SleControlStatusType
_SleBGPAFPeerGroupControlStatus_Object = MibScalar
sleBGPAFPeerGroupControlStatus = _SleBGPAFPeerGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 2),
    _SleBGPAFPeerGroupControlStatus_Type()
)
sleBGPAFPeerGroupControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlStatus.setStatus("current")
_SleBGPAFPeerGroupControlTimer_Type = Gauge32
_SleBGPAFPeerGroupControlTimer_Object = MibScalar
sleBGPAFPeerGroupControlTimer = _SleBGPAFPeerGroupControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 3),
    _SleBGPAFPeerGroupControlTimer_Type()
)
sleBGPAFPeerGroupControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlTimer.setStatus("current")
_SleBGPAFPeerGroupControlTimeStamp_Type = TimeTicks
_SleBGPAFPeerGroupControlTimeStamp_Object = MibScalar
sleBGPAFPeerGroupControlTimeStamp = _SleBGPAFPeerGroupControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 4),
    _SleBGPAFPeerGroupControlTimeStamp_Type()
)
sleBGPAFPeerGroupControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlTimeStamp.setStatus("current")
_SleBGPAFPeerGroupControlReqResult_Type = SleControlRequestResultType
_SleBGPAFPeerGroupControlReqResult_Object = MibScalar
sleBGPAFPeerGroupControlReqResult = _SleBGPAFPeerGroupControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 5),
    _SleBGPAFPeerGroupControlReqResult_Type()
)
sleBGPAFPeerGroupControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlReqResult.setStatus("current")


class _SleBGPAFPeerGroupControlMode_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("vpn4", 3))
    )


_SleBGPAFPeerGroupControlMode_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlMode_Object = MibScalar
sleBGPAFPeerGroupControlMode = _SleBGPAFPeerGroupControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 6),
    _SleBGPAFPeerGroupControlMode_Type()
)
sleBGPAFPeerGroupControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlMode.setStatus("current")


class _SleBGPAFPeerGroupControlType_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("vrf", 3))
    )


_SleBGPAFPeerGroupControlType_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlType_Object = MibScalar
sleBGPAFPeerGroupControlType = _SleBGPAFPeerGroupControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 7),
    _SleBGPAFPeerGroupControlType_Type()
)
sleBGPAFPeerGroupControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlType.setStatus("current")
_SleBGPAFPeerGroupControlName_Type = OctetString
_SleBGPAFPeerGroupControlName_Object = MibScalar
sleBGPAFPeerGroupControlName = _SleBGPAFPeerGroupControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 8),
    _SleBGPAFPeerGroupControlName_Type()
)
sleBGPAFPeerGroupControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlName.setStatus("current")


class _SleBGPAFPeerGroupControlActviate_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlActviate based on Integer32"""
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


_SleBGPAFPeerGroupControlActviate_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlActviate_Object = MibScalar
sleBGPAFPeerGroupControlActviate = _SleBGPAFPeerGroupControlActviate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 9),
    _SleBGPAFPeerGroupControlActviate_Type()
)
sleBGPAFPeerGroupControlActviate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlActviate.setStatus("current")


class _SleBGPAFPeerGroupControlAllowAsIn_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlAllowAsIn based on Integer32"""
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


_SleBGPAFPeerGroupControlAllowAsIn_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlAllowAsIn_Object = MibScalar
sleBGPAFPeerGroupControlAllowAsIn = _SleBGPAFPeerGroupControlAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 10),
    _SleBGPAFPeerGroupControlAllowAsIn_Type()
)
sleBGPAFPeerGroupControlAllowAsIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlAllowAsIn.setStatus("current")


class _SleBGPAFPeerGroupControlAllowAsInNum_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlAllowAsInNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SleBGPAFPeerGroupControlAllowAsInNum_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlAllowAsInNum_Object = MibScalar
sleBGPAFPeerGroupControlAllowAsInNum = _SleBGPAFPeerGroupControlAllowAsInNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 11),
    _SleBGPAFPeerGroupControlAllowAsInNum_Type()
)
sleBGPAFPeerGroupControlAllowAsInNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlAllowAsInNum.setStatus("current")


class _SleBGPAFPeerGroupControlAttrUnchangedAsPath_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlAttrUnchangedAsPath based on Integer32"""
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


_SleBGPAFPeerGroupControlAttrUnchangedAsPath_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlAttrUnchangedAsPath_Object = MibScalar
sleBGPAFPeerGroupControlAttrUnchangedAsPath = _SleBGPAFPeerGroupControlAttrUnchangedAsPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 12),
    _SleBGPAFPeerGroupControlAttrUnchangedAsPath_Type()
)
sleBGPAFPeerGroupControlAttrUnchangedAsPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlAttrUnchangedAsPath.setStatus("current")


class _SleBGPAFPeerGroupControlAttrUnchangedMed_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlAttrUnchangedMed based on Integer32"""
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


_SleBGPAFPeerGroupControlAttrUnchangedMed_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlAttrUnchangedMed_Object = MibScalar
sleBGPAFPeerGroupControlAttrUnchangedMed = _SleBGPAFPeerGroupControlAttrUnchangedMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 13),
    _SleBGPAFPeerGroupControlAttrUnchangedMed_Type()
)
sleBGPAFPeerGroupControlAttrUnchangedMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlAttrUnchangedMed.setStatus("current")


class _SleBGPAFPeerGroupControlAttrUnchangedNexthop_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlAttrUnchangedNexthop based on Integer32"""
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


_SleBGPAFPeerGroupControlAttrUnchangedNexthop_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlAttrUnchangedNexthop_Object = MibScalar
sleBGPAFPeerGroupControlAttrUnchangedNexthop = _SleBGPAFPeerGroupControlAttrUnchangedNexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 14),
    _SleBGPAFPeerGroupControlAttrUnchangedNexthop_Type()
)
sleBGPAFPeerGroupControlAttrUnchangedNexthop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlAttrUnchangedNexthop.setStatus("current")


class _SleBGPAFPeerGroupControlCapGracefulRestart_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlCapGracefulRestart based on Integer32"""
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


_SleBGPAFPeerGroupControlCapGracefulRestart_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlCapGracefulRestart_Object = MibScalar
sleBGPAFPeerGroupControlCapGracefulRestart = _SleBGPAFPeerGroupControlCapGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 15),
    _SleBGPAFPeerGroupControlCapGracefulRestart_Type()
)
sleBGPAFPeerGroupControlCapGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlCapGracefulRestart.setStatus("current")


class _SleBGPAFPeerGroupControlCapOrfMode_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlCapOrfMode based on Integer32"""
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
        *(("disable", 0),
          ("send", 1),
          ("receive", 2),
          ("both", 3))
    )


_SleBGPAFPeerGroupControlCapOrfMode_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlCapOrfMode_Object = MibScalar
sleBGPAFPeerGroupControlCapOrfMode = _SleBGPAFPeerGroupControlCapOrfMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 16),
    _SleBGPAFPeerGroupControlCapOrfMode_Type()
)
sleBGPAFPeerGroupControlCapOrfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlCapOrfMode.setStatus("current")


class _SleBGPAFPeerGroupControlDefOriginate_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlDefOriginate based on Integer32"""
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


_SleBGPAFPeerGroupControlDefOriginate_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlDefOriginate_Object = MibScalar
sleBGPAFPeerGroupControlDefOriginate = _SleBGPAFPeerGroupControlDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 17),
    _SleBGPAFPeerGroupControlDefOriginate_Type()
)
sleBGPAFPeerGroupControlDefOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlDefOriginate.setStatus("current")


class _SleBGPAFPeerGroupControlDefOriginateRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlDefOriginateRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlDefOriginateRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlDefOriginateRoutemap_Object = MibScalar
sleBGPAFPeerGroupControlDefOriginateRoutemap = _SleBGPAFPeerGroupControlDefOriginateRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 18),
    _SleBGPAFPeerGroupControlDefOriginateRoutemap_Type()
)
sleBGPAFPeerGroupControlDefOriginateRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlDefOriginateRoutemap.setStatus("current")


class _SleBGPAFPeerGroupControlFLInAccName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlFLInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlFLInAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlFLInAccName_Object = MibScalar
sleBGPAFPeerGroupControlFLInAccName = _SleBGPAFPeerGroupControlFLInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 19),
    _SleBGPAFPeerGroupControlFLInAccName_Type()
)
sleBGPAFPeerGroupControlFLInAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlFLInAccName.setStatus("current")


class _SleBGPAFPeerGroupControlFLOutAccName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlFLOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlFLOutAccName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlFLOutAccName_Object = MibScalar
sleBGPAFPeerGroupControlFLOutAccName = _SleBGPAFPeerGroupControlFLOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 20),
    _SleBGPAFPeerGroupControlFLOutAccName_Type()
)
sleBGPAFPeerGroupControlFLOutAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlFLOutAccName.setStatus("current")


class _SleBGPAFPeerGroupControlMaxPrefixNum_Type(Gauge32):
    """Custom type sleBGPAFPeerGroupControlMaxPrefixNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleBGPAFPeerGroupControlMaxPrefixNum_Type.__name__ = "Gauge32"
_SleBGPAFPeerGroupControlMaxPrefixNum_Object = MibScalar
sleBGPAFPeerGroupControlMaxPrefixNum = _SleBGPAFPeerGroupControlMaxPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 21),
    _SleBGPAFPeerGroupControlMaxPrefixNum_Type()
)
sleBGPAFPeerGroupControlMaxPrefixNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlMaxPrefixNum.setStatus("current")


class _SleBGPAFPeerGroupControlMaxPrefixThreshold_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlMaxPrefixThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleBGPAFPeerGroupControlMaxPrefixThreshold_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlMaxPrefixThreshold_Object = MibScalar
sleBGPAFPeerGroupControlMaxPrefixThreshold = _SleBGPAFPeerGroupControlMaxPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 22),
    _SleBGPAFPeerGroupControlMaxPrefixThreshold_Type()
)
sleBGPAFPeerGroupControlMaxPrefixThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlMaxPrefixThreshold.setStatus("current")


class _SleBGPAFPeerGroupControlMaxPrefixWarnOnly_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlMaxPrefixWarnOnly based on Integer32"""
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


_SleBGPAFPeerGroupControlMaxPrefixWarnOnly_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlMaxPrefixWarnOnly_Object = MibScalar
sleBGPAFPeerGroupControlMaxPrefixWarnOnly = _SleBGPAFPeerGroupControlMaxPrefixWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 23),
    _SleBGPAFPeerGroupControlMaxPrefixWarnOnly_Type()
)
sleBGPAFPeerGroupControlMaxPrefixWarnOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlMaxPrefixWarnOnly.setStatus("current")


class _SleBGPAFPeerGroupControlRemotePrivateAs_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlRemotePrivateAs based on Integer32"""
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


_SleBGPAFPeerGroupControlRemotePrivateAs_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlRemotePrivateAs_Object = MibScalar
sleBGPAFPeerGroupControlRemotePrivateAs = _SleBGPAFPeerGroupControlRemotePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 24),
    _SleBGPAFPeerGroupControlRemotePrivateAs_Type()
)
sleBGPAFPeerGroupControlRemotePrivateAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlRemotePrivateAs.setStatus("current")


class _SleBGPAFPeerGroupControlInRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlInRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlInRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlInRoutemap_Object = MibScalar
sleBGPAFPeerGroupControlInRoutemap = _SleBGPAFPeerGroupControlInRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 25),
    _SleBGPAFPeerGroupControlInRoutemap_Type()
)
sleBGPAFPeerGroupControlInRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlInRoutemap.setStatus("current")


class _SleBGPAFPeerGroupControlOutRoutemap_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlOutRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlOutRoutemap_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlOutRoutemap_Object = MibScalar
sleBGPAFPeerGroupControlOutRoutemap = _SleBGPAFPeerGroupControlOutRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 26),
    _SleBGPAFPeerGroupControlOutRoutemap_Type()
)
sleBGPAFPeerGroupControlOutRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlOutRoutemap.setStatus("current")


class _SleBGPAFPeerGroupControlRouteReflectClient_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlRouteReflectClient based on Integer32"""
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


_SleBGPAFPeerGroupControlRouteReflectClient_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlRouteReflectClient_Object = MibScalar
sleBGPAFPeerGroupControlRouteReflectClient = _SleBGPAFPeerGroupControlRouteReflectClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 27),
    _SleBGPAFPeerGroupControlRouteReflectClient_Type()
)
sleBGPAFPeerGroupControlRouteReflectClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlRouteReflectClient.setStatus("current")


class _SleBGPAFPeerGroupControlRouteServerClient_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlRouteServerClient based on Integer32"""
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


_SleBGPAFPeerGroupControlRouteServerClient_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlRouteServerClient_Object = MibScalar
sleBGPAFPeerGroupControlRouteServerClient = _SleBGPAFPeerGroupControlRouteServerClient_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 28),
    _SleBGPAFPeerGroupControlRouteServerClient_Type()
)
sleBGPAFPeerGroupControlRouteServerClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlRouteServerClient.setStatus("current")


class _SleBGPAFPeerGroupControlInDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlInDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlInDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlInDistListName_Object = MibScalar
sleBGPAFPeerGroupControlInDistListName = _SleBGPAFPeerGroupControlInDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 29),
    _SleBGPAFPeerGroupControlInDistListName_Type()
)
sleBGPAFPeerGroupControlInDistListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlInDistListName.setStatus("current")


class _SleBGPAFPeerGroupControlOutDistListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlOutDistListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlOutDistListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlOutDistListName_Object = MibScalar
sleBGPAFPeerGroupControlOutDistListName = _SleBGPAFPeerGroupControlOutDistListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 30),
    _SleBGPAFPeerGroupControlOutDistListName_Type()
)
sleBGPAFPeerGroupControlOutDistListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlOutDistListName.setStatus("current")


class _SleBGPAFPeerGroupControlInPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlInPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlInPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlInPrefixListName_Object = MibScalar
sleBGPAFPeerGroupControlInPrefixListName = _SleBGPAFPeerGroupControlInPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 31),
    _SleBGPAFPeerGroupControlInPrefixListName_Type()
)
sleBGPAFPeerGroupControlInPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlInPrefixListName.setStatus("current")


class _SleBGPAFPeerGroupControlOutPrefixListName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlOutPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlOutPrefixListName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlOutPrefixListName_Object = MibScalar
sleBGPAFPeerGroupControlOutPrefixListName = _SleBGPAFPeerGroupControlOutPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 32),
    _SleBGPAFPeerGroupControlOutPrefixListName_Type()
)
sleBGPAFPeerGroupControlOutPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlOutPrefixListName.setStatus("current")


class _SleBGPAFPeerGroupControlSendCommunity_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlSendCommunity based on Integer32"""
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
        *(("disable", 0),
          ("standard", 1),
          ("extended", 2),
          ("both", 3))
    )


_SleBGPAFPeerGroupControlSendCommunity_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlSendCommunity_Object = MibScalar
sleBGPAFPeerGroupControlSendCommunity = _SleBGPAFPeerGroupControlSendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 33),
    _SleBGPAFPeerGroupControlSendCommunity_Type()
)
sleBGPAFPeerGroupControlSendCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlSendCommunity.setStatus("current")


class _SleBGPAFPeerGroupControlNexthopSelf_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlNexthopSelf based on Integer32"""
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


_SleBGPAFPeerGroupControlNexthopSelf_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlNexthopSelf_Object = MibScalar
sleBGPAFPeerGroupControlNexthopSelf = _SleBGPAFPeerGroupControlNexthopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 34),
    _SleBGPAFPeerGroupControlNexthopSelf_Type()
)
sleBGPAFPeerGroupControlNexthopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlNexthopSelf.setStatus("current")


class _SleBGPAFPeerGroupControlSoftReconfig_Type(Integer32):
    """Custom type sleBGPAFPeerGroupControlSoftReconfig based on Integer32"""
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


_SleBGPAFPeerGroupControlSoftReconfig_Type.__name__ = "Integer32"
_SleBGPAFPeerGroupControlSoftReconfig_Object = MibScalar
sleBGPAFPeerGroupControlSoftReconfig = _SleBGPAFPeerGroupControlSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 35),
    _SleBGPAFPeerGroupControlSoftReconfig_Type()
)
sleBGPAFPeerGroupControlSoftReconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlSoftReconfig.setStatus("current")


class _SleBGPAFPeerGroupControlUnsuppressMapName_Type(OctetString):
    """Custom type sleBGPAFPeerGroupControlUnsuppressMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFPeerGroupControlUnsuppressMapName_Type.__name__ = "OctetString"
_SleBGPAFPeerGroupControlUnsuppressMapName_Object = MibScalar
sleBGPAFPeerGroupControlUnsuppressMapName = _SleBGPAFPeerGroupControlUnsuppressMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 2, 36),
    _SleBGPAFPeerGroupControlUnsuppressMapName_Type()
)
sleBGPAFPeerGroupControlUnsuppressMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupControlUnsuppressMapName.setStatus("current")
_SleBGPAFPeerGroupNotification_ObjectIdentity = ObjectIdentity
sleBGPAFPeerGroupNotification = _SleBGPAFPeerGroupNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3)
)
_SleBGPAFNetwork_ObjectIdentity = ObjectIdentity
sleBGPAFNetwork = _SleBGPAFNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5)
)
_SleBGPAFNetworkTable_Object = MibTable
sleBGPAFNetworkTable = _SleBGPAFNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 1)
)
if mibBuilder.loadTexts:
    sleBGPAFNetworkTable.setStatus("current")
_SleBGPAFNetworkEntry_Object = MibTableRow
sleBGPAFNetworkEntry = _SleBGPAFNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 1, 1)
)
sleBGPAFNetworkEntry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPAFNetworkMode"),
    (0, "SLE-BGP-MIB", "sleBGPAFNetworkType"),
    (0, "SLE-BGP-MIB", "sleBGPAFNetworkAddrPrefix"),
)
if mibBuilder.loadTexts:
    sleBGPAFNetworkEntry.setStatus("current")


class _SleBGPAFNetworkMode_Type(Integer32):
    """Custom type sleBGPAFNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFNetworkMode_Type.__name__ = "Integer32"
_SleBGPAFNetworkMode_Object = MibTableColumn
sleBGPAFNetworkMode = _SleBGPAFNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 1, 1, 1),
    _SleBGPAFNetworkMode_Type()
)
sleBGPAFNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkMode.setStatus("current")


class _SleBGPAFNetworkType_Type(Integer32):
    """Custom type sleBGPAFNetworkType based on Integer32"""
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


_SleBGPAFNetworkType_Type.__name__ = "Integer32"
_SleBGPAFNetworkType_Object = MibTableColumn
sleBGPAFNetworkType = _SleBGPAFNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 1, 1, 2),
    _SleBGPAFNetworkType_Type()
)
sleBGPAFNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkType.setStatus("current")
_SleBGPAFNetworkAddrPrefix_Type = OctetString
_SleBGPAFNetworkAddrPrefix_Object = MibTableColumn
sleBGPAFNetworkAddrPrefix = _SleBGPAFNetworkAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 1, 1, 3),
    _SleBGPAFNetworkAddrPrefix_Type()
)
sleBGPAFNetworkAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkAddrPrefix.setStatus("current")


class _SleBGPAFNetworkBackdoor_Type(Integer32):
    """Custom type sleBGPAFNetworkBackdoor based on Integer32"""
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


_SleBGPAFNetworkBackdoor_Type.__name__ = "Integer32"
_SleBGPAFNetworkBackdoor_Object = MibTableColumn
sleBGPAFNetworkBackdoor = _SleBGPAFNetworkBackdoor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 1, 1, 4),
    _SleBGPAFNetworkBackdoor_Type()
)
sleBGPAFNetworkBackdoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkBackdoor.setStatus("current")


class _SleBGPAFNetworkRoutemap_Type(OctetString):
    """Custom type sleBGPAFNetworkRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFNetworkRoutemap_Type.__name__ = "OctetString"
_SleBGPAFNetworkRoutemap_Object = MibTableColumn
sleBGPAFNetworkRoutemap = _SleBGPAFNetworkRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 1, 1, 5),
    _SleBGPAFNetworkRoutemap_Type()
)
sleBGPAFNetworkRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkRoutemap.setStatus("current")
_SleBGPAFNetworkControl_ObjectIdentity = ObjectIdentity
sleBGPAFNetworkControl = _SleBGPAFNetworkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2)
)


class _SleBGPAFNetworkControlRequest_Type(Integer32):
    """Custom type sleBGPAFNetworkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createBGPAFNetwork", 1),
          ("deleteBGPAFNetwork", 2))
    )


_SleBGPAFNetworkControlRequest_Type.__name__ = "Integer32"
_SleBGPAFNetworkControlRequest_Object = MibScalar
sleBGPAFNetworkControlRequest = _SleBGPAFNetworkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 1),
    _SleBGPAFNetworkControlRequest_Type()
)
sleBGPAFNetworkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlRequest.setStatus("current")
_SleBGPAFNetworkControlStatus_Type = SleControlStatusType
_SleBGPAFNetworkControlStatus_Object = MibScalar
sleBGPAFNetworkControlStatus = _SleBGPAFNetworkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 2),
    _SleBGPAFNetworkControlStatus_Type()
)
sleBGPAFNetworkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlStatus.setStatus("current")
_SleBGPAFNetworkControlTimer_Type = Gauge32
_SleBGPAFNetworkControlTimer_Object = MibScalar
sleBGPAFNetworkControlTimer = _SleBGPAFNetworkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 3),
    _SleBGPAFNetworkControlTimer_Type()
)
sleBGPAFNetworkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlTimer.setStatus("current")
_SleBGPAFNetworkControlTimeStamp_Type = TimeTicks
_SleBGPAFNetworkControlTimeStamp_Object = MibScalar
sleBGPAFNetworkControlTimeStamp = _SleBGPAFNetworkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 4),
    _SleBGPAFNetworkControlTimeStamp_Type()
)
sleBGPAFNetworkControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlTimeStamp.setStatus("current")
_SleBGPAFNetworkControlReqResult_Type = SleControlRequestResultType
_SleBGPAFNetworkControlReqResult_Object = MibScalar
sleBGPAFNetworkControlReqResult = _SleBGPAFNetworkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 5),
    _SleBGPAFNetworkControlReqResult_Type()
)
sleBGPAFNetworkControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlReqResult.setStatus("current")


class _SleBGPAFNetworkControlMode_Type(Integer32):
    """Custom type sleBGPAFNetworkControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SleBGPAFNetworkControlMode_Type.__name__ = "Integer32"
_SleBGPAFNetworkControlMode_Object = MibScalar
sleBGPAFNetworkControlMode = _SleBGPAFNetworkControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 6),
    _SleBGPAFNetworkControlMode_Type()
)
sleBGPAFNetworkControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlMode.setStatus("current")


class _SleBGPAFNetworkControlType_Type(Integer32):
    """Custom type sleBGPAFNetworkControlType based on Integer32"""
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


_SleBGPAFNetworkControlType_Type.__name__ = "Integer32"
_SleBGPAFNetworkControlType_Object = MibScalar
sleBGPAFNetworkControlType = _SleBGPAFNetworkControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 7),
    _SleBGPAFNetworkControlType_Type()
)
sleBGPAFNetworkControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlType.setStatus("current")
_SleBGPAFNetworkControlAddrPrefix_Type = OctetString
_SleBGPAFNetworkControlAddrPrefix_Object = MibScalar
sleBGPAFNetworkControlAddrPrefix = _SleBGPAFNetworkControlAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 8),
    _SleBGPAFNetworkControlAddrPrefix_Type()
)
sleBGPAFNetworkControlAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlAddrPrefix.setStatus("current")


class _SleBGPAFNetworkControlBackdoor_Type(Integer32):
    """Custom type sleBGPAFNetworkControlBackdoor based on Integer32"""
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


_SleBGPAFNetworkControlBackdoor_Type.__name__ = "Integer32"
_SleBGPAFNetworkControlBackdoor_Object = MibScalar
sleBGPAFNetworkControlBackdoor = _SleBGPAFNetworkControlBackdoor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 9),
    _SleBGPAFNetworkControlBackdoor_Type()
)
sleBGPAFNetworkControlBackdoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlBackdoor.setStatus("current")


class _SleBGPAFNetworkControlRoutemap_Type(OctetString):
    """Custom type sleBGPAFNetworkControlRoutemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleBGPAFNetworkControlRoutemap_Type.__name__ = "OctetString"
_SleBGPAFNetworkControlRoutemap_Object = MibScalar
sleBGPAFNetworkControlRoutemap = _SleBGPAFNetworkControlRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 2, 10),
    _SleBGPAFNetworkControlRoutemap_Type()
)
sleBGPAFNetworkControlRoutemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBGPAFNetworkControlRoutemap.setStatus("current")
_SleBGPAFNetworkNotification_ObjectIdentity = ObjectIdentity
sleBGPAFNetworkNotification = _SleBGPAFNetworkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 3)
)
_SleBGPStatus_ObjectIdentity = ObjectIdentity
sleBGPStatus = _SleBGPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6)
)
_SleBGPStatusPeer_ObjectIdentity = ObjectIdentity
sleBGPStatusPeer = _SleBGPStatusPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1)
)
_SleBGPStatusPeerV4_ObjectIdentity = ObjectIdentity
sleBGPStatusPeerV4 = _SleBGPStatusPeerV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1)
)
_SleBGPStatusPeerV4Table_Object = MibTable
sleBGPStatusPeerV4Table = _SleBGPStatusPeerV4Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4Table.setStatus("current")
_SleBGPStatusPeerV4Entry_Object = MibTableRow
sleBGPStatusPeerV4Entry = _SleBGPStatusPeerV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1)
)
sleBGPStatusPeerV4Entry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPStatusPeerV4Name"),
)
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4Entry.setStatus("current")
_SleBGPStatusPeerV4Name_Type = OctetString
_SleBGPStatusPeerV4Name_Object = MibTableColumn
sleBGPStatusPeerV4Name = _SleBGPStatusPeerV4Name_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 1),
    _SleBGPStatusPeerV4Name_Type()
)
sleBGPStatusPeerV4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4Name.setStatus("current")
_SleBGPStatusPeerV4RemoteAs_Type = Gauge32
_SleBGPStatusPeerV4RemoteAs_Object = MibTableColumn
sleBGPStatusPeerV4RemoteAs = _SleBGPStatusPeerV4RemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 2),
    _SleBGPStatusPeerV4RemoteAs_Type()
)
sleBGPStatusPeerV4RemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RemoteAs.setStatus("current")
_SleBGPStatusPeerV4LocalAs_Type = Gauge32
_SleBGPStatusPeerV4LocalAs_Object = MibTableColumn
sleBGPStatusPeerV4LocalAs = _SleBGPStatusPeerV4LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 3),
    _SleBGPStatusPeerV4LocalAs_Type()
)
sleBGPStatusPeerV4LocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4LocalAs.setStatus("current")


class _SleBGPStatusPeerV4LinkState_Type(Integer32):
    """Custom type sleBGPStatusPeerV4LinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_SleBGPStatusPeerV4LinkState_Type.__name__ = "Integer32"
_SleBGPStatusPeerV4LinkState_Object = MibTableColumn
sleBGPStatusPeerV4LinkState = _SleBGPStatusPeerV4LinkState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 4),
    _SleBGPStatusPeerV4LinkState_Type()
)
sleBGPStatusPeerV4LinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4LinkState.setStatus("current")
_SleBGPStatusPeerV4RouterID_Type = IpAddress
_SleBGPStatusPeerV4RouterID_Object = MibTableColumn
sleBGPStatusPeerV4RouterID = _SleBGPStatusPeerV4RouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 5),
    _SleBGPStatusPeerV4RouterID_Type()
)
sleBGPStatusPeerV4RouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RouterID.setStatus("current")


class _SleBGPStatusPeerV4State_Type(Integer32):
    """Custom type sleBGPStatusPeerV4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_SleBGPStatusPeerV4State_Type.__name__ = "Integer32"
_SleBGPStatusPeerV4State_Object = MibTableColumn
sleBGPStatusPeerV4State = _SleBGPStatusPeerV4State_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 6),
    _SleBGPStatusPeerV4State_Type()
)
sleBGPStatusPeerV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4State.setStatus("current")
_SleBGPStatusPeerV4HoldTime_Type = Integer32
_SleBGPStatusPeerV4HoldTime_Object = MibTableColumn
sleBGPStatusPeerV4HoldTime = _SleBGPStatusPeerV4HoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 7),
    _SleBGPStatusPeerV4HoldTime_Type()
)
sleBGPStatusPeerV4HoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4HoldTime.setStatus("current")
_SleBGPStatusPeerV4KeepAlive_Type = Integer32
_SleBGPStatusPeerV4KeepAlive_Object = MibTableColumn
sleBGPStatusPeerV4KeepAlive = _SleBGPStatusPeerV4KeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 8),
    _SleBGPStatusPeerV4KeepAlive_Type()
)
sleBGPStatusPeerV4KeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4KeepAlive.setStatus("current")
_SleBGPStatusPeerV4Uptime_Type = OctetString
_SleBGPStatusPeerV4Uptime_Object = MibTableColumn
sleBGPStatusPeerV4Uptime = _SleBGPStatusPeerV4Uptime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 9),
    _SleBGPStatusPeerV4Uptime_Type()
)
sleBGPStatusPeerV4Uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4Uptime.setStatus("current")
_SleBGPStatusPeerV4LastReadTime_Type = OctetString
_SleBGPStatusPeerV4LastReadTime_Object = MibTableColumn
sleBGPStatusPeerV4LastReadTime = _SleBGPStatusPeerV4LastReadTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 10),
    _SleBGPStatusPeerV4LastReadTime_Type()
)
sleBGPStatusPeerV4LastReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4LastReadTime.setStatus("current")
_SleBGPStatusPeerV4RecvMessageCount_Type = Gauge32
_SleBGPStatusPeerV4RecvMessageCount_Object = MibTableColumn
sleBGPStatusPeerV4RecvMessageCount = _SleBGPStatusPeerV4RecvMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 11),
    _SleBGPStatusPeerV4RecvMessageCount_Type()
)
sleBGPStatusPeerV4RecvMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RecvMessageCount.setStatus("current")
_SleBGPStatusPeerV4RecvNotificationCount_Type = Gauge32
_SleBGPStatusPeerV4RecvNotificationCount_Object = MibTableColumn
sleBGPStatusPeerV4RecvNotificationCount = _SleBGPStatusPeerV4RecvNotificationCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 12),
    _SleBGPStatusPeerV4RecvNotificationCount_Type()
)
sleBGPStatusPeerV4RecvNotificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RecvNotificationCount.setStatus("current")
_SleBGPStatusPeerV4SentMessageCount_Type = Gauge32
_SleBGPStatusPeerV4SentMessageCount_Object = MibTableColumn
sleBGPStatusPeerV4SentMessageCount = _SleBGPStatusPeerV4SentMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 13),
    _SleBGPStatusPeerV4SentMessageCount_Type()
)
sleBGPStatusPeerV4SentMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4SentMessageCount.setStatus("current")
_SleBGPStatusPeerV4SentNotificationCount_Type = Gauge32
_SleBGPStatusPeerV4SentNotificationCount_Object = MibTableColumn
sleBGPStatusPeerV4SentNotificationCount = _SleBGPStatusPeerV4SentNotificationCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 14),
    _SleBGPStatusPeerV4SentNotificationCount_Type()
)
sleBGPStatusPeerV4SentNotificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4SentNotificationCount.setStatus("current")
_SleBGPStatusPeerV4RouteRefreshRecvRequestCount_Type = Gauge32
_SleBGPStatusPeerV4RouteRefreshRecvRequestCount_Object = MibTableColumn
sleBGPStatusPeerV4RouteRefreshRecvRequestCount = _SleBGPStatusPeerV4RouteRefreshRecvRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 15),
    _SleBGPStatusPeerV4RouteRefreshRecvRequestCount_Type()
)
sleBGPStatusPeerV4RouteRefreshRecvRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RouteRefreshRecvRequestCount.setStatus("current")
_SleBGPStatusPeerV4RouteRefreshSentRequestCount_Type = Gauge32
_SleBGPStatusPeerV4RouteRefreshSentRequestCount_Object = MibTableColumn
sleBGPStatusPeerV4RouteRefreshSentRequestCount = _SleBGPStatusPeerV4RouteRefreshSentRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 16),
    _SleBGPStatusPeerV4RouteRefreshSentRequestCount_Type()
)
sleBGPStatusPeerV4RouteRefreshSentRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RouteRefreshSentRequestCount.setStatus("current")
_SleBGPStatusPeerV4RouteAdvTime_Type = Integer32
_SleBGPStatusPeerV4RouteAdvTime_Object = MibTableColumn
sleBGPStatusPeerV4RouteAdvTime = _SleBGPStatusPeerV4RouteAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 17),
    _SleBGPStatusPeerV4RouteAdvTime_Type()
)
sleBGPStatusPeerV4RouteAdvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RouteAdvTime.setStatus("current")
_SleBGPStatusPeerV4EstablishedCount_Type = Gauge32
_SleBGPStatusPeerV4EstablishedCount_Object = MibTableColumn
sleBGPStatusPeerV4EstablishedCount = _SleBGPStatusPeerV4EstablishedCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 18),
    _SleBGPStatusPeerV4EstablishedCount_Type()
)
sleBGPStatusPeerV4EstablishedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4EstablishedCount.setStatus("current")
_SleBGPStatusPeerV4DroppedCount_Type = Gauge32
_SleBGPStatusPeerV4DroppedCount_Object = MibTableColumn
sleBGPStatusPeerV4DroppedCount = _SleBGPStatusPeerV4DroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 19),
    _SleBGPStatusPeerV4DroppedCount_Type()
)
sleBGPStatusPeerV4DroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4DroppedCount.setStatus("current")
_SleBGPStatusPeerV4EBgpMultihopCount_Type = Gauge32
_SleBGPStatusPeerV4EBgpMultihopCount_Object = MibTableColumn
sleBGPStatusPeerV4EBgpMultihopCount = _SleBGPStatusPeerV4EBgpMultihopCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 20),
    _SleBGPStatusPeerV4EBgpMultihopCount_Type()
)
sleBGPStatusPeerV4EBgpMultihopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4EBgpMultihopCount.setStatus("current")
_SleBGPStatusPeerV4LocalHost_Type = OctetString
_SleBGPStatusPeerV4LocalHost_Object = MibTableColumn
sleBGPStatusPeerV4LocalHost = _SleBGPStatusPeerV4LocalHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 21),
    _SleBGPStatusPeerV4LocalHost_Type()
)
sleBGPStatusPeerV4LocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4LocalHost.setStatus("current")
_SleBGPStatusPeerV4LocalPort_Type = Integer32
_SleBGPStatusPeerV4LocalPort_Object = MibTableColumn
sleBGPStatusPeerV4LocalPort = _SleBGPStatusPeerV4LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 22),
    _SleBGPStatusPeerV4LocalPort_Type()
)
sleBGPStatusPeerV4LocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4LocalPort.setStatus("current")
_SleBGPStatusPeerV4ForeignHost_Type = OctetString
_SleBGPStatusPeerV4ForeignHost_Object = MibTableColumn
sleBGPStatusPeerV4ForeignHost = _SleBGPStatusPeerV4ForeignHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 23),
    _SleBGPStatusPeerV4ForeignHost_Type()
)
sleBGPStatusPeerV4ForeignHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4ForeignHost.setStatus("current")
_SleBGPStatusPeerV4ForeignPort_Type = Integer32
_SleBGPStatusPeerV4ForeignPort_Object = MibTableColumn
sleBGPStatusPeerV4ForeignPort = _SleBGPStatusPeerV4ForeignPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 24),
    _SleBGPStatusPeerV4ForeignPort_Type()
)
sleBGPStatusPeerV4ForeignPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4ForeignPort.setStatus("current")
_SleBGPStatusPeerV4RemainNextConnTime_Type = Integer32
_SleBGPStatusPeerV4RemainNextConnTime_Object = MibTableColumn
sleBGPStatusPeerV4RemainNextConnTime = _SleBGPStatusPeerV4RemainNextConnTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 1, 1, 1, 25),
    _SleBGPStatusPeerV4RemainNextConnTime_Type()
)
sleBGPStatusPeerV4RemainNextConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV4RemainNextConnTime.setStatus("current")
_SleBGPStatusPeerV6_ObjectIdentity = ObjectIdentity
sleBGPStatusPeerV6 = _SleBGPStatusPeerV6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2)
)
_SleBGPStatusPeerV6Table_Object = MibTable
sleBGPStatusPeerV6Table = _SleBGPStatusPeerV6Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6Table.setStatus("current")
_SleBGPStatusPeerV6Entry_Object = MibTableRow
sleBGPStatusPeerV6Entry = _SleBGPStatusPeerV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1)
)
sleBGPStatusPeerV6Entry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPStatusPeerV6Name"),
)
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6Entry.setStatus("current")
_SleBGPStatusPeerV6Name_Type = OctetString
_SleBGPStatusPeerV6Name_Object = MibTableColumn
sleBGPStatusPeerV6Name = _SleBGPStatusPeerV6Name_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 1),
    _SleBGPStatusPeerV6Name_Type()
)
sleBGPStatusPeerV6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6Name.setStatus("current")
_SleBGPStatusPeerV6RemoteAs_Type = Gauge32
_SleBGPStatusPeerV6RemoteAs_Object = MibTableColumn
sleBGPStatusPeerV6RemoteAs = _SleBGPStatusPeerV6RemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 2),
    _SleBGPStatusPeerV6RemoteAs_Type()
)
sleBGPStatusPeerV6RemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RemoteAs.setStatus("current")
_SleBGPStatusPeerV6LocalAs_Type = Gauge32
_SleBGPStatusPeerV6LocalAs_Object = MibTableColumn
sleBGPStatusPeerV6LocalAs = _SleBGPStatusPeerV6LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 3),
    _SleBGPStatusPeerV6LocalAs_Type()
)
sleBGPStatusPeerV6LocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6LocalAs.setStatus("current")


class _SleBGPStatusPeerV6LinkState_Type(Integer32):
    """Custom type sleBGPStatusPeerV6LinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_SleBGPStatusPeerV6LinkState_Type.__name__ = "Integer32"
_SleBGPStatusPeerV6LinkState_Object = MibTableColumn
sleBGPStatusPeerV6LinkState = _SleBGPStatusPeerV6LinkState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 4),
    _SleBGPStatusPeerV6LinkState_Type()
)
sleBGPStatusPeerV6LinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6LinkState.setStatus("current")
_SleBGPStatusPeerV6RouterID_Type = IpAddress
_SleBGPStatusPeerV6RouterID_Object = MibTableColumn
sleBGPStatusPeerV6RouterID = _SleBGPStatusPeerV6RouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 5),
    _SleBGPStatusPeerV6RouterID_Type()
)
sleBGPStatusPeerV6RouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RouterID.setStatus("current")


class _SleBGPStatusPeerV6State_Type(Integer32):
    """Custom type sleBGPStatusPeerV6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_SleBGPStatusPeerV6State_Type.__name__ = "Integer32"
_SleBGPStatusPeerV6State_Object = MibTableColumn
sleBGPStatusPeerV6State = _SleBGPStatusPeerV6State_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 6),
    _SleBGPStatusPeerV6State_Type()
)
sleBGPStatusPeerV6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6State.setStatus("current")
_SleBGPStatusPeerV6HoldTime_Type = Integer32
_SleBGPStatusPeerV6HoldTime_Object = MibTableColumn
sleBGPStatusPeerV6HoldTime = _SleBGPStatusPeerV6HoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 7),
    _SleBGPStatusPeerV6HoldTime_Type()
)
sleBGPStatusPeerV6HoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6HoldTime.setStatus("current")
_SleBGPStatusPeerV6KeepAlive_Type = Integer32
_SleBGPStatusPeerV6KeepAlive_Object = MibTableColumn
sleBGPStatusPeerV6KeepAlive = _SleBGPStatusPeerV6KeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 8),
    _SleBGPStatusPeerV6KeepAlive_Type()
)
sleBGPStatusPeerV6KeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6KeepAlive.setStatus("current")
_SleBGPStatusPeerV6Uptime_Type = OctetString
_SleBGPStatusPeerV6Uptime_Object = MibTableColumn
sleBGPStatusPeerV6Uptime = _SleBGPStatusPeerV6Uptime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 9),
    _SleBGPStatusPeerV6Uptime_Type()
)
sleBGPStatusPeerV6Uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6Uptime.setStatus("current")
_SleBGPStatusPeerV6LastReadTime_Type = OctetString
_SleBGPStatusPeerV6LastReadTime_Object = MibTableColumn
sleBGPStatusPeerV6LastReadTime = _SleBGPStatusPeerV6LastReadTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 10),
    _SleBGPStatusPeerV6LastReadTime_Type()
)
sleBGPStatusPeerV6LastReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6LastReadTime.setStatus("current")
_SleBGPStatusPeerV6RecvMessageCount_Type = Gauge32
_SleBGPStatusPeerV6RecvMessageCount_Object = MibTableColumn
sleBGPStatusPeerV6RecvMessageCount = _SleBGPStatusPeerV6RecvMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 11),
    _SleBGPStatusPeerV6RecvMessageCount_Type()
)
sleBGPStatusPeerV6RecvMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RecvMessageCount.setStatus("current")
_SleBGPStatusPeerV6RecvNotificationCount_Type = Gauge32
_SleBGPStatusPeerV6RecvNotificationCount_Object = MibTableColumn
sleBGPStatusPeerV6RecvNotificationCount = _SleBGPStatusPeerV6RecvNotificationCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 12),
    _SleBGPStatusPeerV6RecvNotificationCount_Type()
)
sleBGPStatusPeerV6RecvNotificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RecvNotificationCount.setStatus("current")
_SleBGPStatusPeerV6SentMessageCount_Type = Gauge32
_SleBGPStatusPeerV6SentMessageCount_Object = MibTableColumn
sleBGPStatusPeerV6SentMessageCount = _SleBGPStatusPeerV6SentMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 13),
    _SleBGPStatusPeerV6SentMessageCount_Type()
)
sleBGPStatusPeerV6SentMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6SentMessageCount.setStatus("current")
_SleBGPStatusPeerV6SentNotificationCount_Type = Gauge32
_SleBGPStatusPeerV6SentNotificationCount_Object = MibTableColumn
sleBGPStatusPeerV6SentNotificationCount = _SleBGPStatusPeerV6SentNotificationCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 14),
    _SleBGPStatusPeerV6SentNotificationCount_Type()
)
sleBGPStatusPeerV6SentNotificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6SentNotificationCount.setStatus("current")
_SleBGPStatusPeerV6RouteRefreshRecvRequestCount_Type = Gauge32
_SleBGPStatusPeerV6RouteRefreshRecvRequestCount_Object = MibTableColumn
sleBGPStatusPeerV6RouteRefreshRecvRequestCount = _SleBGPStatusPeerV6RouteRefreshRecvRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 15),
    _SleBGPStatusPeerV6RouteRefreshRecvRequestCount_Type()
)
sleBGPStatusPeerV6RouteRefreshRecvRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RouteRefreshRecvRequestCount.setStatus("current")
_SleBGPStatusPeerV6RouteRefreshSentRequestCount_Type = Gauge32
_SleBGPStatusPeerV6RouteRefreshSentRequestCount_Object = MibTableColumn
sleBGPStatusPeerV6RouteRefreshSentRequestCount = _SleBGPStatusPeerV6RouteRefreshSentRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 16),
    _SleBGPStatusPeerV6RouteRefreshSentRequestCount_Type()
)
sleBGPStatusPeerV6RouteRefreshSentRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RouteRefreshSentRequestCount.setStatus("current")
_SleBGPStatusPeerV6RouteAdvTime_Type = Integer32
_SleBGPStatusPeerV6RouteAdvTime_Object = MibTableColumn
sleBGPStatusPeerV6RouteAdvTime = _SleBGPStatusPeerV6RouteAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 17),
    _SleBGPStatusPeerV6RouteAdvTime_Type()
)
sleBGPStatusPeerV6RouteAdvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RouteAdvTime.setStatus("current")
_SleBGPStatusPeerV6EstablishedCount_Type = Gauge32
_SleBGPStatusPeerV6EstablishedCount_Object = MibTableColumn
sleBGPStatusPeerV6EstablishedCount = _SleBGPStatusPeerV6EstablishedCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 18),
    _SleBGPStatusPeerV6EstablishedCount_Type()
)
sleBGPStatusPeerV6EstablishedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6EstablishedCount.setStatus("current")
_SleBGPStatusPeerV6DroppedCount_Type = Gauge32
_SleBGPStatusPeerV6DroppedCount_Object = MibTableColumn
sleBGPStatusPeerV6DroppedCount = _SleBGPStatusPeerV6DroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 19),
    _SleBGPStatusPeerV6DroppedCount_Type()
)
sleBGPStatusPeerV6DroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6DroppedCount.setStatus("current")
_SleBGPStatusPeerV6EBgpMultihopCount_Type = Gauge32
_SleBGPStatusPeerV6EBgpMultihopCount_Object = MibTableColumn
sleBGPStatusPeerV6EBgpMultihopCount = _SleBGPStatusPeerV6EBgpMultihopCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 20),
    _SleBGPStatusPeerV6EBgpMultihopCount_Type()
)
sleBGPStatusPeerV6EBgpMultihopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6EBgpMultihopCount.setStatus("current")
_SleBGPStatusPeerV6LocalHost_Type = OctetString
_SleBGPStatusPeerV6LocalHost_Object = MibTableColumn
sleBGPStatusPeerV6LocalHost = _SleBGPStatusPeerV6LocalHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 21),
    _SleBGPStatusPeerV6LocalHost_Type()
)
sleBGPStatusPeerV6LocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6LocalHost.setStatus("current")
_SleBGPStatusPeerV6LocalPort_Type = Integer32
_SleBGPStatusPeerV6LocalPort_Object = MibTableColumn
sleBGPStatusPeerV6LocalPort = _SleBGPStatusPeerV6LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 22),
    _SleBGPStatusPeerV6LocalPort_Type()
)
sleBGPStatusPeerV6LocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6LocalPort.setStatus("current")
_SleBGPStatusPeerV6ForeignHost_Type = OctetString
_SleBGPStatusPeerV6ForeignHost_Object = MibTableColumn
sleBGPStatusPeerV6ForeignHost = _SleBGPStatusPeerV6ForeignHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 23),
    _SleBGPStatusPeerV6ForeignHost_Type()
)
sleBGPStatusPeerV6ForeignHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6ForeignHost.setStatus("current")
_SleBGPStatusPeerV6ForeignPort_Type = Integer32
_SleBGPStatusPeerV6ForeignPort_Object = MibTableColumn
sleBGPStatusPeerV6ForeignPort = _SleBGPStatusPeerV6ForeignPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 24),
    _SleBGPStatusPeerV6ForeignPort_Type()
)
sleBGPStatusPeerV6ForeignPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6ForeignPort.setStatus("current")
_SleBGPStatusPeerV6RemainNextConnTime_Type = Integer32
_SleBGPStatusPeerV6RemainNextConnTime_Object = MibTableColumn
sleBGPStatusPeerV6RemainNextConnTime = _SleBGPStatusPeerV6RemainNextConnTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 1, 2, 1, 1, 25),
    _SleBGPStatusPeerV6RemainNextConnTime_Type()
)
sleBGPStatusPeerV6RemainNextConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPStatusPeerV6RemainNextConnTime.setStatus("current")
_SleBGPRoutes_ObjectIdentity = ObjectIdentity
sleBGPRoutes = _SleBGPRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2)
)
_SleBGPRoutesV4_ObjectIdentity = ObjectIdentity
sleBGPRoutesV4 = _SleBGPRoutesV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1)
)
_SleBGPRoutesV4Table_Object = MibTable
sleBGPRoutesV4Table = _SleBGPRoutesV4Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleBGPRoutesV4Table.setStatus("current")
_SleBGPRoutesV4Entry_Object = MibTableRow
sleBGPRoutesV4Entry = _SleBGPRoutesV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1)
)
sleBGPRoutesV4Entry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPRoutesV4SAFIType"),
    (0, "SLE-BGP-MIB", "sleBGPRoutesV4RoutePrefix"),
    (0, "SLE-BGP-MIB", "sleBGPRoutesV4Nexthop"),
)
if mibBuilder.loadTexts:
    sleBGPRoutesV4Entry.setStatus("current")


class _SleBGPRoutesV4SAFIType_Type(Integer32):
    """Custom type sleBGPRoutesV4SAFIType based on Integer32"""
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


_SleBGPRoutesV4SAFIType_Type.__name__ = "Integer32"
_SleBGPRoutesV4SAFIType_Object = MibTableColumn
sleBGPRoutesV4SAFIType = _SleBGPRoutesV4SAFIType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 1),
    _SleBGPRoutesV4SAFIType_Type()
)
sleBGPRoutesV4SAFIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4SAFIType.setStatus("current")
_SleBGPRoutesV4RoutePrefix_Type = OctetString
_SleBGPRoutesV4RoutePrefix_Object = MibTableColumn
sleBGPRoutesV4RoutePrefix = _SleBGPRoutesV4RoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 2),
    _SleBGPRoutesV4RoutePrefix_Type()
)
sleBGPRoutesV4RoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4RoutePrefix.setStatus("current")
_SleBGPRoutesV4Nexthop_Type = OctetString
_SleBGPRoutesV4Nexthop_Object = MibTableColumn
sleBGPRoutesV4Nexthop = _SleBGPRoutesV4Nexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 3),
    _SleBGPRoutesV4Nexthop_Type()
)
sleBGPRoutesV4Nexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4Nexthop.setStatus("current")


class _SleBGPRoutesV4NexthopSelected_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopSelected based on Integer32"""
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


_SleBGPRoutesV4NexthopSelected_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopSelected_Object = MibTableColumn
sleBGPRoutesV4NexthopSelected = _SleBGPRoutesV4NexthopSelected_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 4),
    _SleBGPRoutesV4NexthopSelected_Type()
)
sleBGPRoutesV4NexthopSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopSelected.setStatus("current")


class _SleBGPRoutesV4NexthopInternal_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_SleBGPRoutesV4NexthopInternal_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopInternal_Object = MibTableColumn
sleBGPRoutesV4NexthopInternal = _SleBGPRoutesV4NexthopInternal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 5),
    _SleBGPRoutesV4NexthopInternal_Type()
)
sleBGPRoutesV4NexthopInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopInternal.setStatus("current")


class _SleBGPRoutesV4NexthopMed_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPRoutesV4NexthopMed_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopMed_Object = MibTableColumn
sleBGPRoutesV4NexthopMed = _SleBGPRoutesV4NexthopMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 6),
    _SleBGPRoutesV4NexthopMed_Type()
)
sleBGPRoutesV4NexthopMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopMed.setStatus("current")
_SleBGPRoutesV4NexthopLocPref_Type = Gauge32
_SleBGPRoutesV4NexthopLocPref_Object = MibTableColumn
sleBGPRoutesV4NexthopLocPref = _SleBGPRoutesV4NexthopLocPref_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 7),
    _SleBGPRoutesV4NexthopLocPref_Type()
)
sleBGPRoutesV4NexthopLocPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopLocPref.setStatus("current")


class _SleBGPRoutesV4NexthopWeight_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPRoutesV4NexthopWeight_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopWeight_Object = MibTableColumn
sleBGPRoutesV4NexthopWeight = _SleBGPRoutesV4NexthopWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 8),
    _SleBGPRoutesV4NexthopWeight_Type()
)
sleBGPRoutesV4NexthopWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopWeight.setStatus("current")


class _SleBGPRoutesV4NexthopSuppress_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopSuppress based on Integer32"""
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


_SleBGPRoutesV4NexthopSuppress_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopSuppress_Object = MibTableColumn
sleBGPRoutesV4NexthopSuppress = _SleBGPRoutesV4NexthopSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 9),
    _SleBGPRoutesV4NexthopSuppress_Type()
)
sleBGPRoutesV4NexthopSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopSuppress.setStatus("current")


class _SleBGPRoutesV4NexthopValid_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopValid based on Integer32"""
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


_SleBGPRoutesV4NexthopValid_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopValid_Object = MibTableColumn
sleBGPRoutesV4NexthopValid = _SleBGPRoutesV4NexthopValid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 10),
    _SleBGPRoutesV4NexthopValid_Type()
)
sleBGPRoutesV4NexthopValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopValid.setStatus("current")


class _SleBGPRoutesV4NexthopStale_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopStale based on Integer32"""
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


_SleBGPRoutesV4NexthopStale_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopStale_Object = MibTableColumn
sleBGPRoutesV4NexthopStale = _SleBGPRoutesV4NexthopStale_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 11),
    _SleBGPRoutesV4NexthopStale_Type()
)
sleBGPRoutesV4NexthopStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopStale.setStatus("current")


class _SleBGPRoutesV4NexthopDamped_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopDamped based on Integer32"""
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


_SleBGPRoutesV4NexthopDamped_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopDamped_Object = MibTableColumn
sleBGPRoutesV4NexthopDamped = _SleBGPRoutesV4NexthopDamped_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 12),
    _SleBGPRoutesV4NexthopDamped_Type()
)
sleBGPRoutesV4NexthopDamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopDamped.setStatus("current")


class _SleBGPRoutesV4NexthopStaleHistory_Type(Integer32):
    """Custom type sleBGPRoutesV4NexthopStaleHistory based on Integer32"""
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


_SleBGPRoutesV4NexthopStaleHistory_Type.__name__ = "Integer32"
_SleBGPRoutesV4NexthopStaleHistory_Object = MibTableColumn
sleBGPRoutesV4NexthopStaleHistory = _SleBGPRoutesV4NexthopStaleHistory_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 1, 1, 1, 13),
    _SleBGPRoutesV4NexthopStaleHistory_Type()
)
sleBGPRoutesV4NexthopStaleHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV4NexthopStaleHistory.setStatus("current")
_SleBGPRoutesV6_ObjectIdentity = ObjectIdentity
sleBGPRoutesV6 = _SleBGPRoutesV6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2)
)
_SleBGPRoutesV6Table_Object = MibTable
sleBGPRoutesV6Table = _SleBGPRoutesV6Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleBGPRoutesV6Table.setStatus("current")
_SleBGPRoutesV6Entry_Object = MibTableRow
sleBGPRoutesV6Entry = _SleBGPRoutesV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1)
)
sleBGPRoutesV6Entry.setIndexNames(
    (0, "SLE-BGP-MIB", "sleBGPRoutesV4SAFIType"),
    (0, "SLE-BGP-MIB", "sleBGPRoutesV4RoutePrefix"),
    (0, "SLE-BGP-MIB", "sleBGPRoutesV4Nexthop"),
)
if mibBuilder.loadTexts:
    sleBGPRoutesV6Entry.setStatus("current")


class _SleBGPRoutesV6SAFIType_Type(Integer32):
    """Custom type sleBGPRoutesV6SAFIType based on Integer32"""
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


_SleBGPRoutesV6SAFIType_Type.__name__ = "Integer32"
_SleBGPRoutesV6SAFIType_Object = MibTableColumn
sleBGPRoutesV6SAFIType = _SleBGPRoutesV6SAFIType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 1),
    _SleBGPRoutesV6SAFIType_Type()
)
sleBGPRoutesV6SAFIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6SAFIType.setStatus("current")
_SleBGPRoutesV6RoutePrefix_Type = OctetString
_SleBGPRoutesV6RoutePrefix_Object = MibTableColumn
sleBGPRoutesV6RoutePrefix = _SleBGPRoutesV6RoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 2),
    _SleBGPRoutesV6RoutePrefix_Type()
)
sleBGPRoutesV6RoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6RoutePrefix.setStatus("current")
_SleBGPRoutesV6Nexthop_Type = OctetString
_SleBGPRoutesV6Nexthop_Object = MibTableColumn
sleBGPRoutesV6Nexthop = _SleBGPRoutesV6Nexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 3),
    _SleBGPRoutesV6Nexthop_Type()
)
sleBGPRoutesV6Nexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6Nexthop.setStatus("current")


class _SleBGPRoutesV6NexthopSelected_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopSelected based on Integer32"""
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


_SleBGPRoutesV6NexthopSelected_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopSelected_Object = MibTableColumn
sleBGPRoutesV6NexthopSelected = _SleBGPRoutesV6NexthopSelected_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 4),
    _SleBGPRoutesV6NexthopSelected_Type()
)
sleBGPRoutesV6NexthopSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopSelected.setStatus("current")


class _SleBGPRoutesV6NexthopInternal_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_SleBGPRoutesV6NexthopInternal_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopInternal_Object = MibTableColumn
sleBGPRoutesV6NexthopInternal = _SleBGPRoutesV6NexthopInternal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 5),
    _SleBGPRoutesV6NexthopInternal_Type()
)
sleBGPRoutesV6NexthopInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopInternal.setStatus("current")


class _SleBGPRoutesV6NexthopMed_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPRoutesV6NexthopMed_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopMed_Object = MibTableColumn
sleBGPRoutesV6NexthopMed = _SleBGPRoutesV6NexthopMed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 6),
    _SleBGPRoutesV6NexthopMed_Type()
)
sleBGPRoutesV6NexthopMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopMed.setStatus("current")
_SleBGPRoutesV6NexthopLocPref_Type = Gauge32
_SleBGPRoutesV6NexthopLocPref_Object = MibTableColumn
sleBGPRoutesV6NexthopLocPref = _SleBGPRoutesV6NexthopLocPref_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 7),
    _SleBGPRoutesV6NexthopLocPref_Type()
)
sleBGPRoutesV6NexthopLocPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopLocPref.setStatus("current")


class _SleBGPRoutesV6NexthopWeight_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleBGPRoutesV6NexthopWeight_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopWeight_Object = MibTableColumn
sleBGPRoutesV6NexthopWeight = _SleBGPRoutesV6NexthopWeight_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 8),
    _SleBGPRoutesV6NexthopWeight_Type()
)
sleBGPRoutesV6NexthopWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopWeight.setStatus("current")


class _SleBGPRoutesV6NexthopSuppress_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopSuppress based on Integer32"""
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


_SleBGPRoutesV6NexthopSuppress_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopSuppress_Object = MibTableColumn
sleBGPRoutesV6NexthopSuppress = _SleBGPRoutesV6NexthopSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 9),
    _SleBGPRoutesV6NexthopSuppress_Type()
)
sleBGPRoutesV6NexthopSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopSuppress.setStatus("current")


class _SleBGPRoutesV6NexthopValid_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("disable", 0)
    )


_SleBGPRoutesV6NexthopValid_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopValid_Object = MibTableColumn
sleBGPRoutesV6NexthopValid = _SleBGPRoutesV6NexthopValid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 10),
    _SleBGPRoutesV6NexthopValid_Type()
)
sleBGPRoutesV6NexthopValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopValid.setStatus("current")


class _SleBGPRoutesV6NexthopStale_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopStale based on Integer32"""
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


_SleBGPRoutesV6NexthopStale_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopStale_Object = MibTableColumn
sleBGPRoutesV6NexthopStale = _SleBGPRoutesV6NexthopStale_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 11),
    _SleBGPRoutesV6NexthopStale_Type()
)
sleBGPRoutesV6NexthopStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopStale.setStatus("current")


class _SleBGPRoutesV6NexthopDamped_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopDamped based on Integer32"""
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


_SleBGPRoutesV6NexthopDamped_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopDamped_Object = MibTableColumn
sleBGPRoutesV6NexthopDamped = _SleBGPRoutesV6NexthopDamped_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 12),
    _SleBGPRoutesV6NexthopDamped_Type()
)
sleBGPRoutesV6NexthopDamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopDamped.setStatus("current")


class _SleBGPRoutesV6NexthopStaleHistory_Type(Integer32):
    """Custom type sleBGPRoutesV6NexthopStaleHistory based on Integer32"""
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


_SleBGPRoutesV6NexthopStaleHistory_Type.__name__ = "Integer32"
_SleBGPRoutesV6NexthopStaleHistory_Object = MibTableColumn
sleBGPRoutesV6NexthopStaleHistory = _SleBGPRoutesV6NexthopStaleHistory_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 6, 2, 2, 1, 1, 13),
    _SleBGPRoutesV6NexthopStaleHistory_Type()
)
sleBGPRoutesV6NexthopStaleHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBGPRoutesV6NexthopStaleHistory.setStatus("current")

# Managed Objects groups

sleBGPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 7)
)
sleBGPGroup.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseAsNumber"),
        ("SLE-BGP-MIB", "sleBGPBaseConfigType"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771PathSelect"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771Strict"),
        ("SLE-BGP-MIB", "sleBGPBaseAggregateNextHop"),
        ("SLE-BGP-MIB", "sleBGPBaseExtendAsnCap"),
        ("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlStatus"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimer"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlAsNumber"),
        ("SLE-BGP-MIB", "sleBGPBaseControlConfigType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlRfc1771PathSelect"),
        ("SLE-BGP-MIB", "sleBGPBaseControlRfc1771Strict"),
        ("SLE-BGP-MIB", "sleBGPBaseControlAggregateNextHop"),
        ("SLE-BGP-MIB", "sleBGPBaseControlExtendAsnCap"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyMode"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDirection"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearSoft"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPrefixFilter"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPeerName"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearAddr"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearViewName"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDampFlag"),
        ("SLE-BGP-MIB", "sleBGPInfoRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoLogNeighborChange"),
        ("SLE-BGP-MIB", "sleBGPInfoAlwaysCompareMed"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathAsPathIgnore"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareConfedAsPath"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedConfed"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedMisAsWorst"),
        ("SLE-BGP-MIB", "sleBGPInfoClientToClient"),
        ("SLE-BGP-MIB", "sleBGPInfoClusterID"),
        ("SLE-BGP-MIB", "sleBGPInfoConfederationID"),
        ("SLE-BGP-MIB", "sleBGPInfoDeterministicMed"),
        ("SLE-BGP-MIB", "sleBGPInfoEnforceFirstAs"),
        ("SLE-BGP-MIB", "sleBGPInfoFastExternalFailOver"),
        ("SLE-BGP-MIB", "sleBGPInfoGracefulRestartTime"),
        ("SLE-BGP-MIB", "sleBGPInfoGracefulStalepathTime"),
        ("SLE-BGP-MIB", "sleBGPInfoScanTime"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerStatus"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoSnmpNotification"),
        ("SLE-BGP-MIB", "sleBGPInfoUpdateDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoExternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoInternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoLocalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPath"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPathIBGP"),
        ("SLE-BGP-MIB", "sleBGPInfoKeepAliveInterval"),
        ("SLE-BGP-MIB", "sleBGPInfoHoldTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlStatus"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimer"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoControlRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlLogNeighborChange"),
        ("SLE-BGP-MIB", "sleBGPInfoControlAlwaysCompareMed"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathAsPathIgnore"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareConfedAsPath"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareMedConfed"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareMedMisAsWorst"),
        ("SLE-BGP-MIB", "sleBGPInfoControlClientToClient"),
        ("SLE-BGP-MIB", "sleBGPInfoControlClusterID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlConfederationID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlDeterministicMed"),
        ("SLE-BGP-MIB", "sleBGPInfoControlEnforceFirstAs"),
        ("SLE-BGP-MIB", "sleBGPInfoControlFastExternalFailOver"),
        ("SLE-BGP-MIB", "sleBGPInfoControlGracefulRestartTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlGracefulStalepathTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlScanTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlNexthopTriggerStatus"),
        ("SLE-BGP-MIB", "sleBGPInfoControlNexthopTriggerDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoControlSnmpNotification"),
        ("SLE-BGP-MIB", "sleBGPInfoControlUpdateDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoControlExternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlInternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlLocalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlMaximumPath"),
        ("SLE-BGP-MIB", "sleBGPInfoControlMaximumPathIBGP"),
        ("SLE-BGP-MIB", "sleBGPInfoControlKeepAliveInterval"),
        ("SLE-BGP-MIB", "sleBGPInfoControlHoldTime"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceValue"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceAccName"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlValue"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlAccName"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupName"),
        ("SLE-BGP-MIB", "sleBGPPeerAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerPort"),
        ("SLE-BGP-MIB", "sleBGPPeerRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerIfname"),
        ("SLE-BGP-MIB", "sleBGPPeerCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerPassword"),
        ("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlStatus"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimer"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"),
        ("SLE-BGP-MIB", "sleBGPPeerControlAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerControlGroupName"),
        ("SLE-BGP-MIB", "sleBGPPeerControlAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerControlDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerControlWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerControlEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerControlPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerControlUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerControlPort"),
        ("SLE-BGP-MIB", "sleBGPPeerControlRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerControlShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerControlKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerControlStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerControlIfname"),
        ("SLE-BGP-MIB", "sleBGPPeerControlCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerControlCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerControlEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerControlPassword"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPort"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPassword"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStatus"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimer"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlPort"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlPassword"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseNetworkCheck"),
        ("SLE-BGP-MIB", "sleBGPAFBaseSync"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDefOrg"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampReuse"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampMaxSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampUnReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlNetworkCheck"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlSync"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDefOrg"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampReuse"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampMaxSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampUnReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFRedistMode"),
        ("SLE-BGP-MIB", "sleBGPAFRedistType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistProtoType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlProtoType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrMode"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrAsSet"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrSummOnly"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlAsSet"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlSummOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkMode"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkBackdoor"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlBackdoor"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlRoutemap"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4Name"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RemoteAs"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4LocalAs"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4LinkState"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4State"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4HoldTime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4KeepAlive"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4Uptime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4LastReadTime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RecvMessageCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RecvNotificationCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4SentMessageCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4SentNotificationCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RouteRefreshRecvRequestCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RouteRefreshSentRequestCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RouteAdvTime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4EstablishedCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4DroppedCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4EBgpMultihopCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4LocalHost"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4LocalPort"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4ForeignHost"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4ForeignPort"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RemainNextConnTime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6Name"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RemoteAs"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6LocalAs"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6LinkState"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6State"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6HoldTime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6KeepAlive"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6Uptime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6LastReadTime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RecvMessageCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RecvNotificationCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6SentMessageCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6SentNotificationCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RouteRefreshRecvRequestCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RouteRefreshSentRequestCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RouteAdvTime"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6EstablishedCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6DroppedCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6EBgpMultihopCount"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6LocalHost"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6LocalPort"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6ForeignHost"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6ForeignPort"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RemainNextConnTime"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4SAFIType"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4RoutePrefix"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4Nexthop"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopMed"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopLocPref"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopWeight"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopSuppress"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopValid"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopStale"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopDamped"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopStaleHistory"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopSelected"),
        ("SLE-BGP-MIB", "sleBGPRoutesV4NexthopInternal"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6SAFIType"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6RoutePrefix"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6Nexthop"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopMed"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopLocPref"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopWeight"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopSuppress"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopValid"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopStale"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopDamped"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopStaleHistory"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopSelected"),
        ("SLE-BGP-MIB", "sleBGPRoutesV6NexthopInternal"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV4RouterID"),
        ("SLE-BGP-MIB", "sleBGPStatusPeerV6RouterID"))
)
if mibBuilder.loadTexts:
    sleBGPGroup.setStatus("current")


# Notification objects

sleBGPBaseAsModeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 1)
)
sleBGPBaseAsModeCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseAsNumber"))
)
if mibBuilder.loadTexts:
    sleBGPBaseAsModeCreated.setStatus(
        "current"
    )

sleBGPBaseAsModeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 2)
)
sleBGPBaseAsModeDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlAsNumber"))
)
if mibBuilder.loadTexts:
    sleBGPBaseAsModeDeleted.setStatus(
        "current"
    )

sleBGPBaseConfigTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 3)
)
sleBGPBaseConfigTypeChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseConfigType"))
)
if mibBuilder.loadTexts:
    sleBGPBaseConfigTypeChanged.setStatus(
        "current"
    )

sleBGPBaseRfc1771PathSelectChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 4)
)
sleBGPBaseRfc1771PathSelectChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771PathSelect"))
)
if mibBuilder.loadTexts:
    sleBGPBaseRfc1771PathSelectChanged.setStatus(
        "current"
    )

sleBGPBaseRfc1771StrictChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 5)
)
sleBGPBaseRfc1771StrictChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771Strict"))
)
if mibBuilder.loadTexts:
    sleBGPBaseRfc1771StrictChanged.setStatus(
        "current"
    )

sleBGPBaseAggregateNextHopChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 6)
)
sleBGPBaseAggregateNextHopChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseAggregateNextHop"))
)
if mibBuilder.loadTexts:
    sleBGPBaseAggregateNextHopChanged.setStatus(
        "current"
    )

sleBGPBaseExtendAsnCapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 7)
)
sleBGPBaseExtendAsnCapChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseExtendAsnCap"))
)
if mibBuilder.loadTexts:
    sleBGPBaseExtendAsnCapChanged.setStatus(
        "current"
    )

sleBGPBaseAllCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 8)
)
sleBGPBaseAllCleared.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyMode"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDirection"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearSoft"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPrefixFilter"))
)
if mibBuilder.loadTexts:
    sleBGPBaseAllCleared.setStatus(
        "current"
    )

sleBGPBaseAsNumberCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 9)
)
sleBGPBaseAsNumberCleared.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlAsNumber"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyMode"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDirection"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearSoft"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPrefixFilter"))
)
if mibBuilder.loadTexts:
    sleBGPBaseAsNumberCleared.setStatus(
        "current"
    )

sleBGPBasePeerCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 10)
)
sleBGPBasePeerCleared.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPeerName"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyMode"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDirection"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearSoft"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPrefixFilter"))
)
if mibBuilder.loadTexts:
    sleBGPBasePeerCleared.setStatus(
        "current"
    )

sleBGPBaseDampCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 11)
)
sleBGPBaseDampCleared.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearAddr"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDampFlag"))
)
if mibBuilder.loadTexts:
    sleBGPBaseDampCleared.setStatus(
        "current"
    )

sleBGPBaseExternalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 12)
)
sleBGPBaseExternalCleared.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyMode"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDirection"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearSoft"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPrefixFilter"))
)
if mibBuilder.loadTexts:
    sleBGPBaseExternalCleared.setStatus(
        "current"
    )

sleBGPBaseViewCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 1, 3, 13)
)
sleBGPBaseViewCleared.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearViewName"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDirection"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearSoft"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPrefixFilter"))
)
if mibBuilder.loadTexts:
    sleBGPBaseViewCleared.setStatus(
        "current"
    )

sleBGPInfoRouterIDCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 1)
)
sleBGPInfoRouterIDCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoRouterID"))
)
if mibBuilder.loadTexts:
    sleBGPInfoRouterIDCreated.setStatus(
        "current"
    )

sleBGPInfoRouterIDDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 2)
)
sleBGPInfoRouterIDDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoControlRouterID"))
)
if mibBuilder.loadTexts:
    sleBGPInfoRouterIDDeleted.setStatus(
        "current"
    )

sleBGPInfoLogNeighborChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 3)
)
sleBGPInfoLogNeighborChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoLogNeighborChange"))
)
if mibBuilder.loadTexts:
    sleBGPInfoLogNeighborChanged.setStatus(
        "current"
    )

sleBGPInfoAlwaysCompareMedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 4)
)
sleBGPInfoAlwaysCompareMedChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoAlwaysCompareMed"))
)
if mibBuilder.loadTexts:
    sleBGPInfoAlwaysCompareMedChanged.setStatus(
        "current"
    )

sleBGPInfoBestPathAsPathIgnoreChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 5)
)
sleBGPInfoBestPathAsPathIgnoreChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathAsPathIgnore"))
)
if mibBuilder.loadTexts:
    sleBGPInfoBestPathAsPathIgnoreChanged.setStatus(
        "current"
    )

sleBGPInfoBestPathCompareConfedAsPathChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 6)
)
sleBGPInfoBestPathCompareConfedAsPathChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareConfedAsPath"))
)
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareConfedAsPathChanged.setStatus(
        "current"
    )

sleBGPInfoBestPathCompareRouterIDChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 7)
)
sleBGPInfoBestPathCompareRouterIDChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareRouterID"))
)
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareRouterIDChanged.setStatus(
        "current"
    )

sleBGPInfoBestPathCompareMedConfedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 8)
)
sleBGPInfoBestPathCompareMedConfedChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedConfed"))
)
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareMedConfedChanged.setStatus(
        "current"
    )

sleBGPInfoBestPathCompareMedMisAsWorstChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 9)
)
sleBGPInfoBestPathCompareMedMisAsWorstChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedMisAsWorst"))
)
if mibBuilder.loadTexts:
    sleBGPInfoBestPathCompareMedMisAsWorstChanged.setStatus(
        "current"
    )

sleBGPInfoClientToClientChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 10)
)
sleBGPInfoClientToClientChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoClientToClient"))
)
if mibBuilder.loadTexts:
    sleBGPInfoClientToClientChanged.setStatus(
        "current"
    )

sleBGPInfoClusterIDCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 11)
)
sleBGPInfoClusterIDCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoClusterID"))
)
if mibBuilder.loadTexts:
    sleBGPInfoClusterIDCreated.setStatus(
        "current"
    )

sleBGPInfoClusterIDDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 12)
)
sleBGPInfoClusterIDDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoControlClusterID"))
)
if mibBuilder.loadTexts:
    sleBGPInfoClusterIDDeleted.setStatus(
        "current"
    )

sleBGPInfoConfederationIDChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 13)
)
sleBGPInfoConfederationIDChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoConfederationID"))
)
if mibBuilder.loadTexts:
    sleBGPInfoConfederationIDChanged.setStatus(
        "current"
    )

sleBGPInfoDeterministicMedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 14)
)
sleBGPInfoDeterministicMedChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoDeterministicMed"))
)
if mibBuilder.loadTexts:
    sleBGPInfoDeterministicMedChanged.setStatus(
        "current"
    )

sleBGPInfoEnforceFirstAsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 15)
)
sleBGPInfoEnforceFirstAsChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoEnforceFirstAs"))
)
if mibBuilder.loadTexts:
    sleBGPInfoEnforceFirstAsChanged.setStatus(
        "current"
    )

sleBGPInfoFastExternalFailOverChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 16)
)
sleBGPInfoFastExternalFailOverChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoFastExternalFailOver"))
)
if mibBuilder.loadTexts:
    sleBGPInfoFastExternalFailOverChanged.setStatus(
        "current"
    )

sleBGPInfoGracefulRestartProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 17)
)
sleBGPInfoGracefulRestartProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoGracefulRestartTime"),
        ("SLE-BGP-MIB", "sleBGPInfoGracefulStalepathTime"))
)
if mibBuilder.loadTexts:
    sleBGPInfoGracefulRestartProfileChanged.setStatus(
        "current"
    )

sleBGPInfoScanTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 18)
)
sleBGPInfoScanTimeChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoScanTime"))
)
if mibBuilder.loadTexts:
    sleBGPInfoScanTimeChanged.setStatus(
        "current"
    )

sleBGPInfoNexthopTriggerStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 19)
)
sleBGPInfoNexthopTriggerStatusChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerStatus"))
)
if mibBuilder.loadTexts:
    sleBGPInfoNexthopTriggerStatusChanged.setStatus(
        "current"
    )

sleBGPInfoNexthopTriggerDelayChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 20)
)
sleBGPInfoNexthopTriggerDelayChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerDelay"))
)
if mibBuilder.loadTexts:
    sleBGPInfoNexthopTriggerDelayChanged.setStatus(
        "current"
    )

sleBGPInfoSnmpNotificationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 21)
)
sleBGPInfoSnmpNotificationChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoSnmpNotification"))
)
if mibBuilder.loadTexts:
    sleBGPInfoSnmpNotificationChanged.setStatus(
        "current"
    )

sleBGPInfoUpdateDelayChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 22)
)
sleBGPInfoUpdateDelayChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoUpdateDelay"))
)
if mibBuilder.loadTexts:
    sleBGPInfoUpdateDelayChanged.setStatus(
        "current"
    )

sleBGPInfoDistanceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 23)
)
sleBGPInfoDistanceCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoExternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoInternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoLocalRouteDistance"))
)
if mibBuilder.loadTexts:
    sleBGPInfoDistanceCreated.setStatus(
        "current"
    )

sleBGPInfoDistanceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 24)
)
sleBGPInfoDistanceDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoControlExternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlInternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlLocalRouteDistance"))
)
if mibBuilder.loadTexts:
    sleBGPInfoDistanceDeleted.setStatus(
        "current"
    )

sleBGPInfoMaximumPathChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 25)
)
sleBGPInfoMaximumPathChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPath"))
)
if mibBuilder.loadTexts:
    sleBGPInfoMaximumPathChanged.setStatus(
        "current"
    )

sleBGPInfoMaximumPathIBGPChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 26)
)
sleBGPInfoMaximumPathIBGPChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPathIBGP"))
)
if mibBuilder.loadTexts:
    sleBGPInfoMaximumPathIBGPChanged.setStatus(
        "current"
    )

sleBGPInfoTimersChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 2, 3, 27)
)
sleBGPInfoTimersChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoKeepAliveInterval"),
        ("SLE-BGP-MIB", "sleBGPInfoHoldTime"))
)
if mibBuilder.loadTexts:
    sleBGPInfoTimersChanged.setStatus(
        "current"
    )

sleBGPAdminDistanceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 3, 1)
)
sleBGPAdminDistanceCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAdminDistanceControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceValue"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceAccName"))
)
if mibBuilder.loadTexts:
    sleBGPAdminDistanceCreated.setStatus(
        "current"
    )

sleBGPAdminDistanceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 3, 3, 2)
)
sleBGPAdminDistanceDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseAsNumber"),
        ("SLE-BGP-MIB", "sleBGPBaseConfigType"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771PathSelect"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771Strict"),
        ("SLE-BGP-MIB", "sleBGPBaseAggregateNextHop"),
        ("SLE-BGP-MIB", "sleBGPBaseExtendAsnCap"),
        ("SLE-BGP-MIB", "sleBGPBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPBaseControlStatus"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimer"),
        ("SLE-BGP-MIB", "sleBGPBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPBaseControlAsNumber"),
        ("SLE-BGP-MIB", "sleBGPBaseControlConfigType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlRfc1771PathSelect"),
        ("SLE-BGP-MIB", "sleBGPBaseControlRfc1771Strict"),
        ("SLE-BGP-MIB", "sleBGPBaseControlAggregateNextHop"),
        ("SLE-BGP-MIB", "sleBGPBaseControlExtendAsnCap"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyMode"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearFamilyType"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearDirection"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearSoft"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPrefixFilter"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearPeerName"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearIPv4Addr"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearIPv6Addr"),
        ("SLE-BGP-MIB", "sleBGPBaseControlClearViewName"),
        ("SLE-BGP-MIB", "sleBGPInfoRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoLogNeighborChange"),
        ("SLE-BGP-MIB", "sleBGPInfoAlwaysCompareMed"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathAsPathIgnore"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareConfedAsPath"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedConfed"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedMisAsWorst"),
        ("SLE-BGP-MIB", "sleBGPInfoClientToClient"),
        ("SLE-BGP-MIB", "sleBGPInfoClusterID"),
        ("SLE-BGP-MIB", "sleBGPInfoConfederationID"),
        ("SLE-BGP-MIB", "sleBGPInfoDeterministicMed"),
        ("SLE-BGP-MIB", "sleBGPInfoEnforceFirstAs"),
        ("SLE-BGP-MIB", "sleBGPInfoFastExternalFailOver"),
        ("SLE-BGP-MIB", "sleBGPInfoGracefulRestartTime"),
        ("SLE-BGP-MIB", "sleBGPInfoGracefulStalepathTime"),
        ("SLE-BGP-MIB", "sleBGPInfoScanTime"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerStatus"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoSnmpNotification"),
        ("SLE-BGP-MIB", "sleBGPInfoUpdateDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoExternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoInternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoLocalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPath"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPathIBGP"),
        ("SLE-BGP-MIB", "sleBGPInfoKeepAliveInterval"),
        ("SLE-BGP-MIB", "sleBGPInfoHoldTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlRequest"),
        ("SLE-BGP-MIB", "sleBGPInfoControlStatus"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimer"),
        ("SLE-BGP-MIB", "sleBGPInfoControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPInfoControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPInfoControlRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlLogNeighborChange"),
        ("SLE-BGP-MIB", "sleBGPInfoControlAlwaysCompareMed"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathAsPathIgnore"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareConfedAsPath"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareRouterID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareMedConfed"),
        ("SLE-BGP-MIB", "sleBGPInfoControlBestPathCompareMedMisAsWorst"),
        ("SLE-BGP-MIB", "sleBGPInfoControlClientToClient"),
        ("SLE-BGP-MIB", "sleBGPInfoControlClusterID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlConfederationID"),
        ("SLE-BGP-MIB", "sleBGPInfoControlDeterministicMed"),
        ("SLE-BGP-MIB", "sleBGPInfoControlEnforceFirstAs"),
        ("SLE-BGP-MIB", "sleBGPInfoControlFastExternalFailOver"),
        ("SLE-BGP-MIB", "sleBGPInfoControlGracefulRestartTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlGracefulStalepathTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlScanTime"),
        ("SLE-BGP-MIB", "sleBGPInfoControlNexthopTriggerStatus"),
        ("SLE-BGP-MIB", "sleBGPInfoControlNexthopTriggerDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoControlSnmpNotification"),
        ("SLE-BGP-MIB", "sleBGPInfoControlUpdateDelay"),
        ("SLE-BGP-MIB", "sleBGPInfoControlExternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlInternalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlLocalRouteDistance"),
        ("SLE-BGP-MIB", "sleBGPInfoControlMaximumPath"),
        ("SLE-BGP-MIB", "sleBGPInfoControlMaximumPathIBGP"),
        ("SLE-BGP-MIB", "sleBGPInfoControlKeepAliveInterval"),
        ("SLE-BGP-MIB", "sleBGPInfoControlHoldTime"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceValue"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceAccName"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlValue"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceControlAccName"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupName"),
        ("SLE-BGP-MIB", "sleBGPPeerAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerPort"),
        ("SLE-BGP-MIB", "sleBGPPeerRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerIfname"),
        ("SLE-BGP-MIB", "sleBGPPeerCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerPassword"),
        ("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlStatus"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimer"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"),
        ("SLE-BGP-MIB", "sleBGPPeerControlAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerControlGroupName"),
        ("SLE-BGP-MIB", "sleBGPPeerControlAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerControlDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerControlWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerControlEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerControlPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerControlUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerControlPort"),
        ("SLE-BGP-MIB", "sleBGPPeerControlRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerControlShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerControlKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerControlOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerControlStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerControlIfname"),
        ("SLE-BGP-MIB", "sleBGPPeerControlCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerControlCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerControlEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerControlPassword"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPort"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPassword"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStatus"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimer"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlAsNum"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlAdvInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlAsOriInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlDesc"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlDontCapNego"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlWeight"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlEnforcMultiHop"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlPassive"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlUpSourceName"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlPort"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlRetstartTime"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlShutDown"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlHoldInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlConnInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlOverCap"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStrictCapMatch"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlCapRouteRefresh"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlCapDynamic"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlEBGPMulthopCount"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlPassword"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseNetworkCheck"),
        ("SLE-BGP-MIB", "sleBGPAFBaseSync"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDefOrg"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampReuse"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampMaxSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampUnReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlNetworkCheck"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlSync"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDefOrg"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampReuse"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampMaxSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlDampUnReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFRedistMode"),
        ("SLE-BGP-MIB", "sleBGPAFRedistType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistProtoType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlProtoType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlRoutemapName"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrMode"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrIPType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrIPPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrIPMask"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrAsSet"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrSummOnly"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlIPType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlIPPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlIPMask"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlAsSet"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlSummOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlActviate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAllowAsInNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlAttrUnchangedNexthop"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlCapGracefulRestart"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlCapOrfMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlDefOriginateRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlFLInAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlFLOutAccName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlMaxPrefixWarnOnly"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRemotePrivateAs"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlInRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlOutRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRouteReflectClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlRouteServerClient"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlInDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlOutDistListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlInPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlOutPrefixListName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlSendCommunity"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlNexthopSelf"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlSoftReconfig"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupControlUnsuppressMapName"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkMode"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkAddrType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkAddr"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkAddrMask"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkBackdoor"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkRoutemap"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlStatus"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlTimer"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlAddrType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlAddr"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlAddrMask"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlBackdoor"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAdminDistanceDeleted.setStatus(
        "current"
    )

sleBGPPeerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 1)
)
sleBGPPeerCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerAsNum"))
)
if mibBuilder.loadTexts:
    sleBGPPeerCreated.setStatus(
        "current"
    )

sleBGPPeerDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 2)
)
sleBGPPeerDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerDeleted.setStatus(
        "current"
    )

sleBGPPeerGroupNameCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 3)
)
sleBGPPeerGroupNameCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupNameCreated.setStatus(
        "current"
    )

sleBGPPeerGroupNameDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 4)
)
sleBGPPeerGroupNameDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupNameDeleted.setStatus(
        "current"
    )

sleBGPPeerAdvIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 5)
)
sleBGPPeerAdvIntervalChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerAdvInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerAdvIntervalChanged.setStatus(
        "current"
    )

sleBGPPeerAsOriIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 6)
)
sleBGPPeerAsOriIntervalChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerAsOriInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerAsOriIntervalChanged.setStatus(
        "current"
    )

sleBGPPeerDescCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 7)
)
sleBGPPeerDescCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerDesc"))
)
if mibBuilder.loadTexts:
    sleBGPPeerDescCreated.setStatus(
        "current"
    )

sleBGPPeerDescDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 8)
)
sleBGPPeerDescDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"),
        ("SLE-BGP-MIB", "sleBGPPeerControlDesc"))
)
if mibBuilder.loadTexts:
    sleBGPPeerDescDeleted.setStatus(
        "current"
    )

sleBGPPeerDontCapNegoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 9)
)
sleBGPPeerDontCapNegoChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerDontCapNego"))
)
if mibBuilder.loadTexts:
    sleBGPPeerDontCapNegoChanged.setStatus(
        "current"
    )

sleBGPPeerWeightChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 10)
)
sleBGPPeerWeightChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerDontCapNego"))
)
if mibBuilder.loadTexts:
    sleBGPPeerWeightChanged.setStatus(
        "current"
    )

sleBGPPeerEnforcMultiHopChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 11)
)
sleBGPPeerEnforcMultiHopChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerEnforcMultiHop"))
)
if mibBuilder.loadTexts:
    sleBGPPeerEnforcMultiHopChanged.setStatus(
        "current"
    )

sleBGPPeerPassiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 12)
)
sleBGPPeerPassiveChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerPassive"))
)
if mibBuilder.loadTexts:
    sleBGPPeerPassiveChanged.setStatus(
        "current"
    )

sleBGPPeerUpSourceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 13)
)
sleBGPPeerUpSourceCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerUpSourceName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerUpSourceCreated.setStatus(
        "current"
    )

sleBGPPeerUpSourceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 14)
)
sleBGPPeerUpSourceDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerUpSourceDeleted.setStatus(
        "current"
    )

sleBGPPeerPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 15)
)
sleBGPPeerPortChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerPort"))
)
if mibBuilder.loadTexts:
    sleBGPPeerPortChanged.setStatus(
        "current"
    )

sleBGPPeerRetstartTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 16)
)
sleBGPPeerRetstartTimeChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerRetstartTime"))
)
if mibBuilder.loadTexts:
    sleBGPPeerRetstartTimeChanged.setStatus(
        "current"
    )

sleBGPPeerShutDownChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 17)
)
sleBGPPeerShutDownChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerShutDown"))
)
if mibBuilder.loadTexts:
    sleBGPPeerShutDownChanged.setStatus(
        "current"
    )

sleBGPPeerTimersProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 18)
)
sleBGPPeerTimersProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerHoldInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerTimersProfileChanged.setStatus(
        "current"
    )

sleBGPPeerConnIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 19)
)
sleBGPPeerConnIntervalChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerConnInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerConnIntervalChanged.setStatus(
        "current"
    )

sleBGPPeerOverCapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 20)
)
sleBGPPeerOverCapChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerOverCap"))
)
if mibBuilder.loadTexts:
    sleBGPPeerOverCapChanged.setStatus(
        "current"
    )

sleBGPPeerStrictCapMatchChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 21)
)
sleBGPPeerStrictCapMatchChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerStrictCapMatch"))
)
if mibBuilder.loadTexts:
    sleBGPPeerStrictCapMatchChanged.setStatus(
        "current"
    )

sleBGPPeerIfnameCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 22)
)
sleBGPPeerIfnameCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerIfname"))
)
if mibBuilder.loadTexts:
    sleBGPPeerIfnameCreated.setStatus(
        "current"
    )

sleBGPPeerIfnameDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 23)
)
sleBGPPeerIfnameDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerIfnameDeleted.setStatus(
        "current"
    )

sleBGPPeerCapRouteRefreshChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 24)
)
sleBGPPeerCapRouteRefreshChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerCapRouteRefresh"))
)
if mibBuilder.loadTexts:
    sleBGPPeerCapRouteRefreshChanged.setStatus(
        "current"
    )

sleBGPPeerCapDynamicChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 25)
)
sleBGPPeerCapDynamicChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerCapDynamic"))
)
if mibBuilder.loadTexts:
    sleBGPPeerCapDynamicChanged.setStatus(
        "current"
    )

sleBGPPeerEBGPMultihopCountChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 26)
)
sleBGPPeerEBGPMultihopCountChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerEBGPMulthopCount"))
)
if mibBuilder.loadTexts:
    sleBGPPeerEBGPMultihopCountChanged.setStatus(
        "current"
    )

sleBGPPeerPasswordCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 27)
)
sleBGPPeerPasswordCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerName"),
        ("SLE-BGP-MIB", "sleBGPPeerPassword"))
)
if mibBuilder.loadTexts:
    sleBGPPeerPasswordCreated.setStatus(
        "current"
    )

sleBGPPeerPasswordDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 1, 3, 28)
)
sleBGPPeerPasswordDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerControlName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerPasswordDeleted.setStatus(
        "current"
    )

sleBGPPeerGroupCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 1)
)
sleBGPPeerGroupCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupCreated.setStatus(
        "current"
    )

sleBGPPeerGroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 2)
)
sleBGPPeerGroupDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStr"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupDeleted.setStatus(
        "current"
    )

sleBGPPeerGroupRemoteAsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 3)
)
sleBGPPeerGroupRemoteAsChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAsNum"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupRemoteAsChanged.setStatus(
        "current"
    )

sleBGPPeerGroupAdvIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 4)
)
sleBGPPeerGroupAdvIntervalChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAdvInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupAdvIntervalChanged.setStatus(
        "current"
    )

sleBGPPeerGroupAsOriIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 5)
)
sleBGPPeerGroupAsOriIntervalChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAsOriInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupAsOriIntervalChanged.setStatus(
        "current"
    )

sleBGPPeerGroupDescCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 6)
)
sleBGPPeerGroupDescCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDesc"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupDescCreated.setStatus(
        "current"
    )

sleBGPPeerGroupDescDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 7)
)
sleBGPPeerGroupDescDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlDesc"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupDescDeleted.setStatus(
        "current"
    )

sleBGPPeerGroupDontCapNegoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 8)
)
sleBGPPeerGroupDontCapNegoChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDontCapNego"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupDontCapNegoChanged.setStatus(
        "current"
    )

sleBGPPeerGroupWeightChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 9)
)
sleBGPPeerGroupWeightChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerWeight"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupWeightChanged.setStatus(
        "current"
    )

sleBGPPeerGroupPassiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 10)
)
sleBGPPeerGroupPassiveChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPassive"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupPassiveChanged.setStatus(
        "current"
    )

sleBGPPeerGroupUpSourceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 11)
)
sleBGPPeerGroupUpSourceCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupUpSourceName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupUpSourceCreated.setStatus(
        "current"
    )

sleBGPPeerGroupUpSourceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 12)
)
sleBGPPeerGroupUpSourceDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlUpSourceName"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupUpSourceDeleted.setStatus(
        "current"
    )

sleBGPPeerGroupPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 13)
)
sleBGPPeerGroupPortChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPort"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupPortChanged.setStatus(
        "current"
    )

sleBGPPeerGroupRetstartTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 14)
)
sleBGPPeerGroupRetstartTimeChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupRetstartTime"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupRetstartTimeChanged.setStatus(
        "current"
    )

sleBGPPeerGroupShutDownChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 15)
)
sleBGPPeerGroupShutDownChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerShutDown"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupShutDownChanged.setStatus(
        "current"
    )

sleBGPPeerGroupTimersProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 16)
)
sleBGPPeerGroupTimersProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupKeepInterval"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupHoldInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupTimersProfileChanged.setStatus(
        "current"
    )

sleBGPPeerGroupConnIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 17)
)
sleBGPPeerGroupConnIntervalChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupConnInterval"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupConnIntervalChanged.setStatus(
        "current"
    )

sleBGPPeerGroupOverCapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 18)
)
sleBGPPeerGroupOverCapChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupOverCap"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupOverCapChanged.setStatus(
        "current"
    )

sleBGPPeerGroupStrictCapMatchChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 19)
)
sleBGPPeerGroupStrictCapMatchChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStrictCapMatch"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupStrictCapMatchChanged.setStatus(
        "current"
    )

sleBGPPeerGroupCapRouteRefreshChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 20)
)
sleBGPPeerGroupCapRouteRefreshChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapRouteRefresh"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupCapRouteRefreshChanged.setStatus(
        "current"
    )

sleBGPPeerGroupCapDynamicChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 21)
)
sleBGPPeerGroupCapDynamicChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapDynamic"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupCapDynamicChanged.setStatus(
        "current"
    )

sleBGPPeerGroupEBGPMultihopCountChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 22)
)
sleBGPPeerGroupEBGPMultihopCountChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupEBGPMulthopCount"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupEBGPMultihopCountChanged.setStatus(
        "current"
    )

sleBGPPeerGroupPasswordCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 23)
)
sleBGPPeerGroupPasswordCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStr"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPassword"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupPasswordCreated.setStatus(
        "current"
    )

sleBGPPeerGroupPasswordDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 4, 2, 3, 24)
)
sleBGPPeerGroupPasswordDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPPeerGroupControlRequest"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupControlStr"),
        ("SLE-BGP-MIB", "sleBGPPeerControlPassword"))
)
if mibBuilder.loadTexts:
    sleBGPPeerGroupPasswordDeleted.setStatus(
        "current"
    )

sleBGPAFBaseNetworkCheckChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 3, 1)
)
sleBGPAFBaseNetworkCheckChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseNetworkCheck"))
)
if mibBuilder.loadTexts:
    sleBGPAFBaseNetworkCheckChanged.setStatus(
        "current"
    )

sleBGPAFBaseSyncChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 3, 2)
)
sleBGPAFBaseSyncChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseSync"))
)
if mibBuilder.loadTexts:
    sleBGPAFBaseSyncChanged.setStatus(
        "current"
    )

sleBGPAFBaseDefOrgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 3, 3)
)
sleBGPAFBaseDefOrgChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDefOrg"))
)
if mibBuilder.loadTexts:
    sleBGPAFBaseDefOrgChanged.setStatus(
        "current"
    )

sleBGPAFBaseDampRoutemapNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 3, 4)
)
sleBGPAFBaseDampRoutemapNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampRoutemapName"))
)
if mibBuilder.loadTexts:
    sleBGPAFBaseDampRoutemapNameChanged.setStatus(
        "current"
    )

sleBGPAFBaseDampTimeProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 3, 5)
)
sleBGPAFBaseDampTimeProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampReachHlife"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampReuse"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampMaxSuppress"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampUnReachHlife"))
)
if mibBuilder.loadTexts:
    sleBGPAFBaseDampTimeProfileChanged.setStatus(
        "current"
    )

sleBGPAFBaseDampDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 1, 3, 6)
)
sleBGPAFBaseDampDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFBaseControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFBaseControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFBaseMode"),
        ("SLE-BGP-MIB", "sleBGPAFBaseType"))
)
if mibBuilder.loadTexts:
    sleBGPAFBaseDampDeleted.setStatus(
        "current"
    )

sleBGPAFRedistributeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 3, 1)
)
sleBGPAFRedistributeCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFRedistControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFRedistMode"),
        ("SLE-BGP-MIB", "sleBGPAFRedistType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistProtoType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistRoutemapName"))
)
if mibBuilder.loadTexts:
    sleBGPAFRedistributeCreated.setStatus(
        "current"
    )

sleBGPAFRedistributeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 3, 2)
)
sleBGPAFRedistributeDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFRedistControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFRedistMode"),
        ("SLE-BGP-MIB", "sleBGPAFRedistType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlProtoType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlRoutemapName"))
)
if mibBuilder.loadTexts:
    sleBGPAFRedistributeDeleted.setStatus(
        "current"
    )

sleBGPAFRedistributeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 2, 3, 3)
)
sleBGPAFRedistributeChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFRedistControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFRedistControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFRedistMode"),
        ("SLE-BGP-MIB", "sleBGPAFRedistType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistProtoType"),
        ("SLE-BGP-MIB", "sleBGPAFRedistRoutemapName"))
)
if mibBuilder.loadTexts:
    sleBGPAFRedistributeChanged.setStatus(
        "current"
    )

sleBGPAFAggreAddressCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 3, 1)
)
sleBGPAFAggreAddressCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFAggreAddrControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrMode"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrAsSet"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrSummOnly"))
)
if mibBuilder.loadTexts:
    sleBGPAFAggreAddressCreated.setStatus(
        "current"
    )

sleBGPAFAggreAddressDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 3, 3, 2)
)
sleBGPAFAggreAddressDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFAggreAddrControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlType"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlAsSet"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddrControlSummOnly"))
)
if mibBuilder.loadTexts:
    sleBGPAFAggreAddressDeleted.setStatus(
        "current"
    )

sleBGPAFPeerActviateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 1)
)
sleBGPAFPeerActviateChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerActviate"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerActviateChanged.setStatus(
        "current"
    )

sleBGPAFPeerAllowAsInChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 2)
)
sleBGPAFPeerAllowAsInChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsInNum"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerAllowAsInChanged.setStatus(
        "current"
    )

sleBGPAFPeerAttrUnchangedProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 3)
)
sleBGPAFPeerAttrUnchangedProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedNexthop"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerAttrUnchangedProfileChanged.setStatus(
        "current"
    )

sleBGPAFPeerCapGracefulRestartChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 4)
)
sleBGPAFPeerCapGracefulRestartChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapGracefulRestart"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerCapGracefulRestartChanged.setStatus(
        "current"
    )

sleBGPAFPeerCapOrfModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 5)
)
sleBGPAFPeerCapOrfModeChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapOrfMode"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerCapOrfModeChanged.setStatus(
        "current"
    )

sleBGPAFPeerDefOriginateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 6)
)
sleBGPAFPeerDefOriginateChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerDefOriginateRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerDefOriginateChanged.setStatus(
        "current"
    )

sleBGPAFPeerFLInAccNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 7)
)
sleBGPAFPeerFLInAccNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLInAccName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerFLInAccNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerFLOutAccNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 8)
)
sleBGPAFPeerFLOutAccNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLOutAccName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerFLOutAccNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerMaxPrefixProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 9)
)
sleBGPAFPeerMaxPrefixProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixWarnOnly"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerMaxPrefixProfileChanged.setStatus(
        "current"
    )

sleBGPAFPeerRemotePrivateAsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 10)
)
sleBGPAFPeerRemotePrivateAsChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRemotePrivateAs"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerRemotePrivateAsChanged.setStatus(
        "current"
    )

sleBGPAFPeerInRoutemapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 11)
)
sleBGPAFPeerInRoutemapChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerInRoutemapChanged.setStatus(
        "current"
    )

sleBGPAFPeerOutRoutemapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 12)
)
sleBGPAFPeerOutRoutemapChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerOutRoutemapChanged.setStatus(
        "current"
    )

sleBGPAFPeerRouteReflectClientChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 13)
)
sleBGPAFPeerRouteReflectClientChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteReflectClient"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerRouteReflectClientChanged.setStatus(
        "current"
    )

sleBGPAFPeerRouteServerClientChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 14)
)
sleBGPAFPeerRouteServerClientChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteServerClient"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerRouteServerClientChanged.setStatus(
        "current"
    )

sleBGPAFPeerInDistListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 15)
)
sleBGPAFPeerInDistListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInDistListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerInDistListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerOutDistListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 16)
)
sleBGPAFPeerOutDistListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutDistListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerOutDistListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerInPrefixListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 17)
)
sleBGPAFPeerInPrefixListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInPrefixListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerInPrefixListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerOutPrefixListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 18)
)
sleBGPAFPeerOutPrefixListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutPrefixListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerOutPrefixListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerSendCommunityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 19)
)
sleBGPAFPeerSendCommunityChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSendCommunity"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerSendCommunityChanged.setStatus(
        "current"
    )

sleBGPAFPeerNexthopSelfChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 20)
)
sleBGPAFPeerNexthopSelfChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerNexthopSelf"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerNexthopSelfChanged.setStatus(
        "current"
    )

sleBGPAFPeerSoftReconfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 21)
)
sleBGPAFPeerSoftReconfigChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSoftReconfig"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerSoftReconfigChanged.setStatus(
        "current"
    )

sleBGPAFPeerUnsuppressMapNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 1, 3, 22)
)
sleBGPAFPeerUnsuppressMapNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerUnsuppressMapName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerUnsuppressMapNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupActviateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 1)
)
sleBGPAFPeerGroupActviateChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerActviate"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupActviateChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupAllowAsInChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 2)
)
sleBGPAFPeerGroupAllowAsInChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsIn"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsInNum"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupAllowAsInChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupAttrUnchangedProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 3)
)
sleBGPAFPeerGroupAttrUnchangedProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedAsPath"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedMed"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedNexthop"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupAttrUnchangedProfileChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupCapGracefulRestartChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 4)
)
sleBGPAFPeerGroupCapGracefulRestartChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapGracefulRestart"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupCapGracefulRestartChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupCapOrfModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 5)
)
sleBGPAFPeerGroupCapOrfModeChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapOrfMode"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupCapOrfModeChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupDefOriginateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 6)
)
sleBGPAFPeerGroupDefOriginateChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupDefOriginate"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupDefOriginateRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupDefOriginateChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupFLInAccNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 7)
)
sleBGPAFPeerGroupFLInAccNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLInAccName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupFLInAccNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupFLOutAccNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 8)
)
sleBGPAFPeerGroupFLOutAccNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLOutAccName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupFLOutAccNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupMaxPrefixProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 9)
)
sleBGPAFPeerGroupMaxPrefixProfileChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixNum"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixThreshold"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixWarnOnly"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupMaxPrefixProfileChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupRemotePrivateAsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 10)
)
sleBGPAFPeerGroupRemotePrivateAsChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRemotePrivateAs"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupRemotePrivateAsChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupInRoutemapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 11)
)
sleBGPAFPeerGroupInRoutemapChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupInRoutemapChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupOutRoutemapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 12)
)
sleBGPAFPeerGroupOutRoutemapChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupOutRoutemapChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupRouteReflectClientChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 13)
)
sleBGPAFPeerGroupRouteReflectClientChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteReflectClient"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupRouteReflectClientChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupRouteServerClientChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 14)
)
sleBGPAFPeerGroupRouteServerClientChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteServerClient"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupRouteServerClientChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupInDistListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 15)
)
sleBGPAFPeerGroupInDistListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInDistListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupInDistListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupOutDistListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 16)
)
sleBGPAFPeerGroupOutDistListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutDistListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupOutDistListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupInPrefixListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 17)
)
sleBGPAFPeerGroupInPrefixListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInPrefixListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupInPrefixListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupOutPrefixListNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 18)
)
sleBGPAFPeerGroupOutPrefixListNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutPrefixListName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupOutPrefixListNameChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupSendCommunityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 19)
)
sleBGPAFPeerGroupSendCommunityChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSendCommunity"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupSendCommunityChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupNexthopSelfChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 20)
)
sleBGPAFPeerGroupNexthopSelfChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerNexthopSelf"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupNexthopSelfChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupSoftReconfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 21)
)
sleBGPAFPeerGroupSoftReconfigChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSoftReconfig"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupSoftReconfigChanged.setStatus(
        "current"
    )

sleBGPAFPeerGroupUnsuppressMapNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 4, 2, 3, 22)
)
sleBGPAFPeerGroupUnsuppressMapNameChanged.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFPeerControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFPeerControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMode"),
        ("SLE-BGP-MIB", "sleBGPAFPeerType"),
        ("SLE-BGP-MIB", "sleBGPAFPeerName"),
        ("SLE-BGP-MIB", "sleBGPAFPeerUnsuppressMapName"))
)
if mibBuilder.loadTexts:
    sleBGPAFPeerGroupUnsuppressMapNameChanged.setStatus(
        "current"
    )

sleBGPAFNetworkCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 3, 1)
)
sleBGPAFNetworkCreated.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFNetworkControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkMode"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkBackdoor"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFNetworkCreated.setStatus(
        "current"
    )

sleBGPAFNetworkDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 5, 5, 3, 2)
)
sleBGPAFNetworkDeleted.setObjects(
      *(("SLE-BGP-MIB", "sleBGPAFNetworkControlRequest"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlTimeStamp"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlReqResult"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlMode"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlType"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlAddrPrefix"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlBackdoor"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkControlRoutemap"))
)
if mibBuilder.loadTexts:
    sleBGPAFNetworkDeleted.setStatus(
        "current"
    )


# Notifications groups

sleBGPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 53, 8)
)
sleBGPNotificationGroup.setObjects(
      *(("SLE-BGP-MIB", "sleBGPBaseAsModeCreated"),
        ("SLE-BGP-MIB", "sleBGPBaseAsModeDeleted"),
        ("SLE-BGP-MIB", "sleBGPBaseConfigTypeChanged"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771PathSelectChanged"),
        ("SLE-BGP-MIB", "sleBGPBaseRfc1771StrictChanged"),
        ("SLE-BGP-MIB", "sleBGPBaseAggregateNextHopChanged"),
        ("SLE-BGP-MIB", "sleBGPBaseExtendAsnCapChanged"),
        ("SLE-BGP-MIB", "sleBGPBaseAllCleared"),
        ("SLE-BGP-MIB", "sleBGPBaseAsNumberCleared"),
        ("SLE-BGP-MIB", "sleBGPBasePeerCleared"),
        ("SLE-BGP-MIB", "sleBGPBaseDampCleared"),
        ("SLE-BGP-MIB", "sleBGPBaseExternalCleared"),
        ("SLE-BGP-MIB", "sleBGPBaseViewCleared"),
        ("SLE-BGP-MIB", "sleBGPInfoRouterIDCreated"),
        ("SLE-BGP-MIB", "sleBGPInfoRouterIDDeleted"),
        ("SLE-BGP-MIB", "sleBGPInfoLogNeighborChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoAlwaysCompareMedChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathAsPathIgnoreChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareConfedAsPathChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareRouterIDChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedConfedChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoBestPathCompareMedMisAsWorstChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoClientToClientChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoClusterIDCreated"),
        ("SLE-BGP-MIB", "sleBGPInfoClusterIDDeleted"),
        ("SLE-BGP-MIB", "sleBGPInfoConfederationIDChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoDeterministicMedChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoEnforceFirstAsChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoFastExternalFailOverChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoGracefulRestartProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoScanTimeChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerStatusChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoNexthopTriggerDelayChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoSnmpNotificationChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoUpdateDelayChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoDistanceCreated"),
        ("SLE-BGP-MIB", "sleBGPInfoDistanceDeleted"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPathChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoMaximumPathIBGPChanged"),
        ("SLE-BGP-MIB", "sleBGPInfoTimersChanged"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceCreated"),
        ("SLE-BGP-MIB", "sleBGPAdminDistanceDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupNameCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupNameDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerAdvIntervalChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerAsOriIntervalChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerDescCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerDescDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerDontCapNegoChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerWeightChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerEnforcMultiHopChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerPassiveChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerUpSourceCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerUpSourceDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerPortChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerRetstartTimeChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerShutDownChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerTimersProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerConnIntervalChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerOverCapChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerStrictCapMatchChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerIfnameCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerIfnameDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerCapRouteRefreshChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerCapDynamicChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerEBGPMultihopCountChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerPasswordCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerPasswordDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupRemoteAsChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAdvIntervalChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupAsOriIntervalChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDescCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDescDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupDontCapNegoChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupWeightChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPassiveChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupUpSourceCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupUpSourceDeleted"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPortChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupRetstartTimeChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupShutDownChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupTimersProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupConnIntervalChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupOverCapChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupStrictCapMatchChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapRouteRefreshChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupCapDynamicChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupEBGPMultihopCountChanged"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPasswordCreated"),
        ("SLE-BGP-MIB", "sleBGPPeerGroupPasswordDeleted"),
        ("SLE-BGP-MIB", "sleBGPAFBaseNetworkCheckChanged"),
        ("SLE-BGP-MIB", "sleBGPAFBaseSyncChanged"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDefOrgChanged"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampRoutemapNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampTimeProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPAFBaseDampDeleted"),
        ("SLE-BGP-MIB", "sleBGPAFRedistributeCreated"),
        ("SLE-BGP-MIB", "sleBGPAFRedistributeDeleted"),
        ("SLE-BGP-MIB", "sleBGPAFRedistributeChanged"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddressCreated"),
        ("SLE-BGP-MIB", "sleBGPAFAggreAddressDeleted"),
        ("SLE-BGP-MIB", "sleBGPAFPeerActviateChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAllowAsInChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerAttrUnchangedProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapGracefulRestartChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerCapOrfModeChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerDefOriginateChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLInAccNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerFLOutAccNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerMaxPrefixProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRemotePrivateAsChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInRoutemapChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutRoutemapChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteReflectClientChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerRouteServerClientChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInDistListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutDistListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerInPrefixListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerOutPrefixListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSendCommunityChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerNexthopSelfChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerSoftReconfigChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerUnsuppressMapNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupActviateChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAllowAsInChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupAttrUnchangedProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupCapGracefulRestartChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupCapOrfModeChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupDefOriginateChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupFLInAccNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupFLOutAccNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupMaxPrefixProfileChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRemotePrivateAsChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInRoutemapChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutRoutemapChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRouteReflectClientChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupRouteServerClientChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInDistListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutDistListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupInPrefixListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupOutPrefixListNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupSendCommunityChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupNexthopSelfChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupSoftReconfigChanged"),
        ("SLE-BGP-MIB", "sleBGPAFPeerGroupUnsuppressMapNameChanged"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkCreated"),
        ("SLE-BGP-MIB", "sleBGPAFNetworkDeleted"))
)
if mibBuilder.loadTexts:
    sleBGPNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-BGP-MIB",
    **{"sleBGP": sleBGP,
       "sleBGPBase": sleBGPBase,
       "sleBGPBaseInfo": sleBGPBaseInfo,
       "sleBGPBaseAsNumber": sleBGPBaseAsNumber,
       "sleBGPBaseConfigType": sleBGPBaseConfigType,
       "sleBGPBaseRfc1771PathSelect": sleBGPBaseRfc1771PathSelect,
       "sleBGPBaseRfc1771Strict": sleBGPBaseRfc1771Strict,
       "sleBGPBaseAggregateNextHop": sleBGPBaseAggregateNextHop,
       "sleBGPBaseExtendAsnCap": sleBGPBaseExtendAsnCap,
       "sleBGPBaseControl": sleBGPBaseControl,
       "sleBGPBaseControlRequest": sleBGPBaseControlRequest,
       "sleBGPBaseControlStatus": sleBGPBaseControlStatus,
       "sleBGPBaseControlTimer": sleBGPBaseControlTimer,
       "sleBGPBaseControlTimeStamp": sleBGPBaseControlTimeStamp,
       "sleBGPBaseControlReqResult": sleBGPBaseControlReqResult,
       "sleBGPBaseControlAsNumber": sleBGPBaseControlAsNumber,
       "sleBGPBaseControlConfigType": sleBGPBaseControlConfigType,
       "sleBGPBaseControlRfc1771PathSelect": sleBGPBaseControlRfc1771PathSelect,
       "sleBGPBaseControlRfc1771Strict": sleBGPBaseControlRfc1771Strict,
       "sleBGPBaseControlAggregateNextHop": sleBGPBaseControlAggregateNextHop,
       "sleBGPBaseControlExtendAsnCap": sleBGPBaseControlExtendAsnCap,
       "sleBGPBaseControlClearFamilyMode": sleBGPBaseControlClearFamilyMode,
       "sleBGPBaseControlClearFamilyType": sleBGPBaseControlClearFamilyType,
       "sleBGPBaseControlClearDirection": sleBGPBaseControlClearDirection,
       "sleBGPBaseControlClearSoft": sleBGPBaseControlClearSoft,
       "sleBGPBaseControlClearPrefixFilter": sleBGPBaseControlClearPrefixFilter,
       "sleBGPBaseControlClearPeerName": sleBGPBaseControlClearPeerName,
       "sleBGPBaseControlClearAddr": sleBGPBaseControlClearAddr,
       "sleBGPBaseControlClearViewName": sleBGPBaseControlClearViewName,
       "sleBGPBaseControlClearDampFlag": sleBGPBaseControlClearDampFlag,
       "sleBGPBaseNotification": sleBGPBaseNotification,
       "sleBGPBaseAsModeCreated": sleBGPBaseAsModeCreated,
       "sleBGPBaseAsModeDeleted": sleBGPBaseAsModeDeleted,
       "sleBGPBaseConfigTypeChanged": sleBGPBaseConfigTypeChanged,
       "sleBGPBaseRfc1771PathSelectChanged": sleBGPBaseRfc1771PathSelectChanged,
       "sleBGPBaseRfc1771StrictChanged": sleBGPBaseRfc1771StrictChanged,
       "sleBGPBaseAggregateNextHopChanged": sleBGPBaseAggregateNextHopChanged,
       "sleBGPBaseExtendAsnCapChanged": sleBGPBaseExtendAsnCapChanged,
       "sleBGPBaseAllCleared": sleBGPBaseAllCleared,
       "sleBGPBaseAsNumberCleared": sleBGPBaseAsNumberCleared,
       "sleBGPBasePeerCleared": sleBGPBasePeerCleared,
       "sleBGPBaseDampCleared": sleBGPBaseDampCleared,
       "sleBGPBaseExternalCleared": sleBGPBaseExternalCleared,
       "sleBGPBaseViewCleared": sleBGPBaseViewCleared,
       "sleBGPInfo": sleBGPInfo,
       "sleBGPInfoValue": sleBGPInfoValue,
       "sleBGPInfoRouterID": sleBGPInfoRouterID,
       "sleBGPInfoLogNeighborChange": sleBGPInfoLogNeighborChange,
       "sleBGPInfoAlwaysCompareMed": sleBGPInfoAlwaysCompareMed,
       "sleBGPInfoBestPathAsPathIgnore": sleBGPInfoBestPathAsPathIgnore,
       "sleBGPInfoBestPathCompareConfedAsPath": sleBGPInfoBestPathCompareConfedAsPath,
       "sleBGPInfoBestPathCompareRouterID": sleBGPInfoBestPathCompareRouterID,
       "sleBGPInfoBestPathCompareMedConfed": sleBGPInfoBestPathCompareMedConfed,
       "sleBGPInfoBestPathCompareMedMisAsWorst": sleBGPInfoBestPathCompareMedMisAsWorst,
       "sleBGPInfoClientToClient": sleBGPInfoClientToClient,
       "sleBGPInfoClusterID": sleBGPInfoClusterID,
       "sleBGPInfoConfederationID": sleBGPInfoConfederationID,
       "sleBGPInfoDeterministicMed": sleBGPInfoDeterministicMed,
       "sleBGPInfoEnforceFirstAs": sleBGPInfoEnforceFirstAs,
       "sleBGPInfoFastExternalFailOver": sleBGPInfoFastExternalFailOver,
       "sleBGPInfoGracefulRestartTime": sleBGPInfoGracefulRestartTime,
       "sleBGPInfoGracefulStalepathTime": sleBGPInfoGracefulStalepathTime,
       "sleBGPInfoScanTime": sleBGPInfoScanTime,
       "sleBGPInfoNexthopTriggerStatus": sleBGPInfoNexthopTriggerStatus,
       "sleBGPInfoNexthopTriggerDelay": sleBGPInfoNexthopTriggerDelay,
       "sleBGPInfoSnmpNotification": sleBGPInfoSnmpNotification,
       "sleBGPInfoUpdateDelay": sleBGPInfoUpdateDelay,
       "sleBGPInfoExternalRouteDistance": sleBGPInfoExternalRouteDistance,
       "sleBGPInfoInternalRouteDistance": sleBGPInfoInternalRouteDistance,
       "sleBGPInfoLocalRouteDistance": sleBGPInfoLocalRouteDistance,
       "sleBGPInfoMaximumPath": sleBGPInfoMaximumPath,
       "sleBGPInfoMaximumPathIBGP": sleBGPInfoMaximumPathIBGP,
       "sleBGPInfoKeepAliveInterval": sleBGPInfoKeepAliveInterval,
       "sleBGPInfoHoldTime": sleBGPInfoHoldTime,
       "sleBGPInfoControl": sleBGPInfoControl,
       "sleBGPInfoControlRequest": sleBGPInfoControlRequest,
       "sleBGPInfoControlStatus": sleBGPInfoControlStatus,
       "sleBGPInfoControlTimer": sleBGPInfoControlTimer,
       "sleBGPInfoControlTimeStamp": sleBGPInfoControlTimeStamp,
       "sleBGPInfoControlReqResult": sleBGPInfoControlReqResult,
       "sleBGPInfoControlRouterID": sleBGPInfoControlRouterID,
       "sleBGPInfoControlLogNeighborChange": sleBGPInfoControlLogNeighborChange,
       "sleBGPInfoControlAlwaysCompareMed": sleBGPInfoControlAlwaysCompareMed,
       "sleBGPInfoControlBestPathAsPathIgnore": sleBGPInfoControlBestPathAsPathIgnore,
       "sleBGPInfoControlBestPathCompareConfedAsPath": sleBGPInfoControlBestPathCompareConfedAsPath,
       "sleBGPInfoControlBestPathCompareRouterID": sleBGPInfoControlBestPathCompareRouterID,
       "sleBGPInfoControlBestPathCompareMedConfed": sleBGPInfoControlBestPathCompareMedConfed,
       "sleBGPInfoControlBestPathCompareMedMisAsWorst": sleBGPInfoControlBestPathCompareMedMisAsWorst,
       "sleBGPInfoControlClientToClient": sleBGPInfoControlClientToClient,
       "sleBGPInfoControlClusterID": sleBGPInfoControlClusterID,
       "sleBGPInfoControlConfederationID": sleBGPInfoControlConfederationID,
       "sleBGPInfoControlDeterministicMed": sleBGPInfoControlDeterministicMed,
       "sleBGPInfoControlEnforceFirstAs": sleBGPInfoControlEnforceFirstAs,
       "sleBGPInfoControlFastExternalFailOver": sleBGPInfoControlFastExternalFailOver,
       "sleBGPInfoControlGracefulRestartTime": sleBGPInfoControlGracefulRestartTime,
       "sleBGPInfoControlGracefulStalepathTime": sleBGPInfoControlGracefulStalepathTime,
       "sleBGPInfoControlScanTime": sleBGPInfoControlScanTime,
       "sleBGPInfoControlNexthopTriggerStatus": sleBGPInfoControlNexthopTriggerStatus,
       "sleBGPInfoControlNexthopTriggerDelay": sleBGPInfoControlNexthopTriggerDelay,
       "sleBGPInfoControlSnmpNotification": sleBGPInfoControlSnmpNotification,
       "sleBGPInfoControlUpdateDelay": sleBGPInfoControlUpdateDelay,
       "sleBGPInfoControlExternalRouteDistance": sleBGPInfoControlExternalRouteDistance,
       "sleBGPInfoControlInternalRouteDistance": sleBGPInfoControlInternalRouteDistance,
       "sleBGPInfoControlLocalRouteDistance": sleBGPInfoControlLocalRouteDistance,
       "sleBGPInfoControlMaximumPath": sleBGPInfoControlMaximumPath,
       "sleBGPInfoControlMaximumPathIBGP": sleBGPInfoControlMaximumPathIBGP,
       "sleBGPInfoControlKeepAliveInterval": sleBGPInfoControlKeepAliveInterval,
       "sleBGPInfoControlHoldTime": sleBGPInfoControlHoldTime,
       "sleBGPInfoNotification": sleBGPInfoNotification,
       "sleBGPInfoRouterIDCreated": sleBGPInfoRouterIDCreated,
       "sleBGPInfoRouterIDDeleted": sleBGPInfoRouterIDDeleted,
       "sleBGPInfoLogNeighborChanged": sleBGPInfoLogNeighborChanged,
       "sleBGPInfoAlwaysCompareMedChanged": sleBGPInfoAlwaysCompareMedChanged,
       "sleBGPInfoBestPathAsPathIgnoreChanged": sleBGPInfoBestPathAsPathIgnoreChanged,
       "sleBGPInfoBestPathCompareConfedAsPathChanged": sleBGPInfoBestPathCompareConfedAsPathChanged,
       "sleBGPInfoBestPathCompareRouterIDChanged": sleBGPInfoBestPathCompareRouterIDChanged,
       "sleBGPInfoBestPathCompareMedConfedChanged": sleBGPInfoBestPathCompareMedConfedChanged,
       "sleBGPInfoBestPathCompareMedMisAsWorstChanged": sleBGPInfoBestPathCompareMedMisAsWorstChanged,
       "sleBGPInfoClientToClientChanged": sleBGPInfoClientToClientChanged,
       "sleBGPInfoClusterIDCreated": sleBGPInfoClusterIDCreated,
       "sleBGPInfoClusterIDDeleted": sleBGPInfoClusterIDDeleted,
       "sleBGPInfoConfederationIDChanged": sleBGPInfoConfederationIDChanged,
       "sleBGPInfoDeterministicMedChanged": sleBGPInfoDeterministicMedChanged,
       "sleBGPInfoEnforceFirstAsChanged": sleBGPInfoEnforceFirstAsChanged,
       "sleBGPInfoFastExternalFailOverChanged": sleBGPInfoFastExternalFailOverChanged,
       "sleBGPInfoGracefulRestartProfileChanged": sleBGPInfoGracefulRestartProfileChanged,
       "sleBGPInfoScanTimeChanged": sleBGPInfoScanTimeChanged,
       "sleBGPInfoNexthopTriggerStatusChanged": sleBGPInfoNexthopTriggerStatusChanged,
       "sleBGPInfoNexthopTriggerDelayChanged": sleBGPInfoNexthopTriggerDelayChanged,
       "sleBGPInfoSnmpNotificationChanged": sleBGPInfoSnmpNotificationChanged,
       "sleBGPInfoUpdateDelayChanged": sleBGPInfoUpdateDelayChanged,
       "sleBGPInfoDistanceCreated": sleBGPInfoDistanceCreated,
       "sleBGPInfoDistanceDeleted": sleBGPInfoDistanceDeleted,
       "sleBGPInfoMaximumPathChanged": sleBGPInfoMaximumPathChanged,
       "sleBGPInfoMaximumPathIBGPChanged": sleBGPInfoMaximumPathIBGPChanged,
       "sleBGPInfoTimersChanged": sleBGPInfoTimersChanged,
       "sleBGPAdminDistance": sleBGPAdminDistance,
       "sleBGPAdminDistanceTable": sleBGPAdminDistanceTable,
       "sleBGPAdminDistanceEntry": sleBGPAdminDistanceEntry,
       "sleBGPAdminDistanceAddrPrefix": sleBGPAdminDistanceAddrPrefix,
       "sleBGPAdminDistanceValue": sleBGPAdminDistanceValue,
       "sleBGPAdminDistanceAccName": sleBGPAdminDistanceAccName,
       "sleBGPAdminDistanceControl": sleBGPAdminDistanceControl,
       "sleBGPAdminDistanceControlRequest": sleBGPAdminDistanceControlRequest,
       "sleBGPAdminDistanceControlStatus": sleBGPAdminDistanceControlStatus,
       "sleBGPAdminDistanceControlTimer": sleBGPAdminDistanceControlTimer,
       "sleBGPAdminDistanceControlTimeStamp": sleBGPAdminDistanceControlTimeStamp,
       "sleBGPAdminDistanceControlReqResult": sleBGPAdminDistanceControlReqResult,
       "sleBGPAdminDistanceControlAddrPrefix": sleBGPAdminDistanceControlAddrPrefix,
       "sleBGPAdminDistanceControlValue": sleBGPAdminDistanceControlValue,
       "sleBGPAdminDistanceControlAccName": sleBGPAdminDistanceControlAccName,
       "sleBGPAdminDistanceNotification": sleBGPAdminDistanceNotification,
       "sleBGPAdminDistanceCreated": sleBGPAdminDistanceCreated,
       "sleBGPAdminDistanceDeleted": sleBGPAdminDistanceDeleted,
       "sleBGPPeerInfo": sleBGPPeerInfo,
       "sleBGPPeer": sleBGPPeer,
       "sleBGPPeerTable": sleBGPPeerTable,
       "sleBGPPeerEntry": sleBGPPeerEntry,
       "sleBGPPeerName": sleBGPPeerName,
       "sleBGPPeerAsNum": sleBGPPeerAsNum,
       "sleBGPPeerGroupName": sleBGPPeerGroupName,
       "sleBGPPeerAdvInterval": sleBGPPeerAdvInterval,
       "sleBGPPeerAsOriInterval": sleBGPPeerAsOriInterval,
       "sleBGPPeerDesc": sleBGPPeerDesc,
       "sleBGPPeerDontCapNego": sleBGPPeerDontCapNego,
       "sleBGPPeerWeight": sleBGPPeerWeight,
       "sleBGPPeerEnforcMultiHop": sleBGPPeerEnforcMultiHop,
       "sleBGPPeerPassive": sleBGPPeerPassive,
       "sleBGPPeerUpSourceName": sleBGPPeerUpSourceName,
       "sleBGPPeerPort": sleBGPPeerPort,
       "sleBGPPeerRetstartTime": sleBGPPeerRetstartTime,
       "sleBGPPeerShutDown": sleBGPPeerShutDown,
       "sleBGPPeerKeepInterval": sleBGPPeerKeepInterval,
       "sleBGPPeerHoldInterval": sleBGPPeerHoldInterval,
       "sleBGPPeerConnInterval": sleBGPPeerConnInterval,
       "sleBGPPeerOverCap": sleBGPPeerOverCap,
       "sleBGPPeerStrictCapMatch": sleBGPPeerStrictCapMatch,
       "sleBGPPeerIfname": sleBGPPeerIfname,
       "sleBGPPeerCapRouteRefresh": sleBGPPeerCapRouteRefresh,
       "sleBGPPeerCapDynamic": sleBGPPeerCapDynamic,
       "sleBGPPeerEBGPMulthopCount": sleBGPPeerEBGPMulthopCount,
       "sleBGPPeerPassword": sleBGPPeerPassword,
       "sleBGPPeerControl": sleBGPPeerControl,
       "sleBGPPeerControlRequest": sleBGPPeerControlRequest,
       "sleBGPPeerControlStatus": sleBGPPeerControlStatus,
       "sleBGPPeerControlTimer": sleBGPPeerControlTimer,
       "sleBGPPeerControlTimeStamp": sleBGPPeerControlTimeStamp,
       "sleBGPPeerControlReqResult": sleBGPPeerControlReqResult,
       "sleBGPPeerControlName": sleBGPPeerControlName,
       "sleBGPPeerControlAsNum": sleBGPPeerControlAsNum,
       "sleBGPPeerControlGroupName": sleBGPPeerControlGroupName,
       "sleBGPPeerControlAdvInterval": sleBGPPeerControlAdvInterval,
       "sleBGPPeerControlAsOriInterval": sleBGPPeerControlAsOriInterval,
       "sleBGPPeerControlDesc": sleBGPPeerControlDesc,
       "sleBGPPeerControlDontCapNego": sleBGPPeerControlDontCapNego,
       "sleBGPPeerControlWeight": sleBGPPeerControlWeight,
       "sleBGPPeerControlEnforcMultiHop": sleBGPPeerControlEnforcMultiHop,
       "sleBGPPeerControlPassive": sleBGPPeerControlPassive,
       "sleBGPPeerControlUpSourceName": sleBGPPeerControlUpSourceName,
       "sleBGPPeerControlPort": sleBGPPeerControlPort,
       "sleBGPPeerControlRetstartTime": sleBGPPeerControlRetstartTime,
       "sleBGPPeerControlShutDown": sleBGPPeerControlShutDown,
       "sleBGPPeerControlKeepInterval": sleBGPPeerControlKeepInterval,
       "sleBGPPeerControlHoldInterval": sleBGPPeerControlHoldInterval,
       "sleBGPPeerControlConnInterval": sleBGPPeerControlConnInterval,
       "sleBGPPeerControlOverCap": sleBGPPeerControlOverCap,
       "sleBGPPeerControlStrictCapMatch": sleBGPPeerControlStrictCapMatch,
       "sleBGPPeerControlIfname": sleBGPPeerControlIfname,
       "sleBGPPeerControlCapRouteRefresh": sleBGPPeerControlCapRouteRefresh,
       "sleBGPPeerControlCapDynamic": sleBGPPeerControlCapDynamic,
       "sleBGPPeerControlEBGPMulthopCount": sleBGPPeerControlEBGPMulthopCount,
       "sleBGPPeerControlPassword": sleBGPPeerControlPassword,
       "sleBGPPeerNotification": sleBGPPeerNotification,
       "sleBGPPeerCreated": sleBGPPeerCreated,
       "sleBGPPeerDeleted": sleBGPPeerDeleted,
       "sleBGPPeerGroupNameCreated": sleBGPPeerGroupNameCreated,
       "sleBGPPeerGroupNameDeleted": sleBGPPeerGroupNameDeleted,
       "sleBGPPeerAdvIntervalChanged": sleBGPPeerAdvIntervalChanged,
       "sleBGPPeerAsOriIntervalChanged": sleBGPPeerAsOriIntervalChanged,
       "sleBGPPeerDescCreated": sleBGPPeerDescCreated,
       "sleBGPPeerDescDeleted": sleBGPPeerDescDeleted,
       "sleBGPPeerDontCapNegoChanged": sleBGPPeerDontCapNegoChanged,
       "sleBGPPeerWeightChanged": sleBGPPeerWeightChanged,
       "sleBGPPeerEnforcMultiHopChanged": sleBGPPeerEnforcMultiHopChanged,
       "sleBGPPeerPassiveChanged": sleBGPPeerPassiveChanged,
       "sleBGPPeerUpSourceCreated": sleBGPPeerUpSourceCreated,
       "sleBGPPeerUpSourceDeleted": sleBGPPeerUpSourceDeleted,
       "sleBGPPeerPortChanged": sleBGPPeerPortChanged,
       "sleBGPPeerRetstartTimeChanged": sleBGPPeerRetstartTimeChanged,
       "sleBGPPeerShutDownChanged": sleBGPPeerShutDownChanged,
       "sleBGPPeerTimersProfileChanged": sleBGPPeerTimersProfileChanged,
       "sleBGPPeerConnIntervalChanged": sleBGPPeerConnIntervalChanged,
       "sleBGPPeerOverCapChanged": sleBGPPeerOverCapChanged,
       "sleBGPPeerStrictCapMatchChanged": sleBGPPeerStrictCapMatchChanged,
       "sleBGPPeerIfnameCreated": sleBGPPeerIfnameCreated,
       "sleBGPPeerIfnameDeleted": sleBGPPeerIfnameDeleted,
       "sleBGPPeerCapRouteRefreshChanged": sleBGPPeerCapRouteRefreshChanged,
       "sleBGPPeerCapDynamicChanged": sleBGPPeerCapDynamicChanged,
       "sleBGPPeerEBGPMultihopCountChanged": sleBGPPeerEBGPMultihopCountChanged,
       "sleBGPPeerPasswordCreated": sleBGPPeerPasswordCreated,
       "sleBGPPeerPasswordDeleted": sleBGPPeerPasswordDeleted,
       "sleBGPPeerGroup": sleBGPPeerGroup,
       "sleBGPPeerGroupTable": sleBGPPeerGroupTable,
       "sleBGPPeerGroupEntry": sleBGPPeerGroupEntry,
       "sleBGPPeerGroupStr": sleBGPPeerGroupStr,
       "sleBGPPeerGroupAsNum": sleBGPPeerGroupAsNum,
       "sleBGPPeerGroupAdvInterval": sleBGPPeerGroupAdvInterval,
       "sleBGPPeerGroupAsOriInterval": sleBGPPeerGroupAsOriInterval,
       "sleBGPPeerGroupDesc": sleBGPPeerGroupDesc,
       "sleBGPPeerGroupDontCapNego": sleBGPPeerGroupDontCapNego,
       "sleBGPPeerGroupWeight": sleBGPPeerGroupWeight,
       "sleBGPPeerGroupEnforcMultiHop": sleBGPPeerGroupEnforcMultiHop,
       "sleBGPPeerGroupPassive": sleBGPPeerGroupPassive,
       "sleBGPPeerGroupUpSourceName": sleBGPPeerGroupUpSourceName,
       "sleBGPPeerGroupPort": sleBGPPeerGroupPort,
       "sleBGPPeerGroupRetstartTime": sleBGPPeerGroupRetstartTime,
       "sleBGPPeerGroupShutDown": sleBGPPeerGroupShutDown,
       "sleBGPPeerGroupKeepInterval": sleBGPPeerGroupKeepInterval,
       "sleBGPPeerGroupHoldInterval": sleBGPPeerGroupHoldInterval,
       "sleBGPPeerGroupConnInterval": sleBGPPeerGroupConnInterval,
       "sleBGPPeerGroupOverCap": sleBGPPeerGroupOverCap,
       "sleBGPPeerGroupStrictCapMatch": sleBGPPeerGroupStrictCapMatch,
       "sleBGPPeerGroupCapRouteRefresh": sleBGPPeerGroupCapRouteRefresh,
       "sleBGPPeerGroupCapDynamic": sleBGPPeerGroupCapDynamic,
       "sleBGPPeerGroupEBGPMulthopCount": sleBGPPeerGroupEBGPMulthopCount,
       "sleBGPPeerGroupPassword": sleBGPPeerGroupPassword,
       "sleBGPPeerGroupControl": sleBGPPeerGroupControl,
       "sleBGPPeerGroupControlRequest": sleBGPPeerGroupControlRequest,
       "sleBGPPeerGroupControlStatus": sleBGPPeerGroupControlStatus,
       "sleBGPPeerGroupControlTimer": sleBGPPeerGroupControlTimer,
       "sleBGPPeerGroupControlTimeStamp": sleBGPPeerGroupControlTimeStamp,
       "sleBGPPeerGroupControlReqResult": sleBGPPeerGroupControlReqResult,
       "sleBGPPeerGroupControlStr": sleBGPPeerGroupControlStr,
       "sleBGPPeerGroupControlAsNum": sleBGPPeerGroupControlAsNum,
       "sleBGPPeerGroupControlAdvInterval": sleBGPPeerGroupControlAdvInterval,
       "sleBGPPeerGroupControlAsOriInterval": sleBGPPeerGroupControlAsOriInterval,
       "sleBGPPeerGroupControlDesc": sleBGPPeerGroupControlDesc,
       "sleBGPPeerGroupControlDontCapNego": sleBGPPeerGroupControlDontCapNego,
       "sleBGPPeerGroupControlWeight": sleBGPPeerGroupControlWeight,
       "sleBGPPeerGroupControlEnforcMultiHop": sleBGPPeerGroupControlEnforcMultiHop,
       "sleBGPPeerGroupControlPassive": sleBGPPeerGroupControlPassive,
       "sleBGPPeerGroupControlUpSourceName": sleBGPPeerGroupControlUpSourceName,
       "sleBGPPeerGroupControlPort": sleBGPPeerGroupControlPort,
       "sleBGPPeerGroupControlRetstartTime": sleBGPPeerGroupControlRetstartTime,
       "sleBGPPeerGroupControlShutDown": sleBGPPeerGroupControlShutDown,
       "sleBGPPeerGroupControlKeepInterval": sleBGPPeerGroupControlKeepInterval,
       "sleBGPPeerGroupControlHoldInterval": sleBGPPeerGroupControlHoldInterval,
       "sleBGPPeerGroupControlConnInterval": sleBGPPeerGroupControlConnInterval,
       "sleBGPPeerGroupControlOverCap": sleBGPPeerGroupControlOverCap,
       "sleBGPPeerGroupControlStrictCapMatch": sleBGPPeerGroupControlStrictCapMatch,
       "sleBGPPeerGroupControlCapRouteRefresh": sleBGPPeerGroupControlCapRouteRefresh,
       "sleBGPPeerGroupControlCapDynamic": sleBGPPeerGroupControlCapDynamic,
       "sleBGPPeerGroupControlEBGPMulthopCount": sleBGPPeerGroupControlEBGPMulthopCount,
       "sleBGPPeerGroupControlPassword": sleBGPPeerGroupControlPassword,
       "sleBGPPeerGroupNotification": sleBGPPeerGroupNotification,
       "sleBGPPeerGroupCreated": sleBGPPeerGroupCreated,
       "sleBGPPeerGroupDeleted": sleBGPPeerGroupDeleted,
       "sleBGPPeerGroupRemoteAsChanged": sleBGPPeerGroupRemoteAsChanged,
       "sleBGPPeerGroupAdvIntervalChanged": sleBGPPeerGroupAdvIntervalChanged,
       "sleBGPPeerGroupAsOriIntervalChanged": sleBGPPeerGroupAsOriIntervalChanged,
       "sleBGPPeerGroupDescCreated": sleBGPPeerGroupDescCreated,
       "sleBGPPeerGroupDescDeleted": sleBGPPeerGroupDescDeleted,
       "sleBGPPeerGroupDontCapNegoChanged": sleBGPPeerGroupDontCapNegoChanged,
       "sleBGPPeerGroupWeightChanged": sleBGPPeerGroupWeightChanged,
       "sleBGPPeerGroupPassiveChanged": sleBGPPeerGroupPassiveChanged,
       "sleBGPPeerGroupUpSourceCreated": sleBGPPeerGroupUpSourceCreated,
       "sleBGPPeerGroupUpSourceDeleted": sleBGPPeerGroupUpSourceDeleted,
       "sleBGPPeerGroupPortChanged": sleBGPPeerGroupPortChanged,
       "sleBGPPeerGroupRetstartTimeChanged": sleBGPPeerGroupRetstartTimeChanged,
       "sleBGPPeerGroupShutDownChanged": sleBGPPeerGroupShutDownChanged,
       "sleBGPPeerGroupTimersProfileChanged": sleBGPPeerGroupTimersProfileChanged,
       "sleBGPPeerGroupConnIntervalChanged": sleBGPPeerGroupConnIntervalChanged,
       "sleBGPPeerGroupOverCapChanged": sleBGPPeerGroupOverCapChanged,
       "sleBGPPeerGroupStrictCapMatchChanged": sleBGPPeerGroupStrictCapMatchChanged,
       "sleBGPPeerGroupCapRouteRefreshChanged": sleBGPPeerGroupCapRouteRefreshChanged,
       "sleBGPPeerGroupCapDynamicChanged": sleBGPPeerGroupCapDynamicChanged,
       "sleBGPPeerGroupEBGPMultihopCountChanged": sleBGPPeerGroupEBGPMultihopCountChanged,
       "sleBGPPeerGroupPasswordCreated": sleBGPPeerGroupPasswordCreated,
       "sleBGPPeerGroupPasswordDeleted": sleBGPPeerGroupPasswordDeleted,
       "sleBGPAFInfo": sleBGPAFInfo,
       "sleBGPAFBase": sleBGPAFBase,
       "sleBGPAFBaseTable": sleBGPAFBaseTable,
       "sleBGPAFBaseEntry": sleBGPAFBaseEntry,
       "sleBGPAFBaseMode": sleBGPAFBaseMode,
       "sleBGPAFBaseType": sleBGPAFBaseType,
       "sleBGPAFBaseNetworkCheck": sleBGPAFBaseNetworkCheck,
       "sleBGPAFBaseSync": sleBGPAFBaseSync,
       "sleBGPAFBaseDefOrg": sleBGPAFBaseDefOrg,
       "sleBGPAFBaseDampRoutemapName": sleBGPAFBaseDampRoutemapName,
       "sleBGPAFBaseDampReachHlife": sleBGPAFBaseDampReachHlife,
       "sleBGPAFBaseDampReuse": sleBGPAFBaseDampReuse,
       "sleBGPAFBaseDampSuppress": sleBGPAFBaseDampSuppress,
       "sleBGPAFBaseDampMaxSuppress": sleBGPAFBaseDampMaxSuppress,
       "sleBGPAFBaseDampUnReachHlife": sleBGPAFBaseDampUnReachHlife,
       "sleBGPAFBaseControl": sleBGPAFBaseControl,
       "sleBGPAFBaseControlRequest": sleBGPAFBaseControlRequest,
       "sleBGPAFBaseControlStatus": sleBGPAFBaseControlStatus,
       "sleBGPAFBaseControlTimer": sleBGPAFBaseControlTimer,
       "sleBGPAFBaseControlTimeStamp": sleBGPAFBaseControlTimeStamp,
       "sleBGPAFBaseControlReqResult": sleBGPAFBaseControlReqResult,
       "sleBGPAFBaseControlMode": sleBGPAFBaseControlMode,
       "sleBGPAFBaseControlType": sleBGPAFBaseControlType,
       "sleBGPAFBaseControlNetworkCheck": sleBGPAFBaseControlNetworkCheck,
       "sleBGPAFBaseControlSync": sleBGPAFBaseControlSync,
       "sleBGPAFBaseControlDefOrg": sleBGPAFBaseControlDefOrg,
       "sleBGPAFBaseControlDampRoutemapName": sleBGPAFBaseControlDampRoutemapName,
       "sleBGPAFBaseControlDampReachHlife": sleBGPAFBaseControlDampReachHlife,
       "sleBGPAFBaseControlDampReuse": sleBGPAFBaseControlDampReuse,
       "sleBGPAFBaseControlDampSuppress": sleBGPAFBaseControlDampSuppress,
       "sleBGPAFBaseControlDampMaxSuppress": sleBGPAFBaseControlDampMaxSuppress,
       "sleBGPAFBaseControlDampUnReachHlife": sleBGPAFBaseControlDampUnReachHlife,
       "sleBGPAFBaseNotification": sleBGPAFBaseNotification,
       "sleBGPAFBaseNetworkCheckChanged": sleBGPAFBaseNetworkCheckChanged,
       "sleBGPAFBaseSyncChanged": sleBGPAFBaseSyncChanged,
       "sleBGPAFBaseDefOrgChanged": sleBGPAFBaseDefOrgChanged,
       "sleBGPAFBaseDampRoutemapNameChanged": sleBGPAFBaseDampRoutemapNameChanged,
       "sleBGPAFBaseDampTimeProfileChanged": sleBGPAFBaseDampTimeProfileChanged,
       "sleBGPAFBaseDampDeleted": sleBGPAFBaseDampDeleted,
       "sleBGPAFRedist": sleBGPAFRedist,
       "sleBGPAFRedistTable": sleBGPAFRedistTable,
       "sleBGPAFRedistEntry": sleBGPAFRedistEntry,
       "sleBGPAFRedistMode": sleBGPAFRedistMode,
       "sleBGPAFRedistType": sleBGPAFRedistType,
       "sleBGPAFRedistProtoType": sleBGPAFRedistProtoType,
       "sleBGPAFRedistRoutemapName": sleBGPAFRedistRoutemapName,
       "sleBGPAFRedistControl": sleBGPAFRedistControl,
       "sleBGPAFRedistControlRequest": sleBGPAFRedistControlRequest,
       "sleBGPAFRedistControlStatus": sleBGPAFRedistControlStatus,
       "sleBGPAFRedistControlTimer": sleBGPAFRedistControlTimer,
       "sleBGPAFRedistControlTimeStamp": sleBGPAFRedistControlTimeStamp,
       "sleBGPAFRedistControlReqResult": sleBGPAFRedistControlReqResult,
       "sleBGPAFRedistControlMode": sleBGPAFRedistControlMode,
       "sleBGPAFRedistControlType": sleBGPAFRedistControlType,
       "sleBGPAFRedistControlProtoType": sleBGPAFRedistControlProtoType,
       "sleBGPAFRedistControlRoutemapName": sleBGPAFRedistControlRoutemapName,
       "sleBGPAFRedistNotification": sleBGPAFRedistNotification,
       "sleBGPAFRedistributeCreated": sleBGPAFRedistributeCreated,
       "sleBGPAFRedistributeDeleted": sleBGPAFRedistributeDeleted,
       "sleBGPAFRedistributeChanged": sleBGPAFRedistributeChanged,
       "sleBGPAFAggreAddr": sleBGPAFAggreAddr,
       "sleBGPAFAggreAddrTable": sleBGPAFAggreAddrTable,
       "sleBGPAFAggreAddrEntry": sleBGPAFAggreAddrEntry,
       "sleBGPAFAggreAddrMode": sleBGPAFAggreAddrMode,
       "sleBGPAFAggreAddrType": sleBGPAFAggreAddrType,
       "sleBGPAFAggreAddrPrefix": sleBGPAFAggreAddrPrefix,
       "sleBGPAFAggreAddrAsSet": sleBGPAFAggreAddrAsSet,
       "sleBGPAFAggreAddrSummOnly": sleBGPAFAggreAddrSummOnly,
       "sleBGPAFAggreAddrControl": sleBGPAFAggreAddrControl,
       "sleBGPAFAggreAddrControlRequest": sleBGPAFAggreAddrControlRequest,
       "sleBGPAFAggreAddrControlStatus": sleBGPAFAggreAddrControlStatus,
       "sleBGPAFAggreAddrControlTimer": sleBGPAFAggreAddrControlTimer,
       "sleBGPAFAggreAddrControlTimeStamp": sleBGPAFAggreAddrControlTimeStamp,
       "sleBGPAFAggreAddrControlReqResult": sleBGPAFAggreAddrControlReqResult,
       "sleBGPAFAggreAddrControlMode": sleBGPAFAggreAddrControlMode,
       "sleBGPAFAggreAddrControlType": sleBGPAFAggreAddrControlType,
       "sleBGPAFAggreAddrControlAddrPrefix": sleBGPAFAggreAddrControlAddrPrefix,
       "sleBGPAFAggreAddrControlAsSet": sleBGPAFAggreAddrControlAsSet,
       "sleBGPAFAggreAddrControlSummOnly": sleBGPAFAggreAddrControlSummOnly,
       "sleBGPAFAggreAddrNotification": sleBGPAFAggreAddrNotification,
       "sleBGPAFAggreAddressCreated": sleBGPAFAggreAddressCreated,
       "sleBGPAFAggreAddressDeleted": sleBGPAFAggreAddressDeleted,
       "sleBGPAFPeerInfo": sleBGPAFPeerInfo,
       "sleBGPAFPeer": sleBGPAFPeer,
       "sleBGPAFPeerTable": sleBGPAFPeerTable,
       "sleBGPAFPeerEntry": sleBGPAFPeerEntry,
       "sleBGPAFPeerMode": sleBGPAFPeerMode,
       "sleBGPAFPeerType": sleBGPAFPeerType,
       "sleBGPAFPeerName": sleBGPAFPeerName,
       "sleBGPAFPeerActviate": sleBGPAFPeerActviate,
       "sleBGPAFPeerAllowAsIn": sleBGPAFPeerAllowAsIn,
       "sleBGPAFPeerAllowAsInNum": sleBGPAFPeerAllowAsInNum,
       "sleBGPAFPeerAttrUnchangedAsPath": sleBGPAFPeerAttrUnchangedAsPath,
       "sleBGPAFPeerAttrUnchangedMed": sleBGPAFPeerAttrUnchangedMed,
       "sleBGPAFPeerAttrUnchangedNexthop": sleBGPAFPeerAttrUnchangedNexthop,
       "sleBGPAFPeerCapGracefulRestart": sleBGPAFPeerCapGracefulRestart,
       "sleBGPAFPeerCapOrfMode": sleBGPAFPeerCapOrfMode,
       "sleBGPAFPeerDefOriginate": sleBGPAFPeerDefOriginate,
       "sleBGPAFPeerDefOriginateRoutemap": sleBGPAFPeerDefOriginateRoutemap,
       "sleBGPAFPeerFLInAccName": sleBGPAFPeerFLInAccName,
       "sleBGPAFPeerFLOutAccName": sleBGPAFPeerFLOutAccName,
       "sleBGPAFPeerMaxPrefixNum": sleBGPAFPeerMaxPrefixNum,
       "sleBGPAFPeerMaxPrefixThreshold": sleBGPAFPeerMaxPrefixThreshold,
       "sleBGPAFPeerMaxPrefixWarnOnly": sleBGPAFPeerMaxPrefixWarnOnly,
       "sleBGPAFPeerRemotePrivateAs": sleBGPAFPeerRemotePrivateAs,
       "sleBGPAFPeerInRoutemap": sleBGPAFPeerInRoutemap,
       "sleBGPAFPeerOutRoutemap": sleBGPAFPeerOutRoutemap,
       "sleBGPAFPeerRouteReflectClient": sleBGPAFPeerRouteReflectClient,
       "sleBGPAFPeerRouteServerClient": sleBGPAFPeerRouteServerClient,
       "sleBGPAFPeerInDistListName": sleBGPAFPeerInDistListName,
       "sleBGPAFPeerOutDistListName": sleBGPAFPeerOutDistListName,
       "sleBGPAFPeerInPrefixListName": sleBGPAFPeerInPrefixListName,
       "sleBGPAFPeerOutPrefixListName": sleBGPAFPeerOutPrefixListName,
       "sleBGPAFPeerSendCommunity": sleBGPAFPeerSendCommunity,
       "sleBGPAFPeerNexthopSelf": sleBGPAFPeerNexthopSelf,
       "sleBGPAFPeerSoftReconfig": sleBGPAFPeerSoftReconfig,
       "sleBGPAFPeerUnsuppressMapName": sleBGPAFPeerUnsuppressMapName,
       "sleBGPAFPeerControl": sleBGPAFPeerControl,
       "sleBGPAFPeerControlRequest": sleBGPAFPeerControlRequest,
       "sleBGPAFPeerControlStatus": sleBGPAFPeerControlStatus,
       "sleBGPAFPeerControlTimer": sleBGPAFPeerControlTimer,
       "sleBGPAFPeerControlTimeStamp": sleBGPAFPeerControlTimeStamp,
       "sleBGPAFPeerControlReqResult": sleBGPAFPeerControlReqResult,
       "sleBGPAFPeerControlMode": sleBGPAFPeerControlMode,
       "sleBGPAFPeerControlType": sleBGPAFPeerControlType,
       "sleBGPAFPeerControlName": sleBGPAFPeerControlName,
       "sleBGPAFPeerControlActviate": sleBGPAFPeerControlActviate,
       "sleBGPAFPeerControlAllowAsIn": sleBGPAFPeerControlAllowAsIn,
       "sleBGPAFPeerControlAllowAsInNum": sleBGPAFPeerControlAllowAsInNum,
       "sleBGPAFPeerControlAttrUnchangedAsPath": sleBGPAFPeerControlAttrUnchangedAsPath,
       "sleBGPAFPeerControlAttrUnchangedMed": sleBGPAFPeerControlAttrUnchangedMed,
       "sleBGPAFPeerControlAttrUnchangedNexthop": sleBGPAFPeerControlAttrUnchangedNexthop,
       "sleBGPAFPeerControlCapGracefulRestart": sleBGPAFPeerControlCapGracefulRestart,
       "sleBGPAFPeerControlCapOrfMode": sleBGPAFPeerControlCapOrfMode,
       "sleBGPAFPeerControlDefOriginate": sleBGPAFPeerControlDefOriginate,
       "sleBGPAFPeerControlDefOriginateRoutemap": sleBGPAFPeerControlDefOriginateRoutemap,
       "sleBGPAFPeerControlFLInAccName": sleBGPAFPeerControlFLInAccName,
       "sleBGPAFPeerControlFLOutAccName": sleBGPAFPeerControlFLOutAccName,
       "sleBGPAFPeerControlMaxPrefixNum": sleBGPAFPeerControlMaxPrefixNum,
       "sleBGPAFPeerControlMaxPrefixThreshold": sleBGPAFPeerControlMaxPrefixThreshold,
       "sleBGPAFPeerControlMaxPrefixWarnOnly": sleBGPAFPeerControlMaxPrefixWarnOnly,
       "sleBGPAFPeerControlRemotePrivateAs": sleBGPAFPeerControlRemotePrivateAs,
       "sleBGPAFPeerControlInRoutemap": sleBGPAFPeerControlInRoutemap,
       "sleBGPAFPeerControlOutRoutemap": sleBGPAFPeerControlOutRoutemap,
       "sleBGPAFPeerControlRouteReflectClient": sleBGPAFPeerControlRouteReflectClient,
       "sleBGPAFPeerControlRouteServerClient": sleBGPAFPeerControlRouteServerClient,
       "sleBGPAFPeerControlInDistListName": sleBGPAFPeerControlInDistListName,
       "sleBGPAFPeerControlOutDistListName": sleBGPAFPeerControlOutDistListName,
       "sleBGPAFPeerControlInPrefixListName": sleBGPAFPeerControlInPrefixListName,
       "sleBGPAFPeerControlOutPrefixListName": sleBGPAFPeerControlOutPrefixListName,
       "sleBGPAFPeerControlSendCommunity": sleBGPAFPeerControlSendCommunity,
       "sleBGPAFPeerControlNexthopSelf": sleBGPAFPeerControlNexthopSelf,
       "sleBGPAFPeerControlSoftReconfig": sleBGPAFPeerControlSoftReconfig,
       "sleBGPAFPeerControlUnsuppressMapName": sleBGPAFPeerControlUnsuppressMapName,
       "sleBGPAFPeerNotification": sleBGPAFPeerNotification,
       "sleBGPAFPeerActviateChanged": sleBGPAFPeerActviateChanged,
       "sleBGPAFPeerAllowAsInChanged": sleBGPAFPeerAllowAsInChanged,
       "sleBGPAFPeerAttrUnchangedProfileChanged": sleBGPAFPeerAttrUnchangedProfileChanged,
       "sleBGPAFPeerCapGracefulRestartChanged": sleBGPAFPeerCapGracefulRestartChanged,
       "sleBGPAFPeerCapOrfModeChanged": sleBGPAFPeerCapOrfModeChanged,
       "sleBGPAFPeerDefOriginateChanged": sleBGPAFPeerDefOriginateChanged,
       "sleBGPAFPeerFLInAccNameChanged": sleBGPAFPeerFLInAccNameChanged,
       "sleBGPAFPeerFLOutAccNameChanged": sleBGPAFPeerFLOutAccNameChanged,
       "sleBGPAFPeerMaxPrefixProfileChanged": sleBGPAFPeerMaxPrefixProfileChanged,
       "sleBGPAFPeerRemotePrivateAsChanged": sleBGPAFPeerRemotePrivateAsChanged,
       "sleBGPAFPeerInRoutemapChanged": sleBGPAFPeerInRoutemapChanged,
       "sleBGPAFPeerOutRoutemapChanged": sleBGPAFPeerOutRoutemapChanged,
       "sleBGPAFPeerRouteReflectClientChanged": sleBGPAFPeerRouteReflectClientChanged,
       "sleBGPAFPeerRouteServerClientChanged": sleBGPAFPeerRouteServerClientChanged,
       "sleBGPAFPeerInDistListNameChanged": sleBGPAFPeerInDistListNameChanged,
       "sleBGPAFPeerOutDistListNameChanged": sleBGPAFPeerOutDistListNameChanged,
       "sleBGPAFPeerInPrefixListNameChanged": sleBGPAFPeerInPrefixListNameChanged,
       "sleBGPAFPeerOutPrefixListNameChanged": sleBGPAFPeerOutPrefixListNameChanged,
       "sleBGPAFPeerSendCommunityChanged": sleBGPAFPeerSendCommunityChanged,
       "sleBGPAFPeerNexthopSelfChanged": sleBGPAFPeerNexthopSelfChanged,
       "sleBGPAFPeerSoftReconfigChanged": sleBGPAFPeerSoftReconfigChanged,
       "sleBGPAFPeerUnsuppressMapNameChanged": sleBGPAFPeerUnsuppressMapNameChanged,
       "sleBGPAFPeerGroup": sleBGPAFPeerGroup,
       "sleBGPAFPeerGroupTable": sleBGPAFPeerGroupTable,
       "sleBGPAFPeerGroupEntry": sleBGPAFPeerGroupEntry,
       "sleBGPAFPeerGroupMode": sleBGPAFPeerGroupMode,
       "sleBGPAFPeerGroupType": sleBGPAFPeerGroupType,
       "sleBGPAFPeerGroupName": sleBGPAFPeerGroupName,
       "sleBGPAFPeerGroupActviate": sleBGPAFPeerGroupActviate,
       "sleBGPAFPeerGroupAllowAsIn": sleBGPAFPeerGroupAllowAsIn,
       "sleBGPAFPeerGroupAllowAsInNum": sleBGPAFPeerGroupAllowAsInNum,
       "sleBGPAFPeerGroupAttrUnchangedAsPath": sleBGPAFPeerGroupAttrUnchangedAsPath,
       "sleBGPAFPeerGroupAttrUnchangedMed": sleBGPAFPeerGroupAttrUnchangedMed,
       "sleBGPAFPeerGroupAttrUnchangedNexthop": sleBGPAFPeerGroupAttrUnchangedNexthop,
       "sleBGPAFPeerGroupCapGracefulRestart": sleBGPAFPeerGroupCapGracefulRestart,
       "sleBGPAFPeerGroupCapOrfMode": sleBGPAFPeerGroupCapOrfMode,
       "sleBGPAFPeerGroupDefOriginate": sleBGPAFPeerGroupDefOriginate,
       "sleBGPAFPeerGroupDefOriginateRoutemap": sleBGPAFPeerGroupDefOriginateRoutemap,
       "sleBGPAFPeerGroupFLInAccName": sleBGPAFPeerGroupFLInAccName,
       "sleBGPAFPeerGroupFLOutAccName": sleBGPAFPeerGroupFLOutAccName,
       "sleBGPAFPeerGroupMaxPrefixNum": sleBGPAFPeerGroupMaxPrefixNum,
       "sleBGPAFPeerGroupMaxPrefixThreshold": sleBGPAFPeerGroupMaxPrefixThreshold,
       "sleBGPAFPeerGroupMaxPrefixWarnOnly": sleBGPAFPeerGroupMaxPrefixWarnOnly,
       "sleBGPAFPeerGroupRemotePrivateAs": sleBGPAFPeerGroupRemotePrivateAs,
       "sleBGPAFPeerGroupInRoutemap": sleBGPAFPeerGroupInRoutemap,
       "sleBGPAFPeerGroupOutRoutemap": sleBGPAFPeerGroupOutRoutemap,
       "sleBGPAFPeerGroupRouteReflectClient": sleBGPAFPeerGroupRouteReflectClient,
       "sleBGPAFPeerGroupRouteServerClient": sleBGPAFPeerGroupRouteServerClient,
       "sleBGPAFPeerGroupInDistListName": sleBGPAFPeerGroupInDistListName,
       "sleBGPAFPeerGroupOutDistListName": sleBGPAFPeerGroupOutDistListName,
       "sleBGPAFPeerGroupInPrefixListName": sleBGPAFPeerGroupInPrefixListName,
       "sleBGPAFPeerGroupOutPrefixListName": sleBGPAFPeerGroupOutPrefixListName,
       "sleBGPAFPeerGroupSendCommunity": sleBGPAFPeerGroupSendCommunity,
       "sleBGPAFPeerGroupNexthopSelf": sleBGPAFPeerGroupNexthopSelf,
       "sleBGPAFPeerGroupSoftReconfig": sleBGPAFPeerGroupSoftReconfig,
       "sleBGPAFPeerGroupUnsuppressMapName": sleBGPAFPeerGroupUnsuppressMapName,
       "sleBGPAFPeerGroupControl": sleBGPAFPeerGroupControl,
       "sleBGPAFPeerGroupControlRequest": sleBGPAFPeerGroupControlRequest,
       "sleBGPAFPeerGroupControlStatus": sleBGPAFPeerGroupControlStatus,
       "sleBGPAFPeerGroupControlTimer": sleBGPAFPeerGroupControlTimer,
       "sleBGPAFPeerGroupControlTimeStamp": sleBGPAFPeerGroupControlTimeStamp,
       "sleBGPAFPeerGroupControlReqResult": sleBGPAFPeerGroupControlReqResult,
       "sleBGPAFPeerGroupControlMode": sleBGPAFPeerGroupControlMode,
       "sleBGPAFPeerGroupControlType": sleBGPAFPeerGroupControlType,
       "sleBGPAFPeerGroupControlName": sleBGPAFPeerGroupControlName,
       "sleBGPAFPeerGroupControlActviate": sleBGPAFPeerGroupControlActviate,
       "sleBGPAFPeerGroupControlAllowAsIn": sleBGPAFPeerGroupControlAllowAsIn,
       "sleBGPAFPeerGroupControlAllowAsInNum": sleBGPAFPeerGroupControlAllowAsInNum,
       "sleBGPAFPeerGroupControlAttrUnchangedAsPath": sleBGPAFPeerGroupControlAttrUnchangedAsPath,
       "sleBGPAFPeerGroupControlAttrUnchangedMed": sleBGPAFPeerGroupControlAttrUnchangedMed,
       "sleBGPAFPeerGroupControlAttrUnchangedNexthop": sleBGPAFPeerGroupControlAttrUnchangedNexthop,
       "sleBGPAFPeerGroupControlCapGracefulRestart": sleBGPAFPeerGroupControlCapGracefulRestart,
       "sleBGPAFPeerGroupControlCapOrfMode": sleBGPAFPeerGroupControlCapOrfMode,
       "sleBGPAFPeerGroupControlDefOriginate": sleBGPAFPeerGroupControlDefOriginate,
       "sleBGPAFPeerGroupControlDefOriginateRoutemap": sleBGPAFPeerGroupControlDefOriginateRoutemap,
       "sleBGPAFPeerGroupControlFLInAccName": sleBGPAFPeerGroupControlFLInAccName,
       "sleBGPAFPeerGroupControlFLOutAccName": sleBGPAFPeerGroupControlFLOutAccName,
       "sleBGPAFPeerGroupControlMaxPrefixNum": sleBGPAFPeerGroupControlMaxPrefixNum,
       "sleBGPAFPeerGroupControlMaxPrefixThreshold": sleBGPAFPeerGroupControlMaxPrefixThreshold,
       "sleBGPAFPeerGroupControlMaxPrefixWarnOnly": sleBGPAFPeerGroupControlMaxPrefixWarnOnly,
       "sleBGPAFPeerGroupControlRemotePrivateAs": sleBGPAFPeerGroupControlRemotePrivateAs,
       "sleBGPAFPeerGroupControlInRoutemap": sleBGPAFPeerGroupControlInRoutemap,
       "sleBGPAFPeerGroupControlOutRoutemap": sleBGPAFPeerGroupControlOutRoutemap,
       "sleBGPAFPeerGroupControlRouteReflectClient": sleBGPAFPeerGroupControlRouteReflectClient,
       "sleBGPAFPeerGroupControlRouteServerClient": sleBGPAFPeerGroupControlRouteServerClient,
       "sleBGPAFPeerGroupControlInDistListName": sleBGPAFPeerGroupControlInDistListName,
       "sleBGPAFPeerGroupControlOutDistListName": sleBGPAFPeerGroupControlOutDistListName,
       "sleBGPAFPeerGroupControlInPrefixListName": sleBGPAFPeerGroupControlInPrefixListName,
       "sleBGPAFPeerGroupControlOutPrefixListName": sleBGPAFPeerGroupControlOutPrefixListName,
       "sleBGPAFPeerGroupControlSendCommunity": sleBGPAFPeerGroupControlSendCommunity,
       "sleBGPAFPeerGroupControlNexthopSelf": sleBGPAFPeerGroupControlNexthopSelf,
       "sleBGPAFPeerGroupControlSoftReconfig": sleBGPAFPeerGroupControlSoftReconfig,
       "sleBGPAFPeerGroupControlUnsuppressMapName": sleBGPAFPeerGroupControlUnsuppressMapName,
       "sleBGPAFPeerGroupNotification": sleBGPAFPeerGroupNotification,
       "sleBGPAFPeerGroupActviateChanged": sleBGPAFPeerGroupActviateChanged,
       "sleBGPAFPeerGroupAllowAsInChanged": sleBGPAFPeerGroupAllowAsInChanged,
       "sleBGPAFPeerGroupAttrUnchangedProfileChanged": sleBGPAFPeerGroupAttrUnchangedProfileChanged,
       "sleBGPAFPeerGroupCapGracefulRestartChanged": sleBGPAFPeerGroupCapGracefulRestartChanged,
       "sleBGPAFPeerGroupCapOrfModeChanged": sleBGPAFPeerGroupCapOrfModeChanged,
       "sleBGPAFPeerGroupDefOriginateChanged": sleBGPAFPeerGroupDefOriginateChanged,
       "sleBGPAFPeerGroupFLInAccNameChanged": sleBGPAFPeerGroupFLInAccNameChanged,
       "sleBGPAFPeerGroupFLOutAccNameChanged": sleBGPAFPeerGroupFLOutAccNameChanged,
       "sleBGPAFPeerGroupMaxPrefixProfileChanged": sleBGPAFPeerGroupMaxPrefixProfileChanged,
       "sleBGPAFPeerGroupRemotePrivateAsChanged": sleBGPAFPeerGroupRemotePrivateAsChanged,
       "sleBGPAFPeerGroupInRoutemapChanged": sleBGPAFPeerGroupInRoutemapChanged,
       "sleBGPAFPeerGroupOutRoutemapChanged": sleBGPAFPeerGroupOutRoutemapChanged,
       "sleBGPAFPeerGroupRouteReflectClientChanged": sleBGPAFPeerGroupRouteReflectClientChanged,
       "sleBGPAFPeerGroupRouteServerClientChanged": sleBGPAFPeerGroupRouteServerClientChanged,
       "sleBGPAFPeerGroupInDistListNameChanged": sleBGPAFPeerGroupInDistListNameChanged,
       "sleBGPAFPeerGroupOutDistListNameChanged": sleBGPAFPeerGroupOutDistListNameChanged,
       "sleBGPAFPeerGroupInPrefixListNameChanged": sleBGPAFPeerGroupInPrefixListNameChanged,
       "sleBGPAFPeerGroupOutPrefixListNameChanged": sleBGPAFPeerGroupOutPrefixListNameChanged,
       "sleBGPAFPeerGroupSendCommunityChanged": sleBGPAFPeerGroupSendCommunityChanged,
       "sleBGPAFPeerGroupNexthopSelfChanged": sleBGPAFPeerGroupNexthopSelfChanged,
       "sleBGPAFPeerGroupSoftReconfigChanged": sleBGPAFPeerGroupSoftReconfigChanged,
       "sleBGPAFPeerGroupUnsuppressMapNameChanged": sleBGPAFPeerGroupUnsuppressMapNameChanged,
       "sleBGPAFNetwork": sleBGPAFNetwork,
       "sleBGPAFNetworkTable": sleBGPAFNetworkTable,
       "sleBGPAFNetworkEntry": sleBGPAFNetworkEntry,
       "sleBGPAFNetworkMode": sleBGPAFNetworkMode,
       "sleBGPAFNetworkType": sleBGPAFNetworkType,
       "sleBGPAFNetworkAddrPrefix": sleBGPAFNetworkAddrPrefix,
       "sleBGPAFNetworkBackdoor": sleBGPAFNetworkBackdoor,
       "sleBGPAFNetworkRoutemap": sleBGPAFNetworkRoutemap,
       "sleBGPAFNetworkControl": sleBGPAFNetworkControl,
       "sleBGPAFNetworkControlRequest": sleBGPAFNetworkControlRequest,
       "sleBGPAFNetworkControlStatus": sleBGPAFNetworkControlStatus,
       "sleBGPAFNetworkControlTimer": sleBGPAFNetworkControlTimer,
       "sleBGPAFNetworkControlTimeStamp": sleBGPAFNetworkControlTimeStamp,
       "sleBGPAFNetworkControlReqResult": sleBGPAFNetworkControlReqResult,
       "sleBGPAFNetworkControlMode": sleBGPAFNetworkControlMode,
       "sleBGPAFNetworkControlType": sleBGPAFNetworkControlType,
       "sleBGPAFNetworkControlAddrPrefix": sleBGPAFNetworkControlAddrPrefix,
       "sleBGPAFNetworkControlBackdoor": sleBGPAFNetworkControlBackdoor,
       "sleBGPAFNetworkControlRoutemap": sleBGPAFNetworkControlRoutemap,
       "sleBGPAFNetworkNotification": sleBGPAFNetworkNotification,
       "sleBGPAFNetworkCreated": sleBGPAFNetworkCreated,
       "sleBGPAFNetworkDeleted": sleBGPAFNetworkDeleted,
       "sleBGPStatus": sleBGPStatus,
       "sleBGPStatusPeer": sleBGPStatusPeer,
       "sleBGPStatusPeerV4": sleBGPStatusPeerV4,
       "sleBGPStatusPeerV4Table": sleBGPStatusPeerV4Table,
       "sleBGPStatusPeerV4Entry": sleBGPStatusPeerV4Entry,
       "sleBGPStatusPeerV4Name": sleBGPStatusPeerV4Name,
       "sleBGPStatusPeerV4RemoteAs": sleBGPStatusPeerV4RemoteAs,
       "sleBGPStatusPeerV4LocalAs": sleBGPStatusPeerV4LocalAs,
       "sleBGPStatusPeerV4LinkState": sleBGPStatusPeerV4LinkState,
       "sleBGPStatusPeerV4RouterID": sleBGPStatusPeerV4RouterID,
       "sleBGPStatusPeerV4State": sleBGPStatusPeerV4State,
       "sleBGPStatusPeerV4HoldTime": sleBGPStatusPeerV4HoldTime,
       "sleBGPStatusPeerV4KeepAlive": sleBGPStatusPeerV4KeepAlive,
       "sleBGPStatusPeerV4Uptime": sleBGPStatusPeerV4Uptime,
       "sleBGPStatusPeerV4LastReadTime": sleBGPStatusPeerV4LastReadTime,
       "sleBGPStatusPeerV4RecvMessageCount": sleBGPStatusPeerV4RecvMessageCount,
       "sleBGPStatusPeerV4RecvNotificationCount": sleBGPStatusPeerV4RecvNotificationCount,
       "sleBGPStatusPeerV4SentMessageCount": sleBGPStatusPeerV4SentMessageCount,
       "sleBGPStatusPeerV4SentNotificationCount": sleBGPStatusPeerV4SentNotificationCount,
       "sleBGPStatusPeerV4RouteRefreshRecvRequestCount": sleBGPStatusPeerV4RouteRefreshRecvRequestCount,
       "sleBGPStatusPeerV4RouteRefreshSentRequestCount": sleBGPStatusPeerV4RouteRefreshSentRequestCount,
       "sleBGPStatusPeerV4RouteAdvTime": sleBGPStatusPeerV4RouteAdvTime,
       "sleBGPStatusPeerV4EstablishedCount": sleBGPStatusPeerV4EstablishedCount,
       "sleBGPStatusPeerV4DroppedCount": sleBGPStatusPeerV4DroppedCount,
       "sleBGPStatusPeerV4EBgpMultihopCount": sleBGPStatusPeerV4EBgpMultihopCount,
       "sleBGPStatusPeerV4LocalHost": sleBGPStatusPeerV4LocalHost,
       "sleBGPStatusPeerV4LocalPort": sleBGPStatusPeerV4LocalPort,
       "sleBGPStatusPeerV4ForeignHost": sleBGPStatusPeerV4ForeignHost,
       "sleBGPStatusPeerV4ForeignPort": sleBGPStatusPeerV4ForeignPort,
       "sleBGPStatusPeerV4RemainNextConnTime": sleBGPStatusPeerV4RemainNextConnTime,
       "sleBGPStatusPeerV6": sleBGPStatusPeerV6,
       "sleBGPStatusPeerV6Table": sleBGPStatusPeerV6Table,
       "sleBGPStatusPeerV6Entry": sleBGPStatusPeerV6Entry,
       "sleBGPStatusPeerV6Name": sleBGPStatusPeerV6Name,
       "sleBGPStatusPeerV6RemoteAs": sleBGPStatusPeerV6RemoteAs,
       "sleBGPStatusPeerV6LocalAs": sleBGPStatusPeerV6LocalAs,
       "sleBGPStatusPeerV6LinkState": sleBGPStatusPeerV6LinkState,
       "sleBGPStatusPeerV6RouterID": sleBGPStatusPeerV6RouterID,
       "sleBGPStatusPeerV6State": sleBGPStatusPeerV6State,
       "sleBGPStatusPeerV6HoldTime": sleBGPStatusPeerV6HoldTime,
       "sleBGPStatusPeerV6KeepAlive": sleBGPStatusPeerV6KeepAlive,
       "sleBGPStatusPeerV6Uptime": sleBGPStatusPeerV6Uptime,
       "sleBGPStatusPeerV6LastReadTime": sleBGPStatusPeerV6LastReadTime,
       "sleBGPStatusPeerV6RecvMessageCount": sleBGPStatusPeerV6RecvMessageCount,
       "sleBGPStatusPeerV6RecvNotificationCount": sleBGPStatusPeerV6RecvNotificationCount,
       "sleBGPStatusPeerV6SentMessageCount": sleBGPStatusPeerV6SentMessageCount,
       "sleBGPStatusPeerV6SentNotificationCount": sleBGPStatusPeerV6SentNotificationCount,
       "sleBGPStatusPeerV6RouteRefreshRecvRequestCount": sleBGPStatusPeerV6RouteRefreshRecvRequestCount,
       "sleBGPStatusPeerV6RouteRefreshSentRequestCount": sleBGPStatusPeerV6RouteRefreshSentRequestCount,
       "sleBGPStatusPeerV6RouteAdvTime": sleBGPStatusPeerV6RouteAdvTime,
       "sleBGPStatusPeerV6EstablishedCount": sleBGPStatusPeerV6EstablishedCount,
       "sleBGPStatusPeerV6DroppedCount": sleBGPStatusPeerV6DroppedCount,
       "sleBGPStatusPeerV6EBgpMultihopCount": sleBGPStatusPeerV6EBgpMultihopCount,
       "sleBGPStatusPeerV6LocalHost": sleBGPStatusPeerV6LocalHost,
       "sleBGPStatusPeerV6LocalPort": sleBGPStatusPeerV6LocalPort,
       "sleBGPStatusPeerV6ForeignHost": sleBGPStatusPeerV6ForeignHost,
       "sleBGPStatusPeerV6ForeignPort": sleBGPStatusPeerV6ForeignPort,
       "sleBGPStatusPeerV6RemainNextConnTime": sleBGPStatusPeerV6RemainNextConnTime,
       "sleBGPRoutes": sleBGPRoutes,
       "sleBGPRoutesV4": sleBGPRoutesV4,
       "sleBGPRoutesV4Table": sleBGPRoutesV4Table,
       "sleBGPRoutesV4Entry": sleBGPRoutesV4Entry,
       "sleBGPRoutesV4SAFIType": sleBGPRoutesV4SAFIType,
       "sleBGPRoutesV4RoutePrefix": sleBGPRoutesV4RoutePrefix,
       "sleBGPRoutesV4Nexthop": sleBGPRoutesV4Nexthop,
       "sleBGPRoutesV4NexthopSelected": sleBGPRoutesV4NexthopSelected,
       "sleBGPRoutesV4NexthopInternal": sleBGPRoutesV4NexthopInternal,
       "sleBGPRoutesV4NexthopMed": sleBGPRoutesV4NexthopMed,
       "sleBGPRoutesV4NexthopLocPref": sleBGPRoutesV4NexthopLocPref,
       "sleBGPRoutesV4NexthopWeight": sleBGPRoutesV4NexthopWeight,
       "sleBGPRoutesV4NexthopSuppress": sleBGPRoutesV4NexthopSuppress,
       "sleBGPRoutesV4NexthopValid": sleBGPRoutesV4NexthopValid,
       "sleBGPRoutesV4NexthopStale": sleBGPRoutesV4NexthopStale,
       "sleBGPRoutesV4NexthopDamped": sleBGPRoutesV4NexthopDamped,
       "sleBGPRoutesV4NexthopStaleHistory": sleBGPRoutesV4NexthopStaleHistory,
       "sleBGPRoutesV6": sleBGPRoutesV6,
       "sleBGPRoutesV6Table": sleBGPRoutesV6Table,
       "sleBGPRoutesV6Entry": sleBGPRoutesV6Entry,
       "sleBGPRoutesV6SAFIType": sleBGPRoutesV6SAFIType,
       "sleBGPRoutesV6RoutePrefix": sleBGPRoutesV6RoutePrefix,
       "sleBGPRoutesV6Nexthop": sleBGPRoutesV6Nexthop,
       "sleBGPRoutesV6NexthopSelected": sleBGPRoutesV6NexthopSelected,
       "sleBGPRoutesV6NexthopInternal": sleBGPRoutesV6NexthopInternal,
       "sleBGPRoutesV6NexthopMed": sleBGPRoutesV6NexthopMed,
       "sleBGPRoutesV6NexthopLocPref": sleBGPRoutesV6NexthopLocPref,
       "sleBGPRoutesV6NexthopWeight": sleBGPRoutesV6NexthopWeight,
       "sleBGPRoutesV6NexthopSuppress": sleBGPRoutesV6NexthopSuppress,
       "sleBGPRoutesV6NexthopValid": sleBGPRoutesV6NexthopValid,
       "sleBGPRoutesV6NexthopStale": sleBGPRoutesV6NexthopStale,
       "sleBGPRoutesV6NexthopDamped": sleBGPRoutesV6NexthopDamped,
       "sleBGPRoutesV6NexthopStaleHistory": sleBGPRoutesV6NexthopStaleHistory,
       "sleBGPGroup": sleBGPGroup,
       "sleBGPNotificationGroup": sleBGPNotificationGroup}
)
