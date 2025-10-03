# SNMP MIB module (SLE-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-RIP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:59 2025
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

sleRIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54)
)
if mibBuilder.loadTexts:
    sleRIP.setRevisions(
        ("2010-03-21 19:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleRIPBase_ObjectIdentity = ObjectIdentity
sleRIPBase = _SleRIPBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1)
)
_SleRIPBaseInfo_ObjectIdentity = ObjectIdentity
sleRIPBaseInfo = _SleRIPBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1)
)


class _SleRIPVersion_Type(Integer32):
    """Custom type sleRIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SleRIPVersion_Type.__name__ = "Integer32"
_SleRIPVersion_Object = MibScalar
sleRIPVersion = _SleRIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 1),
    _SleRIPVersion_Type()
)
sleRIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPVersion.setStatus("current")


class _SleRIPDefaultMetric_Type(Integer32):
    """Custom type sleRIPDefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleRIPDefaultMetric_Type.__name__ = "Integer32"
_SleRIPDefaultMetric_Object = MibScalar
sleRIPDefaultMetric = _SleRIPDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 2),
    _SleRIPDefaultMetric_Type()
)
sleRIPDefaultMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDefaultMetric.setStatus("current")


class _SleRIPDefaultInformationOrg_Type(Integer32):
    """Custom type sleRIPDefaultInformationOrg based on Integer32"""
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


_SleRIPDefaultInformationOrg_Type.__name__ = "Integer32"
_SleRIPDefaultInformationOrg_Object = MibScalar
sleRIPDefaultInformationOrg = _SleRIPDefaultInformationOrg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 3),
    _SleRIPDefaultInformationOrg_Type()
)
sleRIPDefaultInformationOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDefaultInformationOrg.setStatus("current")


class _SleRIPDefaultDistance_Type(Integer32):
    """Custom type sleRIPDefaultDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPDefaultDistance_Type.__name__ = "Integer32"
_SleRIPDefaultDistance_Object = MibScalar
sleRIPDefaultDistance = _SleRIPDefaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 4),
    _SleRIPDefaultDistance_Type()
)
sleRIPDefaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDefaultDistance.setStatus("current")


class _SleRIPRecvBufferSize_Type(Integer32):
    """Custom type sleRIPRecvBufferSize based on Integer32"""
    defaultValue = 215040

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 2147483647),
    )


_SleRIPRecvBufferSize_Type.__name__ = "Integer32"
_SleRIPRecvBufferSize_Object = MibScalar
sleRIPRecvBufferSize = _SleRIPRecvBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 5),
    _SleRIPRecvBufferSize_Type()
)
sleRIPRecvBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRecvBufferSize.setStatus("current")


class _SleRIPMaximumPaths_Type(Integer32):
    """Custom type sleRIPMaximumPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleRIPMaximumPaths_Type.__name__ = "Integer32"
_SleRIPMaximumPaths_Object = MibScalar
sleRIPMaximumPaths = _SleRIPMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 6),
    _SleRIPMaximumPaths_Type()
)
sleRIPMaximumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPMaximumPaths.setStatus("current")


class _SleRIPMaximumPrefixRoute_Type(Integer32):
    """Custom type sleRIPMaximumPrefixRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRIPMaximumPrefixRoute_Type.__name__ = "Integer32"
_SleRIPMaximumPrefixRoute_Object = MibScalar
sleRIPMaximumPrefixRoute = _SleRIPMaximumPrefixRoute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 7),
    _SleRIPMaximumPrefixRoute_Type()
)
sleRIPMaximumPrefixRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPMaximumPrefixRoute.setStatus("current")


class _SleRIPMaximumPrefixRoutePercent_Type(Integer32):
    """Custom type sleRIPMaximumPrefixRoutePercent based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleRIPMaximumPrefixRoutePercent_Type.__name__ = "Integer32"
_SleRIPMaximumPrefixRoutePercent_Object = MibScalar
sleRIPMaximumPrefixRoutePercent = _SleRIPMaximumPrefixRoutePercent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 8),
    _SleRIPMaximumPrefixRoutePercent_Type()
)
sleRIPMaximumPrefixRoutePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPMaximumPrefixRoutePercent.setStatus("current")


class _SleRIPMetricSumApply_Type(Integer32):
    """Custom type sleRIPMetricSumApply based on Integer32"""
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


_SleRIPMetricSumApply_Type.__name__ = "Integer32"
_SleRIPMetricSumApply_Object = MibScalar
sleRIPMetricSumApply = _SleRIPMetricSumApply_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 9),
    _SleRIPMetricSumApply_Type()
)
sleRIPMetricSumApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPMetricSumApply.setStatus("current")


class _SleRIPBasicUpdateTimer_Type(Integer32):
    """Custom type sleRIPBasicUpdateTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPBasicUpdateTimer_Type.__name__ = "Integer32"
_SleRIPBasicUpdateTimer_Object = MibScalar
sleRIPBasicUpdateTimer = _SleRIPBasicUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 10),
    _SleRIPBasicUpdateTimer_Type()
)
sleRIPBasicUpdateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPBasicUpdateTimer.setStatus("current")


class _SleRIPBasicTimeoutTimer_Type(Integer32):
    """Custom type sleRIPBasicTimeoutTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPBasicTimeoutTimer_Type.__name__ = "Integer32"
_SleRIPBasicTimeoutTimer_Object = MibScalar
sleRIPBasicTimeoutTimer = _SleRIPBasicTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 11),
    _SleRIPBasicTimeoutTimer_Type()
)
sleRIPBasicTimeoutTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPBasicTimeoutTimer.setStatus("current")


class _SleRIPBasicGarbageTimer_Type(Integer32):
    """Custom type sleRIPBasicGarbageTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPBasicGarbageTimer_Type.__name__ = "Integer32"
_SleRIPBasicGarbageTimer_Object = MibScalar
sleRIPBasicGarbageTimer = _SleRIPBasicGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 12),
    _SleRIPBasicGarbageTimer_Type()
)
sleRIPBasicGarbageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPBasicGarbageTimer.setStatus("current")


class _SleRIPRestartPeriod_Type(Integer32):
    """Custom type sleRIPRestartPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRIPRestartPeriod_Type.__name__ = "Integer32"
_SleRIPRestartPeriod_Object = MibScalar
sleRIPRestartPeriod = _SleRIPRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 1, 13),
    _SleRIPRestartPeriod_Type()
)
sleRIPRestartPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRestartPeriod.setStatus("current")
_SleRIPBaseControl_ObjectIdentity = ObjectIdentity
sleRIPBaseControl = _SleRIPBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2)
)


class _SleRIPControlRequest_Type(Integer32):
    """Custom type sleRIPControlRequest based on Integer32"""
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
        *(("createRIPMode", 1),
          ("deleteRIPMode", 2),
          ("setRIPVersion", 3),
          ("setRIPDefaultMetric", 4),
          ("setRIPDefaultInformationOrg", 5),
          ("setRIPDefaultDistance", 6),
          ("setRIPRecvBufferSize", 7),
          ("setRIPMaximumPaths", 8),
          ("setRIPMaximumPrefixRouteProfile", 9),
          ("setRIPMetricSumApply", 10),
          ("setRIPBasicTimersProfile", 11),
          ("setRIPRestartPeriod", 12),
          ("unsetRIPRestartPeriod", 13),
          ("clearRIPAll", 14),
          ("clearRIPRoute", 15),
          ("clearRIPProtoType", 16))
    )


_SleRIPControlRequest_Type.__name__ = "Integer32"
_SleRIPControlRequest_Object = MibScalar
sleRIPControlRequest = _SleRIPControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 1),
    _SleRIPControlRequest_Type()
)
sleRIPControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPControlRequest.setStatus("current")
_SleRIPControlStatus_Type = SleControlStatusType
_SleRIPControlStatus_Object = MibScalar
sleRIPControlStatus = _SleRIPControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 2),
    _SleRIPControlStatus_Type()
)
sleRIPControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlStatus.setStatus("current")
_SleRIPControlTimer_Type = Gauge32
_SleRIPControlTimer_Object = MibScalar
sleRIPControlTimer = _SleRIPControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 3),
    _SleRIPControlTimer_Type()
)
sleRIPControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPControlTimer.setStatus("current")
_SleRIPControlTimeStamp_Type = TimeTicks
_SleRIPControlTimeStamp_Object = MibScalar
sleRIPControlTimeStamp = _SleRIPControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 4),
    _SleRIPControlTimeStamp_Type()
)
sleRIPControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlTimeStamp.setStatus("current")
_SleRIPControlReqResult_Type = SleControlRequestResultType
_SleRIPControlReqResult_Object = MibScalar
sleRIPControlReqResult = _SleRIPControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 5),
    _SleRIPControlReqResult_Type()
)
sleRIPControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlReqResult.setStatus("current")


class _SleRIPControlVersion_Type(Integer32):
    """Custom type sleRIPControlVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SleRIPControlVersion_Type.__name__ = "Integer32"
_SleRIPControlVersion_Object = MibScalar
sleRIPControlVersion = _SleRIPControlVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 6),
    _SleRIPControlVersion_Type()
)
sleRIPControlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlVersion.setStatus("current")


class _SleRIPControlDefaultMetric_Type(Integer32):
    """Custom type sleRIPControlDefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleRIPControlDefaultMetric_Type.__name__ = "Integer32"
_SleRIPControlDefaultMetric_Object = MibScalar
sleRIPControlDefaultMetric = _SleRIPControlDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 7),
    _SleRIPControlDefaultMetric_Type()
)
sleRIPControlDefaultMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlDefaultMetric.setStatus("current")


class _SleRIPControlDefaultInformationOrg_Type(Integer32):
    """Custom type sleRIPControlDefaultInformationOrg based on Integer32"""
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


_SleRIPControlDefaultInformationOrg_Type.__name__ = "Integer32"
_SleRIPControlDefaultInformationOrg_Object = MibScalar
sleRIPControlDefaultInformationOrg = _SleRIPControlDefaultInformationOrg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 8),
    _SleRIPControlDefaultInformationOrg_Type()
)
sleRIPControlDefaultInformationOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlDefaultInformationOrg.setStatus("current")


class _SleRIPControlDefaultDistance_Type(Integer32):
    """Custom type sleRIPControlDefaultDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPControlDefaultDistance_Type.__name__ = "Integer32"
_SleRIPControlDefaultDistance_Object = MibScalar
sleRIPControlDefaultDistance = _SleRIPControlDefaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 9),
    _SleRIPControlDefaultDistance_Type()
)
sleRIPControlDefaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlDefaultDistance.setStatus("current")


class _SleRIPControlRecvBufferSize_Type(Integer32):
    """Custom type sleRIPControlRecvBufferSize based on Integer32"""
    defaultValue = 215040

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 2147483647),
    )


_SleRIPControlRecvBufferSize_Type.__name__ = "Integer32"
_SleRIPControlRecvBufferSize_Object = MibScalar
sleRIPControlRecvBufferSize = _SleRIPControlRecvBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 10),
    _SleRIPControlRecvBufferSize_Type()
)
sleRIPControlRecvBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlRecvBufferSize.setStatus("current")


class _SleRIPControlMaximumPaths_Type(Integer32):
    """Custom type sleRIPControlMaximumPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleRIPControlMaximumPaths_Type.__name__ = "Integer32"
_SleRIPControlMaximumPaths_Object = MibScalar
sleRIPControlMaximumPaths = _SleRIPControlMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 11),
    _SleRIPControlMaximumPaths_Type()
)
sleRIPControlMaximumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlMaximumPaths.setStatus("current")


class _SleRIPControlMaximumPrefixRoute_Type(Integer32):
    """Custom type sleRIPControlMaximumPrefixRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRIPControlMaximumPrefixRoute_Type.__name__ = "Integer32"
_SleRIPControlMaximumPrefixRoute_Object = MibScalar
sleRIPControlMaximumPrefixRoute = _SleRIPControlMaximumPrefixRoute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 12),
    _SleRIPControlMaximumPrefixRoute_Type()
)
sleRIPControlMaximumPrefixRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlMaximumPrefixRoute.setStatus("current")


class _SleRIPControlMaximumPrefixRoutePercent_Type(Integer32):
    """Custom type sleRIPControlMaximumPrefixRoutePercent based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleRIPControlMaximumPrefixRoutePercent_Type.__name__ = "Integer32"
_SleRIPControlMaximumPrefixRoutePercent_Object = MibScalar
sleRIPControlMaximumPrefixRoutePercent = _SleRIPControlMaximumPrefixRoutePercent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 13),
    _SleRIPControlMaximumPrefixRoutePercent_Type()
)
sleRIPControlMaximumPrefixRoutePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlMaximumPrefixRoutePercent.setStatus("current")


class _SleRIPControlMetricSumApply_Type(Integer32):
    """Custom type sleRIPControlMetricSumApply based on Integer32"""
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


_SleRIPControlMetricSumApply_Type.__name__ = "Integer32"
_SleRIPControlMetricSumApply_Object = MibScalar
sleRIPControlMetricSumApply = _SleRIPControlMetricSumApply_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 14),
    _SleRIPControlMetricSumApply_Type()
)
sleRIPControlMetricSumApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlMetricSumApply.setStatus("current")


class _SleRIPControlBasicUpdateTimer_Type(Integer32):
    """Custom type sleRIPControlBasicUpdateTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPControlBasicUpdateTimer_Type.__name__ = "Integer32"
_SleRIPControlBasicUpdateTimer_Object = MibScalar
sleRIPControlBasicUpdateTimer = _SleRIPControlBasicUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 15),
    _SleRIPControlBasicUpdateTimer_Type()
)
sleRIPControlBasicUpdateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlBasicUpdateTimer.setStatus("current")


class _SleRIPControlBasicTimeoutTimer_Type(Integer32):
    """Custom type sleRIPControlBasicTimeoutTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPControlBasicTimeoutTimer_Type.__name__ = "Integer32"
_SleRIPControlBasicTimeoutTimer_Object = MibScalar
sleRIPControlBasicTimeoutTimer = _SleRIPControlBasicTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 16),
    _SleRIPControlBasicTimeoutTimer_Type()
)
sleRIPControlBasicTimeoutTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlBasicTimeoutTimer.setStatus("current")


class _SleRIPControlBasicGarbageTimer_Type(Integer32):
    """Custom type sleRIPControlBasicGarbageTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPControlBasicGarbageTimer_Type.__name__ = "Integer32"
_SleRIPControlBasicGarbageTimer_Object = MibScalar
sleRIPControlBasicGarbageTimer = _SleRIPControlBasicGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 17),
    _SleRIPControlBasicGarbageTimer_Type()
)
sleRIPControlBasicGarbageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlBasicGarbageTimer.setStatus("current")


class _SleRIPControlRestartPeriod_Type(Integer32):
    """Custom type sleRIPControlRestartPeriod based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_SleRIPControlRestartPeriod_Type.__name__ = "Integer32"
_SleRIPControlRestartPeriod_Object = MibScalar
sleRIPControlRestartPeriod = _SleRIPControlRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 18),
    _SleRIPControlRestartPeriod_Type()
)
sleRIPControlRestartPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlRestartPeriod.setStatus("current")
_SleRIPControlClearRoutePrefix_Type = IpAddress
_SleRIPControlClearRoutePrefix_Object = MibScalar
sleRIPControlClearRoutePrefix = _SleRIPControlClearRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 19),
    _SleRIPControlClearRoutePrefix_Type()
)
sleRIPControlClearRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlClearRoutePrefix.setStatus("current")


class _SleRIPControlClearRouteMask_Type(Integer32):
    """Custom type sleRIPControlClearRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPControlClearRouteMask_Type.__name__ = "Integer32"
_SleRIPControlClearRouteMask_Object = MibScalar
sleRIPControlClearRouteMask = _SleRIPControlClearRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 20),
    _SleRIPControlClearRouteMask_Type()
)
sleRIPControlClearRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlClearRouteMask.setStatus("current")


class _SleRIPControlClearProtoTpye_Type(Integer32):
    """Custom type sleRIPControlClearProtoTpye based on Integer32"""
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


_SleRIPControlClearProtoTpye_Type.__name__ = "Integer32"
_SleRIPControlClearProtoTpye_Object = MibScalar
sleRIPControlClearProtoTpye = _SleRIPControlClearProtoTpye_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 2, 21),
    _SleRIPControlClearProtoTpye_Type()
)
sleRIPControlClearProtoTpye.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPControlClearProtoTpye.setStatus("current")
_SleRIPBaseNotification_ObjectIdentity = ObjectIdentity
sleRIPBaseNotification = _SleRIPBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3)
)
_SleRIPNetwork_ObjectIdentity = ObjectIdentity
sleRIPNetwork = _SleRIPNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2)
)
_SleRIPNetworkIP_ObjectIdentity = ObjectIdentity
sleRIPNetworkIP = _SleRIPNetworkIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1)
)
_SleRIPNetworkIPTable_Object = MibTable
sleRIPNetworkIPTable = _SleRIPNetworkIPTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleRIPNetworkIPTable.setStatus("current")
_SleRIPNetworkIPEntry_Object = MibTableRow
sleRIPNetworkIPEntry = _SleRIPNetworkIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 1, 1)
)
sleRIPNetworkIPEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPNetworkIPAddr"),
    (0, "SLE-RIP-MIB", "sleRIPNetworkIPMask"),
)
if mibBuilder.loadTexts:
    sleRIPNetworkIPEntry.setStatus("current")
_SleRIPNetworkIPAddr_Type = IpAddress
_SleRIPNetworkIPAddr_Object = MibTableColumn
sleRIPNetworkIPAddr = _SleRIPNetworkIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 1, 1, 1),
    _SleRIPNetworkIPAddr_Type()
)
sleRIPNetworkIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkIPAddr.setStatus("current")


class _SleRIPNetworkIPMask_Type(Integer32):
    """Custom type sleRIPNetworkIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPNetworkIPMask_Type.__name__ = "Integer32"
_SleRIPNetworkIPMask_Object = MibTableColumn
sleRIPNetworkIPMask = _SleRIPNetworkIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 1, 1, 2),
    _SleRIPNetworkIPMask_Type()
)
sleRIPNetworkIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkIPMask.setStatus("current")
_SleRIPNetworkIPControl_ObjectIdentity = ObjectIdentity
sleRIPNetworkIPControl = _SleRIPNetworkIPControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2)
)


class _SleRIPNetworkIPControlRequest_Type(Integer32):
    """Custom type sleRIPNetworkIPControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPNetworkIP", 1),
          ("deleteRIPNetworkIP", 2))
    )


_SleRIPNetworkIPControlRequest_Type.__name__ = "Integer32"
_SleRIPNetworkIPControlRequest_Object = MibScalar
sleRIPNetworkIPControlRequest = _SleRIPNetworkIPControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2, 1),
    _SleRIPNetworkIPControlRequest_Type()
)
sleRIPNetworkIPControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNetworkIPControlRequest.setStatus("current")
_SleRIPNetworkIPControlStatus_Type = SleControlStatusType
_SleRIPNetworkIPControlStatus_Object = MibScalar
sleRIPNetworkIPControlStatus = _SleRIPNetworkIPControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2, 2),
    _SleRIPNetworkIPControlStatus_Type()
)
sleRIPNetworkIPControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkIPControlStatus.setStatus("current")
_SleRIPNetworkIPControlTimer_Type = Gauge32
_SleRIPNetworkIPControlTimer_Object = MibScalar
sleRIPNetworkIPControlTimer = _SleRIPNetworkIPControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2, 3),
    _SleRIPNetworkIPControlTimer_Type()
)
sleRIPNetworkIPControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNetworkIPControlTimer.setStatus("current")
_SleRIPNetworkIPControlTimeStamp_Type = TimeTicks
_SleRIPNetworkIPControlTimeStamp_Object = MibScalar
sleRIPNetworkIPControlTimeStamp = _SleRIPNetworkIPControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2, 4),
    _SleRIPNetworkIPControlTimeStamp_Type()
)
sleRIPNetworkIPControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkIPControlTimeStamp.setStatus("current")
_SleRIPNetworkIPControlReqResult_Type = SleControlRequestResultType
_SleRIPNetworkIPControlReqResult_Object = MibScalar
sleRIPNetworkIPControlReqResult = _SleRIPNetworkIPControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2, 5),
    _SleRIPNetworkIPControlReqResult_Type()
)
sleRIPNetworkIPControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkIPControlReqResult.setStatus("current")
_SleRIPNetworkIPControlIPAddr_Type = IpAddress
_SleRIPNetworkIPControlIPAddr_Object = MibScalar
sleRIPNetworkIPControlIPAddr = _SleRIPNetworkIPControlIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2, 6),
    _SleRIPNetworkIPControlIPAddr_Type()
)
sleRIPNetworkIPControlIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNetworkIPControlIPAddr.setStatus("current")


class _SleRIPNetworkIPControlIPMask_Type(Integer32):
    """Custom type sleRIPNetworkIPControlIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPNetworkIPControlIPMask_Type.__name__ = "Integer32"
_SleRIPNetworkIPControlIPMask_Object = MibScalar
sleRIPNetworkIPControlIPMask = _SleRIPNetworkIPControlIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 2, 7),
    _SleRIPNetworkIPControlIPMask_Type()
)
sleRIPNetworkIPControlIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNetworkIPControlIPMask.setStatus("current")
_SleRIPNetworkIPNotification_ObjectIdentity = ObjectIdentity
sleRIPNetworkIPNotification = _SleRIPNetworkIPNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 3)
)
_SleRIPNetworkInterface_ObjectIdentity = ObjectIdentity
sleRIPNetworkInterface = _SleRIPNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2)
)
_SleRIPNetworkInterfaceTable_Object = MibTable
sleRIPNetworkInterfaceTable = _SleRIPNetworkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceTable.setStatus("current")
_SleRIPNetworkInterfaceEntry_Object = MibTableRow
sleRIPNetworkInterfaceEntry = _SleRIPNetworkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 1, 1)
)
sleRIPNetworkInterfaceEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPNetworkInterfaceName"),
)
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceEntry.setStatus("current")


class _SleRIPNetworkInterfaceName_Type(OctetString):
    """Custom type sleRIPNetworkInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPNetworkInterfaceName_Type.__name__ = "OctetString"
_SleRIPNetworkInterfaceName_Object = MibTableColumn
sleRIPNetworkInterfaceName = _SleRIPNetworkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 1, 1, 1),
    _SleRIPNetworkInterfaceName_Type()
)
sleRIPNetworkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceName.setStatus("current")
_SleRIPNetworkInterfaceControl_ObjectIdentity = ObjectIdentity
sleRIPNetworkInterfaceControl = _SleRIPNetworkInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 2)
)


class _SleRIPNetworkInterfaceControlRequest_Type(Integer32):
    """Custom type sleRIPNetworkInterfaceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPNetworkIfname", 1),
          ("deleteRIPNetworkIfname", 2))
    )


_SleRIPNetworkInterfaceControlRequest_Type.__name__ = "Integer32"
_SleRIPNetworkInterfaceControlRequest_Object = MibScalar
sleRIPNetworkInterfaceControlRequest = _SleRIPNetworkInterfaceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 2, 1),
    _SleRIPNetworkInterfaceControlRequest_Type()
)
sleRIPNetworkInterfaceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceControlRequest.setStatus("current")
_SleRIPNetworkInterfaceControlStatus_Type = SleControlStatusType
_SleRIPNetworkInterfaceControlStatus_Object = MibScalar
sleRIPNetworkInterfaceControlStatus = _SleRIPNetworkInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 2, 2),
    _SleRIPNetworkInterfaceControlStatus_Type()
)
sleRIPNetworkInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceControlStatus.setStatus("current")
_SleRIPNetworkInterfaceControlTimer_Type = Gauge32
_SleRIPNetworkInterfaceControlTimer_Object = MibScalar
sleRIPNetworkInterfaceControlTimer = _SleRIPNetworkInterfaceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 2, 3),
    _SleRIPNetworkInterfaceControlTimer_Type()
)
sleRIPNetworkInterfaceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceControlTimer.setStatus("current")
_SleRIPNetworkInterfaceControlTimeStamp_Type = TimeTicks
_SleRIPNetworkInterfaceControlTimeStamp_Object = MibScalar
sleRIPNetworkInterfaceControlTimeStamp = _SleRIPNetworkInterfaceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 2, 4),
    _SleRIPNetworkInterfaceControlTimeStamp_Type()
)
sleRIPNetworkInterfaceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceControlTimeStamp.setStatus("current")
_SleRIPNetworkInterfaceControlReqResult_Type = SleControlRequestResultType
_SleRIPNetworkInterfaceControlReqResult_Object = MibScalar
sleRIPNetworkInterfaceControlReqResult = _SleRIPNetworkInterfaceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 2, 5),
    _SleRIPNetworkInterfaceControlReqResult_Type()
)
sleRIPNetworkInterfaceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceControlReqResult.setStatus("current")


class _SleRIPNetworkInterfaceControlName_Type(OctetString):
    """Custom type sleRIPNetworkInterfaceControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPNetworkInterfaceControlName_Type.__name__ = "OctetString"
_SleRIPNetworkInterfaceControlName_Object = MibScalar
sleRIPNetworkInterfaceControlName = _SleRIPNetworkInterfaceControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 2, 6),
    _SleRIPNetworkInterfaceControlName_Type()
)
sleRIPNetworkInterfaceControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceControlName.setStatus("current")
_SleRIPNetworkInterfaceNotification_ObjectIdentity = ObjectIdentity
sleRIPNetworkInterfaceNotification = _SleRIPNetworkInterfaceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 3)
)
_SleRIPNeighbor_ObjectIdentity = ObjectIdentity
sleRIPNeighbor = _SleRIPNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3)
)
_SleRIPNeighborTable_Object = MibTable
sleRIPNeighborTable = _SleRIPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 1)
)
if mibBuilder.loadTexts:
    sleRIPNeighborTable.setStatus("current")
_SleRIPNeighborEntry_Object = MibTableRow
sleRIPNeighborEntry = _SleRIPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 1, 1)
)
sleRIPNeighborEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPNeighborIPAddr"),
)
if mibBuilder.loadTexts:
    sleRIPNeighborEntry.setStatus("current")
_SleRIPNeighborIPAddr_Type = IpAddress
_SleRIPNeighborIPAddr_Object = MibTableColumn
sleRIPNeighborIPAddr = _SleRIPNeighborIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 1, 1, 1),
    _SleRIPNeighborIPAddr_Type()
)
sleRIPNeighborIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNeighborIPAddr.setStatus("current")
_SleRIPNeighborControl_ObjectIdentity = ObjectIdentity
sleRIPNeighborControl = _SleRIPNeighborControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 2)
)


class _SleRIPNeighborControlRequest_Type(Integer32):
    """Custom type sleRIPNeighborControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPNeighbor", 1),
          ("deleteRIPNeighbor", 2))
    )


_SleRIPNeighborControlRequest_Type.__name__ = "Integer32"
_SleRIPNeighborControlRequest_Object = MibScalar
sleRIPNeighborControlRequest = _SleRIPNeighborControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 2, 1),
    _SleRIPNeighborControlRequest_Type()
)
sleRIPNeighborControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNeighborControlRequest.setStatus("current")
_SleRIPNeighborControlStatus_Type = SleControlStatusType
_SleRIPNeighborControlStatus_Object = MibScalar
sleRIPNeighborControlStatus = _SleRIPNeighborControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 2, 2),
    _SleRIPNeighborControlStatus_Type()
)
sleRIPNeighborControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNeighborControlStatus.setStatus("current")
_SleRIPNeighborControlTimer_Type = Gauge32
_SleRIPNeighborControlTimer_Object = MibScalar
sleRIPNeighborControlTimer = _SleRIPNeighborControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 2, 3),
    _SleRIPNeighborControlTimer_Type()
)
sleRIPNeighborControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNeighborControlTimer.setStatus("current")
_SleRIPNeighborControlTimeStamp_Type = TimeTicks
_SleRIPNeighborControlTimeStamp_Object = MibScalar
sleRIPNeighborControlTimeStamp = _SleRIPNeighborControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 2, 4),
    _SleRIPNeighborControlTimeStamp_Type()
)
sleRIPNeighborControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNeighborControlTimeStamp.setStatus("current")
_SleRIPNeighborControlReqResult_Type = SleControlRequestResultType
_SleRIPNeighborControlReqResult_Object = MibScalar
sleRIPNeighborControlReqResult = _SleRIPNeighborControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 2, 5),
    _SleRIPNeighborControlReqResult_Type()
)
sleRIPNeighborControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPNeighborControlReqResult.setStatus("current")
_SleRIPNeighborControlIPAddr_Type = IpAddress
_SleRIPNeighborControlIPAddr_Object = MibScalar
sleRIPNeighborControlIPAddr = _SleRIPNeighborControlIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 2, 6),
    _SleRIPNeighborControlIPAddr_Type()
)
sleRIPNeighborControlIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPNeighborControlIPAddr.setStatus("current")
_SleRIPNeighborNotification_ObjectIdentity = ObjectIdentity
sleRIPNeighborNotification = _SleRIPNeighborNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 3)
)
_SleRIPStaticRoute_ObjectIdentity = ObjectIdentity
sleRIPStaticRoute = _SleRIPStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4)
)
_SleRIPStaticRouteTable_Object = MibTable
sleRIPStaticRouteTable = _SleRIPStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 1)
)
if mibBuilder.loadTexts:
    sleRIPStaticRouteTable.setStatus("current")
_SleRIPStaticRouteEntry_Object = MibTableRow
sleRIPStaticRouteEntry = _SleRIPStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 1, 1)
)
sleRIPStaticRouteEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPStaticRouteIPAddr"),
    (0, "SLE-RIP-MIB", "sleRIPStaticRouteIPMask"),
)
if mibBuilder.loadTexts:
    sleRIPStaticRouteEntry.setStatus("current")
_SleRIPStaticRouteIPAddr_Type = IpAddress
_SleRIPStaticRouteIPAddr_Object = MibTableColumn
sleRIPStaticRouteIPAddr = _SleRIPStaticRouteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 1, 1, 1),
    _SleRIPStaticRouteIPAddr_Type()
)
sleRIPStaticRouteIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPStaticRouteIPAddr.setStatus("current")


class _SleRIPStaticRouteIPMask_Type(Integer32):
    """Custom type sleRIPStaticRouteIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPStaticRouteIPMask_Type.__name__ = "Integer32"
_SleRIPStaticRouteIPMask_Object = MibTableColumn
sleRIPStaticRouteIPMask = _SleRIPStaticRouteIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 1, 1, 2),
    _SleRIPStaticRouteIPMask_Type()
)
sleRIPStaticRouteIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPStaticRouteIPMask.setStatus("current")
_SleRIPStaticRouteControl_ObjectIdentity = ObjectIdentity
sleRIPStaticRouteControl = _SleRIPStaticRouteControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2)
)


class _SleRIPStaticRouteControlRequest_Type(Integer32):
    """Custom type sleRIPStaticRouteControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPStaticRoute", 1),
          ("deleteRIPStaticRoute", 2))
    )


_SleRIPStaticRouteControlRequest_Type.__name__ = "Integer32"
_SleRIPStaticRouteControlRequest_Object = MibScalar
sleRIPStaticRouteControlRequest = _SleRIPStaticRouteControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2, 1),
    _SleRIPStaticRouteControlRequest_Type()
)
sleRIPStaticRouteControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPStaticRouteControlRequest.setStatus("current")
_SleRIPStaticRouteControlStatus_Type = SleControlStatusType
_SleRIPStaticRouteControlStatus_Object = MibScalar
sleRIPStaticRouteControlStatus = _SleRIPStaticRouteControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2, 2),
    _SleRIPStaticRouteControlStatus_Type()
)
sleRIPStaticRouteControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPStaticRouteControlStatus.setStatus("current")
_SleRIPStaticRouteControlTimer_Type = Gauge32
_SleRIPStaticRouteControlTimer_Object = MibScalar
sleRIPStaticRouteControlTimer = _SleRIPStaticRouteControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2, 3),
    _SleRIPStaticRouteControlTimer_Type()
)
sleRIPStaticRouteControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPStaticRouteControlTimer.setStatus("current")
_SleRIPStaticRouteControlTimeStamp_Type = TimeTicks
_SleRIPStaticRouteControlTimeStamp_Object = MibScalar
sleRIPStaticRouteControlTimeStamp = _SleRIPStaticRouteControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2, 4),
    _SleRIPStaticRouteControlTimeStamp_Type()
)
sleRIPStaticRouteControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPStaticRouteControlTimeStamp.setStatus("current")
_SleRIPStaticRouteControlReqResult_Type = SleControlRequestResultType
_SleRIPStaticRouteControlReqResult_Object = MibScalar
sleRIPStaticRouteControlReqResult = _SleRIPStaticRouteControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2, 5),
    _SleRIPStaticRouteControlReqResult_Type()
)
sleRIPStaticRouteControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPStaticRouteControlReqResult.setStatus("current")
_SleRIPStaticRouteControlIPAddr_Type = IpAddress
_SleRIPStaticRouteControlIPAddr_Object = MibScalar
sleRIPStaticRouteControlIPAddr = _SleRIPStaticRouteControlIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2, 6),
    _SleRIPStaticRouteControlIPAddr_Type()
)
sleRIPStaticRouteControlIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPStaticRouteControlIPAddr.setStatus("current")


class _SleRIPStaticRouteControlIPMask_Type(Integer32):
    """Custom type sleRIPStaticRouteControlIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPStaticRouteControlIPMask_Type.__name__ = "Integer32"
_SleRIPStaticRouteControlIPMask_Object = MibScalar
sleRIPStaticRouteControlIPMask = _SleRIPStaticRouteControlIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 2, 7),
    _SleRIPStaticRouteControlIPMask_Type()
)
sleRIPStaticRouteControlIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPStaticRouteControlIPMask.setStatus("current")
_SleRIPStaticRouteNotification_ObjectIdentity = ObjectIdentity
sleRIPStaticRouteNotification = _SleRIPStaticRouteNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 3)
)
_SleRIPAdminDistance_ObjectIdentity = ObjectIdentity
sleRIPAdminDistance = _SleRIPAdminDistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5)
)
_SleRIPAdminDistanceTable_Object = MibTable
sleRIPAdminDistanceTable = _SleRIPAdminDistanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 1)
)
if mibBuilder.loadTexts:
    sleRIPAdminDistanceTable.setStatus("current")
_SleRIPAdminDistanceEntry_Object = MibTableRow
sleRIPAdminDistanceEntry = _SleRIPAdminDistanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 1, 1)
)
sleRIPAdminDistanceEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPAdminDistanceValue"),
    (0, "SLE-RIP-MIB", "sleRIPAdminDistanceAddr"),
    (0, "SLE-RIP-MIB", "sleRIPAdminDistanceMask"),
)
if mibBuilder.loadTexts:
    sleRIPAdminDistanceEntry.setStatus("current")


class _SleRIPAdminDistanceValue_Type(Integer32):
    """Custom type sleRIPAdminDistanceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPAdminDistanceValue_Type.__name__ = "Integer32"
_SleRIPAdminDistanceValue_Object = MibTableColumn
sleRIPAdminDistanceValue = _SleRIPAdminDistanceValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 1, 1, 1),
    _SleRIPAdminDistanceValue_Type()
)
sleRIPAdminDistanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceValue.setStatus("current")
_SleRIPAdminDistanceAddr_Type = IpAddress
_SleRIPAdminDistanceAddr_Object = MibTableColumn
sleRIPAdminDistanceAddr = _SleRIPAdminDistanceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 1, 1, 2),
    _SleRIPAdminDistanceAddr_Type()
)
sleRIPAdminDistanceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceAddr.setStatus("current")


class _SleRIPAdminDistanceMask_Type(Integer32):
    """Custom type sleRIPAdminDistanceMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPAdminDistanceMask_Type.__name__ = "Integer32"
_SleRIPAdminDistanceMask_Object = MibTableColumn
sleRIPAdminDistanceMask = _SleRIPAdminDistanceMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 1, 1, 3),
    _SleRIPAdminDistanceMask_Type()
)
sleRIPAdminDistanceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceMask.setStatus("current")


class _SleRIPAdminDistanceAccessName_Type(OctetString):
    """Custom type sleRIPAdminDistanceAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPAdminDistanceAccessName_Type.__name__ = "OctetString"
_SleRIPAdminDistanceAccessName_Object = MibTableColumn
sleRIPAdminDistanceAccessName = _SleRIPAdminDistanceAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 1, 1, 4),
    _SleRIPAdminDistanceAccessName_Type()
)
sleRIPAdminDistanceAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceAccessName.setStatus("current")
_SleRIPAdminDistanceControl_ObjectIdentity = ObjectIdentity
sleRIPAdminDistanceControl = _SleRIPAdminDistanceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2)
)


class _SleRIPAdminDistanceControlRequest_Type(Integer32):
    """Custom type sleRIPAdminDistanceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPAdminDistance", 1),
          ("deleteRIPAdminDistance", 2))
    )


_SleRIPAdminDistanceControlRequest_Type.__name__ = "Integer32"
_SleRIPAdminDistanceControlRequest_Object = MibScalar
sleRIPAdminDistanceControlRequest = _SleRIPAdminDistanceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 1),
    _SleRIPAdminDistanceControlRequest_Type()
)
sleRIPAdminDistanceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlRequest.setStatus("current")
_SleRIPAdminDistanceControlStatus_Type = SleControlStatusType
_SleRIPAdminDistanceControlStatus_Object = MibScalar
sleRIPAdminDistanceControlStatus = _SleRIPAdminDistanceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 2),
    _SleRIPAdminDistanceControlStatus_Type()
)
sleRIPAdminDistanceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlStatus.setStatus("current")
_SleRIPAdminDistanceControlTimer_Type = Gauge32
_SleRIPAdminDistanceControlTimer_Object = MibScalar
sleRIPAdminDistanceControlTimer = _SleRIPAdminDistanceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 3),
    _SleRIPAdminDistanceControlTimer_Type()
)
sleRIPAdminDistanceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlTimer.setStatus("current")
_SleRIPAdminDistanceControlTimeStamp_Type = TimeTicks
_SleRIPAdminDistanceControlTimeStamp_Object = MibScalar
sleRIPAdminDistanceControlTimeStamp = _SleRIPAdminDistanceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 4),
    _SleRIPAdminDistanceControlTimeStamp_Type()
)
sleRIPAdminDistanceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlTimeStamp.setStatus("current")
_SleRIPAdminDistanceControlReqResult_Type = SleControlRequestResultType
_SleRIPAdminDistanceControlReqResult_Object = MibScalar
sleRIPAdminDistanceControlReqResult = _SleRIPAdminDistanceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 5),
    _SleRIPAdminDistanceControlReqResult_Type()
)
sleRIPAdminDistanceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlReqResult.setStatus("current")


class _SleRIPAdminDistanceControlValue_Type(Integer32):
    """Custom type sleRIPAdminDistanceControlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRIPAdminDistanceControlValue_Type.__name__ = "Integer32"
_SleRIPAdminDistanceControlValue_Object = MibScalar
sleRIPAdminDistanceControlValue = _SleRIPAdminDistanceControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 6),
    _SleRIPAdminDistanceControlValue_Type()
)
sleRIPAdminDistanceControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlValue.setStatus("current")
_SleRIPAdminDistanceControlAddr_Type = IpAddress
_SleRIPAdminDistanceControlAddr_Object = MibScalar
sleRIPAdminDistanceControlAddr = _SleRIPAdminDistanceControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 7),
    _SleRIPAdminDistanceControlAddr_Type()
)
sleRIPAdminDistanceControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlAddr.setStatus("current")


class _SleRIPAdminDistanceControlMask_Type(Integer32):
    """Custom type sleRIPAdminDistanceControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPAdminDistanceControlMask_Type.__name__ = "Integer32"
_SleRIPAdminDistanceControlMask_Object = MibScalar
sleRIPAdminDistanceControlMask = _SleRIPAdminDistanceControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 8),
    _SleRIPAdminDistanceControlMask_Type()
)
sleRIPAdminDistanceControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlMask.setStatus("current")


class _SleRIPAdminDistanceControlAccessName_Type(OctetString):
    """Custom type sleRIPAdminDistanceControlAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPAdminDistanceControlAccessName_Type.__name__ = "OctetString"
_SleRIPAdminDistanceControlAccessName_Object = MibScalar
sleRIPAdminDistanceControlAccessName = _SleRIPAdminDistanceControlAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 2, 9),
    _SleRIPAdminDistanceControlAccessName_Type()
)
sleRIPAdminDistanceControlAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPAdminDistanceControlAccessName.setStatus("current")
_SleRIPAdminDistanceNotification_ObjectIdentity = ObjectIdentity
sleRIPAdminDistanceNotification = _SleRIPAdminDistanceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 3)
)
_SleRIPDistribute_ObjectIdentity = ObjectIdentity
sleRIPDistribute = _SleRIPDistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6)
)
_SleRIPDistributeTable_Object = MibTable
sleRIPDistributeTable = _SleRIPDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 1)
)
if mibBuilder.loadTexts:
    sleRIPDistributeTable.setStatus("current")
_SleRIPDistributeEntry_Object = MibTableRow
sleRIPDistributeEntry = _SleRIPDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 1, 1)
)
sleRIPDistributeEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPDistributeIfName"),
)
if mibBuilder.loadTexts:
    sleRIPDistributeEntry.setStatus("current")


class _SleRIPDistributeIfName_Type(OctetString):
    """Custom type sleRIPDistributeIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeIfName_Type.__name__ = "OctetString"
_SleRIPDistributeIfName_Object = MibTableColumn
sleRIPDistributeIfName = _SleRIPDistributeIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 1, 1, 1),
    _SleRIPDistributeIfName_Type()
)
sleRIPDistributeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeIfName.setStatus("current")


class _SleRIPDistributeInAccessName_Type(OctetString):
    """Custom type sleRIPDistributeInAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeInAccessName_Type.__name__ = "OctetString"
_SleRIPDistributeInAccessName_Object = MibTableColumn
sleRIPDistributeInAccessName = _SleRIPDistributeInAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 1, 1, 2),
    _SleRIPDistributeInAccessName_Type()
)
sleRIPDistributeInAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeInAccessName.setStatus("current")


class _SleRIPDistributeOutAccessName_Type(OctetString):
    """Custom type sleRIPDistributeOutAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeOutAccessName_Type.__name__ = "OctetString"
_SleRIPDistributeOutAccessName_Object = MibTableColumn
sleRIPDistributeOutAccessName = _SleRIPDistributeOutAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 1, 1, 3),
    _SleRIPDistributeOutAccessName_Type()
)
sleRIPDistributeOutAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeOutAccessName.setStatus("current")


class _SleRIPDistributeInPrefixName_Type(OctetString):
    """Custom type sleRIPDistributeInPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeInPrefixName_Type.__name__ = "OctetString"
_SleRIPDistributeInPrefixName_Object = MibTableColumn
sleRIPDistributeInPrefixName = _SleRIPDistributeInPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 1, 1, 4),
    _SleRIPDistributeInPrefixName_Type()
)
sleRIPDistributeInPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeInPrefixName.setStatus("current")


class _SleRIPDistributeOutPrefixName_Type(OctetString):
    """Custom type sleRIPDistributeOutPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeOutPrefixName_Type.__name__ = "OctetString"
_SleRIPDistributeOutPrefixName_Object = MibTableColumn
sleRIPDistributeOutPrefixName = _SleRIPDistributeOutPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 1, 1, 5),
    _SleRIPDistributeOutPrefixName_Type()
)
sleRIPDistributeOutPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeOutPrefixName.setStatus("current")
_SleRIPDistributeControl_ObjectIdentity = ObjectIdentity
sleRIPDistributeControl = _SleRIPDistributeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2)
)


class _SleRIPDistributeControlRequest_Type(Integer32):
    """Custom type sleRIPDistributeControlRequest based on Integer32"""
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
        *(("createRIPDistributeInAccess", 1),
          ("deleteRIPDistributeInAccess", 2),
          ("createRIPDistributeOutAccess", 3),
          ("deleteRIPDistributeOutAccess", 4),
          ("createRIPDistributeInPrefix", 5),
          ("deleteRIPDistributeInPrefix", 6),
          ("createRIPDistributeOutPrefix", 7),
          ("deleteRIPDistributeOutPrefix", 8))
    )


_SleRIPDistributeControlRequest_Type.__name__ = "Integer32"
_SleRIPDistributeControlRequest_Object = MibScalar
sleRIPDistributeControlRequest = _SleRIPDistributeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 1),
    _SleRIPDistributeControlRequest_Type()
)
sleRIPDistributeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPDistributeControlRequest.setStatus("current")
_SleRIPDistributeControlStatus_Type = SleControlStatusType
_SleRIPDistributeControlStatus_Object = MibScalar
sleRIPDistributeControlStatus = _SleRIPDistributeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 2),
    _SleRIPDistributeControlStatus_Type()
)
sleRIPDistributeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeControlStatus.setStatus("current")
_SleRIPDistributeControlTimer_Type = Gauge32
_SleRIPDistributeControlTimer_Object = MibScalar
sleRIPDistributeControlTimer = _SleRIPDistributeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 3),
    _SleRIPDistributeControlTimer_Type()
)
sleRIPDistributeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPDistributeControlTimer.setStatus("current")
_SleRIPDistributeControlTimeStamp_Type = TimeTicks
_SleRIPDistributeControlTimeStamp_Object = MibScalar
sleRIPDistributeControlTimeStamp = _SleRIPDistributeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 4),
    _SleRIPDistributeControlTimeStamp_Type()
)
sleRIPDistributeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeControlTimeStamp.setStatus("current")
_SleRIPDistributeControlReqResult_Type = SleControlRequestResultType
_SleRIPDistributeControlReqResult_Object = MibScalar
sleRIPDistributeControlReqResult = _SleRIPDistributeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 5),
    _SleRIPDistributeControlReqResult_Type()
)
sleRIPDistributeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPDistributeControlReqResult.setStatus("current")


class _SleRIPDistributeControlIfName_Type(OctetString):
    """Custom type sleRIPDistributeControlIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeControlIfName_Type.__name__ = "OctetString"
_SleRIPDistributeControlIfName_Object = MibScalar
sleRIPDistributeControlIfName = _SleRIPDistributeControlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 6),
    _SleRIPDistributeControlIfName_Type()
)
sleRIPDistributeControlIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPDistributeControlIfName.setStatus("current")


class _SleRIPDistributeControlInAccessName_Type(OctetString):
    """Custom type sleRIPDistributeControlInAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeControlInAccessName_Type.__name__ = "OctetString"
_SleRIPDistributeControlInAccessName_Object = MibScalar
sleRIPDistributeControlInAccessName = _SleRIPDistributeControlInAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 7),
    _SleRIPDistributeControlInAccessName_Type()
)
sleRIPDistributeControlInAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPDistributeControlInAccessName.setStatus("current")


class _SleRIPDistributeControlOutAccessName_Type(OctetString):
    """Custom type sleRIPDistributeControlOutAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeControlOutAccessName_Type.__name__ = "OctetString"
_SleRIPDistributeControlOutAccessName_Object = MibScalar
sleRIPDistributeControlOutAccessName = _SleRIPDistributeControlOutAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 8),
    _SleRIPDistributeControlOutAccessName_Type()
)
sleRIPDistributeControlOutAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPDistributeControlOutAccessName.setStatus("current")


class _SleRIPDistributeControlInPrefixName_Type(OctetString):
    """Custom type sleRIPDistributeControlInPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeControlInPrefixName_Type.__name__ = "OctetString"
_SleRIPDistributeControlInPrefixName_Object = MibScalar
sleRIPDistributeControlInPrefixName = _SleRIPDistributeControlInPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 9),
    _SleRIPDistributeControlInPrefixName_Type()
)
sleRIPDistributeControlInPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPDistributeControlInPrefixName.setStatus("current")


class _SleRIPDistributeControlOutPrefixName_Type(OctetString):
    """Custom type sleRIPDistributeControlOutPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPDistributeControlOutPrefixName_Type.__name__ = "OctetString"
_SleRIPDistributeControlOutPrefixName_Object = MibScalar
sleRIPDistributeControlOutPrefixName = _SleRIPDistributeControlOutPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 2, 10),
    _SleRIPDistributeControlOutPrefixName_Type()
)
sleRIPDistributeControlOutPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPDistributeControlOutPrefixName.setStatus("current")
_SleRIPDistributeNotification_ObjectIdentity = ObjectIdentity
sleRIPDistributeNotification = _SleRIPDistributeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3)
)
_SleRIPOffsetList_ObjectIdentity = ObjectIdentity
sleRIPOffsetList = _SleRIPOffsetList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7)
)
_SleRIPOffsetListTable_Object = MibTable
sleRIPOffsetListTable = _SleRIPOffsetListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 1)
)
if mibBuilder.loadTexts:
    sleRIPOffsetListTable.setStatus("current")
_SleRIPOffsetListEntry_Object = MibTableRow
sleRIPOffsetListEntry = _SleRIPOffsetListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 1, 1)
)
sleRIPOffsetListEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPOffsetListIfname"),
)
if mibBuilder.loadTexts:
    sleRIPOffsetListEntry.setStatus("current")


class _SleRIPOffsetListIfname_Type(OctetString):
    """Custom type sleRIPOffsetListIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPOffsetListIfname_Type.__name__ = "OctetString"
_SleRIPOffsetListIfname_Object = MibTableColumn
sleRIPOffsetListIfname = _SleRIPOffsetListIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 1, 1, 1),
    _SleRIPOffsetListIfname_Type()
)
sleRIPOffsetListIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListIfname.setStatus("current")


class _SleRIPOffsetListInAccName_Type(OctetString):
    """Custom type sleRIPOffsetListInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPOffsetListInAccName_Type.__name__ = "OctetString"
_SleRIPOffsetListInAccName_Object = MibTableColumn
sleRIPOffsetListInAccName = _SleRIPOffsetListInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 1, 1, 2),
    _SleRIPOffsetListInAccName_Type()
)
sleRIPOffsetListInAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListInAccName.setStatus("current")


class _SleRIPOffsetListInMetric_Type(Integer32):
    """Custom type sleRIPOffsetListInMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPOffsetListInMetric_Type.__name__ = "Integer32"
_SleRIPOffsetListInMetric_Object = MibTableColumn
sleRIPOffsetListInMetric = _SleRIPOffsetListInMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 1, 1, 3),
    _SleRIPOffsetListInMetric_Type()
)
sleRIPOffsetListInMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListInMetric.setStatus("current")


class _SleRIPOffsetListOutAccName_Type(OctetString):
    """Custom type sleRIPOffsetListOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPOffsetListOutAccName_Type.__name__ = "OctetString"
_SleRIPOffsetListOutAccName_Object = MibTableColumn
sleRIPOffsetListOutAccName = _SleRIPOffsetListOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 1, 1, 4),
    _SleRIPOffsetListOutAccName_Type()
)
sleRIPOffsetListOutAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListOutAccName.setStatus("current")


class _SleRIPOffsetListOutMetric_Type(Integer32):
    """Custom type sleRIPOffsetListOutMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPOffsetListOutMetric_Type.__name__ = "Integer32"
_SleRIPOffsetListOutMetric_Object = MibTableColumn
sleRIPOffsetListOutMetric = _SleRIPOffsetListOutMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 1, 1, 5),
    _SleRIPOffsetListOutMetric_Type()
)
sleRIPOffsetListOutMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListOutMetric.setStatus("current")
_SleRIPOffsetListControl_ObjectIdentity = ObjectIdentity
sleRIPOffsetListControl = _SleRIPOffsetListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2)
)


class _SleRIPOffsetListControlRequest_Type(Integer32):
    """Custom type sleRIPOffsetListControlRequest based on Integer32"""
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
        *(("createRIPOffsetListIn", 1),
          ("deleteRIPOffsetListIn", 2),
          ("createRIPOffsetListOut", 3),
          ("deleteRIPOffsetListOut", 4))
    )


_SleRIPOffsetListControlRequest_Type.__name__ = "Integer32"
_SleRIPOffsetListControlRequest_Object = MibScalar
sleRIPOffsetListControlRequest = _SleRIPOffsetListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 1),
    _SleRIPOffsetListControlRequest_Type()
)
sleRIPOffsetListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlRequest.setStatus("current")
_SleRIPOffsetListControlStatus_Type = SleControlStatusType
_SleRIPOffsetListControlStatus_Object = MibScalar
sleRIPOffsetListControlStatus = _SleRIPOffsetListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 2),
    _SleRIPOffsetListControlStatus_Type()
)
sleRIPOffsetListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlStatus.setStatus("current")
_SleRIPOffsetListControlTimer_Type = Gauge32
_SleRIPOffsetListControlTimer_Object = MibScalar
sleRIPOffsetListControlTimer = _SleRIPOffsetListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 3),
    _SleRIPOffsetListControlTimer_Type()
)
sleRIPOffsetListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlTimer.setStatus("current")
_SleRIPOffsetListControlTimeStamp_Type = TimeTicks
_SleRIPOffsetListControlTimeStamp_Object = MibScalar
sleRIPOffsetListControlTimeStamp = _SleRIPOffsetListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 4),
    _SleRIPOffsetListControlTimeStamp_Type()
)
sleRIPOffsetListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlTimeStamp.setStatus("current")
_SleRIPOffsetListControlReqResult_Type = SleControlRequestResultType
_SleRIPOffsetListControlReqResult_Object = MibScalar
sleRIPOffsetListControlReqResult = _SleRIPOffsetListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 5),
    _SleRIPOffsetListControlReqResult_Type()
)
sleRIPOffsetListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlReqResult.setStatus("current")


class _SleRIPOffsetListControlIfname_Type(OctetString):
    """Custom type sleRIPOffsetListControlIfname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPOffsetListControlIfname_Type.__name__ = "OctetString"
_SleRIPOffsetListControlIfname_Object = MibScalar
sleRIPOffsetListControlIfname = _SleRIPOffsetListControlIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 6),
    _SleRIPOffsetListControlIfname_Type()
)
sleRIPOffsetListControlIfname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlIfname.setStatus("current")


class _SleRIPOffsetListControlInAccName_Type(OctetString):
    """Custom type sleRIPOffsetListControlInAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPOffsetListControlInAccName_Type.__name__ = "OctetString"
_SleRIPOffsetListControlInAccName_Object = MibScalar
sleRIPOffsetListControlInAccName = _SleRIPOffsetListControlInAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 7),
    _SleRIPOffsetListControlInAccName_Type()
)
sleRIPOffsetListControlInAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlInAccName.setStatus("current")


class _SleRIPOffsetListControlInMetric_Type(Integer32):
    """Custom type sleRIPOffsetListControlInMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPOffsetListControlInMetric_Type.__name__ = "Integer32"
_SleRIPOffsetListControlInMetric_Object = MibScalar
sleRIPOffsetListControlInMetric = _SleRIPOffsetListControlInMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 8),
    _SleRIPOffsetListControlInMetric_Type()
)
sleRIPOffsetListControlInMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlInMetric.setStatus("current")


class _SleRIPOffsetListControlOutAccName_Type(OctetString):
    """Custom type sleRIPOffsetListControlOutAccName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPOffsetListControlOutAccName_Type.__name__ = "OctetString"
_SleRIPOffsetListControlOutAccName_Object = MibScalar
sleRIPOffsetListControlOutAccName = _SleRIPOffsetListControlOutAccName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 9),
    _SleRIPOffsetListControlOutAccName_Type()
)
sleRIPOffsetListControlOutAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlOutAccName.setStatus("current")


class _SleRIPOffsetListControlOutMetric_Type(Integer32):
    """Custom type sleRIPOffsetListControlOutMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SleRIPOffsetListControlOutMetric_Type.__name__ = "Integer32"
_SleRIPOffsetListControlOutMetric_Object = MibScalar
sleRIPOffsetListControlOutMetric = _SleRIPOffsetListControlOutMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 2, 10),
    _SleRIPOffsetListControlOutMetric_Type()
)
sleRIPOffsetListControlOutMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPOffsetListControlOutMetric.setStatus("current")
_SleRIPOffsetListNotification_ObjectIdentity = ObjectIdentity
sleRIPOffsetListNotification = _SleRIPOffsetListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 3)
)
_SleRIPRedistribute_ObjectIdentity = ObjectIdentity
sleRIPRedistribute = _SleRIPRedistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8)
)
_SleRIPRedistributeTable_Object = MibTable
sleRIPRedistributeTable = _SleRIPRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 1)
)
if mibBuilder.loadTexts:
    sleRIPRedistributeTable.setStatus("current")
_SleRIPRedistributeEntry_Object = MibTableRow
sleRIPRedistributeEntry = _SleRIPRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 1, 1)
)
sleRIPRedistributeEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPRedistType"),
)
if mibBuilder.loadTexts:
    sleRIPRedistributeEntry.setStatus("current")


class _SleRIPRedistType_Type(Integer32):
    """Custom type sleRIPRedistType based on Integer32"""
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


_SleRIPRedistType_Type.__name__ = "Integer32"
_SleRIPRedistType_Object = MibTableColumn
sleRIPRedistType = _SleRIPRedistType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 1, 1, 1),
    _SleRIPRedistType_Type()
)
sleRIPRedistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRedistType.setStatus("current")


class _SleRIPRedistMetric_Type(Integer32):
    """Custom type sleRIPRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleRIPRedistMetric_Type.__name__ = "Integer32"
_SleRIPRedistMetric_Object = MibTableColumn
sleRIPRedistMetric = _SleRIPRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 1, 1, 2),
    _SleRIPRedistMetric_Type()
)
sleRIPRedistMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRedistMetric.setStatus("current")


class _SleRIPRedistRouteMapName_Type(OctetString):
    """Custom type sleRIPRedistRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPRedistRouteMapName_Type.__name__ = "OctetString"
_SleRIPRedistRouteMapName_Object = MibTableColumn
sleRIPRedistRouteMapName = _SleRIPRedistRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 1, 1, 3),
    _SleRIPRedistRouteMapName_Type()
)
sleRIPRedistRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRedistRouteMapName.setStatus("current")
_SleRIPRedistributeControl_ObjectIdentity = ObjectIdentity
sleRIPRedistributeControl = _SleRIPRedistributeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2)
)


class _SleRIPRedistControlRequest_Type(Integer32):
    """Custom type sleRIPRedistControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createRIPRedistribute", 1),
          ("deleteRIPRedistribute", 2),
          ("setRIPRedistribute", 3))
    )


_SleRIPRedistControlRequest_Type.__name__ = "Integer32"
_SleRIPRedistControlRequest_Object = MibScalar
sleRIPRedistControlRequest = _SleRIPRedistControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 1),
    _SleRIPRedistControlRequest_Type()
)
sleRIPRedistControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPRedistControlRequest.setStatus("current")
_SleRIPRedistControlStatus_Type = SleControlStatusType
_SleRIPRedistControlStatus_Object = MibScalar
sleRIPRedistControlStatus = _SleRIPRedistControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 2),
    _SleRIPRedistControlStatus_Type()
)
sleRIPRedistControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRedistControlStatus.setStatus("current")
_SleRIPRedistControlTimer_Type = Gauge32
_SleRIPRedistControlTimer_Object = MibScalar
sleRIPRedistControlTimer = _SleRIPRedistControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 3),
    _SleRIPRedistControlTimer_Type()
)
sleRIPRedistControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPRedistControlTimer.setStatus("current")
_SleRIPRedistControlTimeStamp_Type = TimeTicks
_SleRIPRedistControlTimeStamp_Object = MibScalar
sleRIPRedistControlTimeStamp = _SleRIPRedistControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 4),
    _SleRIPRedistControlTimeStamp_Type()
)
sleRIPRedistControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRedistControlTimeStamp.setStatus("current")
_SleRIPRedistControlReqResult_Type = SleControlRequestResultType
_SleRIPRedistControlReqResult_Object = MibScalar
sleRIPRedistControlReqResult = _SleRIPRedistControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 5),
    _SleRIPRedistControlReqResult_Type()
)
sleRIPRedistControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRedistControlReqResult.setStatus("current")


class _SleRIPRedistControlType_Type(Integer32):
    """Custom type sleRIPRedistControlType based on Integer32"""
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


_SleRIPRedistControlType_Type.__name__ = "Integer32"
_SleRIPRedistControlType_Object = MibScalar
sleRIPRedistControlType = _SleRIPRedistControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 6),
    _SleRIPRedistControlType_Type()
)
sleRIPRedistControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPRedistControlType.setStatus("current")


class _SleRIPRedistControlMetric_Type(Integer32):
    """Custom type sleRIPRedistControlMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleRIPRedistControlMetric_Type.__name__ = "Integer32"
_SleRIPRedistControlMetric_Object = MibScalar
sleRIPRedistControlMetric = _SleRIPRedistControlMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 7),
    _SleRIPRedistControlMetric_Type()
)
sleRIPRedistControlMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPRedistControlMetric.setStatus("current")


class _SleRIPRedistControlRouteMapName_Type(OctetString):
    """Custom type sleRIPRedistControlRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPRedistControlRouteMapName_Type.__name__ = "OctetString"
_SleRIPRedistControlRouteMapName_Object = MibScalar
sleRIPRedistControlRouteMapName = _SleRIPRedistControlRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 2, 8),
    _SleRIPRedistControlRouteMapName_Type()
)
sleRIPRedistControlRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPRedistControlRouteMapName.setStatus("current")
_SleRIPRedistributeNotification_ObjectIdentity = ObjectIdentity
sleRIPRedistributeNotification = _SleRIPRedistributeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 3)
)
_SleRIPPassInterface_ObjectIdentity = ObjectIdentity
sleRIPPassInterface = _SleRIPPassInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9)
)
_SleRIPPassInterfaceTable_Object = MibTable
sleRIPPassInterfaceTable = _SleRIPPassInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 1)
)
if mibBuilder.loadTexts:
    sleRIPPassInterfaceTable.setStatus("current")
_SleRIPPassInterfaceEntry_Object = MibTableRow
sleRIPPassInterfaceEntry = _SleRIPPassInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 1, 1)
)
sleRIPPassInterfaceEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPPassInterfaceName"),
)
if mibBuilder.loadTexts:
    sleRIPPassInterfaceEntry.setStatus("current")


class _SleRIPPassInterfaceName_Type(OctetString):
    """Custom type sleRIPPassInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPPassInterfaceName_Type.__name__ = "OctetString"
_SleRIPPassInterfaceName_Object = MibTableColumn
sleRIPPassInterfaceName = _SleRIPPassInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 1, 1, 1),
    _SleRIPPassInterfaceName_Type()
)
sleRIPPassInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPPassInterfaceName.setStatus("current")
_SleRIPPassInterfaceControl_ObjectIdentity = ObjectIdentity
sleRIPPassInterfaceControl = _SleRIPPassInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 2)
)


class _SleRIPPassInterfaceControlRequest_Type(Integer32):
    """Custom type sleRIPPassInterfaceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPPassInterface", 1),
          ("deleteRIPPassInterface", 2))
    )


_SleRIPPassInterfaceControlRequest_Type.__name__ = "Integer32"
_SleRIPPassInterfaceControlRequest_Object = MibScalar
sleRIPPassInterfaceControlRequest = _SleRIPPassInterfaceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 2, 1),
    _SleRIPPassInterfaceControlRequest_Type()
)
sleRIPPassInterfaceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPPassInterfaceControlRequest.setStatus("current")
_SleRIPPassInterfaceControlStatus_Type = SleControlStatusType
_SleRIPPassInterfaceControlStatus_Object = MibScalar
sleRIPPassInterfaceControlStatus = _SleRIPPassInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 2, 2),
    _SleRIPPassInterfaceControlStatus_Type()
)
sleRIPPassInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPPassInterfaceControlStatus.setStatus("current")
_SleRIPPassInterfaceControlTimer_Type = Gauge32
_SleRIPPassInterfaceControlTimer_Object = MibScalar
sleRIPPassInterfaceControlTimer = _SleRIPPassInterfaceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 2, 3),
    _SleRIPPassInterfaceControlTimer_Type()
)
sleRIPPassInterfaceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPPassInterfaceControlTimer.setStatus("current")
_SleRIPPassInterfaceControlTimeStamp_Type = TimeTicks
_SleRIPPassInterfaceControlTimeStamp_Object = MibScalar
sleRIPPassInterfaceControlTimeStamp = _SleRIPPassInterfaceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 2, 4),
    _SleRIPPassInterfaceControlTimeStamp_Type()
)
sleRIPPassInterfaceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPPassInterfaceControlTimeStamp.setStatus("current")
_SleRIPPassInterfaceControlReqResult_Type = SleControlRequestResultType
_SleRIPPassInterfaceControlReqResult_Object = MibScalar
sleRIPPassInterfaceControlReqResult = _SleRIPPassInterfaceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 2, 5),
    _SleRIPPassInterfaceControlReqResult_Type()
)
sleRIPPassInterfaceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPPassInterfaceControlReqResult.setStatus("current")


class _SleRIPPassInterfaceControlName_Type(OctetString):
    """Custom type sleRIPPassInterfaceControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPPassInterfaceControlName_Type.__name__ = "OctetString"
_SleRIPPassInterfaceControlName_Object = MibScalar
sleRIPPassInterfaceControlName = _SleRIPPassInterfaceControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 2, 6),
    _SleRIPPassInterfaceControlName_Type()
)
sleRIPPassInterfaceControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPPassInterfaceControlName.setStatus("current")
_SleRIPPassInterfaceNotification_ObjectIdentity = ObjectIdentity
sleRIPPassInterfaceNotification = _SleRIPPassInterfaceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 3)
)
_SleRIPInterface_ObjectIdentity = ObjectIdentity
sleRIPInterface = _SleRIPInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10)
)
_SleRIPInterfaceTable_Object = MibTable
sleRIPInterfaceTable = _SleRIPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1)
)
if mibBuilder.loadTexts:
    sleRIPInterfaceTable.setStatus("current")
_SleRIPInterfaceEntry_Object = MibTableRow
sleRIPInterfaceEntry = _SleRIPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1)
)
sleRIPInterfaceEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sleRIPInterfaceEntry.setStatus("current")


class _SleRIPInterfaceIndex_Type(Integer32):
    """Custom type sleRIPInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleRIPInterfaceIndex_Type.__name__ = "Integer32"
_SleRIPInterfaceIndex_Object = MibTableColumn
sleRIPInterfaceIndex = _SleRIPInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 1),
    _SleRIPInterfaceIndex_Type()
)
sleRIPInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceIndex.setStatus("current")


class _SleRIPInterfaceRecvVer_Type(Integer32):
    """Custom type sleRIPInterfaceRecvVer based on Integer32"""
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
        *(("default", 0),
          ("ripv1", 1),
          ("ripv2", 2),
          ("ripv1-ripv2", 3))
    )


_SleRIPInterfaceRecvVer_Type.__name__ = "Integer32"
_SleRIPInterfaceRecvVer_Object = MibTableColumn
sleRIPInterfaceRecvVer = _SleRIPInterfaceRecvVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 2),
    _SleRIPInterfaceRecvVer_Type()
)
sleRIPInterfaceRecvVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceRecvVer.setStatus("current")


class _SleRIPInterfaceRecvPacket_Type(Integer32):
    """Custom type sleRIPInterfaceRecvPacket based on Integer32"""
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


_SleRIPInterfaceRecvPacket_Type.__name__ = "Integer32"
_SleRIPInterfaceRecvPacket_Object = MibTableColumn
sleRIPInterfaceRecvPacket = _SleRIPInterfaceRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 3),
    _SleRIPInterfaceRecvPacket_Type()
)
sleRIPInterfaceRecvPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceRecvPacket.setStatus("current")


class _SleRIPInterfaceSendVer_Type(Integer32):
    """Custom type sleRIPInterfaceSendVer based on Integer32"""
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
        *(("default", 0),
          ("ripv1", 1),
          ("ripv2", 2),
          ("ripv1-ripv2", 3),
          ("ripv1-compatible", 4))
    )


_SleRIPInterfaceSendVer_Type.__name__ = "Integer32"
_SleRIPInterfaceSendVer_Object = MibTableColumn
sleRIPInterfaceSendVer = _SleRIPInterfaceSendVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 4),
    _SleRIPInterfaceSendVer_Type()
)
sleRIPInterfaceSendVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceSendVer.setStatus("current")


class _SleRIPInterfaceSendPacket_Type(Integer32):
    """Custom type sleRIPInterfaceSendPacket based on Integer32"""
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


_SleRIPInterfaceSendPacket_Type.__name__ = "Integer32"
_SleRIPInterfaceSendPacket_Object = MibTableColumn
sleRIPInterfaceSendPacket = _SleRIPInterfaceSendPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 5),
    _SleRIPInterfaceSendPacket_Type()
)
sleRIPInterfaceSendPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceSendPacket.setStatus("current")


class _SleRIPInterfaceSplitHorizonMode_Type(Integer32):
    """Custom type sleRIPInterfaceSplitHorizonMode based on Integer32"""
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


_SleRIPInterfaceSplitHorizonMode_Type.__name__ = "Integer32"
_SleRIPInterfaceSplitHorizonMode_Object = MibTableColumn
sleRIPInterfaceSplitHorizonMode = _SleRIPInterfaceSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 6),
    _SleRIPInterfaceSplitHorizonMode_Type()
)
sleRIPInterfaceSplitHorizonMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceSplitHorizonMode.setStatus("current")


class _SleRIPInterfaceAuthMode_Type(Integer32):
    """Custom type sleRIPInterfaceAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noauth", 0),
          ("text", 1),
          ("md5", 2))
    )


_SleRIPInterfaceAuthMode_Type.__name__ = "Integer32"
_SleRIPInterfaceAuthMode_Object = MibTableColumn
sleRIPInterfaceAuthMode = _SleRIPInterfaceAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 7),
    _SleRIPInterfaceAuthMode_Type()
)
sleRIPInterfaceAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceAuthMode.setStatus("current")


class _SleRIPInterfaceAuthString_Type(OctetString):
    """Custom type sleRIPInterfaceAuthString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPInterfaceAuthString_Type.__name__ = "OctetString"
_SleRIPInterfaceAuthString_Object = MibTableColumn
sleRIPInterfaceAuthString = _SleRIPInterfaceAuthString_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 8),
    _SleRIPInterfaceAuthString_Type()
)
sleRIPInterfaceAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceAuthString.setStatus("current")


class _SleRIPInterfaceAuthKeyChain_Type(OctetString):
    """Custom type sleRIPInterfaceAuthKeyChain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPInterfaceAuthKeyChain_Type.__name__ = "OctetString"
_SleRIPInterfaceAuthKeyChain_Object = MibTableColumn
sleRIPInterfaceAuthKeyChain = _SleRIPInterfaceAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 1, 1, 9),
    _SleRIPInterfaceAuthKeyChain_Type()
)
sleRIPInterfaceAuthKeyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceAuthKeyChain.setStatus("current")
_SleRIPInterfaceControl_ObjectIdentity = ObjectIdentity
sleRIPInterfaceControl = _SleRIPInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2)
)


class _SleRIPInterfaceControlRequest_Type(Integer32):
    """Custom type sleRIPInterfaceControlRequest based on Integer32"""
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
        *(("setRIPInterfaceRecvVer", 1),
          ("setRIPInterfaceRecvPacketEnable", 2),
          ("setRIPInterfaceSendVer", 3),
          ("setRIPInterfaceSendPacketEnable", 4),
          ("setRIPInterfaceSplitHorizonMode", 5),
          ("setRIPInterfaceAuthMode", 6),
          ("setRIPInterfaceAuthString", 7),
          ("setRIPInterfaceAuthKeyChain", 8))
    )


_SleRIPInterfaceControlRequest_Type.__name__ = "Integer32"
_SleRIPInterfaceControlRequest_Object = MibScalar
sleRIPInterfaceControlRequest = _SleRIPInterfaceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 1),
    _SleRIPInterfaceControlRequest_Type()
)
sleRIPInterfaceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlRequest.setStatus("current")
_SleRIPInterfaceControlStatus_Type = SleControlStatusType
_SleRIPInterfaceControlStatus_Object = MibScalar
sleRIPInterfaceControlStatus = _SleRIPInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 2),
    _SleRIPInterfaceControlStatus_Type()
)
sleRIPInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlStatus.setStatus("current")
_SleRIPInterfaceControlTimer_Type = Gauge32
_SleRIPInterfaceControlTimer_Object = MibScalar
sleRIPInterfaceControlTimer = _SleRIPInterfaceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 3),
    _SleRIPInterfaceControlTimer_Type()
)
sleRIPInterfaceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlTimer.setStatus("current")
_SleRIPInterfaceControlTimeStamp_Type = TimeTicks
_SleRIPInterfaceControlTimeStamp_Object = MibScalar
sleRIPInterfaceControlTimeStamp = _SleRIPInterfaceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 4),
    _SleRIPInterfaceControlTimeStamp_Type()
)
sleRIPInterfaceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlTimeStamp.setStatus("current")
_SleRIPInterfaceControlReqResult_Type = SleControlRequestResultType
_SleRIPInterfaceControlReqResult_Object = MibScalar
sleRIPInterfaceControlReqResult = _SleRIPInterfaceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 5),
    _SleRIPInterfaceControlReqResult_Type()
)
sleRIPInterfaceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlReqResult.setStatus("current")


class _SleRIPInterfaceControlIndex_Type(Integer32):
    """Custom type sleRIPInterfaceControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_SleRIPInterfaceControlIndex_Type.__name__ = "Integer32"
_SleRIPInterfaceControlIndex_Object = MibScalar
sleRIPInterfaceControlIndex = _SleRIPInterfaceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 6),
    _SleRIPInterfaceControlIndex_Type()
)
sleRIPInterfaceControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlIndex.setStatus("current")


class _SleRIPInterfaceControlRecvVer_Type(Integer32):
    """Custom type sleRIPInterfaceControlRecvVer based on Integer32"""
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
        *(("default", 0),
          ("ripv1", 1),
          ("ripv2", 2),
          ("ripv1-ripv2", 3))
    )


_SleRIPInterfaceControlRecvVer_Type.__name__ = "Integer32"
_SleRIPInterfaceControlRecvVer_Object = MibScalar
sleRIPInterfaceControlRecvVer = _SleRIPInterfaceControlRecvVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 7),
    _SleRIPInterfaceControlRecvVer_Type()
)
sleRIPInterfaceControlRecvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlRecvVer.setStatus("current")


class _SleRIPInterfaceControlRecvPacket_Type(Integer32):
    """Custom type sleRIPInterfaceControlRecvPacket based on Integer32"""
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


_SleRIPInterfaceControlRecvPacket_Type.__name__ = "Integer32"
_SleRIPInterfaceControlRecvPacket_Object = MibScalar
sleRIPInterfaceControlRecvPacket = _SleRIPInterfaceControlRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 8),
    _SleRIPInterfaceControlRecvPacket_Type()
)
sleRIPInterfaceControlRecvPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlRecvPacket.setStatus("current")


class _SleRIPInterfaceControlSendVer_Type(Integer32):
    """Custom type sleRIPInterfaceControlSendVer based on Integer32"""
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
        *(("default", 0),
          ("ripv1", 1),
          ("ripv2", 2),
          ("ripv1-ripv2", 3),
          ("ripv1-compatible", 4))
    )


_SleRIPInterfaceControlSendVer_Type.__name__ = "Integer32"
_SleRIPInterfaceControlSendVer_Object = MibScalar
sleRIPInterfaceControlSendVer = _SleRIPInterfaceControlSendVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 9),
    _SleRIPInterfaceControlSendVer_Type()
)
sleRIPInterfaceControlSendVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlSendVer.setStatus("current")


class _SleRIPInterfaceControlSendPacket_Type(Integer32):
    """Custom type sleRIPInterfaceControlSendPacket based on Integer32"""
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


_SleRIPInterfaceControlSendPacket_Type.__name__ = "Integer32"
_SleRIPInterfaceControlSendPacket_Object = MibScalar
sleRIPInterfaceControlSendPacket = _SleRIPInterfaceControlSendPacket_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 10),
    _SleRIPInterfaceControlSendPacket_Type()
)
sleRIPInterfaceControlSendPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlSendPacket.setStatus("current")


class _SleRIPInterfaceControlSplitHorizonMode_Type(Integer32):
    """Custom type sleRIPInterfaceControlSplitHorizonMode based on Integer32"""
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


_SleRIPInterfaceControlSplitHorizonMode_Type.__name__ = "Integer32"
_SleRIPInterfaceControlSplitHorizonMode_Object = MibScalar
sleRIPInterfaceControlSplitHorizonMode = _SleRIPInterfaceControlSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 11),
    _SleRIPInterfaceControlSplitHorizonMode_Type()
)
sleRIPInterfaceControlSplitHorizonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlSplitHorizonMode.setStatus("current")


class _SleRIPInterfaceControlAuthMode_Type(Integer32):
    """Custom type sleRIPInterfaceControlAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noauth", 0),
          ("text", 1),
          ("md5", 2))
    )


_SleRIPInterfaceControlAuthMode_Type.__name__ = "Integer32"
_SleRIPInterfaceControlAuthMode_Object = MibScalar
sleRIPInterfaceControlAuthMode = _SleRIPInterfaceControlAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 12),
    _SleRIPInterfaceControlAuthMode_Type()
)
sleRIPInterfaceControlAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlAuthMode.setStatus("current")


class _SleRIPInterfaceControlAuthString_Type(OctetString):
    """Custom type sleRIPInterfaceControlAuthString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPInterfaceControlAuthString_Type.__name__ = "OctetString"
_SleRIPInterfaceControlAuthString_Object = MibScalar
sleRIPInterfaceControlAuthString = _SleRIPInterfaceControlAuthString_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 13),
    _SleRIPInterfaceControlAuthString_Type()
)
sleRIPInterfaceControlAuthString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlAuthString.setStatus("current")


class _SleRIPInterfaceControlAuthKeyChain_Type(OctetString):
    """Custom type sleRIPInterfaceControlAuthKeyChain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleRIPInterfaceControlAuthKeyChain_Type.__name__ = "OctetString"
_SleRIPInterfaceControlAuthKeyChain_Object = MibScalar
sleRIPInterfaceControlAuthKeyChain = _SleRIPInterfaceControlAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 2, 14),
    _SleRIPInterfaceControlAuthKeyChain_Type()
)
sleRIPInterfaceControlAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRIPInterfaceControlAuthKeyChain.setStatus("current")
_SleRIPInterfaceNotification_ObjectIdentity = ObjectIdentity
sleRIPInterfaceNotification = _SleRIPInterfaceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3)
)
_SleRIPRoutes_ObjectIdentity = ObjectIdentity
sleRIPRoutes = _SleRIPRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11)
)
_SleRIPRoutesTable_Object = MibTable
sleRIPRoutesTable = _SleRIPRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1)
)
if mibBuilder.loadTexts:
    sleRIPRoutesTable.setStatus("current")
_SleRIPRoutesEntry_Object = MibTableRow
sleRIPRoutesEntry = _SleRIPRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1)
)
sleRIPRoutesEntry.setIndexNames(
    (0, "SLE-RIP-MIB", "sleRIPRoutesType"),
    (0, "SLE-RIP-MIB", "sleRIPRoutesPrefix"),
    (0, "SLE-RIP-MIB", "sleRIPRoutesMask"),
    (0, "SLE-RIP-MIB", "sleRIPRoutesNextHop"),
    (0, "SLE-RIP-MIB", "sleRIPRoutesMetric"),
)
if mibBuilder.loadTexts:
    sleRIPRoutesEntry.setStatus("current")


class _SleRIPRoutesType_Type(Integer32):
    """Custom type sleRIPRoutesType based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("ripng", 5),
          ("ospf", 6),
          ("ospfv3", 7),
          ("bgp", 8),
          ("isis", 9))
    )


_SleRIPRoutesType_Type.__name__ = "Integer32"
_SleRIPRoutesType_Object = MibTableColumn
sleRIPRoutesType = _SleRIPRoutesType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 1),
    _SleRIPRoutesType_Type()
)
sleRIPRoutesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesType.setStatus("current")
_SleRIPRoutesPrefix_Type = IpAddress
_SleRIPRoutesPrefix_Object = MibTableColumn
sleRIPRoutesPrefix = _SleRIPRoutesPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 2),
    _SleRIPRoutesPrefix_Type()
)
sleRIPRoutesPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesPrefix.setStatus("current")


class _SleRIPRoutesMask_Type(Integer32):
    """Custom type sleRIPRoutesMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleRIPRoutesMask_Type.__name__ = "Integer32"
_SleRIPRoutesMask_Object = MibTableColumn
sleRIPRoutesMask = _SleRIPRoutesMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 3),
    _SleRIPRoutesMask_Type()
)
sleRIPRoutesMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesMask.setStatus("current")
_SleRIPRoutesNextHop_Type = IpAddress
_SleRIPRoutesNextHop_Object = MibTableColumn
sleRIPRoutesNextHop = _SleRIPRoutesNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 4),
    _SleRIPRoutesNextHop_Type()
)
sleRIPRoutesNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesNextHop.setStatus("current")


class _SleRIPRoutesMetric_Type(Integer32):
    """Custom type sleRIPRoutesMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRIPRoutesMetric_Type.__name__ = "Integer32"
_SleRIPRoutesMetric_Object = MibTableColumn
sleRIPRoutesMetric = _SleRIPRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 6),
    _SleRIPRoutesMetric_Type()
)
sleRIPRoutesMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesMetric.setStatus("current")
_SleRIPRoutesNetworkFrom_Type = IpAddress
_SleRIPRoutesNetworkFrom_Object = MibTableColumn
sleRIPRoutesNetworkFrom = _SleRIPRoutesNetworkFrom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 7),
    _SleRIPRoutesNetworkFrom_Type()
)
sleRIPRoutesNetworkFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesNetworkFrom.setStatus("current")
_SleRIPRoutesIfName_Type = OctetString
_SleRIPRoutesIfName_Object = MibTableColumn
sleRIPRoutesIfName = _SleRIPRoutesIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 8),
    _SleRIPRoutesIfName_Type()
)
sleRIPRoutesIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesIfName.setStatus("current")
_SleRIPRoutesUpTime_Type = TimeTicks
_SleRIPRoutesUpTime_Object = MibTableColumn
sleRIPRoutesUpTime = _SleRIPRoutesUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 11, 1, 1, 9),
    _SleRIPRoutesUpTime_Type()
)
sleRIPRoutesUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRIPRoutesUpTime.setStatus("current")

# Managed Objects groups

sleRIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 12)
)
sleRIPGroup.setObjects(
      *(("SLE-RIP-MIB", "sleRIPVersion"),
        ("SLE-RIP-MIB", "sleRIPDefaultMetric"),
        ("SLE-RIP-MIB", "sleRIPDefaultInformationOrg"),
        ("SLE-RIP-MIB", "sleRIPDefaultDistance"),
        ("SLE-RIP-MIB", "sleRIPRecvBufferSize"),
        ("SLE-RIP-MIB", "sleRIPMaximumPaths"),
        ("SLE-RIP-MIB", "sleRIPMaximumPrefixRoute"),
        ("SLE-RIP-MIB", "sleRIPMaximumPrefixRoutePercent"),
        ("SLE-RIP-MIB", "sleRIPMetricSumApply"),
        ("SLE-RIP-MIB", "sleRIPBasicUpdateTimer"),
        ("SLE-RIP-MIB", "sleRIPBasicTimeoutTimer"),
        ("SLE-RIP-MIB", "sleRIPBasicGarbageTimer"),
        ("SLE-RIP-MIB", "sleRIPRestartPeriod"),
        ("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlStatus"),
        ("SLE-RIP-MIB", "sleRIPControlTimer"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPControlVersion"),
        ("SLE-RIP-MIB", "sleRIPControlDefaultMetric"),
        ("SLE-RIP-MIB", "sleRIPControlDefaultInformationOrg"),
        ("SLE-RIP-MIB", "sleRIPControlDefaultDistance"),
        ("SLE-RIP-MIB", "sleRIPControlRecvBufferSize"),
        ("SLE-RIP-MIB", "sleRIPControlMaximumPaths"),
        ("SLE-RIP-MIB", "sleRIPControlMaximumPrefixRoute"),
        ("SLE-RIP-MIB", "sleRIPControlMaximumPrefixRoutePercent"),
        ("SLE-RIP-MIB", "sleRIPControlMetricSumApply"),
        ("SLE-RIP-MIB", "sleRIPControlBasicUpdateTimer"),
        ("SLE-RIP-MIB", "sleRIPControlBasicTimeoutTimer"),
        ("SLE-RIP-MIB", "sleRIPControlBasicGarbageTimer"),
        ("SLE-RIP-MIB", "sleRIPControlRestartPeriod"),
        ("SLE-RIP-MIB", "sleRIPControlClearRoutePrefix"),
        ("SLE-RIP-MIB", "sleRIPControlClearRouteMask"),
        ("SLE-RIP-MIB", "sleRIPControlClearProtoTpye"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPAddr"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPMask"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlStatus"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlTimer"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlIPAddr"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlIPMask"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceName"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlStatus"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlTimer"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlName"),
        ("SLE-RIP-MIB", "sleRIPNeighborIPAddr"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlStatus"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlTimer"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlIPAddr"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteIPAddr"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteIPMask"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlRequest"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlStatus"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlTimer"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlIPAddr"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlIPMask"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceValue"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceAddr"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceMask"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceAccessName"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlStatus"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlTimer"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlValue"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlAddr"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlMask"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlAccessName"),
        ("SLE-RIP-MIB", "sleRIPDistributeIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeInAccessName"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutAccessName"),
        ("SLE-RIP-MIB", "sleRIPDistributeInPrefixName"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutPrefixName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlStatus"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimer"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlInAccessName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlOutAccessName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlInPrefixName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlOutPrefixName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListIfname"),
        ("SLE-RIP-MIB", "sleRIPOffsetListInAccName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListInMetric"),
        ("SLE-RIP-MIB", "sleRIPOffsetListOutAccName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListOutMetric"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlRequest"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlStatus"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlTimer"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlIfname"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlInAccName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlInMetric"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlOutAccName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlOutMetric"),
        ("SLE-RIP-MIB", "sleRIPRedistType"),
        ("SLE-RIP-MIB", "sleRIPRedistMetric"),
        ("SLE-RIP-MIB", "sleRIPRedistRouteMapName"),
        ("SLE-RIP-MIB", "sleRIPRedistControlRequest"),
        ("SLE-RIP-MIB", "sleRIPRedistControlStatus"),
        ("SLE-RIP-MIB", "sleRIPRedistControlTimer"),
        ("SLE-RIP-MIB", "sleRIPRedistControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPRedistControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPRedistControlType"),
        ("SLE-RIP-MIB", "sleRIPRedistControlMetric"),
        ("SLE-RIP-MIB", "sleRIPRedistControlRouteMapName"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceName"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlStatus"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlTimer"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlName"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceRecvVer"),
        ("SLE-RIP-MIB", "sleRIPInterfaceRecvPacket"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSendVer"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSendPacket"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSplitHorizonMode"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthMode"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthString"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthKeyChain"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlStatus"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimer"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlRecvVer"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlRecvPacket"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlSendVer"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlSendPacket"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlSplitHorizonMode"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlAuthMode"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlAuthString"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlAuthKeyChain"),
        ("SLE-RIP-MIB", "sleRIPRoutesType"),
        ("SLE-RIP-MIB", "sleRIPRoutesPrefix"),
        ("SLE-RIP-MIB", "sleRIPRoutesMask"),
        ("SLE-RIP-MIB", "sleRIPRoutesNextHop"),
        ("SLE-RIP-MIB", "sleRIPRoutesMetric"),
        ("SLE-RIP-MIB", "sleRIPRoutesNetworkFrom"),
        ("SLE-RIP-MIB", "sleRIPRoutesIfName"),
        ("SLE-RIP-MIB", "sleRIPRoutesUpTime"))
)
if mibBuilder.loadTexts:
    sleRIPGroup.setStatus("current")


# Notification objects

sleRIPModeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 1)
)
sleRIPModeCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRIPModeCreated.setStatus(
        "current"
    )

sleRIPModeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 2)
)
sleRIPModeDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRIPModeDeleted.setStatus(
        "current"
    )

sleRIPVersionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 3)
)
sleRIPVersionChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPVersion"))
)
if mibBuilder.loadTexts:
    sleRIPVersionChanged.setStatus(
        "current"
    )

sleRIPDefaultMetricChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 4)
)
sleRIPDefaultMetricChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDefaultMetric"))
)
if mibBuilder.loadTexts:
    sleRIPDefaultMetricChanged.setStatus(
        "current"
    )

sleRIPDefaultInformationOrgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 5)
)
sleRIPDefaultInformationOrgChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDefaultInformationOrg"))
)
if mibBuilder.loadTexts:
    sleRIPDefaultInformationOrgChanged.setStatus(
        "current"
    )

sleRIPDefaultDistanceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 6)
)
sleRIPDefaultDistanceChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDefaultDistance"))
)
if mibBuilder.loadTexts:
    sleRIPDefaultDistanceChanged.setStatus(
        "current"
    )

sleRIPRecvBufferSizeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 7)
)
sleRIPRecvBufferSizeChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPRecvBufferSize"))
)
if mibBuilder.loadTexts:
    sleRIPRecvBufferSizeChanged.setStatus(
        "current"
    )

sleRIPMaximumPathsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 8)
)
sleRIPMaximumPathsChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPMaximumPaths"))
)
if mibBuilder.loadTexts:
    sleRIPMaximumPathsChanged.setStatus(
        "current"
    )

sleRIPMaximumPrefixProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 9)
)
sleRIPMaximumPrefixProfileChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPMaximumPrefixRoute"),
        ("SLE-RIP-MIB", "sleRIPMaximumPrefixRoutePercent"))
)
if mibBuilder.loadTexts:
    sleRIPMaximumPrefixProfileChanged.setStatus(
        "current"
    )

sleRIPMetricSumApplyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 10)
)
sleRIPMetricSumApplyChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPMetricSumApply"))
)
if mibBuilder.loadTexts:
    sleRIPMetricSumApplyChanged.setStatus(
        "current"
    )

sleRIPTimersChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 11)
)
sleRIPTimersChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPBasicUpdateTimer"),
        ("SLE-RIP-MIB", "sleRIPBasicTimeoutTimer"),
        ("SLE-RIP-MIB", "sleRIPBasicGarbageTimer"))
)
if mibBuilder.loadTexts:
    sleRIPTimersChanged.setStatus(
        "current"
    )

sleRIPRestartPeriodChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 12)
)
sleRIPRestartPeriodChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPRestartPeriod"))
)
if mibBuilder.loadTexts:
    sleRIPRestartPeriodChanged.setStatus(
        "current"
    )

sleRIPRestartRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 13)
)
sleRIPRestartRemoved.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPControlRestartPeriod"))
)
if mibBuilder.loadTexts:
    sleRIPRestartRemoved.setStatus(
        "current"
    )

sleRIPAllCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 14)
)
sleRIPAllCleared.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRIPAllCleared.setStatus(
        "current"
    )

sleRIPRouteCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 15)
)
sleRIPRouteCleared.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPControlClearRoutePrefix"),
        ("SLE-RIP-MIB", "sleRIPControlClearRouteMask"))
)
if mibBuilder.loadTexts:
    sleRIPRouteCleared.setStatus(
        "current"
    )

sleRIPProtoTypeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 1, 3, 16)
)
sleRIPProtoTypeCleared.setObjects(
      *(("SLE-RIP-MIB", "sleRIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPControlClearProtoTpye"))
)
if mibBuilder.loadTexts:
    sleRIPProtoTypeCleared.setStatus(
        "current"
    )

sleRIPNetworkIPCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 3, 1)
)
sleRIPNetworkIPCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPNetworkIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPAddr"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPMask"))
)
if mibBuilder.loadTexts:
    sleRIPNetworkIPCreated.setStatus(
        "current"
    )

sleRIPNetworkIPDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 1, 3, 2)
)
sleRIPNetworkIPDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPNetworkIPControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlIPAddr"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPControlIPMask"))
)
if mibBuilder.loadTexts:
    sleRIPNetworkIPDeleted.setStatus(
        "current"
    )

sleRIPNetworkInterfaceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 3, 1)
)
sleRIPNetworkInterfaceCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceName"))
)
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceCreated.setStatus(
        "current"
    )

sleRIPNetworkInterfaceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 2, 2, 3, 2)
)
sleRIPNetworkInterfaceDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceControlName"))
)
if mibBuilder.loadTexts:
    sleRIPNetworkInterfaceDeleted.setStatus(
        "current"
    )

sleRIPNeighborCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 3, 1)
)
sleRIPNeighborCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPNeighborControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNeighborIPAddr"))
)
if mibBuilder.loadTexts:
    sleRIPNeighborCreated.setStatus(
        "current"
    )

sleRIPNeighborDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 3, 3, 2)
)
sleRIPNeighborDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPNeighborControlRequest"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPNeighborControlIPAddr"))
)
if mibBuilder.loadTexts:
    sleRIPNeighborDeleted.setStatus(
        "current"
    )

sleRIPStaticRouteCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 3, 1)
)
sleRIPStaticRouteCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPStaticRouteControlRequest"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteIPAddr"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteIPMask"))
)
if mibBuilder.loadTexts:
    sleRIPStaticRouteCreated.setStatus(
        "current"
    )

sleRIPStaticRouteDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 4, 3, 2)
)
sleRIPStaticRouteDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPStaticRouteControlRequest"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlIPAddr"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteControlIPMask"))
)
if mibBuilder.loadTexts:
    sleRIPStaticRouteDeleted.setStatus(
        "current"
    )

sleRIPAdminDistanceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 3, 1)
)
sleRIPAdminDistanceCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPAdminDistanceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceValue"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceAddr"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceMask"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPAdminDistanceCreated.setStatus(
        "current"
    )

sleRIPAdminDistanceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 5, 3, 2)
)
sleRIPAdminDistanceDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPAdminDistanceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlValue"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlAddr"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlMask"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceControlAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPAdminDistanceDeleted.setStatus(
        "current"
    )

sleRIPDistributeInAccessCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 1)
)
sleRIPDistributeInAccessCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeInAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeInAccessCreated.setStatus(
        "current"
    )

sleRIPDistributeInAccessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 2)
)
sleRIPDistributeInAccessDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlInAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeInAccessDeleted.setStatus(
        "current"
    )

sleRIPDistributeOutAccessCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 3)
)
sleRIPDistributeOutAccessCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeOutAccessCreated.setStatus(
        "current"
    )

sleRIPDistributeOutAccessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 4)
)
sleRIPDistributeOutAccessDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlOutAccessName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeOutAccessDeleted.setStatus(
        "current"
    )

sleRIPDistributeInPrefixCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 5)
)
sleRIPDistributeInPrefixCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeInPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeInPrefixCreated.setStatus(
        "current"
    )

sleRIPDistributeInPrefixDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 6)
)
sleRIPDistributeInPrefixDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlInPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeInPrefixDeleted.setStatus(
        "current"
    )

sleRIPDistributeOutPrefixCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 7)
)
sleRIPDistributeOutPrefixCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeOutPrefixCreated.setStatus(
        "current"
    )

sleRIPDistributeOutPrefixDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 6, 3, 8)
)
sleRIPDistributeOutPrefixDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPDistributeControlRequest"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlIfName"),
        ("SLE-RIP-MIB", "sleRIPDistributeControlOutPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPDistributeOutPrefixDeleted.setStatus(
        "current"
    )

sleRIPOffsetListCreatedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 3, 1)
)
sleRIPOffsetListCreatedIn.setObjects(
      *(("SLE-RIP-MIB", "sleRIPOffsetListControlRequest"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPOffsetListIfname"),
        ("SLE-RIP-MIB", "sleRIPOffsetListInAccName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListInMetric"))
)
if mibBuilder.loadTexts:
    sleRIPOffsetListCreatedIn.setStatus(
        "current"
    )

sleRIPOffsetListDeletedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 3, 2)
)
sleRIPOffsetListDeletedIn.setObjects(
      *(("SLE-RIP-MIB", "sleRIPOffsetListControlRequest"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlIfname"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlInAccName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlInMetric"))
)
if mibBuilder.loadTexts:
    sleRIPOffsetListDeletedIn.setStatus(
        "current"
    )

sleRIPOffsetListCreatedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 3, 3)
)
sleRIPOffsetListCreatedOut.setObjects(
      *(("SLE-RIP-MIB", "sleRIPOffsetListControlRequest"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPOffsetListIfname"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutAccessName"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutPrefixName"))
)
if mibBuilder.loadTexts:
    sleRIPOffsetListCreatedOut.setStatus(
        "current"
    )

sleRIPOffsetListDeletedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 7, 3, 4)
)
sleRIPOffsetListDeletedOut.setObjects(
      *(("SLE-RIP-MIB", "sleRIPOffsetListControlRequest"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlIfname"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlOutAccName"),
        ("SLE-RIP-MIB", "sleRIPOffsetListControlOutMetric"))
)
if mibBuilder.loadTexts:
    sleRIPOffsetListDeletedOut.setStatus(
        "current"
    )

sleRIPRedistributeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 3, 1)
)
sleRIPRedistributeCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPRedistControlRequest"),
        ("SLE-RIP-MIB", "sleRIPRedistControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPRedistControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPRedistType"),
        ("SLE-RIP-MIB", "sleRIPRedistMetric"),
        ("SLE-RIP-MIB", "sleRIPRedistRouteMapName"))
)
if mibBuilder.loadTexts:
    sleRIPRedistributeCreated.setStatus(
        "current"
    )

sleRIPRedistributeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 3, 2)
)
sleRIPRedistributeDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPRedistControlRequest"),
        ("SLE-RIP-MIB", "sleRIPRedistControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPRedistControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPRedistControlType"))
)
if mibBuilder.loadTexts:
    sleRIPRedistributeDeleted.setStatus(
        "current"
    )

sleRIPRedistributeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 8, 3, 3)
)
sleRIPRedistributeChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPRedistControlRequest"),
        ("SLE-RIP-MIB", "sleRIPRedistControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPRedistControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPRedistType"),
        ("SLE-RIP-MIB", "sleRIPRedistMetric"),
        ("SLE-RIP-MIB", "sleRIPRedistRouteMapName"))
)
if mibBuilder.loadTexts:
    sleRIPRedistributeChanged.setStatus(
        "current"
    )

sleRIPPassInterfaceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 3, 1)
)
sleRIPPassInterfaceCreated.setObjects(
      *(("SLE-RIP-MIB", "sleRIPPassInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceName"))
)
if mibBuilder.loadTexts:
    sleRIPPassInterfaceCreated.setStatus(
        "current"
    )

sleRIPPassInterfaceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 9, 3, 2)
)
sleRIPPassInterfaceDeleted.setObjects(
      *(("SLE-RIP-MIB", "sleRIPPassInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceControlName"))
)
if mibBuilder.loadTexts:
    sleRIPPassInterfaceDeleted.setStatus(
        "current"
    )

sleRIPInterfaceRecvVerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 1)
)
sleRIPInterfaceRecvVerChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceRecvVer"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceRecvVerChanged.setStatus(
        "current"
    )

sleRIPInterfaceRecvPacketChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 2)
)
sleRIPInterfaceRecvPacketChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceRecvPacket"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceRecvPacketChanged.setStatus(
        "current"
    )

sleRIPInterfaceSendVerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 3)
)
sleRIPInterfaceSendVerChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSendVer"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceSendVerChanged.setStatus(
        "current"
    )

sleRIPInterfaceSendPacketChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 4)
)
sleRIPInterfaceSendPacketChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSendPacket"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceSendPacketChanged.setStatus(
        "current"
    )

sleRIPInterfaceSplitHorizonModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 5)
)
sleRIPInterfaceSplitHorizonModeChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSplitHorizonMode"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceSplitHorizonModeChanged.setStatus(
        "current"
    )

sleRIPInterfaceAuthModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 6)
)
sleRIPInterfaceAuthModeChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthMode"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceAuthModeChanged.setStatus(
        "current"
    )

sleRIPInterfaceAuthStringChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 7)
)
sleRIPInterfaceAuthStringChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthString"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceAuthStringChanged.setStatus(
        "current"
    )

sleRIPInterfaceAuthKeyChainChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 10, 3, 8)
)
sleRIPInterfaceAuthKeyChainChanged.setObjects(
      *(("SLE-RIP-MIB", "sleRIPInterfaceControlRequest"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlTimeStamp"),
        ("SLE-RIP-MIB", "sleRIPInterfaceControlReqResult"),
        ("SLE-RIP-MIB", "sleRIPInterfaceIndex"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthKeyChain"))
)
if mibBuilder.loadTexts:
    sleRIPInterfaceAuthKeyChainChanged.setStatus(
        "current"
    )


# Notifications groups

sleRIPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 54, 13)
)
sleRIPNotificationGroup.setObjects(
      *(("SLE-RIP-MIB", "sleRIPModeCreated"),
        ("SLE-RIP-MIB", "sleRIPModeDeleted"),
        ("SLE-RIP-MIB", "sleRIPVersionChanged"),
        ("SLE-RIP-MIB", "sleRIPDefaultMetricChanged"),
        ("SLE-RIP-MIB", "sleRIPDefaultInformationOrgChanged"),
        ("SLE-RIP-MIB", "sleRIPDefaultDistanceChanged"),
        ("SLE-RIP-MIB", "sleRIPRecvBufferSizeChanged"),
        ("SLE-RIP-MIB", "sleRIPMaximumPathsChanged"),
        ("SLE-RIP-MIB", "sleRIPMaximumPrefixProfileChanged"),
        ("SLE-RIP-MIB", "sleRIPMetricSumApplyChanged"),
        ("SLE-RIP-MIB", "sleRIPTimersChanged"),
        ("SLE-RIP-MIB", "sleRIPRestartPeriodChanged"),
        ("SLE-RIP-MIB", "sleRIPRestartRemoved"),
        ("SLE-RIP-MIB", "sleRIPAllCleared"),
        ("SLE-RIP-MIB", "sleRIPRouteCleared"),
        ("SLE-RIP-MIB", "sleRIPProtoTypeCleared"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPCreated"),
        ("SLE-RIP-MIB", "sleRIPNetworkIPDeleted"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceCreated"),
        ("SLE-RIP-MIB", "sleRIPNetworkInterfaceDeleted"),
        ("SLE-RIP-MIB", "sleRIPNeighborCreated"),
        ("SLE-RIP-MIB", "sleRIPNeighborDeleted"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteCreated"),
        ("SLE-RIP-MIB", "sleRIPStaticRouteDeleted"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceCreated"),
        ("SLE-RIP-MIB", "sleRIPAdminDistanceDeleted"),
        ("SLE-RIP-MIB", "sleRIPDistributeInAccessCreated"),
        ("SLE-RIP-MIB", "sleRIPDistributeInAccessDeleted"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutAccessCreated"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutAccessDeleted"),
        ("SLE-RIP-MIB", "sleRIPDistributeInPrefixCreated"),
        ("SLE-RIP-MIB", "sleRIPDistributeInPrefixDeleted"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutPrefixCreated"),
        ("SLE-RIP-MIB", "sleRIPDistributeOutPrefixDeleted"),
        ("SLE-RIP-MIB", "sleRIPOffsetListCreatedIn"),
        ("SLE-RIP-MIB", "sleRIPOffsetListDeletedIn"),
        ("SLE-RIP-MIB", "sleRIPOffsetListCreatedOut"),
        ("SLE-RIP-MIB", "sleRIPOffsetListDeletedOut"),
        ("SLE-RIP-MIB", "sleRIPRedistributeCreated"),
        ("SLE-RIP-MIB", "sleRIPRedistributeDeleted"),
        ("SLE-RIP-MIB", "sleRIPRedistributeChanged"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceCreated"),
        ("SLE-RIP-MIB", "sleRIPPassInterfaceDeleted"),
        ("SLE-RIP-MIB", "sleRIPInterfaceRecvVerChanged"),
        ("SLE-RIP-MIB", "sleRIPInterfaceRecvPacketChanged"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSendVerChanged"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSendPacketChanged"),
        ("SLE-RIP-MIB", "sleRIPInterfaceSplitHorizonModeChanged"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthModeChanged"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthStringChanged"),
        ("SLE-RIP-MIB", "sleRIPInterfaceAuthKeyChainChanged"))
)
if mibBuilder.loadTexts:
    sleRIPNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-RIP-MIB",
    **{"sleRIP": sleRIP,
       "sleRIPBase": sleRIPBase,
       "sleRIPBaseInfo": sleRIPBaseInfo,
       "sleRIPVersion": sleRIPVersion,
       "sleRIPDefaultMetric": sleRIPDefaultMetric,
       "sleRIPDefaultInformationOrg": sleRIPDefaultInformationOrg,
       "sleRIPDefaultDistance": sleRIPDefaultDistance,
       "sleRIPRecvBufferSize": sleRIPRecvBufferSize,
       "sleRIPMaximumPaths": sleRIPMaximumPaths,
       "sleRIPMaximumPrefixRoute": sleRIPMaximumPrefixRoute,
       "sleRIPMaximumPrefixRoutePercent": sleRIPMaximumPrefixRoutePercent,
       "sleRIPMetricSumApply": sleRIPMetricSumApply,
       "sleRIPBasicUpdateTimer": sleRIPBasicUpdateTimer,
       "sleRIPBasicTimeoutTimer": sleRIPBasicTimeoutTimer,
       "sleRIPBasicGarbageTimer": sleRIPBasicGarbageTimer,
       "sleRIPRestartPeriod": sleRIPRestartPeriod,
       "sleRIPBaseControl": sleRIPBaseControl,
       "sleRIPControlRequest": sleRIPControlRequest,
       "sleRIPControlStatus": sleRIPControlStatus,
       "sleRIPControlTimer": sleRIPControlTimer,
       "sleRIPControlTimeStamp": sleRIPControlTimeStamp,
       "sleRIPControlReqResult": sleRIPControlReqResult,
       "sleRIPControlVersion": sleRIPControlVersion,
       "sleRIPControlDefaultMetric": sleRIPControlDefaultMetric,
       "sleRIPControlDefaultInformationOrg": sleRIPControlDefaultInformationOrg,
       "sleRIPControlDefaultDistance": sleRIPControlDefaultDistance,
       "sleRIPControlRecvBufferSize": sleRIPControlRecvBufferSize,
       "sleRIPControlMaximumPaths": sleRIPControlMaximumPaths,
       "sleRIPControlMaximumPrefixRoute": sleRIPControlMaximumPrefixRoute,
       "sleRIPControlMaximumPrefixRoutePercent": sleRIPControlMaximumPrefixRoutePercent,
       "sleRIPControlMetricSumApply": sleRIPControlMetricSumApply,
       "sleRIPControlBasicUpdateTimer": sleRIPControlBasicUpdateTimer,
       "sleRIPControlBasicTimeoutTimer": sleRIPControlBasicTimeoutTimer,
       "sleRIPControlBasicGarbageTimer": sleRIPControlBasicGarbageTimer,
       "sleRIPControlRestartPeriod": sleRIPControlRestartPeriod,
       "sleRIPControlClearRoutePrefix": sleRIPControlClearRoutePrefix,
       "sleRIPControlClearRouteMask": sleRIPControlClearRouteMask,
       "sleRIPControlClearProtoTpye": sleRIPControlClearProtoTpye,
       "sleRIPBaseNotification": sleRIPBaseNotification,
       "sleRIPModeCreated": sleRIPModeCreated,
       "sleRIPModeDeleted": sleRIPModeDeleted,
       "sleRIPVersionChanged": sleRIPVersionChanged,
       "sleRIPDefaultMetricChanged": sleRIPDefaultMetricChanged,
       "sleRIPDefaultInformationOrgChanged": sleRIPDefaultInformationOrgChanged,
       "sleRIPDefaultDistanceChanged": sleRIPDefaultDistanceChanged,
       "sleRIPRecvBufferSizeChanged": sleRIPRecvBufferSizeChanged,
       "sleRIPMaximumPathsChanged": sleRIPMaximumPathsChanged,
       "sleRIPMaximumPrefixProfileChanged": sleRIPMaximumPrefixProfileChanged,
       "sleRIPMetricSumApplyChanged": sleRIPMetricSumApplyChanged,
       "sleRIPTimersChanged": sleRIPTimersChanged,
       "sleRIPRestartPeriodChanged": sleRIPRestartPeriodChanged,
       "sleRIPRestartRemoved": sleRIPRestartRemoved,
       "sleRIPAllCleared": sleRIPAllCleared,
       "sleRIPRouteCleared": sleRIPRouteCleared,
       "sleRIPProtoTypeCleared": sleRIPProtoTypeCleared,
       "sleRIPNetwork": sleRIPNetwork,
       "sleRIPNetworkIP": sleRIPNetworkIP,
       "sleRIPNetworkIPTable": sleRIPNetworkIPTable,
       "sleRIPNetworkIPEntry": sleRIPNetworkIPEntry,
       "sleRIPNetworkIPAddr": sleRIPNetworkIPAddr,
       "sleRIPNetworkIPMask": sleRIPNetworkIPMask,
       "sleRIPNetworkIPControl": sleRIPNetworkIPControl,
       "sleRIPNetworkIPControlRequest": sleRIPNetworkIPControlRequest,
       "sleRIPNetworkIPControlStatus": sleRIPNetworkIPControlStatus,
       "sleRIPNetworkIPControlTimer": sleRIPNetworkIPControlTimer,
       "sleRIPNetworkIPControlTimeStamp": sleRIPNetworkIPControlTimeStamp,
       "sleRIPNetworkIPControlReqResult": sleRIPNetworkIPControlReqResult,
       "sleRIPNetworkIPControlIPAddr": sleRIPNetworkIPControlIPAddr,
       "sleRIPNetworkIPControlIPMask": sleRIPNetworkIPControlIPMask,
       "sleRIPNetworkIPNotification": sleRIPNetworkIPNotification,
       "sleRIPNetworkIPCreated": sleRIPNetworkIPCreated,
       "sleRIPNetworkIPDeleted": sleRIPNetworkIPDeleted,
       "sleRIPNetworkInterface": sleRIPNetworkInterface,
       "sleRIPNetworkInterfaceTable": sleRIPNetworkInterfaceTable,
       "sleRIPNetworkInterfaceEntry": sleRIPNetworkInterfaceEntry,
       "sleRIPNetworkInterfaceName": sleRIPNetworkInterfaceName,
       "sleRIPNetworkInterfaceControl": sleRIPNetworkInterfaceControl,
       "sleRIPNetworkInterfaceControlRequest": sleRIPNetworkInterfaceControlRequest,
       "sleRIPNetworkInterfaceControlStatus": sleRIPNetworkInterfaceControlStatus,
       "sleRIPNetworkInterfaceControlTimer": sleRIPNetworkInterfaceControlTimer,
       "sleRIPNetworkInterfaceControlTimeStamp": sleRIPNetworkInterfaceControlTimeStamp,
       "sleRIPNetworkInterfaceControlReqResult": sleRIPNetworkInterfaceControlReqResult,
       "sleRIPNetworkInterfaceControlName": sleRIPNetworkInterfaceControlName,
       "sleRIPNetworkInterfaceNotification": sleRIPNetworkInterfaceNotification,
       "sleRIPNetworkInterfaceCreated": sleRIPNetworkInterfaceCreated,
       "sleRIPNetworkInterfaceDeleted": sleRIPNetworkInterfaceDeleted,
       "sleRIPNeighbor": sleRIPNeighbor,
       "sleRIPNeighborTable": sleRIPNeighborTable,
       "sleRIPNeighborEntry": sleRIPNeighborEntry,
       "sleRIPNeighborIPAddr": sleRIPNeighborIPAddr,
       "sleRIPNeighborControl": sleRIPNeighborControl,
       "sleRIPNeighborControlRequest": sleRIPNeighborControlRequest,
       "sleRIPNeighborControlStatus": sleRIPNeighborControlStatus,
       "sleRIPNeighborControlTimer": sleRIPNeighborControlTimer,
       "sleRIPNeighborControlTimeStamp": sleRIPNeighborControlTimeStamp,
       "sleRIPNeighborControlReqResult": sleRIPNeighborControlReqResult,
       "sleRIPNeighborControlIPAddr": sleRIPNeighborControlIPAddr,
       "sleRIPNeighborNotification": sleRIPNeighborNotification,
       "sleRIPNeighborCreated": sleRIPNeighborCreated,
       "sleRIPNeighborDeleted": sleRIPNeighborDeleted,
       "sleRIPStaticRoute": sleRIPStaticRoute,
       "sleRIPStaticRouteTable": sleRIPStaticRouteTable,
       "sleRIPStaticRouteEntry": sleRIPStaticRouteEntry,
       "sleRIPStaticRouteIPAddr": sleRIPStaticRouteIPAddr,
       "sleRIPStaticRouteIPMask": sleRIPStaticRouteIPMask,
       "sleRIPStaticRouteControl": sleRIPStaticRouteControl,
       "sleRIPStaticRouteControlRequest": sleRIPStaticRouteControlRequest,
       "sleRIPStaticRouteControlStatus": sleRIPStaticRouteControlStatus,
       "sleRIPStaticRouteControlTimer": sleRIPStaticRouteControlTimer,
       "sleRIPStaticRouteControlTimeStamp": sleRIPStaticRouteControlTimeStamp,
       "sleRIPStaticRouteControlReqResult": sleRIPStaticRouteControlReqResult,
       "sleRIPStaticRouteControlIPAddr": sleRIPStaticRouteControlIPAddr,
       "sleRIPStaticRouteControlIPMask": sleRIPStaticRouteControlIPMask,
       "sleRIPStaticRouteNotification": sleRIPStaticRouteNotification,
       "sleRIPStaticRouteCreated": sleRIPStaticRouteCreated,
       "sleRIPStaticRouteDeleted": sleRIPStaticRouteDeleted,
       "sleRIPAdminDistance": sleRIPAdminDistance,
       "sleRIPAdminDistanceTable": sleRIPAdminDistanceTable,
       "sleRIPAdminDistanceEntry": sleRIPAdminDistanceEntry,
       "sleRIPAdminDistanceValue": sleRIPAdminDistanceValue,
       "sleRIPAdminDistanceAddr": sleRIPAdminDistanceAddr,
       "sleRIPAdminDistanceMask": sleRIPAdminDistanceMask,
       "sleRIPAdminDistanceAccessName": sleRIPAdminDistanceAccessName,
       "sleRIPAdminDistanceControl": sleRIPAdminDistanceControl,
       "sleRIPAdminDistanceControlRequest": sleRIPAdminDistanceControlRequest,
       "sleRIPAdminDistanceControlStatus": sleRIPAdminDistanceControlStatus,
       "sleRIPAdminDistanceControlTimer": sleRIPAdminDistanceControlTimer,
       "sleRIPAdminDistanceControlTimeStamp": sleRIPAdminDistanceControlTimeStamp,
       "sleRIPAdminDistanceControlReqResult": sleRIPAdminDistanceControlReqResult,
       "sleRIPAdminDistanceControlValue": sleRIPAdminDistanceControlValue,
       "sleRIPAdminDistanceControlAddr": sleRIPAdminDistanceControlAddr,
       "sleRIPAdminDistanceControlMask": sleRIPAdminDistanceControlMask,
       "sleRIPAdminDistanceControlAccessName": sleRIPAdminDistanceControlAccessName,
       "sleRIPAdminDistanceNotification": sleRIPAdminDistanceNotification,
       "sleRIPAdminDistanceCreated": sleRIPAdminDistanceCreated,
       "sleRIPAdminDistanceDeleted": sleRIPAdminDistanceDeleted,
       "sleRIPDistribute": sleRIPDistribute,
       "sleRIPDistributeTable": sleRIPDistributeTable,
       "sleRIPDistributeEntry": sleRIPDistributeEntry,
       "sleRIPDistributeIfName": sleRIPDistributeIfName,
       "sleRIPDistributeInAccessName": sleRIPDistributeInAccessName,
       "sleRIPDistributeOutAccessName": sleRIPDistributeOutAccessName,
       "sleRIPDistributeInPrefixName": sleRIPDistributeInPrefixName,
       "sleRIPDistributeOutPrefixName": sleRIPDistributeOutPrefixName,
       "sleRIPDistributeControl": sleRIPDistributeControl,
       "sleRIPDistributeControlRequest": sleRIPDistributeControlRequest,
       "sleRIPDistributeControlStatus": sleRIPDistributeControlStatus,
       "sleRIPDistributeControlTimer": sleRIPDistributeControlTimer,
       "sleRIPDistributeControlTimeStamp": sleRIPDistributeControlTimeStamp,
       "sleRIPDistributeControlReqResult": sleRIPDistributeControlReqResult,
       "sleRIPDistributeControlIfName": sleRIPDistributeControlIfName,
       "sleRIPDistributeControlInAccessName": sleRIPDistributeControlInAccessName,
       "sleRIPDistributeControlOutAccessName": sleRIPDistributeControlOutAccessName,
       "sleRIPDistributeControlInPrefixName": sleRIPDistributeControlInPrefixName,
       "sleRIPDistributeControlOutPrefixName": sleRIPDistributeControlOutPrefixName,
       "sleRIPDistributeNotification": sleRIPDistributeNotification,
       "sleRIPDistributeInAccessCreated": sleRIPDistributeInAccessCreated,
       "sleRIPDistributeInAccessDeleted": sleRIPDistributeInAccessDeleted,
       "sleRIPDistributeOutAccessCreated": sleRIPDistributeOutAccessCreated,
       "sleRIPDistributeOutAccessDeleted": sleRIPDistributeOutAccessDeleted,
       "sleRIPDistributeInPrefixCreated": sleRIPDistributeInPrefixCreated,
       "sleRIPDistributeInPrefixDeleted": sleRIPDistributeInPrefixDeleted,
       "sleRIPDistributeOutPrefixCreated": sleRIPDistributeOutPrefixCreated,
       "sleRIPDistributeOutPrefixDeleted": sleRIPDistributeOutPrefixDeleted,
       "sleRIPOffsetList": sleRIPOffsetList,
       "sleRIPOffsetListTable": sleRIPOffsetListTable,
       "sleRIPOffsetListEntry": sleRIPOffsetListEntry,
       "sleRIPOffsetListIfname": sleRIPOffsetListIfname,
       "sleRIPOffsetListInAccName": sleRIPOffsetListInAccName,
       "sleRIPOffsetListInMetric": sleRIPOffsetListInMetric,
       "sleRIPOffsetListOutAccName": sleRIPOffsetListOutAccName,
       "sleRIPOffsetListOutMetric": sleRIPOffsetListOutMetric,
       "sleRIPOffsetListControl": sleRIPOffsetListControl,
       "sleRIPOffsetListControlRequest": sleRIPOffsetListControlRequest,
       "sleRIPOffsetListControlStatus": sleRIPOffsetListControlStatus,
       "sleRIPOffsetListControlTimer": sleRIPOffsetListControlTimer,
       "sleRIPOffsetListControlTimeStamp": sleRIPOffsetListControlTimeStamp,
       "sleRIPOffsetListControlReqResult": sleRIPOffsetListControlReqResult,
       "sleRIPOffsetListControlIfname": sleRIPOffsetListControlIfname,
       "sleRIPOffsetListControlInAccName": sleRIPOffsetListControlInAccName,
       "sleRIPOffsetListControlInMetric": sleRIPOffsetListControlInMetric,
       "sleRIPOffsetListControlOutAccName": sleRIPOffsetListControlOutAccName,
       "sleRIPOffsetListControlOutMetric": sleRIPOffsetListControlOutMetric,
       "sleRIPOffsetListNotification": sleRIPOffsetListNotification,
       "sleRIPOffsetListCreatedIn": sleRIPOffsetListCreatedIn,
       "sleRIPOffsetListDeletedIn": sleRIPOffsetListDeletedIn,
       "sleRIPOffsetListCreatedOut": sleRIPOffsetListCreatedOut,
       "sleRIPOffsetListDeletedOut": sleRIPOffsetListDeletedOut,
       "sleRIPRedistribute": sleRIPRedistribute,
       "sleRIPRedistributeTable": sleRIPRedistributeTable,
       "sleRIPRedistributeEntry": sleRIPRedistributeEntry,
       "sleRIPRedistType": sleRIPRedistType,
       "sleRIPRedistMetric": sleRIPRedistMetric,
       "sleRIPRedistRouteMapName": sleRIPRedistRouteMapName,
       "sleRIPRedistributeControl": sleRIPRedistributeControl,
       "sleRIPRedistControlRequest": sleRIPRedistControlRequest,
       "sleRIPRedistControlStatus": sleRIPRedistControlStatus,
       "sleRIPRedistControlTimer": sleRIPRedistControlTimer,
       "sleRIPRedistControlTimeStamp": sleRIPRedistControlTimeStamp,
       "sleRIPRedistControlReqResult": sleRIPRedistControlReqResult,
       "sleRIPRedistControlType": sleRIPRedistControlType,
       "sleRIPRedistControlMetric": sleRIPRedistControlMetric,
       "sleRIPRedistControlRouteMapName": sleRIPRedistControlRouteMapName,
       "sleRIPRedistributeNotification": sleRIPRedistributeNotification,
       "sleRIPRedistributeCreated": sleRIPRedistributeCreated,
       "sleRIPRedistributeDeleted": sleRIPRedistributeDeleted,
       "sleRIPRedistributeChanged": sleRIPRedistributeChanged,
       "sleRIPPassInterface": sleRIPPassInterface,
       "sleRIPPassInterfaceTable": sleRIPPassInterfaceTable,
       "sleRIPPassInterfaceEntry": sleRIPPassInterfaceEntry,
       "sleRIPPassInterfaceName": sleRIPPassInterfaceName,
       "sleRIPPassInterfaceControl": sleRIPPassInterfaceControl,
       "sleRIPPassInterfaceControlRequest": sleRIPPassInterfaceControlRequest,
       "sleRIPPassInterfaceControlStatus": sleRIPPassInterfaceControlStatus,
       "sleRIPPassInterfaceControlTimer": sleRIPPassInterfaceControlTimer,
       "sleRIPPassInterfaceControlTimeStamp": sleRIPPassInterfaceControlTimeStamp,
       "sleRIPPassInterfaceControlReqResult": sleRIPPassInterfaceControlReqResult,
       "sleRIPPassInterfaceControlName": sleRIPPassInterfaceControlName,
       "sleRIPPassInterfaceNotification": sleRIPPassInterfaceNotification,
       "sleRIPPassInterfaceCreated": sleRIPPassInterfaceCreated,
       "sleRIPPassInterfaceDeleted": sleRIPPassInterfaceDeleted,
       "sleRIPInterface": sleRIPInterface,
       "sleRIPInterfaceTable": sleRIPInterfaceTable,
       "sleRIPInterfaceEntry": sleRIPInterfaceEntry,
       "sleRIPInterfaceIndex": sleRIPInterfaceIndex,
       "sleRIPInterfaceRecvVer": sleRIPInterfaceRecvVer,
       "sleRIPInterfaceRecvPacket": sleRIPInterfaceRecvPacket,
       "sleRIPInterfaceSendVer": sleRIPInterfaceSendVer,
       "sleRIPInterfaceSendPacket": sleRIPInterfaceSendPacket,
       "sleRIPInterfaceSplitHorizonMode": sleRIPInterfaceSplitHorizonMode,
       "sleRIPInterfaceAuthMode": sleRIPInterfaceAuthMode,
       "sleRIPInterfaceAuthString": sleRIPInterfaceAuthString,
       "sleRIPInterfaceAuthKeyChain": sleRIPInterfaceAuthKeyChain,
       "sleRIPInterfaceControl": sleRIPInterfaceControl,
       "sleRIPInterfaceControlRequest": sleRIPInterfaceControlRequest,
       "sleRIPInterfaceControlStatus": sleRIPInterfaceControlStatus,
       "sleRIPInterfaceControlTimer": sleRIPInterfaceControlTimer,
       "sleRIPInterfaceControlTimeStamp": sleRIPInterfaceControlTimeStamp,
       "sleRIPInterfaceControlReqResult": sleRIPInterfaceControlReqResult,
       "sleRIPInterfaceControlIndex": sleRIPInterfaceControlIndex,
       "sleRIPInterfaceControlRecvVer": sleRIPInterfaceControlRecvVer,
       "sleRIPInterfaceControlRecvPacket": sleRIPInterfaceControlRecvPacket,
       "sleRIPInterfaceControlSendVer": sleRIPInterfaceControlSendVer,
       "sleRIPInterfaceControlSendPacket": sleRIPInterfaceControlSendPacket,
       "sleRIPInterfaceControlSplitHorizonMode": sleRIPInterfaceControlSplitHorizonMode,
       "sleRIPInterfaceControlAuthMode": sleRIPInterfaceControlAuthMode,
       "sleRIPInterfaceControlAuthString": sleRIPInterfaceControlAuthString,
       "sleRIPInterfaceControlAuthKeyChain": sleRIPInterfaceControlAuthKeyChain,
       "sleRIPInterfaceNotification": sleRIPInterfaceNotification,
       "sleRIPInterfaceRecvVerChanged": sleRIPInterfaceRecvVerChanged,
       "sleRIPInterfaceRecvPacketChanged": sleRIPInterfaceRecvPacketChanged,
       "sleRIPInterfaceSendVerChanged": sleRIPInterfaceSendVerChanged,
       "sleRIPInterfaceSendPacketChanged": sleRIPInterfaceSendPacketChanged,
       "sleRIPInterfaceSplitHorizonModeChanged": sleRIPInterfaceSplitHorizonModeChanged,
       "sleRIPInterfaceAuthModeChanged": sleRIPInterfaceAuthModeChanged,
       "sleRIPInterfaceAuthStringChanged": sleRIPInterfaceAuthStringChanged,
       "sleRIPInterfaceAuthKeyChainChanged": sleRIPInterfaceAuthKeyChainChanged,
       "sleRIPRoutes": sleRIPRoutes,
       "sleRIPRoutesTable": sleRIPRoutesTable,
       "sleRIPRoutesEntry": sleRIPRoutesEntry,
       "sleRIPRoutesType": sleRIPRoutesType,
       "sleRIPRoutesPrefix": sleRIPRoutesPrefix,
       "sleRIPRoutesMask": sleRIPRoutesMask,
       "sleRIPRoutesNextHop": sleRIPRoutesNextHop,
       "sleRIPRoutesMetric": sleRIPRoutesMetric,
       "sleRIPRoutesNetworkFrom": sleRIPRoutesNetworkFrom,
       "sleRIPRoutesIfName": sleRIPRoutesIfName,
       "sleRIPRoutesUpTime": sleRIPRoutesUpTime,
       "sleRIPGroup": sleRIPGroup,
       "sleRIPNotificationGroup": sleRIPNotificationGroup}
)
