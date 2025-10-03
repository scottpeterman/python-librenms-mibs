# SNMP MIB module (SLE-RIPng-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-RIPng-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:00 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

sleRIPng = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55)
)
if mibBuilder.loadTexts:
    sleRIPng.setRevisions(
        ("2010-03-21 19:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleRIPngBase_ObjectIdentity = ObjectIdentity
sleRIPngBase = _SleRIPngBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1)
)
_SleRIPngBaseInfo_ObjectIdentity = ObjectIdentity
sleRIPngBaseInfo = _SleRIPngBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1)
)


class _SleRIPngDefaultMetric_Type(Integer32):
    """Custom type sleRIPngDefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleRIPngDefaultMetric_Type.__name__ = "Integer32"
_SleRIPngDefaultMetric_Object = MibScalar
sleRIPngDefaultMetric = _SleRIPngDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 1),
    _SleRIPngDefaultMetric_Type()
)
sleRIPngDefaultMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDefaultMetric.setStatus("current")


class _SleRIPngDefaultInformationOrg_Type(Integer32):
    """Custom type sleRIPngDefaultInformationOrg based on Integer32"""
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


_SleRIPngDefaultInformationOrg_Type.__name__ = "Integer32"
_SleRIPngDefaultInformationOrg_Object = MibScalar
sleRIPngDefaultInformationOrg = _SleRIPngDefaultInformationOrg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 2),
    _SleRIPngDefaultInformationOrg_Type()
)
sleRIPngDefaultInformationOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDefaultInformationOrg.setStatus("current")


class _SleRIPngDefaultDistance_Type(Integer32):
    """Custom type sleRIPngDefaultDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPngDefaultDistance_Type.__name__ = "Integer32"
_SleRIPngDefaultDistance_Object = MibScalar
sleRIPngDefaultDistance = _SleRIPngDefaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 3),
    _SleRIPngDefaultDistance_Type()
)
sleRIPngDefaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDefaultDistance.setStatus("current")


class _SleRIPngRecvBufferSize_Type(Integer32):
    """Custom type sleRIPngRecvBufferSize based on Integer32"""
    defaultValue = 215040

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 2147483647),
    )


_SleRIPngRecvBufferSize_Type.__name__ = "Integer32"
_SleRIPngRecvBufferSize_Object = MibScalar
sleRIPngRecvBufferSize = _SleRIPngRecvBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 4),
    _SleRIPngRecvBufferSize_Type()
)
sleRIPngRecvBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRecvBufferSize.setStatus("current")


class _SleRIPngMaximumPaths_Type(Integer32):
    """Custom type sleRIPngMaximumPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleRIPngMaximumPaths_Type.__name__ = "Integer32"
_SleRIPngMaximumPaths_Object = MibScalar
sleRIPngMaximumPaths = _SleRIPngMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 5),
    _SleRIPngMaximumPaths_Type()
)
sleRIPngMaximumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngMaximumPaths.setStatus("current")


class _SleRIPngMaximumPrefixRoute_Type(Integer32):
    """Custom type sleRIPngMaximumPrefixRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRIPngMaximumPrefixRoute_Type.__name__ = "Integer32"
_SleRIPngMaximumPrefixRoute_Object = MibScalar
sleRIPngMaximumPrefixRoute = _SleRIPngMaximumPrefixRoute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 6),
    _SleRIPngMaximumPrefixRoute_Type()
)
sleRIPngMaximumPrefixRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngMaximumPrefixRoute.setStatus("current")


class _SleRIPngMaximumPrefixRoutePercent_Type(Integer32):
    """Custom type sleRIPngMaximumPrefixRoutePercent based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleRIPngMaximumPrefixRoutePercent_Type.__name__ = "Integer32"
_SleRIPngMaximumPrefixRoutePercent_Object = MibScalar
sleRIPngMaximumPrefixRoutePercent = _SleRIPngMaximumPrefixRoutePercent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 7),
    _SleRIPngMaximumPrefixRoutePercent_Type()
)
sleRIPngMaximumPrefixRoutePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngMaximumPrefixRoutePercent.setStatus("current")


class _SleRIPngMetricSumApply_Type(Integer32):
    """Custom type sleRIPngMetricSumApply based on Integer32"""
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


_SleRIPngMetricSumApply_Type.__name__ = "Integer32"
_SleRIPngMetricSumApply_Object = MibScalar
sleRIPngMetricSumApply = _SleRIPngMetricSumApply_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 8),
    _SleRIPngMetricSumApply_Type()
)
sleRIPngMetricSumApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngMetricSumApply.setStatus("current")


class _SleRIPngBasicUpdateTimer_Type(Integer32):
    """Custom type sleRIPngBasicUpdateTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPngBasicUpdateTimer_Type.__name__ = "Integer32"
_SleRIPngBasicUpdateTimer_Object = MibScalar
sleRIPngBasicUpdateTimer = _SleRIPngBasicUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 9),
    _SleRIPngBasicUpdateTimer_Type()
)
sleRIPngBasicUpdateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngBasicUpdateTimer.setStatus("current")


class _SleRIPngBasicTimeoutTimer_Type(Integer32):
    """Custom type sleRIPngBasicTimeoutTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPngBasicTimeoutTimer_Type.__name__ = "Integer32"
_SleRIPngBasicTimeoutTimer_Object = MibScalar
sleRIPngBasicTimeoutTimer = _SleRIPngBasicTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 10),
    _SleRIPngBasicTimeoutTimer_Type()
)
sleRIPngBasicTimeoutTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngBasicTimeoutTimer.setStatus("current")


class _SleRIPngBasicGarbageTimer_Type(Integer32):
    """Custom type sleRIPngBasicGarbageTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPngBasicGarbageTimer_Type.__name__ = "Integer32"
_SleRIPngBasicGarbageTimer_Object = MibScalar
sleRIPngBasicGarbageTimer = _SleRIPngBasicGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 1, 11),
    _SleRIPngBasicGarbageTimer_Type()
)
sleRIPngBasicGarbageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngBasicGarbageTimer.setStatus("current")
_SleRIPngBaseControl_ObjectIdentity = ObjectIdentity
sleRIPngBaseControl = _SleRIPngBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2)
)


class _SleRIPngControlRequest_Type(Integer32):
    """Custom type sleRIPngControlRequest based on Integer32"""
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
        *(("createRIPngMode", 1),
          ("deleteRIPngMode", 2),
          ("setRIPngDefaultMetric", 3),
          ("setRIPngDefaultInformationOrg", 4),
          ("setRIPngDefaultDistance", 5),
          ("setRIPngRecvBufferSize", 6),
          ("setRIPngMaximumPaths", 7),
          ("setRIPngMaximumPrefixRouteProfile", 8),
          ("setRIPngMetricSumApply", 9),
          ("setRIPngBasicTimersProfile", 10),
          ("clearRIPngAll", 11),
          ("clearRIPngRoute", 12),
          ("clearRIPngProtoType", 13))
    )


_SleRIPngControlRequest_Type.__name__ = "Integer32"
_SleRIPngControlRequest_Object = MibScalar
sleRIPngControlRequest = _SleRIPngControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 1),
    _SleRIPngControlRequest_Type()
)
sleRIPngControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngControlRequest.setStatus("current")
_SleRIPngControlStatus_Type = SleControlStatusType
_SleRIPngControlStatus_Object = MibScalar
sleRIPngControlStatus = _SleRIPngControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 2),
    _SleRIPngControlStatus_Type()
)
sleRIPngControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlStatus.setStatus("current")
_SleRIPngControlTimer_Type = Gauge32
_SleRIPngControlTimer_Object = MibScalar
sleRIPngControlTimer = _SleRIPngControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 3),
    _SleRIPngControlTimer_Type()
)
sleRIPngControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngControlTimer.setStatus("current")
_SleRIPngControlTimeStamp_Type = TimeTicks
_SleRIPngControlTimeStamp_Object = MibScalar
sleRIPngControlTimeStamp = _SleRIPngControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 4),
    _SleRIPngControlTimeStamp_Type()
)
sleRIPngControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlTimeStamp.setStatus("current")
_SleRIPngControlReqResult_Type = SleControlRequestResultType
_SleRIPngControlReqResult_Object = MibScalar
sleRIPngControlReqResult = _SleRIPngControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 5),
    _SleRIPngControlReqResult_Type()
)
sleRIPngControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlReqResult.setStatus("current")


class _SleRIPngControlDefaultMetric_Type(Integer32):
    """Custom type sleRIPngControlDefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleRIPngControlDefaultMetric_Type.__name__ = "Integer32"
_SleRIPngControlDefaultMetric_Object = MibScalar
sleRIPngControlDefaultMetric = _SleRIPngControlDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 6),
    _SleRIPngControlDefaultMetric_Type()
)
sleRIPngControlDefaultMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlDefaultMetric.setStatus("current")


class _SleRIPngControlDefaultInformationOrg_Type(Integer32):
    """Custom type sleRIPngControlDefaultInformationOrg based on Integer32"""
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


_SleRIPngControlDefaultInformationOrg_Type.__name__ = "Integer32"
_SleRIPngControlDefaultInformationOrg_Object = MibScalar
sleRIPngControlDefaultInformationOrg = _SleRIPngControlDefaultInformationOrg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 7),
    _SleRIPngControlDefaultInformationOrg_Type()
)
sleRIPngControlDefaultInformationOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlDefaultInformationOrg.setStatus("current")


class _SleRIPngControlDefaultDistance_Type(Integer32):
    """Custom type sleRIPngControlDefaultDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPngControlDefaultDistance_Type.__name__ = "Integer32"
_SleRIPngControlDefaultDistance_Object = MibScalar
sleRIPngControlDefaultDistance = _SleRIPngControlDefaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 8),
    _SleRIPngControlDefaultDistance_Type()
)
sleRIPngControlDefaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlDefaultDistance.setStatus("current")


class _SleRIPngControlRecvBufferSize_Type(Integer32):
    """Custom type sleRIPngControlRecvBufferSize based on Integer32"""
    defaultValue = 215040

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 2147483647),
    )


_SleRIPngControlRecvBufferSize_Type.__name__ = "Integer32"
_SleRIPngControlRecvBufferSize_Object = MibScalar
sleRIPngControlRecvBufferSize = _SleRIPngControlRecvBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 9),
    _SleRIPngControlRecvBufferSize_Type()
)
sleRIPngControlRecvBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlRecvBufferSize.setStatus("current")


class _SleRIPngControlMaximumPaths_Type(Integer32):
    """Custom type sleRIPngControlMaximumPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleRIPngControlMaximumPaths_Type.__name__ = "Integer32"
_SleRIPngControlMaximumPaths_Object = MibScalar
sleRIPngControlMaximumPaths = _SleRIPngControlMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 10),
    _SleRIPngControlMaximumPaths_Type()
)
sleRIPngControlMaximumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlMaximumPaths.setStatus("current")


class _SleRIPngControlMaximumPrefixRoute_Type(Integer32):
    """Custom type sleRIPngControlMaximumPrefixRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRIPngControlMaximumPrefixRoute_Type.__name__ = "Integer32"
_SleRIPngControlMaximumPrefixRoute_Object = MibScalar
sleRIPngControlMaximumPrefixRoute = _SleRIPngControlMaximumPrefixRoute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 11),
    _SleRIPngControlMaximumPrefixRoute_Type()
)
sleRIPngControlMaximumPrefixRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlMaximumPrefixRoute.setStatus("current")


class _SleRIPngControlMaximumPrefixRoutePercent_Type(Integer32):
    """Custom type sleRIPngControlMaximumPrefixRoutePercent based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleRIPngControlMaximumPrefixRoutePercent_Type.__name__ = "Integer32"
_SleRIPngControlMaximumPrefixRoutePercent_Object = MibScalar
sleRIPngControlMaximumPrefixRoutePercent = _SleRIPngControlMaximumPrefixRoutePercent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 12),
    _SleRIPngControlMaximumPrefixRoutePercent_Type()
)
sleRIPngControlMaximumPrefixRoutePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlMaximumPrefixRoutePercent.setStatus("current")


class _SleRIPngControlMetricSumApply_Type(Integer32):
    """Custom type sleRIPngControlMetricSumApply based on Integer32"""
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


_SleRIPngControlMetricSumApply_Type.__name__ = "Integer32"
_SleRIPngControlMetricSumApply_Object = MibScalar
sleRIPngControlMetricSumApply = _SleRIPngControlMetricSumApply_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 13),
    _SleRIPngControlMetricSumApply_Type()
)
sleRIPngControlMetricSumApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlMetricSumApply.setStatus("current")


class _SleRIPngControlBasicUpdateTimer_Type(Integer32):
    """Custom type sleRIPngControlBasicUpdateTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPngControlBasicUpdateTimer_Type.__name__ = "Integer32"
_SleRIPngControlBasicUpdateTimer_Object = MibScalar
sleRIPngControlBasicUpdateTimer = _SleRIPngControlBasicUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 14),
    _SleRIPngControlBasicUpdateTimer_Type()
)
sleRIPngControlBasicUpdateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlBasicUpdateTimer.setStatus("current")


class _SleRIPngControlBasicTimeoutTimer_Type(Integer32):
    """Custom type sleRIPngControlBasicTimeoutTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPngControlBasicTimeoutTimer_Type.__name__ = "Integer32"
_SleRIPngControlBasicTimeoutTimer_Object = MibScalar
sleRIPngControlBasicTimeoutTimer = _SleRIPngControlBasicTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 15),
    _SleRIPngControlBasicTimeoutTimer_Type()
)
sleRIPngControlBasicTimeoutTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlBasicTimeoutTimer.setStatus("current")


class _SleRIPngControlBasicGarbageTimer_Type(Integer32):
    """Custom type sleRIPngControlBasicGarbageTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPngControlBasicGarbageTimer_Type.__name__ = "Integer32"
_SleRIPngControlBasicGarbageTimer_Object = MibScalar
sleRIPngControlBasicGarbageTimer = _SleRIPngControlBasicGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 16),
    _SleRIPngControlBasicGarbageTimer_Type()
)
sleRIPngControlBasicGarbageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlBasicGarbageTimer.setStatus("current")
_SleRIPngControlClearRoutePrefix_Type = InetAddress
_SleRIPngControlClearRoutePrefix_Object = MibScalar
sleRIPngControlClearRoutePrefix = _SleRIPngControlClearRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 17),
    _SleRIPngControlClearRoutePrefix_Type()
)
sleRIPngControlClearRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlClearRoutePrefix.setStatus("current")


class _SleRIPngControlClearRouteMask_Type(Integer32):
    """Custom type sleRIPngControlClearRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleRIPngControlClearRouteMask_Type.__name__ = "Integer32"
_SleRIPngControlClearRouteMask_Object = MibScalar
sleRIPngControlClearRouteMask = _SleRIPngControlClearRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 18),
    _SleRIPngControlClearRouteMask_Type()
)
sleRIPngControlClearRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlClearRouteMask.setStatus("current")


class _SleRIPngControlClearProtoTpye_Type(Integer32):
    """Custom type sleRIPngControlClearProtoTpye based on Integer32"""
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
          ("static", 3),
          ("bgp", 4),
          ("ospf", 5),
          ("rip", 6))
    )


_SleRIPngControlClearProtoTpye_Type.__name__ = "Integer32"
_SleRIPngControlClearProtoTpye_Object = MibScalar
sleRIPngControlClearProtoTpye = _SleRIPngControlClearProtoTpye_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 2, 19),
    _SleRIPngControlClearProtoTpye_Type()
)
sleRIPngControlClearProtoTpye.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngControlClearProtoTpye.setStatus("current")
_SleRIPngBaseNotification_ObjectIdentity = ObjectIdentity
sleRIPngBaseNotification = _SleRIPngBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3)
)
_SleRIPngAggregate_ObjectIdentity = ObjectIdentity
sleRIPngAggregate = _SleRIPngAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2)
)
_SleRIPngAggregateTable_Object = MibTable
sleRIPngAggregateTable = _SleRIPngAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 1)
)
if mibBuilder.loadTexts:
    sleRIPngAggregateTable.setStatus("current")
_SleRIPngAggregateEntry_Object = MibTableRow
sleRIPngAggregateEntry = _SleRIPngAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 1, 1)
)
sleRIPngAggregateEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngAggregateAddr"),
    (0, "SLE-RIPng-MIB", "sleRIPngAggregateMask"),
)
if mibBuilder.loadTexts:
    sleRIPngAggregateEntry.setStatus("current")
_SleRIPngAggregateAddr_Type = InetAddress
_SleRIPngAggregateAddr_Object = MibTableColumn
sleRIPngAggregateAddr = _SleRIPngAggregateAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 1, 1, 1),
    _SleRIPngAggregateAddr_Type()
)
sleRIPngAggregateAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAggregateAddr.setStatus("current")


class _SleRIPngAggregateMask_Type(Integer32):
    """Custom type sleRIPngAggregateMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleRIPngAggregateMask_Type.__name__ = "Integer32"
_SleRIPngAggregateMask_Object = MibTableColumn
sleRIPngAggregateMask = _SleRIPngAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 1, 1, 2),
    _SleRIPngAggregateMask_Type()
)
sleRIPngAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAggregateMask.setStatus("current")
_SleRIPngAggregateControl_ObjectIdentity = ObjectIdentity
sleRIPngAggregateControl = _SleRIPngAggregateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2)
)


class _SleRIPngAggregateControlRequest_Type(Integer32):
    """Custom type sleRIPngAggregateControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPngAggregateAddr", 1),
          ("deleteRIPngAggregateAddr", 2))
    )


_SleRIPngAggregateControlRequest_Type.__name__ = "Integer32"
_SleRIPngAggregateControlRequest_Object = MibScalar
sleRIPngAggregateControlRequest = _SleRIPngAggregateControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2, 1),
    _SleRIPngAggregateControlRequest_Type()
)
sleRIPngAggregateControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAggregateControlRequest.setStatus("current")
_SleRIPngAggregateControlStatus_Type = SleControlStatusType
_SleRIPngAggregateControlStatus_Object = MibScalar
sleRIPngAggregateControlStatus = _SleRIPngAggregateControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2, 2),
    _SleRIPngAggregateControlStatus_Type()
)
sleRIPngAggregateControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAggregateControlStatus.setStatus("current")
_SleRIPngAggregateControlTimer_Type = Gauge32
_SleRIPngAggregateControlTimer_Object = MibScalar
sleRIPngAggregateControlTimer = _SleRIPngAggregateControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2, 3),
    _SleRIPngAggregateControlTimer_Type()
)
sleRIPngAggregateControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAggregateControlTimer.setStatus("current")
_SleRIPngAggregateControlTimeStamp_Type = TimeTicks
_SleRIPngAggregateControlTimeStamp_Object = MibScalar
sleRIPngAggregateControlTimeStamp = _SleRIPngAggregateControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2, 4),
    _SleRIPngAggregateControlTimeStamp_Type()
)
sleRIPngAggregateControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAggregateControlTimeStamp.setStatus("current")
_SleRIPngAggregateControlReqResult_Type = SleControlRequestResultType
_SleRIPngAggregateControlReqResult_Object = MibScalar
sleRIPngAggregateControlReqResult = _SleRIPngAggregateControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2, 5),
    _SleRIPngAggregateControlReqResult_Type()
)
sleRIPngAggregateControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAggregateControlReqResult.setStatus("current")
_SleRIPngAggregateControlAddr_Type = InetAddress
_SleRIPngAggregateControlAddr_Object = MibScalar
sleRIPngAggregateControlAddr = _SleRIPngAggregateControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2, 6),
    _SleRIPngAggregateControlAddr_Type()
)
sleRIPngAggregateControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAggregateControlAddr.setStatus("current")


class _SleRIPngAggregateControlMask_Type(Integer32):
    """Custom type sleRIPngAggregateControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleRIPngAggregateControlMask_Type.__name__ = "Integer32"
_SleRIPngAggregateControlMask_Object = MibScalar
sleRIPngAggregateControlMask = _SleRIPngAggregateControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 2, 7),
    _SleRIPngAggregateControlMask_Type()
)
sleRIPngAggregateControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAggregateControlMask.setStatus("current")
_SleRIPngAggregateNotification_ObjectIdentity = ObjectIdentity
sleRIPngAggregateNotification = _SleRIPngAggregateNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 3)
)
_SleRIPngNeighbor_ObjectIdentity = ObjectIdentity
sleRIPngNeighbor = _SleRIPngNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3)
)
_SleRIPngNeighborTable_Object = MibTable
sleRIPngNeighborTable = _SleRIPngNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 1)
)
if mibBuilder.loadTexts:
    sleRIPngNeighborTable.setStatus("current")
_SleRIPngNeighborEntry_Object = MibTableRow
sleRIPngNeighborEntry = _SleRIPngNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 1, 1)
)
sleRIPngNeighborEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngNeighborAddr"),
)
if mibBuilder.loadTexts:
    sleRIPngNeighborEntry.setStatus("current")
_SleRIPngNeighborAddr_Type = InetAddress
_SleRIPngNeighborAddr_Object = MibTableColumn
sleRIPngNeighborAddr = _SleRIPngNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 1, 1, 1),
    _SleRIPngNeighborAddr_Type()
)
sleRIPngNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngNeighborAddr.setStatus("current")


class _SleRIPngNeighborIfName_Type(OctetString):
    """Custom type sleRIPngNeighborIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngNeighborIfName_Type.__name__ = "OctetString"
_SleRIPngNeighborIfName_Object = MibTableColumn
sleRIPngNeighborIfName = _SleRIPngNeighborIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 1, 1, 2),
    _SleRIPngNeighborIfName_Type()
)
sleRIPngNeighborIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngNeighborIfName.setStatus("current")
_SleRIPngNeighborControl_ObjectIdentity = ObjectIdentity
sleRIPngNeighborControl = _SleRIPngNeighborControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2)
)


class _SleRIPngNeighborControlRequest_Type(Integer32):
    """Custom type sleRIPngNeighborControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPngNeighbor", 1),
          ("deleteRIPngNeighbor", 2))
    )


_SleRIPngNeighborControlRequest_Type.__name__ = "Integer32"
_SleRIPngNeighborControlRequest_Object = MibScalar
sleRIPngNeighborControlRequest = _SleRIPngNeighborControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2, 1),
    _SleRIPngNeighborControlRequest_Type()
)
sleRIPngNeighborControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngNeighborControlRequest.setStatus("current")
_SleRIPngNeighborControlStatus_Type = SleControlStatusType
_SleRIPngNeighborControlStatus_Object = MibScalar
sleRIPngNeighborControlStatus = _SleRIPngNeighborControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2, 2),
    _SleRIPngNeighborControlStatus_Type()
)
sleRIPngNeighborControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngNeighborControlStatus.setStatus("current")
_SleRIPngNeighborControlTimer_Type = Gauge32
_SleRIPngNeighborControlTimer_Object = MibScalar
sleRIPngNeighborControlTimer = _SleRIPngNeighborControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2, 3),
    _SleRIPngNeighborControlTimer_Type()
)
sleRIPngNeighborControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngNeighborControlTimer.setStatus("current")
_SleRIPngNeighborControlTimeStamp_Type = TimeTicks
_SleRIPngNeighborControlTimeStamp_Object = MibScalar
sleRIPngNeighborControlTimeStamp = _SleRIPngNeighborControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2, 4),
    _SleRIPngNeighborControlTimeStamp_Type()
)
sleRIPngNeighborControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngNeighborControlTimeStamp.setStatus("current")
_SleRIPngNeighborControlReqResult_Type = SleControlRequestResultType
_SleRIPngNeighborControlReqResult_Object = MibScalar
sleRIPngNeighborControlReqResult = _SleRIPngNeighborControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2, 5),
    _SleRIPngNeighborControlReqResult_Type()
)
sleRIPngNeighborControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngNeighborControlReqResult.setStatus("current")
_SleRIPngNeighborControlAddr_Type = InetAddress
_SleRIPngNeighborControlAddr_Object = MibScalar
sleRIPngNeighborControlAddr = _SleRIPngNeighborControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2, 6),
    _SleRIPngNeighborControlAddr_Type()
)
sleRIPngNeighborControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngNeighborControlAddr.setStatus("current")


class _SleRIPngNeighborControlIfName_Type(OctetString):
    """Custom type sleRIPngNeighborControlIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngNeighborControlIfName_Type.__name__ = "OctetString"
_SleRIPngNeighborControlIfName_Object = MibScalar
sleRIPngNeighborControlIfName = _SleRIPngNeighborControlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 2, 7),
    _SleRIPngNeighborControlIfName_Type()
)
sleRIPngNeighborControlIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngNeighborControlIfName.setStatus("current")
_SleRIPngNeighborNotification_ObjectIdentity = ObjectIdentity
sleRIPngNeighborNotification = _SleRIPngNeighborNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 3)
)
_SleRIPngStaticRoute_ObjectIdentity = ObjectIdentity
sleRIPngStaticRoute = _SleRIPngStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4)
)
_SleRIPngStaticRouteTable_Object = MibTable
sleRIPngStaticRouteTable = _SleRIPngStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 1)
)
if mibBuilder.loadTexts:
    sleRIPngStaticRouteTable.setStatus("current")
_SleRIPngStaticRouteEntry_Object = MibTableRow
sleRIPngStaticRouteEntry = _SleRIPngStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 1, 1)
)
sleRIPngStaticRouteEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngStaticRouteAddr"),
    (0, "SLE-RIPng-MIB", "sleRIPngStaticRouteMask"),
)
if mibBuilder.loadTexts:
    sleRIPngStaticRouteEntry.setStatus("current")
_SleRIPngStaticRouteAddr_Type = InetAddress
_SleRIPngStaticRouteAddr_Object = MibTableColumn
sleRIPngStaticRouteAddr = _SleRIPngStaticRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 1, 1, 1),
    _SleRIPngStaticRouteAddr_Type()
)
sleRIPngStaticRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteAddr.setStatus("current")


class _SleRIPngStaticRouteMask_Type(Integer32):
    """Custom type sleRIPngStaticRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleRIPngStaticRouteMask_Type.__name__ = "Integer32"
_SleRIPngStaticRouteMask_Object = MibTableColumn
sleRIPngStaticRouteMask = _SleRIPngStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 1, 1, 2),
    _SleRIPngStaticRouteMask_Type()
)
sleRIPngStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteMask.setStatus("current")
_SleRIPngStaticRouteControl_ObjectIdentity = ObjectIdentity
sleRIPngStaticRouteControl = _SleRIPngStaticRouteControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2)
)


class _SleRIPngStaticRouteControlRequest_Type(Integer32):
    """Custom type sleRIPngStaticRouteControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPngStaticRoute", 1),
          ("deleteRIPngStaticRoute", 2))
    )


_SleRIPngStaticRouteControlRequest_Type.__name__ = "Integer32"
_SleRIPngStaticRouteControlRequest_Object = MibScalar
sleRIPngStaticRouteControlRequest = _SleRIPngStaticRouteControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2, 1),
    _SleRIPngStaticRouteControlRequest_Type()
)
sleRIPngStaticRouteControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteControlRequest.setStatus("current")
_SleRIPngStaticRouteControlStatus_Type = SleControlStatusType
_SleRIPngStaticRouteControlStatus_Object = MibScalar
sleRIPngStaticRouteControlStatus = _SleRIPngStaticRouteControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2, 2),
    _SleRIPngStaticRouteControlStatus_Type()
)
sleRIPngStaticRouteControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteControlStatus.setStatus("current")
_SleRIPngStaticRouteControlTimer_Type = Gauge32
_SleRIPngStaticRouteControlTimer_Object = MibScalar
sleRIPngStaticRouteControlTimer = _SleRIPngStaticRouteControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2, 3),
    _SleRIPngStaticRouteControlTimer_Type()
)
sleRIPngStaticRouteControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteControlTimer.setStatus("current")
_SleRIPngStaticRouteControlTimeStamp_Type = TimeTicks
_SleRIPngStaticRouteControlTimeStamp_Object = MibScalar
sleRIPngStaticRouteControlTimeStamp = _SleRIPngStaticRouteControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2, 4),
    _SleRIPngStaticRouteControlTimeStamp_Type()
)
sleRIPngStaticRouteControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteControlTimeStamp.setStatus("current")
_SleRIPngStaticRouteControlReqResult_Type = SleControlRequestResultType
_SleRIPngStaticRouteControlReqResult_Object = MibScalar
sleRIPngStaticRouteControlReqResult = _SleRIPngStaticRouteControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2, 5),
    _SleRIPngStaticRouteControlReqResult_Type()
)
sleRIPngStaticRouteControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteControlReqResult.setStatus("current")
_SleRIPngStaticRouteControlAddr_Type = InetAddress
_SleRIPngStaticRouteControlAddr_Object = MibScalar
sleRIPngStaticRouteControlAddr = _SleRIPngStaticRouteControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2, 6),
    _SleRIPngStaticRouteControlAddr_Type()
)
sleRIPngStaticRouteControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteControlAddr.setStatus("current")


class _SleRIPngStaticRouteControlMask_Type(Integer32):
    """Custom type sleRIPngStaticRouteControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleRIPngStaticRouteControlMask_Type.__name__ = "Integer32"
_SleRIPngStaticRouteControlMask_Object = MibScalar
sleRIPngStaticRouteControlMask = _SleRIPngStaticRouteControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 2, 7),
    _SleRIPngStaticRouteControlMask_Type()
)
sleRIPngStaticRouteControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngStaticRouteControlMask.setStatus("current")
_SleRIPngStaticRouteNotification_ObjectIdentity = ObjectIdentity
sleRIPngStaticRouteNotification = _SleRIPngStaticRouteNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 3)
)
_SleRIPngAdminDistance_ObjectIdentity = ObjectIdentity
sleRIPngAdminDistance = _SleRIPngAdminDistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5)
)
_SleRIPngAdminDistanceTable_Object = MibTable
sleRIPngAdminDistanceTable = _SleRIPngAdminDistanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 1)
)
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceTable.setStatus("current")
_SleRIPngAdminDistanceEntry_Object = MibTableRow
sleRIPngAdminDistanceEntry = _SleRIPngAdminDistanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 1, 1)
)
sleRIPngAdminDistanceEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngAdminDistanceValue"),
    (0, "SLE-RIPng-MIB", "sleRIPngAdminDistanceAddr"),
    (0, "SLE-RIPng-MIB", "sleRIPngAdminDistanceMask"),
)
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceEntry.setStatus("current")


class _SleRIPngAdminDistanceValue_Type(Integer32):
    """Custom type sleRIPngAdminDistanceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPngAdminDistanceValue_Type.__name__ = "Integer32"
_SleRIPngAdminDistanceValue_Object = MibTableColumn
sleRIPngAdminDistanceValue = _SleRIPngAdminDistanceValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 1, 1, 1),
    _SleRIPngAdminDistanceValue_Type()
)
sleRIPngAdminDistanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceValue.setStatus("current")
_SleRIPngAdminDistanceAddr_Type = InetAddress
_SleRIPngAdminDistanceAddr_Object = MibTableColumn
sleRIPngAdminDistanceAddr = _SleRIPngAdminDistanceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 1, 1, 2),
    _SleRIPngAdminDistanceAddr_Type()
)
sleRIPngAdminDistanceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceAddr.setStatus("current")


class _SleRIPngAdminDistanceMask_Type(Integer32):
    """Custom type sleRIPngAdminDistanceMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleRIPngAdminDistanceMask_Type.__name__ = "Integer32"
_SleRIPngAdminDistanceMask_Object = MibTableColumn
sleRIPngAdminDistanceMask = _SleRIPngAdminDistanceMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 1, 1, 3),
    _SleRIPngAdminDistanceMask_Type()
)
sleRIPngAdminDistanceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceMask.setStatus("current")


class _SleRIPngAdminDistanceAccessName_Type(OctetString):
    """Custom type sleRIPngAdminDistanceAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngAdminDistanceAccessName_Type.__name__ = "OctetString"
_SleRIPngAdminDistanceAccessName_Object = MibTableColumn
sleRIPngAdminDistanceAccessName = _SleRIPngAdminDistanceAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 1, 1, 4),
    _SleRIPngAdminDistanceAccessName_Type()
)
sleRIPngAdminDistanceAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceAccessName.setStatus("current")
_SleRIPngAdminDistanceControl_ObjectIdentity = ObjectIdentity
sleRIPngAdminDistanceControl = _SleRIPngAdminDistanceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2)
)


class _SleRIPngAdminDistanceControlRequest_Type(Integer32):
    """Custom type sleRIPngAdminDistanceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPngAdminDistance", 1),
          ("deleteRIPngAdminDistance", 2))
    )


_SleRIPngAdminDistanceControlRequest_Type.__name__ = "Integer32"
_SleRIPngAdminDistanceControlRequest_Object = MibScalar
sleRIPngAdminDistanceControlRequest = _SleRIPngAdminDistanceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 1),
    _SleRIPngAdminDistanceControlRequest_Type()
)
sleRIPngAdminDistanceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlRequest.setStatus("current")
_SleRIPngAdminDistanceControlStatus_Type = SleControlStatusType
_SleRIPngAdminDistanceControlStatus_Object = MibScalar
sleRIPngAdminDistanceControlStatus = _SleRIPngAdminDistanceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 2),
    _SleRIPngAdminDistanceControlStatus_Type()
)
sleRIPngAdminDistanceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlStatus.setStatus("current")
_SleRIPngAdminDistanceControlTimer_Type = Gauge32
_SleRIPngAdminDistanceControlTimer_Object = MibScalar
sleRIPngAdminDistanceControlTimer = _SleRIPngAdminDistanceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 3),
    _SleRIPngAdminDistanceControlTimer_Type()
)
sleRIPngAdminDistanceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlTimer.setStatus("current")
_SleRIPngAdminDistanceControlTimeStamp_Type = TimeTicks
_SleRIPngAdminDistanceControlTimeStamp_Object = MibScalar
sleRIPngAdminDistanceControlTimeStamp = _SleRIPngAdminDistanceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 4),
    _SleRIPngAdminDistanceControlTimeStamp_Type()
)
sleRIPngAdminDistanceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlTimeStamp.setStatus("current")
_SleRIPngAdminDistanceControlReqResult_Type = SleControlRequestResultType
_SleRIPngAdminDistanceControlReqResult_Object = MibScalar
sleRIPngAdminDistanceControlReqResult = _SleRIPngAdminDistanceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 5),
    _SleRIPngAdminDistanceControlReqResult_Type()
)
sleRIPngAdminDistanceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlReqResult.setStatus("current")


class _SleRIPngAdminDistanceControlValue_Type(Integer32):
    """Custom type sleRIPngAdminDistanceControlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPngAdminDistanceControlValue_Type.__name__ = "Integer32"
_SleRIPngAdminDistanceControlValue_Object = MibScalar
sleRIPngAdminDistanceControlValue = _SleRIPngAdminDistanceControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 6),
    _SleRIPngAdminDistanceControlValue_Type()
)
sleRIPngAdminDistanceControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlValue.setStatus("current")
_SleRIPngAdminDistanceControlAddr_Type = InetAddress
_SleRIPngAdminDistanceControlAddr_Object = MibScalar
sleRIPngAdminDistanceControlAddr = _SleRIPngAdminDistanceControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 7),
    _SleRIPngAdminDistanceControlAddr_Type()
)
sleRIPngAdminDistanceControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlAddr.setStatus("current")


class _SleRIPngAdminDistanceControlMask_Type(Integer32):
    """Custom type sleRIPngAdminDistanceControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SleRIPngAdminDistanceControlMask_Type.__name__ = "Integer32"
_SleRIPngAdminDistanceControlMask_Object = MibScalar
sleRIPngAdminDistanceControlMask = _SleRIPngAdminDistanceControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 8),
    _SleRIPngAdminDistanceControlMask_Type()
)
sleRIPngAdminDistanceControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlMask.setStatus("current")


class _SleRIPngAdminDistanceControlAccessName_Type(OctetString):
    """Custom type sleRIPngAdminDistanceControlAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngAdminDistanceControlAccessName_Type.__name__ = "OctetString"
_SleRIPngAdminDistanceControlAccessName_Object = MibScalar
sleRIPngAdminDistanceControlAccessName = _SleRIPngAdminDistanceControlAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 2, 9),
    _SleRIPngAdminDistanceControlAccessName_Type()
)
sleRIPngAdminDistanceControlAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceControlAccessName.setStatus("current")
_SleRIPngAdminDistanceNotification_ObjectIdentity = ObjectIdentity
sleRIPngAdminDistanceNotification = _SleRIPngAdminDistanceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 3)
)
_SleRIPngDistribute_ObjectIdentity = ObjectIdentity
sleRIPngDistribute = _SleRIPngDistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6)
)
_SleRIPngDistributeTable_Object = MibTable
sleRIPngDistributeTable = _SleRIPngDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 1)
)
if mibBuilder.loadTexts:
    sleRIPngDistributeTable.setStatus("current")
_SleRIPngDistributeEntry_Object = MibTableRow
sleRIPngDistributeEntry = _SleRIPngDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 1, 1)
)
sleRIPngDistributeEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngDistributeIfName"),
)
if mibBuilder.loadTexts:
    sleRIPngDistributeEntry.setStatus("current")


class _SleRIPngDistributeIfName_Type(OctetString):
    """Custom type sleRIPngDistributeIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeIfName_Type.__name__ = "OctetString"
_SleRIPngDistributeIfName_Object = MibTableColumn
sleRIPngDistributeIfName = _SleRIPngDistributeIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 1, 1, 1),
    _SleRIPngDistributeIfName_Type()
)
sleRIPngDistributeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeIfName.setStatus("current")


class _SleRIPngDistributeInAccessName_Type(OctetString):
    """Custom type sleRIPngDistributeInAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeInAccessName_Type.__name__ = "OctetString"
_SleRIPngDistributeInAccessName_Object = MibTableColumn
sleRIPngDistributeInAccessName = _SleRIPngDistributeInAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 1, 1, 2),
    _SleRIPngDistributeInAccessName_Type()
)
sleRIPngDistributeInAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeInAccessName.setStatus("current")


class _SleRIPngDistributeOutAccessName_Type(OctetString):
    """Custom type sleRIPngDistributeOutAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeOutAccessName_Type.__name__ = "OctetString"
_SleRIPngDistributeOutAccessName_Object = MibTableColumn
sleRIPngDistributeOutAccessName = _SleRIPngDistributeOutAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 1, 1, 3),
    _SleRIPngDistributeOutAccessName_Type()
)
sleRIPngDistributeOutAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeOutAccessName.setStatus("current")


class _SleRIPngDistributeInPrefixName_Type(OctetString):
    """Custom type sleRIPngDistributeInPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeInPrefixName_Type.__name__ = "OctetString"
_SleRIPngDistributeInPrefixName_Object = MibTableColumn
sleRIPngDistributeInPrefixName = _SleRIPngDistributeInPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 1, 1, 4),
    _SleRIPngDistributeInPrefixName_Type()
)
sleRIPngDistributeInPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeInPrefixName.setStatus("current")


class _SleRIPngDistributeOutPrefixName_Type(OctetString):
    """Custom type sleRIPngDistributeOutPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeOutPrefixName_Type.__name__ = "OctetString"
_SleRIPngDistributeOutPrefixName_Object = MibTableColumn
sleRIPngDistributeOutPrefixName = _SleRIPngDistributeOutPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 1, 1, 5),
    _SleRIPngDistributeOutPrefixName_Type()
)
sleRIPngDistributeOutPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeOutPrefixName.setStatus("current")
_SleRIPngDistributeControl_ObjectIdentity = ObjectIdentity
sleRIPngDistributeControl = _SleRIPngDistributeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2)
)


class _SleRIPngDistributeControlRequest_Type(Integer32):
    """Custom type sleRIPngDistributeControlRequest based on Integer32"""
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
        *(("createRIPngDistributeInAccess", 1),
          ("deleteRIPngDistributeInAccess", 2),
          ("createRIPngDistributeOutAccess", 3),
          ("deleteRIPngDistributeOutAccess", 4),
          ("createRIPngDistributeInPrefix", 5),
          ("deleteRIPngDistributeInPrefix", 6),
          ("createRIPngDistributeOutPrefix", 7),
          ("deleteRIPngDistributeOutPrefix", 8))
    )


_SleRIPngDistributeControlRequest_Type.__name__ = "Integer32"
_SleRIPngDistributeControlRequest_Object = MibScalar
sleRIPngDistributeControlRequest = _SleRIPngDistributeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 1),
    _SleRIPngDistributeControlRequest_Type()
)
sleRIPngDistributeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlRequest.setStatus("current")
_SleRIPngDistributeControlStatus_Type = SleControlStatusType
_SleRIPngDistributeControlStatus_Object = MibScalar
sleRIPngDistributeControlStatus = _SleRIPngDistributeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 2),
    _SleRIPngDistributeControlStatus_Type()
)
sleRIPngDistributeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlStatus.setStatus("current")
_SleRIPngDistributeControlTimer_Type = Gauge32
_SleRIPngDistributeControlTimer_Object = MibScalar
sleRIPngDistributeControlTimer = _SleRIPngDistributeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 3),
    _SleRIPngDistributeControlTimer_Type()
)
sleRIPngDistributeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlTimer.setStatus("current")
_SleRIPngDistributeControlTimeStamp_Type = TimeTicks
_SleRIPngDistributeControlTimeStamp_Object = MibScalar
sleRIPngDistributeControlTimeStamp = _SleRIPngDistributeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 4),
    _SleRIPngDistributeControlTimeStamp_Type()
)
sleRIPngDistributeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlTimeStamp.setStatus("current")
_SleRIPngDistributeControlReqResult_Type = SleControlRequestResultType
_SleRIPngDistributeControlReqResult_Object = MibScalar
sleRIPngDistributeControlReqResult = _SleRIPngDistributeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 5),
    _SleRIPngDistributeControlReqResult_Type()
)
sleRIPngDistributeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlReqResult.setStatus("current")


class _SleRIPngDistributeControlIfName_Type(OctetString):
    """Custom type sleRIPngDistributeControlIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeControlIfName_Type.__name__ = "OctetString"
_SleRIPngDistributeControlIfName_Object = MibScalar
sleRIPngDistributeControlIfName = _SleRIPngDistributeControlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 6),
    _SleRIPngDistributeControlIfName_Type()
)
sleRIPngDistributeControlIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlIfName.setStatus("current")


class _SleRIPngDistributeControlInAccessName_Type(OctetString):
    """Custom type sleRIPngDistributeControlInAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeControlInAccessName_Type.__name__ = "OctetString"
_SleRIPngDistributeControlInAccessName_Object = MibScalar
sleRIPngDistributeControlInAccessName = _SleRIPngDistributeControlInAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 7),
    _SleRIPngDistributeControlInAccessName_Type()
)
sleRIPngDistributeControlInAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlInAccessName.setStatus("current")


class _SleRIPngDistributeControlOutAccessName_Type(OctetString):
    """Custom type sleRIPngDistributeControlOutAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeControlOutAccessName_Type.__name__ = "OctetString"
_SleRIPngDistributeControlOutAccessName_Object = MibScalar
sleRIPngDistributeControlOutAccessName = _SleRIPngDistributeControlOutAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 8),
    _SleRIPngDistributeControlOutAccessName_Type()
)
sleRIPngDistributeControlOutAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlOutAccessName.setStatus("current")


class _SleRIPngDistributeControlInPrefixName_Type(OctetString):
    """Custom type sleRIPngDistributeControlInPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeControlInPrefixName_Type.__name__ = "OctetString"
_SleRIPngDistributeControlInPrefixName_Object = MibScalar
sleRIPngDistributeControlInPrefixName = _SleRIPngDistributeControlInPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 9),
    _SleRIPngDistributeControlInPrefixName_Type()
)
sleRIPngDistributeControlInPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlInPrefixName.setStatus("current")


class _SleRIPngDistributeControlOutPrefixName_Type(OctetString):
    """Custom type sleRIPngDistributeControlOutPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngDistributeControlOutPrefixName_Type.__name__ = "OctetString"
_SleRIPngDistributeControlOutPrefixName_Object = MibScalar
sleRIPngDistributeControlOutPrefixName = _SleRIPngDistributeControlOutPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 2, 10),
    _SleRIPngDistributeControlOutPrefixName_Type()
)
sleRIPngDistributeControlOutPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngDistributeControlOutPrefixName.setStatus("current")
_SleRIPngDistributeNotification_ObjectIdentity = ObjectIdentity
sleRIPngDistributeNotification = _SleRIPngDistributeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3)
)
_SleRIPngOffsetList_ObjectIdentity = ObjectIdentity
sleRIPngOffsetList = _SleRIPngOffsetList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7)
)
_SleRIPngOffsetListTable_Object = MibTable
sleRIPngOffsetListTable = _SleRIPngOffsetListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 1)
)
if mibBuilder.loadTexts:
    sleRIPngOffsetListTable.setStatus("current")
_SleRIPngOffsetListEntry_Object = MibTableRow
sleRIPngOffsetListEntry = _SleRIPngOffsetListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 1, 1)
)
sleRIPngOffsetListEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngOffsetListIfname"),
)
if mibBuilder.loadTexts:
    sleRIPngOffsetListEntry.setStatus("current")


class _SleRIPngOffsetListIfname_Type(OctetString):
    """Custom type sleRIPngOffsetListIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngOffsetListIfname_Type.__name__ = "OctetString"
_SleRIPngOffsetListIfname_Object = MibTableColumn
sleRIPngOffsetListIfname = _SleRIPngOffsetListIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 1, 1, 1),
    _SleRIPngOffsetListIfname_Type()
)
sleRIPngOffsetListIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListIfname.setStatus("current")


class _SleRIPngOffsetListInAccName_Type(OctetString):
    """Custom type sleRIPngOffsetListInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngOffsetListInAccName_Type.__name__ = "OctetString"
_SleRIPngOffsetListInAccName_Object = MibTableColumn
sleRIPngOffsetListInAccName = _SleRIPngOffsetListInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 1, 1, 2),
    _SleRIPngOffsetListInAccName_Type()
)
sleRIPngOffsetListInAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListInAccName.setStatus("current")


class _SleRIPngOffsetListInMetric_Type(Integer32):
    """Custom type sleRIPngOffsetListInMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPngOffsetListInMetric_Type.__name__ = "Integer32"
_SleRIPngOffsetListInMetric_Object = MibTableColumn
sleRIPngOffsetListInMetric = _SleRIPngOffsetListInMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 1, 1, 3),
    _SleRIPngOffsetListInMetric_Type()
)
sleRIPngOffsetListInMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListInMetric.setStatus("current")


class _SleRIPngOffsetListOutAccName_Type(OctetString):
    """Custom type sleRIPngOffsetListOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngOffsetListOutAccName_Type.__name__ = "OctetString"
_SleRIPngOffsetListOutAccName_Object = MibTableColumn
sleRIPngOffsetListOutAccName = _SleRIPngOffsetListOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 1, 1, 4),
    _SleRIPngOffsetListOutAccName_Type()
)
sleRIPngOffsetListOutAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListOutAccName.setStatus("current")


class _SleRIPngOffsetListOutMetric_Type(Integer32):
    """Custom type sleRIPngOffsetListOutMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPngOffsetListOutMetric_Type.__name__ = "Integer32"
_SleRIPngOffsetListOutMetric_Object = MibTableColumn
sleRIPngOffsetListOutMetric = _SleRIPngOffsetListOutMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 1, 1, 5),
    _SleRIPngOffsetListOutMetric_Type()
)
sleRIPngOffsetListOutMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListOutMetric.setStatus("current")
_SleRIPngOffsetListControl_ObjectIdentity = ObjectIdentity
sleRIPngOffsetListControl = _SleRIPngOffsetListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2)
)


class _SleRIPngOffsetListControlRequest_Type(Integer32):
    """Custom type sleRIPngOffsetListControlRequest based on Integer32"""
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
        *(("createRIPngOffsetListIn", 1),
          ("deleteRIPngOffsetListIn", 2),
          ("createRIPngOffsetListOut", 3),
          ("deleteRIPngOffsetListOut", 4))
    )


_SleRIPngOffsetListControlRequest_Type.__name__ = "Integer32"
_SleRIPngOffsetListControlRequest_Object = MibScalar
sleRIPngOffsetListControlRequest = _SleRIPngOffsetListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 1),
    _SleRIPngOffsetListControlRequest_Type()
)
sleRIPngOffsetListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlRequest.setStatus("current")
_SleRIPngOffsetListControlStatus_Type = SleControlStatusType
_SleRIPngOffsetListControlStatus_Object = MibScalar
sleRIPngOffsetListControlStatus = _SleRIPngOffsetListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 2),
    _SleRIPngOffsetListControlStatus_Type()
)
sleRIPngOffsetListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlStatus.setStatus("current")
_SleRIPngOffsetListControlTimer_Type = Gauge32
_SleRIPngOffsetListControlTimer_Object = MibScalar
sleRIPngOffsetListControlTimer = _SleRIPngOffsetListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 3),
    _SleRIPngOffsetListControlTimer_Type()
)
sleRIPngOffsetListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlTimer.setStatus("current")
_SleRIPngOffsetListControlTimeStamp_Type = TimeTicks
_SleRIPngOffsetListControlTimeStamp_Object = MibScalar
sleRIPngOffsetListControlTimeStamp = _SleRIPngOffsetListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 4),
    _SleRIPngOffsetListControlTimeStamp_Type()
)
sleRIPngOffsetListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlTimeStamp.setStatus("current")
_SleRIPngOffsetListControlReqResult_Type = SleControlRequestResultType
_SleRIPngOffsetListControlReqResult_Object = MibScalar
sleRIPngOffsetListControlReqResult = _SleRIPngOffsetListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 5),
    _SleRIPngOffsetListControlReqResult_Type()
)
sleRIPngOffsetListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlReqResult.setStatus("current")


class _SleRIPngOffsetListControlIfname_Type(OctetString):
    """Custom type sleRIPngOffsetListControlIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngOffsetListControlIfname_Type.__name__ = "OctetString"
_SleRIPngOffsetListControlIfname_Object = MibScalar
sleRIPngOffsetListControlIfname = _SleRIPngOffsetListControlIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 6),
    _SleRIPngOffsetListControlIfname_Type()
)
sleRIPngOffsetListControlIfname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlIfname.setStatus("current")


class _SleRIPngOffsetListControlInAccName_Type(OctetString):
    """Custom type sleRIPngOffsetListControlInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngOffsetListControlInAccName_Type.__name__ = "OctetString"
_SleRIPngOffsetListControlInAccName_Object = MibScalar
sleRIPngOffsetListControlInAccName = _SleRIPngOffsetListControlInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 7),
    _SleRIPngOffsetListControlInAccName_Type()
)
sleRIPngOffsetListControlInAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlInAccName.setStatus("current")


class _SleRIPngOffsetListControlInMetric_Type(Integer32):
    """Custom type sleRIPngOffsetListControlInMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPngOffsetListControlInMetric_Type.__name__ = "Integer32"
_SleRIPngOffsetListControlInMetric_Object = MibScalar
sleRIPngOffsetListControlInMetric = _SleRIPngOffsetListControlInMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 8),
    _SleRIPngOffsetListControlInMetric_Type()
)
sleRIPngOffsetListControlInMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlInMetric.setStatus("current")


class _SleRIPngOffsetListControlOutAccName_Type(OctetString):
    """Custom type sleRIPngOffsetListControlOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngOffsetListControlOutAccName_Type.__name__ = "OctetString"
_SleRIPngOffsetListControlOutAccName_Object = MibScalar
sleRIPngOffsetListControlOutAccName = _SleRIPngOffsetListControlOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 9),
    _SleRIPngOffsetListControlOutAccName_Type()
)
sleRIPngOffsetListControlOutAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlOutAccName.setStatus("current")


class _SleRIPngOffsetListControlOutMetric_Type(Integer32):
    """Custom type sleRIPngOffsetListControlOutMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPngOffsetListControlOutMetric_Type.__name__ = "Integer32"
_SleRIPngOffsetListControlOutMetric_Object = MibScalar
sleRIPngOffsetListControlOutMetric = _SleRIPngOffsetListControlOutMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 2, 10),
    _SleRIPngOffsetListControlOutMetric_Type()
)
sleRIPngOffsetListControlOutMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngOffsetListControlOutMetric.setStatus("current")
_SleRIPngOffsetListNotification_ObjectIdentity = ObjectIdentity
sleRIPngOffsetListNotification = _SleRIPngOffsetListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 3)
)
_SleRIPngRedistribute_ObjectIdentity = ObjectIdentity
sleRIPngRedistribute = _SleRIPngRedistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8)
)
_SleRIPngRedistributeTable_Object = MibTable
sleRIPngRedistributeTable = _SleRIPngRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 1)
)
if mibBuilder.loadTexts:
    sleRIPngRedistributeTable.setStatus("current")
_SleRIPngRedistributeEntry_Object = MibTableRow
sleRIPngRedistributeEntry = _SleRIPngRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 1, 1)
)
sleRIPngRedistributeEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngRedistType"),
)
if mibBuilder.loadTexts:
    sleRIPngRedistributeEntry.setStatus("current")


class _SleRIPngRedistType_Type(Integer32):
    """Custom type sleRIPngRedistType based on Integer32"""
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
          ("bgp", 4),
          ("ospf", 5))
    )


_SleRIPngRedistType_Type.__name__ = "Integer32"
_SleRIPngRedistType_Object = MibTableColumn
sleRIPngRedistType = _SleRIPngRedistType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 1, 1, 1),
    _SleRIPngRedistType_Type()
)
sleRIPngRedistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRedistType.setStatus("current")


class _SleRIPngRedistMetric_Type(Integer32):
    """Custom type sleRIPngRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleRIPngRedistMetric_Type.__name__ = "Integer32"
_SleRIPngRedistMetric_Object = MibTableColumn
sleRIPngRedistMetric = _SleRIPngRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 1, 1, 2),
    _SleRIPngRedistMetric_Type()
)
sleRIPngRedistMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRedistMetric.setStatus("current")


class _SleRIPngRedistRouteMapName_Type(OctetString):
    """Custom type sleRIPngRedistRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngRedistRouteMapName_Type.__name__ = "OctetString"
_SleRIPngRedistRouteMapName_Object = MibTableColumn
sleRIPngRedistRouteMapName = _SleRIPngRedistRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 1, 1, 3),
    _SleRIPngRedistRouteMapName_Type()
)
sleRIPngRedistRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRedistRouteMapName.setStatus("current")
_SleRIPngRedistributeControl_ObjectIdentity = ObjectIdentity
sleRIPngRedistributeControl = _SleRIPngRedistributeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2)
)


class _SleRIPngRedistControlRequest_Type(Integer32):
    """Custom type sleRIPngRedistControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createRIPngRedistribute", 1),
          ("deleteRIPngRedistribute", 2),
          ("setRIPngRedistribute", 3))
    )


_SleRIPngRedistControlRequest_Type.__name__ = "Integer32"
_SleRIPngRedistControlRequest_Object = MibScalar
sleRIPngRedistControlRequest = _SleRIPngRedistControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 1),
    _SleRIPngRedistControlRequest_Type()
)
sleRIPngRedistControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRedistControlRequest.setStatus("current")
_SleRIPngRedistControlStatus_Type = SleControlStatusType
_SleRIPngRedistControlStatus_Object = MibScalar
sleRIPngRedistControlStatus = _SleRIPngRedistControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 2),
    _SleRIPngRedistControlStatus_Type()
)
sleRIPngRedistControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRedistControlStatus.setStatus("current")
_SleRIPngRedistControlTimer_Type = Gauge32
_SleRIPngRedistControlTimer_Object = MibScalar
sleRIPngRedistControlTimer = _SleRIPngRedistControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 3),
    _SleRIPngRedistControlTimer_Type()
)
sleRIPngRedistControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRedistControlTimer.setStatus("current")
_SleRIPngRedistControlTimeStamp_Type = TimeTicks
_SleRIPngRedistControlTimeStamp_Object = MibScalar
sleRIPngRedistControlTimeStamp = _SleRIPngRedistControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 4),
    _SleRIPngRedistControlTimeStamp_Type()
)
sleRIPngRedistControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRedistControlTimeStamp.setStatus("current")
_SleRIPngRedistControlReqResult_Type = SleControlRequestResultType
_SleRIPngRedistControlReqResult_Object = MibScalar
sleRIPngRedistControlReqResult = _SleRIPngRedistControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 5),
    _SleRIPngRedistControlReqResult_Type()
)
sleRIPngRedistControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRedistControlReqResult.setStatus("current")


class _SleRIPngRedistControlType_Type(Integer32):
    """Custom type sleRIPngRedistControlType based on Integer32"""
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
          ("bgp", 4),
          ("ospf", 5))
    )


_SleRIPngRedistControlType_Type.__name__ = "Integer32"
_SleRIPngRedistControlType_Object = MibScalar
sleRIPngRedistControlType = _SleRIPngRedistControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 6),
    _SleRIPngRedistControlType_Type()
)
sleRIPngRedistControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRedistControlType.setStatus("current")


class _SleRIPngRedistControlMetric_Type(Integer32):
    """Custom type sleRIPngRedistControlMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleRIPngRedistControlMetric_Type.__name__ = "Integer32"
_SleRIPngRedistControlMetric_Object = MibScalar
sleRIPngRedistControlMetric = _SleRIPngRedistControlMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 7),
    _SleRIPngRedistControlMetric_Type()
)
sleRIPngRedistControlMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRedistControlMetric.setStatus("current")


class _SleRIPngRedistControlRouteMapName_Type(OctetString):
    """Custom type sleRIPngRedistControlRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngRedistControlRouteMapName_Type.__name__ = "OctetString"
_SleRIPngRedistControlRouteMapName_Object = MibScalar
sleRIPngRedistControlRouteMapName = _SleRIPngRedistControlRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 2, 8),
    _SleRIPngRedistControlRouteMapName_Type()
)
sleRIPngRedistControlRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRedistControlRouteMapName.setStatus("current")
_SleRIPngRedistributeNotification_ObjectIdentity = ObjectIdentity
sleRIPngRedistributeNotification = _SleRIPngRedistributeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 3)
)
_SleRIPngRoutemap_ObjectIdentity = ObjectIdentity
sleRIPngRoutemap = _SleRIPngRoutemap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9)
)
_SleRIPngRoutemapTable_Object = MibTable
sleRIPngRoutemapTable = _SleRIPngRoutemapTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 1)
)
if mibBuilder.loadTexts:
    sleRIPngRoutemapTable.setStatus("current")
_SleRIPngRoutemapEntry_Object = MibTableRow
sleRIPngRoutemapEntry = _SleRIPngRoutemapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 1, 1)
)
sleRIPngRoutemapEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngRoutemapName"),
    (0, "SLE-RIPng-MIB", "sleRIPngRoutemapType"),
    (0, "SLE-RIPng-MIB", "sleRIPngRoutemapIfname"),
)
if mibBuilder.loadTexts:
    sleRIPngRoutemapEntry.setStatus("current")


class _SleRIPngRoutemapName_Type(OctetString):
    """Custom type sleRIPngRoutemapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngRoutemapName_Type.__name__ = "OctetString"
_SleRIPngRoutemapName_Object = MibTableColumn
sleRIPngRoutemapName = _SleRIPngRoutemapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 1, 1, 1),
    _SleRIPngRoutemapName_Type()
)
sleRIPngRoutemapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutemapName.setStatus("current")


class _SleRIPngRoutemapType_Type(Integer32):
    """Custom type sleRIPngRoutemapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )


_SleRIPngRoutemapType_Type.__name__ = "Integer32"
_SleRIPngRoutemapType_Object = MibTableColumn
sleRIPngRoutemapType = _SleRIPngRoutemapType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 1, 1, 2),
    _SleRIPngRoutemapType_Type()
)
sleRIPngRoutemapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutemapType.setStatus("current")


class _SleRIPngRoutemapIfname_Type(OctetString):
    """Custom type sleRIPngRoutemapIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngRoutemapIfname_Type.__name__ = "OctetString"
_SleRIPngRoutemapIfname_Object = MibTableColumn
sleRIPngRoutemapIfname = _SleRIPngRoutemapIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 1, 1, 3),
    _SleRIPngRoutemapIfname_Type()
)
sleRIPngRoutemapIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutemapIfname.setStatus("current")
_SleRIPngRoutemapControl_ObjectIdentity = ObjectIdentity
sleRIPngRoutemapControl = _SleRIPngRoutemapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2)
)


class _SleRIPngRoutemapControlRequest_Type(Integer32):
    """Custom type sleRIPngRoutemapControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPngRoutemap", 1),
          ("deleteRIPngRoutemap", 2))
    )


_SleRIPngRoutemapControlRequest_Type.__name__ = "Integer32"
_SleRIPngRoutemapControlRequest_Object = MibScalar
sleRIPngRoutemapControlRequest = _SleRIPngRoutemapControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 1),
    _SleRIPngRoutemapControlRequest_Type()
)
sleRIPngRoutemapControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlRequest.setStatus("current")
_SleRIPngRoutemapControlStatus_Type = SleControlStatusType
_SleRIPngRoutemapControlStatus_Object = MibScalar
sleRIPngRoutemapControlStatus = _SleRIPngRoutemapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 2),
    _SleRIPngRoutemapControlStatus_Type()
)
sleRIPngRoutemapControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlStatus.setStatus("current")
_SleRIPngRoutemapControlTimer_Type = Gauge32
_SleRIPngRoutemapControlTimer_Object = MibScalar
sleRIPngRoutemapControlTimer = _SleRIPngRoutemapControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 3),
    _SleRIPngRoutemapControlTimer_Type()
)
sleRIPngRoutemapControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlTimer.setStatus("current")
_SleRIPngRoutemapControlTimeStamp_Type = TimeTicks
_SleRIPngRoutemapControlTimeStamp_Object = MibScalar
sleRIPngRoutemapControlTimeStamp = _SleRIPngRoutemapControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 4),
    _SleRIPngRoutemapControlTimeStamp_Type()
)
sleRIPngRoutemapControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlTimeStamp.setStatus("current")
_SleRIPngRoutemapControlReqResult_Type = SleControlRequestResultType
_SleRIPngRoutemapControlReqResult_Object = MibScalar
sleRIPngRoutemapControlReqResult = _SleRIPngRoutemapControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 5),
    _SleRIPngRoutemapControlReqResult_Type()
)
sleRIPngRoutemapControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlReqResult.setStatus("current")


class _SleRIPngRoutemapControlName_Type(OctetString):
    """Custom type sleRIPngRoutemapControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngRoutemapControlName_Type.__name__ = "OctetString"
_SleRIPngRoutemapControlName_Object = MibScalar
sleRIPngRoutemapControlName = _SleRIPngRoutemapControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 6),
    _SleRIPngRoutemapControlName_Type()
)
sleRIPngRoutemapControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlName.setStatus("current")


class _SleRIPngRoutemapControlType_Type(Integer32):
    """Custom type sleRIPngRoutemapControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )


_SleRIPngRoutemapControlType_Type.__name__ = "Integer32"
_SleRIPngRoutemapControlType_Object = MibScalar
sleRIPngRoutemapControlType = _SleRIPngRoutemapControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 7),
    _SleRIPngRoutemapControlType_Type()
)
sleRIPngRoutemapControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlType.setStatus("current")


class _SleRIPngRoutemapControlIfname_Type(OctetString):
    """Custom type sleRIPngRoutemapControlIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngRoutemapControlIfname_Type.__name__ = "OctetString"
_SleRIPngRoutemapControlIfname_Object = MibScalar
sleRIPngRoutemapControlIfname = _SleRIPngRoutemapControlIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 2, 8),
    _SleRIPngRoutemapControlIfname_Type()
)
sleRIPngRoutemapControlIfname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngRoutemapControlIfname.setStatus("current")
_SleRIPngRoutemapNotification_ObjectIdentity = ObjectIdentity
sleRIPngRoutemapNotification = _SleRIPngRoutemapNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 3)
)
_SleRIPngPassInterface_ObjectIdentity = ObjectIdentity
sleRIPngPassInterface = _SleRIPngPassInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10)
)
_SleRIPngPassInterfaceTable_Object = MibTable
sleRIPngPassInterfaceTable = _SleRIPngPassInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 1)
)
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceTable.setStatus("current")
_SleRIPngPassInterfaceEntry_Object = MibTableRow
sleRIPngPassInterfaceEntry = _SleRIPngPassInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 1, 1)
)
sleRIPngPassInterfaceEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngPassInterfaceName"),
)
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceEntry.setStatus("current")


class _SleRIPngPassInterfaceName_Type(OctetString):
    """Custom type sleRIPngPassInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngPassInterfaceName_Type.__name__ = "OctetString"
_SleRIPngPassInterfaceName_Object = MibTableColumn
sleRIPngPassInterfaceName = _SleRIPngPassInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 1, 1, 1),
    _SleRIPngPassInterfaceName_Type()
)
sleRIPngPassInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceName.setStatus("current")
_SleRIPngPassInterfaceControl_ObjectIdentity = ObjectIdentity
sleRIPngPassInterfaceControl = _SleRIPngPassInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 2)
)


class _SleRIPngPassInterfaceControlRequest_Type(Integer32):
    """Custom type sleRIPngPassInterfaceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPngPassInterface", 1),
          ("deleteRIPngPassInterface", 2))
    )


_SleRIPngPassInterfaceControlRequest_Type.__name__ = "Integer32"
_SleRIPngPassInterfaceControlRequest_Object = MibScalar
sleRIPngPassInterfaceControlRequest = _SleRIPngPassInterfaceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 2, 1),
    _SleRIPngPassInterfaceControlRequest_Type()
)
sleRIPngPassInterfaceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceControlRequest.setStatus("current")
_SleRIPngPassInterfaceControlStatus_Type = SleControlStatusType
_SleRIPngPassInterfaceControlStatus_Object = MibScalar
sleRIPngPassInterfaceControlStatus = _SleRIPngPassInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 2, 2),
    _SleRIPngPassInterfaceControlStatus_Type()
)
sleRIPngPassInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceControlStatus.setStatus("current")
_SleRIPngPassInterfaceControlTimer_Type = Gauge32
_SleRIPngPassInterfaceControlTimer_Object = MibScalar
sleRIPngPassInterfaceControlTimer = _SleRIPngPassInterfaceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 2, 3),
    _SleRIPngPassInterfaceControlTimer_Type()
)
sleRIPngPassInterfaceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceControlTimer.setStatus("current")
_SleRIPngPassInterfaceControlTimeStamp_Type = TimeTicks
_SleRIPngPassInterfaceControlTimeStamp_Object = MibScalar
sleRIPngPassInterfaceControlTimeStamp = _SleRIPngPassInterfaceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 2, 4),
    _SleRIPngPassInterfaceControlTimeStamp_Type()
)
sleRIPngPassInterfaceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceControlTimeStamp.setStatus("current")
_SleRIPngPassInterfaceControlReqResult_Type = SleControlRequestResultType
_SleRIPngPassInterfaceControlReqResult_Object = MibScalar
sleRIPngPassInterfaceControlReqResult = _SleRIPngPassInterfaceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 2, 5),
    _SleRIPngPassInterfaceControlReqResult_Type()
)
sleRIPngPassInterfaceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceControlReqResult.setStatus("current")


class _SleRIPngPassInterfaceControlName_Type(OctetString):
    """Custom type sleRIPngPassInterfaceControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPngPassInterfaceControlName_Type.__name__ = "OctetString"
_SleRIPngPassInterfaceControlName_Object = MibScalar
sleRIPngPassInterfaceControlName = _SleRIPngPassInterfaceControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 2, 6),
    _SleRIPngPassInterfaceControlName_Type()
)
sleRIPngPassInterfaceControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceControlName.setStatus("current")
_SleRIPngPassInterfaceNotification_ObjectIdentity = ObjectIdentity
sleRIPngPassInterfaceNotification = _SleRIPngPassInterfaceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 3)
)
_SleRIPngInterface_ObjectIdentity = ObjectIdentity
sleRIPngInterface = _SleRIPngInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11)
)
_SleRIPngInterfaceTable_Object = MibTable
sleRIPngInterfaceTable = _SleRIPngInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 1)
)
if mibBuilder.loadTexts:
    sleRIPngInterfaceTable.setStatus("current")
_SleRIPngInterfaceEntry_Object = MibTableRow
sleRIPngInterfaceEntry = _SleRIPngInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 1, 1)
)
sleRIPngInterfaceEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sleRIPngInterfaceEntry.setStatus("current")


class _SleRIPngInterfaceIndex_Type(Integer32):
    """Custom type sleRIPngInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleRIPngInterfaceIndex_Type.__name__ = "Integer32"
_SleRIPngInterfaceIndex_Object = MibTableColumn
sleRIPngInterfaceIndex = _SleRIPngInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 1, 1, 1),
    _SleRIPngInterfaceIndex_Type()
)
sleRIPngInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceIndex.setStatus("current")


class _SleRIPngInterfaceRouterMode_Type(Integer32):
    """Custom type sleRIPngInterfaceRouterMode based on Integer32"""
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


_SleRIPngInterfaceRouterMode_Type.__name__ = "Integer32"
_SleRIPngInterfaceRouterMode_Object = MibTableColumn
sleRIPngInterfaceRouterMode = _SleRIPngInterfaceRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 1, 1, 2),
    _SleRIPngInterfaceRouterMode_Type()
)
sleRIPngInterfaceRouterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceRouterMode.setStatus("current")


class _SleRIPngInterfaceRecvPacket_Type(Integer32):
    """Custom type sleRIPngInterfaceRecvPacket based on Integer32"""
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


_SleRIPngInterfaceRecvPacket_Type.__name__ = "Integer32"
_SleRIPngInterfaceRecvPacket_Object = MibTableColumn
sleRIPngInterfaceRecvPacket = _SleRIPngInterfaceRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 1, 1, 3),
    _SleRIPngInterfaceRecvPacket_Type()
)
sleRIPngInterfaceRecvPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceRecvPacket.setStatus("current")


class _SleRIPngInterfaceSendPacket_Type(Integer32):
    """Custom type sleRIPngInterfaceSendPacket based on Integer32"""
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


_SleRIPngInterfaceSendPacket_Type.__name__ = "Integer32"
_SleRIPngInterfaceSendPacket_Object = MibTableColumn
sleRIPngInterfaceSendPacket = _SleRIPngInterfaceSendPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 1, 1, 4),
    _SleRIPngInterfaceSendPacket_Type()
)
sleRIPngInterfaceSendPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceSendPacket.setStatus("current")


class _SleRIPngInterfaceSplitHorizonMode_Type(Integer32):
    """Custom type sleRIPngInterfaceSplitHorizonMode based on Integer32"""
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
          ("withoutPoisonedReverse", 1),
          ("withPoisonedReverse", 2))
    )


_SleRIPngInterfaceSplitHorizonMode_Type.__name__ = "Integer32"
_SleRIPngInterfaceSplitHorizonMode_Object = MibTableColumn
sleRIPngInterfaceSplitHorizonMode = _SleRIPngInterfaceSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 1, 1, 5),
    _SleRIPngInterfaceSplitHorizonMode_Type()
)
sleRIPngInterfaceSplitHorizonMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceSplitHorizonMode.setStatus("current")
_SleRIPngInterfaceControl_ObjectIdentity = ObjectIdentity
sleRIPngInterfaceControl = _SleRIPngInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2)
)


class _SleRIPngInterfaceControlRequest_Type(Integer32):
    """Custom type sleRIPngInterfaceControlRequest based on Integer32"""
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
        *(("createRIPngInterfaceRouterMode", 1),
          ("deleteRIPngInterfaceRouterMode", 2),
          ("setRIPngInterfaceRecvPacketEnable", 3),
          ("setRIPngInterfaceSendPacketEnable", 4),
          ("setRIPngInterfaceSplitHorizonMode", 5))
    )


_SleRIPngInterfaceControlRequest_Type.__name__ = "Integer32"
_SleRIPngInterfaceControlRequest_Object = MibScalar
sleRIPngInterfaceControlRequest = _SleRIPngInterfaceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 1),
    _SleRIPngInterfaceControlRequest_Type()
)
sleRIPngInterfaceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlRequest.setStatus("current")
_SleRIPngInterfaceControlStatus_Type = SleControlStatusType
_SleRIPngInterfaceControlStatus_Object = MibScalar
sleRIPngInterfaceControlStatus = _SleRIPngInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 2),
    _SleRIPngInterfaceControlStatus_Type()
)
sleRIPngInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlStatus.setStatus("current")
_SleRIPngInterfaceControlTimer_Type = Gauge32
_SleRIPngInterfaceControlTimer_Object = MibScalar
sleRIPngInterfaceControlTimer = _SleRIPngInterfaceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 3),
    _SleRIPngInterfaceControlTimer_Type()
)
sleRIPngInterfaceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlTimer.setStatus("current")
_SleRIPngInterfaceControlTimeStamp_Type = TimeTicks
_SleRIPngInterfaceControlTimeStamp_Object = MibScalar
sleRIPngInterfaceControlTimeStamp = _SleRIPngInterfaceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 4),
    _SleRIPngInterfaceControlTimeStamp_Type()
)
sleRIPngInterfaceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlTimeStamp.setStatus("current")
_SleRIPngInterfaceControlReqResult_Type = SleControlRequestResultType
_SleRIPngInterfaceControlReqResult_Object = MibScalar
sleRIPngInterfaceControlReqResult = _SleRIPngInterfaceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 5),
    _SleRIPngInterfaceControlReqResult_Type()
)
sleRIPngInterfaceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlReqResult.setStatus("current")


class _SleRIPngInterfaceControlIndex_Type(Integer32):
    """Custom type sleRIPngInterfaceControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleRIPngInterfaceControlIndex_Type.__name__ = "Integer32"
_SleRIPngInterfaceControlIndex_Object = MibScalar
sleRIPngInterfaceControlIndex = _SleRIPngInterfaceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 6),
    _SleRIPngInterfaceControlIndex_Type()
)
sleRIPngInterfaceControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlIndex.setStatus("current")


class _SleRIPngInterfaceControlRouterMode_Type(SleControlRequestResultType):
    """Custom type sleRIPngInterfaceControlRouterMode based on SleControlRequestResultType"""
    subtypeSpec = SleControlRequestResultType.subtypeSpec
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


_SleRIPngInterfaceControlRouterMode_Type.__name__ = "SleControlRequestResultType"
_SleRIPngInterfaceControlRouterMode_Object = MibScalar
sleRIPngInterfaceControlRouterMode = _SleRIPngInterfaceControlRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 7),
    _SleRIPngInterfaceControlRouterMode_Type()
)
sleRIPngInterfaceControlRouterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlRouterMode.setStatus("current")


class _SleRIPngInterfaceControlRecvPacket_Type(Integer32):
    """Custom type sleRIPngInterfaceControlRecvPacket based on Integer32"""
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


_SleRIPngInterfaceControlRecvPacket_Type.__name__ = "Integer32"
_SleRIPngInterfaceControlRecvPacket_Object = MibScalar
sleRIPngInterfaceControlRecvPacket = _SleRIPngInterfaceControlRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 8),
    _SleRIPngInterfaceControlRecvPacket_Type()
)
sleRIPngInterfaceControlRecvPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlRecvPacket.setStatus("current")


class _SleRIPngInterfaceControlSendPacket_Type(Integer32):
    """Custom type sleRIPngInterfaceControlSendPacket based on Integer32"""
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


_SleRIPngInterfaceControlSendPacket_Type.__name__ = "Integer32"
_SleRIPngInterfaceControlSendPacket_Object = MibScalar
sleRIPngInterfaceControlSendPacket = _SleRIPngInterfaceControlSendPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 9),
    _SleRIPngInterfaceControlSendPacket_Type()
)
sleRIPngInterfaceControlSendPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlSendPacket.setStatus("current")


class _SleRIPngInterfaceControlSplitHorizonMode_Type(Integer32):
    """Custom type sleRIPngInterfaceControlSplitHorizonMode based on Integer32"""
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
          ("withoutPoisonedReverse", 1),
          ("withPoisonedReverse", 2))
    )


_SleRIPngInterfaceControlSplitHorizonMode_Type.__name__ = "Integer32"
_SleRIPngInterfaceControlSplitHorizonMode_Object = MibScalar
sleRIPngInterfaceControlSplitHorizonMode = _SleRIPngInterfaceControlSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 2, 10),
    _SleRIPngInterfaceControlSplitHorizonMode_Type()
)
sleRIPngInterfaceControlSplitHorizonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPngInterfaceControlSplitHorizonMode.setStatus("current")
_SleRIPngInterfaceNotification_ObjectIdentity = ObjectIdentity
sleRIPngInterfaceNotification = _SleRIPngInterfaceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 3)
)
_SleRIPngRoutes_ObjectIdentity = ObjectIdentity
sleRIPngRoutes = _SleRIPngRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12)
)
_SleRIPngRoutesTable_Object = MibTable
sleRIPngRoutesTable = _SleRIPngRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1)
)
if mibBuilder.loadTexts:
    sleRIPngRoutesTable.setStatus("current")
_SleRIPngRoutesEntry_Object = MibTableRow
sleRIPngRoutesEntry = _SleRIPngRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1)
)
sleRIPngRoutesEntry.setIndexNames(
    (0, "SLE-RIPng-MIB", "sleRIPngRoutesType"),
    (0, "SLE-RIPng-MIB", "sleRIPngRoutesPrefix"),
    (0, "SLE-RIPng-MIB", "sleRIPngRoutesMask"),
    (0, "SLE-RIPng-MIB", "sleRIPngRoutesNextHop"),
)
if mibBuilder.loadTexts:
    sleRIPngRoutesEntry.setStatus("current")


class _SleRIPngRoutesType_Type(Integer32):
    """Custom type sleRIPngRoutesType based on Integer32"""
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
        *(("rip", 1),
          ("kernel", 2),
          ("connected", 3),
          ("static", 4),
          ("ospf", 5),
          ("isis", 6),
          ("bgp", 7))
    )


_SleRIPngRoutesType_Type.__name__ = "Integer32"
_SleRIPngRoutesType_Object = MibTableColumn
sleRIPngRoutesType = _SleRIPngRoutesType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 1),
    _SleRIPngRoutesType_Type()
)
sleRIPngRoutesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesType.setStatus("current")
_SleRIPngRoutesPrefix_Type = IpAddress
_SleRIPngRoutesPrefix_Object = MibTableColumn
sleRIPngRoutesPrefix = _SleRIPngRoutesPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 2),
    _SleRIPngRoutesPrefix_Type()
)
sleRIPngRoutesPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesPrefix.setStatus("current")


class _SleRIPngRoutesMask_Type(Integer32):
    """Custom type sleRIPngRoutesMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPngRoutesMask_Type.__name__ = "Integer32"
_SleRIPngRoutesMask_Object = MibTableColumn
sleRIPngRoutesMask = _SleRIPngRoutesMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 3),
    _SleRIPngRoutesMask_Type()
)
sleRIPngRoutesMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesMask.setStatus("current")
_SleRIPngRoutesNextHop_Type = IpAddress
_SleRIPngRoutesNextHop_Object = MibTableColumn
sleRIPngRoutesNextHop = _SleRIPngRoutesNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 4),
    _SleRIPngRoutesNextHop_Type()
)
sleRIPngRoutesNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesNextHop.setStatus("current")


class _SleRIPngRoutesSelected_Type(Integer32):
    """Custom type sleRIPngRoutesSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deselected", 0),
          ("selected", 1))
    )


_SleRIPngRoutesSelected_Type.__name__ = "Integer32"
_SleRIPngRoutesSelected_Object = MibTableColumn
sleRIPngRoutesSelected = _SleRIPngRoutesSelected_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 5),
    _SleRIPngRoutesSelected_Type()
)
sleRIPngRoutesSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesSelected.setStatus("current")
_SleRIPngRoutesIfName_Type = OctetString
_SleRIPngRoutesIfName_Object = MibTableColumn
sleRIPngRoutesIfName = _SleRIPngRoutesIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 6),
    _SleRIPngRoutesIfName_Type()
)
sleRIPngRoutesIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesIfName.setStatus("current")


class _SleRIPngRoutesMetric_Type(Integer32):
    """Custom type sleRIPngRoutesMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRIPngRoutesMetric_Type.__name__ = "Integer32"
_SleRIPngRoutesMetric_Object = MibTableColumn
sleRIPngRoutesMetric = _SleRIPngRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 7),
    _SleRIPngRoutesMetric_Type()
)
sleRIPngRoutesMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesMetric.setStatus("current")


class _SleRIPngRoutesTag_Type(Integer32):
    """Custom type sleRIPngRoutesTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRIPngRoutesTag_Type.__name__ = "Integer32"
_SleRIPngRoutesTag_Object = MibTableColumn
sleRIPngRoutesTag = _SleRIPngRoutesTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 8),
    _SleRIPngRoutesTag_Type()
)
sleRIPngRoutesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesTag.setStatus("current")
_SleRIPngRoutesUpTime_Type = TimeTicks
_SleRIPngRoutesUpTime_Object = MibTableColumn
sleRIPngRoutesUpTime = _SleRIPngRoutesUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 12, 1, 1, 9),
    _SleRIPngRoutesUpTime_Type()
)
sleRIPngRoutesUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPngRoutesUpTime.setStatus("current")

# Managed Objects groups

sleRIPngGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 13)
)
sleRIPngGroup.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDefaultMetric"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultInformationOrg"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultDistance"),
        ("SLE-RIPng-MIB", "sleRIPngRecvBufferSize"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPaths"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPrefixRoute"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPrefixRoutePercent"),
        ("SLE-RIPng-MIB", "sleRIPngMetricSumApply"),
        ("SLE-RIPng-MIB", "sleRIPngBasicUpdateTimer"),
        ("SLE-RIPng-MIB", "sleRIPngBasicTimeoutTimer"),
        ("SLE-RIPng-MIB", "sleRIPngBasicGarbageTimer"),
        ("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngControlDefaultMetric"),
        ("SLE-RIPng-MIB", "sleRIPngControlDefaultInformationOrg"),
        ("SLE-RIPng-MIB", "sleRIPngControlDefaultDistance"),
        ("SLE-RIPng-MIB", "sleRIPngControlRecvBufferSize"),
        ("SLE-RIPng-MIB", "sleRIPngControlMaximumPaths"),
        ("SLE-RIPng-MIB", "sleRIPngControlMaximumPrefixRoute"),
        ("SLE-RIPng-MIB", "sleRIPngControlMaximumPrefixRoutePercent"),
        ("SLE-RIPng-MIB", "sleRIPngControlMetricSumApply"),
        ("SLE-RIPng-MIB", "sleRIPngControlBasicUpdateTimer"),
        ("SLE-RIPng-MIB", "sleRIPngControlBasicTimeoutTimer"),
        ("SLE-RIPng-MIB", "sleRIPngControlBasicGarbageTimer"),
        ("SLE-RIPng-MIB", "sleRIPngControlClearRoutePrefix"),
        ("SLE-RIPng-MIB", "sleRIPngControlClearRouteMask"),
        ("SLE-RIPng-MIB", "sleRIPngControlClearProtoTpye"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateMask"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlMask"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborAddr"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborIfName"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlIfName"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteAddr"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteMask"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlMask"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceValue"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceMask"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceAccessName"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlValue"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlMask"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlAccessName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInAccessName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutAccessName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInPrefixName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutPrefixName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlInAccessName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlOutAccessName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlInPrefixName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlOutPrefixName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListIfname"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListInAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListInMetric"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListOutAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListOutMetric"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlIfname"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlInAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlInMetric"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlOutAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlOutMetric"),
        ("SLE-RIPng-MIB", "sleRIPngRedistType"),
        ("SLE-RIPng-MIB", "sleRIPngRedistMetric"),
        ("SLE-RIPng-MIB", "sleRIPngRedistRouteMapName"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlType"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlMetric"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlRouteMapName"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapName"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapType"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapIfname"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlName"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlType"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlIfname"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceName"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlName"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceIndex"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceRouterMode"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceRecvPacket"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceSendPacket"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceSplitHorizonMode"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlStatus"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlTimer"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlIndex"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlRouterMode"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlRecvPacket"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlSendPacket"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlSplitHorizonMode"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesType"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesPrefix"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesMask"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesNextHop"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesSelected"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesIfName"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesMetric"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesTag"),
        ("SLE-RIPng-MIB", "sleRIPngRoutesUpTime"))
)
if mibBuilder.loadTexts:
    sleRIPngGroup.setStatus("current")


# Notification objects

sleRIPngModeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 1)
)
sleRIPngModeCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRIPngModeCreated.setStatus(
        "current"
    )

sleRIPngModeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 2)
)
sleRIPngModeDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRIPngModeDeleted.setStatus(
        "current"
    )

sleRIPngDefaultMetricChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 3)
)
sleRIPngDefaultMetricChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultMetric"))
)
if mibBuilder.loadTexts:
    sleRIPngDefaultMetricChanged.setStatus(
        "current"
    )

sleRIPngDefaultInformationOrgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 4)
)
sleRIPngDefaultInformationOrgChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultInformationOrg"))
)
if mibBuilder.loadTexts:
    sleRIPngDefaultInformationOrgChanged.setStatus(
        "current"
    )

sleRIPngDefaultDistanceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 5)
)
sleRIPngDefaultDistanceChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultDistance"))
)
if mibBuilder.loadTexts:
    sleRIPngDefaultDistanceChanged.setStatus(
        "current"
    )

sleRIPngRecvBufferSizeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 6)
)
sleRIPngRecvBufferSizeChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRecvBufferSize"))
)
if mibBuilder.loadTexts:
    sleRIPngRecvBufferSizeChanged.setStatus(
        "current"
    )

sleRIPngMaximumPathsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 7)
)
sleRIPngMaximumPathsChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPaths"))
)
if mibBuilder.loadTexts:
    sleRIPngMaximumPathsChanged.setStatus(
        "current"
    )

sleRIPngMaximumPrefixProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 8)
)
sleRIPngMaximumPrefixProfileChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPrefixRoute"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPrefixRoutePercent"))
)
if mibBuilder.loadTexts:
    sleRIPngMaximumPrefixProfileChanged.setStatus(
        "current"
    )

sleRIPngMetricSumApplyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 9)
)
sleRIPngMetricSumApplyChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngMetricSumApply"))
)
if mibBuilder.loadTexts:
    sleRIPngMetricSumApplyChanged.setStatus(
        "current"
    )

sleRIPngTimersChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 10)
)
sleRIPngTimersChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngBasicUpdateTimer"),
        ("SLE-RIPng-MIB", "sleRIPngBasicTimeoutTimer"),
        ("SLE-RIPng-MIB", "sleRIPngBasicGarbageTimer"))
)
if mibBuilder.loadTexts:
    sleRIPngTimersChanged.setStatus(
        "current"
    )

sleRIPngAllCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 11)
)
sleRIPngAllCleared.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRIPngAllCleared.setStatus(
        "current"
    )

sleRIPngRouteCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 12)
)
sleRIPngRouteCleared.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngControlClearRoutePrefix"),
        ("SLE-RIPng-MIB", "sleRIPngControlClearRouteMask"))
)
if mibBuilder.loadTexts:
    sleRIPngRouteCleared.setStatus(
        "current"
    )

sleRIPngProtoTypeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 1, 3, 13)
)
sleRIPngProtoTypeCleared.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngControlClearProtoTpye"))
)
if mibBuilder.loadTexts:
    sleRIPngProtoTypeCleared.setStatus(
        "current"
    )

sleRIPngAggregateAddrCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 3, 1)
)
sleRIPngAggregateAddrCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngAggregateControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateMask"))
)
if mibBuilder.loadTexts:
    sleRIPngAggregateAddrCreated.setStatus(
        "current"
    )

sleRIPngAggregateAddrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 2, 3, 2)
)
sleRIPngAggregateAddrDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngAggregateControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateControlMask"))
)
if mibBuilder.loadTexts:
    sleRIPngAggregateAddrDeleted.setStatus(
        "current"
    )

sleRIPngNeighborCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 3, 1)
)
sleRIPngNeighborCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngNeighborControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborAddr"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborIfName"))
)
if mibBuilder.loadTexts:
    sleRIPngNeighborCreated.setStatus(
        "current"
    )

sleRIPngNeighborDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 3, 3, 2)
)
sleRIPngNeighborDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngNeighborControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborControlIfName"))
)
if mibBuilder.loadTexts:
    sleRIPngNeighborDeleted.setStatus(
        "current"
    )

sleRIPngStaticRouteCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 3, 1)
)
sleRIPngStaticRouteCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngStaticRouteControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteAddr"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteMask"))
)
if mibBuilder.loadTexts:
    sleRIPngStaticRouteCreated.setStatus(
        "current"
    )

sleRIPngStaticRouteDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 4, 3, 2)
)
sleRIPngStaticRouteDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngStaticRouteControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteControlMask"))
)
if mibBuilder.loadTexts:
    sleRIPngStaticRouteDeleted.setStatus(
        "current"
    )

sleRIPngAdminDistanceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 3, 1)
)
sleRIPngAdminDistanceCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceValue"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceMask"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceCreated.setStatus(
        "current"
    )

sleRIPngAdminDistanceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 5, 3, 2)
)
sleRIPngAdminDistanceDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlValue"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlAddr"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlMask"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceControlAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPngAdminDistanceDeleted.setStatus(
        "current"
    )

sleRIPngDistributeInAccessCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 1)
)
sleRIPngDistributeInAccessCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeInAccessCreated.setStatus(
        "current"
    )

sleRIPngDistributeInAccessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 2)
)
sleRIPngDistributeInAccessDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlInAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeInAccessDeleted.setStatus(
        "current"
    )

sleRIPngDistributeOutAccessCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 3)
)
sleRIPngDistributeOutAccessCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeOutAccessCreated.setStatus(
        "current"
    )

sleRIPngDistributeOutAccessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 4)
)
sleRIPngDistributeOutAccessDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlOutAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeOutAccessDeleted.setStatus(
        "current"
    )

sleRIPngDistributeInPrefixCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 5)
)
sleRIPngDistributeInPrefixCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeInPrefixCreated.setStatus(
        "current"
    )

sleRIPngDistributeInPrefixDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 6)
)
sleRIPngDistributeInPrefixDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlInPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeInPrefixDeleted.setStatus(
        "current"
    )

sleRIPngDistributeOutPrefixCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 7)
)
sleRIPngDistributeOutPrefixCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeOutPrefixCreated.setStatus(
        "current"
    )

sleRIPngDistributeOutPrefixDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 6, 3, 8)
)
sleRIPngDistributeOutPrefixDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngDistributeControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlIfName"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeControlOutPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPngDistributeOutPrefixDeleted.setStatus(
        "current"
    )

sleRIPngOffsetListInCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 3, 1)
)
sleRIPngOffsetListInCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngOffsetListControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListIfname"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListInAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListInMetric"))
)
if mibBuilder.loadTexts:
    sleRIPngOffsetListInCreated.setStatus(
        "current"
    )

sleRIPngOffsetListInDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 3, 2)
)
sleRIPngOffsetListInDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngOffsetListControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlIfname"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlInAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlInMetric"))
)
if mibBuilder.loadTexts:
    sleRIPngOffsetListInDeleted.setStatus(
        "current"
    )

sleRIPngOffsetListOutCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 3, 3)
)
sleRIPngOffsetListOutCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngOffsetListControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListIfname"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListOutAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListOutMetric"))
)
if mibBuilder.loadTexts:
    sleRIPngOffsetListOutCreated.setStatus(
        "current"
    )

sleRIPngOffsetListOutDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 7, 3, 4)
)
sleRIPngOffsetListOutDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngOffsetListControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlIfname"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlOutAccName"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListControlOutMetric"))
)
if mibBuilder.loadTexts:
    sleRIPngOffsetListOutDeleted.setStatus(
        "current"
    )

sleRIPngRedistributeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 3, 1)
)
sleRIPngRedistributeCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngRedistControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRedistType"),
        ("SLE-RIPng-MIB", "sleRIPngRedistMetric"),
        ("SLE-RIPng-MIB", "sleRIPngRedistRouteMapName"))
)
if mibBuilder.loadTexts:
    sleRIPngRedistributeCreated.setStatus(
        "current"
    )

sleRIPngRedistributeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 3, 2)
)
sleRIPngRedistributeDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngRedistControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlType"))
)
if mibBuilder.loadTexts:
    sleRIPngRedistributeDeleted.setStatus(
        "current"
    )

sleRIPngRedistributeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 8, 3, 3)
)
sleRIPngRedistributeChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngRedistControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngRedistControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRedistType"),
        ("SLE-RIPng-MIB", "sleRIPngRedistMetric"),
        ("SLE-RIPng-MIB", "sleRIPngRedistRouteMapName"))
)
if mibBuilder.loadTexts:
    sleRIPngRedistributeChanged.setStatus(
        "current"
    )

sleRIPngRoutemapCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 3, 1)
)
sleRIPngRoutemapCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngRoutemapControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapName"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapType"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapIfname"))
)
if mibBuilder.loadTexts:
    sleRIPngRoutemapCreated.setStatus(
        "current"
    )

sleRIPngRoutemapDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 9, 3, 2)
)
sleRIPngRoutemapDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngRoutemapControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlName"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlType"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapControlIfname"))
)
if mibBuilder.loadTexts:
    sleRIPngRoutemapDeleted.setStatus(
        "current"
    )

sleRIPngPassInterfaceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 3, 1)
)
sleRIPngPassInterfaceCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceName"))
)
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceCreated.setStatus(
        "current"
    )

sleRIPngPassInterfaceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 10, 3, 2)
)
sleRIPngPassInterfaceDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceControlName"))
)
if mibBuilder.loadTexts:
    sleRIPngPassInterfaceDeleted.setStatus(
        "current"
    )

sleRIPngInterfaceRouterModeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 3, 1)
)
sleRIPngInterfaceRouterModeCreated.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceIndex"))
)
if mibBuilder.loadTexts:
    sleRIPngInterfaceRouterModeCreated.setStatus(
        "current"
    )

sleRIPngInterfaceRouterModeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 3, 2)
)
sleRIPngInterfaceRouterModeDeleted.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceIndex"))
)
if mibBuilder.loadTexts:
    sleRIPngInterfaceRouterModeDeleted.setStatus(
        "current"
    )

sleRIPngInterfaceRecvPacketChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 3, 3)
)
sleRIPngInterfaceRecvPacketChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceIndex"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceRecvPacket"))
)
if mibBuilder.loadTexts:
    sleRIPngInterfaceRecvPacketChanged.setStatus(
        "current"
    )

sleRIPngInterfaceSendPacketChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 3, 4)
)
sleRIPngInterfaceSendPacketChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceIndex"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceSendPacket"))
)
if mibBuilder.loadTexts:
    sleRIPngInterfaceSendPacketChanged.setStatus(
        "current"
    )

sleRIPngInterfaceSplitHorizonModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 11, 3, 5)
)
sleRIPngInterfaceSplitHorizonModeChanged.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngInterfaceControlRequest"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlTimeStamp"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceControlReqResult"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceIndex"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceSplitHorizonMode"))
)
if mibBuilder.loadTexts:
    sleRIPngInterfaceSplitHorizonModeChanged.setStatus(
        "current"
    )


# Notifications groups

sleRIPngNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 55, 14)
)
sleRIPngNotificationGroup.setObjects(
      *(("SLE-RIPng-MIB", "sleRIPngModeCreated"),
        ("SLE-RIPng-MIB", "sleRIPngModeDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultMetricChanged"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultInformationOrgChanged"),
        ("SLE-RIPng-MIB", "sleRIPngDefaultDistanceChanged"),
        ("SLE-RIPng-MIB", "sleRIPngRecvBufferSizeChanged"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPathsChanged"),
        ("SLE-RIPng-MIB", "sleRIPngMaximumPrefixProfileChanged"),
        ("SLE-RIPng-MIB", "sleRIPngMetricSumApplyChanged"),
        ("SLE-RIPng-MIB", "sleRIPngTimersChanged"),
        ("SLE-RIPng-MIB", "sleRIPngAllCleared"),
        ("SLE-RIPng-MIB", "sleRIPngRouteCleared"),
        ("SLE-RIPng-MIB", "sleRIPngProtoTypeCleared"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateAddrCreated"),
        ("SLE-RIPng-MIB", "sleRIPngAggregateAddrDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborCreated"),
        ("SLE-RIPng-MIB", "sleRIPngNeighborDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteCreated"),
        ("SLE-RIPng-MIB", "sleRIPngStaticRouteDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceCreated"),
        ("SLE-RIPng-MIB", "sleRIPngAdminDistanceDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInAccessCreated"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInAccessDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutAccessCreated"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutAccessDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInPrefixCreated"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeInPrefixDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutPrefixCreated"),
        ("SLE-RIPng-MIB", "sleRIPngDistributeOutPrefixDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListInCreated"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListInDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListOutCreated"),
        ("SLE-RIPng-MIB", "sleRIPngOffsetListOutDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngRedistributeCreated"),
        ("SLE-RIPng-MIB", "sleRIPngRedistributeDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngRedistributeChanged"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapCreated"),
        ("SLE-RIPng-MIB", "sleRIPngRoutemapDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceCreated"),
        ("SLE-RIPng-MIB", "sleRIPngPassInterfaceDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceRouterModeCreated"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceRouterModeDeleted"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceRecvPacketChanged"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceSendPacketChanged"),
        ("SLE-RIPng-MIB", "sleRIPngInterfaceSplitHorizonModeChanged"))
)
if mibBuilder.loadTexts:
    sleRIPngNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-RIPng-MIB",
    **{"sleRIPng": sleRIPng,
       "sleRIPngBase": sleRIPngBase,
       "sleRIPngBaseInfo": sleRIPngBaseInfo,
       "sleRIPngDefaultMetric": sleRIPngDefaultMetric,
       "sleRIPngDefaultInformationOrg": sleRIPngDefaultInformationOrg,
       "sleRIPngDefaultDistance": sleRIPngDefaultDistance,
       "sleRIPngRecvBufferSize": sleRIPngRecvBufferSize,
       "sleRIPngMaximumPaths": sleRIPngMaximumPaths,
       "sleRIPngMaximumPrefixRoute": sleRIPngMaximumPrefixRoute,
       "sleRIPngMaximumPrefixRoutePercent": sleRIPngMaximumPrefixRoutePercent,
       "sleRIPngMetricSumApply": sleRIPngMetricSumApply,
       "sleRIPngBasicUpdateTimer": sleRIPngBasicUpdateTimer,
       "sleRIPngBasicTimeoutTimer": sleRIPngBasicTimeoutTimer,
       "sleRIPngBasicGarbageTimer": sleRIPngBasicGarbageTimer,
       "sleRIPngBaseControl": sleRIPngBaseControl,
       "sleRIPngControlRequest": sleRIPngControlRequest,
       "sleRIPngControlStatus": sleRIPngControlStatus,
       "sleRIPngControlTimer": sleRIPngControlTimer,
       "sleRIPngControlTimeStamp": sleRIPngControlTimeStamp,
       "sleRIPngControlReqResult": sleRIPngControlReqResult,
       "sleRIPngControlDefaultMetric": sleRIPngControlDefaultMetric,
       "sleRIPngControlDefaultInformationOrg": sleRIPngControlDefaultInformationOrg,
       "sleRIPngControlDefaultDistance": sleRIPngControlDefaultDistance,
       "sleRIPngControlRecvBufferSize": sleRIPngControlRecvBufferSize,
       "sleRIPngControlMaximumPaths": sleRIPngControlMaximumPaths,
       "sleRIPngControlMaximumPrefixRoute": sleRIPngControlMaximumPrefixRoute,
       "sleRIPngControlMaximumPrefixRoutePercent": sleRIPngControlMaximumPrefixRoutePercent,
       "sleRIPngControlMetricSumApply": sleRIPngControlMetricSumApply,
       "sleRIPngControlBasicUpdateTimer": sleRIPngControlBasicUpdateTimer,
       "sleRIPngControlBasicTimeoutTimer": sleRIPngControlBasicTimeoutTimer,
       "sleRIPngControlBasicGarbageTimer": sleRIPngControlBasicGarbageTimer,
       "sleRIPngControlClearRoutePrefix": sleRIPngControlClearRoutePrefix,
       "sleRIPngControlClearRouteMask": sleRIPngControlClearRouteMask,
       "sleRIPngControlClearProtoTpye": sleRIPngControlClearProtoTpye,
       "sleRIPngBaseNotification": sleRIPngBaseNotification,
       "sleRIPngModeCreated": sleRIPngModeCreated,
       "sleRIPngModeDeleted": sleRIPngModeDeleted,
       "sleRIPngDefaultMetricChanged": sleRIPngDefaultMetricChanged,
       "sleRIPngDefaultInformationOrgChanged": sleRIPngDefaultInformationOrgChanged,
       "sleRIPngDefaultDistanceChanged": sleRIPngDefaultDistanceChanged,
       "sleRIPngRecvBufferSizeChanged": sleRIPngRecvBufferSizeChanged,
       "sleRIPngMaximumPathsChanged": sleRIPngMaximumPathsChanged,
       "sleRIPngMaximumPrefixProfileChanged": sleRIPngMaximumPrefixProfileChanged,
       "sleRIPngMetricSumApplyChanged": sleRIPngMetricSumApplyChanged,
       "sleRIPngTimersChanged": sleRIPngTimersChanged,
       "sleRIPngAllCleared": sleRIPngAllCleared,
       "sleRIPngRouteCleared": sleRIPngRouteCleared,
       "sleRIPngProtoTypeCleared": sleRIPngProtoTypeCleared,
       "sleRIPngAggregate": sleRIPngAggregate,
       "sleRIPngAggregateTable": sleRIPngAggregateTable,
       "sleRIPngAggregateEntry": sleRIPngAggregateEntry,
       "sleRIPngAggregateAddr": sleRIPngAggregateAddr,
       "sleRIPngAggregateMask": sleRIPngAggregateMask,
       "sleRIPngAggregateControl": sleRIPngAggregateControl,
       "sleRIPngAggregateControlRequest": sleRIPngAggregateControlRequest,
       "sleRIPngAggregateControlStatus": sleRIPngAggregateControlStatus,
       "sleRIPngAggregateControlTimer": sleRIPngAggregateControlTimer,
       "sleRIPngAggregateControlTimeStamp": sleRIPngAggregateControlTimeStamp,
       "sleRIPngAggregateControlReqResult": sleRIPngAggregateControlReqResult,
       "sleRIPngAggregateControlAddr": sleRIPngAggregateControlAddr,
       "sleRIPngAggregateControlMask": sleRIPngAggregateControlMask,
       "sleRIPngAggregateNotification": sleRIPngAggregateNotification,
       "sleRIPngAggregateAddrCreated": sleRIPngAggregateAddrCreated,
       "sleRIPngAggregateAddrDeleted": sleRIPngAggregateAddrDeleted,
       "sleRIPngNeighbor": sleRIPngNeighbor,
       "sleRIPngNeighborTable": sleRIPngNeighborTable,
       "sleRIPngNeighborEntry": sleRIPngNeighborEntry,
       "sleRIPngNeighborAddr": sleRIPngNeighborAddr,
       "sleRIPngNeighborIfName": sleRIPngNeighborIfName,
       "sleRIPngNeighborControl": sleRIPngNeighborControl,
       "sleRIPngNeighborControlRequest": sleRIPngNeighborControlRequest,
       "sleRIPngNeighborControlStatus": sleRIPngNeighborControlStatus,
       "sleRIPngNeighborControlTimer": sleRIPngNeighborControlTimer,
       "sleRIPngNeighborControlTimeStamp": sleRIPngNeighborControlTimeStamp,
       "sleRIPngNeighborControlReqResult": sleRIPngNeighborControlReqResult,
       "sleRIPngNeighborControlAddr": sleRIPngNeighborControlAddr,
       "sleRIPngNeighborControlIfName": sleRIPngNeighborControlIfName,
       "sleRIPngNeighborNotification": sleRIPngNeighborNotification,
       "sleRIPngNeighborCreated": sleRIPngNeighborCreated,
       "sleRIPngNeighborDeleted": sleRIPngNeighborDeleted,
       "sleRIPngStaticRoute": sleRIPngStaticRoute,
       "sleRIPngStaticRouteTable": sleRIPngStaticRouteTable,
       "sleRIPngStaticRouteEntry": sleRIPngStaticRouteEntry,
       "sleRIPngStaticRouteAddr": sleRIPngStaticRouteAddr,
       "sleRIPngStaticRouteMask": sleRIPngStaticRouteMask,
       "sleRIPngStaticRouteControl": sleRIPngStaticRouteControl,
       "sleRIPngStaticRouteControlRequest": sleRIPngStaticRouteControlRequest,
       "sleRIPngStaticRouteControlStatus": sleRIPngStaticRouteControlStatus,
       "sleRIPngStaticRouteControlTimer": sleRIPngStaticRouteControlTimer,
       "sleRIPngStaticRouteControlTimeStamp": sleRIPngStaticRouteControlTimeStamp,
       "sleRIPngStaticRouteControlReqResult": sleRIPngStaticRouteControlReqResult,
       "sleRIPngStaticRouteControlAddr": sleRIPngStaticRouteControlAddr,
       "sleRIPngStaticRouteControlMask": sleRIPngStaticRouteControlMask,
       "sleRIPngStaticRouteNotification": sleRIPngStaticRouteNotification,
       "sleRIPngStaticRouteCreated": sleRIPngStaticRouteCreated,
       "sleRIPngStaticRouteDeleted": sleRIPngStaticRouteDeleted,
       "sleRIPngAdminDistance": sleRIPngAdminDistance,
       "sleRIPngAdminDistanceTable": sleRIPngAdminDistanceTable,
       "sleRIPngAdminDistanceEntry": sleRIPngAdminDistanceEntry,
       "sleRIPngAdminDistanceValue": sleRIPngAdminDistanceValue,
       "sleRIPngAdminDistanceAddr": sleRIPngAdminDistanceAddr,
       "sleRIPngAdminDistanceMask": sleRIPngAdminDistanceMask,
       "sleRIPngAdminDistanceAccessName": sleRIPngAdminDistanceAccessName,
       "sleRIPngAdminDistanceControl": sleRIPngAdminDistanceControl,
       "sleRIPngAdminDistanceControlRequest": sleRIPngAdminDistanceControlRequest,
       "sleRIPngAdminDistanceControlStatus": sleRIPngAdminDistanceControlStatus,
       "sleRIPngAdminDistanceControlTimer": sleRIPngAdminDistanceControlTimer,
       "sleRIPngAdminDistanceControlTimeStamp": sleRIPngAdminDistanceControlTimeStamp,
       "sleRIPngAdminDistanceControlReqResult": sleRIPngAdminDistanceControlReqResult,
       "sleRIPngAdminDistanceControlValue": sleRIPngAdminDistanceControlValue,
       "sleRIPngAdminDistanceControlAddr": sleRIPngAdminDistanceControlAddr,
       "sleRIPngAdminDistanceControlMask": sleRIPngAdminDistanceControlMask,
       "sleRIPngAdminDistanceControlAccessName": sleRIPngAdminDistanceControlAccessName,
       "sleRIPngAdminDistanceNotification": sleRIPngAdminDistanceNotification,
       "sleRIPngAdminDistanceCreated": sleRIPngAdminDistanceCreated,
       "sleRIPngAdminDistanceDeleted": sleRIPngAdminDistanceDeleted,
       "sleRIPngDistribute": sleRIPngDistribute,
       "sleRIPngDistributeTable": sleRIPngDistributeTable,
       "sleRIPngDistributeEntry": sleRIPngDistributeEntry,
       "sleRIPngDistributeIfName": sleRIPngDistributeIfName,
       "sleRIPngDistributeInAccessName": sleRIPngDistributeInAccessName,
       "sleRIPngDistributeOutAccessName": sleRIPngDistributeOutAccessName,
       "sleRIPngDistributeInPrefixName": sleRIPngDistributeInPrefixName,
       "sleRIPngDistributeOutPrefixName": sleRIPngDistributeOutPrefixName,
       "sleRIPngDistributeControl": sleRIPngDistributeControl,
       "sleRIPngDistributeControlRequest": sleRIPngDistributeControlRequest,
       "sleRIPngDistributeControlStatus": sleRIPngDistributeControlStatus,
       "sleRIPngDistributeControlTimer": sleRIPngDistributeControlTimer,
       "sleRIPngDistributeControlTimeStamp": sleRIPngDistributeControlTimeStamp,
       "sleRIPngDistributeControlReqResult": sleRIPngDistributeControlReqResult,
       "sleRIPngDistributeControlIfName": sleRIPngDistributeControlIfName,
       "sleRIPngDistributeControlInAccessName": sleRIPngDistributeControlInAccessName,
       "sleRIPngDistributeControlOutAccessName": sleRIPngDistributeControlOutAccessName,
       "sleRIPngDistributeControlInPrefixName": sleRIPngDistributeControlInPrefixName,
       "sleRIPngDistributeControlOutPrefixName": sleRIPngDistributeControlOutPrefixName,
       "sleRIPngDistributeNotification": sleRIPngDistributeNotification,
       "sleRIPngDistributeInAccessCreated": sleRIPngDistributeInAccessCreated,
       "sleRIPngDistributeInAccessDeleted": sleRIPngDistributeInAccessDeleted,
       "sleRIPngDistributeOutAccessCreated": sleRIPngDistributeOutAccessCreated,
       "sleRIPngDistributeOutAccessDeleted": sleRIPngDistributeOutAccessDeleted,
       "sleRIPngDistributeInPrefixCreated": sleRIPngDistributeInPrefixCreated,
       "sleRIPngDistributeInPrefixDeleted": sleRIPngDistributeInPrefixDeleted,
       "sleRIPngDistributeOutPrefixCreated": sleRIPngDistributeOutPrefixCreated,
       "sleRIPngDistributeOutPrefixDeleted": sleRIPngDistributeOutPrefixDeleted,
       "sleRIPngOffsetList": sleRIPngOffsetList,
       "sleRIPngOffsetListTable": sleRIPngOffsetListTable,
       "sleRIPngOffsetListEntry": sleRIPngOffsetListEntry,
       "sleRIPngOffsetListIfname": sleRIPngOffsetListIfname,
       "sleRIPngOffsetListInAccName": sleRIPngOffsetListInAccName,
       "sleRIPngOffsetListInMetric": sleRIPngOffsetListInMetric,
       "sleRIPngOffsetListOutAccName": sleRIPngOffsetListOutAccName,
       "sleRIPngOffsetListOutMetric": sleRIPngOffsetListOutMetric,
       "sleRIPngOffsetListControl": sleRIPngOffsetListControl,
       "sleRIPngOffsetListControlRequest": sleRIPngOffsetListControlRequest,
       "sleRIPngOffsetListControlStatus": sleRIPngOffsetListControlStatus,
       "sleRIPngOffsetListControlTimer": sleRIPngOffsetListControlTimer,
       "sleRIPngOffsetListControlTimeStamp": sleRIPngOffsetListControlTimeStamp,
       "sleRIPngOffsetListControlReqResult": sleRIPngOffsetListControlReqResult,
       "sleRIPngOffsetListControlIfname": sleRIPngOffsetListControlIfname,
       "sleRIPngOffsetListControlInAccName": sleRIPngOffsetListControlInAccName,
       "sleRIPngOffsetListControlInMetric": sleRIPngOffsetListControlInMetric,
       "sleRIPngOffsetListControlOutAccName": sleRIPngOffsetListControlOutAccName,
       "sleRIPngOffsetListControlOutMetric": sleRIPngOffsetListControlOutMetric,
       "sleRIPngOffsetListNotification": sleRIPngOffsetListNotification,
       "sleRIPngOffsetListInCreated": sleRIPngOffsetListInCreated,
       "sleRIPngOffsetListInDeleted": sleRIPngOffsetListInDeleted,
       "sleRIPngOffsetListOutCreated": sleRIPngOffsetListOutCreated,
       "sleRIPngOffsetListOutDeleted": sleRIPngOffsetListOutDeleted,
       "sleRIPngRedistribute": sleRIPngRedistribute,
       "sleRIPngRedistributeTable": sleRIPngRedistributeTable,
       "sleRIPngRedistributeEntry": sleRIPngRedistributeEntry,
       "sleRIPngRedistType": sleRIPngRedistType,
       "sleRIPngRedistMetric": sleRIPngRedistMetric,
       "sleRIPngRedistRouteMapName": sleRIPngRedistRouteMapName,
       "sleRIPngRedistributeControl": sleRIPngRedistributeControl,
       "sleRIPngRedistControlRequest": sleRIPngRedistControlRequest,
       "sleRIPngRedistControlStatus": sleRIPngRedistControlStatus,
       "sleRIPngRedistControlTimer": sleRIPngRedistControlTimer,
       "sleRIPngRedistControlTimeStamp": sleRIPngRedistControlTimeStamp,
       "sleRIPngRedistControlReqResult": sleRIPngRedistControlReqResult,
       "sleRIPngRedistControlType": sleRIPngRedistControlType,
       "sleRIPngRedistControlMetric": sleRIPngRedistControlMetric,
       "sleRIPngRedistControlRouteMapName": sleRIPngRedistControlRouteMapName,
       "sleRIPngRedistributeNotification": sleRIPngRedistributeNotification,
       "sleRIPngRedistributeCreated": sleRIPngRedistributeCreated,
       "sleRIPngRedistributeDeleted": sleRIPngRedistributeDeleted,
       "sleRIPngRedistributeChanged": sleRIPngRedistributeChanged,
       "sleRIPngRoutemap": sleRIPngRoutemap,
       "sleRIPngRoutemapTable": sleRIPngRoutemapTable,
       "sleRIPngRoutemapEntry": sleRIPngRoutemapEntry,
       "sleRIPngRoutemapName": sleRIPngRoutemapName,
       "sleRIPngRoutemapType": sleRIPngRoutemapType,
       "sleRIPngRoutemapIfname": sleRIPngRoutemapIfname,
       "sleRIPngRoutemapControl": sleRIPngRoutemapControl,
       "sleRIPngRoutemapControlRequest": sleRIPngRoutemapControlRequest,
       "sleRIPngRoutemapControlStatus": sleRIPngRoutemapControlStatus,
       "sleRIPngRoutemapControlTimer": sleRIPngRoutemapControlTimer,
       "sleRIPngRoutemapControlTimeStamp": sleRIPngRoutemapControlTimeStamp,
       "sleRIPngRoutemapControlReqResult": sleRIPngRoutemapControlReqResult,
       "sleRIPngRoutemapControlName": sleRIPngRoutemapControlName,
       "sleRIPngRoutemapControlType": sleRIPngRoutemapControlType,
       "sleRIPngRoutemapControlIfname": sleRIPngRoutemapControlIfname,
       "sleRIPngRoutemapNotification": sleRIPngRoutemapNotification,
       "sleRIPngRoutemapCreated": sleRIPngRoutemapCreated,
       "sleRIPngRoutemapDeleted": sleRIPngRoutemapDeleted,
       "sleRIPngPassInterface": sleRIPngPassInterface,
       "sleRIPngPassInterfaceTable": sleRIPngPassInterfaceTable,
       "sleRIPngPassInterfaceEntry": sleRIPngPassInterfaceEntry,
       "sleRIPngPassInterfaceName": sleRIPngPassInterfaceName,
       "sleRIPngPassInterfaceControl": sleRIPngPassInterfaceControl,
       "sleRIPngPassInterfaceControlRequest": sleRIPngPassInterfaceControlRequest,
       "sleRIPngPassInterfaceControlStatus": sleRIPngPassInterfaceControlStatus,
       "sleRIPngPassInterfaceControlTimer": sleRIPngPassInterfaceControlTimer,
       "sleRIPngPassInterfaceControlTimeStamp": sleRIPngPassInterfaceControlTimeStamp,
       "sleRIPngPassInterfaceControlReqResult": sleRIPngPassInterfaceControlReqResult,
       "sleRIPngPassInterfaceControlName": sleRIPngPassInterfaceControlName,
       "sleRIPngPassInterfaceNotification": sleRIPngPassInterfaceNotification,
       "sleRIPngPassInterfaceCreated": sleRIPngPassInterfaceCreated,
       "sleRIPngPassInterfaceDeleted": sleRIPngPassInterfaceDeleted,
       "sleRIPngInterface": sleRIPngInterface,
       "sleRIPngInterfaceTable": sleRIPngInterfaceTable,
       "sleRIPngInterfaceEntry": sleRIPngInterfaceEntry,
       "sleRIPngInterfaceIndex": sleRIPngInterfaceIndex,
       "sleRIPngInterfaceRouterMode": sleRIPngInterfaceRouterMode,
       "sleRIPngInterfaceRecvPacket": sleRIPngInterfaceRecvPacket,
       "sleRIPngInterfaceSendPacket": sleRIPngInterfaceSendPacket,
       "sleRIPngInterfaceSplitHorizonMode": sleRIPngInterfaceSplitHorizonMode,
       "sleRIPngInterfaceControl": sleRIPngInterfaceControl,
       "sleRIPngInterfaceControlRequest": sleRIPngInterfaceControlRequest,
       "sleRIPngInterfaceControlStatus": sleRIPngInterfaceControlStatus,
       "sleRIPngInterfaceControlTimer": sleRIPngInterfaceControlTimer,
       "sleRIPngInterfaceControlTimeStamp": sleRIPngInterfaceControlTimeStamp,
       "sleRIPngInterfaceControlReqResult": sleRIPngInterfaceControlReqResult,
       "sleRIPngInterfaceControlIndex": sleRIPngInterfaceControlIndex,
       "sleRIPngInterfaceControlRouterMode": sleRIPngInterfaceControlRouterMode,
       "sleRIPngInterfaceControlRecvPacket": sleRIPngInterfaceControlRecvPacket,
       "sleRIPngInterfaceControlSendPacket": sleRIPngInterfaceControlSendPacket,
       "sleRIPngInterfaceControlSplitHorizonMode": sleRIPngInterfaceControlSplitHorizonMode,
       "sleRIPngInterfaceNotification": sleRIPngInterfaceNotification,
       "sleRIPngInterfaceRouterModeCreated": sleRIPngInterfaceRouterModeCreated,
       "sleRIPngInterfaceRouterModeDeleted": sleRIPngInterfaceRouterModeDeleted,
       "sleRIPngInterfaceRecvPacketChanged": sleRIPngInterfaceRecvPacketChanged,
       "sleRIPngInterfaceSendPacketChanged": sleRIPngInterfaceSendPacketChanged,
       "sleRIPngInterfaceSplitHorizonModeChanged": sleRIPngInterfaceSplitHorizonModeChanged,
       "sleRIPngRoutes": sleRIPngRoutes,
       "sleRIPngRoutesTable": sleRIPngRoutesTable,
       "sleRIPngRoutesEntry": sleRIPngRoutesEntry,
       "sleRIPngRoutesType": sleRIPngRoutesType,
       "sleRIPngRoutesPrefix": sleRIPngRoutesPrefix,
       "sleRIPngRoutesMask": sleRIPngRoutesMask,
       "sleRIPngRoutesNextHop": sleRIPngRoutesNextHop,
       "sleRIPngRoutesSelected": sleRIPngRoutesSelected,
       "sleRIPngRoutesIfName": sleRIPngRoutesIfName,
       "sleRIPngRoutesMetric": sleRIPngRoutesMetric,
       "sleRIPngRoutesTag": sleRIPngRoutesTag,
       "sleRIPngRoutesUpTime": sleRIPngRoutesUpTime,
       "sleRIPngGroup": sleRIPngGroup,
       "sleRIPngNotificationGroup": sleRIPngNotificationGroup}
)
