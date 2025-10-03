# SNMP MIB module (ROSMGMT-ALARM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\ROSMGMT-ALARM-MGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:04 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rosMgmt,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "rosMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rosMgmtAlarmMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34)
)
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmt.setRevisions(
        ("2020-06-18 00:00",
         "2011-03-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmStorageMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("loop", 2))
    )



class AlarmInverseMode(TextualConvention, Integer32):
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
        *(("none", 1),
          ("auto", 2),
          ("manual", 3),
          ("autofinish", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RosMgmtAlarmMgmtObejcts_ObjectIdentity = ObjectIdentity
rosMgmtAlarmMgmtObejcts = _RosMgmtAlarmMgmtObejcts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1)
)
_RosMgmtAlarmMgmtScalarGroup_ObjectIdentity = ObjectIdentity
rosMgmtAlarmMgmtScalarGroup = _RosMgmtAlarmMgmtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1)
)


class _RosMgmtAlarmMgmtRaiseDelay_Type(Integer32):
    """Custom type rosMgmtAlarmMgmtRaiseDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_RosMgmtAlarmMgmtRaiseDelay_Type.__name__ = "Integer32"
_RosMgmtAlarmMgmtRaiseDelay_Object = MibScalar
rosMgmtAlarmMgmtRaiseDelay = _RosMgmtAlarmMgmtRaiseDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 1),
    _RosMgmtAlarmMgmtRaiseDelay_Type()
)
rosMgmtAlarmMgmtRaiseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtRaiseDelay.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtRaiseDelay.setUnits("seconds")


class _RosMgmtAlarmMgmtClearDelay_Type(Integer32):
    """Custom type rosMgmtAlarmMgmtClearDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_RosMgmtAlarmMgmtClearDelay_Type.__name__ = "Integer32"
_RosMgmtAlarmMgmtClearDelay_Object = MibScalar
rosMgmtAlarmMgmtClearDelay = _RosMgmtAlarmMgmtClearDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 2),
    _RosMgmtAlarmMgmtClearDelay_Type()
)
rosMgmtAlarmMgmtClearDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtClearDelay.setStatus("current")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtClearDelay.setUnits("seconds")
_RosMgmtAlarmMgmtActiveStoreMode_Type = AlarmStorageMode
_RosMgmtAlarmMgmtActiveStoreMode_Object = MibScalar
rosMgmtAlarmMgmtActiveStoreMode = _RosMgmtAlarmMgmtActiveStoreMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 3),
    _RosMgmtAlarmMgmtActiveStoreMode_Type()
)
rosMgmtAlarmMgmtActiveStoreMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtActiveStoreMode.setStatus("current")


class _RosMgmtAlarmMgmtInhibitEnable_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtInhibitEnable based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtInhibitEnable_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtInhibitEnable_Object = MibScalar
rosMgmtAlarmMgmtInhibitEnable = _RosMgmtAlarmMgmtInhibitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 4),
    _RosMgmtAlarmMgmtInhibitEnable_Type()
)
rosMgmtAlarmMgmtInhibitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtInhibitEnable.setStatus("current")


class _RosMgmtAlarmMgmtSyslogEnable_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtSyslogEnable based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtSyslogEnable_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtSyslogEnable_Object = MibScalar
rosMgmtAlarmMgmtSyslogEnable = _RosMgmtAlarmMgmtSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 5),
    _RosMgmtAlarmMgmtSyslogEnable_Type()
)
rosMgmtAlarmMgmtSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtSyslogEnable.setStatus("current")
_RosMgmtAlarmMgmtActiveClear_Type = Integer32
_RosMgmtAlarmMgmtActiveClear_Object = MibScalar
rosMgmtAlarmMgmtActiveClear = _RosMgmtAlarmMgmtActiveClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 6),
    _RosMgmtAlarmMgmtActiveClear_Type()
)
rosMgmtAlarmMgmtActiveClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtActiveClear.setStatus("current")


class _RosMgmtAlarmMgmtMonitorLevel_Type(Integer32):
    """Custom type rosMgmtAlarmMgmtMonitorLevel based on Integer32"""
    defaultValue = 5

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
        *(("clear", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_RosMgmtAlarmMgmtMonitorLevel_Type.__name__ = "Integer32"
_RosMgmtAlarmMgmtMonitorLevel_Object = MibScalar
rosMgmtAlarmMgmtMonitorLevel = _RosMgmtAlarmMgmtMonitorLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 7),
    _RosMgmtAlarmMgmtMonitorLevel_Type()
)
rosMgmtAlarmMgmtMonitorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtMonitorLevel.setStatus("current")


class _RosMgmtAlarmMgmtClearLevel_Type(Integer32):
    """Custom type rosMgmtAlarmMgmtClearLevel based on Integer32"""
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
        *(("clear", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_RosMgmtAlarmMgmtClearLevel_Type.__name__ = "Integer32"
_RosMgmtAlarmMgmtClearLevel_Object = MibScalar
rosMgmtAlarmMgmtClearLevel = _RosMgmtAlarmMgmtClearLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 8),
    _RosMgmtAlarmMgmtClearLevel_Type()
)
rosMgmtAlarmMgmtClearLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtClearLevel.setStatus("current")


class _RosMgmtAlarmMgmtMonitor_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtMonitor based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtMonitor_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtMonitor_Object = MibScalar
rosMgmtAlarmMgmtMonitor = _RosMgmtAlarmMgmtMonitor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 9),
    _RosMgmtAlarmMgmtMonitor_Type()
)
rosMgmtAlarmMgmtMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtMonitor.setStatus("current")


class _RosMgmtAlarmMgmtCorrelationInhibit_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtCorrelationInhibit based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtCorrelationInhibit_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtCorrelationInhibit_Object = MibScalar
rosMgmtAlarmMgmtCorrelationInhibit = _RosMgmtAlarmMgmtCorrelationInhibit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 10),
    _RosMgmtAlarmMgmtCorrelationInhibit_Type()
)
rosMgmtAlarmMgmtCorrelationInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCorrelationInhibit.setStatus("current")


class _RosMgmtAlarmMgmtReport_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtReport based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtReport_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtReport_Object = MibScalar
rosMgmtAlarmMgmtReport = _RosMgmtAlarmMgmtReport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 1, 11),
    _RosMgmtAlarmMgmtReport_Type()
)
rosMgmtAlarmMgmtReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtReport.setStatus("current")
_RosMgmtAlarmMgmtConfigTable_Object = MibTable
rosMgmtAlarmMgmtConfigTable = _RosMgmtAlarmMgmtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2)
)
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtConfigTable.setStatus("current")
_RosMgmtAlarmMgmtConfigEntry_Object = MibTableRow
rosMgmtAlarmMgmtConfigEntry = _RosMgmtAlarmMgmtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1)
)
rosMgmtAlarmMgmtConfigEntry.setIndexNames(
    (0, "ROSMGMT-ALARM-MGMT-MIB", "rosMgmtAlarmMgmtId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtConfigEntry.setStatus("current")
_RosMgmtAlarmMgmtId_Type = Unsigned32
_RosMgmtAlarmMgmtId_Object = MibTableColumn
rosMgmtAlarmMgmtId = _RosMgmtAlarmMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1, 1),
    _RosMgmtAlarmMgmtId_Type()
)
rosMgmtAlarmMgmtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtId.setStatus("current")


class _RosMgmtAlarmMgmtClear_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtClear based on TruthValue"""
    defaultValue = 2


_RosMgmtAlarmMgmtClear_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtClear_Object = MibTableColumn
rosMgmtAlarmMgmtClear = _RosMgmtAlarmMgmtClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1, 2),
    _RosMgmtAlarmMgmtClear_Type()
)
rosMgmtAlarmMgmtClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtClear.setStatus("current")


class _RosMgmtAlarmMgmtReportEnable_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtReportEnable based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtReportEnable_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtReportEnable_Object = MibTableColumn
rosMgmtAlarmMgmtReportEnable = _RosMgmtAlarmMgmtReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1, 3),
    _RosMgmtAlarmMgmtReportEnable_Type()
)
rosMgmtAlarmMgmtReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtReportEnable.setStatus("current")


class _RosMgmtAlarmMgmtMonitorEnable_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtMonitorEnable based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtMonitorEnable_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtMonitorEnable_Object = MibTableColumn
rosMgmtAlarmMgmtMonitorEnable = _RosMgmtAlarmMgmtMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1, 4),
    _RosMgmtAlarmMgmtMonitorEnable_Type()
)
rosMgmtAlarmMgmtMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtMonitorEnable.setStatus("current")


class _RosMgmtAlarmMgmtInverseMode_Type(AlarmInverseMode):
    """Custom type rosMgmtAlarmMgmtInverseMode based on AlarmInverseMode"""
    defaultValue = 1


_RosMgmtAlarmMgmtInverseMode_Type.__name__ = "AlarmInverseMode"
_RosMgmtAlarmMgmtInverseMode_Object = MibTableColumn
rosMgmtAlarmMgmtInverseMode = _RosMgmtAlarmMgmtInverseMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1, 5),
    _RosMgmtAlarmMgmtInverseMode_Type()
)
rosMgmtAlarmMgmtInverseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtInverseMode.setStatus("current")


class _RosMgmtAlarmMgmtModuleName_Type(SnmpAdminString):
    """Custom type rosMgmtAlarmMgmtModuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RosMgmtAlarmMgmtModuleName_Type.__name__ = "SnmpAdminString"
_RosMgmtAlarmMgmtModuleName_Object = MibTableColumn
rosMgmtAlarmMgmtModuleName = _RosMgmtAlarmMgmtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1, 6),
    _RosMgmtAlarmMgmtModuleName_Type()
)
rosMgmtAlarmMgmtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtModuleName.setStatus("current")


class _RosMgmtAlarmMgmtGroupName_Type(SnmpAdminString):
    """Custom type rosMgmtAlarmMgmtGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RosMgmtAlarmMgmtGroupName_Type.__name__ = "SnmpAdminString"
_RosMgmtAlarmMgmtGroupName_Object = MibTableColumn
rosMgmtAlarmMgmtGroupName = _RosMgmtAlarmMgmtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 2, 1, 7),
    _RosMgmtAlarmMgmtGroupName_Type()
)
rosMgmtAlarmMgmtGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtGroupName.setStatus("current")
_RosMgmtAlarmMgmtCfgTable_Object = MibTable
rosMgmtAlarmMgmtCfgTable = _RosMgmtAlarmMgmtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3)
)
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgTable.setStatus("current")
_RosMgmtAlarmMgmtCfgEntry_Object = MibTableRow
rosMgmtAlarmMgmtCfgEntry = _RosMgmtAlarmMgmtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1)
)
rosMgmtAlarmMgmtCfgEntry.setIndexNames(
    (0, "ROSMGMT-ALARM-MGMT-MIB", "rosMgmtAlarmMgmtCfgAlarmType"),
    (0, "ROSMGMT-ALARM-MGMT-MIB", "rosMgmtAlarmMgmtCfgAlarmResType"),
    (0, "ROSMGMT-ALARM-MGMT-MIB", "rosMgmtAlarmMgmtCfgAlarmRes"),
)
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgEntry.setStatus("current")
_RosMgmtAlarmMgmtCfgAlarmType_Type = Unsigned32
_RosMgmtAlarmMgmtCfgAlarmType_Object = MibTableColumn
rosMgmtAlarmMgmtCfgAlarmType = _RosMgmtAlarmMgmtCfgAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1, 1),
    _RosMgmtAlarmMgmtCfgAlarmType_Type()
)
rosMgmtAlarmMgmtCfgAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgAlarmType.setStatus("current")


class _RosMgmtAlarmMgmtCfgAlarmResType_Type(Integer32):
    """Custom type rosMgmtAlarmMgmtCfgAlarmResType based on Integer32"""
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
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("slotindex", 1),
          ("pwindex", 2),
          ("lspindex", 3),
          ("loifindex", 4),
          ("agifindex", 5),
          ("apifindex", 6),
          ("obifindex", 7),
          ("tdmifindex", 8),
          ("tunnelifindex", 9),
          ("vlanifindex", 10),
          ("subifindex", 11),
          ("portindex", 12),
          ("apagsubifindex", 13),
          ("powerindex", 14),
          ("fanindex", 15),
          ("boardindex", 16),
          ("cfmindex", 17),
          ("erpsindex", 18),
          ("apsindex", 19),
          ("bfdindex", 20),
          ("ldpindex", 21),
          ("lsaindex", 22),
          ("ifindex", 23),
          ("cpuindex", 24),
          ("tdmsubifindex", 25),
          ("tdmtdmsubifindex", 26),
          ("stmifindex", 27),
          ("stmsubifindex", 28),
          ("stmsubtdmtdmsubindex", 29),
          ("stmvcindex", 30),
          ("eponifindex", 31),
          ("eonuifindex", 32),
          ("eonusubifindex", 33),
          ("apeponifindex", 34),
          ("apagvlansubifindex", 35))
    )


_RosMgmtAlarmMgmtCfgAlarmResType_Type.__name__ = "Integer32"
_RosMgmtAlarmMgmtCfgAlarmResType_Object = MibTableColumn
rosMgmtAlarmMgmtCfgAlarmResType = _RosMgmtAlarmMgmtCfgAlarmResType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1, 2),
    _RosMgmtAlarmMgmtCfgAlarmResType_Type()
)
rosMgmtAlarmMgmtCfgAlarmResType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgAlarmResType.setStatus("current")
_RosMgmtAlarmMgmtCfgAlarmRes_Type = Unsigned32
_RosMgmtAlarmMgmtCfgAlarmRes_Object = MibTableColumn
rosMgmtAlarmMgmtCfgAlarmRes = _RosMgmtAlarmMgmtCfgAlarmRes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1, 3),
    _RosMgmtAlarmMgmtCfgAlarmRes_Type()
)
rosMgmtAlarmMgmtCfgAlarmRes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgAlarmRes.setStatus("current")


class _RosMgmtAlarmMgmtCfgClear_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtCfgClear based on TruthValue"""
    defaultValue = 2


_RosMgmtAlarmMgmtCfgClear_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtCfgClear_Object = MibTableColumn
rosMgmtAlarmMgmtCfgClear = _RosMgmtAlarmMgmtCfgClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1, 4),
    _RosMgmtAlarmMgmtCfgClear_Type()
)
rosMgmtAlarmMgmtCfgClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgClear.setStatus("current")


class _RosMgmtAlarmMgmtCfgMonitorEnable_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtCfgMonitorEnable based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtCfgMonitorEnable_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtCfgMonitorEnable_Object = MibTableColumn
rosMgmtAlarmMgmtCfgMonitorEnable = _RosMgmtAlarmMgmtCfgMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1, 5),
    _RosMgmtAlarmMgmtCfgMonitorEnable_Type()
)
rosMgmtAlarmMgmtCfgMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgMonitorEnable.setStatus("current")


class _RosMgmtAlarmMgmtCfgReportEnable_Type(TruthValue):
    """Custom type rosMgmtAlarmMgmtCfgReportEnable based on TruthValue"""
    defaultValue = 1


_RosMgmtAlarmMgmtCfgReportEnable_Type.__name__ = "TruthValue"
_RosMgmtAlarmMgmtCfgReportEnable_Object = MibTableColumn
rosMgmtAlarmMgmtCfgReportEnable = _RosMgmtAlarmMgmtCfgReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1, 6),
    _RosMgmtAlarmMgmtCfgReportEnable_Type()
)
rosMgmtAlarmMgmtCfgReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgReportEnable.setStatus("current")


class _RosMgmtAlarmMgmtCfgInverseMode_Type(AlarmInverseMode):
    """Custom type rosMgmtAlarmMgmtCfgInverseMode based on AlarmInverseMode"""
    defaultValue = 1


_RosMgmtAlarmMgmtCfgInverseMode_Type.__name__ = "AlarmInverseMode"
_RosMgmtAlarmMgmtCfgInverseMode_Object = MibTableColumn
rosMgmtAlarmMgmtCfgInverseMode = _RosMgmtAlarmMgmtCfgInverseMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 34, 1, 3, 1, 7),
    _RosMgmtAlarmMgmtCfgInverseMode_Type()
)
rosMgmtAlarmMgmtCfgInverseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAlarmMgmtCfgInverseMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROSMGMT-ALARM-MGMT-MIB",
    **{"AlarmStorageMode": AlarmStorageMode,
       "AlarmInverseMode": AlarmInverseMode,
       "rosMgmtAlarmMgmt": rosMgmtAlarmMgmt,
       "rosMgmtAlarmMgmtObejcts": rosMgmtAlarmMgmtObejcts,
       "rosMgmtAlarmMgmtScalarGroup": rosMgmtAlarmMgmtScalarGroup,
       "rosMgmtAlarmMgmtRaiseDelay": rosMgmtAlarmMgmtRaiseDelay,
       "rosMgmtAlarmMgmtClearDelay": rosMgmtAlarmMgmtClearDelay,
       "rosMgmtAlarmMgmtActiveStoreMode": rosMgmtAlarmMgmtActiveStoreMode,
       "rosMgmtAlarmMgmtInhibitEnable": rosMgmtAlarmMgmtInhibitEnable,
       "rosMgmtAlarmMgmtSyslogEnable": rosMgmtAlarmMgmtSyslogEnable,
       "rosMgmtAlarmMgmtActiveClear": rosMgmtAlarmMgmtActiveClear,
       "rosMgmtAlarmMgmtMonitorLevel": rosMgmtAlarmMgmtMonitorLevel,
       "rosMgmtAlarmMgmtClearLevel": rosMgmtAlarmMgmtClearLevel,
       "rosMgmtAlarmMgmtMonitor": rosMgmtAlarmMgmtMonitor,
       "rosMgmtAlarmMgmtCorrelationInhibit": rosMgmtAlarmMgmtCorrelationInhibit,
       "rosMgmtAlarmMgmtReport": rosMgmtAlarmMgmtReport,
       "rosMgmtAlarmMgmtConfigTable": rosMgmtAlarmMgmtConfigTable,
       "rosMgmtAlarmMgmtConfigEntry": rosMgmtAlarmMgmtConfigEntry,
       "rosMgmtAlarmMgmtId": rosMgmtAlarmMgmtId,
       "rosMgmtAlarmMgmtClear": rosMgmtAlarmMgmtClear,
       "rosMgmtAlarmMgmtReportEnable": rosMgmtAlarmMgmtReportEnable,
       "rosMgmtAlarmMgmtMonitorEnable": rosMgmtAlarmMgmtMonitorEnable,
       "rosMgmtAlarmMgmtInverseMode": rosMgmtAlarmMgmtInverseMode,
       "rosMgmtAlarmMgmtModuleName": rosMgmtAlarmMgmtModuleName,
       "rosMgmtAlarmMgmtGroupName": rosMgmtAlarmMgmtGroupName,
       "rosMgmtAlarmMgmtCfgTable": rosMgmtAlarmMgmtCfgTable,
       "rosMgmtAlarmMgmtCfgEntry": rosMgmtAlarmMgmtCfgEntry,
       "rosMgmtAlarmMgmtCfgAlarmType": rosMgmtAlarmMgmtCfgAlarmType,
       "rosMgmtAlarmMgmtCfgAlarmResType": rosMgmtAlarmMgmtCfgAlarmResType,
       "rosMgmtAlarmMgmtCfgAlarmRes": rosMgmtAlarmMgmtCfgAlarmRes,
       "rosMgmtAlarmMgmtCfgClear": rosMgmtAlarmMgmtCfgClear,
       "rosMgmtAlarmMgmtCfgMonitorEnable": rosMgmtAlarmMgmtCfgMonitorEnable,
       "rosMgmtAlarmMgmtCfgReportEnable": rosMgmtAlarmMgmtCfgReportEnable,
       "rosMgmtAlarmMgmtCfgInverseMode": rosMgmtAlarmMgmtCfgInverseMode}
)
