# SNMP MIB module (SLE-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-OSPF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:55 2025
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

sleOSPF = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51)
)
if mibBuilder.loadTexts:
    sleOSPF.setRevisions(
        ("2010-03-21 19:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleOSPFBase_ObjectIdentity = ObjectIdentity
sleOSPFBase = _SleOSPFBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1)
)
_SleOSPFBaseInfo_ObjectIdentity = ObjectIdentity
sleOSPFBaseInfo = _SleOSPFBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 1)
)


class _SleOSPFRestartPeriod_Type(Integer32):
    """Custom type sleOSPFRestartPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOSPFRestartPeriod_Type.__name__ = "Integer32"
_SleOSPFRestartPeriod_Object = MibScalar
sleOSPFRestartPeriod = _SleOSPFRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 1, 1),
    _SleOSPFRestartPeriod_Type()
)
sleOSPFRestartPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRestartPeriod.setStatus("current")


class _SleOSPFRestartHelperPolicy_Type(Integer32):
    """Custom type sleOSPFRestartHelperPolicy based on Integer32"""
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
        *(("unspec", 0),
          ("never", 1),
          ("onlyreload", 2),
          ("onlyugrade", 3))
    )


_SleOSPFRestartHelperPolicy_Type.__name__ = "Integer32"
_SleOSPFRestartHelperPolicy_Object = MibScalar
sleOSPFRestartHelperPolicy = _SleOSPFRestartHelperPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 1, 2),
    _SleOSPFRestartHelperPolicy_Type()
)
sleOSPFRestartHelperPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRestartHelperPolicy.setStatus("current")


class _SleOSPFRestartHelperPeriod_Type(Integer32):
    """Custom type sleOSPFRestartHelperPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOSPFRestartHelperPeriod_Type.__name__ = "Integer32"
_SleOSPFRestartHelperPeriod_Object = MibScalar
sleOSPFRestartHelperPeriod = _SleOSPFRestartHelperPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 1, 3),
    _SleOSPFRestartHelperPeriod_Type()
)
sleOSPFRestartHelperPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRestartHelperPeriod.setStatus("current")


class _SleOSPFSnmpNotification_Type(Integer32):
    """Custom type sleOSPFSnmpNotification based on Integer32"""
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


_SleOSPFSnmpNotification_Type.__name__ = "Integer32"
_SleOSPFSnmpNotification_Object = MibScalar
sleOSPFSnmpNotification = _SleOSPFSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 1, 4),
    _SleOSPFSnmpNotification_Type()
)
sleOSPFSnmpNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFSnmpNotification.setStatus("current")
_SleOSPFBaseControl_ObjectIdentity = ObjectIdentity
sleOSPFBaseControl = _SleOSPFBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2)
)


class _SleOSPFControlRequest_Type(Integer32):
    """Custom type sleOSPFControlRequest based on Integer32"""
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
        *(("setOSPFRestartPeriod", 1),
          ("setOSPFRestartHelperProfile", 2),
          ("restartOSPFGraceful", 3),
          ("setOSPFProcSnmpNotification", 4))
    )


_SleOSPFControlRequest_Type.__name__ = "Integer32"
_SleOSPFControlRequest_Object = MibScalar
sleOSPFControlRequest = _SleOSPFControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 1),
    _SleOSPFControlRequest_Type()
)
sleOSPFControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFControlRequest.setStatus("current")
_SleOSPFControlStatus_Type = SleControlStatusType
_SleOSPFControlStatus_Object = MibScalar
sleOSPFControlStatus = _SleOSPFControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 2),
    _SleOSPFControlStatus_Type()
)
sleOSPFControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFControlStatus.setStatus("current")
_SleOSPFControlTimer_Type = Gauge32
_SleOSPFControlTimer_Object = MibScalar
sleOSPFControlTimer = _SleOSPFControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 3),
    _SleOSPFControlTimer_Type()
)
sleOSPFControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFControlTimer.setStatus("current")
_SleOSPFControlTimeStamp_Type = TimeTicks
_SleOSPFControlTimeStamp_Object = MibScalar
sleOSPFControlTimeStamp = _SleOSPFControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 4),
    _SleOSPFControlTimeStamp_Type()
)
sleOSPFControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFControlTimeStamp.setStatus("current")
_SleOSPFControlReqResult_Type = SleControlRequestResultType
_SleOSPFControlReqResult_Object = MibScalar
sleOSPFControlReqResult = _SleOSPFControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 5),
    _SleOSPFControlReqResult_Type()
)
sleOSPFControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFControlReqResult.setStatus("current")


class _SleOSPFControlRestartPeriod_Type(Integer32):
    """Custom type sleOSPFControlRestartPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOSPFControlRestartPeriod_Type.__name__ = "Integer32"
_SleOSPFControlRestartPeriod_Object = MibScalar
sleOSPFControlRestartPeriod = _SleOSPFControlRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 6),
    _SleOSPFControlRestartPeriod_Type()
)
sleOSPFControlRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFControlRestartPeriod.setStatus("current")


class _SleOSPFControlRestartHelperPolicy_Type(Integer32):
    """Custom type sleOSPFControlRestartHelperPolicy based on Integer32"""
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
        *(("unspec", 0),
          ("never", 1),
          ("onlyreload", 2),
          ("onlyugrade", 3))
    )


_SleOSPFControlRestartHelperPolicy_Type.__name__ = "Integer32"
_SleOSPFControlRestartHelperPolicy_Object = MibScalar
sleOSPFControlRestartHelperPolicy = _SleOSPFControlRestartHelperPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 7),
    _SleOSPFControlRestartHelperPolicy_Type()
)
sleOSPFControlRestartHelperPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFControlRestartHelperPolicy.setStatus("current")


class _SleOSPFControlRestartHelperPeriod_Type(Integer32):
    """Custom type sleOSPFControlRestartHelperPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleOSPFControlRestartHelperPeriod_Type.__name__ = "Integer32"
_SleOSPFControlRestartHelperPeriod_Object = MibScalar
sleOSPFControlRestartHelperPeriod = _SleOSPFControlRestartHelperPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 8),
    _SleOSPFControlRestartHelperPeriod_Type()
)
sleOSPFControlRestartHelperPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFControlRestartHelperPeriod.setStatus("current")


class _SleOSPFControlSnmpNotification_Type(Integer32):
    """Custom type sleOSPFControlSnmpNotification based on Integer32"""
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


_SleOSPFControlSnmpNotification_Type.__name__ = "Integer32"
_SleOSPFControlSnmpNotification_Object = MibScalar
sleOSPFControlSnmpNotification = _SleOSPFControlSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 2, 9),
    _SleOSPFControlSnmpNotification_Type()
)
sleOSPFControlSnmpNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFControlSnmpNotification.setStatus("current")
_SleOSPFBaseNotification_ObjectIdentity = ObjectIdentity
sleOSPFBaseNotification = _SleOSPFBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 3)
)
_SleOSPFProc_ObjectIdentity = ObjectIdentity
sleOSPFProc = _SleOSPFProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2)
)
_SleOSPFProcInfo_ObjectIdentity = ObjectIdentity
sleOSPFProcInfo = _SleOSPFProcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1)
)
_SleOSPFProcInfoTable_Object = MibTable
sleOSPFProcInfoTable = _SleOSPFProcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcInfoTable.setStatus("current")
_SleOSPFProcInfoEntry_Object = MibTableRow
sleOSPFProcInfoEntry = _SleOSPFProcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1)
)
sleOSPFProcInfoEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
)
if mibBuilder.loadTexts:
    sleOSPFProcInfoEntry.setStatus("current")


class _SleOSPFProcID_Type(Integer32):
    """Custom type sleOSPFProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcID_Type.__name__ = "Integer32"
_SleOSPFProcID_Object = MibTableColumn
sleOSPFProcID = _SleOSPFProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 1),
    _SleOSPFProcID_Type()
)
sleOSPFProcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcID.setStatus("current")
_SleOSPFProcRouterID_Type = IpAddress
_SleOSPFProcRouterID_Object = MibTableColumn
sleOSPFProcRouterID = _SleOSPFProcRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 2),
    _SleOSPFProcRouterID_Type()
)
sleOSPFProcRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRouterID.setStatus("current")


class _SleOSPFProcSPFDelayTime_Type(Integer32):
    """Custom type sleOSPFProcSPFDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOSPFProcSPFDelayTime_Type.__name__ = "Integer32"
_SleOSPFProcSPFDelayTime_Object = MibTableColumn
sleOSPFProcSPFDelayTime = _SleOSPFProcSPFDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 3),
    _SleOSPFProcSPFDelayTime_Type()
)
sleOSPFProcSPFDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSPFDelayTime.setStatus("current")


class _SleOSPFProcSPFHoldTime_Type(Integer32):
    """Custom type sleOSPFProcSPFHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOSPFProcSPFHoldTime_Type.__name__ = "Integer32"
_SleOSPFProcSPFHoldTime_Object = MibTableColumn
sleOSPFProcSPFHoldTime = _SleOSPFProcSPFHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 4),
    _SleOSPFProcSPFHoldTime_Type()
)
sleOSPFProcSPFHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSPFHoldTime.setStatus("current")


class _SleOSPFProcAutoCost_Type(Integer32):
    """Custom type sleOSPFProcAutoCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967),
    )


_SleOSPFProcAutoCost_Type.__name__ = "Integer32"
_SleOSPFProcAutoCost_Object = MibTableColumn
sleOSPFProcAutoCost = _SleOSPFProcAutoCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 5),
    _SleOSPFProcAutoCost_Type()
)
sleOSPFProcAutoCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAutoCost.setStatus("current")


class _SleOSPFProcAbrType_Type(Integer32):
    """Custom type sleOSPFProcAbrType based on Integer32"""
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
        *(("standard", 1),
          ("cisco", 2),
          ("ibm", 3),
          ("shortcut", 4))
    )


_SleOSPFProcAbrType_Type.__name__ = "Integer32"
_SleOSPFProcAbrType_Object = MibTableColumn
sleOSPFProcAbrType = _SleOSPFProcAbrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 6),
    _SleOSPFProcAbrType_Type()
)
sleOSPFProcAbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAbrType.setStatus("current")


class _SleOSPFProcSnmpNotification_Type(Integer32):
    """Custom type sleOSPFProcSnmpNotification based on Integer32"""
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


_SleOSPFProcSnmpNotification_Type.__name__ = "Integer32"
_SleOSPFProcSnmpNotification_Object = MibTableColumn
sleOSPFProcSnmpNotification = _SleOSPFProcSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 7),
    _SleOSPFProcSnmpNotification_Type()
)
sleOSPFProcSnmpNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSnmpNotification.setStatus("current")


class _SleOSPFProcDefaultMetricConfig_Type(Integer32):
    """Custom type sleOSPFProcDefaultMetricConfig based on Integer32"""
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


_SleOSPFProcDefaultMetricConfig_Type.__name__ = "Integer32"
_SleOSPFProcDefaultMetricConfig_Object = MibTableColumn
sleOSPFProcDefaultMetricConfig = _SleOSPFProcDefaultMetricConfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 8),
    _SleOSPFProcDefaultMetricConfig_Type()
)
sleOSPFProcDefaultMetricConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDefaultMetricConfig.setStatus("current")


class _SleOSPFProcDefaultMetricValue_Type(Integer32):
    """Custom type sleOSPFProcDefaultMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_SleOSPFProcDefaultMetricValue_Type.__name__ = "Integer32"
_SleOSPFProcDefaultMetricValue_Object = MibTableColumn
sleOSPFProcDefaultMetricValue = _SleOSPFProcDefaultMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 9),
    _SleOSPFProcDefaultMetricValue_Type()
)
sleOSPFProcDefaultMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDefaultMetricValue.setStatus("current")


class _SleOSPFProcMaxArea_Type(Gauge32):
    """Custom type sleOSPFProcMaxArea based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_SleOSPFProcMaxArea_Type.__name__ = "Gauge32"
_SleOSPFProcMaxArea_Object = MibTableColumn
sleOSPFProcMaxArea = _SleOSPFProcMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 10),
    _SleOSPFProcMaxArea_Type()
)
sleOSPFProcMaxArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcMaxArea.setStatus("current")


class _SleOSPFProcMaxConcurrentDD_Type(Integer32):
    """Custom type sleOSPFProcMaxConcurrentDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcMaxConcurrentDD_Type.__name__ = "Integer32"
_SleOSPFProcMaxConcurrentDD_Object = MibTableColumn
sleOSPFProcMaxConcurrentDD = _SleOSPFProcMaxConcurrentDD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 11),
    _SleOSPFProcMaxConcurrentDD_Type()
)
sleOSPFProcMaxConcurrentDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcMaxConcurrentDD.setStatus("current")


class _SleOSPFProcCompatiblerfc1583_Type(Integer32):
    """Custom type sleOSPFProcCompatiblerfc1583 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uncompatible", 0),
          ("compatible", 1))
    )


_SleOSPFProcCompatiblerfc1583_Type.__name__ = "Integer32"
_SleOSPFProcCompatiblerfc1583_Object = MibTableColumn
sleOSPFProcCompatiblerfc1583 = _SleOSPFProcCompatiblerfc1583_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 12),
    _SleOSPFProcCompatiblerfc1583_Type()
)
sleOSPFProcCompatiblerfc1583.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcCompatiblerfc1583.setStatus("current")


class _SleOSPFProcCapabilityOpaque_Type(Integer32):
    """Custom type sleOSPFProcCapabilityOpaque based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uncapability", 0),
          ("capability", 1))
    )


_SleOSPFProcCapabilityOpaque_Type.__name__ = "Integer32"
_SleOSPFProcCapabilityOpaque_Object = MibTableColumn
sleOSPFProcCapabilityOpaque = _SleOSPFProcCapabilityOpaque_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 13),
    _SleOSPFProcCapabilityOpaque_Type()
)
sleOSPFProcCapabilityOpaque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcCapabilityOpaque.setStatus("current")


class _SleOSPFProcLSDBOverflowType_Type(Integer32):
    """Custom type sleOSPFProcLSDBOverflowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspec", 0),
          ("soft", 1),
          ("hard", 2))
    )


_SleOSPFProcLSDBOverflowType_Type.__name__ = "Integer32"
_SleOSPFProcLSDBOverflowType_Object = MibTableColumn
sleOSPFProcLSDBOverflowType = _SleOSPFProcLSDBOverflowType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 14),
    _SleOSPFProcLSDBOverflowType_Type()
)
sleOSPFProcLSDBOverflowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcLSDBOverflowType.setStatus("current")


class _SleOSPFProcLSDBOverflowLimit_Type(Gauge32):
    """Custom type sleOSPFProcLSDBOverflowLimit based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SleOSPFProcLSDBOverflowLimit_Type.__name__ = "Gauge32"
_SleOSPFProcLSDBOverflowLimit_Object = MibTableColumn
sleOSPFProcLSDBOverflowLimit = _SleOSPFProcLSDBOverflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 15),
    _SleOSPFProcLSDBOverflowLimit_Type()
)
sleOSPFProcLSDBOverflowLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcLSDBOverflowLimit.setStatus("current")


class _SleOSPFProcExtLSDBLimit_Type(Integer32):
    """Custom type sleOSPFProcExtLSDBLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SleOSPFProcExtLSDBLimit_Type.__name__ = "Integer32"
_SleOSPFProcExtLSDBLimit_Object = MibTableColumn
sleOSPFProcExtLSDBLimit = _SleOSPFProcExtLSDBLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 16),
    _SleOSPFProcExtLSDBLimit_Type()
)
sleOSPFProcExtLSDBLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcExtLSDBLimit.setStatus("current")


class _SleOSPFProcExitOverFlowInterval_Type(Integer32):
    """Custom type sleOSPFProcExitOverFlowInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcExitOverFlowInterval_Type.__name__ = "Integer32"
_SleOSPFProcExitOverFlowInterval_Object = MibTableColumn
sleOSPFProcExitOverFlowInterval = _SleOSPFProcExitOverFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 17),
    _SleOSPFProcExitOverFlowInterval_Type()
)
sleOSPFProcExitOverFlowInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcExitOverFlowInterval.setStatus("current")


class _SleOSPFProcAdminDistance_Type(Integer32):
    """Custom type sleOSPFProcAdminDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcAdminDistance_Type.__name__ = "Integer32"
_SleOSPFProcAdminDistance_Object = MibTableColumn
sleOSPFProcAdminDistance = _SleOSPFProcAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 18),
    _SleOSPFProcAdminDistance_Type()
)
sleOSPFProcAdminDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAdminDistance.setStatus("current")


class _SleOSPFProcExternalDistance_Type(Integer32):
    """Custom type sleOSPFProcExternalDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcExternalDistance_Type.__name__ = "Integer32"
_SleOSPFProcExternalDistance_Object = MibTableColumn
sleOSPFProcExternalDistance = _SleOSPFProcExternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 19),
    _SleOSPFProcExternalDistance_Type()
)
sleOSPFProcExternalDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcExternalDistance.setStatus("current")


class _SleOSPFProcIntraAreaDistance_Type(Integer32):
    """Custom type sleOSPFProcIntraAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcIntraAreaDistance_Type.__name__ = "Integer32"
_SleOSPFProcIntraAreaDistance_Object = MibTableColumn
sleOSPFProcIntraAreaDistance = _SleOSPFProcIntraAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 20),
    _SleOSPFProcIntraAreaDistance_Type()
)
sleOSPFProcIntraAreaDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcIntraAreaDistance.setStatus("current")


class _SleOSPFProcInterAreaDistance_Type(Integer32):
    """Custom type sleOSPFProcInterAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcInterAreaDistance_Type.__name__ = "Integer32"
_SleOSPFProcInterAreaDistance_Object = MibTableColumn
sleOSPFProcInterAreaDistance = _SleOSPFProcInterAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 21),
    _SleOSPFProcInterAreaDistance_Type()
)
sleOSPFProcInterAreaDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcInterAreaDistance.setStatus("current")


class _SleOSPFProcDefaultOriginType_Type(Integer32):
    """Custom type sleOSPFProcDefaultOriginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspec", 0),
          ("normal", 1),
          ("always", 2))
    )


_SleOSPFProcDefaultOriginType_Type.__name__ = "Integer32"
_SleOSPFProcDefaultOriginType_Object = MibTableColumn
sleOSPFProcDefaultOriginType = _SleOSPFProcDefaultOriginType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 22),
    _SleOSPFProcDefaultOriginType_Type()
)
sleOSPFProcDefaultOriginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginType.setStatus("current")


class _SleOSPFProcDefaultOriginMetricType_Type(Integer32):
    """Custom type sleOSPFProcDefaultOriginMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspec", 0),
          ("external1", 1),
          ("external2", 2))
    )


_SleOSPFProcDefaultOriginMetricType_Type.__name__ = "Integer32"
_SleOSPFProcDefaultOriginMetricType_Object = MibTableColumn
sleOSPFProcDefaultOriginMetricType = _SleOSPFProcDefaultOriginMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 23),
    _SleOSPFProcDefaultOriginMetricType_Type()
)
sleOSPFProcDefaultOriginMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginMetricType.setStatus("current")


class _SleOSPFProcDefaultOriginMetric_Type(Integer32):
    """Custom type sleOSPFProcDefaultOriginMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOSPFProcDefaultOriginMetric_Type.__name__ = "Integer32"
_SleOSPFProcDefaultOriginMetric_Object = MibTableColumn
sleOSPFProcDefaultOriginMetric = _SleOSPFProcDefaultOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 24),
    _SleOSPFProcDefaultOriginMetric_Type()
)
sleOSPFProcDefaultOriginMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginMetric.setStatus("current")


class _SleOSPFProcDefaultOriginRouteMap_Type(OctetString):
    """Custom type sleOSPFProcDefaultOriginRouteMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOSPFProcDefaultOriginRouteMap_Type.__name__ = "OctetString"
_SleOSPFProcDefaultOriginRouteMap_Object = MibTableColumn
sleOSPFProcDefaultOriginRouteMap = _SleOSPFProcDefaultOriginRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 25),
    _SleOSPFProcDefaultOriginRouteMap_Type()
)
sleOSPFProcDefaultOriginRouteMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginRouteMap.setStatus("current")


class _SleOSPFProcLogNeighborChange_Type(Integer32):
    """Custom type sleOSPFProcLogNeighborChange based on Integer32"""
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


_SleOSPFProcLogNeighborChange_Type.__name__ = "Integer32"
_SleOSPFProcLogNeighborChange_Object = MibTableColumn
sleOSPFProcLogNeighborChange = _SleOSPFProcLogNeighborChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 26),
    _SleOSPFProcLogNeighborChange_Type()
)
sleOSPFProcLogNeighborChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcLogNeighborChange.setStatus("current")


class _SleOSPFProcPassiveIfAll_Type(Integer32):
    """Custom type sleOSPFProcPassiveIfAll based on Integer32"""
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


_SleOSPFProcPassiveIfAll_Type.__name__ = "Integer32"
_SleOSPFProcPassiveIfAll_Object = MibTableColumn
sleOSPFProcPassiveIfAll = _SleOSPFProcPassiveIfAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 27),
    _SleOSPFProcPassiveIfAll_Type()
)
sleOSPFProcPassiveIfAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcPassiveIfAll.setStatus("current")


class _SleOSPFProcBfdIFAll_Type(Integer32):
    """Custom type sleOSPFProcBfdIFAll based on Integer32"""
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


_SleOSPFProcBfdIFAll_Type.__name__ = "Integer32"
_SleOSPFProcBfdIFAll_Object = MibTableColumn
sleOSPFProcBfdIFAll = _SleOSPFProcBfdIFAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 28),
    _SleOSPFProcBfdIFAll_Type()
)
sleOSPFProcBfdIFAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcBfdIFAll.setStatus("current")


class _SleOSPFProcEfmIFAll_Type(Integer32):
    """Custom type sleOSPFProcEfmIFAll based on Integer32"""
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


_SleOSPFProcEfmIFAll_Type.__name__ = "Integer32"
_SleOSPFProcEfmIFAll_Object = MibTableColumn
sleOSPFProcEfmIFAll = _SleOSPFProcEfmIFAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 29),
    _SleOSPFProcEfmIFAll_Type()
)
sleOSPFProcEfmIFAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcEfmIFAll.setStatus("current")


class _SleOSPFProcCapabilityRestart_Type(Integer32):
    """Custom type sleOSPFProcCapabilityRestart based on Integer32"""
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
          ("graceful", 1),
          ("signaling", 2),
          ("gracefulAck", 3))
    )


_SleOSPFProcCapabilityRestart_Type.__name__ = "Integer32"
_SleOSPFProcCapabilityRestart_Object = MibTableColumn
sleOSPFProcCapabilityRestart = _SleOSPFProcCapabilityRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 30),
    _SleOSPFProcCapabilityRestart_Type()
)
sleOSPFProcCapabilityRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcCapabilityRestart.setStatus("current")


class _SleOSPFProcVRIndex_Type(Integer32):
    """Custom type sleOSPFProcVRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcVRIndex_Type.__name__ = "Integer32"
_SleOSPFProcVRIndex_Object = MibTableColumn
sleOSPFProcVRIndex = _SleOSPFProcVRIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 31),
    _SleOSPFProcVRIndex_Type()
)
sleOSPFProcVRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcVRIndex.setStatus("current")


class _SleOSPFProcVRFName_Type(OctetString):
    """Custom type sleOSPFProcVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleOSPFProcVRFName_Type.__name__ = "OctetString"
_SleOSPFProcVRFName_Object = MibTableColumn
sleOSPFProcVRFName = _SleOSPFProcVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 32),
    _SleOSPFProcVRFName_Type()
)
sleOSPFProcVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcVRFName.setStatus("current")


class _SleOSPFProcSPFStartDelay_Type(Integer32):
    """Custom type sleOSPFProcSPFStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcSPFStartDelay_Type.__name__ = "Integer32"
_SleOSPFProcSPFStartDelay_Object = MibTableColumn
sleOSPFProcSPFStartDelay = _SleOSPFProcSPFStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 33),
    _SleOSPFProcSPFStartDelay_Type()
)
sleOSPFProcSPFStartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSPFStartDelay.setStatus("current")


class _SleOSPFProcSPFMinDelay_Type(Integer32):
    """Custom type sleOSPFProcSPFMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcSPFMinDelay_Type.__name__ = "Integer32"
_SleOSPFProcSPFMinDelay_Object = MibTableColumn
sleOSPFProcSPFMinDelay = _SleOSPFProcSPFMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 34),
    _SleOSPFProcSPFMinDelay_Type()
)
sleOSPFProcSPFMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSPFMinDelay.setStatus("current")


class _SleOSPFProcSPFMaxDelay_Type(Integer32):
    """Custom type sleOSPFProcSPFMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcSPFMaxDelay_Type.__name__ = "Integer32"
_SleOSPFProcSPFMaxDelay_Object = MibTableColumn
sleOSPFProcSPFMaxDelay = _SleOSPFProcSPFMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 35),
    _SleOSPFProcSPFMaxDelay_Type()
)
sleOSPFProcSPFMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSPFMaxDelay.setStatus("current")


class _SleOSPFProcLSAStartDelay_Type(Integer32):
    """Custom type sleOSPFProcLSAStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcLSAStartDelay_Type.__name__ = "Integer32"
_SleOSPFProcLSAStartDelay_Object = MibTableColumn
sleOSPFProcLSAStartDelay = _SleOSPFProcLSAStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 36),
    _SleOSPFProcLSAStartDelay_Type()
)
sleOSPFProcLSAStartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcLSAStartDelay.setStatus("current")


class _SleOSPFProcLSAMinDelay_Type(Integer32):
    """Custom type sleOSPFProcLSAMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcLSAMinDelay_Type.__name__ = "Integer32"
_SleOSPFProcLSAMinDelay_Object = MibTableColumn
sleOSPFProcLSAMinDelay = _SleOSPFProcLSAMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 37),
    _SleOSPFProcLSAMinDelay_Type()
)
sleOSPFProcLSAMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcLSAMinDelay.setStatus("current")


class _SleOSPFProcLSAMaxDelay_Type(Integer32):
    """Custom type sleOSPFProcLSAMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcLSAMaxDelay_Type.__name__ = "Integer32"
_SleOSPFProcLSAMaxDelay_Object = MibTableColumn
sleOSPFProcLSAMaxDelay = _SleOSPFProcLSAMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 38),
    _SleOSPFProcLSAMaxDelay_Type()
)
sleOSPFProcLSAMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcLSAMaxDelay.setStatus("current")


class _SleOSPFProcLSAArrivalDelay_Type(Integer32):
    """Custom type sleOSPFProcLSAArrivalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcLSAArrivalDelay_Type.__name__ = "Integer32"
_SleOSPFProcLSAArrivalDelay_Object = MibTableColumn
sleOSPFProcLSAArrivalDelay = _SleOSPFProcLSAArrivalDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 1, 1, 39),
    _SleOSPFProcLSAArrivalDelay_Type()
)
sleOSPFProcLSAArrivalDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcLSAArrivalDelay.setStatus("current")
_SleOSPFProcInfoControl_ObjectIdentity = ObjectIdentity
sleOSPFProcInfoControl = _SleOSPFProcInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2)
)


class _SleOSPFProcControlRequest_Type(Integer32):
    """Custom type sleOSPFProcControlRequest based on Integer32"""
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
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcess", 1),
          ("deleteOSPFProcess", 2),
          ("createOSPFProcRouterID", 3),
          ("deleteOSPFProcRouterID", 4),
          ("setOSPFProcSPFTimer", 5),
          ("setOSPFProcAutoCost", 6),
          ("setOSPFProcAbrType", 7),
          ("setOSPFProcSnmpNotification", 8),
          ("setOSPFProcDefaultMetricProfile", 9),
          ("setOSPFProcMaximumArea", 10),
          ("setOSPFProcMaxConcurDD", 11),
          ("setOSPFProcComprfc1583", 12),
          ("setOSPFProcCapOpaque", 13),
          ("setOSPFProcLSDBOverflowProfile", 14),
          ("setOSPFProcExtOverflowProfile", 15),
          ("setOSPFProcAdminDistance", 16),
          ("setOSPFProcExtDistance", 17),
          ("setOSPFProcIntraDistance", 18),
          ("setOSPFProcInterDistance", 19),
          ("setOSPFProcDefaultOriginType", 20),
          ("setOSPFProcDefaultOriginMetricType", 21),
          ("setOSPFProcDefaultOriginMetric", 22),
          ("setOSPFProcDefaultOriginRouteMap", 23),
          ("setOSPFProcLogNeighborChange", 24),
          ("setOSPFProcPassiveIfAll", 25),
          ("setOSPFProcBfdIFAll", 26),
          ("setOSPFProcEfmIFAll", 27),
          ("setOSPFProcCapRestart", 28),
          ("clearOSPFProcess", 29),
          ("setOSPFProcSPFThrottleTimer", 30),
          ("setOSPFProcLSAThrottleTimer", 31),
          ("setOSPFProcLSAArrivalTimer", 32))
    )


_SleOSPFProcControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcControlRequest_Object = MibScalar
sleOSPFProcControlRequest = _SleOSPFProcControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 1),
    _SleOSPFProcControlRequest_Type()
)
sleOSPFProcControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlRequest.setStatus("current")
_SleOSPFProcControlStatus_Type = SleControlStatusType
_SleOSPFProcControlStatus_Object = MibScalar
sleOSPFProcControlStatus = _SleOSPFProcControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 2),
    _SleOSPFProcControlStatus_Type()
)
sleOSPFProcControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcControlStatus.setStatus("current")
_SleOSPFProcControlTimer_Type = Gauge32
_SleOSPFProcControlTimer_Object = MibScalar
sleOSPFProcControlTimer = _SleOSPFProcControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 3),
    _SleOSPFProcControlTimer_Type()
)
sleOSPFProcControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlTimer.setStatus("current")
_SleOSPFProcControlTimeStamp_Type = TimeTicks
_SleOSPFProcControlTimeStamp_Object = MibScalar
sleOSPFProcControlTimeStamp = _SleOSPFProcControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 4),
    _SleOSPFProcControlTimeStamp_Type()
)
sleOSPFProcControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcControlTimeStamp.setStatus("current")
_SleOSPFProcControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcControlReqResult_Object = MibScalar
sleOSPFProcControlReqResult = _SleOSPFProcControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 5),
    _SleOSPFProcControlReqResult_Type()
)
sleOSPFProcControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcControlReqResult.setStatus("current")


class _SleOSPFProcControlID_Type(Integer32):
    """Custom type sleOSPFProcControlID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcControlID_Type.__name__ = "Integer32"
_SleOSPFProcControlID_Object = MibScalar
sleOSPFProcControlID = _SleOSPFProcControlID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 6),
    _SleOSPFProcControlID_Type()
)
sleOSPFProcControlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlID.setStatus("current")
_SleOSPFProcControlRouterID_Type = IpAddress
_SleOSPFProcControlRouterID_Object = MibScalar
sleOSPFProcControlRouterID = _SleOSPFProcControlRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 7),
    _SleOSPFProcControlRouterID_Type()
)
sleOSPFProcControlRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlRouterID.setStatus("current")


class _SleOSPFProcControlSPFDelayTime_Type(Integer32):
    """Custom type sleOSPFProcControlSPFDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOSPFProcControlSPFDelayTime_Type.__name__ = "Integer32"
_SleOSPFProcControlSPFDelayTime_Object = MibScalar
sleOSPFProcControlSPFDelayTime = _SleOSPFProcControlSPFDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 8),
    _SleOSPFProcControlSPFDelayTime_Type()
)
sleOSPFProcControlSPFDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlSPFDelayTime.setStatus("current")


class _SleOSPFProcControlSPFHoldTime_Type(Integer32):
    """Custom type sleOSPFProcControlSPFHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleOSPFProcControlSPFHoldTime_Type.__name__ = "Integer32"
_SleOSPFProcControlSPFHoldTime_Object = MibScalar
sleOSPFProcControlSPFHoldTime = _SleOSPFProcControlSPFHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 9),
    _SleOSPFProcControlSPFHoldTime_Type()
)
sleOSPFProcControlSPFHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlSPFHoldTime.setStatus("current")


class _SleOSPFProcControlAutoCost_Type(Integer32):
    """Custom type sleOSPFProcControlAutoCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967),
    )


_SleOSPFProcControlAutoCost_Type.__name__ = "Integer32"
_SleOSPFProcControlAutoCost_Object = MibScalar
sleOSPFProcControlAutoCost = _SleOSPFProcControlAutoCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 10),
    _SleOSPFProcControlAutoCost_Type()
)
sleOSPFProcControlAutoCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlAutoCost.setStatus("current")


class _SleOSPFProcControlAbrType_Type(Integer32):
    """Custom type sleOSPFProcControlAbrType based on Integer32"""
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
        *(("standard", 1),
          ("cisco", 2),
          ("ibm", 3),
          ("shortcut", 4))
    )


_SleOSPFProcControlAbrType_Type.__name__ = "Integer32"
_SleOSPFProcControlAbrType_Object = MibScalar
sleOSPFProcControlAbrType = _SleOSPFProcControlAbrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 11),
    _SleOSPFProcControlAbrType_Type()
)
sleOSPFProcControlAbrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlAbrType.setStatus("current")


class _SleOSPFProcControlSnmpNotification_Type(Integer32):
    """Custom type sleOSPFProcControlSnmpNotification based on Integer32"""
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


_SleOSPFProcControlSnmpNotification_Type.__name__ = "Integer32"
_SleOSPFProcControlSnmpNotification_Object = MibScalar
sleOSPFProcControlSnmpNotification = _SleOSPFProcControlSnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 12),
    _SleOSPFProcControlSnmpNotification_Type()
)
sleOSPFProcControlSnmpNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlSnmpNotification.setStatus("current")


class _SleOSPFProcControlDefaultMetricConfig_Type(Integer32):
    """Custom type sleOSPFProcControlDefaultMetricConfig based on Integer32"""
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


_SleOSPFProcControlDefaultMetricConfig_Type.__name__ = "Integer32"
_SleOSPFProcControlDefaultMetricConfig_Object = MibScalar
sleOSPFProcControlDefaultMetricConfig = _SleOSPFProcControlDefaultMetricConfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 13),
    _SleOSPFProcControlDefaultMetricConfig_Type()
)
sleOSPFProcControlDefaultMetricConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlDefaultMetricConfig.setStatus("current")


class _SleOSPFProcControlDefaultMetricValue_Type(Integer32):
    """Custom type sleOSPFProcControlDefaultMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_SleOSPFProcControlDefaultMetricValue_Type.__name__ = "Integer32"
_SleOSPFProcControlDefaultMetricValue_Object = MibScalar
sleOSPFProcControlDefaultMetricValue = _SleOSPFProcControlDefaultMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 14),
    _SleOSPFProcControlDefaultMetricValue_Type()
)
sleOSPFProcControlDefaultMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlDefaultMetricValue.setStatus("current")


class _SleOSPFProcControlMaxArea_Type(Gauge32):
    """Custom type sleOSPFProcControlMaxArea based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_SleOSPFProcControlMaxArea_Type.__name__ = "Gauge32"
_SleOSPFProcControlMaxArea_Object = MibScalar
sleOSPFProcControlMaxArea = _SleOSPFProcControlMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 15),
    _SleOSPFProcControlMaxArea_Type()
)
sleOSPFProcControlMaxArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlMaxArea.setStatus("current")


class _SleOSPFProcControlMaxConcurDD_Type(Integer32):
    """Custom type sleOSPFProcControlMaxConcurDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcControlMaxConcurDD_Type.__name__ = "Integer32"
_SleOSPFProcControlMaxConcurDD_Object = MibScalar
sleOSPFProcControlMaxConcurDD = _SleOSPFProcControlMaxConcurDD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 16),
    _SleOSPFProcControlMaxConcurDD_Type()
)
sleOSPFProcControlMaxConcurDD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlMaxConcurDD.setStatus("current")


class _SleOSPFProcControlComprfc1583_Type(Integer32):
    """Custom type sleOSPFProcControlComprfc1583 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uncompatible", 0),
          ("compatible", 1))
    )


_SleOSPFProcControlComprfc1583_Type.__name__ = "Integer32"
_SleOSPFProcControlComprfc1583_Object = MibScalar
sleOSPFProcControlComprfc1583 = _SleOSPFProcControlComprfc1583_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 17),
    _SleOSPFProcControlComprfc1583_Type()
)
sleOSPFProcControlComprfc1583.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlComprfc1583.setStatus("current")


class _SleOSPFProcControlCapabilityOpaque_Type(Integer32):
    """Custom type sleOSPFProcControlCapabilityOpaque based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uncapability", 0),
          ("capability", 1))
    )


_SleOSPFProcControlCapabilityOpaque_Type.__name__ = "Integer32"
_SleOSPFProcControlCapabilityOpaque_Object = MibScalar
sleOSPFProcControlCapabilityOpaque = _SleOSPFProcControlCapabilityOpaque_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 18),
    _SleOSPFProcControlCapabilityOpaque_Type()
)
sleOSPFProcControlCapabilityOpaque.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlCapabilityOpaque.setStatus("current")


class _SleOSPFProcControlLSDBOverflowType_Type(Integer32):
    """Custom type sleOSPFProcControlLSDBOverflowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspec", 0),
          ("soft", 1),
          ("hard", 2))
    )


_SleOSPFProcControlLSDBOverflowType_Type.__name__ = "Integer32"
_SleOSPFProcControlLSDBOverflowType_Object = MibScalar
sleOSPFProcControlLSDBOverflowType = _SleOSPFProcControlLSDBOverflowType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 19),
    _SleOSPFProcControlLSDBOverflowType_Type()
)
sleOSPFProcControlLSDBOverflowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlLSDBOverflowType.setStatus("current")


class _SleOSPFProcControlLSDBOverflowLimit_Type(Gauge32):
    """Custom type sleOSPFProcControlLSDBOverflowLimit based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SleOSPFProcControlLSDBOverflowLimit_Type.__name__ = "Gauge32"
_SleOSPFProcControlLSDBOverflowLimit_Object = MibScalar
sleOSPFProcControlLSDBOverflowLimit = _SleOSPFProcControlLSDBOverflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 20),
    _SleOSPFProcControlLSDBOverflowLimit_Type()
)
sleOSPFProcControlLSDBOverflowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlLSDBOverflowLimit.setStatus("current")


class _SleOSPFProcControlExtLSDBLimit_Type(Integer32):
    """Custom type sleOSPFProcControlExtLSDBLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SleOSPFProcControlExtLSDBLimit_Type.__name__ = "Integer32"
_SleOSPFProcControlExtLSDBLimit_Object = MibScalar
sleOSPFProcControlExtLSDBLimit = _SleOSPFProcControlExtLSDBLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 21),
    _SleOSPFProcControlExtLSDBLimit_Type()
)
sleOSPFProcControlExtLSDBLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlExtLSDBLimit.setStatus("current")


class _SleOSPFProcControlExitOverFlowInterval_Type(Integer32):
    """Custom type sleOSPFProcControlExitOverFlowInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcControlExitOverFlowInterval_Type.__name__ = "Integer32"
_SleOSPFProcControlExitOverFlowInterval_Object = MibScalar
sleOSPFProcControlExitOverFlowInterval = _SleOSPFProcControlExitOverFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 22),
    _SleOSPFProcControlExitOverFlowInterval_Type()
)
sleOSPFProcControlExitOverFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlExitOverFlowInterval.setStatus("current")


class _SleOSPFProcControlAdminDistance_Type(Integer32):
    """Custom type sleOSPFProcControlAdminDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcControlAdminDistance_Type.__name__ = "Integer32"
_SleOSPFProcControlAdminDistance_Object = MibScalar
sleOSPFProcControlAdminDistance = _SleOSPFProcControlAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 23),
    _SleOSPFProcControlAdminDistance_Type()
)
sleOSPFProcControlAdminDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlAdminDistance.setStatus("current")


class _SleOSPFProcControlExtDistance_Type(Integer32):
    """Custom type sleOSPFProcControlExtDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcControlExtDistance_Type.__name__ = "Integer32"
_SleOSPFProcControlExtDistance_Object = MibScalar
sleOSPFProcControlExtDistance = _SleOSPFProcControlExtDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 24),
    _SleOSPFProcControlExtDistance_Type()
)
sleOSPFProcControlExtDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlExtDistance.setStatus("current")


class _SleOSPFProcControlIntraAreaDistance_Type(Integer32):
    """Custom type sleOSPFProcControlIntraAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcControlIntraAreaDistance_Type.__name__ = "Integer32"
_SleOSPFProcControlIntraAreaDistance_Object = MibScalar
sleOSPFProcControlIntraAreaDistance = _SleOSPFProcControlIntraAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 25),
    _SleOSPFProcControlIntraAreaDistance_Type()
)
sleOSPFProcControlIntraAreaDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlIntraAreaDistance.setStatus("current")


class _SleOSPFProcControlInterAreaDistance_Type(Integer32):
    """Custom type sleOSPFProcControlInterAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcControlInterAreaDistance_Type.__name__ = "Integer32"
_SleOSPFProcControlInterAreaDistance_Object = MibScalar
sleOSPFProcControlInterAreaDistance = _SleOSPFProcControlInterAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 26),
    _SleOSPFProcControlInterAreaDistance_Type()
)
sleOSPFProcControlInterAreaDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlInterAreaDistance.setStatus("current")


class _SleOSPFProcControlDefOriginType_Type(Integer32):
    """Custom type sleOSPFProcControlDefOriginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspec", 0),
          ("normal", 1),
          ("always", 2))
    )


_SleOSPFProcControlDefOriginType_Type.__name__ = "Integer32"
_SleOSPFProcControlDefOriginType_Object = MibScalar
sleOSPFProcControlDefOriginType = _SleOSPFProcControlDefOriginType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 27),
    _SleOSPFProcControlDefOriginType_Type()
)
sleOSPFProcControlDefOriginType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlDefOriginType.setStatus("current")


class _SleOSPFProcControlDefOriginMetricType_Type(Integer32):
    """Custom type sleOSPFProcControlDefOriginMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspec", 0),
          ("external1", 1),
          ("external2", 2))
    )


_SleOSPFProcControlDefOriginMetricType_Type.__name__ = "Integer32"
_SleOSPFProcControlDefOriginMetricType_Object = MibScalar
sleOSPFProcControlDefOriginMetricType = _SleOSPFProcControlDefOriginMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 28),
    _SleOSPFProcControlDefOriginMetricType_Type()
)
sleOSPFProcControlDefOriginMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlDefOriginMetricType.setStatus("current")


class _SleOSPFProcControlDefOriginMetric_Type(Integer32):
    """Custom type sleOSPFProcControlDefOriginMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOSPFProcControlDefOriginMetric_Type.__name__ = "Integer32"
_SleOSPFProcControlDefOriginMetric_Object = MibScalar
sleOSPFProcControlDefOriginMetric = _SleOSPFProcControlDefOriginMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 29),
    _SleOSPFProcControlDefOriginMetric_Type()
)
sleOSPFProcControlDefOriginMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlDefOriginMetric.setStatus("current")


class _SleOSPFProcControlDefOriginRouteMap_Type(OctetString):
    """Custom type sleOSPFProcControlDefOriginRouteMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleOSPFProcControlDefOriginRouteMap_Type.__name__ = "OctetString"
_SleOSPFProcControlDefOriginRouteMap_Object = MibScalar
sleOSPFProcControlDefOriginRouteMap = _SleOSPFProcControlDefOriginRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 30),
    _SleOSPFProcControlDefOriginRouteMap_Type()
)
sleOSPFProcControlDefOriginRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlDefOriginRouteMap.setStatus("current")


class _SleOSPFProcControlLogNeighborChange_Type(Integer32):
    """Custom type sleOSPFProcControlLogNeighborChange based on Integer32"""
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


_SleOSPFProcControlLogNeighborChange_Type.__name__ = "Integer32"
_SleOSPFProcControlLogNeighborChange_Object = MibScalar
sleOSPFProcControlLogNeighborChange = _SleOSPFProcControlLogNeighborChange_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 31),
    _SleOSPFProcControlLogNeighborChange_Type()
)
sleOSPFProcControlLogNeighborChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlLogNeighborChange.setStatus("current")


class _SleOSPFProcControlPassiveIFAll_Type(Integer32):
    """Custom type sleOSPFProcControlPassiveIFAll based on Integer32"""
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


_SleOSPFProcControlPassiveIFAll_Type.__name__ = "Integer32"
_SleOSPFProcControlPassiveIFAll_Object = MibScalar
sleOSPFProcControlPassiveIFAll = _SleOSPFProcControlPassiveIFAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 32),
    _SleOSPFProcControlPassiveIFAll_Type()
)
sleOSPFProcControlPassiveIFAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlPassiveIFAll.setStatus("current")


class _SleOSPFProcControlBfdIFAll_Type(Integer32):
    """Custom type sleOSPFProcControlBfdIFAll based on Integer32"""
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


_SleOSPFProcControlBfdIFAll_Type.__name__ = "Integer32"
_SleOSPFProcControlBfdIFAll_Object = MibScalar
sleOSPFProcControlBfdIFAll = _SleOSPFProcControlBfdIFAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 33),
    _SleOSPFProcControlBfdIFAll_Type()
)
sleOSPFProcControlBfdIFAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlBfdIFAll.setStatus("current")


class _SleOSPFProcControlEfmIFAll_Type(Integer32):
    """Custom type sleOSPFProcControlEfmIFAll based on Integer32"""
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


_SleOSPFProcControlEfmIFAll_Type.__name__ = "Integer32"
_SleOSPFProcControlEfmIFAll_Object = MibScalar
sleOSPFProcControlEfmIFAll = _SleOSPFProcControlEfmIFAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 34),
    _SleOSPFProcControlEfmIFAll_Type()
)
sleOSPFProcControlEfmIFAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlEfmIFAll.setStatus("current")


class _SleOSPFProcControlCapabilityRestart_Type(Integer32):
    """Custom type sleOSPFProcControlCapabilityRestart based on Integer32"""
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
          ("graceful", 1),
          ("signaling", 2),
          ("gracefulAck", 3))
    )


_SleOSPFProcControlCapabilityRestart_Type.__name__ = "Integer32"
_SleOSPFProcControlCapabilityRestart_Object = MibScalar
sleOSPFProcControlCapabilityRestart = _SleOSPFProcControlCapabilityRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 35),
    _SleOSPFProcControlCapabilityRestart_Type()
)
sleOSPFProcControlCapabilityRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlCapabilityRestart.setStatus("current")


class _SleOSPFProcControlVRIndex_Type(Integer32):
    """Custom type sleOSPFProcControlVRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcControlVRIndex_Type.__name__ = "Integer32"
_SleOSPFProcControlVRIndex_Object = MibScalar
sleOSPFProcControlVRIndex = _SleOSPFProcControlVRIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 36),
    _SleOSPFProcControlVRIndex_Type()
)
sleOSPFProcControlVRIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlVRIndex.setStatus("current")


class _SleOSPFProcControlVRFName_Type(OctetString):
    """Custom type sleOSPFProcControlVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleOSPFProcControlVRFName_Type.__name__ = "OctetString"
_SleOSPFProcControlVRFName_Object = MibScalar
sleOSPFProcControlVRFName = _SleOSPFProcControlVRFName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 37),
    _SleOSPFProcControlVRFName_Type()
)
sleOSPFProcControlVRFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlVRFName.setStatus("current")


class _SleOSPFProcControlSPFStartDelay_Type(Integer32):
    """Custom type sleOSPFProcControlSPFStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcControlSPFStartDelay_Type.__name__ = "Integer32"
_SleOSPFProcControlSPFStartDelay_Object = MibScalar
sleOSPFProcControlSPFStartDelay = _SleOSPFProcControlSPFStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 38),
    _SleOSPFProcControlSPFStartDelay_Type()
)
sleOSPFProcControlSPFStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlSPFStartDelay.setStatus("current")


class _SleOSPFProcControlSPFMinDelay_Type(Integer32):
    """Custom type sleOSPFProcControlSPFMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcControlSPFMinDelay_Type.__name__ = "Integer32"
_SleOSPFProcControlSPFMinDelay_Object = MibScalar
sleOSPFProcControlSPFMinDelay = _SleOSPFProcControlSPFMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 39),
    _SleOSPFProcControlSPFMinDelay_Type()
)
sleOSPFProcControlSPFMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlSPFMinDelay.setStatus("current")


class _SleOSPFProcControlSPFMaxDelay_Type(Integer32):
    """Custom type sleOSPFProcControlSPFMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcControlSPFMaxDelay_Type.__name__ = "Integer32"
_SleOSPFProcControlSPFMaxDelay_Object = MibScalar
sleOSPFProcControlSPFMaxDelay = _SleOSPFProcControlSPFMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 40),
    _SleOSPFProcControlSPFMaxDelay_Type()
)
sleOSPFProcControlSPFMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlSPFMaxDelay.setStatus("current")


class _SleOSPFProcControlLSAStartDelay_Type(Integer32):
    """Custom type sleOSPFProcControlLSAStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcControlLSAStartDelay_Type.__name__ = "Integer32"
_SleOSPFProcControlLSAStartDelay_Object = MibScalar
sleOSPFProcControlLSAStartDelay = _SleOSPFProcControlLSAStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 41),
    _SleOSPFProcControlLSAStartDelay_Type()
)
sleOSPFProcControlLSAStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlLSAStartDelay.setStatus("current")


class _SleOSPFProcControlLSAMinDelay_Type(Integer32):
    """Custom type sleOSPFProcControlLSAMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcControlLSAMinDelay_Type.__name__ = "Integer32"
_SleOSPFProcControlLSAMinDelay_Object = MibScalar
sleOSPFProcControlLSAMinDelay = _SleOSPFProcControlLSAMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 42),
    _SleOSPFProcControlLSAMinDelay_Type()
)
sleOSPFProcControlLSAMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlLSAMinDelay.setStatus("current")


class _SleOSPFProcControlLSAMaxDelay_Type(Integer32):
    """Custom type sleOSPFProcControlLSAMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcControlLSAMaxDelay_Type.__name__ = "Integer32"
_SleOSPFProcControlLSAMaxDelay_Object = MibScalar
sleOSPFProcControlLSAMaxDelay = _SleOSPFProcControlLSAMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 43),
    _SleOSPFProcControlLSAMaxDelay_Type()
)
sleOSPFProcControlLSAMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlLSAMaxDelay.setStatus("current")


class _SleOSPFProcControlLSAArrivalDelay_Type(Integer32):
    """Custom type sleOSPFProcControlLSAArrivalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_SleOSPFProcControlLSAArrivalDelay_Type.__name__ = "Integer32"
_SleOSPFProcControlLSAArrivalDelay_Object = MibScalar
sleOSPFProcControlLSAArrivalDelay = _SleOSPFProcControlLSAArrivalDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 2, 44),
    _SleOSPFProcControlLSAArrivalDelay_Type()
)
sleOSPFProcControlLSAArrivalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcControlLSAArrivalDelay.setStatus("current")
_SleOSPFProcInfoNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcInfoNotification = _SleOSPFProcInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3)
)
_SleOSPFProcNetwork_ObjectIdentity = ObjectIdentity
sleOSPFProcNetwork = _SleOSPFProcNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2)
)
_SleOSPFProcNetworkTable_Object = MibTable
sleOSPFProcNetworkTable = _SleOSPFProcNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcNetworkTable.setStatus("current")
_SleOSPFProcNetworkEntry_Object = MibTableRow
sleOSPFProcNetworkEntry = _SleOSPFProcNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 1, 1)
)
sleOSPFProcNetworkEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcNetworkIP"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcNetworkIPMask"),
)
if mibBuilder.loadTexts:
    sleOSPFProcNetworkEntry.setStatus("current")
_SleOSPFProcNetworkIP_Type = IpAddress
_SleOSPFProcNetworkIP_Object = MibTableColumn
sleOSPFProcNetworkIP = _SleOSPFProcNetworkIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 1, 1, 1),
    _SleOSPFProcNetworkIP_Type()
)
sleOSPFProcNetworkIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkIP.setStatus("current")


class _SleOSPFProcNetworkIPMask_Type(Integer32):
    """Custom type sleOSPFProcNetworkIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleOSPFProcNetworkIPMask_Type.__name__ = "Integer32"
_SleOSPFProcNetworkIPMask_Object = MibTableColumn
sleOSPFProcNetworkIPMask = _SleOSPFProcNetworkIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 1, 1, 2),
    _SleOSPFProcNetworkIPMask_Type()
)
sleOSPFProcNetworkIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkIPMask.setStatus("current")
_SleOSPFProcNetworkAreaID_Type = IpAddress
_SleOSPFProcNetworkAreaID_Object = MibTableColumn
sleOSPFProcNetworkAreaID = _SleOSPFProcNetworkAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 1, 1, 3),
    _SleOSPFProcNetworkAreaID_Type()
)
sleOSPFProcNetworkAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkAreaID.setStatus("current")
_SleOSPFProcNetworkControl_ObjectIdentity = ObjectIdentity
sleOSPFProcNetworkControl = _SleOSPFProcNetworkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2)
)


class _SleOSPFProcNetworkControlRequest_Type(Integer32):
    """Custom type sleOSPFProcNetworkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcNetwork", 1),
          ("deleteOSPFProcNetwork", 2))
    )


_SleOSPFProcNetworkControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcNetworkControlRequest_Object = MibScalar
sleOSPFProcNetworkControlRequest = _SleOSPFProcNetworkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 1),
    _SleOSPFProcNetworkControlRequest_Type()
)
sleOSPFProcNetworkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlRequest.setStatus("current")
_SleOSPFProcNetworkControlStatus_Type = SleControlStatusType
_SleOSPFProcNetworkControlStatus_Object = MibScalar
sleOSPFProcNetworkControlStatus = _SleOSPFProcNetworkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 2),
    _SleOSPFProcNetworkControlStatus_Type()
)
sleOSPFProcNetworkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlStatus.setStatus("current")
_SleOSPFProcNetworkControlTimer_Type = Gauge32
_SleOSPFProcNetworkControlTimer_Object = MibScalar
sleOSPFProcNetworkControlTimer = _SleOSPFProcNetworkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 3),
    _SleOSPFProcNetworkControlTimer_Type()
)
sleOSPFProcNetworkControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlTimer.setStatus("current")
_SleOSPFProcNetworkControlTimeStamp_Type = TimeTicks
_SleOSPFProcNetworkControlTimeStamp_Object = MibScalar
sleOSPFProcNetworkControlTimeStamp = _SleOSPFProcNetworkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 4),
    _SleOSPFProcNetworkControlTimeStamp_Type()
)
sleOSPFProcNetworkControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlTimeStamp.setStatus("current")
_SleOSPFProcNetworkControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcNetworkControlReqResult_Object = MibScalar
sleOSPFProcNetworkControlReqResult = _SleOSPFProcNetworkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 5),
    _SleOSPFProcNetworkControlReqResult_Type()
)
sleOSPFProcNetworkControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlReqResult.setStatus("current")


class _SleOSPFProcNetworkControlProcID_Type(Integer32):
    """Custom type sleOSPFProcNetworkControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcNetworkControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcNetworkControlProcID_Object = MibScalar
sleOSPFProcNetworkControlProcID = _SleOSPFProcNetworkControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 6),
    _SleOSPFProcNetworkControlProcID_Type()
)
sleOSPFProcNetworkControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlProcID.setStatus("current")
_SleOSPFProcNetworkControlIP_Type = IpAddress
_SleOSPFProcNetworkControlIP_Object = MibScalar
sleOSPFProcNetworkControlIP = _SleOSPFProcNetworkControlIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 7),
    _SleOSPFProcNetworkControlIP_Type()
)
sleOSPFProcNetworkControlIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlIP.setStatus("current")


class _SleOSPFProcNetworkControlIPMask_Type(Integer32):
    """Custom type sleOSPFProcNetworkControlIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleOSPFProcNetworkControlIPMask_Type.__name__ = "Integer32"
_SleOSPFProcNetworkControlIPMask_Object = MibScalar
sleOSPFProcNetworkControlIPMask = _SleOSPFProcNetworkControlIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 8),
    _SleOSPFProcNetworkControlIPMask_Type()
)
sleOSPFProcNetworkControlIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlIPMask.setStatus("current")
_SleOSPFProcNetworkControlAreaID_Type = IpAddress
_SleOSPFProcNetworkControlAreaID_Object = MibScalar
sleOSPFProcNetworkControlAreaID = _SleOSPFProcNetworkControlAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 2, 9),
    _SleOSPFProcNetworkControlAreaID_Type()
)
sleOSPFProcNetworkControlAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNetworkControlAreaID.setStatus("current")
_SleOSPFProcNetworkNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcNetworkNotification = _SleOSPFProcNetworkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 3)
)
_SleOSPFProcSummary_ObjectIdentity = ObjectIdentity
sleOSPFProcSummary = _SleOSPFProcSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3)
)
_SleOSPFProcSummaryTable_Object = MibTable
sleOSPFProcSummaryTable = _SleOSPFProcSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcSummaryTable.setStatus("current")
_SleOSPFProcSummaryEntry_Object = MibTableRow
sleOSPFProcSummaryEntry = _SleOSPFProcSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 1, 1)
)
sleOSPFProcSummaryEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcSummaryIPAddress"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcSummaryIPMask"),
)
if mibBuilder.loadTexts:
    sleOSPFProcSummaryEntry.setStatus("current")
_SleOSPFProcSummaryIPAddress_Type = IpAddress
_SleOSPFProcSummaryIPAddress_Object = MibTableColumn
sleOSPFProcSummaryIPAddress = _SleOSPFProcSummaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 1, 1, 1),
    _SleOSPFProcSummaryIPAddress_Type()
)
sleOSPFProcSummaryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryIPAddress.setStatus("current")


class _SleOSPFProcSummaryIPMask_Type(Integer32):
    """Custom type sleOSPFProcSummaryIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleOSPFProcSummaryIPMask_Type.__name__ = "Integer32"
_SleOSPFProcSummaryIPMask_Object = MibTableColumn
sleOSPFProcSummaryIPMask = _SleOSPFProcSummaryIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 1, 1, 2),
    _SleOSPFProcSummaryIPMask_Type()
)
sleOSPFProcSummaryIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryIPMask.setStatus("current")


class _SleOSPFProcSummaryTag_Type(Gauge32):
    """Custom type sleOSPFProcSummaryTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleOSPFProcSummaryTag_Type.__name__ = "Gauge32"
_SleOSPFProcSummaryTag_Object = MibTableColumn
sleOSPFProcSummaryTag = _SleOSPFProcSummaryTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 1, 1, 3),
    _SleOSPFProcSummaryTag_Type()
)
sleOSPFProcSummaryTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryTag.setStatus("current")


class _SleOSPFProcSummaryAdvertiseFlag_Type(Integer32):
    """Custom type sleOSPFProcSummaryAdvertiseFlag based on Integer32"""
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


_SleOSPFProcSummaryAdvertiseFlag_Type.__name__ = "Integer32"
_SleOSPFProcSummaryAdvertiseFlag_Object = MibTableColumn
sleOSPFProcSummaryAdvertiseFlag = _SleOSPFProcSummaryAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 1, 1, 4),
    _SleOSPFProcSummaryAdvertiseFlag_Type()
)
sleOSPFProcSummaryAdvertiseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryAdvertiseFlag.setStatus("current")
_SleOSPFProcSummaryControl_ObjectIdentity = ObjectIdentity
sleOSPFProcSummaryControl = _SleOSPFProcSummaryControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2)
)


class _SleOSPFProcSummaryControlRequest_Type(Integer32):
    """Custom type sleOSPFProcSummaryControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcSummary", 1),
          ("deleteOSPFProcSummary", 2),
          ("setOSPFProcSummary", 3))
    )


_SleOSPFProcSummaryControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcSummaryControlRequest_Object = MibScalar
sleOSPFProcSummaryControlRequest = _SleOSPFProcSummaryControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 1),
    _SleOSPFProcSummaryControlRequest_Type()
)
sleOSPFProcSummaryControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlRequest.setStatus("current")
_SleOSPFProcSummaryControlStatus_Type = SleControlStatusType
_SleOSPFProcSummaryControlStatus_Object = MibScalar
sleOSPFProcSummaryControlStatus = _SleOSPFProcSummaryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 2),
    _SleOSPFProcSummaryControlStatus_Type()
)
sleOSPFProcSummaryControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlStatus.setStatus("current")
_SleOSPFProcSummaryControlTimer_Type = Gauge32
_SleOSPFProcSummaryControlTimer_Object = MibScalar
sleOSPFProcSummaryControlTimer = _SleOSPFProcSummaryControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 3),
    _SleOSPFProcSummaryControlTimer_Type()
)
sleOSPFProcSummaryControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlTimer.setStatus("current")
_SleOSPFProcSummaryControlTimeStamp_Type = TimeTicks
_SleOSPFProcSummaryControlTimeStamp_Object = MibScalar
sleOSPFProcSummaryControlTimeStamp = _SleOSPFProcSummaryControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 4),
    _SleOSPFProcSummaryControlTimeStamp_Type()
)
sleOSPFProcSummaryControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlTimeStamp.setStatus("current")
_SleOSPFProcSummaryControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcSummaryControlReqResult_Object = MibScalar
sleOSPFProcSummaryControlReqResult = _SleOSPFProcSummaryControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 5),
    _SleOSPFProcSummaryControlReqResult_Type()
)
sleOSPFProcSummaryControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlReqResult.setStatus("current")


class _SleOSPFProcSummaryControlProcID_Type(Integer32):
    """Custom type sleOSPFProcSummaryControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcSummaryControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcSummaryControlProcID_Object = MibScalar
sleOSPFProcSummaryControlProcID = _SleOSPFProcSummaryControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 6),
    _SleOSPFProcSummaryControlProcID_Type()
)
sleOSPFProcSummaryControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlProcID.setStatus("current")
_SleOSPFProcSummaryControlIPAddress_Type = IpAddress
_SleOSPFProcSummaryControlIPAddress_Object = MibScalar
sleOSPFProcSummaryControlIPAddress = _SleOSPFProcSummaryControlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 7),
    _SleOSPFProcSummaryControlIPAddress_Type()
)
sleOSPFProcSummaryControlIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlIPAddress.setStatus("current")


class _SleOSPFProcSummaryControlIPMask_Type(Integer32):
    """Custom type sleOSPFProcSummaryControlIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleOSPFProcSummaryControlIPMask_Type.__name__ = "Integer32"
_SleOSPFProcSummaryControlIPMask_Object = MibScalar
sleOSPFProcSummaryControlIPMask = _SleOSPFProcSummaryControlIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 8),
    _SleOSPFProcSummaryControlIPMask_Type()
)
sleOSPFProcSummaryControlIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlIPMask.setStatus("current")


class _SleOSPFProcSummaryControlTag_Type(Gauge32):
    """Custom type sleOSPFProcSummaryControlTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SleOSPFProcSummaryControlTag_Type.__name__ = "Gauge32"
_SleOSPFProcSummaryControlTag_Object = MibScalar
sleOSPFProcSummaryControlTag = _SleOSPFProcSummaryControlTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 9),
    _SleOSPFProcSummaryControlTag_Type()
)
sleOSPFProcSummaryControlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlTag.setStatus("current")


class _SleOSPFProcSummaryControlAdvertiseFlag_Type(Integer32):
    """Custom type sleOSPFProcSummaryControlAdvertiseFlag based on Integer32"""
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


_SleOSPFProcSummaryControlAdvertiseFlag_Type.__name__ = "Integer32"
_SleOSPFProcSummaryControlAdvertiseFlag_Object = MibScalar
sleOSPFProcSummaryControlAdvertiseFlag = _SleOSPFProcSummaryControlAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 2, 10),
    _SleOSPFProcSummaryControlAdvertiseFlag_Type()
)
sleOSPFProcSummaryControlAdvertiseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcSummaryControlAdvertiseFlag.setStatus("current")
_SleOSPFProcSummaryNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcSummaryNotification = _SleOSPFProcSummaryNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 3)
)
_SleOSPFProcDistributeList_ObjectIdentity = ObjectIdentity
sleOSPFProcDistributeList = _SleOSPFProcDistributeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4)
)
_SleOSPFProcDistributeListTable_Object = MibTable
sleOSPFProcDistributeListTable = _SleOSPFProcDistributeListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListTable.setStatus("current")
_SleOSPFProcDistributeListEntry_Object = MibTableRow
sleOSPFProcDistributeListEntry = _SleOSPFProcDistributeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 1, 1)
)
sleOSPFProcDistributeListEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcDistributeListOutFilterType"),
)
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListEntry.setStatus("current")


class _SleOSPFProcDistributeListOutFilterType_Type(Integer32):
    """Custom type sleOSPFProcDistributeListOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("bgp", 8))
    )


_SleOSPFProcDistributeListOutFilterType_Type.__name__ = "Integer32"
_SleOSPFProcDistributeListOutFilterType_Object = MibTableColumn
sleOSPFProcDistributeListOutFilterType = _SleOSPFProcDistributeListOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 1, 1, 1),
    _SleOSPFProcDistributeListOutFilterType_Type()
)
sleOSPFProcDistributeListOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListOutFilterType.setStatus("current")
_SleOSPFProcDistributeListAccessName_Type = OctetString
_SleOSPFProcDistributeListAccessName_Object = MibTableColumn
sleOSPFProcDistributeListAccessName = _SleOSPFProcDistributeListAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 1, 1, 2),
    _SleOSPFProcDistributeListAccessName_Type()
)
sleOSPFProcDistributeListAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListAccessName.setStatus("current")
_SleOSPFProcDistributeListControl_ObjectIdentity = ObjectIdentity
sleOSPFProcDistributeListControl = _SleOSPFProcDistributeListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2)
)


class _SleOSPFProcDistributeListControlRequest_Type(Integer32):
    """Custom type sleOSPFProcDistributeListControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcDistributeList", 1),
          ("deleteOSPFProcDistributeList", 2))
    )


_SleOSPFProcDistributeListControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcDistributeListControlRequest_Object = MibScalar
sleOSPFProcDistributeListControlRequest = _SleOSPFProcDistributeListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 1),
    _SleOSPFProcDistributeListControlRequest_Type()
)
sleOSPFProcDistributeListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlRequest.setStatus("current")
_SleOSPFProcDistributeListControlStatus_Type = SleControlStatusType
_SleOSPFProcDistributeListControlStatus_Object = MibScalar
sleOSPFProcDistributeListControlStatus = _SleOSPFProcDistributeListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 2),
    _SleOSPFProcDistributeListControlStatus_Type()
)
sleOSPFProcDistributeListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlStatus.setStatus("current")
_SleOSPFProcDistributeListControlTimer_Type = Gauge32
_SleOSPFProcDistributeListControlTimer_Object = MibScalar
sleOSPFProcDistributeListControlTimer = _SleOSPFProcDistributeListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 3),
    _SleOSPFProcDistributeListControlTimer_Type()
)
sleOSPFProcDistributeListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlTimer.setStatus("current")
_SleOSPFProcDistributeListControlTimeStamp_Type = TimeTicks
_SleOSPFProcDistributeListControlTimeStamp_Object = MibScalar
sleOSPFProcDistributeListControlTimeStamp = _SleOSPFProcDistributeListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 4),
    _SleOSPFProcDistributeListControlTimeStamp_Type()
)
sleOSPFProcDistributeListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlTimeStamp.setStatus("current")
_SleOSPFProcDistributeListControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcDistributeListControlReqResult_Object = MibScalar
sleOSPFProcDistributeListControlReqResult = _SleOSPFProcDistributeListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 5),
    _SleOSPFProcDistributeListControlReqResult_Type()
)
sleOSPFProcDistributeListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlReqResult.setStatus("current")


class _SleOSPFProcDistributeListControlProcID_Type(Integer32):
    """Custom type sleOSPFProcDistributeListControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcDistributeListControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcDistributeListControlProcID_Object = MibScalar
sleOSPFProcDistributeListControlProcID = _SleOSPFProcDistributeListControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 6),
    _SleOSPFProcDistributeListControlProcID_Type()
)
sleOSPFProcDistributeListControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlProcID.setStatus("current")


class _SleOSPFProcDistributeListControlOutFilterType_Type(Integer32):
    """Custom type sleOSPFProcDistributeListControlOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("bgp", 8))
    )


_SleOSPFProcDistributeListControlOutFilterType_Type.__name__ = "Integer32"
_SleOSPFProcDistributeListControlOutFilterType_Object = MibScalar
sleOSPFProcDistributeListControlOutFilterType = _SleOSPFProcDistributeListControlOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 7),
    _SleOSPFProcDistributeListControlOutFilterType_Type()
)
sleOSPFProcDistributeListControlOutFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlOutFilterType.setStatus("current")
_SleOSPFProcDistributeListControlAccessName_Type = OctetString
_SleOSPFProcDistributeListControlAccessName_Object = MibScalar
sleOSPFProcDistributeListControlAccessName = _SleOSPFProcDistributeListControlAccessName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 2, 8),
    _SleOSPFProcDistributeListControlAccessName_Type()
)
sleOSPFProcDistributeListControlAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcDistributeListControlAccessName.setStatus("current")
_SleOSPFProcDistributeListNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcDistributeListNotification = _SleOSPFProcDistributeListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 3)
)
_SleOSPFProcNeighbor_ObjectIdentity = ObjectIdentity
sleOSPFProcNeighbor = _SleOSPFProcNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5)
)
_SleOSPFProcNeighborTable_Object = MibTable
sleOSPFProcNeighborTable = _SleOSPFProcNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcNeighborTable.setStatus("current")
_SleOSPFProcNeighborEntry_Object = MibTableRow
sleOSPFProcNeighborEntry = _SleOSPFProcNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 1, 1)
)
sleOSPFProcNeighborEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcNeighborIPAddr"),
)
if mibBuilder.loadTexts:
    sleOSPFProcNeighborEntry.setStatus("current")
_SleOSPFProcNeighborIPAddr_Type = IpAddress
_SleOSPFProcNeighborIPAddr_Object = MibTableColumn
sleOSPFProcNeighborIPAddr = _SleOSPFProcNeighborIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 1, 1, 1),
    _SleOSPFProcNeighborIPAddr_Type()
)
sleOSPFProcNeighborIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborIPAddr.setStatus("current")


class _SleOSPFProcNeighborPriority_Type(Integer32):
    """Custom type sleOSPFProcNeighborPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleOSPFProcNeighborPriority_Type.__name__ = "Integer32"
_SleOSPFProcNeighborPriority_Object = MibTableColumn
sleOSPFProcNeighborPriority = _SleOSPFProcNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 1, 1, 2),
    _SleOSPFProcNeighborPriority_Type()
)
sleOSPFProcNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborPriority.setStatus("current")


class _SleOSPFProcNeighborPollInterval_Type(Integer32):
    """Custom type sleOSPFProcNeighborPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcNeighborPollInterval_Type.__name__ = "Integer32"
_SleOSPFProcNeighborPollInterval_Object = MibTableColumn
sleOSPFProcNeighborPollInterval = _SleOSPFProcNeighborPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 1, 1, 3),
    _SleOSPFProcNeighborPollInterval_Type()
)
sleOSPFProcNeighborPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborPollInterval.setStatus("current")


class _SleOSPFProcNeighborCost_Type(Integer32):
    """Custom type sleOSPFProcNeighborCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcNeighborCost_Type.__name__ = "Integer32"
_SleOSPFProcNeighborCost_Object = MibTableColumn
sleOSPFProcNeighborCost = _SleOSPFProcNeighborCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 1, 1, 4),
    _SleOSPFProcNeighborCost_Type()
)
sleOSPFProcNeighborCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborCost.setStatus("current")
_SleOSPFProcNeighborControl_ObjectIdentity = ObjectIdentity
sleOSPFProcNeighborControl = _SleOSPFProcNeighborControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2)
)


class _SleOSPFProcNeighborControlRequest_Type(Integer32):
    """Custom type sleOSPFProcNeighborControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcNeighbor", 1),
          ("deleteOSPFProcNeighbor", 2),
          ("setOSPFProcNeighbor", 3))
    )


_SleOSPFProcNeighborControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcNeighborControlRequest_Object = MibScalar
sleOSPFProcNeighborControlRequest = _SleOSPFProcNeighborControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 1),
    _SleOSPFProcNeighborControlRequest_Type()
)
sleOSPFProcNeighborControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlRequest.setStatus("current")
_SleOSPFProcNeighborControlStatus_Type = SleControlStatusType
_SleOSPFProcNeighborControlStatus_Object = MibScalar
sleOSPFProcNeighborControlStatus = _SleOSPFProcNeighborControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 2),
    _SleOSPFProcNeighborControlStatus_Type()
)
sleOSPFProcNeighborControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlStatus.setStatus("current")
_SleOSPFProcNeighborControlTimer_Type = Gauge32
_SleOSPFProcNeighborControlTimer_Object = MibScalar
sleOSPFProcNeighborControlTimer = _SleOSPFProcNeighborControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 3),
    _SleOSPFProcNeighborControlTimer_Type()
)
sleOSPFProcNeighborControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlTimer.setStatus("current")
_SleOSPFProcNeighborControlTimeStamp_Type = TimeTicks
_SleOSPFProcNeighborControlTimeStamp_Object = MibScalar
sleOSPFProcNeighborControlTimeStamp = _SleOSPFProcNeighborControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 4),
    _SleOSPFProcNeighborControlTimeStamp_Type()
)
sleOSPFProcNeighborControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlTimeStamp.setStatus("current")
_SleOSPFProcNeighborControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcNeighborControlReqResult_Object = MibScalar
sleOSPFProcNeighborControlReqResult = _SleOSPFProcNeighborControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 5),
    _SleOSPFProcNeighborControlReqResult_Type()
)
sleOSPFProcNeighborControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlReqResult.setStatus("current")


class _SleOSPFProcNeighborControlProcID_Type(Integer32):
    """Custom type sleOSPFProcNeighborControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcNeighborControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcNeighborControlProcID_Object = MibScalar
sleOSPFProcNeighborControlProcID = _SleOSPFProcNeighborControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 6),
    _SleOSPFProcNeighborControlProcID_Type()
)
sleOSPFProcNeighborControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlProcID.setStatus("current")
_SleOSPFProcNeighborControlIPAddr_Type = IpAddress
_SleOSPFProcNeighborControlIPAddr_Object = MibScalar
sleOSPFProcNeighborControlIPAddr = _SleOSPFProcNeighborControlIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 7),
    _SleOSPFProcNeighborControlIPAddr_Type()
)
sleOSPFProcNeighborControlIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlIPAddr.setStatus("current")


class _SleOSPFProcNeighborControlPriority_Type(Integer32):
    """Custom type sleOSPFProcNeighborControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleOSPFProcNeighborControlPriority_Type.__name__ = "Integer32"
_SleOSPFProcNeighborControlPriority_Object = MibScalar
sleOSPFProcNeighborControlPriority = _SleOSPFProcNeighborControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 8),
    _SleOSPFProcNeighborControlPriority_Type()
)
sleOSPFProcNeighborControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlPriority.setStatus("current")


class _SleOSPFProcNeighborControlPollInterval_Type(Integer32):
    """Custom type sleOSPFProcNeighborControlPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcNeighborControlPollInterval_Type.__name__ = "Integer32"
_SleOSPFProcNeighborControlPollInterval_Object = MibScalar
sleOSPFProcNeighborControlPollInterval = _SleOSPFProcNeighborControlPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 9),
    _SleOSPFProcNeighborControlPollInterval_Type()
)
sleOSPFProcNeighborControlPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlPollInterval.setStatus("current")


class _SleOSPFProcNeighborControlCost_Type(Integer32):
    """Custom type sleOSPFProcNeighborControlCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcNeighborControlCost_Type.__name__ = "Integer32"
_SleOSPFProcNeighborControlCost_Object = MibScalar
sleOSPFProcNeighborControlCost = _SleOSPFProcNeighborControlCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 2, 10),
    _SleOSPFProcNeighborControlCost_Type()
)
sleOSPFProcNeighborControlCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcNeighborControlCost.setStatus("current")
_SleOSPFProcNeighborNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcNeighborNotification = _SleOSPFProcNeighborNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 3)
)
_SleOSPFProcPassIf_ObjectIdentity = ObjectIdentity
sleOSPFProcPassIf = _SleOSPFProcPassIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6)
)
_SleOSPFProcPassIfTable_Object = MibTable
sleOSPFProcPassIfTable = _SleOSPFProcPassIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcPassIfTable.setStatus("current")
_SleOSPFProcPassIfEntry_Object = MibTableRow
sleOSPFProcPassIfEntry = _SleOSPFProcPassIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 1, 1)
)
sleOSPFProcPassIfEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcPassIfAddr"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcPassIfName"),
)
if mibBuilder.loadTexts:
    sleOSPFProcPassIfEntry.setStatus("current")
_SleOSPFProcPassIfAddr_Type = IpAddress
_SleOSPFProcPassIfAddr_Object = MibTableColumn
sleOSPFProcPassIfAddr = _SleOSPFProcPassIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 1, 1, 1),
    _SleOSPFProcPassIfAddr_Type()
)
sleOSPFProcPassIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfAddr.setStatus("current")
_SleOSPFProcPassIfName_Type = OctetString
_SleOSPFProcPassIfName_Object = MibTableColumn
sleOSPFProcPassIfName = _SleOSPFProcPassIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 1, 1, 2),
    _SleOSPFProcPassIfName_Type()
)
sleOSPFProcPassIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfName.setStatus("current")
_SleOSPFProcPassIfControl_ObjectIdentity = ObjectIdentity
sleOSPFProcPassIfControl = _SleOSPFProcPassIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2)
)


class _SleOSPFProcPassIfControlRequest_Type(Integer32):
    """Custom type sleOSPFProcPassIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcPassInterface", 1),
          ("deleteOSPFProcPassInterface", 2))
    )


_SleOSPFProcPassIfControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcPassIfControlRequest_Object = MibScalar
sleOSPFProcPassIfControlRequest = _SleOSPFProcPassIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 1),
    _SleOSPFProcPassIfControlRequest_Type()
)
sleOSPFProcPassIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlRequest.setStatus("current")
_SleOSPFProcPassIfControlStatus_Type = SleControlStatusType
_SleOSPFProcPassIfControlStatus_Object = MibScalar
sleOSPFProcPassIfControlStatus = _SleOSPFProcPassIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 2),
    _SleOSPFProcPassIfControlStatus_Type()
)
sleOSPFProcPassIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlStatus.setStatus("current")
_SleOSPFProcPassIfControlTimer_Type = Gauge32
_SleOSPFProcPassIfControlTimer_Object = MibScalar
sleOSPFProcPassIfControlTimer = _SleOSPFProcPassIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 3),
    _SleOSPFProcPassIfControlTimer_Type()
)
sleOSPFProcPassIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlTimer.setStatus("current")
_SleOSPFProcPassIfControlTimeStamp_Type = TimeTicks
_SleOSPFProcPassIfControlTimeStamp_Object = MibScalar
sleOSPFProcPassIfControlTimeStamp = _SleOSPFProcPassIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 4),
    _SleOSPFProcPassIfControlTimeStamp_Type()
)
sleOSPFProcPassIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlTimeStamp.setStatus("current")
_SleOSPFProcPassIfControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcPassIfControlReqResult_Object = MibScalar
sleOSPFProcPassIfControlReqResult = _SleOSPFProcPassIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 5),
    _SleOSPFProcPassIfControlReqResult_Type()
)
sleOSPFProcPassIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlReqResult.setStatus("current")


class _SleOSPFProcPassIfControlProcID_Type(Integer32):
    """Custom type sleOSPFProcPassIfControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcPassIfControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcPassIfControlProcID_Object = MibScalar
sleOSPFProcPassIfControlProcID = _SleOSPFProcPassIfControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 6),
    _SleOSPFProcPassIfControlProcID_Type()
)
sleOSPFProcPassIfControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlProcID.setStatus("current")
_SleOSPFProcPassIfControlIPAddr_Type = IpAddress
_SleOSPFProcPassIfControlIPAddr_Object = MibScalar
sleOSPFProcPassIfControlIPAddr = _SleOSPFProcPassIfControlIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 7),
    _SleOSPFProcPassIfControlIPAddr_Type()
)
sleOSPFProcPassIfControlIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlIPAddr.setStatus("current")
_SleOSPFProcPassIfControlName_Type = OctetString
_SleOSPFProcPassIfControlName_Object = MibScalar
sleOSPFProcPassIfControlName = _SleOSPFProcPassIfControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 2, 8),
    _SleOSPFProcPassIfControlName_Type()
)
sleOSPFProcPassIfControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcPassIfControlName.setStatus("current")
_SleOSPFProcPassIfNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcPassIfNotification = _SleOSPFProcPassIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 3)
)
_SleOSPFProcHost_ObjectIdentity = ObjectIdentity
sleOSPFProcHost = _SleOSPFProcHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7)
)
_SleOSPFProcHostTable_Object = MibTable
sleOSPFProcHostTable = _SleOSPFProcHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcHostTable.setStatus("current")
_SleOSPFProcHostEntry_Object = MibTableRow
sleOSPFProcHostEntry = _SleOSPFProcHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 1, 1)
)
sleOSPFProcHostEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcHostIPAddr"),
)
if mibBuilder.loadTexts:
    sleOSPFProcHostEntry.setStatus("current")
_SleOSPFProcHostIPAddr_Type = IpAddress
_SleOSPFProcHostIPAddr_Object = MibTableColumn
sleOSPFProcHostIPAddr = _SleOSPFProcHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 1, 1, 1),
    _SleOSPFProcHostIPAddr_Type()
)
sleOSPFProcHostIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcHostIPAddr.setStatus("current")
_SleOSPFProcHostAreaID_Type = IpAddress
_SleOSPFProcHostAreaID_Object = MibTableColumn
sleOSPFProcHostAreaID = _SleOSPFProcHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 1, 1, 2),
    _SleOSPFProcHostAreaID_Type()
)
sleOSPFProcHostAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcHostAreaID.setStatus("current")


class _SleOSPFProcHostAreaCost_Type(Integer32):
    """Custom type sleOSPFProcHostAreaCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcHostAreaCost_Type.__name__ = "Integer32"
_SleOSPFProcHostAreaCost_Object = MibTableColumn
sleOSPFProcHostAreaCost = _SleOSPFProcHostAreaCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 1, 1, 3),
    _SleOSPFProcHostAreaCost_Type()
)
sleOSPFProcHostAreaCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcHostAreaCost.setStatus("current")
_SleOSPFProcHostControl_ObjectIdentity = ObjectIdentity
sleOSPFProcHostControl = _SleOSPFProcHostControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2)
)


class _SleOSPFProcHostControlRequest_Type(Integer32):
    """Custom type sleOSPFProcHostControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcHost", 1),
          ("deleteOSPFProcHost", 2),
          ("setOSPFProcHostCost", 3))
    )


_SleOSPFProcHostControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcHostControlRequest_Object = MibScalar
sleOSPFProcHostControlRequest = _SleOSPFProcHostControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 1),
    _SleOSPFProcHostControlRequest_Type()
)
sleOSPFProcHostControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlRequest.setStatus("current")
_SleOSPFProcHostControlStatus_Type = SleControlStatusType
_SleOSPFProcHostControlStatus_Object = MibScalar
sleOSPFProcHostControlStatus = _SleOSPFProcHostControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 2),
    _SleOSPFProcHostControlStatus_Type()
)
sleOSPFProcHostControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlStatus.setStatus("current")
_SleOSPFProcHostControlTimer_Type = Gauge32
_SleOSPFProcHostControlTimer_Object = MibScalar
sleOSPFProcHostControlTimer = _SleOSPFProcHostControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 3),
    _SleOSPFProcHostControlTimer_Type()
)
sleOSPFProcHostControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlTimer.setStatus("current")
_SleOSPFProcHostControlTimeStamp_Type = TimeTicks
_SleOSPFProcHostControlTimeStamp_Object = MibScalar
sleOSPFProcHostControlTimeStamp = _SleOSPFProcHostControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 4),
    _SleOSPFProcHostControlTimeStamp_Type()
)
sleOSPFProcHostControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlTimeStamp.setStatus("current")
_SleOSPFProcHostControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcHostControlReqResult_Object = MibScalar
sleOSPFProcHostControlReqResult = _SleOSPFProcHostControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 5),
    _SleOSPFProcHostControlReqResult_Type()
)
sleOSPFProcHostControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlReqResult.setStatus("current")


class _SleOSPFProcHostControlProcID_Type(Integer32):
    """Custom type sleOSPFProcHostControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcHostControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcHostControlProcID_Object = MibScalar
sleOSPFProcHostControlProcID = _SleOSPFProcHostControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 6),
    _SleOSPFProcHostControlProcID_Type()
)
sleOSPFProcHostControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlProcID.setStatus("current")
_SleOSPFProcHostControlIPAddr_Type = IpAddress
_SleOSPFProcHostControlIPAddr_Object = MibScalar
sleOSPFProcHostControlIPAddr = _SleOSPFProcHostControlIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 7),
    _SleOSPFProcHostControlIPAddr_Type()
)
sleOSPFProcHostControlIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlIPAddr.setStatus("current")
_SleOSPFProcHostControlAreaID_Type = IpAddress
_SleOSPFProcHostControlAreaID_Object = MibScalar
sleOSPFProcHostControlAreaID = _SleOSPFProcHostControlAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 8),
    _SleOSPFProcHostControlAreaID_Type()
)
sleOSPFProcHostControlAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlAreaID.setStatus("current")


class _SleOSPFProcHostControlAreaCost_Type(Integer32):
    """Custom type sleOSPFProcHostControlAreaCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleOSPFProcHostControlAreaCost_Type.__name__ = "Integer32"
_SleOSPFProcHostControlAreaCost_Object = MibScalar
sleOSPFProcHostControlAreaCost = _SleOSPFProcHostControlAreaCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 2, 9),
    _SleOSPFProcHostControlAreaCost_Type()
)
sleOSPFProcHostControlAreaCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcHostControlAreaCost.setStatus("current")
_SleOSPFProcHostNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcHostNotification = _SleOSPFProcHostNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 3)
)
_SleOSPFProcRedistribute_ObjectIdentity = ObjectIdentity
sleOSPFProcRedistribute = _SleOSPFProcRedistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8)
)
_SleOSPFProcRedistTable_Object = MibTable
sleOSPFProcRedistTable = _SleOSPFProcRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcRedistTable.setStatus("current")
_SleOSPFProcRedistEntry_Object = MibTableRow
sleOSPFProcRedistEntry = _SleOSPFProcRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1, 1)
)
sleOSPFProcRedistEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcRedistType"),
)
if mibBuilder.loadTexts:
    sleOSPFProcRedistEntry.setStatus("current")


class _SleOSPFProcRedistType_Type(Integer32):
    """Custom type sleOSPFProcRedistType based on Integer32"""
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
          ("bgp", 5))
    )


_SleOSPFProcRedistType_Type.__name__ = "Integer32"
_SleOSPFProcRedistType_Object = MibTableColumn
sleOSPFProcRedistType = _SleOSPFProcRedistType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1, 1, 1),
    _SleOSPFProcRedistType_Type()
)
sleOSPFProcRedistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistType.setStatus("current")


class _SleOSPFProcRedistMetricType_Type(Integer32):
    """Custom type sleOSPFProcRedistMetricType based on Integer32"""
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


_SleOSPFProcRedistMetricType_Type.__name__ = "Integer32"
_SleOSPFProcRedistMetricType_Object = MibTableColumn
sleOSPFProcRedistMetricType = _SleOSPFProcRedistMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1, 1, 2),
    _SleOSPFProcRedistMetricType_Type()
)
sleOSPFProcRedistMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistMetricType.setStatus("current")


class _SleOSPFProcRedistMetric_Type(Integer32):
    """Custom type sleOSPFProcRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleOSPFProcRedistMetric_Type.__name__ = "Integer32"
_SleOSPFProcRedistMetric_Object = MibTableColumn
sleOSPFProcRedistMetric = _SleOSPFProcRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1, 1, 3),
    _SleOSPFProcRedistMetric_Type()
)
sleOSPFProcRedistMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistMetric.setStatus("current")
_SleOSPFProcRedistRouteMapName_Type = OctetString
_SleOSPFProcRedistRouteMapName_Object = MibTableColumn
sleOSPFProcRedistRouteMapName = _SleOSPFProcRedistRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1, 1, 4),
    _SleOSPFProcRedistRouteMapName_Type()
)
sleOSPFProcRedistRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistRouteMapName.setStatus("current")


class _SleOSPFProcRedistTag_Type(Gauge32):
    """Custom type sleOSPFProcRedistTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleOSPFProcRedistTag_Type.__name__ = "Gauge32"
_SleOSPFProcRedistTag_Object = MibTableColumn
sleOSPFProcRedistTag = _SleOSPFProcRedistTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1, 1, 5),
    _SleOSPFProcRedistTag_Type()
)
sleOSPFProcRedistTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistTag.setStatus("current")


class _SleOSPFProcRedistSubnets_Type(Integer32):
    """Custom type sleOSPFProcRedistSubnets based on Integer32"""
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


_SleOSPFProcRedistSubnets_Type.__name__ = "Integer32"
_SleOSPFProcRedistSubnets_Object = MibTableColumn
sleOSPFProcRedistSubnets = _SleOSPFProcRedistSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 1, 1, 6),
    _SleOSPFProcRedistSubnets_Type()
)
sleOSPFProcRedistSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistSubnets.setStatus("current")
_SleOSPFProcRedistControl_ObjectIdentity = ObjectIdentity
sleOSPFProcRedistControl = _SleOSPFProcRedistControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2)
)


class _SleOSPFProcRedistControlRequest_Type(Integer32):
    """Custom type sleOSPFProcRedistControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFProcRedist", 1),
          ("deleteOSPFProcRedist", 2),
          ("setOSPFProcRedist", 3))
    )


_SleOSPFProcRedistControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcRedistControlRequest_Object = MibScalar
sleOSPFProcRedistControlRequest = _SleOSPFProcRedistControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 1),
    _SleOSPFProcRedistControlRequest_Type()
)
sleOSPFProcRedistControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlRequest.setStatus("current")
_SleOSPFProcRedistControlStatus_Type = SleControlStatusType
_SleOSPFProcRedistControlStatus_Object = MibScalar
sleOSPFProcRedistControlStatus = _SleOSPFProcRedistControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 2),
    _SleOSPFProcRedistControlStatus_Type()
)
sleOSPFProcRedistControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlStatus.setStatus("current")
_SleOSPFProcRedistControlTimer_Type = Gauge32
_SleOSPFProcRedistControlTimer_Object = MibScalar
sleOSPFProcRedistControlTimer = _SleOSPFProcRedistControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 3),
    _SleOSPFProcRedistControlTimer_Type()
)
sleOSPFProcRedistControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlTimer.setStatus("current")
_SleOSPFProcRedistControlTimeStamp_Type = TimeTicks
_SleOSPFProcRedistControlTimeStamp_Object = MibScalar
sleOSPFProcRedistControlTimeStamp = _SleOSPFProcRedistControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 4),
    _SleOSPFProcRedistControlTimeStamp_Type()
)
sleOSPFProcRedistControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlTimeStamp.setStatus("current")
_SleOSPFProcRedistControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcRedistControlReqResult_Object = MibScalar
sleOSPFProcRedistControlReqResult = _SleOSPFProcRedistControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 5),
    _SleOSPFProcRedistControlReqResult_Type()
)
sleOSPFProcRedistControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlReqResult.setStatus("current")


class _SleOSPFProcRedistControlProcID_Type(Integer32):
    """Custom type sleOSPFProcRedistControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcRedistControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcRedistControlProcID_Object = MibScalar
sleOSPFProcRedistControlProcID = _SleOSPFProcRedistControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 6),
    _SleOSPFProcRedistControlProcID_Type()
)
sleOSPFProcRedistControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlProcID.setStatus("current")


class _SleOSPFProcRedistControlType_Type(Integer32):
    """Custom type sleOSPFProcRedistControlType based on Integer32"""
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
          ("bgp", 5))
    )


_SleOSPFProcRedistControlType_Type.__name__ = "Integer32"
_SleOSPFProcRedistControlType_Object = MibScalar
sleOSPFProcRedistControlType = _SleOSPFProcRedistControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 7),
    _SleOSPFProcRedistControlType_Type()
)
sleOSPFProcRedistControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlType.setStatus("current")


class _SleOSPFProcRedistControlMetricType_Type(Integer32):
    """Custom type sleOSPFProcRedistControlMetricType based on Integer32"""
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


_SleOSPFProcRedistControlMetricType_Type.__name__ = "Integer32"
_SleOSPFProcRedistControlMetricType_Object = MibScalar
sleOSPFProcRedistControlMetricType = _SleOSPFProcRedistControlMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 8),
    _SleOSPFProcRedistControlMetricType_Type()
)
sleOSPFProcRedistControlMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlMetricType.setStatus("current")


class _SleOSPFProcRedistControlMetric_Type(Integer32):
    """Custom type sleOSPFProcRedistControlMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleOSPFProcRedistControlMetric_Type.__name__ = "Integer32"
_SleOSPFProcRedistControlMetric_Object = MibScalar
sleOSPFProcRedistControlMetric = _SleOSPFProcRedistControlMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 9),
    _SleOSPFProcRedistControlMetric_Type()
)
sleOSPFProcRedistControlMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlMetric.setStatus("current")
_SleOSPFProcRedistControlRouteMapName_Type = OctetString
_SleOSPFProcRedistControlRouteMapName_Object = MibScalar
sleOSPFProcRedistControlRouteMapName = _SleOSPFProcRedistControlRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 10),
    _SleOSPFProcRedistControlRouteMapName_Type()
)
sleOSPFProcRedistControlRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlRouteMapName.setStatus("current")


class _SleOSPFProcRedistControlTag_Type(Gauge32):
    """Custom type sleOSPFProcRedistControlTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleOSPFProcRedistControlTag_Type.__name__ = "Gauge32"
_SleOSPFProcRedistControlTag_Object = MibScalar
sleOSPFProcRedistControlTag = _SleOSPFProcRedistControlTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 11),
    _SleOSPFProcRedistControlTag_Type()
)
sleOSPFProcRedistControlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlTag.setStatus("current")


class _SleOSPFProcRedistControlSubnets_Type(Integer32):
    """Custom type sleOSPFProcRedistControlSubnets based on Integer32"""
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


_SleOSPFProcRedistControlSubnets_Type.__name__ = "Integer32"
_SleOSPFProcRedistControlSubnets_Object = MibScalar
sleOSPFProcRedistControlSubnets = _SleOSPFProcRedistControlSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 2, 12),
    _SleOSPFProcRedistControlSubnets_Type()
)
sleOSPFProcRedistControlSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcRedistControlSubnets.setStatus("current")
_SleOSPFProcRedistNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcRedistNotification = _SleOSPFProcRedistNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 3)
)
_SleOSPFProcArea_ObjectIdentity = ObjectIdentity
sleOSPFProcArea = _SleOSPFProcArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9)
)
_SleOSPFProcAreaInfo_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaInfo = _SleOSPFProcAreaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1)
)
_SleOSPFProcAreaInfoTable_Object = MibTable
sleOSPFProcAreaInfoTable = _SleOSPFProcAreaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaInfoTable.setStatus("current")
_SleOSPFProcAreaInfoEntry_Object = MibTableRow
sleOSPFProcAreaInfoEntry = _SleOSPFProcAreaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1)
)
sleOSPFProcAreaInfoEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaID"),
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaInfoEntry.setStatus("current")
_SleOSPFProcAreaID_Type = IpAddress
_SleOSPFProcAreaID_Object = MibTableColumn
sleOSPFProcAreaID = _SleOSPFProcAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 1),
    _SleOSPFProcAreaID_Type()
)
sleOSPFProcAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaID.setStatus("current")


class _SleOSPFProcAreaType_Type(Integer32):
    """Custom type sleOSPFProcAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("stub", 1),
          ("nssa", 2))
    )


_SleOSPFProcAreaType_Type.__name__ = "Integer32"
_SleOSPFProcAreaType_Object = MibTableColumn
sleOSPFProcAreaType = _SleOSPFProcAreaType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 2),
    _SleOSPFProcAreaType_Type()
)
sleOSPFProcAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaType.setStatus("current")


class _SleOSPFProcAreaDefaultCost_Type(Integer32):
    """Custom type sleOSPFProcAreaDefaultCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOSPFProcAreaDefaultCost_Type.__name__ = "Integer32"
_SleOSPFProcAreaDefaultCost_Object = MibTableColumn
sleOSPFProcAreaDefaultCost = _SleOSPFProcAreaDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 3),
    _SleOSPFProcAreaDefaultCost_Type()
)
sleOSPFProcAreaDefaultCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaDefaultCost.setStatus("current")


class _SleOSPFProcAreaAuthenType_Type(Integer32):
    """Custom type sleOSPFProcAreaAuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("simple", 1),
          ("crypt", 2))
    )


_SleOSPFProcAreaAuthenType_Type.__name__ = "Integer32"
_SleOSPFProcAreaAuthenType_Object = MibTableColumn
sleOSPFProcAreaAuthenType = _SleOSPFProcAreaAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 4),
    _SleOSPFProcAreaAuthenType_Type()
)
sleOSPFProcAreaAuthenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaAuthenType.setStatus("current")
_SleOSPFProcAreaFAInName_Type = OctetString
_SleOSPFProcAreaFAInName_Object = MibTableColumn
sleOSPFProcAreaFAInName = _SleOSPFProcAreaFAInName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 5),
    _SleOSPFProcAreaFAInName_Type()
)
sleOSPFProcAreaFAInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaFAInName.setStatus("current")
_SleOSPFProcAreaFAOutName_Type = ObjectIdentifier
_SleOSPFProcAreaFAOutName_Object = MibTableColumn
sleOSPFProcAreaFAOutName = _SleOSPFProcAreaFAOutName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 6),
    _SleOSPFProcAreaFAOutName_Type()
)
sleOSPFProcAreaFAOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaFAOutName.setStatus("current")
_SleOSPFProcAreaFPInName_Type = OctetString
_SleOSPFProcAreaFPInName_Object = MibTableColumn
sleOSPFProcAreaFPInName = _SleOSPFProcAreaFPInName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 7),
    _SleOSPFProcAreaFPInName_Type()
)
sleOSPFProcAreaFPInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaFPInName.setStatus("current")
_SleOSPFProcAreaFPOutName_Type = OctetString
_SleOSPFProcAreaFPOutName_Object = MibTableColumn
sleOSPFProcAreaFPOutName = _SleOSPFProcAreaFPOutName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 8),
    _SleOSPFProcAreaFPOutName_Type()
)
sleOSPFProcAreaFPOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaFPOutName.setStatus("current")


class _SleOSPFProcAreaShortcutType_Type(Integer32):
    """Custom type sleOSPFProcAreaShortcutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enable", 1),
          ("disable", 2))
    )


_SleOSPFProcAreaShortcutType_Type.__name__ = "Integer32"
_SleOSPFProcAreaShortcutType_Object = MibTableColumn
sleOSPFProcAreaShortcutType = _SleOSPFProcAreaShortcutType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 9),
    _SleOSPFProcAreaShortcutType_Type()
)
sleOSPFProcAreaShortcutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaShortcutType.setStatus("current")
_SleOSPFProcAreaSpfRuns_Type = Integer32
_SleOSPFProcAreaSpfRuns_Object = MibTableColumn
sleOSPFProcAreaSpfRuns = _SleOSPFProcAreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 10),
    _SleOSPFProcAreaSpfRuns_Type()
)
sleOSPFProcAreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaSpfRuns.setStatus("current")
_SleOSPFProcAreaLsaCount_Type = Integer32
_SleOSPFProcAreaLsaCount_Object = MibTableColumn
sleOSPFProcAreaLsaCount = _SleOSPFProcAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 11),
    _SleOSPFProcAreaLsaCount_Type()
)
sleOSPFProcAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaLsaCount.setStatus("current")
_SleOSPFProcAreaLsaCheckSum_Type = Integer32
_SleOSPFProcAreaLsaCheckSum_Object = MibTableColumn
sleOSPFProcAreaLsaCheckSum = _SleOSPFProcAreaLsaCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 12),
    _SleOSPFProcAreaLsaCheckSum_Type()
)
sleOSPFProcAreaLsaCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaLsaCheckSum.setStatus("current")


class _SleOSPFProcAreaSummary_Type(Integer32):
    """Custom type sleOSPFProcAreaSummary based on Integer32"""
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
          ("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_SleOSPFProcAreaSummary_Type.__name__ = "Integer32"
_SleOSPFProcAreaSummary_Object = MibTableColumn
sleOSPFProcAreaSummary = _SleOSPFProcAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 13),
    _SleOSPFProcAreaSummary_Type()
)
sleOSPFProcAreaSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaSummary.setStatus("current")


class _SleOSPFProcAreaNssaTransRole_Type(Integer32):
    """Custom type sleOSPFProcAreaNssaTransRole based on Integer32"""
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
        *(("never", 0),
          ("always", 1),
          ("candidate", 2),
          ("none", 3))
    )


_SleOSPFProcAreaNssaTransRole_Type.__name__ = "Integer32"
_SleOSPFProcAreaNssaTransRole_Object = MibTableColumn
sleOSPFProcAreaNssaTransRole = _SleOSPFProcAreaNssaTransRole_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 14),
    _SleOSPFProcAreaNssaTransRole_Type()
)
sleOSPFProcAreaNssaTransRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaNssaTransRole.setStatus("current")


class _SleOSPFProcAreaNssaNoRedist_Type(Integer32):
    """Custom type sleOSPFProcAreaNssaNoRedist based on Integer32"""
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
          ("enable", 1),
          ("disable", 2))
    )


_SleOSPFProcAreaNssaNoRedist_Type.__name__ = "Integer32"
_SleOSPFProcAreaNssaNoRedist_Object = MibTableColumn
sleOSPFProcAreaNssaNoRedist = _SleOSPFProcAreaNssaNoRedist_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 15),
    _SleOSPFProcAreaNssaNoRedist_Type()
)
sleOSPFProcAreaNssaNoRedist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaNssaNoRedist.setStatus("current")


class _SleOSPFProcAreaNssaDefOriginate_Type(Integer32):
    """Custom type sleOSPFProcAreaNssaDefOriginate based on Integer32"""
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


_SleOSPFProcAreaNssaDefOriginate_Type.__name__ = "Integer32"
_SleOSPFProcAreaNssaDefOriginate_Object = MibTableColumn
sleOSPFProcAreaNssaDefOriginate = _SleOSPFProcAreaNssaDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 16),
    _SleOSPFProcAreaNssaDefOriginate_Type()
)
sleOSPFProcAreaNssaDefOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaNssaDefOriginate.setStatus("current")


class _SleOSPFProcAreaNssaDefMetricType_Type(Integer32):
    """Custom type sleOSPFProcAreaNssaDefMetricType based on Integer32"""
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


_SleOSPFProcAreaNssaDefMetricType_Type.__name__ = "Integer32"
_SleOSPFProcAreaNssaDefMetricType_Object = MibTableColumn
sleOSPFProcAreaNssaDefMetricType = _SleOSPFProcAreaNssaDefMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 17),
    _SleOSPFProcAreaNssaDefMetricType_Type()
)
sleOSPFProcAreaNssaDefMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaNssaDefMetricType.setStatus("current")


class _SleOSPFProcAreaNssaDefMetric_Type(Integer32):
    """Custom type sleOSPFProcAreaNssaDefMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_SleOSPFProcAreaNssaDefMetric_Type.__name__ = "Integer32"
_SleOSPFProcAreaNssaDefMetric_Object = MibTableColumn
sleOSPFProcAreaNssaDefMetric = _SleOSPFProcAreaNssaDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 1, 1, 18),
    _SleOSPFProcAreaNssaDefMetric_Type()
)
sleOSPFProcAreaNssaDefMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaNssaDefMetric.setStatus("current")
_SleOSPFProcAreaInfoControl_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaInfoControl = _SleOSPFProcAreaInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2)
)


class _SleOSPFProcAreaControlRequest_Type(Integer32):
    """Custom type sleOSPFProcAreaControlRequest based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFGeneralArea", 1),
          ("createOSPFStubNssaArea", 2),
          ("deleteOSPFArea", 3),
          ("setOSPFAreaDefaultCostChange", 4),
          ("setOSPFAreaAuthenTypeChange", 5),
          ("setOSPFAreaFAInNameChange", 6),
          ("setOSPFAreaFAOutNameChang", 7),
          ("setOSPFAreaFPInNameChange", 8),
          ("setOSPFAreaFPOutNameChange", 9),
          ("setOSPFAreaShortcutTypeChange", 10),
          ("setOSPFAreaSummary", 11),
          ("setOSPFNssaAreaTranslateRole", 12),
          ("setOSPFNssaAreaNoRedist", 13),
          ("setOSPFNssaAreaDefaultProfile", 14))
    )


_SleOSPFProcAreaControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlRequest_Object = MibScalar
sleOSPFProcAreaControlRequest = _SleOSPFProcAreaControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 1),
    _SleOSPFProcAreaControlRequest_Type()
)
sleOSPFProcAreaControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlRequest.setStatus("current")
_SleOSPFProcAreaControlStatus_Type = SleControlStatusType
_SleOSPFProcAreaControlStatus_Object = MibScalar
sleOSPFProcAreaControlStatus = _SleOSPFProcAreaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 2),
    _SleOSPFProcAreaControlStatus_Type()
)
sleOSPFProcAreaControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlStatus.setStatus("current")
_SleOSPFProcAreaControlTimer_Type = Gauge32
_SleOSPFProcAreaControlTimer_Object = MibScalar
sleOSPFProcAreaControlTimer = _SleOSPFProcAreaControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 3),
    _SleOSPFProcAreaControlTimer_Type()
)
sleOSPFProcAreaControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlTimer.setStatus("current")
_SleOSPFProcAreaControlTimeStamp_Type = TimeTicks
_SleOSPFProcAreaControlTimeStamp_Object = MibScalar
sleOSPFProcAreaControlTimeStamp = _SleOSPFProcAreaControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 4),
    _SleOSPFProcAreaControlTimeStamp_Type()
)
sleOSPFProcAreaControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlTimeStamp.setStatus("current")
_SleOSPFProcAreaControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcAreaControlReqResult_Object = MibScalar
sleOSPFProcAreaControlReqResult = _SleOSPFProcAreaControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 5),
    _SleOSPFProcAreaControlReqResult_Type()
)
sleOSPFProcAreaControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlReqResult.setStatus("current")


class _SleOSPFProcAreaControlProcID_Type(Integer32):
    """Custom type sleOSPFProcAreaControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlProcID_Object = MibScalar
sleOSPFProcAreaControlProcID = _SleOSPFProcAreaControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 6),
    _SleOSPFProcAreaControlProcID_Type()
)
sleOSPFProcAreaControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlProcID.setStatus("current")
_SleOSPFProcAreaControlID_Type = IpAddress
_SleOSPFProcAreaControlID_Object = MibScalar
sleOSPFProcAreaControlID = _SleOSPFProcAreaControlID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 7),
    _SleOSPFProcAreaControlID_Type()
)
sleOSPFProcAreaControlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlID.setStatus("current")


class _SleOSPFProcAreaControlType_Type(Integer32):
    """Custom type sleOSPFProcAreaControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("stub", 1),
          ("nssa", 2))
    )


_SleOSPFProcAreaControlType_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlType_Object = MibScalar
sleOSPFProcAreaControlType = _SleOSPFProcAreaControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 8),
    _SleOSPFProcAreaControlType_Type()
)
sleOSPFProcAreaControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlType.setStatus("current")


class _SleOSPFProcAreaControlDefaultCost_Type(Integer32):
    """Custom type sleOSPFProcAreaControlDefaultCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SleOSPFProcAreaControlDefaultCost_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlDefaultCost_Object = MibScalar
sleOSPFProcAreaControlDefaultCost = _SleOSPFProcAreaControlDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 9),
    _SleOSPFProcAreaControlDefaultCost_Type()
)
sleOSPFProcAreaControlDefaultCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlDefaultCost.setStatus("current")


class _SleOSPFProcAreaControlAuthenType_Type(Integer32):
    """Custom type sleOSPFProcAreaControlAuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("simple", 1),
          ("crypt", 2))
    )


_SleOSPFProcAreaControlAuthenType_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlAuthenType_Object = MibScalar
sleOSPFProcAreaControlAuthenType = _SleOSPFProcAreaControlAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 10),
    _SleOSPFProcAreaControlAuthenType_Type()
)
sleOSPFProcAreaControlAuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlAuthenType.setStatus("current")
_SleOSPFProcAreaControlFAInName_Type = OctetString
_SleOSPFProcAreaControlFAInName_Object = MibScalar
sleOSPFProcAreaControlFAInName = _SleOSPFProcAreaControlFAInName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 11),
    _SleOSPFProcAreaControlFAInName_Type()
)
sleOSPFProcAreaControlFAInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlFAInName.setStatus("current")
_SleOSPFProcAreaControlFAOutName_Type = OctetString
_SleOSPFProcAreaControlFAOutName_Object = MibScalar
sleOSPFProcAreaControlFAOutName = _SleOSPFProcAreaControlFAOutName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 12),
    _SleOSPFProcAreaControlFAOutName_Type()
)
sleOSPFProcAreaControlFAOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlFAOutName.setStatus("current")
_SleOSPFProcAreaControlFPInName_Type = OctetString
_SleOSPFProcAreaControlFPInName_Object = MibScalar
sleOSPFProcAreaControlFPInName = _SleOSPFProcAreaControlFPInName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 13),
    _SleOSPFProcAreaControlFPInName_Type()
)
sleOSPFProcAreaControlFPInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlFPInName.setStatus("current")
_SleOSPFProcAreaControlFPOutName_Type = OctetString
_SleOSPFProcAreaControlFPOutName_Object = MibScalar
sleOSPFProcAreaControlFPOutName = _SleOSPFProcAreaControlFPOutName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 14),
    _SleOSPFProcAreaControlFPOutName_Type()
)
sleOSPFProcAreaControlFPOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlFPOutName.setStatus("current")


class _SleOSPFProcAreaControlShortcutType_Type(Integer32):
    """Custom type sleOSPFProcAreaControlShortcutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enable", 1),
          ("disable", 2))
    )


_SleOSPFProcAreaControlShortcutType_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlShortcutType_Object = MibScalar
sleOSPFProcAreaControlShortcutType = _SleOSPFProcAreaControlShortcutType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 15),
    _SleOSPFProcAreaControlShortcutType_Type()
)
sleOSPFProcAreaControlShortcutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlShortcutType.setStatus("current")


class _SleOSPFProcAreaControlSummary_Type(Integer32):
    """Custom type sleOSPFProcAreaControlSummary based on Integer32"""
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


_SleOSPFProcAreaControlSummary_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlSummary_Object = MibScalar
sleOSPFProcAreaControlSummary = _SleOSPFProcAreaControlSummary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 16),
    _SleOSPFProcAreaControlSummary_Type()
)
sleOSPFProcAreaControlSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlSummary.setStatus("current")


class _SleOSPFProcAreaControlNssaTransRole_Type(Integer32):
    """Custom type sleOSPFProcAreaControlNssaTransRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("never", 0),
          ("always", 1),
          ("candidate", 2))
    )


_SleOSPFProcAreaControlNssaTransRole_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlNssaTransRole_Object = MibScalar
sleOSPFProcAreaControlNssaTransRole = _SleOSPFProcAreaControlNssaTransRole_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 17),
    _SleOSPFProcAreaControlNssaTransRole_Type()
)
sleOSPFProcAreaControlNssaTransRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlNssaTransRole.setStatus("current")


class _SleOSPFProcAreaControlNssaNoRedist_Type(Integer32):
    """Custom type sleOSPFProcAreaControlNssaNoRedist based on Integer32"""
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


_SleOSPFProcAreaControlNssaNoRedist_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlNssaNoRedist_Object = MibScalar
sleOSPFProcAreaControlNssaNoRedist = _SleOSPFProcAreaControlNssaNoRedist_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 18),
    _SleOSPFProcAreaControlNssaNoRedist_Type()
)
sleOSPFProcAreaControlNssaNoRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlNssaNoRedist.setStatus("current")


class _SleOSPFProcAreaControlNssaDefOriginate_Type(Integer32):
    """Custom type sleOSPFProcAreaControlNssaDefOriginate based on Integer32"""
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


_SleOSPFProcAreaControlNssaDefOriginate_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlNssaDefOriginate_Object = MibScalar
sleOSPFProcAreaControlNssaDefOriginate = _SleOSPFProcAreaControlNssaDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 19),
    _SleOSPFProcAreaControlNssaDefOriginate_Type()
)
sleOSPFProcAreaControlNssaDefOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlNssaDefOriginate.setStatus("current")


class _SleOSPFProcAreaControlNssaDefMetricType_Type(Integer32):
    """Custom type sleOSPFProcAreaControlNssaDefMetricType based on Integer32"""
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


_SleOSPFProcAreaControlNssaDefMetricType_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlNssaDefMetricType_Object = MibScalar
sleOSPFProcAreaControlNssaDefMetricType = _SleOSPFProcAreaControlNssaDefMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 20),
    _SleOSPFProcAreaControlNssaDefMetricType_Type()
)
sleOSPFProcAreaControlNssaDefMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlNssaDefMetricType.setStatus("current")


class _SleOSPFProcAreaControlNssaDefMetric_Type(Integer32):
    """Custom type sleOSPFProcAreaControlNssaDefMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_SleOSPFProcAreaControlNssaDefMetric_Type.__name__ = "Integer32"
_SleOSPFProcAreaControlNssaDefMetric_Object = MibScalar
sleOSPFProcAreaControlNssaDefMetric = _SleOSPFProcAreaControlNssaDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 2, 21),
    _SleOSPFProcAreaControlNssaDefMetric_Type()
)
sleOSPFProcAreaControlNssaDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaControlNssaDefMetric.setStatus("current")
_SleOSPFProcAreaInfoNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaInfoNotification = _SleOSPFProcAreaInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3)
)
_SleOSPFProcAreaRange_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaRange = _SleOSPFProcAreaRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2)
)
_SleOSPFProcAreaRangeTable_Object = MibTable
sleOSPFProcAreaRangeTable = _SleOSPFProcAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeTable.setStatus("current")
_SleOSPFProcAreaRangeEntry_Object = MibTableRow
sleOSPFProcAreaRangeEntry = _SleOSPFProcAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 1, 1)
)
sleOSPFProcAreaRangeEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaRangeIP"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaRangeIPMask"),
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeEntry.setStatus("current")
_SleOSPFProcAreaRangeIP_Type = IpAddress
_SleOSPFProcAreaRangeIP_Object = MibTableColumn
sleOSPFProcAreaRangeIP = _SleOSPFProcAreaRangeIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 1, 1, 1),
    _SleOSPFProcAreaRangeIP_Type()
)
sleOSPFProcAreaRangeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeIP.setStatus("current")


class _SleOSPFProcAreaRangeIPMask_Type(Integer32):
    """Custom type sleOSPFProcAreaRangeIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleOSPFProcAreaRangeIPMask_Type.__name__ = "Integer32"
_SleOSPFProcAreaRangeIPMask_Object = MibTableColumn
sleOSPFProcAreaRangeIPMask = _SleOSPFProcAreaRangeIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 1, 1, 2),
    _SleOSPFProcAreaRangeIPMask_Type()
)
sleOSPFProcAreaRangeIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeIPMask.setStatus("current")


class _SleOSPFProcAreaRangeAdverType_Type(Integer32):
    """Custom type sleOSPFProcAreaRangeAdverType based on Integer32"""
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


_SleOSPFProcAreaRangeAdverType_Type.__name__ = "Integer32"
_SleOSPFProcAreaRangeAdverType_Object = MibTableColumn
sleOSPFProcAreaRangeAdverType = _SleOSPFProcAreaRangeAdverType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 1, 1, 3),
    _SleOSPFProcAreaRangeAdverType_Type()
)
sleOSPFProcAreaRangeAdverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeAdverType.setStatus("current")
_SleOSPFProcAreaRangeControl_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaRangeControl = _SleOSPFProcAreaRangeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2)
)


class _SleOSPFProcAreaRangeControlRequest_Type(Integer32):
    """Custom type sleOSPFProcAreaRangeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFAreaRange", 1),
          ("deleteOSPFAreaRange", 2),
          ("setOSPFAreaRange", 3))
    )


_SleOSPFProcAreaRangeControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcAreaRangeControlRequest_Object = MibScalar
sleOSPFProcAreaRangeControlRequest = _SleOSPFProcAreaRangeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 1),
    _SleOSPFProcAreaRangeControlRequest_Type()
)
sleOSPFProcAreaRangeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlRequest.setStatus("current")
_SleOSPFProcAreaRangeControlStatus_Type = SleControlStatusType
_SleOSPFProcAreaRangeControlStatus_Object = MibScalar
sleOSPFProcAreaRangeControlStatus = _SleOSPFProcAreaRangeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 2),
    _SleOSPFProcAreaRangeControlStatus_Type()
)
sleOSPFProcAreaRangeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlStatus.setStatus("current")
_SleOSPFProcAreaRangeControlTimer_Type = Gauge32
_SleOSPFProcAreaRangeControlTimer_Object = MibScalar
sleOSPFProcAreaRangeControlTimer = _SleOSPFProcAreaRangeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 3),
    _SleOSPFProcAreaRangeControlTimer_Type()
)
sleOSPFProcAreaRangeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlTimer.setStatus("current")
_SleOSPFProcAreaRangeControlTimeStamp_Type = TimeTicks
_SleOSPFProcAreaRangeControlTimeStamp_Object = MibScalar
sleOSPFProcAreaRangeControlTimeStamp = _SleOSPFProcAreaRangeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 4),
    _SleOSPFProcAreaRangeControlTimeStamp_Type()
)
sleOSPFProcAreaRangeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlTimeStamp.setStatus("current")
_SleOSPFProcAreaRangeControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcAreaRangeControlReqResult_Object = MibScalar
sleOSPFProcAreaRangeControlReqResult = _SleOSPFProcAreaRangeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 5),
    _SleOSPFProcAreaRangeControlReqResult_Type()
)
sleOSPFProcAreaRangeControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlReqResult.setStatus("current")


class _SleOSPFProcAreaRangeControlProcID_Type(Integer32):
    """Custom type sleOSPFProcAreaRangeControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaRangeControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcAreaRangeControlProcID_Object = MibScalar
sleOSPFProcAreaRangeControlProcID = _SleOSPFProcAreaRangeControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 6),
    _SleOSPFProcAreaRangeControlProcID_Type()
)
sleOSPFProcAreaRangeControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlProcID.setStatus("current")
_SleOSPFProcAreaRangeControlID_Type = IpAddress
_SleOSPFProcAreaRangeControlID_Object = MibScalar
sleOSPFProcAreaRangeControlID = _SleOSPFProcAreaRangeControlID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 7),
    _SleOSPFProcAreaRangeControlID_Type()
)
sleOSPFProcAreaRangeControlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlID.setStatus("current")
_SleOSPFProcAreaRangeControlIP_Type = IpAddress
_SleOSPFProcAreaRangeControlIP_Object = MibScalar
sleOSPFProcAreaRangeControlIP = _SleOSPFProcAreaRangeControlIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 8),
    _SleOSPFProcAreaRangeControlIP_Type()
)
sleOSPFProcAreaRangeControlIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlIP.setStatus("current")


class _SleOSPFProcAreaRangeControlIPMask_Type(Integer32):
    """Custom type sleOSPFProcAreaRangeControlIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleOSPFProcAreaRangeControlIPMask_Type.__name__ = "Integer32"
_SleOSPFProcAreaRangeControlIPMask_Object = MibScalar
sleOSPFProcAreaRangeControlIPMask = _SleOSPFProcAreaRangeControlIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 9),
    _SleOSPFProcAreaRangeControlIPMask_Type()
)
sleOSPFProcAreaRangeControlIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlIPMask.setStatus("current")


class _SleOSPFProcAreaRangeControlAdverType_Type(Integer32):
    """Custom type sleOSPFProcAreaRangeControlAdverType based on Integer32"""
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


_SleOSPFProcAreaRangeControlAdverType_Type.__name__ = "Integer32"
_SleOSPFProcAreaRangeControlAdverType_Object = MibScalar
sleOSPFProcAreaRangeControlAdverType = _SleOSPFProcAreaRangeControlAdverType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 2, 10),
    _SleOSPFProcAreaRangeControlAdverType_Type()
)
sleOSPFProcAreaRangeControlAdverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaRangeControlAdverType.setStatus("current")
_SleOSPFProcAreaRangeNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaRangeNotification = _SleOSPFProcAreaRangeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 3)
)
_SleOSPFProcAreaVlink_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaVlink = _SleOSPFProcAreaVlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3)
)
_SleOSPFProcAreaVlinkInfo_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaVlinkInfo = _SleOSPFProcAreaVlinkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1)
)
_SleOSPFProcAreaVlinkInfoTable_Object = MibTable
sleOSPFProcAreaVlinkInfoTable = _SleOSPFProcAreaVlinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkInfoTable.setStatus("current")
_SleOSPFProcAreaVlinkInfoEntry_Object = MibTableRow
sleOSPFProcAreaVlinkInfoEntry = _SleOSPFProcAreaVlinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1)
)
sleOSPFProcAreaVlinkInfoEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaVlinkIP"),
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkInfoEntry.setStatus("current")
_SleOSPFProcAreaVlinkIP_Type = IpAddress
_SleOSPFProcAreaVlinkIP_Object = MibTableColumn
sleOSPFProcAreaVlinkIP = _SleOSPFProcAreaVlinkIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1, 1),
    _SleOSPFProcAreaVlinkIP_Type()
)
sleOSPFProcAreaVlinkIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkIP.setStatus("current")


class _SleOSPFProcAreaVlinkAuthenType_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkAuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("simple", 1),
          ("crypto", 2))
    )


_SleOSPFProcAreaVlinkAuthenType_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkAuthenType_Object = MibTableColumn
sleOSPFProcAreaVlinkAuthenType = _SleOSPFProcAreaVlinkAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1, 2),
    _SleOSPFProcAreaVlinkAuthenType_Type()
)
sleOSPFProcAreaVlinkAuthenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkAuthenType.setStatus("current")
_SleOSPFProcAreaVlinkAuthenKey_Type = OctetString
_SleOSPFProcAreaVlinkAuthenKey_Object = MibTableColumn
sleOSPFProcAreaVlinkAuthenKey = _SleOSPFProcAreaVlinkAuthenKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1, 3),
    _SleOSPFProcAreaVlinkAuthenKey_Type()
)
sleOSPFProcAreaVlinkAuthenKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkAuthenKey.setStatus("current")


class _SleOSPFProcAreaVlinkDeadInterval_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkDeadInterval_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkDeadInterval_Object = MibTableColumn
sleOSPFProcAreaVlinkDeadInterval = _SleOSPFProcAreaVlinkDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1, 4),
    _SleOSPFProcAreaVlinkDeadInterval_Type()
)
sleOSPFProcAreaVlinkDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkDeadInterval.setStatus("current")


class _SleOSPFProcAreaVlinkHelloInterval_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkHelloInterval_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkHelloInterval_Object = MibTableColumn
sleOSPFProcAreaVlinkHelloInterval = _SleOSPFProcAreaVlinkHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1, 5),
    _SleOSPFProcAreaVlinkHelloInterval_Type()
)
sleOSPFProcAreaVlinkHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkHelloInterval.setStatus("current")


class _SleOSPFProcAreaVlinkRetranInterval_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkRetranInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkRetranInterval_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkRetranInterval_Object = MibTableColumn
sleOSPFProcAreaVlinkRetranInterval = _SleOSPFProcAreaVlinkRetranInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1, 6),
    _SleOSPFProcAreaVlinkRetranInterval_Type()
)
sleOSPFProcAreaVlinkRetranInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkRetranInterval.setStatus("current")


class _SleOSPFProcAreaVlinkTransDelay_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkTransDelay_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkTransDelay_Object = MibTableColumn
sleOSPFProcAreaVlinkTransDelay = _SleOSPFProcAreaVlinkTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 1, 1, 7),
    _SleOSPFProcAreaVlinkTransDelay_Type()
)
sleOSPFProcAreaVlinkTransDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkTransDelay.setStatus("current")
_SleOSPFProcAreaVlinkControl_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaVlinkControl = _SleOSPFProcAreaVlinkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2)
)


class _SleOSPFProcAreaVlinkControlRequest_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFAreaVlink", 1),
          ("deleteOSPFAreaVlink", 2),
          ("setOSPFAreaVlink", 3))
    )


_SleOSPFProcAreaVlinkControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkControlRequest_Object = MibScalar
sleOSPFProcAreaVlinkControlRequest = _SleOSPFProcAreaVlinkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 1),
    _SleOSPFProcAreaVlinkControlRequest_Type()
)
sleOSPFProcAreaVlinkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlRequest.setStatus("current")
_SleOSPFProcAreaVlinkControlStatus_Type = SleControlStatusType
_SleOSPFProcAreaVlinkControlStatus_Object = MibScalar
sleOSPFProcAreaVlinkControlStatus = _SleOSPFProcAreaVlinkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 2),
    _SleOSPFProcAreaVlinkControlStatus_Type()
)
sleOSPFProcAreaVlinkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlStatus.setStatus("current")
_SleOSPFProcAreaVlinkControlTimer_Type = Gauge32
_SleOSPFProcAreaVlinkControlTimer_Object = MibScalar
sleOSPFProcAreaVlinkControlTimer = _SleOSPFProcAreaVlinkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 3),
    _SleOSPFProcAreaVlinkControlTimer_Type()
)
sleOSPFProcAreaVlinkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlTimer.setStatus("current")
_SleOSPFProcAreaVlinkControlTimeStamp_Type = TimeTicks
_SleOSPFProcAreaVlinkControlTimeStamp_Object = MibScalar
sleOSPFProcAreaVlinkControlTimeStamp = _SleOSPFProcAreaVlinkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 4),
    _SleOSPFProcAreaVlinkControlTimeStamp_Type()
)
sleOSPFProcAreaVlinkControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlTimeStamp.setStatus("current")
_SleOSPFProcAreaVlinkControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcAreaVlinkControlReqResult_Object = MibScalar
sleOSPFProcAreaVlinkControlReqResult = _SleOSPFProcAreaVlinkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 5),
    _SleOSPFProcAreaVlinkControlReqResult_Type()
)
sleOSPFProcAreaVlinkControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlReqResult.setStatus("current")


class _SleOSPFProcAreaVlinkControlProcID_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkControlProcID_Object = MibScalar
sleOSPFProcAreaVlinkControlProcID = _SleOSPFProcAreaVlinkControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 6),
    _SleOSPFProcAreaVlinkControlProcID_Type()
)
sleOSPFProcAreaVlinkControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlProcID.setStatus("current")
_SleOSPFProcAreaVlinkControlControlID_Type = IpAddress
_SleOSPFProcAreaVlinkControlControlID_Object = MibScalar
sleOSPFProcAreaVlinkControlControlID = _SleOSPFProcAreaVlinkControlControlID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 7),
    _SleOSPFProcAreaVlinkControlControlID_Type()
)
sleOSPFProcAreaVlinkControlControlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlControlID.setStatus("current")
_SleOSPFProcAreaVlinkControlIP_Type = IpAddress
_SleOSPFProcAreaVlinkControlIP_Object = MibScalar
sleOSPFProcAreaVlinkControlIP = _SleOSPFProcAreaVlinkControlIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 8),
    _SleOSPFProcAreaVlinkControlIP_Type()
)
sleOSPFProcAreaVlinkControlIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlIP.setStatus("current")


class _SleOSPFProcAreaVlinkControlAuthenType_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkControlAuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("simple", 1),
          ("crypto", 2))
    )


_SleOSPFProcAreaVlinkControlAuthenType_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkControlAuthenType_Object = MibScalar
sleOSPFProcAreaVlinkControlAuthenType = _SleOSPFProcAreaVlinkControlAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 9),
    _SleOSPFProcAreaVlinkControlAuthenType_Type()
)
sleOSPFProcAreaVlinkControlAuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlAuthenType.setStatus("current")
_SleOSPFProcAreaVlinkControlAuthenKey_Type = OctetString
_SleOSPFProcAreaVlinkControlAuthenKey_Object = MibScalar
sleOSPFProcAreaVlinkControlAuthenKey = _SleOSPFProcAreaVlinkControlAuthenKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 10),
    _SleOSPFProcAreaVlinkControlAuthenKey_Type()
)
sleOSPFProcAreaVlinkControlAuthenKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlAuthenKey.setStatus("current")


class _SleOSPFProcAreaVlinkControlDeadInterval_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkControlDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkControlDeadInterval_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkControlDeadInterval_Object = MibScalar
sleOSPFProcAreaVlinkControlDeadInterval = _SleOSPFProcAreaVlinkControlDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 11),
    _SleOSPFProcAreaVlinkControlDeadInterval_Type()
)
sleOSPFProcAreaVlinkControlDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlDeadInterval.setStatus("current")


class _SleOSPFProcAreaVlinkControlHelloInterval_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkControlHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkControlHelloInterval_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkControlHelloInterval_Object = MibScalar
sleOSPFProcAreaVlinkControlHelloInterval = _SleOSPFProcAreaVlinkControlHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 12),
    _SleOSPFProcAreaVlinkControlHelloInterval_Type()
)
sleOSPFProcAreaVlinkControlHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlHelloInterval.setStatus("current")


class _SleOSPFProcAreaVlinkControlRetranInterval_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkControlRetranInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkControlRetranInterval_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkControlRetranInterval_Object = MibScalar
sleOSPFProcAreaVlinkControlRetranInterval = _SleOSPFProcAreaVlinkControlRetranInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 13),
    _SleOSPFProcAreaVlinkControlRetranInterval_Type()
)
sleOSPFProcAreaVlinkControlRetranInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlRetranInterval.setStatus("current")


class _SleOSPFProcAreaVlinkControlTransInterval_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkControlTransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkControlTransInterval_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkControlTransInterval_Object = MibScalar
sleOSPFProcAreaVlinkControlTransInterval = _SleOSPFProcAreaVlinkControlTransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 2, 14),
    _SleOSPFProcAreaVlinkControlTransInterval_Type()
)
sleOSPFProcAreaVlinkControlTransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkControlTransInterval.setStatus("current")
_SleOSPFProcAreaVlinkNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaVlinkNotification = _SleOSPFProcAreaVlinkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 3)
)
_SleOSPFProcAreaVlinkMsgKey_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaVlinkMsgKey = _SleOSPFProcAreaVlinkMsgKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2)
)
_SleOSPFProcAreaVlinkMsgKeyTable_Object = MibTable
sleOSPFProcAreaVlinkMsgKeyTable = _SleOSPFProcAreaVlinkMsgKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyTable.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyEntry_Object = MibTableRow
sleOSPFProcAreaVlinkMsgKeyEntry = _SleOSPFProcAreaVlinkMsgKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 1, 1)
)
sleOSPFProcAreaVlinkMsgKeyEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaID"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaVlinkIP"),
    (0, "SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyID"),
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyEntry.setStatus("current")


class _SleOSPFProcAreaVlinkMsgKeyID_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkMsgKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcAreaVlinkMsgKeyID_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkMsgKeyID_Object = MibTableColumn
sleOSPFProcAreaVlinkMsgKeyID = _SleOSPFProcAreaVlinkMsgKeyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 1, 1, 1),
    _SleOSPFProcAreaVlinkMsgKeyID_Type()
)
sleOSPFProcAreaVlinkMsgKeyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyID.setStatus("current")


class _SleOSPFProcAreaVlinkMsgKeyVal_Type(OctetString):
    """Custom type sleOSPFProcAreaVlinkMsgKeyVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SleOSPFProcAreaVlinkMsgKeyVal_Type.__name__ = "OctetString"
_SleOSPFProcAreaVlinkMsgKeyVal_Object = MibTableColumn
sleOSPFProcAreaVlinkMsgKeyVal = _SleOSPFProcAreaVlinkMsgKeyVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 1, 1, 2),
    _SleOSPFProcAreaVlinkMsgKeyVal_Type()
)
sleOSPFProcAreaVlinkMsgKeyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyVal.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyControl_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaVlinkMsgKeyControl = _SleOSPFProcAreaVlinkMsgKeyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2)
)


class _SleOSPFProcAreaVlinkMsgKeyControlRequest_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkMsgKeyControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createOSPFAreaVlinkMsgKey", 1),
          ("deleteOSPFAreaVlinkMsgKey", 2))
    )


_SleOSPFProcAreaVlinkMsgKeyControlRequest_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkMsgKeyControlRequest_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlRequest = _SleOSPFProcAreaVlinkMsgKeyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 1),
    _SleOSPFProcAreaVlinkMsgKeyControlRequest_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlRequest.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyControlControlStatus_Type = SleControlStatusType
_SleOSPFProcAreaVlinkMsgKeyControlControlStatus_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlControlStatus = _SleOSPFProcAreaVlinkMsgKeyControlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 2),
    _SleOSPFProcAreaVlinkMsgKeyControlControlStatus_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlControlStatus.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyControlControlTimer_Type = Gauge32
_SleOSPFProcAreaVlinkMsgKeyControlControlTimer_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlControlTimer = _SleOSPFProcAreaVlinkMsgKeyControlControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 3),
    _SleOSPFProcAreaVlinkMsgKeyControlControlTimer_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlControlTimer.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyControlTimeStamp_Type = TimeTicks
_SleOSPFProcAreaVlinkMsgKeyControlTimeStamp_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlTimeStamp = _SleOSPFProcAreaVlinkMsgKeyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 4),
    _SleOSPFProcAreaVlinkMsgKeyControlTimeStamp_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlTimeStamp.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyControlReqResult_Type = SleControlRequestResultType
_SleOSPFProcAreaVlinkMsgKeyControlReqResult_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlReqResult = _SleOSPFProcAreaVlinkMsgKeyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 5),
    _SleOSPFProcAreaVlinkMsgKeyControlReqResult_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlReqResult.setStatus("current")


class _SleOSPFProcAreaVlinkMsgKeyControlProcID_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkMsgKeyControlProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFProcAreaVlinkMsgKeyControlProcID_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkMsgKeyControlProcID_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlProcID = _SleOSPFProcAreaVlinkMsgKeyControlProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 6),
    _SleOSPFProcAreaVlinkMsgKeyControlProcID_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlProcID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlProcID.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyControlID_Type = IpAddress
_SleOSPFProcAreaVlinkMsgKeyControlID_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlID = _SleOSPFProcAreaVlinkMsgKeyControlID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 7),
    _SleOSPFProcAreaVlinkMsgKeyControlID_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlID.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyControlIP_Type = IpAddress
_SleOSPFProcAreaVlinkMsgKeyControlIP_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlIP = _SleOSPFProcAreaVlinkMsgKeyControlIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 8),
    _SleOSPFProcAreaVlinkMsgKeyControlIP_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlIP.setStatus("current")


class _SleOSPFProcAreaVlinkMsgKeyControlKeyID_Type(Integer32):
    """Custom type sleOSPFProcAreaVlinkMsgKeyControlKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFProcAreaVlinkMsgKeyControlKeyID_Type.__name__ = "Integer32"
_SleOSPFProcAreaVlinkMsgKeyControlKeyID_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlKeyID = _SleOSPFProcAreaVlinkMsgKeyControlKeyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 9),
    _SleOSPFProcAreaVlinkMsgKeyControlKeyID_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlKeyID.setStatus("current")


class _SleOSPFProcAreaVlinkMsgKeyControlKeyVal_Type(OctetString):
    """Custom type sleOSPFProcAreaVlinkMsgKeyControlKeyVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SleOSPFProcAreaVlinkMsgKeyControlKeyVal_Type.__name__ = "OctetString"
_SleOSPFProcAreaVlinkMsgKeyControlKeyVal_Object = MibScalar
sleOSPFProcAreaVlinkMsgKeyControlKeyVal = _SleOSPFProcAreaVlinkMsgKeyControlKeyVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 2, 10),
    _SleOSPFProcAreaVlinkMsgKeyControlKeyVal_Type()
)
sleOSPFProcAreaVlinkMsgKeyControlKeyVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFProcAreaVlinkMsgKeyControlKeyVal.setStatus("current")
_SleOSPFProcAreaVlinkMsgKeyNotification_ObjectIdentity = ObjectIdentity
sleOSPFProcAreaVlinkMsgKeyNotification = _SleOSPFProcAreaVlinkMsgKeyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 3)
)
_SleOSPFInterface_ObjectIdentity = ObjectIdentity
sleOSPFInterface = _SleOSPFInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3)
)
_SleOSPFIf_ObjectIdentity = ObjectIdentity
sleOSPFIf = _SleOSPFIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1)
)
_SleOSPFIfTable_Object = MibTable
sleOSPFIfTable = _SleOSPFIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleOSPFIfTable.setStatus("current")
_SleOSPFIfEntry_Object = MibTableRow
sleOSPFIfEntry = _SleOSPFIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1, 1)
)
sleOSPFIfEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFIfIndex"),
)
if mibBuilder.loadTexts:
    sleOSPFIfEntry.setStatus("current")


class _SleOSPFIfIndex_Type(Integer32):
    """Custom type sleOSPFIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4097),
    )


_SleOSPFIfIndex_Type.__name__ = "Integer32"
_SleOSPFIfIndex_Object = MibTableColumn
sleOSPFIfIndex = _SleOSPFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1, 1, 1),
    _SleOSPFIfIndex_Type()
)
sleOSPFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfIndex.setStatus("current")


class _SleOSFPIfEnabled_Type(Integer32):
    """Custom type sleOSFPIfEnabled based on Integer32"""
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


_SleOSFPIfEnabled_Type.__name__ = "Integer32"
_SleOSFPIfEnabled_Object = MibTableColumn
sleOSFPIfEnabled = _SleOSFPIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1, 1, 2),
    _SleOSFPIfEnabled_Type()
)
sleOSFPIfEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSFPIfEnabled.setStatus("current")


class _SleOSPFIfNetworkType_Type(Integer32):
    """Custom type sleOSPFIfNetworkType based on Integer32"""
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
          ("virtuallink", 6),
          ("loopback", 7))
    )


_SleOSPFIfNetworkType_Type.__name__ = "Integer32"
_SleOSPFIfNetworkType_Object = MibTableColumn
sleOSPFIfNetworkType = _SleOSPFIfNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1, 1, 3),
    _SleOSPFIfNetworkType_Type()
)
sleOSPFIfNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfNetworkType.setStatus("current")


class _SleOSFPIfMTU_Type(Integer32):
    """Custom type sleOSFPIfMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 65535),
    )


_SleOSFPIfMTU_Type.__name__ = "Integer32"
_SleOSFPIfMTU_Object = MibTableColumn
sleOSFPIfMTU = _SleOSFPIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1, 1, 4),
    _SleOSFPIfMTU_Type()
)
sleOSFPIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSFPIfMTU.setStatus("current")


class _SleOSFPIfBFD_Type(Integer32):
    """Custom type sleOSFPIfBFD based on Integer32"""
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
          ("enable", 1),
          ("none", 2))
    )


_SleOSFPIfBFD_Type.__name__ = "Integer32"
_SleOSFPIfBFD_Object = MibTableColumn
sleOSFPIfBFD = _SleOSFPIfBFD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1, 1, 5),
    _SleOSFPIfBFD_Type()
)
sleOSFPIfBFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSFPIfBFD.setStatus("current")


class _SleOSFPIfEFM_Type(Integer32):
    """Custom type sleOSFPIfEFM based on Integer32"""
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
          ("enable", 1),
          ("none", 2))
    )


_SleOSFPIfEFM_Type.__name__ = "Integer32"
_SleOSFPIfEFM_Object = MibTableColumn
sleOSFPIfEFM = _SleOSFPIfEFM_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 1, 1, 6),
    _SleOSFPIfEFM_Type()
)
sleOSFPIfEFM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSFPIfEFM.setStatus("current")
_SleOSPFIfControl_ObjectIdentity = ObjectIdentity
sleOSPFIfControl = _SleOSPFIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2)
)


class _SleOSPFIfControlRequest_Type(Integer32):
    """Custom type sleOSPFIfControlRequest based on Integer32"""
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
        *(("setOSPFIFEnabled", 1),
          ("setOSPFIFNetworkType", 2),
          ("setOSPFIFMTU", 3),
          ("setOSPFIFBFD", 4),
          ("setOSPFIFEFM", 5))
    )


_SleOSPFIfControlRequest_Type.__name__ = "Integer32"
_SleOSPFIfControlRequest_Object = MibScalar
sleOSPFIfControlRequest = _SleOSPFIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 1),
    _SleOSPFIfControlRequest_Type()
)
sleOSPFIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlRequest.setStatus("current")
_SleOSPFIfControlStatus_Type = SleControlStatusType
_SleOSPFIfControlStatus_Object = MibScalar
sleOSPFIfControlStatus = _SleOSPFIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 2),
    _SleOSPFIfControlStatus_Type()
)
sleOSPFIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfControlStatus.setStatus("current")
_SleOSPFIfControlTimer_Type = Gauge32
_SleOSPFIfControlTimer_Object = MibScalar
sleOSPFIfControlTimer = _SleOSPFIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 3),
    _SleOSPFIfControlTimer_Type()
)
sleOSPFIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlTimer.setStatus("current")
_SleOSPFIfControlTimeStamp_Type = TimeTicks
_SleOSPFIfControlTimeStamp_Object = MibScalar
sleOSPFIfControlTimeStamp = _SleOSPFIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 4),
    _SleOSPFIfControlTimeStamp_Type()
)
sleOSPFIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfControlTimeStamp.setStatus("current")
_SleOSPFIfControlReqResult_Type = SleControlRequestResultType
_SleOSPFIfControlReqResult_Object = MibScalar
sleOSPFIfControlReqResult = _SleOSPFIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 5),
    _SleOSPFIfControlReqResult_Type()
)
sleOSPFIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfControlReqResult.setStatus("current")


class _SleOSPFIfControlIndex_Type(Integer32):
    """Custom type sleOSPFIfControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfControlIndex_Type.__name__ = "Integer32"
_SleOSPFIfControlIndex_Object = MibScalar
sleOSPFIfControlIndex = _SleOSPFIfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 6),
    _SleOSPFIfControlIndex_Type()
)
sleOSPFIfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlIndex.setStatus("current")


class _SleOSPFIfControlEnabled_Type(Integer32):
    """Custom type sleOSPFIfControlEnabled based on Integer32"""
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


_SleOSPFIfControlEnabled_Type.__name__ = "Integer32"
_SleOSPFIfControlEnabled_Object = MibScalar
sleOSPFIfControlEnabled = _SleOSPFIfControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 7),
    _SleOSPFIfControlEnabled_Type()
)
sleOSPFIfControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlEnabled.setStatus("current")


class _SleOSPFIfControlNetworkType_Type(Integer32):
    """Custom type sleOSPFIfControlNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("p2p", 1),
          ("broadcast", 2),
          ("nbma", 3),
          ("p2mp", 4),
          ("p2mpNbma", 5))
    )


_SleOSPFIfControlNetworkType_Type.__name__ = "Integer32"
_SleOSPFIfControlNetworkType_Object = MibScalar
sleOSPFIfControlNetworkType = _SleOSPFIfControlNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 8),
    _SleOSPFIfControlNetworkType_Type()
)
sleOSPFIfControlNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlNetworkType.setStatus("current")


class _SleOSPFIfControlMTU_Type(Integer32):
    """Custom type sleOSPFIfControlMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 65535),
    )


_SleOSPFIfControlMTU_Type.__name__ = "Integer32"
_SleOSPFIfControlMTU_Object = MibScalar
sleOSPFIfControlMTU = _SleOSPFIfControlMTU_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 9),
    _SleOSPFIfControlMTU_Type()
)
sleOSPFIfControlMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlMTU.setStatus("current")


class _SleOSPFIfControlBFD_Type(Integer32):
    """Custom type sleOSPFIfControlBFD based on Integer32"""
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
          ("enable", 1),
          ("none", 2))
    )


_SleOSPFIfControlBFD_Type.__name__ = "Integer32"
_SleOSPFIfControlBFD_Object = MibScalar
sleOSPFIfControlBFD = _SleOSPFIfControlBFD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 10),
    _SleOSPFIfControlBFD_Type()
)
sleOSPFIfControlBFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlBFD.setStatus("current")


class _SleOSPFIfControlEFM_Type(Integer32):
    """Custom type sleOSPFIfControlEFM based on Integer32"""
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
          ("enable", 1),
          ("none", 2))
    )


_SleOSPFIfControlEFM_Type.__name__ = "Integer32"
_SleOSPFIfControlEFM_Object = MibScalar
sleOSPFIfControlEFM = _SleOSPFIfControlEFM_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 2, 11),
    _SleOSPFIfControlEFM_Type()
)
sleOSPFIfControlEFM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfControlEFM.setStatus("current")
_SleOSPFIfBaseNotification_ObjectIdentity = ObjectIdentity
sleOSPFIfBaseNotification = _SleOSPFIfBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 3)
)
_SleOSPFIfInfo_ObjectIdentity = ObjectIdentity
sleOSPFIfInfo = _SleOSPFIfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2)
)
_SleOSPFIfInfoTable_Object = MibTable
sleOSPFIfInfoTable = _SleOSPFIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleOSPFIfInfoTable.setStatus("current")
_SleOSPFIfInfoEntry_Object = MibTableRow
sleOSPFIfInfoEntry = _SleOSPFIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1)
)
sleOSPFIfInfoEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFIfIndex"),
    (0, "SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
)
if mibBuilder.loadTexts:
    sleOSPFIfInfoEntry.setStatus("current")
_SleOSPFIfIpAddr_Type = IpAddress
_SleOSPFIfIpAddr_Object = MibTableColumn
sleOSPFIfIpAddr = _SleOSPFIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 1),
    _SleOSPFIfIpAddr_Type()
)
sleOSPFIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfIpAddr.setStatus("current")


class _SleOSPFIfCost_Type(Integer32):
    """Custom type sleOSPFIfCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfCost_Type.__name__ = "Integer32"
_SleOSPFIfCost_Object = MibTableColumn
sleOSPFIfCost = _SleOSPFIfCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 2),
    _SleOSPFIfCost_Type()
)
sleOSPFIfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfCost.setStatus("current")


class _SleOSPFIfTransmitDelay_Type(Integer32):
    """Custom type sleOSPFIfTransmitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfTransmitDelay_Type.__name__ = "Integer32"
_SleOSPFIfTransmitDelay_Object = MibTableColumn
sleOSPFIfTransmitDelay = _SleOSPFIfTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 3),
    _SleOSPFIfTransmitDelay_Type()
)
sleOSPFIfTransmitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfTransmitDelay.setStatus("current")


class _SleOSPFIfPriority_Type(Integer32):
    """Custom type sleOSPFIfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFIfPriority_Type.__name__ = "Integer32"
_SleOSPFIfPriority_Object = MibTableColumn
sleOSPFIfPriority = _SleOSPFIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 4),
    _SleOSPFIfPriority_Type()
)
sleOSPFIfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfPriority.setStatus("current")


class _SleOSPFIfHelloInterval_Type(Integer32):
    """Custom type sleOSPFIfHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfHelloInterval_Type.__name__ = "Integer32"
_SleOSPFIfHelloInterval_Object = MibTableColumn
sleOSPFIfHelloInterval = _SleOSPFIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 5),
    _SleOSPFIfHelloInterval_Type()
)
sleOSPFIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfHelloInterval.setStatus("current")


class _SleOSPFIfDeadInterval_Type(Integer32):
    """Custom type sleOSPFIfDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfDeadInterval_Type.__name__ = "Integer32"
_SleOSPFIfDeadInterval_Object = MibTableColumn
sleOSPFIfDeadInterval = _SleOSPFIfDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 6),
    _SleOSPFIfDeadInterval_Type()
)
sleOSPFIfDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfDeadInterval.setStatus("current")


class _SleOSPFIfRetransInterval_Type(Integer32):
    """Custom type sleOSPFIfRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfRetransInterval_Type.__name__ = "Integer32"
_SleOSPFIfRetransInterval_Object = MibTableColumn
sleOSPFIfRetransInterval = _SleOSPFIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 7),
    _SleOSPFIfRetransInterval_Type()
)
sleOSPFIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfRetransInterval.setStatus("current")


class _SleOSPFIfAuth_Type(Integer32):
    """Custom type sleOSPFIfAuth based on Integer32"""
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


_SleOSPFIfAuth_Type.__name__ = "Integer32"
_SleOSPFIfAuth_Object = MibTableColumn
sleOSPFIfAuth = _SleOSPFIfAuth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 8),
    _SleOSPFIfAuth_Type()
)
sleOSPFIfAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfAuth.setStatus("current")


class _SleOSPFIfAuthType_Type(Integer32):
    """Custom type sleOSPFIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("simple", 1),
          ("crypt", 2))
    )


_SleOSPFIfAuthType_Type.__name__ = "Integer32"
_SleOSPFIfAuthType_Object = MibTableColumn
sleOSPFIfAuthType = _SleOSPFIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 9),
    _SleOSPFIfAuthType_Type()
)
sleOSPFIfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfAuthType.setStatus("current")


class _SleOSPFIfDataFilterOut_Type(Integer32):
    """Custom type sleOSPFIfDataFilterOut based on Integer32"""
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


_SleOSPFIfDataFilterOut_Type.__name__ = "Integer32"
_SleOSPFIfDataFilterOut_Object = MibTableColumn
sleOSPFIfDataFilterOut = _SleOSPFIfDataFilterOut_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 10),
    _SleOSPFIfDataFilterOut_Type()
)
sleOSPFIfDataFilterOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfDataFilterOut.setStatus("current")


class _SleOSPFIfMTUIgnore_Type(Integer32):
    """Custom type sleOSPFIfMTUIgnore based on Integer32"""
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


_SleOSPFIfMTUIgnore_Type.__name__ = "Integer32"
_SleOSPFIfMTUIgnore_Object = MibTableColumn
sleOSPFIfMTUIgnore = _SleOSPFIfMTUIgnore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 11),
    _SleOSPFIfMTUIgnore_Type()
)
sleOSPFIfMTUIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfMTUIgnore.setStatus("current")


class _SleOSPFIfResync_Type(Integer32):
    """Custom type sleOSPFIfResync based on Integer32"""
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


_SleOSPFIfResync_Type.__name__ = "Integer32"
_SleOSPFIfResync_Object = MibTableColumn
sleOSPFIfResync = _SleOSPFIfResync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 12),
    _SleOSPFIfResync_Type()
)
sleOSPFIfResync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfResync.setStatus("current")


class _SleOSPFIfResyncTimeout_Type(Integer32):
    """Custom type sleOSPFIfResyncTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfResyncTimeout_Type.__name__ = "Integer32"
_SleOSPFIfResyncTimeout_Object = MibTableColumn
sleOSPFIfResyncTimeout = _SleOSPFIfResyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 13),
    _SleOSPFIfResyncTimeout_Type()
)
sleOSPFIfResyncTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfResyncTimeout.setStatus("current")
_SleOSPFIfAuthKeyFirst_Type = OctetString
_SleOSPFIfAuthKeyFirst_Object = MibTableColumn
sleOSPFIfAuthKeyFirst = _SleOSPFIfAuthKeyFirst_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 14),
    _SleOSPFIfAuthKeyFirst_Type()
)
sleOSPFIfAuthKeyFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfAuthKeyFirst.setStatus("current")


class _SleOSPFIfAuthKeyFirstAct_Type(Integer32):
    """Custom type sleOSPFIfAuthKeyFirstAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 0),
          ("active", 1))
    )


_SleOSPFIfAuthKeyFirstAct_Type.__name__ = "Integer32"
_SleOSPFIfAuthKeyFirstAct_Object = MibTableColumn
sleOSPFIfAuthKeyFirstAct = _SleOSPFIfAuthKeyFirstAct_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 15),
    _SleOSPFIfAuthKeyFirstAct_Type()
)
sleOSPFIfAuthKeyFirstAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfAuthKeyFirstAct.setStatus("current")
_SleOSPFIfAuthKeySecond_Type = OctetString
_SleOSPFIfAuthKeySecond_Object = MibTableColumn
sleOSPFIfAuthKeySecond = _SleOSPFIfAuthKeySecond_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 16),
    _SleOSPFIfAuthKeySecond_Type()
)
sleOSPFIfAuthKeySecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfAuthKeySecond.setStatus("current")


class _SleOSPFIfAuthKeySecondAct_Type(Integer32):
    """Custom type sleOSPFIfAuthKeySecondAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 0),
          ("active", 1))
    )


_SleOSPFIfAuthKeySecondAct_Type.__name__ = "Integer32"
_SleOSPFIfAuthKeySecondAct_Object = MibTableColumn
sleOSPFIfAuthKeySecondAct = _SleOSPFIfAuthKeySecondAct_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 1, 1, 17),
    _SleOSPFIfAuthKeySecondAct_Type()
)
sleOSPFIfAuthKeySecondAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfAuthKeySecondAct.setStatus("current")
_SleOSPFIfInfoControl_ObjectIdentity = ObjectIdentity
sleOSPFIfInfoControl = _SleOSPFIfInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2)
)


class _SleOSPFIfInfoControlRequest_Type(Integer32):
    """Custom type sleOSPFIfInfoControlRequest based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("setOSPFIFCost", 1),
          ("setOSPFIFPriority", 2),
          ("setOSPFIFTransmitDelay", 3),
          ("setOSPFIFHelloInterval", 4),
          ("setOSPFIFDeadInterval", 5),
          ("setOSPFIFRetransInterval", 6),
          ("setOSPFIFAuthProfile", 7),
          ("setOSPFIFDataFilterOut", 8),
          ("setOSPFIFMtuIgnore", 9),
          ("setOSPFIFResyncProfile", 10),
          ("setOSPFIFAuthKeyFirstProfile", 11),
          ("setOSPFIFAuthKeySecondProfile", 12))
    )


_SleOSPFIfInfoControlRequest_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlRequest_Object = MibScalar
sleOSPFIfInfoControlRequest = _SleOSPFIfInfoControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 1),
    _SleOSPFIfInfoControlRequest_Type()
)
sleOSPFIfInfoControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlRequest.setStatus("current")
_SleOSPFIfInfoControlStatus_Type = SleControlStatusType
_SleOSPFIfInfoControlStatus_Object = MibScalar
sleOSPFIfInfoControlStatus = _SleOSPFIfInfoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 2),
    _SleOSPFIfInfoControlStatus_Type()
)
sleOSPFIfInfoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlStatus.setStatus("current")
_SleOSPFIfInfoControlTimer_Type = Gauge32
_SleOSPFIfInfoControlTimer_Object = MibScalar
sleOSPFIfInfoControlTimer = _SleOSPFIfInfoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 3),
    _SleOSPFIfInfoControlTimer_Type()
)
sleOSPFIfInfoControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlTimer.setStatus("current")
_SleOSPFIfInfoControlTimeStamp_Type = TimeTicks
_SleOSPFIfInfoControlTimeStamp_Object = MibScalar
sleOSPFIfInfoControlTimeStamp = _SleOSPFIfInfoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 4),
    _SleOSPFIfInfoControlTimeStamp_Type()
)
sleOSPFIfInfoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlTimeStamp.setStatus("current")
_SleOSPFIfInfoControlReqResult_Type = SleControlRequestResultType
_SleOSPFIfInfoControlReqResult_Object = MibScalar
sleOSPFIfInfoControlReqResult = _SleOSPFIfInfoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 5),
    _SleOSPFIfInfoControlReqResult_Type()
)
sleOSPFIfInfoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlReqResult.setStatus("current")


class _SleOSPFIfInfoControlIndex_Type(Integer32):
    """Custom type sleOSPFIfInfoControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfInfoControlIndex_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlIndex_Object = MibScalar
sleOSPFIfInfoControlIndex = _SleOSPFIfInfoControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 6),
    _SleOSPFIfInfoControlIndex_Type()
)
sleOSPFIfInfoControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlIndex.setStatus("current")
_SleOSPFIfInfoControlIpAddr_Type = IpAddress
_SleOSPFIfInfoControlIpAddr_Object = MibScalar
sleOSPFIfInfoControlIpAddr = _SleOSPFIfInfoControlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 7),
    _SleOSPFIfInfoControlIpAddr_Type()
)
sleOSPFIfInfoControlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlIpAddr.setStatus("current")


class _SleOSPFIfInfoControlCost_Type(Integer32):
    """Custom type sleOSPFIfInfoControlCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfInfoControlCost_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlCost_Object = MibScalar
sleOSPFIfInfoControlCost = _SleOSPFIfInfoControlCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 8),
    _SleOSPFIfInfoControlCost_Type()
)
sleOSPFIfInfoControlCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlCost.setStatus("current")


class _SleOSPFIfInfoControlTransmitDelay_Type(Integer32):
    """Custom type sleOSPFIfInfoControlTransmitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfInfoControlTransmitDelay_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlTransmitDelay_Object = MibScalar
sleOSPFIfInfoControlTransmitDelay = _SleOSPFIfInfoControlTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 9),
    _SleOSPFIfInfoControlTransmitDelay_Type()
)
sleOSPFIfInfoControlTransmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlTransmitDelay.setStatus("current")


class _SleOSPFIfInfoControlPriority_Type(Integer32):
    """Custom type sleOSPFIfInfoControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFIfInfoControlPriority_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlPriority_Object = MibScalar
sleOSPFIfInfoControlPriority = _SleOSPFIfInfoControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 10),
    _SleOSPFIfInfoControlPriority_Type()
)
sleOSPFIfInfoControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlPriority.setStatus("current")


class _SleOSPFIfInfoControlHelloInterval_Type(Integer32):
    """Custom type sleOSPFIfInfoControlHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfInfoControlHelloInterval_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlHelloInterval_Object = MibScalar
sleOSPFIfInfoControlHelloInterval = _SleOSPFIfInfoControlHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 11),
    _SleOSPFIfInfoControlHelloInterval_Type()
)
sleOSPFIfInfoControlHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlHelloInterval.setStatus("current")


class _SleOSPFIfInfoControlDeadInterval_Type(Integer32):
    """Custom type sleOSPFIfInfoControlDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfInfoControlDeadInterval_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlDeadInterval_Object = MibScalar
sleOSPFIfInfoControlDeadInterval = _SleOSPFIfInfoControlDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 12),
    _SleOSPFIfInfoControlDeadInterval_Type()
)
sleOSPFIfInfoControlDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlDeadInterval.setStatus("current")


class _SleOSPFIfInfoControlRetransInterval_Type(Integer32):
    """Custom type sleOSPFIfInfoControlRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfInfoControlRetransInterval_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlRetransInterval_Object = MibScalar
sleOSPFIfInfoControlRetransInterval = _SleOSPFIfInfoControlRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 13),
    _SleOSPFIfInfoControlRetransInterval_Type()
)
sleOSPFIfInfoControlRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlRetransInterval.setStatus("current")


class _SleOSPFIfInfoControlAuth_Type(Integer32):
    """Custom type sleOSPFIfInfoControlAuth based on Integer32"""
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


_SleOSPFIfInfoControlAuth_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlAuth_Object = MibScalar
sleOSPFIfInfoControlAuth = _SleOSPFIfInfoControlAuth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 14),
    _SleOSPFIfInfoControlAuth_Type()
)
sleOSPFIfInfoControlAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlAuth.setStatus("current")


class _SleOSPFIfInfoControlAuthType_Type(Integer32):
    """Custom type sleOSPFIfInfoControlAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("simple", 1),
          ("crypt", 2))
    )


_SleOSPFIfInfoControlAuthType_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlAuthType_Object = MibScalar
sleOSPFIfInfoControlAuthType = _SleOSPFIfInfoControlAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 15),
    _SleOSPFIfInfoControlAuthType_Type()
)
sleOSPFIfInfoControlAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlAuthType.setStatus("current")


class _SleOSPFIfInfoControlDataFilterOut_Type(Integer32):
    """Custom type sleOSPFIfInfoControlDataFilterOut based on Integer32"""
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


_SleOSPFIfInfoControlDataFilterOut_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlDataFilterOut_Object = MibScalar
sleOSPFIfInfoControlDataFilterOut = _SleOSPFIfInfoControlDataFilterOut_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 16),
    _SleOSPFIfInfoControlDataFilterOut_Type()
)
sleOSPFIfInfoControlDataFilterOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlDataFilterOut.setStatus("current")


class _SleOSPFIfInfoControlMTUIgnore_Type(Integer32):
    """Custom type sleOSPFIfInfoControlMTUIgnore based on Integer32"""
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


_SleOSPFIfInfoControlMTUIgnore_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlMTUIgnore_Object = MibScalar
sleOSPFIfInfoControlMTUIgnore = _SleOSPFIfInfoControlMTUIgnore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 17),
    _SleOSPFIfInfoControlMTUIgnore_Type()
)
sleOSPFIfInfoControlMTUIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlMTUIgnore.setStatus("current")


class _SleOSPFIfInfoControlResync_Type(Integer32):
    """Custom type sleOSPFIfInfoControlResync based on Integer32"""
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


_SleOSPFIfInfoControlResync_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlResync_Object = MibScalar
sleOSPFIfInfoControlResync = _SleOSPFIfInfoControlResync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 18),
    _SleOSPFIfInfoControlResync_Type()
)
sleOSPFIfInfoControlResync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlResync.setStatus("current")


class _SleOSPFIfInfoControlResyncTimeout_Type(Integer32):
    """Custom type sleOSPFIfInfoControlResyncTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfInfoControlResyncTimeout_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlResyncTimeout_Object = MibScalar
sleOSPFIfInfoControlResyncTimeout = _SleOSPFIfInfoControlResyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 19),
    _SleOSPFIfInfoControlResyncTimeout_Type()
)
sleOSPFIfInfoControlResyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlResyncTimeout.setStatus("current")
_SleOSPFIfInfoControlAuthKeyFirst_Type = OctetString
_SleOSPFIfInfoControlAuthKeyFirst_Object = MibScalar
sleOSPFIfInfoControlAuthKeyFirst = _SleOSPFIfInfoControlAuthKeyFirst_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 20),
    _SleOSPFIfInfoControlAuthKeyFirst_Type()
)
sleOSPFIfInfoControlAuthKeyFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlAuthKeyFirst.setStatus("current")


class _SleOSPFIfInfoControlAuthKeyFirstAct_Type(Integer32):
    """Custom type sleOSPFIfInfoControlAuthKeyFirstAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 0),
          ("active", 1))
    )


_SleOSPFIfInfoControlAuthKeyFirstAct_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlAuthKeyFirstAct_Object = MibScalar
sleOSPFIfInfoControlAuthKeyFirstAct = _SleOSPFIfInfoControlAuthKeyFirstAct_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 21),
    _SleOSPFIfInfoControlAuthKeyFirstAct_Type()
)
sleOSPFIfInfoControlAuthKeyFirstAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlAuthKeyFirstAct.setStatus("current")
_SleOSPFIfInfoControlAuthKeySecond_Type = OctetString
_SleOSPFIfInfoControlAuthKeySecond_Object = MibScalar
sleOSPFIfInfoControlAuthKeySecond = _SleOSPFIfInfoControlAuthKeySecond_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 22),
    _SleOSPFIfInfoControlAuthKeySecond_Type()
)
sleOSPFIfInfoControlAuthKeySecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlAuthKeySecond.setStatus("current")


class _SleOSPFIfInfoControlAuthKeySecondAct_Type(Integer32):
    """Custom type sleOSPFIfInfoControlAuthKeySecondAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 0),
          ("active", 1))
    )


_SleOSPFIfInfoControlAuthKeySecondAct_Type.__name__ = "Integer32"
_SleOSPFIfInfoControlAuthKeySecondAct_Object = MibScalar
sleOSPFIfInfoControlAuthKeySecondAct = _SleOSPFIfInfoControlAuthKeySecondAct_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 2, 23),
    _SleOSPFIfInfoControlAuthKeySecondAct_Type()
)
sleOSPFIfInfoControlAuthKeySecondAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfInfoControlAuthKeySecondAct.setStatus("current")
_SleOSPFIfInfoNotification_ObjectIdentity = ObjectIdentity
sleOSPFIfInfoNotification = _SleOSPFIfInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3)
)
_SleOSPFIfMsgKey_ObjectIdentity = ObjectIdentity
sleOSPFIfMsgKey = _SleOSPFIfMsgKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3)
)
_SleOSPFIfMsgKeyTable_Object = MibTable
sleOSPFIfMsgKeyTable = _SleOSPFIfMsgKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyTable.setStatus("current")
_SleOSPFIfMsgKeyEntry_Object = MibTableRow
sleOSPFIfMsgKeyEntry = _SleOSPFIfMsgKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 1, 1)
)
sleOSPFIfMsgKeyEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFIfIndex"),
    (0, "SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
    (0, "SLE-OSPF-MIB", "sleOSPFIfMsgKeyID"),
)
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyEntry.setStatus("current")


class _SleOSPFIfMsgKeyID_Type(Integer32):
    """Custom type sleOSPFIfMsgKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFIfMsgKeyID_Type.__name__ = "Integer32"
_SleOSPFIfMsgKeyID_Object = MibTableColumn
sleOSPFIfMsgKeyID = _SleOSPFIfMsgKeyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 1, 1, 1),
    _SleOSPFIfMsgKeyID_Type()
)
sleOSPFIfMsgKeyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyID.setStatus("current")
_SleOSPFIfMsgKeyVal_Type = OctetString
_SleOSPFIfMsgKeyVal_Object = MibTableColumn
sleOSPFIfMsgKeyVal = _SleOSPFIfMsgKeyVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 1, 1, 2),
    _SleOSPFIfMsgKeyVal_Type()
)
sleOSPFIfMsgKeyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyVal.setStatus("current")


class _SleOSPFIfMsgKeyAct_Type(Integer32):
    """Custom type sleOSPFIfMsgKeyAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 0),
          ("active", 1))
    )


_SleOSPFIfMsgKeyAct_Type.__name__ = "Integer32"
_SleOSPFIfMsgKeyAct_Object = MibTableColumn
sleOSPFIfMsgKeyAct = _SleOSPFIfMsgKeyAct_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 1, 1, 3),
    _SleOSPFIfMsgKeyAct_Type()
)
sleOSPFIfMsgKeyAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyAct.setStatus("current")
_SleOSPFIfMsgKeyControl_ObjectIdentity = ObjectIdentity
sleOSPFIfMsgKeyControl = _SleOSPFIfMsgKeyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2)
)


class _SleOSPFIfMsgKeyControlRequest_Type(Integer32):
    """Custom type sleOSPFIfMsgKeyControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createMsgDigestKey", 1),
          ("deleteMsgDigestKey", 2))
    )


_SleOSPFIfMsgKeyControlRequest_Type.__name__ = "Integer32"
_SleOSPFIfMsgKeyControlRequest_Object = MibScalar
sleOSPFIfMsgKeyControlRequest = _SleOSPFIfMsgKeyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 1),
    _SleOSPFIfMsgKeyControlRequest_Type()
)
sleOSPFIfMsgKeyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlRequest.setStatus("current")
_SleOSPFIfMsgKeyControlStatus_Type = SleControlStatusType
_SleOSPFIfMsgKeyControlStatus_Object = MibScalar
sleOSPFIfMsgKeyControlStatus = _SleOSPFIfMsgKeyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 2),
    _SleOSPFIfMsgKeyControlStatus_Type()
)
sleOSPFIfMsgKeyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlStatus.setStatus("current")
_SleOSPFIfMsgKeyControlTimer_Type = Gauge32
_SleOSPFIfMsgKeyControlTimer_Object = MibScalar
sleOSPFIfMsgKeyControlTimer = _SleOSPFIfMsgKeyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 3),
    _SleOSPFIfMsgKeyControlTimer_Type()
)
sleOSPFIfMsgKeyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlTimer.setStatus("current")
_SleOSPFIfMsgKeyControlTimeStamp_Type = TimeTicks
_SleOSPFIfMsgKeyControlTimeStamp_Object = MibScalar
sleOSPFIfMsgKeyControlTimeStamp = _SleOSPFIfMsgKeyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 4),
    _SleOSPFIfMsgKeyControlTimeStamp_Type()
)
sleOSPFIfMsgKeyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlTimeStamp.setStatus("current")
_SleOSPFIfMsgKeyControlReqResult_Type = SleControlRequestResultType
_SleOSPFIfMsgKeyControlReqResult_Object = MibScalar
sleOSPFIfMsgKeyControlReqResult = _SleOSPFIfMsgKeyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 5),
    _SleOSPFIfMsgKeyControlReqResult_Type()
)
sleOSPFIfMsgKeyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlReqResult.setStatus("current")


class _SleOSPFIfMsgKeyControlIndex_Type(Integer32):
    """Custom type sleOSPFIfMsgKeyControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfMsgKeyControlIndex_Type.__name__ = "Integer32"
_SleOSPFIfMsgKeyControlIndex_Object = MibScalar
sleOSPFIfMsgKeyControlIndex = _SleOSPFIfMsgKeyControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 6),
    _SleOSPFIfMsgKeyControlIndex_Type()
)
sleOSPFIfMsgKeyControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlIndex.setStatus("current")
_SleOSPFIfMsgKeyControlIpAddr_Type = IpAddress
_SleOSPFIfMsgKeyControlIpAddr_Object = MibScalar
sleOSPFIfMsgKeyControlIpAddr = _SleOSPFIfMsgKeyControlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 7),
    _SleOSPFIfMsgKeyControlIpAddr_Type()
)
sleOSPFIfMsgKeyControlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlIpAddr.setStatus("current")


class _SleOSPFIfMsgKeyControlKeyID_Type(Integer32):
    """Custom type sleOSPFIfMsgKeyControlKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFIfMsgKeyControlKeyID_Type.__name__ = "Integer32"
_SleOSPFIfMsgKeyControlKeyID_Object = MibScalar
sleOSPFIfMsgKeyControlKeyID = _SleOSPFIfMsgKeyControlKeyID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 8),
    _SleOSPFIfMsgKeyControlKeyID_Type()
)
sleOSPFIfMsgKeyControlKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlKeyID.setStatus("current")
_SleOSPFIfMsgKeyControlKeyVal_Type = OctetString
_SleOSPFIfMsgKeyControlKeyVal_Object = MibScalar
sleOSPFIfMsgKeyControlKeyVal = _SleOSPFIfMsgKeyControlKeyVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 9),
    _SleOSPFIfMsgKeyControlKeyVal_Type()
)
sleOSPFIfMsgKeyControlKeyVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlKeyVal.setStatus("current")


class _SleOSPFIfMsgKeyControlKeyAct_Type(Integer32):
    """Custom type sleOSPFIfMsgKeyControlKeyAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 0),
          ("active", 1))
    )


_SleOSPFIfMsgKeyControlKeyAct_Type.__name__ = "Integer32"
_SleOSPFIfMsgKeyControlKeyAct_Object = MibScalar
sleOSPFIfMsgKeyControlKeyAct = _SleOSPFIfMsgKeyControlKeyAct_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 2, 10),
    _SleOSPFIfMsgKeyControlKeyAct_Type()
)
sleOSPFIfMsgKeyControlKeyAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyControlKeyAct.setStatus("current")
_SleOSPFIfMsgKeyNotification_ObjectIdentity = ObjectIdentity
sleOSPFIfMsgKeyNotification = _SleOSPFIfMsgKeyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 3)
)
_SleOSPFIfStatus_ObjectIdentity = ObjectIdentity
sleOSPFIfStatus = _SleOSPFIfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4)
)
_SleOSPFIfStatusTable_Object = MibTable
sleOSPFIfStatusTable = _SleOSPFIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1)
)
if mibBuilder.loadTexts:
    sleOSPFIfStatusTable.setStatus("current")
_SleOSPFIfStatusEntry_Object = MibTableRow
sleOSPFIfStatusEntry = _SleOSPFIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1)
)
sleOSPFIfStatusEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFIfIndex"),
    (0, "SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
)
if mibBuilder.loadTexts:
    sleOSPFIfStatusEntry.setStatus("current")
_SleOSPFIfStatusAddr_Type = IpAddress
_SleOSPFIfStatusAddr_Object = MibTableColumn
sleOSPFIfStatusAddr = _SleOSPFIfStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 1),
    _SleOSPFIfStatusAddr_Type()
)
sleOSPFIfStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusAddr.setStatus("current")


class _SleOSPFIfStatusUpState_Type(Integer32):
    """Custom type sleOSPFIfStatusUpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_SleOSPFIfStatusUpState_Type.__name__ = "Integer32"
_SleOSPFIfStatusUpState_Object = MibTableColumn
sleOSPFIfStatusUpState = _SleOSPFIfStatusUpState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 2),
    _SleOSPFIfStatusUpState_Type()
)
sleOSPFIfStatusUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusUpState.setStatus("current")
_SleOSPFIfStatusAreaID_Type = IpAddress
_SleOSPFIfStatusAreaID_Object = MibTableColumn
sleOSPFIfStatusAreaID = _SleOSPFIfStatusAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 3),
    _SleOSPFIfStatusAreaID_Type()
)
sleOSPFIfStatusAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusAreaID.setStatus("current")


class _SleOSPFIfStatusProcID_Type(Integer32):
    """Custom type sleOSPFIfStatusProcID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfStatusProcID_Type.__name__ = "Integer32"
_SleOSPFIfStatusProcID_Object = MibTableColumn
sleOSPFIfStatusProcID = _SleOSPFIfStatusProcID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 4),
    _SleOSPFIfStatusProcID_Type()
)
sleOSPFIfStatusProcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusProcID.setStatus("current")
_SleOSPFIfStatusRouterID_Type = IpAddress
_SleOSPFIfStatusRouterID_Object = MibTableColumn
sleOSPFIfStatusRouterID = _SleOSPFIfStatusRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 5),
    _SleOSPFIfStatusRouterID_Type()
)
sleOSPFIfStatusRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusRouterID.setStatus("current")


class _SleOSPFIfStatusNetworkType_Type(Integer32):
    """Custom type sleOSPFIfStatusNetworkType based on Integer32"""
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
          ("pointTopoint", 1),
          ("broadcast", 2),
          ("nbma", 3),
          ("pointTomultipoint", 4),
          ("poiintTomultipointnbma", 5),
          ("virtuallink", 6),
          ("loopback", 7))
    )


_SleOSPFIfStatusNetworkType_Type.__name__ = "Integer32"
_SleOSPFIfStatusNetworkType_Object = MibTableColumn
sleOSPFIfStatusNetworkType = _SleOSPFIfStatusNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 6),
    _SleOSPFIfStatusNetworkType_Type()
)
sleOSPFIfStatusNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusNetworkType.setStatus("current")


class _SleOSPFIfStatusCost_Type(Integer32):
    """Custom type sleOSPFIfStatusCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfStatusCost_Type.__name__ = "Integer32"
_SleOSPFIfStatusCost_Object = MibTableColumn
sleOSPFIfStatusCost = _SleOSPFIfStatusCost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 7),
    _SleOSPFIfStatusCost_Type()
)
sleOSPFIfStatusCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusCost.setStatus("current")


class _SleOSPFIfStatusTransmitDelay_Type(Integer32):
    """Custom type sleOSPFIfStatusTransmitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfStatusTransmitDelay_Type.__name__ = "Integer32"
_SleOSPFIfStatusTransmitDelay_Object = MibTableColumn
sleOSPFIfStatusTransmitDelay = _SleOSPFIfStatusTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 8),
    _SleOSPFIfStatusTransmitDelay_Type()
)
sleOSPFIfStatusTransmitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusTransmitDelay.setStatus("current")


class _SleOSPFIfStatusState_Type(Integer32):
    """Custom type sleOSPFIfStatusState based on Integer32"""
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
          ("pointTopoint", 4),
          ("drother", 5),
          ("backup", 6),
          ("dr", 7))
    )


_SleOSPFIfStatusState_Type.__name__ = "Integer32"
_SleOSPFIfStatusState_Object = MibTableColumn
sleOSPFIfStatusState = _SleOSPFIfStatusState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 9),
    _SleOSPFIfStatusState_Type()
)
sleOSPFIfStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusState.setStatus("current")


class _SleOSPFIfStatusPriorityUse_Type(Integer32):
    """Custom type sleOSPFIfStatusPriorityUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nouse", 0),
          ("use", 1))
    )


_SleOSPFIfStatusPriorityUse_Type.__name__ = "Integer32"
_SleOSPFIfStatusPriorityUse_Object = MibTableColumn
sleOSPFIfStatusPriorityUse = _SleOSPFIfStatusPriorityUse_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 10),
    _SleOSPFIfStatusPriorityUse_Type()
)
sleOSPFIfStatusPriorityUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusPriorityUse.setStatus("current")


class _SleOSPFIfStatusPriority_Type(Integer32):
    """Custom type sleOSPFIfStatusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleOSPFIfStatusPriority_Type.__name__ = "Integer32"
_SleOSPFIfStatusPriority_Object = MibTableColumn
sleOSPFIfStatusPriority = _SleOSPFIfStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 11),
    _SleOSPFIfStatusPriority_Type()
)
sleOSPFIfStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusPriority.setStatus("current")


class _SleOSPFIfStatusDRRouterUse_Type(Integer32):
    """Custom type sleOSPFIfStatusDRRouterUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nouse", 0),
          ("use", 1))
    )


_SleOSPFIfStatusDRRouterUse_Type.__name__ = "Integer32"
_SleOSPFIfStatusDRRouterUse_Object = MibTableColumn
sleOSPFIfStatusDRRouterUse = _SleOSPFIfStatusDRRouterUse_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 12),
    _SleOSPFIfStatusDRRouterUse_Type()
)
sleOSPFIfStatusDRRouterUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusDRRouterUse.setStatus("current")
_SleOSPFIfStatusDRRouterID_Type = IpAddress
_SleOSPFIfStatusDRRouterID_Object = MibTableColumn
sleOSPFIfStatusDRRouterID = _SleOSPFIfStatusDRRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 13),
    _SleOSPFIfStatusDRRouterID_Type()
)
sleOSPFIfStatusDRRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusDRRouterID.setStatus("current")
_SleOSPFIfStatusDRIfIpAddr_Type = IpAddress
_SleOSPFIfStatusDRIfIpAddr_Object = MibTableColumn
sleOSPFIfStatusDRIfIpAddr = _SleOSPFIfStatusDRIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 14),
    _SleOSPFIfStatusDRIfIpAddr_Type()
)
sleOSPFIfStatusDRIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusDRIfIpAddr.setStatus("current")


class _SleOSPFIfStatusBDRRouterUse_Type(Integer32):
    """Custom type sleOSPFIfStatusBDRRouterUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nouse", 0),
          ("use", 1))
    )


_SleOSPFIfStatusBDRRouterUse_Type.__name__ = "Integer32"
_SleOSPFIfStatusBDRRouterUse_Object = MibTableColumn
sleOSPFIfStatusBDRRouterUse = _SleOSPFIfStatusBDRRouterUse_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 15),
    _SleOSPFIfStatusBDRRouterUse_Type()
)
sleOSPFIfStatusBDRRouterUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusBDRRouterUse.setStatus("current")
_SleOSPFIfStatusBDRRouterID_Type = IpAddress
_SleOSPFIfStatusBDRRouterID_Object = MibTableColumn
sleOSPFIfStatusBDRRouterID = _SleOSPFIfStatusBDRRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 16),
    _SleOSPFIfStatusBDRRouterID_Type()
)
sleOSPFIfStatusBDRRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusBDRRouterID.setStatus("current")
_SleOSPFIfStatusBDRIfIpAddr_Type = IpAddress
_SleOSPFIfStatusBDRIfIpAddr_Object = MibTableColumn
sleOSPFIfStatusBDRIfIpAddr = _SleOSPFIfStatusBDRIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 17),
    _SleOSPFIfStatusBDRIfIpAddr_Type()
)
sleOSPFIfStatusBDRIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusBDRIfIpAddr.setStatus("current")


class _SleOSPFIfStatusHelloInterval_Type(Integer32):
    """Custom type sleOSPFIfStatusHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfStatusHelloInterval_Type.__name__ = "Integer32"
_SleOSPFIfStatusHelloInterval_Object = MibTableColumn
sleOSPFIfStatusHelloInterval = _SleOSPFIfStatusHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 18),
    _SleOSPFIfStatusHelloInterval_Type()
)
sleOSPFIfStatusHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusHelloInterval.setStatus("current")


class _SleOSPFIfStatusDeadInterval_Type(Integer32):
    """Custom type sleOSPFIfStatusDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfStatusDeadInterval_Type.__name__ = "Integer32"
_SleOSPFIfStatusDeadInterval_Object = MibTableColumn
sleOSPFIfStatusDeadInterval = _SleOSPFIfStatusDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 19),
    _SleOSPFIfStatusDeadInterval_Type()
)
sleOSPFIfStatusDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusDeadInterval.setStatus("current")


class _SleOSPFIfStatusRetransInterval_Type(Integer32):
    """Custom type sleOSPFIfStatusRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfStatusRetransInterval_Type.__name__ = "Integer32"
_SleOSPFIfStatusRetransInterval_Object = MibTableColumn
sleOSPFIfStatusRetransInterval = _SleOSPFIfStatusRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 20),
    _SleOSPFIfStatusRetransInterval_Type()
)
sleOSPFIfStatusRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusRetransInterval.setStatus("current")


class _SleOSPFIfStatusWaitInterval_Type(Integer32):
    """Custom type sleOSPFIfStatusWaitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFIfStatusWaitInterval_Type.__name__ = "Integer32"
_SleOSPFIfStatusWaitInterval_Object = MibTableColumn
sleOSPFIfStatusWaitInterval = _SleOSPFIfStatusWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 21),
    _SleOSPFIfStatusWaitInterval_Type()
)
sleOSPFIfStatusWaitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusWaitInterval.setStatus("current")
_SleOSPFIfStatusNeighborCount_Type = Integer32
_SleOSPFIfStatusNeighborCount_Object = MibTableColumn
sleOSPFIfStatusNeighborCount = _SleOSPFIfStatusNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 22),
    _SleOSPFIfStatusNeighborCount_Type()
)
sleOSPFIfStatusNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusNeighborCount.setStatus("current")
_SleOSPFIfCryptSeqNum_Type = Gauge32
_SleOSPFIfCryptSeqNum_Object = MibTableColumn
sleOSPFIfCryptSeqNum = _SleOSPFIfCryptSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 23),
    _SleOSPFIfCryptSeqNum_Type()
)
sleOSPFIfCryptSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfCryptSeqNum.setStatus("current")
_SleOSPFIfStatusRcvHello_Type = Gauge32
_SleOSPFIfStatusRcvHello_Object = MibTableColumn
sleOSPFIfStatusRcvHello = _SleOSPFIfStatusRcvHello_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 24),
    _SleOSPFIfStatusRcvHello_Type()
)
sleOSPFIfStatusRcvHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusRcvHello.setStatus("current")
_SleOSPFIfStatusSendHello_Type = Gauge32
_SleOSPFIfStatusSendHello_Object = MibTableColumn
sleOSPFIfStatusSendHello = _SleOSPFIfStatusSendHello_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 25),
    _SleOSPFIfStatusSendHello_Type()
)
sleOSPFIfStatusSendHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusSendHello.setStatus("current")
_SleOSPFIfStatusRcvDD_Type = Gauge32
_SleOSPFIfStatusRcvDD_Object = MibTableColumn
sleOSPFIfStatusRcvDD = _SleOSPFIfStatusRcvDD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 26),
    _SleOSPFIfStatusRcvDD_Type()
)
sleOSPFIfStatusRcvDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusRcvDD.setStatus("current")
_SleOSPFIfStatusSendDD_Type = Gauge32
_SleOSPFIfStatusSendDD_Object = MibTableColumn
sleOSPFIfStatusSendDD = _SleOSPFIfStatusSendDD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 27),
    _SleOSPFIfStatusSendDD_Type()
)
sleOSPFIfStatusSendDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusSendDD.setStatus("current")
_SleOSPFIfStatusRcvLSReq_Type = Gauge32
_SleOSPFIfStatusRcvLSReq_Object = MibTableColumn
sleOSPFIfStatusRcvLSReq = _SleOSPFIfStatusRcvLSReq_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 28),
    _SleOSPFIfStatusRcvLSReq_Type()
)
sleOSPFIfStatusRcvLSReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusRcvLSReq.setStatus("current")
_SleOSPFIfStatusSendLSReq_Type = Gauge32
_SleOSPFIfStatusSendLSReq_Object = MibTableColumn
sleOSPFIfStatusSendLSReq = _SleOSPFIfStatusSendLSReq_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 29),
    _SleOSPFIfStatusSendLSReq_Type()
)
sleOSPFIfStatusSendLSReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusSendLSReq.setStatus("current")
_SleOSPFIfStatusRcvLSUpd_Type = Gauge32
_SleOSPFIfStatusRcvLSUpd_Object = MibTableColumn
sleOSPFIfStatusRcvLSUpd = _SleOSPFIfStatusRcvLSUpd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 30),
    _SleOSPFIfStatusRcvLSUpd_Type()
)
sleOSPFIfStatusRcvLSUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusRcvLSUpd.setStatus("current")
_SleOSPFIfStatusSendLSUpd_Type = Gauge32
_SleOSPFIfStatusSendLSUpd_Object = MibTableColumn
sleOSPFIfStatusSendLSUpd = _SleOSPFIfStatusSendLSUpd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 31),
    _SleOSPFIfStatusSendLSUpd_Type()
)
sleOSPFIfStatusSendLSUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusSendLSUpd.setStatus("current")
_SleOSPFIfStatusRcvLSAck_Type = Gauge32
_SleOSPFIfStatusRcvLSAck_Object = MibTableColumn
sleOSPFIfStatusRcvLSAck = _SleOSPFIfStatusRcvLSAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 32),
    _SleOSPFIfStatusRcvLSAck_Type()
)
sleOSPFIfStatusRcvLSAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusRcvLSAck.setStatus("current")
_SleOSPFIfStatusSendLSAck_Type = Gauge32
_SleOSPFIfStatusSendLSAck_Object = MibTableColumn
sleOSPFIfStatusSendLSAck = _SleOSPFIfStatusSendLSAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 33),
    _SleOSPFIfStatusSendLSAck_Type()
)
sleOSPFIfStatusSendLSAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusSendLSAck.setStatus("current")
_SleOSPFIfStatusDiscarded_Type = Gauge32
_SleOSPFIfStatusDiscarded_Object = MibTableColumn
sleOSPFIfStatusDiscarded = _SleOSPFIfStatusDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 34),
    _SleOSPFIfStatusDiscarded_Type()
)
sleOSPFIfStatusDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusDiscarded.setStatus("current")
_SleOSPFIfStatusMtu_Type = Integer32
_SleOSPFIfStatusMtu_Object = MibTableColumn
sleOSPFIfStatusMtu = _SleOSPFIfStatusMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 4, 1, 1, 35),
    _SleOSPFIfStatusMtu_Type()
)
sleOSPFIfStatusMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFIfStatusMtu.setStatus("current")
_SleOSPFLsa_ObjectIdentity = ObjectIdentity
sleOSPFLsa = _SleOSPFLsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4)
)
_SleOSPFLsaTable_Object = MibTable
sleOSPFLsaTable = _SleOSPFLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1)
)
if mibBuilder.loadTexts:
    sleOSPFLsaTable.setStatus("current")
_SleOSPFLsaEntry_Object = MibTableRow
sleOSPFLsaEntry = _SleOSPFLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1, 1)
)
sleOSPFLsaEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFLsaType"),
    (0, "SLE-OSPF-MIB", "sleOSPFLsaAreaID"),
    (0, "SLE-OSPF-MIB", "sleOSPFLsaLinkID"),
    (0, "SLE-OSPF-MIB", "sleOSPFLsaAdvRouter"),
)
if mibBuilder.loadTexts:
    sleOSPFLsaEntry.setStatus("current")


class _SleOSPFLsaType_Type(Integer32):
    """Custom type sleOSPFLsaType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("routerLsa", 2),
          ("networkLsa", 3),
          ("summaryLsa", 4),
          ("summaryLsaAsbr", 5),
          ("asExternalLsa", 6),
          ("groupMemberLsa", 7),
          ("asNssaLsa", 8),
          ("externalAttributeLsa", 9),
          ("linkOpaqueLsa", 10),
          ("areaOpaqueLsa", 11),
          ("asOpaqueLsa", 12))
    )


_SleOSPFLsaType_Type.__name__ = "Integer32"
_SleOSPFLsaType_Object = MibTableColumn
sleOSPFLsaType = _SleOSPFLsaType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1, 1, 1),
    _SleOSPFLsaType_Type()
)
sleOSPFLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFLsaType.setStatus("current")
_SleOSPFLsaAreaID_Type = IpAddress
_SleOSPFLsaAreaID_Object = MibTableColumn
sleOSPFLsaAreaID = _SleOSPFLsaAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1, 1, 2),
    _SleOSPFLsaAreaID_Type()
)
sleOSPFLsaAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFLsaAreaID.setStatus("current")
_SleOSPFLsaLinkID_Type = IpAddress
_SleOSPFLsaLinkID_Object = MibTableColumn
sleOSPFLsaLinkID = _SleOSPFLsaLinkID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1, 1, 3),
    _SleOSPFLsaLinkID_Type()
)
sleOSPFLsaLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFLsaLinkID.setStatus("current")
_SleOSPFLsaAdvRouter_Type = IpAddress
_SleOSPFLsaAdvRouter_Object = MibTableColumn
sleOSPFLsaAdvRouter = _SleOSPFLsaAdvRouter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1, 1, 4),
    _SleOSPFLsaAdvRouter_Type()
)
sleOSPFLsaAdvRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFLsaAdvRouter.setStatus("current")
_SleOSPFLsaAge_Type = Integer32
_SleOSPFLsaAge_Object = MibTableColumn
sleOSPFLsaAge = _SleOSPFLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1, 1, 5),
    _SleOSPFLsaAge_Type()
)
sleOSPFLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFLsaAge.setStatus("current")
_SleOSPFLsaSequence_Type = Gauge32
_SleOSPFLsaSequence_Object = MibTableColumn
sleOSPFLsaSequence = _SleOSPFLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 4, 1, 1, 6),
    _SleOSPFLsaSequence_Type()
)
sleOSPFLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFLsaSequence.setStatus("current")
_SleOSPFNeighbor_ObjectIdentity = ObjectIdentity
sleOSPFNeighbor = _SleOSPFNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5)
)
_SleOSPFNeighborTable_Object = MibTable
sleOSPFNeighborTable = _SleOSPFNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5, 1)
)
if mibBuilder.loadTexts:
    sleOSPFNeighborTable.setStatus("current")
_SleOSPFNeighborEntry_Object = MibTableRow
sleOSPFNeighborEntry = _SleOSPFNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5, 1, 1)
)
sleOSPFNeighborEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFNeighborIPAddr"),
)
if mibBuilder.loadTexts:
    sleOSPFNeighborEntry.setStatus("current")
_SleOSPFNeighborIPAddr_Type = IpAddress
_SleOSPFNeighborIPAddr_Object = MibTableColumn
sleOSPFNeighborIPAddr = _SleOSPFNeighborIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5, 1, 1, 1),
    _SleOSPFNeighborIPAddr_Type()
)
sleOSPFNeighborIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFNeighborIPAddr.setStatus("current")
_SleOSPFNeighborID_Type = IpAddress
_SleOSPFNeighborID_Object = MibTableColumn
sleOSPFNeighborID = _SleOSPFNeighborID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5, 1, 1, 2),
    _SleOSPFNeighborID_Type()
)
sleOSPFNeighborID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFNeighborID.setStatus("current")
_SleOSPFNeighborPriority_Type = Integer32
_SleOSPFNeighborPriority_Object = MibTableColumn
sleOSPFNeighborPriority = _SleOSPFNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5, 1, 1, 3),
    _SleOSPFNeighborPriority_Type()
)
sleOSPFNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFNeighborPriority.setStatus("current")


class _SleOSPFNeighborState_Type(Integer32):
    """Custom type sleOSPFNeighborState based on Integer32"""
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
          ("twoway", 4),
          ("exstart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_SleOSPFNeighborState_Type.__name__ = "Integer32"
_SleOSPFNeighborState_Object = MibTableColumn
sleOSPFNeighborState = _SleOSPFNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5, 1, 1, 4),
    _SleOSPFNeighborState_Type()
)
sleOSPFNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFNeighborState.setStatus("current")
_SleOSPFNeighborIfName_Type = OctetString
_SleOSPFNeighborIfName_Object = MibTableColumn
sleOSPFNeighborIfName = _SleOSPFNeighborIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 5, 1, 1, 5),
    _SleOSPFNeighborIfName_Type()
)
sleOSPFNeighborIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFNeighborIfName.setStatus("current")
_SleOSPFRoute_ObjectIdentity = ObjectIdentity
sleOSPFRoute = _SleOSPFRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6)
)
_SleOSPFRouteTable_Object = MibTable
sleOSPFRouteTable = _SleOSPFRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1)
)
if mibBuilder.loadTexts:
    sleOSPFRouteTable.setStatus("current")
_SleOSPFRouteEntry_Object = MibTableRow
sleOSPFRouteEntry = _SleOSPFRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1)
)
sleOSPFRouteEntry.setIndexNames(
    (0, "SLE-OSPF-MIB", "sleOSPFProcID"),
    (0, "SLE-OSPF-MIB", "sleOSPFRouteNexthop"),
    (0, "SLE-OSPF-MIB", "sleOSPFRouteNbrID"),
    (0, "SLE-OSPF-MIB", "sleOSPFRoutePathType"),
)
if mibBuilder.loadTexts:
    sleOSPFRouteEntry.setStatus("current")


class _SleOSPFRoutePathType_Type(Integer32):
    """Custom type sleOSPFRoutePathType based on Integer32"""
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
        *(("connected", 1),
          ("intraArea", 2),
          ("interArea", 3),
          ("external", 4),
          ("discard", 5),
          ("unknown", 255))
    )


_SleOSPFRoutePathType_Type.__name__ = "Integer32"
_SleOSPFRoutePathType_Object = MibTableColumn
sleOSPFRoutePathType = _SleOSPFRoutePathType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 1),
    _SleOSPFRoutePathType_Type()
)
sleOSPFRoutePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRoutePathType.setStatus("current")
_SleOSPFRouteNexthop_Type = IpAddress
_SleOSPFRouteNexthop_Object = MibTableColumn
sleOSPFRouteNexthop = _SleOSPFRouteNexthop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 2),
    _SleOSPFRouteNexthop_Type()
)
sleOSPFRouteNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRouteNexthop.setStatus("current")
_SleOSPFRouteNbrID_Type = IpAddress
_SleOSPFRouteNbrID_Object = MibTableColumn
sleOSPFRouteNbrID = _SleOSPFRouteNbrID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 3),
    _SleOSPFRouteNbrID_Type()
)
sleOSPFRouteNbrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRouteNbrID.setStatus("current")


class _SleOSPFRoutePathTypeCode_Type(Integer32):
    """Custom type sleOSPFRoutePathTypeCode based on Integer32"""
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
          ("discard", 2),
          ("ospf", 3),
          ("ia", 4),
          ("e1", 5),
          ("e2", 6),
          ("n1", 7),
          ("n2", 8))
    )


_SleOSPFRoutePathTypeCode_Type.__name__ = "Integer32"
_SleOSPFRoutePathTypeCode_Object = MibTableColumn
sleOSPFRoutePathTypeCode = _SleOSPFRoutePathTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 4),
    _SleOSPFRoutePathTypeCode_Type()
)
sleOSPFRoutePathTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRoutePathTypeCode.setStatus("current")


class _SleOSPFRouteMetric_Type(Integer32):
    """Custom type sleOSPFRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleOSPFRouteMetric_Type.__name__ = "Integer32"
_SleOSPFRouteMetric_Object = MibTableColumn
sleOSPFRouteMetric = _SleOSPFRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 5),
    _SleOSPFRouteMetric_Type()
)
sleOSPFRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRouteMetric.setStatus("current")
_SleOSPFRouteIfName_Type = OctetString
_SleOSPFRouteIfName_Object = MibTableColumn
sleOSPFRouteIfName = _SleOSPFRouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 6),
    _SleOSPFRouteIfName_Type()
)
sleOSPFRouteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRouteIfName.setStatus("current")


class _SleOSPFRouteAreaUse_Type(Integer32):
    """Custom type sleOSPFRouteAreaUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nouse", 0),
          ("use", 1))
    )


_SleOSPFRouteAreaUse_Type.__name__ = "Integer32"
_SleOSPFRouteAreaUse_Object = MibTableColumn
sleOSPFRouteAreaUse = _SleOSPFRouteAreaUse_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 7),
    _SleOSPFRouteAreaUse_Type()
)
sleOSPFRouteAreaUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRouteAreaUse.setStatus("current")
_SleOSPFRouteAreaID_Type = IpAddress
_SleOSPFRouteAreaID_Object = MibTableColumn
sleOSPFRouteAreaID = _SleOSPFRouteAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 6, 1, 1, 8),
    _SleOSPFRouteAreaID_Type()
)
sleOSPFRouteAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOSPFRouteAreaID.setStatus("current")

# Managed Objects groups

sleOspfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 7)
)
sleOspfGroup.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFRestartPeriod"),
        ("SLE-OSPF-MIB", "sleOSPFRestartHelperPolicy"),
        ("SLE-OSPF-MIB", "sleOSPFRestartHelperPeriod"),
        ("SLE-OSPF-MIB", "sleOSPFControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFControlRestartPeriod"),
        ("SLE-OSPF-MIB", "sleOSPFControlRestartHelperPolicy"),
        ("SLE-OSPF-MIB", "sleOSPFControlRestartHelperPeriod"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcRouterID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFDelayTime"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFHoldTime"),
        ("SLE-OSPF-MIB", "sleOSPFProcAutoCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcAbrType"),
        ("SLE-OSPF-MIB", "sleOSPFProcSnmpNotification"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultMetricConfig"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultMetricValue"),
        ("SLE-OSPF-MIB", "sleOSPFProcMaxArea"),
        ("SLE-OSPF-MIB", "sleOSPFProcMaxConcurrentDD"),
        ("SLE-OSPF-MIB", "sleOSPFProcCompatiblerfc1583"),
        ("SLE-OSPF-MIB", "sleOSPFProcCapabilityOpaque"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSDBOverflowType"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSDBOverflowLimit"),
        ("SLE-OSPF-MIB", "sleOSPFProcExtLSDBLimit"),
        ("SLE-OSPF-MIB", "sleOSPFProcExitOverFlowInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAdminDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcExternalDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcIntraAreaDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcInterAreaDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginType"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginRouteMap"),
        ("SLE-OSPF-MIB", "sleOSPFProcLogNeighborChange"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassiveIfAll"),
        ("SLE-OSPF-MIB", "sleOSPFProcBfdIFAll"),
        ("SLE-OSPF-MIB", "sleOSPFProcEfmIFAll"),
        ("SLE-OSPF-MIB", "sleOSPFProcCapabilityRestart"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlRouterID"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlSPFDelayTime"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlSPFHoldTime"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlAutoCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlAbrType"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlSnmpNotification"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlDefaultMetricConfig"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlDefaultMetricValue"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlMaxArea"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlMaxConcurDD"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlComprfc1583"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlCapabilityOpaque"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlLSDBOverflowType"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlLSDBOverflowLimit"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlExtLSDBLimit"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlExitOverFlowInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlAdminDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlExtDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlIntraAreaDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlInterAreaDistance"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlDefOriginType"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlDefOriginMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlDefOriginMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlDefOriginRouteMap"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlLogNeighborChange"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlPassiveIFAll"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlBfdIFAll"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlEfmIFAll"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlCapabilityRestart"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryIPAddress"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryAdvertiseFlag"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlIPAddress"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlAdvertiseFlag"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListOutFilterType"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListAccessName"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlOutFilterType"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlAccessName"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborPriority"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborPollInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlPriority"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlPollInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfName"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlName"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostAreaCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlAreaCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistRouteMapName"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistSubnets"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlRouteMapName"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlSubnets"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaDefaultCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaAuthenType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAInName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAOutName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPInName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPOutName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaShortcutType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaSpfRuns"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaLsaCount"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaLsaCheckSum"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaSummary"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaTransRole"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaNoRedist"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaDefOriginate"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaDefMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaDefMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlDefaultCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlAuthenType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlFAInName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlFAOutName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlFPInName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlFPOutName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlShortcutType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlSummary"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlNssaTransRole"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlNssaNoRedist"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlNssaDefOriginate"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlNssaDefMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlNssaDefMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeAdverType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlAdverType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkAuthenType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkAuthenKey"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkDeadInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkHelloInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkRetranInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkTransDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlAuthenType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlAuthenKey"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlDeadInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlHelloInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlRetranInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTransInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyVal"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlKeyID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlKeyVal"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSFPIfEnabled"),
        ("SLE-OSPF-MIB", "sleOSPFIfNetworkType"),
        ("SLE-OSPF-MIB", "sleOSFPIfMTU"),
        ("SLE-OSPF-MIB", "sleOSFPIfBFD"),
        ("SLE-OSPF-MIB", "sleOSFPIfEFM"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlEnabled"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlNetworkType"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlMTU"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlBFD"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlEFM"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfCost"),
        ("SLE-OSPF-MIB", "sleOSPFIfTransmitDelay"),
        ("SLE-OSPF-MIB", "sleOSPFIfPriority"),
        ("SLE-OSPF-MIB", "sleOSPFIfHelloInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfDeadInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfRetransInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuth"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthType"),
        ("SLE-OSPF-MIB", "sleOSPFIfDataFilterOut"),
        ("SLE-OSPF-MIB", "sleOSPFIfMTUIgnore"),
        ("SLE-OSPF-MIB", "sleOSPFIfResync"),
        ("SLE-OSPF-MIB", "sleOSPFIfResyncTimeout"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeyFirst"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeyFirstAct"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeySecond"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeySecondAct"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlCost"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTransmitDelay"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlPriority"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlHelloInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlDeadInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlRetransInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlAuth"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlAuthType"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlDataFilterOut"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlMTUIgnore"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlResync"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlResyncTimeout"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlAuthKeyFirst"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlAuthKeyFirstAct"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlAuthKeySecond"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlAuthKeySecondAct"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyID"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyVal"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyAct"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlStatus"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlTimer"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlKeyID"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlKeyVal"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlKeyAct"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusUpState"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusProcID"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusRouterID"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusNetworkType"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusCost"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusTransmitDelay"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusState"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusPriorityUse"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusPriority"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusDRRouterUse"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusDRRouterID"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusDRIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusBDRRouterUse"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusBDRRouterID"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusBDRIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusHelloInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusDeadInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusRetransInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusWaitInterval"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusNeighborCount"),
        ("SLE-OSPF-MIB", "sleOSPFIfCryptSeqNum"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusRcvHello"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusSendHello"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusRcvDD"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusSendDD"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusRcvLSReq"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusSendLSReq"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusRcvLSUpd"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusSendLSUpd"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusRcvLSAck"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusSendLSAck"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusDiscarded"),
        ("SLE-OSPF-MIB", "sleOSPFLsaType"),
        ("SLE-OSPF-MIB", "sleOSPFLsaAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFLsaLinkID"),
        ("SLE-OSPF-MIB", "sleOSPFLsaAdvRouter"),
        ("SLE-OSPF-MIB", "sleOSPFLsaAge"),
        ("SLE-OSPF-MIB", "sleOSPFLsaSequence"),
        ("SLE-OSPF-MIB", "sleOSPFNeighborIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFNeighborID"),
        ("SLE-OSPF-MIB", "sleOSPFNeighborPriority"),
        ("SLE-OSPF-MIB", "sleOSPFNeighborState"),
        ("SLE-OSPF-MIB", "sleOSPFNeighborIfName"),
        ("SLE-OSPF-MIB", "sleOSPFRoutePathType"),
        ("SLE-OSPF-MIB", "sleOSPFRouteNexthop"),
        ("SLE-OSPF-MIB", "sleOSPFRouteNbrID"),
        ("SLE-OSPF-MIB", "sleOSPFRoutePathTypeCode"),
        ("SLE-OSPF-MIB", "sleOSPFRouteMetric"),
        ("SLE-OSPF-MIB", "sleOSPFRouteIfName"),
        ("SLE-OSPF-MIB", "sleOSPFRouteAreaUse"),
        ("SLE-OSPF-MIB", "sleOSPFSnmpNotification"),
        ("SLE-OSPF-MIB", "sleOSPFControlSnmpNotification"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFStartDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFMinDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFMaxDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAStartDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAMinDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAMaxDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAArrivalDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlSPFStartDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlSPFMinDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlSPFMaxDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlLSAStartDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlLSAMinDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlLSAMaxDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlLSAArrivalDelay"),
        ("SLE-OSPF-MIB", "sleOSPFRouteAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcVRIndex"),
        ("SLE-OSPF-MIB", "sleOSPFProcVRFName"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlVRIndex"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlVRFName"),
        ("SLE-OSPF-MIB", "sleOSPFIfStatusMtu"))
)
if mibBuilder.loadTexts:
    sleOspfGroup.setStatus("current")


# Notification objects

sleOSPFRestartPeriodChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 3, 1)
)
sleOSPFRestartPeriodChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFRestartPeriod"))
)
if mibBuilder.loadTexts:
    sleOSPFRestartPeriodChanged.setStatus(
        "current"
    )

sleOSPFRestartHelperProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 3, 2)
)
sleOSPFRestartHelperProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFRestartHelperPolicy"),
        ("SLE-OSPF-MIB", "sleOSPFRestartHelperPeriod"))
)
if mibBuilder.loadTexts:
    sleOSPFRestartHelperProfileChanged.setStatus(
        "current"
    )

sleOSPFGracefulRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 3, 3)
)
sleOSPFGracefulRestarted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFControlRestartPeriod"))
)
if mibBuilder.loadTexts:
    sleOSPFGracefulRestarted.setStatus(
        "current"
    )

sleOSPFSnmpNotificationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 1, 3, 4)
)
sleOSPFSnmpNotificationChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFControlSnmpNotification"))
)
if mibBuilder.loadTexts:
    sleOSPFSnmpNotificationChanged.setStatus(
        "current"
    )

sleOSPFProcCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 1)
)
sleOSPFProcCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcVRIndex"),
        ("SLE-OSPF-MIB", "sleOSPFProcVRFName"))
)
if mibBuilder.loadTexts:
    sleOSPFProcCreated.setStatus(
        "current"
    )

sleOSPFProcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 2)
)
sleOSPFProcDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlVRIndex"))
)
if mibBuilder.loadTexts:
    sleOSPFProcDeleted.setStatus(
        "current"
    )

sleOSPFRouterIDCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 3)
)
sleOSPFRouterIDCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcRouterID"))
)
if mibBuilder.loadTexts:
    sleOSPFRouterIDCreated.setStatus(
        "current"
    )

sleOSPFRouterIDDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 4)
)
sleOSPFRouterIDDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlRouterID"))
)
if mibBuilder.loadTexts:
    sleOSPFRouterIDDeleted.setStatus(
        "current"
    )

sleOSPFProcSPFTimerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 5)
)
sleOSPFProcSPFTimerChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFDelayTime"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFHoldTime"))
)
if mibBuilder.loadTexts:
    sleOSPFProcSPFTimerChanged.setStatus(
        "current"
    )

sleOSPFProcAutoCostChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 6)
)
sleOSPFProcAutoCostChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAutoCost"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAutoCostChanged.setStatus(
        "current"
    )

sleOSPFProcAbrTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 7)
)
sleOSPFProcAbrTypeChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAbrType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAbrTypeChanged.setStatus(
        "current"
    )

sleOSPFProcSnmpNotificationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 8)
)
sleOSPFProcSnmpNotificationChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSnmpNotification"))
)
if mibBuilder.loadTexts:
    sleOSPFProcSnmpNotificationChanged.setStatus(
        "current"
    )

sleOSPFProcDefaultMetricProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 9)
)
sleOSPFProcDefaultMetricProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultMetricConfig"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultMetricValue"))
)
if mibBuilder.loadTexts:
    sleOSPFProcDefaultMetricProfileChanged.setStatus(
        "current"
    )

sleOSPFProcMaxAreaChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 10)
)
sleOSPFProcMaxAreaChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcMaxArea"))
)
if mibBuilder.loadTexts:
    sleOSPFProcMaxAreaChanged.setStatus(
        "current"
    )

sleOSPFProcMaxConcurDDChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 11)
)
sleOSPFProcMaxConcurDDChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcMaxConcurrentDD"))
)
if mibBuilder.loadTexts:
    sleOSPFProcMaxConcurDDChanged.setStatus(
        "current"
    )

sleOSPFProcComrfc1853Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 12)
)
sleOSPFProcComrfc1853Changed.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcCompatiblerfc1583"))
)
if mibBuilder.loadTexts:
    sleOSPFProcComrfc1853Changed.setStatus(
        "current"
    )

sleOSPFProcCapOpaqueChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 13)
)
sleOSPFProcCapOpaqueChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcCapabilityOpaque"))
)
if mibBuilder.loadTexts:
    sleOSPFProcCapOpaqueChanged.setStatus(
        "current"
    )

sleOSPFProcLSDBOverflowProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 14)
)
sleOSPFProcLSDBOverflowProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSDBOverflowType"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSDBOverflowLimit"))
)
if mibBuilder.loadTexts:
    sleOSPFProcLSDBOverflowProfileChanged.setStatus(
        "current"
    )

sleOSPFProcExtOverflowProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 15)
)
sleOSPFProcExtOverflowProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcExtLSDBLimit"),
        ("SLE-OSPF-MIB", "sleOSPFProcExitOverFlowInterval"))
)
if mibBuilder.loadTexts:
    sleOSPFProcExtOverflowProfileChanged.setStatus(
        "current"
    )

sleOSPFProcAdminDistanceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 16)
)
sleOSPFProcAdminDistanceChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAdminDistance"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAdminDistanceChanged.setStatus(
        "current"
    )

sleOSPFProcExtDistanceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 17)
)
sleOSPFProcExtDistanceChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcExternalDistance"))
)
if mibBuilder.loadTexts:
    sleOSPFProcExtDistanceChanged.setStatus(
        "current"
    )

sleOSPFProcIntraDistanceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 18)
)
sleOSPFProcIntraDistanceChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcIntraAreaDistance"))
)
if mibBuilder.loadTexts:
    sleOSPFProcIntraDistanceChanged.setStatus(
        "current"
    )

sleOSPFProcInterDistanceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 19)
)
sleOSPFProcInterDistanceChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcInterAreaDistance"))
)
if mibBuilder.loadTexts:
    sleOSPFProcInterDistanceChanged.setStatus(
        "current"
    )

sleOSPFProcDefaultOriginTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 20)
)
sleOSPFProcDefaultOriginTypeChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginTypeChanged.setStatus(
        "current"
    )

sleOSPFProcDefaultOriginMetricTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 21)
)
sleOSPFProcDefaultOriginMetricTypeChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginMetricType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginMetricTypeChanged.setStatus(
        "current"
    )

sleOSPFProcDefaultOriginMetricChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 22)
)
sleOSPFProcDefaultOriginMetricChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginMetric"))
)
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginMetricChanged.setStatus(
        "current"
    )

sleOSPFProcDefaultOriginRouteMapChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 23)
)
sleOSPFProcDefaultOriginRouteMapChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginRouteMap"))
)
if mibBuilder.loadTexts:
    sleOSPFProcDefaultOriginRouteMapChanged.setStatus(
        "current"
    )

sleOSPFProcLogNeighborChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 24)
)
sleOSPFProcLogNeighborChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcLogNeighborChange"))
)
if mibBuilder.loadTexts:
    sleOSPFProcLogNeighborChanged.setStatus(
        "current"
    )

sleOSPFProcPassiveIFAllChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 25)
)
sleOSPFProcPassiveIFAllChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassiveIfAll"))
)
if mibBuilder.loadTexts:
    sleOSPFProcPassiveIFAllChanged.setStatus(
        "current"
    )

sleOSPFProcBfdIFAllChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 26)
)
sleOSPFProcBfdIFAllChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcBfdIFAll"))
)
if mibBuilder.loadTexts:
    sleOSPFProcBfdIFAllChanged.setStatus(
        "current"
    )

sleOSPFProcEfmIFAllChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 27)
)
sleOSPFProcEfmIFAllChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcEfmIFAll"))
)
if mibBuilder.loadTexts:
    sleOSPFProcEfmIFAllChanged.setStatus(
        "current"
    )

sleOSPFProcCapRestartChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 28)
)
sleOSPFProcCapRestartChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcCapabilityRestart"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"))
)
if mibBuilder.loadTexts:
    sleOSPFProcCapRestartChanged.setStatus(
        "current"
    )

sleOSPFProcCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 29)
)
sleOSPFProcCleared.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"))
)
if mibBuilder.loadTexts:
    sleOSPFProcCleared.setStatus(
        "current"
    )

sleOSPFProcSPFThrottleTimerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 30)
)
sleOSPFProcSPFThrottleTimerChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFStartDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFMinDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFMaxDelay"))
)
if mibBuilder.loadTexts:
    sleOSPFProcSPFThrottleTimerChanged.setStatus(
        "current"
    )

sleOSPFProcLSAThrottleTimerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 31)
)
sleOSPFProcLSAThrottleTimerChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAStartDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAMinDelay"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAMaxDelay"))
)
if mibBuilder.loadTexts:
    sleOSPFProcLSAThrottleTimerChanged.setStatus(
        "current"
    )

sleOSPFProcLSAArrivalTimerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 1, 3, 32)
)
sleOSPFProcLSAArrivalTimerChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAArrivalDelay"))
)
if mibBuilder.loadTexts:
    sleOSPFProcLSAArrivalTimerChanged.setStatus(
        "current"
    )

sleOSPFProcNetworkCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 3, 1)
)
sleOSPFProcNetworkCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcNetworkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkAreaID"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNetworkCreated.setStatus(
        "current"
    )

sleOSPFProcNetworkDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 2, 3, 2)
)
sleOSPFProcNetworkDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcNetworkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkControlAreaID"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNetworkDeleted.setStatus(
        "current"
    )

sleOSPFSummaryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 3, 1)
)
sleOSPFSummaryCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcSummaryControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryIPAddress"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    sleOSPFSummaryCreated.setStatus(
        "current"
    )

sleOSPFSummaryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 3, 2)
)
sleOSPFSummaryDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcSummaryControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlIPAddress"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    sleOSPFSummaryDeleted.setStatus(
        "current"
    )

sleOSPFSummaryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 3, 3, 3)
)
sleOSPFSummaryChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcSummaryControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryIPAddress"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcSummaryAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    sleOSPFSummaryChanged.setStatus(
        "current"
    )

sleOSPFDistributeListCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 3, 1)
)
sleOSPFDistributeListCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListOutFilterType"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListAccessName"))
)
if mibBuilder.loadTexts:
    sleOSPFDistributeListCreated.setStatus(
        "current"
    )

sleOSPFDistributeListDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 4, 3, 2)
)
sleOSPFDistributeListDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlOutFilterType"),
        ("SLE-OSPF-MIB", "sleOSPFProcDistributeListControlAccessName"))
)
if mibBuilder.loadTexts:
    sleOSPFDistributeListDeleted.setStatus(
        "current"
    )

sleOSPFProcNeighborCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 3, 1)
)
sleOSPFProcNeighborCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcNeighborControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborPollInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborPriority"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNeighborCreated.setStatus(
        "current"
    )

sleOSPFProcNeighborDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 3, 2)
)
sleOSPFProcNeighborDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcNeighborControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlIPAddr"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNeighborDeleted.setStatus(
        "current"
    )

sleOSPFProcNeighborChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 5, 3, 3)
)
sleOSPFProcNeighborChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcNeighborControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborCost"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborPollInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborPriority"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNeighborChanged.setStatus(
        "current"
    )

sleOSPFPassInterfaceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 3, 1)
)
sleOSPFPassInterfaceCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcPassIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfName"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfAddr"))
)
if mibBuilder.loadTexts:
    sleOSPFPassInterfaceCreated.setStatus(
        "current"
    )

sleOSPFPassInterfaceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 6, 3, 2)
)
sleOSPFPassInterfaceDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcPassIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlName"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassIfControlIPAddr"))
)
if mibBuilder.loadTexts:
    sleOSPFPassInterfaceDeleted.setStatus(
        "current"
    )

sleOSPFProcHostCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 3, 1)
)
sleOSPFProcHostCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcHostControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostAreaCost"))
)
if mibBuilder.loadTexts:
    sleOSPFProcHostCreated.setStatus(
        "current"
    )

sleOSPFProcHostDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 3, 2)
)
sleOSPFProcHostDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcHostControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlAreaID"))
)
if mibBuilder.loadTexts:
    sleOSPFProcHostDeleted.setStatus(
        "current"
    )

sleOSPFProcHostCostChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 7, 3, 3)
)
sleOSPFProcHostCostChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcHostControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostIPAddr"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostAreaCost"))
)
if mibBuilder.loadTexts:
    sleOSPFProcHostCostChanged.setStatus(
        "current"
    )

sleOSPFProcRedistCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 3, 1)
)
sleOSPFProcRedistCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcRedistControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistSubnets"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistRouteMapName"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistTag"))
)
if mibBuilder.loadTexts:
    sleOSPFProcRedistCreated.setStatus(
        "current"
    )

sleOSPFProcRedistDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 3, 2)
)
sleOSPFProcRedistDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcRedistControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlRouteMapName"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlSubnets"))
)
if mibBuilder.loadTexts:
    sleOSPFProcRedistDeleted.setStatus(
        "current"
    )

sleOSPFProcRedistChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 8, 3, 3)
)
sleOSPFProcRedistChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcRedistControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistMetric"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistRouteMapName"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistTag"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistControlSubnets"))
)
if mibBuilder.loadTexts:
    sleOSPFProcRedistChanged.setStatus(
        "current"
    )

sleOSPFProcGeneralAreaCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 1)
)
sleOSPFProcGeneralAreaCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaAuthenType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAInName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAOutName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPInName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPOutName"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaShortcutType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcGeneralAreaCreated.setStatus(
        "current"
    )

sleOSPFProcStubNssaAreaCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 2)
)
sleOSPFProcStubNssaAreaCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcStubNssaAreaCreated.setStatus(
        "current"
    )

sleOSPFProcAreaDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 3)
)
sleOSPFProcAreaDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaDeleted.setStatus(
        "current"
    )

sleOSPFProcAreaDefaultCostChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 4)
)
sleOSPFProcAreaDefaultCostChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaDefaultCost"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaDefaultCostChanged.setStatus(
        "current"
    )

sleOSPFProcAreaAuthenTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 5)
)
sleOSPFProcAreaAuthenTypeChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaAuthenType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaAuthenTypeChanged.setStatus(
        "current"
    )

sleOSPFProcAreaFAInNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 6)
)
sleOSPFProcAreaFAInNameChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAInName"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaFAInNameChanged.setStatus(
        "current"
    )

sleOSPFProcAreaFAOutNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 7)
)
sleOSPFProcAreaFAOutNameChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAOutName"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaFAOutNameChanged.setStatus(
        "current"
    )

sleOSPFProcAreaFPInNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 8)
)
sleOSPFProcAreaFPInNameChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPInName"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaFPInNameChanged.setStatus(
        "current"
    )

sleOSPFProcAreaFPOutNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 9)
)
sleOSPFProcAreaFPOutNameChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPOutName"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaFPOutNameChanged.setStatus(
        "current"
    )

sleOSPFProcAreaShortcutTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 10)
)
sleOSPFProcAreaShortcutTypeChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaShortcutType"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaShortcutTypeChanged.setStatus(
        "current"
    )

sleOSPFProcAreaSummaryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 11)
)
sleOSPFProcAreaSummaryChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaSummary"))
)
if mibBuilder.loadTexts:
    sleOSPFProcAreaSummaryChanged.setStatus(
        "current"
    )

sleOSPFProcNssaAreaTransRoleChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 12)
)
sleOSPFProcNssaAreaTransRoleChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaTransRole"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNssaAreaTransRoleChanged.setStatus(
        "current"
    )

sleOSPFProcNssaAreaTransNoRedistChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 13)
)
sleOSPFProcNssaAreaTransNoRedistChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaNoRedist"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNssaAreaTransNoRedistChanged.setStatus(
        "current"
    )

sleOSPFProcNssaAreaDefProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 1, 3, 14)
)
sleOSPFProcNssaAreaDefProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaDefOriginate"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaDefMetricType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaNssaDefMetric"))
)
if mibBuilder.loadTexts:
    sleOSPFProcNssaAreaDefProfileChanged.setStatus(
        "current"
    )

sleOSPFAreaRangeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 3, 1)
)
sleOSPFAreaRangeCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeAdverType"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaRangeCreated.setStatus(
        "current"
    )

sleOSPFAreaRangeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 3, 2)
)
sleOSPFAreaRangeDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlAdverType"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaRangeDeleted.setStatus(
        "current"
    )

sleOSPFAreaRangeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 2, 3, 3)
)
sleOSPFAreaRangeChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeIPMask"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaRangeAdverType"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaRangeChanged.setStatus(
        "current"
    )

sleOSPFAreaVlinkCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 3, 1)
)
sleOSPFAreaVlinkCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkAuthenType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkAuthenKey"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkDeadInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkHelloInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkRetranInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkTransInterval"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaVlinkCreated.setStatus(
        "current"
    )

sleOSPFAreaVLinkDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 3, 2)
)
sleOSPFAreaVLinkDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlControlID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlIP"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaVLinkDeleted.setStatus(
        "current"
    )

sleOSPFAreaVLinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 1, 3, 3)
)
sleOSPFAreaVLinkChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkAuthenType"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkAuthenKey"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkDeadInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkHelloInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkRetranInterval"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkTransInterval"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaVLinkChanged.setStatus(
        "current"
    )

sleOSPFAreaVlinkMsgKeyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 3, 1)
)
sleOSPFAreaVlinkMsgKeyCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyVal"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaVlinkMsgKeyCreated.setStatus(
        "current"
    )

sleOSPFAreaVLinkMsgKeyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 2, 9, 3, 2, 3, 2)
)
sleOSPFAreaVLinkMsgKeyDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFProcID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaID"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkIP"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaVlinkMsgKeyControlKeyID"))
)
if mibBuilder.loadTexts:
    sleOSPFAreaVLinkMsgKeyDeleted.setStatus(
        "current"
    )

sleOSPFIfEnableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 3, 1)
)
sleOSPFIfEnableChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSFPIfEnabled"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"))
)
if mibBuilder.loadTexts:
    sleOSPFIfEnableChanged.setStatus(
        "current"
    )

sleOSPFIfNetworkTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 3, 2)
)
sleOSPFIfNetworkTypeChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfNetworkType"))
)
if mibBuilder.loadTexts:
    sleOSPFIfNetworkTypeChanged.setStatus(
        "current"
    )

sleOSPFIfMTUChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 3, 3)
)
sleOSPFIfMTUChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSFPIfMTU"))
)
if mibBuilder.loadTexts:
    sleOSPFIfMTUChanged.setStatus(
        "current"
    )

sleOSPFIfBFDChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 3, 4)
)
sleOSPFIfBFDChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSFPIfBFD"))
)
if mibBuilder.loadTexts:
    sleOSPFIfBFDChanged.setStatus(
        "current"
    )

sleOSPFIfEFMChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 1, 3, 5)
)
sleOSPFIfEFMChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSFPIfEFM"))
)
if mibBuilder.loadTexts:
    sleOSPFIfEFMChanged.setStatus(
        "current"
    )

sleOSPFIfCostChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 1)
)
sleOSPFIfCostChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfCost"))
)
if mibBuilder.loadTexts:
    sleOSPFIfCostChanged.setStatus(
        "current"
    )

sleOSPFIfPriorityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 2)
)
sleOSPFIfPriorityChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfPriority"))
)
if mibBuilder.loadTexts:
    sleOSPFIfPriorityChanged.setStatus(
        "current"
    )

sleOSPFIfTransmitDelayChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 3)
)
sleOSPFIfTransmitDelayChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfTransmitDelay"))
)
if mibBuilder.loadTexts:
    sleOSPFIfTransmitDelayChanged.setStatus(
        "current"
    )

sleOSPFIfHelloIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 4)
)
sleOSPFIfHelloIntervalChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfHelloInterval"))
)
if mibBuilder.loadTexts:
    sleOSPFIfHelloIntervalChanged.setStatus(
        "current"
    )

sleOSPFIfDeadIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 5)
)
sleOSPFIfDeadIntervalChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfDeadInterval"))
)
if mibBuilder.loadTexts:
    sleOSPFIfDeadIntervalChanged.setStatus(
        "current"
    )

sleOSPFIfRetransIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 6)
)
sleOSPFIfRetransIntervalChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfRetransInterval"))
)
if mibBuilder.loadTexts:
    sleOSPFIfRetransIntervalChanged.setStatus(
        "current"
    )

sleOSPFIfAuthProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 7)
)
sleOSPFIfAuthProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuth"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthType"))
)
if mibBuilder.loadTexts:
    sleOSPFIfAuthProfileChanged.setStatus(
        "current"
    )

sleOSPFIfDatafilterOutChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 8)
)
sleOSPFIfDatafilterOutChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfDataFilterOut"))
)
if mibBuilder.loadTexts:
    sleOSPFIfDatafilterOutChanged.setStatus(
        "current"
    )

sleOSPFIfMTUIgnoreChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 9)
)
sleOSPFIfMTUIgnoreChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfMTUIgnore"))
)
if mibBuilder.loadTexts:
    sleOSPFIfMTUIgnoreChanged.setStatus(
        "current"
    )

sleOSPFIfResyncProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 10)
)
sleOSPFIfResyncProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfResync"),
        ("SLE-OSPF-MIB", "sleOSPFIfResyncTimeout"))
)
if mibBuilder.loadTexts:
    sleOSPFIfResyncProfileChanged.setStatus(
        "current"
    )

sleOSPFIfAuthKeyFirstProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 11)
)
sleOSPFIfAuthKeyFirstProfileChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeyFirst"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeyFirstAct"))
)
if mibBuilder.loadTexts:
    sleOSPFIfAuthKeyFirstProfileChanged.setStatus(
        "current"
    )

sleOSPFIfAuthKeyProfileSecondChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 2, 3, 12)
)
sleOSPFIfAuthKeyProfileSecondChanged.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeySecond"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeySecondAct"))
)
if mibBuilder.loadTexts:
    sleOSPFIfAuthKeyProfileSecondChanged.setStatus(
        "current"
    )

sleOSPFIfMsgKeyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 3, 1)
)
sleOSPFIfMsgKeyCreated.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyID"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyVal"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyAct"))
)
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyCreated.setStatus(
        "current"
    )

sleOSPFIfMsgKeyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 3, 3, 3, 2)
)
sleOSPFIfMsgKeyDeleted.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFIfInfoControlRequest"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlTimeStamp"),
        ("SLE-OSPF-MIB", "sleOSPFIfInfoControlReqResult"),
        ("SLE-OSPF-MIB", "sleOSPFIfIndex"),
        ("SLE-OSPF-MIB", "sleOSPFIfIpAddr"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyControlKeyID"))
)
if mibBuilder.loadTexts:
    sleOSPFIfMsgKeyDeleted.setStatus(
        "current"
    )


# Notifications groups

sleOspfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 51, 8)
)
sleOspfNotificationGroup.setObjects(
      *(("SLE-OSPF-MIB", "sleOSPFRestartPeriodChanged"),
        ("SLE-OSPF-MIB", "sleOSPFRestartHelperProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFGracefulRestarted"),
        ("SLE-OSPF-MIB", "sleOSPFProcCreated"),
        ("SLE-OSPF-MIB", "sleOSPFProcDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFRouterIDCreated"),
        ("SLE-OSPF-MIB", "sleOSPFRouterIDDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFTimerChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAutoCostChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAbrTypeChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcSnmpNotificationChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultMetricProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcMaxAreaChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcMaxConcurDDChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcComrfc1853Changed"),
        ("SLE-OSPF-MIB", "sleOSPFProcCapOpaqueChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSDBOverflowProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcExtOverflowProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAdminDistanceChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcExtDistanceChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcIntraDistanceChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcInterDistanceChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginTypeChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginMetricTypeChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginMetricChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcDefaultOriginRouteMapChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcLogNeighborChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcPassiveIFAllChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcBfdIFAllChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcEfmIFAllChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcCapRestartChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcCleared"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkCreated"),
        ("SLE-OSPF-MIB", "sleOSPFProcNetworkDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFSummaryCreated"),
        ("SLE-OSPF-MIB", "sleOSPFSummaryDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFSummaryChanged"),
        ("SLE-OSPF-MIB", "sleOSPFDistributeListCreated"),
        ("SLE-OSPF-MIB", "sleOSPFDistributeListDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborCreated"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFProcNeighborChanged"),
        ("SLE-OSPF-MIB", "sleOSPFPassInterfaceCreated"),
        ("SLE-OSPF-MIB", "sleOSPFPassInterfaceDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostCreated"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFProcHostCostChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistCreated"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFProcRedistChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcGeneralAreaCreated"),
        ("SLE-OSPF-MIB", "sleOSPFProcStubNssaAreaCreated"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaDefaultCostChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaAuthenTypeChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAInNameChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFAOutNameChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPInNameChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaFPOutNameChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaShortcutTypeChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcAreaSummaryChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcNssaAreaTransRoleChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcNssaAreaTransNoRedistChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcNssaAreaDefProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFAreaRangeCreated"),
        ("SLE-OSPF-MIB", "sleOSPFAreaRangeDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFAreaRangeChanged"),
        ("SLE-OSPF-MIB", "sleOSPFAreaVlinkCreated"),
        ("SLE-OSPF-MIB", "sleOSPFAreaVLinkDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFAreaVLinkChanged"),
        ("SLE-OSPF-MIB", "sleOSPFAreaVlinkMsgKeyCreated"),
        ("SLE-OSPF-MIB", "sleOSPFAreaVLinkMsgKeyDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFIfEnableChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfNetworkTypeChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfMTUChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfBFDChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfEFMChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfCostChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfPriorityChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfTransmitDelayChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfHelloIntervalChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfDeadIntervalChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfRetransIntervalChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfDatafilterOutChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfMTUIgnoreChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfResyncProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeyFirstProfileChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfAuthKeyProfileSecondChanged"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyCreated"),
        ("SLE-OSPF-MIB", "sleOSPFIfMsgKeyDeleted"),
        ("SLE-OSPF-MIB", "sleOSPFSnmpNotificationChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcSPFThrottleTimerChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAThrottleTimerChanged"),
        ("SLE-OSPF-MIB", "sleOSPFProcLSAArrivalTimerChanged"))
)
if mibBuilder.loadTexts:
    sleOspfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-OSPF-MIB",
    **{"sleOSPF": sleOSPF,
       "sleOSPFBase": sleOSPFBase,
       "sleOSPFBaseInfo": sleOSPFBaseInfo,
       "sleOSPFRestartPeriod": sleOSPFRestartPeriod,
       "sleOSPFRestartHelperPolicy": sleOSPFRestartHelperPolicy,
       "sleOSPFRestartHelperPeriod": sleOSPFRestartHelperPeriod,
       "sleOSPFSnmpNotification": sleOSPFSnmpNotification,
       "sleOSPFBaseControl": sleOSPFBaseControl,
       "sleOSPFControlRequest": sleOSPFControlRequest,
       "sleOSPFControlStatus": sleOSPFControlStatus,
       "sleOSPFControlTimer": sleOSPFControlTimer,
       "sleOSPFControlTimeStamp": sleOSPFControlTimeStamp,
       "sleOSPFControlReqResult": sleOSPFControlReqResult,
       "sleOSPFControlRestartPeriod": sleOSPFControlRestartPeriod,
       "sleOSPFControlRestartHelperPolicy": sleOSPFControlRestartHelperPolicy,
       "sleOSPFControlRestartHelperPeriod": sleOSPFControlRestartHelperPeriod,
       "sleOSPFControlSnmpNotification": sleOSPFControlSnmpNotification,
       "sleOSPFBaseNotification": sleOSPFBaseNotification,
       "sleOSPFRestartPeriodChanged": sleOSPFRestartPeriodChanged,
       "sleOSPFRestartHelperProfileChanged": sleOSPFRestartHelperProfileChanged,
       "sleOSPFGracefulRestarted": sleOSPFGracefulRestarted,
       "sleOSPFSnmpNotificationChanged": sleOSPFSnmpNotificationChanged,
       "sleOSPFProc": sleOSPFProc,
       "sleOSPFProcInfo": sleOSPFProcInfo,
       "sleOSPFProcInfoTable": sleOSPFProcInfoTable,
       "sleOSPFProcInfoEntry": sleOSPFProcInfoEntry,
       "sleOSPFProcID": sleOSPFProcID,
       "sleOSPFProcRouterID": sleOSPFProcRouterID,
       "sleOSPFProcSPFDelayTime": sleOSPFProcSPFDelayTime,
       "sleOSPFProcSPFHoldTime": sleOSPFProcSPFHoldTime,
       "sleOSPFProcAutoCost": sleOSPFProcAutoCost,
       "sleOSPFProcAbrType": sleOSPFProcAbrType,
       "sleOSPFProcSnmpNotification": sleOSPFProcSnmpNotification,
       "sleOSPFProcDefaultMetricConfig": sleOSPFProcDefaultMetricConfig,
       "sleOSPFProcDefaultMetricValue": sleOSPFProcDefaultMetricValue,
       "sleOSPFProcMaxArea": sleOSPFProcMaxArea,
       "sleOSPFProcMaxConcurrentDD": sleOSPFProcMaxConcurrentDD,
       "sleOSPFProcCompatiblerfc1583": sleOSPFProcCompatiblerfc1583,
       "sleOSPFProcCapabilityOpaque": sleOSPFProcCapabilityOpaque,
       "sleOSPFProcLSDBOverflowType": sleOSPFProcLSDBOverflowType,
       "sleOSPFProcLSDBOverflowLimit": sleOSPFProcLSDBOverflowLimit,
       "sleOSPFProcExtLSDBLimit": sleOSPFProcExtLSDBLimit,
       "sleOSPFProcExitOverFlowInterval": sleOSPFProcExitOverFlowInterval,
       "sleOSPFProcAdminDistance": sleOSPFProcAdminDistance,
       "sleOSPFProcExternalDistance": sleOSPFProcExternalDistance,
       "sleOSPFProcIntraAreaDistance": sleOSPFProcIntraAreaDistance,
       "sleOSPFProcInterAreaDistance": sleOSPFProcInterAreaDistance,
       "sleOSPFProcDefaultOriginType": sleOSPFProcDefaultOriginType,
       "sleOSPFProcDefaultOriginMetricType": sleOSPFProcDefaultOriginMetricType,
       "sleOSPFProcDefaultOriginMetric": sleOSPFProcDefaultOriginMetric,
       "sleOSPFProcDefaultOriginRouteMap": sleOSPFProcDefaultOriginRouteMap,
       "sleOSPFProcLogNeighborChange": sleOSPFProcLogNeighborChange,
       "sleOSPFProcPassiveIfAll": sleOSPFProcPassiveIfAll,
       "sleOSPFProcBfdIFAll": sleOSPFProcBfdIFAll,
       "sleOSPFProcEfmIFAll": sleOSPFProcEfmIFAll,
       "sleOSPFProcCapabilityRestart": sleOSPFProcCapabilityRestart,
       "sleOSPFProcVRIndex": sleOSPFProcVRIndex,
       "sleOSPFProcVRFName": sleOSPFProcVRFName,
       "sleOSPFProcSPFStartDelay": sleOSPFProcSPFStartDelay,
       "sleOSPFProcSPFMinDelay": sleOSPFProcSPFMinDelay,
       "sleOSPFProcSPFMaxDelay": sleOSPFProcSPFMaxDelay,
       "sleOSPFProcLSAStartDelay": sleOSPFProcLSAStartDelay,
       "sleOSPFProcLSAMinDelay": sleOSPFProcLSAMinDelay,
       "sleOSPFProcLSAMaxDelay": sleOSPFProcLSAMaxDelay,
       "sleOSPFProcLSAArrivalDelay": sleOSPFProcLSAArrivalDelay,
       "sleOSPFProcInfoControl": sleOSPFProcInfoControl,
       "sleOSPFProcControlRequest": sleOSPFProcControlRequest,
       "sleOSPFProcControlStatus": sleOSPFProcControlStatus,
       "sleOSPFProcControlTimer": sleOSPFProcControlTimer,
       "sleOSPFProcControlTimeStamp": sleOSPFProcControlTimeStamp,
       "sleOSPFProcControlReqResult": sleOSPFProcControlReqResult,
       "sleOSPFProcControlID": sleOSPFProcControlID,
       "sleOSPFProcControlRouterID": sleOSPFProcControlRouterID,
       "sleOSPFProcControlSPFDelayTime": sleOSPFProcControlSPFDelayTime,
       "sleOSPFProcControlSPFHoldTime": sleOSPFProcControlSPFHoldTime,
       "sleOSPFProcControlAutoCost": sleOSPFProcControlAutoCost,
       "sleOSPFProcControlAbrType": sleOSPFProcControlAbrType,
       "sleOSPFProcControlSnmpNotification": sleOSPFProcControlSnmpNotification,
       "sleOSPFProcControlDefaultMetricConfig": sleOSPFProcControlDefaultMetricConfig,
       "sleOSPFProcControlDefaultMetricValue": sleOSPFProcControlDefaultMetricValue,
       "sleOSPFProcControlMaxArea": sleOSPFProcControlMaxArea,
       "sleOSPFProcControlMaxConcurDD": sleOSPFProcControlMaxConcurDD,
       "sleOSPFProcControlComprfc1583": sleOSPFProcControlComprfc1583,
       "sleOSPFProcControlCapabilityOpaque": sleOSPFProcControlCapabilityOpaque,
       "sleOSPFProcControlLSDBOverflowType": sleOSPFProcControlLSDBOverflowType,
       "sleOSPFProcControlLSDBOverflowLimit": sleOSPFProcControlLSDBOverflowLimit,
       "sleOSPFProcControlExtLSDBLimit": sleOSPFProcControlExtLSDBLimit,
       "sleOSPFProcControlExitOverFlowInterval": sleOSPFProcControlExitOverFlowInterval,
       "sleOSPFProcControlAdminDistance": sleOSPFProcControlAdminDistance,
       "sleOSPFProcControlExtDistance": sleOSPFProcControlExtDistance,
       "sleOSPFProcControlIntraAreaDistance": sleOSPFProcControlIntraAreaDistance,
       "sleOSPFProcControlInterAreaDistance": sleOSPFProcControlInterAreaDistance,
       "sleOSPFProcControlDefOriginType": sleOSPFProcControlDefOriginType,
       "sleOSPFProcControlDefOriginMetricType": sleOSPFProcControlDefOriginMetricType,
       "sleOSPFProcControlDefOriginMetric": sleOSPFProcControlDefOriginMetric,
       "sleOSPFProcControlDefOriginRouteMap": sleOSPFProcControlDefOriginRouteMap,
       "sleOSPFProcControlLogNeighborChange": sleOSPFProcControlLogNeighborChange,
       "sleOSPFProcControlPassiveIFAll": sleOSPFProcControlPassiveIFAll,
       "sleOSPFProcControlBfdIFAll": sleOSPFProcControlBfdIFAll,
       "sleOSPFProcControlEfmIFAll": sleOSPFProcControlEfmIFAll,
       "sleOSPFProcControlCapabilityRestart": sleOSPFProcControlCapabilityRestart,
       "sleOSPFProcControlVRIndex": sleOSPFProcControlVRIndex,
       "sleOSPFProcControlVRFName": sleOSPFProcControlVRFName,
       "sleOSPFProcControlSPFStartDelay": sleOSPFProcControlSPFStartDelay,
       "sleOSPFProcControlSPFMinDelay": sleOSPFProcControlSPFMinDelay,
       "sleOSPFProcControlSPFMaxDelay": sleOSPFProcControlSPFMaxDelay,
       "sleOSPFProcControlLSAStartDelay": sleOSPFProcControlLSAStartDelay,
       "sleOSPFProcControlLSAMinDelay": sleOSPFProcControlLSAMinDelay,
       "sleOSPFProcControlLSAMaxDelay": sleOSPFProcControlLSAMaxDelay,
       "sleOSPFProcControlLSAArrivalDelay": sleOSPFProcControlLSAArrivalDelay,
       "sleOSPFProcInfoNotification": sleOSPFProcInfoNotification,
       "sleOSPFProcCreated": sleOSPFProcCreated,
       "sleOSPFProcDeleted": sleOSPFProcDeleted,
       "sleOSPFRouterIDCreated": sleOSPFRouterIDCreated,
       "sleOSPFRouterIDDeleted": sleOSPFRouterIDDeleted,
       "sleOSPFProcSPFTimerChanged": sleOSPFProcSPFTimerChanged,
       "sleOSPFProcAutoCostChanged": sleOSPFProcAutoCostChanged,
       "sleOSPFProcAbrTypeChanged": sleOSPFProcAbrTypeChanged,
       "sleOSPFProcSnmpNotificationChanged": sleOSPFProcSnmpNotificationChanged,
       "sleOSPFProcDefaultMetricProfileChanged": sleOSPFProcDefaultMetricProfileChanged,
       "sleOSPFProcMaxAreaChanged": sleOSPFProcMaxAreaChanged,
       "sleOSPFProcMaxConcurDDChanged": sleOSPFProcMaxConcurDDChanged,
       "sleOSPFProcComrfc1853Changed": sleOSPFProcComrfc1853Changed,
       "sleOSPFProcCapOpaqueChanged": sleOSPFProcCapOpaqueChanged,
       "sleOSPFProcLSDBOverflowProfileChanged": sleOSPFProcLSDBOverflowProfileChanged,
       "sleOSPFProcExtOverflowProfileChanged": sleOSPFProcExtOverflowProfileChanged,
       "sleOSPFProcAdminDistanceChanged": sleOSPFProcAdminDistanceChanged,
       "sleOSPFProcExtDistanceChanged": sleOSPFProcExtDistanceChanged,
       "sleOSPFProcIntraDistanceChanged": sleOSPFProcIntraDistanceChanged,
       "sleOSPFProcInterDistanceChanged": sleOSPFProcInterDistanceChanged,
       "sleOSPFProcDefaultOriginTypeChanged": sleOSPFProcDefaultOriginTypeChanged,
       "sleOSPFProcDefaultOriginMetricTypeChanged": sleOSPFProcDefaultOriginMetricTypeChanged,
       "sleOSPFProcDefaultOriginMetricChanged": sleOSPFProcDefaultOriginMetricChanged,
       "sleOSPFProcDefaultOriginRouteMapChanged": sleOSPFProcDefaultOriginRouteMapChanged,
       "sleOSPFProcLogNeighborChanged": sleOSPFProcLogNeighborChanged,
       "sleOSPFProcPassiveIFAllChanged": sleOSPFProcPassiveIFAllChanged,
       "sleOSPFProcBfdIFAllChanged": sleOSPFProcBfdIFAllChanged,
       "sleOSPFProcEfmIFAllChanged": sleOSPFProcEfmIFAllChanged,
       "sleOSPFProcCapRestartChanged": sleOSPFProcCapRestartChanged,
       "sleOSPFProcCleared": sleOSPFProcCleared,
       "sleOSPFProcSPFThrottleTimerChanged": sleOSPFProcSPFThrottleTimerChanged,
       "sleOSPFProcLSAThrottleTimerChanged": sleOSPFProcLSAThrottleTimerChanged,
       "sleOSPFProcLSAArrivalTimerChanged": sleOSPFProcLSAArrivalTimerChanged,
       "sleOSPFProcNetwork": sleOSPFProcNetwork,
       "sleOSPFProcNetworkTable": sleOSPFProcNetworkTable,
       "sleOSPFProcNetworkEntry": sleOSPFProcNetworkEntry,
       "sleOSPFProcNetworkIP": sleOSPFProcNetworkIP,
       "sleOSPFProcNetworkIPMask": sleOSPFProcNetworkIPMask,
       "sleOSPFProcNetworkAreaID": sleOSPFProcNetworkAreaID,
       "sleOSPFProcNetworkControl": sleOSPFProcNetworkControl,
       "sleOSPFProcNetworkControlRequest": sleOSPFProcNetworkControlRequest,
       "sleOSPFProcNetworkControlStatus": sleOSPFProcNetworkControlStatus,
       "sleOSPFProcNetworkControlTimer": sleOSPFProcNetworkControlTimer,
       "sleOSPFProcNetworkControlTimeStamp": sleOSPFProcNetworkControlTimeStamp,
       "sleOSPFProcNetworkControlReqResult": sleOSPFProcNetworkControlReqResult,
       "sleOSPFProcNetworkControlProcID": sleOSPFProcNetworkControlProcID,
       "sleOSPFProcNetworkControlIP": sleOSPFProcNetworkControlIP,
       "sleOSPFProcNetworkControlIPMask": sleOSPFProcNetworkControlIPMask,
       "sleOSPFProcNetworkControlAreaID": sleOSPFProcNetworkControlAreaID,
       "sleOSPFProcNetworkNotification": sleOSPFProcNetworkNotification,
       "sleOSPFProcNetworkCreated": sleOSPFProcNetworkCreated,
       "sleOSPFProcNetworkDeleted": sleOSPFProcNetworkDeleted,
       "sleOSPFProcSummary": sleOSPFProcSummary,
       "sleOSPFProcSummaryTable": sleOSPFProcSummaryTable,
       "sleOSPFProcSummaryEntry": sleOSPFProcSummaryEntry,
       "sleOSPFProcSummaryIPAddress": sleOSPFProcSummaryIPAddress,
       "sleOSPFProcSummaryIPMask": sleOSPFProcSummaryIPMask,
       "sleOSPFProcSummaryTag": sleOSPFProcSummaryTag,
       "sleOSPFProcSummaryAdvertiseFlag": sleOSPFProcSummaryAdvertiseFlag,
       "sleOSPFProcSummaryControl": sleOSPFProcSummaryControl,
       "sleOSPFProcSummaryControlRequest": sleOSPFProcSummaryControlRequest,
       "sleOSPFProcSummaryControlStatus": sleOSPFProcSummaryControlStatus,
       "sleOSPFProcSummaryControlTimer": sleOSPFProcSummaryControlTimer,
       "sleOSPFProcSummaryControlTimeStamp": sleOSPFProcSummaryControlTimeStamp,
       "sleOSPFProcSummaryControlReqResult": sleOSPFProcSummaryControlReqResult,
       "sleOSPFProcSummaryControlProcID": sleOSPFProcSummaryControlProcID,
       "sleOSPFProcSummaryControlIPAddress": sleOSPFProcSummaryControlIPAddress,
       "sleOSPFProcSummaryControlIPMask": sleOSPFProcSummaryControlIPMask,
       "sleOSPFProcSummaryControlTag": sleOSPFProcSummaryControlTag,
       "sleOSPFProcSummaryControlAdvertiseFlag": sleOSPFProcSummaryControlAdvertiseFlag,
       "sleOSPFProcSummaryNotification": sleOSPFProcSummaryNotification,
       "sleOSPFSummaryCreated": sleOSPFSummaryCreated,
       "sleOSPFSummaryDeleted": sleOSPFSummaryDeleted,
       "sleOSPFSummaryChanged": sleOSPFSummaryChanged,
       "sleOSPFProcDistributeList": sleOSPFProcDistributeList,
       "sleOSPFProcDistributeListTable": sleOSPFProcDistributeListTable,
       "sleOSPFProcDistributeListEntry": sleOSPFProcDistributeListEntry,
       "sleOSPFProcDistributeListOutFilterType": sleOSPFProcDistributeListOutFilterType,
       "sleOSPFProcDistributeListAccessName": sleOSPFProcDistributeListAccessName,
       "sleOSPFProcDistributeListControl": sleOSPFProcDistributeListControl,
       "sleOSPFProcDistributeListControlRequest": sleOSPFProcDistributeListControlRequest,
       "sleOSPFProcDistributeListControlStatus": sleOSPFProcDistributeListControlStatus,
       "sleOSPFProcDistributeListControlTimer": sleOSPFProcDistributeListControlTimer,
       "sleOSPFProcDistributeListControlTimeStamp": sleOSPFProcDistributeListControlTimeStamp,
       "sleOSPFProcDistributeListControlReqResult": sleOSPFProcDistributeListControlReqResult,
       "sleOSPFProcDistributeListControlProcID": sleOSPFProcDistributeListControlProcID,
       "sleOSPFProcDistributeListControlOutFilterType": sleOSPFProcDistributeListControlOutFilterType,
       "sleOSPFProcDistributeListControlAccessName": sleOSPFProcDistributeListControlAccessName,
       "sleOSPFProcDistributeListNotification": sleOSPFProcDistributeListNotification,
       "sleOSPFDistributeListCreated": sleOSPFDistributeListCreated,
       "sleOSPFDistributeListDeleted": sleOSPFDistributeListDeleted,
       "sleOSPFProcNeighbor": sleOSPFProcNeighbor,
       "sleOSPFProcNeighborTable": sleOSPFProcNeighborTable,
       "sleOSPFProcNeighborEntry": sleOSPFProcNeighborEntry,
       "sleOSPFProcNeighborIPAddr": sleOSPFProcNeighborIPAddr,
       "sleOSPFProcNeighborPriority": sleOSPFProcNeighborPriority,
       "sleOSPFProcNeighborPollInterval": sleOSPFProcNeighborPollInterval,
       "sleOSPFProcNeighborCost": sleOSPFProcNeighborCost,
       "sleOSPFProcNeighborControl": sleOSPFProcNeighborControl,
       "sleOSPFProcNeighborControlRequest": sleOSPFProcNeighborControlRequest,
       "sleOSPFProcNeighborControlStatus": sleOSPFProcNeighborControlStatus,
       "sleOSPFProcNeighborControlTimer": sleOSPFProcNeighborControlTimer,
       "sleOSPFProcNeighborControlTimeStamp": sleOSPFProcNeighborControlTimeStamp,
       "sleOSPFProcNeighborControlReqResult": sleOSPFProcNeighborControlReqResult,
       "sleOSPFProcNeighborControlProcID": sleOSPFProcNeighborControlProcID,
       "sleOSPFProcNeighborControlIPAddr": sleOSPFProcNeighborControlIPAddr,
       "sleOSPFProcNeighborControlPriority": sleOSPFProcNeighborControlPriority,
       "sleOSPFProcNeighborControlPollInterval": sleOSPFProcNeighborControlPollInterval,
       "sleOSPFProcNeighborControlCost": sleOSPFProcNeighborControlCost,
       "sleOSPFProcNeighborNotification": sleOSPFProcNeighborNotification,
       "sleOSPFProcNeighborCreated": sleOSPFProcNeighborCreated,
       "sleOSPFProcNeighborDeleted": sleOSPFProcNeighborDeleted,
       "sleOSPFProcNeighborChanged": sleOSPFProcNeighborChanged,
       "sleOSPFProcPassIf": sleOSPFProcPassIf,
       "sleOSPFProcPassIfTable": sleOSPFProcPassIfTable,
       "sleOSPFProcPassIfEntry": sleOSPFProcPassIfEntry,
       "sleOSPFProcPassIfAddr": sleOSPFProcPassIfAddr,
       "sleOSPFProcPassIfName": sleOSPFProcPassIfName,
       "sleOSPFProcPassIfControl": sleOSPFProcPassIfControl,
       "sleOSPFProcPassIfControlRequest": sleOSPFProcPassIfControlRequest,
       "sleOSPFProcPassIfControlStatus": sleOSPFProcPassIfControlStatus,
       "sleOSPFProcPassIfControlTimer": sleOSPFProcPassIfControlTimer,
       "sleOSPFProcPassIfControlTimeStamp": sleOSPFProcPassIfControlTimeStamp,
       "sleOSPFProcPassIfControlReqResult": sleOSPFProcPassIfControlReqResult,
       "sleOSPFProcPassIfControlProcID": sleOSPFProcPassIfControlProcID,
       "sleOSPFProcPassIfControlIPAddr": sleOSPFProcPassIfControlIPAddr,
       "sleOSPFProcPassIfControlName": sleOSPFProcPassIfControlName,
       "sleOSPFProcPassIfNotification": sleOSPFProcPassIfNotification,
       "sleOSPFPassInterfaceCreated": sleOSPFPassInterfaceCreated,
       "sleOSPFPassInterfaceDeleted": sleOSPFPassInterfaceDeleted,
       "sleOSPFProcHost": sleOSPFProcHost,
       "sleOSPFProcHostTable": sleOSPFProcHostTable,
       "sleOSPFProcHostEntry": sleOSPFProcHostEntry,
       "sleOSPFProcHostIPAddr": sleOSPFProcHostIPAddr,
       "sleOSPFProcHostAreaID": sleOSPFProcHostAreaID,
       "sleOSPFProcHostAreaCost": sleOSPFProcHostAreaCost,
       "sleOSPFProcHostControl": sleOSPFProcHostControl,
       "sleOSPFProcHostControlRequest": sleOSPFProcHostControlRequest,
       "sleOSPFProcHostControlStatus": sleOSPFProcHostControlStatus,
       "sleOSPFProcHostControlTimer": sleOSPFProcHostControlTimer,
       "sleOSPFProcHostControlTimeStamp": sleOSPFProcHostControlTimeStamp,
       "sleOSPFProcHostControlReqResult": sleOSPFProcHostControlReqResult,
       "sleOSPFProcHostControlProcID": sleOSPFProcHostControlProcID,
       "sleOSPFProcHostControlIPAddr": sleOSPFProcHostControlIPAddr,
       "sleOSPFProcHostControlAreaID": sleOSPFProcHostControlAreaID,
       "sleOSPFProcHostControlAreaCost": sleOSPFProcHostControlAreaCost,
       "sleOSPFProcHostNotification": sleOSPFProcHostNotification,
       "sleOSPFProcHostCreated": sleOSPFProcHostCreated,
       "sleOSPFProcHostDeleted": sleOSPFProcHostDeleted,
       "sleOSPFProcHostCostChanged": sleOSPFProcHostCostChanged,
       "sleOSPFProcRedistribute": sleOSPFProcRedistribute,
       "sleOSPFProcRedistTable": sleOSPFProcRedistTable,
       "sleOSPFProcRedistEntry": sleOSPFProcRedistEntry,
       "sleOSPFProcRedistType": sleOSPFProcRedistType,
       "sleOSPFProcRedistMetricType": sleOSPFProcRedistMetricType,
       "sleOSPFProcRedistMetric": sleOSPFProcRedistMetric,
       "sleOSPFProcRedistRouteMapName": sleOSPFProcRedistRouteMapName,
       "sleOSPFProcRedistTag": sleOSPFProcRedistTag,
       "sleOSPFProcRedistSubnets": sleOSPFProcRedistSubnets,
       "sleOSPFProcRedistControl": sleOSPFProcRedistControl,
       "sleOSPFProcRedistControlRequest": sleOSPFProcRedistControlRequest,
       "sleOSPFProcRedistControlStatus": sleOSPFProcRedistControlStatus,
       "sleOSPFProcRedistControlTimer": sleOSPFProcRedistControlTimer,
       "sleOSPFProcRedistControlTimeStamp": sleOSPFProcRedistControlTimeStamp,
       "sleOSPFProcRedistControlReqResult": sleOSPFProcRedistControlReqResult,
       "sleOSPFProcRedistControlProcID": sleOSPFProcRedistControlProcID,
       "sleOSPFProcRedistControlType": sleOSPFProcRedistControlType,
       "sleOSPFProcRedistControlMetricType": sleOSPFProcRedistControlMetricType,
       "sleOSPFProcRedistControlMetric": sleOSPFProcRedistControlMetric,
       "sleOSPFProcRedistControlRouteMapName": sleOSPFProcRedistControlRouteMapName,
       "sleOSPFProcRedistControlTag": sleOSPFProcRedistControlTag,
       "sleOSPFProcRedistControlSubnets": sleOSPFProcRedistControlSubnets,
       "sleOSPFProcRedistNotification": sleOSPFProcRedistNotification,
       "sleOSPFProcRedistCreated": sleOSPFProcRedistCreated,
       "sleOSPFProcRedistDeleted": sleOSPFProcRedistDeleted,
       "sleOSPFProcRedistChanged": sleOSPFProcRedistChanged,
       "sleOSPFProcArea": sleOSPFProcArea,
       "sleOSPFProcAreaInfo": sleOSPFProcAreaInfo,
       "sleOSPFProcAreaInfoTable": sleOSPFProcAreaInfoTable,
       "sleOSPFProcAreaInfoEntry": sleOSPFProcAreaInfoEntry,
       "sleOSPFProcAreaID": sleOSPFProcAreaID,
       "sleOSPFProcAreaType": sleOSPFProcAreaType,
       "sleOSPFProcAreaDefaultCost": sleOSPFProcAreaDefaultCost,
       "sleOSPFProcAreaAuthenType": sleOSPFProcAreaAuthenType,
       "sleOSPFProcAreaFAInName": sleOSPFProcAreaFAInName,
       "sleOSPFProcAreaFAOutName": sleOSPFProcAreaFAOutName,
       "sleOSPFProcAreaFPInName": sleOSPFProcAreaFPInName,
       "sleOSPFProcAreaFPOutName": sleOSPFProcAreaFPOutName,
       "sleOSPFProcAreaShortcutType": sleOSPFProcAreaShortcutType,
       "sleOSPFProcAreaSpfRuns": sleOSPFProcAreaSpfRuns,
       "sleOSPFProcAreaLsaCount": sleOSPFProcAreaLsaCount,
       "sleOSPFProcAreaLsaCheckSum": sleOSPFProcAreaLsaCheckSum,
       "sleOSPFProcAreaSummary": sleOSPFProcAreaSummary,
       "sleOSPFProcAreaNssaTransRole": sleOSPFProcAreaNssaTransRole,
       "sleOSPFProcAreaNssaNoRedist": sleOSPFProcAreaNssaNoRedist,
       "sleOSPFProcAreaNssaDefOriginate": sleOSPFProcAreaNssaDefOriginate,
       "sleOSPFProcAreaNssaDefMetricType": sleOSPFProcAreaNssaDefMetricType,
       "sleOSPFProcAreaNssaDefMetric": sleOSPFProcAreaNssaDefMetric,
       "sleOSPFProcAreaInfoControl": sleOSPFProcAreaInfoControl,
       "sleOSPFProcAreaControlRequest": sleOSPFProcAreaControlRequest,
       "sleOSPFProcAreaControlStatus": sleOSPFProcAreaControlStatus,
       "sleOSPFProcAreaControlTimer": sleOSPFProcAreaControlTimer,
       "sleOSPFProcAreaControlTimeStamp": sleOSPFProcAreaControlTimeStamp,
       "sleOSPFProcAreaControlReqResult": sleOSPFProcAreaControlReqResult,
       "sleOSPFProcAreaControlProcID": sleOSPFProcAreaControlProcID,
       "sleOSPFProcAreaControlID": sleOSPFProcAreaControlID,
       "sleOSPFProcAreaControlType": sleOSPFProcAreaControlType,
       "sleOSPFProcAreaControlDefaultCost": sleOSPFProcAreaControlDefaultCost,
       "sleOSPFProcAreaControlAuthenType": sleOSPFProcAreaControlAuthenType,
       "sleOSPFProcAreaControlFAInName": sleOSPFProcAreaControlFAInName,
       "sleOSPFProcAreaControlFAOutName": sleOSPFProcAreaControlFAOutName,
       "sleOSPFProcAreaControlFPInName": sleOSPFProcAreaControlFPInName,
       "sleOSPFProcAreaControlFPOutName": sleOSPFProcAreaControlFPOutName,
       "sleOSPFProcAreaControlShortcutType": sleOSPFProcAreaControlShortcutType,
       "sleOSPFProcAreaControlSummary": sleOSPFProcAreaControlSummary,
       "sleOSPFProcAreaControlNssaTransRole": sleOSPFProcAreaControlNssaTransRole,
       "sleOSPFProcAreaControlNssaNoRedist": sleOSPFProcAreaControlNssaNoRedist,
       "sleOSPFProcAreaControlNssaDefOriginate": sleOSPFProcAreaControlNssaDefOriginate,
       "sleOSPFProcAreaControlNssaDefMetricType": sleOSPFProcAreaControlNssaDefMetricType,
       "sleOSPFProcAreaControlNssaDefMetric": sleOSPFProcAreaControlNssaDefMetric,
       "sleOSPFProcAreaInfoNotification": sleOSPFProcAreaInfoNotification,
       "sleOSPFProcGeneralAreaCreated": sleOSPFProcGeneralAreaCreated,
       "sleOSPFProcStubNssaAreaCreated": sleOSPFProcStubNssaAreaCreated,
       "sleOSPFProcAreaDeleted": sleOSPFProcAreaDeleted,
       "sleOSPFProcAreaDefaultCostChanged": sleOSPFProcAreaDefaultCostChanged,
       "sleOSPFProcAreaAuthenTypeChanged": sleOSPFProcAreaAuthenTypeChanged,
       "sleOSPFProcAreaFAInNameChanged": sleOSPFProcAreaFAInNameChanged,
       "sleOSPFProcAreaFAOutNameChanged": sleOSPFProcAreaFAOutNameChanged,
       "sleOSPFProcAreaFPInNameChanged": sleOSPFProcAreaFPInNameChanged,
       "sleOSPFProcAreaFPOutNameChanged": sleOSPFProcAreaFPOutNameChanged,
       "sleOSPFProcAreaShortcutTypeChanged": sleOSPFProcAreaShortcutTypeChanged,
       "sleOSPFProcAreaSummaryChanged": sleOSPFProcAreaSummaryChanged,
       "sleOSPFProcNssaAreaTransRoleChanged": sleOSPFProcNssaAreaTransRoleChanged,
       "sleOSPFProcNssaAreaTransNoRedistChanged": sleOSPFProcNssaAreaTransNoRedistChanged,
       "sleOSPFProcNssaAreaDefProfileChanged": sleOSPFProcNssaAreaDefProfileChanged,
       "sleOSPFProcAreaRange": sleOSPFProcAreaRange,
       "sleOSPFProcAreaRangeTable": sleOSPFProcAreaRangeTable,
       "sleOSPFProcAreaRangeEntry": sleOSPFProcAreaRangeEntry,
       "sleOSPFProcAreaRangeIP": sleOSPFProcAreaRangeIP,
       "sleOSPFProcAreaRangeIPMask": sleOSPFProcAreaRangeIPMask,
       "sleOSPFProcAreaRangeAdverType": sleOSPFProcAreaRangeAdverType,
       "sleOSPFProcAreaRangeControl": sleOSPFProcAreaRangeControl,
       "sleOSPFProcAreaRangeControlRequest": sleOSPFProcAreaRangeControlRequest,
       "sleOSPFProcAreaRangeControlStatus": sleOSPFProcAreaRangeControlStatus,
       "sleOSPFProcAreaRangeControlTimer": sleOSPFProcAreaRangeControlTimer,
       "sleOSPFProcAreaRangeControlTimeStamp": sleOSPFProcAreaRangeControlTimeStamp,
       "sleOSPFProcAreaRangeControlReqResult": sleOSPFProcAreaRangeControlReqResult,
       "sleOSPFProcAreaRangeControlProcID": sleOSPFProcAreaRangeControlProcID,
       "sleOSPFProcAreaRangeControlID": sleOSPFProcAreaRangeControlID,
       "sleOSPFProcAreaRangeControlIP": sleOSPFProcAreaRangeControlIP,
       "sleOSPFProcAreaRangeControlIPMask": sleOSPFProcAreaRangeControlIPMask,
       "sleOSPFProcAreaRangeControlAdverType": sleOSPFProcAreaRangeControlAdverType,
       "sleOSPFProcAreaRangeNotification": sleOSPFProcAreaRangeNotification,
       "sleOSPFAreaRangeCreated": sleOSPFAreaRangeCreated,
       "sleOSPFAreaRangeDeleted": sleOSPFAreaRangeDeleted,
       "sleOSPFAreaRangeChanged": sleOSPFAreaRangeChanged,
       "sleOSPFProcAreaVlink": sleOSPFProcAreaVlink,
       "sleOSPFProcAreaVlinkInfo": sleOSPFProcAreaVlinkInfo,
       "sleOSPFProcAreaVlinkInfoTable": sleOSPFProcAreaVlinkInfoTable,
       "sleOSPFProcAreaVlinkInfoEntry": sleOSPFProcAreaVlinkInfoEntry,
       "sleOSPFProcAreaVlinkIP": sleOSPFProcAreaVlinkIP,
       "sleOSPFProcAreaVlinkAuthenType": sleOSPFProcAreaVlinkAuthenType,
       "sleOSPFProcAreaVlinkAuthenKey": sleOSPFProcAreaVlinkAuthenKey,
       "sleOSPFProcAreaVlinkDeadInterval": sleOSPFProcAreaVlinkDeadInterval,
       "sleOSPFProcAreaVlinkHelloInterval": sleOSPFProcAreaVlinkHelloInterval,
       "sleOSPFProcAreaVlinkRetranInterval": sleOSPFProcAreaVlinkRetranInterval,
       "sleOSPFProcAreaVlinkTransDelay": sleOSPFProcAreaVlinkTransDelay,
       "sleOSPFProcAreaVlinkControl": sleOSPFProcAreaVlinkControl,
       "sleOSPFProcAreaVlinkControlRequest": sleOSPFProcAreaVlinkControlRequest,
       "sleOSPFProcAreaVlinkControlStatus": sleOSPFProcAreaVlinkControlStatus,
       "sleOSPFProcAreaVlinkControlTimer": sleOSPFProcAreaVlinkControlTimer,
       "sleOSPFProcAreaVlinkControlTimeStamp": sleOSPFProcAreaVlinkControlTimeStamp,
       "sleOSPFProcAreaVlinkControlReqResult": sleOSPFProcAreaVlinkControlReqResult,
       "sleOSPFProcAreaVlinkControlProcID": sleOSPFProcAreaVlinkControlProcID,
       "sleOSPFProcAreaVlinkControlControlID": sleOSPFProcAreaVlinkControlControlID,
       "sleOSPFProcAreaVlinkControlIP": sleOSPFProcAreaVlinkControlIP,
       "sleOSPFProcAreaVlinkControlAuthenType": sleOSPFProcAreaVlinkControlAuthenType,
       "sleOSPFProcAreaVlinkControlAuthenKey": sleOSPFProcAreaVlinkControlAuthenKey,
       "sleOSPFProcAreaVlinkControlDeadInterval": sleOSPFProcAreaVlinkControlDeadInterval,
       "sleOSPFProcAreaVlinkControlHelloInterval": sleOSPFProcAreaVlinkControlHelloInterval,
       "sleOSPFProcAreaVlinkControlRetranInterval": sleOSPFProcAreaVlinkControlRetranInterval,
       "sleOSPFProcAreaVlinkControlTransInterval": sleOSPFProcAreaVlinkControlTransInterval,
       "sleOSPFProcAreaVlinkNotification": sleOSPFProcAreaVlinkNotification,
       "sleOSPFAreaVlinkCreated": sleOSPFAreaVlinkCreated,
       "sleOSPFAreaVLinkDeleted": sleOSPFAreaVLinkDeleted,
       "sleOSPFAreaVLinkChanged": sleOSPFAreaVLinkChanged,
       "sleOSPFProcAreaVlinkMsgKey": sleOSPFProcAreaVlinkMsgKey,
       "sleOSPFProcAreaVlinkMsgKeyTable": sleOSPFProcAreaVlinkMsgKeyTable,
       "sleOSPFProcAreaVlinkMsgKeyEntry": sleOSPFProcAreaVlinkMsgKeyEntry,
       "sleOSPFProcAreaVlinkMsgKeyID": sleOSPFProcAreaVlinkMsgKeyID,
       "sleOSPFProcAreaVlinkMsgKeyVal": sleOSPFProcAreaVlinkMsgKeyVal,
       "sleOSPFProcAreaVlinkMsgKeyControl": sleOSPFProcAreaVlinkMsgKeyControl,
       "sleOSPFProcAreaVlinkMsgKeyControlRequest": sleOSPFProcAreaVlinkMsgKeyControlRequest,
       "sleOSPFProcAreaVlinkMsgKeyControlControlStatus": sleOSPFProcAreaVlinkMsgKeyControlControlStatus,
       "sleOSPFProcAreaVlinkMsgKeyControlControlTimer": sleOSPFProcAreaVlinkMsgKeyControlControlTimer,
       "sleOSPFProcAreaVlinkMsgKeyControlTimeStamp": sleOSPFProcAreaVlinkMsgKeyControlTimeStamp,
       "sleOSPFProcAreaVlinkMsgKeyControlReqResult": sleOSPFProcAreaVlinkMsgKeyControlReqResult,
       "sleOSPFProcAreaVlinkMsgKeyControlProcID": sleOSPFProcAreaVlinkMsgKeyControlProcID,
       "sleOSPFProcAreaVlinkMsgKeyControlID": sleOSPFProcAreaVlinkMsgKeyControlID,
       "sleOSPFProcAreaVlinkMsgKeyControlIP": sleOSPFProcAreaVlinkMsgKeyControlIP,
       "sleOSPFProcAreaVlinkMsgKeyControlKeyID": sleOSPFProcAreaVlinkMsgKeyControlKeyID,
       "sleOSPFProcAreaVlinkMsgKeyControlKeyVal": sleOSPFProcAreaVlinkMsgKeyControlKeyVal,
       "sleOSPFProcAreaVlinkMsgKeyNotification": sleOSPFProcAreaVlinkMsgKeyNotification,
       "sleOSPFAreaVlinkMsgKeyCreated": sleOSPFAreaVlinkMsgKeyCreated,
       "sleOSPFAreaVLinkMsgKeyDeleted": sleOSPFAreaVLinkMsgKeyDeleted,
       "sleOSPFInterface": sleOSPFInterface,
       "sleOSPFIf": sleOSPFIf,
       "sleOSPFIfTable": sleOSPFIfTable,
       "sleOSPFIfEntry": sleOSPFIfEntry,
       "sleOSPFIfIndex": sleOSPFIfIndex,
       "sleOSFPIfEnabled": sleOSFPIfEnabled,
       "sleOSPFIfNetworkType": sleOSPFIfNetworkType,
       "sleOSFPIfMTU": sleOSFPIfMTU,
       "sleOSFPIfBFD": sleOSFPIfBFD,
       "sleOSFPIfEFM": sleOSFPIfEFM,
       "sleOSPFIfControl": sleOSPFIfControl,
       "sleOSPFIfControlRequest": sleOSPFIfControlRequest,
       "sleOSPFIfControlStatus": sleOSPFIfControlStatus,
       "sleOSPFIfControlTimer": sleOSPFIfControlTimer,
       "sleOSPFIfControlTimeStamp": sleOSPFIfControlTimeStamp,
       "sleOSPFIfControlReqResult": sleOSPFIfControlReqResult,
       "sleOSPFIfControlIndex": sleOSPFIfControlIndex,
       "sleOSPFIfControlEnabled": sleOSPFIfControlEnabled,
       "sleOSPFIfControlNetworkType": sleOSPFIfControlNetworkType,
       "sleOSPFIfControlMTU": sleOSPFIfControlMTU,
       "sleOSPFIfControlBFD": sleOSPFIfControlBFD,
       "sleOSPFIfControlEFM": sleOSPFIfControlEFM,
       "sleOSPFIfBaseNotification": sleOSPFIfBaseNotification,
       "sleOSPFIfEnableChanged": sleOSPFIfEnableChanged,
       "sleOSPFIfNetworkTypeChanged": sleOSPFIfNetworkTypeChanged,
       "sleOSPFIfMTUChanged": sleOSPFIfMTUChanged,
       "sleOSPFIfBFDChanged": sleOSPFIfBFDChanged,
       "sleOSPFIfEFMChanged": sleOSPFIfEFMChanged,
       "sleOSPFIfInfo": sleOSPFIfInfo,
       "sleOSPFIfInfoTable": sleOSPFIfInfoTable,
       "sleOSPFIfInfoEntry": sleOSPFIfInfoEntry,
       "sleOSPFIfIpAddr": sleOSPFIfIpAddr,
       "sleOSPFIfCost": sleOSPFIfCost,
       "sleOSPFIfTransmitDelay": sleOSPFIfTransmitDelay,
       "sleOSPFIfPriority": sleOSPFIfPriority,
       "sleOSPFIfHelloInterval": sleOSPFIfHelloInterval,
       "sleOSPFIfDeadInterval": sleOSPFIfDeadInterval,
       "sleOSPFIfRetransInterval": sleOSPFIfRetransInterval,
       "sleOSPFIfAuth": sleOSPFIfAuth,
       "sleOSPFIfAuthType": sleOSPFIfAuthType,
       "sleOSPFIfDataFilterOut": sleOSPFIfDataFilterOut,
       "sleOSPFIfMTUIgnore": sleOSPFIfMTUIgnore,
       "sleOSPFIfResync": sleOSPFIfResync,
       "sleOSPFIfResyncTimeout": sleOSPFIfResyncTimeout,
       "sleOSPFIfAuthKeyFirst": sleOSPFIfAuthKeyFirst,
       "sleOSPFIfAuthKeyFirstAct": sleOSPFIfAuthKeyFirstAct,
       "sleOSPFIfAuthKeySecond": sleOSPFIfAuthKeySecond,
       "sleOSPFIfAuthKeySecondAct": sleOSPFIfAuthKeySecondAct,
       "sleOSPFIfInfoControl": sleOSPFIfInfoControl,
       "sleOSPFIfInfoControlRequest": sleOSPFIfInfoControlRequest,
       "sleOSPFIfInfoControlStatus": sleOSPFIfInfoControlStatus,
       "sleOSPFIfInfoControlTimer": sleOSPFIfInfoControlTimer,
       "sleOSPFIfInfoControlTimeStamp": sleOSPFIfInfoControlTimeStamp,
       "sleOSPFIfInfoControlReqResult": sleOSPFIfInfoControlReqResult,
       "sleOSPFIfInfoControlIndex": sleOSPFIfInfoControlIndex,
       "sleOSPFIfInfoControlIpAddr": sleOSPFIfInfoControlIpAddr,
       "sleOSPFIfInfoControlCost": sleOSPFIfInfoControlCost,
       "sleOSPFIfInfoControlTransmitDelay": sleOSPFIfInfoControlTransmitDelay,
       "sleOSPFIfInfoControlPriority": sleOSPFIfInfoControlPriority,
       "sleOSPFIfInfoControlHelloInterval": sleOSPFIfInfoControlHelloInterval,
       "sleOSPFIfInfoControlDeadInterval": sleOSPFIfInfoControlDeadInterval,
       "sleOSPFIfInfoControlRetransInterval": sleOSPFIfInfoControlRetransInterval,
       "sleOSPFIfInfoControlAuth": sleOSPFIfInfoControlAuth,
       "sleOSPFIfInfoControlAuthType": sleOSPFIfInfoControlAuthType,
       "sleOSPFIfInfoControlDataFilterOut": sleOSPFIfInfoControlDataFilterOut,
       "sleOSPFIfInfoControlMTUIgnore": sleOSPFIfInfoControlMTUIgnore,
       "sleOSPFIfInfoControlResync": sleOSPFIfInfoControlResync,
       "sleOSPFIfInfoControlResyncTimeout": sleOSPFIfInfoControlResyncTimeout,
       "sleOSPFIfInfoControlAuthKeyFirst": sleOSPFIfInfoControlAuthKeyFirst,
       "sleOSPFIfInfoControlAuthKeyFirstAct": sleOSPFIfInfoControlAuthKeyFirstAct,
       "sleOSPFIfInfoControlAuthKeySecond": sleOSPFIfInfoControlAuthKeySecond,
       "sleOSPFIfInfoControlAuthKeySecondAct": sleOSPFIfInfoControlAuthKeySecondAct,
       "sleOSPFIfInfoNotification": sleOSPFIfInfoNotification,
       "sleOSPFIfCostChanged": sleOSPFIfCostChanged,
       "sleOSPFIfPriorityChanged": sleOSPFIfPriorityChanged,
       "sleOSPFIfTransmitDelayChanged": sleOSPFIfTransmitDelayChanged,
       "sleOSPFIfHelloIntervalChanged": sleOSPFIfHelloIntervalChanged,
       "sleOSPFIfDeadIntervalChanged": sleOSPFIfDeadIntervalChanged,
       "sleOSPFIfRetransIntervalChanged": sleOSPFIfRetransIntervalChanged,
       "sleOSPFIfAuthProfileChanged": sleOSPFIfAuthProfileChanged,
       "sleOSPFIfDatafilterOutChanged": sleOSPFIfDatafilterOutChanged,
       "sleOSPFIfMTUIgnoreChanged": sleOSPFIfMTUIgnoreChanged,
       "sleOSPFIfResyncProfileChanged": sleOSPFIfResyncProfileChanged,
       "sleOSPFIfAuthKeyFirstProfileChanged": sleOSPFIfAuthKeyFirstProfileChanged,
       "sleOSPFIfAuthKeyProfileSecondChanged": sleOSPFIfAuthKeyProfileSecondChanged,
       "sleOSPFIfMsgKey": sleOSPFIfMsgKey,
       "sleOSPFIfMsgKeyTable": sleOSPFIfMsgKeyTable,
       "sleOSPFIfMsgKeyEntry": sleOSPFIfMsgKeyEntry,
       "sleOSPFIfMsgKeyID": sleOSPFIfMsgKeyID,
       "sleOSPFIfMsgKeyVal": sleOSPFIfMsgKeyVal,
       "sleOSPFIfMsgKeyAct": sleOSPFIfMsgKeyAct,
       "sleOSPFIfMsgKeyControl": sleOSPFIfMsgKeyControl,
       "sleOSPFIfMsgKeyControlRequest": sleOSPFIfMsgKeyControlRequest,
       "sleOSPFIfMsgKeyControlStatus": sleOSPFIfMsgKeyControlStatus,
       "sleOSPFIfMsgKeyControlTimer": sleOSPFIfMsgKeyControlTimer,
       "sleOSPFIfMsgKeyControlTimeStamp": sleOSPFIfMsgKeyControlTimeStamp,
       "sleOSPFIfMsgKeyControlReqResult": sleOSPFIfMsgKeyControlReqResult,
       "sleOSPFIfMsgKeyControlIndex": sleOSPFIfMsgKeyControlIndex,
       "sleOSPFIfMsgKeyControlIpAddr": sleOSPFIfMsgKeyControlIpAddr,
       "sleOSPFIfMsgKeyControlKeyID": sleOSPFIfMsgKeyControlKeyID,
       "sleOSPFIfMsgKeyControlKeyVal": sleOSPFIfMsgKeyControlKeyVal,
       "sleOSPFIfMsgKeyControlKeyAct": sleOSPFIfMsgKeyControlKeyAct,
       "sleOSPFIfMsgKeyNotification": sleOSPFIfMsgKeyNotification,
       "sleOSPFIfMsgKeyCreated": sleOSPFIfMsgKeyCreated,
       "sleOSPFIfMsgKeyDeleted": sleOSPFIfMsgKeyDeleted,
       "sleOSPFIfStatus": sleOSPFIfStatus,
       "sleOSPFIfStatusTable": sleOSPFIfStatusTable,
       "sleOSPFIfStatusEntry": sleOSPFIfStatusEntry,
       "sleOSPFIfStatusAddr": sleOSPFIfStatusAddr,
       "sleOSPFIfStatusUpState": sleOSPFIfStatusUpState,
       "sleOSPFIfStatusAreaID": sleOSPFIfStatusAreaID,
       "sleOSPFIfStatusProcID": sleOSPFIfStatusProcID,
       "sleOSPFIfStatusRouterID": sleOSPFIfStatusRouterID,
       "sleOSPFIfStatusNetworkType": sleOSPFIfStatusNetworkType,
       "sleOSPFIfStatusCost": sleOSPFIfStatusCost,
       "sleOSPFIfStatusTransmitDelay": sleOSPFIfStatusTransmitDelay,
       "sleOSPFIfStatusState": sleOSPFIfStatusState,
       "sleOSPFIfStatusPriorityUse": sleOSPFIfStatusPriorityUse,
       "sleOSPFIfStatusPriority": sleOSPFIfStatusPriority,
       "sleOSPFIfStatusDRRouterUse": sleOSPFIfStatusDRRouterUse,
       "sleOSPFIfStatusDRRouterID": sleOSPFIfStatusDRRouterID,
       "sleOSPFIfStatusDRIfIpAddr": sleOSPFIfStatusDRIfIpAddr,
       "sleOSPFIfStatusBDRRouterUse": sleOSPFIfStatusBDRRouterUse,
       "sleOSPFIfStatusBDRRouterID": sleOSPFIfStatusBDRRouterID,
       "sleOSPFIfStatusBDRIfIpAddr": sleOSPFIfStatusBDRIfIpAddr,
       "sleOSPFIfStatusHelloInterval": sleOSPFIfStatusHelloInterval,
       "sleOSPFIfStatusDeadInterval": sleOSPFIfStatusDeadInterval,
       "sleOSPFIfStatusRetransInterval": sleOSPFIfStatusRetransInterval,
       "sleOSPFIfStatusWaitInterval": sleOSPFIfStatusWaitInterval,
       "sleOSPFIfStatusNeighborCount": sleOSPFIfStatusNeighborCount,
       "sleOSPFIfCryptSeqNum": sleOSPFIfCryptSeqNum,
       "sleOSPFIfStatusRcvHello": sleOSPFIfStatusRcvHello,
       "sleOSPFIfStatusSendHello": sleOSPFIfStatusSendHello,
       "sleOSPFIfStatusRcvDD": sleOSPFIfStatusRcvDD,
       "sleOSPFIfStatusSendDD": sleOSPFIfStatusSendDD,
       "sleOSPFIfStatusRcvLSReq": sleOSPFIfStatusRcvLSReq,
       "sleOSPFIfStatusSendLSReq": sleOSPFIfStatusSendLSReq,
       "sleOSPFIfStatusRcvLSUpd": sleOSPFIfStatusRcvLSUpd,
       "sleOSPFIfStatusSendLSUpd": sleOSPFIfStatusSendLSUpd,
       "sleOSPFIfStatusRcvLSAck": sleOSPFIfStatusRcvLSAck,
       "sleOSPFIfStatusSendLSAck": sleOSPFIfStatusSendLSAck,
       "sleOSPFIfStatusDiscarded": sleOSPFIfStatusDiscarded,
       "sleOSPFIfStatusMtu": sleOSPFIfStatusMtu,
       "sleOSPFLsa": sleOSPFLsa,
       "sleOSPFLsaTable": sleOSPFLsaTable,
       "sleOSPFLsaEntry": sleOSPFLsaEntry,
       "sleOSPFLsaType": sleOSPFLsaType,
       "sleOSPFLsaAreaID": sleOSPFLsaAreaID,
       "sleOSPFLsaLinkID": sleOSPFLsaLinkID,
       "sleOSPFLsaAdvRouter": sleOSPFLsaAdvRouter,
       "sleOSPFLsaAge": sleOSPFLsaAge,
       "sleOSPFLsaSequence": sleOSPFLsaSequence,
       "sleOSPFNeighbor": sleOSPFNeighbor,
       "sleOSPFNeighborTable": sleOSPFNeighborTable,
       "sleOSPFNeighborEntry": sleOSPFNeighborEntry,
       "sleOSPFNeighborIPAddr": sleOSPFNeighborIPAddr,
       "sleOSPFNeighborID": sleOSPFNeighborID,
       "sleOSPFNeighborPriority": sleOSPFNeighborPriority,
       "sleOSPFNeighborState": sleOSPFNeighborState,
       "sleOSPFNeighborIfName": sleOSPFNeighborIfName,
       "sleOSPFRoute": sleOSPFRoute,
       "sleOSPFRouteTable": sleOSPFRouteTable,
       "sleOSPFRouteEntry": sleOSPFRouteEntry,
       "sleOSPFRoutePathType": sleOSPFRoutePathType,
       "sleOSPFRouteNexthop": sleOSPFRouteNexthop,
       "sleOSPFRouteNbrID": sleOSPFRouteNbrID,
       "sleOSPFRoutePathTypeCode": sleOSPFRoutePathTypeCode,
       "sleOSPFRouteMetric": sleOSPFRouteMetric,
       "sleOSPFRouteIfName": sleOSPFRouteIfName,
       "sleOSPFRouteAreaUse": sleOSPFRouteAreaUse,
       "sleOSPFRouteAreaID": sleOSPFRouteAreaID,
       "sleOspfGroup": sleOspfGroup,
       "sleOspfNotificationGroup": sleOspfNotificationGroup}
)
