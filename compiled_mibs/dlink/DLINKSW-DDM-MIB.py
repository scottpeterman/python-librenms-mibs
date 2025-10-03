# SNMP MIB module (DLINKSW-DDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DDM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:47 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72)
)
if mibBuilder.loadTexts:
    dlinkSwDdmMIB.setRevisions(
        ("2013-02-04 00:00",
         "2013-09-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlinkThresholdState(TextualConvention, Integer32):
    status = "current"
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
        *(("normal", 0),
          ("higherAlarm", 1),
          ("higherWarning", 2),
          ("lowerWarning", 3),
          ("lowerAlarm", 4))
    )



# MIB Managed Objects in the order of their OIDs

_DDdmMIBNotifications_ObjectIdentity = ObjectIdentity
dDdmMIBNotifications = _DDdmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 0)
)
_DDdmMIBObjects_ObjectIdentity = ObjectIdentity
dDdmMIBObjects = _DDdmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1)
)
_DDdmCtrl_ObjectIdentity = ObjectIdentity
dDdmCtrl = _DDdmCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 1)
)


class _DDdmNotifyEnable_Type(Bits):
    """Custom type dDdmNotifyEnable based on Bits"""
    namedValues = NamedValues(
        *(("alarm", 0),
          ("warning", 1))
    )

_DDdmNotifyEnable_Type.__name__ = "Bits"
_DDdmNotifyEnable_Object = MibScalar
dDdmNotifyEnable = _DDdmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 1, 1),
    _DDdmNotifyEnable_Type()
)
dDdmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDdmNotifyEnable.setStatus("current")
_DDdmIfCtrl_ObjectIdentity = ObjectIdentity
dDdmIfCtrl = _DDdmIfCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 2)
)
_DDdmIfCfgTable_Object = MibTable
dDdmIfCfgTable = _DDdmIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dDdmIfCfgTable.setStatus("current")
_DDdmIfCfgEntry_Object = MibTableRow
dDdmIfCfgEntry = _DDdmIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 2, 1, 1)
)
dDdmIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDdmIfCfgEntry.setStatus("current")
_DDdmIfCfgEnabled_Type = TruthValue
_DDdmIfCfgEnabled_Object = MibTableColumn
dDdmIfCfgEnabled = _DDdmIfCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 2, 1, 1, 1),
    _DDdmIfCfgEnabled_Type()
)
dDdmIfCfgEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDdmIfCfgEnabled.setStatus("current")


class _DDdmShutdownLevel_Type(Integer32):
    """Custom type dDdmShutdownLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("alarm", 2),
          ("warning", 3))
    )


_DDdmShutdownLevel_Type.__name__ = "Integer32"
_DDdmShutdownLevel_Object = MibTableColumn
dDdmShutdownLevel = _DDdmShutdownLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 2, 1, 1, 2),
    _DDdmShutdownLevel_Type()
)
dDdmShutdownLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDdmShutdownLevel.setStatus("current")
_DDdmThresholdMgmt_ObjectIdentity = ObjectIdentity
dDdmThresholdMgmt = _DDdmThresholdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 3)
)
_DDdmThresholdCfgTable_Object = MibTable
dDdmThresholdCfgTable = _DDdmThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dDdmThresholdCfgTable.setStatus("current")
_DDdmThresholdCfgEntry_Object = MibTableRow
dDdmThresholdCfgEntry = _DDdmThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 3, 1, 1)
)
dDdmThresholdCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLINKSW-DDM-MIB", "dDdmThresholdComponent"),
    (0, "DLINKSW-DDM-MIB", "dDmThresholdAbnormalLevel"),
)
if mibBuilder.loadTexts:
    dDdmThresholdCfgEntry.setStatus("current")


class _DDdmThresholdComponent_Type(Integer32):
    """Custom type dDdmThresholdComponent based on Integer32"""
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
        *(("temperature", 1),
          ("voltage", 2),
          ("biasCurrent", 3),
          ("txPowerMw", 4),
          ("txPowerDbm", 5),
          ("rxPowerMw", 6),
          ("rxPowerDbm", 7))
    )


_DDdmThresholdComponent_Type.__name__ = "Integer32"
_DDdmThresholdComponent_Object = MibTableColumn
dDdmThresholdComponent = _DDdmThresholdComponent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 3, 1, 1, 1),
    _DDdmThresholdComponent_Type()
)
dDdmThresholdComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDdmThresholdComponent.setStatus("current")


class _DDmThresholdAbnormalLevel_Type(Integer32):
    """Custom type dDmThresholdAbnormalLevel based on Integer32"""
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
        *(("highAlarm", 1),
          ("highWarning", 2),
          ("lowWarning", 3),
          ("lowAlarm", 4))
    )


_DDmThresholdAbnormalLevel_Type.__name__ = "Integer32"
_DDmThresholdAbnormalLevel_Object = MibTableColumn
dDmThresholdAbnormalLevel = _DDmThresholdAbnormalLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 3, 1, 1, 2),
    _DDmThresholdAbnormalLevel_Type()
)
dDmThresholdAbnormalLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDmThresholdAbnormalLevel.setStatus("current")
_DDdmThresholdCfgValue_Type = Integer32
_DDdmThresholdCfgValue_Object = MibTableColumn
dDdmThresholdCfgValue = _DDdmThresholdCfgValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 3, 1, 1, 3),
    _DDdmThresholdCfgValue_Type()
)
dDdmThresholdCfgValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDdmThresholdCfgValue.setStatus("current")
_DDdmThresholdCfgRowStatus_Type = RowStatus
_DDdmThresholdCfgRowStatus_Object = MibTableColumn
dDdmThresholdCfgRowStatus = _DDdmThresholdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 3, 1, 1, 4),
    _DDdmThresholdCfgRowStatus_Type()
)
dDdmThresholdCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDdmThresholdCfgRowStatus.setStatus("current")
_DDdmInfo_ObjectIdentity = ObjectIdentity
dDdmInfo = _DDdmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4)
)
_DDdmIfInfoTable_Object = MibTable
dDdmIfInfoTable = _DDdmIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dDdmIfInfoTable.setStatus("current")
_DDdmIfInfoEntry_Object = MibTableRow
dDdmIfInfoEntry = _DDdmIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1)
)
dDdmIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDdmIfInfoEntry.setStatus("current")
_DDdmIfInfoCurrentTemperature_Type = Integer32
_DDdmIfInfoCurrentTemperature_Object = MibTableColumn
dDdmIfInfoCurrentTemperature = _DDdmIfInfoCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 1),
    _DDdmIfInfoCurrentTemperature_Type()
)
dDdmIfInfoCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentTemperature.setUnits("milli-degrees Celsius")
_DDdmIfInfoTemperatureState_Type = DlinkThresholdState
_DDdmIfInfoTemperatureState_Object = MibTableColumn
dDdmIfInfoTemperatureState = _DDdmIfInfoTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 2),
    _DDdmIfInfoTemperatureState_Type()
)
dDdmIfInfoTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoTemperatureState.setStatus("current")
_DDdmIfInfoHighAlarmTemperature_Type = Integer32
_DDdmIfInfoHighAlarmTemperature_Object = MibTableColumn
dDdmIfInfoHighAlarmTemperature = _DDdmIfInfoHighAlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 3),
    _DDdmIfInfoHighAlarmTemperature_Type()
)
dDdmIfInfoHighAlarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmTemperature.setUnits("milli-degrees Celsius")
_DDdmIfInfoHighWarnTemperature_Type = Integer32
_DDdmIfInfoHighWarnTemperature_Object = MibTableColumn
dDdmIfInfoHighWarnTemperature = _DDdmIfInfoHighWarnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 4),
    _DDdmIfInfoHighWarnTemperature_Type()
)
dDdmIfInfoHighWarnTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnTemperature.setUnits("milli-degrees Celsius")
_DDdmIfInfoLowWarnTemperature_Type = Integer32
_DDdmIfInfoLowWarnTemperature_Object = MibTableColumn
dDdmIfInfoLowWarnTemperature = _DDdmIfInfoLowWarnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 5),
    _DDdmIfInfoLowWarnTemperature_Type()
)
dDdmIfInfoLowWarnTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnTemperature.setUnits("milli-degrees Celsius")
_DDdmIfInfoLowAlarmTemperature_Type = Integer32
_DDdmIfInfoLowAlarmTemperature_Object = MibTableColumn
dDdmIfInfoLowAlarmTemperature = _DDdmIfInfoLowAlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 6),
    _DDdmIfInfoLowAlarmTemperature_Type()
)
dDdmIfInfoLowAlarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmTemperature.setUnits("milli-degrees Celsius")
_DDdmIfInfoCurrentVoltage_Type = Integer32
_DDdmIfInfoCurrentVoltage_Object = MibTableColumn
dDdmIfInfoCurrentVoltage = _DDdmIfInfoCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 7),
    _DDdmIfInfoCurrentVoltage_Type()
)
dDdmIfInfoCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentVoltage.setUnits("centi-Volt")
_DDdmIfInfoVoltageState_Type = DlinkThresholdState
_DDdmIfInfoVoltageState_Object = MibTableColumn
dDdmIfInfoVoltageState = _DDdmIfInfoVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 8),
    _DDdmIfInfoVoltageState_Type()
)
dDdmIfInfoVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoVoltageState.setStatus("current")
_DDdmIfInfoHighAlarmVoltage_Type = Integer32
_DDdmIfInfoHighAlarmVoltage_Object = MibTableColumn
dDdmIfInfoHighAlarmVoltage = _DDdmIfInfoHighAlarmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 9),
    _DDdmIfInfoHighAlarmVoltage_Type()
)
dDdmIfInfoHighAlarmVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmVoltage.setUnits("centi-Volt")
_DDdmIfInfoHighWarnVoltage_Type = Integer32
_DDdmIfInfoHighWarnVoltage_Object = MibTableColumn
dDdmIfInfoHighWarnVoltage = _DDdmIfInfoHighWarnVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 10),
    _DDdmIfInfoHighWarnVoltage_Type()
)
dDdmIfInfoHighWarnVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnVoltage.setUnits("centi-Volt")
_DDdmIfInfoLowWarnVoltage_Type = Integer32
_DDdmIfInfoLowWarnVoltage_Object = MibTableColumn
dDdmIfInfoLowWarnVoltage = _DDdmIfInfoLowWarnVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 11),
    _DDdmIfInfoLowWarnVoltage_Type()
)
dDdmIfInfoLowWarnVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnVoltage.setUnits("centi-Volt")
_DDdmIfInfoLowAlarmVoltage_Type = Integer32
_DDdmIfInfoLowAlarmVoltage_Object = MibTableColumn
dDdmIfInfoLowAlarmVoltage = _DDdmIfInfoLowAlarmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 12),
    _DDdmIfInfoLowAlarmVoltage_Type()
)
dDdmIfInfoLowAlarmVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmVoltage.setUnits("centi-Volt")
_DDdmIfInfoCurrentBiasCurrent_Type = Integer32
_DDdmIfInfoCurrentBiasCurrent_Object = MibTableColumn
dDdmIfInfoCurrentBiasCurrent = _DDdmIfInfoCurrentBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 13),
    _DDdmIfInfoCurrentBiasCurrent_Type()
)
dDdmIfInfoCurrentBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentBiasCurrent.setUnits("milli-amperes")
_DDdmIfInfoBiasCurrentState_Type = DlinkThresholdState
_DDdmIfInfoBiasCurrentState_Object = MibTableColumn
dDdmIfInfoBiasCurrentState = _DDdmIfInfoBiasCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 14),
    _DDdmIfInfoBiasCurrentState_Type()
)
dDdmIfInfoBiasCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoBiasCurrentState.setStatus("current")
_DDdmIfInfoHighAlarmBiasCurrent_Type = Integer32
_DDdmIfInfoHighAlarmBiasCurrent_Object = MibTableColumn
dDdmIfInfoHighAlarmBiasCurrent = _DDdmIfInfoHighAlarmBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 15),
    _DDdmIfInfoHighAlarmBiasCurrent_Type()
)
dDdmIfInfoHighAlarmBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmBiasCurrent.setUnits("milli-amperes")
_DDdmIfInfoHighWarnBiasCurrent_Type = Integer32
_DDdmIfInfoHighWarnBiasCurrent_Object = MibTableColumn
dDdmIfInfoHighWarnBiasCurrent = _DDdmIfInfoHighWarnBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 16),
    _DDdmIfInfoHighWarnBiasCurrent_Type()
)
dDdmIfInfoHighWarnBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnBiasCurrent.setUnits("milli-amperes")
_DDdmIfInfoLowWarnBiasCurrent_Type = Integer32
_DDdmIfInfoLowWarnBiasCurrent_Object = MibTableColumn
dDdmIfInfoLowWarnBiasCurrent = _DDdmIfInfoLowWarnBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 17),
    _DDdmIfInfoLowWarnBiasCurrent_Type()
)
dDdmIfInfoLowWarnBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnBiasCurrent.setUnits("milli-amperes")
_DDdmIfInfoLowAlarmBiasCurrent_Type = Integer32
_DDdmIfInfoLowAlarmBiasCurrent_Object = MibTableColumn
dDdmIfInfoLowAlarmBiasCurrent = _DDdmIfInfoLowAlarmBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 18),
    _DDdmIfInfoLowAlarmBiasCurrent_Type()
)
dDdmIfInfoLowAlarmBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmBiasCurrent.setUnits("milli-amperes")
_DDdmIfInfoCurrentTxPower_Type = Integer32
_DDdmIfInfoCurrentTxPower_Object = MibTableColumn
dDdmIfInfoCurrentTxPower = _DDdmIfInfoCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 19),
    _DDdmIfInfoCurrentTxPower_Type()
)
dDdmIfInfoCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentTxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoTxPowerState_Type = DlinkThresholdState
_DDdmIfInfoTxPowerState_Object = MibTableColumn
dDdmIfInfoTxPowerState = _DDdmIfInfoTxPowerState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 20),
    _DDdmIfInfoTxPowerState_Type()
)
dDdmIfInfoTxPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoTxPowerState.setStatus("current")
_DDdmIfInfoHighAlarmTxPower_Type = Integer32
_DDdmIfInfoHighAlarmTxPower_Object = MibTableColumn
dDdmIfInfoHighAlarmTxPower = _DDdmIfInfoHighAlarmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 21),
    _DDdmIfInfoHighAlarmTxPower_Type()
)
dDdmIfInfoHighAlarmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmTxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoHighWarnTxPower_Type = Integer32
_DDdmIfInfoHighWarnTxPower_Object = MibTableColumn
dDdmIfInfoHighWarnTxPower = _DDdmIfInfoHighWarnTxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 22),
    _DDdmIfInfoHighWarnTxPower_Type()
)
dDdmIfInfoHighWarnTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnTxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoLowWarnTxPower_Type = Integer32
_DDdmIfInfoLowWarnTxPower_Object = MibTableColumn
dDdmIfInfoLowWarnTxPower = _DDdmIfInfoLowWarnTxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 23),
    _DDdmIfInfoLowWarnTxPower_Type()
)
dDdmIfInfoLowWarnTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnTxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoLowAlarmTxPower_Type = Integer32
_DDdmIfInfoLowAlarmTxPower_Object = MibTableColumn
dDdmIfInfoLowAlarmTxPower = _DDdmIfInfoLowAlarmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 24),
    _DDdmIfInfoLowAlarmTxPower_Type()
)
dDdmIfInfoLowAlarmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmTxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoCurrentRxPower_Type = Integer32
_DDdmIfInfoCurrentRxPower_Object = MibTableColumn
dDdmIfInfoCurrentRxPower = _DDdmIfInfoCurrentRxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 25),
    _DDdmIfInfoCurrentRxPower_Type()
)
dDdmIfInfoCurrentRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentRxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoCurrentRxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoRxPowerState_Type = DlinkThresholdState
_DDdmIfInfoRxPowerState_Object = MibTableColumn
dDdmIfInfoRxPowerState = _DDdmIfInfoRxPowerState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 26),
    _DDdmIfInfoRxPowerState_Type()
)
dDdmIfInfoRxPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoRxPowerState.setStatus("current")
_DDdmIfInfoHighAlarmRxPower_Type = Integer32
_DDdmIfInfoHighAlarmRxPower_Object = MibTableColumn
dDdmIfInfoHighAlarmRxPower = _DDdmIfInfoHighAlarmRxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 27),
    _DDdmIfInfoHighAlarmRxPower_Type()
)
dDdmIfInfoHighAlarmRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmRxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighAlarmRxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoHighWarnRxPower_Type = Integer32
_DDdmIfInfoHighWarnRxPower_Object = MibTableColumn
dDdmIfInfoHighWarnRxPower = _DDdmIfInfoHighWarnRxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 28),
    _DDdmIfInfoHighWarnRxPower_Type()
)
dDdmIfInfoHighWarnRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnRxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoHighWarnRxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoLowWarnRxPower_Type = Integer32
_DDdmIfInfoLowWarnRxPower_Object = MibTableColumn
dDdmIfInfoLowWarnRxPower = _DDdmIfInfoLowWarnRxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 29),
    _DDdmIfInfoLowWarnRxPower_Type()
)
dDdmIfInfoLowWarnRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnRxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowWarnRxPower.setUnits("tenths of a microwatt")
_DDdmIfInfoLowAlarmRxPower_Type = Integer32
_DDdmIfInfoLowAlarmRxPower_Object = MibTableColumn
dDdmIfInfoLowAlarmRxPower = _DDdmIfInfoLowAlarmRxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 4, 1, 1, 30),
    _DDdmIfInfoLowAlarmRxPower_Type()
)
dDdmIfInfoLowAlarmRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmRxPower.setStatus("current")
if mibBuilder.loadTexts:
    dDdmIfInfoLowAlarmRxPower.setUnits("tenths of a microwatt")
_DDdmNotifyInfo_ObjectIdentity = ObjectIdentity
dDdmNotifyInfo = _DDdmNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 5)
)
_DDdmNotifyInfoIfIndex_Type = InterfaceIndex
_DDdmNotifyInfoIfIndex_Object = MibScalar
dDdmNotifyInfoIfIndex = _DDdmNotifyInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 5, 1),
    _DDdmNotifyInfoIfIndex_Type()
)
dDdmNotifyInfoIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dDdmNotifyInfoIfIndex.setStatus("current")


class _DDdmNotifyInfoComponent_Type(Integer32):
    """Custom type dDdmNotifyInfoComponent based on Integer32"""
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
        *(("temperature", 1),
          ("voltage", 2),
          ("biasCurrent", 3),
          ("txPowerMw", 4),
          ("rxPowerMw", 5))
    )


_DDdmNotifyInfoComponent_Type.__name__ = "Integer32"
_DDdmNotifyInfoComponent_Object = MibScalar
dDdmNotifyInfoComponent = _DDdmNotifyInfoComponent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 5, 2),
    _DDdmNotifyInfoComponent_Type()
)
dDdmNotifyInfoComponent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dDdmNotifyInfoComponent.setStatus("current")


class _DDdmNotifyInfoAbnormalLevel_Type(Integer32):
    """Custom type dDdmNotifyInfoAbnormalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_DDdmNotifyInfoAbnormalLevel_Type.__name__ = "Integer32"
_DDdmNotifyInfoAbnormalLevel_Object = MibScalar
dDdmNotifyInfoAbnormalLevel = _DDdmNotifyInfoAbnormalLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 5, 3),
    _DDdmNotifyInfoAbnormalLevel_Type()
)
dDdmNotifyInfoAbnormalLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dDdmNotifyInfoAbnormalLevel.setStatus("current")


class _DDdmNotifyInfoThresholdExceedOrRecover_Type(Integer32):
    """Custom type dDdmNotifyInfoThresholdExceedOrRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exceed", 1),
          ("recover", 2))
    )


_DDdmNotifyInfoThresholdExceedOrRecover_Type.__name__ = "Integer32"
_DDdmNotifyInfoThresholdExceedOrRecover_Object = MibScalar
dDdmNotifyInfoThresholdExceedOrRecover = _DDdmNotifyInfoThresholdExceedOrRecover_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 1, 5, 4),
    _DDdmNotifyInfoThresholdExceedOrRecover_Type()
)
dDdmNotifyInfoThresholdExceedOrRecover.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dDdmNotifyInfoThresholdExceedOrRecover.setStatus("current")
_DDdmMIBConformance_ObjectIdentity = ObjectIdentity
dDdmMIBConformance = _DDdmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 2)
)
_DDdmCompliances_ObjectIdentity = ObjectIdentity
dDdmCompliances = _DDdmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 2, 1)
)
_DDdmGroups_ObjectIdentity = ObjectIdentity
dDdmGroups = _DDdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 2, 2)
)

# Managed Objects groups

dDdmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 2, 2, 1)
)
dDdmInfoGroup.setObjects(
      *(("DLINKSW-DDM-MIB", "dDdmIfInfoCurrentTemperature"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoTemperatureState"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighAlarmTemperature"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighWarnTemperature"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowWarnTemperature"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowAlarmTemperature"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoCurrentVoltage"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoVoltageState"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighAlarmVoltage"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighWarnVoltage"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowWarnVoltage"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowAlarmVoltage"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoCurrentBiasCurrent"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoBiasCurrentState"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighAlarmBiasCurrent"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighWarnBiasCurrent"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowWarnBiasCurrent"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowAlarmBiasCurrent"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoCurrentTxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoTxPowerState"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighAlarmTxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighWarnTxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowWarnTxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowAlarmTxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoCurrentRxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoRxPowerState"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighAlarmRxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoHighWarnRxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowWarnRxPower"),
        ("DLINKSW-DDM-MIB", "dDdmIfInfoLowAlarmRxPower"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoIfIndex"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoComponent"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoAbnormalLevel"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoThresholdExceedOrRecover"))
)
if mibBuilder.loadTexts:
    dDdmInfoGroup.setStatus("current")

dDdmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 2, 2, 2)
)
dDdmCfgGroup.setObjects(
      *(("DLINKSW-DDM-MIB", "dDdmNotifyEnable"),
        ("DLINKSW-DDM-MIB", "dDdmIfCfgEnabled"),
        ("DLINKSW-DDM-MIB", "dDdmShutdownLevel"),
        ("DLINKSW-DDM-MIB", "dDdmThresholdCfgValue"),
        ("DLINKSW-DDM-MIB", "dDdmThresholdCfgRowStatus"))
)
if mibBuilder.loadTexts:
    dDdmCfgGroup.setStatus("current")


# Notification objects

dDdmAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 0, 1)
)
dDdmAlarmTrap.setObjects(
      *(("DLINKSW-DDM-MIB", "dDdmNotifyInfoIfIndex"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoComponent"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoAbnormalLevel"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoThresholdExceedOrRecover"))
)
if mibBuilder.loadTexts:
    dDdmAlarmTrap.setStatus(
        "current"
    )

dDdmWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 0, 2)
)
dDdmWarningTrap.setObjects(
      *(("DLINKSW-DDM-MIB", "dDdmNotifyInfoIfIndex"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoComponent"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoAbnormalLevel"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyInfoThresholdExceedOrRecover"))
)
if mibBuilder.loadTexts:
    dDdmWarningTrap.setStatus(
        "current"
    )


# Notifications groups

dDdmNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 2, 2, 3)
)
dDdmNotifyGroup.setObjects(
      *(("DLINKSW-DDM-MIB", "dDdmAlarmTrap"),
        ("DLINKSW-DDM-MIB", "dDdmWarningTrap"))
)
if mibBuilder.loadTexts:
    dDdmNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dDdmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 72, 2, 1, 1)
)
dDdmCompliance.setObjects(
      *(("DLINKSW-DDM-MIB", "dDdmInfoGroup"),
        ("DLINKSW-DDM-MIB", "dDdmCfgGroup"),
        ("DLINKSW-DDM-MIB", "dDdmNotifyGroup"))
)
if mibBuilder.loadTexts:
    dDdmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DDM-MIB",
    **{"DlinkThresholdState": DlinkThresholdState,
       "dlinkSwDdmMIB": dlinkSwDdmMIB,
       "dDdmMIBNotifications": dDdmMIBNotifications,
       "dDdmAlarmTrap": dDdmAlarmTrap,
       "dDdmWarningTrap": dDdmWarningTrap,
       "dDdmMIBObjects": dDdmMIBObjects,
       "dDdmCtrl": dDdmCtrl,
       "dDdmNotifyEnable": dDdmNotifyEnable,
       "dDdmIfCtrl": dDdmIfCtrl,
       "dDdmIfCfgTable": dDdmIfCfgTable,
       "dDdmIfCfgEntry": dDdmIfCfgEntry,
       "dDdmIfCfgEnabled": dDdmIfCfgEnabled,
       "dDdmShutdownLevel": dDdmShutdownLevel,
       "dDdmThresholdMgmt": dDdmThresholdMgmt,
       "dDdmThresholdCfgTable": dDdmThresholdCfgTable,
       "dDdmThresholdCfgEntry": dDdmThresholdCfgEntry,
       "dDdmThresholdComponent": dDdmThresholdComponent,
       "dDmThresholdAbnormalLevel": dDmThresholdAbnormalLevel,
       "dDdmThresholdCfgValue": dDdmThresholdCfgValue,
       "dDdmThresholdCfgRowStatus": dDdmThresholdCfgRowStatus,
       "dDdmInfo": dDdmInfo,
       "dDdmIfInfoTable": dDdmIfInfoTable,
       "dDdmIfInfoEntry": dDdmIfInfoEntry,
       "dDdmIfInfoCurrentTemperature": dDdmIfInfoCurrentTemperature,
       "dDdmIfInfoTemperatureState": dDdmIfInfoTemperatureState,
       "dDdmIfInfoHighAlarmTemperature": dDdmIfInfoHighAlarmTemperature,
       "dDdmIfInfoHighWarnTemperature": dDdmIfInfoHighWarnTemperature,
       "dDdmIfInfoLowWarnTemperature": dDdmIfInfoLowWarnTemperature,
       "dDdmIfInfoLowAlarmTemperature": dDdmIfInfoLowAlarmTemperature,
       "dDdmIfInfoCurrentVoltage": dDdmIfInfoCurrentVoltage,
       "dDdmIfInfoVoltageState": dDdmIfInfoVoltageState,
       "dDdmIfInfoHighAlarmVoltage": dDdmIfInfoHighAlarmVoltage,
       "dDdmIfInfoHighWarnVoltage": dDdmIfInfoHighWarnVoltage,
       "dDdmIfInfoLowWarnVoltage": dDdmIfInfoLowWarnVoltage,
       "dDdmIfInfoLowAlarmVoltage": dDdmIfInfoLowAlarmVoltage,
       "dDdmIfInfoCurrentBiasCurrent": dDdmIfInfoCurrentBiasCurrent,
       "dDdmIfInfoBiasCurrentState": dDdmIfInfoBiasCurrentState,
       "dDdmIfInfoHighAlarmBiasCurrent": dDdmIfInfoHighAlarmBiasCurrent,
       "dDdmIfInfoHighWarnBiasCurrent": dDdmIfInfoHighWarnBiasCurrent,
       "dDdmIfInfoLowWarnBiasCurrent": dDdmIfInfoLowWarnBiasCurrent,
       "dDdmIfInfoLowAlarmBiasCurrent": dDdmIfInfoLowAlarmBiasCurrent,
       "dDdmIfInfoCurrentTxPower": dDdmIfInfoCurrentTxPower,
       "dDdmIfInfoTxPowerState": dDdmIfInfoTxPowerState,
       "dDdmIfInfoHighAlarmTxPower": dDdmIfInfoHighAlarmTxPower,
       "dDdmIfInfoHighWarnTxPower": dDdmIfInfoHighWarnTxPower,
       "dDdmIfInfoLowWarnTxPower": dDdmIfInfoLowWarnTxPower,
       "dDdmIfInfoLowAlarmTxPower": dDdmIfInfoLowAlarmTxPower,
       "dDdmIfInfoCurrentRxPower": dDdmIfInfoCurrentRxPower,
       "dDdmIfInfoRxPowerState": dDdmIfInfoRxPowerState,
       "dDdmIfInfoHighAlarmRxPower": dDdmIfInfoHighAlarmRxPower,
       "dDdmIfInfoHighWarnRxPower": dDdmIfInfoHighWarnRxPower,
       "dDdmIfInfoLowWarnRxPower": dDdmIfInfoLowWarnRxPower,
       "dDdmIfInfoLowAlarmRxPower": dDdmIfInfoLowAlarmRxPower,
       "dDdmNotifyInfo": dDdmNotifyInfo,
       "dDdmNotifyInfoIfIndex": dDdmNotifyInfoIfIndex,
       "dDdmNotifyInfoComponent": dDdmNotifyInfoComponent,
       "dDdmNotifyInfoAbnormalLevel": dDdmNotifyInfoAbnormalLevel,
       "dDdmNotifyInfoThresholdExceedOrRecover": dDdmNotifyInfoThresholdExceedOrRecover,
       "dDdmMIBConformance": dDdmMIBConformance,
       "dDdmCompliances": dDdmCompliances,
       "dDdmCompliance": dDdmCompliance,
       "dDdmGroups": dDdmGroups,
       "dDdmInfoGroup": dDdmInfoGroup,
       "dDdmCfgGroup": dDdmCfgGroup,
       "dDdmNotifyGroup": dDdmNotifyGroup}
)
