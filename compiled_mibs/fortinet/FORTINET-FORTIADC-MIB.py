# SNMP MIB module (FORTINET-FORTIADC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIADC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:46 2025
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

(FnBoolState,
 FnIndex,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "fortinet")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName",
    "sysUpTime")

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

fnFortiADCMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FadcHAModeVal(TextualConvention, Integer32):
    status = "current"
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
        *(("standalone", 1),
          ("activePassive", 2),
          ("activeActive", 3),
          ("activeActiveVrrp", 4))
    )



class FadcVdIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FadcHaState(TextualConvention, Integer32):
    status = "current"
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
        *(("master", 1),
          ("backup", 2),
          ("standalone", 3),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_FadcTraps_ObjectIdentity = ObjectIdentity
fadcTraps = _FadcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0)
)
_FadcSystem_ObjectIdentity = ObjectIdentity
fadcSystem = _FadcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1)
)


class _FadcSysModel_Type(DisplayString):
    """Custom type fadcSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FadcSysModel_Type.__name__ = "DisplayString"
_FadcSysModel_Object = MibScalar
fadcSysModel = _FadcSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 1),
    _FadcSysModel_Type()
)
fadcSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysModel.setStatus("current")


class _FadcSysSerial_Type(DisplayString):
    """Custom type fadcSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FadcSysSerial_Type.__name__ = "DisplayString"
_FadcSysSerial_Object = MibScalar
fadcSysSerial = _FadcSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 2),
    _FadcSysSerial_Type()
)
fadcSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysSerial.setStatus("current")


class _FadcSysVersion_Type(DisplayString):
    """Custom type fadcSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FadcSysVersion_Type.__name__ = "DisplayString"
_FadcSysVersion_Object = MibScalar
fadcSysVersion = _FadcSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 3),
    _FadcSysVersion_Type()
)
fadcSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysVersion.setStatus("current")
_FadcSysCpuUsage_Type = Gauge32
_FadcSysCpuUsage_Object = MibScalar
fadcSysCpuUsage = _FadcSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 4),
    _FadcSysCpuUsage_Type()
)
fadcSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysCpuUsage.setStatus("current")
_FadcSysMemUsage_Type = Gauge32
_FadcSysMemUsage_Object = MibScalar
fadcSysMemUsage = _FadcSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 5),
    _FadcSysMemUsage_Type()
)
fadcSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysMemUsage.setStatus("current")
_FadcSysLogDiskUsage_Type = Gauge32
_FadcSysLogDiskUsage_Object = MibScalar
fadcSysLogDiskUsage = _FadcSysLogDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 6),
    _FadcSysLogDiskUsage_Type()
)
fadcSysLogDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysLogDiskUsage.setStatus("current")
_FadcSysLoad_Type = Gauge32
_FadcSysLoad_Object = MibScalar
fadcSysLoad = _FadcSysLoad_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 30),
    _FadcSysLoad_Type()
)
fadcSysLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysLoad.setStatus("current")
_FadcSysCpuUsageTable_Object = MibTable
fadcSysCpuUsageTable = _FadcSysCpuUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 40)
)
if mibBuilder.loadTexts:
    fadcSysCpuUsageTable.setStatus("current")
_FadcSysCpuUsageEntry_Object = MibTableRow
fadcSysCpuUsageEntry = _FadcSysCpuUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 40, 1)
)
fadcSysCpuUsageEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcCpuIndex"),
)
if mibBuilder.loadTexts:
    fadcSysCpuUsageEntry.setStatus("current")
_FadcCpuIndex_Type = FnIndex
_FadcCpuIndex_Object = MibTableColumn
fadcCpuIndex = _FadcCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 40, 1, 1),
    _FadcCpuIndex_Type()
)
fadcCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcCpuIndex.setStatus("current")
_FadcCpuName_Type = DisplayString
_FadcCpuName_Object = MibTableColumn
fadcCpuName = _FadcCpuName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 40, 1, 2),
    _FadcCpuName_Type()
)
fadcCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCpuName.setStatus("current")
_FadcCpu2secAvgUsage_Type = Gauge32
_FadcCpu2secAvgUsage_Object = MibTableColumn
fadcCpu2secAvgUsage = _FadcCpu2secAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 40, 1, 3),
    _FadcCpu2secAvgUsage_Type()
)
fadcCpu2secAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCpu2secAvgUsage.setStatus("current")
_FadcCpu1minAvgUsage_Type = Gauge32
_FadcCpu1minAvgUsage_Object = MibTableColumn
fadcCpu1minAvgUsage = _FadcCpu1minAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 40, 1, 4),
    _FadcCpu1minAvgUsage_Type()
)
fadcCpu1minAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCpu1minAvgUsage.setStatus("current")
_FadcCpu5minAvgUsage_Type = Gauge32
_FadcCpu5minAvgUsage_Object = MibTableColumn
fadcCpu5minAvgUsage = _FadcCpu5minAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 40, 1, 5),
    _FadcCpu5minAvgUsage_Type()
)
fadcCpu5minAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCpu5minAvgUsage.setStatus("current")
_FadcSysOptions_ObjectIdentity = ObjectIdentity
fadcSysOptions = _FadcSysOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 101)
)
_FadcSysOptIdleTimeout_Type = Integer32
_FadcSysOptIdleTimeout_Object = MibScalar
fadcSysOptIdleTimeout = _FadcSysOptIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 101, 1),
    _FadcSysOptIdleTimeout_Type()
)
fadcSysOptIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSysOptIdleTimeout.setStatus("current")
_FadcSysHA_ObjectIdentity = ObjectIdentity
fadcSysHA = _FadcSysHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 200)
)
_FadcHAMode_Type = FadcHAModeVal
_FadcHAMode_Object = MibScalar
fadcHAMode = _FadcHAMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 200, 1),
    _FadcHAMode_Type()
)
fadcHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHAMode.setStatus("current")
_FadcSysAlert_ObjectIdentity = ObjectIdentity
fadcSysAlert = _FadcSysAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300)
)
_FadcSysAlertTable_Object = MibTable
fadcSysAlertTable = _FadcSysAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1)
)
if mibBuilder.loadTexts:
    fadcSysAlertTable.setStatus("current")
_FadcSysAlertEntry_Object = MibTableRow
fadcSysAlertEntry = _FadcSysAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1, 1)
)
fadcSysAlertEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcAlertIndex"),
)
if mibBuilder.loadTexts:
    fadcSysAlertEntry.setStatus("current")
_FadcAlertIndex_Type = FnIndex
_FadcAlertIndex_Object = MibTableColumn
fadcAlertIndex = _FadcAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1, 1, 1),
    _FadcAlertIndex_Type()
)
fadcAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcAlertIndex.setStatus("current")
_FadcAlertName_Type = DisplayString
_FadcAlertName_Object = MibTableColumn
fadcAlertName = _FadcAlertName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1, 1, 2),
    _FadcAlertName_Type()
)
fadcAlertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAlertName.setStatus("current")


class _FadcAlertSourceType_Type(Integer32):
    """Custom type fadcAlertSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("event", 1),
          ("metric", 2))
    )


_FadcAlertSourceType_Type.__name__ = "Integer32"
_FadcAlertSourceType_Object = MibTableColumn
fadcAlertSourceType = _FadcAlertSourceType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1, 1, 3),
    _FadcAlertSourceType_Type()
)
fadcAlertSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAlertSourceType.setStatus("current")


class _FadcAlertPriority_Type(Integer32):
    """Custom type fadcAlertPriority based on Integer32"""
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
          ("middle", 2),
          ("low", 3))
    )


_FadcAlertPriority_Type.__name__ = "Integer32"
_FadcAlertPriority_Object = MibTableColumn
fadcAlertPriority = _FadcAlertPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1, 1, 4),
    _FadcAlertPriority_Type()
)
fadcAlertPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAlertPriority.setStatus("current")
_FadcAlertComments_Type = DisplayString
_FadcAlertComments_Object = MibTableColumn
fadcAlertComments = _FadcAlertComments_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1, 1, 5),
    _FadcAlertComments_Type()
)
fadcAlertComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAlertComments.setStatus("current")
_FadcAlertVdomName_Type = DisplayString
_FadcAlertVdomName_Object = MibTableColumn
fadcAlertVdomName = _FadcAlertVdomName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 300, 1, 1, 6),
    _FadcAlertVdomName_Type()
)
fadcAlertVdomName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAlertVdomName.setStatus("current")
_FadcSysCert_ObjectIdentity = ObjectIdentity
fadcSysCert = _FadcSysCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400)
)
_FadcLocalCertTables_ObjectIdentity = ObjectIdentity
fadcLocalCertTables = _FadcLocalCertTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1)
)
_FadcLocalCertTable_Object = MibTable
fadcLocalCertTable = _FadcLocalCertTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1, 1)
)
if mibBuilder.loadTexts:
    fadcLocalCertTable.setStatus("current")
_FadcLocalCertEntry_Object = MibTableRow
fadcLocalCertEntry = _FadcLocalCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1, 1, 1)
)
fadcLocalCertEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcLocalCertIndex"),
)
if mibBuilder.loadTexts:
    fadcLocalCertEntry.setStatus("current")
_FadcLocalCertIndex_Type = FnIndex
_FadcLocalCertIndex_Object = MibTableColumn
fadcLocalCertIndex = _FadcLocalCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1, 1, 1, 1),
    _FadcLocalCertIndex_Type()
)
fadcLocalCertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcLocalCertIndex.setStatus("current")
_FadcLocalCertName_Type = DisplayString
_FadcLocalCertName_Object = MibTableColumn
fadcLocalCertName = _FadcLocalCertName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1, 1, 1, 2),
    _FadcLocalCertName_Type()
)
fadcLocalCertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLocalCertName.setStatus("current")
_FadcLocalCertValidFrom_Type = DisplayString
_FadcLocalCertValidFrom_Object = MibTableColumn
fadcLocalCertValidFrom = _FadcLocalCertValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1, 1, 1, 3),
    _FadcLocalCertValidFrom_Type()
)
fadcLocalCertValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLocalCertValidFrom.setStatus("current")
_FadcLocalCertValidTo_Type = DisplayString
_FadcLocalCertValidTo_Object = MibTableColumn
fadcLocalCertValidTo = _FadcLocalCertValidTo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1, 1, 1, 4),
    _FadcLocalCertValidTo_Type()
)
fadcLocalCertValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLocalCertValidTo.setStatus("current")
_FadcLocalCertVdom_Type = DisplayString
_FadcLocalCertVdom_Object = MibTableColumn
fadcLocalCertVdom = _FadcLocalCertVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 1, 1, 1, 5),
    _FadcLocalCertVdom_Type()
)
fadcLocalCertVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLocalCertVdom.setStatus("current")
_FadcIntermediateCATables_ObjectIdentity = ObjectIdentity
fadcIntermediateCATables = _FadcIntermediateCATables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2)
)
_FadcIntermediateCATable_Object = MibTable
fadcIntermediateCATable = _FadcIntermediateCATable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2, 1)
)
if mibBuilder.loadTexts:
    fadcIntermediateCATable.setStatus("current")
_FadcIntermediateCAEntry_Object = MibTableRow
fadcIntermediateCAEntry = _FadcIntermediateCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2, 1, 1)
)
fadcIntermediateCAEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcIntermediateCAIndex"),
)
if mibBuilder.loadTexts:
    fadcIntermediateCAEntry.setStatus("current")
_FadcIntermediateCAIndex_Type = FnIndex
_FadcIntermediateCAIndex_Object = MibTableColumn
fadcIntermediateCAIndex = _FadcIntermediateCAIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2, 1, 1, 1),
    _FadcIntermediateCAIndex_Type()
)
fadcIntermediateCAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcIntermediateCAIndex.setStatus("current")
_FadcIntermediateCAName_Type = DisplayString
_FadcIntermediateCAName_Object = MibTableColumn
fadcIntermediateCAName = _FadcIntermediateCAName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2, 1, 1, 2),
    _FadcIntermediateCAName_Type()
)
fadcIntermediateCAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntermediateCAName.setStatus("current")
_FadcIntermediateCAValidFrom_Type = DisplayString
_FadcIntermediateCAValidFrom_Object = MibTableColumn
fadcIntermediateCAValidFrom = _FadcIntermediateCAValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2, 1, 1, 3),
    _FadcIntermediateCAValidFrom_Type()
)
fadcIntermediateCAValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntermediateCAValidFrom.setStatus("current")
_FadcIntermediateCAValidTo_Type = DisplayString
_FadcIntermediateCAValidTo_Object = MibTableColumn
fadcIntermediateCAValidTo = _FadcIntermediateCAValidTo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2, 1, 1, 4),
    _FadcIntermediateCAValidTo_Type()
)
fadcIntermediateCAValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntermediateCAValidTo.setStatus("current")
_FadcIntermediateCAVdom_Type = DisplayString
_FadcIntermediateCAVdom_Object = MibTableColumn
fadcIntermediateCAVdom = _FadcIntermediateCAVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 2, 1, 1, 5),
    _FadcIntermediateCAVdom_Type()
)
fadcIntermediateCAVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntermediateCAVdom.setStatus("current")
_FadcCACertTables_ObjectIdentity = ObjectIdentity
fadcCACertTables = _FadcCACertTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3)
)
_FadcCACertTable_Object = MibTable
fadcCACertTable = _FadcCACertTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3, 1)
)
if mibBuilder.loadTexts:
    fadcCACertTable.setStatus("current")
_FadcCACertEntry_Object = MibTableRow
fadcCACertEntry = _FadcCACertEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3, 1, 1)
)
fadcCACertEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcCACertIndex"),
)
if mibBuilder.loadTexts:
    fadcCACertEntry.setStatus("current")
_FadcCACertIndex_Type = FnIndex
_FadcCACertIndex_Object = MibTableColumn
fadcCACertIndex = _FadcCACertIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3, 1, 1, 1),
    _FadcCACertIndex_Type()
)
fadcCACertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcCACertIndex.setStatus("current")
_FadcCACertName_Type = DisplayString
_FadcCACertName_Object = MibTableColumn
fadcCACertName = _FadcCACertName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3, 1, 1, 2),
    _FadcCACertName_Type()
)
fadcCACertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCACertName.setStatus("current")
_FadcCACertValidFrom_Type = DisplayString
_FadcCACertValidFrom_Object = MibTableColumn
fadcCACertValidFrom = _FadcCACertValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3, 1, 1, 3),
    _FadcCACertValidFrom_Type()
)
fadcCACertValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCACertValidFrom.setStatus("current")
_FadcCACertValidTo_Type = DisplayString
_FadcCACertValidTo_Object = MibTableColumn
fadcCACertValidTo = _FadcCACertValidTo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3, 1, 1, 4),
    _FadcCACertValidTo_Type()
)
fadcCACertValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCACertValidTo.setStatus("current")
_FadcCACertVdom_Type = DisplayString
_FadcCACertVdom_Object = MibTableColumn
fadcCACertVdom = _FadcCACertVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 3, 1, 1, 5),
    _FadcCACertVdom_Type()
)
fadcCACertVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCACertVdom.setStatus("current")
_FadcRemoteCertTables_ObjectIdentity = ObjectIdentity
fadcRemoteCertTables = _FadcRemoteCertTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4)
)
_FadcRemoteCertTable_Object = MibTable
fadcRemoteCertTable = _FadcRemoteCertTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4, 1)
)
if mibBuilder.loadTexts:
    fadcRemoteCertTable.setStatus("current")
_FadcRemoteCertEntry_Object = MibTableRow
fadcRemoteCertEntry = _FadcRemoteCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4, 1, 1)
)
fadcRemoteCertEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcRemoteCertIndex"),
)
if mibBuilder.loadTexts:
    fadcRemoteCertEntry.setStatus("current")
_FadcRemoteCertIndex_Type = FnIndex
_FadcRemoteCertIndex_Object = MibTableColumn
fadcRemoteCertIndex = _FadcRemoteCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4, 1, 1, 1),
    _FadcRemoteCertIndex_Type()
)
fadcRemoteCertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcRemoteCertIndex.setStatus("current")
_FadcRemoteCertName_Type = DisplayString
_FadcRemoteCertName_Object = MibTableColumn
fadcRemoteCertName = _FadcRemoteCertName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4, 1, 1, 2),
    _FadcRemoteCertName_Type()
)
fadcRemoteCertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRemoteCertName.setStatus("current")
_FadcRemoteCertValidFrom_Type = DisplayString
_FadcRemoteCertValidFrom_Object = MibTableColumn
fadcRemoteCertValidFrom = _FadcRemoteCertValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4, 1, 1, 3),
    _FadcRemoteCertValidFrom_Type()
)
fadcRemoteCertValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRemoteCertValidFrom.setStatus("current")
_FadcRemoteCertValidTo_Type = DisplayString
_FadcRemoteCertValidTo_Object = MibTableColumn
fadcRemoteCertValidTo = _FadcRemoteCertValidTo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4, 1, 1, 4),
    _FadcRemoteCertValidTo_Type()
)
fadcRemoteCertValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRemoteCertValidTo.setStatus("current")
_FadcRemoteCertVdom_Type = DisplayString
_FadcRemoteCertVdom_Object = MibTableColumn
fadcRemoteCertVdom = _FadcRemoteCertVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 1, 400, 4, 1, 1, 5),
    _FadcRemoteCertVdom_Type()
)
fadcRemoteCertVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRemoteCertVdom.setStatus("current")
_FadcVirtualDomain_ObjectIdentity = ObjectIdentity
fadcVirtualDomain = _FadcVirtualDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2)
)
_FadcVdInfo_ObjectIdentity = ObjectIdentity
fadcVdInfo = _FadcVdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 1)
)
_FadcVdNumber_Type = Integer32
_FadcVdNumber_Object = MibScalar
fadcVdNumber = _FadcVdNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 1, 1),
    _FadcVdNumber_Type()
)
fadcVdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVdNumber.setStatus("current")
_FadcVdMaxVdoms_Type = Integer32
_FadcVdMaxVdoms_Object = MibScalar
fadcVdMaxVdoms = _FadcVdMaxVdoms_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 1, 2),
    _FadcVdMaxVdoms_Type()
)
fadcVdMaxVdoms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVdMaxVdoms.setStatus("current")
_FadcVdEnabled_Type = FnBoolState
_FadcVdEnabled_Object = MibScalar
fadcVdEnabled = _FadcVdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 1, 3),
    _FadcVdEnabled_Type()
)
fadcVdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVdEnabled.setStatus("current")
_FadcVdTables_ObjectIdentity = ObjectIdentity
fadcVdTables = _FadcVdTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 2)
)
_FadcVdTable_Object = MibTable
fadcVdTable = _FadcVdTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fadcVdTable.setStatus("current")
_FadcVdEntry_Object = MibTableRow
fadcVdEntry = _FadcVdEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 2, 1, 1)
)
fadcVdEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcVdEntIndex"),
)
if mibBuilder.loadTexts:
    fadcVdEntry.setStatus("current")
_FadcVdEntIndex_Type = FadcVdIndex
_FadcVdEntIndex_Object = MibTableColumn
fadcVdEntIndex = _FadcVdEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 2, 1, 1, 1),
    _FadcVdEntIndex_Type()
)
fadcVdEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcVdEntIndex.setStatus("current")
_FadcVdEntName_Type = DisplayString
_FadcVdEntName_Object = MibTableColumn
fadcVdEntName = _FadcVdEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 2, 1, 1, 2),
    _FadcVdEntName_Type()
)
fadcVdEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVdEntName.setStatus("current")
_FadcVdEntHaState_Type = FadcHaState
_FadcVdEntHaState_Object = MibTableColumn
fadcVdEntHaState = _FadcVdEntHaState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 2, 2, 1, 1, 3),
    _FadcVdEntHaState_Type()
)
fadcVdEntHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVdEntHaState.setStatus("current")
_FadcVirtualServer_ObjectIdentity = ObjectIdentity
fadcVirtualServer = _FadcVirtualServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3)
)
_FadcVSNumber_Type = Integer32
_FadcVSNumber_Object = MibScalar
fadcVSNumber = _FadcVSNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 1),
    _FadcVSNumber_Type()
)
fadcVSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSNumber.setStatus("current")
_FadcVSTable_Object = MibTable
fadcVSTable = _FadcVSTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2)
)
if mibBuilder.loadTexts:
    fadcVSTable.setStatus("current")
_FadcVSEntry_Object = MibTableRow
fadcVSEntry = _FadcVSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1)
)
fadcVSEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcVSIndex"),
)
if mibBuilder.loadTexts:
    fadcVSEntry.setStatus("current")
_FadcVSIndex_Type = FnIndex
_FadcVSIndex_Object = MibTableColumn
fadcVSIndex = _FadcVSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 1),
    _FadcVSIndex_Type()
)
fadcVSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcVSIndex.setStatus("current")
_FadcVSName_Type = DisplayString
_FadcVSName_Object = MibTableColumn
fadcVSName = _FadcVSName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 2),
    _FadcVSName_Type()
)
fadcVSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSName.setStatus("current")
_FadcVSStatus_Type = DisplayString
_FadcVSStatus_Object = MibTableColumn
fadcVSStatus = _FadcVSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 3),
    _FadcVSStatus_Type()
)
fadcVSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSStatus.setStatus("current")
_FadcVSHealth_Type = DisplayString
_FadcVSHealth_Object = MibTableColumn
fadcVSHealth = _FadcVSHealth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 4),
    _FadcVSHealth_Type()
)
fadcVSHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSHealth.setStatus("current")


class _FadcVSNewConnections_Type(Integer32):
    """Custom type fadcVSNewConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVSNewConnections_Type.__name__ = "Integer32"
_FadcVSNewConnections_Object = MibTableColumn
fadcVSNewConnections = _FadcVSNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 5),
    _FadcVSNewConnections_Type()
)
fadcVSNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSNewConnections.setStatus("current")


class _FadcVSConcurrent_Type(Integer32):
    """Custom type fadcVSConcurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVSConcurrent_Type.__name__ = "Integer32"
_FadcVSConcurrent_Object = MibTableColumn
fadcVSConcurrent = _FadcVSConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 6),
    _FadcVSConcurrent_Type()
)
fadcVSConcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSConcurrent.setStatus("current")


class _FadcVSThroughputKbps_Type(Integer32):
    """Custom type fadcVSThroughputKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVSThroughputKbps_Type.__name__ = "Integer32"
_FadcVSThroughputKbps_Object = MibTableColumn
fadcVSThroughputKbps = _FadcVSThroughputKbps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 7),
    _FadcVSThroughputKbps_Type()
)
fadcVSThroughputKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSThroughputKbps.setStatus("current")
_FadcVSVdom_Type = DisplayString
_FadcVSVdom_Object = MibTableColumn
fadcVSVdom = _FadcVSVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 3, 2, 1, 8),
    _FadcVSVdom_Type()
)
fadcVSVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSVdom.setStatus("current")
_FadcIntf_ObjectIdentity = ObjectIdentity
fadcIntf = _FadcIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 4)
)
_FadcIntfTable_Object = MibTable
fadcIntfTable = _FadcIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 4, 1)
)
if mibBuilder.loadTexts:
    fadcIntfTable.setStatus("current")
_FadcIntfEntry_Object = MibTableRow
fadcIntfEntry = _FadcIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 4, 1, 1)
)
fadcIntfEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcIntfIndex"),
)
if mibBuilder.loadTexts:
    fadcIntfEntry.setStatus("current")
_FadcIntfIndex_Type = FnIndex
_FadcIntfIndex_Object = MibTableColumn
fadcIntfIndex = _FadcIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 4, 1, 1, 1),
    _FadcIntfIndex_Type()
)
fadcIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcIntfIndex.setStatus("current")
_FadcIntfName_Type = DisplayString
_FadcIntfName_Object = MibTableColumn
fadcIntfName = _FadcIntfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 4, 1, 1, 2),
    _FadcIntfName_Type()
)
fadcIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntfName.setStatus("current")
_FadcIntfVdom_Type = DisplayString
_FadcIntfVdom_Object = MibTableColumn
fadcIntfVdom = _FadcIntfVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 4, 1, 1, 3),
    _FadcIntfVdom_Type()
)
fadcIntfVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntfVdom.setStatus("current")
_FadcAdmin_ObjectIdentity = ObjectIdentity
fadcAdmin = _FadcAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 5)
)
_FadcAdminTable_Object = MibTable
fadcAdminTable = _FadcAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 5, 1)
)
if mibBuilder.loadTexts:
    fadcAdminTable.setStatus("current")
_FadcAdminEntry_Object = MibTableRow
fadcAdminEntry = _FadcAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 5, 1, 1)
)
fadcAdminEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcAdminIndex"),
)
if mibBuilder.loadTexts:
    fadcAdminEntry.setStatus("current")
_FadcAdminIndex_Type = FnIndex
_FadcAdminIndex_Object = MibTableColumn
fadcAdminIndex = _FadcAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 5, 1, 1, 1),
    _FadcAdminIndex_Type()
)
fadcAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcAdminIndex.setStatus("current")
_FadcAdminName_Type = DisplayString
_FadcAdminName_Object = MibTableColumn
fadcAdminName = _FadcAdminName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 5, 1, 1, 2),
    _FadcAdminName_Type()
)
fadcAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAdminName.setStatus("current")
_FadcAdminVdom_Type = DisplayString
_FadcAdminVdom_Object = MibTableColumn
fadcAdminVdom = _FadcAdminVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 5, 1, 1, 3),
    _FadcAdminVdom_Type()
)
fadcAdminVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAdminVdom.setStatus("current")
_FadcHardware_ObjectIdentity = ObjectIdentity
fadcHardware = _FadcHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6)
)
_FadcCPUInfo_ObjectIdentity = ObjectIdentity
fadcCPUInfo = _FadcCPUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 1)
)
_FadcCPUTable_Object = MibTable
fadcCPUTable = _FadcCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fadcCPUTable.setStatus("current")
_FadcCPUEntry_Object = MibTableRow
fadcCPUEntry = _FadcCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 1, 1, 1)
)
fadcCPUEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcCPUIndex"),
)
if mibBuilder.loadTexts:
    fadcCPUEntry.setStatus("current")
_FadcCPUIndex_Type = FnIndex
_FadcCPUIndex_Object = MibTableColumn
fadcCPUIndex = _FadcCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 1, 1, 1, 1),
    _FadcCPUIndex_Type()
)
fadcCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcCPUIndex.setStatus("current")
_FadcCPUName_Type = DisplayString
_FadcCPUName_Object = MibTableColumn
fadcCPUName = _FadcCPUName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 1, 1, 1, 2),
    _FadcCPUName_Type()
)
fadcCPUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCPUName.setStatus("current")
_FadcCPUTemp_Type = Integer32
_FadcCPUTemp_Object = MibTableColumn
fadcCPUTemp = _FadcCPUTemp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 1, 1, 1, 3),
    _FadcCPUTemp_Type()
)
fadcCPUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCPUTemp.setStatus("current")
_FadcPSUInfo_ObjectIdentity = ObjectIdentity
fadcPSUInfo = _FadcPSUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2)
)
_FadcPSUTable_Object = MibTable
fadcPSUTable = _FadcPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1)
)
if mibBuilder.loadTexts:
    fadcPSUTable.setStatus("current")
_FadcPSUEntry_Object = MibTableRow
fadcPSUEntry = _FadcPSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1)
)
fadcPSUEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcPSUIndex"),
)
if mibBuilder.loadTexts:
    fadcPSUEntry.setStatus("current")
_FadcPSUIndex_Type = FnIndex
_FadcPSUIndex_Object = MibTableColumn
fadcPSUIndex = _FadcPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1, 1),
    _FadcPSUIndex_Type()
)
fadcPSUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcPSUIndex.setStatus("current")
_FadcPSUName_Type = DisplayString
_FadcPSUName_Object = MibTableColumn
fadcPSUName = _FadcPSUName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1, 2),
    _FadcPSUName_Type()
)
fadcPSUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUName.setStatus("current")
_FadcPSUTemp_Type = Integer32
_FadcPSUTemp_Object = MibTableColumn
fadcPSUTemp = _FadcPSUTemp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1, 3),
    _FadcPSUTemp_Type()
)
fadcPSUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUTemp.setStatus("current")
_FadcPSUFanSpeed_Type = Integer32
_FadcPSUFanSpeed_Object = MibTableColumn
fadcPSUFanSpeed = _FadcPSUFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1, 4),
    _FadcPSUFanSpeed_Type()
)
fadcPSUFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUFanSpeed.setStatus("current")
_FadcPSUFanStatus_Type = DisplayString
_FadcPSUFanStatus_Object = MibTableColumn
fadcPSUFanStatus = _FadcPSUFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1, 5),
    _FadcPSUFanStatus_Type()
)
fadcPSUFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUFanStatus.setStatus("current")
_FadcPSUVoltage_Type = Integer32
_FadcPSUVoltage_Object = MibTableColumn
fadcPSUVoltage = _FadcPSUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1, 6),
    _FadcPSUVoltage_Type()
)
fadcPSUVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUVoltage.setStatus("current")
_FadcPSUStatus_Type = DisplayString
_FadcPSUStatus_Object = MibTableColumn
fadcPSUStatus = _FadcPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 2, 1, 1, 7),
    _FadcPSUStatus_Type()
)
fadcPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUStatus.setStatus("current")
_FadcNetworkInfo_ObjectIdentity = ObjectIdentity
fadcNetworkInfo = _FadcNetworkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 3)
)
_FadcNetworkTable_Object = MibTable
fadcNetworkTable = _FadcNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 3, 1)
)
if mibBuilder.loadTexts:
    fadcNetworkTable.setStatus("current")
_FadcNetworkEntry_Object = MibTableRow
fadcNetworkEntry = _FadcNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 3, 1, 1)
)
fadcNetworkEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcNetworkIndex"),
)
if mibBuilder.loadTexts:
    fadcNetworkEntry.setStatus("current")
_FadcNetworkIndex_Type = FnIndex
_FadcNetworkIndex_Object = MibTableColumn
fadcNetworkIndex = _FadcNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 3, 1, 1, 1),
    _FadcNetworkIndex_Type()
)
fadcNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcNetworkIndex.setStatus("current")
_FadcPortLinkName_Type = DisplayString
_FadcPortLinkName_Object = MibTableColumn
fadcPortLinkName = _FadcPortLinkName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 3, 1, 1, 2),
    _FadcPortLinkName_Type()
)
fadcPortLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPortLinkName.setStatus("current")
_FadcPortLinkStatus_Type = DisplayString
_FadcPortLinkStatus_Object = MibTableColumn
fadcPortLinkStatus = _FadcPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 3, 1, 1, 3),
    _FadcPortLinkStatus_Type()
)
fadcPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPortLinkStatus.setStatus("current")
_FadcDeviceInfo_ObjectIdentity = ObjectIdentity
fadcDeviceInfo = _FadcDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4)
)
_FadcDeviceTempTables_ObjectIdentity = ObjectIdentity
fadcDeviceTempTables = _FadcDeviceTempTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 1)
)
_FadcDeviceTempTable_Object = MibTable
fadcDeviceTempTable = _FadcDeviceTempTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fadcDeviceTempTable.setStatus("current")
_FadcDeviceTempEntry_Object = MibTableRow
fadcDeviceTempEntry = _FadcDeviceTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 1, 1, 1)
)
fadcDeviceTempEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcDeviceTempIndex"),
)
if mibBuilder.loadTexts:
    fadcDeviceTempEntry.setStatus("current")
_FadcDeviceTempIndex_Type = FnIndex
_FadcDeviceTempIndex_Object = MibTableColumn
fadcDeviceTempIndex = _FadcDeviceTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 1, 1, 1, 1),
    _FadcDeviceTempIndex_Type()
)
fadcDeviceTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcDeviceTempIndex.setStatus("current")
_FadcDeviceTempName_Type = DisplayString
_FadcDeviceTempName_Object = MibTableColumn
fadcDeviceTempName = _FadcDeviceTempName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 1, 1, 1, 2),
    _FadcDeviceTempName_Type()
)
fadcDeviceTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceTempName.setStatus("current")
_FadcDeviceTempValue_Type = Integer32
_FadcDeviceTempValue_Object = MibTableColumn
fadcDeviceTempValue = _FadcDeviceTempValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 1, 1, 1, 3),
    _FadcDeviceTempValue_Type()
)
fadcDeviceTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceTempValue.setStatus("current")
_FadcDeviceFanTables_ObjectIdentity = ObjectIdentity
fadcDeviceFanTables = _FadcDeviceFanTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 2)
)
_FadcDeviceFanTable_Object = MibTable
fadcDeviceFanTable = _FadcDeviceFanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fadcDeviceFanTable.setStatus("current")
_FadcDeviceFanEntry_Object = MibTableRow
fadcDeviceFanEntry = _FadcDeviceFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 2, 1, 1)
)
fadcDeviceFanEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcDeviceFanIndex"),
)
if mibBuilder.loadTexts:
    fadcDeviceFanEntry.setStatus("current")
_FadcDeviceFanIndex_Type = FnIndex
_FadcDeviceFanIndex_Object = MibTableColumn
fadcDeviceFanIndex = _FadcDeviceFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 2, 1, 1, 1),
    _FadcDeviceFanIndex_Type()
)
fadcDeviceFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcDeviceFanIndex.setStatus("current")
_FadcDeviceFanName_Type = DisplayString
_FadcDeviceFanName_Object = MibTableColumn
fadcDeviceFanName = _FadcDeviceFanName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 2, 1, 1, 2),
    _FadcDeviceFanName_Type()
)
fadcDeviceFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceFanName.setStatus("current")
_FadcDeviceFanSpeed_Type = Integer32
_FadcDeviceFanSpeed_Object = MibTableColumn
fadcDeviceFanSpeed = _FadcDeviceFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 2, 1, 1, 3),
    _FadcDeviceFanSpeed_Type()
)
fadcDeviceFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceFanSpeed.setStatus("current")
_FadcDeviceFanStatus_Type = DisplayString
_FadcDeviceFanStatus_Object = MibTableColumn
fadcDeviceFanStatus = _FadcDeviceFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 4, 2, 1, 1, 4),
    _FadcDeviceFanStatus_Type()
)
fadcDeviceFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceFanStatus.setStatus("current")
_FadcHA_ObjectIdentity = ObjectIdentity
fadcHA = _FadcHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5)
)
_FadcHACurMode_Type = FadcHAModeVal
_FadcHACurMode_Object = MibScalar
fadcHACurMode = _FadcHACurMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 1),
    _FadcHACurMode_Type()
)
fadcHACurMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHACurMode.setStatus("current")
_FadcHACurState_Type = DisplayString
_FadcHACurState_Object = MibScalar
fadcHACurState = _FadcHACurState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 2),
    _FadcHACurState_Type()
)
fadcHACurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHACurState.setStatus("current")
_FadcHAPeerCount_Type = Integer32
_FadcHAPeerCount_Object = MibScalar
fadcHAPeerCount = _FadcHAPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 3),
    _FadcHAPeerCount_Type()
)
fadcHAPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHAPeerCount.setStatus("current")
_FadcMonitorIntfCount_Type = Integer32
_FadcMonitorIntfCount_Object = MibScalar
fadcMonitorIntfCount = _FadcMonitorIntfCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 4),
    _FadcMonitorIntfCount_Type()
)
fadcMonitorIntfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcMonitorIntfCount.setStatus("current")
_FadcDiskState_Type = Integer32
_FadcDiskState_Object = MibScalar
fadcDiskState = _FadcDiskState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 5),
    _FadcDiskState_Type()
)
fadcDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDiskState.setStatus("current")
_FadcHALastChangedTime_Type = DisplayString
_FadcHALastChangedTime_Object = MibScalar
fadcHALastChangedTime = _FadcHALastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 6),
    _FadcHALastChangedTime_Type()
)
fadcHALastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHALastChangedTime.setStatus("current")
_FadcHALastChangedReason_Type = DisplayString
_FadcHALastChangedReason_Object = MibScalar
fadcHALastChangedReason = _FadcHALastChangedReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 7),
    _FadcHALastChangedReason_Type()
)
fadcHALastChangedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHALastChangedReason.setStatus("current")
_FadcSyncStats_ObjectIdentity = ObjectIdentity
fadcSyncStats = _FadcSyncStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 20)
)
_FadcHASyncStatsTable_Object = MibTable
fadcHASyncStatsTable = _FadcHASyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 20, 1)
)
if mibBuilder.loadTexts:
    fadcHASyncStatsTable.setStatus("current")
_FadcHASyncStatsEntry_Object = MibTableRow
fadcHASyncStatsEntry = _FadcHASyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 20, 1, 1)
)
fadcHASyncStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcSyncTypeIndex"),
)
if mibBuilder.loadTexts:
    fadcHASyncStatsEntry.setStatus("current")
_FadcSyncTypeIndex_Type = FnIndex
_FadcSyncTypeIndex_Object = MibTableColumn
fadcSyncTypeIndex = _FadcSyncTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 20, 1, 1, 1),
    _FadcSyncTypeIndex_Type()
)
fadcSyncTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcSyncTypeIndex.setStatus("current")
_FadcSyncType_Type = DisplayString
_FadcSyncType_Object = MibTableColumn
fadcSyncType = _FadcSyncType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 20, 1, 1, 2),
    _FadcSyncType_Type()
)
fadcSyncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSyncType.setStatus("current")
_FadcSyncSent_Type = Integer32
_FadcSyncSent_Object = MibTableColumn
fadcSyncSent = _FadcSyncSent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 20, 1, 1, 3),
    _FadcSyncSent_Type()
)
fadcSyncSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSyncSent.setStatus("current")
_FadcSyncReceived_Type = Integer32
_FadcSyncReceived_Object = MibTableColumn
fadcSyncReceived = _FadcSyncReceived_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 20, 1, 1, 4),
    _FadcSyncReceived_Type()
)
fadcSyncReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSyncReceived.setStatus("current")
_FadcDeviceErrCount_ObjectIdentity = ObjectIdentity
fadcDeviceErrCount = _FadcDeviceErrCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 21)
)
_FadcDuplicateNodeID_Type = Integer32
_FadcDuplicateNodeID_Object = MibScalar
fadcDuplicateNodeID = _FadcDuplicateNodeID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 21, 1),
    _FadcDuplicateNodeID_Type()
)
fadcDuplicateNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDuplicateNodeID.setStatus("current")
_FadcVersionMismatch_Type = Integer32
_FadcVersionMismatch_Object = MibScalar
fadcVersionMismatch = _FadcVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 21, 2),
    _FadcVersionMismatch_Type()
)
fadcVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVersionMismatch.setStatus("current")
_FadcHAPeerInfo_ObjectIdentity = ObjectIdentity
fadcHAPeerInfo = _FadcHAPeerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22)
)
_FadcHAPeerTable_Object = MibTable
fadcHAPeerTable = _FadcHAPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22, 1)
)
if mibBuilder.loadTexts:
    fadcHAPeerTable.setStatus("current")
_FadcHAPeerEntry_Object = MibTableRow
fadcHAPeerEntry = _FadcHAPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22, 1, 1)
)
fadcHAPeerEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcPeerIndex"),
)
if mibBuilder.loadTexts:
    fadcHAPeerEntry.setStatus("current")
_FadcPeerIndex_Type = FnIndex
_FadcPeerIndex_Object = MibTableColumn
fadcPeerIndex = _FadcPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22, 1, 1, 1),
    _FadcPeerIndex_Type()
)
fadcPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcPeerIndex.setStatus("current")
_FadcPeerSerialNumber_Type = DisplayString
_FadcPeerSerialNumber_Object = MibTableColumn
fadcPeerSerialNumber = _FadcPeerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22, 1, 1, 2),
    _FadcPeerSerialNumber_Type()
)
fadcPeerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPeerSerialNumber.setStatus("current")
_FadcPeerStatus_Type = DisplayString
_FadcPeerStatus_Object = MibTableColumn
fadcPeerStatus = _FadcPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22, 1, 1, 3),
    _FadcPeerStatus_Type()
)
fadcPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPeerStatus.setStatus("current")
_FadcNodeID_Type = Integer32
_FadcNodeID_Object = MibTableColumn
fadcNodeID = _FadcNodeID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22, 1, 1, 4),
    _FadcNodeID_Type()
)
fadcNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcNodeID.setStatus("current")
_FadcIPAddress_Type = DisplayString
_FadcIPAddress_Object = MibTableColumn
fadcIPAddress = _FadcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 5, 22, 1, 1, 5),
    _FadcIPAddress_Type()
)
fadcIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIPAddress.setStatus("current")
_FadcVoltage_Type = Integer32
_FadcVoltage_Object = MibScalar
fadcVoltage = _FadcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 6),
    _FadcVoltage_Type()
)
fadcVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVoltage.setStatus("current")
_FadcPowerSupplyVoltage_Type = Integer32
_FadcPowerSupplyVoltage_Object = MibScalar
fadcPowerSupplyVoltage = _FadcPowerSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 7),
    _FadcPowerSupplyVoltage_Type()
)
fadcPowerSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPowerSupplyVoltage.setStatus("current")
_FadcLogDiskStatus_Type = Integer32
_FadcLogDiskStatus_Object = MibScalar
fadcLogDiskStatus = _FadcLogDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 6, 8),
    _FadcLogDiskStatus_Type()
)
fadcLogDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLogDiskStatus.setStatus("current")
_FadcSecurity_ObjectIdentity = ObjectIdentity
fadcSecurity = _FadcSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 7)
)
_FadcDDoSAttackStatus_Type = Gauge32
_FadcDDoSAttackStatus_Object = MibScalar
fadcDDoSAttackStatus = _FadcDDoSAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 7, 1),
    _FadcDDoSAttackStatus_Type()
)
fadcDDoSAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDDoSAttackStatus.setStatus("current")
_FadcApplication_ObjectIdentity = ObjectIdentity
fadcApplication = _FadcApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8)
)
_FadcRS_ObjectIdentity = ObjectIdentity
fadcRS = _FadcRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1)
)
_FadcPoolNumber_Type = Integer32
_FadcPoolNumber_Object = MibScalar
fadcPoolNumber = _FadcPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 1),
    _FadcPoolNumber_Type()
)
fadcPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPoolNumber.setStatus("current")
_FadcRSNumber_Type = Integer32
_FadcRSNumber_Object = MibScalar
fadcRSNumber = _FadcRSNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 2),
    _FadcRSNumber_Type()
)
fadcRSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSNumber.setStatus("current")
_FadcRSTable_Object = MibTable
fadcRSTable = _FadcRSTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3)
)
if mibBuilder.loadTexts:
    fadcRSTable.setStatus("current")
_FadcRSEntry_Object = MibTableRow
fadcRSEntry = _FadcRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1)
)
fadcRSEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcRSIndex"),
)
if mibBuilder.loadTexts:
    fadcRSEntry.setStatus("current")
_FadcRSIndex_Type = FnIndex
_FadcRSIndex_Object = MibTableColumn
fadcRSIndex = _FadcRSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1, 1),
    _FadcRSIndex_Type()
)
fadcRSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcRSIndex.setStatus("current")
_FadcPoolName_Type = DisplayString
_FadcPoolName_Object = MibTableColumn
fadcPoolName = _FadcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1, 2),
    _FadcPoolName_Type()
)
fadcPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPoolName.setStatus("current")
_FadcRSStatus_Type = DisplayString
_FadcRSStatus_Object = MibTableColumn
fadcRSStatus = _FadcRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1, 3),
    _FadcRSStatus_Type()
)
fadcRSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSStatus.setStatus("current")
_FadcRSHealth_Type = DisplayString
_FadcRSHealth_Object = MibTableColumn
fadcRSHealth = _FadcRSHealth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1, 4),
    _FadcRSHealth_Type()
)
fadcRSHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSHealth.setStatus("current")
_FadcRSVdom_Type = DisplayString
_FadcRSVdom_Object = MibTableColumn
fadcRSVdom = _FadcRSVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1, 5),
    _FadcRSVdom_Type()
)
fadcRSVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSVdom.setStatus("current")
_FadcRSName_Type = DisplayString
_FadcRSName_Object = MibTableColumn
fadcRSName = _FadcRSName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1, 6),
    _FadcRSName_Type()
)
fadcRSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSName.setStatus("current")
_FadcRSObjStatus_Type = DisplayString
_FadcRSObjStatus_Object = MibTableColumn
fadcRSObjStatus = _FadcRSObjStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 1, 3, 1, 7),
    _FadcRSObjStatus_Type()
)
fadcRSObjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSObjStatus.setStatus("current")
_FadcVS_ObjectIdentity = ObjectIdentity
fadcVS = _FadcVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2)
)
_FadcVirtualServerNumber_Type = Integer32
_FadcVirtualServerNumber_Object = MibScalar
fadcVirtualServerNumber = _FadcVirtualServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 1),
    _FadcVirtualServerNumber_Type()
)
fadcVirtualServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerNumber.setStatus("current")
_FadcVirtualServerTable_Object = MibTable
fadcVirtualServerTable = _FadcVirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2)
)
if mibBuilder.loadTexts:
    fadcVirtualServerTable.setStatus("current")
_FadcVirtualServerEntry_Object = MibTableRow
fadcVirtualServerEntry = _FadcVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1)
)
fadcVirtualServerEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcVirtualServerIndex"),
)
if mibBuilder.loadTexts:
    fadcVirtualServerEntry.setStatus("current")
_FadcVirtualServerIndex_Type = FnIndex
_FadcVirtualServerIndex_Object = MibTableColumn
fadcVirtualServerIndex = _FadcVirtualServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 1),
    _FadcVirtualServerIndex_Type()
)
fadcVirtualServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcVirtualServerIndex.setStatus("current")
_FadcVirtualServerName_Type = DisplayString
_FadcVirtualServerName_Object = MibTableColumn
fadcVirtualServerName = _FadcVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 2),
    _FadcVirtualServerName_Type()
)
fadcVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerName.setStatus("current")
_FadcVirtualServerStatus_Type = DisplayString
_FadcVirtualServerStatus_Object = MibTableColumn
fadcVirtualServerStatus = _FadcVirtualServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 3),
    _FadcVirtualServerStatus_Type()
)
fadcVirtualServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerStatus.setStatus("current")
_FadcVirtualServerHealth_Type = DisplayString
_FadcVirtualServerHealth_Object = MibTableColumn
fadcVirtualServerHealth = _FadcVirtualServerHealth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 4),
    _FadcVirtualServerHealth_Type()
)
fadcVirtualServerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerHealth.setStatus("current")


class _FadcVirtualServerNewConnections_Type(Integer32):
    """Custom type fadcVirtualServerNewConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirtualServerNewConnections_Type.__name__ = "Integer32"
_FadcVirtualServerNewConnections_Object = MibTableColumn
fadcVirtualServerNewConnections = _FadcVirtualServerNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 5),
    _FadcVirtualServerNewConnections_Type()
)
fadcVirtualServerNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerNewConnections.setStatus("current")


class _FadcVirtualServerConcurrent_Type(Integer32):
    """Custom type fadcVirtualServerConcurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirtualServerConcurrent_Type.__name__ = "Integer32"
_FadcVirtualServerConcurrent_Object = MibTableColumn
fadcVirtualServerConcurrent = _FadcVirtualServerConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 6),
    _FadcVirtualServerConcurrent_Type()
)
fadcVirtualServerConcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerConcurrent.setStatus("current")


class _FadcVirtualServerThroughputKbps_Type(Integer32):
    """Custom type fadcVirtualServerThroughputKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirtualServerThroughputKbps_Type.__name__ = "Integer32"
_FadcVirtualServerThroughputKbps_Object = MibTableColumn
fadcVirtualServerThroughputKbps = _FadcVirtualServerThroughputKbps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 7),
    _FadcVirtualServerThroughputKbps_Type()
)
fadcVirtualServerThroughputKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerThroughputKbps.setStatus("current")
_FadcVirtualServerVdom_Type = DisplayString
_FadcVirtualServerVdom_Object = MibTableColumn
fadcVirtualServerVdom = _FadcVirtualServerVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 8),
    _FadcVirtualServerVdom_Type()
)
fadcVirtualServerVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerVdom.setStatus("current")


class _FadcVirtualServerWAF_Type(Integer32):
    """Custom type fadcVirtualServerWAF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirtualServerWAF_Type.__name__ = "Integer32"
_FadcVirtualServerWAF_Object = MibTableColumn
fadcVirtualServerWAF = _FadcVirtualServerWAF_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 2, 2, 1, 9),
    _FadcVirtualServerWAF_Type()
)
fadcVirtualServerWAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirtualServerWAF.setStatus("current")
_FadcLinkLoadBalance_ObjectIdentity = ObjectIdentity
fadcLinkLoadBalance = _FadcLinkLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3)
)
_FadcGatewayTables_ObjectIdentity = ObjectIdentity
fadcGatewayTables = _FadcGatewayTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1)
)
_FadcGatewayTable_Object = MibTable
fadcGatewayTable = _FadcGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fadcGatewayTable.setStatus("current")
_FadcGatewayEntry_Object = MibTableRow
fadcGatewayEntry = _FadcGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1, 1)
)
fadcGatewayEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcGatewayIndex"),
)
if mibBuilder.loadTexts:
    fadcGatewayEntry.setStatus("current")
_FadcGatewayIndex_Type = FnIndex
_FadcGatewayIndex_Object = MibTableColumn
fadcGatewayIndex = _FadcGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1, 1, 1),
    _FadcGatewayIndex_Type()
)
fadcGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGatewayIndex.setStatus("current")
_FadcGatewayName_Type = DisplayString
_FadcGatewayName_Object = MibTableColumn
fadcGatewayName = _FadcGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1, 1, 2),
    _FadcGatewayName_Type()
)
fadcGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayName.setStatus("current")
_FadcGatewayHCStatus_Type = DisplayString
_FadcGatewayHCStatus_Object = MibTableColumn
fadcGatewayHCStatus = _FadcGatewayHCStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1, 1, 3),
    _FadcGatewayHCStatus_Type()
)
fadcGatewayHCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayHCStatus.setStatus("current")
_FadcGatewayInboundBandWidth_Type = DisplayString
_FadcGatewayInboundBandWidth_Object = MibTableColumn
fadcGatewayInboundBandWidth = _FadcGatewayInboundBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1, 1, 4),
    _FadcGatewayInboundBandWidth_Type()
)
fadcGatewayInboundBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayInboundBandWidth.setStatus("current")
_FadcGatewayOutboundBandWidth_Type = DisplayString
_FadcGatewayOutboundBandWidth_Object = MibTableColumn
fadcGatewayOutboundBandWidth = _FadcGatewayOutboundBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1, 1, 5),
    _FadcGatewayOutboundBandWidth_Type()
)
fadcGatewayOutboundBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayOutboundBandWidth.setStatus("current")
_FadcGatewayVdom_Type = DisplayString
_FadcGatewayVdom_Object = MibTableColumn
fadcGatewayVdom = _FadcGatewayVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 1, 1, 1, 6),
    _FadcGatewayVdom_Type()
)
fadcGatewayVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayVdom.setStatus("current")
_FadcLinkGroupTables_ObjectIdentity = ObjectIdentity
fadcLinkGroupTables = _FadcLinkGroupTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2)
)
_FadcLinkGroupTable_Object = MibTable
fadcLinkGroupTable = _FadcLinkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fadcLinkGroupTable.setStatus("current")
_FadcLinkGroupEntry_Object = MibTableRow
fadcLinkGroupEntry = _FadcLinkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2, 1, 1)
)
fadcLinkGroupEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcLinkGroupIndex"),
)
if mibBuilder.loadTexts:
    fadcLinkGroupEntry.setStatus("current")
_FadcLinkGroupIndex_Type = FnIndex
_FadcLinkGroupIndex_Object = MibTableColumn
fadcLinkGroupIndex = _FadcLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2, 1, 1, 1),
    _FadcLinkGroupIndex_Type()
)
fadcLinkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcLinkGroupIndex.setStatus("current")
_FadcLinkGroupName_Type = DisplayString
_FadcLinkGroupName_Object = MibTableColumn
fadcLinkGroupName = _FadcLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2, 1, 1, 2),
    _FadcLinkGroupName_Type()
)
fadcLinkGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupName.setStatus("current")
_FadcLinkGroupHCStatus_Type = DisplayString
_FadcLinkGroupHCStatus_Object = MibTableColumn
fadcLinkGroupHCStatus = _FadcLinkGroupHCStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2, 1, 1, 3),
    _FadcLinkGroupHCStatus_Type()
)
fadcLinkGroupHCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupHCStatus.setStatus("current")
_FadcLinkGroupMode_Type = DisplayString
_FadcLinkGroupMode_Object = MibTableColumn
fadcLinkGroupMode = _FadcLinkGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2, 1, 1, 4),
    _FadcLinkGroupMode_Type()
)
fadcLinkGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupMode.setStatus("current")
_FadcLinkGroupVdom_Type = DisplayString
_FadcLinkGroupVdom_Object = MibTableColumn
fadcLinkGroupVdom = _FadcLinkGroupVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 3, 2, 1, 1, 5),
    _FadcLinkGroupVdom_Type()
)
fadcLinkGroupVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupVdom.setStatus("current")
_FadcGlobalLoadBalance_ObjectIdentity = ObjectIdentity
fadcGlobalLoadBalance = _FadcGlobalLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4)
)
_FadcGLBVSTables_ObjectIdentity = ObjectIdentity
fadcGLBVSTables = _FadcGLBVSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1)
)
_FadcGLBVSTable_Object = MibTable
fadcGLBVSTable = _FadcGLBVSTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fadcGLBVSTable.setStatus("current")
_FadcGLBVSEntry_Object = MibTableRow
fadcGLBVSEntry = _FadcGLBVSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1, 1, 1)
)
fadcGLBVSEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcGLBVSIndex"),
)
if mibBuilder.loadTexts:
    fadcGLBVSEntry.setStatus("current")
_FadcGLBVSIndex_Type = FnIndex
_FadcGLBVSIndex_Object = MibTableColumn
fadcGLBVSIndex = _FadcGLBVSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1, 1, 1, 1),
    _FadcGLBVSIndex_Type()
)
fadcGLBVSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGLBVSIndex.setStatus("current")
_FadcGLBVSName_Type = DisplayString
_FadcGLBVSName_Object = MibTableColumn
fadcGLBVSName = _FadcGLBVSName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1, 1, 1, 2),
    _FadcGLBVSName_Type()
)
fadcGLBVSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSName.setStatus("current")
_FadcGLBVSStatus_Type = DisplayString
_FadcGLBVSStatus_Object = MibTableColumn
fadcGLBVSStatus = _FadcGLBVSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1, 1, 1, 3),
    _FadcGLBVSStatus_Type()
)
fadcGLBVSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSStatus.setStatus("current")
_FadcGLBVSServerName_Type = DisplayString
_FadcGLBVSServerName_Object = MibTableColumn
fadcGLBVSServerName = _FadcGLBVSServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1, 1, 1, 4),
    _FadcGLBVSServerName_Type()
)
fadcGLBVSServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSServerName.setStatus("current")
_FadcGLBVSVdom_Type = DisplayString
_FadcGLBVSVdom_Object = MibTableColumn
fadcGLBVSVdom = _FadcGLBVSVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 1, 1, 1, 5),
    _FadcGLBVSVdom_Type()
)
fadcGLBVSVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSVdom.setStatus("current")
_FadcGLBServerTables_ObjectIdentity = ObjectIdentity
fadcGLBServerTables = _FadcGLBServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 2)
)
_FadcGLBServerTable_Object = MibTable
fadcGLBServerTable = _FadcGLBServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fadcGLBServerTable.setStatus("current")
_FadcGLBServerEntry_Object = MibTableRow
fadcGLBServerEntry = _FadcGLBServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 2, 1, 1)
)
fadcGLBServerEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcGLBServerIndex"),
)
if mibBuilder.loadTexts:
    fadcGLBServerEntry.setStatus("current")
_FadcGLBServerIndex_Type = FnIndex
_FadcGLBServerIndex_Object = MibTableColumn
fadcGLBServerIndex = _FadcGLBServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 2, 1, 1, 1),
    _FadcGLBServerIndex_Type()
)
fadcGLBServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGLBServerIndex.setStatus("current")
_FadcGLBServerName_Type = DisplayString
_FadcGLBServerName_Object = MibTableColumn
fadcGLBServerName = _FadcGLBServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 2, 1, 1, 2),
    _FadcGLBServerName_Type()
)
fadcGLBServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBServerName.setStatus("current")
_FadcGLBServerStatus_Type = DisplayString
_FadcGLBServerStatus_Object = MibTableColumn
fadcGLBServerStatus = _FadcGLBServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 2, 1, 1, 3),
    _FadcGLBServerStatus_Type()
)
fadcGLBServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBServerStatus.setStatus("current")
_FadcGLBServerVdom_Type = DisplayString
_FadcGLBServerVdom_Object = MibTableColumn
fadcGLBServerVdom = _FadcGLBServerVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 2, 1, 1, 4),
    _FadcGLBServerVdom_Type()
)
fadcGLBServerVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBServerVdom.setStatus("current")
_FadcGLBGatewayTables_ObjectIdentity = ObjectIdentity
fadcGLBGatewayTables = _FadcGLBGatewayTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3)
)
_FadcGLBGatewayTable_Object = MibTable
fadcGLBGatewayTable = _FadcGLBGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3, 1)
)
if mibBuilder.loadTexts:
    fadcGLBGatewayTable.setStatus("current")
_FadcGLBGatewayEntry_Object = MibTableRow
fadcGLBGatewayEntry = _FadcGLBGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3, 1, 1)
)
fadcGLBGatewayEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcGLBGatewayIndex"),
)
if mibBuilder.loadTexts:
    fadcGLBGatewayEntry.setStatus("current")
_FadcGLBGatewayIndex_Type = FnIndex
_FadcGLBGatewayIndex_Object = MibTableColumn
fadcGLBGatewayIndex = _FadcGLBGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3, 1, 1, 1),
    _FadcGLBGatewayIndex_Type()
)
fadcGLBGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGLBGatewayIndex.setStatus("current")
_FadcGLBGatewayName_Type = DisplayString
_FadcGLBGatewayName_Object = MibTableColumn
fadcGLBGatewayName = _FadcGLBGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3, 1, 1, 2),
    _FadcGLBGatewayName_Type()
)
fadcGLBGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayName.setStatus("current")
_FadcGLBGatewayStatus_Type = DisplayString
_FadcGLBGatewayStatus_Object = MibTableColumn
fadcGLBGatewayStatus = _FadcGLBGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3, 1, 1, 3),
    _FadcGLBGatewayStatus_Type()
)
fadcGLBGatewayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayStatus.setStatus("current")
_FadcGLBGatewayServerName_Type = DisplayString
_FadcGLBGatewayServerName_Object = MibTableColumn
fadcGLBGatewayServerName = _FadcGLBGatewayServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3, 1, 1, 4),
    _FadcGLBGatewayServerName_Type()
)
fadcGLBGatewayServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayServerName.setStatus("current")
_FadcGLBGatewayVdom_Type = DisplayString
_FadcGLBGatewayVdom_Object = MibTableColumn
fadcGLBGatewayVdom = _FadcGLBGatewayVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 4, 3, 1, 1, 5),
    _FadcGLBGatewayVdom_Type()
)
fadcGLBGatewayVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayVdom.setStatus("current")
_FadcServerLoadBalance_ObjectIdentity = ObjectIdentity
fadcServerLoadBalance = _FadcServerLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5)
)


class _FadcClientSideCPS_Type(Integer32):
    """Custom type fadcClientSideCPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideCPS_Type.__name__ = "Integer32"
_FadcClientSideCPS_Object = MibScalar
fadcClientSideCPS = _FadcClientSideCPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 1),
    _FadcClientSideCPS_Type()
)
fadcClientSideCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcClientSideCPS.setStatus("current")


class _FadcClientSideRPS_Type(Integer32):
    """Custom type fadcClientSideRPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideRPS_Type.__name__ = "Integer32"
_FadcClientSideRPS_Object = MibScalar
fadcClientSideRPS = _FadcClientSideRPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 2),
    _FadcClientSideRPS_Type()
)
fadcClientSideRPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcClientSideRPS.setStatus("current")


class _FadcClientSideSSLCPS_Type(Integer32):
    """Custom type fadcClientSideSSLCPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideSSLCPS_Type.__name__ = "Integer32"
_FadcClientSideSSLCPS_Object = MibScalar
fadcClientSideSSLCPS = _FadcClientSideSSLCPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 3),
    _FadcClientSideSSLCPS_Type()
)
fadcClientSideSSLCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcClientSideSSLCPS.setStatus("current")


class _FadcClientSideSSLRPS_Type(Integer32):
    """Custom type fadcClientSideSSLRPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideSSLRPS_Type.__name__ = "Integer32"
_FadcClientSideSSLRPS_Object = MibScalar
fadcClientSideSSLRPS = _FadcClientSideSSLRPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 4),
    _FadcClientSideSSLRPS_Type()
)
fadcClientSideSSLRPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcClientSideSSLRPS.setStatus("current")


class _FadcClientSideThroughput_Type(Integer32):
    """Custom type fadcClientSideThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideThroughput_Type.__name__ = "Integer32"
_FadcClientSideThroughput_Object = MibScalar
fadcClientSideThroughput = _FadcClientSideThroughput_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 5),
    _FadcClientSideThroughput_Type()
)
fadcClientSideThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcClientSideThroughput.setStatus("current")


class _FadcClientSideSSLThroughput_Type(Integer32):
    """Custom type fadcClientSideSSLThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideSSLThroughput_Type.__name__ = "Integer32"
_FadcClientSideSSLThroughput_Object = MibScalar
fadcClientSideSSLThroughput = _FadcClientSideSSLThroughput_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 6),
    _FadcClientSideSSLThroughput_Type()
)
fadcClientSideSSLThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcClientSideSSLThroughput.setStatus("current")


class _FadcConcurrentClientConnections_Type(Integer32):
    """Custom type fadcConcurrentClientConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcConcurrentClientConnections_Type.__name__ = "Integer32"
_FadcConcurrentClientConnections_Object = MibScalar
fadcConcurrentClientConnections = _FadcConcurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 7),
    _FadcConcurrentClientConnections_Type()
)
fadcConcurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcConcurrentClientConnections.setStatus("current")


class _FadcConcurrentClientSSLSessions_Type(Integer32):
    """Custom type fadcConcurrentClientSSLSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcConcurrentClientSSLSessions_Type.__name__ = "Integer32"
_FadcConcurrentClientSSLSessions_Object = MibScalar
fadcConcurrentClientSSLSessions = _FadcConcurrentClientSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 8),
    _FadcConcurrentClientSSLSessions_Type()
)
fadcConcurrentClientSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcConcurrentClientSSLSessions.setStatus("current")
_FadcClientSSLCacheUtilizeTables_ObjectIdentity = ObjectIdentity
fadcClientSSLCacheUtilizeTables = _FadcClientSSLCacheUtilizeTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20)
)
_FadcClientSSLCacheUtilizeTable_Object = MibTable
fadcClientSSLCacheUtilizeTable = _FadcClientSSLCacheUtilizeTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1)
)
if mibBuilder.loadTexts:
    fadcClientSSLCacheUtilizeTable.setStatus("current")
_FadcClientSSLCacheUtilizeEntry_Object = MibTableRow
fadcClientSSLCacheUtilizeEntry = _FadcClientSSLCacheUtilizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1)
)
fadcClientSSLCacheUtilizeEntry.setIndexNames(
    (0, "FORTINET-FORTIADC-MIB", "fadcSLBVSIndex"),
)
if mibBuilder.loadTexts:
    fadcClientSSLCacheUtilizeEntry.setStatus("current")
_FadcSLBVSIndex_Type = FnIndex
_FadcSLBVSIndex_Object = MibTableColumn
fadcSLBVSIndex = _FadcSLBVSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 1),
    _FadcSLBVSIndex_Type()
)
fadcSLBVSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcSLBVSIndex.setStatus("current")
_FadcSLBVSName_Type = DisplayString
_FadcSLBVSName_Object = MibTableColumn
fadcSLBVSName = _FadcSLBVSName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 2),
    _FadcSLBVSName_Type()
)
fadcSLBVSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBVSName.setStatus("current")


class _FadcSLBTotalCacheItems_Type(Integer32):
    """Custom type fadcSLBTotalCacheItems based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTotalCacheItems_Type.__name__ = "Integer32"
_FadcSLBTotalCacheItems_Object = MibTableColumn
fadcSLBTotalCacheItems = _FadcSLBTotalCacheItems_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 3),
    _FadcSLBTotalCacheItems_Type()
)
fadcSLBTotalCacheItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTotalCacheItems.setStatus("current")


class _FadcSLBTotalCacheSize_Type(Integer32):
    """Custom type fadcSLBTotalCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTotalCacheSize_Type.__name__ = "Integer32"
_FadcSLBTotalCacheSize_Object = MibTableColumn
fadcSLBTotalCacheSize = _FadcSLBTotalCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 4),
    _FadcSLBTotalCacheSize_Type()
)
fadcSLBTotalCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTotalCacheSize.setStatus("current")


class _FadcSLBCacheHitCount_Type(Integer32):
    """Custom type fadcSLBCacheHitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBCacheHitCount_Type.__name__ = "Integer32"
_FadcSLBCacheHitCount_Object = MibTableColumn
fadcSLBCacheHitCount = _FadcSLBCacheHitCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 5),
    _FadcSLBCacheHitCount_Type()
)
fadcSLBCacheHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBCacheHitCount.setStatus("current")


class _FadcSLBCacheHitBytes_Type(Integer32):
    """Custom type fadcSLBCacheHitBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBCacheHitBytes_Type.__name__ = "Integer32"
_FadcSLBCacheHitBytes_Object = MibTableColumn
fadcSLBCacheHitBytes = _FadcSLBCacheHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 6),
    _FadcSLBCacheHitBytes_Type()
)
fadcSLBCacheHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBCacheHitBytes.setStatus("current")


class _FadcSLBTotalCertCacheItems_Type(Integer32):
    """Custom type fadcSLBTotalCertCacheItems based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTotalCertCacheItems_Type.__name__ = "Integer32"
_FadcSLBTotalCertCacheItems_Object = MibTableColumn
fadcSLBTotalCertCacheItems = _FadcSLBTotalCertCacheItems_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 7),
    _FadcSLBTotalCertCacheItems_Type()
)
fadcSLBTotalCertCacheItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTotalCertCacheItems.setStatus("current")


class _FadcSLBTotalCertCacheSize_Type(Integer32):
    """Custom type fadcSLBTotalCertCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTotalCertCacheSize_Type.__name__ = "Integer32"
_FadcSLBTotalCertCacheSize_Object = MibTableColumn
fadcSLBTotalCertCacheSize = _FadcSLBTotalCertCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 8),
    _FadcSLBTotalCertCacheSize_Type()
)
fadcSLBTotalCertCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTotalCertCacheSize.setStatus("current")


class _FadcSLBHitCertCacheCount_Type(Integer32):
    """Custom type fadcSLBHitCertCacheCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBHitCertCacheCount_Type.__name__ = "Integer32"
_FadcSLBHitCertCacheCount_Object = MibTableColumn
fadcSLBHitCertCacheCount = _FadcSLBHitCertCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 9),
    _FadcSLBHitCertCacheCount_Type()
)
fadcSLBHitCertCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBHitCertCacheCount.setStatus("current")


class _FadcSLBHitCertTotalCheck_Type(Integer32):
    """Custom type fadcSLBHitCertTotalCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBHitCertTotalCheck_Type.__name__ = "Integer32"
_FadcSLBHitCertTotalCheck_Object = MibTableColumn
fadcSLBHitCertTotalCheck = _FadcSLBHitCertTotalCheck_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 10),
    _FadcSLBHitCertTotalCheck_Type()
)
fadcSLBHitCertTotalCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBHitCertTotalCheck.setStatus("current")


class _FadcSLBHitCertPercentage_Type(Integer32):
    """Custom type fadcSLBHitCertPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBHitCertPercentage_Type.__name__ = "Integer32"
_FadcSLBHitCertPercentage_Object = MibTableColumn
fadcSLBHitCertPercentage = _FadcSLBHitCertPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 112, 8, 5, 20, 1, 1, 11),
    _FadcSLBHitCertPercentage_Type()
)
fadcSLBHitCertPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBHitCertPercentage.setStatus("current")
_FadcModel_ObjectIdentity = ObjectIdentity
fadcModel = _FadcModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100)
)
_FadcUnknown_ObjectIdentity = ObjectIdentity
fadcUnknown = _FadcUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 1)
)
_FadcDEV_ObjectIdentity = ObjectIdentity
fadcDEV = _FadcDEV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 10)
)
_FadcKVM_ObjectIdentity = ObjectIdentity
fadcKVM = _FadcKVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 20)
)
_FadcVM_ObjectIdentity = ObjectIdentity
fadcVM = _FadcVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 30)
)
_Fadc60F_ObjectIdentity = ObjectIdentity
fadc60F = _Fadc60F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 63)
)
_Fadc100D_ObjectIdentity = ObjectIdentity
fadc100D = _Fadc100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 101)
)
_Fadc100F_ObjectIdentity = ObjectIdentity
fadc100F = _Fadc100F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 103)
)
_Fadc200D_ObjectIdentity = ObjectIdentity
fadc200D = _Fadc200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 201)
)
_Fadc200F_ObjectIdentity = ObjectIdentity
fadc200F = _Fadc200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 203)
)
_Fadc300D_ObjectIdentity = ObjectIdentity
fadc300D = _Fadc300D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 301)
)
_Fadc300E_ObjectIdentity = ObjectIdentity
fadc300E = _Fadc300E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 302)
)
_Fadc300F_ObjectIdentity = ObjectIdentity
fadc300F = _Fadc300F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 303)
)
_Fadc320F_ObjectIdentity = ObjectIdentity
fadc320F = _Fadc320F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 323)
)
_Fadc400D_ObjectIdentity = ObjectIdentity
fadc400D = _Fadc400D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 401)
)
_Fadc400F_ObjectIdentity = ObjectIdentity
fadc400F = _Fadc400F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 403)
)
_Fadc420F_ObjectIdentity = ObjectIdentity
fadc420F = _Fadc420F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 423)
)
_Fadc700D_ObjectIdentity = ObjectIdentity
fadc700D = _Fadc700D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 701)
)
_Fadc1000D_ObjectIdentity = ObjectIdentity
fadc1000D = _Fadc1000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 1001)
)
_Fadc1000F_ObjectIdentity = ObjectIdentity
fadc1000F = _Fadc1000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 1003)
)
_Fadc1200F_ObjectIdentity = ObjectIdentity
fadc1200F = _Fadc1200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 1203)
)
_Fadc1500D_ObjectIdentity = ObjectIdentity
fadc1500D = _Fadc1500D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 1501)
)
_Fadc2000D_ObjectIdentity = ObjectIdentity
fadc2000D = _Fadc2000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 2001)
)
_Fadc2000F_ObjectIdentity = ObjectIdentity
fadc2000F = _Fadc2000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 2003)
)
_Fadc2200F_ObjectIdentity = ObjectIdentity
fadc2200F = _Fadc2200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 2203)
)
_Fadc4000D_ObjectIdentity = ObjectIdentity
fadc4000D = _Fadc4000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 4001)
)
_Fadc4000F_ObjectIdentity = ObjectIdentity
fadc4000F = _Fadc4000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 4003)
)
_Fadc4200F_ObjectIdentity = ObjectIdentity
fadc4200F = _Fadc4200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 4203)
)
_Fadc5000F_ObjectIdentity = ObjectIdentity
fadc5000F = _Fadc5000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 100, 5003)
)
_FadcMIBConformance_ObjectIdentity = ObjectIdentity
fadcMIBConformance = _FadcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600)
)

# Managed Objects groups

fadcSystemConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 1)
)
fadcSystemConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysModel"),
        ("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcSysVersion"),
        ("FORTINET-FORTIADC-MIB", "fadcSysCpuUsage"),
        ("FORTINET-FORTIADC-MIB", "fadcSysMemUsage"),
        ("FORTINET-FORTIADC-MIB", "fadcSysLogDiskUsage"),
        ("FORTINET-FORTIADC-MIB", "fadcSysLoad"),
        ("FORTINET-FORTIADC-MIB", "fadcCpuName"),
        ("FORTINET-FORTIADC-MIB", "fadcCpu2secAvgUsage"),
        ("FORTINET-FORTIADC-MIB", "fadcCpu1minAvgUsage"),
        ("FORTINET-FORTIADC-MIB", "fadcCpu5minAvgUsage"))
)
if mibBuilder.loadTexts:
    fadcSystemConformanceGroup.setStatus("current")

fadcSysOptionsConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 2)
)
fadcSysOptionsConformanceGroup.setObjects(
    ("FORTINET-FORTIADC-MIB", "fadcSysOptIdleTimeout")
)
if mibBuilder.loadTexts:
    fadcSysOptionsConformanceGroup.setStatus("current")

fadcHAModeConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 6)
)
fadcHAModeConformanceGroup.setObjects(
    ("FORTINET-FORTIADC-MIB", "fadcHAMode")
)
if mibBuilder.loadTexts:
    fadcHAModeConformanceGroup.setStatus("current")

fadcAlertConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 7)
)
fadcAlertConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcAlertName"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertSourceType"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertComments"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertVdomName"))
)
if mibBuilder.loadTexts:
    fadcAlertConformanceGroup.setStatus("current")

fadcCertConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 8)
)
fadcCertConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcLocalCertName"),
        ("FORTINET-FORTIADC-MIB", "fadcLocalCertValidFrom"),
        ("FORTINET-FORTIADC-MIB", "fadcLocalCertValidTo"),
        ("FORTINET-FORTIADC-MIB", "fadcLocalCertVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcIntermediateCAName"),
        ("FORTINET-FORTIADC-MIB", "fadcIntermediateCAValidFrom"),
        ("FORTINET-FORTIADC-MIB", "fadcIntermediateCAValidTo"),
        ("FORTINET-FORTIADC-MIB", "fadcIntermediateCAVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcCACertName"),
        ("FORTINET-FORTIADC-MIB", "fadcCACertValidFrom"),
        ("FORTINET-FORTIADC-MIB", "fadcCACertValidTo"),
        ("FORTINET-FORTIADC-MIB", "fadcCACertVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcRemoteCertName"),
        ("FORTINET-FORTIADC-MIB", "fadcRemoteCertValidFrom"),
        ("FORTINET-FORTIADC-MIB", "fadcRemoteCertValidTo"),
        ("FORTINET-FORTIADC-MIB", "fadcRemoteCertVdom"))
)
if mibBuilder.loadTexts:
    fadcCertConformanceGroup.setStatus("current")

fadcVdomConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 9)
)
fadcVdomConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcVdNumber"),
        ("FORTINET-FORTIADC-MIB", "fadcVdMaxVdoms"),
        ("FORTINET-FORTIADC-MIB", "fadcVdEnabled"),
        ("FORTINET-FORTIADC-MIB", "fadcVdEntName"),
        ("FORTINET-FORTIADC-MIB", "fadcVdEntHaState"))
)
if mibBuilder.loadTexts:
    fadcVdomConformanceGroup.setStatus("current")

fadcVSConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 10)
)
fadcVSConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcVSNumber"),
        ("FORTINET-FORTIADC-MIB", "fadcVSName"),
        ("FORTINET-FORTIADC-MIB", "fadcVSStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcVSHealth"),
        ("FORTINET-FORTIADC-MIB", "fadcVSNewConnections"),
        ("FORTINET-FORTIADC-MIB", "fadcVSConcurrent"),
        ("FORTINET-FORTIADC-MIB", "fadcVSThroughputKbps"),
        ("FORTINET-FORTIADC-MIB", "fadcVSVdom"))
)
if mibBuilder.loadTexts:
    fadcVSConformanceGroup.setStatus("current")

fadcIntfConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 11)
)
fadcIntfConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcIntfName"),
        ("FORTINET-FORTIADC-MIB", "fadcIntfVdom"))
)
if mibBuilder.loadTexts:
    fadcIntfConformanceGroup.setStatus("current")

fadcAdminConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 12)
)
fadcAdminConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcAdminName"),
        ("FORTINET-FORTIADC-MIB", "fadcAdminVdom"))
)
if mibBuilder.loadTexts:
    fadcAdminConformanceGroup.setStatus("current")

fadcHardwareConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 13)
)
fadcHardwareConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcCPUName"),
        ("FORTINET-FORTIADC-MIB", "fadcCPUTemp"),
        ("FORTINET-FORTIADC-MIB", "fadcPSUName"),
        ("FORTINET-FORTIADC-MIB", "fadcPSUTemp"),
        ("FORTINET-FORTIADC-MIB", "fadcPSUFanSpeed"),
        ("FORTINET-FORTIADC-MIB", "fadcPSUFanStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcPSUVoltage"),
        ("FORTINET-FORTIADC-MIB", "fadcPSUStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcPortLinkName"),
        ("FORTINET-FORTIADC-MIB", "fadcPortLinkStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcDeviceTempName"),
        ("FORTINET-FORTIADC-MIB", "fadcDeviceTempValue"),
        ("FORTINET-FORTIADC-MIB", "fadcDeviceFanName"),
        ("FORTINET-FORTIADC-MIB", "fadcDeviceFanSpeed"),
        ("FORTINET-FORTIADC-MIB", "fadcDeviceFanStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcHACurMode"),
        ("FORTINET-FORTIADC-MIB", "fadcHACurState"),
        ("FORTINET-FORTIADC-MIB", "fadcHAPeerCount"),
        ("FORTINET-FORTIADC-MIB", "fadcMonitorIntfCount"),
        ("FORTINET-FORTIADC-MIB", "fadcDiskState"),
        ("FORTINET-FORTIADC-MIB", "fadcHALastChangedTime"),
        ("FORTINET-FORTIADC-MIB", "fadcHALastChangedReason"),
        ("FORTINET-FORTIADC-MIB", "fadcSyncType"),
        ("FORTINET-FORTIADC-MIB", "fadcSyncSent"),
        ("FORTINET-FORTIADC-MIB", "fadcSyncReceived"),
        ("FORTINET-FORTIADC-MIB", "fadcDuplicateNodeID"),
        ("FORTINET-FORTIADC-MIB", "fadcVersionMismatch"),
        ("FORTINET-FORTIADC-MIB", "fadcPeerSerialNumber"),
        ("FORTINET-FORTIADC-MIB", "fadcPeerStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcNodeID"),
        ("FORTINET-FORTIADC-MIB", "fadcIPAddress"),
        ("FORTINET-FORTIADC-MIB", "fadcVoltage"),
        ("FORTINET-FORTIADC-MIB", "fadcPowerSupplyVoltage"),
        ("FORTINET-FORTIADC-MIB", "fadcLogDiskStatus"))
)
if mibBuilder.loadTexts:
    fadcHardwareConformanceGroup.setStatus("current")

fadcSecurityConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 14)
)
fadcSecurityConformanceGroup.setObjects(
    ("FORTINET-FORTIADC-MIB", "fadcDDoSAttackStatus")
)
if mibBuilder.loadTexts:
    fadcSecurityConformanceGroup.setStatus("current")

fadcApplicationConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 15)
)
fadcApplicationConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcPoolNumber"),
        ("FORTINET-FORTIADC-MIB", "fadcRSNumber"),
        ("FORTINET-FORTIADC-MIB", "fadcPoolName"),
        ("FORTINET-FORTIADC-MIB", "fadcRSStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcRSHealth"),
        ("FORTINET-FORTIADC-MIB", "fadcRSVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcRSName"),
        ("FORTINET-FORTIADC-MIB", "fadcRSObjStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerNumber"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerName"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerHealth"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerNewConnections"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerConcurrent"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerThroughputKbps"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcVirtualServerWAF"),
        ("FORTINET-FORTIADC-MIB", "fadcGatewayName"),
        ("FORTINET-FORTIADC-MIB", "fadcGatewayHCStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcGatewayInboundBandWidth"),
        ("FORTINET-FORTIADC-MIB", "fadcGatewayOutboundBandWidth"),
        ("FORTINET-FORTIADC-MIB", "fadcGatewayVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcLinkGroupName"),
        ("FORTINET-FORTIADC-MIB", "fadcLinkGroupHCStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcLinkGroupMode"),
        ("FORTINET-FORTIADC-MIB", "fadcLinkGroupVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBVSName"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBVSStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBVSServerName"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBVSVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBServerName"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBServerStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBServerVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBGatewayName"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBGatewayStatus"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBGatewayServerName"),
        ("FORTINET-FORTIADC-MIB", "fadcGLBGatewayVdom"),
        ("FORTINET-FORTIADC-MIB", "fadcClientSideCPS"),
        ("FORTINET-FORTIADC-MIB", "fadcClientSideRPS"),
        ("FORTINET-FORTIADC-MIB", "fadcClientSideSSLCPS"),
        ("FORTINET-FORTIADC-MIB", "fadcClientSideSSLRPS"),
        ("FORTINET-FORTIADC-MIB", "fadcClientSideThroughput"),
        ("FORTINET-FORTIADC-MIB", "fadcClientSideSSLThroughput"),
        ("FORTINET-FORTIADC-MIB", "fadcConcurrentClientConnections"),
        ("FORTINET-FORTIADC-MIB", "fadcConcurrentClientSSLSessions"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBVSName"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBTotalCacheItems"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBTotalCacheSize"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBCacheHitCount"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBCacheHitBytes"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBTotalCertCacheItems"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBTotalCertCacheSize"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBHitCertCacheCount"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBHitCertTotalCheck"),
        ("FORTINET-FORTIADC-MIB", "fadcSLBHitCertPercentage"))
)
if mibBuilder.loadTexts:
    fadcApplicationConformanceGroup.setStatus("current")


# Notification objects

fadcTrapCpuHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 101)
)
fadcTrapCpuHighThreshold.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapCpuHighThreshold.setStatus(
        "current"
    )

fadcTrapMemLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 102)
)
fadcTrapMemLowThreshold.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapMemLowThreshold.setStatus(
        "current"
    )

fadcTrapLogDiskHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 103)
)
fadcTrapLogDiskHighThreshold.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogDiskHighThreshold.setStatus(
        "current"
    )

fadcTrapDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 401)
)
fadcTrapDosAttackStart.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDosAttackStart.setStatus(
        "current"
    )

fadcTrapDosAttackStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 402)
)
fadcTrapDosAttackStop.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDosAttackStop.setStatus(
        "current"
    )

fadcTrapFwConnectionLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 403)
)
fadcTrapFwConnectionLimit.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapFwConnectionLimit.setStatus(
        "current"
    )

fadcTrapFwSnatLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 404)
)
fadcTrapFwSnatLimit.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapFwSnatLimit.setStatus(
        "current"
    )

fadcTrapRequestBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 405)
)
fadcTrapRequestBlocked.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapRequestBlocked.setStatus(
        "current"
    )

fadcTrapXSSAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 406)
)
fadcTrapXSSAttack.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapXSSAttack.setStatus(
        "current"
    )

fadcTrapSQLInjectionAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 407)
)
fadcTrapSQLInjectionAttack.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSQLInjectionAttack.setStatus(
        "current"
    )

fadcTrapGenericAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 408)
)
fadcTrapGenericAttack.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGenericAttack.setStatus(
        "current"
    )

fadcTrapExploitsAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 409)
)
fadcTrapExploitsAttack.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapExploitsAttack.setStatus(
        "current"
    )

fadcTrapTrojansAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 410)
)
fadcTrapTrojansAttack.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapTrojansAttack.setStatus(
        "current"
    )

fadcTrapInfoDisclosureAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 411)
)
fadcTrapInfoDisclosureAttack.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapInfoDisclosureAttack.setStatus(
        "current"
    )

fadcTrapURLPattenViolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 412)
)
fadcTrapURLPattenViolate.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapURLPattenViolate.setStatus(
        "current"
    )

fadcTrapProtocolConstraint = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 413)
)
fadcTrapProtocolConstraint.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapProtocolConstraint.setStatus(
        "current"
    )

fadcTrapGeoViolateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 414)
)
fadcTrapGeoViolateDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGeoViolateDetected.setStatus(
        "current"
    )

fadcTrapReputationViolateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 415)
)
fadcTrapReputationViolateDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapReputationViolateDetected.setStatus(
        "current"
    )

fadcTrapBotDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 416)
)
fadcTrapBotDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapBotDetected.setStatus(
        "current"
    )

fadcTrapFwConnectionDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 417)
)
fadcTrapFwConnectionDeny.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapFwConnectionDeny.setStatus(
        "current"
    )

fadcTrapXmlDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 418)
)
fadcTrapXmlDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapXmlDetected.setStatus(
        "current"
    )

fadcTrapJsonDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 419)
)
fadcTrapJsonDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapJsonDetected.setStatus(
        "current"
    )

fadcTrapSoapDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 420)
)
fadcTrapSoapDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSoapDetected.setStatus(
        "current"
    )

fadcTrapDlpDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 421)
)
fadcTrapDlpDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDlpDetected.setStatus(
        "current"
    )

fadcTrapHtmlDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 422)
)
fadcTrapHtmlDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapHtmlDetected.setStatus(
        "current"
    )

fadcTrapWpdDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 423)
)
fadcTrapWpdDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapWpdDetected.setStatus(
        "current"
    )

fadcTrapCsrfDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 424)
)
fadcTrapCsrfDetected.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapCsrfDetected.setStatus(
        "current"
    )

fadcTrapDdosIpFragmentation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 425)
)
fadcTrapDdosIpFragmentation.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDdosIpFragmentation.setStatus(
        "current"
    )

fadcTrapDdosTcpSlowDataAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 426)
)
fadcTrapDdosTcpSlowDataAttack.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDdosTcpSlowDataAttack.setStatus(
        "current"
    )

fadcTrapDdosTcpAccessFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 427)
)
fadcTrapDdosTcpAccessFlood.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDdosTcpAccessFlood.setStatus(
        "current"
    )

fadcTrapDdosHttpConnectionFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 428)
)
fadcTrapDdosHttpConnectionFlood.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDdosHttpConnectionFlood.setStatus(
        "current"
    )

fadcTrapDdosHttpRequestFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 429)
)
fadcTrapDdosHttpRequestFlood.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDdosHttpRequestFlood.setStatus(
        "current"
    )

fadcTrapDdosHttpAccessLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 430)
)
fadcTrapDdosHttpAccessLimit.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDdosHttpAccessLimit.setStatus(
        "current"
    )

fadcTrapPeriodBlockIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 431)
)
fadcTrapPeriodBlockIP.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPeriodBlockIP.setStatus(
        "current"
    )

fadcTrapCorsViolateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 432)
)
fadcTrapCorsViolateDetected.setObjects(
    ("FORTINET-FORTIADC-MIB", "fadcSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapCorsViolateDetected.setStatus(
        "current"
    )

fadcTrapThresholdViolateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 433)
)
fadcTrapThresholdViolateDetected.setObjects(
    ("FORTINET-FORTIADC-MIB", "fadcSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapThresholdViolateDetected.setStatus(
        "current"
    )

fadcTrapBiometricsBaseDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 434)
)
fadcTrapBiometricsBaseDetected.setObjects(
    ("FORTINET-FORTIADC-MIB", "fadcSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapBiometricsBaseDetected.setStatus(
        "current"
    )

fadcTrapSysUserLoginFailedAndBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 435)
)
fadcTrapSysUserLoginFailedAndBlocked.setObjects(
    ("FORTINET-FORTIADC-MIB", "fadcSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapSysUserLoginFailedAndBlocked.setStatus(
        "current"
    )

fadcTrapCPUTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 501)
)
fadcTrapCPUTempHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapCPUTempHigh.setStatus(
        "current"
    )

fadcTrapCPUTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 502)
)
fadcTrapCPUTempNormal.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapCPUTempNormal.setStatus(
        "current"
    )

fadcTrapDeviceTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 503)
)
fadcTrapDeviceTempHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDeviceTempHigh.setStatus(
        "current"
    )

fadcTrapDeviceTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 504)
)
fadcTrapDeviceTempNormal.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDeviceTempNormal.setStatus(
        "current"
    )

fadcTrapPSUTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 505)
)
fadcTrapPSUTempHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUTempHigh.setStatus(
        "current"
    )

fadcTrapPSUTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 506)
)
fadcTrapPSUTempNormal.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUTempNormal.setStatus(
        "current"
    )

fadcTrapPSUFanSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 507)
)
fadcTrapPSUFanSlow.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUFanSlow.setStatus(
        "current"
    )

fadcTrapDeviceFanSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 508)
)
fadcTrapDeviceFanSlow.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDeviceFanSlow.setStatus(
        "current"
    )

fadcTrapPSUFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 509)
)
fadcTrapPSUFanBad.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUFanBad.setStatus(
        "current"
    )

fadcTrapPSUFanGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 510)
)
fadcTrapPSUFanGood.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUFanGood.setStatus(
        "current"
    )

fadcTrapDeviceFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 511)
)
fadcTrapDeviceFanBad.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDeviceFanBad.setStatus(
        "current"
    )

fadcTrapDeviceFanGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 512)
)
fadcTrapDeviceFanGood.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDeviceFanGood.setStatus(
        "current"
    )

fadcTrapVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 513)
)
fadcTrapVoltageHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVoltageHigh.setStatus(
        "current"
    )

fadcTrapPowerSupplyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 514)
)
fadcTrapPowerSupplyHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPowerSupplyHigh.setStatus(
        "current"
    )

fadcTrapPSUVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 515)
)
fadcTrapPSUVoltageHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUVoltageHigh.setStatus(
        "current"
    )

fadcTrapVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 516)
)
fadcTrapVoltageLow.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVoltageLow.setStatus(
        "current"
    )

fadcTrapPowerSupplyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 517)
)
fadcTrapPowerSupplyLow.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPowerSupplyLow.setStatus(
        "current"
    )

fadcTrapPSUVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 518)
)
fadcTrapPSUVoltageLow.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUVoltageLow.setStatus(
        "current"
    )

fadcTrapPSUFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 519)
)
fadcTrapPSUFailure.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPSUFailure.setStatus(
        "current"
    )

fadcTrapARPConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 520)
)
fadcTrapARPConflict.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapARPConflict.setStatus(
        "current"
    )

fadcTrapExternalLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 521)
)
fadcTrapExternalLinkChange.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapExternalLinkChange.setStatus(
        "current"
    )

fadcTrapLogDiskCloseThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 522)
)
fadcTrapLogDiskCloseThreshold.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogDiskCloseThreshold.setStatus(
        "current"
    )

fadcTrapLogDiskLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 523)
)
fadcTrapLogDiskLost.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogDiskLost.setStatus(
        "current"
    )

fadcTrapSsdMwiNearThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 524)
)
fadcTrapSsdMwiNearThreshold.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSsdMwiNearThreshold.setStatus(
        "current"
    )

fadcTrapSsdMwiReachedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 525)
)
fadcTrapSsdMwiReachedThreshold.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSsdMwiReachedThreshold.setStatus(
        "current"
    )

fadcTrapHAPeerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 526)
)
fadcTrapHAPeerLost.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapHAPeerLost.setStatus(
        "current"
    )

fadcTrapHAMasterFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 527)
)
fadcTrapHAMasterFailover.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapHAMasterFailover.setStatus(
        "current"
    )

fadcTrapPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 528)
)
fadcTrapPortStatusChange.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapPortStatusChange.setStatus(
        "current"
    )

fadcTrapDiskStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 529)
)
fadcTrapDiskStatusChange.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapDiskStatusChange.setStatus(
        "current"
    )

fadcTrapInetPortExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 530)
)
fadcTrapInetPortExhaustion.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapInetPortExhaustion.setStatus(
        "current"
    )

fadcTrapCertExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 531)
)
fadcTrapCertExpire.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapCertExpire.setStatus(
        "current"
    )

fadcTrapLogicalInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 532)
)
fadcTrapLogicalInterfaceUp.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIADC-MIB", "fadcIntfName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogicalInterfaceUp.setStatus(
        "current"
    )

fadcTrapLogicalInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 533)
)
fadcTrapLogicalInterfaceDown.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIADC-MIB", "fadcIntfName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogicalInterfaceDown.setStatus(
        "current"
    )

fadcTrapLogicalInterfaceDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 534)
)
fadcTrapLogicalInterfaceDisabled.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIADC-MIB", "fadcIntfName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogicalInterfaceDisabled.setStatus(
        "current"
    )

fadcTrapAlertTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 535)
)
fadcTrapAlertTrigger.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertName"))
)
if mibBuilder.loadTexts:
    fadcTrapAlertTrigger.setStatus(
        "current"
    )

fadcTrapSysConnMemHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 536)
)
fadcTrapSysConnMemHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysConnMemHigh.setStatus(
        "current"
    )

fadcTrapSysLicenseExpiryNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 537)
)
fadcTrapSysLicenseExpiryNotif.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysLicenseExpiryNotif.setStatus(
        "current"
    )

fadcTrapSysDeviceRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 538)
)
fadcTrapSysDeviceRebooted.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysDeviceRebooted.setStatus(
        "current"
    )

fadcTrapSysDeviceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 539)
)
fadcTrapSysDeviceStarted.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysDeviceStarted.setStatus(
        "current"
    )

fadcTrapSysUpgradeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 540)
)
fadcTrapSysUpgradeComplete.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysUpgradeComplete.setStatus(
        "current"
    )

fadcTrapSysUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 541)
)
fadcTrapSysUserLogin.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysUserLogin.setStatus(
        "current"
    )

fadcTrapSysUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 542)
)
fadcTrapSysUserLogout.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysUserLogout.setStatus(
        "current"
    )

fadcTrapSysDhcpIpAllocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 543)
)
fadcTrapSysDhcpIpAllocFailure.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysDhcpIpAllocFailure.setStatus(
        "current"
    )

fadcTrapSysMetricsDbDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 544)
)
fadcTrapSysMetricsDbDiskFull.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysMetricsDbDiskFull.setStatus(
        "current"
    )

fadcTrapSysStatisticsDbDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 545)
)
fadcTrapSysStatisticsDbDiskFull.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysStatisticsDbDiskFull.setStatus(
        "current"
    )

fadcTrapSysLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 546)
)
fadcTrapSysLogFull.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysLogFull.setStatus(
        "current"
    )

fadcTrapSysFwBandwidthLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 547)
)
fadcTrapSysFwBandwidthLimit.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysFwBandwidthLimit.setStatus(
        "current"
    )

fadcTrapConfigExecute = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 548)
)
fadcTrapConfigExecute.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapConfigExecute.setStatus(
        "current"
    )

fadcTrapConfigCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 549)
)
fadcTrapConfigCreate.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapConfigCreate.setStatus(
        "current"
    )

fadcTrapConfigDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 550)
)
fadcTrapConfigDelete.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapConfigDelete.setStatus(
        "current"
    )

fadcTrapConfigUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 551)
)
fadcTrapConfigUpdate.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapConfigUpdate.setStatus(
        "current"
    )

fadcTrapSysOcspResponseExpires = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 552)
)
fadcTrapSysOcspResponseExpires.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysOcspResponseExpires.setStatus(
        "current"
    )

fadcTrapSysSslCertificateRevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 553)
)
fadcTrapSysSslCertificateRevoked.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysSslCertificateRevoked.setStatus(
        "current"
    )

fadcTrapSysCrlExpires = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 554)
)
fadcTrapSysCrlExpires.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSysCrlExpires.setStatus(
        "current"
    )

fadcTrapMemberConnRateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 600)
)
fadcTrapMemberConnRateStart.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnRateStart.setStatus(
        "current"
    )

fadcTrapVSConnRateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 601)
)
fadcTrapVSConnRateStart.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSConnRateStart.setStatus(
        "current"
    )

fadcTrapMemberConnLimitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 602)
)
fadcTrapMemberConnLimitStart.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnLimitStart.setStatus(
        "current"
    )

fadcTrapVSConnLimitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 603)
)
fadcTrapVSConnLimitStart.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSConnLimitStart.setStatus(
        "current"
    )

fadcTrapMemberConnRateStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 604)
)
fadcTrapMemberConnRateStop.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnRateStop.setStatus(
        "current"
    )

fadcTrapVSConnRateStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 605)
)
fadcTrapVSConnRateStop.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSConnRateStop.setStatus(
        "current"
    )

fadcTrapMemberConnLimitStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 606)
)
fadcTrapMemberConnLimitStop.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnLimitStop.setStatus(
        "current"
    )

fadcTrapVSConnLimitStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 607)
)
fadcTrapVSConnLimitStop.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSConnLimitStop.setStatus(
        "current"
    )

fadcTrapVSTransactionRateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 608)
)
fadcTrapVSTransactionRateStart.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSTransactionRateStart.setStatus(
        "current"
    )

fadcTrapVSTransactionRateStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 609)
)
fadcTrapVSTransactionRateStop.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSTransactionRateStop.setStatus(
        "current"
    )

fadcTrapMemberHCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 610)
)
fadcTrapMemberHCDown.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapMemberHCDown.setStatus(
        "current"
    )

fadcTrapVSHealthChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 611)
)
fadcTrapVSHealthChange.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSHealthChange.setStatus(
        "current"
    )

fadcTrapMemberHCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 612)
)
fadcTrapMemberHCUp.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapMemberHCUp.setStatus(
        "current"
    )

fadcTrapVSAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 613)
)
fadcTrapVSAuthFail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSAuthFail.setStatus(
        "current"
    )

fadcTrapVSIPPoolLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 614)
)
fadcTrapVSIPPoolLimit.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapVSIPPoolLimit.setStatus(
        "current"
    )

fadcTrapGatewayHCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 615)
)
fadcTrapGatewayHCDown.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGatewayHCDown.setStatus(
        "current"
    )

fadcTrapLinkGroupHCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 616)
)
fadcTrapLinkGroupHCDown.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapLinkGroupHCDown.setStatus(
        "current"
    )

fadcTrapGatewayHCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 617)
)
fadcTrapGatewayHCUp.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGatewayHCUp.setStatus(
        "current"
    )

fadcTrapLinkGroupHCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 618)
)
fadcTrapLinkGroupHCUp.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapLinkGroupHCUp.setStatus(
        "current"
    )

fadcTrapGatewayInboundBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 619)
)
fadcTrapGatewayInboundBandwidth.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGatewayInboundBandwidth.setStatus(
        "current"
    )

fadcTrapGatewayOutboundBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 620)
)
fadcTrapGatewayOutboundBandwidth.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGatewayOutboundBandwidth.setStatus(
        "current"
    )

fadcTrapGatewayInboundSpillover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 621)
)
fadcTrapGatewayInboundSpillover.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGatewayInboundSpillover.setStatus(
        "current"
    )

fadcTrapGatewayOutboundSpillover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 622)
)
fadcTrapGatewayOutboundSpillover.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGatewayOutboundSpillover.setStatus(
        "current"
    )

fadcTrapGatewayTotalSpillover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 623)
)
fadcTrapGatewayTotalSpillover.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGatewayTotalSpillover.setStatus(
        "current"
    )

fadcTrapGlbServerNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 624)
)
fadcTrapGlbServerNotAvail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGlbServerNotAvail.setStatus(
        "current"
    )

fadcTrapGlbServerAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 625)
)
fadcTrapGlbServerAvail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGlbServerAvail.setStatus(
        "current"
    )

fadcTrapGlbVSNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 626)
)
fadcTrapGlbVSNotAvail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGlbVSNotAvail.setStatus(
        "current"
    )

fadcTrapGlbVSAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 627)
)
fadcTrapGlbVSAvail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGlbVSAvail.setStatus(
        "current"
    )

fadcTrapGlbGWNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 633)
)
fadcTrapGlbGWNotAvail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGlbGWNotAvail.setStatus(
        "current"
    )

fadcTrapGlbGWAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 634)
)
fadcTrapGlbGWAvail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapGlbGWAvail.setStatus(
        "current"
    )

fadcTrapSlbPoolDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 635)
)
fadcTrapSlbPoolDown.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbPoolDown.setStatus(
        "current"
    )

fadcTrapSlbPoolUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 636)
)
fadcTrapSlbPoolUp.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbPoolUp.setStatus(
        "current"
    )

fadcTrapSlbPoolHealthChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 637)
)
fadcTrapSlbPoolHealthChange.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbPoolHealthChange.setStatus(
        "current"
    )

fadcTrapSlbServerHealthChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 638)
)
fadcTrapSlbServerHealthChange.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbServerHealthChange.setStatus(
        "current"
    )

fadcTrapSlbServerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 639)
)
fadcTrapSlbServerEnabled.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbServerEnabled.setStatus(
        "current"
    )

fadcTrapSlbServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 640)
)
fadcTrapSlbServerDisabled.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbServerDisabled.setStatus(
        "current"
    )

fadcTrapSlbServerMaintain = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 641)
)
fadcTrapSlbServerMaintain.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbServerMaintain.setStatus(
        "current"
    )

fadcTrapSlbVirtualServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 642)
)
fadcTrapSlbVirtualServerDown.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbVirtualServerDown.setStatus(
        "current"
    )

fadcTrapSlbVirtualServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 643)
)
fadcTrapSlbVirtualServerUp.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbVirtualServerUp.setStatus(
        "current"
    )

fadcTrapSlbVirtualServerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 644)
)
fadcTrapSlbVirtualServerEnabled.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbVirtualServerEnabled.setStatus(
        "current"
    )

fadcTrapSlbVirtualServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 645)
)
fadcTrapSlbVirtualServerDisabled.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbVirtualServerDisabled.setStatus(
        "current"
    )

fadcTrapSlbVirtualServerMaintain = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 646)
)
fadcTrapSlbVirtualServerMaintain.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbVirtualServerMaintain.setStatus(
        "current"
    )

fadcTrapSlbFlowTblHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 647)
)
fadcTrapSlbFlowTblHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbFlowTblHigh.setStatus(
        "current"
    )

fadcTrapSlbPersistTblHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 648)
)
fadcTrapSlbPersistTblHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbPersistTblHigh.setStatus(
        "current"
    )

fadcTrapSlbPktBuffHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 649)
)
fadcTrapSlbPktBuffHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbPktBuffHigh.setStatus(
        "current"
    )

fadcTrapSlbSynCacheUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 650)
)
fadcTrapSlbSynCacheUsageHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbSynCacheUsageHigh.setStatus(
        "current"
    )

fadcTrapSlbSynTblHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 651)
)
fadcTrapSlbSynTblHigh.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbSynTblHigh.setStatus(
        "current"
    )

fadcTrapSlbConnDropMaxFlowTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 652)
)
fadcTrapSlbConnDropMaxFlowTbl.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbConnDropMaxFlowTbl.setStatus(
        "current"
    )

fadcTrapSlbConnDropMaxPersistTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 653)
)
fadcTrapSlbConnDropMaxPersistTbl.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbConnDropMaxPersistTbl.setStatus(
        "current"
    )

fadcTrapSlbConnDropMaxSysTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 654)
)
fadcTrapSlbConnDropMaxSysTbl.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbConnDropMaxSysTbl.setStatus(
        "current"
    )

fadcTrapSlbConnDropNoConnMem = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 655)
)
fadcTrapSlbConnDropNoConnMem.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbConnDropNoConnMem.setStatus(
        "current"
    )

fadcTrapSlbConnDropNoPktBuff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 656)
)
fadcTrapSlbConnDropNoPktBuff.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbConnDropNoPktBuff.setStatus(
        "current"
    )

fadcTrapSlbConnDropPoolLBFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 657)
)
fadcTrapSlbConnDropPoolLBFailure.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbConnDropPoolLBFailure.setStatus(
        "current"
    )

fadcTrapSlbPktDropNoPktBuff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 658)
)
fadcTrapSlbPktDropNoPktBuff.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbPktDropNoPktBuff.setStatus(
        "current"
    )

fadcTrapSlbPktBuffAllocFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 659)
)
fadcTrapSlbPktBuffAllocFail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbPktBuffAllocFail.setStatus(
        "current"
    )

fadcTrapSlbCertExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 660)
)
fadcTrapSlbCertExpire.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbCertExpire.setStatus(
        "current"
    )

fadcTrapSlbCacheOBJAllocFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 661)
)
fadcTrapSlbCacheOBJAllocFail.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapSlbCacheOBJAllocFail.setStatus(
        "current"
    )

fadcTrapLlbVSThroughputLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 112, 0, 662)
)
fadcTrapLlbVSThroughputLimit.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSysSerial"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertPriority"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fadcTrapLlbVSThroughputLimit.setStatus(
        "current"
    )


# Notifications groups

fadcTrapsConformanceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 3)
)
fadcTrapsConformanceGroup.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcTrapCpuHighThreshold"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapMemLowThreshold"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLogDiskHighThreshold"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDosAttackStart"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDosAttackStop"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapFwConnectionLimit"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapFwSnatLimit"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapRequestBlocked"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapXSSAttack"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSQLInjectionAttack"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGenericAttack"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapExploitsAttack"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapTrojansAttack"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapInfoDisclosureAttack"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapURLPattenViolate"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapProtocolConstraint"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGeoViolateDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapReputationViolateDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapBotDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapFwConnectionDeny"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapXmlDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapJsonDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSoapDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDlpDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapHtmlDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapWpdDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapCsrfDetected"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDdosIpFragmentation"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDdosTcpSlowDataAttack"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDdosTcpAccessFlood"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDdosHttpConnectionFlood"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDdosHttpRequestFlood"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDdosHttpAccessLimit"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPeriodBlockIP"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapCPUTempHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapCPUTempNormal"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDeviceTempHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDeviceTempNormal"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUTempHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUTempNormal"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUFanSlow"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDeviceFanSlow"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUFanBad"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUFanGood"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDeviceFanBad"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDeviceFanGood"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVoltageHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPowerSupplyHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUVoltageHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVoltageLow"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPowerSupplyLow"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUVoltageLow"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPSUFailure"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapARPConflict"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapExternalLinkChange"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLogDiskCloseThreshold"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLogDiskLost"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSsdMwiNearThreshold"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSsdMwiReachedThreshold"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapHAPeerLost"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapHAMasterFailover"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapPortStatusChange"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapDiskStatusChange"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapInetPortExhaustion"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapCertExpire"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLogicalInterfaceUp"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLogicalInterfaceDown"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLogicalInterfaceDisabled"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapAlertTrigger"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysConnMemHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysLicenseExpiryNotif"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysDeviceRebooted"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysDeviceStarted"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysUpgradeComplete"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysUserLogin"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysUserLogout"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysDhcpIpAllocFailure"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysMetricsDbDiskFull"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysStatisticsDbDiskFull"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysLogFull"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysFwBandwidthLimit"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapConfigExecute"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapConfigCreate"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapConfigDelete"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapConfigUpdate"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysOcspResponseExpires"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysSslCertificateRevoked"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSysCrlExpires"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapMemberConnRateStart"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSConnRateStart"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapMemberConnLimitStart"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSConnLimitStart"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapMemberConnRateStop"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSConnRateStop"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapMemberConnLimitStop"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSConnLimitStop"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSTransactionRateStart"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSTransactionRateStop"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapMemberHCDown"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSHealthChange"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapMemberHCUp"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSAuthFail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapVSIPPoolLimit"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGatewayHCDown"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLinkGroupHCDown"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGatewayHCUp"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLinkGroupHCUp"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGatewayInboundBandwidth"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGatewayOutboundBandwidth"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGatewayInboundSpillover"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGatewayOutboundSpillover"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGatewayTotalSpillover"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGlbServerNotAvail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGlbServerAvail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGlbVSNotAvail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGlbVSAvail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGlbGWNotAvail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapGlbGWAvail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbPoolDown"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbPoolUp"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbPoolHealthChange"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbServerHealthChange"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbServerEnabled"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbServerDisabled"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbServerMaintain"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbVirtualServerDown"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbVirtualServerUp"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbVirtualServerEnabled"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbVirtualServerDisabled"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbVirtualServerMaintain"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbFlowTblHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbPersistTblHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbPktBuffHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbSynCacheUsageHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbSynTblHigh"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbConnDropMaxFlowTbl"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbConnDropMaxPersistTbl"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbConnDropMaxSysTbl"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbConnDropNoConnMem"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbConnDropNoPktBuff"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbConnDropPoolLBFailure"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbPktDropNoPktBuff"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbPktBuffAllocFail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbCertExpire"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapSlbCacheOBJAllocFail"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapLlbVSThroughputLimit"))
)
if mibBuilder.loadTexts:
    fadcTrapsConformanceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fadcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 112, 600, 100)
)
fadcMIBCompliance.setObjects(
      *(("FORTINET-FORTIADC-MIB", "fadcSystemConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcSysOptionsConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcTrapsConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcHAModeConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcAlertConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcCertConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcVdomConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcVSConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcIntfConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcAdminConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcHardwareConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcSecurityConformanceGroup"),
        ("FORTINET-FORTIADC-MIB", "fadcApplicationConformanceGroup"))
)
if mibBuilder.loadTexts:
    fadcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIADC-MIB",
    **{"FadcHAModeVal": FadcHAModeVal,
       "FadcVdIndex": FadcVdIndex,
       "FadcHaState": FadcHaState,
       "fnFortiADCMib": fnFortiADCMib,
       "fadcTraps": fadcTraps,
       "fadcTrapCpuHighThreshold": fadcTrapCpuHighThreshold,
       "fadcTrapMemLowThreshold": fadcTrapMemLowThreshold,
       "fadcTrapLogDiskHighThreshold": fadcTrapLogDiskHighThreshold,
       "fadcTrapDosAttackStart": fadcTrapDosAttackStart,
       "fadcTrapDosAttackStop": fadcTrapDosAttackStop,
       "fadcTrapFwConnectionLimit": fadcTrapFwConnectionLimit,
       "fadcTrapFwSnatLimit": fadcTrapFwSnatLimit,
       "fadcTrapRequestBlocked": fadcTrapRequestBlocked,
       "fadcTrapXSSAttack": fadcTrapXSSAttack,
       "fadcTrapSQLInjectionAttack": fadcTrapSQLInjectionAttack,
       "fadcTrapGenericAttack": fadcTrapGenericAttack,
       "fadcTrapExploitsAttack": fadcTrapExploitsAttack,
       "fadcTrapTrojansAttack": fadcTrapTrojansAttack,
       "fadcTrapInfoDisclosureAttack": fadcTrapInfoDisclosureAttack,
       "fadcTrapURLPattenViolate": fadcTrapURLPattenViolate,
       "fadcTrapProtocolConstraint": fadcTrapProtocolConstraint,
       "fadcTrapGeoViolateDetected": fadcTrapGeoViolateDetected,
       "fadcTrapReputationViolateDetected": fadcTrapReputationViolateDetected,
       "fadcTrapBotDetected": fadcTrapBotDetected,
       "fadcTrapFwConnectionDeny": fadcTrapFwConnectionDeny,
       "fadcTrapXmlDetected": fadcTrapXmlDetected,
       "fadcTrapJsonDetected": fadcTrapJsonDetected,
       "fadcTrapSoapDetected": fadcTrapSoapDetected,
       "fadcTrapDlpDetected": fadcTrapDlpDetected,
       "fadcTrapHtmlDetected": fadcTrapHtmlDetected,
       "fadcTrapWpdDetected": fadcTrapWpdDetected,
       "fadcTrapCsrfDetected": fadcTrapCsrfDetected,
       "fadcTrapDdosIpFragmentation": fadcTrapDdosIpFragmentation,
       "fadcTrapDdosTcpSlowDataAttack": fadcTrapDdosTcpSlowDataAttack,
       "fadcTrapDdosTcpAccessFlood": fadcTrapDdosTcpAccessFlood,
       "fadcTrapDdosHttpConnectionFlood": fadcTrapDdosHttpConnectionFlood,
       "fadcTrapDdosHttpRequestFlood": fadcTrapDdosHttpRequestFlood,
       "fadcTrapDdosHttpAccessLimit": fadcTrapDdosHttpAccessLimit,
       "fadcTrapPeriodBlockIP": fadcTrapPeriodBlockIP,
       "fadcTrapCorsViolateDetected": fadcTrapCorsViolateDetected,
       "fadcTrapThresholdViolateDetected": fadcTrapThresholdViolateDetected,
       "fadcTrapBiometricsBaseDetected": fadcTrapBiometricsBaseDetected,
       "fadcTrapSysUserLoginFailedAndBlocked": fadcTrapSysUserLoginFailedAndBlocked,
       "fadcTrapCPUTempHigh": fadcTrapCPUTempHigh,
       "fadcTrapCPUTempNormal": fadcTrapCPUTempNormal,
       "fadcTrapDeviceTempHigh": fadcTrapDeviceTempHigh,
       "fadcTrapDeviceTempNormal": fadcTrapDeviceTempNormal,
       "fadcTrapPSUTempHigh": fadcTrapPSUTempHigh,
       "fadcTrapPSUTempNormal": fadcTrapPSUTempNormal,
       "fadcTrapPSUFanSlow": fadcTrapPSUFanSlow,
       "fadcTrapDeviceFanSlow": fadcTrapDeviceFanSlow,
       "fadcTrapPSUFanBad": fadcTrapPSUFanBad,
       "fadcTrapPSUFanGood": fadcTrapPSUFanGood,
       "fadcTrapDeviceFanBad": fadcTrapDeviceFanBad,
       "fadcTrapDeviceFanGood": fadcTrapDeviceFanGood,
       "fadcTrapVoltageHigh": fadcTrapVoltageHigh,
       "fadcTrapPowerSupplyHigh": fadcTrapPowerSupplyHigh,
       "fadcTrapPSUVoltageHigh": fadcTrapPSUVoltageHigh,
       "fadcTrapVoltageLow": fadcTrapVoltageLow,
       "fadcTrapPowerSupplyLow": fadcTrapPowerSupplyLow,
       "fadcTrapPSUVoltageLow": fadcTrapPSUVoltageLow,
       "fadcTrapPSUFailure": fadcTrapPSUFailure,
       "fadcTrapARPConflict": fadcTrapARPConflict,
       "fadcTrapExternalLinkChange": fadcTrapExternalLinkChange,
       "fadcTrapLogDiskCloseThreshold": fadcTrapLogDiskCloseThreshold,
       "fadcTrapLogDiskLost": fadcTrapLogDiskLost,
       "fadcTrapSsdMwiNearThreshold": fadcTrapSsdMwiNearThreshold,
       "fadcTrapSsdMwiReachedThreshold": fadcTrapSsdMwiReachedThreshold,
       "fadcTrapHAPeerLost": fadcTrapHAPeerLost,
       "fadcTrapHAMasterFailover": fadcTrapHAMasterFailover,
       "fadcTrapPortStatusChange": fadcTrapPortStatusChange,
       "fadcTrapDiskStatusChange": fadcTrapDiskStatusChange,
       "fadcTrapInetPortExhaustion": fadcTrapInetPortExhaustion,
       "fadcTrapCertExpire": fadcTrapCertExpire,
       "fadcTrapLogicalInterfaceUp": fadcTrapLogicalInterfaceUp,
       "fadcTrapLogicalInterfaceDown": fadcTrapLogicalInterfaceDown,
       "fadcTrapLogicalInterfaceDisabled": fadcTrapLogicalInterfaceDisabled,
       "fadcTrapAlertTrigger": fadcTrapAlertTrigger,
       "fadcTrapSysConnMemHigh": fadcTrapSysConnMemHigh,
       "fadcTrapSysLicenseExpiryNotif": fadcTrapSysLicenseExpiryNotif,
       "fadcTrapSysDeviceRebooted": fadcTrapSysDeviceRebooted,
       "fadcTrapSysDeviceStarted": fadcTrapSysDeviceStarted,
       "fadcTrapSysUpgradeComplete": fadcTrapSysUpgradeComplete,
       "fadcTrapSysUserLogin": fadcTrapSysUserLogin,
       "fadcTrapSysUserLogout": fadcTrapSysUserLogout,
       "fadcTrapSysDhcpIpAllocFailure": fadcTrapSysDhcpIpAllocFailure,
       "fadcTrapSysMetricsDbDiskFull": fadcTrapSysMetricsDbDiskFull,
       "fadcTrapSysStatisticsDbDiskFull": fadcTrapSysStatisticsDbDiskFull,
       "fadcTrapSysLogFull": fadcTrapSysLogFull,
       "fadcTrapSysFwBandwidthLimit": fadcTrapSysFwBandwidthLimit,
       "fadcTrapConfigExecute": fadcTrapConfigExecute,
       "fadcTrapConfigCreate": fadcTrapConfigCreate,
       "fadcTrapConfigDelete": fadcTrapConfigDelete,
       "fadcTrapConfigUpdate": fadcTrapConfigUpdate,
       "fadcTrapSysOcspResponseExpires": fadcTrapSysOcspResponseExpires,
       "fadcTrapSysSslCertificateRevoked": fadcTrapSysSslCertificateRevoked,
       "fadcTrapSysCrlExpires": fadcTrapSysCrlExpires,
       "fadcTrapMemberConnRateStart": fadcTrapMemberConnRateStart,
       "fadcTrapVSConnRateStart": fadcTrapVSConnRateStart,
       "fadcTrapMemberConnLimitStart": fadcTrapMemberConnLimitStart,
       "fadcTrapVSConnLimitStart": fadcTrapVSConnLimitStart,
       "fadcTrapMemberConnRateStop": fadcTrapMemberConnRateStop,
       "fadcTrapVSConnRateStop": fadcTrapVSConnRateStop,
       "fadcTrapMemberConnLimitStop": fadcTrapMemberConnLimitStop,
       "fadcTrapVSConnLimitStop": fadcTrapVSConnLimitStop,
       "fadcTrapVSTransactionRateStart": fadcTrapVSTransactionRateStart,
       "fadcTrapVSTransactionRateStop": fadcTrapVSTransactionRateStop,
       "fadcTrapMemberHCDown": fadcTrapMemberHCDown,
       "fadcTrapVSHealthChange": fadcTrapVSHealthChange,
       "fadcTrapMemberHCUp": fadcTrapMemberHCUp,
       "fadcTrapVSAuthFail": fadcTrapVSAuthFail,
       "fadcTrapVSIPPoolLimit": fadcTrapVSIPPoolLimit,
       "fadcTrapGatewayHCDown": fadcTrapGatewayHCDown,
       "fadcTrapLinkGroupHCDown": fadcTrapLinkGroupHCDown,
       "fadcTrapGatewayHCUp": fadcTrapGatewayHCUp,
       "fadcTrapLinkGroupHCUp": fadcTrapLinkGroupHCUp,
       "fadcTrapGatewayInboundBandwidth": fadcTrapGatewayInboundBandwidth,
       "fadcTrapGatewayOutboundBandwidth": fadcTrapGatewayOutboundBandwidth,
       "fadcTrapGatewayInboundSpillover": fadcTrapGatewayInboundSpillover,
       "fadcTrapGatewayOutboundSpillover": fadcTrapGatewayOutboundSpillover,
       "fadcTrapGatewayTotalSpillover": fadcTrapGatewayTotalSpillover,
       "fadcTrapGlbServerNotAvail": fadcTrapGlbServerNotAvail,
       "fadcTrapGlbServerAvail": fadcTrapGlbServerAvail,
       "fadcTrapGlbVSNotAvail": fadcTrapGlbVSNotAvail,
       "fadcTrapGlbVSAvail": fadcTrapGlbVSAvail,
       "fadcTrapGlbGWNotAvail": fadcTrapGlbGWNotAvail,
       "fadcTrapGlbGWAvail": fadcTrapGlbGWAvail,
       "fadcTrapSlbPoolDown": fadcTrapSlbPoolDown,
       "fadcTrapSlbPoolUp": fadcTrapSlbPoolUp,
       "fadcTrapSlbPoolHealthChange": fadcTrapSlbPoolHealthChange,
       "fadcTrapSlbServerHealthChange": fadcTrapSlbServerHealthChange,
       "fadcTrapSlbServerEnabled": fadcTrapSlbServerEnabled,
       "fadcTrapSlbServerDisabled": fadcTrapSlbServerDisabled,
       "fadcTrapSlbServerMaintain": fadcTrapSlbServerMaintain,
       "fadcTrapSlbVirtualServerDown": fadcTrapSlbVirtualServerDown,
       "fadcTrapSlbVirtualServerUp": fadcTrapSlbVirtualServerUp,
       "fadcTrapSlbVirtualServerEnabled": fadcTrapSlbVirtualServerEnabled,
       "fadcTrapSlbVirtualServerDisabled": fadcTrapSlbVirtualServerDisabled,
       "fadcTrapSlbVirtualServerMaintain": fadcTrapSlbVirtualServerMaintain,
       "fadcTrapSlbFlowTblHigh": fadcTrapSlbFlowTblHigh,
       "fadcTrapSlbPersistTblHigh": fadcTrapSlbPersistTblHigh,
       "fadcTrapSlbPktBuffHigh": fadcTrapSlbPktBuffHigh,
       "fadcTrapSlbSynCacheUsageHigh": fadcTrapSlbSynCacheUsageHigh,
       "fadcTrapSlbSynTblHigh": fadcTrapSlbSynTblHigh,
       "fadcTrapSlbConnDropMaxFlowTbl": fadcTrapSlbConnDropMaxFlowTbl,
       "fadcTrapSlbConnDropMaxPersistTbl": fadcTrapSlbConnDropMaxPersistTbl,
       "fadcTrapSlbConnDropMaxSysTbl": fadcTrapSlbConnDropMaxSysTbl,
       "fadcTrapSlbConnDropNoConnMem": fadcTrapSlbConnDropNoConnMem,
       "fadcTrapSlbConnDropNoPktBuff": fadcTrapSlbConnDropNoPktBuff,
       "fadcTrapSlbConnDropPoolLBFailure": fadcTrapSlbConnDropPoolLBFailure,
       "fadcTrapSlbPktDropNoPktBuff": fadcTrapSlbPktDropNoPktBuff,
       "fadcTrapSlbPktBuffAllocFail": fadcTrapSlbPktBuffAllocFail,
       "fadcTrapSlbCertExpire": fadcTrapSlbCertExpire,
       "fadcTrapSlbCacheOBJAllocFail": fadcTrapSlbCacheOBJAllocFail,
       "fadcTrapLlbVSThroughputLimit": fadcTrapLlbVSThroughputLimit,
       "fadcSystem": fadcSystem,
       "fadcSysModel": fadcSysModel,
       "fadcSysSerial": fadcSysSerial,
       "fadcSysVersion": fadcSysVersion,
       "fadcSysCpuUsage": fadcSysCpuUsage,
       "fadcSysMemUsage": fadcSysMemUsage,
       "fadcSysLogDiskUsage": fadcSysLogDiskUsage,
       "fadcSysLoad": fadcSysLoad,
       "fadcSysCpuUsageTable": fadcSysCpuUsageTable,
       "fadcSysCpuUsageEntry": fadcSysCpuUsageEntry,
       "fadcCpuIndex": fadcCpuIndex,
       "fadcCpuName": fadcCpuName,
       "fadcCpu2secAvgUsage": fadcCpu2secAvgUsage,
       "fadcCpu1minAvgUsage": fadcCpu1minAvgUsage,
       "fadcCpu5minAvgUsage": fadcCpu5minAvgUsage,
       "fadcSysOptions": fadcSysOptions,
       "fadcSysOptIdleTimeout": fadcSysOptIdleTimeout,
       "fadcSysHA": fadcSysHA,
       "fadcHAMode": fadcHAMode,
       "fadcSysAlert": fadcSysAlert,
       "fadcSysAlertTable": fadcSysAlertTable,
       "fadcSysAlertEntry": fadcSysAlertEntry,
       "fadcAlertIndex": fadcAlertIndex,
       "fadcAlertName": fadcAlertName,
       "fadcAlertSourceType": fadcAlertSourceType,
       "fadcAlertPriority": fadcAlertPriority,
       "fadcAlertComments": fadcAlertComments,
       "fadcAlertVdomName": fadcAlertVdomName,
       "fadcSysCert": fadcSysCert,
       "fadcLocalCertTables": fadcLocalCertTables,
       "fadcLocalCertTable": fadcLocalCertTable,
       "fadcLocalCertEntry": fadcLocalCertEntry,
       "fadcLocalCertIndex": fadcLocalCertIndex,
       "fadcLocalCertName": fadcLocalCertName,
       "fadcLocalCertValidFrom": fadcLocalCertValidFrom,
       "fadcLocalCertValidTo": fadcLocalCertValidTo,
       "fadcLocalCertVdom": fadcLocalCertVdom,
       "fadcIntermediateCATables": fadcIntermediateCATables,
       "fadcIntermediateCATable": fadcIntermediateCATable,
       "fadcIntermediateCAEntry": fadcIntermediateCAEntry,
       "fadcIntermediateCAIndex": fadcIntermediateCAIndex,
       "fadcIntermediateCAName": fadcIntermediateCAName,
       "fadcIntermediateCAValidFrom": fadcIntermediateCAValidFrom,
       "fadcIntermediateCAValidTo": fadcIntermediateCAValidTo,
       "fadcIntermediateCAVdom": fadcIntermediateCAVdom,
       "fadcCACertTables": fadcCACertTables,
       "fadcCACertTable": fadcCACertTable,
       "fadcCACertEntry": fadcCACertEntry,
       "fadcCACertIndex": fadcCACertIndex,
       "fadcCACertName": fadcCACertName,
       "fadcCACertValidFrom": fadcCACertValidFrom,
       "fadcCACertValidTo": fadcCACertValidTo,
       "fadcCACertVdom": fadcCACertVdom,
       "fadcRemoteCertTables": fadcRemoteCertTables,
       "fadcRemoteCertTable": fadcRemoteCertTable,
       "fadcRemoteCertEntry": fadcRemoteCertEntry,
       "fadcRemoteCertIndex": fadcRemoteCertIndex,
       "fadcRemoteCertName": fadcRemoteCertName,
       "fadcRemoteCertValidFrom": fadcRemoteCertValidFrom,
       "fadcRemoteCertValidTo": fadcRemoteCertValidTo,
       "fadcRemoteCertVdom": fadcRemoteCertVdom,
       "fadcVirtualDomain": fadcVirtualDomain,
       "fadcVdInfo": fadcVdInfo,
       "fadcVdNumber": fadcVdNumber,
       "fadcVdMaxVdoms": fadcVdMaxVdoms,
       "fadcVdEnabled": fadcVdEnabled,
       "fadcVdTables": fadcVdTables,
       "fadcVdTable": fadcVdTable,
       "fadcVdEntry": fadcVdEntry,
       "fadcVdEntIndex": fadcVdEntIndex,
       "fadcVdEntName": fadcVdEntName,
       "fadcVdEntHaState": fadcVdEntHaState,
       "fadcVirtualServer": fadcVirtualServer,
       "fadcVSNumber": fadcVSNumber,
       "fadcVSTable": fadcVSTable,
       "fadcVSEntry": fadcVSEntry,
       "fadcVSIndex": fadcVSIndex,
       "fadcVSName": fadcVSName,
       "fadcVSStatus": fadcVSStatus,
       "fadcVSHealth": fadcVSHealth,
       "fadcVSNewConnections": fadcVSNewConnections,
       "fadcVSConcurrent": fadcVSConcurrent,
       "fadcVSThroughputKbps": fadcVSThroughputKbps,
       "fadcVSVdom": fadcVSVdom,
       "fadcIntf": fadcIntf,
       "fadcIntfTable": fadcIntfTable,
       "fadcIntfEntry": fadcIntfEntry,
       "fadcIntfIndex": fadcIntfIndex,
       "fadcIntfName": fadcIntfName,
       "fadcIntfVdom": fadcIntfVdom,
       "fadcAdmin": fadcAdmin,
       "fadcAdminTable": fadcAdminTable,
       "fadcAdminEntry": fadcAdminEntry,
       "fadcAdminIndex": fadcAdminIndex,
       "fadcAdminName": fadcAdminName,
       "fadcAdminVdom": fadcAdminVdom,
       "fadcHardware": fadcHardware,
       "fadcCPUInfo": fadcCPUInfo,
       "fadcCPUTable": fadcCPUTable,
       "fadcCPUEntry": fadcCPUEntry,
       "fadcCPUIndex": fadcCPUIndex,
       "fadcCPUName": fadcCPUName,
       "fadcCPUTemp": fadcCPUTemp,
       "fadcPSUInfo": fadcPSUInfo,
       "fadcPSUTable": fadcPSUTable,
       "fadcPSUEntry": fadcPSUEntry,
       "fadcPSUIndex": fadcPSUIndex,
       "fadcPSUName": fadcPSUName,
       "fadcPSUTemp": fadcPSUTemp,
       "fadcPSUFanSpeed": fadcPSUFanSpeed,
       "fadcPSUFanStatus": fadcPSUFanStatus,
       "fadcPSUVoltage": fadcPSUVoltage,
       "fadcPSUStatus": fadcPSUStatus,
       "fadcNetworkInfo": fadcNetworkInfo,
       "fadcNetworkTable": fadcNetworkTable,
       "fadcNetworkEntry": fadcNetworkEntry,
       "fadcNetworkIndex": fadcNetworkIndex,
       "fadcPortLinkName": fadcPortLinkName,
       "fadcPortLinkStatus": fadcPortLinkStatus,
       "fadcDeviceInfo": fadcDeviceInfo,
       "fadcDeviceTempTables": fadcDeviceTempTables,
       "fadcDeviceTempTable": fadcDeviceTempTable,
       "fadcDeviceTempEntry": fadcDeviceTempEntry,
       "fadcDeviceTempIndex": fadcDeviceTempIndex,
       "fadcDeviceTempName": fadcDeviceTempName,
       "fadcDeviceTempValue": fadcDeviceTempValue,
       "fadcDeviceFanTables": fadcDeviceFanTables,
       "fadcDeviceFanTable": fadcDeviceFanTable,
       "fadcDeviceFanEntry": fadcDeviceFanEntry,
       "fadcDeviceFanIndex": fadcDeviceFanIndex,
       "fadcDeviceFanName": fadcDeviceFanName,
       "fadcDeviceFanSpeed": fadcDeviceFanSpeed,
       "fadcDeviceFanStatus": fadcDeviceFanStatus,
       "fadcHA": fadcHA,
       "fadcHACurMode": fadcHACurMode,
       "fadcHACurState": fadcHACurState,
       "fadcHAPeerCount": fadcHAPeerCount,
       "fadcMonitorIntfCount": fadcMonitorIntfCount,
       "fadcDiskState": fadcDiskState,
       "fadcHALastChangedTime": fadcHALastChangedTime,
       "fadcHALastChangedReason": fadcHALastChangedReason,
       "fadcSyncStats": fadcSyncStats,
       "fadcHASyncStatsTable": fadcHASyncStatsTable,
       "fadcHASyncStatsEntry": fadcHASyncStatsEntry,
       "fadcSyncTypeIndex": fadcSyncTypeIndex,
       "fadcSyncType": fadcSyncType,
       "fadcSyncSent": fadcSyncSent,
       "fadcSyncReceived": fadcSyncReceived,
       "fadcDeviceErrCount": fadcDeviceErrCount,
       "fadcDuplicateNodeID": fadcDuplicateNodeID,
       "fadcVersionMismatch": fadcVersionMismatch,
       "fadcHAPeerInfo": fadcHAPeerInfo,
       "fadcHAPeerTable": fadcHAPeerTable,
       "fadcHAPeerEntry": fadcHAPeerEntry,
       "fadcPeerIndex": fadcPeerIndex,
       "fadcPeerSerialNumber": fadcPeerSerialNumber,
       "fadcPeerStatus": fadcPeerStatus,
       "fadcNodeID": fadcNodeID,
       "fadcIPAddress": fadcIPAddress,
       "fadcVoltage": fadcVoltage,
       "fadcPowerSupplyVoltage": fadcPowerSupplyVoltage,
       "fadcLogDiskStatus": fadcLogDiskStatus,
       "fadcSecurity": fadcSecurity,
       "fadcDDoSAttackStatus": fadcDDoSAttackStatus,
       "fadcApplication": fadcApplication,
       "fadcRS": fadcRS,
       "fadcPoolNumber": fadcPoolNumber,
       "fadcRSNumber": fadcRSNumber,
       "fadcRSTable": fadcRSTable,
       "fadcRSEntry": fadcRSEntry,
       "fadcRSIndex": fadcRSIndex,
       "fadcPoolName": fadcPoolName,
       "fadcRSStatus": fadcRSStatus,
       "fadcRSHealth": fadcRSHealth,
       "fadcRSVdom": fadcRSVdom,
       "fadcRSName": fadcRSName,
       "fadcRSObjStatus": fadcRSObjStatus,
       "fadcVS": fadcVS,
       "fadcVirtualServerNumber": fadcVirtualServerNumber,
       "fadcVirtualServerTable": fadcVirtualServerTable,
       "fadcVirtualServerEntry": fadcVirtualServerEntry,
       "fadcVirtualServerIndex": fadcVirtualServerIndex,
       "fadcVirtualServerName": fadcVirtualServerName,
       "fadcVirtualServerStatus": fadcVirtualServerStatus,
       "fadcVirtualServerHealth": fadcVirtualServerHealth,
       "fadcVirtualServerNewConnections": fadcVirtualServerNewConnections,
       "fadcVirtualServerConcurrent": fadcVirtualServerConcurrent,
       "fadcVirtualServerThroughputKbps": fadcVirtualServerThroughputKbps,
       "fadcVirtualServerVdom": fadcVirtualServerVdom,
       "fadcVirtualServerWAF": fadcVirtualServerWAF,
       "fadcLinkLoadBalance": fadcLinkLoadBalance,
       "fadcGatewayTables": fadcGatewayTables,
       "fadcGatewayTable": fadcGatewayTable,
       "fadcGatewayEntry": fadcGatewayEntry,
       "fadcGatewayIndex": fadcGatewayIndex,
       "fadcGatewayName": fadcGatewayName,
       "fadcGatewayHCStatus": fadcGatewayHCStatus,
       "fadcGatewayInboundBandWidth": fadcGatewayInboundBandWidth,
       "fadcGatewayOutboundBandWidth": fadcGatewayOutboundBandWidth,
       "fadcGatewayVdom": fadcGatewayVdom,
       "fadcLinkGroupTables": fadcLinkGroupTables,
       "fadcLinkGroupTable": fadcLinkGroupTable,
       "fadcLinkGroupEntry": fadcLinkGroupEntry,
       "fadcLinkGroupIndex": fadcLinkGroupIndex,
       "fadcLinkGroupName": fadcLinkGroupName,
       "fadcLinkGroupHCStatus": fadcLinkGroupHCStatus,
       "fadcLinkGroupMode": fadcLinkGroupMode,
       "fadcLinkGroupVdom": fadcLinkGroupVdom,
       "fadcGlobalLoadBalance": fadcGlobalLoadBalance,
       "fadcGLBVSTables": fadcGLBVSTables,
       "fadcGLBVSTable": fadcGLBVSTable,
       "fadcGLBVSEntry": fadcGLBVSEntry,
       "fadcGLBVSIndex": fadcGLBVSIndex,
       "fadcGLBVSName": fadcGLBVSName,
       "fadcGLBVSStatus": fadcGLBVSStatus,
       "fadcGLBVSServerName": fadcGLBVSServerName,
       "fadcGLBVSVdom": fadcGLBVSVdom,
       "fadcGLBServerTables": fadcGLBServerTables,
       "fadcGLBServerTable": fadcGLBServerTable,
       "fadcGLBServerEntry": fadcGLBServerEntry,
       "fadcGLBServerIndex": fadcGLBServerIndex,
       "fadcGLBServerName": fadcGLBServerName,
       "fadcGLBServerStatus": fadcGLBServerStatus,
       "fadcGLBServerVdom": fadcGLBServerVdom,
       "fadcGLBGatewayTables": fadcGLBGatewayTables,
       "fadcGLBGatewayTable": fadcGLBGatewayTable,
       "fadcGLBGatewayEntry": fadcGLBGatewayEntry,
       "fadcGLBGatewayIndex": fadcGLBGatewayIndex,
       "fadcGLBGatewayName": fadcGLBGatewayName,
       "fadcGLBGatewayStatus": fadcGLBGatewayStatus,
       "fadcGLBGatewayServerName": fadcGLBGatewayServerName,
       "fadcGLBGatewayVdom": fadcGLBGatewayVdom,
       "fadcServerLoadBalance": fadcServerLoadBalance,
       "fadcClientSideCPS": fadcClientSideCPS,
       "fadcClientSideRPS": fadcClientSideRPS,
       "fadcClientSideSSLCPS": fadcClientSideSSLCPS,
       "fadcClientSideSSLRPS": fadcClientSideSSLRPS,
       "fadcClientSideThroughput": fadcClientSideThroughput,
       "fadcClientSideSSLThroughput": fadcClientSideSSLThroughput,
       "fadcConcurrentClientConnections": fadcConcurrentClientConnections,
       "fadcConcurrentClientSSLSessions": fadcConcurrentClientSSLSessions,
       "fadcClientSSLCacheUtilizeTables": fadcClientSSLCacheUtilizeTables,
       "fadcClientSSLCacheUtilizeTable": fadcClientSSLCacheUtilizeTable,
       "fadcClientSSLCacheUtilizeEntry": fadcClientSSLCacheUtilizeEntry,
       "fadcSLBVSIndex": fadcSLBVSIndex,
       "fadcSLBVSName": fadcSLBVSName,
       "fadcSLBTotalCacheItems": fadcSLBTotalCacheItems,
       "fadcSLBTotalCacheSize": fadcSLBTotalCacheSize,
       "fadcSLBCacheHitCount": fadcSLBCacheHitCount,
       "fadcSLBCacheHitBytes": fadcSLBCacheHitBytes,
       "fadcSLBTotalCertCacheItems": fadcSLBTotalCertCacheItems,
       "fadcSLBTotalCertCacheSize": fadcSLBTotalCertCacheSize,
       "fadcSLBHitCertCacheCount": fadcSLBHitCertCacheCount,
       "fadcSLBHitCertTotalCheck": fadcSLBHitCertTotalCheck,
       "fadcSLBHitCertPercentage": fadcSLBHitCertPercentage,
       "fadcModel": fadcModel,
       "fadcUnknown": fadcUnknown,
       "fadcDEV": fadcDEV,
       "fadcKVM": fadcKVM,
       "fadcVM": fadcVM,
       "fadc60F": fadc60F,
       "fadc100D": fadc100D,
       "fadc100F": fadc100F,
       "fadc200D": fadc200D,
       "fadc200F": fadc200F,
       "fadc300D": fadc300D,
       "fadc300E": fadc300E,
       "fadc300F": fadc300F,
       "fadc320F": fadc320F,
       "fadc400D": fadc400D,
       "fadc400F": fadc400F,
       "fadc420F": fadc420F,
       "fadc700D": fadc700D,
       "fadc1000D": fadc1000D,
       "fadc1000F": fadc1000F,
       "fadc1200F": fadc1200F,
       "fadc1500D": fadc1500D,
       "fadc2000D": fadc2000D,
       "fadc2000F": fadc2000F,
       "fadc2200F": fadc2200F,
       "fadc4000D": fadc4000D,
       "fadc4000F": fadc4000F,
       "fadc4200F": fadc4200F,
       "fadc5000F": fadc5000F,
       "fadcMIBConformance": fadcMIBConformance,
       "fadcSystemConformanceGroup": fadcSystemConformanceGroup,
       "fadcSysOptionsConformanceGroup": fadcSysOptionsConformanceGroup,
       "fadcTrapsConformanceGroup": fadcTrapsConformanceGroup,
       "fadcHAModeConformanceGroup": fadcHAModeConformanceGroup,
       "fadcAlertConformanceGroup": fadcAlertConformanceGroup,
       "fadcCertConformanceGroup": fadcCertConformanceGroup,
       "fadcVdomConformanceGroup": fadcVdomConformanceGroup,
       "fadcVSConformanceGroup": fadcVSConformanceGroup,
       "fadcIntfConformanceGroup": fadcIntfConformanceGroup,
       "fadcAdminConformanceGroup": fadcAdminConformanceGroup,
       "fadcHardwareConformanceGroup": fadcHardwareConformanceGroup,
       "fadcSecurityConformanceGroup": fadcSecurityConformanceGroup,
       "fadcApplicationConformanceGroup": fadcApplicationConformanceGroup,
       "fadcMIBCompliance": fadcMIBCompliance}
)
