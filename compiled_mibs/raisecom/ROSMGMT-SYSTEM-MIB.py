# SNMP MIB module (ROSMGMT-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\ROSMGMT-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:05 2025
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

(rosMgmt,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "rosMgmt")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rosMgmtSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1)
)
if mibBuilder.loadTexts:
    rosMgmtSystem.setRevisions(
        ("2020-04-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ProcessStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("rrunning", 1),
          ("dinterruptiblesleep", 2),
          ("suninterruptiblesleep", 3),
          ("tstopped", 4),
          ("zzombie", 5),
          ("xdead", 6),
          ("wpaging", 7))
    )



class CPUTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d.4d.4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



# MIB Managed Objects in the order of their OIDs

_RosMgmtCpu_ObjectIdentity = ObjectIdentity
rosMgmtCpu = _RosMgmtCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1)
)
_RosMgmtCpuNotifications_ObjectIdentity = ObjectIdentity
rosMgmtCpuNotifications = _RosMgmtCpuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 0)
)
_RosMgmtCpuObjects_ObjectIdentity = ObjectIdentity
rosMgmtCpuObjects = _RosMgmtCpuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1)
)
_RosMgmtCpuScalarGroup_ObjectIdentity = ObjectIdentity
rosMgmtCpuScalarGroup = _RosMgmtCpuScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1)
)


class _RosMgmtCpuTotalProcNum_Type(Integer32):
    """Custom type rosMgmtCpuTotalProcNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RosMgmtCpuTotalProcNum_Type.__name__ = "Integer32"
_RosMgmtCpuTotalProcNum_Object = MibScalar
rosMgmtCpuTotalProcNum = _RosMgmtCpuTotalProcNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1, 1),
    _RosMgmtCpuTotalProcNum_Type()
)
rosMgmtCpuTotalProcNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCpuTotalProcNum.setStatus("current")


class _RosMgmtCpuHistoryTableSize_Type(Integer32):
    """Custom type rosMgmtCpuHistoryTableSize based on Integer32"""
    defaultValue = 60


_RosMgmtCpuHistoryTableSize_Type.__name__ = "Integer32"
_RosMgmtCpuHistoryTableSize_Object = MibScalar
rosMgmtCpuHistoryTableSize = _RosMgmtCpuHistoryTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1, 2),
    _RosMgmtCpuHistoryTableSize_Type()
)
rosMgmtCpuHistoryTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryTableSize.setStatus("current")
_RosMgmtCpuThresholdTrapEnable_Type = EnableVar
_RosMgmtCpuThresholdTrapEnable_Object = MibScalar
rosMgmtCpuThresholdTrapEnable = _RosMgmtCpuThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1, 3),
    _RosMgmtCpuThresholdTrapEnable_Type()
)
rosMgmtCpuThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtCpuThresholdTrapEnable.setStatus("deprecated")


class _RosMgmtCpuRisingThresholdValue_Type(Integer32):
    """Custom type rosMgmtCpuRisingThresholdValue based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 99),
    )


_RosMgmtCpuRisingThresholdValue_Type.__name__ = "Integer32"
_RosMgmtCpuRisingThresholdValue_Object = MibScalar
rosMgmtCpuRisingThresholdValue = _RosMgmtCpuRisingThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1, 4),
    _RosMgmtCpuRisingThresholdValue_Type()
)
rosMgmtCpuRisingThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtCpuRisingThresholdValue.setStatus("current")


class _RosMgmtCpuRecoverThresholdValue_Type(Integer32):
    """Custom type rosMgmtCpuRecoverThresholdValue based on Integer32"""
    defaultValue = 79

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 98),
    )


_RosMgmtCpuRecoverThresholdValue_Type.__name__ = "Integer32"
_RosMgmtCpuRecoverThresholdValue_Object = MibScalar
rosMgmtCpuRecoverThresholdValue = _RosMgmtCpuRecoverThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1, 5),
    _RosMgmtCpuRecoverThresholdValue_Type()
)
rosMgmtCpuRecoverThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtCpuRecoverThresholdValue.setStatus("current")


class _RosMgmtCpuThresholdInterval_Type(Integer32):
    """Custom type rosMgmtCpuThresholdInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 36000),
    )


_RosMgmtCpuThresholdInterval_Type.__name__ = "Integer32"
_RosMgmtCpuThresholdInterval_Object = MibScalar
rosMgmtCpuThresholdInterval = _RosMgmtCpuThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1, 6),
    _RosMgmtCpuThresholdInterval_Type()
)
rosMgmtCpuThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtCpuThresholdInterval.setStatus("current")
_RosMgmtCpuNum_Type = Integer32
_RosMgmtCpuNum_Object = MibScalar
rosMgmtCpuNum = _RosMgmtCpuNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 1, 7),
    _RosMgmtCpuNum_Type()
)
rosMgmtCpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCpuNum.setStatus("current")
_RosMgmtCpuTableGroup_ObjectIdentity = ObjectIdentity
rosMgmtCpuTableGroup = _RosMgmtCpuTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2)
)
_RosMgmtCpuUtilizationGroup_ObjectIdentity = ObjectIdentity
rosMgmtCpuUtilizationGroup = _RosMgmtCpuUtilizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1)
)
_RosMgmtCpuUtilizationTable_Object = MibTable
rosMgmtCpuUtilizationTable = _RosMgmtCpuUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rosMgmtCpuUtilizationTable.setStatus("current")
_RosMgmtCpuUtilizationEntry_Object = MibTableRow
rosMgmtCpuUtilizationEntry = _RosMgmtCpuUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 1, 1)
)
rosMgmtCpuUtilizationEntry.setIndexNames(
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtCpuUtilizationPeriod"),
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtCpuUtilizationCpuIdx"),
)
if mibBuilder.loadTexts:
    rosMgmtCpuUtilizationEntry.setStatus("current")


class _RosMgmtCpuUtilizationPeriod_Type(Integer32):
    """Custom type rosMgmtCpuUtilizationPeriod based on Integer32"""
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
        *(("oneSec", 1),
          ("fiveSec", 2),
          ("oneMin", 3),
          ("tenMin", 4),
          ("twoHour", 5))
    )


_RosMgmtCpuUtilizationPeriod_Type.__name__ = "Integer32"
_RosMgmtCpuUtilizationPeriod_Object = MibTableColumn
rosMgmtCpuUtilizationPeriod = _RosMgmtCpuUtilizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 1, 1, 1),
    _RosMgmtCpuUtilizationPeriod_Type()
)
rosMgmtCpuUtilizationPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtCpuUtilizationPeriod.setStatus("current")


class _RosMgmtCpuUtilizationCpuIdx_Type(Integer32):
    """Custom type rosMgmtCpuUtilizationCpuIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RosMgmtCpuUtilizationCpuIdx_Type.__name__ = "Integer32"
_RosMgmtCpuUtilizationCpuIdx_Object = MibTableColumn
rosMgmtCpuUtilizationCpuIdx = _RosMgmtCpuUtilizationCpuIdx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 1, 1, 2),
    _RosMgmtCpuUtilizationCpuIdx_Type()
)
rosMgmtCpuUtilizationCpuIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCpuUtilizationCpuIdx.setStatus("current")
_RosMgmtCpuUtilization_Type = Integer32
_RosMgmtCpuUtilization_Object = MibTableColumn
rosMgmtCpuUtilization = _RosMgmtCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 1, 1, 3),
    _RosMgmtCpuUtilization_Type()
)
rosMgmtCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtCpuUtilization.setUnits("percent")
_RosMgmtTotalCPUUtilizationTable_Object = MibTable
rosMgmtTotalCPUUtilizationTable = _RosMgmtTotalCPUUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rosMgmtTotalCPUUtilizationTable.setStatus("current")
_RosMgmtTotalCPUUtilizationEntry_Object = MibTableRow
rosMgmtTotalCPUUtilizationEntry = _RosMgmtTotalCPUUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 2, 1)
)
rosMgmtTotalCPUUtilizationEntry.setIndexNames(
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtTotalCPUPeriod"),
)
if mibBuilder.loadTexts:
    rosMgmtTotalCPUUtilizationEntry.setStatus("current")


class _RosMgmtTotalCPUPeriod_Type(Integer32):
    """Custom type rosMgmtTotalCPUPeriod based on Integer32"""
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
        *(("oneSec", 1),
          ("fiveSec", 2),
          ("oneMin", 3),
          ("tenMin", 4),
          ("twoHour", 5))
    )


_RosMgmtTotalCPUPeriod_Type.__name__ = "Integer32"
_RosMgmtTotalCPUPeriod_Object = MibTableColumn
rosMgmtTotalCPUPeriod = _RosMgmtTotalCPUPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 2, 1, 1),
    _RosMgmtTotalCPUPeriod_Type()
)
rosMgmtTotalCPUPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtTotalCPUPeriod.setStatus("current")


class _RosMgmtTotalCPUUtilization_Type(Integer32):
    """Custom type rosMgmtTotalCPUUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RosMgmtTotalCPUUtilization_Type.__name__ = "Integer32"
_RosMgmtTotalCPUUtilization_Object = MibTableColumn
rosMgmtTotalCPUUtilization = _RosMgmtTotalCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 2, 1, 2),
    _RosMgmtTotalCPUUtilization_Type()
)
rosMgmtTotalCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtTotalCPUUtilization.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtTotalCPUUtilization.setUnits("percent")
_RosMgmtCpuHistoryTable_Object = MibTable
rosMgmtCpuHistoryTable = _RosMgmtCpuHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryTable.setStatus("current")
_RosMgmtCpuHistoryEntry_Object = MibTableRow
rosMgmtCpuHistoryEntry = _RosMgmtCpuHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 3, 1)
)
rosMgmtCpuHistoryEntry.setIndexNames(
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtCpuHistoryPeriod"),
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtCpuHistoryIndex"),
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtCpuHistoryCpuIdx"),
)
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryEntry.setStatus("current")


class _RosMgmtCpuHistoryPeriod_Type(Integer32):
    """Custom type rosMgmtCpuHistoryPeriod based on Integer32"""
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
        *(("fiveSec", 1),
          ("oneMin", 2),
          ("tenMin", 3),
          ("twoHour", 4))
    )


_RosMgmtCpuHistoryPeriod_Type.__name__ = "Integer32"
_RosMgmtCpuHistoryPeriod_Object = MibTableColumn
rosMgmtCpuHistoryPeriod = _RosMgmtCpuHistoryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 3, 1, 1),
    _RosMgmtCpuHistoryPeriod_Type()
)
rosMgmtCpuHistoryPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryPeriod.setStatus("current")


class _RosMgmtCpuHistoryIndex_Type(Integer32):
    """Custom type rosMgmtCpuHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RosMgmtCpuHistoryIndex_Type.__name__ = "Integer32"
_RosMgmtCpuHistoryIndex_Object = MibTableColumn
rosMgmtCpuHistoryIndex = _RosMgmtCpuHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 3, 1, 2),
    _RosMgmtCpuHistoryIndex_Type()
)
rosMgmtCpuHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryIndex.setStatus("current")


class _RosMgmtCpuHistoryCpuIdx_Type(Integer32):
    """Custom type rosMgmtCpuHistoryCpuIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RosMgmtCpuHistoryCpuIdx_Type.__name__ = "Integer32"
_RosMgmtCpuHistoryCpuIdx_Object = MibTableColumn
rosMgmtCpuHistoryCpuIdx = _RosMgmtCpuHistoryCpuIdx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 3, 1, 3),
    _RosMgmtCpuHistoryCpuIdx_Type()
)
rosMgmtCpuHistoryCpuIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryCpuIdx.setStatus("current")
_RosMgmtCpuHistoryUtil_Type = Integer32
_RosMgmtCpuHistoryUtil_Object = MibTableColumn
rosMgmtCpuHistoryUtil = _RosMgmtCpuHistoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 3, 1, 4),
    _RosMgmtCpuHistoryUtil_Type()
)
rosMgmtCpuHistoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryUtil.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtCpuHistoryUtil.setUnits("percent")
_RosMgmtTotalCPUHistoryTable_Object = MibTable
rosMgmtTotalCPUHistoryTable = _RosMgmtTotalCPUHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rosMgmtTotalCPUHistoryTable.setStatus("current")
_RosMgmtTotalCPUHistoryEntry_Object = MibTableRow
rosMgmtTotalCPUHistoryEntry = _RosMgmtTotalCPUHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 4, 1)
)
rosMgmtTotalCPUHistoryEntry.setIndexNames(
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtTotalCPUHistoryPeriod"),
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtTotalCPUHistoryIndex"),
)
if mibBuilder.loadTexts:
    rosMgmtTotalCPUHistoryEntry.setStatus("current")


class _RosMgmtTotalCPUHistoryPeriod_Type(Integer32):
    """Custom type rosMgmtTotalCPUHistoryPeriod based on Integer32"""
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
        *(("fiveSec", 1),
          ("oneMin", 2),
          ("tenMin", 3),
          ("twoHour", 4))
    )


_RosMgmtTotalCPUHistoryPeriod_Type.__name__ = "Integer32"
_RosMgmtTotalCPUHistoryPeriod_Object = MibTableColumn
rosMgmtTotalCPUHistoryPeriod = _RosMgmtTotalCPUHistoryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 4, 1, 1),
    _RosMgmtTotalCPUHistoryPeriod_Type()
)
rosMgmtTotalCPUHistoryPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtTotalCPUHistoryPeriod.setStatus("current")


class _RosMgmtTotalCPUHistoryIndex_Type(Integer32):
    """Custom type rosMgmtTotalCPUHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RosMgmtTotalCPUHistoryIndex_Type.__name__ = "Integer32"
_RosMgmtTotalCPUHistoryIndex_Object = MibTableColumn
rosMgmtTotalCPUHistoryIndex = _RosMgmtTotalCPUHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 4, 1, 2),
    _RosMgmtTotalCPUHistoryIndex_Type()
)
rosMgmtTotalCPUHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtTotalCPUHistoryIndex.setStatus("current")
_RosMgmtTotalCPUHistoryUtil_Type = Integer32
_RosMgmtTotalCPUHistoryUtil_Object = MibTableColumn
rosMgmtTotalCPUHistoryUtil = _RosMgmtTotalCPUHistoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 1, 4, 1, 3),
    _RosMgmtTotalCPUHistoryUtil_Type()
)
rosMgmtTotalCPUHistoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtTotalCPUHistoryUtil.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtTotalCPUHistoryUtil.setUnits("percent")
_RosMgmtCpuProcessesGroup_ObjectIdentity = ObjectIdentity
rosMgmtCpuProcessesGroup = _RosMgmtCpuProcessesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2)
)
_RosMgmtProcessesTable_Object = MibTable
rosMgmtProcessesTable = _RosMgmtProcessesTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rosMgmtProcessesTable.setStatus("current")
_RosMgmtProcessesEntry_Object = MibTableRow
rosMgmtProcessesEntry = _RosMgmtProcessesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1)
)
rosMgmtProcessesEntry.setIndexNames(
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtProcessIndex"),
)
if mibBuilder.loadTexts:
    rosMgmtProcessesEntry.setStatus("current")


class _RosMgmtProcessIndex_Type(Integer32):
    """Custom type rosMgmtProcessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RosMgmtProcessIndex_Type.__name__ = "Integer32"
_RosMgmtProcessIndex_Object = MibTableColumn
rosMgmtProcessIndex = _RosMgmtProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 1),
    _RosMgmtProcessIndex_Type()
)
rosMgmtProcessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessIndex.setStatus("current")
_RosMgmtProcessPID_Type = Integer32
_RosMgmtProcessPID_Object = MibTableColumn
rosMgmtProcessPID = _RosMgmtProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 2),
    _RosMgmtProcessPID_Type()
)
rosMgmtProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessPID.setStatus("current")


class _RosMgmtProcessName_Type(OctetString):
    """Custom type rosMgmtProcessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RosMgmtProcessName_Type.__name__ = "OctetString"
_RosMgmtProcessName_Object = MibTableColumn
rosMgmtProcessName = _RosMgmtProcessName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 3),
    _RosMgmtProcessName_Type()
)
rosMgmtProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessName.setStatus("current")
_RosMgmtProcessRunTimeTotal_Type = CPUTimeStamp
_RosMgmtProcessRunTimeTotal_Object = MibTableColumn
rosMgmtProcessRunTimeTotal = _RosMgmtProcessRunTimeTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 4),
    _RosMgmtProcessRunTimeTotal_Type()
)
rosMgmtProcessRunTimeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessRunTimeTotal.setStatus("current")
_RosMgmtProcessInvokedTotal_Type = Integer32
_RosMgmtProcessInvokedTotal_Object = MibTableColumn
rosMgmtProcessInvokedTotal = _RosMgmtProcessInvokedTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 5),
    _RosMgmtProcessInvokedTotal_Type()
)
rosMgmtProcessInvokedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessInvokedTotal.setStatus("current")
_RosMgmtProcessTimeCreated_Type = TimeStamp
_RosMgmtProcessTimeCreated_Object = MibTableColumn
rosMgmtProcessTimeCreated = _RosMgmtProcessTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 6),
    _RosMgmtProcessTimeCreated_Type()
)
rosMgmtProcessTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessTimeCreated.setStatus("current")
_RosMgmtProcessCurrentPriority_Type = Integer32
_RosMgmtProcessCurrentPriority_Object = MibTableColumn
rosMgmtProcessCurrentPriority = _RosMgmtProcessCurrentPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 7),
    _RosMgmtProcessCurrentPriority_Type()
)
rosMgmtProcessCurrentPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessCurrentPriority.setStatus("current")
_RosMgmtProcessStatus_Type = ProcessStatus
_RosMgmtProcessStatus_Object = MibTableColumn
rosMgmtProcessStatus = _RosMgmtProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 1, 1, 8),
    _RosMgmtProcessStatus_Type()
)
rosMgmtProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessStatus.setStatus("current")
_RosMgmtProcessStatisticsTable_Object = MibTable
rosMgmtProcessStatisticsTable = _RosMgmtProcessStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rosMgmtProcessStatisticsTable.setStatus("current")
_RosMgmtProcessStatisticsEntry_Object = MibTableRow
rosMgmtProcessStatisticsEntry = _RosMgmtProcessStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 2, 1)
)
rosMgmtProcessStatisticsEntry.setIndexNames(
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtProcessIndex"),
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtProcessStatisticsPeriod"),
)
if mibBuilder.loadTexts:
    rosMgmtProcessStatisticsEntry.setStatus("current")


class _RosMgmtProcessStatisticsPeriod_Type(Integer32):
    """Custom type rosMgmtProcessStatisticsPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiveSec", 1),
          ("oneMin", 2),
          ("tenMin", 3))
    )


_RosMgmtProcessStatisticsPeriod_Type.__name__ = "Integer32"
_RosMgmtProcessStatisticsPeriod_Object = MibTableColumn
rosMgmtProcessStatisticsPeriod = _RosMgmtProcessStatisticsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 2, 1, 1),
    _RosMgmtProcessStatisticsPeriod_Type()
)
rosMgmtProcessStatisticsPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtProcessStatisticsPeriod.setStatus("current")
_RosMgmtProcessRunTime_Type = CPUTimeStamp
_RosMgmtProcessRunTime_Object = MibTableColumn
rosMgmtProcessRunTime = _RosMgmtProcessRunTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 2, 1, 2),
    _RosMgmtProcessRunTime_Type()
)
rosMgmtProcessRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessRunTime.setStatus("current")
_RosMgmtProcessUtilization_Type = Integer32
_RosMgmtProcessUtilization_Object = MibTableColumn
rosMgmtProcessUtilization = _RosMgmtProcessUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 2, 1, 3),
    _RosMgmtProcessUtilization_Type()
)
rosMgmtProcessUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtProcessUtilization.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtProcessUtilization.setUnits("percent")
_RosMgmtDeadProcessesTable_Object = MibTable
rosMgmtDeadProcessesTable = _RosMgmtDeadProcessesTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rosMgmtDeadProcessesTable.setStatus("current")
_RosMgmtDeadProcessesEntry_Object = MibTableRow
rosMgmtDeadProcessesEntry = _RosMgmtDeadProcessesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3, 1)
)
rosMgmtDeadProcessesEntry.setIndexNames(
    (0, "ROSMGMT-SYSTEM-MIB", "rosMgmtDeadProcessIndex"),
)
if mibBuilder.loadTexts:
    rosMgmtDeadProcessesEntry.setStatus("current")


class _RosMgmtDeadProcessIndex_Type(Integer32):
    """Custom type rosMgmtDeadProcessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RosMgmtDeadProcessIndex_Type.__name__ = "Integer32"
_RosMgmtDeadProcessIndex_Object = MibTableColumn
rosMgmtDeadProcessIndex = _RosMgmtDeadProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3, 1, 1),
    _RosMgmtDeadProcessIndex_Type()
)
rosMgmtDeadProcessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtDeadProcessIndex.setStatus("current")


class _RosMgmtDeadProcessName_Type(OctetString):
    """Custom type rosMgmtDeadProcessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RosMgmtDeadProcessName_Type.__name__ = "OctetString"
_RosMgmtDeadProcessName_Object = MibTableColumn
rosMgmtDeadProcessName = _RosMgmtDeadProcessName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3, 1, 2),
    _RosMgmtDeadProcessName_Type()
)
rosMgmtDeadProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtDeadProcessName.setStatus("current")
_RosMgmtDeadProcessPriority_Type = Integer32
_RosMgmtDeadProcessPriority_Object = MibTableColumn
rosMgmtDeadProcessPriority = _RosMgmtDeadProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3, 1, 3),
    _RosMgmtDeadProcessPriority_Type()
)
rosMgmtDeadProcessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtDeadProcessPriority.setStatus("current")
_RosMgmtDeadProcessTimeDelete_Type = TimeStamp
_RosMgmtDeadProcessTimeDelete_Object = MibTableColumn
rosMgmtDeadProcessTimeDelete = _RosMgmtDeadProcessTimeDelete_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3, 1, 4),
    _RosMgmtDeadProcessTimeDelete_Type()
)
rosMgmtDeadProcessTimeDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtDeadProcessTimeDelete.setStatus("current")
_RosMgmtDeadProcessDeadTimes_Type = Integer32
_RosMgmtDeadProcessDeadTimes_Object = MibTableColumn
rosMgmtDeadProcessDeadTimes = _RosMgmtDeadProcessDeadTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3, 1, 5),
    _RosMgmtDeadProcessDeadTimes_Type()
)
rosMgmtDeadProcessDeadTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtDeadProcessDeadTimes.setStatus("current")
_RosMgmtDeadProcessStatus_Type = ProcessStatus
_RosMgmtDeadProcessStatus_Object = MibTableColumn
rosMgmtDeadProcessStatus = _RosMgmtDeadProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 1, 2, 2, 3, 1, 6),
    _RosMgmtDeadProcessStatus_Type()
)
rosMgmtDeadProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtDeadProcessStatus.setStatus("current")
_RosMgmtCpuConformance_ObjectIdentity = ObjectIdentity
rosMgmtCpuConformance = _RosMgmtCpuConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 2)
)

# Managed Objects groups


# Notification objects

rosMgmtCpuRisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 0, 1)
)
rosMgmtCpuRisingThreshold.setObjects(
      *(("ROSMGMT-SYSTEM-MIB", "rosMgmtProcessIndex"),
        ("ROSMGMT-SYSTEM-MIB", "rosMgmtProcessUtilization"),
        ("ROSMGMT-SYSTEM-MIB", "rosMgmtCpuUtilizationCpuIdx"),
        ("ROSMGMT-SYSTEM-MIB", "rosMgmtCpuUtilization"))
)
if mibBuilder.loadTexts:
    rosMgmtCpuRisingThreshold.setStatus(
        "current"
    )

rosMgmtCpuRisingThresholdRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 1, 1, 0, 2)
)
rosMgmtCpuRisingThresholdRecover.setObjects(
      *(("ROSMGMT-SYSTEM-MIB", "rosMgmtCpuUtilizationCpuIdx"),
        ("ROSMGMT-SYSTEM-MIB", "rosMgmtCpuUtilization"))
)
if mibBuilder.loadTexts:
    rosMgmtCpuRisingThresholdRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROSMGMT-SYSTEM-MIB",
    **{"ProcessStatus": ProcessStatus,
       "CPUTimeStamp": CPUTimeStamp,
       "rosMgmtSystem": rosMgmtSystem,
       "rosMgmtCpu": rosMgmtCpu,
       "rosMgmtCpuNotifications": rosMgmtCpuNotifications,
       "rosMgmtCpuRisingThreshold": rosMgmtCpuRisingThreshold,
       "rosMgmtCpuRisingThresholdRecover": rosMgmtCpuRisingThresholdRecover,
       "rosMgmtCpuObjects": rosMgmtCpuObjects,
       "rosMgmtCpuScalarGroup": rosMgmtCpuScalarGroup,
       "rosMgmtCpuTotalProcNum": rosMgmtCpuTotalProcNum,
       "rosMgmtCpuHistoryTableSize": rosMgmtCpuHistoryTableSize,
       "rosMgmtCpuThresholdTrapEnable": rosMgmtCpuThresholdTrapEnable,
       "rosMgmtCpuRisingThresholdValue": rosMgmtCpuRisingThresholdValue,
       "rosMgmtCpuRecoverThresholdValue": rosMgmtCpuRecoverThresholdValue,
       "rosMgmtCpuThresholdInterval": rosMgmtCpuThresholdInterval,
       "rosMgmtCpuNum": rosMgmtCpuNum,
       "rosMgmtCpuTableGroup": rosMgmtCpuTableGroup,
       "rosMgmtCpuUtilizationGroup": rosMgmtCpuUtilizationGroup,
       "rosMgmtCpuUtilizationTable": rosMgmtCpuUtilizationTable,
       "rosMgmtCpuUtilizationEntry": rosMgmtCpuUtilizationEntry,
       "rosMgmtCpuUtilizationPeriod": rosMgmtCpuUtilizationPeriod,
       "rosMgmtCpuUtilizationCpuIdx": rosMgmtCpuUtilizationCpuIdx,
       "rosMgmtCpuUtilization": rosMgmtCpuUtilization,
       "rosMgmtTotalCPUUtilizationTable": rosMgmtTotalCPUUtilizationTable,
       "rosMgmtTotalCPUUtilizationEntry": rosMgmtTotalCPUUtilizationEntry,
       "rosMgmtTotalCPUPeriod": rosMgmtTotalCPUPeriod,
       "rosMgmtTotalCPUUtilization": rosMgmtTotalCPUUtilization,
       "rosMgmtCpuHistoryTable": rosMgmtCpuHistoryTable,
       "rosMgmtCpuHistoryEntry": rosMgmtCpuHistoryEntry,
       "rosMgmtCpuHistoryPeriod": rosMgmtCpuHistoryPeriod,
       "rosMgmtCpuHistoryIndex": rosMgmtCpuHistoryIndex,
       "rosMgmtCpuHistoryCpuIdx": rosMgmtCpuHistoryCpuIdx,
       "rosMgmtCpuHistoryUtil": rosMgmtCpuHistoryUtil,
       "rosMgmtTotalCPUHistoryTable": rosMgmtTotalCPUHistoryTable,
       "rosMgmtTotalCPUHistoryEntry": rosMgmtTotalCPUHistoryEntry,
       "rosMgmtTotalCPUHistoryPeriod": rosMgmtTotalCPUHistoryPeriod,
       "rosMgmtTotalCPUHistoryIndex": rosMgmtTotalCPUHistoryIndex,
       "rosMgmtTotalCPUHistoryUtil": rosMgmtTotalCPUHistoryUtil,
       "rosMgmtCpuProcessesGroup": rosMgmtCpuProcessesGroup,
       "rosMgmtProcessesTable": rosMgmtProcessesTable,
       "rosMgmtProcessesEntry": rosMgmtProcessesEntry,
       "rosMgmtProcessIndex": rosMgmtProcessIndex,
       "rosMgmtProcessPID": rosMgmtProcessPID,
       "rosMgmtProcessName": rosMgmtProcessName,
       "rosMgmtProcessRunTimeTotal": rosMgmtProcessRunTimeTotal,
       "rosMgmtProcessInvokedTotal": rosMgmtProcessInvokedTotal,
       "rosMgmtProcessTimeCreated": rosMgmtProcessTimeCreated,
       "rosMgmtProcessCurrentPriority": rosMgmtProcessCurrentPriority,
       "rosMgmtProcessStatus": rosMgmtProcessStatus,
       "rosMgmtProcessStatisticsTable": rosMgmtProcessStatisticsTable,
       "rosMgmtProcessStatisticsEntry": rosMgmtProcessStatisticsEntry,
       "rosMgmtProcessStatisticsPeriod": rosMgmtProcessStatisticsPeriod,
       "rosMgmtProcessRunTime": rosMgmtProcessRunTime,
       "rosMgmtProcessUtilization": rosMgmtProcessUtilization,
       "rosMgmtDeadProcessesTable": rosMgmtDeadProcessesTable,
       "rosMgmtDeadProcessesEntry": rosMgmtDeadProcessesEntry,
       "rosMgmtDeadProcessIndex": rosMgmtDeadProcessIndex,
       "rosMgmtDeadProcessName": rosMgmtDeadProcessName,
       "rosMgmtDeadProcessPriority": rosMgmtDeadProcessPriority,
       "rosMgmtDeadProcessTimeDelete": rosMgmtDeadProcessTimeDelete,
       "rosMgmtDeadProcessDeadTimes": rosMgmtDeadProcessDeadTimes,
       "rosMgmtDeadProcessStatus": rosMgmtDeadProcessStatus,
       "rosMgmtCpuConformance": rosMgmtCpuConformance}
)
