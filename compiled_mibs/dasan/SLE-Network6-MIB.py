# SNMP MIB module (SLE-Network6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-Network6-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:54 2025
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

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

(sleIpVRFIndex,) = mibBuilder.importSymbols(
    "SLE-NETWORK-MIB",
    "sleIpVRFIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleNetwork6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26)
)
if mibBuilder.loadTexts:
    sleNetwork6.setRevisions(
        ("2015-01-07 09:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleNetInterface6_ObjectIdentity = ObjectIdentity
sleNetInterface6 = _SleNetInterface6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1)
)
_SleNetIf6Table_Object = MibTable
sleNetIf6Table = _SleNetIf6Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1)
)
if mibBuilder.loadTexts:
    sleNetIf6Table.setStatus("current")
_SleNetIf6Entry_Object = MibTableRow
sleNetIf6Entry = _SleNetIf6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1)
)
sleNetIf6Entry.setIndexNames(
    (0, "SLE-Network6-MIB", "sleNetIf6Index"),
)
if mibBuilder.loadTexts:
    sleNetIf6Entry.setStatus("current")


class _SleNetIf6Index_Type(Integer32):
    """Custom type sleNetIf6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleNetIf6Index_Type.__name__ = "Integer32"
_SleNetIf6Index_Object = MibTableColumn
sleNetIf6Index = _SleNetIf6Index_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 1),
    _SleNetIf6Index_Type()
)
sleNetIf6Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6Index.setStatus("current")
_SleNetIf6Name_Type = OctetString
_SleNetIf6Name_Object = MibTableColumn
sleNetIf6Name = _SleNetIf6Name_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 2),
    _SleNetIf6Name_Type()
)
sleNetIf6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6Name.setStatus("current")


class _SleNetIf6Ipv6State_Type(Integer32):
    """Custom type sleNetIf6Ipv6State based on Integer32"""
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


_SleNetIf6Ipv6State_Type.__name__ = "Integer32"
_SleNetIf6Ipv6State_Object = MibTableColumn
sleNetIf6Ipv6State = _SleNetIf6Ipv6State_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 3),
    _SleNetIf6Ipv6State_Type()
)
sleNetIf6Ipv6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6Ipv6State.setStatus("current")


class _SleNetIf6Mode_Type(Integer32):
    """Custom type sleNetIf6Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )


_SleNetIf6Mode_Type.__name__ = "Integer32"
_SleNetIf6Mode_Object = MibTableColumn
sleNetIf6Mode = _SleNetIf6Mode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 4),
    _SleNetIf6Mode_Type()
)
sleNetIf6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6Mode.setStatus("current")
_SleNetIf6RouteMap_Type = OctetString
_SleNetIf6RouteMap_Object = MibTableColumn
sleNetIf6RouteMap = _SleNetIf6RouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 5),
    _SleNetIf6RouteMap_Type()
)
sleNetIf6RouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6RouteMap.setStatus("current")


class _SleNetIf6AddrAutoConf_Type(Integer32):
    """Custom type sleNetIf6AddrAutoConf based on Integer32"""
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


_SleNetIf6AddrAutoConf_Type.__name__ = "Integer32"
_SleNetIf6AddrAutoConf_Object = MibTableColumn
sleNetIf6AddrAutoConf = _SleNetIf6AddrAutoConf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 6),
    _SleNetIf6AddrAutoConf_Type()
)
sleNetIf6AddrAutoConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6AddrAutoConf.setStatus("current")


class _SleNetIf6AddrAutoConfDefault_Type(Integer32):
    """Custom type sleNetIf6AddrAutoConfDefault based on Integer32"""
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


_SleNetIf6AddrAutoConfDefault_Type.__name__ = "Integer32"
_SleNetIf6AddrAutoConfDefault_Object = MibTableColumn
sleNetIf6AddrAutoConfDefault = _SleNetIf6AddrAutoConfDefault_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 7),
    _SleNetIf6AddrAutoConfDefault_Type()
)
sleNetIf6AddrAutoConfDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6AddrAutoConfDefault.setStatus("current")


class _SleNetIf6NdRouterPref_Type(Integer32):
    """Custom type sleNetIf6NdRouterPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2),
          ("medium", 3))
    )


_SleNetIf6NdRouterPref_Type.__name__ = "Integer32"
_SleNetIf6NdRouterPref_Object = MibTableColumn
sleNetIf6NdRouterPref = _SleNetIf6NdRouterPref_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 8),
    _SleNetIf6NdRouterPref_Type()
)
sleNetIf6NdRouterPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdRouterPref.setStatus("current")


class _SleNetIf6SuppressRA_Type(Integer32):
    """Custom type sleNetIf6SuppressRA based on Integer32"""
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


_SleNetIf6SuppressRA_Type.__name__ = "Integer32"
_SleNetIf6SuppressRA_Object = MibTableColumn
sleNetIf6SuppressRA = _SleNetIf6SuppressRA_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 9),
    _SleNetIf6SuppressRA_Type()
)
sleNetIf6SuppressRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6SuppressRA.setStatus("current")


class _SleNetIf6NdRaMaxInterval_Type(Integer32):
    """Custom type sleNetIf6NdRaMaxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 1800),
    )


_SleNetIf6NdRaMaxInterval_Type.__name__ = "Integer32"
_SleNetIf6NdRaMaxInterval_Object = MibTableColumn
sleNetIf6NdRaMaxInterval = _SleNetIf6NdRaMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 10),
    _SleNetIf6NdRaMaxInterval_Type()
)
sleNetIf6NdRaMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdRaMaxInterval.setStatus("current")


class _SleNetIf6NdRaMinInterval_Type(Integer32):
    """Custom type sleNetIf6NdRaMinInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 1350),
    )


_SleNetIf6NdRaMinInterval_Type.__name__ = "Integer32"
_SleNetIf6NdRaMinInterval_Object = MibTableColumn
sleNetIf6NdRaMinInterval = _SleNetIf6NdRaMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 11),
    _SleNetIf6NdRaMinInterval_Type()
)
sleNetIf6NdRaMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdRaMinInterval.setStatus("current")


class _SleNetIf6NdRaLifeTime_Type(Integer32):
    """Custom type sleNetIf6NdRaLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 9000),
    )


_SleNetIf6NdRaLifeTime_Type.__name__ = "Integer32"
_SleNetIf6NdRaLifeTime_Object = MibTableColumn
sleNetIf6NdRaLifeTime = _SleNetIf6NdRaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 12),
    _SleNetIf6NdRaLifeTime_Type()
)
sleNetIf6NdRaLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdRaLifeTime.setStatus("current")


class _SleNetIf6NdRaReachTime_Type(Integer32):
    """Custom type sleNetIf6NdRaReachTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 3600000),
    )


_SleNetIf6NdRaReachTime_Type.__name__ = "Integer32"
_SleNetIf6NdRaReachTime_Object = MibTableColumn
sleNetIf6NdRaReachTime = _SleNetIf6NdRaReachTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 13),
    _SleNetIf6NdRaReachTime_Type()
)
sleNetIf6NdRaReachTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdRaReachTime.setStatus("current")


class _SleNetIf6NdRaHopLimit_Type(Integer32):
    """Custom type sleNetIf6NdRaHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_SleNetIf6NdRaHopLimit_Type.__name__ = "Integer32"
_SleNetIf6NdRaHopLimit_Object = MibTableColumn
sleNetIf6NdRaHopLimit = _SleNetIf6NdRaHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 14),
    _SleNetIf6NdRaHopLimit_Type()
)
sleNetIf6NdRaHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdRaHopLimit.setStatus("current")


class _SleNetIf6NdRetransTime_Type(Gauge32):
    """Custom type sleNetIf6NdRetransTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleNetIf6NdRetransTime_Type.__name__ = "Gauge32"
_SleNetIf6NdRetransTime_Object = MibTableColumn
sleNetIf6NdRetransTime = _SleNetIf6NdRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 15),
    _SleNetIf6NdRetransTime_Type()
)
sleNetIf6NdRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdRetransTime.setStatus("current")


class _SleNetIf6NdMFlag_Type(Integer32):
    """Custom type sleNetIf6NdMFlag based on Integer32"""
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


_SleNetIf6NdMFlag_Type.__name__ = "Integer32"
_SleNetIf6NdMFlag_Object = MibTableColumn
sleNetIf6NdMFlag = _SleNetIf6NdMFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 16),
    _SleNetIf6NdMFlag_Type()
)
sleNetIf6NdMFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdMFlag.setStatus("current")


class _SleNetIf6NdOFlag_Type(Integer32):
    """Custom type sleNetIf6NdOFlag based on Integer32"""
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


_SleNetIf6NdOFlag_Type.__name__ = "Integer32"
_SleNetIf6NdOFlag_Object = MibTableColumn
sleNetIf6NdOFlag = _SleNetIf6NdOFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 17),
    _SleNetIf6NdOFlag_Type()
)
sleNetIf6NdOFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdOFlag.setStatus("current")


class _SleNetIf6NdProxy_Type(Integer32):
    """Custom type sleNetIf6NdProxy based on Integer32"""
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


_SleNetIf6NdProxy_Type.__name__ = "Integer32"
_SleNetIf6NdProxy_Object = MibTableColumn
sleNetIf6NdProxy = _SleNetIf6NdProxy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 18),
    _SleNetIf6NdProxy_Type()
)
sleNetIf6NdProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdProxy.setStatus("current")


class _SleNetIf6NdDadAttempt_Type(Integer32):
    """Custom type sleNetIf6NdDadAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleNetIf6NdDadAttempt_Type.__name__ = "Integer32"
_SleNetIf6NdDadAttempt_Object = MibTableColumn
sleNetIf6NdDadAttempt = _SleNetIf6NdDadAttempt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 19),
    _SleNetIf6NdDadAttempt_Type()
)
sleNetIf6NdDadAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6NdDadAttempt.setStatus("current")
_SleNetIf6Identifier_Type = OctetString
_SleNetIf6Identifier_Object = MibTableColumn
sleNetIf6Identifier = _SleNetIf6Identifier_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 20),
    _SleNetIf6Identifier_Type()
)
sleNetIf6Identifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIf6Identifier.setStatus("current")


class _SleNetIf6Ip6MartianFilter_Type(Integer32):
    """Custom type sleNetIf6Ip6MartianFilter based on Integer32"""
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


_SleNetIf6Ip6MartianFilter_Type.__name__ = "Integer32"
_SleNetIf6Ip6MartianFilter_Object = MibTableColumn
sleNetIf6Ip6MartianFilter = _SleNetIf6Ip6MartianFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 1, 1, 21),
    _SleNetIf6Ip6MartianFilter_Type()
)
sleNetIf6Ip6MartianFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetIf6Ip6MartianFilter.setStatus("current")
_SleNetIf6Control_ObjectIdentity = ObjectIdentity
sleNetIf6Control = _SleNetIf6Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2)
)


class _SleNetIf6ControlRequest_Type(Integer32):
    """Custom type sleNetIf6ControlRequest based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("setIPv6State", 1),
          ("setMode", 2),
          ("setAddrAutoConf", 3),
          ("setNdProfile", 4),
          ("setRouteMap", 5),
          ("unsetRouteMap", 6),
          ("setIdentifier", 7),
          ("setIp6MartianFilter", 8))
    )


_SleNetIf6ControlRequest_Type.__name__ = "Integer32"
_SleNetIf6ControlRequest_Object = MibScalar
sleNetIf6ControlRequest = _SleNetIf6ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 1),
    _SleNetIf6ControlRequest_Type()
)
sleNetIf6ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlRequest.setStatus("current")
_SleNetIf6ControlStatus_Type = SleControlStatusType
_SleNetIf6ControlStatus_Object = MibScalar
sleNetIf6ControlStatus = _SleNetIf6ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 2),
    _SleNetIf6ControlStatus_Type()
)
sleNetIf6ControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlStatus.setStatus("current")
_SleNetIf6ControlTimer_Type = Gauge32
_SleNetIf6ControlTimer_Object = MibScalar
sleNetIf6ControlTimer = _SleNetIf6ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 3),
    _SleNetIf6ControlTimer_Type()
)
sleNetIf6ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlTimer.setStatus("current")
_SleNetIf6ControlTimeStamp_Type = TimeTicks
_SleNetIf6ControlTimeStamp_Object = MibScalar
sleNetIf6ControlTimeStamp = _SleNetIf6ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 4),
    _SleNetIf6ControlTimeStamp_Type()
)
sleNetIf6ControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlTimeStamp.setStatus("current")
_SleNetIf6ControlReqResult_Type = SleControlRequestResultType
_SleNetIf6ControlReqResult_Object = MibScalar
sleNetIf6ControlReqResult = _SleNetIf6ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 5),
    _SleNetIf6ControlReqResult_Type()
)
sleNetIf6ControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlReqResult.setStatus("current")
_SleNetIf6ControlIndex_Type = Integer32
_SleNetIf6ControlIndex_Object = MibScalar
sleNetIf6ControlIndex = _SleNetIf6ControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 6),
    _SleNetIf6ControlIndex_Type()
)
sleNetIf6ControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlIndex.setStatus("current")


class _SleNetIf6ControlIpv6State_Type(Integer32):
    """Custom type sleNetIf6ControlIpv6State based on Integer32"""
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


_SleNetIf6ControlIpv6State_Type.__name__ = "Integer32"
_SleNetIf6ControlIpv6State_Object = MibScalar
sleNetIf6ControlIpv6State = _SleNetIf6ControlIpv6State_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 7),
    _SleNetIf6ControlIpv6State_Type()
)
sleNetIf6ControlIpv6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlIpv6State.setStatus("current")


class _SleNetIf6ControlMode_Type(Integer32):
    """Custom type sleNetIf6ControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )


_SleNetIf6ControlMode_Type.__name__ = "Integer32"
_SleNetIf6ControlMode_Object = MibScalar
sleNetIf6ControlMode = _SleNetIf6ControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 8),
    _SleNetIf6ControlMode_Type()
)
sleNetIf6ControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlMode.setStatus("current")
_SleNetIf6ControlRouteMap_Type = OctetString
_SleNetIf6ControlRouteMap_Object = MibScalar
sleNetIf6ControlRouteMap = _SleNetIf6ControlRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 9),
    _SleNetIf6ControlRouteMap_Type()
)
sleNetIf6ControlRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlRouteMap.setStatus("current")


class _SleNetIf6ControlAutoConf_Type(Integer32):
    """Custom type sleNetIf6ControlAutoConf based on Integer32"""
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


_SleNetIf6ControlAutoConf_Type.__name__ = "Integer32"
_SleNetIf6ControlAutoConf_Object = MibScalar
sleNetIf6ControlAutoConf = _SleNetIf6ControlAutoConf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 10),
    _SleNetIf6ControlAutoConf_Type()
)
sleNetIf6ControlAutoConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlAutoConf.setStatus("current")


class _SleNetIf6ControlAutoConfDefault_Type(Integer32):
    """Custom type sleNetIf6ControlAutoConfDefault based on Integer32"""
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


_SleNetIf6ControlAutoConfDefault_Type.__name__ = "Integer32"
_SleNetIf6ControlAutoConfDefault_Object = MibScalar
sleNetIf6ControlAutoConfDefault = _SleNetIf6ControlAutoConfDefault_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 11),
    _SleNetIf6ControlAutoConfDefault_Type()
)
sleNetIf6ControlAutoConfDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlAutoConfDefault.setStatus("current")


class _SleNetIf6ControlNdRouterPref_Type(Integer32):
    """Custom type sleNetIf6ControlNdRouterPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("row", 2),
          ("medium", 3))
    )


_SleNetIf6ControlNdRouterPref_Type.__name__ = "Integer32"
_SleNetIf6ControlNdRouterPref_Object = MibScalar
sleNetIf6ControlNdRouterPref = _SleNetIf6ControlNdRouterPref_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 12),
    _SleNetIf6ControlNdRouterPref_Type()
)
sleNetIf6ControlNdRouterPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdRouterPref.setStatus("current")


class _SleNetIf6ControlNdSuppressRA_Type(Integer32):
    """Custom type sleNetIf6ControlNdSuppressRA based on Integer32"""
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


_SleNetIf6ControlNdSuppressRA_Type.__name__ = "Integer32"
_SleNetIf6ControlNdSuppressRA_Object = MibScalar
sleNetIf6ControlNdSuppressRA = _SleNetIf6ControlNdSuppressRA_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 13),
    _SleNetIf6ControlNdSuppressRA_Type()
)
sleNetIf6ControlNdSuppressRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdSuppressRA.setStatus("current")


class _SleNetIf6ControlNdMaxInterval_Type(Integer32):
    """Custom type sleNetIf6ControlNdMaxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 1800),
    )


_SleNetIf6ControlNdMaxInterval_Type.__name__ = "Integer32"
_SleNetIf6ControlNdMaxInterval_Object = MibScalar
sleNetIf6ControlNdMaxInterval = _SleNetIf6ControlNdMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 14),
    _SleNetIf6ControlNdMaxInterval_Type()
)
sleNetIf6ControlNdMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdMaxInterval.setStatus("current")


class _SleNetIf6ControlNdMinInterval_Type(Integer32):
    """Custom type sleNetIf6ControlNdMinInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 1350),
    )


_SleNetIf6ControlNdMinInterval_Type.__name__ = "Integer32"
_SleNetIf6ControlNdMinInterval_Object = MibScalar
sleNetIf6ControlNdMinInterval = _SleNetIf6ControlNdMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 15),
    _SleNetIf6ControlNdMinInterval_Type()
)
sleNetIf6ControlNdMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdMinInterval.setStatus("current")


class _SleNetIf6ControlNdRaLifeTime_Type(Integer32):
    """Custom type sleNetIf6ControlNdRaLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 9000),
    )


_SleNetIf6ControlNdRaLifeTime_Type.__name__ = "Integer32"
_SleNetIf6ControlNdRaLifeTime_Object = MibScalar
sleNetIf6ControlNdRaLifeTime = _SleNetIf6ControlNdRaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 16),
    _SleNetIf6ControlNdRaLifeTime_Type()
)
sleNetIf6ControlNdRaLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdRaLifeTime.setStatus("current")


class _SleNetIf6ControlNdRaReachTime_Type(Integer32):
    """Custom type sleNetIf6ControlNdRaReachTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 3600000),
    )


_SleNetIf6ControlNdRaReachTime_Type.__name__ = "Integer32"
_SleNetIf6ControlNdRaReachTime_Object = MibScalar
sleNetIf6ControlNdRaReachTime = _SleNetIf6ControlNdRaReachTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 17),
    _SleNetIf6ControlNdRaReachTime_Type()
)
sleNetIf6ControlNdRaReachTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdRaReachTime.setStatus("current")


class _SleNetIf6ControlNdRaHopLimit_Type(Integer32):
    """Custom type sleNetIf6ControlNdRaHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_SleNetIf6ControlNdRaHopLimit_Type.__name__ = "Integer32"
_SleNetIf6ControlNdRaHopLimit_Object = MibScalar
sleNetIf6ControlNdRaHopLimit = _SleNetIf6ControlNdRaHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 18),
    _SleNetIf6ControlNdRaHopLimit_Type()
)
sleNetIf6ControlNdRaHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdRaHopLimit.setStatus("current")


class _SleNetIf6ControlNdRetransTime_Type(Gauge32):
    """Custom type sleNetIf6ControlNdRetransTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleNetIf6ControlNdRetransTime_Type.__name__ = "Gauge32"
_SleNetIf6ControlNdRetransTime_Object = MibScalar
sleNetIf6ControlNdRetransTime = _SleNetIf6ControlNdRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 19),
    _SleNetIf6ControlNdRetransTime_Type()
)
sleNetIf6ControlNdRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdRetransTime.setStatus("current")


class _SleNetIf6ControlNdMFlag_Type(Integer32):
    """Custom type sleNetIf6ControlNdMFlag based on Integer32"""
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


_SleNetIf6ControlNdMFlag_Type.__name__ = "Integer32"
_SleNetIf6ControlNdMFlag_Object = MibScalar
sleNetIf6ControlNdMFlag = _SleNetIf6ControlNdMFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 20),
    _SleNetIf6ControlNdMFlag_Type()
)
sleNetIf6ControlNdMFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdMFlag.setStatus("current")


class _SleNetIf6ControlNdOFlag_Type(Integer32):
    """Custom type sleNetIf6ControlNdOFlag based on Integer32"""
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


_SleNetIf6ControlNdOFlag_Type.__name__ = "Integer32"
_SleNetIf6ControlNdOFlag_Object = MibScalar
sleNetIf6ControlNdOFlag = _SleNetIf6ControlNdOFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 21),
    _SleNetIf6ControlNdOFlag_Type()
)
sleNetIf6ControlNdOFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdOFlag.setStatus("current")


class _SleNetIf6ControlNdProxy_Type(Integer32):
    """Custom type sleNetIf6ControlNdProxy based on Integer32"""
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


_SleNetIf6ControlNdProxy_Type.__name__ = "Integer32"
_SleNetIf6ControlNdProxy_Object = MibScalar
sleNetIf6ControlNdProxy = _SleNetIf6ControlNdProxy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 22),
    _SleNetIf6ControlNdProxy_Type()
)
sleNetIf6ControlNdProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdProxy.setStatus("current")


class _SleNetIf6ControlNdDadAttempt_Type(Integer32):
    """Custom type sleNetIf6ControlNdDadAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SleNetIf6ControlNdDadAttempt_Type.__name__ = "Integer32"
_SleNetIf6ControlNdDadAttempt_Object = MibScalar
sleNetIf6ControlNdDadAttempt = _SleNetIf6ControlNdDadAttempt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 23),
    _SleNetIf6ControlNdDadAttempt_Type()
)
sleNetIf6ControlNdDadAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlNdDadAttempt.setStatus("current")
_SleNetIf6ControlIdentifier_Type = OctetString
_SleNetIf6ControlIdentifier_Object = MibScalar
sleNetIf6ControlIdentifier = _SleNetIf6ControlIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 24),
    _SleNetIf6ControlIdentifier_Type()
)
sleNetIf6ControlIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlIdentifier.setStatus("current")


class _SleNetIf6ControlIp6MartianFilter_Type(Integer32):
    """Custom type sleNetIf6ControlIp6MartianFilter based on Integer32"""
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


_SleNetIf6ControlIp6MartianFilter_Type.__name__ = "Integer32"
_SleNetIf6ControlIp6MartianFilter_Object = MibScalar
sleNetIf6ControlIp6MartianFilter = _SleNetIf6ControlIp6MartianFilter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 2, 25),
    _SleNetIf6ControlIp6MartianFilter_Type()
)
sleNetIf6ControlIp6MartianFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetIf6ControlIp6MartianFilter.setStatus("current")
_SleNetIf6Notification_ObjectIdentity = ObjectIdentity
sleNetIf6Notification = _SleNetIf6Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3)
)
_SleIpAddress6_ObjectIdentity = ObjectIdentity
sleIpAddress6 = _SleIpAddress6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2)
)
_SleIpAddr6Table_Object = MibTable
sleIpAddr6Table = _SleIpAddr6Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1)
)
if mibBuilder.loadTexts:
    sleIpAddr6Table.setStatus("current")
_SleIpAddr6Entry_Object = MibTableRow
sleIpAddr6Entry = _SleIpAddr6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1)
)
sleIpAddr6Entry.setIndexNames(
    (0, "SLE-Network6-MIB", "sleNetIf6Index"),
    (0, "SLE-Network6-MIB", "sleIpAddr6Value"),
)
if mibBuilder.loadTexts:
    sleIpAddr6Entry.setStatus("current")
_SleIpAddr6Value_Type = InetAddressIPv6
_SleIpAddr6Value_Object = MibTableColumn
sleIpAddr6Value = _SleIpAddr6Value_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1, 1),
    _SleIpAddr6Value_Type()
)
sleIpAddr6Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6Value.setStatus("current")
_SleIpAddr6Mask_Type = InetAddressPrefixLength
_SleIpAddr6Mask_Object = MibTableColumn
sleIpAddr6Mask = _SleIpAddr6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1, 2),
    _SleIpAddr6Mask_Type()
)
sleIpAddr6Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6Mask.setStatus("current")


class _SleIpAddr6Score_Type(Integer32):
    """Custom type sleIpAddr6Score based on Integer32"""
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
        *(("linklocal", 1),
          ("global", 2),
          ("anycast", 3),
          ("host", 4))
    )


_SleIpAddr6Score_Type.__name__ = "Integer32"
_SleIpAddr6Score_Object = MibTableColumn
sleIpAddr6Score = _SleIpAddr6Score_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1, 3),
    _SleIpAddr6Score_Type()
)
sleIpAddr6Score.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6Score.setStatus("current")


class _SleIpAddr6Type_Type(Integer32):
    """Custom type sleIpAddr6Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_SleIpAddr6Type_Type.__name__ = "Integer32"
_SleIpAddr6Type_Object = MibTableColumn
sleIpAddr6Type = _SleIpAddr6Type_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1, 4),
    _SleIpAddr6Type_Type()
)
sleIpAddr6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6Type.setStatus("current")


class _SleIpAddr6Status_Type(Integer32):
    """Custom type sleIpAddr6Status based on Integer32"""
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
        *(("active", 1),
          ("dadfailed", 2),
          ("tentative", 3),
          ("deprecated", 4))
    )


_SleIpAddr6Status_Type.__name__ = "Integer32"
_SleIpAddr6Status_Object = MibTableColumn
sleIpAddr6Status = _SleIpAddr6Status_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1, 5),
    _SleIpAddr6Status_Type()
)
sleIpAddr6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6Status.setStatus("current")
_SleIpAddr6ValidTime_Type = Integer32
_SleIpAddr6ValidTime_Object = MibTableColumn
sleIpAddr6ValidTime = _SleIpAddr6ValidTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1, 6),
    _SleIpAddr6ValidTime_Type()
)
sleIpAddr6ValidTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6ValidTime.setStatus("current")
_SleIpAddr6UsedTime_Type = Integer32
_SleIpAddr6UsedTime_Object = MibTableColumn
sleIpAddr6UsedTime = _SleIpAddr6UsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 1, 1, 7),
    _SleIpAddr6UsedTime_Type()
)
sleIpAddr6UsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6UsedTime.setStatus("current")
_SleIpAddr6Control_ObjectIdentity = ObjectIdentity
sleIpAddr6Control = _SleIpAddr6Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2)
)


class _SleIpAddr6ControlRequest_Type(Integer32):
    """Custom type sleIpAddr6ControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createIP6Addr", 1),
          ("deleteIP6Addr", 2),
          ("deleteIP6AddrAll", 3))
    )


_SleIpAddr6ControlRequest_Type.__name__ = "Integer32"
_SleIpAddr6ControlRequest_Object = MibScalar
sleIpAddr6ControlRequest = _SleIpAddr6ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 1),
    _SleIpAddr6ControlRequest_Type()
)
sleIpAddr6ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddr6ControlRequest.setStatus("current")
_SleIpAddr6ControlStatus_Type = SleControlStatusType
_SleIpAddr6ControlStatus_Object = MibScalar
sleIpAddr6ControlStatus = _SleIpAddr6ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 2),
    _SleIpAddr6ControlStatus_Type()
)
sleIpAddr6ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6ControlStatus.setStatus("current")
_SleIpAddr6ControlTimer_Type = Gauge32
_SleIpAddr6ControlTimer_Object = MibScalar
sleIpAddr6ControlTimer = _SleIpAddr6ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 3),
    _SleIpAddr6ControlTimer_Type()
)
sleIpAddr6ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpAddr6ControlTimer.setStatus("current")
_SleIpAddr6ControlTimeStamp_Type = TimeTicks
_SleIpAddr6ControlTimeStamp_Object = MibScalar
sleIpAddr6ControlTimeStamp = _SleIpAddr6ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 4),
    _SleIpAddr6ControlTimeStamp_Type()
)
sleIpAddr6ControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6ControlTimeStamp.setStatus("current")
_SleIpAddr6ControlReqResult_Type = SleControlRequestResultType
_SleIpAddr6ControlReqResult_Object = MibScalar
sleIpAddr6ControlReqResult = _SleIpAddr6ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 5),
    _SleIpAddr6ControlReqResult_Type()
)
sleIpAddr6ControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIpAddr6ControlReqResult.setStatus("current")


class _SleIPAddr6ControlIfIndex_Type(Integer32):
    """Custom type sleIPAddr6ControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleIPAddr6ControlIfIndex_Type.__name__ = "Integer32"
_SleIPAddr6ControlIfIndex_Object = MibScalar
sleIPAddr6ControlIfIndex = _SleIPAddr6ControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 6),
    _SleIPAddr6ControlIfIndex_Type()
)
sleIPAddr6ControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlIfIndex.setStatus("current")
_SleIPAddr6ControlValue_Type = InetAddressIPv6
_SleIPAddr6ControlValue_Object = MibScalar
sleIPAddr6ControlValue = _SleIPAddr6ControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 7),
    _SleIPAddr6ControlValue_Type()
)
sleIPAddr6ControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlValue.setStatus("current")
_SleIPAddr6ControlMask_Type = InetAddressPrefixLength
_SleIPAddr6ControlMask_Object = MibScalar
sleIPAddr6ControlMask = _SleIPAddr6ControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 8),
    _SleIPAddr6ControlMask_Type()
)
sleIPAddr6ControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlMask.setStatus("current")


class _SleIPAddr6ControlScore_Type(Integer32):
    """Custom type sleIPAddr6ControlScore based on Integer32"""
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
        *(("linklocal", 1),
          ("global", 2),
          ("anycast", 3),
          ("host", 4))
    )


_SleIPAddr6ControlScore_Type.__name__ = "Integer32"
_SleIPAddr6ControlScore_Object = MibScalar
sleIPAddr6ControlScore = _SleIPAddr6ControlScore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 9),
    _SleIPAddr6ControlScore_Type()
)
sleIPAddr6ControlScore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlScore.setStatus("current")


class _SleIPAddr6ControlType_Type(Integer32):
    """Custom type sleIPAddr6ControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_SleIPAddr6ControlType_Type.__name__ = "Integer32"
_SleIPAddr6ControlType_Object = MibScalar
sleIPAddr6ControlType = _SleIPAddr6ControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 10),
    _SleIPAddr6ControlType_Type()
)
sleIPAddr6ControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlType.setStatus("current")


class _SleIPAddr6ControlStatus_Type(Integer32):
    """Custom type sleIPAddr6ControlStatus based on Integer32"""
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
        *(("active", 1),
          ("dadfailed", 2),
          ("tentative", 3),
          ("deprecated", 4))
    )


_SleIPAddr6ControlStatus_Type.__name__ = "Integer32"
_SleIPAddr6ControlStatus_Object = MibScalar
sleIPAddr6ControlStatus = _SleIPAddr6ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 11),
    _SleIPAddr6ControlStatus_Type()
)
sleIPAddr6ControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlStatus.setStatus("current")


class _SleIPAddr6ControlValidTime_Type(Integer32):
    """Custom type sleIPAddr6ControlValidTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535000),
    )


_SleIPAddr6ControlValidTime_Type.__name__ = "Integer32"
_SleIPAddr6ControlValidTime_Object = MibScalar
sleIPAddr6ControlValidTime = _SleIPAddr6ControlValidTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 12),
    _SleIPAddr6ControlValidTime_Type()
)
sleIPAddr6ControlValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlValidTime.setStatus("current")


class _SleIPAddr6ControlUsedTime_Type(Integer32):
    """Custom type sleIPAddr6ControlUsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535000),
    )


_SleIPAddr6ControlUsedTime_Type.__name__ = "Integer32"
_SleIPAddr6ControlUsedTime_Object = MibScalar
sleIPAddr6ControlUsedTime = _SleIPAddr6ControlUsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 2, 13),
    _SleIPAddr6ControlUsedTime_Type()
)
sleIPAddr6ControlUsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIPAddr6ControlUsedTime.setStatus("current")
_SleIpAddr6Notification_ObjectIdentity = ObjectIdentity
sleIpAddr6Notification = _SleIpAddr6Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 3)
)
_SleNdPrefix_ObjectIdentity = ObjectIdentity
sleNdPrefix = _SleNdPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3)
)
_SleNdPrefixTable_Object = MibTable
sleNdPrefixTable = _SleNdPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1)
)
if mibBuilder.loadTexts:
    sleNdPrefixTable.setStatus("current")
_SleNdPrefixEntry_Object = MibTableRow
sleNdPrefixEntry = _SleNdPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1)
)
sleNdPrefixEntry.setIndexNames(
    (0, "SLE-Network6-MIB", "sleNetIf6Index"),
    (0, "SLE-Network6-MIB", "sleNdPrefixDefault"),
    (0, "SLE-Network6-MIB", "sleNdPrefixValue"),
    (0, "SLE-Network6-MIB", "sleNdPrefixMask"),
)
if mibBuilder.loadTexts:
    sleNdPrefixEntry.setStatus("current")


class _SleNdPrefixDefault_Type(Integer32):
    """Custom type sleNdPrefixDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SleNdPrefixDefault_Type.__name__ = "Integer32"
_SleNdPrefixDefault_Object = MibTableColumn
sleNdPrefixDefault = _SleNdPrefixDefault_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1, 1),
    _SleNdPrefixDefault_Type()
)
sleNdPrefixDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixDefault.setStatus("current")
_SleNdPrefixValue_Type = InetAddressIPv6
_SleNdPrefixValue_Object = MibTableColumn
sleNdPrefixValue = _SleNdPrefixValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1, 2),
    _SleNdPrefixValue_Type()
)
sleNdPrefixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixValue.setStatus("current")


class _SleNdPrefixMask_Type(InetAddressPrefixLength):
    """Custom type sleNdPrefixMask based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleNdPrefixMask_Type.__name__ = "InetAddressPrefixLength"
_SleNdPrefixMask_Object = MibTableColumn
sleNdPrefixMask = _SleNdPrefixMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1, 3),
    _SleNdPrefixMask_Type()
)
sleNdPrefixMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixMask.setStatus("current")


class _SleNdPrefixValTime_Type(Gauge32):
    """Custom type sleNdPrefixValTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleNdPrefixValTime_Type.__name__ = "Gauge32"
_SleNdPrefixValTime_Object = MibTableColumn
sleNdPrefixValTime = _SleNdPrefixValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1, 4),
    _SleNdPrefixValTime_Type()
)
sleNdPrefixValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixValTime.setStatus("current")


class _SleNdPrefixPreTime_Type(Gauge32):
    """Custom type sleNdPrefixPreTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleNdPrefixPreTime_Type.__name__ = "Gauge32"
_SleNdPrefixPreTime_Object = MibTableColumn
sleNdPrefixPreTime = _SleNdPrefixPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1, 5),
    _SleNdPrefixPreTime_Type()
)
sleNdPrefixPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixPreTime.setStatus("current")


class _SleNdPrefixOffLink_Type(Integer32):
    """Custom type sleNdPrefixOffLink based on Integer32"""
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


_SleNdPrefixOffLink_Type.__name__ = "Integer32"
_SleNdPrefixOffLink_Object = MibTableColumn
sleNdPrefixOffLink = _SleNdPrefixOffLink_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1, 6),
    _SleNdPrefixOffLink_Type()
)
sleNdPrefixOffLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixOffLink.setStatus("current")


class _SleNdPrefixNoAutoconfig_Type(Integer32):
    """Custom type sleNdPrefixNoAutoconfig based on Integer32"""
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


_SleNdPrefixNoAutoconfig_Type.__name__ = "Integer32"
_SleNdPrefixNoAutoconfig_Object = MibTableColumn
sleNdPrefixNoAutoconfig = _SleNdPrefixNoAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 1, 1, 7),
    _SleNdPrefixNoAutoconfig_Type()
)
sleNdPrefixNoAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixNoAutoconfig.setStatus("current")
_SleNdPrefixControl_ObjectIdentity = ObjectIdentity
sleNdPrefixControl = _SleNdPrefixControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2)
)


class _SleNdPrefixControlRequest_Type(Integer32):
    """Custom type sleNdPrefixControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createNdPrefix", 1),
          ("deleteNdPrefix", 2))
    )


_SleNdPrefixControlRequest_Type.__name__ = "Integer32"
_SleNdPrefixControlRequest_Object = MibScalar
sleNdPrefixControlRequest = _SleNdPrefixControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 1),
    _SleNdPrefixControlRequest_Type()
)
sleNdPrefixControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlRequest.setStatus("current")
_SleNdPrefixControlStatus_Type = SleControlStatusType
_SleNdPrefixControlStatus_Object = MibScalar
sleNdPrefixControlStatus = _SleNdPrefixControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 2),
    _SleNdPrefixControlStatus_Type()
)
sleNdPrefixControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlStatus.setStatus("current")
_SleNdPrefixControlTimer_Type = Gauge32
_SleNdPrefixControlTimer_Object = MibScalar
sleNdPrefixControlTimer = _SleNdPrefixControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 3),
    _SleNdPrefixControlTimer_Type()
)
sleNdPrefixControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlTimer.setStatus("current")
_SleNdPrefixControlTimeStamp_Type = TimeTicks
_SleNdPrefixControlTimeStamp_Object = MibScalar
sleNdPrefixControlTimeStamp = _SleNdPrefixControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 4),
    _SleNdPrefixControlTimeStamp_Type()
)
sleNdPrefixControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlTimeStamp.setStatus("current")
_SleNdPrefixControlReqResult_Type = SleControlRequestResultType
_SleNdPrefixControlReqResult_Object = MibScalar
sleNdPrefixControlReqResult = _SleNdPrefixControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 5),
    _SleNdPrefixControlReqResult_Type()
)
sleNdPrefixControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlReqResult.setStatus("current")


class _SleNdPrefixControlIfIndex_Type(Integer32):
    """Custom type sleNdPrefixControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleNdPrefixControlIfIndex_Type.__name__ = "Integer32"
_SleNdPrefixControlIfIndex_Object = MibScalar
sleNdPrefixControlIfIndex = _SleNdPrefixControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 6),
    _SleNdPrefixControlIfIndex_Type()
)
sleNdPrefixControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlIfIndex.setStatus("current")


class _SleNdPrefixControlDefault_Type(Integer32):
    """Custom type sleNdPrefixControlDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SleNdPrefixControlDefault_Type.__name__ = "Integer32"
_SleNdPrefixControlDefault_Object = MibScalar
sleNdPrefixControlDefault = _SleNdPrefixControlDefault_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 7),
    _SleNdPrefixControlDefault_Type()
)
sleNdPrefixControlDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlDefault.setStatus("current")
_SleNdPrefixControlValue_Type = InetAddressIPv6
_SleNdPrefixControlValue_Object = MibScalar
sleNdPrefixControlValue = _SleNdPrefixControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 8),
    _SleNdPrefixControlValue_Type()
)
sleNdPrefixControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlValue.setStatus("current")
_SleNdPrefixControlMask_Type = InetAddressPrefixLength
_SleNdPrefixControlMask_Object = MibScalar
sleNdPrefixControlMask = _SleNdPrefixControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 9),
    _SleNdPrefixControlMask_Type()
)
sleNdPrefixControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlMask.setStatus("current")


class _SleNdPrefixControlValTime_Type(Gauge32):
    """Custom type sleNdPrefixControlValTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleNdPrefixControlValTime_Type.__name__ = "Gauge32"
_SleNdPrefixControlValTime_Object = MibScalar
sleNdPrefixControlValTime = _SleNdPrefixControlValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 10),
    _SleNdPrefixControlValTime_Type()
)
sleNdPrefixControlValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlValTime.setStatus("current")


class _SleNdPrefixControlPreTime_Type(Gauge32):
    """Custom type sleNdPrefixControlPreTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleNdPrefixControlPreTime_Type.__name__ = "Gauge32"
_SleNdPrefixControlPreTime_Object = MibScalar
sleNdPrefixControlPreTime = _SleNdPrefixControlPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 11),
    _SleNdPrefixControlPreTime_Type()
)
sleNdPrefixControlPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlPreTime.setStatus("current")


class _SleNdPrefixControlOffLink_Type(Integer32):
    """Custom type sleNdPrefixControlOffLink based on Integer32"""
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


_SleNdPrefixControlOffLink_Type.__name__ = "Integer32"
_SleNdPrefixControlOffLink_Object = MibScalar
sleNdPrefixControlOffLink = _SleNdPrefixControlOffLink_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 12),
    _SleNdPrefixControlOffLink_Type()
)
sleNdPrefixControlOffLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlOffLink.setStatus("current")


class _SleNdPrefixControlNoAutoconfig_Type(Integer32):
    """Custom type sleNdPrefixControlNoAutoconfig based on Integer32"""
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


_SleNdPrefixControlNoAutoconfig_Type.__name__ = "Integer32"
_SleNdPrefixControlNoAutoconfig_Object = MibScalar
sleNdPrefixControlNoAutoconfig = _SleNdPrefixControlNoAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 2, 13),
    _SleNdPrefixControlNoAutoconfig_Type()
)
sleNdPrefixControlNoAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNdPrefixControlNoAutoconfig.setStatus("current")
_SleNdPrefixNotification_ObjectIdentity = ObjectIdentity
sleNdPrefixNotification = _SleNdPrefixNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 3)
)
_SleNeighbour6_ObjectIdentity = ObjectIdentity
sleNeighbour6 = _SleNeighbour6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4)
)
_SleNeighbour6Table_Object = MibTable
sleNeighbour6Table = _SleNeighbour6Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1)
)
if mibBuilder.loadTexts:
    sleNeighbour6Table.setStatus("current")
_SleNeighbour6Entry_Object = MibTableRow
sleNeighbour6Entry = _SleNeighbour6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1, 1)
)
sleNeighbour6Entry.setIndexNames(
    (0, "SLE-Network6-MIB", "sleNetIf6Index"),
    (0, "SLE-Network6-MIB", "sleNeighbour6Address"),
)
if mibBuilder.loadTexts:
    sleNeighbour6Entry.setStatus("current")
_SleNeighbour6Address_Type = InetAddressIPv6
_SleNeighbour6Address_Object = MibTableColumn
sleNeighbour6Address = _SleNeighbour6Address_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1, 1, 1),
    _SleNeighbour6Address_Type()
)
sleNeighbour6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6Address.setStatus("current")
_SleNeighbour6PhyAddress_Type = OctetString
_SleNeighbour6PhyAddress_Object = MibTableColumn
sleNeighbour6PhyAddress = _SleNeighbour6PhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1, 1, 2),
    _SleNeighbour6PhyAddress_Type()
)
sleNeighbour6PhyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6PhyAddress.setStatus("current")


class _SleNeighbour6PortIndex_Type(Integer32):
    """Custom type sleNeighbour6PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleNeighbour6PortIndex_Type.__name__ = "Integer32"
_SleNeighbour6PortIndex_Object = MibTableColumn
sleNeighbour6PortIndex = _SleNeighbour6PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1, 1, 3),
    _SleNeighbour6PortIndex_Type()
)
sleNeighbour6PortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6PortIndex.setStatus("current")


class _SleNeighbour6State_Type(Integer32):
    """Custom type sleNeighbour6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_SleNeighbour6State_Type.__name__ = "Integer32"
_SleNeighbour6State_Object = MibTableColumn
sleNeighbour6State = _SleNeighbour6State_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1, 1, 4),
    _SleNeighbour6State_Type()
)
sleNeighbour6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6State.setStatus("current")


class _SleNeighbour6HwType_Type(Integer32):
    """Custom type sleNeighbour6HwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethernet", 1)
    )


_SleNeighbour6HwType_Type.__name__ = "Integer32"
_SleNeighbour6HwType_Object = MibTableColumn
sleNeighbour6HwType = _SleNeighbour6HwType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1, 1, 5),
    _SleNeighbour6HwType_Type()
)
sleNeighbour6HwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6HwType.setStatus("current")


class _SleNeighbour6HwUsed_Type(Integer32):
    """Custom type sleNeighbour6HwUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonused", 0),
          ("used", 1))
    )


_SleNeighbour6HwUsed_Type.__name__ = "Integer32"
_SleNeighbour6HwUsed_Object = MibTableColumn
sleNeighbour6HwUsed = _SleNeighbour6HwUsed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 1, 1, 6),
    _SleNeighbour6HwUsed_Type()
)
sleNeighbour6HwUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6HwUsed.setStatus("current")
_SleNeighbour6Control_ObjectIdentity = ObjectIdentity
sleNeighbour6Control = _SleNeighbour6Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2)
)


class _SleNeighbour6ControlRequest_Type(Integer32):
    """Custom type sleNeighbour6ControlRequest based on Integer32"""
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
        *(("createNeighbour6", 1),
          ("deleteNeighbour6", 2),
          ("clearNeighbour6", 3),
          ("clearNeighbour6ByAddr", 4))
    )


_SleNeighbour6ControlRequest_Type.__name__ = "Integer32"
_SleNeighbour6ControlRequest_Object = MibScalar
sleNeighbour6ControlRequest = _SleNeighbour6ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 1),
    _SleNeighbour6ControlRequest_Type()
)
sleNeighbour6ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlRequest.setStatus("current")
_SleNeighbour6ControlStatus_Type = SleControlStatusType
_SleNeighbour6ControlStatus_Object = MibScalar
sleNeighbour6ControlStatus = _SleNeighbour6ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 2),
    _SleNeighbour6ControlStatus_Type()
)
sleNeighbour6ControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlStatus.setStatus("current")
_SleNeighbour6ControlTimer_Type = Gauge32
_SleNeighbour6ControlTimer_Object = MibScalar
sleNeighbour6ControlTimer = _SleNeighbour6ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 3),
    _SleNeighbour6ControlTimer_Type()
)
sleNeighbour6ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlTimer.setStatus("current")
_SleNeighbour6ControlTimeStamp_Type = TimeTicks
_SleNeighbour6ControlTimeStamp_Object = MibScalar
sleNeighbour6ControlTimeStamp = _SleNeighbour6ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 4),
    _SleNeighbour6ControlTimeStamp_Type()
)
sleNeighbour6ControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlTimeStamp.setStatus("current")
_SleNeighbour6ControlReqResult_Type = SleControlRequestResultType
_SleNeighbour6ControlReqResult_Object = MibScalar
sleNeighbour6ControlReqResult = _SleNeighbour6ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 5),
    _SleNeighbour6ControlReqResult_Type()
)
sleNeighbour6ControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlReqResult.setStatus("current")


class _SleNeighbour6ControlIfIndex_Type(Integer32):
    """Custom type sleNeighbour6ControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleNeighbour6ControlIfIndex_Type.__name__ = "Integer32"
_SleNeighbour6ControlIfIndex_Object = MibScalar
sleNeighbour6ControlIfIndex = _SleNeighbour6ControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 6),
    _SleNeighbour6ControlIfIndex_Type()
)
sleNeighbour6ControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlIfIndex.setStatus("current")
_SleNeighbour6ControlAddress_Type = InetAddressIPv6
_SleNeighbour6ControlAddress_Object = MibScalar
sleNeighbour6ControlAddress = _SleNeighbour6ControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 7),
    _SleNeighbour6ControlAddress_Type()
)
sleNeighbour6ControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlAddress.setStatus("current")
_SleNeighbour6ControlPhyAddress_Type = OctetString
_SleNeighbour6ControlPhyAddress_Object = MibScalar
sleNeighbour6ControlPhyAddress = _SleNeighbour6ControlPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 8),
    _SleNeighbour6ControlPhyAddress_Type()
)
sleNeighbour6ControlPhyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlPhyAddress.setStatus("current")


class _SleNeighbour6ControlMask_Type(Integer32):
    """Custom type sleNeighbour6ControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleNeighbour6ControlMask_Type.__name__ = "Integer32"
_SleNeighbour6ControlMask_Object = MibScalar
sleNeighbour6ControlMask = _SleNeighbour6ControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 2, 9),
    _SleNeighbour6ControlMask_Type()
)
sleNeighbour6ControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNeighbour6ControlMask.setStatus("current")
_SleNeighbour6Notification_ObjectIdentity = ObjectIdentity
sleNeighbour6Notification = _SleNeighbour6Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 3)
)
_SleRoute6_ObjectIdentity = ObjectIdentity
sleRoute6 = _SleRoute6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5)
)
_SleRoute6Table_Object = MibTable
sleRoute6Table = _SleRoute6Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1)
)
if mibBuilder.loadTexts:
    sleRoute6Table.setStatus("current")
_SleRoute6Entry_Object = MibTableRow
sleRoute6Entry = _SleRoute6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1)
)
sleRoute6Entry.setIndexNames(
    (0, "SLE-NETWORK-MIB", "sleIpVRFIndex"),
    (0, "SLE-Network6-MIB", "sleRoute6DstAddress"),
    (0, "SLE-Network6-MIB", "sleRoute6DstMask"),
    (0, "SLE-Network6-MIB", "sleRoute6Gateway"),
    (0, "SLE-Network6-MIB", "sleRoute6Proto"),
    (0, "SLE-Network6-MIB", "sleNetIf6Index"),
)
if mibBuilder.loadTexts:
    sleRoute6Entry.setStatus("current")
_SleRoute6DstAddress_Type = InetAddressIPv6
_SleRoute6DstAddress_Object = MibTableColumn
sleRoute6DstAddress = _SleRoute6DstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 1),
    _SleRoute6DstAddress_Type()
)
sleRoute6DstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6DstAddress.setStatus("current")


class _SleRoute6DstMask_Type(InetAddressPrefixLength):
    """Custom type sleRoute6DstMask based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRoute6DstMask_Type.__name__ = "InetAddressPrefixLength"
_SleRoute6DstMask_Object = MibTableColumn
sleRoute6DstMask = _SleRoute6DstMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 2),
    _SleRoute6DstMask_Type()
)
sleRoute6DstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6DstMask.setStatus("current")


class _SleRoute6Proto_Type(Integer32):
    """Custom type sleRoute6Proto based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isis", 9),
          ("esis", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16),
          ("dhcp", 17))
    )


_SleRoute6Proto_Type.__name__ = "Integer32"
_SleRoute6Proto_Object = MibTableColumn
sleRoute6Proto = _SleRoute6Proto_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 3),
    _SleRoute6Proto_Type()
)
sleRoute6Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6Proto.setStatus("current")
_SleRoute6Gateway_Type = InetAddressIPv6
_SleRoute6Gateway_Object = MibTableColumn
sleRoute6Gateway = _SleRoute6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 4),
    _SleRoute6Gateway_Type()
)
sleRoute6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6Gateway.setStatus("current")


class _SleRoute6Type_Type(Integer32):
    """Custom type sleRoute6Type based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("direct", 3),
          ("indirect", 4))
    )


_SleRoute6Type_Type.__name__ = "Integer32"
_SleRoute6Type_Object = MibTableColumn
sleRoute6Type = _SleRoute6Type_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 5),
    _SleRoute6Type_Type()
)
sleRoute6Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6Type.setStatus("current")


class _SleRoute6Subtype_Type(Integer32):
    """Custom type sleRoute6Subtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ospfIa", 1),
          ("ospfNssa1", 2),
          ("ospfNssa2", 3),
          ("ospfExternal1", 4),
          ("ospfExternal2", 5),
          ("isisL1", 8),
          ("isisL2", 9),
          ("isisIa", 10),
          ("bgpMpls", 11))
    )


_SleRoute6Subtype_Type.__name__ = "Integer32"
_SleRoute6Subtype_Object = MibTableColumn
sleRoute6Subtype = _SleRoute6Subtype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 6),
    _SleRoute6Subtype_Type()
)
sleRoute6Subtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6Subtype.setStatus("current")


class _SleRoute6Distance_Type(Integer32):
    """Custom type sleRoute6Distance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRoute6Distance_Type.__name__ = "Integer32"
_SleRoute6Distance_Object = MibTableColumn
sleRoute6Distance = _SleRoute6Distance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 7),
    _SleRoute6Distance_Type()
)
sleRoute6Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6Distance.setStatus("current")


class _SleRoute6Metric_Type(Integer32):
    """Custom type sleRoute6Metric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRoute6Metric_Type.__name__ = "Integer32"
_SleRoute6Metric_Object = MibTableColumn
sleRoute6Metric = _SleRoute6Metric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 8),
    _SleRoute6Metric_Type()
)
sleRoute6Metric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6Metric.setStatus("current")


class _SleRoute6Active_Type(Integer32):
    """Custom type sleRoute6Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SleRoute6Active_Type.__name__ = "Integer32"
_SleRoute6Active_Object = MibTableColumn
sleRoute6Active = _SleRoute6Active_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 9),
    _SleRoute6Active_Type()
)
sleRoute6Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6Active.setStatus("current")


class _SleRoute6NexthopStatus_Type(Bits):
    """Custom type sleRoute6NexthopStatus based on Bits"""
    namedValues = NamedValues(
        *(("active", 0),
          ("fib", 1),
          ("recursive", 2))
    )

_SleRoute6NexthopStatus_Type.__name__ = "Bits"
_SleRoute6NexthopStatus_Object = MibTableColumn
sleRoute6NexthopStatus = _SleRoute6NexthopStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 10),
    _SleRoute6NexthopStatus_Type()
)
sleRoute6NexthopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6NexthopStatus.setStatus("current")


class _SleRoute6RibStatus_Type(Bits):
    """Custom type sleRoute6RibStatus based on Bits"""
    namedValues = NamedValues(
        *(("internal", 0),
          ("selfroute", 1),
          ("blackhole", 2),
          ("nonfib", 3),
          ("selected", 4),
          ("changed", 5),
          ("static", 6),
          ("stale", 7))
    )

_SleRoute6RibStatus_Type.__name__ = "Bits"
_SleRoute6RibStatus_Object = MibTableColumn
sleRoute6RibStatus = _SleRoute6RibStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 11),
    _SleRoute6RibStatus_Type()
)
sleRoute6RibStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6RibStatus.setStatus("current")


class _SleRoute6BfdState_Type(Integer32):
    """Custom type sleRoute6BfdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SleRoute6BfdState_Type.__name__ = "Integer32"
_SleRoute6BfdState_Object = MibTableColumn
sleRoute6BfdState = _SleRoute6BfdState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 1, 1, 12),
    _SleRoute6BfdState_Type()
)
sleRoute6BfdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6BfdState.setStatus("current")
_SleRoute6Control_ObjectIdentity = ObjectIdentity
sleRoute6Control = _SleRoute6Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2)
)


class _SleRoute6ControlRequest_Type(Integer32):
    """Custom type sleRoute6ControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createStaticRoute6", 1),
          ("deleteStaticRoute6", 2))
    )


_SleRoute6ControlRequest_Type.__name__ = "Integer32"
_SleRoute6ControlRequest_Object = MibScalar
sleRoute6ControlRequest = _SleRoute6ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 1),
    _SleRoute6ControlRequest_Type()
)
sleRoute6ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlRequest.setStatus("current")
_SleRoute6ControlStatus_Type = SleControlStatusType
_SleRoute6ControlStatus_Object = MibScalar
sleRoute6ControlStatus = _SleRoute6ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 2),
    _SleRoute6ControlStatus_Type()
)
sleRoute6ControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlStatus.setStatus("current")
_SleRoute6ControlTimer_Type = Gauge32
_SleRoute6ControlTimer_Object = MibScalar
sleRoute6ControlTimer = _SleRoute6ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 3),
    _SleRoute6ControlTimer_Type()
)
sleRoute6ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlTimer.setStatus("current")
_SleRoute6ControlTimeStamp_Type = TimeTicks
_SleRoute6ControlTimeStamp_Object = MibScalar
sleRoute6ControlTimeStamp = _SleRoute6ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 4),
    _SleRoute6ControlTimeStamp_Type()
)
sleRoute6ControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlTimeStamp.setStatus("current")
_SleRoute6ControlReqResult_Type = SleControlRequestResultType
_SleRoute6ControlReqResult_Object = MibScalar
sleRoute6ControlReqResult = _SleRoute6ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 5),
    _SleRoute6ControlReqResult_Type()
)
sleRoute6ControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlReqResult.setStatus("current")


class _SleRoute6ControlVRFIndex_Type(Integer32):
    """Custom type sleRoute6ControlVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleRoute6ControlVRFIndex_Type.__name__ = "Integer32"
_SleRoute6ControlVRFIndex_Object = MibScalar
sleRoute6ControlVRFIndex = _SleRoute6ControlVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 6),
    _SleRoute6ControlVRFIndex_Type()
)
sleRoute6ControlVRFIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlVRFIndex.setStatus("current")
_SleRoute6ControlDstAddress_Type = InetAddressIPv6
_SleRoute6ControlDstAddress_Object = MibScalar
sleRoute6ControlDstAddress = _SleRoute6ControlDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 7),
    _SleRoute6ControlDstAddress_Type()
)
sleRoute6ControlDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlDstAddress.setStatus("current")
_SleRoute6ControlDstMask_Type = InetAddressPrefixLength
_SleRoute6ControlDstMask_Object = MibScalar
sleRoute6ControlDstMask = _SleRoute6ControlDstMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 8),
    _SleRoute6ControlDstMask_Type()
)
sleRoute6ControlDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlDstMask.setStatus("current")
_SleRoute6ControlGateway_Type = InetAddressIPv6
_SleRoute6ControlGateway_Object = MibScalar
sleRoute6ControlGateway = _SleRoute6ControlGateway_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 9),
    _SleRoute6ControlGateway_Type()
)
sleRoute6ControlGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlGateway.setStatus("current")


class _SleRoute6ControlInterface_Type(Integer32):
    """Custom type sleRoute6ControlInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11023),
    )


_SleRoute6ControlInterface_Type.__name__ = "Integer32"
_SleRoute6ControlInterface_Object = MibScalar
sleRoute6ControlInterface = _SleRoute6ControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 10),
    _SleRoute6ControlInterface_Type()
)
sleRoute6ControlInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlInterface.setStatus("current")


class _SleRoute6ControlDistance_Type(Integer32):
    """Custom type sleRoute6ControlDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRoute6ControlDistance_Type.__name__ = "Integer32"
_SleRoute6ControlDistance_Object = MibScalar
sleRoute6ControlDistance = _SleRoute6ControlDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 2, 11),
    _SleRoute6ControlDistance_Type()
)
sleRoute6ControlDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRoute6ControlDistance.setStatus("current")
_SleRoute6Notification_ObjectIdentity = ObjectIdentity
sleRoute6Notification = _SleRoute6Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 3)
)
_SleNetworkBase6_ObjectIdentity = ObjectIdentity
sleNetworkBase6 = _SleNetworkBase6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6)
)
_SleNetworkBase6Info_ObjectIdentity = ObjectIdentity
sleNetworkBase6Info = _SleNetworkBase6Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 1)
)


class _SleNetwork6DADinterval_Type(Integer32):
    """Custom type sleNetwork6DADinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 50000),
    )


_SleNetwork6DADinterval_Type.__name__ = "Integer32"
_SleNetwork6DADinterval_Object = MibScalar
sleNetwork6DADinterval = _SleNetwork6DADinterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 1, 1),
    _SleNetwork6DADinterval_Type()
)
sleNetwork6DADinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetwork6DADinterval.setStatus("current")
_SleNetworkBase6Control_ObjectIdentity = ObjectIdentity
sleNetworkBase6Control = _SleNetworkBase6Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 2)
)


class _SleNetworkBase6ControlRequest_Type(Integer32):
    """Custom type sleNetworkBase6ControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDADInterval", 1)
    )


_SleNetworkBase6ControlRequest_Type.__name__ = "Integer32"
_SleNetworkBase6ControlRequest_Object = MibScalar
sleNetworkBase6ControlRequest = _SleNetworkBase6ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 2, 1),
    _SleNetworkBase6ControlRequest_Type()
)
sleNetworkBase6ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkBase6ControlRequest.setStatus("current")
_SleNetworkBase6ControlStatus_Type = SleControlStatusType
_SleNetworkBase6ControlStatus_Object = MibScalar
sleNetworkBase6ControlStatus = _SleNetworkBase6ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 2, 2),
    _SleNetworkBase6ControlStatus_Type()
)
sleNetworkBase6ControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkBase6ControlStatus.setStatus("current")
_SleNetworkBase6ControlTimer_Type = Gauge32
_SleNetworkBase6ControlTimer_Object = MibScalar
sleNetworkBase6ControlTimer = _SleNetworkBase6ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 2, 3),
    _SleNetworkBase6ControlTimer_Type()
)
sleNetworkBase6ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkBase6ControlTimer.setStatus("current")
_SleNetworkBase6ControlTimeStamp_Type = TimeTicks
_SleNetworkBase6ControlTimeStamp_Object = MibScalar
sleNetworkBase6ControlTimeStamp = _SleNetworkBase6ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 2, 4),
    _SleNetworkBase6ControlTimeStamp_Type()
)
sleNetworkBase6ControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkBase6ControlTimeStamp.setStatus("current")
_SleNetworkBase6ControlReqResult_Type = SleControlRequestResultType
_SleNetworkBase6ControlReqResult_Object = MibScalar
sleNetworkBase6ControlReqResult = _SleNetworkBase6ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 2, 5),
    _SleNetworkBase6ControlReqResult_Type()
)
sleNetworkBase6ControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkBase6ControlReqResult.setStatus("current")


class _SleNetworkBase6ControlDADinterval_Type(Integer32):
    """Custom type sleNetworkBase6ControlDADinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 50000),
    )


_SleNetworkBase6ControlDADinterval_Type.__name__ = "Integer32"
_SleNetworkBase6ControlDADinterval_Object = MibScalar
sleNetworkBase6ControlDADinterval = _SleNetworkBase6ControlDADinterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 2, 6),
    _SleNetworkBase6ControlDADinterval_Type()
)
sleNetworkBase6ControlDADinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNetworkBase6ControlDADinterval.setStatus("current")
_SleNetworkBase6Notification_ObjectIdentity = ObjectIdentity
sleNetworkBase6Notification = _SleNetworkBase6Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 3)
)
_SleIpVRF6_ObjectIdentity = ObjectIdentity
sleIpVRF6 = _SleIpVRF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7)
)
_SleIpVRF6SelectionSourceTable_Object = MibTable
sleIpVRF6SelectionSourceTable = _SleIpVRF6SelectionSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 1)
)
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceTable.setStatus("current")
_SleIpVRF6SelectionSourceEntry_Object = MibTableRow
sleIpVRF6SelectionSourceEntry = _SleIpVRF6SelectionSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 1, 1)
)
sleIpVRF6SelectionSourceEntry.setIndexNames(
    (0, "SLE-Network6-MIB", "sleIpVRF6SelectionSourceAddr"),
    (0, "SLE-Network6-MIB", "sleIpVRF6SelectionSourceMask"),
)
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceEntry.setStatus("current")
_SleIpVRF6SelectionSourceAddr_Type = InetAddressIPv6
_SleIpVRF6SelectionSourceAddr_Object = MibTableColumn
sleIpVRF6SelectionSourceAddr = _SleIpVRF6SelectionSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 1, 1, 1),
    _SleIpVRF6SelectionSourceAddr_Type()
)
sleIpVRF6SelectionSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceAddr.setStatus("current")


class _SleIpVRF6SelectionSourceMask_Type(InetAddressPrefixLength):
    """Custom type sleIpVRF6SelectionSourceMask based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleIpVRF6SelectionSourceMask_Type.__name__ = "InetAddressPrefixLength"
_SleIpVRF6SelectionSourceMask_Object = MibTableColumn
sleIpVRF6SelectionSourceMask = _SleIpVRF6SelectionSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 1, 1, 2),
    _SleIpVRF6SelectionSourceMask_Type()
)
sleIpVRF6SelectionSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceMask.setStatus("current")


class _SleIpVRF6SelectionSourceVRFIndex_Type(Integer32):
    """Custom type sleIpVRF6SelectionSourceVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleIpVRF6SelectionSourceVRFIndex_Type.__name__ = "Integer32"
_SleIpVRF6SelectionSourceVRFIndex_Object = MibTableColumn
sleIpVRF6SelectionSourceVRFIndex = _SleIpVRF6SelectionSourceVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 1, 1, 3),
    _SleIpVRF6SelectionSourceVRFIndex_Type()
)
sleIpVRF6SelectionSourceVRFIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceVRFIndex.setStatus("current")
_SleIpVRF6SelectionSourceControl_ObjectIdentity = ObjectIdentity
sleIpVRF6SelectionSourceControl = _SleIpVRF6SelectionSourceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2)
)


class _SleIpVRF6SelectionSourceControlRequest_Type(Integer32):
    """Custom type sleIpVRF6SelectionSourceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createVRF6SelectionSource", 1),
          ("deleteVRF6SelectionSource", 2))
    )


_SleIpVRF6SelectionSourceControlRequest_Type.__name__ = "Integer32"
_SleIpVRF6SelectionSourceControlRequest_Object = MibScalar
sleIpVRF6SelectionSourceControlRequest = _SleIpVRF6SelectionSourceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 1),
    _SleIpVRF6SelectionSourceControlRequest_Type()
)
sleIpVRF6SelectionSourceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlRequest.setStatus("current")
_SleIpVRF6SelectionSourceControlStatus_Type = SleControlStatusType
_SleIpVRF6SelectionSourceControlStatus_Object = MibScalar
sleIpVRF6SelectionSourceControlStatus = _SleIpVRF6SelectionSourceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 2),
    _SleIpVRF6SelectionSourceControlStatus_Type()
)
sleIpVRF6SelectionSourceControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlStatus.setStatus("current")
_SleIpVRF6SelectionSourceControlTimer_Type = Gauge32
_SleIpVRF6SelectionSourceControlTimer_Object = MibScalar
sleIpVRF6SelectionSourceControlTimer = _SleIpVRF6SelectionSourceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 3),
    _SleIpVRF6SelectionSourceControlTimer_Type()
)
sleIpVRF6SelectionSourceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlTimer.setStatus("current")
_SleIpVRF6SelectionSourceControlTimeStamp_Type = TimeTicks
_SleIpVRF6SelectionSourceControlTimeStamp_Object = MibScalar
sleIpVRF6SelectionSourceControlTimeStamp = _SleIpVRF6SelectionSourceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 4),
    _SleIpVRF6SelectionSourceControlTimeStamp_Type()
)
sleIpVRF6SelectionSourceControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlTimeStamp.setStatus("current")
_SleIpVRF6SelectionSourceControlReqResult_Type = SleControlRequestResultType
_SleIpVRF6SelectionSourceControlReqResult_Object = MibScalar
sleIpVRF6SelectionSourceControlReqResult = _SleIpVRF6SelectionSourceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 5),
    _SleIpVRF6SelectionSourceControlReqResult_Type()
)
sleIpVRF6SelectionSourceControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlReqResult.setStatus("current")
_SleIpVRF6SelectionSourceControlAddr_Type = InetAddressIPv6
_SleIpVRF6SelectionSourceControlAddr_Object = MibScalar
sleIpVRF6SelectionSourceControlAddr = _SleIpVRF6SelectionSourceControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 6),
    _SleIpVRF6SelectionSourceControlAddr_Type()
)
sleIpVRF6SelectionSourceControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlAddr.setStatus("current")
_SleIpVRF6SelectionSourceControlMask_Type = InetAddressPrefixLength
_SleIpVRF6SelectionSourceControlMask_Object = MibScalar
sleIpVRF6SelectionSourceControlMask = _SleIpVRF6SelectionSourceControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 7),
    _SleIpVRF6SelectionSourceControlMask_Type()
)
sleIpVRF6SelectionSourceControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlMask.setStatus("current")


class _SleIpVRF6SelectionSourceControlVRFIndex_Type(Integer32):
    """Custom type sleIpVRF6SelectionSourceControlVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleIpVRF6SelectionSourceControlVRFIndex_Type.__name__ = "Integer32"
_SleIpVRF6SelectionSourceControlVRFIndex_Object = MibScalar
sleIpVRF6SelectionSourceControlVRFIndex = _SleIpVRF6SelectionSourceControlVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 2, 8),
    _SleIpVRF6SelectionSourceControlVRFIndex_Type()
)
sleIpVRF6SelectionSourceControlVRFIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceControlVRFIndex.setStatus("current")
_SleIpVRF6SelectionSourceNotification_ObjectIdentity = ObjectIdentity
sleIpVRF6SelectionSourceNotification = _SleIpVRF6SelectionSourceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 3)
)

# Managed Objects groups

sleNetwork6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 9)
)
sleNetwork6Group.setObjects(
      *(("SLE-Network6-MIB", "sleIPAddr6ControlIfIndex"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlValue"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlMask"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlScore"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlType"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlValidTime"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlUsedTime"),
        ("SLE-Network6-MIB", "sleIpAddr6Mask"),
        ("SLE-Network6-MIB", "sleIpAddr6Score"),
        ("SLE-Network6-MIB", "sleIpAddr6Status"),
        ("SLE-Network6-MIB", "sleIpAddr6ValidTime"),
        ("SLE-Network6-MIB", "sleIpAddr6UsedTime"),
        ("SLE-Network6-MIB", "sleIpAddr6ControlRequest"),
        ("SLE-Network6-MIB", "sleIpAddr6ControlTimer"),
        ("SLE-Network6-MIB", "sleIpAddr6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleIpAddr6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6Index"),
        ("SLE-Network6-MIB", "sleNetIf6Name"),
        ("SLE-Network6-MIB", "sleNetIf6Ipv6State"),
        ("SLE-Network6-MIB", "sleNetIf6Mode"),
        ("SLE-Network6-MIB", "sleNetIf6RouteMap"),
        ("SLE-Network6-MIB", "sleNetIf6AddrAutoConf"),
        ("SLE-Network6-MIB", "sleNetIf6AddrAutoConfDefault"),
        ("SLE-Network6-MIB", "sleNetIf6NdRouterPref"),
        ("SLE-Network6-MIB", "sleNetIf6SuppressRA"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaMaxInterval"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaMinInterval"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaLifeTime"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaReachTime"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaHopLimit"),
        ("SLE-Network6-MIB", "sleNetIf6NdRetransTime"),
        ("SLE-Network6-MIB", "sleNetIf6NdMFlag"),
        ("SLE-Network6-MIB", "sleNetIf6NdOFlag"),
        ("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlStatus"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimer"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIndex"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIpv6State"),
        ("SLE-Network6-MIB", "sleNetIf6ControlMode"),
        ("SLE-Network6-MIB", "sleNetIf6ControlRouteMap"),
        ("SLE-Network6-MIB", "sleNetIf6ControlAutoConf"),
        ("SLE-Network6-MIB", "sleNetIf6ControlAutoConfDefault"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdRouterPref"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdSuppressRA"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdMaxInterval"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdMinInterval"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdRaLifeTime"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdRaReachTime"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdRaHopLimit"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdRetransTime"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdMFlag"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdOFlag"),
        ("SLE-Network6-MIB", "sleNdPrefixValue"),
        ("SLE-Network6-MIB", "sleNdPrefixValTime"),
        ("SLE-Network6-MIB", "sleNdPrefixPreTime"),
        ("SLE-Network6-MIB", "sleNdPrefixOffLink"),
        ("SLE-Network6-MIB", "sleNdPrefixNoAutoconfig"),
        ("SLE-Network6-MIB", "sleNdPrefixControlRequest"),
        ("SLE-Network6-MIB", "sleNdPrefixControlStatus"),
        ("SLE-Network6-MIB", "sleNdPrefixControlTimer"),
        ("SLE-Network6-MIB", "sleNdPrefixControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNdPrefixControlReqResult"),
        ("SLE-Network6-MIB", "sleNdPrefixControlIfIndex"),
        ("SLE-Network6-MIB", "sleNdPrefixControlValue"),
        ("SLE-Network6-MIB", "sleNdPrefixControlValTime"),
        ("SLE-Network6-MIB", "sleNdPrefixControlPreTime"),
        ("SLE-Network6-MIB", "sleNdPrefixControlOffLink"),
        ("SLE-Network6-MIB", "sleNdPrefixControlNoAutoconfig"),
        ("SLE-Network6-MIB", "sleNetIf6NdProxy"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdProxy"),
        ("SLE-Network6-MIB", "sleNetIf6NdDadAttempt"),
        ("SLE-Network6-MIB", "sleNetIf6ControlNdDadAttempt"),
        ("SLE-Network6-MIB", "sleNeighbour6HwUsed"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlIfIndex"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlAddress"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlPhyAddress"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlMask"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlRequest"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlStatus"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlTimer"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNeighbour6Address"),
        ("SLE-Network6-MIB", "sleNeighbour6PhyAddress"),
        ("SLE-Network6-MIB", "sleNeighbour6PortIndex"),
        ("SLE-Network6-MIB", "sleNeighbour6State"),
        ("SLE-Network6-MIB", "sleNeighbour6HwType"),
        ("SLE-Network6-MIB", "sleNdPrefixMask"),
        ("SLE-Network6-MIB", "sleNdPrefixControlMask"),
        ("SLE-Network6-MIB", "sleNdPrefixDefault"),
        ("SLE-Network6-MIB", "sleNdPrefixControlDefault"),
        ("SLE-Network6-MIB", "sleRoute6DstAddress"),
        ("SLE-Network6-MIB", "sleRoute6DstMask"),
        ("SLE-Network6-MIB", "sleRoute6Proto"),
        ("SLE-Network6-MIB", "sleRoute6Gateway"),
        ("SLE-Network6-MIB", "sleRoute6Type"),
        ("SLE-Network6-MIB", "sleRoute6Subtype"),
        ("SLE-Network6-MIB", "sleRoute6Distance"),
        ("SLE-Network6-MIB", "sleRoute6Metric"),
        ("SLE-Network6-MIB", "sleRoute6Active"),
        ("SLE-Network6-MIB", "sleRoute6NexthopStatus"),
        ("SLE-Network6-MIB", "sleRoute6RibStatus"),
        ("SLE-Network6-MIB", "sleRoute6BfdState"),
        ("SLE-Network6-MIB", "sleRoute6ControlRequest"),
        ("SLE-Network6-MIB", "sleRoute6ControlStatus"),
        ("SLE-Network6-MIB", "sleRoute6ControlTimer"),
        ("SLE-Network6-MIB", "sleRoute6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleRoute6ControlReqResult"),
        ("SLE-Network6-MIB", "sleRoute6ControlVRFIndex"),
        ("SLE-Network6-MIB", "sleRoute6ControlDstAddress"),
        ("SLE-Network6-MIB", "sleRoute6ControlDstMask"),
        ("SLE-Network6-MIB", "sleRoute6ControlGateway"),
        ("SLE-Network6-MIB", "sleRoute6ControlInterface"),
        ("SLE-Network6-MIB", "sleRoute6ControlDistance"),
        ("SLE-Network6-MIB", "sleNetwork6DADinterval"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlStatus"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlTimer"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlDADinterval"),
        ("SLE-Network6-MIB", "sleIpAddr6Value"),
        ("SLE-Network6-MIB", "sleIpAddr6Type"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlVRFIndex"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlMask"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlAddr"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlReqResult"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlTimeStamp"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlTimer"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlStatus"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlRequest"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceVRFIndex"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceMask"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceAddr"),
        ("SLE-Network6-MIB", "sleIpAddr6ControlStatus"),
        ("SLE-NETWORK-MIB", "sleIpVRFIndex"),
        ("SLE-Network6-MIB", "sleNetIf6Identifier"),
        ("SLE-Network6-MIB", "sleNetIf6Ip6MartianFilter"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIdentifier"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIp6MartianFilter"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlStatus"))
)
if mibBuilder.loadTexts:
    sleNetwork6Group.setStatus("current")


# Notification objects

sleIp6StateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 1)
)
sleIp6StateChanged.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6Index"),
        ("SLE-Network6-MIB", "sleNetIf6Ipv6State"))
)
if mibBuilder.loadTexts:
    sleIp6StateChanged.setStatus(
        "current"
    )

sleIfModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 2)
)
sleIfModeChanged.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6Index"),
        ("SLE-Network6-MIB", "sleNetIf6Mode"))
)
if mibBuilder.loadTexts:
    sleIfModeChanged.setStatus(
        "current"
    )

sleAddrAutoConfChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 3)
)
sleAddrAutoConfChanged.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6Index"),
        ("SLE-Network6-MIB", "sleNetIf6AddrAutoConf"),
        ("SLE-Network6-MIB", "sleNetIf6AddrAutoConfDefault"))
)
if mibBuilder.loadTexts:
    sleAddrAutoConfChanged.setStatus(
        "current"
    )

sleNdProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 4)
)
sleNdProfileChanged.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6Index"),
        ("SLE-Network6-MIB", "sleNetIf6NdRouterPref"),
        ("SLE-Network6-MIB", "sleNetIf6SuppressRA"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaMaxInterval"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaMinInterval"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaLifeTime"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaReachTime"),
        ("SLE-Network6-MIB", "sleNetIf6NdRaHopLimit"),
        ("SLE-Network6-MIB", "sleNetIf6NdRetransTime"),
        ("SLE-Network6-MIB", "sleNetIf6NdMFlag"),
        ("SLE-Network6-MIB", "sleNetIf6NdOFlag"),
        ("SLE-Network6-MIB", "sleNetIf6NdProxy"),
        ("SLE-Network6-MIB", "sleNetIf6NdDadAttempt"))
)
if mibBuilder.loadTexts:
    sleNdProfileChanged.setStatus(
        "current"
    )

sleRouteMapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 5)
)
sleRouteMapSet.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRouteMapSet.setStatus(
        "current"
    )

sleRouteMapUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 6)
)
sleRouteMapUnset.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRouteMapUnset.setStatus(
        "current"
    )

sleIdentifierChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 7)
)
sleIdentifierChanged.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIndex"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIdentifier"))
)
if mibBuilder.loadTexts:
    sleIdentifierChanged.setStatus(
        "current"
    )

sleIp6MartianFilterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 1, 3, 8)
)
sleIp6MartianFilterChanged.setObjects(
      *(("SLE-Network6-MIB", "sleNetIf6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetIf6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetIf6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIndex"),
        ("SLE-Network6-MIB", "sleNetIf6ControlIp6MartianFilter"))
)
if mibBuilder.loadTexts:
    sleIp6MartianFilterChanged.setStatus(
        "current"
    )

sleIPAddr6Created = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 3, 1)
)
sleIPAddr6Created.setObjects(
      *(("SLE-Network6-MIB", "sleIpAddr6Score"),
        ("SLE-Network6-MIB", "sleIpAddr6Type"))
)
if mibBuilder.loadTexts:
    sleIPAddr6Created.setStatus(
        "current"
    )

sleIPAddr6Deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 3, 2)
)
sleIPAddr6Deleted.setObjects(
      *(("SLE-Network6-MIB", "sleIPAddr6ControlIfIndex"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlValue"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlMask"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlScore"),
        ("SLE-Network6-MIB", "sleIPAddr6ControlType"))
)
if mibBuilder.loadTexts:
    sleIPAddr6Deleted.setStatus(
        "current"
    )

sleIPAddr6AllDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 2, 3, 3)
)
sleIPAddr6AllDeleted.setObjects(
    ("SLE-Network6-MIB", "sleIPAddr6ControlIfIndex")
)
if mibBuilder.loadTexts:
    sleIPAddr6AllDeleted.setStatus(
        "current"
    )

sleNdPrefixCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 3, 1)
)
sleNdPrefixCreated.setObjects(
      *(("SLE-Network6-MIB", "sleNdPrefixControlRequest"),
        ("SLE-Network6-MIB", "sleNdPrefixControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNdPrefixControlReqResult"),
        ("SLE-Network6-MIB", "sleNdPrefixControlIfIndex"),
        ("SLE-Network6-MIB", "sleNdPrefixDefault"),
        ("SLE-Network6-MIB", "sleNdPrefixValue"),
        ("SLE-Network6-MIB", "sleNdPrefixMask"),
        ("SLE-Network6-MIB", "sleNdPrefixValTime"),
        ("SLE-Network6-MIB", "sleNdPrefixPreTime"),
        ("SLE-Network6-MIB", "sleNdPrefixOffLink"),
        ("SLE-Network6-MIB", "sleNdPrefixNoAutoconfig"))
)
if mibBuilder.loadTexts:
    sleNdPrefixCreated.setStatus(
        "current"
    )

sleNdPrefixDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 3, 3, 2)
)
sleNdPrefixDeleted.setObjects(
      *(("SLE-Network6-MIB", "sleNdPrefixControlRequest"),
        ("SLE-Network6-MIB", "sleNdPrefixControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNdPrefixControlReqResult"),
        ("SLE-Network6-MIB", "sleNdPrefixControlIfIndex"),
        ("SLE-Network6-MIB", "sleNdPrefixControlDefault"),
        ("SLE-Network6-MIB", "sleNdPrefixControlValue"),
        ("SLE-Network6-MIB", "sleNdPrefixControlMask"))
)
if mibBuilder.loadTexts:
    sleNdPrefixDeleted.setStatus(
        "current"
    )

sleNeighbour6Created = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 3, 1)
)
sleNeighbour6Created.setObjects(
      *(("SLE-Network6-MIB", "sleNeighbour6ControlRequest"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNeighbour6PhyAddress"))
)
if mibBuilder.loadTexts:
    sleNeighbour6Created.setStatus(
        "current"
    )

sleNeighbour6Deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 3, 2)
)
sleNeighbour6Deleted.setObjects(
      *(("SLE-Network6-MIB", "sleNeighbour6ControlRequest"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlAddress"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlMask"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlIfIndex"))
)
if mibBuilder.loadTexts:
    sleNeighbour6Deleted.setStatus(
        "current"
    )

sleNeighbour6Cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 4, 3, 3)
)
sleNeighbour6Cleared.setObjects(
      *(("SLE-Network6-MIB", "sleNeighbour6ControlRequest"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlIfIndex"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlAddress"),
        ("SLE-Network6-MIB", "sleNeighbour6ControlMask"))
)
if mibBuilder.loadTexts:
    sleNeighbour6Cleared.setStatus(
        "current"
    )

sleRoute6Created = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 3, 1)
)
sleRoute6Created.setObjects(
      *(("SLE-Network6-MIB", "sleRoute6ControlRequest"),
        ("SLE-Network6-MIB", "sleRoute6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleRoute6ControlReqResult"),
        ("SLE-Network6-MIB", "sleRoute6DstAddress"),
        ("SLE-Network6-MIB", "sleRoute6DstMask"),
        ("SLE-Network6-MIB", "sleRoute6Proto"),
        ("SLE-Network6-MIB", "sleRoute6Gateway"),
        ("SLE-Network6-MIB", "sleRoute6Distance"))
)
if mibBuilder.loadTexts:
    sleRoute6Created.setStatus(
        "current"
    )

sleRoute6Deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 5, 3, 2)
)
sleRoute6Deleted.setObjects(
      *(("SLE-Network6-MIB", "sleRoute6ControlRequest"),
        ("SLE-Network6-MIB", "sleRoute6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleRoute6ControlReqResult"),
        ("SLE-Network6-MIB", "sleRoute6ControlVRFIndex"),
        ("SLE-Network6-MIB", "sleRoute6ControlDstAddress"),
        ("SLE-Network6-MIB", "sleRoute6ControlDstMask"),
        ("SLE-Network6-MIB", "sleRoute6ControlGateway"),
        ("SLE-Network6-MIB", "sleRoute6ControlInterface"))
)
if mibBuilder.loadTexts:
    sleRoute6Deleted.setStatus(
        "current"
    )

sleNetworkBase6DADIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 6, 3, 1)
)
sleNetworkBase6DADIntervalChanged.setObjects(
      *(("SLE-Network6-MIB", "sleNetworkBase6ControlRequest"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlTimeStamp"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlReqResult"),
        ("SLE-Network6-MIB", "sleNetworkBase6ControlDADinterval"))
)
if mibBuilder.loadTexts:
    sleNetworkBase6DADIntervalChanged.setStatus(
        "current"
    )

sleIpVRF6SelectionSourceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 3, 1)
)
sleIpVRF6SelectionSourceCreated.setObjects(
      *(("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlRequest"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlTimeStamp"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlReqResult"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceVRFIndex"))
)
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceCreated.setStatus(
        "current"
    )

sleIpVRF6SelectionSourceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 7, 3, 2)
)
sleIpVRF6SelectionSourceDeleted.setObjects(
      *(("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlRequest"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlTimeStamp"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlMask"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlAddr"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceControlReqResult"))
)
if mibBuilder.loadTexts:
    sleIpVRF6SelectionSourceDeleted.setStatus(
        "current"
    )


# Notifications groups

sleNetwork6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 26, 10)
)
sleNetwork6NotificationGroup.setObjects(
      *(("SLE-Network6-MIB", "sleIPAddr6Created"),
        ("SLE-Network6-MIB", "sleNdPrefixCreated"),
        ("SLE-Network6-MIB", "sleNdPrefixDeleted"),
        ("SLE-Network6-MIB", "sleIPAddr6AllDeleted"),
        ("SLE-Network6-MIB", "sleNeighbour6Created"),
        ("SLE-Network6-MIB", "sleNeighbour6Deleted"),
        ("SLE-Network6-MIB", "sleNeighbour6Cleared"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceDeleted"),
        ("SLE-Network6-MIB", "sleIpVRF6SelectionSourceCreated"),
        ("SLE-Network6-MIB", "sleIdentifierChanged"),
        ("SLE-Network6-MIB", "sleIp6MartianFilterChanged"),
        ("SLE-Network6-MIB", "sleIPAddr6Deleted"),
        ("SLE-Network6-MIB", "sleIp6StateChanged"),
        ("SLE-Network6-MIB", "sleIfModeChanged"),
        ("SLE-Network6-MIB", "sleAddrAutoConfChanged"),
        ("SLE-Network6-MIB", "sleNdProfileChanged"),
        ("SLE-Network6-MIB", "sleRouteMapSet"),
        ("SLE-Network6-MIB", "sleRouteMapUnset"),
        ("SLE-Network6-MIB", "sleRoute6Created"),
        ("SLE-Network6-MIB", "sleRoute6Deleted"),
        ("SLE-Network6-MIB", "sleNetworkBase6DADIntervalChanged"))
)
if mibBuilder.loadTexts:
    sleNetwork6NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-Network6-MIB",
    **{"sleNetwork6": sleNetwork6,
       "sleNetInterface6": sleNetInterface6,
       "sleNetIf6Table": sleNetIf6Table,
       "sleNetIf6Entry": sleNetIf6Entry,
       "sleNetIf6Index": sleNetIf6Index,
       "sleNetIf6Name": sleNetIf6Name,
       "sleNetIf6Ipv6State": sleNetIf6Ipv6State,
       "sleNetIf6Mode": sleNetIf6Mode,
       "sleNetIf6RouteMap": sleNetIf6RouteMap,
       "sleNetIf6AddrAutoConf": sleNetIf6AddrAutoConf,
       "sleNetIf6AddrAutoConfDefault": sleNetIf6AddrAutoConfDefault,
       "sleNetIf6NdRouterPref": sleNetIf6NdRouterPref,
       "sleNetIf6SuppressRA": sleNetIf6SuppressRA,
       "sleNetIf6NdRaMaxInterval": sleNetIf6NdRaMaxInterval,
       "sleNetIf6NdRaMinInterval": sleNetIf6NdRaMinInterval,
       "sleNetIf6NdRaLifeTime": sleNetIf6NdRaLifeTime,
       "sleNetIf6NdRaReachTime": sleNetIf6NdRaReachTime,
       "sleNetIf6NdRaHopLimit": sleNetIf6NdRaHopLimit,
       "sleNetIf6NdRetransTime": sleNetIf6NdRetransTime,
       "sleNetIf6NdMFlag": sleNetIf6NdMFlag,
       "sleNetIf6NdOFlag": sleNetIf6NdOFlag,
       "sleNetIf6NdProxy": sleNetIf6NdProxy,
       "sleNetIf6NdDadAttempt": sleNetIf6NdDadAttempt,
       "sleNetIf6Identifier": sleNetIf6Identifier,
       "sleNetIf6Ip6MartianFilter": sleNetIf6Ip6MartianFilter,
       "sleNetIf6Control": sleNetIf6Control,
       "sleNetIf6ControlRequest": sleNetIf6ControlRequest,
       "sleNetIf6ControlStatus": sleNetIf6ControlStatus,
       "sleNetIf6ControlTimer": sleNetIf6ControlTimer,
       "sleNetIf6ControlTimeStamp": sleNetIf6ControlTimeStamp,
       "sleNetIf6ControlReqResult": sleNetIf6ControlReqResult,
       "sleNetIf6ControlIndex": sleNetIf6ControlIndex,
       "sleNetIf6ControlIpv6State": sleNetIf6ControlIpv6State,
       "sleNetIf6ControlMode": sleNetIf6ControlMode,
       "sleNetIf6ControlRouteMap": sleNetIf6ControlRouteMap,
       "sleNetIf6ControlAutoConf": sleNetIf6ControlAutoConf,
       "sleNetIf6ControlAutoConfDefault": sleNetIf6ControlAutoConfDefault,
       "sleNetIf6ControlNdRouterPref": sleNetIf6ControlNdRouterPref,
       "sleNetIf6ControlNdSuppressRA": sleNetIf6ControlNdSuppressRA,
       "sleNetIf6ControlNdMaxInterval": sleNetIf6ControlNdMaxInterval,
       "sleNetIf6ControlNdMinInterval": sleNetIf6ControlNdMinInterval,
       "sleNetIf6ControlNdRaLifeTime": sleNetIf6ControlNdRaLifeTime,
       "sleNetIf6ControlNdRaReachTime": sleNetIf6ControlNdRaReachTime,
       "sleNetIf6ControlNdRaHopLimit": sleNetIf6ControlNdRaHopLimit,
       "sleNetIf6ControlNdRetransTime": sleNetIf6ControlNdRetransTime,
       "sleNetIf6ControlNdMFlag": sleNetIf6ControlNdMFlag,
       "sleNetIf6ControlNdOFlag": sleNetIf6ControlNdOFlag,
       "sleNetIf6ControlNdProxy": sleNetIf6ControlNdProxy,
       "sleNetIf6ControlNdDadAttempt": sleNetIf6ControlNdDadAttempt,
       "sleNetIf6ControlIdentifier": sleNetIf6ControlIdentifier,
       "sleNetIf6ControlIp6MartianFilter": sleNetIf6ControlIp6MartianFilter,
       "sleNetIf6Notification": sleNetIf6Notification,
       "sleIp6StateChanged": sleIp6StateChanged,
       "sleIfModeChanged": sleIfModeChanged,
       "sleAddrAutoConfChanged": sleAddrAutoConfChanged,
       "sleNdProfileChanged": sleNdProfileChanged,
       "sleRouteMapSet": sleRouteMapSet,
       "sleRouteMapUnset": sleRouteMapUnset,
       "sleIdentifierChanged": sleIdentifierChanged,
       "sleIp6MartianFilterChanged": sleIp6MartianFilterChanged,
       "sleIpAddress6": sleIpAddress6,
       "sleIpAddr6Table": sleIpAddr6Table,
       "sleIpAddr6Entry": sleIpAddr6Entry,
       "sleIpAddr6Value": sleIpAddr6Value,
       "sleIpAddr6Mask": sleIpAddr6Mask,
       "sleIpAddr6Score": sleIpAddr6Score,
       "sleIpAddr6Type": sleIpAddr6Type,
       "sleIpAddr6Status": sleIpAddr6Status,
       "sleIpAddr6ValidTime": sleIpAddr6ValidTime,
       "sleIpAddr6UsedTime": sleIpAddr6UsedTime,
       "sleIpAddr6Control": sleIpAddr6Control,
       "sleIpAddr6ControlRequest": sleIpAddr6ControlRequest,
       "sleIpAddr6ControlStatus": sleIpAddr6ControlStatus,
       "sleIpAddr6ControlTimer": sleIpAddr6ControlTimer,
       "sleIpAddr6ControlTimeStamp": sleIpAddr6ControlTimeStamp,
       "sleIpAddr6ControlReqResult": sleIpAddr6ControlReqResult,
       "sleIPAddr6ControlIfIndex": sleIPAddr6ControlIfIndex,
       "sleIPAddr6ControlValue": sleIPAddr6ControlValue,
       "sleIPAddr6ControlMask": sleIPAddr6ControlMask,
       "sleIPAddr6ControlScore": sleIPAddr6ControlScore,
       "sleIPAddr6ControlType": sleIPAddr6ControlType,
       "sleIPAddr6ControlStatus": sleIPAddr6ControlStatus,
       "sleIPAddr6ControlValidTime": sleIPAddr6ControlValidTime,
       "sleIPAddr6ControlUsedTime": sleIPAddr6ControlUsedTime,
       "sleIpAddr6Notification": sleIpAddr6Notification,
       "sleIPAddr6Created": sleIPAddr6Created,
       "sleIPAddr6Deleted": sleIPAddr6Deleted,
       "sleIPAddr6AllDeleted": sleIPAddr6AllDeleted,
       "sleNdPrefix": sleNdPrefix,
       "sleNdPrefixTable": sleNdPrefixTable,
       "sleNdPrefixEntry": sleNdPrefixEntry,
       "sleNdPrefixDefault": sleNdPrefixDefault,
       "sleNdPrefixValue": sleNdPrefixValue,
       "sleNdPrefixMask": sleNdPrefixMask,
       "sleNdPrefixValTime": sleNdPrefixValTime,
       "sleNdPrefixPreTime": sleNdPrefixPreTime,
       "sleNdPrefixOffLink": sleNdPrefixOffLink,
       "sleNdPrefixNoAutoconfig": sleNdPrefixNoAutoconfig,
       "sleNdPrefixControl": sleNdPrefixControl,
       "sleNdPrefixControlRequest": sleNdPrefixControlRequest,
       "sleNdPrefixControlStatus": sleNdPrefixControlStatus,
       "sleNdPrefixControlTimer": sleNdPrefixControlTimer,
       "sleNdPrefixControlTimeStamp": sleNdPrefixControlTimeStamp,
       "sleNdPrefixControlReqResult": sleNdPrefixControlReqResult,
       "sleNdPrefixControlIfIndex": sleNdPrefixControlIfIndex,
       "sleNdPrefixControlDefault": sleNdPrefixControlDefault,
       "sleNdPrefixControlValue": sleNdPrefixControlValue,
       "sleNdPrefixControlMask": sleNdPrefixControlMask,
       "sleNdPrefixControlValTime": sleNdPrefixControlValTime,
       "sleNdPrefixControlPreTime": sleNdPrefixControlPreTime,
       "sleNdPrefixControlOffLink": sleNdPrefixControlOffLink,
       "sleNdPrefixControlNoAutoconfig": sleNdPrefixControlNoAutoconfig,
       "sleNdPrefixNotification": sleNdPrefixNotification,
       "sleNdPrefixCreated": sleNdPrefixCreated,
       "sleNdPrefixDeleted": sleNdPrefixDeleted,
       "sleNeighbour6": sleNeighbour6,
       "sleNeighbour6Table": sleNeighbour6Table,
       "sleNeighbour6Entry": sleNeighbour6Entry,
       "sleNeighbour6Address": sleNeighbour6Address,
       "sleNeighbour6PhyAddress": sleNeighbour6PhyAddress,
       "sleNeighbour6PortIndex": sleNeighbour6PortIndex,
       "sleNeighbour6State": sleNeighbour6State,
       "sleNeighbour6HwType": sleNeighbour6HwType,
       "sleNeighbour6HwUsed": sleNeighbour6HwUsed,
       "sleNeighbour6Control": sleNeighbour6Control,
       "sleNeighbour6ControlRequest": sleNeighbour6ControlRequest,
       "sleNeighbour6ControlStatus": sleNeighbour6ControlStatus,
       "sleNeighbour6ControlTimer": sleNeighbour6ControlTimer,
       "sleNeighbour6ControlTimeStamp": sleNeighbour6ControlTimeStamp,
       "sleNeighbour6ControlReqResult": sleNeighbour6ControlReqResult,
       "sleNeighbour6ControlIfIndex": sleNeighbour6ControlIfIndex,
       "sleNeighbour6ControlAddress": sleNeighbour6ControlAddress,
       "sleNeighbour6ControlPhyAddress": sleNeighbour6ControlPhyAddress,
       "sleNeighbour6ControlMask": sleNeighbour6ControlMask,
       "sleNeighbour6Notification": sleNeighbour6Notification,
       "sleNeighbour6Created": sleNeighbour6Created,
       "sleNeighbour6Deleted": sleNeighbour6Deleted,
       "sleNeighbour6Cleared": sleNeighbour6Cleared,
       "sleRoute6": sleRoute6,
       "sleRoute6Table": sleRoute6Table,
       "sleRoute6Entry": sleRoute6Entry,
       "sleRoute6DstAddress": sleRoute6DstAddress,
       "sleRoute6DstMask": sleRoute6DstMask,
       "sleRoute6Proto": sleRoute6Proto,
       "sleRoute6Gateway": sleRoute6Gateway,
       "sleRoute6Type": sleRoute6Type,
       "sleRoute6Subtype": sleRoute6Subtype,
       "sleRoute6Distance": sleRoute6Distance,
       "sleRoute6Metric": sleRoute6Metric,
       "sleRoute6Active": sleRoute6Active,
       "sleRoute6NexthopStatus": sleRoute6NexthopStatus,
       "sleRoute6RibStatus": sleRoute6RibStatus,
       "sleRoute6BfdState": sleRoute6BfdState,
       "sleRoute6Control": sleRoute6Control,
       "sleRoute6ControlRequest": sleRoute6ControlRequest,
       "sleRoute6ControlStatus": sleRoute6ControlStatus,
       "sleRoute6ControlTimer": sleRoute6ControlTimer,
       "sleRoute6ControlTimeStamp": sleRoute6ControlTimeStamp,
       "sleRoute6ControlReqResult": sleRoute6ControlReqResult,
       "sleRoute6ControlVRFIndex": sleRoute6ControlVRFIndex,
       "sleRoute6ControlDstAddress": sleRoute6ControlDstAddress,
       "sleRoute6ControlDstMask": sleRoute6ControlDstMask,
       "sleRoute6ControlGateway": sleRoute6ControlGateway,
       "sleRoute6ControlInterface": sleRoute6ControlInterface,
       "sleRoute6ControlDistance": sleRoute6ControlDistance,
       "sleRoute6Notification": sleRoute6Notification,
       "sleRoute6Created": sleRoute6Created,
       "sleRoute6Deleted": sleRoute6Deleted,
       "sleNetworkBase6": sleNetworkBase6,
       "sleNetworkBase6Info": sleNetworkBase6Info,
       "sleNetwork6DADinterval": sleNetwork6DADinterval,
       "sleNetworkBase6Control": sleNetworkBase6Control,
       "sleNetworkBase6ControlRequest": sleNetworkBase6ControlRequest,
       "sleNetworkBase6ControlStatus": sleNetworkBase6ControlStatus,
       "sleNetworkBase6ControlTimer": sleNetworkBase6ControlTimer,
       "sleNetworkBase6ControlTimeStamp": sleNetworkBase6ControlTimeStamp,
       "sleNetworkBase6ControlReqResult": sleNetworkBase6ControlReqResult,
       "sleNetworkBase6ControlDADinterval": sleNetworkBase6ControlDADinterval,
       "sleNetworkBase6Notification": sleNetworkBase6Notification,
       "sleNetworkBase6DADIntervalChanged": sleNetworkBase6DADIntervalChanged,
       "sleIpVRF6": sleIpVRF6,
       "sleIpVRF6SelectionSourceTable": sleIpVRF6SelectionSourceTable,
       "sleIpVRF6SelectionSourceEntry": sleIpVRF6SelectionSourceEntry,
       "sleIpVRF6SelectionSourceAddr": sleIpVRF6SelectionSourceAddr,
       "sleIpVRF6SelectionSourceMask": sleIpVRF6SelectionSourceMask,
       "sleIpVRF6SelectionSourceVRFIndex": sleIpVRF6SelectionSourceVRFIndex,
       "sleIpVRF6SelectionSourceControl": sleIpVRF6SelectionSourceControl,
       "sleIpVRF6SelectionSourceControlRequest": sleIpVRF6SelectionSourceControlRequest,
       "sleIpVRF6SelectionSourceControlStatus": sleIpVRF6SelectionSourceControlStatus,
       "sleIpVRF6SelectionSourceControlTimer": sleIpVRF6SelectionSourceControlTimer,
       "sleIpVRF6SelectionSourceControlTimeStamp": sleIpVRF6SelectionSourceControlTimeStamp,
       "sleIpVRF6SelectionSourceControlReqResult": sleIpVRF6SelectionSourceControlReqResult,
       "sleIpVRF6SelectionSourceControlAddr": sleIpVRF6SelectionSourceControlAddr,
       "sleIpVRF6SelectionSourceControlMask": sleIpVRF6SelectionSourceControlMask,
       "sleIpVRF6SelectionSourceControlVRFIndex": sleIpVRF6SelectionSourceControlVRFIndex,
       "sleIpVRF6SelectionSourceNotification": sleIpVRF6SelectionSourceNotification,
       "sleIpVRF6SelectionSourceCreated": sleIpVRF6SelectionSourceCreated,
       "sleIpVRF6SelectionSourceDeleted": sleIpVRF6SelectionSourceDeleted,
       "sleNetwork6Group": sleNetwork6Group,
       "sleNetwork6NotificationGroup": sleNetwork6NotificationGroup}
)
