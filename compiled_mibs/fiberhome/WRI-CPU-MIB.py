# SNMP MIB module (WRI-CPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\WRI-CPU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:12 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(wri,
 wriProducts) = mibBuilder.importSymbols(
    "WRI-SMI",
    "wri",
    "wriProducts")


# MODULE-IDENTITY

msppCpu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4)
)
if mibBuilder.loadTexts:
    msppCpu.setRevisions(
        ("2010-01-11 00:00",
         "2009-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mspp_ObjectIdentity = ObjectIdentity
mspp = _Mspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012)
)
_MsppChassis_ObjectIdentity = ObjectIdentity
msppChassis = _MsppChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1)
)
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("current")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1)
)
cpuEntry.setIndexNames(
    (0, "WRI-CPU-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("current")
_CpuIndex_Type = Unsigned32
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_CpuUsage_Type = Counter32
_CpuUsage_Object = MibTableColumn
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 2),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_CpuMaxUsage_Type = Counter32
_CpuMaxUsage_Object = MibTableColumn
cpuMaxUsage = _CpuMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 3),
    _CpuMaxUsage_Type()
)
cpuMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuMaxUsage.setStatus("current")
_CpuHthreshold_Type = Counter32
_CpuHthreshold_Object = MibTableColumn
cpuHthreshold = _CpuHthreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 4),
    _CpuHthreshold_Type()
)
cpuHthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuHthreshold.setStatus("current")
_CpuLthreshold_Type = Counter32
_CpuLthreshold_Object = MibTableColumn
cpuLthreshold = _CpuLthreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 5),
    _CpuLthreshold_Type()
)
cpuLthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuLthreshold.setStatus("current")


class _CpuOneTrap_Type(Integer32):
    """Custom type cpuOneTrap based on Integer32"""
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


_CpuOneTrap_Type.__name__ = "Integer32"
_CpuOneTrap_Object = MibTableColumn
cpuOneTrap = _CpuOneTrap_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 6),
    _CpuOneTrap_Type()
)
cpuOneTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuOneTrap.setStatus("current")


class _CpuStatus_Type(Integer32):
    """Custom type cpuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("highoverflow", 1))
    )


_CpuStatus_Type.__name__ = "Integer32"
_CpuStatus_Object = MibTableColumn
cpuStatus = _CpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 7),
    _CpuStatus_Type()
)
cpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatus.setStatus("current")
_CpuDescr_Type = OctetString
_CpuDescr_Object = MibTableColumn
cpuDescr = _CpuDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 8),
    _CpuDescr_Type()
)
cpuDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDescr.setStatus("current")
_CpuAllSetting_Type = OctetString
_CpuAllSetting_Object = MibTableColumn
cpuAllSetting = _CpuAllSetting_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 9),
    _CpuAllSetting_Type()
)
cpuAllSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAllSetting.setStatus("current")
_CpuLastOneMinuteUsage_Type = Counter32
_CpuLastOneMinuteUsage_Object = MibTableColumn
cpuLastOneMinuteUsage = _CpuLastOneMinuteUsage_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 10),
    _CpuLastOneMinuteUsage_Type()
)
cpuLastOneMinuteUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLastOneMinuteUsage.setStatus("current")
_CpuLastFiveMinuteUsage_Type = Counter32
_CpuLastFiveMinuteUsage_Object = MibTableColumn
cpuLastFiveMinuteUsage = _CpuLastFiveMinuteUsage_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 11),
    _CpuLastFiveMinuteUsage_Type()
)
cpuLastFiveMinuteUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLastFiveMinuteUsage.setStatus("current")
_CpuIndexDescr_Type = OctetString
_CpuIndexDescr_Object = MibTableColumn
cpuIndexDescr = _CpuIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 1, 1, 12),
    _CpuIndexDescr_Type()
)
cpuIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndexDescr.setStatus("current")
_CpuTrap_ObjectIdentity = ObjectIdentity
cpuTrap = _CpuTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 2)
)
_CpuGeneral_ObjectIdentity = ObjectIdentity
cpuGeneral = _CpuGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 3)
)
_CpuNum_Type = Integer32
_CpuNum_Object = MibScalar
cpuNum = _CpuNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 3, 1),
    _CpuNum_Type()
)
cpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuNum.setStatus("current")
_CpuTrapEnable_Type = Integer32
_CpuTrapEnable_Object = MibScalar
cpuTrapEnable = _CpuTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 3, 2),
    _CpuTrapEnable_Type()
)
cpuTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuTrapEnable.setStatus("current")


class _CpuMonitor_Type(Integer32):
    """Custom type cpuMonitor based on Integer32"""
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


_CpuMonitor_Type.__name__ = "Integer32"
_CpuMonitor_Object = MibScalar
cpuMonitor = _CpuMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 3, 3),
    _CpuMonitor_Type()
)
cpuMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuMonitor.setStatus("current")

# Managed Objects groups


# Notification objects

cpuOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 2, 1)
)
cpuOverThreshold.setObjects(
      *(("WRI-CPU-MIB", "cpuUsage"),
        ("WRI-CPU-MIB", "cpuHthreshold"),
        ("WRI-CPU-MIB", "cpuLthreshold"))
)
if mibBuilder.loadTexts:
    cpuOverThreshold.setStatus(
        "current"
    )

cpuUnderThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 2, 2)
)
cpuUnderThreshold.setObjects(
      *(("WRI-CPU-MIB", "cpuUsage"),
        ("WRI-CPU-MIB", "cpuHthreshold"),
        ("WRI-CPU-MIB", "cpuLthreshold"))
)
if mibBuilder.loadTexts:
    cpuUnderThreshold.setStatus(
        "current"
    )

cpuRecoverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 4, 2, 3)
)
cpuRecoverThreshold.setObjects(
      *(("WRI-CPU-MIB", "cpuUsage"),
        ("WRI-CPU-MIB", "cpuHthreshold"),
        ("WRI-CPU-MIB", "cpuLthreshold"))
)
if mibBuilder.loadTexts:
    cpuRecoverThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRI-CPU-MIB",
    **{"mspp": mspp,
       "msppChassis": msppChassis,
       "msppCpu": msppCpu,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuIndex": cpuIndex,
       "cpuUsage": cpuUsage,
       "cpuMaxUsage": cpuMaxUsage,
       "cpuHthreshold": cpuHthreshold,
       "cpuLthreshold": cpuLthreshold,
       "cpuOneTrap": cpuOneTrap,
       "cpuStatus": cpuStatus,
       "cpuDescr": cpuDescr,
       "cpuAllSetting": cpuAllSetting,
       "cpuLastOneMinuteUsage": cpuLastOneMinuteUsage,
       "cpuLastFiveMinuteUsage": cpuLastFiveMinuteUsage,
       "cpuIndexDescr": cpuIndexDescr,
       "cpuTrap": cpuTrap,
       "cpuOverThreshold": cpuOverThreshold,
       "cpuUnderThreshold": cpuUnderThreshold,
       "cpuRecoverThreshold": cpuRecoverThreshold,
       "cpuGeneral": cpuGeneral,
       "cpuNum": cpuNum,
       "cpuTrapEnable": cpuTrapEnable,
       "cpuMonitor": cpuMonitor}
)
