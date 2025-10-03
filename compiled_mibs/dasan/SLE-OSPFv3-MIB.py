# SNMP MIB module (SLE-OSPFv3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-OSPFv3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:56 2025
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

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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

sleOSPFv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleOspfv3Base_ObjectIdentity = ObjectIdentity
sleOspfv3Base = _SleOspfv3Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1)
)
_SleOspfv3BaseInfo_ObjectIdentity = ObjectIdentity
sleOspfv3BaseInfo = _SleOspfv3BaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 1)
)


class _SleOspfv3RouteDisplayMode_Type(Integer32):
    """Custom type sleOspfv3RouteDisplayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("singleLine", 0),
          ("multiLine", 1))
    )


_SleOspfv3RouteDisplayMode_Type.__name__ = "Integer32"
_SleOspfv3RouteDisplayMode_Object = MibScalar
sleOspfv3RouteDisplayMode = _SleOspfv3RouteDisplayMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 1, 1),
    _SleOspfv3RouteDisplayMode_Type()
)
sleOspfv3RouteDisplayMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RouteDisplayMode.setStatus("current")


class _SleOspfv3RestartPeriod_Type(Integer32):
    """Custom type sleOspfv3RestartPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOspfv3RestartPeriod_Type.__name__ = "Integer32"
_SleOspfv3RestartPeriod_Object = MibScalar
sleOspfv3RestartPeriod = _SleOspfv3RestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 1, 2),
    _SleOspfv3RestartPeriod_Type()
)
sleOspfv3RestartPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RestartPeriod.setStatus("current")


class _SleOspfv3RestartHelperPolicy_Type(Integer32):
    """Custom type sleOspfv3RestartHelperPolicy based on Integer32"""
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
        *(("never", 1),
          ("onlyReload", 2),
          ("onlyUpgrade", 3),
          ("reloadUpgrade", 4))
    )


_SleOspfv3RestartHelperPolicy_Type.__name__ = "Integer32"
_SleOspfv3RestartHelperPolicy_Object = MibScalar
sleOspfv3RestartHelperPolicy = _SleOspfv3RestartHelperPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 1, 3),
    _SleOspfv3RestartHelperPolicy_Type()
)
sleOspfv3RestartHelperPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RestartHelperPolicy.setStatus("current")


class _SleOspfv3RestartHelperPeriod_Type(Integer32):
    """Custom type sleOspfv3RestartHelperPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOspfv3RestartHelperPeriod_Type.__name__ = "Integer32"
_SleOspfv3RestartHelperPeriod_Object = MibScalar
sleOspfv3RestartHelperPeriod = _SleOspfv3RestartHelperPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 1, 4),
    _SleOspfv3RestartHelperPeriod_Type()
)
sleOspfv3RestartHelperPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RestartHelperPeriod.setStatus("current")


class _SleOspfv3SnmpNotification_Type(Integer32):
    """Custom type sleOspfv3SnmpNotification based on Integer32"""
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


_SleOspfv3SnmpNotification_Type.__name__ = "Integer32"
_SleOspfv3SnmpNotification_Object = MibScalar
sleOspfv3SnmpNotification = _SleOspfv3SnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 1, 5),
    _SleOspfv3SnmpNotification_Type()
)
sleOspfv3SnmpNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3SnmpNotification.setStatus("current")
_SleOspfv3BaseControl_ObjectIdentity = ObjectIdentity
sleOspfv3BaseControl = _SleOspfv3BaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2)
)


class _SleOspfv3ControlRequest_Type(Integer32):
    """Custom type sleOspfv3ControlRequest based on Integer32"""
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
        *(("setOspfv3RouteDisplayMode", 1),
          ("setOspfv3RestartPeriod", 2),
          ("setOspfv3RestartHelperProfile", 3),
          ("restartOspfv3Graceful", 4),
          ("setSnmpNotification", 5))
    )


_SleOspfv3ControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ControlRequest_Object = MibScalar
sleOspfv3ControlRequest = _SleOspfv3ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 1),
    _SleOspfv3ControlRequest_Type()
)
sleOspfv3ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ControlRequest.setStatus("current")
_SleOspfv3ControlStatus_Type = SleControlStatusType
_SleOspfv3ControlStatus_Object = MibScalar
sleOspfv3ControlStatus = _SleOspfv3ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 2),
    _SleOspfv3ControlStatus_Type()
)
sleOspfv3ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ControlStatus.setStatus("current")
_SleOspfv3ControlTimer_Type = Gauge32
_SleOspfv3ControlTimer_Object = MibScalar
sleOspfv3ControlTimer = _SleOspfv3ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 3),
    _SleOspfv3ControlTimer_Type()
)
sleOspfv3ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ControlTimer.setStatus("current")
_SleOspfv3ControlTimeStamp_Type = TimeTicks
_SleOspfv3ControlTimeStamp_Object = MibScalar
sleOspfv3ControlTimeStamp = _SleOspfv3ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 4),
    _SleOspfv3ControlTimeStamp_Type()
)
sleOspfv3ControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ControlTimeStamp.setStatus("current")
_SleOspfv3ControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ControlReqResult_Object = MibScalar
sleOspfv3ControlReqResult = _SleOspfv3ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 5),
    _SleOspfv3ControlReqResult_Type()
)
sleOspfv3ControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ControlReqResult.setStatus("current")


class _SleOspfv3ControlRouteDisplayMode_Type(Integer32):
    """Custom type sleOspfv3ControlRouteDisplayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("singleLine", 0),
          ("multiLine", 1))
    )


_SleOspfv3ControlRouteDisplayMode_Type.__name__ = "Integer32"
_SleOspfv3ControlRouteDisplayMode_Object = MibScalar
sleOspfv3ControlRouteDisplayMode = _SleOspfv3ControlRouteDisplayMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 6),
    _SleOspfv3ControlRouteDisplayMode_Type()
)
sleOspfv3ControlRouteDisplayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ControlRouteDisplayMode.setStatus("current")


class _SleOspfv3ControlRestartPeriod_Type(Integer32):
    """Custom type sleOspfv3ControlRestartPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOspfv3ControlRestartPeriod_Type.__name__ = "Integer32"
_SleOspfv3ControlRestartPeriod_Object = MibScalar
sleOspfv3ControlRestartPeriod = _SleOspfv3ControlRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 7),
    _SleOspfv3ControlRestartPeriod_Type()
)
sleOspfv3ControlRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ControlRestartPeriod.setStatus("current")


class _SleOspfv3ControlRestartHelperPolicy_Type(Integer32):
    """Custom type sleOspfv3ControlRestartHelperPolicy based on Integer32"""
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
        *(("unspec", 0),
          ("never", 1),
          ("onlyReload", 2),
          ("onlyUpgrade", 3),
          ("reloadUpgrade", 4))
    )


_SleOspfv3ControlRestartHelperPolicy_Type.__name__ = "Integer32"
_SleOspfv3ControlRestartHelperPolicy_Object = MibScalar
sleOspfv3ControlRestartHelperPolicy = _SleOspfv3ControlRestartHelperPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 8),
    _SleOspfv3ControlRestartHelperPolicy_Type()
)
sleOspfv3ControlRestartHelperPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ControlRestartHelperPolicy.setStatus("current")


class _SleOspfv3ControlRestartHelperPeriod_Type(Integer32):
    """Custom type sleOspfv3ControlRestartHelperPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOspfv3ControlRestartHelperPeriod_Type.__name__ = "Integer32"
_SleOspfv3ControlRestartHelperPeriod_Object = MibScalar
sleOspfv3ControlRestartHelperPeriod = _SleOspfv3ControlRestartHelperPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 9),
    _SleOspfv3ControlRestartHelperPeriod_Type()
)
sleOspfv3ControlRestartHelperPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ControlRestartHelperPeriod.setStatus("current")


class _SleOspfv3ControlSnmpNotification_Type(Integer32):
    """Custom type sleOspfv3ControlSnmpNotification based on Integer32"""
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


_SleOspfv3ControlSnmpNotification_Type.__name__ = "Integer32"
_SleOspfv3ControlSnmpNotification_Object = MibScalar
sleOspfv3ControlSnmpNotification = _SleOspfv3ControlSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 2, 10),
    _SleOspfv3ControlSnmpNotification_Type()
)
sleOspfv3ControlSnmpNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ControlSnmpNotification.setStatus("current")
_SleOspfv3BaseNotification_ObjectIdentity = ObjectIdentity
sleOspfv3BaseNotification = _SleOspfv3BaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 3)
)
_SleOspfv3Proc_ObjectIdentity = ObjectIdentity
sleOspfv3Proc = _SleOspfv3Proc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2)
)
_SleOspfv3ProcInfo_ObjectIdentity = ObjectIdentity
sleOspfv3ProcInfo = _SleOspfv3ProcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1)
)
_SleOspfv3ProcInfoTable_Object = MibTable
sleOspfv3ProcInfoTable = _SleOspfv3ProcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3ProcInfoTable.setStatus("current")
_SleOspfv3ProcInfoEntry_Object = MibTableRow
sleOspfv3ProcInfoEntry = _SleOspfv3ProcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1)
)
sleOspfv3ProcInfoEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
)
if mibBuilder.loadTexts:
    sleOspfv3ProcInfoEntry.setStatus("current")


class _SleOspfv3ProcIndex_Type(Integer32):
    """Custom type sleOspfv3ProcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleOspfv3ProcIndex_Type.__name__ = "Integer32"
_SleOspfv3ProcIndex_Object = MibTableColumn
sleOspfv3ProcIndex = _SleOspfv3ProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 1),
    _SleOspfv3ProcIndex_Type()
)
sleOspfv3ProcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcIndex.setStatus("current")


class _SleOspfv3ProcTag_Type(OctetString):
    """Custom type sleOspfv3ProcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3ProcTag_Type.__name__ = "OctetString"
_SleOspfv3ProcTag_Object = MibTableColumn
sleOspfv3ProcTag = _SleOspfv3ProcTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 2),
    _SleOspfv3ProcTag_Type()
)
sleOspfv3ProcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcTag.setStatus("current")
_SleOspfv3ProcRouterId_Type = InetAddressIPv4
_SleOspfv3ProcRouterId_Object = MibTableColumn
sleOspfv3ProcRouterId = _SleOspfv3ProcRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 3),
    _SleOspfv3ProcRouterId_Type()
)
sleOspfv3ProcRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcRouterId.setStatus("current")


class _SleOspfv3ProcSpfDelayTime_Type(Integer32):
    """Custom type sleOspfv3ProcSpfDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOspfv3ProcSpfDelayTime_Type.__name__ = "Integer32"
_SleOspfv3ProcSpfDelayTime_Object = MibTableColumn
sleOspfv3ProcSpfDelayTime = _SleOspfv3ProcSpfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 4),
    _SleOspfv3ProcSpfDelayTime_Type()
)
sleOspfv3ProcSpfDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSpfDelayTime.setStatus("current")


class _SleOspfv3ProcSpfHoldTime_Type(Integer32):
    """Custom type sleOspfv3ProcSpfHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOspfv3ProcSpfHoldTime_Type.__name__ = "Integer32"
_SleOspfv3ProcSpfHoldTime_Object = MibTableColumn
sleOspfv3ProcSpfHoldTime = _SleOspfv3ProcSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 5),
    _SleOspfv3ProcSpfHoldTime_Type()
)
sleOspfv3ProcSpfHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSpfHoldTime.setStatus("current")


class _SleOspfv3ProcAutoCost_Type(Integer32):
    """Custom type sleOspfv3ProcAutoCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967),
    )


_SleOspfv3ProcAutoCost_Type.__name__ = "Integer32"
_SleOspfv3ProcAutoCost_Object = MibTableColumn
sleOspfv3ProcAutoCost = _SleOspfv3ProcAutoCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 6),
    _SleOspfv3ProcAutoCost_Type()
)
sleOspfv3ProcAutoCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAutoCost.setStatus("current")


class _SleOspfv3ProcAbrType_Type(Integer32):
    """Custom type sleOspfv3ProcAbrType based on Integer32"""
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
          ("standard", 1),
          ("cisco", 2),
          ("ibm", 3),
          ("shortcut", 4))
    )


_SleOspfv3ProcAbrType_Type.__name__ = "Integer32"
_SleOspfv3ProcAbrType_Object = MibTableColumn
sleOspfv3ProcAbrType = _SleOspfv3ProcAbrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 7),
    _SleOspfv3ProcAbrType_Type()
)
sleOspfv3ProcAbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAbrType.setStatus("current")


class _SleOspfv3ProcDefaultMetric_Type(Integer32):
    """Custom type sleOspfv3ProcDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleOspfv3ProcDefaultMetric_Type.__name__ = "Integer32"
_SleOspfv3ProcDefaultMetric_Object = MibTableColumn
sleOspfv3ProcDefaultMetric = _SleOspfv3ProcDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 8),
    _SleOspfv3ProcDefaultMetric_Type()
)
sleOspfv3ProcDefaultMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcDefaultMetric.setStatus("current")


class _SleOspfv3ProcMaxConcurrentDD_Type(Integer32):
    """Custom type sleOspfv3ProcMaxConcurrentDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcMaxConcurrentDD_Type.__name__ = "Integer32"
_SleOspfv3ProcMaxConcurrentDD_Object = MibTableColumn
sleOspfv3ProcMaxConcurrentDD = _SleOspfv3ProcMaxConcurrentDD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 9),
    _SleOspfv3ProcMaxConcurrentDD_Type()
)
sleOspfv3ProcMaxConcurrentDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcMaxConcurrentDD.setStatus("current")


class _SleOspfv3ProcDefaultOriginType_Type(Integer32):
    """Custom type sleOspfv3ProcDefaultOriginType based on Integer32"""
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
          ("normal", 1),
          ("always", 2))
    )


_SleOspfv3ProcDefaultOriginType_Type.__name__ = "Integer32"
_SleOspfv3ProcDefaultOriginType_Object = MibTableColumn
sleOspfv3ProcDefaultOriginType = _SleOspfv3ProcDefaultOriginType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 10),
    _SleOspfv3ProcDefaultOriginType_Type()
)
sleOspfv3ProcDefaultOriginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcDefaultOriginType.setStatus("current")


class _SleOspfv3ProcDefaultOriginMetricType_Type(Integer32):
    """Custom type sleOspfv3ProcDefaultOriginMetricType based on Integer32"""
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
          ("external1", 1),
          ("external2", 2))
    )


_SleOspfv3ProcDefaultOriginMetricType_Type.__name__ = "Integer32"
_SleOspfv3ProcDefaultOriginMetricType_Object = MibTableColumn
sleOspfv3ProcDefaultOriginMetricType = _SleOspfv3ProcDefaultOriginMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 11),
    _SleOspfv3ProcDefaultOriginMetricType_Type()
)
sleOspfv3ProcDefaultOriginMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcDefaultOriginMetricType.setStatus("current")


class _SleOspfv3ProcDefaultOriginMetric_Type(Integer32):
    """Custom type sleOspfv3ProcDefaultOriginMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOspfv3ProcDefaultOriginMetric_Type.__name__ = "Integer32"
_SleOspfv3ProcDefaultOriginMetric_Object = MibTableColumn
sleOspfv3ProcDefaultOriginMetric = _SleOspfv3ProcDefaultOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 12),
    _SleOspfv3ProcDefaultOriginMetric_Type()
)
sleOspfv3ProcDefaultOriginMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcDefaultOriginMetric.setStatus("current")


class _SleOspfv3ProcDefaultOriginRouteMap_Type(OctetString):
    """Custom type sleOspfv3ProcDefaultOriginRouteMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3ProcDefaultOriginRouteMap_Type.__name__ = "OctetString"
_SleOspfv3ProcDefaultOriginRouteMap_Object = MibTableColumn
sleOspfv3ProcDefaultOriginRouteMap = _SleOspfv3ProcDefaultOriginRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 13),
    _SleOspfv3ProcDefaultOriginRouteMap_Type()
)
sleOspfv3ProcDefaultOriginRouteMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcDefaultOriginRouteMap.setStatus("current")


class _SleOspfv3ProcLogNeighborChange_Type(Integer32):
    """Custom type sleOspfv3ProcLogNeighborChange based on Integer32"""
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


_SleOspfv3ProcLogNeighborChange_Type.__name__ = "Integer32"
_SleOspfv3ProcLogNeighborChange_Object = MibTableColumn
sleOspfv3ProcLogNeighborChange = _SleOspfv3ProcLogNeighborChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 14),
    _SleOspfv3ProcLogNeighborChange_Type()
)
sleOspfv3ProcLogNeighborChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcLogNeighborChange.setStatus("current")


class _SleOspfv3ProcBfdAllIf_Type(Integer32):
    """Custom type sleOspfv3ProcBfdAllIf based on Integer32"""
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


_SleOspfv3ProcBfdAllIf_Type.__name__ = "Integer32"
_SleOspfv3ProcBfdAllIf_Object = MibTableColumn
sleOspfv3ProcBfdAllIf = _SleOspfv3ProcBfdAllIf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 15),
    _SleOspfv3ProcBfdAllIf_Type()
)
sleOspfv3ProcBfdAllIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcBfdAllIf.setStatus("current")


class _SleOspfv3ProcEfmAllIf_Type(Integer32):
    """Custom type sleOspfv3ProcEfmAllIf based on Integer32"""
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


_SleOspfv3ProcEfmAllIf_Type.__name__ = "Integer32"
_SleOspfv3ProcEfmAllIf_Object = MibTableColumn
sleOspfv3ProcEfmAllIf = _SleOspfv3ProcEfmAllIf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 16),
    _SleOspfv3ProcEfmAllIf_Type()
)
sleOspfv3ProcEfmAllIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcEfmAllIf.setStatus("current")


class _SleOspfv3ProcVRIndex_Type(Integer32):
    """Custom type sleOspfv3ProcVRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleOspfv3ProcVRIndex_Type.__name__ = "Integer32"
_SleOspfv3ProcVRIndex_Object = MibTableColumn
sleOspfv3ProcVRIndex = _SleOspfv3ProcVRIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 17),
    _SleOspfv3ProcVRIndex_Type()
)
sleOspfv3ProcVRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcVRIndex.setStatus("current")


class _SleOspfv3ProcVRFName_Type(OctetString):
    """Custom type sleOspfv3ProcVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleOspfv3ProcVRFName_Type.__name__ = "OctetString"
_SleOspfv3ProcVRFName_Object = MibTableColumn
sleOspfv3ProcVRFName = _SleOspfv3ProcVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 18),
    _SleOspfv3ProcVRFName_Type()
)
sleOspfv3ProcVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcVRFName.setStatus("current")


class _SleOspfv3ProcSPFStartDelay_Type(Integer32):
    """Custom type sleOspfv3ProcSPFStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcSPFStartDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcSPFStartDelay_Object = MibTableColumn
sleOspfv3ProcSPFStartDelay = _SleOspfv3ProcSPFStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 19),
    _SleOspfv3ProcSPFStartDelay_Type()
)
sleOspfv3ProcSPFStartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSPFStartDelay.setStatus("current")


class _SleOspfv3ProcSPFMinDelay_Type(Integer32):
    """Custom type sleOspfv3ProcSPFMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcSPFMinDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcSPFMinDelay_Object = MibTableColumn
sleOspfv3ProcSPFMinDelay = _SleOspfv3ProcSPFMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 20),
    _SleOspfv3ProcSPFMinDelay_Type()
)
sleOspfv3ProcSPFMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSPFMinDelay.setStatus("current")


class _SleOspfv3ProcSPFMaxDelay_Type(Integer32):
    """Custom type sleOspfv3ProcSPFMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcSPFMaxDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcSPFMaxDelay_Object = MibTableColumn
sleOspfv3ProcSPFMaxDelay = _SleOspfv3ProcSPFMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 21),
    _SleOspfv3ProcSPFMaxDelay_Type()
)
sleOspfv3ProcSPFMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSPFMaxDelay.setStatus("current")


class _SleOspfv3ProcLSAStartDelay_Type(Integer32):
    """Custom type sleOspfv3ProcLSAStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcLSAStartDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcLSAStartDelay_Object = MibTableColumn
sleOspfv3ProcLSAStartDelay = _SleOspfv3ProcLSAStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 22),
    _SleOspfv3ProcLSAStartDelay_Type()
)
sleOspfv3ProcLSAStartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcLSAStartDelay.setStatus("current")


class _SleOspfv3ProcLSAMinDelay_Type(Integer32):
    """Custom type sleOspfv3ProcLSAMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcLSAMinDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcLSAMinDelay_Object = MibTableColumn
sleOspfv3ProcLSAMinDelay = _SleOspfv3ProcLSAMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 23),
    _SleOspfv3ProcLSAMinDelay_Type()
)
sleOspfv3ProcLSAMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcLSAMinDelay.setStatus("current")


class _SleOspfv3ProcLSAMaxDelay_Type(Integer32):
    """Custom type sleOspfv3ProcLSAMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcLSAMaxDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcLSAMaxDelay_Object = MibTableColumn
sleOspfv3ProcLSAMaxDelay = _SleOspfv3ProcLSAMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 24),
    _SleOspfv3ProcLSAMaxDelay_Type()
)
sleOspfv3ProcLSAMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcLSAMaxDelay.setStatus("current")


class _SleOspfv3ProcLSAArrivalDelay_Type(Integer32):
    """Custom type sleOspfv3ProcLSAArrivalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcLSAArrivalDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcLSAArrivalDelay_Object = MibTableColumn
sleOspfv3ProcLSAArrivalDelay = _SleOspfv3ProcLSAArrivalDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 1, 1, 25),
    _SleOspfv3ProcLSAArrivalDelay_Type()
)
sleOspfv3ProcLSAArrivalDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcLSAArrivalDelay.setStatus("current")
_SleOspfv3ProcInfoControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcInfoControl = _SleOspfv3ProcInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2)
)


class _SleOspfv3ProcControlRequest_Type(Integer32):
    """Custom type sleOspfv3ProcControlRequest based on Integer32"""
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
        *(("createOspfv3Proc", 1),
          ("setOspfv3Proc", 2),
          ("destroyOspfv3Proc", 3),
          ("clearOspfv3Proc", 4))
    )


_SleOspfv3ProcControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ProcControlRequest_Object = MibScalar
sleOspfv3ProcControlRequest = _SleOspfv3ProcControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 1),
    _SleOspfv3ProcControlRequest_Type()
)
sleOspfv3ProcControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlRequest.setStatus("current")
_SleOspfv3ProcControlStatus_Type = SleControlStatusType
_SleOspfv3ProcControlStatus_Object = MibScalar
sleOspfv3ProcControlStatus = _SleOspfv3ProcControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 2),
    _SleOspfv3ProcControlStatus_Type()
)
sleOspfv3ProcControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlStatus.setStatus("current")
_SleOspfv3ProcControlTimer_Type = Gauge32
_SleOspfv3ProcControlTimer_Object = MibScalar
sleOspfv3ProcControlTimer = _SleOspfv3ProcControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 3),
    _SleOspfv3ProcControlTimer_Type()
)
sleOspfv3ProcControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlTimer.setStatus("current")
_SleOspfv3ProcControlTimeStamp_Type = TimeTicks
_SleOspfv3ProcControlTimeStamp_Object = MibScalar
sleOspfv3ProcControlTimeStamp = _SleOspfv3ProcControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 4),
    _SleOspfv3ProcControlTimeStamp_Type()
)
sleOspfv3ProcControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlTimeStamp.setStatus("current")
_SleOspfv3ProcControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ProcControlReqResult_Object = MibScalar
sleOspfv3ProcControlReqResult = _SleOspfv3ProcControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 5),
    _SleOspfv3ProcControlReqResult_Type()
)
sleOspfv3ProcControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlReqResult.setStatus("current")
_SleOspfv3ProcControlIndex_Type = Integer32
_SleOspfv3ProcControlIndex_Object = MibScalar
sleOspfv3ProcControlIndex = _SleOspfv3ProcControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 6),
    _SleOspfv3ProcControlIndex_Type()
)
sleOspfv3ProcControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlIndex.setStatus("current")


class _SleOspfv3ProcControlTag_Type(OctetString):
    """Custom type sleOspfv3ProcControlTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3ProcControlTag_Type.__name__ = "OctetString"
_SleOspfv3ProcControlTag_Object = MibScalar
sleOspfv3ProcControlTag = _SleOspfv3ProcControlTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 7),
    _SleOspfv3ProcControlTag_Type()
)
sleOspfv3ProcControlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlTag.setStatus("current")
_SleOspfv3ProcControlRouterId_Type = InetAddressIPv4
_SleOspfv3ProcControlRouterId_Object = MibScalar
sleOspfv3ProcControlRouterId = _SleOspfv3ProcControlRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 8),
    _SleOspfv3ProcControlRouterId_Type()
)
sleOspfv3ProcControlRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlRouterId.setStatus("current")


class _SleOspfv3ProcControlSpfDelayTime_Type(Integer32):
    """Custom type sleOspfv3ProcControlSpfDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOspfv3ProcControlSpfDelayTime_Type.__name__ = "Integer32"
_SleOspfv3ProcControlSpfDelayTime_Object = MibScalar
sleOspfv3ProcControlSpfDelayTime = _SleOspfv3ProcControlSpfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 9),
    _SleOspfv3ProcControlSpfDelayTime_Type()
)
sleOspfv3ProcControlSpfDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlSpfDelayTime.setStatus("current")


class _SleOspfv3ProcControlSpfHoldTime_Type(Integer32):
    """Custom type sleOspfv3ProcControlSpfHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOspfv3ProcControlSpfHoldTime_Type.__name__ = "Integer32"
_SleOspfv3ProcControlSpfHoldTime_Object = MibScalar
sleOspfv3ProcControlSpfHoldTime = _SleOspfv3ProcControlSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 10),
    _SleOspfv3ProcControlSpfHoldTime_Type()
)
sleOspfv3ProcControlSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlSpfHoldTime.setStatus("current")


class _SleOspfv3ProcControlAutoCost_Type(Integer32):
    """Custom type sleOspfv3ProcControlAutoCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967),
    )


_SleOspfv3ProcControlAutoCost_Type.__name__ = "Integer32"
_SleOspfv3ProcControlAutoCost_Object = MibScalar
sleOspfv3ProcControlAutoCost = _SleOspfv3ProcControlAutoCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 11),
    _SleOspfv3ProcControlAutoCost_Type()
)
sleOspfv3ProcControlAutoCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlAutoCost.setStatus("current")


class _SleOspfv3ProcControlAbrType_Type(Integer32):
    """Custom type sleOspfv3ProcControlAbrType based on Integer32"""
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
          ("standard", 1),
          ("cisco", 2),
          ("ibm", 3),
          ("shortcut", 4))
    )


_SleOspfv3ProcControlAbrType_Type.__name__ = "Integer32"
_SleOspfv3ProcControlAbrType_Object = MibScalar
sleOspfv3ProcControlAbrType = _SleOspfv3ProcControlAbrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 12),
    _SleOspfv3ProcControlAbrType_Type()
)
sleOspfv3ProcControlAbrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlAbrType.setStatus("current")


class _SleOspfv3ProcControlDefaultMetric_Type(Integer32):
    """Custom type sleOspfv3ProcControlDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleOspfv3ProcControlDefaultMetric_Type.__name__ = "Integer32"
_SleOspfv3ProcControlDefaultMetric_Object = MibScalar
sleOspfv3ProcControlDefaultMetric = _SleOspfv3ProcControlDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 13),
    _SleOspfv3ProcControlDefaultMetric_Type()
)
sleOspfv3ProcControlDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlDefaultMetric.setStatus("current")


class _SleOspfv3ProcControlMaxConcurrentDD_Type(Integer32):
    """Custom type sleOspfv3ProcControlMaxConcurrentDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcControlMaxConcurrentDD_Type.__name__ = "Integer32"
_SleOspfv3ProcControlMaxConcurrentDD_Object = MibScalar
sleOspfv3ProcControlMaxConcurrentDD = _SleOspfv3ProcControlMaxConcurrentDD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 14),
    _SleOspfv3ProcControlMaxConcurrentDD_Type()
)
sleOspfv3ProcControlMaxConcurrentDD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlMaxConcurrentDD.setStatus("current")


class _SleOspfv3ProcControlDefaultOriginType_Type(Integer32):
    """Custom type sleOspfv3ProcControlDefaultOriginType based on Integer32"""
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
          ("normal", 1),
          ("always", 2))
    )


_SleOspfv3ProcControlDefaultOriginType_Type.__name__ = "Integer32"
_SleOspfv3ProcControlDefaultOriginType_Object = MibScalar
sleOspfv3ProcControlDefaultOriginType = _SleOspfv3ProcControlDefaultOriginType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 15),
    _SleOspfv3ProcControlDefaultOriginType_Type()
)
sleOspfv3ProcControlDefaultOriginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlDefaultOriginType.setStatus("current")


class _SleOspfv3ProcControlDefaultOriginMetricType_Type(Integer32):
    """Custom type sleOspfv3ProcControlDefaultOriginMetricType based on Integer32"""
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
          ("external1", 1),
          ("external2", 2))
    )


_SleOspfv3ProcControlDefaultOriginMetricType_Type.__name__ = "Integer32"
_SleOspfv3ProcControlDefaultOriginMetricType_Object = MibScalar
sleOspfv3ProcControlDefaultOriginMetricType = _SleOspfv3ProcControlDefaultOriginMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 16),
    _SleOspfv3ProcControlDefaultOriginMetricType_Type()
)
sleOspfv3ProcControlDefaultOriginMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlDefaultOriginMetricType.setStatus("current")


class _SleOspfv3ProcControlDefaultOriginMetric_Type(Integer32):
    """Custom type sleOspfv3ProcControlDefaultOriginMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOspfv3ProcControlDefaultOriginMetric_Type.__name__ = "Integer32"
_SleOspfv3ProcControlDefaultOriginMetric_Object = MibScalar
sleOspfv3ProcControlDefaultOriginMetric = _SleOspfv3ProcControlDefaultOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 17),
    _SleOspfv3ProcControlDefaultOriginMetric_Type()
)
sleOspfv3ProcControlDefaultOriginMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlDefaultOriginMetric.setStatus("current")


class _SleOspfv3ProcControlDefaultOriginRouteMap_Type(OctetString):
    """Custom type sleOspfv3ProcControlDefaultOriginRouteMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3ProcControlDefaultOriginRouteMap_Type.__name__ = "OctetString"
_SleOspfv3ProcControlDefaultOriginRouteMap_Object = MibScalar
sleOspfv3ProcControlDefaultOriginRouteMap = _SleOspfv3ProcControlDefaultOriginRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 18),
    _SleOspfv3ProcControlDefaultOriginRouteMap_Type()
)
sleOspfv3ProcControlDefaultOriginRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlDefaultOriginRouteMap.setStatus("current")


class _SleOspfv3ProcControlLogNeighborChange_Type(Integer32):
    """Custom type sleOspfv3ProcControlLogNeighborChange based on Integer32"""
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


_SleOspfv3ProcControlLogNeighborChange_Type.__name__ = "Integer32"
_SleOspfv3ProcControlLogNeighborChange_Object = MibScalar
sleOspfv3ProcControlLogNeighborChange = _SleOspfv3ProcControlLogNeighborChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 19),
    _SleOspfv3ProcControlLogNeighborChange_Type()
)
sleOspfv3ProcControlLogNeighborChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlLogNeighborChange.setStatus("current")


class _SleOspfv3ProcControlBfdAllIf_Type(Integer32):
    """Custom type sleOspfv3ProcControlBfdAllIf based on Integer32"""
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


_SleOspfv3ProcControlBfdAllIf_Type.__name__ = "Integer32"
_SleOspfv3ProcControlBfdAllIf_Object = MibScalar
sleOspfv3ProcControlBfdAllIf = _SleOspfv3ProcControlBfdAllIf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 20),
    _SleOspfv3ProcControlBfdAllIf_Type()
)
sleOspfv3ProcControlBfdAllIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlBfdAllIf.setStatus("current")


class _SleOspfv3ProcControlEfmAllIf_Type(Integer32):
    """Custom type sleOspfv3ProcControlEfmAllIf based on Integer32"""
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


_SleOspfv3ProcControlEfmAllIf_Type.__name__ = "Integer32"
_SleOspfv3ProcControlEfmAllIf_Object = MibScalar
sleOspfv3ProcControlEfmAllIf = _SleOspfv3ProcControlEfmAllIf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 21),
    _SleOspfv3ProcControlEfmAllIf_Type()
)
sleOspfv3ProcControlEfmAllIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlEfmAllIf.setStatus("current")
_SleOspfv3ProcControlVRIndex_Type = Integer32
_SleOspfv3ProcControlVRIndex_Object = MibScalar
sleOspfv3ProcControlVRIndex = _SleOspfv3ProcControlVRIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 22),
    _SleOspfv3ProcControlVRIndex_Type()
)
sleOspfv3ProcControlVRIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlVRIndex.setStatus("current")


class _SleOspfv3ProcControlVRFName_Type(OctetString):
    """Custom type sleOspfv3ProcControlVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3ProcControlVRFName_Type.__name__ = "OctetString"
_SleOspfv3ProcControlVRFName_Object = MibScalar
sleOspfv3ProcControlVRFName = _SleOspfv3ProcControlVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 23),
    _SleOspfv3ProcControlVRFName_Type()
)
sleOspfv3ProcControlVRFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlVRFName.setStatus("current")


class _SleOspfv3ProcControlSPFStartDelay_Type(Integer32):
    """Custom type sleOspfv3ProcControlSPFStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcControlSPFStartDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcControlSPFStartDelay_Object = MibScalar
sleOspfv3ProcControlSPFStartDelay = _SleOspfv3ProcControlSPFStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 24),
    _SleOspfv3ProcControlSPFStartDelay_Type()
)
sleOspfv3ProcControlSPFStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlSPFStartDelay.setStatus("current")


class _SleOspfv3ProcControlSPFMinDelay_Type(Integer32):
    """Custom type sleOspfv3ProcControlSPFMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcControlSPFMinDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcControlSPFMinDelay_Object = MibScalar
sleOspfv3ProcControlSPFMinDelay = _SleOspfv3ProcControlSPFMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 25),
    _SleOspfv3ProcControlSPFMinDelay_Type()
)
sleOspfv3ProcControlSPFMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlSPFMinDelay.setStatus("current")


class _SleOspfv3ProcControlSPFMaxDelay_Type(Integer32):
    """Custom type sleOspfv3ProcControlSPFMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcControlSPFMaxDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcControlSPFMaxDelay_Object = MibScalar
sleOspfv3ProcControlSPFMaxDelay = _SleOspfv3ProcControlSPFMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 26),
    _SleOspfv3ProcControlSPFMaxDelay_Type()
)
sleOspfv3ProcControlSPFMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlSPFMaxDelay.setStatus("current")


class _SleOspfv3ProcControlLSAStartDelay_Type(Integer32):
    """Custom type sleOspfv3ProcControlLSAStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcControlLSAStartDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcControlLSAStartDelay_Object = MibScalar
sleOspfv3ProcControlLSAStartDelay = _SleOspfv3ProcControlLSAStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 27),
    _SleOspfv3ProcControlLSAStartDelay_Type()
)
sleOspfv3ProcControlLSAStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlLSAStartDelay.setStatus("current")


class _SleOspfv3ProcControlLSAMinDelay_Type(Integer32):
    """Custom type sleOspfv3ProcControlLSAMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcControlLSAMinDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcControlLSAMinDelay_Object = MibScalar
sleOspfv3ProcControlLSAMinDelay = _SleOspfv3ProcControlLSAMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 28),
    _SleOspfv3ProcControlLSAMinDelay_Type()
)
sleOspfv3ProcControlLSAMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlLSAMinDelay.setStatus("current")


class _SleOspfv3ProcControlLSAMaxDelay_Type(Integer32):
    """Custom type sleOspfv3ProcControlLSAMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcControlLSAMaxDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcControlLSAMaxDelay_Object = MibScalar
sleOspfv3ProcControlLSAMaxDelay = _SleOspfv3ProcControlLSAMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 29),
    _SleOspfv3ProcControlLSAMaxDelay_Type()
)
sleOspfv3ProcControlLSAMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlLSAMaxDelay.setStatus("current")


class _SleOspfv3ProcControlLSAArrivalDelay_Type(Integer32):
    """Custom type sleOspfv3ProcControlLSAArrivalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOspfv3ProcControlLSAArrivalDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcControlLSAArrivalDelay_Object = MibScalar
sleOspfv3ProcControlLSAArrivalDelay = _SleOspfv3ProcControlLSAArrivalDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 2, 30),
    _SleOspfv3ProcControlLSAArrivalDelay_Type()
)
sleOspfv3ProcControlLSAArrivalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcControlLSAArrivalDelay.setStatus("current")
_SleOspfv3ProcInfoNotification_ObjectIdentity = ObjectIdentity
sleOspfv3ProcInfoNotification = _SleOspfv3ProcInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 3)
)
_SleOspfv3ProcSummary_ObjectIdentity = ObjectIdentity
sleOspfv3ProcSummary = _SleOspfv3ProcSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2)
)
_SleOspfv3ProcSummaryTable_Object = MibTable
sleOspfv3ProcSummaryTable = _SleOspfv3ProcSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryTable.setStatus("current")
_SleOspfv3ProcSummaryEntry_Object = MibTableRow
sleOspfv3ProcSummaryEntry = _SleOspfv3ProcSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 1, 1)
)
sleOspfv3ProcSummaryEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryAddress"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryMask"),
)
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryEntry.setStatus("current")
_SleOspfv3ProcSummaryAddress_Type = InetAddressIPv6
_SleOspfv3ProcSummaryAddress_Object = MibTableColumn
sleOspfv3ProcSummaryAddress = _SleOspfv3ProcSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 1, 1, 1),
    _SleOspfv3ProcSummaryAddress_Type()
)
sleOspfv3ProcSummaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryAddress.setStatus("current")


class _SleOspfv3ProcSummaryMask_Type(Integer32):
    """Custom type sleOspfv3ProcSummaryMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleOspfv3ProcSummaryMask_Type.__name__ = "Integer32"
_SleOspfv3ProcSummaryMask_Object = MibTableColumn
sleOspfv3ProcSummaryMask = _SleOspfv3ProcSummaryMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 1, 1, 2),
    _SleOspfv3ProcSummaryMask_Type()
)
sleOspfv3ProcSummaryMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryMask.setStatus("current")


class _SleOspfv3ProcSummaryTag_Type(Gauge32):
    """Custom type sleOspfv3ProcSummaryTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleOspfv3ProcSummaryTag_Type.__name__ = "Gauge32"
_SleOspfv3ProcSummaryTag_Object = MibTableColumn
sleOspfv3ProcSummaryTag = _SleOspfv3ProcSummaryTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 1, 1, 3),
    _SleOspfv3ProcSummaryTag_Type()
)
sleOspfv3ProcSummaryTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryTag.setStatus("current")


class _SleOspfv3ProcSummaryAdvertiseFlag_Type(Integer32):
    """Custom type sleOspfv3ProcSummaryAdvertiseFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAdvertise", 0),
          ("tag", 1))
    )


_SleOspfv3ProcSummaryAdvertiseFlag_Type.__name__ = "Integer32"
_SleOspfv3ProcSummaryAdvertiseFlag_Object = MibTableColumn
sleOspfv3ProcSummaryAdvertiseFlag = _SleOspfv3ProcSummaryAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 1, 1, 4),
    _SleOspfv3ProcSummaryAdvertiseFlag_Type()
)
sleOspfv3ProcSummaryAdvertiseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryAdvertiseFlag.setStatus("current")
_SleOspfv3rocSummaryControl_ObjectIdentity = ObjectIdentity
sleOspfv3rocSummaryControl = _SleOspfv3rocSummaryControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2)
)


class _SleOspfv3ProcSummaryControlRequest_Type(Integer32):
    """Custom type sleOspfv3ProcSummaryControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOpsfv3ProcSummary", 1),
          ("modifyOspfv3ProcSummary", 2),
          ("delstroyOspfv3ProcSummary", 3))
    )


_SleOspfv3ProcSummaryControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ProcSummaryControlRequest_Object = MibScalar
sleOspfv3ProcSummaryControlRequest = _SleOspfv3ProcSummaryControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 1),
    _SleOspfv3ProcSummaryControlRequest_Type()
)
sleOspfv3ProcSummaryControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlRequest.setStatus("current")
_SleOspfv3ProcSummaryControlStatus_Type = SleControlStatusType
_SleOspfv3ProcSummaryControlStatus_Object = MibScalar
sleOspfv3ProcSummaryControlStatus = _SleOspfv3ProcSummaryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 2),
    _SleOspfv3ProcSummaryControlStatus_Type()
)
sleOspfv3ProcSummaryControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlStatus.setStatus("current")
_SleOspfv3ProcSummaryControlTimer_Type = Gauge32
_SleOspfv3ProcSummaryControlTimer_Object = MibScalar
sleOspfv3ProcSummaryControlTimer = _SleOspfv3ProcSummaryControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 3),
    _SleOspfv3ProcSummaryControlTimer_Type()
)
sleOspfv3ProcSummaryControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlTimer.setStatus("current")
_SleOspfv3ProcSummaryControlTimeStamp_Type = TimeTicks
_SleOspfv3ProcSummaryControlTimeStamp_Object = MibScalar
sleOspfv3ProcSummaryControlTimeStamp = _SleOspfv3ProcSummaryControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 4),
    _SleOspfv3ProcSummaryControlTimeStamp_Type()
)
sleOspfv3ProcSummaryControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlTimeStamp.setStatus("current")
_SleOspfv3ProcSummaryControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ProcSummaryControlReqResult_Object = MibScalar
sleOspfv3ProcSummaryControlReqResult = _SleOspfv3ProcSummaryControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 5),
    _SleOspfv3ProcSummaryControlReqResult_Type()
)
sleOspfv3ProcSummaryControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlReqResult.setStatus("current")
_SleOspfv3ProcSummaryControlIndex_Type = Integer32
_SleOspfv3ProcSummaryControlIndex_Object = MibScalar
sleOspfv3ProcSummaryControlIndex = _SleOspfv3ProcSummaryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 6),
    _SleOspfv3ProcSummaryControlIndex_Type()
)
sleOspfv3ProcSummaryControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlIndex.setStatus("current")
_SleOspfv3ProcSummaryControlAddress_Type = InetAddressIPv6
_SleOspfv3ProcSummaryControlAddress_Object = MibScalar
sleOspfv3ProcSummaryControlAddress = _SleOspfv3ProcSummaryControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 7),
    _SleOspfv3ProcSummaryControlAddress_Type()
)
sleOspfv3ProcSummaryControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlAddress.setStatus("current")


class _SleOspfv3ProcSummaryControlMask_Type(Integer32):
    """Custom type sleOspfv3ProcSummaryControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleOspfv3ProcSummaryControlMask_Type.__name__ = "Integer32"
_SleOspfv3ProcSummaryControlMask_Object = MibScalar
sleOspfv3ProcSummaryControlMask = _SleOspfv3ProcSummaryControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 8),
    _SleOspfv3ProcSummaryControlMask_Type()
)
sleOspfv3ProcSummaryControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlMask.setStatus("current")


class _SleOspfv3ProcSummaryControlTag_Type(Gauge32):
    """Custom type sleOspfv3ProcSummaryControlTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleOspfv3ProcSummaryControlTag_Type.__name__ = "Gauge32"
_SleOspfv3ProcSummaryControlTag_Object = MibScalar
sleOspfv3ProcSummaryControlTag = _SleOspfv3ProcSummaryControlTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 9),
    _SleOspfv3ProcSummaryControlTag_Type()
)
sleOspfv3ProcSummaryControlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlTag.setStatus("current")


class _SleOspfv3ProcSummaryControlAdvertiseFlag_Type(Integer32):
    """Custom type sleOspfv3ProcSummaryControlAdvertiseFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAdvertise", 0),
          ("tag", 1))
    )


_SleOspfv3ProcSummaryControlAdvertiseFlag_Type.__name__ = "Integer32"
_SleOspfv3ProcSummaryControlAdvertiseFlag_Object = MibScalar
sleOspfv3ProcSummaryControlAdvertiseFlag = _SleOspfv3ProcSummaryControlAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 2, 10),
    _SleOspfv3ProcSummaryControlAdvertiseFlag_Type()
)
sleOspfv3ProcSummaryControlAdvertiseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryControlAdvertiseFlag.setStatus("current")
_SleOspfv3ProcSummaryNotification_ObjectIdentity = ObjectIdentity
sleOspfv3ProcSummaryNotification = _SleOspfv3ProcSummaryNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 3)
)
_SleOspfv3ProcPassiveIf_ObjectIdentity = ObjectIdentity
sleOspfv3ProcPassiveIf = _SleOspfv3ProcPassiveIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3)
)
_SleOspfv3ProcPassiveIfTable_Object = MibTable
sleOspfv3ProcPassiveIfTable = _SleOspfv3ProcPassiveIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfTable.setStatus("current")
_SleOspfv3ProcPassiveIfEntry_Object = MibTableRow
sleOspfv3ProcPassiveIfEntry = _SleOspfv3ProcPassiveIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 1, 1)
)
sleOspfv3ProcPassiveIfEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfIndex"),
)
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfEntry.setStatus("current")


class _SleOspfv3ProcPassiveIfIndex_Type(Integer32):
    """Custom type sleOspfv3ProcPassiveIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleOspfv3ProcPassiveIfIndex_Type.__name__ = "Integer32"
_SleOspfv3ProcPassiveIfIndex_Object = MibTableColumn
sleOspfv3ProcPassiveIfIndex = _SleOspfv3ProcPassiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 1, 1, 1),
    _SleOspfv3ProcPassiveIfIndex_Type()
)
sleOspfv3ProcPassiveIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfIndex.setStatus("current")
_SleOspfv3ProcPassIfControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcPassIfControl = _SleOspfv3ProcPassIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2)
)


class _SleOspfv3ProcPassiveIfControlRequest_Type(Integer32):
    """Custom type sleOspfv3ProcPassiveIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addOspfv3ProcPassiveIf", 1),
          ("deleteOspfv3ProcPassiveIf", 2))
    )


_SleOspfv3ProcPassiveIfControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ProcPassiveIfControlRequest_Object = MibScalar
sleOspfv3ProcPassiveIfControlRequest = _SleOspfv3ProcPassiveIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2, 1),
    _SleOspfv3ProcPassiveIfControlRequest_Type()
)
sleOspfv3ProcPassiveIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfControlRequest.setStatus("current")
_SleOspfv3ProcPassiveIfControlStatus_Type = SleControlStatusType
_SleOspfv3ProcPassiveIfControlStatus_Object = MibScalar
sleOspfv3ProcPassiveIfControlStatus = _SleOspfv3ProcPassiveIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2, 2),
    _SleOspfv3ProcPassiveIfControlStatus_Type()
)
sleOspfv3ProcPassiveIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfControlStatus.setStatus("current")
_SleOspfv3ProcPassiveIfControlTimer_Type = Gauge32
_SleOspfv3ProcPassiveIfControlTimer_Object = MibScalar
sleOspfv3ProcPassiveIfControlTimer = _SleOspfv3ProcPassiveIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2, 3),
    _SleOspfv3ProcPassiveIfControlTimer_Type()
)
sleOspfv3ProcPassiveIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfControlTimer.setStatus("current")
_SleOspfv3ProcPassiveIfControlTimeStamp_Type = TimeTicks
_SleOspfv3ProcPassiveIfControlTimeStamp_Object = MibScalar
sleOspfv3ProcPassiveIfControlTimeStamp = _SleOspfv3ProcPassiveIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2, 4),
    _SleOspfv3ProcPassiveIfControlTimeStamp_Type()
)
sleOspfv3ProcPassiveIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfControlTimeStamp.setStatus("current")
_SleOspfv3ProcPassiveIfControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ProcPassiveIfControlReqResult_Object = MibScalar
sleOspfv3ProcPassiveIfControlReqResult = _SleOspfv3ProcPassiveIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2, 5),
    _SleOspfv3ProcPassiveIfControlReqResult_Type()
)
sleOspfv3ProcPassiveIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfControlReqResult.setStatus("current")
_SleOspfv3ProcPassiveIfControlIndex_Type = Integer32
_SleOspfv3ProcPassiveIfControlIndex_Object = MibScalar
sleOspfv3ProcPassiveIfControlIndex = _SleOspfv3ProcPassiveIfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2, 6),
    _SleOspfv3ProcPassiveIfControlIndex_Type()
)
sleOspfv3ProcPassiveIfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfControlIndex.setStatus("current")


class _SleOspfv3ProcPassiveIfControlIfIndex_Type(Integer32):
    """Custom type sleOspfv3ProcPassiveIfControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleOspfv3ProcPassiveIfControlIfIndex_Type.__name__ = "Integer32"
_SleOspfv3ProcPassiveIfControlIfIndex_Object = MibScalar
sleOspfv3ProcPassiveIfControlIfIndex = _SleOspfv3ProcPassiveIfControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 2, 7),
    _SleOspfv3ProcPassiveIfControlIfIndex_Type()
)
sleOspfv3ProcPassiveIfControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfControlIfIndex.setStatus("current")
_SleOspfv3ProcPassIfNotification_ObjectIdentity = ObjectIdentity
sleOspfv3ProcPassIfNotification = _SleOspfv3ProcPassIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 3)
)
_SleOspfv3ProcRedist_ObjectIdentity = ObjectIdentity
sleOspfv3ProcRedist = _SleOspfv3ProcRedist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4)
)
_SleOspfv3ProcRedistTable_Object = MibTable
sleOspfv3ProcRedistTable = _SleOspfv3ProcRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistTable.setStatus("current")
_SleOspfv3ProcRedistEntry_Object = MibTableRow
sleOspfv3ProcRedistEntry = _SleOspfv3ProcRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 1, 1)
)
sleOspfv3ProcRedistEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcRedistType"),
)
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistEntry.setStatus("current")


class _SleOspfv3ProcRedistType_Type(Integer32):
    """Custom type sleOspfv3ProcRedistType based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("isis", 3),
          ("static", 4),
          ("rip", 5),
          ("bgp", 6))
    )


_SleOspfv3ProcRedistType_Type.__name__ = "Integer32"
_SleOspfv3ProcRedistType_Object = MibTableColumn
sleOspfv3ProcRedistType = _SleOspfv3ProcRedistType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 1, 1, 1),
    _SleOspfv3ProcRedistType_Type()
)
sleOspfv3ProcRedistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistType.setStatus("current")


class _SleOspfv3ProcRedistMetricType_Type(Integer32):
    """Custom type sleOspfv3ProcRedistMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external1", 1),
          ("external2", 2))
    )


_SleOspfv3ProcRedistMetricType_Type.__name__ = "Integer32"
_SleOspfv3ProcRedistMetricType_Object = MibTableColumn
sleOspfv3ProcRedistMetricType = _SleOspfv3ProcRedistMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 1, 1, 2),
    _SleOspfv3ProcRedistMetricType_Type()
)
sleOspfv3ProcRedistMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistMetricType.setStatus("current")


class _SleOspfv3ProcRedistMetric_Type(Integer32):
    """Custom type sleOspfv3ProcRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOspfv3ProcRedistMetric_Type.__name__ = "Integer32"
_SleOspfv3ProcRedistMetric_Object = MibTableColumn
sleOspfv3ProcRedistMetric = _SleOspfv3ProcRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 1, 1, 3),
    _SleOspfv3ProcRedistMetric_Type()
)
sleOspfv3ProcRedistMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistMetric.setStatus("current")


class _SleOSpfv3ProcRedistRouteMapName_Type(OctetString):
    """Custom type sleOSpfv3ProcRedistRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOSpfv3ProcRedistRouteMapName_Type.__name__ = "OctetString"
_SleOSpfv3ProcRedistRouteMapName_Object = MibTableColumn
sleOSpfv3ProcRedistRouteMapName = _SleOSpfv3ProcRedistRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 1, 1, 4),
    _SleOSpfv3ProcRedistRouteMapName_Type()
)
sleOSpfv3ProcRedistRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSpfv3ProcRedistRouteMapName.setStatus("current")
_SleOspfv3ProcRedistControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcRedistControl = _SleOspfv3ProcRedistControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2)
)


class _SleOspfv3ProcRedistControlRequest_Type(Integer32):
    """Custom type sleOspfv3ProcRedistControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOspfv3ProcRedist", 1),
          ("modifyOspfv3ProcRedist", 2),
          ("destroyOspfv3ProcRedist", 3))
    )


_SleOspfv3ProcRedistControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ProcRedistControlRequest_Object = MibScalar
sleOspfv3ProcRedistControlRequest = _SleOspfv3ProcRedistControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 1),
    _SleOspfv3ProcRedistControlRequest_Type()
)
sleOspfv3ProcRedistControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlRequest.setStatus("current")
_SleOspfv3ProcRedistControlStatus_Type = SleControlStatusType
_SleOspfv3ProcRedistControlStatus_Object = MibScalar
sleOspfv3ProcRedistControlStatus = _SleOspfv3ProcRedistControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 2),
    _SleOspfv3ProcRedistControlStatus_Type()
)
sleOspfv3ProcRedistControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlStatus.setStatus("current")
_SleOspfv3ProcRedistControlTimer_Type = Gauge32
_SleOspfv3ProcRedistControlTimer_Object = MibScalar
sleOspfv3ProcRedistControlTimer = _SleOspfv3ProcRedistControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 3),
    _SleOspfv3ProcRedistControlTimer_Type()
)
sleOspfv3ProcRedistControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlTimer.setStatus("current")
_SleOspfv3ProcRedistControlTimeStamp_Type = TimeTicks
_SleOspfv3ProcRedistControlTimeStamp_Object = MibScalar
sleOspfv3ProcRedistControlTimeStamp = _SleOspfv3ProcRedistControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 4),
    _SleOspfv3ProcRedistControlTimeStamp_Type()
)
sleOspfv3ProcRedistControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlTimeStamp.setStatus("current")
_SleOspfv3ProcRedistControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ProcRedistControlReqResult_Object = MibScalar
sleOspfv3ProcRedistControlReqResult = _SleOspfv3ProcRedistControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 5),
    _SleOspfv3ProcRedistControlReqResult_Type()
)
sleOspfv3ProcRedistControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlReqResult.setStatus("current")
_SleOspfv3ProcRedistControlIndex_Type = Integer32
_SleOspfv3ProcRedistControlIndex_Object = MibScalar
sleOspfv3ProcRedistControlIndex = _SleOspfv3ProcRedistControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 6),
    _SleOspfv3ProcRedistControlIndex_Type()
)
sleOspfv3ProcRedistControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlIndex.setStatus("current")


class _SleOspfv3ProcRedistControlType_Type(Integer32):
    """Custom type sleOspfv3ProcRedistControlType based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("isis", 3),
          ("static", 4),
          ("rip", 5),
          ("bgp", 6))
    )


_SleOspfv3ProcRedistControlType_Type.__name__ = "Integer32"
_SleOspfv3ProcRedistControlType_Object = MibScalar
sleOspfv3ProcRedistControlType = _SleOspfv3ProcRedistControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 7),
    _SleOspfv3ProcRedistControlType_Type()
)
sleOspfv3ProcRedistControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlType.setStatus("current")


class _SleOspfv3ProcRedistControlMetricType_Type(Integer32):
    """Custom type sleOspfv3ProcRedistControlMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external1", 1),
          ("external2", 2))
    )


_SleOspfv3ProcRedistControlMetricType_Type.__name__ = "Integer32"
_SleOspfv3ProcRedistControlMetricType_Object = MibScalar
sleOspfv3ProcRedistControlMetricType = _SleOspfv3ProcRedistControlMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 8),
    _SleOspfv3ProcRedistControlMetricType_Type()
)
sleOspfv3ProcRedistControlMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlMetricType.setStatus("current")


class _SleOspfv3ProcRedistControlMetric_Type(Integer32):
    """Custom type sleOspfv3ProcRedistControlMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_SleOspfv3ProcRedistControlMetric_Type.__name__ = "Integer32"
_SleOspfv3ProcRedistControlMetric_Object = MibScalar
sleOspfv3ProcRedistControlMetric = _SleOspfv3ProcRedistControlMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 9),
    _SleOspfv3ProcRedistControlMetric_Type()
)
sleOspfv3ProcRedistControlMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistControlMetric.setStatus("current")


class _SleOSpfv3ProcRedistControlRouteMapName_Type(OctetString):
    """Custom type sleOSpfv3ProcRedistControlRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOSpfv3ProcRedistControlRouteMapName_Type.__name__ = "OctetString"
_SleOSpfv3ProcRedistControlRouteMapName_Object = MibScalar
sleOSpfv3ProcRedistControlRouteMapName = _SleOSpfv3ProcRedistControlRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 2, 10),
    _SleOSpfv3ProcRedistControlRouteMapName_Type()
)
sleOSpfv3ProcRedistControlRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSpfv3ProcRedistControlRouteMapName.setStatus("current")
_SleOspfv3ProcRedistNotification_ObjectIdentity = ObjectIdentity
sleOspfv3ProcRedistNotification = _SleOspfv3ProcRedistNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 3)
)
_SleOspfv3ProcArea_ObjectIdentity = ObjectIdentity
sleOspfv3ProcArea = _SleOspfv3ProcArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5)
)
_SleOspfv3ProcAreaInfo_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaInfo = _SleOspfv3ProcAreaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1)
)
_SleOspfv3ProcAreaInfoTable_Object = MibTable
sleOspfv3ProcAreaInfoTable = _SleOspfv3ProcAreaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoTable.setStatus("current")
_SleOspfv3ProcAreaInfoEntry_Object = MibTableRow
sleOspfv3ProcAreaInfoEntry = _SleOspfv3ProcAreaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 1, 1)
)
sleOspfv3ProcAreaInfoEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoIndex"),
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoEntry.setStatus("current")
_SleOspfv3ProcAreaInfoIndex_Type = IpAddress
_SleOspfv3ProcAreaInfoIndex_Object = MibTableColumn
sleOspfv3ProcAreaInfoIndex = _SleOspfv3ProcAreaInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 1, 1, 1),
    _SleOspfv3ProcAreaInfoIndex_Type()
)
sleOspfv3ProcAreaInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoIndex.setStatus("current")


class _SleOspfv3ProcAreaInfoType_Type(Integer32):
    """Custom type sleOspfv3ProcAreaInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("general", 1),
          ("stub", 2),
          ("nssa", 3))
    )


_SleOspfv3ProcAreaInfoType_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaInfoType_Object = MibTableColumn
sleOspfv3ProcAreaInfoType = _SleOspfv3ProcAreaInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 1, 1, 2),
    _SleOspfv3ProcAreaInfoType_Type()
)
sleOspfv3ProcAreaInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoType.setStatus("current")


class _SleOspfv3ProcAreaInfoDefaultCost_Type(Integer32):
    """Custom type sleOspfv3ProcAreaInfoDefaultCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOspfv3ProcAreaInfoDefaultCost_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaInfoDefaultCost_Object = MibTableColumn
sleOspfv3ProcAreaInfoDefaultCost = _SleOspfv3ProcAreaInfoDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 1, 1, 3),
    _SleOspfv3ProcAreaInfoDefaultCost_Type()
)
sleOspfv3ProcAreaInfoDefaultCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoDefaultCost.setStatus("current")


class _SleOspfv3ProcAreaInfoSummary_Type(Integer32):
    """Custom type sleOspfv3ProcAreaInfoSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_SleOspfv3ProcAreaInfoSummary_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaInfoSummary_Object = MibTableColumn
sleOspfv3ProcAreaInfoSummary = _SleOspfv3ProcAreaInfoSummary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 1, 1, 4),
    _SleOspfv3ProcAreaInfoSummary_Type()
)
sleOspfv3ProcAreaInfoSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoSummary.setStatus("current")
_SleOspfv3ProcAreaInfoControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaInfoControl = _SleOspfv3ProcAreaInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2)
)


class _SleOspfv3ProcAreaInfoControlRequest_Type(Integer32):
    """Custom type sleOspfv3ProcAreaInfoControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOspfv3ProcAreaInfo", 1),
          ("modifyOspfv3ProcAreaInfo", 2),
          ("destroyOspfv3ProcAreaInfo", 3))
    )


_SleOspfv3ProcAreaInfoControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaInfoControlRequest_Object = MibScalar
sleOspfv3ProcAreaInfoControlRequest = _SleOspfv3ProcAreaInfoControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 1),
    _SleOspfv3ProcAreaInfoControlRequest_Type()
)
sleOspfv3ProcAreaInfoControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlRequest.setStatus("current")
_SleOspfv3ProcAreaInfoControlStatus_Type = SleControlStatusType
_SleOspfv3ProcAreaInfoControlStatus_Object = MibScalar
sleOspfv3ProcAreaInfoControlStatus = _SleOspfv3ProcAreaInfoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 2),
    _SleOspfv3ProcAreaInfoControlStatus_Type()
)
sleOspfv3ProcAreaInfoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlStatus.setStatus("current")
_SleOspfv3ProcAreaInfoControlTimer_Type = Gauge32
_SleOspfv3ProcAreaInfoControlTimer_Object = MibScalar
sleOspfv3ProcAreaInfoControlTimer = _SleOspfv3ProcAreaInfoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 3),
    _SleOspfv3ProcAreaInfoControlTimer_Type()
)
sleOspfv3ProcAreaInfoControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlTimer.setStatus("current")
_SleOspfv3ProcAreaInfoControlTimeStamp_Type = TimeTicks
_SleOspfv3ProcAreaInfoControlTimeStamp_Object = MibScalar
sleOspfv3ProcAreaInfoControlTimeStamp = _SleOspfv3ProcAreaInfoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 4),
    _SleOspfv3ProcAreaInfoControlTimeStamp_Type()
)
sleOspfv3ProcAreaInfoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlTimeStamp.setStatus("current")
_SleOspfv3ProcAreaInfoControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ProcAreaInfoControlReqResult_Object = MibScalar
sleOspfv3ProcAreaInfoControlReqResult = _SleOspfv3ProcAreaInfoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 5),
    _SleOspfv3ProcAreaInfoControlReqResult_Type()
)
sleOspfv3ProcAreaInfoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlReqResult.setStatus("current")
_SleOspfv3ProcAreaInfoControlIndex_Type = Integer32
_SleOspfv3ProcAreaInfoControlIndex_Object = MibScalar
sleOspfv3ProcAreaInfoControlIndex = _SleOspfv3ProcAreaInfoControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 6),
    _SleOspfv3ProcAreaInfoControlIndex_Type()
)
sleOspfv3ProcAreaInfoControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlIndex.setStatus("current")
_SleOspfv3ProcAreaInfoControlAreaIndex_Type = IpAddress
_SleOspfv3ProcAreaInfoControlAreaIndex_Object = MibScalar
sleOspfv3ProcAreaInfoControlAreaIndex = _SleOspfv3ProcAreaInfoControlAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 7),
    _SleOspfv3ProcAreaInfoControlAreaIndex_Type()
)
sleOspfv3ProcAreaInfoControlAreaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlAreaIndex.setStatus("current")


class _SleOspfv3ProcAreaInfoControlType_Type(Integer32):
    """Custom type sleOspfv3ProcAreaInfoControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("general", 1),
          ("stub", 2),
          ("nssa", 3))
    )


_SleOspfv3ProcAreaInfoControlType_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaInfoControlType_Object = MibScalar
sleOspfv3ProcAreaInfoControlType = _SleOspfv3ProcAreaInfoControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 8),
    _SleOspfv3ProcAreaInfoControlType_Type()
)
sleOspfv3ProcAreaInfoControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlType.setStatus("current")


class _SleOspfv3ProcAreaInfoControlDefaultCost_Type(Integer32):
    """Custom type sleOspfv3ProcAreaInfoControlDefaultCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOspfv3ProcAreaInfoControlDefaultCost_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaInfoControlDefaultCost_Object = MibScalar
sleOspfv3ProcAreaInfoControlDefaultCost = _SleOspfv3ProcAreaInfoControlDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 9),
    _SleOspfv3ProcAreaInfoControlDefaultCost_Type()
)
sleOspfv3ProcAreaInfoControlDefaultCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlDefaultCost.setStatus("current")


class _SleOspfv3ProcAreaInfoControlSummary_Type(Integer32):
    """Custom type sleOspfv3ProcAreaInfoControlSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_SleOspfv3ProcAreaInfoControlSummary_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaInfoControlSummary_Object = MibScalar
sleOspfv3ProcAreaInfoControlSummary = _SleOspfv3ProcAreaInfoControlSummary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 2, 10),
    _SleOspfv3ProcAreaInfoControlSummary_Type()
)
sleOspfv3ProcAreaInfoControlSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoControlSummary.setStatus("current")
_SleOspfv3ProcAreaInfoNotification_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaInfoNotification = _SleOspfv3ProcAreaInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 3)
)
_SleOspfv3ProcAreaRange_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaRange = _SleOspfv3ProcAreaRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2)
)
_SleOspfv3ProcAreaRangeTable_Object = MibTable
sleOspfv3ProcAreaRangeTable = _SleOspfv3ProcAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeTable.setStatus("current")
_SleOspfv3ProcAreaRangeEntry_Object = MibTableRow
sleOspfv3ProcAreaRangeEntry = _SleOspfv3ProcAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 1, 1)
)
sleOspfv3ProcAreaRangeEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeAddress"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeMask"),
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeEntry.setStatus("current")
_SleOspfv3ProcAreaRangeAddress_Type = InetAddressIPv6
_SleOspfv3ProcAreaRangeAddress_Object = MibTableColumn
sleOspfv3ProcAreaRangeAddress = _SleOspfv3ProcAreaRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 1, 1, 1),
    _SleOspfv3ProcAreaRangeAddress_Type()
)
sleOspfv3ProcAreaRangeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeAddress.setStatus("current")


class _SleOspfv3ProcAreaRangeMask_Type(Integer32):
    """Custom type sleOspfv3ProcAreaRangeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleOspfv3ProcAreaRangeMask_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaRangeMask_Object = MibTableColumn
sleOspfv3ProcAreaRangeMask = _SleOspfv3ProcAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 1, 1, 2),
    _SleOspfv3ProcAreaRangeMask_Type()
)
sleOspfv3ProcAreaRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeMask.setStatus("current")


class _SleOspfv3ProcAreaRangeAdvertiseFlag_Type(Integer32):
    """Custom type sleOspfv3ProcAreaRangeAdvertiseFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAdvertise", 0),
          ("advertise", 1))
    )


_SleOspfv3ProcAreaRangeAdvertiseFlag_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaRangeAdvertiseFlag_Object = MibTableColumn
sleOspfv3ProcAreaRangeAdvertiseFlag = _SleOspfv3ProcAreaRangeAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 1, 1, 3),
    _SleOspfv3ProcAreaRangeAdvertiseFlag_Type()
)
sleOspfv3ProcAreaRangeAdvertiseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeAdvertiseFlag.setStatus("current")
_SleOspfv3ProcAreaRangeControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaRangeControl = _SleOspfv3ProcAreaRangeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2)
)


class _SleOspfv3ProcAreaRangeControlRequest_Type(Integer32):
    """Custom type sleOspfv3ProcAreaRangeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOspfv3ProcAreaRange", 1),
          ("modifyOspfv3ProcAreaRange", 2),
          ("destroyOspfv3ProcAreaRange", 3))
    )


_SleOspfv3ProcAreaRangeControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaRangeControlRequest_Object = MibScalar
sleOspfv3ProcAreaRangeControlRequest = _SleOspfv3ProcAreaRangeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 1),
    _SleOspfv3ProcAreaRangeControlRequest_Type()
)
sleOspfv3ProcAreaRangeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlRequest.setStatus("current")
_SleOspfv3ProcAreaRangeControlStatus_Type = SleControlStatusType
_SleOspfv3ProcAreaRangeControlStatus_Object = MibScalar
sleOspfv3ProcAreaRangeControlStatus = _SleOspfv3ProcAreaRangeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 2),
    _SleOspfv3ProcAreaRangeControlStatus_Type()
)
sleOspfv3ProcAreaRangeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlStatus.setStatus("current")
_SleOspfv3ProcAreaRangeControlTimer_Type = Gauge32
_SleOspfv3ProcAreaRangeControlTimer_Object = MibScalar
sleOspfv3ProcAreaRangeControlTimer = _SleOspfv3ProcAreaRangeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 3),
    _SleOspfv3ProcAreaRangeControlTimer_Type()
)
sleOspfv3ProcAreaRangeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlTimer.setStatus("current")
_SleOspfv3ProcAreaRangeControlTimeStamp_Type = TimeTicks
_SleOspfv3ProcAreaRangeControlTimeStamp_Object = MibScalar
sleOspfv3ProcAreaRangeControlTimeStamp = _SleOspfv3ProcAreaRangeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 4),
    _SleOspfv3ProcAreaRangeControlTimeStamp_Type()
)
sleOspfv3ProcAreaRangeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlTimeStamp.setStatus("current")
_SleOspfv3ProcAreaRangeControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ProcAreaRangeControlReqResult_Object = MibScalar
sleOspfv3ProcAreaRangeControlReqResult = _SleOspfv3ProcAreaRangeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 5),
    _SleOspfv3ProcAreaRangeControlReqResult_Type()
)
sleOspfv3ProcAreaRangeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlReqResult.setStatus("current")
_SleOspfv3ProcAreaRangeControlIndex_Type = Integer32
_SleOspfv3ProcAreaRangeControlIndex_Object = MibScalar
sleOspfv3ProcAreaRangeControlIndex = _SleOspfv3ProcAreaRangeControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 6),
    _SleOspfv3ProcAreaRangeControlIndex_Type()
)
sleOspfv3ProcAreaRangeControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlIndex.setStatus("current")
_SleOspfv3ProcAreaRangeControlAreaIndex_Type = IpAddress
_SleOspfv3ProcAreaRangeControlAreaIndex_Object = MibScalar
sleOspfv3ProcAreaRangeControlAreaIndex = _SleOspfv3ProcAreaRangeControlAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 7),
    _SleOspfv3ProcAreaRangeControlAreaIndex_Type()
)
sleOspfv3ProcAreaRangeControlAreaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlAreaIndex.setStatus("current")
_SleOspfv3ProcAreaRangeControlAddr_Type = InetAddressIPv6
_SleOspfv3ProcAreaRangeControlAddr_Object = MibScalar
sleOspfv3ProcAreaRangeControlAddr = _SleOspfv3ProcAreaRangeControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 8),
    _SleOspfv3ProcAreaRangeControlAddr_Type()
)
sleOspfv3ProcAreaRangeControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlAddr.setStatus("current")


class _SleOspfv3ProcAreaRangeControlMask_Type(Integer32):
    """Custom type sleOspfv3ProcAreaRangeControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleOspfv3ProcAreaRangeControlMask_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaRangeControlMask_Object = MibScalar
sleOspfv3ProcAreaRangeControlMask = _SleOspfv3ProcAreaRangeControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 9),
    _SleOspfv3ProcAreaRangeControlMask_Type()
)
sleOspfv3ProcAreaRangeControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlMask.setStatus("current")


class _SleOspfv3ProcAreaRangeControlAdvertiseFlag_Type(Integer32):
    """Custom type sleOspfv3ProcAreaRangeControlAdvertiseFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAdvertise", 0),
          ("advertise", 1))
    )


_SleOspfv3ProcAreaRangeControlAdvertiseFlag_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaRangeControlAdvertiseFlag_Object = MibScalar
sleOspfv3ProcAreaRangeControlAdvertiseFlag = _SleOspfv3ProcAreaRangeControlAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 2, 10),
    _SleOspfv3ProcAreaRangeControlAdvertiseFlag_Type()
)
sleOspfv3ProcAreaRangeControlAdvertiseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeControlAdvertiseFlag.setStatus("current")
_SleOspfv3ProcAreaRangeNotification_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaRangeNotification = _SleOspfv3ProcAreaRangeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 3)
)
_SleOspfv3ProcAreaVlink_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaVlink = _SleOspfv3ProcAreaVlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3)
)
_SleOspfv3ProcAreaVlinkTable_Object = MibTable
sleOspfv3ProcAreaVlinkTable = _SleOspfv3ProcAreaVlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkTable.setStatus("current")
_SleOspfv3ProcAreaVlinkEntry_Object = MibTableRow
sleOspfv3ProcAreaVlinkEntry = _SleOspfv3ProcAreaVlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1, 1)
)
sleOspfv3ProcAreaVlinkEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkRouterId"),
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkEntry.setStatus("current")
_SleOspfv3ProcAreaVlinkRouterId_Type = InetAddressIPv4
_SleOspfv3ProcAreaVlinkRouterId_Object = MibTableColumn
sleOspfv3ProcAreaVlinkRouterId = _SleOspfv3ProcAreaVlinkRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1, 1, 1),
    _SleOspfv3ProcAreaVlinkRouterId_Type()
)
sleOspfv3ProcAreaVlinkRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkRouterId.setStatus("current")


class _SleOspfv3ProcAreaVlinkDeadInterval_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkDeadInterval_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkDeadInterval_Object = MibTableColumn
sleOspfv3ProcAreaVlinkDeadInterval = _SleOspfv3ProcAreaVlinkDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1, 1, 2),
    _SleOspfv3ProcAreaVlinkDeadInterval_Type()
)
sleOspfv3ProcAreaVlinkDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkDeadInterval.setStatus("current")


class _SleOspfv3ProcAreaVlinkHelloInterval_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkHelloInterval_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkHelloInterval_Object = MibTableColumn
sleOspfv3ProcAreaVlinkHelloInterval = _SleOspfv3ProcAreaVlinkHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1, 1, 3),
    _SleOspfv3ProcAreaVlinkHelloInterval_Type()
)
sleOspfv3ProcAreaVlinkHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkHelloInterval.setStatus("current")


class _SleOspfv3ProcAreaVlinkInstanceId_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3ProcAreaVlinkInstanceId_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkInstanceId_Object = MibTableColumn
sleOspfv3ProcAreaVlinkInstanceId = _SleOspfv3ProcAreaVlinkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1, 1, 4),
    _SleOspfv3ProcAreaVlinkInstanceId_Type()
)
sleOspfv3ProcAreaVlinkInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkInstanceId.setStatus("current")


class _SleOspfv3ProcAreaVlinkRetransInterval_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkRetransInterval_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkRetransInterval_Object = MibTableColumn
sleOspfv3ProcAreaVlinkRetransInterval = _SleOspfv3ProcAreaVlinkRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1, 1, 5),
    _SleOspfv3ProcAreaVlinkRetransInterval_Type()
)
sleOspfv3ProcAreaVlinkRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkRetransInterval.setStatus("current")


class _SleOspfv3ProcAreaVlinkTransDelay_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkTransDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkTransDelay_Object = MibTableColumn
sleOspfv3ProcAreaVlinkTransDelay = _SleOspfv3ProcAreaVlinkTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 1, 1, 6),
    _SleOspfv3ProcAreaVlinkTransDelay_Type()
)
sleOspfv3ProcAreaVlinkTransDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkTransDelay.setStatus("current")
_SleOspfv3ProcAreaVlinkControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaVlinkControl = _SleOspfv3ProcAreaVlinkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2)
)


class _SleOspfv3ProcAreaVlinkControlRequest_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOspfv3ProcAreaVlink", 1),
          ("modifyOspfv3ProcAreaVlink", 2),
          ("destroyOspfv3ProcAreaVlink", 3))
    )


_SleOspfv3ProcAreaVlinkControlRequest_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkControlRequest_Object = MibScalar
sleOspfv3ProcAreaVlinkControlRequest = _SleOspfv3ProcAreaVlinkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 1),
    _SleOspfv3ProcAreaVlinkControlRequest_Type()
)
sleOspfv3ProcAreaVlinkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlRequest.setStatus("current")
_SleOspfv3ProcAreaVlinkControlStatus_Type = SleControlStatusType
_SleOspfv3ProcAreaVlinkControlStatus_Object = MibScalar
sleOspfv3ProcAreaVlinkControlStatus = _SleOspfv3ProcAreaVlinkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 2),
    _SleOspfv3ProcAreaVlinkControlStatus_Type()
)
sleOspfv3ProcAreaVlinkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlStatus.setStatus("current")
_SleOspfv3ProcAreaVlinkControlTimer_Type = Gauge32
_SleOspfv3ProcAreaVlinkControlTimer_Object = MibScalar
sleOspfv3ProcAreaVlinkControlTimer = _SleOspfv3ProcAreaVlinkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 3),
    _SleOspfv3ProcAreaVlinkControlTimer_Type()
)
sleOspfv3ProcAreaVlinkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlTimer.setStatus("current")
_SleOspfv3ProcAreaVlinkControlTimeStamp_Type = TimeTicks
_SleOspfv3ProcAreaVlinkControlTimeStamp_Object = MibScalar
sleOspfv3ProcAreaVlinkControlTimeStamp = _SleOspfv3ProcAreaVlinkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 4),
    _SleOspfv3ProcAreaVlinkControlTimeStamp_Type()
)
sleOspfv3ProcAreaVlinkControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlTimeStamp.setStatus("current")
_SleOspfv3ProcAreaVlinkControlReqResult_Type = SleControlRequestResultType
_SleOspfv3ProcAreaVlinkControlReqResult_Object = MibScalar
sleOspfv3ProcAreaVlinkControlReqResult = _SleOspfv3ProcAreaVlinkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 5),
    _SleOspfv3ProcAreaVlinkControlReqResult_Type()
)
sleOspfv3ProcAreaVlinkControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlReqResult.setStatus("current")
_SleOspfv3ProcAreaVlinkControlIndex_Type = Integer32
_SleOspfv3ProcAreaVlinkControlIndex_Object = MibScalar
sleOspfv3ProcAreaVlinkControlIndex = _SleOspfv3ProcAreaVlinkControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 6),
    _SleOspfv3ProcAreaVlinkControlIndex_Type()
)
sleOspfv3ProcAreaVlinkControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlIndex.setStatus("current")
_SleOspfv3ProcAreaVlinkControlAreaIndex_Type = IpAddress
_SleOspfv3ProcAreaVlinkControlAreaIndex_Object = MibScalar
sleOspfv3ProcAreaVlinkControlAreaIndex = _SleOspfv3ProcAreaVlinkControlAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 7),
    _SleOspfv3ProcAreaVlinkControlAreaIndex_Type()
)
sleOspfv3ProcAreaVlinkControlAreaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlAreaIndex.setStatus("current")
_SleOspfv3ProcAreaVlinkControlRouterId_Type = InetAddressIPv4
_SleOspfv3ProcAreaVlinkControlRouterId_Object = MibScalar
sleOspfv3ProcAreaVlinkControlRouterId = _SleOspfv3ProcAreaVlinkControlRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 8),
    _SleOspfv3ProcAreaVlinkControlRouterId_Type()
)
sleOspfv3ProcAreaVlinkControlRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlRouterId.setStatus("current")


class _SleOspfv3ProcAreaVlinkControlDeadInterval_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkControlDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkControlDeadInterval_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkControlDeadInterval_Object = MibScalar
sleOspfv3ProcAreaVlinkControlDeadInterval = _SleOspfv3ProcAreaVlinkControlDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 9),
    _SleOspfv3ProcAreaVlinkControlDeadInterval_Type()
)
sleOspfv3ProcAreaVlinkControlDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlDeadInterval.setStatus("current")


class _SleOspfv3ProcAreaVlinkControlHelloInterval_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkControlHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkControlHelloInterval_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkControlHelloInterval_Object = MibScalar
sleOspfv3ProcAreaVlinkControlHelloInterval = _SleOspfv3ProcAreaVlinkControlHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 10),
    _SleOspfv3ProcAreaVlinkControlHelloInterval_Type()
)
sleOspfv3ProcAreaVlinkControlHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlHelloInterval.setStatus("current")


class _SleOspfv3ProcAreaVlinkControlInstanceId_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkControlInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3ProcAreaVlinkControlInstanceId_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkControlInstanceId_Object = MibScalar
sleOspfv3ProcAreaVlinkControlInstanceId = _SleOspfv3ProcAreaVlinkControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 11),
    _SleOspfv3ProcAreaVlinkControlInstanceId_Type()
)
sleOspfv3ProcAreaVlinkControlInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlInstanceId.setStatus("current")


class _SleOspfv3ProcAreaVlinkControlRetransInterval_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkControlRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkControlRetransInterval_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkControlRetransInterval_Object = MibScalar
sleOspfv3ProcAreaVlinkControlRetransInterval = _SleOspfv3ProcAreaVlinkControlRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 12),
    _SleOspfv3ProcAreaVlinkControlRetransInterval_Type()
)
sleOspfv3ProcAreaVlinkControlRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlRetransInterval.setStatus("current")


class _SleOspfv3ProcAreaVlinkControlTransDelay_Type(Integer32):
    """Custom type sleOspfv3ProcAreaVlinkControlTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3ProcAreaVlinkControlTransDelay_Type.__name__ = "Integer32"
_SleOspfv3ProcAreaVlinkControlTransDelay_Object = MibScalar
sleOspfv3ProcAreaVlinkControlTransDelay = _SleOspfv3ProcAreaVlinkControlTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 2, 13),
    _SleOspfv3ProcAreaVlinkControlTransDelay_Type()
)
sleOspfv3ProcAreaVlinkControlTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkControlTransDelay.setStatus("current")
_SleOspfv3ProcAreaVlinkNotification_ObjectIdentity = ObjectIdentity
sleOspfv3ProcAreaVlinkNotification = _SleOspfv3ProcAreaVlinkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 3)
)
_SleOspfv3Interface_ObjectIdentity = ObjectIdentity
sleOspfv3Interface = _SleOspfv3Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3)
)
_SleOspfv3IfInstance_ObjectIdentity = ObjectIdentity
sleOspfv3IfInstance = _SleOspfv3IfInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1)
)
_SleOspfv3IfInstanceTable_Object = MibTable
sleOspfv3IfInstanceTable = _SleOspfv3IfInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceTable.setStatus("current")
_SleOspfv3IfInstanceEntry_Object = MibTableRow
sleOspfv3IfInstanceEntry = _SleOspfv3IfInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1)
)
sleOspfv3IfInstanceEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3IfInstanceIfIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3IfInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceEntry.setStatus("current")


class _SleOspfv3IfInstanceIfIndex_Type(Integer32):
    """Custom type sleOspfv3IfInstanceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleOspfv3IfInstanceIfIndex_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceIfIndex_Object = MibTableColumn
sleOspfv3IfInstanceIfIndex = _SleOspfv3IfInstanceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 1),
    _SleOspfv3IfInstanceIfIndex_Type()
)
sleOspfv3IfInstanceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceIfIndex.setStatus("current")


class _SleOspfv3IfInstanceInstanceId_Type(Integer32):
    """Custom type sleOspfv3IfInstanceInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfInstanceInstanceId_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceInstanceId_Object = MibTableColumn
sleOspfv3IfInstanceInstanceId = _SleOspfv3IfInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 2),
    _SleOspfv3IfInstanceInstanceId_Type()
)
sleOspfv3IfInstanceInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceInstanceId.setStatus("current")


class _SleOspfv3IfInstanceProcTag_Type(OctetString):
    """Custom type sleOspfv3IfInstanceProcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3IfInstanceProcTag_Type.__name__ = "OctetString"
_SleOspfv3IfInstanceProcTag_Object = MibTableColumn
sleOspfv3IfInstanceProcTag = _SleOspfv3IfInstanceProcTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 3),
    _SleOspfv3IfInstanceProcTag_Type()
)
sleOspfv3IfInstanceProcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceProcTag.setStatus("current")


class _SleOspfv3IfInstanceAreaFlag_Type(Integer32):
    """Custom type sleOspfv3IfInstanceAreaFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noArea", 0),
          ("useArea", 1))
    )


_SleOspfv3IfInstanceAreaFlag_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceAreaFlag_Object = MibTableColumn
sleOspfv3IfInstanceAreaFlag = _SleOspfv3IfInstanceAreaFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 4),
    _SleOspfv3IfInstanceAreaFlag_Type()
)
sleOspfv3IfInstanceAreaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceAreaFlag.setStatus("current")
_SleOspfv3IfInstanceAreaIndex_Type = IpAddress
_SleOspfv3IfInstanceAreaIndex_Object = MibTableColumn
sleOspfv3IfInstanceAreaIndex = _SleOspfv3IfInstanceAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 5),
    _SleOspfv3IfInstanceAreaIndex_Type()
)
sleOspfv3IfInstanceAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceAreaIndex.setStatus("current")


class _SleOspfv3IfInstanceDeadInterval_Type(Integer32):
    """Custom type sleOspfv3IfInstanceDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceDeadInterval_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceDeadInterval_Object = MibTableColumn
sleOspfv3IfInstanceDeadInterval = _SleOspfv3IfInstanceDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 6),
    _SleOspfv3IfInstanceDeadInterval_Type()
)
sleOspfv3IfInstanceDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceDeadInterval.setStatus("current")


class _SleOspfv3IfInstanceHelloInterval_Type(Integer32):
    """Custom type sleOspfv3IfInstanceHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceHelloInterval_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceHelloInterval_Object = MibTableColumn
sleOspfv3IfInstanceHelloInterval = _SleOspfv3IfInstanceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 7),
    _SleOspfv3IfInstanceHelloInterval_Type()
)
sleOspfv3IfInstanceHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceHelloInterval.setStatus("current")


class _SleOspfv3IfInstanceNetworkType_Type(Integer32):
    """Custom type sleOspfv3IfInstanceNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p2p", 1),
          ("broadcast", 2),
          ("nbma", 3),
          ("p2mp", 4),
          ("p2mpNbma", 5),
          ("virtualLink", 6),
          ("loopback", 7))
    )


_SleOspfv3IfInstanceNetworkType_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceNetworkType_Object = MibTableColumn
sleOspfv3IfInstanceNetworkType = _SleOspfv3IfInstanceNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 8),
    _SleOspfv3IfInstanceNetworkType_Type()
)
sleOspfv3IfInstanceNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceNetworkType.setStatus("current")


class _SleOspfv3IfInstanceCost_Type(Integer32):
    """Custom type sleOspfv3IfInstanceCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceCost_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceCost_Object = MibTableColumn
sleOspfv3IfInstanceCost = _SleOspfv3IfInstanceCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 9),
    _SleOspfv3IfInstanceCost_Type()
)
sleOspfv3IfInstanceCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceCost.setStatus("current")


class _SleOspfv3IfInstanceTransDelay_Type(Integer32):
    """Custom type sleOspfv3IfInstanceTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceTransDelay_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceTransDelay_Object = MibTableColumn
sleOspfv3IfInstanceTransDelay = _SleOspfv3IfInstanceTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 10),
    _SleOspfv3IfInstanceTransDelay_Type()
)
sleOspfv3IfInstanceTransDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceTransDelay.setStatus("current")


class _SleOspfv3IfInstanceRetransInterval_Type(Integer32):
    """Custom type sleOspfv3IfInstanceRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceRetransInterval_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceRetransInterval_Object = MibTableColumn
sleOspfv3IfInstanceRetransInterval = _SleOspfv3IfInstanceRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 11),
    _SleOspfv3IfInstanceRetransInterval_Type()
)
sleOspfv3IfInstanceRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceRetransInterval.setStatus("current")


class _SleOspfv3IfInstancePriority_Type(Integer32):
    """Custom type sleOspfv3IfInstancePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfInstancePriority_Type.__name__ = "Integer32"
_SleOspfv3IfInstancePriority_Object = MibTableColumn
sleOspfv3IfInstancePriority = _SleOspfv3IfInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 12),
    _SleOspfv3IfInstancePriority_Type()
)
sleOspfv3IfInstancePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstancePriority.setStatus("current")


class _SleOspfv3IfInstanceBfd_Type(Integer32):
    """Custom type sleOspfv3IfInstanceBfd based on Integer32"""
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
          ("disable", 1),
          ("enable", 2))
    )


_SleOspfv3IfInstanceBfd_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceBfd_Object = MibTableColumn
sleOspfv3IfInstanceBfd = _SleOspfv3IfInstanceBfd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 13),
    _SleOspfv3IfInstanceBfd_Type()
)
sleOspfv3IfInstanceBfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceBfd.setStatus("current")


class _SleOspfv3IfInstanceEfm_Type(Integer32):
    """Custom type sleOspfv3IfInstanceEfm based on Integer32"""
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
          ("disable", 1),
          ("enable", 2))
    )


_SleOspfv3IfInstanceEfm_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceEfm_Object = MibTableColumn
sleOspfv3IfInstanceEfm = _SleOspfv3IfInstanceEfm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 1, 1, 14),
    _SleOspfv3IfInstanceEfm_Type()
)
sleOspfv3IfInstanceEfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceEfm.setStatus("current")
_SleOspfv3ProcIfInstanceControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcIfInstanceControl = _SleOspfv3ProcIfInstanceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2)
)


class _SleOspfv3IfInstanceControlRequest_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setOspfv3IfInstance", 1)
    )


_SleOspfv3IfInstanceControlRequest_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlRequest_Object = MibScalar
sleOspfv3IfInstanceControlRequest = _SleOspfv3IfInstanceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 1),
    _SleOspfv3IfInstanceControlRequest_Type()
)
sleOspfv3IfInstanceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlRequest.setStatus("current")
_SleOspfv3IfInstanceControlStatus_Type = SleControlStatusType
_SleOspfv3IfInstanceControlStatus_Object = MibScalar
sleOspfv3IfInstanceControlStatus = _SleOspfv3IfInstanceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 2),
    _SleOspfv3IfInstanceControlStatus_Type()
)
sleOspfv3IfInstanceControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlStatus.setStatus("current")
_SleOspfv3IfInstanceControlTimer_Type = Gauge32
_SleOspfv3IfInstanceControlTimer_Object = MibScalar
sleOspfv3IfInstanceControlTimer = _SleOspfv3IfInstanceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 3),
    _SleOspfv3IfInstanceControlTimer_Type()
)
sleOspfv3IfInstanceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlTimer.setStatus("current")
_SleOspfv3IfInstanceControlTimeStamp_Type = TimeTicks
_SleOspfv3IfInstanceControlTimeStamp_Object = MibScalar
sleOspfv3IfInstanceControlTimeStamp = _SleOspfv3IfInstanceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 4),
    _SleOspfv3IfInstanceControlTimeStamp_Type()
)
sleOspfv3IfInstanceControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlTimeStamp.setStatus("current")
_SleOspfv3IfInstanceControlReqResult_Type = SleControlRequestResultType
_SleOspfv3IfInstanceControlReqResult_Object = MibScalar
sleOspfv3IfInstanceControlReqResult = _SleOspfv3IfInstanceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 5),
    _SleOspfv3IfInstanceControlReqResult_Type()
)
sleOspfv3IfInstanceControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlReqResult.setStatus("current")


class _SleOspfv3IfInstanceControlIfIndex_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleOspfv3IfInstanceControlIfIndex_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlIfIndex_Object = MibScalar
sleOspfv3IfInstanceControlIfIndex = _SleOspfv3IfInstanceControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 6),
    _SleOspfv3IfInstanceControlIfIndex_Type()
)
sleOspfv3IfInstanceControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlIfIndex.setStatus("current")


class _SleOspfv3IfInstanceControlIfInstanceId_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlIfInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfInstanceControlIfInstanceId_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlIfInstanceId_Object = MibScalar
sleOspfv3IfInstanceControlIfInstanceId = _SleOspfv3IfInstanceControlIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 7),
    _SleOspfv3IfInstanceControlIfInstanceId_Type()
)
sleOspfv3IfInstanceControlIfInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlIfInstanceId.setStatus("current")


class _SleOspfv3IfInstanceControlProcTag_Type(OctetString):
    """Custom type sleOspfv3IfInstanceControlProcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3IfInstanceControlProcTag_Type.__name__ = "OctetString"
_SleOspfv3IfInstanceControlProcTag_Object = MibScalar
sleOspfv3IfInstanceControlProcTag = _SleOspfv3IfInstanceControlProcTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 8),
    _SleOspfv3IfInstanceControlProcTag_Type()
)
sleOspfv3IfInstanceControlProcTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlProcTag.setStatus("current")


class _SleOspfv3IfInstanceControlAreaFlag_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlAreaFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noArea", 0),
          ("useArea", 1))
    )


_SleOspfv3IfInstanceControlAreaFlag_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlAreaFlag_Object = MibScalar
sleOspfv3IfInstanceControlAreaFlag = _SleOspfv3IfInstanceControlAreaFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 9),
    _SleOspfv3IfInstanceControlAreaFlag_Type()
)
sleOspfv3IfInstanceControlAreaFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlAreaFlag.setStatus("current")
_SleOspfv3IfInstanceControlAreaIndex_Type = IpAddress
_SleOspfv3IfInstanceControlAreaIndex_Object = MibScalar
sleOspfv3IfInstanceControlAreaIndex = _SleOspfv3IfInstanceControlAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 10),
    _SleOspfv3IfInstanceControlAreaIndex_Type()
)
sleOspfv3IfInstanceControlAreaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlAreaIndex.setStatus("current")


class _SleOspfv3IfInstanceControlDeadInterval_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceControlDeadInterval_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlDeadInterval_Object = MibScalar
sleOspfv3IfInstanceControlDeadInterval = _SleOspfv3IfInstanceControlDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 11),
    _SleOspfv3IfInstanceControlDeadInterval_Type()
)
sleOspfv3IfInstanceControlDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlDeadInterval.setStatus("current")


class _SleOspfv3IfInstanceControlHelloInterval_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceControlHelloInterval_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlHelloInterval_Object = MibScalar
sleOspfv3IfInstanceControlHelloInterval = _SleOspfv3IfInstanceControlHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 12),
    _SleOspfv3IfInstanceControlHelloInterval_Type()
)
sleOspfv3IfInstanceControlHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlHelloInterval.setStatus("current")


class _SleOspfv3IfInstanceControlNetworkType_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p2p", 1),
          ("broadcast", 2),
          ("nbma", 3),
          ("p2mp", 4),
          ("p2mpNbma", 5),
          ("virtualLink", 6),
          ("loopback", 7))
    )


_SleOspfv3IfInstanceControlNetworkType_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlNetworkType_Object = MibScalar
sleOspfv3IfInstanceControlNetworkType = _SleOspfv3IfInstanceControlNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 13),
    _SleOspfv3IfInstanceControlNetworkType_Type()
)
sleOspfv3IfInstanceControlNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlNetworkType.setStatus("current")


class _SleOspfv3IfInstanceControlCost_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceControlCost_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlCost_Object = MibScalar
sleOspfv3IfInstanceControlCost = _SleOspfv3IfInstanceControlCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 14),
    _SleOspfv3IfInstanceControlCost_Type()
)
sleOspfv3IfInstanceControlCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlCost.setStatus("current")


class _SleOspfv3IfInstanceControlTransDelay_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceControlTransDelay_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlTransDelay_Object = MibScalar
sleOspfv3IfInstanceControlTransDelay = _SleOspfv3IfInstanceControlTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 15),
    _SleOspfv3IfInstanceControlTransDelay_Type()
)
sleOspfv3IfInstanceControlTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlTransDelay.setStatus("current")


class _SleOspfv3IfInstanceControlRetransInterval_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOspfv3IfInstanceControlRetransInterval_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlRetransInterval_Object = MibScalar
sleOspfv3IfInstanceControlRetransInterval = _SleOspfv3IfInstanceControlRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 16),
    _SleOspfv3IfInstanceControlRetransInterval_Type()
)
sleOspfv3IfInstanceControlRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlRetransInterval.setStatus("current")


class _SleOspfv3IfInstanceControlPriority_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfInstanceControlPriority_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlPriority_Object = MibScalar
sleOspfv3IfInstanceControlPriority = _SleOspfv3IfInstanceControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 17),
    _SleOspfv3IfInstanceControlPriority_Type()
)
sleOspfv3IfInstanceControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlPriority.setStatus("current")


class _SleOspfv3IfInstanceControlBfd_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlBfd based on Integer32"""
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
          ("disable", 1),
          ("enable", 2))
    )


_SleOspfv3IfInstanceControlBfd_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlBfd_Object = MibScalar
sleOspfv3IfInstanceControlBfd = _SleOspfv3IfInstanceControlBfd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 18),
    _SleOspfv3IfInstanceControlBfd_Type()
)
sleOspfv3IfInstanceControlBfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlBfd.setStatus("current")


class _SleOspfv3IfInstanceControlEfm_Type(Integer32):
    """Custom type sleOspfv3IfInstanceControlEfm based on Integer32"""
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
          ("disable", 1),
          ("enable", 2))
    )


_SleOspfv3IfInstanceControlEfm_Type.__name__ = "Integer32"
_SleOspfv3IfInstanceControlEfm_Object = MibScalar
sleOspfv3IfInstanceControlEfm = _SleOspfv3IfInstanceControlEfm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 2, 19),
    _SleOspfv3IfInstanceControlEfm_Type()
)
sleOspfv3IfInstanceControlEfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceControlEfm.setStatus("current")
_SleOspfv3IfInstanceNotifications_ObjectIdentity = ObjectIdentity
sleOspfv3IfInstanceNotifications = _SleOspfv3IfInstanceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 3)
)
_SleOspfv3IfNeighbor_ObjectIdentity = ObjectIdentity
sleOspfv3IfNeighbor = _SleOspfv3IfNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2)
)
_SleOspfv3IfNeighborTable_Object = MibTable
sleOspfv3IfNeighborTable = _SleOspfv3IfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborTable.setStatus("current")
_SleOspfv3IfNeighborEntry_Object = MibTableRow
sleOspfv3IfNeighborEntry = _SleOspfv3IfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 1, 1)
)
sleOspfv3IfNeighborEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3IfInstanceIfIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3IfInstanceInstanceId"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3IfNeighborAddress"),
)
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborEntry.setStatus("current")
_SleOspfv3IfNeighborAddress_Type = InetAddressIPv6
_SleOspfv3IfNeighborAddress_Object = MibTableColumn
sleOspfv3IfNeighborAddress = _SleOspfv3IfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 1, 1, 1),
    _SleOspfv3IfNeighborAddress_Type()
)
sleOspfv3IfNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborAddress.setStatus("current")


class _SleOspfv3IfNeighborCost_Type(Integer32):
    """Custom type sleOspfv3IfNeighborCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfNeighborCost_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborCost_Object = MibTableColumn
sleOspfv3IfNeighborCost = _SleOspfv3IfNeighborCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 1, 1, 2),
    _SleOspfv3IfNeighborCost_Type()
)
sleOspfv3IfNeighborCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborCost.setStatus("current")


class _SleOspfv3IfNeighborPollIntervalFlag_Type(Integer32):
    """Custom type sleOspfv3IfNeighborPollIntervalFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noUse", 0),
          ("use", 1))
    )


_SleOspfv3IfNeighborPollIntervalFlag_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborPollIntervalFlag_Object = MibTableColumn
sleOspfv3IfNeighborPollIntervalFlag = _SleOspfv3IfNeighborPollIntervalFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 1, 1, 3),
    _SleOspfv3IfNeighborPollIntervalFlag_Type()
)
sleOspfv3IfNeighborPollIntervalFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborPollIntervalFlag.setStatus("current")


class _SleOspfv3IfNeighborPollIntervalValue_Type(Unsigned32):
    """Custom type sleOspfv3IfNeighborPollIntervalValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleOspfv3IfNeighborPollIntervalValue_Type.__name__ = "Unsigned32"
_SleOspfv3IfNeighborPollIntervalValue_Object = MibTableColumn
sleOspfv3IfNeighborPollIntervalValue = _SleOspfv3IfNeighborPollIntervalValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 1, 1, 4),
    _SleOspfv3IfNeighborPollIntervalValue_Type()
)
sleOspfv3IfNeighborPollIntervalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborPollIntervalValue.setStatus("current")


class _SleOspfv3IfNeighborPriority_Type(Integer32):
    """Custom type sleOspfv3IfNeighborPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfNeighborPriority_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborPriority_Object = MibTableColumn
sleOspfv3IfNeighborPriority = _SleOspfv3IfNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 1, 1, 5),
    _SleOspfv3IfNeighborPriority_Type()
)
sleOspfv3IfNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborPriority.setStatus("current")
_SleOspfv3ProcIfNeighborControl_ObjectIdentity = ObjectIdentity
sleOspfv3ProcIfNeighborControl = _SleOspfv3ProcIfNeighborControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2)
)


class _SleOspfv3IfNeighborControlRequest_Type(Integer32):
    """Custom type sleOspfv3IfNeighborControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOspfv3IfNeighbor", 1),
          ("modifyOspfv3IfNeighbor", 2),
          ("destroyOspfv3IfNeighbor", 3))
    )


_SleOspfv3IfNeighborControlRequest_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborControlRequest_Object = MibScalar
sleOspfv3IfNeighborControlRequest = _SleOspfv3IfNeighborControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 1),
    _SleOspfv3IfNeighborControlRequest_Type()
)
sleOspfv3IfNeighborControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlRequest.setStatus("current")
_SleOspfv3IfNeighborControlStatus_Type = SleControlStatusType
_SleOspfv3IfNeighborControlStatus_Object = MibScalar
sleOspfv3IfNeighborControlStatus = _SleOspfv3IfNeighborControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 2),
    _SleOspfv3IfNeighborControlStatus_Type()
)
sleOspfv3IfNeighborControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlStatus.setStatus("current")
_SleOspfv3IfNeighborControlTimer_Type = Gauge32
_SleOspfv3IfNeighborControlTimer_Object = MibScalar
sleOspfv3IfNeighborControlTimer = _SleOspfv3IfNeighborControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 3),
    _SleOspfv3IfNeighborControlTimer_Type()
)
sleOspfv3IfNeighborControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlTimer.setStatus("current")
_SleOspfv3IfNeighborControlTimeStamp_Type = TimeTicks
_SleOspfv3IfNeighborControlTimeStamp_Object = MibScalar
sleOspfv3IfNeighborControlTimeStamp = _SleOspfv3IfNeighborControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 4),
    _SleOspfv3IfNeighborControlTimeStamp_Type()
)
sleOspfv3IfNeighborControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlTimeStamp.setStatus("current")
_SleOspfv3IfNeighborControlReqResult_Type = SleControlRequestResultType
_SleOspfv3IfNeighborControlReqResult_Object = MibScalar
sleOspfv3IfNeighborControlReqResult = _SleOspfv3IfNeighborControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 5),
    _SleOspfv3IfNeighborControlReqResult_Type()
)
sleOspfv3IfNeighborControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlReqResult.setStatus("current")


class _SleOspfv3IfNeighborControlIndex_Type(Integer32):
    """Custom type sleOspfv3IfNeighborControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleOspfv3IfNeighborControlIndex_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborControlIndex_Object = MibScalar
sleOspfv3IfNeighborControlIndex = _SleOspfv3IfNeighborControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 6),
    _SleOspfv3IfNeighborControlIndex_Type()
)
sleOspfv3IfNeighborControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlIndex.setStatus("current")


class _SleOspfv3IfNeighborControlInstanceIndex_Type(Integer32):
    """Custom type sleOspfv3IfNeighborControlInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfNeighborControlInstanceIndex_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborControlInstanceIndex_Object = MibScalar
sleOspfv3IfNeighborControlInstanceIndex = _SleOspfv3IfNeighborControlInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 7),
    _SleOspfv3IfNeighborControlInstanceIndex_Type()
)
sleOspfv3IfNeighborControlInstanceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlInstanceIndex.setStatus("current")
_SleOspfv3IfNeighborControlAddress_Type = InetAddressIPv6
_SleOspfv3IfNeighborControlAddress_Object = MibScalar
sleOspfv3IfNeighborControlAddress = _SleOspfv3IfNeighborControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 8),
    _SleOspfv3IfNeighborControlAddress_Type()
)
sleOspfv3IfNeighborControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlAddress.setStatus("current")


class _SleOspfv3IfNeighborControlCost_Type(Integer32):
    """Custom type sleOspfv3IfNeighborControlCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfNeighborControlCost_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborControlCost_Object = MibScalar
sleOspfv3IfNeighborControlCost = _SleOspfv3IfNeighborControlCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 9),
    _SleOspfv3IfNeighborControlCost_Type()
)
sleOspfv3IfNeighborControlCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlCost.setStatus("current")


class _SleOspfv3IfNeighborControlPollIntervalFlag_Type(Integer32):
    """Custom type sleOspfv3IfNeighborControlPollIntervalFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noUse", 0),
          ("use", 1))
    )


_SleOspfv3IfNeighborControlPollIntervalFlag_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborControlPollIntervalFlag_Object = MibScalar
sleOspfv3IfNeighborControlPollIntervalFlag = _SleOspfv3IfNeighborControlPollIntervalFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 10),
    _SleOspfv3IfNeighborControlPollIntervalFlag_Type()
)
sleOspfv3IfNeighborControlPollIntervalFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlPollIntervalFlag.setStatus("current")


class _SleOspfv3IfNeighborControlPollInterval_Type(Unsigned32):
    """Custom type sleOspfv3IfNeighborControlPollInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleOspfv3IfNeighborControlPollInterval_Type.__name__ = "Unsigned32"
_SleOspfv3IfNeighborControlPollInterval_Object = MibScalar
sleOspfv3IfNeighborControlPollInterval = _SleOspfv3IfNeighborControlPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 11),
    _SleOspfv3IfNeighborControlPollInterval_Type()
)
sleOspfv3IfNeighborControlPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlPollInterval.setStatus("current")


class _SleOspfv3IfNeighborControlPriority_Type(Integer32):
    """Custom type sleOspfv3IfNeighborControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfNeighborControlPriority_Type.__name__ = "Integer32"
_SleOspfv3IfNeighborControlPriority_Object = MibScalar
sleOspfv3IfNeighborControlPriority = _SleOspfv3IfNeighborControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 2, 12),
    _SleOspfv3IfNeighborControlPriority_Type()
)
sleOspfv3IfNeighborControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborControlPriority.setStatus("current")
_SleOspfv3IfNeighborNotifications_ObjectIdentity = ObjectIdentity
sleOspfv3IfNeighborNotifications = _SleOspfv3IfNeighborNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 3)
)
_SleOspfv3IfStatus_ObjectIdentity = ObjectIdentity
sleOspfv3IfStatus = _SleOspfv3IfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3)
)
_SleOspfv3IfStatusTable_Object = MibTable
sleOspfv3IfStatusTable = _SleOspfv3IfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3IfStatusTable.setStatus("current")
_SleOspfv3IfStatusEntry_Object = MibTableRow
sleOspfv3IfStatusEntry = _SleOspfv3IfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1)
)
sleOspfv3IfStatusEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3IfInstanceIfIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3IfInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    sleOspfv3IfStatusEntry.setStatus("current")


class _SleOspfv3IfStatusProcTag_Type(OctetString):
    """Custom type sleOspfv3IfStatusProcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOspfv3IfStatusProcTag_Type.__name__ = "OctetString"
_SleOspfv3IfStatusProcTag_Object = MibTableColumn
sleOspfv3IfStatusProcTag = _SleOspfv3IfStatusProcTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 1),
    _SleOspfv3IfStatusProcTag_Type()
)
sleOspfv3IfStatusProcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusProcTag.setStatus("current")
_SleOspfv3IfStatusAreaId_Type = InetAddressIPv4
_SleOspfv3IfStatusAreaId_Object = MibTableColumn
sleOspfv3IfStatusAreaId = _SleOspfv3IfStatusAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 2),
    _SleOspfv3IfStatusAreaId_Type()
)
sleOspfv3IfStatusAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusAreaId.setStatus("current")


class _SleOspfv3IfStatusNetworkType_Type(Integer32):
    """Custom type sleOspfv3IfStatusNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p2p", 1),
          ("broadcast", 2),
          ("nbma", 3),
          ("p2mp", 4),
          ("p2mpNbma", 5),
          ("virtualLink", 6),
          ("loopback", 7))
    )


_SleOspfv3IfStatusNetworkType_Type.__name__ = "Integer32"
_SleOspfv3IfStatusNetworkType_Object = MibTableColumn
sleOspfv3IfStatusNetworkType = _SleOspfv3IfStatusNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 3),
    _SleOspfv3IfStatusNetworkType_Type()
)
sleOspfv3IfStatusNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusNetworkType.setStatus("current")


class _SleOspfv3IfStatusCost_Type(Integer32):
    """Custom type sleOspfv3IfStatusCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfStatusCost_Type.__name__ = "Integer32"
_SleOspfv3IfStatusCost_Object = MibTableColumn
sleOspfv3IfStatusCost = _SleOspfv3IfStatusCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 4),
    _SleOspfv3IfStatusCost_Type()
)
sleOspfv3IfStatusCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusCost.setStatus("current")


class _SleOspfv3IfStatusTransDelay_Type(Integer32):
    """Custom type sleOspfv3IfStatusTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfStatusTransDelay_Type.__name__ = "Integer32"
_SleOspfv3IfStatusTransDelay_Object = MibTableColumn
sleOspfv3IfStatusTransDelay = _SleOspfv3IfStatusTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 5),
    _SleOspfv3IfStatusTransDelay_Type()
)
sleOspfv3IfStatusTransDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusTransDelay.setStatus("current")


class _SleOspfv3IfStatusState_Type(Integer32):
    """Custom type sleOspfv3IfStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dependUpon", 0),
          ("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("p2p", 4),
          ("drOther", 5),
          ("backup", 6),
          ("dr", 7))
    )


_SleOspfv3IfStatusState_Type.__name__ = "Integer32"
_SleOspfv3IfStatusState_Object = MibTableColumn
sleOspfv3IfStatusState = _SleOspfv3IfStatusState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 6),
    _SleOspfv3IfStatusState_Type()
)
sleOspfv3IfStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusState.setStatus("current")


class _SleOspfv3IfStatusPriority_Type(Integer32):
    """Custom type sleOspfv3IfStatusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOspfv3IfStatusPriority_Type.__name__ = "Integer32"
_SleOspfv3IfStatusPriority_Object = MibTableColumn
sleOspfv3IfStatusPriority = _SleOspfv3IfStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 7),
    _SleOspfv3IfStatusPriority_Type()
)
sleOspfv3IfStatusPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusPriority.setStatus("current")
_SleOspfv3IfStatusDRRouterId_Type = InetAddressIPv4
_SleOspfv3IfStatusDRRouterId_Object = MibTableColumn
sleOspfv3IfStatusDRRouterId = _SleOspfv3IfStatusDRRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 8),
    _SleOspfv3IfStatusDRRouterId_Type()
)
sleOspfv3IfStatusDRRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusDRRouterId.setStatus("current")
_SleOspfv3IfStatusDRAddress_Type = InetAddressIPv6
_SleOspfv3IfStatusDRAddress_Object = MibTableColumn
sleOspfv3IfStatusDRAddress = _SleOspfv3IfStatusDRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 9),
    _SleOspfv3IfStatusDRAddress_Type()
)
sleOspfv3IfStatusDRAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusDRAddress.setStatus("current")
_SleOspfv3IfStatusBackupRouterId_Type = InetAddressIPv4
_SleOspfv3IfStatusBackupRouterId_Object = MibTableColumn
sleOspfv3IfStatusBackupRouterId = _SleOspfv3IfStatusBackupRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 10),
    _SleOspfv3IfStatusBackupRouterId_Type()
)
sleOspfv3IfStatusBackupRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusBackupRouterId.setStatus("current")
_SleOspfv3IfStatusBackupAddress_Type = InetAddressIPv6
_SleOspfv3IfStatusBackupAddress_Object = MibTableColumn
sleOspfv3IfStatusBackupAddress = _SleOspfv3IfStatusBackupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 11),
    _SleOspfv3IfStatusBackupAddress_Type()
)
sleOspfv3IfStatusBackupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusBackupAddress.setStatus("current")


class _SleOspfv3IfStatusHelloInterval_Type(Integer32):
    """Custom type sleOspfv3IfStatusHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfStatusHelloInterval_Type.__name__ = "Integer32"
_SleOspfv3IfStatusHelloInterval_Object = MibTableColumn
sleOspfv3IfStatusHelloInterval = _SleOspfv3IfStatusHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 12),
    _SleOspfv3IfStatusHelloInterval_Type()
)
sleOspfv3IfStatusHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusHelloInterval.setStatus("current")


class _SleOspfv3IfStatusDeadInterval_Type(Integer32):
    """Custom type sleOspfv3IfStatusDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfStatusDeadInterval_Type.__name__ = "Integer32"
_SleOspfv3IfStatusDeadInterval_Object = MibTableColumn
sleOspfv3IfStatusDeadInterval = _SleOspfv3IfStatusDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 13),
    _SleOspfv3IfStatusDeadInterval_Type()
)
sleOspfv3IfStatusDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusDeadInterval.setStatus("current")


class _SleOspfv3IfStatusWaitInterval_Type(Integer32):
    """Custom type sleOspfv3IfStatusWaitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfStatusWaitInterval_Type.__name__ = "Integer32"
_SleOspfv3IfStatusWaitInterval_Object = MibTableColumn
sleOspfv3IfStatusWaitInterval = _SleOspfv3IfStatusWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 14),
    _SleOspfv3IfStatusWaitInterval_Type()
)
sleOspfv3IfStatusWaitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusWaitInterval.setStatus("current")


class _SleOspfv3IfStatusRetransInterval_Type(Integer32):
    """Custom type sleOspfv3IfStatusRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfStatusRetransInterval_Type.__name__ = "Integer32"
_SleOspfv3IfStatusRetransInterval_Object = MibTableColumn
sleOspfv3IfStatusRetransInterval = _SleOspfv3IfStatusRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 15),
    _SleOspfv3IfStatusRetransInterval_Type()
)
sleOspfv3IfStatusRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfStatusRetransInterval.setStatus("current")
_SleOspfv3IfNeighborCount_Type = Integer32
_SleOspfv3IfNeighborCount_Object = MibTableColumn
sleOspfv3IfNeighborCount = _SleOspfv3IfNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 16),
    _SleOspfv3IfNeighborCount_Type()
)
sleOspfv3IfNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborCount.setStatus("current")


class _SleOspfv3IfAdjNeighborCount_Type(Integer32):
    """Custom type sleOspfv3IfAdjNeighborCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOspfv3IfAdjNeighborCount_Type.__name__ = "Integer32"
_SleOspfv3IfAdjNeighborCount_Object = MibTableColumn
sleOspfv3IfAdjNeighborCount = _SleOspfv3IfAdjNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 3, 1, 1, 17),
    _SleOspfv3IfAdjNeighborCount_Type()
)
sleOspfv3IfAdjNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3IfAdjNeighborCount.setStatus("current")
_SleOspfv3Lsdb_ObjectIdentity = ObjectIdentity
sleOspfv3Lsdb = _SleOspfv3Lsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4)
)
_SleOspfv3LsdbTable_Object = MibTable
sleOspfv3LsdbTable = _SleOspfv3LsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3LsdbTable.setStatus("current")
_SleOspfv3LsdbEntry_Object = MibTableRow
sleOspfv3LsdbEntry = _SleOspfv3LsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1, 1)
)
sleOspfv3LsdbEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3LsdbType"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3LsdbLinkStateId"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3LsdbAdvRouterId"),
)
if mibBuilder.loadTexts:
    sleOspfv3LsdbEntry.setStatus("current")


class _SleOspfv3LsdbType_Type(Integer32):
    """Custom type sleOspfv3LsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("unknown", 0),
          ("router", 1),
          ("network", 2),
          ("interPrefix", 3),
          ("interRouter", 4),
          ("asExternal", 5),
          ("groupMembership", 6),
          ("nssa", 7),
          ("link", 8),
          ("intraPrefix", 9))
    )


_SleOspfv3LsdbType_Type.__name__ = "Integer32"
_SleOspfv3LsdbType_Object = MibTableColumn
sleOspfv3LsdbType = _SleOspfv3LsdbType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1, 1, 1),
    _SleOspfv3LsdbType_Type()
)
sleOspfv3LsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3LsdbType.setStatus("current")
_SleOspfv3LsdbLinkStateId_Type = InetAddressIPv4
_SleOspfv3LsdbLinkStateId_Object = MibTableColumn
sleOspfv3LsdbLinkStateId = _SleOspfv3LsdbLinkStateId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1, 1, 2),
    _SleOspfv3LsdbLinkStateId_Type()
)
sleOspfv3LsdbLinkStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3LsdbLinkStateId.setStatus("current")
_SleOspfv3LsdbAdvRouterId_Type = InetAddressIPv4
_SleOspfv3LsdbAdvRouterId_Object = MibTableColumn
sleOspfv3LsdbAdvRouterId = _SleOspfv3LsdbAdvRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1, 1, 3),
    _SleOspfv3LsdbAdvRouterId_Type()
)
sleOspfv3LsdbAdvRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3LsdbAdvRouterId.setStatus("current")
_SleOspfv3LsdbAge_Type = Integer32
_SleOspfv3LsdbAge_Object = MibTableColumn
sleOspfv3LsdbAge = _SleOspfv3LsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1, 1, 4),
    _SleOspfv3LsdbAge_Type()
)
sleOspfv3LsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3LsdbAge.setStatus("current")
_SleOspfv3LsdbSeqnum_Type = Unsigned32
_SleOspfv3LsdbSeqnum_Object = MibTableColumn
sleOspfv3LsdbSeqnum = _SleOspfv3LsdbSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1, 1, 5),
    _SleOspfv3LsdbSeqnum_Type()
)
sleOspfv3LsdbSeqnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3LsdbSeqnum.setStatus("current")
_SleOspfv3LsdbLength_Type = Integer32
_SleOspfv3LsdbLength_Object = MibTableColumn
sleOspfv3LsdbLength = _SleOspfv3LsdbLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 4, 1, 1, 6),
    _SleOspfv3LsdbLength_Type()
)
sleOspfv3LsdbLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3LsdbLength.setStatus("current")
_SleOspfv3Neighbor_ObjectIdentity = ObjectIdentity
sleOspfv3Neighbor = _SleOspfv3Neighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5)
)
_SleOspfv3NeigborTable_Object = MibTable
sleOspfv3NeigborTable = _SleOspfv3NeigborTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3NeigborTable.setStatus("current")
_SleOspfv3NeigborEntry_Object = MibTableRow
sleOspfv3NeigborEntry = _SleOspfv3NeigborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1)
)
sleOspfv3NeigborEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3NeighborRouterId"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3NeighborIfType"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3NeighborAddress"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3NeighborIfIndex"),
)
if mibBuilder.loadTexts:
    sleOspfv3NeigborEntry.setStatus("current")


class _SleOspfv3NeighborIfType_Type(Integer32):
    """Custom type sleOspfv3NeighborIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("virtual", 2))
    )


_SleOspfv3NeighborIfType_Type.__name__ = "Integer32"
_SleOspfv3NeighborIfType_Object = MibTableColumn
sleOspfv3NeighborIfType = _SleOspfv3NeighborIfType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 1),
    _SleOspfv3NeighborIfType_Type()
)
sleOspfv3NeighborIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborIfType.setStatus("current")


class _SleOspfv3NeighborIfIndex_Type(Unsigned32):
    """Custom type sleOspfv3NeighborIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SleOspfv3NeighborIfIndex_Type.__name__ = "Unsigned32"
_SleOspfv3NeighborIfIndex_Object = MibTableColumn
sleOspfv3NeighborIfIndex = _SleOspfv3NeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 2),
    _SleOspfv3NeighborIfIndex_Type()
)
sleOspfv3NeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborIfIndex.setStatus("current")
_SleOspfv3NeighborRouterId_Type = InetAddressIPv4
_SleOspfv3NeighborRouterId_Object = MibTableColumn
sleOspfv3NeighborRouterId = _SleOspfv3NeighborRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 3),
    _SleOspfv3NeighborRouterId_Type()
)
sleOspfv3NeighborRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborRouterId.setStatus("current")
_SleOspfv3NeighborAddress_Type = InetAddressIPv6
_SleOspfv3NeighborAddress_Object = MibTableColumn
sleOspfv3NeighborAddress = _SleOspfv3NeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 4),
    _SleOspfv3NeighborAddress_Type()
)
sleOspfv3NeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborAddress.setStatus("current")
_SleOspfv3NeighborAreaId_Type = InetAddressIPv4
_SleOspfv3NeighborAreaId_Object = MibTableColumn
sleOspfv3NeighborAreaId = _SleOspfv3NeighborAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 5),
    _SleOspfv3NeighborAreaId_Type()
)
sleOspfv3NeighborAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3NeighborAreaId.setStatus("current")


class _SleOspfv3NeighborIfName_Type(OctetString):
    """Custom type sleOspfv3NeighborIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SleOspfv3NeighborIfName_Type.__name__ = "OctetString"
_SleOspfv3NeighborIfName_Object = MibTableColumn
sleOspfv3NeighborIfName = _SleOspfv3NeighborIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 6),
    _SleOspfv3NeighborIfName_Type()
)
sleOspfv3NeighborIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborIfName.setStatus("current")
_SleOspfv3NeighborPriority_Type = Integer32
_SleOspfv3NeighborPriority_Object = MibTableColumn
sleOspfv3NeighborPriority = _SleOspfv3NeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 7),
    _SleOspfv3NeighborPriority_Type()
)
sleOspfv3NeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborPriority.setStatus("current")


class _SleOspfv3NeighborState_Type(Integer32):
    """Custom type sleOspfv3NeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("dependUpon", 0),
          ("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_SleOspfv3NeighborState_Type.__name__ = "Integer32"
_SleOspfv3NeighborState_Object = MibTableColumn
sleOspfv3NeighborState = _SleOspfv3NeighborState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 8),
    _SleOspfv3NeighborState_Type()
)
sleOspfv3NeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborState.setStatus("current")
_SleOspfv3NeighborInstanceId_Type = Integer32
_SleOspfv3NeighborInstanceId_Object = MibTableColumn
sleOspfv3NeighborInstanceId = _SleOspfv3NeighborInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 9),
    _SleOspfv3NeighborInstanceId_Type()
)
sleOspfv3NeighborInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborInstanceId.setStatus("current")
_SleOspfv3NeighborDRRouterId_Type = InetAddressIPv4
_SleOspfv3NeighborDRRouterId_Object = MibTableColumn
sleOspfv3NeighborDRRouterId = _SleOspfv3NeighborDRRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 10),
    _SleOspfv3NeighborDRRouterId_Type()
)
sleOspfv3NeighborDRRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborDRRouterId.setStatus("current")
_SleOspfv3NeighborBDRRouterId_Type = InetAddressIPv4
_SleOspfv3NeighborBDRRouterId_Object = MibTableColumn
sleOspfv3NeighborBDRRouterId = _SleOspfv3NeighborBDRRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 11),
    _SleOspfv3NeighborBDRRouterId_Type()
)
sleOspfv3NeighborBDRRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborBDRRouterId.setStatus("current")


class _SleOspfv3NeighborOption_Type(Bits):
    """Custom type sleOspfv3NeighborOption based on Bits"""
    namedValues = NamedValues(
        *(("forwarding", 0),
          ("externalRouting", 1),
          ("mcastForwarding", 2),
          ("nssaLsa", 3),
          ("anyProtocol", 4),
          ("demand", 5))
    )

_SleOspfv3NeighborOption_Type.__name__ = "Bits"
_SleOspfv3NeighborOption_Object = MibTableColumn
sleOspfv3NeighborOption = _SleOspfv3NeighborOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 12),
    _SleOspfv3NeighborOption_Type()
)
sleOspfv3NeighborOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborOption.setStatus("current")
_SleOspfv3NeighborDeadTime_Type = TimeTicks
_SleOspfv3NeighborDeadTime_Object = MibTableColumn
sleOspfv3NeighborDeadTime = _SleOspfv3NeighborDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 13),
    _SleOspfv3NeighborDeadTime_Type()
)
sleOspfv3NeighborDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborDeadTime.setStatus("current")
_SleOspfv3NeighborLsdbCount_Type = Unsigned32
_SleOspfv3NeighborLsdbCount_Object = MibTableColumn
sleOspfv3NeighborLsdbCount = _SleOspfv3NeighborLsdbCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 14),
    _SleOspfv3NeighborLsdbCount_Type()
)
sleOspfv3NeighborLsdbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborLsdbCount.setStatus("current")
_SleOspfv3NeighborLsreqCount_Type = Unsigned32
_SleOspfv3NeighborLsreqCount_Object = MibTableColumn
sleOspfv3NeighborLsreqCount = _SleOspfv3NeighborLsreqCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 15),
    _SleOspfv3NeighborLsreqCount_Type()
)
sleOspfv3NeighborLsreqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborLsreqCount.setStatus("current")
_SleOspfv3NeighborLsrxmitCount_Type = Unsigned32
_SleOspfv3NeighborLsrxmitCount_Object = MibTableColumn
sleOspfv3NeighborLsrxmitCount = _SleOspfv3NeighborLsrxmitCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 5, 1, 1, 16),
    _SleOspfv3NeighborLsrxmitCount_Type()
)
sleOspfv3NeighborLsrxmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3NeighborLsrxmitCount.setStatus("current")
_SleOspfv3Route_ObjectIdentity = ObjectIdentity
sleOspfv3Route = _SleOspfv3Route_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6)
)
_SleOspfv3RouteTable_Object = MibTable
sleOspfv3RouteTable = _SleOspfv3RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1)
)
if mibBuilder.loadTexts:
    sleOspfv3RouteTable.setStatus("current")
_SleOspfv3RouteEntry_Object = MibTableRow
sleOspfv3RouteEntry = _SleOspfv3RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1)
)
sleOspfv3RouteEntry.setIndexNames(
    (0, "SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3RouteNetAddr"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3RouteNetMask"),
    (0, "SLE-OSPFv3-MIB", "sleOspfv3RouteNexthop"),
)
if mibBuilder.loadTexts:
    sleOspfv3RouteEntry.setStatus("current")
_SleOspfv3RouteNetAddr_Type = InetAddressIPv6
_SleOspfv3RouteNetAddr_Object = MibTableColumn
sleOspfv3RouteNetAddr = _SleOspfv3RouteNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 1),
    _SleOspfv3RouteNetAddr_Type()
)
sleOspfv3RouteNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RouteNetAddr.setStatus("current")


class _SleOspfv3RouteNetMask_Type(Integer32):
    """Custom type sleOspfv3RouteNetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleOspfv3RouteNetMask_Type.__name__ = "Integer32"
_SleOspfv3RouteNetMask_Object = MibTableColumn
sleOspfv3RouteNetMask = _SleOspfv3RouteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 2),
    _SleOspfv3RouteNetMask_Type()
)
sleOspfv3RouteNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RouteNetMask.setStatus("current")
_SleOspfv3RouteNexthop_Type = InetAddressIPv6
_SleOspfv3RouteNexthop_Object = MibTableColumn
sleOspfv3RouteNexthop = _SleOspfv3RouteNexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 3),
    _SleOspfv3RouteNexthop_Type()
)
sleOspfv3RouteNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RouteNexthop.setStatus("current")


class _SleOspfv3RouteType_Type(Integer32):
    """Custom type sleOspfv3RouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("unknown", 0),
          ("connected", 1),
          ("intra", 2),
          ("inter", 3),
          ("externE1", 4),
          ("externE2", 5),
          ("externN1", 6),
          ("externN2", 7),
          ("discard", 8))
    )


_SleOspfv3RouteType_Type.__name__ = "Integer32"
_SleOspfv3RouteType_Object = MibTableColumn
sleOspfv3RouteType = _SleOspfv3RouteType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 4),
    _SleOspfv3RouteType_Type()
)
sleOspfv3RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOspfv3RouteType.setStatus("current")
_SleOspfv3RouteMetric_Type = Integer32
_SleOspfv3RouteMetric_Object = MibTableColumn
sleOspfv3RouteMetric = _SleOspfv3RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 5),
    _SleOspfv3RouteMetric_Type()
)
sleOspfv3RouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3RouteMetric.setStatus("current")


class _SleOspfv3RouteIfName_Type(OctetString):
    """Custom type sleOspfv3RouteIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SleOspfv3RouteIfName_Type.__name__ = "OctetString"
_SleOspfv3RouteIfName_Object = MibTableColumn
sleOspfv3RouteIfName = _SleOspfv3RouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 6),
    _SleOspfv3RouteIfName_Type()
)
sleOspfv3RouteIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3RouteIfName.setStatus("current")


class _SleOspfv3RouteAreaFlag_Type(Integer32):
    """Custom type sleOspfv3RouteAreaFlag based on Integer32"""
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
          ("upon", 1),
          ("transit", 2))
    )


_SleOspfv3RouteAreaFlag_Type.__name__ = "Integer32"
_SleOspfv3RouteAreaFlag_Object = MibTableColumn
sleOspfv3RouteAreaFlag = _SleOspfv3RouteAreaFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 7),
    _SleOspfv3RouteAreaFlag_Type()
)
sleOspfv3RouteAreaFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3RouteAreaFlag.setStatus("current")
_SleOspfv3RouteAreaId_Type = InetAddressIPv4
_SleOspfv3RouteAreaId_Object = MibTableColumn
sleOspfv3RouteAreaId = _SleOspfv3RouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 6, 1, 1, 8),
    _SleOspfv3RouteAreaId_Type()
)
sleOspfv3RouteAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOspfv3RouteAreaId.setStatus("current")

# Managed Objects groups

sleOspfv3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 7)
)
sleOspfv3Group.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3RouteDisplayMode"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlRouteDisplayMode"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSpfDelayTime"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSpfHoldTime"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAutoCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAbrType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultMetric"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcMaxConcurrentDD"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginMetricType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginMetric"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginRouteMap"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLogNeighborChange"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcBfdAllIf"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcEfmAllIf"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcVRIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcVRFName"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlSpfDelayTime"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlSpfHoldTime"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlAutoCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlAbrType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlDefaultMetric"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlMaxConcurrentDD"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlDefaultOriginType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlDefaultOriginMetricType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlDefaultOriginMetric"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlDefaultOriginRouteMap"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlLogNeighborChange"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlBfdAllIf"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlEfmAllIf"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlVRIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlVRFName"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryMask"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryAdvertiseFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlMask"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlAdvertiseFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlIfIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistMetricType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistMetric"),
        ("SLE-OSPFv3-MIB", "sleOSpfv3ProcRedistRouteMapName"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlMetricType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlMetric"),
        ("SLE-OSPFv3-MIB", "sleOSpfv3ProcRedistControlRouteMapName"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoDefaultCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoSummary"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlDefaultCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlSummary"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeMask"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeAdvertiseFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlAddr"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlMask"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlAdvertiseFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkInstanceId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkTransDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlInstanceId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlTransDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceIfIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceInstanceId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceProcTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceAreaFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceNetworkType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceTransDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstancePriority"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceBfd"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceEfm"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlIfIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlIfInstanceId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlProcTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlAreaFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlNetworkType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlTransDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlPriority"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlBfd"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlEfm"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPollIntervalFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPollIntervalValue"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPriority"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlStatus"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlTimer"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlInstanceIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlPollIntervalFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlPollInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlPriority"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusProcTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusAreaId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusNetworkType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusTransDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusState"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusPriority"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusDRRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusDRAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusBackupRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusBackupAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusWaitInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfStatusRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborCount"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfAdjNeighborCount"),
        ("SLE-OSPFv3-MIB", "sleOspfv3LsdbType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3LsdbLinkStateId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3LsdbAdvRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3LsdbAge"),
        ("SLE-OSPFv3-MIB", "sleOspfv3LsdbSeqnum"),
        ("SLE-OSPFv3-MIB", "sleOspfv3LsdbLength"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborIfType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborIfIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborAreaId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborIfName"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborPriority"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborState"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborInstanceId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborDRRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborBDRRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborOption"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborDeadTime"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborLsdbCount"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborLsreqCount"),
        ("SLE-OSPFv3-MIB", "sleOspfv3NeighborLsrxmitCount"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteNetAddr"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteNetMask"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteNexthop"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteMetric"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteIfName"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteAreaFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSPFStartDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSPFMinDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSPFMaxDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAStartDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAMinDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAMaxDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAArrivalDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlSPFStartDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlSPFMinDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlSPFMaxDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlLSAStartDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlLSAMinDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlLSAMaxDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlLSAArrivalDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RouteAreaId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartPeriod"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartHelperPolicy"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartHelperPeriod"),
        ("SLE-OSPFv3-MIB", "sleOspfv3SnmpNotification"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlRestartPeriod"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlRestartHelperPolicy"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlRestartHelperPeriod"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlSnmpNotification"))
)
if mibBuilder.loadTexts:
    sleOspfv3Group.setStatus("current")


# Notification objects

sleOspfv3RouteDisplayModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 3, 1)
)
sleOspfv3RouteDisplayModeChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlRouteDisplayMode"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlReqResult"))
)
if mibBuilder.loadTexts:
    sleOspfv3RouteDisplayModeChanged.setStatus(
        "current"
    )

sleOspfv3RestartPeriodChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 3, 2)
)
sleOspfv3RestartPeriodChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartPeriod"))
)
if mibBuilder.loadTexts:
    sleOspfv3RestartPeriodChanged.setStatus(
        "current"
    )

sleOspfv3RestartHelperProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 3, 3)
)
sleOspfv3RestartHelperProfileChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartHelperPolicy"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartHelperPeriod"))
)
if mibBuilder.loadTexts:
    sleOspfv3RestartHelperProfileChanged.setStatus(
        "current"
    )

sleOspfv3GracefulRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 3, 4)
)
sleOspfv3GracefulRestarted.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlRestartPeriod"))
)
if mibBuilder.loadTexts:
    sleOspfv3GracefulRestarted.setStatus(
        "current"
    )

sleOspfv3SnmpNotificationiChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 1, 3, 5)
)
sleOspfv3SnmpNotificationiChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3SnmpNotification"))
)
if mibBuilder.loadTexts:
    sleOspfv3SnmpNotificationiChanged.setStatus(
        "current"
    )

sleOspfv3ProcCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 3, 1)
)
sleOspfv3ProcCreated.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcVRIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcVRFName"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcCreated.setStatus(
        "current"
    )

sleOspfv3ProcProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 3, 2)
)
sleOspfv3ProcProfileChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSPFStartDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSPFMinDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSPFMaxDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAStartDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAMinDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAMaxDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLSAArrivalDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRouterId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSpfDelayTime"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSpfHoldTime"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAutoCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAbrType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultMetric"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcMaxConcurrentDD"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginMetricType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginMetric"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDefaultOriginRouteMap"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcLogNeighborChange"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcBfdAllIf"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcEfmAllIf"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcProfileChanged.setStatus(
        "current"
    )

sleOspfv3ProcDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 3, 3)
)
sleOspfv3ProcDestroyed.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlVRIndex"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcDestroyed.setStatus(
        "current"
    )

sleOspfv3ProcCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 1, 3, 4)
)
sleOspfv3ProcCleared.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcControlIndex"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcCleared.setStatus(
        "current"
    )

sleOspfv3ProcSummaryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 3, 1)
)
sleOspfv3ProcSummaryCreated.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryCreated.setStatus(
        "current"
    )

sleOspfv3ProcSummaryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 3, 2)
)
sleOspfv3ProcSummaryChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryChanged.setStatus(
        "current"
    )

sleOspfv3ProcSummaryDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 2, 3, 3)
)
sleOspfv3ProcSummaryDestroyed.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlAddress"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryControlMask"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcSummaryDestroyed.setStatus(
        "current"
    )

sleOspfv3ProcPassiveIfAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 3, 1)
)
sleOspfv3ProcPassiveIfAdded.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfIndex"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfAdded.setStatus(
        "current"
    )

sleOspfv3ProcPassiveIfDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 3, 3, 2)
)
sleOspfv3ProcPassiveIfDeleted.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfControlIfIndex"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcPassiveIfDeleted.setStatus(
        "current"
    )

sleOspfv3ProcRedistCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 3, 1)
)
sleOspfv3ProcRedistCreated.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistMetricType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistMetric"),
        ("SLE-OSPFv3-MIB", "sleOSpfv3ProcRedistRouteMapName"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistCreated.setStatus(
        "current"
    )

sleOspfv3ProcRedistChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 3, 2)
)
sleOspfv3ProcRedistChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistMetricType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistMetric"),
        ("SLE-OSPFv3-MIB", "sleOSpfv3ProcRedistRouteMapName"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistChanged.setStatus(
        "current"
    )

sleOspfv3ProcRedistDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 4, 3, 3)
)
sleOspfv3ProcRedistDestroyed.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistControlType"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcRedistDestroyed.setStatus(
        "current"
    )

sleOspfv3ProcAreaInfoCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 3, 1)
)
sleOspfv3ProcAreaInfoCreated.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoDefaultCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoSummary"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoCreated.setStatus(
        "current"
    )

sleOspfv3ProcAreaInfoChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 3, 2)
)
sleOspfv3ProcAreaInfoChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoDefaultCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoSummary"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoChanged.setStatus(
        "current"
    )

sleOspfv3ProcAreaInfoDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 1, 3, 3)
)
sleOspfv3ProcAreaInfoDestroyed.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoControlAreaIndex"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaInfoDestroyed.setStatus(
        "current"
    )

sleOspfv3ProcAreaRangeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 3, 1)
)
sleOspfv3ProcAreaRangeCreated.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeCreated.setStatus(
        "current"
    )

sleOspfv3ProcAreaRangeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 3, 2)
)
sleOspfv3ProcAreaRangeChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeChanged.setStatus(
        "current"
    )

sleOspfv3ProcAreaRangeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 2, 3, 3)
)
sleOspfv3ProcAreaRangeDestroyed.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlMask"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeControlAddr"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaRangeDestroyed.setStatus(
        "current"
    )

sleOspfv3ProcAreaVlinkCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 3, 1)
)
sleOspfv3ProcAreaVlinkCreated.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkInstanceId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkTransDelay"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkCreated.setStatus(
        "current"
    )

sleOspfv3ProcAreaVlinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 3, 2)
)
sleOspfv3ProcAreaVlinkChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkInstanceId"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkTransDelay"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkChanged.setStatus(
        "current"
    )

sleOspfv3ProcAreaVlinkDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 2, 5, 3, 3, 3)
)
sleOspfv3ProcAreaVlinkDestroyed.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkControlRouterId"))
)
if mibBuilder.loadTexts:
    sleOspfv3ProcAreaVlinkDestroyed.setStatus(
        "current"
    )

sleOspfv3IfInstanceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 1, 3, 1)
)
sleOspfv3IfInstanceChanged.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceProcTag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceAreaFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceAreaIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceDeadInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceHelloInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceNetworkType"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceTransDelay"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceRetransInterval"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstancePriority"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceBfd"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceEfm"))
)
if mibBuilder.loadTexts:
    sleOspfv3IfInstanceChanged.setStatus(
        "current"
    )

sleOspfv3IfNeighborCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 3, 1)
)
sleOspfv3IfNeighborCreated.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPollIntervalFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPollIntervalValue"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPriority"))
)
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborCreated.setStatus(
        "current"
    )

sleOspfv3IfNeighborModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 3, 2)
)
sleOspfv3IfNeighborModified.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborCost"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPollIntervalFlag"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPollIntervalValue"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborPriority"))
)
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborModified.setStatus(
        "current"
    )

sleOspfv3IfNeighborDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 3, 2, 3, 3)
)
sleOspfv3IfNeighborDestroyed.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlRequest"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlTimeStamp"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlReqResult"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlInstanceIndex"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborControlAddress"))
)
if mibBuilder.loadTexts:
    sleOspfv3IfNeighborDestroyed.setStatus(
        "current"
    )


# Notifications groups

sleOspfv3NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 52, 8)
)
sleOspfv3NotificationGroup.setObjects(
      *(("SLE-OSPFv3-MIB", "sleOspfv3RouteDisplayModeChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcCreated"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcProfileChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcDestroyed"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcCleared"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryCreated"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcSummaryDestroyed"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfAdded"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcPassiveIfDeleted"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistCreated"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcRedistDestroyed"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoCreated"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaInfoDestroyed"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeCreated"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaRangeDestroyed"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkCreated"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3ProcAreaVlinkDestroyed"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfInstanceChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborCreated"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborModified"),
        ("SLE-OSPFv3-MIB", "sleOspfv3IfNeighborDestroyed"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartPeriodChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3RestartHelperProfileChanged"),
        ("SLE-OSPFv3-MIB", "sleOspfv3GracefulRestarted"),
        ("SLE-OSPFv3-MIB", "sleOspfv3SnmpNotificationiChanged"))
)
if mibBuilder.loadTexts:
    sleOspfv3NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-OSPFv3-MIB",
    **{"sleOSPFv3": sleOSPFv3,
       "sleOspfv3Base": sleOspfv3Base,
       "sleOspfv3BaseInfo": sleOspfv3BaseInfo,
       "sleOspfv3RouteDisplayMode": sleOspfv3RouteDisplayMode,
       "sleOspfv3RestartPeriod": sleOspfv3RestartPeriod,
       "sleOspfv3RestartHelperPolicy": sleOspfv3RestartHelperPolicy,
       "sleOspfv3RestartHelperPeriod": sleOspfv3RestartHelperPeriod,
       "sleOspfv3SnmpNotification": sleOspfv3SnmpNotification,
       "sleOspfv3BaseControl": sleOspfv3BaseControl,
       "sleOspfv3ControlRequest": sleOspfv3ControlRequest,
       "sleOspfv3ControlStatus": sleOspfv3ControlStatus,
       "sleOspfv3ControlTimer": sleOspfv3ControlTimer,
       "sleOspfv3ControlTimeStamp": sleOspfv3ControlTimeStamp,
       "sleOspfv3ControlReqResult": sleOspfv3ControlReqResult,
       "sleOspfv3ControlRouteDisplayMode": sleOspfv3ControlRouteDisplayMode,
       "sleOspfv3ControlRestartPeriod": sleOspfv3ControlRestartPeriod,
       "sleOspfv3ControlRestartHelperPolicy": sleOspfv3ControlRestartHelperPolicy,
       "sleOspfv3ControlRestartHelperPeriod": sleOspfv3ControlRestartHelperPeriod,
       "sleOspfv3ControlSnmpNotification": sleOspfv3ControlSnmpNotification,
       "sleOspfv3BaseNotification": sleOspfv3BaseNotification,
       "sleOspfv3RouteDisplayModeChanged": sleOspfv3RouteDisplayModeChanged,
       "sleOspfv3RestartPeriodChanged": sleOspfv3RestartPeriodChanged,
       "sleOspfv3RestartHelperProfileChanged": sleOspfv3RestartHelperProfileChanged,
       "sleOspfv3GracefulRestarted": sleOspfv3GracefulRestarted,
       "sleOspfv3SnmpNotificationiChanged": sleOspfv3SnmpNotificationiChanged,
       "sleOspfv3Proc": sleOspfv3Proc,
       "sleOspfv3ProcInfo": sleOspfv3ProcInfo,
       "sleOspfv3ProcInfoTable": sleOspfv3ProcInfoTable,
       "sleOspfv3ProcInfoEntry": sleOspfv3ProcInfoEntry,
       "sleOspfv3ProcIndex": sleOspfv3ProcIndex,
       "sleOspfv3ProcTag": sleOspfv3ProcTag,
       "sleOspfv3ProcRouterId": sleOspfv3ProcRouterId,
       "sleOspfv3ProcSpfDelayTime": sleOspfv3ProcSpfDelayTime,
       "sleOspfv3ProcSpfHoldTime": sleOspfv3ProcSpfHoldTime,
       "sleOspfv3ProcAutoCost": sleOspfv3ProcAutoCost,
       "sleOspfv3ProcAbrType": sleOspfv3ProcAbrType,
       "sleOspfv3ProcDefaultMetric": sleOspfv3ProcDefaultMetric,
       "sleOspfv3ProcMaxConcurrentDD": sleOspfv3ProcMaxConcurrentDD,
       "sleOspfv3ProcDefaultOriginType": sleOspfv3ProcDefaultOriginType,
       "sleOspfv3ProcDefaultOriginMetricType": sleOspfv3ProcDefaultOriginMetricType,
       "sleOspfv3ProcDefaultOriginMetric": sleOspfv3ProcDefaultOriginMetric,
       "sleOspfv3ProcDefaultOriginRouteMap": sleOspfv3ProcDefaultOriginRouteMap,
       "sleOspfv3ProcLogNeighborChange": sleOspfv3ProcLogNeighborChange,
       "sleOspfv3ProcBfdAllIf": sleOspfv3ProcBfdAllIf,
       "sleOspfv3ProcEfmAllIf": sleOspfv3ProcEfmAllIf,
       "sleOspfv3ProcVRIndex": sleOspfv3ProcVRIndex,
       "sleOspfv3ProcVRFName": sleOspfv3ProcVRFName,
       "sleOspfv3ProcSPFStartDelay": sleOspfv3ProcSPFStartDelay,
       "sleOspfv3ProcSPFMinDelay": sleOspfv3ProcSPFMinDelay,
       "sleOspfv3ProcSPFMaxDelay": sleOspfv3ProcSPFMaxDelay,
       "sleOspfv3ProcLSAStartDelay": sleOspfv3ProcLSAStartDelay,
       "sleOspfv3ProcLSAMinDelay": sleOspfv3ProcLSAMinDelay,
       "sleOspfv3ProcLSAMaxDelay": sleOspfv3ProcLSAMaxDelay,
       "sleOspfv3ProcLSAArrivalDelay": sleOspfv3ProcLSAArrivalDelay,
       "sleOspfv3ProcInfoControl": sleOspfv3ProcInfoControl,
       "sleOspfv3ProcControlRequest": sleOspfv3ProcControlRequest,
       "sleOspfv3ProcControlStatus": sleOspfv3ProcControlStatus,
       "sleOspfv3ProcControlTimer": sleOspfv3ProcControlTimer,
       "sleOspfv3ProcControlTimeStamp": sleOspfv3ProcControlTimeStamp,
       "sleOspfv3ProcControlReqResult": sleOspfv3ProcControlReqResult,
       "sleOspfv3ProcControlIndex": sleOspfv3ProcControlIndex,
       "sleOspfv3ProcControlTag": sleOspfv3ProcControlTag,
       "sleOspfv3ProcControlRouterId": sleOspfv3ProcControlRouterId,
       "sleOspfv3ProcControlSpfDelayTime": sleOspfv3ProcControlSpfDelayTime,
       "sleOspfv3ProcControlSpfHoldTime": sleOspfv3ProcControlSpfHoldTime,
       "sleOspfv3ProcControlAutoCost": sleOspfv3ProcControlAutoCost,
       "sleOspfv3ProcControlAbrType": sleOspfv3ProcControlAbrType,
       "sleOspfv3ProcControlDefaultMetric": sleOspfv3ProcControlDefaultMetric,
       "sleOspfv3ProcControlMaxConcurrentDD": sleOspfv3ProcControlMaxConcurrentDD,
       "sleOspfv3ProcControlDefaultOriginType": sleOspfv3ProcControlDefaultOriginType,
       "sleOspfv3ProcControlDefaultOriginMetricType": sleOspfv3ProcControlDefaultOriginMetricType,
       "sleOspfv3ProcControlDefaultOriginMetric": sleOspfv3ProcControlDefaultOriginMetric,
       "sleOspfv3ProcControlDefaultOriginRouteMap": sleOspfv3ProcControlDefaultOriginRouteMap,
       "sleOspfv3ProcControlLogNeighborChange": sleOspfv3ProcControlLogNeighborChange,
       "sleOspfv3ProcControlBfdAllIf": sleOspfv3ProcControlBfdAllIf,
       "sleOspfv3ProcControlEfmAllIf": sleOspfv3ProcControlEfmAllIf,
       "sleOspfv3ProcControlVRIndex": sleOspfv3ProcControlVRIndex,
       "sleOspfv3ProcControlVRFName": sleOspfv3ProcControlVRFName,
       "sleOspfv3ProcControlSPFStartDelay": sleOspfv3ProcControlSPFStartDelay,
       "sleOspfv3ProcControlSPFMinDelay": sleOspfv3ProcControlSPFMinDelay,
       "sleOspfv3ProcControlSPFMaxDelay": sleOspfv3ProcControlSPFMaxDelay,
       "sleOspfv3ProcControlLSAStartDelay": sleOspfv3ProcControlLSAStartDelay,
       "sleOspfv3ProcControlLSAMinDelay": sleOspfv3ProcControlLSAMinDelay,
       "sleOspfv3ProcControlLSAMaxDelay": sleOspfv3ProcControlLSAMaxDelay,
       "sleOspfv3ProcControlLSAArrivalDelay": sleOspfv3ProcControlLSAArrivalDelay,
       "sleOspfv3ProcInfoNotification": sleOspfv3ProcInfoNotification,
       "sleOspfv3ProcCreated": sleOspfv3ProcCreated,
       "sleOspfv3ProcProfileChanged": sleOspfv3ProcProfileChanged,
       "sleOspfv3ProcDestroyed": sleOspfv3ProcDestroyed,
       "sleOspfv3ProcCleared": sleOspfv3ProcCleared,
       "sleOspfv3ProcSummary": sleOspfv3ProcSummary,
       "sleOspfv3ProcSummaryTable": sleOspfv3ProcSummaryTable,
       "sleOspfv3ProcSummaryEntry": sleOspfv3ProcSummaryEntry,
       "sleOspfv3ProcSummaryAddress": sleOspfv3ProcSummaryAddress,
       "sleOspfv3ProcSummaryMask": sleOspfv3ProcSummaryMask,
       "sleOspfv3ProcSummaryTag": sleOspfv3ProcSummaryTag,
       "sleOspfv3ProcSummaryAdvertiseFlag": sleOspfv3ProcSummaryAdvertiseFlag,
       "sleOspfv3rocSummaryControl": sleOspfv3rocSummaryControl,
       "sleOspfv3ProcSummaryControlRequest": sleOspfv3ProcSummaryControlRequest,
       "sleOspfv3ProcSummaryControlStatus": sleOspfv3ProcSummaryControlStatus,
       "sleOspfv3ProcSummaryControlTimer": sleOspfv3ProcSummaryControlTimer,
       "sleOspfv3ProcSummaryControlTimeStamp": sleOspfv3ProcSummaryControlTimeStamp,
       "sleOspfv3ProcSummaryControlReqResult": sleOspfv3ProcSummaryControlReqResult,
       "sleOspfv3ProcSummaryControlIndex": sleOspfv3ProcSummaryControlIndex,
       "sleOspfv3ProcSummaryControlAddress": sleOspfv3ProcSummaryControlAddress,
       "sleOspfv3ProcSummaryControlMask": sleOspfv3ProcSummaryControlMask,
       "sleOspfv3ProcSummaryControlTag": sleOspfv3ProcSummaryControlTag,
       "sleOspfv3ProcSummaryControlAdvertiseFlag": sleOspfv3ProcSummaryControlAdvertiseFlag,
       "sleOspfv3ProcSummaryNotification": sleOspfv3ProcSummaryNotification,
       "sleOspfv3ProcSummaryCreated": sleOspfv3ProcSummaryCreated,
       "sleOspfv3ProcSummaryChanged": sleOspfv3ProcSummaryChanged,
       "sleOspfv3ProcSummaryDestroyed": sleOspfv3ProcSummaryDestroyed,
       "sleOspfv3ProcPassiveIf": sleOspfv3ProcPassiveIf,
       "sleOspfv3ProcPassiveIfTable": sleOspfv3ProcPassiveIfTable,
       "sleOspfv3ProcPassiveIfEntry": sleOspfv3ProcPassiveIfEntry,
       "sleOspfv3ProcPassiveIfIndex": sleOspfv3ProcPassiveIfIndex,
       "sleOspfv3ProcPassIfControl": sleOspfv3ProcPassIfControl,
       "sleOspfv3ProcPassiveIfControlRequest": sleOspfv3ProcPassiveIfControlRequest,
       "sleOspfv3ProcPassiveIfControlStatus": sleOspfv3ProcPassiveIfControlStatus,
       "sleOspfv3ProcPassiveIfControlTimer": sleOspfv3ProcPassiveIfControlTimer,
       "sleOspfv3ProcPassiveIfControlTimeStamp": sleOspfv3ProcPassiveIfControlTimeStamp,
       "sleOspfv3ProcPassiveIfControlReqResult": sleOspfv3ProcPassiveIfControlReqResult,
       "sleOspfv3ProcPassiveIfControlIndex": sleOspfv3ProcPassiveIfControlIndex,
       "sleOspfv3ProcPassiveIfControlIfIndex": sleOspfv3ProcPassiveIfControlIfIndex,
       "sleOspfv3ProcPassIfNotification": sleOspfv3ProcPassIfNotification,
       "sleOspfv3ProcPassiveIfAdded": sleOspfv3ProcPassiveIfAdded,
       "sleOspfv3ProcPassiveIfDeleted": sleOspfv3ProcPassiveIfDeleted,
       "sleOspfv3ProcRedist": sleOspfv3ProcRedist,
       "sleOspfv3ProcRedistTable": sleOspfv3ProcRedistTable,
       "sleOspfv3ProcRedistEntry": sleOspfv3ProcRedistEntry,
       "sleOspfv3ProcRedistType": sleOspfv3ProcRedistType,
       "sleOspfv3ProcRedistMetricType": sleOspfv3ProcRedistMetricType,
       "sleOspfv3ProcRedistMetric": sleOspfv3ProcRedistMetric,
       "sleOSpfv3ProcRedistRouteMapName": sleOSpfv3ProcRedistRouteMapName,
       "sleOspfv3ProcRedistControl": sleOspfv3ProcRedistControl,
       "sleOspfv3ProcRedistControlRequest": sleOspfv3ProcRedistControlRequest,
       "sleOspfv3ProcRedistControlStatus": sleOspfv3ProcRedistControlStatus,
       "sleOspfv3ProcRedistControlTimer": sleOspfv3ProcRedistControlTimer,
       "sleOspfv3ProcRedistControlTimeStamp": sleOspfv3ProcRedistControlTimeStamp,
       "sleOspfv3ProcRedistControlReqResult": sleOspfv3ProcRedistControlReqResult,
       "sleOspfv3ProcRedistControlIndex": sleOspfv3ProcRedistControlIndex,
       "sleOspfv3ProcRedistControlType": sleOspfv3ProcRedistControlType,
       "sleOspfv3ProcRedistControlMetricType": sleOspfv3ProcRedistControlMetricType,
       "sleOspfv3ProcRedistControlMetric": sleOspfv3ProcRedistControlMetric,
       "sleOSpfv3ProcRedistControlRouteMapName": sleOSpfv3ProcRedistControlRouteMapName,
       "sleOspfv3ProcRedistNotification": sleOspfv3ProcRedistNotification,
       "sleOspfv3ProcRedistCreated": sleOspfv3ProcRedistCreated,
       "sleOspfv3ProcRedistChanged": sleOspfv3ProcRedistChanged,
       "sleOspfv3ProcRedistDestroyed": sleOspfv3ProcRedistDestroyed,
       "sleOspfv3ProcArea": sleOspfv3ProcArea,
       "sleOspfv3ProcAreaInfo": sleOspfv3ProcAreaInfo,
       "sleOspfv3ProcAreaInfoTable": sleOspfv3ProcAreaInfoTable,
       "sleOspfv3ProcAreaInfoEntry": sleOspfv3ProcAreaInfoEntry,
       "sleOspfv3ProcAreaInfoIndex": sleOspfv3ProcAreaInfoIndex,
       "sleOspfv3ProcAreaInfoType": sleOspfv3ProcAreaInfoType,
       "sleOspfv3ProcAreaInfoDefaultCost": sleOspfv3ProcAreaInfoDefaultCost,
       "sleOspfv3ProcAreaInfoSummary": sleOspfv3ProcAreaInfoSummary,
       "sleOspfv3ProcAreaInfoControl": sleOspfv3ProcAreaInfoControl,
       "sleOspfv3ProcAreaInfoControlRequest": sleOspfv3ProcAreaInfoControlRequest,
       "sleOspfv3ProcAreaInfoControlStatus": sleOspfv3ProcAreaInfoControlStatus,
       "sleOspfv3ProcAreaInfoControlTimer": sleOspfv3ProcAreaInfoControlTimer,
       "sleOspfv3ProcAreaInfoControlTimeStamp": sleOspfv3ProcAreaInfoControlTimeStamp,
       "sleOspfv3ProcAreaInfoControlReqResult": sleOspfv3ProcAreaInfoControlReqResult,
       "sleOspfv3ProcAreaInfoControlIndex": sleOspfv3ProcAreaInfoControlIndex,
       "sleOspfv3ProcAreaInfoControlAreaIndex": sleOspfv3ProcAreaInfoControlAreaIndex,
       "sleOspfv3ProcAreaInfoControlType": sleOspfv3ProcAreaInfoControlType,
       "sleOspfv3ProcAreaInfoControlDefaultCost": sleOspfv3ProcAreaInfoControlDefaultCost,
       "sleOspfv3ProcAreaInfoControlSummary": sleOspfv3ProcAreaInfoControlSummary,
       "sleOspfv3ProcAreaInfoNotification": sleOspfv3ProcAreaInfoNotification,
       "sleOspfv3ProcAreaInfoCreated": sleOspfv3ProcAreaInfoCreated,
       "sleOspfv3ProcAreaInfoChanged": sleOspfv3ProcAreaInfoChanged,
       "sleOspfv3ProcAreaInfoDestroyed": sleOspfv3ProcAreaInfoDestroyed,
       "sleOspfv3ProcAreaRange": sleOspfv3ProcAreaRange,
       "sleOspfv3ProcAreaRangeTable": sleOspfv3ProcAreaRangeTable,
       "sleOspfv3ProcAreaRangeEntry": sleOspfv3ProcAreaRangeEntry,
       "sleOspfv3ProcAreaRangeAddress": sleOspfv3ProcAreaRangeAddress,
       "sleOspfv3ProcAreaRangeMask": sleOspfv3ProcAreaRangeMask,
       "sleOspfv3ProcAreaRangeAdvertiseFlag": sleOspfv3ProcAreaRangeAdvertiseFlag,
       "sleOspfv3ProcAreaRangeControl": sleOspfv3ProcAreaRangeControl,
       "sleOspfv3ProcAreaRangeControlRequest": sleOspfv3ProcAreaRangeControlRequest,
       "sleOspfv3ProcAreaRangeControlStatus": sleOspfv3ProcAreaRangeControlStatus,
       "sleOspfv3ProcAreaRangeControlTimer": sleOspfv3ProcAreaRangeControlTimer,
       "sleOspfv3ProcAreaRangeControlTimeStamp": sleOspfv3ProcAreaRangeControlTimeStamp,
       "sleOspfv3ProcAreaRangeControlReqResult": sleOspfv3ProcAreaRangeControlReqResult,
       "sleOspfv3ProcAreaRangeControlIndex": sleOspfv3ProcAreaRangeControlIndex,
       "sleOspfv3ProcAreaRangeControlAreaIndex": sleOspfv3ProcAreaRangeControlAreaIndex,
       "sleOspfv3ProcAreaRangeControlAddr": sleOspfv3ProcAreaRangeControlAddr,
       "sleOspfv3ProcAreaRangeControlMask": sleOspfv3ProcAreaRangeControlMask,
       "sleOspfv3ProcAreaRangeControlAdvertiseFlag": sleOspfv3ProcAreaRangeControlAdvertiseFlag,
       "sleOspfv3ProcAreaRangeNotification": sleOspfv3ProcAreaRangeNotification,
       "sleOspfv3ProcAreaRangeCreated": sleOspfv3ProcAreaRangeCreated,
       "sleOspfv3ProcAreaRangeChanged": sleOspfv3ProcAreaRangeChanged,
       "sleOspfv3ProcAreaRangeDestroyed": sleOspfv3ProcAreaRangeDestroyed,
       "sleOspfv3ProcAreaVlink": sleOspfv3ProcAreaVlink,
       "sleOspfv3ProcAreaVlinkTable": sleOspfv3ProcAreaVlinkTable,
       "sleOspfv3ProcAreaVlinkEntry": sleOspfv3ProcAreaVlinkEntry,
       "sleOspfv3ProcAreaVlinkRouterId": sleOspfv3ProcAreaVlinkRouterId,
       "sleOspfv3ProcAreaVlinkDeadInterval": sleOspfv3ProcAreaVlinkDeadInterval,
       "sleOspfv3ProcAreaVlinkHelloInterval": sleOspfv3ProcAreaVlinkHelloInterval,
       "sleOspfv3ProcAreaVlinkInstanceId": sleOspfv3ProcAreaVlinkInstanceId,
       "sleOspfv3ProcAreaVlinkRetransInterval": sleOspfv3ProcAreaVlinkRetransInterval,
       "sleOspfv3ProcAreaVlinkTransDelay": sleOspfv3ProcAreaVlinkTransDelay,
       "sleOspfv3ProcAreaVlinkControl": sleOspfv3ProcAreaVlinkControl,
       "sleOspfv3ProcAreaVlinkControlRequest": sleOspfv3ProcAreaVlinkControlRequest,
       "sleOspfv3ProcAreaVlinkControlStatus": sleOspfv3ProcAreaVlinkControlStatus,
       "sleOspfv3ProcAreaVlinkControlTimer": sleOspfv3ProcAreaVlinkControlTimer,
       "sleOspfv3ProcAreaVlinkControlTimeStamp": sleOspfv3ProcAreaVlinkControlTimeStamp,
       "sleOspfv3ProcAreaVlinkControlReqResult": sleOspfv3ProcAreaVlinkControlReqResult,
       "sleOspfv3ProcAreaVlinkControlIndex": sleOspfv3ProcAreaVlinkControlIndex,
       "sleOspfv3ProcAreaVlinkControlAreaIndex": sleOspfv3ProcAreaVlinkControlAreaIndex,
       "sleOspfv3ProcAreaVlinkControlRouterId": sleOspfv3ProcAreaVlinkControlRouterId,
       "sleOspfv3ProcAreaVlinkControlDeadInterval": sleOspfv3ProcAreaVlinkControlDeadInterval,
       "sleOspfv3ProcAreaVlinkControlHelloInterval": sleOspfv3ProcAreaVlinkControlHelloInterval,
       "sleOspfv3ProcAreaVlinkControlInstanceId": sleOspfv3ProcAreaVlinkControlInstanceId,
       "sleOspfv3ProcAreaVlinkControlRetransInterval": sleOspfv3ProcAreaVlinkControlRetransInterval,
       "sleOspfv3ProcAreaVlinkControlTransDelay": sleOspfv3ProcAreaVlinkControlTransDelay,
       "sleOspfv3ProcAreaVlinkNotification": sleOspfv3ProcAreaVlinkNotification,
       "sleOspfv3ProcAreaVlinkCreated": sleOspfv3ProcAreaVlinkCreated,
       "sleOspfv3ProcAreaVlinkChanged": sleOspfv3ProcAreaVlinkChanged,
       "sleOspfv3ProcAreaVlinkDestroyed": sleOspfv3ProcAreaVlinkDestroyed,
       "sleOspfv3Interface": sleOspfv3Interface,
       "sleOspfv3IfInstance": sleOspfv3IfInstance,
       "sleOspfv3IfInstanceTable": sleOspfv3IfInstanceTable,
       "sleOspfv3IfInstanceEntry": sleOspfv3IfInstanceEntry,
       "sleOspfv3IfInstanceIfIndex": sleOspfv3IfInstanceIfIndex,
       "sleOspfv3IfInstanceInstanceId": sleOspfv3IfInstanceInstanceId,
       "sleOspfv3IfInstanceProcTag": sleOspfv3IfInstanceProcTag,
       "sleOspfv3IfInstanceAreaFlag": sleOspfv3IfInstanceAreaFlag,
       "sleOspfv3IfInstanceAreaIndex": sleOspfv3IfInstanceAreaIndex,
       "sleOspfv3IfInstanceDeadInterval": sleOspfv3IfInstanceDeadInterval,
       "sleOspfv3IfInstanceHelloInterval": sleOspfv3IfInstanceHelloInterval,
       "sleOspfv3IfInstanceNetworkType": sleOspfv3IfInstanceNetworkType,
       "sleOspfv3IfInstanceCost": sleOspfv3IfInstanceCost,
       "sleOspfv3IfInstanceTransDelay": sleOspfv3IfInstanceTransDelay,
       "sleOspfv3IfInstanceRetransInterval": sleOspfv3IfInstanceRetransInterval,
       "sleOspfv3IfInstancePriority": sleOspfv3IfInstancePriority,
       "sleOspfv3IfInstanceBfd": sleOspfv3IfInstanceBfd,
       "sleOspfv3IfInstanceEfm": sleOspfv3IfInstanceEfm,
       "sleOspfv3ProcIfInstanceControl": sleOspfv3ProcIfInstanceControl,
       "sleOspfv3IfInstanceControlRequest": sleOspfv3IfInstanceControlRequest,
       "sleOspfv3IfInstanceControlStatus": sleOspfv3IfInstanceControlStatus,
       "sleOspfv3IfInstanceControlTimer": sleOspfv3IfInstanceControlTimer,
       "sleOspfv3IfInstanceControlTimeStamp": sleOspfv3IfInstanceControlTimeStamp,
       "sleOspfv3IfInstanceControlReqResult": sleOspfv3IfInstanceControlReqResult,
       "sleOspfv3IfInstanceControlIfIndex": sleOspfv3IfInstanceControlIfIndex,
       "sleOspfv3IfInstanceControlIfInstanceId": sleOspfv3IfInstanceControlIfInstanceId,
       "sleOspfv3IfInstanceControlProcTag": sleOspfv3IfInstanceControlProcTag,
       "sleOspfv3IfInstanceControlAreaFlag": sleOspfv3IfInstanceControlAreaFlag,
       "sleOspfv3IfInstanceControlAreaIndex": sleOspfv3IfInstanceControlAreaIndex,
       "sleOspfv3IfInstanceControlDeadInterval": sleOspfv3IfInstanceControlDeadInterval,
       "sleOspfv3IfInstanceControlHelloInterval": sleOspfv3IfInstanceControlHelloInterval,
       "sleOspfv3IfInstanceControlNetworkType": sleOspfv3IfInstanceControlNetworkType,
       "sleOspfv3IfInstanceControlCost": sleOspfv3IfInstanceControlCost,
       "sleOspfv3IfInstanceControlTransDelay": sleOspfv3IfInstanceControlTransDelay,
       "sleOspfv3IfInstanceControlRetransInterval": sleOspfv3IfInstanceControlRetransInterval,
       "sleOspfv3IfInstanceControlPriority": sleOspfv3IfInstanceControlPriority,
       "sleOspfv3IfInstanceControlBfd": sleOspfv3IfInstanceControlBfd,
       "sleOspfv3IfInstanceControlEfm": sleOspfv3IfInstanceControlEfm,
       "sleOspfv3IfInstanceNotifications": sleOspfv3IfInstanceNotifications,
       "sleOspfv3IfInstanceChanged": sleOspfv3IfInstanceChanged,
       "sleOspfv3IfNeighbor": sleOspfv3IfNeighbor,
       "sleOspfv3IfNeighborTable": sleOspfv3IfNeighborTable,
       "sleOspfv3IfNeighborEntry": sleOspfv3IfNeighborEntry,
       "sleOspfv3IfNeighborAddress": sleOspfv3IfNeighborAddress,
       "sleOspfv3IfNeighborCost": sleOspfv3IfNeighborCost,
       "sleOspfv3IfNeighborPollIntervalFlag": sleOspfv3IfNeighborPollIntervalFlag,
       "sleOspfv3IfNeighborPollIntervalValue": sleOspfv3IfNeighborPollIntervalValue,
       "sleOspfv3IfNeighborPriority": sleOspfv3IfNeighborPriority,
       "sleOspfv3ProcIfNeighborControl": sleOspfv3ProcIfNeighborControl,
       "sleOspfv3IfNeighborControlRequest": sleOspfv3IfNeighborControlRequest,
       "sleOspfv3IfNeighborControlStatus": sleOspfv3IfNeighborControlStatus,
       "sleOspfv3IfNeighborControlTimer": sleOspfv3IfNeighborControlTimer,
       "sleOspfv3IfNeighborControlTimeStamp": sleOspfv3IfNeighborControlTimeStamp,
       "sleOspfv3IfNeighborControlReqResult": sleOspfv3IfNeighborControlReqResult,
       "sleOspfv3IfNeighborControlIndex": sleOspfv3IfNeighborControlIndex,
       "sleOspfv3IfNeighborControlInstanceIndex": sleOspfv3IfNeighborControlInstanceIndex,
       "sleOspfv3IfNeighborControlAddress": sleOspfv3IfNeighborControlAddress,
       "sleOspfv3IfNeighborControlCost": sleOspfv3IfNeighborControlCost,
       "sleOspfv3IfNeighborControlPollIntervalFlag": sleOspfv3IfNeighborControlPollIntervalFlag,
       "sleOspfv3IfNeighborControlPollInterval": sleOspfv3IfNeighborControlPollInterval,
       "sleOspfv3IfNeighborControlPriority": sleOspfv3IfNeighborControlPriority,
       "sleOspfv3IfNeighborNotifications": sleOspfv3IfNeighborNotifications,
       "sleOspfv3IfNeighborCreated": sleOspfv3IfNeighborCreated,
       "sleOspfv3IfNeighborModified": sleOspfv3IfNeighborModified,
       "sleOspfv3IfNeighborDestroyed": sleOspfv3IfNeighborDestroyed,
       "sleOspfv3IfStatus": sleOspfv3IfStatus,
       "sleOspfv3IfStatusTable": sleOspfv3IfStatusTable,
       "sleOspfv3IfStatusEntry": sleOspfv3IfStatusEntry,
       "sleOspfv3IfStatusProcTag": sleOspfv3IfStatusProcTag,
       "sleOspfv3IfStatusAreaId": sleOspfv3IfStatusAreaId,
       "sleOspfv3IfStatusNetworkType": sleOspfv3IfStatusNetworkType,
       "sleOspfv3IfStatusCost": sleOspfv3IfStatusCost,
       "sleOspfv3IfStatusTransDelay": sleOspfv3IfStatusTransDelay,
       "sleOspfv3IfStatusState": sleOspfv3IfStatusState,
       "sleOspfv3IfStatusPriority": sleOspfv3IfStatusPriority,
       "sleOspfv3IfStatusDRRouterId": sleOspfv3IfStatusDRRouterId,
       "sleOspfv3IfStatusDRAddress": sleOspfv3IfStatusDRAddress,
       "sleOspfv3IfStatusBackupRouterId": sleOspfv3IfStatusBackupRouterId,
       "sleOspfv3IfStatusBackupAddress": sleOspfv3IfStatusBackupAddress,
       "sleOspfv3IfStatusHelloInterval": sleOspfv3IfStatusHelloInterval,
       "sleOspfv3IfStatusDeadInterval": sleOspfv3IfStatusDeadInterval,
       "sleOspfv3IfStatusWaitInterval": sleOspfv3IfStatusWaitInterval,
       "sleOspfv3IfStatusRetransInterval": sleOspfv3IfStatusRetransInterval,
       "sleOspfv3IfNeighborCount": sleOspfv3IfNeighborCount,
       "sleOspfv3IfAdjNeighborCount": sleOspfv3IfAdjNeighborCount,
       "sleOspfv3Lsdb": sleOspfv3Lsdb,
       "sleOspfv3LsdbTable": sleOspfv3LsdbTable,
       "sleOspfv3LsdbEntry": sleOspfv3LsdbEntry,
       "sleOspfv3LsdbType": sleOspfv3LsdbType,
       "sleOspfv3LsdbLinkStateId": sleOspfv3LsdbLinkStateId,
       "sleOspfv3LsdbAdvRouterId": sleOspfv3LsdbAdvRouterId,
       "sleOspfv3LsdbAge": sleOspfv3LsdbAge,
       "sleOspfv3LsdbSeqnum": sleOspfv3LsdbSeqnum,
       "sleOspfv3LsdbLength": sleOspfv3LsdbLength,
       "sleOspfv3Neighbor": sleOspfv3Neighbor,
       "sleOspfv3NeigborTable": sleOspfv3NeigborTable,
       "sleOspfv3NeigborEntry": sleOspfv3NeigborEntry,
       "sleOspfv3NeighborIfType": sleOspfv3NeighborIfType,
       "sleOspfv3NeighborIfIndex": sleOspfv3NeighborIfIndex,
       "sleOspfv3NeighborRouterId": sleOspfv3NeighborRouterId,
       "sleOspfv3NeighborAddress": sleOspfv3NeighborAddress,
       "sleOspfv3NeighborAreaId": sleOspfv3NeighborAreaId,
       "sleOspfv3NeighborIfName": sleOspfv3NeighborIfName,
       "sleOspfv3NeighborPriority": sleOspfv3NeighborPriority,
       "sleOspfv3NeighborState": sleOspfv3NeighborState,
       "sleOspfv3NeighborInstanceId": sleOspfv3NeighborInstanceId,
       "sleOspfv3NeighborDRRouterId": sleOspfv3NeighborDRRouterId,
       "sleOspfv3NeighborBDRRouterId": sleOspfv3NeighborBDRRouterId,
       "sleOspfv3NeighborOption": sleOspfv3NeighborOption,
       "sleOspfv3NeighborDeadTime": sleOspfv3NeighborDeadTime,
       "sleOspfv3NeighborLsdbCount": sleOspfv3NeighborLsdbCount,
       "sleOspfv3NeighborLsreqCount": sleOspfv3NeighborLsreqCount,
       "sleOspfv3NeighborLsrxmitCount": sleOspfv3NeighborLsrxmitCount,
       "sleOspfv3Route": sleOspfv3Route,
       "sleOspfv3RouteTable": sleOspfv3RouteTable,
       "sleOspfv3RouteEntry": sleOspfv3RouteEntry,
       "sleOspfv3RouteNetAddr": sleOspfv3RouteNetAddr,
       "sleOspfv3RouteNetMask": sleOspfv3RouteNetMask,
       "sleOspfv3RouteNexthop": sleOspfv3RouteNexthop,
       "sleOspfv3RouteType": sleOspfv3RouteType,
       "sleOspfv3RouteMetric": sleOspfv3RouteMetric,
       "sleOspfv3RouteIfName": sleOspfv3RouteIfName,
       "sleOspfv3RouteAreaFlag": sleOspfv3RouteAreaFlag,
       "sleOspfv3RouteAreaId": sleOspfv3RouteAreaId,
       "sleOspfv3Group": sleOspfv3Group,
       "sleOspfv3NotificationGroup": sleOspfv3NotificationGroup}
)
